function [sol, number_of_iteration] = fixed_point(f_p, func, tol)

  counter = 1;
  max_iteration = 200;
  sol = func(f_p);

  while (counter <= max_iteration) && abs(sol - f_p) >= tol
    counter = counter + 1;
    f_p = sol;
    sol = func(f_p);
  end

  number_of_iteration = counter - 1

end
