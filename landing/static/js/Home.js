
document.addEventListener('DOMContentLoaded', (event) => {
    const getStartedBtn = document.querySelector('.get-started-btn');
    getStartedBtn.addEventListener('click', () => {
        window.location.href = "/login";  
    });
});

