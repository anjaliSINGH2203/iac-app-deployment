const {createCanvas, loadImage} = require('canvas');

const canvas = createCanvas(800, 600);
const ctx = canvas.getContext('2d');

// ... (Rest of the game logic in Node.js) 

module.exports = {
  canvas,
  ctx
};
