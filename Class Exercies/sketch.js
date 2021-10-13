
let bugs = []; // Declare object
let numberOfBugs = 100;

function setup() {
  createCanvas(710, 400);
  // Create object
  //bug = new Jitter();
  //bugTwo = new Jitter();

  for (let i=0; i < numberOfBugs; i++) {
    bugs.push(new Jitter());
  }
}

function draw() {
  background(50, 89, 100);
  for (let i=0; i < numberOfBugs; i++) {
    bugs[i].move();
    bugs[i].display();
    bugs[i].changeColor();

    if (i%10 ==0) {
      bugs[i].diameter = 100;
    }
  }
  // bug.move();
  // bugTwo.move();
  // bug.display();
  // bugTwo.display();
}

// Jitter class
class Jitter {
  constructor() {
    this.x = random(width);
    this.y = random(height);
    this.diameter = random(10, 30);
    this.speed = 1;
    this.color = (random(0, 255))
  }

  move() {
    this.x += random(-this.speed, this.speed);
    this.y += random(-this.speed, this.speed);
  }

  display() {
    ellipse(this.x, this.y, this.diameter, this.diameter);
  }
  
  changeColor() {
    fill(random(0,255));
  }
}
