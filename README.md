# Complex Numbers Library in Python

In this project, operations with complex numbers are implemented **without using Python’s built-in `complex` type**.  
Complex numbers are modeled as tuples `(real, imaginary)` and, in polar coordinates, as `(magnitude, angle)`.

## Features
The library can perform the following operations:
- Addition
- Subtraction
- Multiplication
- Division
- Magnitude
- Conjugate
- Conversion between Cartesian ↔ Polar form
- Obtain the phase of a complex number

## Basic Operations with Complex Numbers
Additions, multiplications, and divisions of complex numbers are performed, as well as the calculation of their conjugate and magnitude. Results are verified both manually and using Python.

## Visualization on the Complex Plane
A function is implemented to plot complex numbers and their conjugates. It is then extended to graphically display the addition and multiplication of two complex numbers on the complex plane.

## Mandelbrot Set
The Mandelbrot set code is modified to apply zoom to different centers and vary the maximum number of iterations (`max_iter`), observing how the level of detail and the computation time of the fractal change.

## Julia Set
A Julia set generator is implemented using iterations of the form:

