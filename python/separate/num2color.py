# ANSI Escape Codes for Colors
COLOR_CODES = {
    # Tip / Base Colors
    "White": "\033[47m",   # White 
    "Red": "\033[101m",    # Bright Red 
    "Black": "\033[40m",   # Black 
    "Yellow": "\033[103m",        # Bright Yellow 
    "Violet": "\033[45m",         # Magenta/Violet 
    
    # Ring / Stripe Colors
    "Blue": "\033[44m",           # Blue 
    "Orange": "\033[43m",         # Yellow/Orange 
    "Green": "\033[42m",          # Green text
    "Brown": "\033[41m",          # Dark Red/Brown 
    "Slate": "\033[100m",         # Dark Gray/Slate 
    
    # Reset code to return terminal to normal
    "Reset": "\033[0m"
}

binder_units_colors = ["White", "Red", "Black", "Yellow", "Violet", "Blue", "Orange", "Green", "Brown", "Slate"]
tip_unit_colors = ["White", "Red", "Black", "Yellow", "Violet"]
ring_unit_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]


print("\n--- Pair Number to Telco Colour Code ---")

# User Input Selection
while True:
    try:
        pair = int(input("Enter a valid telco pair number: "))
        if pair < 1:
            raise ValueError("Value cannot be less than 1")
        elif pair > 6000:
            raise ValueError("Value cannot be greater than 6000")
        break  # Extis the loop if the number is valid
    except ValueError as e:
        print("That wasn't a valid whole number Between 1 and 4200. Please try again.")

# 1. Super Binder (600 pairs each)
super_index = (pair - 1) // 600
super_binder = binder_units_colors[super_index]
super_binder_color = f"{COLOR_CODES[super_binder]}{super_binder}{COLOR_CODES['Reset']}"


# 2. Local Binder Group inside that Super Unit (25 pairs each)
remaining_in_super = (pair - 1) % 600
binder_tip_index = remaining_in_super // 125
binder_ring_index = remaining_in_super % 125 // 25
binder_tip = tip_unit_colors[binder_tip_index]
binder_ring = ring_unit_colors[binder_ring_index]
print(f"{binder_tip_index=} {binder_ring_index=}")
binder_tip_color = f"{COLOR_CODES[binder_tip]}{binder_tip}{COLOR_CODES['Reset']}"
binder_ring_color = f"{COLOR_CODES[binder_ring]}{binder_ring}{COLOR_CODES['Reset']}"

# 3. Conductor Pair (Standard 25-pair matrix)
pair_index = remaining_in_super % 25
tip = tip_unit_colors[pair_index // 5]
ring = ring_unit_colors[pair_index % 5]
tip_color = f"{COLOR_CODES[tip]}{tip}{COLOR_CODES['Reset']}"
ring_color = f"{COLOR_CODES[ring]}{ring}{COLOR_CODES['Reset']}"


print("\n========================================")
print(f"Success! Ready to calculate colors for pair: {pair}")
print(f"Super: {super_binder_color} -> Binder: {binder_tip_color}/{binder_ring_color} -> Wires: {tip_color}/{ring_color}")
print("========================================")
