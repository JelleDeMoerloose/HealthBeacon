let bathroom = document.getElementById("bathroomBtn")
let fooddrink = document.getElementById("fooddrinkBtn")
let schedule = document.getElementById("scheduleBtn")
let chatbot = document.getElementById("chatbotBtn")
let companion = document.getElementById("companionBtn")
let translator = document.getElementById("translatorBtn")
let emergency = document.getElementById("emergencyBtn")
let popup = document.getElementById("popup");
var url = new URL(window.location.href);
var patientId = Number(url.searchParams.get('patientid'));
document.addEventListener("DOMContentLoaded", function () {
    var buttons = document.querySelectorAll('.button.sidebutton');
    buttons.forEach(function (button) {
        var label = button.querySelector('.labelbutton');
        var info = button.querySelector('.infobutton');
        if (label) {
            var paddingPercentage = 0.4; // Initial padding percentage

            // Calculate the width of the label
            var labelWidth = label.offsetWidth;
            var imageWidth = info.offsetWidth
            // Calculate the width of the button
            var buttonWidth = button.offsetWidth;

            // Calculate the padding percentage based on label and button width
            paddingPercentage = (buttonWidth - labelWidth - imageWidth) / (buttonWidth);

            // Set the padding-left dynamically
            label.style.paddingLeft = (paddingPercentage * 100) + '%';
        }

    });
});
bathroom.addEventListener("click", function () {
    openPopup();
    sendMessage('I need to go to the bathroom.');
});

fooddrink.addEventListener("click", function () {
    openPopup();
    sendMessage('I want something to eat or to drink.');
});

schedule.addEventListener("click", openSchedule);
chatbot.addEventListener("click", openChatbot);
companion.addEventListener("click", openCompanion);
translator.addEventListener("click", openTranslator);
//emergency.addEventListener("click", )

function navigateTo(link) {
    var currentUrl = window.location.href;
    var urlParts = currentUrl.split('/');
    urlParts[urlParts.length - 1] = link;
    var newUrl = urlParts.join('/');
    window.location.href = newUrl + `?patientid=${patientId}`;
}
function openSchedule() {
    navigateTo("schedule.html")
}

function openChatbot() {
    navigateTo("chat")
}

function openCompanion() {
    navigateTo("companion")
}

function openTranslator() {
    navigateTo("translator")
}

function openPopup() {
    popup.style.display = "block";
}

function closePopup() {
    popup.style.display = "none";
}

function sendMessage(message) {
    fetch('/chat/v2', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query: message, id: patientId })
    })
        .then(response => response.json())
        .then(data => {
            // Create a new message card for the bot
            document.getElementById("hiddenImage").hidden = true
            createMessage("bot", data.message);
        })
        .catch(error => console.error('Error:', error));
}



function showExplanation(buttonId, title, explanation) {
    var button = document.getElementById(buttonId);
    button.innerText = explanation; // Set button text to explanation
    button.style.fontSize = "smaller"; // Make the text smaller
    // Clear any existing timeout to prevent overlapping timeouts
    clearTimeout(button.timeout);
    button.timeout = setTimeout(function () {
        button.innerText = title; // Reset button text after 4 seconds
        button.style.fontSize = ""; // Reset font size
    }, 4000);
}


// Attach hover event listeners to each button
document.getElementById("bathroomBtnInfo").addEventListener("click", function () {
    showExplanation("bathroomBtn", "Bathroom", "Push this button if you need to go to the bathroom. The nursing staff will be informed and they'll come to help you out.");
});

document.getElementById("fooddrinkBtnInfo").addEventListener("click", function () {
    showExplanation("fooddrinkBtn", "Food or Drinks", "Push this button if you are hungry or thirsty. The nursing staff will be informed and they'll come to help you out.");
});

document.getElementById("scheduleBtnInfo").addEventListener("click", function () {
    showExplanation("scheduleBtn", "Day Schedule", "Push this button if you want to know your schedule of today.");
});



document.getElementById("companionBtnInfo").addEventListener("click", function () {
    showExplanation("companionBtn", "Companion", "Push this button if you want to go to the companion chatbot.The Companion chatbot is your go-to source for light-hearted interaction, always ready to share a joke or offer engaging conversation for those moments when you just need a bit of company.");
});

document.getElementById("translatorBtnInfo").addEventListener("click", function () {
    showExplanation("translatorBtn", "Translator", "Push this button if you want to go to the translator.The translator tool enhances communication by converting conversations between different languages, making interactions between patients and nurses more efficient and clear.");
});
