import tkinter as tk
import time

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        self.time_left = 0
        self.is_running = False
        self.create_widgets()

    def create_widgets(self):
        self.time_display = tk.Label(self.root, font=("Arial", 30), width=10, height=2, relief="sunken")
        self.time_display.pack(pady=20)

        self.time_entry = tk.Entry(self.root, font=("Arial", 20), width=10)
        self.time_entry.pack(pady=20)

        start_button = tk.Button(self.root, text="Start", font=("Arial", 20), command=self.start_timer)
        start_button.pack(side="left", padx=20)

        stop_button = tk.Button(self.root, text="Stop", font=("Arial", 20), command=self.stop_timer)
        stop_button.pack(side="right", padx=20)

    def update_timer(self):
        if self.is_running and self.time_left > 0:
            self.time_left -= 1
            self.time_display.config(text=str(self.time_left))
            self.root.after(1000, self.update_timer)
        elif self.time_left == 0:
            self.is_running = False
            self.time_display.config(text="Time's Up!")

    def start_timer(self):
        try:
            self.time_left = int(self.time_entry.get())
            self.is_running = True
            self.time_display.config(text=str(self.time_left))
            self.update_timer()
        except ValueError:
            self.time_display.config(text="Invalid Input")

    def stop_timer(self):
        self.is_running = False
        self.time_display.config(text="Timer Stopped")

def main():
    root = tk.Tk()
    timer = CountdownTimer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
