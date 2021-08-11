import controller, sys
import model   # Pass a reference to this module to each update call in update_all

#Use the reference to this module to pass it to update methods

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running = False
cycle_count = 0
balls = set()
object_clicked = None
single_step = False

#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running, cycle_count, balls
    running = False
    cycle_count = 0
    balls = set()


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#tep just one update in the simulation
def step ():
    global running, single_step
    running = True
    single_step = True


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global object_clicked
    object_clicked = kind


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    global object_clicked, balls
    if object_clicked is None:
        pass
    elif object_clicked is 'remove':
        riddance = find(lambda bolas: bolas.conatains(x, y))
        for i in riddance:
            remove(i)
    else:
        balls.add(eval(object_clicked+'({},{})'.format(x,y)))
        

#add simulton s to the simulation
def add(s):
    global balls
    balls.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    global balls
    balls.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    global balls
    new = set()
    for i in balls:
        if p(i):
            new.add(i)
    return new


#call update for each simulton in the simulation (pass the model as an argument)
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def update_all():
    global balls, cycle_count, running, single_step, running
    
    copy = set(balls)
    
    if running:
        cycle_count += 1
        for ball in copy:
            if ball in balls:
                ball.update(model)
    
    if single_step:
        running = False
        single_step = False


#delete from the canvas every simulton being simulated; next call display on every
#  simulton being simulated to add it back to the canvas, possibly in a new location, to
#  animate it; also, update the progress label defined in the controller
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for b in balls:
        b.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(cycle_count)+" cycles/"+str(len(balls))+" balls")
