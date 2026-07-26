# 📖 CNN Basics – Post Class Documentation

## Overview

This document contains the resources, materials, and assignment discussed during the **CNN Basics – Introduction to Neural Networks and Convolutional Layers** session.

The session introduced the fundamentals of Neural Networks and Convolutional Neural Networks (CNNs), along with a hands-on implementation of a **Cat vs Dog Image Classification** model using TensorFlow and Keras.

---

# 📚 Topics Covered

* Introduction to Artificial Intelligence (AI)
* Machine Learning vs Deep Learning
* Neural Networks
* Artificial Neuron
* Neural Network Architecture
* Why Traditional Neural Networks are not suitable for Image Processing
* Introduction to Convolutional Neural Networks (CNNs)
* Convolution Layer
* Feature Extraction
* Batch Normalization
* Max Pooling
* Flatten Layer
* Dense Layer
* Dropout
* Binary Image Classification
* Model Training and Evaluation

---

# 💻 Hands-on Session

During the practical session, we implemented a **Cat vs Dog Image Classification** model using TensorFlow/Keras.

The notebook demonstrates:

* Loading image datasets
* Image preprocessing
* Building a CNN architecture
* Training the model
* Evaluating model performance
* Predicting custom images

### Google Colab Notebook

https://colab.research.google.com/drive/1X5MRbCI0ek6IuDp1FBXhd3lyewV_LRc3?usp=sharing

---

# 📦 Dataset

The dataset used during the session can be downloaded from Kaggle.

**Dog and Cat Classification Dataset**

https://www.kaggle.com/datasets/bhavikjikadara/dog-and-cat-classification-dataset

---

# 🛠️ Technologies Used

* Python
* TensorFlow
* Keras
* Google Colab
* NumPy
* Matplotlib

---

# 🧠 CNN Architecture Covered

```text
Input Image
      │
      ▼
Convolution Layer
      │
      ▼
Batch Normalization
      │
      ▼
Max Pooling
      │
      ▼
Convolution Layer
      │
      ▼
Batch Normalization
      │
      ▼
Max Pooling
      │
      ▼
Flatten
      │
      ▼
Dense Layer
      │
      ▼
Dropout
      │
      ▼
Output Layer (Cat / Dog)
```

---

# 📝 Assignment

Build a **Cat vs Dog Image Classification** model using the provided dataset.

### Minimum Requirements

* Load the dataset.
* Preprocess the images.
* Build a CNN model.
* Train the model.
* Evaluate the model.
* Test the model with custom images.

### Bonus Challenge

* Add more Convolution layers.
* Apply Data Augmentation.
* Experiment with different optimizers.
* Improve the validation accuracy.
* Compare your results with the baseline model.

---

# 📖 Additional Learning Resources

### TensorFlow Documentation

https://www.tensorflow.org/tutorials/images/cnn

### Keras Documentation

https://keras.io/

### Convolutional Neural Networks (Stanford CS231n)

https://cs231n.github.io/convolutional-networks/

---

# 📌 Key Takeaways

* Neural Networks can learn patterns from data.
* Traditional Neural Networks are inefficient for image data because they lose spatial information and require many parameters.
* CNNs solve this problem by using convolutional filters to automatically extract meaningful features.
* A CNN learns hierarchical representations, starting with simple edges and progressing to complex objects.
* CNNs are widely used in image classification, object detection, medical imaging, facial recognition, and autonomous systems.

---

## Thank You!

Thank you for participating in today's session.

Continue experimenting with the notebook, modify the architecture, and explore how different CNN configurations affect model performance.

**Happy Learning! 🚀**

