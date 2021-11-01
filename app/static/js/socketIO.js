$(document).ready(function() {
    var socket = io.connect('http://' + document.domain + ':' + location.port);

    // Aus mqtt Nachrichten bzw. Events warten
    // Wenn neue Nachricht empfangen wurde, loggen und im UI ausgeben
    
    socket.on('mqtt_message', function(data) {
        // Im HAR view
        var text = '(' + data['topic'] + ') | ' + data['timestamp'] + ' | ' + data['payload'];
        if (data['topic'] == "/cs/har") {
            console.log(data);
            var text = '(' + data['topic'] + ') | ' + data['timestamp'] + ' | ' + data['payload'];
            $('#subscribed_HAR_messages').append('<div style="text-indent:20px;color:grey;">' + text + '</div>');
            $('#subscribed_messages').append('<div style="text-indent:20px;color:grey;">' + text + '</div>');
        } else if (data['topic'] == "/cs/bpm") { // Im BPM view
            console.log(data);
            $('#subscribed_BPM_messages').append('<div style="text-indent:20px;color:blue;">' + text + '</div>');
            $('#subscribed_messages').append('<div style="text-indent:20px;color:blue;">' + text + '</div>');
        } else { // Im OCC view
            console.log(data);
            $('#subscribed_OCC_messages').append('<div style="text-indent:20px;color:red;">' + text + '</div>');
            $('#subscribed_messages').append('<div style="text-indent:20px;color:red;">' + text + '</div>');
        }
    })
});