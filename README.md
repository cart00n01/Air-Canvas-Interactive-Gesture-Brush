# Air-Canvas-Interactive-Gesture-Brush

**Air-Canvas-Interactive-Gesture-Brush** is an interactive application that enables users to draw on a virtual canvas using hand gestures detected via webcam. No physical contact with any device is needed—just wave your hand in the air and create digital art!

## Demo

![Air Canvas Demo](demo.gif)

## Features

- **Real-time Hand Gesture Detection**: Uses computer vision to recognize hand landmarks.
- **Virtual Brush**: Draw on the screen by moving your finger in the air.
- **Color & Brush Selection**: Change brush colors and thickness with specific gestures.
- **Eraser Tool**: Easily erase parts of your drawing by switching to the eraser mode.
- **Clear Canvas**: Instantly clear the entire canvas with a gesture.

## Installation

### Prerequisites

- Python 3.7+
- Webcam

### Dependencies

Install the required libraries:

```bash
pip install opencv-python mediapipe numpy
```

## Usage

1. Clone this repository:

    ```bash
    git clone https://github.com/YOUR-USERNAME/Air-Canvas-Interactive-Gesture-Brush.git
    cd Air-Canvas-Interactive-Gesture-Brush
    ```

2. Run the application:

    ```bash
    python air_canvas.py
    ```

3. Allow access to your webcam when prompted.

4. Use your index finger to draw in the air! Explore different gestures for changing color, erasing, and clearing the canvas.

## How it Works

- **Hand Tracking**: Utilizes [MediaPipe](https://google.github.io/mediapipe/solutions/hands.html) to track hand landmarks in real time.
- **Gesture Recognition**: Detects finger positions to interpret drawing, color selection, and erase gestures.
- **Drawing Logic**: Maps finger movements to brush strokes on a virtual canvas using OpenCV.

## Controls

| Gesture                | Action                |
|------------------------|----------------------|
| Index finger up        | Draw/paint           |
| Two fingers up         | Select color/brush   |
| Fist                   | Erase                |
| Open palm              | Clear canvas         |

> *Tip: You can customize gestures and controls in the code!*

## Project Structure

```
Air-Canvas-Interactive-Gesture-Brush/
├── air_canvas.py
├── utils.py
├── README.md
├── requirements.txt
└── assets/
    └── icons/
```

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](LICENSE)

## Acknowledgements

- [MediaPipe](https://github.com/google/mediapipe)
- [OpenCV](https://opencv.org/)

---

Feel free to reach out for suggestions, issues, or feature requests!
