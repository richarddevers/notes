# Python: Generators, Coroutines, Native Coroutines and async/await

source: https://masnun.com/2015/11/13/python-generators-coroutines-native-coroutines-and-async-await.html

# Generators

- function thats **generates** values vs a function that **return** a value
- a classiq function is start from scratch at each call. It's one time execution
- a generator function **yield** a value and pause the execution of the function and the control is **returned** to the calling scope.
- a generator function doesn't return directly value , but instead a **generator object** which is an iterable (so we can call next())