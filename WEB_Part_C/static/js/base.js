// ------------VALIDATION----------------//
//----------validation's functions-----------
function isValidFirstName(name){
    const NameRegex = /^[a-zA-Z]+$/;
    return NameRegex.test(name);
}
function isValidLastName(name){
    const lastNameRegex = /^[a-zA-Z]+(?:[\s-][a-zA-Z]+)*$/;
    return lastNameRegex.test(name);
}
function isValidEmail (email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}
function isValidPhone(phone){
    const phoneRegex = /^0\d{9}$/;
    return phoneRegex.test(phone);
}
function isValidPassword(password){
    const passwordRegex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$/;
    return passwordRegex.test(password);
}
function isValidDob(dob){
    const today = new Date();
    const oneYearAgo = new Date(today.getFullYear() - 1, today.getMonth(), today.getDate());
    return dob <= oneYearAgo;
}