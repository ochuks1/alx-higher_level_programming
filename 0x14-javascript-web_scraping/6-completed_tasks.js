#!/usr/bin/node

const request = require('request'); // Import the request module

const apiUrl = process.argv[2]; // Get the API URL from command line arguments

request(apiUrl, (error, response, body) => {
    if (error) {
        console.error(error); // Print the error if occurred
    } else {
        const todos = JSON.parse(body);
        const completedTasks = {};

        todos.forEach(todo => {
            if (todo.completed) {
                if (!completedTasks[todo.userId]) {
                    completedTasks[todo.userId] = 0; // Initialize user count
                }
                completedTasks[todo.userId]++; // Increment completed task count
            }
        });

        console.log(completedTasks); // Print completed tasks by user ID
    }
});
