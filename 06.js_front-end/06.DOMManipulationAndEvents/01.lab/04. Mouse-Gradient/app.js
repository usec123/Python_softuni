function attachGradientEvents() {
    const gradientElement = document.getElementById('gradient');

    gradientElement.addEventListener('mousemove', (e) => {
        document.getElementById('result').textContent =
            Math.floor((e.offsetX/gradientElement.clientWidth)*100) + '%';
    });
}