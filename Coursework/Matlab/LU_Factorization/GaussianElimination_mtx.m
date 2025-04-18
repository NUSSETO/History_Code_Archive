function [x,error] = GaussianElimination_mtx( A , b )

    n = size (A ,1);
    error = 0;
    x = zeros (n ,1);

    for jj = 1:n -1
        [ val , idx ] = max( abs (A( jj :n , jj )) );
        if ( val < eps )
            error = 1;
            return
        elseif idx ~= 1
            tmp = A(jj ,:);
            A(jj ,:) = A (jj -1+ idx (1) ,:);
            A(jj -1+ idx (1) ,:) = tmp ;
            tmp = b(jj ,1);
            b(jj ,1) = b (jj -1+ idx (1) ,1);
            b(jj -1+ idx (1) ,1) = tmp ;
        end
        scale_vec = A( jj +1: n , jj ) / A(jj , jj );
        A( jj +1: n , jj +1: n) = A( jj +1: n , jj +1: n) - scale_vec * A(jj , jj +1: n );
        A( jj +1: n , jj ) = 0;
        b( jj +1: n ,1) = b( jj +1: n ,1) - b( jj ,1) * scale_vec ;
    end
    if error == 0 
        for ii = n : -1:2
            x(ii ,1) = b(ii ,1) / A(ii , ii );
            b (1: ii -1 ,1) = b (1: ii -1 ,1) - x( ii ,1) * A (1: ii -1 , ii );
        end
        x (1 ,1) = b (1 ,1) / A (1 ,1);
    end

end
