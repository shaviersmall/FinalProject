import tkinter as tk

class FitFrenApp(tk.Frame): #Creates overall window for FitFriend
    def __init__(self, root, set_height = 500, set_width = 800, bg_color = '#98FBCB', text_color = 'black'):
        super().__init__(root) #init for tk.frame, this is where you pass in arguments for the parent class tk.Frame
        
        self.main = root
        self.app_height = set_height
        self.app_width = set_width
        self.bg_color = bg_color
        self.text_color = text_color
        self.frames = []
        
        self.main.geometry(f'{self.app_width}x{self.app_height}')
        self.main.resizable(False, False)
        self.main.title('FitFriend')
        
        self.create_display_area()
        self.create_pages()
        self.create_button_area()
        
    def create_display_area(self):
        self.display_frame = tk.Frame(self.main, bg = self.bg_color, height = self.app_height - 50, width = self.app_width)
        
        #This places the display frame at the 0th row and 0th column of the root window 
        self.display_frame.grid(row = 0, column = 0, sticky = 'nsew')
        #This prevents the display frame from auto sizing to fit the widgets inside it
        self.display_frame.grid_propagate(0)
    
    def create_pages(self): #Creates each page to be displayed in the app
        health_page = HealthInfo(self.display_frame)
        health_page.grid(row=0, column=0, sticky="nsew")
    
        tracker_page = Tracker(self.display_frame)
        tracker_page.grid(row=0, column=0, sticky="nsew")
    
        main_page = MainPage(self.display_frame)
        main_page.grid(row=0, column=0, sticky="nsew")
    
        self.frames = [main_page, health_page, tracker_page]
        
    def create_button_area(self):
        #Create a container to hold buttons
        self.button_frame = tk.Frame(self.main, bg='#FEFFF1', height= 50, width = self.app_width)
        # This places the button frame at the first row and zero column of the root window 
        self.button_frame.grid(row=1, column=0)
        # This prevents the display frame from auto sizing to fit the widgets inside it
        self.button_frame.grid_propagate(0)
        
        #Create and place buttons in button frame
        b2 = tk.Button(self.button_frame, bg='#65C8B6', text="Main", font = 'bold', command=lambda x=self.frames[0]: x.show())
        b2.grid(row = 0, column = 0)

        b1 = tk.Button(self.button_frame, bg='#65C8B6', text="HealthInfo", font = 'bold', command=lambda x=self.frames[1]: x.show())
        b1.grid(row = 0, column = 1)

        b3 = tk.Button(self.button_frame, bg='#65C8B6', text="Tracker", font = 'bold', command=lambda x=self.frames[2]: x.show())
        b3.grid(row = 0, column = 2)
        
    
class MainPage(tk.Frame): #Landing page for FitnessFriend
    def __init__(self, parent, bg_color = '#98FBCB', text_color = 'black'):
        super().__init__(parent, background=bg_color)
        self.main = parent
        self.bg_color = bg_color
        self.text_color = text_color
        self.create_display_area()
        
    def create_display_area(self):
        self.display_frame = tk.Frame(self.main, bg = self.bg_color, height = 500, width = 800)
        
        #This places the display frame at the 0th row and 0th column of the root window
        self.display_frame.grid(row = 0, column = 0, sticky="nsew")
        #This prevents the display frame from auto sizing to fit the widgets inside it
        self.display_frame.grid_propagate(0)                                  
        
        self.display_label = tk.Label(self.display_frame, fg = self.text_color, bg = self.bg_color, font = ('Rockwell', 24, 'bold'), 
                                      text = 'Main Page', wraplength = 500, padx = 5, pady = 5, anchor = 'center')
        self.display_label.grid(row = 0, column = 0, sticky = 'nsew')
        
        self.display_label = tk.Label(self.display_frame, fg = self.text_color, bg = self.bg_color, font = ('Rockwell', 14), 
                                      text = 'Welcome! Please select a page from below. FitnessFriend is here to help YOU reach all your fitness goals!', 
                                      height = 10, width = 50, wraplength = 500, anchor = 'center')
        self.display_label.grid(row = 2, column = 0, sticky = 'nsew')
        
    def show(self):  #Shows desired page
        self.tkraise()
        self.create_display_area()

    def hide(self):  # Hides page
        self.pack_forget()
        
        
