m = [['a', 'b', 'c'], 
     ['d', 'e', 'f'], 
     ['g', 'h', 'i']]

m_m = [[m[abs(i)][abs(j)] 
      for j in range(-len(m)+1, len(m))] 
      for i in range(-len(m)+1, len(m))]

for i in range(0, len(m_m)):
    for i2 in range(0, len(m_m[i])):
        print(m_m[i][i2], end='')
    print()