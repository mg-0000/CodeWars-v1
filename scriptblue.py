from random import randint , random, randrange, choice


def move_to_x(x1,x2):  #move towards x2 from x1 with biased randomness
        ratio = 0.25
        count = 1
        x = x1
        while x != x2 and count <200:
                if x2 - x1 > 0:
                        count += 1
                        number = random()
                        if number >= ratio:
                                x += 1 #move right
                                return 2
                        else:
                                x -= 1 #move left
                                return 4
                        
                elif x2 - x1 < 0:
                        count += 1
                        number = random()
                        if number <= ratio:
                                x += 1 #move right
                                return 2
                        else:
                                x -= 1 #move left
                                return 4
                        
                else:
                        return randint(1,4)
#        return randint(1,4)


def move_to_y(y1,y2):  #move towards y2 from y1 with biased randomness
        ratio = 0.25
        count = 1
        y = y1
        while y != y2 and count <200:
                if y2 - y1 > 0:
                        count += 1
                        number = random()
                        if number >= ratio:
                                y += 1 #move down
                                return 3
                        else:
                                y -= 1 #move up
                                return 1
                        
                elif y2 - y1 < 0:
                        count += 1
                        number = random()
                        if number <= ratio:
                                y += 1 #move down
                                return 3
                        else:
                                y -= 1 #move up
                                return 1
                        
                else: 
                        return randint(1,4)

#        return randint(1,4)

def move_to(x1,y1,x2,y2): #implement movement in x and y simultaneously with bias, to be called in ActRobot
        if x1 == x2:
                return move_to_x(x1,x2)
        elif y1 == y2:
                return move_to_y(y1,y2)
        else:
                dx = abs(x1-x2)
                dy = abs(y1-y2)
                
                ratio = dy/(dx + dy)
                number = random()
                if number <= ratio:
                        return move_to_y(y1,y2)
                else:
                        return move_to_x(x1,x2)
        

def in_zone(robot,x1,x2,y1,y2):  #check if robot is within a given zone
        x,y = robot.GetPosition()
        if x >= min(x1,x2) and x <= max(x1,x2) and y >= min(y1,y2) and y <= max(y1,y2):
                return True
        else:
                return False



        
                

                

                

def search(robot):
         up = robot.investigate_up()
         down = robot.investigate_down()
         left = robot.investigate_left()
         right = robot.investigate_right()
         ne = robot.investigate_ne()
         nw = robot.investigate_nw()
         se = robot.investigate_se()
         sw = robot.investigate_sw()
         l1=[up,down,left,right,ne,nw,se,sw]
         l2 = []
         l2.append(l1.count('blank'))
         l2.append(l1.count('friend'))
         l2.append(l1.count('friend-base'))
         l2.append(l1.count('enemy'))
         l2.append(l1.count('enemy-base'))
         return l2

        


def ActRobot(robot):
        
#        global x,y

        l = search(robot)
        a = l[3] #number of enemy robots around
        b = l[4] #number of enemy bases around ==1 or 0
        
        x,y = robot.GetPosition()

        if robot.GetElixir() < 10 and b == 1:
                sx = ''
                sy = ''
                if x < 10:
                        sx = sx + str(0)+str(x)
                if y < 10:
                        sy = sy + str(0)+str(y)
                if x >= 10:
                        sx = sx + str(x)
                if y >= 10:
                        sy = sy + str(y)
                robot.setSignal(sx+sy)
        

        signal = robot.GetInitialSignal()

        
        #return value according to signal

        if 'c' in signal:

                robot.DeployVirus(a*500 + b*robot.GetVirus()*.25)
                xa = int(signal[:2])
                xb = int(signal[2:4])
                ya = int(signal[4:6])
                yb = int(signal[6:8])
                
                while True:
                        x0 = choice([xa,xb])  #random destination in specific zone
                        y0 = choice([ya,yb])
                            #reach near position, then get new random position
                        if abs(x0-x) + abs(y0-y) <= 2:
                                break
                        return move_to(x,y,x0,y0)

        elif 'd' in signal:
                robot.DeployVirus(a*700 + b*robot.GetVirus()*.25)
                while True:
                        x0 = randint((X-5),(X+5))
                        y0 = randint((Y-5),(Y+5))
                        
                        if abs(x0-x) + abs(y0-y) <= 2:
                                break
                        return move_to(x,y,x0,y0)

        elif 'r' in signal:
                robot.DeployVirus(a*500 + b*robot.GetVirus()*.25)
                signal = robot.GetCurrentBaseSignal()
                if signal != '':

                        return move_to(x,y,signal[:2],signal[2:])
                while True:
                        x0 = choice([0,20,40])
                        y0 = choice([0,20,40])
                        
                        if abs(x0-x) + abs(y0-y) <= 4:
                                break
                        return move_to(x,y,x0,y0)

            
        


                         
                



       
        




def ActBase(base):
        #make base position globally accessible
        global X,Y
        X , Y = base.GetPosition()

        global X_d,Y_d     #dimensions of canvas
        X_d = base.GetDimensionX()
        Y_d = base.GetDimensionY()        
        n = 30
        while base.GetElixir() > 500 and n > 2:
                #create robots moving in fixed zones
                for i in range(0,X_d,int(X_d/2)):
                        for j in range(0,X_d,int(X_d/2)):
                                sx = ''
                                sy = ''
                                if i < 10:
                                        sx = sx + str(0)+str(i)+str(i+int(X_d/2))
                                if j < 10:
                                        sy=sy+str(0)+str(j)+str(j+int(Y_d/2))
                                if i >= 10:
                                        sx=sx+str(i)+str(i+int(X_d/2))
                                if j >= 10:
                                        sy=sy+str(j)+str(j+int(Y_d/2))
                                if in_zone(base,i,(i+int(X_d/2)),j,(j+int(Y_d/2))):
                                        for i in range(4):
                                                base.create_robot(sx+sy+'c')
                                                n -= 1
                                else:
                                         for i in range(6):
                                                base.create_robot(sx+sy+'c')
                                                n -= 1

                #create defenders
                for i in range(4):
                        base.create_robot('d')
                        n -= 1
                #create roamers
                for i in range(n):
                        base.create_robot('r')
                        n -= 1

                
                               
        l = search(base)
        a = l[3]  #number of enemy robots around
        b = l[4]  #enemy base around
        base.DeployVirus(a*800 + b*500)


        l = base.GetListOfSignals()
        if l != []:
                base.SetYourSignal(l[0])

                 