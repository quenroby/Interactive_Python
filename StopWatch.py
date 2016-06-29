# template for "Stopwatch: The Game"
import simplegui


# define global variables

time = 0
x = 0
y = 0
stop = True



# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
# A = mins (0-9), B = tens of secons (0-5), 
# C = ones of seconds(0-9), D = hundreds of seconds (0-9) 

def format(t):
    A = (t / 600) % 10
    B = (t/100) % 6
    C = (t/10) % 10
    D = t % 10
    return str(A) + ":" + str(B) + str(C) + "." + str(D)  
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start_handler():
    global stop
    timer.start()
    stop = False

def Stop_handler():
    global x, y, time, stop
    timer.stop()
    
    #StopWatch Game Logic
    if stop == False:
        if time % 10 == 0 and time != 0:
            x += 1
            y += 1
            stop = True
        elif time != 0:
            y += 1
            stop = True
        else:
            print "This is broken!"

    
     
def Restart_handler():
    global x, y, time, stop
    timer.stop()
    time = 0
    x = 0
    y = 0
    stop = True
    

# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time += 1
    
    

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), [60,100], 36, "White")
    canvas.draw_text(str(x)+"/"+str(y), [160,30], 30, "White")
    
    
# create frame
frame = simplegui.create_frame('StopWatch', 220, 150)

# register event handlers
frame.set_draw_handler(draw)
Start = frame.add_button('Start', Start_handler, 200)
Stop = frame.add_button('Stop', Stop_handler, 200)
Restart = frame.add_button('Restart', Restart_handler, 200)
timer = simplegui.create_timer(100, tick)


# start frame
frame.start()

# Please remember to review the grading rubric
