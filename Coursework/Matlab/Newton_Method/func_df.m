function y = func_df(x, b_1, l, h, D)

  [A, B, C, E] = compute_parameters(b_1, l, h, D);
  y = A*cos(x)*cos(x) - A*sin(x)*sin(x) + 2*B*sin(x)*cos(x) + C*sin(x) - E*cos(x);

end
