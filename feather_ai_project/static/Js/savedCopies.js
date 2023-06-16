const btnScrollDivDatesRight = document.querySelector(".right");
const btnScrollDivDatesLeft = document.querySelector(".left");
const divDates = document.querySelector(".dates");

btnScrollDivDatesRight.addEventListener("click", () => {
    divDates.scroll({
        left: divDates.scrollLeft + 200,
        behavior: "smooth",
    });
});

btnScrollDivDatesLeft.addEventListener("click", () => {
    divDates.scroll({
        left: divDates.scrollLeft - 200,
        behavior: "smooth",
    });
});

divDates.addEventListener("scroll", () => {
    if(divDates.scrollLeft==0)
    {
        btnScrollDivDatesLeft.classList.add("disabled");
    }
    else{
        btnScrollDivDatesLeft.classList.remove("disabled");
    }
})

const iconToShowPop = document.querySelectorAll(".showPop");
iconToShowPop.forEach((btn) => {
    btn.addEventListener("click", () => {
        btn.parentElement.classList.toggle("active");
    });
});
