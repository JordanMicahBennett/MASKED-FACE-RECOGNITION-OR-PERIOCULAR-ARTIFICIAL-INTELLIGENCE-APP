# MASKED-FACE-RECOGNITION-OR-PERIOCULAR-ARTIFICIAL-INTELLIGENCE-APP

Author: God Bennett ([My legal name was changed from Jordan to God.](https://www.researchgate.net/publication/342328687_Why_I_an_atheist_legally_changed_my_name_to_God))

I could not find any artificial intelligence application that did masked face recognition, so I had decided to create an ai based solution, last year in October 2020. The solution took about 5 hours to implement and I am making the code available here.


This artificial intelligence project is a masked face recognition (or periocular recognition) artificial intelligence application, built atop [this original repository](https://github.com/aakashjhawar/face-recognition-using-deep-learning), that does not do masked face recognition, as it only does recognition of faces without masks, and also, I added some neccessary fixes as the original repository did not run without said fixes.

Apart from not running due to artificial intelligence related errors (whose fixes I addressed in section "C" below), it also did not implement a graphical user interface. 

My project here resolves all of the aforementioned issues and constraints.

<img src="https://github.com/JordanMicahBennett/MASKED-FACE-RECOGNITION-OR-PERIOCULAR-ARTIFICIAL-INTELLIGENCE-APP/blob/main/Preview%201_v2.png">

<img src="https://github.com/JordanMicahBennett/MASKED-FACE-RECOGNITION-OR-PERIOCULAR-ARTIFICIAL-INTELLIGENCE-APP/blob/main/God's%20Masked%20Face%20Recognition%20Project%20Preview.gif">


# [A] Instructions_User

1. Download [the related face recognition model](https://drive.google.com/file/d/18EwXB4CQi6zvjndc5GU2JIEaZYERb7io/view?usp=sharing), and copy the .t7 file to this repository's directory on your computer.

2. Follow [B] God's installation modules.

3. To evaluate/test on model trained on God's face/masked face, run my LAUNCH_APP.bat file to evaluate "_test!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/bennett_god_clip_masked.mp4" or "_test/bennett_god_clip_unmasked.mp4" or "_test!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/holness_testing_sample_1.mp4". 

4. Press "q" to end processing of the popup video processing window, so a next video can be loaded by the main Ui.

5. Ui mode for training model coming soon.




# [A] Instructions_Developer

i. Original repository, that has errors addressed by myself in (ii) below: 

https://github.com/aakashjhawar/face-recognition-using-deep-learning

ii. God's fixed version of the base code (that didn't do masked face recognition or had a gui), is documented in section C:  "God's fixes/modifications/additions".

* This includes modfied versions of recognize_video.py, train_model.py without which several errors would occur.
    
* I also included new files for a simple gui, as seen in "recognize_video_v3_ui.py" etc.

iii. Follow my installation modules guide [B], and use my files from (ii) above in this repository (ii) above because the default code (i) failed to run without fixes in section [C] as seen in the files in this repository.

Note: ~50 masked and ~20 unmasked images were used for training for the "God" identity.
Usage: Ensure that custom training data is different from inference samples.


# [B] God's installation modules
Windows 

python 3.5 base (as advised by default repo)

scikit_learn 0.19.2 (extracted by God from recognizer.pickle, line 174 <NsS'_sklearn_version'>)

scipy 1.0.0 (extracted by God from scikit_learn webpage suggested version minimum) https://scikit-learn.org/0.19/whats_new.html

numpy 1.16.4 (installed by aiming to resolve no numpy.testing.decorators error)

* If you want to use examples in /GOD DATA + COMMANDS:

	* Download [Masked_Face_Recognition_Dataset_by_God.zip](https://drive.google.com/file/d/1BV-eArBzxDJqAO1YDzgu-1ZPrxkqgZJb/view?usp=sharing).
	
    * Copy image contents of Masked_Face_Recognition_Dataset_by_God.zip folder, to "dataset" folder this repository's directory.
    
    * Change all Python35 path locations in all batch files to yours.
    
    * Change all .py locations in all batch files to your specific locations.




# [C] God's fixes/modifications/additions
Notes about God's repairs to default repo:

--machine learning fixes:

1. Pickle errors removed from recognizer_image.py from default py files.
2. SVC Load errors from default py files fixed by dumping sklearn model in train_model.py, and loading same model in recognize_image.py
3. Code added to trigger processing of video files instead of live stream.
4. Code added to stamped picture of recognized suspect, in new overview_recognized folder.

--basic fixes:

5. Basic python print bracket errors removed from default py files.

6. Tab errors removed from default py files.



# [D] God's guidelines for setting up training data (for both masked and unmasked recognition):

1.a Take a 10 second clip of person with face masked. (Using [ii] from Suggested Tools below, if applicable)

1.b Convert clip to collection of images (using [i] from Suggested Tools below), and follow instructions to place images in dataset folder from section [A].

2.a Take a 10 second clip of person with face unmasked. (Using [ii] from Suggested Tools below, if applicable)

2.b Convert clip to collection of images (using [i] from Suggested Tools below), and follow instructions to place images in dataset folder from section [A].

Note, place all images taken from mp4 to image set conversion above, pertaining to one person, in the same person folder from [A].


Suggested Tools:

i. Mp4 to jpg collection (download resulting zip): https://ezgif.com/video-to-jpg

ii. WebCam recorder: https://webcamera.io/
