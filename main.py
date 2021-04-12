import re
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


# Recursively parse through the nested lists of tokens
def recursive_parse(tokens):
    new_tokens = []
    for token in tokens:
        if isinstance(token, list):
            new_tokens.append(recursive_parse(token))
        else:
            new_tokens.append(token)

    return construct_string(new_tokens)


# Using the rules defined by the LC, constructs a python code string from the tokens
# Uses a LOT of redundant parenthesis as I just went with something I knew would work
# Does pretty much zero error or type checking as specified by the instructor
def construct_string(tokens):
    if tokens[0] == '+':
        return f'({tokens[1]} + {tokens[2]})'
    if tokens[0] == '*':
        return f'({tokens[1]} * {tokens[2]})'
    if tokens[0] == 'println':
        return f'(print({tokens[1]}))'
    if tokens[0] == '/':
        return f'(lambda {tokens[1]}: {tokens[3]})'
    if tokens[0] == 'ifleq0':
        return f'({tokens[2]} if {tokens[1]} <= 0 else {tokens[3]})'
    if len(tokens) == 2:
        return f'(({tokens[0]})({tokens[1]}))'

    print(f'Phrase {tokens} not understood')
    exit(1)


# Tests the LC evaluation against some test cases I came up with
# Uses Python's built-in function eval() to run the code
# Doesn't test print
def test_cases():
    tests = {
        '(+ 6 -5)': 1,
        '(* 6 -5)': -30,
        '(ifleq0 -1 1 2)': 1,
        '(ifleq0 (+ 1 1) 1 2)': 2,
        '((/ x => x) 4)': 4,
        '((/ q => (+ q 8)) 4)': 12,
        '((((/ x => (/ y => (/ z => (* x (+ y z))))) 4) -3) 2)': -4,
        '(ifleq0 ((/ x => x) 4) ((/ q => (+ q 8)) 4) ((((/ x => (/ y => (/ z => (* x (+ y z))))) 4) -3) 2))': -4,
    }

    print(f'Evaluating {len(tests)} test cases...')

    for test, result in tests.items():
        my_result = eval(recursive_parse(tokenize(test)))
        if not my_result == result:
            print(f'Test failed: {test} evaluated to {my_result} instead of {result}')

    print('Testing complete')


# Runs the tests and takes user input
def main():
    print('------------------------------------------')
    print('Lambda Calculus to Python Translation, CSC530, Spring 2021')
    print('By Christopher Peterson\n')

    test_cases()

    while True:
        print('------------------------------------------\n')

        # Take input
        command = input('Enter command (q to quit): ')
        if command == 'q':
            return

        # Parse and run the command, if possible
        print('')
        print(recursive_parse(tokenize(command)))
        print('')


if __name__ == "__main__":
    main()
