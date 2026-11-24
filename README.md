# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-11-24 · 1,313 papers tracked · 48 curated.

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
| [SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving](https://arxiv.org/abs/2610.20609)<br><sub>Shaoyuan Xie, Zihan Zhang, Jingxuan Wang et al.</sub> | CoRL 2026<br>2026-10<br>📑 1 | [⭐ 37](https://github.com/ASGuard-UCI/safedrive-vla) | Vision-Language-Action (VLA) models are gaining attention in autonomous driving, inheriting commonsense priors from large language models (LLMs) and widening the navigation interface from a fixed command set to free-form… |
| [Scene-Adaptive VLA: Efficient Autonomous Driving via Dynamic Layer Routing](https://arxiv.org/abs/2610.24590)<br><sub>Yujia Yang, Quan Yuan, Jiawei Fan et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 5](https://github.com/yang-luvu/Scene-Adaptive-VLA) | Vision-Language-Action (VLA) models offer a promising paradigm for autonomous driving |
| [AutoVLA-D: Learn a Trajectory-Geometric Condition from Reasoning for Autonomous Driving VLA](https://arxiv.org/abs/2611.12382)<br><sub>Yuguang Yang, Zhewen Tan, Canyu Chen et al.</sub> | NeurIPS 2026<br>2026-11 | [⭐ 5](https://github.com/ShivaTeam/AutoVLA-D) | Autoregressive VLA planning usually predicts continuous trajectories as the final output, but driving instructions often describe actions rather than ego states, which weakens direct conditioning on the final continuous … |
| [Locating and Repairing Domain Shift in VLM Trajectory Planning](https://arxiv.org/abs/2611.10720)<br><sub>Zhihong Cui, Hengyu Liu, Michael Alexander Riegler et al.</sub> | NeurIPS 2026<br>2026-11 | [⭐ 0](https://github.com/ZhihongCui/MoLaRx) | Vision-Language Models (VLMs) are increasingly adopted as end-to-end driving planners, yet they suffer from cross-city domain shift |
| [CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving](https://arxiv.org/abs/2607.04179)<br><sub>Zhaohong Liu, Hao Ye, Xianlin Zhang et al.</sub> | ECCV 2026<br>2026-07<br>📑 3 | [⭐ 1](https://github.com/MICLAB-BUPT/CritiqueDriveVLM) | End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving |
| [PixelPilot: Scalable Vision-Language-Action Models for End-to-End Autonomous Driving](https://arxiv.org/abs/2607.04637)<br><sub>Pin Tang, Guoqing Wang, Xiangxuan Ren et al.</sub> | ECCV 2026<br>2026-07<br>📑 1 | [⭐ 3](https://github.com/VISION-SJTU/PixelPilot) | Vision-Language-Action Models (VLAs), which leverage the advanced reasoning capabilities of Vision-Language Models (VLMs), show promising generalization in complex autonomous driving scenarios |
| [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)<br><sub>Nan Yang, Zhanwen Liu, Linfeng Zhang et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 11](https://github.com/Zizzzzzzz/MVPruner) | Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings |
| [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)<br><sub>Yuan Gao, Wenting Miao, Mattia Piccinini et al.</sub> | IROS<br>2026-07<br>📑 1 | [⭐ 34](https://github.com/TUM-AVS/Chat2scenic) | Validating autonomous driving systems requires diverse, regulation-compliant test scenarios |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 25 | [⭐ 563](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
| [GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives](https://arxiv.org/abs/2609.39601)<br><sub>Qize Yu, Lianrui Fan, Boyu Chen et al.</sub> | arXiv<br>2026-09<br>📑 5 | [⭐ 444](https://github.com/groundingpi/GroundingPI) | Precise grounding matters |
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
| [SimWAM: A Simple World Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.07468)<br><sub>Zongchuang Zhao, Xin Zhou, Tianyang Xu et al.</sub> | arXiv<br>2026-08<br>📑 23 | [⭐ 212](https://github.com/H-EmbodVis/SimWAM) | In autonomous driving, World-Action Models (WAMs) have improved end-to-end planning by transferring video dynamics priors to action prediction, but many still couple planning with future-video generation at inference, in… |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 21 | [⭐ 368](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
| [Latent-Centroid Steering: Single-Pass Classifier-Free Guidance for Command-Aligned Autonomous Driving](https://arxiv.org/abs/2608.00237)<br><sub>Meibo Hu, Jiamian Wang, Pichao Wang et al.</sub> | IROS 2026<br>2026-08<br>📑 1 | [⭐ 2](https://github.com/codingmlinprocess/LCS) | Vision-language models (VLMs) have recently emerged as a promising paradigm for end-to-end autonomous driving, enabling agents to map multimodal inputs and high-level navigation instructions directly to executable trajec… |
| [STAGE: STyle-controllable Action GEneration for personalized autonomous driving](https://arxiv.org/abs/2607.29517)<br><sub>Zihao Liu, Xing Liu, Yizhai Zhang et al.</sub> | RA-L<br>2026-07<br>📑 1 | [⭐ 5](https://github.com/CarlDegio/STAGE) | Driving style refers to the behavioral preferences that drivers maintain during driving, shaped by their diverse experiences, habits, and needs, and is typically reflected in varying levels of aggressiveness |
| [A Survey on End-to-End Autonomous Driving Training from the Perspectives of Data, Strategy, and Platform](https://arxiv.org/abs/2610.00926)<br><sub>Chengkai Xu, Yiming Cui, Jiaqi Liu et al.</sub> | arXiv<br>2026-10<br>📑 7 | [⭐ 110](https://github.com/Jiaaqiliu/Awesome-Training-Ecosystem-for-E2E-AD) | Autonomous driving is a cornerstone technology for the future of intelligent transportation, where end-to-end learning has emerged as a transformative paradigm that directly maps multimodal sensory inputs to driving acti… |
| [AutoE2E: Don't speak - Language free end-to-end autonomy A Real-Time Driving Model for L2++ ADAS and L4 Robotaxis](https://arxiv.org/abs/2611.22374)<br><sub>Muhammad Zain Khawaja, Zaynab El Mawas, Ryota Yamada et al.</sub> | arXiv<br>2026-11 | [⭐ 234](https://github.com/autowarefoundation/auto_e2e) | AutoE2E is an open-source end-to-end driving model developed by the Autoware Foundation Robotaxi Working Group |

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
| [DRS-VPT: Directly Relocalizing in a Scan with Vision Point Transformers](https://arxiv.org/abs/2609.12557)<br><sub>Lanke Frank Tarimo Fu, Maurice Fallon</sub> | ECCV 2026<br>2026-09 | [⭐ 27](https://github.com/ori-drs/drs-vpt) | We present DRS-VPT, a feed-forward transformer architecture for foundational image-to-scan registration |
| [Horizon3D: Sparse Radar-Camera Fusion for Long-Range 3D Perception in Autonomous Driving](https://arxiv.org/abs/2606.31096)<br><sub>Geonho Bang, Geunju Baek, Dongyoung Lee et al.</sub> | ECCV 2026<br>2026-06<br>📑 1 | [⭐ 26](https://github.com/geonhobang/Horizon3D) | Long-range 3D object detection is critical for safe autonomous driving at highway speeds, yet existing radar-camera fusion methods remain limited at extended ranges |
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

<details><summary><b>Waymo</b> (247)</summary>

- 📰 2026-11-24 [With severe weather looming, Waymo halts Bay Area rides](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNbnEya3ZpaW9RcDlSY0J3bFA5d1A3TE12Vm9zbE1fdkxjR2pKTXIxT083Sl9NUnhIY1FoZ1h4RVc0NmFvcXF5R3J3eVJ1SUh6Um1JVU1CMmt6VFhMR2k0M0ZCZl81UWxJSUd4ekNJNUdJZmw0Rmp5b2RIWWpkRTlXUnhBTjNraUhSUmNPZ0JEbE5vVmRrejJzQWtfRG55NGktQmpBU3BTNkZiZw?oc=5) <sub>Mountain View Voice</sub>
- 📰 2026-11-24 [Video shows Waymo car cross police tape in Phoenix days after freeway pause](https://news.google.com/rss/articles/CBMiqgFBVV95cUxQYmNLME1CU0Y5ODRBQ0pmT2gyYWt1a01acGM0QnpIWVFzTDV5a3ZsMU5ldnVISENYTDRGX2lWN1B3di12SWx4Nkd5V0lOb2VjLUdDNTVFN18tSkRJSVR2eDljcVozN0dGRGNheEJVMjY2RUtacmVZQ2ZnTVh3NmcyVVlTdE9EQ2NOTWNVOU44VHRLb3QzVWtaZXl5RmhLMm9icHFBbzZkQUJsQQ?oc=5) <sub>FOX 10 Phoenix</sub>
- 📰 2026-11-23 [Waymo hit pause in San Francisco after robotaxis reportedly blocked traffic](https://news.google.com/rss/articles/CBMiREFVX3lxTFBudzNucV8wODlYemg5NmVueUZSSmdzMkZ2YkRtbl9ybGM4cEtZNkpFUGg2VzJkSUpFWEpWN1BGOVFwUFdU?oc=5) <sub>Digg</sub>
- 📰 2026-11-23 [Waymo to pause service ahead of severe storm coming to San Francisco](https://news.google.com/rss/articles/CBMiqAFBVV95cUxPR29ZMEV2cW5xYzh5TkZKVkFKdGNBVElubExIWHNnVUxaa3lOSzBRbEtGMG5JaUF6X0lFWk1uR0RJMFVrYTcxWUZDclROZ1JSSjhFTF9DeFBESkFfbXU1ZlpueGxYS2NRTEI5X0JqUXhGQXp4Zkl3RjR5WkhfclpiUmRmbS1GRUZTYVVySWQydm1jby1pNENRcGxlbGVxQzZRSXRkcXlzWUXSAa4BQVVfeXFMUF9TMkZvdkNURXd5cEU0Y3NsSVFjaWdTZy05WXV2RUt3VjA1SGx0SFZuRzNpQmo4bzNmeVRJUUZ6YTJnMDFPcmRXN3h2cE04ekpTTmYxVmZDQUFhR1IxNTk0bUVOWlBBYUlGOVRkc0g4MnM2MXVydWR6WHRIWHkwMlpsb3JzQ1EwWVZvR05ERlFfZkhCNGFhcEQ2dEJpYmItRUZ5V1hEbnRzYWhRdmNB?oc=5) <sub>KRON4</sub>
- 📰 2026-11-23 [‘How Can TSLA Compete With Waymo?’ Gary Black Questions Tesla’s Robotaxi Strategy, Predicts Waymo Will Le](https://news.google.com/rss/articles/CBMihAJBVV95cUxQaHRMZGMzSm9RNU1iR1NDZml3bkhBWHRVQjVmbWNZUVNxZ1VkdUtQWk12UF91N2hiVnFBOXNEM29zeHBRTGJ3YWFWZGNYcVhsLXcwNnprWEFqQWtiQ0V5TGk4TE8tYUZkSGtxZ0JXaFMyR0k4NTFKX0xydUt0Z2M3aTdVOUpuNVRkbS1UYlliNjlqRWNZeE5UMFZ0RHJhTmhxZi13MEw4M3owNUZJYWlsRmdRNkJNZUVva0g4YWZ1ZDFpamtUU2N0M216b2J2UWhvbmpVUkMyNVk5QW03RjU5MFp0Q1hEVHdFN1h1ejJhX3duMndEdFNFU0lzWTdlMWJhVWFxSA?oc=5) <sub>Benzinga</sub>

</details>

<details><summary><b>Tesla</b> (386)</summary>

- 📰 2026-11-24 [Tesla jumps 11.5% on FSD v15, a release most owners can't use yet](https://news.google.com/rss/articles/CBMikwFBVV95cUxNQmpFVUZFa0ZPWTFGTmtoQkh0MmRhSDNEcmNXaW5Uc0lONTJzVWtELW45eXVrVEw3NS1TMkRyQ0dlTGQxNGR2aUNSaVJmZUlWbnRPVnJfZngtR19FbEpLU05NZ09FaEFDaURlbi1EQ0FPUEJPQzhBQm81cy1kZU04cTR0X2poSDhlZ2tWZWd3UUY0bVU?oc=5) <sub>Startup Fortune</sub>
- 📰 2026-11-24 [GM Eyes a Former Tesla Autopilot Chief as CEO. No Autonomy, “No More GM,” Says Jason Calacanis](https://news.google.com/rss/articles/CBMimwFBVV95cUxOTHY0QWhBLWsxaXZSZlllb3BlcDFrVEdfT01YUWp4UjFyRFlFVlBybjJvRExqX2pPRzBTaGE4TlpHQzBMbktPamVhV19OMHhRMHFmM1BVbm02aTJqS2RnNGdFUUFMc051NlAwX3BlQ0RuVlpyS0wyZUxCU2tCVEk4QWZEWk0xc2ttY3lpY0ZiNFZZWGdSQXBFOWlDOA?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-11-24 [Tesla Robotaxi vs. Uber in Austin: 5 Details That Matter](https://news.google.com/rss/articles/CBMikwFBVV95cUxOejR4RG1aVGEwRzRfLUNmc0xJSTdCOGtGVk92cHRRVzhlUVRLRS03dmpfajczSHZ5OENFdUFaZVBfNkw2LTl2VW1IVENmSzhwcjhTNE1zRmhQN25zbU1TVkFkdGxzejhaaWI1aUU3NkVHUjY3X2JGUmJZMVN2MlJUX09JS2E5VWc0RFRjSHctbndyZDQ?oc=5) <sub>BASENOR - Tesla Accessories</sub>
- 📰 2026-11-24 [Tesla Wants Drivers to Keep Their Eyes on the AI-Rendered Road](https://news.google.com/rss/articles/CBMiwAFBVV95cUxPXzdTSl9DbnRIZzNLVXRlQkxkc24tMUhfOUxBN3NYSUVjRXlUQXZTREZtUEowU1VNc05wOXVlNXF0Vm1LVE52MS0xcDVoNmpZVWwzM0ZkVUZlc0hWbmJTQWNLRzhPVDVBZzJINTl1NDdybHVFc0w5RzBnT1VIQlNvM21BYndrZlZ0N0VqQUVKTHBRdzh3WmQ5QUNLWkVKZUpyZUpQZXRFY2FsRW5DN0ZESDVwNjF4Yk9QVXFCUmJHaHQ?oc=5) <sub>The Daily Upside</sub>
- 📰 2026-11-24 [Italy just got a head start on Tesla FSD over the rest of Europe. While the rest is still stuck at the red light, Italians are about to let their Teslas do the driving. Picture it. Rush hour in Rome, and you're sipping an espresso while your car deals with the scooters. Ev](https://news.google.com/rss/articles/CBMibEFVX3lxTFBFWVRDU0ktaE8xdUVSQ3hkWDBwTWg0MVBZRjVUaHZzOExXVXB1TW9XQ2hjYmwzbC00cGhvZXNNLTdMbTczOGVXTzlVN1BfVnpCSjQ1aG0yVWloRGFJT2VoblFVaDY1bFJqN2h5bg?oc=5) <sub>X</sub>

</details>

<details><summary><b>NVIDIA</b> (228)</summary>

- 💻 2026-11-19 [NVIDIA/nvidia-linux-utils](https://github.com/NVIDIA/nvidia-linux-utils) <sub>GitHub</sub>
- 💻 2026-11-16 [NVIDIA/scadactl](https://github.com/NVIDIA/scadactl) <sub>GitHub</sub>
- 📰 2026-11-24 [Singapore investigating Nvidia-linked Megaspeed after US blacklisting](https://news.google.com/rss/articles/CBMirgFBVV95cUxQYzlUY1QtZmh2X25XQW1Fd2JscHkyVjlWY3dCWkQ1REVTUk93dU1MN2RXei12WXM0cjBlVnBwZ1ZaWlVzdkdVRTNyWmUxVURJOGpWd0hWWG5iVFM3NGhpX2pNMjI0TkVhamlyNF8wUTFLcUVJVjc3VEQwU3pJdjRQS1VhS1J3aXhldUlLdHdsZkg3Rm9GUEZrcUxzWUJ6VzhlWHNhV1FFRzAzaUs3MFE?oc=5) <sub>93.3 The Drive</sub>
- 📰 2026-11-24 [Nvidia’s comeback bet: Why Jensen Huang’s return calmed markets, for now](https://news.google.com/rss/articles/CBMiwAFBVV95cUxNdFRHU1NQeHBuNEJqR2hqcHRBQ29Yd0thN1ZEeUVfQ1BJMXF5aGVBejFodWVqMC13ZUtqZ3VmcDJ3MjhxU2FwbWFveUNUREZPd05MdkFTX1RNUFdSdUJQbEVHSmw5SW9MSmFPVWFtUDVVLXloZWZuUmh3bi1ubE55ckQ0NFZhZFlxWENTRG9PZEdHcGdPRGt6S1BZUjlFSk13c2p5OGNMd3lNbktldFBBbFh6MGUweC1vdVVBWlljcmo?oc=5) <sub>Audacy</sub>
- 📰 2026-11-24 [Some in Jensen Huang’s native Taiwan welcome his return to Nvidia despite scandal](https://news.google.com/rss/articles/CBMiswFBVV95cUxOQVYxWmk0S3R2dlh0VnhDeW1lc0o2M1hQdVEtaDVXMHdxeE1zZTJOV1NtOXg2WkRHLTFxNVNCZnV3SkFXdWY4OXM1MXowcEtxMl9Pd0Rmc1Q0ajRVZEhremJTV3IwSk9NZ0s4QUNlbzl6RlBCM3hHNU9VNExQSmRJbUVZRThta05JWlBLM2NHOXdFbzVlUHJ3QjB5NVJuTFlpSHc4RjdCbG1sQS1kSHg3ZGVXRQ?oc=5) <sub>Audacy</sub>

</details>

<details><summary><b>Wayve</b> (37)</summary>

- 📰 2026-11-23 [Mercedes gets edge over Tesla in race for self-driving success in Europe](https://news.google.com/rss/articles/CBMihAFBVV95cUxNREhrZGszRlNBUzFxbjBURFBhQldOMDFiOGV0TVNMWWVuYjA5dFdCTGpGV0RCMlJJczEtWkd0eG9YRnkwZnFVTFRseC1iT1lBM2w0LUlUVFhqdk1ydU1vWDRPVGZfTlE4SnRSRnZZTkMzVzdnVFJTM0dobnRKRG1jOV9Yb0w?oc=5) <sub>Financial Times</sub>
- 📰 2026-11-23 [Autonomous Driving Software Market to Reach USD 6.78 Billion](https://news.google.com/rss/articles/CBMinAFBVV95cUxNZFVjLThIaVVwbm1rWlBYT2IzMDFFZEF6LWVzaWY1YTR6b0JLeDBla0VacjF0dEtpQjhGblZpVjUyZV9ZM3lSS3UwdFdtYmp0dm15SzdBZnpEemNqMlcxMXZ4TnVDV3FqZjNCOGdWNFhBRGFUWVNlV2poZHFkdDA1OEY1QlZaZzZ6Z09QQWtTRDQ5WGxyV2xmbEtxOHo?oc=5) <sub>openPR.com</sub>
- 📰 2026-11-22 [Kakao Mobility partners with Nvidia to develop Level 4 autonomous driving technology](https://news.google.com/rss/articles/CBMi2AFBVV95cUxOUnMwVTdET0JiaXlkcm83bUZkQUt0TFpJd1lkZG13a1JIUWl3dW81UXlGbHN1Q2Z4VDZGVE5GcFNmeTRsNG1kODJpTTJCclVueHQ1LVFTOTFFWUVpRUpQYmMwc0ZSUHJqN05IR292WVBsOTFUMDl5VldhWUd2UkRfd1NXZ1BQcnI2TFFJdmx1cHN6RFY3aWl0VnppeUxYV2xPWjdZRWRJVzkwWFZ6SWdXQ3FLdTNLMFE5bTRMUkZRRWdlamhhT3ZZNXVOLW5LbnVaX3h6STh2VGM?oc=5) <sub>Robotics & Automation News</sub>
- 📰 2026-11-22 [Nvidia to Continue Robotics Investments After Huang's Departure, Assures Portfolio Companies Directly Under Interim CEO](https://news.google.com/rss/articles/CBMidkFVX3lxTE1IbWJob3hvWTZuUDRrRXFpZ2phdjVSWllyTmpLN2VSMlR0MV9NaExQVjJ3cHdlVUQ0czI1Y09HM256ZWY4QVhUZ3VLbUFBSTN1RU1GLVdENTdIcmNvSzlibnluYTlHUFc3b2M1TGRWTjNTeXNNZmc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-21 [California Bans Waymo Robotaxis From Motorways](https://news.google.com/rss/articles/CBMilwFBVV95cUxQSnRJcXd3Z0dtS3FZTzh4cHoxclA2Unh0ZWRwZTBKbVZxd0VBSEtOUXBQVWduZjFyMmtfOTdoQldVMUlGQWhtenRwRVNnOElQamx2V1lXUEFINGxrV3FQYUVFTHhWcHhFVmRkYUxDbGZoa2d5VWItS3BFaDBBSklVakFnSlFIOEMzcXRuSWxnMlkzQzNyWGFR?oc=5) <sub>Wisevoter</sub>

</details>

<details><summary><b>Momenta</b> (115)</summary>

- 📰 2026-11-24 [Chinese Robotaxis Expand Overseas, Face Scrutiny from European Passengers](https://news.google.com/rss/articles/CBMizwFBVV95cUxPZGR5QWRWTVJzelo1RDNUVXk5NGJzekRTTUJyTktxSjdtV2RweEJEQjNuSU9pMWZhX2Iza01teko0N1B4ZmVYRUdXWGZiVnI4TWpqMnpxbUZoY2txZkxydEk5cjJDdEdFSVA2bHY1bXp5b3NiLUIta0RiUXJXNHNDamZLM2hpZVFHb3BnOUpFaVpIMnIzdnUxTkpKZGhNZTVocGxaUnlDdENKaWszS205Wmd2WTBvdWMzX1lxMUhuT1MwY3RhTmN3QmZjLVNVS00?oc=5) <sub>Gasgoo</sub>
- 📰 2026-11-24 [奥迪E7X智驾大升级，AUDI的Momenta R7为啥那么能打？](https://news.google.com/rss/articles/CBMickFVX3lxTFBkajNQcWpQdTBkbVZHb25pNWR1U3JXX3ZZTFhtWlN6TkxLcVZyb25NRG1fMnR6MVRhQmpBMEZoazdOMTI4cmloWE1YUHlWTnU2eThvTFRybTAwMVdmd1NWaTM5SEJVQU5TbTJSOXdOVks3Zw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-24 [宝马iX3智驾系统怎么样？技术深度与实测解析](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5NZm44VkpNbzZaUnpHRVBwdko4dTZVTzZRcHBNanlCeHJQZjVTMVI1endKWmM5X3kyeGlPdWdTSjNjWUlCSTZGSXFycVRJamVSYTlGOU54dENTblk?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-24 [【视频】MG 07连续月销破万，11万多给Momenta R7激光雷达智驾！](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9PbjYtNUlfbmhPbmlGLXZNYU5tS0FuTlp2cmU5Q2dMQzV5Tm9KTTIzclhXQnhlc0xpTHZpcUIzZktuZGJPdkhGOHRDZ0xqNXlCUDR5V3hjYkxPOTA?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-24 [迈巴赫S级2026款值得买吗？146.8万起顶配超450万，3个维度说清+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1aUmRjNmVvd1RodGdLU0E1TGs4YnJObjk4TlVZUDMxbGg0VG4tOTJYcjFnTWs3QmVlbmVCV19fUXRtN0lCM0F6cmtITTVFNUp2MEhBVXB0UUM5alNCQ3VV?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>XPeng</b> (238)</summary>

- 📰 2026-11-24 [XPENG Upgrades X-World With Virtual City and Real-Time Simulation](https://news.google.com/rss/articles/CBMixgFBVV95cUxOREVuR2JNTkJzMlNHa3FVMnlranQ0bWhPZjlYQ09BeVdaZW5vM25MbDZkZzBheVdVMXMzaFloSGNCUk1aR0VJSEQySEtwbEoxLU5hVzNBMEJSNng3ZG1fN3pCMXI0MDJIRlREZF9zQlZCSElPZjFORnZvckVOeW85RFFxMDBJelEyVHNUemE5YlBlZEZNNkF4T0NvQ3BpNUdMZlR1VFNmUmFOc19va214cG8xTHJZeGFWalhZU29Ydk92LUtYYmc?oc=5) <sub>Gasgoo</sub>
- 📰 2026-11-24 [XPENG WorldGPT: One Model for Cars, Robots, Drones](https://news.google.com/rss/articles/CBMia0FVX3lxTE94NmVKUnQzN3k2aTkzano2ZHFOVHJ0eW9YUUd4bHVCRVM4S0pudmVLOTBFZTI2d3pJbjJUSG5hQ016Q0lXZVlHQ3RJOWFLYjZOTlItODB1c3picW1rbGdQUUk0VHpZMXlsUEl3?oc=5) <sub>XPENG</sub>
- 📰 2026-11-24 [XPeng Upgrades X-World 1.6 With Repeatable Virtual City Driving Tests](https://news.google.com/rss/articles/CBMiekFVX3lxTE52MldnN2d1VUVkeVZEcU9sSGw1bVlzeXFxWWVHWnluUmNQWHNZQWNsM3BsMFRBV1JJMzB6V1FSTFlVSG9HWGI4TlhlX1J6ZnhiM0t1ZDdKZ0ZGUU1IWnRtU0dRd0hfcnN0algtaUd0eG8xQ3pGY2xWSVlB?oc=5) <sub>Pandaily</sub>
- 📰 2026-11-24 [XPeng using AI for cheaper, faster car design](https://news.google.com/rss/articles/CBMipwFBVV95cUxNVFE5MDVYcThaamg3RXRJWmdyMzZtV0FVanFmVURiemxLZTZiSXJwWFpsRGx6WHR4SVhJM2lkaEh1emFtWXItMTI0NGU3NzJZc0hhM2hwaFNPVmNLLTlmOXRpdXZBRUszc0JlM0JsVXliRC1zNExBVmVlVnFwaEhUV1BtbXUxeE9qNHdNNVowcncxUExxODRTVVl4dGczLVhMa0k2LUh3SQ?oc=5) <sub>GoAuto.com.au</sub>
- 📰 2026-11-24 [E Weekly View \| Two Automakers Secure Production Licenses; Leapmotor Produces 2 Millionth Vehicle](https://news.google.com/rss/articles/CBMi7AFBVV95cUxQUFpvWmlRcFhNeVZEVUZxVVBiazRDblhmXzBxTlR4RzU0TmQ0emFNVEZmS3VmQVlRZk54Q0lXYTZlREl1TlZPZDdkZDFEc0w5MTlKaDJtQVhqY0VyNUhTTUJZczNtTmFsY0ZzUnp5QVI0QWJTSnpZTXFTYTN2OHk1b192eFllaEZwV2xQUDRFbEZhRGZsSlp4Y09nZXR6Skt6VW4yRHNYVWdxaWsxd1dQamF3Z2pyb3N0ZGt2S3FxY3p6RW9NbEVIdGhZem9iZ3VhdzB0UjB1anUzSVV5dktQbnVmT0xTdmhraUN0eA?oc=5) <sub>Gasgoo</sub>

</details>

<details><summary><b>Li Auto</b> (187)</summary>

- 📰 2026-11-24 [They Said They’d Deploy Robots Instead of People... China’s Auto Industry Taps the Brakes](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1jTWMzNmJvdEdZWGdxQ21tM0toWmQ5MXpPd2FWN2FMVHFCUU53Y2JXZV8wOXJDdzdha001MUFjOVJhNzZkMW9TQkIzVTI2cmx3MTBn?oc=5) <sub>매일경제</sub>
- 📰 2026-11-24 [理想MEGA Home家庭特别版50.98万值得买吗？3个维度说清+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE90Ry0ySHNkcGhJSFVBZzRDOEp4S1ctaFV0a1JwQlJBZ2lYZWE4b0h3ODR2aUgwalNUZnNBaUhwRUkzRUxvd2xDTC1RVUZXWHFFR2FNQVpwY2FBOU92OWg4Qk5DeHJSMzR4OXJrS1lUdE5xQQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-24 [理想汽车全系上线菁彩声Audio Vivid，UWA联盟车载专题组第二次工作会议同期举办](https://news.google.com/rss/articles/CBMiZkFVX3lxTE1COHV4WWxYdWpKQU1GTkFuTWdjS2FERUVxU283SENuajVrUG5TTzZmbnFvbnBlWFdMdjN1R0Fxd0tkeHBNSmNEdF9sbTVwcHBrc2ZiNTNnOEdBaUh1d3lYQVVGd2c5UQ?oc=5) <sub>汽车大观</sub>
- 📰 2026-11-24 [5座改6座，新款理想L7曝光，即将上市！](https://news.google.com/rss/articles/CBMiW0FVX3lxTE4zWkxOY2RZY0dIbGh2N1V6bmJGRndUNkYtLUZHdFM1OWtDaEVZdTVheGpPWDUyVlYzMEF5eU5pRTlySV9yQXdfd1hNOTdPNEZLZk5jcHJ1Umx6R0E?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-23 [Nio to begin deliveries of refreshed ET5 Touring and ES6 in H1 2027, no updates planned for ET5 and EC6 next year](https://news.google.com/rss/articles/CBMilAFBVV95cUxOT1BIblYxYUxjaXc2UE5fS1hxVlA5S1NXLVZYWk1KdXM0OFBES1diV1A1NWstckQ1U3FnZzRuNkVUNmZzNE1IX2E3ZGlpajZaMU1BcE9OTUVhY2dhSHZtQlU5d1U3NFBXcmpPWFR0QjQxcmhOQy1Dc2FxemI0Ykx5eW5DQU1YYVNqQkZ5TjVYR3ZFVkRr?oc=5) <sub>CnEVPost</sub>

</details>

<details><summary><b>NIO</b> (197)</summary>

- 📰 2026-11-24 [Nio sets Nio Day 2026 for December 19 in Wuhan, to unveil all-new ET5 Touring](https://news.google.com/rss/articles/CBMigAFBVV95cUxQQ3ZDQm5xQThyMWdfd1NNdktLdjFDaG5nMkdrU3pUNnk4VjhXSTFPSW05cFlkQ3F1eU1lRHRrYllQbmJTOS1ZZ1JyU2dGQ0FNTlNUcGo4VkM3QklfSW9NNVJNTUlFWkcwNkRlVDZ6cUhMb080bDc2LXAyRktyR1hGTw?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-24 [BYD Fang Cheng Bao Shark pickup to launch in China on December 2 after Guangzhou Auto Show debut](https://news.google.com/rss/articles/CBMiggFBVV95cUxQR1M1OGF1R29mVU5pZHo5b0tlT21rTl8zWGt5MlpDb2dJYVh0czdlZHNsbDlSTk1tODRvX0xFWUNaNmozQkN0V3V2SkE3ck1KQkVGNVVQcFlFd3E4X2o2LW5admd0SmEtcGtXdW00UTZEQnhHUHctblB6eFp3V2JSMk13?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-24 [【视频】蔚来ES8这次系统升级1.6版本，智驾进步到底算不算大？](https://news.google.com/rss/articles/CBMia0FVX3lxTE5qcS1ZNVZEUnNGV016cUdqVFpJQWI0MlNEUHpXRjNVcE5DMmpZVHVvTW1xMk1EcUk3cm0wUzRNdTNjdmtYMTdSTFpReGluNkJxMktrZUhmd0hLU01hWm5WTng2MEZCa2hTZGRR?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-24 [全新蔚来ET5T谍照：尺寸暴增，智驾看齐ES8，明年上半年交付](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1mbVZpdmE0akxpMEQwUWltbGc4QllzeXJyVEhLSzFwN3ZxbEh4aHdIWEpzLVIxWWVSSWctcU9zcHN0UzZQQzZ6SkZyZVJDZUlyZlNYbXBYNTNJTEk?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-24 [【视频】同价位比一圈，发现还是它好，腾势N8 26.99万起空悬智驾全系给齐](https://news.google.com/rss/articles/CBMiW0FVX3lxTFB6Ums4bU1OQjJ0Z2hpWE9YcDV3LXM3QWZuM19OTmhnck9SRHhmUHZiLWhKTU5KYVRsQW9kWDlNajJsUW9CNm5WSzZTdXVFOUMyQTdzeTlDSWxlWTA?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Huawei</b> (374)</summary>

- 📰 2026-11-24 [Huawei and BAIC Group Deepen Cooperation as STELATO Scales Up Systematic Operations](https://news.google.com/rss/articles/CBMi3gFBVV95cUxOcmFNR3FOSndmdjZheVh6enV5a2IzOFRMOHcxRE11Y2RWVVF5TEM2RkhDdTVLcmlfMVBBMGRRYTlSSGQyWHVMSHBaSVdqRzlrcXRpRnFVUHp5N3BINnEzSEVub2VCdXUyajdWSUpwZWs0cmlhSE1vRDFfcktUTlItdGVIWnltYTV0eVpQZkNsR0pWVk5qUEZsU3NnU3NsV2lMY0p0bGx5aE9hcXh4QzZmalV3SGlzeEZSWEM0emtxbWdrVXNYY3doR1FqY3NmMzYxRElDa21YNHAxZnBQaEE?oc=5) <sub>Gasgoo</sub>
- 📰 2026-11-24 [Nio sets Nio Day 2026 for December 19 in Wuhan, to unveil all-new ET5 Touring](https://news.google.com/rss/articles/CBMigAFBVV95cUxQQ3ZDQm5xQThyMWdfd1NNdktLdjFDaG5nMkdrU3pUNnk4VjhXSTFPSW05cFlkQ3F1eU1lRHRrYllQbmJTOS1ZZ1JyU2dGQ0FNTlNUcGo4VkM3QklfSW9NNVJNTUlFWkcwNkRlVDZ6cUhMb080bDc2LXAyRktyR1hGTw?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-24 [China's Seres super factory named to national smart factory list as digitalization extends to vehicle validation](https://news.google.com/rss/articles/CBMidkFVX3lxTE14cTYxajgwalE0VmdCay10UjN0cVlpT2FRQUdPeENOOWZsNXFoazFEcFktX2NXTG5ZQnBfbXBKMllLSnZoWHY0T255Zk14bVF6Mm5ZaWVqNmRyV2pfVDFYUnNBOVNsdjJjTjRwX1RjX3JITFE0dmc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-24 [E Weekly View \| Two Automakers Secure Production Licenses; Leapmotor Produces 2 Millionth Vehicle](https://news.google.com/rss/articles/CBMi7AFBVV95cUxQUFpvWmlRcFhNeVZEVUZxVVBiazRDblhmXzBxTlR4RzU0TmQ0emFNVEZmS3VmQVlRZk54Q0lXYTZlREl1TlZPZDdkZDFEc0w5MTlKaDJtQVhqY0VyNUhTTUJZczNtTmFsY0ZzUnp5QVI0QWJTSnpZTXFTYTN2OHk1b192eFllaEZwV2xQUDRFbEZhRGZsSlp4Y09nZXR6Skt6VW4yRHNYVWdxaWsxd1dQamF3Z2pyb3N0ZGt2S3FxY3p6RW9NbEVIdGhZem9iZ3VhdzB0UjB1anUzSVV5dktQbnVmT0xTdmhraUN0eA?oc=5) <sub>Gasgoo</sub>
- 📰 2026-11-24 [AITO Unveils New M7 With L3 Ready Architecture and ADS 5](https://news.google.com/rss/articles/CBMic0FVX3lxTE4tYXlVZFVQSVpwa2ZaZGszSzZoYnFqWlR3ejBWU3NHVWp0SWJ2LTZlV3N1V0hNdVRJZjUyQ21fVWNaUXA5ZWV5QXpoQUhrSndWRFpMQ0pYZVV5VC10UzdvQWEtczQ1eko1VjJjTk9hYUNjNlU?oc=5) <sub>www.suaralandak.co.id</sub>

</details>

<details><summary><b>Baidu Apollo</b> (58)</summary>

- 📰 2026-11-24 [11月AppStore中国免费榜（旅游出行）TOP100：滴滴 同程旅行等居前三](https://news.google.com/rss/articles/CBMijAFBVV95cUxNdFBiME03TmtOV0QzQkxDRnhMa3o1bjJLVUZUZ2Z5elJWVGZJencwTzVnMmFCUlVEalNXaGttTVEtejRJVllDWjJRTU1lZk9pY0o5RldBSXphMWZpa1REU1F3ZktBb0tMOU9ZVkpsblVxMENBZ0g4ZUlyQ1RnRlVVQ3hDMjRIN2NfdkRVRw?oc=5) <sub>Sohu</sub>
- 📰 2026-11-24 [时时彩中三开户平台活动，签到30天居然有大惊喜？](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBpNlhrMFlHdDRqMjlfRkhDd1VCYjVaUkNYWm1hQi1xMkplWTJyc3pNeVVCOUlTbUp5NHI0X05nNnVxUDVraG1HMUdQZFpORmprRDR5NGd2aEJpRmVEekxZ?oc=5) <sub>iheima</sub>
- 📰 2026-11-24 [铂智4X每公里1.13元，深圳单车日净收394元](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9oZDY1UE9qRVBPS0VSeDJXQm9QNkVxOExDQmluODJFb0FSZ0NtTFh0YV8wYUIxc2J1V1BjeFBuUmh2c0p5Q0cwWnBaWWpxTS1qLWVZWXgwTk8zeUk?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-23 [Weekly Recap: Baidu reports Q3 results and analysts adjust outlooks](https://news.google.com/rss/articles/CBMixwFBVV95cUxNdTlTaXZBNzdvclRqTU56cllBN21tLURXajNVUzVtRVlibTFETUlVM3gxTDVJVklPZjI1QUg4a1FTQ0RMSDVQSFBBSWNzeHlaeEpSZW1Jd2ZJSDZHakltWnpUT2VUUUltUm94bHB6RGoxNVFvaWg4ckF2WW9hTE0wcDNwMzAxakZBZW1aWTVmSUhwZ0o5WE1wamYxS2NzcTJ3V3hoRDFMUURFcVJvS0JWdkd0eklhckViV0EzMmJvOEFFNzA0QmZv?oc=5) <sub>TradingView</sub>
- 📰 2026-11-23 [Robotaxi market forecast to reach $179 billion by 2034, says Polaris Market Research](https://news.google.com/rss/articles/CBMi1gFBVV95cUxQVVd2N1FiWjJWb2FUMWZuU3NMeUlleEpUVTFFUWppNDk0Vm9lRlNPNWpTQS1ORE5vMXJZSDFfN2lVLXdNUWVJaDB1aEotbHhMQWhobUFqUDZ3QmVsWHhhTk5ueUt1TWlMaGVnRVZMRmttZGdfei1WRUVycVZNbGQ1NVR0TnZfTnpUM09wYjdOSnRTYzJnY3p4X1FacndOa2gxU2pIY2NZLTg2dVA3d0F0OXh3TjQ2TklXcTR0cDZmSFFoZnR2Qk1nY0VzVkl5UHM5QkxTbW5n?oc=5) <sub>Robotics & Automation News</sub>

</details>

<details><summary><b>Pony.ai</b> (153)</summary>

- 📰 2026-11-24 [Silver Pony Provides a Corporate and Technical Update](https://news.google.com/rss/articles/CBMinAFBVV95cUxQWjdaRjVodGNCd1l2VWg4QzFBSHoxcWRGaTQ1R0tFU1BaYWtVQmVEcVpYVUcxNEF2UEZYZ2lVbTFFS3pvd0pMbnpSS0JwMVFqUXI1Sm84TDVLeWFobmQ5eWp5M0RsZDZfWC1JSmY3ZE1WNVhEUmJnVGg0NEl4ZWlLTWxkOVdCTFg1bXFnQ3cwNEN2Q3lGZVY3WjkyOUo?oc=5) <sub>Quantisnow</sub>
- 📰 2026-11-24 [小马智行港股跌5%创新低 募67亿港元基石浮亏81.5%](https://news.google.com/rss/articles/CBMibkFVX3lxTE84bEU1ZnNfWGdsT1h6eFlRQ01Md3hveV9rZEJiWlBONWRoTTZGbWVjUUFQTWloSTUtanpkSWJqTlNKS0tNeTZZT1lLUFE3T0xoRmJKdGxxem9WY1Rtc2REbUZSUlZOWEdzYW9zMUln?oc=5) <sub>中金在线</sub>
- 📰 2026-11-24 [小马智行Q3财报：收入大增75%，Robotaxi收入翻倍](https://news.google.com/rss/articles/CBMijAFBVV95cUxNQmpMdkxvR3NhTjBzZXZ6ZzVXMkpCNUNjdUtDbXYwUVNIX3AwdHZkZ09KZVJUYzlQNjFKTlJCakNybXJHRl95WXFxcVFWcmtNRVN4cDZsUm9vcWdhOVhZMEU0VWh0V2dfOVdNMk8xYm5tVHF3Y2VxM0M0NGxLUDc3MEQxMnlxX0MzNHJJSA?oc=5) <sub>Sohu</sub>
- 📰 2026-11-24 [极狐Robotaxi成APEC靓丽外景，中国自动驾驶加速驶入全球视野](https://news.google.com/rss/articles/CBMigwFBVV95cUxQTC1GMjFoQUtEcXRJT1d6Rk1CNzV6czFCQk9KaVVuNlhkZFdSU2RjMzNfRDRyT3YzUHlya1AtQlNKd2ljNHNoV2Z1QWVGbDJWS0NfRVlvSUtabm9Va0k1bjZYX0lWZEFPQU53VjZ2MzJKRzU0QVVfemE0Z1FYdEZvXzA2TQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-24 [ARCFOX无人德士亮相APEC Level 4智驾技术领先](https://news.google.com/rss/articles/CBMiuwJBVV95cUxNMndjc29VdjRSbUNTY1RvdGoxdzdDRFlWem42UGVTTXhORlBVNmlEbmpjYVlRaUtMSUEwOThoNUE0LWh5T2xia2ZYakVjMVZ4dzdnUzNCTms3TWdHd2ltOUwtbmRGY2pFWkJ3WmUwdlIwRXYzcnNWZ0JnMGlvQ1BkZDN1RjJBSW1GZXh6SFdfLXJ1dUU3QnRHeDlUWW5zRFc0TFdJVldSV0hiMDN6ZXZSY1JpQ2RxU1RuMnRORmJKWWNMZ29lX3ozd1REcTU2dGtXZlFRMWtiTnRrT0xFRnA0eU1UZVpkTnhDWElObFlaRG5taWVpdm9hYm1wSTFqUzlLTUFoQ3JPWkpxeEN6azRZWnVPUTVfWmFOZUZfbnZ5WkZLVEI5d3luMi1nRXRYR0tzRjBmU2hpeUZCSGM?oc=5) <sub>MyWheels 车天地</sub>

</details>

<details><summary><b>WeRide</b> (140)</summary>

- 📰 2026-11-24 [文远知行Robotaxi三季度收入过亿元，同比增长超2倍](https://news.google.com/rss/articles/CBMijAFBVV95cUxPeXM1UjBqRnlkRTdaelFZcGtPQkgzZGlxYjlKWGxtcDNoRHZtRXV0aUVTYTZwamN5N01hMHZDUFNBTzhJWU9FYkNoUDNvUkxMN0JaVWliTFRMcS1iSE13LXhac0xyTHZzRW5LWXMxZVJNVGlqMWJodEVSelQxTEdJT0ZDNzA1ZXBFbElYZw?oc=5) <sub>Sohu</sub>
- 📰 2026-11-24 [文远知行港股上市累跌70%创新低 募24亿港元首日破发](https://news.google.com/rss/articles/CBMibkFVX3lxTE54MUxROEpCaFBQM2tEa3ZVdlVKWXdlYzF2Wk9JQmdlRlZNYzdzZ19FY3V3RGQ4bFhXN05lVXVTY3hQU2NYTlM5QWgxQWVpSVJoZGpIMVR3SG9GMnlwT0lPZ1J4VmlxXzV6YmhYaTZn?oc=5) <sub>中金在线</sub>
- 📰 2026-11-23 [海外收入暴增172%、占总收入近半：文远知行国际化成果持续突显](https://news.google.com/rss/articles/CBMiWEFVX3lxTE5sTkN1aUJXUjVZb0VlRExZVUpzcHVGclhHandicFdGejNJZWhsWXhmUExXRjVVbjFUSXhXQjJoR3luSHBnRmY2RmF6WVlZMEV5NHFHZlBvOVY?oc=5) <sub>驱动之家</sub>
- 📰 2026-11-23 [How Is WeRide's Global Robotaxi Expansion Driving 88% Revenue Growth in Q3 2026?](https://news.google.com/rss/articles/CBMitwFBVV95cUxOOTZVSEY5VzBhMTBrM1lEWkNRbHpRWUVrRE1hbHV0WUlDQWU0NVVwYzdETS1JdTZVd1ZJNjdaaGRhRTJpSE5iMDBzUVQwTDhuYWZSbnI1T1NKVm1DdmdoNkIyLTV6dHFfZWc1T2o2UFE2WGlZbnhpb0cxSHotQzJzMmE3c29TSHVtLTNIVjZJeFlDN0lzT0NJb1AtSUJncEw5UXg3ZWhUYW9vcF96VzJfUmlacjdYcWM?oc=5) <sub>Kalkine</sub>
- 📰 2026-11-23 [文远知行Q3海外营收增172% 占比近半](https://news.google.com/rss/articles/CBMiTEFVX3lxTE5oNjdMcG4yU05YUDJmaFA1eW9TMDlxUDFRb1kxWm9tay0tMU5sM3Z2elBaUmlyR1NuQ1p0MHJucGt0MDdaZGdBUU9KUVY?oc=5) <sub>www.itsdw.cn</sub>

</details>

<details><summary><b>Horizon Robotics</b> (140)</summary>

- 💻 2026-11-22 [HorizonRobotics/HoloBrain](https://github.com/HorizonRobotics/HoloBrain) <sub>GitHub</sub>
- 💻 2026-11-22 [HorizonRobotics/holobrain-0.5-homepage](https://github.com/HorizonRobotics/holobrain-0.5-homepage) <sub>GitHub</sub>
- 📰 2026-11-24 [捷达M6参数配置全解读：8.08万起3款配置怎么选？+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5ibEVWUVNJYzAwYldRWE9mZVRiZVI5ajdqYlBwNE1UMFgwX3Z3Mk1kZnpiUjRUYzhqQ2JJb21uWFBfMF9NM0k3SWxLNmZmYVVhbXRBYWpyaWhwcmcyZm1B?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-24 [方正造型SUV想要智驾好用，旅行者7、哈弗猛龙、深蓝G318、豹5四台车一次说清](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9WczRwWU53ZDBrUW9McjMtazRJWC14ZTdyRE1pRlpHS1VwdjBja2ZCSWhaMDlmV00zUTA2SnJmd3g2eEFWaDEzc2NnWDZZc3A4bmt2bG1Ca1F2ZEFYN1dz?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-24 [大众ID.AURA T6深度评测：12.99万起的合资纯电SUV，凭什么成15万级智驾标杆？+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5Ra3NwUWVZTGVnbGtCS3pzU1hSQXhCcS15QW5jd3FmN2RZWDFFS05zcjJhTVFueU1kVFJQWi1yQWJOQ1lMbXoyengzbXpOc0hYLVBBQ0tFLThzdGRJYVJN?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (18)</summary>

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

<details><summary><b>Aurora</b> (38)</summary>

- 📰 2026-11-23 [Aurora Innovation (AUR): Hedged Position Gains Despite Share Pullback](https://news.google.com/rss/articles/CBMijwFBVV95cUxQZElieFVfYkJWS09MMV83WXRRU0VIQnBITjZNLTNoY1A4RllLdG1rb19DSDlSTHJxbnZmNnFfMUI3YjVhQlhlUXRuUVpra1doQ0p5c21WX1lCRVZtN3lJaExLcEliVU0xUHA5dzk4YVZBVElLOVlrd0pVVnRXTEtlMVBvSUJuQk5PVzloak54aw?oc=5) <sub>Yahoo Finance Australia</sub>
- 📰 2026-11-23 [AUR Investigation: Kessler Topaz Meltzer & Check, LLP Encourages Aurora Innovation, Inc. (AUR) Investors to Contact the Firm](https://news.google.com/rss/articles/CBMigwJBVV95cUxNblIxN0M5MWplVWNpY2dEUzVCcEp3RW1scjlPbjNRNU10YUhvcVIzbDJudXB0clZSa2NKTkdMU3h4cXpER1QyWmFHZnplSGs1ejZtWG9WOGR3TFFkRVBLaERjdkdUV0lVOEJ5NTFVX2JGcEg4V0ozTlVyWmZZQzZYSEtDTXZ6YmpYYmNLQU9oZDdDSWE3TUJZa2w2NDBiT1dEbzRjQUFYN2pfSTQ4MWROVG8zbURueG5aaHUwdVkxaDExLWlidWtzOHhxZk1zaWY5VnhDdlJiaHdKek05Yi1rLVItdEFOUnZnSzZHcjk3ZVJVNVd6dlFqSDhWTkhXM2pKeHVN?oc=5) <sub>PR Newswire</sub>
- 📰 2026-11-23 [McLane to acquire Northeastern restaurant distributor](https://news.google.com/rss/articles/CBMif0FVX3lxTE5CbHJQVXNlSVhiT2NnMUZqSGFBdDdlMkw5QnpRYkhNVmQzSy1pdXRUWDRXVGdBTEkxaWs1OUxwSWFndkZPeGU2NWY0bTY3RTlnVm1oUWwzNERvUE0wcVkydC1qRklqajR4Y2pSdnRENEFzdHhHS2ZFN0lDS0NPM28?oc=5) <sub>C-Store Dive</sub>
- 📰 2026-11-21 [Bot Auto launches ‘Capacity Grid’ with agreements for 200 million miles of driverless trucking](https://news.google.com/rss/articles/CBMi4wFBVV95cUxNenB0d0xhRHB1QW96VjM5dl9yODU5THZxLWtmZEZ1WEc0TGZhQUlDOU1CdlNiR0Flc3ZoTzAyUnVoaEtOSUp4NEVyNXpqVi1vZldPNUY5VXRKUU5hc2xjVm9aZDdiN3R3NE9mUmVtajF0dG1hM1dFTmtJWWVwakMzQ095TjMxZU81VThwYy15T1FaaTJNN3ZEc1BxcDhCX2xjMDdHQ1pxRVNNaWloSUdTUmxkRkt2TUxNdGd4MTNEU082RnBxcUtxV2paVWFEeEJ0Z2t1SWJONG1jTDZIanM0N1QxNA?oc=5) <sub>Robotics & Automation News</sub>
- 📰 2026-11-21 [NADAQ: AUR Investigation Alert: Kessler Topaz Meltzer & Check, LL](https://news.google.com/rss/articles/CBMisgFBVV95cUxOcUdtQkRtc2tPZkc3dTlWUnJ5YjVRZ2xBV3d2RWxTUFU3QmZPV200dlROY3N1R3Q1S2t6dHItRVQxUU1YNFhzOFNtVzVCWEtxVDM4V2FBblhFTE1oTGo1NWhxUTh4SXFEWXVfZmphc1RNaHJVa1ozMGRfYlZoaUtxUlY1b3FONmZmS3hkLTZjNjZHTWtUalM0OHlRQ2hRa1QxRS1WQkd4eHRYWDlzb213amFB?oc=5) <sub>The National Law Review</sub>

</details>

<details><summary><b>Zoox</b> (110)</summary>

- 📰 2026-11-23 [Zoox Cleared July 30 to Charge for Wheel-Free Robotaxis](https://news.google.com/rss/articles/CBMikwFBVV95cUxNZlNkY2VoTDAtMFNkS1NZYnRKcnhhS25wQjBuUU1kLWhOZXVQYkZiSFVmT3FyZkJMdXJ1NHEyLW02d2dHYmZFd0k4SzZTaWozOFZrSFAwVXI1NXRGc1BtTlhiajVwMmtQUDR3cElxX2dkVFlZMmlnb2hmVXQ3TnpaUFhfZmFySm1mOS1UUHRpQ0lfRU0?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-23 [Zoox Passes One Million Riders, Doubling Its Count in Five Months](https://news.google.com/rss/articles/CBMioAFBVV95cUxNc0I0elBwbDBFcGtjZlg0TWtkeTlIZkxENTNHVUlJaEhNYjlZSTZuSWpzVXBoSGYtODBJdDdhaGNQc3ZER2o4eEZ6ejl5M2hZY2VYTGtKVDJ4dkNkY0s5akV6RjN0V1BTSkc4YXYxX2g4dU5URW9BaVc2bjZ6TGJOTmFxUno3a1haNzBzOGpFYmhVTUtQMzk3eVF3MG10emRa?oc=5) <sub>Electric Vehicles</sub>
- 📰 2026-11-23 [Zoox Partners with Uber for Las Vegas Robotaxi Services](https://news.google.com/rss/articles/CBMikwFBVV95cUxQdWg1ZDM4ME9yMDhoQkV1cV9aOHRkZXZGbF9NQTF1TmlXYlkzLVlZSGYtcUhMXzNDVlhyQ1lKU05rRWNtWGNOQ1JhYUNGanZSNnRCRGZsYjByOGpHMDhPOHUzS0dSWDdTU25MVmNmb1ZFUFk0aDJzM1pHMW8zZXlmYkJjc19aek5DUUI2WGwtOFhTbnM?oc=5) <sub>Future Transport-News</sub>
- 📰 2026-11-23 [Inside the Sonic Language That Guides Safer Driverless Crossings](https://news.google.com/rss/articles/CBMia0FVX3lxTE96bWxuOVVTUzJqb1g4TVp3NHBhaGFXN1Q4eUpldU9DQjV3bWdZWm4zVlVtUUE3TVdIUFpXV25nakt3RmVDdlpHaGxPcmh5dVhPOTJvSFl0SFNjV01fUm1nelJ5Q3ZqOUR4Q2dF?oc=5) <sub>IEEE Spectrum</sub>
- 📰 2026-11-23 [This Week in Chancery Court: Zoox, Restaurant Brands Settlement](https://news.google.com/rss/articles/CBMipAFBVV95cUxPb2IxTUdQdHI4YU5HNEp1bW1hNzUwbGV4WVMwWnI0TTY1N25VQ0lmWmU0M2RJd3c1UUQ1Ti1PcE8yR2xhVzZTR1RMaTFYTHluMUpicXB6QWV1bkRvWnJyVkZVM194bndZaXFkNDNHblI1ZVpURm9WZzBTY1c3UWRKVEExVWJqMkJkSDN0enhDQ3Y3YkRYcFp5d09fbDF1UUk5Y0xGUA?oc=5) <sub>Bloomberg Law News</sub>

</details>

<details><summary><b>Motional</b> (27)</summary>

- 📰 2026-11-24 [Hyundai Motor Group Eases Concerns with Jensen Huang's Return, Accelerating Autonomous Driving and AI Collaboration](https://news.google.com/rss/articles/CBMicEFVX3lxTE01c2Rac3ViNDBNSGl3ZXVQZDlDUXRJLXJvSkQ4ejlZRjdYdnN2cGFUZEdXNkVVY3FLTlNycFdIZElWQnh0V0xxR2VubkFQeENnQzJ3bDQ4RFV3T2Y0c0RCT0dJeXhEbFFzSUhxVldmMjk?oc=5) <sub>머니투데이</sub>
- 📰 2026-11-19 [[Why&Next] Supplying Vehicles to Waymo, Investing in Motional... Hyundai Motor's "Two-Track" Bet](https://news.google.com/rss/articles/CBMiZEFVX3lxTE1fcTNiSzhBMzRuMGl2M0FtOTQyYmY5TDR0d3BoRmJ0RXdMYUVnLVlVRUdGYnh2QkFwUFpYdmM4MzhZc3h6a2prSERaU1hNQ2FQOWJzM1pNNnlRU3UwTkV6VjJqOHg?oc=5) <sub>아시아경제</sub>
- 📰 2026-11-19 [Hyundai Motor Company: “Data Flywheel Gap to Widen in 3–4 Years”... Four Group Companies Put 'Data Union' Into Operation](https://news.google.com/rss/articles/CBMiWEFVX3lxTE1KekR0TXpjWmRySUVDc3pyQWw2ZHFIQXhsZV81VzJNYzRxbHVQZDkwNjMxSHZWNlV5d2pBVFFrUERGM3NKZnE1Qnp5SHpSbDJ4UUFVaV9zLUE?oc=5) <sub>파이낸셜뉴스</sub>
- 📰 2026-11-18 [Hyundai Motor Ramps Up Robot Hiring; Muñoz Says "Physical AI Is Our Bet"](https://news.google.com/rss/articles/CBMidkFVX3lxTE5pTkR0WnlGS2hSdDY0Qm05SmV2S3BVMnRiTmh2blBKbHRTOC1HMjhKaE9QY3pqdVdJZlhGcWdJU3JtZW5Ddllua0dYazFPeTJLbVl4QkVfOXp0czRSRnZXUTZzdDUzSlZDck1ON3dNSGdKdFpaWVE?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-18 [Hyundai to Supply Ioniq 5 to Waymo, Expands Robotaxi Push](https://news.google.com/rss/articles/CBMiYkFVX3lxTE1YSzRfd1k1SE1SWGdMNUtMMmxhbzZmYm1QSVA4aXEtWTF3bi05bmk0cVJKOTVZeG1rMkd6dnN3RVlvaUtRNy1OOGZBdkxETENBVjhqcGJtd0gyamVTWFUxV2ZB?oc=5) <sub>동아비즈니스리뷰</sub>

</details>

<details><summary><b>comma.ai</b> (2)</summary>

- 📰 2026-11-23 [Open Source Drive by Wire Kit Retrofits Standard Passenger Cars for Autonomous Research](https://news.google.com/rss/articles/CBMisgFBVV95cUxOYkF5ZVN3eWtSa1FRSnF4Z091VFZlQ2pwZHIybWlxRHhMRXdwWFZMQk43QUNTc3d2VkNRbmNuSGxKUXh1Z0JMN1BfeHFqbFRtM2VnWldHeE9TQ0RVYThPVEpvTnpESTVYWEJZWlJDWWRqbVFYM1dTdFRkWklFd014a2N1d0ctbjlIQy16VW1YYnh1bm1rSmdOdHJvb0JGN1FTbVMzM2F0RUR5RF9SRnNfS1Z3?oc=5) <sub>Bioengineer.org</sub>
- 📰 2026-11-12 [Goodbye, BlueCruise! We Install a comma four in Our F-150 Lightning](https://news.google.com/rss/articles/CBMirwFBVV95cUxPY1o5ekZ4WnpraUxVMHV6OVdyMEtEbjQxQXY5STdJdXlHNlN6eUFZNzFwSnA5cFhHd3pNdTZNNy03dXBOZ1ZoX3RFX2E5V2JNTE9aVlhJaG90bW5YWEdzX2NGXzd3VFZ6NG5JVkFrM3daTmY4UDBTN1I4NWU3eGJqUm9tY1VaRWxoZkp3WDJLNnVLQjN5WG9NMzlxLWI0aVU2TFhLUEZwUE5YUDdUcWFJ?oc=5) <sub>Transport Evolved</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
