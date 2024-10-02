[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/A2tcAnZG)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=16088861&assignment_repo_type=AssignmentRepo)
# emlov3-session-02

# PyTorch Docker Assignment

Welcome to the PyTorch Docker Assignment. This assignment is designed to help you understand and work with Docker and PyTorch.

## Assignment Overview

In this assignment, you will:

1. Create a Dockerfile for a PyTorch (CPU version) environment.
2. Keep the size of your Docker image under 1GB (uncompressed).
3. Train any model on the MNIST dataset inside the Docker container.
4. Save the trained model checkpoint to the host operating system.
5. Add an option to resume model training from a checkpoint.

## Starter Code

The provided starter code in train.py provides a basic structure for loading data, defining a model, and running training and testing loops. You will need to complete the code at locations marked by TODO: comments.

## Submission

When you have completed the assignment, push your code to your Github repository. The Github Actions workflow will automatically build your Docker image, run your training script, and check if the assignment requirements have been met. Check the Github Actions tab for the results of these checks. Make sure that all checks are passing before you submit the assignment.

# INFRA
I utilized docker in a Windows Machine (Docker Container) since I was facing issues in Gitpod. The logs below are from Windows PS Shell

# RUN and RESUME Logs
PS C:\Users\svij\MLOPSAssignment1> docker run -v C:\Users\svij\MLOPSAssignment1\emlo4-session-02-siddharthvij10:/workspace emlo4session02siddharthvij10:latest python /workspace/train.py
Downloading http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
Failed to download (trying next):
HTTP Error 403: Forbidden

Downloading https://ossci-datasets.s3.amazonaws.com/mnist/train-images-idx3-ubyte.gz
Downloading https://ossci-datasets.s3.amazonaws.com/mnist/train-images-idx3-ubyte.gz to ../data/MNIST/raw/train-images-idx3-ubyte.gz
100.0%
Extracting ../data/MNIST/raw/train-images-idx3-ubyte.gz to ../data/MNIST/raw

Downloading http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz
Failed to download (trying next):
HTTP Error 403: Forbidden

Downloading https://ossci-datasets.s3.amazonaws.com/mnist/train-labels-idx1-ubyte.gz
Downloading https://ossci-datasets.s3.amazonaws.com/mnist/train-labels-idx1-ubyte.gz to ../data/MNIST/raw/train-labels-idx1-ubyte.gz
100.0%
Extracting ../data/MNIST/raw/train-labels-idx1-ubyte.gz to ../data/MNIST/raw

Downloading http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz
Failed to download (trying next):
HTTP Error 403: Forbidden

Downloading https://ossci-datasets.s3.amazonaws.com/mnist/t10k-images-idx3-ubyte.gz
Downloading https://ossci-datasets.s3.amazonaws.com/mnist/t10k-images-idx3-ubyte.gz to ../data/MNIST/raw/t10k-images-idx3-ubyte.gz
100.0%
Extracting ../data/MNIST/raw/t10k-images-idx3-ubyte.gz to ../data/MNIST/raw

Downloading http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz
Failed to download (trying next):
HTTP Error 403: Forbidden

Downloading https://ossci-datasets.s3.amazonaws.com/mnist/t10k-labels-idx1-ubyte.gz
Downloading https://ossci-datasets.s3.amazonaws.com/mnist/t10k-labels-idx1-ubyte.gz to ../data/MNIST/raw/t10k-labels-idx1-ubyte.gz
100.0%
Extracting ../data/MNIST/raw/t10k-labels-idx1-ubyte.gz to ../data/MNIST/raw

