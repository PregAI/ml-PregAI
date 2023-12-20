# ml-PregAI

## Table of Contents
1. [Introduction](#introduction)
2. [Dataset](#dataset)
3. [Model Architecture](#model-architecture)
4. [Evaluation](#evaluation)
5. [Further Work](#further-work)

## Introduction
This project utilizes MoveNet, a machine learning-based model for human pose estimation. MoveNet is designed to predict key points on the human body, providing valuable information for various applications such as yoga pose classification. MoveNet is the state-of-the-art pose estimation model that can detect these 17 key-points:
- Nose
- Left and right eye
- Left and right ear
- Left and right shoulder
- Left and right elbow
- Left and right wrist
- Left and right hip
- Left and right knee
- Left and right ankle

## Dataset
The dataset used for training and evaluation consists of a collection of images containing various yoga poses. Each image is labeled with the corresponding yoga pose category. The dataset consists of 9 classes, each containing 800 images. The images are labeled with different yoga poses, contributing to a diverse set for training the model. The dataset was carefully curated and balanced to ensure a representative training sample.

**Source datasets:**
- [Tensorflow](http://download.tensorflow.org/data/pose_classification/yoga_poses.zip)
- [Kaggle](https://www.kaggle.com/datasets/niharika41298/yoga-poses-dataset)
- [Yoga-82](https://sites.google.com/view/yoga-82/home)

**Merged datasets download link:**
[Dataset](https://drive.google.com/drive/folders/1klZkO1hui1argoJYnOc6rMppXTCrGFT8?usp=sharing)

*Dataset Structure:*
- Yoga Poses
  - Downdog
    - 00000128.jpg
    - 00000181.jpg
    - ...
  - Goddess
    - 00000243.jpg
    - 00000306.jpg
    - ...

## Model Architecture
MoveNet employs a deep learning architecture optimized for human pose estimation. This project leverages MoveNet Thunder, a powerful variant of the MoveNet architecture, to conduct human pose estimation. MoveNet Thunder excels in predicting key points on the human body, forming the cornerstone for accurate yoga pose classification in our machine learning model.

## Evaluation
The model's performance was evaluated using a comprehensive set of metrics, including accuracy, precision, recall, and F1 score. The achieved accuracy of 98.21% demonstrates the model's ability to accurately classify yoga poses on the test dataset. Further accuracy improvement to 98.28% is observed after converting the model to TFLite and applying dynamic range quantization.

## Further Work
Future improvements and extensions to this project may include:

- Expanding the dataset
- Fine-tuning the model for specific yoga poses.
- Exploring additional augmentation techniques for better generalization.

Feel free to contribute to the project or suggest enhancements!
