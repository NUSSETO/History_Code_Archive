function [L_Tri,U_Tri] = LU_Fac(A) % This doesn't prevent incorrect input

    n = size(A,1);
    L_Tri = zeros(n);
    U_Tri = A;

    for i = 1:n-1
        L_Tri(i+1:n,i) = U_Tri(i+1:n,i)/U_Tri(i,i);
        M = eye(n);
        M(i+1:n,i) = (-1)*U_Tri(i+1:n,i)/U_Tri(i,i);
        U_Tri = M*U_Tri;
    end
    L_Tri = L_Tri + eye(n);

end
