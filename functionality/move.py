
import elavator as e

global position_new
position_new=0


floor_number=[1,2,3,4,5,6,7,8,9,10]


def movement(position_new,command):

   
    if command in floor_number:
        if position_new >=command:
            print('Going Down')
            print(f'Now at:{position_new}')
            while position_new > command:
                
                if (position_new-1) == command:
                    break
                print(f'      :{position_new-1}')
                position_new-=1
                
               

            position_new=command
            
            
            print ("level :{}".format(position_new))
            
            
        elif (position_new)<=command:
            
            
            print('Going Up')
            print(f'Now at:{position_new}')
            while position_new < command:
                
                if (position_new+1) == command:
                    break
                print(f'      :{position_new+1}')
                position_new+=1
            position_new+=1
            print ("level :{}".format(position_new))
            
        
    else :
        print('Request denied!!!!')
    
    return position_new

