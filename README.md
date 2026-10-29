# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-10-29 · 1,308 papers tracked · 46 curated.

**Selection rule.** A paper is listed only if it (1) is primarily about autonomous driving,
(2) has public code, and (3) shows at least one strong signal: accepted at a top venue
(CVPR / ICCV / ECCV / NeurIPS / ICLR / ICML / CoRL / RSS / TPAMI, or ICRA / IROS / AAAI / RA-L),
≥200 GitHub stars, ≥3 citations / month, or a well-known lab with traction. Papers are then ranked by a
composite score (venue, stars, citation velocity, LLM rubric for novelty / rigor / impact, SOTA claims)
with a per-topic cap. See [`scripts/rank.py`](scripts/rank.py).

📅 [Daily digests](daily/) · 🗓️ [Weekly digests](weekly/) · 📦 [Raw data](data/)

## Contents

- [VLA / VLM for Driving](#vla--vlm-for-driving) (11)
- [World Models & Generative Simulation](#world-models--generative-simulation) (6)
- [End-to-End Driving & Planning](#end-to-end-driving--planning) (10)
- [3DGS / NeRF Reconstruction & Sensor Sim](#3dgs--nerf-reconstruction--sensor-sim) (5)
- [Perception: BEV, Occupancy, 3D Detection, Mapping](#perception-bev-occupancy-3d-detection-mapping) (8)
- [Motion Prediction & Behavior Modeling](#motion-prediction--behavior-modeling) (1)
- [Datasets & Benchmarks](#datasets--benchmarks) (2)
- [Safety, Robustness & Evaluation](#safety-robustness--evaluation) (3)
- [Industry Tracker](#-industry-tracker)

## VLA / VLM for Driving

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Teaching Vision-Language-Action Models What to See and Where to Look](https://arxiv.org/abs/2607.01658)<br><sub>Yuguang Yang, Canyu Chen, Zhewen Tan et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 35](https://github.com/ShivaTeam/DriveTeach-VLA) | Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving |
| [DeepSight: Long-Horizon World Modeling via Latent States Prediction for End-to-End Autonomous Driving](https://arxiv.org/abs/2605.10564)<br><sub>Lingjun Zhang, Changjie Wu, Linzhe Shi et al.</sub> | ICML 2026<br>2026-05<br>📑 2 | [⭐ 31](https://github.com/hotdogcheesewhite/DeepSight) | End-to-end autonomous driving systems are increasingly integrating Vision-Language Model (VLM) architectures, incorporating text reasoning or visual reasoning to enhance the robustness and accuracy of driving decisions |
| [SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving](https://arxiv.org/abs/2610.20609)<br><sub>Shaoyuan Xie, Zihan Zhang, Jingxuan Wang et al.</sub> | CoRL 2026<br>2026-10 | [⭐ 30](https://github.com/ASGuard-UCI/safedrive-vla) | Vision-Language-Action (VLA) models are gaining attention in autonomous driving, inheriting commonsense priors from large language models (LLMs) and widening the navigation interface from a fixed command set to free-form… |
| [Scene-Adaptive VLA: Efficient Autonomous Driving via Dynamic Layer Routing](https://arxiv.org/abs/2610.24590)<br><sub>Yujia Yang, Quan Yuan, Jiawei Fan et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 2](https://github.com/yang-luvu/Scene-Adaptive-VLA) | Vision-Language-Action (VLA) models offer a promising paradigm for autonomous driving |
| [CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving](https://arxiv.org/abs/2607.04179)<br><sub>Zhaohong Liu, Hao Ye, Xianlin Zhang et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 1](https://github.com/MICLAB-BUPT/CritiqueDriveVLM) | End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving |
| [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)<br><sub>Nan Yang, Zhanwen Liu, Linfeng Zhang et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 11](https://github.com/Zizzzzzzz/MVPruner) | Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings |
| [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)<br><sub>Yuan Gao, Wenting Miao, Mattia Piccinini et al.</sub> | IROS<br>2026-07<br>📑 1 | [⭐ 29](https://github.com/TUM-AVS/Chat2scenic) | Validating autonomous driving systems requires diverse, regulation-compliant test scenarios |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 12 | [⭐ 531](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
| [GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives](https://arxiv.org/abs/2609.39601)<br><sub>Qize Yu, Lianrui Fan, Boyu Chen et al.</sub> | arXiv<br>2026-09<br>📑 2 | [⭐ 232](https://github.com/groundingpi/GroundingPI) | Precise grounding matters |
| [GRAVA: Grounded Reasoning-to-Action Representation and Learning for Autonomous Driving](https://arxiv.org/abs/2609.15169)<br><sub>Xiao Liu, Haoyu Li, Jianghao Leng et al.</sub> | arXiv<br>2026-09 | [⭐ 414](https://github.com/AhernResearch/grava) | Driving vision-language-action (VLA) models increasingly reason before acting, but their intermediate reasoning is often weakly grounded in physical scene evidence and loosely connected to executable behavior |
| [Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air](https://arxiv.org/abs/2605.31066)<br><sub>Tianle Zeng, Yanci Wen, Xueang Yu et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 1,123](https://github.com/louiszengCN/CarlaAir) | Recent aerial vision-language-action (VLA) models show promising single-UAV capabilities, such as tracking moving objects and navigating to language-specified landmarks |

## World Models & Generative Simulation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [HERMES++: Toward a Unified Driving World Model for 3D Scene Understanding and Generation](https://arxiv.org/abs/2604.28196)<br><sub>Xin Zhou, Dingkang Liang, Xiwu Chen et al.</sub> | ICCV 2025<br>2026-04<br>📑 5 | [⭐ 72](https://github.com/H-EmbodVis/HERMESV2) | Driving world models serve as a pivotal technology for autonomous driving by simulating environmental dynamics |
| [FrozenDrive: Zero-Shot Text-Guided Driving Scene Generation and Data Augmentation with Parameter-Free Frozen Diffusion Model](https://arxiv.org/abs/2606.20110)<br><sub>Yuhwan Jeong, Hyeonseong Kim, Daehyun We et al.</sub> | ECCV 2026<br>2026-06<br>📑 1 | [⭐ 10](https://github.com/daehyunwe/FrozenDrive) | Synthetic data for autonomous driving is surging, powered by diffusion models that promise scalable scene generation |
| [MESSENGER: Memory-Enhanced Sequential Scene Flow Estimation via Autoregressive Next-Frame Forecasting](https://arxiv.org/abs/2610.10759)<br><sub>Jiuming Liu, Jianing Li, Mengmeng Liu et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 0](https://github.com/liujiuming123/Messenger) | Scene flow can capture low-level 3D motion displacements in dynamic scenarios |
| [ASTAD: Asymmetric Style Transfer for Synthetic-to-Real Adaptation in Autonomous Driving](https://arxiv.org/abs/2606.29286)<br><sub>Dingyi Yao, Xinqi Zhang, Lihui Peng et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 2](https://github.com/Dingyi-Yao/ASTAD) | Synthetic data mitigates the data scarcity problem in autonomous driving perception |
| [Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends](https://arxiv.org/abs/2606.01164)<br><sub>Jiuming Liu, Chaojun Ni, Mengmeng Liu et al.</sub> | arXiv<br>2026-06<br>📑 9 | [⭐ 247](https://github.com/liujiuming123/Awesome-Interactive-World-Model) | With rapid development of large language models and diffusion-based content generation, world modeling has attracted increasing research attention, benefiting various downstream domains such as game engines, embodied AI,… |
| [Is Your Driving World Model an All-Around Player?](https://arxiv.org/abs/2605.10858)<br><sub>Lingdong Kong, Ao Liang, Tianyi Yan et al.</sub> | arXiv<br>2026-05<br>📑 6 | [⭐ 257](https://github.com/worldbench/WorldLens) | Today's driving world models can generate remarkably realistic dash-cam videos, yet no single model excels universally |

## End-to-End Driving & Planning

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](https://arxiv.org/abs/2609.26792)<br><sub>Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.</sub> | CoRL 2026<br>2026-09<br>📑 1 | [⭐ 14](https://github.com/VAIL-UCLA/DreamStream) | Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions |
| [DriveMLP: When Training Strategy Outperforms Model Complexity in Autonomous Driving](https://arxiv.org/abs/2610.29676)<br><sub>Alessandro Canevaro, Julian Schmidt, Hang Yu et al.</sub> | CoRL<br>2026-10 | [⭐ 5](https://github.com/alessandro-canevaro/DriveMLP) | Learning motion planning policies that remain reliable under closed-loop execution is a central challenge in Autonomous Driving (AD) |
| [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)<br><sub>Shen Zheng, Anurag Ghosh, Gaurav Parmar et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 32](https://github.com/ShenZheng2000/WarpI2I) | Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs) |
| [G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance](https://arxiv.org/abs/2606.26017)<br><sub>Hang Yu, Ye Jin, Alessandro Canevaro et al.</sub> | IROS 2026<br>2026-06<br>📑 5 | [⭐ 7](https://github.com/HangYuu/G2DP) | In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 17 | [⭐ 353](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
| [SimWAM: A Simple World Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.07468)<br><sub>Zongchuang Zhao, Xin Zhou, Tianyang Xu et al.</sub> | arXiv<br>2026-08<br>📑 9 | [⭐ 201](https://github.com/H-EmbodVis/SimWAM) | In autonomous driving, World-Action Models (WAMs) have improved end-to-end planning by transferring video dynamics priors to action prediction, but many still couple planning with future-video generation at inference, in… |
| [Latent-Centroid Steering: Single-Pass Classifier-Free Guidance for Command-Aligned Autonomous Driving](https://arxiv.org/abs/2608.00237)<br><sub>Meibo Hu, Jiamian Wang, Pichao Wang et al.</sub> | IROS 2026<br>2026-08 | [⭐ 2](https://github.com/codingmlinprocess/LCS) | Vision-language models (VLMs) have recently emerged as a promising paradigm for end-to-end autonomous driving, enabling agents to map multimodal inputs and high-level navigation instructions directly to executable trajec… |
| [HEAT: Heterogeneous End-to-End Autonomous Driving via Trajectory-Guided World Models](https://arxiv.org/abs/2605.19631)<br><sub>Hoonhee Cho, Giwon Lee, Jae-Young Kang et al.</sub> | RA-L 2026<br>2026-05<br>📑 2 | [⭐ 0](https://github.com/heat2026/heat2026.github.io) | End-to-end autonomous driving has emerged as a compelling alternative to traditional modular pipelines by directly mapping raw sensor data to driving actions |
| [STAGE: STyle-controllable Action GEneration for personalized autonomous driving](https://arxiv.org/abs/2607.29517)<br><sub>Zihao Liu, Xing Liu, Yizhai Zhang et al.</sub> | RA-L<br>2026-07<br>📑 1 | [⭐ 6](https://github.com/CarlDegio/STAGE) | Driving style refers to the behavioral preferences that drivers maintain during driving, shaped by their diverse experiences, habits, and needs, and is typically reflected in varying levels of aggressiveness |
| [A Survey on End-to-End Autonomous Driving Training from the Perspectives of Data, Strategy, and Platform](https://arxiv.org/abs/2610.00926)<br><sub>Chengkai Xu, Yiming Cui, Jiaqi Liu et al.</sub> | arXiv<br>2026-10<br>📑 5 | [⭐ 109](https://github.com/Jiaaqiliu/Awesome-Training-Ecosystem-for-E2E-AD) | Autonomous driving is a cornerstone technology for the future of intelligent transportation, where end-to-end learning has emerged as a transformative paradigm that directly maps multimodal sensory inputs to driving acti… |

## 3DGS / NeRF Reconstruction & Sensor Sim

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DriveWeaver: Point-Conditioned Video Inpainting for Controllable Vehicle Insertion in Autonomous Driving Simulation](https://arxiv.org/abs/2606.31918)<br><sub>Junzhe Jiang, Zipei Ma, Zijie Pan et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 17](https://github.com/LogosIntelligenceLab/DriveWeaver) | A pivotal step in autonomous driving simulation involves inserting foreground vehicles with predefined trajectories into simulated scenes |
| [MCSplat: Multi-View Photometric and Geometric Consistent Feed-Forward Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2610.25345)<br><sub>Yifei Wang, Wei Tian, Wenhua Bao et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 10](https://github.com/yfwang0824/MCSplat) | Driving-scene reconstruction via feed-forward Gaussian splatting from sparse multi-view images remains challenging due to two factors |
| [Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796)<br><sub>Leshu Li, Jie Peng, Yang Zhao</sub> | ICRA<br>2026-06 | [⭐ 15](https://github.com/UMN-ZhaoLab/Pocket-SLAM) | 3D Gaussian Splatting (3DGS) has garnered significant attention in Simultaneous Localization and Mapping (SLAM) due to its advances in capturing fine-grained geometry features and synthesizing novel views |
| [NIDAR: NIR-Guided Intrinsic Decomposition for Scalable Scene-Agnostic LiDAR Intensity Reconstruction](https://arxiv.org/abs/2609.36878)<br><sub>Junjie Zhang, Jie Yin, Kefei Qian et al.</sub> | IROS 2026<br>2026-09 | [⭐ 22](https://github.com/Zjj587/NIDAR) | LiDAR return intensity provides complementary surface-response cues for robotic perception and state estimation, yet many simulation pipelines omit it or reproduce it using reconstruction methods that require real intens… |
| [MM-TRELLIS: Point-Cloud Guided Multi-Modal 3D Vehicle Generation in Autonomous Driving](https://arxiv.org/abs/2606.24301)<br><sub>Hongli Xiao, Youjian Zhang, Yucai Bai et al.</sub> | ICRA 2026<br>2026-06 | [⭐ 10](https://github.com/HongliXiao/MM-TRELLIS) | Recovering realistic 3D vehicle models from autonomous driving scenes is crucial for synthesizing training data and building simulation environment |

## Perception: BEV, Occupancy, 3D Detection, Mapping

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Deformable Gaussian Occupancy: Decoupling Rigid and Nonrigid Motion with Factorized Distillation](https://arxiv.org/abs/2605.28587)<br><sub>Yang Gao, Wuyang Li, Po-Chien Luan et al.</sub> | CVPR 2026<br>2026-05<br>📑 2 | [⭐ 22](https://github.com/vita-epfl/DeGO) | Understanding dynamic 3D environments is essential for safe autonomous driving, particularly when reasoning about human-centric, nonrigid agents |
| [FreeOcc: Training-Free Embodied Open-Vocabulary Occupancy Prediction](https://arxiv.org/abs/2604.28115)<br><sub>Zeyu Jiang, Changqing Zhou, Xingxing Zuo et al.</sub> | RSS<br>2026-04<br>📑 8 | [⭐ 143](https://github.com/the-masses/FreeOcc) | Existing learning-based occupancy prediction methods rely on large-scale 3D annotations and generalize poorly across environments |
| [Horizon3D: Sparse Radar-Camera Fusion for Long-Range 3D Perception in Autonomous Driving](https://arxiv.org/abs/2606.31096)<br><sub>Geonho Bang, Geunju Baek, Dongyoung Lee et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 25](https://github.com/geonhobang/Horizon3D) | Long-range 3D object detection is critical for safe autonomous driving at highway speeds, yet existing radar-camera fusion methods remain limited at extended ranges |
| [Explainability-Aware Frustum Attack: Exposing Structural Vulnerabilities in LiDAR-Based 3D Object Detectors](https://arxiv.org/abs/2606.29963)<br><sub>Chengzeng You, Binbin Xu, Soteris Demetriou</sub> | ECCV<br>2026-06 | [⭐ 2](https://github.com/SecMindLab/Saliency_LiDAR) | The structural vulnerabilities of point cloud-based 3D object detectors remain poorly understood |
| [PointLAM: Local Attentive Mamba for Efficient Point-based 3D Object Detection](https://arxiv.org/abs/2609.21780)<br><sub>Xuanming Shang, Weijia Zhang, Chao Ma</sub> | ECCV 2026<br>2026-09 | [⭐ 5](https://github.com/PointLAM/PointLAM) | 3D object detection from LiDAR point clouds faces a fundamental dilemma: voxel-based methods achieve efficiency at the cost of geometric quantization, while point-based methods preserve fidelity but suffer from prohibiti… |
| [UniD-Shift: Towards Unified Semantic Segmentation via Interpretable Share-Private Multimodal Decomposition](https://arxiv.org/abs/2605.07356)<br><sub>Shuai Zhang, Zhecheng Shi, Zhuxiao Li et al.</sub> | CVPR 2026<br>2026-05 | [⭐ 5](https://github.com/shuaizhang69/UniD-Shift) | Semantic segmentation of large-scale 3D point clouds is crucial for applications such as autonomous driving and urban digital twins |
| [Vernata: Self-Supervised Learning of LiDAR Point Representations](https://arxiv.org/abs/2608.06919)<br><sub>Oliver Lemke, Alexander Liniger, Abel Gawel et al.</sub> | IROS 2026<br>2026-08 | [⭐ 22](https://github.com/rai-opensource/vernata) | LiDAR serves as a primary sensing modality for robots operating in outdoor environments |
| [Towards Compact Autonomous Driving Perception with Balanced Learning and Multi-sensor Fusion](https://arxiv.org/abs/2606.02979)<br><sub>Oskar Natan, Jun Miura</sub> | arXiv<br>2026-06<br>📑 45 | [⭐ 9](https://github.com/oskarnatan/compact-perception) | We present a novel compact deep multi-task learning model to handle various autonomous driving perception tasks in one forward pass |

## Motion Prediction & Behavior Modeling

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Flow-ERD: Agent-type Aware Flow Matching With Entropy-Regularized Distillation for Diverse Traffic Simulation](https://arxiv.org/abs/2607.06957)<br><sub>Seulbin Hwang, Kiyoung Om, Dae Jung Kim et al.</sub> | RA-L<br>2026-07 | [⭐ 0](https://github.com/seulbinHwang/flow-erd-project-page) | Realistic and diverse traffic simulation is essential to autonomous driving development |

## Datasets & Benchmarks

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Towards All-Day Perception for Off-Road Driving: A Large-Scale Multispectral Dataset and Comprehensive Benchmark](https://arxiv.org/abs/2604.27499)<br><sub>Shuo Wang, Jilin Mei, Wenfei Guan et al.</sub> | RA-L 2026<br>2026-04 | [⭐ 6](https://github.com/wsnbws/IRON) | Off-road nighttime autonomous driving suffers from unreliable visible-light perception, making infrared modality crucial for accurate freespace detection |
| [123D: Unifying Multi-Modal Autonomous Driving Data at Scale](https://arxiv.org/abs/2605.08084)<br><sub>Daniel Dauner, Valentin Charraut, Bastian Berle et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 405](https://github.com/kesai-labs/py123d) | The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics |

## Safety, Robustness & Evaluation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [CCFM: Collision-Constrained Flow Matching for Safety-Critical Scenario Generation](https://arxiv.org/abs/2607.04451)<br><sub>Ke Li, Kaidi Liang, Yuxin Ding et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 3](https://github.com/KELISBU/CCFM) | Evaluation of autonomous vehicle (AV) planners in safety-critical closed-loop simulation is essential for real-world deployment |
| [Lipschitz Optimization for Formal Verification of Homographies](https://arxiv.org/abs/2605.23203)<br><sub>Jean-Guillaume Durand, Panagiotis Kouvaros, Maxime Gariel et al.</sub> | CVPR 2026<br>2026-05 | [⭐ 2](https://github.com/jeangud/homography-verification) | The adoption of vision neural networks in regulated industries requires formal robustness guarantees, especially in safety-critical domains such as healthcare, autonomous vehicles, and aerospace |
| [CADET: A Modular Platform for Evaluating Distributed Cooperative Autonomy in Connected Autonomous Vehicles](https://arxiv.org/abs/2606.04072)<br><sub>Pragya Sharma, Brian Wang, Mani Srivastava</sub> | ICRA 2026<br>2026-06<br>📑 1 | [⭐ 0](https://github.com/nesl/cadet) | Deep learning models are increasingly central to autonomous vehicle (AV) pipelines, yet their integration has traditionally followed a monolithic design where perception, planning, and control execute on a single onboard… |

## 🏢 Industry Tracker

Latest 14 days of news, official blog posts and new open-source repos from tracked companies. Full daily feed in [`daily/`](daily/).

<details><summary><b>Waymo</b> (259)</summary>

- 📝 2026-10-16 [Hello Toronto! Waymo is En Route](https://waymo.com/blog/2026/10/waymo-in-toronto) <sub>official blog</sub>
- 📰 2026-10-29 [Waymo Robotaxi Privacy Risks: Could Chinese-Built Vehicles Spy on Riders?](https://news.google.com/rss/articles/CBMisAFBVV95cUxPby1BZWRYeGR4UVgxc2NxMVRnN0xyc0t3Zk5nZEZSbWxFNEV0V1ZhMkh1eTd6em5CR2FMNkFQdVd2akZTaTJLV1RQcnBpYVAtMmNuVzZadWp6VzNIYkF6TllaVWtVOUVNRDN2cjVLVjM0VVI3QmR0czB6WkFDb1ZneVI0cVNGamlTV3JtS2JOWWpHNkxWMUR4SExYbTUtbzVNc01EXzhOTWlWaXdlX2dSdg?oc=5) <sub>AZ Family</sub>
- 📰 2026-10-29 [Waymo expands driverless ride service into South Bay](https://news.google.com/rss/articles/CBMijwFBVV95cUxOQmVOekZiVjlNNlVwWE8zR0hIRDdEZ3NCWHRpd0dzbEpPUVBlQ2pNVUJRLVNXWHlTaURTQ0w0QTVXNE5pM2lwWkJhblNQZTdQalFiM3hWckFIYjJzbGlEVGdhMXVXd082MTF0VndOanlDUmRwdGZDLXR3MFVPdEViVUhZclRCX0lnaDF2S2otWdIBlwFBVV95cUxPWVlKMDlFSFBBT3M3ZDNvRHJ3LWU0ZnpKM0twb2Y0Q0M2ZDlsVkRPWDBNUTkyaVNSQkxwTmlzdDVGSU1sd1dUVTByaXVvWXBKQ2lNYjdrMG5Xa3hLTlBPTEhESm1JRmlMWkJxLVliRmhtTkhuejRmR2pnV0dXWngyS2FxUTZrbG93NXJwWkZJbTNtTjdEOGtj?oc=5) <sub>NBC Los Angeles</sub>
- 📰 2026-10-29 [AI Election Threats, Waymo Robotaxi Privacy Risks & Web Security Flaws \| Generation AI](https://news.google.com/rss/articles/CBMiwgFBVV95cUxPMWtOQmNoTV9iR20xVmFyajhrdUZFZi16WHR3SGJwZVVMaTlob3c4SkN2R28yRWZ2b2FzREs4bEZ3ZmlPU1VPcUh5MkliN1g4STR0bkVsMldvLWhrVm1QbkNFVlE4dThHSFE5QTc1X0tFdjBlUTZvckFUcTNtRExWWncyYk02RE5JbXZfRHdiWW42Z2RTekY3djVKZzBwVDhxb3E1Wm9PX08xM2MzSnZ0ZlRoeGlHWTN2cmxKRmJLTjRSUQ?oc=5) <sub>AZ Family</sub>
- 📰 2026-10-28 [Waymo vs Tesla Robotaxi [2026]: 7x Gap, Waymo Wins](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPR0d1dUh6eEJFLWJSYzJMY0UyZkhOdGhjaGJLdWFVYWRsYWdZOGpaYmZDZUJLMXhtdVNoTF9SWDVfSUptRVZIMDBPWFdTU0twOV9oNDdObHdpTHBfN3Y0MDdKWTEwekd1ZHVuWG1NeDQzNDBhei1Vd3VQRm9MLWNEZDVvbFdLaFNt?oc=5) <sub>tech-insider.org</sub>

</details>

<details><summary><b>Tesla</b> (382)</summary>

- 📰 2026-10-29 [Tesla Wins Lawsuit in South Korea Over FSD Feature Delays](https://news.google.com/rss/articles/CBMirAFBVV95cUxNcDF4akhSeXBtYlhsWHo5MFNmT1BDblliU2cxMG1Tb0I5bW9MUndfY1ZHa1ZSNFhfanRiNlVuTEgwZmVpTHp3cjZ3NzVxS3ZYMnJMUS1rNlRpU2xER2tJZE9HVWRpRHE1XzE2cUhabG1pWXNaSDFJRmlxaDFFN0hpVjhqMkw0ZHNyWTFxd0dpbHR6ZGRpNXFPUHFPOWtITzdiLUd2NjJTTUlTdURG?oc=5) <sub>Bloomberg.com</sub>
- 📰 2026-10-29 [Tesla owners in South Korea lose legal battle over full self-driving promises](https://news.google.com/rss/articles/CBMiywFBVV95cUxNNlJ3YlVqeGZxazRLczlzcDU4TUlxRVhBNEFyWHVjVDF0dGt4clNHVHhvNnJnYVd0S2xleHVOeW0wTmwyaEJQOURZcGstNC1KMXVlSzM2TlNneWp1N2g4VTJnTUhUN3UzLVdpVVdxeXZkUWhIVDZ2dlQyMC1CM2doZEdLYnpqb2VaeFFVcHVZVDl1TkhPdGU4UUM2NVlicmZpRFMyWHlMQVA4Qlkxdm8yODZfbWZBNHpBSFVlVDdrYkJBamdWSWNMY1B3a9IBywFBVV95cUxOUkpEaXJCSmRzMExFTnpZYngzMG9VbEZFc3RMdkZEQ3Bfai1DNkoxUDcwTVlqcU5rZWpUY1ZYTmgyVExRZWttRWJENHA1UjRRdkJFQVhlRGE5eFFwU3VlZ2pqMUF3VXU5M2dqYTN0eVlCa0xDcVZFdGhuNklCTURRR0hMekZITUtjX3hsVzJ0UEFoSTBNVHNTQzVtd3d1aHRJMFBiRTN2TTdOcW9DTjZJRWt6QkZsWUVuQVhZU1ZIcDFNMmpMcVlydkJJNA?oc=5) <sub>South China Morning Post</sub>
- 📰 2026-10-29 [Tesla FSD V14: 2x Fewer Interventions, No Data [2026]](https://news.google.com/rss/articles/CBMilgFBVV95cUxPbVVVMWdNTlFCWHNoVHhtQnpRdmpycnFmWUJzWXdjdjVzeEs1UlFnZ1hLb0JwdGthNFBiUGFBWDhqbGFwNUNXcDlwMTl2TUh0YkdTOTRjaFc5REowd2FTZmVsN0ltcl9YUGtyZjdBREtOTTVqdnhaaExGX2Y3dU8wM1YyZkJUbUNFeWVWODBsUUVpams1THc?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-10-29 [Tesla FSD Korea Lawsuit: 98 Owners, No Ruling [2026]](https://news.google.com/rss/articles/CBMiigFBVV95cUxPTW5wRENObzBoU1ViMmVpeXh2clRseVRnMmVsVUx6TFhEaE44eEw4bUs3UW00ZXB6T2tpNzJVZ0oteFV3NEJWQkUxRk5FeE1uMlFyUjlycTdTUlNWNld3SDBhdnprQk9iWnRBT3hnQm5ERjdBXzNFLWplTnU4TFozdDZVRWJURENQZGc?oc=5) <sub>shattered.io</sub>
- 📰 2026-10-29 [Court Dismisses Tesla Owners' FSD Refund Lawsuit](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNRGMzb2QtdGdSXy1vMUdvd284bm5CanBLZWloUURiM1lKS3F3SDlnbEM4MDZiLVBoUU1seXdnN3M0ZWpFUzI2dERkQy03RUJzTG45X2t3aXdSWkM4SmZ2VHFrMXJZVy15djZiYWhpMlc5S1NDcGhQb08tS1dRNUd5aUlscGVtajd4?oc=5) <sub>조선일보</sub>

</details>

<details><summary><b>NVIDIA</b> (253)</summary>

- 💻 2026-10-20 [NVIDIA/flare-local-inference](https://github.com/NVIDIA/flare-local-inference) <sub>GitHub</sub>
- 📰 2026-10-28 [Google Cloud and NVIDIA unveil Vera Rubin AI systems and new sovereign cloud tools](https://news.google.com/rss/articles/CBMiwAFBVV95cUxPUkxHUjZ2YVpiSUFiQktPemJQdG1SOTBFNEpEWUtZM1JMcXdmQmkzNXJJbjZnM0RBNmQ3TnVlZms3SE5KWDlsenlnZFpSTEZnN1djRnRLLUFqbjAzeEZwTjdPcjlTNk9rRzR4Uy12RjdkdlV1RUV5amJ3SllqUm1fc1pOcmFhUnc1TVJBa1cyUXAzR2lnUExIbmVGdlNzX1duUFczTVQwYWVNalI5RlR2dVhkMGJVSS1wbnJSbVV4Rk8?oc=5) <sub>EdTech Innovation Hub</sub>
- 📰 2026-10-28 [Palit Says GALAX Is Going Nowhere and Continues To Operate As Usual, Though Recent GPU Shortages Drive Uncertaintity For Smaller Brands](https://news.google.com/rss/articles/CBMikwFBVV95cUxNSkNVNXE3MzJpM3c0MDIySGg5LXZRdnlqS25Gb1FmN2xPYVlYdGFDRGsycGtyNXFrcHRTMVdGT1FkdFdHNHBIWDB5QUFyallPZlVSZHZwMG9wcnJ4aEpteTY2N1ZSMk9kS1Npd245aVQwSTY1dVdLclZVV2lZZkRnc0NhLTliRGlJZ2RXdXlQYzJhSFXSAZMBQVVfeXFMTUpDVTVxNzMyaTN3NDAyMkhoOS12UXZ5aktuRm9RZjdsT2FZWHRhQ0RrMnBrcjVxa3B0UzFXRk9RZHRXRzRwSFgweUFBcmpZT2ZVUmR2cDBvcHJyeGhKbXk2NjdWUjJPZEtTaXduOWlUMEk2NXVXS3JWVVdpWWZEZ3NDYS05YkRpSWdkV3V5UGMyYUhV?oc=5) <sub>Wccftech</sub>
- 📰 2026-10-28 [Test-Driving NVIDIA's L2++ Hyperion AV Stack: A Mercedes CLA Ride Through Berlin](https://news.google.com/rss/articles/CBMijwFBVV95cUxPV0ZxSllLX0hnY09BZS1VXzdmSHdmMjBiRU9pbFBEZ2d3aWVjamQtTnpwak8wSC04Q09laDVra05lYVpPaW5GbmhKVkVtWWNmMExhU1BseEtIRGdJUUhzRnNxbG5mNTNwQkNFV0tHbWEwU3lqT0V4ODhndlFPS21hT3pWQ2QzOWtNVTZZM2NWcw?oc=5) <sub>Counterpoint Research</sub>
- 📰 2026-10-28 [NVIDIA GTX 750 Ti is resurrected with 8GB VRAM - and this ancient GPU even runs some modern games smoothly](https://news.google.com/rss/articles/CBMi6AFBVV95cUxOaXhmeHpHY0xMa29sb0JZWWVyalZYRXV5STJaak1RREVPS0ZiaEJjVHp1NE9QSDhlTHoxSTVINEVER3JzdWlmb3prdUlTaGxueEhaZGctR1pHZFZFTkZMam11U2M3ZFZ3UjBsSFVhaVhidTRiYklsemh6NDZQQWFCR0ZobFFzanlieEtqVElsZnR1WUEwWVZLRjFPb0FwSmlXMkJJV3U4SUJpdklndGlLYXdIa19XQWNFbGRRNWhpTlE5am9RMURkU2pqcVQyeXh4dWNyQVlpcUN6bXlfcGt1UHk2YXhJODk0?oc=5) <sub>TweakTown</sub>

</details>

<details><summary><b>Wayve</b> (63)</summary>

- 📰 2026-10-28 [Bolt and Stellantis to pilot autonomous vehicles in Paris](https://news.google.com/rss/articles/CBMitgFBVV95cUxNV0NnblE0czltekVYbk9iQ2xEQk1BZWMwZ2lQYThscnZnNWQxZTJGcHZKdFhQNHJtSG9vekpNZW50bm9zWUtWeTBGdUZEamd3ZzN4YXV4djFBbjJoaE50TUtQNWUwYTlKcGlnZjByS2pCLVE2RGFtR1hfM3M3Z2ZoaFZ3MzVwbF84MVhvQVVtbjRwRmFmMTFucWstcXpOcEhoTUFocDJ5SWo3eXhMQ3pUbHllX1IxZw?oc=5) <sub>Business Travel News Europe</sub>
- 📰 2026-10-28 [Top 10: AI Leaders in Europe](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1uRm1MZEtJM0RpZzFfTnNoNHJaYkdXRVFhekdtLUUyamQybC1oT3djc2RZMTYtOUpEWkNBNGVQNFdyZFFhNGQ5MkVBZWFZaFdldVc1WkZhR2Z4SGpUOFd4SjEtby1aaEk?oc=5) <sub>AI Magazine</sub>
- 📰 2026-10-28 [Nissan makes next Rogue its first software-defined vehicle as it chases Tesla, Chinese rivals](https://news.google.com/rss/articles/CBMigwFBVV95cUxOSW5oWFBKRzR3Rk0yU2hOZ19PeFJrbWRESDVoWWliMzYwdG12ZWYzeHJLSkw0b1ctckRWckVEZnktRFNNYWMwWHhHR3duNDl0ZUhrUEZJSVpwamI2Y19ZMkUzRTdGVmxDYzVSZEV5cTY4TWhsZ0lYeHNSamRvS3loWHlmWQ?oc=5) <sub>Automotive News</sub>
- 📰 2026-10-28 [Robotaxi Pickup Zones Trend: Curbside Handoffs](https://news.google.com/rss/articles/CBMia0FVX3lxTFBGWUtrUnlaX0R0SzlPcHJvM2dScUcxYVhYc0dMWlVjX1M4Q25fMHhZUmQycUlTSkEzd2VDTjNHaXdOaGs1SnY2WVpIQW0zMzYwZF9XemhJU3R2bHhRSlVMNHVkUEZ2ak14WkJ3?oc=5) <sub>Trend Hunter</sub>
- 📰 2026-10-27 [Wayve, Stellantis, NVIDIA Collaborate on Autonomous Vehicles in France](https://news.google.com/rss/articles/CBMi9AFBVV95cUxOX3MxQjhfdGRNclQ0QnNRenVlZ183TTZjRkt1ODdJNS1zUWJySUZxaVlBN1RwYmduZV9IUFNoeVJtRVc5UVNqeHgyM1FyVXA4RzNjV1dQTkE2QmNucVl3ZTRiUDRua01pV2VTNVN1X1hPbXdNeTFYTllIamVfUVRjOEpINWVUTk1JTkdVQjNBV2RPN19aZjdKMVMzTjd6aTR3Z0hZbXN0bzhzeGFGdGhoUGR4RzhldVBYNzBFV1BwYkN3RUdLc1pSbjRTQlZkU1Z0Z1pWRWJGYzZMZGRRTGUxTDZyczlmeWdrekZ6bnBrSEdJemZf?oc=5) <sub>Fuel Cells Works</sub>

</details>

<details><summary><b>Momenta</b> (109)</summary>

- 📰 2026-10-29 [智己 LS8 NEO 纯电，更大，更强，更领先！](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBSLThBU0k1OWVYbm01QXduaWJ1aGJHdzFxTkNzLTNjMUpVdm8yaFFXai1PNW91ZGJzcXJURTVrYV9MaE1IYklWMW10azBoc251QTJhMHlrakdIWU0?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-28 [新世代宝马i3即将上市，更新Momenta R7双脑协同](https://news.google.com/rss/articles/CBMiW0FVX3lxTFA3ckFjamZVbkVSN2VqcU04akxNYmhMRUtEQW1FYS1yZVNPMEQxUzhjdWRiQ2NPcTFUTDVWcmQxLXpJN05MckxMNlNqOVdiQjJ4TnZSXzN0U05DVFk?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-28 [700TOPS算力满血上车！东风风神L8+把高阶辅助驾驶打到15万级](https://news.google.com/rss/articles/CBMijAFBVV95cUxNQ2t1Wi1JNjZQclZWbWpISEZvcEVncVBIcTFYUGhSWWhOd3RORFFDN1BBMWV3WmU5a2JISmk5SkRNMFZkVDhOb1FxU0JkWk1OZmt0V2dvYTlHRWIzdmxLTmJ0MUFOMjU4b3lnc3NtY0NUWThLQVFtNnk1eGNGOVdkTVdkN0Z4WkViUWdISA?oc=5) <sub>搜狐网</sub>
- 📰 2026-10-28 [【视频】宝马iX3智驾实车体验看看宝马和Momenta的表现如何？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE42cDN0bG8yX3Z3WGM1cXNudE1zcEVtWnZpMHpzZDFxSnp4ODZvbGdSR1RraFdmeVZINXNRbUt4Q1dudkMweWRMd1F4X1QzeG9PR0pSVWpjakNqUEk?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-28 [奔驰利润率下调至2%，推40款新车引入Momenta智驾](https://news.google.com/rss/articles/CBMia0FVX3lxTE52SklUWnJ3U05YOTBncWdzYkZjVGNQWW1wM0JqaS02V0R3UUEyYWN4X0JQUzQ5TlpPS2k4V0hGMHBLZWJYeElpZ25BV2I2d3M5a3RqRVpGRDJhQzI3Zl9kdjdoX3JGVFluU0U4?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>XPeng</b> (240)</summary>

- 📰 2026-10-29 [Seoul court dismisses lawsuit by Tesla owners seeking refunds for 'Full Self-Driving' tech](https://news.google.com/rss/articles/CBMi4AFBVV95cUxPbFNkZ2xyaWxXT294dmlESXdoblVLd0txMENNdFA2dWV6QmJDeHpDeXBoSXR1VHpwdlM0QW9CbzB3bFFTWUZjQjRRSDlBcXhfVFpkV2VIVk1WSFFlZHVoMHJuY0tZVmtRdzBjYnRMNmgzdXV2dy1kQlFtbTZGV3l4YWNOd29BVTFxandrSnFxX2JsYkNpa00tRU9lTnUyWFFqMEltVW9Ia1QyZGQwaGIyMVFjZWltckMyVHZUazFUQUJFNzN5MmYybzI4dl9ISERVNDRsYzUzb1NBcUtHeEZDUQ?oc=5) <sub>The Star</sub>
- 📰 2026-10-29 [Samsung posts record profit in Q3 on AI chip boom](https://news.google.com/rss/articles/CBMipAFBVV95cUxPQm4yTGNwVExDcmxYS2hUNFhBcVlIZUpwSjk2VXpKNDZCWHlYckxIYVlQa1oxMHlNUy1pSGg5b0VfMlBZNTNhbGJIWmVKSjA0akstZV9MN0JPanZMNVFOTWtMS3RacEo5bmNNOWhULU4zSzRqS3UzZkdQV3otRU1xYndGaVU4cHcxLXVQWk10d2Y2YTBycVlDbjE5NDBUSG1oZ3pISw?oc=5) <sub>The Star</sub>
- 📰 2026-10-29 [23万级黄金大五座横评：小鹏G9L与4款新上市新能源SUV推荐清单+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBaN2dNdXZpZVZBci1hR1FJVEtIXzhCaW5iT19mVDJDNHpHSUJIVmRBQ2ROOVYzbEpsUURzeEVxdGc5bTBsU2RXcUozQzJzcVhuWi1JTkh2SjhaUDZ4dGxz?oc=5) <sub>新浪网</sub>
- 📰 2026-10-29 [小鹏GX真实口碑到底如何？50位车主评分4.43分，3个维度说透值不值+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1zTzR5UkJSeTNWQ3dvSE8wUlNmeC1VZkRpaDVkRkFZQlJNbER2T2pzYlA3V2tLWXN0Mms1djJ0V1JkdE5zODhaeTl1cVR5REFoeFJNVlNLWWRlWEhhOWk4?oc=5) <sub>新浪网</sub>
- 📰 2026-10-29 [长途不焦虑的大五座SUV怎么选？小鹏G9L超级增程与4款热门车横评+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1oX0FEV2ZXS0VXNnJjYXZDTktrS1RGXzNMLWppX3JyVVFLRkJUYWdTd2RMejFXR2tLLXhmcy1UbmxVUEtFY0x5Umhsc01kdWI4MEVPa05TMTQ3amNPRy04?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>Li Auto</b> (149)</summary>

- 📰 2026-10-29 [Li Auto launches updated i6 SUV with in-house driving chip and larger battery](https://news.google.com/rss/articles/CBMirwFBVV95cUxQR2FuMVNrU2Vpb1NSOFRyMjZSSnNhVzJZTjFPYTJPU2JVQ1Y2bVBKYVk3YURCRzBwVWdEczhzVDVIX2Q2VlBtQ2FISHR0cm9KeTRCb3pKUEQ0d0JCU1gyZWV1azExOHAwcnJhYUNNVHFqM2ZmY1hnZE51MllVTFFXemtIMkRGVk5KemZ0Q3FwU2VyVFNZanBncWhXRjN3MWE2bi1wNjJwaUVIa3hDcE80?oc=5) <sub>TechNode</sub>
- 📰 2026-10-29 [Li Auto's 2026 i6 Launches: Self-Developed Battery and Chip Standard Across All Trims, Starting at 249,800 Yuan](https://news.google.com/rss/articles/CBMidkFVX3lxTE4zVm54UEt3V0g4WkFWVlRaRWl3a1lZYmRhSHN0bjhCNlJOVlhITnlFNkdEQXl0X0oweENXbjJMU21uNzJfY0lqMmM3UW1oRzBZQ0ZCUXhjSlhUZm5qNjJMenVSN05zRThtNGhkcWlLOGJJc0ZMSkE?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-29 [Does Li Auto (LI) Need The 2026 Li i6 To Broaden Its SUV Lineup?](https://news.google.com/rss/articles/CBMixgFBVV95cUxOZzRTa0JySWZFRUUyd1pPaW1jd1lsSHllYlFRMmRndWg2ai0tQ0NzcHM2T09NNndId05iNDN3NVlJMG12bmQ1M05TVmIyeGR3SUs5cG5qcUdjT1FuRnBWY3ltZ3BuNGFyZmxmcjJZOTNGTnp3MnJzZUdvVVdFSFFKb2VlZE5sX2Z4c2VNREJ1Z0hRTTJCZFJFQUQ0Q0d6S0djOFUxaExuZWh3eE1OSi1PN3hxY2lKb3lkZVVBMkV3SlZOWDNJT2fSAcsBQVVfeXFMUEpSYnNHcDBtWC1ENWI5UlNpakxKR1FYX2w0aHZTTmtpZEJXQXluZ1gyZVpxbVBDeEVXcUtUR3RBNnNIcGFSczV4UUZxT3Y4Wkc4UlFNX2phRjJZeWRXeTQ3NFc4eXpsVmpnbnAyaGo5cl9scGNqQW5kdk82ek9pa3YtNkhGQkE1YlNncXRBNEswNFdDYW9RV0pFTW5DNmFacm55YWdkREM3MFU0ckV5MFpLcndOUHFqdTZ6UlRyU19oX1o3WkRXYzliOTA?oc=5) <sub>Simply Wall St</sub>
- 📰 2026-10-29 [全家六口跨省自驾零焦虑，奕境X9、理想L9、问界M8大六座增程SUV深度横评](https://news.google.com/rss/articles/CBMibkFVX3lxTE9GOUtLYWlpZEp4U0RJbWU5dzNaLWgxeXB5ZzlpTFN6ZFFpRFF1eElnWjdaMHJrSC1ueW1nUzZPM0IxcjdiYVUwckg0OXNpRS1uclNuZHJEY0FYVTY1Yk5ZYXJVRU4tRzV5N3hHdGtn?oc=5) <sub>新浪汽车</sub>
- 📰 2026-10-29 [2026下半年新能源豪华SUV横评：理想i9、领克900与神行者8，谁才是全场景王者？](https://news.google.com/rss/articles/CBMickFVX3lxTE9nRHRmVUp2MjNGOFpiT3lXZEJPM3JPNXBVamxjbTFtc05hbG1GZ3ItTXFvVTFtT3dsTVF5Z09IRDU3UTFuNExEaHN1OVpFaTB4MDRacFRfSmc0d0pBWlhnc2NOdmtlc25sMGtUS245X1cwdw?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>NIO</b> (142)</summary>

- 📰 2026-10-29 [Nio Smart Factory: What Makes its EV Plant Different?](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQaWRpNFEtbGhmLVd5aG9Femh6RnFXZGticFpNY2ctTjdIb1BPRHdweEhFYWY5MElZWFFVa1F4ZUtGVnItRTFSQXM0Qjd1WXVQd0RaV1VtaE5YOGxpZE1pNTdXbHFwdmd5MFk5OG90ZjBUcmJNTTdScDd1endwX0hPSmpqSkVPTWRNekpJY1VNdmxmMC1ud0xCS0ZpWlFQNmV4NXRzX2V6YmtRNm_SAasBQVVfeXFMUGlkaTRRLWxoZi1XeWhvRXpoekZxV2RrYnBaTWNnLU43SG9QT0R3cHhIRWFmOTBJWVhRVWtReGVLRlZyLUUxUkFzNEI3dVl1UHdEWldVbWhOWDhsaWRNaTU3V2xxcHZneTBZOThvdGYwVHJiTU03UnA3dXp3cF9IT0pqakpFT01kTXpKSWNVTXZsZjAtbndMQktGaVpRUDZleDV0c19lemJrUTZv?oc=5) <sub>Artificial Intelligence News & Cryptocurrency News: Latest Trends \| Analytics Insight</sub>
- 📰 2026-10-29 [再测蔚来ES8，世界模型NWM迭代升级智能驾驶](https://news.google.com/rss/articles/CBMikAFBVV95cUxPS1R0aktfU2IwU19rMXN2REc1WGJDVnVwTXRDZ3VWTHhtVkUwSE5PbUNaQzhOZUs1TGRrZngzZW4yWjRzVTNHSnp6OHBMa09JQmJzREJMb0JzSjJsR3VBWlB6LUc1Z3pFbVlPOUxxV2hQUFRoRkhrTmNzTkxySVlhY1RFbVdES1phaW9QQXBQekc?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-28 [【视频】贵1.18万就为紫色？蔚来EC6灵韵特别版值不值](https://news.google.com/rss/articles/CBMiW0FVX3lxTFA2M2xFVldvelEyb0xJdExyZWdWQVlkaFRkMFQxcDZNSWNKaHNPUmU3TmFxR0REYmVKc2Zlb1VYNFN5bm5GNXA3Wjk4MVZ2R2pqSG9QdzNuU2cxYzg?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-28 [智舱与智驾谁更全能？小鹏G9L、智界R7、理想L6、蔚来ES6大五座智能体验盘点](https://news.google.com/rss/articles/CBMickFVX3lxTE4zMnRjandNcDUzS19CcVhMUVNUT0pNbTRaMHJ2TFUtQ1JuRDJnZ2lwWWpPMm80bE1JSHJ1Z3FfMHJ2OXRycXZidFFfUjI4NFF4WXRUMVBIeFlwM1d1TUFEcFFwSTJrdzZqU3NHS01tMGtfdw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-28 [AIIB backs NIO Capital's Eve ONE Fund III with $10M for mobility, energy tech](https://news.google.com/rss/articles/CBMirgFBVV95cUxPVzVPem5ockMwQnlodGd6ZjFraFhta0hVZ1ZmMjNIaXByWUVJOUhIR0V4YTBZSnJ5TllUbVRDS2VZLWYzWG1jU2w0U1B2bzZaRVJzMXhkQW5kS1dPU0c0Q0xkR2VtSTNDRHJkVTRmcW80cVp2X3RYZkRHWXFvN1VFWmxfUS01WlBBOWo1LVN2NWxzajNxTzFwY01reHFaOTlIeWY5Q3I4NVEwVzVuM1E?oc=5) <sub>Dealroom</sub>

</details>

<details><summary><b>Huawei</b> (339)</summary>

- 📰 2026-10-29 [Mini Land Rover Defender Could Get Both Hybrid and Electric Power](https://news.google.com/rss/articles/CBMimgFBVV95cUxOa0lMWTl6TmhObW00aTNCV2pMV0hwdW5qdXlXdFZkVEkxVVg2eGJSVGVnQVhYTzlObTVoVmhzd3piMlAtLU16VzczYkJDTTNod3NaU2hoWi1IUGZyU2pJSHRlMXlacVZrcnVNeFAzcE1FR2V6WGZtMGZOeEhIWVp0Z3RNVExrdDRkSlJwaFJ2SlhybU5Wb1RvVXp3?oc=5) <sub>CarLelo</sub>
- 📰 2026-10-29 [Avatr 06T Electric Wagon Spotted Testing in Australia](https://news.google.com/rss/articles/CBMihgFBVV95cUxPSG1Eb0QwYk0tOG1HRV9qd2ZpOENhdVIzRXMwXzBLbEpzUHVvVlZnWm1lMTNaNFpNMjVEdmpEZGlxRmpzazg4OHZWdmJJNGM4UW1YQXpFakJqU3JZdUc3Qy1ITklIWFVTdldWcTUtZjdreDlBbnhELTBVcS1kQm5iMzF6eXZYUQ?oc=5) <sub>zecar</sub>
- 📰 2026-10-29 [Huawei Starlight’s first phone is reportedly a wide candybar with a 6.39-inch display](https://news.google.com/rss/articles/CBMiwAFBVV95cUxNQzFCbER2MWtNU1ZjRHp3ZGFHNU9nZTFfQkt4Y1U0MG1pdkFEM001enpfTm9DRldoSjU3N0RuaWY0cUtUd1RGUEpSMmVnRldoRzh2dDQ4MjRhYVczRzlDdGJkbFZGb2daZnJTTmlJZDhiTEZiZmVIcV9FUFBhVDJzNkhBa25WSFJ5b1NPaG5pSFdWNkFUeWtPM2dobklxcTE5TzJLTFFQdW1QWUZQYjR2NUd5dm5iempiNUtLMlNEOW4?oc=5) <sub>Gizmochina</sub>
- 📰 2026-10-29 [靳玉志：华为乾崑智驾公开赛首日报名破10万 10月31日开赛](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNbkN3MDREdGEzb2h2MEpjOGt5MUZQdkgyRXl6NVo5di0tVWZMUWVzeGxBTTZJMElHUjJSZjhqejVpbWdvQWw5ODd0UEVzelFQRG40OGZMR0hwd1JLdGs0b0hNVjRobVVUN0UzQm03X1h3bHJwMmtjZGcyQlNLWW04dzY3MUl1dXNF?oc=5) <sub>搜狐网</sub>
- 📰 2026-10-29 [全家六口跨省自驾零焦虑，奕境X9、理想L9、问界M8大六座增程SUV深度横评](https://news.google.com/rss/articles/CBMibkFVX3lxTE9GOUtLYWlpZEp4U0RJbWU5dzNaLWgxeXB5ZzlpTFN6ZFFpRFF1eElnWjdaMHJrSC1ueW1nUzZPM0IxcjdiYVUwckg0OXNpRS1uclNuZHJEY0FYVTY1Yk5ZYXJVRU4tRzV5N3hHdGtn?oc=5) <sub>新浪汽车</sub>

</details>

<details><summary><b>Baidu Apollo</b> (62)</summary>

- 📰 2026-10-29 [萝卜快跑负责人黎宇昕是95后真年轻 提拔真快](https://news.google.com/rss/articles/CBMijAFBVV95cUxPMnJRRnBTeU9TUVRkaHFaS2lvZmxDZkVxYTJ6SVQwN0dIMnEyRVRhXzhxU21TZEFRMlAxT0Y4RU5XbVhpTEpIeDB4YUNlOUpsemdhcDFTVXNsRGlNMjcyWmtMeExRUEsyWjRDRHQ0TTRkalQ5ZXdjUmlZcmtvSzY4LVpZa0N0ZUJXeGtaOQ?oc=5) <sub>搜狐网</sub>
- 📰 2026-10-28 [Baidu reportedly developing world model as autonomous-driving ambitions expand](https://news.google.com/rss/articles/CBMisAFBVV95cUxNX3d2TEVkQU1HN2ZRSFZJMkJaeEpCV0lLMXJvMDNCdWZXd0FzaVd2dlUxOFFDeHZ5bEQyNlpiUUtQTVN5elpUOWd5Q1NBTFh5UjFSYzdzcWFacWdVdDZMMWY5ODJkOE1XY3p3M3BjcU9BODNWajd1eVJaeFlhZG9rNVd0Y0ZaSzNhVXBlbGd1bjRKQXpVb20teHRpRGVTbm85VkZTZjFnU1huVktMQTVXbA?oc=5) <sub>TechNode</sub>
- 📰 2026-10-28 [百度计划近日披露世界模型研发进展 萝卜快跑已覆盖全球28座城市](https://news.google.com/rss/articles/CBMiTkFVX3lxTE5qV3RzLWVJQkxjMFhaZ0FHY0ppUXJEcTBOYURjOEhmSnp2cjNqYk1uSnRMb3lqWV9RTXhpU0xpT3ppRGxNV1pSSlZNQnJwUQ?oc=5) <sub>观点网</sub>
- 📰 2026-10-28 [Nuro Co-CEO Renews Case for LiDAR as Lucid-Uber Robotaxi Nears](https://news.google.com/rss/articles/CBMingFBVV95cUxPR0oxUGk1R3V6dzRNV3RWMnVwQzkzb1ozajBENUNIMjFHdE02c0lCNEpmcTE1OGhCYi1hazRfelBjcXJWc0VTNlRsU0o3R1NiUHVqc2pSZ3BEczkxMmJFZTNIV2REc3NCaENBMVlaNmM2U1o1U0NUNUU2eTdTSHc0SGVnSm5nNWh5NEtzXzRFc2l4NGNuYjhETGhZdzBDQQ?oc=5) <sub>Electric Vehicles</sub>
- 📰 2026-10-28 [Why is Baidu betting on AI cloud as advertising shrinks?](https://news.google.com/rss/articles/CBMimgFBVV95cUxOa3duLS04MmYyV3M0STlkam1lcjRXVUVmSGx2OEhlZi10SE9sWWdGekh4cjZkVkY4QzhNeUJpa29nOU9PM0k1b3pJellmMkFFUXBDbkNPbWRrb0ZBOXlmdXlHbHpNcXRTTTQwU1ctRndyVlAwTkltWmFhRDlvcmdRX3p0QTFMbk80SHhSekVnOTI0RWwwT0kxeFh3?oc=5) <sub>Kalkine</sub>

</details>

<details><summary><b>Pony.ai</b> (145)</summary>

- 📰 2026-10-29 [广汽领程与小马智行联合研发，T9 ROBOTRUCK在广州从化正式下线](https://news.google.com/rss/articles/CBMijAFBVV95cUxONGNtU2xFWHRjT1BrbGN6U2tYbWNtRHVNc1lCdmdDZGhyUTQyTlhwa0V5cERZbGpNYnRCdjdRWkVsQkI4bWZEYlItVmdGb2xYMGlRYXNuOXlBUmQ1YW1heU44b2dvdURFWnRJbFd6d3QtWUlLNWZGZmxYRWduTFkyajVHNW9vTTBlNElkdQ?oc=5) <sub>搜狐网</sub>
- 📰 2026-10-29 [北京小马慧行科技公司增资至2.2亿美元](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNZFhuS0dyU2hDcHdyVmREeVpCMFNHY3FEbzFDM2hGS3c2V2UxUGlGakFPTWhPZEE0MmxjZHJVcWIyQVl0QVowV3kySmwwMDNrTy0tOW5sSF9nYUNBQlAtd21mXzBVMENZaXpTVnE1NDJ5TUdsRjRUMkx0YnBoTS1xdVI4VDNuRjA3?oc=5) <sub>搜狐网</sub>
- 📰 2026-10-28 [Chinese Tech Firms Confident in Challenging NVIDIA, Tesla](https://news.google.com/rss/articles/CBMijgFBVV95cUxQUmdRcGZwbDBHSl9fc1QtQVdtWGNYcFpzSm1IWERfZHhKMGhoSlVrVWJDOV9lNVRlUm4zdHJwWmZfblFRT1BxSlBIT1FpcndiZ1oxQmptRVFySkpqT0ZvcVFaVzBfcDVmcG5OeDFmTXgtV2p3UEZzNzFIeGl1YWxqNldwZmViTTNTSVhveVZn?oc=5) <sub>조선일보</sub>
- 📰 2026-10-28 [Chinese Tech Firms Surge on Domestic Markets, Narrowing Semiconductor Gap](https://news.google.com/rss/articles/CBMijgFBVV95cUxOWXhnUG43eTBrWTd0Q1BhdTRockRmX0QzeGhxSjlBeWRxRE9FQjlBRlFwNldGQ2FGYXBLRmRQOFRlSDJycVZaUGVFWG5tYWp1OVFiNU5zZ2lGY3RxQ1F0RW1MMVdPRW10bk9US25UbndhS2RwcGUwVEhNMVVDQS11QnFQT3cwNTc3ZVhEcDNB?oc=5) <sub>조선일보</sub>
- 📰 2026-10-28 [How NetEase and Pony.ai are testing AI controls and commercial value](https://news.google.com/rss/articles/CBMivAFBVV95cUxNTDlfeHdnbG4yUmVWUFBMQUNqWVdxbkVNLVZzM2djdlFUZHJPdTJSN2JxOFNrbHNZZzhYZWRCWW52enNlZVRGVzJtWFROOGpRRkRIZE96clBNUHVqTjJWWHIxOW5wdnJfbG1YOWFPaG5BaXk1ek42bE9nVnRodmhsZlE5VGlpdG5rN2txM0J5YlZMLWZUTExzd1FFSkswVW5Ib2stNVA0Mnh2OEhwNno4YU9aTXZGTkN0V2ROeQ?oc=5) <sub>The Asian Banker</sub>

</details>

<details><summary><b>WeRide</b> (135)</summary>

- 📰 2026-10-29 [文远知行001号员工带队，景烁科技融资数千万美元](https://news.google.com/rss/articles/CBMid0FVX3lxTE9lTnNlN1Z5ZVpwQS1JZ0hfXzZ3Z3JtZkJDWF9pVkdQZnNWeEZiekUtTkFja2RpVjc5R1JQdGNGd3pkR3BUTFNpZ0tmejh6aU1TTFc0V2FvQzM5LWxHOEFhOTdVVnlFbW8xZm1sNzlsOG0yZ0lSVmI0?oc=5) <sub>新浪财经</sub>
- 📰 2026-10-29 [文远知行-W(00800)：景烁、台州文远及投资者订立增资协议_经济时评_财经](https://news.google.com/rss/articles/CBMiYEFVX3lxTE5LZURJdlI4Um1TWTNLVUV1Z1AzeTl4cFRvenRacHZ2Zm56bC1qNE1BeGhlMENqRmdBczNmWWZlajc0eVpZTmdySHlhUUFhMXB1MjFDdTh5anFPMWk4VklQXw?oc=5) <sub>证券之星</sub>
- 📰 2026-10-29 [文远知行子公司景烁科技完成数千万美元Pre-A轮融资](https://news.google.com/rss/articles/CBMikwFBVV95cUxOMTN3cG1SSXR3aGJySzNmamkxb3diclAzVFFxbHBDRXZSRFBnM2ZUMUtCYUcyU3FDLXFqTktUVC1LaXpZTmRwSVZkdWlJOFdBMk1wMk95dWkweVB0blJYVXF2dUlOTkZFckx3cVZVcTYzSWpObDNiMWhJbVRRQnJvLUFLR1VFcXJ1aVF6b1A1M1lwc3M?oc=5) <sub>动点科技</sub>
- 📰 2026-10-29 [文远知行-W(00800)：景烁、台州文远及投资者订立增资协议\|港E声](https://news.google.com/rss/articles/CBMiS0FVX3lxTE9zZkNEaEpxcEJtX1NOMWJrS1E2OENZNm8tdEZlT0pULVFYQmlOLWZlY1kwR3E0cE9sTVV3eDhndEt2dDZGd196T2t4RQ?oc=5) <sub>时代在线</sub>
- 📰 2026-10-29 [文远知行 - 投资者将以合计对价人民币7,000万元认购景硕注册资本人民币400万元](https://news.google.com/rss/articles/CBMivAFBVV95cUxQeUxYUzI5UE9MMzVyMUpqTTlkU0h1QnQ5RE90MjBLVjNsb3RSbWVlTl9CNlg5TDVFTFRndWZ5Zm5kNnpPbDIwdzJEWlhYNlE0QWhTVjhWT293bEEtY0Q3OXdnLWJaZS1jWTFXODhoRHg4b0JaNi1oWU5UZ2gtanZIUUVUMXFLdTgwUlNvU2N0aTh2TjdUcTBRUGdjaGJlMklVc3g0RHJsY2JxS0RwMDVaemhoQjZ3Q2RSMVREcw?oc=5) <sub>Moomoo</sub>

</details>

<details><summary><b>Horizon Robotics</b> (162)</summary>

- 📰 2026-10-29 [October 2025 Robotics Financing Landscape: 3 High-Growth Key Sectors Capital Is Targeting](https://news.google.com/rss/articles/CBMiU0FVX3lxTE9qYWNEbmt5XzhNcGlaUWFNbEp2Tlp4T1hXdlRDTjhhbWFsTUczS2tQaWRjVzFnMU5DWTU3SmV5amVXc0pxdmRzWXlXWlJvcS1FOXpN?oc=5) <sub>36Kr</sub>
- 📰 2026-10-29 [奇瑞造一辆“硬派SUV”，直降10000元，456Ps，标配猎鹰500智驾](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBOel9oNDZ2Nl95OVRnTHkzSW9Xb2RxemFLdms4ZUl6dUdDVk9waDVfaXFLZ0ExYTBJRkhkTkwtWjQ2SllaR2hQa2Jyb09manQ0eXJOM2g4dV9YRDA?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-29 [鸿海1150亿日元收购三菱电机移动50%股权， 共同经营汽车设备业务](https://news.google.com/rss/articles/CBMiaEFVX3lxTE9rSFdLNUpLc01LTmxWU3ppOG10WmlCMzJyS2s5cHRTU3hiNm1xWnNXUDZkWTJack1iTnhZSFlQRlpZS0dkdURwUkVIdFdRNm9pc1ItaVpmZEphNVUza0QxTlY0Tjk5dnBT?oc=5) <sub>盖世汽车</sub>
- 📰 2026-10-29 [iCAR V27长续航版上市 纯电续航升级至300公里](https://news.google.com/rss/articles/CBMigAFBVV95cUxOSVc3Qm5jOGEybm8wVVM5WEpXb1JDcFVZNEdleFVXVEYzeEZMNllnZ1kzREV1MGJ6Sjl1ZGMyaVhYbEt2dm5uaHFpUFIyaHlNcDZWUi1BenB3cE5ZYWhaSi15bnEtMW1pLTZMZWdwQUN5TVhWcjBCWDZhYWdhVy1MQg?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-29 [歌礼制药ASC30美国II期研究达主要终点及全部次要终点](https://news.google.com/rss/articles/CBMiYkFVX3lxTE5LdXpHMVFpZmhTNG9ONHhIdWpaTVVBMmN3ZkJDSUE5TFRHNXpvQl9hS3pUOGF0dGRwTXJuYXFrTC1TaGdWakZYYXl0bUlSRnFxNEd2T00wMXUwbEhKMElsNU13?oc=5) <sub>观点网</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (29)</summary>

- 📰 2026-10-29 [他在不被看见的技术高地，砸碎了一堵西方60年的技术高墙！](https://news.google.com/rss/articles/CBMiZEFVX3lxTE93ZmRqYi1TVC1qMXJpSEdYXzhCVEF4TGhqT1BVZngwVW9UeEQySDYyZ05uaDViX2ZxN1lmdkVLM05sXy1LdmxjVGstaWwxUnd6akhRZnpYUUVzRGNfODJ0cWxfUnc?oc=5) <sub>中国新闻周刊</sub>
- 📰 2026-10-29 [2022‑2026H1 国内乘用车 NOA 第三方智驾算法厂商全景梳理](https://news.google.com/rss/articles/CBMiU0FVX3lxTFBkSDRpNG03a29aNElYOFZSSjE5OE5iMTRISFd6ME1DWnE4OG95S0FlRFYyNm5oNTRlNktRcVc3VXo4TFpPZ3V0QWxqRjJwMElGWlA4?oc=5) <sub>电子工程专辑</sub>
- 📰 2026-10-24 [4款7系SUV扎堆上市，问界M7车长5080mm](https://news.google.com/rss/articles/CBMiW0FVX3lxTE14Njc1UEhVa2JDUjZldVh5cm9SaHl2bTB4dE5fQnVEbEpuUE1UTzJQS0dXOU50UjVYYm9IeGwyVFIzQ085QktXaFBvaExySzQ5VFROUnoyY2hCT0U?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-24 [从2026 WICV演讲看：文远、元戎、智驾新程把智驾的下一轮押在哪？](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1UMzkyZlFUZFdhS3l3M1dPYVAxemFzYjRHSFlnWjJUbEVzaDgzRF96VUJiUFhPWTlNdG95czM4NXg1Y0ZlY1JiY2VyV1YxcFZxblpv?oc=5) <sub>电子工程专辑</sub>
- 📰 2026-10-24 [欧拉5城市NOA值得买吗？11.58万带激光雷达，3个维度说清+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE9tdVFPMXpMMGg5UlpDNGt2RzJIMVJ5Slk4dG5SVGJxM0dqaENiNHhVWi1TSWFYTXFuc3VvMXdJMFdHOEY4cUNOcF9peENCbmxFVlVxcDRIMUlUdVdpaTYyWGpaZGY2Q2F1UGxTM1lVU0Zkdw?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>Mobileye</b> (32)</summary>

- 📰 2026-10-28 [Intel Unveiled Major Acquisition Deal Worth 15.3 Billion Yuan](https://news.google.com/rss/articles/CBMiU0FVX3lxTE90WEEwZWZVeVUxbkZadThjRlhFQU5ZUXh4N1hidkg4a0lzT2NJNEdpalJvUTlxUFZuY1FKMXI4OUprV2JCVk9tcXdUVi1PR05QRS13?oc=5) <sub>36Kr</sub>
- 📰 2026-10-28 [Mobileye Global Q3 2026 Earnings Date and Estimates](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPdHRycVNma1kxc0tsbVhQRkYtZWdaWUUwX1I1cE1OekhoN1hhbkFLc2xCX2NJRGtPQm1VX3NfOElsUTRYS3k0OGlCOXprUTc4UDlKRi12OXNxUHozcDcwTEZROVNkeWRKR1dlSVhIbndPVkdDZEFzY1ByTmpSMkhfY0h1N3c2SDc4?oc=5) <sub>MarketBeat</sub>
- 📰 2026-10-28 [Mobileye earnings ahead: Can strong results reverse slide? By Investing.com](https://news.google.com/rss/articles/CBMiuAFBVV95cUxQNklzNm1sbm5NMlNON2E2SmU5LWVGeVR2dGZxM1VDVjl1dXowSkFUOEFVMDAwdDN5Y1RWOWREZXNiZkdScEN5eUFKdFloRUI5aGcyT284TW1lQUFZT3pldjRUUUJnQ3RkX1NsOV9jRU9iOHZqaE5xdlVHNmZsc1M0OENfcGlVNXdFaUI5Rm1HWWM3eUdxN0JsNU5jSHR5eWFTYTQ5Si1ZV0Q1TE9LYjdUUWcyQjZqdktQ?oc=5) <sub>Investing.com India</sub>
- 📰 2026-10-28 [LiDAR Market Growth Drivers, Autonomous Technology Trends and Industry Forecast 2026-2034](https://news.google.com/rss/articles/CBMilwFBVV95cUxOVng4THVhTXZHNlJkZDNIQVRtUGw2STBhX0Noa1d3V0IwXzhReXBZT1d0R1pLYUJ4RjdxSHJ5czZhYTIzSFZ5Uk41VlhpNS1DenpIdl9pY0dXM3JidGpjZXFMeVp2UUQxVlNDLUgzRHpLSHZxR0h4SnJxZEVmcGhQbUxVNWV0YVA4dlo2MEljUVd2ZXpyMGVV?oc=5) <sub>openPR.com</sub>
- 📰 2026-10-27 [Intel To Acquire Israeli Quantum Computing Startup Classiq For $2.3 Billion](https://news.google.com/rss/articles/CBMiqgFBVV95cUxPY0N2azgyaUxFbnp2Y2JDd3piZ3hCeXdZdkZDOUVsdUluY0ExeDZvTjVKemU3MnNnNTRVb2NLek5QV1haczhOZGJMeUp2LWZMV1pKckI5M1ZZSDU0VDQ1VlNONmdCOEYwc2x3QnozaVcyZVNRVUJ4UWh0OEhGaHpXel9GQ2l5NDEyZ1E2VmpWbnhURVk4V0tVcUdsTnprVEFhdk16OFlIZldwQQ?oc=5) <sub>VINnews</sub>

</details>

<details><summary><b>Aurora</b> (47)</summary>

- 📰 2026-10-29 [Aurora’s Autonomous Trucks on Track for 2027 After Missing Goals](https://news.google.com/rss/articles/CBMitgFBVV95cUxNdEE4b1hOZGhoT1E2aDRLOWlZZ21XQ2J1WDA0Qkc4bDlkVWVYX2dNMUFLWS1GLXQ2em9GRlJacno0Q3I4NTh2QnlRSlp6eFRUN01uaUF6TnBTLXVtazVfcUNiSGlFQXB0NWR1N215ZXBETWdIZ1pBaDlYaFpuVnB3dHZoVmdaRnpZVmMyc3ZkdXVkc1JhZE9TV3FFRXdnNHM0QzdKQ2plUzNzVWtrZElnd3U2azZRdw?oc=5) <sub>Bloomberg.com</sub>
- 📰 2026-10-28 [Aurora adds 500-truck Charger MOU toward 30,000-truck goal](https://news.google.com/rss/articles/CBMijAFBVV95cUxNVjlTNDV6Sy1keDMzRzFHNWpZekp2eUNUb0RTZEdhN0lTd3g2c04xRTZtYnNOS0Q1RXFjR1kxOURjU3ViSHVEUW1iNGQ1d3BRTHFrSXZSMDhVQW5VSmFWa3pUODZuY2JYNXFocEpiOWN3cUNKUll6d0ZOSXJfS0ZMTkpKVllxLU0tRjNmeA?oc=5) <sub>FreightWaves</sub>
- 📰 2026-10-28 [Aurora Q3 2026 slides: driverless fleet expands amid production delays](https://news.google.com/rss/articles/CBMixAFBVV95cUxPa1d4VVNkMXVxRlp2MWtGNXI1RmV0YmxBNGh3SGtoM1VWbFkzUnRhd2YtWERBcW1NUkdsV0tRZkp4eUJuNXdMLTNQSjhpQ0xBUktaUUJGZ19Fb1ZEanNtYWc4cHFOSFRlUEVNWnNiSDRYOVE0TjRyN2ZDcTBDNHlYR3NvMGdnZmJ1SENycjhyVjh6bXRyb0ticVo3NDZldGxEUTV2YXdzWnRNa3ZNUzJMSWZ4M0dvVlRzaFYzU0hWNzJ6TjlT?oc=5) <sub>Investing.com</sub>
- 📰 2026-10-28 [Aurora Reports Q3 2026 Revenue of $3 Million and Operating Loss of $257 Million](https://news.google.com/rss/articles/CBMi1gFBVV95cUxOSVphR2pfQ3JWYjdfT3BCcFVwb0ZiZnhaUFJhLVQ2VmxFNzN2WkNZYzN0UVB4eXVsX3BSaU5VZzlGMW9LRndjUDlMX1czWVMweGpKUC02QzFXTm8tNUlIOU9CYUs1Y0FEVmgwZW5MRXpNRnRRX1QwdkltaU9QSkFfX3YwWGVDZXdwNXhaV01ITTBfUzA1QUNDRUl0Y0FrWTZJNnlMUEtBd1hCNHdmeHQtWnhrVmhvOXdmRWstWmc1d0hUTlQ3MHIwck9BeEdSQm5TcWlLS1VR?oc=5) <sub>TradingView</sub>
- 📰 2026-10-28 [Aurora Announces Third Quarter 2026 Results](https://news.google.com/rss/articles/CBMiogFBVV95cUxOa1hUVEdjSklsZW4zd0Y0Umh4QVdiR1JJWmIyalRQTGV4aDJUeEJkY2ZrR2M3a3dwNk1VeW9kVG5hQzJOeWhsM2l3bjhsdlBFUDdUOWU2ODUwRnA5MUtfNmxmcExZVUtneVJVN3JJVlhOSzZldm1Od3ZxQnk4dHpTS2JReGVFeG9yd1ExeFYxNkhGWlFoWGRubDJHY0xCT2NaNXc?oc=5) <sub>Business Wire</sub>

</details>

<details><summary><b>Zoox</b> (64)</summary>

- 📰 2026-10-28 [Where Are the Cybercabs? Zoox Eyes 150 Cars [2026]](https://news.google.com/rss/articles/CBMikwFBVV95cUxNMUZXQnhZd0ZhcHl4Qi1tbjFKSGxQSlgxY0tPT2pMbmlKZ1pYbVNaQ01WV2hicndLbGZoV0xTRk1iM1IzSHE0U19EZ3BYS3UyZFNYVHN6WmZDeVZPVnU1M085R3I5ZnFkZ2E2SmtPZHo2bnJEOWZHRl94TXpIZGxPbVBfelJQUHoyU1hSZ3BjTDlIcWs?oc=5) <sub>shattered.io</sub>
- 📰 2026-10-28 [Nevada caught between AI job growth and job losses](https://news.google.com/rss/articles/CBMiggFBVV95cUxQTVF1SXJGdUFXOTE0REU0QU95Zm44ckxxMzRZSXVPakNTQkFFcjVKMHUtcWdSODFzeTRST2U3SHZWRWxSUjJGUUVRdUoxLUVNWHRKUFlxUktKOUhGdGo2SjM5VVJPUk5LbXNjcW5QbGcwM3diaDV0c05OV3BQS1hwSjJB?oc=5) <sub>Reuters</sub>
- 📰 2026-10-28 [As Waymo expands overseas, it remains a niche cash-burning business](https://news.google.com/rss/articles/CBMipgFBVV95cUxNcnFOal9qb29IdlNMWEd0c3I0ZDM3aXBxLTQyYW41ZFlMTnpQLTNadzdQX0p0RnBOLUR5MUFxQUFjRzlPU1pBQW5RZjVwWG52MjNVZFFDUTBwVTlVcU1yYjRxdUtwbVNqM0pWMXBZOG90ekJNSmJ6ckpJam9sZ1dzRUE5SUo4OUsyYlRBSG1BQ0xoRDlhcTFLNUt0a3pFT0lZeHllOERR0gGrAUFVX3lxTFBnV2JPdjVVQkhmSVJVN3ZyRjNjZk95NHZCandZR0FMQTlCbkhHRy1HLXRZMVAxTGNYMU40QUNBSHYxOXZHRzlIRE42VWI5eG1TMlJlOWpEM3pOb3g0UDJUMGVYWVR6cGZUUHV2cUUtQmszSG1yM1JINnc1c2w5NEhwWFp1VC1ITWczUzJPa3U1MVZHNVJad3VYX1Q2MGs1UGE5QjBFcXR2Vl9IZw?oc=5) <sub>CNBC</sub>
- 📰 2026-10-28 [Elon Musk Says Tesla Robotaxi Expansion to Miami, Tampa Beaches Is ‘Coming Soon’ After Ron DeSantis’ Call for Expansion](https://news.google.com/rss/articles/CBMihAJBVV95cUxPU0ZHRFgwYVQxaEkxMENpOVR5Nk5BNzJHekN3V0hQLV9ybXNUM2ZfUldYckhEekZDU2NzcjRNVVJZNlpDMkdqQkhpbGJjUTNNaVctREtHdWxYMVdwU3h1VWlJejVhTWFTUG1Rc1B1TFZXOWRoM2dab3ZpX05TalY1dXplLWZEbzFnTHNYU1E5RWgzb3dzM1Q4MUt6bE4xWkctb2dIcFp6M2o5cEh0ZU52aFdVc21EUExiT1hOUHJZS201ZS1RNWgzQ09wMlpsVzZIU0x4anNiR0Z6UVBnQkV4SEk5aHRUUm52QzRhNDczNmFuNm1nR2ZOOFZ2V1Q2TzhEcXJFbQ?oc=5) <sub>TradingView</sub>
- 📰 2026-10-27 [‘Where Are The Cybercabs?’ Tesla Investor Ross Gerber Takes Aim at Elon Musk as Amazon’s Zoox Eyes Expansion With Santa Monica Deal for 150 Robotaxis](https://news.google.com/rss/articles/CBMiaEFVX3lxTFAtSmZYX1h4LXhNdkpuMjk4MlVBY2ZGRmRjSmhBa2ZITGU3ckNONDBndjRpNU5McVFjaWdfVzJjRWFydmcteGFJRVBTTXh4Mzh2MFhkNXhlTl9xdGttSEhJWXVBdXJFZ0tw?oc=5) <sub>TradingView</sub>

</details>

<details><summary><b>Motional</b> (13)</summary>

- 📰 2026-10-28 [Hyundai Motor Rises to No. 29 in Interbrand’s Best Global Brands 2026 Ranking](https://news.google.com/rss/articles/CBMirgFBVV95cUxOYW13NmJqeUZhQ1A1UnJOYjB6NUdRZU9uOHdFRVR6Um42WFlSZmdOOXV2WnJqVUdJVUw0eXVPSTMxdWlNRnMySXJ6N2dhd0pIYXBpWXU2cDdZRlZNWGhhWWVLcDdnV05kMVd4cGtiYUkzNnRPTVN2UW82cmdSdHNfZy1KMlktRlZWMF9TdWNLSDlZeWJZcWtscG5ZVWg2T2ZMY09NNFNDOGlPUkw3SVE?oc=5) <sub>Indian Television Dot Com</sub>
- 📰 2026-10-28 [Hyundai Motor Rises To No. 29 In Interbrand Global Brand Ranking](https://news.google.com/rss/articles/CBMiqwFBVV95cUxPWlRYZlVKTzNZWmdfWXpGUmxJd2ZKQ1pnX1otaXB4XzgycnY0NmZkUXFsSGFZQlRKbFJWRkFwWmIzWEF6X0IzRjh3Z09YYkxGRm1nbURLQU05R3pnN3ZLcHVfMHRRNm85T3hXeUR5Mklha19vZ2QxUmdiNE4xTUxaaV9Nd3hLQk9Nc1ZTY1lxbmR2Z3RxSXQ5RlRnb2RLTmowMkVaZzRIZUdGZDDSAasBQVVfeXFMT1pUWGZVSk8zWVpnX1l6RlJsSXdmSkNaZ19aLWlweF84MnJ2NDZmZFFxbEhhWUJUSmxSVkZBcFpiM1hBel9CM0Y4d2dPWGJMRkZtZ21ES0FNOUd6Zzd2S3B1XzB0UTZvOU94V3lEeTJJYWtfb2dkMVJnYjROMU1MWmlfTXd4S0JPTXNWU2NZcW5kdmd0cUl0OUZUZ29kS05qMDJFWmc0SGVHRmQw?oc=5) <sub>Autocar Professional</sub>
- 📰 2026-10-28 [Waymo Beats Uber by $10 at Nashville Airport, but Loses on the Highway, Field Report Finds](https://news.google.com/rss/articles/CBMiW0FVX3lxTFAzS3V3bDhOWnRqTmhzRzVNQWx1MlBhV0psZ2lwZEU0TEdoazhtMXZ0Tm9jbUlId2p0TV9EX3FiUmtmZXNPaGdkS3dGY2ZlNEc5cks3WGNUSGxFVnM?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-23 [Waymo Is Accelerating Robotaxi Deployments. Who's Trying to Stop It?｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE83QXNrSG5UMnZyN2ltY3BENUtsUVBVVk4zbnpNTVNCTENELTBYZjVpY0NqMnFRUFYzVmdMSWdzVWswU1NZWHBRSkd1N3E1WnZxbUVaZ2tneWlmQWU0dTVZ?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-22 [Zoox Las Vegas Airport Field Report｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBuM3U0cTFKZHF4ZjhlSVhzY1k4dlVoMDhWVy1PaWUtcUJKWF9jeEtEczdXbm0zbjhTUXBiVFBpdWplUm1NNHBTbndsdzM5TTZYM1ZJSjVJNXBQM09iRkJJ?oc=5) <sub>finance.biggo.com</sub>

</details>

<details><summary><b>comma.ai</b> (6)</summary>

- 📝 2026-10-23 [openpilot 0.11.2](https://blog.comma.ai/0112release/) <sub>official blog</sub>
- 📰 2026-10-21 [Is the race to build self-driving AI turning into a cyberwar?](https://news.google.com/rss/articles/CBMikAFBVV95cUxPd1ljS1V3ZmI4RGdJZkRQdVpkNmRqcm5tVUtpRllXYWMyQ2ZnaFFKRzgzY0VaUDNTR3VwYV9lRHI2RnRUcV9za0p3bTNsMGJmSHNZUlR0MDFsYm1FLTVtUEl1UEJhSi1hXzMtc05tendPaDltRzlMczQwRkx0dTZJaGVjTk1DOXp1cVpSS2Zqc0w?oc=5) <sub>Yahoo Tech</sub>
- 📰 2026-10-21 [SquachWatch Turns ESP32 CYD Into Standalone Privacy Scanner](https://news.google.com/rss/articles/CBMikgFBVV95cUxQT3EzRFl0MWRwUm1tYklBYngwR0lDVGswYUJ5TUdQNjdPdkJLajV0bklVU2FCWFdMUlJjMng5NEc2ejQyUV9MeHB4RjF2UlRxQ1pUdFpSTWlETVU4WmFxTVpLTmJ3Z0NPX3ZnWEc2M09VcDZRNmtlUDlBZU5hQmFrUlNWOHBCRGtZQWs1Z3Z4TlVBQQ?oc=5) <sub>news.lavx.hu</sub>
- 📰 2026-10-21 [IQ.Lvbs claims hack attempt traced to rival Comma.ai IP address](https://news.google.com/rss/articles/CBMilwFBVV95cUxNVXdkQWthMXBaOUd3aGV2Nl9Kb28ydFVOcElQcTUwRnEyWVF4NTVzOWd4d2hDSlFFbjc3Y2hranNuOUtSS2dha2NKYzRvUkxzSlJxSGhQZTI0MEVySU9UOVpjUlVSUEpPTl9LcWhhNWJzLXdQaEhNMnRCZUVGd0dDTEZFYzdhcTdsQWNkczU1X0UtWTdJbXdN?oc=5) <sub>news.lavx.hu</sub>
- 📰 2026-10-20 [Auto tech startup claims it traced hack attempt back to rival's IP address](https://news.google.com/rss/articles/CBMizAFBVV95cUxOVHlZN1E1cDJqNEFHSFg3U1hCbnZRdFhtdk11blVLd2d2dUNIVkYxUG1xd0NIWjdNZGNVMHJvalh4SEM2cTJhclMzWHRyR0thRWJDMHFNUWcwNHAza21ybFYxV1Zyd2ZoaHRORmRtdGxBbWlSWk1UUnllQVp2dGFCVlFjcE0yOG1OaW9hdGhRb0lpS25LeUZFc2pKem5QaGVnZ0pLNExzeDdUOGNERVM2andndkh4LW5JWDdaSGhqQmZxOFMtb283aDFIWkE?oc=5) <sub>The Register</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
