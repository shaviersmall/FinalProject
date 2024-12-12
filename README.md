# FinalProject
FitFriend is an application dedicated to helping the user reach their fitness goals by providing a platform for them to input their health and nutrition information, such as their current weight their target weight. Based on the information provided, FitFriend can make suggestions with regards to calorie deficits, as well provide information on how many calories are taken in from eating and maintenance calories.

This GUI was created using the Python tkinter module. It is necessary to have this imported before running the code. The code makes use of the Frame, Button, and Label tools in order to display content and allow for user interaction with the interface. Each class inherits from tk.Frame, with the FitFrenApp serving as the root from which the initial display is created and the pages and buttons are placed. Each class additionally has methods which enable their respective functionality.

When the program is run, the GUI will pop up with the main screen and three buttons that allow the user to navigate between pages. On the HealthInfo and Tracker pages, the user is able to input information and receive updates when the "Submit" or "Enter" buttons are clicked. These will update if the user changes the input. The Tracker page additionally has functionality that allows users to save their data and return for another session.


