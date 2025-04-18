clear

x_0 = 0.4;
tol = eps;
ang = (11.5*pi)/180;

[sol1, iter1, rsdl1, flag1] = newton_method(@(sol)func_f(sol, ang, 89, 49, 55), @(sol)func_df(sol, ang, 89, 49, 55), x_0, tol);
[sol2, iter2, rsdl2, flag2] = newton_method(@(sol)func_f(sol, ang, 89, 49, 30), @(sol)func_df(sol, ang, 89, 49, 30), x_0, tol);

fprintf('When l = 89 in, h = 49 in, D = 55 in, beta = 11.5 degree \n');
fprintf('alpha = %22.16e degree, iteration number = %2.0f \n', (sol1*180)/pi, iter1);
fprintf('When l = 89 in, h = 49 in, D = 30 in, beta = 11.5 degree \n');
fprintf('alpha = %22.16e degree, iteration number = %2.0f \n', (sol2*180)/pi, iter2);
