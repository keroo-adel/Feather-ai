const containerPage = document.querySelector(".container");
const mainPage = document.querySelector(".sec-home");

// nav ----------------------------------
const createNav = document.createElement("nav");
// ... Add your JavaScript actions for the nav here ...
containerPage.prepend(createNav);

// aside -------------------------------


// -------------------------------
const profileInfo = document.getElementById("profile-info");
const btnProfileInfo = document.getElementById("btnProfileInfo");
const asideNav = document.getElementById("aside-nav");
const btnToggleAsideActive = document.getElementById("btnToggleAside");

btnProfileInfo.addEventListener("click", () => {
    profileInfo.classList.toggle("active");
});

btnToggleAsideActive.addEventListener("click", () => {
    asideNav.classList.toggle("active");
});

window.addEventListener("click", function (event) {
    if (event.target !== profileInfo && event.target !== btnProfileInfo) {
        profileInfo.classList.remove("active");
    }
});
// ---------------------------
const currentUrl = window.location.href;
const links = document.querySelectorAll("aside ul li a");
for (let i = 0; i < links.length; i++) {
    const link = links[i];
    const url = link.href;

    if (currentUrl === url) {
        link.parentElement.classList.add("active");
        break;
    }
}
