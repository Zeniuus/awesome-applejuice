FROM node:10.11.0-alpine

COPY . ./frontend

WORKDIR /frontend

RUN npm install -g yarn

RUN yarn install

CMD ["yarn", "serve"]
