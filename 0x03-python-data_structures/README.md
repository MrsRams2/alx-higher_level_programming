Name of tasks:0x19. C - Stacks, Queues - LIFO, FIFO

All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=c89.

A README.md file, at the root of the folder of the project is mandatory
Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl,
You are allowed to use the C standard library
The prototypes of all your functions should be included in your header file called monty.h

#NAME of TASKS:

0. Print a list of integers
Write a function that prints all integers of a list.

Prototype: def print_list_integer(my_list=[]):


1. Secure access to an element in a list
Write a function that retrieves an element from a list like in C.

Prototype: def element_at(my_list, idx):
If idx is negative, the function should return None
If idx is out of range (> of number of element in my_list), the function should return None


2. Replace element
Write a function that replaces an element of a list at a specific position (like in C).

Prototype: def replace_in_list(my_list, idx, element):
If idx is negative, the function should not modify anything, and returns the original list
If idx is out of range (> of number of element in my_list), the function should not modify anything, and returns the original list


3. Print a list of integers... in reverse!
Write a function that prints all integers of a list, in reverse order.

Prototype: def print_reversed_list_integer(my_list=[]):

4. Replace in a copy
Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).

Prototype: def new_in_list(my_list, idx, element):


5. Can you C me now?
Write a function that removes all characters c and C from a string.

Prototype: def no_c(my_string):


6. Lists of lists = Matrix
Write a function that prints a matrix of integers.

Prototype: def print_matrix_integer(matrix=[[]]):


7. Tuples addition
Write a function that adds 2 tuples.

Prototype: def add_tuple(tuple_a=(), tuple_b=()):
Returns a tuple with 2 integers:
The first element should be the addition of the first element of each argument
The second element should be the addition of the second element of each argument


8. More returns!
Write a function that returns a tuple with the length of a string and its first character.

Prototype: def multiple_returns(sentence):
If the sentence is empty, the first character should be equal to None
You are not allowed to import any module


9. Find the max
Write a function that finds the biggest integer of a list.

Prototype: def max_integer(my_list=[]):
If the list is empty, return None


10. Only by 2
Write a function that finds all multiples of 2 in a list.

Prototype: def divisible_by_2(my_list=[]):


11. Delete at
Write a function that deletes the item at a specific position in a list.

Prototype: def delete_at(my_list=[], idx=0):
If idx is negative or out of range, nothing change (returns the same list)


12. Switch
Complete the source code in order to switch value of a and b


13. Linked list palindrome
Write a function in C that checks if a singly linked list is a palindrome.

Prototype: int is_palindrome(listint_t **head);
Return: 0 if it is not a palindrome, 1 if it is a palindrome
An empty list is considered a palindrome


14. CPython #0: Python lists
CPython is the reference implementation of the Python programming language. Written in C, CPython is the default and most widely used implementation of the language.
Since we now know a bit of C, we can look at what is happening under the hood of Python. 
Let’s have fun with Python and C, and let’s look at what makes Python so easy to use.

