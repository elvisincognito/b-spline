from Tkinter import *
from Canvas import *
import sys

WIDTH  = 400 # width of canvas
HEIGHT = 400 # height of canvas

HPSIZE = 2 # half of point size (must be integer)
CCOLOR = "#0000FF" # blue (color of control-points and polygon)

BCOLOR = "#000000" # black (color of bezier curve)
BWIDTH = 2 # width of bezier curve

pointList = []   # list of (control-)points
elementList = [] # list of elements (used by Canvas.delete(...))

M = -1	#Derzeite Anzahl Kontrollpunkte
maxM = 20	#Maximale Anzahl Kontrollpunkte
#order = 4
#degree = order - 1


def drawPoints():
    """ draw (control-)points """
    for p in pointList:
		element = can.create_oval(p[0]-HPSIZE, p[1]-HPSIZE, p[0]+HPSIZE, p[1]+HPSIZE, fill=CCOLOR, outline=CCOLOR)
		elementList.append(element)


def drawPolygon():
    """ draw (control-)polygon conecting (control-)points """
    if len(pointList) > 1:
        for i in range(len(pointList)-1):
            element = can.create_line(pointList[i][0], pointList[i][1], pointList[i+1][0], pointList[i+1][1], fill=CCOLOR)
            elementList.append(element)


def drawBezierCurve():
    """ draw bezier curve defined by (control-)points """
    print "drawBezierCurve() not yet implemented..."
    print "curve should have color: ", BCOLOR, " and width: ", BWIDTH



def quit(root=None):
    """ quit programm """
    if root==None:
        sys.exit(0)
    root._root().quit()
    root._root().destroy()


def draw():
    """ draw elements """
    can.delete(*elementList)
    drawPoints()
    drawPolygon()
    #drawBezierCurve()
    draw_deboor()
    #script 285
    #knotvector = [x for x in range(0, len(pointList)+order+1)]


def coefficent(t):
	r = 0.0
	if(t < 0.0):
		t = -t
	if(t < 1.0):
		r = (3.0 * t * t * t -6.0 * t * t + 4.0) / 6.0
	elif(t < 2.0):
		r = -1.0 * (t - 2.0) * (t - 2.0) * (t - 2.0) / 6.0
	else:
		r = 0.0
	return r;

#def deboor(degree, controllPoints, knotvector, t):
	#Intervall T faengt an bei K-1 (Ordnung-1) bis Index des letzten Punktes
	#Grad ist die anzahl an Abschnitten die im Intervall gebildet werden koennen (Vernindung zwischen den Punkten)
	
#	return 0
    
def draw_deboor():
	x = 0.0
	y = 0.0   #Variablen fuer x- und y-Koordinaten
	dt = 1.0/100.0 #Abstand zwischen den Punkten auf der Linie
	c = 0.0
	k = 0.0
	if(M >= 1):
		t = -1.0
		while t < M:
			x = 0.0
			y = 0.0
			j = -2
			while j <= M+2.0:
				k = j
				if(k < 1):
					k = 1
				if(k > M):
					k = M
				c = coefficent(t - j)
				print c
				x += pointList[k][0] * c
				y += pointList[k][1] * c
				j += 1
			t += dt
			element = can.create_oval(x-1, y-1, x+1, y+1, fill=BCOLOR, outline=BCOLOR)
			elementList.append(element)
	i = 1
	while i <= M:
		element = can.create_oval(pointList[i][0]-2, pointList[i][1]-2, pointList[i][0]+2, pointList[i][1]+2, fill=CCOLOR, outline=CCOLOR)
		elementList.append(element)
		if(i != M):
			element = can.create_line(pointList[i][0], pointList[i][1], pointList[i+1][0], pointList[i+1][1], fill=CCOLOR)
			elementList.append(element)
		i += 1

def clearAll():
    """ clear all (point list and canvas) """
    can.delete(*elementList)
    del pointList[:]


def mouseEvent(event):
    """ process mouse events """
    global M
    print "left mouse button clicked at ", event.x, event.y
    pointList.append([event.x, event.y])
    M += 1
    draw()

if __name__ == "__main__":
    #check parameters
    if len(sys.argv) != 1:
       print "pointViewerTemplate.py"
       sys.exit(-1)
    # create main window
    mw = Tk()
    # create and position canvas and buttons
    cFr = Frame(mw, width=WIDTH, height=HEIGHT, relief="sunken", bd=1)
    cFr.pack(side="top")
    can = Canvas(cFr, width=WIDTH, height=HEIGHT)
    can.bind("<Button-1>",mouseEvent)
    can.pack()
    cFr = Frame(mw)
    cFr.pack(side="left")
    bClear = Button(cFr, text="Clear", command=clearAll)
    bClear.pack(side="left")
    eFr = Frame(mw)
    eFr.pack(side="right")
    bExit = Button(eFr, text="Quit", command=(lambda root=mw: quit(root)))
    bExit.pack()
    # start
    mw.mainloop()
    
