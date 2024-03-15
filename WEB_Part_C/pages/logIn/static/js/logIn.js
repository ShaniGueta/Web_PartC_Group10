//----------validation for Sign in form-----------
const logInForm = document.querySelector('#login')
const logInSubmit = (e) => {
    e.preventDefault()
    const logInEmailInput = document.querySelector('#logInEmail')
    const logInPasswordInput = document.querySelector('#logInPassword')
    let errorMessage = '';
    if (!isValidEmail(logInEmailInput.value.trim())){
        errorMessage += '-Please enter a valid email.\n';
    }
    if (!isValidPassword(logInPasswordInput.value.trim())){
      errorMessage += '-Please Enter a password with at least 8 characters - ' +
          'at least one number, an uppercase letter and a lowercase letter.\n';
   }
    if (errorMessage !== ''){
      alert(errorMessage);
    }
    else {//all the fields are valid
        logInForm.submit();
    }
}

if (logInForm){
    logInForm.addEventListener('submit',logInSubmit)
}