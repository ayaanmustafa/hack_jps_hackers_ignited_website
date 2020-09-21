// Selecting Elements

const menuOpenButton = document.querySelector('.menu-burger');
const asideNav = document.querySelector('aside');
const menuCloseButton = document.querySelector('.menu-close-btn');
const navLinks = document.querySelectorAll('.nav-link');
const copyrightYear = document.querySelector('.copyright-year');
const loadingScreen = document.querySelector('.loading_screen');

window.setTimeout(() => {
    loadingScreen.remove();
},2000);

menuOpenButton.addEventListener('click', () => {
    asideNav.style.transform = `translateX(0)`;
});

menuCloseButton.addEventListener('click', () => {
    asideNav.style.transform = `translateX(-100%)`;
});

navLinks.forEach((navLink) => {
    navLink.addEventListener('click', () => {
        console.log(window.screen.width);
        if (screen.width < 950) {
            asideNav.style.transform = `translateX(-100%)`;
        };
    });
});

copyrightYear.textContent = new Date().getFullYear();