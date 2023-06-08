const inputSearchKeywords = document.querySelector(".inputSearchKeywords");
const btnSearchKeywords = document.querySelector(".btnSearchKeywords");

inputSearchKeywords.addEventListener("input", function () {
    if (inputSearchKeywords.value != "") {
        btnSearchKeywords.classList.add("valid");
    } else {
        btnSearchKeywords.classList.remove("valid");
    }
});

const inputAddTag = document.querySelector(".inputAddTag");
const btnNext = document.querySelector(".complete-the-fields .btnNext");
const divSomeKeyWords = document.querySelector(
    ".complete-the-fields.one .someKeyWords"
);

inputAddTag.addEventListener("keyup", (event) => {
    if (event.keyCode === 13) {
        const value = inputAddTag.value.trim();
        if (value !== "") {
            const div = document.createElement("div");
            div.innerHTML = `
                <p>${inputAddTag.value}</p>
                <ion-icon
                    name="close-outline"
                    class="deleteKey"
                ></ion-icon>
            `;
            const iconDeleteKey = div.querySelector(".deleteKey");
            iconDeleteKey.addEventListener("click", () => {
                div.remove();
            });
            divSomeKeyWords.appendChild(div);
            inputAddTag.value = "";
        }
    }
    if (divSomeKeyWords.childElementCount > 0) {
        btnNext.classList.add("valid");
    } else {
        btnNext.classList.remove("valid");
    }
});
btnNext.addEventListener("click", (e) => {
    e.preventDefault();
});
// --------------------

const divEmpty = document.querySelector(".part-2-2 .empty");
const divAllKeyWords = document.querySelector(".divAllKeyWords");
btnSearchKeywords.addEventListener("click", (e) => {
    e.preventDefault();
    if (inputSearchKeywords.value != "") {
        divEmpty.style.display = "none";
        divAllKeyWords.style.display = "block";
    }
});
// ---------------------
const selectKeywords = document.querySelectorAll(
    ".divAllKeyWords ul li,.AllIdeas ul li,.AllOutline ul li"
);
selectKeywords.forEach((li) => {
    li.addEventListener("click", () => {
        li.classList.toggle("active");
    });
});
// -------------------
let numDiv = 1;

const allBtnNext = document.querySelectorAll(".btnNext");
allBtnNext.forEach((btn) => {
    btn.addEventListener("click", () => {
        if (numDiv === 1 && divSomeKeyWords.childElementCount > 0) {
            numDiv++;
            showDivStep();
        } else if (numDiv < 4 && numDiv > 1) {
            numDiv++;
            showDivStep();
        }
    });
});

const allBtnBack = document.querySelectorAll(".btnBack");
allBtnBack.forEach((btn) => {
    btn.addEventListener("click", () => {
        if (numDiv <= 4) {
            numDiv--;
            showDivStep();
        }
    });
});

// ------------------------

const allDivOfSteps = document.querySelectorAll(".complete-the-fields");
function showDivStep() {
    const pStepNum = document.querySelectorAll(".stepNum");
    pStepNum.forEach((stepNum) => {
        if (stepNum.textContent == numDiv) {
            stepNum.parentElement.classList.add("active");
            stepNum.parentElement.classList.remove("activeLast");
        } else if (stepNum.textContent < numDiv) {
            stepNum.parentElement.classList.add("activeLast");
        } else {
            stepNum.parentElement.classList.remove("activeLast");
            stepNum.parentElement.classList.remove("active");
        }
    });
    hideAllDivOfSteps();
    hideAllDivOfMainContent();
    divEmpty.style.display = "flex";

    if (numDiv === 1) {
        const activeStepOne = document.querySelector(
            ".complete-the-fields.one"
        );
        activeStepOne.style.display = "flex";
    } else if (numDiv === 2) {
        const activeStepTwo = document.querySelector(
            ".complete-the-fields.two"
        );
        activeStepTwo.style.display = "flex";
    } else if (numDiv === 3) {
        const activeStepThree = document.querySelector(
            ".complete-the-fields.three"
        );
        activeStepThree.style.display = "flex";
    } else if (numDiv === 4) {
        const activeStepFour = document.querySelector(
            ".complete-the-fields.four"
        );
        activeStepFour.style.display = "flex";
    }
}
showDivStep();
function hideAllDivOfSteps() {
    allDivOfSteps.forEach((div) => {
        div.style.display = "none";
    });
}
function hideAllDivOfMainContent() {
    const AllDivInPart_2 = document.querySelectorAll(".part-2-2>div");
    AllDivInPart_2.forEach((div) => {
        div.style.display = "none";
    });
}
// --------------------

const btnGenerateIdeas = document.querySelector(".GenerateIdeas");
btnGenerateIdeas.addEventListener("click", () => {
    hideAllDivOfMainContent();
    const DivAllIdeas = document.querySelector(".AllIdeas");
    DivAllIdeas.style.display = "block";
});
// --------------------

