import requests

class PandaScoreAPI:
    PANDASCORE_API_KEY = "7OPNMeLfwrqvRVn8FApN6qhn0JoCrS5HqTaM_ekvJ4m9TWERQAk"
    PANDASCORE_API_URL = " https://api.pandascore.co/csgo/"

    @staticmethod
    def get_furia_players():
        url = f"{PandaScoreAPI.PANDASCORE_API_URL}teams?filter[slug]=furia"
        headers = {
            "Authorization": f"Bearer {PandaScoreAPI.TOKEN}"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None