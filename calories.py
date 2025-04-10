#Made by Arnav, incoming PhD at INRIM, Italy

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import os

# Set DISPLAY for WSL or SSH environments
if "WSL_DISTRO_NAME" in os.environ or os.getenv("SSH_CLIENT"):
    os.environ["DISPLAY"] = ":0"

# Daily Recommended Values for a 24-year-old male
DAILY_VALUES = {
    "calories": 2690,
    "protein": 120,  # g
    "fat": 70,  # g
    "carbs": 300,  # g
    "fiber": 38,  # g
    "vitamin_c": 90,  # mg
    "calcium": 1000,  # mg
    "iron": 8,  # mg
    "potassium": 3400,  # mg
    "magnesium": 400,  # mg
    "phosphorus": 700,  # mg
    "sodium": 2300,  # mg
    "zinc": 11,  # mg
    "copper": 0.9,  # mg
    "manganese": 2.3,  # mg
    "selenium": 0.055,  # mg
    "vitamin_B6": 1.3,  # mg
    "vitamin_e": 15,  # mg
    "vitamin_k": 0.120,  # mg
    "vitamin_B1": 1.2,  # mg
    "vitamin_B2": 1.3,  # mg
    "vitamin_B3": 16,  # mg
    "vitamin_B9": 0.400,  # mg
    "vitamin_B5": 5,  # mg
    "vitamin_A": 900,  # mcg
}

