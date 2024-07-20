import streamlit as st
import cv2
from ultralytics import YOLO

# Load the YOLO model
model = YOLO(r'D:\sign language\final\slr_weights.pt')

def app():
    st.title("Sign Language Detection with YOLOv8")

    if 'run_detection' not in st.session_state:
        st.session_state.run_detection = False

    if 'quit_detection' not in st.session_state:
        st.session_state.quit_detection = False

    def start_detection():
        st.session_state.run_detection = True
        st.session_state.quit_detection = False

    def stop_detection():
        st.session_state.run_detection = False
        st.session_state.quit_detection = True

    st.button("Start Camera", on_click=start_detection)
    st.button("Quit", on_click=stop_detection)

    if st.session_state.run_detection and not st.session_state.quit_detection:
        detect_objects()
    else:
        st.warning("Camera feed stopped.")

def detect_objects():
    cap = cv2.VideoCapture(1)
    stframe = st.empty()

    while st.session_state.run_detection and not st.session_state.quit_detection:
        ret, frame = cap.read()

        if not ret:
            st.error("Failed to grab frame")
            break

        results = model.predict(source=frame, show=False)

        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                confidence = box.conf[0]
                class_id = box.cls[0]

                label = f"{model.names[int(class_id)]} {confidence:.2f}"

                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        stframe.image(frame)

    cap.release()
