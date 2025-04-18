clear
format long e

s = RandStream('mt19937ar','seed',10);
RandStream.setGlobalStream(s);

n = (200:200:2000);
mm = length(n);
time_vec = zeros(mm,1);
time_mtx = zeros(mm,1);
time_LU_vec = zeros(mm,1);
time_LU_mtx = zeros(mm,1);
counter = 1;

for dim = n

    A = rand(dim);
    A = (A + A')/2; % Make it symmetrical
    row_sum = sum(abs(A),2);
    A = A + diag(row_sum) + 10*eye(dim); % Make the diagonal really big
    b = randn(dim,1);

    tic 
    x_vec = Cholesky_LS_vec(A,b);
    time_vec(counter,1) = toc;
    fprintf('n = %5.0f, residual_Cholesky_vector = %11.4e',dim,norm(A*x_vec - b));

    tic 
    x_mtx = Cholesky_LS_mtx(A,b);
    time_mtx(counter,1) = toc;
    fprintf(', residual_Cholesky_matrix = %11.4e',norm(A*x_mtx - b));

    tic
    x_LU_vec = LU_Sol_vec(A,b);
    time_LU_vec(counter,1) = toc;
    fprintf(', residual_LU_vector = %11.4e',norm(A*x_LU_vec - b));

    tic; 
    x_LU_mtx = LU_Sol_mtx(A,b);
    time_LU_mtx(counter,1) = toc; 
    fprintf(', residual_LU_matrix = %11.4e \n',norm(A*x_LU_mtx - b));

    counter = counter + 1;

end

figure(1)
plot(n,time_vec,'b-o','LineWidth',2)
hold on
plot(n,time_mtx,'r-x','LineWidth',2)
plot(n,time_LU_vec ,'k-^','LineWidth',2)
plot(n,time_LU_mtx ,'g-*','LineWidth',2)
legend('Cholesky - vector','Cholesky - matrix','LU - vector','LU - matrix','Location','northwest','FontSize',14)
xlabel('matrix dimension n','FontSize',14)
ylabel('CPU times (sec)','FontSize',14)
grid on
hold off
