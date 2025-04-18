function x = Lower_col(L,b)

    n = size(L ,1);
    x = zeros(n ,1);

    for ii = 1:n-1
        x(ii ,1) = b(ii ,1) / L( ii , ii );
        b(ii+1:n,1) = b(ii+1:n,1) - x(ii ,1) * L(ii+1:n,ii );
    end
    x(n ,1) = b(n,1) / L(n,n);

end
