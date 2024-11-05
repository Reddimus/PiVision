# Pose Detection using MediaPipe and OpenCV

## Description

This project involves using MediaPipe and OpenCV to detect human poses in an image and draw the pose landmarks. In **Task 1**, we modified the [`draw_pose`](src/main.py) function in [`main.py`](src/main.py) to draw pose landmarks on an input image and generate an output image with the landmarks overlaid.

## Objectives

- Use MediaPipe's pose estimation model to detect human poses.
- Draw pose landmarks on an image using OpenCV.

## Prerequisites

- Python 3.11+
- [OpenCV](https://pypi.org/project/opencv-python/)
- [MediaPipe](https://google.github.io/mediapipe/solutions/pose.html)

## Installation

1. **Clone this repository**:

   ```bash
   git clone [repository link]
   ```

2. **Navigate to the project directory**:

   ```bash
   cd src
   ```

3. **Optional**: Create a virtual environment:

    This repository was created using miniconda to manage the virtual environment. You can install anminiconda by following the instructions [here](https://docs.conda.io/en/latest/miniconda.html).

    To create a new virtual environment, run the following command:

    ```bash
    conda create --name <env_name> python=3.11
    ```

    To activate the virtual environment, run the following command:

    ```bash
    conda activate <env_name>
    ```

4. **Install the required packages**:

    Run the following command to install the required packages:

   ```bash
    pip install -r requirements.txt
    ```

    The `requirements.txt` file contains the following packages:

    ```txt
    pip install opencv-python
    pip install mediapipe
    ```

## Usage

1. Place the input image:

    Ensure that you have an image named `person.png` in the `src` or root directory. This image will be used as the input for pose detection.

2. Run the `main.py` script:

    Run the following command to execute the `main.py` script:

    ```bash
    python main.py
    ```

3. View the output image:

    The script will process the image, detect pose landmarks and generate an output image with the landmarks overlaid. The output image will be saved as `output.png` in the same directory.

## Task 1: Drawing Pose Landmarks on Image

In **Task 1**, we modified the `draw_pose`  function to draw the detected pose landmarks on the input image. The function uses OpenCV to:

- Draw circles at each landmark point.
- Draw lines connecting the landmarks to visualize the pose.

## Example Output

![output.png](output.png)
