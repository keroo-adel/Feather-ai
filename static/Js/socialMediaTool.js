const divAppearAllEmails = document.getElementById("all-emails");
const divPart2=document.querySelector(".part-2");

let emailsSaved = [
    {
        id:1,
        content:`
        It's time to Start my day with a little sunshine and a cup Of coffee. I just got back
from a long run and I'm ready to get to work. #coffee #sunset
        `
    },
    {
        id:2,
        content:`
        I'm excited to start my day today! I just got back from a run and I'm ready to get
to work, but first, I'll need a little caffeine. #coffee
        `
    }
    ,
    {
        id:2,
        content:`
        I'm excited to start my day today! I just got back from a run and I'm ready to get
to work, but first, I'll need a little caffeine. #coffee
        `
    },
    {
        id:2,
        content:`
        I'm excited to start my day today! I just got back from a run and I'm ready to get
to work, but first, I'll need a little caffeine. #coffee
        `
    },
    {
        id:2,
        content:`
        I'm excited to start my day today! I just got back from a run and I'm ready to get
to work, but first, I'll need a little caffeine. #coffee
        `
    },
    {
        id:2,
        content:`
        I'm excited to start my day today! I just got back from a run and I'm ready to get
to work, but first, I'll need a little caffeine. #coffee
        `
    },
    {
        id:2,
        content:`
        I'm excited to start my day today! I just got back from a run and I'm ready to get
to work, but first, I'll need a little caffeine. #coffee
        `
    },
    {
        id:2,
        content:`
        I'm excited to start my day today! I just got back from a run and I'm ready to get
to work, but first, I'll need a little caffeine. #coffee
        `
    }
];

if(emailsSaved.length==0){
    divAppearAllEmails.classList.add("hide");
    divPart2.classList.add("onePage");
}else{
    divAppearAllEmails.classList.remove("hide");
    divPart2.classList.remove("onePage");
emailsSaved.forEach(element => {
    let emailContent=element.content;
    let divEmail=`
    <div class="email">
        <p id="email-text">${emailContent}</p>
        <div class="icon">
            <img src="../../images/copy.svg" alt="icon copy" class="copy">
            <img src="../../images/Icon  trash.svg" alt=" icon trash ">
            <img src="../../images/Icon ben.svg" alt="icon ben">
        </div>
    </div>
    `
    divAppearAllEmails.insertAdjacentHTML("beforeend", divEmail);
    const btnCopy = document.querySelector(".copy");
    btnCopy.addEventListener("click", (e) => {
        let text = document.querySelector("#email-text").innerText;
        navigator.clipboard.writeText(text);
        alert("Text copied to clipboard!");
    });
});
}