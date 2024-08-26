document.addEventListener('DOMContentLoaded', () => {
    const slidesContainer = document.querySelector('.slides');
    
    // Array of image URLs
    const images = [
        "https://images.unsplash.com/photo-1543269664-76bc3997d9ea?ixlib=rb-1.2.1&auto=format&fit=crop&w=250&h=250&q=10",
        "https://images.unsplash.com/photo-1543269664-76bc3997d9ea?ixlib=rb-1.2.1&auto=format&fit=crop&w=250&h=250&q=10",
        "https://images.unsplash.com/photo-1543269664-76bc3997d9ea?ixlib=rb-1.2.1&auto=format&fit=crop&w=250&h=250&q=10",
        "https://images.unsplash.com/photo-1543269664-76bc3997d9ea?ixlib=rb-1.2.1&auto=format&fit=crop&w=250&h=250&q=10",
        "https://images.unsplash.com/photo-1543269664-76bc3997d9ea?ixlib=rb-1.2.1&auto=format&fit=crop&w=250&h=250&q=10",
        "https://images.unsplash.com/photo-1543269664-76bc3997d9ea?ixlib=rb-1.2.1&auto=format&fit=crop&w=250&h=250&q=10",
        "https://images.unsplash.com/photo-1543269664-76bc3997d9ea?ixlib=rb-1.2.1&auto=format&fit=crop&w=250&h=250&q=10"
    ];
    
    // Loop through images array and create img elements
    images.forEach((url) => {
        const imgElement = document.createElement('img');
        imgElement.src = url;
        slidesContainer.appendChild(imgElement);
    });

    // Slider functionality (from the previous implementation)
    let slideIndex = 0;
    const slideCount = images.length;
    const slideWidth = slidesContainer.querySelector('img').clientWidth;
    let translateX = 0;
    let speed = 0.5; // Speed of the slider (pixels per frame)

    // Clone first and last images for seamless looping
    const firstSlide = slidesContainer.querySelector('img').cloneNode(true);
    const lastSlide = slidesContainer.querySelectorAll('img')[slideCount - 1].cloneNode(true);
    slidesContainer.appendChild(firstSlide);
    slidesContainer.insertBefore(lastSlide, slidesContainer.querySelector('img'));

    // Set initial position to show the first actual slide
    translateX = -slideWidth;
    slidesContainer.style.transform = `translateX(${translateX}px)`;

    function animateSlider() {
        translateX -= speed; // Move the slider

        // If the slider has moved past the last cloned slide, reset to the start
        if (translateX <= -((slideCount + 1) * slideWidth)) {
            translateX = -slideWidth;
            slidesContainer.style.transition = 'none'; // Temporarily disable transition
            slidesContainer.style.transform = `translateX(${translateX}px)`;
            requestAnimationFrame(() => {
                slidesContainer.style.transition = 'transform 0s linear'; // Re-enable transition
                animateSlider(); // Continue animation
            });
        } else {
            slidesContainer.style.transform = `translateX(${translateX}px)`;
            requestAnimationFrame(animateSlider); // Continue animation
        }
    }

    // Pause the slider on hover
    slidesContainer.addEventListener('mouseover', () => {
        speed = 0;
    });

    // Resume the slider when not hovered
    slidesContainer.addEventListener('mouseout', () => {
        speed = 0.5;
    });

    // Start the animation
    animateSlider();
});
