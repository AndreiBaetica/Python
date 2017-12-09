class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'

class Rectangle:
    def __init__(self,bl,tr,color='blue'):
        '''(Rectangle,Point,Point,str)->None'''
        self.bl=bl
        self.tr=tr
        self.color=color
    def get_bottom_left(self):
        '''(Rectangle)->Point'''
        return self.bl
    def get_top_right(self):
        '''(Rectangle)->Point'''
        return self.tr
    def get_color(self):
        '''(Rectangle)->str'''
        return self.color
    def reset_color(self, color):
        '''(rectangle)->None'''
        self.color=color
    def get_perimeter(self):
        '''(rectangle)->number'''
        length=self.tr.x-self.bl.x
        height=self.tr.y-self.bl.y
        return ((2*length)+(2*height))
    def get_area(self):
        '''(rectangle)->number'''
        length=self.tr.x-self.bl.x
        height=self.tr.y-self.bl.y
        return length*height
    def move(self,dx,dy):
        '''(rectangle)->number'''
        self.bl.move(dx,dy)
        self.tr.move(dx,dy)
    def intersects(self,rect):
        '''(Rectangle,Rectangle)->bool'''
        if (self.tr.x<rect.bl.x)or(rect.tr.x<self.bl.x)or(self.tr.y<rect.bl.y)or(rect.tr.y<self.bl.y):
            return False
        return True
    def contains(self,x,y):
        '''(Rectangle,number,number)->bool'''
        if (self.bl.x<=x<=self.tr.x) and (self.bl.y<=y<=self.tr.y):
            return True
        return False
    def __eq__(self,other):
        '''(Rectangle,Rectangle)->bool'''
        return self.bl==other.bl and self.tr==other.tr and self.color==other.color
    def __repr__(self):
        '''(Rectangle)->str'''
        return 'Rectangle('+str(self.bl)+','+str(self.tr)+",'"+self.color+"')"
    def __str__(self):
        '''(Rectangle)->str'''
        return 'I am a '+self.color+' rectangle with bottom left corner at ('+str(self.bl.x)+','+str(self.bl.y)+') and top right corner at ('+str(self.tr.x)+','+str(self.tr.y)+').'
    
class Canvas:
    def __init__(self):
        '''(Canvas)->None'''
        self.rlist=[]
    def add_one_rectangle(self,rect):
        '''(Canvas,Rectangle)->None'''
        self.rlist.append(rect)
    def count_same_color(self,color):
        '''(Canvas,str)->int'''
        count=0
        for i in self.rlist:
            if i.color==color:
                count+=1
        return count
    def total_perimeter(self):
        '''(Canvas)->number'''
        perimeter=0
        for i in self.rlist:
            perimeter=perimeter+i.get_perimeter()
        return perimeter
    def min_enclosing_rectangle(self):
        '''(Canvas)->Rectangle'''
        if self.rlist==[]:
            return None
        minx=self.rlist[0].bl.x
        maxx=self.rlist[0].tr.x
        miny=self.rlist[0].bl.y
        maxy=self.rlist[0].tr.y
        for i in self.rlist:
            if i.bl.x<minx:
                minx=i.bl.x
            if i.tr.x>maxx:
                maxx=i.tr.x
            if i.bl.y<miny:
                miny=i.bl.y
            if i.tr.y>maxy:
                maxy=i.tr.y
        return Rectangle(Point(minx,miny),Point(maxx,maxy))
    def common_point(self,point=Point()):
        '''(Canvas,Point)->bool'''
        for i in self.rlist:
            for j in self.rlist:
                if not (i.intersects(j)):
                     return False
        return True
    def __len__(self):
        '''(Canvas)->int'''
        return len(self.rlist)
    def __repr__(self):
        '''(Canvas)->str'''
        return 'Canvas('+str(self.rlist)+')'
