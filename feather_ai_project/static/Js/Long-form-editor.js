let blockClassType = "paragraphStyle";

function formatDoc(cmd, value = null) {
    if (value) {
        document.execCommand(cmd, false, value);
    } else {
        document.execCommand(cmd);
    }
}

function addLink() {
    const url = prompt("Insert url");
    formatDoc("createLink", url);
}

const content = document.getElementById("content");

content.addEventListener("mouseenter", function () {
    const a = content.querySelectorAll("a");
    a.forEach((item) => {
        item.addEventListener("mouseenter", function () {
            content.setAttribute("contenteditable", false);
            item.target = "_blank";
        });
        item.addEventListener("mouseleave", function () {
            content.setAttribute("contenteditable", true);
        });
    });
});

// -------------------------------------
const inputField = document.getElementById("headTitle");
let originalValue = inputField.value;
let isEditing = false;

inputField.addEventListener("click", () => {
    if (!isEditing) {
        inputField.removeAttribute("readonly");
        originalValue = inputField.value;
        isEditing = true;
    }
});

inputField.addEventListener("keydown", (event) => {
    if (isEditing && event.key === "Enter") {
        saveArticleTitle();
        inputField.setAttribute("readonly", true);
        isEditing = false;
    }
});

inputField.addEventListener("blur", () => {
    if (isEditing) {
        saveArticleTitle();
        inputField.setAttribute("readonly", true);
        isEditing = false;
    }
});

function saveArticleTitle() {
    const title = inputField.value.trim(); // Trim whitespace from the title

    // Check if the title is empty
    if (title === "") {
        return; // Don't save if the title is empty
    }

    // Save the article title to the database via an API endpoint
    const formData = new FormData();
    formData.append('article_title', title);
    const csrftoken = getCookie('csrftoken'); // Replace with your method of retrieving the CSRF token

    fetch('api/save-article-title/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
        },
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        console.log(data); // Optional: Handle the response from the server
    })
    .catch(error => {
        console.error(error); // Optional: Handle any errors that occur during the request
    });
}

// -------------------------------------
const divAskFeather = document.querySelector(".askFeather");
const mainInput = document.querySelector("#mainInput");
const inputDraftWithAi = document.getElementById("inputDraftWithAi");
const selectOptions = document.querySelectorAll(".select .option");
const divStepOne = document.querySelector(".step1");
const divStepTwo = document.querySelector(".step2");
const optionReload = document.querySelector(".reload");
const optionClose = document.querySelectorAll(".option.close");

selectOptions.forEach((option) => {
    option.addEventListener("click", () => {
        const optionValue = option.querySelector("p").textContent.trim();
        inputDraftWithAi.value = optionValue;
    });
});


inputDraftWithAi.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
        const question_value = inputDraftWithAi.value.trim();
       
        if (question_value !== "") {
            // Send the question to the server
            fetch('api/ask-feather/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ question: question_value }),
            })
            .then(response => response.json())
            .then(data => {
                // Handle the response from the server
                console.log(data);

                // Check if the response contains the necessary data for creating a block
                if (data.answer) {
                    const content = data.answer;
                    // Create a block using the response data
                    createBlock(content, blockClassType);
                }
            })
            .catch(error => {
                console.error(error); // Optional: Handle any errors that occur during the request
            });

            inputDraftWithAi.placeholder = "Tell Al what to do next...";
            divStepOne.style.display = "none";
            divStepTwo.style.display = "flex";
            inputDraftWithAi.value = "";
        }
    }
});

// optionReload.addEventListener("click", () => {
//     location.reload();
// });

optionClose.forEach((option) => {
    option.addEventListener("click", () => {
        resetAskAiDiv();
    });
});

function resetAskAiDiv() {
    divAskFeather.style.display = "none";
    inputDraftWithAi.placeholder = "Ask Feather.Al to write anything...";
    divStepTwo.style.display = "none";
    divStepOne.style.display = "flex";
    inputDraftWithAi.value = "";
}

document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
        resetAskAiDiv();
    }
});

// --------------------------------
const optionH1 = document.querySelector(".commandsOption .h1");
const optionH2 = document.querySelector(".commandsOption .h2");
const optionH3 = document.querySelector(".commandsOption .h3");
const optionParagraph = document.querySelector(".commandsOption .paragraph");
const optionBullet = document.querySelector(".commandsOption .bullet-list");
const optionAskAi = document.querySelector(".commandsOption .askAi");
const divCommandsOption = document.querySelector(".commandsOption");

