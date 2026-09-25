# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-09-25 · 1,256 papers tracked · 42 curated.

**Selection rule.** A paper is listed only if it (1) is primarily about autonomous driving,
(2) has public code, and (3) shows at least one strong signal: accepted at a top venue
(CVPR / ICCV / ECCV / NeurIPS / ICLR / ICML / CoRL / RSS / TPAMI, or ICRA / IROS / AAAI / RA-L),
≥200 GitHub stars, ≥3 citations / month, or a well-known lab with traction. Papers are then ranked by a
composite score (venue, stars, citation velocity, LLM rubric for novelty / rigor / impact, SOTA claims)
with a per-topic cap. See [`scripts/rank.py`](scripts/rank.py).

📅 [Daily digests](daily/) · 🗓️ [Weekly digests](weekly/) · 📦 [Raw data](data/)

## Contents

- [VLA / VLM for Driving](#vla--vlm-for-driving) (9)
- [World Models & Generative Simulation](#world-models--generative-simulation) (5)
- [End-to-End Driving & Planning](#end-to-end-driving--planning) (12)
- [3DGS / NeRF Reconstruction & Sensor Sim](#3dgs--nerf-reconstruction--sensor-sim) (2)
- [Perception: BEV, Occupancy, 3D Detection, Mapping](#perception-bev-occupancy-3d-detection-mapping) (10)
- [Datasets & Benchmarks](#datasets--benchmarks) (2)
- [Safety, Robustness & Evaluation](#safety-robustness--evaluation) (2)
- [Industry Tracker](#-industry-tracker)

## VLA / VLM for Driving

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DeepSight: Long-Horizon World Modeling via Latent States Prediction for End-to-End Autonomous Driving](https://arxiv.org/abs/2605.10564)<br><sub>Lingjun Zhang, Changjie Wu, Linzhe Shi et al.</sub> | ICML 2026<br>2026-05<br>📑 1 | [⭐ 31](https://github.com/hotdogcheesewhite/DeepSight) | End-to-end autonomous driving systems are increasingly integrating Vision-Language Model (VLM) architectures, incorporating text reasoning or visual reasoning to enhance the robustness and accuracy of driving decisions |
| [Teaching Vision-Language-Action Models What to See and Where to Look](https://arxiv.org/abs/2607.01658)<br><sub>Yuguang Yang, Canyu Chen, Zhewen Tan et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 29](https://github.com/ShivaTeam/DriveTeach-VLA) | Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving |
| [CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving](https://arxiv.org/abs/2607.04179)<br><sub>Zhaohong Liu, Hao Ye, Xianlin Zhang et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 1](https://github.com/MICLAB-BUPT/CritiqueDriveVLM) | End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving |
| [TopoHR: Hierarchical Centerline Representation for Cyclic Topology Reasoning in Driving Scenes with Point-to-Instance Relations](https://arxiv.org/abs/2604.24119)<br><sub>Yifeng Bai, Zhirong Chen, Bo Song et al.</sub> | CVPR 2026<br>2026-04<br>📑 1 | [⭐ 3](https://github.com/Yifeng-Bai/TopoHR) | Topology reasoning is crucial for autonomous driving |
| [EgoDyn-Bench: Evaluating Ego-Motion Understanding in Vision-Centric Foundation Models for Autonomous Driving](https://arxiv.org/abs/2604.22851)<br><sub>Finn Rasmus Schäfer, Yuan Gao, Dingrui Wang et al.</sub> | ECCV 2026<br>2026-04<br>📑 1 | [⭐ 5](https://github.com/TUM-AVS/EgoDyn-Bench) | While Vision-Language Models (VLMs) have advanced high-level reasoning in autonomous driving, their ability to ground this reasoning in the underlying physics of ego-motion remains poorly understood |
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
| [Bench2Drive-VL: Benchmarks for Closed-Loop Autonomous Driving with Vision-Language Models](https://arxiv.org/abs/2604.01259)<br><sub>Xiaosong Jia, Yuqian Shao, Zhenjie Yang et al.</sub> | arXiv<br>2026-04<br>📑 4 | [⭐ 225](https://github.com/Thinklab-SJTU/Bench2Drive-VL) | With the rise of vision-language models (VLM), their application for autonomous driving (VLM4AD) has gained significant attention |
| [DVGT-2: Vision-Geometry-Action Model for Autonomous Driving at Scale](https://arxiv.org/abs/2604.00813)<br><sub>Sicheng Zuo, Zixun Xie, Wenzhao Zheng et al.</sub> | arXiv<br>2026-04<br>📑 10 | [⭐ 362](https://github.com/wzzheng/DVGT) | End-to-end autonomous driving has evolved from the conventional paradigm based on sparse perception into vision-language-action (VLA) models, which focus on learning language descriptions as an auxiliary task to facilita… |

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
| [Towards All-Day Perception for Off-Road Driving: A Large-Scale Multispectral Dataset and Comprehensive Benchmark](https://arxiv.org/abs/2604.27499)<br><sub>Shuo Wang, Jilin Mei, Wenfei Guan et al.</sub> | RA-L 2026<br>2026-04 | [⭐ 6](https://github.com/wsnbws/IRON) | Off-road nighttime autonomous driving suffers from unreliable visible-light perception, making infrared modality crucial for accurate freespace detection |
| [123D: Unifying Multi-Modal Autonomous Driving Data at Scale](https://arxiv.org/abs/2605.08084)<br><sub>Daniel Dauner, Valentin Charraut, Bastian Berle et al.</sub> | arXiv<br>2026-05<br>📑 2 | [⭐ 396](https://github.com/kesai-labs/py123d) | The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics |

## Safety, Robustness & Evaluation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [CCFM: Collision-Constrained Flow Matching for Safety-Critical Scenario Generation](https://arxiv.org/abs/2607.04451)<br><sub>Ke Li, Kaidi Liang, Yuxin Ding et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 3](https://github.com/KELISBU/CCFM) | Evaluation of autonomous vehicle (AV) planners in safety-critical closed-loop simulation is essential for real-world deployment |
| [Lipschitz Optimization for Formal Verification of Homographies](https://arxiv.org/abs/2605.23203)<br><sub>Jean-Guillaume Durand, Panagiotis Kouvaros, Maxime Gariel et al.</sub> | CVPR 2026<br>2026-05 | [⭐ 2](https://github.com/jeangud/homography-verification) | The adoption of vision neural networks in regulated industries requires formal robustness guarantees, especially in safety-critical domains such as healthcare, autonomous vehicles, and aerospace |

## 🏢 Industry Tracker

Latest 14 days of news, official blog posts and new open-source repos from tracked companies. Full daily feed in [`daily/`](daily/).

<details><summary><b>Waymo</b> (60)</summary>

- 📝 2026-09-24 [Our Vision for London: How Waymo can Support a Safer, Connected UK Capital](https://waymo.com/blog/2026/09/visionforlondon) <sub>official blog</sub>
- 📝 2026-09-22 [Introducing transit rewards](https://waymo.com/blog/2026/09/transit-rewards) <sub>official blog</sub>
- 📰 2026-09-25 [Waymo vs Tesla Self-Driving Safety: Key Data Reveal](https://news.google.com/rss/articles/CBMidEFVX3lxTE5yQU9QZ3h6bExfVE9nSGwyaFlCN2tlVk5sLWw3bzdMM1RTWG9LSk0tVXlJV05KQVhRWTUtMnBBMlMyQ21iZkVpczlSbHEtR1MxWVpYMkh4YzR4VEZBSU9MZU1wZXgwOFdzc1pER0g0MzZSTmVI?oc=5) <sub>The Cryptonomist</sub>
- 📰 2026-09-25 [Waymo Tops 1,100 Registered Robotaxis in Texas After Adding 144 in a Day](https://news.google.com/rss/articles/CBMiqwFBVV95cUxNdmE4VnFuT25VNkxDME1SMHpGaHRqOWVBOTFWU1NSWkx4Znd4WkZ4MjI5NkI0RjZxaWFBWldOLWYyTWVHaExYREZYNGhhNlUzUkl2T2hTTVd5ekkzUVd0bUVkNExkTlR2T2ZhNjdlWXdRXzZxaDB4NjJrTmx4eUdfNUVvRE5iMExZWkk0bmhnQXcyYVhWS3I5eWRDUHdTYUVicUxIVkJhMTE4NXM?oc=5) <sub>eletric-vehicles.com</sub>
- 📰 2026-09-25 [What happened when a driverless Waymo drove into a Denver farmers market?](https://news.google.com/rss/articles/CBMi5AFBVV95cUxPLXNHaldSbW16bDYwbjNpbkY2WElrRkVoVjNPYzU3MlpUbE5ITVlzeEI0b1drV1ZhYjgybE91aHJjZlJNNG5qa05iUkVXbXktZ1FXMnhjT19ySFlFenhnZkR3WWVOS183OGVPYWV5QXVXSVRObGRHSjR0Z3daWDZjd0J1VE4wSTlwYTJVV2tGY1JEaF84VnJld1BsX3lqUXl0YzZwcXFHNVJjVTY3WnFoU0JaZzZXaXNuUVNZbUdIRzU3MjAxRTZaZWVtcHRydEc1SkhvS1l4N1pJQ3U2ZW83aGEtU0I?oc=5) <sub>Attack of the Fanboy</sub>

</details>

<details><summary><b>Tesla</b> (73)</summary>

- 📰 2026-09-25 [Tesla ramps Optimus to hundreds a week, but the robots can’t generalize](https://news.google.com/rss/articles/CBMimgFBVV95cUxNMDI3NVZBVWstYkFmTjVYM0MwN1Mya2ZHNkxKWjhlcFBPT3VBTC1sR2lNSnprQlBPTk9RTWkyRlZTQU43dFNiczZFZEFYNGdlci1xLVFlU2JmRXg0Vzg2SEt6NXBscjVQMFFSVkZ4cndleHgyd1hPNXZGR0hFbE9pejZac2dLRC1PN25RSkRYMzZubXU1Ym9aY0xR?oc=5) <sub>Electrek</sub>
- 📰 2026-09-25 [等了这么多年，特斯拉FSD终于能在中国用了，国产智驾慌不慌？](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1FT3pCbUgxYUFycDE5TC14cmVLLWYxaTVYSFdkNnphdnZCV0FxM2FNdFo0Q1E3ZXdwS1NLZm1URE1KQnN5Q0JpZ1RGd1o1a3U4MFVwbGl5QkpXd2tUS2c?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-25 [特斯拉车主嘴是真硬啊，苦等5年6万4买的FSD还是不能用？](https://news.google.com/rss/articles/CBMiXkFVX3lxTE5aWmRXNjJkbXRwa04zUnRJaGNVd0FEbUFhczNxRzZtcVpHODE4Ni1mUVFzUmlXa1Rsa013N1k2RVF5dnZsTGpkVkVKaFNQMTUxMk1zVzhYa0ppTEw5eEE?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-25 [Tesla Robotaxi Rear-Ended While Stopped at Stop Sign, NHTSA Filing Shows](https://news.google.com/rss/articles/CBMiyAFBVV95cUxOajdybHdidWlzUnR1Ti1tWWg5OVBKb3dCemhBcWlRVkFTZFhqOFhUbmhObXpUNzFGQlozMV8wdndQTnhXbFVNWGppbmVCbG5VWE14bEs3VUtXSVZVNHhZOGVZV1drN3hNZXltbVhyTmtRQ0JXTGpiMDFzYVRkWmdpZzdRSm9ISjY2X0pIcmQ5d2xQZjdlRko2MExRNFFuUFhkLWZBQXllZ1h4MExwbjE4bGs1R3duN0ROVF8tYXFLZUg5cldwb2hUaA?oc=5) <sub>Stocktwits</sub>
- 📰 2026-09-25 [Waymo vs. Tesla Robotaxi \| Florida For Reel](https://news.google.com/rss/articles/CBMiYkFVX3lxTE1mZmJNYnhwY1pVR3daLTlreFg4ZlZaVEo4QURUZlcydElmYVdtcGttLVh0eUhrdXhsVlhNcGxTZG9rbW9NM3AtVUpsbngtTk9CQkVzVFJfMHM5MklhMjR3TENn0gFnQVVfeXFMTTgxLWROQVp3TC1uN3F6UThlZ1JxUUdLOVNWT0RRVEN5d05ueXZWaFZkQnlySVZ6RXE4SEpta2lpMzJCWWJWWW1RM3lFazEzZWhMU05VaEd1V2FFcWtpMTBURElwNHo5Yw?oc=5) <sub>FOX 13 Tampa Bay</sub>

</details>

<details><summary><b>NVIDIA</b> (50)</summary>

- 💻 2026-09-18 [NVIDIA/swe-serve — SWE-Serve: an agentic benchmark of 53 production inference-engineering tasks derived from merged SGLang pull requests, run with Harbor.](https://github.com/NVIDIA/swe-serve) <sub>GitHub</sub>
- 💻 2026-09-16 [NVlabs/Skill2Env — Democratizing Collective Intelligence](https://github.com/NVlabs/Skill2Env) <sub>GitHub</sub>
- 📰 2026-09-25 [INL teams with Nvidia in Prometheus project to accelerate nuclear deployment](https://news.google.com/rss/articles/CBMitgFBVV95cUxQODcxcUtmbWdYTlFJSzNQRHpHbElGZW9HYkR3SFlCcktnV3I3blloaWFqTGJqRUtwZXJIY1FvSHlUWFppSTZrWkNKYmRPTDRaR0NEd0VaRlN3Uzh2SXN2c1lrQnRla2dHWlUyVU13TXhLRVhoM3ZraG1UbVlRdzk4QlRmRVI0aTdfUThLbXc4WGpOQUV3ejM3bFRXS292azMwVXFBdlgxdU5KeVVYWEgxVUVnbXFkZw?oc=5) <sub>American Nuclear Society -- ANS</sub>
- 📰 2026-09-25 [Black Forest Labs unveils 'FLUX 3 Action,' an AI model for robot control.](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1NQ1F4cFNZSFpLYTlCQjZzc21pbWpELWNYNVhTeVRrRzNTSkNnQlFDVzJBSDBuaWtEOGhEQXlSdEZnSm5wcnVqV0RmbFNuU29aWDNOY1BPOU1IREZuWUtEQnNPaEpzOTA?oc=5) <sub>GIGAZINE</sub>
- 📰 2026-09-25 [Nvidia says major robotaxi programmes use its stack](https://news.google.com/rss/articles/CBMihgFBVV95cUxQTHhGZTBYWHpUSEUxSHFzVkhWemRhRHNxV2haQkJoQTE3dGFRWVJUNWhTSXNqSzBha0RnZC1BcnRzRXBiRTBaVzQ5VHhhVUZZd2gwbUdtbXJLOGl2SWxuZmxrX2Y2VWVSRDdyZnBxWklQR09CODJfVGF2UEVwVThGT2dWT2xfQQ?oc=5) <sub>IT Brief UK</sub>

</details>

<details><summary><b>Wayve</b> (33)</summary>

- 📰 2026-09-25 [Nvidia says major robotaxi programmes use its stack](https://news.google.com/rss/articles/CBMihgFBVV95cUxQTHhGZTBYWHpUSEUxSHFzVkhWemRhRHNxV2haQkJoQTE3dGFRWVJUNWhTSXNqSzBha0RnZC1BcnRzRXBiRTBaVzQ5VHhhVUZZd2gwbUdtbXJLOGl2SWxuZmxrX2Y2VWVSRDdyZnBxWklQR09CODJfVGF2UEVwVThGT2dWT2xfQQ?oc=5) <sub>IT Brief UK</sub>
- 📰 2026-09-25 [Light Hits: This Week in Collision Repair](https://news.google.com/rss/articles/CBMiogFBVV95cUxPYlJMTl9ONnlacXpzWUFMR2I1RlFNYkExeWdnZU5uRUxjYmFiY0ppMXM1TWNZZFZPV3FDQ1FWSm9oOVV6S1pGanZIa0tBazFjZ19ZTXNXOWFMTnlXLVB5RTNZb2FKN29BYW1razdqMV9GYU5HM29wRUROc2hSMUhCQVlYUXBYcDF1YVJLU0FKa3hQdENJSnpXV2tFYWxxVTZGbUE?oc=5) <sub>fenderbender.com</sub>
- 📰 2026-09-25 [Mercedes-Benz Bets on 2028 Autonomous Driving Rollout While Squeezing German Labor Costs](https://news.google.com/rss/articles/CBMi2AFBVV95cUxOWXVMQlJzXy1UV0JoTTE4LW9teml4WjRsNDU0aGNkT2FnNUthSVd3cHhzYjNleTIxYUxSeHhBN3E1a3VPVkQ1UmxMcjZKeWN0WWtTaGNIMUEtTDBZZUVXSWgwNHJUWGNFY0wzLXo4eUVwa1F0UVRvY1FONk1jYkJITUQtRHlZdVFsaUZRTF9DLWg1bmJLRVdERF9WZlFMQ0dJU3ltdWFwb3ZabjN0SFVJSFg5d1oxNzhRNno3a1VIaDdIbW5aODdvMUFkQVpHWTZSbGJmbDZyamw?oc=5) <sub>AD HOC NEWS</sub>
- 📰 2026-09-25 [How to Invest in Wayve, the UK AI Firm Behind London’s Robotaxis](https://news.google.com/rss/articles/CBMimwFBVV95cUxNZE5qWjRuOER3T0dUVkE1MGM4UTYyRGpkM1RHS3JoR1o0MmdsVkZMVmQtSjJpXzVUZFJtRzk3M2FkcHdRdVRXdW9kZnROMkZLeHJBSElWVFBSRFdOeExHS2JnelMycF9SRVlHbUxwNEs2aC1ZZ05nNVRlYWRzaHVnQ1FHOTctYUFoZV8xWGtoOVVCbllsSEJiLXJvUQ?oc=5) <sub>Morningstar</sub>
- 📰 2026-09-24 [Wayve pens deal with Mercedes-Benz to integrate AI driving into production vehicles](https://news.google.com/rss/articles/CBMimAFBVV95cUxNbW9RcDFNM0dERlMzcndZVHVhNm1CdEhPODJBZ2ttWnRZUTRWNlc5UDJ5dU1BTEJNZWN0ZXpuT3VxUUR5eWhUUW1tM1ExX2FILVAzSUFWbjROT3JtVzg5NlROZEJhREpUbGp4eHZkZHc1b1VCZjlDSjN1UzVKT3RWTndabWc2dW0yc3VjT3hVb0V2dldhX2dSNg?oc=5) <sub>Imaging and Machine Vision Europe</sub>

</details>

<details><summary><b>Momenta</b> (50)</summary>

- 📰 2026-09-25 [带激光雷达的豪华插混SUV哪款好？凯迪拉克全新XT5 PHEV与4款智驾SUV横评+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE1HS2ZfcVpfS0NRLWk3MGhjMzVQdWFhbWpKSEo3WTRLbnVzZ2FJZnJGM0pWUjU3ZWxrYjZBcy10XzNzQmJCQVBEQV9PdTNaYXczSWs1Q2VsSF9HVGNLX1V5UnJvd0lBVXB6MXVHN1l2Z2dTQQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-25 [新N7上市，12万级搭载激光雷达，Momenta R7智驾上车](https://news.google.com/rss/articles/CBMickFVX3lxTE91OGVib0VKRUdzWmVma2oxb2VSMGlxdDh6dXE4a0dtZ2NiVlppdXVMdUZHbl9RcE9qcWZDU3F5ckhIRE5wOTRjYlJ4elZYcVVDeXlMMlYtR2V6UlozU055SXdWTi1qeGtJUlZ4ZHJtY2M5Zw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-25 [Nvidia says major robotaxi programmes use its stack](https://news.google.com/rss/articles/CBMihgFBVV95cUxQTHhGZTBYWHpUSEUxSHFzVkhWemRhRHNxV2haQkJoQTE3dGFRWVJUNWhTSXNqSzBha0RnZC1BcnRzRXBiRTBaVzQ5VHhhVUZZd2gwbUdtbXJLOGl2SWxuZmxrX2Y2VWVSRDdyZnBxWklQR09CODJfVGF2UEVwVThGT2dWT2xfQQ?oc=5) <sub>IT Brief UK</sub>
- 📰 2026-09-25 [【视频】日产N7：8295P芯片 + Momenta端到端智驾，智能宽适纯电轿车](https://news.google.com/rss/articles/CBMia0FVX3lxTFBCb1NBWVdIVTZYVmk0NTN0VlQ2NXJ3ODYzZXZLb0NxNFJVWS05R2RmNDUyS0pubkhuZWo2U3hQaEMzY3JFazBEOGZnaThkMzJyUW14aXFPT3h5NURJUFVtX1hSLVd4UGQzejB3?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-25 [凯迪拉克全新XT5 PHEV智驾深度解读：激光雷达+Momenta R7+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE44VktaXzhRSGdrWlFtQTFiZ29BTU5PUkc0TVJhY05VTl9zVloyak9VREVkVXFURWNRSm9GRXNBOFdaVUp1OWpGSVl4VUxUbFhtdTVvSkM5YkpsUmkzU2M5WExjR3FNMWNyZlhqajAxZjdDZw?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>XPeng</b> (79)</summary>

- 📰 2026-09-25 [2026款小鹏P7+值得买吗？增程版续航1550km，3个维度说清+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE8wZ2QtLXFFUTVTWjhHdHVReE5RUVR2UFpsdmYwbDVxVm82SDdKeVp3U3ZGQmdpaGplWjIySkFNYWh3NkZNTkoyVTRVakZNT1FrZTdKeW9kYXFqMXdGRjdIY2MtajlSQVNnbUdyd0FMTGhMdw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-25 [25万级纯电SUV怎么选？新款智界R7 vs 阿维塔07L vs 小鹏G6参数对比](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5nNS1oSFJvMVp5VEwtN2RnTVBubVhfRDZXQlgxbjNJbDhoTUd4eTM5MVozVGtFbExOZE1KWTBjVml0Z29tcERKQkVsVnpQMjFjdHZkWGJNbVRTU00?oc=5) <sub>网通社</sub>
- 📰 2026-09-25 [智驾新高度！小鹏天玑AIOS 6.1.0正式推送](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5aUW9QbUtPWXJsbmRtaDRWUEJjYk8zemVkQzFwMTNMbEJ5Mnd3SDBvemhxUG5OcFhGQkloc19mZkZzdmtPd1hOcWpOck02S2FFYTlzMi1TWDBRd2s?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-25 [【视频】小鹏智驾+大众底盘，预售价19.99万元起，这台与众09到底有多能打](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBuNElTZHM2ZE80SGR5LXQ3bzBjcmVYaVpyQ3RHVkJvc0JzQXBveXhoRnBkanNlTHVUSGYwWDRFWnZpYl9KdzZMZHR4bHppR2paR3VXTDFPQ0pLTU0?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-25 [XPeng's robotics arm valued at $6.2B aims globa...](https://news.google.com/rss/articles/CBMimAFBVV95cUxPNWxwazBtNkNWSUpQaEltUmx1S21ZNjJud1ZlZ0FFTHFWdWpRa0FISWh0MTItb3BCUW9kVHVqLW5Pb1FVbm53UkhleTJUaUpxM1hMMDRzTUc4REZWcHRCNFpONm5OQXpPZTFfdWNxeE9tNWRzVnB0UlZQV2FEUVYzOURnb0ZsUDFkMU9oSWQtemV1cjYyeWEwRg?oc=5) <sub>Pluang</sub>

</details>

<details><summary><b>Li Auto</b> (60)</summary>

- 📰 2026-09-25 [理想汽车广告抄袭沃尔沃？沃尔沃发文：有些经典，总在一次次重温中被铭记\|理想L9\|智驾\|宣传片\|风波\|车辆_手机新浪网](https://news.google.com/rss/articles/CBMiqwFBVV95cUxNbE1DZVQ1NmdHcUJ5aHgzUjNxamhWWUZRaWUzcGJBSWd0anJGaDVSdkJhcUxndFd4eFlwTFMyM2o5YXUzcDJtbXlvWVpvVlc2YWVRakxjTWRFUXJGU000YjBYb0RVRDZ1b2ljaHhfb1g1U0tuSnVFR0g2MmhwdzlEV0xReVBzTkdhazY5cWpTb3Q3NXI2d2VDVHZBNkc0c0psQVVjaWxuaDFpaFE?oc=5) <sub>finance.sina.com.cn</sub>
- 📰 2026-09-25 [Dongfeng to trial-produce humanoid robots by end-2026 – Xiaodong to work in car plants, human-level by 2027](https://news.google.com/rss/articles/CBMi0gFBVV95cUxOMjVuUXVZWGJ5eDZhUDliVGFkenA1UGpMZExsemlkeUVwMVB4eFJuZm1kcFpYdzFSSmxwc3BXdmtkVlFaRzhmNVJ3ZE1GcDJfei1sZHVLWkExLVprUU1CaThQQlBWRDNrdlBMUEdybjBwSV81RS03dk9UM1FCZDg5OThiS0VYS1J1aWhsUERrMDd3emxJLXZEclVOc3otUGJ2YU9IY3VUWDU5UERTZlRBWjFlUmYxUjNJV0hBYTM5eG9fZnA3Z091VzFqaG9ZUFhHSkE?oc=5) <sub>Paul Tan's Automotive News</sub>
- 📰 2026-09-25 [理想VLA第三站智驾牛庄一线天，L8livis携手詹锟杨杰实测](https://news.google.com/rss/articles/CBMigAFBVV95cUxPMEp6dUFfdU9Va3BMZU00NzVmaDZzdHhEOUdXR1AzcE15SGdVcVFMUF8xaWtwMV9yWnQ1U09HbXppRlVaZEhKS2ItVkZJY2JyWTEzdjVkNWdrTTMyRkhGSWxQQVZ4SHhKNWs2YlBqaThlZFZsMmVNRHo4UjRFQkt2Xw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-25 [体验理想OTA 8.6，马赫VLA变道绕行更丝滑](https://news.google.com/rss/articles/CBMigAFBVV95cUxOWU9jZDdVT3h0UXQ0eS04TUQyNmNXRDJSc0E2RlNuN2syVVF6QXNYRVl1czdqc1hUei03TFhlLU0wUjUzUEhhaGprZTFoQ0F6cjJUZGM0Umc0Yy00WjVXdkNPRU1JWnhkdlVTemlBaWF5MTBLS1Y2dmhoaS1DMWhfaw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-25 [10 Open World AI Models Actually Worth Following in 2026](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBnRk9CNXNEZTVWajdvYnJGd1lZSjhvLUtlMTFiTWViMjhhVEtnd3ZxUUpUMVloSTZTMERnMXVaX2VOaG8zU1JlNEVTc0hoSnpESkN0YXJPWFg?oc=5) <sub>autogpt.net</sub>

</details>

<details><summary><b>NIO</b> (52)</summary>

- 📰 2026-09-25 [蔚来世界模型Cedar 1.5.8 最新版本智驾，领航驶出停车场，选道能力相当优秀！](https://news.google.com/rss/articles/CBMiVkFVX3lxTE5Xcm93ZXNMeFNzMWxKRmotaTYxNENuWWE0b19OUjJUemw2N25TR2MwYm1WcVJfRFV1WG85LUF1a2psZm5CbEN3TDBuXzc2aXlDblVDNm1R?oc=5) <sub>QQ News</sub>
- 📰 2026-09-25 [长途自驾豪华SUV横评：当问界M8和蔚来ES8还在偏科，这台车已经交出了全优答卷](https://news.google.com/rss/articles/CBMickFVX3lxTE9aV3haakdpeTBtbFlMQmx4YTF3WnJPdkM5alNVenJybThSMWJsbG5VMzFJU3gwd3Q5ZTV6dnI0VmplNm9ZZVVUWXFzMkpZdGEwUGZ1NVUyWHMxTkw2RjdBVTBTN204eWxGdjBvUnItLUxhZw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-25 [【视频】2022年蔚来EC6，买断电池，二手车性价比如何？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5aTTdGSnBreXRmanNnVzNEVllzSTk2TlRuMTZtU2F2SEdfQlZTWVhpYVNVSG5JVmt5WDJqZHJHUXpuZGw3Qk1JUjlDeTIwUllvZ2NTc2g3bnRQU1U?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-25 [Nio Rolls Out Cedar S 1.6.0 to ES6, EC6, ET5 and ET5 Touring in China](https://news.google.com/rss/articles/CBMiowFBVV95cUxPclo0MlduYUN2MHFtT0VORUVKOXplVXRiV1NSNFFjWHk0TFV4V2lBU2RHQXF4UXotektuYVFUYW5MRm1xRm1HTnpOU1JNVmNheEZhN3dwSmY2SnRLTjVmQUpueGlzZ2tCc2VXb0lrWXBleld0UlFjNEJWRTMtb2g5cENTdzBNWDU0X0VsNjJSaHdVNHZHa0Jzdm9JVGtmaWJudjlJ?oc=5) <sub>eletric-vehicles.com</sub>
- 📰 2026-09-25 [蔚来2026款ET5、ET5T正式上市](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1jTV8teHFfLTJZWjROMUo3NURONFpjTTJMb25Cdm03U0d3OTlLdnFWVnU3aVdGdmp0aXRhd19mT05nc09LZmM4c0xoY0tiQUFsQkVQU2VCLUJFWk0?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Huawei</b> (95)</summary>

- 📰 2026-09-25 [27.98万起，奕境X9上市，华为全栈智能上车](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5iZG94RkphWlV5TW9wZVlaZnlNR1VQWFdXNjlMNXhsV2UtWUVfTS1GQ1doWWFTLXBkNGI1b2hxckw4RE5ONExQdTRuWUN3M3ZPR0pqeDBoUXh3anM?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-25 [China's autonomous-driving suppliers confront the limits of software moats](https://news.google.com/rss/articles/CBMilwFBVV95cUxQQ1N0OTJNempXMjlfZVc0R3had1UxUll0TVQwLWp6TnJsLXQ0U3hLaUlvb2dmUzBvSjdKNnhleTlwSFlfT2J3WVFLM3ViQ0xoMW5hbmZReDByOE9PTkowTjY3ZUF1Y1pmU1ZUbms3aHNUOWE2RWpsSmE0Rkd3OXN1SVM2M2NpY3RUOGRmdFl2Znk1U3JnLWVZ?oc=5) <sub>digitimes</sub>
- 📰 2026-09-25 [【视频】奕境X9限时优惠价27.98万起华为乾崑+4激光雷达+大六座SUV](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1TS0FhOUZXWDYwUk5BRFhkWWcxWV9xUEt5TUhlSnJnclRkZmlMT1Vjc2tYSW85cmJTbjNxSjRuWUdPVEhmSWxyc0dwQWVnMUxURzFxcnliR3R5Ymc?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-25 [HUAWEI WATCH GT 7 Pro Brings Sleep, HRV, Activity And Recovery Together For Daily Readiness, Expert Says](https://news.google.com/rss/articles/CBMiywFBVV95cUxNYXB0d2MzVmdxM09YckJTYTBieW94V3dxQlhHTmF1eWs2RW1WeHFndlhGcmdBREZBN293UTZtNFRORDlrbXYwSlU3aWhWcWVUR0I3dUxWa0lEaWRaREIwNWFWaDh1aUdYeW9LMEFvTXJNZVVRVVNrVVlWckx2d2dEcENsSkx1WC1QckMtaHJJYmlkODdHbmpCcFJXZnJncEQwN0xlSEU5RU5zb2JKQXVpa3YxOXIzNmNsZGR6bWtNRVVhODR5U1FUUXlxbw?oc=5) <sub>Mena FN</sub>
- 📰 2026-09-25 [Huawei Mate 90 Pro Max Collector’s Edition telephoto extender leaked with 1-inch sensor, 10x optical zoom](https://news.google.com/rss/articles/CBMiiwJBVV95cUxPa0JyalpTTkpIajhvLV9WUVhkaWJ2TDdpNGZBMjFEeU1GR3QxblpXNjNQWGV3dkZ6QW5TNnA0cTlYVmY4RUljVmVjRXV3eld4Zkt4UGIyRUV1V05teEpsZzc2MW9GU01oaEpYcFp5VGRvUlZJWnA1UUFxVHh3OXV0QzlGT3Z1eXdoM3ZaZEU2dV9wVVdkbTlPSEpiWXRnY3dWSHV6UF9HRG41ak1xUzkwa0VwN09KRDZZdk01ZmFBOUFaUElEZmduM2JVLW42di1Ya3NtVkFJbUI0Z212Sjkwcy01a1AtOUZsbENvYmRiZ1FITXdnOTdnQzVzN3BRRm52YkJ3eWRaTUEzVzg?oc=5) <sub>Gizmochina</sub>

</details>

<details><summary><b>Baidu Apollo</b> (34)</summary>

- 📰 2026-09-24 [Waymo is Taking Robotaxis to Tokyo. Can Alphabet Get Ahead of Uber in Japan?](https://news.google.com/rss/articles/CBMiowFBVV95cUxNY2RtWFhhOHpQemRpdFhYNmFRdjNuaUdxbnFlNmlOa1V6djUtMkdlaUxrN3FqQk1Id2R1Z0pTTTc2YmtCWFd4aGd5Sk9vekFjM0I0VHd4UHBwQTlINEFkMzBnMWxTUXoxYUpyNkY4MktIWEdwSWZ1clV3YnBfZjI5RGFZOHJYNGdfUVhnVlZUbDU4ZnlPQ2N4WmNuY2JtUUU4amhj?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-09-24 [亚博ag真人最新网址在哪里找？一文读懂热门游戏礼包兑换和使用攻略](https://news.google.com/rss/articles/CBMiXEFVX3lxTE1XY2t6Wnc4eVFLYldzazhheFdhdlFheGZiS2czMV9Oc3d1cEYyMVJBaDRNUjdOcU5FbVhDVmpjNzd2aXRvM2FtMXZaYnpFQUpTRFhScFhMZkZ2LTVM?oc=5) <sub>womenofchina.com</sub>
- 📰 2026-09-23 [李彦宏的AI课题：百度遇上“快播式”老剧本](https://news.google.com/rss/articles/CBMiTkFVX3lxTFBIdkZoQTNtai0zMWgwSGlzdnlSQVNPZHY4dXFFcEFjaG5wbWcxZU9jX1JEOUNNeFNWS01HV3dFVGhFLWtzR3BmNTFGWGhyUQ?oc=5) <sub>36kr.com</sub>
- 📰 2026-09-23 [打卡全球首家机器人4S店,试乘L4级无人车,体验京东方柔性屏](https://news.google.com/rss/articles/CBMigAFBVV95cUxNNHBfdEdLOEtFbkp2dXdCZXJ6U01QV2ZNakhPSDhrM0xndjBMblVzcWxpWHpud1FjSlN3Y1RXZWpzZUh5Q1pLd3M3d2kyRWhlT1A0Q1poLU9EakxZSG50aTFnZTVoaDhaZW4ycjljV3VqVW9fVHFfVTZuX2xud09BNQ?oc=5) <sub>t.cj.sina.cn</sub>
- 📰 2026-09-23 [Aurora Cannabis and Baidu have been highlighted as Zacks Bull and Bear of the Day](https://news.google.com/rss/articles/CBMi0wFBVV95cUxQNWJZZzE0Qm02Y2NZVl9pY18tYmllaEZRMEhUdzR6eEZSS1gzcWx2QmZNRmNWdTV3Q2xzZmhjV05ic1RMcjVydGZKMjRWUkZZOFJ5LXVTU3hwVE1UY2M3NVVWa2daLWphbnZZRjl2QjQ3YWpBMVdpVzY1MHVvd2VSMXNkeEdyQmltQWItTVJVSzJRMnZvdF8zY0hmbWlYOU9IZExfMGY4Wm9IcHBnU1Q3c09oUS13V1NvU29lQno0eUhrYl9JWTU2QlRWUUZ4QW5hOHBB?oc=5) <sub>TradingView</sub>

</details>

<details><summary><b>Pony.ai</b> (54)</summary>

- 📰 2026-09-25 [纳斯达克中国金龙指数跌超0.5%，DCX跌15.26%](https://news.google.com/rss/articles/CBMiY0FVX3lxTE9iOVNFR0t4ZlBJQUlSazlEMWZ1S2R1NkR0X05zQTQ5NXlFTXo5dHBnMUJMc0JaZEVaRHJrOXZ0aTczLVB0eGltbUQzNWJkdW02ajEtbFFPYkxWWkQ4a2Jta1psaw?oc=5) <sub>东方财富</sub>
- 📰 2026-09-25 [汇丰将雪佛龙目标价从每股218.00美元上调至250.00美元。](https://news.google.com/rss/articles/CBMiT0FVX3lxTE4xRjZFYm9oSGFpQlFzeldPT0w3V2ZhSGpUbXB1Zmxzc1lDbzZKS2hIV2piY0JOOTVMWVd4VDllSVBMYnY1Z3QxYjF5WnBiSDQ?oc=5) <sub>finance.sina.com.cn</sub>
- 📰 2026-09-25 [MeetKai将基于英伟达构建的主权人工智能推广至六个国家。](https://news.google.com/rss/articles/CBMiT0FVX3lxTE10YnlWTXBKOFdPMFVoS09iUmhEb2JrelgyM3BuLUlXX0F2bEY1ZEF3SHJ0WFF5RzRLdF92bWRSS251dk5vQ2RFVjFiVW5ZQm8?oc=5) <sub>finance.sina.com.cn</sub>
- 📰 2026-09-25 [Ethereum, Circle’s Arc Set To Gain With Stablecoins Powering AI, Says BlackRock](https://news.google.com/rss/articles/CBMi5AFBVV95cUxQbjZpMExZV3ZLTFU5NkFPazNnOW1MVkdDc1lCYTBFbS00Q3J0R2FYWnBta0hYMm41bXlLUUJfaEp1dDh2RWxOeWFzRG1UZG9TYTNaOWR5ZV9jcHZCc2l0bzJVcXNheHNrc1dvUk1nX1JPdF9xN0NyaGlqY1BFTGVOUV9XdHVXRWl6V3B2V3NmeTFFV3dsQzdORTU3M0JWTFhWbHhfQ3gxU01CZlZPa1MtRkZlV21IZHpZRXVPS1ZWTkZWOXJBSEN2RExKZkNsTkQ1Wi1FaXhBbHd3WEp6MHVOWktUUjU?oc=5) <sub>Stocktwits</sub>
- 📰 2026-09-25 [GAC Commercial Vehicle Accelerates Global Expansion with IAA TRANSPORTATION 2026 Debut](https://news.google.com/rss/articles/CBMixwFBVV95cUxNdmtjRjRLSzNrZU5YSF9CVkxLVFRndnQxRVBUOVlwbFRjUGo2dWx5b3YyLXdwMjVTM3VLdEhiS2RKV3FuUHprQUZtX211cGhoVUhITkZsb3l2Z1lXd3FxNnZuTUh4OWtlT1RNdjdRTTA5bWQ3cDkxZmVTODF1NkhEMGJQdDZEajhVWXRBYUF3TUtzbmxEdDdiUl9vb1Bkc3JKSnNfV0lBZ3dZNWNuWHRDaGNmZGhucnltRldoQzZiMW1BTFdYeFdN0gHHAUFVX3lxTE12a2NGNEtLM2tlTlhIX0JWTEtUVGd2dDFFUFQ5WXBsVGNQajZ1bHlvdjItd3AyNVMzdUt0SGJLZEpXcW5QemtBRm1fbXVwaGhVSEhORmxveXZnWVd3cXE2dm5NSHg5a2VPVE12N1FNMDltZDdwOTFmZVM4MXU2SEQwYlB0NkRqOFVZdEFhQXdNS3NubER0N2JSX29vUGRzckpKc19XSUFnd1k1Y25YdENoY2ZkaG5yeW1GV2hDNmIxbUFMV1h4V00?oc=5) <sub>ANTARA News</sub>

</details>

<details><summary><b>WeRide</b> (39)</summary>

- 📰 2026-09-25 [卖一辆亏5000块10万华为车背后全是门道](https://news.google.com/rss/articles/CBMiUEFVX3lxTFBQSFAwS3plbzZzNkRZXzJvaGZWcmc2dU9kamctX2R6OHUxd2k0NFNLNkVlRDJVVUxGdkJPQmJaaUNmb2Q5MnVNLUN1X3hQZ3lZ?oc=5) <sub>VanPeople</sub>
- 📰 2026-09-25 [埃安i60智能泊车真那么强？实测3小时订单破5000，10万级SUV终于能停断头路+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFBzRTFtOTdVWHB2MVE4RW55ZDdxZmhmV2VZX3hndEV6MzBWbkg5aXRudHpfUHZKVHczaTF6UGxQTXNfc2pMQmFMQTRmRHFRQ2xCUDhvaXJMSlNhY3o3SzRMei1aNnBONThRMldIQVh5ZUNJZw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-25 [埃安i60智能泊车](https://news.google.com/rss/articles/CBMickFVX3lxTE5DUDhDSlY5QzVnV3ZhYTFwdlYwUFBLM0dXYzNvOEhiZlZTWHc2eU8td011b1F0Y3lyVno0N2FIYkRFdktsVmoxNzIzSXVvUjZISUFYTHgwczh6VFJKODA5OVlxdGZnNDB5YTlWc0pQMlNCQQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-24 [WeRide Recognized on Fortune's 2026 Change the World List as the Only Autonomous Driving Company Honored](https://news.google.com/rss/articles/CBMihwJBVV95cUxPMTFLZDJhNlBoVnNhTkthWFowSXgwMDN4eTRPYnBTZ3VSWDlzVFFjR1EzcmZxeGxwclcxOFd2SHc4ZS1fbEtkaVdkTm90d2N2MU9YMkdnMWF6YXBWaTBmYzZEZkRCTkZyam93U2djazJzYUZFbkZiV000cWxIWVB2bVdndUhYUkJrM3V0OVFkZ3NsT3I2UC1UZFBENHdMX3o4TzRmb3F2clh0TE9nNXNGYkdDdG1KQ3FUTnBYMFV2c0FXS3YySEp0LWVldHhGSkpZSXR4MDlLOHQtOUpQd3NsSWVGeV9wdDlxZURJcG80NlMwRk93VktUdDJIOXJlY1EzeE42Y2xtZw?oc=5) <sub>GlobeNewswire</sub>
- 📰 2026-09-24 [传祺越7上市 权益价16.18万元起](https://news.google.com/rss/articles/CBMifkFVX3lxTFBWQ1VLNndkdUZmWFkxM1lDcC1tQjFYNkJjT3FSaUhaOWdXdmw1ODJ6Y0ZqdERMVVkzQXIzcUtackFMa0xFODF0QkwwTmdVUFZGeUJKdVRBcTN0Wk9kS3JMSnJ3emZ3ZjZxMkVKZE9LSlZxSk1qbXZ6amdYSnRJZw?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>Horizon Robotics</b> (45)</summary>

- 💻 2026-09-24 [HorizonRobotics/CogWAM](https://github.com/HorizonRobotics/CogWAM) <sub>GitHub</sub>
- 📰 2026-09-25 [地平线机器人-W(09660)股票股价_股价行情_讨论_资讯_财报_数据报告](https://news.google.com/rss/articles/CBMiP0FVX3lxTE5wcmdlajVOMnh2QkdteTlCUVhKMzlrT255RmY3c2RocGxMemlKNWRhcnJwbV9JcTlfT0NwQkJfYw?oc=5) <sub>雪球</sub>
- 📰 2026-09-25 [9万到30万全覆盖！大众5款重磅新车，四季度将上市](https://news.google.com/rss/articles/CBMiW0FVX3lxTFA2MDRVbEVQd2hJMGNkbzVYR2lKZzhfTlRZOGdrbUJXeEdJaWFjbTd3NnhQQ3dGSmhoV29qQ28tNy1IN1I5dDR5NlZkSm1GbDd3eUJxODFnemxsMTQ?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-25 [地平线机器人-W(09660)_地平线机器人-W怎么样 - 热门讨论](https://news.google.com/rss/articles/CBMiRkFVX3lxTE13MDJXNnZSdGdYUTNMSzNHejhLZzBVOVByVkRKTkxucjBSS25sbGNFX3lNR2dmMndETVprWW9wRm9fVzJaYmc?oc=5) <sub>雪球</sub>
- 📰 2026-09-25 [华兴证券：地平线机器人-W重申“买入”评级 目标价5.80港元](https://news.google.com/rss/articles/CBMi4AFBVV95cUxNNGc2S2piQVJIRVp0U1o4R0RmcnVtVEdzY09RYXRNenhBM1JXVm9ZUXFaT1llTmticUd5SFNKU0RXb3R6U2s0T3hpQ09GdklSWGgxY1ZEQ3pQY09lZzFsV3c5SDJ3Y1M4SzUwdUtsRktWU1MwdGNJOWlBZDNnckRqSGhfSEhVOXotTXhUQUFOSVR3SG9BTFB2UmRfNHpJWlFNUmdNSVJ4UGQxZ21CcnhYajlsRnMyN1JER3FQX2FWcDlJbUhETzlvMHNYVTg1NDVmMDlXMTJqSGpfd3JFaGF6VA?oc=5) <sub>新浪财经</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (9)</summary>

- 📰 2026-09-25 [摩根士丹利MD误发内部机密文件，泄露约60个Deal Related项目及多家公司上市计划](https://news.google.com/rss/articles/CBMiX0FVX3lxTE05S1BTM1N1NnBXT1kwSWpaeWhsVDdWdmlXNlQ2MDR1YkwwU1FTX3R4cFJGSnNNWjRxSHh2eXRWRWNmWG1OMGpCdDl4X2w1Y1VqWjBSMktLVDA3bk5YZHpn?oc=5) <sub>huxiu.com</sub>
- 📰 2026-09-24 [@元戎启行DeepRoute vs特斯拉FSD，高难度挂壁公路谁更丝滑？ ​](https://news.google.com/rss/articles/CBMigAFBVV95cUxQM25aR1dYajhUNEpiRW5UNDY2cmNUSzF1cjBadF94TXZmWHM3d19PLVlydlZiaVBNbFF4c3VfZGw5U1ZlTmtDVzY0WnRGS3NocHFTdkVrb1NpNGNVbmZ1Ukw0NmJUSVJsYVJ1N25EUmZ2RVBjYWFpWVNraWFzSTdDRQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-22 [赛力斯的辞“旧”迎“新”](https://news.google.com/rss/articles/CBMiU0FVX3lxTE5HTzhXM1hKdGZKS3ZweFB3cDEwbVlRUG1yVWNRbm45aGhSOU8wSlFqWk0wOHVvTXpBMjJDckxrellEWDhTR1pjLWpqYkRnWEpWSjNz?oc=5) <sub>搜狐网</sub>
- 📰 2026-09-21 [从技术参与到议题共建，元戎在顶尖学术会议ECCV给出AI安全“方法论”](https://news.google.com/rss/articles/CBMifkFVX3lxTE5pUHQtNEtWOElVek1QbFF1b29yWDRhWFg2ZU4wTF9OX2hNZjVkTWdHNWowX29DOFBNVk00MUNmMTRiR3JWeXd1ZjJoWDF0WVNYOG1SOTN5VkJ4ZmozSmhnT0EzMGZJSUdzc29tU2wyakJqallMTHNOTC1BX3Mydw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-21 [2026年国内智驾领先企业观察：魔视智能、佑驾创新、卓驭科技、天瞳威视、智华科技、元戎启行](https://news.google.com/rss/articles/CBMickFVX3lxTFBSRllxZkhMS3FJVl8yWmQ2ZklqVjRtemxaeGpTRG1PNjc1ZVRtT20telZyU1R6S29NU0JsalQ5WU92WkI1YlBfejRxOW5ZRWRpQ0dIRVk2OFFVSF9MdlZJVWVIUlBvT2tHTDZfMnRQbl90QQ?oc=5) <sub>t.cj.sina.cn</sub>

</details>

<details><summary><b>Mobileye</b> (8)</summary>

- 📰 2026-09-25 [Mobileye Global, Inc. Class A (MBLY) Live Share Price, Invest From India](https://news.google.com/rss/articles/CBMie0FVX3lxTE11MFdpQnBMczBkWUF5azl2bE1SaUIwT0Nhb2tLU3NPdTdtX2R0U3BSV2toUnNFN1puX3BqaEE2ZHJuRHdlN2N4dDY4a3NuZktyZFFSREFFQXhRTlVSbENxcUw3SHZ6VWRpN2tqZ0lmWHNkR3JuaXZWY0dXRQ?oc=5) <sub>INDmoney</sub>
- 📰 2026-09-24 [VW’s MOIA Starts Robotaxi Rides In Orlando](https://news.google.com/rss/articles/CBMiekFVX3lxTE5meUdldmgzNmRkbFlWLXlHU2J1RmVQRmlreWZqdDBRMVRud1NIV2tXdDNEdFBjYmU0NmdMel95UUdITUVtZVhZQ1BPSGo3R0syb0M0aVBrZWVvRWRGeHcwVEt6TEh2emZiX0RiSURXVFFrWC1TSUdjVjBR?oc=5) <sub>finimize.com</sub>
- 📰 2026-09-24 [Ruqi Mobility: Data Sales as a Business Model](https://news.google.com/rss/articles/CBMiuAFBVV95cUxQM19Zb2x4SzlmVk1pbGZkMXpHMGhGbURBa2tUWUMtOXVCQ0EyMTFkRDBkcWd0QlotcFJnU2hDRWZ5ZzdpQkx5cWswRFd5MHlXbkVNUFJFRVpZaUFtQWhYcnZkUXczRFlEUGZrN0paMTZQRjhkS1lXWEotSnZyZWpMYVRzSTgtSlFwMEtyNmVMT0ZHeWtBOFl4czRHeEcyX1JmOEhiUVlsb0tNNTJBOHFyaEhGSUtjWUJT?oc=5) <sub>All-About-Industries</sub>
- 📰 2026-09-24 [BlackBerry Falls 2% Despite Record QNX Quarter and Raised Full-Year Outlook; Mobileye Holds Steady](https://news.google.com/rss/articles/CBMi1wFBVV95cUxONnJLWWpPQU9jMVpXamNpVkVmRXJzNEFRZDgwc3dnclNXQW5LSWpTdnd2VVBIaXlpV3Zfal96akpOOFEyckVuN2FGU3IzbEZkSk9BQklFeElKbFdDbVJjZEVPUUJ0dXJqVHlZS1BmNW1xeGRTc1N3ZWdJZm1VLXpHbm90Ykt6MHJZd0xrZUhNUExPcm93UGNjRTliaC1sX25LTzBJZ0lOREk5clNoQjFOTXlWRUVUNXBnamY3ZWZRRVVkN21xZU95UXZBMkJRcUFWYldnYTJfVQ?oc=5) <sub>24/7 Wall St.</sub>
- 📰 2026-09-24 [VW unit MOIA begins US robotaxi rides with Orlando rollout](https://news.google.com/rss/articles/CBMilwFBVV95cUxPYnU2TE5ueVZuRmlzdVVON2NsYmxxOHY1NXhwUnkyWjdqYmFwOHJxdDNmejRQenFUQnRlSkN2RW1WTVR4dDJtdFdrVkM0T1ViS3ZZX29FVnZMVUFWa1JYcExzSHFTVXkxeFVucnpBaDBHUWVuR2xjS21VeEF5aVF5cjJlaHdJSUVId2NqOG1OMThxeDVQQzQ0?oc=5) <sub>Reuters</sub>

</details>

<details><summary><b>Aurora</b> (23)</summary>

- 📰 2026-09-24 [Aurora Innovation Targets 30,000 Driverless Trucks, $5B Revenue by 2030](https://news.google.com/rss/articles/CBMixwFBVV95cUxOT2RxazR6ZHRvQk1GVWVOT3hSTnFkaFJkVTZxRnE3TVFzQjVHNWZEQ29YOVlBaUd3LW9YS2JmNE50bmJHdjhjWTg0cEdLWmJoSTR4Z25xOUx4SzAxSTdGZzE2VW1NLXJJT1FFaUFXOENXcVc3aXFFUTFqYktIMUVrTEI2Vm50Z0RnSTNBSUF3aEF1OFoxeVUyV3RTQVdnSVEybnR1bEp4TmZjRGhhcklDU2hKbnAwRkVVUUZHb3JObXRLR1pwd3M4?oc=5) <sub>MarketBeat</sub>
- 📰 2026-09-23 [Aurora outlines 2030 plan to scale to 30,000 driverless trucks; targets breakeven gross margin by 1H 2027](https://news.google.com/rss/articles/CBMi-gFBVV95cUxQWnFMTkE3YzI1Z3BVWnFocFRVaVlzcTFWVnNRaDlWZjUzUVFZUDE4dVpMYm1OZ2ZFamVuWHRQa0RXcXN6YkVOTExEVk9ESF9yRGVLUUg4TE13cGh0bVduaXhqTXJnMnljNWZjSnBoT193WE5pSG1QUFZSQlNNMVVBem8wUnVydWlNRm1HeVVsbjVJeTZuYkF4ajdjd0RFbVJLaVdlV3NkbEJhbVZVMHg3TzZLc3BnNE1LYjFtVTVGZ0tDZk41SEI2N2VaZ0hLQzl2VS1ncVY2UG9DMkxIOW82ZUVSMnhVQzRsM1U1dDlJUDEtMTlLcGtpU2RB?oc=5) <sub>TradingView</sub>
- 📰 2026-09-23 [Aurora says its technology will guide 200 driverless trucks by end of 2026](https://news.google.com/rss/articles/CBMi2wFBVV95cUxQUkM1MWdad0l0alNfejhmQXlWNjNzQjlqNzVKVmlxQUlQMkc5bDdLV2dfa21wMzRKRWo1QnR1enRMTElpTXB2MzlyNWVxYzNzZFJfT1Rqb3lJUy1mTkdZYUtsN19JQVo2T3RWTWJpcEZOVUhyNExYbk1EcDdIaXNqTHZRQlF4cjFrVEJjanIxM0Q2RHdBZUJxMkhPOEdtU0tXUGh3THFPMnJtWnJMRVlxdFhNR1lYZkZGNjVReUpSZVBKcmItdXR2TmpSbVo4dXY5WHhqWTVPcjFHTG8?oc=5) <sub>DC Velocity</sub>
- 📰 2026-09-23 [Aurora Targets 30,000 Driverless Trucks by 2030 From About 20 Today](https://news.google.com/rss/articles/CBMipgFBVV95cUxPQ3FEbWFhRW9RZmRkUjhxb0JBZG9OcjVmbl9ydEJRR1JCYXFkbkV4TndrYVRobUVzZnFXbnpTR09qbFdVb0o2elA5TEhrMDlYQ1R5bjBucm1OMVlHSUh6aEVtd3RyNlo4SVV1ejNsUUNkQ1hWWEZsUmFOZUZwM0dWN0lBdDNGR2RVbVNZWXBoUHRoZkhxMTZvU0Nqa0VhaFM1VFVINU5R?oc=5) <sub>eletric-vehicles.com</sub>
- 📰 2026-09-23 [Aurora Expects to End 2026 With 200 Driverless Trucks in Operation; Aims for Over 30,000 by 2030](https://news.google.com/rss/articles/CBMilgFBVV95cUxNNEhLU0JOaDZJN0dDUExUTHV3Y3NKNnRCWXlvLVIxT3pURDkzdnd2aWVQb3JSdHBHdDhlN0VuZUtiWjZpM0x1THY1NTZhQXdlUkJibXY5UmRoeTRESWdvc0VQRDhXOVoxWFF0UlZrZ1dJV0pIdHcyZFZYQm8zbkNoUWk4SnNLeFk5aTJKVkp6MWlQWkZtVXc?oc=5) <sub>finance.yahoo.com</sub>

</details>

<details><summary><b>Zoox</b> (37)</summary>

- 📰 2026-09-25 [Police respond to crash involving Zoox vehicle on Las Vegas Strip](https://news.google.com/rss/articles/CBMiqwFBVV95cUxPOVBQcmdTSUJsYTBBR3VhLWdJSzE1S1BIX09Dc0J5RDNTUXpUV2NXS0FhSmt3NnBacEhNdGEwT1FfSHV3bDJwYlFIbDF6TGVDRUFqOWJWZWs4RDdEeGtjWXlvb3g0ckU2V1hIMEExV1pjOFBNTlhxcXYzV05keTFMUlJncXNVTHFPU1kyeXl1OE05SURIdjFNcFEtRVFpTGU5Vk00d0gwVFRBV03SAbABQVVfeXFMUEVFNG5NRkQxZXc4REg4M0tZQV8tckpKNjNDYUNQRjN0NVJ0dWNzOF9FY3NmTjJOVWg3Qm1wb2pWUFI3eUsyeFZjTzl2cU1Rc01xd1lNNXc4cVdsSlBVYndoN3JJTnc0WGR1ZGFfMGFubEdEZEZRcnpQdGUzcFhNYTF4SHRoT0VoOUVPYjhNY2NLV203VXFIa0pIRWwxMG1xalBpMGhCOWFUNm8wTUhWOWE?oc=5) <sub>KLAS 8 News Now</sub>
- 📰 2026-09-25 [Driver hospitalized after crash involving Zoox robotaxi on Las Vegas Boulevard](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQNEdtckJRYWFvYlJoVV9XUWNrbVJFdG5QYV9ia2luX2hRaklMMEtJaldQVUFZN2lyT3k1WWk4c2RQYzZGa0NPczgwMDVxNlQtWFZKQWgxalVzcWpMX0Z0VExydWNfSlZkN1BiaHhSM05BWmdEdmVBWFE3cnk5TzZaUG00V1d4eTlZRmczb3FHNzdvcFp3NjB3WG45RTRCWHEzczNEY3BuamNWbjg?oc=5) <sub>ktnv.com</sub>
- 📰 2026-09-25 [Zoox autonomous vehicle involved in crash on Las Vegas Strip](https://news.google.com/rss/articles/CBMihANBVV95cUxPZHBkbGdDdmlJY3UwZmZIVk9KUU9DZEpRTGh2eE1kdmhFdV9PRWRoWDRIUUp2UUhHbWQydGh1MlJ3T2I0eXE5d1QzUnBwMVo5VHd3T3dJenFXcW92X3k5RVphSG43aS1kZWtxb05iUFN0aE9LcHljSTRjZ1lzY1Q4aXJDM1dzck10S3BBeGNKVTNxOUlQR2FtV1BnNlpBa0Z3OFFEZjB0U09mS1lQWFU2R2NpblF1VzNYYlBPcVdXQ3R3ZFJxaUdJaWVXVmUzRGxnQk01Q2NRZWcxUEdjX042bjd2M3lycEphckwwYjZzWlpSM0JDX0V3bUlQSU1KRW52M0puT3hOa0xBUXBVTURKUlItU3hXel9GMkNLNWFfR2E2S29SVG1QSWdzVjB2eW1zdEhPRmpFREZ2anpiY3B2d2tfclk5SUJaTlFOM3h3aDlQbGwyMU1SbExNaWU2UHBmZ0JwTG4yYU55Y2VqUE9sUkJHLXpIbnFudnNIV0w5NjNhRlk2?oc=5) <sub>Las Vegas Review-Journal</sub>
- 📰 2026-09-25 [Injury crash involving Zoox vehicle under investigation on Las Vegas Strip](https://news.google.com/rss/articles/CBMivAFBVV95cUxPQkJiSVY2dlRob1hVR2hHbVJyanFTYXZtR1p1OHRfYVBBT3ZhTnhFeENMLXcwa0pmSDZzVGJ4TkhaaUdxY0hPYmlSQzh6dnRoTklOQXhTQ0Z4cUZ3RFNPRXNTdEFSbXFFa25MajVjQlVSSjNrSVFFRXhDSmdlTnZJdE5xUXAtdzg5MnJiN2FqZThkeXhuQjBGbi1hb3N6MU95dFdJOFp1TU1nUk5kY0ZKZnJMYUpxemhacGpUcA?oc=5) <sub>KSNV</sub>
- 📰 2026-09-25 [Driver hospitalized following crash with Zoox vehicle near Las Vegas Strip](https://news.google.com/rss/articles/CBMipAFBVV95cUxNclN0cXJsUGFLYms2dW5wNE9rRFJHMDlnZGxoNTNpR0FfTmtfZG1MbVM4TnY2T0xGbnhGQjI1OXEtZEF5MDhHZGNsbjNRMWRwOGlDQjI2QkpGTmxqc0NJY0JaaDFiX3d6TW1LUko4ZDRyM3NpY3c1TTBuWE5hRWRjclpfRG5sTk5xZDloalMtcE8wS1ZsUVdITHhjTjBqNlN2ZE5KWtIBuAFBVV95cUxNSGRKVmxKMjFkZmpuZWROc3ZhMGxuZGVkTThRMVRnMnFtLUJxNEZTSEZFNHkzeWt3RFl0Z3NjWW1PeHJfLXJ6Q3ZPenhhb2JjY3NxZmdWb2o4Y243bG1TMU9sU00zaHptUHZNa2I0bExHeEZsMS1QNjFhWVBlSk05d3pKamlOVDdJWGRSNElNRWxERkVOV0I0OWhmZWxoVG1XemJZbDgzZmY0ZGNRRkdQUi15dS1Cbmhi?oc=5) <sub>FOX5 Vegas</sub>

</details>

<details><summary><b>Motional</b> (10)</summary>

- 📰 2026-09-21 [Hyundai to Build Tens of Thousands of IONIQ 5 Robotaxis for Waymo in the US as EV Strategy Shifts Toward Autonomous Mobility](https://news.google.com/rss/articles/CBMi7wFBVV95cUxQc0QyV2VOamV0NmZXTzJDb1NqeFRfblA5NXdXcWZ5S0tuaGxsa0k2Vi12V0N6WDkxRjdfWUlKNG5jUWtWQy1DOGtMZ1M5Uml2a3hkZUdSSHNab3BtTlJOaXplclpRZjNocVN4a0dHWGpCbHNpZUN6ZDZCaUwwcE9MZXo4SDBrY09jdXNSVld1SDZfaEluLWZ1WEJVaFRPdkJBMnRtVDFXR1RicEZEdzdITkVTZjNJbkJ0bklOcExMN28wN0xXTmg0S1I1b2RCNEg5eHhISHU3eFcyVzBIei1WcnZvb2dSOVhzSVFhcTFMTQ?oc=5) <sub>EVTech.News</sub>
- 📰 2026-09-19 [Hyundai Motor turns to robotaxis as U.S. EV demand slows, to produce at Georgia plant](https://news.google.com/rss/articles/CBMiwwFBVV95cUxPNEtaQl80RDhIbFNaWDJkRGQwMllxQzdMZ0JxZC1EcEsxdUdkWWJqMzlRbVFVOGc5VF9Ta2cxZEl0b3o3ZEhjeUczZTdDWmdaTUg0VGppeUhuX1dKbUdMLWJ5X1VSOWFxYmZiYWlGQ1ZiT0NDRmJ0YkZiNWRTQWV1SnFIc2hyNVh4Q3dYRE5UWXJJUFoxTEEweng3MExUWnVtaFllalBTZ3dfQ2ZjSXFsWWRzLWw3Nkl4SDFLNzJrVzdxU1k?oc=5) <sub>디지털투데이</sub>
- 📰 2026-09-18 [System helps humans predict when self-driving cars will make mistakes](https://news.google.com/rss/articles/CBMirAFBVV95cUxQY2xDYi02dkFwc3hwX3ZOdmliM2JNWUlhUVFXQ2lIeFRxNjJKVHE5T2REVUVIWGY3YzByNE5OWjd3RU52R3Y1NWFydmtHMU5CZUIya2NhQnMzYXJqRDlSY2tSUW10XzAyY2JYV0l5UGlHX096TFZGX3g4bTczZEFacTF3R3BXVkJ2LUU0VHh2RTRpdWxxQVB5Z3NjVnlfM2pMWG11Q1hrVFRkekJH?oc=5) <sub>Technology Org</sub>
- 📰 2026-09-14 [Waymo Launches Public Robotaxi Service in Las Vegas](https://news.google.com/rss/articles/CBMiakFVX3lxTE9XZVEzX0wxTDlwNTQwb01KemQtcGpXSFVpNTY5bnFnTlJIYWZyZHFKWW0zQzVSUFNnN3J1Zlk1Ml9kSkRrWk10c2VWZE5XWDBrMG9PTWlUbHMwSXp4MzBKUGVqLXJhZmtXS3c?oc=5) <sub>Межа. Новини України.</sub>
- 📰 2026-09-14 [Waymo opens robotaxi service in Las Vegas](https://news.google.com/rss/articles/CBMiggFBVV95cUxNVDRidnM4S3JQOERUR0Z4VUtfdERybjc1UXA4Rkd2U09mX0Q1VGJHM2IwYmJuVlRWZHJXZzVfaXU3QVVwcElrTzd1R0JZQ1pnekIyMWM4ZHgzZW5sQjVfNWU3US1uQmpWeXVORWxseXpiWXd0dVl1ZFFPX2NRQnR0Z1hB?oc=5) <sub>TechCrunch</sub>

</details>

<details><summary><b>comma.ai</b> (32)</summary>

- 📝 2026-09-16 [Bugs that broke driving: Machine Learning edition](https://blog.comma.ai/ml-bugs/) <sub>official blog</sub>
- 💻 2026-09-15 [commaai/comma_hack_7 — some chestnut examples](https://github.com/commaai/comma_hack_7) <sub>GitHub</sub>
- 📰 2026-09-25 [Minister of Foreign Affairs Sugiono Emphasizes National Ownership as the Key to Sustainable Peace](https://news.google.com/rss/articles/CBMiQkFVX3lxTFBaQzYwNXpHTG1CRFJzbXJQc3VKN0RuQ0dTenJ1SzZYOUhHVEljMVQwWV9zd1UtUzB4UXYxdFE5QnZ1UdIBQkFVX3lxTFBaQzYwNXpHTG1CRFJzbXJQc3VKN0RuQ0dTenJ1SzZYOUhHVEljMVQwWV9zd1UtUzB4UXYxdFE5QnZ1UQ?oc=5) <sub>VOI.ID</sub>
- 📰 2026-09-25 [NHTSA Investigates comma.ai's openpilot After Five Crashes Kill Three People](https://news.google.com/rss/articles/CBMiR0FVX3lxTE85dkM5TnE2UmJfZVdRckZPV1N3bUgwLV9GREFzUzRiQlhiMklRMG54Z1lvUlA4ajZERkxjY1BjRmt2SXhYdk9R0gFCQVVfeXFMUFQtcDFrZURyTWJ5Q1NwM0tFODg0cW5GNHNKRVBPTm94Q0V1ZFlFT1lCRjNzZkdjcXN2U2JQMURia3lR?oc=5) <sub>VOI.ID</sub>
- 📰 2026-09-25 [Three Generations of Pagani Roadster Conquer the Italian Road](https://news.google.com/rss/articles/CBMiQkFVX3lxTE5DQzBOVUhEcmVsb0VGVkhNNFBtbElLcmRWRi1nNTlycXBNbDlOOWo1dldkcXQ5ZXQydUJSSnZrZUtkQdIBQkFVX3lxTE5DQzBOVUhEcmVsb0VGVkhNNFBtbElLcmRWRi1nNTlycXBNbDlOOWo1dldkcXQ5ZXQydUJSSnZrZUtkQQ?oc=5) <sub>VOI.ID</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
