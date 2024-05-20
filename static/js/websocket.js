/*const { hostname, port, protocol } = window.location;
const socket = new WebSocket(`ws://${hostname}:${port}/staff/websocket`);
socket.onopen = function () {
    console.log('WebSocket connection opened');

};

socket.onmessage = function (event) {
    const data = JSON.parse(event.data);
    console.log('Received message from server:', data);
};

socket.onclose = function () {
    console.log('WebSocket connection closed');
};*/


var socket = io();
socket.on('connect', function () {
    socket.emit('my event', { data: 'I\'m connected!' });
});


socket.on('notification', function (data) {
    console.log('Received message from server: ', data);
});