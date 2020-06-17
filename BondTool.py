import tkinter as tk
import BackEnd as be


mainwindow = tk.Tk() # Window
mainwindow.title('Bond Tool')
mainwindow.iconbitmap(r'bitcoin_19t_icon.ico')


# Functions
InflReturnButton = tk.Button(
    master=mainwindow, 
    height=3, 
    text='Click to calculate Implied Inflation per year'
    )
InflReturnButton.grid(
    row=2, 
    column=0, 
    columnspan=3, 
    sticky='ew'
    )
Input = tk.Entry(
    master=mainwindow
    )
Input.insert(tk.END, '0') # sets default implied inflation
Input.grid(
    row=1, 
    column=2, 
    columnspan=1, 
    sticky='ew'
    )
InputLabel = tk.Label(
    master=mainwindow,
    text='Type Real Return in Basis Points per year:'
    )
InputLabel.grid(row=1, column=0, sticky='w', columnspan=2)




# Five Year Stuff
fiveYearFrame = tk.Frame(master=mainwindow, bg='white', relief=tk.GROOVE, borderwidth=3)


fiveYearLabel = tk.Label(
    master=fiveYearFrame, 
    text='5 Year',
    anchor='w',
    font='-weight bold'
    )
fiveYearLabel.pack(fill=tk.BOTH)
fiveYearYieldLabel = tk.Label(
    master=fiveYearFrame, 
    text = 'Current Yield: {}%'.format(str(be.fiveYearYield)),
    anchor='w'   
)
fiveYearYieldLabel.pack(fill=tk.BOTH)
fiveYearReturnLabel = tk.Label(
    master=fiveYearFrame,
    text='Real Return: {}%'.format(str(be.get_real_return(be.fiveYearYield, float(Input.get())))),
    anchor='w'
)
fiveYearReturnLabel.pack(fill=tk.BOTH)
fiveYearImpInflLabel = tk.Label(
    master=fiveYearFrame,
    text='Implied Inflation: {}%'.format(str(.01)),
    anchor='w'
)
fiveYearImpInflLabel.pack(fill=tk.BOTH)


fiveYearFrame.grid(row=0, column=0, sticky='w')
# Five Year End


# Ten Year Stuff
tenYearFrame = tk.Frame(master=mainwindow, bg='white', relief=tk.GROOVE, borderwidth=3)


tenYearLabel = tk.Label(
    master=tenYearFrame, 
    text = '10 Year',
    anchor='w',
    font='-weight bold'
    )
tenYearLabel.pack(fill=tk.BOTH)
tenYearYieldLabel = tk.Label(
    master=tenYearFrame,
    text = 'Current Yield: {}%'.format(str(be.tenYearYield)),
    anchor='w'
)
tenYearYieldLabel.pack(fill=tk.BOTH)
tenYearReturnLabel = tk.Label(
    master=tenYearFrame,
    text='Real Return: {}%'.format(str(be.get_real_return(be.tenYearYield, float(Input.get())))),
    anchor='w'
)
tenYearReturnLabel.pack(fill=tk.BOTH)
tenYearImpInflLabel = tk.Label(
    master=tenYearFrame,
    text='Implied Inflation: {}%'.format(str(.01)),
    anchor='w'
)
tenYearImpInflLabel.pack(fill=tk.BOTH)


tenYearFrame.grid(row=0, column=1)
# Ten Year End


# Thirty Year Stuff
thirtyYearFrame = tk.Frame(master=mainwindow, bg='white', relief=tk.GROOVE, borderwidth=3)


thirtyYearLabel = tk.Label(
    master=thirtyYearFrame, 
    text = '30 Year',
    anchor='w',
    font='-weight bold'
    )
thirtyYearLabel.pack(fill=tk.BOTH)
thirtyYearYieldLabel = tk.Label(
    master=thirtyYearFrame,
    text = 'Current Yield: {}%'.format(str(be.thirtyYearYield)),
    anchor='w'
)
thirtyYearYieldLabel.pack(fill=tk.BOTH)
thirtyYearReturnLabel = tk.Label(
    master=thirtyYearFrame,
    text='Real Return: {}%'.format(str(be.get_real_return(be.thirtyYearYield, float(Input.get())))),
    anchor='w'
)
thirtyYearReturnLabel.pack(fill=tk.BOTH)
thirtyYearImpInflLabel = tk.Label(
    master=thirtyYearFrame,
    text='Implied Inflation: {}%'.format(str(.01)),
    anchor='w'
)
thirtyYearImpInflLabel.pack(fill=tk.BOTH)


thirtyYearFrame.grid(row=0, column=2)
#Thirty Year End



mainwindow.mainloop()



