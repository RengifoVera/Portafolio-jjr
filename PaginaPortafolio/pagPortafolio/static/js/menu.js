let menutoggle = document.querySelector('.menu-toggle');
let menutoggleIcon = document.querySelector('.menu-toggle i');
let menu = document.getElementById('menu');

menutoggle.addEventListener('click',e=>{
    menu.classList.toggle('show');

    if(menu.classList.contains('show'))
    {
        menutoggleIcon.setAttribute('class','fas fa-times');

    }else{
        menutoggleIcon.setAttribute('class','fas fa-bars');

    }
});

