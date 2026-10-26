FROM node:24.22.0-alpine
WORKDIR /app

COPY package.json ./
RUN npm install
COPY server.js ./
EXPOSE 3000

USER node

CMD [ "sh", "-c", "while true; do node /app/server.js; echo '[supervisor] worker exited, restarting' >&2; done" ]
