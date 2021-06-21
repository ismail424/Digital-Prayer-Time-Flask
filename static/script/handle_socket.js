var socket = io();
// socket.on('connect', function() {
//     socket.emit('my event', {data: 'I\'m connected!'});
// });
socket.on('refresh', () => {window.location.reload()});