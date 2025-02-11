
from random import randint

def robot_goto(robot,target_x,target_y):
    
              robot_x,robot_y=robot.GetPosition()
              blue_base_x=target_x
              blue_base_y=target_y
              robot_x-=1
              robot_y+=1
                
              if (hasattr(robot, "local_time_2")==False):
                     setattr(robot, "local_time_2",0)
              if robot.local_time_2==0:
                     if (robot_x+1)<blue_base_x:
                            return 2
                     elif (robot_x+1)>blue_base_x:
                            return 4
                     elif (robot_y+1)<blue_base_y:
                            return 3
                     elif (robot_y+1)>blue_base_y:
                            return 1
                        
                     robot.local_time_2=1
                
              elif robot.local_time_2==1:
                     if (robot_y+1)<blue_base_y:
                            return 3
                     elif (robot_y+1)>blue_base_y:
                            return 1
                     elif (robot_x+1)<blue_base_x:
                            return 2
                     elif (robot_x+1)>blue_base_x:
                            return 4
                                
                     robot.local_time_2=0



def robot_investigate(robot):
        up=robot.investigate_up()
        down=robot.investigate_down()
        left=robot.investigate_left()
        right=robot.investigate_right()
        nw=robot.investigate_nw()
        ne=robot.investigate_ne()
        sw=robot.investigate_sw()
        se=robot.investigate_se()
        return (up,down,left,right,nw,ne,sw,se)

def robot_robodance(robot):
    if(robot.local_time_robodance==-1):
        robot.local_time_robodance=0
    if robot.local_time_robodance>=0:
                if(robot.local_time_robodance==0):
                        robot.local_time_robodance+=1
                        return 4
                elif(robot.local_time_robodance==1):
                        robot.local_time_robodance+=1
                        return 3
                elif(robot.local_time_robodance==2):
                        robot.local_time_robodance+=1
                        return 2       
                elif(robot.local_time_robodance==3):
                        robot.local_time_robodance+=1
                        return 2
                elif(robot.local_time_robodance==4):
                        robot.local_time_robodance+=1
                        return 1
                elif(robot.local_time_robodance==5):
                        robot.local_time_robodance+=1
                        return 1
                elif(robot.local_time_robodance==6):
                        robot.local_time_robodance+=1
                        return 4
                elif(robot.local_time_robodance==7):
                        robot.local_time_robodance+=1
                        return 4
                elif(robot.local_time_robodance==8):
                        robot.local_time_robodance+=1
                        return 3
                elif(robot.local_time_robodance==9):
                        robot.local_time_robodance=-1
                        return 2
    else:
        return randint(1,4)

