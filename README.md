# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-11-18 · 1,282 papers tracked · 49 curated.

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
| [SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving](https://arxiv.org/abs/2610.20609)<br><sub>Shaoyuan Xie, Zihan Zhang, Jingxuan Wang et al.</sub> | CoRL 2026<br>2026-10 | [⭐ 36](https://github.com/ASGuard-UCI/safedrive-vla) | Vision-Language-Action (VLA) models are gaining attention in autonomous driving, inheriting commonsense priors from large language models (LLMs) and widening the navigation interface from a fixed command set to free-form… |
| [Scene-Adaptive VLA: Efficient Autonomous Driving via Dynamic Layer Routing](https://arxiv.org/abs/2610.24590)<br><sub>Yujia Yang, Quan Yuan, Jiawei Fan et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 5](https://github.com/yang-luvu/Scene-Adaptive-VLA) | Vision-Language-Action (VLA) models offer a promising paradigm for autonomous driving |
| [Locating and Repairing Domain Shift in VLM Trajectory Planning](https://arxiv.org/abs/2611.10720)<br><sub>Zhihong Cui, Hengyu Liu, Michael Alexander Riegler et al.</sub> | NeurIPS 2026<br>2026-11 | [⭐ 0](https://github.com/ZhihongCui/MoLaRx) | Vision-Language Models (VLMs) are increasingly adopted as end-to-end driving planners, yet they suffer from cross-city domain shift |
| [AutoVLA-D: Learn a Trajectory-Geometric Condition from Reasoning for Autonomous Driving VLA](https://arxiv.org/abs/2611.12382)<br><sub>Yuguang Yang, Zhewen Tan, Canyu Chen et al.</sub> | NeurIPS 2026<br>2026-11 | [⭐ 4](https://github.com/ShivaTeam/AutoVLA-D) | Autoregressive VLA planning usually predicts continuous trajectories as the final output, but driving instructions often describe actions rather than ego states, which weakens direct conditioning on the final continuous … |
| [CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving](https://arxiv.org/abs/2607.04179)<br><sub>Zhaohong Liu, Hao Ye, Xianlin Zhang et al.</sub> | ECCV 2026<br>2026-07<br>📑 3 | [⭐ 1](https://github.com/MICLAB-BUPT/CritiqueDriveVLM) | End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving |
| [PixelPilot: Scalable Vision-Language-Action Models for End-to-End Autonomous Driving](https://arxiv.org/abs/2607.04637)<br><sub>Pin Tang, Guoqing Wang, Xiangxuan Ren et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 2](https://github.com/VISION-SJTU/PixelPilot) | Vision-Language-Action Models (VLAs), which leverage the advanced reasoning capabilities of Vision-Language Models (VLMs), show promising generalization in complex autonomous driving scenarios |
| [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)<br><sub>Nan Yang, Zhanwen Liu, Linfeng Zhang et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 11](https://github.com/Zizzzzzzz/MVPruner) | Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings |
| [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)<br><sub>Yuan Gao, Wenting Miao, Mattia Piccinini et al.</sub> | IROS<br>2026-07<br>📑 1 | [⭐ 33](https://github.com/TUM-AVS/Chat2scenic) | Validating autonomous driving systems requires diverse, regulation-compliant test scenarios |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 21 | [⭐ 562](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
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
| [UNIVERSE: Unified Video Action Models for Autonomous Driving with Flexible Mask-Modulated Modality Generation](https://arxiv.org/abs/2607.05133)<br><sub>Mengmeng Liu, Diankun Zhang, Jiuming Liu et al.</sub> | NeurIPS 2026<br>2026-07<br>📑 15 | [⭐ 6](https://github.com/xiaomi-mlab/UNIVERSE) | World Action Models (WAMs) can improve action generalization in autonomous driving by learning scene dynamics through dense future-video supervision |
| [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](https://arxiv.org/abs/2609.26792)<br><sub>Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.</sub> | CoRL 2026<br>2026-09<br>📑 1 | [⭐ 15](https://github.com/VAIL-UCLA/DreamStream) | Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions |
| [DriveMLP: When Training Strategy Outperforms Model Complexity in Autonomous Driving](https://arxiv.org/abs/2610.29676)<br><sub>Alessandro Canevaro, Julian Schmidt, Hang Yu et al.</sub> | CoRL<br>2026-10 | [⭐ 6](https://github.com/alessandro-canevaro/DriveMLP) | Learning motion planning policies that remain reliable under closed-loop execution is a central challenge in Autonomous Driving (AD) |
| [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)<br><sub>Shen Zheng, Anurag Ghosh, Gaurav Parmar et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 32](https://github.com/ShenZheng2000/WarpI2I) | Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs) |
| [G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance](https://arxiv.org/abs/2606.26017)<br><sub>Hang Yu, Ye Jin, Alessandro Canevaro et al.</sub> | IROS 2026<br>2026-06<br>📑 6 | [⭐ 7](https://github.com/HangYuu/G2DP) | In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors |
| [SimWAM: A Simple World Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.07468)<br><sub>Zongchuang Zhao, Xin Zhou, Tianyang Xu et al.</sub> | arXiv<br>2026-08<br>📑 17 | [⭐ 211](https://github.com/H-EmbodVis/SimWAM) | In autonomous driving, World-Action Models (WAMs) have improved end-to-end planning by transferring video dynamics priors to action prediction, but many still couple planning with future-video generation at inference, in… |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 20 | [⭐ 365](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
| [Latent-Centroid Steering: Single-Pass Classifier-Free Guidance for Command-Aligned Autonomous Driving](https://arxiv.org/abs/2608.00237)<br><sub>Meibo Hu, Jiamian Wang, Pichao Wang et al.</sub> | IROS 2026<br>2026-08<br>📑 1 | [⭐ 2](https://github.com/codingmlinprocess/LCS) | Vision-language models (VLMs) have recently emerged as a promising paradigm for end-to-end autonomous driving, enabling agents to map multimodal inputs and high-level navigation instructions directly to executable trajec… |
| [STAGE: STyle-controllable Action GEneration for personalized autonomous driving](https://arxiv.org/abs/2607.29517)<br><sub>Zihao Liu, Xing Liu, Yizhai Zhang et al.</sub> | RA-L<br>2026-07<br>📑 1 | [⭐ 5](https://github.com/CarlDegio/STAGE) | Driving style refers to the behavioral preferences that drivers maintain during driving, shaped by their diverse experiences, habits, and needs, and is typically reflected in varying levels of aggressiveness |
| [A Survey on End-to-End Autonomous Driving Training from the Perspectives of Data, Strategy, and Platform](https://arxiv.org/abs/2610.00926)<br><sub>Chengkai Xu, Yiming Cui, Jiaqi Liu et al.</sub> | arXiv<br>2026-10<br>📑 5 | [⭐ 110](https://github.com/Jiaaqiliu/Awesome-Training-Ecosystem-for-E2E-AD) | Autonomous driving is a cornerstone technology for the future of intelligent transportation, where end-to-end learning has emerged as a transformative paradigm that directly maps multimodal sensory inputs to driving acti… |
| [AutoE2E: Don't speak - Language free end-to-end autonomy A Real-Time Driving Model for L2++ ADAS and L4 Robotaxis](https://arxiv.org/abs/2611.22374)<br><sub>Muhammad Zain Khawaja, Zaynab El Mawas, Ryota Yamada et al.</sub> | arXiv<br>2026-11 | [⭐ 227](https://github.com/autowarefoundation/auto_e2e) | AutoE2E is an open-source end-to-end driving model developed by the Autoware Foundation Robotaxi Working Group |

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

<details><summary><b>Waymo</b> (197)</summary>

- 📝 2026-11-05 [How the Waymo Driver Manages Severe Winter Weather](https://waymo.com/blog/2026/11/winter-weather-preparedness) <sub>official blog</sub>
- 📝 2026-11-05 [Rethinking What Freedom of Movement Feels Like for Women](https://waymo.com/blog/2026/11/because-women) <sub>official blog</sub>
- 📰 2026-11-18 [Waymo suspends driverless freeway rides across US after California ban](https://news.google.com/rss/articles/CBMisgFBVV95cUxQaFhXM0tsVjB3bi0zZzdsU3AwSlMwdFBTZE1UeUdQdzIxTC16OFkycVJhVXVNelN0NW9ScnZnaUhES2RCcDBEWk1aODgxNXFJTlpsMzhUTzNsSWpzZ0ZZLVVnMDFfNm9Ic0V6cTBTSFRyMjU1dXpVRFRBZzBhVlZqU0kwb2NDbmo2d1RUa3ZLcGRUTVRNRlI2WjJBaWVXRmtHNi13Q1BPN0JyN1dISXV2WGF30gG3AUFVX3lxTE8tX2lldzhza0k5RS10U1RXYzk2ZnBTYkV1dFB0OElrTjdtb3d2YnJYdl9uamQ2REktbGF1ZmF6V0Exa2R4UXlwaUhBT2RockVvQ1lRSmRzaU5BUmg2MzQ3WE9WdjJMblpwU1Zld0Yxenk1cGRST2hXaElkMV96WTZNVVJ5eVM1TFFyMVpJNjVXTV8zLWRmRmcxcEZETTB5dDJOTTRRdGdxMGY1RDBpSW5sWE5LSDlsTQ?oc=5) <sub>Al Jazeera</sub>
- 📰 2026-11-18 [Waymo pauses robotaxi rides on US freeways after California ban](https://news.google.com/rss/articles/CBMixAFBVV95cUxQTkw0bE5kQUlYTVp4amxvbkwtbnc3ZmZTc0FUaWtiUmtmbkF6SldmOXpGOUt0T3BHRk0zOVN3QXpLQ0d3UDRwakVSblEwT3h1NHV5ekdyVHhCMDJBOGtsZEdaZDJzUGlYTlMxRGxXWjZmRDU5dnh1Y1NyY0duUlFmNEF5YjVxQV85aVBhTUw3UGptQ1hBSFJQSXpVRkg4VXd4VEdlak9MTDdjM1FOTVdzaHB4djl1Y21VSGtLU1hLcS1OTTdl?oc=5) <sub>Reuters</sub>
- 📰 2026-11-18 [Waymo suspends all driverless taxi rides on freeways after ban in California](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQWDB2R0RQRGVXUFMtd0M3YUoyRXlSaDZVWVBWRVBKT3gwc3MxQjN3a01fREpMdDFwWXRJaFZuQ0sxTUJzYXkyMGMwOGs5YVUxeUwwd2owRnRuRFl0NWxuT0VHZ2k0eHF1Q0tTc0NoVi1mYTQtM1NrQUUyZ0VzcngzQjZ1M1d6QWRwNzlnQm5qQ0JUVmNXN2NEQ3U5eFpJN3pGSTVUTmRtN1VHc1E?oc=5) <sub>AP News</sub>

</details>

<details><summary><b>Tesla</b> (274)</summary>

- 📰 2026-11-18 [Tesla Robotaxi Hand Signals: 0 Drivers in Texas Clip](https://news.google.com/rss/articles/CBMijwFBVV95cUxQR2gxQ1BSRnhjMXNKaGQ3UVR6RTRrd2RHYlBMZTRVMTNrTm9NSGZfOWMxNlBGdW1lZUIxdHlYR2hlU3RnLUxLQ25qa2pSZTVIbGpJeDl2c3ZlaUhTbVc0ZFlpbVg2dG8ydW41bVVxUEZlTUI4cTZWdnF2eW1Ub2U2UHpuclFGeDhDY3FBNTNMNA?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-18 [Tesla Robotaxi Follows Construction Workers' Hand Gestures at Intersection](https://news.google.com/rss/articles/CBMirAFBVV95cUxNeTdWUDkydFM1dVVyVW9nZUVWQ2htS0tTNmVBMGVrRGdxYXRJZXRvZ081YjlwVHhKaGlfYndaX3dYczhPdlRMQ0piUHM4RHAwRUdzZDhqOGwtWWpOdUYxOWlRLUtoQ2pCcnFBQkllY3B6TGZfSHJULXdTdFRaMy0wTk5Rb2toMk90dW5TY1hoWTZjWjFJY3VweW16emx2X211S1VCWEg1dzZzQjh3?oc=5) <sub>BASENOR - Tesla Accessories</sub>
- 📰 2026-11-18 [Warning: one ride in FSD Supervised and normal driving gets boring. People keep saying the same thing after their first try. "The videos don't do it justice." There's life before FSD, and there's life after. @Tesla / Writer: Annette, Designer: Janné](https://news.google.com/rss/articles/CBMibEFVX3lxTFB4bFJNLXJzNlY2SXJMaU1zb05UVl9EejNmdzlSdnB5dE5BOXRCY05ZNF94czZZMGJhWHBnZTliNkVpQ2lKemExVkxZS3BqajdoLV91T0hPTEJVVXEtT2VEenZENEVfT3hUMU5qWA?oc=5) <sub>X</sub>
- 📰 2026-11-18 [Can Private Vehicles Join Tesla Robotaxi Service to Earn Independently Next Month? Elon Musk’s Latest Unrealistic Promise](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1QanJMX25IVkRUdnJjVDdqTEpIM0JXek0wZFBkT3ZyT0FZejgyM0NsOHR0TFFjazlqdFNGRk01MHhkMklzSzAxejJ0WVZIMWNVRzRR?oc=5) <sub>eu.36kr.com</sub>
- 📰 2026-11-18 [Waymo pauses robotaxi rides on US freeways after California ban](https://news.google.com/rss/articles/CBMi0gFBVV95cUxPeEJHTkYwTXdVMTVCb1k4SHJSVkR4cnAybjlHd1dtbjZRU0J2SWFXWFl4UXlmbDBScm1VbUpEN0ltMjZMNWREdHBTeVB4YmVELWNSOEZteklCbzVTLUdyUGctZTZreGNnY05lSjRYMVZBS1RqcGwycHJpRENXWUM0MFBtSC1fLXI5YWR6aXNGb0NYbEV0S0E5VWZaU0FWXzlUVC1xdGFZdU1TcmpyUUtudFJ1QlhSUzhibmJ5QnduckhJMEJLcml3WkdHVGlKckItWVE?oc=5) <sub>The Detroit News</sub>

</details>

<details><summary><b>NVIDIA</b> (173)</summary>

- 💻 2026-11-16 [NVIDIA/scadactl](https://github.com/NVIDIA/scadactl) <sub>GitHub</sub>
- 📰 2026-11-18 [NVIDIA Announces Financial Results for Third Quarter Fiscal 2027](https://news.google.com/rss/articles/CBMioAFBVV95cUxNS1NfbkFJSF9aUlBlMkphNjFXMERWTUluUWdsNjQxajFFbjdEdEJHU0FwRU1USGh2MkVWMUYtNDRFNU1qVHlRSzNyQ2ZUQXZuY2M4bWhmdHVaczZqXzJWaExTVXVIQlIyVWNQMUZsV09Ua0F1UDJ5Wkg0engwakZkbDdkaGRTOHZpN200clNRVXR5QXZRNXo0NDlBaVZJdDE0?oc=5) <sub>NVIDIA Newsroom</sub>
- 📰 2026-11-18 [NVIDIA Posts 14th Straight Record Revenue, AI Data Centers Drive Growth](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPTXBZcHI0QWRXeG1QSnZDRjFIeHJUZEpLU0k4OTBJNndnWkRidzh1T21TV2xoX2IxTlBUWFVhMUR6eUlVS3N5dWVrS1FGWC1QdGp0djdvQ3dqVzlweHVoLTBabnUxSGt2UDgySUpvQU5rallwNmZOUnZmSkdEYVB4Rk1QQmNWUzdE?oc=5) <sub>조선일보</sub>
- 📰 2026-11-18 [Dow Jones Falls 849 Points as Nvidia Woes Hit US Stocks](https://news.google.com/rss/articles/CBMi1gFBVV95cUxPaGltemtQTWNwdnlIR3VySVYxSTVqc19fUDVNMVdkbUVUQV9saU1ldlVsRlpReXozNnE5RWw1WFpNVFpxdVNaUVFlVUtOdXcxaG9LZmhPZWk1ZWdBTEVzTG9jMzcyaVBlMW93Q1Bncno0dHptRlhDRzM3Y1pna21ZNmxYeEM2dHVjRWpQQVpNaVVJZmNvMUREMm1LbzlwblVfU1V3NjFvMllYTmdpckVEX2MwcVhyQkNTSGg3R3RBRmJfR3FuYl9xWjIwZVZHdW5hTDZXaVJn?oc=5) <sub>HDFC Sky</sub>
- 📰 2026-11-18 [SET Index Rises as Nvidia’s Earnings Beat Drives Thai Electronics Stocks](https://news.google.com/rss/articles/CBMiYEFVX3lxTE1SMTM3aVFkcEFSdjh0T3o0VmppTUwxTjFIQ1RIMlBrNnI5T3JBVTJjbXZKdE1zNkFvQlFPOUlxZExvR3BQclktM3ZOYk03aUpTRVh4WUpvbW9XY2gtN092cQ?oc=5) <sub>kaohoon international</sub>

</details>

<details><summary><b>Wayve</b> (42)</summary>

- 📰 2026-11-18 [Waymo pulls self-driving cars from US freeways after California ban](https://news.google.com/rss/articles/CBMihAFBVV95cUxOeUxwOEZXY0h0ZnlBRDlfam1EekxqMThtT0lSYks5UWZ3SDIxS09wX2lyeU1ROWdwaC1QQVFPSWFWZDR5dWV6WkNWYjlDSW5laW1PWlRqQ3l3OHBLb0ktRFhCMWdneEZvOTZ1MzgyWno3MnhXU0s4UXU3bUk3X2IxaEF1Unk?oc=5) <sub>Yahoo Finance UK</sub>
- 📰 2026-11-18 [Nvidia contacts robotics startups after Jensen Huang resignation to keep support](https://news.google.com/rss/articles/CBMixAFBVV95cUxNMXdFT01DcG1xOUMzOTZEYXNRV0Frd3hPNTVleTRHMndEQnZ6aEdyejF3TzNvMzBEM0YyZm1sOUVYMmdEc05LU0ZhS2JCMjNROW44ZW1oTklGX2FiOWlaWVowVDRmTUtqWm9sZFk3ZEJib2ZRZWtqenhVdlhIWjFwemY4d3A3TS1qVDZfZTdsTllRWW1kUnNlWUdYZmJwek9aeEZKdGFTdW00LTJ2RmZpZzl1YzNPUzhzQ1ZGaS1hYUs1YUM3?oc=5) <sub>디지털투데이</sub>
- 📰 2026-11-17 [Nvidia tells robotics startups they have its support as questions swirl about its investment strategy](https://news.google.com/rss/articles/CBMirAFBVV95cUxPbGRrWnlsOHJUN0xqM2kydkxFQS1qTUY0LWY4Q1VrWl9JOFUtVzhLbHhWXzY3Y1hTOTlGY1ZPM2UxaWhsZlNMOXM4VXJsMms5VzlxUUhwa3BUODBXZFh1cHVuTHJ5YnNVcnIwMHg1eE1VRDREX1kyRDJ5VWt2bWNFNC1ESmtlYjAtWGwxWEE0OHJwb0lVcHhrWlQxenhzWEtjcWtYVkdvcHZLN2pU?oc=5) <sub>Business Insider</sub>
- 📰 2026-11-16 [Brits don't trust self-driving cars, survey finds](https://news.google.com/rss/articles/CBMimgFBVV95cUxObEhUVmlYTGI3blZzVzZkRmhjMnJGcEhQTjhiVm5YbExDNUM3UmgtdTRsNEpZVnRfOEJCU1ZvQ2NrZ29vcnlhWFg4WGlGUkpmbDhZNGE1NW5udHI2M21UM3ZMVVlpcXNTS204WGJGTG5HYWhHdGh1TUpwYkpIaVhtZHdIRWFHbU01T2QtLWtUTldieVlkU3BEYVJ3?oc=5) <sub>Female First</sub>
- 📰 2026-11-16 [Weekly Recap: Q3 income growth, wider losses and $4.2B financing](https://news.google.com/rss/articles/CBMiwAFBVV95cUxQYnlsREtGYjdOTjRPMHR4b00tZ05mdEI4UkdHN2xPNjdMVE94MnhqR1VjM0FsT014bk9sTVFSWnZHcmlSdTJ3RmRNdWdlLXpaSTBBVXBiZS1zRDNKZk5KaU9yam9pbHVWd01ZejlEMW8xZjN4bmhHMG1mQjFpTTJlZkJWTjdkaXVNM3c0OHBhWmEzR1U3anh4bU1Bai1TZkgxSjk5MzNPbmpVVWx5SWtTalVXYUpqVUlwM1ZZWXBsa2U?oc=5) <sub>TradingView</sub>

</details>

<details><summary><b>Momenta</b> (86)</summary>

- 📰 2026-11-17 [Mercedes-Benz to Offer Hands-Free City Driving in First Half of 2027, Rolling Out in US and Germany](https://news.google.com/rss/articles/CBMidkFVX3lxTE5CbFFkYzFNd1o3bFRrT1NDMEdMeFU5VXg1WW14NnBwQ05Sc3hvOGdJV29scVZQT1N0YzN2OTd6cnJpODM0SXlhRmZTUHNHclJpZEkzcjJ3bzRGaXAzUHN4LWItNUZxN0Z5d1liTHhSRHBjVXkwSFE?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-17 [地平线炮轰算力虚标，Momenta X7 Ultra甩出700TOPS](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5xVlAwbnRyUGpDXzJwOG5FX2VNTWFRRXlDMzhwLTcwRl9VTS0wcUlUUGo4dTM2WFlqS3FubmUwMEFMbzRmR2E3MzZXdGtSb0plVUJsRkZKUHdIN1E?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-17 [US lawmakers want Mercedes-Benz to disclose details of Chinese ties](https://news.google.com/rss/articles/CBMihwFBVV95cUxPNWFFSDVybVdtUHk2dU9sNUI1SVFDOUszN2x0bDVxMVlUcmxWRFZmUkNuczdZdWVJeWhtcTJMUDg5U2Z1ald6M2R4aFhpaWRSZV9qN1dxSlpGWW8yY055eFY1WFBPR3NVVHQtcGZnODQ0QTJOTlRWTDdGZW1QbVltVHl5S1E5Rzg?oc=5) <sub>Yahoo Finance Singapore</sub>
- 📰 2026-11-17 [Momenta上市市值696亿港元，余凯炮轰算力虚标](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1TRGRueUk4aGhZcTAzVHU0UGE0OG1FU1FZVTgxYmc1cXNtcDRWWlNlRERVbVB0eExvSXVsc01JTnBZR2dZak9KZ3JEMEdWQWhOS0s1ZUdiYm5vLWs?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-17 [【视频】跳出算力内卷！奇瑞新车首发Momenta x XHEART 软硬一体技术路线](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1pSnNBUXZBUTNzdzlramNja0JQM2tpV25jdU1qYVdfTFB1eGJLRHZZRVEwVG42V0J0QWxPYWVWNGo2ZWZzdHByTGhrTlhUaW1zaHZZRHlqdU0tZjg?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>XPeng</b> (177)</summary>

- 📰 2026-11-18 [From Guangzhou to Paris: How XPENG Raised the Bar for Chinese Carmakers in Europe](https://news.google.com/rss/articles/CBMiiAFBVV95cUxObVgzWGZpSlVablU1T2p6bEVTdWp2bjk2MUM2RnhoemttN2V1dVVUZ004Tll2dWRDb2RmV1BfNTRJZHFzVG5lNm9HTGtnRjNybFBwX29Bd1RNVUdsbU9KUlZkcS1NYm5lRjhGVm9CYjNOTlVSUGJCbVhlU0dmVEJ1aVBoX1N6alFt?oc=5) <sub>RADII</sub>
- 📰 2026-11-18 [How Record Deliveries Will Impact XPeng (XPEV) Investors](https://news.google.com/rss/articles/CBMiuwFBVV95cUxOTzhCS0d4VEk0UUFRZV9PRndMLVlkQzYzbVZNRTdpUmVudEFXRTFHOUJXUzgySXJXZUVnVWltLWtFYkpmQ0Q0LTZYVjBXT2ljRHRBX01fNGhYS19KVjBQeWY3NUt2YU1pTUc3ZFQxN1UzaXVTMVZLbG9TNi1yWHZMVVBORGN6YUdvVU5zWkdKckdPRFk3QTRLTDk2dXdrbHFRZXhLMlExX092WkFTc0tUa0xaV0RjbTE2OHBZ0gHAAUFVX3lxTE5qcV9uUndMaEUzekpDb3JXWnU0MDktOVpodjU2RklFYW9yNXJrQjl2WHhsRWxZS3l4YWJRTHlKTDYzZ3ByckRRT0E3UTZKek5ZOHc0MlZUeUlDYXVUZl9zV0xxOHNJaDhUbFY2QmdRbTVPYi1tU2ZhWHJqemZxbjdObUcxNEJ5eGFWVEhLR092WW9HdUtRR2VWM01QRXdhcVdNb3k5V1VkaUN3cHdQNS13LUkyV082dUFCRjNPSElCWg?oc=5) <sub>Simply Wall St</sub>
- 📰 2026-11-18 [【视频】小鹏G9 2026款](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1NQW95a0x4cTJBdFpyU1RDdUpBZnRuR29JSkF3Y3d6Z3dnd0VZVGFoNmlYa2txUV9pa01ldExjYXpDVS1fY1NwMkpEMkh1MHZVTjhvZXB1VzRYTEU?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-18 [4款家用新能源SUV怎么选？奕境X9对比问界M8、理想L9、小鹏GX+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9yam1yODBTd0VUV281bTd4c1RVRWp2ZkdQbEpPSnZBY3Ayc0ZRRXZCTXJzN29PSUUtTHoyTl9TSHRFNUZkMVY4cU81UEZFVEQ0cVZJNkdXWkJfaWs1QlU4?oc=5) <sub>新浪网</sub>
- 📰 2026-11-18 [【视频】提了台小鹏L05#小鹏L05](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1Iajk2WmdwMWZXdzg4SkEwSG1VM3pqemJnVk1LLWdLbHNtdC1pd1BLek5DLU9jMGhodERsNGRYdm1VX2k4Zk1MZFREcW53dFFLb1ViWUIxR3ZKZ1k?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Li Auto</b> (162)</summary>

- 📰 2026-11-18 [The first Chinese automaker began L3 autopilot tests on highways](https://news.google.com/rss/articles/CBMiowFBVV95cUxPcEJ3c3RweXlvMzR5MlhQYWNpQnZhcVo5ZmIwaHliX1AxOWpUaVNlTmNMUHFlblBackVhd3hROHpjNVE3Q1VZTEpPVnVhQWhtSnZlX2FueWVGZmdZR1dDMTA4ZHhodTlBb1FRS1JXM0J1SnNheHRSb3Zmc3pjN0hMSGZfQlQ4dGVDUGp2V1doWHpzYWl0cDFTZVFBeHFTZGRubi1r?oc=5) <sub>CarNewsChina.com</sub>
- 📰 2026-11-18 [European car giants face a brutal reality: Chinese technology forced a massive strategy pivot](https://news.google.com/rss/articles/CBMigAFBVV95cUxNY210d2M5N2tHN05yWGZydjhWMW1wVFd6U2ZJRHp1QWNrcXBUaTdjNWdEWGNwOXZOZXZ0Qm52bWE5MGx4OThRZmVrV3gxSEx1TVhJbHRoOGlBYlN3bVBIWmY5VS1rWUo3TXJDWWlSM2RKLTUtWlVNRjBMbW5rbTJ5Uw?oc=5) <sub>PravdaReport</sub>
- 📰 2026-11-18 [【视频】理想汽车理想L9 2023款 Pro](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5KRlpQaUpfeGEycjFVZTh0M3lpYnFtUjRKRUlWTW5acHpPUHUyM2pkMHROb19qallzTTlwQmQwajZaSVdSb25lVU9XMURLUWYtSHk5b0xkWENCdEU?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-18 [理想L9 Livis前5后5锚点，UWB替代3至5种硬件](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9iOHo0TGRuN2ZUM3VmZURFNDZRRkdvdFliaGRDa3A3VzkwdlZidXYwN0k3X2Y4NnhaYWxRbGViSG9VYzhIVnQzX3NRLWtsWXgyUW9IZjRuVll6ZGc?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-17 [【视频】最新到店理想汽车理想L82025款Max智能焕新版](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1lbk51RmR4SC1uNlJab2RHNF9LLTNiMnlndWcyNm5CeGw3Z09pWlJQQ2xtbEx6ODZ2dzJpLVdvQ20yNU5kWnEzdHJsQ1MybmRCOHEwRTRRTDdIaVE?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>NIO</b> (152)</summary>

- 📰 2026-11-18 [BAIC Motor plans to sell battery swap assets as parent expands partnership with CATL](https://news.google.com/rss/articles/CBMie0FVX3lxTE9qRE9vOEhEaFdUZXIyQ1U1Q1l2NTNLWWxuRmYwbU95MHpXWFZOSXFyVGRNVGdnNWRqZlJBVnRVaDk0M0FRN1BFS3hMRFB3OVlWa2phV2tVMzhIV2YtaktWWXpjSUg5S3dzcFhtWXRkaUUybmx5WDRLREhHWQ?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-18 [BYD marks its 32nd anniversary, from making batteries in Shenzhen to building cars overseas](https://news.google.com/rss/articles/CBMia0FVX3lxTE4wajJVRl90dmIwdXdqbGZPSmNDVTZ6N21YQkVXT1NyU3NBNzZTTzlUUF9Yc2xHeWoyeEFZTGxrOUxKOUNWT2hDSEpzUTFFTGE3ektQMFN1N0R2WVV3SldiMmphTldiWkZPT2pn?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-18 [Dongfeng's Voyah gains independent production qualification, strengthening operational autonomy](https://news.google.com/rss/articles/CBMiiAFBVV95cUxQTWJBWDRmbGNsb0RUVUR5R3VJbDBxeWhvajZIckFOeWFRZ0FkcTRSTWctYVNEMWNYNTZaREdHTFRrbFpraFFZT2d5V0xLXzNQeU56SnFfR29LbURoanNaNWhRYmxrOWRISXZGSUlZS3ZKaXVPNmRVTjQ3MGxKUk9pakk4WlZfWHU2?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-18 [盖世汽车研究院：智能悬架2030年渗透率将超40%](https://news.google.com/rss/articles/CBMiUEFVX3lxTFBFNGREVFV3cmRKVUhvZF9nZ2NEUFAxcHdHNzl5OXdXdFFRdDlTcllYSUl6N0Ntbm9jeVpsU1Uzd3lyZFVuWVQ3RTJNNlNxS2oy?oc=5) <sub>盖世汽车</sub>
- 📰 2026-11-18 [【视频】月销均破万，一台中大型纯电SUV，蔚来ES8到底凭什么？](https://news.google.com/rss/articles/CBMia0FVX3lxTE0wSnFwVEJ3alQwRVNMLVVOQnd0ZmoyVm5xRHNPMHlUNTlqbG5wbEJqa1NOR1EyaVFxUzZ2NWg4VUYwYXRsd3Z5NzA5WGN1dmVwa2VLel9RTlBwOUY2TlNqWm1yOTJEdU50LWJv?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Huawei</b> (299)</summary>

- 📰 2026-11-18 [Jetour Global Traveler EV Global Pre-sales, Traveler 7 C-DM Huawei Qiankun Intelligent Driving Edition Launches](https://news.google.com/rss/articles/CBMi_wFBVV95cUxPQWV1QkVNeVZlMWdvamY0aU1hSVZlN0JobWFUUDZTeVd4MmMtR18wU1ZLTlpNTzk3U0Vjak91MmFiVTl1a3Y5QTRIaGZLWWxRaWFyT0M4NVU3ZFVyb0Z0MGpVd3FSMkN0OVliTVMyQVVQNUM2a0lBZmVaRGxoMENJWV8xZXpWbnk1eXRxN2Q5U2RRcV92ZkJtTXdLTE5JaHdFdGtfbTZfRDZ2X3p5V3RIWFJESjY3OFlWZDdySzZWY0oxQmFqcW5JY2JWbmk3YWkxbkxxS3FfalF3bnNhQ1NQTFl3SjR6bGNEc2lHYVppMnEzT2xsTjl6QkFoN25LODQ?oc=5) <sub>Gasgoo</sub>
- 📰 2026-11-18 [The first Chinese automaker began L3 autopilot tests on highways](https://news.google.com/rss/articles/CBMiowFBVV95cUxPcEJ3c3RweXlvMzR5MlhQYWNpQnZhcVo5ZmIwaHliX1AxOWpUaVNlTmNMUHFlblBackVhd3hROHpjNVE3Q1VZTEpPVnVhQWhtSnZlX2FueWVGZmdZR1dDMTA4ZHhodTlBb1FRS1JXM0J1SnNheHRSb3Zmc3pjN0hMSGZfQlQ4dGVDUGp2V1doWHpzYWl0cDFTZVFBeHFTZGRubi1r?oc=5) <sub>CarNewsChina.com</sub>
- 📰 2026-11-18 [BAIC Motor plans to sell battery swap assets as parent expands partnership with CATL](https://news.google.com/rss/articles/CBMie0FVX3lxTE9qRE9vOEhEaFdUZXIyQ1U1Q1l2NTNLWWxuRmYwbU95MHpXWFZOSXFyVGRNVGdnNWRqZlJBVnRVaDk0M0FRN1BFS3hMRFB3OVlWa2phV2tVMzhIV2YtaktWWXpjSUg5S3dzcFhtWXRkaUUybmx5WDRLREhHWQ?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-18 [STELATO V8 Initiates China's First 120 km/h L3 Cross-City Highway Road Test](https://news.google.com/rss/articles/CBMizwFBVV95cUxORFlsVGVBQ1hody1tWkhobVJ1cmYxUkhGM0xqUmg2Z05pc2h3Vm5kTlV6VnlBa0xTMVh1bXkydXZJdHpONEU4Tldad3hOLUVTT01ZcFU5aVFjMm9BMm4ybHpYc19vRHI2OWE5bWdtTlQySXQ1R0JuNmtRUF9sOWJrODdncTIzang0UFlFVnkwcmlJODN1UGZmZ2lPWVhWdzFOUXgta1VjYnhnSE9wX0xnSHVJV3QzVllRZUhMMVNpT3g4dE9PRFpQd0hqOUMxRUk?oc=5) <sub>Gasgoo</sub>
- 📰 2026-11-18 [In closings, Chinese tech giant Huawei is cast by prosecutors as a villain as its lawyer disagrees](https://news.google.com/rss/articles/CBMiiwJBVV95cUxQZm5MRGRCc041S081a09XREIxYkh5YmxoR0UzSXhqcjJhVy1xQnN6bHRrSHVDNEFSaHFQVGVkRXR1akJKbkhVa1NVbFFLd1RMeVhXQl9KMlp4WEptd2VxbUQyWDBORWl2bGtmdzNOMFN4N1plb2JtTEFzSXpuQTgyS2E0a0JkWFpmS3ZFeXVGR3UyUmhGUXRxWDNzTUZmRGJsZnAzQmJvMm9BbnNVNnVPbWVaMTZtQklQVFhyNHlEeUR3MDFnX1o5WWpVeXRiZmpCbTJlNVJEZWY1b2RtTmR5ZjUzSVVJYzRna2l5U2pVU1htQ0liMVZVcmdvVVRxcDB6aU9WVUppMWpzZHPSAYsCQVVfeXFMUGZuTERkQnNONUtPNWtPV0RCMWJIeWJsaEdFM0l4anIyYVctcUJzemx0a0h1QzRBUmhxUFRlZEV0dWpCSm5IVWtTVWxRS3dUTHlYV0JfSjJaeFhKbXdlcW1EMlgwTkVpdmxrZnczTjBTeDdaZW9ibUxBc0l6bkE4MkthNGtCZFhaZkt2RXl1Rkd1MlJoRlF0cVgzc01GZkRibGZwM0JibzJvQW5zVTZ1T21lWjE2bUJJUFRYcjR5RHlEdzAxZ19aOVlqVXl0YmZqQm0yZTVSRGVmNW9kbU5keWY1M0lVSWM0Z2tpeVNqVVNYbUNJYjFWVXJnb1VUcXAwemlPVlVKaTFqc2Rz?oc=5) <sub>Indiatimes</sub>

</details>

<details><summary><b>Baidu Apollo</b> (52)</summary>

- 📰 2026-11-18 [Waymo pauses robotaxi rides on US freeways after California ban](https://news.google.com/rss/articles/CBMilwFBVV95cUxPYkJYNmliaU1HQkhZTmVudDF2bUVsejVtM2paSU9hZDQwTldYM2RUWTNuOGdEQktKVzNyYWhlNk92UlFYa0FOUHFaZDBhQUJkT3Q5LWd1SXJ4c0F3Q243V2l0czQxVVd3Si1VNVRIaG1RWDdjRUxMWEJrYUI4RlNRSG1PUm1FdlRMMWphQld3Z2Y0VXBGb0lZ?oc=5) <sub>DZRH</sub>
- 📰 2026-11-17 [APEC CEO Summit Opens in Shenzhen: Baidu's Robin Li and CATL's Robin Zeng Share Stage as AI and Electrification Take Center Stage](https://news.google.com/rss/articles/CBMidkFVX3lxTE5Bc3UtNW1sRXJhd1NjNXVlNGsyVlpBNFluZDVFMkFuc3dBR2tKa3BRVDhlTGpOdmtISlpIWDJDY3dRWFhpZ3RrQjVSdlp1TlRyVGJnZXNKYkYyTXR3QmtiTVFUbHVITG5wLS1IT0tpTS1mcXh2ZlE?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-17 [Robin Li Warns of AI Bubble Risk: Massive Compute Spending, but Application Rollout Falls Short of Expectations](https://news.google.com/rss/articles/CBMidkFVX3lxTFBGRXI1STBlUGQ4b2toUFZyb0NXNVBTZHpCaU9oV3h2dVlXUWcxd1NVaEExek9TeG9OSXY4cU5kVTBoLXRkaHZ1U084alR4d1Q2R1c1NnA3YWU2ZnF1WGhZa3pkam5NRnhtVXMxVFREWmNqYzFHLUE?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-17 [百度李彦宏APEC峰会发声：萝卜快跑安全记录达人类司机10倍，端到端AI驱动Robotaxi规模化落地](https://news.google.com/rss/articles/CBMiXEFVX3lxTE9wTllOU2RlMUxhMTlfcDVFSWRXZ0V4V3RYamtfSi0wZ0FJSXNLMTNNTEhPZExXaUlRMjNHTUNUaUN0LWFJeVBHTWhxajhkMGlrWS1NV1kyY3p0VlFG?oc=5) <sub>网通社</sub>
- 📰 2026-11-16 [百度第三季度GPU云收入增长191%，昆仑芯M100预计年底前具备量产条件](https://news.google.com/rss/articles/CBMiigFBVV95cUxOaEhjY2tIdE14MHhBZVFDNXU3bEhwbTVydWkxQVdQMXNzQ1AtWHplVDBuOGRYWE9CQnNFYW03aGdCMnpfWGY2NWdIYk9vbWc4Yk5iMURrMTJlenFqeGNQMDRvQ1dtdng4TWc4NUxyclpGQ3NuWExyWE1HLWpFbWNPbzdodVRLQ1JERVE?oc=5) <sub>广州日报新花城</sub>

</details>

<details><summary><b>Pony.ai</b> (93)</summary>

- 📰 2026-11-18 [Pony.ai Launches 7th-Gen bZ4X Robotaxi Pilot Operations in Guangzhou](https://news.google.com/rss/articles/CBMixwFBVV95cUxQMk9lSDNUdnh0ZERkSXhVbXU1U1c4dVMyZEE2NkRiaE5YMzdPeHhkcHNsT0Y0ZnAzMFExWG5LbWQtenBhUXJkNjBHcmdJU0NjRm5lR0VVTDBCelZFNWY3bnlPY1dCUkNnQ0FPRHdXS0FtZ0ROQ1Jsc3k3YkNvRmFBcE1hRHdlSnRPbVZLc0NiRnBfb3lfOG9HRlhhZzFNY1M3ZjJVOFVEZ1RRX3FmT3pzeHhwQlpmSGU2MktPQkp2VjRxZjlfLWJV?oc=5) <sub>Gasgoo</sub>
- 📰 2026-11-18 [小马智行铂智4X每公里1.13元，深圳单车日净收394元](https://news.google.com/rss/articles/CBMia0FVX3lxTE9jcy1tN3ZSQWQ0UzVmQ2ExRTNQcWYxQW13eUN3c3hWZzlnVGJOcTJpaDNTQ0Nha3oyMUdXdENfa241LXFGY19UV2NLVE5qTmJqcHlwMDdkM1dNSFJBbVVlREZGejBmMXBmdnhR?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-17 [Interview: China's autonomous vehicle ecosystem favorable for foreign operators, says Singapore transport group CEO](https://news.google.com/rss/articles/CBMifEFVX3lxTFAxOE9ldk90N3VNb3Z2QkowMllRRmVnMGNOUDZpVTJkNlc2WU1JV3dJcVRwZmNGOFJiMkdMQThVWmQ1YUVvcGxlR1EtdXV3YkVoaGhPcmpUZmhmdFQydURiWUY2RjBxbXlHR1pEZkYwdnZUVnR4b0ZnMmZfZ2g?oc=5) <sub>Xinhua</sub>
- 📰 2026-11-17 [Connected and autonomous vehicles - Pony.Ai and Toyota deploy driverless services in China](https://news.google.com/rss/articles/CBMixAFBVV95cUxOVnB6SkFvT1hlcjNndldjeE1FcFJvVVJhVUQ1NGhYUDdkMlhIZTlxUUJGNmRfRThZdE5aX0tkaXJnWElmd3lzT1dfU093SzhjellGYUVZcldlN3Q1bThvNm1wZDhJc0VmdkhaZnJPbWJtTUdIVGJ6alZsN3B5dEV3VXVaamRhN2Uzd3Brdnc1WEFOMmt3OXFVM3QwM0s5bUN4OGZJQWdRclg2b3BOQWUwRVI2cDI0UlRlNURMNTlERm1mQnZn?oc=5) <sub>Smart Cities World</sub>
- 📰 2026-11-17 [All eyes on Pony AI earnings after Toyota driverless launch](https://news.google.com/rss/articles/CBMisgFBVV95cUxNME9kdmVhLUlPZHVKU3h2Uzk4YTEyMDFlNWpGaFpRbllaV3pSZzNhMUEzeHBGUlBZWkI5S3dLZFFFY0pZREZTbW16ZTJhWVRpSlF3Ty1sYXFobm05TFk1UC1wNmZQWWNjOTRmMU96TlNnd1VaVGhCRnktckc0QldCYWc0Wnk5TmtFbXFpRmpFV1lFMWJNZ2ZpV256RWpDRFREM3JtaS1JTEtZVm1sN2dJSldB?oc=5) <sub>Investing.com</sub>

</details>

<details><summary><b>WeRide</b> (100)</summary>

- 📰 2026-11-18 [Let Users Spend $30,000 to Help Test Autonomous Driving? Tesla’s Controversial CyberCab Individual Purchase Scheme Explained](https://news.google.com/rss/articles/CBMiU0FVX3lxTE5QbGE0SXdibWFMeXJEN05FTGdGeWNKSEhrVGRjNWNTNi1KZkdMdVdpSkZzVzdzWnppTGNlUEdocDBjZF92TVlaYnptb2wyZWx3RVlB?oc=5) <sub>eu.36kr.com</sub>
- 📰 2026-11-18 [小马智行铂智4X每公里1.13元，深圳单车日净收394元](https://news.google.com/rss/articles/CBMia0FVX3lxTE9jcy1tN3ZSQWQ0UzVmQ2ExRTNQcWYxQW13eUN3c3hWZzlnVGJOcTJpaDNTQ0Nha3oyMUdXdENfa241LXFGY19UV2NLVE5qTmJqcHlwMDdkM1dNSFJBbVVlREZGejBmMXBmdnhR?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-17 [【视频】与L4同源的一段式端到端智驾夯中夯10万出头就能上车？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1SX01FemFpRVFObC1sWjkxMi1GcjN3NGNNX0lneE1VUGdCRTNfVE5xWWJRVGVFbDFBZGZMWmVxT1kyaC1WTkJZSnhvekJuQTREczBOdVNSVXloMVU?oc=5) <sub>车家号</sub>
- 📰 2026-11-17 [文远知行将于11月20日盘前发布财报，一图速览分析师最新预测](https://news.google.com/rss/articles/CBMitAFBVV95cUxQaEZJX1lzXzV3cmpSSFI3bU1NRVY2b213MWItRFBEQ3J4ZVQyeER2Qk5kTXpQMjFoZjdycnp3TXZSU1JkOGphRTdKM1UxQndCUFlJUFQ0enNraVJDYWhJeFBkSnJxaXVBRVlQQUxWWDFORjYxbDhOcVVOUlhYdXhNR01JV3pCa1ByeGFmWVJBQWg5VjFXbEZ4Q0R2ZnVGTkRhV2ZRNTFfMTJ1WVpIbFc2MXFYX0w?oc=5) <sub>Moomoo</sub>
- 📰 2026-11-17 [XPeng's Q3 revenue hits record 24.28 billion yuan; He Xiaopeng says scale effects will show quarter by quarter](https://news.google.com/rss/articles/CBMidkFVX3lxTE5pcmRjTkRyM09Id3RvSHpBRnlhYmlOdkNXeG8ySF9FMndvRlBad1g4dzRNT0FWRFRfSkFOT19ER2hodUZpdm83ZTBZa3FNWkQzaVZQdmJoQk5FU0EyaG1MZ3p6R2RucWFTelg3N2d2SVd3TVdNd1E?oc=5) <sub>BigGo Finance</sub>

</details>

<details><summary><b>Horizon Robotics</b> (100)</summary>

- 📰 2026-11-18 [Volkswagen ID. AURA L5 Debuts With 580 km Range](https://news.google.com/rss/articles/CBMikAFBVV95cUxPanVObzJPZ0VkaEFpemhpZ3ltNDVNNDFERHc0REdzZVpZTDFGbU9vNkpIdXBBeDlIUG00eGhEZ3I1SHdtSFpGOHROR0MzSGZ3dm1XRmZLeHUyYU02ZUR4LWI3Qi1Sb1FBLVRTZm93WllJOHJFSkJsdDRGczZDQlpWTG9oYkxZdjdEalZEZ2ExSWU?oc=5) <sub>Electric Cars Report</sub>
- 📰 2026-11-18 [四款方正造型SUV智驾横评：旅行者7、哈弗猛龙、iCAR V23、深蓝G318，谁把高速NOA与城区NCA给得更全](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1GTU9Qa0lGM3hNLU5MRWJZNGFyVTdFUGVDaGI2VFZUUGt2MmJ1aDRIMllsQlByQnQteDRPaklsVk5GSUtsVk9neVVWSVB6U3o4bWlIb0dJcUU3NVB2N2VF?oc=5) <sub>新浪网</sub>
- 📰 2026-11-18 [从V23和V27的销量曲线，预测iCAR V25正式上市价格区间](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5qdUpoTG9QTlVZcm9GRGpvMUZTZTJtSy1CY2xNUmlxWmNuUEdQWnJTYWYtUXl6elR1TDJFNkwtRElMbzRaVHF3Z3hFMWxjRW9QbXhYdmJxWXpRUWM?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-18 [iCar V27销往俄罗斯市场，Esteo V27实车图曝光](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBXT29KeHVTbVV1NmV5QzFKTlV5LWVNTTRoMF9LS3VRSEhiMWpZWmpjY21tVVkyaXlibUVuZGEwUm1NbWZxdGdxcDF0cEVWU19acnA0V2xyaE1nUkU?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-17 [Momenta上市市值696亿港元，余凯炮轰算力虚标](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1TRGRueUk4aGhZcTAzVHU0UGE0OG1FU1FZVTgxYmc1cXNtcDRWWlNlRERVbVB0eExvSXVsc01JTnBZR2dZak9KZ3JEMEdWQWhOS0s1ZUdiYm5vLWs?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (22)</summary>

- 📰 2026-11-16 [又一“国产保时捷”？赛豆ME7实车到店，大过小米YU7配571马力](https://news.google.com/rss/articles/CBMia0FVX3lxTE5fWTNxTkVfa2RHM29CZ3JabmtSbllKTVdGN2x4aVpqS0U0bG81RTFHeDhqNHZhaUg3MGJFVjEzOVU3aDdIMS1zR05mNXZ0blNyZ3cxVWRnVF85bmc3Tl9aenNZSlpDaWRDSV9n?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-16 [AIVA ME7实车到店剑指25万级轿跑SUV市场](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5fM1B6RnpLTlpiVEtIUmJaR0Ffci1BVVpqTzY0ZnBab3JSZ2luNDRWeEhPeHJ6YXlaek9BRDZvdmU0TEw3d2JXTVdMbHgzLXh3TWhLTmpCTDlvdw?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-16 [中国智驾出海新突破！元戎启行交付超10万辆](https://news.google.com/rss/articles/CBMiW0FVX3lxTE80eWh5OVZNRlpOY3ZTN1hMeHlsN1NtbldkODZOVTQ5U3hMVXBrOXZ3RnhWUXA5eXdsNTVYbUlDUnNsNEhnX05Jam9VUUhDZkJ5RmtIb3RJX1IxQ0k?oc=5) <sub>车家号</sub>
- 📰 2026-11-14 [DeepSeek无人创业](https://news.google.com/rss/articles/CBMiTEFVX3lxTE1QUnM4dm1XbE8tWmIwSE1hN1JMTjZKRklrM3FmbkdNbVd2WllWUWpjQVhYV0xwaHhqUHp4T2ZkMGpHMExqWjFNU1lPYXo?oc=5) <sub>凤凰网科技</sub>
- 📰 2026-11-13 [【视频】小米澎程N90和特斯拉Model Y L怎么选，同价位还有哪些推荐？](https://news.google.com/rss/articles/CBMiW0FVX3lxTFB6dElibXRFYWFsZU9vQnhjX3YwZjF2VVd6QjhLdXJIV3pmRGhzTmpuTFRER2xXV1Zjc2ZqNld2RVY1MkxrTENqczVRc2MwNHl1VFljSkt2TjRxZ0U?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Mobileye</b> (12)</summary>

- 📰 2026-11-18 [Intel Cuts IT Jobs as Tan's Cost Drive Extends Into Year-End](https://news.google.com/rss/articles/CBMidkFVX3lxTE9XMEIyWkJScF9ld3AzQXYxN0hhaFJQWnJ3czJVOE9FelQtbG12YUdoWkZmZW55cWdQamJlSnRGQTF4bWVDNi0zRFdfZ0hpVkJFNThWdmYtWDk4WGRBY1F5dWFrRklNQjNLUU1UVUQzakRvUFZhYUE?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-16 [When Human Superstars Shine: 9 Unmissable Historical Snippets Between Elon Musk and Jensen Huang](https://news.google.com/rss/articles/CBMiU0FVX3lxTFBjclJYNXBJbVBjYUxUQkJCU2pOcDBpVnZZZ2lqWDhZY3lzYk1udjlFWGxNS3loQjAtUDdKYXJySWZWZTJLQ1I1UGtueDdvd2E2RGdJ?oc=5) <sub>eu.36kr.com</sub>
- 📰 2026-11-14 [May Mobility plans 10,000 ID. Buzz robotaxis on €9 million revenue](https://news.google.com/rss/articles/CBMihwFBVV95cUxQdkgzeUVTSS1wc1czVWhUTllrV1ZaVk1VLUUtUTVhTlFVSnJVSGFvcmtvRC1QZHNnWUxHY1B6c3gtUjZqdzFRSm9CSTNuZENtdFlRZGpoaDZGalJQb2xmZ1UtMGJyX1JObkdfaVF6SThudG9kajdDaW1xZVY4dzFraUF6NXd5RVk?oc=5) <sub>AutoNext.co</sub>
- 📰 2026-11-13 [Automobile manufacturing stocks Q3 recap: Benchmarking Tesla](https://news.google.com/rss/articles/CBMivAFBVV95cUxQemM0Qm9BZXFLb2o3YWdJWkFwb1FLcVdMb3NZNDE2bTB2U0hTb29PbnRiQXhFejA3ZklYUEdTR1lZaGpFT2tjOWJPT0luaXF2aXI2ekRhSlhPQnpQNWxQQUpLdTAyeWxvN2dBV2dNcEhiM0VDOWtwNzNtUHlSVVBmMVR3eDZKTWtXSWRvTUd6V1FhVzRqX0MyMDZjQm4xdjAwRmREZEl1X1V3b25CVk9MSUF6Q1draU9nZU1peQ?oc=5) <sub>TradingView</sub>
- 📰 2026-11-13 [Korean Optics Maker Optrontec Triples Profit as US Automakers Replace Chinese Camera Suppliers](https://news.google.com/rss/articles/CBMi3wFBVV95cUxPWHNlSUphR3lWUXJBNm93Mm1QdFZ1MVVSZU9jTlBxc0ZuR3JyU3pYQU9OUmk4VDh1NnhCMnV3dXdSenBkVldzS09Zb0NVeGJSc1V3aXhiU1E1aTNsd1RydXlIT2RDdDk5SWZUOC0zbTNlbUxxZVpMaUdIcm1lRUM4U1k0TVBhUmNtMXlCUDh2Vzd3dXE4aGxCRDZlaU5MZFNHNllfRDM3dXoyRWlTckRFREZfRjBpNjhLaW5YVkd3OWJuQWRLVmE2ZFpOck9zdXZrYnVXZk5pYks2WnFKNURZ?oc=5) <sub>Tech Times</sub>

</details>

<details><summary><b>Aurora</b> (34)</summary>

- 📰 2026-11-18 [AUR Investigation Reminder: Kessler Topaz Meltzer & Check, LLP Encourages Aurora Innovation, Inc. (AUR) Investors to Contact the Firm](https://news.google.com/rss/articles/CBMijwJBVV95cUxQUG0zV1RGOEJxX3V3Z3I4eDNMdGJoenR4ME12SGdvcnNlRGhpWl9TTld5WUljTmU5R1ppb2RKSmtzUDhlU0ZZTkxWejVDSTFKbkRBS1NiTHBUcThDa0o1TU1BekdKdEVXVzN2ZHp1bVdKM21MQWprbFFjQWhQU3VZc0Y2OHdpek42eDBXQU96bGEzQVFxQmpPWDh0VDBCRVlMVEpFY0FheUVqbUoxR0JCbzBtZXpCT3NSQkZmYk81QXYzTGhXMU1YakM4QldsZ2N0d1FuTUxKQkUxb3VGdi1FWUNlLUQ4Z1l6ZTc0Vy10aElSZUp0dVB2a19XcGxSWkZHUWpTZDZGaWNBVlN6dHpV?oc=5) <sub>PR Newswire</sub>
- 📰 2026-11-17 [Kodiak signs up carrier for driverless trucks](https://news.google.com/rss/articles/CBMipAFBVV95cUxOSGVfVHBvY1E1cVQzemgzR0N5cEhQREVvUzREWVhyYWFicXdNOGlnX2p1Tk5YSUpvT1VyRFJLS3U4VGZxY3h6TkhuS0NDX2pUNGpmcHU4NUZfZTB6cFBCYUpOczRiWlN2VTFQYXl2VHdPa3VDc0pEYXd0VmM0SEJZdUJmYkdZM1V5dUhUUnRSMVkxNEdLcDZDRXVDallzUE50Ykg4bw?oc=5) <sub>Global Fleet</sub>
- 📰 2026-11-17 [Ease Logistics looks to expand use of autonomous trucks](https://news.google.com/rss/articles/CBMingFBVV95cUxOYUk2VXB1clZ6S0VaenNGUklWaHBnbkd5ankzRjczaWpyUEhHbm5VT216MndJN3RMaVBwSG44S09OaVBWaFM2amxVMHY0MHRaT0J2LTE3N1JNTTFORU16V2tlNjhwX2g2SjJKcDl0a3dvT09jZTFRZTQzQ21YMU8ydjdodkl3ZVY2MWVCeFdtVkF2aHMwMVRYdnlxTEFwUQ?oc=5) <sub>Trucking Dive</sub>
- 📰 2026-11-17 [INVESTOR ALERT: Pomerantz Law Firm Investigates Claims On Behalf of Investors of Aurora Innovation, Inc. - AUR](https://news.google.com/rss/articles/CBMi9gFBVV95cUxNSDR4T2hDWk1pektycDhrSUhYQWYxTHNuZ1A4VTBfRG94b1FCLUpMY2h5YW9EZ0dDQi1uUjUzM1NNQ2EtX052UWsxYVdSRFNLUmx4cmRKNnRURlZCWDJ3a0xVeUMyWF81QlUxc2ZrY2o5TEc5MGNoaTkzWFV0dS1VaWdIS0xDOVZOZ1duOFVRTm1Gc2RXOVJObUNLSFJMakJfR0dOeDNvV29LMU82VFNUcWpFTlMwX25HcFdHMzNob1RoWE5GNFQ3TzFyOEtNdzI5ZXpqV01CTlZ1UkNUYUM2Y2FXRjV1VmtzQU5oYzkwRFRTbEZoTGc?oc=5) <sub>FinancialContent</sub>
- 📰 2026-11-16 [Which Penny Stocks Are Drawing Attention for Stronger Balance Sheets?](https://news.google.com/rss/articles/CBMirgFBVV95cUxPcWhuMFBKNEtPclVId0laSWhGdndMYlJxZEZhUWE2ZFYxVk5RUzM4Mkotb29XYjFiTmlQSDhDTzJETUpicXJMazc0SUxBWnkzdmQ3M0l5UjVOSFMyWDVuei1TQUl2MFRTT2FUNXFxdE1NZktJN05OZnBuMG51dkxfdjZUZ0pWNGxFMVBPbkNjdjFKQVZUNzQ5WXNnbGZFcFhOOVJLSXpVM3NZbFlGQ3c?oc=5) <sub>Kalkine Media</sub>

</details>

<details><summary><b>Zoox</b> (78)</summary>

- 📰 2026-11-18 [Zoox Partnering with Uber to Bring Autonomous Mobility to More Riders](https://news.google.com/rss/articles/CBMiqwFBVV95cUxOb2pmZkprYjF1cVpxQ3h0UzVkRVA5eTQwVzd1MnVpRzFTMXVuTmM5aU1NLXlVakh1R2RnOUxGQlVVdV9VaTNoMTRibndQSXhOMERxQVluSTZ2U3NtN25nZXBjc2Q3MGpoOXVjZlNaMGV0czBoN2RFQUlOX0o1OHd0eTZlSzZlVkVGaUZ6Vk93YnMwYVdqTTAwY09tLXdVWTRxTzNraDZndG40SkU?oc=5) <sub>CleanTechnica</sub>
- 📰 2026-11-18 [Uber, Zoox launch autonomous ride-hailing service in Las Vegas](https://news.google.com/rss/articles/CBMiqwFBVV95cUxON1hJMlRla29mQTN5bkRYejZnNF9jRHlPME1KMDhKSVYzZzFSLXJWNnd6WGt5Tm9RckdKeXV1SWx6UnRQSldaVzFoX3haZnQxWEU0bVBzRXN0QmxJQnNhb0hzZmUyRVBLNVVBYUhPMUJzVW1BbGw3T05GdGdXZUM5RDIweHYxTEtNUmc5V29HNXRKU3BlN21rTDJaMzJob0FmaUNlcFVUYjJFRDQ?oc=5) <sub>디지털투데이</sub>
- 📰 2026-11-17 [Zoox robotaxis arrive on the streets of Atlanta](https://news.google.com/rss/articles/CBMiywFBVV95cUxNbW1iU0d6MG5TRkVjak16bFBhVU9pN0VNWGhjWHJCNVpjdVhSNVdWXzlDYzJsNmNXVGlGd0FGVnFlVkV2SnJvWVNGM3BpTlFnbDdpSVhXLVI3NXlsNVZidU9kOFVfZ3Fpa2Z4TkwtN1VVOVU4QjJTYjgyei1ZT25SS2RrUkhhYS1YczBxQ0xpUlBKTFMxS09NODF2VnNnazhzR3JjVGxEWkFVSm03TllSX2tlcFNqcGVXSFpfdUd0cm8wb19SbnR3cEd2cw?oc=5) <sub>WABE</sub>
- 📰 2026-11-17 [You can now get a Zoox robotaxi through Uber in Las Vegas – KLAS](https://news.google.com/rss/articles/CBMinwFBVV95cUxNNVZfa3lPeGkyQzY1Wng2TkhhM0U3OXFHVzVjSm5tdnpPZ2tZSENsc1Jwa1h6OVRuS29oRlJyU19UbkNxQXpDZ0twbzhqQk1vLWZDT2JvOHo3Tmd5VDVQSUxVSXM0eDZUd3dGTjQ2WUF1anNYZlM0V29GeHBocDk3UGdsS2NZM0JyNVlEVUNLd1FDMEVQMVJMUHVoemlJYUk?oc=5) <sub>KLAS 8 News Now</sub>
- 📰 2026-11-17 [Zoox is now available on Uber in Las Vegas](https://news.google.com/rss/articles/CBMiXkFVX3lxTFBJYzlUTVpudTFTX016bV9pMUZSOUpKVUl2SDM1S1NBSzczdEYzWU9IVHJicHRqdjdiT1Zyd0twM1kwZDE5cUlDYzhZeHhOY25tYjFrR1NMTkV5MlU5dVE?oc=5) <sub>Uber</sub>

</details>

<details><summary><b>Motional</b> (30)</summary>

- 📰 2026-11-18 [Hyundai's Muñoz: "Nvidia Partnership Is Unshaken… Ioniq 5 Deliveries to Waymo Begin"](https://news.google.com/rss/articles/CBMidkFVX3lxTE1GbVF0M3dXQWhSdHVQMThlRGtPVlY1eE9ibndWMkR1Y0hqX2xJajJYTlloVzYzXy05Y0ZyWHMyZzhXNG9yTHpJM1RmU0dEY0o5b2lpaFhRU1pxbHc1UklnWVdjbndady1NYlJCaTd6RXVZSVhlQWc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-18 [Hyundai CEO says Nvidia partnership remains key despite CEO change](https://news.google.com/rss/articles/CBMiggFBVV95cUxOSXh1T2prSXk1N25jeHIyY0RIRGFxU1BmUTJxWk00VkdLcC1CNFJ5YjhvZXR5a2xBR0h6eS02U2VlY1c5YU55UERnclZKV2JRZllzRUptTENmeE9kZW5YMktwc3pBWE5aVk51RGI4SXFDU25qWWh1YjlZdEY2MHVtVThn0gGWAUFVX3lxTE54UnM0d1JobVNDMElXWGVnb3N0VGRzOVBEYUx0U2tNT2pWcEhaYUdmTUszOFJveHJLdFN4M09VMnRFcmlFb1loLW1ZSGFPMHJJcWl5WnRYcHZCWm9KYUVGczRkVlFua0drS1F3MHNuTEdnbWExR01TWEh0ZWZvSExPVGJSejBJTnFzNnpyWHlaX1BfclpJQQ?oc=5) <sub>Chosunbiz</sub>
- 📰 2026-11-18 [Hyundai Motor Ramps Up Its Robotics Push ... Muñoz: 'Hiring Robot Maintenance Staff'](https://news.google.com/rss/articles/CBMiU0FVX3lxTE51OGxXZnRrRVRCQzRKTmliQlJSVFB2NUh0QWVsdVVVM3FfQzU1NkpMU01oVnZGNVExUVZHdWpoME96Q3RuR2RLYnNaN0pQTnJfVWhr?oc=5) <sub>매일경제</sub>
- 📰 2026-11-18 [Hyundai Motor Ramps Up Robot Hiring; Muñoz Says "Physical AI Is Our Bet"](https://news.google.com/rss/articles/CBMidkFVX3lxTE5pTkR0WnlGS2hSdDY0Qm05SmV2S3BVMnRiTmh2blBKbHRTOC1HMjhKaE9QY3pqdVdJZlhGcWdJU3JtZW5Ddllua0dYazFPeTJLbVl4QkVfOXp0czRSRnZXUTZzdDUzSlZDck1ON3dNSGdKdFpaWVE?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-17 [Uber Adds Zoox Robotaxis to Its Las Vegas App](https://news.google.com/rss/articles/CBMia0FVX3lxTE55THR6a21GRF94YzIxNDhmc2pPeFJjeG5sMnhWOFNYNV9tTDY5U3Z6TnE2SF9sZEEySUl0UGZJT1hHWTE0NEF4SlV3eF9VYm90RzNuQi0wYUNfSjBQU2ZhSEtvdEREa0gyOHNr?oc=5) <sub>WeRSM</sub>

</details>

<details><summary><b>comma.ai</b> (2)</summary>

- 📰 2026-11-12 [Goodbye, BlueCruise! We Install a comma four in Our F-150 Lightning](https://news.google.com/rss/articles/CBMirwFBVV95cUxPY1o5ekZ4WnpraUxVMHV6OVdyMEtEbjQxQXY5STdJdXlHNlN6eUFZNzFwSnA5cFhHd3pNdTZNNy03dXBOZ1ZoX3RFX2E5V2JNTE9aVlhJaG90bW5YWEdzX2NGXzd3VFZ6NG5JVkFrM3daTmY4UDBTN1I4NWU3eGJqUm9tY1VaRWxoZkp3WDJLNnVLQjN5WG9NMzlxLWI0aVU2TFhLUEZwUE5YUDdUcWFJ?oc=5) <sub>Transport Evolved</sub>
- 📰 2026-11-06 [Canadian YouTuber Linus Tech Tips Tests Tesla FSD](https://news.google.com/rss/articles/CBMiggFBVV95cUxNZVZaT1Q4X0NlakJzTnFkTGdqTmFPM3pDbFZPUnBYVVNrVzFxMlpZQ3VaTEJFUmJrNVpjMmZ5RVphUDE4WURNT0x4NkhnN01LdTdzSEVnS2NUNkROams2cnNzNkpnalhWcDVuckhETUtxaDZrSHNXTXhKYUlpN2dPTlZn?oc=5) <sub>Drive Tesla Canada</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
