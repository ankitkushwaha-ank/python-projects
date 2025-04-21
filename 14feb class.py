# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.linspace(0, 2*np.pi, 400)  # Generate x values from 0 to 2π
# plt.plot(x, np.sin(x), label='sin(x)')
# plt.plot(x, np.cos(x), label='cos(x)')
# plt.plot(x, np.sin(3*x), label='sin(3x)')
# plt.plot(x, np.cos(3*x), label='cos(3x)')
#
# plt.xlabel('x')
# plt.ylabel('Function value')
# plt.title('Trigonometric Functions')
# plt.legend()
# plt.grid(True)
#
# plt.show()
#
# plt.close
# all;
#
# format
# np.long
#
# a = 0;
# b = 1;
# n = 10;
#
# h = (b - a) / n;
# f = @(x) exp(-x.^2);
#
# i = 1:1:n-1
# S = f(a + i.*h);
#
# trueval = integral(f, a, b);
# int_trap = (h/2) * (f(a) + 2*sum(S) + f(b));
# err_trap = abs(trueval - int_trap);
#
# sprintf("%0.6f", int_trap)



a = 0;
b = 1;
n = 8;
h = (b - a) / n;
x = a:h:b;
y = f(x);
f = @(x) 1 / (1 + x);

% Trapezoidal rule formula
integral_approx = (h/2) * (y(1) + 2*sum(y(2:end-1)) + y(end));
integral_exact = log(2);
error = abs(integral_exact - integral_approx);

% Display the results
fprintf('Approximate integral (N = %d): %f\n', n, integral_approx);
fprintf('Exact integral: %f\n', integral_exact);
fprintf('Absolute error: %f\n', error);


n_values = [4, 8, 16, 32, 64, 128, 256];

fprintf('\nExploring different values of n:\n');
fprintf('----------------------------------------\n');
fprintf('   n      Approximate Integral        Error\n');
fprintf('----------------------------------------\n');

for n = n_values
    h = (b - a) / n;
    x = a:h:b;
    y = f(x);
    integral_approx = (h/2) * (y(1) + 2*sum(y(2:end-1)) + y(end));
    error = abs(integral_exact - integral_approx);
    fprintf('%5d      %20.10f    %10.10f\n', n, integral_approx, error);
end
fprintf('----------------------------------------\n');


