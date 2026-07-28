---
title: SCVD Violence Intelligence Dashboard
emoji: 🎯
colorFrom: blue
colorTo: red
sdk: gradio
app_file: app.py
pinned: false
license: cc-by-nc-sa-4.0
---

# SCVD Violence Intelligence Dashboard

An explainable CCTV video-analysis dashboard for classifying video segments as
**Normal**, **Violence**, or **Weaponized Violence**.

## Live demo

The permanent deployment link will be added here after the Render deployment.

The interface includes `test.mp4`, so reviewers can test the full workflow
without supplying their own video.

> The free deployment may sleep after a period of inactivity. The first request
> after sleep can take about one minute while the service starts.

## Features

- ResNet18 + two-layer LSTM video classifier
- Sliding temporal-window analysis
- Interactive probability chart
- Incident timeline with start and end times
- Detailed segment-level probability table
- YOLO person detection during alert scenes
- Downloadable annotated video
- Structured Arabic explanation
- Downloadable HTML incident report

## System pipeline

```text
CCTV video
   ├── Temporal windows → 16 frames → ResNet18 → LSTM
   │                                    ↓
   │                    Normal / Violence / Weaponized
   │                                    ↓
   │                       Smoothing + event merging
   │
   └── YOLO person detector ────────────┐
                                        ↓
               Dashboard + timeline + annotated video + report
```

## Important limitation

The SCVD model classifies temporal video segments. YOLO only identifies people
present in an alert scene. A bounding box does **not** prove that the person
inside it is the aggressor.

## Run locally

```bash
pip install -r requirements.txt
python app.py
```

Required files:

- `best_model.pth`
- `SCVD_Professional_GUI.py`
- `app.py`
- `test.mp4`

## Dataset

[Smart-City CCTV Violence Detection Dataset (SCVD)](https://www.kaggle.com/datasets/toluwaniaremu/smartcity-cctv-violence-detection-dataset-scvd)

The dataset is distributed under the **CC BY-NC-SA 4.0** license. Cite the
original SCVD authors and associated paper when using this project.