class HealthInfo(tk.Frame): #Page where user will enter their health information
    def __init__(self, parent, bg_color = '#98FBCB', text_color = 'black'):
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
        
        self.display_label = tk.Label(self.display_frame, fg = self.text_color, bg = self.bg_color, font = ('Rockwell', 24, 'bold'), 
                                      text = 'Health Information', height = 2, width = 10, wraplength = 200)
        self.display_label.grid(row = 0, column = 0)
        
    def input_health_info(self): #Creates all the fields for user to enter health info and receive suggestions
        #Create overall frame
        self.user_input_frame = tk.Frame(self.display_frame, height= 500, width=800, bg=self.bg_color)
        self.user_input_frame.grid(row=1, column=0)
        self.user_input_frame.grid_propagate(0)
        
        #Current height entry
        self.height_label = tk.Label(self.user_input_frame, fg = self.text_color, bg = self.bg_color, text='Enter your height in meters: ').grid(row=1, column=0, sticky='w')
        self.userheight = tk.DoubleVar()
        self.userheight.set(0)
        self.health_entry = tk.Entry(self.user_input_frame, textvariable = self.userheight, width=10).grid(row=1, column=1)
        
        #Current weight entry
        self.weight_label = tk.Label(self.user_input_frame, fg = self.text_color, bg = self.bg_color, text='Enter your weight in kilograms: ').grid(row=2, column=0, sticky='w')
        self.userweight = tk.DoubleVar()
        self.userweight.set(0)
        self.health_entry = tk.Entry(self.user_input_frame, textvariable = self.userweight, width=10).grid(row=2, column=1)
        
        self.enter_button = tk.Button(self.user_input_frame, fg = 'white', bg='black', text='Enter', command=lambda: self.calc_bmi(self.userheight.get(), self.userweight.get()))
        self.enter_button.grid(row=3, column=1, ipadx=1, ipady=1, pady=2)
        
        #Calculates BMI once user hits "enter" on height and weight
        self.bmi_label = tk.Label(self.user_input_frame, fg = self.text_color, bg = self.bg_color, text='Your BMI:')
        self.bmi_label.grid(row=4, column=0, sticky='w')
        
        #Outputs maintenance calories based on weight
        self.maintenance_label = tk.Label(self.user_input_frame, fg = self.text_color, bg = self.bg_color, text='Your maintenance calories:')
        self.maintenance_label.grid(row=5, column=0, sticky='w')
        
        #Target weight entry
        self.maintenance_label = tk.Label(self.user_input_frame, fg = self.text_color, bg = self.bg_color, text='Enter your target weight:').grid(row=6, column=0)
        self.targetweight = tk.DoubleVar()
        self.targetweight.set(0)
        self.target_entry = tk.Entry(self.user_input_frame, textvariable = self.targetweight, width=10).grid(row=6, column=1, ipadx=1, ipady=1, pady=2)
        
        self.enter_button = tk.Button(self.user_input_frame, fg = 'white', bg='black', text='Enter', command=lambda: self.calc_cal_deficit(self.targetweight.get()))
        self.enter_button.grid(row=6, column=3, ipadx=1, ipady=1, pady=2)
        
        #Outputs calorie deficit based on target weight
        self.cal_def = tk.Label(self.user_input_frame, fg = self.text_color, bg = self.bg_color, text='Your suggested calorie deficit:')
        self.cal_def.grid(row=7, column=0, sticky='w')
        
    def calc_bmi(self, height, weight):#Calculates BMI and handles exceptions in case user enters invalid characters
        try:
            height_square = (height ** 2)
            bmi = weight / height_square
            round_bmi = f"{bmi:.1f}" #BMI format: 1 decimal
            self.bmi_label['text'] = 'Your BMI: ' + str(round_bmi)
            
        except ZeroDivisionError:
            self.bmi_label['text'] = 'Please enter your height and weight.'
            
        except Exception as e:
            print(e)
            
    def calc_maintenance_cals(self, weight): #Calculates calories to maintain current weight and updates label
        try:
            maintenance_cals = weight * 15
            self.maintenance_label['text'] = 'Your maintenance calories: ' + str(maintenance_cals)
        except:
            self.maintenance_label['text'] = 'Please try again.'
            
    def calc_cal_deficit(self, target_weight): #Calculates recommended calorie deficit and updates labels
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
        
