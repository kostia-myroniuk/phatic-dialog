// import { startPoint } from "./helpers/events/startPoint.mjs";

// startPoint();
const url = "http://localhost:3050/bot";


const fetchPost = async (link, jsonObject) => {
  try {
    const response = await fetch(link, {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify(jsonObject),
    });

    const isResponseOk = response.ok;
    const status = response.status;

    const responseBody = await response.json();

    if (!isResponseOk && responseBody.message) {
      throw responseBody.message;
    } else if (!isResponseOk) {
      throw `some error occured, server responded with status ${status}`;
    }

    return responseBody;
  } catch (err) {
    if (err) {
      throw err;
    }
  }
};

const startPoint = async () => {
  const chatInput = document.getElementById("chatinput");
  const sendButton = document.getElementById("sendbtn");
  sendButton.innerText = "Відправити";
  sendButton.addEventListener("click", async () => {
    const inputValue = chatInput.value;
    if (inputValue.trim() == "") {
      return;
    }
    
    const reqBody = {message: inputValue}
    const response = await fetchPost(url, reqBody);

    const elemQ = document.createElement('div');
    elemQ.classList.add("message-from");
    elemQ.innerText = "Ви: " + inputValue;

    const elemA = document.createElement('div');
    elemA.classList.add("message-to");
    elemA.innerText = "Бот: " + response.row;
    
    chatInput.parentNode.insertBefore(elemQ, chatInput);
    chatInput.parentNode.insertBefore(elemA, chatInput);

    chatInput.value = '';
  });
};

startPoint();
