"use strict";
//#region nav
const hamburgerButton = document.querySelector('.hamburger-btn');
const menu = document.querySelector('#menu');
hamburgerButton.addEventListener('click', () => {
    const isOpened = hamburgerButton.getAttribute('aria-expanded');
    // toggle the aria-expanded value
    if (isOpened === 'false') {
        hamburgerButton.setAttribute('aria-expanded', 'true');
    }
    else {
        hamburgerButton.setAttribute('aria-expanded', 'false');
    }
    // toggle the menu as required
    menu.classList.toggle('hidden');
});
//#endregion nav
