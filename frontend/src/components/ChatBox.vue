<template>
  <div class="chat-box">
    <div class="messages-container" ref="messagesContainer">
      <div v-for="(message, index) in chatStore.messages" :key="index" class="message-container">
        <MessageInput :message="message" />
      </div>
    </div>

    <div class="input-container">
      <input
        v-model="chatStore.userMessage"
        @keyup.enter="sendMessageAndScroll"
        placeholder="Digite sua mensagem..."
      />
      <button @click="sendMessageAndScroll">Enviar</button>
    </div>
  </div>
</template>

<script>
import { onMounted, ref, watch, nextTick } from 'vue';
import { useChatStore } from '../stores/chatStore';
import MessageInput from './MessageInput.vue';

export default {
  components: {
    MessageInput,
  },
  setup() {
    const chatStore = useChatStore();
    const messagesContainer = ref(null);

    const scrollToBottom = () => {
      if (messagesContainer.value) {
        messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight;
      }
    };

    watch(
  () => chatStore.messages.length,
  async () => {
    await nextTick(); // aguarda a renderização da nova mensagem
    scrollToBottom();
  }
);

    const sendMessageAndScroll = () => {
      chatStore.sendMessage(); // scroll será chamado automaticamente via watch
    };

    onMounted(() => {
      chatStore.initializeChat();
      scrollToBottom();
    });

    return {
      chatStore,
      messagesContainer,
      sendMessageAndScroll,
    };
  },
};
</script>



  
  <style scoped>
.chat-box {
  display: flex;
  flex-direction: column;
  height: 100%;
  max-height: 600px; 
}

.messages-container {
  flex: 1;
  overflow-y: auto;
  padding-right: 8px;
  margin-bottom: 10px;
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
  