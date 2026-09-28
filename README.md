# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-09-28 · 1,246 papers tracked · 45 curated.

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
- [Perception: BEV, Occupancy, 3D Detection, Mapping](#perception-bev-occupancy-3d-detection-mapping) (10)
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
| [$AutoDrive\text{-}P^3$: Unified Chain of Perception-Prediction-Planning Thought via Reinforcement Fine-Tuning](https://arxiv.org/abs/2603.28116)<br><sub>Yuqi Ye, Zijian Zhang, Junhong Lin et al.</sub> | ICLR 2026<br>2026-03<br>📑 14 | [⭐ 20](https://github.com/haha-yuki-haha/AutoDrive-P3) | Vision-language models (VLMs) are increasingly being adopted for end-to-end autonomous driving systems due to their exceptional performance in handling long-tail scenarios |
| [ExploreVLA: Dense World Modeling and Exploration for End-to-End Autonomous Driving](https://arxiv.org/abs/2604.02714)<br><sub>Zihao Sheng, Xin Ye, Jingru Luo et al.</sub> | ECCV 2026<br>2026-04<br>📑 7 | [⭐ 30](https://github.com/zihaosheng/ExploreVLA) | End-to-end autonomous driving models based on Vision-Language-Action (VLA) architectures have shown promising results by learning driving policies through behavior cloning on expert demonstrations |
| [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](https://arxiv.org/abs/2609.26792)<br><sub>Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.</sub> | CoRL 2026<br>2026-09<br>📑 1 | [⭐ 10](https://github.com/VAIL-UCLA/DreamStream) | Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions |
| [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)<br><sub>Shen Zheng, Anurag Ghosh, Gaurav Parmar et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 31](https://github.com/ShenZheng2000/WarpI2I) | Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs) |
| [G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance](https://arxiv.org/abs/2606.26017)<br><sub>Hang Yu, Ye Jin, Alessandro Canevaro et al.</sub> | IROS 2026<br>2026-06<br>📑 4 | [⭐ 6](https://github.com/HangYuu/G2DP) | In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors |
| [Fail2Drive: Benchmarking Closed-Loop Driving Generalization](https://arxiv.org/abs/2604.08535)<br><sub>Simon Gerstenecker, Andreas Geiger, Katrin Renz</sub> | arXiv<br>2026-04<br>📑 13 | [⭐ 172](https://github.com/autonomousvision/fail2drive) | Generalization under distribution shift remains a central bottleneck for closed-loop autonomous driving |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 12 | [⭐ 343](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
| [Latent-Centroid Steering: Single-Pass Classifier-Free Guidance for Command-Aligned Autonomous Driving](https://arxiv.org/abs/2608.00237)<br><sub>Meibo Hu, Jiamian Wang, Pichao Wang et al.</sub> | IROS 2026<br>2026-08 | [⭐ 2](https://github.com/codingmlinprocess/LCS) | Vision-language models (VLMs) have recently emerged as a promising paradigm for end-to-end autonomous driving, enabling agents to map multimodal inputs and high-level navigation instructions directly to executable trajec… |
| [STAGE: STyle-controllable Action GEneration for personalized autonomous driving](https://arxiv.org/abs/2607.29517)<br><sub>Zihao Liu, Xing Liu, Yizhai Zhang et al.</sub> | RA-L<br>2026-07<br>📑 1 | [⭐ 6](https://github.com/CarlDegio/STAGE) | Driving style refers to the behavioral preferences that drivers maintain during driving, shaped by their diverse experiences, habits, and needs, and is typically reflected in varying levels of aggressiveness |
| [SparseDriveV2: Scoring is All You Need for End-to-End Autonomous Driving](https://arxiv.org/abs/2603.29163)<br><sub>Wenchao Sun, Xuewu Lin, Keyu Chen et al.</sub> | arXiv<br>2026-03<br>📑 16 | [⭐ 255](https://github.com/swc-17/SparseDriveV2) | End-to-end multi-modal planning has been widely adopted to model the uncertainty of driving behavior, typically by scoring candidate trajectories and selecting the optimal one |
| [DVGT-2: Vision-Geometry-Action Model for Autonomous Driving at Scale](https://arxiv.org/abs/2604.00813)<br><sub>Sicheng Zuo, Zixun Xie, Wenzhao Zheng et al.</sub> | arXiv<br>2026-04<br>📑 10 | [⭐ 362](https://github.com/wzzheng/DVGT) | End-to-end autonomous driving has evolved from the conventional paradigm based on sparse perception into vision-language-action (VLA) models, which focus on learning language descriptions as an auxiliary task to facilita… |
| [Bench2Drive-VL: Benchmarks for Closed-Loop Autonomous Driving with Vision-Language Models](https://arxiv.org/abs/2604.01259)<br><sub>Xiaosong Jia, Yuqian Shao, Zhenjie Yang et al.</sub> | arXiv<br>2026-04<br>📑 4 | [⭐ 225](https://github.com/Thinklab-SJTU/Bench2Drive-VL) | With the rise of vision-language models (VLM), their application for autonomous driving (VLM4AD) has gained significant attention |

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
| [Native-Domain Cross-Attention for Camera-LiDAR Extrinsic Calibration Under Large Initial Perturbations](https://arxiv.org/abs/2603.29414)<br><sub>Ni Ou, Zhuo Chen, Xinru Zhang et al.</sub> | RA-L 2026<br>2026-03 | [⭐ 12](https://github.com/gitouni/ProjFusion) | Accurate camera-LiDAR fusion relies on precise extrinsic calibration, which fundamentally depends on establishing reliable cross-modal correspondences under potentially large misalignments |
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

<details><summary><b>Waymo</b> (90)</summary>

- 📝 2026-09-24 [Our Vision for London: How Waymo can Support a Safer, Connected UK Capital](https://waymo.com/blog/2026/09/visionforlondon) <sub>official blog</sub>
- 📝 2026-09-22 [Introducing transit rewards](https://waymo.com/blog/2026/09/transit-rewards) <sub>official blog</sub>
- 📰 2026-09-27 [Wayve Taps Ex-Waymo CFO Elisa de Martel to Navigate Critical Transition from R&D to Commercial Scale](https://news.google.com/rss/articles/CBMivwFBVV95cUxNSTZ5NlhOLW9ZZ016cms5ZFlBTG5lUUpfM1ZadEw1LWcwVHNsWW9XX0NwSkdZcHU5NmdjTHlXYnFFY1JSMGxLeUZFVEY0b2lJbE1tV2g5TDhpYjEzbVltOVI1RzdfVnY3NmtWT1c3a3U5R1lkSW5uV1FuWHRnTUJibEthZzFvV0lVUk1ISkxzZGxEYTZ1dTNsMTdwQkg3dGxCRC1OV1ZiSkloZ2V6YjdwYTJzYlZGQXAtc3hwLVZjTQ?oc=5) <sub>Vocal</sub>
- 📰 2026-09-27 [Waymo concentrated about 80% of its robotaxis in California and Texas — TechCrunch](https://news.google.com/rss/articles/CBMipwFBVV95cUxNS0h4dGsyN3B5d1o5dTdpVkhSZHZjeEtZLVYzQUx0azJPM2hZaF85SERpdUhxckVTaGU5RlNvV0hRUDlUZ1pxWnhIMzNDRFZOd3hkRnh2SWxTRGJRWkt4cnJzc0tQNk9WWjFhbzVLTW1HRFNobDNBWkhTYnFaUDhVSUdsenZyUjk2T0JYVEI5MEZnbTlWUHkwSVh2ME02Sl9PMTlSNVJzOA?oc=5) <sub>UA.NEWS</sub>
- 📰 2026-09-27 [TechCrunch Mobility: AV companies pick their lanes](https://news.google.com/rss/articles/CBMijAFBVV95cUxOLXRFeWtSOUtPeUZndVA4OGR5TVJ6ckprVXpxZHUxV25ISjZiNWM5ZDA2ZlgwLW54YXhuOGF6U2s3V09PNmthaTJRRjdaaHNINmQwWThsVWpfaGhMMkFyNXpkN1lqY1J1S2o5YTFCNW9RNHlqdDdLRjY3RldCWVBqZ0RqZXBmOFc3R2w5MA?oc=5) <sub>TechCrunch</sub>

</details>

<details><summary><b>Tesla</b> (123)</summary>

- 📰 2026-09-27 [Tesla Robotaxi Charging: 4 Details That Matter](https://news.google.com/rss/articles/CBMihwFBVV95cUxQM1NTWFYxQzdFeWUwMTYySGU1d2pPbmtOOVNXMzJLWGJUUUFMZFZWV21GSUl0YXJZakVIRE5hMV9SWlZCNmdzMHMtaC1YVGhJRmVHT0NWRjlWUzBiV1hxdEFjekU4ZFlIMkp5N3gzRmNuM1k1b1c1LWR5NkNYY3lPY1AxNUJrd1U?oc=5) <sub>BASENOR</sub>
- 📰 2026-09-27 [昨夜今晨：AI大模型竞速升级，BOB体育推荐网址推动智能终端新浪潮- 体坛网_体坛+](https://news.google.com/rss/articles/CBMiT0FVX3lxTE5NNGJiRnNWTGJRMWxYeHhUYjVTRHlDSzcyb2NJbjdBLThlUmNkSThkb1NnbUozSnlUNnhfVzZycVE2SlhfRjYtVkNzNkM3Rms?oc=5) <sub>体坛加</sub>
- 📰 2026-09-27 [SpaceX completes Starship Flight 14 launch rehearsal, gets final FAA approval for launch on Monday, more](https://news.google.com/rss/articles/CBMi2gFBVV95cUxNZ0pnbkZsdHE0eXF5Nl9OaW50VEoxaDR2WUs4dldJTk9uT1Y3SUgzYlBscDNUbEo5MTIydTRNeTVlTGJ2SFZVanRrZWlUVE92MU96U1U2QWRPaXdWVHlSbVVyQWd1c09UaGpGRlFLTEZ3UFY2b0tpQ29TQkFxNzJ4THZWSU9HVVdlVlA0YWZYZ2lzOGwtMVNtRTlCU3RQVDFGRzJ3S1ZGODBldnB5eUxKR0x6NnpzUDZfbzYwNTdzRXU0WWJRZVFZZkc1YmMxOXBJcWVpQkxEMWlSUQ?oc=5) <sub>Tesla Oracle</sub>
- 📰 2026-09-27 [Tesla Model S Breaks Crash Test Machine](https://news.google.com/rss/articles/CBMidEFVX3lxTE9haDFjUy1HekFEell1NGxvRXVIaElCYmV1ckkzSWVmb0lyN1F0aGhEblpxeldUQTJ3czZrOW1nUmo0eFZqVV9LazkwLVRjc2wxQ3Z2UERiWERiTktnQ0xpSU9iMlZlX1V4VVl3SDZDSFVMUVcy?oc=5) <sub>Teslarati</sub>
- 📰 2026-09-27 [Tesla's Roadster Teaser, US-China Airline Dispute, Boeing's Big Deals and More: This Week in Mobility](https://news.google.com/rss/articles/CBMi4wFBVV95cUxNcTdiWng5b2ZDUFdWb29XTGx1aVZjVzlzNjlnMmEwYlNIOElfTEdtbzZSeWxBZ2xJQ0tBZ2tvdjZXRnM3cE1Dd29NbVBRUjVzeUxsczlGNXk2cFhfTEQ3R1dEZ2pUMXhuZnRkNGtSdWJwV3NVR0QyY01heHJsSnZRbkFvT04zdnJsNjhlXzE2MjQzNVdUeGhYYk10RW5KbXJ4cFFjVUFYMERtREFhZE1ROTFjUEF3dENjc215QXlnRlp1bkhtcmh4a1NlV1NJbkhLRXNRMWVpYjJ6T1RXbzdab2VtUQ?oc=5) <sub>Benzinga</sub>

</details>

<details><summary><b>NVIDIA</b> (84)</summary>

- 💻 2026-09-18 [NVIDIA/swe-serve — SWE-Serve: an agentic benchmark of 53 production inference-engineering tasks derived from merged SGLang pull requests, run with Harbor.](https://github.com/NVIDIA/swe-serve) <sub>GitHub</sub>
- 💻 2026-09-16 [NVlabs/Skill2Env — Democratizing Collective Intelligence](https://github.com/NVlabs/Skill2Env) <sub>GitHub</sub>
- 📰 2026-09-28 [China May Let Alibaba Buy Nvidia’s RTX Chips, Information Says](https://news.google.com/rss/articles/CBMitAFBVV95cUxNSmpMYk0xRTBfdm5NMXRfNVNfMlE0cnppenNvTHNITzhVNXZ0R2NIX0Z3bmlWSmV1RHBpYURmWmdMT1ZLY2hUWG5WcDRsaFVSWktoRWFNQkdtRzg5UHpLeGstQXFGdkprdGhEbk05RUE5MEM4UTVlb281N3lOb2Y2WndNNHhzNUEtU3JlMUd5Z2FQRFRiM29JMU1fa25QRzBnekJJU3FYZGZlby1faklDS1pURG8?oc=5) <sub>Bloomberg</sub>
- 📰 2026-09-28 [Powerhouse PC, ideal for QHD or 4K gaming, gets price slashed by $239 on Newegg right now in this unmissable deal](https://news.google.com/rss/articles/CBMi2AFBVV95cUxNcUNmWlpkdDFtcEJpcW16TWlYMnViMi05aDc4dWJ2a0xhdHJTSzFnQTJJRjJRUEYzWUxMM0FhcWxGeEF5bkIzYU9WZTM4MGVJTi1zUjJObUxZWWlic0J5d3JnTGRTdmJXa19Sb0NpT3czUWd6TGJnVHEzRmxUSGNLeDRWTkgyVG8yNzF5aXk3MEd5T3RxMnF1MGdJSFlKWnVDVWhYa0hoMVRLODV2bk5uWW1nOG9rTG1ZdkRRY3I1N0tYWmRCcEdKZTVqNDlHMVI3LUpBd0k2eTQ?oc=5) <sub>pcguide.com</sub>
- 📰 2026-09-27 [China weighs allowing ByteDance, Alibaba to buy new Nvidia chips, report says](https://news.google.com/rss/articles/CBMiswFBVV95cUxOejE4SE4wRmpLOTJ5T2dyWFkzSG1zVEdDR09pbXFtM1JLVzB5THJOWnRzdmNSVGZtSzE0YkRpQUlLR2ZoZzVid3VtaXkzSG9CUlQ4anNkRmNxVjloM3ItRGM0aEV3MEVDMkt6WXQ3bXE0Y3V2VXBPLWdBN3UyV0lYaERpNWlDdVJLT1VfZmI0RFJaV1ViWjA4eGJvTXowWGZIRjBBNkVKTTdVVmFtdVNDeXZaWQ?oc=5) <sub>The Straits Times</sub>

</details>

<details><summary><b>Wayve</b> (43)</summary>

- 📰 2026-09-27 [Wayve Taps Ex-Waymo CFO Elisa de Martel to Navigate Critical Transition from R&D to Commercial Scale](https://news.google.com/rss/articles/CBMivwFBVV95cUxNSTZ5NlhOLW9ZZ016cms5ZFlBTG5lUUpfM1ZadEw1LWcwVHNsWW9XX0NwSkdZcHU5NmdjTHlXYnFFY1JSMGxLeUZFVEY0b2lJbE1tV2g5TDhpYjEzbVltOVI1RzdfVnY3NmtWT1c3a3U5R1lkSW5uV1FuWHRnTUJibEthZzFvV0lVUk1ISkxzZGxEYTZ1dTNsMTdwQkg3dGxCRC1OV1ZiSkloZ2V6YjdwYTJzYlZGQXAtc3hwLVZjTQ?oc=5) <sub>Vocal</sub>
- 📰 2026-09-27 [White House Releases Another Taxpayer-Funded Trump Video Ahead of US Midterms](https://news.google.com/rss/articles/CBMiaEFVX3lxTE80TlVfeUd3UFJEam1CZTdabkZjalVqTjFONjgzbkdzWDA5NmFIOEtnaWQzZjRxd0RkdVlfcXZkalRBanlEaTRTeXhxcktqbHZyZ1pGR3huU1dhVXhqZmZlWm1USVp6LVdh?oc=5) <sub>Межа. Новини України.</sub>
- 📰 2026-09-27 [After Nigeria Exit, Uber Launches Autonomous Rides In London](https://news.google.com/rss/articles/CBMiigFBVV95cUxNLUF6QjVUelRzR21sRGo4elZDVmNsSnFpX0pibDFTY3g0b1dpbDVlalVpOHcwRlNmWEFkUk5FMEpGRjcydHJ2d2xXU2V3cVE0VEVEMDdTbWFjaHlWeXkyc1dyTUZwajdRTzlOQUVoZVpTbHN0YmVEcnJEVGozdTRqWXp2U2dVWUZhVkE?oc=5) <sub>LEADERSHIP Newspapers</sub>
- 📰 2026-09-27 [Autonomous Vehicle Firms Pursue Partnerships as Robotaxi and Truck Fleets Grow](https://news.google.com/rss/articles/CBMibkFVX3lxTE1mZGlNMGtPdklhNDRnRGQ5bHY2Q3BpaWhPNjFzSHI5aFh5SGN0MVZzVGdCZ29yOXAxMUhNODdreEJDQWdpMVVXSHk4b3hMZHBBMnEweXhfVlZxdG5LSG1rMmZFeGNJaURaM1NfZEtR?oc=5) <sub>Межа. Новини України.</sub>
- 📰 2026-09-27 [Waymo concentrated about 80% of its robotaxis in California and Texas — TechCrunch](https://news.google.com/rss/articles/CBMipwFBVV95cUxNS0h4dGsyN3B5d1o5dTdpVkhSZHZjeEtZLVYzQUx0azJPM2hZaF85SERpdUhxckVTaGU5RlNvV0hRUDlUZ1pxWnhIMzNDRFZOd3hkRnh2SWxTRGJRWkt4cnJzc0tQNk9WWjFhbzVLTW1HRFNobDNBWkhTYnFaUDhVSUdsenZyUjk2T0JYVEI5MEZnbTlWUHkwSVh2ME02Sl9PMTlSNVJzOA?oc=5) <sub>UA.NEWS</sub>

</details>

<details><summary><b>Momenta</b> (90)</summary>

- 📰 2026-09-28 [Momenta Brings Driver-Assist Tech To Jeep And Peugeot](https://news.google.com/rss/articles/CBMiigFBVV95cUxOdTZqa2tVZWRpZGtOd05rT0pXRXRUQnFuTi1uUnlYVHVRMW5KTnFTbFJkU0pib3hYS0tORTBLdEh4cHBQWUk4dFQxQW1nN2x0bG53WldzS0JrdG1BczFaeHItTktzYW4tOVBKb1g5blk2WnB1Qlo3U2JuS0dfQnE4RG5HTHQ3cFlpZ3c?oc=5) <sub>Finimize</sub>
- 📰 2026-09-28 [Momenta and Stellantis' China JV with Dongfeng to co-develop intelligent driving technology](https://news.google.com/rss/articles/CBMivAFBVV95cUxQMzByVUtHMHlIWGhiUzl5Vzd0YXhiWnZ6R25pMzVUTjlLSW1SaDFnRy1fSnAwd1BlUWwzb0dBa3ljWnZLRWlKNmdIYXpXUTM3QUg3MjByLVZSd042VkZZT2F1LXVaM2xaZzN1X01WWWE1LS1wVG9hNlY4TjE1MmtKb1YzR1NoTTBhRHNwSzMzYW9LSDhTMlFjQ3g2NWtNYWdfSmFpX3c5bHlBSkxPUnFnbDBpb1ppS2ZQNHM3NQ?oc=5) <sub>Reuters</sub>
- 📰 2026-09-28 [Momenta 智驾方案上车标致、Jeep 全新车型 将落地中国及欧洲等市场](https://news.google.com/rss/articles/CBMiXEFVX3lxTE9xRnQ5dGJUSk9fRTRGQVFsZ0M4SmFqOHZpLXNZYklDc1lEeU93T2ZIbXNrSGpTTzhGTWhlMHdZRVJyZUduczdLdlBldzM4U19oTWR5cC1Xa01vbThH?oc=5) <sub>Moomoo</sub>
- 📰 2026-09-28 [Momenta, Stellantis' China JV with Dongfeng to co-develop intelligent driving technology](https://news.google.com/rss/articles/CBMiuAFBVV95cUxPWGVYNnVlOHpSVlB0czRybUZkcUJvZFBRMzRHNzd0cW1TV2p1TmM5MC1XZkl1RFEwLTlVcG9RbWdDN1A5UkFmTllUMEdLNmNOVEZrN3VEQWt3M0xMdWNHeURTZ0g5a3dDVDVTbVBhVWRXV1F2X2pHMlVxUmlKRWF6YW96ZmtabVhQZU9iRmVMTUcxeElVeXVWWGpkMzA5OWpQb3BkTnowVUVfT0Q0NkVlX1c4VG1hOGpu?oc=5) <sub>NST Online</sub>
- 📰 2026-09-27 [凯迪拉克XT5 PHEV 25.99万起，近期中型豪华SUV推荐值得买吗？+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE0wUURFSEhlb0otenpPV3lvLUhDQWtGeFl4QkVhU2oxZXNjcl9MNnNiUlFYZTAwS3NRVWJDdmNuN0xpNXYwMENQY2FIdGJRd0otZ2lSRTgydXhZdF9kbjBKZV9raWs0bkZta0hTUGwyMDZNZw?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>XPeng</b> (118)</summary>

- 📰 2026-09-27 [轿跑SUV 小鹏MONA L03申报 轴距2850mm](https://news.google.com/rss/articles/CBMiXkFVX3lxTE5rQ1JhRjVIcmF4TFN6ci1KRkFRNXdaTHZoU0YyOE5vQy1CZlhqeE84Ym55T01vdFVGN2U2Z1IzMEtEMXZQMzllRHNJYjB3WExEVVJYOE9XQzJQOURSYWc?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-27 [2026款小鹏MONA M03智驾值得买吗？750 TOPS算力只卖11.98万起，3个维度说清+FAQ](https://news.google.com/rss/articles/CBMif0FVX3lxTE9TYTE5eHlMV0d3ZXJnV0hCVmZoRlZTdDUwNlZLdVVMZmw4Q3BYMk5SYVAwZVFxVWFKS0NoM2VVTGVmR25hSmM1WlBzSHdHMU5aMW02RlRzUkE5UnRSbTVmZmxNTEFZMDdrZ2Qtei1ONlNFUmhzdDVhVDk0SzlkS2c?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-27 [小鹏MONA M03 11.98万起值不值？13.98万Max版和入门版差在哪，3个维度说清+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE1oeElfOHgyRVZCUmdBNEtRcmc0MmdMY2YyaTVvUXhGN18xVjNlSW1oS19OZkY5eFp0V19WOTgxZ1pEX2hPWl9XRGRVamFBMV9iMFlheHdscTgzUU1HaXN3QmtoZmk3dkJYbVc4a1pjRDlNZw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-27 [小鹏MONA M03 2026款值得买吗？12.38万起的L03 3个维度说清+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE1UQTI5SDFtUzFoWkpoeHhmNk9Vc2JldzZLZ1dVY19tbXpZRFVONkJYVENTQjB6OTRMbmlzdE9oUDJvUnFuZDNZMHl6RzNuSU9tdS1MTS1HeHc4WnZJRVFxMjVwcEg0RHc3U003YlZ6MXk3QQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-27 [小鹏汽车2月共交付新车30,453台，同比增长570%](https://news.google.com/rss/articles/CBMiXkFVX3lxTFBseFRMbVU0VjlUVzY1UHJNbWZOazBhdlUxZHk1NW5fM29FeHZDVU9yTGU3dlBxYnFBWHJndVFyT3ZDR21vc3EzZGc2Z014YWZuVHpZZl9RR2E0SXR4Nmc?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Li Auto</b> (88)</summary>

- 📰 2026-09-27 [理想i6 2026款值得等吗？上市时间、自研硬件、购车政策3个维度说清+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE5Ka2w1ZFdkV2d3cnFZcTlaNnZKTzZoSlptV3RUSllydjNhclVaLXlmTmxpU2lPel9kUmxlM2ktQnN3R3NyS1kzVXdrVlYwU3FpcVo2TFpqWnhXdTFxeExLVEQ1TlBQUW9TdVNRUGZ5cmlSdw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-27 [理想i6纯电SUV官图揭晓：10分钟补能500km，24.98万起值得等吗？+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5LNENqdE5DdjJTZEgzR2NfdFA3WnZCeGR2b1d4M0tvSE4zMHZJbmFIRjg2Y1luSVlRb0pnSXU4M0dNZnVoWXhsTTVCdTFTLXg3YTVaQTN0VF9hNEpIREY4?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-27 [Li Auto i9 Debuts With 705 km Range and 400 kW AWD](https://news.google.com/rss/articles/CBMilAFBVV95cUxNTVg0cjF4T3htZ29YekpDM0xHbU5JVEJlbDNoMVlSZVB3RmhxUFNiZ0R6MjA5N1BWZEZSdWdObTBKcjAzS2xxRzRTWE1GRExUUzZNanVoN1YxZFEzVmY4Ui1mdEcxM1VzQlBGOVpveFJtcEdyZktRa0ZBRi1jdU5sSmxBWTJXc3dZbnhoeUY2WTlfUW9q?oc=5) <sub>Electric Cars Report</sub>
- 📰 2026-09-27 [ID.4 X低配版试驾前，先看理想L6入门款值不值：24.98万3个维度+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE5XcGVJXzZlSXg0Z2JnWUx1dHcyc19YakhGR2k2QjBtNUllWVpTbEpZU2NGMTI3Y2FGNXlwYmVrWHN0cHlrSHJsVGNTRElxc3dBRmN6d1NGRGs5Yk55bDhJVDQ4WUNhZVZDUFRsa0lXUFBUUQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-27 [2026款后驱吉利 vs 传统豪华/新势力：舒适智能售后谁更胜一筹？3个维度说清+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBzZ05ydEtjd2E1TjFwUTFocmNIUnFhdjN0RGJYSy1ZUzJVVVdmNkZ0eXo3M2NyckNpRXJuWTNmd3NGMi1XYnRDZGl5UEFVM0EtZG1sNS1HcFV0T2x6UXZj?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>NIO</b> (89)</summary>

- 📰 2026-09-28 [长途自驾豪华SUV横评：理想L9、问界M8、蔚来ES8和神行者8，谁才是全场景旗舰？](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5DcGpMTWMtdnVrREVqSVRlTkRjeXFVU2pRdEtESjNibjYyNVhZWFkzbVFmQ0djZ1p4SXFYTUR6VlFZRTV5c2xrTXNfeDhFSTNXR3UyM2R5LUF4NFpIOS1v?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-27 [【视频】多种复杂路况，乐道L80智驾能打吗？#乐道蔚来世界模型NWM](https://news.google.com/rss/articles/CBMia0FVX3lxTE45QnZVeFlCNHMzZFhRTnRKbWF3Y19tN1ZFemk1dUNMMG8wenkxdzhLZjkzdTRFQ0k3SWlMODFXc3htNWx6WkFaRjJkS24tUkNqM01qZXVqSmp2dnhKZmwwSnlfNzd1ZXVqZEdz?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-27 [ET5T vs ET5，家庭出游选谁？后备箱大一倍真香！](https://news.google.com/rss/articles/CBMiW0FVX3lxTE90alZjaklfRjItUGN2bWsyN25rRjJzWGMzMmFNeHU4elIwVWNhcVpzOEEzemdHVmlDc1lwbkVQQVlIWmNEbWw3WFBhOUNvYlhyTkFZalpNTmM0ZGM?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-27 [【视频】8月蔚来公司在全国8省37城销量超越宝马、奔驰、奥迪](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBKZDh3clRnZUp3Q1JlM1dSNGVHTHktSjdZUTJuMnNRX0J4N1p1TzJYU1Fsa3VZTThfTTBybnhlSTZhUHpXRFg2c3hzd19qbHN0MnMzSzdCa1BieG8?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-27 [二手报价12.68万，蔚来ET5T 2024款，行驶4.90万公里，2次过户](https://news.google.com/rss/articles/CBMia0FVX3lxTE9iV2lKWC1POEFOaDYzQnVqZFNoeHk0YnRHdy1wcDNnbGx6MW5JaHM4VERvZGtOUV9mSHhhV3NfWl9CV09YQS1SRnNxVWNhVTZIV3lYYlhnMEFiNklMZzlSRWhycGRDWkFHOG5R?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Huawei</b> (150)</summary>

- 📰 2026-09-28 [周末一家老小出门，星海V6和极狐阿尔法T5谁更坐得下？](https://news.google.com/rss/articles/CBMia0FVX3lxTE1iekp4cjhub1dNUmtpSk1iOFdGd0RtS1dKQlM2NXNLSU1rRlc2dmtXTXhFUlRlRjMxQmdXSGNDXzlTbG5ieVl4MkxNRmhSejBDS1o2aDFpTXpFZUVLcUEzTUx6Y0wzczJRbXlZ?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-28 [24小时揽9157单！奕境X9把50万级旗舰逼到墙角了](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1fZlRJbVRSdFY1ZElpaWZ0MUpjUUVmZHU2MmdFeDlSVWRGSEJPREZsQmtVbE5YaGJoYVdBVWhseVcyRjlGVGtMTklIVjlGY0I3WUpQQjViSW5iN1U?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-28 [Huawei Mate XT2 import prices climb past €5,000, far above Apple’s iPhone Duo](https://news.google.com/rss/articles/CBMiswFBVV95cUxNOWcycjBSZjMyMlJyZGo4Skg0c2h5OUc1REc1ZlZrZ0RnNjNsRGFSMXp2elRFQlZUTkc4RTZxWDlSZmZXc3c1QjQtWU15cWlMWFFpbzZxMnlJcEZTTUEzMWdGdmVLUVpJV3ExaVNYMnFBc3ZDeWRXVWtZVy00NUNxYmg5NnBIaFVlYWdlcnNfZDE0RS1EZXpTYjUwaFVacHpmMUJMR0JpWmd5NGZpYlhFNHViZw?oc=5) <sub>Gizmochina</sub>
- 📰 2026-09-28 [东风华为合体，奕境X9掀桌，30万级大六座SUV市场变天](https://news.google.com/rss/articles/CBMia0FVX3lxTE54WTROVTVuOVkxWXBIblNtMm9KdF9ud18wTTdrNkcyUVN6VDhvaXNqVk5oMjZ5MUQxXy1GbDU5QU5oZkNyS0U4MnVFdHRCQ2tOVkthSWJ1OHk0a0hFZUZ4VXZXSDMtdTU1OW5j?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-28 [问界新 M8 全系标配 L3 级架构；手机暂不支持无网通信；《三星堆：未来往事》定档｜Do早报](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1VWDJLdVQtNGZ6dm13MC1FNHBtUXFhOEgtZmpsWm5TeXFIUWZXWTBCOGp0a0Y3RFk5TlI3d2xjNFBPUHNJc1pDXzZKYlhIN1BqakRidEZsN0pkRkJabnc?oc=5) <sub>DoNews</sub>

</details>

<details><summary><b>Baidu Apollo</b> (35)</summary>

- 📰 2026-09-26 [特斯拉Cybercab进入商业化运营，Robotaxi竞争转向运营效率与成本控制](https://news.google.com/rss/articles/CBMiVEFVX3lxTE5iYm1EU2d3RHV1dzE1ZmVWYnVlR01GR0dPZUdidERtdjAtLXlWZnFTUk94VTVMT0ZkMHV6bHl4bHJ3UHNNS0lRME55dUI4NENMZjVpaw?oc=5) <sub>虎嗅网</sub>
- 📰 2026-09-26 [The Robotaxi Reality Check You Won't Get From an Investor Deck｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1oVm5UbjMzU3RzeTlQUTNNQkkzdUUxMWFzalpCZlJIMGdKQWx5ZVo4eU1mQW9MWWxEdlFZSjlpUHRXMDRQd19uRkRVcWRCNmxEd2JraF9nVC1zd0ZDRDBj?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-09-26 [Is Tesla the Savior of Robotaxi? Unveiling the Truth Behind the Autonomous Ride-Hailing Revolution](https://news.google.com/rss/articles/CBMiU0FVX3lxTE4zVUdoQ201TVNPb3V2NXhmRkhoaVc2RGxPWGxGV1NJRHZvRk02QUszU252WlNWT0R6eFNrYVNwWm5JNldDa00xSUc0V1dHQTI2Q2Fj?oc=5) <sub>eu.36kr.com</sub>
- 📰 2026-09-25 [亚慱app官方网站上线！通勤族、孕妇、老人出行神器](https://news.google.com/rss/articles/CBMicEFVX3lxTE1RZXRDNm1wNFBKa0gxTXdkeHdKZDNxcHFQV3FISU42Z1Fqd2RYaEJpOGhEeWRmZ3NrNm5yV0dHcGhsNmdsNlpXdzlxYmp1M0xEeG8tYnVmNmlJTlN1RFVRWUdvOWNGbFM2TjBILUFuVlA?oc=5) <sub>womenofchina.com</sub>
- 📰 2026-09-24 [Waymo is Taking Robotaxis to Tokyo. Can Alphabet Get Ahead of Uber in Japan?](https://news.google.com/rss/articles/CBMiowFBVV95cUxNY2RtWFhhOHpQemRpdFhYNmFRdjNuaUdxbnFlNmlOa1V6djUtMkdlaUxrN3FqQk1Id2R1Z0pTTTc2YmtCWFd4aGd5Sk9vekFjM0I0VHd4UHBwQTlINEFkMzBnMWxTUXoxYUpyNkY4MktIWEdwSWZ1clV3YnBfZjI5RGFZOHJYNGdfUVhnVlZUbDU4ZnlPQ2N4WmNuY2JtUUU4amhj?oc=5) <sub>Yahoo Finance</sub>

</details>

<details><summary><b>Pony.ai</b> (75)</summary>

- 📰 2026-09-27 [Dubai opens autonomous vehicle testing center — The National](https://news.google.com/rss/articles/CBMilAFBVV95cUxOM3FGRGp5X1FPSjl5OFZMbzFHSXVRT1V6dWNYRTF0U29JallSSVRIVXhVNXJ5V0hnbWxQdWs5dmYxVWJlakdjNHBBc202VDRxMTNrU2xSOEVKXzgwS3ltUjIyU3J2OFFJbzBldV9meUJKSzdXUTByZEZKUXZ1b0xKbFdZY21LX04xQnNsM2lnMGFWWjlo?oc=5) <sub>UA.NEWS</sub>
- 📰 2026-09-27 [Dubai Mobility Labs opens for autonomous vehicle testing](https://news.google.com/rss/articles/CBMifEFVX3lxTFBHaDA4aWtmTFgyY1hGSmN5NHRlYmFPeGFldjBvOXd0Z2w3dC10VDlDQWE5LXFBLW8yMWlZOE9hanRJeXEwUkJhczlWM1VRMHg1cGRJalVmbnFBb3F0VHkwWElGcGVQdEJoZGRDcHdwV3BqZFVqc0E2T3Y1dGY?oc=5) <sub>tbreak.com</sub>
- 📰 2026-09-27 [15块大厂月饼再战中秋之巅，今年谁能一饼封神？](https://news.google.com/rss/articles/CBMiYEFVX3lxTE1HY3dXMnBJclZWaHhpNUVNV25HX3Zpbk9SMmR0RGhHTThFdzBaaTFDUFlYYnBmd3RzcUxyNjh1cWdNN0hXdEwtWHYxSWR6Q2EwQWJHWXBoejJOMFZpMktTSg?oc=5) <sub>thepaper.cn</sub>
- 📰 2026-09-27 [Dubai unveils advanced testing ground to prepare autonomous vehicles for the roads](https://news.google.com/rss/articles/CBMi0AFBVV95cUxNQWxYRWxTaGl5cGRQOFBFNUhFQkZDdGZLMnVwbmdYcExyMlc4NFU0YktuYTJjY2RlX3kzX1FaTUxZVWQtekUzcXpXa1lZa3pXbUljRDNQeXdvWWx1Mlpza0pVSWRWSTdnVHp2WWpmSlNHS2c2eC1DT0p4LUsxWEctNy1hRTdhdktDWEFvb3drbnd4V3FPUTJRN2FDaU96dHF5Vi03cU9KRkg2VGJhOXlzMHd1alJoWmJpR2UxWTdQZDVfenp5Z255UUVWWU5VQ0ha?oc=5) <sub>thenationalnews.com</sub>
- 📰 2026-09-27 [Robotaxi收入暴增691%、车队冲向3500辆，小马智行离盈利还有一道20倍鸿沟](https://news.google.com/rss/articles/CBMiRkFVX3lxTE9GOUltS0FPYmlhWDg1WnBJMlV0OGl3WTY2aHRacExPN202emhBUXZ5dUxlWF9lcFZCQy0xYlRtVlNVUENyUEE?oc=5) <sub>茉莉花新闻网</sub>

</details>

<details><summary><b>WeRide</b> (59)</summary>

- 📰 2026-09-27 [晚点独家丨Momenta 港股秘密递表，预计年内上市](https://news.google.com/rss/articles/CBMiW0FVX3lxTE0tUGs3MEhCSVhlQXJFVXh5MUNUbE9wdVg2YU81aFdqT3A3YUtINVZKeE03MVA5bnd1MWdLYzY5b3dVcGJfdzhKT2RYaTRFSk5vcHI5R3B5cGUxMTQ?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-27 [Dubai Mobility Labs opens for autonomous vehicle testing](https://news.google.com/rss/articles/CBMifEFVX3lxTFBHaDA4aWtmTFgyY1hGSmN5NHRlYmFPeGFldjBvOXd0Z2w3dC10VDlDQWE5LXFBLW8yMWlZOE9hanRJeXEwUkJhczlWM1VRMHg1cGRJalVmbnFBb3F0VHkwWElGcGVQdEJoZGRDcHdwV3BqZFVqc0E2T3Y1dGY?oc=5) <sub>tbreak.com</sub>
- 📰 2026-09-27 [RTA, DIEZ launch Dubai Mobility Labs for autonomous transport testing](https://news.google.com/rss/articles/CBMikgFBVV95cUxPY2o4NEJYdTFYMXdHYlBFM1UxTGt0OFpEc01KQ2d2d3ItaG93MWhNZWRiX2xkVmtMMlJIVmEwbWM3U3NWamRRZWdaWG1NQW03WjdtZUxDZ3JDTTQ0dmJtaU9vMExBS1FWS0RfLUgwekVmM1d2LXBqcnpua2hpb3MwWXpiaVBuekVBT1RhUGJwNkZQQQ?oc=5) <sub>wam.ae</sub>
- 📰 2026-09-27 [文远知行获西班牙L4自动驾驶牌照 二季度营收同比增82.2%仍亏损](https://news.google.com/rss/articles/CBMi3gRBVV95cUxNMnk5OGw3enFPamY2Y3BMdTgxWWF5NVd4Q0ZNTmpvSWh1LV93Y2toVk1IUEpXZUZnX3Boc19OajRGNC1YamNhem4taXJqMnMxcV9ESll5SzF4QWtDaURzb0xlSkY1YjV1Vmthcy01YXNzaS00LTVub3hzenlNbjNDbVZULVBLYzBQeWxQRDJybkpJVWdjMjJuUlBLS1NRZmRGMFhJQkIzUktlR1JCVEJpMXJxWXJ2SURCX2stWERfQnctV1JtV1JRZlZ2RlBNSFZqcWtFaHZqQ04xeW90UTk1Wi1wV0JCbjZuaTlKVnNJWmQ0RWFwWVJ1Tmc3dVFYZk9zRk45d1dwZlp5OFpnTk1tRDYzaUZXNm1ZaFBwUlg5OWJtQU5NRkhLdXEtV05QN2RxMzlYd0FyWllsM0VZa0p5VzR3OWhvSExHempsZFVGRHdpM1FXYjVSbWNQNnpoc3ZWakhESWJlZ1VoUktZQzF0azM0WFM4bUlpNEtuRWVEWDJLZ204SkRCeXR2NE9PUGZUWGJ0YndhLWo1b3BzYllIYktxRVdtdmJPem00b29qdndzSU44MGRYSzlaUThRREFvSTctZENWaTBodm5SdzFFLUliQ1FuMERGYkl5OGFscENFLTNBOEJ6LTl6ZlEwTjRiTElTTzJHMUhxd202OHJ0c3RqMG9JWnpKUWVhUENMMklUU01iNkV5SkREbFVjcXNqTWZZX1hPbEQzSUhQam1zTEtkNF9NdnVYWWl0ckg0RnNEVHYxdEl5UW5wVmppWWZzZmZOREtac2tRazgyVWc?oc=5) <sub>新浪财经</sub>
- 📰 2026-09-27 [Elon Musk Ally Jason Calacanis Bets These 4 Autonomy Stocks Will Be Bought Within 2 Years — And Double His Money](https://news.google.com/rss/articles/CBMi3gFBVV95cUxNcHBiYU9RMDB2Q3M1Zk9yODFvelBJd2pfZDRvZklSNGw1dGlSQktBcDlaSFp1TVBxZU9PcXdHR25INjhXNE9YMUJwT2oyM1Y0TjZKd25nRlZQR3Q1T2tidk44UTdBMTRZczB1eVhoSVFWeE9NbzVXZjlRZTVfVWNyXy1hWVYtaVJMb0w0c1hmVWRqS0ktMkRBQXhuNXU2UEtIeXZLMm1RRkU3ekV3VDctUGR6N3d3TjFfOGt1X3dkYUlhcmtXUF9YMlVnZjRPZHRycmNmc2o4TVFtV2FUSFE?oc=5) <sub>Stocktwits</sub>

</details>

<details><summary><b>Horizon Robotics</b> (66)</summary>

- 💻 2026-09-24 [HorizonRobotics/CogWAM](https://github.com/HorizonRobotics/CogWAM) <sub>GitHub</sub>
- 📰 2026-09-28 [限时8.08万起捷达M6开启预售将于10月中旬正式上市_热点推荐](https://news.google.com/rss/articles/CBMiYEFVX3lxTE15VTY1WU9iSEF5V0pRWEhTMHFXQlJoaTZsNGxScjVNaHJoV0V1ZmFYcDN4d2VnZDlGZUQtZGdRS3dVek5QRzhybU1DdGtidjdycW5kZjk2UnpKV2E1ZHRuSA?oc=5) <sub>证券之星</sub>
- 📰 2026-09-27 [启源Q06智驾不靠供应商方案，长安的“自研”牌含金量有多少](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPRU0tYUdxdW5KdXoxU1hmRmFMQlg4aFQ3WERsSXVteU1FcHhHMjUwVmNLbTlWSzd4R2Fib3F5aWhMOW9ac3pFYWNSVHN5TlRvRVIyU0dHRm04SlRhMkJwZlpJV3o5UTV4TVhLc3BwX0o1Wi1JdS1pYXQ3WXZuYnlEQVNqUkhVSmdm?oc=5) <sub>搜狐网</sub>
- 📰 2026-09-27 [ID. ERA 5S值得买吗？11.59万起配城市NOA，3个维度说清+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE9zQ1lnQzQ3S2NGNU93RE12WHZrMk1nYl9KQm5IVFA2aEtoUU45Y3ZDSEN3T3lJcDFHckJzMlpfRkxGNzB6blo3YzJadzUzRkJOV0lrUkZzS2JmT1ZyLWpNSF9GV0oyb2h0cVhXVFBPeU5ZQQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-27 [奇瑞QQ3售8.89万，连续5个月销破万](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBvZVNkZkMtOGJqU2liYklmYkxxaE5jYjhfY1NZSFdrZFJGWjktd1RFWDFRdTlXdk5FdUw2ZkgtS3RLdUh6SE93dzVReEpaekVyNFdDaktZNFNkXzQ?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (15)</summary>

- 📰 2026-09-28 [单飞后，半价“问界”来了！赛力斯官宣，新车9月28日发布！](https://news.google.com/rss/articles/CBMifkFVX3lxTE1pdjI1Q2h5Qjl4ckhIR0piVWdNYXdkc281bEM0VXBMUWYxM1VxUUg4ZXBMWDlZempiUkNFd0lsOG5wUkJTcWI5MkNTbUNoWnZzc2xwbW1ZSmlFWE9YclRMNjVNX0VHbVNaemkxZ1Z3bjg0QlFUelZUNTJZY2p4dw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-27 [k云体育中国官方全新升级：多模态AI生态正式发布，开启智能交互新纪元](https://news.google.com/rss/articles/CBMiU0FVX3lxTE5xUnRUdEVGdnhpQmtELV8zTzg2V19pTXJoUVVfQURQektBaHZnUDk2VGdXV1VQbTByX3Z3WW5sbXY4cGhUaXplN3Y1dmh6MVg4NFZr?oc=5) <sub>体坛加</sub>
- 📰 2026-09-27 [黑芝麻智能华山A2000家族芯片斩获2026国际新能源汽车创新技术奖](https://news.google.com/rss/articles/CBMiUkFVX3lxTE9uWTJmQ0hXcWlIU3YxU21JTlFGelM4eGxSU0tnWkI4OU56QmFyOFBUUjhJTFZwblJZNUFsVHdhUVhwUnhOQ29rblN2WWNGZFRzdkE?oc=5) <sub>icloudnews.net</sub>
- 📰 2026-09-27 [升博官网app已启动3nm云端AI推理芯片EYU-3300的量产筹备](https://news.google.com/rss/articles/CBMibkFVX3lxTE9SUEgyX05XeUVPZVFwMF9nalYwek1tSjJfSjJmdVhYcElhOVV3NHhjQmx4SVpVVkJYelJaVEstU3JqREhvV0RaazNLMTRGbmRjT3ZGMUwzMHlERGstZU45bWI2bERxOERsaVR1bEdR?oc=5) <sub>体坛加</sub>
- 📰 2026-09-26 [leyucom·乐鱼官方网2.0正式上线：全新UI与联网对战功能，免费下载](https://news.google.com/rss/articles/CBMickFVX3lxTE5IaXgzS1NiX2JDLTI2UG10andmdVdPa3ZCSXh5bk95Sk1JMlJlWW1TMl9hVGVqcE0zR0VsWVoySzlIS0RGbmFsYkNKUzBaYkNfTnRqSFJiT1hKSHR3aFZBdHlYMTFaTDc0WThFbUUwS3dNdw?oc=5) <sub>体坛加</sub>

</details>

<details><summary><b>Mobileye</b> (8)</summary>

- 📰 2026-09-27 [TechCrunch Mobility: AV companies pick their lanes](https://news.google.com/rss/articles/CBMijAFBVV95cUxOLXRFeWtSOUtPeUZndVA4OGR5TVJ6ckprVXpxZHUxV25ISjZiNWM5ZDA2ZlgwLW54YXhuOGF6U2s3V09PNmthaTJRRjdaaHNINmQwWThsVWpfaGhMMkFyNXpkN1lqY1J1S2o5YTFCNW9RNHlqdDdLRjY3RldCWVBqZ0RqZXBmOFc3R2w5MA?oc=5) <sub>TechCrunch</sub>
- 📰 2026-09-25 [Mobileye Global, Inc. Class A (MBLY) Live Share Price, Invest From India](https://news.google.com/rss/articles/CBMie0FVX3lxTE11MFdpQnBMczBkWUF5azl2bE1SaUIwT0Nhb2tLU3NPdTdtX2R0U3BSV2toUnNFN1puX3BqaEE2ZHJuRHdlN2N4dDY4a3NuZktyZFFSREFFQXhRTlVSbENxcUw3SHZ6VWRpN2tqZ0lmWHNkR3JuaXZWY0dXRQ?oc=5) <sub>INDmoney</sub>
- 📰 2026-09-24 [VW’s MOIA Starts Robotaxi Rides In Orlando](https://news.google.com/rss/articles/CBMiekFVX3lxTE5meUdldmgzNmRkbFlWLXlHU2J1RmVQRmlreWZqdDBRMVRud1NIV2tXdDNEdFBjYmU0NmdMel95UUdITUVtZVhZQ1BPSGo3R0syb0M0aVBrZWVvRWRGeHcwVEt6TEh2emZiX0RiSURXVFFrWC1TSUdjVjBR?oc=5) <sub>finimize.com</sub>
- 📰 2026-09-24 [Ruqi Mobility: Data Sales as a Business Model](https://news.google.com/rss/articles/CBMiuAFBVV95cUxQM19Zb2x4SzlmVk1pbGZkMXpHMGhGbURBa2tUWUMtOXVCQ0EyMTFkRDBkcWd0QlotcFJnU2hDRWZ5ZzdpQkx5cWswRFd5MHlXbkVNUFJFRVpZaUFtQWhYcnZkUXczRFlEUGZrN0paMTZQRjhkS1lXWEotSnZyZWpMYVRzSTgtSlFwMEtyNmVMT0ZHeWtBOFl4czRHeEcyX1JmOEhiUVlsb0tNNTJBOHFyaEhGSUtjWUJT?oc=5) <sub>All-About-Industries</sub>
- 📰 2026-09-24 [BlackBerry Falls 2% Despite Record QNX Quarter and Raised Full-Year Outlook; Mobileye Holds Steady](https://news.google.com/rss/articles/CBMi1wFBVV95cUxONnJLWWpPQU9jMVpXamNpVkVmRXJzNEFRZDgwc3dnclNXQW5LSWpTdnd2VVBIaXlpV3Zfal96akpOOFEyckVuN2FGU3IzbEZkSk9BQklFeElKbFdDbVJjZEVPUUJ0dXJqVHlZS1BmNW1xeGRTc1N3ZWdJZm1VLXpHbm90Ykt6MHJZd0xrZUhNUExPcm93UGNjRTliaC1sX25LTzBJZ0lOREk5clNoQjFOTXlWRUVUNXBnamY3ZWZRRVVkN21xZU95UXZBMkJRcUFWYldnYTJfVQ?oc=5) <sub>24/7 Wall St.</sub>

</details>

<details><summary><b>Aurora</b> (31)</summary>

- 📰 2026-09-27 [Aurora Innovation’s Road to Profitability Runs Through Fleet Expansion](https://news.google.com/rss/articles/CBMiuwFBVV95cUxOMGZqV0c1ZXlBY2VoanlHVEdycEFQQVBqYktmV01tMGM5c3lPT2Ntb0Q5TndWTlk1dUtOSzEteHhJWWI4RFY2YnBwbEduQ3RqUXVrdTFoUTZzd2xQZXViQmxLWnFicjhmUTJIRTBsamxnUVZtZDdzOVhycm0tM3NCX2xYMmE1M1ZCWlJoZXVpd095cHc2M21uVmM2empyVUcwMkdvejNMNXRFbDVvNnRRNkRoZkJzZGdGaEp30gG7AUFVX3lxTE4wZmpXRzVleUFjZWhqeUdUR3JwQVBBUGpiS2ZXTW0wYzlzeU9PY21vRDlOd1ZOWTV1S05LMS14eElZYjhEVjZicHBsR25DdGpRdWt1MWhRNnN3bFBldWJCbEtacWJyOGZRMkhFMGxqbGdRVm1kN3M5WHJybS0zc0JfbFgyYTUzVkJaUmhldWl3T3lwdzYzbW5WYzZ6anJVRzAyR296M0w1dEVsNW82dFE2RGhmQnNkZ0ZoSnc?oc=5) <sub>Insider Monkey</sub>
- 📰 2026-09-27 [Autonomous & Self-Driving Vehicles News: Waymo, ComEd, TIER IV, Einride, Hyundai, AEye, Witherite, Aurora, NHTSA, Volvo & Arbe Robotics \| auto connected car news](https://news.google.com/rss/articles/CBMi9gFBVV95cUxPXzN2cFVQendmTl9ma0N5YzVwbkJRZ0ZneTdESG1VeTduazdQVzN6MXJwWmt2UlZYZDh2WkVZLU10TFphRnhVRGNidU5yU1p4dFhLTlR3Ukk3S1VSQkVqd0pkYXhNZ2RyZHp3SXpJNW14NVhORWl2WE9CVm9QSDN6aXJjS1Brdjd3ZEw3ODczM1ItVVlidXJ2TmFPbW1OZ08xZnozd2hKbWNZdmpTS1lLZVB0ZjdlSzlQa3VKVGFsQ2ZUeXVaWVZWNW5SaDh4NzVrZVZROVFmMkVwVUVqbXp0ZTlBOEpnYVdWMEdNYUFZdWQzS2k5SkE?oc=5) <sub>AUTO Connected Car News</sub>
- 📰 2026-09-27 [Aurora Innovation (AUR): What Could Drive AUR Higher or Lower From Here?](https://news.google.com/rss/articles/CBMinwFBVV95cUxPcC1VZ3RJY3VQWU9MTGtnenhtSVdDZWdGY0FBWG1ibXlsLVpVTlliMnI2cjBkZ1NRSXRvbWk3MVRVNllYclgxNWJqWDg5VDFFUWhmT0dRTUc1bm11c3ZtMUliS2R3Y2c4eUtYYVlzTnVKUVhtU2p2Mmx4UlctSHVVTllpczB6ZTRybk5IUkVGY1UzZldqdDN4VUtZRkVzTUk?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-09-27 [Aurora plans 30,000 driverless trucks as carriers weigh cost](https://news.google.com/rss/articles/CBMif0FVX3lxTE5RSFN4cVVvUmtzSXpLcEhCZTh6b3EzS2ZGbjBOdmN1TjNheGx0TjAtd3FfWFZBblNiWGhiWGZvakxQRkY4b00tdFhaR1Q2b3hHX1YyU2tSUi1VeXhtX09Pc29raS04eTFwR2p2ZmM1ejJ1ZXFfT1hIVVp3d1o2Z0E?oc=5) <sub>FreightWaves</sub>
- 📰 2026-09-26 [Aurora Showcases Commercial Driverless Trucking at Investor Day](https://news.google.com/rss/articles/CBMitgFBVV95cUxOWGNkTTJweWNXNXpNVEc3YzlxQWEyRHF6b09YVGluTFg3dFdOV0JLRXc0R0ctYkZGSVBGUjBneDBhVWhsejgxQkMyeGlpTURuRnJHV3hpS2tnSVhxYWhMVHZYWlA4NVJmY3ZLOGJQLVJnSmpMYzFKd2tyVkp1N2E1V2c4Wnh0RDR2Ni1fUklZRThFY3VhRTN5Sno4VE5mRjE0WkMwRmZrZUpSbjRpV2lzVHhENTlCUQ?oc=5) <sub>TipRanks</sub>

</details>

<details><summary><b>Zoox</b> (53)</summary>

- 📰 2026-09-27 [Zoox robotaxi crash on Las Vegas Strip raises questions about driverless safety](https://news.google.com/rss/articles/CBMirwFBVV95cUxOanNQaVZhWGh5dkdFOXBWUHdlVlNncnE5aHdINGRrai1uWi1UdmZHUF9zNHMydkJoTnhEMUdscnBmMUZVQm9HMFlZdnNvYllFM2VXQ3NvSGtqRXFkZFVaZW05dk50aXBLbU9EZzF2aVVJQTVDeU0tazhnNWlLeGVZS2tELWhNUkpBVGsxM1ZhQWk2eWZVbVk1ZTNEd2o2ak9LOGh6aC12eHk0Zl9Jelpn?oc=5) <sub>KSNV</sub>
- 📰 2026-09-27 [Zoox’s Robotaxi Is All-Electric. The SUVs Teaching It to Drive Still Have Tailpipes.](https://news.google.com/rss/articles/CBMimAFBVV95cUxQZ281bHRmdFI4clRoa2J3a1MtcVI0SVpxanViTjl3akx0SGZSanhCZDN4cThZOFBpQXZBaWNuVnpMV2poc3BmX1dtY2J6NE9BLU44NWI4MjkxeXNTeUJrY0REUGtrLXh1TmNMQXVVYTV0NUMyOXFXUU1CSlRxT2hmUjZJMzl2dk4xc1dKLXQ2WHVLdjZVT3Fucg?oc=5) <sub>The Auto Wire</sub>
- 📰 2026-09-27 [Autonomous Vehicle Firms Pursue Partnerships as Robotaxi and Truck Fleets Grow](https://news.google.com/rss/articles/CBMibkFVX3lxTE1mZGlNMGtPdklhNDRnRGQ5bHY2Q3BpaWhPNjFzSHI5aFh5SGN0MVZzVGdCZ29yOXAxMUhNODdreEJDQWdpMVVXSHk4b3hMZHBBMnEweXhfVlZxdG5LSG1rMmZFeGNJaURaM1NfZEtR?oc=5) <sub>Межа. Новини України.</sub>
- 📰 2026-09-27 [AlienFest at Windmill Library draws crowds to explore UFOs and UAPs](https://news.google.com/rss/articles/CBMinwFBVV95cUxOeGZtMk5WTUpwUE5FbGp3dUhNMVJacVFCbnA3QkgyZG5OSHdFSHZsd1hhUjVyOHo2aUtsaGpja21DOEMtOWx0OWxpYjRJOTJGWDFlOVJrWXl6OHU3T01EYllqc28wa1hMLWpReU02eGhyWEMtYmh6bDVMaHZxX1NLU0dTbUV2MUdwWXZBMWstdE9udENyYkJzTVpicmJfWU0?oc=5) <sub>KSNV</sub>
- 📰 2026-09-27 [White House Releases Another Taxpayer-Funded Trump Video Ahead of US Midterms](https://news.google.com/rss/articles/CBMiaEFVX3lxTE80TlVfeUd3UFJEam1CZTdabkZjalVqTjFONjgzbkdzWDA5NmFIOEtnaWQzZjRxd0RkdVlfcXZkalRBanlEaTRTeXhxcktqbHZyZ1pGR3huU1dhVXhqZmZlWm1USVp6LVdh?oc=5) <sub>Межа. Новини України.</sub>

</details>

<details><summary><b>Motional</b> (9)</summary>

- 📰 2026-09-26 [The Robotaxi Reality Check You Won't Get From an Investor Deck｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1oVm5UbjMzU3RzeTlQUTNNQkkzdUUxMWFzalpCZlJIMGdKQWx5ZVo4eU1mQW9MWWxEdlFZSjlpUHRXMDRQd19uRkRVcWRCNmxEd2JraF9nVC1zd0ZDRDBj?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-09-26 [Walter Piecyk and Grayson Brulte: The Robotaxi Bottleneck Is Depots, Not Software](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBlREZaMnNLXzJxMGdBNUQ0S0Y1VGxGb0NqVWJtZVpfOGl2SW9pZnNhRFpacjVLUUdFOG10S0ozWHFVazVveWkxQUt3dnNNeFlyU1BiVlNTNjlreWs?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-09-21 [Hyundai to Build Tens of Thousands of IONIQ 5 Robotaxis for Waymo in the US as EV Strategy Shifts Toward Autonomous Mobility](https://news.google.com/rss/articles/CBMi7wFBVV95cUxQc0QyV2VOamV0NmZXTzJDb1NqeFRfblA5NXdXcWZ5S0tuaGxsa0k2Vi12V0N6WDkxRjdfWUlKNG5jUWtWQy1DOGtMZ1M5Uml2a3hkZUdSSHNab3BtTlJOaXplclpRZjNocVN4a0dHWGpCbHNpZUN6ZDZCaUwwcE9MZXo4SDBrY09jdXNSVld1SDZfaEluLWZ1WEJVaFRPdkJBMnRtVDFXR1RicEZEdzdITkVTZjNJbkJ0bklOcExMN28wN0xXTmg0S1I1b2RCNEg5eHhISHU3eFcyVzBIei1WcnZvb2dSOVhzSVFhcTFMTQ?oc=5) <sub>EVTech.News</sub>
- 📰 2026-09-19 [Hyundai Motor turns to robotaxis as U.S. EV demand slows, to produce at Georgia plant](https://news.google.com/rss/articles/CBMiwwFBVV95cUxPNEtaQl80RDhIbFNaWDJkRGQwMllxQzdMZ0JxZC1EcEsxdUdkWWJqMzlRbVFVOGc5VF9Ta2cxZEl0b3o3ZEhjeUczZTdDWmdaTUg0VGppeUhuX1dKbUdMLWJ5X1VSOWFxYmZiYWlGQ1ZiT0NDRmJ0YkZiNWRTQWV1SnFIc2hyNVh4Q3dYRE5UWXJJUFoxTEEweng3MExUWnVtaFllalBTZ3dfQ2ZjSXFsWWRzLWw3Nkl4SDFLNzJrVzdxU1k?oc=5) <sub>디지털투데이</sub>
- 📰 2026-09-18 [System helps humans predict when self-driving cars will make mistakes](https://news.google.com/rss/articles/CBMirAFBVV95cUxQY2xDYi02dkFwc3hwX3ZOdmliM2JNWUlhUVFXQ2lIeFRxNjJKVHE5T2REVUVIWGY3YzByNE5OWjd3RU52R3Y1NWFydmtHMU5CZUIya2NhQnMzYXJqRDlSY2tSUW10XzAyY2JYV0l5UGlHX096TFZGX3g4bTczZEFacTF3R3BXVkJ2LUU0VHh2RTRpdWxxQVB5Z3NjVnlfM2pMWG11Q1hrVFRkekJH?oc=5) <sub>Technology Org</sub>

</details>

<details><summary><b>comma.ai</b> (38)</summary>

- 📝 2026-09-16 [Bugs that broke driving: Machine Learning edition](https://blog.comma.ai/ml-bugs/) <sub>official blog</sub>
- 💻 2026-09-15 [commaai/comma_hack_7 — some chestnut examples](https://github.com/commaai/comma_hack_7) <sub>GitHub</sub>
- 📰 2026-09-27 [Autonomous & Self-Driving Vehicles News: Waymo, ComEd, TIER IV, Einride, Hyundai, AEye, Witherite, Aurora, NHTSA, Volvo & Arbe Robotics \| auto connected car news](https://news.google.com/rss/articles/CBMi9gFBVV95cUxPXzN2cFVQendmTl9ma0N5YzVwbkJRZ0ZneTdESG1VeTduazdQVzN6MXJwWmt2UlZYZDh2WkVZLU10TFphRnhVRGNidU5yU1p4dFhLTlR3Ukk3S1VSQkVqd0pkYXhNZ2RyZHp3SXpJNW14NVhORWl2WE9CVm9QSDN6aXJjS1Brdjd3ZEw3ODczM1ItVVlidXJ2TmFPbW1OZ08xZnozd2hKbWNZdmpTS1lLZVB0ZjdlSzlQa3VKVGFsQ2ZUeXVaWVZWNW5SaDh4NzVrZVZROVFmMkVwVUVqbXp0ZTlBOEpnYVdWMEdNYUFZdWQzS2k5SkE?oc=5) <sub>AUTO Connected Car News</sub>
- 📰 2026-09-26 [Only 15 Minutes, Riau Researchers Offer a Way to Get Water to Put Out Peat](https://news.google.com/rss/articles/CBMiQkFVX3lxTFA2aTZXWGtxRHBaczVwMFBwRENsMHpBQ292MVBzMEpHbF8wTXpjekdqeElmVnM1a2VVWEN0YUZPZGM4dw?oc=5) <sub>VOI.ID</sub>
- 📰 2026-09-26 [GPT-6 Astra is the first model to drive a real Corolla on its own](https://news.google.com/rss/articles/CBMijwFBVV95cUxNM0llcjdUV1l5U2Jvc0ZTaWhrdmh2bHctM29ubFp6RWdRemtXNDFmZWhvcW5mNXRidE9FTEFCcXl3MkNhTHdUbHRqSDZRWVNDNGQ0OHFFNzBmSWZONzVZSFhfaUhWdF9WcE5mQjBCT21WZWt5TE1pZjlCRjVDT1RXY2NITlN0dTNZdUQySndKZw?oc=5) <sub>Pasquale Pillitteri</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
