FROM node:22-alpine3.19

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN npm install

# RUN npm install -g serve

EXPOSE 5173


# CMD ["serve", "-s", "build", "-l", "5173"]
CMD ["npm", "run", "dev"]