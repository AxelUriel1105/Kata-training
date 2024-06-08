"""Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds."""

def past(h, m, s):
    h_to_milsec = h * ((1000*60)*60)
    m_to_milsec = m * (1000*60)
    s_to_milsec = s * 1000
    m_to_milsec = m * (1000*60)
    s_to_milsec = s * 1000
    return h_to_milsec + m_to_milsec + s_to_milsec
    
    