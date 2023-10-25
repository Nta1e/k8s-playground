FROM node:21-alpine AS build

WORKDIR /app

COPY package.json yarn.lock ./

RUN yarn install --frozen-lockfile

COPY . ./

RUN yarn run build
RUN npm prune --production

FROM node:21-alpine

WORKDIR /app

COPY --from=build /app/build build/
COPY --from=build /app/node_modules node_modules/

COPY package.json .
EXPOSE 3000

ENV NODE_ENV=production

CMD [ "node", "build" ]
