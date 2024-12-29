import FreeCAD
import Part

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

# Create seat
seat = Part.makeBox(w, d, t_seat)

# Create backrest as an arc extruded
backrest_curve = Part.makeCircle(r_backrest, FreeCAD.Vector(w/2, d, h), FreeCAD.Vector(0, 0, 1), 0, 180)
backrest = backrest_curve.extrude(FreeCAD.Vector(0, 0, h_backrest))

# Create legs
leg1 = Part.makeCylinder(leg_d/2, leg_h, FreeCAD.Vector(leg_offset, leg_offset, 0))
leg2 = Part.makeCylinder(leg_d/2, leg_h, FreeCAD.Vector(w-leg_offset, leg_offset, 0))
leg3 = Part.makeCylinder(leg_d/2, leg_h, FreeCAD.Vector(leg_offset, d-leg_offset, 0))
leg4 = Part.makeCylinder(leg_d/2, leg_h, FreeCAD.Vector(w-leg_offset, d-leg_offset, 0))

# Combine all parts
chair = Part.makeCompound([seat, backrest, leg1, leg2, leg3, leg4])

# Display the model
Part.show(chair)