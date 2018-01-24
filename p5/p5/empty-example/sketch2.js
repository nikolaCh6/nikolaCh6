function setup() {
  // put setup code here
  createCanvas(6040, 4080);
}

function draw() {
  // put drawing code here
    r =random(255);
    g =random(255);
    b =random(255);
    strokeWeight(6);
    fill();
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
