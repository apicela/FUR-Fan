// src/services/botService.js

export const useBotService = () => {
    // Respostas pré-definidas do bot
    const botResponses = {
      default: "Desculpe, não entendi. Por favor, escolha uma opção de 1 a 7.",
      welcome: [
        'Olá, seja bem-vindo(a) ao chat 4fun!',
        'Digo... chat FUR FAN, como posso te ajudar hoje?',
        '1. Quem somos nós?\n2. Calendário de Jogos CSGO\n3. Acompanhe jogos ao vivo\n4. Conheça nossa Line Up de CS 🔥\n5. Lojinha da Pantera\n6. Criadores de Conteúdo e Streamers\n7. Conversar com a furIA\nDigite uma opção!'
      ],
      options: {
        '1': 'Somos a FURIA, uma organização brasileira de esportes eletrônicos fundada em 2017! 🐆',
        '2': 'Você pode conferir o calendário de jogos no nosso site oficial: https://furia.gg',
        '3': 'Acompanhe nossos jogos ao vivo no Twitch: https://twitch.tv/furiagg',
        '4': 'Nossa incrível line up de CS:GO inclui... (lista de jogadores aqui) 🔥',
        '5': 'Conheça nossos produtos FURIOSOS! Acesse: https://www.furia.gg/produtos',
        '6': 'Nossos criadores de conteúdo e streamers: (lista de streamers aqui)',
        '7': 'Você escolheu conversar com a furIA! Me pergunte qualquer coisa sobre a FURIA!'
      }
    };
  
    // Processa a mensagem do usuário e retorna a resposta do bot
    const processMessage = (userMessage) => {
      const normalizedInput = userMessage.trim().toLowerCase();
      
      // Verifica se é uma das opções numéricas
      if (botResponses.options[normalizedInput]) {
        return {
          reply: botResponses.options[normalizedInput],
          followUp: 'Posso te ajudar com mais alguma coisa? Digite outra opção ou "sair" para encerrar.'
        };
      }
      
      // Respostas para outras palavras-chave
      switch(normalizedInput) {
        case 'oi':
        case 'olá':
        case 'ola':
          return { reply: botResponses.welcome.join('\n') };
        case 'voltar':
        case 'sair':
        case 'tchau':
          return { reply: 'Até mais! Qualquer coisa é só chamar novamente. 🐆' };
        default:
          return { reply: botResponses.default };
      }
    };
  
    return {
      processMessage,
      getWelcomeMessages: () => botResponses.welcome.map(text => ({ type: 'bot', text }))
    };
  };