FROM node:18 AS build

WORKDIR /app

COPY frontend/package.json frontend/package-lock.json ./

RUN npm install --legacy-peer-deps --unsafe-perm

COPY frontend /app

#RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