class Tracker(tk.Frame): #Log for calorie intake for each day of the week
    def __init__(self, parent, bg_color = '#98FBCB', text_color = 'black'):
        super().__init__(parent, background=bg_color)
        self.main = parent
        self.bg_color = bg_color
        self.text_color = text_color
        self.create_display_area()
     
    def save_data(self, entry, t): #Source: StackOverflow, save data for log purposes
        global last_entry
        last_entry = entry.get()
        
    def create_display_area(self):
        self.display_frame = tk.Frame(self.main, bg = self.bg_color)
        
        #This places the display frame at the 0th row and 0th column of the root window
        self.display_frame.grid(row = 0, column = 0, sticky="nsew")
        #This prevents the display frame from auto sizing to fit the widgets inside it
        self.display_frame.grid_propagate(0)
        
        self.display_label = tk.Label(self.display_frame, fg = self.text_color, bg = self.bg_color, font = ('Rockwell', 24, 'bold'), 
                                      text = 'Calorie Tracker', height = 2, width = 10, wraplength = 200)
        self.display_label.grid(row = 0, column = 0)
        
        
    def daily_tracker(self): #Display calorie count per day of the week based on selected meals
        #Create frame to hold tracker
        self.tracker_frame = tk.Frame(self.display_frame, height= 500, width=800, bg='#98FBCB')
        self.tracker_frame.grid(row=1, column=0)
        self.tracker_frame.grid_propagate(0)
        
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        
        self.cal_count = []
        for i, day in enumerate(days):
            #Create calorie entry points for each day of the week
            self.day_label = tk.Label(self.tracker_frame, fg = self.text_color, bg = self.bg_color, text = day, font = ('Rockwell', '10'), height = 2, width = 20, wraplength = 200)
            self.day_label.grid(row = i + 2, column=0, sticky='w')
            
            self.cals = tk.IntVar()
            self.cals.set(0)
            
            self.cals_entry = tk.Entry(self.tracker_frame, textvariable = self.cals, width=10)
            self.cals_entry.grid(row=i+2, column=1, ipadx=5, ipady=1, padx = 5, pady=2)
            
            self.enter_button = tk.Button(self.tracker_frame, fg = self.text_color, bg='white', text='Submit', command=lambda: self.get_cal_list(self.cals.get()))
            self.enter_button.grid(row=i+2, column=2, ipadx=1, ipady=1, padx = 10, pady=2)
    
       
        #Enter average calories to keep track of for the week
        self.avg_label = tk.Label(self.tracker_frame, fg = self.text_color, bg = self.bg_color, text = "Average Weekly Calories:", font = ('Rockwell', '9'), height = 2, width = 20, wraplength = 200)
        self.avg_label.grid(row = 9, column=0, sticky='w')
        
        self.avg_cals = tk.IntVar()
        self.avg_cals.set(0)
            
        self.avgcals_entry = tk.Entry(self.tracker_frame, textvariable = self.avg_cals, width=10)
        self.avgcals_entry.grid(row=9, column=1, ipadx=5, ipady=1, padx = 5, pady=2)
            
        self.entry_button = tk.Button(self.tracker_frame, fg = self.text_color, bg='white', text='Submit', command=lambda: self.get_cal_list(self.cals.get()))
        self.entry_button.grid(row=9, column=2, ipadx=1, ipady=1, padx = 10, pady=2)
        
        #save button to return for another session
        save_button = tk.Button(self.tracker_frame, text = 'Save', command = lambda: self.save_data(self.cals, str(self.cals)))
        save_button.grid(row = 11, column = 0)
        
        #Show sample meal database for easy calculating
        self.brekkie_dict = {'Avocado-arugula omelet' : 344,
                     'Apple-cinnamon quinoa bowl': 331,
                     'Raspberry ricotta waffle': 318,
                     'Power greens fruit salad': 433,
                     'Beef lettuce wraps' : 494,
                     'Veggie brown rice bowl' : 501
                     }
        self.avg_label = tk.Label(self.tracker_frame, fg = self.text_color, bg = self.bg_color, text = "Sample Meals:", height = 2, width = 20, wraplength = 200, font = ('Rockwell', 12, 'bold')).grid(row = 1, column=11, sticky = 'e')
        self.avg_label = tk.Label(self.tracker_frame, fg = self.text_color, bg = self.bg_color, text = "Calories:", height = 2, width = 20, wraplength = 200, font = ('Rockwell', 12, 'bold')).grid(row = 1, column=12, sticky ='e')
        
        row = 2
        
        #adds each meal to frame
        for meal, calories in self.brekkie_dict.items():
            tk.Label(self.tracker_frame, text=meal, font = ('Rockwell', 10, 'bold'), width=30, bg = '#FEFFF1', borderwidth=2, relief="solid").grid(row=row, column=11, ipadx=5, ipady=5)
            tk.Label(self.tracker_frame, text=calories, font = ('Rockwell', 10, 'bold'), width=15, bg = '#FEFFF1', borderwidth=2, relief="solid").grid(row=row, column=12, ipadx=5, ipady=5)
            row += 1
            
                           
    def get_cal_list(self, cals):
        self.cal_list = self.cal_count.append(cals)

        
    def show(self):  #Shows desired page
        self.tkraise()
        self.create_display_area()
        self.daily_tracker()
        

    def hide(self):  # Hides page
        self.pack_forget()
   

if __name__ == '__main__':
    #This creates the root window
    root = tk.Tk()
    fit_fren_app = FitFrenApp(root)
    root.mainloop()
        