Train Epoch: 1 [0/60000 (0%)]   Loss: 2.329474
Train Epoch: 1 [640/60000 (1%)] Loss: 1.425185
Train Epoch: 1 [1280/60000 (2%)]        Loss: 0.826809
Train Epoch: 1 [1920/60000 (3%)]        Loss: 0.556883
Train Epoch: 1 [2560/60000 (4%)]        Loss: 0.483756
Train Epoch: 1 [3200/60000 (5%)]        Loss: 0.257975
Train Epoch: 1 [3840/60000 (6%)]        Loss: 0.348440
Train Epoch: 1 [4480/60000 (7%)]        Loss: 0.333388
Train Epoch: 1 [5120/60000 (9%)]        Loss: 0.524236
Train Epoch: 1 [5760/60000 (10%)]       Loss: 0.174640
Train Epoch: 1 [6400/60000 (11%)]       Loss: 0.176443
Train Epoch: 1 [7040/60000 (12%)]       Loss: 0.204510
Train Epoch: 1 [7680/60000 (13%)]       Loss: 0.189632
Train Epoch: 1 [8320/60000 (14%)]       Loss: 0.109184
Train Epoch: 1 [8960/60000 (15%)]       Loss: 0.222831
Train Epoch: 1 [9600/60000 (16%)]       Loss: 0.140818
Train Epoch: 1 [10240/60000 (17%)]      Loss: 0.520451
Train Epoch: 1 [10880/60000 (18%)]      Loss: 0.198344
Train Epoch: 1 [11520/60000 (19%)]      Loss: 0.653131
Train Epoch: 1 [12160/60000 (20%)]      Loss: 0.204425
Train Epoch: 1 [12800/60000 (21%)]      Loss: 0.133712
Train Epoch: 1 [13440/60000 (22%)]      Loss: 0.171830
Train Epoch: 1 [14080/60000 (23%)]      Loss: 0.120295
Train Epoch: 1 [14720/60000 (25%)]      Loss: 0.328583
Train Epoch: 1 [15360/60000 (26%)]      Loss: 0.130127
Train Epoch: 1 [16000/60000 (27%)]      Loss: 0.309889
Train Epoch: 1 [16640/60000 (28%)]      Loss: 0.158437
Train Epoch: 1 [17280/60000 (29%)]      Loss: 0.056400
Train Epoch: 1 [17920/60000 (30%)]      Loss: 0.112370
Train Epoch: 1 [18560/60000 (31%)]      Loss: 0.165443
Train Epoch: 1 [19200/60000 (32%)]      Loss: 0.178987
Train Epoch: 1 [19840/60000 (33%)]      Loss: 0.120552
Train Epoch: 1 [20480/60000 (34%)]      Loss: 0.077266
Train Epoch: 1 [21120/60000 (35%)]      Loss: 0.251985
Train Epoch: 1 [21760/60000 (36%)]      Loss: 0.028953
Train Epoch: 1 [22400/60000 (37%)]      Loss: 0.043980
Train Epoch: 1 [23040/60000 (38%)]      Loss: 0.176588
Train Epoch: 1 [23680/60000 (39%)]      Loss: 0.323919
Train Epoch: 1 [24320/60000 (41%)]      Loss: 0.013553
Train Epoch: 1 [24960/60000 (42%)]      Loss: 0.212146
Train Epoch: 1 [25600/60000 (43%)]      Loss: 0.109924
Train Epoch: 1 [26240/60000 (44%)]      Loss: 0.156672
Train Epoch: 1 [26880/60000 (45%)]      Loss: 0.260443
Train Epoch: 1 [27520/60000 (46%)]      Loss: 0.168455
Train Epoch: 1 [28160/60000 (47%)]      Loss: 0.059279
Train Epoch: 1 [28800/60000 (48%)]      Loss: 0.113021
Train Epoch: 1 [29440/60000 (49%)]      Loss: 0.085967
Train Epoch: 1 [30080/60000 (50%)]      Loss: 0.114650
Train Epoch: 1 [30720/60000 (51%)]      Loss: 0.157801
Train Epoch: 1 [31360/60000 (52%)]      Loss: 0.197543
Train Epoch: 1 [32000/60000 (53%)]      Loss: 0.119325
Train Epoch: 1 [32640/60000 (54%)]      Loss: 0.222015
Train Epoch: 1 [33280/60000 (55%)]      Loss: 0.172127
Train Epoch: 1 [33920/60000 (57%)]      Loss: 0.030576
Train Epoch: 1 [34560/60000 (58%)]      Loss: 0.090383
Train Epoch: 1 [35200/60000 (59%)]      Loss: 0.231498
Train Epoch: 1 [35840/60000 (60%)]      Loss: 0.242864
Train Epoch: 1 [36480/60000 (61%)]      Loss: 0.026988
Train Epoch: 1 [37120/60000 (62%)]      Loss: 0.066209
Train Epoch: 1 [37760/60000 (63%)]      Loss: 0.263972
Train Epoch: 1 [38400/60000 (64%)]      Loss: 0.117417
Train Epoch: 1 [39040/60000 (65%)]      Loss: 0.026811
Train Epoch: 1 [39680/60000 (66%)]      Loss: 0.112190
Train Epoch: 1 [40320/60000 (67%)]      Loss: 0.105352
Train Epoch: 1 [40960/60000 (68%)]      Loss: 0.213338
Train Epoch: 1 [41600/60000 (69%)]      Loss: 0.137817
Train Epoch: 1 [42240/60000 (70%)]      Loss: 0.042226
Train Epoch: 1 [42880/60000 (71%)]      Loss: 0.173074
Train Epoch: 1 [43520/60000 (72%)]      Loss: 0.190492
Train Epoch: 1 [44160/60000 (74%)]      Loss: 0.028924
Train Epoch: 1 [44800/60000 (75%)]      Loss: 0.048417
Train Epoch: 1 [45440/60000 (76%)]      Loss: 0.152409
Train Epoch: 1 [46080/60000 (77%)]      Loss: 0.163627
Train Epoch: 1 [46720/60000 (78%)]      Loss: 0.303969
Train Epoch: 1 [47360/60000 (79%)]      Loss: 0.100144
Train Epoch: 1 [48000/60000 (80%)]      Loss: 0.108896
Train Epoch: 1 [48640/60000 (81%)]      Loss: 0.080212
Train Epoch: 1 [49280/60000 (82%)]      Loss: 0.056271
Train Epoch: 1 [49920/60000 (83%)]      Loss: 0.064962
Train Epoch: 1 [50560/60000 (84%)]      Loss: 0.089722
Train Epoch: 1 [51200/60000 (85%)]      Loss: 0.110190
Train Epoch: 1 [51840/60000 (86%)]      Loss: 0.021843
Train Epoch: 1 [52480/60000 (87%)]      Loss: 0.019528
Train Epoch: 1 [53120/60000 (88%)]      Loss: 0.280549
Train Epoch: 1 [53760/60000 (90%)]      Loss: 0.067030
Train Epoch: 1 [54400/60000 (91%)]      Loss: 0.028754
Train Epoch: 1 [55040/60000 (92%)]      Loss: 0.023544
Train Epoch: 1 [55680/60000 (93%)]      Loss: 0.161516
Train Epoch: 1 [56320/60000 (94%)]      Loss: 0.083252
Train Epoch: 1 [56960/60000 (95%)]      Loss: 0.050743
Train Epoch: 1 [57600/60000 (96%)]      Loss: 0.144901
Train Epoch: 1 [58240/60000 (97%)]      Loss: 0.004297
Train Epoch: 1 [58880/60000 (98%)]      Loss: 0.004678
Train Epoch: 1 [59520/60000 (99%)]      Loss: 0.003761

