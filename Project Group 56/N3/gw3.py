import time

def maze_game(maze,row,col,key_row,key_col,door_row,door_col,key_row2,key_col2,door_row2,door_col2,key_row3,key_col3,door_row3,door_col3,escape_row,escape_col):
    print("Welcome to the maze game!")
    # variables
    # row=1
    # col=6
    inventory=[]
    # key_row=3
    # key_col=4
    # door_row=5
    # door_col=7
    # key_row2=0
    # key_col2=0
    # door_row2=0
    # door_col2=1
    # key_row3=0
    # key_col3=2
    # door_row3=0
    # door_col3=7

    # Timer starts here
    start_time = time.time()

    def printer():
        for rows in maze:
            print(''.join(rows))
    printer()

    while True:
        # player is at maze[1][6]
        
        # showing this every move
        print("Rules: 1. * is the escape, you must go there 2. you cant go over # 3. w= up s= down a= left d= right")
        movement=input("where do you want to move?:")
       
        # w system
        if movement == "w" and row > 0 and maze[row - 1][col] != "X" and maze[row - 1][col] != "/":  # Move up
            maze[row][col]=" "
            row -= 1
            maze[row][col]="O"
        # system
        # s system
        elif movement == "s" and row < len(maze) - 1 and maze[row + 1][col]!="X" and maze[row + 1][col]!="/":  
            maze[row][col] = " " 
            row += 1  
            maze[row][col] = "O" 
            # s system
       
       # d system
        elif movement == "d" and col<len(maze[row])-1 and maze[row][col+1]!= "X" and maze[row][col + 1] != "/":
            maze[row][col]= " "
            col+=1
            maze[row][col]="O"
        # d system

        # a system
        elif movement== "a" and col > 0 and maze[row][col-1] !="X" and maze[row][col - 1] != "/":
            maze[row][col]= " "
            col-=1
            maze[row][col]="O"
        # a system
        # game end
        if maze[row][col] == maze[escape_row][escape_col]: #18 22
            end_time = time.time()  # Stop the timer
            elapsed_time = end_time - start_time  # Calculate elapsed time
            print(f"Very Good! Now to the next level. Time taken: {elapsed_time:.2f} seconds")
            break  # End the game
        # Unlock the door and move through it
        # door unlocking system
        
        if maze[row][col]== maze[key_row][key_col]:
            inventory.append("key")
        if maze[row][col]== maze[key_row2][key_col2]:
            inventory.append("key2")
        if maze[row][col]== maze[key_row3][key_col3]:
            inventory.append("key3")
        
        
        if maze[row][col]== maze[door_row-1][door_col] or maze[row][col]==maze[door_row][door_col-1] and "key" in inventory:
            maze[row][col] = " "  
            maze[door_row][door_col]=" "
            print("You've unlocked the door!")
            inventory.remove("key")
            
        
        
        # for second door
        if maze[row][col]== maze[door_row2-1][door_col2] or maze[row][col]==maze[door_row2][door_col2-1] and "key" in inventory:
            maze[row][col] = " "  
            maze[door_row2][door_col2]=" "
            print("You've unlocked the door!")
            inventory.remove("key2")
            
        
        
        # for third door
        if maze[row][col]== maze[door_row3-1][door_col3] or maze[row][col]==maze[door_row3][door_col3-1]:
            maze[row][col] = " "  
            maze[door_row3][door_col3]=" "
            print("You've unlocked the door!")
            inventory.remove("key3")
            
                
        
        printer()

