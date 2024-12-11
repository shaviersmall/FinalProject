import tkinter as tk

class FitFrenApp(tk.Frame): #Creates parent class for pages which each page will inherit from
    def __init__(self, root, set_height = 500, set_width = 800, bg_color = 'lightgreen', text_color = 'white'):
        super().__init__(root) #init for tk.frame, this is where you pass in arguments for the parent class tk.Frame
        
        self.main = root
        self.app_height = set_height
        self.app_width = set_width
        self.bg_color = bg_color
        self.text_color = text_color
        self.frames = []
        
        self.main.geometry(f'{self.app_width}x{self.app_height}')
        self.main.resizable(False, False)
        self.main.title('FitFren')
        
        self.create_display_area()
        self.create_pages()
        self.create_button_area()
        
    def create_display_area(self):
        self.display_frame = tk.Frame(self.main, bg = self.bg_color, height = self.app_height -100, width = self.app_width)
        
        #This places the display frame at the 0th row and 0th column of the root window 
        self.display_frame.grid(row = 0, column = 0)
        #This prevents the display frame from auto sizing to fit the widgets inside it
        self.display_frame.grid_propagate(0)
    
    def create_pages(self):
        health_page = HealthInfo(self.display_frame)
        health_page.grid(row=0, column=0, sticky="nsew")
    
        tracker_page = Tracker(self.display_frame)
        tracker_page.grid(row=0, column=0, sticky="nsew")
    
        main_page = MainPage(self.display_frame)
        main_page.grid(row=0, column=0, sticky="nsew")
    
        self.frames = [main_page, health_page, tracker_page]   
        
    def create_button_area(self):
        # Lets create a container to hold our buttons
        self.button_frame = tk.Frame(self.main, bg='blue', height= self.app_height - self.display_frame["height"], width=self.app_width)
        # This places the button frame at the first row and zero column of the root window 
        self.button_frame.grid(row=1, column=0)
        # This prevents the display frame from auto sizing to fit the widgets inside it
        self.button_frame.grid_propagate(0)
        
        #Create and place buttons
        b2 = tk.Button(self.button_frame, bg='red', text="Main", command=lambda x=self.frames[0]: x.show())
        b2.grid(row = 0, column = 0)

        b1 = tk.Button(self.button_frame, bg='red', text="HealthInfo", command=lambda x=self.frames[1]: x.show())
        b1.grid(row = 0, column = 1)

        b3 = tk.Button(self.button_frame, bg='red', text="Tracker", command=lambda x=self.frames[2]: x.show())
        b3.grid(row = 0, column = 2)
        
    
        
