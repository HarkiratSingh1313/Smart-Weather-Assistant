# Clothing Advice

def clothing_advice(temp):

    if temp >= 35:
        return "Wear light cotton clothes and stay hydrated."

    elif temp >= 25:
        return "Light clothing is recommended."

    elif temp >= 15:
        return "A light jacket may be comfortable."

    else:
        return "Wear warm clothes."
    


# Rain Advice

def umbrella_advice(condition):

    condition = condition.lower()

    if "rain" in condition:
        return "Carry an umbrella."

    elif "thunderstorm" in condition:
        return "Avoid outdoor activities."

    else:
        return "No umbrella needed."