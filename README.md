# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-11-19 · 1,288 papers tracked · 49 curated.

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
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 21 | [⭐ 562](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
| [GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives](https://arxiv.org/abs/2609.39601)<br><sub>Qize Yu, Lianrui Fan, Boyu Chen et al.</sub> | arXiv<br>2026-09<br>📑 4 | [⭐ 439](https://github.com/groundingpi/GroundingPI) | Precise grounding matters |
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
| [SimWAM: A Simple World Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.07468)<br><sub>Zongchuang Zhao, Xin Zhou, Tianyang Xu et al.</sub> | arXiv<br>2026-08<br>📑 17 | [⭐ 211](https://github.com/H-EmbodVis/SimWAM) | In autonomous driving, World-Action Models (WAMs) have improved end-to-end planning by transferring video dynamics priors to action prediction, but many still couple planning with future-video generation at inference, in… |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 21 | [⭐ 365](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
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
| [MolmoMotion: Forecasting Point Trajectories in 3D with Language Instruction](https://arxiv.org/abs/2606.18558)<br><sub>Jianing Zhang, Chenhao Zheng, Yajun Yang et al.</sub> | arXiv<br>2026-06<br>📑 20 | [⭐ 153](https://github.com/allenai/molmo-motion) | Motion forecasting is central to visual intelligence: agents must anticipate how objects will move in order to plan actions, reason about physical interactions, and synthesize realistic futures |
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

<details><summary><b>Waymo</b> (216)</summary>

- 📝 2026-11-05 [How the Waymo Driver Manages Severe Winter Weather](https://waymo.com/blog/2026/11/winter-weather-preparedness) <sub>official blog</sub>
- 📝 2026-11-05 [Rethinking What Freedom of Movement Feels Like for Women](https://waymo.com/blog/2026/11/because-women) <sub>official blog</sub>
- 📰 2026-11-19 [Waymo pauses driverless taxis on U.S. freeways after California traffic incidents](https://news.google.com/rss/articles/CBMiywFBVV95cUxPbldKa1dEUWkwU2k5X254WGpCS1RDbFlWcmZ4UktIdHY3OWhNNExnNXlTbDI5TVlVQXZ3b0pLcU1iRTJSZ2FMd3ZBWTFhd3JRVll4Z0MzcHY0TFRvb0E0NDVnTkw1OXI3SnJhdEt4S3ltNjZCaGNaYTdnN3ZfNTFZRjN4by1yS1ozZ3M3R3VsTXl6YS1IeWJNRnVZSl81QmhsY3FLSXNNSzdGSjJnYy03Z05jVnBYbmN6cE5hTl9ZdkF5ZlUyS3NsQWpnWQ?oc=5) <sub>The Washington Post</sub>
- 📰 2026-11-19 [Will Cincinnati welcome Waymo after California ban?](https://news.google.com/rss/articles/CBMiyAFBVV95cUxPZ0RBc1pSRVY3M3VkblVjWnpYdFd4LS1BdE5jUmJaQlRPNmsxR19HUWdSVFFvM3MtRzJBTjctRXhpdWs4aGxJRHp2N3lOU2Z1SFd3WW52WDU2d3RSZ3otbUppNjdXSExYREZhZzdRZ21RVy1UQUh1RmtreTBMY3JkS0xwUVRjYndGUnZEZDZmbnFTV1NTakxyenFzMEoxZ2tkNzZVM2VQYnIyd1lNYlpBZldHQXFPSzd1TmhCZ3dtQTdXZFFjLW1oVg?oc=5) <sub>Cincinnati Enquirer</sub>
- 📰 2026-11-19 [Waymo temporarily suspends driverless freeway rides in all markets](https://news.google.com/rss/articles/CBMiiwFBVV95cUxNWjM2clFPZDAzMDdTVGZtVFpmMEpUaERQRXlTOTFjUm5jcEw2MWpEZlJIX2c0YVhxd3U5b0d6eWhOcENVRmROUlJ5S042TjdxYUg0ZFdGM2hsT0xPaEpwcXYyNFBNb3ZOcEpNUTYzUl9IcmdUZ3lVU1lJMzNYeDloU2tMc2FPQ1VVOWhv?oc=5) <sub>LiveNOW from FOX</sub>

</details>

<details><summary><b>Tesla</b> (289)</summary>

- 📰 2026-11-19 [Tesla Robotaxi Rides Replace Uber Credits, Loaners](https://news.google.com/rss/articles/CBMihgFBVV95cUxOREFSaWVsZUx0NkpVcWtXYnoycXgyNFV4czN3Vmk1MVdlNHBKSzdxVll5dnVydVhBN1M4MWhIR1ZIdklwQkx2MUZfRFF6TjhUM1ZIWlFqN1Rtck1aellUS2FGSmx0ekhrQzFFUERSYTVNWGtxWDJfUUI1eE9mNlVzM0thMmpmZw?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-19 [Elon Musk says Tesla plans to make an autonomous Model Y with no steering wheel](https://news.google.com/rss/articles/CBMipgFBVV95cUxPU3BVSkNtTXpvSHp4UHpCRFRoZjkzYXpqUEhoMUpldWZwLTNmRFA3amhvRDJqTmE3WlVqeXMtRU1nT2ZYZmNyR0Nidl9YWEJqUDFZSEVFckVISl9HX3RRZFhrZ0EwZXp4TkZsUWJXMEMwS1BBRlVsYXdkQ1g0aVdaNFFLRE9ob3l6akZjVmdGTXY4Nm9XYkNsMUF2OU1nN3Q1TFBMb3hn?oc=5) <sub>Business Insider</sub>
- 📰 2026-11-19 [How Tesla Cybercab personal ownership could change the roads](https://news.google.com/rss/articles/CBMi1wFBVV95cUxPdnc1QjJLdkx6eHpla2dNYXRTaFJpMGxhVld3cG4xQnpWYlFlOWV2RW52SnhZVWZfZml0eml3dWxXSUhqRVdPVDVjX240MFNSSEM4dTBIMWdEVVVraU1vR2dONDVaTU9WcXZlN2o1d3BWcHV5VVE0bHg2TG5tWjFxcFI1dldNR2xTbV95RVVlVlVSakZXVHBjNnFGUS11NzVXTzlybzhISG9uXy10Mko1N1JnbFU3NXpDdGg1ZmZReTdLeXVIaEZDaktiNWZOaVhMVkVvajVCMA?oc=5) <sub>The Detroit News</sub>
- 📰 2026-11-19 [Tesla crashes make headlines, Lidar makes sense, IONNA makes it easy](https://news.google.com/rss/articles/CBMinwFBVV95cUxOUTRKcUZTNTRGYzlDQ2c5Vk9ybU1aSllZd054OHljZmRMSVMtTmx6R1hiM2k0c3c1VkFpaUxjb2lVWDE0bVptaHhmNmQ5WWpjeWRRRW5qcE1vUmFmMjVYbnVrcmlaS2c1M1ZmYlRNc1cxemxVS2JkNG95UThvRXJKNFdUdm0zYnBBa3BWNE5lbFQ2NmpSUmJ2dVlLQ0tpOXM?oc=5) <sub>Electrek</sub>
- 📰 2026-11-19 [Tesla’s Cybercab fleet just had its biggest day ever](https://news.google.com/rss/articles/CBMihAFBVV95cUxPQzRnQlJTMGRkTkpNYjF3RXJyRkN2c3ZmSENlU3pReGZSNkdkejRrOXV2RDY4YVNyQnNyNkJVaUVsZzlSUXNSeUZsb1hieW9BbE9qTEZicUo0ak90ZE1CQlpWZnIzMmZBZjUtWTdKZnJkeTFRelF1OGFkNEZqV3BtWGE5b0M?oc=5) <sub>Teslarati</sub>

</details>

<details><summary><b>NVIDIA</b> (192)</summary>

- 💻 2026-11-16 [NVIDIA/scadactl](https://github.com/NVIDIA/scadactl) <sub>GitHub</sub>
- 📰 2026-11-19 [Hyundai Motor Group, 42dot Recruit 3 Self-Driving Executives from Apple, Nvidia to Expand Silicon Valley Organization](https://news.google.com/rss/articles/CBMidkFVX3lxTE1tZ3lLUVJoakljZTZXOVQ4VjRBQ2tWbEtHdjE3M3hKZ2tvTHVzTVpjbFVDOFVEeXRwRVZSMEdjR2hxUndFZHFNTHBRV3ZIb3ctWnR6ZUZvVElIRGdMTEtXamVaY0NGZ3hrZ2RkZ1cwaGhIcE1kWXc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-19 [Bug in Nvidia GeForce drivers writes up to 30 GB of data per hour to SSDs](https://news.google.com/rss/articles/CBMipAFBVV95cUxQaEQtWEd1blp0TzIzMm43ZXZpQ1ExSnRoN2R0OHZjaXN4ZGltd0Ftb09BU0trQXlZV3JhQUpLbEt2R3JadnMzdWNORFVoT2tyY0VZcjRKcmdOc0M0MnQzZlVCWnF4dlEyVGI0UlIzTTRzbnliWGFyQVZUcnpiSzdKRVE1eFJ5ODkxTURDRW9pcG8tazlwS21scEJnc1NuSGZTQ1IxLQ?oc=5) <sub>news.lavx.hu</sub>
- 📰 2026-11-19 [NVIDIA Details Two-Prompt Cosmos Workflow for Physical AI Data](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9oQVNPX1Z4RnhKVDVfN3p2TV85VjVIdDJCTnZtNmJTX3kwb040UEFkTDh3Zk4zekhRZlFSM0RyWVkzVUp1Y0Y2R1VPeHk0ckhCZFBmeEI4NDI0Xzg?oc=5) <sub>www.tokenpost.com</sub>
- 📰 2026-11-19 [Nvidia Shorts Drive $2.65 Million in Gains for Five Trading Accounts](https://news.google.com/rss/articles/CBMiWkFVX3lxTE51SHowRFhWY2g5aFY2WDVDdzBRajZ4b2lvNTUzRWx5aVQzTi1vWFZLem93M1dSNHF5MDJWLWRGZXVMN1VVMTc0VXN3NmMtTmd0UzgxWFVLcHUxZw?oc=5) <sub>www.tokenpost.com</sub>

</details>

<details><summary><b>Wayve</b> (45)</summary>

- 📰 2026-11-18 [Nvidia contacts robotics startups after Jensen Huang resignation to keep support](https://news.google.com/rss/articles/CBMixAFBVV95cUxNMXdFT01DcG1xOUMzOTZEYXNRV0Frd3hPNTVleTRHMndEQnZ6aEdyejF3TzNvMzBEM0YyZm1sOUVYMmdEc05LU0ZhS2JCMjNROW44ZW1oTklGX2FiOWlaWVowVDRmTUtqWm9sZFk3ZEJib2ZRZWtqenhVdlhIWjFwemY4d3A3TS1qVDZfZTdsTllRWW1kUnNlWUdYZmJwek9aeEZKdGFTdW00LTJ2RmZpZzl1YzNPUzhzQ1ZGaS1hYUs1YUM3?oc=5) <sub>디지털투데이</sub>
- 📰 2026-11-18 [Waymo pulls self-driving cars from US freeways after California ban](https://news.google.com/rss/articles/CBMihAFBVV95cUxOeUxwOEZXY0h0ZnlBRDlfam1EekxqMThtT0lSYks5UWZ3SDIxS09wX2lyeU1ROWdwaC1QQVFPSWFWZDR5dWV6WkNWYjlDSW5laW1PWlRqQ3l3OHBLb0ktRFhCMWdneEZvOTZ1MzgyWno3MnhXU0s4UXU3bUk3X2IxaEF1Unk?oc=5) <sub>Yahoo Finance UK</sub>
- 📰 2026-11-18 [Waymo Pauses Freeway Rides Nationwide After California DMV Order](https://news.google.com/rss/articles/CBMiiwFBVV95cUxNZ1NETWFWSzlHNE1XbjlsVHlPNmw2WVF5WTBUSEpIdFUtMzVFY0dQaG9VNFlmeTd5Y3hYc05kX3h6LUVPdGlfQS1vSVJ0V2NVWHpTaHVVSmtyS2ZNSUpIdDhCWHhsT3VVTlcxWC0wUGdQUERwTGxKamgwcTJISzhUYkdITC1DVkNwWDZn?oc=5) <sub>TechRepublic</sub>
- 📰 2026-11-18 [Waymo expansion poses limited threat to Uber growth, says Jefferies](https://news.google.com/rss/articles/CBMijgFBVV95cUxPQXdiWjVPdnkxamtvTkh5N1FLdDlLSnFXbUl5Yy0xZUFqZnR3dkZZak9pOEgwZ04yZjhzcXd6ajVLRVJHR0c1MlEzOGxrSS13WDBTZkhIRUpNOURkZndoVG8wRnl3Qmc4RHFMbFJfMmRHLTN1ZUlTbnFSWENoR2ctRTd0elJ0cHdLMUNrdWZB?oc=5) <sub>Yahoo Finance UK</sub>
- 📰 2026-11-18 [Mercedes-Benz unveils hands-free driving](https://news.google.com/rss/articles/CBMioAFBVV95cUxQME53Zlk0TWhPUUM3clBMMG9URTNSdnFtb0dSOVZ3ZTFPYmFDaHJiRFQ3Y3pDTHkxeHExLU9PVWZSZFJyTFE3UVY3M2NFVk1LcmxmOTA1a0xaTTZMblVfeWdYaU4yOUlFZnFRcGxyc1ZQV1JUdGZfZUlqbGltb0lPMTNMNzc1NkdMQ3R6YmpTcE9lQ1l4Vkp2U0hKVlZxbmZw?oc=5) <sub>FleetPoint</sub>

</details>

<details><summary><b>Momenta</b> (102)</summary>

- 📰 2026-11-18 [Uber and Momenta Launch Supervised Autonomous Vehicle Pilot in Munich](https://news.google.com/rss/articles/CBMitgFBVV95cUxNRDNyc0RwUzdfbmhxemo0dmhwTHJ2RUw1SkJXMkpCeHRTSVRUSnpyMXBDOUhUYlVxb3J0cU5tTUhRT2h1MEJBMEZoQ24wcTdrX1pwd0RtT3AzcWNaN1A4Nl9ZNGJwWlRlVnVYYkU5V0RGcE1QclRSUnJiaGRjc0V0dDhEeGQtNVhCQk1uMTZLRFJGcEQwWk1MZ2EyYm5JRFFsb3dvaTZrdXp4NFdkY2cxWUhpMjc5UQ?oc=5) <sub>Fuel Cells Works</sub>
- 📰 2026-11-18 [Uber, Momenta launch Robotaxi pilot operation in Munich](https://news.google.com/rss/articles/CBMitAFBVV95cUxQZUtqTHY0cjNyOW5MWkQzcjA0a25nRHhubEk5QlEwVDRlaVppZXQwOUhuV1NNTmtaaUNPOUlOMWZtTy1DWGRaMlNGVnpkRXNZU0xQalhQdFN5VERPRUwxOWc0eDVzZS1kemFiUGVxY3ZqU0dpS3ppd0tpanZ3bzRBZmZxdEFkdUhNVnh1Q1dUX0NvUWZzNnlxNEtIQmpfS216VHppbHhoSU5Dc2drc2tULVNKaVQ?oc=5) <sub>Gasgoo</sub>
- 📰 2026-11-18 [Uber and Momenta test autonomous taxi in Munich](https://news.google.com/rss/articles/CBMijgFBVV95cUxQSE9uSVV1SFIyaEJPN2ctbkFOREowZS1nX2dJM0hlOUI1MnpFZDN1OTdwOUsxNC11Y1VqWHNkYnprX3M4OWxsa2dCQ0J6RUgwNEs2ZlFXbU5lTThGNHViX1RCaDlOaExSRVdSNDA1WDBOWk0tQ2NaaWRkT2NkVE4wbWZSd2pHVXd3UmhhWlB3?oc=5) <sub>electrive.com</sub>
- 📰 2026-11-18 [Momenta, Uber launch autonomous ride pilot in Munich](https://news.google.com/rss/articles/CBMimAFBVV95cUxNNFI3S1Fwajl6NEdTLU5FM2duTExxNnY5UHZRckZEblZ3OWZTQ1pYVGNDMTlJVzJZa2cydWYwR1oxR1B6YkU1M243UmhZeWRaazBNSG1VS2xJem90UkJTTUJqaG5jaF82RnB3WDRjc2RIMkdNZDRxWDctM3VEZjhmSzZPQlE4azBjQ29aam1TNUh6OWpnMGgxeQ?oc=5) <sub>Automotive News</sub>
- 📰 2026-11-18 [Uber Starts First Robotaxi Rides in Germany With Momenta in Munich](https://news.google.com/rss/articles/CBMipwFBVV95cUxNbUU5N0tOQWF1cng3eGd2eWRic09ZaFRjTWJyR1RYSlJBUkdQaC1TcEQtaVR2WWV1eE5hV1VJcm5qVlZVZl91MGlQc1RCMTdmMmR3MXNVV1hOTEtPUkUwYjE3RjZWakVfMkJTVWh0MVUxSkVpbGI1VnJuMXM3WnJKemxWLWVuUUEtYUNTcEFlSWpGZGp1bmE1MGdwLWtWS3VWS05SdUU1QQ?oc=5) <sub>Electric Vehicles</sub>

</details>

<details><summary><b>XPeng</b> (198)</summary>

- 📰 2026-11-19 [Xpeng to hold 2026 AI Day on November 25 with focus on physical AI and robotics](https://news.google.com/rss/articles/CBMic0FVX3lxTFA5MjZqRzVpNDlHTnB3X2U4eDRfZFNOcW85YTVCSEVtODl6VFMyeWR4emNvMHNxYWpOd3ZRNEFOVkxySWZYaXVUX1ZUM1MzVVB3Wmlacy12UG1wdjNUYnUwTnYtbk16NzR0MGNELW15em1iNG8?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-19 [Toyota bZ4X Robotaxi Runs 24 Hours a Day in Guangzhou](https://news.google.com/rss/articles/CBMilwFBVV95cUxQUTRGaTVNRE1RZzltamFfTmxFUGJKVlA0Yk9tYk5EbG9sU1lVVldyQ3dfd3F1eE9YRWlmcWVJek1KYVo0UlBYTFpBSzZmNEd3RUt1OXR2NmVRZ25YREROZnVoYW9HRVhwREJLbW5aU19Rb3RNZTNxSEZ6MXg1QmlReExyUDlBRlQ5emg0dUR3dHBaRXZEYTJR?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-19 [小鹏科技日定档11月25日，物理AI有看点](https://news.google.com/rss/articles/CBMia0FVX3lxTE1sQWMtWlQ1QkswcFBJMVEzbVBWM2hWZF9Vanp0VnpWMllkbWxfUWNmUV9hc011Y3hvUkVvdm51ZlN0RUZOclhENVBRN1A4dkNUUWFDR2g5YXd5ZzRBem9kSTM0WW5hYWRvTkdn?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-19 [小鹏MONA L03值得买吗？12.38万起的紧凑型SUV，3个维度说清+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBZTnFyR1hjRXc4bENnbU8xd2pEZWtXY3BFdDJzYzU2WTlpc1R3OVBaSXl0WDVpX0dQM3FSVWIwUkxWNi01RFhjdDF6WnR2YXM3SHJyOThjRXM0aUpFM1kw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-19 [【视频】为什么要提一台小鹏MONA L05？#小鹏MONA L05](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBoaFA4NmdIY3VUZlNqeEI4OENfdmZmRWN4TDNFSmtXMWZhaTZzQ0x6VlRucXkwajhIXzlMNG5GMVpOWUFydU9CaWpqcnc5cDJ3S1VnNUtCWXBqRHM?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Li Auto</b> (168)</summary>

- 📰 2026-11-19 [Another Chinese EV brand eyes Australia: Li Auto recruits for a potential 2027 local launch](https://news.google.com/rss/articles/CBMitwFBVV95cUxPUy1SRWJxdEc4RVRnNVVhWHBzUmM3VnlUblZ2bW93LTA3NFlhYS0xRmxFS3U1QTBNeEx2Q2Q1YVJ6cDczRk5WbEtXSVZoTHVNdHBmcGRhSkZqQUY2RjZITXpoaEo1dmFLempYb2pwSXRDUDMtZFJzSk5HeDhpNzFjTU9SaVloX24zV2h2UGtNSGRfclFCeDdsbEpMSHo5UzU4bFo0Y1lLckVpR2dWalBTa2ZQMW9PVXM?oc=5) <sub>EV Central</sub>
- 📰 2026-11-19 [Xpeng to hold 2026 AI Day on November 25 with focus on physical AI and robotics](https://news.google.com/rss/articles/CBMic0FVX3lxTFA5MjZqRzVpNDlHTnB3X2U4eDRfZFNOcW85YTVCSEVtODl6VFMyeWR4emNvMHNxYWpOd3ZRNEFOVkxySWZYaXVUX1ZUM1MzVVB3Wmlacy12UG1wdjNUYnUwTnYtbk16NzR0MGNELW15em1iNG8?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-19 [2026六座SUV四车横评：领克900、理想L9、东风奕派M8与奕境X9，三排空间与智驾该怎么权衡](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9sMENBYnc1OFNtZ21TOVhKQXFySzBPZVd1X0JpVFZkWEJCdU1GNUVFZU5mZjV4bGFQNHpQR1Bmbm5zYWt1UjNMREFDMHBTNHRaRGxHZThxZVZMRmx4TVg0?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-19 [3款30万级家用新能源SUV如何选？奕境X9、小鹏GX、理想L9围绕空间安全续航的实车对谈+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5wRm5oWW45SlhZRm93WUNxa3d4TjFMY1lYbTYyQ1pra29VVzBCbFNISEZMLW00QS15MzItYzhMTVQ1VnhZWDBVODdNUlZHdFFhTzJNalRCMmo0a1hjcjEw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-18 [【视频】理想汽车理想L9 2023款 Pro](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5KRlpQaUpfeGEycjFVZTh0M3lpYnFtUjRKRUlWTW5acHpPUHUyM2pkMHROb19qallzTTlwQmQwajZaSVdSb25lVU9XMURLUWYtSHk5b0xkWENCdEU?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>NIO</b> (162)</summary>

- 📰 2026-11-19 [Xpeng to hold 2026 AI Day on November 25 with focus on physical AI and robotics](https://news.google.com/rss/articles/CBMic0FVX3lxTFA5MjZqRzVpNDlHTnB3X2U4eDRfZFNOcW85YTVCSEVtODl6VFMyeWR4emNvMHNxYWpOd3ZRNEFOVkxySWZYaXVUX1ZUM1MzVVB3Wmlacy12UG1wdjNUYnUwTnYtbk16NzR0MGNELW15em1iNG8?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-19 [Elon Musk says Tesla to keep boosting China output during APEC trip in Shenzhen](https://news.google.com/rss/articles/CBMigAFBVV95cUxNako2TEhyNFBIQnl5c2RqcVNneEZjTzJsTFd4VzY1QThaYk1iRlhvLUx6d2ZDMWhmMVo5cXN1dnRjRlpwQUNYM0RzRWp4eUVsWWY2V1NzcHBtOWtNd00zdHZqaV9ITS1OOUstSG1Ia3c4UkNEVmpBa3plN1FiOV9PaA?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-19 [Ford ships first in-house LFP battery cells using CATL tech in push for affordable EVs](https://news.google.com/rss/articles/CBMigwFBVV95cUxNX195czhtemcwYnpwUzd6MlJkZmZNMncxczZmRUltaEhDTFFqY1FHNFhaMVpDN3oxME5fQ3hXaHdHOWNpN1F0dG9lRVo5a2RnZlNyWkJ4YVk3N1lQMFhtM3o1N0xRd05RR3MwUy1XYmxjUU1kZlpLVW0ycElZOWJ5akFOOA?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-19 [Top battery makers' share in China in October 2026: CATL 40.00%, BYD 21.36%](https://news.google.com/rss/articles/CBMifEFVX3lxTFBQRXpGdU9LRmZiYXBwMHNURnlmQ1Y3dmt5OW9yQ0luYk1OVHRsQjZUUzZrSlhITzRsdjVDbUhVeGl5cVllN2loSTVKUV9JWHp4QjhPZElsNDQ0MGszZUdHclJXaG5fY0lnYkpvYjRPVUF2aGltVlJNeFlVamw?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-19 [Zeekr sets November 27 launch for 2027 7X as it refreshes core SUV lineup](https://news.google.com/rss/articles/CBMic0FVX3lxTE85UkJZYjJySk56clMtV3o0clQ2MUlJYldGYUgtem5hblkwSzJSampzQmJaS3k2RllpWjdiaWRoX2JoanVLV2Z5YXVoMEVlUzlmREJhZ2RkeGxCYUdhNHc0SjRCRmlEdzFDb2ZQRmlSbkNSVTQ?oc=5) <sub>CnEVPost</sub>

</details>

<details><summary><b>Huawei</b> (296)</summary>

- 📰 2026-11-19 [Xpeng to hold 2026 AI Day on November 25 with focus on physical AI and robotics](https://news.google.com/rss/articles/CBMic0FVX3lxTFA5MjZqRzVpNDlHTnB3X2U4eDRfZFNOcW85YTVCSEVtODl6VFMyeWR4emNvMHNxYWpOd3ZRNEFOVkxySWZYaXVUX1ZUM1MzVVB3Wmlacy12UG1wdjNUYnUwTnYtbk16NzR0MGNELW15em1iNG8?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-19 [Ford ships first in-house LFP battery cells using CATL tech in push for affordable EVs](https://news.google.com/rss/articles/CBMigwFBVV95cUxNX195czhtemcwYnpwUzd6MlJkZmZNMncxczZmRUltaEhDTFFqY1FHNFhaMVpDN3oxME5fQ3hXaHdHOWNpN1F0dG9lRVo5a2RnZlNyWkJ4YVk3N1lQMFhtM3o1N0xRd05RR3MwUy1XYmxjUU1kZlpLVW0ycElZOWJ5akFOOA?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-19 [China's October power battery installations hit record 99.4 GWh as LFP share reaches 86.9%](https://news.google.com/rss/articles/CBMigAFBVV95cUxQWUJ4Y0VxRjJNV2ZlWEJMcW9HcnJjS1hkREd5SjNDY1RJbE1ZQVRibUdja25kWkJnTVpYVloyTGlaZTlCOVpvTDFXUHd6NFBQYzktM0JoZW4yZFpMVjhFQXFVNVJCazh1Sk1VT0pLSVdUSkpndkZUVVdRaWIxV3dQWA?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-19 [Dongfeng unit voyah wins independent carmaking licence in china](https://news.google.com/rss/articles/CBMikAFBVV95cUxOYWJULXA4OGJtRWFoR2d0WWE0aXpYVXQ2cHBVRUE5WThqQmZkSUcycFkxd3E4VmYwN191d1Q4RXB6OUVXVFZIUERmbkdiZmNSZ0d4bEpDNmY2OEozc25BSEhUXzZBSnRyX2hPZkZvLWtEOEF4ZzkyMmZDQUlZZFpZOEZsOXRIdGJiZ3JWM1llTjU?oc=5) <sub>Retail News Asia</sub>
- 📰 2026-11-19 [Huawei nova 16s Is RM1,999 in Malaysia After Rebate](https://news.google.com/rss/articles/CBMigwFBVV95cUxOVDc0TzZIbWM3N3AzZXBDN0JycUdZd0tXcEVzMXNXdGk1ZkVNTHRGYUwxLWNENEUybWViWkpQSHdSaTExQmZibGtFZXRudEZUcHE2NzF6RjYwVzdoOW85VXVlbF94Q2RqTHZ1OEVPX2lTdHNTLXRnTTBGUm1yMHQ5LXRrYw?oc=5) <sub>ProductNation</sub>

</details>

<details><summary><b>Baidu Apollo</b> (56)</summary>

- 📰 2026-11-19 [Toyota bZ4X Robotaxi Runs 24 Hours a Day in Guangzhou](https://news.google.com/rss/articles/CBMilwFBVV95cUxQUTRGaTVNRE1RZzltamFfTmxFUGJKVlA0Yk9tYk5EbG9sU1lVVldyQ3dfd3F1eE9YRWlmcWVJek1KYVo0UlBYTFpBSzZmNEd3RUt1OXR2NmVRZ25YREROZnVoYW9HRVhwREJLbW5aU19Rb3RNZTNxSEZ6MXg1QmlReExyUDlBRlQ5emg0dUR3dHBaRXZEYTJR?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-19 [APEC Summit Automotive Industry Keywords: Globalization Trends & AI Implementation in Auto Sector](https://news.google.com/rss/articles/CBMiU0FVX3lxTFBMOGlzWjBweExwNy1KNEZQZVJlOTFQRDZHd2RRYUdSZWJqeXl5YzNhdDY2eDlCU1ZhWUhpbDN3REJwSjdRdlJKTEt1Q1ZyYUZaSUVv?oc=5) <sub>36Kr</sub>
- 📰 2026-11-19 [[Why&Next] Supplying Vehicles to Waymo, Investing in Motional... Hyundai Motor's "Two-Track" Bet](https://news.google.com/rss/articles/CBMiZEFVX3lxTE1fcTNiSzhBMzRuMGl2M0FtOTQyYmY5TDR0d3BoRmJ0RXdMYUVnLVlVRUdGYnh2QkFwUFpYdmM4MzhZc3h6a2prSERaU1hNQ2FQOWJzM1pNNnlRU3UwTkV6VjJqOHg?oc=5) <sub>아시아경제</sub>
- 📰 2026-11-19 [萝卜快跑落地28城，江铃新能源无人车驶向30国](https://news.google.com/rss/articles/CBMif0FVX3lxTE4zVlo4bjVEYzlyQUt2N1lTNDhDYUphcUJzS1FJcEVhdEJFVEctcmhZNHNJSTJxM3gwQ1k0eFFkWUttRzF2ZWY3WU1CMGJRMDJtNWVXdHRVd3llZ0F1cjdxMHhzUW83SHoxX29uMHlZOUJfTEI4ZHJBN3hTcTZDQlE?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-19 [从南昌出发驶向全球，4000 台无人车背后的硬核工厂\|江铃集团新能源汽车公司\|江铃新能源\|萝卜快跑\|无人驾驶_新浪新闻](https://news.google.com/rss/articles/CBMiY0FVX3lxTE9qekRyNEk2TmhVSi0yMXZwX1JWTmlETUdvUm93MThCa1FSTTZ4dG93aUpsUjZSWTlzczI2emFoLTdRYVpkMFpON0pweG01a0hDelpLR1VDTXB1X3pUZTJ2V0I3NA?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>Pony.ai</b> (132)</summary>

- 📰 2026-11-19 [Toyota bZ4X Robotaxi Runs 24 Hours a Day in Guangzhou](https://news.google.com/rss/articles/CBMilwFBVV95cUxQUTRGaTVNRE1RZzltamFfTmxFUGJKVlA0Yk9tYk5EbG9sU1lVVldyQ3dfd3F1eE9YRWlmcWVJek1KYVo0UlBYTFpBSzZmNEd3RUt1OXR2NmVRZ25YREROZnVoYW9HRVhwREJLbW5aU19Rb3RNZTNxSEZ6MXg1QmlReExyUDlBRlQ5emg0dUR3dHBaRXZEYTJR?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-19 [Pony.ai Q3 revenue jumps 75% to $44.6m on robotaxi growth](https://news.google.com/rss/articles/CBMilwFBVV95cUxOUWM5S3ZfS1dIeERtS1I1OERqbkdZM3V0alF1WE5ibk9RUmNKSFpacGxOd1p4LWk2eWFfNXIyX2VHWkhrUjFMUjFzS2NDZnp3bk1KZno4ck9vMnFtZ0NnVFJXaHBoUmxsNWctRER0eTFNWmJJSUZXd0czVENMc0pJUk9XZjdLWndvdE1lcFdGdlBwMl9yaEtN?oc=5) <sub>Tech in Asia</sub>
- 📰 2026-11-19 [Pony AI’s third-quarter revenue rises 75% as adjusted loss narrows](https://news.google.com/rss/articles/CBMilwFBVV95cUxQMGkxTDJfLS1LVm1hYzFzWG1iU09YUWh2eEFFVkZTZzR0bjNBanhCLWRIYjBaWnU5eWNvM3prUlFJNDZSa04tZ0ZLbnZBV2pvNkphTzJ2aWxBRDd0Z1NleVdGOXMzeDVaWENwdmt0d0sxR2xqZFZ0Sk1TSlZhRHNocmlZdXlLWm5JZGVKVmFsckEtU0Z6a3dJ?oc=5) <sub>Bamboo Works</sub>
- 📰 2026-11-19 [Toyota-Built EV Robotaxis Begin 24-Hour Service in Guangzhou; Pony.ai Plans 1,000-Vehicle Fleet](https://news.google.com/rss/articles/CBMidkFVX3lxTE1OeXpKOUpfQmdBVWFjcDdLc3MxZmFTTmY3U3duMWpzX2NvQ3FUcXlIZm8zVXdKdngyU285ellLUzlnYXhxTWxkOFVyNGM1ellXWnM0elQ5VGtmMnNscnRKQnE0Si1VblZtQXphaUdDZWFUTDA1NEE?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-19 [【BT财报瞬析】小马智行Robotaxi收入占近四成，自动驾驶能否扭亏为盈_公司新闻](https://news.google.com/rss/articles/CBMiYEFVX3lxTE1vRUtRZzJJUVN5VUw3dlNDc2pPTWtNV0Q4SzhBSThWZTZkUGxpT1NFQ0YxTzhZMFVwN3ZrdjBFbFlVT21faHFNRkZIWDZ4UzZ1eExmYTd3T3o3R3Vlc3Q1dg?oc=5) <sub>证券之星</sub>

</details>

<details><summary><b>WeRide</b> (106)</summary>

- 📰 2026-11-19 [汽车行业的终极之车：造Robotaxi，6大厂商的不同思路](https://news.google.com/rss/articles/CBMiW0FVX3lxTE53eVpvOURsQUxZREoxUVZKSkllM1ZCc2NsNTZRSFlTRHlqUDZBTDRhcDB4TmtNSmNLLWhXTHFoRlFqYVc2MWtDSFNITHdoalROTWdiVk5qZmk4T0U?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-18 [小马智行铂智4X每公里1.13元，深圳单车日净收394元](https://news.google.com/rss/articles/CBMia0FVX3lxTE9jcy1tN3ZSQWQ0UzVmQ2ExRTNQcWYxQW13eUN3c3hWZzlnVGJOcTJpaDNTQ0Nha3oyMUdXdENfa241LXFGY19UV2NLVE5qTmJqcHlwMDdkM1dNSFJBbVVlREZGejBmMXBmdnhR?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-18 [Let Users Spend $30,000 to Help Test Autonomous Driving? Tesla’s Controversial CyberCab Individual Purchase Scheme Explained](https://news.google.com/rss/articles/CBMiU0FVX3lxTE5QbGE0SXdibWFMeXJEN05FTGdGeWNKSEhrVGRjNWNTNi1KZkdMdVdpSkZzVzdzWnppTGNlUEdocDBjZF92TVlaYnptb2wyZWx3RVlB?oc=5) <sub>eu.36kr.com</sub>
- 📰 2026-11-18 [Uber Technologies Targets 10,000 Driverless Vehicles by 2028 Amid $10 Billion AV Push](https://news.google.com/rss/articles/CBMi3gFBVV95cUxQYURnOE5NSVZZODU3WEpLb2xjT3poUzlXSURWc1hCcVFjbkp4Z3FaYnFMNW5oTjVweUdIZWZ2bGdWNkVsTlZlTVdlQUpoMjRzNTlDS3RsQm0ta0ZubDNLeFd2bGYzSVVlLVg4S014bi1RVDU2b2ljOUs0VV82TUFqMDJjTWtLZEs4d0E2TkFZYTlLd3BuR2NRSElLc0xfbVdHRm5ibTlDRkl1bTRpRWp1N1d4TXB1ZVhyOVBmM0ZqYjhnLVNsRjQxcWZDOUdwZko2QWFUUFZzRXMwOWpZTWc?oc=5) <sub>TradingView</sub>
- 📰 2026-11-18 [Uber plans to bring robotaxis to three more Dubai districts](https://news.google.com/rss/articles/CBMidkFVX3lxTE9UX0Q4Nk4zdEFPdWt5a1pvMlNodlNwVW1qS050Um1sVzhFbS10RGNKVlpTZExGVm1SRE9zYnFZOUhLS0tYUGZpdlp1WDJFMnpLRjl5S19FWXVfVktFZVRTdkFfdGk3NHk0aEJjYVgzdjZKOTROcmc?oc=5) <sub>Tbreak UAE</sub>

</details>

<details><summary><b>Horizon Robotics</b> (112)</summary>

- 📰 2026-11-19 [Horizon Robotics Announces LoFT Video Geometry Model With Resources Still Pending](https://news.google.com/rss/articles/CBMiggFBVV95cUxNWFpnWWIxWFNWUzBkVFBWRUdJRnJGM2cxS3RvNnNQcEJsNndwVnNEVXpyOWlhUzNsbU5KMkkwNzlCb2tPbVhkQnJPNUVzV3hzanNkLWYzaE5VSUV0M0l6eFcwZ0FtbmgzSHRETVlFZEZTZ3NhemJyOGtlMTZCdGZVUHZR?oc=5) <sub>Pandaily</sub>
- 📰 2026-11-19 [【视频】300km纯电续航的方盒子，增程SUV也能当电车开？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9GVG43b1NGSTY1aUlCd184WGl5Z2tHTU5Ea3FYUC1ZbnRYb0taUzNBbU42WmhQRjJBdWpOejJKMTJDVTZwT09jalZ5VXNxOTFpbm8wQWRJU19lc1E?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-19 [地平线发布原生视频几何基础模型LoFT，实现RGB视频端到端三维场景重建](https://news.google.com/rss/articles/CBMiXkFVX3lxTE5JUnBqUWQtRXd3bU9DOTFxMllRQzBadWo3YnRYZEUzLUVpdTk3OHRtazdURzFRNko2LXNRNmJ3RG1vRzZ4STdtd0djUVY4R0JWZ256QkdLajZobnpuQ3c?oc=5) <sub>SmartHey</sub>
- 📰 2026-11-19 [【视频】增程SUV续航卷到1300km？iCAR V27纯电300km够野吗](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9lYkpUVG1TMHo4b25NbVpBdzY0WFJMZ1k5Wm4yaENaMXRFcllHTzBaU2laRjZkekgwSjJRLTJKRVQ0RXhobmdvb1BUWTVDWkgtSG5zNFRfVHJUTDQ?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-19 [【视频】2027款iCAR V27 16.98万起两款配置如何选？](https://news.google.com/rss/articles/CBMia0FVX3lxTE4wMU5uN0xadkZOaTQwTm5UbklVVjJQSEhQRkNmZjBBSHJrc0FsU2U1UlhWQjVLaE1fNUFma0sxV1E2NzZGbjBmN2dGZ0tLVXNoczdqTHN4VXlkMDVwWHp5VElfSm8wT1N3U0xV?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (21)</summary>

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

<details><summary><b>Aurora</b> (35)</summary>

- 📰 2026-11-18 [AUR Investigation Reminder: Kessler Topaz Meltzer & Check, LLP Encourages Aurora Innovation, Inc. (AUR) Investors to Contact the Firm](https://news.google.com/rss/articles/CBMijwJBVV95cUxQUG0zV1RGOEJxX3V3Z3I4eDNMdGJoenR4ME12SGdvcnNlRGhpWl9TTld5WUljTmU5R1ppb2RKSmtzUDhlU0ZZTkxWejVDSTFKbkRBS1NiTHBUcThDa0o1TU1BekdKdEVXVzN2ZHp1bVdKM21MQWprbFFjQWhQU3VZc0Y2OHdpek42eDBXQU96bGEzQVFxQmpPWDh0VDBCRVlMVEpFY0FheUVqbUoxR0JCbzBtZXpCT3NSQkZmYk81QXYzTGhXMU1YakM4QldsZ2N0d1FuTUxKQkUxb3VGdi1FWUNlLUQ4Z1l6ZTc0Vy10aElSZUp0dVB2a19XcGxSWkZHUWpTZDZGaWNBVlN6dHpV?oc=5) <sub>PR Newswire</sub>
- 📰 2026-11-18 [Einride expands autonomous trucking operations, plans major fleet growth in 2027](https://news.google.com/rss/articles/CBMizAFBVV95cUxNeXBtWGRJa2JuZlpjYmxXbWNOZlZsdVNkSXZMZmJuUlFrTFR0NzVVZDNGQ3FfQXlMZTNxdlJnbmlUUXJ2bm1yMjZGVy03X2xsZzhHUTM0YTg2TXVoWmt5TXJYZVFRRVdEUTFyMzVMcUdkbTIxVHhlS19EUVpUV0x1cmVvaVZQVldWeVhTUjRORzBfb0RzY29KRmdsMjBkckx2TW41ZnY0MkJSa1ZYZlktSmw4M0ZUSGczX0JTNERIdVRBZnQ2WDd3dmI5VVg?oc=5) <sub>Truck News</sub>
- 📰 2026-11-18 [Einride Provides Q3 2026 Update With Revenue Growth, Autonomous Operations](https://news.google.com/rss/articles/CBMiwwFBVV95cUxNbzA5WU0xa0cxQzZ3c29SWWxvVjdzbVA4SE9SelROR2xzaXJfOUpfVUlLU1ZMNDJsRWxVNG5JQi1SUjF5UC1RR1gzZ2tZOVRwcW10WDBRM1ZPT2JSZTc4eERfdFUwSjVfU3FuSmFWbFc3aVV0bFdaSjlROExralJtSjJHcVVremtxdGFudzZmRDhzb1NKS1VMT2V2aEhfY0tBejQtRUJLT1A3SU1vV1lNem13NUxxRUNxdDdETUdZMTFJZkU?oc=5) <sub>TipRanks</sub>
- 📰 2026-11-17 [INVESTOR ALERT: Pomerantz Law Firm Investigates Claims On Behalf of Investors of Aurora Innovation, Inc. - AUR](https://news.google.com/rss/articles/CBMi9gFBVV95cUxNSDR4T2hDWk1pektycDhrSUhYQWYxTHNuZ1A4VTBfRG94b1FCLUpMY2h5YW9EZ0dDQi1uUjUzM1NNQ2EtX052UWsxYVdSRFNLUmx4cmRKNnRURlZCWDJ3a0xVeUMyWF81QlUxc2ZrY2o5TEc5MGNoaTkzWFV0dS1VaWdIS0xDOVZOZ1duOFVRTm1Gc2RXOVJObUNLSFJMakJfR0dOeDNvV29LMU82VFNUcWpFTlMwX25HcFdHMzNob1RoWE5GNFQ3TzFyOEtNdzI5ZXpqV01CTlZ1UkNUYUM2Y2FXRjV1VmtzQU5oYzkwRFRTbEZoTGc?oc=5) <sub>FinancialContent</sub>
- 📰 2026-11-17 [Kodiak signs up carrier for driverless trucks](https://news.google.com/rss/articles/CBMipAFBVV95cUxOSGVfVHBvY1E1cVQzemgzR0N5cEhQREVvUzREWVhyYWFicXdNOGlnX2p1Tk5YSUpvT1VyRFJLS3U4VGZxY3h6TkhuS0NDX2pUNGpmcHU4NUZfZTB6cFBCYUpOczRiWlN2VTFQYXl2VHdPa3VDc0pEYXd0VmM0SEJZdUJmYkdZM1V5dUhUUnRSMVkxNEdLcDZDRXVDallzUE50Ykg4bw?oc=5) <sub>Global Fleet</sub>

</details>

<details><summary><b>Zoox</b> (91)</summary>

- 📰 2026-11-19 [Waymo Pauses All Freeway Rides After California DMV Order](https://news.google.com/rss/articles/CBMihgFBVV95cUxPUDhWbGpIaTlXSzNITFBJSWxkMmhFZFNXU1dZTm1Kb0FLQldxbnB2TkcwdHh6Ympib0lYc3BYOGhKV284UkdocVNQYS1LYUdWZmZVaDdzYlBkdFpkbjlZeGlmU0NJWDF1dmplT0I3WnI4QlRrY1QzVnI1YU43VjdJYmFtU2g1Zw?oc=5) <sub>EVXL.co</sub>
- 📰 2026-11-18 [Zoox Partnering with Uber to Bring Autonomous Mobility to More Riders](https://news.google.com/rss/articles/CBMiqwFBVV95cUxOb2pmZkprYjF1cVpxQ3h0UzVkRVA5eTQwVzd1MnVpRzFTMXVuTmM5aU1NLXlVakh1R2RnOUxGQlVVdV9VaTNoMTRibndQSXhOMERxQVluSTZ2U3NtN25nZXBjc2Q3MGpoOXVjZlNaMGV0czBoN2RFQUlOX0o1OHd0eTZlSzZlVkVGaUZ6Vk93YnMwYVdqTTAwY09tLXdVWTRxTzNraDZndG40SkU?oc=5) <sub>CleanTechnica</sub>
- 📰 2026-11-18 [Uber, Zoox launch autonomous ride-hailing service in Las Vegas](https://news.google.com/rss/articles/CBMiqwFBVV95cUxON1hJMlRla29mQTN5bkRYejZnNF9jRHlPME1KMDhKSVYzZzFSLXJWNnd6WGt5Tm9RckdKeXV1SWx6UnRQSldaVzFoX3haZnQxWEU0bVBzRXN0QmxJQnNhb0hzZmUyRVBLNVVBYUhPMUJzVW1BbGw3T05GdGdXZUM5RDIweHYxTEtNUmc5V29HNXRKU3BlN21rTDJaMzJob0FmaUNlcFVUYjJFRDQ?oc=5) <sub>디지털투데이</sub>
- 📰 2026-11-18 [Uber Unleashes an Awkward Driverless on the Las Vegas Strip](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPbkUyVG9JUDhicnhMN1NrQmctMkdLc1dhMkFaanVjUlVERDFic0pyWlhRR1FXRmNiRG05RFZNNVZ1a3pwZGtJOTNHSFFyYTlIU3J5ZzhUOFJGSm84aU5WellwdmJzUVI5dl9Xa2ozY0llMERWMGtGTmJmLXlKMTZDUE9rQzU4MmEy?oc=5) <sub>AOL.com</sub>
- 📰 2026-11-18 [Zoox robotaxis on Uber in Las Vegas: how matching works](https://news.google.com/rss/articles/CBMihwFBVV95cUxNcTZPRlZKLW1LMFlQVk8xUG5uaTE2d1ZYcHJsSjI5VXFQSDlIX1V0ZXM2dVlRVHJZNldWYmo1UVp1dFpXQ1NJSUpDcXIyMFhsSU5NZU5Oc0ZsTmU0d0VsVGhubElBY1lZUG1nc1RFSUxqUEZabktNbzlVSEVGRGk4Mmx5dHlfZnc?oc=5) <sub>NeoTeo</sub>

</details>

<details><summary><b>Motional</b> (33)</summary>

- 📰 2026-11-19 [[Why&Next] Supplying Vehicles to Waymo, Investing in Motional... Hyundai Motor's "Two-Track" Bet](https://news.google.com/rss/articles/CBMiZEFVX3lxTE1fcTNiSzhBMzRuMGl2M0FtOTQyYmY5TDR0d3BoRmJ0RXdMYUVnLVlVRUdGYnh2QkFwUFpYdmM4MzhZc3h6a2prSERaU1hNQ2FQOWJzM1pNNnlRU3UwTkV6VjJqOHg?oc=5) <sub>아시아경제</sub>
- 📰 2026-11-18 [Hyundai Motor Ramps Up Robot Hiring; Muñoz Says "Physical AI Is Our Bet"](https://news.google.com/rss/articles/CBMidkFVX3lxTE5pTkR0WnlGS2hSdDY0Qm05SmV2S3BVMnRiTmh2blBKbHRTOC1HMjhKaE9QY3pqdVdJZlhGcWdJU3JtZW5Ddllua0dYazFPeTJLbVl4QkVfOXp0czRSRnZXUTZzdDUzSlZDck1ON3dNSGdKdFpaWVE?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-18 [Hyundai's Muñoz: "Nvidia Partnership Is Unshaken… Ioniq 5 Deliveries to Waymo Begin"](https://news.google.com/rss/articles/CBMidkFVX3lxTE1GbVF0M3dXQWhSdHVQMThlRGtPVlY1eE9ibndWMkR1Y0hqX2xJajJYTlloVzYzXy05Y0ZyWHMyZzhXNG9yTHpJM1RmU0dEY0o5b2lpaFhRU1pxbHc1UklnWVdjbndady1NYlJCaTd6RXVZSVhlQWc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-18 [Hyundai Motor Ramps Up Its Robotics Push ... Muñoz: 'Hiring Robot Maintenance Staff'](https://news.google.com/rss/articles/CBMiU0FVX3lxTE51OGxXZnRrRVRCQzRKTmliQlJSVFB2NUh0QWVsdVVVM3FfQzU1NkpMU01oVnZGNVExUVZHdWpoME96Q3RuR2RLYnNaN0pQTnJfVWhr?oc=5) <sub>매일경제</sub>
- 📰 2026-11-18 [Hyundai CEO says Nvidia partnership remains key despite CEO change](https://news.google.com/rss/articles/CBMiggFBVV95cUxOSXh1T2prSXk1N25jeHIyY0RIRGFxU1BmUTJxWk00VkdLcC1CNFJ5YjhvZXR5a2xBR0h6eS02U2VlY1c5YU55UERnclZKV2JRZllzRUptTENmeE9kZW5YMktwc3pBWE5aVk51RGI4SXFDU25qWWh1YjlZdEY2MHVtVThn0gGWAUFVX3lxTE54UnM0d1JobVNDMElXWGVnb3N0VGRzOVBEYUx0U2tNT2pWcEhaYUdmTUszOFJveHJLdFN4M09VMnRFcmlFb1loLW1ZSGFPMHJJcWl5WnRYcHZCWm9KYUVGczRkVlFua0drS1F3MHNuTEdnbWExR01TWEh0ZWZvSExPVGJSejBJTnFzNnpyWHlaX1BfclpJQQ?oc=5) <sub>Chosunbiz</sub>

</details>

<details><summary><b>comma.ai</b> (2)</summary>

- 📰 2026-11-12 [Goodbye, BlueCruise! We Install a comma four in Our F-150 Lightning](https://news.google.com/rss/articles/CBMirwFBVV95cUxPY1o5ekZ4WnpraUxVMHV6OVdyMEtEbjQxQXY5STdJdXlHNlN6eUFZNzFwSnA5cFhHd3pNdTZNNy03dXBOZ1ZoX3RFX2E5V2JNTE9aVlhJaG90bW5YWEdzX2NGXzd3VFZ6NG5JVkFrM3daTmY4UDBTN1I4NWU3eGJqUm9tY1VaRWxoZkp3WDJLNnVLQjN5WG9NMzlxLWI0aVU2TFhLUEZwUE5YUDdUcWFJ?oc=5) <sub>Transport Evolved</sub>
- 📰 2026-11-06 [Canadian YouTuber Linus Tech Tips Tests Tesla FSD](https://news.google.com/rss/articles/CBMiggFBVV95cUxNZVZaT1Q4X0NlakJzTnFkTGdqTmFPM3pDbFZPUnBYVVNrVzFxMlpZQ3VaTEJFUmJrNVpjMmZ5RVphUDE4WURNT0x4NkhnN01LdTdzSEVnS2NUNkROams2cnNzNkpnalhWcDVuckhETUtxaDZrSHNXTXhKYUlpN2dPTlZn?oc=5) <sub>Drive Tesla Canada</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
