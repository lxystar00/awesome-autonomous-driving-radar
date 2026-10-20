# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-10-20 · 1,302 papers tracked · 41 curated.

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
- [3DGS / NeRF Reconstruction & Sensor Sim](#3dgs--nerf-reconstruction--sensor-sim) (3)
- [Perception: BEV, Occupancy, 3D Detection, Mapping](#perception-bev-occupancy-3d-detection-mapping) (8)
- [Datasets & Benchmarks](#datasets--benchmarks) (2)
- [Safety, Robustness & Evaluation](#safety-robustness--evaluation) (3)
- [Industry Tracker](#-industry-tracker)

## VLA / VLM for Driving

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Teaching Vision-Language-Action Models What to See and Where to Look](https://arxiv.org/abs/2607.01658)<br><sub>Yuguang Yang, Canyu Chen, Zhewen Tan et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 34](https://github.com/ShivaTeam/DriveTeach-VLA) | Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving |
| [DeepSight: Long-Horizon World Modeling via Latent States Prediction for End-to-End Autonomous Driving](https://arxiv.org/abs/2605.10564)<br><sub>Lingjun Zhang, Changjie Wu, Linzhe Shi et al.</sub> | ICML 2026<br>2026-05<br>📑 2 | [⭐ 31](https://github.com/hotdogcheesewhite/DeepSight) | End-to-end autonomous driving systems are increasingly integrating Vision-Language Model (VLM) architectures, incorporating text reasoning or visual reasoning to enhance the robustness and accuracy of driving decisions |
| [SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving](https://arxiv.org/abs/2610.20609)<br><sub>Shaoyuan Xie, Zihan Zhang, Jingxuan Wang et al.</sub> | CoRL 2026<br>2026-10 | [⭐ 21](https://github.com/ASGuard-UCI/safedrive-vla) | Vision-Language-Action (VLA) models are gaining attention in autonomous driving, inheriting commonsense priors from large language models (LLMs) and widening the navigation interface from a fixed command set to free-form… |
| [Scene-Adaptive VLA: Efficient Autonomous Driving via Dynamic Layer Routing](https://arxiv.org/abs/2610.24590)<br><sub>Yujia Yang, Quan Yuan, Jiawei Fan et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 0](https://github.com/yang-luvu/Scene-Adaptive-VLA) | Vision-Language-Action (VLA) models offer a promising paradigm for autonomous driving |
| [CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving](https://arxiv.org/abs/2607.04179)<br><sub>Zhaohong Liu, Hao Ye, Xianlin Zhang et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 1](https://github.com/MICLAB-BUPT/CritiqueDriveVLM) | End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving |
| [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)<br><sub>Nan Yang, Zhanwen Liu, Linfeng Zhang et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 11](https://github.com/Zizzzzzzz/MVPruner) | Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings |
| [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)<br><sub>Yuan Gao, Wenting Miao, Mattia Piccinini et al.</sub> | IROS<br>2026-07<br>📑 1 | [⭐ 28](https://github.com/TUM-AVS/Chat2scenic) | Validating autonomous driving systems requires diverse, regulation-compliant test scenarios |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 10 | [⭐ 517](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
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

<details><summary><b>Waymo</b> (225)</summary>

- 📝 2026-10-16 [Hello Toronto! Waymo is En Route](https://waymo.com/blog/2026/10/waymo-in-toronto) <sub>official blog</sub>
- 📝 2026-10-08 [Sober Drivers Still Face Nearly 4x Nighttime Risk: Why Road Safety Demands a Safe System Approach](https://waymo.com/blog/2026/10/sober-driving-benchmarks) <sub>official blog</sub>
- 📰 2026-10-20 [Element Expands Waymo Partnership to Support Toronto Robotaxi Fleet](https://news.google.com/rss/articles/CBMiqAFBVV95cUxPZmMtREhhMTVJRHhtQWRLQnBRTEp3ZEJ6N3l2d1RlZHZvRzl1VkRtWU53VDlZVnlPYkFwODhkYXpLTDR3N1Y1b2NZU1VSakZDM1dnSWxEUllzMzktNmpQZWp0LS1heUtrbGFMNUZveWtHRWJ2UlVXRVVhcUx3U1VhaVhNYk1Wc2JfMVYzNFNQeFUtUE9WS0ZKTFd3SjkyRXZrNFd4QVNkNWs?oc=5) <sub>Automotive Fleet</sub>
- 📰 2026-10-20 [Waymo to bring fully driverless ride-hailing service to its first Canadian city](https://news.google.com/rss/articles/CBMid0FVX3lxTE1uXzlXSUtyUERjQ0dpOEJlNWN4QjZVZmotOVBzQmhXa0xfQkZQSVZOSENZSnV2OENpNDFNbFhPU0h3VVBvQVJmQnNJdEtNTGd0OHhBODEzX0ZUWXNiTmd5cWpwaERIdjlRaGxEWnFXVVlYYmIzLWtJ?oc=5) <sub>Daily Hive</sub>
- 📰 2026-10-20 [Waymo Plans to Quintuple Fleet With $5 Billion Private Debt](https://news.google.com/rss/articles/CBMikAFBVV95cUxOVy0ydmJQU28xSVhQVFJTZFRqVGw4ck1xNkU1NGIwV2ZZN0lNWWdxQ1cyTjBOVnM4TVV6dGJNUzZIcko5TDVSOTAyaVEybnNCUENpdUplRDh6SXphanpULXBSWlgxQzk5MXdoOFZmYlVIenhrdGo2UzYxYkktM0NhNkJXV2VYeE9lQmRCZ2ZXSkM?oc=5) <sub>news.lavx.hu</sub>

</details>

<details><summary><b>Tesla</b> (355)</summary>

- 📰 2026-10-20 [The Boring Company’s latest Tesla tunnel truck mod “fits like a glove”](https://news.google.com/rss/articles/CBMie0FVX3lxTFBBWEJmaHJ6UTNEWS1fSEJBcUoySmVJVC0zelRPY3I4SEl5LU1zZWRFXzVoZ3ZVUTlwd3JkRERjY09kbE55blNQeTYwVmVQSWJQYl9vU2VHRXEyck10VW95RlFidFdMSGV2RFMxR2RUdFlSazlVRkJaUG9xYw?oc=5) <sub>Teslarati</sub>
- 📰 2026-10-20 [特斯拉Semi重卡路测FSD 2028年或上路](https://news.google.com/rss/articles/CBMigAFBVV95cUxORXVGQWQ3NWpJc0IwSkdhSVJ5YzNMQ2FSNWU4YV83WXlZTkZkM2RRTGdVUkUzNFBWck1LaElUX3dxRl9TZXAtTDlnRG5yT2QxTUUzSE9XWWZzamRDaVBwajhHLWZJNUd6RFdPdHVlaURoaWxPYksyZ3pzN2dubmNtSA?oc=5) <sub>新浪网</sub>
- 📰 2026-10-19 [Tesla FSD and Autopilot: Features, HW3 vs AI4, and Subscriptions](https://news.google.com/rss/articles/CBMidEFVX3lxTE1Fa1Jpa0YzLUtUSXhXbkdzMTFVdlVmVWdWaU5VVXljMlNDcDBUQWFxc09pNFZpOXdDMU16ekRycjRFcUpkakpTWWZnY2RzcGQ5eUJlZ0FBc1RGaml6VnpuSTZwN3J5YWpESzgySThXbmZIWkQ0?oc=5) <sub>Drive Tesla Canada</sub>
- 📰 2026-10-19 [Tesla FSD Showroom Trials: 5 Details That Matter](https://news.google.com/rss/articles/CBMiigFBVV95cUxQQ0lIVGs4c0xHQWpqS1dYQ1h6NEJORldvZjY2ZmxLYUtEWC1KVXlxSjZBVkZMRHBDT01pekpJblB0cFdfVVg2U0ZqdE1SbmFmWWpXUkc2Z3M5TzZ2a2Y0MkRQN0tsdkdVSE9kRlI5UWh4MmhSSkE2QzdzOWRYYmJmZ3NiMjMxZ3NBZWc?oc=5) <sub>BASENOR - Tesla Accessories</sub>
- 📰 2026-10-19 [Tesla's FSD Trial Pop-Up: 5 Details That Matter](https://news.google.com/rss/articles/CBMihwFBVV95cUxPUFJ6cUttbFpqXzJMUWplQXJxSFBIWWtKMDhtRzlVVVFHX1VTejNPQVdkNmtWRm1Sb2tsZ1RpSnhSYWU5emg0R2diZ2tvYTFXcmQ0S01iNUJVc0JZa2s5dDZUWmlzLWJZVG1pdFNYM3BpaDdReVdCUGFseW4zMnV1VEt0NFljVGc?oc=5) <sub>BASENOR - Tesla Accessories</sub>

</details>

<details><summary><b>NVIDIA</b> (237)</summary>

- 📰 2026-10-20 [Volvo Expands Partnership with NVIDIA to Develop Next-Generation Driver Assistance Systems](https://news.google.com/rss/articles/CBMi9gFBVV95cUxPamFENURJNWtpbXk5bXl2MWU4amVJRUJKemZzLXJsakNxNjZENlphdkJXZ0ZiN3F2UDlXMEVra0Z6SXdLRkk3NnRlSGd2WGV4YXNIekxxWExQRzhHZFF1NlpjN0tSQW83WHdoUXlFU0xOMl81ZVlhRWl0UG9HdXR1X1duQ2JRckQxX2hUNHdCR1NIcnJ2UENQQlN1QUUzT3VTdU94UHh1S294di00Rm5BdXdiNVNPLU9abGZmM3IzU2NLSzUySnI1cFplRXZUYUVhQmNuZDJCSC1DZjlmOFlnWVlaVEtJaGJid3JSQlhaenJQZnRTNUE?oc=5) <sub>Gasgoo</sub>
- 📰 2026-10-20 [Nvidia, German Ministries Sign Declaration to Develop Industrial AI Models](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBDT1dONjlDR00zX2ZfMktFaVhZU05PX0NlbGZhd2hkVUw5YUhZdnhxUnRwYi1rY1MwXy1NYl9KUnl4Z1d3RkJNanBjaWxtNFhLNHlNdHctNzVscVE?oc=5) <sub>www.tokenpost.com</sub>
- 📰 2026-10-19 [Nvidia Shield Running Slow? Here's How To Speed It Up](https://news.google.com/rss/articles/CBMia0FVX3lxTFBaQjZnT0t6cmt1YlR6R3JGRlZRbWdlOEpKVzNKWmp6b1J2X010YUFYRENiSEMtajN4SEx5NTVlbDhDWHBrQmVLRUFZX24taUdHNnprQjh0V2huOFBmZGRER3BSeU55bkoyWm9r?oc=5) <sub>BGR</sub>
- 📰 2026-10-19 [Volvo Cars and Mercedes-Benz build next automated driving systems on NVIDIA technology](https://news.google.com/rss/articles/CBMi0wFBVV95cUxPLWVBZ3RmWDR5RHROcV8tNXJWT0xsX2luUVZCX1RkUDVkUEJuSHNlbXg2cWhDNjIyZF9yVk5zU0g1a1lXX3UydHZVQWprdGhGazc3TGRod3FSbUEwVTFnWEZ5ME1NVkZqVkV3X3VvX1ZmVlNheEFYbzVPeXk4anhBVUx1MWowY0FBRkJmY2JQMDhfVHh4N2lsZXF1WlRjOUFaNi1XRFNJVGtFckR5QW1nNWMwNzNTMUdSUlMtVU5qblBhOUoyVHFHeTVBalJ5TVk2clpj?oc=5) <sub>EV Infrastructure News</sub>
- 📰 2026-10-19 [Nvidia CEO urges German manufacturers to adopt AI, saying digital tech won't replace heavy industry](https://news.google.com/rss/articles/CBMi2wFBVV95cUxOemVEYWt3Q1dFbnBkVVhLSVNLcWwtLVR0Y2dXTU53UnE1dGV6M1N1anJnUVBsVzNmYUtfZTBKV3VvSVJuMldVenpscVZoMllEQkItZUd1WkEtWDQzZVVXQUo0RHFZUFhUNlN2RDdqNlZ5eS1tSlN4MEpfdW9RcTdORWNmM0tFdnB5OHFnQ1o2ZWxSemY3LUNqR19aNjE5SzBaOVRYckRMc3cxMFZ4Q0JxdGNEWGZaWDh1LWIzeWkzN2oyMzF5ejVxSzJLdHFjSS1fUEFNeEt5djVLd00?oc=5) <sub>Audacy</sub>

</details>

<details><summary><b>Wayve</b> (65)</summary>

- 📰 2026-10-19 [End-to-End AI vs. Traditional Self-Driving Systems](https://news.google.com/rss/articles/CBMifEFVX3lxTE1KcWxyOW1pbFVjVUxIaXZ3NEl3T0J1ZV9BTzFLWmV6bnF6cDgxRTJlamZEZjB0ZjEwWkJZUHdkMFFVUkhpcUNRd1plX2F6d3JhTmhqQ0R5MVlvbzI5bG1nRWtDamVEUnQwNVNQUkRwNVFERGQ5NEdZeDNONkw?oc=5) <sub>HackerNoon</sub>
- 📰 2026-10-19 [Driverless cars are a progressive cause](https://news.google.com/rss/articles/CBMia0FVX3lxTE5yZy1KVnFVMl9PamtVTDlBWkFxaXdzaEpIcTI4WnJsbmpCRUVvVnA3ellWZ1k5bUNnRlhjUnMzcnZRcFF4UFNoSUdVMnB1TlZ2ME5GbXVmSDNpa29vNjBqdXp1cDBjVGIxcDZV?oc=5) <sub>Arguably \| George Eaton</sub>
- 📰 2026-10-19 [London's new self-driving taxis spark safety and traffic concerns](https://news.google.com/rss/articles/CBMirwFBVV95cUxQNXk3M1FmT0NlRGxZWmRFT1FocmF5SzlPWFFEUng0cWdvbGtQZ0NwRURsV1VYUUJYMW5Ib08wUUMycWlWWC0xVlZhX2J6U3E0VTZUZUM0TFhPb05BYVNkcFdDN3NFQ2tIdkV5T2pQWW4xbHljS3Zid0k5VVdpaHlaYzM1NlJVcG1fZkw4enRyaTVqMGVobl9URDAtT1lrVGlNVzRxNHd4UEtUY1A0YkxZ?oc=5) <sub>Autocar</sub>
- 📰 2026-10-19 [London black cab drivers’ case against Uber thrown out in High Court](https://news.google.com/rss/articles/CBMidEFVX3lxTE1jbndEb3FDNFBYU0k2ejJNbVNXSVpIMmEzb09uOWM3elZfYkJ5SWxoakZndE5mM1VMbEQ3b2dQbnN0OVJ2Vk9GRVQ3dWRmU08tLTg1NlB5T2lHcEFPdDZFN253TndxVWdFaWc4NER1QzkySmFI?oc=5) <sub>LBC</sub>
- 📰 2026-10-19 [Uber beats London cabbies in £340m court battle](https://news.google.com/rss/articles/CBMiekFVX3lxTFBmYmdSOWI5TnJnSDN3TkVDUlhzMlZvb3VZd05aSnYxRGp3RVdVdUJFaW1UbDV6dzA1ZTRBQU1SQlhETHJEaGgxUFA0OFJNM01YNVpNX1lDRzlIRkZmUnhpRC00Zno3aWQ3cDk5RENEN0p4N1h4c2J5S21R?oc=5) <sub>City AM</sub>

</details>

<details><summary><b>Momenta</b> (91)</summary>

- 📰 2026-10-20 [Asian Growth Companies With Strong Insider Ownership](https://news.google.com/rss/articles/CBMi2gFBVV95cUxNbmZlSUEyX0MwLTRiYUVTYy1qMmZkN1NmNTB6b3VnOU1hS1ljOWx6a3N4NDFmSENvNUtTNWhOUXhqcnRoVDVBYk9nLUlnVjdTNkhJb0RNaG45d0hkMjUtdmpLM3RDY0pMVy11NFh5ZzRZeENDWHFqUU80OXpEc1JtZzY3OHI0SHpnV3lzLUNTVzNnZFRmWkJfUWR3S2NZckVVdXFyWnAtbHFyd3FpU2xLOUFWUmZhdm9NQks5bkFDX2swZm10enppSXd2QTREZS1VTE1sSDlqYkFFd9IB3wFBVV95cUxOQWhqWVF5UGt2Mk1XaVB1eTFzcjJYSzBMenk0VUFpLWl4em0zdTZWaGlpZ2hmX1JaLTMtZy1sUENhN2FPeGxXdmVqdENMc1l5UGxJYS1SZHhhTmZIVS1uVkJfVS1HdjFnM1NVUV9qTmZHaXRUSkVmOEZ1dWdmQzIzNDRuWDg0U1c3QU5rdlduS3gza0hVQTdTNTJON1ZjNXdXZUxnbDZGam9zYlNFQVpjek9WdnRUbkQ0cVNxR0k1OFJJeFo4YmRWSTZvUkdnbzlmQ01xTFFuOHI2VV9Ja204?oc=5) <sub>Simply Wall Street</sub>
- 📰 2026-10-20 [带激光雷达的豪华插混SUV哪款好？全新XT5 PHEV、领克900与腾势N9智驾算法横评+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE15MEFrYklyUm0wZUU4Q0hwN1JOYXd6anNjcGtPSk9MWkhqX3Z3S2ZyMTdZRHc5dEFGVHdzR3lCdmVpWmxpYlpmTHVKV0FvVHZmOUEwajZVUUFSb21zWVRPMGN5Nnp1dnhLMWZYTnZBOFZFUQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-19 [北京现代艾尼氪V拼了，能否撬动新能源车市场？](https://news.google.com/rss/articles/CBMijAFBVV95cUxNSEFPNHN0QW45Wl9JamgzcFNtMS00T1Z5anJsUEYwbU9ocF9HX19kSVJHQVhQWjEwY3oyR3g2djV0blFCckZpR2VXcUktRXllYnFTYXVXU1p5YXlyNUZmMWZyNjhka0pHbkFuU1JucFlWVV9fcEhEVS1VNE1wR2RVbGpqM1AwQWVIYzZMTw?oc=5) <sub>搜狐</sub>
- 📰 2026-10-19 [Momenta R7世界模型上车奇瑞JAECOO 7，无接管征服巴黎凯旋门“魔鬼环岛”](https://news.google.com/rss/articles/CBMiXEFVX3lxTE5QWkozekt2dm9sX1BzVXFXNXV6SHRVaDJjSTZmdXFmQ19CeWdCdW01NjFQM3pzMERuaXRXbjFXOFpBTUN2bm04MElfNEhqSjNsZksybTY4YjlZRUpG?oc=5) <sub>网通社</sub>
- 📰 2026-10-19 [东风风神L8+定档10月23日上市，激光雷达+Momenta智驾加持，15万级插混SUV要掀桌？](https://news.google.com/rss/articles/CBMipAFBVV95cUxQRXF4WnB1YXdMaXJaVE54THQ1RTNyR1JYYkJxUVZ2YWpzWHhNMUt3SG1ORk1fYzV1aGE0TmVJUzEtdmY1MFNrQ2Vob1JvR0lqZkYyc0txQkN0RW5JWTZyNWNSSElHeXVCZGhYdmhIZFNpVUpkckxwdklnRnJzTUp5bGMtdTlTVW1EX1ZIR2VDQmZQTjVOWUR1TklCMVRjVmRKMHVOeg?oc=5) <sub>搜狐</sub>

</details>

<details><summary><b>XPeng</b> (304)</summary>

- 📰 2026-10-20 [Volkswagen bet on Xpeng to save its China business. It's not going to plan](https://news.google.com/rss/articles/CBMihwFBVV95cUxNQkN3WGxnLXN1c1dZQmFDSXFjTDBNbHdheTdOX3RGTjJyT0pXMzM3aFJ5ZDlRZEVGMnVnd2lfa05rU0VkbmlmTC1DanlrNkFqanNPeVd5Qm9pSEdtWlZYbWw4LW5OS3dTM3AxWUFoSW1tZEE4aFJwOVYxd2ZpaWRQNk9yQWJZZmM?oc=5) <sub>Yahoo! Finance Canada</sub>
- 📰 2026-10-20 [小鹏MONA L03值得买吗？15万级智驾天花板，3个维度说清+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBfdHJSeklkTUxFcnBpTG5nOXlNNmVXelRyNW93SU9FZVJFc19SZmdNMF9USmtXTmh3QTBXUUdmQVlLOE9KNWtiNjd6d0dyTW83bklycHlzb3hwZmNfY1RF?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-20 [25万预算新能源SUV横评：小鹏G9L、理想L6与问界M7怎么选+选购避坑指南](https://news.google.com/rss/articles/CBMickFVX3lxTE95QzVxMTRpNkZLQ2tMMk5lUjFmVkJDQlo1YVJhU0JnOV9fOXdzNU80X1BSWDg4dG1Zbk5CSVc5cHM1eEVUMmtYR29RejhBdU9TUWt0Z1UyRnMwcVNQOU9HQnlDWmZXaGhBZGplOTFqQTJkdw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-20 [【视频】12万起，颜值智能续航空间都给你！小鹏MONA L03哪款最具性价比？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9pR3QweEhTNjFjNk1va24tTGpDYVl2NEZTWXpJY01yUHpmZ1VINGlXdlN5c2FHSnczWGJCY2lGR0I0Y1FXeXpWVnFlbGFUTkF6bDh3TjFNZ0Z2UGM?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-20 [综合1602km加92号油：小鹏G9L与3款热门大五座SUV长途横评 + FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE1CUXZNU1hGTlA1LUFyWmlkRHMyelRvNDNDbVlOdEpZZnpVZkRIWXlUdUszRDJpUGR4UTBYVGlLb0JqbXE0NzNYZVpscU0tN1IxcE5pYlQyN096NHRFWHJKbzJpeW1lZlhBZjBkWW56bGxfUQ?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>Li Auto</b> (148)</summary>

- 📰 2026-10-20 [理想L6后驱增程版对比问界M7/岚图FREE，25万级该选谁？3个维度说清+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFB1eWhqbmdhazNkaldLeXhfbUtzM25vMlVLRFl0SDAxX2FDc1V1ekR3YVBmaXVjb1ZvdVBRNi1uOFFTcE1oYUF1ZVJjZkJhdXFsSHR4aDBVamxvYnVMYlBERnZfQTRHaFQ2WTdzUWtpalBMQQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-19 [理想L6目前价位多少？24.98万起值得买吗？3个维度说清+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE4xOHRCeEFhQ2plZm5XWjZyR2lDcHNXNUJqNkFwWmhSU2tGYk0yTXY2bllMS2tHYTRvTXZoekItaG4xZ1FHVmNKUmZEdUx6WkhzdVpXMkY5X21scU5xWXo3NENwb2oteTQ2bXlPSmNMTTg1Zw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-19 [新上市的豪华插混SUV哪款值得买？凯迪拉克全新XT5 PHEV与热门车型横评+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFBoQTZaV2RvZEhnYzRSdTZFTzZzTF9TcGNMM0xOVUdtQ3JNZEstdlg2aUdmbEh0NERmMEJ6RUR3ODVxSFFRUDV3SElsQjZtUHFva1dGTVJETDQ1RmpPOFMyeGRacDc4TVFOOFdneEJ0cm5UZw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-19 [理想智驾迎来技术大牛：原华为ADS核心成员杨旭光被曝入职](https://news.google.com/rss/articles/CBMiWEFVX3lxTE9LYnB4cF9KU2JpendYLW12SDNETzE4RkNoTUxJQ0paSDJjd2tlYXNRYUFDTTMwNE1zeWMwYnFmR2NXTFBubGlodURJdXgtamlVREN6eFNUNWw?oc=5) <sub>驱动之家</sub>
- 📰 2026-10-19 [智能大五座SUV怎么选：小鹏G9L、智界R7、理想L6智能体验横评+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5TTTZSM20wRUMyU2hMa25DaDhGYVFjaWNxLWhkOHJtanRoemFOdnhSSkZleFNUZ0MxemxURi1GOG9TV1ozWENmSi1PR2JTT1NwdUNkSHhwcmVPVEswUXVj?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>NIO</b> (156)</summary>

- 📰 2026-10-20 [【视频】22年蔚来ES6电池租赁](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9VSUg3WFRLcGJfSlBzdm1PT3htd3JObXpvTE1laTZTWXdEYms1Ml9mSVpUdnRtbUdEQVFHSFJUckJRbS1YLW54bWpobFh1RWN5SXZMbjRKVlJYUUU?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-20 [蔚来EC6 2026款值得买吗？35.8万起这些变化最值钱+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBnSm5kUnl6M3ZGWWFTM3RwS0pmM2lXSHh5bE53WENDbXM1cEYxaWxGZmg3QklLN1N4ZlVhMXpYelNUc1VDR3FxR0Y0bzUtUFl3Q1E3bXpkcXBaNzhFV3Mw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-20 [国产“豪华大型SUV”，车长5365mm+707Ps，压榨700牛米](https://news.google.com/rss/articles/CBMia0FVX3lxTE90dTdSaW5EYk5ld2VHdTZjWGFuX3N4a3lMdjJVRHdBRkVsRE9sa3BuVmVaaUM4UzVFOWdvNEI1cEI3YXFibnB2VlVZWk9rSUdMV0w0UnN0bHFsQXo3bUVLUExzdnVpT3FQOFF3?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-19 [蔚来和乐道的技术底色，智能驾驶在关键的时候能救命！蔚来乐道L80 蔚来智驾](https://news.google.com/rss/articles/CBMigAFBVV95cUxNWVBJaW5wYjc2TlZIQVNvbDhfM0d4ZWEwOWlsYVlfQ1RFekVKc0owUlRCZkU3OHQ3S185X2kyR191dlYycGpNQnZ5a2dSSUNlYjZBMXJjWFhJNWc4ODRzaGd2TzJyd2UyZWlEUm8zQi1udXR1TklaQWJJanc0Z0VPUA?oc=5) <sub>新浪网</sub>
- 📰 2026-10-19 [蔚来15-20万两款车怎么选？乐道L60对比蔚来ET5，家庭与个性你站哪边+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9jM2d2RzVOX1hjUFJyTFlxOUpaWFB1cXBTN1NDTUM4ZVVIWnlWM253cVB3ODlZWW5lekVCcS1MdzV0SUFQb1VIeVZlNnVqNlVuRC0zQ1E0VVBpUW1HWURV?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>Huawei</b> (349)</summary>

- 📰 2026-10-20 [EPICLAND X9 Steps Up Deliveries as Zeng Qinglin Emphasizes Quality](https://news.google.com/rss/articles/CBMixwFBVV95cUxPRVkzOGdhT3ZBdkZJcW9yNmxpb0t6SWxuTWNMVElHS0hZXzJtaUlnS3BYSHVpUlloMWFuYURBa2NLalZyWEdlM2kyZEExZWltSFdsY0RsbzN4MFZTaDUyZzdVWE54N1VvTTBMSUpsVlpkeXpOTnJOVTU1clZEN3M2cTk2cUQxUWtoSEp4UGdqSFZIQktyS2RlbEdLZzllNXR6MWx3cXdhcDhrZkU0eTdMRzQ4cy1HTEMtd3V4alp0UU1wLWRhZmRz?oc=5) <sub>Gasgoo</sub>
- 📰 2026-10-20 [On October 19, Yinwang officially signed a strategic cooperation frame](https://news.google.com/rss/articles/CBMiqwFBVV95cUxPUWJHTjJzYWxFeW9YWmZ1WDQwVG5YcUtSUFBURGFuWHVBTlBrYXZLZm1oMXJYYmo4cGZISlZHOEtncmRMcDN5TWhZdmVleVQ4V2ZJeVBmNlVLdVRxS3Qyc2VLQVZsSlJZUFdReEEwUEw1SjlfLUs4MzBCNGtnVHUzZXFJUGkxSVlIUDFlZWRpN1Bwd1FabnkxS2FIbk84WUtYTkJCRnYtUjd2ejg?oc=5) <sub>Shanghai Metals Market</sub>
- 📰 2026-10-20 [Avatr T09 Concept debuts in Paris as a flagship SUV](https://news.google.com/rss/articles/CBMikgFBVV95cUxNT0d6amc5WWY4dWp1SllIeGY1enNnc2pLclNaOTBQQl9yVTFReXVBdlZ0ZF9XRDRrVmwzMzVBZkhVTjlnV0E0eDRkQmxILXduZmdtT3pYREhNT1lBYmNyamVSUW9zTllkd25qV1YzMFhoSGF3S1Z5ZjVQSjJ3SGkxMHlqTHFxUlBLZWtzUi0zU3Y3QQ?oc=5) <sub>Motorist Singapore</sub>
- 📰 2026-10-20 [【视频】十万级华为乾崑智驾ADS 5 SE大六座！星海V6上市：9.99万起](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBzLU5IM01FbDcwbTFRRWRfQkNXYlhZUy1ZeExoTUZoRzlXXzlGbFM1eldnS01rNUNuLVpTWFQ5SVN5Z3MwSWFPekFrUm00SXlCcWc4UFZZWk9ubEU?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-20 [深蓝S07值得买吗？华为智驾+1.5万优惠，3个维度说清+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE95akQ5cElvYjd2c3QyV2pRbE5jNlZRUk5kWVNHckZMYkUteGhhMHhKRGd5VzV0QlhjbmxiaGdhTkZsWGhGaU5RZ3ZMTUlPelI0TnlNUlptLXBWYmdCT2xJMk50eWhzWTVZQTRPTmRGNXpIZw?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>Baidu Apollo</b> (48)</summary>

- 📰 2026-10-19 [Top 5 Self-Driving Car Companies Leading the Autonomous Vehicle Industry \| Automotive IQ](https://news.google.com/rss/articles/CBMizAFBVV95cUxOWERVaVQ1RW5iLVlrYWtvRFFkS0pvQ3B6cno2dWlWN280NDFvdU9yZl9NcXItSTFGTmtReFlOQXhCcUxiX3dJYkd1WVp1NHY5b29yOXFfSXhBSThyQU81ZDdYMHdPUFhFZ0F0TmpFamhHQnNLWHJlQ0lDRnhUMjdtbTh4QjNsMkZxeEpuT0s5ODhBcS1La2xzWldXc0l0Z290Y2JheE9uVXhUWF8yOVRXV3J5NGdfV0sxVHVVb0FVS1BXZ3A0LUVxaGRVb07SAcwBQVVfeXFMTlhEVWlUNUVuYi1Za2Frb0RRZEtKb0NwenJ6NnVpVjdvNDQxb3VPcmZfTXFyLUkxRk5rUXhZTkF4QnFMYl93SWJHdVladTR2OW9vcjlxX0l4QUk4ckFPNWQ3WDB3T1BYRWdBdE5qRWpoR0JzS1hyZUNJQ0Z4VDI3bW04eEIzbDJGcXhKbk9LOTg4QXEtS2tsc1pXV3NJdGdvdGNiYXhPblV4VFhfMjlUV1dyeTRnX1dLMVR1VW9BVUtQV2dwNC1FcWhkVW9O?oc=5) <sub>Automotive IQ</sub>
- 📰 2026-10-18 [The Gap Between Autonomous Hype and Reality is Growing](https://news.google.com/rss/articles/CBMiO0FVX3lxTE9xdjBpQUdKZUowYjhpVlZwU20tUjNhN3hpQnFldWpfOV9tdUdaVkRObnR6VlY1eFlFdFU4?oc=5) <sub>Howl.link</sub>
- 📰 2026-10-18 [Seoul taxi overcharge complaints by foreigners top 6,000, few acted on](https://news.google.com/rss/articles/CBMiugFBVV95cUxQcEZXRHVkMXg5Sy1yNXNsZXNEWXo5X0hDemZkMERmYzM0ZkIzQ2I4bndEZWFRbjRGV3B1Z1BzNFRtT1NvbGJrSG9CTEltRGF3V3ZGcWhLakI0My1KVGNLcHU0YnRGNlpmbHVhcWg1ZWtxOXl2LUR0ZmFGUlgxWkdWM2gzcXdTYS1hT182R0ZSZ2hFOUlIVVU3b2FlVGx2WG5wZTJFZTlQaEdRN28tc0p3MXZQRDdPM0Juemc?oc=5) <sub>Korea JoongAng Daily</sub>
- 📰 2026-10-18 [钰见雄安Vlog \|在雄安体验没有司机没有方向盘的车 你的出行，自动驾驶来接管](https://news.google.com/rss/articles/CBMif0FVX3lxTE4zMXFWSUZQSVB4TGhtXzRweXdJbmpKY1JnR1dVVG1YLUt6bUhXTXViMmhEcGNuMmpSbHdFdVFRbkNnclV4QnJ6Qk9GbmdmX19NeHVfZG0yTzBpMHYtekY2NjZNSlFNYVV3aENaVWFqUEV5bHNOT2dDcFRDVWdSdHM?oc=5) <sub>新浪网</sub>
- 📰 2026-10-17 [Croatia Robotaxi Goes Driverless: Pony.ai Hardware, 22km [2026]](https://news.google.com/rss/articles/CBMigAFBVV95cUxPbXpWaW1YYXplbkJnTzFEYV9LVmpRT2lvY0dxMmNkakw4OWNJQzVNVFpQbW55SUFhT0lvUGNsaV8zY1VUdUhmem52LUtRZl85TXBDaFVDc0U1UGc3Rno1SnQ0Z3hwcDJlNEpWQ0hZV3lRT1lDTDAxbGpjUlhNWV93Yg?oc=5) <sub>https://tech-insider.org/</sub>

</details>

<details><summary><b>Pony.ai</b> (148)</summary>

- 📰 2026-10-20 [5年招引16个百亿级项目，广州南沙产业聚链积厚成势](https://news.google.com/rss/articles/CBMijwFBVV95cUxOckZMcHo0c2p6SmlUeVAtSWRFajJGNmFrVUNNMVhkb2daenJoNjVyeDVwTndieWpkVlRManhka1JUaVl4eTBXU09jZ0JNdXRJdW9QTWh3WkFkZlB3S1ZfbDYxd0Vqa3llX2htUVRDV0FQTjE1cVNDX3RFY1BlMmVINTl5VWJuSG84Q1REeml2Zw?oc=5) <sub>21财经</sub>
- 📰 2026-10-20 [小马智行收涨1.62%，成交额1250.1万美元](https://news.google.com/rss/articles/CBMiggFBVV95cUxPSnJFdFY1VnRwYXY0Z1J0UUVGdUx4UnQyT3E5Wlo4V3p6b0tCVFFWNnZDV1NSSmlXYV8ySFo2RllBcmxoaVpMSWU1RzFCb0JVRVFNeFQzZGFsdWR2ZGV4bFNTSU9mVzQ1SktIR0tPdnlhaFlYVDY1bWpQd3dsZm1CaE9n?oc=5) <sub>新浪网</sub>
- 📰 2026-10-19 [Top 5 Self-Driving Car Companies Leading the Autonomous Vehicle Industry \| Automotive IQ](https://news.google.com/rss/articles/CBMizAFBVV95cUxOWERVaVQ1RW5iLVlrYWtvRFFkS0pvQ3B6cno2dWlWN280NDFvdU9yZl9NcXItSTFGTmtReFlOQXhCcUxiX3dJYkd1WVp1NHY5b29yOXFfSXhBSThyQU81ZDdYMHdPUFhFZ0F0TmpFamhHQnNLWHJlQ0lDRnhUMjdtbTh4QjNsMkZxeEpuT0s5ODhBcS1La2xzWldXc0l0Z290Y2JheE9uVXhUWF8yOVRXV3J5NGdfV0sxVHVVb0FVS1BXZ3A0LUVxaGRVb07SAcwBQVVfeXFMTlhEVWlUNUVuYi1Za2Frb0RRZEtKb0NwenJ6NnVpVjdvNDQxb3VPcmZfTXFyLUkxRk5rUXhZTkF4QnFMYl93SWJHdVladTR2OW9vcjlxX0l4QUk4ckFPNWQ3WDB3T1BYRWdBdE5qRWpoR0JzS1hyZUNJQ0Z4VDI3bW04eEIzbDJGcXhKbk9LOTg4QXEtS2tsc1pXV3NJdGdvdGNiYXhPblV4VFhfMjlUV1dyeTRnX1dLMVR1VW9BVUtQV2dwNC1FcWhkVW9O?oc=5) <sub>Automotive IQ</sub>
- 📰 2026-10-19 [[Gen-AI Analysis] HERE Technologies and QCraft partner to advance localized autonomous driving in Europe](https://news.google.com/rss/articles/CBMiUkFVX3lxTE1CYjNCNnNzYk5fdnhnaEJadWtsVWlxRE5fck96ZXNaM0dHa29XZldfMzM1WVpPNS1Ua09UV1FtalNpeHNkZmJyM0w3eVZ5UUY5LVE?oc=5) <sub>Automotive Industry Portal MarkLines</sub>
- 📰 2026-10-19 [[Gen-AI Analysis] Bot Auto, US, selects Lenovo AD1 built on NVIDIA Hyperion for autonomous trucking](https://news.google.com/rss/articles/CBMiUkFVX3lxTE4ydEd2cTQ4NDZtVTFnQ1hhbW5VWGRnZEZVTFd0ZlpsZTNjODVvYmpnMlhfOHVTQ0FsaGpwM0hIMGVROWxwRDZBNU1fcS00TVJRMFE?oc=5) <sub>Automotive Industry Portal MarkLines</sub>

</details>

<details><summary><b>WeRide</b> (157)</summary>

- 📰 2026-10-19 [Top 5 Self-Driving Car Companies Leading the Autonomous Vehicle Industry \| Automotive IQ](https://news.google.com/rss/articles/CBMizAFBVV95cUxOWERVaVQ1RW5iLVlrYWtvRFFkS0pvQ3B6cno2dWlWN280NDFvdU9yZl9NcXItSTFGTmtReFlOQXhCcUxiX3dJYkd1WVp1NHY5b29yOXFfSXhBSThyQU81ZDdYMHdPUFhFZ0F0TmpFamhHQnNLWHJlQ0lDRnhUMjdtbTh4QjNsMkZxeEpuT0s5ODhBcS1La2xzWldXc0l0Z290Y2JheE9uVXhUWF8yOVRXV3J5NGdfV0sxVHVVb0FVS1BXZ3A0LUVxaGRVb07SAcwBQVVfeXFMTlhEVWlUNUVuYi1Za2Frb0RRZEtKb0NwenJ6NnVpVjdvNDQxb3VPcmZfTXFyLUkxRk5rUXhZTkF4QnFMYl93SWJHdVladTR2OW9vcjlxX0l4QUk4ckFPNWQ3WDB3T1BYRWdBdE5qRWpoR0JzS1hyZUNJQ0Z4VDI3bW04eEIzbDJGcXhKbk9LOTg4QXEtS2tsc1pXV3NJdGdvdGNiYXhPblV4VFhfMjlUV1dyeTRnX1dLMVR1VW9BVUtQV2dwNC1FcWhkVW9O?oc=5) <sub>Automotive IQ</sub>
- 📰 2026-10-19 [10月20日热门中概股涨跌不一，台积电涨1.84%](https://news.google.com/rss/articles/CBMiqgFBVV95cUxONEVMQ1hzcTVKek4zWjlzNFBfMkVwSHI4a2I3aTJWbWhiUXNWcjhZUXY3Q21sZGtfckdxdDhhTkpXZXhUYXhnMUpvMmlJaWgyNkx3eU0xaU40NFRCSmkxTW5ySXpBOGRUMWlpYTdOYm9BeDhIckkzQUt5ajQ3U0pObFNOY1VZRWR0WDFyVUN2QUJFNi13dk0tNDZURThFaWtwUFdUdnBqSE42UQ?oc=5) <sub>新浪财经</sub>
- 📰 2026-10-19 [埃安Ray7开启预售：纯电续航最高702公里，预售价12.88万元起\|ray 7\|后驱\|电池\|华为\|制动](https://news.google.com/rss/articles/CBMi9ARBVV95cUxQWGF1bGtUTW9TRWxQZ05ITVdsOVoxRktyMUZQQVdjMFMwbTdSR2g2MmRDb3BkWi1Ydl9uM0lzTHV6SmdHYmFSNmtzY1hpeUo5U3hudm51WklUQ2p5NzR0M00yWjVxREFoZ2YwT3gyVlFTTkhId3VoelNzbEJhMXNGd0tnenVud2YzY2ZfbjBXRUNNVDZTMjc3QkcyQjg3Z0pTYjRRamZDSmJ4bUVNa29QS2VJRVdUVnZVSmdEVkZMNmNocFZveGplbWJvOFItMnB3Qkw4X05tUjRxdjM4SkV3VDR3WUhYdVpOc2hvWnZxbnVld2Y4MWoyWkZkYk5qOWt0aGJOc1BnU3FLYnltUlZTWVVKYWVqcEs1bHJvRTFDMS1PMkZwUkVoVkZzUEZoWEFBMTM4NlRyLVpzQm1oLXk3NUJOWG5lZXNhLUJ3Mkk3VERzMVRDb1BJVFlfZjBBeFVUVkl0c3ZjR29GNUY2RVR2UzIxT0JWaWtveDdTSFVEX0JhOXRDRFM1dEJUOFJsY1J2dklsQ05lQ2FfSDVOVUJjR0ttdUdwcWRVRldPYW84MXBDdzgwaTE2RDZscE0tcTFNV2NtTmc5VFJLVWJIWEF5NUplUGR6V0NiSUZJX1hNVXF1VC1UQkNDeE1aS1Fwd3hTRW9xWHNXdGs4bTM3dXVJVGR0Unl0dUs3cm5hVkdPbnRtM0tiMHJ0RzYySDl4bHh2QThPUVBGWXpXbE04eEk1Uk0yeVVVMnh1ekdXUk9fQXFSOER3aEZEZk9rUWt3aDY2aXNVTGNfTGxFV0pEcmpLTGdGdHJEVU5MNlBLX25oTXdfbkRH?oc=5) <sub>finance.sina.com.cn</sub>
- 📰 2026-10-19 [美股存储巨头深夜大涨，闪迪涨超7%，西部数据涨超6%，中概股走势分化，现货黄金跌破4150美元](https://news.google.com/rss/articles/CBMiggFBVV95cUxQX3RDNGpBYWphUVJzeWZ4TE5RVGh5SWFnTFVUSGZ4QlRBcndRZ3ZKQVlHNzlkMFJqcUw3aEZnSkhfZlpVMHNNRllsN2JRWlI3Umw4TGtWZmR4b3hjaEdWcDBpeEt3eFdRaU1nU1VsQlZCX2dkdjlNbjlXZ1h3ZHl3T2pn?oc=5) <sub>新浪网</sub>
- 📰 2026-10-18 [埃安Ray7预售：12.88万起！45.58度电池能跑530公里！](https://news.google.com/rss/articles/CBMiW0FVX3lxTE54Vm1GMHhPdnVpZl9pMG51eVhhcjhFOU1qdXhPWFVWOWtkVHNiWWRfUHdMTTZiejUta0Nfd0ZGZExINTE2MXd3R3lHV3pSc0lUOUZjMEc1U1pCYXM?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Horizon Robotics</b> (152)</summary>

- 📰 2026-10-20 [ID.AURA T6首月锁单3.3万，智驾版占比超90%](https://news.google.com/rss/articles/CBMiW0FVX3lxTFB2YjRrUlp1REdOMnNvZmpubDNSaDZlWENHbXVlTGtmemU1TXRWeTNGVHhjWXZZYXlzZHk5empGVE1xdVBRM1ZCbXFjbEE4RkdSRXdfTV9wUU9JWUk?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-20 [首销首月锁单33022台！12.99万的德系纯电SUV卖爆](https://news.google.com/rss/articles/CBMifkFVX3lxTE54WWM4WFRRSlRBQjY1WkozTGN4UWFWMk5KTUhxZWNELUtGbVpxYlUwdDBmbmVSTzZHUWpWdDNkTUlyZ1hoeGNTbDF4VVlTZHJrczlRTWtmbEhEU0ZOeUZEV1hLMkMyUlBjbFN3b2dQLU94ZUJXVl94dV93c1ZVQQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-20 [2026合资纯电SUV高速领航实测：从丰田bZ5到别克E5，谁才是真正的德系智驾优等生？](https://news.google.com/rss/articles/CBMiX0FVX3lxTE45Nm5EX050Q2FQLWJOeFg2YkZBYUlWUmk5VC1QQ1NfNnpBRHZDN3Z6OUwzQ0lKdDFMdEVtSU9iVUtEUndaQXVCX1BpdlF2blBnclpJWk9QLTNKb0FSOEg4?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-20 [iCAR V25正式开启预售，提供后驱四驱版本最大涉水深度600mm](https://news.google.com/rss/articles/CBMiW0FVX3lxTFAtT3J1WmtKSDlMdzdEemxOTlN3NVd6WjJzbWVMcHJQbzJxRlp3SUJlM1BUVlFtcWhoVF9uaDRSQmVXMTlQN2k4NjhmZDk1WjROY0VLOERBdmZISFE?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-20 [【视频】正值年底购车季，为什么越来越多人划掉了BBA？](https://news.google.com/rss/articles/CBMia0FVX3lxTE8xMG50M3QxcjhPUm04ek5LbWZiaXRUYTNlNV80bGZXSXI2Z1JzVE9CRHMyajQ1aEg0TmoybnNSSXItXzVTdDJCVmZYR0lUcUE0eGpwV0gtRnhoWTFYd0lGREtIVFJ2ZnRMVHFj?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (32)</summary>

- 📰 2026-10-19 [Autonomous & Self-Driving Vehicle News: NHTSA, Tesla, Waymo, Bot Auto, Lenovo, NVIDIA, PlusAI, Texas Ventures III, TomTom, DeepRoute.ai, Valeo, KE:SAI, TIER IV, Arm, Technical University of Munich, Taisei, Nissan & Volvo. \| auto connected car news](https://news.google.com/rss/articles/CBMixgJBVV95cUxPRmFjNXk1ZGVyVjRJVXlPMTRvc0tTdlc3UU81MDZfYXJ6bFVzYzVJeUZwR2t4bm5pMjZLajJGODJRN1pHU3V1c2p2ZFVZX1Q5bmM2cUt0clhiNjEzWXhoQS10eDliZ1pwc3ZwejBnZXBPUmhGTkxCUWtrejZrZDJRcElzeHo5RV93dnZ6bXk2WlRZM0J0a0czZGRQTmZBS1lRV0w1aU53VTc1Vy04SzgzcnBRbzdLR2tUUjlrdEhxeFFkaU44MHdQRC1zSU0zcUpZMTJpek94SkZkV1pXdlhQN242MG94OXZXS0RDRTE2c0J1MEttdUg3SGVoMWVZMElQcUUtNG1pcERUS2lWbURScXhmNi1yWS1XOWw3MHdpc0l4NURabWVDRWswRnpOZTZjV1k3RHNjWXNEWFJQMGRESWpET0dTdw?oc=5) <sub>AUTO Connected Car News</sub>
- 📰 2026-10-19 [Beep Begins Testing Autonomous Vans with Passengers in Orlando](https://news.google.com/rss/articles/CBMinAFBVV95cUxQYjhIdjZwdXJCellJZVUteWZIQkgxZEJoN0tldFEyV1pxTVNyRlh4dzJsV2NKOHd4UzNxa2YxLTJQQk1qelA3cm9rVWU0VXJCZ2R1Q3JNbW13dWc3ejVoZk1wX3NEN1VodFZTS3ljVVBHX2JXTmRvdTJDTkpwTXA5MVphMEliRnhxX01yQTg1d1ZkN2JiM2xfdmhrSTI?oc=5) <sub>Future Transport-News</sub>
- 📰 2026-10-19 [元戎启行拿下城区NOA前装标配23.8%份额，位居全栈方案商第二](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPQzBaY1V1X2RrMWFsdkt1c0dRM2NUby15bFBGRVIyVzhHNElXVWlzejlDVW50cWZ5d0RIckZLalc5Tjd5VVVnVS0wTUNyVVFNSVF5b3FsUkgxQTJZQU9yTDU2N2t1M3hFSkxUMUxSeWJONnNGcjhuTDB3YkljM0U0TlU3bzVFRFJV?oc=5) <sub>搜狐</sub>
- 📰 2026-10-18 [工信部412批新车，赛豆ME7和方程豹钛9应该是关注度最高的了……赛豆M...](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1zUzU1RXBKR3pOMDJWSV9JajBMWThiSWsxNVVjZW1NblZHZVQwRUxqWHJjTnlBeFktWXVzdGdWSm92RXdHTW15T0RJZjk2YW1yNExsYXhqY3NSTlU?oc=5) <sub>车家号</sub>
- 📰 2026-10-18 [金年体育平台官方：从“安装障碍”到“用户激增”，安装成功率提升至99%](https://news.google.com/rss/articles/CBMiV0FVX3lxTFBTSWxuOGdya2hsQ1FwSURIUWhUUV9RWjRoem5sQkJCMEwzM25nay1JU0xmM3NpcS1adUl2bG51RU13WmRWOEY1cEUwMnZLX0xxcnRiZlk0OA?oc=5) <sub>TGBUS</sub>

</details>

<details><summary><b>Mobileye</b> (17)</summary>

- 📰 2026-10-19 [Beep Begins Testing Autonomous Vans with Passengers in Orlando](https://news.google.com/rss/articles/CBMinAFBVV95cUxQYjhIdjZwdXJCellJZVUteWZIQkgxZEJoN0tldFEyV1pxTVNyRlh4dzJsV2NKOHd4UzNxa2YxLTJQQk1qelA3cm9rVWU0VXJCZ2R1Q3JNbW13dWc3ejVoZk1wX3NEN1VodFZTS3ljVVBHX2JXTmRvdTJDTkpwTXA5MVphMEliRnhxX01yQTg1d1ZkN2JiM2xfdmhrSTI?oc=5) <sub>Future Transport-News</sub>
- 📰 2026-10-19 [DoublesAI unveils CEM AI model to cut computing costs by up to 67 percent](https://news.google.com/rss/articles/CBMiuwFBVV95cUxOUWExeFBKN2RaRFduZUY3UGdHZXNjdGxEWklyRnByX1oxcWhidEdUbjlnbTlQQ2tRMlZkT2NCazZkTC1wZTJtVEtTMWhhOUl0cGVOSmstdllLa3N2UVFsd0lQM00yVmg1THVKVVF1TlA1ZXkzY3FIZGVZR1lsOHNucnhCcEdEcTB1cS1LbDZ0aGxuQjJodzd3VE9md3MxZzQ2aG5nbGpybnRKN0FQR1ZXRG92TDVoR3dGU2VB?oc=5) <sub>디지털투데이</sub>
- 📰 2026-10-18 [Polestar 4 is an electric car that combines everything into one](https://news.google.com/rss/articles/CBMiUEFVX3lxTFB6eFU2TG1qczVlQ0dzbHAwOWF2MVZXNkFFYTJDemJVT2EzUFE0M1k5dnJDR2thNWNIM3c4cnR2c29HOUlTdGNlX2k1U1kzbk81?oc=5) <sub>Mashable</sub>
- 📰 2026-10-18 [Is ADAS really helping the driver?](https://news.google.com/rss/articles/CBMiU0FVX3lxTFBobHh3SFdJUm1KQnV2dDAwMU5ZZHhUR0lkMlJnRXVobWFVeGJRd3MzbTgzNEtCZ3ZUU2Rqb3VjM0lpQmNZaFp0cUZ1ZHV4MS1TOHhR0gFaQVVfeXFMUGF4UXBzNmwwcl9xU1ZOYW5xVEdYeHM1TGdTV3FCRE1WZ1E2SXhTNjllbWlVR3QtZVloaEVtZ2R1MTREMXlFRTMzb252T1dlU2tFNTF6eVQxSlhn?oc=5) <sub>Gadget</sub>
- 📰 2026-10-17 [Why Mobileye Global Fell Even As Sales Rose](https://news.google.com/rss/articles/CBMivAFBVV95cUxOblE2a0FORVFwdlBzb2t3bTJ4Z0w2YUpPVURicGRfMDlpdUNpWmowRzMwcDJPVEp6NXJZOXg3UXJEcTN2VVdHSkxXTGY4TmxVZmpZTk9QSmVOYVRzUDdJamo1bXF3aFdreUZGb19CWjVyQ2NqRHB2SWs4OEw2N2t0c21pZG9XMENUMEtMTVh4blRuMERqaUJHekQ3S0I5SFhxRU9LdXdyckEzamRmWDFqRnNROUowaUZweGl4aNIBwgFBVV95cUxPYjV5SndkRFlUM1EtOUtUWGVMOHNTNFYyYnZVU0Rfamg5SjJIbWtfcjJWY0ZoVHRVN3ljQlVkekNfY3I1NDlkbDBYNkx0UUhaU2N5OWk2cmpmZ3NYejZjQkI5T0Myenp6ZUN5Z3VoWVR4eDNGei1paGdvcUt5b3VPNEZleDZCZW55c3Zzb0FSYTU3S0M1MzZhdXEtNllTM1VSTWw1a0pWYm55aHBJUDU2OXZOd1A1Ql9INkNhVkgtR0cwdw?oc=5) <sub>Simply Wall Street</sub>

</details>

<details><summary><b>Aurora</b> (61)</summary>

- 📰 2026-10-20 [Trucks at ATA's 2026 MC&E in Charlotte, North Carolina [Photos]](https://news.google.com/rss/articles/CBMipgFBVV95cUxPZENwSTBGNU9tanAtcTRjaWtSSFlRQUVyMnZTVEtDVnVmR2E1SFEzVy1JblNObU8zZGVfUXhMMzcyUDhmVEhNVENnVVgtMXZvOUdicXJBZjQ1RmVjc3c0bng5bkNsWDdZSGxxUUI0NTIxWmN5UExQMVJkcVc3SEhWbnlXUU5MU1owWVNMdWNuZUU3VzlkN1huT3J2bGRsWVlzQ2JjcHR3?oc=5) <sub>Heavy Duty Trucking</sub>
- 📰 2026-10-19 [Self-Driving Big Rigs Rack Up Miles, Just Don’t Tell Them to Back Up…Yet](https://news.google.com/rss/articles/CBMitgFBVV95cUxPSm5xdlZtbXc5S2I5NGc1d09XN21RRmhTcWpWUnQwQ3ROMURBVW5NdkthbmVCdEdHbTRBMmRnaENJU3dPVnNjSmFfamRSZFpJbWlJM0diZG9icUxxWDZlX1NmYi13al9tbnlVaGFIRC1EcW9vTjlWQTMtVGNhMkV4Z29Vd1B0cmNxUG9ZcHhhRXM3LTl5WEYzVGp4Qko4WmRfd3EzbnZKZ1VGc1duSUxZWFQ1VHNMQQ?oc=5) <sub>WSJ</sub>
- 📰 2026-10-18 [Aurora Innovation (AUR) Wins A 5 Year US Waiver, Is It 60% Undervalued?](https://news.google.com/rss/articles/CBMi1gFBVV95cUxNZUY3dFlETjNKYmxFRWVKLURRTjlfVDVLVWliNjJrcXpjWXFxTklncXpNYWwyM0xfYjBaNFpBOHlaX0I4eFNJMF9WZWNCR2R0RWxfOTBhTGFfREtLd1JVOTJaLUVLTFJoY3hNTzExZFdaR3RDTnk0NGJBOGs2T1NyZ29yV2otempKQ2RzalppRHJ5TnhfV2JTdzBDTVM1T3AteTBmSHZldHRGMlRlc2ZfaEc0T0VOcnpOQnBwcExLUEUyRmVib1M5MFJVRkpWamkzU3l6Ui1n0gHWAUFVX3lxTE1lRjd0WUROM0pibEVFZUotRFFOOV9UNUtVaWI2MmtxemNZcXFOSWdxek1hbDIzTF9iMFo0WkE4eVpfQjh4U0kwX1ZlY0JHZHRFbF85MGFMYV9ES0t3UlU5MlotRUtMUmhjeE1PMTFkV1pHdENOeTQ0YkE4azZPU3Jnb3JXai16akpDZHNqWmlEcnlOeF9XYlN3MENNUzVPcC15MGZIdmV0dEYyVGVzZl9oRzRPRU5yek5CcHBwTEtQRTJGZWJvUzkwUlVGSlZqaTNTeXpSLWc?oc=5) <sub>Simply Wall Street</sub>
- 📰 2026-10-18 [Driverless 18-wheelers are hitting US roads. Are they ready for every emergency?](https://news.google.com/rss/articles/CBMi2wFBVV95cUxOeDhYbFlPYVdOaUhZZzBSWU93QUxWMmFPMzZpYUlxNzg1X3BIZWxsSFBEeUFoVkdaUlZDc0g3NUZXQ0VyMDlReWMwem1HbXhfU2FtbDFUT3MyLXRvSWZXWUp1X1ZnQXhpaXpvUWMyblhWeEdlYzl3Q0VBZkljR3d6LXFzSTBISEJiNTF3VlRRUTF0N0k0eTJVZVVLZ1dfUl9uaGdiUFdWVDJtcDZYY0hXalFZek9EMHd6MkxMM1Jpbmd4c1kxRnBYMVBKei0xUzlOSi1rQzhBaDltVTDSAdsBQVVfeXFMTng4WGxZT2FXTmlIWWcwUllPd0FMVjJhTzM2aWFJcTc4NV9wSGVsbEhQRHlBaFZHWlJWQ3NINzVGV0NFcjA5UXljMHptR214X1NhbWwxVE9zMi10b0lmV1lKdV9WZ0F4aWl6b1FjMm5YVnhHZWM5d0NFQWZJY0d3ei1xc0kwSEhCYjUxd1ZUUVExdDdJNHkyVWVVS2dXX1JfbmhnYlBXVlQybXA2WGNIV2pRWXpPRDB3ejJMTDNSaW5neHNZMUZwWDFQSnotMVM5Tkota0M4QWg5bVUw?oc=5) <sub>The Financial Express</sub>
- 📰 2026-10-17 [The Most Polite Trucker in America Is a Driverless 18-Wheeler](https://news.google.com/rss/articles/CBMifkFVX3lxTE93OW9admIyUlN5bFZhR01TY2d3S1J1a19qSDdpOEJONWtORnNBVm9rWGMyaEtXV05KRXBJTjZPWUNXOVFSSFA3R0tPTWhXQUdEaEhaVWFfMDFYMHNLT1M0dzFTclE3ZlVKdkhSZXp5dk1feXdUdXl2WnZNM0xQZw?oc=5) <sub>WSJ</sub>

</details>

<details><summary><b>Zoox</b> (60)</summary>

- 📰 2026-10-20 [Alibaba Backs Chinese Robovan Maker in $400 Million Fundraising](https://news.google.com/rss/articles/CBMiswFBVV95cUxPdHJFZ2hnVEF0QmdfZ2Q4b09uLTBrTHpjT2pMODJ4Z2k4WlNoT0xDakdJUTdpcEJWR1FpbzlvRHNzRE5ZTWZ2bkxXVzNVQl90YUJTdnVybURmb01WZ2lyTWxrbHF5Q2JEbi1EZ09IWFVMeUVQQnhYUHZXLXJzODZOandZd3pWa29WZnJrTm84T1BLcHUxSUNrWUhRNHBFWGt6aU5ha1dKYzFtaS1YQUtkWTBEYw?oc=5) <sub>Bloomberg.com</sub>
- 📰 2026-10-19 [Santa Monica Moves Forward with Zoox Robotaxi Parking Agreement](https://news.google.com/rss/articles/CBMilgFBVV95cUxNZ19oblNJdHlHR3BOdFhvV3BWSHB1MEdHM3VQMmgtdGJNQklPNnRDZ05ZUWN0cWJVdXNtQ3VhWjlEZVFiRUJla1h5WE1mRjBSbEFGQjZpcExvMHZZd2g0S1dKdTZmNFByMlA2ZDZ3NC1lSWoyb2JOd0daTlNaRHZvR0IxQ3Vrcmo4T3BoRVZYYndwTzN4Q1E?oc=5) <sub>Santa Monica Daily Press</sub>
- 📰 2026-10-19 [The 2026 Florida Automated Vehicles Summit is coming, and so is the future](https://news.google.com/rss/articles/CBMiugFBVV95cUxPU0IxbFZKcTA2b0d3cXJEcGpXR2ZJY3RwZVdzOUNnVERnazhiVDltM1pPalYtR0tLODN0NWRYNzJ2VWFMWUhCTk12YWg1QlRyUGo3TTV4TVE0c2RzSHRoMlRlc0Rac19oN2U0eE85SThEbWpGUUNVbEVNMWZXdHRvbTFEaEgwbUNyTGV2LWNHVWpwY3BPWm9ObzdxVFRjSTB2N2JRVlhNYlRweGxDVVI4RFc3dmMyV2FjeFE?oc=5) <sub>Florida Politics</sub>
- 📰 2026-10-19 [Robotaxi: Cities and states want to put a brake on it](https://news.google.com/rss/articles/CBMid0FVX3lxTFBpYi1sWXVUZjU5QVFLTGF2NmY3VmdmTEJBNUc2UFR3dVdRdmVsRS0zTnpQYlEwWlQ0MXZhYy1MX0ZjOURic0p2eXpPczR2RlRJMkN2b29iazd2SVVTZ1NtODlJZnBCZUNsMHFLazI0ZTVBbUMzajI4?oc=5) <sub>SecNews.gr</sub>
- 📰 2026-10-19 [Metallica Sphere Residency Revives Rare Songs in Las Vegas](https://news.google.com/rss/articles/CBMingFBVV95cUxPTFhWMnNWX2JwbS1TdEpKX0VFalg2VEJJbExIQU54bThuaWV4cW9scWdzZ3h1Ym01d2JoQ3lmMlhfWF9vMGg4Y3ZEcld1aWVMa3MzZ21jYXZ0N0xseGJNNDhtWVhZbjRSOVB0OGhrN1pUTWVNMDlJcnZCcWVxMlFUMk5FNzRDLUZGVjRwRkRXZjJKaDdKUzUtbHRMZTlkZw?oc=5) <sub>Casino.com</sub>

</details>

<details><summary><b>Motional</b> (27)</summary>

- 📰 2026-10-18 [Hyundai Motor moves to sidestep self-driving fallout in India](https://news.google.com/rss/articles/CBMiugFBVV95cUxNaXZ0YW55OGwzWnN4XzN4Y3YxeVpDQTJKOExNM1dmWkRSbUpjaUhhUUd5T084cnIxY3VSNzB6TzNSMjRreHJfN3l0VEt4b2VSM1lpanRUY3dDTmRNRWxBeVdwdlBCZGFMcWVHQkl5Yk9ReDgxbk14RTVmN0JNbU5RTWwyaVJ2ZTBRcU1Bc1BBai00eXNHMExxb0VkNEozUGl0dlZtT1BpWTN5M2dmbkZtZlI4ZEQxc3hibnfSAb8BQVVfeXFMTjY1OFZ6b3Z2S2lxd296ZHE0VTFpaHYzeU01bmZkSGJlSi1kbDRjWVJZLTl5VXhMVWRNVUxjeEg0aFdUWDg4Ukhhc2NYNkZ4dUlPQUFHeGtlRnB6QkotMDZYcXN3clRwZWduT1RndFg5WGZYWXlHQkZpUEZhb3NXNjlPYUZxRVVFcXlNTW1wWVYxUHhyWWFKbmJ3c1RsUk8xbnZmb2FIYW1EejBzWGdpNU5XT1R1dThfbDFaell0czg?oc=5) <sub>The Korea Times</sub>
- 📰 2026-10-18 [Hyundai Motor, Kia to Deploy Humanoids in Factories from 2032, Unveil 'Autonomous Operating Factory' Roadmap](https://news.google.com/rss/articles/CBMidkFVX3lxTE5BSkloNVFid1JrenR2b2g4a1N2OXI4SVNYQmRvMW5wc2lHS0Y5TVUzVlRJTjd0Wlo4UUFmWDA0U3hQTmFxOG9uSF9oOC1TMGs0cV9temVoeXhzUkx0Vzg3ZU5qNDJXRnJTb2l4VXg4U195Q2U3R0E?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-18 [Hyundai Motor, Kia Unveil 'Autonomous Operating Factory' Roadmap with Humanoid Deployment by 2032](https://news.google.com/rss/articles/CBMidkFVX3lxTE5BSkloNVFid1JrenR2b2g4a1N2OXI4SVNYQmRvMW5wc2lHS0Y5TVUzVlRJTjd0Wlo4UUFmWDA0U3hQTmFxOG9uSF9oOC1TMGs0cV9temVoeXhzUkx0Vzg3ZU5qNDJXRnJTb2l4VXg4U195Q2U3R0E?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-17 [Grayson Brulte: Waymo Will Launch Driver-Out UK Service by Q1 2027 as London Permit Becomes 'the Keys'](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9VUjFlTTg4T2NGVlQ5dlIteGN1RVVNOWV1UTVCTEhGU3poT1FHOFN6VjB3VU5QX012ZEpaZ2RNNV9RNkRuV2hmQkxTY2EyN2FjanZhRVpPczBLWTg?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-14 [Hyundai’s two robotaxi plans take different routes](https://news.google.com/rss/articles/CBMikAFBVV95cUxQNWdFN1RBOWctNVVIZmRxemEzVEhrQ2MzVkN6YkJWME81bW41bFFqQVVDLTl4SEQ3OTYwalRQaFo0Q0xwaVR4M3FYOUZpMUV3OEJSTDktdHY4enVEdDgzY0xuV3lSa3hCTTAwdE93bkhoS2M5aHdxcmVkbEJIM1QteTlVbjhfTk9UUVBraW9GX2TSAZABQVVfeXFMUDVnRTdUQTlnLTVVSGZkcXphM1RIa0NjM1ZDemJCVjBPNW1uNWxRakFVQy05eEhENzk2MGpUUGhaNENMcGlUeDNxWDlGaTFFdzhCUkw5LXR2OHp1RHQ4M2NMbld5Umt4Qk0wMHRPd25IaEtjOWh3cXJlZGxCSDNULXk5VW44X05PVFFQa2lvRl9k?oc=5) <sub>ABC27</sub>

</details>

<details><summary><b>comma.ai</b> (3)</summary>

- 📰 2026-10-07 [Researchers Find that AI Models Struggle With Even The Most Basic Driving Skills](https://news.google.com/rss/articles/CBMiuwFBVV95cUxNb2ZGRGxGZDNjLWU1OVBPNjUtUlJXR0hiVGV3WEJ1eUVnSWExMWVvRmJjX2NtQm9sX0plMTU3YzZwUm5ZTzVoSGttcXZmQ3BqbW40X2doNFMycUk4UWE3anlidy1vWHNYZndVZjZWLUYtbnlHeVBFRjJOaTF4SWxzbmotR0xsNkVIcEhfZ0M3LUs5R2FyV1lVdlRRU3JwakpQcXpBUzlEOEhsWlB3Q19EdXFhQjRvZDU5MHln?oc=5) <sub>Auto Spies</sub>
- 📰 2026-10-07 [OpenAI's GPT-6 Astra is the only AI model to finish a real-world driving test in a Toyota Corolla](https://news.google.com/rss/articles/CBMifEFVX3lxTE9iZmN2ZFp6blVBRnZUTkYtYTJ3b0hSb0xhQjZyQXh5MUN2T3ladUlEb1F1SWJzc3FtamZtazk4LTVUWVpNX0ZjbGZwMnpERk45TVVQWVA1RjBZVUxxTTAzTWpaV1JqUzIwM1I2Wk1tTzc3bDJpaWluc2JVam4?oc=5) <sub>Crypto Briefing</sub>
- 📰 2026-10-06 [AI Agents Tried to Drive a Corolla, Crashing on 8 of 11 Runs](https://news.google.com/rss/articles/CBMiuAFBVV95cUxONWxQTEZham1kc1J4S2lMNUh6OTN1QWhXbl92U21NUWZTZWhNUUdwcFVvUHYtVWJzSjl4TjlCeFhUY2ppMXd3WkkxaHJFRmFlNUN2NGFSSENnV2ZZYWRNZ3JIUjd0dzFlTS0wR3gtbmxXN3VHOUkxWWg2VVFpTVgzWGN2T3RPdEFJV0cyWjRPSVFyNWZTYjFyX0pzYjFEUWQwLUlfbGo1bm8xVUZXQmpyQ3pCNXV5ZE9x?oc=5) <sub>thetruthaboutcars.com</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
