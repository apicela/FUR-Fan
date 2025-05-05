# 📘 API - FUR-Fan

Esta documentação descreve os endpoints disponíveis no backend do projeto **FUR-Fan**, que fornece dados sobre membros da equipe FURIA, partidas recentes de CS:GO e um chatbot com identidade da organização.

---

## 🔌 Base URL

```
https://backend-fur-backend-fur.up.railway.app/
```

---

## 🤖 Chatbot

### `POST /chatbot/ask`

Envia uma mensagem para o chatbot da FURIA. Ele responderá apenas sobre assuntos relacionados à equipe ou ao seu contexto.

#### Corpo da Requisição (JSON)

```json
{
  "message": "Qual a história da FURIA?"
}
```

#### Resposta (200 OK)

```json
{
  "message": {
    "data": "A resposta gerada pela IA"
  }
}
```

#### Códigos de Resposta

- `200 OK` – Mensagem respondida com sucesso.
- `400 Bad Request` – Campo `message` ausente.

---

## 🎮 Jogadores e Criadores

### `GET /players/csgo/all`

Retorna uma lista com todos os jogadores de CS:GO da FURIA (via HLTV).

#### Resposta (200 OK)

```json
{
  "message": {
    "data": [
{
          "@type": "Person",
          "alternateName": "molodoy",
          "image": "https://img-cdn.hltv.org/playerbodyshot/qNyAd_xVHTTmbCAKPx-jPk.png?bg=3e4c54&h=100&ixlib=java-2.1.0&rect=124%2C8%2C467%2C467&w=100&s=6e7ebf5efe7776697df7bc1ff6aa8949",
          "name": "Danil Golubenko",
          "nationality": "Kazakhstan",
          "url": "https://www.hltv.org/player/24144/molodoy"
        }
        ...
      ],
      "coaches": {
        "@type": "Person",
        "name": "Sid Macedo",
        "nationality": "Brazil",
        "url": "https://www.hltv.org/coach/24267/sidde"
      }
  }
}
```

---

### `GET /streamers/all`

Retorna uma lista com os streamers vinculados à FURIA.

#### Resposta (200 OK)

```json
{
  "message": {
    "data": [
        {
          "name": "Thiago sem T",
          "twitch": "https://www.twitch.tv/thiagosemtlives",
          "youtube": "https://www.youtube.com/@thiagosemt"
        },
        ...
    ]
  }
}
```

---

### `GET /creators/all`

Retorna uma lista com os criadores de conteúdo da FURIA.

#### Resposta (200 OK)

```json
{
  "message": {
    "data": [
      {
          "instagram": "https://www.instagram.com/brino/",
          "name": "Brino",
          "twitch": "https://www.twitch.tv/brino",
          "twitter": "https://x.com/Brunozor"
      },
        ...
    ]
  }
}
```

---

## 📅 Partidas Recentes

### `GET /matches/all`

Retorna uma lista com as partidas recentes da FURIA (dados do HLTV).

#### Resposta (200 OK)

```json
{
  "message": {
    "data": {
      "recent": [
        {
          "date": "09/04/2025",
          "event": "PGL Bucharest 2025 - 12-14th",
          "result": {
            "furia": {
              "name": "FURIA",
              "score": "0"
            },
            "opponent": {
              "name": "The MongolZ",
              "score": "2"
            }
          }
        },
        ...
      ],
      "upcoming": [
        {
          "date": "10/05/2025",
          "event": "PGL Astana 2025",
          "result": {
            "furia": {
              "name": "FURIA",
              "score": "-"
            },
            "opponent": {
              "name": "The MongolZ",
              "score": "-"
            }
          }
        }
      ]
    }
  }
}
```

---

## 📝 Observações

- Os dados são obtidos por **web scraping** e podem variar conforme mudanças nas fontes externas.(Fonte: HLTV)
- O chatbot utiliza a API da **Gemini** para respostas baseadas em IA.
