v=0
k=0
def setup():
    size(1000,1000)
def draw():
    global v,k
    background(111)
    rect(450,0,100,100)
    rect(450,900,100,100)
    rect(0,450,100,100)
    rect(900,450,100,100)
    ellipse(v,k,60,60)
    if mousePressed == True:
        if mouseX > 450 and mouseX < 550 and mouseY > 0 and mouseY < 100:
            k=k-1
        if mouseX > 450 and mouseX < 550 and mouseY > 900 and mouseY < 1000:
            k=k+1
        if mouseX > 0 and mouseX < 100 and mouseY > 450 and mouseY < 550:
            v=v-1
        if mouseX > 900 and mouseX < 1000 and mouseY > 450 and mouseY < 550:
            v=v+1
