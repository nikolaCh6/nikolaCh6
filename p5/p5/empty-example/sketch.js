function setup() {
  // put setup code here
  createCanvas(6040, 4080);
}

function draw() {
  // put drawing code here
  strokeWeight(4);
  stroke ("pink");
  fill(51);
  ellipse(100, 50, 80, 80);

  strokeWeight(2);
  stroke ("yellow");
  fill(57);
  ellipse(60, 50, 80, 80);

  strokeWeight(2);
  stroke ("red");
  fill(57);
  rect(30, 20, 55, 55);


  noFill();
  noStroke();
  if (mouseIsPressed){
    if(mouseButton === LEFT) {
    r =random(255);
    g =random(255);
    b =random(255);
    strokeWeight(26);
    fill("pink");
    stroke(r, g, b);
  }
  if(mouseButton === CENTER) {
    strokeWeight(20);
    fill(255, 255, 255);
    stroke ("255, 255, 255");
    rect(mouseX-10, mouseY-10, 20, 20);
  }
      } else {
  noFill ();
  noStroke();
}
point (mouseX, mouseY);
}
