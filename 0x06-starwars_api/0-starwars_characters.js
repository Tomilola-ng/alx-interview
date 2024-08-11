#!/usr/bin/node

const request = require("request");
const movie_id = process.argv[2];
// API URL | ENDPOINT | Movie ID
const url = `https://swapi-api.alx-tools.com/api/films/${movie_id}`;

request(url, async (err, response, body) => {
  if (err) {
    console.log(err);
  }
  for (const characterId of JSON.parse(body).characters) {
    await new Promise((resolve, reject) => {
        // Call the API
      request(characterId, (err, response, body) => {
        if (err) {
          reject(err);
        }
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
