# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-10-26 · 1,294 papers tracked · 43 curated.

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
- [Motion Prediction & Behavior Modeling](#motion-prediction--behavior-modeling) (1)
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
| [HERMES++: Toward a Unified Driving World Model for 3D Scene Understanding and Generation](https://arxiv.org/abs/2604.28196)<br><sub>Xin Zhou, Dingkang Liang, Xiwu Chen et al.</sub> | ICCV 2025<br>2026-04<br>📑 5 | [⭐ 72](https://github.com/H-EmbodVis/HERMESV2) | Driving world models serve as a pivotal technology for autonomous driving by simulating environmental dynamics |
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

## Motion Prediction & Behavior Modeling

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Flow-ERD: Agent-type Aware Flow Matching With Entropy-Regularized Distillation for Diverse Traffic Simulation](https://arxiv.org/abs/2607.06957)<br><sub>Seulbin Hwang, Kiyoung Om, Dae Jung Kim et al.</sub> | RA-L<br>2026-07 | [⭐ 0](https://github.com/seulbinHwang/flow-erd-project-page) | Realistic and diverse traffic simulation is essential to autonomous driving development |

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

<details><summary><b>Waymo</b> (240)</summary>

- 📝 2026-10-16 [Hello Toronto! Waymo is En Route](https://waymo.com/blog/2026/10/waymo-in-toronto) <sub>official blog</sub>
- 📰 2026-10-26 [Tesla Cybercab Adds 2 Features: Rear Cam, Quiet Mode [2026]](https://news.google.com/rss/articles/CBMihAFBVV95cUxQRzhJaGVfZ3FpUE1oaFlnOEItREJMZ1ZJeXhUMU1jbHFjWkRsWkZCLTdTTXM3SXNIUm1LdGxUanZWY3BpcGZMTUlLeFhrZlVQWWw3ck9vZC1tMm9Vdk1SUVp5eVlQcGpmVWlVN000OGFncmVZTmU3aWktRmVMWVZ3WVRuRXM?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-10-26 [Waymo's 2027 Madrid target and Bolt's reported plan](https://news.google.com/rss/articles/CBMifEFVX3lxTFBXQ0xuUThNT29JMHE3VEJTX3k1WnA1TUljNGRqX3ZHUi1KMG8yVXVhT3ZWQ2FDaHhwRS1hTVRQY0xlRmhKUk91a3FiYndHckdBTlc4V2toQkp0NFJfTDZEbWItR2ZETDdkTlM3RE9tdVpVM1hJa3F1VWJ0djY?oc=5) <sub>NeoTeo</sub>
- 📰 2026-10-26 [Tesla robotaxi seen closing in on Waymo if weekly miles rise 20 percent](https://news.google.com/rss/articles/CBMiwwFBVV95cUxOYm96NzBKbS1Va3Bmc0ZvbEJyak11UDQ1X0I2cVplOW02anpJV21RMjJYYUR2RU5ubVVYRFRSa210NmpQVm40cGV0Y1JCV0JGRTBVbUV0dm5hQzd5QkxjU0xld29DVFF2ZDR3NnJ5ekdhWDJvTENSejdXZ1VkZXNsTElLbmxqQnN5QmRsS1hGZ0tMSEdwSlA0UHpUOWhPdXRDSHdOUW5UaVZPYl9iU0p4VHUxWWdjdzVrWTRob1pTVWl5U28?oc=5) <sub>디지털투데이</sub>
- 📰 2026-10-25 [Driverless electric taxi fleets learn to adapt to the unexpected](https://news.google.com/rss/articles/CBMipwFBVV95cUxOVmJON3FFZENCby1DVzhxeGluc0FLN29qdW1tTk4zSGU3eVZnM0xxYkFnS21hOHo1NHFfOHBoZ1ZtZXcta002SjVyekl3dmNoTkpYeTA2d2ltdFlDcjFjV3NfMWlEcGFtRHA1NUdmbC13ZDhoX0k0bzJvSGtQNzFYYUZmdHh0TG5QbjBqQWl4U21BS29kdlhkZEhzOFdfeVE0ek5DX0lqVQ?oc=5) <sub>Digital Journal</sub>

</details>

<details><summary><b>Tesla</b> (356)</summary>

- 📰 2026-10-26 [Elon Musk Met Xi Jinping and Took Tesla FSD to China — Now His CFO Says Getting the Green Light for Unsupervised Driving Is ‘Hard’](https://news.google.com/rss/articles/CBMikgFBVV95cUxQemsxTXd3Nk15RmVMbmc2TENtNmpDNWZVWEN1X0NLTjh0aW1JOHNpYWF4bHVzQ29KTFVvbmNGVVRSUkFMSUlnU2J2SE5aLVdQcVBHZmM0VWVQRnpvMEhRNzJVcktUcklPTUhtNTQ0bWt0bHlybzlCbVMyT0tJQkJGR3I4VzZyc0xWRU5rREdYckVHZw?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-10-26 [Tesla’s AI ambitions take flight as rivals race to keep up](https://news.google.com/rss/articles/CBMihAFBVV95cUxOZjRISUlMdDF1alVHd0JSeDdZOUhFQ2dTTzFkMFlkME9pNHRCTGFGME9GLVJ3TklGbGhydk9QQ3dNWTE2Y2lhbTdfeHdPdmxZREtQMHZSUDI4b0txc1VGR1N3bHBRUTVyc2pSVkY1TGxhY3VlRVRFUm5acjlDWUR1M0lnY2k?oc=5) <sub>Financial Times</sub>
- 📰 2026-10-26 [特斯拉FSD开通率75%托底毛利率](https://news.google.com/rss/articles/CBMiW0FVX3lxTE14V1B3TkRKYXRsaFpONmhiQnVzZTNFbjd2RkRONk9jbWZuTGtGeGVJQ29rN2x3Sjhqa3NfODNyWk1ZenlOeWNoSnZYWGlqWjBRUUlPc1BxVU11ZzQ?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-26 [特斯拉Cybertruck辅助泊车遇后车硬钻，两车互不相让](https://news.google.com/rss/articles/CBMif0FVX3lxTE5aV3ZrNFJZZzA1VUlKRl9Mb2xvdnBwQmUtOGJPdm5CVUtlX29qV2dIYTcteXVTUU9WX1R0WjIyeS1sY3FROWN5OHgyMjdNb1hKUG56VTAxN01qLXZtUl9mRGpKVzdPSlRnYW1hMDdjWk5kX0dJT1NRc2tWNzM0Tmc?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-26 [Tesla FSD China: CFO Flags 1 Big Hurdle [2026]](https://news.google.com/rss/articles/CBMiekFVX3lxTE1YamEtRzcxdVVzNEY5X2V1akhiUGxyUnBUSElRUjBINXpMME5MSktQUlJuUlFPNE9IUTVhZkgyeml4ZG5qNURxUmdaRTlnd1BtRi1CeXgxbVRCVVdNZ3VFYk1HYjNBeWFtdjZ6RmVPQ3MySW1aQm1IMHRB?oc=5) <sub>shattered.io</sub>

</details>

<details><summary><b>NVIDIA</b> (263)</summary>

- 💻 2026-10-20 [NVIDIA/flare-local-inference](https://github.com/NVIDIA/flare-local-inference) <sub>GitHub</sub>
- 📰 2026-10-26 [Autonomous & Self-Driving Vehicle News: Tesla, Mobileye, Aeva, Ouster, Pony.ai, NVIDIA, Stellantis, Bolt, Wayve, Volkswagen, Einride, Valeo, Aptiv & TIER IV \| auto connected car news](https://news.google.com/rss/articles/CBMijgJBVV95cUxNLXpSRDZNWTdpaUNvcWdGUWJBRUxfMGlXTXYtNFEyV0NxU0hfTmhxUlQwb2JGN3Y0VW9QS25NeVRPNkxsVV93ZkZGdGp5bW9iU3VERTFwaW5MckVKc0xmTEJVR1NFTFJORXR5SVZ2VlNDY0VFRjhabEo4dkp4WU1xTFpYci1kcWNsNndSNHg2cExQUVlCRVEtb1plX0dLa2diaDV6eU9hX1dnT1pOTmVkZXBNQ1pnUHlZQ1BVX1FEWWJfcS1fejBXbUdWZE5qZDRDUGtmTnFUZVhYTkItWlN5emwyMnRGNWFITHVDTEZwQk9hdXpJT3d3N2UybExoRjRtLTVZUFE4ZFBZQVZJLXc?oc=5) <sub>AUTO Connected Car News</sub>
- 📰 2026-10-26 [Jensen Huang calls AI as a five-layer cake: Nvidia GTC Berlin](https://news.google.com/rss/articles/CBMirAFBVV95cUxPYXNNWS1vQ1Z1czhXRk0ycS1tOWM1WHhWMFhXZnVaNmpvU2tlcXN4N29DTjB0WFAyNkhwekVrOWgyOUU0Q21jOUFLenJhZnJ4NzFvZS1XRC1UcGFyelFHa1RWeVA1cEw2ZVpkRHdjZk5BcmlieHhpTTktM1NPUFFhdHZpTXVGZm40aEl2ZHA0UW5pNlN2dWkzcWpIVnF2S2pBR1dNX0tqaU5lang20gGsAUFVX3lxTE9hc01ZLW9DVnVzOFdGTTJxLW05YzVYeFYwWFdmdVo2am9Ta2Vxc3g3b0NOMHRYUDI2SHB6RWs5aDI5RTRDbWM5QUt6cmFmcng3MW9lLVdELVRwYXJ6UUdrVFZ5UDVwTDZlWmREd2NmTkFyaWJ4eGlNOS0zU09QUWF0dmlNdUZmbjRoSXZkcDRRbmk2U3Z1aTNxakhWcXZLakFHV01fS2ppTmVqeDY?oc=5) <sub>DQ</sub>
- 📰 2026-10-26 [inDrive and Pony.ai Announce Kazakhstan Robotaxi Collaboration Using NVIDIA Hyperion](https://news.google.com/rss/articles/CBMiugFBVV95cUxNZ3RvSm9KeXB2MDFwX1pEWExvS3VlZDNGNTdLSWkwV1R1VE9uclRtVU5vTEtBcDh2dlI0UHZFaE1jTzV4aHpRcmpicUNDaUlxZjBFQWI3cDg0NXZYLUJUQkQtNDBBN1cyaWVpSGhSM2pkYWM2M2M3VGNYelBhUmgzMFdXb1p2MlhYQW9fVnhXMWEtWHVqMEw5Sm9BTXNNdnBxYV9LVTAyR1UtZ00zOE40YXBLSE42RTRsc1E?oc=5) <sub>World Business Outlook</sub>
- 📰 2026-10-26 [Teradyne Robotics and Sereact partner to drive physical AI solutions for retail and logistics](https://news.google.com/rss/articles/CBMivgFBVV95cUxPa01VQ2sySmRzN2tjaDJKeDFLZEc4UnE0SC1haWI1TDViOFNIV1A5cV94NUhja0ZOMjdTX2lvQ2c4M05CWkkyT1p1Q0JMcUtlSzBSd3JGdk5qOHQ4cDlzSlJZd1lrRWUteHZPbnRwX1JJQjNnWHhmOHRGQjJZdHBjajBEWWtrcC1UVzhpU0loMDdjaTZqZXdYNkk2am9uLVJxSjBqM1htcXQydXpCeThtQ1NZS1RzNnBabEVCTkx3?oc=5) <sub>Process and Control Today</sub>

</details>

<details><summary><b>Wayve</b> (65)</summary>

- 📰 2026-10-26 [Autonomous & Self-Driving Vehicle News: Tesla, Mobileye, Aeva, Ouster, Pony.ai, NVIDIA, Stellantis, Bolt, Wayve, Volkswagen, Einride, Valeo, Aptiv & TIER IV \| auto connected car news](https://news.google.com/rss/articles/CBMijgJBVV95cUxNLXpSRDZNWTdpaUNvcWdGUWJBRUxfMGlXTXYtNFEyV0NxU0hfTmhxUlQwb2JGN3Y0VW9QS25NeVRPNkxsVV93ZkZGdGp5bW9iU3VERTFwaW5MckVKc0xmTEJVR1NFTFJORXR5SVZ2VlNDY0VFRjhabEo4dkp4WU1xTFpYci1kcWNsNndSNHg2cExQUVlCRVEtb1plX0dLa2diaDV6eU9hX1dnT1pOTmVkZXBNQ1pnUHlZQ1BVX1FEWWJfcS1fejBXbUdWZE5qZDRDUGtmTnFUZVhYTkItWlN5emwyMnRGNWFITHVDTEZwQk9hdXpJT3d3N2UybExoRjRtLTVZUFE4ZFBZQVZJLXc?oc=5) <sub>AUTO Connected Car News</sub>
- 📰 2026-10-25 [Canva Enters AI Image Generation Race With In-House Canva Craft Model](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQY1VYbVRXMWFlNzJCemo4My1SaGd1V1V2MkJ3elRJR1lKaVJqNlVobnUxTnA5bEFNWklWaEZEZ0t2U2xQeFlXRS1peUVqVHdFeHJCVkxEQzZ2elZ6SU9FZE5IcHhCd0FzNUg5Tmthd3FITlUwelotMHk3d2F2a3cwOFBsT3hYZG15OGF5RUw1UnlJODhrUjJrdHBHRmN4ODMzWk1CZ3lGbnNyMHM?oc=5) <sub>AI Insider</sub>
- 📰 2026-10-25 [Waymo Is Accelerating Robotaxi Deployments. Who's Trying to Stop It?｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE83QXNrSG5UMnZyN2ltY3BENUtsUVBVVk4zbnpNTVNCTENELTBYZjVpY0NqMnFRUFYzVmdMSWdzVWswU1NZWHBRSkd1N3E1WnZxbUVaZ2tneWlmQWU0dTVZ?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-24 [Over sixty Stellantis plants bet on AI and robotics to fix manufacturing chaos](https://news.google.com/rss/articles/CBMisAFBVV95cUxQY1ZHYlRLUmJVTFlzTWJiZzBNejVLbFdlUXVFUVRSNFVRRHk4LTJ5eGdLN3NPVGRmMjNwby1iX0lWSE81TzlfX0dDWmFFUVBaNGo4QmlQOWFoY19xLWozcnI4WUFkZ3AweGRObzZjV0JqWnZubWdPbkdtVWxzRzYzR2ZMWlQxQ09jZnc1bHk3TmxfX3o4Sm1fekxaVjUwbHJHRzU2enZDT3RZSGxzN3FRNg?oc=5) <sub>ClubAlfa.it</sub>
- 📰 2026-10-24 [China's Baidu tests robotaxi on London streets, World News](https://news.google.com/rss/articles/CBMifEFVX3lxTE8tWW5taWpYWllPUkx0WVE1S2s3Y1B4UDEzTHliWWpDaWZfOFp5RklzejNuSEJBNXJSZ0h6UlV0R1E1QTJNVlZaTjQ3NFY0em9NalZOeHdaZzFrYjlFWG1CUnBESExUVV82d21fb1Z2UkhOTmw0SHVVeUVhYW8?oc=5) <sub>AsiaOne.com</sub>

</details>

<details><summary><b>Momenta</b> (110)</summary>

- 📰 2026-10-26 [央视全程直播智驾上珠峰，风神L8+重新定义15 万级智驾天花板](https://news.google.com/rss/articles/CBMiaEFVX3lxTE9kR2h0cHFzZEl2emdNUjNNM291UFpzT25uNF9zcGpvQTVYS3dfdUZmaXh0ZzMwY19ndzdQcXY2bDVHUUNWRG9IQ3JYWW5xZ1pkS2tyU043eXFHa2taSFFlYmlhZ2hTTVFz?oc=5) <sub>盖世汽车</sub>
- 📰 2026-10-26 [【视频】抢先实拍东风日产NX7，宁德电池Momenta智驾，插混大沙发依然最强](https://news.google.com/rss/articles/CBMia0FVX3lxTE5jM3hGYzZlMElvMDYyeENRSldqUWhMXzFSVHAyWWw4ZEtUR3RfNFNmdS1zbldfbTRhZ2Vqc1Rqek5INVE2V1VuM0c0Y3YwV0pFZnYzNHZJNzdRbEhSdDRTZUtOM09DajRvMmZZ?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-25 [【视频】深度测评上汽大众ID. ERA 9X(2)，拆解底盘结构和用料](https://news.google.com/rss/articles/CBMiW0FVX3lxTE0wZU9wVWhYdV9HSExPTkF4dEVNYjh1RkR3MEVkdFBVdmVrV3Y3R3ZLUFZnQXN1UkVNbXR5dHc1bUNpVTg2LTJmZGJUZ1RNaWhPLU5GbkdkejRSbVU?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-25 [带激光雷达的豪华插混SUV哪款好？激光雷达与Momenta R7智驾硬件横评，全新XT5入榜+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFBONjVqeHpYM0JnLW9NS1pXQUdmQ1poZ2hqQ3pBQzI5bkR4Nl9wZU9DaGZsZktQenJxNnBzOWR6NzhhSE94X01ZdVJpVVlldkUwbTFaRU1BLXczZkM0enhidkUyREpjN2N5XzlZdzczYUZ5QQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-25 [DiDi Shareholders Overwhelmingly Back Hong Kong Relisting; Want Independent Director, Open Earnings Calls, and First Shareholder Meeting in Four Years, Survey Finds](https://news.google.com/rss/articles/CBMilgFBVV95cUxNM1VkSndqYnRHN19LQUpyN3Y0UjFGUVRfanVkYl9SaWUydXlPaHdjSHU5anhBS21SZDVhUjVmUzV6bnFGNUxEWG5uOVRKblFaQWtZSWIxcS1EX0s3UmdWaWZscUMzUmNsNkRGNmRYZUtjMENDU1g2UjhUTzRqbVhqaG9GZlRlaFJ6eG5ZM3h1NzZ6S1B4Rmc?oc=5) <sub>Yahoo Finance Singapore</sub>

</details>

<details><summary><b>XPeng</b> (246)</summary>

- 📰 2026-10-26 [XPENG receives approval for citywide L4 Robotaxi demonstration operations in Guangzhou](https://news.google.com/rss/articles/CBMi4AFBVV95cUxOOGZFai04eDV6ek5oUTJQOUFHQUpfcW8zeDVfZVVjenlycHNlMHh5MXpKWUZOWV9idmpRU3d3c1BXcVhZaEUwRHB2dGNxYWh6Q3J1QU0zcE1rT2lnMEVBYzNTamtPUEFtLXlwMnYyblRnQUhSYUMxcWo3LWM3UmYxN3hHY2Rnb1pTdS12RzlvcnlVcFhOMVlNdU1oMmFYQU1XR2pJREdfMGhHUVpuOUJFUnhHN0xhdDR6M21CYWRObXB2OE5IRHlmU3pIeFJsNTVFOEF4LXdMMmFMNDFmb0pmdA?oc=5) <sub>Gasgoo</sub>
- 📰 2026-10-26 [25万预算新能源SUV怎么选？小鹏G9L对比理想L6、问界M6横评+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE1fNWxhQ3J2dzYyTkxCaVRTWk9mZGMyTm5FZ0RaeVhvemFtRzFtSVYwZFRic3VqMjZtaHR3b1V0S200QlNFS1hSLUxMRmkxX19VVHBlT1RtVDA1SFdLWUxxS0pCN0JLUjg0U2FtTVVXSVR2QQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-26 [智能体验好的大五座SUV推荐：小鹏G9L、理想L6与问界M7的智驾横评](https://news.google.com/rss/articles/CBMickFVX3lxTE1lTzl1Y3lYVmtQYWpxZWJUUWJjZFk5Z1BnS1pvenJLVkh6eWxjOGVJTUE5OEt2eTRnbndWN2tTY3JQcUQ0aVNibnlQbnBKcmJBQWNualp4aExrOWN2X09iV3pPOXFtdERLTE45azR3YzI2QQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-26 [Xpeng wins Guangzhou robotaxi trial approval in step toward public service](https://news.google.com/rss/articles/CBMigwFBVV95cUxOWEotdU01T3dnZDVhYzNPWkxCS0hUd24zam9JMXpYTmotMXkxTHh4Z3VtbFpkUEd3bVdLV1dsU2JUTGg0VXJtZ0M2NXlnbFFfYmRZSFgxQXpOM0JpTnN6WlloTUlTbXAydkpxRXdhOHNxNzRRUTZuR3N1Qk9iajFPelhDWQ?oc=5) <sub>CnEVPost</sub>
- 📰 2026-10-26 [5米级、5C超充、小鹏智驾全给了：大众与众09只差一个招牌](https://news.google.com/rss/articles/CBMi3AFBVV95cUxObXFEbUFNYXVnTENJb0NsRDFrM2NlMHVtU29HQTVGeWt1N2lDakphMGFBclEyTHlMWUJmeXVLWFk4dXJzbGk0b1B3T2phOHlxYm8xVUxBcHdaaVd4eTYtNFlDYzdnd0tGODZfLWxzWkh6bnYzWHdjTExocXY0bUhubXRPck41eV9CM29XSWRlc2V0RDFlWXlQaWZlM1pIUG5wcHJQSEV2S1BUZXdzWlpBS1FLY0pQdGhjRVZhaFVkN2NmQnlRTkx4ajVtV1Q0YWRGWFZMRkNtWTgtRmxD?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>Li Auto</b> (159)</summary>

- 📰 2026-10-26 [25万预算新能源SUV怎么选？小鹏G9L对比理想L6、问界M6横评+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE1fNWxhQ3J2dzYyTkxCaVRTWk9mZGMyTm5FZ0RaeVhvemFtRzFtSVYwZFRic3VqMjZtaHR3b1V0S200QlNFS1hSLUxMRmkxX19VVHBlT1RtVDA1SFdLWUxxS0pCN0JLUjg0U2FtTVVXSVR2QQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-26 [车企电池自研真相：理想26.5亿入股，比亚迪全链掌控](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9WWjBLa0NpUUVickFnOHdKTEFqZHJPNFBMVFlnV1YyaU1odngxNVJ0cmNlQTBLbDFSQk5taEdFcnh6WTJqQm96ME5mcUlQYWE4NjBrWUMtZVRwZVE?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-26 [豪华大六座与全地形的交集：神行者8、理想L8、领克900横评](https://news.google.com/rss/articles/CBMickFVX3lxTFBHTnZNeno1ay04MWZNZGpzU2hKblpnWTVxZEhBOVJLQWpTUFRYU2ZobmwxU0NRRXYzSlBWYWtLV25MSXpOVjQ0Z1o5Q3NhWmVpVEhaRHRiVjFiOTRhS3hqRmNzWTRtRlYzc3NnYng0MGlndw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-26 [舱驾一体谁更懂你：小鹏G9L与智界R7、理想L6、极氪7X智能体验横评+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE5KeGRYVkdOb2VXZ0xmNnhzWVVFenlEam9uRVo2T2JUNHpRaHd5blhxZHRfUFhzT2g2YWlQVzVrN1BhXzIzM0FGNThUc2hkOC1LbVBsUkQxT1pyNXRTb01pY29QbnA0SVpmVGc5dERFSXlCZw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-25 [舱驾一体体验如何？小鹏G9L对比智界R7、理想L6等智能大五座SUV横评](https://news.google.com/rss/articles/CBMickFVX3lxTFBPYTRzSEJySUxONGgyM2NQeDVxQ0ZYdXl6YWVoeU9ReWtYR28zUWJuRm1GVGJ0c253MEZrSVZ6TU90Z3lTNnZKeXF4S2lsSGVnWVdmVVY2UlNRNU5Rc0lWa0h1UGo1TnB5c0hjSGd5OXl3QQ?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>NIO</b> (162)</summary>

- 📰 2026-10-26 [变道时别克130码超车 蔚来ET9智驾抢方向盘出车祸](https://news.google.com/rss/articles/CBMigAFBVV95cUxPVkRXeFJuMkhBbXkybVFGMjBGN2xVWXlQVDB5TmZVUVdtQnlveERySEJIUmgwTmJQX3MwT0FIMjVZMjYtTTNvYzdPNEQzbkh0aExyMDlyeW1pV1ZTcFVzSXhCU1hiX1NfTGNoWDZkOTRmTmNLYlFzV3ZJNEY3WWRhTg?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-26 [4款热门新能源豪华SUV横评：经常长途自驾，凭什么神行者8成了川藏线上的移动观景台？](https://news.google.com/rss/articles/CBMickFVX3lxTE5BOHJISGY1VEpiMzYwYmY0YzFOVWk0MTVTUWNIbVB6NVpnczFFZWpNNUdDajhvTFM4bjdpZFZzQlZ3dDNwTy1PeTNZUmFTd2ZZTzA0X1JUd1l5TEtwSzBVbkV6dmdxbDgtUmtkUi11SUJNdw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-25 [舱驾一体时代来临：小鹏G9L、智界R7等智能体验好的大五座SUV推荐](https://news.google.com/rss/articles/CBMickFVX3lxTE1KT3hFVmtHYmZBb1FjVmFuS3M3QTVreGFKZkdRa1dqQjJraFVxLWVZeUJTcHM1R2Vtck55ZDZtalJRNVNGTnpTZ0dhNmRrZV9IdlV6c1drV09TWEx5eW14MjlPeWpRb2hka1RhYjFKMExaZw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-25 [舱驾一体重新定义智能SUV：小鹏G9L与4款热门大五座横评+选购清单](https://news.google.com/rss/articles/CBMickFVX3lxTFA5cGhDQWVaRWJWUzJNMW9qSnN2MFg3ZHNfbzJEZWVXUDI3OE5ET2NsRkJSZTdjS1RMTTZJbnd1bXVkaXgzV0QtVGl5RWVHVlE3OUZOa0p5ZE9BVmJkU3VreTk4QzgyaTZ6SU1fTE54eGlWQQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-25 [蔚来ES9值49.8万吗？3个维度拆解50万级纯电大型SUV+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE53cVBJcEo5R1JGRmRpT0owVlpNSERVUEMzNlM1a1F5RFJtRk8weDIxeGdiSGJPUzBRQ285eGVQTzMwMzB4UVVyWnQ0d1ZVeEY0OTJ5YzU4ekZ0cm1LUG1sMXlocFozc2JPSUhRTWxyTGY2UQ?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>Huawei</b> (353)</summary>

- 📰 2026-10-26 [20.98万起！猛士X700正式上市｜带华为乾崑智驾的硬派方盒子来了](https://news.google.com/rss/articles/CBMiW0FVX3lxTFAwdGFPUDVCbm9WQm5TNnlid0tIeG1BTkJObTZIT2NlYlZXYUdBQ1VlamhjMzh0SUtIclRBVWN2XzdzUUtadGxMZF9KN0w4dkxLQWVURVNYUHY0T00?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-26 [猛士X700携华为智驾21.98万起售](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1PZ1gxVW9xd3hGdHJKTEMxb0ZtZ0czeDdRTDJxZjNfaUhZdlR4V3NZTF9WNHJhYmpKY3ZJaUx0ZDdYaHk1UTkzZFFNUUFnREhWQW9BYmdvR19HS2M?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-26 [豪华智慧全地形SUV猛士X700上市限时焕新价20.98万起](https://news.google.com/rss/articles/CBMidkFVX3lxTE9yR0VaclZMYjR5dnNpMUpoQzZtTE9wQkZrNEFoUE5DT204d2ZJMGQ1b09GOHJGYlI4eTE2NHQxbHFoSlFvSHc4M0JKZlJuZlJaejUyUUIwYUtUaWFDMHlmS0VabGlIZ0lyM3FJX3pMN0k4RE1pb0E?oc=5) <sub>新浪新闻_手机新浪网</sub>
- 📰 2026-10-26 [10月26日开放报名，10月31日开赛！第二届华为乾崑智驾公开赛](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNMlhMeExlNjQ1ZnNpTS1YRjNoV1ZVejR3QTJjZ0o1TFJydGFQcEZibWszVXpFb0cyeklkYmEzR0FjLWU4Tk5xTWJ6VVZZN1pUMk9sWU5lZHl2MW1WeFpOTDBXcnF0WUt5cmc4Slh0Uk9QVFFHMWcwbW9hbXVJN253Q2xNZmhRcTR2?oc=5) <sub>Sohu</sub>
- 📰 2026-10-26 [People Who Left Huawei: 23 AI Entrepreneurs, 18 Companies, A Commercial Journey Beyond the Gates](https://news.google.com/rss/articles/CBMiU0FVX3lxTFBPMVFfQXN2WXRzcGdwSTh6UTBrVVlMZXFZalgzXzQ3VG9paWJSdWphZW9ydXlGbmFfUnh0Nk1ydXdTLUhwWDJOUlVmV19FdGtUa1Rz?oc=5) <sub>36Kr</sub>

</details>

<details><summary><b>Baidu Apollo</b> (53)</summary>

- 📰 2026-10-26 [Robotaxi赛道又来狠角！小鹏悠游拿下L4级自动驾驶示范运营资质](https://news.google.com/rss/articles/CBMif0FVX3lxTE80R1FKeUFrOXpDaV9HaXlDeVI3a2JtN0FsSGZJQmZJS3VIMkxYVU12R1d2SVNqbTlTQzFvWVFmbEZ5U2xndVFPWlNudXBYSVV6eGxjSjl1WkthUzJpMjhYbUtWYU5FRFpubzdrZk13cjZpMHM2eGN1VG1EbklnWUE?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-25 [Driverless electric taxi fleets learn to adapt to the unexpected](https://news.google.com/rss/articles/CBMipwFBVV95cUxOVmJON3FFZENCby1DVzhxeGluc0FLN29qdW1tTk4zSGU3eVZnM0xxYkFnS21hOHo1NHFfOHBoZ1ZtZXcta002SjVyekl3dmNoTkpYeTA2d2ltdFlDcjFjV3NfMWlEcGFtRHA1NUdmbC13ZDhoX0k0bzJvSGtQNzFYYUZmdHh0TG5QbjBqQWl4U21BS29kdlhkZEhzOFdfeVE0ek5DX0lqVQ?oc=5) <sub>Digital Journal</sub>
- 📰 2026-10-25 [Baidu, Inc. $BIDU Holdings Boosted by Corecam Pte. Ltd.](https://news.google.com/rss/articles/CBMisAFBVV95cUxPR0RTNFFxTVJCbDNZbXNOaTNTVzV2c3lGYVMtVC1LajhWN3hNMU9ZTnhia3JJMFJtdXdLVXBEaXN6cGJGNTFMcGZHcThyNGZDUkFNdS1zTE9mWGd4WUwyQnJ5NFY2RDgyNFEzbmcwMkFhc05lMTZ0M25LZGs2M0lLVHlXUWZzNTlaZnlOOEUxa2FSRTFNaVoyb0QtTVpacmlPczA1NkNUT1lpX3JpRjRqWg?oc=5) <sub>MarketBeat</sub>
- 📰 2026-10-25 ['Full of excitement:' Sydney's new airport opens to passengers](https://news.google.com/rss/articles/CBMiekFVX3lxTE1nbW1GTmJYeWF4ZnVXbk8tWkNBV2lTcHNUU0xQS1htVGZ1VEszLWd0QWlZbnYwOXRVRFU2elZabUFBTnNiWENucmVOZnVja1FHREdoNm91NGFrMDhlRVRELWVSNk1PZkNQRGVJV1B1N0FjVG1mb0dfMkxn?oc=5) <sub>Reuters</sub>
- 📰 2026-10-24 [Baidu and Lyft Showcase London Robotaxi as 2027 Rides Remain a Target](https://news.google.com/rss/articles/CBMiWEFVX3lxTE1tcENqVlgweFRQQ2VFUmpkbm93ZktIVEFKX2VuaUVtTUVhSlk2TTY2MUgtTTlucUZnOGZ2N3B3bjEzZjBwMnVQcFBHWDcwaWE4TUVFMVRQU1c?oc=5) <sub>TOKENPOST</sub>

</details>

<details><summary><b>Pony.ai</b> (151)</summary>

- 📰 2026-10-26 [Pony.ai Kazakhstan: Astana Robotaxi MOU, 5 Takeaways [2026]](https://news.google.com/rss/articles/CBMigwFBVV95cUxQMXlZcDlNZVJScEtuVjY3c2xzeGRYRnBKelJnRUlOWXp2Z3R5OW0tdXluMEVpaC1qNGg0c3p5WlptLXhocU8xUS1HdXJ5VjFld2xPUEdZMmhURjdPbFQweGRmdkF4Q09tUVVSOE5hZGx3Q1pnQk1TQ3NrdFF2NUd4RGJ1OA?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-10-26 [inDrive and Pony.ai Announce Kazakhstan Robotaxi Collaboration Using NVIDIA Hyperion](https://news.google.com/rss/articles/CBMiugFBVV95cUxNZ3RvSm9KeXB2MDFwX1pEWExvS3VlZDNGNTdLSWkwV1R1VE9uclRtVU5vTEtBcDh2dlI0UHZFaE1jTzV4aHpRcmpicUNDaUlxZjBFQWI3cDg0NXZYLUJUQkQtNDBBN1cyaWVpSGhSM2pkYWM2M2M3VGNYelBhUmgzMFdXb1p2MlhYQW9fVnhXMWEtWHVqMEw5Sm9BTXNNdnBxYV9LVTAyR1UtZ00zOE40YXBLSE42RTRsc1E?oc=5) <sub>World Business Outlook</sub>
- 📰 2026-10-26 [广州全域L4 示范运营，小鹏Robotaxi 从测试走向商业验证](https://news.google.com/rss/articles/CBMiY0FVX3lxTE5kVWJjc3ZrZ2ZjMFI4X3dUZUZlUHhGU3VFSzVNVHp0dGExZHJxQlgteVQta0JKdHhjR0dmUm5QdXptMUkwc3ZRV2FuWllQdG5RZ3BkdXJPQXE0ZWlGRXVQd2VxWQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-26 [Pony.ai, inDrive, NVIDIA plan L4 Robotaxi pilot in Kazakhstan](https://news.google.com/rss/articles/CBMiuwFBVV95cUxONzAwOUUyMDVfa2c4SzdVUWtOM3FfMGQ3NXlmcG9vTXpnQ1ZQQVU3R2FDQW4zMndWUUZCS2lwRXV6TW5maTk1TDNPV2FiRGZOQmh1MDNzZTdiNEI5eGdIZnNoazFabzd4TUV2cDUtSEJBYUl3b0NCVGI5cE5yY3Q2ckUyaE9HQmVKeHd3ZTI4dDAzTEJveVFmUnFyUEM3XzBxWWRpUGM3LUJ2bEJHS3RYVWVHbjdDVjN0MFlv?oc=5) <sub>Gasgoo</sub>
- 📰 2026-10-26 [Robotaxi赛道又来狠角！小鹏悠游拿下L4级自动驾驶示范运营资质](https://news.google.com/rss/articles/CBMif0FVX3lxTE80R1FKeUFrOXpDaV9HaXlDeVI3a2JtN0FsSGZJQmZJS3VIMkxYVU12R1d2SVNqbTlTQzFvWVFmbEZ5U2xndVFPWlNudXBYSVV6eGxjSjl1WkthUzJpMjhYbUtWYU5FRFpubzdrZk13cjZpMHM2eGN1VG1EbklnWUE?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>WeRide</b> (153)</summary>

- 📰 2026-10-26 [广州全域L4 示范运营，小鹏Robotaxi 从测试走向商业验证](https://news.google.com/rss/articles/CBMiY0FVX3lxTE5kVWJjc3ZrZ2ZjMFI4X3dUZUZlUHhGU3VFSzVNVHp0dGExZHJxQlgteVQta0JKdHhjR0dmUm5QdXptMUkwc3ZRV2FuWllQdG5RZ3BkdXJPQXE0ZWlGRXVQd2VxWQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-26 [国产医疗神经接口龙头企业亮相北京CMEF 品驰医疗携前沿脑机创新成果迎接全球宾客](https://news.google.com/rss/articles/CBMiUkFVX3lxTE5ZejZQckFJaTBvSHNsMXJxaE9QRVlEUjhnbUpCUDVuRDBIT0NsS1hsU2hLZko5VE42QnAzbDkwdWpRT05kVDJqZFNnOUlIOXlnT0E?oc=5) <sub>www.icloudnews.net</sub>
- 📰 2026-10-26 [美国超微公司(AMD)讨论区- 股票评论- 股吧交流社区](https://news.google.com/rss/articles/CBMiX0FVX3lxTE92cGk5ZkJsMTZKcUp6R1JYZWFKd3U1Q2xZa25fRm9mb3ZEZnoydXpYWE9idW9Vd056OTMyVEtnUnlULTZQbHlWeno3YmRtM1g4dF9QSDgxdzRXbkFtcUpv?oc=5) <sub>Moomoo</sub>
- 📰 2026-10-26 [泉城入梦｜Simmons®席梦思以非遗剪纸跨界演绎东方美眠新境](https://news.google.com/rss/articles/CBMiUkFVX3lxTE9HOC1YXy1aRnVtU1pHQVJRVFpOUm4xNmgtWmR2ZGt2dmt6ZzFCa0hwemxCLXNldzRDRUExNGRrb3VpdG04cnJ1OVVlZVFJeThUNGc?oc=5) <sub>www.icloudnews.net</sub>
- 📰 2026-10-26 [讯飞听见亮相2026科大讯飞全球1024开发者节](https://news.google.com/rss/articles/CBMiUkFVX3lxTE5oS25rOUVvaVNBdVdUYVZYTlFDOWxIZ21XNlRpQVdyOTE4dkN5WjFfVW51elFVOEtOeTFIZWtuTDNtRURHYUVvSHFiZm1UY0l3akE?oc=5) <sub>www.icloudnews.net</sub>

</details>

<details><summary><b>Horizon Robotics</b> (156)</summary>

- 📰 2026-10-26 [智驾新程一段式端到端智驾系统量产搭载长城大狗HEV](https://news.google.com/rss/articles/CBMiUEFVX3lxTE1NRnBaRXJVX0xOWXByOXhud1gzYUtnc3ZNeWp1YnZOb0Y5Mnc3NmoyS0RKQy1lNVRaZmN3cFZYQkNCRDFBWjFtbWN1bEM4QVdS?oc=5) <sub>盖世汽车</sub>
- 📰 2026-10-26 [大神Jim Keller再融15亿美元，Tenstorrent 到底能做出点什么？](https://news.google.com/rss/articles/CBMiiAFBVV95cUxOZDdGLUdjMW9EVGVUcEhRTDNET29zRjF5cEdUNjBlOTVnTzkwNHo1UU9DMEtVWVNJVExOVkN3R0dRMzF2V0x6bWF0VDI3Q3ZyT0J1UmhsQndpZnhqQ2JJRG9zVUNnNUVnNW1QMUhpNVdYQVhVMV9hd3NBeG9zT0YyZmpXOWVUUk83?oc=5) <sub>Sohu</sub>
- 📰 2026-10-25 [捷达电动化“第一枪”： M6冲击8—10万元纯电家轿市场](https://news.google.com/rss/articles/CBMijAFBVV95cUxPamczYjZ3T1E1dFZwcTFSbUZ4ejc1Z2s0eU8yWkkxUkctS1U4TUNRcWFpM3VTSGloNXFzZW9Oa29VRDJhOEV4NUpycDRlcEx6dU40U19VZnZlZmVIdkI5dW1FMkNTdWVBd3NBNWNwTmNybXcwQVJKUnFPREVNSlhhcC1aTnducmtyeElIVw?oc=5) <sub>手机搜狐网</sub>
- 📰 2026-10-25 [iCAR V27正式上市 售价16.98-19.68万](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1NN0pvbFNPaGk2U0g0ZEk2Tl80THNHcnUtOVdSQ3BNejZ5cGx3TkZMM25Oc2htRS1zRFlsazEzbG4wOHdoemxNcjgwa1dIcXhKaHVRbVgweUJ0dEU?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-25 [带娃露营装车，ID.AURA T6和零跑C10的后备厢差距在哪？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE84VGtKb2dTdlNObjRaUzdYSUpYQzJ0cGRTMy1Vejh4Ujd6bTFjWFVRMFdYSE0wbDJ1Y1dlbFR6Sk4xMVE3MDM3VU8wVVo5T0F5cDlMWUo1T1FhanM?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (36)</summary>

- 📰 2026-10-24 [4款7系SUV扎堆上市，问界M7车长5080mm](https://news.google.com/rss/articles/CBMiW0FVX3lxTE14Njc1UEhVa2JDUjZldVh5cm9SaHl2bTB4dE5fQnVEbEpuUE1UTzJQS0dXOU50UjVYYm9IeGwyVFIzQ085QktXaFBvaExySzQ5VFROUnoyY2hCT0U?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-24 [从2026 WICV演讲看：文远、元戎、智驾新程把智驾的下一轮押在哪？](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1UMzkyZlFUZFdhS3l3M1dPYVAxemFzYjRHSFlnWjJUbEVzaDgzRF96VUJiUFhPWTlNdG95czM4NXg1Y0ZlY1JiY2VyV1YxcFZxblpv?oc=5) <sub>电子工程专辑</sub>
- 📰 2026-10-24 [欧拉5城市NOA值得买吗？11.58万带激光雷达，3个维度说清+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE9tdVFPMXpMMGg5UlpDNGt2RzJIMVJ5Slk4dG5SVGJxM0dqaENiNHhVWi1TSWFYTXFuc3VvMXdJMFdHOEY4cUNOcF9peENCbmxFVlVxcDRIMUlUdVdpaTYyWGpaZGY2Q2F1UGxTM1lVU0Zkdw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-23 [元戎启行周光：基座模型成自动驾驶新引擎，推动MPCI向千公里级跃迁](https://news.google.com/rss/articles/CBMiXkFVX3lxTE9wRGVmQ3liVG9hUjNic1QyekVrS3VKVUNZbFJ5WHc2dlR3UHQzdGhCRFVROHVnTl9NLVdENGZIM2hUT1doV01USEtvSHJsaV9iclpoWEd4M1hfVDZFMFE?oc=5) <sub>SmartHey</sub>
- 📰 2026-10-23 [US: Waymo Launches Services to Harry Reid International Airport](https://news.google.com/rss/articles/CBMinAFBVV95cUxOV2M2dkZzWEw4TXdrbU1kMzlPelNRbk5FQU5YbTY1MUNoRUdITmY0a1dzSUZjWE9JdXotNkI5Mkg5RzZQMlZORlM0OUppSVNlc0llbVFMa1NJNHpzLWhEbkl5RC1wSnZsUFNoVDJyUlgxa19OTWVGRFBvMHBIbDlYZllzV3NQMjMwMklTSWp6NWZqaDVuZndFUnpjckg?oc=5) <sub>Future Transport-News</sub>

</details>

<details><summary><b>Mobileye</b> (26)</summary>

- 📰 2026-10-26 [Autonomous & Self-Driving Vehicle News: Tesla, Mobileye, Aeva, Ouster, Pony.ai, NVIDIA, Stellantis, Bolt, Wayve, Volkswagen, Einride, Valeo, Aptiv & TIER IV \| auto connected car news](https://news.google.com/rss/articles/CBMijgJBVV95cUxNLXpSRDZNWTdpaUNvcWdGUWJBRUxfMGlXTXYtNFEyV0NxU0hfTmhxUlQwb2JGN3Y0VW9QS25NeVRPNkxsVV93ZkZGdGp5bW9iU3VERTFwaW5MckVKc0xmTEJVR1NFTFJORXR5SVZ2VlNDY0VFRjhabEo4dkp4WU1xTFpYci1kcWNsNndSNHg2cExQUVlCRVEtb1plX0dLa2diaDV6eU9hX1dnT1pOTmVkZXBNQ1pnUHlZQ1BVX1FEWWJfcS1fejBXbUdWZE5qZDRDUGtmTnFUZVhYTkItWlN5emwyMnRGNWFITHVDTEZwQk9hdXpJT3d3N2UybExoRjRtLTVZUFE4ZFBZQVZJLXc?oc=5) <sub>AUTO Connected Car News</sub>
- 📰 2026-10-26 [Connected Car News: OmniAir, Arbe, MapQuest, State Farm, MIT, Google, Apple, NXP, Mobileye, TÜV SÜD, Audi, Spotify, Mercedes-Benz, Hyundai Mobis & Samsung \| auto connected car news](https://news.google.com/rss/articles/CBMijAJBVV95cUxQU0RRRTJIRGVJZllKWlNWTVREYl9lSzItOGJNU2VwOGo2cWdDT1lXQVpVNWd0ZnN3RnIzVU5pWUluNF9BTUNWUEhQTTZ3bmVCOUtuaGNkdDJEY2dsMGxTVU9iOHROazVSc29TWktSZUZ6V2tJRzViQzRob3RpTWJpQXVfSUJtMXBMVVFWTjk1b3RRWnpaWnJwWWc4N1J6bjl5dlBmX2xHYXVvZ2p0MXJzalJYTG81ZnhkUXp4SzhLQkZRNEV3c1Y0dm9lQ1FldVRqS0NQdTdMMmxkZFVCTXBoUVJMSHNwRk8tMWs5cHFxaksxeGFCdlVaTnZxdk5ucWM3eWhpYkkxNHZ2bGEz?oc=5) <sub>AUTO Connected Car News</sub>
- 📰 2026-10-25 [The Volkswagen ID. Buzz Robotaxi Is Hitting LA Streets](https://news.google.com/rss/articles/CBMiigFBVV95cUxQVnBCOFFaRFlDdFFJakpKYTA5Q0ZhUExWa25faUxINEdVYnZJaldGcVdDQXRoR3ozWmMyLW44U1RNZHVHUzBUQjZ3U3ZUOU9fNmpXYlpwQnFzejV2cFBFeHFNMUdLblM1NjlEbUhGUzZDUzRNaUdia21DcGwzY3ZjMHlwLXltV2VqZVE?oc=5) <sub>InsideEVs</sub>
- 📰 2026-10-25 [US Auto Manufacturing Stocks With Real Onshoring Backlog Growth](https://news.google.com/rss/articles/CBMiwAFBVV95cUxNYTFqM1RUek15WTBwZVdYLWNnWEx3U01remloTWFzR0VaSUdVNjhJT3BpOWZ0VEt6c1ZnZVhQR0MwTy1ZaFB6amVpdFVRWm5wSDVrM3hNRDZ6WmsxeTlJNkNoTlBpNjRKUVZaZWJvUFg1UHVhM0NuelU3SmRUck9vclF3TU8tQU5iOERGVy1hQjMzbE45UzlXa2ZVc2dfbk9DTThBdldjNi1aQ0xrSFY1LW1JazZjV1duc2ZITXJNT23SAcYBQVVfeXFMUDgzZktZRFhIaFVuTHBzYmJZX3d3Zm84azdkZFhWRi1jMk84VkVsb3dzRW1OSGtncEdDYXJxbzZUU0tCR2xKc2JIQ0RvOV8xdE1UVm1kZHJQcFR0VHVKZjZuM1V4OGpnRF9DVC12SDBMd0I1WTRPSGREZi1IQ09iNmpGR2xJbUJFOFlrZk9rWFV3UWxYekJBamJOdng2VjVLNUw5YVU0Y1otaGhjdk5pMHppS3JOT0l1NVQteDJCVGVUWTRyejR3?oc=5) <sub>Simply Wall Street</sub>
- 📰 2026-10-25 [Israeli autotech industry has shifted into drive](https://news.google.com/rss/articles/CBMilwFBVV95cUxPNW51THkxZnp3OHQyQzhqVkdDX256bXVCcmNuVmRtMG03cGI1Uk80bUk3bE9ESGdoYXhzS2dXUUpZc1ZVckJDbTZYdU9kM085QkdFMHc2aDhuM2pnaWVTSGZlZ1hod1I4RTFHU2dJSkhZeGdRbFlNdXBsSlIwY0lRbzBVMDd4NWlRMEpCQWhMazJfMDZzaG9J?oc=5) <sub>PEI Private Equity</sub>

</details>

<details><summary><b>Aurora</b> (46)</summary>

- 📰 2026-10-24 [Some US transit systems weigh whether to run trains without a human at the controls](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNUk11OVZhb1dSNnVBMkFpcjg5bjV4VkdBbXhmS05mRmtXd2xBaG04QjFLZEJidXl3NVVvcXdNd2VNaFQ4TTNpTUo4dnQ5SFdyUGRrVkEyUE90SkY5b1NTQWFKdE5KbWVpdzRRdF8xRWExZk5JZ05zYXo0WENfcnZJa3lMT3gzY1hM?oc=5) <sub>Yahoo! Finance Canada</sub>
- 📰 2026-10-23 [Driverless Trucks Log 1,200 Miles, Observer Returns [2026]](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQcG1PcHdpRkFhcENGLUpkbTl2LTNWdGRKdFVfbmJBYV9TMFhHMDJzTlZDTDh3aFh6bnYzS1d3YlJmS01DRVc1NGpLNTBseVZqS05LSDBBX2tsNlhsN3Jid3dGNTRxeFAyNVVJQzBxYmkyaExDSXlfaXZWbE0tQi1ZYXdMOWVxUFFqT2dz?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-10-23 [Self-Driving Trucks on I-45: 240-Mile Route [2026]](https://news.google.com/rss/articles/CBMihwFBVV95cUxPaDFqOGxqUlRHZEFfNVJCMGdJUndhZm1EbldJaWJxamRFbkt0TE94blF3U2ZTMUJFbkxSZWtFNHBqUEhab2daeHZwSFVsVFZFeWNtV0M0elEySk1sMTdTbk9VNzI1dFk3OEgyLWg2dFBIenVwNGFkSzMzaklnYXhfa19TUjdsM2M?oc=5) <sub>shattered.io</sub>
- 📰 2026-10-23 [Self-Driving Big Rigs on I-45: 650-Ft Pole Spacing [2026]](https://news.google.com/rss/articles/CBMihwFBVV95cUxPaDFqOGxqUlRHZEFfNVJCMGdJUndhZm1EbldJaWJxamRFbkt0TE94blF3U2ZTMUJFbkxSZWtFNHBqUEhab2daeHZwSFVsVFZFeWNtV0M0elEySk1sMTdTbk9VNzI1dFk3OEgyLWg2dFBIenVwNGFkSzMzaklnYXhfa19TUjdsM2M?oc=5) <sub>shattered.io</sub>
- 📰 2026-10-23 [Einride Puts Nvidia’s 32B Alpamayo AI in Trucks [2026]](https://news.google.com/rss/articles/CBMickFVX3lxTE9qWk10YmdBcWlpOUJBVHZXQ2tVYUNaUEN5ZDQ3bmRWczN4bGk4ek1FUnlVX0NoQ2V6UUVSUDBzQVY0Uk5sUzZxOE14dUhHWDZXUzU5MWk3Vm9oWGpaTTRyMWZpVDZheUlfNy1pVDRqcm5oQQ?oc=5) <sub>shattered.io</sub>

</details>

<details><summary><b>Zoox</b> (66)</summary>

- 📰 2026-10-25 [Waymo Robotaxis Now Pick Up at the Las Vegas Airport—but Not Everyone Can Ride Yet](https://news.google.com/rss/articles/CBMisgFBVV95cUxPRkhtbzhqWVBjcFl1cEdFRk1rTkpMQ19paUxkNkZkbHM2WEpucGRwTWNLU3ctdFo0dFZGQXlPQ1R4THFxdmhoakRfbjdubnctRGQ0V1U5b1BNTWNwMi1xdlNmOVZnTW94cW1PbXcyVWw3UWJFQkpIZS1hanhOQmp0ZlJjMkxqNUtIWUxvZjhyRGF3d2NyTzIzaVBFMkdBVVFXMnV3dUJ3Q2ozNk1NT0diMHF3?oc=5) <sub>MotorBiscuit</sub>
- 📰 2026-10-25 [Dawn of War 4’s four faction campaigns grew into at least 70 missions, says creative director](https://news.google.com/rss/articles/CBMiekFVX3lxTE0xcnhZb1o1em5mdjZUbTJyYVFqWWJ4ek1OR1F4Sk83TWdMaGN4Zk44bFdJUVB6MjI1VXBodGJ0Y2pzc1JnN1FSeXlUM19kcURmckhTTFVYdDl1SklKS1JIUmczcTNJS3RaRjhpU1pncWVidFdtb0VxWU1R?oc=5) <sub>Mezha.net</sub>
- 📰 2026-10-25 [WATCH: Three rival robotaxis end up in a suburban Austin standoff](https://news.google.com/rss/articles/CBMimAFBVV95cUxQQ0J6eUFBSzBLanFUWklEOVA3S3RCaVp1dDJwZHJvX0lQUVNXMHBGOVdkR2U0VDNIcFhCM2J5RzBicGdNVkh5UzFDdkhiUkpLYU9yblFqdWZmZ1laSTFtN0k3anVzOWdZVlUtRmFlWDJSYzkxTVdIX1I3UnVpbGRSVm91QTlPOU5FZ2lEUEV5ZVdBdC1BTTZYcQ?oc=5) <sub>Stuff</sub>
- 📰 2026-10-25 [At the initiative of the Ministry of Defense, a military surgery and resuscitation course was held in Ukraine for the first time](https://news.google.com/rss/articles/CBMiggFBVV95cUxNTkRYSTRTVmFxclUwRXRfT0dKR3JPdUR6anJIQXJrSXl0cXFHOXoySnFzcGwzNi1oTGRoZlp2cTFGS0VNaEJ6NnZwUzlhdURPeVBwZWhBZGt4YkR6b0NBeDU5MGRaRGJjdlRTMDloTUtDLWhrNGlXMWpNZTdVNGN1UzFn?oc=5) <sub>Mezha.net</sub>
- 📰 2026-10-25 [THE FUTURE OF TAXIS IS HERE! Waymo Zeekr RT (Ojai) Ride Experience & Specs. Sanne Dijkstra-downie (19BJMDZ81L)](https://news.google.com/rss/articles/CBMiZkFVX3lxTE9DZjRCczZBUXhBc3pYbFhHdVY3QUI1LUVocWlmVkZrbFUxUTAzTXFVYXlMQTJmQmpfZG1IQlpKVFRGSDJoMVlLSlUydHRlUFREb0hlN241R0h5TjhabXRtbWpwN2VzUQ?oc=5) <sub>Unisba Media</sub>

</details>

<details><summary><b>Motional</b> (12)</summary>

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
