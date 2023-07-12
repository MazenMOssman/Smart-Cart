# This file has the GUI and the running process.
from PIL import ImageTk,Image
from cart_list import Cart
import tkinter as tk
import cv2
from Class_NN import NN


# initialize a tkinter window with a background image
root = tk.Tk()
root.title("Welcome To Smart Cart")
root.iconbitmap("resource/test2.ico")
root.geometry("500x500")
img = ImageTk.PhotoImage(Image.open(r"resource/test2.jpeg").resize((300,500)))

#Initialize a list  
cart = Cart()


# configure the tkinter window
my_can = tk.Canvas(root,width = 500, height = 500)
my_can.pack(fill = "both",expand = True)
my_can.create_image(200,0,image = img, anchor = "nw")


flag = False
Check_out2 = False

# initializing a button in the tkinter window with an image.
def button1():
    global my_can
    global root
    global img
    # global Check_out2
    global flag
    img = ImageTk.PhotoImage(Image.open(r"resource/QR_New.jpeg").resize((450, 450)))
    #image not visual
    my_can.create_image(25, 0, image = img, anchor = "nw")
    cart.checkout()
    flag = True
global label1
label1 = my_can.create_text(100, 50, text="List of buys", font=("Helvetica", 10))
global label2
label2 = my_can.create_text(100, 100, text="  " , font=("Helvetica", 10))
global label3
label3 = my_can.create_text(100, 150, text="  "  , font=("Helvetica", 10))
global label4
label4 = my_can.create_text(100, 200, text="  " , font=("Helvetica", 10))
global label5
label5 = my_can.create_text(100, 250, text="  "  , font=("Helvetica", 10))
global label6
label6 = my_can.create_text(100, 300, text="  " , font=("Helvetica", 10))
global label7
label7 = my_can.create_text(100, 350, text="Total price  "  + "LE", font=("Helvetica", 10))


# Initialize a neural network
network = NN()

flag = False
# Create the scan button and use it to open the camera and scan for the product.
def button3():
    global my_can
    global root
    global flag
    global cart
    global network
    global label1
    global label2
    global label3
    global label4
    global label5
    global label6
    global label7
    if flag == False:
        cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        state, img_1 = cam.read()
        x = cv2.cvtColor(img_1, cv2.COLOR_BGR2RGB)
        img = cv2.resize(x, (500, 500))
        cv2.imshow("Img", img_1)
        cv2.waitKey(10)
        pro_number,pred_num,predict,class_model,fl = network.run_NN(img)
        print(pred_num)
        print(predict)

        if pred_num  > 0.97:
            print(pred_num)
            print(predict)
            cart.Quantaty(pro_number)
            cart.Full_price()
            a, s, d, f, g, price = cart.Get_products()
            my_can.delete(label1)
            my_can.delete(label2)
            my_can.delete(label3)
            my_can.delete(label4)
            my_can.delete(label5)
            my_can.delete(label6)
            my_can.delete(label7)
            label1 = my_can.create_text(100, 50, text="List of buys", font=("Helvetica", 10))
            label2 = my_can.create_text(100, 100, text="Apples  " + str(a) + " KG", font=("Helvetica", 10))
            label3 = my_can.create_text(100, 150, text="Chepsi  " + str(s), font=("Helvetica", 10))
            label4 = my_can.create_text(100, 200, text="Chocolate  " + str(d), font=("Helvetica", 10))
            label5 = my_can.create_text(100, 250, text="Dalton  " + str(f), font=("Helvetica", 10))
            label6 = my_can.create_text(100, 300, text="Salsa  " + str(g), font=("Helvetica", 10))
            label7 = my_can.create_text(100, 350, text="Total price  " + str(price) + "LE", font=("Helvetica", 10))

            print(label6)

# Create the checkout button
Cout = tk.Button(root,text = "Checkout",command = button1  ,fg ="white",bg = "black" )
button = my_can.create_window(100,450, anchor = "nw", window = Cout )

# Create the scan button
Cout2 = tk.Button(root,text = "Scan",command = button3 ,fg ="white",bg = "black" )
button2 = my_can.create_window(25,450, anchor = "nw", window = Cout2 )


root.mainloop()
