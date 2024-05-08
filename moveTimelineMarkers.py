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

# First argument is the time multiplier e.g.:
# original marker frame number is 100, multiplier is 1.1
# -> marker will be moved to frame 100 * 1.1 = F110
# Second argument is bool:
# False to move all the scene's markers
# True to move only selected markers 
moveMarkers(1.1, False)