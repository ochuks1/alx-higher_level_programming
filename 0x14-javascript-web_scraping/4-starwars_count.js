#!/usr/bin/node

const request = require('request'); // Import the request module

const apiUrl = process.argv[2]; // Get the API URL from command line arguments

request(apiUrl, (error, response, body) => {
    if (error) {
        console.error(error); // Print the error if occurred
    } else {
        const films = JSON.parse(body).results;
        let count = 0;

        films.forEach(film => {
            if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
                count++; // Increment count if Wedge Antilles is in the film
            }
        });

        console.log(count); // Print the count of movies
    }
});
