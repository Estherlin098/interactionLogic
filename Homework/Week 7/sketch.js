// Esther Lin Assginment 7
// https://kylemcdonald.github.io/cv-examples/
// https://github.com/kylemcdonald/AppropriatingNewTechnologies/wiki/Week-2

var capture;
var tracker
var w = 640,
    h = 480;

function preload() {
  img = loadImage('imagehat.png');
  pumpkin = loadImage('pumpkin.png');
}

function setup() {
    capture = createCapture({
        audio: false,
        video: {
            width: w,
            height: h
        }
    }, function() {
        console.log('capture ready.')
    });
    capture.elt.setAttribute('playsinline', '');
    createCanvas(w, h);
    capture.size(w, h);
    capture.hide();

    colorMode(HSB);

    tracker = new clm.tracker();
    tracker.init();
    tracker.start(capture.elt);
    textSize(20);
}

function draw() {
    image(capture, 0, 0, w, h);
    var positions = tracker.getCurrentPosition();
    console.log(positions);

    noFill();
    stroke(255);
    //draw line for between dots
    beginShape();
    for (var i = 0; i < positions.length; i++) {
      // vertex: used to specify the coordinates of the vertices used to draw a shape
        //vertex(positions[i][0], positions[i][1]); 
    }
  //draw line for between dots
    endShape();

    noStroke();
    textSize(10);
    for (var i = 0; i < positions.length; i++) {
        fill(map(i, 0, positions.length, 0, 360), 50, 100);
    }
    filter(GRAY);
    if (positions.length > 0) {
        image(img, positions[0][0]-60, positions[0][1]-300, 320, 240);
        image(pumpkin, positions[1][0], positions[1][1], 55, 55);
        image(pumpkin, positions[13][0]-40, positions[13][1], 55, 55);

    }
}
