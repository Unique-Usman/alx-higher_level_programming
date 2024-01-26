const nums = [1, 2, 3, 4];
const numberIterator = nums[Symbol.iterator]();
console.log(numberIterator)
console.log(numberIterator.next());
console.log(numberIterator.next());
console.log(numberIterator.next());
for (const n of nums) {
  console.log(n);
}
