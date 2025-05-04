from google import genai

class ChatbotService:
    GEMINI_API_KEY = 'AIzaSyAW8Q0whMob8YX0w3ueXhnbEkQF-6xnUNs'
    GEMINI_MODEL = 'gemini-2.5-flash-preview-04-17'

    def __init__(self):
        self.client = genai.Client(api_key=self.GEMINI_API_KEY)
        self.model = self.GEMINI_MODEL

    def sendMessageToGemini(self, message):
        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=message,
            )
            print(f"Response: {response.text}")
            return response.text
        except Exception as e:
            print(f"Error: {e}")
            return None