food_data = {
    "tofu": {"calories": 76, "protein": 23, "fat": 4.9, "carbs": 4.4, "fiber": 0.3, 
             "vitamin_c": 0, "calcium": 21.6, "iron": 4, "potassium": 121, 
             "magnesium": 56, "phosphorus": 240, "sodium": 7, "zinc": 1.54, 
             "copper": 0.378, "manganese": 1.173, "selenium": 0.0176},

    "rice": {"calories": 354, "protein": 9, "fat": 3, "carbs": 71, "fiber": 2,
             "vitamin_c": 0, "calcium": 4.31, "iron": 0.23, "potassium": 44, 
             "magnesium": 16, "phosphorus": 72, "sodium": 0, "zinc": 1.5, 
             "copper": 0.11, "manganese": 1, "selenium": 0.012},

    "soya chunks": {"calories": 330, "protein": 50, 'fat': 0.12, 'carbs': 32.05,
                    'sodium': 12, 'potassium':1500, 'fiber': 13, 'calcium': 445.31, 'iron': 20.07,
                    'vitamin_B6': 0.6, 'zinc': 5, 'magnesium': 280, 'phosphorus': 700, 
                    'vitamin_e': 0.8, 'vitamin_k': 0.0069, 'vitamin_B1':0.9, 'vitamin_B2': 0.4, 
                    'vitamin_B3':1.5, 'vitamin_B9':0.6,'vitamin_B5':0.3, 'copper': 0.9, 
                    'manganese': 2.2, 'selenium': 0.0365},

    "toor dal": {"calories": 335, "protein": 22, 'fat': 1.5, 'carbs': 63, 'fiber': 15, 
                'iron': 7.5, 'calcium': 130, 'potassium': 368, 'vitamin_e': 0.21, 
                'vitamin_k': 0.002, 'vitamin_B1': 0.64, 'vitamin_B2':  0.19, 'vitamin_B3': 2.9,
                'vitamin_B6': 0.28, 'vitamin_B9': 0.456, 'magnesium': 168, 
                'phosphorus': 367, 'sodium': 17, 'zinc': 3, 'copper': 0.89, 'manganese': 1.5},

    "cashew": {"calories": 7.189, "protein": 0.236, 'fat': 1.5 , 'carbs': 0.7, "per_piece": True},
    "almond": {"calories": 7.514, "protein": 0.273, 'fat': 0.75 , 'carbs': 0.32, 'fiber': 12.2/(100/1.5), 
               "per_piece": True},

    # "milk": {"calories": 71, "protein": 3, 'fat': 4.5 , 'carbs': 4.7},
    "roti": {"calories": 90, "protein": 11/3, "per_piece": True},
    # "oil": {"calories": 884, "protein": 0, 'vitamin_e':24, 'vitamin_k': 0.074},
    "milk": {"calories": 71, "protein": 3, 'fat': 4.5 , 'carbs': 4.7, "is_liquid": True},
    
    "oil": {"calories": 884, "protein": 0, 'vitamin_e':24, 'vitamin_k': 0.074, "is_liquid": True},
    
    "soya sauce":{"calories": 53, "protein": 8.1, "is_liquid": True},
    
    "red chilly sauce":{"calories": 165, "protein": 1.25, "is_liquid": True},
    "green chilly sauce":{"calories": 39, "protein": 3.7, "is_liquid": True},

    "walnut": {"calories": 8.5, "protein": 0.195, 'fat': 65.2/(100/1.5),  'fiber': 6.7/(100/1.5), 
                'carbs': 13.7/(100/1.5),"per_piece": True},

    "cocoa powder": {"calories": 346, "protein": 24},
    "pista":{"calories": 3.192, "protein": 0.115, 'fat': 44.8/(100/1.5),  'fiber': 9.9/(100/1.5), 
                'carbs': 29.4/(100/1.5), "per_piece": True},

    "maggi masala":{"calories": 4.1, "protein": 0.118,  'fat': 0.1,  'fiber': 0.1, 
                'carbs': 0.6, 'sodium': 218, 'iron': 4.8, 'vitamin_B9': 0.031, "per_piece": True},

    "dates":{"calories": 20, "protein": 0.2, 'sodium': 0.2, 'iron': 0.1, 'potassium': 65.6, 'carbs': 7.5,
             "per_piece": True},

    "potato": {"calories": 77, "protein": 2.05, "fat": 0.09, "carbs": 17.49,
    "fiber": 2.1, "calcium": 12, "iron": 0.81, "vitamin_B1": 0.08, "vitamin_B2": 0.03, 
    "vitamin_B3": 1.06, "vitamin_B5": 0.30, "vitamin_B6": 0.30, "vitamin_B9": 0.015,
    "vitamin_A": 2, "vitamin_E": 0.01, "vitamin_K": 0.002, "potassium": 425, "sodium": 6, "magnesium": 23, "phosphorus": 57,
    "zinc": 0.30, "copper": 0.11, "manganese": 0.15, "selenium": 0.0004},

    "cauliflower": {
    "calories": 25, "protein": 1.92, "fat": 0.28, "carbs": 4.97,
    "fiber": 2.0, "calcium": 22, "iron": 0.42,
    "vitamin_B1": 0.05, "vitamin_B2": 0.06, "vitamin_B3": 0.51, "vitamin_B5": 0.67, "vitamin_B6": 0.18, "vitamin_B9": 0.057,
    "vitamin_A": 0, "vitamin_E": 0.08, "vitamin_K": 0.0155,
    "potassium": 299, "sodium": 30, "magnesium": 15, "phosphorus": 44,
    "zinc": 0.27, "copper": 0.04, "manganese": 0.16, "selenium": 0.0006},

    "onion": {
    "calories": 40, "protein": 1.10, "fat": 0.10, "carbs": 9.34,
    "fiber": 1.7, "calcium": 23, "iron": 0.21,
    "vitamin_B1": 0.05, "vitamin_B2": 0.03, "vitamin_B3": 0.12, "vitamin_B5": 0.12, "vitamin_B6": 0.12, "vitamin_B9": 0.019,
    "vitamin_A": 2, "vitamin_E": 0.02, "vitamin_K": 0.0004,
    "potassium": 146, "sodium": 4, "magnesium": 10, "phosphorus": 29,
    "zinc": 0.17, "copper": 0.04, "manganese": 0.13, "selenium": 0.0005},

    "tomato": {
    "calories": 18, "protein": 0.88, "fat": 0.20, "carbs": 3.89,
    "fiber": 1.2, "calcium": 10, "iron": 0.27,
    "vitamin_B1": 0.04, "vitamin_B2": 0.02, "vitamin_B3": 0.59, "vitamin_B5": 0.09, "vitamin_B6": 0.08, "vitamin_B9": 0.015,
    "vitamin_A": 833, "vitamin_E": 0.54, "vitamin_K": 0.0079,
    "potassium": 237, "sodium": 5, "magnesium": 11, "phosphorus": 24,
    "zinc": 0.17, "copper": 0.06, "manganese": 0.11, "selenium": 0.0},

   "cabbage": {
    "calories": 25, "protein": 1.28, "fat": 0.10, "carbs": 5.8,
    "fiber": 2.5, "calcium": 40, "iron": 0.47,
    "vitamin_B1": 0.06, "vitamin_B2": 0.04, "vitamin_B3": 0.23, "vitamin_B5": 0.21, "vitamin_B6": 0.12, "vitamin_B9": 0.043,
    "vitamin_A": 98, "vitamin_E": 0.15, "vitamin_K": 0.076,
    "potassium": 170, "sodium": 18, "magnesium": 12, "phosphorus": 26,
    "zinc": 0.18, "copper": 0.02, "manganese": 0.16, "selenium": 0.0003},

   "banana": {
    "calories": 89, "protein": 1.09, "fat": 0.33, "carbs": 22.84,
    "fiber": 2.6, "calcium": 5, "iron": 0.26,
    "vitamin_B1": 0.03, "vitamin_B2": 0.07, "vitamin_B3": 0.67, "vitamin_B5": 0.33, "vitamin_B6": 0.37, "vitamin_B9": 0.020,
    "vitamin_A": 64, "vitamin_E": 0.10, "vitamin_K": 0.0005,
    "potassium": 358, "sodium": 1, "magnesium": 27, "phosphorus": 22,
    "zinc": 0.15, "copper": 0.08, "manganese": 0.27, "selenium": 0.001},

    "elaichi":{"calories": 0.46, "protein": 0.0165, "per_piece": True},
    "chilly powder": {"calories": 314, "protein": 12.3},
    "turmeric powder": {"calories": 354, "protein": 7.9},
    "pavbhaji masala": {"calories": 375, "protein": 12},

    "peas": {
    "calories": 81, "protein": 5.42, "fat": 0.40, "carbs": 14.45,
    "fiber": 5.1, "calcium": 25, "iron": 1.47,
    "vitamin_B1": 0.27, "vitamin_B2": 0.13, "vitamin_B3": 2.09, "vitamin_B5": 0.10, "vitamin_B6": 0.17, "vitamin_B9": 0.065,
    "vitamin_A": 765, "vitamin_E": 0.13, "vitamin_K": 0.0248,
    "potassium": 244, "sodium": 5, "magnesium": 33, "phosphorus": 108,
    "zinc": 1.24, "copper": 0.18, "manganese": 0.41, "selenium": 0.0018},

    "garlic": {
    "calories": 149, "protein": 6.36, "fat": 0.5, "carbs": 33.06,
    "fiber": 2.1, "calcium": 181, "iron": 1.70,
    "vitamin_B1": 0.20, "vitamin_B2": 0.11, "vitamin_B3": 0.70, "vitamin_B5": 0.60, "vitamin_B6": 1.24, "vitamin_B9": 0.003,
    "vitamin_A": 9, "vitamin_E": 0.08, "vitamin_K": 0.0017,
    "potassium": 401, "sodium": 17, "magnesium": 25, "phosphorus": 153,
    "zinc": 1.16, "copper": 0.30, "manganese": 1.67, "selenium": 0.0142},

    "lemon": {
    "calories": 14.5, "protein": 0.55, "fat": 0.15, "carbs": 4.66,
    "fiber": 1.4, "calcium": 13, "iron": 0.30,
    "vitamin_B1": 0.02, "vitamin_B2": 0.01, "vitamin_B3": 0.05, "vitamin_B5": 0.095, "vitamin_B6": 0.04, "vitamin_B9": 0.0055,
    "vitamin_A": 11, "vitamin_E": 0.075, "vitamin_K": 0,
    "potassium": 69, "sodium": 1, "magnesium": 4, "phosphorus": 8,
    "zinc": 0.03, "copper": 0.02, "manganese": 0.015, "selenium": 0.0002},
    
    "Coriander Cumin Powder":{"calories": 149, "protein": 6.4},
    "salt":{"calories": 0, "protein": 0, 'sodium': 36000},
    "soya sauce":{"calories": 53, "protein": 8.1},
    "brinjal":{"calories": 25, "protein": 1},
    'bhakhri':{"calories": 180, "protein": 22/3, "per_piece": True},

    "chana dal": {
    "calories": 364, "protein": 20.8, "fat": 5.3, "carbs": 61.0,
    "fiber": 15.0, "calcium": 56, "iron": 4.31,
    "vitamin_B1": 0.47, "vitamin_B2": 0.21, "vitamin_B3": 2.0, "vitamin_B5": 1.6, "vitamin_B6": 0.54, "vitamin_B9": 0.437,  # 437 µg → 0.437 mg
    "vitamin_A": 67, "vitamin_E": 0.82, "vitamin_K": 0.009,  # 9 µg → 0.009 mg
    "potassium": 846, "sodium": 24, "magnesium": 166, "phosphorus": 318,
    "zinc": 3.4, "copper": 0.98, "manganese": 2.2, "selenium": 0.0082,  # 8.2 µg → 0.0082 mg
},

    "udad dal": {
    "calories": 341, "protein": 25.0, "fat": 1.4, "carbs": 59.0,
    "fiber": 18.0, "calcium": 138, "iron": 7.57,
    "vitamin_B1": 0.42, "vitamin_B2": 0.20, "vitamin_B3": 2.3, "vitamin_B5": 1.5, "vitamin_B6": 0.28, "vitamin_B9": 0.216,  # 216 µg → 0.216 mg
    "vitamin_A": 23, "vitamin_E": 0.15, "vitamin_K": 0.004,  # 4 µg → 0.004 mg
    "potassium": 983, "sodium": 38, "magnesium": 267, "phosphorus": 379,
    "zinc": 3.4, "copper": 0.98, "manganese": 1.5, "selenium": 0.0085,  # 8.5 µg → 0.0085 mg
},
    'rajma': {
    "calories": 337, "protein": 22.5, "fat": 1.06, "carbs": 61.3,
    "fiber": 15.0, "calcium": 83, "iron": 6.69,
    "vitamin_B1": 0.61, "vitamin_B2": 0.22, "vitamin_B3": 2.1, "vitamin_B5": 0.78, "vitamin_B6": 0.4, "vitamin_B9": 0.394,  # 394 µg → 0.394 mg
    "vitamin_A": 0, "vitamin_E": 0.21, "vitamin_K": 0.0056,  # 5.6 µg → 0.0056 mg
    "potassium": 1359, "sodium": 12, "magnesium": 138, "phosphorus": 406,
    "zinc": 2.8, "copper": 0.7, "manganese": 1.1, "selenium": 0.0032,  # 3.2 µg → 0.0032 mg
},
    'shikara': {'calories': 298, 'protein': 12.5, 'carbs': 17.3, 'fiber': 2.8, 'fat': 18.8, 'sodium': 1802},
    "besan": {
    "calories": 387, "protein": 22.4, "fat": 6.7, "carbs": 57.8,
    "fiber": 10.8, "calcium": 45, "iron": 4.86,
    "vitamin_B1": 0.49, "vitamin_B2": 0.11, "vitamin_B3": 1.76, "vitamin_B5": 0.61, "vitamin_B6": 0.49, "vitamin_B9": 0.437,  # 437 µg → 0.437 mg
    "vitamin_A": 41, "vitamin_E": 0.83, "vitamin_K": 0.009,  # 9 µg → 0.009 mg
    "potassium": 846, "sodium": 64, "magnesium": 166, "phosphorus": 318,
    "zinc": 2.81, "copper": 0.91, "manganese": 1.03, "selenium": 0.0083,  # 8.3 µg → 0.0083 mg
},
"okra": {
    "calories": 33, "protein": 1.9, "fat": 0.2, "carbs": 7.5,
    "fiber": 3.2, "calcium": 82, "iron": 0.62,
    "vitamin_B1": 0.2, "vitamin_B2": 0.06, "vitamin_B3": 1.0, "vitamin_B5": 0.25, "vitamin_B6": 0.22, "vitamin_B9": 0.060,  # 60 µg → 0.060 mg
    "vitamin_A": 36, "vitamin_C": 23, "vitamin_E": 0.27, "vitamin_K": 0.031,  # 31 µg → 0.031 mg
    "potassium": 299, "sodium": 7, "magnesium": 57, "phosphorus": 61,
    "zinc": 0.58, "copper": 0.11, "manganese": 0.79, "selenium": 0.0007,  # 0.7 µg → 0.0007 mg
},
"dahi": {
    "calories": 61.5, "protein": 4, "fat": 3.1, "carbs": 4.4, "calcium": 138, "iron": 0.62,   
},
"protein shake":{
    "calories": 488.1, "protein": 38.59, "fat": 7.15, "carbs": 71.62,
    "fiber": 10.4, "calcium": 272.19, "iron": 12.6,
    "vitamin_B1": 0.57, "vitamin_B2": 0.31, "vitamin_B3": 1.57, "vitamin_B5": 0.51, "vitamin_B6": 0.73, "vitamin_B9": 0.38,
    "vitamin_A": 64, "vitamin_C": 0, "vitamin_E": 0.48, "vitamin_K": 0,
    "potassium": 1454.8, "sodium": 8.8, "magnesium": 195, "phosphorus": 442,
    "zinc": 3.15, "copper": 0.62, "manganese": 1.59, "selenium": 0.02, "per_piece": True, "unit": "serving" 
}

}


