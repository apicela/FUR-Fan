from flask import request, jsonify, Blueprint
from services import HLTVWebScrapperService, MembersService
furia_members = Blueprint('FuriaMembersRoute', __name__)
HLTVService = HLTVWebScrapperService()
MembersService = MembersService()

@furia_members.route('/players/csgo/all', methods=['GET'])
def getAllCSGOPlayers():
    return jsonify({'message': {'data': HLTVService.get_players()}}), 200

@furia_members.route('/streamers/all', methods=['GET'])
def getAllStreamers():
    return jsonify({'message': {'data': MembersService.get_streamers()}}), 200

@furia_members.route('/creators/all', methods=['GET'])
def getAllCreators():
    return jsonify({'message': {'data': MembersService.get_creators()}}), 200

