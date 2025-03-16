import os

class GCodeCommand:
    def __init__(self, command, params):
        self.command = command  # e.g., "G1"
        self.params = params    # e.g., {"X": 10, "Y": 20, "F": 1500}

def parse_gcode(file_path):
    commands = []
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith(";"):  # Ignore comments
                line = line.split(";")[0] # remove in-line comments
                parts = line.split()
                command = parts[0]
                params = {}
                for part in parts[1:]:
                    key = part[0]
                    value = try_read_value(part)
                    params[key] = value
                commands.append(GCodeCommand(command, params))
    return commands

def try_read_value(part): # not all G commands has values after X, Y, Z or E notation
    if "." in part:
        try:
            return float(part[1:])
        except:
            return part[1:]
    else:
        try:
            return int(part[1:])
        except:
            return part[1:]


def analyze_gcode(commands):
    total_time = 0
    total_filament = 0
    for cmd in commands:
        if cmd.command == "G1":
            if "F" in cmd.params:  # Feedrate (speed)
                speed = cmd.params["F"]
                # Calculate time for this move (assuming linear moves)
                if "X" in cmd.params or "Y" in cmd.params or "Z" in cmd.params:
                    distance = ((cmd.params.get("X", 0)**2) + 
                                (cmd.params.get("Y", 0)**2) + 
                                (cmd.params.get("Z", 0)**2))**0.5
                    time = distance / speed
                    total_time += time
            if "E" in cmd.params:  # Extruder movement
                total_filament += abs(cmd.params["E"])
    return {"total_time": total_time, "total_filament": total_filament}

def optimize_gcode(commands):
    optimized_commands = []
    for cmd in commands:
        if cmd.command == "G1":
            # Example: Reduce speed for outer walls (simplified logic)
            if "X" in cmd.params or "Y" in cmd.params:  # Assume outer wall if X/Y movement
                cmd.params["F"] = min(cmd.params.get("F", 1000), 1000)  # Limit speed
        optimized_commands.append(cmd)
    return optimized_commands

def save_gcode(commands, output_path):
    with open(output_path, "w") as file:
        for cmd in commands:
            line = cmd.command + " " + " ".join(f"{k}{v}" for k, v in cmd.params.items())
            file.write(line + "\n")

def display_menu():
    print("\n=== G-code Parser, Analyzer, and Optimizer ===")
    print("1. Load G-code file")
    print("2. Analyze G-code")
    print("3. Optimize G-code")
    print("4. Save optimized G-code")
    print("5. Exit")

def main():
    commands = None
    optimized_commands = None
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":  # Load G-code file
            file_path = input("Enter the path to the G-code file: ")
            if os.path.exists(file_path):
                commands = parse_gcode(file_path)
                print(f"G-code file loaded successfully with {len(commands)} commands.")
            else:
                print("File not found. Please try again.")

        elif choice == "2":  # Analyze G-code
            if commands:
                analysis = analyze_gcode(commands)
                print("\nAnalysis Results:")
                print(f"Estimated Print Time: {analysis['total_time']:.2f} seconds")
                print(f"Estimated Filament Used: {analysis['total_filament']:.2f} mm")
            else:
                print("No G-code file loaded. Please load a file first.")

        elif choice == "3":  # Optimize G-code
            if commands:
                optimized_commands = optimize_gcode(commands)
                print("G-code optimized successfully.")
            else:
                print("No G-code file loaded. Please load a file first.")

        elif choice == "4":  # Save optimized G-code
            if optimized_commands:
                output_path = input("Enter the path to save the optimized G-code: ")
                save_gcode(optimized_commands, output_path)
                print(f"Optimized G-code saved to {output_path}.")
            else:
                print("No optimized G-code available. Please optimize first.")

        elif choice == "5":  # Exit
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
