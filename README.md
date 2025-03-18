# Triangle Checker and Visualizer

A Python script that checks if three given side lengths can form a valid triangle and visualizes the triangle using matplotlib.

## Features
- Validates if three positive numbers can form a triangle using the triangle inequality theorem
- Plots the triangle with given side lengths using matplotlib
- Interactive command-line interface
- Visual output with labeled vertices and filled triangle shape

## Prerequisites
- Python 3.x
- Required libraries:
  - matplotlib
  - numpy

## Installation
1. Clone the repository:
```bash
git clone https://github.com/your-username/triangle-checker.git
```
2. Install required dependencies:
```bash
pip install matplotlib numpy
```

## Usage
Run the script and follow the prompts:
```bash
python triangle_checker.py
```

1. Enter three positive numbers when prompted
2. The program will:
   - Check if the numbers can form a valid triangle
   - Display a message indicating if a triangle is possible
   - If valid, show a plot of the triangle
3. Choose to try again or exit

## Example
```
Welcome to Triangle Checker!
Enter three positive numbers to see if they form a triangle
Enter side a: 3
Enter side b: 4
Enter side c: 5

Yes, 3.0, 4.0, 5.0 can form a triangle!
[Triangle plot appears]
```

## Code Structure
- `is_valid_triangle(a, b, c)`: Validates triangle possibility using triangle inequality theorem
- `plot_triangle(a, b, c)`: Creates a visualization of the triangle using calculated coordinates
- `main()`: Handles user interaction and program flow

## Output
- The triangle is plotted with:
  - Magenta outline and light fill
  - Labeled vertices (P1, P2, P3)
  - Grid background
  - Equal aspect ratio for accurate representation

## Limitations
- Requires positive numbers as input
- May encounter floating-point precision issues with very large or very small numbers

## Contributing
Feel free to fork this repository and submit pull requests with improvements!

## License
[MIT License](LICENSE)
```

To use this README:
1. Create a file named `README.md` in your repository
2. Copy and paste this content
3. Replace `your-username` with your actual GitHub username
4. Save the file as `triangle_checker.py` (or adjust the usage section if you choose a different filename)
5. Consider adding a `LICENSE` file if you want to specify licensing terms
