function [L_Tri,U_Tri] = LU_Fac_vec(A)

    n = size(A,1);
    L_Tri = eye(n);
    U_Tri = A;

    for i = 1:n-1
        for j = i+1:n
            L_Tri(j,i) = U_Tri(j,i)/U_Tri(i,i);
            U_Tri(j,i+1:n) = U_Tri(j,i+1:n) - L_Tri(j,i)*U_Tri(i,i+1:n);
            U_Tri(j,i) = 0;
        end
    end
end
