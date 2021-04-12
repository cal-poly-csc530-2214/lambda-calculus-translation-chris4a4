# Assignment 2: Lambda Calculus Translation by Christopher Peterson

## What I did

I wrote my LC Translator in vanilla Python. It translates a LC expression into executable Python code. This allowed me to test my code easily using Python's built-in ``eval()`` function.

I completed the assignment as specified and added some tests.

## Results

My code successfully transforms LC expressions into Python code. The returned code often has many redundant parenthesis, but this is by design. Some sample runs are shown below:

```
------------------------------------------
Lambda Calculus to Python Translation, CSC530, Spring 2021
By Christopher Peterson

Evaluating 8 test cases...
Testing complete
------------------------------------------

Enter command (q to quit): (+ 6 -5)

(6 + -5)

------------------------------------------

Enter command (q to quit): (ifleq0 -1 1 2)

(1 if -1 <= 0 else 2)

------------------------------------------

Enter command (q to quit): ((/ q => (+ q 8)) 4)

(((lambda q: (q + 8)))(4))

------------------------------------------

Enter command (q to quit): ((((/ x => (/ y => (/ z => (* x (+ y z))))) 4) -3) 2)

(((((((lambda x: (lambda y: (lambda z: (x * (y + z))))))(4)))(-3)))(2))

------------------------------------------

Enter command (q to quit): (println (ifleq0 (+ 6 -5) 2 (* 1 8)))

(print((2 if (6 + -5) <= 0 else (1 * 8))))

------------------------------------------

Enter command (q to quit): (ifleq0 ((/ x => x) 4) ((/ q => (+ q 8)) 4) ((((/ x => (/ y => (/ z => (* x (+ y z))))) 4) -3) 2))

((((lambda q: (q + 8)))(4)) if (((lambda x: x))(4)) <= 0 else (((((((lambda x: (lambda y: (lambda z: (x * (y + z))))))(4)))(-3)))(2)))

------------------------------------------

Enter command (q to quit): q

Process finished with exit code 0
```

## Tokenization Using ``literal_eval``

I found a very painless and Pythonic way to tokenize input strings. This utilizes the fact that the LC expression can be made to look like nested Python lists with a few regex operations:

```
import ast

# Quick and dirty python tokenization
def tokenize(input_string):
    # Convert to lists
    new_str = re.sub(r' ', ', ', input_string)
    new_str = re.sub(r'\(', '[', new_str)
    new_str = re.sub(r'\)', ']', new_str)

    # Add quotes around items
    new_str = re.sub(r'([^\[\], ]+)', r'"\1"', new_str)

    # Remove quotes around numbers (this is optional, depending on implementation)
    new_str = re.sub(r'"([-0-9]+)"', r'\1', new_str)

    return ast.literal_eval(new_str)
```

## Further Work

More intelligent type/error checking was not part of this assignment, but could be added.

Redundant parenthesis could be removed.

## Questions

I was considering sharing my tokenization code on Piazza, as tokenization wasn't the main purpose of this assignment and it could have saved other students a lot of headache. However, I wasn't sure if this was appropriate, since getting tokenization + recursive parsing to work was the hardest part of this assignment.

Other than that, this assignment was fairly straightforward.
