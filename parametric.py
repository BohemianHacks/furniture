import FreeCAD
import Part
import Sketcher

# Define parameters
w = 500  # Width of seat in mm
d = 500  # Depth of seat in mm
h = 450  # Height of seat from floor in mm
r_backrest = 300  # Radius of backrest curve in mm
h_backrest = 400  # Height of backrest from seat in mm
h_armrest = 200  # Height of armrest from seat in mm
t_seat = 10  # Thickness of seat in mm
t_backrest = 10  # Thickness of backrest in mm
t_armrest = 10  # Thickness of armrest in mm
leg_d = 50  # Diameter of leg in mm
leg_h = 450  # Height of leg in mm
leg_offset = 50  # Offset of leg from edge in mm

# Create a new document
doc = FreeCAD.newDocument()

# Create seat sketch
seat_sketch = doc.addObject('Sketcher::SketchObject', 'SeatSketch')
seat_sketch.Placement = FreeCAD.Placement(FreeCAD.Vector(0, 0, 0), FreeCAD.Rotation(FreeCAD.Vector(0, 0, 1), 0))
seat_sketch.addGeometry(Part.LineSegment(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(w, 0, 0)), False)
seat_sketch.addGeometry(Part.LineSegment(FreeCAD.Vector(w, 0, 0), FreeCAD.Vector(w, d, 0)), False)
seat_sketch.addGeometry(Part.LineSegment(FreeCAD.Vector(w, d, 0), FreeCAD.Vector(0, d, 0)), False)
seat_sketch.addGeometry(Part.LineSegment(FreeCAD.Vector(0, d, 0), FreeCAD.Vector(0, 0, 0)), False)
# Add constraints to make it a rectangle
seat_sketch.addConstraint(Sketcher.Constraint('Coincident', 0, 2, 1, 1))
seat_sketch.addConstraint(Sketcher.Constraint('Coincident', 1, 2, 2, 1))
seat_sketch.addConstraint(Sketcher.Constraint('Coincident', 2, 2, 3, 1))
seat_sketch.addConstraint(Sketcher.Constraint('Coincident', 3, 2, 0, 1))
seat_sketch.addConstraint(Sketcher.Constraint('Horizontal', 0))
seat_sketch.addConstraint(Sketcher.Constraint('Horizontal', 2))
seat_sketchOops, something broke. Talk to me later?
