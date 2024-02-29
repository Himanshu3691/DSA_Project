// console.log("this is the home page js");
// add_users = document.getElementById('add-users');
// register_txt = document.getElementById('register-new-user');

// document.getElementById('register-new-user').addEventListener('click',()=>{
    
//    register_txt.style.display = 'none'
    

//     add_users.style.display = 'block';
// })

// document.getElementById('close').addEventListener('click',()=>{
//     add_users.style.display = 'none';
//     register_txt.style.display = 'block'

// })


  register_txt = document.getElementById('register-new-user');
 



document.getElementById('register-new-user').addEventListener('click', function() {
  document.getElementById('add-users').style.display = 'block';
  register_txt.style.display = 'none'
});

document.getElementById('close-popup').addEventListener('click', function() {
  document.getElementById('add-users').style.display = 'none';
  register_txt.style.display = 'block'
});

document.getElementById('toggle-link').addEventListener('click', function(event) {
  event.preventDefault();
  var signupContainer = document.querySelector('.signup-container');
  var loginContainer = document.querySelector('.login-container');
  console.log("ma toih chal rtaha huy bahiweh");

  if (signupContainer.style.display === 'none') {
    signupContainer.style.display = 'block';
    loginContainer.style.display = 'none';
    document.getElementById('popup-title').innerHTML = '<h3>Sign Up</h3>';
    document.getElementById('toggle-link').innerHTML = 'Login';
  } else {
    signupContainer.style.display = 'none';
    loginContainer.style.display = 'block';
    document.getElementById('popup-title').innerHTML = '<h3>Login</h3>';
    document.getElementById('toggle-link').innerHTML = 'Sign Up';
  }
});

// Trigger the sign-in pop-up when the page is opened
window.onload = function() {
  document.querySelector('.signup-container').style.display = 'none';
  document.getElementById('add-users').style.display = 'block';
};