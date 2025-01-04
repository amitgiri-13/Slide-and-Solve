from tkinter import *
import random
import pygame


#creating class for 8 puzzle box 
class PuzzleBox:
    #initializing attributes for puzzle box
    def __init__(self,root):
        #window geometry
        root.geometry("500x600")
        #name of our puzzle
        root.title("Solve Me")
        
        #start frame
        self.start_frame = Frame(root,bg="lightgray",height=50)
        self.start_frame.pack(fill="both",expand=1)
        
        #playing frame
        self.puzzle_frame = Frame()
        self.button_frame = Frame()

        #END FRAME
        self.end_frame = Frame()
        
        self.game_label = Label(self.start_frame,text="Solve Me",bg="lightgray",font=("arial",20))
        self.game_label.place(relx=.37,rely=.38 )
        #play button
        self.play_button = Button(self.start_frame,text="play",bg="teal",borderwidth=2,command=self.play_now)
        self.play_button.place(relx=.45,rely=.45)
        
        #button name
        self.selected_button = None
        self.to_swap = None

        self.count_steps = 0
        

    def play_now(self):
        self.count_steps = 0
        self.end_frame.destroy()
        self.play_sound("button.mp3")
        self.start_frame.destroy()
        #creating frame for game
        self.puzzle_frame = Frame(root)
        self.puzzle_frame.pack(fill="both",expand=1)
        self.puzzle_frame.config(bg="beige",height=400)
        #frame for buttons 
        self.button_frame = Frame(root,bg="lightgray",height=50)
        self.button_frame.pack(fill="both",expand=1)

        #to rearrange buttons
        self.again_button = Button(self.button_frame,text="REPLAY",bg="orange",command=self.rearrange_blocks)
        self.again_button.grid(row=0,column=0,padx=10,pady=10,ipadx=30)
       
        #to exit the game
        self.exit_button = Button(self.button_frame,text="EXIT",bg="red",command=root.quit)
        self.exit_button.grid(row=0,column=3,padx=10,pady=10,ipadx=40)

        

        self.create_blocks()

    def create_blocks(self):    
        #buttons for blocks
        self.number = 0
        unique_numbers = random.sample(range(9), 9)
        #unique_numbers = ["1","2","3","4","5","6","","7","8"]
        for row in range(3):
            for column in range(3):
                if unique_numbers[self.number] == 0:
                    self.block = Button(self.puzzle_frame,text="",bg="lightblue",relief=RAISED,borderwidth=5)
                    self.block.bind("<Button-1>",self.select_button)
                    self.block.grid(row=row,column=column,padx=1,pady=1,ipadx=60,ipady=60)
                else:
                    self.block = Button(self.puzzle_frame,text=f"{unique_numbers[self.number]}",bg="lightblue",relief=RAISED,borderwidth=5)
                    self.block.bind("<Button-1>",self.select_button)
                    self.block.grid(row=row,column=column,padx=1,pady=1,ipadx=60,ipady=60)

                self.number = self.number + 1
        
    #swap function
    def swap_blocks(self,button):
        self.to_swap = button
        a,b = self.selected_button.grid_info()["row"],self.selected_button.grid_info()["column"]
        i,j = self.to_swap.grid_info()["row"],self.to_swap.grid_info()["column"]
        x = self.selected_button.cget("text")
        y = self.to_swap.cget("text")
        if i==a:
            if j==b-1 or j==b+1:
                self.play_sound("swipe.mp3")
                # self.selected_button.grid(row=i,column=j)
                # self.to_swap.grid(row=a,column=b)
                self.selected_button.config(text=y)
                self.to_swap.config(text=x)
                self.win_checker()
                self.steps_label = Label(self.button_frame)
                self.steps_label.config(text=f"steps: {self.count_steps}",bg="lightgray",font=("arial",12))
                self.steps_label.grid(row=0,column=2,padx=10,pady=10,ipadx=40)
        elif j==b:
            if i==a-1 or i==a+1:
                self.play_sound("swipe.mp3")
                # self.selected_button.grid(row=i,column=j)
                # self.to_swap.grid(row=a,column=b)
                self.selected_button.config(text=y)
                self.to_swap.config(text=x)
                self.win_checker()
                self.steps_label = Label(self.button_frame)
                self.steps_label.config(text=f"steps: {self.count_steps}",bg="lightgray",font=("arial",12))
                self.steps_label.grid(row=0,column=2,padx=10,pady=10,ipadx=40)
        else:
            pass  
        self.selected_button=None
    #rearrange function
    def rearrange_blocks(self):
        self.end_frame.destroy()
        self.play_sound("button.mp3") 
        self.puzzle_frame.destroy()
        self.button_frame.destroy()
        self.play_now()

    def select_button(self,event):
        self.play_sound("button.mp3")  
        if self.selected_button:
            self.selected_button.config(bg="lightblue")
            if self.selected_button.cget("text") == "" or event.widget.cget("text") == "":
                self.swap_blocks(event.widget)
            else:
                self.selected_button = None
        else:
            self.selected_button = event.widget
            self.selected_button.config(bg="blue")

    def restart(self):
       
        self.end_frame = Frame(root,bg="lightgray",height=50)
        self.end_frame.pack(fill="both",expand=1)

        self.won_label = Label(self.end_frame,text="You Won!!",bg="lightgray",font=("arial",20))
        self.won_label.place(relx=.37,rely=.0 )
        


    def win_checker(self):
        root.update_idletasks()
        self.count_steps += 1
        correct = ["1","2","3","4","5","6","7","8","",]
        all_children = self.puzzle_frame.winfo_children()
        current = []
        # Filter the list to include only buttons
        for children in all_children:
            current.append((children.cget("text")))
      
        if current == correct:
            self.puzzle_frame.destroy()
            #self.button_frame.destroy()
            self.restart()

        
    def play_sound(self,path):
        file_path = f"sounds/{path}"
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

if __name__ == "__main__":
    #initializing root window
    root = Tk()

    puzzle = PuzzleBox(root)

    #mainloop
    root.mainloop() 