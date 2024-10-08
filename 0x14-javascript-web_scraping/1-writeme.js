#!/usr/bin/node

const fs = require('fs'); // Import the file system module

const filePath = process.argv[2]; // Get the file path from command line arguments
const content = process.argv[3]; // Get the content to write from command line arguments

fs.writeFile(filePath, content, 'utf8', (err) => {
    if (err) {
        console.error(err); // Print the error if occurred
    }
});
