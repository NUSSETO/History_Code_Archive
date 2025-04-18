function G = Cholesky_mtx(A)
    n = size(A,1);
    G = zeros(n);
    for k = 1:n
        if k == 1
            G(k,k) = sqrt(A(k,k));
        else
            G(k,k) = sqrt(A(k,k) - G(k,1:k-1)*G(k,1:k-1)');
        end
        G(k+1:n,k) = (A(k+1:n,k) - G(k+1:n,1:k-1)*G(k,1:k-1)')/G(k,k);
    end
end
