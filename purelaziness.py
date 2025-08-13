from eyetrax import GazeEstimator, run_9_point_calibration # pyright: ignore[reportMissingImports]
from eyetrax.calibration import run_lissajous_calibration, run_5_point_calibration # pyright: ignore[reportMissingImports]
from eyetrax.calibration.adaptive import run_adaptive_calibration # pyright: ignore[reportMissingImports]
from eyetrax.filters import KalmanSmoother, make_kalman # pyright: ignore[reportMissingImports]
import pyautogui # pyright: ignore[reportMissingModuleSource]
import cv2

pyautogui.PAUSE = 0.01

f = 0

cursoravgx = []
cursoravgy = []

estimator = GazeEstimator()
try:
    estimator.load_model("gaze_model.pkl")
except:
    print("Model not found, please calibrate first.")
    run_9_point_calibration(estimator)
    # run_adaptive_calibration(estimator)
    # run_lissajous_calibration(estimator)
    estimator.save_model("gaze_model.pkl")

kalman = make_kalman()
smoother = KalmanSmoother(kalman)
smoother.tune(estimator)

cap = cv2.VideoCapture(0)

while True:
    # Extract features from frame
    ret, frame = cap.read()
    features, blink = estimator.extract_features(frame)

    # Predict screen coordinates
    if features is not None and not blink:
        x, y = estimator.predict([features])[0]
        # print(f"Gaze: ({x:.0f}, {y:.0f})")
        cursoravgx.append(x)
        cursoravgy.append(y)
        if f > 0:
            f -= 1

    # if f > 0:
    #     stringthing = ""
    #     for i in range(0, f):
    #         stringthing += "█"
    #     print("    Blink! " + stringthing)

    avgx = sum(cursoravgx) / len(cursoravgx) if cursoravgx else 0
    avgy = sum(cursoravgy) / len(cursoravgy) if cursoravgy else 0
    if len(cursoravgx) > 15:
        cursoravgx.pop(0)

    if len(cursoravgy) > 15:
        cursoravgy.pop(0)

    if features is not None and blink:
        f += 1
        if f > 20:
            f = 0
            pyautogui.click()
    else:
        pyautogui.moveTo(avgx, avgy)

