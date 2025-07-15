
// Navabar on the phone
var navLinks = document.getElementById("navLinks");

function openMenu() {
  navLinks.style.right = "0";
}

function closeMenu() {
  navLinks.style.right = "-200px";
}


// Carousel slider animation
const slider = document.querySelector(".slider");
const dots = document.querySelectorAll(".slider-nav a");
const slides = slider.querySelectorAll("img");

slider.addEventListener("scroll", () => {
  const scrollLeft = slider.scrollLeft;
  const slideWidth = slider.clientWidth;

  const index = Math.round(scrollLeft / slideWidth);

  dots.forEach((dot) => dot.classList.remove("active"));
  if (dots[index]) dots[index].classList.add("active");
});
