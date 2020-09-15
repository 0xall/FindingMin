# FindingMin

FindingMin is a program implemented by python, it helps to find local
minimum or local maximum for polynomial function using Newton Method.

# Usage

For printing help messages, use `-h` option.

```
python find_min.py -h
```

### Using 1st, 2nd Derivative
```
python find_min.py 5 -22.4 15.85272 24.161472 -23.4824832 -f 50 -s 6 -v
```

Above command means it uses
the polynomial with 5x^4 - 22.4x^3 + 15.85272 x^2 + 24.161472 -23.4824832, 
starts point with 6, uses the 50 floatings points,
and visualize the graph per every iteration.

### Approximation

```
python find_min.py 5 -22.4 15.85272 24.161472 -23.4824832 -s 10 -f 50 -n 16 --approximation 0.01
```

For using approximation method, use `--approximation` option. 
Above command means it uses
the polynomial with 5x^4 - 22.4x^3 + 15.85272 x^2 + 24.161472 -23.4824832, 
uses approximation method with h = 0.01, uses the 50 
floatings points, starts point with 10, and iterates with maximum 16.
