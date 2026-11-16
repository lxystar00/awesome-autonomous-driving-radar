# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-11-16 · 1,266 papers tracked · 47 curated.

**Selection rule.** A paper is listed only if it (1) is primarily about autonomous driving,
(2) has public code, and (3) shows at least one strong signal: accepted at a top venue
(CVPR / ICCV / ECCV / NeurIPS / ICLR / ICML / CoRL / RSS / TPAMI, or ICRA / IROS / AAAI / RA-L),
≥200 GitHub stars, ≥3 citations / month, or a well-known lab with traction. Papers are then ranked by a
composite score (venue, stars, citation velocity, LLM rubric for novelty / rigor / impact, SOTA claims)
with a per-topic cap. See [`scripts/rank.py`](scripts/rank.py).

📅 [Daily digests](daily/) · 🗓️ [Weekly digests](weekly/) · 📦 [Raw data](data/)

## Contents

- [VLA / VLM for Driving](#vla--vlm-for-driving) (13)
- [World Models & Generative Simulation](#world-models--generative-simulation) (4)
- [End-to-End Driving & Planning](#end-to-end-driving--planning) (11)
- [3DGS / NeRF Reconstruction & Sensor Sim](#3dgs--nerf-reconstruction--sensor-sim) (5)
- [Perception: BEV, Occupancy, 3D Detection, Mapping](#perception-bev-occupancy-3d-detection-mapping) (8)
- [Motion Prediction & Behavior Modeling](#motion-prediction--behavior-modeling) (2)
- [Datasets & Benchmarks](#datasets--benchmarks) (1)
- [Safety, Robustness & Evaluation](#safety-robustness--evaluation) (3)
- [Industry Tracker](#-industry-tracker)

## VLA / VLM for Driving

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Teaching Vision-Language-Action Models What to See and Where to Look](https://arxiv.org/abs/2607.01658)<br><sub>Yuguang Yang, Canyu Chen, Zhewen Tan et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 38](https://github.com/ShivaTeam/DriveTeach-VLA) | Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving |
| [SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving](https://arxiv.org/abs/2610.20609)<br><sub>Shaoyuan Xie, Zihan Zhang, Jingxuan Wang et al.</sub> | CoRL 2026<br>2026-10 | [⭐ 36](https://github.com/ASGuard-UCI/safedrive-vla) | Vision-Language-Action (VLA) models are gaining attention in autonomous driving, inheriting commonsense priors from large language models (LLMs) and widening the navigation interface from a fixed command set to free-form… |
| [Scene-Adaptive VLA: Efficient Autonomous Driving via Dynamic Layer Routing](https://arxiv.org/abs/2610.24590)<br><sub>Yujia Yang, Quan Yuan, Jiawei Fan et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 5](https://github.com/yang-luvu/Scene-Adaptive-VLA) | Vision-Language-Action (VLA) models offer a promising paradigm for autonomous driving |
| [Locating and Repairing Domain Shift in VLM Trajectory Planning](https://arxiv.org/abs/2611.10720)<br><sub>Zhihong Cui, Hengyu Liu, Michael Alexander Riegler et al.</sub> | NeurIPS 2026<br>2026-11 | [⭐ 0](https://github.com/ZhihongCui/MoLaRx) | Vision-Language Models (VLMs) are increasingly adopted as end-to-end driving planners, yet they suffer from cross-city domain shift |
| [AutoVLA-D: Learn a Trajectory-Geometric Condition from Reasoning for Autonomous Driving VLA](https://arxiv.org/abs/2611.12382)<br><sub>Yuguang Yang, Zhewen Tan, Canyu Chen et al.</sub> | NeurIPS 2026<br>2026-11 | [⭐ 4](https://github.com/ShivaTeam/AutoVLA-D) | Autoregressive VLA planning usually predicts continuous trajectories as the final output, but driving instructions often describe actions rather than ego states, which weakens direct conditioning on the final continuous … |
| [CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving](https://arxiv.org/abs/2607.04179)<br><sub>Zhaohong Liu, Hao Ye, Xianlin Zhang et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 1](https://github.com/MICLAB-BUPT/CritiqueDriveVLM) | End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving |
| [PixelPilot: Scalable Vision-Language-Action Models for End-to-End Autonomous Driving](https://arxiv.org/abs/2607.04637)<br><sub>Pin Tang, Guoqing Wang, Xiangxuan Ren et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 2](https://github.com/VISION-SJTU/PixelPilot) | Vision-Language-Action Models (VLAs), which leverage the advanced reasoning capabilities of Vision-Language Models (VLMs), show promising generalization in complex autonomous driving scenarios |
| [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)<br><sub>Nan Yang, Zhanwen Liu, Linfeng Zhang et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 11](https://github.com/Zizzzzzzz/MVPruner) | Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings |
| [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)<br><sub>Yuan Gao, Wenting Miao, Mattia Piccinini et al.</sub> | IROS<br>2026-07<br>📑 1 | [⭐ 31](https://github.com/TUM-AVS/Chat2scenic) | Validating autonomous driving systems requires diverse, regulation-compliant test scenarios |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 19 | [⭐ 556](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
| [GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives](https://arxiv.org/abs/2609.39601)<br><sub>Qize Yu, Lianrui Fan, Boyu Chen et al.</sub> | arXiv<br>2026-09<br>📑 3 | [⭐ 438](https://github.com/groundingpi/GroundingPI) | Precise grounding matters |
| [GRAVA: Grounded Reasoning-to-Action Representation and Learning for Autonomous Driving](https://arxiv.org/abs/2609.15169)<br><sub>Xiao Liu, Haoyu Li, Jianghao Leng et al.</sub> | arXiv<br>2026-09 | [⭐ 487](https://github.com/AhernResearch/grava) | Driving vision-language-action (VLA) models increasingly reason before acting, but their intermediate reasoning is often weakly grounded in physical scene evidence and loosely connected to executable behavior |
| [Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air](https://arxiv.org/abs/2605.31066)<br><sub>Tianle Zeng, Yanci Wen, Xueang Yu et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 1,133](https://github.com/louiszengCN/CarlaAir) | Recent aerial vision-language-action (VLA) models show promising single-UAV capabilities, such as tracking moving objects and navigating to language-specified landmarks |

## World Models & Generative Simulation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [FrozenDrive: Zero-Shot Text-Guided Driving Scene Generation and Data Augmentation with Parameter-Free Frozen Diffusion Model](https://arxiv.org/abs/2606.20110)<br><sub>Yuhwan Jeong, Hyeonseong Kim, Daehyun We et al.</sub> | ECCV 2026<br>2026-06<br>📑 1 | [⭐ 10](https://github.com/daehyunwe/FrozenDrive) | Synthetic data for autonomous driving is surging, powered by diffusion models that promise scalable scene generation |
| [MESSENGER: Memory-Enhanced Sequential Scene Flow Estimation via Autoregressive Next-Frame Forecasting](https://arxiv.org/abs/2610.10759)<br><sub>Jiuming Liu, Jianing Li, Mengmeng Liu et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 0](https://github.com/liujiuming123/Messenger) | Scene flow can capture low-level 3D motion displacements in dynamic scenarios |
| [ASTAD: Asymmetric Style Transfer for Synthetic-to-Real Adaptation in Autonomous Driving](https://arxiv.org/abs/2606.29286)<br><sub>Dingyi Yao, Xinqi Zhang, Lihui Peng et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 2](https://github.com/Dingyi-Yao/ASTAD) | Synthetic data mitigates the data scarcity problem in autonomous driving perception |
| [Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends](https://arxiv.org/abs/2606.01164)<br><sub>Jiuming Liu, Chaojun Ni, Mengmeng Liu et al.</sub> | arXiv<br>2026-06<br>📑 9 | [⭐ 251](https://github.com/liujiuming123/Awesome-Interactive-World-Model) | With rapid development of large language models and diffusion-based content generation, world modeling has attracted increasing research attention, benefiting various downstream domains such as game engines, embodied AI,… |

## End-to-End Driving & Planning

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [MOJITO: Modal Joint Learning for Unified End-to-End Autonomous Driving](https://arxiv.org/abs/2607.23511)<br><sub>Zhijing Cheng, Xuancheng Zhang, Donglin Di et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 32](https://github.com/mumucc01/MOJITO) | End-to-end autonomous driving systems commonly follow a cascaded two-stage pipeline where a perception stage compresses multi-modal sensor inputs into a compact context and a downstream planner predicts trajectories cond… |
| [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](https://arxiv.org/abs/2609.26792)<br><sub>Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.</sub> | CoRL 2026<br>2026-09<br>📑 1 | [⭐ 15](https://github.com/VAIL-UCLA/DreamStream) | Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions |
| [DriveMLP: When Training Strategy Outperforms Model Complexity in Autonomous Driving](https://arxiv.org/abs/2610.29676)<br><sub>Alessandro Canevaro, Julian Schmidt, Hang Yu et al.</sub> | CoRL<br>2026-10 | [⭐ 6](https://github.com/alessandro-canevaro/DriveMLP) | Learning motion planning policies that remain reliable under closed-loop execution is a central challenge in Autonomous Driving (AD) |
| [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)<br><sub>Shen Zheng, Anurag Ghosh, Gaurav Parmar et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 32](https://github.com/ShenZheng2000/WarpI2I) | Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs) |
| [G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance](https://arxiv.org/abs/2606.26017)<br><sub>Hang Yu, Ye Jin, Alessandro Canevaro et al.</sub> | IROS 2026<br>2026-06<br>📑 6 | [⭐ 7](https://github.com/HangYuu/G2DP) | In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors |
| [SimWAM: A Simple World Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.07468)<br><sub>Zongchuang Zhao, Xin Zhou, Tianyang Xu et al.</sub> | arXiv<br>2026-08<br>📑 15 | [⭐ 209](https://github.com/H-EmbodVis/SimWAM) | In autonomous driving, World-Action Models (WAMs) have improved end-to-end planning by transferring video dynamics priors to action prediction, but many still couple planning with future-video generation at inference, in… |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 20 | [⭐ 364](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
| [Latent-Centroid Steering: Single-Pass Classifier-Free Guidance for Command-Aligned Autonomous Driving](https://arxiv.org/abs/2608.00237)<br><sub>Meibo Hu, Jiamian Wang, Pichao Wang et al.</sub> | IROS 2026<br>2026-08 | [⭐ 2](https://github.com/codingmlinprocess/LCS) | Vision-language models (VLMs) have recently emerged as a promising paradigm for end-to-end autonomous driving, enabling agents to map multimodal inputs and high-level navigation instructions directly to executable trajec… |
| [HEAT: Heterogeneous End-to-End Autonomous Driving via Trajectory-Guided World Models](https://arxiv.org/abs/2605.19631)<br><sub>Hoonhee Cho, Giwon Lee, Jae-Young Kang et al.</sub> | RA-L 2026<br>2026-05<br>📑 2 | [⭐ 0](https://github.com/heat2026/heat2026.github.io) | End-to-end autonomous driving has emerged as a compelling alternative to traditional modular pipelines by directly mapping raw sensor data to driving actions |
| [STAGE: STyle-controllable Action GEneration for personalized autonomous driving](https://arxiv.org/abs/2607.29517)<br><sub>Zihao Liu, Xing Liu, Yizhai Zhang et al.</sub> | RA-L<br>2026-07<br>📑 1 | [⭐ 5](https://github.com/CarlDegio/STAGE) | Driving style refers to the behavioral preferences that drivers maintain during driving, shaped by their diverse experiences, habits, and needs, and is typically reflected in varying levels of aggressiveness |
| [A Survey on End-to-End Autonomous Driving Training from the Perspectives of Data, Strategy, and Platform](https://arxiv.org/abs/2610.00926)<br><sub>Chengkai Xu, Yiming Cui, Jiaqi Liu et al.</sub> | arXiv<br>2026-10<br>📑 5 | [⭐ 110](https://github.com/Jiaaqiliu/Awesome-Training-Ecosystem-for-E2E-AD) | Autonomous driving is a cornerstone technology for the future of intelligent transportation, where end-to-end learning has emerged as a transformative paradigm that directly maps multimodal sensory inputs to driving acti… |

## 3DGS / NeRF Reconstruction & Sensor Sim

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DriveWeaver: Point-Conditioned Video Inpainting for Controllable Vehicle Insertion in Autonomous Driving Simulation](https://arxiv.org/abs/2606.31918)<br><sub>Junzhe Jiang, Zipei Ma, Zijie Pan et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 18](https://github.com/LogosIntelligenceLab/DriveWeaver) | A pivotal step in autonomous driving simulation involves inserting foreground vehicles with predefined trajectories into simulated scenes |
| [MCSplat: Multi-View Photometric and Geometric Consistent Feed-Forward Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2610.25345)<br><sub>Yifei Wang, Wei Tian, Wenhua Bao et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 12](https://github.com/yfwang0824/MCSplat) | Driving-scene reconstruction via feed-forward Gaussian splatting from sparse multi-view images remains challenging due to two factors |
| [Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796)<br><sub>Leshu Li, Jie Peng, Yang Zhao</sub> | ICRA<br>2026-06 | [⭐ 15](https://github.com/UMN-ZhaoLab/Pocket-SLAM) | 3D Gaussian Splatting (3DGS) has garnered significant attention in Simultaneous Localization and Mapping (SLAM) due to its advances in capturing fine-grained geometry features and synthesizing novel views |
| [NIDAR: NIR-Guided Intrinsic Decomposition for Scalable Scene-Agnostic LiDAR Intensity Reconstruction](https://arxiv.org/abs/2609.36878)<br><sub>Junjie Zhang, Jie Yin, Kefei Qian et al.</sub> | IROS 2026<br>2026-09 | [⭐ 25](https://github.com/Zjj587/NIDAR) | LiDAR return intensity provides complementary surface-response cues for robotic perception and state estimation, yet many simulation pipelines omit it or reproduce it using reconstruction methods that require real intens… |
| [MM-TRELLIS: Point-Cloud Guided Multi-Modal 3D Vehicle Generation in Autonomous Driving](https://arxiv.org/abs/2606.24301)<br><sub>Hongli Xiao, Youjian Zhang, Yucai Bai et al.</sub> | ICRA 2026<br>2026-06 | [⭐ 10](https://github.com/HongliXiao/MM-TRELLIS) | Recovering realistic 3D vehicle models from autonomous driving scenes is crucial for synthesizing training data and building simulation environment |

## Perception: BEV, Occupancy, 3D Detection, Mapping

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Deformable Gaussian Occupancy: Decoupling Rigid and Nonrigid Motion with Factorized Distillation](https://arxiv.org/abs/2605.28587)<br><sub>Yang Gao, Wuyang Li, Po-Chien Luan et al.</sub> | CVPR 2026<br>2026-05<br>📑 2 | [⭐ 25](https://github.com/vita-epfl/DeGO) | Understanding dynamic 3D environments is essential for safe autonomous driving, particularly when reasoning about human-centric, nonrigid agents |
| [DRS-VPT: Directly Relocalizing in a Scan with Vision Point Transformers](https://arxiv.org/abs/2609.12557)<br><sub>Lanke Frank Tarimo Fu, Maurice Fallon</sub> | ECCV 2026<br>2026-09 | [⭐ 18](https://github.com/ori-drs/drs-vpt) | We present DRS-VPT, a feed-forward transformer architecture for foundational image-to-scan registration |
| [Horizon3D: Sparse Radar-Camera Fusion for Long-Range 3D Perception in Autonomous Driving](https://arxiv.org/abs/2606.31096)<br><sub>Geonho Bang, Geunju Baek, Dongyoung Lee et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 26](https://github.com/geonhobang/Horizon3D) | Long-range 3D object detection is critical for safe autonomous driving at highway speeds, yet existing radar-camera fusion methods remain limited at extended ranges |
| [Explainability-Aware Frustum Attack: Exposing Structural Vulnerabilities in LiDAR-Based 3D Object Detectors](https://arxiv.org/abs/2606.29963)<br><sub>Chengzeng You, Binbin Xu, Soteris Demetriou</sub> | ECCV<br>2026-06 | [⭐ 2](https://github.com/SecMindLab/Saliency_LiDAR) | The structural vulnerabilities of point cloud-based 3D object detectors remain poorly understood |
| [PointLAM: Local Attentive Mamba for Efficient Point-based 3D Object Detection](https://arxiv.org/abs/2609.21780)<br><sub>Xuanming Shang, Weijia Zhang, Chao Ma</sub> | ECCV 2026<br>2026-09 | [⭐ 5](https://github.com/PointLAM/PointLAM) | 3D object detection from LiDAR point clouds faces a fundamental dilemma: voxel-based methods achieve efficiency at the cost of geometric quantization, while point-based methods preserve fidelity but suffer from prohibiti… |
| [PriorMaskMap: Robust Online Vectorized Map Construction with Biased Priors](https://arxiv.org/abs/2610.39283)<br><sub>Haoming Xu, Wei Li, Yu Hu</sub> | ECCV 2026<br>2026-10 | [⭐ 1](https://github.com/healenrens/PriorMaskMap) | Online vectorized map construction provides autonomous vehicles with essential, real-time semantic and geometric scene understanding |
| [Vernata: Self-Supervised Learning of LiDAR Point Representations](https://arxiv.org/abs/2608.06919)<br><sub>Oliver Lemke, Alexander Liniger, Abel Gawel et al.</sub> | IROS 2026<br>2026-08 | [⭐ 22](https://github.com/rai-opensource/vernata) | LiDAR serves as a primary sensing modality for robots operating in outdoor environments |
| [Towards Compact Autonomous Driving Perception with Balanced Learning and Multi-sensor Fusion](https://arxiv.org/abs/2606.02979)<br><sub>Oskar Natan, Jun Miura</sub> | arXiv<br>2026-06<br>📑 47 | [⭐ 9](https://github.com/oskarnatan/compact-perception) | We present a novel compact deep multi-task learning model to handle various autonomous driving perception tasks in one forward pass |

## Motion Prediction & Behavior Modeling

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [MolmoMotion: Forecasting Point Trajectories in 3D with Language Instruction](https://arxiv.org/abs/2606.18558)<br><sub>Jianing Zhang, Chenhao Zheng, Yajun Yang et al.</sub> | arXiv<br>2026-06<br>📑 19 | [⭐ 153](https://github.com/allenai/molmo-motion) | Motion forecasting is central to visual intelligence: agents must anticipate how objects will move in order to plan actions, reason about physical interactions, and synthesize realistic futures |
| [Flow-ERD: Agent-type Aware Flow Matching With Entropy-Regularized Distillation for Diverse Traffic Simulation](https://arxiv.org/abs/2607.06957)<br><sub>Seulbin Hwang, Kiyoung Om, Dae Jung Kim et al.</sub> | RA-L<br>2026-07 | [⭐ 0](https://github.com/seulbinHwang/flow-erd-project-page) | Realistic and diverse traffic simulation is essential to autonomous driving development |

## Datasets & Benchmarks

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [The Road Ahead in Autonomous Driving: The KITScenes Multimodal Dataset](https://arxiv.org/abs/2606.02956)<br><sub>Richard Schwarzkopf, Fabian Immel, Alexander Blumberg et al.</sub> | NeurIPS 2026<br>2026-06<br>📑 3 | [⭐ 30](https://github.com/KIT-MRT/kitscenes) | Existing autonomous driving datasets have enabled major progress, but fall short in sensor fidelity, map completeness, or geographic diversity |

## Safety, Robustness & Evaluation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [CCFM: Collision-Constrained Flow Matching for Safety-Critical Scenario Generation](https://arxiv.org/abs/2607.04451)<br><sub>Ke Li, Kaidi Liang, Yuxin Ding et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 3](https://github.com/KELISBU/CCFM) | Evaluation of autonomous vehicle (AV) planners in safety-critical closed-loop simulation is essential for real-world deployment |
| [Lipschitz Optimization for Formal Verification of Homographies](https://arxiv.org/abs/2605.23203)<br><sub>Jean-Guillaume Durand, Panagiotis Kouvaros, Maxime Gariel et al.</sub> | CVPR 2026<br>2026-05 | [⭐ 3](https://github.com/jeangud/homography-verification) | The adoption of vision neural networks in regulated industries requires formal robustness guarantees, especially in safety-critical domains such as healthcare, autonomous vehicles, and aerospace |
| [CADET: A Modular Platform for Evaluating Distributed Cooperative Autonomy in Connected Autonomous Vehicles](https://arxiv.org/abs/2606.04072)<br><sub>Pragya Sharma, Brian Wang, Mani Srivastava</sub> | ICRA 2026<br>2026-06<br>📑 1 | [⭐ 0](https://github.com/nesl/cadet) | Deep learning models are increasingly central to autonomous vehicle (AV) pipelines, yet their integration has traditionally followed a monolithic design where perception, planning, and control execute on a single onboard… |

## 🏢 Industry Tracker

Latest 14 days of news, official blog posts and new open-source repos from tracked companies. Full daily feed in [`daily/`](daily/).

<details><summary><b>Waymo</b> (173)</summary>

- 📝 2026-11-05 [How the Waymo Driver Manages Severe Winter Weather](https://waymo.com/blog/2026/11/winter-weather-preparedness) <sub>official blog</sub>
- 📝 2026-11-05 [Rethinking What Freedom of Movement Feels Like for Women](https://waymo.com/blog/2026/11/because-women) <sub>official blog</sub>
- 📰 2026-11-16 [Ivy City rally targets Waymo charging site after DC robotaxi bill stalls](https://news.google.com/rss/articles/CBMixgJBVV95cUxPdDZGSi1wUEdvazZlVkVYMlhqWjZNei1Kcl9PVS1XbU1lMjlBakg3UmQ0dVhEdWxoeXZtT1NLcXBKWDBVLXROQUZuSGVpeWFVejBKQ0RSbUE0RndUY19yM002ZzVQSGl6TjNOSldhRmxqZUFUQTVKNWlvRHNwbmFvVy1yeVVZd0ZpMzdNMkRsNTJreF93d0ZPN1pITUpSWjV2NTJGdVJ1eUZFYlNGZVc0cmpxSElIMzRreXFVS2hCZEhzXzd3SXhnTENQbmJidTVnM3ZVajNqYzRnMXFQZ2JqZkJfOUF6TXBYVWVGUV9XTnpoZTJjSXNCVS1MN3MydkJmcU1wSTBuNzFoTjk1el96cHhMVjNCcjJkLUwzNW9GXzZjdGppT2dGTWtDbzBoQkktS185UUFIZ21oQVFjM1BWbENCTEdwQQ?oc=5) <sub>WJLA</sub>
- 📰 2026-11-16 [Robotaxis Need “20M AVs” for 3-4% of Global Rides, Says Jason Calacanis. Good News for Uber](https://news.google.com/rss/articles/CBMiswFBVV95cUxPN1h5b21wMkFsel9ZUnpGMzM5dDZuYzZ2b2hkUlZJV1pjaGNhSGlJNlZKY2FsZDJZVXdTSkFRbGdJdm1ySzVJcmx3dFZURktMa29GQTN0b24zYS1ZWGJpc1lyblFjblIxQnFQX0xSZVlrU1hUZzh1am05cjlvRnpnX2RqMXFIX29QXzNneGxRNlNyWVZMZmpPMWFWcUNVN01sX3BfZVVTWVR4U0J0MzFNUFVLRQ?oc=5) <sub>TIKR.com</sub>
- 📰 2026-11-16 [What's it like to take a self-driving taxi? Pól Ó Conghaile hailed a Waymo and captured his trip on video](https://news.google.com/rss/articles/CBMi9wFBVV95cUxOWHBtWmY0SjhGRm5ZMENPQldOUmtpSU92VVhOazBiMEFZU1FyX2RWaGxZZE81R0R3dDNqb0VaX0JlTkZPMzBVZFNiLW96T1lTQTlibFFZSzhvRV9QYnEwTEtsaDlxWlRrRzhWdGRkV3dlQWRCN0VxSVdCYUduaC1xVGw0OVJEendabVJZVmU0S1dxazNDQnpmc3VhM050NmwzajhNVVhlU0k3dzNUcHdRMUMyZ0J4bzduM1JLanpQUjVfZ1hiNVU4ZUdPVUpERVdUbU05NlUxMEN3YzR3Und2ZVpRa3lxYUsteW1kdkMyS3dGYmZEdmdZ?oc=5) <sub>Irish Independent</sub>

</details>

<details><summary><b>Tesla</b> (240)</summary>

- 📰 2026-11-16 [Elon Musk Admits Tesla Cybercab's $300 Monthly Fee Is Too High — MKBHD Says His Headshave Bet Isn't Over](https://news.google.com/rss/articles/CBMikwJBVV95cUxQbWVlRW43RTR4cDBaMEp0MEVwYlFNM2ZlUVlKcTd4YkVfeDJYeHpKY3pOU1dhcEdadVBUWHd2U1lfMFMyemhyTXVlVzdiNkdTSXM4ejdDZ3oyS19sdXlnQkJ5LS1YYlVBYlJ1d0ZGMkFwOU5tWkxCazNwMzJUSk9IU2MyMWJLMUhzTEpLSTc2bThOOTdGbXEwVGFYOTQxSktKSnpabks2SFpzRURKbHBoa1l4cGlwTkUtVE05blcxTGN4U3lOQ0F0UEd0S182QXVqVDczOTRTNFNfdVdHNnJ3UF9KWVVIRjhHQXQ1akhrUjJpQmZacWVVWUNQYy1sZ1lKM0hZMW01MUtaeWJHZXV3VTZvTQ?oc=5) <sub>Benzinga</sub>
- 📰 2026-11-16 [Tesla removes its most affordable Model Y AWD from lineup](https://news.google.com/rss/articles/CBMipAFBVV95cUxPQWFYMUpZdHNYZndpejVMd014OGhaOWE2a1JVY0xyMmIyTS1Fa2w0MExKNjdkbUg5Y1pleGlaVnd1MkJwOHhHNVRETlg0cUFpTG00ZTl2SmxoV3VqM2dRWFUzN1RsNi1mQjB3c3kxa0xrVmxpZkJKV2M0VUJoVmZORXA1Q0o3YTZvX0NjNlEwQVc1QTVYdkpwVDBjVDN1ZzhDeEMtSA?oc=5) <sub>Notebookcheck</sub>
- 📰 2026-11-16 [特斯拉FSD准入引讨论！文远知行L4 Robotaxi已在国内多城落地运营](https://news.google.com/rss/articles/CBMijAFBVV95cUxQNGktZ0FBclhpVzNJbkZDUktLZEJ1Q095MHNzUDNCelV5SjVEWklfaVQwMXJYcGRvbGJmOW5jV0E4LURqYVA1c2FjQWplTnFkRTVsUHA0elBJam5UNHZWekFGWk94c1BVRkd0VVlmeVJnWXVlY05GZ2lsd0lBcUNSdE5UMmVXekRWajFNRw?oc=5) <sub>Sohu</sub>
- 📰 2026-11-15 [Tesla opens $29,990 Cybercab orders, but owners face $299 monthly fee to drive](https://news.google.com/rss/articles/CBMivAFBVV95cUxOZVpSNmZncVVBVUlQR1JpNjNuby1vUG9pQXRLakNjYjFjR20xaXRuQlUxZ3BLcGxEVV9XcmZtU3FsMnlqc0djZG14UExxalZGWUhDd2p4TjNqV3BqeDVlU0VZY2taV25LRUg5d1R6N0dUX2JHT2I1LTZpTm80ZWk1dmRPSXZTOXN1SDRkMl9XSG42bENHWUlZLVluaE1XVkFORHhQZmZ0V0JCOXdWb1dLSUJFclhCN2NuUXlDbw?oc=5) <sub>Notebookcheck</sub>
- 📰 2026-11-15 [Tesla makes major Cybercab announcement as driverless vehicle goes on sale](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQeWRiUWowYWVmQW9OdUFReWE4cDdfWDlZSUVJNURfUEp3UTJncjFBQVVwOVhxcVB1dmpfSkJNYVhmQ2lUM01YNHUwTzRDX2VNdHdWenNkSjN1RTFpM1ByeG1XeElsdDN6Yl8xSnlsZnlqUUtDY0VyVU90c1Rxb3JZdmM3M0czSVRTUmI5V2pVRlRVQ0VYMi0zckIycFM3eWtEcEhnTXpEa29iUlHSAbABQVVfeXFMUHp6UmxGSl9iLUxTY3hhSmRUYkNZcHkzck16VVprb3pqVE9nUnRrdDJKNWxpYUZybFNrMkt2WFFZejdJdkxBMDJESFR0N01rRTJoVGxVa21uWm1zbFk4aXFaT093SVRVQlFuaWU3aDh3MGkxeERGcmJCbzFkeTc4dnRORmFyU010cjR0Y0I3bW5RU2hweUlmQU1xVFFiZzlfN2Z0SEJubUhxR1BOel85X0U?oc=5) <sub>Fox Business</sub>

</details>

<details><summary><b>NVIDIA</b> (156)</summary>

- 💻 2026-11-02 [NVIDIA/nvperf-core — Core NVIDIA Nsight Perf SDK APIs and libraries for collecting and analyzing GPU performance data directly from application code.](https://github.com/NVIDIA/nvperf-core) <sub>GitHub</sub>
- 📰 2026-11-16 [Morning Bid: AI selloff resumes as Nvidia earnings loom](https://news.google.com/rss/articles/CBMimgFBVV95cUxPeWdHZ012dm1zRlNNbk16YWNnRngxVnJCUVJvQVZwX204ckZhcEN6Q0wyRHJHell1MUpTWTVjSUwwUzYwUmFWMm1FNFRjQnFSY1hkckpPdE1NSEFxR2RCM2F2djhTNTVfNG5VNUNqX3FvQVVXVHVNTjBZa1czTjNnek5WdldSbXU0NzRfTkJLVnVHNGpVZ0dYc0NR?oc=5) <sub>93.3 The Drive</sub>
- 📰 2026-11-16 [China's self-driving industry readies Plan B without Nvidia](https://news.google.com/rss/articles/CBMipwFBVV95cUxNVWtyMGFOTUc0cnUzaXptNlVTc1lEODRoNU1UZi1TbUMyNWRMYjdJaTF4eWh0WWp2dGlGQ0wzUU9VQVZsQzBaRGx2UThKSXpOTUVld0h4RlRQcW1qMHR1Ml9nUXF5V2dtR1ZxWFZuUnZOaGZ5dzV1VjBiX0dGOUE3Sko1ZnAxUHF2Mko0UkVaRk1QTVd5TDRhN2NacWcweXZ6RWNjMXJkVQ?oc=5) <sub>디지털투데이</sub>
- 📰 2026-11-16 [Denny's Removes Then Reinstates NVIDIA Founding Plaque](https://news.google.com/rss/articles/CBMiiAFBVV95cUxOZ2hVbTlyMTN3M2REMDNZNXZSaFZUU1QtcVRJRnpLZWtWWExRUEZZRXdPeHJueDdRcC1kVWtDalMwWER2c2VNd2I3Z1Qxc1E1bmVDZG9kZmZOSk9RalBrTmtBZlZOSHh6aDVSSWFwR0tJVDJ6T3gwOFZoQ29lcHZ2THdSc0p6Rzdm?oc=5) <sub>조선일보</sub>
- 📰 2026-11-16 [Lutnick faces scrutiny over Nvidia spy scandal](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1sV3Z6UVk0V2lJS29CZUR4NzFCMkc3cmJiTUc3eDFyd1RaNmtMd1dRUkZpNW9WMjFYbkNNczRhQ09jQTFTVWR4Z3RaMlRfM0F2TWlibHBieDktZw?oc=5) <sub>CBC</sub>

</details>

<details><summary><b>Wayve</b> (42)</summary>

- 📰 2026-11-15 [Autonomous & Self-Driving Vehicle News: Rivian, CoreWeave, Wayve, Kakao, Nvidia, Kia, ASI, TIER IV, MAN Truck & Bus, Komatsu, May Mobility, Volkswagen, Tesla, Terawatt & Waymo \| auto connected car news](https://news.google.com/rss/articles/CBMiogJBVV95cUxPMkxJVEkxdjYzbWJ0LVRPYlNBVElOczdQOXRITVpsWEpzVF9RYm0xT1ZOeURGRFdYTFJ0bDJDTnNkUFNBSUFpcHFFSV9IVkl0NjhoZUNRT21qV2JoM2FmZmg1NmdOMXEweWJOekJqbTZvS085NXlhU01XZ3U1TUxFQVdvdXRPM3RvWGUxWUg0TzYyWW1FbnQ1OTBYaUltNU1QbkwxODdxeGt6OHZrUVZaQldlQVd1dEZSdHlFeVJkVWphQzZEaVBxRGR4Q29Gd2VVbThuWldLRlRzZTRYOVhuelh4YmpoTEM2Nmc2OW1jb0l0MU5ZWTlfdzJIUWY5dkh3UG9JcUJfaF9nNUQwTVhUbWhXRXU4VGpOTlRCMlBfbEpsQQ?oc=5) <sub>AUTO Connected Car News</sub>
- 📰 2026-11-15 [CoreWeave partners with Wayve to accelerate AI training for autonomous vehicles](https://news.google.com/rss/articles/CBMi0gFBVV95cUxNMzN1Qk5zalMzYno3SC14ZmQxQmRVTEpwVU1JR2NTWUItbTVhTXQtelAxREJCTExNZTVPLWJkN0xpZ19yeHZpLTAzdFN0SlZJRkJudll4ZGt2YnNLVUtVcjJIcmhjY0QyR29HcHFhRTdWM2tCYVZCYTFINmRlMmc5SmtvTWlkaHpkZlNtU3ZSY1RKREpydHk2cUoyNkxkQlJmRHZiSXNRdU1Ud3Q2S2YyU3FpaHhHMjQ1T05FWk1fbC1wRFFNWWozLWhlcEJrX2NEZmc?oc=5) <sub>Robotics & Automation News</sub>
- 📰 2026-11-15 [Savings app Chip targets retail investors in private market first](https://news.google.com/rss/articles/CBMiowFBVV95cUxNbDNCcGlYLWlpM2l3VmVnT0ZNMHpIUjFLalFsNmpTZGgzVlU2TkxtbUN4aDZTRm55aWZrZmRkV1dyZHloU01yMlVEcW55MG9RUzFNZFdSQ0JqMnZ3cjZRcHdfSDQ4RHdPV05OYmg3NzBvWXZSRW5icElfSmdLRzlzSlAxOVgzekM2ekgtVU40R3VfQWNURkdVUTBuVjNxc2VhRUtn?oc=5) <sub>Sky News</sub>
- 📰 2026-11-13 [The Verdict Is In And The Brits Lead The World In Detesting Self Driving Cars](https://news.google.com/rss/articles/CBMibkFVX3lxTFBJZWtXTkdEQVRoMVVIZUhjbWZkQXJla04zZ2dteGxMQlp6LW9CSGpIbjNJSFhXdVN4VkxIVnZvdGNMeTNoTlNrRUdjeVcyU2RXUmJOZThLOUtNQmpfNmNZeHJRYzJ3LTg0bXJiX1NR?oc=5) <sub>AutoSpies.com</sub>
- 📰 2026-11-13 [Nvidia’s Interim CEO Inherits Robotaxi Bet Jensen Huang Built](https://news.google.com/rss/articles/CBMingFBVV95cUxNMTZobWtOZjZDc1duRG85T2tIVE05NTZ3cXZaQnE0Y1Z1UUJETGJONDJGX19mZ00zUGJkXzVZdmJGRV9VeC1kUjQ0QmxOcHotbFdWNmQ4SkM5WXlOLVhYWDNSTURaX0lVM0RlS1ZTTnJjYVBVWEJJLUZNZGd0NkFVazRxU2dTSmF3aDlnem1iYUlWNkQxQXlDZkRTbUNxUQ?oc=5) <sub>Electric Vehicles</sub>

</details>

<details><summary><b>Momenta</b> (89)</summary>

- 📰 2026-11-16 [How Intelligence Is Reshaping the Automotive Value Chain](https://news.google.com/rss/articles/CBMiugFBVV95cUxNZHd6ekhyLXF1V2Nwc1hvQzRoR0tmdmZJRkl5cXhBeGEyaEg0cWFma2xET2hvMnhtMC1hZkFTandDYXZfaGxSNDBSZnZrOU5Pd3Y5OXdEeWN3dnpncWd4X1J2Rm9OdDM0YnVTVVdubE9kQVdVcER5TUpfMmlLRmdSM0t5QjVPeUxtYUpiSDlCalNKR1AybTNacnBDd2ptMWoyd3RrOF9ITWRSenpxb2plUmdOY2hZUTlCMEE?oc=5) <sub>Gasgoo</sub>
- 📰 2026-11-16 [东风日产NX7搭载Momenta R7模型，预售12.99万起](https://news.google.com/rss/articles/CBMic0FVX3lxTFBYWVJncnJQWDRHbHQtZUs5eU1iRjVibl9aMklWbk9GbkxnN0xqMDhhWmp6cnI1MWZ4UXEtV0RJSHoySk5FTENHUFpZOGJTRVk5MXRVeUVzdTBwWVk2OGItZHVtc1hrYkFEQVFMU0dtOWlmRXc?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-16 [宝马新3系申报，2.0T双版本+Momenta智驾](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1OWkF2ZklWR0NZUTh2b2FhRzVoeXNUQXYxa0tVU2JCVmJVQXNkQVk4TU5vMHRELTNLVlA3QlVSdkI3VkNqazUwVEliemNJQmRVaWNYXzQzR2hjb1E?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-16 [新世代平台 + Momenta 智驾，宝马 i3 广州车展首发](https://news.google.com/rss/articles/CBMia0FVX3lxTE1aODg2TmNKQlJKRHdYRnhoRHBUR0hTYTczSE1SYnBtMnpUN1QtdFFCWDNzQm1zUkFhOC1pOUw2UUU2dnkzNzZmYkFlX181MFBMTlR2NURuNDNKOG1sRElidzBiQlVkVWo5UGp3?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-16 [郑钦文点赞Momenta智驾 奥迪E7X将升级搭载R7世界模型](https://news.google.com/rss/articles/CBMic0FVX3lxTE1JTDBXU2RzVmEtSnhLSlRrYkRqQXJYOFJCNmpTLUdkbzZtcS10OGZCczRwOXdZZm82aU1QZ3U2T1ZDU0lhRnB4VjFNd1NOSUNnSXkzTm5BQkMyQWludHN6RENqdjFaVG9RTTFYZVFfUmJTT0k?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>XPeng</b> (154)</summary>

- 📰 2026-11-16 [Pony AI and Toyota launch bZ4X robotaxi service in Guangzhou](https://news.google.com/rss/articles/CBMie0FVX3lxTE9vVWhYZHMweHlIV2c5SnR0RjluOFVqSFM4eFJIR0M0Tmlqb1MzelZ4QWV6cTRUY041ZUhUUlN1djFGZUhybVpwNG1venZCanBHTVVZdmJZWW14RXNfNkdRUUpMSEI5R3RzR2ZMd2hOa1d0U3JDTFFQb3FCaw?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-16 [South Korean automakers join forces to counter foreign robotaxis](https://news.google.com/rss/articles/CBMiV0FVX3lxTFAtWWlTc190V21DLUJVVXdZSlVLNC1PRWkySmFKemhXTHNMTUpySmVOZVZHSHV5U3A0Ui10YTdqNDRQbkkwNjBtNm9GSWtWLWxORTkyU0YtUQ?oc=5) <sub>매일경제</sub>
- 📰 2026-11-16 [XPENG launches G9L, MONA L03 in UK, outlines next phase of market development](https://news.google.com/rss/articles/CBMi0AFBVV95cUxPRlZrM05HN2JZRmoyQ1J3UlpMR1ZsLWY4SEdjZ2Z5emhXS1l5ejdBODQ0X0x4OU90Y2h3Y2I2M09DeFZCQTktTC1Gblo0c0VNWHhQbEFQN0hKNy1sbW53Z0swTHY3WG9mWm1vVk02SWpwdjV1X1FoNm5YRUZCRzBCLUZ2TlB4eHRWU2lkUnkyeEVCcUlZU3BPc3JxZGRDanJLMTRCbWdRSlg3R0lIRnJBMjIxUGRTTkZwUVgwSEFRMUJJRWJHb1BpeF9jR1J5MVdT?oc=5) <sub>Gasgoo</sub>
- 📰 2026-11-16 [小鹏P7i 2026年还值得买吗？3个维度说清+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE8xb3F3bHRiTHdpeXh2TG1NQ3J3WDBiSjJvQVFNMHJLOUFCN0hkTzlCLXZqbDVtN2w2WkNFbmNBX2ZzazlJeE1PejNEcnd6dHFFTXJOaW85SWpTR0wyUlFSUWtIUmtJdkpvMGxfZ3ljQ1IzUQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-16 [小鹏加速英国市场布局：MONA L03、G9L双车上市，未来一年将再推5 款右舵车型](https://news.google.com/rss/articles/CBMiUEFVX3lxTE9KeEdEcEdTaFhvX0NQZ0x0dXg5WUFVMkVmYVZlZUZVdDRFc2JYblMtMmlOWjFfN3BGczlMdmQ4VlNTVFY4LVdDUHVYRnRVX3Vm?oc=5) <sub>盖世汽车</sub>

</details>

<details><summary><b>Li Auto</b> (156)</summary>

- 📰 2026-11-15 [小鹏G9L对比智界R7、理想L6、极氪7X：智能大五座SUV横评推荐](https://news.google.com/rss/articles/CBMickFVX3lxTE1nTW1JYlZVdGIwYVVHc1FNQW5JbmEzNTJ0eU9xYl8xenpZODdLdUdZSGFBemZjMUdYSG9PYzlxWmYtdzF3YmV5aGpMVUpSX25ZajFIaDIxSmZEcmN1SVZ0MEk2UDJYZ1hMU080a2ZxT1VVZw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-15 [理想MEGA 2026款值得买吗？50.98万配5C超充+后轮转向，3个维度说清+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9jbVExR0RFOVZBcTJ2MlZ5RjY2dDBFMS1YSW9DLU5jT2ZHZVpUekpZcXBDTDhUQUwzbHQzRFlUdy1oWklfYUFPUWpyeXVaM3ppWTNTb1NxSWY2aTY4Qjdr?oc=5) <sub>新浪网</sub>
- 📰 2026-11-15 [Nio opens northernmost swap station in China, touting 3-minute swaps in extreme cold](https://news.google.com/rss/articles/CBMihwFBVV95cUxQaFIzeTlpQzVKTkJ6eGE1WTZYOVN5MnhVR0ZtQi1ZaXo4cl9WS0w0X0dFM25sWHlTT0JqRWFiRFhpVS02UmwzZXdIVVBRYmcwQkpPdlFpSld4cnBHS25YZXYxaFlnMFFIRzhJcGFXdmR0NE50d3BWWEhzOGItM0xoWFVkRmQ3cXc?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-15 [4款家庭增程SUV自驾游横评：续航补能、三排舒适、智驾露营，奕境X9表现如何](https://news.google.com/rss/articles/CBMickFVX3lxTE5PTjBYSG1BY2tHbmFMTTl1a3Y0WEJyR3RSX2JaLXBEeE9EQlkxa2ZrVzYtd3VmSDNRZTJaWlpSV04zdTNVZzRQUFF1TGJHTVY4OVc0NDlmMFRGelpGTEcxNGl4NElTVy13VFNqVVRFdUxrQQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-15 [OTA8.7理想VLA2.0智驾高效模式是什么段位？ #理想i6##辅助驾驶##智能驾驶##理想汽车[超话]# ​](https://news.google.com/rss/articles/CBMigAFBVV95cUxOdl9QUWlIOFdfdG1wbHE5SWlsLVVhSGZ0X2JQLWZtazhnN25RQTAtRTVFNnkydnFua1p2UGlucDBpZkJaLVd1LTVvSTR1VHlnN0t1WVN2UDN5VG01eVljSGFYZVVNVEY4bHU0V0Nwc0o5azVlVFR3Rlg4bFZEaWF5aw?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>NIO</b> (121)</summary>

- 📰 2026-11-16 [Pony AI and Toyota launch bZ4X robotaxi service in Guangzhou](https://news.google.com/rss/articles/CBMie0FVX3lxTE9vVWhYZHMweHlIV2c5SnR0RjluOFVqSFM4eFJIR0M0Tmlqb1MzelZ4QWV6cTRUY041ZUhUUlN1djFGZUhybVpwNG1venZCanBHTVVZdmJZWW14RXNfNkdRUUpMSEI5R3RzR2ZMd2hOa1d0U3JDTFFQb3FCaw?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-16 [Geely Galaxy previews new M8 5-seat hybrid SUV to expand lineup](https://news.google.com/rss/articles/CBMifEFVX3lxTFAtSHMxSGZMdFFSamtrSGVFNDNyU1RieTR2MnFFNG9oU19JWmwwV2Z1QjRQeEJnTlMtQVA1dk9GUXFiWUE0eEZBdE1ONGNsdnNzWnNpdXg4ckNzQlFSLW1FbTRFdlVQcTI2d0VDQVRjUjFmOXRvZE95YkdOTlU?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-16 [BYD to launch third-gen Tang 5-seat electric SUV on November 24 with up to 850 km range](https://news.google.com/rss/articles/CBMidEFVX3lxTE1RcWpFQndaV0lvcDNmS1ZqVGV5WDdHSWZyQjJmVkU2aThpTE5QbERIZFNleFhGWUNYNURBdEVMc2dDYThJYm1wY05kUW1CRTVaRjdIVDlqREJ5dl9LQmhJOXNNcDNEdXRQcGZpUm9adkp6dER3?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-15 [【视频】买下！24年蔚来ec6 外南极星蓝内丹霞红75kw买断](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5kMndaZEZPdVhHRnRsdkpMZ0NWaVl3ZEIxUy1TYWwwcEVwcG1GVzd3cVdLWXIyTVlvbWhvY0x1WFhGZ0lNR0ZEOWFhRlhxckZoeUl0dnVmWkNTRWs?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-15 [二手报价12.98万，蔚来ES6，行驶9.7万公里，0次过户](https://news.google.com/rss/articles/CBMia0FVX3lxTE5qQTVwc1NfQnJMemdfcmVucGpzV05rNm1COXZvSkJZLVRxTnF5enBMZndvN1lMZnh4dERtcDJ3WXhKbUpocmtPMEMtM0NKZEVkSDBxLTd5T09qZzU5VmZ3dW5XM3pxTjVzWDM4?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Huawei</b> (251)</summary>

- 📰 2026-11-16 [Pony AI and Toyota launch bZ4X robotaxi service in Guangzhou](https://news.google.com/rss/articles/CBMie0FVX3lxTE9vVWhYZHMweHlIV2c5SnR0RjluOFVqSFM4eFJIR0M0Tmlqb1MzelZ4QWV6cTRUY041ZUhUUlN1djFGZUhybVpwNG1venZCanBHTVVZdmJZWW14RXNfNkdRUUpMSEI5R3RzR2ZMd2hOa1d0U3JDTFFQb3FCaw?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-16 [Huawei Cloud Releases CloudRobo-WM1.2 Embodied World Action Model, Says It Will Be Open Source](https://news.google.com/rss/articles/CBMingFBVV95cUxOaUt5WmJBOEVCcHJtZEduMEdrdzU3b0d6YW1vamFHSVhFMnI1V24ycFROOFJubkFzTXpoZUxid0VhNGxtWGZMTE43MWhwUlJMSXBBUmhXajJsc1lKY2hJd3Y0aU5fYld3eTFCM0lwQmFNUjJvbWhVUFhYaUpPMGpkQmNILXRkNkNRcjNFTHd2cmtnbTlNX1pBQ2NlUjBYUQ?oc=5) <sub>Pandaily</sub>
- 📰 2026-11-16 [BYD to launch third-gen Tang 5-seat electric SUV on November 24 with up to 850 km range](https://news.google.com/rss/articles/CBMidEFVX3lxTE1RcWpFQndaV0lvcDNmS1ZqVGV5WDdHSWZyQjJmVkU2aThpTE5QbERIZFNleFhGWUNYNURBdEVMc2dDYThJYm1wY05kUW1CRTVaRjdIVDlqREJ5dl9LQmhJOXNNcDNEdXRQcGZpUm9adkp6dER3?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-16 [Geely Galaxy previews new M8 5-seat hybrid SUV to expand lineup](https://news.google.com/rss/articles/CBMifEFVX3lxTFAtSHMxSGZMdFFSamtrSGVFNDNyU1RieTR2MnFFNG9oU19JWmwwV2Z1QjRQeEJnTlMtQVA1dk9GUXFiWUE0eEZBdE1ONGNsdnNzWnNpdXg4ckNzQlFSLW1FbTRFdlVQcTI2d0VDQVRjUjFmOXRvZE95YkdOTlU?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-16 [Will The GAC Aion Ray 7 Come To Malaysia?: 702KM CLTC Range, Huawei DriveONE Power, Brake-by-Wire Tech](https://news.google.com/rss/articles/CBMitwFBVV95cUxOa21KNjN3MU0xWXBuTTc0WE52MFJ2LXVSdVFaMEZKX2RsbWRnTXJJb25qSDhRaVBIRG1MRVlwaFpjOW95TTZhTVpUaUQ3dTJNUWhXS01RSVVQY3lxZk95ZmtfWjROc2JzZFR3OEM0X0lpUEtRZXpUQU5QS2g1Wm5paU1vZk5vYWhkZnBxZjhUN0RGMEgwSHpMalNKYjF1ZnVYNk9JM1RkT3BlRDcxTjlhb0pyeDdqMjg?oc=5) <sub>Newswav</sub>

</details>

<details><summary><b>Baidu Apollo</b> (43)</summary>

- 📰 2026-11-16 [Shenzhen Driverless Taxis: 188 km² Baidu License](https://news.google.com/rss/articles/CBMilAFBVV95cUxPNTVZMFVJOVAxMFJiVFpNMWtVRURVSEtrRVd4cjdmNlVaYUhIRHYtNnNaYXI5Y2RsOXBDdndGd3NnYU5QY0kwaG02MEI1QTUtY3BvazRTaGRaaTVjOHZhbm5SVmVZanpsalc3eERjUE1xcS1MWnIzMG8xSW9qTHVVMjBGM2ZlcFI5aFY0eWFTeDdCTTV3?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-16 [South Korean automakers join forces to counter foreign robotaxis](https://news.google.com/rss/articles/CBMiV0FVX3lxTFAtWWlTc190V21DLUJVVXdZSlVLNC1PRWkySmFKemhXTHNMTUpySmVOZVZHSHV5U3A0Ui10YTdqNDRQbkkwNjBtNm9GSWtWLWxORTkyU0YtUQ?oc=5) <sub>매일경제</sub>
- 📰 2026-11-15 [Asia week ahead: Japan's third-quarter GDP and China's October activity data open a week shadowed by Nvidia and Iran](https://news.google.com/rss/articles/CBMizwFBVV95cUxNaUIydGxUTm01MWJwNXlSS2pyN3psVmVoemRpYndLT0dUa0RtSl91elpWOTBaS0VoWlR2WnhHeDZwNDdWU3ljYzM5Q2k5YmhFNVFKMG9pbmFJNDZoMDgzMnE0eUpPMlFUWk9kQnNoQmk4TDcwaU9RX0g5YXhqWUdMT1RzbWM5TFQ4cEtXTWxZVl9qcFY0VWNnRnpTanhkdERCNXJzb1ZvajhzRmJyMUdmck9BUFhlRnVtMlIzQ0ZadVg4NEFNd0lzUElKTWlVcnM?oc=5) <sub>MLQ.ai</sub>
- 📰 2026-11-15 [U.S. and China Step Up Robotaxi Push ... ‘Team Korea’ Fights Back](https://news.google.com/rss/articles/CBMiU0FVX3lxTE9WVmdneGp4aU81UlJhWmJwUW4zNjBKc1V0Qzh2ZHRhNFlGeHVFRnBtMjlpcmpoSzF5Y2hGSWp5SlVtMEkyT1hwM0F4NG1VVWFHdlFr?oc=5) <sub>매일경제</sub>
- 📰 2026-11-15 [Baidu (BIDU) Earnings Preview: Profits Seen Falling 46% Despite AI Cloud Boom](https://news.google.com/rss/articles/CBMipgFBVV95cUxPbmlLcjUxRUVBQjBKMnI1V0FwMkt3LVhPUnBlcENRWGJOY3RhSTBmOXkzNGZaNEROTUJKZHBWS21sTTNwLV9KRXJJNF9YS0tfaUJ3RmxZSlJPVU5uOUtWS2tWYWgtS0FOWmxObnpGalc0Um1Da1NSTU5BV0M1YTlZdFRYV2pDdFRuZU9pRHI0MHktbWp2NDYtTnB0NGp0X3BISF9DMGdn?oc=5) <sub>TipRanks</sub>

</details>

<details><summary><b>Pony.ai</b> (77)</summary>

- 📰 2026-11-16 [Pony.ai Adds Toyota bZ4X to Guangzhou Driverless Service](https://news.google.com/rss/articles/CBMinwFBVV95cUxQMHdSdGl1Nl94YnBlMlZudU1sVWhLOERqS2hGdGZqZ1N5WDN0TGJUT0RvRWdLYlNQQ281VWp3QlViN2hmZGRTLXQ3YjAwV3h2RjhLX1ZEc3FEUjM1OHh6TkRjVXVqNF9fWUY4WUhjZXlRU0ZkaXdrY3dHMVFZczNwbnpFYl9vZWRoMUxyd0dCU3QyZUR2ZzI4ZWd0aEtQQkU?oc=5) <sub>The Defiant</sub>
- 📰 2026-11-16 [Pony.ai, Toyota roll out fully driverless robotaxis in Guangzhou](https://news.google.com/rss/articles/CBMixAFBVV95cUxOY1FLd2JhdjJIbDlDNnIzeXozRlBwX0xkRHpCNUJqZHg1a1piU1NLYU5YX0plc01oRC1Nd0dQcW1XSmRwSkpmUVRHQ001aGsyOFg3VVN2VmxUMnBtTV9INUIwZW8ybHJCV0dQbkFXdEI2eVdLOVNnRGl0VHNFbTR1aXpneVVtNTJHclp4WU15WkhXT01IWXBYZWw3UTctdmNxelpYSmg2VTNBTkNDTzk2RWFrYl9zY3E0NU9pcml5NlJfRHRy?oc=5) <sub>TradingView</sub>
- 📰 2026-11-16 [Pony.ai, Toyota launch public L4 service with Gen-7 bZ4X Robotaxi in Guangzhou](https://news.google.com/rss/articles/CBMibkFVX3lxTFBsVEo1QllwMnJVRjlpbTM4a3NjQ0hqa0VmY0VtTDB3WWE5LUozNGJRck1uVmJtZmdrb2UwcHlvUVN2LW9oMlhFZ2VVcXVTenBoNXhiWDNpLTdpM1Zmb1d1M2dEd3JKRDd5R0k4V0Z3?oc=5) <sub>Gasgoo</sub>
- 📰 2026-11-16 [Pony AI and Toyota launch bZ4X robotaxi service in Guangzhou](https://news.google.com/rss/articles/CBMie0FVX3lxTE9vVWhYZHMweHlIV2c5SnR0RjluOFVqSFM4eFJIR0M0Tmlqb1MzelZ4QWV6cTRUY041ZUhUUlN1djFGZUhybVpwNG1venZCanBHTVVZdmJZWW14RXNfNkdRUUpMSEI5R3RzR2ZMd2hOa1d0U3JDTFFQb3FCaw?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-16 [Pony.ai and Toyota Begin Driverless bZ4X Service in Guangzhou](https://news.google.com/rss/articles/CBMikgFBVV95cUxOOFRqSlFEVlN2VGxTYUpfN2VTejNCOWVFNno2WmFuczdWYWZxNEZnRkcwLUpFNXEzNS1qZjR1bkE5cklYNUctaTFWbnhPVHRYQm4tQmljUW9xeDZZbFczNTU4bmNyQXVaeWNSYUNOUEVhS0lOT3RCc0hJVTVCOWw4bTJBUHkzM1dYUWdobldQcjdadw?oc=5) <sub>Securities.io</sub>

</details>

<details><summary><b>WeRide</b> (103)</summary>

- 📰 2026-11-16 [Will The GAC Aion Ray 7 Come To Malaysia?: 702KM CLTC Range, Huawei DriveONE Power, Brake-by-Wire Tech](https://news.google.com/rss/articles/CBMitwFBVV95cUxOa21KNjN3MU0xWXBuTTc0WE52MFJ2LXVSdVFaMEZKX2RsbWRnTXJJb25qSDhRaVBIRG1MRVlwaFpjOW95TTZhTVpUaUQ3dTJNUWhXS01RSVVQY3lxZk95ZmtfWjROc2JzZFR3OEM0X0lpUEtRZXpUQU5QS2g1Wm5paU1vZk5vYWhkZnBxZjhUN0RGMEgwSHpMalNKYjF1ZnVYNk9JM1RkT3BlRDcxTjlhb0pyeDdqMjg?oc=5) <sub>Newswav</sub>
- 📰 2026-11-16 [文远知行-W将于11月20日发布财报，一图速览分析师最新预测](https://news.google.com/rss/articles/CBMitAFBVV95cUxQY2ZXc3FKWlMwdFdwaEFfRVN3UENFRGh4bU4zMnhLUHY3NGo3LWhNakk0Z1I4R3hia1huTFZ0bzB2UW5QNDNtZ0pYMml1a2hlT3pscUwzZHVQcFpVNTJ1VjFYYnVoZ3pzOElSd1FxTDhvdDNmVXR2Tm85Y3JscGhsbFgzN0hfVjQ3a2ZhUDE0aGRPd1RUN3hHbHFlUUZPUHQzSjc3ZDdxcEpDbkU3cVRoMVMxSHY?oc=5) <sub>Moomoo</sub>
- 📰 2026-11-16 [特斯拉FSD准入引讨论！文远知行L4 Robotaxi已在国内多城落地运营](https://news.google.com/rss/articles/CBMijAFBVV95cUxQNGktZ0FBclhpVzNJbkZDUktLZEJ1Q095MHNzUDNCelV5SjVEWklfaVQwMXJYcGRvbGJmOW5jV0E4LURqYVA1c2FjQWplTnFkRTVsUHA0elBJam5UNHZWekFGWk94c1BVRkd0VVlmeVJnWXVlY05GZ2lsd0lBcUNSdE5UMmVXekRWajFNRw?oc=5) <sub>Sohu</sub>
- 📰 2026-11-16 [埃安Ray7配置参数全解读：12.88万起值不值得买？3个维度说清+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE5JS0pfazUycGEwZ3lYUVBQN2pqS3FOWFRMSUd2TjVyaFZKRVowOEhxVTZ0T3pTQ3ZYLVpISXZkb0tGTF9GM29uTGxTUEFfYjlHS1duNXZjZ0NabDBsWENZMjl5Qk9WNWVKTmV6SU1HVlhhdw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-16 [无界进化完成超亿元Pre-A轮融资，将用于AI4S基础设施建设](https://news.google.com/rss/articles/CBMiZEFVX3lxTE5fRkRiUnNlS0E0bmV0SExZMlRLX0dUS1R0Nlg2emVaWE5LM2RTRGN2TTJENGU4dkppamxJZGRnSEZHN0NwTzRBWk1VNzVrUXJ4OXVlbF9fZE9mR2xiS0JRckcyY00?oc=5) <sub>新京报</sub>

</details>

<details><summary><b>Horizon Robotics</b> (77)</summary>

- 📰 2026-11-16 [SAIC-VW ID. ERA 5X hitting the market](https://news.google.com/rss/articles/CBMiggFBVV95cUxPWDBrZFRDNVA0OEpaNVNuQm4tclF2aDlBQ1hXd24zbWJxRXlyNzVFd3RObk1ldEt1dk9LZmI2ZjNKNHBCUU8xUVFuMGsyQnB3c3U3VUREYkJ1UFdzWS1oZFNaRHU2dkJIbDNOUGxYbFlmLTExdnBFd2Zmcmx6SlBRYXFn?oc=5) <sub>China Daily Global Edition</sub>
- 📰 2026-11-16 [Volkswagen ID. ERA 5X Goes On Sale in China at Just $14,900](https://news.google.com/rss/articles/CBMinAFBVV95cUxPRjJKTE85RXlGMEVJdklmY2U5OHNQMXd1eWxySG9rNTZTT0g0czE1WXdfN21nTEgwVUh2WDBXM3hkM3p0cExxY01RSmhuUEVMbGR3a2ktOFhXN0VDU2s0NFlDV0NETWJ3ZXdDSTZFSGF5dlktemZZLWRac29oODJBZlBPRlVwczBfMHMxUEJXUTRVSkNGNC15WUFlb0Y?oc=5) <sub>Electric Cars Report</sub>
- 📰 2026-11-16 [【视频】304不锈钢油箱都用上了！iCAR V27 底盘用料怎么样？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE92amwyLUF0MERlSEFMWm5Sa2lwc0Fyd1dLUzRjZW9ybmxzZXpIT0NvQmw3LXpLbGRkSnNScG1xZlI4blFjUC1fMGRFQ1FXR2FpbU1vQzlVMG5CX1k?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-16 [11.16-11.20将要上市的8款新车，最便宜12万出头](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5tYldmUVVLOWFIcW0tWVFTcENJTmEtS1BKVVY3S2xNclhmWkJ2bDlXNXp0VDhYSng3UWdZQXBhS2xielpudnRTUVZlaEpXY0JTMk5ia053bzFKMDQ?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-16 [10万买电车，捷达M6智驾+低电耗，MG4空间小怎么选？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE0xUmZIY05ILW9CaXpDU1djb3FTMmVTeUxVNE9jRU9DckNreU1MWFdsOTdnd1M0bVZxbmZCd0JmV0hfaEdGOENjcnpreW9TZ0RXWEtUUVdadXhqQU0?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (22)</summary>

- 📰 2026-11-16 [又一“国产保时捷”？赛豆ME7实车到店，大过小米YU7配571马力](https://news.google.com/rss/articles/CBMia0FVX3lxTE5fWTNxTkVfa2RHM29CZ3JabmtSbllKTVdGN2x4aVpqS0U0bG81RTFHeDhqNHZhaUg3MGJFVjEzOVU3aDdIMS1zR05mNXZ0blNyZ3cxVWRnVF85bmc3Tl9aenNZSlpDaWRDSV9n?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-14 [DeepSeek无人创业](https://news.google.com/rss/articles/CBMiTEFVX3lxTE1QUnM4dm1XbE8tWmIwSE1hN1JMTjZKRklrM3FmbkdNbVd2WllWUWpjQVhYV0xwaHhqUHp4T2ZkMGpHMExqWjFNU1lPYXo?oc=5) <sub>凤凰网科技</sub>
- 📰 2026-11-13 [【视频】小米澎程N90和特斯拉Model Y L怎么选，同价位还有哪些推荐？](https://news.google.com/rss/articles/CBMiW0FVX3lxTFB6dElibXRFYWFsZU9vQnhjX3YwZjF2VVd6QjhLdXJIV3pmRGhzTmpuTFRER2xXV1Zjc2ZqNld2RVY1MkxrTENqczVRc2MwNHl1VFljSkt2TjRxZ0U?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-13 [Valued at over 500 billion yuan but barely producing founders: Why DeepSeek has become a "settling pool" for AI talent](https://news.google.com/rss/articles/CBMidkFVX3lxTE5BN29naDgxcE4xa2NUUi1qSlFKTHpBZlVjVVozN2FaWS1kVy1ENkxsV0dxVTlQS0ZJWHkxV3lfY09LN2xldl9XYk1mTFA1SjBUdTJfV05LYWllNFJZZ3RwV1VPSmNQZGk1a085UGFMOXloMHE0d2c?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-11 [【视频】特斯拉发函，媒体CEO：放马过来#特斯拉#埃安Ray7](https://news.google.com/rss/articles/CBMia0FVX3lxTE5xOHhzcEd1V1RKWmxPZ3BEYUN6NGRhOXB2cHFXSWxFNGEzdjFPbkotY0VMQlpGTGxyV0FCc3p3S1NkU1NjSjI3b01nN2FTcnl3blB4dC00UGlQNlk0Ukp4SEhIYUtSVXNhRlQ4?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Mobileye</b> (13)</summary>

- 📰 2026-11-16 [When Human Superstars Shine: 9 Unmissable Historical Snippets Between Elon Musk and Jensen Huang](https://news.google.com/rss/articles/CBMiU0FVX3lxTFBjclJYNXBJbVBjYUxUQkJCU2pOcDBpVnZZZ2lqWDhZY3lzYk1udjlFWGxNS3loQjAtUDdKYXJySWZWZTJLQ1I1UGtueDdvd2E2RGdJ?oc=5) <sub>eu.36kr.com</sub>
- 📰 2026-11-14 [May Mobility plans 10,000 ID. Buzz robotaxis on €9 million revenue](https://news.google.com/rss/articles/CBMihwFBVV95cUxQdkgzeUVTSS1wc1czVWhUTllrV1ZaVk1VLUUtUTVhTlFVSnJVSGFvcmtvRC1QZHNnWUxHY1B6c3gtUjZqdzFRSm9CSTNuZENtdFlRZGpoaDZGalJQb2xmZ1UtMGJyX1JObkdfaVF6SThudG9kajdDaW1xZVY4dzFraUF6NXd5RVk?oc=5) <sub>AutoNext.co</sub>
- 📰 2026-11-13 [Automobile manufacturing stocks Q3 recap: Benchmarking Tesla](https://news.google.com/rss/articles/CBMivAFBVV95cUxQemM0Qm9BZXFLb2o3YWdJWkFwb1FLcVdMb3NZNDE2bTB2U0hTb29PbnRiQXhFejA3ZklYUEdTR1lZaGpFT2tjOWJPT0luaXF2aXI2ekRhSlhPQnpQNWxQQUpLdTAyeWxvN2dBV2dNcEhiM0VDOWtwNzNtUHlSVVBmMVR3eDZKTWtXSWRvTUd6V1FhVzRqX0MyMDZjQm4xdjAwRmREZEl1X1V3b25CVk9MSUF6Q1draU9nZU1peQ?oc=5) <sub>TradingView</sub>
- 📰 2026-11-13 [Korean Optics Maker Optrontec Triples Profit as US Automakers Replace Chinese Camera Suppliers](https://news.google.com/rss/articles/CBMi3wFBVV95cUxPWHNlSUphR3lWUXJBNm93Mm1QdFZ1MVVSZU9jTlBxc0ZuR3JyU3pYQU9OUmk4VDh1NnhCMnV3dXdSenBkVldzS09Zb0NVeGJSc1V3aXhiU1E1aTNsd1RydXlIT2RDdDk5SWZUOC0zbTNlbUxxZVpMaUdIcm1lRUM4U1k0TVBhUmNtMXlCUDh2Vzd3dXE4aGxCRDZlaU5MZFNHNllfRDM3dXoyRWlTckRFREZfRjBpNjhLaW5YVkd3OWJuQWRLVmE2ZFpOck9zdXZrYnVXZk5pYks2WnFKNURZ?oc=5) <sub>Tech Times</sub>
- 📰 2026-11-12 [JPMorgan Downgrades Self-Driving Technology Supplier as Volkswagen Faces Delays](https://news.google.com/rss/articles/CBMi1gFBVV95cUxNRXhmZ1ZxandRVnNmaEhwZmljMjNVemVoUEIzVFZPQWlGQ0lxeTNES2JuczR4dnZiU3hpUWlydklMWXVLeW5tWVBFSVVlY2hfXzM5dm4yWEZ4UmJYcTdJU2o2MWZhS1VMWkhwb281SndVb1BkN25QTUV3TURlUmxVTzdYTUFDVFVVTkdKRk1wVlpzMmZ0QjZqWUw5ZDU4dnV0bXhzZEtJYll5SkFlZFBxWFU2aGFvYVZLWHQ1d3RfZDdrdVFzQkVUd09lUjlqYjVTWlNSZDhB?oc=5) <sub>TradingView</sub>

</details>

<details><summary><b>Aurora</b> (31)</summary>

- 📰 2026-11-15 [Archer Aviation And 2 Other Penny Stocks To Watch](https://news.google.com/rss/articles/CBMixAFBVV95cUxPMmkwbVE5akZOMWNlM1ZOMzhiRERnSDM5Y2hxc1dPYzdPN2xNdW11RnZXMXlfb09vQ0FpaUNwQnVlM1BYekRKMlpwU2h2OFRkU296MG4weU0xbENsejRhelMwR1AtclowWDhtZkd3WGdISDBjWWRCTTNUT2tWcXN1S05rR0lFLUlQVEpOSHJwc0VqcDVJZ3YzcWRncGZUTk5OU1UyUVhHVl92OFJ6MGxuWWRtTUthLVBEeldqcDVuM201VHVF0gHKAUFVX3lxTFBVM0k1cUlMdzFYUy04cDBhN1IwU1J4cWkxQzlOY2VyNUJjQWk5VHlrWVlBcVlrRnBkY1JXdjFCUm9Fa1VxLXVKSWpxdnJQV3U3OEtFdVhmSDhaUHMzR016a1FOMkpCQjN3bmZUTGVCTnVuaE9wX1dCbkJtb3FKSzE5TGNpbmMzbDNFQWFaRkpqSVRFdXhHaFNZa2F5OElxZzhBS3VwMXlCMW5DLWV3bmhhck1HdTVhZ1VLLWptcTZtQXhYa0l5aEVPN3c?oc=5) <sub>Simply Wall St</sub>
- 📰 2026-11-14 [Should Truck Production Delays Require Action From Aurora Innovation (AUR) Investors?](https://news.google.com/rss/articles/CBMi0AFBVV95cUxQM0Z3WEJQclFZaGZESEs2VUNRSXRLVnAzUW9Mdy1hSFQ0QTBXdWs2ZVd1SDdFQXBFZWhGM0IxamZKcmN6VGQwaGpORzFNdEZvUE16T1pDN3VGa3pmRmR4VHF6YV9yMFBVYnllUnlOdmxzWUR4bzhab1A2dlVNSFllS0NmQXBJQ3BRcDN3V0wtQy01R1R6ZmQ2SHpkTFFVNTBmZEdTTGlJVmV1YWtHX1F4c0lJWlljVXZkbWlKTlZjMDhLQlgxWGtrN1pJc0RJYVhO0gHWAUFVX3lxTE1VS1NpejQzUVhxSnEwMjZ1NE53QUlwMHZ2dkxRNFhpSlE2RHJpeEZ1ckZFZlZQMmxGbXYyRHNXaXNWLWNrODc5eW1oTURNc3ZSUVZOY0FpaEh0UEZUcjJMZjJJWjFLWDNxX1VEVzE2a2NGTEtwZDZjOHctVE53Q094YlY3c2NybEN4UTV6MEZSTjlvRlhWc2M1VjdlaUxoM2ZqTW5QRkVTVWR0a2hnV1ctejNVaFdiaXNzakV6ZGRIblEzVVp4Y0x6dF9xM0RiV2lCcDFFR1E?oc=5) <sub>Simply Wall St</sub>
- 📰 2026-11-14 [Aurora: 3 Key Takeaways for Long-Term Investors](https://news.google.com/rss/articles/CBMilwFBVV95cUxNMVFqdzVjR2I5Ulp3TldKbTdXUWprU1BmWTAwMXJOTVl2cWQwZGdNTF9qRlIwVFp0OG9Qdk9QcEY3VG81cG9iV3dFTWVRRFltM3I4ODRDQ2pNUUlhc09zS2Q5ZU85RVNoUHBOb0Y5R1FRZXJ0V1I2Sk9kVUpjdlU0bFpCM0N5TUY1NUxONDZMN2pBeWs2ZVBz?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-11-14 [3 Penny Stocks To Watch With Up To 72% Revenue Growth](https://news.google.com/rss/articles/CBMizgFBVV95cUxONWJzcExzODFFZG1rUElNUW9KYllJRkxMT2ZmaVNKNjdyb1RtMzZVUG5SMHFEYXZTUnpvd2JhSmVrckJ6Z3hCd1FUNEI1T20zQmZRQ1dqaUcxS3p3NTlZTm5MV1dWSG5wZUdpdDFKem5XdGVuaEh1MXhycUZKWWhSQm5xWl9GR1BoTlZ3TjRFeWJiSlZ6QVZMTC01S0FpRDhuMV9LRHhORFFoeXhCeUJWWjAzNm45RUxlX1JQSXpqX2ZQQzVkZ3N2QkNiRTNQd9IBzgFBVV95cUxONWJzcExzODFFZG1rUElNUW9KYllJRkxMT2ZmaVNKNjdyb1RtMzZVUG5SMHFEYXZTUnpvd2JhSmVrckJ6Z3hCd1FUNEI1T20zQmZRQ1dqaUcxS3p3NTlZTm5MV1dWSG5wZUdpdDFKem5XdGVuaEh1MXhycUZKWWhSQm5xWl9GR1BoTlZ3TjRFeWJiSlZ6QVZMTC01S0FpRDhuMV9LRHhORFFoeXhCeUJWWjAzNm45RUxlX1JQSXpqX2ZQQzVkZ3N2QkNiRTNQdw?oc=5) <sub>Simply Wall St</sub>
- 📰 2026-11-14 [3 Penny Stocks With Revenue Growth Up To 72%](https://news.google.com/rss/articles/CBMimgFBVV95cUxNdzdhdzhKazlYX1NsMEpMV3d0WExrXzlRRllxWVBnUVc1UTBVTFN0aXF3WGdwazY0X3ZaQVZXaGpyVEs0RFFHeU1EX2ZtOXA4SGhJcTVnd0pNNVlabWNxaTB2R1JaOC1jbkJWbVNoQlRxZ0kwTUZHRllvV0pTLU5YYnE1NEFKVUdrdmFnUjRPbHd2aFdSTmM0X0tB?oc=5) <sub>Yahoo Finance</sub>

</details>

<details><summary><b>Zoox</b> (54)</summary>

- 📰 2026-11-16 [‘Like one of those ski lifts’: Zoox robotaxis roll into Atlanta](https://news.google.com/rss/articles/CBMilAFBVV95cUxNT3NaVG5zekFkNTM0Vmg1a0ZxODR6bEJSVC1HcFBOc2p4TDBYTHlydU1Va3piOUJYWXllYjdrNjB0dF9ZNlBlbDVvNXhUS0kwdGh5eDNVZWNUSExsY09ZMXlwZFRlM1NzcnE0VEJOM05OM1Z5NWhQakpWZ3RhYjhlYWFwd3hTazN3TXdVbUkzMzBHVmst0gGoAUFVX3lxTE9ESlA2ai0wdUtjYjZ6ZGZZbUdLeVdMd3JrQ3lkQi1WSkJyTUtHd2Q4R1lTNF9pTGU0b00xNDZJeDdFbV9ZVXNwQ0hENFBWd0dxMTFzbEpNRTlVaUpPR0tQSWE3Yld6TnNreVBVaWFuZGVjR0ZBcEUyT245OFI3ZzFzYW5iS0NPcGNzei1lQ1ItcFFPZG9fOWt0ZDI0d1BvV1ZDOUVHWDVEVw?oc=5) <sub>WRDW</sub>
- 📰 2026-11-16 [Zoox robotaxis are carrying a limited number of riders in Atlanta following more than a year of street mapping. #atlantanewsfirst #crimewatchatlanta](https://news.google.com/rss/articles/CBMiUkFVX3lxTE1CdWc2TnlYQ1QwNDBtWW9WU3BwQWtHZUtTU3JRNmo2c3JmLWRKZTlXY29TaE8zU00tUkRLZk5YLXZRb1Q4S2hGTUpoYWFzcGphR0E?oc=5) <sub>Instagram</sub>
- 📰 2026-11-15 [Autonomous ride-hailing Zoox adds downtown Las Vegas and Arts District rides, extends daily hours](https://news.google.com/rss/articles/CBMilwFBVV95cUxOanlfNG9PS2laeS1CU0djVGpQRzc4R1k5SkNrdXFESWN0VklJRzRHNUMtTDhHcmt2eExYWnNsOXl6a0U0dXFFYkQtOV9YWGlidXFXU2YwcnZEME1ZTENieXNRcHNGQnVsOGtsMmJFZEZKMFVGWkxxb1Z2aW85MkxvTHlHQTM1UDh1WjZ0Z1pHUUNOaUIzY0JV?oc=5) <sub>Las Vegas Sun</sub>
- 📰 2026-11-14 [Zoox Expands Robotaxi Service in Las Vegas](https://news.google.com/rss/articles/CBMihwFBVV95cUxQTFQtODdsVXI1akFuaVRmWWl5V19NMVJ1eERkdjB2ck15cklwOXoyY2ZQa283V3REVUZuTEJkYWN1ZFNZTy1IV3VFZDFtVEpHWU5JWEhUMHRIdVlodkk1VXN4cnNEV0tjbWIwaS1uVTA0aGQ3T3lULW12aTB5MTkxZm1FanFpM2s?oc=5) <sub>CleanTechnica</sub>
- 📰 2026-11-14 [Zoox Launches Robotaxis in Atlanta](https://news.google.com/rss/articles/CBMifEFVX3lxTFBuWnJ1QmFxN2RYUzR0SnVoYzFGdlFCTTNSOEctbFRLTENZOTN3UHlKZGlLak1vTzdiN0ZPS0puY3A5LTF3OXFNMHR2UGtMeXFVbC1Nc3RtXzhNWFJpdzkzU3E1WlIwbWRTdmtxQTJDZzZkdUpMNGhnazloRWY?oc=5) <sub>CleanTechnica</sub>

</details>

<details><summary><b>Motional</b> (16)</summary>

- 📰 2026-11-14 [Samsara's David Gal: Physical AI Starts With the Forklift You Already Own](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1aSWJmMnZVNkpEUFZYeV8tREdvaEp2VVRpZXRZYURLbzNDRkR2Y3N3Uy1YSi1UZzV0Z0U4VWZLalRXZzhQaGVGRmVGekc2TktFWnlScFpJRHJFdjQ?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-13 ["Cars That Keep Going Even When Sensors Fail"... Hyundai Motor Boosts Autonomous Driving Reliability](https://news.google.com/rss/articles/CBMiZEFVX3lxTE9BX3gtSThrelhocW04V2VGTXc5NnB0X1F6VFBlenZLX2Mzc01UY3o1c2E2eE8tQzdqbktEOVIyTzBtdnFOeXF5NlEzS3lIXzNLMEVzQ1V4dTQ1M3ZXY1FQR21pank?oc=5) <sub>아시아경제</sub>
- 📰 2026-11-13 [Hyundai Motor: "Safety Over Speed"... Ensuring Cars Keep Moving Even If Sensors Fail](https://news.google.com/rss/articles/CBMidEFVX3lxTE5Vc1NOV0ZacmFwUjhSNVhhSTc3VFQ4QV9DanB6aGNSWFhONW1CcEpyZ1NaNm9heUk2ZGhLRm9XaE5NcXVJZUtjUmJIeDQ2TUFEczBVem0tbGYtRkp6eVlhTjVHdmtVUno3NmRpZldWalhZbUYz?oc=5) <sub>아시아경제</sub>
- 📰 2026-11-13 [Huang’s Exit Puts Hyundai Motor Group’s Dual-Track Autonomous Driving Strategy to the Test](https://news.google.com/rss/articles/CBMidEFVX3lxTFBZTG1rU1ozSDFnd1diLWNmZVBXcFRjZ0J1UGpqZ1BCck83SFhJOUhBcDE3ZlZKV0tod29JZzh4dVctU0pYR2h5bWxSTVg3ci1XTUFMeVh6WmQ3SkpncVBadDZMX2p4VWlzSG1MQVh5NFZhWGVN?oc=5) <sub>Businesskorea</sub>
- 📰 2026-11-11 [Korean firms shift CES focus to industrial AI](https://news.google.com/rss/articles/CBMiqgFBVV95cUxQQVpGVm5oN2E0dXpVQ2tfaXVaZXlZanNWcllzRTJCc19OS0F3V2Z1eWEteEpub2dQWWJleEtYMTVyVkRGaVpmWmwwQi12V0JhdjlvRENjU3JWMlpLTkJkOHhMYl9JeDh0RU14Mm5fZmx0X1Z4NlJTYmtKNkc2ck4wT3pQTUZxYjFmQ2M5a1ZoTC1WSmZOOGxMOGJFakVoTm4tcTNaekZZdVFWZ9IBqgFBVV95cUxQQVpGVm5oN2E0dXpVQ2tfaXVaZXlZanNWcllzRTJCc19OS0F3V2Z1eWEteEpub2dQWWJleEtYMTVyVkRGaVpmWmwwQi12V0JhdjlvRENjU3JWMlpLTkJkOHhMYl9JeDh0RU14Mm5fZmx0X1Z4NlJTYmtKNkc2ck4wT3pQTUZxYjFmQ2M5a1ZoTC1WSmZOOGxMOGJFakVoTm4tcTNaekZZdVFWZw?oc=5) <sub>The Korea Times</sub>

</details>

<details><summary><b>comma.ai</b> (2)</summary>

- 📰 2026-11-12 [Goodbye, BlueCruise! We Install a comma four in Our F-150 Lightning](https://news.google.com/rss/articles/CBMirwFBVV95cUxPY1o5ekZ4WnpraUxVMHV6OVdyMEtEbjQxQXY5STdJdXlHNlN6eUFZNzFwSnA5cFhHd3pNdTZNNy03dXBOZ1ZoX3RFX2E5V2JNTE9aVlhJaG90bW5YWEdzX2NGXzd3VFZ6NG5JVkFrM3daTmY4UDBTN1I4NWU3eGJqUm9tY1VaRWxoZkp3WDJLNnVLQjN5WG9NMzlxLWI0aVU2TFhLUEZwUE5YUDdUcWFJ?oc=5) <sub>Transport Evolved</sub>
- 📰 2026-11-06 [Canadian YouTuber Linus Tech Tips Tests Tesla FSD](https://news.google.com/rss/articles/CBMiggFBVV95cUxNZVZaT1Q4X0NlakJzTnFkTGdqTmFPM3pDbFZPUnBYVVNrVzFxMlpZQ3VaTEJFUmJrNVpjMmZ5RVphUDE4WURNT0x4NkhnN01LdTdzSEVnS2NUNkROams2cnNzNkpnalhWcDVuckhETUtxaDZrSHNXTXhKYUlpN2dPTlZn?oc=5) <sub>Drive Tesla Canada</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
