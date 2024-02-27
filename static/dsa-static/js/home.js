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


