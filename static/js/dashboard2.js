
// Chart.js script
var ctx1 = document.getElementById('emergenciesChart').getContext('2d');
var socket = io();
loadAll()

var emergenciesChart = new Chart(ctx1, {
    type: 'bar',
    data: {
        labels: [],
        datasets: [{
            label: 'Amount of Emergencies',
            data: [],
            fill: true,
            //borderColor: 'rgba(75, 192, 192, 0.1)',
            tension: 0.1,
            backgroundColor: 'rgba(45,153,225, 1)'

        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        },
        plugins: {
            legend: {
                display: false

            }
        }
    }
});

var ctx2 = document.getElementById('questionsChart').getContext('2d');
var questionsChart = new Chart(ctx2, {
    type: 'doughnut',
    data: {
        labels: ['Normal Questions', 'Emergency Questions'],
        datasets: [{
            label: 'Question Types',
            data: [300, 50],
            backgroundColor: [
                'rgb(255, 99, 132)',
                'rgb(54, 162, 235)'
            ]
        }]
    },
    options: {}
});

//  setTimeout(function() {
//   emergenciesChart.data.datasets[0].data[6] = 70;
//    emergenciesChart.update();
//  }, 2000);

function fetchData() {
    fetch('http://localhost:5000/dashboard/emergencies/all')
        .then(response => response.json())
        .then(data => {

            var labels = data.label;
            var dataValues = data.data;


            emergenciesChart.data.labels = labels;
            emergenciesChart.data.datasets[0].data = dataValues

            emergenciesChart.update()

        })
        .catch(error => console.error('Error fetching data:', error));
}


function loadAll() {
    fetchData()
    loadAllEmergencies()
    loadAllChatMessages()

}
function loadAllChatMessages() {
    fetch(`/staff/chatmessages`).then(resp => {
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
    fetch(`/staff/emergencies`).then(resp => {
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
    if (!data.chatmessage) {

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
      <p class="card-text">Patient ID: ${emergency.patient_id} Nurse ID: ${emergency.nurse_id}</p>
      <p class="card-text">${question}</p>
      <p class="card-text">${answer}</p>
      <p class="card-text">Timestamp: ${emergency.timestamp}</p>
    `;
    cardBody.innerHTML = content;

    // Append card body to card
    card.appendChild(cardBody);

    return card;
}


setInterval(fetchData, 5000);
