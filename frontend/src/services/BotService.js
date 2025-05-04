// src/services/botService.js
import axios from 'axios';
import { useChatStore } from '../stores/chatStore';

export const useBotService = () => {
  const URL_API = 'http://localhost:5000';
  const optionsDefaultMessage ='1. Quem somos nós?\n2. Calendário de Jogos CSGO\n3. Acompanhe jogos ao vivo\n4. Conheça nossa Line Up de CS 🔥\n5. Lojinha da Pantera\n6. Criadores de Conteúdo e Streamers\n7. Conversar com a furIA\nDigite uma opção!';

  const botResponses = {
    default: "Desculpe, não entendi. Por favor, escolha uma opção de 1 a 7.",
    welcome: [
      'Olá, seja bem-vindo(a) ao chat 4fun!',
      'Digo... chat FUR FAN, como posso te ajudar hoje?',
      optionsDefaultMessage
    ],
    options: {
      '1': '👋 Bem-vindo à FURIA Esports!\n Somos uma organização brasileira de eSports, fundada em 2017, com a missão de levar o nome do Brasil para o topo dos campeonatos mundiais. A FURIA se destaca especialmente no Counter-Strike 2 (CS2), mas também atua em outros jogos competitivos como League of Legends, Valorant, Rocket League, Apex Legends, e mais! 🌎🏆\n Nosso time é conhecido pela sua paixão, desempenho e pela base de fãs incrível, com apoio até de grandes nomes como o Neymar Jr. ⚡💛\n Se você quer saber mais sobre nossos times, jogadores ou próximos torneios, estou aqui para te ajudar!\n',
      '3': 'Infelizmente o PandaScore API ou qualquer outra API gratuita, seja libs da HLTV, não fornecem essas informações sendo usuário free...',
      '5': 'Conheça nossos produtos FURIOSOS! Acesse: https://www.furia.gg/produtos',
      '7': 'Você escolheu conversar com a furIA! Me pergunte qualquer coisa sobre a FURIA!'
    }
  };
  function formatFuriaMembers(streamers, creators) {
    let response = '🎥 *STREAMERS:*\n';
    streamers.forEach(s => {
      response += `• ${s.name}\n`;
      Object.entries(s).forEach(([key, value]) => {
        if (key !== 'name') {
          response += `   - ${capitalize(key)}: ${value}\n`;
        }
      });
    });
  
    response += '\n🌟 *CRIADORES DE CONTEÚDO:*\n';
    creators.forEach(c => {
      response += `• ${c.name}\n`;
      Object.entries(c).forEach(([key, value]) => {
        if (key !== 'name') {
          response += `   - ${capitalize(key)}: ${value}\n`;
        }
      });
    });
  
    return response;
  }

  async function talkToIA(input) {
    useChatStore().messages.push({
      type: 'bot',
      text: 'Um momento...',
    });
    try {
      const response = await axios.post(`${URL_API}/chatbot/ask`, { 
        message: input
      });
      const data = await response.data.message.data;
      return data;
    } catch (err) {
      return {
        reply: 'Erro. Tente novamente mais tarde.'
      };
    }
  }
  
  function capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
  }
  
  const processMessage = async (userMessage) => {
    const normalizedInput = userMessage.trim().toLowerCase();
    // Opções com lógica extra
    switch (normalizedInput) {
      case '2':
        try {
          const response = await axios.get(`${URL_API}/matches/all`);
          const data = response.data.message.data;
                return {
            reply: ` • PRÓXIMAS PARTIDAS:\n${data.upcoming.map(jogo => `Campeonato: ${jogo.event} - ${jogo.date}\n ${jogo.result.furia.name} x ${jogo.result.opponent.name}`).join('\n')}\n\n • PARTIDAS RECENTES:\n${data.recent.map(jogo => `Campeonato: ${jogo.event} - ${jogo.date}\n ${jogo.result.furia.name} ${jogo.result.furia.score} - ${jogo.result.opponent.name} ${jogo.result.opponent.score}`).join('\n')}`,
            followUp: 'Posso te ajudar com mais alguma coisa? \n' + optionsDefaultMessage
          };
        } catch (err) {
          return {
            reply: 'Erro ao buscar o calendário. Tente novamente mais tarde.'
          };
        }

        case '4':
          try {
            const response = await axios.get(`${URL_API}/players/csgo/all`);
            const data = await response.data.message.data;
            return {
              reply: `Nosso elenco FURIOSO de CSGO:\n \n${data.athletes.map(player => `• ${player.name} - (${player.alternateName})`).join('\n')}
              \nCoach: ${data.coaches.name}`,
              followUp: 'Posso te ajudar com mais alguma coisa? \n' + optionsDefaultMessage
            };
          } catch (err) {
            console.log('Erro ao buscar a line up:', err);
            return {
              reply: 'Erro ao registrar presença. Tente novamente mais tarde.'
            };
          }

          case '6':
            try {
              const streamers = await axios.get(`${URL_API}/streamers/all`);
              const creators = await axios.get(`${URL_API}/creators/all`);
              const data =  streamers.data.message.data.streamers;
              const data2 =  creators.data.message.data.creators;

              return {
                reply: formatFuriaMembers(data, data2),
                followUp: 'Posso te ajudar com mais alguma coisa? \n' + optionsDefaultMessage
              };
            } catch (err) {
              console.log('Erro ao buscar a line up:', err);
              return {
                reply: 'Erro ao registrar presença. Tente novamente mais tarde.'
              };
            }

      case '7':
        return {
          reply: 'Você escolheu conversar com a furIA! Me pergunte qualquer coisa sobre a FURIA!'
        }


      default:
        if (botResponses.options[normalizedInput]) {
          return {
            reply: botResponses.options[normalizedInput],
            followUp: 'Posso te ajudar com mais alguma coisa? \n' + optionsDefaultMessage
          };
        }

        // Respostas para palavras-chave
        switch (normalizedInput) {
          case 'oi':
          case 'olá':
          case 'ola':
            return { reply: botResponses.welcome.join('\n') };
          case 'voltar':
          case 'sair':
          case 'tchau':
            useChatStore().chatState = 1;
            return 
          default:
            if(useChatStore().chatState === 7) {
              return { reply: await talkToIA(normalizedInput),
                followUp: 'Digite voltar, sair ou tchau caso queira sair da conversa com a IA.' }
               }
            
            return { reply: botResponses.default };
        }
    }
  };

  return {
    processMessage,
    getWelcomeMessages: () => botResponses.welcome.map(text => ({ type: 'bot', text }))
  };
};
