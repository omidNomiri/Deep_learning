# Face Recognition

## Table of Contents

- [About](#about)
- [Getting Started](#getting-started)
- [Usage](#usage)

## About <a name="about"></a>

In this section, I have implemented the MLP and MLP+CNN models on four datasets.

### Accuracy in Train

|           |       MLP (Machine Learning) 😢     |        CNN + MLP (Deep Learning) 🙂   |
|---------: | :----------------: |:----------------: |
|    Mnist            |       0.9949           |        0.9979           |
|    Fashion Mnist            |        0.9092           |        0.9720           |
|    Cifar 10            |       0.4161           |        0.7290           |
|    Cifar 100            |        0.1055         |        0.4540           |  

### Accuracy in Test

|           |       MLP (Machine Learning) 😢     |        CNN + MLP (Deep Learning) 🙂   |
|---------: | :----------------: |:----------------: |
|    Mnist            |       0.9784           |        0.9882           |
|    Fashion Mnist            |        0.8763           |        0.9169           |
|    Cifar 10            |       0.4140           |        0.6385           |
|    Cifar 100            |        0.1042         |        0.3208           |  

## Getting Started <a name="getting-started"></a>

### Installation

To begin, install the required libraries by running the following command in your terminal:

```bash
pip install -r requirements.txt
```

## Usage <a name = "usage"></a>

If the requirements are installed, choose a project and run it.

### Run CNN MLP

``` terminal
jupyter nbconvert --to script CNN_MLP_compare.ipynb
```
