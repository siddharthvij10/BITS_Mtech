[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/H1dh0F7f)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=16269875&assignment_repo_type=AssignmentRepo)
# EMLO4 - Session 03

Docker Compose for MNIST Training, Evaluation, and Inference

In this assignment, you will create a Docker Compose configuration to perform training, evaluation, and inference on the MNIST dataset.

Requirements:

1. You’ll need to use this model and training technique (MNIST Hogwild): https://github.com/pytorch/examples/tree/main/mnist_hogwild
2. Set Num Processes to 2 for MNIST HogWild
3. Create three services in the Docker Compose file: **`train`**, **`evaluate`**, and **`infer`**.
4. Use a shared volume called **`mnist`** for sharing data between the services.
5. The **`train`** service should:
    - Look for a checkpoint file in the volume. If found, resume training from that checkpoint. Train for **ONLY 1 epoch** and save the final checkpoint. Once done, exit.
6. The **`evaluate`** service should:
    - Look for the final checkpoint file in the volume. Evaluate the model using the checkpoint and save the evaluation metrics in a json file. Once done, exit.
    - Share the model code by importing the model instead of copy-pasting it in eval.py
7. The **`infer`** service should:
    - Run inference on any 5 random MNIST images and save the results (images with file name as predicted number) in the **`results`** folder in the volume. Then exit.
8. After running all the services, ensure that the model, and results are available in the **`mnist`** volume.

Detailed Instructions:

1. Build all the Docker images using **`docker compose build`**.
2. Run the Docker Compose services using **`docker compose run train`**, **`docker compose run evaluate`**, and **`docker compose run infer`**. Verify that all services have completed successfully.
3. Check if the checkpoint file (**`mnist_cnn.pt`**) is saved in the **`mnist`** volume. If found, display "Checkpoint file found." If not found, display "Checkpoint file not found!" and exit with an error.
4. Check if the evaluation results file (**`eval_results.json`**) is saved in the **`mnist`** volume.
    1. Example: `{"Test loss": 0.0890245330810547, "Accuracy": 97.12}`
5. Check the contents of the **`results`** folder in the **`mnist`** volume see if the inference results are saved.

The provided grading script will run the Docker Compose configuration, check for the required files, display the results, and perform size and version checks.

You can run it yourself before pushing the code to your repo

**LOGS of FINAL EXECUTION**
siddharth@AP-PF4FEVBK:~/emlo4-session-03-siddharthvij10$ docker compose build --no-cache
[+] Building 60.8s (26/26) FINISHED                                      docker:default
 => [evaluate internal] load build definition from Dockerfile.eval                 0.0s
 => => transferring dockerfile: 330B                                               0.0s
 => [evaluate internal] load metadata for docker.io/library/python:3.10-slim-bust  1.9s
 => [train internal] load build definition from Dockerfile.train                   0.0s
 => => transferring dockerfile: 302B                                               0.0s
 => [infer internal] load build definition from Dockerfile.infer                   0.0s
 => => transferring dockerfile: 344B                                               0.0s
 => [evaluate auth] library/python:pull token for registry-1.docker.io             0.0s
 => [train internal] load .dockerignore                                            0.0s
 => => transferring context: 44B                                                   0.0s
 => [evaluate internal] load .dockerignore                                         0.0s
 => => transferring context: 44B                                                   0.0s
 => [infer internal] load .dockerignore                                            0.0s
 => => transferring context: 44B                                                   0.0s
 => [infer 1/6] FROM docker.io/library/python:3.10-slim-buster@sha256:37aa274c2d0  0.0s
 => [evaluate internal] load build context                                         0.0s
 => => transferring context: 4.28kB                                                0.0s
 => CACHED [infer 2/6] WORKDIR /workspace                                          0.0s
 => [train internal] load build context                                            0.0s
 => => transferring context: 4.61kB                                                0.0s
 => [infer internal] load build context                                            0.0s
 => => transferring context: 151B                                                  0.0s
 => [evaluate 3/6] COPY model-eval/eval.py /workspace/                             0.1s
 => [infer 3/5] COPY model-infer/infer.py /workspace/                              0.1s
 => [train 3/5] COPY model-train/train.py /workspace/                              0.1s
 => [evaluate 4/6] COPY model/model.py /workspace/                                 0.1s
 => [train 4/5] COPY ./model-train/requirements.txt /workspace/                    0.1s
 => [infer 4/5] COPY ./model-train/requirements.txt /workspace/                    0.1s
 => [evaluate 5/6] COPY ./model-train/requirements.txt /workspace/                 0.1s
 => [train 5/5] RUN pip install --no-cache-dir -r requirements.txt                55.6s
 => [infer 5/5] RUN pip install --no-cache-dir -r requirements.txt                52.3s
 => [evaluate 6/6] RUN pip install --no-cache-dir -r requirements.txt             53.8s
 => [infer] exporting to image                                                     3.0s
 => => exporting layers                                                            3.0s
 => => writing image sha256:8524ec997259684ed1fbc14b547971afdf99c3f3c344336201306  0.0s
 => => naming to docker.io/library/emlo4-session-03-siddharthvij10-infer           0.0s
 => [evaluate] exporting to image                                                  2.7s
 => => exporting layers                                                            2.7s
 => => writing image sha256:e478556eed66cab53d127013b7e65f7698601be7381c27db90055  0.0s
 => => naming to docker.io/library/emlo4-session-03-siddharthvij10-evaluate        0.0s
 => [train] exporting to image                                                     2.8s
 => => exporting layers                                                            2.8s
 => => writing image sha256:9c9d6f861bbcbeafcc9e2404b902cf71f425e3cf5ba845bed9936  0.0s
 => => naming to docker.io/library/emlo4-session-03-siddharthvij10-train           0.0s
