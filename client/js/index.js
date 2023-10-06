const changeTitle = () => {
  const chrome = window.chrome || browser; // for cross-browser compatibility
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    chrome.tabs.sendMessage(tabs[0].id, { message: "main" }, (response) => {
      console.log(response);
    });
  });
};
const board = Chessboard("myBoard", "start");
document.getElementById("changeTitle").addEventListener("click", changeTitle);
