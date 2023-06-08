
const divWelcome = document.querySelector(".welcome");
const divSomePrompts = document.querySelector(".some-prompts");
const InputChat = document.querySelector(".input-chat input");
const divChatWithAi = document.querySelector(".chat-with-ai");
const sentMessage = document.querySelector(".sent");
const inputChat = document.getElementById("inputChat");
InputChat.focus();

InputChat.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
        createChatAi();
    }
});

sentMessage.addEventListener("click", function () {
    createChatAi();
});

function createChatAi() {
    const valueInputChat = inputChat.value;
    
    if (isValid(valueInputChat)) {
        divWelcome.style.display = "none";
        divSomePrompts.style.display = "none";
        divChatWithAi.style.display = "flex";
        writeMessage();
    }
}

function isValid(value) {
    return value.length > 0;
}

function writeMessage() {
    let message = `
    <div class="message me">
        <div class="img">
            <img src="
            ${staticUrl}/MyPersonalPhoto.svg"
            
            " alt="">
        </div>
        <div class="text">
            <p>
                ${inputChat.value}
            </p>
        </div>
    </div>
	`;

    divChatWithAi.insertAdjacentHTML("beforeend", message);
    inputChat.focus();

    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
const headers = {
  'Content-Type': 'application/json',
  'X-CSRFToken': csrfToken,
};

    fetch(`send_message/${activeChatId}/${inputChat.value}/`, {
        method: 'POST',
        headers: headers,
      })
        .then(response => response.text())
        .then(responseText => {
            autoReply(responseText);
          })
        .catch(error => {
          console.error('Error:', error);
        });
  
    inputChat.value = "";
    scrollBottom();
}

function autoReply(responseText) {
    let message = `
    <div class="message ai">
        <div class="img">
            <img
                src= ${staticUrl}/robot.svg
                alt=""
            />
        </div>
        <div class="text">
            <p id="ai-text">
                ${responseText}
            </p>
            <div class="copy">
                <ion-icon
                    name="copy-outline"
                ></ion-icon>
            </div>
        </div>
    </div>
	`;
    divChatWithAi.insertAdjacentHTML("beforeend", message);
    scrollBottom();
    
    const btnCopy = document.querySelector(".copy");
    btnCopy.addEventListener("click", () => {
        let text = document.querySelector("#ai-text").innerText;
        navigator.clipboard.writeText(text);
        alert("Text copied to clipboard!");
    });
}

function scrollBottom() {
    divChatWithAi.scrollTo(0, divChatWithAi.scrollHeight);
}

// document.addEventListener("keydown", function (event) {
//     if (event.code === "Space") {
//         InputChat.focus();
//     }
// });
// ---------------
const paragraphFeatures = document.querySelectorAll(
    ".some-features .feature > div:nth-of-type(2)"
);

paragraphFeatures.forEach((div) => {
    div.addEventListener("click", () => {
        const text = div.querySelector("p").innerText;
        inputChat.value = text;
    });
});
// ---------------

const recordButton = document.getElementById("mic");
const recognition = new window.webkitSpeechRecognition();
let isRecording = false;

recognition.continuous = true;

recordButton.addEventListener("click", () => {
    if (!isRecording) {
        recognition.start();
        recordButton.src=staticUrl+'Icon  mic.svg';
    } else {
        recognition.stop();
        recordButton.src=staticUrl+'Icon  mic-2.svg';
    }
    isRecording = !isRecording;
});

recognition.addEventListener("result", (event) => {
    for (let i = event.resultIndex; i < event.results.length; i++) {
        if (event.results[i].isFinal) {
            inputChat.value += event.results[i][0].transcript;
        }
    }
});

recognition.addEventListener("end", () => {
    if (isRecording) {
        recognition.start();
    }
});;


