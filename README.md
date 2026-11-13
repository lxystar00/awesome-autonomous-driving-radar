# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-11-13 · 1,280 papers tracked · 47 curated.

**Selection rule.** A paper is listed only if it (1) is primarily about autonomous driving,
(2) has public code, and (3) shows at least one strong signal: accepted at a top venue
(CVPR / ICCV / ECCV / NeurIPS / ICLR / ICML / CoRL / RSS / TPAMI, or ICRA / IROS / AAAI / RA-L),
≥200 GitHub stars, ≥3 citations / month, or a well-known lab with traction. Papers are then ranked by a
composite score (venue, stars, citation velocity, LLM rubric for novelty / rigor / impact, SOTA claims)
with a per-topic cap. See [`scripts/rank.py`](scripts/rank.py).

📅 [Daily digests](daily/) · 🗓️ [Weekly digests](weekly/) · 📦 [Raw data](data/)

## Contents

- [VLA / VLM for Driving](#vla--vlm-for-driving) (13)
- [World Models & Generative Simulation](#world-models--generative-simulation) (4)
- [End-to-End Driving & Planning](#end-to-end-driving--planning) (11)
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
| [Scene-Adaptive VLA: Efficient Autonomous Driving via Dynamic Layer Routing](https://arxiv.org/abs/2610.24590)<br><sub>Yujia Yang, Quan Yuan, Jiawei Fan et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 4](https://github.com/yang-luvu/Scene-Adaptive-VLA) | Vision-Language-Action (VLA) models offer a promising paradigm for autonomous driving |
| [Locating and Repairing Domain Shift in VLM Trajectory Planning](https://arxiv.org/abs/2611.10720)<br><sub>Zhihong Cui, Hengyu Liu, Michael Alexander Riegler et al.</sub> | NeurIPS 2026<br>2026-11 | [⭐ 0](https://github.com/ZhihongCui/MoLaRx) | Vision-Language Models (VLMs) are increasingly adopted as end-to-end driving planners, yet they suffer from cross-city domain shift |
| [AutoVLA-D: Learn a Trajectory-Geometric Condition from Reasoning for Autonomous Driving VLA](https://arxiv.org/abs/2611.12382)<br><sub>Yuguang Yang, Zhewen Tan, Canyu Chen et al.</sub> | NeurIPS 2026<br>2026-11 | [⭐ 4](https://github.com/ShivaTeam/AutoVLA-D) | Autoregressive VLA planning usually predicts continuous trajectories as the final output, but driving instructions often describe actions rather than ego states, which weakens direct conditioning on the final continuous … |
| [CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving](https://arxiv.org/abs/2607.04179)<br><sub>Zhaohong Liu, Hao Ye, Xianlin Zhang et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 1](https://github.com/MICLAB-BUPT/CritiqueDriveVLM) | End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving |
| [PixelPilot: Scalable Vision-Language-Action Models for End-to-End Autonomous Driving](https://arxiv.org/abs/2607.04637)<br><sub>Pin Tang, Guoqing Wang, Xiangxuan Ren et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 2](https://github.com/VISION-SJTU/PixelPilot) | Vision-Language-Action Models (VLAs), which leverage the advanced reasoning capabilities of Vision-Language Models (VLMs), show promising generalization in complex autonomous driving scenarios |
| [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)<br><sub>Nan Yang, Zhanwen Liu, Linfeng Zhang et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 11](https://github.com/Zizzzzzzz/MVPruner) | Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings |
| [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)<br><sub>Yuan Gao, Wenting Miao, Mattia Piccinini et al.</sub> | IROS<br>2026-07<br>📑 1 | [⭐ 31](https://github.com/TUM-AVS/Chat2scenic) | Validating autonomous driving systems requires diverse, regulation-compliant test scenarios |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 19 | [⭐ 556](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
| [GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives](https://arxiv.org/abs/2609.39601)<br><sub>Qize Yu, Lianrui Fan, Boyu Chen et al.</sub> | arXiv<br>2026-09<br>📑 3 | [⭐ 437](https://github.com/groundingpi/GroundingPI) | Precise grounding matters |
| [GRAVA: Grounded Reasoning-to-Action Representation and Learning for Autonomous Driving](https://arxiv.org/abs/2609.15169)<br><sub>Xiao Liu, Haoyu Li, Jianghao Leng et al.</sub> | arXiv<br>2026-09 | [⭐ 487](https://github.com/AhernResearch/grava) | Driving vision-language-action (VLA) models increasingly reason before acting, but their intermediate reasoning is often weakly grounded in physical scene evidence and loosely connected to executable behavior |
| [Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air](https://arxiv.org/abs/2605.31066)<br><sub>Tianle Zeng, Yanci Wen, Xueang Yu et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 1,133](https://github.com/louiszengCN/CarlaAir) | Recent aerial vision-language-action (VLA) models show promising single-UAV capabilities, such as tracking moving objects and navigating to language-specified landmarks |

## World Models & Generative Simulation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [FrozenDrive: Zero-Shot Text-Guided Driving Scene Generation and Data Augmentation with Parameter-Free Frozen Diffusion Model](https://arxiv.org/abs/2606.20110)<br><sub>Yuhwan Jeong, Hyeonseong Kim, Daehyun We et al.</sub> | ECCV 2026<br>2026-06<br>📑 1 | [⭐ 10](https://github.com/daehyunwe/FrozenDrive) | Synthetic data for autonomous driving is surging, powered by diffusion models that promise scalable scene generation |
| [MESSENGER: Memory-Enhanced Sequential Scene Flow Estimation via Autoregressive Next-Frame Forecasting](https://arxiv.org/abs/2610.10759)<br><sub>Jiuming Liu, Jianing Li, Mengmeng Liu et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 0](https://github.com/liujiuming123/Messenger) | Scene flow can capture low-level 3D motion displacements in dynamic scenarios |
| [ASTAD: Asymmetric Style Transfer for Synthetic-to-Real Adaptation in Autonomous Driving](https://arxiv.org/abs/2606.29286)<br><sub>Dingyi Yao, Xinqi Zhang, Lihui Peng et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 2](https://github.com/Dingyi-Yao/ASTAD) | Synthetic data mitigates the data scarcity problem in autonomous driving perception |
| [Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends](https://arxiv.org/abs/2606.01164)<br><sub>Jiuming Liu, Chaojun Ni, Mengmeng Liu et al.</sub> | arXiv<br>2026-06<br>📑 9 | [⭐ 251](https://github.com/liujiuming123/Awesome-Interactive-World-Model) | With rapid development of large language models and diffusion-based content generation, world modeling has attracted increasing research attention, benefiting various downstream domains such as game engines, embodied AI,… |

## End-to-End Driving & Planning

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [MOJITO: Modal Joint Learning for Unified End-to-End Autonomous Driving](https://arxiv.org/abs/2607.23511)<br><sub>Zhijing Cheng, Xuancheng Zhang, Donglin Di et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 32](https://github.com/mumucc01/MOJITO) | End-to-end autonomous driving systems commonly follow a cascaded two-stage pipeline where a perception stage compresses multi-modal sensor inputs into a compact context and a downstream planner predicts trajectories cond… |
| [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](https://arxiv.org/abs/2609.26792)<br><sub>Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.</sub> | CoRL 2026<br>2026-09<br>📑 1 | [⭐ 15](https://github.com/VAIL-UCLA/DreamStream) | Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions |
| [DriveMLP: When Training Strategy Outperforms Model Complexity in Autonomous Driving](https://arxiv.org/abs/2610.29676)<br><sub>Alessandro Canevaro, Julian Schmidt, Hang Yu et al.</sub> | CoRL<br>2026-10 | [⭐ 6](https://github.com/alessandro-canevaro/DriveMLP) | Learning motion planning policies that remain reliable under closed-loop execution is a central challenge in Autonomous Driving (AD) |
| [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)<br><sub>Shen Zheng, Anurag Ghosh, Gaurav Parmar et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 32](https://github.com/ShenZheng2000/WarpI2I) | Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs) |
| [G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance](https://arxiv.org/abs/2606.26017)<br><sub>Hang Yu, Ye Jin, Alessandro Canevaro et al.</sub> | IROS 2026<br>2026-06<br>📑 6 | [⭐ 7](https://github.com/HangYuu/G2DP) | In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors |
| [SimWAM: A Simple World Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.07468)<br><sub>Zongchuang Zhao, Xin Zhou, Tianyang Xu et al.</sub> | arXiv<br>2026-08<br>📑 14 | [⭐ 209](https://github.com/H-EmbodVis/SimWAM) | In autonomous driving, World-Action Models (WAMs) have improved end-to-end planning by transferring video dynamics priors to action prediction, but many still couple planning with future-video generation at inference, in… |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 19 | [⭐ 364](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
| [Latent-Centroid Steering: Single-Pass Classifier-Free Guidance for Command-Aligned Autonomous Driving](https://arxiv.org/abs/2608.00237)<br><sub>Meibo Hu, Jiamian Wang, Pichao Wang et al.</sub> | IROS 2026<br>2026-08 | [⭐ 2](https://github.com/codingmlinprocess/LCS) | Vision-language models (VLMs) have recently emerged as a promising paradigm for end-to-end autonomous driving, enabling agents to map multimodal inputs and high-level navigation instructions directly to executable trajec… |
| [HEAT: Heterogeneous End-to-End Autonomous Driving via Trajectory-Guided World Models](https://arxiv.org/abs/2605.19631)<br><sub>Hoonhee Cho, Giwon Lee, Jae-Young Kang et al.</sub> | RA-L 2026<br>2026-05<br>📑 2 | [⭐ 0](https://github.com/heat2026/heat2026.github.io) | End-to-end autonomous driving has emerged as a compelling alternative to traditional modular pipelines by directly mapping raw sensor data to driving actions |
| [STAGE: STyle-controllable Action GEneration for personalized autonomous driving](https://arxiv.org/abs/2607.29517)<br><sub>Zihao Liu, Xing Liu, Yizhai Zhang et al.</sub> | RA-L<br>2026-07<br>📑 1 | [⭐ 5](https://github.com/CarlDegio/STAGE) | Driving style refers to the behavioral preferences that drivers maintain during driving, shaped by their diverse experiences, habits, and needs, and is typically reflected in varying levels of aggressiveness |
| [A Survey on End-to-End Autonomous Driving Training from the Perspectives of Data, Strategy, and Platform](https://arxiv.org/abs/2610.00926)<br><sub>Chengkai Xu, Yiming Cui, Jiaqi Liu et al.</sub> | arXiv<br>2026-10<br>📑 5 | [⭐ 109](https://github.com/Jiaaqiliu/Awesome-Training-Ecosystem-for-E2E-AD) | Autonomous driving is a cornerstone technology for the future of intelligent transportation, where end-to-end learning has emerged as a transformative paradigm that directly maps multimodal sensory inputs to driving acti… |

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
| [Deformable Gaussian Occupancy: Decoupling Rigid and Nonrigid Motion with Factorized Distillation](https://arxiv.org/abs/2605.28587)<br><sub>Yang Gao, Wuyang Li, Po-Chien Luan et al.</sub> | CVPR 2026<br>2026-05<br>📑 2 | [⭐ 24](https://github.com/vita-epfl/DeGO) | Understanding dynamic 3D environments is essential for safe autonomous driving, particularly when reasoning about human-centric, nonrigid agents |
| [Horizon3D: Sparse Radar-Camera Fusion for Long-Range 3D Perception in Autonomous Driving](https://arxiv.org/abs/2606.31096)<br><sub>Geonho Bang, Geunju Baek, Dongyoung Lee et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 26](https://github.com/geonhobang/Horizon3D) | Long-range 3D object detection is critical for safe autonomous driving at highway speeds, yet existing radar-camera fusion methods remain limited at extended ranges |
| [Explainability-Aware Frustum Attack: Exposing Structural Vulnerabilities in LiDAR-Based 3D Object Detectors](https://arxiv.org/abs/2606.29963)<br><sub>Chengzeng You, Binbin Xu, Soteris Demetriou</sub> | ECCV<br>2026-06 | [⭐ 2](https://github.com/SecMindLab/Saliency_LiDAR) | The structural vulnerabilities of point cloud-based 3D object detectors remain poorly understood |
| [DRS-VPT: Directly Relocalizing in a Scan with Vision Point Transformers](https://arxiv.org/abs/2609.12557)<br><sub>Lanke Frank Tarimo Fu, Maurice Fallon</sub> | ECCV 2026<br>2026-09 | [⭐ 11](https://github.com/ori-drs/drs-vpt) | We present DRS-VPT, a feed-forward transformer architecture for foundational image-to-scan registration |
| [PointLAM: Local Attentive Mamba for Efficient Point-based 3D Object Detection](https://arxiv.org/abs/2609.21780)<br><sub>Xuanming Shang, Weijia Zhang, Chao Ma</sub> | ECCV 2026<br>2026-09 | [⭐ 5](https://github.com/PointLAM/PointLAM) | 3D object detection from LiDAR point clouds faces a fundamental dilemma: voxel-based methods achieve efficiency at the cost of geometric quantization, while point-based methods preserve fidelity but suffer from prohibiti… |
| [PriorMaskMap: Robust Online Vectorized Map Construction with Biased Priors](https://arxiv.org/abs/2610.39283)<br><sub>Haoming Xu, Wei Li, Yu Hu</sub> | ECCV 2026<br>2026-10 | [⭐ 1](https://github.com/healenrens/PriorMaskMap) | Online vectorized map construction provides autonomous vehicles with essential, real-time semantic and geometric scene understanding |
| [Vernata: Self-Supervised Learning of LiDAR Point Representations](https://arxiv.org/abs/2608.06919)<br><sub>Oliver Lemke, Alexander Liniger, Abel Gawel et al.</sub> | IROS 2026<br>2026-08 | [⭐ 22](https://github.com/rai-opensource/vernata) | LiDAR serves as a primary sensing modality for robots operating in outdoor environments |
| [Towards Compact Autonomous Driving Perception with Balanced Learning and Multi-sensor Fusion](https://arxiv.org/abs/2606.02979)<br><sub>Oskar Natan, Jun Miura</sub> | arXiv<br>2026-06<br>📑 47 | [⭐ 9](https://github.com/oskarnatan/compact-perception) | We present a novel compact deep multi-task learning model to handle various autonomous driving perception tasks in one forward pass |

## Motion Prediction & Behavior Modeling

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [MolmoMotion: Forecasting Point Trajectories in 3D with Language Instruction](https://arxiv.org/abs/2606.18558)<br><sub>Jianing Zhang, Chenhao Zheng, Yajun Yang et al.</sub> | arXiv<br>2026-06<br>📑 17 | [⭐ 153](https://github.com/allenai/molmo-motion) | Motion forecasting is central to visual intelligence: agents must anticipate how objects will move in order to plan actions, reason about physical interactions, and synthesize realistic futures |
| [Flow-ERD: Agent-type Aware Flow Matching With Entropy-Regularized Distillation for Diverse Traffic Simulation](https://arxiv.org/abs/2607.06957)<br><sub>Seulbin Hwang, Kiyoung Om, Dae Jung Kim et al.</sub> | RA-L<br>2026-07 | [⭐ 0](https://github.com/seulbinHwang/flow-erd-project-page) | Realistic and diverse traffic simulation is essential to autonomous driving development |

## Datasets & Benchmarks

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [The Road Ahead in Autonomous Driving: The KITScenes Multimodal Dataset](https://arxiv.org/abs/2606.02956)<br><sub>Richard Schwarzkopf, Fabian Immel, Alexander Blumberg et al.</sub> | NeurIPS 2026<br>2026-06<br>📑 2 | [⭐ 30](https://github.com/KIT-MRT/kitscenes) | Existing autonomous driving datasets have enabled major progress, but fall short in sensor fidelity, map completeness, or geographic diversity |

## Safety, Robustness & Evaluation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [CCFM: Collision-Constrained Flow Matching for Safety-Critical Scenario Generation](https://arxiv.org/abs/2607.04451)<br><sub>Ke Li, Kaidi Liang, Yuxin Ding et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 3](https://github.com/KELISBU/CCFM) | Evaluation of autonomous vehicle (AV) planners in safety-critical closed-loop simulation is essential for real-world deployment |
| [Lipschitz Optimization for Formal Verification of Homographies](https://arxiv.org/abs/2605.23203)<br><sub>Jean-Guillaume Durand, Panagiotis Kouvaros, Maxime Gariel et al.</sub> | CVPR 2026<br>2026-05 | [⭐ 3](https://github.com/jeangud/homography-verification) | The adoption of vision neural networks in regulated industries requires formal robustness guarantees, especially in safety-critical domains such as healthcare, autonomous vehicles, and aerospace |
| [CADET: A Modular Platform for Evaluating Distributed Cooperative Autonomy in Connected Autonomous Vehicles](https://arxiv.org/abs/2606.04072)<br><sub>Pragya Sharma, Brian Wang, Mani Srivastava</sub> | ICRA 2026<br>2026-06<br>📑 1 | [⭐ 0](https://github.com/nesl/cadet) | Deep learning models are increasingly central to autonomous vehicle (AV) pipelines, yet their integration has traditionally followed a monolithic design where perception, planning, and control execute on a single onboard… |

## 🏢 Industry Tracker

Latest 14 days of news, official blog posts and new open-source repos from tracked companies. Full daily feed in [`daily/`](daily/).

<details><summary><b>Waymo</b> (138)</summary>

- 📝 2026-11-05 [How the Waymo Driver Manages Severe Winter Weather](https://waymo.com/blog/2026/11/winter-weather-preparedness) <sub>official blog</sub>
- 📝 2026-11-05 [Rethinking What Freedom of Movement Feels Like for Women](https://waymo.com/blog/2026/11/because-women) <sub>official blog</sub>
- 📰 2026-11-13 [Body-cam video shows Denver police trying to question a driverless Waymo after chain-reaction crash](https://news.google.com/rss/articles/CBMixgFBVV95cUxPTlFWX0xYRWZFWHctNkVWbHVDRGhoa1Y2TG02QnBzT3pYNDZwNmRtNHdhaVotOHM2TjBRdlFBeFlzZ0kzd096cVZwaUFSa3NDMEtrU3JEb2pOTWkyYzRNRG02NTlYRHA5aUpvQ3BNNElPUE5oM2NtdmcyTlU2ZGxCSTlaRUZ2YUhydlJ0eHVQbEdZNVpwT21udzZnTWE2c21NWHlCY0Nrc1RjQkZrN01tOWZtODR2LUZ2ZDJlTE9QcU43b0p1amc?oc=5) <sub>9News</sub>
- 📰 2026-11-13 [Waymo launches self-driving rides in Las Vegas, covering 24 square miles](https://news.google.com/rss/articles/CBMiugFBVV95cUxNZWpvSVpzeHk3ZXFfWVFNaHBhMktrbFVLZUpIRWo2TEJMSHprak5YMDRVUGFCMk9NZW9kQmxkb0E3TTNQZ0J4RjJJRnFtbUpwdHZUYW1MU3dmUVhyXzBldHRQS3I5TnFBVXAtY2h6RURkR0Z5MDItMk5vSDctb2ppQldQVEFITDNaS3Bfd2VnTWVEODZWQ2J3UmRDdkdfMmozWTNDMWZUM2xNVWJibzNLWTdxd0tvd0M1QkE?oc=5) <sub>KSNV</sub>
- 📰 2026-11-13 [Most reported Waymo school bus violations came after a software fix, triggering a new probe](https://news.google.com/rss/articles/CBMiigFBVV95cUxPbEJ2blFBN0RUT1dBNzdvemJfOFNraHZYZldtUDRlc1BZeVA0R0JEVm5UYWRSVGFGRTNUSGYwQnVUR3gwZlRFNWpvSEktVGpjRFVTcU5iWlJlR0Q5N1Q2QUw3dmFPQnhKSzdtX3JwX2x6NW9obXRyaUxiSXZoYXpWQVp1TGpLV09ZVUE?oc=5) <sub>The Cool Down</sub>

</details>

<details><summary><b>Tesla</b> (178)</summary>

- 📰 2026-11-13 [Tesla FSD Supervised at NZ Expo: 5 Details That Matter](https://news.google.com/rss/articles/CBMikgFBVV95cUxQbWdIQVhfNS1GRnhnRkltVjlPQ2NnMWpWSDNJYkloZzg2Z183aVBncTZIdlVvcWx4bFZlamRzRW1zUU93RmFOYk44OFpMVkF2MktoSXAwaWlqWXBUVWx1M1VKbEFEZV9OVV8xcDJKYVVTSGh2OWVaZUJ5ZDA5ZGVjME56WjhSQkdfU3FpUnNETlZwUQ?oc=5) <sub>BASENOR - Tesla Accessories</sub>
- 📰 2026-11-13 [Tesla Robotaxi Hits San Antonio: 274 Sq Mi [2026]](https://news.google.com/rss/articles/CBMinAFBVV95cUxPdmpRRE5GblA1R0VvSEQwUVVTNmsyaUVUeF9HR0hkSjFyUTRuQXRIUDZQT3BvVGVXZkRXX1RFMlRjczRLZlZQNnNrdGthcnN5QllKbHBlTE5yNVZjdXpMc1VMTHhSN09DRHU5ZW5MWXBOYmtWaVRzNGk4dHJ5NWV3czZ2cFNmd0N6QmwxVllzbmZobDd2SlZuOGctOFY?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-13 [Tesla Phases Out Standard Autopilot: Users Must Buy FSD or Choose Stripped-Down Base Version Without Intelligent Driving Features](https://news.google.com/rss/articles/CBMiU0FVX3lxTFBpdy0za1h2NVFtR09UZEV5U3pwdlo2MzRMcnpZQ2Y3eVlaMTdBdUQwMjFIeVVoblpVMnBicHRkaFJkb1l0c2dESXVZSE9WekIxblQ4?oc=5) <sub>eu.36kr.com</sub>
- 📰 2026-11-13 [Texas is getting rather SPOILED with Robotaxis. San Antonio just became Tesla's FIFTH city in the state. Its new launch zone covers around 274 SQUARE MILES. The biggest opening-day area yet. The service now covers downtown and stretches towards the](https://news.google.com/rss/articles/CBMibEFVX3lxTE9LUWNva3ZTRjZBekQwd3gwRmFZd1lSdWMyNjdpLTV1X0RvSXpNc3ZpY2RqLVFEVm83MXVKaWhJbWZBUnZRRVppNDFvMnhudTQ2akpOSkdxOG84NXFTdjQ3Y2h6ZFByRC1HU2ZPMg?oc=5) <sub>X</sub>
- 📰 2026-11-13 [How Tesla FSD Monitors 360 Degrees Around Your Car](https://news.google.com/rss/articles/CBMijgFBVV95cUxOSUtfQ2daQ0VzREhaN3AzTlNFRThLZDg0bnA2cUJjMGRNRnhpbHNXLVM5M3Iyb3cxTGxVbHV5RExGQXBqNERKc0ZKMXNEdWc4VXJhMmVYbnpaWHA5SnpHUkRnU3Z5bmZmVkdzazg3eDdfaE4xdHY5blpBajZCRUlvVlQwQ2NOajFoQ0p5akNB?oc=5) <sub>BASENOR - Tesla Accessories</sub>

</details>

<details><summary><b>NVIDIA</b> (120)</summary>

- 💻 2026-11-02 [NVIDIA/nvperf-core — Core NVIDIA Nsight Perf SDK APIs and libraries for collecting and analyzing GPU performance data directly from application code.](https://github.com/NVIDIA/nvperf-core) <sub>GitHub</sub>
- 📰 2026-11-13 [Fallout from the Nvidia scandal may dampen the exuberance around the AI boom](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQeEZnNG9Ec3V4bVhSRHpZcVpsMmZyVzhQZE1SODNpYXgtd1BGcklSSEtTMDFwd1pBX0ttU21oaFJYRDJTaGQ2UkFCZldNdm5fcXRjQXhMNXlJRmZMVHlUY2ZLVTZyZUV6bFJGVUc4Rlc5QnRuWFNsVVk3VUJFTk56dVg3dWU5dEc0Y01LcHRRSE9aa0dvZldxd2VWbThNUURmLUptT3dPRkM5MlU?oc=5) <sub>Audacy</sub>
- 📰 2026-11-13 [Trading Day: Weathering the Nvidia storm](https://news.google.com/rss/articles/CBMihgFBVV95cUxOdlRiUzVpMWdlaWkwR1N1MU80UTc0Sll4UTZGcnFOXzVhbG1WUG5qZi10dXZJOVdsUWZJVWNKQVFLUGVZSi11TnZhTTJpY05aRl9ROWVXQWVfZDBvQ0pGNURBeUxvLTNicWt1QzFEN2tQTGFUcWE5dXg3eDYwdHNHWklzRzJlQQ?oc=5) <sub>93.3 The Drive</sub>
- 📰 2026-11-13 [Evening Wrap: ASX 200 slides as NVIDIA woes, bond yield spike and falling commodities drive broad sell-off](https://news.google.com/rss/articles/CBMiqwFBVV95cUxPc1pzOXV5Vmc0dmdOU3ZQV3ZfSzNUd18tY1hfaTdlSjZqOGgyci05LW9VTzh5QklGNktzay1BNnIzYmZxeHZUcWNJTXhDNUtvZ2lmY2lqZUJtM1NMYWxwRlpYTlZmRG0tNXp6WHAtTnlObm9lVlFFRlhDNTRBaVphWHFpaElkaVVoWDBZd3dPaGtodDc2eF9rSXFNOHVQLTBNV0RrNkVXM0FEYkU?oc=5) <sub>Market Index</sub>
- 📰 2026-11-12 [Morning Bid: Jensen hangs on as Nvidia tumbles](https://news.google.com/rss/articles/CBMijgFBVV95cUxPTlJzTHY4Q3VzUF9fS1ZwWlFrUWdPSi1WbTJDSVBpbXUybVpRUlVvajVLakJYcldpNi1raUwyT2R5RTAxM2REclViNDZST3loTVE3elhGQnZ4VUh3M0pMRTBLOC1zM3Q1OEk5REpZZkw5LXFUZkFpM3I3Nm5aaGRBZmFSNmtvSG5tM0R4ekV3?oc=5) <sub>93.3 The Drive</sub>

</details>

<details><summary><b>Wayve</b> (35)</summary>

- 📰 2026-11-12 [AI Startup Wayve is Charting a New Road](https://news.google.com/rss/articles/CBMidEFVX3lxTE0ya29aQXBDRTd1VWFUMHlSdVNwWmRyQW0zZkExNHdvMVNHUHBkcmVaNm5fNWMwU1VQbDU3YXNkQ3lOYzVVb3VZcmpYVjRUWTNBZ2hTeHFTX0pmUC1sZHUyVURLMmZ2dFJQMXh6U2ZnMTNNdFN1?oc=5) <sub>J.P. Morgan</sub>
- 📰 2026-11-12 [Brits lead the world in hating self-driving cars, and there's one big reason why](https://news.google.com/rss/articles/CBMiiwFBVV95cUxObEZNNndscVpKcWVER1JFMUVyTmdvOFNtdG9jMnRscHFjLXFMLUtVdjl4cGtkZkFUMnZmV0duUkpCSkY3a2RJcnB5TFNqRGlzbGJaQTlVWnZrMlhkalZRTWhYSVlLc2NnbjBfblVrNXI1RHMxS0lYa0d3M054NDFMeENYZzRLRFhmcnB3?oc=5) <sub>Auto Express</sub>
- 📰 2026-11-12 [Agile Robots Raises 500 Million Dollars at 8.5 Billion Valuation](https://news.google.com/rss/articles/CBMiZkFVX3lxTFB0Mi1XZFA0Rm5Bek12cXNKNHdNZ0lBNTF2bHE1TzZ2b1ctQzVURXFVVnhlTFdGejNmb0NvTFkxbXBzcENjc29oX1k1VTRib0NzS0pRTkpFajl1UmRBQTJKeVREdWpGZw?oc=5) <sub>SuaraGarut.ID</sub>
- 📰 2026-11-11 [Wayve accelerates autonomous vehicle AI with CoreWeave](https://news.google.com/rss/articles/CBMiogFBVV95cUxQTk9NV0lfWjVZQ0pwSnlmcHJ4NXlpU1RxOHhITm9XVmJfeExYdU9OSHE0MHBua1l5Q1JicDlQWUZkcDdkTFJDcEFQaWRUNGw2NVlxTmdTWGQ3alBMb1l4TGZZbHZXSmxnZ1BlVUdLZVAtc0RkekVhNl96R245S0liVkpBQmtHdFd6T19zRF91MDVDOFVZV1FFVWRMSWJFZnkxaEE?oc=5) <sub>Computer Weekly</sub>
- 📰 2026-11-10 [Wayve bets its driver on rented Blackwell muscle](https://news.google.com/rss/articles/CBMisAFBVV95cUxPUDZ6bGVHcndyRzNMVzNqdTdWVHUyT09VTG1FNkVNd05iVWpNTTgtb0p3ZHRLUlFUd2c4U2Y5bzYwX1pKeHh2RnhFRUZ4MTg5TXJPZzhDUUJEU0hyTF8zcWNKX05lOUItQVNpTEhfTk4zS0d1bkN0NnVxNm1SNzlMbmI0UW9QSk1uMUNwRVlSNFZ2S3oyMmw2d2JobUV4bGpPdFFmMnJiLWI3MmxRdjdGYg?oc=5) <sub>StartupHub.ai</sub>

</details>

<details><summary><b>Momenta</b> (69)</summary>

- 📰 2026-11-13 [把智驾和电驱做成透明模型，这次发布会看得比参数表更直观\|Momenta\|东风日产\|AI 云擎电驱\|NX7_新浪新闻](https://news.google.com/rss/articles/CBMiY0FVX3lxTE1CVlppZ1NIX1dXNGZNZFR4bG1ldjRmTEEyUlR4RnlvTm5BV1BYTjlOc3h1MmlXcmhhMmFwUFk0VWNveHpvWjk0QVlBVU1QdENOdGdDclRxMm5nYTBzZV8zb0ZtVQ?oc=5) <sub>新浪网</sub>
- 📰 2026-11-13 [凯迪拉克XT5插混版智驾值得买吗？3个维度说清+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE14Q3pIU1pNWVlObVhxS1lDUVMtclh3S3BNRFNfTGNZRjltWjhFSHROUkR4bzhFWTdaT1JjRWVTaUp2UDVoSlZHYW43ajhnU01rMjF0djlLcUZISVpoNGlNNUQ5UHZnYklCM2N4d0NpcWRGdw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-13 [Momenta R7世界模型上车 日产NX7预售在即合资品牌智驾如何破局？](https://news.google.com/rss/articles/CBMia0FVX3lxTE1wdFF5eFZxcWVadTRybEphSGd0b0FTSnFISGdmU21SX2NQR1hxS0ZDZzM2cW9OeWhteFNFVkVXNGhjTXFKeHB0cHV6OWhVc1lIU0ZGd3VrZ1o0QXE0T1h0bVBrREYxOFhrb0Fz?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-13 [20 万内插混首选？看 GTR 同框，NX7 把舒适和智驾揉进车里\|Momenta\|东风日产\|战神 GTR_新浪新闻](https://news.google.com/rss/articles/CBMiY0FVX3lxTE50Q04yYkVURHZXdTlZRUoxV3BQX244WVpwT3NEd3Mtejg2cFpwdjF5V25qaUdiU3FDNVBpX29IMmNVU1lOdVI2YTlNTEd0bllnWFphLTVYWmMtMmFRTGQxYVBRMA?oc=5) <sub>新浪网</sub>
- 📰 2026-11-13 [【视频】ID.ERA 9X 2026款 Max四驱版](https://news.google.com/rss/articles/CBMia0FVX3lxTE1JUE9PRmdMQjQ2NUxzeFVtUEJWUzg2MU54UGFwZ1YxbHF3bWtVQWRfLTl1aEphLXFzRzZrWE5CMmxuRHJ0dVRMSGxsSlNXenYxaVc3VVB6TExMbk1HRDJKejVWQVh0WlYtSGhR?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>XPeng</b> (130)</summary>

- 📰 2026-11-13 [23.18万起的小鹏G9L，智能座舱与智驾能赢过问界M7、理想L8吗？三车大五座横评+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE5HdEtkcHA1SVFaaWIxZ2VYc2RxeTNxamJuVnRwdFpMMkN4OE9QV0dmdUVPbUVMOEltQzU5MmZFY0VHZWhqV1NMc3ZERkRkNnR5bVk5LXJIVmVQS2FEeUV0bG5MUExsaXVRa3Jfc3A2Z1RMUQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-13 [23.18万元起的小鹏G9L，对比问界M6、理想L6、问界M7，智能大五座SUV该怎么选？+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE1lSml0blFaRzBhRDhrX2hoTTRNRzBOZ3RNeERQYXFJNlpnUEpmTDNpNXhZX2JZY1dDREFkd2lZVmthV0haZ2ZBQWZuckZpN3BkZjRoOEpCNThUUnd5Z3N1SjE0UGFCTG8yLUg3cmpWZmx2UQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-13 [23.18万起的小鹏G9L、问界M6、理想L6怎么选？25万级大五座SUV三车横评+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFBVODRjREpyeEt5MXVrS0JJY2YwaHlKNlhITDRfM3N0M0F5aVlEZ08xbWg1bG9KWnpHUkxZVnZUaWNkaEZLQ2ZucFlQdzRCNGJLYjFPVGQ0OURjcmdmZExzSVlvUmFpNjdFSE1CanBlYTlCdw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-13 [25万预算大五座横评：小鹏G9L、理想L6、问界M6、乐道L80谁更值](https://news.google.com/rss/articles/CBMickFVX3lxTE93YloxZjBLZXFwNk1kbk5jV2tBeDlYd253YVBjWFV5SlBySUVjQmJ0ejZUUkRhZnI3VFpvZTlhVnIzeGwxVjBnTjhON2lfYXVuZ0VQMnd6TXMyTGhlUWdZeEI3eGtqNFQzcjZ4VG5PNU9tUQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-13 [25万级大五座SUV选谁不纠结？小鹏G9L、问界M6、理想i6三车横评+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE8xY2MtWXJkcGU2ejBJOXFrT2FOTk5meURuSl9pbVlpM2g1bkF4RmhTdUtUTnFzZzNwY1NaMThhNHFZcjlMM0E3T0hfeVEyYWtBdHFWR2ZiMExBV2NCNjJj?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>Li Auto</b> (129)</summary>

- 📰 2026-11-13 [Li Auto's 6-seat electric flagship i9 tops 10,000 deliveries less than 2 months after launch](https://news.google.com/rss/articles/CBMic0FVX3lxTFBUX1l4YmRoaWFFendhTU5UdFV3ODZ3czFBS2ZPT1B5RG12aXZSb2tJMEhPc3RXeXNicjJRb0o1RV82Q0xkUHkzT1daa1hCcW5WWmhidnVwMEdMVkpoRjJ1VWp5bUNtelZ1alR3akhKN1VqYkk?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-13 [Li Auto enters Singapore with biggest electric seven-seater](https://news.google.com/rss/articles/CBMipAFBVV95cUxPSnVVMVg4VXJndEgzblUxZkZPdXlYd010dXhPOHJ1QWJlRzVCLXppVWxCSWpwWnJuR1p2RHQxMm0tbmpJMlJ3UXBjSXFWQVBxM0tpNTdiY1pKUFYwUU51OUxtTkhLVjRWVUNwVXhxZlNYZFV1UmpfVEcyT0pnTGxTRmNmQlFvQ1JsaXZvS19vX2ZxWWZRenR2V1JWTVVCZUJmaHY1OA?oc=5) <sub>The Straits Times</sub>
- 📰 2026-11-13 [Changan seeks to sell 10% stake in Avatr at implied valuation of $4.7 billion](https://news.google.com/rss/articles/CBMidEFVX3lxTE1uanlOMHRrZkNjeXNqSE9OcmJ4d3RUeTFCREpqU3NXa2RRWDJoV2RtUVhWOUFySFY2VkplRzYzeDRqSzNGcFlvZ1NHV2hUelh3dTVqNTF2cXdlWEtqUzZBdkQ4T2MtWlB0VW1BTjBkWlV5MVBR?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-13 [23.18万元起的小鹏G9L，对比问界M6、理想L6、问界M7，智能大五座SUV该怎么选？+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE1lSml0blFaRzBhRDhrX2hoTTRNRzBOZ3RNeERQYXFJNlpnUEpmTDNpNXhZX2JZY1dDREFkd2lZVmthV0haZ2ZBQWZuckZpN3BkZjRoOEpCNThUUnd5Z3N1SjE0UGFCTG8yLUg3cmpWZmx2UQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-13 [23.18万起的小鹏G9L、问界M6、理想L6怎么选？25万级大五座SUV三车横评+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFBVODRjREpyeEt5MXVrS0JJY2YwaHlKNlhITDRfM3N0M0F5aVlEZ08xbWg1bG9KWnpHUkxZVnZUaWNkaEZLQ2ZucFlQdzRCNGJLYjFPVGQ0OURjcmdmZExzSVlvUmFpNjdFSE1CanBlYTlCdw?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>NIO</b> (97)</summary>

- 📰 2026-11-13 [GAC-Huawei brand Aistaland adds EREV variant to GT7 amid slow sales ramp-up](https://news.google.com/rss/articles/CBMickFVX3lxTE5DQVZVVGRGZzN2eE9tNFlPSE9EaW1sMHJuS3JkekdJSXJhZm5VbDRaVWdBb0NUanQ3eTNwV1R0ak1aZjNldk5SeDNGb2JRVDhtNThza19FSFpJR2dqN1lHUVRYNC1fbWtIY05MZWtUYnBSdw?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-13 [Changan seeks to sell 10% stake in Avatr at implied valuation of $4.7 billion](https://news.google.com/rss/articles/CBMidEFVX3lxTE1uanlOMHRrZkNjeXNqSE9OcmJ4d3RUeTFCREpqU3NXa2RRWDJoV2RtUVhWOUFySFY2VkplRzYzeDRqSzNGcFlvZ1NHV2hUelh3dTVqNTF2cXdlWEtqUzZBdkQ4T2MtWlB0VW1BTjBkWlV5MVBR?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-13 [Voyah launches 2027 Zhiyin SUV with upgraded Huawei driver-assistance hardware](https://news.google.com/rss/articles/CBMicEFVX3lxTE9ybUV6ekgzeFU5YTRFR19EWF9XR0FJQlB4REl0eDFwNUNrcW1DUFdBRnR1bVdfTHMtTDFRazk5OFZlay1tcnF1WE16cDR1YzN2LXJHckwwcGRIdjhnOGxzcmdiMzZKN01DTkQxVmJweHc?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-13 [BYD opens pre-sales for third-gen Tang, expanding 5-seat electric SUV lineup](https://news.google.com/rss/articles/CBMic0FVX3lxTE5paGlsXzBRclozQXoyTkVEbkNOWVJDblYxQTBBdlZkc0xfRFFrZTY0aUs3cW0zLXJ6aVR1ZlRTX0tSMko5dWhiT0wydkk2S3hNSFRKZk5hT3NvaVpVVnFUR3FxTDNqeXJuc2RMTDUwZl9SVWM?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-13 [Li Auto's 6-seat electric flagship i9 tops 10,000 deliveries less than 2 months after launch](https://news.google.com/rss/articles/CBMic0FVX3lxTFBUX1l4YmRoaWFFendhTU5UdFV3ODZ3czFBS2ZPT1B5RG12aXZSb2tJMEhPc3RXeXNicjJRb0o1RV82Q0xkUHkzT1daa1hCcW5WWmhidnVwMEdMVkpoRjJ1VWp5bUNtelZ1alR3akhKN1VqYkk?oc=5) <sub>CnEVPost</sub>

</details>

<details><summary><b>Huawei</b> (200)</summary>

- 📰 2026-11-13 [GAC-Huawei brand Aistaland adds EREV variant to GT7 amid slow sales ramp-up](https://news.google.com/rss/articles/CBMickFVX3lxTE5DQVZVVGRGZzN2eE9tNFlPSE9EaW1sMHJuS3JkekdJSXJhZm5VbDRaVWdBb0NUanQ3eTNwV1R0ak1aZjNldk5SeDNGb2JRVDhtNThza19FSFpJR2dqN1lHUVRYNC1fbWtIY05MZWtUYnBSdw?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-13 [Voyah launches 2027 Zhiyin SUV with upgraded Huawei driver-assistance hardware](https://news.google.com/rss/articles/CBMicEFVX3lxTE9ybUV6ekgzeFU5YTRFR19EWF9XR0FJQlB4REl0eDFwNUNrcW1DUFdBRnR1bVdfTHMtTDFRazk5OFZlay1tcnF1WE16cDR1YzN2LXJHckwwcGRIdjhnOGxzcmdiMzZKN01DTkQxVmJweHc?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-13 [BAIC Xingtan 5X launched in China – Defender-like EV and PHEV with Huawei ADS 5 Pro, from RM79k](https://news.google.com/rss/articles/CBMibEFVX3lxTE1jNEVRYUxUNEVhQWdkbmtRbDhleDIwNWxORUk2QXhwblhYenFUNUYybTQ5cUppcHJacW4xYjlEc2c2ZHlWSlZDelJnZlRFcGZ2c0lwamVnSzd3UDhBaUpTdVFDeWZnY3c1WFFoWA?oc=5) <sub>Paul Tan's Automotive News</sub>
- 📰 2026-11-13 [Changan seeks to sell 10% stake in Avatr at implied valuation of $4.7 billion](https://news.google.com/rss/articles/CBMidEFVX3lxTE1uanlOMHRrZkNjeXNqSE9OcmJ4d3RUeTFCREpqU3NXa2RRWDJoV2RtUVhWOUFySFY2VkplRzYzeDRqSzNGcFlvZ1NHV2hUelh3dTVqNTF2cXdlWEtqUzZBdkQ4T2MtWlB0VW1BTjBkWlV5MVBR?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-13 [Li Auto's 6-seat electric flagship i9 tops 10,000 deliveries less than 2 months after launch](https://news.google.com/rss/articles/CBMic0FVX3lxTFBUX1l4YmRoaWFFendhTU5UdFV3ODZ3czFBS2ZPT1B5RG12aXZSb2tJMEhPc3RXeXNicjJRb0o1RV82Q0xkUHkzT1daa1hCcW5WWmhidnVwMEdMVkpoRjJ1VWp5bUNtelZ1alR3akhKN1VqYkk?oc=5) <sub>CnEVPost</sub>

</details>

<details><summary><b>Baidu Apollo</b> (33)</summary>

- 📰 2026-11-12 [百度李彦宏：今天的具身智能大约相当于2016年前后的无人驾驶](https://news.google.com/rss/articles/CBMidEFVX3lxTFBEal9NZExGTzFna2haSzdhSnVwR2VLZDA5dm81MjFmMXJhWFcwNEJXMTBxc0NzTEVFY2dvWi14d1Z6RUxkREpsNkd4N2JoSjdQMDVnMjgtbkFiRWJYejQyMUFYS3gtcGxtSXA1aUJLUVRjeU13?oc=5) <sub>金融界</sub>
- 📰 2026-11-12 [百度世界 2026：萝卜快跑把无人驾驶做成了全球出行新服务](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9lSDh4ZUdHSTdGQjNEZFpZTDFJVGVuamRNdndvQWExOVJnUXQyZ3owSTIzTU5sakF2Mk5PbGpNWlEtN3BpVEFKdVlKVnljcTJBU1FqeVEtMzFhdkk?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-12 [Baidu's daily active agents surge sixfold in a year as Robin Li says AI's next stop is the "intelligent organization"](https://news.google.com/rss/articles/CBMidkFVX3lxTE84TUxtbGFWdllMYWlLb2lvZHBXalVza09ZbS1qVlVWMTMtamp3WnVqUkpWdnRyelNLMWJ4RUFIVmlGUmduUEpwQUp6cnNYRDZJdDVBUkF5NW5nMFJiYmZfNGNvdzdubGlpUGNJUjYzV2tCR3ZrTXc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-12 [What Bears Saw Before Baidu Slid](https://news.google.com/rss/articles/CBMimAFBVV95cUxOQ0NqSEZrQ2k0TFlHQnhaMEpDQ05OSnc0TWU1MEw4cmJNVlNJVlZxa2s2SngxVlRORHFwbWtOWE9ickNSRTBRZ2tucjdqbzlUeV9Ta0NZRmxSVmFLdnVPcTVnREV3QWJ3MW5VeDB5ZjZ4YVRKNWV2SGFuSXZrcENDcWVfQkd1MHFnWXlSc2lhTGZ0SDhwc3pHctIBngFBVV95cUxQRkdOVG50UDN4Q0ZWbGhPN3o4Q3haNEpkRk40NldsaF8yZ0VHWnBiVVQ0blJBSGNLdmk5a2xiaGo4dFk2eko4VFZ2cGNfQUpFRXZDanNPUVZVWXgzZWhnT2ZBaUZHV1RTdGJEQVZyOWp3UWhDZzBSSmt4OEpSa1hsaDZaWVAyNVRQWUtPTWY0M2FNXzRob3hLZ0hsOVU2QQ?oc=5) <sub>Simply Wall St</sub>
- 📰 2026-11-12 [萝卜快跑联手神州租车在海南推出无人车租赁，关于无人自驾游你想知道的都在这里（Q&A）](https://news.google.com/rss/articles/CBMiXEFVX3lxTE1FcHRhbWk2cVdabFAyWHcteWFMQk9DSkR6aUZfMmdIWUlmU2tsNWZ1bUsxZGQ0UDY4Vndha0JITWlGajRyc2kxWnJ2MzVrdm5BZmN6c3JNS1Vpd0hM?oc=5) <sub>网通社</sub>

</details>

<details><summary><b>Pony.ai</b> (55)</summary>

- 📰 2026-11-13 [Blue‑Green Signals: The Autonomy Revolution Shaping Transportation](https://news.google.com/rss/articles/CBMikAFBVV95cUxQaDhyZW5kYjJZT1JVTF9rM3ZXeFpUUnlTdHVOVE80cTlOV2thczVobTNoa014SlJlUTJLTlNYczlPZ0R6SC10SkVYRThZRWdrYUVoU0JXR1NScEJQNWZGOVhDMVNxVWlqS1hIQkxTYzZVLS1MWTB2dlUyWUpMRXFSVjJ4N1ZRQUhtN241cFZoeGY?oc=5) <sub>Vocal</sub>
- 📰 2026-11-13 [小马智行将于11月18日盘前发布财报，一图速览分析师最新预测](https://news.google.com/rss/articles/CBMisgFBVV95cUxPYVcxVjZZbVVYNTdjclg5emVCMmlOb2VDU0t5SXZQblRNXzEwSFpIU0VLbGktTHNRaHZad2ZNdnUzcDJ4cFBsaDJwSkU3VUJ1amFub1BGa2N6SjJwUHhBanltbHVKeHJpSlZwZE1CdVdpb04wWVFGcXFfbG5uUWU1MXJzcWFOeUx6NllWU0dWLWtsOGRzT0J5ZHRGU09xUm5acUFCZml1eGFyX1RaNnVlOXhB?oc=5) <sub>Moomoo</sub>
- 📰 2026-11-12 [META_TITLE_QUOTE](https://news.google.com/rss/articles/CBMiUkFVX3lxTFA3LVZJeTBpcEZ6N09KTHJ2MUJfVHJXUmdYVDZRQVVjbEVkZ0tLeHJFNkJWbE5uUTYtaHFXeVZJeWo1cGRudVU3SlNxWm1nYWxfZGc?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-11-12 [Top 3 AI Stocks To Watch In November 2026](https://news.google.com/rss/articles/CBMisgFBVV95cUxOOENJbW5nOHlTZ016WjhjdjlrNXA3Z1ZKbHNtdGtoTUcwSjY4WVVzZTQ4WG1TY2NvQnZ5LU9mdm15eE5jTnZMbWVTT2ttaTU3cjl0LVhseldDTS1rSURENk90RU95QllteXpHNzYzZGhidGJPclgxTnVCRUI5QVl6WVBYcjdfU3hpMlZuZjNYWmhvb1NWTXBuUS1ka3kwQlZ5aElDVWk0bG94Q3Fwc3YtUFdB0gG3AUFVX3lxTE96N2xrM1RmRnY2Y0VubmN4aHNjXzFHSGh5NzlZd0h2a3NxY21UNGhObTVSbnFrWEczdGlUbjYzSjVEYVhDWkg5UUhMeGJScUlEbUF0d1ZpbUY5X0k2Zkpkd1hpU0d3M3RNeWNEQXJPcElMYllkdXRGTld6V05nYUdDYzdNVmc4WjRHMVRBaWI3M0FhV3pMRFdyRll1emU4VkhNcExFMkxJYWgxQ1VieTV5Wm5PTkdPNA?oc=5) <sub>Simply Wall St</sub>
- 📰 2026-11-12 [Dubai and Abu Dhabi want 4k driverless cars, but the rollout hinges on public trust, insurance, and nuanced regulations](https://news.google.com/rss/articles/CBMi7gFBVV95cUxPQlhaTHRGb1hTcTN2ZXlmNjYxZHl2emlkNGx5OUJSSm9KdjAwRjNTclM0V1QzSkx1X0lJcXNLRTBUOVNXeDdZWUwwN3FBMmh1d3lCeTZ4WnFwX2Y5SGdPRW1vUDBHa0ZvWjdLbV82YTU5SEU0d2hxcDN4dGlQdzk3c3MtVnIxUHdLUlYzT3BuRnIwNUJoRHVYbFVMYThIalJrY05CdnZxb0pRc2FrLUIwamEtczhIUE4wS3NhYkVsR0hjU3B1TTNuSVhBZDF1OHpON0VmWHZLNnNoS0RVUlJRdXBaeDlIa0NIT1pyMkZ3?oc=5) <sub>EnterpriseAM</sub>

</details>

<details><summary><b>WeRide</b> (78)</summary>

- 📰 2026-11-13 [Is the UAE ready for driverless cars?](https://news.google.com/rss/articles/CBMifkFVX3lxTE9vU0ZCZmgtMW9uSlhFNmZLS1BjZVloWnZKS2lVZ2labURKWGdPRXlIRXV4dDFWTkdsVHZ6NjF6N3d5QU5lT1FhZEwwX3hKcFVCQWtUTGRzUFp2eFMwZ25KdGpsNWVLXy04X1FiTE1oajB1eTRqVFRyMlhrNHNFZw?oc=5) <sub>EnterpriseAM</sub>
- 📰 2026-11-13 [八冠王智驾上车！文远知行赋能AION Ray7正式上市](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1rTTlfYktOTlVHODA3clc5MUxNVmhJTlQ0UGVzeDJxOEkwRlQ0Wlc4Y0QyZ3V2WjVPV2RLbEg0SzJpci1Uc250R25kLUNoSURuV3JpaDduQzdxOE5RSkE?oc=5) <sub>CSDN</sub>
- 📰 2026-11-13 [文远知行赋能AION i60实测两度刷新纪录，好评率超90%凭什么？](https://news.google.com/rss/articles/CBMiiAFBVV95cUxQc2t2YV9kUmx0SXI0SXZaSWRQem1mbml4YkpvUVZyTkFXZTU3LU0zUGpzZ25JV09UcXVldGk5YXFoVHZ4YmJpMTltYmxlaTNVQ0tHX0lTQXJYeGVvZ3p6YUdiNFJubTY4TGxsMVYyOWRIVmJpbF9EVEJ0TG1RTk9aQkw0X1Y1cS0y?oc=5) <sub>Sohu</sub>
- 📰 2026-11-13 [埃安Ray7限时11.47万元起 后驱702km续航](https://news.google.com/rss/articles/CBMikAFBVV95cUxOd2VxcjlQQmJWWk5LVERkLTZBdWZGcnNXSk1nLVp5UUFTbkg1MEdkV2M5S3RkUkRHcFZjdVpVdEpteXlrRmg4cU50SDB4MWhuZkpsN1R4b2ZSdzRCbEk5aF9DYmNPdmQxbEhXbGs4WDRZbGx6Q1lhYjNScFdSMDVzdzM2VEY2c2htZnd1U1R3NXE?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-13 [我们的APEC局②｜从广州到新加坡：一辆无人巴士的出海故事](https://news.google.com/rss/articles/CBMiigFBVV95cUxOSlZqbG1OZEdNQy1PYVVHend5THZKWDQxVUxZaFRWRGM1c2pxa254c2tJR1d0QlZDd2lqTnhDak5Dcm1rb20ySWw4VFd0SzRUVTlqYkU5MkRDaUp0WHRjNURVWG5uTVItcDdyZnAwR29pZ2dhcTRtWkNpcVg5cmtuSV9kT2NaQ2xNb0E?oc=5) <sub>广州日报新花城</sub>

</details>

<details><summary><b>Horizon Robotics</b> (49)</summary>

- 📰 2026-11-13 [ID.ERA 5X Starts at 99,900 Yuan, SAIC Volkswagen Finds New Competitive Position](https://news.google.com/rss/articles/CBMi4wFBVV95cUxNVjYtTHhSQzJYLWNBVjdSUy1uZF9SNENvLUlUY2txRGcxU0RmMlh6Qm91T0xZQVE5WjBXOUVIaUJ4WUxPdkJXbDlsRU54ZHd3anVuQzdnTnZzWnVCWjZxX3NNaWN5dXRDQzI2SGFnRTdBSEtjOHlnN0lnZGJfaTNtU2RHMUFIX0toRVl3bUFPbG0wcDBjUFR2VTlJSUFvZy14S19NUk5yeWplSnNlUTZNV01IUGZfMlZ0MGswaTVHZnVUdThJXzJSbFFFWDFoYlV6SHAtU0RNMmhlY0RiLUJjNzVFdw?oc=5) <sub>Gasgoo</sub>
- 📰 2026-11-13 [【视频】地平线 V2.1，路况再乱也从容](https://news.google.com/rss/articles/CBMia0FVX3lxTE00eVBMN0hDbXkwalg3TGk4dFRRdGJCUjVqeWYwZUwwSE9DNzNseTEyRU91RDFiNG8wMUdWTEZvMDliaXJTWHVxeVg4aEU5UnNEcTF1aWFqbHg4VTNqaTU1cEc3UUFCR3kxSUJr?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-13 [【视频】酷睿程HS8+地平线HSD，ID. AURA L5同级独一档](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5OZ05KS0Z2UFAxN0FvNnltQVNOaE4wYUlWdWU3LW5KWi1KaldVNFpGd2dlbHA1WUtoWmx2QUlHeXBuS0RkSGJiQVFDRDZhYUVCaThOdmkySk9mSVE?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-12 [大众ID.AURA T6深度评测：12.99万起的中型纯电SUV，家用能闭眼选吗？+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE1zUnNCUVp0Q1ZoZ3VUUXQ2dklTTGVRZjRGQlRoS21OQ0xTa3ZCMlRjMUlfUFUtNkZGTWVLVlRPMHNNaTRpSE44T1owaE5mVmUxdlNaQ2JldUVSWmlWaEdmLXVjR085VVoxdGcwLWJxdFhQUQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-12 [【视频】iCAR V27 全能家用硬派SUV，颜值实力双双在线](https://news.google.com/rss/articles/CBMiW0FVX3lxTE4zZ0t6NjlGdk5kcU44Q2laN2NsTWZ6c1g1RTZFMVBjUXFTQnUwTWlIaDdlZW41SFdyczN1VHRtMnM3SlVySkpYLXk3VmFubjRVUXE5dUNTUEQ2RFU?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (19)</summary>

- 📰 2026-11-13 [【视频】小米澎程N90和特斯拉Model Y L怎么选，同价位还有哪些推荐？](https://news.google.com/rss/articles/CBMiW0FVX3lxTFB6dElibXRFYWFsZU9vQnhjX3YwZjF2VVd6QjhLdXJIV3pmRGhzTmpuTFRER2xXV1Zjc2ZqNld2RVY1MkxrTENqczVRc2MwNHl1VFljSkt2TjRxZ0U?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-11 [【视频】特斯拉发函，媒体CEO：放马过来#特斯拉#埃安Ray7](https://news.google.com/rss/articles/CBMia0FVX3lxTE5xOHhzcEd1V1RKWmxPZ3BEYUN6NGRhOXB2cHFXSWxFNGEzdjFPbkotY0VMQlpGTGxyV0FCc3p3S1NkU1NjSjI3b01nN2FTcnl3blB4dC00UGlQNlk0Ukp4SEhIYUtSVXNhRlQ4?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-11 [【视频】26年特斯拉YL](https://news.google.com/rss/articles/CBMiW0FVX3lxTE15a0hBYUc1enJBUDFBTkRRNlQtdGs4OFU0NjR0WXNFYnhHX09YZGd0WTRkREJVZlVwSTBNaGVUY0ZUSmU5WEFWQlVnZ1o1dUpCNENiYVptdHZYa3M?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-10 [官方预告已发！smart #2 BRABUS，比你想象的来得更快](https://news.google.com/rss/articles/CBMiXkFVX3lxTE5Nd2ZtYXF4b3pfdGJ6dEdBTVcxcS1zeUIyNzA3bzNTRFI0bmgydlJJYWplR2ZNYXFDQTlsLUpDS1BLdmJ4bThYdU1RNjM5VUR2NnlvNEJMcHBScVBzekE?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-10 [【视频】Model Y L 六座家用｜一副好脚垫能省多少事？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE92blRNM1I5N0tnc3BHSmRid3RwcFIwNnMtYWJwTkcxZ1Z4RDVjTVRzS3hvUm5BMGptOGNSelRBdWM4cW9ZZWtNMHN1Nm9lUkNtdnB1aUtiVkVyREE?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Mobileye</b> (9)</summary>

- 📰 2026-11-12 [JPMorgan Downgrades Self-Driving Technology Supplier as Volkswagen Faces Delays](https://news.google.com/rss/articles/CBMi1gFBVV95cUxNRXhmZ1ZxandRVnNmaEhwZmljMjNVemVoUEIzVFZPQWlGQ0lxeTNES2JuczR4dnZiU3hpUWlydklMWXVLeW5tWVBFSVVlY2hfXzM5dm4yWEZ4UmJYcTdJU2o2MWZhS1VMWkhwb281SndVb1BkN25QTUV3TURlUmxVTzdYTUFDVFVVTkdKRk1wVlpzMmZ0QjZqWUw5ZDU4dnV0bXhzZEtJYll5SkFlZFBxWFU2aGFvYVZLWHQ1d3RfZDdrdVFzQkVUd09lUjlqYjVTWlNSZDhB?oc=5) <sub>TradingView</sub>
- 📰 2026-11-11 [Mobileye Announces Participation in Upcoming Fourth Quarter 2026 Investor Conferences](https://news.google.com/rss/articles/CBMiwgFBVV95cUxOR29NaGt3LXBWY1o0YTZEZXBTaGhySjAycERjTVRxcEw1RjhXT21tb2hxbGk1ODkwWFZlbnBkdTE3ems3dW0tbWlUaUpUNUs3T0VJeXlBUF9wUGtLeEtVRGNnQmVsUWQzZEJxeHl4OGdiRjFpbGFkV3JEM3Vwb1NRVDZGc3EyZUpIQXpyV1NBckR2MG9sZGRvZWJRZk9ycDdrYWY4ZmtIS2pSUmpuZFFvX2V4VUVJXzZaS0xrQkNCVV9JQQ?oc=5) <sub>Quantisnow</sub>
- 📰 2026-11-09 [Nvidia Scandal Sparks Auto Industry Watch](https://news.google.com/rss/articles/CBMidEFVX3lxTFBUSkZrRUk0TktpdFF1dEthaHQzMFdVRXQySHRMMXFwT2s2akhzT183RFlib2NuZG9lNkVoUElrOWFmbEx2OUNUY2ZhYlROQWRyZjN1eDFXdk9ObmFYQkdOUzNNM1FCazUwVWJRbWZILThIM1RO?oc=5) <sub>Businesskorea</sub>
- 📰 2026-11-09 [Maxwell AI Cuts Code Costs 67%, Runs 38x Faster [2026]](https://news.google.com/rss/articles/CBMieEFVX3lxTFBlMjEtN1BpMTdFQ1JKOTBKQjBvaFV3V0dISVg4SGtlQS1YczlwRFJsRHFEWTl4eHRiak1wYmVnS1lEMkhGaUpmNks3eUU5ckExSl9DekNyLTNhSHRNcllrSXNSbHFzMFdDUHZPVkljalNlZTV6c0R0UA?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-07 [Mobileye Global (MBLY) Lifts Guidance Following Earnings As Fair Value Debate Returns](https://news.google.com/rss/articles/CBMi0wFBVV95cUxNOF9fMHVEMXdjcUJ1ci1PZ3hqNnV3SHVHanAwSHc4TzJvTnVPSnlxYzRaekFoLUtETWdTeVFVNzNFY2U4SnNxczlUVjF2bEE4WEFPcXdDRjZQWnhKU0J0ekFGS0l2cnlLVmZTN0o4MjFSMUgwOTJ1UkEwQXREdnZXbTM3VmNpNm42YndkTHBGT2prNENPZ1JHTURJRy11a19YRjQyc1B2V0Y4aXBVamRXeFpzamRYWWpWX1c4eXpWYmdiWVIwUVRYck1OUXZjTElGaFM40gHYAUFVX3lxTE5nb2VZYnRkMGY3a1l5UTJTU1ZJUndzc1VjWHpicnNpRm1pdURTMUwzYWJYeVdYRy1kNVh3UjNub19fWm11eTVLSGVUVEJFTlBDcHExWFhBWFdPZDdsY05FRS1kUEtoRi1RVFROcjIzalJmdVA2amlrOG5OSmtlMUJtMlo0S21IUGpaRXE5b1JvV0xCaEo0OGZPaW9UeWQ0bEZ0d0VQU1Y2b2QzQnh2YzVaSTIzVV9pTUJOUy1BM1puZ2N0SUc0SzltUnotUU4ySDlfR2psMm0tSA?oc=5) <sub>Simply Wall St</sub>

</details>

<details><summary><b>Aurora</b> (24)</summary>

- 📰 2026-11-13 [Archer Aviation And 2 Top Penny Stocks To Watch](https://news.google.com/rss/articles/CBMiwgFBVV95cUxNckZLN21fSnBMejAtZFNiTk9sbzlWM1drb2R0Qi1YcHdFbGZGSnlaLURxQUFqcUlIWkM4MGtMOE5tWXVob0FYczBvUks4aTJrc0lrMmlzLUNpV2FMT0p2eWI2alVBSEF5bnlqUGVaSklMYWFiTGVtaE15c0Z3Rm1yQ0ROWlZmeWhsSENHY2FjSnkwRTlKQ2JEY2RpVUJXd29fWFhUOEVicVpweFBiUlI2MG5rM083TTZQUlExbFpnSDdlZw?oc=5) <sub>Simply Wall St</sub>
- 📰 2026-11-12 [Autonomous Trucks Could Be Cheaper Than Human Drivers in U.S. by 2028](https://news.google.com/rss/articles/CBMi5AFBVV95cUxNZ09XbjNWYmswcURfNFRaN2poUF90MXRtN0lRSmlZclptYk5vQUptQ19Denh4ZlhyblRFNk9Vb3Vra085cmdnSWZyZE5KSVFMa3JhczgtdFZFTVVjVVphSWo0OGNiN3E2Q3VzN1lYaFM0TXhfVVA4R3RhaER1TmtBRkVuZWItQ2VPVDlWd3dfOFdPUC1VZ2V5dVJ2bl9qNTFwTjc4V2YtUGJQdGQ0Y3ZMZWc0Y0otdUlRa1BSOHlJUVNYWm93NWk4bTNRRG1aVmxpRDlmZTF6dDV3Qk1DM3JacFA2NFA?oc=5) <sub>SupplyChainBrain</sub>
- 📰 2026-11-12 [Notice of AUR Investigation Reminder: Kessler Topaz Meltzer & Check, LLP Encourages Aurora Innovation, Inc. (AUR) Investors to Contact the Firm](https://news.google.com/rss/articles/CBMinAJBVV95cUxQdzhkSk9OWkM3cTJ1QnZ4TDdSdERuc21sUHVYRDNkZUwtc0d5TEs3XzJqbXZ0aTRab2RTcUs4QUVSbnFMcFEwSTBKV1czSjN4cldUOXI1ek9qbkxPbHRvdHNfSEV6WTRFTE9hNWMyWDNuV3JuNzFWbWxwc3RjWF9DaG1UX3d4YnVNTm9rSGxoZjZkTkNST0xTdWpTajRkQ2pXM093RnBvWFVvNXhnREFJUUkwc3VfeWZoUklSZ2dkeHR3ZHY5OTJCTjFLZk9jS05sMFBYcDd5WVFZUENoSHcxZW54dGNaX2thTUszdHpTcmVyTTNPWnY3QkZZcUlBRTRVQlJpRFZsOWFIVE94VWk3bmUyVHRSXzdnUk5uaQ?oc=5) <sub>PR Newswire</sub>
- 📰 2026-11-12 [Nissan Reports Tough Market Conditions in China](https://news.google.com/rss/articles/CBMiuwFBVV95cUxNcDlMelRHWkY2aG9SWld0WlVaeU12TUxVVXgzN1BGWVliclZjd1R0akQ0ekEwVW5RMmRrX2hkcUdCZkFtUk1LT2dSNHBmdlJzLWdxeVNJTmJndmRnc3JVME9kZkVVUUdNaDE0bzBrVzM0U1lPY3U2Q1pENmV1T0oxWVc3WXFhMXF2VmtKclBSemgtaE5vd0hqSVpVQ095dWZleWNVcGVtb1JtTUJhUUw2c0RJMTJZcm1UUFRn?oc=5) <sub>SupplyChainBrain</sub>
- 📰 2026-11-11 [DTL Transport commits to running 75 driverless trucks with Kodiak](https://news.google.com/rss/articles/CBMiqwFBVV95cUxOdXV3RjNmZHdIVG9jR2xlbXR6WG9qOTFkN2NqVHhROTVoRVhsdGR3ODk1aVlNbTFRRDBYTV93OHRGTGZHcUFDRk1zcHY1VUtYa3lhQ05rTW13VjFXUm1DeE93QUJOcFBkVVBKSEFKYUtTWTZkU0pjQkpXWEE2ZUhySUlLbmRCNHo4VlBPVTVobXhNRUtCcjZuQ1NGWmlPZUxaelZMclNhQnVDUFE?oc=5) <sub>Trucking Dive</sub>

</details>

<details><summary><b>Zoox</b> (40)</summary>

- 📰 2026-11-13 [Zoox expands Las Vegas service, rolls out next-gen robotaxi](https://news.google.com/rss/articles/CBMikwFBVV95cUxNeC1CcmxNUFdoeFU5TVBkNE9Za2U0d09pR0hQR0dDNnFjLU5feGhCa2FQN05tdTZ0NUFBVXhjS0p3bnlnWjdfZVB4aFdlVkw3MktUQU9NNWhJN3RUcXZzaUlaWndVWDFaT2phelkzZ0Qya1VpejgyUTk2TU5uTWJoYm8tVDNEWG9QRFRSTVN2RlRzaHc?oc=5) <sub>KSNV</sub>
- 📰 2026-11-12 [Zoox Expands Las Vegas Robotaxi Zone, Adds Redesigned Vehicle and Hours](https://news.google.com/rss/articles/CBMiqAFBVV95cUxPbU5CX3diN2ZDLTBmVUllOEEwYUR2eDZWQWN1Y3pZN3FxQkVOWmRkcEVmbVB2c25ibC1fLXJObERCTk9KWkhuMWR6VTF2VHlCVnFtWXZzQ0ZGVURqb3dyVGhFX2RpSGJocGF6bmZ4MHRtVXdYYmJ1Y0IxMnk4VHgyYzZpa1NsbV9PZzVMT01JUUNJa2liWnBtQ0p1VGV3QmJOZDMzNU1keGg?oc=5) <sub>Electric Vehicles</sub>
- 📰 2026-11-12 [Zoox expands Las Vegas robotaxi service beyond the Strip](https://news.google.com/rss/articles/CBMinAFBVV95cUxPNTJ5LXhlcV9wY1VXOGUxM3NCU1QtRDc5d2pnWUlKVmhJc1RZUnVmR3JKWXFjVFIxOE1HM1pDSWx6Yi1MREJQRmRpYlNrNzhHd29YLWFUSFd2eTAyYkpXYW5xUHMtaEVKdzg1SG5LdGRrbXZ4b2ZwWFNidTVRNk81Y2tHVFluWUUtekdBQUpSSnpNTF93czlpUjFiN0w?oc=5) <sub>FOX5 Vegas</sub>
- 📰 2026-11-12 [Zoox robotaxis expand into downtown Las Vegas and the Arts District](https://news.google.com/rss/articles/CBMimAFBVV95cUxNb1BJbFJFZVlNZGJnR1pkM2xtbGxqdlNsd0dUbmhwZzFvWVNFQ1RWV05NZFFyU1laU1haM2o2b3RESEJ3a2M4ckFzTThqbDE0OFA3TGpfM2o1bmNnTzVxbmFEWndCQkVNbHdpQ2d1enFVUnFiei1jZVhwdDFDN0xiNGhsbFdEeE9TSHVZUEtObDBUNFRGRmdqdQ?oc=5) <sub>KTNV Las Vegas</sub>
- 📰 2026-11-12 [Zoox offering updated Las Vegas service area, vehicles and operating hours](https://news.google.com/rss/articles/CBMixAFBVV95cUxPd1Q3RnprcE1rY08tOW4yTUY1d2tPZGZTaFFCbFhYLVBGYmVRSHZOWjBsN2lhWUVIWGtUZmh3aDBiY3p1eFJ5X1lhSnYtTW5vdWtwVlItTkZtQ3hTMVVIT1BIOWV3UW1vazVkZzVLRWhIMXZ4RWxfX2F4bmNJS1ZReVpJVW16NWZpdkJESzZLMm9NVG92MG1seS05RmRPRUN3SDhpRDNVNWZZUHNBVnlJaG45VUN2Y21jMk02X0dhSXY0QzdP?oc=5) <sub>Las Vegas Review-Journal</sub>

</details>

<details><summary><b>Motional</b> (15)</summary>

- 📰 2026-11-13 [Huang’s Exit Puts Hyundai Motor Group’s Dual-Track Autonomous Driving Strategy to the Test](https://news.google.com/rss/articles/CBMidEFVX3lxTFBZTG1rU1ozSDFnd1diLWNmZVBXcFRjZ0J1UGpqZ1BCck83SFhJOUhBcDE3ZlZKV0tod29JZzh4dVctU0pYR2h5bWxSTVg3ci1XTUFMeVh6WmQ3SkpncVBadDZMX2p4VWlzSG1MQVh5NFZhWGVN?oc=5) <sub>Businesskorea</sub>
- 📰 2026-11-13 ["Cars That Keep Going Even When Sensors Fail"... Hyundai Motor Boosts Autonomous Driving Reliability](https://news.google.com/rss/articles/CBMiZEFVX3lxTE9BX3gtSThrelhocW04V2VGTXc5NnB0X1F6VFBlenZLX2Mzc01UY3o1c2E2eE8tQzdqbktEOVIyTzBtdnFOeXF5NlEzS3lIXzNLMEVzQ1V4dTQ1M3ZXY1FQR21pank?oc=5) <sub>아시아경제</sub>
- 📰 2026-11-13 [Hyundai Motor: "Safety Over Speed"... Ensuring Cars Keep Moving Even If Sensors Fail](https://news.google.com/rss/articles/CBMidEFVX3lxTE5Vc1NOV0ZacmFwUjhSNVhhSTc3VFQ4QV9DanB6aGNSWFhONW1CcEpyZ1NaNm9heUk2ZGhLRm9XaE5NcXVJZUtjUmJIeDQ2TUFEczBVem0tbGYtRkp6eVlhTjVHdmtVUno3NmRpZldWalhZbUYz?oc=5) <sub>아시아경제</sub>
- 📰 2026-11-11 [Korean firms shift CES focus to industrial AI](https://news.google.com/rss/articles/CBMiqgFBVV95cUxQQVpGVm5oN2E0dXpVQ2tfaXVaZXlZanNWcllzRTJCc19OS0F3V2Z1eWEteEpub2dQWWJleEtYMTVyVkRGaVpmWmwwQi12V0JhdjlvRENjU3JWMlpLTkJkOHhMYl9JeDh0RU14Mm5fZmx0X1Z4NlJTYmtKNkc2ck4wT3pQTUZxYjFmQ2M5a1ZoTC1WSmZOOGxMOGJFakVoTm4tcTNaekZZdVFWZ9IBqgFBVV95cUxQQVpGVm5oN2E0dXpVQ2tfaXVaZXlZanNWcllzRTJCc19OS0F3V2Z1eWEteEpub2dQWWJleEtYMTVyVkRGaVpmWmwwQi12V0JhdjlvRENjU3JWMlpLTkJkOHhMYl9JeDh0RU14Mm5fZmx0X1Z4NlJTYmtKNkc2ck4wT3pQTUZxYjFmQ2M5a1ZoTC1WSmZOOGxMOGJFakVoTm4tcTNaekZZdVFWZw?oc=5) <sub>The Korea Times</sub>
- 📰 2026-11-10 [Tesla Fort Worth Robotaxi Field Report｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1aT2xVRzVDa1RNSDEwb0FuOTRwU1lPenVGSmhER1ZoRmJJdTZpeGlaNEt6OEN1SWxKYlBUS2N0aXprRnBPQ3NxVjB5VG9maVNGWHVWU2VwbW45UWpJS0xB?oc=5) <sub>finance.biggo.com</sub>

</details>

<details><summary><b>comma.ai</b> (2)</summary>

- 📰 2026-11-12 [Goodbye, BlueCruise! We Install a comma four in Our F-150 Lightning](https://news.google.com/rss/articles/CBMirwFBVV95cUxPY1o5ekZ4WnpraUxVMHV6OVdyMEtEbjQxQXY5STdJdXlHNlN6eUFZNzFwSnA5cFhHd3pNdTZNNy03dXBOZ1ZoX3RFX2E5V2JNTE9aVlhJaG90bW5YWEdzX2NGXzd3VFZ6NG5JVkFrM3daTmY4UDBTN1I4NWU3eGJqUm9tY1VaRWxoZkp3WDJLNnVLQjN5WG9NMzlxLWI0aVU2TFhLUEZwUE5YUDdUcWFJ?oc=5) <sub>Transport Evolved</sub>
- 📰 2026-11-06 [Canadian YouTuber Linus Tech Tips Tests Tesla FSD](https://news.google.com/rss/articles/CBMiggFBVV95cUxNZVZaT1Q4X0NlakJzTnFkTGdqTmFPM3pDbFZPUnBYVVNrVzFxMlpZQ3VaTEJFUmJrNVpjMmZ5RVphUDE4WURNT0x4NkhnN01LdTdzSEVnS2NUNkROams2cnNzNkpnalhWcDVuckhETUtxaDZrSHNXTXhKYUlpN2dPTlZn?oc=5) <sub>Drive Tesla Canada</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
