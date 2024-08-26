import turtle as tt
import time
def instruct():
    st.clear()
    inst = tt.Turtle()
    inst.speed(0)
    inst.penup()
    inst.hideturtle()
    inst.pendown()
    inst.write("Welcome to this game demo.here are the basic rules for the game you should know before playing :",align="center",font=("Courier",10,"bold"))
    inst.penup()
    inst.goto(0,-20)
    inst.pendown()
    inst.write("1. Prevent the ball to pass through your paddle.",align="center",font=("Courier",10,"bold"))
    inst.penup()
    inst.goto(0,-40)
    inst.pendown()
    inst.write("2.The player who will reach the require score will win.",align="center",font=("Courier",10,"bold"))
    inst.penup()
    inst.goto(0,-60)
    inst.pendown()
    inst.write("3.Player A: Up->w Down->s  ",align="center",font=("Courier",10,"bold"))
    inst.penup()
    inst.goto(0,-80)
    inst.pendown()
    inst.write("4.Player B: Up->up arrow Down->down arrow",align="center",font=("Courier",10,"bold"))
    inst.penup()
    inst.goto(0,-310)
    inst.pendown()
    inst.write("Press k to start",align="center",font=("Courier",10,"bold"))
    
def start():
    #screen boundary
    screen.clear()

    bound = tt.Turtle()
    bound.shape("turtle")
    bound.pencolor('black')
    bound.penup()
    bound.goto(-498,290)
    bound.pendown()
    for i in range(2):
        bound.fd(980)
        bound.rt(90)
        bound.fd(580)
        bound.rt(90)
    bound.hideturtle()    


    #paddle1 -->left side
    paddle1 = tt.Turtle()
    paddle1.speed(0)
    paddle1.shape("square")
    paddle1.color('orange')
    paddle1.pencolor('white')
    paddle1.shapesize(stretch_wid=6,stretch_len=2)
    paddle1.penup()
    paddle1.goto(-400,0)
    paddle1.pendown()

    #paddle2 -->right side
    paddle2 = tt.Turtle()
    paddle2.speed(0)
    paddle2.shape("square")
    paddle2.color('green')
    paddle2.pencolor('white')
    paddle2.shapesize(stretch_wid=6,stretch_len=2)
    paddle2.penup()
    paddle2.goto(400,0)
    paddle2.pendown()

    #ball turtle
    ball = tt.Turtle()
    ball.color('navy')
    ball.pencolor('white')
    ball.shape('circle')
    ball.speed(0)
    ball.penup()
    ball.goto(0,0)
    ball.pendown()
    #setting dx and dy that decides the speed of ball
    ball.dx = 2
    ball.dy = -2

    #starting the scores of players
    playerA = 0 
    playerB = 0

    #displaying the score
    score = tt.Turtle()
    score.speed(0)
    score.penup()
    score.hideturtle()
    score.goto(0,290)
    score.pendown()
    score.write("Player A:0 Player B:0",align="center",font=("Courier",20,"bold"))

    #target score
    target = 2
    targ = tt.Turtle()
    targ.speed(0)
    targ.penup()
    targ.hideturtle()
    targ.goto(420,290)
    targ.pendown()
    targ.write("Target :{}".format(target),align='center',font=("Courier",20,"bold"))
            

    #instructions for playing
    inst = tt.Turtle()
    inst.speed(0)
    inst.penup()
    inst.hideturtle()
    inst.goto(0,-310)
    inst.pendown()
    inst.write("Player A: Up->w Down->s | Player B: Up->up arrow Down->down arrow",align="center",font=("Courier",10,"bold"))

    def starting(x,y):
        screen.clearscreen()
        start()
    def exitting(x,y):
        screen.bye()
    # #buttons for restart and quit
    def restarting():
        restart = tt.Turtle()
        restart.speed(0)
        restart.pencolor('black')
        restart.penup()
        restart.goto(-100,0)
        restart.pendown()
        restart.write("Restart",align="center",font=("Courier",25,"bold"))
        restart.showturtle()  
        restart.onclick(starting)

    def quitting():
        leave = tt.Turtle()
        leave.speed(0)
        leave.pencolor('black')
        leave.penup()
        leave.goto(100,0)
        leave.pendown()
        leave.write("Quit",align="center",font=("Courier",25,"bold"))
        leave.showturtle()
        leave.onclick(exitting)    
    #instruction for pause and play
    global is_paused 
    is_paused = False
    
    #function for pause and play
    def pauseandplay():
        global is_paused
        if(is_paused==False):
            restarting()
            quitting()
            is_paused = True
        elif(is_paused==True):
            is_paused=False    
               
    #Moving of paddles functions
    def movePad1Up():
        if(paddle1.ycor()+60<290):
            y = paddle1.ycor()
            y += 10
            paddle1.sety(y)

    def movePad1Down():
        if(paddle1.ycor()-60>-290):
            y = paddle1.ycor()
            y -= 10
            paddle1.sety(y)

    def movePad2Up():
        if(paddle2.ycor()+60<290):
            y = paddle2.ycor()
            y += 10
            paddle2.sety(y)
        
    def movePad2Down():
        if(paddle2.ycor()-60>-290):
            y = paddle2.ycor()
            y -= 10
            paddle2.sety(y)  
            
  
    #Matching the above functions to keys
    screen.listen()
    screen.onkeypress(movePad1Up,"w")
    screen.onkeypress(movePad1Down,"s")
    screen.onkeypress(movePad2Up,"Up")
    screen.onkeypress(movePad2Down,"Down")
    screen.onkeypress(pauseandplay,"space")
            
    while True:
        if not is_paused:
            screen.update()
            #moving ball using changing of frames
            ball.setx(ball.xcor()+ball.dx)
            ball.sety(ball.ycor()+ball.dy)
            
            
            #checking if ball hit above screen or not
            if ball.ycor() > 280:
                ball.sety(280)
                ball.dy *= -1 #bouncing back the ball
                
            #checking if ball hit bottom screen or not
            if ball.ycor() < -280:
                ball.sety(-280)
                ball.dy *= -1 #bouncing back the ball    
            
            #checking if ball hits wall on left or right side or not
            if ball.xcor() < -480 or ball.xcor() > 480:
                if ball.xcor() < -480:
                    playerB += 1 
                    #increasing score of right player as left player missed the ball
                    
                if ball.xcor() > 480:
                    playerA += 1 
                    #increasing score of left player as right player missed the ball
                
                #now ball will again start from center(0,0)
                ball.penup()
                ball.goto(0,0)
                ball.pendown()
                ball.dx *= -1
                ball.dy *= -1
                
                #updating scoreboard
                score.clear()
                score.write("Player A: {} Player B: {}".format(playerA,playerB),align="center",font=("Courier",20,"bold"))
                
            #checking ki kya left wale ne ball mari h ya nhi
            if (ball.xcor() < -370 and ball.xcor() > -380 ) and(paddle1.ycor()+60 > ball.ycor() > paddle1.ycor()-60):
                ball.dx *= -1 #bounce the ball back
                
                playerA += 1
                score.clear()
                score.write("Player A: {} Player B: {}".format(playerA,playerB),align="center",font=("Courier",20,"bold"))
                
                #increasing the speed of ball (limit 5)
                if(ball.dy > 0 and ball.dy < 5):
                    ball.dy+=0.5
                elif(ball.dy < 0 and ball.dy > -5):
                    ball.dx-=0.5
                    
                if(ball.dx > 0 and ball.dx < 5):
                    ball.dx += 0.5
                elif(ball.dx < 0 and ball.dx > -5):
                    ball.dx -= 0.5
                        
            
            #checking if right wale ne ball mari h ya nhi
            if (ball.xcor() > 370 and ball.xcor() < 380) and (paddle2.ycor()+60 > ball.ycor() > paddle2.ycor()-60):
                ball.dx *= -1  
                
                playerB += 1
                score.clear()
                score.write("Player A: {} Player B: {}".format(playerA,playerB),align="center",font=("Courier",20,"bold"))
                
                #increasing the speed of ball (limit 7)
                if(ball.dy > 0 and ball.dy < 7):
                    ball.dy += 1
                elif(ball.dy < 0 and ball.dy > -7):
                    ball.dy -= 1   
                
                if(ball.dx > 0 and ball.dx < 7):
                    ball.dx += 1
                elif(ball.dx < 0 and ball.dx > -7):
                    ball.dx -= 1
                    
            #Checking if Target get achived or not by any of Two Players
            
            if playerA== target or playerB == target:
                result = tt.Turtle()
                result.speed(0)
                result.penup()
                result.goto(0,100)
                result.pendown()
                result.hideturtle()
                
                screen.clearscreen()
                if playerA==target and playerB==target:
                    result.write("Draw rha!!",align="center",font=("Courier",20,"bold"))
                elif playerA==target:
                    result.write("Player A ko badhai HO!!",align="center",font=("Courier",20,"bold"))
                elif playerB==target:
                    result.write("Player B ko badhai HO!!",align="center",font=("Courier",20,"bold"))        
                  
                restarting()
                quitting()    
                break
        else:
            screen.update()        

            
        
 #screen turtle
screen = tt.Screen()
screen.title("Pong Game")
screen.setup(width=1050,height=650)

st=tt.Turtle()
st.speed(0)
st.hideturtle() 
st.write("PRESS ENTER TO START",align="center",font=("Courier",20,"bold"))

screen.listen()
screen.onkeypress(instruct,"Return")
screen.onkeypress(start,"k")

tt.mainloop()




   


                   
              
      
        
                                     