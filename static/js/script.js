
// Navabar on the phone
var navLinks = document.getElementById("navLinks");

function openMenu() {
  navLinks.style.right = "0";
}

function closeMenu() {
  navLinks.style.right = "-200px";
}

document.getElementById('menu-btn').addEventListener('click', function() {
  document.querySelector('.navbar').classList.toggle('open');
});
