FROM node:10
RUN mkdir /app
WORKDIR /app
COPY ./package*.json ./
RUN npm install
RUN npm install -g http-server
#COPY . .
#EXPOSE 8080
RUN npm install -g http-server
CMD [ "http-server", "dist" ]
#CMD ["npm", "start"]
