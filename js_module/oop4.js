"use strict";

const Person = function (firstName, birthYear) {
  this.firstName = firstName;
  this.birthYear = birthYear;
}

Person.prototype.calcAge = function () {
  console.log(2037 - this.birthYear);
}

const Student = function (firstName, birthYear, course) {
  Person.call(this, firstName, birthYear);
  this.course = course;
}
 
Student.prototype = Object.create(Person.prototype);

Student.prototype.introduce = function () {
  console.log(`My name is ${this.firstName} and I study ${this.course}`)
}

const mike = new Student("Mike", 2020, "Computer Science");
console.log(mike.introduce());
mike.calcAge();

console.log(mike.__proto__);
console.log(mike.__proto__.__proto__)

Student.prototype.constructor = Student;
console.dir(Student.prototype.constructor);

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
    console.log(`Tesla going at ${this.speed} with a charge of ${this.charge}`);
    return this;
  }
  brake () {
    this.speed -= 5;
    console.log(this.speed);
  };
}
const car1 = new EVCl("Rivian", 120, 23);
console.log(`
===========================
${car1.accelerate()}
==========================
`)

const Car = function (make, speed) {
  this.make = make;
  this.speed = speed;
};
Car.prototype.accelerate = function () {
  this.speed += 10;
  console.log(this.speed);
};
Car.prototype.brake = function () {
  this.speed -= 5;
  console.log(this.speed);
};

const EV = function (make, speed, charge) {
  Car.call(this, make, speed);
  this.charge = charge;
}

EV.prototype = Object.create(Car.prototype);
EV.prototype.constructor = EV; 

EV.prototype.chargeBattery = function (chargeTo) {
  this.charge = chargeTo;
}

EV.prototype.accelerate = function () {
  this.speed += 20;
  this.charge -= 1;

  console.log(`Tesla going at ${this.speed} with a charge of ${this.charge}`);
}

const car = new EV("Tesla", 100, 24);
car.accelerate()
