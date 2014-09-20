def quizsolver1():
  for a in range(0,10):
    for b in range(0,10):
      for c in range(0,10):
        for d in range(0,10):
          for e in range(0,10):
            for f in range(1,10):
              for g in range(0,10):
                if (((10*a+b)*(10*b+c)==d*100+a*10+d)
                  and ((10*e+c)/f == f) 
                  and ((100*b+10*c+d)*g==1000*b+100*b+10*e+a)
                  and ((10*a+b)*(10*e+c)==100*b+10*c+d)
                  and ((10*b+c)/f == g) 
                  and ((100*d+10*a+d) * f == 1000*b+100*b+10*e+a)):
                    print(''.join([str(a),str(b),str(c),str(d),str(e),
                    str(f),str(g)]))

def quizsolver2():
  for a in range(0,10):
    for b in range(0,10):
      for d in range(0,10):
		for f in range(1,10):
		  for g in range(0,10):
			c = (f*f) % 10
			e = (f*f) / 10
			if (((10*a+b)*(10*b+c)==d*100+a*10+d)
			  and ((10*e+c)/f == f) 
			  and ((100*b+10*c+d)*g==1000*b+100*b+10*e+a)
			  and ((10*a+b)*(10*e+c)==100*b+10*c+d)
			  and ((10*b+c)/f == g) 
			  and ((100*d+10*a+d) * f == 1000*b+100*b+10*e+a)):
			  print(''.join([str(a),str(b),str(c),str(d),
			    str(e),str(f),str(g)]))
                    
quizsolver1()
quizsolver2()
