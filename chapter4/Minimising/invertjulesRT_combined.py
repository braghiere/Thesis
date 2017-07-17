from library_rami4pilps import *
#from foo1 import *
from RAMI4PILPS_reference_values import *
from invertJulesRT_new import *
from copy import copy
from array import array
from pylab import *

from runJulesRTStruct import runJulesRTStruct

import numpy as np
import matplotlib.pyplot as plt


controlData=[]

# Sparse canopy 

#Absorbed PAR
controlData.append(OFC_FABS_PAR_050_BLK_27)
controlData.append(OFC_FABS_PAR_050_BLK_60)
controlData.append(OFC_FABS_PAR_050_BLK_83)
controlData.append(OFC_FABS_PAR_050_BLK_99)
controlData.append(OFC_FABS_PAR_050_MED_27)
controlData.append(OFC_FABS_PAR_050_MED_60)
controlData.append(OFC_FABS_PAR_050_MED_83)
controlData.append(OFC_FABS_PAR_050_MED_99)
controlData.append(OFC_FABS_PAR_050_SNW_27)
controlData.append(OFC_FABS_PAR_050_SNW_60)
controlData.append(OFC_FABS_PAR_050_SNW_83)
controlData.append(OFC_FABS_PAR_050_SNW_99)

#Reflected PAR
controlData.append(OFC_FREF_PAR_050_BLK_27)
controlData.append(OFC_FREF_PAR_050_BLK_60)
controlData.append(OFC_FREF_PAR_050_BLK_83)
controlData.append(OFC_FREF_PAR_050_BLK_99)
controlData.append(OFC_FREF_PAR_050_MED_27)
controlData.append(OFC_FREF_PAR_050_MED_60)
controlData.append(OFC_FREF_PAR_050_MED_83)
controlData.append(OFC_FREF_PAR_050_MED_99)
controlData.append(OFC_FREF_PAR_050_SNW_27)
controlData.append(OFC_FREF_PAR_050_SNW_60)
controlData.append(OFC_FREF_PAR_050_SNW_83)
controlData.append(OFC_FREF_PAR_050_SNW_99)

#Absorbed NIR
#controlData.append(OFC_FABS_NIR_050_BLK_27)
#controlData.append(OFC_FABS_NIR_050_BLK_60)
#controlData.append(OFC_FABS_NIR_050_BLK_83)
#controlData.append(OFC_FABS_NIR_050_BLK_99)
#controlData.append(OFC_FABS_NIR_050_MED_27)
#controlData.append(OFC_FABS_NIR_050_MED_60)
#controlData.append(OFC_FABS_NIR_050_MED_83)
#controlData.append(OFC_FABS_NIR_050_MED_99)
#controlData.append(OFC_FABS_NIR_050_SNW_27)
#controlData.append(OFC_FABS_NIR_050_SNW_60)
#controlData.append(OFC_FABS_NIR_050_SNW_83)
#controlData.append(OFC_FABS_NIR_050_SNW_99)

#Reflected NIR
#controlData.append(OFC_FREF_NIR_050_BLK_27)
#controlData.append(OFC_FREF_NIR_050_BLK_60)
#controlData.append(OFC_FREF_NIR_050_BLK_83)
#controlData.append(OFC_FREF_NIR_050_BLK_99)
#controlData.append(OFC_FREF_NIR_050_MED_27)
#controlData.append(OFC_FREF_NIR_050_MED_60)
#controlData.append(OFC_FREF_NIR_050_MED_83)
#controlData.append(OFC_FREF_NIR_050_MED_99)
#controlData.append(OFC_FREF_NIR_050_SNW_27)
#controlData.append(OFC_FREF_NIR_050_SNW_60)
#controlData.append(OFC_FREF_NIR_050_SNW_83)
#controlData.append(OFC_FREF_NIR_050_SNW_99)



#Medium canopy

#Absorbed PAR
#controlData.append(OFC_FABS_PAR_150_BLK_27)
#controlData.append(OFC_FABS_PAR_150_BLK_60)
#controlData.append(OFC_FABS_PAR_150_BLK_83)
#controlData.append(OFC_FABS_PAR_150_BLK_99)
#controlData.append(OFC_FABS_PAR_150_MED_27)
#controlData.append(OFC_FABS_PAR_150_MED_60)
#controlData.append(OFC_FABS_PAR_150_MED_83)
#controlData.append(OFC_FABS_PAR_150_MED_99)
#controlData.append(OFC_FABS_PAR_150_SNW_27)
#controlData.append(OFC_FABS_PAR_150_SNW_60)
#controlData.append(OFC_FABS_PAR_150_SNW_83)
#controlData.append(OFC_FABS_PAR_150_SNW_99)

