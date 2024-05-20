const messageInput = document.getElementById('messageInput');
const sendButton = document.getElementById('sendButton');
let emergency = document.getElementById("emergency")
let homescreen = document.getElementById("homescreen")

let emergencyText = document.getElementById("emergencySuccess")


//emergency.addEventListener("click", )

var url = new URL(window.location.href);
var patientId = Number(url.searchParams.get('patientid'));

sendButton.addEventListener('click', function () {
    const message = messageInput.value.trim();
    if (message !== '') {
        createMessage("You", message);
        document.getElementById("hiddenImage").hidden = false
        sendMessage(message);
        messageInput.value = ''; // Clear input field after sending
    }
});


emergency.addEventListener('click', function () {

    sendEmergency(patientId)
    
    
});




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
    console.log("patiendid:"+ patientId)
    fetch('/patients/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query: message, id: patientId })
    // }).then(response => {
    //     if (response.ok) {
    //         return response.json();
    //     } else {
    //         response.text()
    //             .then(text => {
    //                 console.error(text);
    //                 createMessage("bot", "Sorry, I am not able to help you with that. Please try again.");
    //             });
    //     }
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



function sendEmergency(id) {
    fetch('/patients/emergency/'+id, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }

    })
        .then(response => response.json())
        .then(data => {
            
            console.log(data.message)
            if (data.message == "Emergency sent successfully"){
                emergencyText.innerText = "Emergency sent successfully"
            }

        })
        .catch(error => console.error('Error:', error));
}