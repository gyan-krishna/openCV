# Pendulum tracking using opencv
##### WORK IN PROGRESS!
<img src="screen shots/screenshot1.jpg" width="1000">

## Aim of the project:
  1. track the motion of the pendulum
  2. plot the sin wave of the pendulum
  3. calculate the time period, frequency etc of the pendulum.
 
## Tracking the pendulum:-
  1. For yellow ball:- <br/>
    i. convert each frame to hsv format <br/>
    ii. isolate saturation channel <br/>
    iii. perfom thresholding on the saturation channel <br/>
   2. For green/red/blue ball:- <br/>
    i. extract green channel of the frame <br/>
    ii. perform binary thresholding on the green channel <br/>
  3. use HoughCircles algorithm on the binary image and find the location and radius of the ball<br/>
  4. perform analysis on the data gathered and plot it.
