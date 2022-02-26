## What is the Big O of the below function? (Hint, you may want to go line by line)

```javascript
function funChallenge(input) {
  let a = 10;
  a = 50 + 3;

  for (let i = 0; i < input.length; i++) {
    anotherFunction();
    let stranger = true;
    a++;
  }
  return a;
}
```

## Answer

```javascript
function funChallenge(input) {
  let a = 10; // O(1)
  a = 50 + 3; // O(1)

  for (let i = 0; i < input.length; i++) {
    anotherFunction(); // O(n)
    let stranger = true; // O(1)
    a++; // O(1)
  }
  return a;
}
```

> Big O of function: **O(n)**