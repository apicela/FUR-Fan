FROM node:23-alpine
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install
COPY . .

# Modificar para expor em todas as interfaces
CMD ["npm", "run", "dev", "--", "--host"]
