document.querySelector('#login_button').addEventListener('click', evt => {
    let username = document.querySelector('#username').value;
    let password = document.querySelector('#password').value;
    apiGet(`/api/check_user/${username}`).then(
        r => {
            console.log(r);
            if (!!!r.username) {
                let error = document.querySelector('#error_message');
                error.style.visibility = 'visible';
                error.innerHTML = `<h1 style="color: red;">Username does not exist!</h1>`;
            }
            else if(!r.password_match){
                let error = document.querySelector('#error_message');
                error.style.visibility = 'visible';
                error.innerHTML = `<h1 style="color: red;">Incorrect password!</h1>`;
            }
            else {
                document.querySelector('#login_form').submit();
            }

    })
});