#!/usr/bin/node

// change color with click but import list classes CSS

const redHeader = document.querySelector('#red_header');
const header = document.querySelector('header');
redHeader.addEventListener('click', function () {
  header.classList.add('red');
});