class HealthInfo(tk.Frame): #Page where user will enter their health information
    def __init__(self, parent, bg_color = 'lightgreen', text_color = 'white'):
        super().__init__(parent, background=bg_color)
        self.bg_color = bg_color
        self.main = parent
        self.text_color = text_color
        self.create_display_area()
        self.input_health_info()
     
    def create_display_area(self):
        self.display_frame = tk.Frame(self.main, height = 500, width = 800, bg = self.bg_color)
        
        #This places the display frame at the 0th row and 0th column of the root window
        self.display_frame.grid(row = 0, column = 0, sticky="nsew")
        #This prevents the display frame from auto sizing to fit the widgets inside it
        self.display_frame.grid_propagate(0)
        
        self.display_label = tk.Label(self.display_frame, fg = self.text_color, bg = self.bg_color, font = ('Arial', 24, 'bold'), 
                                      text = 'Health Information', height = 2, width = 10, wraplength = 200)
        self.display_label.grid(row = 0, column = 0)
        
    def input_health_info(self):
        self.user_input_frame = tk.Frame(self.display_frame, height= 500, width=800, bg='purple')
        self.user_input_frame.grid(row=1, column=0)
        self.user_input_frame.grid_propagate(0)
        
        self.height_label = tk.Label(self.user_input_frame, fg = self.text_color, bg = self.bg_color, text='Enter your height in meters: ').grid(row=1, column=0, sticky='w')
        self.userheight = tk.IntVar()
        self.userheight.set(0)
        self.health_entry = tk.Entry(self.user_input_frame, textvariable = self.userheight, width=10).grid(row=1, column=1)
        
        self.weight_label = tk.Label(self.user_input_frame, fg = self.text_color, bg = self.bg_color, text='Enter your weight in kg: ').grid(row=2, column=0, sticky='w')
        self.userweight = tk.IntVar()
        self.userweight.set(0)
        self.health_entry = tk.Entry(self.user_input_frame, textvariable = self.userweight, width=10).grid(row=2, column=1)
        
        self.enter_button = tk.Button(self.user_input_frame, fg = self.text_color, bg='black', text='Enter', command=lambda: self.calc_bmi(self.userheight.get(), self.userweight.get()))
        self.enter_button.grid(row=3, column=1, ipadx=1, ipady=1, pady=2)
        
        self.bmi_label = tk.Label(self.user_input_frame, fg = self.text_color, bg = self.bg_color, text='Your BMI:')
        self.bmi_label.grid(row=4, column=0, sticky='w')
        
        self.maintenance_label = tk.Label(self.user_input_frame, fg = self.text_color, bg = self.bg_color, text='Your maintenance calories:')
        self.maintenance_label.grid(row=5, column=0, sticky='w')
        
        self.maintenance_label = tk.Label(self.user_input_frame, fg = self.text_color, bg = self.bg_color, text='Enter your target weight:').grid(row=6, column=0)
        self.targetweight = tk.IntVar()
        self.targetweight.set(0)
        self.target_entry = tk.Entry(self.user_input_frame, textvariable = self.targetweight, width=10).grid(row=6, column=1, ipadx=1, ipady=1, pady=2)
        
        self.enter_button = tk.Button(self.user_input_frame, fg = self.text_color, bg='black', text='Enter', command=lambda: self.calc_cal_deficit(self.targetweight.get()))
        self.enter_button.grid(row=6, column=3, ipadx=1, ipady=1, pady=2)
        
        self.cal_def = tk.Label(self.user_input_frame, fg = self.text_color, bg = self.bg_color, text='Your suggested calorie deficit:')
        self.cal_def.grid(row=7, column=0, sticky='w')
        
        
        
    def calc_bmi(self, height, weight):
        try:
            height_square = height ** 2
            bmi = weight // height_square
            self.bmi_label['text'] = 'Your BMI: ' + str(bmi)
            
        except ZeroDivisionError:
            self.bmi_label['text'] = 'Please enter your height and weight.'
            
        except Exception as e:
            print(e)
            
    def calc_maintenance_cals(self, weight):
        try:
            maintenance_cals = weight * 15
            self.maintenance_label['text'] = 'Your maintenance calories: ' + str(maintenance_cals)
        except:
            self.maintenance_label['text'] = 'Please try again.'
            
    def calc_cal_deficit(self, target_weight): 
        try:
            cal_deficit = target_weight * 2.2 * 12
            float_def = f"{cal_deficit:.2f}"
            self.cal_def['text'] = 'Your suggested calorie deficit: ' + str(float_def) + 'cals'

        except:
            self.cal_def['text'] = 'Please try again.'
            
        
        
        
        
        
        
        
    
        
        
    def show(self):  #Shows desired page
        self.tkraise()
        self.create_display_area()
        self.input_health_info()

    def hide(self):  # Hides page
        self.pack_forget()
        
