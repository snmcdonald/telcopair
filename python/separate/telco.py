#!/usr/bin/env python3

import subprocess
import sys
from pathlib import Path

def main():
    # Get the exact folder where this script is located
    script_dir = Path(__file__).resolve().parent
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Numbers to Colours")
        print("2. Colours to Numbers")
        print("3. Exit")
        
        choice = input("Please select an option (1-3): ").strip()
        
        if choice == '1':
            target_script = script_dir / "num2color.py"
            #print(f"\nRunning {target_script.name}...")
            try:
                subprocess.run([sys.executable, str(target_script)], check=True)
            except FileNotFoundError:
                print(f"Error: Could not find '{target_script.name}' in: {script_dir}")
            except subprocess.CalledProcessError as e:
                print(f"The script finished with an error: {e}")
                
        elif choice == '2':
            target_script = script_dir / "color2num.py"
            #print(f"\nRunning {target_script.name}...")
            try:
                subprocess.run([sys.executable, str(target_script)], check=True)
            except FileNotFoundError:
                print(f"Error: Could not find '{target_script.name}' in: {script_dir}")
            except subprocess.CalledProcessError as e:
                print(f"The script finished with an error: {e}")
                
        elif choice == '3':
            print("\nExiting. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
