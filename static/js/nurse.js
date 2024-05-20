var url = new URL(window.location.href);
var nurseId = Number(url.searchParams.get('nurseid'));
var socket = io();
loadAll()

function loadAll() {
    loadAllEmergencies()
}

function loadAllEmergencies() {

}

socket.on('connect', function () {
    socket.emit('my event', { data: 'I\'m connected!' });
});


socket.on('notification', function (data) {
    console.log('Received message from server: ', data);
    message = JSON.parse(data.message)
    if (nurseId == message.nurseID) {
        console.log("message for me")
        if (!data.chatmessage && message.nurseID == nurseId) {
            console.log("emergency")
            makeEmergency(message)
        }
    }
});
function makeEmergency(message) {
    let element = createNotificationCard(message)
    let list = document.getElementById("emergencyList")
    list.insertBefore(element, list.children[0])
}
function createNotificationCard(emergency) {
    // Create card element
    const card = document.createElement('div');
    card.classList.add('card', 'notification-card', "emergency-card");

    // Create card body
    const cardBody = document.createElement('div');
    cardBody.classList.add('card-body');

    // Add content to card body
    const content = `
      <h5 class="card-title">Emergency Notification</h5>
      <p class="card-text">Patient ID: ${emergency.patientID}</p>
      <p class="card-text">Timestamp: ${emergency.timestamp}</p>
    `;
    cardBody.innerHTML = content;

    // Append card body to card
    card.appendChild(cardBody);

    return card;
}


function displayNotifications(notifications) {
    const notificationsContainer = document.getElementById('notifications');
    notificationsContainer.innerHTML = ''; // Clear previous notifications

    for (const [patientId, chatElements] of Object.entries(notifications)) {
        const patientColumn = document.createElement('div');
        patientColumn.classList.add('col-12', 'col-md-6', 'col-lg-4', 'mb-4');

        const card = document.createElement('div');
        card.classList.add('card', 'h-100');

        const cardBody = document.createElement('div');
        cardBody.classList.add('card-body');

        const cardTitle = document.createElement('h5');
        cardTitle.classList.add('card-title');
        cardTitle.textContent = `Patient ${patientId}`;

        const ul = document.createElement('ul');
        ul.classList.add('list-group', 'list-group-flush');

        for (const chatElement of chatElements) {
            const li = document.createElement('li');
            li.classList.add('list-group-item');
            li.textContent = `Question: ${chatElement.question}, Answer: ${chatElement.answer || 'No answer yet'}`;
            ul.appendChild(li);
        }

        cardBody.appendChild(cardTitle);
        cardBody.appendChild(ul);
        card.appendChild(cardBody);
        patientColumn.appendChild(card);
        notificationsContainer.appendChild(patientColumn);
    }
}