maze1=[ 
        ["X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X"],
        ["X"," "," "," "," "," ","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","X"],
        ["X"," "," ","X","X","X","X","X","X","X","X"," "," ","X","X","X","X","X","X","X","X"," "," ","X"], 
        ["X"," "," ","X","^"," "," "," "," "," "," "," "," "," "," ","X"," "," "," "," "," "," "," ","X"],
        ["X"," "," ","X"," "," "," "," ","X","X","X","X","X","X","X"," "," "," ","X","X","X","X","X","X"],
        ["X"," "," ","X"," "," "," ","/"," "," "," "," "," "," "," "," ","X"," "," "," "," "," "," ","X"],
        ["X"," "," ","X","X","X","X","X","X"," "," ","X","X","X","X","X","X","X","X"," "," "," "," ","X"],
        ["X"," "," "," "," "," ","X"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","X"," ","X"],
        ["X","X","X","X","X"," ","X","X","X","X","X","X","X","X","X","X","X","X"," "," "," "," "," ","X"],                                
        ["X"," "," ","X"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","X","X","X"],                
        ["X"," "," ","X"," "," "," "," ","X","X","X","X","X","X","X","X","X","X"," ","X"," "," "," ","X"],                               
        ["X"," "," ","X"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","X"],                                 
        ["X","/","X","X","X","X","X","X","X","X"," "," ","X","X","X","X","X","X","X"," "," "," "," ","X"],
        ["X"," "," ","X"," "," "," "," "," "," "," "," ","X"," "," "," "," "," "," "," "," "," "," ","X"],                              
        ["X"," "," "," "," "," ","/","X","X","X","X","X"," ","X","X","X","X"," "," "," ","X"," "," ","X"],   
        ["X","X","X","X","X","X"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","X"," "," ","X"],   
        ["X"," "," "," "," "," "," "," "," ","/","X","X","X","X","X","X","X","X","X","X","X"," "," ","X"],                                
        ["X"," "," "," "," ","X","X","X","X"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","X"],                                   
        ["X"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"," "],                    
        ["X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X"]]
maze2=  [["X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X"],
         ["X","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","X"],
         ["X"," "," ","X","X","X","X","X","X","X"," "," ","X","X","X","X","X","X","X","X","X","X"," "," ","X"],
         ["X"," "," ","X"," "," "," "," "," "," "," "," "," "," "," ","X"," "," "," "," "," "," "," "," ","X"],
         ["X"," "," ","X"," "," "," "," ","X","X","X","X","X","X"," ","X"," "," "," ","X","X","X","X","X","X"],
         ["X"," "," ","X"," "," "," "," ","X"," "," "," "," "," "," "," "," "," ","X"," "," "," "," "," ","X"], 
         ["X"," "," ","X","X","X","X","X","X"," ","^"," ","X","X","X","X","X","X","X","X"," "," ","X"," ","X"],                          
         ["X"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","X"," "," "," ","X"],
         ["X","X","X","X","X"," ","X","X","X","X","X","X","X","X","X","X","X","X"," "," ","X"," "," "," ","X"],                            
         ["X"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","X"," "," "," ","X"],
         ["X"," "," ","X"," "," "," "," ","X","X","X","X","X","X","X","X","X","X"," ","X"," "," "," ","X","X"],                        
         ["X"," "," ","X"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","X"],   
         ["X"," "," ","X","X","X","X","X","X","X","X","X","X","/","X","X","X","X","X","X","X"," "," ","X","X"],                        
         ["X"," "," ","X"," "," "," "," "," "," "," "," ","X"," "," "," "," "," "," "," "," ","X","X"," ","X"],
         ["X"," "," "," "," "," ","X","X","X","X","X","X"," ","X","X","X","X"," ","X"," "," "," ","X"," ","X"],                        
         ["X","X","X","X","X","X"," ","X"," "," "," "," "," "," "," "," "," "," "," "," "," ","X"," "," ","X"],
         ["X"," "," "," "," "," "," "," "," "," "," "," "," ","X","X","X","X","X","X","X","X","X"," "," ","X"],
         ["X","X","X","X","X","X","X","X","X","X","X"," "," "," "," "," "," "," "," "," "," "," "," "," ","X"],
         ["X"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"]]
    
maze_game(maze2,1,1,6,10,12,13,0,0,0,0,0,0,0,0,18,24)
maze_game(maze1,1,6,3,4,5,7,0,0,0,0,0,0,0,0,18,22)