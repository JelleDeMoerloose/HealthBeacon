let bathroom = document.getElementById("bathroomBtn")
let fooddrink = document.getElementById("fooddrinkBtn")
let schedule = document.getElementById("scheduleBtn")
let chatbot = document.getElementById("chatbotBtn")
let companion = document.getElementById("companionBtn")
let translator = document.getElementById("translatorBtn")
let emergency = document.getElementById("emergencyBtn")
let popup = document.getElementById("popup");

bathroom.addEventListener("click", function() {
    openPopup();
    sendMessage('I need to go to the bathroom.');
});

fooddrink.addEventListener("click", function() {
    openPopup();
    sendMessage('I want something to eat or to drink.');
});

schedule.addEventListener("click", openSchedule);
chatbot.addEventListener("click", openChatbot);
companion.addEventListener("click", openCompanion);
translator.addEventListener("click", openTranslator);
//emergency.addEventListener("click", )

function openSchedule() {
    var currentUrl = window.location.href;
    var urlParts = currentUrl.split('/');
    urlParts[urlParts.length - 1] = 'schedule.html';
    var newUrl = urlParts.join('/');
    window.location.href = newUrl;
}

function openChatbot() {
    var currentUrl = window.location.href;
    var urlParts = currentUrl.split('/');
    urlParts[urlParts.length - 1] = 'chat.html';
    var newUrl = urlParts.join('/');
    window.location.href = newUrl;
}

function openCompanion() {
    var currentUrl = window.location.href;
    var urlParts = currentUrl.split('/');
    urlParts[urlParts.length - 1] = 'companion.html';
    var newUrl = urlParts.join('/');
    window.location.href = newUrl;
}

function openTranslator() {
    var currentUrl = window.location.href;
    var urlParts = currentUrl.split('/');
    urlParts[urlParts.length - 1] = 'translator.html';
    var newUrl = urlParts.join('/');
    window.location.href = newUrl;
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



function showExplanation(buttonId, explanation) {
    var button = document.getElementById(buttonId);
    var originalText = button.innerText; // Store original button text
    button.innerText = explanation; // Set button text to explanation
    button.style.fontSize = "smaller"; // Make the text smaller
    // Clear any existing timeout to prevent overlapping timeouts
    clearTimeout(button.timeout);
    button.timeout = setTimeout(function() {
        button.innerText = originalText; // Reset button text after 4 seconds
        button.style.fontSize = ""; // Reset font size
    }, 4000);
}


// Attach hover event listeners to each button
bathroom.addEventListener("mouseover", function() {
    showExplanation("bathroomBtn", "Push this button if you need to go to the bathroom. The nursing staff will be informed and they'll come to help you out.");
});

fooddrink.addEventListener("mouseover", function() {
    showExplanation("fooddrinkBtn", "Push this button if you are hungry or thirsty. The nursing staff will be informed and they'll come to help you out.");
});

schedule.addEventListener("mouseover", function() {
    showExplanation("scheduleBtn", "Push this button if you want to know your schedule of today.");
});

chatbot.addEventListener("mouseover", function() {
    showExplanation("chatbotBtn", "Push this button to go to the chatbot. You can ask any questions here and the chatbot will answer simple questions and if needed, alarm a nurse.");
});

companion.addEventListener("mouseover", function() {
    showExplanation("companionBtn", "Push this button if you want to go to the companion chatbot.The Companion chatbot is your go-to source for light-hearted interaction, always ready to share a joke or offer engaging conversation for those moments when you just need a bit of company.");
});

translator.addEventListener("mouseover", function() {
    showExplanation("translatorBtn", "Push this button if you want to go to the translator.The translator tool enhances communication by converting conversations between different languages, making interactions between patients and nurses more efficient and clear.");
});
