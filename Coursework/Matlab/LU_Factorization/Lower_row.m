function x = Lower_row(L,b)

    n = size (L ,1);
    x = zeros (n ,1);

    x(1,1) = b(1,1) / L(1,1);
    for ii = 2:n
        x(ii,1) = ( b(ii,1) - L(ii,1:ii-1) * x(1:ii-1,1) ) / L(ii,ii);
    end

end
