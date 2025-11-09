function ddayCountdown() {
    const ddayElement = document.getElementById('dday-counter');
    // The target date is 2025-12-08
    const targetDate = new Date('2025-12-08T00:00:00');

    function updateCounter() {
        const now = new Date();
        const difference = targetDate - now;

        if (difference <= 0) {
            ddayElement.innerHTML = "시험 시작! 🔥";
            clearInterval(interval);
            return;
        }

        const days = Math.floor(difference / (1000 * 60 * 60 * 24));
        const hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((difference % (1000 * 60)) / 1000);

        ddayElement.innerHTML = `D-${days} <br> <span style="font-size: 0.5em;">${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}</span>`;
    }

    const interval = setInterval(updateCounter, 1000);
    updateCounter(); // Initial call
}

ddayCountdown();