mainInput.addEventListener("input", function (event) {
    const inputValue = event.target.value;
    const modifiedValue = inputValue.replace(/\//g, "");
    event.target.value = modifiedValue;
});

mainInput.addEventListener("keydown", function (event) {
    divAskFeather.style.display = "none";
    if (event.key === "/") {
        divCommandsOption.style.display = "block";
        optionH1.addEventListener("click", () => {
            blockClassType = "h1Style";
            hideDivCommandsOption();
        });
        optionH2.addEventListener("click", () => {
            blockClassType = "h2Style";
            hideDivCommandsOption();
        });
        optionH3.addEventListener("click", () => {
            blockClassType = "h3Style";
            hideDivCommandsOption();
        });
        optionParagraph.addEventListener("click", () => {
            blockClassType = "paragraphStyle";
            hideDivCommandsOption();
        });
        optionBullet.addEventListener("click", () => {
            blockClassType = "listStyle";
            hideDivCommandsOption();
        });
        optionAskAi.addEventListener("click", () => {
            hideDivCommandsOption();
            divAskFeather.style.display = "block";
        });
    } else if (
        event.key === "Enter" &&
        divCommandsOption.style.display === "none" && 
        mainInput.value !=""
    ) {
        createBlock(mainInput.value, blockClassType);
        blockClassType = "paragraphStyle";
        mainInput.setAttribute("class", `${blockClassType}`);
        mainInput.value = "";
    } else if (event.key != "ArrowUp" && event.key != "ArrowDown") {
        divCommandsOption.style.display = "none";
    }
});

function hideDivCommandsOption() {
    divCommandsOption.style.display = "none";
    mainInput.focus();
    mainInput.setAttribute("class", `${blockClassType}`);
}

function deleteSlash() {
    const inputValue = mainInput.value;
    const modifiedValue = inputValue.slice(0, -1);
    mainInput.value = modifiedValue;
}

function generateBlockId() {
    // Generate a UUID (Universally Unique Identifier)
    return Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15);
  }
  
  function createBlock(value, classType) {
    const block = document.createElement("div");
    const blockId = generateBlockId();
    block.setAttribute("class", `newBlock ${classType}`);
    block.setAttribute("data-block-id", blockId);
    block.innerHTML = `
      <img src="${window.location.origin}/static/images/enable to darg and drop.svg"/>
      <ion-icon name="radio-button-on-outline"></ion-icon>
      <p>${value}</p>
    `;
  
    content.appendChild(block);
  
    // Save the block to the database via an API endpoint
    const formData = new FormData();
    formData.append('content', value);
    formData.append('block_type', classType);
    formData.append('position', content.children.length);
    formData.append('unique_id', blockId);
    const csrftoken = getCookie('csrftoken'); // Replace with your method of retrieving the CSRF token
  
    fetch('api/create-block/', {
      method: 'POST',
      headers: {
        'X-CSRFToken': csrftoken,
      },
      body: formData,
    })
    .then(response => response.json())
    .then(data => {
      console.log(data); // Optional: Handle the response from the server
    })
    .catch(error => {
      console.error(error); // Optional: Handle any errors that occur during the request
    });
  
    dragAndDrop();
  }
function getCookie(name) {
    const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
    return cookieValue ? cookieValue.pop() : '';
}

// ---------------

const myList = document.querySelector(".commandsOption ul");
const listItems = myList.querySelectorAll("li");
let focusedIndex = -1;

mainInput.addEventListener("keydown", function (event) {
    
        if (event.key === "ArrowUp") {
            focusedIndex = Math.max(focusedIndex - 1, 0);
            updateFocus();
            event.preventDefault();
        } else if (event.key === "ArrowDown") {
            focusedIndex = Math.min(focusedIndex + 1, listItems.length - 1);
            updateFocus();
            event.preventDefault();
        } else if (event.key === "Enter" && focusedIndex !== -1) {
            listItems.forEach((option, index) => {
                if (index === focusedIndex) {
                    option.click();
                }
            });
        }
    
});

function updateFocus() {
    listItems.forEach((item, index) => {
        if (index === focusedIndex) {
            item.classList.add("focused");
        } else {
            item.classList.remove("focused");
        }
    });
}

myList.addEventListener("mouseover", function (event) {
    const target = event.target;
    if (target.tagName === "LI") {
        focusedIndex = Array.from(listItems).indexOf(target);
        updateFocus();
    }
});

updateFocus();

// -----------------------
function dragAndDrop() {
    const allCols = document.querySelector("#content");
    let items = document.querySelectorAll(".newBlock");
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
  
        // Call the function to update block positions
        updateBlockPositions();
      });
  
      allCols.addEventListener("dragover", function (e) {
        if (
          drag &&
          !drag.classList.contains("upContent") &&
          this.classList.contains(drag.closest(".upContent").classList)
        ) {
          e.preventDefault();
        }
      });
      allCols.addEventListener("dragleave", function () {
        this.style.background = "none";
      });
      allCols.addEventListener("drop", function (e) {
        if (
          drag &&
          !drag.classList.contains("upContent") &&
          this.classList.contains(drag.closest(".upContent").classList)
        ) {
          e.preventDefault();
          this.insertBefore(drag, e.target);
          this.style.background = "none";
  
          // Call the function to update block positions
          updateBlockPositions();
        }
      });
    });
  }
  
  function updateBlockPositions() {
    const blocks = document.querySelectorAll('.newBlock');
    const positions = [];
  
    blocks.forEach((block, index) => {
      const blockId = block.dataset.blockId;
      positions.push({ id: blockId, position: index });
    });
  
    // Send the positions data to the API endpoint
    fetch('api/update-block-positions/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken'),
      },
      body: JSON.stringify(positions),
    })
    .then((response) => {
      if (response.ok) {
        console.log('Block positions updated successfully');
      } else {
        console.log('Error updating block positions');
      }
    })
    .catch((error) => {
      console.log('Error:', error);
    });
  }
  