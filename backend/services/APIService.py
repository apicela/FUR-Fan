from hltv_async_api.aiohltv import Hltv

class APIService:
    FURIA_ID = 8297

    async def get_furia_matches(self):
            hltv = Hltv()
            matches = await hltv.get_best_players()
            return matches