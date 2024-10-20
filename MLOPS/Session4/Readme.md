# Dog Breed Image Classification Project

## Overview
This project focuses on building a model to classify dog breeds using a dataset from Kaggle. The project includes creating a DataModule for handling the dataset, training a model, evaluating its performance, and running inference on new images using Docker for reproducibility.

## Dataset
- **Dataset**: [Dog Breed Image Dataset](https://www.kaggle.com/datasets/khushikhushikhushi/dog-breed-image-dataset)
- **Download Instructions**: Use the Kaggle API to download the dataset. Refer to the [Kaggle API documentation](https://www.kaggle.com/docs/api#interacting-with-datasets) for setup and usage.

## Project Structure
- `src/train.py`: Script for training the model.
- `src/eval.py`: Script for evaluating the model using a trained checkpoint.
- `src/infer.py`: Script for running inference on new images.
- `src/datamodules/dog_datamodule.py`: Script for data module
- `src/models/dog_classifier.py`: Model script
- `src/utils`: Contains script for logging
- `Dockerfile`: Docker configuration for building an image with all dependencies.
- `logs/`: Directory for storing logs and checkpoints.
- `data/`: Directory for storing the dataset.
- `samples/`: Directory for storing the samples for inferences.
- `predictions/`: Directory for storing the predictions of samples.


### Docker Image
The Docker image should include all dependencies and have your Python package installed for training, evaluation, and inference. To build the Docker image:

```bash
docker build -t emlo04session04siddharthvij10 .
```

## Using Docker

### 1. Train the Model
Train the model using the Docker image:

```bash
docker run --rm -v $(pwd)/data:/workspace/data -v $(pwd)/logs:/workspace/logs --shm-size=8g emlo04session04siddharthvij10 \
    python src/train.py
```

- **Volume Mounts**:
  - `data/` is mounted to `/workspace/data` for access to the dataset.
  - `logs/` is mounted to `/workspace/logs` for saving model checkpoints and logs.
- **Shared Memory**: Set `--shm-size=8g` to avoid memory-related errors during training.

### 2. Evaluate the Model
Evaluate the model using a saved checkpoint:

```bash
docker run --rm -v $(pwd)/data:/workspace/data -v $(pwd)/logs:/workspace/logs --shm-size=4g emlo04session04siddharthvij10 \
    python src/eval.py --checkpoint "/workspace/logs/checkpoints/dog_classifier-epoch=04-val_loss=0.01.ckpt"
```

- Ensure that the checkpoint path matches where the model checkpoint is saved in the mounted `logs` directory.

### 3. Run Inference
Run inference on new images using the trained model:

```bash
docker run --rm -v $(pwd)/data:/workspace/data -v $(pwd)/logs:/workspace/logs -v $(pwd)/predictions:/workspace/predictions --shm-size=4g emlo04session04siddharthvij10 \
    python src/infer.py --ckpt_path "/workspace/logs/checkpoints/dog_classifier-epoch=04-val_loss=0.01.ckpt" \
    --input_folder "/workspace/samples" --output_folder "/workspace/predictions"
```
## Sample Prediction

Here is an example of the model's prediction for an image:

![Sample Prediction](image.png)

- **Predicted Breed**: Beagle
- **Confidence**: 0.99

The prediction shows that the model successfully identified the breed of the dog with high confidence.

- **Additional Volume Mount**:
  - `predictions/` is mounted to `/workspace/predictions` for saving output predictions.

## Notes
- Adjust `log_every_n_steps` if you encounter logging interval warnings during training:

```python
Trainer(log_every_n_steps=10)
```

- Ensure the paths in the `docker run` commands match the structure of your local file system and the expected paths inside the Docker container.

## References
- [Kaggle API Documentation](https://www.kaggle.com/docs/api#interacting-with-datasets)
- [Dog Breed Image Dataset](https://www.kaggle.com/datasets/khushikhushikhushi/dog-breed-image-dataset)
