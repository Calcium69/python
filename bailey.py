from ursina import * #imports everything from the module ursina

window.title="Callum clicker" #Sets the name of the game at the top as "Callum clicker"
app=Ursina() #make the variable the class (dont have to put brackets)

window.borderless=False #Makes the window of the game have borders

def score(): #defining a function so it can be called at anypoint in the code
    global Clicks #Globallly defines the function so it can be edited within the function
    Clicks+=1 #Adds 1 to the Clicks variable

Button1=Button(icon="ArryPothead.jpg", scale=[.54,.6], y=-.02, x=-.5) #making button a class and passing arguments which are the things in the brackets
#              ^^^^^^^^^^^^^^^^ Remove and put icon="ArryPothead.jpg"

Button1.on_click=score #when you click the button in game it will call the function it is set to

Button2=Button(amount=0,cost=100,icon="strong snowman.jpg", scale=[.16,.2], y=.35, x=.7,enabled=False)

Button3=Button(amount=0,cost=500,icon="thumbs up.jpg", scale=[.16,.2], y=.05, x=.7,enabled=False)

Button4=Button(amount=0,cost=1000,icon="devious smile.jpg", scale=[.16,.2], y=-.25, x=.7,enabled=False)



def shopfunc():
    if Button2.enabled:
        Button1.enabled=True
        Button2.enabled=False
        Button3.enabled=False 
        Button4.enabled=False
        Text2.visible=True
        Text3.visible=False 
        Text4.visible=False 
        Text5.visible=False 
        Text6.visible=False 
        Text7.visible=False 
        Text8.visible=False
        Text10.visible=False
        shop.enabled=True
        returnButton.enabled=False
    else:
        Button1.enabled=False
        Button2.enabled=True
        Button3.enabled=True
        Button4.enabled=True
        Text2.visible=False
        Text3.visible=True
        Text4.visible=True
        Text5.visible=True
        Text6.visible=True
        Text7.visible=True
        Text8.visible=True
        Text10.visible=True
        shop.enabled=False
        returnButton.enabled=True


shop=Button(scale=.4,icon="Callums (store).jpg",x=.5, y=.2,enabled=True)
shop.on_click=shopfunc

returnButton=Button(scale=.4,icon="Return.jpg",x=.4,enabled=False)
returnButton.on_click=shopfunc

def Gen1():
    global Clicks,Button2
    if Clicks>=Button2.cost:
        Clicks-=Button2.cost
        Button2.cost *= 2
        Button2.amount += 1
        Gen1Func()

def Gen1Func():
    global Clicks
    Clicks+=2*Button2.amount
    invoke(Gen1Func,delay=2)
Button2.on_click=Gen1



def Gen2():
    global Clicks,Button3
    if Clicks>=Button3.cost:
        Clicks-=Button3.cost
        Button3.cost *= 2
        Button3.amount += 1
        Gen2Func()

def Gen2Func():
    global Clicks
    Clicks+=10*Button3.amount
    invoke(Gen2Func,delay=2)
Button3.on_click=Gen2



def Gen3():
    global Clicks,Button4
    if Clicks>=Button4.cost:
        Clicks-=Button4.cost
        Button4.cost *= 2
        Button4.amount += 1
        Gen3Func()

def Gen3Func():
    global Clicks
    Clicks+=50*Button4.amount
    invoke(Gen3Func,delay=2)
Button4.on_click=Gen3



Text1=Text(text="callums: 0", y=.45, x=-.1, scale=1.4) #creates text using the Text class
Text2=Text(text="click for callums", y=.32, x=-.65, scale=1.4,visible=True) #creates text using the Text class
Text3=Text(text="2 callums p/s", y=.25, x=.625, scale=.9,visible=False) #creates text using the Text class
Text4=Text(text="cost: 0", y=.47, x=.65, scale=.9,visible=False) #creates text using the Text class
Text5=Text(text="10 callums p/s", y=-.05, x=.625, scale=.9,visible=False) #creates text using the Text class
Text6=Text(text="cost: 0", y=.17, x=.65, scale=.9,visible=False) #creates text using the Text class
Text7=Text(text="50 callums p/s", y=-.35, x=.625, scale=.9,visible=False) #creates text using the Text class
Text8=Text(text="cost: 0", y=-.13, x=.65, scale=.9,visible=False) #creates text using the Text class
Text9=Text(text="callum's store", y=-.01, x=.25, scale=1.9,visible=True)
Text10=Text(text="return", y=-.1, x=.25, scale=1.9,visible=False)


Clicks=0 #sets intiger (int) value as 0 to the Clicks variable

def update(): #update function get calls every frame
    Text1.text=f"callums: {Clicks}" #Changes the text of the Text1 variable class
    Text4.text=f"cost: {Button2.cost}" #Changes the text of the Text1 variable class
    Text6.text=f"cost: {Button3.cost}" #Changes the text of the Text1 variable class
    Text8.text=f"cost: {Button4.cost}" #Changes the text of the Text1 variable class
    Text1.create_background()


app.run() #Mainloop runs so the app doesn't just open and close