#Reflected PAR
#controlData.append(OFC_FREF_PAR_150_BLK_27)
#controlData.append(OFC_FREF_PAR_150_BLK_60)
#controlData.append(OFC_FREF_PAR_150_BLK_83)
#controlData.append(OFC_FREF_PAR_150_BLK_99)
#controlData.append(OFC_FREF_PAR_150_MED_27)
#controlData.append(OFC_FREF_PAR_150_MED_60)
#controlData.append(OFC_FREF_PAR_150_MED_83)
#controlData.append(OFC_FREF_PAR_150_MED_99)
#controlData.append(OFC_FREF_PAR_150_SNW_27)
#controlData.append(OFC_FREF_PAR_150_SNW_60)
#controlData.append(OFC_FREF_PAR_150_SNW_83)
#controlData.append(OFC_FREF_PAR_150_SNW_99)

#Absorbed NIR
#controlData.append(OFC_FABS_NIR_150_BLK_27)
#controlData.append(OFC_FABS_NIR_150_BLK_60)
#controlData.append(OFC_FABS_NIR_150_BLK_83)
#controlData.append(OFC_FABS_NIR_150_BLK_99)
#controlData.append(OFC_FABS_NIR_150_MED_27)
#controlData.append(OFC_FABS_NIR_150_MED_60)
#controlData.append(OFC_FABS_NIR_150_MED_83)
#controlData.append(OFC_FABS_NIR_150_MED_99)
#controlData.append(OFC_FABS_NIR_150_SNW_27)
#controlData.append(OFC_FABS_NIR_150_SNW_60)
#controlData.append(OFC_FABS_NIR_150_SNW_83)
#controlData.append(OFC_FABS_NIR_150_SNW_99)

#Reflected NIR
#controlData.append(OFC_FREF_NIR_150_BLK_27)
#controlData.append(OFC_FREF_NIR_150_BLK_60)
#controlData.append(OFC_FREF_NIR_150_BLK_83)
#controlData.append(OFC_FREF_NIR_150_BLK_99)
#controlData.append(OFC_FREF_NIR_150_MED_27)
#controlData.append(OFC_FREF_NIR_150_MED_60)
#controlData.append(OFC_FREF_NIR_150_MED_83)
#controlData.append(OFC_FREF_NIR_150_MED_99)
#controlData.append(OFC_FREF_NIR_150_SNW_27)
#controlData.append(OFC_FREF_NIR_150_SNW_60)
#controlData.append(OFC_FREF_NIR_150_SNW_83)
#controlData.append(OFC_FREF_NIR_150_SNW_99)



#Dense canopy


#Absorbed PAR
#controlData.append(OFC_FABS_PAR_250_BLK_27)
#controlData.append(OFC_FABS_PAR_250_BLK_60)
#controlData.append(OFC_FABS_PAR_250_BLK_83)
#controlData.append(OFC_FABS_PAR_250_BLK_99)
#controlData.append(OFC_FABS_PAR_250_MED_27)
#controlData.append(OFC_FABS_PAR_250_MED_60)
#controlData.append(OFC_FABS_PAR_250_MED_83)
#controlData.append(OFC_FABS_PAR_250_MED_99)
#controlData.append(OFC_FABS_PAR_250_SNW_27)
#controlData.append(OFC_FABS_PAR_250_SNW_60)
#controlData.append(OFC_FABS_PAR_250_SNW_83)
#controlData.append(OFC_FABS_PAR_250_SNW_99)

#Reflected PAR
#controlData.append(OFC_FREF_PAR_250_BLK_27)
#controlData.append(OFC_FREF_PAR_250_BLK_60)
#controlData.append(OFC_FREF_PAR_250_BLK_83)
#controlData.append(OFC_FREF_PAR_250_BLK_99)
#controlData.append(OFC_FREF_PAR_250_MED_27)
#controlData.append(OFC_FREF_PAR_250_MED_60)
#controlData.append(OFC_FREF_PAR_250_MED_83)
#controlData.append(OFC_FREF_PAR_250_MED_99)
#controlData.append(OFC_FREF_PAR_250_SNW_27)
#controlData.append(OFC_FREF_PAR_250_SNW_60)
#controlData.append(OFC_FREF_PAR_250_SNW_83)
#controlData.append(OFC_FREF_PAR_250_SNW_99)

