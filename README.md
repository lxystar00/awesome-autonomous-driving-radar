# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-09-27 · 1,242 papers tracked · 46 curated.

**Selection rule.** A paper is listed only if it (1) is primarily about autonomous driving,
(2) has public code, and (3) shows at least one strong signal: accepted at a top venue
(CVPR / ICCV / ECCV / NeurIPS / ICLR / ICML / CoRL / RSS / TPAMI, or ICRA / IROS / AAAI / RA-L),
≥200 GitHub stars, ≥3 citations / month, or a well-known lab with traction. Papers are then ranked by a
composite score (venue, stars, citation velocity, LLM rubric for novelty / rigor / impact, SOTA claims)
with a per-topic cap. See [`scripts/rank.py`](scripts/rank.py).

📅 [Daily digests](daily/) · 🗓️ [Weekly digests](weekly/) · 📦 [Raw data](data/)

## Contents

- [VLA / VLM for Driving](#vla--vlm-for-driving) (10)
- [World Models & Generative Simulation](#world-models--generative-simulation) (5)
- [End-to-End Driving & Planning](#end-to-end-driving--planning) (12)
- [3DGS / NeRF Reconstruction & Sensor Sim](#3dgs--nerf-reconstruction--sensor-sim) (2)
- [Perception: BEV, Occupancy, 3D Detection, Mapping](#perception-bev-occupancy-3d-detection-mapping) (11)
- [Datasets & Benchmarks](#datasets--benchmarks) (3)
- [Safety, Robustness & Evaluation](#safety-robustness--evaluation) (3)
- [Industry Tracker](#-industry-tracker)

## VLA / VLM for Driving

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DeepSight: Long-Horizon World Modeling via Latent States Prediction for End-to-End Autonomous Driving](https://arxiv.org/abs/2605.10564)<br><sub>Lingjun Zhang, Changjie Wu, Linzhe Shi et al.</sub> | ICML 2026<br>2026-05<br>📑 1 | [⭐ 31](https://github.com/hotdogcheesewhite/DeepSight) | End-to-end autonomous driving systems are increasingly integrating Vision-Language Model (VLM) architectures, incorporating text reasoning or visual reasoning to enhance the robustness and accuracy of driving decisions |
| [Teaching Vision-Language-Action Models What to See and Where to Look](https://arxiv.org/abs/2607.01658)<br><sub>Yuguang Yang, Canyu Chen, Zhewen Tan et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 29](https://github.com/ShivaTeam/DriveTeach-VLA) | Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving |
| [CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving](https://arxiv.org/abs/2607.04179)<br><sub>Zhaohong Liu, Hao Ye, Xianlin Zhang et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 1](https://github.com/MICLAB-BUPT/CritiqueDriveVLM) | End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving |
| [TopoHR: Hierarchical Centerline Representation for Cyclic Topology Reasoning in Driving Scenes with Point-to-Instance Relations](https://arxiv.org/abs/2604.24119)<br><sub>Yifeng Bai, Zhirong Chen, Bo Song et al.</sub> | CVPR 2026<br>2026-04<br>📑 1 | [⭐ 3](https://github.com/Yifeng-Bai/TopoHR) | Topology reasoning is crucial for autonomous driving |
| [EgoDyn-Bench: Evaluating Ego-Motion Understanding in Vision-Centric Foundation Models for Autonomous Driving](https://arxiv.org/abs/2604.22851)<br><sub>Finn Rasmus Schäfer, Yuan Gao, Dingrui Wang et al.</sub> | ECCV 2026<br>2026-04<br>📑 1 | [⭐ 5](https://github.com/TUM-AVS/EgoDyn-Bench) | While Vision-Language Models (VLMs) have advanced high-level reasoning in autonomous driving, their ability to ground this reasoning in the underlying physics of ego-motion remains poorly understood |
| [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)<br><sub>Nan Yang, Zhanwen Liu, Linfeng Zhang et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 3](https://github.com/Zizzzzzzz/MVPruner) | Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings |
| [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)<br><sub>Yuan Gao, Wenting Miao, Mattia Piccinini et al.</sub> | IROS<br>2026-07<br>📑 1 | [⭐ 25](https://github.com/TUM-AVS/chat2scenic) | Validating autonomous driving systems requires diverse, regulation-compliant test scenarios |
| [UniDriveVLA: Unifying Understanding, Perception, and Action Planning for Autonomous Driving](https://arxiv.org/abs/2604.02190)<br><sub>Yongkang Li, Lijun Zhou, Sixu Yan et al.</sub> | arXiv<br>2026-04<br>📑 14 | [⭐ 246](https://github.com/xiaomi-research/unidrivevla) | Vision-Language-Action (VLA) models have recently emerged in autonomous driving, with the promise of leveraging rich world knowledge to improve the cognitive capabilities of driving systems |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 3 | [⭐ 476](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
| [Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air](https://arxiv.org/abs/2605.31066)<br><sub>Tianle Zeng, Yanci Wen, Xueang Yu et al.</sub> | arXiv<br>2026-05<br>📑 2 | [⭐ 1,103](https://github.com/louiszengCN/CarlaAir) | Recent aerial vision-language-action (VLA) models show promising single-UAV capabilities, such as tracking moving objects and navigating to language-specified landmarks |

## World Models & Generative Simulation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [HERMES++: Toward a Unified Driving World Model for 3D Scene Understanding and Generation](https://arxiv.org/abs/2604.28196)<br><sub>Xin Zhou, Dingkang Liang, Xiwu Chen et al.</sub> | ICCV 2025<br>2026-04<br>📑 4 | [⭐ 71](https://github.com/H-EmbodVis/HERMESV2) | Driving world models serve as a pivotal technology for autonomous driving by simulating environmental dynamics |
| [FrozenDrive: Zero-Shot Text-Guided Driving Scene Generation and Data Augmentation with Parameter-Free Frozen Diffusion Model](https://arxiv.org/abs/2606.20110)<br><sub>Yuhwan Jeong, Hyeonseong Kim, Daehyun We et al.</sub> | ECCV 2026<br>2026-06<br>📑 1 | [⭐ 10](https://github.com/daehyunwe/FrozenDrive) | Synthetic data for autonomous driving is surging, powered by diffusion models that promise scalable scene generation |
| [ASTAD: Asymmetric Style Transfer for Synthetic-to-Real Adaptation in Autonomous Driving](https://arxiv.org/abs/2606.29286)<br><sub>Dingyi Yao, Xinqi Zhang, Lihui Peng et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 1](https://github.com/Dingyi-Yao/ASTAD) | Synthetic data mitigates the data scarcity problem in autonomous driving perception |
| [Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends](https://arxiv.org/abs/2606.01164)<br><sub>Jiuming Liu, Chaojun Ni, Mengmeng Liu et al.</sub> | arXiv<br>2026-06<br>📑 4 | [⭐ 236](https://github.com/liujiuming123/Awesome-Interactive-World-Model) | With rapid development of large language models and diffusion-based content generation, world modeling has attracted increasing research attention, benefiting various downstream domains such as game engines, embodied AI,… |
| [Is Your Driving World Model an All-Around Player?](https://arxiv.org/abs/2605.10858)<br><sub>Lingdong Kong, Ao Liang, Tianyi Yan et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 253](https://github.com/worldbench/WorldLens) | Today's driving world models can generate remarkably realistic dash-cam videos, yet no single model excels universally |

## End-to-End Driving & Planning

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [$AutoDrive\text{-}P^3$: Unified Chain of Perception-Prediction-Planning Thought via Reinforcement Fine-Tuning](https://arxiv.org/abs/2603.28116)<br><sub>Yuqi Ye, Zijian Zhang, Junhong Lin et al.</sub> | ICLR 2026<br>2026-03<br>📑 14 | [⭐ 20](https://github.com/haha-yuki-haha/AutoDrive-P3) | Vision-language models (VLMs) are increasingly being adopted for end-to-end autonomous driving systems due to their exceptional performance in handling long-tail scenarios |
| [ExploreVLA: Dense World Modeling and Exploration for End-to-End Autonomous Driving](https://arxiv.org/abs/2604.02714)<br><sub>Zihao Sheng, Xin Ye, Jingru Luo et al.</sub> | ECCV 2026<br>2026-04<br>📑 7 | [⭐ 29](https://github.com/zihaosheng/ExploreVLA) | End-to-end autonomous driving models based on Vision-Language-Action (VLA) architectures have shown promising results by learning driving policies through behavior cloning on expert demonstrations |
| [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](https://arxiv.org/abs/2609.26792)<br><sub>Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.</sub> | CoRL 2026<br>2026-09<br>📑 1 | [⭐ 9](https://github.com/VAIL-UCLA/DreamStream) | Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions |
| [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)<br><sub>Shen Zheng, Anurag Ghosh, Gaurav Parmar et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 31](https://github.com/ShenZheng2000/WarpI2I) | Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs) |
| [G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance](https://arxiv.org/abs/2606.26017)<br><sub>Hang Yu, Ye Jin, Alessandro Canevaro et al.</sub> | IROS 2026<br>2026-06<br>📑 4 | [⭐ 6](https://github.com/HangYuu/G2DP) | In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors |
| [Fail2Drive: Benchmarking Closed-Loop Driving Generalization](https://arxiv.org/abs/2604.08535)<br><sub>Simon Gerstenecker, Andreas Geiger, Katrin Renz</sub> | arXiv<br>2026-04<br>📑 13 | [⭐ 172](https://github.com/autonomousvision/fail2drive) | Generalization under distribution shift remains a central bottleneck for closed-loop autonomous driving |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 11 | [⭐ 342](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
| [STAGE: STyle-controllable Action GEneration for personalized autonomous driving](https://arxiv.org/abs/2607.29517)<br><sub>Zihao Liu, Xing Liu, Yizhai Zhang et al.</sub> | RA-L<br>2026-07<br>📑 1 | [⭐ 6](https://github.com/CarlDegio/STAGE) | Driving style refers to the behavioral preferences that drivers maintain during driving, shaped by their diverse experiences, habits, and needs, and is typically reflected in varying levels of aggressiveness |
| [Latent-Centroid Steering: Single-Pass Classifier-Free Guidance for Command-Aligned Autonomous Driving](https://arxiv.org/abs/2608.00237)<br><sub>Meibo Hu, Jiamian Wang, Pichao Wang et al.</sub> | IROS 2026<br>2026-08 | [⭐ 1](https://github.com/codingmlinprocess/LCS) | Vision-language models (VLMs) have recently emerged as a promising paradigm for end-to-end autonomous driving, enabling agents to map multimodal inputs and high-level navigation instructions directly to executable trajec… |
| [SparseDriveV2: Scoring is All You Need for End-to-End Autonomous Driving](https://arxiv.org/abs/2603.29163)<br><sub>Wenchao Sun, Xuewu Lin, Keyu Chen et al.</sub> | arXiv<br>2026-03<br>📑 16 | [⭐ 255](https://github.com/swc-17/SparseDriveV2) | End-to-end multi-modal planning has been widely adopted to model the uncertainty of driving behavior, typically by scoring candidate trajectories and selecting the optimal one |
| [DVGT-2: Vision-Geometry-Action Model for Autonomous Driving at Scale](https://arxiv.org/abs/2604.00813)<br><sub>Sicheng Zuo, Zixun Xie, Wenzhao Zheng et al.</sub> | arXiv<br>2026-04<br>📑 10 | [⭐ 362](https://github.com/wzzheng/DVGT) | End-to-end autonomous driving has evolved from the conventional paradigm based on sparse perception into vision-language-action (VLA) models, which focus on learning language descriptions as an auxiliary task to facilita… |
| [Bench2Drive-VL: Benchmarks for Closed-Loop Autonomous Driving with Vision-Language Models](https://arxiv.org/abs/2604.01259)<br><sub>Xiaosong Jia, Yuqian Shao, Zhenjie Yang et al.</sub> | arXiv<br>2026-04<br>📑 4 | [⭐ 225](https://github.com/Thinklab-SJTU/Bench2Drive-VL) | With the rise of vision-language models (VLM), their application for autonomous driving (VLM4AD) has gained significant attention |

## 3DGS / NeRF Reconstruction & Sensor Sim

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DriveWeaver: Point-Conditioned Video Inpainting for Controllable Vehicle Insertion in Autonomous Driving Simulation](https://arxiv.org/abs/2606.31918)<br><sub>Junzhe Jiang, Zipei Ma, Zijie Pan et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 16](https://github.com/LogosRoboticsGroup/DriveWeaver) | A pivotal step in autonomous driving simulation involves inserting foreground vehicles with predefined trajectories into simulated scenes |
| [Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796)<br><sub>Leshu Li, Jie Peng, Yang Zhao</sub> | ICRA<br>2026-06 | [⭐ 10](https://github.com/UMN-ZhaoLab/Pocket-SLAM) | 3D Gaussian Splatting (3DGS) has garnered significant attention in Simultaneous Localization and Mapping (SLAM) due to its advances in capturing fine-grained geometry features and synthesizing novel views |

## Perception: BEV, Occupancy, 3D Detection, Mapping

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Deformable Gaussian Occupancy: Decoupling Rigid and Nonrigid Motion with Factorized Distillation](https://arxiv.org/abs/2605.28587)<br><sub>Yang Gao, Wuyang Li, Po-Chien Luan et al.</sub> | CVPR 2026<br>2026-05<br>📑 2 | [⭐ 22](https://github.com/vita-epfl/DeGO) | Understanding dynamic 3D environments is essential for safe autonomous driving, particularly when reasoning about human-centric, nonrigid agents |
| [ProOOD: Prototype-Guided Out-of-Distribution 3D Occupancy Prediction](https://arxiv.org/abs/2604.01081)<br><sub>Yuheng Zhang, Mengfei Duan, Kunyu Peng et al.</sub> | CVPR 2026<br>2026-04 | [⭐ 21](https://github.com/7uHeng/ProOOD) | 3D semantic occupancy prediction is central to autonomous driving, yet current methods are vulnerable to long-tailed class bias and out-of-distribution (OOD) inputs, often overconfidently assigning anomalies to rare clas… |
| [Revisiting Token Compression for Accelerating ViT-based Sparse Multi-View 3D Object Detectors](https://arxiv.org/abs/2604.14563)<br><sub>Mingqian Ji, Shanshan Zhang, Jian Yang</sub> | CVPR 2026<br>2026-04<br>📑 1 | [⭐ 9](https://github.com/Mingqj/SEPatch3D) | Vision Transformer (ViT)-based sparse multi-view 3D object detectors have achieved remarkable accuracy but still suffer from high inference latency due to heavy token processing |
| [FreeOcc: Training-Free Embodied Open-Vocabulary Occupancy Prediction](https://arxiv.org/abs/2604.28115)<br><sub>Zeyu Jiang, Changqing Zhou, Xingxing Zuo et al.</sub> | RSS<br>2026-04<br>📑 4 | [⭐ 138](https://github.com/the-masses/FreeOcc) | Existing learning-based occupancy prediction methods rely on large-scale 3D annotations and generalize poorly across environments |
| [Horizon3D: Sparse Radar-Camera Fusion for Long-Range 3D Perception in Autonomous Driving](https://arxiv.org/abs/2606.31096)<br><sub>Geonho Bang, Geunju Baek, Dongyoung Lee et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 23](https://github.com/geonhobang/Horizon3D) | Long-range 3D object detection is critical for safe autonomous driving at highway speeds, yet existing radar-camera fusion methods remain limited at extended ranges |
| [Explainability-Aware Frustum Attack: Exposing Structural Vulnerabilities in LiDAR-Based 3D Object Detectors](https://arxiv.org/abs/2606.29963)<br><sub>Chengzeng You, Binbin Xu, Soteris Demetriou</sub> | ECCV<br>2026-06 | [⭐ 1](https://github.com/SecMindLab/Saliency_LiDAR) | The structural vulnerabilities of point cloud-based 3D object detectors remain poorly understood |
| [PointLAM: Local Attentive Mamba for Efficient Point-based 3D Object Detection](https://arxiv.org/abs/2609.21780)<br><sub>Xuanming Shang, Weijia Zhang, Chao Ma</sub> | ECCV 2026<br>2026-09 | [⭐ 3](https://github.com/PointLAM/PointLAM) | 3D object detection from LiDAR point clouds faces a fundamental dilemma: voxel-based methods achieve efficiency at the cost of geometric quantization, while point-based methods preserve fidelity but suffer from prohibiti… |
| [Native-Domain Cross-Attention for Camera-LiDAR Extrinsic Calibration Under Large Initial Perturbations](https://arxiv.org/abs/2603.29414)<br><sub>Ni Ou, Zhuo Chen, Xinru Zhang et al.</sub> | RA-L 2026<br>2026-03 | [⭐ 12](https://github.com/gitouni/ProjFusion) | Accurate camera-LiDAR fusion relies on precise extrinsic calibration, which fundamentally depends on establishing reliable cross-modal correspondences under potentially large misalignments |
| [Benchmarking Multi-View BEV Object Detection with Mixed Pinhole and Fisheye Cameras](https://arxiv.org/abs/2603.27818)<br><sub>Xiangzhong Liu, Hao Shen</sub> | ICRA<br>2026-03<br>📑 2 | [⭐ 8](https://github.com/CesarLiu/FishBEVOD) | Modern autonomous driving systems increasingly rely on mixed camera configurations with pinhole and fisheye cameras for full view perception |
| [Vernata: Self-Supervised Learning of LiDAR Point Representations](https://arxiv.org/abs/2608.06919)<br><sub>Oliver Lemke, Alexander Liniger, Abel Gawel et al.</sub> | IROS 2026<br>2026-08 | [⭐ 17](https://github.com/rai-opensource/vernata) | LiDAR serves as a primary sensing modality for robots operating in outdoor environments |
| [Towards Compact Autonomous Driving Perception with Balanced Learning and Multi-sensor Fusion](https://arxiv.org/abs/2606.02979)<br><sub>Oskar Natan, Jun Miura</sub> | arXiv<br>2026-06<br>📑 44 | [⭐ 9](https://github.com/oskarnatan/compact-perception) | We present a novel compact deep multi-task learning model to handle various autonomous driving perception tasks in one forward pass |

## Datasets & Benchmarks

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [SearchAD: Large-Scale Rare Image Retrieval Dataset for Autonomous Driving](https://arxiv.org/abs/2604.08008)<br><sub>Felix Embacher, Jonas Uhrig, Marius Cordts et al.</sub> | CVPR 2026<br>2026-04 | [⭐ 9](https://github.com/iis-esslingen/searchad_devkit) | Retrieving rare and safety-critical driving scenarios from large-scale datasets is essential for building robust autonomous driving (AD) systems |
| [Towards All-Day Perception for Off-Road Driving: A Large-Scale Multispectral Dataset and Comprehensive Benchmark](https://arxiv.org/abs/2604.27499)<br><sub>Shuo Wang, Jilin Mei, Wenfei Guan et al.</sub> | RA-L 2026<br>2026-04 | [⭐ 6](https://github.com/wsnbws/IRON) | Off-road nighttime autonomous driving suffers from unreliable visible-light perception, making infrared modality crucial for accurate freespace detection |
| [123D: Unifying Multi-Modal Autonomous Driving Data at Scale](https://arxiv.org/abs/2605.08084)<br><sub>Daniel Dauner, Valentin Charraut, Bastian Berle et al.</sub> | arXiv<br>2026-05<br>📑 2 | [⭐ 396](https://github.com/kesai-labs/py123d) | The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics |

## Safety, Robustness & Evaluation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [CCFM: Collision-Constrained Flow Matching for Safety-Critical Scenario Generation](https://arxiv.org/abs/2607.04451)<br><sub>Ke Li, Kaidi Liang, Yuxin Ding et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 3](https://github.com/KELISBU/CCFM) | Evaluation of autonomous vehicle (AV) planners in safety-critical closed-loop simulation is essential for real-world deployment |
| [Lipschitz Optimization for Formal Verification of Homographies](https://arxiv.org/abs/2605.23203)<br><sub>Jean-Guillaume Durand, Panagiotis Kouvaros, Maxime Gariel et al.</sub> | CVPR 2026<br>2026-05 | [⭐ 2](https://github.com/jeangud/homography-verification) | The adoption of vision neural networks in regulated industries requires formal robustness guarantees, especially in safety-critical domains such as healthcare, autonomous vehicles, and aerospace |
| [CADET: A Modular Platform for Evaluating Distributed Cooperative Autonomy in Connected Autonomous Vehicles](https://arxiv.org/abs/2606.04072)<br><sub>Pragya Sharma, Brian Wang, Mani Srivastava</sub> | ICRA 2026<br>2026-06<br>📑 1 | [⭐ 0](https://github.com/nesl/cadet) | Deep learning models are increasingly central to autonomous vehicle (AV) pipelines, yet their integration has traditionally followed a monolithic design where perception, planning, and control execute on a single onboard… |

## 🏢 Industry Tracker

Latest 14 days of news, official blog posts and new open-source repos from tracked companies. Full daily feed in [`daily/`](daily/).

<details><summary><b>Waymo</b> (76)</summary>

- 📝 2026-09-24 [Our Vision for London: How Waymo can Support a Safer, Connected UK Capital](https://waymo.com/blog/2026/09/visionforlondon) <sub>official blog</sub>
- 📝 2026-09-22 [Introducing transit rewards](https://waymo.com/blog/2026/09/transit-rewards) <sub>official blog</sub>
- 📰 2026-09-26 [I rode in a car with no driver. Apparently, my survival instincts retired before I did.](https://news.google.com/rss/articles/CBMiwwFBVV95cUxPY0dfNW84ZmFOQ0JRUmlKMFZDVEEzbURPaGxFbU5vdUlZNTgzTWI1bmd6LXQ1cWNkdERDUkswV1piSC1rRG9STU5pbzVDQ2o2N2Fjdi1pdmpqMnZmTzVYVGZodDd1cU5saVgxeXYtdmw0WDI0WFJ3N21Dd2lJa09SdzJVNkVNVnRQYWxNeTI3ZUdzVW5JNldFMm9oaTZOZTFZN19vaWIxaHQ3TnZwYlVrVEo2SXg2cjN5M2dhdUVtQTVuSGc?oc=5) <sub>SILive.com</sub>
- 📰 2026-09-26 [Journalist Alarmed When His Waymo Barges Into Path of Presidential Motorcade](https://news.google.com/rss/articles/CBMihwFBVV95cUxPbUFkT0NoZWxibEVfRndIcTlXdkRPT2diUXB5R1Fwc1M1VC1CVHF5NWYtUXZYdUduSjdLNXdidXZ2RjV0Uklpd2M2d1l4RXhOZmxMNC15R3Z4WTVYR3Q0UDNKLVJILUlSYzVMclUyTzNCaFpCZ0tfdklLUkhfTkNfQ2d1bmJ6dWM?oc=5) <sub>Futurism</sub>
- 📰 2026-09-26 [💥 Driverless cars crash 68 percent less than human drivers](https://news.google.com/rss/articles/CBMingFBVV95cUxQOGRBM3ZyZDVrTlhxdElNMm5mTDBXSk44c3d0dmJwTjFyNnpMQ29KVXBhWF9xdGdpUm4zRjZrMTdmZ19YR05BNlpKQWNaS0VmNzBFMmpfbE8zWjhDb3ZqU2tvYlhHblZMVEFRUEhSODZEbkxxY0ZZVTBEd1FEY2dodGU0a25XNzBsQ3BMd0JqQjkySGVnaHo4ODg3WV9WUQ?oc=5) <sub>warpnews.org</sub>

</details>

<details><summary><b>Tesla</b> (107)</summary>

- 📰 2026-09-27 [Tesla Robotaxi Charging: 4 Details That Matter](https://news.google.com/rss/articles/CBMihwFBVV95cUxQM1NTWFYxQzdFeWUwMTYySGU1d2pPbmtOOVNXMzJLWGJUUUFMZFZWV21GSUl0YXJZakVIRE5hMV9SWlZCNmdzMHMtaC1YVGhJRmVHT0NWRjlWUzBiV1hxdEFjekU4ZFlIMkp5N3gzRmNuM1k1b1c1LWR5NkNYY3lPY1AxNUJrd1U?oc=5) <sub>BASENOR</sub>
- 📰 2026-09-26 [Tesla's Cybercab Just Turned 2021 To 2024 Model 3 And Model Y Into Used Bargains With A Catch](https://news.google.com/rss/articles/CBMicEFVX3lxTFBTaXFTY2d2VWlVakswMnFjZHZzU2g2a1czelU4MlVkd3RDQk1GckM5d2N0US1IcEZqemIwUmROOV9RVlV3WV9aTmpZSHozZnkwSlZLczBFTUpPdDAxOG9nX2drNmlLOC1NcU15aVNucUw?oc=5) <sub>CarBuzz</sub>
- 📰 2026-09-26 [Tesla Full Self Driving Unsupervised Soon? And Further Conversations with Ara (the Grok AI Bot)](https://news.google.com/rss/articles/CBMiygFBVV95cUxOamcxSlJGUEM1T1VPbmdBNTJXLXJkNmZ2SlhScnRQdDAtdjBwZ0tfOFN2ZGstSFM4QUZETlp2UGdndXVfbUM4VkRaMXJreXE3TkhjMWJfS291TFNZOGxhNGtVYzQ5Umh5OXhkTVlrQlpmNnFzQk1WaWJDQXFsZ21yRFRMZUtCZktjTkhOeDF0RktYeVJYRldEZHUyVGYtWXFmb1huYlZPYXVOdHZuSjVvSmRvTjhaTE1PNzFjUjliMGJvdV9NdkVxaW5R?oc=5) <sub>CleanTechnica</sub>
- 📰 2026-09-26 [Tesla in Talks for FSD Approval in Ireland as EU Delays Vote](https://news.google.com/rss/articles/CBMioAFBVV95cUxOalRUNGxsNFJYa0swcWJVbnlONEVYQWwwUkkzWFI5eHdDM0ZpX1ZHb3FvVVRVMnZqTFcwUncyenVRRGVYN2JyZ1h6dEM4UzBUR05LZnppU2RKaFNRVkNOaVpQUE04N29uUWpVOFMxcnk1M2VfTkthUjUycnFxYjFMZG53VEp4c2FuRlJkbDhrTkZveUNEUExyMnFGY3JQamtL?oc=5) <sub>Not a Tesla App</sub>
- 📰 2026-09-26 [Move Over, Tesla: This $140 Billion Company Looks Like a Superior Robotaxi Investment](https://news.google.com/rss/articles/CBMilwFBVV95cUxNZzQxaFB0bExYYVFzZ09tVm96bXh0bUd3TUVvTmRBaDFIUU00NDBnSk9NbWpsOFNMaWJ0LUZJbXc4LXJJQzBscVV2UVJ4c0k5WU1GOVJVUmtHNlJFN05hSm9aWFZzX2tKUXVLaU1OQXZ4Z3U1eXpUQk1RVzAtc19vekVnREdZU1FNTnhpcWZHQ21aSmhTb2RF?oc=5) <sub>The Motley Fool</sub>

</details>

<details><summary><b>NVIDIA</b> (68)</summary>

- 💻 2026-09-18 [NVIDIA/swe-serve — SWE-Serve: an agentic benchmark of 53 production inference-engineering tasks derived from merged SGLang pull requests, run with Harbor.](https://github.com/NVIDIA/swe-serve) <sub>GitHub</sub>
- 💻 2026-09-16 [NVlabs/Skill2Env — Democratizing Collective Intelligence](https://github.com/NVlabs/Skill2Env) <sub>GitHub</sub>
- 📰 2026-09-26 [NVIDIA Powers Robotaxi Fleets With Full-stack AI Platform](https://news.google.com/rss/articles/CBMiekFVX3lxTE1oWFY5enlNbVRVeVRwZFRiZnkyOF9XYkxZMG92NTdHUEtpRDFLZS1Wa25BN2JJR2RiLWVJNkU3czJXcTZWMDVZLU42NGNoRDVaZkpwbEpBZTRkUkFCbi03R3MwVi1NeUxOT1hfdk9jY2ZkTFVpdm1PejVn?oc=5) <sub>Quantum Zeitgeist</sub>
- 📰 2026-09-26 [Nvidia Trades Near Its 52-Week High at Its Cheapest Valuation in a Decade. History Says This Is What $1,000 Invested Could Be Worth by 2030.](https://news.google.com/rss/articles/CBMimAFBVV95cUxNR2l3Z0tLMHFfRjdGZFNsYmVsTjJpSGFyNW5rckFwS0Nlbk1lM05HTmZYMk5BZTJLS2RSWF85S3VBczRvSVlpaktULTZMRnllX2RMVUI1SnQ0cThrajB5VE9NVDZGWU04cmxhRDZveW43amhQR1lpOWFIRU10OG13Q3dSWnFkRzM0ak8zd25fa3JfU3Jpb1lGYg?oc=5) <sub>The Motley Fool</sub>
- 📰 2026-09-26 [NVIDIA CEO says to 'just stop' AI if worred](https://news.google.com/rss/articles/CBMilwFBVV95cUxPMFJHWkp4NGFaQVNydklBTFlGWlJQUmNPcEhKamxxekU3NHRiOWFiVGFvbEYtZ0NnSnAwNG15ejh0ZnJXcjN1Rm4tNEFkU1B0VDc4UHIzSjR3bWlETWJkM1dNSWR4dFFWWmxaX1h6V2JXZmZIOFJGZkNLUDA3VUk3WFdfRmktbUN0T05OVGxvRFhRd2NBdU9n?oc=5) <sub>KLTV.com</sub>

</details>

<details><summary><b>Wayve</b> (35)</summary>

- 📰 2026-09-26 [Mercedes-Benz Outsources Conecto Bus Production to Otokar as Buybacks and Wayve Deal Offset 31% Shar](https://news.google.com/rss/articles/CBMi3gFBVV95cUxOblBCamdVWXA2dk9pZGMzbGgzMGdyNzQtMVM2YUwwY09hd1FsbnNDcEFQX1RjYkRuT2JvRlhOMHd3TU9GbWkwb3pQZEhEQlBOS1ZmcEFlNXRmYXBoVHhOZE55RUs5dU5ka0UyOHhWZ0ItRjkyZTZLZGZLSURubVc3aUoyMVJ5c3NPcUtUT0FzcWZfSnJnWlUzWFJ6SjB6T3RjNGlXa2ROWk9WQk85ZmtHUDFXUUJxNkFJSGVULXZkRXA5RkdhMnF5WDFtNEk2RE5JV1FaZGY3bW5ISFduN1E?oc=5) <sub>AD HOC NEWS</sub>
- 📰 2026-09-25 [Nvidia says major robotaxi programmes use its stack](https://news.google.com/rss/articles/CBMihgFBVV95cUxQTHhGZTBYWHpUSEUxSHFzVkhWemRhRHNxV2haQkJoQTE3dGFRWVJUNWhTSXNqSzBha0RnZC1BcnRzRXBiRTBaVzQ5VHhhVUZZd2gwbUdtbXJLOGl2SWxuZmxrX2Y2VWVSRDdyZnBxWklQR09CODJfVGF2UEVwVThGT2dWT2xfQQ?oc=5) <sub>IT Brief UK</sub>
- 📰 2026-09-25 [Light Hits: This Week in Collision Repair](https://news.google.com/rss/articles/CBMiogFBVV95cUxPYlJMTl9ONnlacXpzWUFMR2I1RlFNYkExeWdnZU5uRUxjYmFiY0ppMXM1TWNZZFZPV3FDQ1FWSm9oOVV6S1pGanZIa0tBazFjZ19ZTXNXOWFMTnlXLVB5RTNZb2FKN29BYW1razdqMV9GYU5HM29wRUROc2hSMUhCQVlYUXBYcDF1YVJLU0FKa3hQdENJSnpXV2tFYWxxVTZGbUE?oc=5) <sub>fenderbender.com</sub>
- 📰 2026-09-25 [Mercedes-Benz Bets on 2028 Autonomous Driving Rollout While Squeezing German Labor Costs](https://news.google.com/rss/articles/CBMi2AFBVV95cUxOWXVMQlJzXy1UV0JoTTE4LW9teml4WjRsNDU0aGNkT2FnNUthSVd3cHhzYjNleTIxYUxSeHhBN3E1a3VPVkQ1UmxMcjZKeWN0WWtTaGNIMUEtTDBZZUVXSWgwNHJUWGNFY0wzLXo4eUVwa1F0UVRvY1FONk1jYkJITUQtRHlZdVFsaUZRTF9DLWg1bmJLRVdERF9WZlFMQ0dJU3ltdWFwb3ZabjN0SFVJSFg5d1oxNzhRNno3a1VIaDdIbW5aODdvMUFkQVpHWTZSbGJmbDZyamw?oc=5) <sub>AD HOC NEWS</sub>
- 📰 2026-09-25 [Uber Launches Robotaxi Service In London After Nigeria Exit](https://news.google.com/rss/articles/CBMiigFBVV95cUxPRlNoeXVmVV8tNFJfNWg0cmdQdzA1QWF3Y1RWX0ZwRlV3UkJ1VllLdGo5UXc4a3l0WU1KWGp3eXJwVU5DSmRWM2dCNEdzbEJ0RFNCb3J6dlc4Qk9HSm4wRUZ1c2FGUmZ6SlJkamdJSFZiQ2pZV2tkcWtzZ21vS3VYWTNzWE8weDFPOFE?oc=5) <sub>LEADERSHIP Newspapers</sub>

</details>

<details><summary><b>Momenta</b> (72)</summary>

- 📰 2026-09-26 [【视频】乡间无标线窄路，Momenta R7智驾竟能稳如老司机？](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBUYi1wd1U0aG1JV1daWjNxVHp5S09iZU5uaHZhTDVsSFZkaVZIdHh6ZVNKdGlLNVZKQUM5OXE5NlNvQzEzczFGTUhDdThwc0Rxc1VlVXZGbEc1b2M?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-26 [大众09智驾功能详解：ID.ERA 9X能否靠L2+城市领航反攻新势力？+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE51WS1OVVl2X3Q2SkNpenh1WVloT2Uxb1dnUXVyM3FGVVBfYXdJUjJUangzS3F5bmt5aUE2cjBTN0E2eFMtSllQUUpXOTVZazhhVmgwd09GQlVncEZoRVZCQ0FqZ2M3aVhGQmNmUHRXeUZJdw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-26 [上汽大众ID.ERA 8X空间智驾长续航，25万级德系旗舰](https://news.google.com/rss/articles/CBMic0FVX3lxTFBQdVlIWWtUeVhYZi1INnBrOWVwNmxjam5TX1VieURhTmxkN2tKeEZRbHNkY1UtVVZ4bG9xRUdIV29VbnFURndoeXFraTVPT0ZVLVZWNnFZVVI1ZS1kSFRCbjU4U2V2bDEwd1lkaElRcXg0c1U?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-26 [13.99万东风日产N7最值配置](https://news.google.com/rss/articles/CBMia0FVX3lxTFBrR21BWUlNM2ltUjJtbXlqRk9iOU9fcE45X041QktYRjBFOHY3MGFNYmtYdVpZenV1N0dhREZYSkFsXzdQbmRzeGlZOWhscHEyU1A5TVhXVlZuTjM0SVdkOGZibXNFV0dnNU1v?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-26 [【视频】探店凯迪拉克全新XT5 PHEV，兼顾性能与油耗，还有Momenta R7](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1EU1k1b1BjVjZLRll6WFFKbWwtTlBLUUJqcXYwa3NwM180T29uanpSdDFYVlBOaHFjM3FDc3luY2RqNnhmc0V6WjdQejFYUC05SGlLQUVTVnF4MU0?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>XPeng</b> (103)</summary>

- 📰 2026-09-26 [15万买纯电SUV，小鹏MONA L03跑625km和铂智3X大空间区别在哪](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBpS3hDRU5MODVWX3JWTTlWUnd5Um5oNXhTYUpwZ05oWkxaZXZ3bW9sZVdBWGtNQzZCWHh4dHB4VnlUbTd6N01iRGZhSzBYaUdaNUd2WEtHdjFaWXc?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-26 [小鹏MONA M03真实测评：十几万配满血智驾，后排真是唯一短板？+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE10Z0dQeWFqdkp6RmR3QTY3alU1QmJKRjZHNFc5WkpwU0V1bGMyRFJLMkl2MDdnb09LRXVLemVJNkM0TmdOWnFHQmJ4alAyVmI0S3ZjVU9Ycnk4N0Q4TVBvQkpoX1RVYk9LV05XUEUwVnYyZw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-26 [小鹏GX纯电续航实测：打几折？高速能跑多远？3个真实场景告诉你答案+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE0zdHduVmRHTUI1SDVMdFUyalVwelJVTEowSU1kQWZuQjd5bEJEeWlOaTFZMmtMYS14dmRzS0VILW1kWjE0eE55QUk4TEQ5bWtCN2p2NnNaQV9pdXp4M2hR?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-26 [11.98万起，750TOPS智驾下放！2026款小鹏MONA M03值得买吗？3个维度说清+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFAzak9FRFUyOVg5OThHRW9PYVoySFBDLXhnWF90T3Faa3B6a1J2QUh0NTBSS0NkckRzdWNrdmV5a0I5Z2JEeGEtZGE4N2p5czZpOGtPNWNlMTdIM3ZIckhGQlJ4dUVEWGxoWmhDNVRaYWlaZw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-26 [小鹏 G7 和 G6 谁更值得入？](https://news.google.com/rss/articles/CBMiXkFVX3lxTE04Vi1CZ3R4WXRkZjZSUlhybzZjenREaE1PU2dNTXJudmNDTmwxeVRpeGpmM0tlY1M5T2JFNnpOSW1fT0hRWVdYZzRnUEhkalBVR2tSTk0wZEFXdEM3dWc?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Li Auto</b> (72)</summary>

- 📰 2026-09-27 [理想ONE停售4年还值得买吗？二手11万起，3个维度说清+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTFB5M1RSU3p5R0hOOXFuNTdKSjNOdXdPbVNlZ2V1QlEzbVdZdVFVR2N0U1FTWmE1RkZKc1FkQUZwdkt1cXdFQkJGT0xiZjRqS2lTZjVvRVFVQkxuZ3AyMUdN?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-26 [一篇文章说清楚2026款全新理想L9优缺点，能否再次续写昨日荣光？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE8zUWpSa19TTEVmREVFNUNPR1NORWM2aE11dHVRNjA3Z0M5anRuMGRTNWNQYzBYekhmRm5FdEM1amRxV3Fjd3FZSzI1bzFNNGo1dVBqTnVZSmRHT28?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-26 [零跑D19值得买吗？21.98万起“半价理想”如何选？3个维度说清+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE92Q0VfTHh5Uk5ES05NNm1RMDBjd2hSZDNMd1RyVGNtLWFFWWtveTNEamtwNWRHaFRQX2ZuY2RHNDhSSGRjeEpycE1XS3JqRjlyVVFnQjJITTJVWEZ3dHFn?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-25 [理想汽车广告抄袭沃尔沃？沃尔沃发文：有些经典，总在一次次重温中被铭记\|理想L9\|智驾\|宣传片\|风波\|车辆_手机新浪网](https://news.google.com/rss/articles/CBMiqwFBVV95cUxNbE1DZVQ1NmdHcUJ5aHgzUjNxamhWWUZRaWUzcGJBSWd0anJGaDVSdkJhcUxndFd4eFlwTFMyM2o5YXUzcDJtbXlvWVpvVlc2YWVRakxjTWRFUXJGU000YjBYb0RVRDZ1b2ljaHhfb1g1U0tuSnVFR0g2MmhwdzlEV0xReVBzTkdhazY5cWpTb3Q3NXI2d2VDVHZBNkc0c0psQVVjaWxuaDFpaFE?oc=5) <sub>finance.sina.com.cn</sub>
- 📰 2026-09-25 [Dongfeng to trial-produce humanoid robots by end-2026 – Xiaodong to work in car plants, human-level by 2027](https://news.google.com/rss/articles/CBMi0gFBVV95cUxOMjVuUXVZWGJ5eDZhUDliVGFkenA1UGpMZExsemlkeUVwMVB4eFJuZm1kcFpYdzFSSmxwc3BXdmtkVlFaRzhmNVJ3ZE1GcDJfei1sZHVLWkExLVprUU1CaThQQlBWRDNrdlBMUEdybjBwSV81RS03dk9UM1FCZDg5OThiS0VYS1J1aWhsUERrMDd3emxJLXZEclVOc3otUGJ2YU9IY3VUWDU5UERTZlRBWjFlUmYxUjNJV0hBYTM5eG9fZnA3Z091VzFqaG9ZUFhHSkE?oc=5) <sub>Paul Tan's Automotive News</sub>

</details>

<details><summary><b>NIO</b> (74)</summary>

- 📰 2026-09-26 [【视频】体验蔚来ES8，有品质更有品位](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBVWWNvaE9Zd1VJVGR0cTZoYW5PS1p0RDdLQXB1eU5lOEloU3BSQU92MGNld1ZJT25wWlk0RFdWQUZ6cEI0enRhMnVkM3JpVzZtYVhkR0hvMXhYVzQ?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-26 [蔚来Cedar S雪松1.6.0全量推送，辅助驾驶雨天策略与NWM高光时刻同步上线](https://news.google.com/rss/articles/CBMiWEFVX3lxTE53RDY5SEh4bHpKRFZEcU0yLVJicjhGdllkc2FiMTd3RWtsajRxYzdCdDdrMjNBTjVwMHNHcHREVG1INEtFY0hkdWUzMUlfWVJveTVzQ0U3bTk?oc=5) <sub>news18a.com</sub>
- 📰 2026-09-26 [蔚来EC6灵韵特别版上市：36.98万起值不值？3个维度深度评测+FAQ](https://news.google.com/rss/articles/CBMifkFVX3lxTE9XRWVPNi1ITzVvUjNfUnEtaXF0YnpXazItczNKQlZKRXhwQ2JPVzU0ckUxVWVmWEhnb2J0dFVhRnVMUVdlbzNiTDdpc09vVUMyd1dpM0V4bi1fcUxOa0tmTGNYc0hXQmp5RU14LXd4clJmSlF6WXVfbEkxVDdYQQ?oc=5) <sub>新浪财经</sub>
- 📰 2026-09-26 [捍卫旗舰身份？新款蔚来ES8，支持5C超快充倍率](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9BcDVuZ2RzQ3FOMzRfUGNFS0kxcTJVOEtmNUNfdkhFa0ZEeERZMURjVk1yRktMdlRBLVVWUVd3OWdVTjZQWWN6djVFVGkzajFUNmJOY0ZiMFZ1RlE?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-26 [【视频】买下！！22年蔚来es6 性能版外灰内灰行驶8万多公里](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9vendVZVhGcjd3bUY2NXpYSU81U0IzbDh5Z19Ld3kydVhPVENscV9CX2xuV3RHR21MZWJmLVlnczMwZGZqYlR3Qk1VWW8xS1VpZVhSNkZ4MEcwNmM?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Huawei</b> (132)</summary>

- 📰 2026-09-27 [27.98万起！全系华为ADS 5+鸿蒙座舱6，奕境X9四款配置怎么选？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1iSGhVNkJJTG5NTEU2Mm44dnRLdGItbDc5TDYtZFh5cUNqM3hYcU5CMlBwc1FHMHZzZHBEckE1WkF3NnJTZXVCS0lkVWhtX3daRXUwLXprYlE0MVU?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-27 [【视频】全栈华为乾崑智驾，猛士X700挑战“盲驾”迷阵漫游！](https://news.google.com/rss/articles/CBMia0FVX3lxTE5RNXJkYjY3Y3FJUURKcU5UR05nRDRrMzR3RWczY1lIYlhoWFFsNTh4LXBXSkhScGdFQnNiZUhvQW1HT2V4RlVfaHAzeUdoT2pralNtUGZhdWdRZzItWFVIY0pWLVhPal9LSG1v?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-27 [【视频】泰山X8用实测告诉你：智驾看华为乾崑，底盘看岚图虎踞](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBPcGM4c1pYREhqZ1JobThRNXk1UGNvRFdpXzA2NXNxYXRnWHE1Uzl0UUc0enJkVnhsdEhhSTYwU045amo4UGxLb28wWWJfZDY5NTNGTkxHVFhYczA?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-27 [北京越野泰钽700首批交付 24.98万起华为乾崑ADS 5装进了硬派越野](https://news.google.com/rss/articles/CBMiW0FVX3lxTFB3b2dJTkNfX0FSdzQxMUsyQWhEdkZ3SVhXV1R5dWJDVXZOdkpTcWpJVGZncW4xaFBDaGFJNWpJUnU2dXdCSmJ2bmczVHBOMWhnZWtpb3gtZEJFUGM?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-27 [多花6100块，星海V6多1个座位和35km续航，值吗？](https://news.google.com/rss/articles/CBMia0FVX3lxTE5DbDMweVNOR3lpbC1NVnRLYXlMdzQyNExrRlo1RVdVcnU1M1B0ZkE3b2tjeVBMdWRJSlVnajA0dGFSTTBLNUFIMmR3UGNEMDZaNm1lQmVlVi1QYjZaMU1rSWN3ejYtU0Y3Z1Jn?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Baidu Apollo</b> (37)</summary>

- 📰 2026-09-26 [Is Tesla the Savior of Robotaxi? Unveiling the Truth Behind the Autonomous Ride-Hailing Revolution](https://news.google.com/rss/articles/CBMiU0FVX3lxTE4zVUdoQ201TVNPb3V2NXhmRkhoaVc2RGxPWGxGV1NJRHZvRk02QUszU252WlNWT0R6eFNrYVNwWm5JNldDa00xSUc0V1dHQTI2Q2Fj?oc=5) <sub>eu.36kr.com</sub>
- 📰 2026-09-26 [The Robotaxi Reality Check You Won't Get From an Investor Deck｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1oVm5UbjMzU3RzeTlQUTNNQkkzdUUxMWFzalpCZlJIMGdKQWx5ZVo4eU1mQW9MWWxEdlFZSjlpUHRXMDRQd19uRkRVcWRCNmxEd2JraF9nVC1zd0ZDRDBj?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-09-26 [特斯拉Cybercab进入商业化运营，Robotaxi竞争转向运营效率与成本控制](https://news.google.com/rss/articles/CBMiVEFVX3lxTE5iYm1EU2d3RHV1dzE1ZmVWYnVlR01GR0dPZUdidERtdjAtLXlWZnFTUk94VTVMT0ZkMHV6bHl4bHJ3UHNNS0lRME55dUI4NENMZjVpaw?oc=5) <sub>虎嗅网</sub>
- 📰 2026-09-25 [亚慱app官方网站上线！通勤族、孕妇、老人出行神器](https://news.google.com/rss/articles/CBMicEFVX3lxTE1RZXRDNm1wNFBKa0gxTXdkeHdKZDNxcHFQV3FISU42Z1Fqd2RYaEJpOGhEeWRmZ3NrNm5yV0dHcGhsNmdsNlpXdzlxYmp1M0xEeG8tYnVmNmlJTlN1RFVRWUdvOWNGbFM2TjBILUFuVlA?oc=5) <sub>womenofchina.com</sub>
- 📰 2026-09-24 [Waymo is Taking Robotaxis to Tokyo. Can Alphabet Get Ahead of Uber in Japan?](https://news.google.com/rss/articles/CBMiowFBVV95cUxNY2RtWFhhOHpQemRpdFhYNmFRdjNuaUdxbnFlNmlOa1V6djUtMkdlaUxrN3FqQk1Id2R1Z0pTTTc2YmtCWFd4aGd5Sk9vekFjM0I0VHd4UHBwQTlINEFkMzBnMWxTUXoxYUpyNkY4MktIWEdwSWZ1clV3YnBfZjI5RGFZOHJYNGdfUVhnVlZUbDU4ZnlPQ2N4WmNuY2JtUUU4amhj?oc=5) <sub>Yahoo Finance</sub>

</details>

<details><summary><b>Pony.ai</b> (58)</summary>

- 📰 2026-09-26 [Is Tesla the Savior of Robotaxi? Unveiling the Truth Behind the Autonomous Ride-Hailing Revolution](https://news.google.com/rss/articles/CBMiU0FVX3lxTE4zVUdoQ201TVNPb3V2NXhmRkhoaVc2RGxPWGxGV1NJRHZvRk02QUszU252WlNWT0R6eFNrYVNwWm5JNldDa00xSUc0V1dHQTI2Q2Fj?oc=5) <sub>eu.36kr.com</sub>
- 📰 2026-09-26 [哈米电玩app官网下载荣誉揭晓以影像续写电影梦-体坛网_体坛+](https://news.google.com/rss/articles/CBMibkFVX3lxTFBSYmZyX2VCZ2YtZEhvX2FQVEtHUnFZZGpBekN1a3l4VThhcEw0T0J4YmpMZkdodld5V2c1cHZfM2l3TWlJbllPLWNTcWhfelZ5N2NISHZmdWNpOUo0cnZhWVJEdTkwT1ZKSTNjWXdn?oc=5) <sub>体坛</sub>
- 📰 2026-09-25 [苹果创历史新高，市值一夜猛增5000亿元，中概股走低，陆控跌近9%，国际油价跌超2%，俄美乌三方会晤或近期举行](https://news.google.com/rss/articles/CBMijwFBVV95cUxPMHNPTnA1Z2JxbXVsQWh5MlJVTnZndkZEcTM4bTlmNmZDQjk4ZWNXdWI2Mm5ESnc4MEhuM1JkSlI0ay1qRkw4N2h0eHJHcTgzdXQwOXZYUW1VU05OV2owRHBJR0p0YnZFaTJPQzNybDE5cEdXN2VOcTMySnBiMmJMNVM5eUVkMUM0S1dnc0k0RQ?oc=5) <sub>21财经</sub>
- 📰 2026-09-25 [纳斯达克中国金龙指数跌超0.5%，DCX跌15.26%](https://news.google.com/rss/articles/CBMiY0FVX3lxTE9iOVNFR0t4ZlBJQUlSazlEMWZ1S2R1NkR0X05zQTQ5NXlFTXo5dHBnMUJMc0JaZEVaRHJrOXZ0aTczLVB0eGltbUQzNWJkdW02ajEtbFFPYkxWWkQ4a2Jta1psaw?oc=5) <sub>东方财富</sub>
- 📰 2026-09-25 [汇丰将雪佛龙目标价从每股218.00美元上调至250.00美元。](https://news.google.com/rss/articles/CBMiT0FVX3lxTE4xRjZFYm9oSGFpQlFzeldPT0w3V2ZhSGpUbXB1Zmxzc1lDbzZKS2hIV2piY0JOOTVMWVd4VDllSVBMYnY1Z3QxYjF5WnBiSDQ?oc=5) <sub>finance.sina.com.cn</sub>

</details>

<details><summary><b>WeRide</b> (50)</summary>

- 📰 2026-09-26 [苹果，逼近5万亿美元](https://news.google.com/rss/articles/CBMiYkFVX3lxTE43dkc1bEhpYmIyVmg5THpQaW1wd1lraUttMjlQZ2trOXcxU1dQbWVrSzY1MGRCUUpWbEhYLWNyc3lBaE8zRThVVWt4TE1GMzJDai15MWFnUVVSNk1kcWFlOHdn?oc=5) <sub>同花顺</sub>
- 📰 2026-09-26 [Is Tesla the Savior of Robotaxi? Unveiling the Truth Behind the Autonomous Ride-Hailing Revolution](https://news.google.com/rss/articles/CBMiU0FVX3lxTE4zVUdoQ201TVNPb3V2NXhmRkhoaVc2RGxPWGxGV1NJRHZvRk02QUszU252WlNWT0R6eFNrYVNwWm5JNldDa00xSUc0V1dHQTI2Q2Fj?oc=5) <sub>eu.36kr.com</sub>
- 📰 2026-09-26 [Uber’s $100 Million Charging Bet Is More Than Just About EVs](https://news.google.com/rss/articles/CBMifEFVX3lxTE1TLXJ5UXJlUVMwU1RTbTQ1TXFnSGp1VHFTOFRJVFdONTFzX1Jra1Z3WWdJQmNtMVVrZ1E2UjVxMTNSLWR4ckpnZ0tra3FhZmlQS01saURXZ1JRbFpyajUxYlNIU2ZoSTVwcVRuSWdEZHgyWFp1VjM0Z3FXcjc?oc=5) <sub>InsideEVs</sub>
- 📰 2026-09-26 [特斯拉Cybercab进入商业化运营，Robotaxi竞争转向运营效率与成本控制](https://news.google.com/rss/articles/CBMiX0FVX3lxTFB0aFZWY0xDenV3THlBUHd0Zl9zaTFoeFdzeWcxYVRDZXpsaDZLY1J4VDhTenVwXzExdXpFbmtGYk9CUlpxOFhZc2ttWjlfMHFMY19DRm1FWWs1a3c3SzlN?oc=5) <sub>虎嗅网</sub>
- 📰 2026-09-26 [埃安i60反向虚标，实测续航552.5公里超标称](https://news.google.com/rss/articles/CBMic0FVX3lxTE1CYkdqWlBrSDlUMHRkQVVnSXhEdTE1ekhPeE92dV9ieEwzWVkxcDFQTjF1dXRRMXoyLWtrbTRMbUdwZnhmb3otTUgwd21XOTRqNWg2Tnk2U291SjA3NzlhVllYTVNhLXdpMnk1NUlCaTdrYmM?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>Horizon Robotics</b> (53)</summary>

- 💻 2026-09-24 [HorizonRobotics/CogWAM](https://github.com/HorizonRobotics/CogWAM) <sub>GitHub</sub>
- 📰 2026-09-27 [启源Q06智驾不靠供应商方案，长安的“自研”牌含金量有多少](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPRU0tYUdxdW5KdXoxU1hmRmFMQlg4aFQ3WERsSXVteU1FcHhHMjUwVmNLbTlWSzd4R2Fib3F5aWhMOW9ac3pFYWNSVHN5TlRvRVIyU0dHRm04SlRhMkJwZlpJV3o5UTV4TVhLc3BwX0o1Wi1JdS1pYXQ3WXZuYnlEQVNqUkhVSmdm?oc=5) <sub>搜狐网</sub>
- 📰 2026-09-26 [地平线开放日：11年积累，从智驾走向物理AI超级平台](https://news.google.com/rss/articles/CBMiYEFVX3lxTFBRcmxPNURJcGk3clNOOWRpRHNiU0oyaU5ZUDJLdjRYcV9xZFhWUWpyb2RRMTRDS2J1M016NXZuT3BRYlNUWXdoNmN0Vk5JZ01mbmM0cUhnVnFKVWZDeFNrZg?oc=5) <sub>cosmopolitancn.com</sub>
- 📰 2026-09-26 [吉利银河E5 H5智驾搭载地平线J6M芯片具备全场景能力](https://news.google.com/rss/articles/CBMic0FVX3lxTE9VUWYzb2JKa1VvemlpaTdrdTM4b2ozcll4TnhLMUxQcm9hSlhiNS1NdlF2RHdlQ2ptbnBmMnNtRk54WEJ1Z29lbzlXb3g2N0xkWmhlVEs2LW9mTk5xN2lxcTNzMDZMMFlPLXVSVHRFYjFtSjA?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-26 [【视频】买不起特斯拉就选它！深蓝S05比油车省好几万，车主都说很不错！](https://news.google.com/rss/articles/CBMia0FVX3lxTE1SZzNnSllOTVJNX2F0bGRuME8tMlpWQWg3aHZIa3RrVUhYNEkxLThvWGxwcG1UUGRCa3pERnV1ODFid2VFQ1VaSHAwaktTOXJ1ZlFuZ2ZaU0JDUlRsWTZMUUh6VjNhSFlNQWFN?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (10)</summary>

- 📰 2026-09-25 [摩根士丹利MD误发内部机密文件，泄露约60个Deal Related项目及多家公司上市计划](https://news.google.com/rss/articles/CBMiX0FVX3lxTE05S1BTM1N1NnBXT1kwSWpaeWhsVDdWdmlXNlQ2MDR1YkwwU1FTX3R4cFJGSnNNWjRxSHh2eXRWRWNmWG1OMGpCdDl4X2w1Y1VqWjBSMktLVDA3bk5YZHpn?oc=5) <sub>huxiu.com</sub>
- 📰 2026-09-25 [万博官网max发布：AI助手上线，下载量突破500万，响应提速40%](https://news.google.com/rss/articles/CBMiW0FVX3lxTFA2dlhnbGlqTl9XbWRPaHF4SlFSVjV2aFBRelpCNDFxYjMtd1EzaEhMZ3d2bElhRXhLNDYtZVNiRzlKZDdTRVQ2TFJweU1INkQzMGNoU1VTTktWbDA?oc=5) <sub>体坛</sub>
- 📰 2026-09-24 [@元戎启行DeepRoute vs特斯拉FSD，高难度挂壁公路谁更丝滑？ ​](https://news.google.com/rss/articles/CBMigAFBVV95cUxQM25aR1dYajhUNEpiRW5UNDY2cmNUSzF1cjBadF94TXZmWHM3d19PLVlydlZiaVBNbFF4c3VfZGw5U1ZlTmtDVzY0WnRGS3NocHFTdkVrb1NpNGNVbmZ1Ukw0NmJUSVJsYVJ1N25EUmZ2RVBjYWFpWVNraWFzSTdDRQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-22 [赛力斯的辞“旧”迎“新”](https://news.google.com/rss/articles/CBMiU0FVX3lxTE5HTzhXM1hKdGZKS3ZweFB3cDEwbVlRUG1yVWNRbm45aGhSOU8wSlFqWk0wOHVvTXpBMjJDckxrellEWDhTR1pjLWpqYkRnWEpWSjNz?oc=5) <sub>搜狐网</sub>
- 📰 2026-09-21 [从技术参与到议题共建，元戎在顶尖学术会议ECCV给出AI安全“方法论”](https://news.google.com/rss/articles/CBMifkFVX3lxTE5pUHQtNEtWOElVek1QbFF1b29yWDRhWFg2ZU4wTF9OX2hNZjVkTWdHNWowX29DOFBNVk00MUNmMTRiR3JWeXd1ZjJoWDF0WVNYOG1SOTN5VkJ4ZmozSmhnT0EzMGZJSUdzc29tU2wyakJqallMTHNOTC1BX3Mydw?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>Mobileye</b> (7)</summary>

- 📰 2026-09-25 [Mobileye Global, Inc. Class A (MBLY) Live Share Price, Invest From India](https://news.google.com/rss/articles/CBMie0FVX3lxTE11MFdpQnBMczBkWUF5azl2bE1SaUIwT0Nhb2tLU3NPdTdtX2R0U3BSV2toUnNFN1puX3BqaEE2ZHJuRHdlN2N4dDY4a3NuZktyZFFSREFFQXhRTlVSbENxcUw3SHZ6VWRpN2tqZ0lmWHNkR3JuaXZWY0dXRQ?oc=5) <sub>INDmoney</sub>
- 📰 2026-09-24 [VW’s MOIA Starts Robotaxi Rides In Orlando](https://news.google.com/rss/articles/CBMiekFVX3lxTE5meUdldmgzNmRkbFlWLXlHU2J1RmVQRmlreWZqdDBRMVRud1NIV2tXdDNEdFBjYmU0NmdMel95UUdITUVtZVhZQ1BPSGo3R0syb0M0aVBrZWVvRWRGeHcwVEt6TEh2emZiX0RiSURXVFFrWC1TSUdjVjBR?oc=5) <sub>finimize.com</sub>
- 📰 2026-09-24 [Ruqi Mobility: Data Sales as a Business Model](https://news.google.com/rss/articles/CBMiuAFBVV95cUxQM19Zb2x4SzlmVk1pbGZkMXpHMGhGbURBa2tUWUMtOXVCQ0EyMTFkRDBkcWd0QlotcFJnU2hDRWZ5ZzdpQkx5cWswRFd5MHlXbkVNUFJFRVpZaUFtQWhYcnZkUXczRFlEUGZrN0paMTZQRjhkS1lXWEotSnZyZWpMYVRzSTgtSlFwMEtyNmVMT0ZHeWtBOFl4czRHeEcyX1JmOEhiUVlsb0tNNTJBOHFyaEhGSUtjWUJT?oc=5) <sub>All-About-Industries</sub>
- 📰 2026-09-24 [BlackBerry Falls 2% Despite Record QNX Quarter and Raised Full-Year Outlook; Mobileye Holds Steady](https://news.google.com/rss/articles/CBMi1wFBVV95cUxONnJLWWpPQU9jMVpXamNpVkVmRXJzNEFRZDgwc3dnclNXQW5LSWpTdnd2VVBIaXlpV3Zfal96akpOOFEyckVuN2FGU3IzbEZkSk9BQklFeElKbFdDbVJjZEVPUUJ0dXJqVHlZS1BmNW1xeGRTc1N3ZWdJZm1VLXpHbm90Ykt6MHJZd0xrZUhNUExPcm93UGNjRTliaC1sX25LTzBJZ0lOREk5clNoQjFOTXlWRUVUNXBnamY3ZWZRRVVkN21xZU95UXZBMkJRcUFWYldnYTJfVQ?oc=5) <sub>24/7 Wall St.</sub>
- 📰 2026-09-24 [VW unit MOIA begins US robotaxi rides with Orlando rollout](https://news.google.com/rss/articles/CBMilwFBVV95cUxPYnU2TE5ueVZuRmlzdVVON2NsYmxxOHY1NXhwUnkyWjdqYmFwOHJxdDNmejRQenFUQnRlSkN2RW1WTVR4dDJtdFdrVkM0T1ViS3ZZX29FVnZMVUFWa1JYcExzSHFTVXkxeFVucnpBaDBHUWVuR2xjS21VeEF5aVF5cjJlaHdJSUVId2NqOG1OMThxeDVQQzQ0?oc=5) <sub>Reuters</sub>

</details>

<details><summary><b>Aurora</b> (27)</summary>

- 📰 2026-09-26 [Aurora Showcases Commercial Driverless Trucking at Investor Day](https://news.google.com/rss/articles/CBMitgFBVV95cUxOWGNkTTJweWNXNXpNVEc3YzlxQWEyRHF6b09YVGluTFg3dFdOV0JLRXc0R0ctYkZGSVBGUjBneDBhVWhsejgxQkMyeGlpTURuRnJHV3hpS2tnSVhxYWhMVHZYWlA4NVJmY3ZLOGJQLVJnSmpMYzFKd2tyVkp1N2E1V2c4Wnh0RDR2Ni1fUklZRThFY3VhRTN5Sno4VE5mRjE0WkMwRmZrZUpSbjRpV2lzVHhENTlCUQ?oc=5) <sub>TipRanks</sub>
- 📰 2026-09-25 [California Opened the Door to Robot Semis. Most of the Homework Gets Done in Texas.](https://news.google.com/rss/articles/CBMimAFBVV95cUxOcVBYT3E4VnRUV182R3Juc2FocTB0Wi1VNE5YR2lYT1k1NjJuUEpyLTFpVWVzUlM5T3FKRGRCVWdkSXR3LUVnZGxHYTJDWm9BVWFDQTV4Sm9lVGR6d0Z2elhJczl0RzV3Y2tjUG85dG1XaEtoQTJDMEpkcFRnQXN0UUxOc3lxQTV0UHBaV19jQ0dOM055LU5iVQ?oc=5) <sub>theautowire.com</sub>
- 📰 2026-09-25 [Tesla Opens First High-Volume Semi Factory in Nevada to Boost Big Rig Production](https://news.google.com/rss/articles/CBMiggFBVV95cUxNWGhfbGRwenZCM2Y3SXFCaDNlSlJ4ZEo4d205OHdKcnhTTzZHSE94WmZ3dlFPb192dTE2UEtOUGFnNExqNXJxN21VUEZkR1YyTTVQVlYxZENMTjJXS2FJN0ZLaUlyT2RTdUtSRkkzTlFWdVY5aG1vVHZhZVhRd1F3NTl3?oc=5) <sub>TIKR.com</sub>
- 📰 2026-09-25 [Tesla starts up first dedicated Semi truck mass production plant in Nevada](https://news.google.com/rss/articles/CBMivAFBVV95cUxPc2htcy1lVmlsMExiLU1wYVJIUEhfZ0VKaUxfdkcyV2RHYnVWalkzNTdrdFluMkQtWXRKLVVLSDgwUGlGQWl6cVlKWG5lbjVBeHJlOHNvZ05rWTBlY0NRREJpR182S1d6YzRGT0FEZkl3SkQyamtVNW9DTWk2STJhMGtBakxrdEtSVGttWHcyb1RDeGFyWHJpVnhoMWh3YTRtMUg1Tk9JbFh1NHptTHVhNkdsYUNxckNqc3RUVQ?oc=5) <sub>디지털투데이</sub>
- 📰 2026-09-24 [Aurora Innovation Targets 30,000 Driverless Trucks, $5B Revenue by 2030](https://news.google.com/rss/articles/CBMixwFBVV95cUxOT2RxazR6ZHRvQk1GVWVOT3hSTnFkaFJkVTZxRnE3TVFzQjVHNWZEQ29YOVlBaUd3LW9YS2JmNE50bmJHdjhjWTg0cEdLWmJoSTR4Z25xOUx4SzAxSTdGZzE2VW1NLXJJT1FFaUFXOENXcVc3aXFFUTFqYktIMUVrTEI2Vm50Z0RnSTNBSUF3aEF1OFoxeVUyV3RTQVdnSVEybnR1bEp4TmZjRGhhcklDU2hKbnAwRkVVUUZHb3JObXRLR1pwd3M4?oc=5) <sub>MarketBeat</sub>

</details>

<details><summary><b>Zoox</b> (43)</summary>

- 📰 2026-09-27 [Zoox robotaxi crash on Las Vegas Strip raises questions about driverless safety](https://news.google.com/rss/articles/CBMirwFBVV95cUxOanNQaVZhWGh5dkdFOXBWUHdlVlNncnE5aHdINGRrai1uWi1UdmZHUF9zNHMydkJoTnhEMUdscnBmMUZVQm9HMFlZdnNvYllFM2VXQ3NvSGtqRXFkZFVaZW05dk50aXBLbU9EZzF2aVVJQTVDeU0tazhnNWlLeGVZS2tELWhNUkpBVGsxM1ZhQWk2eWZVbVk1ZTNEd2o2ak9LOGh6aC12eHk0Zl9Jelpn?oc=5) <sub>KSNV</sub>
- 📰 2026-09-26 [Zoox Robotaxi Crash Injures Nissan Driver on Las Vegas Strip as Multiple Incidents Accumulate in 2026](https://news.google.com/rss/articles/CBMi6gFBVV95cUxNbTJpUjQ1YnpwWUlKWGZ2Z243bUp2OG9tbGEtZVdjZ05rc3ZmUUNVSGxJbkk0akJUMFl1a2lNeEJrWERmTmxGcnhwT1g1LXk5ZmFIN2NXU0VZTlh3UnJHTTRzMFd6Mi1LN05SZG9jcmtrZi12bWhjM0w5ekpMdl9CSzhqYXlPVVdtQjQySzBRVlFfQUpoaTdnUTZ2Mk5Fb3lITC1uOC1ORXItWVo1bTQ3d0ZVNF85WUhYdFNfTWxyWGd3Sm1YX1Axb2ZadVA5UDlfQzU4UlRLemU2NC01aEhIWGppQm1rcDYySkE?oc=5) <sub>SCCG Management</sub>
- 📰 2026-09-26 [Zoox Robotaxi Crash on Las Vegas Strip Hospitalizes Driver](https://news.google.com/rss/articles/CBMingFBVV95cUxNZEhYQ3htQUlZenVjRk9nM3hYWEh6alFFRGkwa1VYNE9Sdl9KcWFmcmtZc3NWRGowYWUtX2FfOEZFYVRLZVRXM0s5QVFROXhCd1JvWTN0Q3ZNTEUtc184UGh1RUNUSWxmem8wYVVGM3IyZ040N2d0SmZSQjQtdlQyM0RZM21jNkg2OHhUU3Fwbl82Z2ZRWVdZdm1aUExuUQ?oc=5) <sub>Casino.com</sub>
- 📰 2026-09-26 [US: 1 Hospitalised After Zoox Autonomous Vehicle and SUV Collide on Las Vegas Strip (Video)](https://news.google.com/rss/articles/CBMiyAFBVV95cUxNUGJZSnM2ZVRLT1BWaTBsODFGYUZXSWNaMGxHaGduc2FDZXFmS2JSUDZKTzcyejFtX2NfNm9pbFNZclN6TVZ1eXR4bVFuZlNvVUcyVVE0LXktbzlmRG9iUTFuR2tYRUxfZVZkWkh3MEVCdkRkaURvc1AwS05FcHkwRTh2OEszNjdSbXo5TVBfaTFlQzBZejBhU0duRVJBZTRyQU5xTW5LS3hRLWw0eFdnVTlNa2tDM1Z5MFJpZWFiajVWSWZybktqVdIBzgFBVV95cUxQR0FYam9vTDlPWDJnajVHQTlCb0c1TnJIcTM4NW9iUkQ3RGNJRzhnR29kd05lUTh5ckNULW51WmktRUhDUnhYdmR3cHhPTlJ5cWxXWG42MXQ1Q0xFdVdIaHV3Y1BGUkx5eVlJMlUzNkxtWXRNck56Ry0zZUhkSDZCVEM1Nk11MjF2T1BGaVowaHVXN0x5TE5SdzRCWmw5dWdzajJLajF0bE1qMzZ1U0lQYjBUdk4xbG4wT21FVnlQRXV0bUM0QTVYcXltVkVoQQ?oc=5) <sub>LatestLY</sub>
- 📰 2026-09-25 [Driver hospitalized following crash with Zoox vehicle near Las Vegas Strip](https://news.google.com/rss/articles/CBMipAFBVV95cUxNclN0cXJsUGFLYms2dW5wNE9rRFJHMDlnZGxoNTNpR0FfTmtfZG1MbVM4TnY2T0xGbnhGQjI1OXEtZEF5MDhHZGNsbjNRMWRwOGlDQjI2QkpGTmxqc0NJY0JaaDFiX3d6TW1LUko4ZDRyM3NpY3c1TTBuWE5hRWRjclpfRG5sTk5xZDloalMtcE8wS1ZsUVdITHhjTjBqNlN2ZE5KWtIBuAFBVV95cUxNSGRKVmxKMjFkZmpuZWROc3ZhMGxuZGVkTThRMVRnMnFtLUJxNEZTSEZFNHkzeWt3RFl0Z3NjWW1PeHJfLXJ6Q3ZPenhhb2JjY3NxZmdWb2o4Y243bG1TMU9sU00zaHptUHZNa2I0bExHeEZsMS1QNjFhWVBlSk05d3pKamlOVDdJWGRSNElNRWxERkVOV0I0OWhmZWxoVG1XemJZbDgzZmY0ZGNRRkdQUi15dS1Cbmhi?oc=5) <sub>FOX5 Vegas</sub>

</details>

<details><summary><b>Motional</b> (11)</summary>

- 📰 2026-09-26 [Walter Piecyk and Grayson Brulte: The Robotaxi Bottleneck Is Depots, Not Software](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBlREZaMnNLXzJxMGdBNUQ0S0Y1VGxGb0NqVWJtZVpfOGl2SW9pZnNhRFpacjVLUUdFOG10S0ozWHFVazVveWkxQUt3dnNNeFlyU1BiVlNTNjlreWs?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-09-26 [The Robotaxi Reality Check You Won't Get From an Investor Deck｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1oVm5UbjMzU3RzeTlQUTNNQkkzdUUxMWFzalpCZlJIMGdKQWx5ZVo4eU1mQW9MWWxEdlFZSjlpUHRXMDRQd19uRkRVcWRCNmxEd2JraF9nVC1zd0ZDRDBj?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-09-21 [Hyundai to Build Tens of Thousands of IONIQ 5 Robotaxis for Waymo in the US as EV Strategy Shifts Toward Autonomous Mobility](https://news.google.com/rss/articles/CBMi7wFBVV95cUxQc0QyV2VOamV0NmZXTzJDb1NqeFRfblA5NXdXcWZ5S0tuaGxsa0k2Vi12V0N6WDkxRjdfWUlKNG5jUWtWQy1DOGtMZ1M5Uml2a3hkZUdSSHNab3BtTlJOaXplclpRZjNocVN4a0dHWGpCbHNpZUN6ZDZCaUwwcE9MZXo4SDBrY09jdXNSVld1SDZfaEluLWZ1WEJVaFRPdkJBMnRtVDFXR1RicEZEdzdITkVTZjNJbkJ0bklOcExMN28wN0xXTmg0S1I1b2RCNEg5eHhISHU3eFcyVzBIei1WcnZvb2dSOVhzSVFhcTFMTQ?oc=5) <sub>EVTech.News</sub>
- 📰 2026-09-19 [Hyundai Motor turns to robotaxis as U.S. EV demand slows, to produce at Georgia plant](https://news.google.com/rss/articles/CBMiwwFBVV95cUxPNEtaQl80RDhIbFNaWDJkRGQwMllxQzdMZ0JxZC1EcEsxdUdkWWJqMzlRbVFVOGc5VF9Ta2cxZEl0b3o3ZEhjeUczZTdDWmdaTUg0VGppeUhuX1dKbUdMLWJ5X1VSOWFxYmZiYWlGQ1ZiT0NDRmJ0YkZiNWRTQWV1SnFIc2hyNVh4Q3dYRE5UWXJJUFoxTEEweng3MExUWnVtaFllalBTZ3dfQ2ZjSXFsWWRzLWw3Nkl4SDFLNzJrVzdxU1k?oc=5) <sub>디지털투데이</sub>
- 📰 2026-09-18 [System helps humans predict when self-driving cars will make mistakes](https://news.google.com/rss/articles/CBMirAFBVV95cUxQY2xDYi02dkFwc3hwX3ZOdmliM2JNWUlhUVFXQ2lIeFRxNjJKVHE5T2REVUVIWGY3YzByNE5OWjd3RU52R3Y1NWFydmtHMU5CZUIya2NhQnMzYXJqRDlSY2tSUW10XzAyY2JYV0l5UGlHX096TFZGX3g4bTczZEFacTF3R3BXVkJ2LUU0VHh2RTRpdWxxQVB5Z3NjVnlfM2pMWG11Q1hrVFRkekJH?oc=5) <sub>Technology Org</sub>

</details>

<details><summary><b>comma.ai</b> (37)</summary>

- 📝 2026-09-16 [Bugs that broke driving: Machine Learning edition](https://blog.comma.ai/ml-bugs/) <sub>official blog</sub>
- 💻 2026-09-15 [commaai/comma_hack_7 — some chestnut examples](https://github.com/commaai/comma_hack_7) <sub>GitHub</sub>
- 📰 2026-09-26 [GPT-6 Astra is the first model to drive a real Corolla on its own](https://news.google.com/rss/articles/CBMijwFBVV95cUxNM0llcjdUV1l5U2Jvc0ZTaWhrdmh2bHctM29ubFp6RWdRemtXNDFmZWhvcW5mNXRidE9FTEFCcXl3MkNhTHdUbHRqSDZRWVNDNGQ0OHFFNzBmSWZONzVZSFhfaUhWdF9WcE5mQjBCT21WZWt5TE1pZjlCRjVDT1RXY2NITlN0dTNZdUQySndKZw?oc=5) <sub>Pasquale Pillitteri</sub>
- 📰 2026-09-26 [Only 15 Minutes, Riau Researchers Offer a Way to Get Water to Put Out Peat](https://news.google.com/rss/articles/CBMiQkFVX3lxTFA2aTZXWGtxRHBaczVwMFBwRENsMHpBQ292MVBzMEpHbF8wTXpjekdqeElmVnM1a2VVWEN0YUZPZGM4dw?oc=5) <sub>VOI.ID</sub>
- 📰 2026-09-25 [Minister of Foreign Affairs Sugiono Emphasizes National Ownership as the Key to Sustainable Peace](https://news.google.com/rss/articles/CBMiQkFVX3lxTFBaQzYwNXpHTG1CRFJzbXJQc3VKN0RuQ0dTenJ1SzZYOUhHVEljMVQwWV9zd1UtUzB4UXYxdFE5QnZ1UdIBQkFVX3lxTFBaQzYwNXpHTG1CRFJzbXJQc3VKN0RuQ0dTenJ1SzZYOUhHVEljMVQwWV9zd1UtUzB4UXYxdFE5QnZ1UQ?oc=5) <sub>VOI.ID</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
