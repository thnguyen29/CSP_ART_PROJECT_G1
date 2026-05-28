import simple_graphics as sg

def draw_picture(width, height):
    """Draws a static picture."""

    # Bill's code (Added center logo, halfcourt line, and background
    
    # Fill the background
    sg.fill_background("#F1CC84")
    
    # Halfcourt line
    sg.set_outline_color("white")
    sg.draw_line(300,0,300,400, 2)

    # draw circle for logo
    sg.set_line_thickness(10)
    sg.set_fill_color("#DC8535")
    sg.set_outline_color("#34569B")
    sg.fill_circle(300, 200, 60)

    # Draw Y
    sg.set_outline_color("black")
    sg.draw_line(300,250,300,195, 8)
    sg.draw_line(270,160,300,200, 8)
    sg.draw_line(330,160,300,200, 8)

    # Draw N
    sg.draw_line(260,175,260,225, 8)
    sg.draw_line(260,180,280,220, 8)
    sg.draw_line(280,175,280,225, 8)

    # Draw K
    sg.draw_line(320,175,320,225, 8)
    sg.draw_line(320,200,340,225, 8)
    sg.draw_line(320,200,340,175, 8)
    
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
    
    #freethrow circle
    sg.draw_circle(460, 200, 40, 2)
    
    #hoop and backboard
    sg.draw_circle(575,200,5,1)
    sg.draw_line(580,180,580,220)
    
    # Mario's code (Left side of the court)
    # draw upper left 3pt corner line
    sg.set_line_thickness(2)
    sg.set_outline_color("white")
    
    #Three point line
    sg.draw_line (0,40,100,40,2)
    sg.draw_line (0,360,100,360,2)
    sg.draw_curve([(100,40),(300,200),(100,360)])
    
    # Inner Paint
    sg.set_fill_color("#DC8535") # Color Knicks Orange
    sg.fill_rectangle (0,160,140,80)
    
    # Outer Paint
    sg.draw_rectangle (0,140,140,120)
    # Free Throw Circle
    sg.draw_circle (140,200,40,2)
    
    #Basketball hoop
    sg.draw_line (20,180,20,220,1)
    sg.draw_circle (25,200,5,2)
    
if __name__ == "__main__":
    # Launch the wrapper; only edit starting dimensions of canvas if you would like to
    sg.start(draw_picture, 600, 400)
