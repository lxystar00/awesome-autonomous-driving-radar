# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-11-21 · 1,280 papers tracked · 48 curated.

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
| [Locating and Repairing Domain Shift in VLM Trajectory Planning](https://arxiv.org/abs/2611.10720)<br><sub>Zhihong Cui, Hengyu Liu, Michael Alexander Riegler et al.</sub> | NeurIPS 2026<br>2026-11 | [⭐ 0](https://github.com/ZhihongCui/MoLaRx) | Vision-Language Models (VLMs) are increasingly adopted as end-to-end driving planners, yet they suffer from cross-city domain shift |
| [AutoVLA-D: Learn a Trajectory-Geometric Condition from Reasoning for Autonomous Driving VLA](https://arxiv.org/abs/2611.12382)<br><sub>Yuguang Yang, Zhewen Tan, Canyu Chen et al.</sub> | NeurIPS 2026<br>2026-11 | [⭐ 4](https://github.com/ShivaTeam/AutoVLA-D) | Autoregressive VLA planning usually predicts continuous trajectories as the final output, but driving instructions often describe actions rather than ego states, which weakens direct conditioning on the final continuous … |
| [CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving](https://arxiv.org/abs/2607.04179)<br><sub>Zhaohong Liu, Hao Ye, Xianlin Zhang et al.</sub> | ECCV 2026<br>2026-07<br>📑 3 | [⭐ 1](https://github.com/MICLAB-BUPT/CritiqueDriveVLM) | End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving |
| [PixelPilot: Scalable Vision-Language-Action Models for End-to-End Autonomous Driving](https://arxiv.org/abs/2607.04637)<br><sub>Pin Tang, Guoqing Wang, Xiangxuan Ren et al.</sub> | ECCV 2026<br>2026-07<br>📑 1 | [⭐ 3](https://github.com/VISION-SJTU/PixelPilot) | Vision-Language-Action Models (VLAs), which leverage the advanced reasoning capabilities of Vision-Language Models (VLMs), show promising generalization in complex autonomous driving scenarios |
| [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)<br><sub>Nan Yang, Zhanwen Liu, Linfeng Zhang et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 11](https://github.com/Zizzzzzzz/MVPruner) | Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings |
| [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)<br><sub>Yuan Gao, Wenting Miao, Mattia Piccinini et al.</sub> | IROS<br>2026-07<br>📑 1 | [⭐ 33](https://github.com/TUM-AVS/Chat2scenic) | Validating autonomous driving systems requires diverse, regulation-compliant test scenarios |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 25 | [⭐ 563](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
| [GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives](https://arxiv.org/abs/2609.39601)<br><sub>Qize Yu, Lianrui Fan, Boyu Chen et al.</sub> | arXiv<br>2026-09<br>📑 4 | [⭐ 441](https://github.com/groundingpi/GroundingPI) | Precise grounding matters |
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
| [A Survey on End-to-End Autonomous Driving Training from the Perspectives of Data, Strategy, and Platform](https://arxiv.org/abs/2610.00926)<br><sub>Chengkai Xu, Yiming Cui, Jiaqi Liu et al.</sub> | arXiv<br>2026-10<br>📑 6 | [⭐ 110](https://github.com/Jiaaqiliu/Awesome-Training-Ecosystem-for-E2E-AD) | Autonomous driving is a cornerstone technology for the future of intelligent transportation, where end-to-end learning has emerged as a transformative paradigm that directly maps multimodal sensory inputs to driving acti… |
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
| [CADET: A Modular Platform for Evaluating Distributed Cooperative Autonomy in Connected Autonomous Vehicles](https://arxiv.org/abs/2606.04072)<br><sub>Pragya Sharma, Brian Wang, Mani Srivastava</sub> | ICRA 2026<br>2026-06<br>📑 1 | [⭐ 0](https://github.com/nesl/cadet) | Deep learning models are increasingly central to autonomous vehicle (AV) pipelines, yet their integration has traditionally followed a monolithic design where perception, planning, and control execute on a single onboard… |

## 🏢 Industry Tracker

Latest 14 days of news, official blog posts and new open-source repos from tracked companies. Full daily feed in [`daily/`](daily/).

<details><summary><b>Waymo</b> (232)</summary>

- 📰 2026-11-21 [Opinion \| I’m a former Lyft driver. This is why I believe in robotaxis.](https://news.google.com/rss/articles/CBMiqAFBVV95cUxQZ2NJeEtCTlp1bEtlMGpZdWZGUmxEa1NmU3dxVjBjMkM4SWdXTlpFeVZ4czcxai1GUVVZNnJnWnA4akg4eGFwbUFadWhNNjhvMGhJVTRLVHlKaUVLcW03djFXZDlOZFlHNHBHdTNsbUNBc1RlU2FzQUE1RU02RV9tX3I1a0VHSU5ueTdCa3luXzhNdS1pMFlyTzMyMnIzV1l2Q2NoTjBuZ3Y?oc=5) <sub>The Washington Post</sub>
- 📰 2026-11-21 [Waymo Robotaxis Face 2 Recalls Over Closed Freeway Lane Violations, Traffic Control Issues](https://news.google.com/rss/articles/CBMilAFBVV95cUxQeWIwMTV4bS1fdnVHT3NrdkptejF6NURtRDdHX1JUbTFhZ2Z3NmZOaC1BM1M0bkVLQ1FwWjFBbnVzengxSU10UUI3U3NvcE1Vc1pxMjEtR015LVRyeFk5b3dpYmpSdVBKLTJKVVdqMmYyVkVCMkJJb2FSd3czd19RRGZYRFZhOWNyZmdPbTJHb2JNUTlj?oc=5) <sub>Benzinga</sub>
- 📰 2026-11-21 [Waymo’s map crosses the city line for cliff divers and sopapillas](https://news.google.com/rss/articles/CBMivwFBVV95cUxNc0hNcnVXdmd2VmU2VmhzS08xNXNEeWhWUThJaHVxQVI4S2MwMHhHSTRzVktybDl3Wmg0eTNrUG9NRTBNelZlNHROeTJ3eFpzZUpGYm8tZHRxZGZWNVBPTlVkS3pyY3Y0VUFPR2RyN2RsVEhSNTByb0ZMTC1rUFZEVzhwOU1KS2VCbS1vN1pKVjJDQXdxTnlOU1JSZEZ6eDdLVXZwZllvM0g4UXE2c2hwMnJoZTdoS0pPTkZySTJSUQ?oc=5) <sub>9News</sub>
- 📰 2026-11-21 [Waymo files two new NHTSA recalls days after California bans its freeway driving](https://news.google.com/rss/articles/CBMirAFBVV95cUxNYXVTWWJQOFgwVVN5Umh1alAxYWJGb1ZKYmZCVUhLUEJEc0RMbzEyeGRCSjJkRFQ1NGs2YmtqMDVVc1FXVVYyQnNraFd5LUJMTnJXX05tV01VMmNIU1daVFhnbC16RHdld2lrSEpVVXRUSVZMbFFaSnZNXzZtS2RqRVB1NnVnaGNDZFAxTEZpcVl4LTN2MWwyMEJZd3U1aWoxaENHTGU5ckt1RjlY?oc=5) <sub>Startup Fortune</sub>
- 📰 2026-11-21 [Waymo Recall Shuts Freeway Lanes, Forces Manual Control](https://news.google.com/rss/articles/CBMikwFBVV95cUxPeUFuM2R4a3FLa3l3V1FtVXUyU1lTRjVxdWlIajZFV1UzNmFldDFWSzE1dFlUalVsRlV0NW9SWDhHYTJtR01tYTh4X1dkSHE1OTJQZ2lhUlZhRHpBakV2TlFwU05CaVNVdmQxZjVQQnh0alJMRTgtNVlHcy1KRml0a0JvRUlodE14TDZUZ1R0blpFR1U?oc=5) <sub>shattered.io</sub>

</details>

<details><summary><b>Tesla</b> (315)</summary>

- 📰 2026-11-21 [2027 Tesla Cybercab Preview: Specs, Price, Photos, Release Date](https://news.google.com/rss/articles/CBMiWkFVX3lxTFA5czdNc3V6czUwVnR0c3liTU1ockRaYkYteVVpeFplLXlIcGZWNk12a3pWclJ0UEVzX1FFNGZxaXlhd0RhblpjTGI4VXJFd25EWnp1eHJNbGhxZw?oc=5) <sub>CarsDirect</sub>
- 📰 2026-11-21 [Tesla FSD Gets Green Light in Italy as First Major European Market](https://news.google.com/rss/articles/CBMikwFBVV95cUxPMkdMQWlNRjJ2OHlTTHFuU2JLY0s5bVNXMk1BZGhGejF2aEZWZHg4YVNOLWRZUDN3MXNyYXp0OExyeWFJNmdkVmF5S2ZJNmZIekdPaTJfVXFvZFZGelpBZXlOQ2ZydGdRTDl5X1V6YjYxMWhGRnpyR1ZNYkl2U3BrYUQyb1NvakRCb3lYeVhlRllTeDg?oc=5) <sub>hi-Tech.ua</sub>
- 📰 2026-11-21 [Tesla Creates Dedicated Robotaxi Instagram Account](https://news.google.com/rss/articles/CBMijgFBVV95cUxOSVJBdk1CTzNQcG9hY1huWUkyUDVHVWNVQ0N2MzVfNWNDWUFyZ3dKb1JmS0dtQ1M1cHNnRGloMjJ3WnVjYjRsTVRuUy1xa0FxTzBMQUFDc0FzVlM1REgzbDZPYkFZZEpPOXgzT1N1d2JpMUp5YWdUV24xZUM1b0VHdnB5eExfNFBNSHhwZFhB?oc=5) <sub>BASENOR - Tesla Accessories</sub>
- 📰 2026-11-21 [Cybercab Under $30K & Tesla Merger Talks: What to Watch](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNUV9vd2xiT0RLNVZfS1NMMHFQZDZCeEtrQXhFZEExeExhek4zc1BaUi1ab0p3Z3B2bG02VkJWOHpIcVBxS3JxTXhRVFRYZXhfSnV4OHVnbDVmWC1reXM4SmFxV3dQYk5KeTJvdWw0TlVCa3ZoV1NoNDJDSUdzU0ZmQklYTzljTE1I?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-21 [FSD V15 in December: 5 Details That Matter](https://news.google.com/rss/articles/CBMiggFBVV95cUxQY3pNQWo3ZzhTajlLMWVwTEcyeXo5YWdtOVEwNy1xNDBrS3ZpN180Mno3YmN4aGIyeC1MNElmY01EQ3h2S0wtS05jeF92QnlzQjlva0RHZVZrdjlJSFpQbjhDX19HRHFycU51TFpsdS1hWldfeHdoMFZGS2lHUmNkSnN3?oc=5) <sub>BASENOR - Tesla Accessories</sub>

</details>

<details><summary><b>NVIDIA</b> (199)</summary>

- 💻 2026-11-19 [NVIDIA/nvidia-linux-utils](https://github.com/NVIDIA/nvidia-linux-utils) <sub>GitHub</sub>
- 💻 2026-11-16 [NVIDIA/scadactl](https://github.com/NVIDIA/scadactl) <sub>GitHub</sub>
- 📰 2026-11-21 [NVIDIA Hotfix Stops Excessive SSD Writes at Idle](https://news.google.com/rss/articles/CBMigAFBVV95cUxOTnRpcjJLemJsY1prRXBxNUp4clFldDc2WUR4RERnWkFHRHRwN0V4TzBGaU1LQVRTYnEzbzhOcFEyMVotWmFuMWJtVnowcHhHTk1BRjVjMGJuNEozRlFUa0x0LTMyNjZMRm0xMjhibGZVbmZOYUh5QnM0MXV6LTdaYw?oc=5) <sub>Wisevoter</sub>
- 📰 2026-11-21 [NVIDIA Releases Hotfix Driver 621.35 to Fix Excessive SSD Writes Caused by Background Process](https://news.google.com/rss/articles/CBMickFVX3lxTE9mcVZCOElhRmFTYU5tSkQtSHRWRVlnbXFuQTE2Y1lscnl3aTF1VmRsUmNSaV9KOUxJdUlEM2FORjluRUpFXy14dmtnN0l2YTJKQ3BodlViYThXRzR1ODdJTlFDRk5QWWxQSWk4alhIVENtdw?oc=5) <sub>TwistedVoxel</sub>
- 📰 2026-11-20 [California attorney general subpoenas Nvidia over chips, former CEO's affair](https://news.google.com/rss/articles/CBMiuAFBVV95cUxOQmZITEdpR3o0QTFWdDNqTFB1bWRnbjR6aUJJRjdzN3dqaU5fZDBReWdHdDJiUVFIeGZnMUZFWG51YVdzZ0tVb2NBZXVvMGR5UUxVVnJZOUdrdkxMQXdQU0N6OHdVMUp4WW5UWFk4ek9yY3FPVjJsV09lbE9RdC16LUtNWUVkMVpheUM0SFZ5UVI5MlptbXZ4U0kyVXZiZlU0REtodlVmRjVsb2RoVUVOREhpb1JsUTJK?oc=5) <sub>Audacy</sub>

</details>

<details><summary><b>Wayve</b> (46)</summary>

- 📰 2026-11-20 [CoreWeave and Humatica: Scaling Proprietary Enterprise AI](https://news.google.com/rss/articles/CBMijAFBVV95cUxNUlZMWTNaYTJnT0RvcFhBWXFRQlg4aVF3WWFNTkRPZVJ3S09zX2p3UzBSTTcwWnJGci1Pb0JHb3ROTG1RY0NRMElaRUI1SG91bXpvdHRrc3ExRktrcllHV2IwbTgwTzBjVmNvR1lNcGdDSlJhOVphTk1YQU0xSlBRYmphZ191U3lZSXZKSA?oc=5) <sub>AI Magazine</sub>
- 📰 2026-11-20 [First Shift: Tesla to sell Cybercabs for private ownership](https://news.google.com/rss/articles/CBMikwFBVV95cUxQcmhja0Z6TGs3XzF1eW9pcUc1Ry0wQU8tVDhWOG9UVWhfZHhRNXJNc3hicjdmQVBiV3JnWGxsVGZwd1hhRXV4Mmkxa09vNDYwb3dOLVhPNnhQMDVEdlFoVDRGV3FxbnhHXzNnRnBIUlB0cEliQmJHeEF2OW9rU1piSmdVWEIzQnBnMFVnMzJFNFlJVlU?oc=5) <sub>Automotive News</sub>
- 📰 2026-11-19 [Qualcomm takes on Wayve, Chinese rivals with new AI driving platform](https://news.google.com/rss/articles/CBMihwFBVV95cUxPSmpFQkxRLWs0ZU16X1hveXRWQlJDbnpiZDZoa2FnVDRVYloySE5qSHpGQUNJb2ZEZjFLcGxrRTViWmhYS3pybUp1SHFuZWU4eWNSX0o0REtSa0NVVDJCaTMxRzlKbGhpN0RNRzVUVFhsMmx1RUk4V1dFYzJoSFhvLUZXMWZFM1k?oc=5) <sub>Automotive News</sub>
- 📰 2026-11-19 [Bolt and Stellantis plan autonomous vehicle trials in Greater Paris from 2028](https://news.google.com/rss/articles/CBMizwFBVV95cUxNVmF4U3dEUHlQTHB6NTdHSVhBT2dwblNQSXhLbnlMQUVCQnFTSVJ0TW9KcTdlTmhLZkdsRDg2TGxBMGVvdkNSamNaV3lmaXdkSXI4UVlyZFd1Z2hYT3gtU3NGVmVXY3N4WHZQMjRxSEM0OENfVndrT1E0Q2pOQ0pfUExTYXdadzlUNFhxaF8tTWdwVmszVm9NM0JlaktadFJPaWZ1eFkzMUVSdXVOSlpPZVhLNG40THc1aTdaaGJ1c0F2R0tnMjBkY25FakJfRzA?oc=5) <sub>Robotics & Automation News</sub>
- 📰 2026-11-19 [Wayve and Stellantis partner to advance autonomous driving in France](https://news.google.com/rss/articles/CBMiwwFBVV95cUxQREhYNVdPX2d4S19MaVFhNWxmWHh0Z2Y3dnVmeWw3aElKcndIekVGYm5CRTlydldmdDA4ZUhCQVlYeGxqeDM4MURQT1BZME5QY0VBTzBhTXVJNEc5bUlpaFZ5OFdqeFZtQUc0YUxNN3BWNWZSMEVzNV9XdkloOU1pdHJZYzM2OGFJY0pvc0cwRXdnblk2T3lVTDlEUEJURFcwY083VnlfU1d6Q2s3VlZ5allzLUFacGtfTC1kMUpacmo4QXM?oc=5) <sub>Robotics & Automation News</sub>

</details>

<details><summary><b>Momenta</b> (106)</summary>

- 📰 2026-11-21 [Momenta获得了全栈ASIL D认证，智驾更安全？](https://news.google.com/rss/articles/CBMiW0FVX3lxTFA2ZEZEZ3gzdlFjdjYyN2VLN01aNXNQSl82aGhseGZDOEJqRkc4VG1sWjNiYUVZTUpna2ltZVh2SV9NTHAyaWVpNUdCNFV5dXBSMFNFa2swVmc5SDg?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-21 [中国Robotaxi出海， 开始接受欧洲乘客检验](https://news.google.com/rss/articles/CBMiUEFVX3lxTE9CZkF5cmJhbkg2SkhFZXRJb0xPdDgydDlTTWJaMWRZR25sWWFVQ1BUYVVlSTVnbDA1emkzU3VzNXp1TUZ6XzQ0VzAybTZ3azBx?oc=5) <sub>盖世汽车</sub>
- 📰 2026-11-21 [【视频】带你看MG 07，845km+Momenta R7激光雷达智驾，15万内超哇塞！](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5jcWVHbGoxQlZtYV9JMi00WC10ajh2Ml95S3BZNWd0NXloMTFLc2RrNmRESkVHMDJ0Tlg2emh5MC1KODM1QTZnbHRjbFBZM3M5UmFNbDEzWWVWSFk?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-20 [从一趟Robotaxi看中国智驾出海，Momenta加快欧洲落地](https://news.google.com/rss/articles/CBMiZkFVX3lxTFBvYnBMd2Uxd1dzLUw1cnFSTzgyMDEwSDRBZnBkMDc2Q3ZYZmQ1Vk43STg0NEM0SGV2d01YV05IU3V0UXN5c1Ryb0ZYazIxeWRLZkthQnkwZ0dIa1VYUjgyYlJYQUhMUQ?oc=5) <sub>每日经济新闻</sub>
- 📰 2026-11-20 [Momenta and Uber Launch Robotaxi Pilot in Germany, Offering Free Rides to Passengers](https://news.google.com/rss/articles/CBMi3gFBVV95cUxQaDU4R0NuMWEydGl0djRJaTluMEJiUlRqTHdCV29YUHhpT1ppTnNoak4yMmpEY2dwblBmaFR1dlVLVHQyZkZrZmlYQXVPWjlDcTB2QWR2VndfRFVtTkZlTmZ6VGdBaDhWakZMOVhKdzBqSXBCYTFxY1VESnNWbTlaT0Z6X0VWQVRSU1Jxc3NWeFRiVDNPYzY1MjgwWDJnVWt6eXdnTnl5SzFrUEZNX21RTlFMNVBJR1lfWHdCTXZ5U19uWWtITVJLVmNfMC02V3VJYXpaV0cxMUhfRHlTZ3c?oc=5) <sub>Gasgoo</sub>

</details>

<details><summary><b>XPeng</b> (197)</summary>

- 📰 2026-11-21 [The XPENG G9L’s First Right-Hand-Drive Price Is In, and Australia’s Next](https://news.google.com/rss/articles/CBMigAFBVV95cUxNR1BpWXNvRVVjY3R0di1pQ3hMNjV5NkJ0Vjktc25Xdy1CT1FOb251bEtNeFZvWFRzUl9mWWxYakZDVjFJeVNTdDdKZ29UUmUxOUVpelZHN0tFT05vSkVia2I5Tk9YN211WEx5ZDl4OWgxR3JFMW0tYUxBWGpHZEk2NA?oc=5) <sub>CarSauce</sub>
- 📰 2026-11-21 [小鹏行业首发VLA人驾版，AI共驾实现自适应减速](https://news.google.com/rss/articles/CBMic0FVX3lxTE1LWkNXTDBQZFc5LVdmNlJYaGIzVi1leFdfbF9HVVR1Q3NMaTZJbnBnX3lMUzJlNnNGSUNOR0VKYWQ2SnFxeWMtaHAzRjd4V0RIbW1ETFNfaEJuRVZMcGZHR0toa3YtR29XTGRrWFlCXy03WDQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-20 [智驾硬件买了却爱自己开？这套VLA 让能耗提升12.4%\|小鹏\|VLA\|图灵AI 共驾\|P7_新浪新闻](https://news.google.com/rss/articles/CBMiY0FVX3lxTFBxWTg3QnFROXVPWGxSbjlpeHpsOXY4aXZXaDJVay1yUDBmMjNra3NFVGV6cWNCYTd6aGU2ZFJLV0xwcGtOZGlsVkZncXVXN0dUT0drOWFjX0dqUk9QcldLTFNCWQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-20 [17万选纯电SUV，702L大后备厢 vs 510L够用吗？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE13c3dHZ1p6bEtHQ1FJcVEwOGxKS051LUtiSW1SaXdZbTdiNkJxZGxablRjSDBVQThPdXloSE0zMl96UkcwQVVYakFhblN4SzJvQWJwMGcyd0N5UlE?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-20 [XPeng Fell 54% While Sales Rose](https://news.google.com/rss/articles/CBMimwFBVV95cUxQRzNkNktCOTNuWERBV0ZGSEVmd2hEdzhhWVZpeC05MkZkeFRzSFlLTS1HM3dJTU5NTlNJMHIyY1dnZXQ3LTFpWnp5SEZPN29LLVZ2eDg2bVpHaTlab0gzY2pYekZxSlo0MFVtVHVDNFFQcGVSRnp6X3lERGJNaGN6UnFlSGVmNzVScDUtbVJrejhrWms0Q2tFOHVsWdIBoAFBVV95cUxOejVfRWRMRW5mUnpMbXNVY1RpV1h5TC1NMU1OcmZzTHdWLWdjckw1dThsb3hzRzlCRHB2MEl6YVhObGJ6M01xcF9pdmo2TUlXYlNuZ0tuNWUzMjE3NllYSGViZW54NmU1MHBnSExMdXZET1JSUzVLUkNlMlVhWlNMaURCYXBZOVAwcXZtaGFyZmx5QVN4NnA2Rnl5ZFFwTEF6?oc=5) <sub>Simply Wall St</sub>

</details>

<details><summary><b>Li Auto</b> (173)</summary>

- 📰 2026-11-21 [LEPAS L8 PHEV launches in Gulf, offering luxury hybrid SUV with advanced tech and long electric range.](https://news.google.com/rss/articles/CBMinwFBVV95cUxObWk1QW9mQjROaWl1UDRtYm5qeUZFSVlyVDFWdDhXbnJtUThwN2pRaF9hejdFN3hWUGRUUURnYnk4VW02cGF4VWFjRGhwRDlZdU1kMVQ2UG55TTBSQ1M5X0RRS0V6NDIteUpILU9mS1ZWY0FyX3pSMFptanNIRWMtWXhLa3JyUEdEcDFfOENZSkRiVWM0NHZmMC1ZQk9IQ1E?oc=5) <sub>Pluang</sub>
- 📰 2026-11-21 [全新理想L6上市 售价24.98万 限时赠2万元配置](https://news.google.com/rss/articles/CBMic0FVX3lxTE1mcXdvUFNmNl9VRzJKWEV4V0VuNFJXSVozLWd0SFBQZFl0V2lmMkZGY3otZXJEbURUMXIyY1dpd19KVk9xQlVIaW1YVk5OT1NsaW9TZzJJYmtCdTJyUEgxaEJGeW02bHdKUncydHFydEtSVVk?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-21 [小米极氪理想拆车，智驾标定与OTA承诺才是软质量](https://news.google.com/rss/articles/CBMia0FVX3lxTE4yeG1BbTRuUUpmajdVYnhNSFNQcDRuM2I4MktaZEJYaVhDRFd3amRfZzJzTUJ4elA4MnJSWVhMSFZJclZXRkZ3MmhZaXBmQ2piOVVKT1hSZVZ4Y2dwNlhUcnhNajJsRDVIVmpJ?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-21 [高配置增程SUV怎么选？奕境X9、问界M8增程版、理想L9、领克900四车横评，入门即超配才是2026年的答案](https://news.google.com/rss/articles/CBMiX0FVX3lxTFB2clZkUThjT2Q5U3ltUk9wZlQ3Rl9KNXZZSWlLRVAzYkZGczBub1kyWXF0dWVucXZMZjRZSjJlMk5MYXBzWTFnQzFDZUdqbWRyYVZSOXdKYTB2bjdyTXk4?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-21 [【视频】理想OTA9.2.0进步大吗？城区实测理想i9 Home \| Xauto智驾榜](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1iZmMzQlc2UWlYV2xSWm5MU2p4b0NQOENTQWdoMGYwSzBFREpoSXpzQ3F5VGR5dWVLQ3pNRXVrU3JSMGJ2SzhoSncta1M5aTc3aWRRNlVfMXlZQ1E?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>NIO</b> (170)</summary>

- 📰 2026-11-21 [享界G9对比蔚来ES8，从硬件与用车成本解析性价比差异](https://news.google.com/rss/articles/CBMickFVX3lxTE9GZ2FQVEZPZTBEVWVOaEdNaVZkYkI5UWgwUEZDZExoTER1cGZja25QUG9jcUhGb3A1cWs3aEZKRVZ5d1NuVFVMSXczdDA0TzNlWkd5eTlwX2hkUEZZTzduUnlIaVptb3dTbUtPN09YZVdLdw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-21 [【视频】蔚来品牌标识发布10周年，奉献ES9地平线鎏金特别版](https://news.google.com/rss/articles/CBMiW0FVX3lxTFByRmNUT1FhZE9MTXNRVWtwUEI4aDd5UHZ5NzBhZFhjaGxUQVVoVDRlYUxJMVM1Sk94TTRMSWxaYjRGSXRSSHBmYU51MzBYbUkzTlB5Y1VqcVlXMEE?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-21 [蔚来ES9地平线鎏金特别版上市24K鎏金车标](https://news.google.com/rss/articles/CBMiTEFVX3lxTFBhTTdRUkhBSlZFcFBqenRsQkc1VEZVNUw2UVRFbkdVNk9DaktyTHFtX1R1djF5djdVSVJpQXdwbVYyNFFvYkxSRWx0eko?oc=5) <sub>www.itsdw.cn</sub>
- 📰 2026-11-20 [Nio Firefly launches new 333-unit special edition to sustain record delivery momentum](https://news.google.com/rss/articles/CBMifkFVX3lxTE5MUlpxZGVkYWVtVXVJeVZJSk9SVms3VWZjcll3MmFud0JrdVBFR3RfcTFOMHlTY3lQckNUYi1lX0Rwd1pKX2gzakdsZGozRkhHY2pXQjZsVzBqdVdnM1hwYTZIbUFsYVpmNUItcXoxWHNMNDM0RngwaUFOU0w3Zw?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-20 [Spy photos show camouflaged prototype of suspected Onvo L70 set to expand SUV lineup](https://news.google.com/rss/articles/CBMiYkFVX3lxTE1IckxVS2FsU0g2enFaSUFRbk9icXFjc2JYNFpQcmZYYVNsdHNlcjRBOTBWMURoWkMyLXp3cFRnemQ4UFVwQWx6UFc3X3VhZzlrR01pcjhIMm5KS0hLYjh4T1Bn?oc=5) <sub>CnEVPost</sub>

</details>

<details><summary><b>Huawei</b> (333)</summary>

- 📰 2026-11-21 [Watch: China's Ghost EV' Tries To Park Itself 800 Times Overnight](https://news.google.com/rss/articles/CBMingFBVV95cUxOeGhKYWdMSE01elRGYzNOMXRHM2xrdzBqNUF0YndxcVFJek9zSE91Tm9DcEFWNVg3eExOU3kwemlJdkZveDFQRHA1LWZwNkREaTl6YUFXR01wbURrTnBwU0FPYjNhWG1YRTREQ29mZXozZ0dIRUxYT3ltdmQyN0JaYldKNFVfV3A4Rmw4QzRRQV9FbWM0OGZqQk1tTUplZw?oc=5) <sub>NDTV</sub>
- 📰 2026-11-21 [China's Stelato V8 Launches From 319,800 Yuan as Premium MPV Segment Sees No Model Top 10,000 Monthly Sales](https://news.google.com/rss/articles/CBMidkFVX3lxTE1wZWhCT0drMVlhTVl6RW51RjZUdUU1VURCTEEzZ2tiYzg0MWduTU9rQ0VBUHBaTHd6akpFMHNrZW5EYlBDcE5fVEZiRXotY050Z1FNV2hlZmc1dk4yVHpsdWp3c0IxaXhGMHhobnd2bV9SOEMyOWc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-21 [Stelato V8 with L3-ready autonomous driving architecture launched in China](https://news.google.com/rss/articles/CBMixgFBVV95cUxPSWFkRDZYdEx4eGVZLVJ4YnZHeVJqSUFIdjFkRk81VkVheWFBcE1USkZaNjdsVndBMzEwbjJQbHhkeVRSV2t5REMtMHEyemo5eDdEQnlmV1ZCdmFHU1JJWDhIQjFhb1cyT0k0MmxOUERVSEUzT0pRRDdaZVJINkZxUktxV21qdVVZZTVtaDRRaUtrN1hpVXVfN1E4YkZuTlJscXJNNGg3LWJURmRhc1RSS0kzdUY2WHdYc1pQclRqX0s3VjVZbnc?oc=5) <sub>The Tech Outlook</sub>
- 📰 2026-11-21 [从15万到50万，华为乾崑智驾SUV怎么挑？四款新款SUV横向盘完，奕境X9把四激光雷达做成了全系标配](https://news.google.com/rss/articles/CBMiX0FVX3lxTE93X2tVNmw1amJMUHBoYnlkejJkaDZMVVJPVnp4NkZzc3ljYndLQUdqQVZNNTIyX25lRFBKcWNsRHYtT2QtR3hfUDY4c2NGTTFzX3pzQ0Z2dUJFMUJoZGMw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-21 [华为乾崑ADS 5 Pro](https://news.google.com/rss/articles/CBMiW0FVX3lxTE04aGg3ZVcwWW1JbmRSRDZ6dC1TekV5SVpTMHlRRjltX3BPNndvNmljanA5Zk5TR1hPWGEtT1FKendsc1o3UUdtX19IRlU0bDRqTnZLcERxYzhYUlk?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Baidu Apollo</b> (56)</summary>

- 📰 2026-11-21 [百度世界2026发布多项AI成果，李彦宏：AI下一幕是“智能组织”](https://news.google.com/rss/articles/CBMidEFVX3lxTFB2QXdyQXJBd0xyTDBIeENlSDVSN0htT1haRWU0NEprc3ZBYlJPTU54ejlFVjBwZUpzc004aGdMYW42NzFrM3V3LVBsX3Z5ZlRXQWNzb0lkd20tdTJuVmR3V2otWHo4NXRrTi1aYVluaXBEVmg1?oc=5) <sub>风闻</sub>
- 📰 2026-11-20 [Google 开放 Genie4世界模型 API，支持实时交互与原生音频生成](https://news.google.com/rss/articles/CBMiTkFVX3lxTE9sLURMU3dDZHJRN0N0U25LV19oWlBvTThkQVI5TzNCVnBHYlFkNUREbzJxYXBnWVV0SHQ2WGRpQUViM0ZKbXpIdUw0Y0dZQQ?oc=5) <sub>AIBase</sub>
- 📰 2026-11-20 [加州禁止Waymo在高速公路无安全员运营，Waymo扩大暂停范围至五个市场](https://news.google.com/rss/articles/CBMiVEFVX3lxTE9Nb2JMa0dKaHBZdHo2QldXczIzeGtoRTVRdnRjQ1FiZmM1Y0RoX3RrYWQ4QUE0TlFRdE1uZnNwbkxYNmIyS05NbDRPeEtIdE1XVkt5Wg?oc=5) <sub>虎嗅网</sub>
- 📰 2026-11-20 [边玩边改的世界：谷歌 Genie 4 向开发者开放，一分钟约 6 美元](https://news.google.com/rss/articles/CBMiTkFVX3lxTE5NYnUzSE5kS20yVDJXRC1iZWEwcnhTaVlfRGt4MEFfOFhUZjJ2YmEtUFFrcElvc3hyVFZtQk1rY1liNFBMSTNQRjBJMWhLQQ?oc=5) <sub>AIBase</sub>
- 📰 2026-11-19 [萝卜快跑落地28城，江铃新能源无人车驶向30国](https://news.google.com/rss/articles/CBMif0FVX3lxTE4zVlo4bjVEYzlyQUt2N1lTNDhDYUphcUJzS1FJcEVhdEJFVEctcmhZNHNJSTJxM3gwQ1k0eFFkWUttRzF2ZWY3WU1CMGJRMDJtNWVXdHRVd3llZ0F1cjdxMHhzUW83SHoxX29uMHlZOUJfTEI4ZHJBN3hTcTZDQlE?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>Pony.ai</b> (140)</summary>

- 📰 2026-11-20 [Pony AI’s robotaxi fares surge nearly 400% but its operating losses barely budge](https://news.google.com/rss/articles/CBMipgFBVV95cUxQejkzT3hlZnI4SG9LdWVCc0FKMF91cW1TWVBTNlJ5enRQOUxMOEFzTUg1STVDRHpOVTBpanlFNHgzd3RzN3ZDLTRaNV83azIxVEZTR09FWGx0OF9rWVR1bFlod050WlRzWTY2TVd4cHRQeGNrVklWcWNtUlV3QlZyYzB4WEZSZGtRd0pvWDlDU2kxTVB4Q3FYN1ZpeXlmeXVWZmRpOUFn?oc=5) <sub>CryptoSlate</sub>
- 📰 2026-11-20 [Pony.ai's Q3 Report: Revenue Surges, Losses Narrow — What Are the Key Takeaways?](https://news.google.com/rss/articles/CBMi0AFBVV95cUxNQlhkdThZM1dJYmkwWGdBYXMxYjNsMUp2ak1xUzZWbkdkaGluR2QzNkFXLVVGTk95NnhMcDlvUmg1RG1xWFg5X2dNbGpKN0dJajdwb0cxZEhydjhDUEFUZEN2c0k2T0VyQnoxc25ONkkwVUdBMk5OeWdvR2dFMWtHNkx2emh5T1JqSF9NQTE1TUczb3EyWG42TGhxYURQX0lnMlZ2ZnE2TEtkeUpTS0tiTTcyaE85alNoTm8xNmNiLXdOaF9WSUE1VFhvTnBVV2l2?oc=5) <sub>Gasgoo</sub>
- 📰 2026-11-20 [Pony AI Hits 2,768 Robotaxis, Outpacing Tesla](https://news.google.com/rss/articles/CBMihgFBVV95cUxQcFdhb2g4WTREUmVwUHNkOGdpS3pEOWxMdlozU1hHdnZGcTN4QmI3M0RMdHdOQWlTT1MwXzhYLUxMSUhNMVBITWlHeHM3Nkl4c1kzVWc5bmtIbzFZbFBldDdQdWh6NnFGcHBNZnU5TVhYdDg1SlpTWG56ZGZKcENQV3dTQXBfQQ?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-20 [Pony AI: Latest Company Developments](https://news.google.com/rss/articles/CBMiuwFBVV95cUxQUEl2OFBteDdSZGFaQUQ5bmpkYWNWVTV5NVV4RFplWjNHZ0twdWY4QlZGM2NFZlJuNUowY19fM013eGZGcmY0ekJkUlhNSWNDUkt6R1A5bUhjTzUwakI2aVpPVUVJRGFQek5HcDExalcyTkQtTEJvLVlYQkJ1TG1vOEFVbC1LY2MtNnBGWE9tcHlzZi1xR1NmQjlEZmpjZWRMeXRUaG16bzBsNGpfR2RER1BJWTZIRWJoMDM0?oc=5) <sub>Kalkine India</sub>
- 📰 2026-11-20 [一年股价跌去80.7%！丰田看中的小马智行，三季度净亏了9.14亿](https://news.google.com/rss/articles/CBMibkFVX3lxTE03SGpVdDFaLXp4VjBqdWo3M2lyU25qUWlwNU83cFk4NkpZZWRiSUdlc2hfbWxYWTB6QnhsTlB0d3Vxa3VBVXNvWjZsSzdHNEFDUzdoVmx4S24tOExEdEV0T0w1Q2Z2dGxUUnN5ZDFR?oc=5) <sub>中华网财经</sub>

</details>

<details><summary><b>WeRide</b> (130)</summary>

- 📰 2026-11-21 [文远知行全球Robotaxi第三季营收首次突破1亿人民币](https://news.google.com/rss/articles/CBMia0FVX3lxTE1ROVRINE9GdV9KSENISmhMUXNkX2hFbGo3QXdKajQ4bHFqaGlUck1FWXBwYmM1azBDQnVRdWd4VGJuZDVXM0tvTjJWa0JBUkNsdXZLSFhEUjQ3MTgxWmtlOFlMMmVKSVRLb3pN?oc=5) <sub>联合早报</sub>
- 📰 2026-11-21 [11万级后驱激光雷达搭载文远知行L4同源辅助驾驶](https://news.google.com/rss/articles/CBMickFVX3lxTFB5ZWRUSmtLTmFFV2pUZEIwaEtfODJ3SEhRWGRHdzJ3ZzE3RWZ1RERhRXBZRkZSOUM0SHZ0RTUtUk9od2pyUXdyMTF4RjQxYUdudFVqem5vaFBUWktzSXVWWnVVMHc1LTM1TXhBN1YtNnk1dw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-21 [单季营收3.2亿元创历史新高、大超市场预期：文远知行增长确定性持续释放](https://news.google.com/rss/articles/CBMiiAFBVV95cUxOVlVCZV8wbEFQNGJQOXZSSXNxeUxlbkFNMHZZUHhEQmZ3WHMwTkZNOGN0U3B3UzNXU3RBd2swVFotdWdIbUFYVGZxVU9QaXNaVV9IZ0ZpMFdmbVVfSEV2aDJTTElhcW1OQWNVOWtBbXFXdmtPSkNuX05PY2JMRlY4VkNwblRPWDll?oc=5) <sub>Sohu</sub>
- 📰 2026-11-20 [LensTalk \| Embodied AI takes on daily tasks in Singapore](https://news.google.com/rss/articles/CBMifEFVX3lxTFBHbzBhNHZCNk9LaGs0cmM1cHhPdWliT0NTTDJuSGhMZGN3QjJjdTk3dzFQWjVKX01QMm5BRkZBNU1KVldyMnNlaUV6TmhCQS1ILVdJZnJSSjhkNlRCYy1zQWR6dFJiaHVxbGJ2Y3hzX1R5NnFrTDF0NUllcFo?oc=5) <sub>Xinhua</sub>
- 📰 2026-11-20 [WeRide revenue up 88% as overseas robotaxi business grows](https://news.google.com/rss/articles/CBMimgFBVV95cUxNRnZCU3JETkFEdnhRNUExY2hmMjVTSEtqLXh5eE15bF9pNGJyX1Q5ZHZZV1VhS3JFWmtuRllCckFnT1dNRllsYkw0MDgtNnh0MXY0ZFFITFR6TkJfUzluOGJRXzRhR3ZjYU9KTTVpM0RYYzU2MHRFaFpycFBIcWlEX044YXRUNmlyd2dFWHEyYU1OdEFtUVM5T2J3?oc=5) <sub>Automotive World</sub>

</details>

<details><summary><b>Horizon Robotics</b> (114)</summary>

- 💻 2026-11-19 [HorizonRobotics/LoFT](https://github.com/HorizonRobotics/LoFT) <sub>GitHub</sub>
- 📰 2026-11-21 [蔚来ES9地平线鎏金特别版上市24K鎏金车标](https://news.google.com/rss/articles/CBMiTEFVX3lxTFBhTTdRUkhBSlZFcFBqenRsQkc1VEZVNUw2UVRFbkdVNk9DaktyTHFtX1R1djF5djdVSVJpQXdwbVYyNFFvYkxSRWx0eko?oc=5) <sub>www.itsdw.cn</sub>
- 📰 2026-11-21 [蔚来ES9地平线鎏金版上市，BaaS方案53万元起售](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9Ic2ZiUHoxaXplYUpuLUV0N0trWU9FRk16bDlMWjhhZVdydjd0V0lDNVBJbXoyMzJGdUtJS01MWmRJa3dGMmpLb2lrbkFnSy1pM21ybjJIVm9CMGc?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-20 [天风证券调研纪要：地平线11 月下旬起密集发布具身模型，非车领域已有批量订单_IPO观察_新股](https://news.google.com/rss/articles/CBMiYkFVX3lxTE9TQ2lYRmljM2ZrQU1YZ3BaZDUzN2o1djFqYXZtbXpWZEo5TEIzd004bnFKa0pxR2ZwNkN2ZXdRZDhBZGJiVllhTzFSRFgwQnVrTEp6Z3E4emt1cVdzeGJyLTBn?oc=5) <sub>证券之星</sub>
- 📰 2026-11-20 [4款方盒子SUV智驾横评：高速NOA、城区NCA逐一对比，旅行者7的油电同智最省心](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBDRGxwVXgwd0I1V3M0RVhmVjFKY0tMalhybldaUThCZGs4ZjFlNlJXNUhxM2dzdm1Wc3d3V2U5a0pydGRyYkJYcVY2Ny1nUGo0djB4SXJhc0hVbGMzQm1r?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (20)</summary>

- 📰 2026-11-21 [【视频】3分钟看懂特斯拉Model Y L值不值得买？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9VQU9UWDByVEt0TnRIcDk0Q2RQTDBzWU9JRTBqMUtKMUgwTGsxNWNTc3k4OV8wQ0hfUkh3R0oxYm51S1ZRSzJLRlR6NTU2XzFhMTVRMG9MNlRCSVk?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-16 [中国智驾出海新突破！元戎启行交付超10万辆](https://news.google.com/rss/articles/CBMiW0FVX3lxTE80eWh5OVZNRlpOY3ZTN1hMeHlsN1NtbldkODZOVTQ5U3hMVXBrOXZ3RnhWUXA5eXdsNTVYbUlDUnNsNEhnX05Jam9VUUhDZkJ5RmtIb3RJX1IxQ0k?oc=5) <sub>车家号</sub>
- 📰 2026-11-16 [又一“国产保时捷”？赛豆ME7实车到店，大过小米YU7配571马力](https://news.google.com/rss/articles/CBMia0FVX3lxTE5fWTNxTkVfa2RHM29CZ3JabmtSbllKTVdGN2x4aVpqS0U0bG81RTFHeDhqNHZhaUg3MGJFVjEzOVU3aDdIMS1zR05mNXZ0blNyZ3cxVWRnVF85bmc3Tl9aenNZSlpDaWRDSV9n?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-16 [AIVA ME7实车到店剑指25万级轿跑SUV市场](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5fM1B6RnpLTlpiVEtIUmJaR0Ffci1BVVpqTzY0ZnBab3JSZ2luNDRWeEhPeHJ6YXlaek9BRDZvdmU0TEw3d2JXTVdMbHgzLXh3TWhLTmpCTDlvdw?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-14 [DeepSeek无人创业](https://news.google.com/rss/articles/CBMiTEFVX3lxTE1QUnM4dm1XbE8tWmIwSE1hN1JMTjZKRklrM3FmbkdNbVd2WllWUWpjQVhYV0xwaHhqUHp4T2ZkMGpHMExqWjFNU1lPYXo?oc=5) <sub>凤凰网科技</sub>

</details>

<details><summary><b>Mobileye</b> (12)</summary>

- 📰 2026-11-19 [Growth in the Adaptive Cruise Control and Blind Spot Detection](https://news.google.com/rss/articles/CBMinwFBVV95cUxPa0x3SFRDX194b3VtTHJnYlJPNEZzRHNpRHd6RS1JOVVkWnBBMnZxQ1AyRjFpUWdVSDBuZHdVdUdFczFGbUVMSFlhdU41UmYwbmhzdFlDaGhvSmptUzNSYzktbGJpRG96ZmZvQ2ZHY3Z3aUt6aWV4WFJzLXctV2k5dFoxVTlta3YzSmNkZGxBRmxYdnlLQ1JKV0RFOWxVcjQ?oc=5) <sub>openPR.com</sub>
- 📰 2026-11-18 [Intel Cuts IT Jobs as Tan's Cost Drive Extends Into Year-End](https://news.google.com/rss/articles/CBMidkFVX3lxTE9XMEIyWkJScF9ld3AzQXYxN0hhaFJQWnJ3czJVOE9FelQtbG12YUdoWkZmZW55cWdQamJlSnRGQTF4bWVDNi0zRFdfZ0hpVkJFNThWdmYtWDk4WGRBY1F5dWFrRklNQjNLUU1UVUQzakRvUFZhYUE?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-16 [When Human Superstars Shine: 9 Unmissable Historical Snippets Between Elon Musk and Jensen Huang](https://news.google.com/rss/articles/CBMiU0FVX3lxTFBjclJYNXBJbVBjYUxUQkJCU2pOcDBpVnZZZ2lqWDhZY3lzYk1udjlFWGxNS3loQjAtUDdKYXJySWZWZTJLQ1I1UGtueDdvd2E2RGdJ?oc=5) <sub>eu.36kr.com</sub>
- 📰 2026-11-14 [May Mobility plans 10,000 ID. Buzz robotaxis on €9 million revenue](https://news.google.com/rss/articles/CBMihwFBVV95cUxQdkgzeUVTSS1wc1czVWhUTllrV1ZaVk1VLUUtUTVhTlFVSnJVSGFvcmtvRC1QZHNnWUxHY1B6c3gtUjZqdzFRSm9CSTNuZENtdFlRZGpoaDZGalJQb2xmZ1UtMGJyX1JObkdfaVF6SThudG9kajdDaW1xZVY4dzFraUF6NXd5RVk?oc=5) <sub>AutoNext.co</sub>
- 📰 2026-11-13 [Automobile manufacturing stocks Q3 recap: Benchmarking Tesla](https://news.google.com/rss/articles/CBMivAFBVV95cUxQemM0Qm9BZXFLb2o3YWdJWkFwb1FLcVdMb3NZNDE2bTB2U0hTb29PbnRiQXhFejA3ZklYUEdTR1lZaGpFT2tjOWJPT0luaXF2aXI2ekRhSlhPQnpQNWxQQUpLdTAyeWxvN2dBV2dNcEhiM0VDOWtwNzNtUHlSVVBmMVR3eDZKTWtXSWRvTUd6V1FhVzRqX0MyMDZjQm4xdjAwRmREZEl1X1V3b25CVk9MSUF6Q1draU9nZU1peQ?oc=5) <sub>TradingView</sub>

</details>

<details><summary><b>Aurora</b> (36)</summary>

- 📰 2026-11-20 [AUR Investors: BFA Law Notifies Aurora Investors with Losses of its Ongoing Securities Fraud Investigation](https://news.google.com/rss/articles/CBMiiAJBVV95cUxQVFAwZ0VhZEh6UWFhWXV0RXdxNk1GV3V1ZEpGeUh4cG5tc2Z6aWxVM0hvMUFtUlhTXzdkTENzU3U0S2ZsTC1OZmVlVDNXdS11WWF0VzJUeFBZcnR6NmYzd1JNZ25HLWo5TE1yNmd5TXo4NFlxRTRFSFdSQW1Ka0h3b0JZd2h1LUY2LUxwbWtXX0U2NFh5QmxPNzBDOHIzRG5yQ3J4cVl5T1JxV05SaG5qYWZxekpYbVd0Mk1GdHpmREplRlNpVE5Eb0VpUnQ2b05TdXhLdjhKeEh1Z214VWN6Nmd3WHRFd1lyYVFhQ0ZicXYzdVY0b3owNmRpTHlycHlLU1ZGRl9UcUM?oc=5) <sub>GlobeNewswire</sub>
- 📰 2026-11-20 [AUR Investigation Reminder: Kessler Topaz Meltzer & Check,](https://news.google.com/rss/articles/CBMiowJBVV95cUxOazBaMjVSWHZESFowVURkVVg1NURsOVhELWtUYjlWM0ZMZGIxNVNXeUtsMk5USFFQemRXcUdObEdUQjBUTjhwNnJvZVNzNmRERHRsOFViVFJ5NGtNdnVvLWF4emk1MXJyZ3F1LUFqOWk2d2pjN3JlOWVQdGdoWFhUM2ZOQ2xja3d3d19rZFZGdHd2TWZpQngxUTYta2FJVWo0RlBuYjFOUXplSGpqNkxEcjZyRlFZNmMtWDNreHF1d2ZMb0xxNGJlT2lDcVFnMHg3Y1Izb2hNcVh0NFRmYTBIcUt2Z08zWWdkTlJwSlpnTHR2SEJDdWNUeFUwY0RGUWw0c1E4aVVVdkowUjRVektKT3NPMTc5Y2pRRkhXdUdLbXBNZG8?oc=5) <sub>GlobeNewswire</sub>
- 📰 2026-11-19 [Can Humanoid Robots Earn Their Keep on the Factory Floor?](https://news.google.com/rss/articles/CBMixAFBVV95cUxPMHZxYlNrWkdBWDBjSlJKR3pHeGltUUk2R0loMjdQMENnSFFSZG5TZ1NuaExZcXA2c2ZrSXNaN2hIQ0hnUEwtSWhudU56MTdYdlhnTmZvSXNiLUhIckR1T0xRRzRBb3RSSm5sQzVHRk9YMm9yaEUtVVdQMEVhWGJrR2JEVHVNeUxIS0pORHM2bFJDcDdQV0Rqdm1Pb1NUTzRtLWo2cHdIakcxakxmeEhycW00WEdHZ2pBSU9OTGQ3Q1VISEpp?oc=5) <sub>SupplyChainBrain</sub>
- 📰 2026-11-19 [California to Waymo: Get off our freeways](https://news.google.com/rss/articles/CBMickFVX3lxTE9wblcxcTBFUTZ3RzdfZ2ZzalBxM2IzODVGa3RMZjhXcWRDblhyWk5IUzVBZTltRW1aY0U1UDZma0tGZUNKUG8ySTFzc1N2Vzlmclk4a3RpaXJOOXBjNV9GRmF2SWZpV0U5QjJSLXI0T1BQUQ?oc=5) <sub>Land Line Media</sub>
- 📰 2026-11-19 [Autonomous Driving Nears Its ‘ChatGPT Moment,’ T. Rowe Says](https://news.google.com/rss/articles/CBMikAFBVV95cUxQWmh0UEN2aHUxWE5XdW9ic055c3M0ZW5MMEpDQWprTXdxSldKZ2dUN1RZYU9BWGlQYl9RdHppQ29QY0JmOWNJX1dnRTUxM0s0QmpVYnhGMVRBZlQtMFhPa1B1TkF1ZE9jMXRlUGlYRlRqZTZPQUREZzRqeHJ3VW1USlNzbVZ6a2Z4RWtwVU5mMmc?oc=5) <sub>ETF Database</sub>

</details>

<details><summary><b>Zoox</b> (107)</summary>

- 📰 2026-11-21 [Waymo announces two robotaxi recalls as closed-lane software fix remains unfinished](https://news.google.com/rss/articles/CBMiwgFBVV95cUxNXzk3UHRGSjRZdU15TC1mNm9NLWxxNVg4LWFtZUdReTlENWszWmxCLTFEMzd1Z29RNkpEcFprd3NjTTROUkhPSkhsdkhCWEQ5azJVakdxeGhiTUNxalVTTnhZM1ZyallJMEZ1akdYZ0FFVDFQUWl3a0FSMWx0czV4cGg5TnFUREgyaG9BX0FybTRWY2lfaE1GRlVibVRUNUZ3RHJVUC1jbTdWWDdhZVY1dUlfWGpDMVJqYjJKaENENVZZQQ?oc=5) <sub>Business Upturn</sub>
- 📰 2026-11-20 [Where to see F1 cars free in Las Vegas](https://news.google.com/rss/articles/CBMifEFVX3lxTE5rRVNoemlmQWJJMDZfN21ZYndpZENfNHNHbUE2Q2RuaVdCWThIbnMyZUlFTmdaZkhPdld6VGVzeUtzTlF0c2l5elZqTktkb1FJeGpFX2VNalRidzJfWjM4X2FaQ1B1YVY3SzRnSm0yc1g2c25HelNZMi1fMUU?oc=5) <sub>streamlinefeed.co.ke</sub>
- 📰 2026-11-20 [Geotab Helps Nurture Group Reduce Idling Events per Vehicle by 27% across Its UK Fleet](https://news.google.com/rss/articles/CBMiuwFBVV95cUxNcUUzYlUtbTJfZ3VpZ01vZ05pOU9IdlgwU1VGejQyTWZZZDloYjlqTExHMEVBNS1hRGtQbGgzX2ZpS0dFdWtTLUgtUnUzTW1jeFpwNHhmZEc1a2dnTzBKTG8yLURUaHUyOEtqM3o3N0UtMjkxVlF6VDNVRU5PZzNYcWRFZlNRSWhoZ2ppZ0JXUFlQWmdvUlRLRGxjWmpRZWFHN1FDdFdzRHZvTFpPaG1RUFFMS25lYkNtdkV3?oc=5) <sub>Future Transport-News</sub>
- 📰 2026-11-19 [Einride Says Contracted Revenue Grew 76% to $167 Million](https://news.google.com/rss/articles/CBMia0FVX3lxTE1DQVhjQk5KSHZLNmdyRDJJNG9QejE3Y0Z5Nlppazk3UzVGd2hsSmpLSnI1N3NCYTAtRTdHZi1SS3FKam1JQ3NPTlVGZFJ5RWFBNU9CVjhrQXAyU3pRSEFkQkRaRjZvd0ZwZF9V?oc=5) <sub>EVXL.co</sub>
- 📰 2026-11-19 [Amazon Zoox enters Uber platform: driverless rides in Las Vegas](https://news.google.com/rss/articles/CBMijgFBVV95cUxNUHh1RnNsb2dZcElfYkxQV3hybk50dmNHSWNGZ0hzLUlzS3pZVzBkellCTnM1bHZ4Q05VSURzZ0dYY1RPXzV5SFBpS2xYZFpNVzBYU041Ny1IWGRpMGJJM2tyOUQzX25lb2ZmSWlOOGVPcFNNd1dHNC1tVWNrN205Z1p6TlNERHZxV3FXd21R?oc=5) <sub>hi-Tech.ua</sub>

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
