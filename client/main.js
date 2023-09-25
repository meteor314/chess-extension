const getDataFigurine = (selector, context) => {
  const el = (context || document).querySelector(selector);
  return el ? el.getAttribute("data-figurine") : "";
};

const moves = document.querySelectorAll(".move");
const chessMoves = [];

moves.forEach((move, index) => {
  if (index === moves.length - 1) return; // stop before the last move
  // get the text after div.white.node or div.black.node
  const whiteMove = move.querySelector(".white.node").textContent;
  const blackMove = move.querySelector(".black.node").textContent;

  // get the from  classs span.icon-font-chess data-figurine="value"
  const pieceNameWhite = getDataFigurine(
    ".white.node span.icon-font-chess",
    move
  );
  let pieceNameBlack = getDataFigurine(
    ".black.node span.icon-font-chess",
    move
  );

  chessMoves.push({
    whiteMove: pieceNameWhite + whiteMove,
    blackMove: pieceNameBlack + blackMove,
  });
});
