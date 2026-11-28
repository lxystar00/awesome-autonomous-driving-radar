# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-11-28 · 1,318 papers tracked · 50 curated.

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
- [End-to-End Driving & Planning](#end-to-end-driving--planning) (14)
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
| [AutoVLA-D: Learn a Trajectory-Geometric Condition from Reasoning for Autonomous Driving VLA](https://arxiv.org/abs/2611.12382)<br><sub>Yuguang Yang, Zhewen Tan, Canyu Chen et al.</sub> | NeurIPS 2026<br>2026-11<br>📑 1 | [⭐ 46](https://github.com/ShivaTeam/AutoVLA-D) | Autoregressive VLA planning usually predicts continuous trajectories as the final output, but driving instructions often describe actions rather than ego states, which weakens direct conditioning on the final continuous … |
| [Scene-Adaptive VLA: Efficient Autonomous Driving via Dynamic Layer Routing](https://arxiv.org/abs/2610.24590)<br><sub>Yujia Yang, Quan Yuan, Jiawei Fan et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 5](https://github.com/yang-luvu/Scene-Adaptive-VLA) | Vision-Language-Action (VLA) models offer a promising paradigm for autonomous driving |
| [Locating and Repairing Domain Shift in VLM Trajectory Planning](https://arxiv.org/abs/2611.10720)<br><sub>Zhihong Cui, Hengyu Liu, Michael Alexander Riegler et al.</sub> | NeurIPS 2026<br>2026-11 | [⭐ 0](https://github.com/ZhihongCui/MoLaRx) | Vision-Language Models (VLMs) are increasingly adopted as end-to-end driving planners, yet they suffer from cross-city domain shift |
| [CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving](https://arxiv.org/abs/2607.04179)<br><sub>Zhaohong Liu, Hao Ye, Xianlin Zhang et al.</sub> | ECCV 2026<br>2026-07<br>📑 3 | [⭐ 1](https://github.com/MICLAB-BUPT/CritiqueDriveVLM) | End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving |
| [PixelPilot: Scalable Vision-Language-Action Models for End-to-End Autonomous Driving](https://arxiv.org/abs/2607.04637)<br><sub>Pin Tang, Guoqing Wang, Xiangxuan Ren et al.</sub> | ECCV 2026<br>2026-07<br>📑 1 | [⭐ 3](https://github.com/VISION-SJTU/PixelPilot) | Vision-Language-Action Models (VLAs), which leverage the advanced reasoning capabilities of Vision-Language Models (VLMs), show promising generalization in complex autonomous driving scenarios |
| [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)<br><sub>Nan Yang, Zhanwen Liu, Linfeng Zhang et al.</sub> | ECCV 2026<br>2026-06<br>📑 1 | [⭐ 11](https://github.com/Zizzzzzzz/MVPruner) | Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings |
| [Teaching VLMs What to Say, Not How to Reason: Rethinking Counterfactual Reasoning in Autonomous Driving](https://arxiv.org/abs/2611.24376)<br><sub>Hayeon Oh, Donghwan Lee</sub> | NeurIPS 2026<br>2026-11 | [⭐ 3](https://github.com/OPhD-hahao/Rethink-CF) | End-to-end autonomous driving systems have been shown to suffer from shortcut learning and causal confusion, limiting their ability to generalize robustly under distribution shift |
| [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)<br><sub>Yuan Gao, Wenting Miao, Mattia Piccinini et al.</sub> | IROS<br>2026-07<br>📑 2 | [⭐ 34](https://github.com/TUM-AVS/Chat2scenic) | Validating autonomous driving systems requires diverse, regulation-compliant test scenarios |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 28 | [⭐ 572](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
| [GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives](https://arxiv.org/abs/2609.39601)<br><sub>Qize Yu, Lianrui Fan, Boyu Chen et al.</sub> | arXiv<br>2026-09<br>📑 5 | [⭐ 448](https://github.com/groundingpi/GroundingPI) | Precise grounding matters |
| [CARLA-GS: Decoupling Representation, Reasoning, and Physics Simulation for Autonomous Driving Corner-Case Synthesis](https://arxiv.org/abs/2607.07601)<br><sub>Kaicong Huang, Meng Ma, Ruimin Ke</sub> | IROS 2026<br>2026-07<br>📑 2 | [⭐ 3](https://github.com/ccoopq/CARLA-GS) | Safety evaluation for autonomous driving is dominated by rare, safety-critical interactions, motivating simulators that can deliberately synthesize corner cases with photorealistic observations |
| [GRAVA: Grounded Reasoning-to-Action Representation and Learning for Autonomous Driving](https://arxiv.org/abs/2609.15169)<br><sub>Xiao Liu, Haoyu Li, Jianghao Leng et al.</sub> | arXiv<br>2026-09 | [⭐ 487](https://github.com/AhernResearch/grava) | Driving vision-language-action (VLA) models increasingly reason before acting, but their intermediate reasoning is often weakly grounded in physical scene evidence and loosely connected to executable behavior |

## World Models & Generative Simulation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Orbis 2: A Hierarchical World Model for Driving](https://arxiv.org/abs/2607.15898)<br><sub>Sudhanshu Mittal, Arian Mousakhan, Silvio Galesso et al.</sub> | NeurIPS 2026<br>2026-07<br>📑 3 | [⭐ 32](https://github.com/lmb-freiburg/orbis2) | Current world models operate at a single level of abstraction, with most prioritizing perceptual fidelity while lacking the spatial reasoning and semantic understanding required for real-world downstream tasks |
| [FrozenDrive: Zero-Shot Text-Guided Driving Scene Generation and Data Augmentation with Parameter-Free Frozen Diffusion Model](https://arxiv.org/abs/2606.20110)<br><sub>Yuhwan Jeong, Hyeonseong Kim, Daehyun We et al.</sub> | ECCV 2026<br>2026-06<br>📑 1 | [⭐ 10](https://github.com/daehyunwe/FrozenDrive) | Synthetic data for autonomous driving is surging, powered by diffusion models that promise scalable scene generation |
| [MESSENGER: Memory-Enhanced Sequential Scene Flow Estimation via Autoregressive Next-Frame Forecasting](https://arxiv.org/abs/2610.10759)<br><sub>Jiuming Liu, Jianing Li, Mengmeng Liu et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 0](https://github.com/liujiuming123/Messenger) | Scene flow can capture low-level 3D motion displacements in dynamic scenarios |
| [ASTAD: Asymmetric Style Transfer for Synthetic-to-Real Adaptation in Autonomous Driving](https://arxiv.org/abs/2606.29286)<br><sub>Dingyi Yao, Xinqi Zhang, Lihui Peng et al.</sub> | ECCV 2026<br>2026-06<br>📑 1 | [⭐ 2](https://github.com/Dingyi-Yao/ASTAD) | Synthetic data mitigates the data scarcity problem in autonomous driving perception |
| [Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends](https://arxiv.org/abs/2606.01164)<br><sub>Jiuming Liu, Chaojun Ni, Mengmeng Liu et al.</sub> | arXiv<br>2026-06<br>📑 10 | [⭐ 253](https://github.com/liujiuming123/Awesome-Interactive-World-Model) | With rapid development of large language models and diffusion-based content generation, world modeling has attracted increasing research attention, benefiting various downstream domains such as game engines, embodied AI,… |

## End-to-End Driving & Planning

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [UNIVERSE: Unified Video Action Models for Autonomous Driving with Flexible Mask-Modulated Modality Generation](https://arxiv.org/abs/2607.05133)<br><sub>Mengmeng Liu, Diankun Zhang, Jiuming Liu et al.</sub> | NeurIPS 2026<br>2026-07<br>📑 18 | [⭐ 6](https://github.com/xiaomi-mlab/UNIVERSE) | World Action Models (WAMs) can improve action generalization in autonomous driving by learning scene dynamics through dense future-video supervision |
| [MOJITO: Modal Joint Learning for Unified End-to-End Autonomous Driving](https://arxiv.org/abs/2607.23511)<br><sub>Zhijing Cheng, Xuancheng Zhang, Donglin Di et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 31](https://github.com/mumucc01/MOJITO) | End-to-end autonomous driving systems commonly follow a cascaded two-stage pipeline where a perception stage compresses multi-modal sensor inputs into a compact context and a downstream planner predicts trajectories cond… |
| [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](https://arxiv.org/abs/2609.26792)<br><sub>Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.</sub> | CoRL 2026<br>2026-09<br>📑 1 | [⭐ 16](https://github.com/VAIL-UCLA/DreamStream) | Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions |
| [DriveMLP: When Training Strategy Outperforms Model Complexity in Autonomous Driving](https://arxiv.org/abs/2610.29676)<br><sub>Alessandro Canevaro, Julian Schmidt, Hang Yu et al.</sub> | CoRL<br>2026-10 | [⭐ 6](https://github.com/alessandro-canevaro/DriveMLP) | Learning motion planning policies that remain reliable under closed-loop execution is a central challenge in Autonomous Driving (AD) |
| [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)<br><sub>Shen Zheng, Anurag Ghosh, Gaurav Parmar et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 32](https://github.com/ShenZheng2000/WarpI2I) | Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs) |
| [G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance](https://arxiv.org/abs/2606.26017)<br><sub>Hang Yu, Ye Jin, Alessandro Canevaro et al.</sub> | IROS 2026<br>2026-06<br>📑 7 | [⭐ 7](https://github.com/HangYuu/G2DP) | In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors |
| [DriveZero: End-to-End Driving Beyond Human Demonstrations](https://arxiv.org/abs/2609.06055)<br><sub>Hao He, Chengcheng Hu, Zirun Su et al.</sub> | arXiv<br>2026-09<br>📑 12 | [⭐ 151](https://github.com/XiaomiAutoL3/DriveZero) | Most end-to-end autonomous-driving systems learn by imitating human driving logs, leaving their learned behavior constrained by the quality and behavioral coverage of the recorded trajectories |
| [SimWAM: A Simple World Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.07468)<br><sub>Zongchuang Zhao, Xin Zhou, Tianyang Xu et al.</sub> | arXiv<br>2026-08<br>📑 27 | [⭐ 216](https://github.com/H-EmbodVis/SimWAM) | In autonomous driving, World-Action Models (WAMs) have improved end-to-end planning by transferring video dynamics priors to action prediction, but many still couple planning with future-video generation at inference, in… |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 25 | [⭐ 372](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
| [Latent-Centroid Steering: Single-Pass Classifier-Free Guidance for Command-Aligned Autonomous Driving](https://arxiv.org/abs/2608.00237)<br><sub>Meibo Hu, Jiamian Wang, Pichao Wang et al.</sub> | IROS 2026<br>2026-08<br>📑 1 | [⭐ 2](https://github.com/codingmlinprocess/LCS) | Vision-language models (VLMs) have recently emerged as a promising paradigm for end-to-end autonomous driving, enabling agents to map multimodal inputs and high-level navigation instructions directly to executable trajec… |
| [STAGE: STyle-controllable Action GEneration for personalized autonomous driving](https://arxiv.org/abs/2607.29517)<br><sub>Zihao Liu, Xing Liu, Yizhai Zhang et al.</sub> | RA-L<br>2026-07<br>📑 1 | [⭐ 5](https://github.com/CarlDegio/STAGE) | Driving style refers to the behavioral preferences that drivers maintain during driving, shaped by their diverse experiences, habits, and needs, and is typically reflected in varying levels of aggressiveness |
| [WA-JEPA: Rethinking the Video JEPA Paradigm for World-Action Modeling in Autonomous Driving](https://arxiv.org/abs/2608.20974)<br><sub>Xinlin Wang, Yujiao Xiang, Yuheng Zhou et al.</sub> | arXiv<br>2026-08<br>📑 13 | [⭐ 91](https://github.com/AFARI-Research/WA-JEPA) | Video Joint Embedding Predictive Architecture (V-JEPA) learns powerful spatiotemporal representations from video through self-supervised latent feature prediction |
| [A Survey on End-to-End Autonomous Driving Training from the Perspectives of Data, Strategy, and Platform](https://arxiv.org/abs/2610.00926)<br><sub>Chengkai Xu, Yiming Cui, Jiaqi Liu et al.</sub> | arXiv<br>2026-10<br>📑 7 | [⭐ 112](https://github.com/Jiaaqiliu/Awesome-Training-Ecosystem-for-E2E-AD) | Autonomous driving is a cornerstone technology for the future of intelligent transportation, where end-to-end learning has emerged as a transformative paradigm that directly maps multimodal sensory inputs to driving acti… |
| [AutoE2E: Don't speak - Language free end-to-end autonomy for L2++ ADAS and L4 Robotaxis](https://arxiv.org/abs/2611.22374)<br><sub>Muhammad Zain Khawaja, Zaynab El Mawas, Ryota Yamada et al.</sub> | arXiv<br>2026-11 | [⭐ 238](https://github.com/autowarefoundation/auto_e2e) | AutoE2E is an open-source end-to-end driving model developed by the Autoware Foundation Robotaxi Working Group |

## 3DGS / NeRF Reconstruction & Sensor Sim

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [MCSplat: Multi-View Photometric and Geometric Consistent Feed-Forward Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2610.25345)<br><sub>Yifei Wang, Wei Tian, Wenhua Bao et al.</sub> | NeurIPS 2026<br>2026-10<br>📑 1 | [⭐ 15](https://github.com/yfwang0824/MCSplat) | Driving-scene reconstruction via feed-forward Gaussian splatting from sparse multi-view images remains challenging due to two factors |
| [DriveWeaver: Point-Conditioned Video Inpainting for Controllable Vehicle Insertion in Autonomous Driving Simulation](https://arxiv.org/abs/2606.31918)<br><sub>Junzhe Jiang, Zipei Ma, Zijie Pan et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 18](https://github.com/LogosIntelligenceLab/DriveWeaver) | A pivotal step in autonomous driving simulation involves inserting foreground vehicles with predefined trajectories into simulated scenes |
| [Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796)<br><sub>Leshu Li, Jie Peng, Yang Zhao</sub> | ICRA<br>2026-06 | [⭐ 16](https://github.com/UMN-ZhaoLab/Pocket-SLAM) | 3D Gaussian Splatting (3DGS) has garnered significant attention in Simultaneous Localization and Mapping (SLAM) due to its advances in capturing fine-grained geometry features and synthesizing novel views |
| [NIDAR: NIR-Guided Intrinsic Decomposition for Scalable Scene-Agnostic LiDAR Intensity Reconstruction](https://arxiv.org/abs/2609.36878)<br><sub>Junjie Zhang, Jie Yin, Kefei Qian et al.</sub> | IROS 2026<br>2026-09 | [⭐ 25](https://github.com/Zjj587/NIDAR) | LiDAR return intensity provides complementary surface-response cues for robotic perception and state estimation, yet many simulation pipelines omit it or reproduce it using reconstruction methods that require real intens… |
| [MM-TRELLIS: Point-Cloud Guided Multi-Modal 3D Vehicle Generation in Autonomous Driving](https://arxiv.org/abs/2606.24301)<br><sub>Hongli Xiao, Youjian Zhang, Yucai Bai et al.</sub> | ICRA 2026<br>2026-06 | [⭐ 10](https://github.com/HongliXiao/MM-TRELLIS) | Recovering realistic 3D vehicle models from autonomous driving scenes is crucial for synthesizing training data and building simulation environment |

## Perception: BEV, Occupancy, 3D Detection, Mapping

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Horizon3D: Sparse Radar-Camera Fusion for Long-Range 3D Perception in Autonomous Driving](https://arxiv.org/abs/2606.31096)<br><sub>Geonho Bang, Geunju Baek, Dongyoung Lee et al.</sub> | ECCV 2026<br>2026-06<br>📑 3 | [⭐ 26](https://github.com/geonhobang/Horizon3D) | Long-range 3D object detection is critical for safe autonomous driving at highway speeds, yet existing radar-camera fusion methods remain limited at extended ranges |
| [DRS-VPT: Directly Relocalizing in a Scan with Vision Point Transformers](https://arxiv.org/abs/2609.12557)<br><sub>Lanke Frank Tarimo Fu, Maurice Fallon</sub> | ECCV 2026<br>2026-09 | [⭐ 29](https://github.com/ori-drs/drs-vpt) | We present DRS-VPT, a feed-forward transformer architecture for foundational image-to-scan registration |
| [Explainability-Aware Frustum Attack: Exposing Structural Vulnerabilities in LiDAR-Based 3D Object Detectors](https://arxiv.org/abs/2606.29963)<br><sub>Chengzeng You, Binbin Xu, Soteris Demetriou</sub> | ECCV<br>2026-06 | [⭐ 2](https://github.com/SecMindLab/Saliency_LiDAR) | The structural vulnerabilities of point cloud-based 3D object detectors remain poorly understood |
| [PointLAM: Local Attentive Mamba for Efficient Point-based 3D Object Detection](https://arxiv.org/abs/2609.21780)<br><sub>Xuanming Shang, Weijia Zhang, Chao Ma</sub> | ECCV 2026<br>2026-09 | [⭐ 6](https://github.com/PointLAM/PointLAM) | 3D object detection from LiDAR point clouds faces a fundamental dilemma: voxel-based methods achieve efficiency at the cost of geometric quantization, while point-based methods preserve fidelity but suffer from prohibiti… |
| [PriorMaskMap: Robust Online Vectorized Map Construction with Biased Priors](https://arxiv.org/abs/2610.39283)<br><sub>Haoming Xu, Wei Li, Yu Hu</sub> | ECCV 2026<br>2026-10 | [⭐ 1](https://github.com/healenrens/PriorMaskMap) | Online vectorized map construction provides autonomous vehicles with essential, real-time semantic and geometric scene understanding |
| [Vernata: Self-Supervised Learning of LiDAR Point Representations](https://arxiv.org/abs/2608.06919)<br><sub>Oliver Lemke, Alexander Liniger, Abel Gawel et al.</sub> | IROS 2026<br>2026-08 | [⭐ 22](https://github.com/rai-opensource/vernata) | LiDAR serves as a primary sensing modality for robots operating in outdoor environments |
| [Towards Compact Autonomous Driving Perception with Balanced Learning and Multi-sensor Fusion](https://arxiv.org/abs/2606.02979)<br><sub>Oskar Natan, Jun Miura</sub> | arXiv<br>2026-06<br>📑 47 | [⭐ 9](https://github.com/oskarnatan/compact-perception) | We present a novel compact deep multi-task learning model to handle various autonomous driving perception tasks in one forward pass |

## Motion Prediction & Behavior Modeling

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [MolmoMotion: Forecasting Point Trajectories in 3D with Language Instruction](https://arxiv.org/abs/2606.18558)<br><sub>Jianing Zhang, Chenhao Zheng, Yajun Yang et al.</sub> | arXiv<br>2026-06<br>📑 23 | [⭐ 154](https://github.com/allenai/molmo-motion) | Motion forecasting is central to visual intelligence: agents must anticipate how objects will move in order to plan actions, reason about physical interactions, and synthesize realistic futures |
| [Flow-ERD: Agent-type Aware Flow Matching With Entropy-Regularized Distillation for Diverse Traffic Simulation](https://arxiv.org/abs/2607.06957)<br><sub>Seulbin Hwang, Kiyoung Om, Dae Jung Kim et al.</sub> | RA-L<br>2026-07 | [⭐ 0](https://github.com/seulbinHwang/flow-erd-project-page) | Realistic and diverse traffic simulation is essential to autonomous driving development |

## Datasets & Benchmarks

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [The Road Ahead in Autonomous Driving: The KITScenes Multimodal Dataset](https://arxiv.org/abs/2606.02956)<br><sub>Richard Schwarzkopf, Fabian Immel, Alexander Blumberg et al.</sub> | NeurIPS 2026<br>2026-06<br>📑 6 | [⭐ 30](https://github.com/KIT-MRT/kitscenes) | Existing autonomous driving datasets have enabled major progress, but fall short in sensor fidelity, map completeness, or geographic diversity |

## Safety, Robustness & Evaluation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [CCFM: Collision-Constrained Flow Matching for Safety-Critical Scenario Generation](https://arxiv.org/abs/2607.04451)<br><sub>Ke Li, Kaidi Liang, Yuxin Ding et al.</sub> | ECCV 2026<br>2026-07<br>📑 1 | [⭐ 3](https://github.com/KELISBU/CCFM) | Evaluation of autonomous vehicle (AV) planners in safety-critical closed-loop simulation is essential for real-world deployment |
| [CADET: A Modular Platform for Evaluating Distributed Cooperative Autonomy in Connected Autonomous Vehicles](https://arxiv.org/abs/2606.04072)<br><sub>Pragya Sharma, Brian Wang, Mani Srivastava</sub> | ICRA 2026<br>2026-06<br>📑 1 | [⭐ 0](https://github.com/nesl/cadet) | Deep learning models are increasingly central to autonomous vehicle (AV) pipelines, yet their integration has traditionally followed a monolithic design where perception, planning, and control execute on a single onboard… |

## 🏢 Industry Tracker

Latest 14 days of news, official blog posts and new open-source repos from tracked companies. Full daily feed in [`daily/`](daily/).

<details><summary><b>Waymo</b> (249)</summary>

- 📰 2026-11-28 [A Denver man is trapping and egging Waymo’s self-driving cars, police say](https://news.google.com/rss/articles/CBMiuwFBVV95cUxPbGtyN2RyS2d6S3JSMDgzSFdxMFhaWEFpajNDMVRGZHV3Qkk3YTY2dldYS3pRakEtUGdCU3VWZlJVMi1ra2pqVlFCaUJuR202SHNRZmlETWhzYk50b0g2U1h1VGgxajR3WHNQYjF4eHVFaEEzUjU3d0U1dlBoajVoOHJaNlhlRGpSYU1jZnNnQ3ROWVNYQ1ZhZUxvcWxGUTd5QVQ1VzF6ZkdQZXZTYlpHcjQ3N2lkcVlFaWU4?oc=5) <sub>The Washington Post</sub>
- 📰 2026-11-28 [Waymo on the streets of Baltimore](https://news.google.com/rss/articles/CBMidkFVX3lxTE9HRW1tWnlDbEUzM2RhT2Vta2RiQTU3Zm9Jak00NFFDVGlUd1kxRzdpRG1fX1A5TkpCTy1IYTJlWFhWZ0I5ZXhSQi1pSmh0Z3JYNnEtT0gzZTg2VmNCZWJHb3c1UV9vdWNYRnBtRmtjMTlZaWFLMnc?oc=5) <sub>The Maryland Wire</sub>
- 📰 2026-11-28 [Robotaxi Market on the Verge of Taking Off... Which Korean Automakers Stand to Benefit? [Weekend Money]](https://news.google.com/rss/articles/CBMie0FVX3lxTE9WdExydXRKUXdVXzAwSXdjRTRVX3RDOGM1VFd4MmNRaUNBaFhxVWlnNUNxaTdWRDVYZnd1UzlEbUlKVVlydWlZeFgtNjlPdFF4S0I5aWI5SHBLMEZvejRid0I3OTVrRGFnRm1BLTlTTy1wcDUxRHpnN1RGRQ?oc=5) <sub>아시아경제</sub>
- 📰 2026-11-27 [Waymo Robotaxi Attacked: 30+ Eggs Hit Car in Denver](https://news.google.com/rss/articles/CBMikgFBVV95cUxPT2NFLXhRMHRiMGNVNUlMbEpwcUpJLUpObEFzRDdWbjUtUGc1R3kwX19aaTdEME5pRGg5OVRNaGx4UldOUjQ1Q2poQm15eGRGMy1qc3pHb3AwMlAzTHBXbnd6a2c5dkpfbTZKWml0a1o0akEtUEM2QzRzeGRlb0NoSXloRlR0T3BsWEZRYl9IendrZw?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-27 [Texas Autonomous Vehicle Law: 2 Bills, No Crash Reports](https://news.google.com/rss/articles/CBMimAFBVV95cUxQZFNjVUpUWFNyVlFCVnUzMVdvMTlMaDFKbEdiV29rbGZJcnFqV284N1ZIQ2laaTR4ZERUU3habjdmM1JQUGE0eklRWkxQVDFhSzZ4OVd1WG5udzM4UENGUjNpTXpyLXdIckVXRmZtckhmaVVDeVF3eS1IaWhwOFZFVTZrcDV5Qkt0UTQyeXNfZjZkRlhQUHM2TA?oc=5) <sub>shattered.io</sub>

</details>

<details><summary><b>Tesla</b> (393)</summary>

- 📰 2026-11-28 [Tesla FSD V15: Vegas Night Clip Unverified, $99 Plan](https://news.google.com/rss/articles/CBMilwFBVV95cUxPVnZReG45cUhmMmNtVlVxQnk0MlRjZ1hBcXNuTHJtZUVlTDNWSG9Tdk5uMWFtUzJYM2NVSVFTZGFianRzUVQ3TXFXRlRTdU5DVUZwNmpzYm9YelZQYU9IazhZWFdHR2pFd1piVmttTGRBYkJyWUxzdDZOZEFkVEtTQTlPT1FoRmctYnMzMk5WYUxwbk4zakFV?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-28 [Zero To Sixty: Tesla Cybercab Fleet Tops 1,000 In Texas, Lucid Starts Fully Driverless Tests And Chinese EV Maker Posts Stronger Margins](https://news.google.com/rss/articles/CBMinAFBVV95cUxNdTFrUm1GQVVSaC1KN2hoaS02bk95MDBBcnBTQnRpQmJJRGt2YVdrYzI4Q0J1QVQ5NmpVVFdKUWVPaWpFTm1BeEVuNkFnTVFZN0lVdGVTRTVoaHlmU21oelJkcUt6elpmcktKMV85T1RaRWllWVpRR0lEN0xWNFhCVlFadkp3eUVvNG1WU1VUaEtZamx4STJyckc3Rnk?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-11-28 [🇺🇲 "You see EVERYTHING" as Tesla FSD V15 hits Las Vegas Strip at NIGHT The touchscreen tracks surrounding cars in real time and even MATCHES the action outside. Vegas looks like a video game, but Tesla's playing it for REAL 🔥 Writer: Marie](https://news.google.com/rss/articles/CBMibEFVX3lxTE1xWkhNS3VfcW1zMWhGai1qNFB1S2Jpc3FHcnZ5Y1hFQ2xFR25TWjZVSUQ4czZmOWJsMWxiTWVzRllCaFhlVjAyNXNKTmFUSjVHSHVxXzFlLTdURGJBWmRnY2pUenk5RGtEOUhFcg?oc=5) <sub>X</sub>
- 📰 2026-11-28 [NJ Man Rates Tesla FSD Safety 100%, Musk a Dealbreaker](https://news.google.com/rss/articles/CBMimgFBVV95cUxNQWY3WWg0Y1hRMWpUZ0RSTXpIVXY1cHI4ODhZUHNhUlVMbFp6Y2NoTUhkWWJpYm1qQkdTU3FfNmVnNjdtaTY4ai05ZmN4a0dMZTFnbnVrUlQ4QlFyb3FjemxDZmJaQzFLQ29pUEtoQ3IzNVZaYkNYUWJxYUZlejJnUVBldlY5bE5YNkxDVWdMRzItV21CbUdsb1N3?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-28 [全新实景视图特斯拉FSD v15不再独有，小米汽车世界模型2.0实时渲染能力公开](https://news.google.com/rss/articles/CBMicEFVX3lxTE4yM1ZyZDlMQlNhY1RNZGFNX3YtTmctZVpVd0xwYi0zY3UtOHVSVU5IeTRESGhjaFdMdVdCZTVPMHliNVp4Rm1tLW4td0lkbWVxM25DUTZXM2dsa3BYakxMVWFzOFpSZUE3NTZKSDJGRmw?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>NVIDIA</b> (222)</summary>

- 💻 2026-11-19 [NVIDIA/nvidia-linux-utils](https://github.com/NVIDIA/nvidia-linux-utils) <sub>GitHub</sub>
- 💻 2026-11-16 [NVIDIA/scadactl](https://github.com/NVIDIA/scadactl) <sub>GitHub</sub>
- 📰 2026-11-28 [Your NVIDIA GPU Driver May Be Destroying Your SSD. And the Fix is Causing Black Screens.](https://news.google.com/rss/articles/CBMizwFBVV95cUxQWkVtTU9sblNmdGg2cmplaGlaTldGZUhzYWpuaUNpMkYxREhxUXlhakxTeGdKS0JLMThMRi1PMEJQSDV5angtMkotUDFMSjI5Q1Rjd0lCcFR3S25OeVp1NzhKZ2UzWUxVcEtLU1RPQWNHa2dmbDV5Y0NIcW1uZDNEYUVONWlzVnY5TkFfSkIyLVBGaVhKaUNhNlE4SU0zUl9oYV9jdlRXRjhhbnQxenhYVzhkM1FnQ21XczRYa0FpSkx1LW5SQWZmRVdhcVBQeVU?oc=5) <sub>Medium</sub>
- 📰 2026-11-28 [Nvidia says its GeForce driver fixes a bug that could keep writing to your SSD in the background](https://news.google.com/rss/articles/CBMihwFBVV95cUxOR1czMGp3UXNob0JXUDZYNmFYSGVJYlpCWXVXaHBvdjExdV9TOEZSc0JnR0dUcGlpUHcwUVpFT2JqUUVjSmdHSWpoM1QwcjBoT1R3VEJlWXhzOURUYW43bWVGaktPdmJZaWpYNUVuMGFoX3VGTThXeW5vZGwxYWVIWDFBUVB4OHc?oc=5) <sub>MIXED News</sub>
- 📰 2026-11-28 [AI Data Center Investment Sparks PC Parts Shortage; 'Chip-Tech' Trend Drives Used-Market Search Volume Up 90%](https://news.google.com/rss/articles/CBMidkFVX3lxTE5ESk91WDgzWVBONGZjQTVNZkczbHZ5TE9DQU5taGJpZ3Mwc2lOWnpHYjVfTVMtdW15V254bzNodWZneS1HN0NpLWNnOF8xbFdLSzZma0xfbEtTUTJZTk5rLXF3S1FvOHVNT3hCejk0dGtfQUI4THc?oc=5) <sub>BigGo Finance</sub>

</details>

<details><summary><b>Wayve</b> (25)</summary>

- 📰 2026-11-26 [Transportation: Europe’s 10 most-funded companies in H1 2026](https://news.google.com/rss/articles/CBMijwFBVV95cUxOaGZzS19fUHdTZm93NGdZVU5oMGFmR2lOV3dvSFR1bTNHM0RMR3lyQzVKRnl2Rmk5eFRla0puMWtQaW9TbEhRN3NzVzV6RmNnVE42SlZTT2ZLZDVqaVk2R29hRlVKV3BRX2lJNHZhMzdYbHhWRXktVWFTSFJ4VjVjV3A5YXFWMVljeEI5X0Zkbw?oc=5) <sub>Tech.eu</sub>
- 📰 2026-11-26 [Why data, not distance, may determine winners in autonomous driving](https://news.google.com/rss/articles/CBMif0FVX3lxTFBHem93SFVRQXJ5OTdlSXNqY0xwTWpGY054cmdBVThPNU9LRXVRdHItSjhuLUV0MUZlQUM5a3NVM3AtWHZJZDM5ZHpLaVlIVFdOUi1fOEdybDZCck42Sk1pTDZPaUt4OGxOazFUUFdVRlpBX2dwSExjaFRXem1SUXM?oc=5) <sub>Automotive News</sub>
- 📰 2026-11-23 [Autonomous Driving Software Market to Reach USD 6.78 Billion](https://news.google.com/rss/articles/CBMinAFBVV95cUxNZFVjLThIaVVwbm1rWlBYT2IzMDFFZEF6LWVzaWY1YTR6b0JLeDBla0VacjF0dEtpQjhGblZpVjUyZV9ZM3lSS3UwdFdtYmp0dm15SzdBZnpEemNqMlcxMXZ4TnVDV3FqZjNCOGdWNFhBRGFUWVNlV2poZHFkdDA1OEY1QlZaZzZ6Z09QQWtTRDQ5WGxyV2xmbEtxOHo?oc=5) <sub>openPR.com</sub>
- 📰 2026-11-23 [Mercedes gets edge over Tesla in race for self-driving success in Europe](https://news.google.com/rss/articles/CBMihAFBVV95cUxNREhrZGszRlNBUzFxbjBURFBhQldOMDFiOGV0TVNMWWVuYjA5dFdCTGpGV0RCMlJJczEtWkd0eG9YRnkwZnFVTFRseC1iT1lBM2w0LUlUVFhqdk1ydU1vWDRPVGZfTlE4SnRSRnZZTkMzVzdnVFJTM0dobnRKRG1jOV9Yb0w?oc=5) <sub>Financial Times</sub>
- 📰 2026-11-22 [Kakao Mobility partners with Nvidia to develop Level 4 autonomous driving technology](https://news.google.com/rss/articles/CBMi2AFBVV95cUxOUnMwVTdET0JiaXlkcm83bUZkQUt0TFpJd1lkZG13a1JIUWl3dW81UXlGbHN1Q2Z4VDZGVE5GcFNmeTRsNG1kODJpTTJCclVueHQ1LVFTOTFFWUVpRUpQYmMwc0ZSUHJqN05IR292WVBsOTFUMDl5VldhWUd2UkRfd1NXZ1BQcnI2TFFJdmx1cHN6RFY3aWl0VnppeUxYV2xPWjdZRWRJVzkwWFZ6SWdXQ3FLdTNLMFE5bTRMUkZRRWdlamhhT3ZZNXVOLW5LbnVaX3h6STh2VGM?oc=5) <sub>Robotics & Automation News</sub>

</details>

<details><summary><b>Momenta</b> (128)</summary>

- 📰 2026-11-28 [Guangzhou Auto Show \| All-new IM LS9 Confirmed to Debut on Dec. 10](https://news.google.com/rss/articles/CBMi0gFBVV95cUxPd1ZFODZTbWsySE5XeEtWcm5OdEg5WXQ0OFF5ZkUzYlVfN1p0MlNOeExMNWt2ZTNUS0lDVDBPM0xqTnhWU21mUmM5bHhuc1dfeDMxUmpTN2FNYkNidm13dXI5T1JyODNSY1B6M1hpaGJ3aF9oeGd5bW5saXVQWkpKVi1Gc0FDeFhwb0RMbS1LcWs4Xy1DQ0RZV2hSYWpfMkh5MHhBOVBCWnFacTc2cXhWS2RWRDhZMC12SHFHR3IxeGJQUTFTT3RWSHlUczFRYlZxRmc?oc=5) <sub>Gasgoo</sub>
- 📰 2026-11-28 [奔驰纯电GLC标配Momenta智驾？别被表面合作骗了，真正的看点在800V和25.49万](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5NWEVuMXFGb1NubDFUNjh2TWFGZ3c3X0xtTFkwSWlTeFcyREh3MXk2bjBISUJFcVNWNE8zSTdQNExwNWlxREVpakdnUXpOZzh1eGhmT1BpaFJkSGc?oc=5) <sub>网通社</sub>
- 📰 2026-11-27 [#2026广州车展# 东风日产是疯了吗？NX7带Momenta R7辅助驾驶的最顶配版本，139900？？？ ​](https://news.google.com/rss/articles/CBMiY0FVX3lxTE5wVkx6MVR2cjkxd2Zuak9SLTc2a2xXWXZWS284Q1RIbkowemtWRDBNQnpaOWpoVjhtMXIxR201NTFmUURpY1FYOHhCYkhlME5FZV9JbDl3bV9oN2VZUTI2c2dROA?oc=5) <sub>新浪网</sub>
- 📰 2026-11-27 [2026广州车展 \| 国产本田全新冠道首发，搭载Momenta R7智驾](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5vY0RQcFh3WW13blFCaTVrY090aF9pQ0V3anBlQlFReFc2am0zQmpCdXBKNmdLT1FYRmhYanVHNDI1d2w5Sy0tczhTZlFkOUxESXV6NVkzMzVKZlk?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-27 [奥迪 E7X 登陆2026广州车展，搭载Momenta R7世界模型](https://news.google.com/rss/articles/CBMiSkFVX3lxTE4xWWVwQWkwT1FWRmZMOV9CakJCZThYbmpYMUtkYTVMX1ItZV91ME14NXJQY09PQUR3V1FsdDl1VHlVaW9yZVVJcXdB?oc=5) <sub>TGBUS</sub>

</details>

<details><summary><b>XPeng</b> (250)</summary>

- 📰 2026-11-28 [广州车展小鹏展台：机器人真来上班了，车只是背景板\|IRON\|小鹏\|MONA\|广州车展_新浪新闻](https://news.google.com/rss/articles/CBMiY0FVX3lxTE8zdVJEVTE3UFR0WXdqakp4R2ZETE9lR19zWW1PV3EwRGQzYzA5SG8tOFlTcm9fUXB4ekxYckZhNjRRRTZ3bXBwZGZ6SEd0bm1VZmtpbzQzRHNvYWhQYkdfRWxFRQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-28 [小鹏MONA L05和L03怎么选？13.98万起，3个维度说清+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBWS2phdWlKdkRGMl9fSkNPVlJMdGpuTUpnSUxLTUZSVVRNenNTSTNXUjRodUhwRlhDWHdqR2drU3NOYk5KVnR4Q1B5ei1SUDF2Zkt4TEZnQzVwUzlnbkhJ?oc=5) <sub>新浪网</sub>
- 📰 2026-11-28 [小鹏MONA L03升第三，宋Pro新能源降4位｜10月紧凑型SUV销量TOP15](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5rWFoxaFJHTmsycjkxR1E5QjZqV080anFVUXFjci1Yc1FTWVhvWFdRMWFUMmJNd0JVcUNhVnk4cVpzMlN6NEhHbjQzdVRaVGdVcGFIMWxkRi1pUEU?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-27 [XPENG targets more than doubling overseas vehicle sales in 2027](https://news.google.com/rss/articles/CBMioAFBVV95cUxPMjFHd29KOHEyZUx1RkhBTkdnYmw5TlBGcWtxb0lkN3ExdTVXUzVGMjhueVJDTmxCaHdBMkRHMElIU3J5MElma0RhNFVtQmVZbTUyNElCb2M4enZrNVhBUFZyMkZseGx5bGFSaU5kdThDOVA2UzB4eE00cFBKOWFDLWQ1UDNLQy11RDIwN3ZRNzVlaDRhd0tIVHVtX0JkeElT?oc=5) <sub>grafa.com</sub>
- 📰 2026-11-27 [小鹏MONA M03落地多少钱？6个版本算完账，这三类人闭眼选+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE81M0ctYWJOQ1dYbHViVkxkbGhZb3FJRFN4SDlCdkVieGZfZXZLSDNhM3RnU2RmU0ROV3RXMUVNeExTN0N4bEdNTTdEOHpLcWxxV0ZkdzRyYXdRNmQ2cWVz?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>Li Auto</b> (169)</summary>

- 📰 2026-11-28 [Are Automakers' "Competitors" About to Change?](https://news.google.com/rss/articles/CBMipwFBVV95cUxPMG5rb3I2RHA0Qlh5WjNtTHZGQnVVcGlHWjRKXzNoNlF5eE9RTm1UXzlYemUtNkdxMWRoQ0RQalQ1eGN0QmZrYkR3Z20yTW5vOU55Z2tEd1pKMV9GSGhWLVVkNUg3SXc2TVpOdy1EZG9Ud3VnWEloc1hMd0hheW1jX1NrVWs0akNwWnFtTmwyc1MyRncybW53SVBKdnJ4Ymk0U0wwdXNwWQ?oc=5) <sub>Gasgoo</sub>
- 📰 2026-11-27 [Hongqi H9 plug-in hybrid launches at 329,800 CNY with Huawei ADS 5, holding pre-sale prices](https://news.google.com/rss/articles/CBMiwgFBVV95cUxNcm04a0N2X1JEMXhFc295YzhDUW91bUZrVTZWWHhDUjMzakJnXzNJQ01sVjFRNnoyUWYxYndVSGpZT3FsUm1pTGpNeDJzMW5EcEpBQ1o4UTNUZDkxSGtLcTdTQW5YT3hTVXFqUVdOYnhFcll6SzZfRE9GVTZXWTRWRDNKU1Q3aFc5c1RValVwT0dPTEVtdDUtZndwMUF1R3BWS1l6YjFONi1VNzliMjQ5ZjU5RkxKbmZ3eTBVMnBLRER0QQ?oc=5) <sub>GlobalChinaEV</sub>
- 📰 2026-11-27 [Nio expands best-selling SUV lineup with launch of ES8 Mirror Black Edition 2.0 at Guangzhou Auto Show](https://news.google.com/rss/articles/CBMikwFBVV95cUxQVEVXTlNDOW4wMDRWUzRXa3NSXzdZTTlUU3MzOFh6Vl81ekM2UlZMb3pVRlQwdkhhMDhsSWhEU21yWGVzZXM1emNSOHZ2Y0pTQzUyTUgwRmF5b1JjYW8tWnhKWFJFOUZZb0E0alNHdjFvbWdidTRNQ2tvZGc0SktJYmpGU241RTljRnFHeW9YbG5tYWc?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-27 [NIO's William Li: No Blind AI Labeling, Long-Term Gross Margin Target Raised by 10 Percentage Points](https://news.google.com/rss/articles/CBMidkFVX3lxTFBRZlF4bmZIM1FpakZtZjdiMG9mcE5UNF9tdnZicnEzUXdMZU9OVF9FUEUzZjQ3MEFacE1wMnRZLTNOLXhDdFVBX3RVVEdPcGpEWDdmNHFsQzd1d3JXSHBaYlR1VXdGYm84ME9FLV8wOEV4WENycnc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-27 ["Self driving" LiDAR domes now a status symbol in China as 1 USD fake plastic covers spark confusion](https://news.google.com/rss/articles/CBMi0AFBVV95cUxNRy1iVUVZR1RDOGdtMHlXOEJyMVdxOEhYNUpqekhkMUVvVm9ySFMxQnBpdEh4dlpqZGRXa2RyR1VoM1JSbFdpZy14ZXU1VGg4WG82OTN4MW5YOGE2OW5WV2k3d09xNVV0dVc3QmZqQUZ0Sk54Zm9RRzZZeFJlaVlWNWt6a0tNZk95OVpaV2tvWGUwd3hiVGY2UkdqQXVUTFBUSzZEdHZZSjhaU1dkeTV0QjdTVG95aWFQVy1VVFowQ3didHl3ZG9KRDJMTXBxbC1i?oc=5) <sub>CarNewsChina.com</sub>

</details>

<details><summary><b>NIO</b> (203)</summary>

- 📰 2026-11-27 [小鹏的展区对面就是小米，两小无猜紧挨着。小米的旁边是蔚来，小鹏的旁边是上汽。 http://t.cn/AXTSaa5W ​](https://news.google.com/rss/articles/CBMiY0FVX3lxTE5BdUhNNW9uUnhwcC1oRkVJT1hpR0M5N2pfWlVjQW9GcDhxeWxpRTFmYTVzVlhmX3BpMmJMQ2RhUGxOWFBpZ1gyaFRHTmhteEZLeEMzbHlTMTMxX1RnU3pNMTJrZw?oc=5) <sub>新浪网</sub>
- 📰 2026-11-27 [Nio Onvo launches updated L60 Black Knight edition starting at $31,430](https://news.google.com/rss/articles/CBMiiwFBVV95cUxONUZaeTNXbnZsS1JDLW5XbGNDdW1aeFotNXFtTDVISU03OUhxNk0zUXNqZmpNY1BnTjNjTFY5Nll5ZDgxZ0k5NS1uUWVlaGROMWtZVkNJejVfVE5tN0xvUE96WS1qUmRtMlNjMUdKZERxV2JESFpVNWl2WW1uakJFQ2E4VmY5VE5vY2Zv?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-27 [NIO Deploys Over 7,500 AI Agents, William Li Estimates Annual Savings of About 6 Billion Yuan](https://news.google.com/rss/articles/CBMidkFVX3lxTFBWVWFYUm5SMWtVUGFFWWcwQnRfYlJmaHJ0a1VPanNpLUpsem1TRXJLMXZXMWVQMFM4OGR0a2RON1hLM2I0QmFfMk4xRnBJS3ozUEpMUDBuVU9udXk4ZjN5WXcxZ2dnMlNLTklla0hObTdfeUJ3R0E?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-27 [蔚来发布NWM 3.0智驾系统与NOMI 4.0，端侧算力效率与座舱智能体重构](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBoWUhVa1A2T2FoeS02ejVXNGNVdi05UkVRcjlFbkF2amVUQ0QzdVFuSTBlQVZ1cGNnMXB1dXJubzhGdkxrR0E3RENLSmpMMWczcW9FN2RmZU9yTkE?oc=5) <sub>网通社</sub>
- 📰 2026-11-27 [【三分半看懂发布会】蔚来开始造人了？！语音助手NOMI直接成精？](https://news.google.com/rss/articles/CBMiWEFVX3lxTE9uZ0lSR0dla0J0clJpTWhNWl9maUtja3NGNTg1SGZDSjUyS3pFSHNZelcwWkNBV204ZExmRUJmNVNobllUQTZoZTlTTFd5alJBN3ZBY2JuS0s?oc=5) <sub>爱咖号</sub>

</details>

<details><summary><b>Huawei</b> (366)</summary>

- 📰 2026-11-28 [New Deepal L07 & S07 Unveiled at Guangzhou Auto Show, First to Feature Huawei Yinwang Xingchi](https://news.google.com/rss/articles/CBMi5wFBVV95cUxOOER2ckIyamdRZ1JrLUJiOGZYTi1KTWZZQnhBYnFiLV92azdSTlVMNkk2UnVYWC1zcmNjZThhdURxV3VJVmU1OGwtV2FGbm5mekRjdGotMy0wQmhkemxHYXRjQzBicWs3YXZjS3VzRTE3RDRQTHEzc3gzZ091dG5XTXJqNS1WRWF4bGF0Wjk0VE1tS2VDdWVObjN1WlVLWjNNclREMVN6UUJRSnRtT2pfc25NOUlTVldjRW9XUjBiTDE4QkZvZU5BS3h5cEtlRFcyd0xYdzhhWkpMQjVzQ0dqV3hETl9sclU?oc=5) <sub>Gasgoo</sub>
- 📰 2026-11-28 [Toyota Highlander 9X: First EREV, Q1 2027 Debut](https://news.google.com/rss/articles/CBMimAFBVV95cUxOeGFWei1xUlVZNTdBNXVqdzZJSC00OHpIUHRIeWxKa3RhQlJESjJaM2tjT2lrV1U5YlZsUFNMZkVyVC1UTkgzX25VUk1LT3hObzhhekZsdUcxWHBwQ2pvS0I1cy14OTNGU05xRndnbDhVdWlYWmotb1F4azBSUVNVSU01eG5TSHJZQ1Iwb2V5ckdxeEtCa1FPcg?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-28 [Smart Driving Installation Rate Exceeds 70%, Trust Test Has Just Begun](https://news.google.com/rss/articles/CBMiygFBVV95cUxQT3dibEYwZFdaMVp0OGo4c09wTlZLbF9uV1JFX1VWY1lBOG9UemwzdGxFal9oaTZXckNfN1haRy01eGdFR0REbUtwLTYzb3hlNmlJMmtmSXpaTW90bXpYdHdDR3BsYmpRdjY1OE5BR2JnaFVfckE5MWtuMVA5dVVYWWpQYWtpRUFOdmVfTzg1ZnVkUE52dFcyTGp2QnJGc1BxQy11ZHlwdG92enFwNEJIdWxnNmFkbTRhdGtyS2taNUlqbGUzR1RXZm5n?oc=5) <sub>Gasgoo</sub>
- 📰 2026-11-28 [EPICLAND Launches X9 EV, Limited-Time Price Starts at 279,800 Yuan](https://news.google.com/rss/articles/CBMixAFBVV95cUxQemtmWE1NYXZlWXVmbnBJekdkLTBtZHhkem9QaVlZVUt5dDNFeGxibzZ5NEdRSHRGeThjQUQ2eWFlVVhCX05zUm9HaDhOTWh4VUtndGZjMUZNWlRLeERZTzdBa29rb3JBYkZwZUp1RlVMMlNjMlFFSFlsTzNVZmZCMjQwb1VOaHg1ZkFCcHg3RXA5SFZzb2Nrd29YNjJNUHV3RnduSFhUUXl4bFRDWmpJX1k2OWVZdzQwVUJZMHJDZWYyYUgz?oc=5) <sub>Gasgoo</sub>
- 📰 2026-11-28 [Avatr T09 Production Version Debuts at Guangzhou Auto Show, Launch Planned for This Year](https://news.google.com/rss/articles/CBMi4wFBVV95cUxNQVlKNllKbG9NNVBYNUN3dW5QTElrTEwxWTdrejhuNTFFWkluOG1fVjJvSkFKUzAzdW5wcTRMcXhWdkY2Qkc5R0dfeUVvZl8tWmdXbERqRU9qd3g5WDRUU2FFNEJYbEJuZldua0NkZ2gxOXRDN09TN2JjUXVpQ0FOSE5Bd2tCR1FKWkJ6aTduZ0xobG10UFlVV3FHNVM2SmZ3dGhxSjZYTEJlS3FjaUtJZDNuOG41WmhYYmZQRkRlUjRKTmxRVDZSZ21FQVpwcGxaVTRtaEpxem9SUmNPSjcxZ19ncw?oc=5) <sub>Gasgoo</sub>

</details>

<details><summary><b>Baidu Apollo</b> (54)</summary>

- 📰 2026-11-27 [Competitive Analysis of Autonomous Vehicles Market: Waymo,](https://news.google.com/rss/articles/CBMilwFBVV95cUxNQjdpUFNMQzN3REM5ekNZaV9JUlU1TlFZWWtKb28yNTNRaHFHVjNWM1RxVl9NbDA0Yl9TWGJlOVF0WXVPVHV6VE1kSXJOaEVYcFVFb3RYd08xb19JWFhwUENlaElmV1ZVWjJuMzg4WTJRM2piQ3dUSkhrSHQwYjIxNUc0N0IzcWZtdXlnbnFhUW91eXJXYW0w?oc=5) <sub>openPR.com</sub>
- 📰 2026-11-27 [US and Chinese robotaxi markets enter explosive growth; 2026 output value gain at 100%; estimated total at US$850 million](https://news.google.com/rss/articles/CBMia0FVX3lxTE5pSkZtLXVFOEgxMnotMWxJOTNtQ3FHRjdHNjR2LTc0TklSbXp1S0k5S3FtSEY5NmtNWlVPN2xZaTNxTmxiNWxLSVc1SVY5UzZnNl9mZ2Rsazk4SDFuQVhMR0Noa2VvT2VCR2RR?oc=5) <sub>digitimes</sub>
- 📰 2026-11-27 [百度萝卜快跑Q3财报：深圳全无人订单环比增约170%，武汉模式跨城复制仍待验证](https://news.google.com/rss/articles/CBMiVEFVX3lxTFB6Sk9TQTE4UklmeXAzSC12b05nckJXYW11dEZWNTJoNnRHVXVuc2NUdnluc0ZIOEVFMkhkZzNkV0VLc2JBcWFxV2lZNUhodHJmb1RRbQ?oc=5) <sub>虎嗅网</sub>
- 📰 2026-11-26 [The Fierce Competition of Chinese Autonomous Taxis in Dubai: Market Expansion, Tech Advantages & Global Layout](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1rNWFaSE9Ed0Z3cVV3WE9aYjc1MW9QWjE1VEZ0cmV5TDZ5cW96TktTWXVrWWlyLUFhWG9pd2YyeFoxWFZteVNtZ0hFamVkOVU3cGhR?oc=5) <sub>eu.36kr.com</sub>
- 📰 2026-11-26 [Hop In, Buckle Up, Sit Back: Everything To Know About Dubai’s Robotaxis](https://news.google.com/rss/articles/CBMimAFBVV95cUxQT20yRnBGODVyb1NLdl90MlZ0UXNTY3lzdVVfSHJweTFla2Rkdk9DbFFFUjFTVEVnWmxlVW1TdzVtQ3EyRzE4YVZBdVJvM2JMZlBJR2pVdmVuYVVxd0VWaEQ4bkp2b0RvTF9KT0hNZldZVW1XanpwWkZkZjJPUzRHdWQtNjZRYmJmTnQ4REttZ000ZUxzUXpGQw?oc=5) <sub>Gulfbuzz</sub>

</details>

<details><summary><b>Pony.ai</b> (154)</summary>

- 📰 2026-11-27 [港股异动 \| 小马智行-W(02026)涨超6% 三季度自动驾驶出行服务收入飙升165% 公司重申全年车队目标计划-证券之星](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1mcU5vck51WFVnLVhsVVU5emhuWXJQUDk3YkpqXzhXbF9qeUJLZ0JHM3RzUjJmdWFZZXBzY0ljdHFFQmRrRVkwZHQ4Zm0wNGxLbDZURmR3Ml8yRUtsM1E?oc=5) <sub>证券之星</sub>
- 📰 2026-11-27 [华泰证券：具身数据标准提速，关注Optimus亮相与T链](https://news.google.com/rss/articles/CBMijwFBVV95cUxQYmJjUS1XdkFZM0xXam1uZWJuOHFLYXktZE5TdU5XWEJrMVh5VXB2VHIyalZrVmZZMnFMd0FwakFRbkpvNU1PeWRsMWpDT1JpNVFtZVNPX01LbldvVlZvYTNoalFJWkxTYTlOazZrWWJEUDFYWkJKa2lmLWxGa09YVmZOUE50YjdKR2FNemg1TQ?oc=5) <sub>21财经</sub>
- 📰 2026-11-27 [小马智行-W盘中涨超5%](https://news.google.com/rss/articles/CBMiXEFVX3lxTE1zdkJxOXV1ZV9maEhRQzRlUTdiT0VHUmZCSEFKcGxJSE03SlJGZDlBN3BjQ2doaTlaa0d1SmxfemNtZExUTXVQNGdCNjJLOXYybndxMHRUSjdmMmlH?oc=5) <sub>www.caiwennews.com</sub>
- 📰 2026-11-27 [新能源车周报：中国车企前9个月在39国市场份额超日本_股市要闻_市场](https://news.google.com/rss/articles/CBMibkFVX3lxTFB3REJ0c2taWUpmSXZmcThDZmJYVENLbWw4cUNqMjF4UGZxTnJxOHRwWm1EdWdxTmtzN2dSQXk0empHWUttemNBWE11ZERiU1dxclI5eTZVMmFxU0puYUQwUmpiTjFGUmdqUDU3cDNn?oc=5) <sub>中金在线</sub>
- 📰 2026-11-27 [US and Chinese robotaxi markets enter explosive growth; 2026 output value gain at 100%; estimated total at US$850 million](https://news.google.com/rss/articles/CBMia0FVX3lxTE5pSkZtLXVFOEgxMnotMWxJOTNtQ3FHRjdHNjR2LTc0TklSbXp1S0k5S3FtSEY5NmtNWlVPN2xZaTNxTmxiNWxLSVc1SVY5UzZnNl9mZ2Rsazk4SDFuQVhMR0Noa2VvT2VCR2RR?oc=5) <sub>digitimes</sub>

</details>

<details><summary><b>WeRide</b> (133)</summary>

- 📰 2026-11-28 [WeRide: Q3 Proves The International Robotaxi Inflection While The Market Prices It For Distress (Strong Buy)](https://news.google.com/rss/articles/CBMi3wFBVV95cUxNZkx6bUw4aVBabnV6NTdVRVA5WlpEZHdmc0JSWWs1TTlwMWZDT19lTEpQck9WMzZteFQ1ME00UFltS1NDZm9QZFR0ZU1lZkUzZGJpdFFFbmJGU2t3UGtfaEJHaUVIOFFXZm0wTjJpMmVsdjRITkI4UDRYRmhGY2ZxbFZ6engxTjB3VjJybXlnd1ZRMDVtLWFWVFJtRzZFdjdyU2lkTEo0TGEtV0w1ZFhhVjhDdGVyZFFfNllqZlBQUE5wM1VsRzA3NWhYZFdyWWl1Q2Q2ekp3ZjZjSkVlUUNF?oc=5) <sub>Seeking Alpha</sub>
- 📰 2026-11-27 [US and Chinese robotaxi markets enter explosive growth; 2026 output value gain at 100%; estimated total at US$850 million](https://news.google.com/rss/articles/CBMia0FVX3lxTE5pSkZtLXVFOEgxMnotMWxJOTNtQ3FHRjdHNjR2LTc0TklSbXp1S0k5S3FtSEY5NmtNWlVPN2xZaTNxTmxiNWxLSVc1SVY5UzZnNl9mZ2Rsazk4SDFuQVhMR0Noa2VvT2VCR2RR?oc=5) <sub>digitimes</sub>
- 📰 2026-11-27 [Chinese Robotaxis Land in Germany: Momenta Teams Up with Uber to Launch Free Robotaxi Pilot in Munich](https://news.google.com/rss/articles/CBMidkFVX3lxTE9na1R0ZWQzYU5kX2xndXZkbXpMWWFTbmdDXzBsQjBydE1ZVTlYYktzbWFybmFtR1hGSFNUTzlLY1E1NWhHV1puM2x2RVlyT0ZuM204S3ItVDJ2UFR5UmZTWjRCdlhhYWlOdkUxQk1EbWNJa09lOGc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-27 [WeRide CEO Tony Han buys 199,306 ADSs in his first open-market purchase](https://news.google.com/rss/articles/CBMilgFBVV95cUxNTDBnV2dLYVJDQllRdkJaSEU1YjBNNE9ILXREeFlDZkc4eUtnNC1RbTBETE8xa0ZNWDRKNm44SVBrSGlsNi11NVphUTV3V0I1Ym0wV196SC0xZm16bjY0Vy1ZSGExZmZpaTBqVHQwQVhkSy1qVUswYzZDSlpqRUVBbGZ2NzVMTEQ4dHdwdzNYR1l1dW9tZXc?oc=5) <sub>MLQ.ai</sub>
- 📰 2026-11-27 [We Spoke To An Autonomous Safety Operator To Find Out More About The Future Of Transport In Singapore](https://news.google.com/rss/articles/CBMiiwFBVV95cUxOOE53QTVyd0xlekN3TWhReHI1c29pSWVrMDF4ZElmTVhIcnNPM1ZLalowZHlIN0JwaV9MLU81Z1A2WDl2Q0ppWnhZU0RXbkNNU3FoR3pROWNteEpsVkZXT25INTR0Y0xXV2R0ZGM2Qlk1Yy1nZzRMOUxzakwxYjVoQTVhQ2tKb0RFSGY40gGLAUFVX3lxTE44TndBNXJ3TGV6Q3dNaFF4cjVzb2lJZWswMXhkSWZNWEhyc08zVktqWjBkeUg3QnBpX0wtTzVnUDZYOXZDSmlaeFlTRFduQ01TcWhHelE5Y214SmxWRldPbkg1NHRjTFdXZHRkYzZCWTVjLWdnNEw5THNqTDFiNWhBNWFDa0pvREVIZjg?oc=5) <sub>TheSmartLocal</sub>

</details>

<details><summary><b>Horizon Robotics</b> (153)</summary>

- 💻 2026-11-22 [HorizonRobotics/holobrain-0.5-homepage](https://github.com/HorizonRobotics/holobrain-0.5-homepage) <sub>GitHub</sub>
- 💻 2026-11-22 [HorizonRobotics/HoloBrain](https://github.com/HorizonRobotics/HoloBrain) <sub>GitHub</sub>
- 📰 2026-11-28 [FAW-Volkswagen ID. AURA T6 Cumulative Orders Exceed 50,000 Units, 20,000th Delivery Completed](https://news.google.com/rss/articles/CBMi5gFBVV95cUxPa2MwcHhFS2c1X1lNZTVqcU5nTEVOTjhJWFgxc2hBd1ozMVVPRE5raTRzajEwLTNEeTdtdXhzOVdld0hKOFhwbER4eTdGdGY2d1dPaTNsU3dodjJLdDB2azVGdEJ1aGNjU1ZjQnRzTVJuR05sTDlGeURKRnZKa09Ba1VhZUF3XzV0QnQyRDRsQTBwS1JQVy1NNWhRMHRRTE43blpiZTJVSkFVSDQwRjh5eUw4MzhuTGl5d0V6c1FNYmw5eTdhbHl1Y2NXczlMcHVMWGQyeDJkbG55RVpVYl9PaXJzMWM0UQ?oc=5) <sub>Gasgoo</sub>
- 📰 2026-11-28 [SAIC Volkswagen ID. ERA 8X Adds Ultra Version, Limited-Time Price 249,800 Yuan](https://news.google.com/rss/articles/CBMi0wFBVV95cUxORVZqd1RfUW1MbGZFRnhjdmU3aDRSR0dISUVqVWFIWDRDNUtoX3J1QTJtdW5yRG84Q0dkeFZjYVI3Y2g4NUxoVUdTOUdtX0EzZWFpLUxmTDBFSkRVRnVWVmZuOWQyMXhXaGJxMTg4dFdYaXhuVkNoME9JTlFqWEpBaUZON1RsZVVnZnFtQ2F3WUtBOThncEhzUWEyRWszNkJKUXBwQkJwMi1LRHYtd056Z2RXR1l2empNV2JVNmxzVzFhU1BEUGJmeFJWS0FPZU1sMGpj?oc=5) <sub>Gasgoo</sub>
- 📰 2026-11-28 [长城大狗H6L双车上市，地平线征程®6M推动城区NOA进入燃油车市场](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5nU21aX213TV9WTURhQlhOcHJDd1BjenpqVHNGZnBsMEQtM1RZNFNScEhGTy1wZ09aRzRTcno1SV83V2haQi1GdXhFMU9zVDE2a2FPdVVtSExpWEU?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (17)</summary>

- 📰 2026-11-28 [顶尖澳门彩098258联名空调亮相：以冠军品质定义智能温控新标杆](https://news.google.com/rss/articles/CBMiU0FVX3lxTFBXWkNXS0UxcFBzX2pVV3dBcGVURVpmVUk1RlVKYkZtWUkwVTRvSDdaSmxTdUVFcE9TaW4waFE3SFpSeHdSWEkxWU1FeENLYXFrUVNZ?oc=5) <sub>集微网</sub>
- 📰 2026-11-27 [元戎启行的这个RV方案感觉已经很接近特斯拉FSD V15了[哆啦A梦吃惊]猜猜看哪个车型会首批搭载？ ​](https://news.google.com/rss/articles/CBMigAFBVV95cUxNU2l1S0NlMGl5NTZ0VTFfbFpmdVd4VlVndU82YkFrRnZYeFR5dmxSakc3OWJqalM3Z21mX2x0Y2xoNzBRRXJpeG55SXlNUU5NTFZBNDNzRDYtelRLY1NqT3ZZdFE0Zi02aWJ6U0lvU0xuLVBIc0k1WktCamd6dnEzTQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-26 [特斯拉Reality View引关注，元戎启行发布深圳街景渲染视频](https://news.google.com/rss/articles/CBMigAFBVV95cUxOWXVweWkyU3RMMW1URnhrSHJBWkdfLWtVbEdUUkRjd0tPZUM2WDFybUVmRjcta3MwWHRWYjA5Z052dG1DTDFrdFJMRURXdE9KeGM0NWF3UUNNTDl6STZnbkRaZjdFRTJ4cS1mZE9EemxUd01kOERvaVUtS3VYWjdraQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-25 [特斯拉FSD V15 Reality View惊艳 元戎启行同类技术曝光](https://news.google.com/rss/articles/CBMic0FVX3lxTE5jNldwNDBLcDU5OVNNckN3RzhlMXVZdFJ5a2haZXpSTHJsc1BqcmRSRUd5eWlyRVZVcnUycU1VT0ZHancxaFZ1eXVxTmxDVVlkc2llODB4ME9fVmVDMVJ3dTA4ckRRV0hSMGMtbjRQUlV5cDQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-25 [特斯拉FSD带火Reality View，元戎启行早有技术储备](https://news.google.com/rss/articles/CBMigAFBVV95cUxQbVpMVEdmdnJxblRkVjdEODU2Y3BYZkdYMElDU1BKS0x5Sl9sR1M0bGFWQmRhNEQ5dGhYYWNWd2pBQmVyX3ROQ183c0x6NmI2X3Q5NFdQZHZjUFNXMWNoYW1WRzJ5NE9JTFAzX0VaX0VFcURsV1VqcXk0ZWo2Ny0teQ?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>Mobileye</b> (15)</summary>

- 📰 2026-11-27 [Why Automakers Are Shifting Autonomous Driving Budgets Toward Edge AI in 2027](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNeTV1TFRGQjVlTkc0TGVaOGJ1YUJxOTFER3RQaFFTU0Fab255RWJlRUFKRjN0MmhjZHFNcVlQbjRTbzNBUnZ1MkxFTF9wY0ZYY0pscXRuWDY2SHFCZG9jakJRN1lUM3lGMmVvaDFLb1ZnNmFraS1CWDc3dnAwVmdfX0Z0Wk1IZlc3ZUd5dXY5MVlLeDlxQjl6MHBzcm5WcUZzbTUtU1NFZmw4dw?oc=5) <sub>The Weekly Driver</sub>
- 📰 2026-11-26 [Has Mobileye Global (MBLY) Fallen Far Enough To Look Undervalued?](https://news.google.com/rss/articles/CBMi2AFBVV95cUxPbmdYOTJyc1VLTFNOTDR3eXB4alExa1VIazR0UlRlWW9JeVRPYmZ0LUZCNnNyRkdrc3lKd1hLWU5nX293QUZadmU3SW9KREtzWjIwemhpaUpzMTNCN0F3ZDFGcHNZaU1OZkJxM3ZKTVF4ZVRwZ0Y3aElrQlVvcVBOMi1yRjhTWTZsak1hVExvdkpia3JmZDBKRUxRQzV1bWdQM1dXTHdHaFlFQ21kTXBWemRrMklERzdOcmdaNjNJVktTaUY0Sk10bWNOVHctZm5OMjBUYXhzeXLSAdgBQVVfeXFMT25nWDkycnNVS0xTTkw0d3lweGpRMWtVSGs0dFJUZVlvSXlUT2JmdC1GQjZzckZHa3N5SndYS1lOZ19vd0FGWnZlN0lvSkRLc1oyMHpoaWlKczEzQjdBd2QxRnBzWWlNTmZCcTN2Sk1ReGVUcGdGN2hJa0JVb3FQTjItckY4U1k2bGpNYVRMb3ZKYmtyZmQwSkVMUUM1dW1nUDNXV0x3R2hZRUNtZE1wVnpkazJJREc3TnJnWjYzSVZLU2lGNEpNdG1jTlR3LWZuTjIwVGF4c3ly?oc=5) <sub>Simply Wall St</sub>
- 📰 2026-11-26 [Shimmick And 2 Other EV Stocks To Own](https://news.google.com/rss/articles/CBMilgFBVV95cUxQWjNPbHNyS0xsVmZWRTVra0gxZV81TklmR01YOUJhU2IwazJsb2d2aE9FaFlYRTVoMzJKQy1HMmJ4djJWSkMwbW0xb2NZaHdobnY0d2pZa1hXV0xYTnp4S0VlLXJhREZ5Z3Brc1NHNVRDNnFEaGtmb1dZU0kzaE12Z3NVMWVrZmtHdUMtSWF2U0hXX09iQXc?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-11-26 [Mobileye Faces Rising Competition in Driver-Assistance Chips](https://news.google.com/rss/articles/CBMinAFBVV95cUxOS3dfVkV6M3dNNlh3Qlh4LVJjTlk1Y2FZRkhEZXBKR1RBVEdUYTNLR0RieUJwSmdBU3c4THIybEhlT1lwQnBocWU1X0ZvVUI4cW5KRUUtTFBrNlBMQ1lqdEZQa0RRd0ozaVdFTkR2ZVFvYngyUGVwZkdoS1hKYmhCN2lkWVFXRzFpRlBKeFl3WVZuakpfSkp2X3JMMDc?oc=5) <sub>Wisevoter</sub>
- 📰 2026-11-25 [Mobileye faces new competition as cars get smarter](https://news.google.com/rss/articles/CBMipgFBVV95cUxQTEZyekgzdFhjTy1DUzIyVHUtOUdyM3U3YWJmd0g1TDE0b2F5U09INkh6N3NycHNkSnBPYzJ2cENQWVFmMzdHOFdEdWVudm5fNnpsWlRPQjhrN1cxVWpJVTF1LW9ETUhfSGYxZFFHX2RFa2ctZGc0MGF6a2lMU3kyeFRQR1BuS0tIWXNmVnJwOHdYS2VSYUM1VGFMMGF1MzZUd0gwQVB3?oc=5) <sub>Yahoo Finance</sub>

</details>

<details><summary><b>Aurora</b> (35)</summary>

- 📰 2026-11-27 [Competitive Analysis of Autonomous Vehicles Market: Waymo,](https://news.google.com/rss/articles/CBMilwFBVV95cUxNQjdpUFNMQzN3REM5ekNZaV9JUlU1TlFZWWtKb28yNTNRaHFHVjNWM1RxVl9NbDA0Yl9TWGJlOVF0WXVPVHV6VE1kSXJOaEVYcFVFb3RYd08xb19JWFhwUENlaElmV1ZVWjJuMzg4WTJRM2piQ3dUSkhrSHQwYjIxNUc0N0IzcWZtdXlnbnFhUW91eXJXYW0w?oc=5) <sub>openPR.com</sub>
- 📰 2026-11-27 [AUR Legal News: Aurora Faces Securities Fraud Investigation](https://news.google.com/rss/articles/CBMitwJBVV95cUxQbDdxN2hoMm1FVG1vRHNlMGNNMVFfY1B1UnFEeFFhaU1yQTFWbUtKX2QtMDRKOG5XT0dkS0pMVDJHeHdqTDZtcV9WNXpESDkzUzd3eWpVVUhGS3Myd1BmZ2Q0cUZzd25EZXgtbDlYZXZURTNrMDc2Ry1KTk90M0g0NW9yWE05NmxzSzBqcG9tOEQwMWQya05nbmJEdUctWHNVOElIVHJpYktDSHlTa1dmRVB1MFI0NTZnSGY0dUF1Zk1oLU5kZlczRlF1ZWExeXRBOFY3TXdhT1V4RDJoS0V2RDhSTzBYelRWbXhwazE3eXpDODgxTXhrZFp0NWluS1R5Nm5iTlNoRWxLZ2RXTVEyWnZRSWFEcGx5cnAybXhOVGpCRVRZNlhXWE9DcE05V2hyMFFrV3Nsdw?oc=5) <sub>GlobeNewswire</sub>
- 📰 2026-11-27 [Driverless Trucks Are Already Here. Is Pakistan Ready?](https://news.google.com/rss/articles/CBMikAFBVV95cUxPanljb0t0eVlZaDV0dWZ4c0FHNTFvcTktTk1pZnpMT3R2T0lXQjlKMkx2N2V6TVNzOU9iRi10b3Byc2RWVTkyYmdTeEZHTjlJX096X3hGcWQwUlF0U182X0E2X0E2dXd1Qjh5SUIwRTlMcndZeUNUTnZzZUtOTGtsWllZNHRjQi1Dc3Q0ZHpsTTc?oc=5) <sub>Pakwheels</sub>
- 📰 2026-11-26 [Physical AI comes in every shape. Connectivity decides which ones scale.](https://news.google.com/rss/articles/CBMioAFBVV95cUxNUFkyZ1k4ZFRpSGpVSEZmY1J6dTFPNWFzTDA2ZV9lQm5qdHJtOFlxdU9Gd2NZNXRvcDRuQjZzaFVLVzNyc25QTVptOGI2VHcyLVBjcDJRVkpfdU1WT08xNW1oZVllTFdVYmxuZUpMRUtHVnZnVHhGTVZleXVvbGIxRFMzd3QtS1lFWWoyZklSdERDb0ljam9wZDFwZ3JMcUZo?oc=5) <sub>Cubic3</sub>
- 📰 2026-11-25 [Notice of Investigation of AUR: Kessler Topaz Meltzer &](https://news.google.com/rss/articles/CBMiqAJBVV95cUxOSlh0RmpSLUI5ZGFGYTkwS1EwUHdsYmpfV0lETHR4UW1wUS1RSlVVdUY1bi1jNVRtM3hKLWlQNXBBVk02Ti1CcWViWWhJLTlybmcxRnliWG45Z0RUQWRiTFE4aDZHeVFXUDNrNDZUUGdJdENTMjJtYkk3R0pzaFQtLVd0ZDBwV0RtRU5GSHNJMTJFdUtNMFlOdnRaQzhWQXdmYjM4UW10VFIyY2JRS2tBTTdpSDhIVXhLUVJFQjJULUdyR0MzdnBkR091N2VrT3JqdEcyaE1oRkttUzlDbm00WkFjWllkZWJjbFlZZUhKUDZWcTlHRWc0YlJwcllqdW0tSHM4YzREUGpDWHREWUZiZFBiQkV0QW1hN24yR0hBYnEyWlJidjFGaQ?oc=5) <sub>GlobeNewswire</sub>

</details>

<details><summary><b>Zoox</b> (113)</summary>

- 📰 2026-11-27 [US and Chinese robotaxi markets enter explosive growth; 2026 output value gain at 100%; estimated total at US$850 million](https://news.google.com/rss/articles/CBMia0FVX3lxTE5pSkZtLXVFOEgxMnotMWxJOTNtQ3FHRjdHNjR2LTc0TklSbXp1S0k5S3FtSEY5NmtNWlVPN2xZaTNxTmxiNWxLSVc1SVY5UzZnNl9mZ2Rsazk4SDFuQVhMR0Noa2VvT2VCR2RR?oc=5) <sub>digitimes</sub>
- 📰 2026-11-27 [Zoox Launches Robotaxi Services in Los Angeles](https://news.google.com/rss/articles/CBMihwFBVV95cUxNQnJjanUwRXVVdFRMQVN0WXd3QlltRGdfeVR3YlRYZ0NOcExZX2V2V3IzOEY2ZlgtMHhQOFJ5ZkpGMXdGM1VXZEN2TEFMclJNZkEySkFfY2xmQzdoQkJVZ0Z6bEVwX2NsVG9PWG9WbEJod2loQnNSb1RiaHRWTWlZWmpueDA0eVU?oc=5) <sub>Future Transport-News</sub>
- 📰 2026-11-27 [Zoox tests custom warning sounds for robotaxis](https://news.google.com/rss/articles/CBMiekFVX3lxTE9nOHVlWXAzVkluYTFOWXRRUi1xQjVoajFhSWZ4RjNXM1lOOHVJZUdvVjZ6bTE5VGlqQ05qaDBzQXBfVUp5d0FhbWlENFE0VmRkNjNqd2x4d3VpWWJ2WVA2ejU5VzNtdTRwTXVUS1ZSYmY5VWpwb01JX2VB?oc=5) <sub>The Rundown AI</sub>
- 📰 2026-11-26 [Jakkuh Vibe Codes Autonomous Lawnmower That Cuts Perfect Stripes Across Five Acres](https://news.google.com/rss/articles/CBMidEFVX3lxTE5lOGNlTXBwbzV2bkFVajBJamVmRDRLNjdHOFh0R2pWU1UtaE1fTEZOQ3dLUjJnLUd0TEt6QUJ4RTU4QWt0ZDhzLTNFVmZYVGh3Szd3QUotYmNOM2dleGp2LXJUOGV6NnFMVERXb3I3YkJ4OEQ2?oc=5) <sub>TechEBlog -</sub>
- 📰 2026-11-26 [Las Vegas Police Ran a Dutch Drone Radar Over the F1 Grand Prix](https://news.google.com/rss/articles/CBMijgFBVV95cUxPMzM3el9kMFVldzF6MkJLMkVOUFAtWEdBeWJDYzR3R2VCdjZ4QUxRc2pMRmh4X1pFV1AtZ1M1UnlxdDdXMHkyNWhZRTZCaDNjbkxiYXVVeWdkVzB2OWhIVk1SNGRpcDdTOXE2eWRRcmlSYlRTT0VsZ3EzcF83bElXeEdaRnJVMmtTcFB4UHZR?oc=5) <sub>DroneXL</sub>

</details>

<details><summary><b>Motional</b> (34)</summary>

- 📰 2026-11-28 [Robotaxi Market on the Verge of Taking Off... Which Korean Automakers Stand to Benefit? [Weekend Money]](https://news.google.com/rss/articles/CBMie0FVX3lxTE9WdExydXRKUXdVXzAwSXdjRTRVX3RDOGM1VFd4MmNRaUNBaFhxVWlnNUNxaTdWRDVYZnd1UzlEbUlKVVlydWlZeFgtNjlPdFF4S0I5aWI5SHBLMEZvejRid0I3OTVrRGFnRm1BLTlTTy1wcDUxRHpnN1RGRQ?oc=5) <sub>아시아경제</sub>
- 📰 2026-11-26 [Hyundai Motor to Begin Supplying Robotaxis to Waymo Starting in the Fourth Quarter : Finance : JKN](https://news.google.com/rss/articles/CBMiYkFVX3lxTE9QTVEzS1B4cFlESWNVbklSTGlEc2RfV05ESzRaVGgxZFhXemNhRWdQaU9vMkdCcTRKWFNvYnFaSnk2NGRGZzFOUmVtQVhvWC1RWmRKa3VQYV9maVdxeXBMRk1n?oc=5) <sub>재경일보</sub>
- 📰 2026-11-25 [Zoox begins driving its purpose-built robotaxi in Santa Monica](https://news.google.com/rss/articles/CBMijAFBVV95cUxNSU55dTlpUjVzSzJjU3NSSS1FdmJxcGo4clpJbklsZWQ3alB6NXZmT0lOelFzS25aYW40VmRMeDFfOURoX09aeGFGdl90V09NSTlaVWdnUjNsekZlTXNSNTlHeHJSUWItNDdFM0xKaXhES3psY1UzZnA5MHJDSVI4VHJad2JnYURDZ2xYcg?oc=5) <sub>Santa Monica Daily Press</sub>
- 📰 2026-11-25 [Motional retools for the robotaxi race](https://news.google.com/rss/articles/CBMicEFVX3lxTE9OODFESWJPQWc1cnNIVVlaSVU2NXZSMEJETzBfOVB4eGdGcTJyaEt5VkRJbWxtUHpRdFJmVDJKR3JONVduSkdfc0pfLVp5RTlFejM0R0lfR1h1RS1ZNEFwSnluUzJiblJyS1dwZjdVT3A?oc=5) <sub>Axios</sub>
- 📰 2026-11-25 [Motional prepares for Uber robotaxi launch in Las Vegas](https://news.google.com/rss/articles/CBMihwFBVV95cUxNZndrdzVJUDJpY3I4VzctSDBMVzA2VWNjU25uRVYwa2FTSjhkU0IwQkpLcFRlSWRCbnBwTUJMWnJMc2Y0MnBhTzdueFRLQVdhWEdLSW9ZZ3hIXzR0Ml9uMkgtbGZteXhvcWxvOXFoU0lrNEdLSGVGczRQVGFpNW1RYXNZN1FTdEU?oc=5) <sub>Mezha.net</sub>

</details>

<details><summary><b>comma.ai</b> (1)</summary>

- 📰 2026-11-23 [Open Source Drive by Wire Kit Retrofits Standard Passenger Cars for Autonomous Research](https://news.google.com/rss/articles/CBMisgFBVV95cUxOYkF5ZVN3eWtSa1FRSnF4Z091VFZlQ2pwZHIybWlxRHhMRXdwWFZMQk43QUNTc3d2VkNRbmNuSGxKUXh1Z0JMN1BfeHFqbFRtM2VnWldHeE9TQ0RVYThPVEpvTnpESTVYWEJZWlJDWWRqbVFYM1dTdFRkWklFd014a2N1d0ctbjlIQy16VW1YYnh1bm1rSmdOdHJvb0JGN1FTbVMzM2F0RUR5RF9SRnNfS1Z3?oc=5) <sub>Bioengineer.org</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
