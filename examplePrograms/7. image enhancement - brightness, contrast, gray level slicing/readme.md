# Demonstration of image brightness, contrast, gray level slicing manipulation techniques

## Image Brightness Manipulation:-
    Image brightness is the general measure of pixel intensity of a image. Image brightness 
    can be enhanced by adding a constant value to each pixel of the image,and can be supressed 
    by substracting a constant from each pixel of the image.
  
  ### Raw image:-
  <img src="agreabw.jpg" width="400">
    
  ### Brightness Enhanced Image (const - 50):-
  #### [brightnessEnhancement.py](https://github.com/gyan-krishna/openCV/blob/main/examplePrograms/7.%20image%20enhancement%20-%20brightness%2C%20contrast%2C%20gray%20level%20slicing/brightnessEnhancement.py)
  <img src="brightness enhancement image.jpg" width="400"> 
  
  ### Brightness Supressed Image (const - 50):-
  #### [brightnessEnhancement.py](https://github.com/gyan-krishna/openCV/blob/main/examplePrograms/7.%20image%20enhancement%20-%20brightness%2C%20contrast%2C%20gray%20level%20slicing/brightnessSuppression.py)
  <img src="brightness supression image.jpg" width="400"> 
 
## Image Contrast Manipulation:-
    Contrast of an image is the differrence between the brightest and the darkest pixel in an image.
    The contrast of an image can be manipulated by multiplying a contrast factor with each individual 
    pixel of the image. 
    contrastFactor - 
          if lies between 0 and 1 - will result in contrast supression
          if lies above 1         - will result in contrast enhancement
  #### [contrastmanipulation.py](https://github.com/gyan-krishna/openCV/blob/main/examplePrograms/7.%20image%20enhancement%20-%20brightness%2C%20contrast%2C%20gray%20level%20slicing/contrastmanipulation.py)
  ### Raw image:-
  <img src="agreabw.jpg" width="400">
    
  ### Contrast Enhanced Image (const - 1.2):-
  <img src="contrasted image (1.2).jpg" width="400"> 
  
  ### Contrast Supressed Image (const - 0.5):-
  <img src="contrasted image (0.5).jpg" width="400"> 
  
   
