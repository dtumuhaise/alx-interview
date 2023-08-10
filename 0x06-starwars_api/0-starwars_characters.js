#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

function getCharacters (characters) {
  return new Promise((resolve, reject) => {
    request(characters, (err, res, body) => {
      if (err) reject(err);
      resolve(JSON.parse(body).name);
    });
  });
}

request(url, async (err, res, body) => {
  if (err) console.log(err);
  const characters = JSON.parse(body).characters;
  for (const character of characters) {
    console.log(await getCharacters(character));
  }
});
