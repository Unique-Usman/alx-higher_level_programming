'use strict';

const Person = function (firstName, birthYear) {
  this.firstName = firstName;
  this.birthYear = birthYear;
};

Person.prototype.calcage = function () {
  console.log(2037 - this.birthYear);
};

Person.hey = function () {
  console.log('Hey there');
};
const jonas = new Person('Jonas', 1991);
console.log(jonas);

const matilda = new Person('Matilda', 2017);
const jack = new Person('Jack', 1975);
console.log(matilda);

console.log(jonas instanceof Person);
jonas.calcage();
matilda.calcage();

console.log(matilda.__proto__);
console.log(jonas.__proto__);

console.log(matilda.__proto__ === Person.prototype);

console.log(Person.prototype.isPrototypeOf(jonas));
Person.prototype.species = 'Homo Sapiens';
console.log(jonas.species, matilda.species);
console.log(jonas.hasOwnProperty('species'));
console.log(jonas.hasOwnProperty('calcage'));
console.log(Person.__proto__.__proto__.__proto__);

console.log(typeof Person.prototype.constructor.__proto__);

const arr = [1, 2, 3, 4, 4, 3];
console.log(arr.__proto__.__proto__);

Array.prototype.unique = function () {
  return [...new Set(this)];
};

console.log(arr.unique());

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



const car1 = new Car('BMW', 120);
const car2 = new Car('Merceded', 95);
car1.accelerate();
car2.brake();

Person.hey();


