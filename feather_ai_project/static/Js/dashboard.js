const btnStart = document.querySelectorAll(".fav");
btnStart.forEach(btn => {
    btn.addEventListener("click", () => {
        btn.classList.toggle("active");
    });
});


