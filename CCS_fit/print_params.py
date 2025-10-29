from ccs_fit.ase_calculator.ccs_ase_calculator import spline_table
import json
import numpy as np

with open("UNC_params.json", "r") as f:
    CCS_params = json.load(f)

q=CCS_params["Charge scaling factor"]

print ("species   5")
print (f"Li      core    {q}")
print ("X      core   0.000000")
print (f"Tc     core    {-q}")
print ("Rh      core   0.000000")
print (f"Mn      core   {-q}")

elem1="Li"
elem2="Li"
r=[3.0451129999999997]
tb = spline_table(elem1, elem2, CCS_params)
#for rr in r:
#    print(elem1,elem2,rr,tb.eval_energy(rr)) 

#for rr in r:
#	print('lennard 0 0')
#	print(elem1,'core',elem2,tb.eval_energy(rr),rr)

for i in range(len(r)):
	print('lennard 0 0')
	if i==0:
		print(elem1,'core',elem2,tb.eval_energy(r[i]),0,0, r[i]+0.01)
	else:
		print(elem1,'core',elem2,tb.eval_energy(r[i]),0,r[i-1]+0.01,r[i]+0.01)

elem1="Tc"
elem2="Tc"
r=[3.9180338998155695]
tb = spline_table(elem1, elem2, CCS_params)
#for rr in r:
#    print(elem1,elem2,rr,tb.eval_energy(rr)) 
#for rr in r:
#        print('lennard 0 0')
#        print(elem1,'core',elem2,tb.eval_energy(rr),rr)
for i in range(len(r)):
        print('lennard 0 0')
        if i==0:
                print(elem1,'core',elem2,tb.eval_energy(r[i]),0,0, r[i]+0.01)
        else:
                print(elem1,'core',elem2,tb.eval_energy(r[i]),0,r[i-1]+0.01,r[i]+0.01)

elem1="Mn"
elem2="Mn"
r=[3.9180338998155695]
tb = spline_table(elem1, elem2, CCS_params)
#for rr in r:
#    print(elem1,elem2,rr,tb.eval_energy(rr))
#for rr in r:
#        print('lennard 0 0')
#        print(elem1,'core',elem2,tb.eval_energy(rr),rr)
for i in range(len(r)):
        print('lennard 0 0')
        if i==0:
                print(elem1,'core',elem2,tb.eval_energy(r[i]),0,0, r[i]+0.01)
        else:
                print(elem1,'core',elem2,tb.eval_energy(r[i]),0,r[i-1]+0.01,r[i]+0.01)

elem1="Li"
elem2="Tc"
r=[3.3172787008235822,3.5483990550643667,3.70222119590868]
tb = spline_table(elem1, elem2, CCS_params)
#for rr in r:
#    print(elem1,elem2,rr,tb.eval_energy(rr)) 
#for rr in r:
#        print('lennard 0 0')
#        print(elem1,'core',elem2,tb.eval_energy(rr),rr)
for i in range(len(r)):
        print('lennard 0 0')
        if i==0:
                print(elem1,'core',elem2,tb.eval_energy(r[i]),0,0, r[i]+0.01)
        else:
                print(elem1,'core',elem2,tb.eval_energy(r[i]),0,r[i-1]+0.01,r[i]+0.01)

elem1="Li"
elem2="Mn"
r=[3.3172787008235822,3.5483990550643667,3.70222119590868]
tb = spline_table(elem1, elem2, CCS_params)
#for rr in r:
#    print(elem1,elem2,rr,tb.eval_energy(rr)) 
#for rr in r:
#        print('lennard 0 0')
#        print(elem1,'core',elem2,tb.eval_energy(rr),rr)
for i in range(len(r)):
        print('lennard 0 0')
        if i==0:
                print(elem1,'core',elem2,tb.eval_energy(r[i]),0,0, r[i]+0.01)
        else:
                print(elem1,'core',elem2,tb.eval_energy(r[i]),0,r[i-1]+0.01,r[i]+0.01)

elem1="Tc"
elem2="Mn"
r=[3.9180338998155695]
tb = spline_table(elem1, elem2, CCS_params)
#for rr in r:
#    print(elem1,elem2,rr,tb.eval_energy(rr)) 
#for rr in r:
#        print('lennard 0 0')
#        print(elem1,'core',elem2,tb.eval_energy(rr),rr)
for i in range(len(r)):
        print('lennard 0 0')
        if i==0:
                print(elem1,'core',elem2,tb.eval_energy(r[i]),0,0, r[i]+0.01)
        else:
                print(elem1,'core',elem2,tb.eval_energy(r[i]),0,r[i-1]+0.01,r[i]+0.01)
