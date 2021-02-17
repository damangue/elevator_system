import move

def name_of_res():  
    print('Urban Oh "Shiiiit" ')



def floor_num():
    while True:
        k=input('Enter the number of your floor?')
        if k.isdigit() is True:
            command=int(k)
            return command
        else:
            print("Enter a valid floor!")


def print_sec_in_lift(position_new,command):
    
    if command<position_new:
        
        time=(position_new-command)*10
        print(f'{time}s :Now that was a fast ride')
    elif command>position_new:

        time=(command-position_new)*10
        print(f'{time}s :Now that was a fast ride')
    else:
        pass
    #return time
def RunGame():
    global position_new
    position_new=0
    name_of_res()
    while True:
        command=floor_num()
        temp_ps = position_new
        position_new = move.movement(position_new,command)
        print_sec_in_lift(temp_ps,command)
        
if __name__ == "__main__":
    RunGame()
    



