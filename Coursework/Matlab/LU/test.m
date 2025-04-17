clear
format short

s = RandStream('mt19937ar', 'seed', 10);
RandStream.setGlobalStream(s);

n = (2:5);

for dim = n

  A = rand(dim);
  [L, U] = LU_Fac(A);
  
  fprintf('n = %1.0f\nA = \n', dim);
  disp(A);
  
  fprintf('Lower Triangular Matrix of A = \n');
  disp(L);
  
  fprintf('Upper Triangular Matrix of A = \n');
  disp(U);

  fprintf('The Residual of LU factoriation = %11.4e \n \n', norm(A - L*U));

end
