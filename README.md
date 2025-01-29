# GCode Parser

A lightweight Python module for parsing G-code files, commonly used in CNC machining and 3D printing. This module reads and interprets G-code commands, extracting movement instructions and machine settings from G-code files.

## Features
- Reads and parses G-code files
- Extracts commands and their parameters
- Ignores comments
- Supports common G-code commands like G1 (linear move), G0 (rapid move), and M commands (machine control)
- Supports additional G-code commands such as G2 (clockwise arc), G3 (counterclockwise arc), G4 (dwell), M5 (stop spindle), and M30 (end program)
- Simple API for integration into other Python projects
- Basic error handling for malformed G-code

## Installation
No external dependencies are required. Just clone the repository and use the script.

```sh
git clone <repo_url>
cd <repo_folder>
```

## Usage
### Parsing a G-code File
```python
from gcodeop import parse_gcode

# Path to a G-code file
gcode_file = "example.gcode"

# Parse G-code commands
commands = parse_gcode(gcode_file)

# Display parsed commands
for cmd in commands:
    print(f"Command: {cmd.command}, Params: {cmd.params}")
```

### Output Example
```
Command: G1, Params: {'X': 10, 'Y': 20, 'F': 1500}
Command: G1, Params: {'X': 30, 'Y': 40}
Command: G0, Params: {'Z': 10}
Command: M3, Params: {'S': 1000}
Command: G2, Params: {'X': 50, 'Y': 60, 'I': 10, 'J': 5}
```

## Example G-code File
```
G1 X10 Y20 F1500
G1 X30 Y40
G0 Z10
G2 X50 Y60 I10 J5
; This is a comment
M3 S1000
M5
M30
```

## Understanding G-code Commands
- **G1 X Y F** → Linear movement to X, Y at feedrate F
- **G0 X Y** → Rapid movement to X, Y
- **G2 X Y I J** → Clockwise arc movement centered at I, J
- **G3 X Y I J** → Counterclockwise arc movement centered at I, J
- **G4 P** → Dwell for P milliseconds
- **M3 S** → Spindle ON with speed S
- **M5** → Stop spindle
- **M30** → End program
- **;** → Comments in G-code files (ignored by the parser)

## Error Handling
- Detects and skips invalid or malformed G-code lines
- Logs warnings for unrecognized commands
- Ensures parameter values are correctly formatted

## License
This project is licensed under the MIT License.

## Contributions
Contributions are welcome! Feel free to submit a pull request.

## Future Enhancements
- More robust error handling and validation
- Support for additional G-code commands
- GUI-based visualization of parsed G-code
