#!/usr/bin/node

const request = require('request'); // Import the request module

const url = process.argv[2]; // Get the URL from command line arguments

request(url, (error, response) => {
    if (error) {
        console.error(error); // Print the error if occurred
    } else {
        console.log(`code: ${response.statusCode}`); // Print the status code
    }
});
