# 🐺 Chat Fã FURIA – Experiência Conversacional

Este projeto é uma aplicação de chatbot criada para engajar fãs do time de CS:GO da FURIA, oferecendo uma experiência interativa, informativa e divertida diretamente via [Web](https://frontend-fur.vercel.app/) . #DIADEFURIA

## 🎯 Objetivo

Criar um chat para os fãs da FURIA com funcionalidades que ajudem a acompanhar o time, interagir como torcida e se manter por dentro das novidades. Essa solução visa simular a experiência de um contato oficial com a FURIA no WhatsApp ou em um canal exclusivo.

## 🚀 Funcionalidades
- 👀 **História da FURIA**
- 📅 **Calendário de jogos** 
- 🔴 **Status ao vivo dos jogos** 
- 🔥 **Nossa LineUp** 
- 🎉 **Converse com a IA** - Pergunte o que quiser
- 🛍️ Link para a **loja oficial** e cupons exclusivos
- 😍 **Criadores de conteúdo e Streamers**

## 🛠️ Tecnologias Utilizadas

- Frontend: Vue.js 3 + JavaScript, deploy na Vercel. https://frontend-fur.vercel.app/
- Backend: Python + Flask, deploy de suas edge functions na Railway. 
- [Documentação dos endpoints](https://github.com/apicela/FUR-Fan/tree/main/backend#readme)
- Utilização de **Selenium** para extrair dados. (Web Scrapping)
- Implementação de caches para uma rápida resposta ao furioso

## 📁 Estrutura do Projeto

```bash
FUR-Fan/
├── frontend/                      # Interface do usuário (Landing Page)
│   ├── Dockerfile
│   ├── public/                    # Recursos estáticos
│   ├── src/                       # Código-fonte da aplicação
│   ├── ├── components/            # Componentes das páginas          
│   ├── ├── router/                # Rotas das paginas         
│   ├── ├── services/              # Lógica de manipulação       
│   ├── ├── stores/                # Armazenar estados do chatBot e informações      
│   ├── ├── views/                 # Páginas     
│   ├── ├── App.vue                # Header e content do RouterView
├── backend/                       # Lógica do chatbot e APIs
│   ├── .dockerignore
│   ├── app.py                     # Entrada principal da aplicação Flask
│   ├── chromedriver               # Webdriver para scraping ( Selenium)
│   ├── creators.json              # Dados estáticos de creators
│   ├── matches_cache.json         # Cache de partidas pós Web Scrapping
│   ├── players_cache.json         # Cache de jogadores pós Web Scrapping
│   ├── requirements.txt           # Dependências Python
│   ├── streamers.json             # Dados de streamers
│   ├── routes/                    # Rotas da API
│   ├── services/                  # Lógica de negócio / scraping / etc.
