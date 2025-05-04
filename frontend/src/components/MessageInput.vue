<template>  
  <div v-if="message" class="message-container">
    <div v-if="message.type === 'bot'" class="bot-avatar">
      <img src="../assets/furia-logo.png" alt="FURIA Logo" class="avatar"/>
    </div> 
    
    <div class="message" :class="{ 'bot-message': message.type === 'bot', 'user-message': message.type === 'user' }">
      <p class="message-text">{{ message.text }}</p>
    </div>

    <div v-if="message.type === 'user'" class="user-avatar">
      <img src="../../public/user.png" alt="FURIA Logo" class="avatar"/>
    </div>
  </div> 
</template>

<script>
export default {
  props: {
    message: {
      type: Object,
      required: true,
    },
  },
};
</script>



  
  <style scoped>
  .message-container {
    display: flex;
    align-items: flex-start; /* Alinha avatar e mensagem verticalmente */
    margin-bottom: 10px;
  }
  
  .message-text {
  white-space: pre-wrap;
  text-align: left;
}


  .avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
  }
  
  .bot-avatar {
    margin: 10px;
  }
  
  .user-avatar {
margin: 10px;  
}
  
  .message {
    max-width: 80%;
    padding: 10px;
    border-radius: 5px;
    font-size: 14px;
    display: inline-block;
  }
  
  .bot-message {
    background: #ffcc00;
    color: #000;
  }
  
  .user-message {
    background: #0073e6;
    color: white;
    margin-left: auto; /* Alinha a mensagem do usuário à direita */
  }
  </style>
  