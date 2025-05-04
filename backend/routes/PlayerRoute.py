from flask import request, jsonify, Blueprint
from services import HLTVWebScrapperService
player_route = Blueprint('PlayerRoute', __name__)
HLTVService = HLTVWebScrapperService()

@player_route.route('/players/all', methods=['GET'])
def getAllFuriaPlayers():
    return jsonify({'message': {'data': HLTVService.get_players()}}), 200

