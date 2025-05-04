import json
import os

class MembersService:
    STREAMERS_FILE = "streamers.json"
    CREATORS_FILE = "creators.json"

    def get_streamers(self):
        if os.path.exists(self.STREAMERS_FILE):
            with open(self.STREAMERS_FILE, 'r') as f:
                return json.load(f)
        return None

    def get_creators(self):
        if os.path.exists(self.CREATORS_FILE):
            with open(self.CREATORS_FILE, 'r') as f:
                return json.load(f)
        return None