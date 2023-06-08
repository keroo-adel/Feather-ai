const divAppearAllEmails = document.getElementById("all-emails");
const divPart2=document.querySelector(".part-2");
let emailsSaved = [
    // {
    //     id:1,
    //     content:`
    //     Welcome to [Product/Service Name]! 
    //     Dear [Name], 
    
    //     We are excited to welcome you as a new customer of [Product/Service Name]! We believe that our [Product/Service] will be an essential part of your journey ahead. 
    
    //     As a courtesy, [add any details about any special offers]. To learn more about [Product/Service Name], we invite you to explore our website and feel free to contact our team of experts with any questions that may arise. 
    
    //     We hope your experience with us is both enjoyable and beneficial!
    
    //     Warm regards, 
    //     [Name/Company] Team
    //     `
    // },
    // {
    //     id:2,
    //     content:`
    //     Welcome to [Product/Service Name]! 
    //     Dear [Name], 
    
    //     We are excited to welcome you as a new customer of [Product/Service Name]! We believe that our [Product/Service] will be an essential part of your journey ahead. 
    
    //     As a courtesy, [add any details about any special offers]. To learn more about [Product/Service Name], we invite you to explore our website and feel free to contact our team of experts with any questions that may arise. 
    
    //     We hope your experience with us is both enjoyable and beneficial!
    
    //     Warm regards, 
    //     [Name/Company] Team
    //     `
    // },
    // {
    //     id:2,
    //     content:`
    //     Welcome to [Product/Service Name]! 
    //     Dear [Name], 
    
    //     We are excited to welcome you as a new customer of [Product/Service Name]! We believe that our [Product/Service] will be an essential part of your journey ahead. 
    
    //     As a courtesy, [add any details about any special offers]. To learn more about [Product/Service Name], we invite you to explore our website and feel free to contact our team of experts with any questions that may arise. 
    
    //     We hope your experience with us is both enjoyable and beneficial!
    
    //     Warm regards, 
    //     [Name/Company] Team
    //     `
    // }
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