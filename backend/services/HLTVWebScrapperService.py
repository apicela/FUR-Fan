import json
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

class HLTVWebScrapperService:
    DRIVER_PATH = os.path.join(os.getcwd(), 'chromedriver')
    CACHE_FILE = 'players_cache.json'
    CACHE_TTL = 86400  # 24 horas em segundos

    def __init__(self):
        self.driver = self._setup_selenium()
        self.url = 'https://www.hltv.org/team/8297/furia'

    @staticmethod
    def _setup_selenium():
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        return driver

    def _get_players_data(self):
        try:
            self.driver.get(self.url)
            time.sleep(3)

            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            script = soup.find('script', {'type': 'application/ld+json'})

            if not script:
                return None

            data = json.loads(script.string)
            athletes = data.get('athlete')
            coaches = data.get('coach')

            if athletes and coaches:
                return {'athletes': athletes, 'coaches': coaches}

        except Exception:
            return None

    def _load_cache(self):
        if os.path.exists(self.CACHE_FILE):
            with open(self.CACHE_FILE, 'r') as f:
                cached = json.load(f)
                if time.time() - cached['timestamp'] < self.CACHE_TTL:
                    return cached['data']
        return None

    def _save_cache(self, data):
        with open(self.CACHE_FILE, 'w') as f:
            json.dump({'timestamp': time.time(), 'data': data}, f)

    def get_players(self):
        cached_data = self._load_cache()
        if cached_data:
            return cached_data
        
        fresh_data = self._get_players_data()
        if fresh_data:
            self._save_cache(fresh_data)
        return fresh_data

    def get_recent_matches(self):
        try:
            url_with_matches = self.url + '#tab-matchesBox'
            self.driver.get(url_with_matches)

            wait = WebDriverWait(self.driver, 10)
            matches_box = wait.until(EC.presence_of_element_located((By.ID, 'matchesBox')))
            
            # Encontrar todas as tabelas de resultados recentes
            recent_results_section = matches_box.find_element(By.XPATH, ".//h2[contains(text(), 'Recent results for')]/following-sibling::table")
            
            matches = []
            
            # Iterar por cada linha de jogo
            for row in recent_results_section.find_elements(By.CSS_SELECTOR, "tbody tr.team-row"):
                # Extrair data
                date_element = row.find_element(By.CLASS_NAME, "date-cell")
                date = date_element.find_element(By.TAG_NAME, "span").text
                
                # Extrair times e resultado
                team_cell = row.find_element(By.CLASS_NAME, "team-center-cell")
                
                # Nome do time 1 (FURIA)
                team1 = team_cell.find_element(By.CSS_SELECTOR, ".team-flex .team-name.team-1").text
                
                # Nome do time 2 (oponente)
                team2 = team_cell.find_element(By.CSS_SELECTOR, ".team-flex .team-name.team-2").text
                
                # Resultado
                score_cell = team_cell.find_element(By.CLASS_NAME, "score-cell")
                score1 = score_cell.find_element(By.CSS_SELECTOR, ".score:not(.score-divider)").text
                score2 = score_cell.find_elements(By.CSS_SELECTOR, ".score:not(.score-divider)")[1].text
                
                # Determinar quem ganhou
                if "lost" in row.find_element(By.CSS_SELECTOR, ".team-flex .team-name.team-1").get_attribute("class"):
                    # FURIA perdeu
                    result = f"{team1} {score1}-{score2} {team2}"
                else:
                    # FURIA ganhou
                    result = f"{team1} {score1}-{score2} {team2}"
                
                matches.append({
                    "date": date,
                    "result": result,
                    "opponent": team2
                })
            
            return matches
            
        except Exception as e:
            print(f"Erro ao obter jogos recentes: {e}")
            return []

    def __del__(self):
        if hasattr(self, 'driver') and self.driver:
            self.driver.quit()