#Absorbed NIR
#controlData.append(OFC_FABS_NIR_250_BLK_27)
#controlData.append(OFC_FABS_NIR_250_BLK_60)
#controlData.append(OFC_FABS_NIR_250_BLK_83)
#controlData.append(OFC_FABS_NIR_250_BLK_99)
#controlData.append(OFC_FABS_NIR_250_MED_27)
#controlData.append(OFC_FABS_NIR_250_MED_60)
#controlData.append(OFC_FABS_NIR_250_MED_83)
#controlData.append(OFC_FABS_NIR_250_MED_99)
#controlData.append(OFC_FABS_NIR_250_SNW_27)
#controlData.append(OFC_FABS_NIR_250_SNW_60)
#controlData.append(OFC_FABS_NIR_250_SNW_83)
#controlData.append(OFC_FABS_NIR_250_SNW_99)

#Reflected NIR
#controlData.append(OFC_FREF_NIR_250_BLK_27)
#controlData.append(OFC_FREF_NIR_250_BLK_60)
#controlData.append(OFC_FREF_NIR_250_BLK_83)
#controlData.append(OFC_FREF_NIR_250_BLK_99)
#controlData.append(OFC_FREF_NIR_250_MED_27)
#controlData.append(OFC_FREF_NIR_250_MED_60)
#controlData.append(OFC_FREF_NIR_250_MED_83)
#controlData.append(OFC_FREF_NIR_250_MED_99)
#controlData.append(OFC_FREF_NIR_250_SNW_27)
#controlData.append(OFC_FREF_NIR_250_SNW_60)
#controlData.append(OFC_FREF_NIR_250_SNW_83)
#controlData.append(OFC_FREF_NIR_250_SNW_99)



[a,b]=solveJulesStruct(controlData,initParams=np.array([1.0,0.0]))
[a,b]=solveJulesStruct(controlData,[a,b])

x = []
jules_str = []
jules_ori = []

#type here your own structure factor parameters
#[a,b]=[0.34346912,0.09578224]

print a,b

for sza in range (0,90):
    x.append(sza),jules_str.append(runJulesRTStruct(sza=sza,astruc=a,bstruc=b,lai=0.50265, soilR=0.9640, leafR=0.0735, leafT=0.0566, diffuse=False, uniform=True)),jules_ori.append(runJulesRTStruct(sza=sza,astruc=1.0,bstruc=0.0,lai=0.50265, soilR=0.9640, leafR=0.0735, leafT=0.0566, diffuse=False, uniform=True))

#print x
#print y 

fapar_str = tuple(x[0] for x in jules_str)
albedo_str = tuple(x[1] for x in jules_str)
fapar_ori = tuple(x[0] for x in jules_ori)
albedo_ori = tuple(x[1] for x in jules_ori)


forwardModel=copy(controlData)

#addTwinObs(forwardModel,astruc=a,bstruc=b)

  #figure

title('Nonsense')
xlabel('x-stuff')
ylabel('y-stuff')
plt.grid()
plt.legend()
   # the scatter plot:
axScatter = plt.subplot(111)
axScatter.scatter(x, albedo_ori,label='Two-stream')

   # set axes range
plt.xlim(0, 90)
plt.ylim(0, 1)

#plt.scatter(SZA_RAMI4PILPS,RAMI4PILPS_fabs_NIR_OFC_050_BLK, color='Y', marker='x', s=300)
#plt.scatter(SZA_RAMI4PILPS,RAMI4PILPS_fabs_NIR_OFC_050_MED, color='Y', marker='x', s=300)
#plt.scatter(SZA_RAMI4PILPS,RAMI4PILPS_fabs_NIR_OFC_050_SNW, color='Y', marker='x', s=300)
plt.scatter(SZA_RAMI4PILPS,RAMI4PILPS_fref_PAR_OFC_050_SNW, color='Y', marker='x', s=300)
#plt.scatter(SZA_RAMI4PILPS,RAMI4PILPS_fabs_PAR_OFC_050_BLK, color='R', marker='x', s=300)
#plt.scatter(SZA_RAMI4PILPS,RAMI4PILPS_fabs_PAR_OFC_050_MED, color='R', marker='x', s=300)
#plt.scatter(SZA_RAMI4PILPS,RAMI4PILPS_fabs_PAR_OFC_050_SNW, color='R', marker='x', s=300)

plt.scatter(x, albedo_str, alpha=0.5,label='Structure')

plt.show()


