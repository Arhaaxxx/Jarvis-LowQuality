import cv2
import mediapipe as mp
import pyautogui
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_w, screen_h = pyautogui.size()
index_y = 0
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_h, frame_w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:

            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x =  int(landmark.x * frame_w)
                y =  int(landmark.y * frame_h)
                if id == 8:
                    index_x = int(landmark.x * screen_w)
                    index_y = int(landmark.y * screen_h)
                    cv2.circle(frame, (x, y), 10, (0, 255, 255))
                    pyautogui.moveTo(index_x, index_y)
                if id == 4:
                    thumb_x = int(landmark.x * screen_w)
                    thumb_y = int(landmark.y * screen_h)
                    cv2.circle(frame, (x, y), 10, (0, 0, 255))
                if id == 12:
                    middle_x = int(landmark.x * screen_w)
                    middle_y = int(landmark.y * screen_h)
                    cv2.circle(frame, (x, y), 10, (0, 0, 255))
                    if abs(middle_y - thumb_y) < 20:
                        pyautogui.leftClick()
                        pyautogui.sleep(1)
                if id == 16:
                    ring_x = int(landmark.x * screen_w)
                    ring_y = int(landmark.y * screen_h)
                    cv2.circle(frame, (x, y), 10, (0, 0, 255))
                    if abs(ring_y - thumb_y) < 20:
                        pyautogui.rightClick()
                        pyautogui.sleep(1)
                if id == 20:
                    ring_x = int(landmark.x * screen_w)
                    ring_y = int(landmark.y * screen_h)
                    cv2.circle(frame, (x, y), 10, (0, 0, 255))
                    if abs(ring_y - thumb_y) < 20:
                        pyautogui.doubleClick()
                        pyautogui.sleep(1)
    cv2.imshow('Mouse controller', frame)
    cv2.waitKey(1)