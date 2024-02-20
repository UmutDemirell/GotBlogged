var arrError = {
    "UsernameError": "Username field cannot be empty",
    "UsernameFormatError": "Please write a valid Username",
    "FirstNameError": "First Name field cannot be empty",
    "FirstNameFormatError": "Please write a valid First Name",
    "LastNameError": "Last Name field cannot be empty",
    "LastNameFormatError": "Please write a valid Last Name",
    "EmailError": "E-Mail field cannot be empty",
    "EmailFormatError": "Please write a valid E-Mail",
    "PasswordError": "Password field cannot be empty",
    "PasswordLengthError": "Password is too short",
    "PasswordLengthWeak": "Password: Weak!",
    "PasswordLengthModerate": "Pasword: Moderate!",
    "PasswordLengthStrong": "Password: Strong!",
    "PasswordMatchError": "Passwords are not matching",
    "FormError": "Please fill all the required blanks",
}

function validateUsername() {
    var Username = document.getElementById('contact-username').value;
    var UsernameError = document.getElementById('username-error');

    if (Username.length == 0) {
        UsernameError.innerHTML = arrError["UsernameError"];
        return false;
    }
    if (Username.match(/[^A-Z0-9]/ig)) {
        UsernameError.innerHTML = arrError["UsernameFormatError"];
        return false;
    }

    UsernameError.innerHTML = '<i class="fa fa-solid fa-check" id ="check" style="color:green"></i>';
    return true;
}

function validatePassword() {
    var password = document.getElementById('contact-password').value;
    var passwordError = document.getElementById('password-error');

    if (password.length == 0) {
        passwordError.innerHTML = arrError["PasswordError"];
        return false;
    }

    passwordError.innerHTML = '<i class="fa fa-solid fa-check" id ="check" style="color:green"></i>';
    return true;
}

function validateFirstName() {
    var firstName = document.getElementById('contact-first-name').value;
    var firstNameError = document.getElementById('first-name-error');

    if (firstName.length == 0) {
        firstNameError.innerHTML = arrError["FirstNameError"];
        return false;
    }
    if (!firstName.match(/^(?=.{1,50}$)[a-z-ğüşöçıİĞÜŞÖÇ]+(?:['_.\s][a-z-ğüşöçıİĞÜŞÖÇ]+)*$/i)) {
        firstNameError.innerHTML = arrError["FirstNameFormatError"];
        return false;
    }

    firstNameError.innerHTML = '<i class="fa fa-solid fa-check" id ="check" style="color:green"></i>';
    return true;
}

function validateLastName() {
    var lastName = document.getElementById('contact-last-name').value;
    var lastNameError = document.getElementById('last-name-error');

    if (lastName.length == 0) {
        lastNameError.innerHTML = arrError["LastNameError"];
        return false;
    }
    if (!lastName.match(/^(?=.{1,50}$)[a-z-ğüşöçıİĞÜŞÖÇ]+(?:['_.\s][a-z-ğüşöçıİĞÜŞÖÇ]+)*$/i)) {
        lastNameError.innerHTML = arrError["LastNameFormatError"];
        return false;
    }

    lastNameError.innerHTML = '<i class="fa fa-solid fa-check" id ="check" style="color:green"></i>';
    return true;
}

function validateEmail() {
    var email = document.getElementById('contact-email').value;
    var emailError = document.getElementById('email-error');

    if (email.length == 0) {
        emailError.innerHTML = arrError["EmailError"];
        return false;
    }
    if (!email.match(/^[A-Za-z\._\-[0-9]*[@][A-Za-z]*[\.][a-z]{2,4}$/)) {
        emailError.innerHTML = arrError["EmailFormatError"];
        return false;
    }

    emailError.innerHTML = '<i class="fa fa-solid fa-check" id ="check" style="color:green"></i>';
    return true;
}

function validatePasswordCreation() {
    var password = document.getElementById('contact-password').value;
    var passwordError = document.getElementById('password-error');

    var strongRegex = new RegExp("^(?=.{14,})(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*\\W).*$", "g");
    var mediumRegex = new RegExp("^(?=.{10,})(((?=.*[A-Z])(?=.*[a-z]))|((?=.*[A-Z])(?=.*[0-9]))|((?=.*[a-z])(?=.*[0-9]))).*$", "g");
    var enoughRegex = new RegExp("(?=.{8,}).*", "g");

    if (password.length == 0) {
        passwordError.innerHTML = arrError["PasswordError"];
        validateConfirmPassword();
        return false;
    } else if (false == enoughRegex.test(password)) {
        passwordError.innerHTML = arrError["PasswordLengthError"];
        validateConfirmPassword();
        return false;
    } else if (strongRegex.test(password)) {
        passwordError.innerHTML = '<span style="color:green;">' + arrError["PasswordLengthStrong"] + '<i class="fa fa-solid fa-check"b style="color:green";></i></span>';
    } else if (mediumRegex.test(password)) {
        passwordError.innerHTML = '<span style="color:orange;">' + arrError["PasswordLengthModerate"] + '<i class="fa fa-solid fa-check" style="color:orange";></i></span>';
    } else {
        passwordError.innerHTML = '<span style="color:red;">' + arrError["PasswordLengthWeak"] + '<i class="fa fa-solid fa-check" style"color:red;"></i></span>';
    }
    validateConfirmPassword();
    return true;
}

function validateConfirmPassword() {
    var confirmPassword = document.getElementById('contact-confirm-password').value;
    var password = document.getElementById('contact-password').value;
    var confirmPasswordError = document.getElementById('confirm-password-error');

    if (password.length == 0) {
        return false;
    }

    if (password != confirmPassword) {
        confirmPasswordError.innerHTML = arrError["PasswordMatchError"];
        return false;
    }

    confirmPasswordError.innerHTML = '<span style="color:green;">Passwords are Matching <i class="fa fa-solid fa-check"></i></span>';
    return true;
}

function validateLoginForm() {
    var loginSubmitError = document.getElementById('login-submit-error');
    var boolUsername = validateUsername(), boolPassword = validatePassword();

    if (!(boolUsername && boolPassword)) {
        loginSubmitError.innerHTML = arrError["FormError"];
        $(loginSubmitError).show();
        return false;
    }

    $(loginSubmitError).hide();
    return true;
}

function validateRegisterForm() {
    var registerSubmitError = document.getElementById('register-submit-error');
    var boolUsername = validateUsername(), boolFirstName = validateFirstName(), boolLastName = validateLastName(), boolEmail = validateEmail(), boolPassword = validatePasswordCreation(),  boolConfirmPassword = validateConfirmPassword();

    if (!(boolUsername && boolFirstName &&  boolLastName && boolEmail && boolPassword && boolConfirmPassword)) {
        registerSubmitError.innerHTML = arrError["FormError"];
        $(registerSubmitError).show();
        return false;
    }

    $(registerSubmitError).hide();
    return true;
}

function validateResetPasswordForm() {
    var resetPasswordSubmitError = document.getElementById('reset-password-submit-error');
    var boolEmail = validateEmail();

    if (!boolEmail) {
        resetPasswordSubmitError.innerHTML = arrError["FormError"];
        $(resetPasswordSubmitError).show();
        return false;
    }

    $(resetPasswordSubmitError).hide();
    return true;
}

function validateResetPasswordForm() {
    var editSubmitError = document.getElementById('reset-password-submit-error');
        boolPassword = validatePassword();

    if (!boolPassword) {
        editSubmitError.innerHTML = arrError["FormError"];
        $(editSubmitError).show();
        return false;
    }

    $(editSubmitError).hide();
    return true;
}

