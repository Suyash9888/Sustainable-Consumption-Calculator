# ui_components.py
import tkinter as tk
from tkinter import ttk, messagebox
from calculator_logic import calculate_sustainability
from chart_visualizer import show_chart


class SustainabilityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌿 Sustainable Consumption Calculator")
        self.root.geometry("620x550")
        self.root.config(bg="#E8F5E9")

        self.create_header()
        self.create_form()
        self.create_buttons()
        self.create_result_area()
        # self.create_footer()

    # -----------------------
    # Header
    # -----------------------
    def create_header(self):
        header = tk.Label(self.root, text="🌍 Sustainable Consumption Calculator",
                          font=("Helvetica", 18, "bold"), bg="#388E3C", fg="white", pady=10)
        header.pack(fill="x")

    # -----------------------
    # Input Form
    # -----------------------
    def create_form(self):
        self.frame = tk.Frame(self.root, bg="#E8F5E9", padx=20, pady=20)
        self.frame.pack(pady=10)

        self.electricity_entry = self.create_field("Electricity Usage (kWh/month):", 0)
        self.water_entry = self.create_field("Water Usage (liters/day):", 1)
        self.transport_combo = self.create_dropdown("Main Mode of Transport:", 2, ["Car", "Bike", "Bus", "Walk"])
        self.waste_entry = self.create_field("Waste Generated (kg/week):", 3)
        self.plastic_entry = self.create_field("Plastic Items Used (per week):", 4)

    def create_field(self, label_text, row):
        tk.Label(self.frame, text=label_text, font=("Arial", 12), bg="#E8F5E9").grid(row=row, column=0, sticky="w", pady=5)
        entry = tk.Entry(self.frame, width=25)
        entry.grid(row=row, column=1, pady=5)
        return entry

    def create_dropdown(self, label_text, row, options):
        tk.Label(self.frame, text=label_text, font=("Arial", 12), bg="#E8F5E9").grid(row=row, column=0, sticky="w", pady=5)
        combo = ttk.Combobox(self.frame, values=options, width=22, state="readonly")
        combo.set("Select")
        combo.grid(row=row, column=1, pady=5)
        return combo

    # -----------------------
    # Buttons
    # -----------------------
    def create_buttons(self):
        button_frame = tk.Frame(self.root, bg="#E8F5E9")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Calculate Footprint", command=self.calculate,
                  bg="#43A047", fg="white", font=("Arial", 12, "bold"), width=18, relief="raised").grid(row=0, column=0, padx=10)

        tk.Button(button_frame, text="Reset", command=self.reset,
                  bg="#00897B", fg="white", font=("Arial", 12, "bold"), width=10, relief="raised").grid(row=0, column=1, padx=10)

        tk.Button(button_frame, text="Exit", command=self.root.destroy,
                  bg="#E53935", fg="white", font=("Arial", 12, "bold"), width=10, relief="raised").grid(row=0, column=2, padx=10)

    # -----------------------
    # Result Display
    # -----------------------
    def create_result_area(self):
        self.result_label = tk.Label(self.root, text="", font=("Arial", 14, "bold"), bg="#E8F5E9")
        self.result_label.pack(pady=10)

        self.suggestion_label = tk.Label(self.root, text="", font=("Arial", 12, "italic"),
                                         bg="#E8F5E9", wraplength=500)
        self.suggestion_label.pack(pady=5)

    # def create_footer(self):
        # footer = tk.Label(self.root,
        #                   text="Developed for SDG 12 – Responsible Consumption and Production",
        #                   font=("Arial", 10, "italic"), bg="#C8E6C9", fg="black", pady=5)
        # footer.pack(side="bottom", fill="x")

    # -----------------------
    # Actions
    # -----------------------
    def calculate(self):
        try:
            electricity = float(self.electricity_entry.get())
            water = float(self.water_entry.get())
            transport = self.transport_combo.get()
            waste = float(self.waste_entry.get())
            plastic = float(self.plastic_entry.get())

            total, message, color, scores = calculate_sustainability(electricity, water, transport, waste, plastic)

            self.result_label.config(text=f"Your Sustainability Score: {total:.2f}", fg=color)
            self.suggestion_label.config(text=message, fg=color)

            show_chart(scores)

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for all fields.")

    def reset(self):
        self.electricity_entry.delete(0, tk.END)
        self.water_entry.delete(0, tk.END)
        self.waste_entry.delete(0, tk.END)
        self.plastic_entry.delete(0, tk.END)
        self.transport_combo.set("Select")
        self.result_label.config(text="")
        self.suggestion_label.config(text="")
