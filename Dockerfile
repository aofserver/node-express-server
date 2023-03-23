FROM node:16.16.0-alpine

WORKDIR /usr/src
COPY package.json /usr/src

RUN npm install -g npm@9.6.0
RUN npm install
 
COPY . /usr/src

EXPOSE 3000
CMD ["npm","start"]