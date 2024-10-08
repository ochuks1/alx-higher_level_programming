#!/usr/bin/node

const request = require('request'); // Import the request module

const movieId = process.argv[2]; // Get the movie ID from command line arguments

request(`https://swapi-api.alx-tools.com/api/films/${movieId}`, (error, response, body) => {
    if (error) {
        console.error(error); // Print the error if occurred
    } else {
        const movie = JSON.parse(body);
        console.log(movie.title); // Print the movie title
    }
});
