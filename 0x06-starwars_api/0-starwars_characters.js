#!/usr/bin/node
const request = require("request");

function fetchCharacter(characterList, index) {
  if (!characterList[index]) return;

  request(characterList[index], (error, _, body) => {
    if (error) {
      console.log(error);
      return;
    }

    console.log(JSON.parse(body).name);
    fetchCharacter(characterList, index + 1);
  });
}

function fetchMovie(movieId) {
  const endpoint = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  request(endpoint, (error, _, body) => {
    if (error) {
      console.log(error);
      return;
    }

    const characterList = JSON.parse(body).characters;
    fetchCharacter(characterList, 0);
  });
}

const movieId = process.argv[2];
fetchMovie(movieId);
