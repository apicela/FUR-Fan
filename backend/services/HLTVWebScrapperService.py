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
    PLAYERS_CACHE_FILE = 'players_cache.json'
    MATCHES_CACHE_FILE = 'matches_cache.json'
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

    def _load_cache(self, cache_file):
        if os.path.exists(cache_file):
            with open(cache_file, 'r') as f:
                cached = json.load(f)
                if time.time() - cached['timestamp'] < self.CACHE_TTL:
                    return cached['data']
        return None

    def _save_cache(self, data, cache_file):
        with open(cache_file, 'w') as f:
            json.dump({'timestamp': time.time(), 'data': data}, f)

    def get_players(self):
        cached_data = self._load_cache(self.PLAYERS_CACHE_FILE)
        if cached_data:
            return cached_data
        
        fresh_data = self._get_players_data()
        if fresh_data:
            self._save_cache(fresh_data, self.PLAYERS_CACHE_FILE)
        return fresh_data

    def _get_matches_data(self):
        try:
            url_with_matches = self.url + '#tab-matchesBox'
            self.driver.get(url_with_matches)

            wait = WebDriverWait(self.driver, 10)
            matches_box = wait.until(EC.presence_of_element_located((By.ID, 'matchesBox')))
            
            matches_data = {
                "upcoming": [],
                "recent": []
            }
            
            # Extrair próximos jogos
            upcoming_section = matches_box.find_element(By.XPATH, ".//h2[contains(text(), 'Upcoming matches for')]/following-sibling::table")
            
            # Pegar todos os grupos de eventos (cada um com seu header)
            upcoming_event_groups = upcoming_section.find_elements(By.XPATH, ".//thead[tr[@class='event-header-cell']]")
            
            for event_group in upcoming_event_groups:
                # Pegar nome do evento
                event_name = event_group.find_element(By.CSS_SELECTOR, "th a").text
                
                # Pegar a tabela de jogos seguinte a este header
                games_table = event_group.find_element(By.XPATH, "following-sibling::tbody")
                
                for row in games_table.find_elements(By.CSS_SELECTOR, "tr.team-row"):
                    date_element = row.find_element(By.CLASS_NAME, "date-cell")
                    date = date_element.find_element(By.TAG_NAME, "span").text
                    
                    team_cell = row.find_element(By.CLASS_NAME, "team-center-cell")
                    
                    team1 = team_cell.find_element(By.CSS_SELECTOR, ".team-flex .team-name.team-1").text
                    team2 = team_cell.find_element(By.CSS_SELECTOR, ".team-flex .team-name.team-2").text
                    
                    score_cell = team_cell.find_element(By.CLASS_NAME, "score-cell")
                    score1 = score_cell.find_element(By.CSS_SELECTOR, ".score:not(.score-divider)").text
                    score2 = score_cell.find_elements(By.CSS_SELECTOR, ".score:not(.score-divider)")[1].text
                    
                    matches_data["upcoming"].append({
                        "event": event_name,
                        "date": date,
                        "result": {
                            "furia": {
                                "name": team1,
                                "score": score1
                            },
                            "opponent": {
                                "name": team2,
                                "score": score2
                            }
                        }
                    })
            
            # Extrair resultados recentes
            recent_section = matches_box.find_element(By.XPATH, ".//h2[contains(text(), 'Recent results for')]/following-sibling::table")
            
            # Pegar todos os grupos de eventos recentes
            recent_event_groups = recent_section.find_elements(By.XPATH, ".//thead[tr[@class='event-header-cell']]")
            
            for event_group in recent_event_groups:
                # Pegar nome do evento
                event_name = event_group.find_element(By.CSS_SELECTOR, "th a").text
                
                # Pegar a tabela de jogos seguinte a este header
                games_table = event_group.find_element(By.XPATH, "following-sibling::tbody")
                
                for row in games_table.find_elements(By.CSS_SELECTOR, "tr.team-row"):
                    date_element = row.find_element(By.CLASS_NAME, "date-cell")
                    date = date_element.find_element(By.TAG_NAME, "span").text
                    
                    team_cell = row.find_element(By.CLASS_NAME, "team-center-cell")
                    
                    team1 = team_cell.find_element(By.CSS_SELECTOR, ".team-flex .team-name.team-1").text
                    team2 = team_cell.find_element(By.CSS_SELECTOR, ".team-flex .team-name.team-2").text
                    
                    score_cell = team_cell.find_element(By.CLASS_NAME, "score-cell")
                    score1 = score_cell.find_element(By.CSS_SELECTOR, ".score:not(.score-divider)").text
                    score2 = score_cell.find_elements(By.CSS_SELECTOR, ".score:not(.score-divider)")[1].text
                    
                    matches_data["recent"].append({
                        "event": event_name,
                        "date": date,
                        "result": {
                            "furia": {
                                "name": team1,
                                "score": score1
                            },
                            "opponent": {
                                "name": team2,
                                "score": score2
                            }
                        }
                    })
            
            return matches_data
            
        except Exception as e:
            print(f"Erro ao obter dados dos jogos: {e}")
            return {"upcoming": [], "recent": []}

    def get_recent_matches(self):
        cached_data = self._load_cache(self.MATCHES_CACHE_FILE)
        if cached_data:
            return cached_data
        
        fresh_data = self._get_matches_data()
        if fresh_data:
            self._save_cache(fresh_data, self.MATCHES_CACHE_FILE)
        return fresh_data

    def __del__(self):
        if hasattr(self, 'driver') and self.driver:
            self.driver.quit()