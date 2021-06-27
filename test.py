import tensorflow
import keras
from keras.models import load_model

model = load_model('/root/Downloads/Facial-Expressions-Recognition-master/Emotion_little_vgg.h5')

model.summary()
