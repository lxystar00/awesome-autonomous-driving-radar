# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-11-22 · 1,278 papers tracked · 48 curated.

**Selection rule.** A paper is listed only if it (1) is primarily about autonomous driving,
(2) has public code, and (3) shows at least one strong signal: accepted at a top venue
(CVPR / ICCV / ECCV / NeurIPS / ICLR / ICML / CoRL / RSS / TPAMI, or ICRA / IROS / AAAI / RA-L),
≥200 GitHub stars, ≥3 citations / month, or a well-known lab with traction. Papers are then ranked by a
composite score (venue, stars, citation velocity, LLM rubric for novelty / rigor / impact, SOTA claims)
with a per-topic cap. See [`scripts/rank.py`](scripts/rank.py).

📅 [Daily digests](daily/) · 🗓️ [Weekly digests](weekly/) · 📦 [Raw data](data/)

## Contents

- [VLA / VLM for Driving](#vla--vlm-for-driving) (13)
- [World Models & Generative Simulation](#world-models--generative-simulation) (5)
- [End-to-End Driving & Planning](#end-to-end-driving--planning) (12)
- [3DGS / NeRF Reconstruction & Sensor Sim](#3dgs--nerf-reconstruction--sensor-sim) (5)
- [Perception: BEV, Occupancy, 3D Detection, Mapping](#perception-bev-occupancy-3d-detection-mapping) (8)
- [Motion Prediction & Behavior Modeling](#motion-prediction--behavior-modeling) (2)
- [Datasets & Benchmarks](#datasets--benchmarks) (1)
- [Safety, Robustness & Evaluation](#safety-robustness--evaluation) (2)
- [Industry Tracker](#-industry-tracker)

## VLA / VLM for Driving

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Teaching Vision-Language-Action Models What to See and Where to Look](https://arxiv.org/abs/2607.01658)<br><sub>Yuguang Yang, Canyu Chen, Zhewen Tan et al.</sub> | ECCV 2026<br>2026-07<br>📑 3 | [⭐ 38](https://github.com/ShivaTeam/DriveTeach-VLA) | Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving |
| [SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving](https://arxiv.org/abs/2610.20609)<br><sub>Shaoyuan Xie, Zihan Zhang, Jingxuan Wang et al.</sub> | CoRL 2026<br>2026-10<br>📑 1 | [⭐ 36](https://github.com/ASGuard-UCI/safedrive-vla) | Vision-Language-Action (VLA) models are gaining attention in autonomous driving, inheriting commonsense priors from large language models (LLMs) and widening the navigation interface from a fixed command set to free-form… |
| [Scene-Adaptive VLA: Efficient Autonomous Driving via Dynamic Layer Routing](https://arxiv.org/abs/2610.24590)<br><sub>Yujia Yang, Quan Yuan, Jiawei Fan et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 5](https://github.com/yang-luvu/Scene-Adaptive-VLA) | Vision-Language-Action (VLA) models offer a promising paradigm for autonomous driving |
| [AutoVLA-D: Learn a Trajectory-Geometric Condition from Reasoning for Autonomous Driving VLA](https://arxiv.org/abs/2611.12382)<br><sub>Yuguang Yang, Zhewen Tan, Canyu Chen et al.</sub> | NeurIPS 2026<br>2026-11 | [⭐ 5](https://github.com/ShivaTeam/AutoVLA-D) | Autoregressive VLA planning usually predicts continuous trajectories as the final output, but driving instructions often describe actions rather than ego states, which weakens direct conditioning on the final continuous … |
| [Locating and Repairing Domain Shift in VLM Trajectory Planning](https://arxiv.org/abs/2611.10720)<br><sub>Zhihong Cui, Hengyu Liu, Michael Alexander Riegler et al.</sub> | NeurIPS 2026<br>2026-11 | [⭐ 0](https://github.com/ZhihongCui/MoLaRx) | Vision-Language Models (VLMs) are increasingly adopted as end-to-end driving planners, yet they suffer from cross-city domain shift |
| [CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving](https://arxiv.org/abs/2607.04179)<br><sub>Zhaohong Liu, Hao Ye, Xianlin Zhang et al.</sub> | ECCV 2026<br>2026-07<br>📑 3 | [⭐ 1](https://github.com/MICLAB-BUPT/CritiqueDriveVLM) | End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving |
| [PixelPilot: Scalable Vision-Language-Action Models for End-to-End Autonomous Driving](https://arxiv.org/abs/2607.04637)<br><sub>Pin Tang, Guoqing Wang, Xiangxuan Ren et al.</sub> | ECCV 2026<br>2026-07<br>📑 1 | [⭐ 3](https://github.com/VISION-SJTU/PixelPilot) | Vision-Language-Action Models (VLAs), which leverage the advanced reasoning capabilities of Vision-Language Models (VLMs), show promising generalization in complex autonomous driving scenarios |
| [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)<br><sub>Nan Yang, Zhanwen Liu, Linfeng Zhang et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 11](https://github.com/Zizzzzzzz/MVPruner) | Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings |
| [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)<br><sub>Yuan Gao, Wenting Miao, Mattia Piccinini et al.</sub> | IROS<br>2026-07<br>📑 1 | [⭐ 33](https://github.com/TUM-AVS/Chat2scenic) | Validating autonomous driving systems requires diverse, regulation-compliant test scenarios |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 25 | [⭐ 563](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
| [GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives](https://arxiv.org/abs/2609.39601)<br><sub>Qize Yu, Lianrui Fan, Boyu Chen et al.</sub> | arXiv<br>2026-09<br>📑 5 | [⭐ 441](https://github.com/groundingpi/GroundingPI) | Precise grounding matters |
| [GRAVA: Grounded Reasoning-to-Action Representation and Learning for Autonomous Driving](https://arxiv.org/abs/2609.15169)<br><sub>Xiao Liu, Haoyu Li, Jianghao Leng et al.</sub> | arXiv<br>2026-09 | [⭐ 487](https://github.com/AhernResearch/grava) | Driving vision-language-action (VLA) models increasingly reason before acting, but their intermediate reasoning is often weakly grounded in physical scene evidence and loosely connected to executable behavior |
| [Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air](https://arxiv.org/abs/2605.31066)<br><sub>Tianle Zeng, Yanci Wen, Xueang Yu et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 1,140](https://github.com/louiszengCN/CarlaAir) | Recent aerial vision-language-action (VLA) models show promising single-UAV capabilities, such as tracking moving objects and navigating to language-specified landmarks |

## World Models & Generative Simulation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Orbis 2: A Hierarchical World Model for Driving](https://arxiv.org/abs/2607.15898)<br><sub>Sudhanshu Mittal, Arian Mousakhan, Silvio Galesso et al.</sub> | NeurIPS 2026<br>2026-07<br>📑 2 | [⭐ 31](https://github.com/lmb-freiburg/orbis2) | Current world models operate at a single level of abstraction, with most prioritizing perceptual fidelity while lacking the spatial reasoning and semantic understanding required for real-world downstream tasks |
| [FrozenDrive: Zero-Shot Text-Guided Driving Scene Generation and Data Augmentation with Parameter-Free Frozen Diffusion Model](https://arxiv.org/abs/2606.20110)<br><sub>Yuhwan Jeong, Hyeonseong Kim, Daehyun We et al.</sub> | ECCV 2026<br>2026-06<br>📑 1 | [⭐ 9](https://github.com/daehyunwe/FrozenDrive) | Synthetic data for autonomous driving is surging, powered by diffusion models that promise scalable scene generation |
| [MESSENGER: Memory-Enhanced Sequential Scene Flow Estimation via Autoregressive Next-Frame Forecasting](https://arxiv.org/abs/2610.10759)<br><sub>Jiuming Liu, Jianing Li, Mengmeng Liu et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 0](https://github.com/liujiuming123/Messenger) | Scene flow can capture low-level 3D motion displacements in dynamic scenarios |
| [ASTAD: Asymmetric Style Transfer for Synthetic-to-Real Adaptation in Autonomous Driving](https://arxiv.org/abs/2606.29286)<br><sub>Dingyi Yao, Xinqi Zhang, Lihui Peng et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 2](https://github.com/Dingyi-Yao/ASTAD) | Synthetic data mitigates the data scarcity problem in autonomous driving perception |
| [Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends](https://arxiv.org/abs/2606.01164)<br><sub>Jiuming Liu, Chaojun Ni, Mengmeng Liu et al.</sub> | arXiv<br>2026-06<br>📑 10 | [⭐ 251](https://github.com/liujiuming123/Awesome-Interactive-World-Model) | With rapid development of large language models and diffusion-based content generation, world modeling has attracted increasing research attention, benefiting various downstream domains such as game engines, embodied AI,… |

## End-to-End Driving & Planning

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [UNIVERSE: Unified Video Action Models for Autonomous Driving with Flexible Mask-Modulated Modality Generation](https://arxiv.org/abs/2607.05133)<br><sub>Mengmeng Liu, Diankun Zhang, Jiuming Liu et al.</sub> | NeurIPS 2026<br>2026-07<br>📑 17 | [⭐ 6](https://github.com/xiaomi-mlab/UNIVERSE) | World Action Models (WAMs) can improve action generalization in autonomous driving by learning scene dynamics through dense future-video supervision |
| [MOJITO: Modal Joint Learning for Unified End-to-End Autonomous Driving](https://arxiv.org/abs/2607.23511)<br><sub>Zhijing Cheng, Xuancheng Zhang, Donglin Di et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 32](https://github.com/mumucc01/MOJITO) | End-to-end autonomous driving systems commonly follow a cascaded two-stage pipeline where a perception stage compresses multi-modal sensor inputs into a compact context and a downstream planner predicts trajectories cond… |
| [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](https://arxiv.org/abs/2609.26792)<br><sub>Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.</sub> | CoRL 2026<br>2026-09<br>📑 1 | [⭐ 15](https://github.com/VAIL-UCLA/DreamStream) | Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions |
| [DriveMLP: When Training Strategy Outperforms Model Complexity in Autonomous Driving](https://arxiv.org/abs/2610.29676)<br><sub>Alessandro Canevaro, Julian Schmidt, Hang Yu et al.</sub> | CoRL<br>2026-10 | [⭐ 6](https://github.com/alessandro-canevaro/DriveMLP) | Learning motion planning policies that remain reliable under closed-loop execution is a central challenge in Autonomous Driving (AD) |
| [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)<br><sub>Shen Zheng, Anurag Ghosh, Gaurav Parmar et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 32](https://github.com/ShenZheng2000/WarpI2I) | Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs) |
| [G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance](https://arxiv.org/abs/2606.26017)<br><sub>Hang Yu, Ye Jin, Alessandro Canevaro et al.</sub> | IROS 2026<br>2026-06<br>📑 6 | [⭐ 7](https://github.com/HangYuu/G2DP) | In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors |
| [SimWAM: A Simple World Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.07468)<br><sub>Zongchuang Zhao, Xin Zhou, Tianyang Xu et al.</sub> | arXiv<br>2026-08<br>📑 22 | [⭐ 212](https://github.com/H-EmbodVis/SimWAM) | In autonomous driving, World-Action Models (WAMs) have improved end-to-end planning by transferring video dynamics priors to action prediction, but many still couple planning with future-video generation at inference, in… |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 21 | [⭐ 367](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
| [Latent-Centroid Steering: Single-Pass Classifier-Free Guidance for Command-Aligned Autonomous Driving](https://arxiv.org/abs/2608.00237)<br><sub>Meibo Hu, Jiamian Wang, Pichao Wang et al.</sub> | IROS 2026<br>2026-08<br>📑 1 | [⭐ 2](https://github.com/codingmlinprocess/LCS) | Vision-language models (VLMs) have recently emerged as a promising paradigm for end-to-end autonomous driving, enabling agents to map multimodal inputs and high-level navigation instructions directly to executable trajec… |
| [STAGE: STyle-controllable Action GEneration for personalized autonomous driving](https://arxiv.org/abs/2607.29517)<br><sub>Zihao Liu, Xing Liu, Yizhai Zhang et al.</sub> | RA-L<br>2026-07<br>📑 1 | [⭐ 5](https://github.com/CarlDegio/STAGE) | Driving style refers to the behavioral preferences that drivers maintain during driving, shaped by their diverse experiences, habits, and needs, and is typically reflected in varying levels of aggressiveness |
| [A Survey on End-to-End Autonomous Driving Training from the Perspectives of Data, Strategy, and Platform](https://arxiv.org/abs/2610.00926)<br><sub>Chengkai Xu, Yiming Cui, Jiaqi Liu et al.</sub> | arXiv<br>2026-10<br>📑 7 | [⭐ 110](https://github.com/Jiaaqiliu/Awesome-Training-Ecosystem-for-E2E-AD) | Autonomous driving is a cornerstone technology for the future of intelligent transportation, where end-to-end learning has emerged as a transformative paradigm that directly maps multimodal sensory inputs to driving acti… |
| [AutoE2E: Don't speak - Language free end-to-end autonomy A Real-Time Driving Model for L2++ ADAS and L4 Robotaxis](https://arxiv.org/abs/2611.22374)<br><sub>Muhammad Zain Khawaja, Zaynab El Mawas, Ryota Yamada et al.</sub> | arXiv<br>2026-11 | [⭐ 229](https://github.com/autowarefoundation/auto_e2e) | AutoE2E is an open-source end-to-end driving model developed by the Autoware Foundation Robotaxi Working Group |

## 3DGS / NeRF Reconstruction & Sensor Sim

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [MCSplat: Multi-View Photometric and Geometric Consistent Feed-Forward Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2610.25345)<br><sub>Yifei Wang, Wei Tian, Wenhua Bao et al.</sub> | NeurIPS 2026<br>2026-10<br>📑 1 | [⭐ 13](https://github.com/yfwang0824/MCSplat) | Driving-scene reconstruction via feed-forward Gaussian splatting from sparse multi-view images remains challenging due to two factors |
| [DriveWeaver: Point-Conditioned Video Inpainting for Controllable Vehicle Insertion in Autonomous Driving Simulation](https://arxiv.org/abs/2606.31918)<br><sub>Junzhe Jiang, Zipei Ma, Zijie Pan et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 18](https://github.com/LogosIntelligenceLab/DriveWeaver) | A pivotal step in autonomous driving simulation involves inserting foreground vehicles with predefined trajectories into simulated scenes |
| [Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796)<br><sub>Leshu Li, Jie Peng, Yang Zhao</sub> | ICRA<br>2026-06 | [⭐ 15](https://github.com/UMN-ZhaoLab/Pocket-SLAM) | 3D Gaussian Splatting (3DGS) has garnered significant attention in Simultaneous Localization and Mapping (SLAM) due to its advances in capturing fine-grained geometry features and synthesizing novel views |
| [NIDAR: NIR-Guided Intrinsic Decomposition for Scalable Scene-Agnostic LiDAR Intensity Reconstruction](https://arxiv.org/abs/2609.36878)<br><sub>Junjie Zhang, Jie Yin, Kefei Qian et al.</sub> | IROS 2026<br>2026-09 | [⭐ 25](https://github.com/Zjj587/NIDAR) | LiDAR return intensity provides complementary surface-response cues for robotic perception and state estimation, yet many simulation pipelines omit it or reproduce it using reconstruction methods that require real intens… |
| [MM-TRELLIS: Point-Cloud Guided Multi-Modal 3D Vehicle Generation in Autonomous Driving](https://arxiv.org/abs/2606.24301)<br><sub>Hongli Xiao, Youjian Zhang, Yucai Bai et al.</sub> | ICRA 2026<br>2026-06 | [⭐ 10](https://github.com/HongliXiao/MM-TRELLIS) | Recovering realistic 3D vehicle models from autonomous driving scenes is crucial for synthesizing training data and building simulation environment |

## Perception: BEV, Occupancy, 3D Detection, Mapping

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Deformable Gaussian Occupancy: Decoupling Rigid and Nonrigid Motion with Factorized Distillation](https://arxiv.org/abs/2605.28587)<br><sub>Yang Gao, Wuyang Li, Po-Chien Luan et al.</sub> | CVPR 2026<br>2026-05<br>📑 2 | [⭐ 25](https://github.com/vita-epfl/DeGO) | Understanding dynamic 3D environments is essential for safe autonomous driving, particularly when reasoning about human-centric, nonrigid agents |
| [Horizon3D: Sparse Radar-Camera Fusion for Long-Range 3D Perception in Autonomous Driving](https://arxiv.org/abs/2606.31096)<br><sub>Geonho Bang, Geunju Baek, Dongyoung Lee et al.</sub> | ECCV 2026<br>2026-06<br>📑 1 | [⭐ 26](https://github.com/geonhobang/Horizon3D) | Long-range 3D object detection is critical for safe autonomous driving at highway speeds, yet existing radar-camera fusion methods remain limited at extended ranges |
| [DRS-VPT: Directly Relocalizing in a Scan with Vision Point Transformers](https://arxiv.org/abs/2609.12557)<br><sub>Lanke Frank Tarimo Fu, Maurice Fallon</sub> | ECCV 2026<br>2026-09 | [⭐ 25](https://github.com/ori-drs/drs-vpt) | We present DRS-VPT, a feed-forward transformer architecture for foundational image-to-scan registration |
| [Explainability-Aware Frustum Attack: Exposing Structural Vulnerabilities in LiDAR-Based 3D Object Detectors](https://arxiv.org/abs/2606.29963)<br><sub>Chengzeng You, Binbin Xu, Soteris Demetriou</sub> | ECCV<br>2026-06 | [⭐ 2](https://github.com/SecMindLab/Saliency_LiDAR) | The structural vulnerabilities of point cloud-based 3D object detectors remain poorly understood |
| [PointLAM: Local Attentive Mamba for Efficient Point-based 3D Object Detection](https://arxiv.org/abs/2609.21780)<br><sub>Xuanming Shang, Weijia Zhang, Chao Ma</sub> | ECCV 2026<br>2026-09 | [⭐ 5](https://github.com/PointLAM/PointLAM) | 3D object detection from LiDAR point clouds faces a fundamental dilemma: voxel-based methods achieve efficiency at the cost of geometric quantization, while point-based methods preserve fidelity but suffer from prohibiti… |
| [PriorMaskMap: Robust Online Vectorized Map Construction with Biased Priors](https://arxiv.org/abs/2610.39283)<br><sub>Haoming Xu, Wei Li, Yu Hu</sub> | ECCV 2026<br>2026-10 | [⭐ 1](https://github.com/healenrens/PriorMaskMap) | Online vectorized map construction provides autonomous vehicles with essential, real-time semantic and geometric scene understanding |
| [Vernata: Self-Supervised Learning of LiDAR Point Representations](https://arxiv.org/abs/2608.06919)<br><sub>Oliver Lemke, Alexander Liniger, Abel Gawel et al.</sub> | IROS 2026<br>2026-08 | [⭐ 22](https://github.com/rai-opensource/vernata) | LiDAR serves as a primary sensing modality for robots operating in outdoor environments |
| [Towards Compact Autonomous Driving Perception with Balanced Learning and Multi-sensor Fusion](https://arxiv.org/abs/2606.02979)<br><sub>Oskar Natan, Jun Miura</sub> | arXiv<br>2026-06<br>📑 47 | [⭐ 9](https://github.com/oskarnatan/compact-perception) | We present a novel compact deep multi-task learning model to handle various autonomous driving perception tasks in one forward pass |

## Motion Prediction & Behavior Modeling

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [MolmoMotion: Forecasting Point Trajectories in 3D with Language Instruction](https://arxiv.org/abs/2606.18558)<br><sub>Jianing Zhang, Chenhao Zheng, Yajun Yang et al.</sub> | arXiv<br>2026-06<br>📑 20 | [⭐ 154](https://github.com/allenai/molmo-motion) | Motion forecasting is central to visual intelligence: agents must anticipate how objects will move in order to plan actions, reason about physical interactions, and synthesize realistic futures |
| [Flow-ERD: Agent-type Aware Flow Matching With Entropy-Regularized Distillation for Diverse Traffic Simulation](https://arxiv.org/abs/2607.06957)<br><sub>Seulbin Hwang, Kiyoung Om, Dae Jung Kim et al.</sub> | RA-L<br>2026-07 | [⭐ 0](https://github.com/seulbinHwang/flow-erd-project-page) | Realistic and diverse traffic simulation is essential to autonomous driving development |

## Datasets & Benchmarks

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [The Road Ahead in Autonomous Driving: The KITScenes Multimodal Dataset](https://arxiv.org/abs/2606.02956)<br><sub>Richard Schwarzkopf, Fabian Immel, Alexander Blumberg et al.</sub> | NeurIPS 2026<br>2026-06<br>📑 4 | [⭐ 30](https://github.com/KIT-MRT/kitscenes) | Existing autonomous driving datasets have enabled major progress, but fall short in sensor fidelity, map completeness, or geographic diversity |

## Safety, Robustness & Evaluation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [CCFM: Collision-Constrained Flow Matching for Safety-Critical Scenario Generation](https://arxiv.org/abs/2607.04451)<br><sub>Ke Li, Kaidi Liang, Yuxin Ding et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 3](https://github.com/KELISBU/CCFM) | Evaluation of autonomous vehicle (AV) planners in safety-critical closed-loop simulation is essential for real-world deployment |
| [CADET: A Modular Platform for Evaluating Distributed Cooperative Autonomy in Connected Autonomous Vehicles](https://arxiv.org/abs/2606.04072)<br><sub>Pragya Sharma, Brian Wang, Mani Srivastava</sub> | ICRA 2026<br>2026-06<br>📑 1 | [⭐ 0](https://github.com/nesl/cadet) | Deep learning models are increasingly central to autonomous vehicle (AV) pipelines, yet their integration has traditionally followed a monolithic design where perception, planning, and control execute on a single onboard… |

## 🏢 Industry Tracker

Latest 14 days of news, official blog posts and new open-source repos from tracked companies. Full daily feed in [`daily/`](daily/).

<details><summary><b>Waymo</b> (241)</summary>

- 📰 2026-11-22 [Waymo issues double safety recall days after California bans robotaxis from freeways](https://news.google.com/rss/articles/CBMiwAFBVV95cUxNT2ZkUHhXcVlDSGkyVjZONVotRGdoREg0WG4yQk9VX3FCSjN0TkE0QXY2VHRQWU5Vd3Y2ZFdsbXRYUXkxbzFlOFBDSXJKUlo4SnJkQVpReEs1T2hsLTJpdkliYUdfeHpwUEI2U2tmRFZsSWZ1czVQNWwxdW5rNFk1N0hYYzNkeHFkVDFlS21JbzdVellJNWVnOElmNTZFZWtUQmpwZTJBel9hZi1YNmVscXdRREE4aXY0MGg1QXR1UUXSAcYBQVVfeXFMTTFFdGt0aTZ5YXh5b1pNSmFTeVhHY21FSVJ3VUI1NXBDdk95aDRkNkxodlZIWUQ2V3h4WUdQWXg0cWpYWjdmT0pqTlF4YzRBNWlPQmdTQm1kd0k4RUM3Ny1PMjlET1JMdkFpN3hLV1lQOXdCVUc2ZDRQNjRhU25BTUxNMzRfRVQ1QUhncV9DWjdXbHN0eVd4RUxyZjVPdU5CZDJPbXZnbE9xMjZ1X2NSaUU0aDdwWElvY3FfTHhNSUxUMUNYem1n?oc=5) <sub>Fox Business</sub>
- 📰 2026-11-22 [Can Waymo drive on freeways now? No: California's ban stands and Waymo has filed two new robotaxi recalls](https://news.google.com/rss/articles/CBMiwAFBVV95cUxQNUFwWVM2WGVCeElUT3VYcEw4Z2RpelJNVTVZbzJSdzhvVzhwNXlzZmM0WEF3LV8xZjZaT1JWb3cwSjVXVDQwS1VLYlE0YVR1aVVmUzNka3lGbmh5amQyOXF1RjFUX2VBU2FHeTNMMzFVWGxBZlAxbFQ5M25DZ1FnVXlTWHR2Uml3ZUFZMFhxa0ZfUUEtaDg3Rm0tMEhuSk8xUVUzLTA4SUZwRk1SVlZzVWx5cjZ0VGVlX1hxTmhEOXM?oc=5) <sub>Nacionale</sub>
- 📰 2026-11-21 [Waymo Recall Shuts Freeway Lanes, Forces Manual Control](https://news.google.com/rss/articles/CBMikwFBVV95cUxPeUFuM2R4a3FLa3l3V1FtVXUyU1lTRjVxdWlIajZFV1UzNmFldDFWSzE1dFlUalVsRlV0NW9SWDhHYTJtR01tYTh4X1dkSHE1OTJQZ2lhUlZhRHpBakV2TlFwU05CaVNVdmQxZjVQQnh0alJMRTgtNVlHcy1KRml0a0JvRUlodE14TDZUZ1R0blpFR1U?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-21 [Waymo Robotaxis Face 2 Recalls Over Closed Freeway Lane Violations, Traffic Control Issues](https://news.google.com/rss/articles/CBMilAFBVV95cUxQeWIwMTV4bS1fdnVHT3NrdkptejF6NURtRDdHX1JUbTFhZ2Z3NmZOaC1BM1M0bkVLQ1FwWjFBbnVzengxSU10UUI3U3NvcE1Vc1pxMjEtR015LVRyeFk5b3dpYmpSdVBKLTJKVVdqMmYyVkVCMkJJb2FSd3czd19RRGZYRFZhOWNyZmdPbTJHb2JNUTlj?oc=5) <sub>Benzinga</sub>
- 📰 2026-11-21 [Opinion \| I’m a former Lyft driver. This is why I believe in robotaxis.](https://news.google.com/rss/articles/CBMiqAFBVV95cUxQZ2NJeEtCTlp1bEtlMGpZdWZGUmxEa1NmU3dxVjBjMkM4SWdXTlpFeVZ4czcxai1GUVVZNnJnWnA4akg4eGFwbUFadWhNNjhvMGhJVTRLVHlKaUVLcW03djFXZDlOZFlHNHBHdTNsbUNBc1RlU2FzQUE1RU02RV9tX3I1a0VHSU5ueTdCa3luXzhNdS1pMFlyTzMyMnIzV1l2Q2NoTjBuZ3Y?oc=5) <sub>The Washington Post</sub>

</details>

<details><summary><b>Tesla</b> (350)</summary>

- 📰 2026-11-22 [Tesla FSD v15 Is Rolling Out: New Gestures and Quiet Mode](https://news.google.com/rss/articles/CBMibEFVX3lxTE1XcVpObUVKMU5FYTEyZnVHck9jQXlIbFJPRWZQWWZzWnJxR3pjZi1UT0E2RnR3QmxRWU5EMzhMUWZXSW5QT1FnLUlXMWJzRk5HUFJjbHF5LXpyTWtxUVdleVhFVzkwaXhlWXA2TA?oc=5) <sub>BASENOR - Tesla Accessories</sub>
- 📰 2026-11-22 [Tesla FSD V14 and Disabled Drivers: 1 Test, 1 Warning](https://news.google.com/rss/articles/CBMimgFBVV95cUxOYm10VE8wUUUtNmloS3lGdmFNVHBxRC1vMndiblR4U2tTUXI0anBnSGJrbmRWME9xenFraHh2WklZNmE5OXY0X0Y0SDNfaWhJMlJQdnAtRExYbUlXcXU3cXJhUVBaWHNFTVJwRTJMc0NjdzdkakVIQ25KMkxaQjVmMmF2NHJCNmpmYmhsSEZvaVlBanU2NjREUnZB?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-22 [Tesla Begins FSD v15 Rollout to First-Wave Customers](https://news.google.com/rss/articles/CBMijwFBVV95cUxQNGJpaG1ROFlUQzE0TWkzZFlXSkhVampmNlNxS2JsQnpxSXNXYVRBYV9TUzd1X21tNXdhM2ZYalpDQThZQ01DN1gzckJlSEczY0JxblpVQWZFZ194SnB0VUVvQUtBY3hlWkg0RTdMTi0wbTI5d1luRlF6bXVzTUV4Rm43WU82MGNiek1Ya2V3NA?oc=5) <sub>The Defiant</sub>
- 📰 2026-11-22 [Tesla FSD v15 Rollout: 25x Claim, Full Release Notes](https://news.google.com/rss/articles/CBMikwFBVV95cUxNQ0lkaV9YZlF1NzEydGZ2U2xlWERQY3RyODFLSm9FQXpmTVpaTGdqTTFDdjA5NUItOVIxWFBXZHlManBza1FtS09mQUg0VE5IbENhb0NfU2FDZVJwd2FnT1l1Tml0enh0TVFua2lBcThXVlZZVzVOcnQwNTFOX2lFRDk3a3NsaXoyaHBFYzZHZTBWYWs?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-22 [Is FSD v15 coming to Europe and the UK? Not yet: Europe runs v14 as Tesla Assisted Driving](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNdTdoZWdwdGhmNWUtRjB6Tm8yX294SW1wdjQ4bEZKZF9jdUJnUnYwcXNQYk9vZk9xNnV2eVF2QmRmVHQ0TTdFRGtUUERNTHh6VFZGdmdDSkxQMzQ4eExZNEFHZExUZUhZN00xM3ZZd0c5d2NDUm9nU0syZ3dObVVBYmJlT1FTOTBKQ1ZyMXo3LWZXWVM5LUtMMWdwWmI4Q0dhQXVsdE5zWXRBZw?oc=5) <sub>Nacionale</sub>

</details>

<details><summary><b>NVIDIA</b> (219)</summary>

- 💻 2026-11-19 [NVIDIA/nvidia-linux-utils](https://github.com/NVIDIA/nvidia-linux-utils) <sub>GitHub</sub>
- 💻 2026-11-16 [NVIDIA/scadactl](https://github.com/NVIDIA/scadactl) <sub>GitHub</sub>
- 📰 2026-11-22 [GPU Audio raises $1.1M to bring sound zones to cars](https://news.google.com/rss/articles/CBMijAFBVV95cUxNd00zazZhOWxxSEltUEVTTlJTMHpQYzY0N2RWX2VTaVhHdDkwcTZKTjlpb0RiN1FaNHRkMlNSOUVSeXdVVHo4cFNEdzJUTFBVVEZxcG8zMFZDWXB4cGx4TFprU0hhNUVzbWE0bVdPZUNnNnNWN2tjN1ctRzlzZXgxNEFYckVRcTJORmQyYw?oc=5) <sub>Dealroom</sub>
- 📰 2026-11-22 [Nvidia says RTX 50 cards are unaffected by its SSD-write bug, but some owners disagree](https://news.google.com/rss/articles/CBMihAFBVV95cUxQT0VjSTVLQndPc0lSZWhJWHJhNUFlQzVHZWpCbDh1TUFyNjhvYklwNlJiNktOdE93cmlqcGp2d2xnTFk1dHl1WndGWWNxcG1yZzNEcC1CRExHQXBhMmE4bTJ4a3R4VHRUOTdrYnNmNUFsd3VLLUlsSDVEMUY1YnVGU2dGMHA?oc=5) <sub>MIXED News</sub>
- 📰 2026-11-21 [NVIDIA Releases Hotfix Driver 621.35 to Fix Excessive SSD Writes Caused by Background Process](https://news.google.com/rss/articles/CBMickFVX3lxTE9mcVZCOElhRmFTYU5tSkQtSHRWRVlnbXFuQTE2Y1lscnl3aTF1VmRsUmNSaV9KOUxJdUlEM2FORjluRUpFXy14dmtnN0l2YTJKQ3BodlViYThXRzR1ODdJTlFDRk5QWWxQSWk4alhIVENtdw?oc=5) <sub>TwistedVoxel</sub>

</details>

<details><summary><b>Wayve</b> (47)</summary>

- 📰 2026-11-21 [California Bans Waymo Robotaxis From Motorways](https://news.google.com/rss/articles/CBMilwFBVV95cUxQSnRJcXd3Z0dtS3FZTzh4cHoxclA2Unh0ZWRwZTBKbVZxd0VBSEtOUXBQVWduZjFyMmtfOTdoQldVMUlGQWhtenRwRVNnOElQamx2V1lXUEFINGxrV3FQYUVFTHhWcHhFVmRkYUxDbGZoa2d5VWItS3BFaDBBSklVakFnSlFIOEMzcXRuSWxnMlkzQzNyWGFR?oc=5) <sub>Wisevoter</sub>
- 📰 2026-11-20 [First Shift: Tesla to sell Cybercabs for private ownership](https://news.google.com/rss/articles/CBMikwFBVV95cUxQcmhja0Z6TGs3XzF1eW9pcUc1Ry0wQU8tVDhWOG9UVWhfZHhRNXJNc3hicjdmQVBiV3JnWGxsVGZwd1hhRXV4Mmkxa09vNDYwb3dOLVhPNnhQMDVEdlFoVDRGV3FxbnhHXzNnRnBIUlB0cEliQmJHeEF2OW9rU1piSmdVWEIzQnBnMFVnMzJFNFlJVlU?oc=5) <sub>Automotive News</sub>
- 📰 2026-11-20 [CoreWeave and Humatica: Scaling Proprietary Enterprise AI](https://news.google.com/rss/articles/CBMijAFBVV95cUxNUlZMWTNaYTJnT0RvcFhBWXFRQlg4aVF3WWFNTkRPZVJ3S09zX2p3UzBSTTcwWnJGci1Pb0JHb3ROTG1RY0NRMElaRUI1SG91bXpvdHRrc3ExRktrcllHV2IwbTgwTzBjVmNvR1lNcGdDSlJhOVphTk1YQU0xSlBRYmphZ191U3lZSXZKSA?oc=5) <sub>AI Magazine</sub>
- 📰 2026-11-19 [Qualcomm takes on Wayve, Chinese rivals with new AI driving platform](https://news.google.com/rss/articles/CBMihwFBVV95cUxPSmpFQkxRLWs0ZU16X1hveXRWQlJDbnpiZDZoa2FnVDRVYloySE5qSHpGQUNJb2ZEZjFLcGxrRTViWmhYS3pybUp1SHFuZWU4eWNSX0o0REtSa0NVVDJCaTMxRzlKbGhpN0RNRzVUVFhsMmx1RUk4V1dFYzJoSFhvLUZXMWZFM1k?oc=5) <sub>Automotive News</sub>
- 📰 2026-11-19 [Bolt and Stellantis plan autonomous vehicle trials in Greater Paris from 2028](https://news.google.com/rss/articles/CBMizwFBVV95cUxNVmF4U3dEUHlQTHB6NTdHSVhBT2dwblNQSXhLbnlMQUVCQnFTSVJ0TW9KcTdlTmhLZkdsRDg2TGxBMGVvdkNSamNaV3lmaXdkSXI4UVlyZFd1Z2hYT3gtU3NGVmVXY3N4WHZQMjRxSEM0OENfVndrT1E0Q2pOQ0pfUExTYXdadzlUNFhxaF8tTWdwVmszVm9NM0JlaktadFJPaWZ1eFkzMUVSdXVOSlpPZVhLNG40THc1aTdaaGJ1c0F2R0tnMjBkY25FakJfRzA?oc=5) <sub>Robotics & Automation News</sub>

</details>

<details><summary><b>Momenta</b> (109)</summary>

- 📰 2026-11-22 [Uber and Momenta Launch Supervised Robotaxi Pilot in Munich](https://news.google.com/rss/articles/CBMikgFBVV95cUxOeXdWeUxBNWpfNEg3UmEwMUd4U2l2SmVtYkR2VjlibUZoWl9iNVNUd2lXSWx6Y1M2NnB5LWxnLVF4MExobHJ6UTJGcWNHN1VaWDA4SVBYOTN5TTRhVTZqWWNhXzlqQmpXSVdTNmE1WVlZalJCbFprRDE4TEg3LXlqdzN0bFJIaVZWa1pHcHA1X0lHZw?oc=5) <sub>Electric Cars Report</sub>
- 📰 2026-11-22 [Kakao, Hyundai Motor, and Socar Compete in Robotaxi Services… They Need to Join Hands to Get Moving](https://news.google.com/rss/articles/CBMiXkFVX3lxTFBLTWFnNExOTUIzcG5MMTVtNUh2VXB5VjBRRXhySXRiNF93OUQ1RFJDYXVNODFxUi01aFRxZmhhZVZlUC1xdzlRaXF1VlUzaktudl9aMzducnI2d2I1NEE?oc=5) <sub>경향신문</sub>
- 📰 2026-11-21 [中国Robotaxi出海， 开始接受欧洲乘客检验](https://news.google.com/rss/articles/CBMiUEFVX3lxTE9CZkF5cmJhbkg2SkhFZXRJb0xPdDgydDlTTWJaMWRZR25sWWFVQ1BUYVVlSTVnbDA1emkzU3VzNXp1TUZ6XzQ0VzAybTZ3azBx?oc=5) <sub>盖世汽车</sub>
- 📰 2026-11-21 [Momenta获得了全栈ASIL D认证，智驾更安全？](https://news.google.com/rss/articles/CBMiW0FVX3lxTFA2ZEZEZ3gzdlFjdjYyN2VLN01aNXNQSl82aGhseGZDOEJqRkc4VG1sWjNiYUVZTUpna2ltZVh2SV9NTHAyaWVpNUdCNFV5dXBSMFNFa2swVmc5SDg?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-21 [【视频】带你看MG 07，845km+Momenta R7激光雷达智驾，15万内超哇塞！](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5jcWVHbGoxQlZtYV9JMi00WC10ajh2Ml95S3BZNWd0NXloMTFLc2RrNmRESkVHMDJ0Tlg2emh5MC1KODM1QTZnbHRjbFBZM3M5UmFNbDEzWWVWSFk?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>XPeng</b> (203)</summary>

- 📰 2026-11-22 [XPENG Is Weighing Its First Ute, and Australia Is a Big Reason Why](https://news.google.com/rss/articles/CBMif0FVX3lxTE5aT1h5SzNlTGZsVDJwcHJPbFE3aDBsQWtNeEFld3RvYTVSWEhGV2REd1R5ZnJrc05ieEQ5N0luQVFKZ2VJaHQweHdwME4ySm80UU1iRnZCT2xsa3NRRWZVbGRRRzllUW5RMTBxYmhRbF85cFFEczdnTGJXeE92Wms?oc=5) <sub>CarSauce</sub>
- 📰 2026-11-21 [The XPENG G9L’s First Right-Hand-Drive Price Is In, and Australia’s Next](https://news.google.com/rss/articles/CBMigAFBVV95cUxNR1BpWXNvRVVjY3R0di1pQ3hMNjV5NkJ0Vjktc25Xdy1CT1FOb251bEtNeFZvWFRzUl9mWWxYakZDVjFJeVNTdDdKZ29UUmUxOUVpelZHN0tFT05vSkVia2I5Tk9YN211WEx5ZDl4OWgxR3JFMW0tYUxBWGpHZEk2NA?oc=5) <sub>CarSauce</sub>
- 📰 2026-11-21 [小鹏行业首发VLA人驾版，AI共驾实现自适应减速](https://news.google.com/rss/articles/CBMic0FVX3lxTE1LWkNXTDBQZFc5LVdmNlJYaGIzVi1leFdfbF9HVVR1Q3NMaTZJbnBnX3lMUzJlNnNGSUNOR0VKYWQ2SnFxeWMtaHAzRjd4V0RIbW1ETFNfaEJuRVZMcGZHR0toa3YtR29XTGRrWFlCXy03WDQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-21 [WeRide Robotaxi Revenue Tops RMB 100M, Up 204%](https://news.google.com/rss/articles/CBMiigFBVV95cUxNVk5SQllVeEx0a0lnanJYUy1WOUtWTWFxY2tNV0pMcWxoYUxJc3dXWU92WXdQMzJxci11ZTFwcEVNYUdUcndsWkZSLUFoVHh1Sy1NSWY4SGVOeGs2MkxwUzctajRncmZJcHRzendzNDNwNlJINi1nbmU5dmRSNmVMbEYtV3BNQ2xPU1E?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-21 [While Tesla Argues With Regulators, Others Push Their Automated Driving Systems Into the Mainstream](https://news.google.com/rss/articles/CBMi3gFBVV95cUxOa3FSZzI4bldWaUwtTlU2ZENRcS02WGN5eGxKWlptV2czTEVNWUcxRUVmYU1VRl9SYWJydWl5cDlaQ1duVjdfaVJyLVpjdS1BT2lLbE55SDVwTHlzWG5fczFnZmxMcEtkMEgtMHJkTkJncHJiNTlNd1lmVWM1Vklib0NxeUdGc3BOVGViNUFtN1U3ZnRiZkZOZTNrS3JaWkdYUlRDMXA4ak5IaGc4bHc1Q3FaNDFMZ05FNmVYc1JnTEpINXRkVFR2NGZrb0s2ZVZ3TEFSMUhRZ1h2bmtGV1E?oc=5) <sub>autoevolution</sub>

</details>

<details><summary><b>Li Auto</b> (183)</summary>

- 📰 2026-11-22 [Automechanika Shanghai showcases smart fleet technology as the Middle East advance commercial transport innovation](https://news.google.com/rss/articles/CBMiiwFBVV95cUxNMzR1YmFBeDJraE5oM1czUEtnWm9QMlJPaVRjX3daNVJjcV9oZTU1WWx1NURYY0s4S0VLcVBkc2pKclpGNE50M28wSEJsaFM1TWpMWEd6V0UxT0JqSnJpUTc1YmthZGhFVWJETnBaRFlRUGQyTHM0NUpCanBUN1VLS2x5R1pRQmx3MGcw?oc=5) <sub>Al-Bawaba</sub>
- 📰 2026-11-22 [2026年四款六座SUV横评：从理想L9到奕境X9，30万级多了个满配新答案](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1xS25kcllQdnYwd2x6NTF1QnJJZlltbExOMkFPNWlLWnVWSDdhSHl2NFdQd2VDYWlvZmZKeWFtQjBUWWlOZTlmcHIwX0JtSVYxMXhWUXdvcThxLVBfNVhJ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-21 [LEPAS L8 PHEV launches in Gulf, offering luxury hybrid SUV with advanced tech and long electric range.](https://news.google.com/rss/articles/CBMinwFBVV95cUxObWk1QW9mQjROaWl1UDRtYm5qeUZFSVlyVDFWdDhXbnJtUThwN2pRaF9hejdFN3hWUGRUUURnYnk4VW02cGF4VWFjRGhwRDlZdU1kMVQ2UG55TTBSQ1M5X0RRS0V6NDIteUpILU9mS1ZWY0FyX3pSMFptanNIRWMtWXhLa3JyUEdEcDFfOENZSkRiVWM0NHZmMC1ZQk9IQ1E?oc=5) <sub>Pluang</sub>
- 📰 2026-11-21 [小米极氪理想拆车，智驾标定与OTA承诺才是软质量](https://news.google.com/rss/articles/CBMia0FVX3lxTE4yeG1BbTRuUUpmajdVYnhNSFNQcDRuM2I4MktaZEJYaVhDRFd3amRfZzJzTUJ4elA4MnJSWVhMSFZJclZXRkZ3MmhZaXBmQ2piOVVKT1hSZVZ4Y2dwNlhUcnhNajJsRDVIVmpJ?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-21 [高配置增程SUV怎么选？奕境X9、问界M8增程版、理想L9、领克900四车横评，入门即超配才是2026年的答案](https://news.google.com/rss/articles/CBMiX0FVX3lxTFB2clZkUThjT2Q5U3ltUk9wZlQ3Rl9KNXZZSWlLRVAzYkZGczBub1kyWXF0dWVucXZMZjRZSjJlMk5MYXBzWTFnQzFDZUdqbWRyYVZSOXdKYTB2bjdyTXk4?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>NIO</b> (186)</summary>

- 📰 2026-11-22 [Nio Firefly debuts Haven special edition in Oslo, plans spring 2027 launch in Europe](https://news.google.com/rss/articles/CBMinAFBVV95cUxNenFKVkNaZ3diUWY0MEI5SzdsMUlTQ19sTy1YYWFBdVFkWE1scm4yNXFwb01od29OSFNVUHNOeXpma3FvNmhoSm02N0s4Sk5aZVYwcDlrRXlRWWF4WnVjNi10WUVrUktSVS1vSDgybnR4M3NXazE2b0hUV2UyUGdwejZyNXhycDQzMWtXcWdZNHJjbW8yTzhyeVJjMWo?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-22 [Dutch court bars EU sales of BYD Ti7, citing infringement of Land Rover Defender design rights](https://news.google.com/rss/articles/CBMimAFBVV95cUxPQmhlbzgybVc4OWlPcGJjZ3NrMUhpVDRCeUZiY3V1LVlnUzNjWDdtTS1Ta191UUhZclU2ekdSc2RtM2FtNWo0ZFE1bUFCdXE1LXJwMy02eVFNcGxrYUFZZVptY2psSVh6RVd1dlUtOGpaRGttX3FGSkRmY3ZaYkFDM0hsUXJtTDJDUGlRcGJLRzVGUDJUT2dTag?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-22 [【视频】蔚来EC6 2020款430KM运动版买断版](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5HMndBRVhTZHFSSkpicXYwMXFtWkNUd2FFWGhXZ1dTT0xXUk5kb05HSWJ1clN3QUxFMGFYVTZ5OFVYTHJ1Szk1MWstdUVzMXBmRExGeTVaZzc0djg?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-22 [【视频】2024年蔚来es8](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5ITXpJeE02eExoVXhuQlhLMUZWbVRfQXRNTlk3QzdYM3Rjd2FRa1dOUDdFb0IxVV9QT2NYdGlDMHRDY2NhWk50bFMwMXAxdUJWeWo2dlM3ejlQcms?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-22 [50万预算带娃长途，ES9换电和M9充电的差距有多大？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5zRzhGOVN5MVpzRDVDb0VwT0NUU0IyOGxNemV0SVZIZUoxcmtibm1NYW9GQkpoRTRsS240S0VLMmlQbWJ5TUx1ZXVvdWk0dlNWOVVkMW43OHUyblk?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Huawei</b> (337)</summary>

- 📰 2026-11-22 [China unveils a 7-seat electric luxury minivan with up to 910 miles of range](https://news.google.com/rss/articles/CBMitwFBVV95cUxNZEdleWcyNmRVVDNjQXExa1UwNWhSQ2JaWnliVGoxTG42RUptRndscHVsNHN5WDlzc2xxMkg1MjVsX2dGa1REWEVTREh0ODdJdnBrVmdMdC1vWlREU3hrSFlCRHppWXJmZVVIVFpGWFpFUk1rYUk4QUFqUy1tR3JodzdPYXcxYXJiWjE3VFU3LWNCTFRzNFJQaWZ1S1p6b2R0eDdzTk9tbkhWYUxFV2pwY2Z3S1ZLSzA?oc=5) <sub>Interesting Engineering</sub>
- 📰 2026-11-22 [WATCH: China EV Attempts To Park Itself 868 Times Overnight, Refuses To Give Up As Owner Sleeps; Internet Says ' Respect The Dedication'](https://news.google.com/rss/articles/CBMijwJBVV95cUxQU0duNTRBVWlzUnZERVlMY3o1N1IwRV8xRVFiUlc5RXFfSWxkTEFqZWdtWXBabWxOYUFrRkxqUndCZDZfYnRpenctUTA2TUt5VXBFMjd1d1RUdWJFblZSRUlHRThoOGdHTzhScFRKdVZzY1dPZjA5cGUweG5sNmdZU2RJQ2ZaRWY4bEFFd2FqdVkwLTNkZDJwOXAtaVNGcERVcEc0N011NU53TktTTWxmd0ZpTU81UUlKU3dvZHdJbHNYcm9KcURzYUFaSWFFUm5zUnpfR1hKYVB0WDFJdEZCRE1XMDJxRmJ5U1Zma2Ftd0UxMTMzTVV6b0JVbFJjRVh6NFQ1Z3cxdVZqQS04b01R?oc=5) <sub>The Sunday Guardian</sub>
- 📰 2026-11-22 [【视频】13万起配华为智驾？探店阿尔法T7](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1jbzdHVkYxR1lZMlNYY0NWR2lSV0FJTkt4bVF1LWFVTlgyWms5QXB2YzlYS084bXpsV1Y3a0lRTGtteGJ5WUxOZzBEWERkT0hPMHl6VFFYRXV2QlU?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-22 [智驾硬件、座舱AI与底盘智控，四款三十万级增程大六座横向评测](https://news.google.com/rss/articles/CBMikgFBVV95cUxQWTd3aW1ET3M2b1Nla2xCQlYwRnA0M3V0Z3Qwb0VEVndMdmZxMGVaaWsyb01ULXFuLXJrYVE5U1h6UjI4dVZZajZ5MnhHTmpnUld2eTROVE04bGxuUk0tRk5WVGdUcDhydmM4Nlg5S1NTRDI3SmhzdXlRWGc1czF0Y0RPVXF6MUU3eHdoVFMtTnVnUQ?oc=5) <sub>新浪财经</sub>
- 📰 2026-11-22 [预售高喊有几千订单，落地月销仅68台，这车真“凉”了？](https://news.google.com/rss/articles/CBMiW0FVX3lxTFA0T0d4aTA1V0Rmd0Fsa0ZiT1QyX0ZGWVU2NHBJVUFVdkVCZlVaTmE3bFRQRHhYZ3Q2UjVTUmlXNU54Zld6YzVtSUh6TUNweEQ1TEtlT3pueVlodG8?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Baidu Apollo</b> (58)</summary>

- 📰 2026-11-22 [中国公司全球化周报｜阿里国际站前两季度GMV增速均超20% / 镁伽科技获近2亿美元融资-36氪](https://news.google.com/rss/articles/CBMiT0FVX3lxTFBsQTVqMHlBdmNaQkZ4TXQ2VTBSNklrbWhsekU3VFQ4TFhnQm1rNkFiT3YxTDVpUE50bmJQVHVKalVHSXFQeDhaUGFpV1V1Rk0?oc=5) <sub>36kr</sub>
- 📰 2026-11-21 [百度世界2026发布多项AI成果，李彦宏：AI下一幕是“智能组织”](https://news.google.com/rss/articles/CBMidEFVX3lxTFB2QXdyQXJBd0xyTDBIeENlSDVSN0htT1haRWU0NEprc3ZBYlJPTU54ejlFVjBwZUpzc004aGdMYW42NzFrM3V3LVBsX3Z5ZlRXQWNzb0lkd20tdTJuVmR3V2otWHo4NXRrTi1aYVluaXBEVmg1?oc=5) <sub>风闻</sub>
- 📰 2026-11-21 [APEC期间深圳街头无人车驶入全球30座城市](https://news.google.com/rss/articles/CBMigAFBVV95cUxOLS16MmVLY29WTFBTSFpwWk1xa0NDYlZvOW1UY3hZelZlSHZQNkpPM3hWVENURllxNTdSRk1OUEFLZmpxZHhYQ3FCSVpnN2h0QTdnUjYteGRRYWtFVmZOSTZ2ZnlaelQ3cE9JQ1JSMnFWS1lJazhmT05ORWNuOHZ6cA?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-20 [Google 开放 Genie4世界模型 API，支持实时交互与原生音频生成](https://news.google.com/rss/articles/CBMiTkFVX3lxTE9sLURMU3dDZHJRN0N0U25LV19oWlBvTThkQVI5TzNCVnBHYlFkNUREbzJxYXBnWVV0SHQ2WGRpQUViM0ZKbXpIdUw0Y0dZQQ?oc=5) <sub>AIBase</sub>
- 📰 2026-11-20 [边玩边改的世界：谷歌 Genie 4 向开发者开放，一分钟约 6 美元](https://news.google.com/rss/articles/CBMiTkFVX3lxTE5NYnUzSE5kS20yVDJXRC1iZWEwcnhTaVlfRGt4MEFfOFhUZjJ2YmEtUFFrcElvc3hyVFZtQk1rY1liNFBMSTNQRjBJMWhLQQ?oc=5) <sub>AIBase</sub>

</details>

<details><summary><b>Pony.ai</b> (144)</summary>

- 📰 2026-11-22 [Tesla Cybercab Orders Open: $29,990, 2027 Push Unproven](https://news.google.com/rss/articles/CBMikwFBVV95cUxQZUVWZXdCQkhLNFVuWHZ4T19oUV9GVDFyZ012bHBHbDBJbWNxX0cwdzY0Z3ZlLUhyTWJ6RHpJQ3hTbzRwQTJ5YU1LRnhwNm1QcjhldjNHZnFpV0I1bC1BU2RMRTJNbWpoelp3NGl5XzJ5WVJ4Ulo1dkVOWmdFd0tvbXJoV3BweGJVN0cyOENDbDJEc2s?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-21 [WeRide Robotaxi Revenue Tops RMB 100M, Up 204%](https://news.google.com/rss/articles/CBMiigFBVV95cUxNVk5SQllVeEx0a0lnanJYUy1WOUtWTWFxY2tNV0pMcWxoYUxJc3dXWU92WXdQMzJxci11ZTFwcEVNYUdUcndsWkZSLUFoVHh1Sy1NSWY4SGVOeGs2MkxwUzctajRncmZJcHRzendzNDNwNlJINi1nbmU5dmRSNmVMbEYtV3BNQ2xPU1E?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-21 [Amid US-China tech rivalry, S’pore wants to be open to both: PM Wong](https://news.google.com/rss/articles/CBMiygFBVV95cUxQOWM2QVNGb2Y5MGw5WGtFQmxBMDhINGFaVmRndTRQUkhObk9QcHRfNHQyZms1dzFUUDBpWFR5MnBPZy1MZUJFcDNOV1ZXTjZYMGtxbDdPOUZSaUt6Z1lFWndrdDdhM1dZUVkxbjhkN2xMVEhmMTY2dklSVEJqWlowcjlHdUtReldRY3ZlRUlLSG9KbVNBMHVZUERVaG1YSVFzYTNRLUNPSVpGcFlnanVrYzhOdnFvSWhOWFBXSmRtbnh1M09iazVlWkRn?oc=5) <sub>The Straits Times</sub>
- 📰 2026-11-21 [文远知行Robotaxi 第三季营收首破1亿人民币](https://news.google.com/rss/articles/CBMiY0FVX3lxTFBKR0ExcmFhRjFPRktiYnRyS3huS0NuTS1jdmU0VXBVTGFoSklJWmdWbTlva1JBZUFVSkZEbXRwWlZaTHpfNUdSZnJKaTF3QnZES1R6aEcxc1M4ODg0UWlZWnRiWQ?oc=5) <sub>e南洋</sub>
- 📰 2026-11-20 [Pony AI’s robotaxi fares surge nearly 400% but its operating losses barely budge](https://news.google.com/rss/articles/CBMipgFBVV95cUxQejkzT3hlZnI4SG9LdWVCc0FKMF91cW1TWVBTNlJ5enRQOUxMOEFzTUg1STVDRHpOVTBpanlFNHgzd3RzN3ZDLTRaNV83azIxVEZTR09FWGx0OF9rWVR1bFlod050WlRzWTY2TVd4cHRQeGNrVklWcWNtUlV3QlZyYzB4WEZSZGtRd0pvWDlDU2kxTVB4Q3FYN1ZpeXlmeXVWZmRpOUFn?oc=5) <sub>CryptoSlate</sub>

</details>

<details><summary><b>WeRide</b> (132)</summary>

- 📰 2026-11-21 [单季营收3.2亿元创历史新高、大超市场预期：文远知行增长确定性持续释放](https://news.google.com/rss/articles/CBMiiAFBVV95cUxOVlVCZV8wbEFQNGJQOXZSSXNxeUxlbkFNMHZZUHhEQmZ3WHMwTkZNOGN0U3B3UzNXU3RBd2swVFotdWdIbUFYVGZxVU9QaXNaVV9IZ0ZpMFdmbVVfSEV2aDJTTElhcW1OQWNVOWtBbXFXdmtPSkNuX05PY2JMRlY4VkNwblRPWDll?oc=5) <sub>Sohu</sub>
- 📰 2026-11-21 [文远知行全球Robotaxi第三季营收首次突破1亿人民币](https://news.google.com/rss/articles/CBMia0FVX3lxTE1ROVRINE9GdV9KSENISmhMUXNkX2hFbGo3QXdKajQ4bHFqaGlUck1FWXBwYmM1azBDQnVRdWd4VGJuZDVXM0tvTjJWa0JBUkNsdXZLSFhEUjQ3MTgxWmtlOFlMMmVKSVRLb3pN?oc=5) <sub>联合早报</sub>
- 📰 2026-11-21 [11万级后驱激光雷达搭载文远知行L4同源辅助驾驶](https://news.google.com/rss/articles/CBMickFVX3lxTFB5ZWRUSmtLTmFFV2pUZEIwaEtfODJ3SEhRWGRHdzJ3ZzE3RWZ1RERhRXBZRkZSOUM0SHZ0RTUtUk9od2pyUXdyMTF4RjQxYUdudFVqem5vaFBUWktzSXVWWnVVMHc1LTM1TXhBN1YtNnk1dw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-21 [WeRide Robotaxi Revenue Tops RMB 100M, Up 204%](https://news.google.com/rss/articles/CBMiigFBVV95cUxNVk5SQllVeEx0a0lnanJYUy1WOUtWTWFxY2tNV0pMcWxoYUxJc3dXWU92WXdQMzJxci11ZTFwcEVNYUdUcndsWkZSLUFoVHh1Sy1NSWY4SGVOeGs2MkxwUzctajRncmZJcHRzendzNDNwNlJINi1nbmU5dmRSNmVMbEYtV3BNQ2xPU1E?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-21 [WeRide’s global robotaxi revenue tops 100 million yuan for first time in third quarter](https://news.google.com/rss/articles/CBMiugFBVV95cUxNaXVUV0VvcVIwcF9mTFFLdjM0eUdiVld0SVJ0ZWRIbF9KTmJLeFRJekQxbTQwMkFGSG8zSW5HZW9tTEhKSlo5WVQwcWNZRFNQX2g1bzdnOWs0ejhYNEk1S3R1cVNJdy1GQlNoX1pmVkw5OVZKMEVKYXRCekxiTVJmYzhTdUtuMGRIR2hwZnNqWFFEZ3RQVkNyT0dDQ1lyVTZrSFhGTGZnMkpzWFBHVVFkbUQzZ3FiZWQ1WlE?oc=5) <sub>联合早报</sub>

</details>

<details><summary><b>Horizon Robotics</b> (120)</summary>

- 💻 2026-11-19 [HorizonRobotics/LoFT](https://github.com/HorizonRobotics/LoFT) <sub>GitHub</sub>
- 📰 2026-11-22 [捷达M6混动值得买吗？7.98万起19小时锁单破万，3个维度说透+FAQ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPUGJjZTZSYzkxenUzbnR6ellQMnlrRHl5bEx0NDdfLWZmVUR0by15cTljSjFzRU9mcTdLVTVwVzgyaG9vVFhyT2VtLXMyZTRUUUxlbkJmcTVYcFhPNzBIQ3MzakJUMENWNW5ETHpSY3Zac2EyUmtnRmtySTllUXBJd2NGQnV6cUcxRF9QdE1hSC1oZw?oc=5) <sub>新浪财经</sub>
- 📰 2026-11-21 [蔚来ES9地平线鎏金特别版上市24K鎏金车标](https://news.google.com/rss/articles/CBMiTEFVX3lxTFBhTTdRUkhBSlZFcFBqenRsQkc1VEZVNUw2UVRFbkdVNk9DaktyTHFtX1R1djF5djdVSVJpQXdwbVYyNFFvYkxSRWx0eko?oc=5) <sub>www.itsdw.cn</sub>
- 📰 2026-11-21 [蔚来ES9地平线鎏金版上市，BaaS方案53万元起售](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9Ic2ZiUHoxaXplYUpuLUV0N0trWU9FRk16bDlMWjhhZVdydjd0V0lDNVBJbXoyMzJGdUtJS01MWmRJa3dGMmpLb2lrbkFnSy1pM21ybjJIVm9CMGc?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-21 [捷达M6智驾靠谱吗？7.98万起配地平线城区NOA，3个维度说清+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE1Yd2dxeW9hWjJQUmtxRTYzNWt5ZlJGdENRdGw5ZXhqUlBkaHdlWlRWUkpvdk5QOHZRaEJySkktaWkwanc2SkNxd2owc0Z5WjMtZi1CMmVUVFJYNlZSRmdsYUFBZ2hFVFdaam5XSGVyUHAzUQ?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (21)</summary>

- 📰 2026-11-21 [【视频】3分钟看懂特斯拉Model Y L值不值得买？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9VQU9UWDByVEt0TnRIcDk0Q2RQTDBzWU9JRTBqMUtKMUgwTGsxNWNTc3k4OV8wQ0hfUkh3R0oxYm51S1ZRSzJLRlR6NTU2XzFhMTVRMG9MNlRCSVk?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-21 [购彩大厅～welcome手机购彩公司的校园体验报告：不拼参数，拼场景与协同](https://news.google.com/rss/articles/CBMiT0FVX3lxTFA5R0pUNmlUbUtPNW1KR19EdDlnd3FocHQ2UnZHdUM3Q0t5WkJod1B6emt0bFg4YnhsdUhWYUk5M2t4WVZlVW91TUYzS1plZ1k?oc=5) <sub>iheima</sub>
- 📰 2026-11-16 [中国智驾出海新突破！元戎启行交付超10万辆](https://news.google.com/rss/articles/CBMiW0FVX3lxTE80eWh5OVZNRlpOY3ZTN1hMeHlsN1NtbldkODZOVTQ5U3hMVXBrOXZ3RnhWUXA5eXdsNTVYbUlDUnNsNEhnX05Jam9VUUhDZkJ5RmtIb3RJX1IxQ0k?oc=5) <sub>车家号</sub>
- 📰 2026-11-16 [又一“国产保时捷”？赛豆ME7实车到店，大过小米YU7配571马力](https://news.google.com/rss/articles/CBMia0FVX3lxTE5fWTNxTkVfa2RHM29CZ3JabmtSbllKTVdGN2x4aVpqS0U0bG81RTFHeDhqNHZhaUg3MGJFVjEzOVU3aDdIMS1zR05mNXZ0blNyZ3cxVWRnVF85bmc3Tl9aenNZSlpDaWRDSV9n?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-16 [AIVA ME7实车到店剑指25万级轿跑SUV市场](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5fM1B6RnpLTlpiVEtIUmJaR0Ffci1BVVpqTzY0ZnBab3JSZ2luNDRWeEhPeHJ6YXlaek9BRDZvdmU0TEw3d2JXTVdMbHgzLXh3TWhLTmpCTDlvdw?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Mobileye</b> (12)</summary>

- 📰 2026-11-21 [3 Penny Stocks With Revenue Growth Up To 56%](https://news.google.com/rss/articles/CBMimgFBVV95cUxQNThVYk1RYkI1YkNMVi1JN2FWaG5fdjFHNVZ6bEVBNktGSURBeEd3NHh2dEVmSk5HRXdzRHdLd1NsdU5vLWJfTzBhaHVvWmw5SGZPandLZUpqc1NreFkwdUlRRllqOHpEcmVXRHJpZU1fSnhGdjNlblgzU2ZoXzh5RFNnNDlqVEFNd0R6TFJ4MjNEdkNORHUxaUZ3?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-11-19 [Growth in the Adaptive Cruise Control and Blind Spot Detection](https://news.google.com/rss/articles/CBMinwFBVV95cUxPa0x3SFRDX194b3VtTHJnYlJPNEZzRHNpRHd6RS1JOVVkWnBBMnZxQ1AyRjFpUWdVSDBuZHdVdUdFczFGbUVMSFlhdU41UmYwbmhzdFlDaGhvSmptUzNSYzktbGJpRG96ZmZvQ2ZHY3Z3aUt6aWV4WFJzLXctV2k5dFoxVTlta3YzSmNkZGxBRmxYdnlLQ1JKV0RFOWxVcjQ?oc=5) <sub>openPR.com</sub>
- 📰 2026-11-18 [Intel Cuts IT Jobs as Tan's Cost Drive Extends Into Year-End](https://news.google.com/rss/articles/CBMidkFVX3lxTE9XMEIyWkJScF9ld3AzQXYxN0hhaFJQWnJ3czJVOE9FelQtbG12YUdoWkZmZW55cWdQamJlSnRGQTF4bWVDNi0zRFdfZ0hpVkJFNThWdmYtWDk4WGRBY1F5dWFrRklNQjNLUU1UVUQzakRvUFZhYUE?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-16 [When Human Superstars Shine: 9 Unmissable Historical Snippets Between Elon Musk and Jensen Huang](https://news.google.com/rss/articles/CBMiU0FVX3lxTFBjclJYNXBJbVBjYUxUQkJCU2pOcDBpVnZZZ2lqWDhZY3lzYk1udjlFWGxNS3loQjAtUDdKYXJySWZWZTJLQ1I1UGtueDdvd2E2RGdJ?oc=5) <sub>eu.36kr.com</sub>
- 📰 2026-11-14 [May Mobility plans 10,000 ID. Buzz robotaxis on €9 million revenue](https://news.google.com/rss/articles/CBMihwFBVV95cUxQdkgzeUVTSS1wc1czVWhUTllrV1ZaVk1VLUUtUTVhTlFVSnJVSGFvcmtvRC1QZHNnWUxHY1B6c3gtUjZqdzFRSm9CSTNuZENtdFlRZGpoaDZGalJQb2xmZ1UtMGJyX1JObkdfaVF6SThudG9kajdDaW1xZVY4dzFraUF6NXd5RVk?oc=5) <sub>AutoNext.co</sub>

</details>

<details><summary><b>Aurora</b> (39)</summary>

- 📰 2026-11-21 [Bot Auto launches ‘Capacity Grid’ with agreements for 200 million miles of driverless trucking](https://news.google.com/rss/articles/CBMi4wFBVV95cUxNenB0d0xhRHB1QW96VjM5dl9yODU5THZxLWtmZEZ1WEc0TGZhQUlDOU1CdlNiR0Flc3ZoTzAyUnVoaEtOSUp4NEVyNXpqVi1vZldPNUY5VXRKUU5hc2xjVm9aZDdiN3R3NE9mUmVtajF0dG1hM1dFTmtJWWVwakMzQ095TjMxZU81VThwYy15T1FaaTJNN3ZEc1BxcDhCX2xjMDdHQ1pxRVNNaWloSUdTUmxkRkt2TUxNdGd4MTNEU082RnBxcUtxV2paVWFEeEJ0Z2t1SWJONG1jTDZIanM0N1QxNA?oc=5) <sub>Robotics & Automation News</sub>
- 📰 2026-11-21 [NADAQ: AUR Investigation Alert: Kessler Topaz Meltzer & Check, LL](https://news.google.com/rss/articles/CBMisgFBVV95cUxOcUdtQkRtc2tPZkc3dTlWUnJ5YjVRZ2xBV3d2RWxTUFU3QmZPV200dlROY3N1R3Q1S2t6dHItRVQxUU1YNFhzOFNtVzVCWEtxVDM4V2FBblhFTE1oTGo1NWhxUTh4SXFEWXVfZmphc1RNaHJVa1ozMGRfYlZoaUtxUlY1b3FONmZmS3hkLTZjNjZHTWtUalM0OHlRQ2hRa1QxRS1WQkd4eHRYWDlzb213amFB?oc=5) <sub>The National Law Review</sub>
- 📰 2026-11-20 [AUR Investors: BFA Law Notifies Aurora Investors with Losses of its Ongoing Securities Fraud Investigation](https://news.google.com/rss/articles/CBMiiAJBVV95cUxQVFAwZ0VhZEh6UWFhWXV0RXdxNk1GV3V1ZEpGeUh4cG5tc2Z6aWxVM0hvMUFtUlhTXzdkTENzU3U0S2ZsTC1OZmVlVDNXdS11WWF0VzJUeFBZcnR6NmYzd1JNZ25HLWo5TE1yNmd5TXo4NFlxRTRFSFdSQW1Ka0h3b0JZd2h1LUY2LUxwbWtXX0U2NFh5QmxPNzBDOHIzRG5yQ3J4cVl5T1JxV05SaG5qYWZxekpYbVd0Mk1GdHpmREplRlNpVE5Eb0VpUnQ2b05TdXhLdjhKeEh1Z214VWN6Nmd3WHRFd1lyYVFhQ0ZicXYzdVY0b3owNmRpTHlycHlLU1ZGRl9UcUM?oc=5) <sub>GlobeNewswire</sub>
- 📰 2026-11-20 [AUR Investigation Reminder: Kessler Topaz Meltzer & Check,](https://news.google.com/rss/articles/CBMiowJBVV95cUxOazBaMjVSWHZESFowVURkVVg1NURsOVhELWtUYjlWM0ZMZGIxNVNXeUtsMk5USFFQemRXcUdObEdUQjBUTjhwNnJvZVNzNmRERHRsOFViVFJ5NGtNdnVvLWF4emk1MXJyZ3F1LUFqOWk2d2pjN3JlOWVQdGdoWFhUM2ZOQ2xja3d3d19rZFZGdHd2TWZpQngxUTYta2FJVWo0RlBuYjFOUXplSGpqNkxEcjZyRlFZNmMtWDNreHF1d2ZMb0xxNGJlT2lDcVFnMHg3Y1Izb2hNcVh0NFRmYTBIcUt2Z08zWWdkTlJwSlpnTHR2SEJDdWNUeFUwY0RGUWw0c1E4aVVVdkowUjRVektKT3NPMTc5Y2pRRkhXdUdLbXBNZG8?oc=5) <sub>GlobeNewswire</sub>
- 📰 2026-11-20 [Elite Penny Stocks To Watch In November 2026](https://news.google.com/rss/articles/CBMiigFBVV95cUxNajdPRWw0a0VnR1ZtU1l6ZnMxT0tTNERicGw1cGpYdDJBVUE0UW9UZkJ2VnpkeXpzODJEamNwa0FNNWctUlZicFVUYmJtWnBzMGRRWkZ5MXNwY1U3WEZJX2NKdFd2ZEpzSHNZRUpPa3ZsdVozUVpmcXIyNU9FcGx0c0xtU21Mb2R3dEE?oc=5) <sub>Yahoo Finance UK</sub>

</details>

<details><summary><b>Zoox</b> (109)</summary>

- 📰 2026-11-21 [Waymo announces two robotaxi recalls as closed-lane software fix remains unfinished](https://news.google.com/rss/articles/CBMiwgFBVV95cUxNXzk3UHRGSjRZdU15TC1mNm9NLWxxNVg4LWFtZUdReTlENWszWmxCLTFEMzd1Z29RNkpEcFprd3NjTTROUkhPSkhsdkhCWEQ5azJVakdxeGhiTUNxalVTTnhZM1ZyallJMEZ1akdYZ0FFVDFQUWl3a0FSMWx0czV4cGg5TnFUREgyaG9BX0FybTRWY2lfaE1GRlVibVRUNUZ3RHJVUC1jbTdWWDdhZVY1dUlfWGpDMVJqYjJKaENENVZZQQ?oc=5) <sub>Business Upturn</sub>
- 📰 2026-11-21 [Zoox launches its first robotaxi rides in L.A. County](https://news.google.com/rss/articles/CBMiowFBVV95cUxQeVpseUpWdjdRQjZ4YUUtaUNRdzB3ell5ck9zNHZWYVAxc3BKdVFMS1l0WkcyVXY4Q0d5a1M1dUJZYllxNkNTalppWVBNQURLN284ZVNraW9RU0ZNWnlQVFBGc3BpaVR1N3VjOWNDdGRTZ2ZYRVdtTXJteUlqTUthLXhOMVNwXzNKay1YNkR0aDNYYzFEVGZXY2szeDVEWjJhSXFr?oc=5) <sub>Los Angeles Times</sub>
- 📰 2026-11-21 [Celebrities at F1 Las Vegas Grand Prix 2026: See all the stars](https://news.google.com/rss/articles/CBMi2AFBVV95cUxPYU1mVGVuQzZHUHltY09Hc0xRRUhNRldrMnIzSlE3OHRNUXh5UlUyTEtxUWw2eW9YZ2lFVHRrYWN3aXBWaU1kbW9GckNWTWNVLXBYWVl6dUtsYTBNNWRCUFRmYXRSWUFtNG9sTlZFVDdNXzNvWnlRWEZNVkx6Q29XTTBENjY2Z3RZSGItRGtGUG5PdGxoTGJ6NV9OUTVSRVZMX3JnRHJwSDNxaXZyNUZscUZnWDNxbzNRZWVpLXlXZGpwTE90cGZVUEgtcVVobW1VcFhqV2g2cU8?oc=5) <sub>Page Six</sub>
- 📰 2026-11-21 [Zoox Launches Robotaxi Rides for Employees](https://news.google.com/rss/articles/CBMiogFBVV95cUxQYm4yZnUtR09RSTNvX285QXlVOFlzbGNYRDY0Sm4zemVGakJUcDhtQmhMdWxFNXBPUHpFak43MzhtX0ZidXl2TkRyendFRzFXemctR25fNk1uRnhVc1lTbGJabG1nX1ZLUU9ZclhEd3lPUUlqakw1QW5ZRHVra1J6ZnJrNVZYMVhnQU1xUk4yeU81MTI2b3pnYkVCNlpBT3NoS2c?oc=5) <sub>Wisevoter</sub>
- 📰 2026-11-20 [Where to see F1 cars free in Las Vegas](https://news.google.com/rss/articles/CBMifEFVX3lxTE5rRVNoemlmQWJJMDZfN21ZYndpZENfNHNHbUE2Q2RuaVdCWThIbnMyZUlFTmdaZkhPdld6VGVzeUtzTlF0c2l5elZqTktkb1FJeGpFX2VNalRidzJfWjM4X2FaQ1B1YVY3SzRnSm0yc1g2c25HelNZMi1fMUU?oc=5) <sub>streamlinefeed.co.ke</sub>

</details>

<details><summary><b>Motional</b> (30)</summary>

- 📰 2026-11-19 [[Why&Next] Supplying Vehicles to Waymo, Investing in Motional... Hyundai Motor's "Two-Track" Bet](https://news.google.com/rss/articles/CBMiZEFVX3lxTE1fcTNiSzhBMzRuMGl2M0FtOTQyYmY5TDR0d3BoRmJ0RXdMYUVnLVlVRUdGYnh2QkFwUFpYdmM4MzhZc3h6a2prSERaU1hNQ2FQOWJzM1pNNnlRU3UwTkV6VjJqOHg?oc=5) <sub>아시아경제</sub>
- 📰 2026-11-19 [Hyundai Motor Company: “Data Flywheel Gap to Widen in 3–4 Years”... Four Group Companies Put 'Data Union' Into Operation](https://news.google.com/rss/articles/CBMiWEFVX3lxTE1KekR0TXpjWmRySUVDc3pyQWw2ZHFIQXhsZV81VzJNYzRxbHVQZDkwNjMxSHZWNlV5d2pBVFFrUERGM3NKZnE1Qnp5SHpSbDJ4UUFVaV9zLUE?oc=5) <sub>파이낸셜뉴스</sub>
- 📰 2026-11-18 [Hyundai Motor Ramps Up Robot Hiring; Muñoz Says "Physical AI Is Our Bet"](https://news.google.com/rss/articles/CBMidkFVX3lxTE5pTkR0WnlGS2hSdDY0Qm05SmV2S3BVMnRiTmh2blBKbHRTOC1HMjhKaE9QY3pqdVdJZlhGcWdJU3JtZW5Ddllua0dYazFPeTJLbVl4QkVfOXp0czRSRnZXUTZzdDUzSlZDck1ON3dNSGdKdFpaWVE?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-18 [Hyundai to Supply Ioniq 5 to Waymo, Expands Robotaxi Push](https://news.google.com/rss/articles/CBMiYkFVX3lxTE1YSzRfd1k1SE1SWGdMNUtMMmxhbzZmYm1QSVA4aXEtWTF3bi05bmk0cVJKOTVZeG1rMkd6dnN3RVlvaUtRNy1OOGZBdkxETENBVjhqcGJtd0gyamVTWFUxV2ZB?oc=5) <sub>동아비즈니스리뷰</sub>
- 📰 2026-11-18 [Hyundai's Muñoz: "Nvidia Partnership Is Unshaken… Ioniq 5 Deliveries to Waymo Begin"](https://news.google.com/rss/articles/CBMidkFVX3lxTE1GbVF0M3dXQWhSdHVQMThlRGtPVlY1eE9ibndWMkR1Y0hqX2xJajJYTlloVzYzXy05Y0ZyWHMyZzhXNG9yTHpJM1RmU0dEY0o5b2lpaFhRU1pxbHc1UklnWVdjbndady1NYlJCaTd6RXVZSVhlQWc?oc=5) <sub>BigGo Finance</sub>

</details>

<details><summary><b>comma.ai</b> (1)</summary>

- 📰 2026-11-12 [Goodbye, BlueCruise! We Install a comma four in Our F-150 Lightning](https://news.google.com/rss/articles/CBMirwFBVV95cUxPY1o5ekZ4WnpraUxVMHV6OVdyMEtEbjQxQXY5STdJdXlHNlN6eUFZNzFwSnA5cFhHd3pNdTZNNy03dXBOZ1ZoX3RFX2E5V2JNTE9aVlhJaG90bW5YWEdzX2NGXzd3VFZ6NG5JVkFrM3daTmY4UDBTN1I4NWU3eGJqUm9tY1VaRWxoZkp3WDJLNnVLQjN5WG9NMzlxLWI0aVU2TFhLUEZwUE5YUDdUcWFJ?oc=5) <sub>Transport Evolved</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
