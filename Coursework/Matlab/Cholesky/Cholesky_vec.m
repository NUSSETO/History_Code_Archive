function G = Cholesky_vec(A)
    n = size(A,1);
    G = zeros(n);
    for k = 1:n
        if k == 1
            G(k,k) = sqrt(A(k,k));
        else
            G(k,k) = sqrt(A(k,k) - G(k,1:k-1)*G(k,1:k-1)');
        end
        for i = k+1:n
            G(i,k) = (A(i,k) - G(i,1:k-1)*G(k,1:k-1)')/G(k,k);
        end
    end
end
