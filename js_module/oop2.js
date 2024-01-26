'use strict';
// const PersonCl = class {}

class PersonCl {
  constructor (fullName, birthYear) {
    this.fullName = fullName;
    this.birthYear = birthYear;
  }

  // methods will be added to prototype property
  calcAge () {
    console.log(2037 - this.birthYear);
  }

  get age () {
    return 2037 - this.birthYear;
  }

  set fullName (name) {
    if (name.includes(' ')) { this._fullName = name; } else { console.log('Nmae is not a full name'); }
  }

  get fullName () {
    return this._fullName;
  }

  static hey () {
    console.log('Hey there');
  }
}

class StudentCl extends PersonCl {
  constructor (fullName, birthYear, course) {
    super(fullName, birthYear);
    this.course = course;
  }

  introduce() {
    console.log(`My Name is ${this.fullName} and I study ${this.course}`);
  }

  calcAge() {
    console.log(`I'm ${2037 - this.birthYear} year old, but as a
    student I feel more like ${2037 - this.birthYear + 10}`);
  }
}

console.log(`----${StudentCl.prototype.constructor}----`);
const martha = new StudentCl('Marthia Jones', 2012, "Computer Science");
console.log(martha._fullName);
martha.introduce()

const jessica = new PersonCl('Jessica', 1916);
console.log(jessica.age);
console.log(jessica.__proto__ === PersonCl.prototype);

const walter = new PersonCl('Walter', 1965);
PersonCl.prototype.greet = function () {
  console.log(`Hey ${this.firstName}`);
};

const account = {
  owner: 'jonas',
  movements: [200, 530, 120, 300],

  get latest () {
    return this.movements.slice(-1).pop();
  },

  set latest (mov) {
    this.movements.push(mov);
  }
};

console.log(account.latest);
account.latest = 50;

console.log(account.movements);

PersonCl.hey();
