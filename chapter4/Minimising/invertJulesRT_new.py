#!/usr/bin/env python

import sys
import os
from copy import copy

import numpy as np
import matplotlib.pyplot as plt

import scipy.optimize as opt

from runJulesRTStruct import runJulesRTStruct

class julesRTData():
  def __init__(self):
    self.lai=float()
    self.leafT=float()
    self.leafR=float()
    self.soilR=float()
    self.sza=float()
    self.obsUncert=float()
    self.obsVal=float()
    self.diffuse=False
    self.unifrom=True
    self.obsType="fapar"

def julesRT_wrapper( argList, data ):
  """Call the Jules 2S model using a list variable
  Also implement any specific relationships between
  variables here (e.g. leaf_r=leaf_t)  
  
  argList is stuff to be minimised (i.e. structural parameters)  

  controlVars are other arguments required to be passed 

  szaList are the solar angles at which to evaluate the model
  """

  
  astruc=argList[0]
  bstruc=argList[1]    
  
  julesReturn=runJulesRTStruct(
    astruc=astruc,
    bstruc=bstruc,
    lai=data.lai,
    leafT=data.leafT,
    leafR=data.leafR,
    soilR=data.soilR,
    sza=data.sza,
    diffuse=data.diffuse,
    uniform=data.uniform)
    
  if data.obsType=='fapar':
    return julesReturn[0]
  else:
    return julesReturn[1]
  
  
  
  
def costFunction( params, controlData, Xprior=None, Xuncert=None  ):
  """Var-type cost function for JULES
  """
  
  n=len(controlData)
  Ymodel=np.zeros(n)
  Yobs=np.zeros(n)
  R=np.zeros((n,n))
  
  #compute the modelled albedo/fAPAR values
  for (i,data) in enumerate(controlData):
    Ymodel[i]=julesRT_wrapper( params, data )
    Yobs[i]=data.obsVal
    R[i,i]=1./(data.obsUncert**2)
 
 
  #VAR term one (obs):
  diff=Ymodel-Yobs
  cost=0.5*np.dot(diff,np.dot(R,diff.T))
  
  if Xprior != None:
    #compute B matrix
    B=np.diag(1./(np.array(Xuncert)**2))
    
    #VAR term two:
    diff=np.array(params)-np.array(Xprior)      
    cost+=0.5*np.dot(diff,np.dot(B,diff.T))
    
  return cost


  

def fminJulesRT( initParams, controls, Xprior=None, Xuncert=None ):
  '''Run the chosen minimisers over the data
  '''
  xOpt=opt.fmin( costFunction, initParams, args=(controls, Xprior, Xuncert ), disp=True, maxfun=10000)  
  return xOpt
  


def solveJulesStruct(controlData, initParams=np.array([0.0,0.0])):
  ''' An example function for running the minimiser
  '''
    
  ret=fminJulesRT( initParams, controlData, Xprior=None, Xuncert=None )
  print ret
  return ret

def addTwinObs(controlData,astruc=1.0,bstruc=0.0):  
  '''Add dummy (or "twin") observations into the control
  data given a value for the structure parameters
  '''
  for (i,data) in enumerate(controlData):
    controlData[i].obsVal=julesRT_wrapper( [astruc,bstruc], data )
    #print controlData[i].obsVal    

if __name__=="__main__":

  controlData=[]


  controlData.append(julesRTData())
  controlData[-1].lai=2.0
  controlData[-1].leafT=0.1 
  controlData[-1].leafR=0.15
  controlData[-1].soilR=0.05
  controlData[-1].sza=30.
  controlData[-1].diffuse=False  
  controlData[-1].uniform=True
  controlData[-1].obsType='fapar'
  controlData[-1].obsVal=0.0
  controlData[-1].obsUncert=1.0

  controlData.append(julesRTData())
  controlData[-1].lai=2.0
  controlData[-1].leafT=0.1 
  controlData[-1].leafR=0.15
  controlData[-1].soilR=0.05
  controlData[-1].sza=10.
  controlData[-1].diffuse=False  
  controlData[-1].uniform=True
  controlData[-1].obsType='fapar'
  controlData[-1].obsVal=0.0
  controlData[-1].obsUncert=1.0

  controlData.append(julesRTData())
  controlData[-1].lai=2.0
  controlData[-1].leafT=0.1 
  controlData[-1].leafR=0.15
  controlData[-1].soilR=0.05
  controlData[-1].sza=60.
  controlData[-1].diffuse=False  
  controlData[-1].uniform=True
  controlData[-1].obsType='fapar'
  controlData[-1].obsVal=0.0
  controlData[-1].obsUncert=1.0

  addTwinObs(controlData,astruc=1.0,bstruc=0.0)
  solveJulesStruct(controlData)

