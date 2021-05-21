from tkinter import *
import requests,json
from nutritionix import Nutritionix
import datetime 
nix = Nutritionix(app_id="511e8a53", api_key="e85772f6a9f668c67cd840bfc33669d4")

initial=Tk()
initial.title("Nutrition APP")
initial.iconbitmap('C:/Users/jlorenc1/Desktop/project1-nutrition/app.ico')
#getting the date
date_now= datetime.datetime.now()


#creating a creating the frame to introduce the graphics.
frame1=LabelFrame(initial, text="Welcome please type ingredient " +date_now.strftime('%A %d %B %Y') ,padx=50,pady=100,)
frame1.pack(fill="both",expand="yes")
#creating a entry
entry=Entry(frame1,width=20,bd=4)
entry.grid(row=0,column=0)

#function do the searching.
def looking():
     product=nix.search(entry.get()).json()
     product_id=product['hits'][0]['_id']
     nutrition_val=nix.item(id=product_id).json()
     calories=nutrition_val['nf_calories']
     cholesterol=nutrition_val['nf_cholesterol']
     suggars=nutrition_val['nf_cholesterol']
     lable=Label(frame1,text=entry.get()+'\nThe number of Calories(KJ): '+str(calories)+ '\ncholesterol grams '+str(cholesterol)+ ' \nsuggars grams '+str(suggars))
     lable.grid(row=1,columnspan=3,)
     entry.delete(0,END)
#Button to search for the ingredients
calories=Button(frame1,text="Ingredient",command=looking )
calories.grid(row=0,column=1,padx=6, pady=6)

#Exit program
quit_button=Button(frame1,text="Exit app",command=quit)
quit_button.grid(row=0,column=2)

#closing the program
initial.mainloop()



















