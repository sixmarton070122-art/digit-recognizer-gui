# Digit Recognizer GUI

A simple `tkinter` desktop app that lets you draw a digit (0–9) by hand and get a live prediction from a CNN trained on MNIST.

This is the sibling project of [digit-recognizer-ai](../digit-recognizer-ai), where the CNN model was built and trained from scratch using PyTorch. This repo takes the trained model and wraps it in a small drawing interface.

## Current Status

* ✅ Drawing canvas (28×28 grid, scaled up for easier drawing)
* ✅ Left-click to draw, right-click to erase
* ✅ Loads a pretrained model from `digit-recognizer-ai`
* ✅ Live prediction on demand via a "Predict" button
* ✅ Clear canvas button

## Project Structure

```
.
├── main.py          # Tkinter GUI: canvas, drawing, prediction
├── model.py         # CNN architecture (DigitClassifier) — must match the trained model
└── models/          # Trained model weights (.pth files), copied over from digit-recognizer-ai
```

## How It Works

* The canvas is a 28×28 grid (scaled ×10 for visibility) that mirrors the MNIST image format.
* Left-click and drag paints pixels, gradually darkening them; right-click and drag erases.
* Clicking **Predict** converts the grid into a tensor, runs it through the loaded `DigitClassifier` model, and displays the predicted digit.
* Clicking **Clear** resets the canvas and the underlying pixel grid.

## Model Architecture

Same CNN as in `digit-recognizer-ai`:

* 2 convolutional layers (16 → 32 channels, 3×3 kernels, padding=1), each followed by ReLU and max pooling
* 2 fully connected layers narrowing down to 10 output classes (digits 0–9)

The `model.py` in this repo must stay in sync with the one used to train whatever weights are loaded, since `load_state_dict` requires matching architecture.

## Requirements

* Python 3
* PyTorch
* NumPy
* Tkinter (included with most standard Python installs)

Install dependencies:

```
pip install torch numpy
```

## Usage

1. Copy a trained model file (e.g. `test_maxp.pth`) from `digit-recognizer-ai` into a local `models/` folder.
2. Make sure the `model_name` variable in `main.py` matches the filename you're loading.
3. Run the app:

```
python main.py
```

4. Draw a digit on the canvas with the left mouse button.
5. Click **Predict** to see the model's guess.
6. Click **Clear** to start over.

## Planned Next Steps

* Show prediction confidence alongside the predicted digit
* Better preprocessing to more closely match MNIST centering/normalization
* Smoother brush strokes / anti-aliasing on the canvas

## Related Project

* [digit-recognizer-ai](../digit-recognizer-ai) — trains the CNN on MNIST and evaluates its accuracy
