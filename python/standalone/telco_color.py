#!/usr/bin/env python3
# (c) Shane McDonald - 2026

# ANSI Escape Codes for Colors
COLOR_CODES = {
	# Tip / Base Colors
	"White": "\033[47m",          # White 
	"Red": "\033[101m",           # Bright Red 
	"Black": "\033[40m",          # Black 
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

# Telco Color Names
super_binder_unit_colors = ["White", "Red", "Black", "Yellow", "Violet", 
	"Blue", "Orange", "Green", "Brown", "Slate"]
tip_unit_colors = ["White", "Red", "Black", "Yellow", "Violet"]
ring_unit_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]

# Main - Select between Converting Numbers to Colors or vice-versa
def main():
	while True:
		print("\n--- Main Menu ---")
		print("1. Numbers to Colours")
		print("2. Colours to Numbers")
		print("3. Exit")
		
		choice = input("Please select an option (1-3): ").strip()
		
		if choice == '1':
			num2color()
			
		elif choice == '2':
			color2num()
			
		elif choice == '3':
			print("\nExiting. Goodbye!")
			break
		else:
			print("\nInvalid choice. Please enter 1, 2, or 3.")

# Telco Number to Color Function
def num2color():

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
	
	# 1. Super Binder Colors (600 pairs each)
	# REMEMBER SUBTRACT ONE AT THE BEGINNING IN NUMBER TO COLOR
	super_binder_index = (pair - 1) // 600
	
	# 2. Local Binder Colors  (125 pairs for tip AND 25 pairs for ring)
	remaining_in_super = (pair - 1) % 600
	binder_tip_index = remaining_in_super // 125
	binder_ring_index = remaining_in_super % 125 // 25
	
	# 3. Wire Pair Colors (5 pairs for tip and 1 pair for ring)
	pair_index = remaining_in_super % 25
	tip_index = pair_index // 5
	ring_index = pair_index % 5
	
	# 4. Print the final answer
	printTelco(pair, super_binder_index, binder_tip_index, binder_ring_index, tip_index, ring_index)

# Telco Color to Number
def color2num():
	
	print("\n--- Telco Colour Code to Pair Number ---")
	
	# Helper function to let users pick safely from a list
	def get_choice(menu_title, options_list):
		print(f"\n--- Select {menu_title} ---")
		for i, option in enumerate(options_list):
			print(f"[{i + 1}] {COLOR_CODES[option]}{option}{COLOR_CODES['Reset']}")
			
		while True:
			try:
				choice = int(input(f"Enter number (1-{len(options_list)}): "))
				if 1 <= choice <= len(options_list):
					return choice - 1  # Convert to 0-based index
				print(f"Out of range. Please choose between 1 and {len(options_list)}.")
			except ValueError:
				print("Invalid input. Please enter a whole number.")
				
	
	# 2. Get the 5 individual user inputs via separate menus
	super_binder_index = get_choice("1. Super Binder", super_binder_unit_colors)
	binder_tip_index = get_choice("2. Binder Tip Color", tip_unit_colors)
	binder_ring_index = get_choice("3. Binder Ring Color", ring_unit_colors)
	conductor_tip_index = get_choice("4. Conductor Tip Color", tip_unit_colors)
	conductor_ring_index = get_choice("5. Conductor Ring Color", ring_unit_colors)
	
	# Validate and map the separate binder tip/ring selections to the valid 24-binder group index
	if binder_tip_index == 4 and binder_ring_index == 4:
		invalid_binder_text = (
			f"{COLOR_CODES[tip_unit_colors[4]]}{tip_unit_colors[4]}{COLOR_CODES['Reset']}/"
			f"{COLOR_CODES[ring_unit_colors[4]]}{ring_unit_colors[4]}{COLOR_CODES['Reset']}"
			)
		print(f"\nError: {invalid_binder_text} is not a valid 600-pair binder group combination.")
		return
	
	# 3. Reverse Math Calculation 
	# REMEMBER ADD ONE AT THE END FOR COLOR TO NUMBER
	binder_index = binder_tip_index * 125 + binder_ring_index * 25
	conductor_index = (conductor_tip_index * 5) + conductor_ring_index
	pair = (super_binder_index * 600) + binder_index + (conductor_index + 1)
	
	# 4. Print the final answer
	printTelco(pair, super_binder_index, binder_tip_index, binder_ring_index, conductor_tip_index, conductor_ring_index)
	
# Print Uniformed Output for color2num and num2color()
def printTelco(pair, super_binder_index, binder_tip_index, binder_ring_index, tip_index, ring_index):
	
	# Super Binder Color String
	super_binder_string = super_binder_unit_colors[super_binder_index]
	super_binder_string_formatted = f"{COLOR_CODES[super_binder_string]}{super_binder_string}{COLOR_CODES['Reset']}"
	
	# Binder Tip and Ring Color String
	binder_tip_string = tip_unit_colors[binder_tip_index]
	binder_ring_string = ring_unit_colors[binder_ring_index]
	binder_tip_string_formatted = f"{COLOR_CODES[binder_tip_string]}{binder_tip_string}{COLOR_CODES['Reset']}"
	binder_ring_string_formatted = f"{COLOR_CODES[binder_ring_string]}{binder_ring_string}{COLOR_CODES['Reset']}"\
	
	# Tip and Ring Color String
	tip_string = tip_unit_colors[tip_index]
	ring_string = ring_unit_colors[ring_index]
	tip_color_string_formatted = f"{COLOR_CODES[tip_string]}{tip_string}{COLOR_CODES['Reset']}"
	ring_color_string_formatted = f"{COLOR_CODES[ring_string]}{ring_string}{COLOR_CODES['Reset']}"
	
	# 4. Print Output
	print("\n========================================")
	print(f"Success! The pair: {pair}")
	print(f"Super: {super_binder_string_formatted} \
	-> Binder: {binder_tip_string_formatted}/{binder_ring_string_formatted} \
	-> Wires: {tip_color_string_formatted}/{ring_color_string_formatted}")
	print("========================================")

# Main - Program Entry Point
if __name__ == "__main__":
	main()
