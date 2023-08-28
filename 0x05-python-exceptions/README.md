# Python Exception Handling

Exceptions in Python are a way to manage errors and unexpected situations during program execution.

## Key Points

- Use `try`, `except`, and `finally` blocks for exception handling.
- Catch specific exceptions to handle different error types.
- Uncaught exceptions propagate up the call stack or terminate the program.

## Common Exceptions

- `ZeroDivisionError`: Division or modulo by zero.
- `TypeError`: Inappropriate object type.
- `ValueError`: Inappropriate object value.
- `NameError`: Name not found.
- `IndexError`: Sequence index out of range.
- `KeyError`: Dictionary key not found.
- `FileNotFoundError`: File open failure.
- `IOError`: I/O operation failure.

## Exception Handling

- Catch multiple exceptions with parentheses.
- Use `else` for code that runs when no exceptions occur.
- Create custom exceptions by subclassing `Exception`.

## Best Practices

- Handle specific exceptions for effective error management.
- Plan for graceful program behavior when exceptions occur.
- Log exceptions for debugging and code reliability.
