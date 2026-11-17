# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-11-17 · 1,290 papers tracked · 49 curated.

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
| [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)<br><sub>Yuan Gao, Wenting Miao, Mattia Piccinini et al.</sub> | IROS<br>2026-07<br>📑 1 | [⭐ 33](https://github.com/TUM-AVS/Chat2scenic) | Validating autonomous driving systems requires diverse, regulation-compliant test scenarios |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 19 | [⭐ 562](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
| [GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives](https://arxiv.org/abs/2609.39601)<br><sub>Qize Yu, Lianrui Fan, Boyu Chen et al.</sub> | arXiv<br>2026-09<br>📑 3 | [⭐ 439](https://github.com/groundingpi/GroundingPI) | Precise grounding matters |
| [GRAVA: Grounded Reasoning-to-Action Representation and Learning for Autonomous Driving](https://arxiv.org/abs/2609.15169)<br><sub>Xiao Liu, Haoyu Li, Jianghao Leng et al.</sub> | arXiv<br>2026-09 | [⭐ 487](https://github.com/AhernResearch/grava) | Driving vision-language-action (VLA) models increasingly reason before acting, but their intermediate reasoning is often weakly grounded in physical scene evidence and loosely connected to executable behavior |
| [Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air](https://arxiv.org/abs/2605.31066)<br><sub>Tianle Zeng, Yanci Wen, Xueang Yu et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 1,133](https://github.com/louiszengCN/CarlaAir) | Recent aerial vision-language-action (VLA) models show promising single-UAV capabilities, such as tracking moving objects and navigating to language-specified landmarks |

## World Models & Generative Simulation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [FrozenDrive: Zero-Shot Text-Guided Driving Scene Generation and Data Augmentation with Parameter-Free Frozen Diffusion Model](https://arxiv.org/abs/2606.20110)<br><sub>Yuhwan Jeong, Hyeonseong Kim, Daehyun We et al.</sub> | ECCV 2026<br>2026-06<br>📑 1 | [⭐ 10](https://github.com/daehyunwe/FrozenDrive) | Synthetic data for autonomous driving is surging, powered by diffusion models that promise scalable scene generation |
| [Orbis 2: A Hierarchical World Model for Driving](https://arxiv.org/abs/2607.15898)<br><sub>Sudhanshu Mittal, Arian Mousakhan, Silvio Galesso et al.</sub> | NeurIPS 2026<br>2026-07<br>📑 2 | [⭐ 31](https://github.com/lmb-freiburg/orbis2) | Current world models operate at a single level of abstraction, with most prioritizing perceptual fidelity while lacking the spatial reasoning and semantic understanding required for real-world downstream tasks |
| [MESSENGER: Memory-Enhanced Sequential Scene Flow Estimation via Autoregressive Next-Frame Forecasting](https://arxiv.org/abs/2610.10759)<br><sub>Jiuming Liu, Jianing Li, Mengmeng Liu et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 0](https://github.com/liujiuming123/Messenger) | Scene flow can capture low-level 3D motion displacements in dynamic scenarios |
| [ASTAD: Asymmetric Style Transfer for Synthetic-to-Real Adaptation in Autonomous Driving](https://arxiv.org/abs/2606.29286)<br><sub>Dingyi Yao, Xinqi Zhang, Lihui Peng et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 2](https://github.com/Dingyi-Yao/ASTAD) | Synthetic data mitigates the data scarcity problem in autonomous driving perception |
| [Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends](https://arxiv.org/abs/2606.01164)<br><sub>Jiuming Liu, Chaojun Ni, Mengmeng Liu et al.</sub> | arXiv<br>2026-06<br>📑 9 | [⭐ 251](https://github.com/liujiuming123/Awesome-Interactive-World-Model) | With rapid development of large language models and diffusion-based content generation, world modeling has attracted increasing research attention, benefiting various downstream domains such as game engines, embodied AI,… |

## End-to-End Driving & Planning

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [MOJITO: Modal Joint Learning for Unified End-to-End Autonomous Driving](https://arxiv.org/abs/2607.23511)<br><sub>Zhijing Cheng, Xuancheng Zhang, Donglin Di et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 32](https://github.com/mumucc01/MOJITO) | End-to-end autonomous driving systems commonly follow a cascaded two-stage pipeline where a perception stage compresses multi-modal sensor inputs into a compact context and a downstream planner predicts trajectories cond… |
| [UNIVERSE: Unified Video Action Models for Autonomous Driving with Flexible Mask-Modulated Modality Generation](https://arxiv.org/abs/2607.05133)<br><sub>Mengmeng Liu, Diankun Zhang, Jiuming Liu et al.</sub> | NeurIPS 2026<br>2026-07<br>📑 14 | [⭐ 6](https://github.com/xiaomi-mlab/UNIVERSE) | World Action Models (WAMs) can improve action generalization in autonomous driving by learning scene dynamics through dense future-video supervision |
| [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](https://arxiv.org/abs/2609.26792)<br><sub>Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.</sub> | CoRL 2026<br>2026-09<br>📑 1 | [⭐ 15](https://github.com/VAIL-UCLA/DreamStream) | Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions |
| [DriveMLP: When Training Strategy Outperforms Model Complexity in Autonomous Driving](https://arxiv.org/abs/2610.29676)<br><sub>Alessandro Canevaro, Julian Schmidt, Hang Yu et al.</sub> | CoRL<br>2026-10 | [⭐ 6](https://github.com/alessandro-canevaro/DriveMLP) | Learning motion planning policies that remain reliable under closed-loop execution is a central challenge in Autonomous Driving (AD) |
| [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)<br><sub>Shen Zheng, Anurag Ghosh, Gaurav Parmar et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 32](https://github.com/ShenZheng2000/WarpI2I) | Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs) |
| [G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance](https://arxiv.org/abs/2606.26017)<br><sub>Hang Yu, Ye Jin, Alessandro Canevaro et al.</sub> | IROS 2026<br>2026-06<br>📑 6 | [⭐ 7](https://github.com/HangYuu/G2DP) | In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors |
| [SimWAM: A Simple World Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.07468)<br><sub>Zongchuang Zhao, Xin Zhou, Tianyang Xu et al.</sub> | arXiv<br>2026-08<br>📑 15 | [⭐ 211](https://github.com/H-EmbodVis/SimWAM) | In autonomous driving, World-Action Models (WAMs) have improved end-to-end planning by transferring video dynamics priors to action prediction, but many still couple planning with future-video generation at inference, in… |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 20 | [⭐ 365](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
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
| [DRS-VPT: Directly Relocalizing in a Scan with Vision Point Transformers](https://arxiv.org/abs/2609.12557)<br><sub>Lanke Frank Tarimo Fu, Maurice Fallon</sub> | ECCV 2026<br>2026-09 | [⭐ 23](https://github.com/ori-drs/drs-vpt) | We present DRS-VPT, a feed-forward transformer architecture for foundational image-to-scan registration |
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

<details><summary><b>Waymo</b> (182)</summary>

- 📝 2026-11-05 [How the Waymo Driver Manages Severe Winter Weather](https://waymo.com/blog/2026/11/winter-weather-preparedness) <sub>official blog</sub>
- 📝 2026-11-05 [Rethinking What Freedom of Movement Feels Like for Women](https://waymo.com/blog/2026/11/because-women) <sub>official blog</sub>
- 📰 2026-11-17 [Waymo Fairbanks Test: 0 Fares, 6th-Gen Driver](https://news.google.com/rss/articles/CBMihwFBVV95cUxPb2x5MTNVa0JQVWJmZ3VoSXhjVFJRUmpfSy1BbEJTRmprb3BSaUNhQ0ZDYVhPNTlfdjE0aUtBN1R6d1k4eF94QlpNS0pQMERaWEo2NXZ2cUhGY3NBdUVzdUJQZWd5Umhuc3JnV1pDdDc5Vm5OQVRJSnN5eVpheHdfdWc1Qm1yNWs?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-16 [South Korean automakers join forces to counter foreign robotaxis](https://news.google.com/rss/articles/CBMiV0FVX3lxTFAtWWlTc190V21DLUJVVXdZSlVLNC1PRWkySmFKemhXTHNMTUpySmVOZVZHSHV5U3A0Ui10YTdqNDRQbkkwNjBtNm9GSWtWLWxORTkyU0YtUQ?oc=5) <sub>매일경제</sub>
- 📰 2026-11-16 [Zoox robotaxis expand into downtown Las Vegas and the Arts District](https://news.google.com/rss/articles/CBMimAFBVV95cUxNb1BJbFJFZVlNZGJnR1pkM2xtbGxqdlNsd0dUbmhwZzFvWVNFQ1RWV05NZFFyU1laU1haM2o2b3RESEJ3a2M4ckFzTThqbDE0OFA3TGpfM2o1bmNnTzVxbmFEWndCQkVNbHdpQ2d1enFVUnFiei1jZVhwdDFDN0xiNGhsbFdEeE9TSHVZUEtObDBUNFRGRmdqdQ?oc=5) <sub>KTNV Las Vegas</sub>

</details>

<details><summary><b>Tesla</b> (268)</summary>

- 📰 2026-11-17 [Musk Says Owner Robotaxi Trials May Start in December](https://news.google.com/rss/articles/CBMimwFBVV95cUxPd1Ytb0RISy1CVW04SDhPWi12dWhVVGg3dFR4RXhyRHpYX3hUOEpnblp3R2k0X0syVHdoZUVMYlF3V0V2eXdZR1FLbFJqRzF5am5EMHV6bVFSUjZsc3VLQTJRbHltYmk1cm11MjBaRndPaXliTmg4UFJDTEs4Wmw2VFU3S0FHWFZzMUV6eFNBNGc1UHB5eFJkOUFrbw?oc=5) <sub>The Defiant</sub>
- 📰 2026-11-17 [Elon Musk says he will visit China, renewing hopes for full FSD roll-out](https://news.google.com/rss/articles/CBMifkFVX3lxTE1mUzNSTjVnbWpNU2ZybE9zVWJ6WXgtMDg1V1kyNk0wNVh6RzRRc0pvalVsWi0yQ0ZEWFBUZDlZUDdQYlcwMjYyRWpxd2hCaFdsTlBQMHdOcWVKRjFPZFZjLXVSSGpfckZJSmpTc0RySzFDa2N3T0NXVXVtbWNidw?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-17 [Tesla may test customer-owned Robotaxis as early as next month, Musk says](https://news.google.com/rss/articles/CBMimAFBVV95cUxPNktCZTlaVkVTUUZ3TXh3S2hDc1Q0LTNlSGdIdXhEZWxGaUFQZjVWNVlmZDJzdjZnLW1ScWxzUWVuYUV5TTJwX0hiWFJYRWh6aXRGeG1QcEtJTFBjUUkzSkJ6ZHZHeVI2Nmw2Z05DTzJYS0ZrSEkxZGRWa2cwNm1TMzA5S3BIVTd5Y0VZNnU2ekFsaklYRGhVbA?oc=5) <sub>Teslarati</sub>
- 📰 2026-11-17 ['Coming Soon': Elon Musk Hints Tesla Owners Could Put Their Model Ys to Work as Robotaxis Without Driving](https://news.google.com/rss/articles/CBMi6wFBVV95cUxPd2Rwb1BqN3pxWWZUbVNfVDJCX1hsOHE5OTJKMDR4RnZoRFRnUU92OUxHeDR2YzhPb3dTUDZzcTBWTmNoU01CYnF2Skp3OUpYUmZYUndJRjlVbmxBVlE0bGd2MGhMT0syMTRGY1ZfZHNmMlhSZERtbFVrWXh2V2R2QmhsWHQxcnlzRXhZU2REYXlVSllKSEJTbXI3S2FpczVtclE5alB3SVZEWU9OOUhDLW1LQnZhbmJiU2VhMVljVnA0UlVTYW43VFczNkNvaFJxeFJFMUhOSUwwUjg5UVhVSjJjeWlXcV82OEZV?oc=5) <sub>Benzinga</sub>
- 📰 2026-11-17 [Mercedes-Benz Prepares Tesla FSD Rival — Cars Will Be Able to Drive Through Cities and on Highways](https://news.google.com/rss/articles/CBMif0FVX3lxTE9lS3lmR3BGUDRqYWNDeVM3cXUwU0l3b0Y2ZHRsOEU3MDYzQm1sS040NEc2U3RIZ3d6Q0haM0ZSQ3gxUWF1OVdwNS1lNVlBd1JKVTNETjFyWWpVaGtucmlKUUlXTHRlX1hneXByN2lXNmpqd3FsOWtwNXZtWDFBYVHSAYQBQVVfeXFMUGhCNGlBMVlJVnpTdkcwUWpMcjhPMEVvR3RoTVpMZDNlVGxER0k4Vkg3c3FuVnpSUi03TVY0LU5jaG5Cck1sWWZhMGs4YzZUblVCblBma09EWjJEcGRsVWJ2ZE5uSnAyc183STU3V2RiMVlVdm9ORkUxSmtzQW05VzhtTXNs?oc=5) <sub>Mezha</sub>

</details>

<details><summary><b>NVIDIA</b> (169)</summary>

- 💻 2026-11-16 [NVIDIA/scadactl](https://github.com/NVIDIA/scadactl) <sub>GitHub</sub>
- 📰 2026-11-17 [Report says Madison Huang wields influence at Nvidia, clashes drive exits](https://news.google.com/rss/articles/CBMiiAFBVV95cUxObzh4a0Q2Vl9pNWFic1lJRGNWdnc4OTE3aG5NcTU0ajNDYXBZVW0tQW4wamgxck5BdlBJZE5ySUZQaUdxOGJoNFRxZktvcndoeHhONUM3Vko0eFIyX011RmVSY1E4VGdNa0JRTkhTNFZ5N1dyZmdodXEtNXVXY0pTQzUxeENPZWJS0gGcAUFVX3lxTE95WldrN3RvVFlMd1ZFNkVQNzgzaWJIMnRxT0tfdkVlclhxMS1tR0FMdGxrTk02LWhtUWlDV1pZRzJlaEJKSTFmU1RsMjZnT2ZoVjFUTmRqZTJTaS1ERk1MVEkyZDlISHV0SEtJUF85NXNsRG5mUldFOE5kN2tXNXlqelJHVFBQM0c4YmZiWG14d2tEOUcza1BFcmZtQQ?oc=5) <sub>Chosunbiz</sub>
- 📰 2026-11-17 [DeepSeek and Huawei drive China’s AI ascent, but Nvidia remains a hurdle](https://news.google.com/rss/articles/CBMiggFBVV95cUxPWm82VUZCTzN1LVBkN1VMQ3lHMzNrd000QVZMQWN2MmtZNkY3MGZ2d2JoQUFzZ0MzWmpzWU1JV2J5T1Bxc0tld01lUnJtaHdjbFZoQ00xUmtGQ2lHMk5QSi1QOTAzSk1xTWlla181QmFReG9EakZxQVZacnAxXzZXWWhn?oc=5) <sub>Hankyoreh : English Edition</sub>
- 📰 2026-11-17 [Madison Huang’s Nvidia Role: $1.23M Pay, Age 35](https://news.google.com/rss/articles/CBMikAFBVV95cUxPanNxSkZCR2VMRlBkWFd3c0M2QVNsV0s5LWgxRVdfSDVfd2Y0aWhIOUZibXVfSE9rXzlTcG94dFBfcHF0VkdrWFJfR05fWk1zemFOdlZ2bWJCN20wM2pMMjduajBYVUhmMkw0blh4NnZRYmIxOXNoVEhOMXdPOGVPV0VvVGhsZHhKUXNMOFA3WnU?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-17 [Who is Madison Huang? Questions rise over her role at Nvidia after Jensen Huang’s exit](https://news.google.com/rss/articles/CBMiU0FVX3lxTE5nVnRMeHpReGp4d1NMc0poc3lhZTF6TDV3QWM5MVdxdWlaam11dHVRWkNqQVpQTFRubmtPbnIyT3pVcUp3S1RXN0FWUmZjQXk5ODZj?oc=5) <sub>شبكة تواصل الإخبارية</sub>

</details>

<details><summary><b>Wayve</b> (39)</summary>

- 📰 2026-11-16 [Weekly Recap: Q3 income growth, wider losses and $4.2B financing](https://news.google.com/rss/articles/CBMiwAFBVV95cUxQYnlsREtGYjdOTjRPMHR4b00tZ05mdEI4UkdHN2xPNjdMVE94MnhqR1VjM0FsT014bk9sTVFSWnZHcmlSdTJ3RmRNdWdlLXpaSTBBVXBiZS1zRDNKZk5KaU9yam9pbHVWd01ZejlEMW8xZjN4bmhHMG1mQjFpTTJlZkJWTjdkaXVNM3c0OHBhWmEzR1U3anh4bU1Bai1TZkgxSjk5MzNPbmpVVWx5SWtTalVXYUpqVUlwM1ZZWXBsa2U?oc=5) <sub>TradingView</sub>
- 📰 2026-11-16 [Brits don't trust self-driving cars, survey finds](https://news.google.com/rss/articles/CBMimgFBVV95cUxObEhUVmlYTGI3blZzVzZkRmhjMnJGcEhQTjhiVm5YbExDNUM3UmgtdTRsNEpZVnRfOEJCU1ZvQ2NrZ29vcnlhWFg4WGlGUkpmbDhZNGE1NW5udHI2M21UM3ZMVVlpcXNTS204WGJGTG5HYWhHdGh1TUpwYkpIaVhtZHdIRWFHbU01T2QtLWtUTldieVlkU3BEYVJ3?oc=5) <sub>Female First</sub>
- 📰 2026-11-15 [Autonomous & Self-Driving Vehicle News: Rivian, CoreWeave, Wayve, Kakao, Nvidia, Kia, ASI, TIER IV, MAN Truck & Bus, Komatsu, May Mobility, Volkswagen, Tesla, Terawatt & Waymo \| auto connected car news](https://news.google.com/rss/articles/CBMiogJBVV95cUxPMkxJVEkxdjYzbWJ0LVRPYlNBVElOczdQOXRITVpsWEpzVF9RYm0xT1ZOeURGRFdYTFJ0bDJDTnNkUFNBSUFpcHFFSV9IVkl0NjhoZUNRT21qV2JoM2FmZmg1NmdOMXEweWJOekJqbTZvS085NXlhU01XZ3U1TUxFQVdvdXRPM3RvWGUxWUg0TzYyWW1FbnQ1OTBYaUltNU1QbkwxODdxeGt6OHZrUVZaQldlQVd1dEZSdHlFeVJkVWphQzZEaVBxRGR4Q29Gd2VVbThuWldLRlRzZTRYOVhuelh4YmpoTEM2Nmc2OW1jb0l0MU5ZWTlfdzJIUWY5dkh3UG9JcUJfaF9nNUQwTVhUbWhXRXU4VGpOTlRCMlBfbEpsQQ?oc=5) <sub>AUTO Connected Car News</sub>
- 📰 2026-11-15 [CoreWeave partners with Wayve to accelerate AI training for autonomous vehicles](https://news.google.com/rss/articles/CBMi0gFBVV95cUxNMzN1Qk5zalMzYno3SC14ZmQxQmRVTEpwVU1JR2NTWUItbTVhTXQtelAxREJCTExNZTVPLWJkN0xpZ19yeHZpLTAzdFN0SlZJRkJudll4ZGt2YnNLVUtVcjJIcmhjY0QyR29HcHFhRTdWM2tCYVZCYTFINmRlMmc5SmtvTWlkaHpkZlNtU3ZSY1RKREpydHk2cUoyNkxkQlJmRHZiSXNRdU1Ud3Q2S2YyU3FpaHhHMjQ1T05FWk1fbC1wRFFNWWozLWhlcEJrX2NEZmc?oc=5) <sub>Robotics & Automation News</sub>
- 📰 2026-11-15 [Savings app Chip targets retail investors in private market first](https://news.google.com/rss/articles/CBMiowFBVV95cUxNbDNCcGlYLWlpM2l3VmVnT0ZNMHpIUjFLalFsNmpTZGgzVlU2TkxtbUN4aDZTRm55aWZrZmRkV1dyZHloU01yMlVEcW55MG9RUzFNZFdSQ0JqMnZ3cjZRcHdfSDQ4RHdPV05OYmg3NzBvWXZSRW5icElfSmdLRzlzSlAxOVgzekM2ekgtVU40R3VfQWNURkdVUTBuVjNxc2VhRUtn?oc=5) <sub>Sky News</sub>

</details>

<details><summary><b>Momenta</b> (87)</summary>

- 📰 2026-11-17 [Mercedes-Benz to Offer Hands-Free City Driving in First Half of 2027, Rolling Out in US and Germany](https://news.google.com/rss/articles/CBMidkFVX3lxTE5CbFFkYzFNd1o3bFRrT1NDMEdMeFU5VXg1WW14NnBwQ05Sc3hvOGdJV29scVZQT1N0YzN2OTd6cnJpODM0SXlhRmZTUHNHclJpZEkzcjJ3bzRGaXAzUHN4LWItNUZxN0Z5d1liTHhSRHBjVXkwSFE?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-17 [地平线炮轰算力虚标，Momenta X7 Ultra甩出700TOPS](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5xVlAwbnRyUGpDXzJwOG5FX2VNTWFRRXlDMzhwLTcwRl9VTS0wcUlUUGo4dTM2WFlqS3FubmUwMEFMbzRmR2E3MzZXdGtSb0plVUJsRkZKUHdIN1E?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-16 [How Intelligence Is Reshaping the Automotive Value Chain](https://news.google.com/rss/articles/CBMiugFBVV95cUxNZHd6ekhyLXF1V2Nwc1hvQzRoR0tmdmZJRkl5cXhBeGEyaEg0cWFma2xET2hvMnhtMC1hZkFTandDYXZfaGxSNDBSZnZrOU5Pd3Y5OXdEeWN3dnpncWd4X1J2Rm9OdDM0YnVTVVdubE9kQVdVcER5TUpfMmlLRmdSM0t5QjVPeUxtYUpiSDlCalNKR1AybTNacnBDd2ptMWoyd3RrOF9ITWRSenpxb2plUmdOY2hZUTlCMEE?oc=5) <sub>Gasgoo</sub>
- 📰 2026-11-16 [新世代平台 + Momenta 智驾，宝马 i3 广州车展首发](https://news.google.com/rss/articles/CBMia0FVX3lxTE1aODg2TmNKQlJKRHdYRnhoRHBUR0hTYTczSE1SYnBtMnpUN1QtdFFCWDNzQm1zUkFhOC1pOUw2UUU2dnkzNzZmYkFlX181MFBMTlR2NURuNDNKOG1sRElidzBiQlVkVWo5UGp3?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-16 [郑钦文点赞Momenta智驾 奥迪E7X将升级搭载R7世界模型](https://news.google.com/rss/articles/CBMic0FVX3lxTE1JTDBXU2RzVmEtSnhLSlRrYkRqQXJYOFJCNmpTLUdkbzZtcS10OGZCczRwOXdZZm82aU1QZ3U2T1ZDU0lhRnB4VjFNd1NOSUNnSXkzTm5BQkMyQWludHN6RENqdjFaVG9RTTFYZVFfUmJTT0k?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>XPeng</b> (168)</summary>

- 📰 2026-11-17 [XPeng loss widens in third quarter as vehicle sales revenue rises 20%](https://news.google.com/rss/articles/CBMinAFBVV95cUxQd1NzR3VFTUJpYVM4SmtGODc4ZmRlRFowVFlyelRBRlktaXFLWklYWWxFSG01ajJLY090QVhUTFdoSkdUYUxKd1AxTTNlY2JGZGRkT19GV245dVlFWjdSUGZUQ25uSEdLdXhvNG1jUi10bnpvTW11QkRxSWJYTTNRR0dsWF9USUhTbWRHRkF4cEUyZ1FvVmZ2dUJ6MlI?oc=5) <sub>Bamboo Works</sub>
- 📰 2026-11-17 [He Xiaopeng Unveils 7 Major Consecutive Profitability Targets: 100,000 Annual Overseas Sales Goal & 2025 Tech Commercialization Revenue Plan](https://news.google.com/rss/articles/CBMiU0FVX3lxTFBudEZGZm9DX1ZDZmUxaDhtNmdKMlhkcVE0cnJaZ2MwU2FLTW9EdEtpTUk2WHFtZ0Y3ZGVuZDdscVJYQ1pHZzl2SGZLd3BSVUx4R1dR?oc=5) <sub>eu.36kr.com</sub>
- 📰 2026-11-17 [Xpeng Q3 revenue rises 19% as deliveries hit record high](https://news.google.com/rss/articles/CBMijAFBVV95cUxOYWlsQ0hkOHN0RmUtLU5DbkdUS1lxdi1fOUtESW41dnVqblJtZDVGOEJjMW9rZUx5dEVMOUIzc3pVZVAyMGRMTTdkNmtHdE14dXlsTkcxNk1oYm9oSjhYemVPU3l4NXZDSVZETW1KajJIaUFrdmduSUpOYTBMdi1QZVlTdVNJeTU0ZktiNA?oc=5) <sub>Tech in Asia</sub>
- 📰 2026-11-17 [时速40盲区窜出电动车，小鹏2022款辅助驾驶1秒内完成减速](https://news.google.com/rss/articles/CBMic0FVX3lxTE4wd1h4RTY4LWNfY1lta0dwSlJHUUEtQTZjV2RWV2dSX01HS1BtM0w0cmRWdFRUZXNrRDNFNW16anRzS0lQNlFLYnlXb1NnS3lRNWtmOVFHSlYzdm55YTlPM1o5YnlFelJlU1ctNFczTUEyLXM?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-17 [【视频】小鹏P7 + 溜背轿跑上新，800V 快充兼顾颜值与大空间](https://news.google.com/rss/articles/CBMia0FVX3lxTE0tUEJTNHNDOWkxOUdmbFI0MHBHbldqNWoydmdhQVZOVG5mR19VRnM2MkJfT3JlVktvMGdxelgxR0VQNk1MajEwUm9KanJuUFl6NzlGejhQYXY5QlFhczY2QUFEX3luNHhNaFpV?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Li Auto</b> (165)</summary>

- 📰 2026-11-17 [Li Auto CEO says Mach M100 chips will gradually be offered to outside customers as robotics firms show interest](https://news.google.com/rss/articles/CBMimAFBVV95cUxPWkJCQWo1VlhxUXQ1Vk9ZRzVzUzRfZFZtX1lBMjZ1bFJjeXZPNWtuUzBmWlozSDlFb1NoelVOS2IxbDhJbmNRWFIxVVBYNy1vZXR3RVRrSEVPdnA4OWpPZGRIa1FaRzY5Vmt0S0s1Ymozc3JzRVpnYzkzaTBNYXpNaXY1WDlKYUc0Ukw5eHRYZFM5cjZRb1FOOQ?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-17 [Elon Musk says he will visit China, renewing hopes for full FSD roll-out](https://news.google.com/rss/articles/CBMifkFVX3lxTE1mUzNSTjVnbWpNU2ZybE9zVWJ6WXgtMDg1V1kyNk0wNVh6RzRRc0pvalVsWi0yQ0ZEWFBUZDlZUDdQYlcwMjYyRWpxd2hCaFdsTlBQMHdOcWVKRjFPZFZjLXVSSGpfckZJSmpTc0RySzFDa2N3T0NXVXVtbWNidw?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-17 [30万预算增程SUV四车横评：奕境X9、智己LS9、理想L8、问界M8谁把配置标配到位？](https://news.google.com/rss/articles/CBMickFVX3lxTE1rUll4d0FUYmV0aUVFakpjN2xNQWpvcW5uUEFCYTRzR2g3X2xQbWw2UkdwLU8xTl9fQjByaWxSb05oQnNjNDh4NGRJbG5keFhCX2RLMGZoS2hrdmozSTZDcFV1S1o2bGhoZEwzanl3d1FXUQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-17 [30万级大六座增程SUV横评：奕境X9、问界M8、理想L9、领克900高配逻辑拆解](https://news.google.com/rss/articles/CBMickFVX3lxTFByWmRaWlNpMHNzWlpidEE4SmFwMXBIem9tc01uSlpJMlRGRDVLdVU3ZFU5WUlJV1ZWbURWU3ZqNl9kWTJiazVTTXZnWUFaM19SQmhwcEkyc1dKcDkyY2plZ3hpbFJtUFNtVGxWX1MwX1AwZw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-17 [【视频】最新到店理想汽车理想L82025款Max智能焕新版](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1lbk51RmR4SC1uNlJab2RHNF9LLTNiMnlndWcyNm5CeGw3Z09pWlJQQ2xtbEx6ODZ2dzJpLVdvQ20yNU5kWnEzdHJsQ1MybmRCOHEwRTRRTDdIaVE?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>NIO</b> (141)</summary>

- 📰 2026-11-17 [Elon Musk says he will visit China, renewing hopes for full FSD roll-out](https://news.google.com/rss/articles/CBMifkFVX3lxTE1mUzNSTjVnbWpNU2ZybE9zVWJ6WXgtMDg1V1kyNk0wNVh6RzRRc0pvalVsWi0yQ0ZEWFBUZDlZUDdQYlcwMjYyRWpxd2hCaFdsTlBQMHdOcWVKRjFPZFZjLXVSSGpfckZJSmpTc0RySzFDa2N3T0NXVXVtbWNidw?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-17 [BYD Denza enters India with D9 and Z9GT EVs](https://news.google.com/rss/articles/CBMiZkFVX3lxTFBKb2FkUVQ4cElJOFJrc3V2czZMZTdES1pBczh6UnlQb0FqOFV5VG9WZEtwdzBqVEZUbXh4VG8tSUg3cjJzUUZSZUFMWEtZVEY3UVBJR0VONnVzdDBLdjUxTHhFNElpZw?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-17 [Li Auto CEO says Mach M100 chips will gradually be offered to outside customers as robotics firms show interest](https://news.google.com/rss/articles/CBMimAFBVV95cUxPWkJCQWo1VlhxUXQ1Vk9ZRzVzUzRfZFZtX1lBMjZ1bFJjeXZPNWtuUzBmWlozSDlFb1NoelVOS2IxbDhJbmNRWFIxVVBYNy1vZXR3RVRrSEVPdnA4OWpPZGRIa1FaRzY5Vmt0S0s1Ymozc3JzRVpnYzkzaTBNYXpNaXY1WDlKYUc0Ukw5eHRYZFM5cjZRb1FOOQ?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-17 [Geely Galaxy releases more M8 images ahead of Q4 launch of flagship 5-seat SUV](https://news.google.com/rss/articles/CBMibEFVX3lxTE9teDBoTUNXOGF1czliOExGS25PX2ZjekMzN3RWZFZfM1NGcGlwUjJ0d1FRZnZnYVRnd3JIV21GSVFnVERHSVpWSlJfVEk1Y2pnOUxfaWx5TUNJQno1aFY1ZmtwMWlmRHBQb2RveA?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-17 [新能源市场太卷了！黑河自贸区蔚来换电站上线运营，-48℃极寒也能3分钟满电](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1nLU1lM0gxTXBrd0VuX255QThXcnhEMlQ1akdMbC1qVjFuTkVyX1Y4dWNaZFVrUmdwN0ItVFduSVctM2ljb2c5UXIzajAzZDU2TXMyZkNHMFE1Mms?oc=5) <sub>网通社</sub>

</details>

<details><summary><b>Huawei</b> (276)</summary>

- 📰 2026-11-17 [Li Auto CEO says Mach M100 chips will gradually be offered to outside customers as robotics firms show interest](https://news.google.com/rss/articles/CBMimAFBVV95cUxPWkJCQWo1VlhxUXQ1Vk9ZRzVzUzRfZFZtX1lBMjZ1bFJjeXZPNWtuUzBmWlozSDlFb1NoelVOS2IxbDhJbmNRWFIxVVBYNy1vZXR3RVRrSEVPdnA4OWpPZGRIa1FaRzY5Vmt0S0s1Ymozc3JzRVpnYzkzaTBNYXpNaXY1WDlKYUc0Ukw5eHRYZFM5cjZRb1FOOQ?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-17 [OLED TV deals at Best Buy: 10 stunning discounts on LG, Samsung, and Sony](https://news.google.com/rss/articles/CBMigwFBVV95cUxNd1JNT0VEWi1BbGlSRTB3dzhvcXI0MHMycE56WXNuT0JwNG5xSHRFckktZU55Z2FNakZoU0FieXlyRTlYN09CS3NWRWJYbWVJWFVBT0tseklfUjBfT0I5ZnE3Tk5tZXpJZ2Y4SGdidUJGM0w5MXI0MG1SY3loOXhGaFF1SQ?oc=5) <sub>Mashable</sub>
- 📰 2026-11-17 [BYD Denza enters India with D9 and Z9GT EVs](https://news.google.com/rss/articles/CBMiZkFVX3lxTFBKb2FkUVQ4cElJOFJrc3V2czZMZTdES1pBczh6UnlQb0FqOFV5VG9WZEtwdzBqVEZUbXh4VG8tSUg3cjJzUUZSZUFMWEtZVEY3UVBJR0VONnVzdDBLdjUxTHhFNElpZw?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-17 [Geely Galaxy releases more M8 images ahead of Q4 launch of flagship 5-seat SUV](https://news.google.com/rss/articles/CBMibEFVX3lxTE9teDBoTUNXOGF1czliOExGS25PX2ZjekMzN3RWZFZfM1NGcGlwUjJ0d1FRZnZnYVRnd3JIV21GSVFnVERHSVpWSlJfVEk1Y2pnOUxfaWx5TUNJQno1aFY1ZmtwMWlmRHBQb2RveA?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-17 [捷途旅行者7 C-DM华为乾崑智驾版上市，超级焕新价18.49万元起](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBKZXhmVG9BMFVNbE9FT1NQUUstcGIyZF9SbXRNNHRjV21EcDhwNXNSQXBudWJZdkY3Q2VLR1pxcFRuNk5RdGttalBENFZUU1p4a3ZMcXVoQ2o1Mkk?oc=5) <sub>车家号</sub>

</details>

<details><summary><b>Baidu Apollo</b> (54)</summary>

- 📰 2026-11-17 [APEC CEO Summit Opens in Shenzhen: Baidu's Robin Li and CATL's Robin Zeng Share Stage as AI and Electrification Take Center Stage](https://news.google.com/rss/articles/CBMidkFVX3lxTE5Bc3UtNW1sRXJhd1NjNXVlNGsyVlpBNFluZDVFMkFuc3dBR2tKa3BRVDhlTGpOdmtISlpIWDJDY3dRWFhpZ3RrQjVSdlp1TlRyVGJnZXNKYkYyTXR3QmtiTVFUbHVITG5wLS1IT0tpTS1mcXh2ZlE?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-16 [Shenzhen Driverless Taxis: 188 km² Baidu License](https://news.google.com/rss/articles/CBMilAFBVV95cUxPNTVZMFVJOVAxMFJiVFpNMWtVRURVSEtrRVd4cjdmNlVaYUhIRHYtNnNaYXI5Y2RsOXBDdndGd3NnYU5QY0kwaG02MEI1QTUtY3BvazRTaGRaaTVjOHZhbm5SVmVZanpsalc3eERjUE1xcS1MWnIzMG8xSW9qTHVVMjBGM2ZlcFI5aFY0eWFTeDdCTTV3?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-16 [South Korean automakers join forces to counter foreign robotaxis](https://news.google.com/rss/articles/CBMiV0FVX3lxTFAtWWlTc190V21DLUJVVXdZSlVLNC1PRWkySmFKemhXTHNMTUpySmVOZVZHSHV5U3A0Ui10YTdqNDRQbkkwNjBtNm9GSWtWLWxORTkyU0YtUQ?oc=5) <sub>매일경제</sub>
- 📰 2026-11-16 [Baidu's AI Cloud Surge Leaves One Big Question About Margins](https://news.google.com/rss/articles/CBMivAFBVV95cUxQV3NITFFfQkRfdGNaY2thaGxkbWUyeEg4S21LQ1dya1dLM2dmY1ZubmszVGpVdFAwODMwV3kyT0FKU1FkclhvODhhZGlsQ2tITnlUdV9pRkpFR1htWTNfbWtSWE5Yd05IcFg2T2FuVFFRVTFlcG1VYUtuek1Kdy1ZX19sRExubzF4MVlDSTI2RDFManFuWWpNRXo2UW9BYXlDS1JqMm9TQ0N2bjNKckl0cHBDTllmV3UxNV84Qg?oc=5) <sub>TradingView</sub>
- 📰 2026-11-16 [Baidu: AI Cloud growth propelled AI-powered revenue up 37% as robotaxi reach expanded](https://news.google.com/rss/articles/CBMi-gFBVV95cUxONDRXdjdlbUt5R0ZteTRmS2IzMENTZlZlN004ckpqcEdtMFFUYmkwMFl6dllNLVpuNlVWQVhkTDU0Q1JyLTFWcHJ6S0M4dWpwR2NKUlJRb0NieURTRXlmbkJfVTI4SUdjeWt1STlZOW02WncxMzZUTUstdkhpU3pOcGM3akVobmJ2MkQ5b2tkc1QyVEEtZGRLVUJjZXhMREZTVmN4RThHR0FfWE9nTzRzQVNaUFozSU0ycGZqNWJFLV9rc0xEZ013N2Z5bXFiTkFlUGdnREkyU1RTaXlTdE5yb19tT3VSUkRtb1VEMTdBcmt3VDJvanpXVGlR?oc=5) <sub>TradingView</sub>

</details>

<details><summary><b>Pony.ai</b> (88)</summary>

- 📰 2026-11-17 [Connected and autonomous vehicles - Pony.Ai and Toyota deploy driverless services in China](https://news.google.com/rss/articles/CBMixAFBVV95cUxOVnB6SkFvT1hlcjNndldjeE1FcFJvVVJhVUQ1NGhYUDdkMlhIZTlxUUJGNmRfRThZdE5aX0tkaXJnWElmd3lzT1dfU093SzhjellGYUVZcldlN3Q1bThvNm1wZDhJc0VmdkhaZnJPbWJtTUdIVGJ6alZsN3B5dEV3VXVaamRhN2Uzd3Brdnc1WEFOMmt3OXFVM3QwM0s5bUN4OGZJQWdRclg2b3BOQWUwRVI2cDI0UlRlNURMNTlERm1mQnZn?oc=5) <sub>Smart Cities World</sub>
- 📰 2026-11-17 [Interview: China's autonomous vehicle ecosystem favorable for foreign operators, says Singapore transport group CEO](https://news.google.com/rss/articles/CBMifEFVX3lxTFAxOE9ldk90N3VNb3Z2QkowMllRRmVnMGNOUDZpVTJkNlc2WU1JV3dJcVRwZmNGOFJiMkdMQThVWmQ1YUVvcGxlR1EtdXV3YkVoaGhPcmpUZmhmdFQydURiWUY2RjBxbXlHR1pEZkYwdnZUVnR4b0ZnMmZfZ2g?oc=5) <sub>Xinhua</sub>
- 📰 2026-11-16 [Pony AI and Toyota launch bZ4X robotaxi service in Guangzhou](https://news.google.com/rss/articles/CBMie0FVX3lxTE9vVWhYZHMweHlIV2c5SnR0RjluOFVqSFM4eFJIR0M0Tmlqb1MzelZ4QWV6cTRUY041ZUhUUlN1djFGZUhybVpwNG1venZCanBHTVVZdmJZWW14RXNfNkdRUUpMSEI5R3RzR2ZMd2hOa1d0U3JDTFFQb3FCaw?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-16 [Pony.ai and Toyota Motor Launch Driverless bZ4X Robotaxi Services in Guangzhou](https://news.google.com/rss/articles/CBMiWEFVX3lxTE5mWXI4MWoxYWo0cHpoUHRYWV9JT0k4bmlyZzYyeThUcHdJQ3dmMS1OVWkwY3pvX0VhN1FMUUVXbUNlVl9lLTRVcEJGNGYwWXhHQ3NQWXNUNU8?oc=5) <sub>www.tokenpost.com</sub>
- 📰 2026-11-16 [The driverless taxis, robots and tech companies in APEC host city Shenzhen show China's ambitions](https://news.google.com/rss/articles/CBMiqwFBVV95cUxPVnU3ZUZMRW5YOS1tbEgyNmJhcWVCRW9UZmZOdGM5dG05SjBPMGdEN29Ydm9kdm5iaEk0U1lCeU4wLW1NLUR2OXJDMUVfNUdyUVYxc3VpZFliQU1qM3ZVY21lNGQ5czRtdm8yQThLejJLQ00zYVZkV2ttV0Q2bVJzeHJDV21mbWNCVEVVanF5RFdfajVZZGtRR0VkVDZfUkxYVnhXdVVxMVpCTzQ?oc=5) <sub>Alton Telegraph</sub>

</details>

<details><summary><b>WeRide</b> (106)</summary>

- 📰 2026-11-17 [XPeng's Q3 revenue hits record 24.28 billion yuan; He Xiaopeng says scale effects will show quarter by quarter](https://news.google.com/rss/articles/CBMidkFVX3lxTE5pcmRjTkRyM09Id3RvSHpBRnlhYmlOdkNXeG8ySF9FMndvRlBad1g4dzRNT0FWRFRfSkFOT19ER2hodUZpdm83ZTBZa3FNWkQzaVZQdmJoQk5FU0EyaG1MZ3p6R2RucWFTelg3N2d2SVd3TVdNd1E?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-17 [Xpeng Q3 revenue rises 19% as deliveries hit record high](https://news.google.com/rss/articles/CBMijAFBVV95cUxOYWlsQ0hkOHN0RmUtLU5DbkdUS1lxdi1fOUtESW41dnVqblJtZDVGOEJjMW9rZUx5dEVMOUIzc3pVZVAyMGRMTTdkNmtHdE14dXlsTkcxNk1oYm9oSjhYemVPU3l4NXZDSVZETW1KajJIaUFrdmduSUpOYTBMdi1QZVlTdVNJeTU0ZktiNA?oc=5) <sub>Tech in Asia</sub>
- 📰 2026-11-17 [文远知行将于11月20日盘前发布财报，一图速览分析师最新预测](https://news.google.com/rss/articles/CBMitAFBVV95cUxQaEZJX1lzXzV3cmpSSFI3bU1NRVY2b213MWItRFBEQ3J4ZVQyeER2Qk5kTXpQMjFoZjdycnp3TXZSU1JkOGphRTdKM1UxQndCUFlJUFQ0enNraVJDYWhJeFBkSnJxaXVBRVlQQUxWWDFORjYxbDhOcVVOUlhYdXhNR01JV3pCa1ByeGFmWVJBQWg5VjFXbEZ4Q0R2ZnVGTkRhV2ZRNTFfMTJ1WVpIbFc2MXFYX0w?oc=5) <sub>Moomoo</sub>
- 📰 2026-11-17 [【视频】与L4同源的一段式端到端智驾夯中夯10万出头就能上车？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1SX01FemFpRVFObC1sWjkxMi1GcjN3NGNNX0lneE1VUGdCRTNfVE5xWWJRVGVFbDFBZGZMWmVxT1kyaC1WTkJZSnhvekJuQTREczBOdVNSVXloMVU?oc=5) <sub>车家号</sub>
- 📰 2026-11-16 [特斯拉FSD准入引讨论！文远知行L4 Robotaxi已在国内多城落地运营](https://news.google.com/rss/articles/CBMijAFBVV95cUxQNGktZ0FBclhpVzNJbkZDUktLZEJ1Q095MHNzUDNCelV5SjVEWklfaVQwMXJYcGRvbGJmOW5jV0E4LURqYVA1c2FjQWplTnFkRTVsUHA0elBJam5UNHZWekFGWk94c1BVRkd0VVlmeVJnWXVlY05GZ2lsd0lBcUNSdE5UMmVXekRWajFNRw?oc=5) <sub>Sohu</sub>

</details>

<details><summary><b>Horizon Robotics</b> (95)</summary>

- 📰 2026-11-17 [ID.AURA T6用户真实测评：13.59万起的德系智驾到底值不值？3个维度说透+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1lMWlqRVdnTDVDWlpmNXR2VmRsZG1Ec0dzd2I5TnJkR3Z2dUZqTWFpX0VWMEpiS3pCcUFPR19jQ1RHbjlqSnp6OUhMb1k2cDJhS0YzOGp2aVZaQTd6MzVz?oc=5) <sub>新浪网</sub>
- 📰 2026-11-17 [地平线炮轰算力虚标，Momenta X7 Ultra甩出700TOPS](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5xVlAwbnRyUGpDXzJwOG5FX2VNTWFRRXlDMzhwLTcwRl9VTS0wcUlUUGo4dTM2WFlqS3FubmUwMEFMbzRmR2E3MzZXdGtSb0plVUJsRkZKUHdIN1E?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-17 [Momenta上市市值696亿港元，余凯炮轰算力虚标](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1TRGRueUk4aGhZcTAzVHU0UGE0OG1FU1FZVTgxYmc1cXNtcDRWWlNlRERVbVB0eExvSXVsc01JTnBZR2dZak9KZ3JEMEdWQWhOS0s1ZUdiYm5vLWs?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-16 [SAIC-VW ID. ERA 5X hitting the market](https://news.google.com/rss/articles/CBMiggFBVV95cUxPWDBrZFRDNVA0OEpaNVNuQm4tclF2aDlBQ1hXd24zbWJxRXlyNzVFd3RObk1ldEt1dk9LZmI2ZjNKNHBCUU8xUVFuMGsyQnB3c3U3VUREYkJ1UFdzWS1oZFNaRHU2dkJIbDNOUGxYbFlmLTExdnBFd2Zmcmx6SlBRYXFn?oc=5) <sub>China Daily Global Edition</sub>
- 📰 2026-11-16 [【视频】304不锈钢油箱都用上了！iCAR V27 底盘用料怎么样？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE92amwyLUF0MERlSEFMWm5Sa2lwc0Fyd1dLUzRjZW9ybmxzZXpIT0NvQmw3LXpLbGRkSnNScG1xZlI4blFjUC1fMGRFQ1FXR2FpbU1vQzlVMG5CX1k?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (22)</summary>

- 📰 2026-11-16 [又一“国产保时捷”？赛豆ME7实车到店，大过小米YU7配571马力](https://news.google.com/rss/articles/CBMia0FVX3lxTE5fWTNxTkVfa2RHM29CZ3JabmtSbllKTVdGN2x4aVpqS0U0bG81RTFHeDhqNHZhaUg3MGJFVjEzOVU3aDdIMS1zR05mNXZ0blNyZ3cxVWRnVF85bmc3Tl9aenNZSlpDaWRDSV9n?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-16 [AIVA ME7实车到店剑指25万级轿跑SUV市场](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5fM1B6RnpLTlpiVEtIUmJaR0Ffci1BVVpqTzY0ZnBab3JSZ2luNDRWeEhPeHJ6YXlaek9BRDZvdmU0TEw3d2JXTVdMbHgzLXh3TWhLTmpCTDlvdw?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-14 [DeepSeek无人创业](https://news.google.com/rss/articles/CBMiTEFVX3lxTE1QUnM4dm1XbE8tWmIwSE1hN1JMTjZKRklrM3FmbkdNbVd2WllWUWpjQVhYV0xwaHhqUHp4T2ZkMGpHMExqWjFNU1lPYXo?oc=5) <sub>凤凰网科技</sub>
- 📰 2026-11-13 [【视频】小米澎程N90和特斯拉Model Y L怎么选，同价位还有哪些推荐？](https://news.google.com/rss/articles/CBMiW0FVX3lxTFB6dElibXRFYWFsZU9vQnhjX3YwZjF2VVd6QjhLdXJIV3pmRGhzTmpuTFRER2xXV1Zjc2ZqNld2RVY1MkxrTENqczVRc2MwNHl1VFljSkt2TjRxZ0U?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-13 [Valued at over 500 billion yuan but barely producing founders: Why DeepSeek has become a "settling pool" for AI talent](https://news.google.com/rss/articles/CBMidkFVX3lxTE5BN29naDgxcE4xa2NUUi1qSlFKTHpBZlVjVVozN2FaWS1kVy1ENkxsV0dxVTlQS0ZJWHkxV3lfY09LN2xldl9XYk1mTFA1SjBUdTJfV05LYWllNFJZZ3RwV1VPSmNQZGk1a085UGFMOXloMHE0d2c?oc=5) <sub>BigGo Finance</sub>

</details>

<details><summary><b>Mobileye</b> (13)</summary>

- 📰 2026-11-16 [When Human Superstars Shine: 9 Unmissable Historical Snippets Between Elon Musk and Jensen Huang](https://news.google.com/rss/articles/CBMiU0FVX3lxTFBjclJYNXBJbVBjYUxUQkJCU2pOcDBpVnZZZ2lqWDhZY3lzYk1udjlFWGxNS3loQjAtUDdKYXJySWZWZTJLQ1I1UGtueDdvd2E2RGdJ?oc=5) <sub>eu.36kr.com</sub>
- 📰 2026-11-14 [May Mobility plans 10,000 ID. Buzz robotaxis on €9 million revenue](https://news.google.com/rss/articles/CBMihwFBVV95cUxQdkgzeUVTSS1wc1czVWhUTllrV1ZaVk1VLUUtUTVhTlFVSnJVSGFvcmtvRC1QZHNnWUxHY1B6c3gtUjZqdzFRSm9CSTNuZENtdFlRZGpoaDZGalJQb2xmZ1UtMGJyX1JObkdfaVF6SThudG9kajdDaW1xZVY4dzFraUF6NXd5RVk?oc=5) <sub>AutoNext.co</sub>
- 📰 2026-11-13 [Automobile manufacturing stocks Q3 recap: Benchmarking Tesla](https://news.google.com/rss/articles/CBMivAFBVV95cUxQemM0Qm9BZXFLb2o3YWdJWkFwb1FLcVdMb3NZNDE2bTB2U0hTb29PbnRiQXhFejA3ZklYUEdTR1lZaGpFT2tjOWJPT0luaXF2aXI2ekRhSlhPQnpQNWxQQUpLdTAyeWxvN2dBV2dNcEhiM0VDOWtwNzNtUHlSVVBmMVR3eDZKTWtXSWRvTUd6V1FhVzRqX0MyMDZjQm4xdjAwRmREZEl1X1V3b25CVk9MSUF6Q1draU9nZU1peQ?oc=5) <sub>TradingView</sub>
- 📰 2026-11-13 [Korean Optics Maker Optrontec Triples Profit as US Automakers Replace Chinese Camera Suppliers](https://news.google.com/rss/articles/CBMi3wFBVV95cUxPWHNlSUphR3lWUXJBNm93Mm1QdFZ1MVVSZU9jTlBxc0ZuR3JyU3pYQU9OUmk4VDh1NnhCMnV3dXdSenBkVldzS09Zb0NVeGJSc1V3aXhiU1E1aTNsd1RydXlIT2RDdDk5SWZUOC0zbTNlbUxxZVpMaUdIcm1lRUM4U1k0TVBhUmNtMXlCUDh2Vzd3dXE4aGxCRDZlaU5MZFNHNllfRDM3dXoyRWlTckRFREZfRjBpNjhLaW5YVkd3OWJuQWRLVmE2ZFpOck9zdXZrYnVXZk5pYks2WnFKNURZ?oc=5) <sub>Tech Times</sub>
- 📰 2026-11-12 [JPMorgan Downgrades Self-Driving Technology Supplier as Volkswagen Faces Delays](https://news.google.com/rss/articles/CBMi1gFBVV95cUxNRXhmZ1ZxandRVnNmaEhwZmljMjNVemVoUEIzVFZPQWlGQ0lxeTNES2JuczR4dnZiU3hpUWlydklMWXVLeW5tWVBFSVVlY2hfXzM5dm4yWEZ4UmJYcTdJU2o2MWZhS1VMWkhwb281SndVb1BkN25QTUV3TURlUmxVTzdYTUFDVFVVTkdKRk1wVlpzMmZ0QjZqWUw5ZDU4dnV0bXhzZEtJYll5SkFlZFBxWFU2aGFvYVZLWHQ1d3RfZDdrdVFzQkVUd09lUjlqYjVTWlNSZDhB?oc=5) <sub>TradingView</sub>

</details>

<details><summary><b>Aurora</b> (31)</summary>

- 📰 2026-11-16 [Archer Aviation And 2 Financially Strong Penny Stocks](https://news.google.com/rss/articles/CBMijgFBVV95cUxQYmltdUpDelBpOG1FeUtfUkRadFA1NTM5VmVVLUtHbmI3ZndHYUlMWWpJX3FaVmVXcEMtYkd3YUhsN29hZjdmOWw0QS1NRGRTNDZmN0syTmRaUTlxUGgtSS1jQXc4OTVxM0o3bVVMLTdmMkV2MENfTk9abEFXdmxHb0pucEJQaDZJUHY1TnNB?oc=5) <sub>Yahoo Finance Singapore</sub>
- 📰 2026-11-16 [Which Penny Stocks Are Drawing Attention for Stronger Balance Sheets?](https://news.google.com/rss/articles/CBMirgFBVV95cUxPcWhuMFBKNEtPclVId0laSWhGdndMYlJxZEZhUWE2ZFYxVk5RUzM4Mkotb29XYjFiTmlQSDhDTzJETUpicXJMazc0SUxBWnkzdmQ3M0l5UjVOSFMyWDVuei1TQUl2MFRTT2FUNXFxdE1NZktJN05OZnBuMG51dkxfdjZUZ0pWNGxFMVBPbkNjdjFKQVZUNzQ5WXNnbGZFcFhOOVJLSXpVM3NZbFlGQ3c?oc=5) <sub>Kalkine Media</sub>
- 📰 2026-11-15 [Archer Aviation And 2 Other Penny Stocks To Watch](https://news.google.com/rss/articles/CBMixAFBVV95cUxPMmkwbVE5akZOMWNlM1ZOMzhiRERnSDM5Y2hxc1dPYzdPN2xNdW11RnZXMXlfb09vQ0FpaUNwQnVlM1BYekRKMlpwU2h2OFRkU296MG4weU0xbENsejRhelMwR1AtclowWDhtZkd3WGdISDBjWWRCTTNUT2tWcXN1S05rR0lFLUlQVEpOSHJwc0VqcDVJZ3YzcWRncGZUTk5OU1UyUVhHVl92OFJ6MGxuWWRtTUthLVBEeldqcDVuM201VHVF0gHKAUFVX3lxTFBVM0k1cUlMdzFYUy04cDBhN1IwU1J4cWkxQzlOY2VyNUJjQWk5VHlrWVlBcVlrRnBkY1JXdjFCUm9Fa1VxLXVKSWpxdnJQV3U3OEtFdVhmSDhaUHMzR016a1FOMkpCQjN3bmZUTGVCTnVuaE9wX1dCbkJtb3FKSzE5TGNpbmMzbDNFQWFaRkpqSVRFdXhHaFNZa2F5OElxZzhBS3VwMXlCMW5DLWV3bmhhck1HdTVhZ1VLLWptcTZtQXhYa0l5aEVPN3c?oc=5) <sub>Simply Wall St</sub>
- 📰 2026-11-14 [Should Truck Production Delays Require Action From Aurora Innovation (AUR) Investors?](https://news.google.com/rss/articles/CBMi0AFBVV95cUxQM0Z3WEJQclFZaGZESEs2VUNRSXRLVnAzUW9Mdy1hSFQ0QTBXdWs2ZVd1SDdFQXBFZWhGM0IxamZKcmN6VGQwaGpORzFNdEZvUE16T1pDN3VGa3pmRmR4VHF6YV9yMFBVYnllUnlOdmxzWUR4bzhab1A2dlVNSFllS0NmQXBJQ3BRcDN3V0wtQy01R1R6ZmQ2SHpkTFFVNTBmZEdTTGlJVmV1YWtHX1F4c0lJWlljVXZkbWlKTlZjMDhLQlgxWGtrN1pJc0RJYVhO0gHWAUFVX3lxTE1VS1NpejQzUVhxSnEwMjZ1NE53QUlwMHZ2dkxRNFhpSlE2RHJpeEZ1ckZFZlZQMmxGbXYyRHNXaXNWLWNrODc5eW1oTURNc3ZSUVZOY0FpaEh0UEZUcjJMZjJJWjFLWDNxX1VEVzE2a2NGTEtwZDZjOHctVE53Q094YlY3c2NybEN4UTV6MEZSTjlvRlhWc2M1VjdlaUxoM2ZqTW5QRkVTVWR0a2hnV1ctejNVaFdiaXNzakV6ZGRIblEzVVp4Y0x6dF9xM0RiV2lCcDFFR1E?oc=5) <sub>Simply Wall St</sub>
- 📰 2026-11-14 [Aurora: 3 Key Takeaways for Long-Term Investors](https://news.google.com/rss/articles/CBMilwFBVV95cUxNMVFqdzVjR2I5Ulp3TldKbTdXUWprU1BmWTAwMXJOTVl2cWQwZGdNTF9qRlIwVFp0OG9Qdk9QcEY3VG81cG9iV3dFTWVRRFltM3I4ODRDQ2pNUUlhc09zS2Q5ZU85RVNoUHBOb0Y5R1FRZXJ0V1I2Sk9kVUpjdlU0bFpCM0N5TUY1NUxONDZMN2pBeWs2ZVBz?oc=5) <sub>Yahoo Finance</sub>

</details>

<details><summary><b>Zoox</b> (80)</summary>

- 📰 2026-11-17 [Zoox robotaxis arrive on the streets of Atlanta](https://news.google.com/rss/articles/CBMiywFBVV95cUxNbW1iU0d6MG5TRkVjak16bFBhVU9pN0VNWGhjWHJCNVpjdVhSNVdWXzlDYzJsNmNXVGlGd0FGVnFlVkV2SnJvWVNGM3BpTlFnbDdpSVhXLVI3NXlsNVZidU9kOFVfZ3Fpa2Z4TkwtN1VVOVU4QjJTYjgyei1ZT25SS2RrUkhhYS1YczBxQ0xpUlBKTFMxS09NODF2VnNnazhzR3JjVGxEWkFVSm03TllSX2tlcFNqcGVXSFpfdUd0cm8wb19SbnR3cEd2cw?oc=5) <sub>WABE</sub>
- 📰 2026-11-17 [Zoox is now available on Uber in Las Vegas](https://news.google.com/rss/articles/CBMiXkFVX3lxTFBJYzlUTVpudTFTX016bV9pMUZSOUpKVUl2SDM1S1NBSzczdEYzWU9IVHJicHRqdjdiT1Zyd0twM1kwZDE5cUlDYzhZeHhOY25tYjFrR1NMTkV5MlU5dVE?oc=5) <sub>Uber</sub>
- 📰 2026-11-17 [You can now get a Zoox robotaxi through Uber in Las Vegas – KLAS](https://news.google.com/rss/articles/CBMinwFBVV95cUxNNVZfa3lPeGkyQzY1Wng2TkhhM0U3OXFHVzVjSm5tdnpPZ2tZSENsc1Jwa1h6OVRuS29oRlJyU19UbkNxQXpDZ0twbzhqQk1vLWZDT2JvOHo3Tmd5VDVQSUxVSXM0eDZUd3dGTjQ2WUF1anNYZlM0V29GeHBocDk3UGdsS2NZM0JyNVlEVUNLd1FDMEVQMVJMUHVoemlJYUk?oc=5) <sub>KLAS 8 News Now</sub>
- 📰 2026-11-17 [Uber Adds Zoox Robotaxis to Its Las Vegas App](https://news.google.com/rss/articles/CBMia0FVX3lxTE55THR6a21GRF94YzIxNDhmc2pPeFJjeG5sMnhWOFNYNV9tTDY5U3Z6TnE2SF9sZEEySUl0UGZJT1hHWTE0NEF4SlV3eF9VYm90RzNuQi0wYUNfSjBQU2ZhSEtvdEREa0gyOHNr?oc=5) <sub>WeRSM</sub>
- 📰 2026-11-17 [Uber Adds Zoox Robotaxis to Las Vegas App](https://news.google.com/rss/articles/CBMigwFBVV95cUxQTEdCcVVOSDlsRXpPZFUzUHdTM0V2bmtSQVdXeEt0bTAzN2RDN3ZJNVBKbDB4UVNlUF9SVmNFTTBuaHpXX3A0ck9XRVdxMHdXOFAweDItQTF0a2twM0hReWJwTjlXYXAyV0FtOXJueGtkWkFucXk2dEY1WDB3SjdrZkR4UQ?oc=5) <sub>Briefs Finance</sub>

</details>

<details><summary><b>Motional</b> (23)</summary>

- 📰 2026-11-17 [Uber Adds Zoox Robotaxis to Its Las Vegas App](https://news.google.com/rss/articles/CBMia0FVX3lxTE55THR6a21GRF94YzIxNDhmc2pPeFJjeG5sMnhWOFNYNV9tTDY5U3Z6TnE2SF9sZEEySUl0UGZJT1hHWTE0NEF4SlV3eF9VYm90RzNuQi0wYUNfSjBQU2ZhSEtvdEREa0gyOHNr?oc=5) <sub>WeRSM</sub>
- 📰 2026-11-16 [Uber Starts Offering Amazon’s Driverless Zoox Rides in Las Vegas](https://news.google.com/rss/articles/CBMitgFBVV95cUxOcXdqaVIzMmoxQXdXNG9EZWtCMnpSNTB4Z1duZEEzUGt2N2p1SUZpc1IzNTJKb2VwUVIxZVBDTFNfU1hSNVdFT0JuN25zOHdCc1J6YUgyUTV1LXV6ZjRpcnk2YVpQS0RmMTZsSk1hamVNbUp3cjVjWWQzQ041SG5OZnZuLUVubzFqa1Uyb2lqZEEtZTA2QmdQLVptNkt4UlRXRi1KS01sV1BIaFF4Vk15WE9WcU53Zw?oc=5) <sub>Bloomberg.com</sub>
- 📰 2026-11-16 [Hyundai Motor standardizes sensors across Kia, 42dot and Motional to integrate autonomous driving data](https://news.google.com/rss/articles/CBMicEFVX3lxTFBRM2t6aWZ0R3FTeXR6dlZrenFLbDM4YUlRbkRBX2p0VGY2dGwxcGtNUHB6WGxVV1N2XzNwZVRwN1g0d05lVDdZOWI2QmxYbTVxWGZNOEhoM1JtdnJnN3NWT1V4ZjZnWWFySlV3SVcwZms?oc=5) <sub>머니투데이</sub>
- 📰 2026-11-16 [In Vegas, Uber aims to end robotaxi crapshoot](https://news.google.com/rss/articles/CBMib0FVX3lxTE45RnFPMWxRaHFmVG02S19acy1WQVQxcUl6Snd2bUlEdklJSkhxTG9mVnNYQUNCdXM2eTVGNm56R0U2RjN1NXd4Y1hvcHNIemFWcDdoSzRRZjJsUVhpaXgtdndMeHAxdm9qd3lxcDJ4QQ?oc=5) <sub>Axios</sub>
- 📰 2026-11-16 [Uber started offering Amazon's Zoox robotaxis to riders in Las Vegas](https://news.google.com/rss/articles/CBMiZkFVX3lxTE1RVDhRS1l3ZmZhZ3pPTkpCWnI2SnFNZ3JPS2R0ZWVFcFo5QVBVLVJFV253SjdTR0lKTlVzTGxJUThYZFFIRm1QdVNkc1RKeTc4VlFlWThYNlFMZDhoQXJjU2x0QVN4UQ?oc=5) <sub>Quartz</sub>

</details>

<details><summary><b>comma.ai</b> (2)</summary>

- 📰 2026-11-12 [Goodbye, BlueCruise! We Install a comma four in Our F-150 Lightning](https://news.google.com/rss/articles/CBMirwFBVV95cUxPY1o5ekZ4WnpraUxVMHV6OVdyMEtEbjQxQXY5STdJdXlHNlN6eUFZNzFwSnA5cFhHd3pNdTZNNy03dXBOZ1ZoX3RFX2E5V2JNTE9aVlhJaG90bW5YWEdzX2NGXzd3VFZ6NG5JVkFrM3daTmY4UDBTN1I4NWU3eGJqUm9tY1VaRWxoZkp3WDJLNnVLQjN5WG9NMzlxLWI0aVU2TFhLUEZwUE5YUDdUcWFJ?oc=5) <sub>Transport Evolved</sub>
- 📰 2026-11-06 [Canadian YouTuber Linus Tech Tips Tests Tesla FSD](https://news.google.com/rss/articles/CBMiggFBVV95cUxNZVZaT1Q4X0NlakJzTnFkTGdqTmFPM3pDbFZPUnBYVVNrVzFxMlpZQ3VaTEJFUmJrNVpjMmZ5RVphUDE4WURNT0x4NkhnN01LdTdzSEVnS2NUNkROams2cnNzNkpnalhWcDVuckhETUtxaDZrSHNXTXhKYUlpN2dPTlZn?oc=5) <sub>Drive Tesla Canada</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
