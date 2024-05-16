const messageInput = document.getElementById('messageInput');
const sendButton = document.getElementById('sendButton');
let returnChatbot_ = document.getElementById("returnChatbot")
let homescreen = document.getElementById("homescreen")
var url = new URL(window.location.href);
var patientId = Number(url.searchParams.get('patientid'));
returnChatbot_.addEventListener("click", returnChatbot)
sendButton.addEventListener('click', function () {
    const message = messageInput.value.trim();
    if (message !== '') {
        createMessage("You", message);
        document.getElementById("hiddenImage").hidden = false
        sendMessage(message);
        messageInput.value = ''; // Clear input field after sending
    }
});

function returnChatbot() {
    navigateTo("chat")
}

homescreen.addEventListener("click", function () {
    navigateTo("home")
});
function navigateTo(link) {
    var currentUrl = window.location.href;
    var urlParts = currentUrl.split('/');
    urlParts[urlParts.length - 1] = link;
    var newUrl = urlParts.join('/');
    window.location.href = newUrl + `?patientid=${patientId}`;
}

function sendMessage(message) {
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query: message })
    })
        .then(response => response.json())
        .then(data => {
            // Create a new message card for the bot
            document.getElementById("hiddenImage").hidden = true
            createMessage("bot", data.message);
        })
        .catch(error => console.error('Error:', error));
}

function createMessage(sender, message) {
    const chatBody = document.getElementById('chatbox');
    const botMessageCard = document.createElement('div');
    botMessageCard.classList.add('message', `${sender}-message`);
    const botMessageContent = document.createElement('div');

    botMessageContent.innerHTML = `<strong>${sender}:</strong> ${message}`;

    botMessageCard.appendChild(botMessageContent);
    chatBody.appendChild(botMessageCard);
}
