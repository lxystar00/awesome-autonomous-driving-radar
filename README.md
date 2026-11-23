# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-11-23 · 1,273 papers tracked · 48 curated.

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

<details><summary><b>Waymo</b> (257)</summary>

- 📰 2026-11-23 [‘How Can TSLA Compete With Waymo?’ Gary Black Questions Tesla’s Robotaxi Strategy, Predicts Waymo Will Le](https://news.google.com/rss/articles/CBMihAJBVV95cUxQaHRMZGMzSm9RNU1iR1NDZml3bkhBWHRVQjVmbWNZUVNxZ1VkdUtQWk12UF91N2hiVnFBOXNEM29zeHBRTGJ3YWFWZGNYcVhsLXcwNnprWEFqQWtiQ0V5TGk4TE8tYUZkSGtxZ0JXaFMyR0k4NTFKX0xydUt0Z2M3aTdVOUpuNVRkbS1UYlliNjlqRWNZeE5UMFZ0RHJhTmhxZi13MEw4M3owNUZJYWlsRmdRNkJNZUVva0g4YWZ1ZDFpamtUU2N0M216b2J2UWhvbmpVUkMyNVk5QW03RjU5MFp0Q1hEVHdFN1h1ejJhX3duMndEdFNFU0lzWTdlMWJhVWFxSA?oc=5) <sub>Benzinga</sub>
- 📰 2026-11-23 [SF mayor Lurie says Waymo agrees to pause service Monday ahead of storm](https://news.google.com/rss/articles/CBMiogFBVV95cUxQTmx5dV9Ib2VyTzE0czRkU2NIY0hPcHpqTV9CWi1sQjFfTzRNRDNYbnd2UlY3N1I5cUFzWjN4VlJRUVRSRDlna2l0VGx1a0RqTWl1Sktpb1dVWlhoYlYzdmVuMkRMSm8tcW81M1VuanJrdVM2VUdreEM2ampnclctUHNRN09nYXV0SVJEbndVOEYtUzhucmdFZnpIQjFPdzIzekE?oc=5) <sub>SFGATE</sub>
- 📰 2026-11-23 [Waymo is pausing Bay Area robotaxi service again as Thanksgiving storm approaches](https://news.google.com/rss/articles/CBMilAFBVV95cUxQbzdKTDJubW4wLXR2amh6bXpTZEpiUmpGQmZlN2dLOHNtVkdpaEtHbW40WHQ0UG9ySWZZeG4wZGU2c3FRYkNMeUNCNF9PcHFnU0pOeEVNTWZHQ3lfSWRIbXA4WTFPcGFBUVFxV2I4YnFuOWszazFFVWNYWTVkTW1EMURqVlVvY3hmdWg1NjRta2d5eXk2?oc=5) <sub>Yahoo</sub>
- 📰 2026-11-23 [Waymo Files Second Freeway-Closure Recall in 5 Months Amid Freeway Ban](https://news.google.com/rss/articles/CBMiqgFBVV95cUxQaHRUQmR6QW04cUxXRG8yTmNlZkNhOTNNUVg4a1ZJLW4zX1l3cy1qMkhXSFNaODhVa3N4cWlZMG9NOTJ2ak5OQzhhMHJ3a2dpZXFCYTMzcEVXTWx5dFVVRWJMeDc5M2QzUFNWaHc4aEhkenZWZUxYQlJJVHhlTmhLdXZ1OUZ2R1VrZ25DWGtxNk8xbUJBMGE4NHFqYlRXa0NvdW04ZjhhbTBFUQ?oc=5) <sub>Electric Vehicles</sub>
- 📰 2026-11-23 [Waymo to pause service ahead of severe storm coming to San Francisco](https://news.google.com/rss/articles/CBMiqAFBVV95cUxPR29ZMEV2cW5xYzh5TkZKVkFKdGNBVElubExIWHNnVUxaa3lOSzBRbEtGMG5JaUF6X0lFWk1uR0RJMFVrYTcxWUZDclROZ1JSSjhFTF9DeFBESkFfbXU1ZlpueGxYS2NRTEI5X0JqUXhGQXp4Zkl3RjR5WkhfclpiUmRmbS1GRUZTYVVySWQydm1jby1pNENRcGxlbGVxQzZRSXRkcXlzWUXSAa4BQVVfeXFMUF9TMkZvdkNURXd5cEU0Y3NsSVFjaWdTZy05WXV2RUt3VjA1SGx0SFZuRzNpQmo4bzNmeVRJUUZ6YTJnMDFPcmRXN3h2cE04ekpTTmYxVmZDQUFhR1IxNTk0bUVOWlBBYUlGOVRkc0g4MnM2MXVydWR6WHRIWHkwMlpsb3JzQ1EwWVZvR05ERlFfZkhCNGFhcEQ2dEJpYmItRUZ5V1hEbnRzYWhRdmNB?oc=5) <sub>KRON4</sub>

</details>

<details><summary><b>Tesla</b> (380)</summary>

- 📰 2026-11-23 [Tesla FSD V15 Adds 6 Detection Upgrades, Puddles Unproven](https://news.google.com/rss/articles/CBMimwFBVV95cUxPRnNyYVNVTEc0Z0FNX05JdUdsWGdONUdSMmI5cUZnSkdGOW9DaUFyc0hOamJJQnlDc25pNWtvdXV5TDZ1VVhpdTNIMlNZaC1nLWNXc05uNHl0aHhFcXZZaGpibHlmZWNMRklhRGQtZ0FhMm5kZ3EwcGtfNTFkZWVTajFBMERwZmMtSzVWc3hsUUNia21TaURsMVE1Zw?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-23 [‘How Can TSLA Compete With Waymo?’ Gary Black Questions Tesla’s Robotaxi Strategy, Predicts Waymo Will Le](https://news.google.com/rss/articles/CBMihAJBVV95cUxQaHRMZGMzSm9RNU1iR1NDZml3bkhBWHRVQjVmbWNZUVNxZ1VkdUtQWk12UF91N2hiVnFBOXNEM29zeHBRTGJ3YWFWZGNYcVhsLXcwNnprWEFqQWtiQ0V5TGk4TE8tYUZkSGtxZ0JXaFMyR0k4NTFKX0xydUt0Z2M3aTdVOUpuNVRkbS1UYlliNjlqRWNZeE5UMFZ0RHJhTmhxZi13MEw4M3owNUZJYWlsRmdRNkJNZUVva0g4YWZ1ZDFpamtUU2N0M216b2J2UWhvbmpVUkMyNVk5QW03RjU5MFp0Q1hEVHdFN1h1ejJhX3duMndEdFNFU0lzWTdlMWJhVWFxSA?oc=5) <sub>Benzinga</sub>
- 📰 2026-11-23 [Tesla rolls out FSD Supervised v15 with improved pothole and animal detection](https://news.google.com/rss/articles/CBMi7gFBVV95cUxNM1d1NWVtTVBOdk9mZmU1WkxMdlM0WHhZT2JIaWNUZDQxTlpzQ0dMLXNHMVJ6MU56eDgzWlIwODBiUXk0QkZ3NlQ3ZzE1LU81bV9EQ1VnaG5LN2FnbWV0NUstcWJ2OVdjTmFORG1zWFNOLUZORjE0QmVmSS0wWE9DOG9OUFdlMmRFVTczcWlyN0w2MU83cTRhaVZNdFNxalNhWHdlMU5SLUJEMm5ubmxWalVEb3VpX0pOb3NneWNJS0RjbW4xNnBYTkdMTXpiaU5icVFLT3pJN25WMWJWQURqd3k5VTlfc1FWaW9OS2VB?oc=5) <sub>The Driven</sub>
- 📰 2026-11-23 [Tesla Rolls Out FSD v15 Featuring 25x Better Handling of Critical Safety, Reality View, and More Upgrades](https://news.google.com/rss/articles/CBMi5gFBVV95cUxQUDhKX2FUY0dYZWotTWt5aDg4U1Z2UUgxR0FCaERKZ3RVUnhMd2VoY0tWcWQ2UkJQUy1uM0xQbEhqRnlLV0tfRXFHUElrNG15STFSbHVYLUF3UUVBd0o0TThLWmVPMm8yQTJQRVUwMEtWamlRekFyVGVyeDhiZjk2RDdFZnlGeEJxcVpyR0kxdjJjUXNYZFBmVzNiSzFGVVZQM1c0NlEySUQyY0VRLVJxUF8zQkNGaldCV3RQeTZBdTBjZkpqZVZFcnJnQmlGTnl4V3NwV0RuUG5JNkVJbGhESzRMZHk0dw?oc=5) <sub>Tech Times</sub>
- 📰 2026-11-23 [Tesla’s Unsupervised FSD future likely to bring Starlink to every model](https://news.google.com/rss/articles/CBMiZEFVX3lxTE1BUHFDNWF5Q200N0tDSmgzamt0VXJWUDRsRkxEdlM5T0dxXzdvUGJibmpxRFRSOW1qd3ExSkd4VHRmVjdLUjBIYml4UXhjRjVqY2RFZTg4Z2lCR0VwOEhGZy0xWnI?oc=5) <sub>Teslarati</sub>

</details>

<details><summary><b>NVIDIA</b> (234)</summary>

- 💻 2026-11-19 [NVIDIA/nvidia-linux-utils](https://github.com/NVIDIA/nvidia-linux-utils) <sub>GitHub</sub>
- 💻 2026-11-16 [NVIDIA/scadactl](https://github.com/NVIDIA/scadactl) <sub>GitHub</sub>
- 📰 2026-11-23 [AMD vs Nvidia: 7 RTX Tiers, 1 Confirmed Radeon Price](https://news.google.com/rss/articles/CBMilAFBVV95cUxNV2poY2pWbE85OWdaZDVSaXJSUUV6RmxucFYxYmViNzhlajV5THVEQldqNVg4Ymhjc3BpdG9xVzBYSXFyTTZ5Yms4clFhbjQ3eWxsaG1WNEdkWEhvbTN1WlRFMHd4SzRoaTVLYml0OEkyZHFnVWptTDRxbkp1Yll3SFZvSnY1WUpzQVNKdWdnd3p4dldo?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-23 [Nvidia pushes out-of-schedule GeForce hotfix 621.35 after SSD write reports](https://news.google.com/rss/articles/CBMiekFVX3lxTE42Rm9EdXJLV2NITUN0QjJmakRQX21UVzNpV2NLd1Zha3lIel85WjFLTTZOckMwWHJ5Z215Y0JOMXFMNklhOVFKSWIxZldXUXE5eF8xN1N4eUNnX1k1bjNwby1BTjJXRFFndFZJRllQYWNUb0JmWTBBU0JB?oc=5) <sub>MMOs.com</sub>
- 📰 2026-11-23 [Nvidia rushes out GeForce hotfix 621.35 after reports of 30GB-an-hour SSD writes](https://news.google.com/rss/articles/CBMisgFBVV95cUxOODNsa1lVOHRVUHM0UFBXZEM3T2h6emNwNml1ejUxUUhvVldtQXE1ejRnRmUweTF1emxwV0k4ZFdGUDhXMDlPSEpxWnFQaDd1NHdUQTFlWjFSZnItSnlBMWxBLTVncm9ZZG9QQml5UWh6Vy1NSHNUU0ZuU0x5MnByMXdFRlFqTThrbHpPYmt5WGlVdkhyWnJObjJJeXl3cF9mbXVaaXVKNFZJZnMzbFQ5b1Nn?oc=5) <sub>WellPlayed</sub>

</details>

<details><summary><b>Wayve</b> (49)</summary>

- 📰 2026-11-22 [Kakao Mobility partners with Nvidia to develop Level 4 autonomous driving technology](https://news.google.com/rss/articles/CBMi2AFBVV95cUxOUnMwVTdET0JiaXlkcm83bUZkQUt0TFpJd1lkZG13a1JIUWl3dW81UXlGbHN1Q2Z4VDZGVE5GcFNmeTRsNG1kODJpTTJCclVueHQ1LVFTOTFFWUVpRUpQYmMwc0ZSUHJqN05IR292WVBsOTFUMDl5VldhWUd2UkRfd1NXZ1BQcnI2TFFJdmx1cHN6RFY3aWl0VnppeUxYV2xPWjdZRWRJVzkwWFZ6SWdXQ3FLdTNLMFE5bTRMUkZRRWdlamhhT3ZZNXVOLW5LbnVaX3h6STh2VGM?oc=5) <sub>Robotics & Automation News</sub>
- 📰 2026-11-22 [Nvidia to Continue Robotics Investments After Huang's Departure, Assures Portfolio Companies Directly Under Interim CEO](https://news.google.com/rss/articles/CBMidkFVX3lxTE1IbWJob3hvWTZuUDRrRXFpZ2phdjVSWllyTmpLN2VSMlR0MV9NaExQVjJ3cHdlVUQ0czI1Y09HM256ZWY4QVhUZ3VLbUFBSTN1RU1GLVdENTdIcmNvSzlibnluYTlHUFc3b2M1TGRWTjNTeXNNZmc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-21 [California Bans Waymo Robotaxis From Motorways](https://news.google.com/rss/articles/CBMilwFBVV95cUxQSnRJcXd3Z0dtS3FZTzh4cHoxclA2Unh0ZWRwZTBKbVZxd0VBSEtOUXBQVWduZjFyMmtfOTdoQldVMUlGQWhtenRwRVNnOElQamx2V1lXUEFINGxrV3FQYUVFTHhWcHhFVmRkYUxDbGZoa2d5VWItS3BFaDBBSklVakFnSlFIOEMzcXRuSWxnMlkzQzNyWGFR?oc=5) <sub>Wisevoter</sub>
- 📰 2026-11-20 [First Shift: Tesla to sell Cybercabs for private ownership](https://news.google.com/rss/articles/CBMikwFBVV95cUxQcmhja0Z6TGs3XzF1eW9pcUc1Ry0wQU8tVDhWOG9UVWhfZHhRNXJNc3hicjdmQVBiV3JnWGxsVGZwd1hhRXV4Mmkxa09vNDYwb3dOLVhPNnhQMDVEdlFoVDRGV3FxbnhHXzNnRnBIUlB0cEliQmJHeEF2OW9rU1piSmdVWEIzQnBnMFVnMzJFNFlJVlU?oc=5) <sub>Automotive News</sub>
- 📰 2026-11-20 [CoreWeave and Humatica: Scaling Proprietary Enterprise AI](https://news.google.com/rss/articles/CBMijAFBVV95cUxNUlZMWTNaYTJnT0RvcFhBWXFRQlg4aVF3WWFNTkRPZVJ3S09zX2p3UzBSTTcwWnJGci1Pb0JHb3ROTG1RY0NRMElaRUI1SG91bXpvdHRrc3ExRktrcllHV2IwbTgwTzBjVmNvR1lNcGdDSlJhOVphTk1YQU0xSlBRYmphZ191U3lZSXZKSA?oc=5) <sub>AI Magazine</sub>

</details>

<details><summary><b>Momenta</b> (109)</summary>

- 📰 2026-11-23 [在德国用优步打车，来的竟是智己LS6，还是辆Robotaxi](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPeDlLeHp2TndxQ1YzS3RSMTNhZWM3R0xHVG04b2FBV1Zka29CRURZSjA4SkwzZWhzLVJabDdjVURYdEZsZnpMdzBWMW1wbncwR0M3VjlpdktuN1FESDlzc2RtZ1hLWHVOeU5admxiS1NMRlM4RUZvNHQ1MnhFREMxdEdsUDR5VHVh?oc=5) <sub>Sohu</sub>
- 📰 2026-11-22 [Uber and Momenta Launch Supervised Robotaxi Pilot in Munich](https://news.google.com/rss/articles/CBMikgFBVV95cUxOeXdWeUxBNWpfNEg3UmEwMUd4U2l2SmVtYkR2VjlibUZoWl9iNVNUd2lXSWx6Y1M2NnB5LWxnLVF4MExobHJ6UTJGcWNHN1VaWDA4SVBYOTN5TTRhVTZqWWNhXzlqQmpXSVdTNmE1WVlZalJCbFprRDE4TEg3LXlqdzN0bFJIaVZWa1pHcHA1X0lHZw?oc=5) <sub>Electric Cars Report</sub>
- 📰 2026-11-22 [Kakao, Hyundai Motor, and Socar Compete in Robotaxi Services… They Need to Join Hands to Get Moving](https://news.google.com/rss/articles/CBMiXkFVX3lxTFBLTWFnNExOTUIzcG5MMTVtNUh2VXB5VjBRRXhySXRiNF93OUQ1RFJDYXVNODFxUi01aFRxZmhhZVZlUC1xdzlRaXF1VlUzaktudl9aMzducnI2d2I1NEE?oc=5) <sub>경향신문</sub>
- 📰 2026-11-22 [Free Autonomous Taxis in Germany ᐉ News from Fakti.bg - Auto](https://news.google.com/rss/articles/CBMieEFVX3lxTE1HUzJrTEJxc3hDWXBOLWM0c2VMQjFlUnBlWmV1SW5MWkl6OVFyb3RncWp6ejJnMEdzQ2NHczR5emxfUm5Rd2EyZmlsbDdwQVVDTllUMklVaW52QWh0TmI5d2pORmhURTd0XzlQRzRZMXRHdDdOYnNvLQ?oc=5) <sub>Fakti.bg</sub>
- 📰 2026-11-22 [东风日产NX7预售12.99万起 14.99万版配激光雷达](https://news.google.com/rss/articles/CBMicEFVX3lxTE9wV0YyWURndjctY21JOFZUczlpQjhyUTREbGxsRkVDVURVNFFIc0ZvNGtLTmI4YlY5U1dPV0szV2xocXBQLVRsOElmbEwwdlJwTUtmb3E3MVktZnpyVW9DY3p0WGlDTWYyWHg4RjctUWY?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>XPeng</b> (220)</summary>

- 📰 2026-11-23 [XPENG Moves Public NGP Rides Into Its Paris Retail Store](https://news.google.com/rss/articles/CBMihAFBVV95cUxQOWZXbTFHMGlpekhDbGZUWmhJZTRsVGY2dXd0dkw5RVdreC1DYXAzVGxjZkthMkdiQXRyQ0ZEMmJYVlNodmlMU1Z4aGdVS2VFaVhwLS1XbjYxaUF3VDRKT21OZUowSjYtQmJHcExid1NOZ2NCT1p0d2htZlhxUFcxN1IwVXA?oc=5) <sub>Unite.AI</sub>
- 📰 2026-11-23 [Following BYD, Zeekr and Xpeng ramp up South Korea expansion; Chinese vehicles target premium market beyond price competitiveness](https://news.google.com/rss/articles/CBMiYkFVX3lxTE9Pa2JLN25EWUZSelg1Sm54U0VnU3d1OFB6dllqX0cyb2VfdWtQV0Q5RUpaRklQUEJfUUlkS0lTdjNDQVkwLXRlM1hUajg1RVdxRmhKdXU5RGVaUWZabnd4YkdR?oc=5) <sub>재경일보</sub>
- 📰 2026-11-23 [Xpeng says Mona L05 November deliveries exceed 10,000 as Mona lineup set to top 400,000 owners](https://news.google.com/rss/articles/CBMigAFBVV95cUxOOUE4d0VVZE5nTXJQTERCMExpV0FoS0lDbXZIdWVfckRLRGZQdDI0cy1zTHNwV3RiS2JGLU5xMXpxWVNEQ0JPZXZmeXludkxXUmFhMXo1MmZaZmZ2a3dSeWNlbzdoMGgycV9uTG1ZVGR2d0VSV2JxTVFTSUJmazZfcw?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-23 [XPENG Opens ADAS Test Rides in Paris \| Europe First](https://news.google.com/rss/articles/CBMia0FVX3lxTFA4bkNZUWFVd2FaVDhudUVtVWpZaUppcE0zZEhJZ3EwR2dBSm9zU1Q0cDV1d3pBYTZXX3Y2YVhFTVNOM2hkYXdocGNoZ21lMVNjcUdiV0Ntb25WaERKS1Q4YUQxSzFUZkRudjJZ?oc=5) <sub>XPENG</sub>
- 📰 2026-11-23 [Xpeng launches G9L in Thailand and Indonesia, accelerating global roll-out of flagship SUV](https://news.google.com/rss/articles/CBMiekFVX3lxTE45U3lMNURoSU1WX19heGt6MDF3eHNBREFoV3VXblBvNC1Ia240T1oyQVc2SkhGMXRRa0JCVzBlenZ1bzZtRzZ0Sm5yb0FsTFNxX1VRRlR5M29laS1qc1FNT2xzekM5UVBYanVKMGZ6c05rVWNPeHZWbXdn?oc=5) <sub>CnEVPost</sub>

</details>

<details><summary><b>Li Auto</b> (192)</summary>

- 📰 2026-11-23 [Nio to begin deliveries of refreshed ET5 Touring and ES6 in H1 2027, no updates planned for ET5 and EC6 next year](https://news.google.com/rss/articles/CBMilAFBVV95cUxOT1BIblYxYUxjaXc2UE5fS1hxVlA5S1NXLVZYWk1KdXM0OFBES1diV1A1NWstckQ1U3FnZzRuNkVUNmZzNE1IX2E3ZGlpajZaMU1BcE9OTUVhY2dhSHZtQlU5d1U3NFBXcmpPWFR0QjQxcmhOQy1Dc2FxemI0Ykx5eW5DQU1YYVNqQkZ5TjVYR3ZFVkRr?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-23 [理想ONE二手车还值得买吗？2026年11万起3个维度说透+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9RWnJ2cGlLbWJUODVES1duMnQwdjdTaEIwdHJYYTA2OVpidDlqYUt1cjhJZWtXamFJUDhGYm1RTE90andudWh6M2tlVExBY0piRG9iaXZfaVppZG52UldR?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-23 [全新理想L7谍照流出，2027年上市前先睹为快](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBIWGRHVURuNUkzSUdnZWpLNE5GVTJNWV9kWURQVkZWc0pweFlSQ2d3bWdncmJuRVFXZXAzVGJXd2hWcjdqZE9XdWVCUXhzWktlR0xsZHpMekpjbWM?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-23 [理想ONE 21款现在还值多少钱？新车33.8万二手10万，3个维度说清+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1vQktKMHg4aVJ2cHpIMXRFbDFWbmZwN01jOVM3ckhiX2tvcS03MG9Ia0hDRS12TE4zUjNKR1ZwMU5iSmVUZEpZSlRSSWRqSGJVeW1PeTB6cTlsR1hsd3Bz?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-23 [理想ONE二手车21款值得买吗？11万抄底还是9万捡漏？3个维度说清+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBnem9vVHRpbThZOU9aYXEwNTVMQUpLdVl4VmlnMFRoTFZpa19VS0FidGRmWnc0c3I5dVAycVlzclZ0T1Z5Q2l4aFZ5MWJQaGtEZHRTMHRfSkFGS2hlcWxv?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>NIO</b> (194)</summary>

- 📰 2026-11-23 [Nio CEO Says AI Sent Memory Prices Up Fivefold, Echoing 2022 Lithium Shock](https://news.google.com/rss/articles/CBMiqwFBVV95cUxOY1ZkMXQ0aW5DREx1M01lM3M5U2ROWENHMXdHYjc5Z1FDbk4wRl9oVzdzMFcweGRiYTJ0U1hteE1ZMlRxWWxMZjloSmNJUUI2U1FMRFUzQmI5ZmM5bUhUS3BJc1ExaGlpM3BKSXJ3bzBVUXlQR0tvWVlHTTRuSVc2ODhTQlJlZmsyaDhtSUp6UEQyLTQ0dkJXYmtMbWtxTnZURzhTQmhqaEZmalk?oc=5) <sub>eletric-vehicles.com</sub>
- 📰 2026-11-23 [New Nio ET5 Touring spied in China as CEO confirms 2027 rollout amid Europe delays](https://news.google.com/rss/articles/CBMiuwFBVV95cUxOZ0doR2ZKdHNza2VweldxSTA0amc5Z3k0OHVCZzFwUjUwc2ZPcFdtRmRXcDdfXzF3bllYcDBDS05yNm1BQk1uQ3JqTlRVR0FCNlhiTzFfQzB4a1lRVmhiUmVQY2JhazNTVHJYVFFxUExBODlOY3lJNjFVUjRsaGV0SHlsd0hxaEwtTy1XSTQ3YmJUZUlZamhJVnFzaWZUX2g1RUFSZGZGYjFBc0c3YXotbmNWazNjam90cXNV?oc=5) <sub>CarNewsChina.com</sub>
- 📰 2026-11-23 [Nio to deliver 170,000th third-gen ES8 this week, about 1 month after last milestone](https://news.google.com/rss/articles/CBMihAFBVV95cUxOTmYzeGFreVFJdElYSDduVTFkYjdmT2xoZDBfV2UyUWFtUWlSbkk4aEx4SnFLdEJJWTBueUJ0aTRyQi1YaVRpQWg5SW9leThReVlYQkU2N2JSWjY0MGdURVRmZ2pSZGtMcnU3ajEzRVRsY29nY1pZblgzUW5Pal9XVHk4bEc?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-23 [Nio to begin deliveries of refreshed ET5 Touring and ES6 in H1 2027, no updates planned for ET5 and EC6 next year](https://news.google.com/rss/articles/CBMilAFBVV95cUxOT1BIblYxYUxjaXc2UE5fS1hxVlA5S1NXLVZYWk1KdXM0OFBES1diV1A1NWstckQ1U3FnZzRuNkVUNmZzNE1IX2E3ZGlpajZaMU1BcE9OTUVhY2dhSHZtQlU5d1U3NFBXcmpPWFR0QjQxcmhOQy1Dc2FxemI0Ykx5eW5DQU1YYVNqQkZ5TjVYR3ZFVkRr?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-23 [【视频】昆明蔚来ES9装贴XPEL隐形车衣细节欣赏](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBEdVdZREszMVJuNGNpV2MwVnRfdTZucktzY01zRTJXZ29ScDBXcTI3VHJrN1dSWGZ6TUY0bmtRdFlBZl9TWHdhV01YS3JXYWM0ajlncmp2aWdTU0U?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Huawei</b> (360)</summary>

- 📰 2026-11-23 [‘More anxiety than me’: Driverless car attempts to park 868 times overnight](https://news.google.com/rss/articles/CBMiyAFBVV95cUxQQnlLSmFVODh3a2oyeklNYVhaWGM1WUJNZnl3LV93R2Fwd2p3R3QzQk1CRkJ3b1VpR2J3QWpMV09yX255eVRZM3phU3p5TG9XSjdFem5LelA0a3VlckdST29haWFBRjZoLXpNNWZvWGlLbXpuWWdyc0tIZjlxcGZidXRRemlzYnpWT2tQLVRXN1NJWlhwc1gtMnJ2WktYVzVkSkhKZGdqemNVaG5MTlFwWktOZzVaWlh4WEo0YV8zNEZDY3RKcVBDedIBzwFBVV95cUxOYTdwRTRMWllNYU9SdWhYbnZKdm9KN2xidEpnZENNZDJLeWpWT2tHR3hRMjFRNGtOVDdFeHJzMW9yVTY2Zm8yNUx6ZGFUNXVaR04yMVVLbHJxTkF4R0NPa3dRTlZBNzRBbDQ0V2JpdDZCMXJ1YzAtYTFYV05FLUt1YjdMVmdGaXZJdUtLVEFpNFpRSm9wUUVQMWVqbVZrZS04RlJNUVY5SkZKd0hkcjFnLWNtTDZLVmFicWNtLVRxRXNBYXpCQWF5VXYtVEdTZzA?oc=5) <sub>The Indian Express</sub>
- 📰 2026-11-23 [Why is someone alone in the parking lot at dawn… The truth behind China’s late-night ‘ghost electric vehicle’ footage](https://news.google.com/rss/articles/CBMigwFBVV95cUxNZlNHa2gwTUJHQy1GaHJRcEhvZ3FEUXE3b3FxOERSZVJtX0VMejd3RVBVLVd5WEhoR3FPRXlCQmszM00xSjRZU2FrQTZWM25ud18tV3U2cDU1Y1pYTXY2Z0ROQnZYYktPajcwcWNHVzJkcHBURUdqVjdCYjR5YlpFQTFxbw?oc=5) <sub>스타뉴스</sub>
- 📰 2026-11-23 [Nio to deliver 170,000th third-gen ES8 this week, about 1 month after last milestone](https://news.google.com/rss/articles/CBMihAFBVV95cUxOTmYzeGFreVFJdElYSDduVTFkYjdmT2xoZDBfV2UyUWFtUWlSbkk4aEx4SnFLdEJJWTBueUJ0aTRyQi1YaVRpQWg5SW9leThReVlYQkU2N2JSWjY0MGdURVRmZ2pSZGtMcnU3ajEzRVRsY29nY1pZblgzUW5Pal9XVHk4bEc?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-23 [Huawei Unites Europe's Creative Talent at the HUAWEI Watch Faces Summit Milano 2026](https://news.google.com/rss/articles/CBMi1wFBVV95cUxNeGFoNWNGSTBJU1g1c0RuYVduMDh0UVgwMFpSX1pSOVFORmlDVEh5NU83SFpHemdkUTJ4LXRqM29WMDVFY2U1eGpVUFRKajVKVHo0OWF4LW1hQjZsZkFOeVdzNHJpTHltUm1BcWxpalBLNDRqazJkNU9UbTR6N2dXRlFqOHMzcFMtMHVIcXdQTzRXbjR1Wkl5ZUx2MFo4aHhnYjJjMWFUTldZV3cwX0RhT29hWEFISEVzdmQ2dmxqUVFwNGVfRGUxT3AxRk9oNkNrTVZidDVZaw?oc=5) <sub>PR Newswire UK</sub>
- 📰 2026-11-23 [Xpeng says Mona L05 November deliveries exceed 10,000 as Mona lineup set to top 400,000 owners](https://news.google.com/rss/articles/CBMigAFBVV95cUxOOUE4d0VVZE5nTXJQTERCMExpV0FoS0lDbXZIdWVfckRLRGZQdDI0cy1zTHNwV3RiS2JGLU5xMXpxWVNEQ0JPZXZmeXludkxXUmFhMXo1MmZaZmZ2a3dSeWNlbzdoMGgycV9uTG1ZVGR2d0VSV2JxTVFTSUJmazZfcw?oc=5) <sub>CnEVPost</sub>

</details>

<details><summary><b>Baidu Apollo</b> (58)</summary>

- 📰 2026-11-22 [中国公司全球化周报｜阿里国际站前两季度GMV增速均超20% / 镁伽科技获近2亿美元融资-36氪](https://news.google.com/rss/articles/CBMiT0FVX3lxTFBsQTVqMHlBdmNaQkZ4TXQ2VTBSNklrbWhsekU3VFQ4TFhnQm1rNkFiT3YxTDVpUE50bmJQVHVKalVHSXFQeDhaUGFpV1V1Rk0?oc=5) <sub>36kr</sub>
- 📰 2026-11-22 [特斯拉在美推出FSDv 15 智驾产业链中长期空间或进一步打开](https://news.google.com/rss/articles/CBMiRkFVX3lxTE0tRk1rNHlrU0ltOFcxVHJ1VGtTRHRIODRfQXJoQjBKZmJVSGkzZUJYbld0NkI3UzNDWUNaUFhNZEtVVW1VWlE?oc=5) <sub>财联社电报</sub>
- 📰 2026-11-21 [APEC期间深圳街头无人车驶入全球30座城市](https://news.google.com/rss/articles/CBMigAFBVV95cUxOLS16MmVLY29WTFBTSFpwWk1xa0NDYlZvOW1UY3hZelZlSHZQNkpPM3hWVENURllxNTdSRk1OUEFLZmpxZHhYQ3FCSVpnN2h0QTdnUjYteGRRYWtFVmZOSTZ2ZnlaelQ3cE9JQ1JSMnFWS1lJazhmT05ORWNuOHZ6cA?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-21 [百度世界2026发布多项AI成果，李彦宏：AI下一幕是“智能组织”](https://news.google.com/rss/articles/CBMidEFVX3lxTFB2QXdyQXJBd0xyTDBIeENlSDVSN0htT1haRWU0NEprc3ZBYlJPTU54ejlFVjBwZUpzc004aGdMYW42NzFrM3V3LVBsX3Z5ZlRXQWNzb0lkd20tdTJuVmR3V2otWHo4NXRrTi1aYVluaXBEVmg1?oc=5) <sub>风闻</sub>
- 📰 2026-11-20 [Google 开放 Genie4世界模型 API，支持实时交互与原生音频生成](https://news.google.com/rss/articles/CBMiTkFVX3lxTE9sLURMU3dDZHJRN0N0U25LV19oWlBvTThkQVI5TzNCVnBHYlFkNUREbzJxYXBnWVV0SHQ2WGRpQUViM0ZKbXpIdUw0Y0dZQQ?oc=5) <sub>AIBase</sub>

</details>

<details><summary><b>Pony.ai</b> (148)</summary>

- 📰 2026-11-23 [Amplitude And 2 Other AI Stocks To Watch](https://news.google.com/rss/articles/CBMilgFBVV95cUxQVmFzWW00a2ltdVRFWmNveFpQc2VzX09NeW1JRWRYWm1kc2I1RVZpNGY3MF84aGtyTkp2Z2FoRTRFeE44ZjB2MFJoZnphTkhjVVVuaFF5VlhRNTd4THgwVUd3WmdEa1lHOXM2Vm5hclpzR2FSNnRSSnJ5NXVvTkdBS3hTTDdaa240QlVzZUU3RWl2My1PVUE?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-11-22 [Tesla Cybercab Orders Open: $29,990, 2027 Push Unproven](https://news.google.com/rss/articles/CBMikwFBVV95cUxQZUVWZXdCQkhLNFVuWHZ4T19oUV9GVDFyZ012bHBHbDBJbWNxX0cwdzY0Z3ZlLUhyTWJ6RHpJQ3hTbzRwQTJ5YU1LRnhwNm1QcjhldjNHZnFpV0I1bC1BU2RMRTJNbWpoelp3NGl5XzJ5WVJ4Ulo1dkVOWmdFd0tvbXJoV3BweGJVN0cyOENDbDJEc2s?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-22 [Kakao Mobility partners with Nvidia to develop Level 4 autonomous driving technology](https://news.google.com/rss/articles/CBMi2AFBVV95cUxOUnMwVTdET0JiaXlkcm83bUZkQUt0TFpJd1lkZG13a1JIUWl3dW81UXlGbHN1Q2Z4VDZGVE5GcFNmeTRsNG1kODJpTTJCclVueHQ1LVFTOTFFWUVpRUpQYmMwc0ZSUHJqN05IR292WVBsOTFUMDl5VldhWUd2UkRfd1NXZ1BQcnI2TFFJdmx1cHN6RFY3aWl0VnppeUxYV2xPWjdZRWRJVzkwWFZ6SWdXQ3FLdTNLMFE5bTRMUkZRRWdlamhhT3ZZNXVOLW5LbnVaX3h6STh2VGM?oc=5) <sub>Robotics & Automation News</sub>
- 📰 2026-11-22 [Nvidia's AI Demand, Alibaba's Chip Pressure and More: This Week in Tech](https://news.google.com/rss/articles/CBMiiwFBVV95cUxNX3hjMW9mc2hoVVBHWmxhVXRmNW01V1BpM0VFRTNJYlhhN3VXby1JVWR4dHhjeEVGMm1EbWZPM3RPQkVxbXo4WHByYmNkQmdBUUJtZFhSZ0pITnVSYWFUaEhkQWlmWmg4cWNmdXBxMmY1cXFNMUFMdDJNQUN0NnQ1cE9iYTM2VkN5azBJ?oc=5) <sub>Benzinga</sub>
- 📰 2026-11-22 [Vectigo launches road-embedded safety system for autonomous vehicles in Colorado](https://news.google.com/rss/articles/CBMi0wFBVV95cUxNbkprNzRNMkRHWnVNRDVfeHUtTHQzOTlTd3FVeHpNS0pXUU4ySTBOUUhHeDlTb1VmUTBHSFZqeVZBQzdhMmplUWlLV3BWVU1ab1BPVENSVHdtUms3NlZIVm5xYlVLb2FRU2RxbXRtYWtnWUVDRXRfallSVnJ4WVJGUmkyVkZtQVB4MXhJMDlqYkZuZlBmNEJiRG1vbVNRUjBRcHNBWmRVWXRmTzdndjlRM2loOUdFdUtQRW5GdjZIOEJQQUJPTXZ5MVFWeXlwR05ia3Nv?oc=5) <sub>Robotics & Automation News</sub>

</details>

<details><summary><b>WeRide</b> (143)</summary>

- 📰 2026-11-23 [How Is WeRide's Global Robotaxi Expansion Driving 88% Revenue Growth in Q3 2026?](https://news.google.com/rss/articles/CBMitwFBVV95cUxOOTZVSEY5VzBhMTBrM1lEWkNRbHpRWUVrRE1hbHV0WUlDQWU0NVVwYzdETS1JdTZVd1ZJNjdaaGRhRTJpSE5iMDBzUVQwTDhuYWZSbnI1T1NKVm1DdmdoNkIyLTV6dHFfZWc1T2o2UFE2WGlZbnhpb0cxSHotQzJzMmE3c29TSHVtLTNIVjZJeFlDN0lzT0NJb1AtSUJncEw5UXg3ZWhUYW9vcF96VzJfUmlacjdYcWM?oc=5) <sub>Kalkine</sub>
- 📰 2026-11-23 [海外收入暴增172%、占总收入近半：文远知行国际化成果持续突显](https://news.google.com/rss/articles/CBMiWEFVX3lxTE5sTkN1aUJXUjVZb0VlRExZVUpzcHVGclhHandicFdGejNJZWhsWXhmUExXRjVVbjFUSXhXQjJoR3luSHBnRmY2RmF6WVlZMEV5NHFHZlBvOVY?oc=5) <sub>驱动之家</sub>
- 📰 2026-11-23 [文远知行执行长称计画在欧洲部署1000辆自动驾驶出租车](https://news.google.com/rss/articles/CBMia0FVX3lxTE1pYklSWmQxWnFwVjJTczI0TzMzS3hGYXF4bDIycDROa2dZUW9SNDdTQlhSQkNoaEFZUzZKWk94d08wUmdZLVRlbnNNNlFyQ0hXY1pjM3lsdjNqR21sUVh5YVJxWEh3MlZtRTdV?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-23 [物理AI数据需求爆发，文远知行AI Infra收入接近翻番，未来增长潜力有多大？](https://news.google.com/rss/articles/CBMiUkFVX3lxTE1tMzFlTXBVZWN0UWNJT0FuQVBxQmdNTDNaRVVyNE5McXowQ0t5SzVldzlkZlhzZGJUcHBVM21wRG9JbjkteFFKX0o5RGlGQVJ1VFE?oc=5) <sub>人工智能</sub>
- 📰 2026-11-23 [【百强透视】绩后股价再创新低！文远知行（00800.HK）盈利困境难解？](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPQUQ4TVJ6WndnUXEyeEpNdXVLN29TSGc3TkxCT2dFMGFpRlZnS1RwMnMtSmFqcDluT1Bkd090WVNnTFo4LXJ1MEI3V3JsVC1KQzA0UUhodFUybWd0bWpsX1ZmQW5qNE1vOHVnU2EzREQxVF96T0hmZWlId1hZZTh1M2NvYlNNaTVG?oc=5) <sub>Sohu</sub>

</details>

<details><summary><b>Horizon Robotics</b> (130)</summary>

- 💻 2026-11-22 [HorizonRobotics/HoloBrain](https://github.com/HorizonRobotics/HoloBrain) <sub>GitHub</sub>
- 💻 2026-11-19 [HorizonRobotics/LoFT](https://github.com/HorizonRobotics/LoFT) <sub>GitHub</sub>
- 📰 2026-11-23 [方盒子造型想要激光雷达和高阶智驾：旅行者7对比iCAR V23、哈弗猛龙，油电同智怎么选](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBTX3A5RDNCc1Q5dFgxSjJRVkdrb2pfSUJIY2t2Z2xMTzRjOVN0U01kc3hNdmdHeVZIOUdCSWJ5d1FWSVJ0ZWMwUDBES1VNdmpCamNROXdHSEJBN0hWZUFR?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-23 [三款方正SUV智驾横评：旅行者7油电同智，猎鹰500和华为乾崑ADS 5怎么选？](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5WMFhXQllIc05aNFF3MWRVYUR6TS1jZk5jbDhtYk4xRnZSMFRqV3pTTjdtbzQtS0M1NVN2dlFWQkNOZWJNOEl5eG5pdnh1Q21mcVY1QkpyalhXM29SMFdN?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-23 [【视频】24K金车标！蔚来ES9地平线鎏金特别版开售，十周年排面拉满！](https://news.google.com/rss/articles/CBMiW0FVX3lxTE54a1pqTzlMQ3g2VWtaN2xvSEVSRzlMd0hhWDRSc2ZWeHNaV0MybjdZejFZTS1zcWp2ZFRjWnRsQWhNdnNEeGFGT0FfRVo4OFcyUFpicG96bnVwQ0k?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (24)</summary>

- 📰 2026-11-23 [【视频】#奥迪E7X用车日记# Model YL和奥迪E7X 我为什么选了它](https://news.google.com/rss/articles/CBMiW0FVX3lxTE0xXzI3eHc3Y0NkcVFIQk5FcWdFMzZidmtYTm1oWlZFamVaSDlRbk5obWlYQzNfMzVPc3I5VzA5Z1BRWU5nQmplWUw1TS1QR2ZlZ19COWdYNVg2bTA?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-22 [元戎启行\|ICAR\|地平线 - 智驾大赛办了好多次](https://news.google.com/rss/articles/CBMiY0FVX3lxTE52Q055UnNJRUJqYmc2dGtmS3BVVUVqajduOHg4YnhucUlwSkx1REZFQjY0Y2dUcTl0UzNTM29nYloxRkVRQXVDMVNER2N0My1DenhxUUpLYWxiWFNjSGtTbjYxbw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-22 [巅峰对决松山湖！k8凯发入口官网下载入口2026圆满落幕](https://news.google.com/rss/articles/CBMiUEFVX3lxTE9YQXhzRFRySlFzc0h5eEpZZXJHekZ2bjZFZ2pma1hSdHViR2RHYlNVTjJBaFFEUFhhNzd6MEgwODQ1SlFydU9jMEt3UGJFaUly?oc=5) <sub>iheima</sub>
- 📰 2026-11-21 [【视频】3分钟看懂特斯拉Model Y L值不值得买？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9VQU9UWDByVEt0TnRIcDk0Q2RQTDBzWU9JRTBqMUtKMUgwTGsxNWNTc3k4OV8wQ0hfUkh3R0oxYm51S1ZRSzJLRlR6NTU2XzFhMTVRMG9MNlRCSVk?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-21 [购彩大厅～welcome手机购彩公司的校园体验报告：不拼参数，拼场景与协同](https://news.google.com/rss/articles/CBMiT0FVX3lxTFA5R0pUNmlUbUtPNW1KR19EdDlnd3FocHQ2UnZHdUM3Q0t5WkJod1B6emt0bFg4YnhsdUhWYUk5M2t4WVZlVW91TUYzS1plZ1k?oc=5) <sub>iheima</sub>

</details>

<details><summary><b>Mobileye</b> (14)</summary>

- 📰 2026-11-23 [Musk Says Cybercab “Would Win Even at Price Parity.” That’s a Problem for Uber and Lyft](https://news.google.com/rss/articles/CBMi5AFBVV95cUxQeW1Zb3BkMkFhT1p3NnIyVW9kX0xhU0p3Z2preUZSR3FOVm01V3lSOFlNM1dSbHJyWU51WmJLUkxtWTY1ckRHLThvNnJvZ0FTaFdXazVSQ3JuZEhHU1dYN3U4cEszSXNYdnRPSFpNZzl6a2E5MGtPWDhKZFRtUDV3Q0ZRcDRweWdPdTlqcVotaktSeUJtOG5Jck10MzNtTlREOE03a29CR3BmWkxwcm9XbC1xa0d1Yy0ya2tyWkM3NFdDTUxYUWtkTkpVU3lFV2NpYS0xSkoyOTZUU0lDS3ZZZHh5SFc?oc=5) <sub>TIKR.com</sub>
- 📰 2026-11-23 [Robotaxi Market to Reach US$198.6 Billion by 2035 as Waymo-Uber](https://news.google.com/rss/articles/CBMioAFBVV95cUxOOVFHa1QzX0FoWEhodlVoV2tBekhIb245dmxkLTZBSTJyYVBuVU5LQWg0WFVtLWFIU0c5SDc4cjRTRVlJNEVXemxRQmlhTFhDTVEzb2JwcDVzZDZHNmRlN3BUTnZuTzFjSGFLNjhEb1J5RzNqVXV5cW91d0FVVjdKYUV0OEF1ZjlFM2VSQUNUSXQ2X1FUYmFLZ1VLbXFOdXly?oc=5) <sub>openPR.com</sub>
- 📰 2026-11-21 [3 Penny Stocks With Revenue Growth Up To 56%](https://news.google.com/rss/articles/CBMimgFBVV95cUxQNThVYk1RYkI1YkNMVi1JN2FWaG5fdjFHNVZ6bEVBNktGSURBeEd3NHh2dEVmSk5HRXdzRHdLd1NsdU5vLWJfTzBhaHVvWmw5SGZPandLZUpqc1NreFkwdUlRRllqOHpEcmVXRHJpZU1fSnhGdjNlblgzU2ZoXzh5RFNnNDlqVEFNd0R6TFJ4MjNEdkNORHUxaUZ3?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-11-19 [Growth in the Adaptive Cruise Control and Blind Spot Detection](https://news.google.com/rss/articles/CBMinwFBVV95cUxPa0x3SFRDX194b3VtTHJnYlJPNEZzRHNpRHd6RS1JOVVkWnBBMnZxQ1AyRjFpUWdVSDBuZHdVdUdFczFGbUVMSFlhdU41UmYwbmhzdFlDaGhvSmptUzNSYzktbGJpRG96ZmZvQ2ZHY3Z3aUt6aWV4WFJzLXctV2k5dFoxVTlta3YzSmNkZGxBRmxYdnlLQ1JKV0RFOWxVcjQ?oc=5) <sub>openPR.com</sub>
- 📰 2026-11-18 [Intel Cuts IT Jobs as Tan's Cost Drive Extends Into Year-End](https://news.google.com/rss/articles/CBMidkFVX3lxTE9XMEIyWkJScF9ld3AzQXYxN0hhaFJQWnJ3czJVOE9FelQtbG12YUdoWkZmZW55cWdQamJlSnRGQTF4bWVDNi0zRFdfZ0hpVkJFNThWdmYtWDk4WGRBY1F5dWFrRklNQjNLUU1UVUQzakRvUFZhYUE?oc=5) <sub>BigGo Finance</sub>

</details>

<details><summary><b>Aurora</b> (38)</summary>

- 📰 2026-11-21 [Bot Auto launches ‘Capacity Grid’ with agreements for 200 million miles of driverless trucking](https://news.google.com/rss/articles/CBMi4wFBVV95cUxNenB0d0xhRHB1QW96VjM5dl9yODU5THZxLWtmZEZ1WEc0TGZhQUlDOU1CdlNiR0Flc3ZoTzAyUnVoaEtOSUp4NEVyNXpqVi1vZldPNUY5VXRKUU5hc2xjVm9aZDdiN3R3NE9mUmVtajF0dG1hM1dFTmtJWWVwakMzQ095TjMxZU81VThwYy15T1FaaTJNN3ZEc1BxcDhCX2xjMDdHQ1pxRVNNaWloSUdTUmxkRkt2TUxNdGd4MTNEU082RnBxcUtxV2paVWFEeEJ0Z2t1SWJONG1jTDZIanM0N1QxNA?oc=5) <sub>Robotics & Automation News</sub>
- 📰 2026-11-21 [NADAQ: AUR Investigation Alert: Kessler Topaz Meltzer & Check, LL](https://news.google.com/rss/articles/CBMisgFBVV95cUxOcUdtQkRtc2tPZkc3dTlWUnJ5YjVRZ2xBV3d2RWxTUFU3QmZPV200dlROY3N1R3Q1S2t6dHItRVQxUU1YNFhzOFNtVzVCWEtxVDM4V2FBblhFTE1oTGo1NWhxUTh4SXFEWXVfZmphc1RNaHJVa1ozMGRfYlZoaUtxUlY1b3FONmZmS3hkLTZjNjZHTWtUalM0OHlRQ2hRa1QxRS1WQkd4eHRYWDlzb213amFB?oc=5) <sub>The National Law Review</sub>
- 📰 2026-11-20 [AUR Investors: BFA Law Notifies Aurora Investors with Losses of its Ongoing Securities Fraud Investigation](https://news.google.com/rss/articles/CBMiiAJBVV95cUxQVFAwZ0VhZEh6UWFhWXV0RXdxNk1GV3V1ZEpGeUh4cG5tc2Z6aWxVM0hvMUFtUlhTXzdkTENzU3U0S2ZsTC1OZmVlVDNXdS11WWF0VzJUeFBZcnR6NmYzd1JNZ25HLWo5TE1yNmd5TXo4NFlxRTRFSFdSQW1Ka0h3b0JZd2h1LUY2LUxwbWtXX0U2NFh5QmxPNzBDOHIzRG5yQ3J4cVl5T1JxV05SaG5qYWZxekpYbVd0Mk1GdHpmREplRlNpVE5Eb0VpUnQ2b05TdXhLdjhKeEh1Z214VWN6Nmd3WHRFd1lyYVFhQ0ZicXYzdVY0b3owNmRpTHlycHlLU1ZGRl9UcUM?oc=5) <sub>GlobeNewswire</sub>
- 📰 2026-11-20 [Elite Penny Stocks To Watch In November 2026](https://news.google.com/rss/articles/CBMiigFBVV95cUxNajdPRWw0a0VnR1ZtU1l6ZnMxT0tTNERicGw1cGpYdDJBVUE0UW9UZkJ2VnpkeXpzODJEamNwa0FNNWctUlZicFVUYmJtWnBzMGRRWkZ5MXNwY1U3WEZJX2NKdFd2ZEpzSHNZRUpPa3ZsdVozUVpmcXIyNU9FcGx0c0xtU21Mb2R3dEE?oc=5) <sub>Yahoo Finance UK</sub>
- 📰 2026-11-20 [AUR Investigation Reminder: Kessler Topaz Meltzer & Check,](https://news.google.com/rss/articles/CBMiowJBVV95cUxOazBaMjVSWHZESFowVURkVVg1NURsOVhELWtUYjlWM0ZMZGIxNVNXeUtsMk5USFFQemRXcUdObEdUQjBUTjhwNnJvZVNzNmRERHRsOFViVFJ5NGtNdnVvLWF4emk1MXJyZ3F1LUFqOWk2d2pjN3JlOWVQdGdoWFhUM2ZOQ2xja3d3d19rZFZGdHd2TWZpQngxUTYta2FJVWo0RlBuYjFOUXplSGpqNkxEcjZyRlFZNmMtWDNreHF1d2ZMb0xxNGJlT2lDcVFnMHg3Y1Izb2hNcVh0NFRmYTBIcUt2Z08zWWdkTlJwSlpnTHR2SEJDdWNUeFUwY0RGUWw0c1E4aVVVdkowUjRVektKT3NPMTc5Y2pRRkhXdUdLbXBNZG8?oc=5) <sub>GlobeNewswire</sub>

</details>

<details><summary><b>Zoox</b> (107)</summary>

- 📰 2026-11-23 [Zoox Cleared July 30 to Charge for Wheel-Free Robotaxis](https://news.google.com/rss/articles/CBMikwFBVV95cUxNZlNkY2VoTDAtMFNkS1NZYnRKcnhhS25wQjBuUU1kLWhOZXVQYkZiSFVmT3FyZkJMdXJ1NHEyLW02d2dHYmZFd0k4SzZTaWozOFZrSFAwVXI1NXRGc1BtTlhiajVwMmtQUDR3cElxX2dkVFlZMmlnb2hmVXQ3TnpaUFhfZmFySm1mOS1UUHRpQ0lfRU0?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-22 [Zoox Can Start Charging For Steering Wheel-Free Robotaxis In Las Vegas](https://news.google.com/rss/articles/CBMidEFVX3lxTE5KdXlvTWstMi11OWlnWXpFQzBDMllTTWtrVzJqTWM3XzdoeW1xU2s1Y0hDWEdwY1hwYzlwcVZBX2tRNmVRMGdpV0JSLVNVZ1ozVnRzcG11VXNpZ1FkNXRrc1B5TEFnWXFiN21jRFZkTGJueTJN?oc=5) <sub>Motor1.com</sub>
- 📰 2026-11-21 [Zoox Launches Robotaxi Rides for Employees](https://news.google.com/rss/articles/CBMiogFBVV95cUxQYm4yZnUtR09RSTNvX285QXlVOFlzbGNYRDY0Sm4zemVGakJUcDhtQmhMdWxFNXBPUHpFak43MzhtX0ZidXl2TkRyendFRzFXemctR25fNk1uRnhVc1lTbGJabG1nX1ZLUU9ZclhEd3lPUUlqakw1QW5ZRHVra1J6ZnJrNVZYMVhnQU1xUk4yeU81MTI2b3pnYkVCNlpBT3NoS2c?oc=5) <sub>Wisevoter</sub>
- 📰 2026-11-21 [Waymo announces two robotaxi recalls as closed-lane software fix remains unfinished](https://news.google.com/rss/articles/CBMiwgFBVV95cUxNXzk3UHRGSjRZdU15TC1mNm9NLWxxNVg4LWFtZUdReTlENWszWmxCLTFEMzd1Z29RNkpEcFprd3NjTTROUkhPSkhsdkhCWEQ5azJVakdxeGhiTUNxalVTTnhZM1ZyallJMEZ1akdYZ0FFVDFQUWl3a0FSMWx0czV4cGg5TnFUREgyaG9BX0FybTRWY2lfaE1GRlVibVRUNUZ3RHJVUC1jbTdWWDdhZVY1dUlfWGpDMVJqYjJKaENENVZZQQ?oc=5) <sub>Business Upturn</sub>
- 📰 2026-11-21 [Zoox launches its first robotaxi rides in L.A. County](https://news.google.com/rss/articles/CBMiowFBVV95cUxQeVpseUpWdjdRQjZ4YUUtaUNRdzB3ell5ck9zNHZWYVAxc3BKdVFMS1l0WkcyVXY4Q0d5a1M1dUJZYllxNkNTalppWVBNQURLN284ZVNraW9RU0ZNWnlQVFBGc3BpaVR1N3VjOWNDdGRTZ2ZYRVdtTXJteUlqTUthLXhOMVNwXzNKay1YNkR0aDNYYzFEVGZXY2szeDVEWjJhSXFr?oc=5) <sub>Los Angeles Times</sub>

</details>

<details><summary><b>Motional</b> (28)</summary>

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
