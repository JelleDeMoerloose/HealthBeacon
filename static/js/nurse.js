var url = new URL(window.location.href);
var nurseId = Number(url.searchParams.get('nurseid'));
var socket = io();
loadAll()

function loadAll() {
    document.getElementById("nurseid").innerHTML = "Nurse id " + nurseId
    loadAllEmergencies()
    loadAllChatMessages()

}
function loadAllChatMessages() {
    fetch(`/staff/chatmessages/${nurseId}`).then(resp => {
        if (!resp.ok) {
            resp.text().then(err => console.error(err))
        } else {
            return resp.json()
        }
    }).then(
        resp => {
            for (let item of resp.message) {
                obj = JSON.parse(item)
                let category = obj.category
                if (category === 2) {
                    makeEmergency(obj)
                } else if (category === 1) {
                    makeHelp(obj)
                } else {
                    makeNoHelp(obj)
                }
            }
        }
    )
}

function loadAllEmergencies() {
    fetch(`/staff/emergencies/${nurseId}`).then(resp => {
        if (!resp.ok) {
            resp.text().then(err => console.error(err))
        } else {
            return resp.json()
        }
    }).then(
        resp => {
            for (let item of resp.message) {

                obj = JSON.parse(item)

                makeEmergency(obj)
            }
        }
    )
}

socket.on('connect', function () {
    socket.emit('my event', { data: 'I\'m connected!' });
});


socket.on('notification', function (data) {


    message = JSON.parse(data.message)
    if (!data.chatmessage && nurseId == message.nurse_id) {

        console.log("emergency")
        makeEmergency(message)

    } else {
        //it is a chatmessage: check category
        let category = message.category
        if (category === 2) {
            makeEmergency(message)
        } else if (category === 1) {
            makeHelp(message)
        } else {
            makeNoHelp(message)
        }

    }
});

function makeEmergency(message) {
    let element = createNotificationCard(message)
    element.classList.add("emergency-card");
    let list = document.getElementById("emergencyList")
    list.insertBefore(element, list.children[0])
}
function makeHelp(message) {
    let element = createNotificationCard(message)
    element.classList.add("help-card");
    let list = document.getElementById("helpList")
    list.insertBefore(element, list.children[0])
}
function makeNoHelp(message) {
    let element = createNotificationCard(message)
    element.classList.add("nohelp-card");
    let list = document.getElementById("nohelpList")
    list.insertBefore(element, list.children[0])
}
function createNotificationCard(emergency) {
    // Create card element
    const card = document.createElement('div');
    card.classList.add('card', 'notification-card');

    // Create card body
    const cardBody = document.createElement('div');
    cardBody.classList.add('card-body');
    let question = "NO CONTEXT"
    let answer = "BUTTON PRESSED"
    if (emergency.question) {
        question = "Q:" + emergency.question
        answer = "A:" + emergency.answer
    }
    // Add content to card body
    let noti = "Notification"
    if (emergency.category === 2 || emergency.button === true) {
        noti = "Emergency Notification"
    } else if (emergency.category === 1) {
        noti = "Help Needed"
    } else {
        noti = "Handled by chatbot"
    }
    const content = `
      <h5 class="card-title">${noti}</h5>
      <p class="card-text">Patient ID: ${emergency.patient_id} </p>
      <p class="card-text">${question}</p>
      <p class="card-text">${answer}</p>
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


