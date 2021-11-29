function sendForm(regform) {
    emailjs.send('CiTest', 'ContactCI', {
        "from_name": regform.username.value,
        "from_email": regform.email.value,
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
};