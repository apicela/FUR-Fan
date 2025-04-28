<template>
  <div class="chat-box">
    <div v-for="(message, index) in chatStore.messages" :key="index" class="message-container">
      <MessageInput :message="message" />
    </div>
    <div class="input-container">
      <input
        v-model="chatStore.userMessage"
        @keyup.enter="chatStore.sendMessage"
        placeholder="Digite sua mensagem..."
      />
      <button @click="chatStore.sendMessage">Enviar</button>
    </div>
  </div>
</template>

<script>
import { useChatStore } from '../stores/chatStore';
import MessageInput from './MessageInput.vue';

export default {
  components: {
    MessageInput,
  },
  setup() {
    const chatStore = useChatStore();

    // Inicializa o chat com a primeira mensagem do bot
    chatStore.initializeChat();

    return {
      chatStore,
    };
  },
};
</script>



  
  <style scoped>
  .chat-box {
    max-height: 400px;
    overflow-y: auto;
    margin-bottom: 20px;
  }
  
  .input-container {
    display: flex;
    justify-content: space-between;
  }
  
  input {
    width: 80%;
    padding: 10px;
    border-radius: 20px;
    border: none;
    margin-right: 10px;
    background: #2c2c2c;
    color: white;
  }
  
  button {
    padding: 10px 15px;
    border-radius: 5px;
    background: #ffcc00;
    color: black;
    border: none;
    cursor: pointer;
  }
  
  button:hover {
    background: #e5b900;
  }
  </style>
  