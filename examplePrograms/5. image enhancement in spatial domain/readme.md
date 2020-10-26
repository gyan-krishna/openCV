# Image Enhancement in Spatial Domain

--------------------------------------------------------------------------------------------
# 1. Image Negative
  Image negative is produced by subtracting each pixel from the maximum intensity value
  the transformation function used in image negative is,

  #### **s = T(r) = L – 1 – r**

  ### Raw Image
  <img src="minions_raw.jpg" width="400"> 
  
  ### Negative Image
  <img src="negativeImg.jpg" width="400">
  
--------------------------------------------------------------------------------------------
# 2. Log Transformation 
 Log transformation is done on gray scale image where, all pixels are replaced with log of 
 the pixel, this method is used to expand darker pixels of an image as compaired to higher
 pixel values.
 The formulas needed for log conversion is:-
 #### **const = 255 / log(max_input_pixel_value)**
 The constant is chosen such that maximun voutput value corrosponding to the bit size used.
 #### **op_pixel = const * log(ip_pixel)**
 however pre-procressing should be done on the input image such that no pixel has 0 value,
 since log(0) = inf will result in a exception, simply replace all pixels with 0 value with 1
 ### Raw Image
 <img src="minions_raw.jpg" width="400"> 
  
 ### Log Transformed Image
 <img src="log transformation.jpg" width="400">
 
 --------------------------------------------------------------------------------------------
# 3. Power Law/ Gamma Transformation:-
  Gamma transformation is done on an image where, it is important for displaying images on a 
  screen correctly, to prevent bleaching or darkening ofimages when viewed from diffent monitors
  and display settings. it is done since our eyes perceive a gamma shaped curved instead of a 
  linear curve. the formula for gamma transofrmation is:-
  #### **opImg = const * ipImg ^ gammaConst**
  
  where, gamma constant is a constant used to specify the intensity of gamma correction.
  
  ### Raw Image
  <img src="minions_raw.jpg" width="400"> 
  
  ### Gamma Image with gamma = 0.5
  <img src="gamma transformation image - 0.5.jpg" width="400"> 
  
  ### Gamma Image with gamma = 1.5
  <img src="gamma transformation image - 1.5.jpg" width="400"> 
  
  ### Gamma Image with gamma = 3.5
  <img src="gamma transformation image - 3.5.jpg" width="400"> 
 
 --------------------------------------------------------------------------------------------
  
