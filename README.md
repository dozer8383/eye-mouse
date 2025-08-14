# Eye Mouse!
You're _still_ using your arm and hand to move a decades-old computing peripheral just to point and click? Cut out all that latency with Eye Mouse! It only requires a webcam and the eyes you're already using!

##### Disclaimer: Eye Mouse is far from perfect and really isn't that great at the moment. This is almost exclusively a fun novelty and will not make you more productive, only less.

# Installation and Setup
1. Install EyeTrax and PyAutoGui with `pip install eyetrax` and `pip install pyautogui`.
2. Get the code for Eye Mouse with `git clone https://github.com/dozer8383/eye-mouse/`.
3. `cd eye-mouse` and then run `python3 purelaziness.py`.
4. Calibration should begin with a green dot on a full black screen. Look at each of the green dots appearing. It's important to not move your head during this calibration to improve the results.
5. After calibration, there are three more dots that will tune the smoothing algorithm.
6. After tuning, the cursor will begin to follow your gaze shortly.

# Usage
Look to point, blink (see tips below) to click.

# Tips for usage
- Most important: the more contrast your eyes have with your face, the better. When possible, get a lamp or similar to light your face from the front.
- Get your webcam closer to your face. Make sure most of your face is visible, but you want as much detail as possible to help track subtle eye movements.
- The higher resolution your webcam is, the better.
- Avoid moving your head during calibration or use, as this makes the eye tracking more inaccurate. **However**, these inaccuracies can be fixed by focusing on a point on the screen and moving your head until the cursor returns to *roughly* the same area you're focusing on. This requires some practice.
- Eye Mouse saves your eye movements in a model file that can be reused, but given that any amount of head movement will increase eye tracking error, it's best to delete the model file before every run.
- When you blink, it's hard to see anything (crazy, I know). This makes clicking on things kind of difficult, since you have to point precisely and then close your eyes for a second, not knowing if you hit your target. Squinting will also trigger a click, and lets you see while you're doing it.
- **One last really helpful tip**: increase the interface scaling in your OS to make buttons bigger and easier to click.
