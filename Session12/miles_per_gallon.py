import tkinter

class MilesPerGallon:
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.prompt_label_miles = tkinter.Label(self.top_frame,
                    text='Enter a Miles: ')
        self.miles_entry = tkinter.Entry(self.top_frame,
                                        width=10)

        self.prompt_label_gallons = tkinter.Label(self.top_frame,
                    text='Enter a Gallons: ')
        self.gallons_entry = tkinter.Entry(self.top_frame,
                                        width=10)

        self.prompt_label_miles.pack(side='left')
        self.miles_entry.pack(side='left')

        self.prompt_label_gallons.pack(side='left')
        self.gallons_entry.pack(side='left')

        self.descr_label = tkinter.Label(self.mid_frame,
                                         text='Converted to Miles per Gallon: ')

        self.value = tkinter.StringVar()

        self.miles_label = tkinter.Label(self.mid_frame,
                                         textvariable=self.value)

        self.descr_label.pack(side='left')
        self.miles_label.pack(side='left')

        # Create the button widgets for the bottom frame.
        self.calc_button = tkinter.Button(self.bottom_frame,
                                          text='Convert',
                                          command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)

        # Pack the buttons.
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames.
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()
    
    def convert(self):

        miles = float(self.miles_entry.get())
        gallons = float(self.gallons_entry.get())

        miles_per_gallon = miles / gallons

        self.value.set(miles_per_gallon)

if __name__ == '__main__':
    kilo_conv = MilesPerGallon()
