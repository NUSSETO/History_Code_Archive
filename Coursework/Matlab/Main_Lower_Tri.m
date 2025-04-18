clear
format long e

s = RandStream ('mt19937ar','Seed',10); 
RandStream.setGlobalStream(s);

n_vec = (1000:500:10000); % Setting the dimensions
mm = length(n_vec);
Time1 = zeros(mm ,1); % Record the cpu time for each different number of dimension
Time2 = zeros(mm ,1); % Since we have two ways to calculate.
counter = 1; 

for dim = n_vec
    mtx_U = rand(dim); % Create matrix
    mtx_U = 10* eye(dim) + diag(6*rand(dim ,1)) + triu(mtx_U ,1); % Making it an upper triangle, use 'eye' and 'diag' to make sure the diagnol has value.
    mtx_L = mtx_U'; % transit
    rhs = randn(dim,1); % Create constants
    x1 = zeros(dim,1); % Store soluition for first method

    tic ; % Solve by row
    x1(1,1) = rhs(1,1) / mtx_L(1,1);
    for ii = 2:dim
        x1(ii,1) = ( rhs(ii,1) - mtx_L(ii,1:ii-1) * x1(1:ii-1,1) ) / mtx_L(ii,ii);
    end
    Time1 (counter ,1) = toc ;
    fprintf ('n = %5.0f, residual_row = %11.4e, ', dim , norm( mtx_L * x1 - rhs ));

    rhs_tmp = rhs ; % Since solving by col will change the constant, so we copy one just in case
    x2 = zeros ( dim ,1); % Store solution for second method
    tic ;
    for ii = 1:dim-1
        x2 (ii ,1) = rhs_tmp (ii ,1) / mtx_L ( ii , ii );
        rhs_tmp (ii+1:dim,1) = rhs_tmp (ii+1:dim,1) - x2 ( ii ,1) * mtx_L (ii+1:dim,ii );
    end
    x2 (dim ,1) = rhs_tmp (dim ,1) / mtx_L (dim ,dim);
    Time2 (counter ,1) = toc ;
    fprintf ('residual_col = %11.4e \n', norm ( mtx_L * x2 - rhs ));

    counter = counter + 1;
end

figure (1)
plot(n_vec,Time1,'b-o','LineWidth',2)
hold on
plot(n_vec,Time2,'r-x','LineWidth',2)
legend('row','column','Location','northwest','FontSize',14)
xlabel('matrix dimension n','FontSize',14)
ylabel('CPU times (sec)','FontSize',14)
grid on
hold off

% Making a quadratic function (via magic) to approach the cpu time
mtx_B = [n_vec' .^2 , n_vec' , ones(mm ,1)]; 
coef_a = (mtx_B' * mtx_B) \ ( mtx_B' * [Time1,Time2]);
p2_Alg1 = mtx_B * coef_a(:,1);
p2_Alg2 = mtx_B * coef_a(:,2);

figure (2)
plot(n_vec,Time1,'b-o','LineWidth',2)
hold on
plot(n_vec,p2_Alg1,'r-x','LineWidth',2)
legend ('row','poly2','Location','northwest','FontSize', 14)
xlabel('matrix dimension n','FontSize',14)
ylabel('CPU times (sec)','FontSize',14)
grid on
hold off

txtAlg1 = ['$ P(x) = (', num2str(coef_a(1 ,1)) ,') x^2 + (', num2str(coef_a(2 ,1)) ,') x + (', num2str(coef_a(3 ,1)) ,') $']; % $ make symbol look 'math'
title(txtAlg1,'Interpreter','latex') % Making title

figure (3)
plot (n_vec,Time2,'b-o','LineWidth',2)
hold on
plot (n_vec,p2_Alg2,'r-x','LineWidth',2)
legend ('column','poly2','Location','northwest','FontSize', 14)
xlabel('matrix dimension n','FontSize',14)
ylabel('CPU times (sec)','FontSize',14)
grid on
hold off

txtAlg2 = ['$ P(x) = (', num2str(coef_a(1 ,2)) ,') x^2 + (', num2str(coef_a(2 ,2)) ,') x + (', num2str(coef_a(3 ,2)) ,') $'];
title(txtAlg2,'Interpreter','latex')
