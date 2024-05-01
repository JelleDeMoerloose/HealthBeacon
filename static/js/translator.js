let input = document.getElementById("textInput")
let output = document.getElementById("textOutput")
let fromlanguage = document.getElementById("fromlanguage")
let tolanguage = document.getElementById("tolanguage")
let button = document.getElementById("translate")
let clear_ = document.getElementById("clear")
let homescreen = document.getElementById("homescreen")

initiateCountries()
clear_.addEventListener("click", clear)
button.addEventListener("click", function () {
    let text = input.value.trim()
    let from = fromlanguage.value
    let to = tolanguage.value
    translate(text, from, to)
})

homescreen.addEventListener("click", function() {
    var currentUrl = window.location.href; // Get the current URL
    var urlParts = currentUrl.split('/'); // Split the URL into parts
    urlParts[urlParts.length - 1] = 'homescreen.html'; // Replace the last part
    var newUrl = urlParts.join('/'); // Rejoin the URL parts
    window.location.href = newUrl; // Navigate to the new URL
});

function translate(text, from, to) {

    fetch("/patients/translate", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ lang: `${from}|${to}`, text: text })
    }).then(response => {
        console.log(response)
        if (!response.ok) {
            throw new Error("Network response was not OK")
        }
        return response.json()
    }).then(
        response => {
            output.innerHTML = response.translation;
        }
    ).catch(error => console.error)

}

function clear() {
    input.value = ""
    output.value = ""
    input.placeholder = "Enter text to translate"
    output.placeholder="Translated text will appear here"
}

function returnChatbot() {
    var currentUrl = window.location.href; // Get the current URL
    var urlParts = currentUrl.split('/'); // Split the URL into parts
    urlParts[urlParts.length - 1] = 'chat.html'; // Replace the last part
    var newUrl = urlParts.join('/'); // Rejoin the URL parts
    window.location.href = newUrl; // Navigate to the new URL
}


function initiateCountries() {
    fetch("/patients/translate").then(response => {
        if (!response.ok) {
            throw new Error("Network response was not OK")
        }
        return response.json()
    }).then(
        response => {
            for (let country in response) {
                // Create a new option element for "fromlanguage" select
                let fromOption = document.createElement("option");
                fromOption.value = country;
                fromOption.innerHTML = response[country];

                // Create a new option element for "tolanguage" select
                let toOption = document.createElement("option");
                toOption.value = country;
                toOption.innerHTML = response[country];

                // Append options to their respective select elements
                fromlanguage.appendChild(fromOption);
                tolanguage.appendChild(toOption);
            }
        }
    ).catch(error => console.error)

}

