// this is Esther Lin Homework 4
// October 3, 2021

function preload() {
  // Pre-load font and image
  font = loadFont('AmericanTypeEF-Medium.otf');
  heart = loadImage('Heart.png')
}

function setup() {
  // Create canvas and specify canvas size
  createCanvas(1950, 1300);

  // Set text characteristics
  textFont(font);
  
  //smallerText = textSize(70)
  textAlign(CENTER, CENTER);
  textArray1 = ['I', 'N', 'Y']
  textArray2 = ['MORE', 'THAN', 'EVER']
}

function draw() {
  if (mouseIsPressed) {
    fill(random(0, 211)), random(221), random(0, 221);
    Poster();
  } 
}

function Poster() {
  // set the text Size to 120
  textSize(120);
  
  // Set the gap between letters and the left and top margin
  let gap = 65;
  let margin = 20;
  translate(margin * 1, margin * 1);

  // letter I 
  let letter = textArray1[0];
  text(letter,mouseX + 50, mouseY + 30)

  // display the heart to the scree
  image(heart, mouseX + 90, mouseY + 0)
  heart.resize (78, 75)

  // letter N
  let letter2 = textArray1[1];
  text(letter2, mouseX + 50, mouseY + 120)

  // letter Y
  let letter3 = textArray1[2];
  text(letter3,mouseX + 150, mouseY + 120)

  // draw MORE THAN EVER
  let counter = 0;
  // set the text Size to 60
  textSize(60);

  for (let y = 210; y < height - gap; y += gap) {
    let phrase = textArray2[counter];
    text (phrase, mouseX + 100, mouseY + y);
    counter++;
  }
}