class MainPage(tk.Frame):
    def __init__(self, parent, bg_color = 'pink', text_color = 'white'):
        super().__init__(parent, background=bg_color)
        self.main = parent
        self.bg_color = bg_color
        self.text_color = text_color
        self.create_display_area()
    def create_display_area(self):
        self.display_frame = tk.Frame(self.main, bg = self.bg_color)
        
        #This places the display frame at the 0th row and 0th column of the root window
        self.display_frame.grid(row = 0, column = 0, sticky="nsew")
        #This prevents the display frame from auto sizing to fit the widgets inside it
        self.display_frame.grid_propagate(0)                                  
        
        self.display_label = tk.Label(self.display_frame, fg = self.text_color, bg = self.bg_color, font = ('Arial', 24, 'bold'), 
                                      text = 'Main Page!', height = 2, width = 10, wraplength = 200)
        self.display_label.grid(row = 0, column = 0)
        
    def show(self):  #Shows desired page
        self.tkraise()
        self.create_display_area()

    def hide(self):  # Hides page
        self.pack_forget()

class Tracker(tk.Frame):
    def __init__(self, parent, bg_color = 'pink', text_color = 'white'):
        super().__init__(parent, background=bg_color)
        self.main = parent
        self.bg_color = bg_color
        self.text_color = text_color
        self.create_display_area()
     
    def create_display_area(self):
        self.display_frame = tk.Frame(self.main, bg = self.bg_color)
        
        #This places the display frame at the 0th row and 0th column of the root window
        self.display_frame.grid(row = 0, column = 0, sticky="nsew")
        #This prevents the display frame from auto sizing to fit the widgets inside it
        self.display_frame.grid_propagate(0)
        
        self.display_label = tk.Label(self.display_frame, fg = self.text_color, bg = self.bg_color, font = ('Arial', 24, 'bold'), 
                                      text = 'Tracker!', height = 2, width = 10, wraplength = 200)
        self.display_label.grid(row = 0, column = 0)
        
    def show(self):  #Shows desired page
        self.tkraise()
        self.create_display_area()

    def hide(self):  # Hides page
        self.pack_forget()
   
        
# class MainView(tk.Frame): #Main view where all other pages and widgets will be accessed from
#     def __init__(self, root, set_height = 500, set_width = 800, bg_color = 'pink', text_color = 'white'):
#         super().__init__(root) #init for tk.frame, this is where you pass in arguments for the parent class tk.Frame
#         self.main = root
#         self.app_height = set_height
#         self.app_width = set_width
#         self.bg_color = bg_color
#         self.text_color = text_color
        
#         #Container and button frame
#         self.button_frame = tk.Frame(self, bg = bg_color)
#         self.container = tk.Frame(self.main, bg = self.bg_color)
        
#         self.button_frame.grid(row = 0, column = 0, columnspan = 3)
#         self.container.grid(row = 0, column = 0)
                        
#         #Create and place pages
#         self.p1 = HealthInfo(self)
#         self.p1.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
        
#         self.p2 = MainPage(self)
#         self.p2.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
        
#         self.p3 = Tracker(self)
#         self.p3.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
        
#         #Create and place buttons
#         b1 = tk.Button(self.button_frame, bg='red', text="HealthInfo", command=lambda x = self.p1: self.show_page(x))
#         b1.grid(row = 0, column = 0)

#         b2 = tk.Button(self.button_frame, bg='red', text="Main", command=lambda x = self.p2: self.show_page(x))
#         b2.grid(row = 0, column = 1)

#         b3 = tk.Button(self.button_frame, bg='red', text="Tracker", command=lambda: self.show_page(self.p3))
#         b3.grid(row = 0, column = 2)

#         # Initially show the MainPage
#         self.show_page(self.p2)
        
#     def show_page(self, page):
#         # Hide all pages
#         self.p1.hide()
#         self.p2.hide()
#         self.p3.hide()

#         # Show the selected page
#         page.show()
        
#     def func(self, args):
#         print(args)
 
        
        
        
          
        
if __name__ == '__main__':
    #This creates the root window
    root = tk.Tk()
    fit_fren_app = FitFrenApp(root)
    root.mainloop()
        