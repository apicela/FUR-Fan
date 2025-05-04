import { defineStore } from 'pinia';
import { useBotService } from '../services/BotService';

export const useChatStore = defineStore('chatStore', {
  state: () => ({
    messages: [],
    userMessage: '',
    chatState: 1
  }),
  actions: {
    initializeChat() {
      const botService = useBotService();
      
      // Adiciona a primeira mensagem do bot se a lista de mensagens estiver vazia
      if (this.messages.length === 0) {
        this.messages = botService.getWelcomeMessages();
      }
    },

    async sendMessage() {
      if (this.userMessage.trim() !== '') {
        const input = this.userMessage;
        const botService = useBotService();

        // Adiciona a mensagem do usuário
        this.messages.push({ type: 'user', text: input });

        // Limpa o campo de entrada
        this.userMessage = '';

        try {
          // Processa a mensagem localmente usando o botService
          const response = botService.processMessage(input);
          
          this.messages.push({
            type: 'bot',
            text: response.reply,
          });

          // Adiciona follow-up se existir
          if (response.followUp) {
            setTimeout(() => {
              this.messages.push({
                type: 'bot',
                text: response.followUp,
              });
            }, 1000);
          }

        } catch (error) {
          console.error('Erro ao processar mensagem:', error);

          this.messages.push({
            type: 'bot',
            text: 'Desculpe, não consegui entender sua mensagem. Tente novamente mais tarde.',
          });
        }
      }
    },
  },
});