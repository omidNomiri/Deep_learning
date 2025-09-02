# CNN Regression Projects

In this part we have two deep learning regression projects using Convolutional Neural Networks (CNNs):

- **Age Prediction from Face Images** (using UTKFace dataset)
- **House Price Prediction** (using images and tabular data)

---

## 2. Age Prediction from Face Images

Predicts age from face images using the UTKFace dataset and a CNN (ResNet50 backbone).

### Age Prediction Dataset

[UTKFace Dataset](https://www.kaggle.com/jangedoo/utkface-new)

- Images named as `{age}_{gender}_{date}.jpg`
- Age labels extracted from filenames

### How to Run Age Prediction notebook

1. Install requirements:

    ```bash
    pip install -r requirements.txt
    ```

2. Open and run all cells in [`age_prediction.ipynb`](age_prediction.ipynb)

---

## 1. House Price Prediction

Predicts house prices using **images of houses** (frontal, bedroom, bathroom, kitchen) and **tabular data** (bedrooms, bathrooms, area, zipcode).

### Approaches

- Simple CNN on images + tabular data
- ResNet50 (pre-trained) on images + tabular data

### House Price Prediction Dataset

[Houses Dataset](https://github.com/emanhamed/Houses-dataset)

- Images for each house: bathroom, bedroom, kitchen, frontal view
- Tabular data: bedrooms, bathrooms, area, zipcode, price

### How to Run House Price Prediction notebook

1. Install requirements:

    ```bash
    pip install -r requirements.txt
    ```

2. Open and run all cells in [`house_price.ipynb`](house_price.ipynb)

### Results

| Model              | Test MAE (USD) |
| ------------------ | -------------- |
| ResNet50 + Tabular | ~214,150       |

### Features

- Data loading and preprocessing
- Age distribution visualization
- Model: ResNet50 + custom regression head
- Early stopping and learning rate scheduling
- Predict age for a sample image

---

## Requirements

See [`requirements.txt`](requirements.txt) for dependencies.
