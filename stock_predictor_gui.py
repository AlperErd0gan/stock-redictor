import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Placeholder data to change with yfinance later
example_real = [150, 152, 151, 153, 155, 157]
example_predicted = [151, 151.5, 152, 154, 156, 158]
example_next_day = 159.2

class StockApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Stock Prediction App")
        self.geometry("700x500")
        
        self.frames = {}
        for F in (MainMenu, PlotPage, PredictionPage):
            frame = F(parent=self, controller=self)
            self.frames[F] = frame
            frame.place(relwidth=1, relheight=1)

        self.show_frame(MainMenu)

    def show_frame(self, page_class):
        frame = self.frames[page_class]
        frame.tkraise()
      # Varsayılan sistem rengi

def on_enter(e):
         e.widget['background'] = '#dcdcdc'  # Açık gri

def on_leave(e):
        e.widget['background'] = 'SystemButtonFace'


class MainMenu(tk.Frame):
 
        
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        title = tk.Label(self, text="Prediction of MSFT stock", font=("Helvetica", 20))
        title.pack(pady=30)

        btn1 = tk.Button(self, text="Visualize Prediction", command=lambda: controller.show_frame(PlotPage), width=30)
        btn1.pack(pady=10)
        btn1.bind("<Enter>", on_enter)
        btn1.bind("<Leave>", on_leave)

        btn2 = tk.Button(self, text="Predict Next Day", command=lambda: controller.show_frame(PredictionPage), width=30)
        btn2.pack(pady=10)
        btn2.bind("<Enter>", on_enter)
        btn2.bind("<Leave>", on_leave)


class PlotPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.grid_rowconfigure(1, weight=1) 
        self.grid_columnconfigure(0, weight=1)  

        top_frame = tk.Frame(self)
        top_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

        back_btn = tk.Button(top_frame, text="← Back to Menu", command=lambda: controller.show_frame(MainMenu))
        back_btn.pack(anchor='w')

        plot_frame = tk.Frame(self)
        plot_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)

        fig, ax = plt.subplots(figsize=(7, 4), dpi=100,constrained_layout=True)
        ax.plot(example_real, label='Real Prices', color='blue', linewidth=2)
        ax.plot(example_predicted, label='Predicted Prices', color='orange', linestyle='--', linewidth=2)
        ax.set_title("Stock Price Prediction", fontsize=14)
        ax.set_xlabel("Days")
        ax.set_ylabel("Price (USD)")
        ax.legend(loc='lower right')
        ax.grid(True)
       

        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill='both', expand=True)


class PredictionPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        back_btn = tk.Button(self, text="← Back to Menu", command=lambda: controller.show_frame(MainMenu))
        back_btn.pack(pady=10)

        label = tk.Label(self, text="Next Day Predicted Closing Price", font=("Helvetica", 16))
        label.pack(pady=20)

        price_label = tk.Label(self, text=f"${example_next_day:.2f}", font=("Helvetica", 24), fg="green")
        price_label.pack(pady=10)


# Running the app 
if __name__ == "__main__":
    app = StockApp()
    app.mainloop()
