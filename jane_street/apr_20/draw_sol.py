import matplotlib.pyplot as plt 
import glob

T=[int(k*(k+1)/2) for k in range(40)]

dx = 1
dy = 3**(0.5)/2

def f(n):
	if n==1:
		return (0,0)

	prev = f(n-1)

	if (n-1) in T:
		return (-prev[0]-0.5,prev[1]-dy)

	else:
		return (prev[0]+1,prev[1])


files = glob.glob('sol/data/tri_*.txt')

for file_name in files:
	with open(file_name,"r") as file:
		print(file_name)
		lines = file.readlines()
		if lines[-1]=="solutions: 1\n":
			go = True
			lines=lines[:-2]
		else:
			go = False
	
	if go:
		N_points = len(lines[0][:-1].replace(" ",""))
		N=T.index(N_points)
		
		P = range(1,N_points+1)
		plt.figure()
		for l in lines:
			l=l[:-1]
			o=map(int,l.split(" "))
			p1,p2,p3 = [f(P[i]) for i,j in enumerate(o) if j==1]

			plt.plot([p1[0],p2[0]],[p1[1],p2[1]],linewidth=0.5,color='r')
			plt.plot([p1[0],p3[0]],[p1[1],p3[1]],linewidth=0.5,color='r')
			plt.plot([p3[0],p2[0]],[p3[1],p2[1]],linewidth=0.5,color='r')

		for p in P:
			plt.plot(f(p)[0],f(p)[1],'ok',markersize=1)


		plt.axis('off')
		plt.tight_layout()
		plt.savefig("./img/"+str(N)+".pdf")