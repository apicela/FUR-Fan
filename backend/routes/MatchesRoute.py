from flask import request, jsonify, Blueprint
from services import HLTVWebScrapperService
matches_route = Blueprint('MatchesRoute', __name__)
HLTVService = HLTVWebScrapperService()
@matches_route.route('/matches/all', methods=['GET'])
def getAllFuriaPlayers():
    return jsonify({'message': {'data': HLTVService.get_recent_matches()}}), 200

