# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-11-25 · 1,323 papers tracked · 49 curated.

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
- [End-to-End Driving & Planning](#end-to-end-driving--planning) (13)
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
| [SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving](https://arxiv.org/abs/2610.20609)<br><sub>Shaoyuan Xie, Zihan Zhang, Jingxuan Wang et al.</sub> | CoRL 2026<br>2026-10<br>📑 1 | [⭐ 37](https://github.com/ASGuard-UCI/safedrive-vla) | Vision-Language-Action (VLA) models are gaining attention in autonomous driving, inheriting commonsense priors from large language models (LLMs) and widening the navigation interface from a fixed command set to free-form… |
| [AutoVLA-D: Learn a Trajectory-Geometric Condition from Reasoning for Autonomous Driving VLA](https://arxiv.org/abs/2611.12382)<br><sub>Yuguang Yang, Zhewen Tan, Canyu Chen et al.</sub> | NeurIPS 2026<br>2026-11 | [⭐ 45](https://github.com/ShivaTeam/AutoVLA-D) | Autoregressive VLA planning usually predicts continuous trajectories as the final output, but driving instructions often describe actions rather than ego states, which weakens direct conditioning on the final continuous … |
| [Scene-Adaptive VLA: Efficient Autonomous Driving via Dynamic Layer Routing](https://arxiv.org/abs/2610.24590)<br><sub>Yujia Yang, Quan Yuan, Jiawei Fan et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 5](https://github.com/yang-luvu/Scene-Adaptive-VLA) | Vision-Language-Action (VLA) models offer a promising paradigm for autonomous driving |
| [Locating and Repairing Domain Shift in VLM Trajectory Planning](https://arxiv.org/abs/2611.10720)<br><sub>Zhihong Cui, Hengyu Liu, Michael Alexander Riegler et al.</sub> | NeurIPS 2026<br>2026-11 | [⭐ 0](https://github.com/ZhihongCui/MoLaRx) | Vision-Language Models (VLMs) are increasingly adopted as end-to-end driving planners, yet they suffer from cross-city domain shift |
| [CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving](https://arxiv.org/abs/2607.04179)<br><sub>Zhaohong Liu, Hao Ye, Xianlin Zhang et al.</sub> | ECCV 2026<br>2026-07<br>📑 3 | [⭐ 1](https://github.com/MICLAB-BUPT/CritiqueDriveVLM) | End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving |
| [PixelPilot: Scalable Vision-Language-Action Models for End-to-End Autonomous Driving](https://arxiv.org/abs/2607.04637)<br><sub>Pin Tang, Guoqing Wang, Xiangxuan Ren et al.</sub> | ECCV 2026<br>2026-07<br>📑 1 | [⭐ 3](https://github.com/VISION-SJTU/PixelPilot) | Vision-Language-Action Models (VLAs), which leverage the advanced reasoning capabilities of Vision-Language Models (VLMs), show promising generalization in complex autonomous driving scenarios |
| [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)<br><sub>Nan Yang, Zhanwen Liu, Linfeng Zhang et al.</sub> | ECCV 2026<br>2026-06<br>📑 1 | [⭐ 11](https://github.com/Zizzzzzzz/MVPruner) | Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings |
| [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)<br><sub>Yuan Gao, Wenting Miao, Mattia Piccinini et al.</sub> | IROS<br>2026-07<br>📑 1 | [⭐ 34](https://github.com/TUM-AVS/Chat2scenic) | Validating autonomous driving systems requires diverse, regulation-compliant test scenarios |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 25 | [⭐ 563](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
| [GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives](https://arxiv.org/abs/2609.39601)<br><sub>Qize Yu, Lianrui Fan, Boyu Chen et al.</sub> | arXiv<br>2026-09<br>📑 5 | [⭐ 444](https://github.com/groundingpi/GroundingPI) | Precise grounding matters |
| [GRAVA: Grounded Reasoning-to-Action Representation and Learning for Autonomous Driving](https://arxiv.org/abs/2609.15169)<br><sub>Xiao Liu, Haoyu Li, Jianghao Leng et al.</sub> | arXiv<br>2026-09 | [⭐ 488](https://github.com/AhernResearch/grava) | Driving vision-language-action (VLA) models increasingly reason before acting, but their intermediate reasoning is often weakly grounded in physical scene evidence and loosely connected to executable behavior |
| [Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air](https://arxiv.org/abs/2605.31066)<br><sub>Tianle Zeng, Yanci Wen, Xueang Yu et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 1,144](https://github.com/louiszengCN/CarlaAir) | Recent aerial vision-language-action (VLA) models show promising single-UAV capabilities, such as tracking moving objects and navigating to language-specified landmarks |

## World Models & Generative Simulation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [FrozenDrive: Zero-Shot Text-Guided Driving Scene Generation and Data Augmentation with Parameter-Free Frozen Diffusion Model](https://arxiv.org/abs/2606.20110)<br><sub>Yuhwan Jeong, Hyeonseong Kim, Daehyun We et al.</sub> | ECCV 2026<br>2026-06<br>📑 1 | [⭐ 9](https://github.com/daehyunwe/FrozenDrive) | Synthetic data for autonomous driving is surging, powered by diffusion models that promise scalable scene generation |
| [Orbis 2: A Hierarchical World Model for Driving](https://arxiv.org/abs/2607.15898)<br><sub>Sudhanshu Mittal, Arian Mousakhan, Silvio Galesso et al.</sub> | NeurIPS 2026<br>2026-07<br>📑 2 | [⭐ 31](https://github.com/lmb-freiburg/orbis2) | Current world models operate at a single level of abstraction, with most prioritizing perceptual fidelity while lacking the spatial reasoning and semantic understanding required for real-world downstream tasks |
| [MESSENGER: Memory-Enhanced Sequential Scene Flow Estimation via Autoregressive Next-Frame Forecasting](https://arxiv.org/abs/2610.10759)<br><sub>Jiuming Liu, Jianing Li, Mengmeng Liu et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 0](https://github.com/liujiuming123/Messenger) | Scene flow can capture low-level 3D motion displacements in dynamic scenarios |
| [ASTAD: Asymmetric Style Transfer for Synthetic-to-Real Adaptation in Autonomous Driving](https://arxiv.org/abs/2606.29286)<br><sub>Dingyi Yao, Xinqi Zhang, Lihui Peng et al.</sub> | ECCV 2026<br>2026-06<br>📑 1 | [⭐ 2](https://github.com/Dingyi-Yao/ASTAD) | Synthetic data mitigates the data scarcity problem in autonomous driving perception |
| [Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends](https://arxiv.org/abs/2606.01164)<br><sub>Jiuming Liu, Chaojun Ni, Mengmeng Liu et al.</sub> | arXiv<br>2026-06<br>📑 10 | [⭐ 252](https://github.com/liujiuming123/Awesome-Interactive-World-Model) | With rapid development of large language models and diffusion-based content generation, world modeling has attracted increasing research attention, benefiting various downstream domains such as game engines, embodied AI,… |

## End-to-End Driving & Planning

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [UNIVERSE: Unified Video Action Models for Autonomous Driving with Flexible Mask-Modulated Modality Generation](https://arxiv.org/abs/2607.05133)<br><sub>Mengmeng Liu, Diankun Zhang, Jiuming Liu et al.</sub> | NeurIPS 2026<br>2026-07<br>📑 17 | [⭐ 6](https://github.com/xiaomi-mlab/UNIVERSE) | World Action Models (WAMs) can improve action generalization in autonomous driving by learning scene dynamics through dense future-video supervision |
| [MOJITO: Modal Joint Learning for Unified End-to-End Autonomous Driving](https://arxiv.org/abs/2607.23511)<br><sub>Zhijing Cheng, Xuancheng Zhang, Donglin Di et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 31](https://github.com/mumucc01/MOJITO) | End-to-end autonomous driving systems commonly follow a cascaded two-stage pipeline where a perception stage compresses multi-modal sensor inputs into a compact context and a downstream planner predicts trajectories cond… |
| [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](https://arxiv.org/abs/2609.26792)<br><sub>Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.</sub> | CoRL 2026<br>2026-09<br>📑 1 | [⭐ 15](https://github.com/VAIL-UCLA/DreamStream) | Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions |
| [DriveMLP: When Training Strategy Outperforms Model Complexity in Autonomous Driving](https://arxiv.org/abs/2610.29676)<br><sub>Alessandro Canevaro, Julian Schmidt, Hang Yu et al.</sub> | CoRL<br>2026-10 | [⭐ 6](https://github.com/alessandro-canevaro/DriveMLP) | Learning motion planning policies that remain reliable under closed-loop execution is a central challenge in Autonomous Driving (AD) |
| [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)<br><sub>Shen Zheng, Anurag Ghosh, Gaurav Parmar et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 32](https://github.com/ShenZheng2000/WarpI2I) | Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs) |
| [G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance](https://arxiv.org/abs/2606.26017)<br><sub>Hang Yu, Ye Jin, Alessandro Canevaro et al.</sub> | IROS 2026<br>2026-06<br>📑 6 | [⭐ 7](https://github.com/HangYuu/G2DP) | In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors |
| [DriveZero: End-to-End Driving Beyond Human Demonstrations](https://arxiv.org/abs/2609.06055)<br><sub>Hao He, Chengcheng Hu, Zirun Su et al.</sub> | arXiv<br>2026-09<br>📑 11 | [⭐ 149](https://github.com/XiaomiAutoL3/DriveZero) | Most end-to-end autonomous-driving systems learn by imitating human driving logs, leaving their learned behavior constrained by the quality and behavioral coverage of the recorded trajectories |
| [SimWAM: A Simple World Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.07468)<br><sub>Zongchuang Zhao, Xin Zhou, Tianyang Xu et al.</sub> | arXiv<br>2026-08<br>📑 23 | [⭐ 212](https://github.com/H-EmbodVis/SimWAM) | In autonomous driving, World-Action Models (WAMs) have improved end-to-end planning by transferring video dynamics priors to action prediction, but many still couple planning with future-video generation at inference, in… |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 23 | [⭐ 368](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
| [Latent-Centroid Steering: Single-Pass Classifier-Free Guidance for Command-Aligned Autonomous Driving](https://arxiv.org/abs/2608.00237)<br><sub>Meibo Hu, Jiamian Wang, Pichao Wang et al.</sub> | IROS 2026<br>2026-08<br>📑 1 | [⭐ 2](https://github.com/codingmlinprocess/LCS) | Vision-language models (VLMs) have recently emerged as a promising paradigm for end-to-end autonomous driving, enabling agents to map multimodal inputs and high-level navigation instructions directly to executable trajec… |
| [STAGE: STyle-controllable Action GEneration for personalized autonomous driving](https://arxiv.org/abs/2607.29517)<br><sub>Zihao Liu, Xing Liu, Yizhai Zhang et al.</sub> | RA-L<br>2026-07<br>📑 1 | [⭐ 5](https://github.com/CarlDegio/STAGE) | Driving style refers to the behavioral preferences that drivers maintain during driving, shaped by their diverse experiences, habits, and needs, and is typically reflected in varying levels of aggressiveness |
| [A Survey on End-to-End Autonomous Driving Training from the Perspectives of Data, Strategy, and Platform](https://arxiv.org/abs/2610.00926)<br><sub>Chengkai Xu, Yiming Cui, Jiaqi Liu et al.</sub> | arXiv<br>2026-10<br>📑 7 | [⭐ 111](https://github.com/Jiaaqiliu/Awesome-Training-Ecosystem-for-E2E-AD) | Autonomous driving is a cornerstone technology for the future of intelligent transportation, where end-to-end learning has emerged as a transformative paradigm that directly maps multimodal sensory inputs to driving acti… |
| [AutoE2E: Don't speak - Language free end-to-end autonomy A Real-Time Driving Model for L2++ ADAS and L4 Robotaxis](https://arxiv.org/abs/2611.22374)<br><sub>Muhammad Zain Khawaja, Zaynab El Mawas, Ryota Yamada et al.</sub> | arXiv<br>2026-11 | [⭐ 234](https://github.com/autowarefoundation/auto_e2e) | AutoE2E is an open-source end-to-end driving model developed by the Autoware Foundation Robotaxi Working Group |

## 3DGS / NeRF Reconstruction & Sensor Sim

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [MCSplat: Multi-View Photometric and Geometric Consistent Feed-Forward Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2610.25345)<br><sub>Yifei Wang, Wei Tian, Wenhua Bao et al.</sub> | NeurIPS 2026<br>2026-10<br>📑 1 | [⭐ 15](https://github.com/yfwang0824/MCSplat) | Driving-scene reconstruction via feed-forward Gaussian splatting from sparse multi-view images remains challenging due to two factors |
| [DriveWeaver: Point-Conditioned Video Inpainting for Controllable Vehicle Insertion in Autonomous Driving Simulation](https://arxiv.org/abs/2606.31918)<br><sub>Junzhe Jiang, Zipei Ma, Zijie Pan et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 18](https://github.com/LogosIntelligenceLab/DriveWeaver) | A pivotal step in autonomous driving simulation involves inserting foreground vehicles with predefined trajectories into simulated scenes |
| [Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796)<br><sub>Leshu Li, Jie Peng, Yang Zhao</sub> | ICRA<br>2026-06 | [⭐ 15](https://github.com/UMN-ZhaoLab/Pocket-SLAM) | 3D Gaussian Splatting (3DGS) has garnered significant attention in Simultaneous Localization and Mapping (SLAM) due to its advances in capturing fine-grained geometry features and synthesizing novel views |
| [NIDAR: NIR-Guided Intrinsic Decomposition for Scalable Scene-Agnostic LiDAR Intensity Reconstruction](https://arxiv.org/abs/2609.36878)<br><sub>Junjie Zhang, Jie Yin, Kefei Qian et al.</sub> | IROS 2026<br>2026-09 | [⭐ 25](https://github.com/Zjj587/NIDAR) | LiDAR return intensity provides complementary surface-response cues for robotic perception and state estimation, yet many simulation pipelines omit it or reproduce it using reconstruction methods that require real intens… |
| [MM-TRELLIS: Point-Cloud Guided Multi-Modal 3D Vehicle Generation in Autonomous Driving](https://arxiv.org/abs/2606.24301)<br><sub>Hongli Xiao, Youjian Zhang, Yucai Bai et al.</sub> | ICRA 2026<br>2026-06 | [⭐ 10](https://github.com/HongliXiao/MM-TRELLIS) | Recovering realistic 3D vehicle models from autonomous driving scenes is crucial for synthesizing training data and building simulation environment |

## Perception: BEV, Occupancy, 3D Detection, Mapping

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Deformable Gaussian Occupancy: Decoupling Rigid and Nonrigid Motion with Factorized Distillation](https://arxiv.org/abs/2605.28587)<br><sub>Yang Gao, Wuyang Li, Po-Chien Luan et al.</sub> | CVPR 2026<br>2026-05<br>📑 3 | [⭐ 25](https://github.com/vita-epfl/DeGO) | Understanding dynamic 3D environments is essential for safe autonomous driving, particularly when reasoning about human-centric, nonrigid agents |
| [Horizon3D: Sparse Radar-Camera Fusion for Long-Range 3D Perception in Autonomous Driving](https://arxiv.org/abs/2606.31096)<br><sub>Geonho Bang, Geunju Baek, Dongyoung Lee et al.</sub> | ECCV 2026<br>2026-06<br>📑 3 | [⭐ 26](https://github.com/geonhobang/Horizon3D) | Long-range 3D object detection is critical for safe autonomous driving at highway speeds, yet existing radar-camera fusion methods remain limited at extended ranges |
| [DRS-VPT: Directly Relocalizing in a Scan with Vision Point Transformers](https://arxiv.org/abs/2609.12557)<br><sub>Lanke Frank Tarimo Fu, Maurice Fallon</sub> | ECCV 2026<br>2026-09 | [⭐ 27](https://github.com/ori-drs/drs-vpt) | We present DRS-VPT, a feed-forward transformer architecture for foundational image-to-scan registration |
| [Explainability-Aware Frustum Attack: Exposing Structural Vulnerabilities in LiDAR-Based 3D Object Detectors](https://arxiv.org/abs/2606.29963)<br><sub>Chengzeng You, Binbin Xu, Soteris Demetriou</sub> | ECCV<br>2026-06 | [⭐ 2](https://github.com/SecMindLab/Saliency_LiDAR) | The structural vulnerabilities of point cloud-based 3D object detectors remain poorly understood |
| [PointLAM: Local Attentive Mamba for Efficient Point-based 3D Object Detection](https://arxiv.org/abs/2609.21780)<br><sub>Xuanming Shang, Weijia Zhang, Chao Ma</sub> | ECCV 2026<br>2026-09 | [⭐ 5](https://github.com/PointLAM/PointLAM) | 3D object detection from LiDAR point clouds faces a fundamental dilemma: voxel-based methods achieve efficiency at the cost of geometric quantization, while point-based methods preserve fidelity but suffer from prohibiti… |
| [PriorMaskMap: Robust Online Vectorized Map Construction with Biased Priors](https://arxiv.org/abs/2610.39283)<br><sub>Haoming Xu, Wei Li, Yu Hu</sub> | ECCV 2026<br>2026-10 | [⭐ 1](https://github.com/healenrens/PriorMaskMap) | Online vectorized map construction provides autonomous vehicles with essential, real-time semantic and geometric scene understanding |
| [Vernata: Self-Supervised Learning of LiDAR Point Representations](https://arxiv.org/abs/2608.06919)<br><sub>Oliver Lemke, Alexander Liniger, Abel Gawel et al.</sub> | IROS 2026<br>2026-08 | [⭐ 22](https://github.com/rai-opensource/vernata) | LiDAR serves as a primary sensing modality for robots operating in outdoor environments |
| [Towards Compact Autonomous Driving Perception with Balanced Learning and Multi-sensor Fusion](https://arxiv.org/abs/2606.02979)<br><sub>Oskar Natan, Jun Miura</sub> | arXiv<br>2026-06<br>📑 47 | [⭐ 9](https://github.com/oskarnatan/compact-perception) | We present a novel compact deep multi-task learning model to handle various autonomous driving perception tasks in one forward pass |

## Motion Prediction & Behavior Modeling

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [MolmoMotion: Forecasting Point Trajectories in 3D with Language Instruction](https://arxiv.org/abs/2606.18558)<br><sub>Jianing Zhang, Chenhao Zheng, Yajun Yang et al.</sub> | arXiv<br>2026-06<br>📑 21 | [⭐ 154](https://github.com/allenai/molmo-motion) | Motion forecasting is central to visual intelligence: agents must anticipate how objects will move in order to plan actions, reason about physical interactions, and synthesize realistic futures |
| [Flow-ERD: Agent-type Aware Flow Matching With Entropy-Regularized Distillation for Diverse Traffic Simulation](https://arxiv.org/abs/2607.06957)<br><sub>Seulbin Hwang, Kiyoung Om, Dae Jung Kim et al.</sub> | RA-L<br>2026-07 | [⭐ 0](https://github.com/seulbinHwang/flow-erd-project-page) | Realistic and diverse traffic simulation is essential to autonomous driving development |

## Datasets & Benchmarks

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [The Road Ahead in Autonomous Driving: The KITScenes Multimodal Dataset](https://arxiv.org/abs/2606.02956)<br><sub>Richard Schwarzkopf, Fabian Immel, Alexander Blumberg et al.</sub> | NeurIPS 2026<br>2026-06<br>📑 5 | [⭐ 30](https://github.com/KIT-MRT/kitscenes) | Existing autonomous driving datasets have enabled major progress, but fall short in sensor fidelity, map completeness, or geographic diversity |

## Safety, Robustness & Evaluation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [CCFM: Collision-Constrained Flow Matching for Safety-Critical Scenario Generation](https://arxiv.org/abs/2607.04451)<br><sub>Ke Li, Kaidi Liang, Yuxin Ding et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 3](https://github.com/KELISBU/CCFM) | Evaluation of autonomous vehicle (AV) planners in safety-critical closed-loop simulation is essential for real-world deployment |
| [CADET: A Modular Platform for Evaluating Distributed Cooperative Autonomy in Connected Autonomous Vehicles](https://arxiv.org/abs/2606.04072)<br><sub>Pragya Sharma, Brian Wang, Mani Srivastava</sub> | ICRA 2026<br>2026-06<br>📑 1 | [⭐ 0](https://github.com/nesl/cadet) | Deep learning models are increasingly central to autonomous vehicle (AV) pipelines, yet their integration has traditionally followed a monolithic design where perception, planning, and control execute on a single onboard… |

## 🏢 Industry Tracker

Latest 14 days of news, official blog posts and new open-source repos from tracked companies. Full daily feed in [`daily/`](daily/).

<details><summary><b>Waymo</b> (253)</summary>

- 📰 2026-11-25 [Waymo Recalls Nearly 4,500 Robotaxis Over Freeway Safety Risks](https://news.google.com/rss/articles/CBMiiAFBVV95cUxQUTdkNnBiV0RkbXpZNkFNeTZ0Q1pZekl2elppaHhWVi1nMzFhdHFfYkU1Q0cxNEpyT2NRcmM1LXJ6RVIxRVRiLVlaTExPWk1fei1KdGxQd3hkSWNhcEI4UTFtM0lUZHlTcms0QndCRXViRTIxSEtlOTktMmw0VHhUZ2NiMDB0TmZT?oc=5) <sub>Law Commentary</sub>
- 📰 2026-11-25 [Waymo halts freeway rides after California DMV orders ban, cites safety incidents](https://news.google.com/rss/articles/CBMie0FVX3lxTE5CRE1XVnFnWlBYaldncXdqRWI2YkEtNTVxOGtrOGk5bDRGLWw2aTdZRWg4UUZlZVYtaWliY1N5M09WM2d0Zl84T1JZOWlzZVd6V0hRbHN4dHVwX0hrcXJtcEVhRGkzODVCOGdyWU1yRkdfY1RoVEhpR1BONA?oc=5) <sub>Mashable</sub>
- 📰 2026-11-25 [Waymo Is Banned From California Freeways, For Now — Here’s Why](https://news.google.com/rss/articles/CBMiekFVX3lxTE9XZEhtSy11OGtOSm9NUG5aZGJ4T3JKSVduUng4T0tnMmszZFlGU09Ea2NvVUh3ckNRY0RJTzBzdFA4cHVpV1hSZjJiNlFWUEg4dzlVdkZjUENfWVNsLU9uc19CalluZko5OVc1VjhjR2FJbkUtU29lcWdB?oc=5) <sub>Family Handyman</sub>
- 📰 2026-11-25 [Waymo Issues Multiple Recalls: What Atlanta Drivers Should Know](https://news.google.com/rss/articles/CBMinAFBVV95cUxNMUs0ZkZMT0NaYjMzbU9pM3VVLTJNaG5sVTE3ODhpeXNWemZpQlVIU1BKRVBrZ1VCOGY3SjczWVpLM1k0STg2cEFoSFNOS1ZFTGtZajRsaUlEd1ZBSXFaQkpONzlvd2N5X2NUQVlMc1ZGbTd3MWI4em5EelR1Z1NEVm93eWN0YkFfSDBISmphamN6MGo5Z3dySGg3THrSAa4BQVVfeXFMUGtYdmRhQ0plVHU2SE05aVdKSHBRNk00dkdHZ0cyM0RXQ2NKN1JXQmJ6eXdPUU5XWFI2LUpqaEtaUXpzY1hjZFoyWXA3c0lVVVNhU043cG5GdXM2S2tQaUlsbGl3LVNIdGNVaW5nTGg5bGlWN3hhMWNxR3gyVU83UHBsZEpZV0I4TnY1djhTdHZkTjQteFVwUTF5dmtac0RaVVRfN3FZVXQ1ank5eV9R?oc=5) <sub>Patch</sub>
- 📰 2026-11-25 [A Denver man has egged and trapped Waymo cars 30+ times and isn’t facing charges](https://news.google.com/rss/articles/CBMinAFBVV95cUxPZVBuYjUzbmk5dnUybVVrYk1kUGd5RzNzMV90SGNNV2RpRUVKcTRrZ0NSWXY0dnVXYzBJcnRDUjhPV3ZQdEd4cm53Qjdhc051NWp6Q0ZBZndxWExCRDR3OHZrRWYxTzVCUmMxZE9GY3l5amdwalVhbXliczEwRlByN0pEY24wcTBmU2x2LTQyU2g3N3NHaFY5S2Mwbzk?oc=5) <sub>98.5 KYGO</sub>

</details>

<details><summary><b>Tesla</b> (393)</summary>

- 📰 2026-11-25 [Tesla FSD V15: 25x Claim, 0 Baselines Published](https://news.google.com/rss/articles/CBMijwFBVV95cUxOZkhNTVJLQ2lidjJaUFpXcE1hYV9KMEpKV3NXOFdBdjFkVjdfR2tOUkdJaHlsRDVuS1FKc3hQN2loeXkyQUVUVzhaa011NUw1V3pFbzM1dnZxSnVVa01FUlJTeV93OVF2UWlGTUg0RS0wRzNkc01jWjNuNTgxRHZGc003Vmx3Vm9OODRhUkdtaw?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-25 [Tesla FSD V15 has completely shattered the so-called "intelligent driving is good enough" narrative.](https://news.google.com/rss/articles/CBMiU0FVX3lxTE45eXdDNGVMWEV2eWsxdEJXNEZlelhoUkNIN2V3QktDa3pOMzQ3WGprTmdUV0pFbC0zaEVBV2l6clRoZ1ZTaURRQ2JXcl9hSE9qT2s0?oc=5) <sub>eu.36kr.com</sub>
- 📰 2026-11-25 [Tesla FSD v15 is a whopping 25 TIMES better at handling SAFETY-CRITICAL situations on the road. And yes, that's 25 TIMES, not 25%! We're talking about those split-second moments when a driver might need to grab the wheel to prevent an accident. Tesla'](https://news.google.com/rss/articles/CBMibEFVX3lxTFBKM0JBNTNvaVc2Z0hVTTVEVHFnMjlxQ21ZcG15U2R6N3R6NDJpNmtGdGV6Z19CbWhwOFJ3cm9nbmo0bU1VTlFRLXBvVDAtVVg1aXpSd0NNOGpfS1E3b1dpeWt4OWRlU1FNNktDQg?oc=5) <sub>X</sub>
- 📰 2026-11-25 [Tesla Begins FSD V15 Rollout With AI-generated Reality View](https://news.google.com/rss/articles/CBMimgFBVV95cUxNZUhiUnFmTXRLaXRRb2M0SE05TWRpNkpoZUVhNF9XLWhVMml1ek5Bb2k2TEE0YjFvVHEyMjZHejNzS0V3SUZFcFh5LWVJb1pfb1lCVXdud016VzBJZmd6aDJJaDJ3TGI5bW1oMThFZkp5THBPYzY3VzVXR0k1dDZJVElIRDdJcEFNNlY2aDVndVBDSm1oVXVDS19R?oc=5) <sub>Dataconomy</sub>
- 📰 2026-11-25 [特斯拉FSD新版本“抛下”老车型，机构：国内部分智驾车型或在2028年面临类似问题](https://news.google.com/rss/articles/CBMiZkFVX3lxTFAtRzlxMmhIUzBoYjRnTVE0YUlOTzBLb3NhbUt2N3N3WWhMMFRsaVg2aWVtdUxteDBGc2Z1MTF5MGhiTGZwU0tWM3RFNTRCY2NZQ1JzX3hLb0x4ZzQ4WHl4M0hBaEJiUQ?oc=5) <sub>金融界</sub>

</details>

<details><summary><b>NVIDIA</b> (225)</summary>

- 💻 2026-11-19 [NVIDIA/nvidia-linux-utils](https://github.com/NVIDIA/nvidia-linux-utils) <sub>GitHub</sub>
- 💻 2026-11-16 [NVIDIA/scadactl](https://github.com/NVIDIA/scadactl) <sub>GitHub</sub>
- 📰 2026-11-25 [NVIDIA's new GeForce Game Ready Driver 621.40 reportedly fixes 'excessive' SSD writes](https://news.google.com/rss/articles/CBMiywFBVV95cUxNMnQydTZGclR3ZGJxcXM1eXFGWW1oRWRHREtLZy1XY1pkQWJ6QjhHQXVHNk0wRjczWXpjdEpheUlKZFY0ei1iYjJPY1BxRGdnanNiZ2lMV2xUemdtZ2FiakhlRzl2Tll4Wk8xNUtLUkU1dGxZLW16YW9ubHRTcDk2cUt4dFB4dDJMYUZSTENtX1ozM2FRdHJ0a0pGSjNGVS02MVhodFFTNE9RRHdiVXJDMVI3UXBhVmRTQ1hZWE9IcVdYS0pUcGt6c2FjQQ?oc=5) <sub>TweakTown</sub>
- 📰 2026-11-25 [Trump’s China Hawk Act: How Nvidia and AI Profits Drive His Policy](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBkaDFQQWxLazNqYkZ3TWxxTVFHOVZ6N2xKOWFrNHFiRjVLOGZpWUZEaTRBSTVBampRMXR4U3NBSG9kaTMzc2wwQ1ZlUTRNYUFrWjZFdXB0czhuSURMX2Zr?oc=5) <sub>Savage Minds \| Substack</sub>
- 📰 2026-11-25 [NVIDIA Fixes SSD Abnormal Write Bug, Releases Standard Driver 621.40](https://news.google.com/rss/articles/CBMidkFVX3lxTFBGSTRFNDh3OV94YTZKQUxqQm5mM1lGcWE3dmZGNEg0WG9kaUZ4UkdpTVR2aGR2MzhZZmdxQmdmMnQxSlhVMmgwNmtPM25Zdkk2RmZmMTR3dk1DTG1ILWl1NVFSOUNRVnVSX3dUUTNaZ0xCWGJsTXc?oc=5) <sub>BigGo Finance</sub>

</details>

<details><summary><b>Wayve</b> (32)</summary>

- 📰 2026-11-23 [Autonomous Driving Software Market to Reach USD 6.78 Billion](https://news.google.com/rss/articles/CBMinAFBVV95cUxNZFVjLThIaVVwbm1rWlBYT2IzMDFFZEF6LWVzaWY1YTR6b0JLeDBla0VacjF0dEtpQjhGblZpVjUyZV9ZM3lSS3UwdFdtYmp0dm15SzdBZnpEemNqMlcxMXZ4TnVDV3FqZjNCOGdWNFhBRGFUWVNlV2poZHFkdDA1OEY1QlZaZzZ6Z09QQWtTRDQ5WGxyV2xmbEtxOHo?oc=5) <sub>openPR.com</sub>
- 📰 2026-11-23 [Mercedes gets edge over Tesla in race for self-driving success in Europe](https://news.google.com/rss/articles/CBMihAFBVV95cUxNREhrZGszRlNBUzFxbjBURFBhQldOMDFiOGV0TVNMWWVuYjA5dFdCTGpGV0RCMlJJczEtWkd0eG9YRnkwZnFVTFRseC1iT1lBM2w0LUlUVFhqdk1ydU1vWDRPVGZfTlE4SnRSRnZZTkMzVzdnVFJTM0dobnRKRG1jOV9Yb0w?oc=5) <sub>Financial Times</sub>
- 📰 2026-11-22 [Kakao Mobility partners with Nvidia to develop Level 4 autonomous driving technology](https://news.google.com/rss/articles/CBMi2AFBVV95cUxOUnMwVTdET0JiaXlkcm83bUZkQUt0TFpJd1lkZG13a1JIUWl3dW81UXlGbHN1Q2Z4VDZGVE5GcFNmeTRsNG1kODJpTTJCclVueHQ1LVFTOTFFWUVpRUpQYmMwc0ZSUHJqN05IR292WVBsOTFUMDl5VldhWUd2UkRfd1NXZ1BQcnI2TFFJdmx1cHN6RFY3aWl0VnppeUxYV2xPWjdZRWRJVzkwWFZ6SWdXQ3FLdTNLMFE5bTRMUkZRRWdlamhhT3ZZNXVOLW5LbnVaX3h6STh2VGM?oc=5) <sub>Robotics & Automation News</sub>
- 📰 2026-11-22 [Nvidia to Continue Robotics Investments After Huang's Departure, Assures Portfolio Companies Directly Under Interim CEO](https://news.google.com/rss/articles/CBMidkFVX3lxTE1IbWJob3hvWTZuUDRrRXFpZ2phdjVSWllyTmpLN2VSMlR0MV9NaExQVjJ3cHdlVUQ0czI1Y09HM256ZWY4QVhUZ3VLbUFBSTN1RU1GLVdENTdIcmNvSzlibnluYTlHUFc3b2M1TGRWTjNTeXNNZmc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-21 [California Bans Waymo Robotaxis From Motorways](https://news.google.com/rss/articles/CBMilwFBVV95cUxQSnRJcXd3Z0dtS3FZTzh4cHoxclA2Unh0ZWRwZTBKbVZxd0VBSEtOUXBQVWduZjFyMmtfOTdoQldVMUlGQWhtenRwRVNnOElQamx2V1lXUEFINGxrV3FQYUVFTHhWcHhFVmRkYUxDbGZoa2d5VWItS3BFaDBBSklVakFnSlFIOEMzcXRuSWxnMlkzQzNyWGFR?oc=5) <sub>Wisevoter</sub>

</details>

<details><summary><b>Momenta</b> (112)</summary>

- 📰 2026-11-25 [凯迪拉克XT5插混版智驾值得买吗？23.99万起配置分水岭+3个维度说清+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE9lX1pIR3hpbk5DSWFDN3Nwb18tQU9jMTdrNHNnX0w5dEpqMzRXbEdjUFZGTGdUMDZrLXhYQTkxejRyNERHQjJwb2k4X0ZjMWZXS2pibGEySUU2Q3ZmR0dfMU0tVF9OYloyVzZYR1pNMGluZw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-25 [【网通社快报】Jeep品牌计划2027年在华推出首款车型并搭载Momenta智驾系统](https://news.google.com/rss/articles/CBMiTEFVX3lxTE9iX3FIMFRyX0JrT2c5RW05dmo5Z28wRmxZOHJ2a3FtTW9Na1BwYXRSUlZER0ZuRlB5dEpwVERqSGlCbW42X3U4RTdha1g?oc=5) <sub>凤凰网</sub>
- 📰 2026-11-25 [Jeep发布“Jeep+”生态战略，首款新能源车2027年上市](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9WczJqQ19QRzBqUmdCdWFXUmRpbWFHbGRmQWIyWW42cmdjR0xkOUFZQl9wZ054RWxGNjlwd1lPR0o1aGFNVHZBa3doa0JWbUZ4Z3AwVzF3ME9mV1k?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-25 [26.99 万起的新世代iX3，开进秋天里，10 分钟补能418 公里\|Momenta\|宝马\|麒麟\|BMW iX3_新浪新闻](https://news.google.com/rss/articles/CBMiY0FVX3lxTE5VX3hxQkRYaW5JSjhTOTBramFvalFSeXdqZjZlbHE3VGFCVkVpdkpsSWVDM3JZOFpxYUNyMWJNckpxTzV4a2ZkTnVOYWhjUGFCT1VQMndPUnZfc3hhZHdJMi1LTQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-25 [传祺E8 PHEV和M8怎么选？3个维度说清谁更适合你+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE1jd09TRzdzRjNxUl9EZWJZMnA0MkJ5RUJTY1M1d3lqdVlNUi00LVVfTGpQbVI1VUZIOHZPZnFrNDUxSGtBOUxwVWgtS01qSlJnT1RIVGZLdWlVWUExZUU1ZHBNQVVtMm10cVg0WFBGOWEzQQ?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>XPeng</b> (248)</summary>

- 📰 2026-11-25 [XPENG Positions IRON Humanoid as an Autonomous Work Partner](https://news.google.com/rss/articles/CBMiiAFBVV95cUxQSjVxMVhjZ1ZFdllETE1iOVZwakxoMWx1ZlNXRHhQRVMwZWZUZGU3SWp6X2M2OFpCOWU4ODBGVExIRW1LZHlPNGxBWWdKQ3hvd0JNdndLYzVrNTdVVGRJYUN4SjJGN1BhMWdZN1lVS0J5N2pLamc1TkpFcVZjUmtWUUwxN25TYVdn?oc=5) <sub>Unite.AI</sub>
- 📰 2026-11-25 [XPENG Unveils WorldGPT AI Model For Cars, Robots And Drones](https://news.google.com/rss/articles/CBMimAFBVV95cUxNODFfcGpLWXNPLVB2NkVVSUpmTlZhS3BkMU00NFRDQVR3YXZzR3RjNTVqLTRIVkxTbF90R0RHc1hCN090bW84SFhsUlMzX1Raa21NaWd2NWFxM3VhZWI0UGJ5ZHdLN0NPcUZlQjFGRlNleExFeDNBZmRTMHBxaWRNajBYVWdHT2J4OEgzUVNRSVE2Rkdkb0tSOQ?oc=5) <sub>Dataconomy</sub>
- 📰 2026-11-25 [XPENG Shows Off AI-Powered EV Factory As China's Robotaxis Gear Up For Global Expansion](https://news.google.com/rss/articles/CBMiW0FVX3lxTE42RUlCOTFzcWNWVlVzUEk1Ri1NSkFfdWRBN29jd29od1RCYzA0alk4X3NyWUhaT2pDRVRQeHJ6QjRVT0dyYVBiMUN3Y0l0aWxZQlZ5enc2TUdpZGs?oc=5) <sub>Wake Up Singapore</sub>
- 📰 2026-11-25 [【视频】15万元带智驾的纯电SUV 逃不过的选择](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5fMXhHYVhnNXNYU2JKMnJyTjZkNGJFVkoyOW50a1JKLWptMjNNNXlDZ3ZuLURGd2ZyY1hjQ1hUdkhQVmZ4MldKdF85NGNnVExkczhha0FOZVZRa1k?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-25 [小鹏智驾订阅2027 年开启，老车主权益终身不变\|小鹏\|图灵AI 智驾_新浪新闻](https://news.google.com/rss/articles/CBMiY0FVX3lxTE5QQzlob0FWeXFoci1RaVB3TVhfVDhEZkpNVVpvMGtRaWhNek5Pa0hQWmVMLXFHN3gtVG5SU0dLMXl5dW4wNXo2YXp5S1c2ejI1T0tkdWdNX3dkT1hBamtPRTlrcw?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>Li Auto</b> (187)</summary>

- 📰 2026-11-25 [China’s Neolix gets nod to test self-driving delivery vehicle in Singapore](https://news.google.com/rss/articles/CBMirwFBVV95cUxPY1V6b0VBRS1ESnRTZGNPRHMyNlRlNDZMei03cklEbzl5dzZGX1p6Y3VVZ05BNmRuNnNMQmV6TjZBWkVTa3M3ZWROYkZpUVl4TlZyTHQxdDZyUzA4bm1WbmpRcGZoTlFDU1V6T2paLTZwU0IxODJzb1oxQ3R4NWxSdWtybzI2ZHAydXJSQjdsTW5NSGVjSHc4T05vN3dIaUxlb2R2ajV5SHFfSTlYdEhj?oc=5) <sub>The Business Times</sub>
- 📰 2026-11-25 [【网通社快报】理想汽车首个全场景试驾体验中心落地郑州，L8 Livis与L9 Livis开启试驾](https://news.google.com/rss/articles/CBMiTEFVX3lxTE5sdTFaZVRxcTVUbHBFZlYwN3o4blJaUzk4aXI4VGpEcTdiOVdLeGpRM3B1czhzRjA3RmFHQVo1TmtISC1CRnN3NUdtd1k?oc=5) <sub>凤凰网</sub>
- 📰 2026-11-25 [理想ONE 2021款还值得买吗？11万抄底前必看3个维度+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBxSTRXV1BWLUZzc3htcEo2aV9FQnFqWVQxNnhKX3RLczdFOXYzZ1VJN1JWYnkzTVZJbDVFSFlaT0R2dGZHblg3QXlxMkxSa0ZHQkdSbnpoUE5tU3h4SER3?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-25 [港股异动｜理想汽车-W(02015)涨超5% 今日将发三季度业绩 前三季度累计交付约29.34万辆-证券之星](https://news.google.com/rss/articles/CBMiXkFVX3lxTE5xUzhqcF96N1hrN3JIVVFCUFYydnN1X3cxR3hPeUpId2VxQlRnTF9HRFNNcF9VLW5ub29pTU9Nc2Z0MDNreGNsV1Y4QV9lNG9oN2JUTk9GZnhZYVFCcnc?oc=5) <sub>证券之星</sub>
- 📰 2026-11-25 [试驾理想L9 Livis 10000N主动悬架稳吗？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE8yR29SczQ3aFlROFhqLVdxaGFfUDk1elF2QU50YUJ4Ny1OZ0dyN1JUQW5kODJjZnNVRW1pUkxzUUZhQk9Fb2xUYnJmODkxWjMzR2ZxUHR6QTlwT3c?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>NIO</b> (191)</summary>

- 📰 2026-11-25 [BYD targets acquisition of Ineos French plant as Macron confirms January details](https://news.google.com/rss/articles/CBMigAFBVV95cUxNVE9uUWlQcTlxNS1JMWRvV05nNms2Mk1QZ2U1MW5KZUMwQ3ZaWDA5R041TkFEWUxhaDJFWVRPXzYtMDZaTGJ5cllIT04zSFdOY1ZqSUhTYlRJVVp5N3lVQ3V0b0tBR0I0R1lJcEVJdmkwZWdvYUJFMkxPVTBVcVhOZQ?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-25 [智驾不再只是反应快，蔚来这次把物理世界装进了车里\|蔚来\|nomi Intelligence 4.0\|NWM 3.0_新浪新闻](https://news.google.com/rss/articles/CBMiY0FVX3lxTE9xeVZVdS15LXpDMEVFM0dmbkU0c2poS3hWNEswLUxiRHFYWjhJZWlhdW5IYWNoUHNBb2NNd0lKZEhDelo3OHpjUlNGMExKclNIb2xYVzlqdVdEMU9paXR3SGROcw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-25 [【视频】蔚来ES6 2020款610KM性能版租电版](https://news.google.com/rss/articles/CBMiW0FVX3lxTE02SVRCM1lvUTNyWXR6ZjZvdFN2cTZlanNXRi1VYVpqbnUwSVJwcHpPcEllYlZIR3RUZlpXUjdOSy11R2huOEs0RWtyQjRoUTJJbVpJWEVmTzlhdFE?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-25 [蔚来ES8值得买吗？95.7%车主满意+3分钟换电，3个维度说清+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1VV0tuRHg4LWRBSnJad0JuTUZDMldBc1hDc2ptNFpXaDM1YUdGS1ljTU1QeUV4NVd4NFo3bjk5VFk2eXJ2dmFMT0ZtOFQ0TWluT2dvRkpEelVjOVlvektR?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-24 [BYD Fang Cheng Bao Shark pickup to launch in China on December 2 after Guangzhou Auto Show debut](https://news.google.com/rss/articles/CBMiggFBVV95cUxQR1M1OGF1R29mVU5pZHo5b0tlT21rTl8zWGt5MlpDb2dJYVh0czdlZHNsbDlSTk1tODRvX0xFWUNaNmozQkN0V3V2SkE3ck1KQkVGNVVQcFlFd3E4X2o2LW5admd0SmEtcGtXdW00UTZEQnhHUHctblB6eFp3V2JSMk13?oc=5) <sub>CnEVPost</sub>

</details>

<details><summary><b>Huawei</b> (376)</summary>

- 📰 2026-11-25 [HIMA AITO M8 Debuts Huawei DriveONE Range-Extender](https://news.google.com/rss/articles/CBMikgFBVV95cUxNRmhLcVlFUDA1QW5oS3hKUjNGS2JWanM5cllmMmVQUmhqQ0pkaGlVWkZLeDZvaWR4MEhZN1JlMk95Y1R2NUNzT3A1VDhRWXhibC01end4V2wwemVqQzBBamwzMTRJSmtCOGNpWVlVLW81MGF6OUpja0h4ZS0zZ0tLdTRySG5KaGEwMTE1WU9ya1loQQ?oc=5) <sub>DSF.my</sub>
- 📰 2026-11-25 [Chinese tech giant Huawei is guilty of conspiracy to steal trade secrets, US jury finds](https://news.google.com/rss/articles/CBMi_AFBVV95cUxPVVlwVkdBNDBvZWQ1QThoREhxQUtQNmlrN2d1MFN0REM3bVpHVjFoRjEzR2RtZVRmOFh0Z0w3U2ZfWXROZWIxTGpzWFlhMlJabG0ta3pheWVyVHJYeWwxUXJLMTh2UEQtN1ZxVmNlOS0xcEdYTFllelZkZ2Y2LTJRTnROQWlFLUxIVm5rN1BjSURaVUVMMGNwZ1AxZUgyRnRKMzFxVzZ5MVNPbFlMUjRKWEl0UTk1a3dMN09FaFpvbGZ5UzZFVDJsQ1Z6Y2ZvQUZUd2Q2bVVMS3M0WWZvRy1lOFVVVUlaRWRBSm1sbjcwQ2lORmhIRUVlSkVaQVrSAfwBQVVfeXFMT1VZcFZHQTQwb2VkNUE4aERIcUFLUDZpazdndTBTdERDN21aR1YxaEYxM0dkbWVUZjhYdGdMN1NmX1l0TmViMUxqc1hZYTJSWmxtLWt6YXllclRyWHlsMVFySzE4dlBELTdWcVZjZTktMXBHWExZZXpWZGdmNi0yUU50TkFpRS1MSFZuazdQY0lEWlVFTDBjcGdQMWVIMkZ0SjMxcVc2eTFTT2xZTFI0SlhJdFE5NWt3TDdPRWhab2xmeVM2RVQybENWemNmb0FGVHdkNm1VTEtzNFlmb0ctZThVVVVJWkVkQUptbG43MENpTkZoSEVFZUpFWkFa?oc=5) <sub>Indiatimes</sub>
- 📰 2026-11-25 [Huawei and Landmark Group drive measurable digital growth for Centrepoint and Home Centre](https://news.google.com/rss/articles/CBMi5gFBVV95cUxPR2R1aDFLYmZTX21YTFAxZVVOS0s0Y2dkY2pINmNiMi1jY2tTZWV3VkZWNV9veEZOb2JHUFllaXV4dGFkUEtLX3R5T296MEFiTHpjUlJ1Z1lnb3N0VDktaXFVT0NXcTU5UTBmaHBVdnc0UXhDYlhYZG1ocnpFR01FcEhONm83MlcxRXRSb3VRaWNQbUVfZHV4aVk5eWdxWHNEendNWUNaU3JFR3FCMHV6UzJFV1VfS21OOWw1akNtSm1waTJhVVJ3eGN0MGJyU0NMWFR0akRXaDJCNzl3N1AtTTJjVklHQQ?oc=5) <sub>Zawya</sub>
- 📰 2026-11-25 [BYD targets acquisition of Ineos French plant as Macron confirms January details](https://news.google.com/rss/articles/CBMigAFBVV95cUxNVE9uUWlQcTlxNS1JMWRvV05nNms2Mk1QZ2U1MW5KZUMwQ3ZaWDA5R041TkFEWUxhaDJFWVRPXzYtMDZaTGJ5cllIT04zSFdOY1ZqSUhTYlRJVVp5N3lVQ3V0b0tBR0I0R1lJcEVJdmkwZWdvYUJFMkxPVTBVcVhOZQ?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-25 [Huawei and Landmark Group report digital growth for Centrepoint and Home Centre](https://news.google.com/rss/articles/CBMijAFBVV95cUxNV0xOSFBUWkthbHlpUndGX2N6clJWUjFPMEw1NjVBQmt0Q3g4QkYzeUdRa25GLXdKMXV5LTFvdjE5cUY5Y2lldFV6Um9ubk1zcTdURnNvSjdjcV93QTI4VGR0TG1UdlVpM3hGUU5pcTVhVzZRQTJIcElSbWdNS0xTZ0VqN2JpY2xDSmJYTg?oc=5) <sub>Campaign Middle East</sub>

</details>

<details><summary><b>Baidu Apollo</b> (56)</summary>

- 📰 2026-11-24 [时时彩中三开户平台活动，签到30天居然有大惊喜？](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBpNlhrMFlHdDRqMjlfRkhDd1VCYjVaUkNYWm1hQi1xMkplWTJyc3pNeVVCOUlTbUp5NHI0X05nNnVxUDVraG1HMUdQZFpORmprRDR5NGd2aEJpRmVEekxZ?oc=5) <sub>iheima</sub>
- 📰 2026-11-24 [11月AppStore中国免费榜（旅游出行）TOP100：滴滴 同程旅行等居前三](https://news.google.com/rss/articles/CBMijAFBVV95cUxNdFBiME03TmtOV0QzQkxDRnhMa3o1bjJLVUZUZ2Z5elJWVGZJencwTzVnMmFCUlVEalNXaGttTVEtejRJVllDWjJRTU1lZk9pY0o5RldBSXphMWZpa1REU1F3ZktBb0tMOU9ZVkpsblVxMENBZ0g4ZUlyQ1RnRlVVQ3hDMjRIN2NfdkRVRw?oc=5) <sub>Sohu</sub>
- 📰 2026-11-24 [铂智4X每公里1.13元，深圳单车日净收394元](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9oZDY1UE9qRVBPS0VSeDJXQm9QNkVxOExDQmluODJFb0FSZ0NtTFh0YV8wYUIxc2J1V1BjeFBuUmh2c0p5Q0cwWnBaWWpxTS1qLWVZWXgwTk8zeUk?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-24 [WeRide edges ahead in China’s robotaxi race](https://news.google.com/rss/articles/CBMiekFVX3lxTE1QSEp5TjZvQVFYVWU0ZVowMC1obGJTaHhnWkZLTjZlYWhFTW44bF9zVlRFbm5fZ1JGdy0zZ2pWLXNlQ1hGQzRKZXZvWDdiRk81OHFUZS0yY2FSNDFWYjZsbV9fSjJUWEhKdUF6anVUREExd2pOeEgxOTB3?oc=5) <sub>Bamboo Works</sub>
- 📰 2026-11-23 [Robotaxi market forecast to reach $179 billion by 2034, says Polaris Market Research](https://news.google.com/rss/articles/CBMi1gFBVV95cUxQVVd2N1FiWjJWb2FUMWZuU3NMeUlleEpUVTFFUWppNDk0Vm9lRlNPNWpTQS1ORE5vMXJZSDFfN2lVLXdNUWVJaDB1aEotbHhMQWhobUFqUDZ3QmVsWHhhTk5ueUt1TWlMaGVnRVZMRmttZGdfei1WRUVycVZNbGQ1NVR0TnZfTnpUM09wYjdOSnRTYzJnY3p4X1FacndOa2gxU2pIY2NZLTg2dVA3d0F0OXh3TjQ2TklXcTR0cDZmSFFoZnR2Qk1nY0VzVkl5UHM5QkxTbW5n?oc=5) <sub>Robotics & Automation News</sub>

</details>

<details><summary><b>Pony.ai</b> (149)</summary>

- 📰 2026-11-25 [Robotaxi同题答卷：文远知行押注AI基础设施，小马智行死磕自动驾驶_公司新闻_财经](https://news.google.com/rss/articles/CBMiYEFVX3lxTE5GZ29PS2R5bDE0U2p1OW1OZU85SXRRenlheU5WT014THJiRmM4MTRRN1NaRmRoUm1ZS3g0MHppNTZCSGZ1V3l2eDM2OXFxZ0FMdW5yekRhbnBIVTBwVm1jRA?oc=5) <sub>证券之星</sub>
- 📰 2026-11-24 [小马智行Q3财报：收入大增75%，Robotaxi收入翻倍](https://news.google.com/rss/articles/CBMijAFBVV95cUxNQmpMdkxvR3NhTjBzZXZ6ZzVXMkpCNUNjdUtDbXYwUVNIX3AwdHZkZ09KZVJUYzlQNjFKTlJCakNybXJHRl95WXFxcVFWcmtNRVN4cDZsUm9vcWdhOVhZMEU0VWh0V2dfOVdNMk8xYm5tVHF3Y2VxM0M0NGxLUDc3MEQxMnlxX0MzNHJJSA?oc=5) <sub>Sohu</sub>
- 📰 2026-11-24 [小马智行港股跌5%创新低 募67亿港元基石浮亏81.5%](https://news.google.com/rss/articles/CBMibkFVX3lxTE84bEU1ZnNfWGdsT1h6eFlRQ01Md3hveV9rZEJiWlBONWRoTTZGbWVjUUFQTWloSTUtanpkSWJqTlNKS0tNeTZZT1lLUFE3T0xoRmJKdGxxem9WY1Rtc2REbUZSUlZOWEdzYW9zMUln?oc=5) <sub>中金在线</sub>
- 📰 2026-11-24 [极狐Robotaxi成APEC靓丽外景，中国自动驾驶加速驶入全球视野](https://news.google.com/rss/articles/CBMigwFBVV95cUxQTC1GMjFoQUtEcXRJT1d6Rk1CNzV6czFCQk9KaVVuNlhkZFdSU2RjMzNfRDRyT3YzUHlya1AtQlNKd2ljNHNoV2Z1QWVGbDJWS0NfRVlvSUtabm9Va0k1bjZYX0lWZEFPQU53VjZ2MzJKRzU0QVVfemE0Z1FYdEZvXzA2TQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-24 [ARCFOX无人德士亮相APEC Level 4智驾技术领先](https://news.google.com/rss/articles/CBMiuwJBVV95cUxNMndjc29VdjRSbUNTY1RvdGoxdzdDRFlWem42UGVTTXhORlBVNmlEbmpjYVlRaUtMSUEwOThoNUE0LWh5T2xia2ZYakVjMVZ4dzdnUzNCTms3TWdHd2ltOUwtbmRGY2pFWkJ3WmUwdlIwRXYzcnNWZ0JnMGlvQ1BkZDN1RjJBSW1GZXh6SFdfLXJ1dUU3QnRHeDlUWW5zRFc0TFdJVldSV0hiMDN6ZXZSY1JpQ2RxU1RuMnRORmJKWWNMZ29lX3ozd1REcTU2dGtXZlFRMWtiTnRrT0xFRnA0eU1UZVpkTnhDWElObFlaRG5taWVpdm9hYm1wSTFqUzlLTUFoQ3JPWkpxeEN6azRZWnVPUTVfWmFOZUZfbnZ5WkZLVEI5d3luMi1nRXRYR0tzRjBmU2hpeUZCSGM?oc=5) <sub>MyWheels 车天地</sub>

</details>

<details><summary><b>WeRide</b> (136)</summary>

- 📰 2026-11-25 [Robotaxi同题答卷：文远知行押注AI基础设施，小马智行死磕自动驾驶_公司新闻_财经](https://news.google.com/rss/articles/CBMiYEFVX3lxTE5GZ29PS2R5bDE0U2p1OW1OZU85SXRRenlheU5WT014THJiRmM4MTRRN1NaRmRoUm1ZS3g0MHppNTZCSGZ1V3l2eDM2OXFxZ0FMdW5yekRhbnBIVTBwVm1jRA?oc=5) <sub>证券之星</sub>
- 📰 2026-11-24 [文远知行Robotaxi三季度收入过亿元，同比增长超2倍](https://news.google.com/rss/articles/CBMijAFBVV95cUxPeXM1UjBqRnlkRTdaelFZcGtPQkgzZGlxYjlKWGxtcDNoRHZtRXV0aUVTYTZwamN5N01hMHZDUFNBTzhJWU9FYkNoUDNvUkxMN0JaVWliTFRMcS1iSE13LXhac0xyTHZzRW5LWXMxZVJNVGlqMWJodEVSelQxTEdJT0ZDNzA1ZXBFbElYZw?oc=5) <sub>Sohu</sub>
- 📰 2026-11-24 [文远知行港股上市累跌70%创新低 募24亿港元首日破发](https://news.google.com/rss/articles/CBMibkFVX3lxTE54MUxROEpCaFBQM2tEa3ZVdlVKWXdlYzF2Wk9JQmdlRlZNYzdzZ19FY3V3RGQ4bFhXN05lVXVTY3hQU2NYTlM5QWgxQWVpSVJoZGpIMVR3SG9GMnlwT0lPZ1J4VmlxXzV6YmhYaTZn?oc=5) <sub>中金在线</sub>
- 📰 2026-11-24 [WeRide edges ahead in China’s robotaxi race](https://news.google.com/rss/articles/CBMiekFVX3lxTE1QSEp5TjZvQVFYVWU0ZVowMC1obGJTaHhnWkZLTjZlYWhFTW44bF9zVlRFbm5fZ1JGdy0zZ2pWLXNlQ1hGQzRKZXZvWDdiRk81OHFUZS0yY2FSNDFWYjZsbV9fSjJUWEhKdUF6anVUREExd2pOeEgxOTB3?oc=5) <sub>Bamboo Works</sub>
- 📰 2026-11-24 [43%毛利率叠加Robotaxi单位经济模型转正：文远知行经营拐点已现？](https://news.google.com/rss/articles/CBMickFVX3lxTE96aUowMC1VMWpfcnFkeFJnMGtLSHFhNzlCNC1nX0hiWWNpNFJlSEJKRndRQnJXMS1CTzBpbk5vUUZLZXR3VGprOTRId1o0eEFFU19CZlBHcXJpSUtfR0ZaV3JTQ2J3WUVkNXBnTlBvSlE1Zw?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>Horizon Robotics</b> (152)</summary>

- 💻 2026-11-22 [HorizonRobotics/holobrain-0.5-homepage](https://github.com/HorizonRobotics/holobrain-0.5-homepage) <sub>GitHub</sub>
- 💻 2026-11-22 [HorizonRobotics/HoloBrain](https://github.com/HorizonRobotics/HoloBrain) <sub>GitHub</sub>
- 📰 2026-11-25 [VW’s $18,000 Self-Driving Sedan Shows How China Leads on Car Tech](https://news.google.com/rss/articles/CBMitgFBVV95cUxQVXlfc0M1VERmTWd0UzV6SlRhYi1PdWtoQ0tHTG9vVnRDdUhBVXQxbzZYbHBxSlJQdHVYMWp6T1lUcE9xZzFqNXdJV1doZUtSNDFpWkllalZ5MU5sQl9McDJrdVlvZWxQdW1NYTlhYzZLRzBva3ZEZUc2OE1PVDA5ZldUOGlzTEdOQmtlVG9RSDNIUkJxVlZ1aHQ4RlhMcDM2THhURXp2SWs4UHJPaGVpb0JFanNZUQ?oc=5) <sub>Bloomberg</sub>
- 📰 2026-11-25 [VW ID. Era 5S: $17,175, Level 2, Not Self-Driving](https://news.google.com/rss/articles/CBMihAFBVV95cUxPX29OaGs5X29FN0szaGhwMzdIOXJ3bWFBdHFHZVZFUjgxb1Z4dzBCVk9vOXU0cVNseXI3NlZkU1ZHN2t0R2hHLXE2cUVNcWFhN1JfS19hRVdaMy1aYlRlNFJiOTVyZzlPd3pzV2d0aEV3bTB5UkdubDh4TlVzX0xiTzJ2cWM?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-25 [Volkswagen's new self-driving sedan costs $18,000](https://news.google.com/rss/articles/CBMimAFBVV95cUxOTVFicVpsZVRTelI2T3pmY0g1amxKMXZNcnRQV3p4QlMzWjBOemp4TlIzc2lfWk9pdVJFa24wellyeU9mRzR2MEJhTTZhNzBIeVA2Z3FXZGRnZjFNM3E0NHNvQ1dFRW01UzdZbEdabHZJM2taNWs2a25OMGxaSFdxbGNwM2JrZmpwR1lYaElUc1RsMkVqbEtxMg?oc=5) <sub>NewsBytes</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (16)</summary>

- 📰 2026-11-24 [Anthropic创始人第一份工作在百度，几年就打造超13万亿元市值公司](https://news.google.com/rss/articles/CBMijwFBVV95cUxNMXZJWE1ta2hxdmZ1VzFDOEluOEZ0Q1hmaEFwOUdvemZtTXljVGhLbTlYOVdEQkhaVEhfQ2ROazctRWNrdnE3TWNERWg2dFlDakNuSWJtRzBJUmxzQzlCWEtVNjNacWExQUNvT3Bkdmt2Y3VNOEYxUDV2eTlhcGhIWWluZWpMX2c3SFFvY2NQMA?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-23 [【视频】#奥迪E7X用车日记# Model YL和奥迪E7X 我为什么选了它](https://news.google.com/rss/articles/CBMiW0FVX3lxTE0xXzI3eHc3Y0NkcVFIQk5FcWdFMzZidmtYTm1oWlZFamVaSDlRbk5obWlYQzNfMzVPc3I5VzA5Z1BRWU5nQmplWUw1TS1QR2ZlZ19COWdYNVg2bTA?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-23 [【视频】最糟心的一公里，元戎启行DeepRoute IO 4.0帮你解决！](https://news.google.com/rss/articles/CBMiW0FVX3lxTE96eWM5ZDFCWTZsYVcwODlDTkt5eGtzNjdfQWswazZ1bHY3d3ZNM0FVLTZwSWlHZnVOWXZNVmpqT3ByOFVVaW1PajA0TXJONDVRWlJ1dDNneXFSUWc?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-23 [电竞明星表演赛+机器人嘉年华，2026AIE电子展不止是展会](https://news.google.com/rss/articles/CBMiTkFVX3lxTE42RzdweEtpMGdqeENTTWl3a1JidU13VXpRdWlYMS1sNXplX0VBaGkySTFxTVJqd0hJWHo2VllfeW1BZ2N1a2xKeVYwcHNudw?oc=5) <sub>36Kr</sub>
- 📰 2026-11-22 [巅峰对决松山湖！k8凯发入口官网下载入口2026圆满落幕](https://news.google.com/rss/articles/CBMiUEFVX3lxTE9YQXhzRFRySlFzc0h5eEpZZXJHekZ2bjZFZ2pma1hSdHViR2RHYlNVTjJBaFFEUFhhNzd6MEgwODQ1SlFydU9jMEt3UGJFaUly?oc=5) <sub>iheima</sub>

</details>

<details><summary><b>Mobileye</b> (14)</summary>

- 📰 2026-11-24 [Tesla Wants Drivers to Keep Their Eyes on the AI-Rendered Road](https://news.google.com/rss/articles/CBMiwAFBVV95cUxPXzdTSl9DbnRIZzNLVXRlQkxkc24tMUhfOUxBN3NYSUVjRXlUQXZTREZtUEowU1VNc05wOXVlNXF0Vm1LVE52MS0xcDVoNmpZVWwzM0ZkVUZlc0hWbmJTQWNLRzhPVDVBZzJINTl1NDdybHVFc0w5RzBnT1VIQlNvM21BYndrZlZ0N0VqQUVKTHBRdzh3WmQ5QUNLWkVKZUpyZUpQZXRFY2FsRW5DN0ZESDVwNjF4Yk9QVXFCUmJHaHQ?oc=5) <sub>The Daily Upside</sub>
- 📰 2026-11-23 [Robotaxi Market to Reach US$198.6 Billion by 2035 as Waymo-Uber](https://news.google.com/rss/articles/CBMioAFBVV95cUxOOVFHa1QzX0FoWEhodlVoV2tBekhIb245dmxkLTZBSTJyYVBuVU5LQWg0WFVtLWFIU0c5SDc4cjRTRVlJNEVXemxRQmlhTFhDTVEzb2JwcDVzZDZHNmRlN3BUTnZuTzFjSGFLNjhEb1J5RzNqVXV5cW91d0FVVjdKYUV0OEF1ZjlFM2VSQUNUSXQ2X1FUYmFLZ1VLbXFOdXly?oc=5) <sub>openPR.com</sub>
- 📰 2026-11-23 [Musk Says Cybercab “Would Win Even at Price Parity.” That’s a Problem for Uber and Lyft](https://news.google.com/rss/articles/CBMi5AFBVV95cUxQeW1Zb3BkMkFhT1p3NnIyVW9kX0xhU0p3Z2preUZSR3FOVm01V3lSOFlNM1dSbHJyWU51WmJLUkxtWTY1ckRHLThvNnJvZ0FTaFdXazVSQ3JuZEhHU1dYN3U4cEszSXNYdnRPSFpNZzl6a2E5MGtPWDhKZFRtUDV3Q0ZRcDRweWdPdTlqcVotaktSeUJtOG5Jck10MzNtTlREOE03a29CR3BmWkxwcm9XbC1xa0d1Yy0ya2tyWkM3NFdDTUxYUWtkTkpVU3lFV2NpYS0xSkoyOTZUU0lDS3ZZZHh5SFc?oc=5) <sub>TIKR.com</sub>
- 📰 2026-11-23 [Musk Agrees Automakers Must License FSD to “Survive Past the Next Decade.” GM Is Hunting for a Self-Driving CEO](https://news.google.com/rss/articles/CBMizwFBVV95cUxNNTBJU1JMVkxveWtjMU1mckJtS2c4UUhQXzBaMTczalpia29qT2U0WTBSUVc5NHBobjVBUER4WERvU1Nid2haWXpRbFZHMF83akM3T0JNUEdoTXlkOWpfQXRVV0xCT2xRWFZxbkpvdUtBbjBjTmxpVUd1N3V4NnVHaGI2UXB2Qm05Y3FnNmVzVmpOM0VMM1Rac2w3WGFSVVA4TkZ0eEZuZ2NZaEM5SWJnbXN2M1pDVk9PNGZjZ2t3cER3VEdZWlV3OElHcU10bVE?oc=5) <sub>TIKR.com</sub>
- 📰 2026-11-21 [3 Penny Stocks With Revenue Growth Up To 56%](https://news.google.com/rss/articles/CBMimgFBVV95cUxQNThVYk1RYkI1YkNMVi1JN2FWaG5fdjFHNVZ6bEVBNktGSURBeEd3NHh2dEVmSk5HRXdzRHdLd1NsdU5vLWJfTzBhaHVvWmw5SGZPandLZUpqc1NreFkwdUlRRllqOHpEcmVXRHJpZU1fSnhGdjNlblgzU2ZoXzh5RFNnNDlqVEFNd0R6TFJ4MjNEdkNORHUxaUZ3?oc=5) <sub>Yahoo Finance</sub>

</details>

<details><summary><b>Aurora</b> (36)</summary>

- 📰 2026-11-24 [Aurora Innovation (AUR) Draws Fresh Fund Attention, Where Does Fair Value Sit?](https://news.google.com/rss/articles/CBMi1AFBVV95cUxNNXNhcjdGTDhleVVxTFFWY0ZCVFdRVUhOeUxGY1lkb1FUNTMyLVBOTlUtRkJmRXdleUE5aXJ0MURSTUs3Y25fMk9HU0J6eXNFaGtPQi1FMmRvRDFGdzUycVg3NHk2MUpzWlhvclZjU1l6ZUkyNVRHdkdHT2dtaEp4NloybTZWVVd1cEZOOWh2S2VtNVJhYVc3UDEzQnp4cU9DQk5wTDdRd05Kd0dFdU5BRnJBSzFFV2dLMEU4aldtbEFsYU9sTnkxYmxFbFRoT0dkejV6TdIB1AFBVV95cUxNNXNhcjdGTDhleVVxTFFWY0ZCVFdRVUhOeUxGY1lkb1FUNTMyLVBOTlUtRkJmRXdleUE5aXJ0MURSTUs3Y25fMk9HU0J6eXNFaGtPQi1FMmRvRDFGdzUycVg3NHk2MUpzWlhvclZjU1l6ZUkyNVRHdkdHT2dtaEp4NloybTZWVVd1cEZOOWh2S2VtNVJhYVc3UDEzQnp4cU9DQk5wTDdRd05Kd0dFdU5BRnJBSzFFV2dLMEU4aldtbEFsYU9sTnkxYmxFbFRoT0dkejV6TQ?oc=5) <sub>Simply Wall St</sub>
- 📰 2026-11-23 [McLane to acquire Northeastern restaurant distributor](https://news.google.com/rss/articles/CBMif0FVX3lxTE5CbHJQVXNlSVhiT2NnMUZqSGFBdDdlMkw5QnpRYkhNVmQzSy1pdXRUWDRXVGdBTEkxaWs1OUxwSWFndkZPeGU2NWY0bTY3RTlnVm1oUWwzNERvUE0wcVkydC1qRklqajR4Y2pSdnRENEFzdHhHS2ZFN0lDS0NPM28?oc=5) <sub>C-Store Dive</sub>
- 📰 2026-11-23 [AUR Investigation: Kessler Topaz Meltzer & Check, LLP Encourages Aurora Innovation, Inc. (AUR) Investors to Contact the Firm](https://news.google.com/rss/articles/CBMigwJBVV95cUxNblIxN0M5MWplVWNpY2dEUzVCcEp3RW1scjlPbjNRNU10YUhvcVIzbDJudXB0clZSa2NKTkdMU3h4cXpER1QyWmFHZnplSGs1ejZtWG9WOGR3TFFkRVBLaERjdkdUV0lVOEJ5NTFVX2JGcEg4V0ozTlVyWmZZQzZYSEtDTXZ6YmpYYmNLQU9oZDdDSWE3TUJZa2w2NDBiT1dEbzRjQUFYN2pfSTQ4MWROVG8zbURueG5aaHUwdVkxaDExLWlidWtzOHhxZk1zaWY5VnhDdlJiaHdKek05Yi1rLVItdEFOUnZnSzZHcjk3ZVJVNVd6dlFqSDhWTkhXM2pKeHVN?oc=5) <sub>PR Newswire</sub>
- 📰 2026-11-23 [Aurora Innovation (AUR): Hedged Position Gains Despite Share Pullback](https://news.google.com/rss/articles/CBMijwFBVV95cUxQZElieFVfYkJWS09MMV83WXRRU0VIQnBITjZNLTNoY1A4RllLdG1rb19DSDlSTHJxbnZmNnFfMUI3YjVhQlhlUXRuUVpra1doQ0p5c21WX1lCRVZtN3lJaExLcEliVU0xUHA5dzk4YVZBVElLOVlrd0pVVnRXTEtlMVBvSUJuQk5PVzloak54aw?oc=5) <sub>Yahoo Finance Australia</sub>
- 📰 2026-11-21 [Bot Auto launches ‘Capacity Grid’ with agreements for 200 million miles of driverless trucking](https://news.google.com/rss/articles/CBMi4wFBVV95cUxNenB0d0xhRHB1QW96VjM5dl9yODU5THZxLWtmZEZ1WEc0TGZhQUlDOU1CdlNiR0Flc3ZoTzAyUnVoaEtOSUp4NEVyNXpqVi1vZldPNUY5VXRKUU5hc2xjVm9aZDdiN3R3NE9mUmVtajF0dG1hM1dFTmtJWWVwakMzQ095TjMxZU81VThwYy15T1FaaTJNN3ZEc1BxcDhCX2xjMDdHQ1pxRVNNaWloSUdTUmxkRkt2TUxNdGd4MTNEU082RnBxcUtxV2paVWFEeEJ0Z2t1SWJONG1jTDZIanM0N1QxNA?oc=5) <sub>Robotics & Automation News</sub>

</details>

<details><summary><b>Zoox</b> (107)</summary>

- 📰 2026-11-24 [Uber’s Lucid robotaxis now drive Bay Area streets with nobody at the wheel](https://news.google.com/rss/articles/CBMimAFBVV95cUxQeGluQ2hwZFNKcWx0UzB2UndFOHY3dWhwOVhnZ0EwdGZ2TVdjTXFzbDJXQUtCeTU4LUdKTHJ0QjNPaG5lcnFSU0xmcTc2UTVpalVZQzBDM0JTVkU4QVV4ZnFMdnNQdVl2T1ZYb0NLbUZvY25yQmNkbUw5X3ZmNlpHZGNGSDFXRkQyX09kZ3JhMmRqb3Q0czVLUg?oc=5) <sub>Martin Cid Magazine</sub>
- 📰 2026-11-23 [This Week in Chancery Court: Zoox, Restaurant Brands Settlement](https://news.google.com/rss/articles/CBMipAFBVV95cUxPb2IxTUdQdHI4YU5HNEp1bW1hNzUwbGV4WVMwWnI0TTY1N25VQ0lmWmU0M2RJd3c1UUQ1Ti1PcE8yR2xhVzZTR1RMaTFYTHluMUpicXB6QWV1bkRvWnJyVkZVM194bndZaXFkNDNHblI1ZVpURm9WZzBTY1c3UWRKVEExVWJqMkJkSDN0enhDQ3Y3YkRYcFp5d09fbDF1UUk5Y0xGUA?oc=5) <sub>Bloomberg Law News</sub>
- 📰 2026-11-23 [Forget the Race Track: Kacey Musgraves Had the Wildest Ride of Vegas Grand Prix Weekend](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1wQm1nbmJpV3BxTUtVRGlvRW1Bb01JNElFN3BoRXNqWGEyZXpKX1AzOVhUSDdWOHI2Q1d2djFINU1zWWE4N3ZmM2c0YUtiV2JNTEpZ?oc=5) <sub>شبكة تواصل الإخبارية</sub>
- 📰 2026-11-23 [Inside the Sonic Language That Guides Safer Driverless Crossings](https://news.google.com/rss/articles/CBMia0FVX3lxTE96bWxuOVVTUzJqb1g4TVp3NHBhaGFXN1Q4eUpldU9DQjV3bWdZWm4zVlVtUUE3TVdIUFpXV25nakt3RmVDdlpHaGxPcmh5dVhPOTJvSFl0SFNjV01fUm1nelJ5Q3ZqOUR4Q2dF?oc=5) <sub>IEEE Spectrum</sub>
- 📰 2026-11-23 [Zoox Passes One Million Riders, Doubling Its Count in Five Months](https://news.google.com/rss/articles/CBMioAFBVV95cUxNc0I0elBwbDBFcGtjZlg0TWtkeTlIZkxENTNHVUlJaEhNYjlZSTZuSWpzVXBoSGYtODBJdDdhaGNQc3ZER2o4eEZ6ejl5M2hZY2VYTGtKVDJ4dkNkY0s5akV6RjN0V1BTSkc4YXYxX2g4dU5URW9BaVc2bjZ6TGJOTmFxUno3a1haNzBzOGpFYmhVTUtQMzk3eVF3MG10emRa?oc=5) <sub>Electric Vehicles</sub>

</details>

<details><summary><b>Motional</b> (30)</summary>

- 📰 2026-11-24 [Hyundai Motor Group Eases Concerns with Jensen Huang's Return, Accelerating Autonomous Driving and AI Collaboration](https://news.google.com/rss/articles/CBMicEFVX3lxTE01c2Rac3ViNDBNSGl3ZXVQZDlDUXRJLXJvSkQ4ejlZRjdYdnN2cGFUZEdXNkVVY3FLTlNycFdIZElWQnh0V0xxR2VubkFQeENnQzJ3bDQ4RFV3T2Y0c0RCT0dJeXhEbFFzSUhxVldmMjk?oc=5) <sub>머니투데이</sub>
- 📰 2026-11-24 [Motional's CES self-driving demo crucial to reviving market confidence](https://news.google.com/rss/articles/CBMixAFBVV95cUxPYUs4MjRrRVQ3a1pSOHltMWwtbTQ3S2lzUWFZZmpQXzFtWlQyRm5Ta1FKWGdLTmZxY1RKQnBUX3l6dkZZcnc0S2RuajE0VlEzLWxMRVQ0NnRIdFBvbmZhZWhlenUyQTF2LWJUWGNIZ3FFWUFFRUcwNDVCdnR5MUZuVVhPT1pKeXFmQ1I3TWhxRnVjS2lEcG11T2JUY3VsOUk3X3FHcmVoLWJfZ2huYU1ySEYwZlByR2hyemM2dVBKSVBKb0ND0gHKAUFVX3lxTE1rLU8yUElERTh4U3JhZVF5MjlwcmctRzJsdGVwT1Z4eWZEd0p2M1cxUU5MaGdvV2lrYlVlNGxTd1RTM3pnVVRDdnJPNnF2WmpySmQ3YXUwb201ckNfbFd0QXp0M3ZsbU45b09ZR1JGdTVrQ3hMZldaY3VzelJFWXJRM2NGWEpoSEI3RGpmV3ZnZXpHM3Rid3A2d3RMYVV2YTRmdnZMZ2JtM1N5Q3gtRDlOajJ5WFZPOXdBbFpXMzhzNHlSUzc3b2tZeGc?oc=5) <sub>The Korea Times</sub>
- 📰 2026-11-24 [Nuro and Uber launch driverless testing in San Francisco](https://news.google.com/rss/articles/CBMihgFBVV95cUxQV1BiOFRXT05YdjZ3eG9ONlpieWlNTGxXSUNoWV9qcWVCX1hvbUVMb25YRlpZbjBRZWoxdC1tRUlzRlJJVG1EaFdWQVpBc3hiMkVYSXZWejFheUlLMUtvX3E0d2FXVkQ2VDJXYWh5WTZRX0tQV0VLV2NyaFg4QUlSWWsybHMzQQ?oc=5) <sub>Axios</sub>
- 📰 2026-11-24 [Uber Lucid Nuro Driverless Tests: SF Bay Q1 2027 Launch](https://news.google.com/rss/articles/CBMiggFBVV95cUxOTGxRQ1o3Sy1QRU9fNExyZmNIS1pnNlc4X0N5S0djZHFpQ254ZGZNa2U2OXpweFhPeF82TmhySk1JTDA4XzhYM3BweWhGaFM3b0RjSjcySlp4OW13OEx4Ukd3WmprSm1qcl9ST1ExOVVtSGp4UHFSTmNQUWY3QzlOT0d3?oc=5) <sub>explainx.ai</sub>
- 📰 2026-11-24 [Hyundai Motor steps up autonomous driving and AI cooperation as Jensen Huang returns](https://news.google.com/rss/articles/CBMifkFVX3lxTE1XX3pDamQzY3V3dU9JQlVOdXZ6ODA0N0Z1UWhBaVFGXzNvcnh1ZHMwZUUwN1FTWmg0U25Yc0NGeXhDYjFYNTlGWWlZVGZIWFlrUFhQMndRc0lid0ZzQ3lYTTRJNXBlLXM1Z25DQUdxQVhPR1h4MC1jZDZMR09FUQ?oc=5) <sub>머니투데이</sub>

</details>

<details><summary><b>comma.ai</b> (2)</summary>

- 📰 2026-11-23 [Open Source Drive by Wire Kit Retrofits Standard Passenger Cars for Autonomous Research](https://news.google.com/rss/articles/CBMisgFBVV95cUxOYkF5ZVN3eWtSa1FRSnF4Z091VFZlQ2pwZHIybWlxRHhMRXdwWFZMQk43QUNTc3d2VkNRbmNuSGxKUXh1Z0JMN1BfeHFqbFRtM2VnWldHeE9TQ0RVYThPVEpvTnpESTVYWEJZWlJDWWRqbVFYM1dTdFRkWklFd014a2N1d0ctbjlIQy16VW1YYnh1bm1rSmdOdHJvb0JGN1FTbVMzM2F0RUR5RF9SRnNfS1Z3?oc=5) <sub>Bioengineer.org</sub>
- 📰 2026-11-12 [Goodbye, BlueCruise! We Install a comma four in Our F-150 Lightning](https://news.google.com/rss/articles/CBMirwFBVV95cUxPY1o5ekZ4WnpraUxVMHV6OVdyMEtEbjQxQXY5STdJdXlHNlN6eUFZNzFwSnA5cFhHd3pNdTZNNy03dXBOZ1ZoX3RFX2E5V2JNTE9aVlhJaG90bW5YWEdzX2NGXzd3VFZ6NG5JVkFrM3daTmY4UDBTN1I4NWU3eGJqUm9tY1VaRWxoZkp3WDJLNnVLQjN5WG9NMzlxLWI0aVU2TFhLUEZwUE5YUDdUcWFJ?oc=5) <sub>Transport Evolved</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
