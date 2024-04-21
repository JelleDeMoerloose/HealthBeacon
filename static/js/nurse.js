document.addEventListener('DOMContentLoaded', function() {

function makeRequest() {
    fetch('/nurse/notifications/latest')
        .then(response => {
            // Handle response
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if(data.question){
                alert(`New question from patient ${data.patientId}: ${data.question}`);
                fetchNotifications()
            }
        })
        .catch(error => {
            // Handle error
            console.error('There was a problem with the fetch operation:', error);
        });
}

function fetchNotifications() {
    fetch('/nurse/notifications/all')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Process notifications and display them
            displayNotifications(data);
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
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

fetchNotifications();


// Make the initial request
makeRequest();



// Make a request every 5 seconds
setInterval(makeRequest, 1000);

});