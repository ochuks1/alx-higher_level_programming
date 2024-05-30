#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      // If w or h is not positive or not an integer, create an empty object
      return {};
    }
    this.width = w;
    this.height = h;
  }

  print() {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate() {
    // Exchange width and height
    [this.width, this.height] = [this.height, this.width];
  }

  double() {
    // Multiply width and height by 2
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
