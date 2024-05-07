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


primary → number

primary → '(' expression ')'

exit_command → EXIT

##Explanation


