# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-11-27 · 1,324 papers tracked · 51 curated.

**Selection rule.** A paper is listed only if it (1) is primarily about autonomous driving,
(2) has public code, and (3) shows at least one strong signal: accepted at a top venue
(CVPR / ICCV / ECCV / NeurIPS / ICLR / ICML / CoRL / RSS / TPAMI, or ICRA / IROS / AAAI / RA-L),
≥200 GitHub stars, ≥3 citations / month, or a well-known lab with traction. Papers are then ranked by a
composite score (venue, stars, citation velocity, LLM rubric for novelty / rigor / impact, SOTA claims)
with a per-topic cap. See [`scripts/rank.py`](scripts/rank.py).

📅 [Daily digests](daily/) · 🗓️ [Weekly digests](weekly/) · 📦 [Raw data](data/)

## Contents

- [VLA / VLM for Driving](#vla--vlm-for-driving) (15)
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
| [AutoVLA-D: Learn a Trajectory-Geometric Condition from Reasoning for Autonomous Driving VLA](https://arxiv.org/abs/2611.12382)<br><sub>Yuguang Yang, Zhewen Tan, Canyu Chen et al.</sub> | NeurIPS 2026<br>2026-11 | [⭐ 45](https://github.com/ShivaTeam/AutoVLA-D) | Autoregressive VLA planning usually predicts continuous trajectories as the final output, but driving instructions often describe actions rather than ego states, which weakens direct conditioning on the final continuous … |
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
| [GRAVA: Grounded Reasoning-to-Action Representation and Learning for Autonomous Driving](https://arxiv.org/abs/2609.15169)<br><sub>Xiao Liu, Haoyu Li, Jianghao Leng et al.</sub> | arXiv<br>2026-09 | [⭐ 488](https://github.com/AhernResearch/grava) | Driving vision-language-action (VLA) models increasingly reason before acting, but their intermediate reasoning is often weakly grounded in physical scene evidence and loosely connected to executable behavior |
| [Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air](https://arxiv.org/abs/2605.31066)<br><sub>Tianle Zeng, Yanci Wen, Xueang Yu et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 1,144](https://github.com/louiszengCN/CarlaAir) | Recent aerial vision-language-action (VLA) models show promising single-UAV capabilities, such as tracking moving objects and navigating to language-specified landmarks |

## World Models & Generative Simulation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Orbis 2: A Hierarchical World Model for Driving](https://arxiv.org/abs/2607.15898)<br><sub>Sudhanshu Mittal, Arian Mousakhan, Silvio Galesso et al.</sub> | NeurIPS 2026<br>2026-07<br>📑 3 | [⭐ 32](https://github.com/lmb-freiburg/orbis2) | Current world models operate at a single level of abstraction, with most prioritizing perceptual fidelity while lacking the spatial reasoning and semantic understanding required for real-world downstream tasks |
| [FrozenDrive: Zero-Shot Text-Guided Driving Scene Generation and Data Augmentation with Parameter-Free Frozen Diffusion Model](https://arxiv.org/abs/2606.20110)<br><sub>Yuhwan Jeong, Hyeonseong Kim, Daehyun We et al.</sub> | ECCV 2026<br>2026-06<br>📑 1 | [⭐ 9](https://github.com/daehyunwe/FrozenDrive) | Synthetic data for autonomous driving is surging, powered by diffusion models that promise scalable scene generation |
| [MESSENGER: Memory-Enhanced Sequential Scene Flow Estimation via Autoregressive Next-Frame Forecasting](https://arxiv.org/abs/2610.10759)<br><sub>Jiuming Liu, Jianing Li, Mengmeng Liu et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 0](https://github.com/liujiuming123/Messenger) | Scene flow can capture low-level 3D motion displacements in dynamic scenarios |
| [ASTAD: Asymmetric Style Transfer for Synthetic-to-Real Adaptation in Autonomous Driving](https://arxiv.org/abs/2606.29286)<br><sub>Dingyi Yao, Xinqi Zhang, Lihui Peng et al.</sub> | ECCV 2026<br>2026-06<br>📑 1 | [⭐ 2](https://github.com/Dingyi-Yao/ASTAD) | Synthetic data mitigates the data scarcity problem in autonomous driving perception |
| [Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends](https://arxiv.org/abs/2606.01164)<br><sub>Jiuming Liu, Chaojun Ni, Mengmeng Liu et al.</sub> | arXiv<br>2026-06<br>📑 10 | [⭐ 252](https://github.com/liujiuming123/Awesome-Interactive-World-Model) | With rapid development of large language models and diffusion-based content generation, world modeling has attracted increasing research attention, benefiting various downstream domains such as game engines, embodied AI,… |

## End-to-End Driving & Planning

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [UNIVERSE: Unified Video Action Models for Autonomous Driving with Flexible Mask-Modulated Modality Generation](https://arxiv.org/abs/2607.05133)<br><sub>Mengmeng Liu, Diankun Zhang, Jiuming Liu et al.</sub> | NeurIPS 2026<br>2026-07<br>📑 18 | [⭐ 6](https://github.com/xiaomi-mlab/UNIVERSE) | World Action Models (WAMs) can improve action generalization in autonomous driving by learning scene dynamics through dense future-video supervision |
| [MOJITO: Modal Joint Learning for Unified End-to-End Autonomous Driving](https://arxiv.org/abs/2607.23511)<br><sub>Zhijing Cheng, Xuancheng Zhang, Donglin Di et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 31](https://github.com/mumucc01/MOJITO) | End-to-end autonomous driving systems commonly follow a cascaded two-stage pipeline where a perception stage compresses multi-modal sensor inputs into a compact context and a downstream planner predicts trajectories cond… |
| [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](https://arxiv.org/abs/2609.26792)<br><sub>Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.</sub> | CoRL 2026<br>2026-09<br>📑 1 | [⭐ 15](https://github.com/VAIL-UCLA/DreamStream) | Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions |
| [DriveMLP: When Training Strategy Outperforms Model Complexity in Autonomous Driving](https://arxiv.org/abs/2610.29676)<br><sub>Alessandro Canevaro, Julian Schmidt, Hang Yu et al.</sub> | CoRL<br>2026-10 | [⭐ 6](https://github.com/alessandro-canevaro/DriveMLP) | Learning motion planning policies that remain reliable under closed-loop execution is a central challenge in Autonomous Driving (AD) |
| [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)<br><sub>Shen Zheng, Anurag Ghosh, Gaurav Parmar et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 32](https://github.com/ShenZheng2000/WarpI2I) | Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs) |
| [G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance](https://arxiv.org/abs/2606.26017)<br><sub>Hang Yu, Ye Jin, Alessandro Canevaro et al.</sub> | IROS 2026<br>2026-06<br>📑 6 | [⭐ 7](https://github.com/HangYuu/G2DP) | In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors |
| [DriveZero: End-to-End Driving Beyond Human Demonstrations](https://arxiv.org/abs/2609.06055)<br><sub>Hao He, Chengcheng Hu, Zirun Su et al.</sub> | arXiv<br>2026-09<br>📑 11 | [⭐ 151](https://github.com/XiaomiAutoL3/DriveZero) | Most end-to-end autonomous-driving systems learn by imitating human driving logs, leaving their learned behavior constrained by the quality and behavioral coverage of the recorded trajectories |
| [SimWAM: A Simple World Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.07468)<br><sub>Zongchuang Zhao, Xin Zhou, Tianyang Xu et al.</sub> | arXiv<br>2026-08<br>📑 27 | [⭐ 216](https://github.com/H-EmbodVis/SimWAM) | In autonomous driving, World-Action Models (WAMs) have improved end-to-end planning by transferring video dynamics priors to action prediction, but many still couple planning with future-video generation at inference, in… |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 23 | [⭐ 372](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
| [Latent-Centroid Steering: Single-Pass Classifier-Free Guidance for Command-Aligned Autonomous Driving](https://arxiv.org/abs/2608.00237)<br><sub>Meibo Hu, Jiamian Wang, Pichao Wang et al.</sub> | IROS 2026<br>2026-08<br>📑 1 | [⭐ 2](https://github.com/codingmlinprocess/LCS) | Vision-language models (VLMs) have recently emerged as a promising paradigm for end-to-end autonomous driving, enabling agents to map multimodal inputs and high-level navigation instructions directly to executable trajec… |
| [STAGE: STyle-controllable Action GEneration for personalized autonomous driving](https://arxiv.org/abs/2607.29517)<br><sub>Zihao Liu, Xing Liu, Yizhai Zhang et al.</sub> | RA-L<br>2026-07<br>📑 1 | [⭐ 5](https://github.com/CarlDegio/STAGE) | Driving style refers to the behavioral preferences that drivers maintain during driving, shaped by their diverse experiences, habits, and needs, and is typically reflected in varying levels of aggressiveness |
| [WA-JEPA: Rethinking the Video JEPA Paradigm for World-Action Modeling in Autonomous Driving](https://arxiv.org/abs/2608.20974)<br><sub>Xinlin Wang, Yujiao Xiang, Yuheng Zhou et al.</sub> | arXiv<br>2026-08<br>📑 13 | [⭐ 91](https://github.com/AFARI-Research/WA-JEPA) | Video Joint Embedding Predictive Architecture (V-JEPA) learns powerful spatiotemporal representations from video through self-supervised latent feature prediction |
| [A Survey on End-to-End Autonomous Driving Training from the Perspectives of Data, Strategy, and Platform](https://arxiv.org/abs/2610.00926)<br><sub>Chengkai Xu, Yiming Cui, Jiaqi Liu et al.</sub> | arXiv<br>2026-10<br>📑 7 | [⭐ 111](https://github.com/Jiaaqiliu/Awesome-Training-Ecosystem-for-E2E-AD) | Autonomous driving is a cornerstone technology for the future of intelligent transportation, where end-to-end learning has emerged as a transformative paradigm that directly maps multimodal sensory inputs to driving acti… |
| [AutoE2E: Don't speak - Language free end-to-end autonomy for L2++ ADAS and L4 Robotaxis](https://arxiv.org/abs/2611.22374)<br><sub>Muhammad Zain Khawaja, Zaynab El Mawas, Ryota Yamada et al.</sub> | arXiv<br>2026-11 | [⭐ 238](https://github.com/autowarefoundation/auto_e2e) | AutoE2E is an open-source end-to-end driving model developed by the Autoware Foundation Robotaxi Working Group |

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
| [DRS-VPT: Directly Relocalizing in a Scan with Vision Point Transformers](https://arxiv.org/abs/2609.12557)<br><sub>Lanke Frank Tarimo Fu, Maurice Fallon</sub> | ECCV 2026<br>2026-09 | [⭐ 29](https://github.com/ori-drs/drs-vpt) | We present DRS-VPT, a feed-forward transformer architecture for foundational image-to-scan registration |
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
| [CCFM: Collision-Constrained Flow Matching for Safety-Critical Scenario Generation](https://arxiv.org/abs/2607.04451)<br><sub>Ke Li, Kaidi Liang, Yuxin Ding et al.</sub> | ECCV 2026<br>2026-07<br>📑 1 | [⭐ 3](https://github.com/KELISBU/CCFM) | Evaluation of autonomous vehicle (AV) planners in safety-critical closed-loop simulation is essential for real-world deployment |
| [CADET: A Modular Platform for Evaluating Distributed Cooperative Autonomy in Connected Autonomous Vehicles](https://arxiv.org/abs/2606.04072)<br><sub>Pragya Sharma, Brian Wang, Mani Srivastava</sub> | ICRA 2026<br>2026-06<br>📑 1 | [⭐ 0](https://github.com/nesl/cadet) | Deep learning models are increasingly central to autonomous vehicle (AV) pipelines, yet their integration has traditionally followed a monolithic design where perception, planning, and control execute on a single onboard… |

## 🏢 Industry Tracker

Latest 14 days of news, official blog posts and new open-source repos from tracked companies. Full daily feed in [`daily/`](daily/).

<details><summary><b>Waymo</b> (253)</summary>

- 📰 2026-11-27 [The vehicles that shaped Waymo's robotaxi fleet, from desert racers to luxury SUVs](https://news.google.com/rss/articles/CBMijwFBVV95cUxQZThJY0FIWE5EYW95R1ZrV18tbjJMMjYtclVrdUZhd05fbWRPZFFsRmg2dEdnU0xWa0pMZnV5YTRIUW4xbkNsNGx6THluUWluMFl5S0JmdFBZSkhxX0ZNb3JWX3l5RmlNR0F1Z3pPbXNXZVJfeWhHTFZVS19hRDk3TEtmRmRpbFMwX2VqdUZYaw?oc=5) <sub>Business Insider</sub>
- 📰 2026-11-27 [With Cones and Eggs, a Denver Man Keeps Trapping Waymos](https://news.google.com/rss/articles/CBMiYEFVX3lxTE9tMUlEeXdIZF85VldvdTlxX05IRmVlMTg4OWhjZUdtVGJtMUtJVGxTZkJzSUE4djJtODcydGM1UFhad0hPQmJfbzNPZnNLMmJ4Y0FGeTZXX2V3MmstSWl0eQ?oc=5) <sub>www.trendingtopics.eu</sub>
- 📰 2026-11-27 [Waymo Robotaxi Attacked: 30+ Eggs Hit Car in Denver](https://news.google.com/rss/articles/CBMikgFBVV95cUxPT2NFLXhRMHRiMGNVNUlMbEpwcUpJLUpObEFzRDdWbjUtUGc1R3kwX19aaTdEME5pRGg5OVRNaGx4UldOUjQ1Q2poQm15eGRGMy1qc3pHb3AwMlAzTHBXbnd6a2c5dkpfbTZKWml0a1o0akEtUEM2QzRzeGRlb0NoSXloRlR0T3BsWEZRYl9IendrZw?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-27 [Texas Autonomous Vehicle Law: 2 Bills, No Crash Reports](https://news.google.com/rss/articles/CBMimAFBVV95cUxQZFNjVUpUWFNyVlFCVnUzMVdvMTlMaDFKbEdiV29rbGZJcnFqV284N1ZIQ2laaTR4ZERUU3habjdmM1JQUGE0eklRWkxQVDFhSzZ4OVd1WG5udzM4UENGUjNpTXpyLXdIckVXRmZtckhmaVVDeVF3eS1IaWhwOFZFVTZrcDV5Qkt0UTQyeXNfZjZkRlhQUHM2TA?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-27 [Google's Waymo says egg attacks took seven cars out of service after a Denver man allegedly blocked them](https://news.google.com/rss/articles/CBMiowJBVV95cUxNRTN6bTN5YjcxZ0dEaV83dC1CVURKT3ZFak00dG16V3dDVHRRb0FJSHpoWnN6X291M2g1TzdJQjJsalVzdGxjeXdqNnlleWFja3FOSXJUd0dFaXE0VVNYREI4T2JVWTZ4eWF4V0ZRRDBTallTeEIzMjdZRkUwYzV2cFlRQ2R5M2pxY1EtM0M2bG1ZOXN4MVhsTlRBenkxM2REYnZlNDZvTWdxUUVBOVZidFpTa21zRkVLXzdyb3pEeWV4SEZnX1dRRHFzdFdTdVZ2SWkwMGx3aVJKaHRlckVqcEhhMHhEcFF5Sk5LVThBZmJCSzFBVzZGUjJaLUNQeVY0a0VMVUk2TDh4Vkx6RWozSExMVjFaeXQ2RE9QZ2prWGZKd2fSAagCQVVfeXFMT3ZwUGFZbmVhUXdjRWNRWDZXUEE4WGZXZF9WRGI1bVFBbVJJNnBDU0w4aXJLRDYtazB3dm5KaWRQZ0pwYTFfc1dmekJhVDF2UlBURUNCUDlNQTlKbnBDNUhRaHRFR0Rha1ZwWXlXa1ZoSVA5cWE4aVhoWTFLZ1JMTzd5SjNvY3J2MlhWaTg0NGQ0VmxGZm4tQkpJZ0NXYV9BbE1WbGJMcjF4OXprd3kwSTNydHJZLTdoRXZnQWdleHU2Z1Vzc1VjRF8zU0ljYzFGaDk3TG5aR005TmtEdWxkMzdtTllqNklxSU5WUVFvVnpXTTNCRFJneUg1Z1lXbHZBc0RoVDZQSjZTdDhxVjdkdFpDdGJaaHE3M1U4UmhoQVRHTXVnSENHRG8?oc=5) <sub>The Times of India</sub>

</details>

<details><summary><b>Tesla</b> (389)</summary>

- 📰 2026-11-27 [Tesla 2026.44.3.1 Rolls Out With FSD v14.3, Battery Preconditioning](https://news.google.com/rss/articles/CBMia0FVX3lxTE04N1A2cVN4ZmRkb1RGMmgxWDM2ak1aSFZfOEZfdVJMYjY3WmdidjBfODBlOGNQb0luVFVGYjJJRTluUDhCdi04WmVjejBKTVc2WlpUZV9FajE4VXJ6ZU5kTjJEVFR1eW5yLUY0?oc=5) <sub>BASENOR - Tesla Accessories</sub>
- 📰 2026-11-27 [Tesla’s latest FSD update adds camera-based visuals, pothole and animal detection](https://news.google.com/rss/articles/CBMimAFBVV95cUxNQ2ZYeFB4a19vaWQ3eEFXWk5YdDdjQjRua3NKSzdnNTlQdzZrTXVGRVB3VHVKZkpyQzNhbm1xaG9VeFNWVXNha0lxOUw4YkFsZlpyakdXRnlQQ3g4bGlKYXpIdFFTRWFLYzFsWi1YYVo4U196bDBIQXdTS2lWZWQtc3h1MGczZl9ZMVJ1MWsxR0U0QW9uaHR6Tw?oc=5) <sub>Drive</sub>
- 📰 2026-11-27 [@wongmjane says Tesla Robotaxi can be sent into San Francisco’s flood zone](https://news.google.com/rss/articles/CBMiREFVX3lxTE91RGo5ZlNucVZrVTVJTkNQUDZqNEl6VDlBQWFuZkU5bjhTY2IwWUFSVTJabllKWlpqa2pkc2drNURUYXZC?oc=5) <sub>Digg</sub>
- 📰 2026-11-27 [2026.44.3.1 Official Tesla Release Notes - Software Updates](https://news.google.com/rss/articles/CBMiO0FVX3lxTE5tbkJzcEhvTlRyMW9uNnpkQmJFcUs3MEEycV9XMkVYaGZYM1RKMmFsQ3gwV2xuek9CLWFN?oc=5) <sub>Howl.Link</sub>
- 📰 2026-11-27 [Tesla Expands Dallas Robotaxi Service Area and Adds 285 Cybercab Robotaxi](https://news.google.com/rss/articles/CBMitwFBVV95cUxNcTZ3MmZXLUt3V0ktV0RuREtXcnF0UmdpQ2o3UG5CREQ1eVlrTXk4SFFYTU9rYW1Nc0pQUWZhQ3NxVkI5WENWNUVydGlRSEtHRlh2cktlaURIcTNtZERhM1oyXzhhRHVFODQzMlZlVTFqNTVmU3V6YTlKLXNjTUFtSGpYQk9hVktIZi1VMnFmbmZmR1g1VTdqRDBSeXZmQmNVZ1gzR25BQXV6bUdsYWVkV3hIM1d5eUk?oc=5) <sub>NextBigFuture.com</sub>

</details>

<details><summary><b>NVIDIA</b> (227)</summary>

- 💻 2026-11-19 [NVIDIA/nvidia-linux-utils](https://github.com/NVIDIA/nvidia-linux-utils) <sub>GitHub</sub>
- 💻 2026-11-16 [NVIDIA/scadactl](https://github.com/NVIDIA/scadactl) <sub>GitHub</sub>
- 📰 2026-11-27 [NVIDIA Releases Autoregressive Image-Generation AI for Free, Challenging Diffusion-Model Assumptions](https://news.google.com/rss/articles/CBMidkFVX3lxTE5lUFRLRVlDa2ZGOS1mQXAzYzY1bmp5c3psSFlXLTQySnZJa3V0LTAzNDBjNHdTMlZyRi01ZS1QNUtoWHp4UDN5LWdUMVdKaWh2MloyRWFnbW5fcmdEdVVlNkNKLWVTbjhzaFVQVk8zaGVrNHRNRHc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-27 [Kioxia's GP2 SSD tops 18 million IOPS for direct GPU memory access](https://news.google.com/rss/articles/CBMijwFBVV95cUxQa2IxSE5aTzBXWWZEcHFzR0dVTDlfTG5lTVhNVTdaYTdmcnBxcFpBaWFVSkhiZFlXTFpqNjVCYUdGdE9lQmVOWEhaVy13S01BV2JIQVF2UnphbW1ZWjZTT2Q2Qlg3UExVYXo2bzVMUEZwY2RjamxNcFFVbTRpS2gwRUVKaHpxRmxyR1JZV1Nqdw?oc=5) <sub>MLQ.ai</sub>
- 📰 2026-11-27 [Take Five: A December to remember](https://news.google.com/rss/articles/CBMifEFVX3lxTE1xbm9TQ2lmZmw2azNhR0hPNnJqRm53VU1zeVpTMDRzV1BNdEtEUXdNRy1mSFhfd0IxenBKXzZFZWF1aFItWVdfVFZxamZoQnhmS3ZCb2ZQTEdOTE9Oc1k0R2Y0bWdBLVRfU3hkNVdoMHRUQzE1amtuOHRxODY?oc=5) <sub>93.3 The Drive</sub>

</details>

<details><summary><b>Wayve</b> (28)</summary>

- 📰 2026-11-26 [Transportation: Europe’s 10 most-funded companies in H1 2026](https://news.google.com/rss/articles/CBMijwFBVV95cUxOaGZzS19fUHdTZm93NGdZVU5oMGFmR2lOV3dvSFR1bTNHM0RMR3lyQzVKRnl2Rmk5eFRla0puMWtQaW9TbEhRN3NzVzV6RmNnVE42SlZTT2ZLZDVqaVk2R29hRlVKV3BRX2lJNHZhMzdYbHhWRXktVWFTSFJ4VjVjV3A5YXFWMVljeEI5X0Zkbw?oc=5) <sub>Tech.eu</sub>
- 📰 2026-11-26 [Why data, not distance, may determine winners in autonomous driving](https://news.google.com/rss/articles/CBMif0FVX3lxTFBHem93SFVRQXJ5OTdlSXNqY0xwTWpGY054cmdBVThPNU9LRXVRdHItSjhuLUV0MUZlQUM5a3NVM3AtWHZJZDM5ZHpLaVlIVFdOUi1fOEdybDZCck42Sk1pTDZPaUt4OGxOazFUUFdVRlpBX2dwSExjaFRXem1SUXM?oc=5) <sub>Automotive News</sub>
- 📰 2026-11-23 [Autonomous Driving Software Market to Reach USD 6.78 Billion](https://news.google.com/rss/articles/CBMinAFBVV95cUxNZFVjLThIaVVwbm1rWlBYT2IzMDFFZEF6LWVzaWY1YTR6b0JLeDBla0VacjF0dEtpQjhGblZpVjUyZV9ZM3lSS3UwdFdtYmp0dm15SzdBZnpEemNqMlcxMXZ4TnVDV3FqZjNCOGdWNFhBRGFUWVNlV2poZHFkdDA1OEY1QlZaZzZ6Z09QQWtTRDQ5WGxyV2xmbEtxOHo?oc=5) <sub>openPR.com</sub>
- 📰 2026-11-23 [Mercedes gets edge over Tesla in race for self-driving success in Europe](https://news.google.com/rss/articles/CBMihAFBVV95cUxNREhrZGszRlNBUzFxbjBURFBhQldOMDFiOGV0TVNMWWVuYjA5dFdCTGpGV0RCMlJJczEtWkd0eG9YRnkwZnFVTFRseC1iT1lBM2w0LUlUVFhqdk1ydU1vWDRPVGZfTlE4SnRSRnZZTkMzVzdnVFJTM0dobnRKRG1jOV9Yb0w?oc=5) <sub>Financial Times</sub>
- 📰 2026-11-22 [Kakao Mobility partners with Nvidia to develop Level 4 autonomous driving technology](https://news.google.com/rss/articles/CBMi2AFBVV95cUxOUnMwVTdET0JiaXlkcm83bUZkQUt0TFpJd1lkZG13a1JIUWl3dW81UXlGbHN1Q2Z4VDZGVE5GcFNmeTRsNG1kODJpTTJCclVueHQ1LVFTOTFFWUVpRUpQYmMwc0ZSUHJqN05IR292WVBsOTFUMDl5VldhWUd2UkRfd1NXZ1BQcnI2TFFJdmx1cHN6RFY3aWl0VnppeUxYV2xPWjdZRWRJVzkwWFZ6SWdXQ3FLdTNLMFE5bTRMUkZRRWdlamhhT3ZZNXVOLW5LbnVaX3h6STh2VGM?oc=5) <sub>Robotics & Automation News</sub>

</details>

<details><summary><b>Momenta</b> (126)</summary>

- 📰 2026-11-27 [The 2027 Nissan NX7 Is An Impressive PHEV That May Be Coming To The Philippines](https://news.google.com/rss/articles/CBMigAFBVV95cUxPZmxRdEhXQlZkN0Vvalg3LWdjdzV6NjR0Q0lDM05DRWNfY2Fya3M1WGJQeHRaS09IWFUyNTltNl9QTmFWUzRyQ3dndUdKckhkS0J1U1g0S0tKNTlRQnltNGRNU3hVaDRKRkhPS2pMbUVaay0ycldPaUxteU9jbWppMg?oc=5) <sub>CarGuide.PH</sub>
- 📰 2026-11-27 [奥迪E7X领衔亮相广州车展，搭载Momenta R7世界模型实现Door-to-Door全场景智驾](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1rZ09uVXRnY3MtNkFkckpBZW9VNmp1MUZ0RnBWVGJPZWRKU3BoUXlQdk9wUnkwVzhIOEJ6N0VWNS1wOHUzdTZ1R05sUml5OVloTDhhUm1XdEUyam5zYUE?oc=5) <sub>SmartHey</sub>
- 📰 2026-11-27 [东风日产NX7上市，限时权益价11.99万元起，配Momenta R7智驾](https://news.google.com/rss/articles/CBMiUkFVX3lxTE55dVJZd2pLeklXcW5vNmxlV0RMMEh3SDR3Mmk4MTduVW45SkNDb1JPeVdDZHFMZ3pxN2VmZmVjd19HZzB0a3N3NnhMTThZS2dhbXc?oc=5) <sub>凤凰网</sub>
- 📰 2026-11-27 [全新奔驰纯电 GLC SUV 上市：限时 25.49~36.22 万元，标配 800V 架构与 Momenta 智驾](https://news.google.com/rss/articles/CBMif0FVX3lxTFBsRmU2ZTFkdm9SVERodC1lNk5KS3RQQWwzTU9YR3lsM3VlRVpfYVVqOTRkekswTDJGYmRzdHdqYjBoWnJWU2Fnd2NBSDJPV1QxOGZlSFAxM1FQakZkbDZFY3JlWExSd0ZqNGowQWZJTjd0S1NUN05UNWpVRExpVG8?oc=5) <sub>新浪财经</sub>
- 📰 2026-11-27 [电子后视镜配上世界模型智驾，这台混动冠道有点东西\|Momenta\|广汽本田\|混动冠道\|Momenta R7\|广州车展_新浪新闻](https://news.google.com/rss/articles/CBMiY0FVX3lxTE1zUmUtaGx1a243cUlGb1phaWcxNE5GUTRCeWNqeC12bFg1VjRhVDB6NHVlQU9BZ2pUN1JmcnZIdmxyVl85dnZiVTRGVGk0Nk1XVFdOZTk1R1BHY21FQXhfX056TQ?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>XPeng</b> (257)</summary>

- 📰 2026-11-27 [The Liability Gap: Why XPeng's Autonomous Driving Claims Don't Add Up](https://news.google.com/rss/articles/CBMilwFBVV95cUxNUUtEc3JWUVNVODZGSEw4VlY3enNTa2lfbmpDUFZ1YklIRGxERVNuTnBVNjZUa3Z5ZzY3S3QwU01hQVlqM2FKajY0cm91TW82REJTNEJWNnFzQXJMUGlKRlN4LVVyRWZJay1CT0RsZ3ZyMUltWDFuS0pNRHJsdUM4ZzRlaWEtU1pNMzhfNmtZZTJFQ2Q0elJN?oc=5) <sub>Vocal</sub>
- 📰 2026-11-27 [XPENG Accelerates Global Physical AI Expansion at the 2026 Guangzhou International Automobile Exhibition](https://news.google.com/rss/articles/CBMigwJBVV95cUxPNnBDMml5eGJRNjhoclVTeENKc0EzR3VrM0tfalhKbzczbHNHNVlYN2ZQMXNPV2twMHZRcW9lOFNJb21xbE5WclhUU002a0t6SlBLMGE0eHJpSDVGdkdfWlhRMDNYUUg4NFhCZ1ZuQVF3WUJjSzMtSmZxMTFkWllXNl8wR0VVdXlCaHNPMVVObVQwNEdtVHdnTi15UGxJMEpRaFNNNHJkVTFsV1FYbmozYVRrbkYzc1lrZkg5NGZXMjJ5UXl4Zzl6QVBlRHZ3bFRWc1AyWFhLMmtaU0x1MGJiclYwLWJiY3l5aFEyLXBjdnNRNWYyNl83SkJMdVBTbXFBZWw4?oc=5) <sub>FinancialContent</sub>
- 📰 2026-11-27 [XPENG targets more than doubling overseas vehicle sales in 2027](https://news.google.com/rss/articles/CBMioAFBVV95cUxPMjFHd29KOHEyZUx1RkhBTkdnYmw5TlBGcWtxb0lkN3ExdTVXUzVGMjhueVJDTmxCaHdBMkRHMElIU3J5MElma0RhNFVtQmVZbTUyNElCb2M4enZrNVhBUFZyMkZseGx5bGFSaU5kdThDOVA2UzB4eE00cFBKOWFDLWQ1UDNLQy11RDIwN3ZRNzVlaDRhd0tIVHVtX0JkeElT?oc=5) <sub>grafa.com</sub>
- 📰 2026-11-27 [BofAS: XPENG-W Investor Day Focuses on Commercialization of Humanoid Robots and Robotaxi](https://news.google.com/rss/articles/CBMi3AFBVV95cUxNTUVQQTQwcHRQc21JWGxxQmVQMGRBSXNxdW5QUnQtZGZVbllBeTlaeUdiLThkTUQyQlJqLWdiWGlnczdoMWRDRFdQWE1MeUlTUGFjR0FQTWpsRDNac0dnYmVYNVNEeWVweXRLdmdLdlZEc1VmNlgxR1VHRFVSbnNEbkRWSkM2akVUeElEQVhnS0dJNWdJbUJkM1BweWNRWThORXZqLTF4dl9mZE1FdFlILVh1bEp1eDkzZ2tZVFZkaU9ZcmtSMVlfV0VRTnJvVHRNZFZPMFZZam5iaUM4?oc=5) <sub>TradingView</sub>
- 📰 2026-11-27 [XPENG unveils global expansion with humanoid ro...](https://news.google.com/rss/articles/CBMiogFBVV95cUxONnVsS2pWVEdEQ3NjM1pOSy1vaU1tQlU3SXJKMlRTaUxMVGlzblZlUWFaakEwT0hOX0NNMV9Fd2ZPMlM1RHJ6bjdaY0ZwekNTN1VFQjhSQ05UeERQaDhIOTF5ZXVtQXlNRXhJUjNOVmNxZ1o0eVJiM3dFeUpJOE13YnNOU09LSndSUW53cTk3c3lHMUV4Ynp4OTlGVkhHa2l3a2c?oc=5) <sub>Pluang</sub>

</details>

<details><summary><b>Li Auto</b> (182)</summary>

- 📰 2026-11-27 [NIO's William Li: No Blind AI Labeling, Long-Term Gross Margin Target Raised by 10 Percentage Points](https://news.google.com/rss/articles/CBMidkFVX3lxTFBRZlF4bmZIM1FpakZtZjdiMG9mcE5UNF9tdnZicnEzUXdMZU9OVF9FUEUzZjQ3MEFacE1wMnRZLTNOLXhDdFVBX3RVVEdPcGpEWDdmNHFsQzd1d3JXSHBaYlR1VXdGYm84ME9FLV8wOEV4WENycnc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-27 [Nio expands best-selling SUV lineup with launch of ES8 Mirror Black Edition 2.0 at Guangzhou Auto Show](https://news.google.com/rss/articles/CBMikwFBVV95cUxQVEVXTlNDOW4wMDRWUzRXa3NSXzdZTTlUU3MzOFh6Vl81ekM2UlZMb3pVRlQwdkhhMDhsSWhEU21yWGVzZXM1emNSOHZ2Y0pTQzUyTUgwRmF5b1JjYW8tWnhKWFJFOUZZb0E0alNHdjFvbWdidTRNQ2tvZGc0SktJYmpGU241RTljRnFHeW9YbG5tYWc?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-27 [Hongqi H9 plug-in hybrid launches at 329,800 CNY with Huawei ADS 5, holding pre-sale prices](https://news.google.com/rss/articles/CBMiwgFBVV95cUxNcm04a0N2X1JEMXhFc295YzhDUW91bUZrVTZWWHhDUjMzakJnXzNJQ01sVjFRNnoyUWYxYndVSGpZT3FsUm1pTGpNeDJzMW5EcEpBQ1o4UTNUZDkxSGtLcTdTQW5YT3hTVXFqUVdOYnhFcll6SzZfRE9GVTZXWTRWRDNKU1Q3aFc5c1RValVwT0dPTEVtdDUtZndwMUF1R3BWS1l6YjFONi1VNzliMjQ5ZjU5RkxKbmZ3eTBVMnBLRER0QQ?oc=5) <sub>GlobalChinaEV</sub>
- 📰 2026-11-26 [NIO to Deploy 7,500 AI Agents, Targeting 10-Point Gross Margin Improvement](https://news.google.com/rss/articles/CBMidkFVX3lxTFBscGt1ZVRmeUpmajZpOGVkOE92R3dydnBzYzNWaHdEd1BpYmNaX1hLME1ZY0h3cUVfMnZkQnRwd0QxQThqdXpRRW56SEkwUjJzcms0YnI5cHR0SDZEdHRQMjFCeWhTZjhFLXJkU2V3OHVLTHFtUXc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-26 [带你了解2026小鹏科技日：说了那些话和展示了那些产品？](https://news.google.com/rss/articles/CBMia0FVX3lxTE9zbDhVLVBPOFNXMkk0VFVWeVZSNk40NWs5cDZMU1JEVVlGYnBNWU4zdHJLanpYWm50X3ZydmtRckF4TDdCWkhLcmp6ZTZ3U093elpSZjhmMzliMG1BTkV2NzUycXlTX2k5WldJ?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>NIO</b> (204)</summary>

- 📰 2026-11-27 [Nio expands best-selling SUV lineup with launch of ES8 Mirror Black Edition 2.0 at Guangzhou Auto Show](https://news.google.com/rss/articles/CBMikwFBVV95cUxQVEVXTlNDOW4wMDRWUzRXa3NSXzdZTTlUU3MzOFh6Vl81ekM2UlZMb3pVRlQwdkhhMDhsSWhEU21yWGVzZXM1emNSOHZ2Y0pTQzUyTUgwRmF5b1JjYW8tWnhKWFJFOUZZb0E0alNHdjFvbWdidTRNQ2tvZGc0SktJYmpGU241RTljRnFHeW9YbG5tYWc?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-27 [NIO's William Li: No Blind AI Labeling, Long-Term Gross Margin Target Raised by 10 Percentage Points](https://news.google.com/rss/articles/CBMidkFVX3lxTFBRZlF4bmZIM1FpakZtZjdiMG9mcE5UNF9tdnZicnEzUXdMZU9OVF9FUEUzZjQ3MEFacE1wMnRZLTNOLXhDdFVBX3RVVEdPcGpEWDdmNHFsQzd1d3JXSHBaYlR1VXdGYm84ME9FLV8wOEV4WENycnc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-27 [Nio Onvo launches updated L60 Black Knight edition starting at $31,430](https://news.google.com/rss/articles/CBMiiwFBVV95cUxONUZaeTNXbnZsS1JDLW5XbGNDdW1aeFotNXFtTDVISU03OUhxNk0zUXNqZmpNY1BnTjNjTFY5Nll5ZDgxZ0k5NS1uUWVlaGROMWtZVkNJejVfVE5tN0xvUE96WS1qUmRtMlNjMUdKZERxV2JESFpVNWl2WW1uakJFQ2E4VmY5VE5vY2Zv?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-27 [NIO Deploys Over 7,500 AI Agents, William Li Estimates Annual Savings of About 6 Billion Yuan](https://news.google.com/rss/articles/CBMidkFVX3lxTFBWVWFYUm5SMWtVUGFFWWcwQnRfYlJmaHJ0a1VPanNpLUpsem1TRXJLMXZXMWVQMFM4OGR0a2RON1hLM2I0QmFfMk4xRnBJS3ozUEpMUDBuVU9udXk4ZjN5WXcxZ2dnMlNLTklla0hObTdfeUJ3R0E?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-27 [蔚来发布NWM 3.0智驾系统与NOMI 4.0，端侧算力效率与座舱智能体重构](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBoWUhVa1A2T2FoeS02ejVXNGNVdi05UkVRcjlFbkF2amVUQ0QzdVFuSTBlQVZ1cGNnMXB1dXJubzhGdkxrR0E3RENLSmpMMWczcW9FN2RmZU9yTkE?oc=5) <sub>网通社</sub>

</details>

<details><summary><b>Huawei</b> (373)</summary>

- 📰 2026-11-27 [Combined Driving Assistance Penetration Hits 70%; Huawei Qiankun Exceeds 90%](https://news.google.com/rss/articles/CBMizwFBVV95cUxQN2k3V09nWVcyZm84TmVrZENCNzlNQkxZNHFvWl9CVGtEcWJyWWRtVWN6eFl2eU9xamYzelQ4RDVsT1Z1RG53aXhCaVBwVE9COW80NlpjUjlFOU5IRFRFcFJZVkdINk1qbXJDNGIxMkF3NTdteTQwNDhKd2JScUNlOGloaGgwT01BZld1ZjJlWDhrQlFFb2hTVU1LdC1qOXJ6aUtGZ0pXNWhQVXdBTkQycWd3WXl0T0JiS1A4LVByYWY5TlZaUEduS19peEs3NFk?oc=5) <sub>Gasgoo</sub>
- 📰 2026-11-27 [Hongqi H9 plug-in hybrid launches at 329,800 CNY with Huawei ADS 5, holding pre-sale prices](https://news.google.com/rss/articles/CBMiwgFBVV95cUxNcm04a0N2X1JEMXhFc295YzhDUW91bUZrVTZWWHhDUjMzakJnXzNJQ01sVjFRNnoyUWYxYndVSGpZT3FsUm1pTGpNeDJzMW5EcEpBQ1o4UTNUZDkxSGtLcTdTQW5YT3hTVXFqUVdOYnhFcll6SzZfRE9GVTZXWTRWRDNKU1Q3aFc5c1RValVwT0dPTEVtdDUtZndwMUF1R3BWS1l6YjFONi1VNzliMjQ5ZjU5RkxKbmZ3eTBVMnBLRER0QQ?oc=5) <sub>GlobalChinaEV</sub>
- 📰 2026-11-27 [The Liability Gap: Why XPeng's Autonomous Driving Claims Don't Add Up](https://news.google.com/rss/articles/CBMilwFBVV95cUxNUUtEc3JWUVNVODZGSEw4VlY3enNTa2lfbmpDUFZ1YklIRGxERVNuTnBVNjZUa3Z5ZzY3S3QwU01hQVlqM2FKajY0cm91TW82REJTNEJWNnFzQXJMUGlKRlN4LVVyRWZJay1CT0RsZ3ZyMUltWDFuS0pNRHJsdUM4ZzRlaWEtU1pNMzhfNmtZZTJFQ2Q0elJN?oc=5) <sub>Vocal</sub>
- 📰 2026-11-27 [Huawei Qiankun, CATL unveil intelligent battery swapping solution, introduce 100-kWh battery](https://news.google.com/rss/articles/CBMi5wFBVV95cUxOYWFFUGc1RUM3NXlQTnZGZUdwOHFFYVhyU19DUkc4WDc2NjFZMGFrVEVtZUoyVzZNSnJwMXlrUnNmMVJuY3FTNXJyeE4zOHgyU3Z6UWQyUy00LUltYlFfN05NTE1BTUhSNnpUMHRjTmtZNEhDbXFmR3JBbVpGbG0zSEZyaVNFNENUWGhPRTVVWHZzVlBqZ1FPY1ZQeVk2QmJoZjhUcy11Q2c1c2hCblU0RUpQYVgxZnZ4OHhqWVJfckxoTmJhYzhnMmlGbnVsc3RCOFR5bzl5VHdpYVpSZjhJbklRUVlWT0U?oc=5) <sub>Gasgoo</sub>
- 📰 2026-11-27 [Dongfeng's Epicland X9 BEV version launched in China: 102 kWh LFP battery, starting at 41,800 USD](https://news.google.com/rss/articles/CBMiygFBVV95cUxOSmtoWVFUVEpIVEE4TjIzZHU0T1VyN1AySFoyNHA0T2xWeWhSellpUTNMUFdjZmxzMU9BM3ljN1g3VHNuNmVNVEV2RTZVRTRuWHM5eEE5S2kyY2lmSk9yYlFoR1ZvZ1Zid0lTS3p5OHN5U1lvZUp2Z0RiZGhXN2VpUXRRclFBMFBnTXU5bkY5dDVPVEl1VDNKVEcxQXJ3MDd5eTBwYUNXQXNyanlKeE00QlhtOW1lWi1zc3paWGdWWFl6Ymlzc2YtbjF3?oc=5) <sub>CarNewsChina.com</sub>

</details>

<details><summary><b>Baidu Apollo</b> (55)</summary>

- 📰 2026-11-27 [US and Chinese robotaxi markets enter explosive growth; 2026 output value gain at 100%; estimated total at US$850 million](https://news.google.com/rss/articles/CBMia0FVX3lxTE5pSkZtLXVFOEgxMnotMWxJOTNtQ3FHRjdHNjR2LTc0TklSbXp1S0k5S3FtSEY5NmtNWlVPN2xZaTNxTmxiNWxLSVc1SVY5UzZnNl9mZ2Rsazk4SDFuQVhMR0Noa2VvT2VCR2RR?oc=5) <sub>digitimes</sub>
- 📰 2026-11-27 [Competitive Analysis of Autonomous Vehicles Market: Waymo,](https://news.google.com/rss/articles/CBMilwFBVV95cUxNQjdpUFNMQzN3REM5ekNZaV9JUlU1TlFZWWtKb28yNTNRaHFHVjNWM1RxVl9NbDA0Yl9TWGJlOVF0WXVPVHV6VE1kSXJOaEVYcFVFb3RYd08xb19JWFhwUENlaElmV1ZVWjJuMzg4WTJRM2piQ3dUSkhrSHQwYjIxNUc0N0IzcWZtdXlnbnFhUW91eXJXYW0w?oc=5) <sub>openPR.com</sub>
- 📰 2026-11-26 [The Fierce Competition of Chinese Autonomous Taxis in Dubai: Market Expansion, Tech Advantages & Global Layout](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1rNWFaSE9Ed0Z3cVV3WE9aYjc1MW9QWjE1VEZ0cmV5TDZ5cW96TktTWXVrWWlyLUFhWG9pd2YyeFoxWFZteVNtZ0hFamVkOVU3cGhR?oc=5) <sub>eu.36kr.com</sub>
- 📰 2026-11-26 [Hop In, Buckle Up, Sit Back: Everything To Know About Dubai’s Robotaxis](https://news.google.com/rss/articles/CBMimAFBVV95cUxQT20yRnBGODVyb1NLdl90MlZ0UXNTY3lzdVVfSHJweTFla2Rkdk9DbFFFUjFTVEVnWmxlVW1TdzVtQ3EyRzE4YVZBdVJvM2JMZlBJR2pVdmVuYVVxd0VWaEQ4bkp2b0RvTF9KT0hNZldZVW1XanpwWkZkZjJPUzRHdWQtNjZRYmJmTnQ4REttZ000ZUxzUXpGQw?oc=5) <sub>Gulfbuzz</sub>
- 📰 2026-11-25 [Is WeRide Overtaking Rival Pony AI?](https://news.google.com/rss/articles/CBMiigFBVV95cUxPaVVSTGFqQldCYV9HNEFBQ0hxZVp4aE1oaDhpUVNjaHVnWElfMVdBeHMwSllNMGtBamU1QVpfdE1sN2NiU1RqS0NrdnN5eTQxZ3pWOHg4UkxPMXZ2bHhYNHQyR1pmZ0NMUW1BeFE3QUt0SVlNaEdUWFp2SDJheXNGMkp6UFZJUWhRZ2c?oc=5) <sub>Benzinga</sub>

</details>

<details><summary><b>Pony.ai</b> (155)</summary>

- 📰 2026-11-27 [US and Chinese robotaxi markets enter explosive growth; 2026 output value gain at 100%; estimated total at US$850 million](https://news.google.com/rss/articles/CBMia0FVX3lxTE5pSkZtLXVFOEgxMnotMWxJOTNtQ3FHRjdHNjR2LTc0TklSbXp1S0k5S3FtSEY5NmtNWlVPN2xZaTNxTmxiNWxLSVc1SVY5UzZnNl9mZ2Rsazk4SDFuQVhMR0Noa2VvT2VCR2RR?oc=5) <sub>digitimes</sub>
- 📰 2026-11-27 [港股异动 \| 小马智行-W(02026)涨超6% 三季度自动驾驶出行服务收入飙升165% 公司重申全年车队目标计划-证券之星](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1mcU5vck51WFVnLVhsVVU5emhuWXJQUDk3YkpqXzhXbF9qeUJLZ0JHM3RzUjJmdWFZZXBzY0ljdHFFQmRrRVkwZHQ4Zm0wNGxLbDZURmR3Ml8yRUtsM1E?oc=5) <sub>证券之星</sub>
- 📰 2026-11-27 [小马智行-W盘中涨超5%](https://news.google.com/rss/articles/CBMiXEFVX3lxTE1zdkJxOXV1ZV9maEhRQzRlUTdiT0VHUmZCSEFKcGxJSE03SlJGZDlBN3BjQ2doaTlaa0d1SmxfemNtZExUTXVQNGdCNjJLOXYybndxMHRUSjdmMmlH?oc=5) <sub>www.caiwennews.com</sub>
- 📰 2026-11-27 [财联社汽车早报【11月27日】](https://news.google.com/rss/articles/CBMiSEFVX3lxTE9ONVJiYWpvVE4yeGxKdXhtanpIbDd1cE9takstcUl2QzdkS3l2XzRlcDZpUHY4aU82bF9Xb1pydzVyazdHZG9TTQ?oc=5) <sub>财联社</sub>
- 📰 2026-11-27 [华泰证券：具身数据标准提速，关注Optimus亮相与T链](https://news.google.com/rss/articles/CBMijwFBVV95cUxQYmJjUS1XdkFZM0xXam1uZWJuOHFLYXktZE5TdU5XWEJrMVh5VXB2VHIyalZrVmZZMnFMd0FwakFRbkpvNU1PeWRsMWpDT1JpNVFtZVNPX01LbldvVlZvYTNoalFJWkxTYTlOazZrWWJEUDFYWkJKa2lmLWxGa09YVmZOUE50YjdKR2FNemg1TQ?oc=5) <sub>21财经</sub>

</details>

<details><summary><b>WeRide</b> (145)</summary>

- 📰 2026-11-27 [US and Chinese robotaxi markets enter explosive growth; 2026 output value gain at 100%; estimated total at US$850 million](https://news.google.com/rss/articles/CBMia0FVX3lxTE5pSkZtLXVFOEgxMnotMWxJOTNtQ3FHRjdHNjR2LTc0TklSbXp1S0k5S3FtSEY5NmtNWlVPN2xZaTNxTmxiNWxLSVc1SVY5UzZnNl9mZ2Rsazk4SDFuQVhMR0Noa2VvT2VCR2RR?oc=5) <sub>digitimes</sub>
- 📰 2026-11-26 [The Fierce Competition of Chinese Autonomous Taxis in Dubai: Market Expansion, Tech Advantages & Global Layout](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1rNWFaSE9Ed0Z3cVV3WE9aYjc1MW9QWjE1VEZ0cmV5TDZ5cW96TktTWXVrWWlyLUFhWG9pd2YyeFoxWFZteVNtZ0hFamVkOVU3cGhR?oc=5) <sub>eu.36kr.com</sub>
- 📰 2026-11-26 [解密文远知行Q3利润承压三大诱因_公司新闻](https://news.google.com/rss/articles/CBMiYkFVX3lxTE4zT2NVZkktV2ZVTndlcThzWmVLZ0NiWUpmcks5MXdYaVp5VGY3RkMxT3lKZFlyN3pBQXhJZjk0ZW5XTngtdjh3bnJidEN4SU9MNnAteWt1WXZySzYzbFZjNnF3?oc=5) <sub>证券之星</sub>
- 📰 2026-11-26 [文远知行-W(00800.HK)盘中涨超5%，截至发稿，涨4.98%，报7.795港元，成交额340.86万港元-证券之星](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1kYm1IQWhEUXFyTmR2eTVVVm1FMTNKOWZ1akppYnl5M2RCbTFIdHZkSGctTjhycUJwYzRucWZQN0NudUVqZmxPYkJZTG94LVdsb25WMVBzbmUxQUtpTUE?oc=5) <sub>证券之星</sub>
- 📰 2026-11-26 [营收暴涨、研发超营收，文远知行出海遇安全考验 新加坡榜鹅，搭载文远知行方案的自动驾驶接驳车测试时险些撞到过马路学生，当地监管叫停同类路口测试。险情背后，文远知行第三季度，营收同比大增 88%，Robotaxi 收入首破亿元；但单季研发投入高于营收，亏损仍](https://news.google.com/rss/articles/CBMiiAFBVV95cUxObEZ5YkkyNGJjaW5mSEJaVE84cDMwYWpRdW5Kb3FmQU91eGRqNXd2TVpyVWFLcXpKWUxxUUI1RXl4WElfMzgwZ3NEMlNTbG0wS3FnUGI0c2NyWUZIX0NzV1R0aVZ0Y09uOXE1d2NCTnQwZW8xV2VsY3BLLW5qWmM1a2wwemdEbzNy?oc=5) <sub>Sohu</sub>

</details>

<details><summary><b>Horizon Robotics</b> (154)</summary>

- 💻 2026-11-22 [HorizonRobotics/holobrain-0.5-homepage](https://github.com/HorizonRobotics/holobrain-0.5-homepage) <sub>GitHub</sub>
- 💻 2026-11-22 [HorizonRobotics/HoloBrain](https://github.com/HorizonRobotics/HoloBrain) <sub>GitHub</sub>
- 📰 2026-11-27 [Morgan Stanley Updates China Humanoid Robot Value Chain Map: 48 Companies Included, Only 3 in the "Brain" Tier](https://news.google.com/rss/articles/CBMidkFVX3lxTE12N25wbnVxbTNKRUl0a0RMSUp2bXNSQUpWaVNiNk1UaDBRTldFZTBaUnFZYzRnLXc5ZHVnQWlaajFna3JQVGtGSmlNelI2ODBVdUI1Nl9mZ2F1UWxpRElBQ2NhclN1dXZLQTVUT2U5WGNZVWtQRUE?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-27 [The Liability Gap: Why XPeng's Autonomous Driving Claims Don't Add Up](https://news.google.com/rss/articles/CBMilwFBVV95cUxNUUtEc3JWUVNVODZGSEw4VlY3enNTa2lfbmpDUFZ1YklIRGxERVNuTnBVNjZUa3Z5ZzY3S3QwU01hQVlqM2FKajY0cm91TW82REJTNEJWNnFzQXJMUGlKRlN4LVVyRWZJay1CT0RsZ3ZyMUltWDFuS0pNRHJsdUM4ZzRlaWEtU1pNMzhfNmtZZTJFQ2Q0elJN?oc=5) <sub>Vocal</sub>
- 📰 2026-11-27 [FAW-Volkswagen ID. AURA T6 Reaches 20,000th Vehicle Delivery-](https://news.google.com/rss/articles/CBMiYkFVX3lxTE12dDRGMUtkY25OaU5Id1FRb0VKa254R0pkZlVpU3dNUExzVVN0TDNfeFNGR3Q2X21tMnRNUkRwRklQOHJlVzJjSE5jSEN4YVhIWkNqVFNFckctOS00Q041MXh3?oc=5) <sub>网通社</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (18)</summary>

- 📰 2026-11-27 [元戎启行的这个RV方案感觉已经很接近特斯拉FSD V15了[哆啦A梦吃惊]猜猜看哪个车型会首批搭载？ ​](https://news.google.com/rss/articles/CBMigAFBVV95cUxNU2l1S0NlMGl5NTZ0VTFfbFpmdVd4VlVndU82YkFrRnZYeFR5dmxSakc3OWJqalM3Z21mX2x0Y2xoNzBRRXJpeG55SXlNUU5NTFZBNDNzRDYtelRLY1NqT3ZZdFE0Zi02aWJ6U0lvU0xuLVBIc0k1WktCamd6dnEzTQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-26 [特斯拉Reality View引关注，元戎启行发布深圳街景渲染视频](https://news.google.com/rss/articles/CBMigAFBVV95cUxOWXVweWkyU3RMMW1URnhrSHJBWkdfLWtVbEdUUkRjd0tPZUM2WDFybUVmRjcta3MwWHRWYjA5Z052dG1DTDFrdFJMRURXdE9KeGM0NWF3UUNNTDl6STZnbkRaZjdFRTJ4cS1mZE9EemxUd01kOERvaVUtS3VYWjdraQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-25 [特斯拉FSD V15 Reality View惊艳 元戎启行同类技术曝光](https://news.google.com/rss/articles/CBMic0FVX3lxTE5jNldwNDBLcDU5OVNNckN3RzhlMXVZdFJ5a2haZXpSTHJsc1BqcmRSRUd5eWlyRVZVcnUycU1VT0ZHancxaFZ1eXVxTmxDVVlkc2llODB4ME9fVmVDMVJ3dTA4ckRRV0hSMGMtbjRQUlV5cDQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-25 [特斯拉FSD带火Reality View，元戎启行早有技术储备](https://news.google.com/rss/articles/CBMigAFBVV95cUxQbVpMVEdmdnJxblRkVjdEODU2Y3BYZkdYMElDU1BKS0x5Sl9sR1M0bGFWQmRhNEQ5dGhYYWNWd2pBQmVyX3ROQ183c0x6NmI2X3Q5NFdQZHZjUFNXMWNoYW1WRzJ5NE9JTFAzX0VaX0VFcURsV1VqcXk0ZWo2Ny0teQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-24 [Anthropic创始人第一份工作在百度，几年就打造超13万亿元市值公司](https://news.google.com/rss/articles/CBMijwFBVV95cUxNMXZJWE1ta2hxdmZ1VzFDOEluOEZ0Q1hmaEFwOUdvemZtTXljVGhLbTlYOVdEQkhaVEhfQ2ROazctRWNrdnE3TWNERWg2dFlDakNuSWJtRzBJUmxzQzlCWEtVNjNacWExQUNvT3Bkdmt2Y3VNOEYxUDV2eTlhcGhIWWluZWpMX2c3SFFvY2NQMA?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>Mobileye</b> (16)</summary>

- 📰 2026-11-26 [Mobileye Faces Rising Competition in Driver-Assistance Chips](https://news.google.com/rss/articles/CBMinAFBVV95cUxOS3dfVkV6M3dNNlh3Qlh4LVJjTlk1Y2FZRkhEZXBKR1RBVEdUYTNLR0RieUJwSmdBU3c4THIybEhlT1lwQnBocWU1X0ZvVUI4cW5KRUUtTFBrNlBMQ1lqdEZQa0RRd0ozaVdFTkR2ZVFvYngyUGVwZkdoS1hKYmhCN2lkWVFXRzFpRlBKeFl3WVZuakpfSkp2X3JMMDc?oc=5) <sub>Wisevoter</sub>
- 📰 2026-11-26 [Has Mobileye Global (MBLY) Fallen Far Enough To Look Undervalued?](https://news.google.com/rss/articles/CBMi2AFBVV95cUxPbmdYOTJyc1VLTFNOTDR3eXB4alExa1VIazR0UlRlWW9JeVRPYmZ0LUZCNnNyRkdrc3lKd1hLWU5nX293QUZadmU3SW9KREtzWjIwemhpaUpzMTNCN0F3ZDFGcHNZaU1OZkJxM3ZKTVF4ZVRwZ0Y3aElrQlVvcVBOMi1yRjhTWTZsak1hVExvdkpia3JmZDBKRUxRQzV1bWdQM1dXTHdHaFlFQ21kTXBWemRrMklERzdOcmdaNjNJVktTaUY0Sk10bWNOVHctZm5OMjBUYXhzeXLSAdgBQVVfeXFMT25nWDkycnNVS0xTTkw0d3lweGpRMWtVSGs0dFJUZVlvSXlUT2JmdC1GQjZzckZHa3N5SndYS1lOZ19vd0FGWnZlN0lvSkRLc1oyMHpoaWlKczEzQjdBd2QxRnBzWWlNTmZCcTN2Sk1ReGVUcGdGN2hJa0JVb3FQTjItckY4U1k2bGpNYVRMb3ZKYmtyZmQwSkVMUUM1dW1nUDNXV0x3R2hZRUNtZE1wVnpkazJJREc3TnJnWjYzSVZLU2lGNEpNdG1jTlR3LWZuTjIwVGF4c3ly?oc=5) <sub>Simply Wall St</sub>
- 📰 2026-11-26 [Shimmick And 2 Other EV Stocks To Own](https://news.google.com/rss/articles/CBMilgFBVV95cUxQWjNPbHNyS0xsVmZWRTVra0gxZV81TklmR01YOUJhU2IwazJsb2d2aE9FaFlYRTVoMzJKQy1HMmJ4djJWSkMwbW0xb2NZaHdobnY0d2pZa1hXV0xYTnp4S0VlLXJhREZ5Z3Brc1NHNVRDNnFEaGtmb1dZU0kzaE12Z3NVMWVrZmtHdUMtSWF2U0hXX09iQXc?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-11-25 [Mobileye faces new competition as cars get smarter](https://news.google.com/rss/articles/CBMipgFBVV95cUxQTEZyekgzdFhjTy1DUzIyVHUtOUdyM3U3YWJmd0g1TDE0b2F5U09INkh6N3NycHNkSnBPYzJ2cENQWVFmMzdHOFdEdWVudm5fNnpsWlRPQjhrN1cxVWpJVTF1LW9ETUhfSGYxZFFHX2RFa2ctZGc0MGF6a2lMU3kyeFRQR1BuS0tIWXNmVnJwOHdYS2VSYUM1VGFMMGF1MzZUd0gwQVB3?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-11-25 [Motional retools for the robotaxi race](https://news.google.com/rss/articles/CBMimgFBVV95cUxQRmQtVzZpbHI2WEpZS1o3MnRDVUtabFA4OEJ6MjdiVHhmekZQTS1OcFVPXzYwcklrRDJYQXpEOHJqckxPMmpjd2RpRndrcHFxUVpEYS1WWWctZWdCOUswejRxUHExX0RreUFnVWV5OEpxRGRmQ2hvWVQzVEM4S2RxQzd5NXkxVVhxaVA1TmJ1RFVEaEUyVktydHln?oc=5) <sub>Yahoo Finance</sub>

</details>

<details><summary><b>Aurora</b> (37)</summary>

- 📰 2026-11-27 [Competitive Analysis of Autonomous Vehicles Market: Waymo,](https://news.google.com/rss/articles/CBMilwFBVV95cUxNQjdpUFNMQzN3REM5ekNZaV9JUlU1TlFZWWtKb28yNTNRaHFHVjNWM1RxVl9NbDA0Yl9TWGJlOVF0WXVPVHV6VE1kSXJOaEVYcFVFb3RYd08xb19JWFhwUENlaElmV1ZVWjJuMzg4WTJRM2piQ3dUSkhrSHQwYjIxNUc0N0IzcWZtdXlnbnFhUW91eXJXYW0w?oc=5) <sub>openPR.com</sub>
- 📰 2026-11-26 [Physical AI comes in every shape. Connectivity decides which ones scale.](https://news.google.com/rss/articles/CBMioAFBVV95cUxNUFkyZ1k4ZFRpSGpVSEZmY1J6dTFPNWFzTDA2ZV9lQm5qdHJtOFlxdU9Gd2NZNXRvcDRuQjZzaFVLVzNyc25QTVptOGI2VHcyLVBjcDJRVkpfdU1WT08xNW1oZVllTFdVYmxuZUpMRUtHVnZnVHhGTVZleXVvbGIxRFMzd3QtS1lFWWoyZklSdERDb0ljam9wZDFwZ3JMcUZo?oc=5) <sub>Cubic3</sub>
- 📰 2026-11-25 [Notice of Investigation of AUR: Kessler Topaz Meltzer &](https://news.google.com/rss/articles/CBMiqAJBVV95cUxOSlh0RmpSLUI5ZGFGYTkwS1EwUHdsYmpfV0lETHR4UW1wUS1RSlVVdUY1bi1jNVRtM3hKLWlQNXBBVk02Ti1CcWViWWhJLTlybmcxRnliWG45Z0RUQWRiTFE4aDZHeVFXUDNrNDZUUGdJdENTMjJtYkk3R0pzaFQtLVd0ZDBwV0RtRU5GSHNJMTJFdUtNMFlOdnRaQzhWQXdmYjM4UW10VFIyY2JRS2tBTTdpSDhIVXhLUVJFQjJULUdyR0MzdnBkR091N2VrT3JqdEcyaE1oRkttUzlDbm00WkFjWllkZWJjbFlZZUhKUDZWcTlHRWc0YlJwcllqdW0tSHM4YzREUGpDWHREWUZiZFBiQkV0QW1hN24yR0hBYnEyWlJidjFGaQ?oc=5) <sub>GlobeNewswire</sub>
- 📰 2026-11-25 [AUR Investigation Alert: Aurora Investors are Reminded to](https://news.google.com/rss/articles/CBMivAJBVV95cUxPZ1VGZS0tdUNINmJOSUZ6eV8wdXVwd0hBd25USFh0Q2ItQWJnajBMcTBiVlZpdkk5cjFkRHZxQzVoWVNQSU1YNDVFcDYyN0RXaG1Hc25TTGpDclo1YlZyNDhNUXk1S3o2WUpIS2JIaVBzZlQtd2FGbkJqd3JQQzZnc1E3SVh4U1Jla0RBcXExdXBHcF96VldTdmVtS1NFVk8yb3FEY01BbWxWdFd5WUhnR3psQnNSUkRrNkpfZVJuTnBzMWdjMG9VbTVGQlp0S2E3YS1ac2JRSjFMc0I3UDZzQ1liY3RvM2F6UjhUTURkVC1oRlM5ZWxWeE5SMGZqUDRueUZnVm53Z2IyTU1yQ2V3bVRleXBYSkxhT0FaVU5XNjU0WEJEMEpFVEFrMk5xeVh0NV81WnVYWkYzbHlZ?oc=5) <sub>GlobeNewswire</sub>
- 📰 2026-11-25 [Autonomous Trucking Cost Parity Projected for 2028](https://news.google.com/rss/articles/CBMiwgFBVV95cUxOSVlKQU5Kd1BINGNjaFhBTEQzXzBwdmhDc3V6ZHVTc0JpZU40QmZlN3lzM1R6Nl9SQTkyRjVrZTZFMTBhdDN5RlVOMUNMck5OWERJVGNrYXltMnNGb09mcG9BQ0R6NTFkaml4ZGRZNHlSRzFaMkZDNVZ2TUJ0UUJmRFVpNzFqT3g0Rmt2SUFYbWFDOWdRWU84VFFfdFhCTnlhV3RMb3h3TW56MC01RVFhX2o4bkloaVA0alYwTURBZXFBdw?oc=5) <sub>Commercial Carrier Journal</sub>

</details>

<details><summary><b>Zoox</b> (119)</summary>

- 📰 2026-11-27 [US and Chinese robotaxi markets enter explosive growth; 2026 output value gain at 100%; estimated total at US$850 million](https://news.google.com/rss/articles/CBMia0FVX3lxTE5pSkZtLXVFOEgxMnotMWxJOTNtQ3FHRjdHNjR2LTc0TklSbXp1S0k5S3FtSEY5NmtNWlVPN2xZaTNxTmxiNWxLSVc1SVY5UzZnNl9mZ2Rsazk4SDFuQVhMR0Noa2VvT2VCR2RR?oc=5) <sub>digitimes</sub>
- 📰 2026-11-26 [Uber adds Amazon’s Zoox robotaxis in Las Vegas, Bloomberg reports](https://news.google.com/rss/articles/CBMiUkFVX3lxTE9Zc25aTlhMN0k1cUUzTlpnbHVERkxYUHhBa3kwd3RwTmxHRXVic0xXT2Q3SHZ3UF9qSk5BakVKMU1fOWpNMDRwRURIYXFES0Nqb2c?oc=5) <sub>Digg</sub>
- 📰 2026-11-26 [Jakkuh Vibe Codes Autonomous Lawnmower That Cuts Perfect Stripes Across Five Acres](https://news.google.com/rss/articles/CBMidEFVX3lxTE5lOGNlTXBwbzV2bkFVajBJamVmRDRLNjdHOFh0R2pWU1UtaE1fTEZOQ3dLUjJnLUd0TEt6QUJ4RTU4QWt0ZDhzLTNFVmZYVGh3Szd3QUotYmNOM2dleGp2LXJUOGV6NnFMVERXb3I3YkJ4OEQ2?oc=5) <sub>TechEBlog -</sub>
- 📰 2026-11-26 [Bolt Begins Self-Driving Operations in Luxembourg](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQZU9RZWVNZjZPQi0tdWp4Mkw1TFJENWc1ZEJ6WFUxRks5N0xHLVFScHRwc2ZtZlM1WVJxSzN3UnktbHp6Mzg1Qmw2S3dLbGVaODF3UUdZaVV3VjAzQnBxUlBNM1QzWldReVpzOTlmdjdESTJMam9qLVpsUXdtbXZERUFtVjRWdm9jTEY4?oc=5) <sub>Future Transport-News</sub>
- 📰 2026-11-26 [Does Texas law keep pace with Austin’s self-driving taxi boom? Experts weigh in](https://news.google.com/rss/articles/CBMixAFBVV95cUxQbTdjZGxQMlRkSHJPdmw0R1d3ZC0tS3R1ODYyeE8xUFdndEpZNWVPU2RQam1kWDFQMFk2TmF0eXFwakt1aXJFQnlpbTJYQ2N0SzdMMVRmM05takJnUW1uTS1xaVZUZ1RZdDUwMk9hSlVaejFnZUFfeUJ1bEJZT1ZLYlVqdE1lR2VjeFdtR1lFSnA2dU56MlJydXJabGY3SkM2Q3ZYQnFjV3k5TmtWRVpYWURSU3ZhaWpONE15SVIwR0g2Tjh50gHEAUFVX3lxTFBtN2NkbFAyVGRIck92bDRHV3dkLS1LdHU4NjJ4TzFQV2d0Slk1ZU9TZFBqbWRYMVAwWTZOYXR5cXBqS3VpckVCeWltMlhDY3RLN0wxVGYzTm1qQmdRbW5NLXFpVlRnVFl0NTAyT2FKVVp6MWdlQV95QnVsQllPVktiVWp0TWVHZWN4V21HWUVKcDZ1TnoyUnJ1clpsZjdKQzZDdlhCcWNXeTlOa1ZFWlhZRFJTdmFpak40TXlJUjBHSDZOOHk?oc=5) <sub>KXAN Austin</sub>

</details>

<details><summary><b>Motional</b> (36)</summary>

- 📰 2026-11-26 [Hyundai Motor to Begin Supplying Robotaxis to Waymo Starting in the Fourth Quarter : Finance : JKN](https://news.google.com/rss/articles/CBMiYkFVX3lxTE9QTVEzS1B4cFlESWNVbklSTGlEc2RfV05ESzRaVGgxZFhXemNhRWdQaU9vMkdCcTRKWFNvYnFaSnk2NGRGZzFOUmVtQVhvWC1RWmRKa3VQYV9maVdxeXBMRk1n?oc=5) <sub>재경일보</sub>
- 📰 2026-11-25 [Motional retools for the robotaxi race](https://news.google.com/rss/articles/CBMicEFVX3lxTE9OODFESWJPQWc1cnNIVVlaSVU2NXZSMEJETzBfOVB4eGdGcTJyaEt5VkRJbWxtUHpRdFJmVDJKR3JONVduSkdfc0pfLVp5RTlFejM0R0lfR1h1RS1ZNEFwSnluUzJiblJyS1dwZjdVT3A?oc=5) <sub>Axios</sub>
- 📰 2026-11-25 [Motional prepares for Uber robotaxi launch in Las Vegas](https://news.google.com/rss/articles/CBMihwFBVV95cUxNZndrdzVJUDJpY3I4VzctSDBMVzA2VWNjU25uRVYwa2FTSjhkU0IwQkpLcFRlSWRCbnBwTUJMWnJMc2Y0MnBhTzdueFRLQVdhWEdLSW9ZZ3hIXzR0Ml9uMkgtbGZteXhvcWxvOXFoU0lrNEdLSGVGczRQVGFpNW1RYXNZN1FTdEU?oc=5) <sub>Mezha.net</sub>
- 📰 2026-11-25 [Motional readies Uber robotaxi launch in Las Vegas as it resets cost strategy](https://news.google.com/rss/articles/CBMimAFBVV95cUxNVkdrcXFnSkpDcklYN005Ykd0SGtFUi03akM0OG43c0E5Ny1Xbk5PYUFCTWFQNGZkc1FNUzNVUTRJaHdVS0FGUGNrMkVQWnFjc1ZMRU9mM2d1Nkc4THprYUNJbXdjMkJjck9ZQjQwRFFtVVNBSGY2RDE5UE5wMmtkWjNoUVRmS01NSUVRVlBkSzhuQmhnamxvZA?oc=5) <sub>Traders Union</sub>
- 📰 2026-11-25 [Humble Robotics targets short-haul trucking with a cabless electric vehicle](https://news.google.com/rss/articles/CBMiigFBVV95cUxOdVFPVFYzNUp6V3RSYl9zRExaZlVwcE92cVVQTzZvTEFYejBHQnVZZ0lKTVA1dEc4WENEVkhuNDNxbS1VbHR3S0JEdFJwRTBlQWdlaTdXMUlwcmt4OEo4MGdUOWxIWnFwOUNJS2NpUjF0dWxkek9ZdFhib3NMWW9iTEVqYTdfYjRxVEE?oc=5) <sub>Mezha.net</sub>

</details>

<details><summary><b>comma.ai</b> (1)</summary>

- 📰 2026-11-23 [Open Source Drive by Wire Kit Retrofits Standard Passenger Cars for Autonomous Research](https://news.google.com/rss/articles/CBMisgFBVV95cUxOYkF5ZVN3eWtSa1FRSnF4Z091VFZlQ2pwZHIybWlxRHhMRXdwWFZMQk43QUNTc3d2VkNRbmNuSGxKUXh1Z0JMN1BfeHFqbFRtM2VnWldHeE9TQ0RVYThPVEpvTnpESTVYWEJZWlJDWWRqbVFYM1dTdFRkWklFd014a2N1d0ctbjlIQy16VW1YYnh1bm1rSmdOdHJvb0JGN1FTbVMzM2F0RUR5RF9SRnNfS1Z3?oc=5) <sub>Bioengineer.org</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
