import tkinter as tk

def conv(giris):
    try:
        sonuc = eval(giris)
        return str(sonuc)
    except Exception as e:
        return "Error"

def sonuc(giris):
    return(conv(giris))

# Function to get the input and display it
def retrieve_input():
    input_value = input_box.get()  # Get the value from the input box
    output_label.config(text="İşlem: " + input_value + "\n" + "Cevap: " + sonuc(input_value))

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("450x223")

# Create an input box (Entry widget)
input_box = tk.Entry(root, width=40, font=("Helvetica", 16), justify="center")
input_box.pack(pady=20)  # Add some padding for better layout

# Create a button to submit the input
submit_button = tk.Button(root, text="Submit", command=retrieve_input)
submit_button.pack(pady=10)

# Create a label to display the output
output_label = tk.Label(root, text="", font=("Helvetica", 16))
output_label.pack(pady=20)

# Start the main loop
root.mainloop()
