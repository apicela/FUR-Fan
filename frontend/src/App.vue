
<template>
 <header>
  <div class="wrapper bg-header">
    <nav class="navbar navbar-expand-lg bg-secondary-color position-relative">
      <div class="container-fluid">
        <!-- Botão mobile -->
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>

        <!-- Logo fixo no meio -->
        <div class="navbar-logo-center">
          <img src="/furia-logo.png" alt="FURIA Logo" id="header-logo" />
        </div>

        <!-- Links do menu -->
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <div class="navbar-nav ms-5">
            <RouterLink class="nav-link rounded-4" to="/">Início</RouterLink>
          </div>
        </div>

      </div>
    </nav>
  </div>
</header>


<main class="d-flex justify-content-center align-items-center text-center">
    <router-view></router-view>
  </main>

</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
.chat-container {
  max-width: 600px;
  margin: 50px auto;
  padding: 20px;
  background: #c7c3c3;
  border-radius: 10px;
  color: white;
  box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.5);
}

#header-logo {
  height: 70px;
}

.navbar-logo-center {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  top: 50%;
  transform: translate(-50%, -50%);
}

nav.navbar {
  height: 70px; /* ou um valor adequado ao tamanho do seu logo */
  position: relative; /* mantém a posição relativa para o logo absoluto */
}
main{
  margin-top: 120px;
}
.container {
  height: 100%;
}
</style>
