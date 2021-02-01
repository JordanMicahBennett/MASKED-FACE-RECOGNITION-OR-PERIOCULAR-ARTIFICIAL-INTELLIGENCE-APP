# import libraries
import os
import cv2
import imutils
import time
import pickle
import numpy as np
from imutils.video import FPS
from imutils.video import VideoStream
from imutils.video import FileVideoStream


# load serialized face detector
print("Loading Face Detector...")
protoPath = "face_detection_model/deploy.prototxt"
modelPath = "face_detection_model/res10_300x300_ssd_iter_140000.caffemodel"
detector = cv2.dnn.readNetFromCaffe(protoPath, modelPath)

# load serialized face embedding model
print("Loading Face Recognizer...")
embedder = cv2.dnn.readNetFromTorch("openface_nn4.small2.v1.t7")

# load the actual face recognition model along with the label encoder
"""
God's modification

Description: This solves the SVC Object has no attribute probability error upon trying to do inference/recognition on image,
...due to model modules mismatch problems. Original authors did not specify original libraries.

Solution flow:
1. Generate embeddings after installing all dependencies on current machine.
2. Alter train_model.py, such that model is dumped over training dependencies. (simple dump of sklearn job)
3. Alter recognize_image.py such that new model is loaded.
"""
from joblib import load #Code added by God
recognizer = load('model_v2.joblib') #pickle.loads(open("output/recognizer.pickle", "rb").read(), encoding = 'bytes')
le = pickle.loads(open("output/le.pickle", "rb").read())

# initialize the video stream, then allow the camera sensor to warm up
INPUT_FILE_NAME = "_test/bennett_god_clip_unmasked.mp4"
# Create an output movie file (make sure resolution/frame rate matches input video!)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')



print("Starting Video Stream...")
vs = FileVideoStream(path=INPUT_FILE_NAME).start() #Modifed by God to use FileVideoStream(path=, instead of VideoStream(src=, for stored instead of live video feed.
#time.sleep(2.0)

# start the FPS throughput estimator
fps = FPS().start()


#God's way of controlling how many overview image samples are printed per identified target
DISCOVERY_COUNT = 0


# loop over frames from the video file stream
while True:
	# grab the frame from the threaded video stream
	frame = vs.read()

	# resize the frame to have a width of 600 pixels (while maintaining the aspect ratio), and then grab the image dimensions
	frame = imutils.resize(frame, width=600)
	(h, w) = frame.shape[:2]

	# construct a blob from the image
	imageBlob = cv2.dnn.blobFromImage(
		cv2.resize(frame, (300, 300)), 1.0, (300, 300),
		(104.0, 177.0, 123.0), swapRB=False, crop=False)

	# apply OpenCV's deep learning-based face detector to localize faces in the input image
	detector.setInput(imageBlob)
	detections = detector.forward()

	# loop over the detections
	for i in range(0, detections.shape[2]):
		# extract the confidence (i.e., probability) associated with the prediction
		confidence = detections[0, 0, i, 2]

		# filter out weak detections
		if confidence > 0.5:
			# compute the (x, y)-coordinates of the bounding box for the face
			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int")

			# extract the face ROI
			face = frame[startY:int(endY-(.27*endY)), startX:endX]
			(fH, fW) = face.shape[:2]

			# ensure the face width and height are sufficiently large
			if fW < 20 or fH < 20:
				continue

			# construct a blob for the face ROI, then pass the blob through our face embedding model to obtain the 128-d quantification of the face
			faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255,
				(96, 96), (0, 0, 0), swapRB=True, crop=False)
			embedder.setInput(faceBlob)
			vec = embedder.forward()

			# perform classification to recognize the face
			preds = recognizer.predict_proba(vec)[0]
			j = np.argmax(preds)
			proba = preds[j]
			name = le.classes_[j]
			


			DISCOVERY_COUNT += 1


			# dump image with recognized target
			if ( DISCOVERY_COUNT < 2 ):
                                cv2.imwrite("overview_recognized/Recognized_Unmasked_Suspect=%s__videoStamp=%d_seconds.jpg" % (name, cv2.CAP_PROP_FRAME_COUNT), face)

			# draw the bounding box of the face along with the associated probability
			text = "{}: {:.2f}%".format(name, proba * 100)
			y = startY - 10 if startY - 10 > 10 else startY + 10
			cv2.rectangle(frame, (startX, startY), (endX, endY),
				(0, 0, 255), 2)
			cv2.putText(frame, text, (startX, y),
				cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

	# update the FPS counter
	fps.update()


	# show the output frame
	cv2.imshow("God's project is now processing : %s" % INPUT_FILE_NAME, frame)
	key = cv2.waitKey(1) & 0xFF

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

	# Write the resulting image to the output video file
	#height, width, channels = frame.shape
	#out = cv2.VideoWriter("output_test.mp4", fourcc, 29.97, (width, height))
	#out.write(frame)
		
# stop the timer and display FPS information
fps.stop()
print("Elasped time: {:.2f}".format(fps.elapsed()))
print("Approx. FPS: {:.2f}".format(fps.fps()))

# cleanup
out and out.release()
cv2.destroyAllWindows()
vs.stop()
