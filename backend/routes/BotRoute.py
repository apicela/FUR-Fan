from flask import request, jsonify, Blueprint
from services import ChatbotService

chatbot = Blueprint('BotRoute', __name__)
chatbot_service = ChatbotService()


@chatbot.route('/chatbot/ask', methods=['POST'])
def askToIA():
    data = request.json
    message = f"Sua missão:  Você está destinado para ser o chatbot da equipe de e-sports FURIA. Caso você não entenda e não tenha a ver com o contexto, fala que não entendeu. Agora q vc sabe seu contexto,esponda a mensagem do usuário: {data.get('message')}"
    if not message:
        return jsonify({'error': 'Message is required'}), 400
    return jsonify({'message': {'data': chatbot_service.sendMessageToGemini(message=message)}}), 200