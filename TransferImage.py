import tensorflow_hub as hub
import tensorflow as tf
import numpy as np
import cv2


def load_image(img_path):
        img = tf.io.read_file(img_path)
        img = tf.image.decode_image(img, channels=3)
        img = tf.image.convert_image_dtype(img, tf.float32)
        img = img[tf.newaxis, :]
        return img

def transfer(content_path, style_path):
    print("[INFO] Loading the Model")

    # model = hub.load("https://www.kaggle.com/models/google/arbitrary-image-stylization-v1/TensorFlow1/256/2")
    model = hub.load("arbitrary-image-stylization-v1-tensorflow1-256-v2/")

    print("[INFO] Model Loaded")
    
    style_image =  load_image(style_path)
    content_image =  load_image(content_path)

    print("[INFO] Images Pre processed")

    transfer_image = model(tf.constant(content_image), tf.constant(style_image))[0]

    print("[INFO] Style Transfered")

    cv2.imwrite("generated_img.jpg", cv2.cvtColor(np.squeeze(transfer_image)*255, cv2.COLOR_BGR2RGB))
    output = {}
    output["output_file_path"] = "generated_img.jpg"
    output["status_code"] = "200"
    return output


# print("[INFO] Calling the Functyion")
# print(transfer("images/scene.jpg", "images/leo.jpg"))