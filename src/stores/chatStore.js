import { defineStore } from 'pinia';

export const useChatStore = defineStore('chatStore', {
  state: () => ({
    messages: [],
    userMessage: '',
  }),
  actions: {
    initializeChat() {
      // Adiciona a primeira mensagem do bot se a lista de mensagens estiver vazia
      if (this.messages.length === 0) {
        this.messages.push({
          type: 'bot',
          text: 'Olá, FURIA! Como posso te ajudar hoje?',
        });
      }
    },

    async sendMessage() {
      if (this.userMessage.trim() !== '') {
        const input = this.userMessage;

        // Adiciona a mensagem do usuário
        this.messages.push({ type: 'user', text: input });

        // Limpa o campo de entrada
        this.userMessage = '';

        try {
          // const response = await fetch('https://sua-api-aqui.com/endpoint', {
          //   method: 'POST',
          //   headers: { 'Content-Type': 'application/json' },
          //   body: JSON.stringify({ message: input }), // Corpo da requisição
          // });

          // if (!response.ok) {
          //   throw new Error(`Erro: ${response.status}`);
          // }

          // const data = await response.json();
          const data = {
            reply : 'hello world'
          }
          // Adiciona a resposta da API (bot) ao array de mensagens
          this.messages.push({
            type: 'bot',
            text: data.reply || 'Desculpe, não entendi.',
          });

        } catch (error) {
          console.error('Erro ao chamar a API:', error);

          // Mensagem padrão do bot em caso de falha
          this.messages.push({
            type: 'bot',
            text: 'Desculpe, não consegui entender sua mensagem. Tente novamente mais tarde.',
          });
        }
      }
    },
  },
});
