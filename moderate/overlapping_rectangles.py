import sys

class Rectangle(object):
    def __init__(self, ulx, uly, lrx, lry):
        self.ulx = ulx
        self.uly = uly
        self.lrx = lrx
        self.lry = lry
    
    @property
    def corners(self):
        points = []
        points.append((self.ulx, self.uly))
        points.append((self.ulx, self.lry))
        points.append((self.lrx, self.lry))
        points.append((self.lrx, self.uly))
        return points
    
    def is_in(self, x, y):
        # point is <x,y> cordinate (tuple)
        
        # check if x lies inside x domain
        if x >= self.ulx and x <= self.lrx:
            # check if it lies in the y domain
            if y >= self.lry and y <= self.uly:
                return True
        return False
        
if len(sys.argv) == 2:
    with open(sys.argv[1]) as reader:
        for line in reader:
            ulx1, uly1, lrx1, lry1, ulx2, uly2, lrx2, lry2 = line.split(",")
            rect1 = Rectangle(ulx1, uly1, lrx1, lry1)
            rect2 = Rectangle(ulx2, uly2, lrx2, lry2)
            p = False
            for point in rect2.corners:
                if rect1.is_in(point[0], point[1]):
                    p = True
            print p

if __name__ == "__main__":
    rect = Rectangle(-3,3,-1,1)
    rect2 = Rectangle(-2,4,2,2)
    for point in rect2.corners:
        print rect.is_in(point[0], point[1])