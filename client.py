import socket 
import threading

from tkinter import *
from tkinter import messagebox


window = Tk()

cell = ""
turn = False;

host = '127.0.0.1'
port = 8080



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host , port))




def update():
    if cell =='A':
        clicked1()
    elif cell =='B':
        clicked2()
    elif cell =='C':
        clicked3()
    elif cell =='D':
        clicked4()
    elif cell =='E':
        clicked5()
    elif cell =='F':
        clicked6()
    elif cell =='G':
        clicked7()
    elif cell =='H':
        clicked8()
    elif cell =='I':
        clicked9()
    elif cell =='J':
        clicked10() 
    elif cell =='K':
        clicked11()  
    elif cell =='L':
        clicked12()  
    elif cell =='M':
        clicked13()  
    elif cell =='N':
        clicked14()  
    elif cell =='O':
        clicked15()  
    elif cell =='P':
        clicked16()  
    elif cell =='Q':
        clicked17()  
    elif cell =='R':
        clicked18()  
    elif cell =='S':
        clicked19()  
    elif cell =='T':
        clicked20()  
    elif cell =='U':
        clicked21()  
    elif cell =='V':
        clicked22()  
    elif cell =='W':
        clicked23()  
    elif cell =='X':
        clicked24()  
    elif cell =='Y':
        clicked25() 
    else:
        print("No Match") 








def createThread (targett):
   thread = threading.Thread(target = targett)
   thread.daemon = True
   thread.start()

def receiveData():
    global cell
    global turn   
    while True:
        data, addr = sock.recvfrom(1024)
        data2 = data.decode()
        dataa = data2.split('-')
        cell = dataa[0]
        update()
        if dataa[1]=='Your Turn':
            print(cell + "Client turn")
            turn = True
            print("Client turn = "+str(turn))


createThread(receiveData)

window.title("Welcome Player 2 to Tic-Tak-Toe")


host = '127.0.0.2'
port = 8080

lbl=Label(window,text="TIC-TAK-TOE GAME",font=('Helvetica','15'))
lbl.grid(row=0,column=0)
lbl=Label(window,text="Player 1 : X",font=('Helvetica','10'))
lbl.grid(row=1,column=0)
lbl=Label(window,text="Player 2 : O",font=('Helvetica','10'))
lbl.grid(row=2,column=0)



print(cell)
print("Client turn = "+str(turn))


def clicked1():
    global turn
    global cell
    if turn and btn1["text"]==" ":
         btn1["text"]="O"
         send_data = '{}-{}'.format('A','Your Turn').encode()
         sock.send(send_data)
         print(send_data)
         turn = False
         check()
    elif turn == False and btn1["text"]==" " and cell =="A":
        btn1["text"]=="X"
        turn =  True
        check()


def clicked2():
    global turn
    global cell
    if turn and btn2["text"]==" ":
         btn2["text"]="O"
         send_data = '{}-{}'.format('B','Your Turn').encode()
         sock.send(send_data)
         print(send_data)
         turn = False
         check()
    elif turn == False and btn2["text"]==" " and cell =="B":
        btn2["text"]=="X"
        turn = True  
        check()

def clicked3():
    global turn
    global cell
    if turn  and btn3["text"]==" ":
         btn3["text"]="O"
         send_data = '{}-{}'.format('C','Your Turn').encode()
         sock.send(send_data)
         print(send_data)
         turn = False
         check()
    elif turn == False and btn3["text"]==" " and cell =="C":
        btn3["text"]=="X"
        turn = True  
        check()

def clicked4():
    global turn
    global cell
    if turn and btn4["text"]==" ":
         btn4["text"]="O"
         send_data = '{}-{}'.format('D','Your Turn').encode()
         sock.send(send_data)
         print(send_data)
         turn = False
         check()
    elif turn == False and btn4["text"]==" " and cell =="D":
        btn4["text"]=="X"
        turn = True 
        check()

def clicked5():
    global turn
    global cell
    if turn and btn5["text"]==" ":
         btn5["text"]="O"
         send_data = '{}-{}'.format('E','Your Turn').encode()
         sock.send(send_data)
         print(send_data)
         turn = False
         check()
    elif turn == False and btn5["text"]==" " and cell =="E":
        btn5["text"]=="X"
        turn = True 
        check()

