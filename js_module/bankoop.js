"use strict";

class Account {
  
  //Public field
  locale = "yoruba";

  //Private field
  #movements = [];
  #pin;


  constructor(owner, currency, pin) {
    this.owner = owner;
    this.currency = currency;
    this.#pin = pin;
    console.log(`Thanks for opening an account ${owner}`);
  }

  deposit (val) {
    this.#movements.push(val);
    return this;
  }

  getMovements () {
    return this.#movements;
  }
  withdraw(val) {
    this.deposit(-val);
    return this;
  }

  requestLoan(val) {
    if (this.#approveload(val)) {
      this.deposit(val);
      console.log(`Loan approved`);
      return this;
    }
  }

  #approveload(val) {
    return true;
  }
}

const acc1 = new Account("Jonas", "EUR", 1111);
acc1.deposit(250);
acc1.withdraw(140);

console.log(acc1);
