let currentSlide = 0;
const slideInterval = 5000; // Intervalo de 3 segundos
let slideIntervalId;

function showSlide(index) {
  const slides = document.querySelectorAll('.carousel-item');
  const totalSlides = slides.length;

  if (index >= totalSlides) {
    currentSlide = 0;
  } else if (index < 0) {
    currentSlide = totalSlides - 1;
  } else {
    currentSlide = index;
  }

  const carouselInner = document.querySelector('.carousel-inner');
  carouselInner.style.transform = `translateX(-${currentSlide * 100}%)`;
}

function nextSlide() {
  showSlide(currentSlide + 1);
}

function prevSlide() {
  showSlide(currentSlide - 1);
}

function startAutoSlide() {
  slideIntervalId = setInterval(nextSlide, slideInterval);
}

function stopAutoSlide() {
  clearInterval(slideIntervalId);
}

// Inicializa o carrossel
showSlide(currentSlide);
startAutoSlide();

// Opcional: parar o carrossel automático quando o mouse estiver sobre o carrossel
document.querySelector('.carousel').addEventListener('mouseenter', stopAutoSlide);
document.querySelector('.carousel').addEventListener('mouseleave', startAutoSlide);