def clicked6():
    global turn
    global cell
    if turn and btn6["text"]==" ":
         btn6["text"]="O"
         send_data = '{}-{}'.format('F','Your Turn').encode()
         sock.send(send_data)
         print(send_data)
         turn = False
         check()
    elif turn == False and btn6["text"]==" " and cell =="F":
        btn6["text"]=="X"
        turn = True 
        check()

def clicked7():
    global turn
    global cell
    if turn and btn7["text"]==" ":
         btn7["text"]="O"
         send_data = '{}-{}'.format('G','Your Turn').encode()
         sock.send(send_data)
         print(send_data)
         turn = False
         check()
    elif turn == False and btn7["text"]==" " and cell =="G":
        btn7["text"]=="X"
        turn = True  
        check()

def clicked8():
    global turn
    global cell
    if turn  and btn8["text"]==" ":
         btn8["text"]="O"
         send_data = '{}-{}'.format('H','Your Turn').encode()
         sock.send(send_data)
         print(send_data)
         turn = False
         check()
    elif turn == False and btn8["text"]==" " and cell =="H":
        btn8["text"]=="X"
        turn = True  
        check()

def clicked9():
    global turn
    global cell
    if turn and btn9["text"]==" ":
         btn9["text"]="O"
         send_data = '{}-{}'.format('I','Your Turn').encode()
         sock.send(send_data)
         print(send_data)
         turn = False
         check()
    elif turn == False and btn9["text"]==" " and cell =="I":
        btn9["text"]=="X"
        turn = True 
        check()

def clicked10():
    global turn
    global cell
    if turn  and btn10["text"]==" ":
         btn10["text"]="O"
         send_data = '{}-{}'.format('J','Your Turn').encode()
         sock.send(send_data)
         print(send_data)
         turn = False
         check()
    elif turn == False and btn10["text"]==" " and cell =="J":
        btn10["text"]=="X"
        turn = True 
        check()

def clicked11():
    global turn
    global cell
    if turn and btn11["text"]==" ":
         btn11["text"]="O"
         send_data = '{}-{}'.format('K','Your Turn').encode()
         sock.send(send_data)
         print(send_data)
         turn = False
         check()
    elif turn == False and btn11["text"]==" " and cell =="K":
        btn11["text"]=="X"
        turn = True 
        check()

def clicked12():
    global turn
    global cell
    if turn  and btn12["text"]==" ":
         btn12["text"]="O"
         send_data = '{}-{}'.format('L','Your Turn').encode()
         sock.send(send_data)
         print(send_data)
         turn = False
         check()
    elif turn == False and btn12["text"]==" " and cell =="L":
        btn12["text"]=="X"
        turn = True  
        check()

def clicked13():
    global turn
    global cell
    if turn  and btn13["text"]==" ":
         btn13["text"]="O"
         send_data = '{}-{}'.format('M','Your Turn').encode()
         sock.send(send_data)
         print(send_data)
         turn = False
         check()
    elif turn == False and btn13["text"]==" " and cell =="M":
        btn13["text"]=="X"
        turn = True 
        check()

def clicked14():
    global turn
    global cell
    if turn and btn14["text"]==" ":
         btn14["text"]="O"
         send_data = '{}-{}'.format('N','Your Turn').encode()
         sock.send(send_data)
         print(send_data)
         turn = False
         check()
    elif turn == False and btn14["text"]==" " and cell =="N":
        btn14["text"]=="X"
        turn = True 
        check()

def clicked15():
    global turn
    global cell
    if turn  and btn15["text"]==" ":
         btn15["text"]="O"
         send_data = '{}-{}'.format('O','Your Turn').encode()
         sock.send(send_data)
         print(send_data)
         turn = False
         check()
    elif turn == False and btn15["text"]==" " and cell =="O":
        btn15["text"]=="X"
        turn =  True  
        check()

def clicked16():
    global turn
    global cell
    if turn  and btn16["text"]==" ":
         btn16["text"]="O"
         send_data = '{}-{}'.format('P','Your Turn').encode()
         sock.send(send_data)
         print(send_data)
         turn = False
         check()
    elif turn == False and btn16["text"]==" " and cell =="P":
        btn16["text"]=="X"
        turn = True 
        check()

def clicked17():
    global turn
    global cell
    if turn and btn17["text"]==" ":
         btn17["text"]="O"
         send_data = '{}-{}'.format('Q','Your Turn').encode()
         sock.send(send_data)
         print(send_data)
         turn = False
         check()
    elif turn == False and btn17["text"]==" " and cell =="Q":
        btn17["text"]=="X"
        turn = True  
        check()

