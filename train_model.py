# USAGE
# python train_model.py --embeddings output/embeddings.pickle --recognizer output/recognizer.pickle --le output/le.pickle

# import the necessary packages
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import argparse
import pickle

# load the face embeddings
print("[INFO] loading face embeddings...")
data = pickle.loads(open("output/embeddings.pickle", "rb").read())

# encode the labels
print("[INFO] encoding labels...")
le = LabelEncoder()
labels = le.fit_transform(data["names"])

# train the model used to accept the 128-d embeddings of the face and
# then produce the actual face recognition
print("[INFO] training model...")
recognizer = SVC(C=1.0, kernel="linear", probability=True)
recognizer.fit(data["embeddings"], labels)


"""
God's modification

Description: This solves the SVC Object has no attribute probability error upon trying to do inference/recognition on image,
...due to model modules mismatch problems. Original authors did not specify original libraries.

Solution flow:
1. Generate embeddings after installing all dependencies on current machine.
2. Alter train_model.py, such that model is dumped over training dependencies. (simple dump of sklearn job)
3. Alter recognize_image.py such that new model is loaded.
"""
from joblib import dump #Code added by God
dump(recognizer, 'model_v2.joblib')  #Code added by God

# write the actual face recognition model to disk
f = open("output/recognizer", "wb")
f.write(pickle.dumps(recognizer))
f.close()

# write the label encoder to disk
f = open("output/le.pickle", "wb")
f.write(pickle.dumps(le))
f.close()
print("[INFO] model training complete...")
