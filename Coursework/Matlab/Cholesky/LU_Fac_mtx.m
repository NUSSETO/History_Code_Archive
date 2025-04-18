function [L_Tri,U_Tri] = LU_Fac_mtx(A)

    n = size(A,1);
    L_Tri = eye(n);
    U_Tri = A;

    for i = 1:n-1
        L_Tri(i+1:n,i) = U_Tri(i+1:n,i)/U_Tri(i,i);
        U_Tri(i+1:n,i+1:n) = U_Tri(i+1:n,i+1:n) - L_Tri(i+1:n,i)*U_Tri(i,i+1:n);
        U_Tri(i+1:n,i) = 0;
    end
end
