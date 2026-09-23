### Project 13 — `project13/README.md`
# Project 13 - SIFT Feature Matching and Homography

## Description

This project demonstrates feature detection and feature matching using the SIFT algorithm with OpenCV.

The program detects SIFT keypoints and descriptors in two images, matches them using FLANN, filters the best matches with Lowe's Ratio Test, and uses Homography with RANSAC to locate the first image inside the second image.

## Requirements

* Python
* OpenCV
* NumPy
* Matplotlib

## How to Run

```bash
python opencv_project.py
```

## Features

* SIFT Keypoint Detection
* SIFT Descriptor Computation
* FLANN Feature Matching
* Lowe's Ratio Test
* Homography Estimation
* RANSAC
* Perspective Transformation
* Image Matching and Localization

## Output

<img width="1920" height="1080" alt="Screenshot (19)" src="https://github.com/user-attachments/assets/4232a065-ca24-47da-94f3-7059c888f13c" />
