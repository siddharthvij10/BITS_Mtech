Assignment
 

Add Dockerfile for the project
Create a DevContainer for the Project
Docker Image should have your package installed
Use this dataset: https://www.kaggle.com/datasets/khushikhushikhushi/dog-breed-image-datasetLinks to an external site.
You’ll need to Create a DataModule for this
You can download using Kaggle API: https://www.kaggle.com/docs/api#interacting-with-datasetsLinks to an external site.
Add eval.pyLinks to an external site. to load model from checkpoint and run on validation dataset
Must print the validation metrics
Push the repository to GitHub
Use infer.pyLinks to an external site. to run on 10 images
Add instructions on README.mdLinks to an external site.
How to use docker run to train and eval the model
How to Train, Eval, Infer using Docker
Make sure to use Volume Mounts!

***Train Model using DockerFile***
siddharth@AP-PF4FEVBK:~/emlo04-session-04-siddharthvij10$ docker run --rm -v $(pwd)/data:/workspace/data -v $(pwd)/logs:/workspace/logs --shm-size=8g emlo04session04siddharthvij10 python src/train.py
2024-10-20 09:39:20.377 | INFO     | utils.logging:wrapper:19 - Starting train
Seed set to 42
Trainer already configured with model summary callbacks: [<class 'lightning.pytorch.callbacks.rich_model_summary.RichModelSummary'>]. Skipping setting a default `ModelSummary` callback.
GPU available: False, used: False
TPU available: False, using: 0 TPU cores
HPU available: False, using: 0 HPUs
2024-10-20 09:39:23.346 | INFO     | __main__:train:46 - Model Hyperparameters:
Config
2024-10-20 09:39:23.349 | INFO     | __main__:train:50 - Starting model training...
Dataset already downloaded and split into train and validation sets.
┏━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━┓
┃    ┃ Name              ┃ Type                 ┃ Params ┃ Mode  ┃
┡━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━┩
│ 0  │ model             │ ResNet               │ 11.2 M │ train │
│ 1  │ model.conv1       │ Conv2d               │  9.4 K │ train │
│ 2  │ model.bn1         │ BatchNorm2d          │    128 │ train │
│ 3  │ model.act1        │ ReLU                 │      0 │ train │
│ 4  │ model.maxpool     │ MaxPool2d            │      0 │ train │
│ 5  │ model.layer1      │ Sequential           │  147 K │ train │
│ 6  │ model.layer2      │ Sequential           │  525 K │ train │
│ 7  │ model.layer3      │ Sequential           │  2.1 M │ train │
│ 8  │ model.layer4      │ Sequential           │  8.4 M │ train │
│ 9  │ model.global_pool │ SelectAdaptivePool2d │      0 │ train │
│ 10 │ model.fc          │ Linear               │  5.1 K │ train │
│ 11 │ train_acc         │ MulticlassAccuracy   │      0 │ train │
│ 12 │ val_acc           │ MulticlassAccuracy   │      0 │ train │
│ 13 │ test_acc          │ MulticlassAccuracy   │      0 │ train │
└────┴───────────────────┴──────────────────────┴────────┴───────┘
Trainable params: 11.2 M                                                        
Non-trainable params: 0                                                         
Total params: 11.2 M                                                            
Total estimated model params size (MB): 44                                      
Modules in train mode: 97                                                       
Modules in eval mode: 0                                                         
/usr/local/lib/python3.10/site-packages/lightning/pytorch/loops/fit_loop.py:298: The number of training batches (25) is smaller than the logging interval Trainer(log_every_n_steps=50). Set a lower value for log_every_n_steps if you want to see logs for the training epoch.
`Trainer.fit` stopped: `max_epochs=5` reached.
Epoch 4/4  ━━━━━━━━━━━━━━━━━ 25/25 0:00:48 • 0:00:00 0.48it/s v_num: 2.000      
                                                              train_loss: 0.430 
                                                              train_acc: 1.000  
                                                              val_loss: 0.007   
                                                              val_acc: 1.000    
2024-10-20 09:43:29.158 | INFO     | __main__:train:52 - Model training completed.
2024-10-20 09:43:29.160 | INFO     | __main__:train:55 - Starting model testing...
Dataset already downloaded and split into train and validation sets.
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Test metric        ┃       DataLoader 0        ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│         test_acc          │            1.0            │
│         test_loss         │   0.007050957530736923    │
└───────────────────────────┴───────────────────────────┘
Testing ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7/7 0:00:04 • 0:00:00 1.50it/s 
2024-10-20 09:43:34.465 | INFO     | __main__:train:57 - Model testing completed.
2024-10-20 09:43:34.466 | INFO     | utils.logging:wrapper:22 - Finished train

***Evaluation of Model using DockerFile***
siddharth@AP-PF4FEVBK:~/emlo04-session-04-siddharthvij10$ docker run --rm -v $(pwd)/data:/workspace/data -v $(pwd)/logs:/workspace/logs --shm-size=4g emlo04session04siddharthvij10 python src/eval.py --checkpoint "/workspace/logs/checkpoints/d
og_classifier-epoch=04-val_loss=0.01.ckpt"
2024-10-20 10:10:31.902 | INFO     | utils.logging:wrapper:19 - Starting evaluate
Seed set to 42
Trainer already configured with model summary callbacks: [<class 'lightning.pytorch.callbacks.rich_model_summary.RichModelSummary'>]. Skipping setting a default `ModelSummary` callback.
GPU available: False, used: False
TPU available: False, using: 0 TPU cores
HPU available: False, using: 0 HPUs
2024-10-20 10:10:34.454 | INFO     | __main__:evaluate:37 - Model Hyperparameters:
Config
2024-10-20 10:10:34.455 | INFO     | __main__:evaluate:41 - Starting model evaluation on validation dataset...
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Validate metric      ┃       DataLoader 0        ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│          val_acc          │            1.0            │
│         val_loss          │   0.007050957530736923    │
└───────────────────────────┴───────────────────────────┘
Validation ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7/7 0:00:03 • 0:00:00 2.32it/s 
2024-10-20 10:10:38.111 | INFO     | __main__:evaluate:43 - Model evaluation completed.
2024-10-20 10:10:38.111 | INFO     | utils.logging:wrapper:22 - Finished evaluate

***Inference on Model using DockerFile***
siddharth@AP-PF4FEVBK:~/emlo04-session-04-siddharthvij10$ docker run --rm -v $(pwd)/data:/workspace/data -v $(pwd)/logs:/workspace/logs -v $(pwd)/predictions:/workspace/predictions --shm-size=4g emlo04session04siddharthvij10 python src/infer.
py --ckpt_path "/workspace/logs/checkpoints/dog_classifier-epoch=04-val_loss=0.01.ckpt" --input_folder "/workspace/sample
s" --output_folder "/workspace/predictions"
2024-10-20 10:14:20.357 | INFO     | utils.logging:wrapper:19 - Starting main
2024-10-20 10:14:20.357 | INFO     | __main__:main:54 - Loading model from checkpoint: /workspace/logs/checkpoints/dog_classifier-epoch=04-val_loss=0.01.ckpt
Processed Boxer.jpg ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
2024-10-20 10:14:35.374 | INFO     | __main__:main:77 - Inference completed. Results saved in /workspace/predictions
2024-10-20 10:14:35.377 | INFO     | utils.logging:wrapper:22 - Finished main
