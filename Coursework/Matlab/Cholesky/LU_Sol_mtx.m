function x = LU_Sol_mtx(A,b)

    n = size(A ,1);
    x = zeros(n ,1);
    y = zeros(n ,1);

    [L,U] = LU_Fac_mtx(A);

    for ii = 1:n-1
        y(ii ,1) = b(ii ,1) / L( ii , ii );
        b(ii+1:n,1) = b(ii+1:n,1) - y(ii ,1) * L(ii+1:n,ii );
    end
    y(n ,1) = b(n,1) / L(n,n);

    for ii = n:-1:2
        x(ii ,1) = y(ii ,1) / U( ii , ii );
        y(1:ii-1,1) = y(1:ii-1,1) - x(ii,1) * U(1:ii-1,ii);
    end
    x(1,1) = y(1,1)/U(1,1);

end
