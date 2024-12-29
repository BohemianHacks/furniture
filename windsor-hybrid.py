def calculate_steam_bend_parameters(bow_radius, wood_thickness):
    """
    Calculate steam bending parameters for the curved bow
    """
    # Minimum bend radius is typically 8x material thickness
    min_radius = wood_thickness * 8
    if bow_radius < min_radius:
        raise ValueError(f"Radius too tight for {wood_thickness}in stock. Minimum: {min_radius}in")
    
    # Calculate blank length needed (accounting for spring back)
    arc_length = (2 * math.pi * bow_radius) * (120 / 360)  # 120 degree arc
    spring_back_factor = 1.15  # Add 15% for spring back
    blank_length = arc_length * spring_back_factor
    
    return {
        "blank_length": round(blank_length, 1),
        "steam_time": wood_thickness * 60,  # 1 hour per inch rule of thumb
        "recommended_species": [
            "white oak",
            "ash",
            "hickory",
            "maple"
        ]
    }

def calculate_spindle_joints(bow_height, seat_depth, num_spindles):
    """
    Calculate spindle dimensions and angles
    """
    # Typical spindle taper from 5/8" to 3/8"
    base_diameter = 0.625
    top_diameter = 0.375
    
    # Calculate angles for compound drilling
    splay_angle = 15  # degrees of spindle spread
    rake_angle = 12   # degrees of backward lean
    
    # Space spindles evenly
    spacing = seat_depth / (num_spindles + 1)
    
    spindle_specs = {
        "stock_diameter": 0.75,  # Start with 3/4" square stock
        "length": bow_height + 2,  # Add 2" for tenons
        "taper": {
            "bottom": base_diameter,
            "top": top_diameter
        },
        "drilling": {
            "seat": {
                "diameter": base_diameter,
                "splay_angle": splay_angle,
                "rake_angle": rake_angle
            },
            "bow": {
                "diameter": top_diameter,
                "angle": rake_angle
            }
        },
        "spacing": spacing
    }
    
    return spindle_specs

def generate_upholstery_pattern(seat_width, seat_depth, back_height):
    """
    Calculate dimensions for upholstery pads
    """
    # Add seam allowance and padding thickness
    seam_allowance = 0.5
    padding_depth = 1
    
    patterns = {
        "seat_pad": {
            "width": seat_width + (seam_allowance * 2),
            "depth": seat_depth + (seam_allowance * 2),
            "foam_thickness": padding_depth,
            "corner_radius": 2
        },
        "back_pad": {
            "width": seat_width - 4,  # Narrower than seat
            "height": back_height - 6,  # Leave wood exposed top and bottom
            "foam_thickness": padding_depth,
            "curve_radius": bow_radius
        }
    }
    
    return patterns
