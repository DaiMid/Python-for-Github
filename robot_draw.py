import math, time
from tkinter import *

    
class Arm():
 
 def __init__ (self):
  # set length of 2 arms
  self.a1 = 300
  self.a2 = 200
  # start both arms vertical
  self.q1 = math.pi/2
  self.q2 = math.pi/2
  self.basex = 10
  self.basey = 350
  self.color = ("green")
  return

 def set_angle(self,pos):
   x1 = pos[0] - self.basex
   y1 = self.basey - pos[1]
   a1 = self.a1
   a2 = self.a2
  # first calculate q2
   self.q2 = math.acos((x1*x1+ y1*y1 - (a1*a1) - (a2*a2))/(2*a1*a2))
   #print (self.q2,180 * self.q2 / math.pi, "q2" )
     
   # now q1
   self.q1 = math.atan2(y1,x1) - math.atan2(a2*math.sin(self.q2), (a1+a2*math.cos(self.q2)))
   #print (self.q1,180 * self.q1 / math.pi, "q1")
   return self.q1

 def set_pivot(self, q1):
   x2 = self.a1*math.cos(self.q1)
   y2 = 350 - self.a1*math.sin(self.q1)
   pos = [x2,y2]
    
   return pos
 def draw_arm(self,canvas,pos1,pos2):
   self.canvas = canvas 
   self.canvas.create_line(self.basex,self.basey,pos1[0], pos1[1], fill=self.color, width= 5)
   self.canvas.create_line(pos1[0], pos1[1], pos2[0],pos2[1], fill=self.color, width= 5)
   return
class A_line():
 def __init__(self,pos1,pos2):
     self.pos1x = pos1[0]
     self.pos1y = pos1[1]
      
     self.pos2x = pos2[0]
     self.pos2y = pos2[1]
     self.by_value = 20
     self.complete = 0
     self.current_posx = self.pos1x
     self.current_posy = self.pos1y
     self.color = ("red")
     self.incx = (self.pos2x-self.pos1x)/self.by_value
     self.incy = (self.pos2y-self.pos1y)/self.by_value
     return
 def update_current_pos(self):
     self.current_posx += self.incx
     self.current_posy += self.incy
     current_pos = [self.current_posx, self.current_posy ]
      
     return current_pos
    
 def set_complete(self):
     self.complete = 1
      
     return
 def draw_line(self,canvas):
     self.canvas = canvas
      
     if self.complete == 1:
            x2 = self.pos2x
            y2 = self.pos2y
     else:
            x2 = self.current_posx
            y2 = self.current_posy
     self.canvas.create_line(self.pos1x, self.pos1y, x2, y2, fill=self.color) 
     return

        
      
my_page = Tk() 
my_page.title('Calculator') 
my_page.geometry('600x600')   
# Create a tkinter canvas object to draw on
my_canvas = Canvas(my_page)
my_canvas.pack(fill=BOTH, expand=1) 
     

# define the 6 points
our_points = [[100,100],[100,200],[180,260],[260,200],[260,100],[180,40]]
our_arm = Arm()
 
lines = []
for i in range (6):
    pos1 = our_points[i]
    next_i = (i+1)%6
    pos2 = our_points[next_i]
    
    our_line = A_line(pos1,pos2)
    lines.append(our_line)
   
for i in range (6):
    
    for j in range(20):
       my_canvas.delete("all") 
       my_canvas.pack(fill=BOTH, expand=1) 
       #my_page.update_idletasks() 
       target_pos = lines[i].update_current_pos()
       # print the lines    
       for k in range (6) :
    
            
           lines[k].draw_line(my_canvas)
       angle = our_arm.set_angle(target_pos)
       pivot1 = our_arm.set_pivot(angle)
       
       our_arm.draw_arm(my_canvas,pivot1,target_pos)
       my_page.update_idletasks()
       
       time.sleep(0.1)
      
    lines[i].set_complete() 
 
