let menuContainer = document.querySelector('.menu-container');
let navBar = document.querySelector('.navbar');
let hamburger = document.querySelector('#burger-menu');
let closeMenu = document.querySelector('#close-menu');

menuContainer.addEventListener('click', () => {
    navBar.classList.toggle('active');
    hamburger.classList.toggle('not-active');
    closeMenu.classList.toggle('active');
});