def clicked18():
    global turn
    global cell
    if turn  and btn18["text"]==" ":
         btn18["text"]="O"
         send_data = '{}-{}'.format('R','Your Turn').encode()
         sock.send(send_data)
         print(send_data)
         turn = False
         check()
    elif turn == False and btn18["text"]==" " and cell =="R":
        btn18["text"]=="X"
        turn = True 
        check()

def clicked19():
    global turn
    global cell
    if turn and btn19["text"]==" ":
         btn19["text"]="O"
         send_data = '{}-{}'.format('S','Your Turn').encode()
         sock.send(send_data)
         print(send_data)
         turn = False
         check()
    elif turn == False and btn19["text"]==" " and cell =="S":
        btn19["text"]=="X"
        turn = True  
        check()

def clicked20():
    global turn
    global cell
    if turn and btn20["text"]==" ":
         btn20["text"]="O"
         send_data = '{}-{}'.format('T','Your Turn').encode()
         sock.send(send_data)
         print(send_data)
         turn = False
         check()
    elif turn == False and btn20["text"]==" " and cell =="T":
        btn20["text"]=="X"
        turn = True 
        check()

def clicked21():
    global turn
    global cell
    if turn and btn21["text"]==" ":
         btn21["text"]="O"
         send_data = '{}-{}'.format('U','Your Turn').encode()
         sock.send(send_data)
         print(send_data)
         turn = False
         check()
    elif turn == False and btn21["text"]==" " and cell =="U":
        btn21["text"]=="X"
        turn = True  
        check()

def clicked22():
    global turn
    global cell
    if turn and btn22["text"]==" ":
         btn22["text"]="O"
         send_data = '{}-{}'.format('V','Your Turn').encode()
         sock.send(send_data)
         print(send_data)
         turn = False
         check()
    elif turn == False and btn22["text"]==" " and cell =="V":
        btn22["text"]=="X"
        turn = True 
        check()

def clicked23():
    global turn
    global cell
    if turn and btn23["text"]==" ":
         btn23["text"]="O"
         send_data = '{}-{}'.format('W','Your Turn').encode()
         sock.send(send_data)
         print(send_data)
         turn = False
         check()
    elif turn == False and btn23["text"]==" " and cell =="W":
        btn23["text"]=="X"
        turn = True  
        check()

def clicked24():
    global turn
    global cell
    if turn and btn24["text"]==" ":
         btn24["text"]="O"
         send_data = '{}-{}'.format('X','Your Turn').encode()
         sock.send(send_data)
         print(send_data)
         turn = False
         check()
    elif turn == False and btn24["text"]==" " and cell =="X":
        btn24["text"]=="X"
        turn = True  
        check()

def clicked25():
    global turn
    global cell
    if turn and btn25["text"]==" ":
         btn25["text"]="O"
         send_data = '{}-{}'.format('Y','Your Turn').encode()
         sock.send(send_data)
         print(send_data)
         turn = False
         check()
    elif turn == False and btn25["text"]==" " and cell =="Y":
        btn25["text"]=="X"
        turn = True 
        check()



