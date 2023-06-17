const divSelectedSystem = document.querySelector(".divSelect.system");
const divSelectedGeneration = document.querySelector(".divSelect.Generation");
const ulSelectSystem = document.querySelector(".ulSelect.system");
const ulSelectGeneration = document.querySelector(".ulSelect.Generation");
const liSelectGeneration = document.querySelectorAll(".ulSelect.Generation ul li");
const liSelectSystem= document.querySelectorAll(".ulSelect.system ul li");
const valueSelectGeneration = document.querySelector(
    ".divSelect.Generation .details"
);
const valueSelectSystem = document.querySelector(".divSelect.system .details");

divSelectedGeneration.addEventListener("click", () => {
    ulSelectGeneration.classList.toggle("active");
});

divSelectedSystem.addEventListener("click", () => {
    ulSelectSystem.classList.toggle("active");
});

liSelectGeneration.forEach((li) => {
    li.addEventListener("click", () => {
        valueSelectGeneration.innerHTML = li.innerHTML;
        ulSelectGeneration.classList.remove("active");
    });
});

liSelectSystem.forEach((li) => {
    li.addEventListener("click", () => {
        valueSelectSystem.innerHTML = li.innerHTML;
        ulSelectSystem.classList.remove("active");
    });
});

// ------------------
const allDiv=document.querySelectorAll(".all-div>div");
function hideAllDiv(){
    allDiv.forEach(div=>{
        div.style.display="none"
    })
}

const liNav=document.querySelectorAll(".part-2 ul li");

liNav.forEach(li=>{
    li.addEventListener("click",function(){
        hideAllDiv();
        if(li.innerHTML==="Languages"){
            allDiv[0].style.display="flex";
        }
        else if(li.innerHTML==="Profile Details"){
            allDiv[1].style.display="block";
        }else{
            hideAllDiv();
        }
    })
    
})