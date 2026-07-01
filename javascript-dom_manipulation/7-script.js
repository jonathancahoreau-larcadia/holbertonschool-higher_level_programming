#!/usr/bin/node

//use for each to fill a list movie from api

const listMovie = document.querySelector('#list_movies');

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    data.results.forEach(function (movie) {
      const newMovie = document.createElement('li');
      newMovie.textContent = movie.title;
      listMovie.appendChild(newMovie);
    });
  });
