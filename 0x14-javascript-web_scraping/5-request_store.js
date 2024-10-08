#!/usr/bin/node

const request = require('request'); // Import the request module

const url = process.argv[2]; // Get the URL from command line arguments
const filePath = process.argv[3]; // Get the file path from command line arguments

request(url, (error, response, body) => {
    if (error) {
        console.error(error); // Print the error if occurred
    } else {
        fs.writeFile(filePath, body, 'utf8', (err) => {
            if (err) {
                console.error(err); // Print the error if occurred
            }
        });
    }
});
