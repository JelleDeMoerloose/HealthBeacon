

var socket = io();
socket.on('connect', function () {
    socket.emit('my event', { data: 'I\'m connected!' });
});


socket.on('notification', function (data) {
    console.log('Received message from server: ', data);
});