Test set: Average loss: 0.0485, Accuracy: 9817/10000 (98%)

Model saved at epoch 1.
Train Epoch: 2 [0/60000 (0%)]   Loss: 0.056159
Train Epoch: 2 [640/60000 (1%)] Loss: 0.031085
Train Epoch: 2 [1280/60000 (2%)]        Loss: 0.059390
Train Epoch: 2 [1920/60000 (3%)]        Loss: 0.227593
Train Epoch: 2 [2560/60000 (4%)]        Loss: 0.038973
Train Epoch: 2 [3200/60000 (5%)]        Loss: 0.018625
Train Epoch: 2 [3840/60000 (6%)]        Loss: 0.010728
Train Epoch: 2 [4480/60000 (7%)]        Loss: 0.114644
Train Epoch: 2 [5120/60000 (9%)]        Loss: 0.186310
Train Epoch: 2 [5760/60000 (10%)]       Loss: 0.061912
Train Epoch: 2 [6400/60000 (11%)]       Loss: 0.208459
Train Epoch: 2 [7040/60000 (12%)]       Loss: 0.170969
Train Epoch: 2 [7680/60000 (13%)]       Loss: 0.024932
Train Epoch: 2 [8320/60000 (14%)]       Loss: 0.007327
Train Epoch: 2 [8960/60000 (15%)]       Loss: 0.231445
Train Epoch: 2 [9600/60000 (16%)]       Loss: 0.018403
Train Epoch: 2 [10240/60000 (17%)]      Loss: 0.204720
Train Epoch: 2 [10880/60000 (18%)]      Loss: 0.015609
Train Epoch: 2 [11520/60000 (19%)]      Loss: 0.121538
Train Epoch: 2 [12160/60000 (20%)]      Loss: 0.123560
Train Epoch: 2 [12800/60000 (21%)]      Loss: 0.069249
Train Epoch: 2 [13440/60000 (22%)]      Loss: 0.078495
Train Epoch: 2 [14080/60000 (23%)]      Loss: 0.007350
Train Epoch: 2 [14720/60000 (25%)]      Loss: 0.120804
Train Epoch: 2 [15360/60000 (26%)]      Loss: 0.053632
Train Epoch: 2 [16000/60000 (27%)]      Loss: 0.040169
Train Epoch: 2 [16640/60000 (28%)]      Loss: 0.152507
Train Epoch: 2 [17280/60000 (29%)]      Loss: 0.015645
Train Epoch: 2 [17920/60000 (30%)]      Loss: 0.094933
Train Epoch: 2 [18560/60000 (31%)]      Loss: 0.023420
Train Epoch: 2 [19200/60000 (32%)]      Loss: 0.049777
Train Epoch: 2 [19840/60000 (33%)]      Loss: 0.136624
Train Epoch: 2 [20480/60000 (34%)]      Loss: 0.014840
Train Epoch: 2 [21120/60000 (35%)]      Loss: 0.134831
Train Epoch: 2 [21760/60000 (36%)]      Loss: 0.021501
Train Epoch: 2 [22400/60000 (37%)]      Loss: 0.012051
Train Epoch: 2 [23040/60000 (38%)]      Loss: 0.177253
Train Epoch: 2 [23680/60000 (39%)]      Loss: 0.042449
Train Epoch: 2 [24320/60000 (41%)]      Loss: 0.057287
Train Epoch: 2 [24960/60000 (42%)]      Loss: 0.025111
Train Epoch: 2 [25600/60000 (43%)]      Loss: 0.044895
Train Epoch: 2 [26240/60000 (44%)]      Loss: 0.023982
Train Epoch: 2 [26880/60000 (45%)]      Loss: 0.070708
Train Epoch: 2 [27520/60000 (46%)]      Loss: 0.100057
Train Epoch: 2 [28160/60000 (47%)]      Loss: 0.096940
Train Epoch: 2 [28800/60000 (48%)]      Loss: 0.032878
Train Epoch: 2 [29440/60000 (49%)]      Loss: 0.014438
Train Epoch: 2 [30080/60000 (50%)]      Loss: 0.037828
Train Epoch: 2 [30720/60000 (51%)]      Loss: 0.036023
Train Epoch: 2 [31360/60000 (52%)]      Loss: 0.112860
Train Epoch: 2 [32000/60000 (53%)]      Loss: 0.075143
Train Epoch: 2 [32640/60000 (54%)]      Loss: 0.072120
Train Epoch: 2 [33280/60000 (55%)]      Loss: 0.126685
Train Epoch: 2 [33920/60000 (57%)]      Loss: 0.009580
Train Epoch: 2 [34560/60000 (58%)]      Loss: 0.059165
Train Epoch: 2 [35200/60000 (59%)]      Loss: 0.300351
Train Epoch: 2 [35840/60000 (60%)]      Loss: 0.100552
Train Epoch: 2 [36480/60000 (61%)]      Loss: 0.043724
Train Epoch: 2 [37120/60000 (62%)]      Loss: 0.030763
Train Epoch: 2 [37760/60000 (63%)]      Loss: 0.051557
Train Epoch: 2 [38400/60000 (64%)]      Loss: 0.062071
Train Epoch: 2 [39040/60000 (65%)]      Loss: 0.011753
Train Epoch: 2 [39680/60000 (66%)]      Loss: 0.058666
Train Epoch: 2 [40320/60000 (67%)]      Loss: 0.066985
Train Epoch: 2 [40960/60000 (68%)]      Loss: 0.114277
Train Epoch: 2 [41600/60000 (69%)]      Loss: 0.071272
Train Epoch: 2 [42240/60000 (70%)]      Loss: 0.010139
Train Epoch: 2 [42880/60000 (71%)]      Loss: 0.046250
Train Epoch: 2 [43520/60000 (72%)]      Loss: 0.022923
Train Epoch: 2 [44160/60000 (74%)]      Loss: 0.003598
Train Epoch: 2 [44800/60000 (75%)]      Loss: 0.165504
Train Epoch: 2 [45440/60000 (76%)]      Loss: 0.099116
Train Epoch: 2 [46080/60000 (77%)]      Loss: 0.084217
Train Epoch: 2 [46720/60000 (78%)]      Loss: 0.138465
Train Epoch: 2 [47360/60000 (79%)]      Loss: 0.062901
Train Epoch: 2 [48000/60000 (80%)]      Loss: 0.067393
Train Epoch: 2 [48640/60000 (81%)]      Loss: 0.032203
Train Epoch: 2 [49280/60000 (82%)]      Loss: 0.033983
Train Epoch: 2 [49920/60000 (83%)]      Loss: 0.104751
Train Epoch: 2 [50560/60000 (84%)]      Loss: 0.049874
Train Epoch: 2 [51200/60000 (85%)]      Loss: 0.258861
Train Epoch: 2 [51840/60000 (86%)]      Loss: 0.003859
Train Epoch: 2 [52480/60000 (87%)]      Loss: 0.001082
Train Epoch: 2 [53120/60000 (88%)]      Loss: 0.126498
Train Epoch: 2 [53760/60000 (90%)]      Loss: 0.115297
Train Epoch: 2 [54400/60000 (91%)]      Loss: 0.095270
Train Epoch: 2 [55040/60000 (92%)]      Loss: 0.054223
Train Epoch: 2 [55680/60000 (93%)]      Loss: 0.014983
Train Epoch: 2 [56320/60000 (94%)]      Loss: 0.011451
Train Epoch: 2 [56960/60000 (95%)]      Loss: 0.046288
Train Epoch: 2 [57600/60000 (96%)]      Loss: 0.109725
Train Epoch: 2 [58240/60000 (97%)]      Loss: 0.017066
Train Epoch: 2 [58880/60000 (98%)]      Loss: 0.002172
Train Epoch: 2 [59520/60000 (99%)]      Loss: 0.001673

