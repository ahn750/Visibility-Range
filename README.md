# Visibility-Range
Calculates Visibility Range in a hazy scene using given landmarks

# Requirements: 
Python 3

# package installation:
1. Download the repository, open cmd and navigate inside the downloaded folder 
2. run the given command: 'pip install -r requirements.txt'


# Running the script
1. Open the script and add image location in place of 'sample_image/smog.jpg' on line 5.
2. Inside the repository run the command: 'python visrange.py'
3. An image will appear. Click on the top left and bottom right corners of the landmark you want to choose.
4. A dialogue box asking for landmark distance will appear. Enter the landmark distance. Repeat for every landmark
![Choose landmarks](/sample_image/entertext2.jpg)
5. Once all landmarks are marked press any key to continue
6. An output image with landmarks classified as 'visible', 'not visible' or 'barely visible' along with the visibility range will appear.
![Choose landmarks](/sample_image/smog_out.jpg)
7. The visibility range value will also be saved in a seperate text file 'visrange.txt'.






