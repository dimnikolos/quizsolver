def quizsolver1():
  for a in range(0,10):
    for b in range(0,10):
      for c in range(0,10):
        for d in range(0,10):
          for e in range(0,10):
            for f in range(1,10):
              for g in range(0,10):
                if ((10*a+b)*(10*b+c)==(d*100+a*10+d)):
                  if ((10*e+c)/f == f):
                    if ((100*b+10*c+d)*g==1000*b+100*b+10*e+a):
                      if ((10*a+b)*(10*e+c)==(100*b+10*c+d)):
                        if ((10*b+c)/f == g):
                          if ((100*d+10*a+d) * f == (1000*b+100*b+10*e+a)):
                            print(''.join([str(a),str(b),str(c),
                              str(d),str(e),str(f),str(g)]))

def quizsolver2():
  posf = [1,2,3,4,5,6,7,8,9]
  pose = [0,0,0,1,2,3,4,6,8]
  posc = [1,4,9,6,5,6,9,4,1]
  for (i,f) in enumerate(posf):
    e = pose[i]
    c = posc[i]
    for a in range(0,10):
      for b in range(0,10):
        for d in range(0,10):
          for g in range(0,10):
            if ((10*a+b)*(10*b+c)==(d*100+a*10+d)):
              if ((10*e+c)/f == f):
                if ((100*b+10*c+d)*g==1000*b+100*b+10*e+a):
                  if ((10*a+b)*(10*e+c)==(100*b+10*c+d)):
                    if ((10*b+c)/f == g):
                      if ((100*d+10*a+d) * f == (1000*b+100*b+10*e+a)):
                        print(''.join([str(a),str(b),str(c),str(d),str(e),
                          str(f),str(g)]))
                    
quizsolver1()
quizsolver2()
