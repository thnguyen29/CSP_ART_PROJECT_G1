import simple_graphics as sg

def draw_picture(width, height):
    """Draws a static picture."""

    # Bill's code (Added center logo, halfcourt line, and background
    
    # Fill the background
    sg.fill_background("#F1CC84")
    sg.half_court_line()
    sg.knicks_logo()
    
    #Right side of the court (sonny)
    
    #Draw 3 point line
    sg.set_line_thickness(2)
    sg.set_outline_color("white")
    sg.draw_line(500,40,600,40)
    sg.draw_line(500,360,600,360)
    sg.draw_curve( [(500,40), (300,200), (500,360)] )
    
    #inner paint
    sg.set_fill_color("#DC8535")
    sg.fill_rectangle(460, 160, 200, 80)
    
    #Outer paint
    sg.draw_line(460,140,460,260)
    sg.draw_line(460,140,600,140)
    sg.draw_line(460,260,600,260)
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
