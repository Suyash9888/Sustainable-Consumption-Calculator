# chart_visualizer.py
import matplotlib.pyplot as plt

def show_chart(values):
    categories = ['Energy', 'Water', 'Transport', 'Waste', 'Plastic']
    plt.figure(figsize=(6, 4))
    plt.bar(categories, values, color=['#4CAF50', '#00BFFF', '#FFD700', '#FF8C00', '#FF69B4'])
    plt.title("Your Environmental Footprint Breakdown")
    plt.xlabel("Category")
    plt.ylabel("Impact Score")
    plt.tight_layout()
    plt.show()
