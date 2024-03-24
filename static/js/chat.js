const messageInput = document.getElementById('messageInput');
const sendButton = document.getElementById('sendButton');

const urlParams = new URLSearchParams(window.location.search);
let patientId =  urlParams.get('patientid');


sendButton.addEventListener('click', function () {
    let message = messageInput.value.trim();
    if (message !== '') {

        fetch(`/patients/id/${patientId}`).then(response=>response.json()).then(data=>{

            delete data.id;
            delete data.days_in_hospital

            console.log(data)




            createMessage("You", message);
            document.getElementById("hiddenImage").hidden = false

           
    
            //message = message + " IMPORTANT: " + JSON.stringify(data)
            console.log(message)
            sendMessage(message);
            messageInput.value = ''; // Clear input field after sending



        })
 
    }
});

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
    botMessageCard.classList.add('card', 'message', `${sender}-message`);

    const botMessageContent = document.createElement('div');
    botMessageContent.classList.add('card-body');
    botMessageContent.innerHTML = `<strong>${sender}:</strong> ${message}`;

    botMessageCard.appendChild(botMessageContent);
    chatBody.appendChild(botMessageCard);
}
