document.querySelector('#register_button').addEventListener('click', evt => {
    evt.preventDefault();
    if(document.querySelector('#password').value !== document.querySelector('#confirm_password').value){
        let error = document.querySelector('#error_message');
        error.style.visibility = 'visible';
        error.innerHTML = `<h1 style="color: red;">Passwords does not match!</h1>`;
    }
    let isAnyEmpty = false;
    document.querySelectorAll('input').forEach(i => {
        if (i.value === '') {
            isAnyEmpty = true;
        }
    })
    if(isAnyEmpty){
        let error = document.querySelector('#error_message');
            error.style.visibility = 'visible';
            error.innerHTML = `<h1 style="color: red;">All details must be completed!</h1>`;
    }else{
        document.querySelector('#register_form').submit()
    }

})