def robot_baseattack(robot):
    investigate_tuple=robot_investigate(robot)
    v=robot.GetVirus()
    robot.DeployVirus(v)
    if(hasattr(robot,'blue_base_direction')==False):
                     setattr(robot,'blue_base_direction',"none")
                     if(investigate_tuple[0]=='enemy-base'):
                            robot.blue_base_direction='up'
                     elif(investigate_tuple[1]=='enemy-base'):
                            robot.blue_base_direction='down'
                     elif(investigate_tuple[2]=='enemy-base'):
                            robot.blue_base_direction='left'
                     elif(investigate_tuple[3]=='enemy-base'):
                            robot.blue_base_direction='right'
                     elif(investigate_tuple[4]=='enemy-base'):
                            robot.blue_base_direction='nw'
                     elif(investigate_tuple[5]=='enemy-base'):
                            robot.blue_base_direction='ne'
                     elif(investigate_tuple[6]=='enemy-base'):
                            robot.blue_base_direction='sw'
                     elif(investigate_tuple[7]=='enemy-base'):
                            robot.blue_base_direction='se'
                     if(hasattr(robot,'local_time_baseattack')==False):
                            setattr(robot,'local_time_baseattack',0)
                     else:
                            robot.local_time_baseattack=0
    elif(robot.blue_base_direction=='done'):
                     if(investigate_tuple[0]=='enemy-base'):
                            robot.blue_base_direction='up'
                     elif(investigate_tuple[1]=='enemy-base'):
                            robot.blue_base_direction='down'
                     elif(investigate_tuple[2]=='enemy-base'):
                            robot.blue_base_direction='left'
                     elif(investigate_tuple[3]=='enemy-base'):
                            robot.blue_base_direction='right'
                     elif(investigate_tuple[4]=='enemy-base'):
                            robot.blue_base_direction='nw'
                     elif(investigate_tuple[5]=='enemy-base'):
                            robot.blue_base_direction='ne'
                     elif(investigate_tuple[6]=='enemy-base'):
                            robot.blue_base_direction='sw'
                     elif(investigate_tuple[7]=='enemy-base'):
                            robot.blue_base_direction='se'
                     if(hasattr(robot,'local_time_baseattack')==False):
                            setattr(robot,'local_time_baseattack',0)
                     else:
                            robot.local_time_baseattack=0
    if(robot.blue_base_direction=='up'):
                     if(robot.local_time_baseattack==0):
                            robot.local_time_baseattack+=1
                            return 2
                     elif(robot.local_time_baseattack==1):
                            robot.local_time_baseattack+=1
                            return 1
                     elif(robot.local_time_baseattack==2):
                            robot.local_time_baseattack+=1
                            return 1
                     elif(robot.local_time_baseattack==3):
                            robot.local_time_baseattack+=1
                            return 4
                     elif(robot.local_time_baseattack==4):
                            robot.local_time_baseattack+=1
                            return 4
                     elif(robot.local_time_baseattack==5):
                            robot.local_time_baseattack+=1
                            return 3
                     elif(robot.local_time_baseattack==6):
                            robot.local_time_baseattack+=1
                            return 3
                     elif(robot.local_time_baseattack==7):
                            robot.blue_base_direction='done'
                            return 2
                     else:
                            return 0
    elif(robot.blue_base_direction=='down'):
                     if(robot.local_time_baseattack==0):
                            robot.local_time_baseattack+=1
                            return 2
                     elif(robot.local_time_baseattack==1):
                            robot.local_time_baseattack+=1
                            return 3
                     elif(robot.local_time_baseattack==2):
                            robot.local_time_baseattack+=1
                            return 3
                     elif(robot.local_time_baseattack==3):
                            robot.local_time_baseattack+=1
                            return 4
                     elif(robot.local_time_baseattack==4):
                            robot.local_time_baseattack+=1
                            return 4
                     elif(robot.local_time_baseattack==5):
                            robot.local_time_baseattack+=1
                            return 1
                     elif(robot.local_time_baseattack==6):
                            robot.local_time_baseattack+=1
                            return 1
                     elif(robot.local_time_baseattack==7):
                            robot.blue_base_direction='done'
                            return 2
                     else:
                            return 0
    elif(robot.blue_base_direction=='left'):
                     if(robot.local_time_baseattack==0):
                            robot.local_time_baseattack+=1
                            return 1
                     elif(robot.local_time_baseattack==1):
                            robot.local_time_baseattack+=1
                            return 4
                     elif(robot.local_time_baseattack==2):
                            robot.local_time_baseattack+=1
                            return 4
                     elif(robot.local_time_baseattack==3):
                            robot.local_time_baseattack+=1
                            return 3
                     elif(robot.local_time_baseattack==4):
                            robot.local_time_baseattack+=1
                            return 3
                     elif(robot.local_time_baseattack==5):
                            robot.local_time_baseattack+=1
                            return 2
                     elif(robot.local_time_baseattack==6):
                            robot.local_time_baseattack+=1
                            return 2
                     elif(robot.local_time_baseattack==7):
                            robot.blue_base_direction='done'
                            return 1
                     else:
                            return 0
    elif(robot.blue_base_direction=='right'):
                     if(robot.local_time_baseattack==0):
                            robot.local_time_baseattack+=1
                            return 1
                     elif(robot.local_time_baseattack==1):
                            robot.local_time_baseattack+=1
                            return 2
                     elif(robot.local_time_baseattack==2):
                            robot.local_time_baseattack+=1
                            return 2
                     elif(robot.local_time_baseattack==3):
                            robot.local_time_baseattack+=1
                            return 3
                     elif(robot.local_time_baseattack==4):
                            robot.local_time_baseattack+=1
                            return 3
                     elif(robot.local_time_baseattack==5):
                            robot.local_time_baseattack+=1
                            return 4
                     elif(robot.local_time_baseattack==6):
                            robot.local_time_baseattack+=1
                            return 4
                     elif(robot.local_time_baseattack==7):
                            robot.blue_base_direction='done'
                            return 1
                     else:
                            return 0
    elif(robot.blue_base_direction=='nw'):
                     if(robot.local_time_baseattack==0):
                            robot.local_time_baseattack+=1
                            return 1
                     elif(robot.local_time_baseattack==1):
                            robot.local_time_baseattack+=1
                            return 1
                     elif(robot.local_time_baseattack==2):
                            robot.local_time_baseattack+=1
                            return 4
                     elif(robot.local_time_baseattack==3):
                            robot.local_time_baseattack+=1
                            return 4
                     elif(robot.local_time_baseattack==4):
                            robot.local_time_baseattack+=1
                            return 3
                     elif(robot.local_time_baseattack==5):
                            robot.local_time_baseattack+=1
                            return 3
                     elif(robot.local_time_baseattack==6):
                            robot.local_time_baseattack+=1
                            return 2
                     elif(robot.local_time_baseattack==7):
                            robot.blue_base_direction='done'
                            return 2
                     else:
                            return 0
    elif(robot.blue_base_direction=='ne'):
                     if(robot.local_time_baseattack==0):
                            robot.local_time_baseattack+=1
                            return 1
                     elif(robot.local_time_baseattack==1):
                            robot.local_time_baseattack+=1
                            return 1
                     elif(robot.local_time_baseattack==2):
                            robot.local_time_baseattack+=1
                            return 2
                     elif(robot.local_time_baseattack==3):
                            robot.local_time_baseattack+=1
                            return 2
                     elif(robot.local_time_baseattack==4):
                            robot.local_time_baseattack+=1
                            return 3
                     elif(robot.local_time_baseattack==5):
                            robot.local_time_baseattack+=1
                            return 3
                     elif(robot.local_time_baseattack==6):
                            robot.local_time_baseattack+=1
                            return 4
                     elif(robot.local_time_baseattack==7):
                            robot.blue_base_direction='done'
                            return 4
                     else:
                            return 0
    elif(robot.blue_base_direction=='sw'):
                     if(robot.local_time_baseattack==0):
                            robot.local_time_baseattack+=1
                            return 3
                     elif(robot.local_time_baseattack==1):
                            robot.local_time_baseattack+=1
                            return 3
                     elif(robot.local_time_baseattack==2):
                            robot.local_time_baseattack+=1
                            return 4
                     elif(robot.local_time_baseattack==3):
                            robot.local_time_baseattack+=1
                            return 4
                     elif(robot.local_time_baseattack==4):
                            robot.local_time_baseattack+=1
                            return 1
                     elif(robot.local_time_baseattack==5):
                            robot.local_time_baseattack+=1
                            return 1
                     elif(robot.local_time_baseattack==6):
                            robot.local_time_baseattack+=1
                            return 2
                     elif(robot.local_time_baseattack==7):
                            robot.blue_base_direction='done'
                            return 2
                     else:
                            return 0
    elif(robot.blue_base_direction=='se'):
                     if(robot.local_time_baseattack==0):
                            robot.local_time_baseattack+=1
                            return 3
                     elif(robot.local_time_baseattack==1):
                            robot.local_time_baseattack+=1
                            return 3
                     elif(robot.local_time_baseattack==2):
                            robot.local_time_baseattack+=1
                            return 2
                     elif(robot.local_time_baseattack==3):
                            robot.local_time_baseattack+=1
                            return 2
                     elif(robot.local_time_baseattack==4):
                            robot.local_time_baseattack+=1
                            return 1
                     elif(robot.local_time_baseattack==5):
                            robot.local_time_baseattack+=1
                            return 1
                     elif(robot.local_time_baseattack==6):
                            robot.local_time_baseattack+=1
                            return 4
                     elif(robot.local_time_baseattack==7):
                            robot.blue_base_direction='done'
                            return 4
                     else:
                            return 0

