import tkinter

import input_schedule

if __name__ == '__main__':
    root = tkinter.Tk()

    root.title('Real Quest')
    root.geometry('640x360')

    label = tkinter.Label(root, text = 'Schedule')
    label.pack()

    button = tkinter.Button(root, text = 'Input Schedule', overrelief = 'solid', width = 15, command = input_schedule.add_schedule, repeatdelay = 1000, repeatinterval = 100)
    button.pack()

    root.mainloop()