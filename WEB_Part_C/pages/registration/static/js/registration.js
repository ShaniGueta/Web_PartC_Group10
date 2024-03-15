
//----------validation for Sign up form-----------
const registrationForm = document.querySelector('#regForm');
const regiSubmit = (e) => {
  e.preventDefault()
  const firstNameInput = document.querySelector('#firstNameReg');
  const lastNameInput = document.querySelector('#lastNameReg');
  const emailInput = document.querySelector('#emailReg');
  const phoneNumberInput = document.querySelector('#phoneReg');
  const birthdateInput = document.querySelector('#dobReg');
  const passwordInput = document.querySelector('#passwordReg');
  const confPasswordInput = document.querySelector('#confPasswordReg');
  let errorMessage = '';
  if (!isValidFirstName(firstNameInput.value.trim())){
      errorMessage += '-Please enter a first name with english letters only.\n';
  }
  if (!isValidLastName(lastNameInput.value.trim())){
      errorMessage += '-Please enter a last name with english letters only.\n';
  }
  if (!isValidEmail(emailInput.value.trim())){
      errorMessage += '-Please enter a valid email.\n';
  }
  if (!isValidPhone(phoneNumberInput.value.trim())){
      errorMessage += '-Please enter a valid phone number.\n';
  }
  if (!isValidDob(new Date(birthdateInput.value.trim()))){
      errorMessage += '-Must be at least one year old.\n';
  }
  if (!isValidPassword(passwordInput.value.trim())){
      errorMessage += '-Please Enter a password with at least 8 characters - ' +
          'at least one number, an uppercase letter and a lowercase letter.\n';
  }
  if (passwordInput.value.trim() !== confPasswordInput.value.trim()){
      errorMessage += '-Passwords must be identical.\n';
  }

  if (errorMessage !== ''){
      alert(errorMessage);
  }
  else { //all the fields are valid
      registrationForm.submit();
  }
}

if (registrationForm){
    registrationForm.addEventListener('submit', regiSubmit)
}



