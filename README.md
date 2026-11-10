# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-11-10 · 1,292 papers tracked · 46 curated.

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
- [Perception: BEV, Occupancy, 3D Detection, Mapping](#perception-bev-occupancy-3d-detection-mapping) (7)
- [Motion Prediction & Behavior Modeling](#motion-prediction--behavior-modeling) (2)
- [Datasets & Benchmarks](#datasets--benchmarks) (1)
- [Safety, Robustness & Evaluation](#safety-robustness--evaluation) (3)
- [Industry Tracker](#-industry-tracker)

## VLA / VLM for Driving

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Teaching Vision-Language-Action Models What to See and Where to Look](https://arxiv.org/abs/2607.01658)<br><sub>Yuguang Yang, Canyu Chen, Zhewen Tan et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 38](https://github.com/ShivaTeam/DriveTeach-VLA) | Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving |
| [SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving](https://arxiv.org/abs/2610.20609)<br><sub>Shaoyuan Xie, Zihan Zhang, Jingxuan Wang et al.</sub> | CoRL 2026<br>2026-10 | [⭐ 35](https://github.com/ASGuard-UCI/safedrive-vla) | Vision-Language-Action (VLA) models are gaining attention in autonomous driving, inheriting commonsense priors from large language models (LLMs) and widening the navigation interface from a fixed command set to free-form… |
| [Scene-Adaptive VLA: Efficient Autonomous Driving via Dynamic Layer Routing](https://arxiv.org/abs/2610.24590)<br><sub>Yujia Yang, Quan Yuan, Jiawei Fan et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 4](https://github.com/yang-luvu/Scene-Adaptive-VLA) | Vision-Language-Action (VLA) models offer a promising paradigm for autonomous driving |
| [Locating and Repairing Domain Shift in VLM Trajectory Planning](https://arxiv.org/abs/2611.10720)<br><sub>Zhihong Cui, Hengyu Liu, Michael Alexander Riegler et al.</sub> | NeurIPS 2026<br>2026-11 | [⭐ 0](https://github.com/ZhihongCui/MoLaRx) | Vision-Language Models (VLMs) are increasingly adopted as end-to-end driving planners, yet they suffer from cross-city domain shift |
| [AutoVLA-D: Learn a Trajectory-Geometric Condition from Reasoning for Autonomous Driving VLA](https://arxiv.org/abs/2611.12382)<br><sub>Yuguang Yang, Zhewen Tan, Canyu Chen et al.</sub> | NeurIPS 2026<br>2026-11 | [⭐ 3](https://github.com/ShivaTeam/AutoVLA-D) | Autoregressive VLA planning usually predicts continuous trajectories as the final output, but driving instructions often describe actions rather than ego states, which weakens direct conditioning on the final continuous … |
| [CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving](https://arxiv.org/abs/2607.04179)<br><sub>Zhaohong Liu, Hao Ye, Xianlin Zhang et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 1](https://github.com/MICLAB-BUPT/CritiqueDriveVLM) | End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving |
| [PixelPilot: Scalable Vision-Language-Action Models for End-to-End Autonomous Driving](https://arxiv.org/abs/2607.04637)<br><sub>Pin Tang, Guoqing Wang, Xiangxuan Ren et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 1](https://github.com/VISION-SJTU/PixelPilot) | Vision-Language-Action Models (VLAs), which leverage the advanced reasoning capabilities of Vision-Language Models (VLMs), show promising generalization in complex autonomous driving scenarios |
| [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)<br><sub>Nan Yang, Zhanwen Liu, Linfeng Zhang et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 11](https://github.com/Zizzzzzzz/MVPruner) | Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings |
| [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)<br><sub>Yuan Gao, Wenting Miao, Mattia Piccinini et al.</sub> | IROS<br>2026-07<br>📑 1 | [⭐ 31](https://github.com/TUM-AVS/Chat2scenic) | Validating autonomous driving systems requires diverse, regulation-compliant test scenarios |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 18 | [⭐ 548](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
| [GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives](https://arxiv.org/abs/2609.39601)<br><sub>Qize Yu, Lianrui Fan, Boyu Chen et al.</sub> | arXiv<br>2026-09<br>📑 3 | [⭐ 419](https://github.com/groundingpi/GroundingPI) | Precise grounding matters |
| [GRAVA: Grounded Reasoning-to-Action Representation and Learning for Autonomous Driving](https://arxiv.org/abs/2609.15169)<br><sub>Xiao Liu, Haoyu Li, Jianghao Leng et al.</sub> | arXiv<br>2026-09 | [⭐ 487](https://github.com/AhernResearch/grava) | Driving vision-language-action (VLA) models increasingly reason before acting, but their intermediate reasoning is often weakly grounded in physical scene evidence and loosely connected to executable behavior |
| [Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air](https://arxiv.org/abs/2605.31066)<br><sub>Tianle Zeng, Yanci Wen, Xueang Yu et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 1,132](https://github.com/louiszengCN/CarlaAir) | Recent aerial vision-language-action (VLA) models show promising single-UAV capabilities, such as tracking moving objects and navigating to language-specified landmarks |

## World Models & Generative Simulation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [FrozenDrive: Zero-Shot Text-Guided Driving Scene Generation and Data Augmentation with Parameter-Free Frozen Diffusion Model](https://arxiv.org/abs/2606.20110)<br><sub>Yuhwan Jeong, Hyeonseong Kim, Daehyun We et al.</sub> | ECCV 2026<br>2026-06<br>📑 1 | [⭐ 10](https://github.com/daehyunwe/FrozenDrive) | Synthetic data for autonomous driving is surging, powered by diffusion models that promise scalable scene generation |
| [MESSENGER: Memory-Enhanced Sequential Scene Flow Estimation via Autoregressive Next-Frame Forecasting](https://arxiv.org/abs/2610.10759)<br><sub>Jiuming Liu, Jianing Li, Mengmeng Liu et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 0](https://github.com/liujiuming123/Messenger) | Scene flow can capture low-level 3D motion displacements in dynamic scenarios |
| [ASTAD: Asymmetric Style Transfer for Synthetic-to-Real Adaptation in Autonomous Driving](https://arxiv.org/abs/2606.29286)<br><sub>Dingyi Yao, Xinqi Zhang, Lihui Peng et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 2](https://github.com/Dingyi-Yao/ASTAD) | Synthetic data mitigates the data scarcity problem in autonomous driving perception |
| [Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends](https://arxiv.org/abs/2606.01164)<br><sub>Jiuming Liu, Chaojun Ni, Mengmeng Liu et al.</sub> | arXiv<br>2026-06<br>📑 9 | [⭐ 250](https://github.com/liujiuming123/Awesome-Interactive-World-Model) | With rapid development of large language models and diffusion-based content generation, world modeling has attracted increasing research attention, benefiting various downstream domains such as game engines, embodied AI,… |

## End-to-End Driving & Planning

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [MOJITO: Modal Joint Learning for Unified End-to-End Autonomous Driving](https://arxiv.org/abs/2607.23511)<br><sub>Zhijing Cheng, Xuancheng Zhang, Donglin Di et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 32](https://github.com/mumucc01/MOJITO) | End-to-end autonomous driving systems commonly follow a cascaded two-stage pipeline where a perception stage compresses multi-modal sensor inputs into a compact context and a downstream planner predicts trajectories cond… |
| [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](https://arxiv.org/abs/2609.26792)<br><sub>Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.</sub> | CoRL 2026<br>2026-09<br>📑 1 | [⭐ 14](https://github.com/VAIL-UCLA/DreamStream) | Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions |
| [DriveMLP: When Training Strategy Outperforms Model Complexity in Autonomous Driving](https://arxiv.org/abs/2610.29676)<br><sub>Alessandro Canevaro, Julian Schmidt, Hang Yu et al.</sub> | CoRL<br>2026-10 | [⭐ 6](https://github.com/alessandro-canevaro/DriveMLP) | Learning motion planning policies that remain reliable under closed-loop execution is a central challenge in Autonomous Driving (AD) |
| [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)<br><sub>Shen Zheng, Anurag Ghosh, Gaurav Parmar et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 32](https://github.com/ShenZheng2000/WarpI2I) | Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs) |
| [G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance](https://arxiv.org/abs/2606.26017)<br><sub>Hang Yu, Ye Jin, Alessandro Canevaro et al.</sub> | IROS 2026<br>2026-06<br>📑 6 | [⭐ 7](https://github.com/HangYuu/G2DP) | In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors |
| [SimWAM: A Simple World Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.07468)<br><sub>Zongchuang Zhao, Xin Zhou, Tianyang Xu et al.</sub> | arXiv<br>2026-08<br>📑 14 | [⭐ 207](https://github.com/H-EmbodVis/SimWAM) | In autonomous driving, World-Action Models (WAMs) have improved end-to-end planning by transferring video dynamics priors to action prediction, but many still couple planning with future-video generation at inference, in… |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 19 | [⭐ 361](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
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
| [Deformable Gaussian Occupancy: Decoupling Rigid and Nonrigid Motion with Factorized Distillation](https://arxiv.org/abs/2605.28587)<br><sub>Yang Gao, Wuyang Li, Po-Chien Luan et al.</sub> | CVPR 2026<br>2026-05<br>📑 2 | [⭐ 22](https://github.com/vita-epfl/DeGO) | Understanding dynamic 3D environments is essential for safe autonomous driving, particularly when reasoning about human-centric, nonrigid agents |
| [Horizon3D: Sparse Radar-Camera Fusion for Long-Range 3D Perception in Autonomous Driving](https://arxiv.org/abs/2606.31096)<br><sub>Geonho Bang, Geunju Baek, Dongyoung Lee et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 26](https://github.com/geonhobang/Horizon3D) | Long-range 3D object detection is critical for safe autonomous driving at highway speeds, yet existing radar-camera fusion methods remain limited at extended ranges |
| [Explainability-Aware Frustum Attack: Exposing Structural Vulnerabilities in LiDAR-Based 3D Object Detectors](https://arxiv.org/abs/2606.29963)<br><sub>Chengzeng You, Binbin Xu, Soteris Demetriou</sub> | ECCV<br>2026-06 | [⭐ 2](https://github.com/SecMindLab/Saliency_LiDAR) | The structural vulnerabilities of point cloud-based 3D object detectors remain poorly understood |
| [PointLAM: Local Attentive Mamba for Efficient Point-based 3D Object Detection](https://arxiv.org/abs/2609.21780)<br><sub>Xuanming Shang, Weijia Zhang, Chao Ma</sub> | ECCV 2026<br>2026-09 | [⭐ 5](https://github.com/PointLAM/PointLAM) | 3D object detection from LiDAR point clouds faces a fundamental dilemma: voxel-based methods achieve efficiency at the cost of geometric quantization, while point-based methods preserve fidelity but suffer from prohibiti… |
| [PriorMaskMap: Robust Online Vectorized Map Construction with Biased Priors](https://arxiv.org/abs/2610.39283)<br><sub>Haoming Xu, Wei Li, Yu Hu</sub> | ECCV 2026<br>2026-10 | [⭐ 1](https://github.com/healenrens/PriorMaskMap) | Online vectorized map construction provides autonomous vehicles with essential, real-time semantic and geometric scene understanding |
| [Vernata: Self-Supervised Learning of LiDAR Point Representations](https://arxiv.org/abs/2608.06919)<br><sub>Oliver Lemke, Alexander Liniger, Abel Gawel et al.</sub> | IROS 2026<br>2026-08 | [⭐ 22](https://github.com/rai-opensource/vernata) | LiDAR serves as a primary sensing modality for robots operating in outdoor environments |
| [Towards Compact Autonomous Driving Perception with Balanced Learning and Multi-sensor Fusion](https://arxiv.org/abs/2606.02979)<br><sub>Oskar Natan, Jun Miura</sub> | arXiv<br>2026-06<br>📑 47 | [⭐ 9](https://github.com/oskarnatan/compact-perception) | We present a novel compact deep multi-task learning model to handle various autonomous driving perception tasks in one forward pass |

## Motion Prediction & Behavior Modeling

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [MolmoMotion: Forecasting Point Trajectories in 3D with Language Instruction](https://arxiv.org/abs/2606.18558)<br><sub>Jianing Zhang, Chenhao Zheng, Yajun Yang et al.</sub> | arXiv<br>2026-06<br>📑 16 | [⭐ 153](https://github.com/allenai/molmo-motion) | Motion forecasting is central to visual intelligence: agents must anticipate how objects will move in order to plan actions, reason about physical interactions, and synthesize realistic futures |
| [Flow-ERD: Agent-type Aware Flow Matching With Entropy-Regularized Distillation for Diverse Traffic Simulation](https://arxiv.org/abs/2607.06957)<br><sub>Seulbin Hwang, Kiyoung Om, Dae Jung Kim et al.</sub> | RA-L<br>2026-07 | [⭐ 0](https://github.com/seulbinHwang/flow-erd-project-page) | Realistic and diverse traffic simulation is essential to autonomous driving development |

## Datasets & Benchmarks

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [The Road Ahead in Autonomous Driving: The KITScenes Multimodal Dataset](https://arxiv.org/abs/2606.02956)<br><sub>Richard Schwarzkopf, Fabian Immel, Alexander Blumberg et al.</sub> | NeurIPS 2026<br>2026-06<br>📑 2 | [⭐ 29](https://github.com/KIT-MRT/kitscenes) | Existing autonomous driving datasets have enabled major progress, but fall short in sensor fidelity, map completeness, or geographic diversity |

## Safety, Robustness & Evaluation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [CCFM: Collision-Constrained Flow Matching for Safety-Critical Scenario Generation](https://arxiv.org/abs/2607.04451)<br><sub>Ke Li, Kaidi Liang, Yuxin Ding et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 3](https://github.com/KELISBU/CCFM) | Evaluation of autonomous vehicle (AV) planners in safety-critical closed-loop simulation is essential for real-world deployment |
| [Lipschitz Optimization for Formal Verification of Homographies](https://arxiv.org/abs/2605.23203)<br><sub>Jean-Guillaume Durand, Panagiotis Kouvaros, Maxime Gariel et al.</sub> | CVPR 2026<br>2026-05 | [⭐ 3](https://github.com/jeangud/homography-verification) | The adoption of vision neural networks in regulated industries requires formal robustness guarantees, especially in safety-critical domains such as healthcare, autonomous vehicles, and aerospace |
| [CADET: A Modular Platform for Evaluating Distributed Cooperative Autonomy in Connected Autonomous Vehicles](https://arxiv.org/abs/2606.04072)<br><sub>Pragya Sharma, Brian Wang, Mani Srivastava</sub> | ICRA 2026<br>2026-06<br>📑 1 | [⭐ 0](https://github.com/nesl/cadet) | Deep learning models are increasingly central to autonomous vehicle (AV) pipelines, yet their integration has traditionally followed a monolithic design where perception, planning, and control execute on a single onboard… |

## 🏢 Industry Tracker

Latest 14 days of news, official blog posts and new open-source repos from tracked companies. Full daily feed in [`daily/`](daily/).

<details><summary><b>Waymo</b> (145)</summary>

- 📝 2026-11-05 [How the Waymo Driver Manages Severe Winter Weather](https://waymo.com/blog/2026/11/winter-weather-preparedness) <sub>official blog</sub>
- 📝 2026-11-05 [Rethinking What Freedom of Movement Feels Like for Women](https://waymo.com/blog/2026/11/because-women) <sub>official blog</sub>
- 📰 2026-11-10 [Breakingviews - COMMENTARY: Robotaxi wars will end in Uber-Waymo union](https://news.google.com/rss/articles/CBMiogFBVV95cUxOUml0MXFsTGhBZ1hKVWtqRkZjZTRwbzZsYVBvSWVxVm4tV0hqVkxsUEtiTVI4QkxJcFh6THMwNGJmUTF6ZlVzWlNOeUdSV205ZC1nU1d3MUNTOVlPZEhBQ04zeEw0TF9rcU9xNlVtc0loaUZ2a2FiVGdaNXhQRW4xTXRWa1IzOGx2N3lKY0xqRWhhQ0VLbmVNOTk3M3dtN1gtN3c?oc=5) <sub>Reuters</sub>
- 📰 2026-11-10 [U.S. Investigates Waymo over school bus safety concerns](https://news.google.com/rss/articles/CBMihAFBVV95cUxNUDNER1ZLbmZDTWE5ekFsakFweWJJb3hmRnhqZWZLU0xKckZ4TVVEVzQ1amMtV2V0NDNJci1lb2U3RlozN1NzSEIzZ2lIeEtHWFA0ZGZocFU2QWFubGV1V3JkYkkxUHI1cWJEalByNWp4VjI5WDNTYTg2VzUxS2NZY2JxdkE?oc=5) <sub>The San Joaquin Valley Sun</sub>
- 📰 2026-11-10 [NHTSA questions whether Waymo's school bus fix worked on 2,895 robotaxis](https://news.google.com/rss/articles/CBMinwFBVV95cUxQamRxb3ZEeFR5YXJPY3dfWWNuQ0lfNllYeEhpV3lzX01CY2VFd25ZX0NKSHljbWFSYXFuUk1kcFZWYWRVbC1Nam5vMmNFWUgtQzFjVEhjSm9GVzNZb1pMUDFjakhXb2F1aDNSdy1Qd25yLVRhUU1vTk1tOTdfa09FNzYyUUY4ZVVwMUczSE1tWENXaTRsdmxrZ2hmbEZEdU0?oc=5) <sub>Startup Fortune</sub>

</details>

<details><summary><b>Tesla</b> (203)</summary>

- 📰 2026-11-10 [Tesla Renames FSD to TAD in Europe: What 2026.39.100 Changes](https://news.google.com/rss/articles/CBMia0FVX3lxTE1HaW5uVWtDdzNfdmVSQlJnYTV5NnB2cEp5enBsM2JxTmR3SnlFbk83OHRfQ3pCMEZBai1vQ0dRbWRGU2ZZd0s0M2taVUdwUnN2S01JM0hmb3JHaTdMSU5aNjZycVZERmNmWWpB?oc=5) <sub>BASENOR - Tesla Accessories</sub>
- 📰 2026-11-10 [Tesla Robotaxi service launches in San Antonio as experts examine safety and future innovation of autonomous vehicles](https://news.google.com/rss/articles/CBMitwJBVV95cUxNY0dnZEx1aVgzRmhNZDlYeW1vZmFTcmlnOTFTcllIM0ZVTXh5MWQxdVRrOVRCcWxPMTU2d3NiNXZhZWg5czV2cDJzRkFJRVVIOG5vZlcxcXZBNDh2ckoySXc3c080RlpOUW5RY0pfUmZiWC1GNFRLSkdEMnZ1VjJSM2NPMDRWVHg0MUVvSU9Cd3BOdGFMTW90V3FzUHJFVkJ5QWlvM1Z5Z2JfNEZOSzdyczJxRmw1Y3VpSlZfeWl0dHMySFh0QUZNY25XR1pjUUY5SXcxMi1FcFN1QUxyQmZZQmdPSlZnMjNHUUVETkRseFNuWHFUZ2otWjJheG4wN2RibTBtT0tQY0FMdGFlQ1ZVemZzQVNUVlpNVmxfUkVfS0RNcmRZQU5VUjZSV0JmaFdyR0k0V0FZQQ?oc=5) <sub>kens5.com</sub>
- 📰 2026-11-10 [Tesla exec hints at a wild fix for Robotaxi’s biggest weather problem](https://news.google.com/rss/articles/CBMiekFVX3lxTE4yam52YVpONThETzE1Z2d6clVyNktSd1V0Uk9uejJPcThZemZQQnpRSTFtSzBTdmNSc0JjN0tRNWxYNnNWVUk2WDloVVYzVGxjeHBadE1JWHluNE1iRDQwbmhSVm00V0daT09EZmMzSU5CQUt0Nk1DQTFB?oc=5) <sub>Teslarati</sub>
- 📰 2026-11-10 [Tesla 2026.38.4.5 Is Out: FSD v14.2 Lite and What to Do](https://news.google.com/rss/articles/CBMia0FVX3lxTE9ha2pCV0VmbTNxTllKa2hZcUlsU2U2V2Jma0Z5TUZGS2REM2pRQ3piOVdCa3huNFVDU0FCUE44emtlRlNpcGxoTkQwdThZTjRqaURERG8xRGd2N0NoN0JNVjZyd0ZXUFVQQ3R3?oc=5) <sub>BASENOR - Tesla Accessories</sub>
- 📰 2026-11-10 [FSD Beta Safety Score Resets: What Owners Need to Know](https://news.google.com/rss/articles/CBMikgFBVV95cUxNb0oyRWx2RHBibkhfSy1GeUlDbmZBRXZYZmZITTBRU2NVZl9BMFBNdlNSelhQYno0NnBGcmdTVThyZWtWX2hKcERZa0V6Y2FlT25aLUpWcXpoUEJOd3JpTE5LVzJ3YXM5eVhaSTBOTk5YZmZia2NjQks0WGhJUWkzS0pPb0FlUDktT3ZCUTE5TWN5QQ?oc=5) <sub>BASENOR - Tesla Accessories</sub>

</details>

<details><summary><b>NVIDIA</b> (109)</summary>

- 💻 2026-11-02 [NVIDIA/nvperf-core — Core NVIDIA Nsight Perf SDK APIs and libraries for collecting and analyzing GPU performance data directly from application code.](https://github.com/NVIDIA/nvperf-core) <sub>GitHub</sub>
- 📰 2026-11-10 [Kakao Mobility Partners With Nvidia to Develop Autonomous Kia Vehicles](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1VS0gxNGViX2IyQ211cVhMSTRxQ0lUeU9GcHhZSVhUQnRSaU82bGtNM193eUpvTmYwd0xZaDR2eDdVdG04U0hfZ2Q5QV9jM0hnM3J0WHIyb1lxS2tJMlA4WXZzbGVQSWc?oc=5) <sub>THE ELEC, Korea Electronics Industry Media</sub>
- 📰 2026-11-09 [NVIDIA Physical AI in Korea: Samsung Cuts a Chip Thermal Solve From 18 Hours to 41 Seconds, Kakao Targets L...](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNcVpDbFB1RzNmMER6czRmUEszVHEyZzVITlkzazJmLUNKcTdJQklBeHVzRlo0UndWb1pIN3BzUWpqbFd6OVZ2eW04SnZQdTg5R05Jb25IeE1SNndnamU1bnlFbjRsbS1VbDdhZUllcVp3VmhwY2ZZajQzOVhJQ3U2d0dGZ1JKN0lKMHo5OFNidlJTWUlQMUdXWjJKelBRNG5TZFNZQkVzLWE2d9IBqgFBVV95cUxNcVpDbFB1RzNmMER6czRmUEszVHEyZzVITlkzazJmLUNKcTdJQklBeHVzRlo0UndWb1pIN3BzUWpqbFd6OVZ2eW04SnZQdTg5R05Jb25IeE1SNndnamU1bnlFbjRsbS1VbDdhZUllcVp3VmhwY2ZZajQzOVhJQ3U2d0dGZ1JKN0lKMHo5OFNidlJTWUlQMUdXWjJKelBRNG5TZFNZQkVzLWE2dw?oc=5) <sub>StorageReview.com</sub>
- 📰 2026-11-09 [Market Today: Nvidia, Tesla, Boeing, and More Drive Headlines](https://news.google.com/rss/articles/CBMinAFBVV95cUxNd1BNQlVZLUR5cXhQUWIwM2ZsTHBEVUhHWlQ5M3BSQUJkSGM5eTN5WXRrV1EtSUlJU3pKLUpPbkVtOUg1WmNzNUt1M1VNd3VIVkF5RWJJbUVnS3VQbWhKRTFMT19VS1RvNkZENk52Mmp4OG5QZF9HZ004SHF2NkFhcVltSmtiMXhHM3Qtc3BCdGp0SkJqY3BtR2dTbTk?oc=5) <sub>GuruFocus</sub>
- 📰 2026-11-09 [Nvidia Hardware to Run Kakao Mobility’s Own Level 4 Driving AI in Kia Vans](https://news.google.com/rss/articles/CBMiqwFBVV95cUxOdnhiQkNMYk5WWWNtak9OVFdvdjdJYzNQT3htNzc4MjFiemlCRVpSaHJQUHlqd1N3NUVQZ0pESjBHWXZpR3RkdDVqNDhTc3RJd0l1ak96OXRFeEF6T0o4bWdnNHA5dDZjTEhWQjJobWtmY1JXMXItQUdtdUwyeE95WFR2Znk1dGI2eXk4N1hXMmxvVHFxU3J6R1l3Z2hpNEdmSDBTZjl1M05HaGc?oc=5) <sub>Electric Vehicles</sub>

</details>

<details><summary><b>Wayve</b> (38)</summary>

- 📰 2026-11-10 [What Does CoreWeave (CRWV) Winning A New AI Training Deal Mean?](https://news.google.com/rss/articles/CBMimgFBVV95cUxOcDNZY2dVeVo0ZWNwN2hmZDlEZFJOelNPMy0yRmhWRzV5UjV5Q2tmNEtxN0p4d2pTb29iR0FtZjFueXJvUzB5cVpxaXBnNXpwelZXTXFEdzFvalotZjB2bWc3eThkS3BLZ2xLN3haOV8xRERuY0hYRFQtVjRsc1VvNE9FclhlT1YyVnFhWkFtaThfTkszRlVNa3V3?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-11-09 [CoreWeave Stocks Jump 6.96% After Multi-Year Wayve Self-Driving AI Deal](https://news.google.com/rss/articles/CBMilAFBVV95cUxORzJGLV94c2U1YUJ5LWFjR3NwTkxDenpSbnJkRkN5bTBGc2I0WU1WYVBlNUoyQnBQRzI5VE92SnFZQUw2ekZQdm5TY0c0S3cydU9wMHZmbU5NZnJSOUk4T2dPU3RITUZiRGw4elFYdE4ybGlwWElEZG9Qa1kxQ1ZzdERkcnBjdGVwMWs2QVZXZ0FOcFFy?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-11-09 [CoreWeave signs multi-year deal to train Wayve's autonomous vehicle AI](https://news.google.com/rss/articles/CBMixwFBVV95cUxOcXRBa0pWc2h5eFI5cFEwdWFsdzZ5UmtmNkFoeGxraUZiSHpDSkZuUWZaX0ppSG0zeHhxQTNZbHVadk1yekR3WE95YXczUXUzWXN5MXo5VElGU3NUd29HRVZDaGtWV1MybnhIbkFwLTBZSWphSERqc2xLSG40TVFmN3N6dkpCV0ctNzNQajZpTDFveVVfWWdyZHhVVlFVa0djMEFMUXo4QTBaTkdCUzBOcllSdEh0MnJ4enZWWHFIN0xaOWdma3Nv?oc=5) <sub>StreetInsider</sub>
- 📰 2026-11-09 [CoreWeave signs multi-year cloud deal with autonomous vehicle firm Wayve](https://news.google.com/rss/articles/CBMixwFBVV95cUxNaXNSZkNkSEs5dkVuaURWMnBINXhEekp1aTJEclVCNmhGR3dvZWZEcjhPMHFTYjRmRkUwdFlldlZRSWl6WkY1S3pXZjNodjhaMTJtRldaamFpNGdIRHFMdHNWOWNQeE5QRllCMUVGbE9CWTlUbXRFaTNJc2szTnMyZmF6bHM0NGMwVVJpUFdjRDRUOGRrblpiZ0t5bnpPaFpUOHIxRkYxdVNPakQyTzZwbmN5am9EUDhzcXY3bkdZaVV3anNtV1NV?oc=5) <sub>Investing.com</sub>
- 📰 2026-11-09 [CoreWeave Signs Multi-Year Agreement to Support Wayve’s Autonomous Driving AI Development](https://news.google.com/rss/articles/CBMipgFBVV95cUxQZ0pMUW82QURwSTVwem1NYUVBamM1VFp4aFYwdHNtSXNrbVBmZ3dmbjVDaHN5ZlVLeF9wMmQySE5VaXR0eEpJeFFjTUFIMl9lOEZZYksySUZheW9iU0kzWndMWVZtaG1rOThmZXNUbTNYMG5oZlJMYmtUMmVOeVdSX3NfVDdEbXBIdXdHRmVkQWFCSy1yZ0JVaHJwSTMtNXdBTXpvcEJR?oc=5) <sub>Yahoo Finance</sub>

</details>

<details><summary><b>Momenta</b> (71)</summary>

- 📰 2026-11-10 [Zero Interventions at the Arc de Triomphe, a Love Letter in the WSJ: How 100% US Tariffs Fail to Halt the Global Surge of Chinese Automotive Tech](https://news.google.com/rss/articles/CBMinwJBVV95cUxNQnNxQ2NGS0VCSkc0RXVpSFlnVTh6WUQwa2NEUnpfMXJlNEVqWW5FMW1yazM3UXdMVTRWZllLWERCRWphWkRKOTM0YUUtby1nWVMwYnp6V2ZqUFI3bTlEYkhwYUNjcmVVWDdKSTc0c3hVSGN0VThxWEFxZU1TUHBRYWw0d1pmMzNsUE5xYnhENTRCMzF0ZkU1a2NBejFzbTZXa19UUFVoTnRBci1LTnpURXlPMHd5UFlWakVBQWpsWndNQ3pBcjk1VHJxdHFBWXl5SzhtVmxwTE5XSjZKYkVPZmJpUVNsU0toN0ZYQ1ltSWJsTXFZVjc3MGJoU2c4RHJuS3JDRVVkRlRXTmFqNzRheG9lemZuLVZXVWM5WVEzZw?oc=5) <sub>巴士的報</sub>
- 📰 2026-11-10 [奔驰跳过L3直冲L4，引入Momenta智驾](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9WOVUtMEhKamt5NVIxMGkyRFZBOFI5ZUw4MF82Z1VVR2FYOGlNNFVZOUNTdUhCbW93eTIwZTlOWVNRZmlJbnEzcXpzUzRxVjZ6cWp1MEpLbzBXN00?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-10 [电池+智驾外购、配置看齐国产，日产NX7能打动看重合资的用户？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE84TlFBTHJmWFp4S0ktWGFHQzU1S2NOWi1tMGNJcmZGd0lwUmZhZEFqSkt4RVdCQlE5aTRXajhJaFVZaXQyNGgwUmlxT3ZIOVNRaDE1TUpBVE5UOGc?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-10 [3亿元！上汽集团成立新合资公司](https://news.google.com/rss/articles/CBMiiAFBVV95cUxQaVlsRnZrOFJwN2I2clBxdlJXRGZfSlhsT0ZMcjAtZ2J3U3FIc3RhX2hyNDVoaEJNRDNUaWpnTWVQa3R1cl9CV2ktcVV3ZzBjdjh5cGtDRy1MQTduVkVXRmtMQUFzejhGREtIM2I5NlhzT2gtWTR4c1RVV1dILVpJYjl0T3Y5ckZz?oc=5) <sub>搜狐网</sub>
- 📰 2026-11-10 [铂智3X试驾测评：9.48万起买激光雷达值吗？3个维度说清+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBLZG1ZOWN1Y1FPTXVSUzc3SlQyQ0p5QTlNRXFzajdESUtHMzBjZ1pGWGF0TmdWckhYemRfbG9NQ005cWhmc2lOT2ZTOWE0eTRHb0xCMTlWVG9Hb0xYeVJJ?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>XPeng</b> (148)</summary>

- 📰 2026-11-10 [Motoring: Ideal launchpad for flying cars](https://news.google.com/rss/articles/CBMiU0FVX3lxTE9wXzFPZlQ3dDhuV1pmb28tdHYwa2UzcTZrZmV6YWktalh3cWhJQm83OUtGVEs5clJITlZwdFk0bHZ4MVJYVTFzamc3TWxEWTRROUpn?oc=5) <sub>Gulf Daily News (Bahrain)</sub>
- 📰 2026-11-10 [76岁张艺谋被小鹏GX圈粉！现场追问智驾趋势：感叹中国科技扑面而来](https://news.google.com/rss/articles/CBMiWEFVX3lxTFA4QjhXQ0tnSXQzUl84RXo3bE81VV9IR2xqeEJENElPTU1MNGFSMGJGSHZmT3pmMzliRXJzVVc2YV80cUVNZDFPd2lWM0N0S1dRX01RaUNYN0k?oc=5) <sub>驱动之家</sub>
- 📰 2026-11-10 [手握25万，3款新能源SUV谁更值得进家庭清单？小鹏G9L给出新解法+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9XYTN5Z2lwLU1EMTdvNm5QTl9YVmpjRTFpQ1E2THRTMjAyZUhXUTdOOURFMG1NVGpQc0pwdVpVT0lJcVQ4SG5EcGVDMUx6aEU5d1JnZ1lkZE1XYWg4Nlhr?oc=5) <sub>新浪网</sub>
- 📰 2026-11-10 [小鹏G9L入列25万级大五座SUV推荐清单：理想L6、极氪7X、智界R7怎么选](https://news.google.com/rss/articles/CBMiX0FVX3lxTFByZ3BKMHd1d2d6MU05OFNFNWNvYXYzcFBJa3BXTHhxcTZCaU1ad0M0OGpzWEViSWFlcXllX29oSDEzMVEzcjlJLUg0S1hRYmdfeDY5V2FFaU0zNjFnODRV?oc=5) <sub>新浪网</sub>
- 📰 2026-11-10 [【视频】国产车挑战德国高速！德国试驾小鹏XPENG L03](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1uNFU3ckpDUklzejVKc1NqWjVTaks0T3pEXzV4X3BBdEpJWG5xRV9xbE9LdWNYT1hJMkU1SGdYZVlKMGUtSEd5REVIeXdHYm1YbGxYV3UzOG13N1U?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Li Auto</b> (112)</summary>

- 📰 2026-11-10 [Li Auto's updated i6 orders estimated above 50,000 as Deutsche Bank sees year-end delivery recovery](https://news.google.com/rss/articles/CBMihwFBVV95cUxQbXpuYThJWERLMlRfUE1oaEZUb2FneVVfNUhtMDVkLVBBSnpHbWk4OG11MEdtT1ZrYW8tVF9pY1FSbzhfZ1FreTROMTJ1MTBoU2F3YU44Ymx4QngwZGFYODE0b3lxZFpNWFhVaHBUSm9DSmJfR2FlOXY3VjhXa1NlZE9abDQ4Yk0?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-10 [Cyan is emerging as a signal for autonomous driving, UDC, OLEDWorks and Audi to evaluate light-blue OLED lighting](https://news.google.com/rss/articles/CBMipgFBVV95cUxQd2pUSDY1Q2xnWWxQYjhaakxyR0JBOXpxSG9qRkdTa3lJczZyNE4tMUt0UjVYUTlNbUlxQ2ZrVVUySnpXdzhwRmk0SlFaMFo3bzJYZUotY2hteEZxdVFDdFdLenZwOUlNRWUtQ1NMNjJobFM4N3NWUDB6ZGZwWl9LamxsbXVJb0g0cHROTldhRlZ0aXhrTkozVHVtVjVlb0EwVXBlZE9R?oc=5) <sub>OLED-Info</sub>
- 📰 2026-11-10 [China’s Li Auto makes Asia-Pacific push announcing entry into Singapore, Hong Kong, Thailand, Vietnam](https://news.google.com/rss/articles/CBMi1gFBVV95cUxQc2tmb2FhYjN2V1BtSUUwanJHcW96Ny1kRDJHYTBLeDdENDRuVl9USXpTNUR2dnpoU1ZkTTE0RmdrT21YR25MbVE5Nm1jRDdtWjdKMVV3azJxQ0ZwYUwwZGsyRFRmYV82VXpnZ3RLbDJnTVgzblE4OU1oS05qWVJVclFWZ1MxSG9SMFpkUUYzM3pQQmFJMldDb253cEY0RnNzUFVFdmdVc01BU3hYMDhyOWpHcV9USHNrN2JTU1d6aFBDUUx0UFI0TFBzQVZ2SWNXX2tLSzZ3?oc=5) <sub>The Business Times</sub>
- 📰 2026-11-09 [Nio ET7 Sales Hit Record Low in October, CPCA Data Shows](https://news.google.com/rss/articles/CBMikwFBVV95cUxQbG5tdkJZRk94MTFvQjBraUc3aF9VcXdlaHBoSUJOS0lBSVluQkdCTDlWc2ZhVFhzOHl0S2ZreDE0ZmhDMTZpa2xiR0dxVGQzdkxsZ0kzVjZtOXc0c1Atck9abEZ0OGcyQzczV1pLR3lPYUdkakFTYWRDVmVNSkhvU0RMOUxabmZnY1hlZkxEWGpHdG8?oc=5) <sub>Electric Vehicles</sub>
- 📰 2026-11-09 [Nio ES9 Sales Fall 13% in October as Flagship Nears 40,000th Delivery](https://news.google.com/rss/articles/CBMiowFBVV95cUxOREJQdWNvZkVtbWJhQTN5TGxVbWZvbDZ0REFtejk5N2J2blhqLWEzSTBzQ05EbF9KQVdUSnkzYmg3X3R2b0Vuc19UNTZVUkRoenNhcXNoMUFtNFFFdV9MdmdtM21PbnZweVpPMDdqYkNoVVY0aVY2SFJ6NlZCZWNsX19kYjBIdk45Yk1HVHBtRDRyZm1sMjlZelZadWpoSC1ObTJB?oc=5) <sub>Electric Vehicles</sub>

</details>

<details><summary><b>NIO</b> (68)</summary>

- 📰 2026-11-10 [The Subscription Trap: Are Luxury Carmakers Charging Owners Twice?](https://news.google.com/rss/articles/CBMisAFBVV95cUxQN1c4d293VWwzWTdscExVVGdoMVBId2ROS21kdlV2Mkt0ZU9nYnRMenB6UEhIeFJqNFJ3NEZVcW4yR3dDd2NQRW1NOHBpLUx6SlNaQlZWeEpxeGhodW5TWE1iMGpXZVZGR0llYkp4TkJlM1NuQ0VzTkI3RHp3aUY2VmlVQy12bTMyVjBqMjMzQjlQdmFVXzJid2lYb3ZkWnkzYUpRaTVPV29VdU82YmpHQQ?oc=5) <sub>LUXUO</sub>
- 📰 2026-11-10 [【视频】蔚来ET5 2024款75kWh租电版](https://news.google.com/rss/articles/CBMiW0FVX3lxTE11RVBrajlfNzNsUUlqOWdhUS14N29oQ1JyUXJxclUwMHpwanhMbXgzWDJUNFFYMUw2Y01mOHVpSjlJbGlrb3pWSmVjNXRXYWJpem5uU0JvRk82YTA?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-10 [家用新能源大五座SUV盘点：小鹏G9L、理想L6、极氪7X与蔚来ES6怎么挑](https://news.google.com/rss/articles/CBMiX0FVX3lxTE10My1MbWpHVEV0bHBBbVd5X1VKd2RUN2NmVVN0Y0xMR0VJTWVDbkJ2OFliNF8wSDcwLU5mQWExWlU2bUlvYy1xSWFWMHRiNTJFVVduZ1FOWk9OXzdieDFr?oc=5) <sub>新浪网</sub>
- 📰 2026-11-09 [Nio ES9 Sales Fall 13% in October as Flagship Nears 40,000th Delivery](https://news.google.com/rss/articles/CBMiowFBVV95cUxOREJQdWNvZkVtbWJhQTN5TGxVbWZvbDZ0REFtejk5N2J2blhqLWEzSTBzQ05EbF9KQVdUSnkzYmg3X3R2b0Vuc19UNTZVUkRoenNhcXNoMUFtNFFFdV9MdmdtM21PbnZweVpPMDdqYkNoVVY0aVY2SFJ6NlZCZWNsX19kYjBIdk45Yk1HVHBtRDRyZm1sMjlZelZadWpoSC1ObTJB?oc=5) <sub>Electric Vehicles</sub>
- 📰 2026-11-09 [Nio flagship SUV ES9 nears 40,000 deliveries as large SUVs underpin brand sales](https://news.google.com/rss/articles/CBMicEFVX3lxTE1YaEhSVi04dDRFcmhTN1JMVDZvbjI4d3B3Nmd6Um93SV95UXJoanVweWcwbmNweU1TcHNWSExwU3BGeXNVNE9mN1dVZ1A2ODU5UnF4NTlNQ0xyUjkzMDU0TEU4c1NabV9vR1M3VU1qb3E?oc=5) <sub>CnEVPost</sub>

</details>

<details><summary><b>Huawei</b> (181)</summary>

- 📰 2026-11-10 [Li Auto's updated i6 orders estimated above 50,000 as Deutsche Bank sees year-end delivery recovery](https://news.google.com/rss/articles/CBMihwFBVV95cUxQbXpuYThJWERLMlRfUE1oaEZUb2FneVVfNUhtMDVkLVBBSnpHbWk4OG11MEdtT1ZrYW8tVF9pY1FSbzhfZ1FreTROMTJ1MTBoU2F3YU44Ymx4QngwZGFYODE0b3lxZFpNWFhVaHBUSm9DSmJfR2FlOXY3VjhXa1NlZE9abDQ4Yk0?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-10 [CATL says expanding swap network will help accelerate sodium-ion battery adoption](https://news.google.com/rss/articles/CBMigAFBVV95cUxQNXJXMzEyT2puRTVING5DWC1FODM3ZUFFUExJVk5NOVppRkdCSi03aGpDWm82N0hMRVdSY2hWTHQ1cEJ1M2RpWC10T3JjQjBCRGVyYXVMVU9QTkJqRjdxa2JQOGpqeDNFX21IdllieXl0RW5KQ001SUtWNkxXYUltOQ?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-10 [GWM Wey opens pre-sales for second-gen Lanshan with new boxy SUV design](https://news.google.com/rss/articles/CBMifEFVX3lxTE9zWGg2UEZqempkTmpUNV9uR1NRa1h6Vy1jelUzMEwwamVYUmpHbXhGUUpCNm1lbi1USDhLZEZrbk4tY01aVG02NkZrcVRDTFhCUzE5Tlk2ZmNUTU9hLW5wX0JqSFR2end3a2RFcEYtM0kyNm5ISzBWLVY0MDI?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-10 [Huawei MateBook Fold S puts a 14.7-inch PC in your coat pocket, with a cover screen on the outside](https://news.google.com/rss/articles/CBMi0AFBVV95cUxPTUwtUm9aekMxaVBBVU42THhBU0s4R3lvd3c3X1ZLazJrRmo2ZUtnSEJpNHA4VkVjT3prUHl2ZEN0YzZCdTVHN0xPVDVOcm1KdVpnME11N3lHMUlzQjZhYnNUUGktQjh3aU9TUTFtWFE1RDl3NzBxbFB5SVdrUVFwWnlsSUJqZGVzclVEcndnLWNOVkw0RWF1OG1pdTFFdDVraFJMUVJVd3BWZWlRWXZpWTZvMEZBWk1Od0x5N1p0Qlk0VVM4SE1DbXhWeEdUVmdM?oc=5) <sub>The Gadgeteer</sub>
- 📰 2026-11-10 [华境 S 大六座 SUV 累计交付突破 4 万台，标配华为乾崑智驾 ADS 5 Pro](https://news.google.com/rss/articles/CBMiYkFVX3lxTE9XbDdISFBkS0RuRjNwZ09oQXdoNEFPRWJuTmVGYWhmcFE2YXptbXNZVkpQRldYeFRKS2tHWU5lRW9TX0RtczlibzdWUU9paVRLZFpFc0IzNThzbTZNZ1Q5QmpB?oc=5) <sub>同花顺</sub>

</details>

<details><summary><b>Baidu Apollo</b> (39)</summary>

- 📰 2026-11-10 [萝卜快跑28城落地，百度Apollo World定L4仿真标准](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBIX01CdUNMdW8zZG9CWFgzM0RpSWFQQ3FjQjdKazFOQ2R0eXpKRFIwZXdvOHZ3b3VVOEI2WGR5R0tqNWs5MDI4TDJIYUJ4bnJUQUVqTWtUUmFwN00?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-10 [百度Apollo World首秀，萝卜快跑2.4亿公里全无人](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9IOHlYeHpXSnBsX1RQMFA1ZV9BclR2TXI1WXVXS0FvOVVVRlVTNGUxaVQ3YnY4UWtGa05SZmtHYi1seW10NV9adkRLLW9LZ3lBa2p2M3VRZlVNbGs?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-09 [China robotaxi services spread but still require long walk to pickup points](https://news.google.com/rss/articles/CBMivgFBVV95cUxQOUpMWFNyUU92N1BuckN4QkRtUDV0MkdRdDUtTWowN3VmVWgxdFNTQ3o2cVFiM2o5T1Joc25sS05OR2xGUWYxT3hIc3NGMDMxWEhha0JxNGNOSUlKZWNjTkJVUlF5enhZRnJNWkdMOHppNWo3SVBNa3FyQUNZY2dzV00wbTRQOWRqdG5RR0hJQkdyMFZOZUtWUEtDTmxQNTI1NktyTkVyM1M0X3NzeU5DWTlPNkpjV0N6VndsNGpn?oc=5) <sub>디지털투데이</sub>
- 📰 2026-11-09 [Weekly Recap: Robotaxi expansion and Lyft Go subscription launch](https://news.google.com/rss/articles/CBMiwwFBVV95cUxPcmd6T05CeEN1eDVfUGtrN0U3c0RXOS1sMUNCNXdvblV6WTVpNGFDTXI4NE9QNm1DWEhZZzlSTTQ0QXVKeElRZVNYcDJuLU51MUVQVFVXTXFhenVseEhoMnE2VnVlMW1ZVWFwNDZuQWJnUk5JM3czejVkYUJ6SllXdi1oVWtXUncxeEpzUllwQ0RheG1PNWM3aDVIWlpLdUs4UXB5d2NyNU1VYnRFVHpWd1FEZW10ZFlRUmdaUVNjU0YwTXc?oc=5) <sub>TradingView</sub>
- 📰 2026-11-09 [Alphabet’s Waymo Faces Fresh Safety Scrutiny Over Driverless Cars Near Schools](https://news.google.com/rss/articles/CBMitgFBVV95cUxOdDNqd3dHSWpnd3dJZGlfZkhtVnRBdFQ5bVlPYkpSV1B2SDgwX3k1bC1MODNTMDdzTmNkQmc5aUtQNko1WUNzaEJBOGdtbDRValVCTjZicTJtTlZxdkxyR2hjSTR4M2FrajlLT2phZkMxaTBUV0x4ZEhrcU4wR3d6Y21iOHJvMUV1V3hEd255TXhfTXprXzZBanNBRVk0VW5ORXJPMnBqbVh4RE94V1ZUazV2QUNXZ9IBwwFBVV95cUxNQ0hRYWlmRG81UUtxSUpsTzUzdHloQmpkTExCWmJERld0N3pXOG1KOUc5OXZ4anJNbU9NTUVIY0NWRl96ckNMdlJ3Q0kxYzJheEFMUDJnYXpsUkw5RlZiaXBSdWRPcVVhMGpDcm1LaklYUkV4MWs2NVVaUlpVbmxFYVpOSC1uVEhtWDVFdXhudzBtSWVybHRrbDZESjJESW8wV2xjY1c0RC1hVE5wM2NnMGxIM3p1RUdOcTdFb3ZUNE9qb1k?oc=5) <sub>Analytics Insight</sub>

</details>

<details><summary><b>Pony.ai</b> (73)</summary>

- 📰 2026-11-10 [CDG autonomous vehicle stops in yellow box in Punggol, company adjusting software after incident](https://news.google.com/rss/articles/CBMiwAFBVV95cUxNdFZGdWVlOXcyaEx1Z0JYWnoweXFLbGJjY2dfWEVnWS1Xc2Q0ZU4zaWxCbGVqa01WWTRTRVd5OVNpR2dpR3hSR0FCVHdHR0hEbFpwSjNiTTczZmFNSkx6NFJoRGdWa2prRUhQeEZicnpTN2UxUWxXZGUwaTNGdFpEWG9CNzl2bE9KTV9TYkVxY1RERzlPUnJXSjJPWjlfc0ZVdzBpekdjNzR3WmtoVC1BS0NmQWdrWks0enRUOUJWdjE?oc=5) <sub>Stomp Singapore</sub>
- 📰 2026-11-10 [11月10日热门中概股多数下跌 阿里拼多多跌超3% 京东跌超2%](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9BTU1kai0tem9QQjlaUFEwMTlHWHA4ZDNZZXZRQVdNZVNhSWFSdEc3cGFOMU1MYjN4Q2doSjJMaEdMbzRNQmJCaEhGWDEzLVJYamhXRF9MVHdjMU41aHJj?oc=5) <sub>Kuai.Media</sub>
- 📰 2026-11-09 [China robotaxi services spread but still require long walk to pickup points](https://news.google.com/rss/articles/CBMivgFBVV95cUxQOUpMWFNyUU92N1BuckN4QkRtUDV0MkdRdDUtTWowN3VmVWgxdFNTQ3o2cVFiM2o5T1Joc25sS05OR2xGUWYxT3hIc3NGMDMxWEhha0JxNGNOSUlKZWNjTkJVUlF5enhZRnJNWkdMOHppNWo3SVBNa3FyQUNZY2dzV00wbTRQOWRqdG5RR0hJQkdyMFZOZUtWUEtDTmxQNTI1NktyTkVyM1M0X3NzeU5DWTlPNkpjV0N6VndsNGpn?oc=5) <sub>디지털투데이</sub>
- 📰 2026-11-09 [Senior Auto: Delivering Reliable Autonomous Heavy-Duty Transport Services Worldwide](https://news.google.com/rss/articles/CBMiqgFBVV95cUxOT0ZfMmFUWmdkbW5xUjg0Q1JOUUl3TnlJb2FHblluTEVyRGZTY2hWRjV3aEozSnVLZjVTZFRYVl82Z3U5YzdrcFBzNjJJRElwOFMtblNpNXB5TEVETjlUdzFEMnItYWlNbnRoVG1OYzNrUFZKdVVlRVl5U3E4bHNyeXVTMjNNb21CLVUwNzYzWC1xeWRfNmJONDUtVHZTTDNFUFRlTGhZQ0FhQQ?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-11-09 [From human-guided learning to self-evolution: How AI is learning to drive itself](https://news.google.com/rss/articles/CBMiggFBVV95cUxQdS0zMGZqLTFicUpUNGhQdVlEdlRJemZWOWh0NngtRTlPTEhRQTA0dW9ncDM0MTEtc1g0MzJYazV0YWdHQTJuV01pZDR4WmxUSXd2WWFWRVNiQVI0QUNOaHN0NTZOLU5IM0lINkVtbnJ6dHhQMUY5ZklpVGJuVjJjdDJn?oc=5) <sub>China Daily Global Edition</sub>

</details>

<details><summary><b>WeRide</b> (68)</summary>

- 📰 2026-11-09 [WeRide to Report Third Quarter 2026 Financial Results on Friday, November 20, 2026](https://news.google.com/rss/articles/CBMi7wFBVV95cUxNMEJOY2xmTXhkb0JaRnFndmFUVE0yOC1iX2lrRE90Rk9QcWIzd0FEa2pheFlFVHdWQ3M2cGdMa3pFRkh2TXR1MlpwS25MTUh5d29NNGIzTWFxZ0dPTlB0YVhfSUpXMndJSmFMZmo3alRMQUNZWlktcThwWWN2SkJzWHBQSXcwSG9sUlRFMlZCTzJhYmtGNEhjanROYzlEajZEaW1YaUxjSDBLY1dMb0FwQm9qVUN5TWNLdDJkSElZS0JhaEtGYTdxQWN1VmhxblYtdERXQ3Y5SE9UdGxsZUphRjlzRURaZFJnVGVBYmVrWdIB7wFBVV95cUxNMEJOY2xmTXhkb0JaRnFndmFUVE0yOC1iX2lrRE90Rk9QcWIzd0FEa2pheFlFVHdWQ3M2cGdMa3pFRkh2TXR1MlpwS25MTUh5d29NNGIzTWFxZ0dPTlB0YVhfSUpXMndJSmFMZmo3alRMQUNZWlktcThwWWN2SkJzWHBQSXcwSG9sUlRFMlZCTzJhYmtGNEhjanROYzlEajZEaW1YaUxjSDBLY1dMb0FwQm9qVUN5TWNLdDJkSElZS0JhaEtGYTdxQWN1VmhxblYtdERXQ3Y5SE9UdGxsZUphRjlzRURaZFJnVGVBYmVrWQ?oc=5) <sub>The Manila Times</sub>
- 📰 2026-11-09 [WeRide Inc. to report Q3FY26 results on November 20](https://news.google.com/rss/articles/CBMiowFBVV95cUxNWXZaZHdsb28yS1c0MHFzMWNqOXpyRzNpRlpmZ01IVUxvRDh2cFYyZXJoMVZnS25rUFJNMlZ5emd0Z0xUMzdHWHRFREtmLURzeWF4ZWFiVUdaRmpUUHlEemtDWmFZQjhTdmlLNm5mVHhGNkxMUS1XUXlqWERFT0dXZ1NwSDRQMThjS29NX1YzeXktNmZPTTQtUXJ3Ymk1N2pHbnNB?oc=5) <sub>scanx.trade</sub>
- 📰 2026-11-09 [近94%的用户天天在用，文远知行10万级智驾的“真香定律”如何被验证_行业动态](https://news.google.com/rss/articles/CBMiWEFVX3lxTE96c25USFBkaFlyMG13MkNfTGpTY0hsLXZvUGZYNzZGNTVMc1NxUndMcDEzUTdDalNYVlZJbjFCajYtRWtSeU5oT2hzSnVxNjhfa3M1Mi1hUjA?oc=5) <sub>投资界</sub>
- 📰 2026-11-09 [文远知行将于2026年11月20日（星期五）公布2026年第三季度财务业绩](https://news.google.com/rss/articles/CBMipgFBVV95cUxOT0g4RFpCa1hrMmpNQllRR2gwLVozazVPYXNfdWY2NzFIX1czWV8wWFV0cng3enhCYy1EUGZJeEpTZmJHcDBReVVJT0N3dmw2VUdsVUlqLWhGMldiZU93SkFIY19OdVMwdXhCdE45eWhETldoZFc4dmtub2U3S2RxUGtVT2RuUEZEaF8tNlNRajZIcmNWOGpLLURmc1dtVU14eTNkcHBR?oc=5) <sub>富途牛牛</sub>
- 📰 2026-11-09 [冠军能力终于下放到10万级市场 文远知行WRD3.0智驾包揽冠亚军背后的秘密](https://news.google.com/rss/articles/CBMiWEFVX3lxTE5ubS1hMmVhbjJYb3hqV1I2Q1V3ZWtCS0dDc0J1SW85U2xOQk1nVmMweTVVbS1pcllhNHNVV2xLM2JUdS1sczlpWGF0WnppMS14TVRpaUNCZ2U?oc=5) <sub>驱动之家</sub>

</details>

<details><summary><b>Horizon Robotics</b> (61)</summary>

- 📰 2026-11-10 [Apple's HALO Ignites Physical AI; Manycore Tech Surges 30% in Afternoon Hong Kong Trading](https://news.google.com/rss/articles/CBMidkFVX3lxTE9kRDdUVnMwSm1KSzFmUzlLVDBTVG1zUHNzaTVRLUdtUmJwTnVHWWFGbjFTazMtSnJVQWtoQVFUMm5MQ3V4dnFkNERfUzVxQjhxalZ4QzVjVTl5bVI5NGlLQmJjd0Y2LTlqRC1xdk5OS2VwQXZCclE?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-10 [网传比亚迪天神之眼C将停产？比亚迪紧急辟谣：均为不实信息！](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1kelpMaG5NWkJpLUZWN3BIOHdqRjIxWWtWZXZnTy1mMTBJVU1CSmRlMERRMld4dVkwR1JyV21GTm5VZUhXUmVZeUJwN0cwQXJENUVBcm5pVXEyN0U?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-09 [英伟达智驾芯片份额从45%跌至30.2%，地平线 华为芯片份额紧追](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1Xa2lvYmRDdVM5alNieHA0OFU2WXZMcUlqaTRCMW53c3FfendtYXVWNm5HLW9FZmRYbjR3a1B4MklUemswU3NLeXJmZnUxblBOa2luOTdMa0w5VEU?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-09 [德国总统试驾大众ID.AURA T6与ERA5X 智驾获高规格关注](https://news.google.com/rss/articles/CBMiXkFVX3lxTE9zNlBLZXU4NmlKSE0yQ0c1UWxUWTljTUNnU1lsV19NU00tMlNJcFJDZFdDRzU2bHMzVmpuSUNkdWRiY2d5WWJtdjAxNTk0WTQtOEVGYnh3MEt2MzJFakE?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-09 [iCAR V27：不到20万，把“精装”硬派SUV开回家](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBsdkFORkxiNXhUYlhrejBKUVZKZFA1YUVzV2haWm04RFE3emhvRzlkam00clJxZjBxVGxsUmp1RGZjc21ncmZLUC11YnBZdGRYNHROMnlsT01TTlU?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (15)</summary>

- 📰 2026-11-10 [【视频】Model Y L 六座家用｜一副好脚垫能省多少事？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE92blRNM1I5N0tnc3BHSmRid3RwcFIwNnMtYWJwTkcxZ1Z4RDVjTVRzS3hvUm5BMGptOGNSelRBdWM4cW9ZZWtNMHN1Nm9lUkNtdnB1aUtiVkVyREE?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-09 [DFF Partners with DP World for Development of Autonomous Logistics Solutions](https://news.google.com/rss/articles/CBMirwFBVV95cUxNQ0Zpa21lNWZ6bjFZdFdnY2NIWmNuLUJIMTdTZGhtZVBDZzZ4NVRjWGthUnhWSmk2emlDVWdFQXdSYnBkR2NUSkVya0dJTEZyUUltdlBmWkdjUmprZUVYcGpTV0w2cXBVOEhLTTJhNDVYVHlXbklnUEtUbHhLWWRMaFJ5WktuUVA2dkxsamM2Vm9aa1lXaG85dkJJOUh4cHhZMkhkRDdGMlBBdzZOamlF?oc=5) <sub>Future Transport-News</sub>
- 📰 2026-11-09 [赛力斯工厂3000台机器人 问界ME7明年初预订](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBwRUJtNXlwblZfMUlJRVNxam1ub19hUWRDQjlrZDlDMWxuR3ZZMFJkMmdEbmYxX0QyZC1zRGVNbW1vV2xIQUNHUC1qQVBfU0RJQ0x2aDZoTHVWenc?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-09 [雨天接娃四车开过，赛那四驱油耗6.1L，两驱版差距在哪？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9EbHdKOVNtb0k5TEhKbkxJSVZFOWxZUXZlS3kwNWtLcTBxcTJmc2RBUEVHTzRzdzBOS3N2Z2JmZnpEZzQxbVlXR3pKeC04YzFhWnRRUGRZOVY2Zm8?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-09 [【视频】全新腾势Z9GT征战沐尘GT549，易三方降维打击，全场唯一素车漂移](https://news.google.com/rss/articles/CBMia0FVX3lxTFB2VXJBcUdVbW1IdFA1OFpLTkRSUTdSZ1hfSlhZVmdLWmdhQ2ZRR3NoUWgxeW5rdlJPeGZFdlQ5Ri02azBRdmpyUzExZzFmVEEzNG01ZU9aMV9xZHF1aHdLQVZxME5xMHozeEsw?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Mobileye</b> (18)</summary>

- 📰 2026-11-09 [Nvidia Scandal Sparks Auto Industry Watch](https://news.google.com/rss/articles/CBMidEFVX3lxTFBUSkZrRUk0TktpdFF1dEthaHQzMFdVRXQySHRMMXFwT2s2akhzT183RFlib2NuZG9lNkVoUElrOWFmbEx2OUNUY2ZhYlROQWRyZjN1eDFXdk9ObmFYQkdOUzNNM1FCazUwVWJRbWZILThIM1RO?oc=5) <sub>Businesskorea</sub>
- 📰 2026-11-09 [Maxwell AI Cuts Code Costs 67%, Runs 38x Faster [2026]](https://news.google.com/rss/articles/CBMieEFVX3lxTFBlMjEtN1BpMTdFQ1JKOTBKQjBvaFV3V0dISVg4SGtlQS1YczlwRFJsRHFEWTl4eHRiak1wYmVnS1lEMkhGaUpmNks3eUU5ckExSl9DekNyLTNhSHRNcllrSXNSbHFzMFdDUHZPVkljalNlZTV6c0R0UA?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-07 [Mobileye Global (MBLY) Lifts Guidance Following Earnings As Fair Value Debate Returns](https://news.google.com/rss/articles/CBMi0wFBVV95cUxNOF9fMHVEMXdjcUJ1ci1PZ3hqNnV3SHVHanAwSHc4TzJvTnVPSnlxYzRaekFoLUtETWdTeVFVNzNFY2U4SnNxczlUVjF2bEE4WEFPcXdDRjZQWnhKU0J0ekFGS0l2cnlLVmZTN0o4MjFSMUgwOTJ1UkEwQXREdnZXbTM3VmNpNm42YndkTHBGT2prNENPZ1JHTURJRy11a19YRjQyc1B2V0Y4aXBVamRXeFpzamRYWWpWX1c4eXpWYmdiWVIwUVRYck1OUXZjTElGaFM40gHYAUFVX3lxTE5nb2VZYnRkMGY3a1l5UTJTU1ZJUndzc1VjWHpicnNpRm1pdURTMUwzYWJYeVdYRy1kNVh3UjNub19fWm11eTVLSGVUVEJFTlBDcHExWFhBWFdPZDdsY05FRS1kUEtoRi1RVFROcjIzalJmdVA2amlrOG5OSmtlMUJtMlo0S21IUGpaRXE5b1JvV0xCaEo0OGZPaW9UeWQ0bEZ0d0VQU1Y2b2QzQnh2YzVaSTIzVV9pTUJOUy1BM1puZ2N0SUc0SzltUnotUU4ySDlfR2psMm0tSA?oc=5) <sub>Simply Wall St</sub>
- 📰 2026-11-06 [Mois Navon: On Mobileye’s Success, AI Ethics, and the $15.3 Billion Intel Deal](https://news.google.com/rss/articles/CBMivwFBVV95cUxNZWE4YU1udlFHX2tSMHFJWERQME5TMk9FaVBxRUZjbm81MlVjZDU2V25FRS1DVFdWV3lHZ3IzaUJLaHBsZnJHN3pPLUt0QlhzYU5NaXpkZ3ZDZGVEdGJNb2ZjRFV4MUk1bXllek45NVR3NHFITFY5RUZESE1qUWZmbjJsYnE0eVFtWXRYYU1iM2VwTmZoanZPT0doUUxyY2ZpeDAwLXRzTENQRzJKZXJYNDNheVcySGRRQnlDaURHbw?oc=5) <sub>UA.NEWS</sub>
- 📰 2026-11-03 [Elon Musk: Teslas will soon be able to drive themselves coast to coast](https://news.google.com/rss/articles/CBMic0FVX3lxTFA3WXZ0NzdKSEFxdnJJWWdIZ08zMThvN2h1UllLc3p6RlJrTHBfNTFMcmVKYmNMZGdzWG1uY2NqSzNmUXdGVWFsdzM4TXdoaGNRWFNYQWpYcHZ1c0JEdzQ4VnM4YTczYlNWWE9wYnFGRnFLZzQ?oc=5) <sub>Mashable</sub>

</details>

<details><summary><b>Aurora</b> (29)</summary>

- 📰 2026-11-09 [Opinion \| Truckers hate these jobs. Let driverless trucks take them.](https://news.google.com/rss/articles/CBMipgFBVV95cUxQM0k0WWkzYlVsOFdpbFNSZmJfenVKeV94ZkFCOHZRZmZhM1JfUlpaVTUwcnVFNDJkMjJBWlhIb0lhdzJsa3Nodnh3N19tVzlRcXFJZFN0ZU5MZmlnV2hYZmZ4RV9BZmVyRE01ZVhydjg0VlZBUkp0NElEM3BGTEhuNXpNa3F3UC1rRkg1R3czdWZQQWFNa2VoWXkzbkhiOFl5RGxUMUt3?oc=5) <sub>The Washington Post</sub>
- 📰 2026-11-09 [Clark: What fleets should know about autonomous trucking](https://news.google.com/rss/articles/CBMi1wFBVV95cUxQRldXemJMcGs5TnpOalV4d1g2aEdDaTN3aGRZS1pQSHJzbFRBY0FOaTV3VHlCMTJZQ1NDZmo3UFpaRjhtSFNKZk9uYk5VN1VUSDlDamFhY19vWktyd2pRVmtuN3lUV2RLRGZINWpLQ05wQXVIZzdGd2JrRGk2NEl3aHNlNGJMWFY5RzNiR25NRkQ1NmVCR2dPNXhDVDVNQTVTeU4tOGlqT2FERXMzdHNudzVNRmd2S3hiNWliRGd6QVJERjB5NWh3dzZKZ3ZKdjdLTTc5alZTUQ?oc=5) <sub>FleetOwner</sub>
- 📰 2026-11-09 [Premium Comment Driverless trucking’s carriers start to sign – next test: which signatures bind](https://news.google.com/rss/articles/CBMiogFBVV95cUxPRnZJU2hDWWxLQkZYeTNKUUxtem9acEsxd1ljZlBFV2dCV1l5NHY5bFBVeFlwNXJHTVlqQWpicGk5c3UwSDVxTUF2ZVhxZGRQSzNsQTdNLWJEWC1KWFFpcG43MDNvX2FaMTFycXRzSmJnMW4zSlA2eWV2YWJqU1FWeTZoWk1fTTA1a21YdDdFblpWUHcyNVdIeUpsRXZjLWhuSnc?oc=5) <sub>The Loadstar</sub>
- 📰 2026-11-08 [Nuvation Bio And 2 Penny Stocks To Watch](https://news.google.com/rss/articles/CBMiygFBVV95cUxPQTRqN0NwOFFPV1dBeUtGSXp6RGtfLS1MQ0l2cWlrd0tDdi0xME1ObzR0ZndYbmUzeERRNExDS3k5WmJVcmNkRnhTMUkxWHJQYU5OSWhMczRsdmZZZVVwZlhocmdFYTlTcWN6NExmaFFPMXJzNnN1ZWVaMnFYb0VnRmdhS0Mta1ktQW0yRXRPUmJIVUtYTjg0elduS1RaMFlpamtqRkZ3YkxWRlZmZHdhRFJrQ1NGYkViYWhrQ2lPLVJIMGYtU0dkR0930gHKAUFVX3lxTE9BNGo3Q3A4UU9XV0F5S0ZJenpEa18tLUxDSXZxaWt3S0N2LTEwTU5vNHRmd1huZTN4RFE0TENLeTlaYlVyY2RGeFMxSTFYclBhTk5JaExzNGx2ZlllVXBmWGhyZ0VhOVNxY3o0TGZoUU8xcnM2c3VlZVoycVhvRWdGZ2FLQy1rWS1BbTJFdE9SYkhVS1hOODR6V25LVFowWWlqa2pGRndiTFZGVmZkd2FEUmtDU0ZiRWJhaGtDaU8tUkgwZi1TR2RHT3c?oc=5) <sub>Simply Wall St</sub>
- 📰 2026-11-06 [Aurora Innovation delays driverless truck produ...](https://news.google.com/rss/articles/CBMipAFBVV95cUxQRklSWDhVZ2l3NXVOMmVHXzRyUURUYmVqVTBibE4zOXlLTEZmdS0zal8zRnF2WEhWdGhoZFJ5WVFZLWhSRE9HQmJmVGROandBODJLRWZEZkhuckpJblpjbFBzUmNlV3RRVmRvaFYzQW5vN2V2Z2ZUNmxnUnJadnI5UTgwbW5hMU1jZzJYY1VaYVhvSEtZYWlzb0VpUGhRZk9ScFItYw?oc=5) <sub>Pluang</sub>

</details>

<details><summary><b>Zoox</b> (37)</summary>

- 📰 2026-11-09 [Zoox Steers Into Las Vegas Grand Prix With Multi-Year Robotaxi Deal](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQMHdFVldVQzRFZFhHbUxiNFU2YkZyNkt6MmtwbHplWDc5OWtfRUQyUjRyaGdUdW55anBvM0JYclFyOFQ2clNmUUlCYmZKRnc1cVdNdXNaaDY0c0Nsa0xzRDNzMWg0azlMdkVMdDY5bUFXbWJFVUtIUTZtRHZNYUhsdG9veEd2T0dVY1oteXNoYVlNc251cXlBQ3NWZFFtVmRLLW5Eb01WcWRrNmc?oc=5) <sub>102.7 Coyote Country</sub>
- 📰 2026-11-09 [Robotaxi Service Expansion](https://news.google.com/rss/articles/CBMiqgFBVV95cUxOQ0Y0S1N2S1J1SjR0bHAzVVdGaGJsZF9LaE9VX2VpdDdoRnBfcHdpZlpRVEExWVBwMGZCei1KNF9OQ3V6WlBWR1FiNDBvSXNOWmlaaWp1UGtrZ2d5UEFISlR4NDBvQXpSMDU3ZTl1RWRSejREM0FGU1Byb2N2WjN6V0gtN3NoYmxnOWVBY29zdW9GMEpIWEhld0VqVEw3Ri1sc25rY0NOdW82d9IBqgFBVV95cUxOQ0Y0S1N2S1J1SjR0bHAzVVdGaGJsZF9LaE9VX2VpdDdoRnBfcHdpZlpRVEExWVBwMGZCei1KNF9OQ3V6WlBWR1FiNDBvSXNOWmlaaWp1UGtrZ2d5UEFISlR4NDBvQXpSMDU3ZTl1RWRSejREM0FGU1Byb2N2WjN6V0gtN3NoYmxnOWVBY29zdW9GMEpIWEhld0VqVEw3Ri1sc25rY0NOdW82dw?oc=5) <sub>USBE and Information Technology</sub>
- 📰 2026-11-09 [Vegas Fashion Week Returns for Second Year With Runway Shows Across Las Vegas](https://news.google.com/rss/articles/CBMirgFBVV95cUxPb1J1SVdXTUtIMEp4MVdsZXd0ZE9mZU5ObnNKVFFJaVhrV3VvUVdNdW9PSVR1NUIyVlB2M29tUV9WcDNYNTk3VkpwZ0NCQnFGQkptWFkxbkVPeFkwR0hzNjgxZ3gzODlLQVVrQlNBaGpSeDh1UENZYVpQczhUSUZtdUp3TlFCblItLUYyVzVZbGR3YXVkeWVvWW5XMEhDY0thenNvZkI1WDJSVUk3NFE?oc=5) <sub>96.3 KKLZ</sub>
- 📰 2026-11-09 [Uber robotaxi expansion: 2026–27 targets and plans](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPRHJUblQtU1dnWHFFT1VUdlhjS2pZZEwtcWd3NmkwQ1phaU0wR21YZV9CcTZkY05aU2w5QzJIYzZQS3VGczhEcG8ybTd5UEo0bEsyWUhZLUhMOWVQU19OeTJSNENNZFEzb3ExZ25wYzFxUGEtYk5wYUNzRHdRT202R0wyNHZ6N25yejJ3?oc=5) <sub>NeoTeo</sub>
- 📰 2026-11-09 [Hope Means Nevada Returns to UNLV With Hope in Action 5K Walk](https://news.google.com/rss/articles/CBMimAFBVV95cUxQZGV1R0Y3Skd0ajhWbmMtQW5YOEdpWUtsYjhkeU5BbTBfdWZ1UTVGSHBJcHI5R1E3djhHaGc4UDk5VTY4SlpreWhvVWNmX0FXNndCeUczcjRrTExlYmc0eXNvRGQ3Qm9mYk1ZekRJUlZDMHlhT3kzYkJQTVdCcWNaQjRtRUROUHFNSzBOSXdUUXBnLXgtSXY3WQ?oc=5) <sub>96.3 KKLZ</sub>

</details>

<details><summary><b>Motional</b> (15)</summary>

- 📰 2026-11-09 [Nvidia Hardware to Run Kakao Mobility’s Own Level 4 Driving AI in Kia Vans](https://news.google.com/rss/articles/CBMiqwFBVV95cUxOdnhiQkNMYk5WWWNtak9OVFdvdjdJYzNQT3htNzc4MjFiemlCRVpSaHJQUHlqd1N3NUVQZ0pESjBHWXZpR3RkdDVqNDhTc3RJd0l1ak96OXRFeEF6T0o4bWdnNHA5dDZjTEhWQjJobWtmY1JXMXItQUdtdUwyeE95WFR2Znk1dGI2eXk4N1hXMmxvVHFxU3J6R1l3Z2hpNEdmSDBTZjl1M05HaGc?oc=5) <sub>Electric Vehicles</sub>
- 📰 2026-11-09 [Jony Ive Shows The Real Process Behind the Ferrari Luce｜Cleo Abram: HUGE Conversations](https://news.google.com/rss/articles/CBMiX0FVX3lxTE42VWFqQXo4YTIwQjRGbk4xZjZ4Rko5MkNmMFZ2OHlEZGZpaURkM2NhLVRNSG02M0NsS3RIaTJ2WHlEVDRKY2U1bFdjZ0NLWjZJblhHVzhuQzdXYzZTeHZz?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-11-08 [Tesla Robotaxi Orlando Field Report｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5ObkNyUS1ncHVCU28ybkRSblpObzVkeGRqaEg3dTRRcWIwTFdCV0tyRnNMeEw3Wk1oRVhZM1g0OW8xSkdxYU5rM2NfLWo0SV9heXRKSnZRd3Nwc3FnRkxZ?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-11-08 [Waymo Just Blew Up Uber’s Robotaxi Growth Story｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBXdmg5SVRYNVVVT0d3Y3o1S1drU3RrT0szWGpoSHZMZzFlb09ZVVNJS2xvY3VDUWoyVW5hZXppeHN5OTRwTTFwZW1BZkdqdy1jX2U0ZUotR1dYaHFCaXhr?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-11-06 [Uber CEO Dara Khosrowshahi Ramps Up Robotaxi Deals as Freight Revenue Jumps](https://news.google.com/rss/articles/CBMijwFBVV95cUxPaEVFaUVkcmt0OXh0V04yS3pYeW9ZVXg2aUxTV0g3TzhoQUZPTVQ5WmFSUlVFR0ctMkdoc0dlcXpyTXdTdVJoTjBhRmxrVE9pdzUzVkN6WGE5b2RMSVhBblhBU3lHcjZvY3lVVmZPWExpbWRESTZ1c1dTZlVOSEczRzdVX3dIMmV2ZkcwSzZ3QQ?oc=5) <sub>Observer</sub>

</details>

<details><summary><b>comma.ai</b> (4)</summary>

- 📰 2026-11-06 [Canadian YouTuber Linus Tech Tips Tests Tesla FSD](https://news.google.com/rss/articles/CBMiggFBVV95cUxNZVZaT1Q4X0NlakJzTnFkTGdqTmFPM3pDbFZPUnBYVVNrVzFxMlpZQ3VaTEJFUmJrNVpjMmZ5RVphUDE4WURNT0x4NkhnN01LdTdzSEVnS2NUNkROams2cnNzNkpnalhWcDVuckhETUtxaDZrSHNXTXhKYUlpN2dPTlZn?oc=5) <sub>Drive Tesla Canada</sub>
- 📰 2026-10-29 [We Upgrade Our comma three to a comma four: Is It Worth It?](https://news.google.com/rss/articles/CBMimwFBVV95cUxOVkgtNU9hLXVYM0U2VjNpVldsNFFoQm53SjJGcU1CcnNMWXY5YzFYdVhoYlNZdG5vX21Va2h4b2RLYTNEUTBLdUFhMXd5eTVjLXBSTHE5bFN6elNqa1diTThPQ0Z0Mlo4SldDTzQ4eGxEWl9NTjNKcUNGQmhLeGRSMUxOSElpMkVNOTN4QWhMV0hPRFFJV3cyeVNLSQ?oc=5) <sub>Transport Evolved</sub>
- 📰 2026-10-29 [Aftermarket Self-Driving Devices Face Federal Investigation Following Five Crashes, Three Deaths](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPUG8ycGN4Tl96dk4xZk1yTEJrVkpvVGNsX2JnbWJoeXlzS1ZsVDlEYWk0SnFQQTZXQXpfN21BU20wR1FmR1lsUFpoeHdzU1BUaGdheTZ3LUFkVnpaOHhyWUU0YU1yWERQYmI2TDRnd1VpbTM3Ui1yWFdQVzZIRHVrUEhZUFBKcGpM?oc=5) <sub>AOL.com</sub>
- 📰 2026-10-29 [A $1,000 Device Enables Hands-Free Driving. But Fatal Crashes Have Prompted Scrutiny.](https://news.google.com/rss/articles/CBMixAFBVV95cUxObnRHUXNNS2wxNVFWeHVLdm9qYmZ1bnpaUVN2VWJ1eHZhbFRiWGxoVWxaSjNuNzNKQXZ0RV80dVRnckFGc003eXZJeW5ZWkhUakpsdk9sQ0lnQUZZeVNGekRzYmhvR2RrU1Ric29JeUFmQzNNdEE5NEtZLUgyS2hmQ1hwYWlMdFNDRHNZQVB6dHNqUjIyaXpRMFd2c0YxN0c3Vk9yZF9kR255QmtTUlRiaEtYbDY1dHVZQm9ReHY5WUdMSzJQ?oc=5) <sub>WSJ</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
