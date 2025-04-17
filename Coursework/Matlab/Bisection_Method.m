function m_p = Bisection_method(l_p, r_p, f, tol)  % input two end seperately, then any function, tolerance last

  l_v = f(l_p); % the value of the function at one end
  r_v = f(r_p); % the value of the function at the other end
  m_p = (l_p + r_p)/2; % middle point
  m_v = f(m_p); % the value of the function at middle point
  count = 1; % how many time the function has executed
  max_count = 100; % otherwise it might still runnung
  
  while count <= max_count && abs(m_v - 0) >= tol
    count = count + 1;
    
    if sign(l_v) == sign(r_v)
      return
    else
    
      if sign(l_v) == sign(m_v)
        l_p = m_p;
        l_v = m_v;
      else
        r_p = m_p;
        r_v = m_v;
      end
      
    m_p = (l_p + r_p)/2;
    m_v = f(m_p);
    end
  end
end
      
