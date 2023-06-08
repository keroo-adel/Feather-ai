
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
    const messageText = document.createElement('p');
    messageText.innerText = inputChat.value;

    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', 'me');
    messageDiv.innerHTML = `
        <div class="img">
            <img src="${staticUrl}/MyPersonalPhoto.svg" alt="">
        </div>
        <div class="text"></div>
    `;
    messageDiv.querySelector('.text').appendChild(messageText);

    divChatWithAi.appendChild(messageDiv);
    inputChat.focus();

    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    fetch('send_message/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({
          chat_id: activeChatId,
          message: inputChat.value,
        }),
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
            <div class="copy" onclick="copyToClipboard('${responseText}')">
                <ion-icon
                    name="copy-outline"
                ></ion-icon>
            </div>
        </div>
    </div>
	`;
    divChatWithAi.insertAdjacentHTML("beforeend", message);
    scrollBottom();

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
});

function copyToClipboard(text) {
    const tempInput = document.createElement('input');
    tempInput.value = text;
    document.body.appendChild(tempInput);
    tempInput.select();
    document.execCommand('copy');
    document.body.removeChild(tempInput);
    
    const copyIcon = document.querySelector('.copy-icon');
    copyIcon.setAttribute('name', 'checkmark-outline');  // Change the icon name

    const tooltip = document.querySelector('.tooltip');
    tooltip.innerText = 'copied!';

    setTimeout(() => {
        tooltip.innerText = 'copy';  // Clear the inner text
        copyIcon.setAttribute('name', 'copy-outline');  // Reset the icon name
    }, 3000);
}
