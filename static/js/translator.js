let input = document.getElementById("textInput")
let output = document.getElementById("textOutput")
let languageselector = document.getElementById("language")
let button = document.getElementById("translate")
let clear_ = document.getElementById("clear")

clear_.addEventListener("click", clear)
button.addEventListener("click", function () {
    let text = input.value.trim()
    let language = languageselector.value
    translate(text, language)
})

function translate(text, language) {
    output.value = `vertaling in ${language}`
}

function clear() {
    input.value = ""
    output.value = ""
}

