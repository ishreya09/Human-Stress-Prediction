# import libraries
from tkinter import *
import pickle

knn_model = pickle.load(open('knn_model.pkl', 'rb'))
rf_model = pickle.load(open('model.pkl','rb'))


# main function
def main():


        
    root= Tk()

    # set the background colour of GUI window
    root.configure(background='light green')
    root.title("Predict Stress Levels on the basis of snoring range of the user, respiration rate, body temperature, limb movement rate, \
blood oxygen levels, eye movement, number of hours of sleep, heart rate and predict Stress Levels")
    # (0- low/normal, 1 – medium low, 2- medium, 3-medium high, 4 -high)

    # Heading label
    # head = Label(root, text="Predict Stress Levels on the basis of snoring range of the user,\n respiration rate, body temperature, limb movement rate,\n \
    #             blood oxygen levels, eye movement, number of hours of sleep, \n heart rate and predict Stress Levels", bg="light green")
    # head.grid(row=0, column=0, padx=10, pady=10)
    # head.config(font=("times", 10   , "bold"))


    # create a label : Enter Snoring Range
    Snoring_Range_l = Label(root, text="Enter Snoring Range", bg="light green")
    Snoring_Range_l.grid(row=0, column=0, padx=10, pady=10)
    Snoring_Range_l.config(font=("times", 20, "bold"))

    # create a entry box for Snoring Range
    Snoring_Range = Entry(root)
    Snoring_Range.grid(row=0, column=1, padx=10, pady=10)
    Snoring_Range.config(font=("times", 20, "bold"))

    # create a label : Enter Respiration Rate
    Respiration_Rate_l = Label(root, text="Enter Respiration Rate", bg="light green")
    Respiration_Rate_l.grid(row=1, column=0, padx=10, pady=10)
    Respiration_Rate_l.config(font=("times", 20, "bold"))

    # create a entry box for Respiration Rate
    Respiration_Rate = Entry(root)
    Respiration_Rate.grid(row=1, column=1, padx=10, pady=10)
    Respiration_Rate.config(font=("times", 20, "bold"))

    # create a label : Enter Body Temperature
    Body_Temperature_l = Label(root, text="Enter Body Temperature", bg="light green")
    Body_Temperature_l.grid(row=2, column=0, padx=10, pady=10)
    Body_Temperature_l.config(font=("times", 20, "bold"))
    
    # create a entry box for Body Temperature
    Body_Temperature = Entry(root)
    Body_Temperature.grid(row=2, column=1, padx=10, pady=10)
    Body_Temperature.config(font=("times", 20, "bold"))

    # create a label : Enter Limb Movement Rate
    Limb_Movement_Rate_l = Label(root, text="Enter Limb Movement Rate", bg="light green")
    Limb_Movement_Rate_l.grid(row=3, column=0, padx=10, pady=10)
    Limb_Movement_Rate_l.config(font=("times", 20, "bold"))

    # create a entry box for Limb Movement Rate
    Limb_Movement_Rate = Entry(root)
    Limb_Movement_Rate.grid(row=3, column=1, padx=10, pady=10)
    Limb_Movement_Rate.config(font=("times", 20, "bold"))

    # create a label : Enter Blood Oxygen Levels
    Blood_Oxygen_Levels_l = Label(root, text="Enter Blood Oxygen Levels", bg="light green")
    Blood_Oxygen_Levels_l.grid(row=4, column=0, padx=10, pady=10)
    Blood_Oxygen_Levels_l.config(font=("times", 20, "bold"))

    # create a entry box for Blood Oxygen Levels
    Blood_Oxygen_Levels = Entry(root)
    Blood_Oxygen_Levels.grid(row=4, column=1, padx=10, pady=10)
    Blood_Oxygen_Levels.config(font=("times", 20, "bold"))

    # create a label : Enter Eye Movement
    Eye_Movement_l = Label(root, text="Enter Eye Movement", bg="light green")
    Eye_Movement_l.grid(row=5, column=0, padx=10, pady=10)
    Eye_Movement_l.config(font=("times", 20, "bold"))

    # create a entry box for Eye Movement
    Eye_Movement = Entry(root)
    Eye_Movement.grid(row=5, column=1, padx=10, pady=10)
    Eye_Movement.config(font=("times", 20, "bold"))
    
    # create a label : Enter Heart Rate
    Heart_Rate_l = Label(root, text="Enter Heart Rate", bg="light green")
    Heart_Rate_l.grid(row=6, column=0, padx=10, pady=10)
    Heart_Rate_l.config(font=("times", 20, "bold"))

    # create a entry box for Heart Rate
    Heart_Rate = Entry(root)
    Heart_Rate.grid(row=6, column=1, padx=10, pady=10)
    Heart_Rate.config(font=("times", 20, "bold"))

    # create a label : Enter Number of Hours of Sleep
    Number_of_Hours_of_Sleep_l = Label(root, text="Enter Number of Hours of Sleep", bg="light green")
    Number_of_Hours_of_Sleep_l.grid(row=7, column=0, padx=10, pady=10)
    Number_of_Hours_of_Sleep_l.config(font=("times", 20, "bold"))

    # create a entry box for Number of Hours of Sleep
    Number_of_Hours_of_Sleep = Entry(root)
    Number_of_Hours_of_Sleep.grid(row=7, column=1, padx=10, pady=10)
    Number_of_Hours_of_Sleep.config(font=("times", 20, "bold"))


    # function to find the stress level
    def submit():
        sr = float(Snoring_Range.get())
        rr = float(Respiration_Rate.get())
        bt = float(Body_Temperature.get())
        lmr = float(Limb_Movement_Rate.get())
        bol = float(Blood_Oxygen_Levels.get())
        em = float(Eye_Movement.get())
        hr = float(Heart_Rate.get())
        n = float(Number_of_Hours_of_Sleep.get())


        # df.columns=['snoring_rate', 'respiration_rate', 'body_temperature', 'limb_movement', 'blood_oxygen', \
        #      'eye_movement', 'sleeping_hours', 'heart_rate', 'stress_level']

        # predict the stress level using knn model
        knn_prediction = knn_model.predict([[sr, rr, bt, lmr, bol, em, n, hr]])
        # predict the stress level using random forest model
        rf_prediction = rf_model.predict([[sr, rr, bt, lmr, bol, em, n, hr]])

        # display the stress level
        if knn_prediction[0] == 0:
            knn_result = "Low/Normal"
        elif knn_prediction[0] == 1:
            knn_result = "Medium Low"
        elif knn_prediction[0] == 2:
            knn_result = "Medium"
        elif knn_prediction[0] == 3:
            knn_result = "Medium High"
        elif knn_prediction[0] == 4:
            knn_result = "High"

        if rf_prediction[0] == 0:
            rf_result = "Low/Normal"
        elif rf_prediction[0] == 1:
            rf_result = "Medium Low"
        elif rf_prediction[0] == 2:
            rf_result = "Medium"
        elif rf_prediction[0] == 3:
            rf_result = "Medium High"
        elif rf_prediction[0] == 4:
            rf_result = "High"

        # display the stress level
        knn_display = Label(root, text="Stress Level predicted using KNN model is " + str(knn_result), bg="light green")
        knn_display.grid(row=9, column=0, padx=10, pady=10)   
        knn_display.config(font=("times", 20, "bold"))

        rf_display = Label(root, text="Stress Level predicted using Random Forest model is " + str(rf_result), bg="light green")
        rf_display.grid(row=10, column=0, padx=10, pady=10)
        rf_display.config(font=("times", 20, "bold"))

    
    # Submit button
    submit = Button(root, text="Submit", fg="Black", bg="Red", command=submit)
    submit.grid(row=8, column=1, padx=10, pady=10)
    submit.config(font=("times", 20, "bold"))

    # run the mainloop
    root.mainloop()

if __name__=="__main__":
    main()