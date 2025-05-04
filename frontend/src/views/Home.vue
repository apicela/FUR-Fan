<template>

      <main>
        <ChatBox />
        <MessageInput />
      </main>
  </template>
  
  <script>
  import ChatBox from '../components/ChatBox.vue'
  import MessageInput from '../components/MessageInput.vue'
  
  export default {
    name: 'Home',
    components: {
      ChatBox,
      MessageInput
    }
  }
  </script>
  
  <style scoped>

  .header {
    text-align: center;
  }
  
  .logo {
    width: 150px;
  }
  
  main {
    margin-top: 20px;
    width: 100%;
    max-width: 900px;
  }
  </style>
  