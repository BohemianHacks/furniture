import math
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Point3D:
    x: float
    y: float
    z: float

@dataclass
class WoodComponent:
    species: str
    thickness: float
    width: float
    length: float
    grain_direction: str = "longitudinal"

class HybridWindsorChair:
    def __init__(self, width: float, height: float, depth: float):
        self.width = width
        self.height = height
        self.depth = depth
        self.bow_radius = width * 0.8  # Bow curve radius
        self.spindles: List[Point3D] = []
        self.attachment_points: List[Point3D] = []

    def calculate_bow_blank(self) -> WoodComponent:
        # Calculate required length for steam bending
        arc_angle = math.radians(120)  # 120° bow arc
        arc_length = self.bow_radius * arc_angle
        spring_back_factor = 1.15
        
        return WoodComponent(
            species="white oak",
            thickness=0.75,  # 3/4" thick
            width=1.5,       # 1.5" wide
            length=arc_length * spring_back_factor
        )

    def calculate_spindle_positions(self, num_spindles: int) -> List[Point3D]:
        spindles = []
        spacing = self.width / (num_spindles + 1)
        
        for i in range(num_spindles):
            x = spacing * (i + 1)
            # Calculate y position along bow curve
            y = self.height - math.sqrt(
                self.bow_radius**2 - (x - self.width/2)**2
            )
            # Add splay angle
            z = self.depth * 0.3 * (0.5 - abs(0.5 - i/(num_spindles-1)))
            spindles.append(Point3D(x, y, z))
        
        return spindles

    def calculate_upholstery_points(self) -> Tuple[List[Point3D], List[Point3D]]:
        """Calculate attachment points for seat and back upholstery"""
        seat_points = [
            Point3D(x, self.height * 0.3, z)
            for x in [0.1, 0.9]
            for z in [0.1, 0.9]
        ]
        
        back_points = []
        for t in [0.3, 0.6, 0.9]:  # Height positions
            y = self.height * t
            # Calculate x position along bow curve
            x = self.width/2 + self.bow_radius * math.cos(math.asin(t))
            back_points.append(Point3D(x, y, self.depth * 0.8))
            
        return seat_points, back_points

    def generate_cut_list(self) -> List[WoodComponent]:
        cut_list = []
        
        # Bow back
        cut_list.append(self.calculate_bow_blank())
        
        # Spindles (assuming 7 spindles)
        for _ in range(7):
            cut_list.append(WoodComponent(
                species="maple",
                thickness=0.75,
                width=0.75,
                length=self.height * 0.6  # Spindle length
            ))
        
        # Seat blank
        cut_list.append(WoodComponent(
            species="maple",
            thickness=1.75,
            width=self.width,
            length=self.depth,
            grain_direction="quarter-sawn"
        ))
        
        return cut_list

    def generate_drilling_angles(self) -> dict:
        """Calculate compound angles for spindle joints"""
        return {
            "seat": {
                "rake": 12,    # Backward lean
                "splay": 15    # Side spread
            },
            "bow": {
                "rake": 12,    # Match seat rake
                "splay": 0     # No splay at top
            }
        }

# Example usage
chair = HybridWindsorChair(width=24, height=32, depth=20)
cut_list = chair.generate_cut_list()
spindles = chair.calculate_spindle_positions(7)
seat_points, back_points = chair.calculate_upholstery_points()
drilling_angles = chair.generate_drilling_angles()
