let input = document.getElementById("textInput")
let output = document.getElementById("textOutput")
let fromlanguage = document.getElementById("fromlanguage")
let tolanguage = document.getElementById("tolanguage")
let button = document.getElementById("translate")
let clear_ = document.getElementById("clear")
initiateCountries()
clear_.addEventListener("click", clear)
button.addEventListener("click", function () {
    let text = input.value.trim()
    let from = fromlanguage.value
    let to = tolanguage.value
    translate(text, from, to)
})

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