def calculate_nutrition():
    total_nutrients = {key: 0.0 for key in DAILY_VALUES.keys()}
    
    for food, var in food_vars.items():
        if var.get():
            quantity = quantity_entries[food].get()
            try:
                quantity = float(quantity)
                data = food_data[food]
                per_piece = data.get("per_piece", False)
                for nutrient in total_nutrients.keys():
                    if nutrient in data:
                        value = data[nutrient]
                        if per_piece:
                            contribution = value * quantity
                        else:
                            contribution = (value * quantity) / 100
                        total_nutrients[nutrient] += contribution
            except ValueError:
                messagebox.showerror("Input Error", f"Invalid input for {food}. Please enter a number.")
                return
    
    # Formatting the result text with comparison to daily values
    result_text = "Nutritional Totals:\n\n"
    result_text += "="*50 + "\n"
    result_text += "{:<20} {:<10} {:<10} {:<15}\n".format("Nutrient", "Consumed", "Daily Value", "% Difference")
    result_text += "="*50 + "\n"
    
    for nutrient in sorted(total_nutrients.keys()):
        consumed = total_nutrients[nutrient]
        daily_value = DAILY_VALUES[nutrient]
        if daily_value == 0:
            percentage_diff = 0.0
        else:
            percentage_diff = ((consumed - daily_value) / daily_value) * 100
        
        formatted_percent = f"{percentage_diff:+.1f}%"
        result_text += "{:<20} {:<10.2f} {:<10.2f} {}\n".format(
            nutrient.capitalize(), 
            consumed, 
            daily_value, 
            formatted_percent
        )
    
    result_area.delete(1.0, tk.END)
    result_area.insert(tk.INSERT, result_text)

