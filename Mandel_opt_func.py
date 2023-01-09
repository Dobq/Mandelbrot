
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
RR=[[i,j] for j in R for i in R]

#print(dist*2**(res-1)) #distance in complex plane from center to side of generated square

carmi=[102,0,51]
yello=[184,174,0]
seagr=[20,85,95]
white=[255,255,255]
black=[0,0,0]

#IMPORTS######################################################################

from math import sin,pi
from PIL.Image import fromarray
from numpy import array,full,uint8

#MACHINERY####################################################################

def num(i,j):
    return focus+complex((i-resn)*dist,(j-resn)*dist)

def citer(p,x=0,lim=maxlim):
    if abs(x)>2:
        return 0
    elif lim==0:
        return 0
    else:
        return citer(p,x**2+p,lim-1)+1 

def calc_inse(i,j):
    M[i,j]=citer(num(i,j))

def calc_cros(l):
    i,j,s,k=l[0],l[1],l[2],l[3]
    calc_inse(s*(2*i)+k,s*(1+2*j))
    calc_inse(s*(1+2*i),s*(2*j)+k)

def squa_divi(step):
    ss=s
    list(map(calc_cros,
            [
                    (i,j,s,k)
                    for k in list(range(1,ss*2))
                    for (i,j,s) in list(filter(
                            lambda l: M[l[2]*(2*l[0]+1),l[2]*(2*l[1]+1)]==-1,
                            [(i,j,ss) for (i,j) in RR_l]
                    ))
            ]
    ))

def squa_inse(l):
    squac[0]+=s**2 #comment it if statistics not wanted
    M[s*l[0]+1:s*l[0]+s,s*l[1]+1:s*l[1]+s]=full((s-1,s-1),M[s*l[0],s*l[1]],dtype=int)

def squa_chec(step):
    list(map(squa_inse,
            list(filter(
                    lambda l:
                            M[s*l[0]+s//2,s*l[1]+s//2]==-1
                            and len(set([
                                    M[s*l[0],s*l[1]],
                                    M[s*l[0]+s,s*l[1]],
                                    M[s*l[0],s*l[1]+s],
                                    M[s*l[0]+s,s*l[1]+s]
                            ]))==1
                            and len(set().union(
                                    set(M[s*l[0]:s*l[0]+s,s*l[1]]),
                                    set(M[s*l[0],s*l[1]:s*l[1]+s]),
                                    set(M[s*l[0]:s*l[0]+s,s*l[1]+s]),
                                    set(M[s*l[0]+s,s*l[1]:s*l[1]+s])
                            ))==1,
                    [[i,j] for j in range(2**(res-step+1)) for i in range(2**(res-step+1))]
            ))
    ))

squac=[0] #comment it if statistics not wanted
s=0
RR_l=[]
def squa_stuf(step):
    #print(step)
    global s
    s=(2**(step-1))
    RR_l[:]=[(i,j) for j in range(2**(res-step)) for i in range(2**(res-step))]
    squa_divi(step)
    squa_chec(step)

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
    if -1<n<maxlim:
        return Col[n%(len(Col))]
    elif n==maxlim:
        return black
    else:
        return yello

def arrayRGB(L):
    return array([array(list(map(fRGB,L[i]))) for i in R],dtype=uint8)

T.append(timer()) #1

#CALCULATIONS#################################################################

M=full((ress,ress),-1,dtype=int)

for k in R:
    calc_inse(k,0)
    calc_inse(k,ress-1)
    calc_inse(0,k)
    calc_inse(ress-1,k)

T.append(timer()) #2

list(map(squa_stuf,reversed(range(3,res+1))))

T.append(timer()) #3

list(map(lambda l: calc_inse(l[0],l[1]),list(filter(lambda l: M[l[0],l[1]]==-1,RR))))

T.append(timer()) #4

#SAVING GRAPHICS##############################################################

fromarray(arrayRGB(M),'RGB').save('image_opt_func.png')

T.append(timer()) #5

#PRINTING STATISTICS##########################################################

#comment three lines below if statistics not wanted
print(ress**2)
print(squac[0])
print('Pixels calculated indirectly: '+str(round(100*squac[0]/ress**2,3))+'%.')

#PRINTING TIMES###############################################################

for i in range(5):
    print(round(T[i+1]-T[i],3))
print('Total time: '+str(round(T[5]-T[0],3))+' seconds.')

##############################################################################