Test set: Average loss: 0.0380, Accuracy: 9874/10000 (99%)

Model saved at epoch 2.
PS C:\Users\svij\MLOPSAssignment1> docker run -v C:\Users\svij\MLOPSAssignment1\emlo4-session-02-siddharthvij10:/workspace emlo4session02siddharthvij10:latest python /workspace/train.py --resume
Downloading http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
Failed to download (trying next):
HTTP Error 403: Forbidden

Downloading https://ossci-datasets.s3.amazonaws.com/mnist/train-images-idx3-ubyte.gz
Downloading https://ossci-datasets.s3.amazonaws.com/mnist/train-images-idx3-ubyte.gz to ../data/MNIST/raw/train-images-idx3-ubyte.gz
100.0%
Extracting ../data/MNIST/raw/train-images-idx3-ubyte.gz to ../data/MNIST/raw

Downloading http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz
Failed to download (trying next):
HTTP Error 403: Forbidden

Downloading https://ossci-datasets.s3.amazonaws.com/mnist/train-labels-idx1-ubyte.gz
Downloading https://ossci-datasets.s3.amazonaws.com/mnist/train-labels-idx1-ubyte.gz to ../data/MNIST/raw/train-labels-idx1-ubyte.gz
100.0%
Extracting ../data/MNIST/raw/train-labels-idx1-ubyte.gz to ../data/MNIST/raw