def robot_collector(robot):
    
    
    
    if(hasattr(robot,'initial_var_collector')==False):
              setattr(robot,'initial_var_collector',0)
    robot_x,robot_y=robot.GetPosition()
    robot_x=robot_x+1
    robot_y=robot_y+1
    init_signal=robot.GetInitialSignal()
    robot_id,base_x_pos,base_y_pos,robot_no,base_x,base_y,canvas_x,canvas_y=init_signal.split(',')
       
    

    if(base_x_pos=='l'):
              if(robot_no=='1' or robot_no=='4'):
                     left_bound=1
                     right_bound=5
              elif(robot_no=='2' or robot_no=='5'):
                     left_bound=5
                     right_bound=10
              elif(robot_no=='3' or robot_no=='6'):
                     left_bound=10
                     right_bound=15
    elif(base_x_pos=='r'):
              if(robot_no=='1' or robot_no=='4'):
                     left_bound=int(canvas_x)-5
                     right_bound=int(canvas_x)-1
              elif(robot_no=='2' or robot_no=='5'):
                     left_bound=int(canvas_x)-10
                     right_bound=int(canvas_x)-5
              elif(robot_no=='3' or robot_no=='6'):
                     left_bound=int(canvas_x)-15
                     right_bound=int(canvas_x)-10
    elif(base_x_pos=='m'):
              if(robot_no=='1' or robot_no=='4'):
                     left_bound=1
                     right_bound=int(canvas_x)//3
              elif(robot_no=='2' or robot_no=='5'):
                     left_bound=int(canvas_x)//3
                     right_bound=int(canvas_x)*2//3
              elif(robot_no=='3' or robot_no=='6'):
                     left_bound=int(canvas_x)*2//3
                     right_bound=int(canvas_x)-1
    if(base_y_pos=='t'):
              if(robot_no=='1' or robot_no=='2' or robot_no=='3'):
                     upper_bound=1
                     lower_bound=7
              elif(robot_no=='4' or robot_no=='5' or robot_no=='6'):
                     upper_bound=7
                     lower_bound=14
              
    elif(base_y_pos=='b'):
              if(robot_no=='1' or robot_no=='2' or robot_no=='3'):
                     upper_bound=int(canvas_y)-7
                     lower_bound=int(canvas_y)-1
              elif(robot_no=='4' or robot_no=='5' or robot_no=='6'):
                     upper_bound=int(canvas_y)-14
                     lower_bound=int(canvas_y)-7
              
    elif(base_y_pos=='m'):
              if(robot_no=='1' or robot_no=='2' or robot_no=='3'):
                     upper_bound=1
                     lower_bound=int(canvas_y)//2
              elif(robot_no=='4' or robot_no=='5' or robot_no=='6'):
                     upper_bound=int(canvas_y)//2
                     lower_bound=int(canvas_y)-1
              
       
              
       
              
       
    if(robot_x==left_bound):
              robot.initial_var_collector=0
       #initialise the position to the bottom right corner
    if(robot.initial_var_collector==0):
              if(robot_x<right_bound):
                     return 2
              elif(robot_y<(lower_bound-1)):
                     return 3
              else:
                     robot.initial_var_collector=1
                     return 4
       #move up,left,down,left,repeat
    elif(robot.initial_var_collector==1):
              if(robot_y>upper_bound):
                     return 1
              else:
                     robot.initial_var_collector=2
                     return 4
    elif(robot.initial_var_collector==2):
              if(robot_y<(lower_bound-1)):
                     return 3
              else:
                     robot.initial_var_collector=1
                     return 4

