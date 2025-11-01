# calculator_logic.py

def calculate_sustainability(electricity, water, transport, waste, plastic):
    """
    Calculate total sustainability score and provide suggestions.
    """

    # Score calculation
    energy_score = electricity * 0.5
    water_score = water * 0.01
    transport_score = {"Car": 10, "Bike": 5, "Bus": 3, "Walk": 0}.get(transport, 0)
    waste_score = waste * 2
    plastic_score = plastic * 1.5

    total_score = energy_score + water_score + transport_score + waste_score + plastic_score

    # Determine sustainability level
    if total_score < 50:
        message = "🌱 Excellent! You live sustainably."
        color = "#3CB371"
    elif total_score < 100:
        message = "🚴 Good job! Try to reduce your water or waste usage slightly."
        color = "#FFD700"
    else:
        message = "⚠️ High impact! Try renewable energy, carpooling, and recycling more."
        color = "#FF6347"

    scores = [energy_score, water_score, transport_score, waste_score, plastic_score]
    return total_score, message, color, scores
