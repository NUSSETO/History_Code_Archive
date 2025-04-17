clear

f_p = input('Give an initial point \n');
tol = input('Give a tolerance \n'); % Please must enter value
mm = 10000; % How many time we gonna re-run this function

for i = 1:mm % Warm up
  [sol1, no_iter1] = fixed_point(f_p, @fun_g1, tol);
end

tic;
for i = 1:mm
  [sol1, no_iter1] = fixed_point(f_p, @fun_g1, tol);
end
cpu_time1 = toc/mm;

tic;
for i = 1:mm
  [sol2, no_iter2] = fixed_point(f_p, @fun_g2, tol);
end
cpu_time2 = toc/mm;

fprintf('The fixed point of function 1 is %22.16e with %2.0f iterations and cpu time of %10.4e second \n', sol1, no_iter1, cpu_time1)
fprintf('The fixed point of function 2 is %22.16e with %2.0f iterations and cpu time of %10.4e second \n', sol2, no_iter2, cpu_time2)
