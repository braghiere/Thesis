#!/home/db903833/dataLand01/enthoughtDistros/epd-7.2-2-rh5-x86_64/bin/python
#!/use/bin/env python

import sys
import subprocess

import numpy as np

##################################################### RUN JULES RT VERSION 2 ############################################################
#Tonzi Ranch
#lai=0.7, soilR=0.105, leafR=0.085, leafT=0.028, sza=20., astruc=1.0, bstruc= 0.0, diffuse=False, uniform=True 
#RAMI4PILPS PAR_050_BLK 
#lai=0.50265, soilR=0.00001, leafR=0.0735, leafT=0.0566, sza=20., astruc=1.0, bstruc= 0.0, diffuse=False, uniform=True

def runJulesRTStruct( lai=0.50265, soilR=0.2142, leafR=0.3912, leafT=0.4146, sza=20., astruc=0.418187, bstruc= 0.205974, diffuse=False, uniform=True  ):
  """Run the JULES 2-stream interface
  """

#def runJulesRTStruct( lai=2.0, soilR=0.1, leafR=0.1, leafT=0.1, sza=20., astruc=0.4, bstruc=0.0, diffuse=False, uniform=True ):
#  """Run the JULES 2-stream interface
#  """
 
  #run JULES 2S

  exe="./julesRTStruct"

  cmd=[]
  cmd.append(exe)
  
  cmd.append("-sza")
  cmd.append("%f"%sza)
  
  cmd.append("-lai")
  cmd.append("%f"%lai)
  
  cmd.append("-albs")
  cmd.append("%f"%soilR)
  
  cmd.append("-rleaf")
  cmd.append("%f"%leafR)

  cmd.append("-astruc")
  cmd.append("%f"%astruc)
  
  cmd.append("-bstruc")
  cmd.append("%f"%bstruc)
  
  cmd.append("-omega")
  cmd.append("%f"%(leafR+leafT))
  
  if diffuse:
    cmd.append("-diffuse")
  else:
    cmd.append("-direct")
    
  if uniform:
    cmd.append("-uniform")
  else:
    cmd.append("-horizontal")
    
    
    
  p=subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  out=p.stdout.readlines()
  err=p.stderr.readlines()
  p.wait()
    
  try:  
    print "Success in runJules2S:", out,lai,leafR,leafT,soilR
    return [float(out[0].split()[0]),float(out[0].split()[1])]
  except:
    print >> sys.stderr, "Error in runJules2S:", out,lai,leafR,leafT,soilR
    raise
  
if __name__=="__main__":
 
  
  #for sza in [27.4643]:
  #	print sza, runJulesRTStruct(sza=sza,astruc=0.341,bstruc=0.099) 
  
   for sza in [0,	1,	2,	3,	4,	5,	6,	7,	8,	9,	10,	11,	12,	13,	14,	15,	16,	17,	18,	19,	20,	21,	22,	23,	24,	25,	26,	27,	28,	29,	30,	31,	32,	33,	34,	35,	36,	37,	38,	39,	40,	41,	42,	43,	44,	45,	46,	47,	48,	49,	50,	51,	52,	53,	54,	55,	56,	57,	58,	59,	60,	61,	62,	63,	64,	65,	66,	67,	68,	69,	70,	71,	72,	73,	74,	75,	76,	77,	78,	79,	80,	81,	82,	83,	84,     85,     86,     87,     88,     89,     89.9]:
    print sza, runJulesRTStruct(sza=sza,astruc=1.0, bstruc= 0.0) 
     #print sza, runJulesRTStruct(sza=27.4643,astruc=0.341,bstruc=0.099) 