Downloading http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz
Failed to download (trying next):
HTTP Error 403: Forbidden

Downloading https://ossci-datasets.s3.amazonaws.com/mnist/t10k-images-idx3-ubyte.gz
Downloading https://ossci-datasets.s3.amazonaws.com/mnist/t10k-images-idx3-ubyte.gz to ../data/MNIST/raw/t10k-images-idx3-ubyte.gz
100.0%
Extracting ../data/MNIST/raw/t10k-images-idx3-ubyte.gz to ../data/MNIST/raw

Downloading http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz
Failed to download (trying next):
HTTP Error 403: Forbidden

Downloading https://ossci-datasets.s3.amazonaws.com/mnist/t10k-labels-idx1-ubyte.gz
Downloading https://ossci-datasets.s3.amazonaws.com/mnist/t10k-labels-idx1-ubyte.gz to ../data/MNIST/raw/t10k-labels-idx1-ubyte.gz
100.0%
Extracting ../data/MNIST/raw/t10k-labels-idx1-ubyte.gz to ../data/MNIST/raw

Resumed training from saved model.
Train Epoch: 1 [0/60000 (0%)]   Loss: 0.028084
Train Epoch: 1 [640/60000 (1%)] Loss: 0.006276
Train Epoch: 1 [1280/60000 (2%)]        Loss: 0.036465
Train Epoch: 1 [1920/60000 (3%)]        Loss: 0.202436
Train Epoch: 1 [2560/60000 (4%)]        Loss: 0.032306
Train Epoch: 1 [3200/60000 (5%)]        Loss: 0.067385
Train Epoch: 1 [3840/60000 (6%)]        Loss: 0.002116
Train Epoch: 1 [4480/60000 (7%)]        Loss: 0.033772
Train Epoch: 1 [5120/60000 (9%)]        Loss: 0.025256
Train Epoch: 1 [5760/60000 (10%)]       Loss: 0.088008
Train Epoch: 1 [6400/60000 (11%)]       Loss: 0.154508
Train Epoch: 1 [7040/60000 (12%)]       Loss: 0.150625
Train Epoch: 1 [7680/60000 (13%)]       Loss: 0.014908
Train Epoch: 1 [8320/60000 (14%)]       Loss: 0.013130
Train Epoch: 1 [8960/60000 (15%)]       Loss: 0.044950
Train Epoch: 1 [9600/60000 (16%)]       Loss: 0.005718
Train Epoch: 1 [10240/60000 (17%)]      Loss: 0.165862
Train Epoch: 1 [10880/60000 (18%)]      Loss: 0.029341
Train Epoch: 1 [11520/60000 (19%)]      Loss: 0.064026
Train Epoch: 1 [12160/60000 (20%)]      Loss: 0.013531
Train Epoch: 1 [12800/60000 (21%)]      Loss: 0.011276
Train Epoch: 1 [13440/60000 (22%)]      Loss: 0.029691
Train Epoch: 1 [14080/60000 (23%)]      Loss: 0.001440
Train Epoch: 1 [14720/60000 (25%)]      Loss: 0.016422
Train Epoch: 1 [15360/60000 (26%)]      Loss: 0.024570
Train Epoch: 1 [16000/60000 (27%)]      Loss: 0.028134
Train Epoch: 1 [16640/60000 (28%)]      Loss: 0.089308
Train Epoch: 1 [17280/60000 (29%)]      Loss: 0.001675
Train Epoch: 1 [17920/60000 (30%)]      Loss: 0.012022
Train Epoch: 1 [18560/60000 (31%)]      Loss: 0.004025
Train Epoch: 1 [19200/60000 (32%)]      Loss: 0.019301
Train Epoch: 1 [19840/60000 (33%)]      Loss: 0.028955
Train Epoch: 1 [20480/60000 (34%)]      Loss: 0.011338
Train Epoch: 1 [21120/60000 (35%)]      Loss: 0.093223
Train Epoch: 1 [21760/60000 (36%)]      Loss: 0.003842
Train Epoch: 1 [22400/60000 (37%)]      Loss: 0.012684
Train Epoch: 1 [23040/60000 (38%)]      Loss: 0.038706
Train Epoch: 1 [23680/60000 (39%)]      Loss: 0.043595
Train Epoch: 1 [24320/60000 (41%)]      Loss: 0.001310
Train Epoch: 1 [24960/60000 (42%)]      Loss: 0.005644
Train Epoch: 1 [25600/60000 (43%)]      Loss: 0.005499
Train Epoch: 1 [26240/60000 (44%)]      Loss: 0.011792
Train Epoch: 1 [26880/60000 (45%)]      Loss: 0.028461
Train Epoch: 1 [27520/60000 (46%)]      Loss: 0.048395
Train Epoch: 1 [28160/60000 (47%)]      Loss: 0.039113
Train Epoch: 1 [28800/60000 (48%)]      Loss: 0.002302
Train Epoch: 1 [29440/60000 (49%)]      Loss: 0.001211
Train Epoch: 1 [30080/60000 (50%)]      Loss: 0.021293
Train Epoch: 1 [30720/60000 (51%)]      Loss: 0.020997
Train Epoch: 1 [31360/60000 (52%)]      Loss: 0.057313
Train Epoch: 1 [32000/60000 (53%)]      Loss: 0.082699
Train Epoch: 1 [32640/60000 (54%)]      Loss: 0.032347
Train Epoch: 1 [33280/60000 (55%)]      Loss: 0.025546
Train Epoch: 1 [33920/60000 (57%)]      Loss: 0.000572
Train Epoch: 1 [34560/60000 (58%)]      Loss: 0.004108
Train Epoch: 1 [35200/60000 (59%)]      Loss: 0.062906
Train Epoch: 1 [35840/60000 (60%)]      Loss: 0.018535
Train Epoch: 1 [36480/60000 (61%)]      Loss: 0.006468
Train Epoch: 1 [37120/60000 (62%)]      Loss: 0.005775
Train Epoch: 1 [37760/60000 (63%)]      Loss: 0.229196
Train Epoch: 1 [38400/60000 (64%)]      Loss: 0.083012
Train Epoch: 1 [39040/60000 (65%)]      Loss: 0.001570
Train Epoch: 1 [39680/60000 (66%)]      Loss: 0.018579
Train Epoch: 1 [40320/60000 (67%)]      Loss: 0.007267
Train Epoch: 1 [40960/60000 (68%)]      Loss: 0.072014
Train Epoch: 1 [41600/60000 (69%)]      Loss: 0.056512
Train Epoch: 1 [42240/60000 (70%)]      Loss: 0.003511
Train Epoch: 1 [42880/60000 (71%)]      Loss: 0.032240
Train Epoch: 1 [43520/60000 (72%)]      Loss: 0.021367
Train Epoch: 1 [44160/60000 (74%)]      Loss: 0.006386
Train Epoch: 1 [44800/60000 (75%)]      Loss: 0.003987
Train Epoch: 1 [45440/60000 (76%)]      Loss: 0.016992
Train Epoch: 1 [46080/60000 (77%)]      Loss: 0.017524
Train Epoch: 1 [46720/60000 (78%)]      Loss: 0.029660
Train Epoch: 1 [47360/60000 (79%)]      Loss: 0.003231
Train Epoch: 1 [48000/60000 (80%)]      Loss: 0.034320
Train Epoch: 1 [48640/60000 (81%)]      Loss: 0.000838
Train Epoch: 1 [49280/60000 (82%)]      Loss: 0.009855
Train Epoch: 1 [49920/60000 (83%)]      Loss: 0.005785
Train Epoch: 1 [50560/60000 (84%)]      Loss: 0.004238
Train Epoch: 1 [51200/60000 (85%)]      Loss: 0.041485
Train Epoch: 1 [51840/60000 (86%)]      Loss: 0.001649
Train Epoch: 1 [52480/60000 (87%)]      Loss: 0.001738
Train Epoch: 1 [53120/60000 (88%)]      Loss: 0.068742
Train Epoch: 1 [53760/60000 (90%)]      Loss: 0.112233
Train Epoch: 1 [54400/60000 (91%)]      Loss: 0.001627
Train Epoch: 1 [55040/60000 (92%)]      Loss: 0.000580
Train Epoch: 1 [55680/60000 (93%)]      Loss: 0.027453
Train Epoch: 1 [56320/60000 (94%)]      Loss: 0.023177
Train Epoch: 1 [56960/60000 (95%)]      Loss: 0.001672
Train Epoch: 1 [57600/60000 (96%)]      Loss: 0.016955
Train Epoch: 1 [58240/60000 (97%)]      Loss: 0.000046
Train Epoch: 1 [58880/60000 (98%)]      Loss: 0.000151
Train Epoch: 1 [59520/60000 (99%)]      Loss: 0.000044

