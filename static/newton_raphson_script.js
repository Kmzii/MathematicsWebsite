document.getElementById("newton-raphson-form").addEventListener("submit", async function (event) {
    event.preventDefault(); // Prevent the default form submission

    // Get user input
    const functionInput = document.getElementById("function").value;
    const guessInput = document.getElementById("guess").value.trim(); // Trim leading/trailing whitespace
    const iterationsInput = parseInt(document.getElementById("iterations").value);

    // Validate the guess input using a regular expression
    const validInput = /^(\d+(\.\d*)?|(\.\d+))$/; // Regular expression for valid formats

    if (!validInput.test(guessInput)) {
        // Show an error message for invalid guess formats
        document.getElementById("result").innerHTML = "Invalid initial guess. Please enter a valid number.";
        document.querySelector(".results").style.display = "flex"; // Display the result section
        document.getElementById("graph").style.display = "none"; // Hide the graph section
    } else {
        try {
            // Send the data to the server for processing
            const response = await fetch('/calculate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ function: functionInput, guess: parseFloat(guessInput), iterations: iterationsInput }),
            });

            if (!response.ok) {
                throw new Error('Network response was not ok.');
            }

            const data = await response.json();

            if (data.error) {
                // Handle server-side errors
                document.getElementById("result").innerHTML = `Server Error: ${data.error}`;
                document.querySelector(".results").style.display = "flex"; // Display the result section
                document.getElementById("graph").style.display = "none"; // Hide the graph section
            } else {
                // Extract and display the last root value
                const lastRoot = data.result[data.result.length - 1];
                document.getElementById("result").innerHTML = `Root: ${lastRoot}`;
                document.querySelector(".results").style.display = "flex"; // Display the result section
                document.getElementById("graph").style.display = "flex"; // Show the graph section

                // Show the results section and set it to display as flex
                const resultGraph = document.querySelector(".results");
                resultGraph.style.display = "flex";

                // Update the graph source
                const graph = document.getElementById("graph");
                graph.src = `data:image/png;base64,${data.plot}`;
            }
        } catch (error) {
            // Handle various errors
            document.getElementById("result").innerHTML = `Error: ${error.message}`;
            document.querySelector(".results").style.display = "flex"; // Display the result section
            document.getElementById("graph").style.display = "none"; // Hide the graph section
        }
    }
});