def robot_defender(robot):
    robotx,roboty=robot.GetPosition()
    initial_code,basex,basey,posx,posy=robot.GetInitialSignal().split(',')
    
    
    if(posx=='right' and posy=='top'):
                     
                     if((robotx-int(basex))==2):
                            return 4
                     elif((int(basex)-robotx)==4):
                            return 2
                            
                     if((roboty-int(basey))==4):
                            return 1
                     elif((int(basey)-roboty)==2):
                            return 3
                     else:
                            return randint(1,4)
    elif(posx=='right' and posy=='bottom'):
                     if((robotx-int(basex))==2):
                            return 4
                     elif((int(basex)-robotx)==4):
                            return 2
                            
                     if((roboty-int(basey))==2):
                            return 1
                     elif((int(basey)-roboty)==4):
                            return 3
                     else:
                            return randint(1,4)
    elif(posx=='left' and posy=='top'):
                     if((robotx-int(basex))==4):
                            return 4
                     elif((int(basex)-robotx)==4):
                            return 2
                            
                     if((roboty-int(basey))==4):
                            return 1
                     elif((int(basey)-roboty)==2):
                            return 3
                     else:
                            return randint(1,4)
    elif(posx=='left' and posy=='bottom'):
                     if((robotx-int(basex))==4):
                            return 4
                     elif((int(basex)-robotx)==2):
                            return 2
                            
                     if((roboty-int(basey))==2):
                            return 1
                     elif((int(basey)-roboty)==4):
                            return 3
                     else:
                            return randint(1,4)
    elif(posx=='right' and posy=='middle'):
                     if((robotx-int(basex))==2):
                            return 4
                     elif((int(basex)-robotx)==4):
                            return 2
                            
                     if((roboty-int(basey))==4):
                            return 1
                     elif((int(basey)-roboty)==4):
                            return 3
                     else:
                            return randint(1,4)
    elif(posx=='left' and posy=='middle'):
                     if((robotx-int(basex))==4):
                            return 4
                     elif((int(basex)-robotx)==2):
                            return 2
                            
                     if((roboty-int(basey))==4):
                            return 1
                     elif((int(basey)-roboty)==4):
                            return 3
                     else:
                            return randint(1,4)
    elif(posx=='middle' and posy=='top'):
                     if((robotx-int(basex))==4):
                            return 4
                     elif((int(basex)-robotx)==4):
                            return 2
                            
                     if((roboty-int(basey))==4):
                            return 1
                     elif((int(basey)-roboty)==2):
                            return 3
                     else:
                            return randint(1,4)
    elif(posx=='middle' and posy=='bottom'):
                     if((robotx-int(basex))==4):
                            return 4
                     elif((int(basex)-robotx)==4):
                            return 2
                            
                     if((roboty-int(basey))==2):
                            return 1
                     elif((int(basey)-roboty)==4):
                            return 3
                     else:
                            return randint(1,4)

