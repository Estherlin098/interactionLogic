// this is Esther week 6 homework
// this is based on ITP NYU, serial communication example

var portName = '/dev/tty.usbserial-14410';  // fill in your serial port name here
var serial;          // variable to hold an instance of the serialport library
var inData;   // variable to hold the input data from Arduino
var outData = 0;  // variable to hold the output data to Arduino
var rightSlider;    // slider for controlling

function setup() {
  // set the canvas to match the window size
  createCanvas(windowWidth, windowHeight);
  noStroke();

  // set up right slider
  rightSlider = createSlider(0, 255, 0);
  rightSlider.position(width/2 + (width/2-300)/2 , height-100);
  rightSlider.style('width', '300px');

  //set up communication port
  serial = new p5.SerialPort();       // make a new instance of the serialport library
  serial.on('list', printList);  // set a callback function for the serialport list event
  serial.on('connected', serverConnected); // callback for connecting to the server
  serial.on('open', portOpen);        // callback for the port opening
  serial.on('data', serialEvent);     // callback for when new data arrives
  serial.on('error', serialError);    // callback for errors
  serial.on('close', portClose);      // callback for the port closing

  serial.list();                      // list the serial ports
  serial.open(portName);              // open a serial port
}

function draw() {
  // set background to black
  background(0);

  // drawing the left side to viuslize the volume graph
  var leftBrightness = map(inData, 0, 255, 0, 255);   // map input to the correct range of brightness
  fill(leftBrightness);   // transfer the brightness to brightness of the color used for drawing

  //show the rectangles based on the knob
  if (inData > 0) {
    rect(windowWidth/15 + 20, windowHeight/3, 60, windowWidth/8);   // rec 1
    if (inData > 51) {
      rect(windowWidth/15 + 100, windowHeight/3 - 40, 60, windowWidth/8 + 40);   // rec 2
      if (inData > 102) {
        rect(windowWidth/15 + 180, windowHeight/3 - 80, 60, windowWidth/8 + 80);   // rec 3
        if (inData > 153) {
          rect(windowWidth/15 + 260, windowHeight/3 - 120, 60, windowWidth/8 + 120);   // rec 4
          if (inData > 204) {
            rect(windowWidth/15 + 340, windowHeight/3 - 160, 60, windowWidth/8 + 160);   // rec 5
          }
        }
      }
    }
  } 

  // draw the text - left
  var textLColor = map(leftBrightness, 0, 255, 255,0);  // inverse the color for drawing the text on background
  fill(textLColor);
  textSize(16);
  text("ARDUINO LIGHT", 30, 30);
  textSize(12);
  text("BRIGHTNESS LEVEL: " + inData, 30, 50);    // displaying the input

  textSize(25);
  fill(255);
  text ("If only I could adjust my WIFI signal as easy as this...", windowWidth/15+20, windowHeight/1.5 -30);

  // right side setup, using a variable for Part 3 purpose, currently it does not change
  var rightBrightness = map(rightSlider.value(), 0, 255, 0, 255);   // read the value from slider and write to visualization
  fill(rightBrightness, 0 , rightBrightness);
  rect(width/2,0,windowWidth/2,windowHeight); // right half
  
  // set up serial output, to write the control value to the port
  outData = rightBrightness;
  serial.write(outData);

  // draw the text - right
  var textRColor = map(rightBrightness, 0, 255, 255,0);
  fill(textRColor);
  textSize(16);
  text("MY LED", windowWidth - 70, 30);
  textSize(12);
  rightBrightness = map(rightBrightness, 0, 255, 0, 100)
  text("BRIGHTNESS LEVEL: " + rightBrightness + "%", windowWidth - 170, 50);

  // draw the separator between frames
  fill(255);
  rect(windowWidth/2 - 0.5, 0, 1, windowHeight);
}


// Following functions print the serial communication status to the console for debugging purposes

function printList(portList) {
 // portList is an array of serial port names
 for (var i = 0; i < portList.length; i++) {
 // Display the list the console:
 print(i + " " + portList[i]);
 }
}

function serverConnected() {
  print('connected to server.');
}

function portOpen() {
  print('the serial port opened.')
}

function serialEvent() {
  inData = Number(serial.read());
}

function serialError(err) {
  print('Something went wrong with the serial port. ' + err);
}

function portClose() {
  print('The serial port closed.');
}