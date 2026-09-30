# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-09-30 · 1,261 papers tracked · 42 curated.

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
- [End-to-End Driving & Planning](#end-to-end-driving--planning) (10)
- [3DGS / NeRF Reconstruction & Sensor Sim](#3dgs--nerf-reconstruction--sensor-sim) (2)
- [Perception: BEV, Occupancy, 3D Detection, Mapping](#perception-bev-occupancy-3d-detection-mapping) (9)
- [Datasets & Benchmarks](#datasets--benchmarks) (3)
- [Safety, Robustness & Evaluation](#safety-robustness--evaluation) (3)
- [Industry Tracker](#-industry-tracker)

## VLA / VLM for Driving

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DeepSight: Long-Horizon World Modeling via Latent States Prediction for End-to-End Autonomous Driving](https://arxiv.org/abs/2605.10564)<br><sub>Lingjun Zhang, Changjie Wu, Linzhe Shi et al.</sub> | ICML 2026<br>2026-05<br>📑 1 | [⭐ 31](https://github.com/hotdogcheesewhite/DeepSight) | End-to-end autonomous driving systems are increasingly integrating Vision-Language Model (VLM) architectures, incorporating text reasoning or visual reasoning to enhance the robustness and accuracy of driving decisions |
| [Teaching Vision-Language-Action Models What to See and Where to Look](https://arxiv.org/abs/2607.01658)<br><sub>Yuguang Yang, Canyu Chen, Zhewen Tan et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 30](https://github.com/ShivaTeam/DriveTeach-VLA) | Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving |
| [CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving](https://arxiv.org/abs/2607.04179)<br><sub>Zhaohong Liu, Hao Ye, Xianlin Zhang et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 1](https://github.com/MICLAB-BUPT/CritiqueDriveVLM) | End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving |
| [TopoHR: Hierarchical Centerline Representation for Cyclic Topology Reasoning in Driving Scenes with Point-to-Instance Relations](https://arxiv.org/abs/2604.24119)<br><sub>Yifeng Bai, Zhirong Chen, Bo Song et al.</sub> | CVPR 2026<br>2026-04<br>📑 1 | [⭐ 3](https://github.com/Yifeng-Bai/TopoHR) | Topology reasoning is crucial for autonomous driving |
| [EgoDyn-Bench: Evaluating Ego-Motion Understanding in Vision-Centric Foundation Models for Autonomous Driving](https://arxiv.org/abs/2604.22851)<br><sub>Finn Rasmus Schäfer, Yuan Gao, Dingrui Wang et al.</sub> | ECCV 2026<br>2026-04<br>📑 1 | [⭐ 5](https://github.com/TUM-AVS/EgoDyn-Bench) | While Vision-Language Models (VLMs) have advanced high-level reasoning in autonomous driving, their ability to ground this reasoning in the underlying physics of ego-motion remains poorly understood |
| [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)<br><sub>Nan Yang, Zhanwen Liu, Linfeng Zhang et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 3](https://github.com/Zizzzzzzz/MVPruner) | Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings |
| [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)<br><sub>Yuan Gao, Wenting Miao, Mattia Piccinini et al.</sub> | IROS<br>2026-07<br>📑 1 | [⭐ 26](https://github.com/TUM-AVS/Chat2scenic) | Validating autonomous driving systems requires diverse, regulation-compliant test scenarios |
| [UniDriveVLA: Unifying Understanding, Perception, and Action Planning for Autonomous Driving](https://arxiv.org/abs/2604.02190)<br><sub>Yongkang Li, Lijun Zhou, Sixu Yan et al.</sub> | arXiv<br>2026-04<br>📑 14 | [⭐ 246](https://github.com/xiaomi-research/unidrivevla) | Vision-Language-Action (VLA) models have recently emerged in autonomous driving, with the promise of leveraging rich world knowledge to improve the cognitive capabilities of driving systems |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 3 | [⭐ 477](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
| [Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air](https://arxiv.org/abs/2605.31066)<br><sub>Tianle Zeng, Yanci Wen, Xueang Yu et al.</sub> | arXiv<br>2026-05<br>📑 2 | [⭐ 1,103](https://github.com/louiszengCN/CarlaAir) | Recent aerial vision-language-action (VLA) models show promising single-UAV capabilities, such as tracking moving objects and navigating to language-specified landmarks |

## World Models & Generative Simulation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [HERMES++: Toward a Unified Driving World Model for 3D Scene Understanding and Generation](https://arxiv.org/abs/2604.28196)<br><sub>Xin Zhou, Dingkang Liang, Xiwu Chen et al.</sub> | ICCV 2025<br>2026-04<br>📑 4 | [⭐ 71](https://github.com/H-EmbodVis/HERMESV2) | Driving world models serve as a pivotal technology for autonomous driving by simulating environmental dynamics |
| [FrozenDrive: Zero-Shot Text-Guided Driving Scene Generation and Data Augmentation with Parameter-Free Frozen Diffusion Model](https://arxiv.org/abs/2606.20110)<br><sub>Yuhwan Jeong, Hyeonseong Kim, Daehyun We et al.</sub> | ECCV 2026<br>2026-06<br>📑 1 | [⭐ 10](https://github.com/daehyunwe/FrozenDrive) | Synthetic data for autonomous driving is surging, powered by diffusion models that promise scalable scene generation |
| [ASTAD: Asymmetric Style Transfer for Synthetic-to-Real Adaptation in Autonomous Driving](https://arxiv.org/abs/2606.29286)<br><sub>Dingyi Yao, Xinqi Zhang, Lihui Peng et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 1](https://github.com/Dingyi-Yao/ASTAD) | Synthetic data mitigates the data scarcity problem in autonomous driving perception |
| [Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends](https://arxiv.org/abs/2606.01164)<br><sub>Jiuming Liu, Chaojun Ni, Mengmeng Liu et al.</sub> | arXiv<br>2026-06<br>📑 4 | [⭐ 237](https://github.com/liujiuming123/Awesome-Interactive-World-Model) | With rapid development of large language models and diffusion-based content generation, world modeling has attracted increasing research attention, benefiting various downstream domains such as game engines, embodied AI,… |
| [Is Your Driving World Model an All-Around Player?](https://arxiv.org/abs/2605.10858)<br><sub>Lingdong Kong, Ao Liang, Tianyi Yan et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 253](https://github.com/worldbench/WorldLens) | Today's driving world models can generate remarkably realistic dash-cam videos, yet no single model excels universally |

## End-to-End Driving & Planning

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [ExploreVLA: Dense World Modeling and Exploration for End-to-End Autonomous Driving](https://arxiv.org/abs/2604.02714)<br><sub>Zihao Sheng, Xin Ye, Jingru Luo et al.</sub> | ECCV 2026<br>2026-04<br>📑 7 | [⭐ 30](https://github.com/zihaosheng/ExploreVLA) | End-to-end autonomous driving models based on Vision-Language-Action (VLA) architectures have shown promising results by learning driving policies through behavior cloning on expert demonstrations |
| [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](https://arxiv.org/abs/2609.26792)<br><sub>Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.</sub> | CoRL 2026<br>2026-09<br>📑 1 | [⭐ 10](https://github.com/VAIL-UCLA/DreamStream) | Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions |
| [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)<br><sub>Shen Zheng, Anurag Ghosh, Gaurav Parmar et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 31](https://github.com/ShenZheng2000/WarpI2I) | Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs) |
| [G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance](https://arxiv.org/abs/2606.26017)<br><sub>Hang Yu, Ye Jin, Alessandro Canevaro et al.</sub> | IROS 2026<br>2026-06<br>📑 4 | [⭐ 6](https://github.com/HangYuu/G2DP) | In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors |
| [Fail2Drive: Benchmarking Closed-Loop Driving Generalization](https://arxiv.org/abs/2604.08535)<br><sub>Simon Gerstenecker, Andreas Geiger, Katrin Renz</sub> | arXiv<br>2026-04<br>📑 13 | [⭐ 172](https://github.com/autonomousvision/fail2drive) | Generalization under distribution shift remains a central bottleneck for closed-loop autonomous driving |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 12 | [⭐ 343](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
| [Latent-Centroid Steering: Single-Pass Classifier-Free Guidance for Command-Aligned Autonomous Driving](https://arxiv.org/abs/2608.00237)<br><sub>Meibo Hu, Jiamian Wang, Pichao Wang et al.</sub> | IROS 2026<br>2026-08 | [⭐ 2](https://github.com/codingmlinprocess/LCS) | Vision-language models (VLMs) have recently emerged as a promising paradigm for end-to-end autonomous driving, enabling agents to map multimodal inputs and high-level navigation instructions directly to executable trajec… |
| [STAGE: STyle-controllable Action GEneration for personalized autonomous driving](https://arxiv.org/abs/2607.29517)<br><sub>Zihao Liu, Xing Liu, Yizhai Zhang et al.</sub> | RA-L<br>2026-07<br>📑 1 | [⭐ 6](https://github.com/CarlDegio/STAGE) | Driving style refers to the behavioral preferences that drivers maintain during driving, shaped by their diverse experiences, habits, and needs, and is typically reflected in varying levels of aggressiveness |
| [Bench2Drive-VL: Benchmarks for Closed-Loop Autonomous Driving with Vision-Language Models](https://arxiv.org/abs/2604.01259)<br><sub>Xiaosong Jia, Yuqian Shao, Zhenjie Yang et al.</sub> | arXiv<br>2026-04<br>📑 4 | [⭐ 225](https://github.com/Thinklab-SJTU/Bench2Drive-VL) | With the rise of vision-language models (VLM), their application for autonomous driving (VLM4AD) has gained significant attention |
| [DVGT-2: Vision-Geometry-Action Model for Autonomous Driving at Scale](https://arxiv.org/abs/2604.00813)<br><sub>Sicheng Zuo, Zixun Xie, Wenzhao Zheng et al.</sub> | arXiv<br>2026-04<br>📑 10 | [⭐ 362](https://github.com/wzzheng/DVGT) | End-to-end autonomous driving has evolved from the conventional paradigm based on sparse perception into vision-language-action (VLA) models, which focus on learning language descriptions as an auxiliary task to facilita… |

## 3DGS / NeRF Reconstruction & Sensor Sim

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DriveWeaver: Point-Conditioned Video Inpainting for Controllable Vehicle Insertion in Autonomous Driving Simulation](https://arxiv.org/abs/2606.31918)<br><sub>Junzhe Jiang, Zipei Ma, Zijie Pan et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 16](https://github.com/LogosRoboticsGroup/DriveWeaver) | A pivotal step in autonomous driving simulation involves inserting foreground vehicles with predefined trajectories into simulated scenes |
| [Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796)<br><sub>Leshu Li, Jie Peng, Yang Zhao</sub> | ICRA<br>2026-06 | [⭐ 11](https://github.com/UMN-ZhaoLab/Pocket-SLAM) | 3D Gaussian Splatting (3DGS) has garnered significant attention in Simultaneous Localization and Mapping (SLAM) due to its advances in capturing fine-grained geometry features and synthesizing novel views |

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

<details><summary><b>Waymo</b> (119)</summary>

- 📝 2026-09-24 [Our Vision for London: How Waymo can Support a Safer, Connected UK Capital](https://waymo.com/blog/2026/09/visionforlondon) <sub>official blog</sub>
- 📝 2026-09-22 [Introducing transit rewards](https://waymo.com/blog/2026/09/transit-rewards) <sub>official blog</sub>
- 📰 2026-09-30 [Minneapolis council advances proposal to mandate human drivers in robotaxis](https://news.google.com/rss/articles/CBMiuAFBVV95cUxOVklnZnJWWmxNa1kyLWIyUXMwb1lIVks4YnRVUjZsYzlwQndqTjM2eFdQLUQ1X2g4M1oxZWVGNzJFNnNrOUVoNGVGbEI0ZmVsLUdWMlFac052djN6UHRqeGkxQ3hqVk9NUWFweExpUnJGaHlkNTMzWnkxX1owemZLRk1HOG40VWhLUWtqdDNfMlhvQkZYQ2hZMG1MMHV3elFBNUYxbThQRlVvYm00NHpCTV9udHo4aW5F?oc=5) <sub>Minnesota Reformer</sub>
- 📰 2026-09-29 [By the numbers: Waymo logs big miles in Philadelphia](https://news.google.com/rss/articles/CBMilAFBVV95cUxQNVNIMnM1RUFPSGc3WkZWVlNjWDRSM25iVnRqNUFRaXE1NEtWcG9Wd0M2Y3JKOFRwTk1UWjFpTE52TFA2bDRnaUEtMHRjVHVXMlZrbHRnTUdpeGRRWXZtQy10eU5iYUZ0ZkVhY3luOUZCSGdlb3IxeHdPRnFMcThkVXdzWmM4YUpCM1VJeU5uRmg0a2ts?oc=5) <sub>axios.com</sub>
- 📰 2026-09-29 [Make Way: Waymo Comes To Denver And Glendale](https://news.google.com/rss/articles/CBMijAFBVV95cUxNQm5nYTd1eXEtYTRrVFFlZDk4RW1QQ0lxcGpLXzBsMl8yamRFY0N2Q0x1TWdKdjMzQTRiamVFd3hBQ0xTRF9Ibmp5TnRoTTBGdGlKYXh5SkF0WVFrelFaS1dpbFNIT0ZoREFSM18ySXZyR1BJR29tNFg4bWZMOFA3UWNjbmg5Q3hiQzM5Tw?oc=5) <sub>Glendale Cherry Creek Chronicle</sub>

</details>

<details><summary><b>Tesla</b> (183)</summary>

- 📰 2026-09-29 [中国智能辅助驾驶达到全球新高度 小鹏NGP和特斯拉FSD首次同台竞技，小鹏在小路窄路和复杂场景更胜一筹](https://news.google.com/rss/articles/CBMidEFVX3lxTFBwNTBtUXdBVHBqRmxCeXM4aUk3MmwzOTZESHZycm0ycUlNU0ZjUVotcVdpaG1IaTZSV0RzMzd4bk9pZ1hKZXhxbWN1R3hWb3FnZG9fRWpseGgwUW4xQ0dBR0QtSmpXdzFYR2Z4RjZudEdoSldk?oc=5) <sub>金融界</sub>
- 📰 2026-09-29 [Tesla lines up $30 billion credit lines as capex, AI push accelerate](https://news.google.com/rss/articles/CBMi0AFBVV95cUxNNVNKTHdSTnpiNkQ2UkhyZzZsZWVyZG1mTWJqNkhpTkFRZTF1dDVLRkRPcW12V2hmT3hKRXBfYnZVME9ORmZvdVM3UGd1aGZwaGN0RV8xb2poTzd6VXB4eGJNcmpDT1BIcDZVNUFvRERjSzRhS2lHbTNvcm5oRHlfOG4zRmN0ODZreWpIcWFNeHVfNnVZZE04N0tXYWoxWDd0bXpjR1FsZm1nNTNTOGIxQ2dzdXR3NjdvVXU2VU92cWtuNHNhb3lTM0lsSmgwZV94?oc=5) <sub>reuters.com</sub>
- 📰 2026-09-29 [Exclusive: Ex-Tesla team raises $12.5M to put supply chains on autopilot](https://news.google.com/rss/articles/CBMimwFBVV95cUxNTEU5M1V0V2dNMW1OOWY2eXpPWXVFSTlEMTZSVDgwdHA5Sk9tN1pzNDlPRzdRR3pjM0VfMURtdS1YVnJaRlZQRkd1dGVoVjhzQ21sb0tGQ0RDUlNyblhjR3YzMjU4NFJ3TEJiYTcwY0I2V24xV0xaalpMRWRPZ3JpWDU4YzZ6alR0NHh4d1FiaHZNZVFVZXpaeFFBaw?oc=5) <sub>TechCrunch</sub>
- 📰 2026-09-29 [Tesla FSD (Supervised) Now Live in 16 Countries Across 4 Continents](https://news.google.com/rss/articles/CBMiogFBVV95cUxQNnpUM0xsYWJlMENzZ0dqQmxOMW0yUWNTcl92U3FHQmJFcGJxT3JCSk9RN181NXZfZTNUV28tZ0ZCN3B0eFducm0yTEZLMHBIOXpUcDJfVVJVZzNPSUdNNVBqdGN3QV9HcTBESVpXSmxYamNXUzR4aEdILTdpSmtZbC1RYlNycC12TDYyZDlncHNvcmxwcVlRYTFSRS1pNkx1Nnc?oc=5) <sub>BASENOR</sub>
- 📰 2026-09-29 [All of Tesla's Robotaxi Markets and Their Actual Sizes](https://news.google.com/rss/articles/CBMijgFBVV95cUxOLThnY0RHWVBMRE16LU1MZnF2aVRQTTB4RDhCVmxDcXVQaGw5WW5oN25xOHdJV3ZZb2FERFhJMW5ELUtaal9RY3Q3bXNqeGNfS3p6ZmJORUxmanNXZmhrT0I5a0F3WktVamYyTXFPZWFETVI4X1hnVVc3cGNESmlOb2h5MTVtaUpjVUJNMk1B?oc=5) <sub>Not a Tesla App</sub>

</details>

<details><summary><b>NVIDIA</b> (116)</summary>

- 💻 2026-09-18 [NVIDIA/swe-serve — SWE-Serve: an agentic benchmark of 53 production inference-engineering tasks derived from merged SGLang pull requests, run with Harbor.](https://github.com/NVIDIA/swe-serve) <sub>GitHub</sub>
- 💻 2026-09-16 [NVlabs/Skill2Env — Democratizing Collective Intelligence](https://github.com/NVlabs/Skill2Env) <sub>GitHub</sub>
- 📰 2026-09-29 [Lower the Cost of Building and Running Visual AI Agents with NVIDIA VSS Blueprint 3.3 \| NVIDIA Technical Blog](https://news.google.com/rss/articles/CBMivAFBVV95cUxQM2hlQ0dycjFqRXl3T3Vabm83eTZIS25RSnB2dko4T0NneVdaM1NHMVVLYlJJMTlieURSdC1QSnFUZ2lhczdFeDEwOVN5VGl6SVl2S0RwRnVfRkZldWZHOFUzamc2UlZHb213eGd0OTI0bFRPUEhaZ0JZcVUxb3NoWFJteGMyUTBObld4aXRrSWVCWnZsZ1dsYmFLU01qZ2dOUG9EOHBpN1lKWFVHMGpLc2ZlWElld1E1ZUZKYQ?oc=5) <sub>NVIDIA Developer</sub>
- 📰 2026-09-29 [Delta Electronics to Advance Next-Generation Autonomous Driving built on NVIDIA Hyperion](https://news.google.com/rss/articles/CBMi3AFBVV95cUxPeEU2cGhQS09oeXFsa096X1JZblZ0akI2Y25Ray1qOGFUTF9tS3RRb1A1aWlHU0k2SFF2XzRSbHowRUFkVlBCSDBLWm5iMl9KQVEzZlc5aGdNN3dmWnoxX3AwS3BuQ1ZEM2tsb05lMXlYbW9hazVMUE50Sl9iME1NVDk3NUFXYnZXYjhwMmhybVdYT3Fub192X3NIcS0yYV92Q1R0d2FnQ3NyT0RPMndSb2pqbG80elluREZSbVljcGI4b0d0QUh4dDhVajFVdy1ZUnlVekR5TkpSM1ZJ?oc=5) <sub>PR Newswire</sub>
- 📰 2026-09-29 [Japan and NVIDIA Launch the World’s First National AI Infrastructure for Physical AI: Expert View By Spherical Insights](https://news.google.com/rss/articles/CBMiwgFBVV95cUxPMGlzRVh2QWxnejh2dXM3cGU5UlBvNWdwZUN2VlBHcEtJRmk4LTVraW0xTjRmOE12TVBxWnZmbUJoT0duaHdHUnRfMHN6T0RvbjctUS1vQzh6NXdCbi0ya1J5eXhPdzBYR0ZSY2xpaFl6ZXc5X0xPRERvRlMzYzNSQUF5TkEwWlFnT2xVMHEwYkR5SjhuLTRuMXNLS3NObk02N2stNWxvMzkyS0ZDazZoYkJwRE9GYmdJMmZjbFhWdFpHZw?oc=5) <sub>sphericalinsights.com</sub>

</details>

<details><summary><b>Wayve</b> (54)</summary>

- 📰 2026-09-29 [Why London has become the battleground for self-driving taxis](https://news.google.com/rss/articles/CBMirAFBVV95cUxPN3lXOGI1U3BuV0tjTmpxZkdEZTJYRVpxV1h1WFR0MU90eEQ1Q3daazF1alNvUjJ0eHBNSkd3WkJuWFJiNEsyczJjTEh5X0N6eWZQMzBJY01qalBQaXMzZTBmWFBGcERENlVGcFdoLVZrS1FvRVhCVWZRRXVmSUkzRV84alBOdldpQ1laQUZvVE1jQjl6a1lOcFQzVVJrd0pFZW9IVXBDUkUxeUt5?oc=5) <sub>The Times</sub>
- 📰 2026-09-29 [Nissan to Launch Autonomous Driving Project in Cambridge](https://news.google.com/rss/articles/CBMilAFBVV95cUxPc1lnTUNoYWFOOTdqVWpob25tY0pkRmluZHhnNGVTVEstN0t6cXJ4SXBHV0NTcERjdFNCcDVKWlVaT1NLaEsweU00dlhsMl8xNW9aQzVSX25xWDlKVXRQWGNoZmx1blVWRmdnM0VRTEVnUTlyNHJxS182TUpxblpraG8zdnc2Vl9iZUVqSHZqOHJCMXBS?oc=5) <sub>Future Transport-News</sub>
- 📰 2026-09-29 [Autonomous taxis could raise ADAS understanding](https://news.google.com/rss/articles/CBMijwFBVV95cUxQR2NuMklXMEZ2cjBOTHhmNERYOHgxMGdMQWRBWS13dWRONTFBaFUxdTJIc3RPSWxVcGZXRXJLanlEMk93NUFnVFRkTGlBZEwwdW9WNUZTajZwd3lrcGUwaXVLVEUySTg0eksxdy1URlZGYVR5RHg4cGtjLXZMX21lREE3dDJ4S1RDNXBCelo4VQ?oc=5) <sub>Bodyshop Magazine</sub>
- 📰 2026-09-29 [AMD World Labs Deal vs Xilinx, ZT Systems [2026]](https://news.google.com/rss/articles/CBMie0FVX3lxTE1YWnJOajJsVE9xU3huYlFZSGpBRHVYY1lmN3h6N1p2dXhPR2pMQ2hzN3NZZ0FrcnM4czlPeUdyRV9KQ3JIaUFnVXY1Q193SEEzSHBtZG5USFJDUEFLNTVMbW1VanhDcXFHNW9UNk5PYzlDVncwQk5PRW90dw?oc=5) <sub>tech-insider.org</sub>
- 📰 2026-09-29 [Driverless Expansion](https://news.google.com/rss/articles/CBMiakFVX3lxTE5wWGxMaURna2tkbzhzTUE4QlpJdUhVZTFRREtLaXhtSVg4Z3FzSGJlM1B0WDhkaWpaWjU4X3p5bVotYnBrWE5JZEtVYmZqYjdWMHFvUTA4VGlIbWswbEtxRWFHdlY1QVBEX1E?oc=5) <sub>Trend Hunter</sub>

</details>

<details><summary><b>Momenta</b> (111)</summary>

- 📰 2026-09-30 [上汽大众ID.ERA 8X预售，1.5T增程/Momenta智驾，价格25万级别](https://news.google.com/rss/articles/CBMiW0FVX3lxTE11emZVVzlRNFZQbm5hVW1oRC1PclVXb2EtNXYyalJBMG5tczVENTJjQkdPX1JkWlJueGNSWUtzeTBJdDZMM1l0OW5ybnhCV1R6NThVV3VmYUtjWW8?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-29 [Momenta develops driver assistance systems for Peugeot and Jeep](https://news.google.com/rss/articles/CBMiowFBVV95cUxPU0lIVTlYTU9mNGpqOWZsVmhxSmIzalVDQVFwSWVEVGQ1eHpBT0xlWTRDemlMWF9OdE9TVHBLd09pbEZJVlktc3lpYU9YNllOVmdTbTZ5eEtZT0pQOTFxLVhPdXdiZV9wOENjWHpNNnBfeXRIdFdQTWVZY2hlNzlzMnhXTEtLUHJ2cl9yV0o1dVV2ekNkRDQ0N254TGxjajF2Uno4?oc=5) <sub>electrive.com</sub>
- 📰 2026-09-29 [China’s Momenta, Stellantis to co-develop intelligent driving tech](https://news.google.com/rss/articles/CBMingFBVV95cUxPSUR2alRJb1NDbUxRLTlHaWltSS11bllZVXE5M1cyZ2drVW93al9xaXI3eExDeVExZFVRWTdVRW92Nm1NeklOZ0RUajVhMVRQRHhCWThDZjNrTThicUlRTG1KOUprbjZhdG1EZE1pM1F5emE5XzZiTFN4cmVOZEFpS0sxMnhKWHZneWdZcC1hdlgzMWEwd2hMbURfbFdQZ9IBowFBVV95cUxOTHZaekZJTkFmVVVxcHNkZTNidndtNkdROFpEWENOUGdfT1I0aEJjOVlSdzI0TG9ocmtWSkVORVFmR21NYUQ3T0dkbWpWQjNfMGZxVk5HQk1sU3FaNU9qcnBhUEVoVXR3aVVMODNIc0lWQ0JwbEh3YUtlSTdrRUVqQWJ2MldNN19hQlBRUkpMYUVIcnlIT0tZUTk0RHlRTHpWQkNv?oc=5) <sub>chinaeconomicreview.com</sub>
- 📰 2026-09-29 [十万出头上8295P+Momenta智驾，艾尼氪V玩真的](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9CUE5oSHphRC03cWYwYzVwQnBoOC0xRTN3QjY1MjNvSmx1Sjd2TkxzMWtjZlowZVdodl9JX3lHbnZQNjRDeFNNMmpuOHJiY0FDanYzWFR3QldCR2c?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-29 [Momenta 与神龙科技签署战略合作，智驾系统将搭载标致、Jeep 全球车型_IPO观察_新股](https://news.google.com/rss/articles/CBMiYkFVX3lxTE9RQkFTRkliSkZsTEpzUzBZdmIxZEYwS3Q4ZG94NmI3ZTM2TWtRLVZLU0JUdk9fRUE4Vk01VzkxcC1DbmxwY1pyMlRnTkk3cE9nZjBmTnJvaHNDVF9tMzd4TEh3?oc=5) <sub>证券之星</sub>

</details>

<details><summary><b>XPeng</b> (155)</summary>

- 📰 2026-09-30 [华为智驾对决小鹏GX，奕境X9这30万值不值](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9XeXNtVlZkMzJzUFlCVXVOdW1zVkdLTF9XZUwybEJJZXJvX1RKX0ZpOW1hLWM0U2YxZ1dWRk9MNkdFcVZqbEJ3dTB4Z2RfTjg1MFRKZkxYYU1ocW8?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-29 [Nio Slides 4% as Geely Takes 30% Stake in Nio Power Unit; XPeng Drops 4%, Tesla Slips](https://news.google.com/rss/articles/CBMiwgFBVV95cUxPSDRxdzA0bnhuMHdpT29qUXZ0WnVxcloxMmNOX0V0bHRkY3JOcjk5TFZqSGhJUXBZUmo1MFVsdXV5eHBsWklVekhadzYzR2hZclFfaFF4WV9MQk96aDYzd19hWU90VnJzczEwb3dQcE5rc2YtakE1SjJIc0JieFYxaFNSa1JDWFhlVndYLWJQWlRQWDV4REh5OElvSDFNQnBBenBXYTE4SFc5NmFlNGg3ZlFYU0U1SDVpSWNWZ21yN2Eydw?oc=5) <sub>24/7 Wall St.</sub>
- 📰 2026-09-29 [Asian ADRs Slipped As EV Names Led The Drop](https://news.google.com/rss/articles/CBMifEFVX3lxTE0yblZrQ2p1UDFKdW5JTWRCcXctWFlKWkI1Q3FrZG1BQmlCUTFLZ3pIbmZqQ05TNXdFc0daQllyUDlJNVlMbEpRLTY1VEczSXAtd09sZ2hKekZnSW10aUl4TVBSSWlsc3h6Umt4Z0xuRC1CQmhmOVVIdS14SnY?oc=5) <sub>Finimize</sub>
- 📰 2026-09-29 [Inside China's "Token Capital": Ulanqab's Zero-Carbon Computing Bet](https://news.google.com/rss/articles/CBMiakFVX3lxTE9xcTJJbmJaUnVqSzZnMklaVHh4TTVzSmY4aFluSFp0bElVYnNwOGtFbWVTdFZLT0FNN2kxZG5Zc3BmOUJmNU4tbGx5cGY2MVA2Z29wZ1dzU01PbHN3aWxqOEJHeXRib1owQmc?oc=5) <sub>China Economic Net</sub>
- 📰 2026-09-29 [20-30万小鹏G6 vs 豪华新势力：舒适、智能、售后谁更值？3个维度说清+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFBEY2xlREh1clM2Q3hweFBKWWl6M1llS01xbHlQdW9LSkNUdHVqSWJuTURIM2RIQTMxU20yWTQtMjdOcS1GbmxMRGNYMmxncE9vZmk2SWp5bHhSMVk0cEV5cFNuZHpJSjE4SnFCaVNBa1Q4Zw?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>Li Auto</b> (115)</summary>

- 📰 2026-09-30 [问界M9 2026款智驾：6颗激光雷达+L3预埋，50万级智能天花板？+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE1scmZ2M3hSOWYwb2dhWGR0MEtpcTMzMFQtU0sxMnAyUWZFdXZKa19WZFlZZFVmSTJaR1dyVkZqYzhGMFhuNUhiMlMxb3RKWHViVXVVcE9maG0zUjE0SnByMGtxeTA3Uk13UVdUVWRqNVBfQQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-29 [After Building Two 20-Billion-Yuan Valued Companies, He Leads Sharpa to Re-Open the Path for Real-World Robotic Application Deployment](https://news.google.com/rss/articles/CBMiU0FVX3lxTFAyaUtyanFlY293cVkzT3loY3U3ZnJqdF8zWm1qMnVzN2VrNklLTkVuR29CWTYzd25EOUN4X2Q3ZTQwd1pZSTNSYUZzZUhUdkp3STB3?oc=5) <sub>eu.36kr.com</sub>
- 📰 2026-09-29 [全新理想L9导购分析：Ultra与Livis怎么选？一次说透](https://news.google.com/rss/articles/CBMiXkFVX3lxTE5BSlNNZmJuYUl2MVN3b0xrLVdpVVdENng5SkJSbktTV0FoMDVaTjM3X0sxTmdmeHd6OEFxSHpxd2c2OUlsRTlTNWNZS09hNng5ZzhpenVXMkZkd0Z3eVE?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-29 [理想8.6智驾宣传升级，却识别不了路面障碍物…](https://news.google.com/rss/articles/CBMigAFBVV95cUxPSi15TDVyVnlIXy1zZmRDV0RJb3hOUEFMYzJURnNwZ2lQdFdrcmVPSUJsTldBQUc0LXpNbmNDcml3S0hOUUc0N3ZmMjVBd0Vuck5XaHhKemI3eDNPYXNQWEZONFlJNTg2cWhNT2xvM0FtbEU5Q3lvUVhqYWplQm82WQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-29 [试完理想L9和问界M8再开神行者8，才知道新能源长途自驾该选谁](https://news.google.com/rss/articles/CBMickFVX3lxTE5xbUtSTjBIY2haU0dxT1BWeVpETDNqS0pNV1NqeVNBZ25palAxNGlEb1kwWEI1N2p1STRtTHM4YXNNclIta3hIX2FRLVZlYV9ZWGljcGRPd0xDUF91WDJPQ3R0WTBlQlYzRlFyMG1WLTZLdw?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>NIO</b> (116)</summary>

- 📰 2026-09-29 [Nio Slides 4% as Geely Takes 30% Stake in Nio Power Unit; XPeng Drops 4%, Tesla Slips](https://news.google.com/rss/articles/CBMiwgFBVV95cUxPSDRxdzA0bnhuMHdpT29qUXZ0WnVxcloxMmNOX0V0bHRkY3JOcjk5TFZqSGhJUXBZUmo1MFVsdXV5eHBsWklVekhadzYzR2hZclFfaFF4WV9MQk96aDYzd19hWU90VnJzczEwb3dQcE5rc2YtakE1SjJIc0JieFYxaFNSa1JDWFhlVndYLWJQWlRQWDV4REh5OElvSDFNQnBBenBXYTE4SFc5NmFlNGg3ZlFYU0U1SDVpSWNWZ21yN2Eydw?oc=5) <sub>24/7 Wall St.</sub>
- 📰 2026-09-29 [The Elevated Eden Concept Is So Unique and Well-Executed That It Landed the Designer a Job at Nio](https://news.google.com/rss/articles/CBMi3AFBVV95cUxPNi1qcVVCbU0xS204QmprU1RPSXBLMnBEUlZIOVZZajU1T3FjVnhUZ1FkMkt4b0ROSE1Kb3BhNTY2UzY1TXdyMU9ZOGdVZVdXUkcwYVBHdVR4MEFSX1A3dFRBX3Buc2oxcG1XbTJ5Ukx4dktySzNiQ1R5b1JDdW1UbHM0TWxuZnlJTUVZUHRLODlGUUZwd3BHNzJLNWQxVXRER2dsSzdhT0NELUlRLWVfckpmYzQ2ZWtKSUI5N1VBdFlFNWJwUWdjaXJwcUIySWVJR01kM0dGR295UWNF?oc=5) <sub>autoevolution</sub>
- 📰 2026-09-29 [Asian ADRs Slipped As EV Names Led The Drop](https://news.google.com/rss/articles/CBMifEFVX3lxTE0yblZrQ2p1UDFKdW5JTWRCcXctWFlKWkI1Q3FrZG1BQmlCUTFLZ3pIbmZqQ05TNXdFc0daQllyUDlJNVlMbEpRLTY1VEczSXAtd09sZ2hKekZnSW10aUl4TVBSSWlsc3h6Umt4Z0xuRC1CQmhmOVVIdS14SnY?oc=5) <sub>Finimize</sub>
- 📰 2026-09-29 [Nio Reports First Quarterly Profit After Seven Years of Losses](https://news.google.com/rss/articles/CBMifEFVX3lxTE5JYUx4ZDk0N3dDSEdRREFEakVicVBQY3FhRTh3Z2V3dmQ5YjVZdHF3cWxKeHdYR1RJakhvOHdiVHoxVGljUWNxNHR1SVdKT1ItZ3lFQXM3MVM3cG9SSlEtSm9vcEh6OWN4X0pJMHFVelRHTmpLbnFKTW9oQkU?oc=5) <sub>briefasia.com</sub>
- 📰 2026-09-29 [纯电310km、6C超充与全地形，四款热门新能源豪华SUV长途横评](https://news.google.com/rss/articles/CBMickFVX3lxTE1RYl81bWFQRldFRTMwMzdwZzUwTGRJSURiLUlxTTVUWm05SE5QR1YtUGVZY3VYZWZJLTJMMjVUWHhvRHNKX01hZWpac2RGMHdwWU9Odmh1WnZoN0pQTEJqOFZrc1c0M0hQR1hJbktUMU90UQ?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>Huawei</b> (209)</summary>

- 📰 2026-09-30 [新款智界R7焕新上市，华为乾崑智驾加持，23.98万起](https://news.google.com/rss/articles/CBMiW0FVX3lxTE8tdU5ra0R6ZEZ1aWFncld4ZldsejNPcDBFcGNvaVUtYXNLM0NySXBLREo1VHJUTU9PUFZZanlQam92cFZ3TU0tTktkWW80SDNBZFV1bzItOTFEVWc?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-30 [30.49万起，华为乾崑+三把锁，2027款纵横G700上市](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5CM3hVR2xQYnJobWVhaWo0N1RZa3JkWkU3M0tDRVJqOU56MmpSa2V3OVVkSVk4VWp6dEctMTVIc3FHSXJxQUpfSTFqb0k3dExFV3liTWhtY3pHTWs?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-30 [【视频】800V平台+华为乾崑ADS 5赋能24.98万起猛士X700开启预售](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBjR1pjWVZHamw4SU5tSWxwdTdYbjhGZ3VuVXZTZEVFcE5JUUFlUmVxZHN1dWpxdUdGSTR5a1dLNXVfNmx2c0hKSTgtbU1IdjRtejFpUFl0STVKNnM?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-29 [希望与车企达成双赢合作！靳玉志：华为智驾今年研发投入190亿元](https://news.google.com/rss/articles/CBMiWEFVX3lxTE1ZaWNKZ3JoRmlBN1B6WVl2eF90c1FNNnZQaXNhTmJ5dFhGRkJmMldMbS1ZYkk4TXUyVkNhRmJKMlVfNm5HLVh3TXZHUHI0akFtZFJPbDctV1g?oc=5) <sub>驱动之家</sub>
- 📰 2026-09-29 [36Kr Exclusive: Ex-Huawei Noah's Ark Lab Generative Large Model Team Head Launches Home Embodied Intelligence Startup, Secures Over 1 Billion Yuan Financing In One Year](https://news.google.com/rss/articles/CBMiU0FVX3lxTE9hWHM0ckhIXzdnLWFrLU5TQkxNUDJJZ05BdE5xeWRoWV91Nkc1NHl6aDFHZmZmSzNqSWxrdGVPa2taUmtMOHBmZ1kydUNvU1ZVY0lR?oc=5) <sub>36Kr</sub>

</details>

<details><summary><b>Baidu Apollo</b> (43)</summary>

- 📰 2026-09-29 [Baidu Spent 15 Years Building Its Own AI Chips. Now Comes the Public Market Test.](https://news.google.com/rss/articles/CBMipAFBVV95cUxQcGhuWWIyZmE3NUIxTTVYbDJEWHk4dnM3eG5jVXd5SlEyeHZZcmJ4Z0pTb3VoWklZVDJSWUpkMXJsZDZDSUxpVjkwdTRuQWNuYmJQM0xZQ2JCXzJEdVVwQjlYTXI1ZG5RV3YxUThOeTN0ak9SZjNudWVBcVZBUUxXcl9HTUFTV2RJek5sczAwdS1scnNLTi1TRk9nUHZkZlJjTnh6cw?oc=5) <sub>Vocal</sub>
- 📰 2026-09-29 [Why London has become the battleground for self-driving taxis](https://news.google.com/rss/articles/CBMirAFBVV95cUxPN3lXOGI1U3BuV0tjTmpxZkdEZTJYRVpxV1h1WFR0MU90eEQ1Q3daazF1alNvUjJ0eHBNSkd3WkJuWFJiNEsyczJjTEh5X0N6eWZQMzBJY01qalBQaXMzZTBmWFBGcERENlVGcFdoLVZrS1FvRVhCVWZRRXVmSUkzRV84alBOdldpQ1laQUZvVE1jQjl6a1lOcFQzVVJrd0pFZW9IVXBDUkUxeUt5?oc=5) <sub>The Times</sub>
- 📰 2026-09-29 [Buckle up, robotaxis will be in Australia within a year](https://news.google.com/rss/articles/CBMi0AFBVV95cUxNa01UNzFEd1JydWE0OUlUVjVlSFZJLWh1cXpWSFVPbl9UbFY1azNCR1lXSFlua1RKVXl0YTNWMjg5MXhsbmFFY2ZRbzk0M3JVQkx1X2U0d3lXNDdxdjlsR2tJUkp0am9lTWNZRm1McHlpS0tjdGVKOWlDVU4xeXZrV2l0SE9KZGtzN2pjcmQ5R1Q4bGRKZG5uZVVWRUJZb000MENFUkNLT0VuMXVNVkVlYVlncjRXWG9SLWNiak9EaGIwRldTT2lkVVplSURTVmh0?oc=5) <sub>The Australian</sub>
- 📰 2026-09-29 [【视频】蔚来全新ES8大战萝卜快跑](https://news.google.com/rss/articles/CBMiW0FVX3lxTE0yTFJSMFdmT1ZNenRpZWd4MjNGSWpiQ2hTUWNzZy1xMko0YjFtV1dabWtyZUhvWGpLeDBhcnNfQ1RMSF9iNGJBTGEyWUFSemVVNE5tM1ozWUhiZ28?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-28 [逐一摸需求，5个项目落地！顺德把高校科研送进车间](https://news.google.com/rss/articles/CBMiUkFVX3lxTFA4TGJGRXhIRzNTNzB5T1RKa2tYcFR5VkNXWWI3ZjRqcGJOcXN5UEpIVFRleEhHY2o4cVJ0YnlsQjFBLVQxT1Zyd2FXM3l3V3poc3c?oc=5) <sub>南方网</sub>

</details>

<details><summary><b>Pony.ai</b> (77)</summary>

- 📰 2026-09-30 [美股AI硬件股普涨，BE上涨超11%，SpaceX涨2.59%；贝恩报告：数据中心投资需6万亿美元AI年收入支撑，缺口高达4.2万亿；CPU交货周期延长至25-30周——《投资早参》](https://news.google.com/rss/articles/CBMiZkFVX3lxTE4xckFKNkY4ZjJTMTFvZ093UXlUYV9aaFBXN096Ml8tbzB5Y3N4STFMNnN4RkhUNnBTZGdiVFVpRVZqXzVyMmppWEtKLWVLR2tOVnVocVdOajJpcXpOTlJNbXB3MjRaZw?oc=5) <sub>mrjjxw.com</sub>
- 📰 2026-09-29 [纳斯达克中国金龙指数下跌2%](https://news.google.com/rss/articles/CBMiY0FVX3lxTE5JYlJ4N3Jzb1ZZa1FBd2FzdkJpZm5URVlIWTBBR3pFOWh3eUNIT251OG80NGJ2Y054OFR6WGs2NUg4aU5fTUljNjJyN193UmlSTWs4OTh3YkZlN3B1a1M4ak9NZw?oc=5) <sub>emwap.eastmoney.com</sub>
- 📰 2026-09-29 [纳斯达克中国金龙指数收跌1.60%](https://news.google.com/rss/articles/CBMiT0FVX3lxTE5NM1BHTDh4LUNuVHpmQUpTcjBfSFp4UUg1WFNQdUdVdVN5anNzZXhMVUdENzVSV196R1RWdGNRcldfWEY4dUpmdEVRSmwxQmc?oc=5) <sub>新浪财经</sub>
- 📰 2026-09-29 [9月30日早餐 \| 房贷贴息政策10月落地；央行下调抵押补充贷款利率](https://news.google.com/rss/articles/CBMiiAFBVV95cUxQY0RTelFZSmlLMlhmNktnOWxSR0ZkUEFrYUpRYUd6TDA5dzVaZWwxcUJLYUhTSV9UcXlNVkVMc3FsOGpsSlotUVdpYmVLVGxyNi1HaXlQa0txMlZ0WTJWdkU1Sk1ZaWQ3dlJ0ZllCeXBSTURoMk1IRFNRM3pnOGpQYllRLWdMY19i?oc=5) <sub>搜狐网</sub>
- 📰 2026-09-29 [美股光通信概念爆发，Lumentum涨超5%，芯片股普涨，中概股走弱，国际油价大跌，美联储加息预期降温](https://news.google.com/rss/articles/CBMiYEFVX3lxTFB4V0VvVTFuVGJZX19yU1VQNjhndXFRcFJ3WTlUemtrTmlRc1phc3lTa1pNaUtUeTBjR2NzbEZjc01GU0JRdDZuZGs2VGF0enRKeWdtUUc5czF6eW9PRUQ5Rg?oc=5) <sub>gold.stockstar.com</sub>

</details>

<details><summary><b>WeRide</b> (70)</summary>

- 📰 2026-09-29 [深耕两年！自动驾驶出海，文远知行在新加坡持续领跑！🚀自扎根新加坡以来，文远知行WeRide以实践验证技术实力，实现了多项东南亚及新加坡「首个」落地突破，三大核心业务线齐发力，让自动驾驶真正融入公众出行与城市日常。🚖 Robotaxi GXR成居民出行新选择，](https://news.google.com/rss/articles/CBMiY0FVX3lxTE04MkRiNGpoSHVFRldhMkNsaWxUSkRkaS1mc0xYMzZYWHJ4dkdOTHduamlGcklCRmpQSlkyWkM1YUxPeGFBc1JHMHFDeG5pNm4yRDVfSWhzNUZmSGg1WkdZT0JCbw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-29 [【视频】静态探店五菱扬光L：重新定义高效城配大面新标准](https://news.google.com/rss/articles/CBMia0FVX3lxTE1OTW1HN1JoZEp0ajVjUXAyNTg3U2t0T1VjeGt5ZVdOeWFaNE14NnRrZlhESTlUTW5MODFJWldrblNyYW5jaVFsQmN5MHN6QUROaGR6dVVuNXd5Z05HU2NJeGZmVktiYXFZTk5r?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-29 [纳斯达克中国金龙指数下跌2%](https://news.google.com/rss/articles/CBMiY0FVX3lxTE5JYlJ4N3Jzb1ZZa1FBd2FzdkJpZm5URVlIWTBBR3pFOWh3eUNIT251OG80NGJ2Y054OFR6WGs2NUg4aU5fTUljNjJyN193UmlSTWs4OTh3YkZlN3B1a1M4ak9NZw?oc=5) <sub>emwap.eastmoney.com</sub>
- 📰 2026-09-29 [恒生科技指数收跌1.1% 光通信板块反弹](https://news.google.com/rss/articles/CBMiZkFVX3lxTE02NEdlOFNwYnJMSzJPRmNVbUx6Zm5sei1FYlNKY0ZzN2x5cE1aZXBKWHNTVGo0dnNqakVLVWNYRzVFM1FPUWw4QVYzOU1va0dlVmRLUTBCSXJab1NsQk8yQkxVeGJndw?oc=5) <sub>mrjjxw.com</sub>
- 📰 2026-09-29 [恒生指数收跌0.48%，半导体、房地产走强，万科涨超11%，融创涨超8% ，汽车股集体走弱｜港股收盘](https://news.google.com/rss/articles/CBMiZkFVX3lxTE9iYnpZUDkzQTZPaDJHMGxmdXlkQklmY19haW9NLW9WQjd1OUdJTzl1VWpKUGhXV3J5SVRrRWoxLU1tc1kxd1pFbHdHbzdva202d3ltSF9FbmY1SmdYcmJ1c201OXBkdw?oc=5) <sub>每日经济新闻</sub>

</details>

<details><summary><b>Horizon Robotics</b> (94)</summary>

- 💻 2026-09-29 [HorizonRobotics/Ego4WAM](https://github.com/HorizonRobotics/Ego4WAM) <sub>GitHub</sub>
- 💻 2026-09-24 [HorizonRobotics/CogWAM](https://github.com/HorizonRobotics/CogWAM) <sub>GitHub</sub>
- 📰 2026-09-30 [【视频】15万级激光性价比之王！到店体验全新深蓝S05](https://news.google.com/rss/articles/CBMia0FVX3lxTE1fb1hKclJtbmtBS3ZIOTIyenY5Q0VfN09tcmxiYmg0RWdxcC1YQW43TUJfUUFORnJrYm5heTFsLUI3Q1ZhZk90UVBqQ2YwVG1hY3BfZFVYVjhCdVdWTUdWVnMxamVCVm9nTUFN?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-29 [A safety camera using BlackBerry software was selected; production is projected at several million units.](https://news.google.com/rss/articles/CBMitAFBVV95cUxQODl1MUJydG04c0RYSXR5RExHMFluSVJtb3hjZXUxbjVOVWtUdDFTTHBmY1lZblFJR08wUVRoOHhqS0lwalVualpNRTZ2NFFXRG9JMFdrOUdQLV9EZHhuQVdJSDgwY05hYVRsejlueWF2bXdHOEV3S29MQmo2TVFOTlZtUGxxWXVPOGJYWmdBV1pnZTBjMExLMndrS0xROTc5QmJUaks4U2ZQTEtaUXk1MVpINms?oc=5) <sub>Stock Titan</sub>
- 📰 2026-09-29 [QNX and neueHCT Join Forces to Accelerate Global Intelligent Driving Deployment, Anchored by Major German Automaker Program Win](https://news.google.com/rss/articles/CBMi5AFBVV95cUxPcW5NS2FqTm9yNVV6ZDY5QURNaTBjcmVhQnMyRW84Y2o3Q1FBY2VhbndIbWppTVFicGhRd3lfLXZjNWNuOWtWX0RNbWczSV9LRmNiaktqS3FjZWtnQzF3UjhERWMtYXR2aEZxYVhmUFV3ejQwLUVXZ3E4LW1SM3dNWkNPTTJMSnhqSnN1b255enFldFJGX1EzdHRwMFp1NHkzeWlDajlienNCLVNaRDZLVWNzSG5sSWd0anMtczlzMUZWMjAzd3g5Q1NZWFNNS0w1ZWE3X2NaMlhvbmxwTjJJaHREYWs?oc=5) <sub>ACCESS Newswire</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (20)</summary>

- 📰 2026-09-29 [奔驰长轴距GLE上市：国产大五座豪华SUV值不值](https://news.google.com/rss/articles/CBMiXkFVX3lxTE9nLUUzRnVPRUNnUVNHTUtrYThkY29wOW05NXREWDZQY3NtT2EwMEtCclFxbFZ5S1ZGZTQ4RnEzTUw5X2dRaWMwbmR3eXBiVVdjcW1qbU9vV3BMM2VyalE?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-29 [AIVA ME7巴黎完成全球首秀，纯电版快充15分钟即可补能至80%](https://news.google.com/rss/articles/CBMiW0FVX3lxTE03REhqQXhsSEhKZ1VIdDFkWXM5d3pPZjMwSGw2OWJFUkdhbXk4YWNTODhDT2JGQXU3bkpMNF9TakpjLWJVNWE4aXRpZXZGcHZxTzNwYTVMOXJSTlU?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-28 [Momenta与神龙科技签署全球战略合作协议](https://news.google.com/rss/articles/CBMiT0FVX3lxTE9XREQ4ZEJaWjc5UmJMQVVTYVctMS1wWUNBVUk1Mk9TWUFiZWtIM3l0ZEpxY2c2dW1LRm5CVkpNLTlqdDBzeXlNZ2ZfdjA5V28?oc=5) <sub>citnews.com.cn</sub>
- 📰 2026-09-28 [云鼎4008登录网站AI推理平台发布，本地化部署赋能体育产业智能化升级](https://news.google.com/rss/articles/CBMiSkFVX3lxTE1xaXFmUXlZOVA1Q2NmdnQxMlBOQ0RGNGdreDNSbEFhbllZVHRZODQ2MTNPekxNWi1lTjRJSU1LQ0VYSGxzczdPSU5B?oc=5) <sub>体坛</sub>
- 📰 2026-09-28 [aiyouxi真人中国官网全新版本上线，打造极致数字娱乐体验- 体坛网_体坛+](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1BcWIzNW5ETDl4Q1c5Q2V1QkRVaDVUR2xPSEpxYmFyTnlqUDQ0ODkzQ3poUU1pWjJFTXA0N3VqNUZELUgwdldKSTg3REplcEItS193VTlXSUhMMGhHMmc?oc=5) <sub>体坛</sub>

</details>

<details><summary><b>Mobileye</b> (13)</summary>

- 📰 2026-09-29 [Mobileye at Evercore’s 9th Annual ADAS, AV & AI Forum: growth and autonomy](https://news.google.com/rss/articles/CBMiywFBVV95cUxPU2lGZVVxeEFwczgySTQyOFBlNkhoN2ROMU1aaFBsWWlFVF9nZndrN284OEMxUTJ6WGtLb1l5dWlCd25qSHRwdW8ybTZTcTg2ZnZ0eVM1MWhreko0dVYyNVNpSUtRd3MwUkdfU2MzT210ZUxLYzRPU2RjUnFjSGNyZGNBVTd2WURGNThzRnBGYXU2NFNsMGhyMmdhZFZpdl85WTV1SUtmS0dUYVJCcmljNFlNYTR1UUNBTF9fWFhieE52TGJlZHZ2QXltTQ?oc=5) <sub>Investing.com UK</sub>
- 📰 2026-09-28 [Can NIO's Geely Alliance Drive Battery-Swapping Adoption?](https://news.google.com/rss/articles/CBMisgFBVV95cUxQLW5zM3paYXpzenJuMTBXbENBWUZ2NHBFQmNYZDFSX1NJUjlFQWNjeXBwdGl3WFhiNEloUGR3UmtyZHJFYU5OeFprS3RMT1kxMkVyWG5qeVJHbzNZMUFPeVpfYmp6Uk8yRUQwOHk5dkdUMkNJNjZNMk5BT3M0ME5DOE1zd3NNMXV3Y1NyTmRIQUtZSzRQYUhqTm9teU45bEU4WGIwVldTWk5hUjJHdXp1Z1dB?oc=5) <sub>TradingView</sub>
- 📰 2026-09-28 [Germany: RMV, Deutsche Bahn and HOLON launch KIRA+ for Level 4 autonomous public transport in Rhine-Main region](https://news.google.com/rss/articles/CBMipAFBVV95cUxQVE41MUVYal9PVDQyMHc3TlpHNXhna1ItOGFrZVp0NjJyaVZzVzU5bkxFSmFrd0dNTl9BM1E4RzJybzY2Ml91SVMwdmJlV3lXdllyLUJBTTZWMEpMN0ZCU1U0QlhpUF9WcDFwV0w2ZmRXcTNDSmxxZ2stMW0xUzdRZXdYVkl6Zy15bFdKNEdXc1d3b1FmMTljQ1pYRVFWYzBnUS1Ucw?oc=5) <sub>Sustainable Bus</sub>
- 📰 2026-09-28 [Aurora CFO says 30,000 driverless trucks by 2030 isn’t as far-fetched as it sounds](https://news.google.com/rss/articles/CBMitgFBVV95cUxOOHZmNEZELWs1TXRlV1hHQ2tzMVp1X0FGaWtSQXVMSDF5ZXJ3MnJ1MTVIckFPanA1bS1iMHFnTUxRdlNaVEVReV9XLXdjY0NxQ3p5ZVY5cV9HcF9tYUZ3bnFNbHZNMWFWZGxKSlZSYWdwRG0wM3FQMDhFU1hTZTgzZnNmd01xQUZhRTl0c3RqNVZQU3pjYlZNRUxFNWVYYU1iTGhqZnB6M0lIZE1YM2EtQWt3SEZ1dw?oc=5) <sub>TechCrunch</sub>
- 📰 2026-09-28 [Kerry Liu Xiangke: Tesla's AI5 Chip Lead Concealed Progress for a Year—Musk Personally Sent Blueprints to TSMC Before the Truth Came Out](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5lekRXS2d6V1J3ZE1kQURJNm4tTG9XRmRxQ1ZhQi1JVzFwVTBoekU4c0VVb0k0bllJeHZJbDhfTzYxRUVjbFVUOFBvdFRzTUh1dFJDOE5KSDRYdXM?oc=5) <sub>finance.biggo.com</sub>

</details>

<details><summary><b>Aurora</b> (35)</summary>

- 📰 2026-09-29 [Aurora Innovation Targets $5B Revenue as Driverless Truck Fleet Scales](https://news.google.com/rss/articles/CBMiogFBVV95cUxPN25IeTJfcUpqSTQ2RzFHWE0yd09HUUhoZ3FXTlBweWJhSlF6QjN5Y19rR1dWbmZCdVpKRE5aellXQjU1VndhMjNyN3pvbGl2aXJiRUo1cTdPUTViUTI1Tjd2Q0tvZFFvOVdUNzhQUEJMeGUyMG1lb1VRQWRUdVlXQXNNRHFnUm1BMmo1MEd4QXBRYWs3R21CbFhxY0dDM0FDLUE?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-09-29 [Should You Trim Or Add To Your Aurora Innovation Position Now?](https://news.google.com/rss/articles/CBMivgFBVV95cUxOSXFJN0xiVGxZZTZVemNIYzJ6d0F5aUtLd2RYUWxFUDdYZWo3ZnlxYi1RLUlVUFg4dHpOTWxvU1NiTHpVMjlmaEVmQTNhRmZabmd3TG15LUFKcGhoMUxnRUV1TEExaXMzb0Y1d3p1Y0daSVBpV1NIZFFxZVd5azRUcmdwaXdFOWEyWU1kTTE3N0NEcGZfb3V2bXc4d1hXX3dDaGZPRGluUERUQ0RBSHJhMFBNaVdZZXhJRWplVUNn?oc=5) <sub>trefis.com</sub>
- 📰 2026-09-29 [Aurora at Evercore forum: driverless trucking moves toward scale By Investing.com](https://news.google.com/rss/articles/CBMiwgFBVV95cUxOMDB0Q0lrcmY2Z0ItWUtPWUpXUldCMnZJOWI0bW9ZMUJ6STNKejZFYUVlSVgzMUs0OGo0cEpvdnIyVlNXekh4RVVVRHF3aVIzOEUxWGM2X0E1ZW1jb28zQVV0X1YwdkwwSW4tVm9Ca1RxbUFtOFJJRG1MSXFWLU9mWkZweVlqNDJaTkNrdVN3cHNmdTBkZlJSanBSd2tHcHI4SVVKRnhRWnBOQjFMN3RTc0FCb1JycDlGc1paVzVmaE9kZw?oc=5) <sub>Investing.com UK</sub>
- 📰 2026-09-28 [Aurora CFO says 30,000 driverless trucks by 2030 isn’t as far-fetched as it sounds](https://news.google.com/rss/articles/CBMitgFBVV95cUxOOHZmNEZELWs1TXRlV1hHQ2tzMVp1X0FGaWtSQXVMSDF5ZXJ3MnJ1MTVIckFPanA1bS1iMHFnTUxRdlNaVEVReV9XLXdjY0NxQ3p5ZVY5cV9HcF9tYUZ3bnFNbHZNMWFWZGxKSlZSYWdwRG0wM3FQMDhFU1hTZTgzZnNmd01xQUZhRTl0c3RqNVZQU3pjYlZNRUxFNWVYYU1iTGhqZnB6M0lIZE1YM2EtQWt3SEZ1dw?oc=5) <sub>TechCrunch</sub>
- 📰 2026-09-28 [Aurora targets 30,000 trucks by 2030 via asset-light option](https://news.google.com/rss/articles/CBMiYkFVX3lxTE1ybm9lejV3R3JwZDA0eDVVVjNwcTZqemRTQ2xQQXJrcXp2d01zZS1UWTRLbk4xRkNfVHV6UTNxbFhHVnFLMFFLZkJvQlR3cS1tbG9ranVmdGIxOUQtNDlxYzJR?oc=5) <sub>Transport Topics</sub>

</details>

<details><summary><b>Zoox</b> (62)</summary>

- 📰 2026-09-30 [Minneapolis council advances proposal to mandate human drivers in robotaxis](https://news.google.com/rss/articles/CBMiuAFBVV95cUxOVklnZnJWWmxNa1kyLWIyUXMwb1lIVks4YnRVUjZsYzlwQndqTjM2eFdQLUQ1X2g4M1oxZWVGNzJFNnNrOUVoNGVGbEI0ZmVsLUdWMlFac052djN6UHRqeGkxQ3hqVk9NUWFweExpUnJGaHlkNTMzWnkxX1owemZLRk1HOG40VWhLUWtqdDNfMlhvQkZYQ2hZMG1MMHV3elFBNUYxbThQRlVvYm00NHpCTV9udHo4aW5F?oc=5) <sub>Minnesota Reformer</sub>
- 📰 2026-09-29 [Autonomous vehicle company Zoox training technology in Denver](https://news.google.com/rss/articles/CBMingFBVV95cUxNQnFERVhxeG1MUHduc2lTd0lyQ252WWJzSmxsUEdmQzRxTjZKVEx5bzE1cG1LR0Jwb05qTXJJUWxzSnhVSzVzWVFrY21xcnVwUDBTX05xeUF1Q2htWTB0T3RUOHl3R0dNRkpCMFhoT2hMYVRwNzdiX3ROOWZzUlhUT3RTSk5vVEtaVFNqTzZNbHN0SlF5NlB2MGtfZTBpUQ?oc=5) <sub>CBS News</sub>
- 📰 2026-09-29 [Amazon bringing Waymo competition in Denver with Zoox](https://news.google.com/rss/articles/CBMie0FVX3lxTFBkazBNTVZnOUF4M21HazdIdHdrbTZxcFZoZWxCdXJfX3lGQUN5cUl2T25FVnVJbzI4T3BsNE1mbHQ2RjVRN2dub1g5TkRZU2cxUjcteWJ0ME9WZENXTmtOZE1ZWmVnc0FjNkhOUURYYnVzNHdJT09ueWN4VQ?oc=5) <sub>98.5 KYGO</sub>
- 📰 2026-09-29 [Buckle up, robotaxis will be in Australia within a year](https://news.google.com/rss/articles/CBMi0AFBVV95cUxNa01UNzFEd1JydWE0OUlUVjVlSFZJLWh1cXpWSFVPbl9UbFY1azNCR1lXSFlua1RKVXl0YTNWMjg5MXhsbmFFY2ZRbzk0M3JVQkx1X2U0d3lXNDdxdjlsR2tJUkp0am9lTWNZRm1McHlpS0tjdGVKOWlDVU4xeXZrV2l0SE9KZGtzN2pjcmQ5R1Q4bGRKZG5uZVVWRUJZb000MENFUkNLT0VuMXVNVkVlYVlncjRXWG9SLWNiak9EaGIwRldTT2lkVVplSURTVmh0?oc=5) <sub>The Australian</sub>
- 📰 2026-09-29 [LG Innotek launches autonomous driving data collection fleet on Korean roads](https://news.google.com/rss/articles/CBMiVkFVX3lxTE9ZSmNIa1lRR0VQWWF4UEpMNFVDejN3RUJXemtqaFBPcnNXT0EwTVVHZF83MVNaRjBzSnppaEI5TGpoNDIyam1xbHlkN09PeEYyZjVrT2x3?oc=5) <sub>헤럴드경제</sub>

</details>

<details><summary><b>Motional</b> (11)</summary>

- 📰 2026-09-29 [Hyundai Motor touts physical AI vision, courts global tech talent in U.S. - CHOSUNBIZ](https://news.google.com/rss/articles/CBMiggFBVV95cUxQNWZDY3F6Mk9mMGRIT2lWdnlVZmhib3FBbktkRG56al9PdTZwWUVTUTZ1ZnNvT1ZLTzA5N3NFa3dFZGRSWUNGTTFJX09pVVZRTFM2NVU4WHM3YjMyYjBaM1Z5Z0NmZjV2M0NXdzdIWHZvTzNLclg0OVM1MGNXcGpSb1ln0gGWAUFVX3lxTE9BYlRHQ3hoMEZlNE1CYV9VdXhUYk5jRHQ2N1gwZUdnUnA3elhNRm9ZRUdVSjAwZkVKLWt5WTRobkxMdUVNNXVISjhkU2ZjQ3AyU0RfUG5ZRHQ2OXZSYXh3cGJHaVhxT1p2djU4cnU4NFg5TXBKaUxTWThYNmN1X3NjLTFBSTB3WGlRM2pPVFNfSGNFaHRyUQ?oc=5) <sub>Chosunbiz</sub>
- 📰 2026-09-29 [Hyundai Motor Group Completes Tech Talent Forum for Global Top-Tier Technical Talent](https://news.google.com/rss/articles/CBMigwFBVV95cUxNYWttY2laenc2bk0tT21JVVViMk9SN1RZSWNuMkdrSWUzSlB3ZVM5UjZtVDlBUlM0VFZMd0JHdVA1LVhqUXBXcU1vczF3eTVibDg5X0F3eHBpaV9mRHBRZjlnRzh5ZkowMTRpZ2pDZmhHZW1jUzJSZndDV3BUbFBFdXRQZw?oc=5) <sub>starnewskorea.com</sub>
- 📰 2026-09-29 [Hyundai Motor Group wraps up HMG Tech Talent Forum in Silicon Valley](https://news.google.com/rss/articles/CBMiV0FVX3lxTE04TjRpT3lvQW1oUWc3Y0NuWXJtMjdPVFIyS05XZThIX19XNG53RVktaENMYlQzX0NoMW1mdG44RUpWZjZwcHBJdklHZHV6cHU3WVllckFiQQ?oc=5) <sub>헤럴드경제</sub>
- 📰 2026-09-29 ["Sharing a Vision for AI, Robotics and Autonomous Driving"...Hyundai Motor Group Holds Tech Forum in Silicon Valley](https://news.google.com/rss/articles/CBMiU0FVX3lxTFAtOTlDdkFCRHYtZHQ2ZFJRN1VtY2VaSEdBbHhTS3FsUndkdGZyTXpfZU1PTnNGMHdyZUVFNkVTelRmMU9Jdl9lLVJwSldUVDYyN2pz?oc=5) <sub>매일경제</sub>
- 📰 2026-09-29 [Hyundai Motor touts physical AI vision at HMG Tech Talent Forum in US - CHOSUNBIZ](https://news.google.com/rss/articles/CBMiggFBVV95cUxQNWZDY3F6Mk9mMGRIT2lWdnlVZmhib3FBbktkRG56al9PdTZwWUVTUTZ1ZnNvT1ZLTzA5N3NFa3dFZGRSWUNGTTFJX09pVVZRTFM2NVU4WHM3YjMyYjBaM1Z5Z0NmZjV2M0NXdzdIWHZvTzNLclg0OVM1MGNXcGpSb1ln0gGWAUFVX3lxTE9BYlRHQ3hoMEZlNE1CYV9VdXhUYk5jRHQ2N1gwZUdnUnA3elhNRm9ZRUdVSjAwZkVKLWt5WTRobkxMdUVNNXVISjhkU2ZjQ3AyU0RfUG5ZRHQ2OXZSYXh3cGJHaVhxT1p2djU4cnU4NFg5TXBKaUxTWThYNmN1X3NjLTFBSTB3WGlRM2pPVFNfSGNFaHRyUQ?oc=5) <sub>Chosunbiz</sub>

</details>

<details><summary><b>comma.ai</b> (42)</summary>

- 📝 2026-09-16 [Bugs that broke driving: Machine Learning edition](https://blog.comma.ai/ml-bugs/) <sub>official blog</sub>
- 📰 2026-09-29 [NHTSA investigating deaths/injuries linked to comma.ai driving system](https://news.google.com/rss/articles/CBMitwFBVV95cUxQMUxNaU15eUlyamdpeUtadXJFQnlOMTJYOHJmdHRJYnpJMWdJb3hJRlRISlNGZVA3dkhSNnNVOG53N3dMQUtOVmFCNUpqRWhaXzA1TG5HM2I0aEV2bG42VkdoRXRyYUI3SkpnM3ZCS2JLUkMtemRJNEVONkh3cExkakF1LVNEVjNZMjFpVndjaExSaHhiME45NGZEbWFCUi1YQ2M4Q2pLOGFISWQyeGhVV1Z3QW0yM28?oc=5) <sub>repairerdrivennews.com</sub>
- 📰 2026-09-29 [We Are Alarmed to Learn That People Are Installing DIY Self-Driving "Mods" on Their Cars](https://news.google.com/rss/articles/CBMihwFBVV95cUxNdG05Y3ZTV0RTazFBUW1KY1NuUnc2el9ld3R0TnNwb0hUcTFhN2ZRVjRmamtldXZEb3VsV1l5UElsRXFiOVZuSVpwM3lxSVY0b2JfN3N1NnNPS09UTFpLOU9YMmZ3T3psdVQ4OUlWR2VUTmFvTzRuZ3UwZnJ2dUttSHg0bWNFUVk?oc=5) <sub>Futurism</sub>
- 📰 2026-09-29 [The NHTSA investigates Comma’s self-driving kit after a string of crashes — 5 incidents that killed 3 people linked to 'hands-free' device for older cars](https://news.google.com/rss/articles/CBMirAFBVV95cUxQZmtjVG44dXhVVGx0WllJYkdHcmlmdGt1dkxwWjVzSVA2UkJUWGRTYjI3Q1lMOGRVQVk5Z3Z1QjdMMGsza253WlVObUJPSDB4SFJLNTJhQkZ6Qi1ZX2NMbW55WjAtVXNqUkpONkFSYWlpdFE4WE9OdndqWEdLNWM1TzRsTGFadHlVVlFEVlVkYlpTZlhkRjF4R3BKWXRxMjNBUER5MVFKZUEzSmJE?oc=5) <sub>Yahoo Autos</sub>
- 📰 2026-09-29 [US auto regulator closes airbag defect petition in about 807,000 Honda Odyssey cars](https://news.google.com/rss/articles/CBMigAFBVV95cUxPbllOY01DRVNHZUd5dXR2MXJDc0N1bXdVS2V2V3BzX0NqdmxORnl1cm9PU25FSU9YX2xyajJVNEVwdXFjZFM4eHQzX1ZmeHVTR3lyTVpnNlRna0dXMThiR1A5TGdseEtJTDUyQzVqN25nMUV3MVdYWVExMHlQZTFPWQ?oc=5) <sub>AOL.com</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
