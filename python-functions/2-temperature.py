def convert_to_celsius (farenhiet):
    result = ((farenhiet - 32)/9) * 5
    if result < -40:
        return round (result, 2)
    else:
        return result

    
