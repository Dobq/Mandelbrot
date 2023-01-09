
#STARTING TO COUNT TIME#######################################################

from timeit import default_timer as timer

T=[timer()] #0

#CONSTANTS####################################################################

maxlim=500
#maxlim=1800
focus=complex(-1.759,0.02)
#focus=complex(-0.7471,0.1021)
dist=0.0000025
#dist=0.00000375
res=11
cl=16

resn=2**(res-1)
ress=2**res+1
R=list(range(ress))

#print(dist*2**(res-1)) #distance in complex plane from center to side of generated square

carmi=[102,0,51]
yello=[184,174,0]
seagr=[20,85,95]
white=[255,255,255]
black=[0,0,0]

#IMPORTS######################################################################

from math import sin,pi
from PIL.Image import fromarray
from numpy import array,uint8

#MACHINERY####################################################################

def citer(x,p,lim):
    if abs(x)>2:
        return 0
    if lim==0:
        return 0
    else:
        return citer(x**2+p,p,lim-1)+1

#COLOR PATTERN AND COLORING FUNCTIONS#########################################

Col_c=[
        array([
                round((sin(i/cl*pi))*carmi[j]+(1-sin(i/cl*pi))*white[j])
                for j in range(3)
        ])
        for i in range(cl)
]
Col_s=[
        array([
                round((sin(i/cl*pi))*seagr[j]+(1-sin(i/cl*pi))*white[j])
                for j in range(3)
        ])
        for i in range(cl)
]
Col=Col_c+Col_s

def fRGB(n):
    if n<maxlim:
        return Col[n%(len(Col))]
    else:
        return black

def arrayRGB(L):
    data=array([array(list(map(fRGB,L[i]))) for i in R],dtype=uint8)
    return data

T.append(timer()) #1

#CALCULATING STUFF, COLORING AND SAVING GRAPHICS##############################

fromarray(arrayRGB([[citer(0,focus+complex((i-resn)*dist,(j-resn)*dist),maxlim) for j in R] for i in R]),'RGB').save('image_simple.png')

T.append(timer()) #2

#PRINTING TIMES###############################################################

for i in range(2):
    print(round(T[i+1]-T[i],3))
print('Total time: '+str(round(T[2]-T[0],4))+' seconds.')

##############################################################################
