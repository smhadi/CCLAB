# Compiler Construction Lab Project
This is our lab project where we are going to be using Python to iomplement a parser and also add a GUI for a calculator programming language

## CFG
line → expression exit_command

line → UserIn VAR '=' expression exit_command

line → exit_command

line → line exit_command

line → line expression exit_command

line → Print expression exit_command


expression → term '+' expression

expression → term '-' expression

expression → term

expression → VAR

expression → term UserIn


factor → primary '^' factor

factor → primary UserIn

factor → primary

factor → VAR


term → factor

term → factor '*' term

term → factor '/' term

term → factor UserIn

term → VAR


primary → number

primary → '(' expression ')'


exit_command → EXIT

##Explanation

Line:

- An expression followed by an exit command
- An input variable followed by an exit command
- An exit command
- An exit command
- A line followed by an expression and an exit command
- Print statements takes an expression and displays the result

Expression:

- A term followed by a + and another expression
- A term followed by a - and another expression
- A term
- A variable
- A term followed by a user input

Factor:

- A primary expression that is raised to the power of another factor
- A primary expression followed by a user input
- A primary expression
- A variable

Term:

- A factor
- A factor multiplied by another term
- A factor divided by another term
- A factor followed by user input
- A variable


Primary:

- A number
- An expression enclosed in parentheses

Exit Command:

- The exit command "EXIT"

