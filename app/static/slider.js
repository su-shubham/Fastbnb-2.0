document.addEventListener('DOMContentLoaded', () => {
    const slidesContainer = document.querySelector('.slider-container');
    const slides = document.querySelectorAll('.slides img');
    let slideIndex = 0;
    const slideCount = slides.length;

    // Clone first image and append it to the end for seamless looping
    const firstSlide = slides[0].cloneNode(true);
    slidesContainer.appendChild(firstSlide);

    function startSlider() {
        const slideWidth = slides[0].clientWidth;
        slidesContainer.style.transition = 'transform 1s linear'; // Smooth transition

        setInterval(() => {
            slideIndex++;
            if (slideIndex >= slideCount + 1) { // Adjust for cloned slide
                slideIndex = 1; // Move to first slide
                slidesContainer.style.transition = 'none'; // Disable transition for the reset
                slidesContainer.style.transform = `translateX(-${slideWidth}px)`; // Reset to start position
                setTimeout(() => {
                    slidesContainer.style.transition = 'transform 1s linear'; // Re-enable transition
                }, 50);
            } else {
                slidesContainer.style.transform = `translateX(-${slideIndex * slideWidth}px)`;
            }
        }, 3000); // Slide moves every 3 seconds
    }

    // Start the automated slider
    startSlider();
});
