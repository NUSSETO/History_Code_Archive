function y = func_f(x, b_1, l, h, D)

  [A, B, C, E] = compute_parameters(b_1, l, h, D);
  y = A*sin(x)*cos(x) + B*sin(x)*sin(x) - C*cos(x) - E*sin(x);

end