const btnGenerateOutline = document.querySelector(".GenerateOutline");
btnGenerateOutline.addEventListener("click", function () {
    hideAllDivOfMainContent();
    const divAllOutline = document.querySelector(".AllOutline");
    divAllOutline.style.display = "block";
});
// ----------------------
const btnGenerateArticle = document.querySelector(".GenerateArticle");
btnGenerateArticle.addEventListener("click", () => {
    hideAllDivOfMainContent();
    const DivEndArt = document.querySelector(".endArt");
    DivEndArt.style.display = "block";
    const endStepLastActive = document.querySelector(".step-by-step .four");
    endStepLastActive.classList.add("activeLast");
});
// ----------------------

const iconDeleteKeyInIdeas = document.querySelectorAll(
    ".complete-the-fields.two .deleteKey"
);
iconDeleteKeyInIdeas.forEach((item) => {
    item.addEventListener("click", () => {
        iconDeleteKeyInIdeas.parentElement.remove();
    });
});

// ----------------------
function DeleteTalkingPoint() {
    const iconDeleteTalkingPoint = document.querySelectorAll(
        ".complete-the-fields.four .up .oneArt .icon-remove"
    );
    iconDeleteTalkingPoint.forEach((item) => {
        item.addEventListener("click", () => {
            item.parentElement.parentElement.remove();
        });
    });
}

DeleteTalkingPoint();
// ----------------------
const addTalkingPoint = document.querySelectorAll(".addTalkingPoint");
addTalkingPoint.forEach((inputAdd) => {
    inputAdd.addEventListener("keyup", (event) => {
        if (event.keyCode === 13 && inputAdd.value != "") {
            const point = document.createElement("div");
            point.classList.add("oneArt");
            point.innerHTML = `
                <img
                src="../../images/enable to darg and drop.svg"
                alt=""
                />
                <div class="img">
                    <ion-icon
                        name="checkmark-outline"
                    ></ion-icon>
                </div>
                <span>
                    <p>${inputAdd.value}</p>

                    <ion-icon
                        name="remove-outline"
                        class="icon-remove"
                    ></ion-icon>
                </span>
    `;
            inputAdd.parentNode.insertBefore(
                point,
                inputAdd.parentNode.lastElementChild
            );
            dragAndDrop();
            DeleteTalkingPoint();
            inputAdd.value = "";
        }
    });
});

function dragAndDrop() {
    const allCols = document.querySelectorAll(".Article-Outline .up");
    let items = document.querySelectorAll(".oneArt");
    items.forEach(function (element) {
        element.draggable = true;
    });

    let drag = null;
    items.forEach((column) => {
        column.addEventListener("dragstart", (e) => {
            e.dataTransfer.setData("text/plain", e.target.id);
            drag = column;
            column.style.opacity = 0.5;
        });

        column.addEventListener("dragend", () => {
            drag = null;
            column.style.opacity = 1;
        });

        allCols.forEach((col) => {
            col.addEventListener("dragover", function (e) {
                if (
                    drag &&
                    !drag.classList.contains("up") &&
                    this.classList.contains(drag.closest(".up").classList)
                ) {
                    e.preventDefault();
                }
            });
            col.addEventListener("dragleave", function () {
                this.style.background = "none";
            });
            col.addEventListener("drop", function (e) {
                if (
                    drag &&
                    !drag.classList.contains("up") &&
                    this.classList.contains(drag.closest(".up").classList)
                ) {
                    e.preventDefault();
                    this.insertBefore(drag, e.target);
                    this.style.background = "none";
                }
            });
        });
    });
}
dragAndDrop();
// -------------------

const divSelectedTone = document.querySelector(".divSelect.tone");
const divSelectedLanguage = document.querySelector(".divSelect.language");
const ulSelectTone = document.querySelector(".ulSelect.tone");
const ulSelectLanguage = document.querySelector(".ulSelect.language");
const liSelectLanguage = document.querySelectorAll(".ulSelect.language ul li");
const liSelectTone = document.querySelectorAll(".ulSelect.tone ul li");
const valueSelectLanguage = document.querySelector(
    ".divSelect.language .valueSelect"
);
const valueSelectTone = document.querySelector(".divSelect.tone .valueSelect");

divSelectedLanguage.addEventListener("click", () => {
    divSelectedLanguage.classList.toggle("active");
    ulSelectLanguage.classList.toggle("active");
});

divSelectedTone.addEventListener("click", () => {
    divSelectedTone.classList.toggle("active");
    ulSelectTone.classList.toggle("active");
});

liSelectLanguage.forEach((li) => {
    li.addEventListener("click", () => {
        valueSelectLanguage.innerHTML = li.innerHTML;
        ulSelectLanguage.classList.remove("active");
    });
});

liSelectTone.forEach((li) => {
    li.addEventListener("click", () => {
        valueSelectTone.innerHTML = li.innerHTML;
        ulSelectTone.classList.remove("active");
    });
});

// -----------------------
const iconExport=document.querySelector(".iconExport");
const divOptionExport=document.querySelector(".optionExport");
iconExport.addEventListener("click",()=>{
    divOptionExport.classList.toggle("active");
})