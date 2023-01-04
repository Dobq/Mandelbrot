[Please turn on line wrapping.]

Welcome to Mandelbrot set drawer.

Using one of this python codes You are able to draw various images of Mandelbrot set zooms.

----INSTRUCTIONS----

On the beginning You have to set constants:

maxlim - maximal number of iterations calculated for single pixel.

focus=complex(,) - complex number, determines center of image.

dist - distance between complex numbers to "be drawn" on output image.

res - output image is square of pixels, length of it's side is 2^res+1.

cl - length of color pattern is equal to 2*cl, You probably want it bo be bigger in some deeper zooms.

Remark that if - for example - You want to draw the same image, but in 2^n times higher resolution, You have to both decrease dist 2^n times and increase res n times.

At the end of the work, time needed to run whole (and parts of) code is printed.

After running the same .py file again, image generated earlier - if not renamed or moved to other folder - is overwritten by new one.

----ALGORITHMS----

Mandel_simple.py - uses simplest, naive algorithm, "MACHINERY" part of code consists of single function, all calculations are done in line 67th that defines image, whole code is very brief; as expected, it's least effective algorithm (see efficiency.txt).

----

Mandel_opt_loops.py - rough description: calculates values on the sides of whole square, then starts doing following things:

1. check if center of given square is calculated yet (-1 means it's not calculated yet), if so, divide square into four squares (i.e. calculate values on the cross (calc_cros function)), it's job of squa_divi;
2. for each of squares, check if it's center (and so whole square) is calculated yet, if not, then check if values in corners are equal, if yes, then check if values on the sides are equal, if so, fill square with this value (squa_inse), it's job of squa_chec;
3. go to first step, but consider two times smaller squares.

This goes until smallest unfilled squares are 3 by 3 (or 4 by 4, depending on how we understand it) beacuse going this way further is ineffective; rest of the job is done by naive algorithm.

----

Mandel_opt_func.py - the same algorithm as in Mandel_opt_loops.py case, but python's inbuilt map and filter functions are applied possibly widely.

----COMMENTS----

In examples folder You can see examples and description.txt that describes each of them.

See efficiency.txt for very short efficiency analysis of each algorithm.



