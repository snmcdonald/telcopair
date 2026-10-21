print("\n--- Telco Colour Code to Pair Number ---")

# 1. Define reference lists
super_units = ["White", "Red", "Black", "Yellow", "Violet", "Blue", "Orange", "Green", "Brown", "Slate"]
tip_colors = ["White", "Red", "Black", "Yellow", "Violet"]
ring_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]

# Generate the 24 standard binder group combinations (omitting Violet/Slate for standard 600-pair counts)
binder_colors = []
for t in tip_colors:
    for r in ring_colors:
        if not (t == "Violet" and r == "Slate"):
            binder_colors.append(f"{t}/{r}")

# Helper function to let users pick safely from a list
def get_choice(menu_title, options_list):
    print(f"\n--- Select {menu_title} ---")
    for i, option in enumerate(options_list):
        print(f"[{i + 1}] {option}")
        
    while True:
        try:
            choice = int(input(f"Enter number (1-{len(options_list)}): "))
            if 1 <= choice <= len(options_list):
                return choice - 1  # Convert to 0-based index
            print(f"Out of range. Please choose between 1 and {len(options_list)}.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

# 2. Get the 5 individual user inputs via separate menus
super_index = get_choice("1. Super Binder", super_units)
binder_tip_index = get_choice("2. Binder Tip Color", tip_colors)
binder_ring_index = get_choice("3. Binder Ring Color", ring_colors)
conductor_tip_index = get_choice("4. Conductor Tip Color", tip_colors)
conductor_ring_index = get_choice("5. Conductor Ring Color", ring_colors)

# Validate and map the separate binder tip/ring selections to the valid 24-binder group index
binder_string = f"{tip_colors[binder_tip_index]}/{ring_colors[binder_ring_index]}"
if binder_string not in binder_colors:
    print(f"\nError: {binder_string} is not a valid 600-pair binder group combination.")
    exit()

binder_index = binder_colors.index(binder_string)
conductor_index = (conductor_tip_index * 5) + conductor_ring_index

# 3. Reverse Math Calculation
pair_number = (super_index * 600) + (binder_index * 25) + (conductor_index + 1)

# 4. Print the final answer
print("\n========================================")
print(f"SUCCESS! The matching telco pair is: {pair_number}")
print(f"Super: {super_units[super_index]} -> Binder: {binder_string} -> Pair: {tip_colors[conductor_tip_index]}/{ring_colors[conductor_ring_index]}")
print("========================================")
