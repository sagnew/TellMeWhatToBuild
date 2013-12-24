var request_server = function(){
    $.getJSON("/tellme", function(data){
        $('#display').html("<h2>" + data.idea + "</h2>");
        $('#submitButton').html("Tell me more");
    });
}
