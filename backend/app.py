from flask import Flask
from routes import PlayerRoute, MatchesRoute
from flask_cors import CORS
import asyncio
import os
app = Flask(__name__)
# Configurações do Flask
app.config['FLASK_ENV'] = os.getenv('FLASK_ENV', 'development')  # Define o ambiente (development/production)
CORS(app)

app.register_blueprint(PlayerRoute.player_route)
app.register_blueprint(MatchesRoute.matches_route)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)