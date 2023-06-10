const divPreviousRequests = document.querySelector(".previous-requests");
let arrAllRequests = [
    {
        id: 1,
        name: "Al Article Writer",
        time: "12 minutes ago",
        lang: "english",
    },
    {
        id: 2,
        name: "Al Article Writer",
        time: "12 minutes ago",
        lang: "english",
    },
    {
        id: 3,
        name: "Al Article Writer",
        time: "12 minutes ago",
        lang: "english",
    },
    {
        id: 4,
        name: "Al Article Writer",
        time: "12 minutes ago",
        lang: "english",
    },
];

arrAllRequests.forEach((element) => {
    let divRequest = `
    <div class="requests">
        <div>
            <img
                src="${staticUrl}/timer-2.svg"
                alt="chat logo"
            />
        </div>
        <div>
            <p>${element.name}</p>
            <div class="details">
                <img src="${staticUrl}/timer.svg" alt="clock icon">
                <p>created ${element.time}</p>
                <img src="${staticUrl}/location.svg" alt="language:">
                <p>${element.lang}</p>
            </div>
        </div>
    </div>
    `;
    divPreviousRequests.insertAdjacentHTML("beforeend", divRequest);
});
