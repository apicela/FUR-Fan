from flask import Flask
from routes import MatchesRoute, FuriaMembersRoute, BotRoute
from flask_cors import CORS
import os
app = Flask(__name__)
# Configurações do Flask
app.config['FLASK_ENV'] = os.getenv('FLASK_ENV', 'development')  # Define o ambiente (development/production)
CORS(app)

app.register_blueprint(FuriaMembersRoute.furia_members)
app.register_blueprint(MatchesRoute.matches_route)
app.register_blueprint(BotRoute.chatbot)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)