def robot_lineattack(robot):
    base_signal=robot.GetCurrentBaseSignal()
    
    initial_signal=robot.GetInitialSignal()
    robot_id,base_x_pos,base_y_pos,robot_no,line_no,base_x,base_y=initial_signal.split(',')
    base_x=int(base_x)+1
    base_y=int(base_y)+1
    robot_x,robot_y=robot.GetPosition()
    robot_x=int(robot_x)+1
    robot_y=int(robot_y)+1
    canvas_x=robot.GetDimensionX()
    canvas_y=robot.GetDimensionY()
    bluebase_y=canvas_y-(base_y-1)
    bluebase_x=canvas_x-(base_x-1)
    if(robot_x==1 or robot_x==canvas_x or robot_y==1 or robot_y==canvas_y or hasattr(robot,'temp_goto')==True):
           if(hasattr(robot,'temp_goto')==False):
                  setattr(robot,'temp_goto',0)
           return robot_goto(robot,bluebase_x,bluebase_y)
    

    robot_no=int(robot_no)
    if(base_x_pos=='l' and base_y_pos=='m'):
        if(line_no=='1'):
               target_x=int(base_x)+4
               target_y=int(base_y)+robot_no
        elif(line_no=='2'):
               target_x=int(base_x)+2
               target_y=int(base_y)+robot_no
        elif(line_no=='3'):
               target_x=int(base_x)+0
               target_y=int(base_y)+robot_no
        

    elif(base_x_pos=='r' and base_y_pos=='m'):
        if(line_no=='1'):
               target_x=int(base_x)-4
               target_y=int(base_y)+robot_no
        elif(line_no=='2'):
               target_x=int(base_x)-2
               target_y=int(base_y)+robot_no
        elif(line_no=='3'):
               target_x=int(base_x)-0
               target_y=int(base_y)+robot_no
    elif(base_x_pos=='m' and base_y_pos=='t'):
        if(line_no=='1'):
               target_x=int(base_x)+robot_no
               target_y=int(base_y)+4
        elif(line_no=='2'):
               target_x=int(base_x)+robot_no
               target_y=int(base_y)+2
        elif(line_no=='3'):
               target_x=int(base_x)+robot_no
               target_y=int(base_y)+0
        
    elif(base_x_pos=='m' and base_y_pos=='b'):
        if(line_no=='1'):
               target_x=int(base_x)+robot_no
               target_y=int(base_y)-4
        elif(line_no=='2'):
               target_x=int(base_x)+robot_no
               target_y=int(base_y)-2
        elif(line_no=='3'):
               target_x=int(base_x)+robot_no
               target_y=int(base_y)-0
    elif(base_x_pos=='l' and base_y_pos=='t'):
        if(line_no=='1'):
               target_x=int(base_x)+robot_no+4
               target_y=int(base_y)+robot_no+4
        elif(line_no=='2'):
               target_x=int(base_x)+robot_no+2
               target_y=int(base_y)+robot_no+2
        elif(line_no=='3'):
               target_x=int(base_x)+robot_no+0
               target_y=int(base_y)+robot_no+0
    elif(base_x_pos=='l' and base_y_pos=='b'):
        if(line_no=='1'):
               target_x=int(base_x)+robot_no+4
               target_y=int(base_y)-robot_no-4
        elif(line_no=='2'):
               target_x=int(base_x)+robot_no+2
               target_y=int(base_y)-robot_no-2
        elif(line_no=='3'):
               target_x=int(base_x)+robot_no+0
               target_y=int(base_y)-robot_no-0
    elif(base_x_pos=='r' and base_y_pos=='t'):
        if(line_no=='1'):
               target_x=int(base_x)+robot_no-4
               target_y=int(base_y)-robot_no+4
        elif(line_no=='2'):
               target_x=int(base_x)+robot_no-2
               target_y=int(base_y)-robot_no+2
        elif(line_no=='3'):
               target_x=int(base_x)+robot_no-0
               target_y=int(base_y)-robot_no+0
    elif(base_x_pos=='r' and base_y_pos=='b'):
        if(line_no=='1'):
               target_x=int(base_x)+robot_no-4
               target_y=int(base_y)-robot_no-4
        elif(line_no=='2'):
               target_x=int(base_x)+robot_no-2
               target_y=int(base_y)-robot_no-2
        elif(line_no=='3'):
               target_x=int(base_x)+robot_no-0
               target_y=int(base_y)-robot_no-0
    
    if(hasattr(robot,'target_X')==False):
        setattr(robot,'target_X',target_x)
        setattr(robot,'target_Y',target_y)
    
    if(base_signal=='1'):
        if(base_x_pos=='l' and base_y_pos=='m'):
            robot.target_X+=1
        elif(base_x_pos=='r' and base_y_pos=='m'):
            robot.target_X-=1
        elif(base_x_pos=='m' and base_y_pos=='t'):
            robot.target_Y+=1
        elif(base_x_pos=='m' and base_y_pos=='b'):
            robot.target_Y-=1
        elif(base_x_pos=='l' and base_y_pos=='t'):
            robot.target_X+=1
            robot.target_Y+=1
        elif(base_x_pos=='l' and base_y_pos=='b'):
            robot.target_X+=1
            robot.target_Y-=1
        elif(base_x_pos=='r' and base_y_pos=='t'):
            robot.target_X-=1
            robot.target_Y+=1
        elif(base_x_pos=='r' and base_y_pos=='b'):
            robot.target_X+=1
            robot.target_Y-=1
    

    return_var=robot_goto(robot,robot.target_X,robot.target_Y)
    
    return return_var

