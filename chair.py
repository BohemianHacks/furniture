import math

class Chair:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth
    
    def draw_frame(self):
        # Draw the base of the chair (assuming it's a rectangular frame)
        print(f"Drawing frame: width: {self.width}, depth: {self.depth}")
        # Simulate drawing lines for the frame
        for _ in range(4):  # 4 sides of a rectangle
            print("  - Drawing side of frame")
    
    def draw_legs(self, num_legs=4):
        print(f"Drawing {num_legs} legs")
        # Simulate drawing legs at each corner
        for i in range(num_legs):
            print(f"  - Leg {i+1} at position: x: {i % 2 * self.width}, y: {i // 2 * self.depth}")
    
    def draw_backrest(self, curve_factor=0.5):
        print("Drawing backrest with a slight curve to mimic the sketch")
        # Simulate drawing a curved backrest
        for angle in range(0, 181, 10):  # 0 to 180 degrees in 10-degree increments
            x = self.width / 2 + curve_factor * math.cos(math.radians(angle)) * self.width / 4
            y = self.height - curve_factor * math.sin(math.radians(angle)) * self.height / 4
            print(f"  - Point at x: {x}, y: {y}")
    
    def assemble(self):
        self.draw_frame()
        self.draw_legs()
        self.draw_backrest()

# Create a chair similar to the sketch
my_chair = Chair(width=50, height=100, depth=50)
my_chair.assemble()
