# Image Arithmethic in OpenCV

## Image Addition:-
Image addition is the procress of superimposing an image on top of another.
It can be done in two methods:-<br/>
### 1. Weighted Addition:- <br/>
	in this method of addition, a weight is associated with it that will denote
	its significance in the final image. The weight lies between 0 and 1. <br/>
	Python code to perform weighted addition:- <br/>
**OPImage = cv2.addWeighted(img1, weight1, img2, weight2, gamma)**

### 2. Non Weighted Addition:- <br/>
	In this method of addition, both images has a 0.5 weight associated with it
	i.e. both image will have equal significance in the output image.
	Python code to perform non weighted addition:- <br/>
**OPImage = cv2.add(img1, img2)**			
				
#### Image One:-
<img src="nebula.jpg" width=400>

#### Image Two:-
<img src="rocket.jpg" width=400>

#### Weighted Addition Results:-
<img src="weightedSum.jpg" width=400>

#### Non Weighted Addition Results:-
<img src="NonWeightedSum.jpg" width=400>
