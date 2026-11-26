# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-11-26 · 1,327 papers tracked · 49 curated.

**Selection rule.** A paper is listed only if it (1) is primarily about autonomous driving,
(2) has public code, and (3) shows at least one strong signal: accepted at a top venue
(CVPR / ICCV / ECCV / NeurIPS / ICLR / ICML / CoRL / RSS / TPAMI, or ICRA / IROS / AAAI / RA-L),
≥200 GitHub stars, ≥3 citations / month, or a well-known lab with traction. Papers are then ranked by a
composite score (venue, stars, citation velocity, LLM rubric for novelty / rigor / impact, SOTA claims)
with a per-topic cap. See [`scripts/rank.py`](scripts/rank.py).

📅 [Daily digests](daily/) · 🗓️ [Weekly digests](weekly/) · 📦 [Raw data](data/)

## Contents

- [VLA / VLM for Driving](#vla--vlm-for-driving) (14)
- [World Models & Generative Simulation](#world-models--generative-simulation) (5)
- [End-to-End Driving & Planning](#end-to-end-driving--planning) (13)
- [3DGS / NeRF Reconstruction & Sensor Sim](#3dgs--nerf-reconstruction--sensor-sim) (5)
- [Perception: BEV, Occupancy, 3D Detection, Mapping](#perception-bev-occupancy-3d-detection-mapping) (7)
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
| [Teaching VLMs What to Say, Not How to Reason: Rethinking Counterfactual Reasoning in Autonomous Driving](https://arxiv.org/abs/2611.24376)<br><sub>Hayeon Oh, Donghwan Lee</sub> | NeurIPS 2026<br>2026-11 | [⭐ 3](https://github.com/OPhD-hahao/Rethink-CF) | End-to-end autonomous driving systems have been shown to suffer from shortcut learning and causal confusion, limiting their ability to generalize robustly under distribution shift |
| [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)<br><sub>Yuan Gao, Wenting Miao, Mattia Piccinini et al.</sub> | IROS<br>2026-07<br>📑 1 | [⭐ 34](https://github.com/TUM-AVS/Chat2scenic) | Validating autonomous driving systems requires diverse, regulation-compliant test scenarios |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 25 | [⭐ 563](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
| [GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives](https://arxiv.org/abs/2609.39601)<br><sub>Qize Yu, Lianrui Fan, Boyu Chen et al.</sub> | arXiv<br>2026-09<br>📑 5 | [⭐ 444](https://github.com/groundingpi/GroundingPI) | Precise grounding matters |
| [GRAVA: Grounded Reasoning-to-Action Representation and Learning for Autonomous Driving](https://arxiv.org/abs/2609.15169)<br><sub>Xiao Liu, Haoyu Li, Jianghao Leng et al.</sub> | arXiv<br>2026-09 | [⭐ 488](https://github.com/AhernResearch/grava) | Driving vision-language-action (VLA) models increasingly reason before acting, but their intermediate reasoning is often weakly grounded in physical scene evidence and loosely connected to executable behavior |
| [Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air](https://arxiv.org/abs/2605.31066)<br><sub>Tianle Zeng, Yanci Wen, Xueang Yu et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 1,144](https://github.com/louiszengCN/CarlaAir) | Recent aerial vision-language-action (VLA) models show promising single-UAV capabilities, such as tracking moving objects and navigating to language-specified landmarks |

## World Models & Generative Simulation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Orbis 2: A Hierarchical World Model for Driving](https://arxiv.org/abs/2607.15898)<br><sub>Sudhanshu Mittal, Arian Mousakhan, Silvio Galesso et al.</sub> | NeurIPS 2026<br>2026-07<br>📑 2 | [⭐ 32](https://github.com/lmb-freiburg/orbis2) | Current world models operate at a single level of abstraction, with most prioritizing perceptual fidelity while lacking the spatial reasoning and semantic understanding required for real-world downstream tasks |
| [FrozenDrive: Zero-Shot Text-Guided Driving Scene Generation and Data Augmentation with Parameter-Free Frozen Diffusion Model](https://arxiv.org/abs/2606.20110)<br><sub>Yuhwan Jeong, Hyeonseong Kim, Daehyun We et al.</sub> | ECCV 2026<br>2026-06<br>📑 1 | [⭐ 9](https://github.com/daehyunwe/FrozenDrive) | Synthetic data for autonomous driving is surging, powered by diffusion models that promise scalable scene generation |
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
| [AutoE2E: Don't speak - Language free end-to-end autonomy for L2++ ADAS and L4 Robotaxis](https://arxiv.org/abs/2611.22374)<br><sub>Muhammad Zain Khawaja, Zaynab El Mawas, Ryota Yamada et al.</sub> | arXiv<br>2026-11 | [⭐ 234](https://github.com/autowarefoundation/auto_e2e) | AutoE2E is an open-source end-to-end driving model developed by the Autoware Foundation Robotaxi Working Group |

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

- 📰 2026-11-26 [Waymo Passenger Finds Loaded Handgun Riding Shotgun In Autonomous Taxi](https://news.google.com/rss/articles/CBMipwFBVV95cUxNLUZGbDRkaWljWl9TNVBKTXRweThYWS1Nd21pTUNSaVRzRzNQU1hjbTVUcWM2dXJWWnR2M2VNd1ZtaWlPQ3U5YnpDblBzd3R1azUyWkltZE0xM0UyZmNNRHR4ZG91SGpaYkNlLU9QWmxLTWZ5aGtvVjg2UXI2a0R3dkZlUkVlRU1FcEZ6ajNWeXh5Tl9VYjhfRmdhMGJyeDJiUjhiQ19QVQ?oc=5) <sub>Newsweek</sub>
- 📰 2026-11-26 [Waymo avoiding flood-prone areas across San Diego following historic king tides](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQdXVzM0VJT3JNcV9HYmlERVMyUFhLcTU0VnZoODc5YWxwY2VOaXJNbTVOX0Z4N1ZqVFJUVmNTVWZrRU5tczJ6d05jaXNXVkowV0dSNmx1bTdxczNubDVROXRtY1o5cXdZMXRpU2ZlcGlUZXFsSUQ4ckFTVm40b21iTEp5TDlXU0VUcFZV0gGQAUFVX3lxTE5pbm9YZ21XUmZGLWJGc0Y2dVV1dXpPRVEzQmliUGRPdElVdjMyTVBCVXI1VHg0STZZXzVFRDZCUUdFSmFiLVJ2dVplQXpaTDFSVE9mTlFwR2wwMHlibVJBdVVqQW1QREhIMTNaRkFQWEpiRjhFemN5Mms4Um10MnVzQy1mM3VNZEtOazRJX0lEdQ?oc=5) <sub>FOX 5 San Diego & KUSI News</sub>
- 📰 2026-11-26 [Waymo Says It’s Reviewing Customer Service After Passenger Finds Loaded Gun in Robotaxi](https://news.google.com/rss/articles/CBMivgFBVV95cUxPbTR6RlR4N1ZwbkwwNmdhWFR0RTY3YkVoaFEyYWNhaEJuX2ZGLXkyRk9PWTVlV0I1T182MzBITXg3YmZWSU93cUY3eENWQ0hBNXhySUZybEtwbEhhanNYR2xHamg5bVlxQVVXNTFET2g4QXByLUd3RDZDRjFZc18zak1NVGFZVG1UaGZsVVBab3A5QzlFYURySngtUjlTc3BuT0V3VHVZbWFseXlpTG5OVDVsYjZway1SNkxfUUJR?oc=5) <sub>KQED</sub>
- 📰 2026-11-26 [Tesla's Robotaxi fleet just pulled AHEAD of Waymo in Texas. And it's adding Cybercabs by the HUNDREDS. The numbers? 1,507 vehicles registered for Tesla vs. 1,390 for Waymo. Tesla added around 200 Cybercabs in one batch, helping it take the lead in th](https://news.google.com/rss/articles/CBMibEFVX3lxTFBsZGhad2N2Z3NmSi1Mcnloa1labzhTX29iWjJId2NGNE1PTG1yQ2x6N2VXb1dIZG5fRWx1NXRmMzhjR1JUVUw5dmJjT2Y5c2VCTXRqRXJQOW1VUloybFhyb2hJUzNreTRPd1EtSQ?oc=5) <sub>X</sub>
- 📰 2026-11-26 [A Waymo passenger found a loaded gun in S.F. robotaxi. Then things got more complicated](https://news.google.com/rss/articles/CBMibkFVX3lxTE1fYVZZMkN6MVJhRWM0QnZlSlh6UDRDaWw4SWY2NjNrRzF6ZGlkclpPZ0NSOF9NU19YVUV6X2RuaFZKUVNmNXZxcVBZNnFfR3lwWXpCMDBqdTVmMTVUR2ZYNHRtdHdwOFZuV1VFbVZ3?oc=5) <sub>San Francisco Chronicle</sub>

</details>

<details><summary><b>Tesla</b> (387)</summary>

- 📰 2026-11-26 [Tesla's Robotaxi fleet just pulled AHEAD of Waymo in Texas. And it's adding Cybercabs by the HUNDREDS. The numbers? 1,507 vehicles registered for Tesla vs. 1,390 for Waymo. Tesla added around 200 Cybercabs in one batch, helping it take the lead in th](https://news.google.com/rss/articles/CBMibEFVX3lxTFBsZGhad2N2Z3NmSi1Mcnloa1labzhTX29iWjJId2NGNE1PTG1yQ2x6N2VXb1dIZG5fRWx1NXRmMzhjR1JUVUw5dmJjT2Y5c2VCTXRqRXJQOW1VUloybFhyb2hJUzNreTRPd1EtSQ?oc=5) <sub>X</sub>
- 📰 2026-11-26 [Her Tesla Model Y Saw the State Trooper Before She Did, and the Owner Says That One Moment Made Her $99 FSD Subscription Worth It](https://news.google.com/rss/articles/CBMiugFBVV95cUxNUE5HM1lmMlkyblE2dnpuaU1tbmRWSTFQdlpWS2pMcWdBQ3VzRnlWQ1EwUXpUVURmcm91THVUOVRBbm5ZdmxKLVZBSklmSGE1MElEcTg1TklMUGJpOGFOajJUUEZucl9pTWdYVVlUMXpUYkZ5bjljazRpWkdYM0RaQUhTaFZ1WTRNRUhHNHcxdWdRd0hKMjd1QTBXeVFsQ3ZIb1UtUzAxX09qb24tcGVPclAxcEZwRkFqMFE?oc=5) <sub>Torque News</sub>
- 📰 2026-11-26 [Tesla Falls 5%, Sandisk 13% as EU Delays FSD Vote](https://news.google.com/rss/articles/CBMinAFBVV95cUxQSlZaeUpvamI1Nl9Ibzd5dGZNSVJkQnBBNHQwazBpbFJwbjhDV2d6aVNEWDRFVTQ3cUVZOS1DaW1tdHE0WEpBdVhKaWNzQXd0M0NSNDBkY2FzR1dWY3FzZmJFY1dkMHQ0cTNUVi1Od05vVTQ2SmVoaHNXUFBqcDNXZWVLZnlra1NfdnhTemttQzRyWGs4ZEdzZmRhRDg?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-26 [2026.38.6.11 Tesla Release Notes](https://news.google.com/rss/articles/CBMicEFVX3lxTE9jS3pEbXJ6WU11Z0VRM1AzdXVrVXNvckhrdFI3TWNRa2ZqTUtRV3dfQV91RURHaG1kS0FicUx5NzRnUFhSVUN4MUctRU9nWEF4UGRtNkJUYnlmYXpYVV9XU2Vtc2M0RUZhNnRBM2lRUGI?oc=5) <sub>Drive Tesla Canada</sub>
- 📰 2026-11-26 [Tesla FSD v15 AI4 compute: Musk's half-TRIP claim](https://news.google.com/rss/articles/CBMiigFBVV95cUxNY3J3YkRYN1A2SW1kYUFSeTRYTGpYQkhDMkNDZHd0dzNlaTYtWkNfSXVST1gwdGVxR3NzSzM5Q0tJVWltZWhoazZlT01RXzZlb3U5Sl94b0d5dE9rS1htXzBzbWgtcTlMWTRtc2paWDRhLUR2alp1a0k1b01tSGZicnh5cUR2aUkydGc?oc=5) <sub>NeoTeo</sub>

</details>

<details><summary><b>NVIDIA</b> (231)</summary>

- 💻 2026-11-19 [NVIDIA/nvidia-linux-utils](https://github.com/NVIDIA/nvidia-linux-utils) <sub>GitHub</sub>
- 💻 2026-11-16 [NVIDIA/scadactl](https://github.com/NVIDIA/scadactl) <sub>GitHub</sub>
- 📰 2026-11-26 [VIDEO: Tariffs, NVIDIA and fears of AI bubble drive spike in market volatility](https://news.google.com/rss/articles/CBMi0AFBVV95cUxORGlCY0JQd2dHZ01Tc0tieVN4cFZueHZSaTdhVG1nZm5lb2FldjhWdkg4Z1FvanVreEd3MUdVNTBTRFdCWjZwbXhTbVV1U0h0ZzZVcXptTVZfSDFXVmNJbk5ZQl9MRi1nN1pwanRuNXlpWnZtaTUtelZrSmpQSERmSG96UXdxeHpWSFpLQzZBQndPaDFiR1lueHhEVUFDOV9ab1NJOWJiSF82N2JVSlh0aXhPcVdyUXI4eFl6VElYR2Z0R0tEX0hnOFIzUUVFN1pL?oc=5) <sub>ABC News & Headlines – Australian Broadcasting Corporation</sub>
- 📰 2026-11-25 [Trump’s China Hawk Act: How Nvidia and AI Profits Drive His Policy](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBkaDFQQWxLazNqYkZ3TWxxTVFHOVZ6N2xKOWFrNHFiRjVLOGZpWUZEaTRBSTVBampRMXR4U3NBSG9kaTMzc2wwQ1ZlUTRNYUFrWjZFdXB0czhuSURMX2Zr?oc=5) <sub>Savage Minds \| Substack</sub>
- 📰 2026-11-25 [Run NVIDIA Cosmos 3 Nano Locally with Hugging Face](https://news.google.com/rss/articles/CBMivAFBVV95cUxNRG1zZVloSnhtYzV1LW1lS2RTMTEyOXFfTTl3OGhnVl9TWGJ5MnFzS3R5N3gtRE5BZ0xsYkthaXhsczJmdTB6LWpSSEZsRU9ZQVhaN0Rod2hqMG1ZM1VYbHRkZ1NITXZNUmZrNF9UN2dCS2dHYTE3VFNZSlR2c2EzM0RsLW9SbEVlQnQ1M0w3SU90LW1iYlVyVU1IeFNtY0NnMXdkZFVRTGhxd05oMk4tdjZ5ZEl4Mkh3cXR2bw?oc=5) <sub>The Chenab Times</sub>

</details>

<details><summary><b>Wayve</b> (31)</summary>

- 📰 2026-11-23 [Autonomous Driving Software Market to Reach USD 6.78 Billion](https://news.google.com/rss/articles/CBMinAFBVV95cUxNZFVjLThIaVVwbm1rWlBYT2IzMDFFZEF6LWVzaWY1YTR6b0JLeDBla0VacjF0dEtpQjhGblZpVjUyZV9ZM3lSS3UwdFdtYmp0dm15SzdBZnpEemNqMlcxMXZ4TnVDV3FqZjNCOGdWNFhBRGFUWVNlV2poZHFkdDA1OEY1QlZaZzZ6Z09QQWtTRDQ5WGxyV2xmbEtxOHo?oc=5) <sub>openPR.com</sub>
- 📰 2026-11-23 [Mercedes gets edge over Tesla in race for self-driving success in Europe](https://news.google.com/rss/articles/CBMihAFBVV95cUxNREhrZGszRlNBUzFxbjBURFBhQldOMDFiOGV0TVNMWWVuYjA5dFdCTGpGV0RCMlJJczEtWkd0eG9YRnkwZnFVTFRseC1iT1lBM2w0LUlUVFhqdk1ydU1vWDRPVGZfTlE4SnRSRnZZTkMzVzdnVFJTM0dobnRKRG1jOV9Yb0w?oc=5) <sub>Financial Times</sub>
- 📰 2026-11-22 [Kakao Mobility partners with Nvidia to develop Level 4 autonomous driving technology](https://news.google.com/rss/articles/CBMi2AFBVV95cUxOUnMwVTdET0JiaXlkcm83bUZkQUt0TFpJd1lkZG13a1JIUWl3dW81UXlGbHN1Q2Z4VDZGVE5GcFNmeTRsNG1kODJpTTJCclVueHQ1LVFTOTFFWUVpRUpQYmMwc0ZSUHJqN05IR292WVBsOTFUMDl5VldhWUd2UkRfd1NXZ1BQcnI2TFFJdmx1cHN6RFY3aWl0VnppeUxYV2xPWjdZRWRJVzkwWFZ6SWdXQ3FLdTNLMFE5bTRMUkZRRWdlamhhT3ZZNXVOLW5LbnVaX3h6STh2VGM?oc=5) <sub>Robotics & Automation News</sub>
- 📰 2026-11-22 [Nvidia to Continue Robotics Investments After Huang's Departure, Assures Portfolio Companies Directly Under Interim CEO](https://news.google.com/rss/articles/CBMidkFVX3lxTE1IbWJob3hvWTZuUDRrRXFpZ2phdjVSWllyTmpLN2VSMlR0MV9NaExQVjJ3cHdlVUQ0czI1Y09HM256ZWY4QVhUZ3VLbUFBSTN1RU1GLVdENTdIcmNvSzlibnluYTlHUFc3b2M1TGRWTjNTeXNNZmc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-21 [California Bans Waymo Robotaxis From Motorways](https://news.google.com/rss/articles/CBMilwFBVV95cUxQSnRJcXd3Z0dtS3FZTzh4cHoxclA2Unh0ZWRwZTBKbVZxd0VBSEtOUXBQVWduZjFyMmtfOTdoQldVMUlGQWhtenRwRVNnOElQamx2V1lXUEFINGxrV3FQYUVFTHhWcHhFVmRkYUxDbGZoa2d5VWItS3BFaDBBSklVakFnSlFIOEMzcXRuSWxnMlkzQzNyWGFR?oc=5) <sub>Wisevoter</sub>

</details>

<details><summary><b>Momenta</b> (120)</summary>

- 📰 2026-11-26 [新款奔驰S级曝光：一体式超联屏与Momenta智驾](https://news.google.com/rss/articles/CBMia0FVX3lxTFBxMDFsSERHVVFVSDBHNGM0b2JXTVhMc1BkZ0I2N1NBNzhvdWdXZ3NraHEyU0dnb1ZJS2NnNHA5UVVNNERINWxZZXplcktBejBBWEhJR3hBSUY5Tk9FRVJzcTJ2ajJ5QW53c3g4?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-26 [艾尼氪V的智驾到底行不行？Momenta联合打造，3个维度说清值不值+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE91M1VlZ0NCRnFfYW1DXzc0Tzh0YmhldGpzLW5PWFpaMFhZdlp5aVJKUjRlNjhVSVBDNW16SnRnM0lFTlhxVGZ1UFRnYlJsVXY4VXFkUEtpNE5FN044a0l3?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-26 [电动化后宝马还有味道吗？这台新3 系在赛道给出了答案\|Momenta\|广州车展\|宝马\|新世代BMW i3_新浪新闻](https://news.google.com/rss/articles/CBMiY0FVX3lxTE01Y2UyY1F2VS1Hd0ttYWJIYVJRVTBwcS1QdEctdXpHRjJQenRaREpmTFF2QklyaHMxYWlVS2k1RHlMTDVIRkNEZ0R2b2JEdmdZTFFmTFVPZE9UQ2FkaXp1amFMWQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-25 [宝马新世代首款车型BMW iX3上市交付：26.99万元起，800V架构+ Momenta R7-yeeyi](https://news.google.com/rss/articles/CBMiggFBVV95cUxOY0F1QjBVS3JaTlhtZkxSZWhCWVNYVHFmUWdjbktBZWJTSGJXcWQyUjZ2NUQ5Z093bzM1ZjFmX0xxaUxaNEFJb3J1UG5jdHZWdkhmd3IyblBoNWtpLUFrajZkQzBoVl9NVlhFNWYwbnJ4QkdwY3hMcHJOeHRPaUlqNWlB?oc=5) <sub>yeeyi</sub>
- 📰 2026-11-25 [凯迪拉克XT5插混版智驾值得买吗？23.99万起配置分水岭+3个维度说清+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE9lX1pIR3hpbk5DSWFDN3Nwb18tQU9jMTdrNHNnX0w5dEpqMzRXbEdjUFZGTGdUMDZrLXhYQTkxejRyNERHQjJwb2k4X0ZjMWZXS2pibGEySUU2Q3ZmR0dfMU0tVF9OYloyVzZYR1pNMGluZw?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>XPeng</b> (257)</summary>

- 📰 2026-11-26 [XPENG Achieves New Milestone in Humanoid Robotics as IRON Brings Human-Centric Intelligence into the Mass Production Era](https://news.google.com/rss/articles/CBMiiwJBVV95cUxNR1NMMnZkQzMwdEhvQ2kweXlNT05aRW9JQlo4TXVVd3lWWV9HU1NqNVpHSWpwdFFBTGJBczVDVWVZVGhjYk9mdXJuNGI2VURXRzFPRnlUZHVpOENKUG5QNnNmSTBnTURES0QydXlkSjJ5RjVDaDJ6TmRoT293eFhqRy1vd1RvZXBBZmhoY1hoaThDSFJsWWU0S0lBMjlxcWZUUDFUSFo5ZjQ4RjhwbzVuNUFiZXoxa0IyTzh1bXE2ZTQyYUdNZVZ2Z0pyMi1rd2lfNm9tLW9lclphSkl0Yzhzdk1SeEJNclhpV1BOTmkwSHU1ZmwtTzVINndhaE1VUlJRZzFUaGU1VUM3Mmc?oc=5) <sub>markets.businessinsider.com</sub>
- 📰 2026-11-26 [Hong Kong Stocks in Motion \| XPeng Group-W (09868) rises over 4% as XPeng launches L4 autonomous Robotaxi services; custom models scheduled for release next year](https://news.google.com/rss/articles/CBMinAFBVV95cUxOTWpib3RWVkRDR0NqeUhucW1YN2JHSkh6cXY3RUxQY2hpV09rbWtQQU5BNVFybEZkT2dKenRFNkVJNzhlUktVSG1fOVFIMWc4Ym45eGNFNGoyVWtvdHh4eGk3dEFfbHd6OERTQTg1V2FOWkwyZURyT2hBeWlnWXF1VWtrOUlSTXVKeGEwOTBUSk5razdnd1l5czB5dE8?oc=5) <sub>Moomoo</sub>
- 📰 2026-11-26 [XPENG Driver-Assist Subscription Due in Australia in 2027](https://news.google.com/rss/articles/CBMifkFVX3lxTE10aXE4SGJfS2k2dlpfcEVXelFRQlVtNkhtTnZvQTcxN1JKaFBURDlrak50QzUwX29GZFFoaXZGX3BtZExZNlFDSkJaWHQzVWpZS2FkUWlXeWRVdDFFemtCYXpsZklkLXZLdldkZGRCVUM5Rm8zTXNUVW5QMXBkdw?oc=5) <sub>Zecar</sub>
- 📰 2026-11-26 [Xpeng unveils humanoid robot and showcases robotaxi at AI Day](https://news.google.com/rss/articles/CBMiiAFBVV95cUxQMl8xVXEwbllPS0FpNGZvUFQtUHlBTlhmUjFrVDlPQmg0TXhNc3BWMXJGcWl6VkpPQlJteGRuMkVya0VMSXk1aFBNenFMOWpnU1E3UFJjWjdYcXZKaXdsbkpBVmgtQWZvaE1aX19WdTFqZGowQTgzb3NMWTROSU54b2RfVkl1aWRZ0gGcAUFVX3lxTFBOWmtFZFZOdDRRd1NkNGNYY0FTNVpzQXBKQWQ1ZkFvRWVCTXRXNXRMRHZiTFdTX09SLVg3Vjg4NEphMGlnaDJjVGFXaWhMNmZkNHdpdHJvSnYzYU9ZXzUwRjVObTJXQURIRjZmMWVXZmIxcHVJMGgxS05aNW11S2M0VTFBUEx2ZjVuRE5uMGtubHMxMGNvZmotZlY2Rw?oc=5) <sub>Chosunbiz</sub>
- 📰 2026-11-26 [XPENG's Tesla FSD Rival Goes Global in 2027 as VLA 3.0 Debuts](https://news.google.com/rss/articles/CBMie0FVX3lxTE83blJJWEN2VUMtOHhId2hpdzlPMzdkZ3dZZi14Zmd3amkwdlAydEZHME9taHJxUzhNRnQ3RlR3QU91bW9HaWFPd1hSZ0lqQVdnT0ZSRjhSdDNkdHpQNUxDbjJsaHRlQ1pwamNySXlXM3h6VnBNdG5BQVF1Yw?oc=5) <sub>CarSauce</sub>

</details>

<details><summary><b>Li Auto</b> (189)</summary>

- 📰 2026-11-26 [NIO to Deploy 7,500 AI Agents, Targeting 10-Point Gross Margin Improvement](https://news.google.com/rss/articles/CBMidkFVX3lxTFBscGt1ZVRmeUpmajZpOGVkOE92R3dydnBzYzNWaHdEd1BpYmNaX1hLME1ZY0h3cUVfMnZkQnRwd0QxQThqdXpRRW56SEkwUjJzcms0YnI5cHR0SDZEdHRQMjFCeWhTZjhFLXJkU2V3OHVLTHFtUXc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-26 [刚刚，李想曝新车规划！自研芯片上车21万颗，拒绝被供应商牵着走](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9FeWxoMTZfZDRZc2JObzRqdGc2NHBJRXRaUm1LVk1FYUI4VzZ5STJodGpCcUxVWVpzUXBsRWk3YVJJeC1kX3pmMm90bWtLY3VxNG1URm9qdWhocUE?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-26 [带你了解2026小鹏科技日：说了那些话和展示了那些产品？](https://news.google.com/rss/articles/CBMia0FVX3lxTE9zbDhVLVBPOFNXMkk0VFVWeVZSNk40NWs5cDZMU1JEVVlGYnBNWU4zdHJLanpYWm50X3ZydmtRckF4TDdCWkhLcmp6ZTZ3U093elpSZjhmMzliMG1BTkV2NzUycXlTX2k5WldJ?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-26 [理想i9李维斯版值得买吗？36.98万六座纯电旗舰3个维度说清+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5sUU0tMDlzVHJpbUM2cUFyekdxYTVhWWt4SEdtOXFTZGo5ejU5UGV5T1ZQSkJhTUpZS050Y3JsWFlmWXJFMmx1ck5IWUFtZDFzdFNSb21uUjFRNnpFVm5j?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-25 [China’s Neolix gets nod to test self-driving delivery vehicle in Singapore](https://news.google.com/rss/articles/CBMirwFBVV95cUxPY1V6b0VBRS1ESnRTZGNPRHMyNlRlNDZMei03cklEbzl5dzZGX1p6Y3VVZ05BNmRuNnNMQmV6TjZBWkVTa3M3ZWROYkZpUVl4TlZyTHQxdDZyUzA4bm1WbmpRcGZoTlFDU1V6T2paLTZwU0IxODJzb1oxQ3R4NWxSdWtybzI2ZHAydXJSQjdsTW5NSGVjSHc4T05vN3dIaUxlb2R2ajV5SHFfSTlYdEhj?oc=5) <sub>The Business Times</sub>

</details>

<details><summary><b>NIO</b> (208)</summary>

- 📰 2026-11-26 [China's NIO unveils NWM3.0 world model and vehicle-wide intelligence architecture, cutting onboard compute consumption to one thirty-sixth](https://news.google.com/rss/articles/CBMidkFVX3lxTE9FeExVRGhHOHVNeXdQQzQxMnZrcmg4aVNUcDRNZWFqUno5cFNSczB6ZGhEZTdwUC1uZG82cEpMUDRWQzlaUlo0bklVZTk0dmNfM3ZLQUhOaU9abEN2SDR2dUJBWkwyQmJlekk1ZlhBcUNYN0Fmanc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-26 [Onvo to List Updated L60 Black Knight Edition at Guangzhou Show](https://news.google.com/rss/articles/CBMingFBVV95cUxOZW1RWXVodVpKV0ljUUNNMjVlYnZSV296WTV2U0J1QlpCcVdCS0hHdk0xdUVLODNXOTU3UHZlcVFmN1VPTFVJZTB0V0lHbGY1Z3RmeVc1VjBzLVZEVF9vYkdidmxQUDlHa01INzUzR2RtRWJmZmIzYU5Qd0hZNlZKNFdiQ0dlaEMyMHBqY1oxdlNtNS04VFQ3ZEp1dm5QQQ?oc=5) <sub>Electric Vehicles</sub>
- 📰 2026-11-26 [Nio Onvo to launch updated L60 Black Knight edition at Guangzhou Auto Show on November 27](https://news.google.com/rss/articles/CBMioAFBVV95cUxNOVFkMmRRTzlkem9yUnItNncxMkNyMmY0X1VMOXJTQ2pkRzVWX0RaSFB5NHA1QmYzdFZDM1ZnSnhaRDB0MjhTNndEalZUN0pzdFZ2Q1h5dTZMUzdhcXBwUm5ENGJHTGxLSTRLLWdRcWhWR1hOd1dXak82RlI5VEhIV3VQckcyNDNUNUJHdXppYmFyTzllb0RvRndWcWhyVGc4?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-26 [NIO to Deploy 7,500 AI Agents, Targeting 10-Point Gross Margin Improvement](https://news.google.com/rss/articles/CBMidkFVX3lxTFBscGt1ZVRmeUpmajZpOGVkOE92R3dydnBzYzNWaHdEd1BpYmNaX1hLME1ZY0h3cUVfMnZkQnRwd0QxQThqdXpRRW56SEkwUjJzcms0YnI5cHR0SDZEdHRQMjFCeWhTZjhFLXJkU2V3OHVLTHFtUXc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-26 [XPeng's Turing AI Driver Assist to Shift to Subscription Model in Q2 2027; William Li Says "Buy an XPeng While You Still Can"](https://news.google.com/rss/articles/CBMidkFVX3lxTE0zSFVzbkZ0REF3SWRnUXJnUWJCZ2RJSElpQmh6TXJYejZYOHByV0ViZ2M2N2lrTEFtYWJLVVJVYzN4c0JQS3AzcUROOU1SVF80dlA2eUlleVRodDc4Vmk2aGgtUFpITXZpOFRsMHRIMTItOHc5Q2c?oc=5) <sub>BigGo Finance</sub>

</details>

<details><summary><b>Huawei</b> (371)</summary>

- 📰 2026-11-26 [Huawei Says Qiankun Intelligent Automotive Solution Parts Have Topped 100 Million](https://news.google.com/rss/articles/CBMiggFBVV95cUxQakZXVllRSWhrck1OSTBJdGxXLUp2UUlQRFRQaWo0OEtiQlVCQzB0ajU4VGdrQmlKNzVkNHRoNlpmaTJwbUpsN2ZVSzM5dHg2M2RkV0NpZ0c0dDhKdlBwZXlrelYyX1VqR2dQTFZHS3ZINEJkRXJ2ZjZLOEJHekh6QlZR?oc=5) <sub>Pandaily</sub>
- 📰 2026-11-26 [XPeng's Turing AI Driver Assist to Shift to Subscription Model in Q2 2027; William Li Says "Buy an XPeng While You Still Can"](https://news.google.com/rss/articles/CBMidkFVX3lxTE0zSFVzbkZ0REF3SWRnUXJnUWJCZ2RJSElpQmh6TXJYejZYOHByV0ViZ2M2N2lrTEFtYWJLVVJVYzN4c0JQS3AzcUROOU1SVF80dlA2eUlleVRodDc4Vmk2aGgtUFpITXZpOFRsMHRIMTItOHc5Q2c?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-26 [Nio Onvo to launch updated L60 Black Knight edition at Guangzhou Auto Show on November 27](https://news.google.com/rss/articles/CBMioAFBVV95cUxNOVFkMmRRTzlkem9yUnItNncxMkNyMmY0X1VMOXJTQ2pkRzVWX0RaSFB5NHA1QmYzdFZDM1ZnSnhaRDB0MjhTNndEalZUN0pzdFZ2Q1h5dTZMUzdhcXBwUm5ENGJHTGxLSTRLLWdRcWhWR1hOd1dXak82RlI5VEhIV3VQckcyNDNUNUJHdXppYmFyTzllb0RvRndWcWhyVGc4?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-26 [Huawei's patent licensing tops $6.9b as innovation DNA drives long-term R&D](https://news.google.com/rss/articles/CBMifkFVX3lxTE1hejI5NGJXZHY3OW1YMU51T0VleTZraTFLbWN4ZjJMX2tMODBTTGNLeUhNZTFId19lVlJyeGxDSzc2RUJDcWk5UnVMaTNvMnhya2JhZlNNSHZ3RUpWSE9oazJmMG4zSW5HZU9LUXZVLTVfcjVRTTJGMUgzamFZZw?oc=5) <sub>China Daily</sub>
- 📰 2026-11-26 [华为公布智能汽车部件发货量超1亿件 乾崑智驾ADS份额居首](https://news.google.com/rss/articles/CBMiYkFVX3lxTE9MYTB3anU5d2E3VE5DM045amJtYlk0ZDFQUEs4aVBVMUFKcHNKQXIxVFpQeTBJVVpTdWg2SHdsbnYwQ2w3azV5SHF5eFhHSVVMOE5JeEd5VVhNNXExWFRpcFVR?oc=5) <sub>观点网</sub>

</details>

<details><summary><b>Baidu Apollo</b> (60)</summary>

- 📰 2026-11-26 [The Fierce Competition of Chinese Autonomous Taxis in Dubai: Market Expansion, Tech Advantages & Global Layout](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1rNWFaSE9Ed0Z3cVV3WE9aYjc1MW9QWjE1VEZ0cmV5TDZ5cW96TktTWXVrWWlyLUFhWG9pd2YyeFoxWFZteVNtZ0hFamVkOVU3cGhR?oc=5) <sub>eu.36kr.com</sub>
- 📰 2026-11-25 [Is WeRide Overtaking Rival Pony AI?](https://news.google.com/rss/articles/CBMiigFBVV95cUxPaVVSTGFqQldCYV9HNEFBQ0hxZVp4aE1oaDhpUVNjaHVnWElfMVdBeHMwSllNMGtBamU1QVpfdE1sN2NiU1RqS0NrdnN5eTQxZ3pWOHg4UkxPMXZ2bHhYNHQyR1pmZ0NMUW1BeFE3QUt0SVlNaEdUWFp2SDJheXNGMkp6UFZJUWhRZ2c?oc=5) <sub>Benzinga</sub>
- 📰 2026-11-25 [Chinese companies make new progress in driverless taxi development](https://news.google.com/rss/articles/CBMiYkFVX3lxTE5Ld3lrUFctLVBCWFpaUldMVG5mM2VyQzF2ZnRGazE1ZE1JYkk4dktGa0hJN0N2QWQ2V2ttUjEwVHNGY2FhcmgtdlhHQUtfbHVvbGNBUTJocURHMXpVOFdGV0ln?oc=5) <sub>Global Times</sub>
- 📰 2026-11-24 [WeRide edges ahead in China’s robotaxi race](https://news.google.com/rss/articles/CBMiekFVX3lxTE1QSEp5TjZvQVFYVWU0ZVowMC1obGJTaHhnWkZLTjZlYWhFTW44bF9zVlRFbm5fZ1JGdy0zZ2pWLXNlQ1hGQzRKZXZvWDdiRk81OHFUZS0yY2FSNDFWYjZsbV9fSjJUWEhKdUF6anVUREExd2pOeEgxOTB3?oc=5) <sub>Bamboo Works</sub>
- 📰 2026-11-24 [时时彩中三开户平台活动，签到30天居然有大惊喜？](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBpNlhrMFlHdDRqMjlfRkhDd1VCYjVaUkNYWm1hQi1xMkplWTJyc3pNeVVCOUlTbUp5NHI0X05nNnVxUDVraG1HMUdQZFpORmprRDR5NGd2aEJpRmVEekxZ?oc=5) <sub>iheima</sub>

</details>

<details><summary><b>Pony.ai</b> (149)</summary>

- 📰 2026-11-26 [Connected and autonomous vehicles - Drone and AV test centre to be founded in Abu Dhabi](https://news.google.com/rss/articles/CBMiwgFBVV95cUxQTThPQ3JPSU94Z2FUekdGSkxxVS1fWVc4YjM0UEY5elQ0elZtVVFoMWZnZkdMSjhIdFdFX1dwWDQ3bXhUU0FEQW1hbExYZVlFcEhoMjBWU05jemVubW9OYkNGZVVlT1RKNlBWb3NlNTRkNmZ2dmhfZVhIWWdSNl9FdFJFRVlKdW14X0V6alNGZEluandkNHJINWEyZkVITVpMaWh3dHB2X3VMYjFXaVdNcWpMclpGZl83VS1BR1F3NkNHQQ?oc=5) <sub>Smart Cities World</sub>
- 📰 2026-11-25 [Robotaxi同题答卷：文远知行押注AI基础设施，小马智行死磕自动驾驶_公司新闻_财经](https://news.google.com/rss/articles/CBMiYEFVX3lxTE5GZ29PS2R5bDE0U2p1OW1OZU85SXRRenlheU5WT014THJiRmM4MTRRN1NaRmRoUm1ZS3g0MHppNTZCSGZ1V3l2eDM2OXFxZ0FMdW5yekRhbnBIVTBwVm1jRA?oc=5) <sub>证券之星</sub>
- 📰 2026-11-25 [Is WeRide Overtaking Rival Pony AI?](https://news.google.com/rss/articles/CBMiigFBVV95cUxPaVVSTGFqQldCYV9HNEFBQ0hxZVp4aE1oaDhpUVNjaHVnWElfMVdBeHMwSllNMGtBamU1QVpfdE1sN2NiU1RqS0NrdnN5eTQxZ3pWOHg4UkxPMXZ2bHhYNHQyR1pmZ0NMUW1BeFE3QUt0SVlNaEdUWFp2SDJheXNGMkp6UFZJUWhRZ2c?oc=5) <sub>Benzinga</sub>
- 📰 2026-11-25 [Chinese companies make new progress in driverless taxi development](https://news.google.com/rss/articles/CBMiYkFVX3lxTE5Ld3lrUFctLVBCWFpaUldMVG5mM2VyQzF2ZnRGazE1ZE1JYkk4dktGa0hJN0N2QWQ2V2ttUjEwVHNGY2FhcmgtdlhHQUtfbHVvbGNBUTJocURHMXpVOFdGV0ln?oc=5) <sub>Global Times</sub>
- 📰 2026-11-25 [Lucid Gravity robotaxis for Uber now run with nobody at the wheel](https://news.google.com/rss/articles/CBMigAFBVV95cUxPQ0lMSl91V0liM3h6S0VKMW1OREdWMC1RbHRiNklMRHp1SUkzeUsxV3VjcjdyREE3bno3eV9EOGc1RVpZLWZ3QjhhVzdsb0tyRnliYkJXR0ZKWk9OTk50ajhUTEUzNWdSWDlSZVBtVDhMbTZBU280a1lGUEo1enNrSA?oc=5) <sub>AutoNext.co</sub>

</details>

<details><summary><b>WeRide</b> (149)</summary>

- 📰 2026-11-26 [China’s WeRide targets threefold Middle East expansion](https://news.google.com/rss/articles/CBMimAFBVV95cUxNUUZBWGNUd1Q0T0dnN1UwY2xjZi1MMDdxY0JtU2tocjVUOEdWWld4UXdMYWo2X0JpcXkybFNtemlfdU40X2pCb3JLbDItVkZRQ3RPZ0g0MDYyaHR3V0xvbnJTS09TVEZhdTBIekNGRWZmb3NIbjdqNkhRV3dIam1yZ21NaG1QLXlfWDlCTG5RNlUwZjZvYTJFOA?oc=5) <sub>Arabian Gulf Business Insight \| AGBI</sub>
- 📰 2026-11-26 [The Fierce Competition of Chinese Autonomous Taxis in Dubai: Market Expansion, Tech Advantages & Global Layout](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1rNWFaSE9Ed0Z3cVV3WE9aYjc1MW9QWjE1VEZ0cmV5TDZ5cW96TktTWXVrWWlyLUFhWG9pd2YyeFoxWFZteVNtZ0hFamVkOVU3cGhR?oc=5) <sub>eu.36kr.com</sub>
- 📰 2026-11-26 [解密文远知行Q3利润承压三大诱因_公司新闻](https://news.google.com/rss/articles/CBMiYkFVX3lxTE4zT2NVZkktV2ZVTndlcThzWmVLZ0NiWUpmcks5MXdYaVp5VGY3RkMxT3lKZFlyN3pBQXhJZjk0ZW5XTngtdjh3bnJidEN4SU9MNnAteWt1WXZySzYzbFZjNnF3?oc=5) <sub>证券之星</sub>
- 📰 2026-11-26 [营收暴涨、研发超营收，文远知行出海遇安全考验 新加坡榜鹅，搭载文远知行方案的自动驾驶接驳车测试时险些撞到过马路学生，当地监管叫停同类路口测试。险情背后，文远知行第三季度，营收同比大增 88%，Robotaxi 收入首破亿元；但单季研发投入高于营收，亏损仍](https://news.google.com/rss/articles/CBMiiAFBVV95cUxObEZ5YkkyNGJjaW5mSEJaVE84cDMwYWpRdW5Kb3FmQU91eGRqNXd2TVpyVWFLcXpKWUxxUUI1RXl4WElfMzgwZ3NEMlNTbG0wS3FnUGI0c2NyWUZIX0NzV1R0aVZ0Y09uOXE1d2NCTnQwZW8xV2VsY3BLLW5qWmM1a2wwemdEbzNy?oc=5) <sub>Sohu</sub>
- 📰 2026-11-26 [文远知行-W早盘涨超4% 三季度总收入同比增长88%至3.215亿元](https://news.google.com/rss/articles/CBMilgFBVV95cUxPWWZ6R1NOU3VTd1RhVnhRTWtsNnFJcmlFdUduakFJdloxdVQ5R3M1N1ZSZmxlUzFFTC1xUTlVQmJucWFVX0xlNl83Y05mQlBRRVVrbXFjbC0zSUF1YTlOZHlRVHhJaV9yajBxNVM4VldHdmoyRHRmbjV1SWdmeUlMYjg3ZXV3QU9aM0gybWVPODJYclRDWEE?oc=5) <sub>新浪财经</sub>

</details>

<details><summary><b>Horizon Robotics</b> (157)</summary>

- 💻 2026-11-22 [HorizonRobotics/holobrain-0.5-homepage](https://github.com/HorizonRobotics/holobrain-0.5-homepage) <sub>GitHub</sub>
- 💻 2026-11-22 [HorizonRobotics/HoloBrain](https://github.com/HorizonRobotics/HoloBrain) <sub>GitHub</sub>
- 📰 2026-11-26 [Volkswagen’s $23,000 self-driving sedan shows how China leads on car tech](https://news.google.com/rss/articles/CBMitAFBVV95cUxQaWQ0cXNkbk5EbjBlUXJSZUUzNkQtSG04UXA5YUpmS0dleXV5Zzh3TXlTNFBaMnB0Yzl0ajFmVXJhS2lWYVh4MUZ4b3B0Uk1SaDk5RklXckU2Uk1TOXYxT2VtamVOUE55NHJpOUdKUnlaUnY4eU56RzJBR3pIUFJMd1NGVmtnQ0ZyMFNhRXFBb3IxdkpjakEyblg5ZXpnRnMzSi1ERmpIbFRNWDV2LTQtSGZDb0k?oc=5) <sub>The Straits Times</sub>
- 📰 2026-11-25 [China builds tech behind Volkswagen's new $18,000 self-driving sedan for global markets](https://news.google.com/rss/articles/CBMixgFBVV95cUxPcHVWcS12N0ZtOTRKZ3NWYmo1OXlnbklaWUZ4Rk9NMWRqaFo5S1dLdVVWQ1E1OGZZM3BzdXBrN3JoMHdkSVI1dkpOckZCMFVnbjBmOG9Nd096MTVpOHdxVkZKcEcwYzlLZmhGeHNRUzZ0SzFrLUlEZ1NPdWhwdlN1Wmd3VTk2LXpRRUJwV3MwYVAtc2ZGNmtKTi1OTUxGUzRPXzl6Mzg4Z2h0cnpfdkoxSEhkUnd6aWRmSUtTVjhGSzZTblRJTkHSAcsBQVVfeXFMTVBNcTZQdkdDcFVKUDNJY2JGLUp5ZkZhYkhjMkNPajh1Wl9PVFpvRFpmV05lTUd5dlJ2T19XTk5fcFV3TTZobGNvS0JIUGhySkNNLVVHQk5MN2ZDY21qOTRadTBiMkRqdHdSeXFpRTlBT1dtanc5SHI2LXZYa0ttOFp3VG1RaVZpeE8wZTNnMVFNMnByNHUxWUJJNTU3XzBvUlFROGdMVW9tcy16Njh1MlFVRWNNOFpDNFFTcnNsOGQtbC16VThmSjdiWWs?oc=5) <sub>CNBC TV18</sub>
- 📰 2026-11-25 [VW ID. Era 5S: $17,175, Level 2, Not Self-Driving](https://news.google.com/rss/articles/CBMihAFBVV95cUxPX29OaGs5X29FN0szaGhwMzdIOXJ3bWFBdHFHZVZFUjgxb1Z4dzBCVk9vOXU0cVNseXI3NlZkU1ZHN2t0R2hHLXE2cUVNcWFhN1JfS19hRVdaMy1aYlRlNFJiOTVyZzlPd3pzV2d0aEV3bTB5UkdubDh4TlVzX0xiTzJ2cWM?oc=5) <sub>shattered.io</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (17)</summary>

- 📰 2026-11-26 [特斯拉Reality View引关注，元戎启行发布深圳街景渲染视频](https://news.google.com/rss/articles/CBMigAFBVV95cUxOWXVweWkyU3RMMW1URnhrSHJBWkdfLWtVbEdUUkRjd0tPZUM2WDFybUVmRjcta3MwWHRWYjA5Z052dG1DTDFrdFJMRURXdE9KeGM0NWF3UUNNTDl6STZnbkRaZjdFRTJ4cS1mZE9EemxUd01kOERvaVUtS3VYWjdraQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-25 [特斯拉FSD带火Reality View，元戎启行早有技术储备](https://news.google.com/rss/articles/CBMigAFBVV95cUxQbVpMVEdmdnJxblRkVjdEODU2Y3BYZkdYMElDU1BKS0x5Sl9sR1M0bGFWQmRhNEQ5dGhYYWNWd2pBQmVyX3ROQ183c0x6NmI2X3Q5NFdQZHZjUFNXMWNoYW1WRzJ5NE9JTFAzX0VaX0VFcURsV1VqcXk0ZWo2Ny0teQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-25 [特斯拉FSD V15 Reality View惊艳 元戎启行同类技术曝光](https://news.google.com/rss/articles/CBMic0FVX3lxTE5jNldwNDBLcDU5OVNNckN3RzhlMXVZdFJ5a2haZXpSTHJsc1BqcmRSRUd5eWlyRVZVcnUycU1VT0ZHancxaFZ1eXVxTmxDVVlkc2llODB4ME9fVmVDMVJ3dTA4ckRRV0hSMGMtbjRQUlV5cDQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-24 [Anthropic创始人第一份工作在百度，几年就打造超13万亿元市值公司](https://news.google.com/rss/articles/CBMijwFBVV95cUxNMXZJWE1ta2hxdmZ1VzFDOEluOEZ0Q1hmaEFwOUdvemZtTXljVGhLbTlYOVdEQkhaVEhfQ2ROazctRWNrdnE3TWNERWg2dFlDakNuSWJtRzBJUmxzQzlCWEtVNjNacWExQUNvT3Bkdmt2Y3VNOEYxUDV2eTlhcGhIWWluZWpMX2c3SFFvY2NQMA?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-23 [【视频】#奥迪E7X用车日记# Model YL和奥迪E7X 我为什么选了它](https://news.google.com/rss/articles/CBMiW0FVX3lxTE0xXzI3eHc3Y0NkcVFIQk5FcWdFMzZidmtYTm1oWlZFamVaSDlRbk5obWlYQzNfMzVPc3I5VzA5Z1BRWU5nQmplWUw1TS1QR2ZlZ19COWdYNVg2bTA?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Mobileye</b> (16)</summary>

- 📰 2026-11-26 [Mobileye Faces Rising Competition in Driver-Assistance Chips](https://news.google.com/rss/articles/CBMinAFBVV95cUxOS3dfVkV6M3dNNlh3Qlh4LVJjTlk1Y2FZRkhEZXBKR1RBVEdUYTNLR0RieUJwSmdBU3c4THIybEhlT1lwQnBocWU1X0ZvVUI4cW5KRUUtTFBrNlBMQ1lqdEZQa0RRd0ozaVdFTkR2ZVFvYngyUGVwZkdoS1hKYmhCN2lkWVFXRzFpRlBKeFl3WVZuakpfSkp2X3JMMDc?oc=5) <sub>Wisevoter</sub>
- 📰 2026-11-25 [Mobileye faces new competition as cars get smarter](https://news.google.com/rss/articles/CBMipgFBVV95cUxQTEZyekgzdFhjTy1DUzIyVHUtOUdyM3U3YWJmd0g1TDE0b2F5U09INkh6N3NycHNkSnBPYzJ2cENQWVFmMzdHOFdEdWVudm5fNnpsWlRPQjhrN1cxVWpJVTF1LW9ETUhfSGYxZFFHX2RFa2ctZGc0MGF6a2lMU3kyeFRQR1BuS0tIWXNmVnJwOHdYS2VSYUM1VGFMMGF1MzZUd0gwQVB3?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-11-25 [Motional retools for the robotaxi race](https://news.google.com/rss/articles/CBMimgFBVV95cUxQRmQtVzZpbHI2WEpZS1o3MnRDVUtabFA4OEJ6MjdiVHhmekZQTS1OcFVPXzYwcklrRDJYQXpEOHJqckxPMmpjd2RpRndrcHFxUVpEYS1WWWctZWdCOUswejRxUHExX0RreUFnVWV5OEpxRGRmQ2hvWVQzVEM4S2RxQzd5NXkxVVhxaVA1TmJ1RFVEaEUyVktydHln?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-11-24 [Tesla Wants Drivers to Keep Their Eyes on the AI-Rendered Road](https://news.google.com/rss/articles/CBMiwAFBVV95cUxPXzdTSl9DbnRIZzNLVXRlQkxkc24tMUhfOUxBN3NYSUVjRXlUQXZTREZtUEowU1VNc05wOXVlNXF0Vm1LVE52MS0xcDVoNmpZVWwzM0ZkVUZlc0hWbmJTQWNLRzhPVDVBZzJINTl1NDdybHVFc0w5RzBnT1VIQlNvM21BYndrZlZ0N0VqQUVKTHBRdzh3WmQ5QUNLWkVKZUpyZUpQZXRFY2FsRW5DN0ZESDVwNjF4Yk9QVXFCUmJHaHQ?oc=5) <sub>The Daily Upside</sub>
- 📰 2026-11-23 [Robotaxi Market to Reach US$198.6 Billion by 2035 as Waymo-Uber](https://news.google.com/rss/articles/CBMioAFBVV95cUxOOVFHa1QzX0FoWEhodlVoV2tBekhIb245dmxkLTZBSTJyYVBuVU5LQWg0WFVtLWFIU0c5SDc4cjRTRVlJNEVXemxRQmlhTFhDTVEzb2JwcDVzZDZHNmRlN3BUTnZuTzFjSGFLNjhEb1J5RzNqVXV5cW91d0FVVjdKYUV0OEF1ZjlFM2VSQUNUSXQ2X1FUYmFLZ1VLbXFOdXly?oc=5) <sub>openPR.com</sub>

</details>

<details><summary><b>Aurora</b> (35)</summary>

- 📰 2026-11-25 [Notice of Investigation of AUR: Kessler Topaz Meltzer &](https://news.google.com/rss/articles/CBMiqAJBVV95cUxOSlh0RmpSLUI5ZGFGYTkwS1EwUHdsYmpfV0lETHR4UW1wUS1RSlVVdUY1bi1jNVRtM3hKLWlQNXBBVk02Ti1CcWViWWhJLTlybmcxRnliWG45Z0RUQWRiTFE4aDZHeVFXUDNrNDZUUGdJdENTMjJtYkk3R0pzaFQtLVd0ZDBwV0RtRU5GSHNJMTJFdUtNMFlOdnRaQzhWQXdmYjM4UW10VFIyY2JRS2tBTTdpSDhIVXhLUVJFQjJULUdyR0MzdnBkR091N2VrT3JqdEcyaE1oRkttUzlDbm00WkFjWllkZWJjbFlZZUhKUDZWcTlHRWc0YlJwcllqdW0tSHM4YzREUGpDWHREWUZiZFBiQkV0QW1hN24yR0hBYnEyWlJidjFGaQ?oc=5) <sub>GlobeNewswire</sub>
- 📰 2026-11-24 [Aurora Innovation (AUR) Draws Fresh Fund Attention, Where Does Fair Value Sit?](https://news.google.com/rss/articles/CBMi1AFBVV95cUxNNXNhcjdGTDhleVVxTFFWY0ZCVFdRVUhOeUxGY1lkb1FUNTMyLVBOTlUtRkJmRXdleUE5aXJ0MURSTUs3Y25fMk9HU0J6eXNFaGtPQi1FMmRvRDFGdzUycVg3NHk2MUpzWlhvclZjU1l6ZUkyNVRHdkdHT2dtaEp4NloybTZWVVd1cEZOOWh2S2VtNVJhYVc3UDEzQnp4cU9DQk5wTDdRd05Kd0dFdU5BRnJBSzFFV2dLMEU4aldtbEFsYU9sTnkxYmxFbFRoT0dkejV6TdIB1AFBVV95cUxNNXNhcjdGTDhleVVxTFFWY0ZCVFdRVUhOeUxGY1lkb1FUNTMyLVBOTlUtRkJmRXdleUE5aXJ0MURSTUs3Y25fMk9HU0J6eXNFaGtPQi1FMmRvRDFGdzUycVg3NHk2MUpzWlhvclZjU1l6ZUkyNVRHdkdHT2dtaEp4NloybTZWVVd1cEZOOWh2S2VtNVJhYVc3UDEzQnp4cU9DQk5wTDdRd05Kd0dFdU5BRnJBSzFFV2dLMEU4aldtbEFsYU9sTnkxYmxFbFRoT0dkejV6TQ?oc=5) <sub>Simply Wall St</sub>
- 📰 2026-11-23 [McLane to acquire Northeastern restaurant distributor](https://news.google.com/rss/articles/CBMif0FVX3lxTE5CbHJQVXNlSVhiT2NnMUZqSGFBdDdlMkw5QnpRYkhNVmQzSy1pdXRUWDRXVGdBTEkxaWs1OUxwSWFndkZPeGU2NWY0bTY3RTlnVm1oUWwzNERvUE0wcVkydC1qRklqajR4Y2pSdnRENEFzdHhHS2ZFN0lDS0NPM28?oc=5) <sub>C-Store Dive</sub>
- 📰 2026-11-23 [AUR Investigation: Kessler Topaz Meltzer & Check, LLP Encourages Aurora Innovation, Inc. (AUR) Investors to Contact the Firm](https://news.google.com/rss/articles/CBMigwJBVV95cUxNblIxN0M5MWplVWNpY2dEUzVCcEp3RW1scjlPbjNRNU10YUhvcVIzbDJudXB0clZSa2NKTkdMU3h4cXpER1QyWmFHZnplSGs1ejZtWG9WOGR3TFFkRVBLaERjdkdUV0lVOEJ5NTFVX2JGcEg4V0ozTlVyWmZZQzZYSEtDTXZ6YmpYYmNLQU9oZDdDSWE3TUJZa2w2NDBiT1dEbzRjQUFYN2pfSTQ4MWROVG8zbURueG5aaHUwdVkxaDExLWlidWtzOHhxZk1zaWY5VnhDdlJiaHdKek05Yi1rLVItdEFOUnZnSzZHcjk3ZVJVNVd6dlFqSDhWTkhXM2pKeHVN?oc=5) <sub>PR Newswire</sub>
- 📰 2026-11-23 [Aurora Innovation (AUR): Hedged Position Gains Despite Share Pullback](https://news.google.com/rss/articles/CBMijwFBVV95cUxQZElieFVfYkJWS09MMV83WXRRU0VIQnBITjZNLTNoY1A4RllLdG1rb19DSDlSTHJxbnZmNnFfMUI3YjVhQlhlUXRuUVpra1doQ0p5c21WX1lCRVZtN3lJaExLcEliVU0xUHA5dzk4YVZBVElLOVlrd0pVVnRXTEtlMVBvSUJuQk5PVzloak54aw?oc=5) <sub>Yahoo Finance Australia</sub>

</details>

<details><summary><b>Zoox</b> (114)</summary>

- 📰 2026-11-26 [Uber adds Amazon’s Zoox robotaxis in Las Vegas, Bloomberg reports](https://news.google.com/rss/articles/CBMiUkFVX3lxTE9Zc25aTlhMN0k1cUUzTlpnbHVERkxYUHhBa3kwd3RwTmxHRXVic0xXT2Q3SHZ3UF9qSk5BakVKMU1fOWpNMDRwRURIYXFES0Nqb2c?oc=5) <sub>Digg</sub>
- 📰 2026-11-25 [Zoox Robotaxi Launches in Santa Monica](https://news.google.com/rss/articles/CBMijAFBVV95cUxNSU55dTlpUjVzSzJjU3NSSS1FdmJxcGo4clpJbklsZWQ3alB6NXZmT0lOelFzS25aYW40VmRMeDFfOURoX09aeGFGdl90V09NSTlaVWdnUjNsekZlTXNSNTlHeHJSUWItNDdFM0xKaXhES3psY1UzZnA5MHJDSVI4VHJad2JnYURDZ2xYcg?oc=5) <sub>Santa Monica Daily Press</sub>
- 📰 2026-11-24 [Uber’s Lucid robotaxis now drive Bay Area streets with nobody at the wheel](https://news.google.com/rss/articles/CBMimAFBVV95cUxQeGluQ2hwZFNKcWx0UzB2UndFOHY3dWhwOVhnZ0EwdGZ2TVdjTXFzbDJXQUtCeTU4LUdKTHJ0QjNPaG5lcnFSU0xmcTc2UTVpalVZQzBDM0JTVkU4QVV4ZnFMdnNQdVl2T1ZYb0NLbUZvY25yQmNkbUw5X3ZmNlpHZGNGSDFXRkQyX09kZ3JhMmRqb3Q0czVLUg?oc=5) <sub>Martin Cid Magazine</sub>
- 📰 2026-11-24 [Lucid Gravity Robotaxis with Nuro Autonomy Start Driverless Testing on Bay Area Streets for Uber](https://news.google.com/rss/articles/CBMihgFBVV95cUxNZ0Yzd0VWMnNzRlYtSzNDeXU2S0drNmVVd1VMelh2bERpRWNVem9sUHBtdTlEUjNNa1dOLXRrZG9kS0syYkJ6Mml4UzkzbjlsaDVsYXFoTGVvU25FYkY1QUQtc3Z1SWlFZVJrcWVBUXo1NFJGS29FdGx2SjdvUUFtMU1WTXlaUQ?oc=5) <sub>TechEBlog -</sub>
- 📰 2026-11-24 [Hong Kong International Airport Uses Robots to Repaint Runway](https://news.google.com/rss/articles/CBMimwFBVV95cUxONDd1LXc2NE9wdW9kdTk2SFdqZE5JRVlvSEI3VzFZN0doaUdqWWV1cXVCLUlJNWVUYVVyZHVxRFFYckhHcXZodXZXRDFjM3VfOHBXZXYwX09oWnUyRmQyNmFpZEJpalFUa2tndEd6ZVUxM0VvTTBReElubEtNNjNsdDNUVnhXYURJazFyRkpBRWpkdHIwNWhaWUhTSQ?oc=5) <sub>Future Transport-News</sub>

</details>

<details><summary><b>Motional</b> (35)</summary>

- 📰 2026-11-26 [Hyundai Motor to Begin Supplying Robotaxis to Waymo Starting in the Fourth Quarter : Finance : JKN](https://news.google.com/rss/articles/CBMiYkFVX3lxTE9QTVEzS1B4cFlESWNVbklSTGlEc2RfV05ESzRaVGgxZFhXemNhRWdQaU9vMkdCcTRKWFNvYnFaSnk2NGRGZzFOUmVtQVhvWC1RWmRKa3VQYV9maVdxeXBMRk1n?oc=5) <sub>재경일보</sub>
- 📰 2026-11-25 [Motional retools for the robotaxi race](https://news.google.com/rss/articles/CBMicEFVX3lxTE9OODFESWJPQWc1cnNIVVlaSVU2NXZSMEJETzBfOVB4eGdGcTJyaEt5VkRJbWxtUHpRdFJmVDJKR3JONVduSkdfc0pfLVp5RTlFejM0R0lfR1h1RS1ZNEFwSnluUzJiblJyS1dwZjdVT3A?oc=5) <sub>Axios</sub>
- 📰 2026-11-25 [Motional prepares for Uber robotaxi launch in Las Vegas](https://news.google.com/rss/articles/CBMihwFBVV95cUxNZndrdzVJUDJpY3I4VzctSDBMVzA2VWNjU25uRVYwa2FTSjhkU0IwQkpLcFRlSWRCbnBwTUJMWnJMc2Y0MnBhTzdueFRLQVdhWEdLSW9ZZ3hIXzR0Ml9uMkgtbGZteXhvcWxvOXFoU0lrNEdLSGVGczRQVGFpNW1RYXNZN1FTdEU?oc=5) <sub>Mezha.net</sub>
- 📰 2026-11-25 [Motional readies Uber robotaxi launch in Las Vegas as it resets cost strategy](https://news.google.com/rss/articles/CBMimAFBVV95cUxNVkdrcXFnSkpDcklYN005Ykd0SGtFUi03akM0OG43c0E5Ny1Xbk5PYUFCTWFQNGZkc1FNUzNVUTRJaHdVS0FGUGNrMkVQWnFjc1ZMRU9mM2d1Nkc4THprYUNJbXdjMkJjck9ZQjQwRFFtVVNBSGY2RDE5UE5wMmtkWjNoUVRmS01NSUVRVlBkSzhuQmhnamxvZA?oc=5) <sub>Traders Union</sub>
- 📰 2026-11-25 [Zoox Robotaxi Launches in Santa Monica](https://news.google.com/rss/articles/CBMijAFBVV95cUxNSU55dTlpUjVzSzJjU3NSSS1FdmJxcGo4clpJbklsZWQ3alB6NXZmT0lOelFzS25aYW40VmRMeDFfOURoX09aeGFGdl90V09NSTlaVWdnUjNsekZlTXNSNTlHeHJSUWItNDdFM0xKaXhES3psY1UzZnA5MHJDSVI4VHJad2JnYURDZ2xYcg?oc=5) <sub>Santa Monica Daily Press</sub>

</details>

<details><summary><b>comma.ai</b> (2)</summary>

- 📰 2026-11-23 [Open Source Drive by Wire Kit Retrofits Standard Passenger Cars for Autonomous Research](https://news.google.com/rss/articles/CBMisgFBVV95cUxOYkF5ZVN3eWtSa1FRSnF4Z091VFZlQ2pwZHIybWlxRHhMRXdwWFZMQk43QUNTc3d2VkNRbmNuSGxKUXh1Z0JMN1BfeHFqbFRtM2VnWldHeE9TQ0RVYThPVEpvTnpESTVYWEJZWlJDWWRqbVFYM1dTdFRkWklFd014a2N1d0ctbjlIQy16VW1YYnh1bm1rSmdOdHJvb0JGN1FTbVMzM2F0RUR5RF9SRnNfS1Z3?oc=5) <sub>Bioengineer.org</sub>
- 📰 2026-11-12 [Goodbye, BlueCruise! We Install a comma four in Our F-150 Lightning](https://news.google.com/rss/articles/CBMirwFBVV95cUxPY1o5ekZ4WnpraUxVMHV6OVdyMEtEbjQxQXY5STdJdXlHNlN6eUFZNzFwSnA5cFhHd3pNdTZNNy03dXBOZ1ZoX3RFX2E5V2JNTE9aVlhJaG90bW5YWEdzX2NGXzd3VFZ6NG5JVkFrM3daTmY4UDBTN1I4NWU3eGJqUm9tY1VaRWxoZkp3WDJLNnVLQjN5WG9NMzlxLWI0aVU2TFhLUEZwUE5YUDdUcWFJ?oc=5) <sub>Transport Evolved</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
