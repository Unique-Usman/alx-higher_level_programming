'use strict';

const PersonProto = {
  calcAge () {
    console.log(2037 - this.birthYear);
  },

  init (firstName, birthYear) {
    this.firstName = firstName;
    this.birthYear = birthYear;
  }
};

const steven = Object.create(PersonProto);
console.log(steven.__proto__ === PersonProto);

steven.name = 'Steven';
steven.birthYear = 2002;

steven.calcAge();
const sarah = Object.create(PersonProto);
sarah.init('Sarah', 1979);
sarah.calcAge();

const StudentProto = Object.create(PersonProto);
StudentProto.init = function (firstName, birthYear, course) {
  PersonProto.init.call(this, firstName, birthYear);
  this.course = course;
}

StudentProto.introduce = function () {
  console.log(`My name is ${this.firstName}\
and I study ${this.course}`);
}

const jay = Object.create(StudentProto);
jay.init("Jay", 2010, "Computer Science");
jay.calcAge()
jay.introduce()
