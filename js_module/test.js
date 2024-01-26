class CarCl {
  constructor (make, speed) {
    this.speed = speed;
    this.make = make;
  }

  accelerate () {
    this.speed += 10;
    console.log(this.speed);
  }

  brake () {
    this.speed -= 5;
    console.log(this.speed);
  }
}

class EVCl extends CarCl {
  #charge;

  constructor (make, speed, charge) {
    super(make, speed);
    this.#charge = charge;
  }

  chargeBattery (chargeTo) {
    this.#charge = chargeTo;
    return this;
  }

  accelerate () {
    this.speed += 20;
    this.#charge -= 1;
    console.log(`${this.make} going at ${this.speed} with a charge of ${this.#charge}`);
    return this;
  }
  brake () {
    this.speed -= 5;
    console.log(this.speed);
  };
}
const car1 = new EVCl("Rivian", 120, 23);
console.log(car1.accelerate());


const t = {
  print () {
    console.log("Usman Akinyemi");
  }
}
t.print()
