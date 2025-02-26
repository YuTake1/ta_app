import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import cv2
from streamlit_drawable_canvas import st_canvas
import os

MODEL_PATH = "mnist_model.h5"

# モデルをロード
@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_PATH):
        st.error("モデルファイルが見つかりません。mnist_train.py を実行して作成してください。")
        return None
    return tf.keras.models.load_model(MODEL_PATH)

model = load_model()

def preprocess_canvas(img_array):
    img = cv2.cvtColor(img_array, cv2.COLOR_RGBA2GRAY)  # グレースケール変換
    img = cv2.resize(img, (28, 28))  # MNISTサイズにリサイズ
    img = img / 255.0  # 正規化
    img = img.reshape(1, 28, 28, 1)  # モデルの入力形状に変換
    return img

st.title("MNIST 手書き数字認識アプリ")
st.write("キャンバスに手書き数字を書いて、AIに判定させまよう！")

canvas_result = st_canvas(
    fill_color="black",
    stroke_width=10,
    stroke_color="white",
    background_color="black",
    height=280,
    width=280,
    drawing_mode="freedraw",
    key="canvas"
)

if canvas_result.image_data is not None:
    img_array = np.array(canvas_result.image_data)
    processed_img = preprocess_canvas(img_array)
    
    if model:
        prediction = model.predict(processed_img)
        predicted_label = np.argmax(prediction)
        st.write(f"### 予測結果: {predicted_label}")
