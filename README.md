# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-11-20 · 1,288 papers tracked · 49 curated.

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
| [Teaching Vision-Language-Action Models What to See and Where to Look](https://arxiv.org/abs/2607.01658)<br><sub>Yuguang Yang, Canyu Chen, Zhewen Tan et al.</sub> | ECCV 2026<br>2026-07<br>📑 3 | [⭐ 38](https://github.com/ShivaTeam/DriveTeach-VLA) | Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving |
| [SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving](https://arxiv.org/abs/2610.20609)<br><sub>Shaoyuan Xie, Zihan Zhang, Jingxuan Wang et al.</sub> | CoRL 2026<br>2026-10<br>📑 1 | [⭐ 36](https://github.com/ASGuard-UCI/safedrive-vla) | Vision-Language-Action (VLA) models are gaining attention in autonomous driving, inheriting commonsense priors from large language models (LLMs) and widening the navigation interface from a fixed command set to free-form… |
| [Scene-Adaptive VLA: Efficient Autonomous Driving via Dynamic Layer Routing](https://arxiv.org/abs/2610.24590)<br><sub>Yujia Yang, Quan Yuan, Jiawei Fan et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 5](https://github.com/yang-luvu/Scene-Adaptive-VLA) | Vision-Language-Action (VLA) models offer a promising paradigm for autonomous driving |
| [Locating and Repairing Domain Shift in VLM Trajectory Planning](https://arxiv.org/abs/2611.10720)<br><sub>Zhihong Cui, Hengyu Liu, Michael Alexander Riegler et al.</sub> | NeurIPS 2026<br>2026-11 | [⭐ 0](https://github.com/ZhihongCui/MoLaRx) | Vision-Language Models (VLMs) are increasingly adopted as end-to-end driving planners, yet they suffer from cross-city domain shift |
| [AutoVLA-D: Learn a Trajectory-Geometric Condition from Reasoning for Autonomous Driving VLA](https://arxiv.org/abs/2611.12382)<br><sub>Yuguang Yang, Zhewen Tan, Canyu Chen et al.</sub> | NeurIPS 2026<br>2026-11 | [⭐ 4](https://github.com/ShivaTeam/AutoVLA-D) | Autoregressive VLA planning usually predicts continuous trajectories as the final output, but driving instructions often describe actions rather than ego states, which weakens direct conditioning on the final continuous … |
| [CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving](https://arxiv.org/abs/2607.04179)<br><sub>Zhaohong Liu, Hao Ye, Xianlin Zhang et al.</sub> | ECCV 2026<br>2026-07<br>📑 3 | [⭐ 1](https://github.com/MICLAB-BUPT/CritiqueDriveVLM) | End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving |
| [PixelPilot: Scalable Vision-Language-Action Models for End-to-End Autonomous Driving](https://arxiv.org/abs/2607.04637)<br><sub>Pin Tang, Guoqing Wang, Xiangxuan Ren et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 2](https://github.com/VISION-SJTU/PixelPilot) | Vision-Language-Action Models (VLAs), which leverage the advanced reasoning capabilities of Vision-Language Models (VLMs), show promising generalization in complex autonomous driving scenarios |
| [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)<br><sub>Nan Yang, Zhanwen Liu, Linfeng Zhang et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 11](https://github.com/Zizzzzzzz/MVPruner) | Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings |
| [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)<br><sub>Yuan Gao, Wenting Miao, Mattia Piccinini et al.</sub> | IROS<br>2026-07<br>📑 1 | [⭐ 33](https://github.com/TUM-AVS/Chat2scenic) | Validating autonomous driving systems requires diverse, regulation-compliant test scenarios |
| [GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives](https://arxiv.org/abs/2609.39601)<br><sub>Qize Yu, Lianrui Fan, Boyu Chen et al.</sub> | arXiv<br>2026-09<br>📑 4 | [⭐ 441](https://github.com/groundingpi/GroundingPI) | Precise grounding matters |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 21 | [⭐ 563](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
| [GRAVA: Grounded Reasoning-to-Action Representation and Learning for Autonomous Driving](https://arxiv.org/abs/2609.15169)<br><sub>Xiao Liu, Haoyu Li, Jianghao Leng et al.</sub> | arXiv<br>2026-09 | [⭐ 487](https://github.com/AhernResearch/grava) | Driving vision-language-action (VLA) models increasingly reason before acting, but their intermediate reasoning is often weakly grounded in physical scene evidence and loosely connected to executable behavior |
| [Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air](https://arxiv.org/abs/2605.31066)<br><sub>Tianle Zeng, Yanci Wen, Xueang Yu et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 1,139](https://github.com/louiszengCN/CarlaAir) | Recent aerial vision-language-action (VLA) models show promising single-UAV capabilities, such as tracking moving objects and navigating to language-specified landmarks |

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
| [MOJITO: Modal Joint Learning for Unified End-to-End Autonomous Driving](https://arxiv.org/abs/2607.23511)<br><sub>Zhijing Cheng, Xuancheng Zhang, Donglin Di et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 32](https://github.com/mumucc01/MOJITO) | End-to-end autonomous driving systems commonly follow a cascaded two-stage pipeline where a perception stage compresses multi-modal sensor inputs into a compact context and a downstream planner predicts trajectories cond… |
| [UNIVERSE: Unified Video Action Models for Autonomous Driving with Flexible Mask-Modulated Modality Generation](https://arxiv.org/abs/2607.05133)<br><sub>Mengmeng Liu, Diankun Zhang, Jiuming Liu et al.</sub> | NeurIPS 2026<br>2026-07<br>📑 15 | [⭐ 6](https://github.com/xiaomi-mlab/UNIVERSE) | World Action Models (WAMs) can improve action generalization in autonomous driving by learning scene dynamics through dense future-video supervision |
| [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](https://arxiv.org/abs/2609.26792)<br><sub>Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.</sub> | CoRL 2026<br>2026-09<br>📑 1 | [⭐ 15](https://github.com/VAIL-UCLA/DreamStream) | Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions |
| [DriveMLP: When Training Strategy Outperforms Model Complexity in Autonomous Driving](https://arxiv.org/abs/2610.29676)<br><sub>Alessandro Canevaro, Julian Schmidt, Hang Yu et al.</sub> | CoRL<br>2026-10 | [⭐ 6](https://github.com/alessandro-canevaro/DriveMLP) | Learning motion planning policies that remain reliable under closed-loop execution is a central challenge in Autonomous Driving (AD) |
| [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)<br><sub>Shen Zheng, Anurag Ghosh, Gaurav Parmar et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 32](https://github.com/ShenZheng2000/WarpI2I) | Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs) |
| [G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance](https://arxiv.org/abs/2606.26017)<br><sub>Hang Yu, Ye Jin, Alessandro Canevaro et al.</sub> | IROS 2026<br>2026-06<br>📑 6 | [⭐ 7](https://github.com/HangYuu/G2DP) | In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors |
| [SimWAM: A Simple World Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.07468)<br><sub>Zongchuang Zhao, Xin Zhou, Tianyang Xu et al.</sub> | arXiv<br>2026-08<br>📑 17 | [⭐ 212](https://github.com/H-EmbodVis/SimWAM) | In autonomous driving, World-Action Models (WAMs) have improved end-to-end planning by transferring video dynamics priors to action prediction, but many still couple planning with future-video generation at inference, in… |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 21 | [⭐ 367](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
| [Latent-Centroid Steering: Single-Pass Classifier-Free Guidance for Command-Aligned Autonomous Driving](https://arxiv.org/abs/2608.00237)<br><sub>Meibo Hu, Jiamian Wang, Pichao Wang et al.</sub> | IROS 2026<br>2026-08<br>📑 1 | [⭐ 2](https://github.com/codingmlinprocess/LCS) | Vision-language models (VLMs) have recently emerged as a promising paradigm for end-to-end autonomous driving, enabling agents to map multimodal inputs and high-level navigation instructions directly to executable trajec… |
| [STAGE: STyle-controllable Action GEneration for personalized autonomous driving](https://arxiv.org/abs/2607.29517)<br><sub>Zihao Liu, Xing Liu, Yizhai Zhang et al.</sub> | RA-L<br>2026-07<br>📑 1 | [⭐ 5](https://github.com/CarlDegio/STAGE) | Driving style refers to the behavioral preferences that drivers maintain during driving, shaped by their diverse experiences, habits, and needs, and is typically reflected in varying levels of aggressiveness |
| [A Survey on End-to-End Autonomous Driving Training from the Perspectives of Data, Strategy, and Platform](https://arxiv.org/abs/2610.00926)<br><sub>Chengkai Xu, Yiming Cui, Jiaqi Liu et al.</sub> | arXiv<br>2026-10<br>📑 6 | [⭐ 110](https://github.com/Jiaaqiliu/Awesome-Training-Ecosystem-for-E2E-AD) | Autonomous driving is a cornerstone technology for the future of intelligent transportation, where end-to-end learning has emerged as a transformative paradigm that directly maps multimodal sensory inputs to driving acti… |
| [AutoE2E: Don't speak - Language free end-to-end autonomy A Real-Time Driving Model for L2++ ADAS and L4 Robotaxis](https://arxiv.org/abs/2611.22374)<br><sub>Muhammad Zain Khawaja, Zaynab El Mawas, Ryota Yamada et al.</sub> | arXiv<br>2026-11 | [⭐ 227](https://github.com/autowarefoundation/auto_e2e) | AutoE2E is an open-source end-to-end driving model developed by the Autoware Foundation Robotaxi Working Group |

## 3DGS / NeRF Reconstruction & Sensor Sim

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [MCSplat: Multi-View Photometric and Geometric Consistent Feed-Forward Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2610.25345)<br><sub>Yifei Wang, Wei Tian, Wenhua Bao et al.</sub> | NeurIPS 2026<br>2026-10<br>📑 1 | [⭐ 12](https://github.com/yfwang0824/MCSplat) | Driving-scene reconstruction via feed-forward Gaussian splatting from sparse multi-view images remains challenging due to two factors |
| [DriveWeaver: Point-Conditioned Video Inpainting for Controllable Vehicle Insertion in Autonomous Driving Simulation](https://arxiv.org/abs/2606.31918)<br><sub>Junzhe Jiang, Zipei Ma, Zijie Pan et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 18](https://github.com/LogosIntelligenceLab/DriveWeaver) | A pivotal step in autonomous driving simulation involves inserting foreground vehicles with predefined trajectories into simulated scenes |
| [Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796)<br><sub>Leshu Li, Jie Peng, Yang Zhao</sub> | ICRA<br>2026-06 | [⭐ 15](https://github.com/UMN-ZhaoLab/Pocket-SLAM) | 3D Gaussian Splatting (3DGS) has garnered significant attention in Simultaneous Localization and Mapping (SLAM) due to its advances in capturing fine-grained geometry features and synthesizing novel views |
| [NIDAR: NIR-Guided Intrinsic Decomposition for Scalable Scene-Agnostic LiDAR Intensity Reconstruction](https://arxiv.org/abs/2609.36878)<br><sub>Junjie Zhang, Jie Yin, Kefei Qian et al.</sub> | IROS 2026<br>2026-09 | [⭐ 25](https://github.com/Zjj587/NIDAR) | LiDAR return intensity provides complementary surface-response cues for robotic perception and state estimation, yet many simulation pipelines omit it or reproduce it using reconstruction methods that require real intens… |
| [MM-TRELLIS: Point-Cloud Guided Multi-Modal 3D Vehicle Generation in Autonomous Driving](https://arxiv.org/abs/2606.24301)<br><sub>Hongli Xiao, Youjian Zhang, Yucai Bai et al.</sub> | ICRA 2026<br>2026-06 | [⭐ 10](https://github.com/HongliXiao/MM-TRELLIS) | Recovering realistic 3D vehicle models from autonomous driving scenes is crucial for synthesizing training data and building simulation environment |

## Perception: BEV, Occupancy, 3D Detection, Mapping

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Deformable Gaussian Occupancy: Decoupling Rigid and Nonrigid Motion with Factorized Distillation](https://arxiv.org/abs/2605.28587)<br><sub>Yang Gao, Wuyang Li, Po-Chien Luan et al.</sub> | CVPR 2026<br>2026-05<br>📑 2 | [⭐ 25](https://github.com/vita-epfl/DeGO) | Understanding dynamic 3D environments is essential for safe autonomous driving, particularly when reasoning about human-centric, nonrigid agents |
| [DRS-VPT: Directly Relocalizing in a Scan with Vision Point Transformers](https://arxiv.org/abs/2609.12557)<br><sub>Lanke Frank Tarimo Fu, Maurice Fallon</sub> | ECCV 2026<br>2026-09 | [⭐ 25](https://github.com/ori-drs/drs-vpt) | We present DRS-VPT, a feed-forward transformer architecture for foundational image-to-scan registration |
| [Horizon3D: Sparse Radar-Camera Fusion for Long-Range 3D Perception in Autonomous Driving](https://arxiv.org/abs/2606.31096)<br><sub>Geonho Bang, Geunju Baek, Dongyoung Lee et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 26](https://github.com/geonhobang/Horizon3D) | Long-range 3D object detection is critical for safe autonomous driving at highway speeds, yet existing radar-camera fusion methods remain limited at extended ranges |
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
| [Lipschitz Optimization for Formal Verification of Homographies](https://arxiv.org/abs/2605.23203)<br><sub>Jean-Guillaume Durand, Panagiotis Kouvaros, Maxime Gariel et al.</sub> | CVPR 2026<br>2026-05 | [⭐ 3](https://github.com/jeangud/homography-verification) | The adoption of vision neural networks in regulated industries requires formal robustness guarantees, especially in safety-critical domains such as healthcare, autonomous vehicles, and aerospace |
| [CADET: A Modular Platform for Evaluating Distributed Cooperative Autonomy in Connected Autonomous Vehicles](https://arxiv.org/abs/2606.04072)<br><sub>Pragya Sharma, Brian Wang, Mani Srivastava</sub> | ICRA 2026<br>2026-06<br>📑 1 | [⭐ 0](https://github.com/nesl/cadet) | Deep learning models are increasingly central to autonomous vehicle (AV) pipelines, yet their integration has traditionally followed a monolithic design where perception, planning, and control execute on a single onboard… |

## 🏢 Industry Tracker

Latest 14 days of news, official blog posts and new open-source repos from tracked companies. Full daily feed in [`daily/`](daily/).

<details><summary><b>Waymo</b> (222)</summary>

- 📰 2026-11-20 [What next for self-driving cars after California Waymo ban?](https://news.google.com/rss/articles/CBMitwFBVV95cUxPdFlwLW5kNnJELWZscFV0WUZ2c3FQTWN1X2FrOWluVnlLUDJpUkJtYUR5NzNsU1BPTUdVR0RwUHYwVGhVVzhlSHR6TjVBX2liZWhJaUVhTnFkTV92b1lTMzFWdE5ic3JQRWptemM4ZzA5NHVnaTNyeXI5Z2k2RDlIaDhSbW5OYUcxTnZsZEw5cFlCNGN1MHp2NnNVVVBEUHdvVnFrRGc1VmQzb0NZMkVzNjNaSzJvMlU?oc=5) <sub>AP News</sub>
- 📰 2026-11-20 [DMV bans Waymos from California highways. What lessons can be learned from their operations?](https://news.google.com/rss/articles/CBMi0gFBVV95cUxObk5Ca0w2RVZncGU5VmRYS3c3cC1EWTVJcmR2THc1OTM0UFJlWW4yQ1pGSzhWdHJJcWJ6Z0JXc2FwTTNpQzlhQkZfTDBKb1p2VXdHWmRxTTYzTWhvNnI3WF9tZjFUVk9TbmFkV055b0lJMVFrT0FNTHItSTQ3ZUF1bGM5cEIzWFZ3cXNsSDhfejBFOUlveTEwaUpndnNxaDJTcGJjeXFudUx5OG9BTHp0WWRFUFNqUFBicUE5bVFRbTVRbDhjSWIzVkRqLTRnMVMySGc?oc=5) <sub>capradio.org</sub>
- 📰 2026-11-20 [Waymo resumes service in Bay Area following storm disruptions](https://news.google.com/rss/articles/CBMie0FVX3lxTE5qTUFZa25WOXEtNllVVzB4dHY0a0VvbTBrdWRWX05Pbk1hVGpUX3lwZjlneEpDSnNISktYMWFMODdEbVZ0M3U2VXVQX1FEWE95NDd6RVhlWTRYc3h2N3EtZ0hST3p2SzdGUWNuXzRsQ1ozQXpudVdCNVlMMA?oc=5) <sub>Local News Matters</sub>
- 📰 2026-11-20 [California freeway restrictions create new challenges for Waymo following widely shared I-280 incident](https://news.google.com/rss/articles/CBMipgFBVV95cUxOdW4yNUFJZ1IzNkE0M2xfX0p2QnFIVWVIcUEtaENoTUNtU0sxampodGMzRVhEN2tpTjlSbDBadzFCQ3p6REFRTU5zMEJDVFZCazh2a3NHVDhVaVJxREZMejZDVEJlMjRiYnVHVVhNZWFSNDlUdnVWNzdYdlRUTFVSQUtrelg2cW5hcXVONVZKbzhoSWh4Z0pRNEo0a3o2S04xNjlJUjNB?oc=5) <sub>Yahoo</sub>
- 📰 2026-11-19 [Waymo pauses driverless taxis on U.S. freeways after California traffic incidents](https://news.google.com/rss/articles/CBMiywFBVV95cUxPbldKa1dEUWkwU2k5X254WGpCS1RDbFlWcmZ4UktIdHY3OWhNNExnNXlTbDI5TVlVQXZ3b0pLcU1iRTJSZ2FMd3ZBWTFhd3JRVll4Z0MzcHY0TFRvb0E0NDVnTkw1OXI3SnJhdEt4S3ltNjZCaGNaYTdnN3ZfNTFZRjN4by1yS1ozZ3M3R3VsTXl6YS1IeWJNRnVZSl81QmhsY3FLSXNNSzdGSjJnYy03Z05jVnBYbmN6cE5hTl9ZdkF5ZlUyS3NsQWpnWQ?oc=5) <sub>The Washington Post</sub>

</details>

<details><summary><b>Tesla</b> (311)</summary>

- 📰 2026-11-20 [Two California Tesla Crashes Allegedly On Auto Pilot](https://news.google.com/rss/articles/CBMihwFBVV95cUxNUDROX1U4Z1VybHBxUmtNeXl1UGlBUTJtOWdUQ1dJLTI1WE5tOFdVUGg2WV9XQlNRbl9iaTc5ck1CNEMyeFdxNVViUWJoRDdaX0lCX3p0Rm5kUTRoZ0hEemQ2bkdhb2xnSXFmNjVuVERMVnYyM08zandCQUo5SEQzMGdUY01MX1HSAZcBQVVfeXFMTjdCVmtqcVNQa0xDQllGVmw5bXY0V1J2MkM5UjgzcWR2b1UtQzN0eEtBV2cyUzczRXZuX2hXZ29RREJrZUkzbi13bjM5Q1c0MDNpSFc3WEJCQUFidDRINER1NjhqZWVaaXpvTE4zbGRMNU9JSHlHUGZtWnhMejU3MUJ6MlBkZU9wSnllSExPd1RhR2hXdW92NA?oc=5) <sub>CarProUSA.com.</sub>
- 📰 2026-11-20 [Elon Musk Is Planning A Tesla Model Y With No Steering Wheel Or Pedals](https://news.google.com/rss/articles/CBMidkFVX3lxTE1aVmJOVE1qcVFrNHQwY2lpSGRBTl96NTY1RFduR2tsN1BsQmdDQl9wTk9RWjZBQTBzd2tOc01sUk9XQlFjR1dGem5NSlI4UEluQS1nSHFfQXJmYVViU2FBUU9GSUNlN1lmbUwwTUpCaXJnLS1nMGc?oc=5) <sub>Motor1.com</sub>
- 📰 2026-11-20 [Pony AI Hits 2,768 Robotaxis, Outpacing Tesla](https://news.google.com/rss/articles/CBMihgFBVV95cUxQcFdhb2g4WTREUmVwUHNkOGdpS3pEOWxMdlozU1hHdnZGcTN4QmI3M0RMdHdOQWlTT1MwXzhYLUxMSUhNMVBITWlHeHM3Nkl4c1kzVWc5bmtIbzFZbFBldDdQdWh6NnFGcHBNZnU5TVhYdDg1SlpTWG56ZGZKcENQV3dTQXBfQQ?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-20 [South Korea's First Review Hurdle Stalls Tesla's FSD Exemption Bid Over Two-Page Technical Brief](https://news.google.com/rss/articles/CBMidkFVX3lxTE9SSGNRYlFySHF6ejdndVBfdmZPTmVydWZ3bS0wYkxFYnVpTVNvWTVaV0JkeHF1SzE3QkQ0ajdVd0lLRkxiT0hqSzRmbmlwd3VWMzJ5M0l4SUZ1dEM4d05rdnVpdG9ueGFhT1FDMjdDRHFzTW8wLWc?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-11-20 [Korean authority rejects request for full self-driving for China-made Teslas](https://news.google.com/rss/articles/CBMizgFBVV95cUxPMEx0WVRzNDdZX2YyY1VOY0RwbFZGeTBjeUlWZjBYMXF6SVg2MkxMQ0E1bjdOWVU4YXY4OFpGeHdLQVU4ellDQUd4MVpZY1Z0QUZCdnF2X2RCOWRhWS14R3ZTN0k3TERxT01RbHY2Z25XZFFiZkFrWTMzeUktU2I1dVptbVplSXBYalhoTEZIVldibzZpN0p1RG50cHRLdWR1MFdMTTlIYnJxZ3ZMeU9sd2lNLVVvVnFacUZVTkh6eU52YXBHVmVRYlktU0cwQdIB0wFBVV95cUxNVVplSHk4ODZLY3NQTHpOSFE3NWpnR0V2ZXlJUVNMWnFiZG1uYXFXN3pEUWJabnJqTWloS29PSlpPUi0wbHVTaVhPRmxvWVlwSDE4S2VObDZNNWtMbjFYdlpKaW9tT2xjbUNtVkVjVGdwOUNrRlhCZndDbU9HaFhrZWhkTFRPNTc1T0pUTTVDY0RtSWFnRzNwejNjY19tQkZkc0EyTEF5bkNKMWU4WTlYLWtnYURQTmRBSzJoT0ZaU3VKeVQ1R3dhU2dwb3docUtqQlpJ?oc=5) <sub>The Korea Times</sub>

</details>

<details><summary><b>NVIDIA</b> (197)</summary>

- 💻 2026-11-19 [NVIDIA/nvidia-linux-utils](https://github.com/NVIDIA/nvidia-linux-utils) <sub>GitHub</sub>
- 💻 2026-11-16 [NVIDIA/scadactl](https://github.com/NVIDIA/scadactl) <sub>GitHub</sub>
- 📰 2026-11-20 [California attorney general subpoenas Nvidia over chips, former CEO's affair](https://news.google.com/rss/articles/CBMiuAFBVV95cUxOQmZITEdpR3o0QTFWdDNqTFB1bWRnbjR6aUJJRjdzN3dqaU5fZDBReWdHdDJiUVFIeGZnMUZFWG51YVdzZ0tVb2NBZXVvMGR5UUxVVnJZOUdrdkxMQXdQU0N6OHdVMUp4WW5UWFk4ek9yY3FPVjJsV09lbE9RdC16LUtNWUVkMVpheUM0SFZ5UVI5MlptbXZ4U0kyVXZiZlU0REtodlVmRjVsb2RoVUVOREhpb1JsUTJK?oc=5) <sub>Audacy</sub>
- 📰 2026-11-19 [Nvidia Shorts Drive $2.65 Million in Gains for Five Trading Accounts](https://news.google.com/rss/articles/CBMiWkFVX3lxTE51SHowRFhWY2g5aFY2WDVDdzBRajZ4b2lvNTUzRWx5aVQzTi1vWFZLem93M1dSNHF5MDJWLWRGZXVMN1VVMTc0VXN3NmMtTmd0UzgxWFVLcHUxZw?oc=5) <sub>www.tokenpost.com</sub>
- 📰 2026-11-19 [Hyundai Motor Group, 42dot Recruit 3 Self-Driving Executives from Apple, Nvidia to Expand Silicon Valley Organization](https://news.google.com/rss/articles/CBMidkFVX3lxTE1tZ3lLUVJoakljZTZXOVQ4VjRBQ2tWbEtHdjE3M3hKZ2tvTHVzTVpjbFVDOFVEeXRwRVZSMEdjR2hxUndFZHFNTHBRV3ZIb3ctWnR6ZUZvVElIRGdMTEtXamVaY0NGZ3hrZ2RkZ1cwaGhIcE1kWXc?oc=5) <sub>BigGo Finance</sub>

</details>

<details><summary><b>Wayve</b> (46)</summary>

- 📰 2026-11-19 [Wayve and Stellantis partner to advance autonomous driving in France](https://news.google.com/rss/articles/CBMiwwFBVV95cUxQREhYNVdPX2d4S19MaVFhNWxmWHh0Z2Y3dnVmeWw3aElKcndIekVGYm5CRTlydldmdDA4ZUhCQVlYeGxqeDM4MURQT1BZME5QY0VBTzBhTXVJNEc5bUlpaFZ5OFdqeFZtQUc0YUxNN3BWNWZSMEVzNV9XdkloOU1pdHJZYzM2OGFJY0pvc0cwRXdnblk2T3lVTDlEUEJURFcwY083VnlfU1d6Q2s3VlZ5allzLUFacGtfTC1kMUpacmo4QXM?oc=5) <sub>Robotics & Automation News</sub>
- 📰 2026-11-19 [Qualcomm takes on Wayve, Chinese rivals with new AI driving platform](https://news.google.com/rss/articles/CBMihwFBVV95cUxPSmpFQkxRLWs0ZU16X1hveXRWQlJDbnpiZDZoa2FnVDRVYloySE5qSHpGQUNJb2ZEZjFLcGxrRTViWmhYS3pybUp1SHFuZWU4eWNSX0o0REtSa0NVVDJCaTMxRzlKbGhpN0RNRzVUVFhsMmx1RUk4V1dFYzJoSFhvLUZXMWZFM1k?oc=5) <sub>Automotive News</sub>
- 📰 2026-11-19 [Bolt and Stellantis plan autonomous vehicle trials in Greater Paris from 2028](https://news.google.com/rss/articles/CBMizwFBVV95cUxNVmF4U3dEUHlQTHB6NTdHSVhBT2dwblNQSXhLbnlMQUVCQnFTSVJ0TW9KcTdlTmhLZkdsRDg2TGxBMGVvdkNSamNaV3lmaXdkSXI4UVlyZFd1Z2hYT3gtU3NGVmVXY3N4WHZQMjRxSEM0OENfVndrT1E0Q2pOQ0pfUExTYXdadzlUNFhxaF8tTWdwVmszVm9NM0JlaktadFJPaWZ1eFkzMUVSdXVOSlpPZVhLNG40THc1aTdaaGJ1c0F2R0tnMjBkY25FakJfRzA?oc=5) <sub>Robotics & Automation News</sub>
- 📰 2026-11-18 [Waymo Pauses Freeway Rides Nationwide After California DMV Order](https://news.google.com/rss/articles/CBMiiwFBVV95cUxNZ1NETWFWSzlHNE1XbjlsVHlPNmw2WVF5WTBUSEpIdFUtMzVFY0dQaG9VNFlmeTd5Y3hYc05kX3h6LUVPdGlfQS1vSVJ0V2NVWHpTaHVVSmtyS2ZNSUpIdDhCWHhsT3VVTlcxWC0wUGdQUERwTGxKamgwcTJISzhUYkdITC1DVkNwWDZn?oc=5) <sub>TechRepublic</sub>
- 📰 2026-11-18 [Mercedes-Benz unveils hands-free driving](https://news.google.com/rss/articles/CBMioAFBVV95cUxQME53Zlk0TWhPUUM3clBMMG9URTNSdnFtb0dSOVZ3ZTFPYmFDaHJiRFQ3Y3pDTHkxeHExLU9PVWZSZFJyTFE3UVY3M2NFVk1LcmxmOTA1a0xaTTZMblVfeWdYaU4yOUlFZnFRcGxyc1ZQV1JUdGZfZUlqbGltb0lPMTNMNzc1NkdMQ3R6YmpTcE9lQ1l4Vkp2U0hKVlZxbmZw?oc=5) <sub>FleetPoint</sub>

</details>

<details><summary><b>Momenta</b> (102)</summary>

- 📰 2026-11-20 [Momenta and Uber Launch Robotaxi Pilot in Germany, Offering Free Rides to Passengers](https://news.google.com/rss/articles/CBMi3gFBVV95cUxQaDU4R0NuMWEydGl0djRJaTluMEJiUlRqTHdCV29YUHhpT1ppTnNoak4yMmpEY2dwblBmaFR1dlVLVHQyZkZrZmlYQXVPWjlDcTB2QWR2VndfRFVtTkZlTmZ6VGdBaDhWakZMOVhKdzBqSXBCYTFxY1VESnNWbTlaT0Z6X0VWQVRSU1Jxc3NWeFRiVDNPYzY1MjgwWDJnVWt6eXdnTnl5SzFrUEZNX21RTlFMNVBJR1lfWHdCTXZ5U19uWWtITVJLVmNfMC02V3VJYXpaV0cxMUhfRHlTZ3c?oc=5) <sub>Gasgoo</sub>
- 📰 2026-11-20 [从一趟Robotaxi看中国智驾出海，Momenta加快欧洲落地](https://news.google.com/rss/articles/CBMiZkFVX3lxTFBvYnBMd2Uxd1dzLUw1cnFSTzgyMDEwSDRBZnBkMDc2Q3ZYZmQ1Vk43STg0NEM0SGV2d01YV05IU3V0UXN5c1Ryb0ZYazIxeWRLZkthQnkwZ0dIa1VYUjgyYlJYQUhMUQ?oc=5) <sub>每日经济新闻</sub>
- 📰 2026-11-20 [中国智驾出海Momenta在德国先行一步，RoboTaxi试运营在德国开启](https://news.google.com/rss/articles/CBMiiAFBVV95cUxOb3BrWWZraS10allKZXdDXzRhYV9BVUFvUmkwdS1pcEJIOWRudjlJYkUtRFZ4NDVLd0VPbjZsXzUyZl9rSHJtb3Z2MTBxUGlOR19DRHhCTUM0V2hvRkJQT3NZYWJnLTc5T3ptZXdxSlplLWJFSmZ3c0tTOTR5dnNNRkZJaktqaWp5?oc=5) <sub>Sohu</sub>
- 📰 2026-11-19 [Momenta and Uber launch supervised robotaxi trial in Munich](https://news.google.com/rss/articles/CBMingFBVV95cUxQbk9iZ3BwalBoNGFTX2k5SmFRWldDVXY3SmxsUnZJbVlzVlc4UUpBNk9wUUJCREl3M2NmbXFMUlF1THg3MkVGU3g4d1hNMFRKN2E5MGN1M2VnZXl3MENmMDVpN3h6Mno1dzdfaUNOTVIxN3FteWpHc3RWUGJjOVBQWVZQRkZCdnoxM2gtSlFaVDhfaHF0Qm5tZWhBMnpSUQ?oc=5) <sub>Automotive World</sub>
- 📰 2026-11-19 [Momenta与Uber慕尼黑试运营Robotaxi](https://news.google.com/rss/articles/CBMiW0FVX3lxTE0yRTV4cDJiMFBMYXlKRzNrMjFuM3RwclhlQXBrQXdMbG5LeC1tSl91OXBkNmhMbEg3RUM4RGQ0RDVVcC0xUWYxUzFKV1R4c2IwTnJUQjdFWUx0SUU?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>XPeng</b> (204)</summary>

- 📰 2026-11-20 [智驾硬件买了却爱自己开？这套VLA 让能耗提升12.4%\|小鹏\|VLA\|图灵AI 共驾\|P7_新浪新闻](https://news.google.com/rss/articles/CBMiY0FVX3lxTFBxWTg3QnFROXVPWGxSbjlpeHpsOXY4aXZXaDJVay1yUDBmMjNra3NFVGV6cWNCYTd6aGU2ZFJLV0xwcGtOZGlsVkZncXVXN0dUT0drOWFjX0dqUk9QcldLTFNCWQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-20 [17万选纯电SUV，702L大后备厢 vs 510L够用吗？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE13c3dHZ1p6bEtHQ1FJcVEwOGxKS051LUtiSW1SaXdZbTdiNkJxZGxablRjSDBVQThPdXloSE0zMl96UkcwQVVYakFhblN4SzJvQWJwMGcyd0N5UlE?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-19 [Xpeng to hold 2026 AI Day on November 25 with focus on physical AI and robotics](https://news.google.com/rss/articles/CBMic0FVX3lxTFA5MjZqRzVpNDlHTnB3X2U4eDRfZFNOcW85YTVCSEVtODl6VFMyeWR4emNvMHNxYWpOd3ZRNEFOVkxySWZYaXVUX1ZUM1MzVVB3Wmlacy12UG1wdjNUYnUwTnYtbk16NzR0MGNELW15em1iNG8?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-19 [小鹏科技日定档11月25日，物理AI有看点](https://news.google.com/rss/articles/CBMia0FVX3lxTE1sQWMtWlQ1QkswcFBJMVEzbVBWM2hWZF9Vanp0VnpWMllkbWxfUWNmUV9hc011Y3hvUkVvdm51ZlN0RUZOclhENVBRN1A4dkNUUWFDR2g5YXd5ZzRBem9kSTM0WW5hYWRvTkdn?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-19 [Toyota bZ4X Robotaxi Runs 24 Hours a Day in Guangzhou](https://news.google.com/rss/articles/CBMilwFBVV95cUxQUTRGaTVNRE1RZzltamFfTmxFUGJKVlA0Yk9tYk5EbG9sU1lVVldyQ3dfd3F1eE9YRWlmcWVJek1KYVo0UlBYTFpBSzZmNEd3RUt1OXR2NmVRZ25YREROZnVoYW9HRVhwREJLbW5aU19Rb3RNZTNxSEZ6MXg1QmlReExyUDlBRlQ5emg0dUR3dHBaRXZEYTJR?oc=5) <sub>shattered.io</sub>

</details>

<details><summary><b>Li Auto</b> (176)</summary>

- 📰 2026-11-19 [Another Chinese EV brand eyes Australia: Li Auto recruits for a potential 2027 local launch](https://news.google.com/rss/articles/CBMitwFBVV95cUxPUy1SRWJxdEc4RVRnNVVhWHBzUmM3VnlUblZ2bW93LTA3NFlhYS0xRmxFS3U1QTBNeEx2Q2Q1YVJ6cDczRk5WbEtXSVZoTHVNdHBmcGRhSkZqQUY2RjZITXpoaEo1dmFLempYb2pwSXRDUDMtZFJzSk5HeDhpNzFjTU9SaVloX24zV2h2UGtNSGRfclFCeDdsbEpMSHo5UzU4bFo0Y1lLckVpR2dWalBTa2ZQMW9PVXM?oc=5) <sub>EV Central</sub>
- 📰 2026-11-19 [3款30万级家用新能源SUV如何选？奕境X9、小鹏GX、理想L9围绕空间安全续航的实车对谈+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5wRm5oWW45SlhZRm93WUNxa3d4TjFMY1lYbTYyQ1pra29VVzBCbFNISEZMLW00QS15MzItYzhMTVQ1VnhZWDBVODdNUlZHdFFhTzJNalRCMmo0a1hjcjEw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-19 [2026六座SUV四车横评：领克900、理想L9、东风奕派M8与奕境X9，三排空间与智驾该怎么权衡](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9sMENBYnc1OFNtZ21TOVhKQXFySzBPZVd1X0JpVFZkWEJCdU1GNUVFZU5mZjV4bGFQNHpQR1Bmbm5zYWt1UjNMREFDMHBTNHRaRGxHZThxZVZMRmx4TVg0?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-19 [Xpeng to hold 2026 AI Day on November 25 with focus on physical AI and robotics](https://news.google.com/rss/articles/CBMic0FVX3lxTFA5MjZqRzVpNDlHTnB3X2U4eDRfZFNOcW85YTVCSEVtODl6VFMyeWR4emNvMHNxYWpOd3ZRNEFOVkxySWZYaXVUX1ZUM1MzVVB3Wmlacy12UG1wdjNUYnUwTnYtbk16NzR0MGNELW15em1iNG8?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-19 [The Volkswagen ID. Era 9X EREV model was unexpectedly displayed in Vietnam.](https://news.google.com/rss/articles/CBMimgFBVV95cUxOUlA0SVRLd0xYSTVfc2YwQ1N0c2NDUHpjMmlNSVhGaXZLZ0ZnWTl3UXFMdUYzVEoxQVUzVkRTVnB1UThjR3F4cGhpb1dGcnpCV2dWQW93aS14OUdNOFp6V2hlR1ZHOFRHNWU3b2F1WnRreTF3UnN6X180Wk5UcmJMRXphdjNjY1RIUlJNM3prV3FaelBFcjQ1YVNn?oc=5) <sub>Vietnam.vn</sub>

</details>

<details><summary><b>NIO</b> (168)</summary>

- 📰 2026-11-20 [Nio Firefly launches new 333-unit special edition to sustain record delivery momentum](https://news.google.com/rss/articles/CBMifkFVX3lxTE5MUlpxZGVkYWVtVXVJeVZJSk9SVms3VWZjcll3MmFud0JrdVBFR3RfcTFOMHlTY3lQckNUYi1lX0Rwd1pKX2gzakdsZGozRkhHY2pXQjZsVzBqdVdnM1hwYTZIbUFsYVpmNUItcXoxWHNMNDM0RngwaUFOU0w3Zw?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-20 [Spy photos show camouflaged prototype of suspected Onvo L70 set to expand SUV lineup](https://news.google.com/rss/articles/CBMiYkFVX3lxTE1IckxVS2FsU0g2enFaSUFRbk9icXFjc2JYNFpQcmZYYVNsdHNlcjRBOTBWMURoWkMyLXp3cFRnemQ4UFVwQWx6UFc3X3VhZzlrR01pcjhIMm5KS0hLYjh4T1Bn?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-20 [US lawmakers near deal to ban Chinese cars with carve-out for Mercedes, report says](https://news.google.com/rss/articles/CBMifEFVX3lxTFB5Ull0RHk4MURKVlZFR0VzaFJ5WnNUMXdlNlJjMUNSX3FjNFFTT1ZoSm4ta3JLZHBIZERULVdEU0VoNGxSVDBGLVA2a3U1YWg0WXhWcjE2QmpQbHRrRnlxSGdLcWVNVDRoRW4zejlXUERJS2ota3VkUWhRTDY?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-20 [BYD teases first flagship MPV for Ocean lineup to expand minivan offerings](https://news.google.com/rss/articles/CBMigAFBVV95cUxPZGtwZXhFM3E1NEwxcXNpRVdXN245UXVIMGRUbjhRVFN4TFVZYWNkQnNGb2QxUDBfaXdGMGpjT0J6SndqNG1SeWZDUDdyZG1mcWpXU0h0aXpBME9GcF8wVFNjU0VVQ3BZTDRkNUdjeno0cVhNbWotWlZiVE1EMk02OQ?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-20 [【视频】蔚来ES8动态体验：零下4℃三分钟换电！能缓解纯电车的续航焦虑吗](https://news.google.com/rss/articles/CBMia0FVX3lxTFBNRjZtQlVUT0tpbzdYcDNOaXF6Y1lFcHMxakFEdnlCV3BZSGJlRUJhdXJCcWtqcTVQNEkwYTJ1MXkyN3VvSV9BT0N4bHBUZTdOUHNFSlJJNTNVX2E2WXZoQ3lWUlhxaUZvd2Nj?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Huawei</b> (325)</summary>

- 📰 2026-11-20 [MIIT's 412th Catalog Confirms Anhui LUXEED's Vehicle Production Qualification](https://news.google.com/rss/articles/CBMi0wFBVV95cUxQZWwwWGpIeVRHMlg1TzNrZTJpSjZoMGFobnV0UUFoSXJWaU41Umw4MmVCWXF3dkQzSWlvT1VkY3lKcU90MFRtNUVSd193R2tuMWZiMTJybG1iU3pfQmMxS3pqS0pITlJWclJsX29FcDRockxqemtPV3NNQ0RuQzdKYkxjRWNtLTJCS2xZdWpyMGdKQXFOamRxZUZWYjhHUDZTbVloWndHNndralgyVTl0aHVta3JqYi1oTWNhMVlORzR0c1d0b1lRbmcyVmhqLTZLeE8w?oc=5) <sub>Gasgoo</sub>
- 📰 2026-11-20 [HuaJing Auto Officially Announces Five-Seat Version of HuaJing S-Internet Info Agency](https://news.google.com/rss/articles/CBMiYkFVX3lxTE1kLXhqT05SeHNDd0g1dlFWTmg0SVdCV1RkTk5Pa1dVendMdXFMT3U4YnE5djd0TVkwNUdYSUNHSzhxTlZUNjBhWEozYW1QNFRSd0tTTXBXMzBuSDROTW9tRE1n?oc=5) <sub>网通社</sub>
- 📰 2026-11-20 [Kenya flags off 8 students for Huawei’s Global ICT Programme](https://news.google.com/rss/articles/CBMiigFBVV95cUxQQ1VuOWV0ZnZhRURORzlTNVFBVWZmTHdsZl9CQXg2U0RXRk9xRndOSzhnUTIycGgyQm9teFZVU2xRTk1LMnZpeDBzQ1hYZEJLOEpydkV0ZVM2bUcwOUhtdTcyZkJDZEJsUElUWDNHcHZEV0pjZ2Fpc0p6MXZjMzZqbmhQQzdHVlVua2c?oc=5) <sub>KBC Digital</sub>
- 📰 2026-11-20 [US lawmakers near deal to ban Chinese cars with carve-out for Mercedes, report says](https://news.google.com/rss/articles/CBMifEFVX3lxTFB5Ull0RHk4MURKVlZFR0VzaFJ5WnNUMXdlNlJjMUNSX3FjNFFTT1ZoSm4ta3JLZHBIZERULVdEU0VoNGxSVDBGLVA2a3U1YWg0WXhWcjE2QmpQbHRrRnlxSGdLcWVNVDRoRW4zejlXUERJS2ota3VkUWhRTDY?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-20 [BYD teases first flagship MPV for Ocean lineup to expand minivan offerings](https://news.google.com/rss/articles/CBMigAFBVV95cUxPZGtwZXhFM3E1NEwxcXNpRVdXN245UXVIMGRUbjhRVFN4TFVZYWNkQnNGb2QxUDBfaXdGMGpjT0J6SndqNG1SeWZDUDdyZG1mcWpXU0h0aXpBME9GcF8wVFNjU0VVQ3BZTDRkNUdjeno0cVhNbWotWlZiVE1EMk02OQ?oc=5) <sub>CnEVPost</sub>

</details>

<details><summary><b>Baidu Apollo</b> (56)</summary>

- 📰 2026-11-20 [Google 开放 Genie4世界模型 API，支持实时交互与原生音频生成](https://news.google.com/rss/articles/CBMiTkFVX3lxTE9sLURMU3dDZHJRN0N0U25LV19oWlBvTThkQVI5TzNCVnBHYlFkNUREbzJxYXBnWVV0SHQ2WGRpQUViM0ZKbXpIdUw0Y0dZQQ?oc=5) <sub>AIBase</sub>
- 📰 2026-11-19 [萝卜快跑落地28城，江铃新能源无人车驶向30国](https://news.google.com/rss/articles/CBMif0FVX3lxTE4zVlo4bjVEYzlyQUt2N1lTNDhDYUphcUJzS1FJcEVhdEJFVEctcmhZNHNJSTJxM3gwQ1k0eFFkWUttRzF2ZWY3WU1CMGJRMDJtNWVXdHRVd3llZ0F1cjdxMHhzUW83SHoxX29uMHlZOUJfTEI4ZHJBN3hTcTZDQlE?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-19 [Toyota bZ4X Robotaxi Runs 24 Hours a Day in Guangzhou](https://news.google.com/rss/articles/CBMilwFBVV95cUxQUTRGaTVNRE1RZzltamFfTmxFUGJKVlA0Yk9tYk5EbG9sU1lVVldyQ3dfd3F1eE9YRWlmcWVJek1KYVo0UlBYTFpBSzZmNEd3RUt1OXR2NmVRZ25YREROZnVoYW9HRVhwREJLbW5aU19Rb3RNZTNxSEZ6MXg1QmlReExyUDlBRlQ5emg0dUR3dHBaRXZEYTJR?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-19 [从南昌出发驶向全球，4000 台无人车背后的硬核工厂\|江铃集团新能源汽车公司\|江铃新能源\|萝卜快跑\|无人驾驶_新浪新闻](https://news.google.com/rss/articles/CBMiY0FVX3lxTE9qekRyNEk2TmhVSi0yMXZwX1JWTmlETUdvUm93MThCa1FSTTZ4dG93aUpsUjZSWTlzczI2emFoLTdRYVpkMFpON0pweG01a0hDelpLR1VDTXB1X3pUZTJ2V0I3NA?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-19 [APEC Summit Automotive Industry Keywords: Globalization Trends & AI Implementation in Auto Sector](https://news.google.com/rss/articles/CBMiU0FVX3lxTFBMOGlzWjBweExwNy1KNEZQZVJlOTFQRDZHd2RRYUdSZWJqeXl5YzNhdDY2eDlCU1ZhWUhpbDN3REJwSjdRdlJKTEt1Q1ZyYUZaSUVv?oc=5) <sub>36Kr</sub>

</details>

<details><summary><b>Pony.ai</b> (141)</summary>

- 📰 2026-11-20 [Pony AI Hits 2,768 Robotaxis, Outpacing Tesla](https://news.google.com/rss/articles/CBMihgFBVV95cUxQcFdhb2g4WTREUmVwUHNkOGdpS3pEOWxMdlozU1hHdnZGcTN4QmI3M0RMdHdOQWlTT1MwXzhYLUxMSUhNMVBITWlHeHM3Nkl4c1kzVWc5bmtIbzFZbFBldDdQdWh6NnFGcHBNZnU5TVhYdDg1SlpTWG56ZGZKcENQV3dTQXBfQQ?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-20 [Pony AI’s robotaxi fares surge nearly 400% but its operating losses barely budge](https://news.google.com/rss/articles/CBMipgFBVV95cUxQejkzT3hlZnI4SG9LdWVCc0FKMF91cW1TWVBTNlJ5enRQOUxMOEFzTUg1STVDRHpOVTBpanlFNHgzd3RzN3ZDLTRaNV83azIxVEZTR09FWGx0OF9rWVR1bFlod050WlRzWTY2TVd4cHRQeGNrVklWcWNtUlV3QlZyYzB4WEZSZGtRd0pvWDlDU2kxTVB4Q3FYN1ZpeXlmeXVWZmRpOUFn?oc=5) <sub>CryptoSlate</sub>
- 📰 2026-11-20 [Pony.ai's Q3 Report: Revenue Surges, Losses Narrow — What Are the Key Takeaways?](https://news.google.com/rss/articles/CBMi0AFBVV95cUxNQlhkdThZM1dJYmkwWGdBYXMxYjNsMUp2ak1xUzZWbkdkaGluR2QzNkFXLVVGTk95NnhMcDlvUmg1RG1xWFg5X2dNbGpKN0dJajdwb0cxZEhydjhDUEFUZEN2c0k2T0VyQnoxc25ONkkwVUdBMk5OeWdvR2dFMWtHNkx2emh5T1JqSF9NQTE1TUczb3EyWG42TGhxYURQX0lnMlZ2ZnE2TEtkeUpTS0tiTTcyaE85alNoTm8xNmNiLXdOaF9WSUE1VFhvTnBVV2l2?oc=5) <sub>Gasgoo</sub>
- 📰 2026-11-19 [小马智行彭军：L3不存在，坚持L4路线因其长期价值最大](https://news.google.com/rss/articles/CBMiUkFVX3lxTE1weHo1bFBIOHRSNWZqQXBwdDZQTllnVUVocnFmdy1Bam5kRmFWQU9ONGZMVDJLaTBMNl9ITXBicnFleVFyTFVQNzZVbUd5YzFnMnc?oc=5) <sub>凤凰网</sub>
- 📰 2026-11-19 [【百强透视】收入大增股价却创新低！小马智行（02026.HK）仍面临多重考验？](https://news.google.com/rss/articles/CBMia0FVX3lxTE51aGMydEZrTktKTjZCSTZNSDBtV2Yxc1JXY3FBUzBIZzZXY3p2N0NlSXhLcXo4T18xN2dTX1pUQThFYXUtQUQ1enpXUGVBTmtSRENNdE9WXzV5cWczbVJ4ZjNKZHZVaFNXVnJR?oc=5) <sub>财华智库网</sub>

</details>

<details><summary><b>WeRide</b> (112)</summary>

- 📰 2026-11-20 [LensTalk \| Embodied AI takes on daily tasks in Singapore](https://news.google.com/rss/articles/CBMifEFVX3lxTFBHbzBhNHZCNk9LaGs0cmM1cHhPdWliT0NTTDJuSGhMZGN3QjJjdTk3dzFQWjVKX01QMm5BRkZBNU1KVldyMnNlaUV6TmhCQS1ILVdJZnJSSjhkNlRCYy1zQWR6dFJiaHVxbGJ2Y3hzX1R5NnFrTDF0NUllcFo?oc=5) <sub>Xinhua</sub>
- 📰 2026-11-19 [汽车行业的终极之车：造Robotaxi，6大厂商的不同思路](https://news.google.com/rss/articles/CBMiW0FVX3lxTE53eVpvOURsQUxZREoxUVZKSkllM1ZCc2NsNTZRSFlTRHlqUDZBTDRhcDB4TmtNSmNLLWhXTHFoRlFqYVc2MWtDSFNITHdoalROTWdiVk5qZmk4T0U?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-19 [Uber to invest $50 million in autonomous vehicles across Dubai](https://news.google.com/rss/articles/CBMisgFBVV95cUxOLUsxcElOb0tDdUxOaS1nYjR5bTVCM0U2RmlXN2VTUUNOQ0FHcG4yOVpRZm5CTUp5c2xrRDQ2b3h5cngxY1NoZXEzRm12MGNTYWpnRVRZUURoa29BT2pXTGVFdk5ON1dZalNEbWJCVEl2NlNwbkFFNENiT0s4ZDdtMjJoeU5YRlJpLTBaZ2tIRnZKcS1yaGNmX0wzdk5zQWxJWHJPOXg5QnhWazlXV016b1VB?oc=5) <sub>Arabian Business</sub>
- 📰 2026-11-19 [China Solutions, Global Value \| Gasgoo Awards 2026: China's ADAS Algorithms Enter a New Phase of “Production Validation + Global Export”](https://news.google.com/rss/articles/CBMimAJBVV95cUxPa04xRzBfLTM3YTZOQ3ViVXV4VUpKcjk4NHF0TlJTLVdNYjE3LWszb0dCS3V6bndYUGFpYmo1ZVpQcFZjUFM1RlBsTWdsYktWRmxrY0RNR0hxeTNkNjB5WmxfSDNHNFk5Q1o0c1F2SURISnF3cVB0N3hrSkNzbHBJRUloMGFXVnB4MGxhT3J0ZWdPd3hzbkV4Ykd3cV9FaWQ0Vlk3eS1vdVVQRzNHS19iV0FnQW5HZHcyd0FLRVFmTVdOdWxSeUVrMDJ2ZGRaT2stS25LZFNMRkRHRExWdjdXSXZTMG1GX0NKSGVXZDFITUdyODBXYW9CYjJkVHktWXYwRVdpSFBCZnUwbFdDUThWRkR3RzF4dWxr?oc=5) <sub>Gasgoo</sub>
- 📰 2026-11-19 [Uber commits Dh184m to expand driverless rides in Dubai](https://news.google.com/rss/articles/CBMirgFBVV95cUxOWU9aN05uNTlRWE8zci1FWmJRZksyUmZEaUZiSGd3VUtadVMxMWdaNUlLTTNRaXl4bUlMQlRpcGR5Nmh3X3VlemZ1RjFTbzlrd3pkQkdaT1I5QjFNZ3ViT0xqbFNKd3llMDFIOVFnR041R0M4YTNPU0pTMnBGMWNLNWNwdzVLaWd0b2R4OTBVNFdOdmt4bjUwUVhJOVNpT1JKLTNIQ2dBdGh1RU1yN1HSAa4BQVVfeXFMTllPWjdObjU5UVhPM3ItRVpiUWZLMlJmRGlGYkhnd1VLWnVTMTFnWjVJS00zUWl5eG1JTEJUaXBkeTZod191ZXpmdUYxU285a3d6ZEJHWk9SOUIxTWd1Yk9MamxTSnd5ZTAxSDlRZ0dONUdDOGEzT1NKUzJwRjFjSzVjcHc1S2lndG9keDkwVTRXTnZreG41MFFYSTlTaU9SSi0zSENnQXRodUVNcjdR?oc=5) <sub>Gulf News</sub>

</details>

<details><summary><b>Horizon Robotics</b> (120)</summary>

- 💻 2026-11-19 [HorizonRobotics/LoFT](https://github.com/HorizonRobotics/LoFT) <sub>GitHub</sub>
- 📰 2026-11-20 [Chery’s iCar V25 EREV officially launched in China, starting at 17,900 USD](https://news.google.com/rss/articles/CBMirAFBVV95cUxQVExXdHhZU0JjdllVc0F4R1U2YlR5N2NXSGVSdFJrejI1T1FtN0x3ZzVPQmFyUWp3ZkRpZHI0cmdiQnIxWlJPUGRMenhsVF9RbS1KNUwyRUVqdTlBblZTcHAxV0VnemJyMkd3NjhzYTNEbTJKNFZaLTlvRWt3ZW9kQ1NZVjdlSDNiNDBqSThQQVM0T1U3WFVJblJEQnAxaTl3ck1NTk9FVUktdDIw?oc=5) <sub>CarNewsChina.com</sub>
- 📰 2026-11-20 [单颗征程6M带动城区NOA下探，地平线进入“谱系化量产”阶段_IPO观察_新股](https://news.google.com/rss/articles/CBMiYkFVX3lxTE9jdDJ4akRaWURBeGJjSHVxLWpqYU9CSmZHYnljVUpfVEwwMzFPMUhUUzByUHFzTHhSUWNxT1NpdzUzN0pVQ1otYnQxZDh0YjVWLURYNklzWXo1c0hMNWxUZlR3?oc=5) <sub>证券之星</sub>
- 📰 2026-11-20 [4款方盒子SUV智驾横评：高速NOA、城区NCA逐一对比，旅行者7的油电同智最省心](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBDRGxwVXgwd0I1V3M0RVhmVjFKY0tMalhybldaUThCZGs4ZjFlNlJXNUhxM2dzdm1Wc3d3V2U5a0pydGRyYkJYcVY2Ny1nUGo0djB4SXJhc0hVbGMzQm1r?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-20 [天风证券调研纪要：地平线11 月下旬起密集发布具身模型，非车领域已有批量订单_IPO观察_新股](https://news.google.com/rss/articles/CBMiYkFVX3lxTE9TQ2lYRmljM2ZrQU1YZ3BaZDUzN2o1djFqYXZtbXpWZEo5TEIzd004bnFKa0pxR2ZwNkN2ZXdRZDhBZGJiVllhTzFSRFgwQnVrTEp6Z3E4emt1cVdzeGJyLTBn?oc=5) <sub>证券之星</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (20)</summary>

- 📰 2026-11-16 [中国智驾出海新突破！元戎启行交付超10万辆](https://news.google.com/rss/articles/CBMiW0FVX3lxTE80eWh5OVZNRlpOY3ZTN1hMeHlsN1NtbldkODZOVTQ5U3hMVXBrOXZ3RnhWUXA5eXdsNTVYbUlDUnNsNEhnX05Jam9VUUhDZkJ5RmtIb3RJX1IxQ0k?oc=5) <sub>车家号</sub>
- 📰 2026-11-16 [又一“国产保时捷”？赛豆ME7实车到店，大过小米YU7配571马力](https://news.google.com/rss/articles/CBMia0FVX3lxTE5fWTNxTkVfa2RHM29CZ3JabmtSbllKTVdGN2x4aVpqS0U0bG81RTFHeDhqNHZhaUg3MGJFVjEzOVU3aDdIMS1zR05mNXZ0blNyZ3cxVWRnVF85bmc3Tl9aenNZSlpDaWRDSV9n?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-16 [AIVA ME7实车到店剑指25万级轿跑SUV市场](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5fM1B6RnpLTlpiVEtIUmJaR0Ffci1BVVpqTzY0ZnBab3JSZ2luNDRWeEhPeHJ6YXlaek9BRDZvdmU0TEw3d2JXTVdMbHgzLXh3TWhLTmpCTDlvdw?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-14 [DeepSeek无人创业](https://news.google.com/rss/articles/CBMiTEFVX3lxTE1QUnM4dm1XbE8tWmIwSE1hN1JMTjZKRklrM3FmbkdNbVd2WllWUWpjQVhYV0xwaHhqUHp4T2ZkMGpHMExqWjFNU1lPYXo?oc=5) <sub>凤凰网科技</sub>
- 📰 2026-11-13 [【视频】小米澎程N90和特斯拉Model Y L怎么选，同价位还有哪些推荐？](https://news.google.com/rss/articles/CBMiW0FVX3lxTFB6dElibXRFYWFsZU9vQnhjX3YwZjF2VVd6QjhLdXJIV3pmRGhzTmpuTFRER2xXV1Zjc2ZqNld2RVY1MkxrTENqczVRc2MwNHl1VFljSkt2TjRxZ0U?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Mobileye</b> (13)</summary>

- 📰 2026-11-19 [Growth in the Adaptive Cruise Control and Blind Spot Detection](https://news.google.com/rss/articles/CBMinwFBVV95cUxPa0x3SFRDX194b3VtTHJnYlJPNEZzRHNpRHd6RS1JOVVkWnBBMnZxQ1AyRjFpUWdVSDBuZHdVdUdFczFGbUVMSFlhdU41UmYwbmhzdFlDaGhvSmptUzNSYzktbGJpRG96ZmZvQ2ZHY3Z3aUt6aWV4WFJzLXctV2k5dFoxVTlta3YzSmNkZGxBRmxYdnlLQ1JKV0RFOWxVcjQ?oc=5) <sub>openPR.com</sub>
- 📰 2026-11-18 [Intel Cuts IT Jobs as Tan's Cost Drive Extends Into Year-End](https://news.google.com/rss/articles/CBMidkFVX3lxTE9XMEIyWkJScF9ld3AzQXYxN0hhaFJQWnJ3czJVOE9FelQtbG12YUdoWkZmZW55cWdQamJlSnRGQTF4bWVDNi0zRFdfZ0hpVkJFNThWdmYtWDk4WGRBY1F5dWFrRklNQjNLUU1UVUQzakRvUFZhYUE?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-16 [When Human Superstars Shine: 9 Unmissable Historical Snippets Between Elon Musk and Jensen Huang](https://news.google.com/rss/articles/CBMiU0FVX3lxTFBjclJYNXBJbVBjYUxUQkJCU2pOcDBpVnZZZ2lqWDhZY3lzYk1udjlFWGxNS3loQjAtUDdKYXJySWZWZTJLQ1I1UGtueDdvd2E2RGdJ?oc=5) <sub>eu.36kr.com</sub>
- 📰 2026-11-14 [May Mobility plans 10,000 ID. Buzz robotaxis on €9 million revenue](https://news.google.com/rss/articles/CBMihwFBVV95cUxQdkgzeUVTSS1wc1czVWhUTllrV1ZaVk1VLUUtUTVhTlFVSnJVSGFvcmtvRC1QZHNnWUxHY1B6c3gtUjZqdzFRSm9CSTNuZENtdFlRZGpoaDZGalJQb2xmZ1UtMGJyX1JObkdfaVF6SThudG9kajdDaW1xZVY4dzFraUF6NXd5RVk?oc=5) <sub>AutoNext.co</sub>
- 📰 2026-11-13 [Automobile manufacturing stocks Q3 recap: Benchmarking Tesla](https://news.google.com/rss/articles/CBMivAFBVV95cUxQemM0Qm9BZXFLb2o3YWdJWkFwb1FLcVdMb3NZNDE2bTB2U0hTb29PbnRiQXhFejA3ZklYUEdTR1lZaGpFT2tjOWJPT0luaXF2aXI2ekRhSlhPQnpQNWxQQUpLdTAyeWxvN2dBV2dNcEhiM0VDOWtwNzNtUHlSVVBmMVR3eDZKTWtXSWRvTUd6V1FhVzRqX0MyMDZjQm4xdjAwRmREZEl1X1V3b25CVk9MSUF6Q1draU9nZU1peQ?oc=5) <sub>TradingView</sub>

</details>

<details><summary><b>Aurora</b> (37)</summary>

- 📰 2026-11-19 [Autonomous Driving Nears Its ‘ChatGPT Moment,’ T. Rowe Says](https://news.google.com/rss/articles/CBMikAFBVV95cUxQWmh0UEN2aHUxWE5XdW9ic055c3M0ZW5MMEpDQWprTXdxSldKZ2dUN1RZYU9BWGlQYl9RdHppQ29QY0JmOWNJX1dnRTUxM0s0QmpVYnhGMVRBZlQtMFhPa1B1TkF1ZE9jMXRlUGlYRlRqZTZPQUREZzRqeHJ3VW1USlNzbVZ6a2Z4RWtwVU5mMmc?oc=5) <sub>ETF Database</sub>
- 📰 2026-11-19 [California to Waymo: Get off our freeways](https://news.google.com/rss/articles/CBMickFVX3lxTE9wblcxcTBFUTZ3RzdfZ2ZzalBxM2IzODVGa3RMZjhXcWRDblhyWk5IUzVBZTltRW1aY0U1UDZma0tGZUNKUG8ySTFzc1N2Vzlmclk4a3RpaXJOOXBjNV9GRmF2SWZpV0U5QjJSLXI0T1BQUQ?oc=5) <sub>Land Line Media</sub>
- 📰 2026-11-19 [Waymo soon will be joined in Denver by self-driving trucks, other autonomous vehicles](https://news.google.com/rss/articles/CBMiiwFBVV95cUxOQnNzTDZaMy1wVGVoZGlpTkdrcDBXNkRIR3YwNDA5cVZDemdONmQyajA3SlBiX1l1aGRYdTRVNFFxclhVR09sN1NnWHBFOVdkRkJHYzg1TFV4Mm1FalZnUG5hckI3QkE3MUVrMmRobWdTNjI0MXcyd0pCdWYzRm9hTWk0MVpRU2QwNmxB?oc=5) <sub>Daily Camera</sub>
- 📰 2026-11-19 [Can Humanoid Robots Earn Their Keep on the Factory Floor?](https://news.google.com/rss/articles/CBMixAFBVV95cUxPMHZxYlNrWkdBWDBjSlJKR3pHeGltUUk2R0loMjdQMENnSFFSZG5TZ1NuaExZcXA2c2ZrSXNaN2hIQ0hnUEwtSWhudU56MTdYdlhnTmZvSXNiLUhIckR1T0xRRzRBb3RSSm5sQzVHRk9YMm9yaEUtVVdQMEVhWGJrR2JEVHVNeUxIS0pORHM2bFJDcDdQV0Rqdm1Pb1NUTzRtLWo2cHdIakcxakxmeEhycW00WEdHZ2pBSU9OTGQ3Q1VISEpp?oc=5) <sub>SupplyChainBrain</sub>
- 📰 2026-11-18 [Einride Provides Q3 2026 Update With Revenue Growth, Autonomous Operations](https://news.google.com/rss/articles/CBMiwwFBVV95cUxNbzA5WU0xa0cxQzZ3c29SWWxvVjdzbVA4SE9SelROR2xzaXJfOUpfVUlLU1ZMNDJsRWxVNG5JQi1SUjF5UC1RR1gzZ2tZOVRwcW10WDBRM1ZPT2JSZTc4eERfdFUwSjVfU3FuSmFWbFc3aVV0bFdaSjlROExralJtSjJHcVVremtxdGFudzZmRDhzb1NKS1VMT2V2aEhfY0tBejQtRUJLT1A3SU1vV1lNem13NUxxRUNxdDdETUdZMTFJZkU?oc=5) <sub>TipRanks</sub>

</details>

<details><summary><b>Zoox</b> (103)</summary>

- 📰 2026-11-20 [Where to see F1 cars free in Las Vegas](https://news.google.com/rss/articles/CBMifEFVX3lxTE5rRVNoemlmQWJJMDZfN21ZYndpZENfNHNHbUE2Q2RuaVdCWThIbnMyZUlFTmdaZkhPdld6VGVzeUtzTlF0c2l5elZqTktkb1FJeGpFX2VNalRidzJfWjM4X2FaQ1B1YVY3SzRnSm0yc1g2c25HelNZMi1fMUU?oc=5) <sub>streamlinefeed.co.ke</sub>
- 📰 2026-11-19 [Waymo Pauses All Freeway Rides After California DMV Order](https://news.google.com/rss/articles/CBMihgFBVV95cUxPUDhWbGpIaTlXSzNITFBJSWxkMmhFZFNXU1dZTm1Kb0FLQldxbnB2TkcwdHh6Ympib0lYc3BYOGhKV284UkdocVNQYS1LYUdWZmZVaDdzYlBkdFpkbjlZeGlmU0NJWDF1dmplT0I3WnI4QlRrY1QzVnI1YU43VjdJYmFtU2g1Zw?oc=5) <sub>EVXL.co</sub>
- 📰 2026-11-19 [Amazon-owned Zoox begins robotaxi road tests with employees, their families, and friends aboard](https://news.google.com/rss/articles/CBMihgFBVV95cUxPTFZDTm1XVjBiT3cwY0Zod2xxVlhuQlRlOXNKUVdsTWp6Ujl1RE80RnhmV0MxdzBHWVJPTkY1RmZBWkNqVXFDbUJmcDMwRlg4U1B0akh2NHQ1Q1VhcGR5ZmdfUlB0N1dGUXFYRzZvZ1JBM3FSZ1VRUEpGSDFrVU14UTVzcUpkZw?oc=5) <sub>The Cool Down</sub>
- 📰 2026-11-19 [Amazon Zoox enters Uber platform: driverless rides in Las Vegas](https://news.google.com/rss/articles/CBMijgFBVV95cUxNUHh1RnNsb2dZcElfYkxQV3hybk50dmNHSWNGZ0hzLUlzS3pZVzBkellCTnM1bHZ4Q05VSURzZ0dYY1RPXzV5SFBpS2xYZFpNVzBYU041Ny1IWGRpMGJJM2tyOUQzX25lb2ZmSWlOOGVPcFNNd1dHNC1tVWNrN205Z1p6TlNERHZxV3FXd21R?oc=5) <sub>hi-Tech.ua</sub>
- 📰 2026-11-19 [Amazon's Zoox Just Joined Uber—Could That Change the Robotaxi Threat?](https://news.google.com/rss/articles/CBMipgFBVV95cUxPTFV2Q1JSUE9NWlF0V1dtd0syUFlVY21mb21saW45Nkl1bzBoYlJlM2FHdFVnejF5U3NFS3lZNF9RbVFUR3k0TWgxam1URXpoVHU0OVByUDE5dVFOU0RFb2FrWU9EdlRtVGdfcUpZd3dFUkhnTWU3Y3lyWXpPdHpQTWJBSGhPbnlQTFplYjlGVERzQ3RudHFmM21jUXZEWWRWV1ZYVG9R?oc=5) <sub>MarketBeat</sub>

</details>

<details><summary><b>Motional</b> (33)</summary>

- 📰 2026-11-19 [[Why&Next] Supplying Vehicles to Waymo, Investing in Motional... Hyundai Motor's "Two-Track" Bet](https://news.google.com/rss/articles/CBMiZEFVX3lxTE1fcTNiSzhBMzRuMGl2M0FtOTQyYmY5TDR0d3BoRmJ0RXdMYUVnLVlVRUdGYnh2QkFwUFpYdmM4MzhZc3h6a2prSERaU1hNQ2FQOWJzM1pNNnlRU3UwTkV6VjJqOHg?oc=5) <sub>아시아경제</sub>
- 📰 2026-11-19 [Hyundai Motor Company: “Data Flywheel Gap to Widen in 3–4 Years”... Four Group Companies Put 'Data Union' Into Operation](https://news.google.com/rss/articles/CBMiWEFVX3lxTE1KekR0TXpjWmRySUVDc3pyQWw2ZHFIQXhsZV81VzJNYzRxbHVQZDkwNjMxSHZWNlV5d2pBVFFrUERGM3NKZnE1Qnp5SHpSbDJ4UUFVaV9zLUE?oc=5) <sub>파이낸셜뉴스</sub>
- 📰 2026-11-18 [Hyundai Motor Ramps Up Robot Hiring; Muñoz Says "Physical AI Is Our Bet"](https://news.google.com/rss/articles/CBMidkFVX3lxTE5pTkR0WnlGS2hSdDY0Qm05SmV2S3BVMnRiTmh2blBKbHRTOC1HMjhKaE9QY3pqdVdJZlhGcWdJU3JtZW5Ddllua0dYazFPeTJLbVl4QkVfOXp0czRSRnZXUTZzdDUzSlZDck1ON3dNSGdKdFpaWVE?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-18 [Hyundai's Muñoz: "Nvidia Partnership Is Unshaken… Ioniq 5 Deliveries to Waymo Begin"](https://news.google.com/rss/articles/CBMidkFVX3lxTE1GbVF0M3dXQWhSdHVQMThlRGtPVlY1eE9ibndWMkR1Y0hqX2xJajJYTlloVzYzXy05Y0ZyWHMyZzhXNG9yTHpJM1RmU0dEY0o5b2lpaFhRU1pxbHc1UklnWVdjbndady1NYlJCaTd6RXVZSVhlQWc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-18 [Hyundai Motor CEO Munoz: "Beginning delivery of IONIQ 5 to Waymo… Hyundai is a Physical AI company"](https://news.google.com/rss/articles/CBMicEFVX3lxTE1VTHp1elFqNzVGUlVfU3lDSUxKcWpQQTFnMVhSbll1alk2UDhQdVU3eTZVWE1xZUl6ZVpiYm5FcXFyZDRjcmRDOExheWNsRFA3N2xKTVJqdThsSzZtTmtmdGtEUGFKNG91WXFKSFluTUk?oc=5) <sub>머니투데이</sub>

</details>

<details><summary><b>comma.ai</b> (2)</summary>

- 📰 2026-11-12 [Goodbye, BlueCruise! We Install a comma four in Our F-150 Lightning](https://news.google.com/rss/articles/CBMirwFBVV95cUxPY1o5ekZ4WnpraUxVMHV6OVdyMEtEbjQxQXY5STdJdXlHNlN6eUFZNzFwSnA5cFhHd3pNdTZNNy03dXBOZ1ZoX3RFX2E5V2JNTE9aVlhJaG90bW5YWEdzX2NGXzd3VFZ6NG5JVkFrM3daTmY4UDBTN1I4NWU3eGJqUm9tY1VaRWxoZkp3WDJLNnVLQjN5WG9NMzlxLWI0aVU2TFhLUEZwUE5YUDdUcWFJ?oc=5) <sub>Transport Evolved</sub>
- 📰 2026-11-06 [Canadian YouTuber Linus Tech Tips Tests Tesla FSD](https://news.google.com/rss/articles/CBMiggFBVV95cUxNZVZaT1Q4X0NlakJzTnFkTGdqTmFPM3pDbFZPUnBYVVNrVzFxMlpZQ3VaTEJFUmJrNVpjMmZ5RVphUDE4WURNT0x4NkhnN01LdTdzSEVnS2NUNkROams2cnNzNkpnalhWcDVuckhETUtxaDZrSHNXTXhKYUlpN2dPTlZn?oc=5) <sub>Drive Tesla Canada</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
