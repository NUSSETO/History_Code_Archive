% Basically, LU_F is the most time-consuming, doesn't matter it's by row or by col (so there is only one)
% Normally, Gaussian would be better option with less restriction 
% But if it's a (upper) lower triangle matrix, by row or by col would much faster

clear 

s = RandStream('mt19937ar','Seed',10); 
RandStream.setGlobalStream (s);

n = (200:200:2000); % Once over 1000, it consumes lots of time IMO
mm = length(n);
Time1 = zeros(mm,1); % Store the cpu time for Gaussian vecotor method
Time2 = zeros(mm,1); % Store the cpu time for Gaussian matrix method
Time3 = zeros(mm,1); % Store the cpu time for lower triangle by row method
Time4 = zeros(mm,1); % Store the cpu time for lower triangle by col method
TimeLU = zeros(mm,1); % Store the cpu time for LU factorize method 
counter = 1;

for dim = n
    A = rand(dim) + 10*eye(dim); % Prevent LU_F from not working
    b = rand(dim,1);

    tic; % Gaussian_vec
    [x1,error1] = GaussianElimination_vec(A,b);
    Time1(counter,1) = toc;
    fprintf ('n = %5.0f \n', dim);
    fprintf ('residual_vector = %11.4e, error_1 = %1.0f, ', norm(A*x1 - b), error1);

    tic; % Gaussian_mtx
    [x2,error2] = GaussianElimination_mtx ( A , b );
    Time2(counter,1) = toc;
    fprintf ('residual_matrix = %11.4e, error_2 = %1.0f \n', norm(A*x2 - b), error2);

    tic; % LU_F
    [L,U] = LU_Fac(A);
    TimeLU(counter,1) = toc;
    fprintf ('residual_LU_Factorization = %11.4e, ', norm(L*U - A));

    tic; % LT_row
    x3 = Lower_row(L,b);
    Time3(counter,1) = toc;
    fprintf ('residual_row = %11.4e, ', norm(L*x3 - b));   

    tic; % LT_col
    x4 = Lower_col(L,b);
    Time4(counter,1) = toc;
    fprintf ('residual_col = %11.4e \n', norm(L*x4 - b));   

    counter = counter + 1;
end

figure(1)
plot(n,Time1,'b-o','LineWidth',2)
hold on
plot(n,Time2,'r-x','LineWidth',2)
plot(n,Time3,'g-*','LineWidth',2)
plot(n,Time4,'y-+','LineWidth',2)
plot(n,TimeLU,'k-square','LineWidth',3)
legend ('vector','matrix','row','column','LU Factorization','Location','northwest','FontSize',14)
xlabel ('matrix dimension n','FontSize',14)
ylabel ('CPU times (sec)','FontSize',14)
grid on
hold off

% Making a cubic function (via magic) to approach
B1 = [n'.^3, n'.^2, n', ones(mm,1)];
a1 = B1\[Time1,Time2];
Alg1 = B1*a1(:,1);
Alg2 = B1*a1(:,2);

figure(2)
plot(n,Time1,'b-o','LineWidth',2)
hold on
plot(n,Alg1,'r-x','LineWidth',2)
legend ('vector','poly3','Location','northwest','FontSize',14)
xlabel ('matrix dimension n','FontSize',14)
ylabel ('CPU times (sec)','FontSize',14)
grid on
hold off

figure(3)
plot(n,Time2,'b-o','LineWidth',2)
hold on
plot(n,Alg2,'r-x','LineWidth',2)
legend ('vector','poly3','Location','northwest','FontSize',14)
xlabel ('matrix dimension n','FontSize',14)
ylabel ('CPU times (sec)','FontSize',14)
grid on
hold off

% Making a quadratic function (via magic) to approach
B2 = [n'.^2 , n', ones(mm ,1)]; 
a2 = (B2' * B2) \ ( B2' * [Time3,Time4]);
Alg3 = B2 * a2(:,1);
Alg4 = B2 * a2(:,2);

figure (4)
plot(n,Time3,'b-o','LineWidth',2)
hold on
plot(n,Alg3,'r-x','LineWidth',2)
legend ('row','poly2','Location','northwest','FontSize', 14)
xlabel('matrix dimension n','FontSize',14)
ylabel('CPU times (sec)','FontSize',14)
grid on
hold off

figure (5)
plot (n,Time4,'b-o','LineWidth',2)
hold on
plot (n,Alg4,'r-x','LineWidth',2)
legend ('column','poly2','Location','northwest','FontSize', 14)
xlabel('matrix dimension n','FontSize',14)
ylabel('CPU times (sec)','FontSize',14)
grid on
hold off
