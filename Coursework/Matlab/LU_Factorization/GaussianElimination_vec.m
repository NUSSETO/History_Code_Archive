function [x,error] = GaussianElimination_vec( A , b )

    n = size (A ,1);
    error = 0;
    x = zeros (n ,1);

    for jj = 1:n -1
        [ val , idx ] = max( abs (A( jj :n , jj )) );
        if ( val < eps ) % Prevent all cols are 0
            error = 1;
            return
        elseif idx ~= 1 % Change if differnt index
            tmp = A(jj ,:);
            A(jj ,:) = A (jj - 1 + idx,:);
            A(jj - 1 + idx,:) = tmp ;
            tmp = b(jj ,1);
            b(jj ,1) = b (jj - 1 + idx,1);
            b(jj - 1 + idx,1) = tmp ;
        end
        for ii = jj +1: n % Calculate the matrix
            A(ii , jj +1: n) = A(ii , jj +1: n) - A(ii , jj ) / A(jj , jj ) * A(jj , jj +1: n );
            b(ii ,1) = b (ii ,1) - A(ii , jj ) / A(jj , jj ) * b(jj ,1);
            A(ii , jj ) = 0;
        end
    end
    if error == 0 % Not all cols are 0
        for ii = n : -1:2 % Solve
            x(ii ,1) = b(ii ,1) / A(ii , ii );
            b (1: ii -1 ,1) = b (1: ii -1 ,1) - x( ii ,1) * A (1: ii -1 , ii );
        end
        x (1 ,1) = b (1 ,1) / A (1 ,1);
    end

end