def robot_random(robot):
   
    
    return randint(1,4)

def ActRobot(robot):
    return_var=-1
    if('enemy-base' in robot_investigate(robot)):
        return_var=robot_baseattack(robot)
        return return_var

    if (hasattr(robot, 'local_time_robodance')==False):                
                setattr(robot, "local_time_robodance", -1)
    if('enemy' in robot_investigate(robot) or robot.local_time_robodance!=-1):
        if('enemy' in robot_investigate(robot)):
               robot.DeployVirus(robot.GetVirus())
        return_var=robot_robodance(robot)
        return return_var
    
    robot_id=robot.GetInitialSignal()[:1]

    if(robot_id=='R'):
        
        return_var=robot_random(robot)
        return return_var
    
    

    if(robot_id=='c'):
        return_var=robot_collector(robot)
        return return_var    

    if(robot_id=='D'):
        return_var=robot_defender(robot)
        return return_var

    if(robot_id=='A'):
        return_var=robot_lineattack(robot)
        return return_var

    


def get_bluebase_loc(base):
        x,y=base.GetPosition()
        canvas_x=base.GetDimensionX()
        canvas_y=base.GetDimensionY()
        bluebase_y=canvas_y-(y+1)
        bluebase_x=canvas_x-(x+1)
        return (bluebase_x,bluebase_y)

