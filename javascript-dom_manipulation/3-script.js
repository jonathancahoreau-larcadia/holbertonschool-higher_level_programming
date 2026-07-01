#!/usr/bin/node

// Toggle the header class between red and green

const toggleHeader = document.querySelector("#toggle_header");
const header = document.querySelector("header");

toggleHeader.addEventListener("click", function () {
  if (header.classList.contains("green")) {
    header.className = "red";
  } else {
    header.className = "green";
  }
});