Test set: Average loss: 0.0434, Accuracy: 9873/10000 (99%)

Model saved at epoch 1.
Train Epoch: 2 [0/60000 (0%)]   Loss: 0.014649
Train Epoch: 2 [640/60000 (1%)] Loss: 0.002749
Train Epoch: 2 [1280/60000 (2%)]        Loss: 0.009414
Train Epoch: 2 [1920/60000 (3%)]        Loss: 0.034755
Train Epoch: 2 [2560/60000 (4%)]        Loss: 0.002775
Train Epoch: 2 [3200/60000 (5%)]        Loss: 0.001128
Train Epoch: 2 [3840/60000 (6%)]        Loss: 0.002535
Train Epoch: 2 [4480/60000 (7%)]        Loss: 0.008959
Train Epoch: 2 [5120/60000 (9%)]        Loss: 0.181903
Train Epoch: 2 [5760/60000 (10%)]       Loss: 0.005620
Train Epoch: 2 [6400/60000 (11%)]       Loss: 0.023844
Train Epoch: 2 [7040/60000 (12%)]       Loss: 0.044284
Train Epoch: 2 [7680/60000 (13%)]       Loss: 0.010109
Train Epoch: 2 [8320/60000 (14%)]       Loss: 0.001649
Train Epoch: 2 [8960/60000 (15%)]       Loss: 0.199998
Train Epoch: 2 [9600/60000 (16%)]       Loss: 0.001225
Train Epoch: 2 [10240/60000 (17%)]      Loss: 0.083575
Train Epoch: 2 [10880/60000 (18%)]      Loss: 0.003478
Train Epoch: 2 [11520/60000 (19%)]      Loss: 0.022357
Train Epoch: 2 [12160/60000 (20%)]      Loss: 0.065243
Train Epoch: 2 [12800/60000 (21%)]      Loss: 0.014334
Train Epoch: 2 [13440/60000 (22%)]      Loss: 0.041954
Train Epoch: 2 [14080/60000 (23%)]      Loss: 0.000514
Train Epoch: 2 [14720/60000 (25%)]      Loss: 0.034821
Train Epoch: 2 [15360/60000 (26%)]      Loss: 0.003979
Train Epoch: 2 [16000/60000 (27%)]      Loss: 0.007738
Train Epoch: 2 [16640/60000 (28%)]      Loss: 0.086212
Train Epoch: 2 [17280/60000 (29%)]      Loss: 0.000579
Train Epoch: 2 [17920/60000 (30%)]      Loss: 0.020424
Train Epoch: 2 [18560/60000 (31%)]      Loss: 0.004246
Train Epoch: 2 [19200/60000 (32%)]      Loss: 0.007053
Train Epoch: 2 [19840/60000 (33%)]      Loss: 0.037517
Train Epoch: 2 [20480/60000 (34%)]      Loss: 0.000234
Train Epoch: 2 [21120/60000 (35%)]      Loss: 0.080913
Train Epoch: 2 [21760/60000 (36%)]      Loss: 0.003258
Train Epoch: 2 [22400/60000 (37%)]      Loss: 0.003281
Train Epoch: 2 [23040/60000 (38%)]      Loss: 0.073923
Train Epoch: 2 [23680/60000 (39%)]      Loss: 0.045781
Train Epoch: 2 [24320/60000 (41%)]      Loss: 0.003716
Train Epoch: 2 [24960/60000 (42%)]      Loss: 0.008828
Train Epoch: 2 [25600/60000 (43%)]      Loss: 0.002958
Train Epoch: 2 [26240/60000 (44%)]      Loss: 0.001539
Train Epoch: 2 [26880/60000 (45%)]      Loss: 0.024108
Train Epoch: 2 [27520/60000 (46%)]      Loss: 0.029217
Train Epoch: 2 [28160/60000 (47%)]      Loss: 0.001783
Train Epoch: 2 [28800/60000 (48%)]      Loss: 0.025000
Train Epoch: 2 [29440/60000 (49%)]      Loss: 0.003335
Train Epoch: 2 [30080/60000 (50%)]      Loss: 0.011062
Train Epoch: 2 [30720/60000 (51%)]      Loss: 0.012839
Train Epoch: 2 [31360/60000 (52%)]      Loss: 0.003999
Train Epoch: 2 [32000/60000 (53%)]      Loss: 0.006665
Train Epoch: 2 [32640/60000 (54%)]      Loss: 0.023100
Train Epoch: 2 [33280/60000 (55%)]      Loss: 0.007789
Train Epoch: 2 [33920/60000 (57%)]      Loss: 0.006381
Train Epoch: 2 [34560/60000 (58%)]      Loss: 0.000900
Train Epoch: 2 [35200/60000 (59%)]      Loss: 0.113734
Train Epoch: 2 [35840/60000 (60%)]      Loss: 0.010519
Train Epoch: 2 [36480/60000 (61%)]      Loss: 0.005380
Train Epoch: 2 [37120/60000 (62%)]      Loss: 0.003972
Train Epoch: 2 [37760/60000 (63%)]      Loss: 0.001708
Train Epoch: 2 [38400/60000 (64%)]      Loss: 0.027470
Train Epoch: 2 [39040/60000 (65%)]      Loss: 0.000861
Train Epoch: 2 [39680/60000 (66%)]      Loss: 0.045591
Train Epoch: 2 [40320/60000 (67%)]      Loss: 0.030018
Train Epoch: 2 [40960/60000 (68%)]      Loss: 0.016718
Train Epoch: 2 [41600/60000 (69%)]      Loss: 0.028866
Train Epoch: 2 [42240/60000 (70%)]      Loss: 0.001001
Train Epoch: 2 [42880/60000 (71%)]      Loss: 0.001889
Train Epoch: 2 [43520/60000 (72%)]      Loss: 0.005280
Train Epoch: 2 [44160/60000 (74%)]      Loss: 0.002151
Train Epoch: 2 [44800/60000 (75%)]      Loss: 0.034497
Train Epoch: 2 [45440/60000 (76%)]      Loss: 0.015790
Train Epoch: 2 [46080/60000 (77%)]      Loss: 0.049999
Train Epoch: 2 [46720/60000 (78%)]      Loss: 0.038438
Train Epoch: 2 [47360/60000 (79%)]      Loss: 0.009348
Train Epoch: 2 [48000/60000 (80%)]      Loss: 0.057028
Train Epoch: 2 [48640/60000 (81%)]      Loss: 0.007159
Train Epoch: 2 [49280/60000 (82%)]      Loss: 0.018498
Train Epoch: 2 [49920/60000 (83%)]      Loss: 0.012803
Train Epoch: 2 [50560/60000 (84%)]      Loss: 0.004006
Train Epoch: 2 [51200/60000 (85%)]      Loss: 0.204006
Train Epoch: 2 [51840/60000 (86%)]      Loss: 0.002410
Train Epoch: 2 [52480/60000 (87%)]      Loss: 0.000157
Train Epoch: 2 [53120/60000 (88%)]      Loss: 0.017502
Train Epoch: 2 [53760/60000 (90%)]      Loss: 0.025902
Train Epoch: 2 [54400/60000 (91%)]      Loss: 0.032567
Train Epoch: 2 [55040/60000 (92%)]      Loss: 0.006052
Train Epoch: 2 [55680/60000 (93%)]      Loss: 0.002111
Train Epoch: 2 [56320/60000 (94%)]      Loss: 0.001167
Train Epoch: 2 [56960/60000 (95%)]      Loss: 0.000647
Train Epoch: 2 [57600/60000 (96%)]      Loss: 0.015518
Train Epoch: 2 [58240/60000 (97%)]      Loss: 0.000036
Train Epoch: 2 [58880/60000 (98%)]      Loss: 0.000018
Train Epoch: 2 [59520/60000 (99%)]      Loss: 0.000414

Test set: Average loss: 0.0407, Accuracy: 9869/10000 (99%)

Model saved at epoch 2.

# Screenshot of Docker Image
<img width="444" alt="{C856938F-5FBC-49E9-A19D-C4EDF1BD5D52}" src="https://github.com/user-attachments/assets/cabcec12-bf55-4145-9e06-89a3189d31f5">

