function [sol, no_iter, rsdl, flag] = newton_method(func, func_d, x_0, tol)

  counter = 1;
  max_counter = 1000;
  sol = x_0 - func(x_0)/func_d(x_0);

  while counter <= max_counter && abs((sol - x_0)/sol) >= tol
    counter = counter + 1;
    x_0 = sol;
    sol = x_0 - func(x_0)/func_d(x_0);
  end

  no_iter = counter;
  rsdl = func(sol);
  
  if counter <= max_counter
    flag = 0;
  else
    flag = 1;
  end
  
end