siddharth@AP-PF4FEVBK:~/emlo4-session-03-siddharthvij10$ docker compose up
[+] Running 4/4
 ✔ Network emlo4-session-03-siddharthvij10_default       Created                   0.1s 
 ✔ Container emlo4-session-03-siddharthvij10-train-1     Created                   2.9s 
 ✔ Container emlo4-session-03-siddharthvij10-evaluate-1  Created                   2.9s 
 ✔ Container emlo4-session-03-siddharthvij10-infer-1     Created                   2.8s 
Attaching to evaluate-1, infer-1, train-1
100.0%1     | 
100.0%1     | 
100.0%1     | 
100.0%1     | 
train-1     | Resumed training from saved model
train-1     | Downloading http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
train-1     | Failed to download (trying next):
train-1     | HTTP Error 403: Forbidden
train-1     | 
train-1     | Downloading https://ossci-datasets.s3.amazonaws.com/mnist/train-images-idx3-ubyte.gz
train-1     | Downloading https://ossci-datasets.s3.amazonaws.com/mnist/train-images-idx3-ubyte.gz to ./data/MNIST/raw/train-images-idx3-ubyte.gz
train-1     | Extracting ./data/MNIST/raw/train-images-idx3-ubyte.gz to ./data/MNIST/raw
train-1     | 
train-1     | Downloading http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz
train-1     | Failed to download (trying next):
train-1     | HTTP Error 403: Forbidden
train-1     | 
train-1     | Downloading https://ossci-datasets.s3.amazonaws.com/mnist/train-labels-idx1-ubyte.gz
train-1     | Downloading https://ossci-datasets.s3.amazonaws.com/mnist/train-labels-idx1-ubyte.gz to ./data/MNIST/raw/train-labels-idx1-ubyte.gz
train-1     | Extracting ./data/MNIST/raw/train-labels-idx1-ubyte.gz to ./data/MNIST/raw
train-1     | 
train-1     | Downloading http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz
train-1     | Failed to download (trying next):
train-1     | HTTP Error 403: Forbidden
train-1     | 
train-1     | Downloading https://ossci-datasets.s3.amazonaws.com/mnist/t10k-images-idx3-ubyte.gz
train-1     | Downloading https://ossci-datasets.s3.amazonaws.com/mnist/t10k-images-idx3-ubyte.gz to ./data/MNIST/raw/t10k-images-idx3-ubyte.gz
train-1     | Extracting ./data/MNIST/raw/t10k-images-idx3-ubyte.gz to ./data/MNIST/raw
train-1     | 
train-1     | Downloading http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz
train-1     | Failed to download (trying next):
train-1     | HTTP Error 403: Forbidden
train-1     | 
train-1     | Downloading https://ossci-datasets.s3.amazonaws.com/mnist/t10k-labels-idx1-ubyte.gz
train-1     | Downloading https://ossci-datasets.s3.amazonaws.com/mnist/t10k-labels-idx1-ubyte.gz to ./data/MNIST/raw/t10k-labels-idx1-ubyte.gz
train-1     | Extracting ./data/MNIST/raw/t10k-labels-idx1-ubyte.gz to ./data/MNIST/raw
train-1     | 
train-1     | 31        Train Epoch: 1 [0/60000 (0%)]   Loss: 0.120003
train-1     | 31        Train Epoch: 1 [640/60000 (1%)] Loss: 0.139464
train-1     | 31        Train Epoch: 1 [1280/60000 (2%)]        Loss: 0.098063
train-1     | 31        Train Epoch: 1 [1920/60000 (3%)]        Loss: 0.221962
train-1     | 31        Train Epoch: 1 [2560/60000 (4%)]        Loss: 0.189583
train-1     | 31        Train Epoch: 1 [3200/60000 (5%)]        Loss: 0.063627
train-1     | 31        Train Epoch: 1 [3840/60000 (6%)]        Loss: 0.099780
train-1     | 31        Train Epoch: 1 [4480/60000 (7%)]        Loss: 0.054971
train-1     | 31        Train Epoch: 1 [5120/60000 (9%)]        Loss: 0.137946
train-1     | 31        Train Epoch: 1 [5760/60000 (10%)]       Loss: 0.071730
train-1     | 31        Train Epoch: 1 [6400/60000 (11%)]       Loss: 0.089669
train-1     | 31        Train Epoch: 1 [7040/60000 (12%)]       Loss: 0.197461
train-1     | 31        Train Epoch: 1 [7680/60000 (13%)]       Loss: 0.202474
train-1     | 31        Train Epoch: 1 [8320/60000 (14%)]       Loss: 0.110442
train-1     | 31        Train Epoch: 1 [8960/60000 (15%)]       Loss: 0.064181
train-1     | 31        Train Epoch: 1 [9600/60000 (16%)]       Loss: 0.134522
train-1     | 31        Train Epoch: 1 [10240/60000 (17%)]      Loss: 0.070893
train-1     | 31        Train Epoch: 1 [10880/60000 (18%)]      Loss: 0.190662
train-1     | 31        Train Epoch: 1 [11520/60000 (19%)]      Loss: 0.079264
train-1     | 31        Train Epoch: 1 [12160/60000 (20%)]      Loss: 0.195683
train-1     | 31        Train Epoch: 1 [12800/60000 (21%)]      Loss: 0.115846
train-1     | 31        Train Epoch: 1 [13440/60000 (22%)]      Loss: 0.198914
train-1     | 31        Train Epoch: 1 [14080/60000 (23%)]      Loss: 0.177264
train-1     | 31        Train Epoch: 1 [14720/60000 (25%)]      Loss: 0.097441
train-1     | 31        Train Epoch: 1 [15360/60000 (26%)]      Loss: 0.055951
train-1     | 31        Train Epoch: 1 [16000/60000 (27%)]      Loss: 0.406724
train-1     | 31        Train Epoch: 1 [16640/60000 (28%)]      Loss: 0.171300
train-1     | 31        Train Epoch: 1 [17280/60000 (29%)]      Loss: 0.119668
train-1     | 31        Train Epoch: 1 [17920/60000 (30%)]      Loss: 0.051041
train-1     | 31        Train Epoch: 1 [18560/60000 (31%)]      Loss: 0.054248
train-1     | 31        Train Epoch: 1 [19200/60000 (32%)]      Loss: 0.201068
train-1     | 31        Train Epoch: 1 [19840/60000 (33%)]      Loss: 0.094062
train-1     | 31        Train Epoch: 1 [20480/60000 (34%)]      Loss: 0.116281
train-1     | 31        Train Epoch: 1 [21120/60000 (35%)]      Loss: 0.205761
train-1     | 31        Train Epoch: 1 [21760/60000 (36%)]      Loss: 0.192400
train-1     | 31        Train Epoch: 1 [22400/60000 (37%)]      Loss: 0.308049
train-1     | 31        Train Epoch: 1 [23040/60000 (38%)]      Loss: 0.143641
train-1     | 31        Train Epoch: 1 [23680/60000 (39%)]      Loss: 0.186412
train-1     | 31        Train Epoch: 1 [24320/60000 (41%)]      Loss: 0.079828
train-1     | 31        Train Epoch: 1 [24960/60000 (42%)]      Loss: 0.105329
train-1     | 31        Train Epoch: 1 [25600/60000 (43%)]      Loss: 0.092373
train-1     | 31        Train Epoch: 1 [26240/60000 (44%)]      Loss: 0.106905
train-1     | 31        Train Epoch: 1 [26880/60000 (45%)]      Loss: 0.092540
train-1     | 31        Train Epoch: 1 [27520/60000 (46%)]      Loss: 0.238980
train-1     | 31        Train Epoch: 1 [28160/60000 (47%)]      Loss: 0.077485
train-1     | 31        Train Epoch: 1 [28800/60000 (48%)]      Loss: 0.234232
train-1     | 31        Train Epoch: 1 [29440/60000 (49%)]      Loss: 0.048258
train-1     | 31        Train Epoch: 1 [30080/60000 (50%)]      Loss: 0.250890
train-1     | 31        Train Epoch: 1 [30720/60000 (51%)]      Loss: 0.236329
train-1     | 31        Train Epoch: 1 [31360/60000 (52%)]      Loss: 0.198738
train-1     | 31        Train Epoch: 1 [32000/60000 (53%)]      Loss: 0.051458
train-1     | 31        Train Epoch: 1 [32640/60000 (54%)]      Loss: 0.203519
train-1     | 31        Train Epoch: 1 [33280/60000 (55%)]      Loss: 0.120329
train-1     | 31        Train Epoch: 1 [33920/60000 (57%)]      Loss: 0.086578
train-1     | 31        Train Epoch: 1 [34560/60000 (58%)]      Loss: 0.151158
train-1     | 31        Train Epoch: 1 [35200/60000 (59%)]      Loss: 0.091952
train-1     | 31        Train Epoch: 1 [35840/60000 (60%)]      Loss: 0.184044
train-1     | 31        Train Epoch: 1 [36480/60000 (61%)]      Loss: 0.070758
train-1     | 31        Train Epoch: 1 [37120/60000 (62%)]      Loss: 0.198044
train-1     | 31        Train Epoch: 1 [37760/60000 (63%)]      Loss: 0.221744
train-1     | 31        Train Epoch: 1 [38400/60000 (64%)]      Loss: 0.231677
train-1     | 31        Train Epoch: 1 [39040/60000 (65%)]      Loss: 0.040050
train-1     | 31        Train Epoch: 1 [39680/60000 (66%)]      Loss: 0.224902
train-1     | 31        Train Epoch: 1 [40320/60000 (67%)]      Loss: 0.096600
train-1     | 31        Train Epoch: 1 [40960/60000 (68%)]      Loss: 0.140638
train-1     | 31        Train Epoch: 1 [41600/60000 (69%)]      Loss: 0.033761
train-1     | 31        Train Epoch: 1 [42240/60000 (70%)]      Loss: 0.081190
train-1     | 31        Train Epoch: 1 [42880/60000 (71%)]      Loss: 0.107872
train-1     | 31        Train Epoch: 1 [43520/60000 (72%)]      Loss: 0.152841
train-1     | 31        Train Epoch: 1 [44160/60000 (74%)]      Loss: 0.130206
train-1     | 31        Train Epoch: 1 [44800/60000 (75%)]      Loss: 0.087455
train-1     | 31        Train Epoch: 1 [45440/60000 (76%)]      Loss: 0.072160
train-1     | 31        Train Epoch: 1 [46080/60000 (77%)]      Loss: 0.102065
train-1     | 31        Train Epoch: 1 [46720/60000 (78%)]      Loss: 0.108584
train-1     | 31        Train Epoch: 1 [47360/60000 (79%)]      Loss: 0.080532
train-1     | 31        Train Epoch: 1 [48000/60000 (80%)]      Loss: 0.054104
train-1     | 31        Train Epoch: 1 [48640/60000 (81%)]      Loss: 0.092771
train-1     | 31        Train Epoch: 1 [49280/60000 (82%)]      Loss: 0.184649
train-1     | 31        Train Epoch: 1 [49920/60000 (83%)]      Loss: 0.116144
train-1     | 31        Train Epoch: 1 [50560/60000 (84%)]      Loss: 0.050905
train-1     | 31        Train Epoch: 1 [51200/60000 (85%)]      Loss: 0.102999
train-1     | 31        Train Epoch: 1 [51840/60000 (86%)]      Loss: 0.110576
train-1     | 31        Train Epoch: 1 [52480/60000 (87%)]      Loss: 0.139880
train-1     | 31        Train Epoch: 1 [53120/60000 (88%)]      Loss: 0.222104
train-1     | 31        Train Epoch: 1 [53760/60000 (90%)]      Loss: 0.024487
train-1     | 31        Train Epoch: 1 [54400/60000 (91%)]      Loss: 0.292722
train-1     | 31        Train Epoch: 1 [55040/60000 (92%)]      Loss: 0.092096
train-1     | 31        Train Epoch: 1 [55680/60000 (93%)]      Loss: 0.247555
train-1     | 31        Train Epoch: 1 [56320/60000 (94%)]      Loss: 0.122840
train-1     | 31        Train Epoch: 1 [56960/60000 (95%)]      Loss: 0.118589
train-1     | 31        Train Epoch: 1 [57600/60000 (96%)]      Loss: 0.043501
train-1     | 31        Train Epoch: 1 [58240/60000 (97%)]      Loss: 0.146476
train-1     | 31        Train Epoch: 1 [58880/60000 (98%)]      Loss: 0.058278
train-1     | 31        Train Epoch: 1 [59520/60000 (99%)]      Loss: 0.064985
train-1     | 32        Train Epoch: 1 [0/60000 (0%)]   Loss: 0.281762
train-1     | 32        Train Epoch: 1 [640/60000 (1%)] Loss: 0.328216
train-1     | 32        Train Epoch: 1 [1280/60000 (2%)]        Loss: 0.098606
train-1     | 32        Train Epoch: 1 [1920/60000 (3%)]        Loss: 0.039401
train-1     | 32        Train Epoch: 1 [2560/60000 (4%)]        Loss: 0.159213
train-1     | 32        Train Epoch: 1 [3200/60000 (5%)]        Loss: 0.095181
train-1     | 32        Train Epoch: 1 [3840/60000 (6%)]        Loss: 0.254097
train-1     | 32        Train Epoch: 1 [4480/60000 (7%)]        Loss: 0.132739
train-1     | 32        Train Epoch: 1 [5120/60000 (9%)]        Loss: 0.231095
train-1     | 32        Train Epoch: 1 [5760/60000 (10%)]       Loss: 0.120940
train-1     | 32        Train Epoch: 1 [6400/60000 (11%)]       Loss: 0.200217
train-1     | 32        Train Epoch: 1 [7040/60000 (12%)]       Loss: 0.110686
train-1     | 32        Train Epoch: 1 [7680/60000 (13%)]       Loss: 0.196104
train-1     | 32        Train Epoch: 1 [8320/60000 (14%)]       Loss: 0.174780
train-1     | 32        Train Epoch: 1 [8960/60000 (15%)]       Loss: 0.130077
train-1     | 32        Train Epoch: 1 [9600/60000 (16%)]       Loss: 0.360353
train-1     | 32        Train Epoch: 1 [10240/60000 (17%)]      Loss: 0.043277
train-1     | 32        Train Epoch: 1 [10880/60000 (18%)]      Loss: 0.075198
train-1     | 32        Train Epoch: 1 [11520/60000 (19%)]      Loss: 0.060210
train-1     | 32        Train Epoch: 1 [12160/60000 (20%)]      Loss: 0.069173
train-1     | 32        Train Epoch: 1 [12800/60000 (21%)]      Loss: 0.105193
train-1     | 32        Train Epoch: 1 [13440/60000 (22%)]      Loss: 0.087001
train-1     | 32        Train Epoch: 1 [14080/60000 (23%)]      Loss: 0.111851
train-1     | 32        Train Epoch: 1 [14720/60000 (25%)]      Loss: 0.206008
train-1     | 32        Train Epoch: 1 [15360/60000 (26%)]      Loss: 0.219978
train-1     | 32        Train Epoch: 1 [16000/60000 (27%)]      Loss: 0.037728
train-1     | 32        Train Epoch: 1 [16640/60000 (28%)]      Loss: 0.074012
train-1     | 32        Train Epoch: 1 [17280/60000 (29%)]      Loss: 0.377045
train-1     | 32        Train Epoch: 1 [17920/60000 (30%)]      Loss: 0.224913
train-1     | 32        Train Epoch: 1 [18560/60000 (31%)]      Loss: 0.093415
train-1     | 32        Train Epoch: 1 [19200/60000 (32%)]      Loss: 0.061707
train-1     | 32        Train Epoch: 1 [19840/60000 (33%)]      Loss: 0.180652
train-1     | 32        Train Epoch: 1 [20480/60000 (34%)]      Loss: 0.078409
train-1     | 32        Train Epoch: 1 [21120/60000 (35%)]      Loss: 0.132704
train-1     | 32        Train Epoch: 1 [21760/60000 (36%)]      Loss: 0.122244
train-1     | 32        Train Epoch: 1 [22400/60000 (37%)]      Loss: 0.129357
train-1     | 32        Train Epoch: 1 [23040/60000 (38%)]      Loss: 0.113507
train-1     | 32        Train Epoch: 1 [23680/60000 (39%)]      Loss: 0.169422
train-1     | 32        Train Epoch: 1 [24320/60000 (41%)]      Loss: 0.047302
train-1     | 32        Train Epoch: 1 [24960/60000 (42%)]      Loss: 0.228989
train-1     | 32        Train Epoch: 1 [25600/60000 (43%)]      Loss: 0.072442
train-1     | 32        Train Epoch: 1 [26240/60000 (44%)]      Loss: 0.159428
train-1     | 32        Train Epoch: 1 [26880/60000 (45%)]      Loss: 0.057673
train-1     | 32        Train Epoch: 1 [27520/60000 (46%)]      Loss: 0.098343
train-1     | 32        Train Epoch: 1 [28160/60000 (47%)]      Loss: 0.159371
train-1     | 32        Train Epoch: 1 [28800/60000 (48%)]      Loss: 0.113588
train-1     | 32        Train Epoch: 1 [29440/60000 (49%)]      Loss: 0.083626
train-1     | 32        Train Epoch: 1 [30080/60000 (50%)]      Loss: 0.208424
train-1     | 32        Train Epoch: 1 [30720/60000 (51%)]      Loss: 0.207902
train-1     | 32        Train Epoch: 1 [31360/60000 (52%)]      Loss: 0.177332
train-1     | 32        Train Epoch: 1 [32000/60000 (53%)]      Loss: 0.125179
train-1     | 32        Train Epoch: 1 [32640/60000 (54%)]      Loss: 0.144561
train-1     | 32        Train Epoch: 1 [33280/60000 (55%)]      Loss: 0.106453
train-1     | 32        Train Epoch: 1 [33920/60000 (57%)]      Loss: 0.160919
train-1     | 32        Train Epoch: 1 [34560/60000 (58%)]      Loss: 0.098364
train-1     | 32        Train Epoch: 1 [35200/60000 (59%)]      Loss: 0.090059
train-1     | 32        Train Epoch: 1 [35840/60000 (60%)]      Loss: 0.188143
train-1     | 32        Train Epoch: 1 [36480/60000 (61%)]      Loss: 0.123233
train-1     | 32        Train Epoch: 1 [37120/60000 (62%)]      Loss: 0.089707
train-1     | 32        Train Epoch: 1 [37760/60000 (63%)]      Loss: 0.171842
train-1     | 32        Train Epoch: 1 [38400/60000 (64%)]      Loss: 0.261674
train-1     | 32        Train Epoch: 1 [39040/60000 (65%)]      Loss: 0.089714
train-1     | 32        Train Epoch: 1 [39680/60000 (66%)]      Loss: 0.105058
train-1     | 32        Train Epoch: 1 [40320/60000 (67%)]      Loss: 0.079972
train-1     | 32        Train Epoch: 1 [40960/60000 (68%)]      Loss: 0.158286
train-1     | 32        Train Epoch: 1 [41600/60000 (69%)]      Loss: 0.173277
train-1     | 32        Train Epoch: 1 [42240/60000 (70%)]      Loss: 0.256053
train-1     | 32        Train Epoch: 1 [42880/60000 (71%)]      Loss: 0.056716
train-1     | 32        Train Epoch: 1 [43520/60000 (72%)]      Loss: 0.199347
train-1     | 32        Train Epoch: 1 [44160/60000 (74%)]      Loss: 0.074209
train-1     | 32        Train Epoch: 1 [44800/60000 (75%)]      Loss: 0.076676
train-1     | 32        Train Epoch: 1 [45440/60000 (76%)]      Loss: 0.088473
train-1     | 32        Train Epoch: 1 [46080/60000 (77%)]      Loss: 0.260641
train-1     | 32        Train Epoch: 1 [46720/60000 (78%)]      Loss: 0.172219
train-1     | 32        Train Epoch: 1 [47360/60000 (79%)]      Loss: 0.083659
train-1     | 32        Train Epoch: 1 [48000/60000 (80%)]      Loss: 0.139517
train-1     | 32        Train Epoch: 1 [48640/60000 (81%)]      Loss: 0.273821
train-1     | 32        Train Epoch: 1 [49280/60000 (82%)]      Loss: 0.173492
train-1     | 32        Train Epoch: 1 [49920/60000 (83%)]      Loss: 0.109608
train-1     | 32        Train Epoch: 1 [50560/60000 (84%)]      Loss: 0.087854
train-1     | 32        Train Epoch: 1 [51200/60000 (85%)]      Loss: 0.129037
train-1     | 32        Train Epoch: 1 [51840/60000 (86%)]      Loss: 0.307558
train-1     | 32        Train Epoch: 1 [52480/60000 (87%)]      Loss: 0.024691
train-1     | 32        Train Epoch: 1 [53120/60000 (88%)]      Loss: 0.167913
train-1     | 32        Train Epoch: 1 [53760/60000 (90%)]      Loss: 0.129642
train-1     | 32        Train Epoch: 1 [54400/60000 (91%)]      Loss: 0.082539
train-1     | 32        Train Epoch: 1 [55040/60000 (92%)]      Loss: 0.222302
train-1     | 32        Train Epoch: 1 [55680/60000 (93%)]      Loss: 0.109931
train-1     | 32        Train Epoch: 1 [56320/60000 (94%)]      Loss: 0.230067
train-1     | 32        Train Epoch: 1 [56960/60000 (95%)]      Loss: 0.090649
train-1     | 32        Train Epoch: 1 [57600/60000 (96%)]      Loss: 0.137945
train-1     | 32        Train Epoch: 1 [58240/60000 (97%)]      Loss: 0.161381
train-1     | 32        Train Epoch: 1 [58880/60000 (98%)]      Loss: 0.042063
train-1     | 32        Train Epoch: 1 [59520/60000 (99%)]      Loss: 0.252414
train-1 exited with code 0
100.0%te-1  | 
100.0%te-1  | 
100.0%te-1  | 
100.0%te-1  | 
evaluate-1  | Downloading http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
evaluate-1  | Failed to download (trying next):
evaluate-1  | HTTP Error 403: Forbidden
evaluate-1  | 
evaluate-1  | Downloading https://ossci-datasets.s3.amazonaws.com/mnist/train-images-idx3-ubyte.gz
evaluate-1  | Downloading https://ossci-datasets.s3.amazonaws.com/mnist/train-images-idx3-ubyte.gz to ./data/MNIST/raw/train-images-idx3-ubyte.gz
evaluate-1  | Extracting ./data/MNIST/raw/train-images-idx3-ubyte.gz to ./data/MNIST/raw
evaluate-1  | 
evaluate-1  | Downloading http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz
evaluate-1  | Failed to download (trying next):
evaluate-1  | HTTP Error 403: Forbidden
evaluate-1  | 
evaluate-1  | Downloading https://ossci-datasets.s3.amazonaws.com/mnist/train-labels-idx1-ubyte.gz
evaluate-1  | Downloading https://ossci-datasets.s3.amazonaws.com/mnist/train-labels-idx1-ubyte.gz to ./data/MNIST/raw/train-labels-idx1-ubyte.gz
evaluate-1  | Extracting ./data/MNIST/raw/train-labels-idx1-ubyte.gz to ./data/MNIST/raw
evaluate-1  | 
evaluate-1  | Downloading http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz
evaluate-1  | Failed to download (trying next):
evaluate-1  | HTTP Error 403: Forbidden
evaluate-1  | 
evaluate-1  | Downloading https://ossci-datasets.s3.amazonaws.com/mnist/t10k-images-idx3-ubyte.gz
evaluate-1  | Downloading https://ossci-datasets.s3.amazonaws.com/mnist/t10k-images-idx3-ubyte.gz to ./data/MNIST/raw/t10k-images-idx3-ubyte.gz
evaluate-1  | Extracting ./data/MNIST/raw/t10k-images-idx3-ubyte.gz to ./data/MNIST/raw
evaluate-1  | 
evaluate-1  | Downloading http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz
evaluate-1  | Failed to download (trying next):
evaluate-1  | HTTP Error 403: Forbidden
evaluate-1  | 
evaluate-1  | Downloading https://ossci-datasets.s3.amazonaws.com/mnist/t10k-labels-idx1-ubyte.gz
evaluate-1  | Downloading https://ossci-datasets.s3.amazonaws.com/mnist/t10k-labels-idx1-ubyte.gz to ./data/MNIST/raw/t10k-labels-idx1-ubyte.gz
evaluate-1  | Extracting ./data/MNIST/raw/t10k-labels-idx1-ubyte.gz to ./data/MNIST/raw
evaluate-1  | 
evaluate-1  | {'Test loss': 0.05652666740417481, 'Accuracy': 98.25}
evaluate-1  | Sid {'Test loss': 0.05652666740417481, 'Accuracy': 98.25}
evaluate-1 exited with code 0
100.0%1     | 
100.0%1     | 
100.0%1     | 
100.0%1     | 
infer-1     | Downloading http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
infer-1     | Failed to download (trying next):
infer-1     | HTTP Error 403: Forbidden
infer-1     | 
infer-1     | Downloading https://ossci-datasets.s3.amazonaws.com/mnist/train-images-idx3-ubyte.gz
infer-1     | Downloading https://ossci-datasets.s3.amazonaws.com/mnist/train-images-idx3-ubyte.gz to ./data/MNIST/raw/train-images-idx3-ubyte.gz
infer-1     | Extracting ./data/MNIST/raw/train-images-idx3-ubyte.gz to ./data/MNIST/raw
infer-1     | 
infer-1     | Downloading http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz
infer-1     | Failed to download (trying next):
infer-1     | HTTP Error 403: Forbidden
infer-1     | 
infer-1     | Downloading https://ossci-datasets.s3.amazonaws.com/mnist/train-labels-idx1-ubyte.gz
infer-1     | Downloading https://ossci-datasets.s3.amazonaws.com/mnist/train-labels-idx1-ubyte.gz to ./data/MNIST/raw/train-labels-idx1-ubyte.gz
infer-1     | Extracting ./data/MNIST/raw/train-labels-idx1-ubyte.gz to ./data/MNIST/raw
infer-1     | 
infer-1     | Downloading http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz
infer-1     | Failed to download (trying next):
infer-1     | HTTP Error 403: Forbidden
infer-1     | 
infer-1     | Downloading https://ossci-datasets.s3.amazonaws.com/mnist/t10k-images-idx3-ubyte.gz
infer-1     | Downloading https://ossci-datasets.s3.amazonaws.com/mnist/t10k-images-idx3-ubyte.gz to ./data/MNIST/raw/t10k-images-idx3-ubyte.gz
infer-1     | Extracting ./data/MNIST/raw/t10k-images-idx3-ubyte.gz to ./data/MNIST/raw
infer-1     | 
infer-1     | Downloading http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz
infer-1     | Failed to download (trying next):
infer-1     | HTTP Error 403: Forbidden
infer-1     | 
infer-1     | Downloading https://ossci-datasets.s3.amazonaws.com/mnist/t10k-labels-idx1-ubyte.gz
infer-1     | Downloading https://ossci-datasets.s3.amazonaws.com/mnist/t10k-labels-idx1-ubyte.gz to ./data/MNIST/raw/t10k-labels-idx1-ubyte.gz
infer-1     | Extracting ./data/MNIST/raw/t10k-labels-idx1-ubyte.gz to ./data/MNIST/raw
infer-1     | 
infer-1     | model/results
infer-1     | model/results
infer-1     | model/results
infer-1     | model/results
infer-1     | model/results
infer-1     | Inference completed. Results saved in the 'results' folder.
infer-1 exited with code 0
