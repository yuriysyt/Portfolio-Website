
const containers = document.querySelectorAll('.content');
containers.forEach(container => {
    container.addEventListener('mouseenter', () => {
        anime({
            targets: container,
            scale: 1.1,
            duration: 300, // Adjust the duration as needed
            easing: 'easeInOutQuad' // Use easeInOutQuad easing for smoother effect
        });
    });
    container.addEventListener('mouseleave', () => {
        anime({
            targets: container,
            scale: 1,
            duration: 300, // Adjust the duration as needed
            easing: 'easeInOutQuad' // Use easeInOutQuad easing for smoother effect
        });
    });
});