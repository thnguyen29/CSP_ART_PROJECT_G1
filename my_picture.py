import simple_graphics as sg

def draw_picture(width, height):
    """Draws a static picture."""

    # Bill's code (Added center logo, halfcourt line, and background
    
    # Fill the background
    sg.fill_background("#F1CC84")
    sg.half_court_line()
    sg.knicks_logo()
    
    #Right side of the court (sonny)
    
    #Sonny's changes function
    #Draw 3 point line
    sg.right_three_point_line("white")
    
    #Paint
    sg.right_paint()
    #freethrow circle
    sg.draw_circle(460, 200, 40, 2)
    
    #hoop and backboard
    sg.draw_circle(575,200,5,1)
    sg.draw_line(580,180,580,220)

    #Mario's code
    sg.draw_leftthreeline()
    sg.draw_leftinsidethree()
    
if __name__ == "__main__":
    # Launch the wrapper; only edit starting dimensions of canvas if you would like to
    sg.start(draw_picture, 600, 400)
