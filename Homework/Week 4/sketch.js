// this is Esther Lin Homework 4
// october 3, 2021

function preload() {
  // pre-load font and image
  font = loadFont('AmericanTypeEF-Medium.otf');
  heart = loadImage('Heart.png')
}

function setup() {
  // create canvas and specify canvas size
  createCanvas(windowWidth, windowHeight);

  // set text characteristics
  textFont(font);
  
  // smallerText = textSize(70)
  textAlign(CENTER, CENTER);
  textArray1 = ['I', 'N', 'Y']
  textArray2 = ['MORE', 'THAN', 'EVER']

  // create a button called Reset, when the mouse is pressed, call the resetSketch function
  let button = createButton("Reset");
  button.mousePressed(resetSketch);
}

// clear the canvas when the reset button is pressed
function resetSketch() {
  background(255);
  poster();
}

function draw() {
  // when mouse is pressed, randomize one grey color, 
  // change the cursor to CROSS, and call poster function
  if (mouseIsPressed) {
    fill(random(0, 255));
    cursor(CROSS)
    poster();
  }
}

function poster() {
  // set the text Size to 120
  textSize(120);
  
  // set the gap between letters and the left and top margin
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
  textSize(60);

  for (let y = 210; y < height - gap; y += gap) {
    let phrase = textArray2[counter];
    text (phrase, mouseX + 100, mouseY + y);
    counter++;
  }
}