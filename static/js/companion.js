const messageInput = document.getElementById('messageInput');
const sendButton = document.getElementById('sendButton');
let returnChatbot_ = document.getElementById("returnChatbot")

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
    var currentUrl = window.location.href; // Get the current URL
    var urlParts = currentUrl.split('/'); // Split the URL into parts
    urlParts[urlParts.length - 1] = 'chat.html'; // Replace the last part
    var newUrl = urlParts.join('/'); // Rejoin the URL parts
    window.location.href = newUrl; // Navigate to the new URL
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