# GUI setup
if "DISPLAY" in os.environ or os.name == "nt":
    root = tk.Tk()
    root.title("Food Nutrition Calculator")
    root.geometry("600x800")

    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Canvas and Scrollbar for food list
    canvas = tk.Canvas(main_frame)
    scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    food_vars = {}
    quantity_entries = {}
    for food in food_data.keys():
        var = tk.BooleanVar()
        food_vars[food] = var
        frame_food = tk.Frame(scrollable_frame)
        frame_food.pack(anchor='w', pady=2)
        chk = tk.Checkbutton(frame_food, text=food, variable=var)
        chk.pack(side='left')
        entry = tk.Entry(frame_food, width=5)
        entry.pack(side='left', padx=5)
        
        # Get food data and determine unit
        data = food_data[food]
        custom_unit = data.get("unit", None)
        is_liquid = data.get("is_liquid", False)
        per_piece = data.get("per_piece", False)
        
        unit = custom_unit or ("ml" if is_liquid else ("pieces" if per_piece else "g"))
        
        tk.Label(frame_food, text=unit).pack(side='left')
        quantity_entries[food] = entry

    # Calculate button and result area
    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=5)
    tk.Button(btn_frame, text="Calculate Nutrition", command=calculate_nutrition).pack()

    result_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=25)
    result_area.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    root.mainloop()
else:
    print("GUI cannot be displayed. Please run this script on a graphical system.")