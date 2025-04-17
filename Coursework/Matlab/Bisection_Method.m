function m_p = Bisection_method(l_p, r_p, f, tol)  %input two end seperately, then any function, tolerance last
  l_v = f(l_p);
  r_v = f(r_p);
  m_p = (l_p + r_p)/2;
  m_v = f(m_p);
  count = 1;
  max_count = 100;
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
      
