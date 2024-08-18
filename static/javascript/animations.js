
function animateElements() {
    // Animation for the title text
    anime({
        targets: '.title-text p',
        translateY: [50, 0],
        opacity: [0, 1],
        delay: anime.stagger(100),
        easing: 'easeOutQuad',
    });

    // Animation for the showcase images
    anime({
        targets: '.showcase-img',
        scale: {
            value: [0.5, 1],
            duration: 500, // Duration of the scaling animation (ms)
            easing: 'easeInOutQuad' // Easing function for smoother transition
        },
        opacity: [0, 1],
        delay: anime.stagger(100),
        easing: 'easeOutQuad',
    });

    // Animation for the navigation links
    anime({
        targets: '.menu_items',
        translateY: [20, 0],
        opacity: [0, 1],
        delay: anime.stagger(100),
        easing: 'easeOutQuad',
    });

    // Animation for the footer message
    anime({
        targets: '.footer_message',
        translateY: [20, 0],
        opacity: [0, 1],
        delay: 500, // Delay for the footer message animation
        easing: 'easeOutQuad',
    });
}

window.requestAnimationFrame(animateElements);

// Adding event listeners to scale the image smoothly on hover
const showcaseImgs = document.querySelectorAll('.showcase-img');
showcaseImgs.forEach(img => {
    img.addEventListener('mouseenter', () => {
        anime({
            targets: img,
            scale: 1.1,
            duration: 300, // Duration of the scaling animation on hover (ms)
            easing: 'easeInOutQuad' // Easing function for smoother transition
        });
    });
    img.addEventListener('mouseleave', () => {
        anime({
            targets: img,
            scale: 1,
            duration: 300, // Duration of the scaling animation on mouse leave (ms)
            easing: 'easeInOutQuad' // Easing function for smoother transition
        });
    });
});
