const divWelcome = document.querySelector(".welcome");
const divSomePrompts = document.querySelector(".some-prompts");
const inputChat = document.querySelector(".input-chat #inputChat");
const divChatWithAi = document.querySelector(".chat-with-ai");
const sentMessage = document.querySelector(".sent");

inputChat.focus();

inputChat.addEventListener("keydown", function (event) {
    if (event.shiftKey && key === 13) {
        inputChat.value += "\n";
        event.preventDefault();
    } else if (event.key === "Enter") {
        createChatAi();
    }
});
sentMessage.addEventListener("click", function () {
    createChatAi();
});

function createChatAi() {
    
    if (inputChat.value.trim() !=="") {
        divWelcome.style.display = "none";
        divSomePrompts.style.display = "none";
        divChatWithAi.style.display = "flex";
        writeMessage();
    }
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
    let lastMessage = divChatWithAi.lastElementChild;
    let aiText = null;

    if (lastMessage && lastMessage.classList.contains('ai')) {
        aiText = lastMessage.querySelector('.text #ai-text');
    } else {
        let message = `
        <div class="message ai">
            <div class="img">
                <img src="${staticUrl}/robot.svg" alt="" />
            </div>
            <div class="text">
                <p id="ai-text"></p>
                <div class="copy" onclick="copyToClipboard('${responseText}', '${activeChatId}')">
                    <ion-icon name="copy-outline"></ion-icon>
                </div>
            </div>
        </div>
        `;
        divChatWithAi.insertAdjacentHTML('beforeend', message);
        lastMessage = divChatWithAi.lastElementChild;
        aiText = lastMessage.querySelector('.text #ai-text');
    }

    const textLength = responseText.length;
    let index = 0;

    const typeText = () => {
        aiText.textContent += responseText[index];
        index++;
        if (index < textLength) {
            setTimeout(typeText, 20); // Adjust the typing speed here
        } else {
            scrollChatBoxToBottom();
        }
    };

    const scrollChatBoxToBottom = () => {
        divChatWithAi.scrollTop = divChatWithAi.scrollHeight;
    };

    typeText();

    // Create a MutationObserver to listen for changes in the chat box size
    const observer = new MutationObserver(scrollChatBoxToBottom);
    observer.observe(divChatWithAi, { attributes: true, childList: true, subtree: true });
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

// ------------------

inputChat.addEventListener("input", () => {
    const numberOfLines = inputChat.value.split("\n").length;
    if (numberOfLines > 1) {
        inputChat.style.height = "auto";
        inputChat.style.height = inputChat.scrollHeight + "px";
        divSomePrompts.style.display = "none";
    } else {
        inputChat.style.height = "2rem";
    }
});

inputChat.addEventListener("input", () => {
    const numberOfLines = inputChat.value.split("\n").length;
    if (numberOfLines > 1) {
        inputChat.style.height = "auto";
        inputChat.style.height = inputChat.scrollHeight + "px";
        divSomePrompts.style.display = "none";
    } else {
        inputChat.style.height = "2rem";
    }
});
function copyToClipboard(response, messageId) {
    const tempInput = document.createElement('input');
    tempInput.value = response;
    document.body.appendChild(tempInput);
    tempInput.select();
    document.execCommand('copy');
    document.body.removeChild(tempInput);

    const copyIcon = document.querySelector(`.copy-icon-${messageId}`);
    if (!copyIcon) return;
    copyIcon.setAttribute('name', 'checkmark-outline');  // Change the icon name

    const tooltip = document.querySelector(`.tooltip-${messageId}`);
    if (!tooltip) return;
    tooltip.innerText = 'copied!';

    setTimeout(() => {
        tooltip.innerText = 'copy';  // Clear the inner text
        copyIcon.setAttribute('name', 'copy-outline');  // Reset the icon name
    }, 3000);
}