count = 1
def check():
    global count
    b1 = btn1["text"]
    b2 = btn2["text"]
    b3 = btn3["text"]
    b4 = btn4["text"]
    b5 = btn5["text"]
    b6 = btn6["text"]
    b7 = btn7["text"]
    b8 = btn8["text"]
    b9 = btn9["text"]
    b10 = btn10["text"]
    b11 = btn11["text"]
    b12 = btn12["text"]
    b13 = btn13["text"]
    b14 = btn14["text"]
    b15 = btn15["text"]
    b16 = btn16["text"]
    b17 = btn17["text"]
    b18 = btn18["text"]
    b19 = btn19["text"]
    b20 = btn20["text"]
    b21 = btn21["text"]
    b22 = btn22["text"]
    b23 = btn23["text"]
    b24 = btn24["text"]
    b25 = btn25["text"]
    count = count+1

    if b1==b2 and b2==b3 and b3==b4 and b4==b5 and b1=="O" or b1==b2 and b2==b3 and b3==b4 and b4==b5 and b1=="X":
        win(btn1["text"])

    if b6==b7 and b7==b8 and b8==b9 and b9==b10 and b6=="O" or b6==b7 and b7==b8 and b8==b9 and b9==b10 and b6=="X":
        win(btn6["text"])

    if b11==b12 and b12==b13 and b13==b14 and b14==b15 and b11=="O" or b11==b12 and b12==b13 and b13==b14 and b14==b15 and b11=="X":
        win(btn11["text"])

    if b16==b17 and b17==b18 and b18==b19 and b19==b20 and b16=="O" or b16==b17 and b17==b18 and b18==b19 and b19==b20 and b16=="X":
        win(btn16["text"])

    if b21==b22 and b22==b23 and b23==b24 and b24==b25 and b21=="O" or b21==b22 and b22==b23 and b23==b24 and b24==b25 and b21=="X":
        win(btn21["text"])





    if b1==b6 and b6==b11 and b11==b16 and b16==b21 and b1=="O" or b1==b6 and b6==b11 and b11==b16 and b16==b21 and b1=="X":
        win(btn1["text"])

    if b2==b7 and b7==b12 and b12==b17 and b17==b22 and b2=="O" or b2==b7 and b7==b12 and b12==b17 and b17==b22 and b2=="X":
        win(btn2["text"])

    if b3==b8 and b8==b13 and b13==b18 and b18==b23 and b3=="O" or b3==b8 and b8==b13 and b13==b18 and b18==b23 and b3=="X":
        win(btn3["text"])

    if b4==b9 and b9==b14 and b14==b19 and b19==b24 and b4=="O" or b4==b9 and b9==b14 and b14==b19 and b19==b24 and b4=="X":
        win(btn4["text"])

    if b5==b10 and b10==b15 and b15==b20 and b20==b25 and b5=="O" or b5==b10 and b10==b15 and b15==b20 and b20==b25 and b5=="X":
        win(btn5["text"])






    if b1==b7 and b7==b13 and b13==b19 and b19==b25 and b1=="O" or b1==b7 and b7==b13 and b13==b19 and b19==b25 and b1=="X":
        win(btn1["text"])

    if b21==b17 and b17==b13 and b13==b9 and b9==b5 and b21=="O" or b21==b17 and b17==b13 and b13==b9 and b9==b5 and b21=="X":
        win(btn21["text"])


    if count == 26:
        messagebox.showinfo("Match Tied!!")
        window.destroy()


def win(player):
    ans = "Game Complete " +player +"Wins!! ";
    messagebox.showinfo("Congratulations!!", ans)
    window.destroy()



btn1 = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Silver", command=clicked1)
btn2 = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Silver", command=clicked2)
btn3 = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Silver", command=clicked3)
btn4 = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Silver", command=clicked4)   
btn5 = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Silver", command=clicked5)

btn6 = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Silver", command=clicked6)    
btn7 = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Silver", command=clicked7)
btn8 = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Silver", command=clicked8)
btn9 = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Silver", command=clicked9)
btn10 = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Silver", command=clicked10)


btn11 = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Silver", command=clicked11)    
btn12 = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Silver", command=clicked12)    
btn13 = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Silver", command=clicked13)
btn14 = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Silver", command=clicked14)
btn15 = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Silver", command=clicked15)

btn16 = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Silver", command=clicked16)    
btn17 = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Silver", command=clicked17)    
btn18 = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Silver", command=clicked18)    
btn19 = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Silver", command=clicked19)    
btn20 = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Silver", command=clicked20)

btn21 = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Silver", command=clicked21)    
btn22 = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Silver", command=clicked22)    
btn23 = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Silver", command=clicked23)    
btn24 = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Silver", command=clicked24)    
btn25 = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Silver", command=clicked25) 


btn1.grid(row=1, column=1)
btn2.grid(row=2, column=1)
btn3.grid(row=3, column=1)
btn4.grid(row=4, column=1)
btn5.grid(row=5, column=1)


btn6.grid(row=1, column=2)    
btn7.grid(row=2, column=2)
btn8.grid(row=3, column=2)
btn9.grid(row=4, column=2)
btn10.grid(row=5, column=2)


btn11.grid(row=1, column=3)
btn12.grid(row=2, column=3)
btn13.grid(row=3, column=3)
btn14.grid(row=4, column=3)
btn15.grid(row=5, column=3)


btn16.grid(row=1, column=4)
btn17.grid(row=2, column=4)
btn18.grid(row=3, column=4)
btn19.grid(row=4, column=4)
btn20.grid(row=5, column=4)

btn21.grid(row=1, column=5)
btn22.grid(row=2, column=5)
btn23.grid(row=3, column=5)
btn24.grid(row=4, column=5)
btn25.grid(row=5, column=5)

    
window.mainloop()
