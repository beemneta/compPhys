'''
project simulation.py
motion of a ball
'''
from visual import *
from math import cos,sin
from visual.controls import *


#define a floor
floor = box(length=40, height=0.5,width = 100,color=color.green)
leftpost=box(length=0.5,height=2.75,width=0.5,color=color.white,pos=(3.5,1.4,0))
rightpost=box(length=0.5,height=2.75,width=0.5,color=color.white,pos=(-3.5,1.4,0))
toppost=box(length=7.5,height=0.5,width=0.5,color=color.white,pos=(0,2.75,0))
#change the s u and t values to try different trajectories
s=  -60   #the horizontal component speed of shot (Z dxn)
u=9     #vertical component speed of shot
t=2       #horizontal component speed of shot (X dxn)
teta=55         #angle from the ground towards the goal
g=9.81
vt=25       #terminal speed
k_D=0.00275
k_L=0.0025
phi=-5
#create a ball
ball = sphere(pos= (0,0.8,30), color = color.white,radius=0.22,mass=0.43)       #change the position to try different distances in the z axis, and to a reasonable range the x axis, the y component is the v
#vertical height which is supposed to be on the ground level
ball.velocity= vector(t,u,s)
c = controls(title='Speed and Distance selection',x=440, y=0, range=100,width=400)

h = 0.01
ball.trail=curve(color=ball.color)
xs=0     #initial value

##vx=slider(pos=(-50,0), width=7, length=50, axis=(10,0,0),min=-3,max=3,action=lambda: set())
##vx.value=t
##vy=slider(pos=(-50,-20), width=7, length=50, axis=(10,0,0),min=0,max=25,action=lambda: set())
##vy.value=u
##vz=slider(pos=(-50,-40), width=7, length=50, axis=(10,0,0),min=0,max=32,action=lambda: set())
##vz.value=s
##s_text=label(pos=(60,0), text='initial speed in x dxn ' ,display=c.display,box=0,line=0)
##s_text=label(pos=(60,-20), text='initial speed in y dxn  ' ,display=c.display,box=0,line=0)
##s_text=label(pos=(60,-40), text='initial speed in z dxn ' ,display=c.display,box=0,line=0)
##reset_button = button(pos=(-20,40), height=10, width=50, text='Reset', action=lambda: reset())
##s2=slider (pos=(-50,-60), width=7, length=50, axis=(10,0,0))
##s_text=label(pos=(60,-60), text='distance from goal ',display=c.display,box=0,line=0,min=20,max=35)
##start_button = button(pos=(40,40), height=10, width=50, text='Start', action=lambda: reset())
##
def set():
    if vx.value>2.5:
        vx.value=2.5
    elif vx.value<-2.5:
        vx.value=-2.5
    t=int(vx.value)
    if vy.value>20:
        vy.value=20
    elif vy.value<0:
        vy.value=0
    u=int(vy.value)
    if vz.value>30:
        vz.value=30
    elif vz.value<0:
        vz.value=0
    s=int(vz.value)
def start():
    ball.velocity.y=u
    ball.velocity.z=s
    ball.velocity.x=t
    go()
def reset():
    s=0
    t=0
    u=0
    ball.pos=(0,0.8,30)
    
while True:
    rate(100)
    ball.pos = ball.pos + ball.velocity*h
    ball.trail.append(pos=ball.pos)
    if ball.y < 0.8:
        ball.velocity.y= -ball.velocity.y
    if ball.z < -120:
        ball.velocity=0
        ball.pos(0,1,25)
        
    else:
        #az = -g* sqrt(ball.velocity.z*ball.velocity.z+ball.velocity.y*ball.velocity.y)*ball.velocity.z/(vt*vt)
        az = -k_D*mag(ball.velocity)*ball.velocity.z + k_L*(ball.velocity.y*teta*sin(phi) - ball.velocity.x*teta*cos(phi))
        ay= -g*(1.0 + ball.velocity.y/vt)
        ax = -k_D*mag(ball.velocity)*ball.velocity.x + k_L*ball.velocity.z*teta*cos(phi)
        ball.velocity.y= ball.velocity.y + ay*h
        ball.velocity.z = ball.velocity.z + az*h
        ball.velocity.x= ball.velocity.x +ax*h       
    
