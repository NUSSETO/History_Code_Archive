function x = Cholesky_LS_vec(A,b)
    n = size(A,1);
    G = Cholesky_vec(A);
    x = zeros(n,1);
    y = zeros(n,1);

    for i = 1:n-1
        y(i,1) = b(i,1)/G(i,i);
        b(1+i:n,1) = b(1+i:n,1) - y(i,1)*G(1+i:n,i);
    end
    y(n,1) = b(n,1)/G(n,n);

    x(n,1) = y(n,1)/G(n,n);
    for i = n-1:-1:1
        x(i,1) = (y(i,1) - G(i+1:n,i)'*x(i+1:n,1))/G(i,i);
    end
end
