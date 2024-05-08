import bpy

def moveMarkers(time_multiplier, move_selected):
    # Ensure timeline_markers are accessible
    if bpy.context.scene.timeline_markers:
        # Select all markers

        # Iterate over timeline_markers
        for marker in bpy.context.scene.timeline_markers:
            
            current_frame = marker.frame
            move_to_frame = current_frame * time_multiplier
            
            # Check for selected markers
            if marker.select and move_selected:
                
                marker.frame = int(move_to_frame)
                
            # Move all markers
            else:
                
                marker.frame = int(move_to_frame)

    else:
        print("No timeline markers found")

moveMarkers(1.1, False)