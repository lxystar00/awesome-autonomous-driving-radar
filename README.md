# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-10-21 · 1,300 papers tracked · 42 curated.

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
| [SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving](https://arxiv.org/abs/2610.20609)<br><sub>Shaoyuan Xie, Zihan Zhang, Jingxuan Wang et al.</sub> | CoRL 2026<br>2026-10 | [⭐ 25](https://github.com/ASGuard-UCI/safedrive-vla) | Vision-Language-Action (VLA) models are gaining attention in autonomous driving, inheriting commonsense priors from large language models (LLMs) and widening the navigation interface from a fixed command set to free-form… |
| [Scene-Adaptive VLA: Efficient Autonomous Driving via Dynamic Layer Routing](https://arxiv.org/abs/2610.24590)<br><sub>Yujia Yang, Quan Yuan, Jiawei Fan et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 0](https://github.com/yang-luvu/Scene-Adaptive-VLA) | Vision-Language-Action (VLA) models offer a promising paradigm for autonomous driving |
| [CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving](https://arxiv.org/abs/2607.04179)<br><sub>Zhaohong Liu, Hao Ye, Xianlin Zhang et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 1](https://github.com/MICLAB-BUPT/CritiqueDriveVLM) | End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving |
| [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)<br><sub>Nan Yang, Zhanwen Liu, Linfeng Zhang et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 11](https://github.com/Zizzzzzzz/MVPruner) | Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings |
| [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)<br><sub>Yuan Gao, Wenting Miao, Mattia Piccinini et al.</sub> | IROS<br>2026-07<br>📑 1 | [⭐ 28](https://github.com/TUM-AVS/Chat2scenic) | Validating autonomous driving systems requires diverse, regulation-compliant test scenarios |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 11 | [⭐ 517](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
| [Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air](https://arxiv.org/abs/2605.31066)<br><sub>Tianle Zeng, Yanci Wen, Xueang Yu et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 1,116](https://github.com/louiszengCN/CarlaAir) | Recent aerial vision-language-action (VLA) models show promising single-UAV capabilities, such as tracking moving objects and navigating to language-specified landmarks |
| [GRAVA: Grounded Reasoning-to-Action Representation and Learning for Autonomous Driving](https://arxiv.org/abs/2609.15169)<br><sub>Xiao Liu, Haoyu Li, Jianghao Leng et al.</sub> | arXiv<br>2026-09 | [⭐ 262](https://github.com/AhernResearch/grava) | Driving vision-language-action (VLA) models increasingly reason before acting, but their intermediate reasoning is often weakly grounded in physical scene evidence and loosely connected to executable behavior |

## World Models & Generative Simulation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [HERMES++: Toward a Unified Driving World Model for 3D Scene Understanding and Generation](https://arxiv.org/abs/2604.28196)<br><sub>Xin Zhou, Dingkang Liang, Xiwu Chen et al.</sub> | ICCV 2025<br>2026-04<br>📑 4 | [⭐ 72](https://github.com/H-EmbodVis/HERMESV2) | Driving world models serve as a pivotal technology for autonomous driving by simulating environmental dynamics |
| [FrozenDrive: Zero-Shot Text-Guided Driving Scene Generation and Data Augmentation with Parameter-Free Frozen Diffusion Model](https://arxiv.org/abs/2606.20110)<br><sub>Yuhwan Jeong, Hyeonseong Kim, Daehyun We et al.</sub> | ECCV 2026<br>2026-06<br>📑 1 | [⭐ 10](https://github.com/daehyunwe/FrozenDrive) | Synthetic data for autonomous driving is surging, powered by diffusion models that promise scalable scene generation |
| [MESSENGER: Memory-Enhanced Sequential Scene Flow Estimation via Autoregressive Next-Frame Forecasting](https://arxiv.org/abs/2610.10759)<br><sub>Jiuming Liu, Jianing Li, Mengmeng Liu et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 0](https://github.com/liujiuming123/Messenger) | Scene flow can capture low-level 3D motion displacements in dynamic scenarios |
| [ASTAD: Asymmetric Style Transfer for Synthetic-to-Real Adaptation in Autonomous Driving](https://arxiv.org/abs/2606.29286)<br><sub>Dingyi Yao, Xinqi Zhang, Lihui Peng et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 1](https://github.com/Dingyi-Yao/ASTAD) | Synthetic data mitigates the data scarcity problem in autonomous driving perception |
| [Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends](https://arxiv.org/abs/2606.01164)<br><sub>Jiuming Liu, Chaojun Ni, Mengmeng Liu et al.</sub> | arXiv<br>2026-06<br>📑 7 | [⭐ 244](https://github.com/liujiuming123/Awesome-Interactive-World-Model) | With rapid development of large language models and diffusion-based content generation, world modeling has attracted increasing research attention, benefiting various downstream domains such as game engines, embodied AI,… |
| [Is Your Driving World Model an All-Around Player?](https://arxiv.org/abs/2605.10858)<br><sub>Lingdong Kong, Ao Liang, Tianyi Yan et al.</sub> | arXiv<br>2026-05<br>📑 6 | [⭐ 256](https://github.com/worldbench/WorldLens) | Today's driving world models can generate remarkably realistic dash-cam videos, yet no single model excels universally |

## End-to-End Driving & Planning

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](https://arxiv.org/abs/2609.26792)<br><sub>Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.</sub> | CoRL 2026<br>2026-09<br>📑 1 | [⭐ 13](https://github.com/VAIL-UCLA/DreamStream) | Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions |
| [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)<br><sub>Shen Zheng, Anurag Ghosh, Gaurav Parmar et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 32](https://github.com/ShenZheng2000/WarpI2I) | Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs) |
| [G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance](https://arxiv.org/abs/2606.26017)<br><sub>Hang Yu, Ye Jin, Alessandro Canevaro et al.</sub> | IROS 2026<br>2026-06<br>📑 5 | [⭐ 6](https://github.com/HangYuu/G2DP) | In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 17 | [⭐ 347](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
| [SimWAM: A Simple World Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.07468)<br><sub>Zongchuang Zhao, Xin Zhou, Tianyang Xu et al.</sub> | arXiv<br>2026-08<br>📑 9 | [⭐ 197](https://github.com/H-EmbodVis/SimWAM) | In autonomous driving, World-Action Models (WAMs) have improved end-to-end planning by transferring video dynamics priors to action prediction, but many still couple planning with future-video generation at inference, in… |
| [Latent-Centroid Steering: Single-Pass Classifier-Free Guidance for Command-Aligned Autonomous Driving](https://arxiv.org/abs/2608.00237)<br><sub>Meibo Hu, Jiamian Wang, Pichao Wang et al.</sub> | IROS 2026<br>2026-08 | [⭐ 2](https://github.com/codingmlinprocess/LCS) | Vision-language models (VLMs) have recently emerged as a promising paradigm for end-to-end autonomous driving, enabling agents to map multimodal inputs and high-level navigation instructions directly to executable trajec… |
| [DVGT-2: Vision-Geometry-Action Model for Autonomous Driving at Scale](https://arxiv.org/abs/2604.00813)<br><sub>Sicheng Zuo, Zixun Xie, Wenzhao Zheng et al.</sub> | arXiv<br>2026-04<br>📑 15 | [⭐ 367](https://github.com/wzzheng/DVGT) | End-to-end autonomous driving has evolved from the conventional paradigm based on sparse perception into vision-language-action (VLA) models, which focus on learning language descriptions as an auxiliary task to facilita… |
| [STAGE: STyle-controllable Action GEneration for personalized autonomous driving](https://arxiv.org/abs/2607.29517)<br><sub>Zihao Liu, Xing Liu, Yizhai Zhang et al.</sub> | RA-L<br>2026-07<br>📑 1 | [⭐ 6](https://github.com/CarlDegio/STAGE) | Driving style refers to the behavioral preferences that drivers maintain during driving, shaped by their diverse experiences, habits, and needs, and is typically reflected in varying levels of aggressiveness |
| [A Survey on End-to-End Autonomous Driving Training from the Perspectives of Data, Strategy, and Platform](https://arxiv.org/abs/2610.00926)<br><sub>Chengkai Xu, Yiming Cui, Jiaqi Liu et al.</sub> | arXiv<br>2026-10<br>📑 5 | [⭐ 109](https://github.com/Jiaaqiliu/Awesome-Training-Ecosystem-for-E2E-AD) | Autonomous driving is a cornerstone technology for the future of intelligent transportation, where end-to-end learning has emerged as a transformative paradigm that directly maps multimodal sensory inputs to driving acti… |

## 3DGS / NeRF Reconstruction & Sensor Sim

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DriveWeaver: Point-Conditioned Video Inpainting for Controllable Vehicle Insertion in Autonomous Driving Simulation](https://arxiv.org/abs/2606.31918)<br><sub>Junzhe Jiang, Zipei Ma, Zijie Pan et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 16](https://github.com/LogosRoboticsGroup/DriveWeaver) | A pivotal step in autonomous driving simulation involves inserting foreground vehicles with predefined trajectories into simulated scenes |
| [Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796)<br><sub>Leshu Li, Jie Peng, Yang Zhao</sub> | ICRA<br>2026-06 | [⭐ 14](https://github.com/UMN-ZhaoLab/Pocket-SLAM) | 3D Gaussian Splatting (3DGS) has garnered significant attention in Simultaneous Localization and Mapping (SLAM) due to its advances in capturing fine-grained geometry features and synthesizing novel views |
| [NIDAR: NIR-Guided Intrinsic Decomposition for Scalable Scene-Agnostic LiDAR Intensity Reconstruction](https://arxiv.org/abs/2609.36878)<br><sub>Junjie Zhang, Jie Yin, Kefei Qian et al.</sub> | IROS 2026<br>2026-09 | [⭐ 19](https://github.com/Zjj587/NIDAR) | LiDAR return intensity provides complementary surface-response cues for robotic perception and state estimation, yet many simulation pipelines omit it or reproduce it using reconstruction methods that require real intens… |
| [MM-TRELLIS: Point-Cloud Guided Multi-Modal 3D Vehicle Generation in Autonomous Driving](https://arxiv.org/abs/2606.24301)<br><sub>Hongli Xiao, Youjian Zhang, Yucai Bai et al.</sub> | ICRA 2026<br>2026-06 | [⭐ 9](https://github.com/HongliXiao/MM-TRELLIS) | Recovering realistic 3D vehicle models from autonomous driving scenes is crucial for synthesizing training data and building simulation environment |

## Perception: BEV, Occupancy, 3D Detection, Mapping

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Deformable Gaussian Occupancy: Decoupling Rigid and Nonrigid Motion with Factorized Distillation](https://arxiv.org/abs/2605.28587)<br><sub>Yang Gao, Wuyang Li, Po-Chien Luan et al.</sub> | CVPR 2026<br>2026-05<br>📑 2 | [⭐ 22](https://github.com/vita-epfl/DeGO) | Understanding dynamic 3D environments is essential for safe autonomous driving, particularly when reasoning about human-centric, nonrigid agents |
| [FreeOcc: Training-Free Embodied Open-Vocabulary Occupancy Prediction](https://arxiv.org/abs/2604.28115)<br><sub>Zeyu Jiang, Changqing Zhou, Xingxing Zuo et al.</sub> | RSS<br>2026-04<br>📑 6 | [⭐ 142](https://github.com/the-masses/FreeOcc) | Existing learning-based occupancy prediction methods rely on large-scale 3D annotations and generalize poorly across environments |
| [Horizon3D: Sparse Radar-Camera Fusion for Long-Range 3D Perception in Autonomous Driving](https://arxiv.org/abs/2606.31096)<br><sub>Geonho Bang, Geunju Baek, Dongyoung Lee et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 24](https://github.com/geonhobang/Horizon3D) | Long-range 3D object detection is critical for safe autonomous driving at highway speeds, yet existing radar-camera fusion methods remain limited at extended ranges |
| [Explainability-Aware Frustum Attack: Exposing Structural Vulnerabilities in LiDAR-Based 3D Object Detectors](https://arxiv.org/abs/2606.29963)<br><sub>Chengzeng You, Binbin Xu, Soteris Demetriou</sub> | ECCV<br>2026-06 | [⭐ 2](https://github.com/SecMindLab/Saliency_LiDAR) | The structural vulnerabilities of point cloud-based 3D object detectors remain poorly understood |
| [PointLAM: Local Attentive Mamba for Efficient Point-based 3D Object Detection](https://arxiv.org/abs/2609.21780)<br><sub>Xuanming Shang, Weijia Zhang, Chao Ma</sub> | ECCV 2026<br>2026-09 | [⭐ 5](https://github.com/PointLAM/PointLAM) | 3D object detection from LiDAR point clouds faces a fundamental dilemma: voxel-based methods achieve efficiency at the cost of geometric quantization, while point-based methods preserve fidelity but suffer from prohibiti… |
| [UniD-Shift: Towards Unified Semantic Segmentation via Interpretable Share-Private Multimodal Decomposition](https://arxiv.org/abs/2605.07356)<br><sub>Shuai Zhang, Zhecheng Shi, Zhuxiao Li et al.</sub> | CVPR 2026<br>2026-05 | [⭐ 5](https://github.com/shuaizhang69/UniD-Shift) | Semantic segmentation of large-scale 3D point clouds is crucial for applications such as autonomous driving and urban digital twins |
| [Vernata: Self-Supervised Learning of LiDAR Point Representations](https://arxiv.org/abs/2608.06919)<br><sub>Oliver Lemke, Alexander Liniger, Abel Gawel et al.</sub> | IROS 2026<br>2026-08 | [⭐ 22](https://github.com/rai-opensource/vernata) | LiDAR serves as a primary sensing modality for robots operating in outdoor environments |
| [Towards Compact Autonomous Driving Perception with Balanced Learning and Multi-sensor Fusion](https://arxiv.org/abs/2606.02979)<br><sub>Oskar Natan, Jun Miura</sub> | arXiv<br>2026-06<br>📑 45 | [⭐ 9](https://github.com/oskarnatan/compact-perception) | We present a novel compact deep multi-task learning model to handle various autonomous driving perception tasks in one forward pass |

## Datasets & Benchmarks

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Towards All-Day Perception for Off-Road Driving: A Large-Scale Multispectral Dataset and Comprehensive Benchmark](https://arxiv.org/abs/2604.27499)<br><sub>Shuo Wang, Jilin Mei, Wenfei Guan et al.</sub> | RA-L 2026<br>2026-04 | [⭐ 6](https://github.com/wsnbws/IRON) | Off-road nighttime autonomous driving suffers from unreliable visible-light perception, making infrared modality crucial for accurate freespace detection |
| [123D: Unifying Multi-Modal Autonomous Driving Data at Scale](https://arxiv.org/abs/2605.08084)<br><sub>Daniel Dauner, Valentin Charraut, Bastian Berle et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 403](https://github.com/kesai-labs/py123d) | The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics |

## Safety, Robustness & Evaluation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [CCFM: Collision-Constrained Flow Matching for Safety-Critical Scenario Generation](https://arxiv.org/abs/2607.04451)<br><sub>Ke Li, Kaidi Liang, Yuxin Ding et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 3](https://github.com/KELISBU/CCFM) | Evaluation of autonomous vehicle (AV) planners in safety-critical closed-loop simulation is essential for real-world deployment |
| [Lipschitz Optimization for Formal Verification of Homographies](https://arxiv.org/abs/2605.23203)<br><sub>Jean-Guillaume Durand, Panagiotis Kouvaros, Maxime Gariel et al.</sub> | CVPR 2026<br>2026-05 | [⭐ 2](https://github.com/jeangud/homography-verification) | The adoption of vision neural networks in regulated industries requires formal robustness guarantees, especially in safety-critical domains such as healthcare, autonomous vehicles, and aerospace |
| [CADET: A Modular Platform for Evaluating Distributed Cooperative Autonomy in Connected Autonomous Vehicles](https://arxiv.org/abs/2606.04072)<br><sub>Pragya Sharma, Brian Wang, Mani Srivastava</sub> | ICRA 2026<br>2026-06<br>📑 1 | [⭐ 0](https://github.com/nesl/cadet) | Deep learning models are increasingly central to autonomous vehicle (AV) pipelines, yet their integration has traditionally followed a monolithic design where perception, planning, and control execute on a single onboard… |

## 🏢 Industry Tracker

Latest 14 days of news, official blog posts and new open-source repos from tracked companies. Full daily feed in [`daily/`](daily/).

<details><summary><b>Waymo</b> (223)</summary>

- 📝 2026-10-16 [Hello Toronto! Waymo is En Route](https://waymo.com/blog/2026/10/waymo-in-toronto) <sub>official blog</sub>
- 📝 2026-10-08 [Sober Drivers Still Face Nearly 4x Nighttime Risk: Why Road Safety Demands a Safe System Approach](https://waymo.com/blog/2026/10/sober-driving-benchmarks) <sub>official blog</sub>
- 📰 2026-10-21 [A Waymo Turned Into Oncoming Bucs Traffic—Its Riders Jumped Out and Ran](https://news.google.com/rss/articles/CBMiowFBVV95cUxQV3N5Vzc2bWpseUZHQ2p2QTl2eXRON1RJZjM5NGNZUVduZDFmdXZDYjNLdk5CbjlFbVZOTm1MWXZzTVFxenhnNFJJTTZTNTVaRUNtM1J4SWFUOXRHTGxSUkplbHFvdnpjWG9Ram4yVlFDZkwwekRLYkQwaENfOXpjQTBtblQzeUlmNk13OVgwQURmQmp2d0ZPaWFBYll1M3RFX25j?oc=5) <sub>MotorBiscuit</sub>
- 📰 2026-10-20 [Waymo to bring fully driverless ride-hailing service to its first Canadian city](https://news.google.com/rss/articles/CBMid0FVX3lxTE1uXzlXSUtyUERjQ0dpOEJlNWN4QjZVZmotOVBzQmhXa0xfQkZQSVZOSENZSnV2OENpNDFNbFhPU0h3VVBvQVJmQnNJdEtNTGd0OHhBODEzX0ZUWXNiTmd5cWpwaERIdjlRaGxEWnFXVVlYYmIzLWtJ?oc=5) <sub>Daily Hive</sub>
- 📰 2026-10-20 [Waymo Plans to Quintuple Fleet With $5 Billion Private Debt](https://news.google.com/rss/articles/CBMikAFBVV95cUxOVy0ydmJQU28xSVhQVFJTZFRqVGw4ck1xNkU1NGIwV2ZZN0lNWWdxQ1cyTjBOVnM4TVV6dGJNUzZIcko5TDVSOTAyaVEybnNCUENpdUplRDh6SXphanpULXBSWlgxQzk5MXdoOFZmYlVIenhrdGo2UzYxYkktM0NhNkJXV2VYeE9lQmRCZ2ZXSkM?oc=5) <sub>news.lavx.hu</sub>

</details>

<details><summary><b>Tesla</b> (342)</summary>

- 📰 2026-10-21 [Tesla Mad Max Mode Hits Australia: 4 Details That Matter](https://news.google.com/rss/articles/CBMilAFBVV95cUxNSzNJenk0TmRUOWdKemJNSXQxR0xpdmlDMWFpYW42UHNqVWpfb200RkdpMlJyMGNDSlBSTWNrTkZGbk9Ud2lFUmJpM2laNHc3RUV1cmJkaWg5eGRiNlByclMtUzdmejI5NmE4UDZYc3QweGk2ZWlMbGtfNk1jbzkzcWpJVkg0bjdubjBQRkQ2aVd2SE9m?oc=5) <sub>BASENOR</sub>
- 📰 2026-10-21 [【视频】被喷也要说，2026巴黎车展小鹏NGP与特斯拉FSD对比体验](https://news.google.com/rss/articles/CBMia0FVX3lxTE1XVlVJWDZ3VHA3bGtRT2pBWDdOWEFBMmJyZDBKVDJZZ2lPam5OeWF2a0ZNaWhPRlZSTkRzWFZMQ2VmdE5yVkFIMDc3RU9tby1PejhNNHY5dFZHRXB3bXJEaUJQQ2dIdDlWb0k4?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-20 [特斯拉Semi重卡路测FSD 2028年或上路](https://news.google.com/rss/articles/CBMigAFBVV95cUxORXVGQWQ3NWpJc0IwSkdhSVJ5YzNMQ2FSNWU4YV83WXlZTkZkM2RRTGdVUkUzNFBWck1LaElUX3dxRl9TZXAtTDlnRG5yT2QxTUUzSE9XWWZzamRDaVBwajhHLWZJNUd6RFdPdHVlaURoaWxPYksyZ3pzN2dubmNtSA?oc=5) <sub>新浪网</sub>
- 📰 2026-10-20 [The Boring Company’s latest Tesla tunnel truck mod “fits like a glove”](https://news.google.com/rss/articles/CBMie0FVX3lxTFBBWEJmaHJ6UTNEWS1fSEJBcUoySmVJVC0zelRPY3I4SEl5LU1zZWRFXzVoZ3ZVUTlwd3JkRERjY09kbE55blNQeTYwVmVQSWJQYl9vU2VHRXEyck10VW95RlFidFdMSGV2RFMxR2RUdFlSazlVRkJaUG9xYw?oc=5) <sub>Teslarati</sub>
- 📰 2026-10-20 [2026.38.5.10 (FSD 14.3 Lite & 14.3.13) Official Tesla Release Notes - Software Updates](https://news.google.com/rss/articles/CBMihwFBVV95cUxOQ3FZQ1VQWWxKTlpPUTJCeDJMR29hdXExVnF6LVAxSmxnVnNNaUZXRHB6dnhTTEd6el8xTmVSTWtReWVRQWxJNGxKQl9aLW9pcFJMMEpJbjlPcmp3NWlzSWtoeDlXa3FyV0RuUlBha3VKSkx3MlRiV3ZVTzBab2VCX0o0MXNnelk?oc=5) <sub>Not a Tesla App</sub>

</details>

<details><summary><b>NVIDIA</b> (232)</summary>

- 💻 2026-10-20 [NVIDIA/flare-local-inference](https://github.com/NVIDIA/flare-local-inference) <sub>GitHub</sub>
- 📰 2026-10-20 [Nvidia, German Ministries Sign Declaration to Develop Industrial AI Models](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBDT1dONjlDR00zX2ZfMktFaVhZU05PX0NlbGZhd2hkVUw5YUhZdnhxUnRwYi1rY1MwXy1NYl9KUnl4Z1d3RkJNanBjaWxtNFhLNHlNdHctNzVscVE?oc=5) <sub>www.tokenpost.com</sub>
- 📰 2026-10-20 [Volvo Expands Partnership with NVIDIA to Develop Next-Generation Driver Assistance Systems](https://news.google.com/rss/articles/CBMi9gFBVV95cUxPamFENURJNWtpbXk5bXl2MWU4amVJRUJKemZzLXJsakNxNjZENlphdkJXZ0ZiN3F2UDlXMEVra0Z6SXdLRkk3NnRlSGd2WGV4YXNIekxxWExQRzhHZFF1NlpjN0tSQW83WHdoUXlFU0xOMl81ZVlhRWl0UG9HdXR1X1duQ2JRckQxX2hUNHdCR1NIcnJ2UENQQlN1QUUzT3VTdU94UHh1S294di00Rm5BdXdiNVNPLU9abGZmM3IzU2NLSzUySnI1cFplRXZUYUVhQmNuZDJCSC1DZjlmOFlnWVlaVEtJaGJid3JSQlhaenJQZnRTNUE?oc=5) <sub>Gasgoo</sub>
- 📰 2026-10-20 [Mercedes-Benz and Nvidia extend strategic technology partnership](https://news.google.com/rss/articles/CBMipgFBVV95cUxQYXc2bWNFcV8wVVVsNnhIRzJfeENTTC1lM1BiOW9oYVA0Mm9lVzV5MVB4ZU91VVd3M1NoMkx0RUMwMXFCTW5QRThTWDBVM1VyMzFhZHQ5RklFVzBwMDE0TzQ1ZFNMSlpubEJSaDdmRWxvVDVtZTVqal9YY2E1a3YzdW5nbHpvYzZPcDBCQ2o5ZGpYMDhOZ3owWFpubW9NcjN2S1lyTENn?oc=5) <sub>WardsAuto</sub>
- 📰 2026-10-20 [Volvo, Mercedes-Benz separately expand NVIDIA partnership for automated driving](https://news.google.com/rss/articles/CBMiwwFBVV95cUxQbTU3V1Q4aEc3eHZpMkFKR3hCOUctZm1adnNEZDNoT3cwMEtsNUpUcnd4bmtjVWM4eWhpZllxWmtfdDNscTBRQXA2eFppdWo5UTlYNHR3YWJKWHJINXNpek1yd1g4MThjRVNwNjFSWUloLVJMOUJ6VWF3QTlaR1FHYkg2S0dyUU1HaHgycXN3ZGRhWmkwYUlGOC1nXzM3WVRRcXROSnFFTFU5RnFfU19FZTlOcFF1cVFUMDY1cG9iMjh5UlU?oc=5) <sub>Repairer Driven News</sub>

</details>

<details><summary><b>Wayve</b> (63)</summary>

- 📰 2026-10-20 [Protesters Call For Limits On London Robotaxis](https://news.google.com/rss/articles/CBMilwFBVV95cUxOMEpoWDVobFR3S192T0xjM2xMcTktR01qdkVJa2hVQUtONk1NVjlPR1dXMnBMVHB0LXFPdEszMEVJVDE1QnZIaTJFaDFaV3lNc3Z0UlVLYWtlWDRpRW41V3N3RWdSOWZoSkhnTG1XVkhQUzdFRlZwSmxpUDdDTzY2d05OWF8zdGVtbTVZLUtfcDV1TzN3RExF?oc=5) <sub>Silicon UK</sub>
- 📰 2026-10-19 [Uber beats London cabbies in £340m court battle](https://news.google.com/rss/articles/CBMiekFVX3lxTFBmYmdSOWI5TnJnSDN3TkVDUlhzMlZvb3VZd05aSnYxRGp3RVdVdUJFaW1UbDV6dzA1ZTRBQU1SQlhETHJEaGgxUFA0OFJNM01YNVpNX1lDRzlIRkZmUnhpRC00Zno3aWQ3cDk5RENEN0p4N1h4c2J5S21R?oc=5) <sub>City AM</sub>
- 📰 2026-10-19 [Driverless cars are a progressive cause](https://news.google.com/rss/articles/CBMia0FVX3lxTE5yZy1KVnFVMl9PamtVTDlBWkFxaXdzaEpIcTI4WnJsbmpCRUVvVnA3ellWZ1k5bUNnRlhjUnMzcnZRcFF4UFNoSUdVMnB1TlZ2ME5GbXVmSDNpa29vNjBqdXp1cDBjVGIxcDZV?oc=5) <sub>Arguably \| George Eaton</sub>
- 📰 2026-10-19 [Uber launches Britain’s first autonomous taxi service in London — Autocar](https://news.google.com/rss/articles/CBMipwFBVV95cUxNRW1BMFUtZl9kX0lxdHJ1R05kS0FNN0hGUTU0VVl6S3dpSjlTWUs1cmpXREJyLXZkY3JvVmNHcXo2eXBybjRiTmprLTFKS3hJdm1lS0lYNXVETGZ2cjBES1hzcllXU2ZTUlBFOUg5UmdzSmtFdC1fR1B3M2VHcV96VkpqaU90VzVKMUF3LXJTM1M0OGx0TFJWUURWRUdKYVN6TEQwYVRWQQ?oc=5) <sub>UA.NEWS</sub>
- 📰 2026-10-19 [London's new self-driving taxis spark safety and traffic concerns](https://news.google.com/rss/articles/CBMirwFBVV95cUxQNXk3M1FmT0NlRGxZWmRFT1FocmF5SzlPWFFEUng0cWdvbGtQZ0NwRURsV1VYUUJYMW5Ib08wUUMycWlWWC0xVlZhX2J6U3E0VTZUZUM0TFhPb05BYVNkcFdDN3NFQ2tIdkV5T2pQWW4xbHljS3Zid0k5VVdpaHlaYzM1NlJVcG1fZkw4enRyaTVqMGVobl9URDAtT1lrVGlNVzRxNHd4UEtUY1A0YkxZ?oc=5) <sub>Autocar</sub>

</details>

<details><summary><b>Momenta</b> (93)</summary>

- 📰 2026-10-21 [Momenta曹旭东：世界模型加速“智驾摩尔定律”，2028年迎来L4规模化落地拐点](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1ZTEpzYjZWMGlUckQ0TWJnM0tEXzFmQWJuc0hCSVV2Z01RRUJiUkNSYzRzeFMyRDhzdS1qaDN1RVFxNUliY2lsVDF4d3JTcGVhQTJrNXl3RU8wMU0?oc=5) <sub>网通社</sub>
- 📰 2026-10-21 [【图】2028年或为L4规模化落地重要拐点 Momenta累计量产交付超130万台](https://news.google.com/rss/articles/CBMiYkFVX3lxTE9nZnlIaFhNTzZrcXItaWxIOENDUkMwUGdTc3Bia3ZGano3dzAzbnY5b3oyRnY0cWMycHcwY1ZpQmw5UkJGYnVpOG9rdElTZXNHa2gzQ3p4NTlyZWRHSWFGaUh3?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-20 [Asian Growth Companies With Strong Insider Ownership](https://news.google.com/rss/articles/CBMi2gFBVV95cUxNbmZlSUEyX0MwLTRiYUVTYy1qMmZkN1NmNTB6b3VnOU1hS1ljOWx6a3N4NDFmSENvNUtTNWhOUXhqcnRoVDVBYk9nLUlnVjdTNkhJb0RNaG45d0hkMjUtdmpLM3RDY0pMVy11NFh5ZzRZeENDWHFqUU80OXpEc1JtZzY3OHI0SHpnV3lzLUNTVzNnZFRmWkJfUWR3S2NZckVVdXFyWnAtbHFyd3FpU2xLOUFWUmZhdm9NQks5bkFDX2swZm10enppSXd2QTREZS1VTE1sSDlqYkFFd9IB3wFBVV95cUxOQWhqWVF5UGt2Mk1XaVB1eTFzcjJYSzBMenk0VUFpLWl4em0zdTZWaGlpZ2hmX1JaLTMtZy1sUENhN2FPeGxXdmVqdENMc1l5UGxJYS1SZHhhTmZIVS1uVkJfVS1HdjFnM1NVUV9qTmZHaXRUSkVmOEZ1dWdmQzIzNDRuWDg0U1c3QU5rdlduS3gza0hVQTdTNTJON1ZjNXdXZUxnbDZGam9zYlNFQVpjek9WdnRUbkQ0cVNxR0k1OFJJeFo4YmRWSTZvUkdnbzlmQ01xTFFuOHI2VV9Ja204?oc=5) <sub>Simply Wall Street</sub>
- 📰 2026-10-20 [带激光雷达的豪华插混SUV哪款好？全新XT5 PHEV、领克900与腾势N9智驾算法横评+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE15MEFrYklyUm0wZUU4Q0hwN1JOYXd6anNjcGtPSk9MWkhqX3Z3S2ZyMTdZRHc5dEFGVHdzR3lCdmVpWmxpYlpmTHVKV0FvVHZmOUEwajZVUUFSb21zWVRPMGN5Nnp1dnhLMWZYTnZBOFZFUQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-20 [Chinese Autonomous Driving in Europe: How Close Is It to the Global Supply Chain?](https://news.google.com/rss/articles/CBMi2AFBVV95cUxPZGR1Q3UyZThrRm53UHFwM29iTjJPLXZUZ0JsVVdJcl95dFZvanVWcElQTU44SWI1c05tMTlWcnNLREhUQ3lDUGgyMkJpVXBBeHVTb1pHRFhXMjRvdWllN0JmWmlpajFhVnBldHAtSWpJb1B3bkhKV1NxT1picUpJNVVrUmF6aTFpUXVLVEpwUmFjVmJuVHEtV2VwS3dlZFBYb0ZKckphMHB3Ti1Xb0dhbzdXcTVLN0NZVGtEM1piRUw0ZXVwODNJYTNGMno3N3hzMFZIMWhWVGM?oc=5) <sub>Gasgoo</sub>

</details>

<details><summary><b>XPeng</b> (301)</summary>

- 📰 2026-10-21 [【视频】小鹏MONA L03探店：12万级，配置单“卷”疯了](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBqaks4TXhqZ1huMm5QNy10UFpUNTg5OXhLdnQyX3Y2U0p3amxVa1E1UGVwUGs4a1E2amN6ZFNUOTlKa1UzeUpDTEVmd3ljQm1KR18tazd4cEdlZFk?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-21 [9分钟补能450km：小鹏G9L与4款大五座SUV超快充横评](https://news.google.com/rss/articles/CBMickFVX3lxTE5ldEx2N2ZxVkMtZy1KNlkzQ1VYWm1QUG4yT1ljVG0wWG94dG5NS3ZHV1BwT05xdmxxZFhYZUdQcTUzc3J3NnJzWXkzbWN5R3hidTZjeFUyLWpIVUhEeEJTS1RiTUhwWkZSU1dmRndWVmhwdw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-21 [智能体验好的大五座怎么选：小鹏G9L、智界R7、理想L6、极氪7X横评+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5EVjBRMnMzZjNXNjB0cExnUjlacVg3QThraDIwVTRPNGxRNmZid1VQekhxaWg2MjRNbGlmOVBsMk5OLS1Hc0dBYmh6d2h1NTVwWXktN1FmYmJDa2liSlU0?oc=5) <sub>新浪网</sub>
- 📰 2026-10-21 [智能体验好的大五座SUV盘点，小鹏G9L第二代VLA全系标配值得优先看+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBWMXQzOWs0ZEdCbEVIM0FjYy1OaUo4Y2hCbFdXemNVcHNvaTNIN2tMTGRoNWRSNFIySGxvYW9kcWpKSlVJa1o5ZzZEY1BibzJMcXJwb3djdXEyaklWRlhJ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-21 [舱驾一体怎么选：小鹏G9L、智界R7、理想L6与极氪7X智能体验横评+避坑指南](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1zdzJBS3kta2I2UGpQdFpIOTNkVDhibm1sNHBfNUlwTjBwNmlGVk9lYXRIYUN4Y19kcmZBcWpIRlp0YXlKM21JaTd2Q3NfcGU4M1I1endLTHhjOXotOEsw?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>Li Auto</b> (156)</summary>

- 📰 2026-10-21 [The Little Blue Light Steps Out of the "Confinement Room"](https://news.google.com/rss/articles/CBMiU0FVX3lxTE14OF8wQ0xkMmlwT3NTMmhqUUgtcUItUTdZRE01V1hoTHVzRFZRR0VnUmNWZ0o4RG9pNGNySVJHZzh2RXVkdGtzRncyMzR1Sl9IQ0pz?oc=5) <sub>36Kr</sub>
- 📰 2026-10-20 [理想L6后驱增程版对比问界M7/岚图FREE，25万级该选谁？3个维度说清+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFB1eWhqbmdhazNkaldLeXhfbUtzM25vMlVLRFl0SDAxX2FDc1V1ekR3YVBmaXVjb1ZvdVBRNi1uOFFTcE1oYUF1ZVJjZkJhdXFsSHR4aDBVamxvYnVMYlBERnZfQTRHaFQ2WTdzUWtpalBMQQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-20 [China proposes uniform rules for automated driving lights, targeting 2028 roll-out](https://news.google.com/rss/articles/CBMijwFBVV95cUxOMlNLYWJGS0lnZld6LUtDY3VJNkQxM1ZVSlR3cEpRdWwyT0hfZDBnMDBnSVdUVVJIS0NtVVFjUkxhV2VENkFmY0dSdHZUaW1JdW52UkNZRGRBeDVTZ1o2YzBYNzJ5ellMb2JhNXBMRVp3dTJaZVJWcVQ0TmpZem5ESk1reGVoNy1nMDRXdkY0cw?oc=5) <sub>CnEVPost</sub>
- 📰 2026-10-20 [Li Auto: China's best-selling premium EV firm is coming to the UK](https://news.google.com/rss/articles/CBMiqAFBVV95cUxQbk1TSE9aVC1VOGhHcmJxRk9TTzVYcHNCcUd2UGlvWVFIbG9FQkJTbjVkTVhXeERrV19lcXM5c1ZBUTNQZWk1WHNWa29YS0xYZ1VrOFFHS2NDOUdIVnVNMVJpend0d0FOUE1rblpDN05Idk1rdE1HQmpyMkZ6UGNJU2M1RlFJSDM4clRjbUlzbjJtWFViS3luaFVVNzhicmFSNUVvLXFxb0k?oc=5) <sub>Autocar</sub>
- 📰 2026-10-20 [Li Auto's Chip Subsidiary Completes First-Round Financing of RMB 1.625 Billion](https://news.google.com/rss/articles/CBMi4wFBVV95cUxOUFZ1UkxUTmZGU2IwbV9CSGpmTldUQjFhYU9MUy1wRXpXczJiNGdRVEpLRE5lLUIxTV9aQ3NWamlLMXQyOG96ZWJhMnhma0ktbUEtSHdjOE9zWkNmb2haVl9FM3F1T2lpOEQ0cnJvQ0VSeEM1TUpIOENyQlZCVGQ4MTRNa0ctUmY3dlEyZUF1d2VpS0NjdEI3UUJhMU9TZlB0eFJzbGNNdWxlaUNVM0thRkxtZ0hYdTRNUDFHY0ptZ1pnUF92MjhQeDlQeTJ1SGFTS2cxM3RMVTE0QWs4bzFIbGxkcw?oc=5) <sub>Gasgoo</sub>

</details>

<details><summary><b>NIO</b> (157)</summary>

- 📰 2026-10-21 [【视频】标配激光雷达却月销仅300台？蔚来EC6为何卖不动](https://news.google.com/rss/articles/CBMia0FVX3lxTE53UFVpSzNiQnk2T3Y0aTBrOEJ4bVlSRnpOa3I4eWJTamdlaFpkV3MzaFdNNzkwNXdkSnd4QW9SWGJCNTBORWFJamFrazA4MDhLZ0RnNjB4NUJoSWVZZDhseXdTWERoSUV1WHJF?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-21 [【视频】家用纯电运动SUV，探店蔚来EC6 租电26.18万起，精致小家庭首选](https://news.google.com/rss/articles/CBMia0FVX3lxTE9SZ0IwRjZ1UVBwWlZnVHRvMVlZZzBEV3pLUW1ORmJsLVlFNHBFbUxYakVpSzY3V1Joc240R09FcHhkV0lMdkJVZ0NUc3FiZUtidFNMeEljX3g5ODdpNFJGVlowaEgzb1pIMnBv?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-21 [综合1602km续航+9分钟快充：小鹏G9L超级增程与4款热门车长途横评](https://news.google.com/rss/articles/CBMickFVX3lxTE03Mmp3S0dCcHZZQjdabnlkQmszXzdMY2ZuSjhoZTByM2ktWXgwcTQ5SmtQazNORUM2TkViTkxEcENqLVRsTDNjdWQyNUVDRUJLV2hRQTkxdXZnY0ttQzBhWW1VNV85WmwyaWFZcFZDYnRoZw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-20 [国产“豪华大型SUV”，车长5365mm+707Ps，压榨700牛米](https://news.google.com/rss/articles/CBMia0FVX3lxTE90dTdSaW5EYk5ld2VHdTZjWGFuX3N4a3lMdjJVRHdBRkVsRE9sa3BuVmVaaUM4UzVFOWdvNEI1cEI3YXFibnB2VlVZWk9rSUdMV0w0UnN0bHFsQXo3bUVLUExzdnVpT3FQOFF3?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-20 [【视频】22年蔚来ES6电池租赁](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9VSUg3WFRLcGJfSlBzdm1PT3htd3JObXpvTE1laTZTWXdEYms1Ml9mSVpUdnRtbUdEQVFHSFJUckJRbS1YLW54bWpobFh1RWN5SXZMbjRKVlJYUUU?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Huawei</b> (346)</summary>

- 📰 2026-10-21 [GAC-Huawei brand Aistaland said to be planning battery swap models under CATL tie-up](https://news.google.com/rss/articles/CBMiiwFBVV95cUxOa3VxTlUwR1Vxa1NjQm1KcTdSN1pQLUJXTXRKM29sVWNNZDFyV1VrVm5YaXlJRWNhRU92ZXNKUVNnR0NIcnBCU0Uwb1dYN1BrTEcyUENqUDhoR1lFQ0psdTh4SHNCWVB4UkhjemVLOUljNW51T2ZlS0pKa09CQXlpOG04NEViMW1MWjFv?oc=5) <sub>CnEVPost</sub>
- 📰 2026-10-21 [【视频】华为乾崑智驾ADS 5 OTA，细节升级更实用！](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBHTk15U1VWbHNJd1gzZ2I0TWVBZGJFRC1qS0s3RU40SnE0TUVPRFN4YVFuY0JIcjFwMmNsTVpYaEJSaGUwOFFvTl9XUXc0a2FkVmdiZXp0N0U5UFU?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-21 [【视频】岚图泰山X8搭载华为乾崑智驾ADS V5.0.2，用了半个月感受如何？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9BRjlFMnJlTDF4SnYwV3dOMFJ5SG4ya3BNMGEzMDNnZzgtb2pRYTJodlN1WlZDMmFlQmtXVUh2aW04WnExRkkxcGNQZ1lGMHFZTHRhMkJjeHByMHc?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-21 [【视频】24年奥迪A6L 24款 45 TFSI 臻选动感型](https://news.google.com/rss/articles/CBMiW0FVX3lxTFB1UU1kTUdQbUxySlp2cnR6MzU3WWRhSGxmMHJveTZaeEViNmY5aEl2eVh0cUVwTm5DSjZ6NGJ5anNMQkxLcUJXSDdkZFFUUXJQZTFaYlBzLW9wdEE?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-20 [Avatr T09 Concept debuts in Paris as a flagship SUV](https://news.google.com/rss/articles/CBMikgFBVV95cUxNT0d6amc5WWY4dWp1SllIeGY1enNnc2pLclNaOTBQQl9yVTFReXVBdlZ0ZF9XRDRrVmwzMzVBZkhVTjlnV0E0eDRkQmxILXduZmdtT3pYREhNT1lBYmNyamVSUW9zTllkd25qV1YzMFhoSGF3S1Z5ZjVQSjJ3SGkxMHlqTHFxUlBLZWtzUi0zU3Y3QQ?oc=5) <sub>Motorist Singapore</sub>

</details>

<details><summary><b>Baidu Apollo</b> (48)</summary>

- 📰 2026-10-21 [Robotaxi周订单突破25万笔，无人车替代网约车进入商业验证期](https://news.google.com/rss/articles/CBMiVEFVX3lxTE82YUlXRTRURjh1SElJNG9PdWtLd1dMSjdCSGQ2Y1Nnd2M2UmxEYXpzbU1rOFdPVTBDZEZGZnVCTFlaRWl3UFVrMmZJemVrX09FOWdXUQ?oc=5) <sub>虎嗅</sub>
- 📰 2026-10-20 [The most visited websites in the world today](https://news.google.com/rss/articles/CBMiVEFVX3lxTFBZSHRyd1hRTG1DR2pYakZKeDlVeU1heGd6enpNdXNFMEd3bVBpS3RxZ2x5Mm5kYktNN1U2QURtZzg4dzdiTTlYNFRhamVQXy1fQUpUNw?oc=5) <sub>qz.com</sub>
- 📰 2026-10-20 [GM to Close Detroit EV Battery Plant as it Scales Back EV Investments](https://news.google.com/rss/articles/CBMieEFVX3lxTFBxandTYTJBVXBWUDF1RUxxa2JUMzJUTE1CUGk2TzcyQkk0RDJGMTJFSi1FVlFOelF3NWNqMkJEdGU5TFBHeE5wRDRPSWtUdFdmMWdfMVhyTllNZTVWY0JMOHF0YlBaNE5nTXVOQjFEU05ZbnZseDMwZw?oc=5) <sub>Drive Tesla Canada</sub>
- 📰 2026-10-19 [Top 5 Self-Driving Car Companies Leading the Autonomous Vehicle Industry \| Automotive IQ](https://news.google.com/rss/articles/CBMizAFBVV95cUxOWERVaVQ1RW5iLVlrYWtvRFFkS0pvQ3B6cno2dWlWN280NDFvdU9yZl9NcXItSTFGTmtReFlOQXhCcUxiX3dJYkd1WVp1NHY5b29yOXFfSXhBSThyQU81ZDdYMHdPUFhFZ0F0TmpFamhHQnNLWHJlQ0lDRnhUMjdtbTh4QjNsMkZxeEpuT0s5ODhBcS1La2xzWldXc0l0Z290Y2JheE9uVXhUWF8yOVRXV3J5NGdfV0sxVHVVb0FVS1BXZ3A0LUVxaGRVb07SAcwBQVVfeXFMTlhEVWlUNUVuYi1Za2Frb0RRZEtKb0NwenJ6NnVpVjdvNDQxb3VPcmZfTXFyLUkxRk5rUXhZTkF4QnFMYl93SWJHdVladTR2OW9vcjlxX0l4QUk4ckFPNWQ3WDB3T1BYRWdBdE5qRWpoR0JzS1hyZUNJQ0Z4VDI3bW04eEIzbDJGcXhKbk9LOTg4QXEtS2tsc1pXV3NJdGdvdGNiYXhPblV4VFhfMjlUV1dyeTRnX1dLMVR1VW9BVUtQV2dwNC1FcWhkVW9O?oc=5) <sub>Automotive IQ</sub>
- 📰 2026-10-18 [The Gap Between Autonomous Hype and Reality is Growing](https://news.google.com/rss/articles/CBMiO0FVX3lxTE9xdjBpQUdKZUowYjhpVlZwU20tUjNhN3hpQnFldWpfOV9tdUdaVkRObnR6VlY1eFlFdFU4?oc=5) <sub>Howl.link</sub>

</details>

<details><summary><b>Pony.ai</b> (148)</summary>

- 📰 2026-10-21 [Robotaxi周订单突破25万笔，无人车替代网约车进入商业验证期](https://news.google.com/rss/articles/CBMiVEFVX3lxTE82YUlXRTRURjh1SElJNG9PdWtLd1dMSjdCSGQ2Y1Nnd2M2UmxEYXpzbU1rOFdPVTBDZEZGZnVCTFlaRWl3UFVrMmZJemVrX09FOWdXUQ?oc=5) <sub>虎嗅</sub>
- 📰 2026-10-20 [5年招引16个百亿级项目，广州南沙产业聚链积厚成势](https://news.google.com/rss/articles/CBMijwFBVV95cUxOckZMcHo0c2p6SmlUeVAtSWRFajJGNmFrVUNNMVhkb2daenJoNjVyeDVwTndieWpkVlRManhka1JUaVl4eTBXU09jZ0JNdXRJdW9QTWh3WkFkZlB3S1ZfbDYxd0Vqa3llX2htUVRDV0FQTjE1cVNDX3RFY1BlMmVINTl5VWJuSG84Q1REeml2Zw?oc=5) <sub>21财经</sub>
- 📰 2026-10-20 [小马智行收涨1.62%，成交额1250.1万美元](https://news.google.com/rss/articles/CBMiggFBVV95cUxPSnJFdFY1VnRwYXY0Z1J0UUVGdUx4UnQyT3E5Wlo4V3p6b0tCVFFWNnZDV1NSSmlXYV8ySFo2RllBcmxoaVpMSWU1RzFCb0JVRVFNeFQzZGFsdWR2ZGV4bFNTSU9mVzQ1SktIR0tPdnlhaFlYVDY1bWpQd3dsZm1CaE9n?oc=5) <sub>新浪网</sub>
- 📰 2026-10-20 [PONY AI Inc. to Report Third Quarter 2026 Financial Results on November 18, 2026](https://news.google.com/rss/articles/CBMi5AFBVV95cUxNak5xVkVieXhOdmtHaTJaR1RQaktaeGNORjdUQW5xZ3lrclVGYXpleEJwQUhYLWlLSHZWdTBfeF9mN1M1cW5CRFdMUU02bkYtbUt2Ny1wdjlaekYxUDQ3U2tlTEtsLTlFUXB5NWQ4VmRzUGJVaTNnbmF4Vkhxd3IzUVlrbm0wY0ZiNTJBSHpYUENXTGJEWU5JRU1JeDVLWG9VVHBlNWttR1FpOXhUamhWemhYem9uaTFkQ25jREhDRkI3SmZKSzg5ZU1RQ201RmczY25ZajNSZlFneHI2NGlwVEhLeno?oc=5) <sub>GlobeNewswire</sub>
- 📰 2026-10-20 [Pony AI Inc. Announces Third Quarter 2026 Earnings Conference Call and Financial Results Date](https://news.google.com/rss/articles/CBMixAFBVV95cUxOdTREV19naVQxeG5XQjlxY3ZvTFZ1QXNPQ0RzYU8wVmgyZTJTQ2lfdV9JQ0xrUVJfaHpNYXE1Z051b253TGI5N2lDZVFWanZueVZWM0FzNmZvV0w3SDc1Q2VpUFBvcFJldUw4bW5DT1RlN3otRW9WaTJuN2ptaHMtemUtYlRwMHkxVWR5ZUpPTXFxWVVHSUtrdnlPelNqaFI5b2EtRjV6bk1tZ0N2TFlRWl9BVHRRdEpVajh6Y09ZVktncktn?oc=5) <sub>Quiver Quantitative</sub>

</details>

<details><summary><b>WeRide</b> (165)</summary>

- 📰 2026-10-21 [Sunway Wants Driverless Buses And Air Taxis In Malaysia](https://news.google.com/rss/articles/CBMijAFBVV95cUxPMkRhN1R4dFdGZUszS0EzVWdfV1phOUphZ0Vua25ncEZYdE11bUlGa0hHN2x5WFFQZ0hka2lQM3FTZ25heDJYcTlCN1RDZXdtemFXMTFpTlRDbDRFd1kyMk5Nc3QtLWNYX09lSGtxVGpsZWRRbWdHbnJaRXRmOWZxenV5RFl0VmtCa0JYZA?oc=5) <sub>Finimize</sub>
- 📰 2026-10-21 [Sunway plans trials of autonomous buses, driverless logistics and electric aircraft in Malaysia](https://news.google.com/rss/articles/CBMimwFBVV95cUxQRGM2ZWt0ZXFhcGo2UEVYeEZLank5WktEMzJvcGx1dVVYZUJvcU10aFV1Q25DM1JmZHVQSXJYVFdxZ2hSdF91SWZGOVRTaTZKeGxRYkM0SnR3SktMSXNsT0trX2pTRGI5Qi1KU2o2RE42ZmJHMzJmbmRxUjFiX1IxNEVFM2FrdC1RdVJxQXo2bFBDaGFZMXNiNzRkQQ?oc=5) <sub>TNGlobal</sub>
- 📰 2026-10-20 [Waymo joins Uber and WeRide in Madrid robotaxi race](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQdnRtSjJXejFCSm5rNGxrWTB6d3hKODE5MHBEMVJHODFSSzRKdEduVTRQNHJ2dzkzbDRSdUJCRnhfeFlRUG50NGFxOFlFX21sMjRuMHhMS2l1OTdDSTFESkM2Tjl3SDlJVnpTcTZ1UVR6MXN4b3NNNno3MFpLSjBoQWhNTklBSXpBbGFJ?oc=5) <sub>Zag Daily</sub>
- 📰 2026-10-20 [Sunway Eyes Future Mobility With Autonomous Bus, Driverless Logistics And Electric Aircrafts](https://news.google.com/rss/articles/CBMi0gFBVV95cUxQS0lmM0hFcjJ3clBwSVpVaEkycUxhck80MmdraGdXRHNCNk9DMWctZlhlZFJaTFhNeGkzVmJPTU9NY1NNTlRwb0w5Nk80bzNSZF9PNGZ2bi1sNHJleXdwLUhJOVd5TzdrVmNXOW5rQV9GTGtYWXZIYnhpNWc2aDZqTm9BRUhIOVFYSWNMRFFMd1ZRcDVoalM3QkdTaWJyVEdhT2FnMFNmMVJKTFMzOEpxN3N2UVRURjJUNGx2NEtham9KVUJTWWNPdENiS2JPYlEzWUE?oc=5) <sub>BusinessToday Malaysia</sub>
- 📰 2026-10-20 [Sunway eyes driverless transport, electric aircraft](https://news.google.com/rss/articles/CBMisgFBVV95cUxOUWJCb3pJUXVrU0J4cm0xaDdnNVI1Q3dRU2E3NmJ6enNZaUZjYk5IQzNUVVJwaWJLTHBvbF9VanhXdjlIeWtISUlQWUdMdkVCTnQ5UVpkZzRRMjBtVUVqVUNjRlFkaVFDVVYxQmtSZFBBcnRCczBJZXhtcWZWLWtrVnd3TVlsWU1DQjJCWXBwQXFTTzBsMjVlUGJmSl8zbE9HMzIzMzNaeGZQX05EaW53ajBB0gGyAUFVX3lxTE5RYkJveklRdWtTQnhybTFoN2c1UjVDd1FTYTc2Ynp6c1lpRmNiTkhDM1RVUnBpYktMcG9sX1VqeFd2OUh5a0hJSVBZR0x2RUJOdDlRWmRnNFEyMG1VRWpVQ2NGUWRpUUNVVjFCa1JkUEFydEJzMElleG1xZlYta2tWd3dNWWxZTUNCMkJZcHBBcVNPMGwyNWVQYmZKXzNsT0czMjMzM1p4ZlBfTkRpbndqMEE?oc=5) <sub>NST Online</sub>

</details>

<details><summary><b>Horizon Robotics</b> (157)</summary>

- 📰 2026-10-21 [捷达M6将于10月22日上市 预售8.08万起 续航最高555km](https://news.google.com/rss/articles/CBMia0FVX3lxTE9GNi1yMHNEVmtQaFNkc3lFMFVFTTNkN0pTZVRnYmo5RmVOTzRLZF9CU0JWUWN3cUJkN19zWi1jQU9WcE4xUmV2cHhoNGdTaXE2dnBWNnZ1dklSb3UteGxUc3NoNEZGYmM4dlVF?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-21 [捷达M6将于10月22日正式上市，捷思架构打造](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1oaUdMdXhMV042LWhfcXd0VU96VG1nbUVCQjB4YjJ2OHpER3AtNGZCR3h3SFQ1NVEwSVlGZXFGbDdydDlsWTRtVzRwWWhyajRmZ1FTMVBJSVVYaFU?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-21 [博世拿下千万套订单，地平线芯片出海，Mobileye怎么办？](https://news.google.com/rss/articles/CBMiiAFBVV95cUxQRUg1V0lmQ0RnVTFvb1RjaFV2M2lDQUhBdk1LTkpiRE5rX1Npd3JnWEFDSFhkSFVldEVqWWNmWnNSOEg3VVJoX2Zqa1BsM3pXbmlLVTRMbzI4ZFpKcks1eUx2NVY1bFE5Ml9TcThfMExfT0hoNlJBd1E4OU0zdjdFNXF5Q1U2WUJE?oc=5) <sub>搜狐</sub>
- 📰 2026-10-20 [iCAR V25正式开启预售，提供后驱四驱版本最大涉水深度600mm](https://news.google.com/rss/articles/CBMiW0FVX3lxTFAtT3J1WmtKSDlMdzdEemxOTlN3NVd6WjJzbWVMcHJQbzJxRlp3SUJlM1BUVlFtcWhoVF9uaDRSQmVXMTlQN2k4NjhmZDk1WjROY0VLOERBdmZISFE?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-20 [iCAR V25预售13.98万起，方盒子有点东西](https://news.google.com/rss/articles/CBMia0FVX3lxTE1Kd2FHR0JzbnlxRm9sV1RYb2EySkVleTBLaTZsdl9ZRHpPSmE0UExaNGR5U0VwNkFLTmhiZkthd09QSzhST1NZNmhvbGRQaGhkR2ViYmhKYllrXzdlWklSU0FjVGtZMTlkazlJ?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (31)</summary>

- 📰 2026-10-20 [对标小米YU7，赛力斯全新品牌新车曝光，这车“含华量”高吗？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1FOUdwR2hiMVk2d2tKOUUzMFk2VkVKbm91cUpVRHFac1hmanBZOVlBSnB4NThBV1JVRUpZSTRGYXZRNmFyS3FJS18xcHlvVXl0MDE4WWxvOFBfdGs?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-19 [元戎启行拿下城区NOA前装标配23.8%份额，位居全栈方案商第二](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPQzBaY1V1X2RrMWFsdkt1c0dRM2NUby15bFBGRVIyVzhHNElXVWlzejlDVW50cWZ5d0RIckZLalc5Tjd5VVVnVS0wTUNyVVFNSVF5b3FsUkgxQTJZQU9yTDU2N2t1M3hFSkxUMUxSeWJONnNGcjhuTDB3YkljM0U0TlU3bzVFRFJV?oc=5) <sub>搜狐</sub>
- 📰 2026-10-19 [Beep Begins Testing Autonomous Vans with Passengers in Orlando](https://news.google.com/rss/articles/CBMinAFBVV95cUxQYjhIdjZwdXJCellJZVUteWZIQkgxZEJoN0tldFEyV1pxTVNyRlh4dzJsV2NKOHd4UzNxa2YxLTJQQk1qelA3cm9rVWU0VXJCZ2R1Q3JNbW13dWc3ejVoZk1wX3NEN1VodFZTS3ljVVBHX2JXTmRvdTJDTkpwTXA5MVphMEliRnhxX01yQTg1d1ZkN2JiM2xfdmhrSTI?oc=5) <sub>Future Transport-News</sub>
- 📰 2026-10-19 [Autonomous & Self-Driving Vehicle News: NHTSA, Tesla, Waymo, Bot Auto, Lenovo, NVIDIA, PlusAI, Texas Ventures III, TomTom, DeepRoute.ai, Valeo, KE:SAI, TIER IV, Arm, Technical University of Munich, Taisei, Nissan & Volvo. \| auto connected car news](https://news.google.com/rss/articles/CBMixgJBVV95cUxPRmFjNXk1ZGVyVjRJVXlPMTRvc0tTdlc3UU81MDZfYXJ6bFVzYzVJeUZwR2t4bm5pMjZLajJGODJRN1pHU3V1c2p2ZFVZX1Q5bmM2cUt0clhiNjEzWXhoQS10eDliZ1pwc3ZwejBnZXBPUmhGTkxCUWtrejZrZDJRcElzeHo5RV93dnZ6bXk2WlRZM0J0a0czZGRQTmZBS1lRV0w1aU53VTc1Vy04SzgzcnBRbzdLR2tUUjlrdEhxeFFkaU44MHdQRC1zSU0zcUpZMTJpek94SkZkV1pXdlhQN242MG94OXZXS0RDRTE2c0J1MEttdUg3SGVoMWVZMElQcUUtNG1pcERUS2lWbURScXhmNi1yWS1XOWw3MHdpc0l4NURabWVDRWswRnpOZTZjV1k3RHNjWXNEWFJQMGRESWpET0dTdw?oc=5) <sub>AUTO Connected Car News</sub>
- 📰 2026-10-18 [工信部412批新车，赛豆ME7和方程豹钛9应该是关注度最高的了……赛豆M...](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1zUzU1RXBKR3pOMDJWSV9JajBMWThiSWsxNVVjZW1NblZHZVQwRUxqWHJjTnlBeFktWXVzdGdWSm92RXdHTW15T0RJZjk2YW1yNExsYXhqY3NSTlU?oc=5) <sub>车家号</sub>

</details>

<details><summary><b>Mobileye</b> (21)</summary>

- 📰 2026-10-21 [Intel Banks $150M Paper Gain As Joby And Mobileye Rally In Q2](https://news.google.com/rss/articles/CBMiywFBVV95cUxOZVNKbmU1VlRTYVdUcExFLTRvdXhPLWJ5MkJyUFVMT3RMMlFvWjI5ejFPVjBfVFlET0p3RG04enRyd09pMHdpLWFZME94OXFoNHdFdFBJbXNMekRhR3pfcGstVmRWMTBEcHViMDdBaWxSLVRPNHhNUlZLYkRlcE1xM1BoS1NIWmpQUk9zQy1oUm5Fd1BOUWkyQkpGQnF5YUltUDAwS0tEYnJ0c2hkNVg5ZWFGalpxTTU4V3JyU3ZVc3MtazFJeXdkVnhHNA?oc=5) <sub>Stocktwits</sub>
- 📰 2026-10-21 [Mobileye cut to Underperform at RBC Capital on ADAS displacement risk](https://news.google.com/rss/articles/CBMiuwFBVV95cUxQbGV2OURKazdBc0c3ZlkwTDg1aDBENU5uN0ozYXRaQTBzWnNyX2hEWjI5Tm9FSDkybXBsVHFnNjJHaW9OaGg0NUsxY3Qzd2dKRUx4eUhBSW5EU242VVEwV3lKU3k3ZkpGUFpYTzdVNnhXQjVzU29YTVdCYndDOElCQkNVd2l6RzdkQ1ZyMHhsc19TQVJVS29kSmtoaGFfZkhxWkZMWEczLTlvSk1Ga2pwUWdBLTgxd1BnUmE0?oc=5) <sub>TipRanks</sub>
- 📰 2026-10-20 [BlackBerry Climbs 6% as QNX Royalty Backlog Tops $1.2B; Aptiv Edges Higher, Mobileye Global Holds Steady](https://news.google.com/rss/articles/CBMi3AFBVV95cUxPWk9iSUpIeHRDOXd4T1NSYnlfYkJVNEJaLUlONWpKSFBPdFhsVHhGMjN2VDRBeS01ZDViX3E5ZWQ3QUU5UGtZUDFfZXpkenJfZHREZXhOZGMxRVM2MHloMGFheVZkNTQ1b05xRHFWeG84cXFIc2x2NjJYcDZaRkEteExDTk5iTnBxRGczYWtGaWZ0U0pIQmVpNVEwajJwS3ZzZ2ZYQV9UbUJ0OWwyVlNDWlFqZGtsUTR0cHpnd1hqWk1yU3VwMllCYTIyLU1XcnNBOFJEbE5IU0NNQnNo?oc=5) <sub>24/7 Wall St.</sub>
- 📰 2026-10-19 [DoublesAI unveils CEM AI model to cut computing costs by up to 67 percent](https://news.google.com/rss/articles/CBMiuwFBVV95cUxOUWExeFBKN2RaRFduZUY3UGdHZXNjdGxEWklyRnByX1oxcWhidEdUbjlnbTlQQ2tRMlZkT2NCazZkTC1wZTJtVEtTMWhhOUl0cGVOSmstdllLa3N2UVFsd0lQM00yVmg1THVKVVF1TlA1ZXkzY3FIZGVZR1lsOHNucnhCcEdEcTB1cS1LbDZ0aGxuQjJodzd3VE9md3MxZzQ2aG5nbGpybnRKN0FQR1ZXRG92TDVoR3dGU2VB?oc=5) <sub>디지털투데이</sub>
- 📰 2026-10-19 [Beep Begins Testing Autonomous Vans with Passengers in Orlando](https://news.google.com/rss/articles/CBMinAFBVV95cUxQYjhIdjZwdXJCellJZVUteWZIQkgxZEJoN0tldFEyV1pxTVNyRlh4dzJsV2NKOHd4UzNxa2YxLTJQQk1qelA3cm9rVWU0VXJCZ2R1Q3JNbW13dWc3ejVoZk1wX3NEN1VodFZTS3ljVVBHX2JXTmRvdTJDTkpwTXA5MVphMEliRnhxX01yQTg1d1ZkN2JiM2xfdmhrSTI?oc=5) <sub>Future Transport-News</sub>

</details>

<details><summary><b>Aurora</b> (62)</summary>

- 📰 2026-10-20 [Trucks at ATA's 2026 MC&E in Charlotte, North Carolina [Photos]](https://news.google.com/rss/articles/CBMipgFBVV95cUxPZENwSTBGNU9tanAtcTRjaWtSSFlRQUVyMnZTVEtDVnVmR2E1SFEzVy1JblNObU8zZGVfUXhMMzcyUDhmVEhNVENnVVgtMXZvOUdicXJBZjQ1RmVjc3c0bng5bkNsWDdZSGxxUUI0NTIxWmN5UExQMVJkcVc3SEhWbnlXUU5MU1owWVNMdWNuZUU3VzlkN1huT3J2bGRsWVlzQ2JjcHR3?oc=5) <sub>Heavy Duty Trucking</sub>
- 📰 2026-10-20 ['Driver shortage' narrative returns just as 'driverless' rollout accelerates](https://news.google.com/rss/articles/CBMizgFBVV95cUxQX0RpNzY2SUs5VDhqUTdjMGs2aU9WemxXOWdaSWlXd1A1ZHMwQVNEY2liX1RFNXJkUThKN2hsSnpJYVd2bE80dzFVdjU5enVubzhNYWREQjNaakxicy1rcmc2eTA5am1BeGg1OWpydDIwSkkwQkt1dGNhcDFSblg5Q2pmd2JvaV9QRzZXQ25XZXJYYmMyV1h4YUpDVU5UOVd4dzk1bE9kd0RSaDItY0lyZ2V0T25Ha0FmMUlWVDFVRG1nVWJNTEVoN2pGNDhOdw?oc=5) <sub>Overdrive Magazine</sub>
- 📰 2026-10-20 [Innovators With DFW Ties Claim 8 Spots on Time’s List of Best Inventions for 2026](https://news.google.com/rss/articles/CBMirgFBVV95cUxNOEtiZzNjMno1aGE3blZzMktscFNrWkVJUkFCcTRsOVZ2YVhBTEtXZU0zWXVZWkhGaFh5YmloeGZVSldTV3dCeG9fTFF4MGxPTy0xNzVWenRxVmIyZVdlaVlJcHNxZkFHemtBR0tNV0xuXy1Jd0FsOFJhOWdKTWlrWGY5Y1M1b3VkdFZWQnV6SHVJS3ZRbTF5azdLZjloM1RVS1RjbzJubkhLOExoSkE?oc=5) <sub>Dallas Innovates</sub>
- 📰 2026-10-20 [Why driverless trucks could beat cars to full autonomy](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQa1dHQzdxRjBXVG1HclhGY1podk5HWmxWd25rbXFlYXJOOFpLN093Z0Z1MHplTm1zZWJIRkRJNEpWZ05DYU9jN255QjFuX0lmTUhhYjl2dFhhMDFfektpN0ltRDV4cnFRNUluT3ZvcnJsdFVYTUtyaS1kN1FsRDVjRE1XU1k1a3ZvdVlaUGF4VTIxMkxpN0otRkpTSnZvdUktSTI2aWI4S1Bsa0E?oc=5) <sub>Korea JoongAng Daily</sub>
- 📰 2026-10-20 [Where a robotaxi can drive matters more than how well it drives](https://news.google.com/rss/articles/CBMicEFVX3lxTE5YWGNMWXc5end0dEFzMWJvc0NzVjV1eXpxMGI3YkZFMGdSbzVJWVJld3g4eDJ2TWJGWmtFeXpsNzNEQTF1Smp1aHVOYlpqV01QM2ZWM0cwMG9nU0xrSjVtSjJlSE11M09xOTQ5eFVfaXI?oc=5) <sub>Cubic3</sub>

</details>

<details><summary><b>Zoox</b> (63)</summary>

- 📰 2026-10-21 [Yomiuri: Japan's Carbon Fiber Manufacturers Expand to Robotaxis, Space](https://news.google.com/rss/articles/CBMixwFBVV95cUxQNzg3LUNDWl9vekhpc29xRzFXSFVmbHZ5anp4RnhOVUNma0hVZE5hNUtzczNRR25CSVRUWGlVdEFLMkVZcDg0R3lqbXBEWDdTSGFVUlZDdGhwSEtsSkRvZURYWDFfOUxRSGdYMDhGQVlaQTBZcDFxa2pXcU8zN002RUNJOE80LTFIR01TNzZfU3dWelRPSFphVDFVa3ljbDh1SjdBRnRUX2lNbUtzQ3MtenZUVFY1TUtjZEtnd0RDNkd5SHVsU1dZ?oc=5) <sub>MarketWatch</sub>
- 📰 2026-10-20 [Alibaba Backs Chinese Robovan Maker in $400 Million Fundraising](https://news.google.com/rss/articles/CBMiswFBVV95cUxPdHJFZ2hnVEF0QmdfZ2Q4b09uLTBrTHpjT2pMODJ4Z2k4WlNoT0xDakdJUTdpcEJWR1FpbzlvRHNzRE5ZTWZ2bkxXVzNVQl90YUJTdnVybURmb01WZ2lyTWxrbHF5Q2JEbi1EZ09IWFVMeUVQQnhYUHZXLXJzODZOandZd3pWa29WZnJrTm84T1BLcHUxSUNrWUhRNHBFWGt6aU5ha1dKYzFtaS1YQUtkWTBEYw?oc=5) <sub>Bloomberg.com</sub>
- 📰 2026-10-20 [Self-driving taxis are in Las Vegas. Now what?](https://news.google.com/rss/articles/CBMioAFBVV95cUxPc1hmeUZ2WXAzUDZhUHpPV05nc1hLMWcxSXE3bVFvX2FUdmtkR1g5ZlVqU1Bpd1F2aU9TVGhLSlhBaXZLR3hWTVhQUG4xZEZmNFNMQW9YWUpVNlFoV0ZNRS1RTUJzTXlTcEtHQ1hoMmY1dXhReU1qZ0lrOXkxMVpvVmZ1Z1pJUE8wRmRFUGRCY2FGTFpUTUphd1FLd3pRSGhz?oc=5) <sub>KNPR</sub>
- 📰 2026-10-20 [News \| Amazon robotaxi unit continues San Francisco Bay Area real estate rollout](https://news.google.com/rss/articles/CBMitgFBVV95cUxPLXh3cC0xSno0NUFENjVEQkZQalF0anhXaWQtSnJVcHhXYjRsZTExM0dOMnFWVTdWMkhxNDYyeHZOT2tacjgwWGdVNkppMzhZTkNSNWNSQWZROEw5OWNfeHNsN0RxdHZINEpxcW85SkhYdjNLWDhGUkxHS3dRS3VGcm5HMzlIUjBTSGt4cHlPcU1PTmYwOUExSEtkR3RlNmZqZ3lSTlNtTzVvLUNVcm9NcE84eVc2Zw?oc=5) <sub>CoStar</sub>
- 📰 2026-10-20 [Nevada Regulators Clear Commercial Permits for up to 8,000 Autonomous Taxis Across Clark County Roads](https://news.google.com/rss/articles/CBMi0wFBVV95cUxOcGtCVnZma2hRb2xkLTdtTW5NZFlhNGhhVjF3X0VXa01WVzZmSkw0Ylo4dzVFRmRNREkxUHd5ak5XVHZhZHctTDJnRlc5SFVvV2xJNy1zTlBpMkp1b0RvandPb29lR3I3Y193QUV3Q3EwRkVDY2hvNDFOT3dJMkkyblJmaHBZWVJMRXJSUlJiMUo5Yk5EYzdFUzB4OHlxTkNoSTNlQV9CcW1lWDJaLUJkM0cxX2RMSHZ4OHFEdTRmWmF3QVNvbHhQQ3NZSk9hNnhESk9V?oc=5) <sub>Nevada Globe</sub>

</details>

<details><summary><b>Motional</b> (23)</summary>

- 📰 2026-10-20 [China's CATL posts 14.54% rise in Q3 net profit to 21.246 billion yuan](https://news.google.com/rss/articles/CBMidkFVX3lxTE1VaFpob2tDMTR0dDMtMmNOcks2V1M4V0pKWmltNTY3VmRZNE43UHZxaHRRQW9hOVVjWWFzVkxWdmlpaDRoWUVuN0xISzNUVnZsMVVYU05CMWx1ZDctS1EtdzhDbVVqS0laSGJDbkFtRExycnJRV1E?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-18 [Hyundai Motor moves to sidestep self-driving fallout in India](https://news.google.com/rss/articles/CBMiugFBVV95cUxNaXZ0YW55OGwzWnN4XzN4Y3YxeVpDQTJKOExNM1dmWkRSbUpjaUhhUUd5T084cnIxY3VSNzB6TzNSMjRreHJfN3l0VEt4b2VSM1lpanRUY3dDTmRNRWxBeVdwdlBCZGFMcWVHQkl5Yk9ReDgxbk14RTVmN0JNbU5RTWwyaVJ2ZTBRcU1Bc1BBai00eXNHMExxb0VkNEozUGl0dlZtT1BpWTN5M2dmbkZtZlI4ZEQxc3hibnfSAb8BQVVfeXFMTjY1OFZ6b3Z2S2lxd296ZHE0VTFpaHYzeU01bmZkSGJlSi1kbDRjWVJZLTl5VXhMVWRNVUxjeEg0aFdUWDg4Ukhhc2NYNkZ4dUlPQUFHeGtlRnB6QkotMDZYcXN3clRwZWduT1RndFg5WGZYWXlHQkZpUEZhb3NXNjlPYUZxRVVFcXlNTW1wWVYxUHhyWWFKbmJ3c1RsUk8xbnZmb2FIYW1EejBzWGdpNU5XT1R1dThfbDFaell0czg?oc=5) <sub>The Korea Times</sub>
- 📰 2026-10-18 [Hyundai Motor, Kia to Deploy Humanoids in Factories from 2032, Unveil 'Autonomous Operating Factory' Roadmap](https://news.google.com/rss/articles/CBMidkFVX3lxTE5BSkloNVFid1JrenR2b2g4a1N2OXI4SVNYQmRvMW5wc2lHS0Y5TVUzVlRJTjd0Wlo4UUFmWDA0U3hQTmFxOG9uSF9oOC1TMGs0cV9temVoeXhzUkx0Vzg3ZU5qNDJXRnJTb2l4VXg4U195Q2U3R0E?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-18 [Hyundai Motor, Kia Unveil 'Autonomous Operating Factory' Roadmap with Humanoid Deployment by 2032](https://news.google.com/rss/articles/CBMidkFVX3lxTE5BSkloNVFid1JrenR2b2g4a1N2OXI4SVNYQmRvMW5wc2lHS0Y5TVUzVlRJTjd0Wlo4UUFmWDA0U3hQTmFxOG9uSF9oOC1TMGs0cV9temVoeXhzUkx0Vzg3ZU5qNDJXRnJTb2l4VXg4U195Q2U3R0E?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-17 [Grayson Brulte: Waymo Will Launch Driver-Out UK Service by Q1 2027 as London Permit Becomes 'the Keys'](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9VUjFlTTg4T2NGVlQ5dlIteGN1RVVNOWV1UTVCTEhGU3poT1FHOFN6VjB3VU5QX012ZEpaZ2RNNV9RNkRuV2hmQkxTY2EyN2FjanZhRVpPczBLWTg?oc=5) <sub>BigGo Finance</sub>

</details>

<details><summary><b>comma.ai</b> (4)</summary>

- 📰 2026-10-20 [2400 miles with Comma AI, Android Auto, YouTube Music, and other various tech](https://news.google.com/rss/articles/CBMisAFBVV95cUxNeUNQVTFnMUoxMUpGT080WUdQMHlSVTBDdWxFM3lGRndwbmtZZnZGMVFZRWpDb3JoZllSVk1ZaUFCUHM0TmZTeng1bXlvQUJ4S25rSW9uZFljSExya0FPblRsMTEtZkUwWVhyM1ZqNkx1V01jbFBqdURfMlU5TmJHWnVqQV9aWUhrdUhCa25PN0tRalctSmpWYUkzOGVJUUxxUmFIeXIyczRlVGhqUVFIcQ?oc=5) <sub>Pocketables</sub>
- 📰 2026-10-20 [Auto tech startup claims it traced hack attempt back to rival's IP address](https://news.google.com/rss/articles/CBMizAFBVV95cUxOVHlZN1E1cDJqNEFHSFg3U1hCbnZRdFhtdk11blVLd2d2dUNIVkYxUG1xd0NIWjdNZGNVMHJvalh4SEM2cTJhclMzWHRyR0thRWJDMHFNUWcwNHAza21ybFYxV1Zyd2ZoaHRORmRtdGxBbWlSWk1UUnllQVp2dGFCVlFjcE0yOG1OaW9hdGhRb0lpS25LeUZFc2pKem5QaGVnZ0pLNExzeDdUOGNERVM2andndkh4LW5JWDdaSGhqQmZxOFMtb283aDFIWkE?oc=5) <sub>The Register</sub>
- 📰 2026-10-07 [Researchers Find that AI Models Struggle With Even The Most Basic Driving Skills](https://news.google.com/rss/articles/CBMiuwFBVV95cUxNb2ZGRGxGZDNjLWU1OVBPNjUtUlJXR0hiVGV3WEJ1eUVnSWExMWVvRmJjX2NtQm9sX0plMTU3YzZwUm5ZTzVoSGttcXZmQ3BqbW40X2doNFMycUk4UWE3anlidy1vWHNYZndVZjZWLUYtbnlHeVBFRjJOaTF4SWxzbmotR0xsNkVIcEhfZ0M3LUs5R2FyV1lVdlRRU3JwakpQcXpBUzlEOEhsWlB3Q19EdXFhQjRvZDU5MHln?oc=5) <sub>Auto Spies</sub>
- 📰 2026-10-07 [OpenAI's GPT-6 Astra is the only AI model to finish a real-world driving test in a Toyota Corolla](https://news.google.com/rss/articles/CBMifEFVX3lxTE9iZmN2ZFp6blVBRnZUTkYtYTJ3b0hSb0xhQjZyQXh5MUN2T3ladUlEb1F1SWJzc3FtamZtazk4LTVUWVpNX0ZjbGZwMnpERk45TVVQWVA1RjBZVUxxTTAzTWpaV1JqUzIwM1I2Wk1tTzc3bDJpaWluc2JVam4?oc=5) <sub>Crypto Briefing</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
