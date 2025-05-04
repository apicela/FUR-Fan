from flask import request, jsonify, Blueprint
from services import ChatbotService

chatbot = Blueprint('BotRoute', __name__)
chatbot_service = ChatbotService()


@chatbot.route('/chatbot/ask', methods=['POST'])
def askToIA():
    data = request.json
    message = f"Contexto da mensagem: Você está destinado para ser o chatbot da equipe de e-sports FURIA. Mensagem do usuário: {data.get('message')}"
    if not message:
        return jsonify({'error': 'Message is required'}), 400
    return jsonify({'message': {'data': chatbot_service.sendMessageToGemini(message=message)}}), 200