# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-10-25 · 1,295 papers tracked · 42 curated.

**Selection rule.** A paper is listed only if it (1) is primarily about autonomous driving,
(2) has public code, and (3) shows at least one strong signal: accepted at a top venue
(CVPR / ICCV / ECCV / NeurIPS / ICLR / ICML / CoRL / RSS / TPAMI, or ICRA / IROS / AAAI / RA-L),
≥200 GitHub stars, ≥3 citations / month, or a well-known lab with traction. Papers are then ranked by a
composite score (venue, stars, citation velocity, LLM rubric for novelty / rigor / impact, SOTA claims)
with a per-topic cap. See [`scripts/rank.py`](scripts/rank.py).

📅 [Daily digests](daily/) · 🗓️ [Weekly digests](weekly/) · 📦 [Raw data](data/)

## Contents

- [VLA / VLM for Driving](#vla--vlm-for-driving) (10)
- [World Models & Generative Simulation](#world-models--generative-simulation) (6)
- [End-to-End Driving & Planning](#end-to-end-driving--planning) (9)
- [3DGS / NeRF Reconstruction & Sensor Sim](#3dgs--nerf-reconstruction--sensor-sim) (4)
- [Perception: BEV, Occupancy, 3D Detection, Mapping](#perception-bev-occupancy-3d-detection-mapping) (8)
- [Datasets & Benchmarks](#datasets--benchmarks) (2)
- [Safety, Robustness & Evaluation](#safety-robustness--evaluation) (3)
- [Industry Tracker](#-industry-tracker)

## VLA / VLM for Driving

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Teaching Vision-Language-Action Models What to See and Where to Look](https://arxiv.org/abs/2607.01658)<br><sub>Yuguang Yang, Canyu Chen, Zhewen Tan et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 34](https://github.com/ShivaTeam/DriveTeach-VLA) | Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving |
| [DeepSight: Long-Horizon World Modeling via Latent States Prediction for End-to-End Autonomous Driving](https://arxiv.org/abs/2605.10564)<br><sub>Lingjun Zhang, Changjie Wu, Linzhe Shi et al.</sub> | ICML 2026<br>2026-05<br>📑 2 | [⭐ 31](https://github.com/hotdogcheesewhite/DeepSight) | End-to-end autonomous driving systems are increasingly integrating Vision-Language Model (VLM) architectures, incorporating text reasoning or visual reasoning to enhance the robustness and accuracy of driving decisions |
| [SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving](https://arxiv.org/abs/2610.20609)<br><sub>Shaoyuan Xie, Zihan Zhang, Jingxuan Wang et al.</sub> | CoRL 2026<br>2026-10 | [⭐ 29](https://github.com/ASGuard-UCI/safedrive-vla) | Vision-Language-Action (VLA) models are gaining attention in autonomous driving, inheriting commonsense priors from large language models (LLMs) and widening the navigation interface from a fixed command set to free-form… |
| [Scene-Adaptive VLA: Efficient Autonomous Driving via Dynamic Layer Routing](https://arxiv.org/abs/2610.24590)<br><sub>Yujia Yang, Quan Yuan, Jiawei Fan et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 2](https://github.com/yang-luvu/Scene-Adaptive-VLA) | Vision-Language-Action (VLA) models offer a promising paradigm for autonomous driving |
| [CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving](https://arxiv.org/abs/2607.04179)<br><sub>Zhaohong Liu, Hao Ye, Xianlin Zhang et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 1](https://github.com/MICLAB-BUPT/CritiqueDriveVLM) | End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving |
| [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)<br><sub>Nan Yang, Zhanwen Liu, Linfeng Zhang et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 11](https://github.com/Zizzzzzzz/MVPruner) | Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings |
| [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)<br><sub>Yuan Gao, Wenting Miao, Mattia Piccinini et al.</sub> | IROS<br>2026-07<br>📑 1 | [⭐ 29](https://github.com/TUM-AVS/Chat2scenic) | Validating autonomous driving systems requires diverse, regulation-compliant test scenarios |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 12 | [⭐ 522](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
| [Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air](https://arxiv.org/abs/2605.31066)<br><sub>Tianle Zeng, Yanci Wen, Xueang Yu et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 1,123](https://github.com/louiszengCN/CarlaAir) | Recent aerial vision-language-action (VLA) models show promising single-UAV capabilities, such as tracking moving objects and navigating to language-specified landmarks |
| [GRAVA: Grounded Reasoning-to-Action Representation and Learning for Autonomous Driving](https://arxiv.org/abs/2609.15169)<br><sub>Xiao Liu, Haoyu Li, Jianghao Leng et al.</sub> | arXiv<br>2026-09 | [⭐ 355](https://github.com/AhernResearch/grava) | Driving vision-language-action (VLA) models increasingly reason before acting, but their intermediate reasoning is often weakly grounded in physical scene evidence and loosely connected to executable behavior |

## World Models & Generative Simulation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [HERMES++: Toward a Unified Driving World Model for 3D Scene Understanding and Generation](https://arxiv.org/abs/2604.28196)<br><sub>Xin Zhou, Dingkang Liang, Xiwu Chen et al.</sub> | ICCV 2025<br>2026-04<br>📑 4 | [⭐ 72](https://github.com/H-EmbodVis/HERMESV2) | Driving world models serve as a pivotal technology for autonomous driving by simulating environmental dynamics |
| [FrozenDrive: Zero-Shot Text-Guided Driving Scene Generation and Data Augmentation with Parameter-Free Frozen Diffusion Model](https://arxiv.org/abs/2606.20110)<br><sub>Yuhwan Jeong, Hyeonseong Kim, Daehyun We et al.</sub> | ECCV 2026<br>2026-06<br>📑 1 | [⭐ 10](https://github.com/daehyunwe/FrozenDrive) | Synthetic data for autonomous driving is surging, powered by diffusion models that promise scalable scene generation |
| [MESSENGER: Memory-Enhanced Sequential Scene Flow Estimation via Autoregressive Next-Frame Forecasting](https://arxiv.org/abs/2610.10759)<br><sub>Jiuming Liu, Jianing Li, Mengmeng Liu et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 0](https://github.com/liujiuming123/Messenger) | Scene flow can capture low-level 3D motion displacements in dynamic scenarios |
| [ASTAD: Asymmetric Style Transfer for Synthetic-to-Real Adaptation in Autonomous Driving](https://arxiv.org/abs/2606.29286)<br><sub>Dingyi Yao, Xinqi Zhang, Lihui Peng et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 2](https://github.com/Dingyi-Yao/ASTAD) | Synthetic data mitigates the data scarcity problem in autonomous driving perception |
| [Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends](https://arxiv.org/abs/2606.01164)<br><sub>Jiuming Liu, Chaojun Ni, Mengmeng Liu et al.</sub> | arXiv<br>2026-06<br>📑 8 | [⭐ 245](https://github.com/liujiuming123/Awesome-Interactive-World-Model) | With rapid development of large language models and diffusion-based content generation, world modeling has attracted increasing research attention, benefiting various downstream domains such as game engines, embodied AI,… |
| [Is Your Driving World Model an All-Around Player?](https://arxiv.org/abs/2605.10858)<br><sub>Lingdong Kong, Ao Liang, Tianyi Yan et al.</sub> | arXiv<br>2026-05<br>📑 6 | [⭐ 257](https://github.com/worldbench/WorldLens) | Today's driving world models can generate remarkably realistic dash-cam videos, yet no single model excels universally |

## End-to-End Driving & Planning

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](https://arxiv.org/abs/2609.26792)<br><sub>Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.</sub> | CoRL 2026<br>2026-09<br>📑 1 | [⭐ 13](https://github.com/VAIL-UCLA/DreamStream) | Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions |
| [DriveMLP: When Training Strategy Outperforms Model Complexity in Autonomous Driving](https://arxiv.org/abs/2610.29676)<br><sub>Alessandro Canevaro, Julian Schmidt, Hang Yu et al.</sub> | CoRL<br>2026-10 | [⭐ 3](https://github.com/alessandro-canevaro/DriveMLP) | Learning motion planning policies that remain reliable under closed-loop execution is a central challenge in Autonomous Driving (AD) |
| [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)<br><sub>Shen Zheng, Anurag Ghosh, Gaurav Parmar et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 32](https://github.com/ShenZheng2000/WarpI2I) | Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs) |
| [G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance](https://arxiv.org/abs/2606.26017)<br><sub>Hang Yu, Ye Jin, Alessandro Canevaro et al.</sub> | IROS 2026<br>2026-06<br>📑 5 | [⭐ 6](https://github.com/HangYuu/G2DP) | In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 17 | [⭐ 349](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
| [SimWAM: A Simple World Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.07468)<br><sub>Zongchuang Zhao, Xin Zhou, Tianyang Xu et al.</sub> | arXiv<br>2026-08<br>📑 9 | [⭐ 198](https://github.com/H-EmbodVis/SimWAM) | In autonomous driving, World-Action Models (WAMs) have improved end-to-end planning by transferring video dynamics priors to action prediction, but many still couple planning with future-video generation at inference, in… |
| [Latent-Centroid Steering: Single-Pass Classifier-Free Guidance for Command-Aligned Autonomous Driving](https://arxiv.org/abs/2608.00237)<br><sub>Meibo Hu, Jiamian Wang, Pichao Wang et al.</sub> | IROS 2026<br>2026-08 | [⭐ 2](https://github.com/codingmlinprocess/LCS) | Vision-language models (VLMs) have recently emerged as a promising paradigm for end-to-end autonomous driving, enabling agents to map multimodal inputs and high-level navigation instructions directly to executable trajec… |
| [STAGE: STyle-controllable Action GEneration for personalized autonomous driving](https://arxiv.org/abs/2607.29517)<br><sub>Zihao Liu, Xing Liu, Yizhai Zhang et al.</sub> | RA-L<br>2026-07<br>📑 1 | [⭐ 6](https://github.com/CarlDegio/STAGE) | Driving style refers to the behavioral preferences that drivers maintain during driving, shaped by their diverse experiences, habits, and needs, and is typically reflected in varying levels of aggressiveness |
| [A Survey on End-to-End Autonomous Driving Training from the Perspectives of Data, Strategy, and Platform](https://arxiv.org/abs/2610.00926)<br><sub>Chengkai Xu, Yiming Cui, Jiaqi Liu et al.</sub> | arXiv<br>2026-10<br>📑 5 | [⭐ 109](https://github.com/Jiaaqiliu/Awesome-Training-Ecosystem-for-E2E-AD) | Autonomous driving is a cornerstone technology for the future of intelligent transportation, where end-to-end learning has emerged as a transformative paradigm that directly maps multimodal sensory inputs to driving acti… |

## 3DGS / NeRF Reconstruction & Sensor Sim

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DriveWeaver: Point-Conditioned Video Inpainting for Controllable Vehicle Insertion in Autonomous Driving Simulation](https://arxiv.org/abs/2606.31918)<br><sub>Junzhe Jiang, Zipei Ma, Zijie Pan et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 16](https://github.com/LogosIntelligenceLab/DriveWeaver) | A pivotal step in autonomous driving simulation involves inserting foreground vehicles with predefined trajectories into simulated scenes |
| [Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796)<br><sub>Leshu Li, Jie Peng, Yang Zhao</sub> | ICRA<br>2026-06 | [⭐ 14](https://github.com/UMN-ZhaoLab/Pocket-SLAM) | 3D Gaussian Splatting (3DGS) has garnered significant attention in Simultaneous Localization and Mapping (SLAM) due to its advances in capturing fine-grained geometry features and synthesizing novel views |
| [NIDAR: NIR-Guided Intrinsic Decomposition for Scalable Scene-Agnostic LiDAR Intensity Reconstruction](https://arxiv.org/abs/2609.36878)<br><sub>Junjie Zhang, Jie Yin, Kefei Qian et al.</sub> | IROS 2026<br>2026-09 | [⭐ 22](https://github.com/Zjj587/NIDAR) | LiDAR return intensity provides complementary surface-response cues for robotic perception and state estimation, yet many simulation pipelines omit it or reproduce it using reconstruction methods that require real intens… |
| [MM-TRELLIS: Point-Cloud Guided Multi-Modal 3D Vehicle Generation in Autonomous Driving](https://arxiv.org/abs/2606.24301)<br><sub>Hongli Xiao, Youjian Zhang, Yucai Bai et al.</sub> | ICRA 2026<br>2026-06 | [⭐ 9](https://github.com/HongliXiao/MM-TRELLIS) | Recovering realistic 3D vehicle models from autonomous driving scenes is crucial for synthesizing training data and building simulation environment |

## Perception: BEV, Occupancy, 3D Detection, Mapping

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Deformable Gaussian Occupancy: Decoupling Rigid and Nonrigid Motion with Factorized Distillation](https://arxiv.org/abs/2605.28587)<br><sub>Yang Gao, Wuyang Li, Po-Chien Luan et al.</sub> | CVPR 2026<br>2026-05<br>📑 2 | [⭐ 22](https://github.com/vita-epfl/DeGO) | Understanding dynamic 3D environments is essential for safe autonomous driving, particularly when reasoning about human-centric, nonrigid agents |
| [FreeOcc: Training-Free Embodied Open-Vocabulary Occupancy Prediction](https://arxiv.org/abs/2604.28115)<br><sub>Zeyu Jiang, Changqing Zhou, Xingxing Zuo et al.</sub> | RSS<br>2026-04<br>📑 7 | [⭐ 143](https://github.com/the-masses/FreeOcc) | Existing learning-based occupancy prediction methods rely on large-scale 3D annotations and generalize poorly across environments |
| [Horizon3D: Sparse Radar-Camera Fusion for Long-Range 3D Perception in Autonomous Driving](https://arxiv.org/abs/2606.31096)<br><sub>Geonho Bang, Geunju Baek, Dongyoung Lee et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 25](https://github.com/geonhobang/Horizon3D) | Long-range 3D object detection is critical for safe autonomous driving at highway speeds, yet existing radar-camera fusion methods remain limited at extended ranges |
| [Explainability-Aware Frustum Attack: Exposing Structural Vulnerabilities in LiDAR-Based 3D Object Detectors](https://arxiv.org/abs/2606.29963)<br><sub>Chengzeng You, Binbin Xu, Soteris Demetriou</sub> | ECCV<br>2026-06 | [⭐ 2](https://github.com/SecMindLab/Saliency_LiDAR) | The structural vulnerabilities of point cloud-based 3D object detectors remain poorly understood |
| [PointLAM: Local Attentive Mamba for Efficient Point-based 3D Object Detection](https://arxiv.org/abs/2609.21780)<br><sub>Xuanming Shang, Weijia Zhang, Chao Ma</sub> | ECCV 2026<br>2026-09 | [⭐ 5](https://github.com/PointLAM/PointLAM) | 3D object detection from LiDAR point clouds faces a fundamental dilemma: voxel-based methods achieve efficiency at the cost of geometric quantization, while point-based methods preserve fidelity but suffer from prohibiti… |
| [UniD-Shift: Towards Unified Semantic Segmentation via Interpretable Share-Private Multimodal Decomposition](https://arxiv.org/abs/2605.07356)<br><sub>Shuai Zhang, Zhecheng Shi, Zhuxiao Li et al.</sub> | CVPR 2026<br>2026-05 | [⭐ 5](https://github.com/shuaizhang69/UniD-Shift) | Semantic segmentation of large-scale 3D point clouds is crucial for applications such as autonomous driving and urban digital twins |
| [Vernata: Self-Supervised Learning of LiDAR Point Representations](https://arxiv.org/abs/2608.06919)<br><sub>Oliver Lemke, Alexander Liniger, Abel Gawel et al.</sub> | IROS 2026<br>2026-08 | [⭐ 22](https://github.com/rai-opensource/vernata) | LiDAR serves as a primary sensing modality for robots operating in outdoor environments |
| [Towards Compact Autonomous Driving Perception with Balanced Learning and Multi-sensor Fusion](https://arxiv.org/abs/2606.02979)<br><sub>Oskar Natan, Jun Miura</sub> | arXiv<br>2026-06<br>📑 45 | [⭐ 9](https://github.com/oskarnatan/compact-perception) | We present a novel compact deep multi-task learning model to handle various autonomous driving perception tasks in one forward pass |

## Datasets & Benchmarks

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Towards All-Day Perception for Off-Road Driving: A Large-Scale Multispectral Dataset and Comprehensive Benchmark](https://arxiv.org/abs/2604.27499)<br><sub>Shuo Wang, Jilin Mei, Wenfei Guan et al.</sub> | RA-L 2026<br>2026-04 | [⭐ 6](https://github.com/wsnbws/IRON) | Off-road nighttime autonomous driving suffers from unreliable visible-light perception, making infrared modality crucial for accurate freespace detection |
| [123D: Unifying Multi-Modal Autonomous Driving Data at Scale](https://arxiv.org/abs/2605.08084)<br><sub>Daniel Dauner, Valentin Charraut, Bastian Berle et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 404](https://github.com/kesai-labs/py123d) | The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics |

## Safety, Robustness & Evaluation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [CCFM: Collision-Constrained Flow Matching for Safety-Critical Scenario Generation](https://arxiv.org/abs/2607.04451)<br><sub>Ke Li, Kaidi Liang, Yuxin Ding et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 3](https://github.com/KELISBU/CCFM) | Evaluation of autonomous vehicle (AV) planners in safety-critical closed-loop simulation is essential for real-world deployment |
| [Lipschitz Optimization for Formal Verification of Homographies](https://arxiv.org/abs/2605.23203)<br><sub>Jean-Guillaume Durand, Panagiotis Kouvaros, Maxime Gariel et al.</sub> | CVPR 2026<br>2026-05 | [⭐ 2](https://github.com/jeangud/homography-verification) | The adoption of vision neural networks in regulated industries requires formal robustness guarantees, especially in safety-critical domains such as healthcare, autonomous vehicles, and aerospace |
| [CADET: A Modular Platform for Evaluating Distributed Cooperative Autonomy in Connected Autonomous Vehicles](https://arxiv.org/abs/2606.04072)<br><sub>Pragya Sharma, Brian Wang, Mani Srivastava</sub> | ICRA 2026<br>2026-06<br>📑 1 | [⭐ 0](https://github.com/nesl/cadet) | Deep learning models are increasingly central to autonomous vehicle (AV) pipelines, yet their integration has traditionally followed a monolithic design where perception, planning, and control execute on a single onboard… |

## 🏢 Industry Tracker

Latest 14 days of news, official blog posts and new open-source repos from tracked companies. Full daily feed in [`daily/`](daily/).

<details><summary><b>Waymo</b> (232)</summary>

- 📝 2026-10-16 [Hello Toronto! Waymo is En Route](https://waymo.com/blog/2026/10/waymo-in-toronto) <sub>official blog</sub>
- 📰 2026-10-25 [Waymo Robotaxis Now Pick Up at the Las Vegas Airport—but Not Everyone Can Ride Yet](https://news.google.com/rss/articles/CBMisgFBVV95cUxPRkhtbzhqWVBjcFl1cEdFRk1rTkpMQ19paUxkNkZkbHM2WEpucGRwTWNLU3ctdFo0dFZGQXlPQ1R4THFxdmhoakRfbjdubnctRGQ0V1U5b1BNTWNwMi1xdlNmOVZnTW94cW1PbXcyVWw3UWJFQkpIZS1hanhOQmp0ZlJjMkxqNUtIWUxvZjhyRGF3d2NyTzIzaVBFMkdBVVFXMnV3dUJ3Q2ozNk1NT0diMHF3?oc=5) <sub>MotorBiscuit</sub>
- 📰 2026-10-24 [Tesla Robotaxi vs. Google Waymo: Who Has the Advantage in Autonomous Taxi Commercialization?](https://news.google.com/rss/articles/CBMi4gFBVV95cUxOWGpHYk1JM1BiTWNTS3lGU1VkX0F4a0RwUENxaHhqYklZUkNHY05IUnFPY2FfOFVGcDF5N0NiT0pfTGFxc0hLZ3lLd0JKdDF1c0xXb05CanRMUGpfWWdsb0tiWmVDODU4WDdENlgzdk1fMHVRdzdTMzdfalA0cmxkRlFTeExTVVd2MFlna09UUzR0N3RiRjBYcmwyQkNPOGRNVzlPV0lmdEd5X3BtR0trejlVc21DNm9pTl9vR1RnSC1jU1J4N1g3SmVaM0NmRFZEOXBvSW5KVVJzSVNaYWNiS09n?oc=5) <sub>TradingKey</sub>
- 📰 2026-10-24 [Waymo Wins the Airport Curb, Tesla Hits 75% FSD Take-Up: Grayson Brulte's Robotaxi Field Notes](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9KLUJMQlBlcUJtMW1HeGVUWWg1amE5dnExdHFkb1hkNDd6aG1HM3BXNndKN2Zka3llRWVKVTZxbUVRSWRGVkYxeUpocTRtZnJkRTZtMGRoYVVXcDQ?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-24 [If Tesla’s Robotaxi Miles Keep Compounding at 20% a Week, the Math Gets Interesting Fast](https://news.google.com/rss/articles/CBMiwAFBVV95cUxNMEY5ZjRvbXpGcVdWdWRaQlJKYlFlaHNfdUVvMU9SLU84RXM1NHZEcURDUC1VUEtNVkhZakQ4RXZGTlp5WTBOQnNYZWlZcFh5bFR4M0p4aDZISmMzYVRsQkNrOEM1d2VrMGhZbE0yNTNLbG1LcC1lUkJYMlFBQU9hdWNTaXBaTmJaM282bWRIY25tNnVUVE1QdE84NTg1Rk9nVnM5NHlzU0loOWtvQzQzVTYzM3hOaVZrRHFKdDllY3g?oc=5) <sub>CleanTechnica</sub>

</details>

<details><summary><b>Tesla</b> (350)</summary>

- 📰 2026-10-25 [Tesla Reshapes Its Website Around Robotaxi, Semi, and Roadster](https://news.google.com/rss/articles/CBMimwFBVV95cUxPTmdEN0RDNTdqOC1pNUp6UkZuNnZGMjNvQVBhb2w4RVU0QnljQWZWbGV1OGFQejVKYUR3cm8zRElTcFh4RVg0bjVPMzlCaUdfTW5SXzcyWDY3X1Z4a1dqQjdlcGVncHVuU2hsN1NaaVdYRXV4ek91aFo3bjJCazhzVXlzdDlmYVYtYVc4R3lZamFsOTFoWWJUdVV0WQ?oc=5) <sub>BASENOR - Tesla Accessories</sub>
- 📰 2026-10-25 [Vallejo Crash: Tesla Hardware Evidence at 70 mph [2026]](https://news.google.com/rss/articles/CBMiiwFBVV95cUxOdVl2NzdfZkpfMm5Fay1WTmljY21haDV5eTlJTUpLRUtzODVhWWJUcGZabUc4cFB2UkVObmZZdGd4NDZtbE5SeHphOHRoVVNxc2hUUGtWdExsUHhVLWdoWTdHMEhlM19NblV2T1p1YWc1NnJLT2V5YnVfTUtUMWtMdU5uRFVfb3hHVFJ3?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-10-25 [🇺🇸Tesla FSD saved a driver from an UNHINGED trucker. A reckless truck driver tried forcing a car into a concrete divider until self driving AI instantly dodged the crash. This is why we ride with Tesla. Worth every penny for safety alone. Writer: Bri https://t.co/Xp](https://news.google.com/rss/articles/CBMibEFVX3lxTE1RZjY5eWFMZlQydC1Ga205UnRHSVZac09MVjRFTUNLWThSUmpOT1RaQ0hXSi1MVndUZmJXMzhVLWFLMFNzdUVUMDdpQkZ0VTF1Y0ZwNW5sNjNNVUNWRmlmWXc5NlZuQTB4SjRRNA?oc=5) <sub>X</sub>
- 📰 2026-10-25 [FSD v14.3 Lite, Explained in 4 Points](https://news.google.com/rss/articles/CBMiakFVX3lxTE5VaVU4MkVScThJNG5Yd0E3dDNYRVdMdm1HbHRWWnB3Z2dYOVlkdlI0MGE0WHJSdUVCaDhTM2NURFJ1WGg3UXcyNXNhUGpVRUJVZ0xtQmdwNUY0NnRaSjN5dFl1UENDdy0xQnc?oc=5) <sub>BASENOR - Tesla Accessories</sub>
- 📰 2026-10-25 [陈茜体验无方向盘Cybercab，特斯拉FSD芯片方案量产前被砍](https://news.google.com/rss/articles/CBMic0FVX3lxTE5vMS03eWNwZl9PeGNZZU5JNlVfcXlrVFhCU1RwUlZDb2lXclV1VEw4c1ZPNi1qa3BHbW80N0ZUYUNoRmZ5aDNlMHRweDBVR2N5bk1Ea0FrRDNKSEhSMnpHT09lZExHTGJuQ0ZfdDVBNkFoRFU?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>NVIDIA</b> (253)</summary>

- 💻 2026-10-20 [NVIDIA/flare-local-inference](https://github.com/NVIDIA/flare-local-inference) <sub>GitHub</sub>
- 📰 2026-10-24 [Mercedes-Benz And Nvidia Are Taking Their Self-Driving Partnership To Level 4](https://news.google.com/rss/articles/CBMioAFBVV95cUxQSjdFbE5UNFJNYUluMnhDd0xoZm9WSWNZVXpZdHRPYzRYOXhicjdyZDBIUXZ4dWtoNVAxS1N4Y1V1akR1c2I3dVJ4SVBuLVRiM3BiMGFxNnRETW9UR2VyWklpWjFxUGNzejE0blhFYU44U1NVcmlHODRLbUVYUm9DNHZiS19jbkg0TVFRMzlBcEJMNENwOUE0RzJTcE5PTWtj?oc=5) <sub>Yahoo Autos</sub>
- 📰 2026-10-24 [NVIDIA Shader Cache Size: 13 Steps, 40 Min [2026]](https://news.google.com/rss/articles/CBMihgFBVV95cUxPR2RwQ3g5RG43MTk5U2w4Ymg1YzdCZTlpUlROSVVMRWwxLWg0UEQwaWhkNEthMGJhMkN1Q0FKMUZGRmhIU2xmS1FPbXFSMVJBQlFXTXItMVFvSHdCWGx3U0M3d2pJRldCUXY3QTd4VjNFSzE4d3phQW5iT3lKYU5iZldXSVJ1QQ?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-10-24 [NVIDIA Cosmos: 3 Powerful Wins for Smart Physical AI](https://news.google.com/rss/articles/CBMickFVX3lxTFB5cFo1cTVOeV95OEx0Rk1BOEsyeGtPMWxRREM0aWJOZmRlUW9oRENCODYxNlRhc3l1azE4bGUyby1EQnN1UTZ4aUsxNTZkMjVaZU9ESHdSM0xmNGloYmZ0X2dGMTlONWxFWDM1RDBmb2c2dw?oc=5) <sub>Global Brands Magazine</sub>
- 📰 2026-10-24 [NVIDIA has officially acknowledged the presence of a critical error in the GeForce 621.01 driver.](https://news.google.com/rss/articles/CBMitgFBVV95cUxQZEhTc18xTjJSVVBsY0Njb2RNamRwOXBoUzFGY3lGZzdJS3QxZXBOSmJrU1dBTlNfNVlMVmNndmMzYnFRT2VUYW1JY3BSaHJrUkNlcGJtUWlCUHhMS1FMQ2tPX08yR3dqVjlvdm9Mamo1cHUxS3p5UGVVeUVVLVlwZHNrXzVFLTFUaVNTMzBKYVl1dV9CbER2N2FuOVhHQWkxeVBrd1pvd2xiVkpTdVNlVlo1U0Nudw?oc=5) <sub>GameGPU</sub>

</details>

<details><summary><b>Wayve</b> (65)</summary>

- 📰 2026-10-24 [China's Baidu tests robotaxi on London streets, World News](https://news.google.com/rss/articles/CBMifEFVX3lxTE8tWW5taWpYWllPUkx0WVE1S2s3Y1B4UDEzTHliWWpDaWZfOFp5RklzejNuSEJBNXJSZ0h6UlV0R1E1QTJNVlZaTjQ3NFY0em9NalZOeHdaZzFrYjlFWG1CUnBESExUVV82d21fb1Z2UkhOTmw0SHVVeUVhYW8?oc=5) <sub>AsiaOne.com</sub>
- 📰 2026-10-24 [France Sets 2027 Autonomous Vehicle Approval Path as Stellantis, Wayve, Bolt and G7 Pitch Pilots](https://news.google.com/rss/articles/CBMizAFBVV95cUxNYV9LSWp4anNhM3l6bXVpcGN0algtUXFTcjdvRnZPT2ZyZU1kSEdNVGxHTUc0ZUdzWldsUHA0SjZXVVhfdHpPMVlITDFENldldDROcU1iMmxQeTFOVkJ4Q1FOYmFDdjhzck80ZllFd25fVGpGYUI5clVJenh5empMd3RiQzJVRHVXbFduTFRKcmNueU5VMG9oOE44eXJYRWh3TG9xbWJPTlJ0NTZ5aWh1d0xiVkVvSUpKS3dIajNfZ1BpczFsSjZ3bUliaE0?oc=5) <sub>AI Insider</sub>
- 📰 2026-10-23 [Wayve, Stellantis and Nvidia partner on autonomy in France](https://news.google.com/rss/articles/CBMimwFBVV95cUxNQzF0S1EwY0dYazEzclQxbmVpV0I2ZUF3TzRzRVhkb0NSeHpTeG5SUVNwWnRoOTBFRUt6X0lnMUc3WkJsbHBJNXU5UzhiZ3FVczNNYmRPRGg2VXREMzVFMzU3RzBRMTBnYXQ1bmNGaUNRczFVNmhoTzFLWnl0cjd4aVBtZmlkbU9nclhBWXlnczRQM3h4c3Vkck8wUQ?oc=5) <sub>Automotive World</sub>
- 📰 2026-10-23 [Stellantis teams up with Wayve and NVIDIA as France targets autonomous driving](https://news.google.com/rss/articles/CBMisAFBVV95cUxPZkpxbldocXFYdFlxd0NpNWJrbGU5bFVjbGh2bW1mY3BzQnBTeFdqeUhkVkh0bjRSbmZGQUJjTE9UYks2WUpPX1dZcVNtXzBxZGwtVDR1MTRaaFdFZGRvMnBRdUVkb3MxLUxPLXpEUmVRSE1mMkYxblhQbWNPT0pPRjc2YzNwZXZGMFBmQWE1RFhkSEZxNzlLaDNVQndqVHNRR2Z1QVZTVjUzM0d3T0dIdA?oc=5) <sub>ClubAlfa.it</sub>
- 📰 2026-10-23 [Uber rival inDrive eyes 2027 robotaxi tests in Central Asia with Pony.ai and Nvidia](https://news.google.com/rss/articles/CBMiugFBVV95cUxOaWhUal96SUMzM0RCbURnU0FPWnNfYzF2Qmtjc09PbjcwUmgzTmFyR1lyOHdtbUNFV0tuX3hMTzhIamtJTGk2cVBFeGI5dXJYOW04NERCU005LVp3NkdUMlVwSjVGYzJJcGZDTElfRVhfYjJYNnpPdmNVNjhlRUtHQ1hwbjZKc1NDNXc3cUdGbWtmNVJrRW1oR2d3SGtmemZfV0s0dmhVT2tqQWtQWHoySEN1SFpiYk5yUnc?oc=5) <sub>TechCrunch</sub>

</details>

<details><summary><b>Momenta</b> (106)</summary>

- 📰 2026-10-25 [12.99万元起售，东风风神L8+把700TOPS智驾与4挡电混带入1](https://news.google.com/rss/articles/CBMiWEFVX3lxTFAtVGQ0OFNobURSVF9jajhXc1kzZXprc1FlQWxzUll2YWNqbW5PQnctWEFYZkJFTWVhT2s2VFV4TXlZRzc4OGt6bGJoV3lKandOZldWTkZUaWE?oc=5) <sub>爱咖号</sub>
- 📰 2026-10-24 [13.99万起，配Momenta R7世界模型，但有几个人真的看懂了风神L8+](https://news.google.com/rss/articles/CBMiW0FVX3lxTFB4MFJHSV9WdDdWMHlTV001bXVXZm1kRXVuelFXcG94WmN0LThQNlhMZ1NhcnVzQk94d29nbTdPYlgtWlhSeVJDcDl6NE5SSzdUZmxyZXNBZDN5LXM?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-24 [家越07订单火爆 99.7%选装Momenta](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1mQWJmYUttaXl6cnYtY0R1b29Qd1JwZjk3UFhKQzNKYjZSNXJNTXZKdHcwWFd6WEZtUTBrYlE2d2RYLVdhREZiRFNkNVNsaGpJall4aHA1c2dQT00?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-24 [700TOPS算力配Momenta R7智驾 东风风神L8+上市12.99万起](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9DWUxpb0hwMmlzUVdla3l1d3BCM3pieWUyQ1VOVW9uVFp6dmJiTE1DWHl2NFh0cUh5UDlVV1BjTXYwTVFRQlF2dVZHd0hDUkllMjdKbVNGOG1UaTZDdnIw?oc=5) <sub>新车资讯</sub>
- 📰 2026-10-24 [【视频】豆包上车+综合续航1480km+Momenta智驾！15万以内家用SUV这么卷？](https://news.google.com/rss/articles/CBMia0FVX3lxTE1hNk9JMU1vdlNSQ2o2OHVMR081YTl0ZFNaekt2cVo1TFlLVVRfUGdzWXFJZU5PdDFxb2I0RUl2dlFodWdyOS1KQ1VjT1hMMDJLcmYzc2t4ZjNGVGR0amQteGNVY0NDVU0wNHUw?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>XPeng</b> (248)</summary>

- 📰 2026-10-25 [舱驾一体体验如何？小鹏G9L对比智界R7、理想L6等智能大五座SUV横评](https://news.google.com/rss/articles/CBMickFVX3lxTFBPYTRzSEJySUxONGgyM2NQeDVxQ0ZYdXl6YWVoeU9ReWtYR28zUWJuRm1GVGJ0c253MEZrSVZ6TU90Z3lTNnZKeXF4S2lsSGVnWVdmVVY2UlNRNU5Rc0lWa0h1UGo1TnB5c0hjSGd5OXl3QQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-25 [25万预算新能源SUV横评：小鹏G9L、理想L6、深蓝S09、乐道L80怎么选](https://news.google.com/rss/articles/CBMickFVX3lxTE5uOUhVQVUtbUlKWUZVY2J0SEJTc3FyNERXeU5hOE13a0F6MzBBMmdLSFQ3dUNyUEhlVS1fa281TWZYVEVWbHc0Q3B6RElUc082LVhhSUMxVGVMX1pxLUt3SWZFT1pQbHItOFNNclh0LTZhUQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-25 [智能大五座怎么选：小鹏G9L、智界R7、理想L6与问界M7智能体验横评](https://news.google.com/rss/articles/CBMickFVX3lxTE9DYk1KSnJBZmhLa2NkNDB0ODF4cDRUOVJuUmxqWncxU3JETm5KNE5FY3hlMVVaVU9sNGszdV9KMGlqTGZXWGt3Yk5TMmRvSFNYVDdwamJpbnVWSlI0N0RTdlN0ZGNFaW5oN05ZZ0Jra0I1UQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-25 [25万预算买新能源SUV怎么选：小鹏G9L、理想L6与问界M7横评+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFBDNnZWcDg0M3YwREJiYjRvYk1qeUpmT0h3TXBQWU1PYVdnU05Yei15RnctYi1fX2JCYl9GMjQ1ZjBlWjJoQ1lqQXdhSkJZUFZCV0RzWFdZd2xHbk5jMlpqSk1PdU9jTFVIdDRFNFd4MG5lUQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-25 [15万买电SUV，服务区充电小鹏L03省8分钟，值不值？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE55VFNMUFlHWUJnREZWYzZ3TzdQcmdCQmlBamVtZUEtSDhFV2lvdjBORUtjWVRVUFl6bzFfSEtJUkNiU2hKNnNoRnl5Ylg4TXpNeFVKWGtJUjlpcFU?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Li Auto</b> (155)</summary>

- 📰 2026-10-25 [舱驾一体体验如何？小鹏G9L对比智界R7、理想L6等智能大五座SUV横评](https://news.google.com/rss/articles/CBMickFVX3lxTFBPYTRzSEJySUxONGgyM2NQeDVxQ0ZYdXl6YWVoeU9ReWtYR28zUWJuRm1GVGJ0c253MEZrSVZ6TU90Z3lTNnZKeXF4S2lsSGVnWVdmVVY2UlNRNU5Rc0lWa0h1UGo1TnB5c0hjSGd5OXl3QQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-25 [理想i9武汉晚高峰挑战马赫VLA表现亮眼](https://news.google.com/rss/articles/CBMic0FVX3lxTE01MDBmekhHVVlkVEgtZEhKU1A4ZnlkVENHdXdPVmg0YzhTbTRhMGg0bDBhblk3V2VIbnZmZTNQVDBfQlh0ek1iNTBfaUR3S2djdU03TXJMdTl0aXVpT2lHU1dRanlNYUctRHFsQUVSZVNsaGc?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-25 [25万预算买新能源SUV怎么选：小鹏G9L、理想L6与问界M7横评+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFBDNnZWcDg0M3YwREJiYjRvYk1qeUpmT0h3TXBQWU1PYVdnU05Yei15RnctYi1fX2JCYl9GMjQ1ZjBlWjJoQ1lqQXdhSkJZUFZCV0RzWFdZd2xHbk5jMlpqSk1PdU9jTFVIdDRFNFd4MG5lUQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-24 [综合1602km与9分钟快充：小鹏G9L与理想L6、问界M7长途SUV横评+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFBzTkMtd2VPalkxVTN1cDBoNjdUYVlJSTduZ3dJLUtlNWtCaGZGWDhEQ3NJMzJMdVVuaU1RLVNTbGxpQmw2TVlEbmNNQW00UHJwUmZNcVFOODFvRmdDdHJRQ2t5RHdwN0c5MDlMVFFrZlB1dw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-24 [9月豪华SUV市场神仙打架：理想i9、问界M8与FREELANDER神行者8深度横评，谁才是真正的全场景王者？](https://news.google.com/rss/articles/CBMickFVX3lxTFBkLVQzX3RxX1BJSXE3MloyamJuWUFnc2RJdWVxZ3VGYUgzb2c2SHVJMW93ZF9BTWIzZ3loX1ZlWVBKYUlqTWxLbXYxVWJEM1Yzc2JMRFpCR19LT2QwUXk2QTJSSHFUd1g1WjJlVjRZYWRlZw?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>NIO</b> (163)</summary>

- 📰 2026-10-25 [【视频】北京情侣十一Vlog 蔚来ET5的真实试驾体验](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBtVjV4cHdOTzlDaFQySEtmd2dnVzVwRkZNY2gxN2hydmZSdlZOWFV3QlI0MWE2UUJ2c3Y5Y1h0d3dteWF6SV9NaW13dmJ0REc0RzVzT1dNVndBUTg?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-25 [舱驾一体体验如何？小鹏G9L对比智界R7、理想L6等智能大五座SUV横评](https://news.google.com/rss/articles/CBMickFVX3lxTFBPYTRzSEJySUxONGgyM2NQeDVxQ0ZYdXl6YWVoeU9ReWtYR28zUWJuRm1GVGJ0c253MEZrSVZ6TU90Z3lTNnZKeXF4S2lsSGVnWVdmVVY2UlNRNU5Rc0lWa0h1UGo1TnB5c0hjSGd5OXl3QQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-25 [【视频】无人区的老越野，现在换5年93000公里老电车去川西高原了](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1lQU9GemJlbE5nYmdwSEtwdlJIczFxd1VTRkZFeXhxTnlyRy1EUHl2SHdTYVJHeDc2MkJrZl82TEI2R3ZranRRdWo0cV8zOWV0U2dIa1pRZ2d0Mms?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-25 [舱驾一体重新定义智能SUV：小鹏G9L与4款热门大五座横评+选购清单](https://news.google.com/rss/articles/CBMickFVX3lxTFA5cGhDQWVaRWJWUzJNMW9qSnN2MFg3ZHNfbzJEZWVXUDI3OE5ET2NsRkJSZTdjS1RMTTZJbnd1bXVkaXgzV0QtVGl5RWVHVlE3OUZOa0p5ZE9BVmJkU3VreTk4QzgyaTZ6SU1fTE54eGlWQQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-24 [智驾怎么比 ，享界G9与蔚来ES9解析](https://news.google.com/rss/articles/CBMif0FVX3lxTE93c0lKRDRQU2RLdS1Eemk1d0x5QTZFcUI1c253b0hxdlZscTE5Q0JIUm5OX2d0dVhxc05wZUlPNmFqT0haajk4dElBMGJtOFFTYW13cjktMDdDNTNQT0JwZTF3Skh5SDliRWc4dGQ0anhjeVRuWldLRGMwdHFOVzg?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>Huawei</b> (355)</summary>

- 📰 2026-10-25 [舱驾一体重新定义智能SUV：小鹏G9L与4款热门大五座横评+选购清单](https://news.google.com/rss/articles/CBMickFVX3lxTFA5cGhDQWVaRWJWUzJNMW9qSnN2MFg3ZHNfbzJEZWVXUDI3OE5ET2NsRkJSZTdjS1RMTTZJbnd1bXVkaXgzV0QtVGl5RWVHVlE3OUZOa0p5ZE9BVmJkU3VreTk4QzgyaTZ6SU1fTE54eGlWQQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-25 [28.99万起标配华为ADS5与三把锁，神行者8如何重写豪华全地形SUV规则？](https://news.google.com/rss/articles/CBMickFVX3lxTE9OOVNETFJXd2N0VnNISXktUHBJSWJBejEtMGZMRExMc25LNjM2d2x3dUhYdXFtTkNyUFh1SnFibVRQLTVLbGF2emxsbFZUQjQ5Z1dXUUdRTk1GMkdFSmVRYWFMcWJPYnF3TjhiaXZEeS1kdw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-24 [同为华为乾崑，差价9万买的是什么](https://news.google.com/rss/articles/CBMiW0FVX3lxTE52M3c1ZXBHUFZOZ2JZZkJCUDVfU2QyWFBYeDRpaFBUYl9kMlFzbnM3OVVobTBlSkJpQVZtUk9MVU1kVnh1bVZtS09HTnVOUUFtSHZNSHNXcl9lM2s?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-24 [不做选择题：28.99万起，神行者8用全地形与智驾重新定义新豪华SUV](https://news.google.com/rss/articles/CBMickFVX3lxTE9HdG0zT1RLQzR2RnYtNHA5OEhOWU5DZk83R2VNUUJBWjZEYkw1cjBWMXBKNXZOVWs2RUJnLXVyM1RUQ1VuRjhjRFFyM2ROWVVGamJ0dTNvVEhIMlZrWnRoNS1SYVZJZjBFOTRtSFRqYkJmZw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-24 [第二届华为乾崑智驾公开赛10月31日开赛](https://news.google.com/rss/articles/CBMigAFBVV95cUxPcUhoWkxLYlpqNE03ZkU1ZmFDNUdwR2Y2N2d1LU8xTUxNanRtSGloME5LdnJnN085NXpNU0c1SkFOUjFCSjhCR09xUkh0MldONklRZU5nV1JXZ1N2ZUlJelFvYkk5SlEyM0ZVNF9TRGI1X29aYUd1ckM2U1FrYXhzbA?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>Baidu Apollo</b> (48)</summary>

- 📰 2026-10-24 [Baidu and Lyft Showcase London Robotaxi as 2027 Rides Remain a Target](https://news.google.com/rss/articles/CBMiWEFVX3lxTE1tcENqVlgweFRQQ2VFUmpkbm93ZktIVEFKX2VuaUVtTUVhSlk2TTY2MUgtTTlucUZnOGZ2N3B3bjEzZjBwMnVQcFBHWDcwaWE4TUVFMVRQU1c?oc=5) <sub>TOKENPOST</sub>
- 📰 2026-10-23 [Baidu Robotaxis in London: Driverless Rides Target 2027](https://news.google.com/rss/articles/CBMilwFBVV95cUxPYkhxcm5kcWJLWkZjclVGOS11dUlvMXdaM2dGNGhkZ2JYVkVJX0xKQW5KY0ZteEFhM1lhZ1U4eGNxaWhBN3RiRkxjWTdyMVJpNFBxQ3F1TFk3U3l1WFNsMVVrLUFGYXI5dXk1VDJxQllvUWpzcmpuM09FMEV0d1V5V0p0Y1FOSE1Dc3l0Wm1rTUZvakxJWkFJ0gGkAUFVX3lxTE9xcm9URHQ0RWlvdVZQTkR3NHc1U2FDd0cwU1hTd0xCQWRJZEZEQ1czZEVZT2U5NFdVNHg1OFJCZVBWN0xvVGRhWjVTQTAtVVB3VDFpQjA5cmV5ODNVbDBqQVBlbTFDbzZ0R3d1aDBMY0xhcE9NdWNiRmp0c2gtMDBFb0wyNHEwR0xZaXMwN0o1cU85ZGs3QjN1ZzdpQW9RU3BJdmt5?oc=5) <sub>Analytics Insight</sub>
- 📰 2026-10-23 [China's Baidu showcases robotaxi test vehicle in London](https://news.google.com/rss/articles/CBMirAFBVV95cUxPUDVibU56QktsNWRhVU1rQ1pKSUJpNGZNZUc2T2RRd0Rqb040RjIzR2Y3NjlFTFktU2dIRnBGb2pDdUFNbTgyVkdxRnc1Q0pPenVnQUstSmZwUU1BUzYzbFlOTUYtVHVJY3FWd1NnaXBmU1NCdmdVVGZqWlBmcFU5VFlQSi1ROE5Gb0NKLWc1bFNYNWhvWjNSeDQzS0NSOTZWUHEwcWo4eFNUOFZT?oc=5) <sub>marketscreener.com</sub>
- 📰 2026-10-23 [China's Baidu tests robotaxi on London streets](https://news.google.com/rss/articles/CBMimwFBVV95cUxOcUl6bGxJdkU1a3dZU1JRbmY1WWNfZ0RfV0V4LXhOTi1ZLUxpVFV1cjNFS1lHRTVsTkhmUTRpVHpKOHd4dXp1a25TazhJTXUwdFdWNWotNE9qRExzZmVmVnVnbnRmbGJJRV9SbU93UVhSdGxYUnpkX0pXYy11UVc3VGdrSW1XQjdqQTVVZHl0MFJGMVZtdlJzQVU5RQ?oc=5) <sub>Reuters</sub>
- 📰 2026-10-23 [L'azienda cinese Baidu testa i robotaxi per le strade di Londra](https://news.google.com/rss/articles/CBMieEFVX3lxTE9WbTJaT194WVQtajJsdk5OLXRMb1VOb1JCaDY0eG5VdVl1OEdIczdXTEFVOGxjXzdiZW5LSjhSR0JobzJBZUFXSm16NVB6V0RhUDZQcENUVXM2T29UcnZsbjFhS3JWWDVoSU1rNjB4dnBRWThJbEk3dw?oc=5) <sub>TradingView</sub>

</details>

<details><summary><b>Pony.ai</b> (147)</summary>

- 📰 2026-10-24 [inDrive taps Pony.ai and Nvidia to test robotaxis in one of the world's coldest capitals](https://news.google.com/rss/articles/CBMi7AFBVV95cUxPUW44ZW5nZWlNTE1sS0YwYnQzVWFlcEIzbmxOYmxZUTNlRm9Cc3p6emVUTl9STnZoYml3SzIwUWhqeExzUUtrWENXNWpudklSRlpVY2FDVVN6MW5BOURZUU45X0t1MFBub3czVEp1ZnRoYURUdHlXTXVXZFJacEEtRkxIa0pjV2lxQWhvMlByRDNRSkZOejhaQ21hMXJQamV3bXJwbjRkeUV5M0tDN1lpMWtmUTVfelhlYmFWWHZyVGRIOURNc3ZjbkJkUDJzelJCUl9nMDJKOHh5Y3hDeEJqWkFySnJUNnFaX0N6VdIB8gFBVV95cUxNcjRkZE5FdU4waFVTb2VLNlNHaVh5ejMtb2RJN2FXNVhWZUl6OWdQRW55aHphUnZ0b0ZPWTRXTWxuRXljOFpENER3SlZKT2loZllmdXVMMjF4REZjRUhWLWNubkZ4d1MwcmFjcGs3Tlc2UEFQYTBzcHlYOG5LUzdVdEZfQVFSZWxaUElwNVBZMF9rRmNCSWUxTE5fbjhpaUtudXByX1VkVkxKOE1Lck13Rml5OFpVYWViaHdPdGxmV09QRWlqZk8wRkNGSUhZRkNHTlFadWJ6dUxCRTlnM2ZzYWlMa3FWSW5IQ2UwaUo0RWgwZw?oc=5) <sub>The Economic Times</sub>
- 📰 2026-10-24 [inDrive Eyes 2027 Robotaxi Tests With Pony.ai and NVIDIA](https://news.google.com/rss/articles/CBMilAFBVV95cUxNWktyTk9mOXR4aWVRLVE2SFFqUlVxcTR1ekoxeFhGeDdOZVBrTjBNUjNzWUVsX2lHV2loRnlQLUVTU1UtNjNwVnF1OUtHQm1BRDZvWDBRNGZQN095bTZNNy00aUppOFJobGRZM2Y0dWdPQ0dHYzRncXdnaGVkZUFIZ0xzWGN0Ul9uWHM0VnpkN0NjMlJD0gGUAUFVX3lxTE1aS3JOT2Y5dHhpZVEtUTZIUWpSVXFxNHV6SjF4WEZ4N05lUGtOME1SM3NZRWxfaUdXaWhGeVAtRVNTVS02M3BWcXU5S0dCbUFENm9YMFE0ZlA3T3ltNk03LTRpSmk4UmhsZFkzZjR1Z09DR0djNGdxd2doZWRlQUhnTHNYY3RSX25YczRWemQ3Q2MyUkM?oc=5) <sub>CIOL</sub>
- 📰 2026-10-24 [10月24日热门中概股涨跌不一，台积电涨1.49%，阿里巴巴跌超2%](https://news.google.com/rss/articles/CBMiigFBVV95cUxPazc0d3hpc0NuLWF3ZUw1SE5zX0dBTmZycm40Y0tVcTFFM3BpUWlyX3BoMUhCM2dZSGprS2dMTm1KaFFBUUplOWQtdFVqQ0hwOHlVWU5wS3RydEhYUERac0xUOTdNbnVnd0xCLUJLUnFOclM2eW85N3g0T3EyLVFldk12WHZKd25BN0E?oc=5) <sub>新浪财经</sub>
- 📰 2026-10-24 [美股芯片股近全线上涨，英伟达重回“股王”，现货黄金再失守4000美元，国际油价大涨](https://news.google.com/rss/articles/CBMisANBVV95cUxOUXJRQmwwUklhUkdnNzJMbU0zOEJELUtuRzVRSk5ieG9iaE5DS2dycWpqLUg1Q1UxS3RMMmhOZDdMZ3JGaFNMV2ducmdpZzFiSWp4dUlZYVRPRVRMNUR5SzdLbVNXdlcweDd0UUxkeGMwQUczTkx2TE5iSFdMa2haMklpTmtXYkJiUmNRMVZZNE9INHhvSU90RXN5MFJfeEJuR3gyMFlaZ1VsX3AtLXJDZUs1YVdFYW5TTGQ0RGtKdnBsZDhheUdBU3czWm96RjNSSFFvR0psOS1kSFJPT0l0NFlyN3FvcHVLZ0gxSkQyVlg1Q3lHWGJyRTZxM0NoR2hVYU9KSGMyZk5sZ0gwenUyZ3BXTTZzdVNiT0UyWHVXdHRxNVlOMkduLWZQZDVPd0tHU1A4RWl4SV9WY05yd0swOHk2SVo5RE03cVVXeTJNOTlCbFZtdnZFcERzM1JBeVo0SmpPY0F5VHNZR2drRnEzNGQtSG0yNDgxODBoY3lYR0cwQWpOa1dQUDlOalNrOVBUMXBCWGpucEozdzJxc2hfOWkwY282RXdMQkxPV0tadl8?oc=5) <sub>finance.sina.com.cn</sub>
- 📰 2026-10-24 [泰伯早报\| 10月24日：太空算力首个基金即将发布；国产微型无人机再创吉尼斯世界纪录；OpenAI即将完成300亿美元融资](https://news.google.com/rss/articles/CBMiQkFVX3lxTE4wTXYxbTdZYXpyOXZyc2EtWUxVcGVRejNjRWN1MUZjUkU3V0pncy03ZG1ZM0Zfd2RCZkI0V1dpZVlVZw?oc=5) <sub>泰伯网</sub>

</details>

<details><summary><b>WeRide</b> (145)</summary>

- 📰 2026-10-24 [广汽埃安Ray7预售12.88万元起，首发华为DriveONE EMB全电线控制动](https://news.google.com/rss/articles/CBMiVEFVX3lxTE53MGZOWXFjdmh2dGc1eWoyeVNKTGk2aGFpWXBLa0pVMGJIbEg3Vm5PMVRyZXgxQUNIOWlnWUNzaGVnQU8wckpTbEZ0RGNVYm9Jal82SQ?oc=5) <sub>虎嗅</sub>
- 📰 2026-10-24 [【视频】官方套件变身，4小时让家用车秒变运动潮车](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBzRXJEeHBLZUVqSnFyZ2NWNHZ2QUpQNk5zOE9jZEFubGZuS01sTlBwRFJaajZ6REN3bm1CeGhDb2tuS0wzTXZJRVBkYVFyQ085dDl4OExETmg4MGs?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-24 [【视频】不用大刀阔斧，一套原厂运动套件，也能让埃安N60颜值升级](https://news.google.com/rss/articles/CBMiW0FVX3lxTE53SkhIN0EydUROUDlybTNzNUdlUld0ZWx1ZGhwY0I4T3hmZWVvR0ZFSmwyaEVEcFpIUV9yZTIzZXJka3BpYkU1eWZOb00xazdHRzFDU3gxZk5yX3M?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-24 [“老司机”搭i人出行？文远知行L4自动驾驶出租车广州小体验](https://news.google.com/rss/articles/CBMijAFBVV95cUxQazFZZ213QzBrX2U0X2RTOTB4LUJYcEF6NGtELVZRYnhjWURLck1HUWhvd1pqMzlBQUFHR2NtaEJmREdGU0hSaDVOWFF5UTFOUUVyOU5GLWRJdTNLTkE0QVQxS0tGRTRzMnQ2dFZVXy1MNEFka3h0MDRGRjV1Q1Z1cVY0WVQ1WG5keE9oNQ?oc=5) <sub>搜狐网</sub>
- 📰 2026-10-24 [从2026 WICV演讲看：文远、元戎、智驾新程把智驾的下一轮押在哪？](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1UMzkyZlFUZFdhS3l3M1dPYVAxemFzYjRHSFlnWjJUbEVzaDgzRF96VUJiUFhPWTlNdG95czM4NXg1Y0ZlY1JiY2VyV1YxcFZxblpv?oc=5) <sub>电子工程专辑</sub>

</details>

<details><summary><b>Horizon Robotics</b> (149)</summary>

- 📰 2026-10-24 [10万级城区NOA激战正酣，智驾供应商却盯上了另一张船票](https://news.google.com/rss/articles/CBMiU0FVX3lxTE94T0xKVFV5XzZlS1Q2RFUtWTFCWTZTTXdVOG8ydGlCa3ZEc1hDUERjbEh0Vy1oVFUxZENaTVc5WWVZbDZXb1NDZkpfc05kWElMMmlV?oc=5) <sub>电子工程专辑</sub>
- 📰 2026-10-24 [Volkswagen’s Two New China Models Pull Orders as Group Sales Sink 39%](https://news.google.com/rss/articles/CBMiuAFBVV95cUxPd0liYkhPMUxyY19NV0tOWFRyZ2FiQXFnZzFER0dueEVPcGY5a2tHTXdmTHF2cktyODdKUHB5bVhOYTAyYlg0MUxRMVdiR1dPa1h4bXVQUFdxallla2FlSjFSazhvZm9zNkRROEpaeUkxcFd6YzBNbWhhTjQ3dy0weFJ1dzlOX2M5M29OSEE1ZnI5SXczX05aejl1S3BYZzkyV3owT3NQV19xa2Fja3FvbWkxLW93Q2Jt?oc=5) <sub>Electric Vehicles</sub>
- 📰 2026-10-24 [Volkswagen’s 11,900 USD Jetta M6 EV is a hit in China, gets 10,000 orders in 19 hours](https://news.google.com/rss/articles/CBMirAFBVV95cUxORk5NSWxzRWJycERidks4TGd3T05NZ01LWnFYZFQ3a3lyNUJ0dEVxeDdKRXVQZWxOQTFjUld6QV82MmlScVlBUmJjbnNqYnMyOWJoZnNoSElDNlk2VkV2a05PQ0dDaEk5RW9hWS1QdzNtUFNSSDlSdDRySkJHTVhJTnJoUFBOLW1MWFRRbnNPbFZVYkJaVll5UEJlNDJkd1Z1a1ZjcG02ajcxYlg2?oc=5) <sub>CarNewsChina.com</sub>
- 📰 2026-10-24 [VW ID. UNYX 09 undercuts Xiaomi SU7 by 40,000 CNY at list price](https://news.google.com/rss/articles/CBMinAFBVV95cUxPWDdBb1g1U1ZmclhqZ2pPS2FWVHEyN3ZLVTdMOXRhYjBYMWdSd093TV9Mdmx1bW1CQlpFa1RKV25pLTMtNFhUcFNhQ2p3UTg0SkkyNHk5V1BTVUE4MGktSVN0TWNMbVRGN2dBS3FjQTlVTDQtWnptYnZPanVIZXdjanAtV3h4N3U3UXIwSUM3RVFmVm5uOW5GNVl0eHk?oc=5) <sub>GlobalChinaEV</sub>
- 📰 2026-10-24 [三款合资纯电SUV高速NOA实测：15万级德系智驾凭什么领跑？](https://news.google.com/rss/articles/CBMickFVX3lxTE1mdEZRa2Z3VTVPVFotVVlkWHZwZFBpS1V5bjUtQ1ppY3NBVWQ3UGx6d2pnOUFtcXVfb1lWTWllRE1aWlM0dzFsMmhoYWtwVXVuY3VIUmNwQm95Qk9nanlyMm5QMzhQWTYzX1UtdllFdThFUQ?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (37)</summary>

- 📰 2026-10-24 [从2026 WICV演讲看：文远、元戎、智驾新程把智驾的下一轮押在哪？](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1UMzkyZlFUZFdhS3l3M1dPYVAxemFzYjRHSFlnWjJUbEVzaDgzRF96VUJiUFhPWTlNdG95czM4NXg1Y0ZlY1JiY2VyV1YxcFZxblpv?oc=5) <sub>电子工程专辑</sub>
- 📰 2026-10-24 [欧拉5城市NOA值得买吗？11.58万带激光雷达，3个维度说清+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE9tdVFPMXpMMGg5UlpDNGt2RzJIMVJ5Slk4dG5SVGJxM0dqaENiNHhVWi1TSWFYTXFuc3VvMXdJMFdHOEY4cUNOcF9peENCbmxFVlVxcDRIMUlUdVdpaTYyWGpaZGY2Q2F1UGxTM1lVU0Zkdw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-24 [4款7系SUV扎堆上市，问界M7车长5080mm](https://news.google.com/rss/articles/CBMiW0FVX3lxTE14Njc1UEhVa2JDUjZldVh5cm9SaHl2bTB4dE5fQnVEbEpuUE1UTzJQS0dXOU50UjVYYm9IeGwyVFIzQ085QktXaFBvaExySzQ5VFROUnoyY2hCT0U?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-23 [元戎启行周光：基座模型成自动驾驶新引擎，推动MPCI向千公里级跃迁](https://news.google.com/rss/articles/CBMiXkFVX3lxTE9wRGVmQ3liVG9hUjNic1QyekVrS3VKVUNZbFJ5WHc2dlR3UHQzdGhCRFVROHVnTl9NLVdENGZIM2hUT1doV01USEtvSHJsaV9iclpoWEd4M1hfVDZFMFE?oc=5) <sub>SmartHey</sub>
- 📰 2026-10-23 [US: Waymo Launches Services to Harry Reid International Airport](https://news.google.com/rss/articles/CBMinAFBVV95cUxOV2M2dkZzWEw4TXdrbU1kMzlPelNRbk5FQU5YbTY1MUNoRUdITmY0a1dzSUZjWE9JdXotNkI5Mkg5RzZQMlZORlM0OUppSVNlc0llbVFMa1NJNHpzLWhEbkl5RC1wSnZsUFNoVDJyUlgxa19OTWVGRFBvMHBIbDlYZllzV3NQMjMwMklTSWp6NWZqaDVuZndFUnpjckg?oc=5) <sub>Future Transport-News</sub>

</details>

<details><summary><b>Mobileye</b> (21)</summary>

- 📰 2026-10-23 [Mobileye Sinks 5% While BlackBerry Rises 3%: Is Wall Street Choosing Car Software Over Chips?](https://news.google.com/rss/articles/CBMizgFBVV95cUxQbm9SLTUwcmItY2g1d05SYU04Nld6NDB5ekhDcVB1a3pyYlZqVWRNN19VNEZYalhiX08xTUo5bnF6Nk41OHpNNWdBUFI0YkRIX3N3ZWxCMWVOUFB5Si1SQVJpa2JFSTBjMVhEWkFLNmFXMm9waC1Xc3QyVXREb1g4UEJFRFhWaVhwb0w3dGxpUGhTdG5pVk9FeW0zVmJQTmxCZjVPclEyS3J1Tm96T3lvSmN6MFl1eHo3aHV5cVc3NlF2TmVxZzE2c0tNOWE5dw?oc=5) <sub>24/7 Wall St.</sub>
- 📰 2026-10-22 [Mobileye secures first TÜV SÜD certificate for ADAS work](https://news.google.com/rss/articles/CBMimgFBVV95cUxQM2E4elBaalF6Um9lajNMQTEyUmpaYW0zbTVMV1BNR0hlUTlIMkpyUWNoaXlHM3JWblBwSUhiNGRJTTgxVDFYOWROWW43TW1qZlZQeDhXaFY4TmJ6VE9vRi11SGcwQjg4WHpPM2g0Q0YxUGFBdmhMcTFtbEFWaTZqdmh0dkloM2RYMS1GdVVlblpSX0hTbVdMRG1R?oc=5) <sub>Automotive World</sub>
- 📰 2026-10-22 [Mobileye Achieves First TÜV SÜD Inspection Certificate for ADAS Development](https://news.google.com/rss/articles/CBMiygFBVV95cUxOTHZRQjV1cnA1T01OSC0yZ1Z5TmtOVy0zRHhtNGcwTmw2NGhoeVJsR1BhbVpEbnFLeGtYMkxubGFpVUxIelFVZlNBcVlMUlFwT0NMdE5TM3JVTnhpcW9HekxZUVdOOXFYY3otb3ZTd1FRU0hISlIxb3g0eURSME11dlFxUUtTdFlGNlZkS0RIekZSeGQ1WW1rRjdNbVI3VUZ5RUs1RXpid3B1WV90MS1LQzc1aXBpZ0VzRXB3V2J0eGJ5dFUtQnhWNVlB?oc=5) <sub>Business Wire</sub>
- 📰 2026-10-21 [Intel Banks $150M Paper Gain As Joby And Mobileye Rally In Q2](https://news.google.com/rss/articles/CBMiywFBVV95cUxOZVNKbmU1VlRTYVdUcExFLTRvdXhPLWJ5MkJyUFVMT3RMMlFvWjI5ejFPVjBfVFlET0p3RG04enRyd09pMHdpLWFZME94OXFoNHdFdFBJbXNMekRhR3pfcGstVmRWMTBEcHViMDdBaWxSLVRPNHhNUlZLYkRlcE1xM1BoS1NIWmpQUk9zQy1oUm5Fd1BOUWkyQkpGQnF5YUltUDAwS0tEYnJ0c2hkNVg5ZWFGalpxTTU4V3JyU3ZVc3MtazFJeXdkVnhHNA?oc=5) <sub>Stocktwits</sub>
- 📰 2026-10-21 [Mobileye cut to Underperform at RBC Capital on ADAS displacement risk](https://news.google.com/rss/articles/CBMiuwFBVV95cUxQbGV2OURKazdBc0c3ZlkwTDg1aDBENU5uN0ozYXRaQTBzWnNyX2hEWjI5Tm9FSDkybXBsVHFnNjJHaW9OaGg0NUsxY3Qzd2dKRUx4eUhBSW5EU242VVEwV3lKU3k3ZkpGUFpYTzdVNnhXQjVzU29YTVdCYndDOElCQkNVd2l6RzdkQ1ZyMHhsc19TQVJVS29kSmtoaGFfZkhxWkZMWEczLTlvSk1Ga2pwUWdBLTgxd1BnUmE0?oc=5) <sub>TipRanks</sub>

</details>

<details><summary><b>Aurora</b> (51)</summary>

- 📰 2026-10-24 [Some US transit systems weigh whether to run trains without a human at the controls](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNUk11OVZhb1dSNnVBMkFpcjg5bjV4VkdBbXhmS05mRmtXd2xBaG04QjFLZEJidXl3NVVvcXdNd2VNaFQ4TTNpTUo4dnQ5SFdyUGRrVkEyUE90SkY5b1NTQWFKdE5KbWVpdzRRdF8xRWExZk5JZ05zYXo0WENfcnZJa3lMT3gzY1hM?oc=5) <sub>Yahoo! Finance Canada</sub>
- 📰 2026-10-23 [Driverless Trucks Log 1,200 Miles, Observer Returns [2026]](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQcG1PcHdpRkFhcENGLUpkbTl2LTNWdGRKdFVfbmJBYV9TMFhHMDJzTlZDTDh3aFh6bnYzS1d3YlJmS01DRVc1NGpLNTBseVZqS05LSDBBX2tsNlhsN3Jid3dGNTRxeFAyNVVJQzBxYmkyaExDSXlfaXZWbE0tQi1ZYXdMOWVxUFFqT2dz?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-10-23 [Self-Driving Trucks on I-45: 240-Mile Route [2026]](https://news.google.com/rss/articles/CBMihwFBVV95cUxPaDFqOGxqUlRHZEFfNVJCMGdJUndhZm1EbldJaWJxamRFbkt0TE94blF3U2ZTMUJFbkxSZWtFNHBqUEhab2daeHZwSFVsVFZFeWNtV0M0elEySk1sMTdTbk9VNzI1dFk3OEgyLWg2dFBIenVwNGFkSzMzaklnYXhfa19TUjdsM2M?oc=5) <sub>shattered.io</sub>
- 📰 2026-10-23 [Self-Driving Big Rigs on I-45: 650-Ft Pole Spacing [2026]](https://news.google.com/rss/articles/CBMihwFBVV95cUxPaDFqOGxqUlRHZEFfNVJCMGdJUndhZm1EbldJaWJxamRFbkt0TE94blF3U2ZTMUJFbkxSZWtFNHBqUEhab2daeHZwSFVsVFZFeWNtV0M0elEySk1sMTdTbk9VNzI1dFk3OEgyLWg2dFBIenVwNGFkSzMzaklnYXhfa19TUjdsM2M?oc=5) <sub>shattered.io</sub>
- 📰 2026-10-23 [Einride Puts Nvidia’s 32B Alpamayo AI in Trucks [2026]](https://news.google.com/rss/articles/CBMickFVX3lxTE9qWk10YmdBcWlpOUJBVHZXQ2tVYUNaUEN5ZDQ3bmRWczN4bGk4ek1FUnlVX0NoQ2V6UUVSUDBzQVY0Uk5sUzZxOE14dUhHWDZXUzU5MWk3Vm9oWGpaTTRyMWZpVDZheUlfNy1pVDRqcm5oQQ?oc=5) <sub>shattered.io</sub>

</details>

<details><summary><b>Zoox</b> (62)</summary>

- 📰 2026-10-25 [Waymo Robotaxis Now Pick Up at the Las Vegas Airport—but Not Everyone Can Ride Yet](https://news.google.com/rss/articles/CBMisgFBVV95cUxPRkhtbzhqWVBjcFl1cEdFRk1rTkpMQ19paUxkNkZkbHM2WEpucGRwTWNLU3ctdFo0dFZGQXlPQ1R4THFxdmhoakRfbjdubnctRGQ0V1U5b1BNTWNwMi1xdlNmOVZnTW94cW1PbXcyVWw3UWJFQkpIZS1hanhOQmp0ZlJjMkxqNUtIWUxvZjhyRGF3d2NyTzIzaVBFMkdBVVFXMnV3dUJ3Q2ozNk1NT0diMHF3?oc=5) <sub>MotorBiscuit</sub>
- 📰 2026-10-24 [Robotaxis May Soon Need Cyan Lights to Tell People Who Is Driving](https://news.google.com/rss/articles/CBMidEFVX3lxTE80V1UzRmd3bzB5THZLc2doaVN4SHV2VzVZWmVzM0hfbmFtaWhnSU9CQnZoUnFFZG9ZR2lpRDNNZUZnWkRUcjNidFl0UFJZTHZwNU9IY0xUQlNPRkpTbmZ5UHFvLWRORXlIcE4zSHE0RUdtN1FX?oc=5) <sub>WeRSM</sub>
- 📰 2026-10-24 [Waymo Wins the Airport Curb, Tesla Hits 75% FSD Take-Up: Grayson Brulte's Robotaxi Field Notes](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9KLUJMQlBlcUJtMW1HeGVUWWg1amE5dnExdHFkb1hkNDd6aG1HM3BXNndKN2Zka3llRWVKVTZxbUVRSWRGVkYxeUpocTRtZnJkRTZtMGRoYVVXcDQ?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-23 [Mark Cuban-backed FORT Robotics secures more funding ahead of public debut](https://news.google.com/rss/articles/CBMi0wFBVV95cUxOOXNOUERmcEFvR0V0NnNhRmJNNUlPR19WZndLMlNfal85X29qYlZ1cXMtZTJTUWc5b09IemI1TW9ZbHpkODRyZWN6M1BMek5SaUZybzk5VnYySDd2UHlhX2I2dmg1b0l2a0ttZmtDeGZtRkY4eU53SVpUWGltNmlvZHp2UldYMkVDSjZpOGFidEFvanY1MDV2TXhtMUI4cldMSjIyT3lQLWhOLUdUb2RvWWxuNVFoNmxRUlMyUl9fWGVmS3B5RFl2aDVlQWo1WUZsXzlR?oc=5) <sub>TradingView</sub>
- 📰 2026-10-23 [New Report Explores Waymo's Impact on LA Uber, Lyft Drivers](https://news.google.com/rss/articles/CBMiqAFBVV95cUxQSDJXRUQ1cVdMMlNWUEl6VkI2UkRvRk1GU09NUVlyd2lydWZQMGp1Sk5NRTJKMThNaTlaX2RsN0hJMlVwQ2tZOGdEcjJZdWRFU2dUbnZiWmxQTVAzekJWNWRZcEgteXBhUm8zZ2Qzb3AxS3VZN3RTNWpaa1ZUSS1tZmZEcXpIb2hhX0N5aHFIWUI3WFZ5R2g5M2Rzb29yaUhCeWpHUmp6Vy0?oc=5) <sub>KFI AM 640</sub>

</details>

<details><summary><b>Motional</b> (13)</summary>

- 📰 2026-10-23 [Waymo Is Accelerating Robotaxi Deployments. Who's Trying to Stop It?｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE83QXNrSG5UMnZyN2ltY3BENUtsUVBVVk4zbnpNTVNCTENELTBYZjVpY0NqMnFRUFYzVmdMSWdzVWswU1NZWHBRSkd1N3E1WnZxbUVaZ2tneWlmQWU0dTVZ?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-22 [Zoox Las Vegas Airport Field Report｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBuM3U0cTFKZHF4ZjhlSVhzY1k4dlVoMDhWVy1PaWUtcUJKWF9jeEtEczdXbm0zbjhTUXBiVFBpdWplUm1NNHBTbndsdzM5TTZYM1ZJSjVJNXBQM09iRkJJ?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-21 [XPENG Next Generation Pilot (NGP) Field Report｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE4xUFBoMW5mRlRQenVJWmVBMHhyMU5HV3VGQXBzQVhYMXVPXzhKeEhRY2Q0d1pKZ2hTcm81X0pSMF8yUGRwYzE3QlVVRko4YUlNNUhncUNzbTZhSkVveTBF?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-21 [EU Regulators Open Probe Into Booking.com Over Fake Listings and Phishing Scams](https://news.google.com/rss/articles/CBMidkFVX3lxTE1Rd2lBWTFiT2s0UG55ZzNOS2NlQ1JOQkVPX3hwSEhRQ2tTa0ZpS19telVJUmRSclZnZXlBSEF3eURRcnNTUDFIaVZ3VG1rcUFXc1cwOVRiU2hIMnFDY0pGTVVVcTZ6U1Fhc2JVSU9xdkI0eTRiX1E?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-21 [Taiwan Blocks Grab's $600 Million Foodpanda Deal, Citing Uber Ties](https://news.google.com/rss/articles/CBMidkFVX3lxTE9sZHZrRlE3bFZXdlJoUEg5azRoMTJiUnVyLVNKWmNaYVgyeDdGZVJ1bEFTN196cEhuaTFJVFVhVW5fdG5aanN6d0s3MmJmVFQ5Nms3OTBCek1IS09nSkFfLUdTV0pDMkR0TlZTNlltWUQtM1k1V1E?oc=5) <sub>BigGo Finance</sub>

</details>

<details><summary><b>comma.ai</b> (6)</summary>

- 📝 2026-10-23 [openpilot 0.11.2](https://blog.comma.ai/0112release/) <sub>official blog</sub>
- 📰 2026-10-21 [Is the race to build self-driving AI turning into a cyberwar?](https://news.google.com/rss/articles/CBMikAFBVV95cUxPd1ljS1V3ZmI4RGdJZkRQdVpkNmRqcm5tVUtpRllXYWMyQ2ZnaFFKRzgzY0VaUDNTR3VwYV9lRHI2RnRUcV9za0p3bTNsMGJmSHNZUlR0MDFsYm1FLTVtUEl1UEJhSi1hXzMtc05tendPaDltRzlMczQwRkx0dTZJaGVjTk1DOXp1cVpSS2Zqc0w?oc=5) <sub>Yahoo Tech</sub>
- 📰 2026-10-21 [SquachWatch Turns ESP32 CYD Into Standalone Privacy Scanner](https://news.google.com/rss/articles/CBMikgFBVV95cUxQT3EzRFl0MWRwUm1tYklBYngwR0lDVGswYUJ5TUdQNjdPdkJLajV0bklVU2FCWFdMUlJjMng5NEc2ejQyUV9MeHB4RjF2UlRxQ1pUdFpSTWlETVU4WmFxTVpLTmJ3Z0NPX3ZnWEc2M09VcDZRNmtlUDlBZU5hQmFrUlNWOHBCRGtZQWs1Z3Z4TlVBQQ?oc=5) <sub>news.lavx.hu</sub>
- 📰 2026-10-21 [IQ.Lvbs claims hack attempt traced to rival Comma.ai IP address](https://news.google.com/rss/articles/CBMilwFBVV95cUxNVXdkQWthMXBaOUd3aGV2Nl9Kb28ydFVOcElQcTUwRnEyWVF4NTVzOWd4d2hDSlFFbjc3Y2hranNuOUtSS2dha2NKYzRvUkxzSlJxSGhQZTI0MEVySU9UOVpjUlVSUEpPTl9LcWhhNWJzLXdQaEhNMnRCZUVGd0dDTEZFYzdhcTdsQWNkczU1X0UtWTdJbXdN?oc=5) <sub>news.lavx.hu</sub>
- 📰 2026-10-20 [Auto tech startup claims it traced hack attempt back to rival's IP address](https://news.google.com/rss/articles/CBMizAFBVV95cUxOVHlZN1E1cDJqNEFHSFg3U1hCbnZRdFhtdk11blVLd2d2dUNIVkYxUG1xd0NIWjdNZGNVMHJvalh4SEM2cTJhclMzWHRyR0thRWJDMHFNUWcwNHAza21ybFYxV1Zyd2ZoaHRORmRtdGxBbWlSWk1UUnllQVp2dGFCVlFjcE0yOG1OaW9hdGhRb0lpS25LeUZFc2pKem5QaGVnZ0pLNExzeDdUOGNERVM2andndkh4LW5JWDdaSGhqQmZxOFMtb283aDFIWkE?oc=5) <sub>The Register</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
