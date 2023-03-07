// MESSAGES
const messagesNotification = document.querySelector("#messages-notification");
const messages = document.querySelector(".messages");
const message = messages.querySelectorAll(".message");
const messageSearch = document.querySelector("#message-search");

// ================== MESSAGES ====================

// searches chats
const searchMessage = () => {
    const val = messageSearch.value.toLowerCase();
    console.log(val);
    message.forEach((chat) => {
      let name = chat.querySelector("h5").textContent.toLowerCase();
      if (name.indexOf(val) != -1) {
        chat.style.display = "flex";
      } else {
        chat.style.display = "none";
      }
    });
  };
  
  // search chat
  messageSearch.addEventListener("keyup", searchMessage);
  
  // hightlight messages card when messages menu item is clicked
  messagesNotification.addEventListener("click", () => {
    messages.style.boxShadow = " 0 0 1rem var(--color-primary)";
    messagesNotification.querySelector(".notification-count").style.display =
      "none";
    setTimeout(() => {
      messages.style.boxShadow = "none";
    }, 2000);
  });