def base_create_collectors(base):
    init_str=''
    base_x,base_y=base.GetPosition()
    base_y=int(base_y)+1
    base_x=int(base_x)+1
       
       
    if(base_x<(base.GetDimensionX()/2)):
              init_str+='l'
    elif(base_x>(base.GetDimensionX()/2)):
              init_str+='r'
    else:
              init_str+='m'
    if(base_y<(base.GetDimensionY()/2)):
              init_str+=',t'
    elif(base_y>(base.GetDimensionX()/2)):
              init_str+=',b'
    else:
              init_str+=',m'
       
       
    base.create_robot('c'+','+init_str+','+'1'+','+str(base_x)+','+str(base_y)+','+str(base.GetDimensionX())+','+str(base.GetDimensionY()))
       
    base.create_robot('c'+','+init_str+','+'2'+','+str(base_x)+','+str(base_y)+','+str(base.GetDimensionX())+','+str(base.GetDimensionY()))
       
    base.create_robot('c'+','+init_str+','+'3'+','+str(base_x)+','+str(base_y)+','+str(base.GetDimensionX())+','+str(base.GetDimensionY()))
       
    base.create_robot('c'+','+init_str+','+'4'+','+str(base_x)+','+str(base_y)+','+str(base.GetDimensionX())+','+str(base.GetDimensionY()))
       
    base.create_robot('c'+','+init_str+','+'5'+','+str(base_x)+','+str(base_y)+','+str(base.GetDimensionX())+','+str(base.GetDimensionY()))
       
    base.create_robot('c'+','+init_str+','+'6'+','+str(base_x)+','+str(base_y)+','+str(base.GetDimensionX())+','+str(base.GetDimensionY()))    

def base_create_defenders(base):
    basex,basey=base.GetPosition()
    if(basex>(base.GetDimensionX()/2)):
              posx='right'
    elif(basex<(base.GetDimensionX()/2)):
              posx='left'
    else:
              posx='middle'
    if(basey>(base.GetDimensionY()/2)):
              posy='bottom'
    elif(basey<(base.GetDimensionY()/2)):
              posy='top'
    else:
              posy='middle'
       
    base.create_robot('D' + ','+ str(basex) + ',' + str(basey) + ',' + posx + ',' + posy)

