function setup() {
  createCanvas(10000, 10000);
}

function draw() {

    // fill(0,255,0);
    // strokeWeight(4);
    // stroke(255,0,0);
    //   ellipse(90, 90, 100, 80);
    //   ellipse(90, 175, 100, 80);
    //
    // fill(255,0,0);
    // strokeWeight(4);
    // stroke(0,255,0);
    //   rect(30, 100, 505, 55, 100);
    //
    // fill(0,0,255);
    // strokeWeight(4);
    // stroke(0,0,0);
    //   triangle(200, 75, 58, 20, 86, 75);
    //   triangle(30, 75, 58, 20, 86, 75);

  //     noFill();
  //     noStroke();
  //     if(mouseIsPressed){
  //       if (mouseButton === LEFT) {
  //         r = random(255);
  //         g = random(255);
  //         b = random(255);
  //         strokeWeight(20);
  //         fill(r, g, b, 127);
  //         stroke(r, g, b);
  //       } if (mouseButton === CENTER){
  //         strokeWeight(30);
  //         fill(255, 255, 255);
  //         stroke(255, 255, 255);
  //         rect(mouseX-10,mouseY-10,20,20);
  //       }
  //     } else {
  //       noFill();
  //       noStroke();
  //     }
  //     point(mouseX, mouseY);

  fill(0,255,0);
  strokeWeight(4);
  stroke(255,0,0);
  line(100, 100, 250, 100);
  line(100, 150, 250, 150);
  line(150, 50, 150, 200);
  line(200,50,200,200);


  noFill();
  noStroke();
  if(mouseIsPressed){
    if (mouseButton === LEFT) {
      fill(255,0,0);
      strokeWeight(4);
      stroke(0,0,0);
      ellipse(mouseX-10,mouseY-10,20,20);
    } if (mouseButton === CENTER){
      fill(255,0,0);
      strokeWeight(4);
      stroke(0,0,0);
      rect(mouseX-10,mouseY-10,20,20);
    } if (mouseButton === RIGHT){
      strokeWeight(30);
      fill(255, 255, 255);
      stroke(255, 255, 255);
      rect(mouseX-10,mouseY-10,20,20);
  }
  } else {
    noFill();
    noStroke();
  }
   }
