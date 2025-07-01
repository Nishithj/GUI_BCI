# GUI_BCI 🎯🧠

A Brain-Computer Interface (BCI) GUI for real-time cursor control using deep learning predictions. This project integrates EEG signal classification models with a graphical user interface to move a cursor based on the predicted motor imagery.

## 🧩 Overview

This project is a simulation of a BCI system where a deep learning model is trained on EEG signals (e.g., motor imagery tasks), and the real-time predictions are used to move a cursor in a GUI. The system is designed to assist or experiment with BCI cursor control frameworks.

## 🚀 Features

- ✅ Real-time cursor movement based on model outputs
- 🧠 Integration with deep learning models trained on EEG data
- 📊 Easy-to-use graphical user interface (built with `pygame`)
- 🧪 Suitable for BCI experimentation, prototyping, and testing

## 🧠 How It Works

1. EEG signals are classified into movement directions (e.g., up, down, left, right).
2. A trained deep learning model processes the EEG input.
3. The model's output is used to move a GUI-based cursor accordingly.

## 🛠️ Tech Stack

- Python
- Pygame (for GUI)
- TensorFlow / Keras (for model loading and prediction)
- NumPy, SciPy (for EEG signal processing)

## 📦 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Nishithj/GUI_BCI.git
   cd GUI_BCI
