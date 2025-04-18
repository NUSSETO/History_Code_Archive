function[A, B, C, E] = compute_parameters(b_1, l, h, D)

  A = l*sin(b_1);
  B = l*cos(b_1);
  C = (h + 0.5*D)*sin(b_1) - 0.5*D*tan(b_1);
  E = (h + 0.5*D)*cos(b_1) - 0.5*D;

end