def base_create_random(base):
    base_x,base_y=base.GetPosition()
    base_x=int(base_x)+1
    base_x=int(base_x)+1
    base.create_robot('R'+','+str(base_x)+','+str(base_y))

def base_create_attackers(base):
    init_str_x=''
    init_str_y=''
    base_x,base_y=base.GetPosition()
    base_y=int(base_y)+1
    base_x=int(base_x)+1
    blue_base_x,blue_base_y=get_bluebase_loc(base)
       
       
    if(base_x<(base.GetDimensionX()/2)):
        init_str_x='l'
    elif(base_x>(base.GetDimensionX()/2)):
        init_str_x='r'
    else:
        init_str_x='m'
    if(base_y<(base.GetDimensionY()/2)):
        init_str_y='t'
    elif(base_y>(base.GetDimensionX()/2)):
        init_str_y='b'
    else:
        init_str_y='m'
    
    #if(hasattr(base,'robot_no')==False):
     #   setattr(base,'robot_no',1)
    '''
    if(base.GetElixir()>=2000):
        base.create_robot(init_str_x+','+init_str_y+','+'1'+','+'1'+','+str(base_x)+','+str(base_y))
    elif(base.GetElixir()>=1950):
        base.create_robot(init_str_x+','+init_str_y+','+'2'+','+'1'+','+str(base_x)+','+str(base_y))
    elif(base.GetElixir()>=1900):
        base.create_robot(init_str_x+','+init_str_y+','+'4'+','+'1'+','+str(base_x)+','+str(base_y))
     '''
    
    for i in [1,3,5]:
              base.create_robot('A'+','+init_str_x+','+init_str_y+','+str(i)+','+'1'+','+str(base_x)+','+str(base_y))
              base.create_robot('A'+','+init_str_x+','+init_str_y+','+str(-i)+','+'1'+','+str(base_x)+','+str(base_y))
              #base.create_robot(init_str_x+','+init_str_y+','+str(i)+','+'2'+','+str(base_x)+','+str(base_y))
              #base.create_robot(init_str_x+','+init_str_y+','+str(-i)+','+'2'+','+str(base_x)+','+str(base_y)) 
              #base.create_robot(init_str_x+','+init_str_y+','+str(i)+','+'3'+','+str(base_x)+','+str(base_y))
              #base.create_robot(init_str_x+','+init_str_y+','+str(-i)+','+'3'+','+str(base_x)+','+str(base_y)) 
    base.create_robot('A'+','+init_str_x+','+init_str_y+','+'0'+','+'2'+','+str(base_x)+','+str(base_y))
         
    for i in [2,6]:
              base.create_robot('A'+','+init_str_x+','+init_str_y+','+str(i)+','+'2'+','+str(base_x)+','+str(base_y))
              base.create_robot('A'+','+init_str_x+','+init_str_y+','+str(-i)+','+'2'+','+str(base_x)+','+str(base_y))
    for i in [1,4,7]:
              base.create_robot('A'+','+init_str_x+','+init_str_y+','+str(i)+','+'3'+','+str(base_x)+','+str(base_y))
              base.create_robot('A'+','+init_str_x+','+init_str_y+','+str(-i)+','+'3'+','+str(base_x)+','+str(base_y)) 
    
    

def ActBase(base):
    if(base.GetElixir()==2000):
        
        base_create_collectors(base)
        for _ in range(1,10):
            base_create_defenders(base)
        for _ in range(1,8):
            base_create_random(base)
        
        base_create_attackers(base)
    
    if(hasattr(base,'global_temp_time_lineattack')==False):
        setattr(base,'global_temp_time_lineattack',0)
        setattr(base,'global_time_lineattack',0)
    base.SetYourSignal(str(base.global_time_lineattack))
    if(base.global_time_lineattack==1):
        base.global_time_lineattack=0
    if(base.global_temp_time_lineattack==0):
        base.global_temp_time_lineattack+=1
    elif(base.global_temp_time_lineattack==1):
        
        
        base.global_temp_time_lineattack=0
        base.global_time_lineattack=1
    return


