# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-11-12 · 1,277 papers tracked · 45 curated.

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
- [Motion Prediction & Behavior Modeling](#motion-prediction--behavior-modeling) (1)
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
| [PixelPilot: Scalable Vision-Language-Action Models for End-to-End Autonomous Driving](https://arxiv.org/abs/2607.04637)<br><sub>Pin Tang, Guoqing Wang, Xiangxuan Ren et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 2](https://github.com/VISION-SJTU/PixelPilot) | Vision-Language-Action Models (VLAs), which leverage the advanced reasoning capabilities of Vision-Language Models (VLMs), show promising generalization in complex autonomous driving scenarios |
| [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)<br><sub>Nan Yang, Zhanwen Liu, Linfeng Zhang et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 11](https://github.com/Zizzzzzzz/MVPruner) | Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings |
| [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)<br><sub>Yuan Gao, Wenting Miao, Mattia Piccinini et al.</sub> | IROS<br>2026-07<br>📑 1 | [⭐ 31](https://github.com/TUM-AVS/Chat2scenic) | Validating autonomous driving systems requires diverse, regulation-compliant test scenarios |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 19 | [⭐ 548](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
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

<details><summary><b>Waymo</b> (139)</summary>

- 📝 2026-11-05 [How the Waymo Driver Manages Severe Winter Weather](https://waymo.com/blog/2026/11/winter-weather-preparedness) <sub>official blog</sub>
- 📝 2026-11-05 [Rethinking What Freedom of Movement Feels Like for Women](https://waymo.com/blog/2026/11/because-women) <sub>official blog</sub>
- 📰 2026-11-12 [NHTSA probes whether Waymo fixed robotaxis passing stopped school buses](https://news.google.com/rss/articles/CBMipwFBVV95cUxNWm5Qc2M5TTExMzNfR19YRFV2WlVac1lLVWFNRkxsQU9TZjRTcy14N1p3QWxRU2dNeWFiOG8xYUtVLXEwREtra2ZzU3Y4R19EeUxiOEJsTXhmS0JPYTFxUXlhYzA2d3YwTWJmRHlEOHdqcW9BclZpT0ludDQxX201U3c0aWxCWGpRNWVMRktvNEF6aWVyaXdhSkU1dEZ5clRRX3NrcVNBOA?oc=5) <sub>KEYE</sub>
- 📰 2026-11-12 [Video shows Waymo trying to get around CHP traffic break on Bay Area freeway](https://news.google.com/rss/articles/CBMihAFBVV95cUxPank4VWNFM1R2c3l4dk1jZkZIUGFHX1pmcVFRR2NoR0QwTWduUjB6RTY4eGNXcVlTV19lbXVSaWU4RTMxXzIwMWZRVU9rX0YxVWYzRUQ4RkNtUGxZWHBMUDNOZUNIdFY0WVlhVlBHbjBHTkxCQVhZREg1aF9lZVl2YWxkLW7SAYwBQVVfeXFMTW83ejZyVldEYks2LV9peEY3V0dHdzlaT0kwSHNVN1E3T2ROVFhPQms5ZGJzb0xDVldxNTZ1Z054TktCNkQyQVNyUXFMdWMyM3NxZ0FwZEdST0JDVlc5aEJNYldKVVV5clpQVUtWM1hJNnhyZjB0UGxCSnY3SWZIOXktR05zOGM2WTZ5bTc?oc=5) <sub>NBC Bay Area</sub>
- 📰 2026-11-12 [Video: Waymo ignores CHP trying to stop traffic on S.F. freeway](https://news.google.com/rss/articles/CBMigwFBVV95cUxOZVRnVXFCTXFVY2pteF82SjBkakpjNVp5LWpBUEZNTnpKODBrVHJFa1IxclVpYk9sRGozY0J0am1ZbU93cGdBaERmUFY1S193akdWdjVqWkx4cmpQT24tVzNCbExkMk5mSWxablMweE5UZW9XNVlGZXA1WGZZOEFVUGREYw?oc=5) <sub>San Francisco Chronicle</sub>

</details>

<details><summary><b>Tesla</b> (192)</summary>

- 📰 2026-11-12 [Tesla Robotaxi Now Works 24/7 While Elon Musk's Robots Head to Optimus Academy](https://news.google.com/rss/articles/CBMia0FVX3lxTE9EYUNMaUxJQ2pXeGtmMkU3Wk85MUFUUFdkOWY0b01HbE5GbU9seVVKLUNUdGN4QTR2XzVMZHVYTmxQNjhKZF9NRzBFZ25LbllrYXdISzY3QWZ6c19Xc01XNVZmT1o3bzdNOEUw?oc=5) <sub>BeInCrypto</sub>
- 📰 2026-11-12 [Tesla Robotaxi Now Runs 24/7, Up From 16 Hours in August](https://news.google.com/rss/articles/CBMijwFBVV95cUxQR0R3N1dEaHlWbUZZOTBVQmZOQUpHX0d3YXBWU0lJXzJLaWJyM0xNQkp1YmFuRWcxQl9nRzM2aTZGQld3d1VIZnR2RE9XOV92Z1FlQ3JpS0NRZWFIYmRkaHhpSjc4UzVNWXRJdUtMMnpQdmZUYUZ2VU8tX1FCY1NTZm1tVVE4TUNNTm5VV2xKRQ?oc=5) <sub>FourWeekMBA</sub>
- 📰 2026-11-12 [【网通社快报】特斯拉于2026年1月取消新车基础版Autopilot，马斯克决定此举以推动FSD订阅量](https://news.google.com/rss/articles/CBMiTEFVX3lxTE1qLXlOUWFieFkzamVra2puWVhpUXhGcDJtNXNuQkdYUmJqMVVTSGtEVE1ySkdXRU9xTGUzWTY0ZkIwYlVTdTFFRWZEaHI?oc=5) <sub>凤凰网汽车</sub>
- 📰 2026-11-12 [曝马斯克亲自取消特斯拉基础版Autopilot](https://news.google.com/rss/articles/CBMicEFVX3lxTE1pY3JSNlBXNFl3ZlVVb0U4c0EydFFmQ1RXZ1NWNURSc0piX2VRaFhGYnRMUnBrUFlfYUR4eVFtSm1VOG1BejJ0Zmg0S2tzSlRpcHhBZ09pb2t5UHdJZmVrOHIwSlVyUnhzME1QbzZCRXg?oc=5) <sub>新浪网</sub>
- 📰 2026-11-12 [iCAR V25同台对比特斯拉FSD与华为ADS](https://news.google.com/rss/articles/CBMic0FVX3lxTE5xbF9wZnY1YS02Z1F5c1dHcVJSMThqSDNTUmFKX2kwNFFPbERGZDkzWkR6R2sxN3FfZEs4YTdBdHJZelNkNkZ3NXBkLUJmZWZITmJrcS1ybWhCZGx5OXA0QS1xUzFoRTJsblAwOGRTWERBeE0?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>NVIDIA</b> (114)</summary>

- 💻 2026-11-02 [NVIDIA/nvperf-core — Core NVIDIA Nsight Perf SDK APIs and libraries for collecting and analyzing GPU performance data directly from application code.](https://github.com/NVIDIA/nvperf-core) <sub>GitHub</sub>
- 📰 2026-11-12 [Morning Bid: Jensen hangs on as Nvidia tumbles](https://news.google.com/rss/articles/CBMijgFBVV95cUxPTlJzTHY4Q3VzUF9fS1ZwWlFrUWdPSi1WbTJDSVBpbXUybVpRUlVvajVLakJYcldpNi1raUwyT2R5RTAxM2REclViNDZST3loTVE3elhGQnZ4VUh3M0pMRTBLOC1zM3Q1OEk5REpZZkw5LXFUZkFpM3I3Nm5aaGRBZmFSNmtvSG5tM0R4ekV3?oc=5) <sub>93.3 The Drive</sub>
- 📰 2026-11-12 [Siemens, NVIDIA Develop AI-Based Virtual PCB Inspection Workflow](https://news.google.com/rss/articles/CBMikgFBVV95cUxQYjVlXzM3NGJqME8wcVRXbWU0SzR0YmdEUlpZdmVFcTZjRjR6VHJKZWpmSHYzUDJhbnJqREV6cGsyTjRBVzVRT1FqdWlrVGxCc3dWY3dRMHVOWktiUU9uR2ZBZGhQN2RQZVJUMjRMd1JPdkpZTDBWVnQ2Qk9vbHBJV0hYLVlNZmhJQVRYRFkyblgtUQ?oc=5) <sub>EE Times Asia</sub>
- 📰 2026-11-12 [Who are Jensen Huang's children, Madison and Spencer? Former pastry chef and cocktail bar owner making $2.55mn at Nvidia](https://news.google.com/rss/articles/CBMiigJBVV95cUxPRzVkOWRXcmxmZkFLcjF2bi15a3h2dEZKWnhLQmVkNDJ4UktHbDhKaUpqMHExOHlrdnhUaGpoRzRYbDFHell3cldzeHJ5THdDb1NGNmlKMVNzU0JsaFNnajd0QVZVMkFXTDA1MTJSay1wR1ZMYndoWG53a0l6RUh2WDM1ak1QY3JtX0dwcE5VYkRERTlTeklINVVoUmpMZXNVNnExVGlDM0Q0VkYzUlZza1pxNlN2V3RpcE1oWldTdEFmQ05RY0N4ZzVLeTNUZENGbGZtby1uc1ZXTWJyQVlrYTZwS0E0OWhfQnVNQmY2aEJ3QUhOVUdPN1h3UlM0NTZ4WnVYWlhIT25mQdIBjwJBVV95cUxPS0VCMTJPbTBWVm5vSEM3dFhLNC1uM29JOFNiZDZBT0hvR1FIZjRfVUVNS044U3IyU1ZxUkg2ZU40M1pNUlBkVmVHaFV6VG1ja2hTdU9WVVR6OWFqeERNbzNCeVJWYXlNY0VaX3NQZ1J5U3czUWV5WXdiNWNnQnpjOWNTT0JhbWZ5WUhGMHN2bFRiOFViQzVnT1ZIcGtVbldPRms2eTdNZ3hJODZIaHFzMjdIUXVGUmRNenU0ck9ncERqcUhCY0V1T3AwU1V6eHRaSTZCMWlNenhPamRudXpxQTZ0VGh0MnFLLWtTRWg5alVCakZYaWZBcEpQME1KLVJBVGpQdzhXb3NvZC1SU3NJ?oc=5) <sub>Livemint</sub>
- 📰 2026-11-11 [Tech: What The Nvidia Scandal Means For The Global Economy : 1A](https://news.google.com/rss/articles/CBMipAFBVV95cUxORWlBRVdUZGVGeEt3aXgzUXc2ZEpibHMzZGRxUDRhSTBTZkd4d2NBaGROQVlpTEI0UzJPRXNjZ2Joa1VfeWJVdlZoSUt2ekxtOW15eDVwZHM1M1RRTW04d3E5bVNtb05CSGF2UllKdkdza1BubDRnMWlINGo3ZkE3STlWODktX3B2RExUdXZURkphekRxVXllSTVQQTdlUmlJZ1VJaw?oc=5) <sub>NPR</sub>

</details>

<details><summary><b>Wayve</b> (34)</summary>

- 📰 2026-11-11 [Wayve accelerates autonomous vehicle AI with CoreWeave](https://news.google.com/rss/articles/CBMiogFBVV95cUxQTk9NV0lfWjVZQ0pwSnlmcHJ4NXlpU1RxOHhITm9XVmJfeExYdU9OSHE0MHBua1l5Q1JicDlQWUZkcDdkTFJDcEFQaWRUNGw2NVlxTmdTWGQ3alBMb1l4TGZZbHZXSmxnZ1BlVUdLZVAtc0RkekVhNl96R245S0liVkpBQmtHdFd6T19zRF91MDVDOFVZV1FFVWRMSWJFZnkxaEE?oc=5) <sub>Computer Weekly</sub>
- 📰 2026-11-10 [Wayve bets its driver on rented Blackwell muscle](https://news.google.com/rss/articles/CBMisAFBVV95cUxPUDZ6bGVHcndyRzNMVzNqdTdWVHUyT09VTG1FNkVNd05iVWpNTTgtb0p3ZHRLUlFUd2c4U2Y5bzYwX1pKeHh2RnhFRUZ4MTg5TXJPZzhDUUJEU0hyTF8zcWNKX05lOUItQVNpTEhfTk4zS0d1bkN0NnVxNm1SNzlMbmI0UW9QSk1uMUNwRVlSNFZ2S3oyMmw2d2JobUV4bGpPdFFmMnJiLWI3MmxRdjdGYg?oc=5) <sub>StartupHub.ai</sub>
- 📰 2026-11-10 [CoreWeave Falls 1% Pre-Market: Strikes Multi-Year AI Cloud Partnership With UK Autonomous Driving Company Wayve Ahead of Q3 Earnings](https://news.google.com/rss/articles/CBMi0wFBVV95cUxOVTlxMlUydHpuRlJWdXdoNHU1Z19ISmg0UTcwaG1tNXh1YnpMOVNmSXdzZXVqS19uSG9oU3hJaXhFSFNpdktxWmdQR0YwTENiT3R6d0RJS2JwSDA0T3pYWG41T1pJWmpFaDViV1F3SDJuNnduc1N3U0h1SVRRNWYzY1RkY3planFLV1dnYmllMy1YN29fUzUtWVdyb0d4Q3VsbDlZNHpIeFNuQm5ldjRlRklPOFhoSDVsSVhQd2VrZkptVURGVVNyNHlrTlVOUWc2NnU0?oc=5) <sub>TradingKey</sub>
- 📰 2026-11-10 [What Does CoreWeave (CRWV) Winning A New AI Training Deal Mean?](https://news.google.com/rss/articles/CBMimgFBVV95cUxOcDNZY2dVeVo0ZWNwN2hmZDlEZFJOelNPMy0yRmhWRzV5UjV5Q2tmNEtxN0p4d2pTb29iR0FtZjFueXJvUzB5cVpxaXBnNXpwelZXTXFEdzFvalotZjB2bWc3eThkS3BLZ2xLN3haOV8xRERuY0hYRFQtVjRsc1VvNE9FclhlT1YyVnFhWkFtaThfTkszRlVNa3V3?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-11-10 [CoreWeave Cloud to power Wayve's AI Driver training in deployment of autonomous vehicles](https://news.google.com/rss/articles/CBMixgFBVV95cUxPMUNvcEZsZ3kzNzFsN295US1lLUlUQW5xcExTdFRwMm91ZG91dlVHU0lyeU40b2dweF9aYzBScEd5VHZXRmtBLUxYTTFkbzdheTFUN0Jrb0xiWklZWExlV0ZpRzZ1ZGlUNTlhaVdnM1p3aVdSdlRBUjk1eXBLRmRHemVUdk13WTRnUmU5bG5ReHREQkFPU0NxQmtRMk9qYXJpbk40cm82Mko1Y21oUGoySG1OeXZYZi1Ba2l0WkFQYVV2V2liWXc?oc=5) <sub>ROI-NJ</sub>

</details>

<details><summary><b>Momenta</b> (73)</summary>

- 📰 2026-11-12 [大众智驾四线赛马，HS8能否成为主流？](https://news.google.com/rss/articles/CBMickFVX3lxTE9LZ0dhRUo2ZVBhcnd0MHFBaHdYeUJlWDNncVJXWkxIcFRPdXdtOTZZdUc5dUk1N3lTR3FySTFoT3d0eEVHQkdGR0tFWWNMWUs3X21TbklvU1JfbW5oM0U5SHItRjU4aVNBWldsZ08tUlluUQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-12 [奔驰 CEO 说车要大，可中国在售最长车榜里全是国产\|Momenta\|奔驰_新浪新闻](https://news.google.com/rss/articles/CBMiY0FVX3lxTE0yZlVSZ1k5Rk9YNC1meEFieVIwQjhma3ZJRmJwR1pJeE1maV9XTmUzTC1nMzNzOENva0xERHVTR0NMUi1DNHY0Qjg1UFZyS3RKc1dPVWNPdExOQjZoeXcyWUNScw?oc=5) <sub>新浪网</sub>
- 📰 2026-11-12 [东风日产NX7搭载Momenta R7世界模型，直面复杂路况](https://news.google.com/rss/articles/CBMickFVX3lxTFB0cDJQQjFtaHQ0SnJJWkc4NGdYUmh6QVl1dHVWTHotYURfQ0VzRmw4Z0hUMFk3UGpnb0VpaFBxa0xURmNvT013em9PQS1USW41dEJIRDdsVlIxZkFJMTFkV2drbjJHcm9MYkliTHd4Um1kdw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-12 [奥迪E7X搭载Momenta R7世界模型，辅助驾驶这次能带来哪些变化？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1wM0JuOWhTUWlTVk1aRmlVaGxSWjBxMDRvNEZJWXR0ZHZMbjRubFVQdlRFOEZ2UU5XcTRqQVBVaWFLdEFtbHNoTGRsRzFaTERpQ3BDX2NiSl9fQlU?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-11 [物理AI第一股上市，车企主权意识觉醒](https://news.google.com/rss/articles/CBMiW0FVX3lxTE8yVWQ4TkFyWGt2VGpYd3R3emRISURZQVFCSnRObVJGYXJWUDRjb3BPdEU5MmhfQWI1SENXUTJIOTBGdTFkNmhLOTJOU05wN0s2ZVpDaktyRllHWDg?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>XPeng</b> (130)</summary>

- 📰 2026-11-12 [Nvidia's Thor Quadruples Compute, but Memory Bandwidth Lags: The Smart-Driving Chip "Arms Race" Needs a New Yardstick](https://news.google.com/rss/articles/CBMidkFVX3lxTE1WcGhZWE1iNDI2ajBpMVNUQmptOVUwOUdRSGZETlRHVHBwdmFzXzU5TVhmeXZTdmljMXdFRFRRYkZGRHNQMzN5bDlfNllxMElvTXdaUm40NHlwM1RZVVFjWERLdjRsc1NnaGNDZ3MydkVvbWFaV1E?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-12 [【视频】小鹏VS问界，同样是国内第一梯队，激光雷达和纯视觉到底差多少？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE11WkthRFZMX01FMm45WnNZMjZscjV4c3ZoZkpvVnhCQ2FzVEM2RXV4N29FSng0RXpXSkRmWXdjWXFXd3l2dDdZcXhmTVBrVWp2NlMyd0dTOTJtOU0?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-12 [预算30万选智能增程大六座？奕境X9/问界M7/深蓝S09/小鹏GX四车座舱智驾体验+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE45cTBBX1JIb2s1M0phT3VfdDZ1UWUwcmRfeDBHMnFXSTBQd3BtdkIzSVl0c0pSWEFCMzNqckZGaFVldzNtejk1WUJfZTVqX01tR2FJc2l2UDNvZnp6M3gxOGpzalJFa0I0c1JPTFZEaWVhUQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-12 [小鹏G9L领衔，4款热门家用大五座SUV横评：23万预算怎么选？+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE90RnVrZTQ2MW1kWjF6bHV0LTFBYXNXVmFlOTdJUlB0WThrdEM5cGxGYWdtZmRxdG90SjhENldydTMtZW9iWFR3LV9xSF9KWjRZUE9ta3pNR2otUDM4SmZn?oc=5) <sub>新浪网</sub>
- 📰 2026-11-12 [25万级大五座新车盘点：小鹏G9L、理想L6、智界R7与极氪7X怎么选？](https://news.google.com/rss/articles/CBMickFVX3lxTE5oSkltWUlxSnN3WU5QdnNvdHI5QXBVM2p6MlJuZUJaTVRWSXNlWTQ3Y3NPRlRfdHRvcy1SR2NnQnNWNDFmWXZHQlVodnk4aDk2LVBRaVRkbVJCN09CLXM1ZUJ6UUdLVTNrS2YxYXJ6WllBUQ?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>Li Auto</b> (122)</summary>

- 📰 2026-11-12 [Nvidia's Thor Quadruples Compute, but Memory Bandwidth Lags: The Smart-Driving Chip "Arms Race" Needs a New Yardstick](https://news.google.com/rss/articles/CBMidkFVX3lxTE1WcGhZWE1iNDI2ajBpMVNUQmptOVUwOUdRSGZETlRHVHBwdmFzXzU5TVhmeXZTdmljMXdFRFRRYkZGRHNQMzN5bDlfNllxMElvTXdaUm40NHlwM1RZVVFjWERLdjRsc1NnaGNDZ3MydkVvbWFaV1E?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-12 [理想OTA 8.7和9.2怎么选？易烊千玺语音包上线，3个维度说清该不该等+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFBUeGFhV3k3MEFYcDRiMURTSWFZQjhsNnd6YWFhU1B1cXQ5RHdvTUJDaGJXNWZYSVhBZ1kzWXM1eENWSVYxc01BYm5qYTZncE1xZ21va19yNWFmZGNjN2FZT1NQMU1jeGY3UUI4RWNudnIxUQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-12 [小鹏G9L领衔，4款热门家用大五座SUV横评：23万预算怎么选？+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE90RnVrZTQ2MW1kWjF6bHV0LTFBYXNXVmFlOTdJUlB0WThrdEM5cGxGYWdtZmRxdG90SjhENldydTMtZW9iWFR3LV9xSF9KWjRZUE9ta3pNR2otUDM4SmZn?oc=5) <sub>新浪网</sub>
- 📰 2026-11-12 [30万预算买华为智驾大六座：奕境X9、问界M8、奕派M8三车横评，谁把四激光雷达做成标配](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1EYmhlZmhobUhfbTFXSVJzUGhULVZhQWs5LTRPRjY1UHRKTGU4YkZoRExSdXZTNnF3S1hMamNhTU9QRTRITjNrRUQ3ZTBGWEpYMzJQR3NwRDZJTmUzaTRj?oc=5) <sub>新浪网</sub>
- 📰 2026-11-12 [奕境X9、问界M8增程版、理想L9横评：最近上市的高配置增程SUV推荐，谁把满配做成了标配？](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBIU28zSy1yRWgwSnBxNjdGZVJ2OTRNWVpGNzRBdUtYdDQ5SGRXVzhxN2cyWDh4aFBrdnZxNG1JeGZRVndpazUwUXBSN0lYYjJ6Y0FnRnpmZi1zbjBBeHhj?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>NIO</b> (90)</summary>

- 📰 2026-11-12 [China, UK discuss EVs after Beijing warns against trade restrictions](https://news.google.com/rss/articles/CBMia0FVX3lxTE1GNXdKRkVGLTNkWEZmRVJfZWZPUDdFd1JDOGx3aWs3d1VxNFFDM3NYbG85OVhMQWxCU1RXQTBYRXExdkk4dVhRcncwbXI2V1NmZlgybXBGM2VzOWZ6cWhFdXkyNFVqMmZYYVdz?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-12 [Nvidia's Thor Quadruples Compute, but Memory Bandwidth Lags: The Smart-Driving Chip "Arms Race" Needs a New Yardstick](https://news.google.com/rss/articles/CBMidkFVX3lxTE1WcGhZWE1iNDI2ajBpMVNUQmptOVUwOUdRSGZETlRHVHBwdmFzXzU5TVhmeXZTdmljMXdFRFRRYkZGRHNQMzN5bDlfNllxMElvTXdaUm40NHlwM1RZVVFjWERLdjRsc1NnaGNDZ3MydkVvbWFaV1E?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-12 [VW Anhui reportedly has no new models planned for 2027-2028 as ID. UNYX sales disappoint](https://news.google.com/rss/articles/CBMic0FVX3lxTE9abXQ5VGZMU2d0dkxyUFk2aGVFWWs4cktvd0dDdE1uS25EbGJNWW9BUjZwT0dvdXpwVC12aFJHVEx3dEFBcmNnSEtMajVRQmJxc0ktRUVWOVZPR3R4SmwtU1RmcTR4cUhjUm5UcVA3cUxaM2s?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-12 [GWM to launch Ferrari-rivaling hybrid supercar in 2027](https://news.google.com/rss/articles/CBMickFVX3lxTFBoNGYzcXRPUlgtNEYwY3R6YV90MkdPclRxcWJrNHhrUGJDbHE5bDVBWTZoUnV1NFp5eUloSGxkVi04WmpZX0ZYNVJpSXRMSTJtejhtUDQ4NmR3Q3A2cS02bzVhaGQ1ZGN4LUw5bTRNRHBxZw?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-12 [25万预算新能源SUV候选清单：小鹏G9L、理想L6、乐道L80、蔚来ES6怎么选](https://news.google.com/rss/articles/CBMiX0FVX3lxTE85V0NheHNjMlNGY0dQYW1UT3V6aDBHeXU2Wk1FWDhSY2NLaDZSLVpCU3ptNXZBaVMxbG1sdXVDUHJDaWZOcHpRYXl6MzVFNGFsaExtQkRaRzRVR3YzMzBn?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>Huawei</b> (189)</summary>

- 📰 2026-11-12 [GWM to launch Ferrari-rivaling hybrid supercar in 2027](https://news.google.com/rss/articles/CBMickFVX3lxTFBoNGYzcXRPUlgtNEYwY3R6YV90MkdPclRxcWJrNHhrUGJDbHE5bDVBWTZoUnV1NFp5eUloSGxkVi04WmpZX0ZYNVJpSXRMSTJtejhtUDQ4NmR3Q3A2cS02bzVhaGQ1ZGN4LUw5bTRNRHBxZw?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-12 [Nvidia's Thor Quadruples Compute, but Memory Bandwidth Lags: The Smart-Driving Chip "Arms Race" Needs a New Yardstick](https://news.google.com/rss/articles/CBMidkFVX3lxTE1WcGhZWE1iNDI2ajBpMVNUQmptOVUwOUdRSGZETlRHVHBwdmFzXzU5TVhmeXZTdmljMXdFRFRRYkZGRHNQMzN5bDlfNllxMElvTXdaUm40NHlwM1RZVVFjWERLdjRsc1NnaGNDZ3MydkVvbWFaV1E?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-12 [Inside Maserati's Unexpected Survival Strategy With Huawei A](https://news.google.com/rss/articles/CBMiiAFBVV95cUxQSUl3MTh4YTNIcElqVXo3QWZYS0RzaEIySENLemI2QkE2d3J1RmVLT0JPQTNjVW1xV3pVeldHSFhNNFFnZUh1NmZsRHcxZlFBWE1iUG8xaE5Pcl9IQTZtbnM2dFlaVFp2LVN0OW9DUWs4XzZjREZiVGZDZTlNdDU5cmJxTmFqZ3Q2?oc=5) <sub>ИФЗ РАН</sub>
- 📰 2026-11-12 [VW Anhui reportedly has no new models planned for 2027-2028 as ID. UNYX sales disappoint](https://news.google.com/rss/articles/CBMic0FVX3lxTE9abXQ5VGZMU2d0dkxyUFk2aGVFWWs4cktvd0dDdE1uS25EbGJNWW9BUjZwT0dvdXpwVC12aFJHVEx3dEFBcmNnSEtMajVRQmJxc0ktRUVWOVZPR3R4SmwtU1RmcTR4cUhjUm5UcVA3cUxaM2s?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-12 [China, UK discuss EVs after Beijing warns against trade restrictions](https://news.google.com/rss/articles/CBMia0FVX3lxTE1GNXdKRkVGLTNkWEZmRVJfZWZPUDdFd1JDOGx3aWs3d1VxNFFDM3NYbG85OVhMQWxCU1RXQTBYRXExdkk4dVhRcncwbXI2V1NmZlgybXBGM2VzOWZ6cWhFdXkyNFVqMmZYYVdz?oc=5) <sub>CnEVPost</sub>

</details>

<details><summary><b>Baidu Apollo</b> (31)</summary>

- 📰 2026-11-12 [百度世界 2026：萝卜快跑把无人驾驶做成了全球出行新服务](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9lSDh4ZUdHSTdGQjNEZFpZTDFJVGVuamRNdndvQWExOVJnUXQyZ3owSTIzTU5sakF2Mk5PbGpNWlEtN3BpVEFKdVlKVnljcTJBU1FqeVEtMzFhdkk?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-12 [百度李彦宏：今天的具身智能大约相当于2016年前后的无人驾驶](https://news.google.com/rss/articles/CBMidEFVX3lxTFBEal9NZExGTzFna2haSzdhSnVwR2VLZDA5dm81MjFmMXJhWFcwNEJXMTBxc0NzTEVFY2dvWi14d1Z6RUxkREpsNkd4N2JoSjdQMDVnMjgtbkFiRWJYejQyMUFYS3gtcGxtSXA1aUJLUVRjeU13?oc=5) <sub>金融界</sub>
- 📰 2026-11-10 [Kakao Mobility, Nvidia form Level 4 autonomous driving alliance; Tesla Cybertruck to be phased out](https://news.google.com/rss/articles/CBMi0AFBVV95cUxQSnM4VW1mOHpXVW0yQ0tEN25KT2RWTVJBZ1JUZ0FYNUcyYWZJRlg3YzF3ME45Yno2dXNPT3dVWnozcERjdnBZLXZ2OTAyVE1TcXFtSEFKYVFnXzV2aFFUak12Y0NWSU9LQVlKMzVUblJsbVljbjc0OFBaVXY2d2diQ2NpRGhFaTJfWDFOVEdpemNCVXBpSzYwWnNxQnRRNHVZc09OTWFTTTRZSTQtUGFFRmlTM0JHMGowNF9vZ1lRcEZ4QUFKbzlsaWdwZUs3SS1n?oc=5) <sub>디지털투데이</sub>
- 📰 2026-11-10 [百度Apollo World首秀，萝卜快跑2.4亿公里全无人](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9IOHlYeHpXSnBsX1RQMFA1ZV9BclR2TXI1WXVXS0FvOVVVRlVTNGUxaVQ3YnY4UWtGa05SZmtHYi1seW10NV9adkRLLW9LZ3lBa2p2M3VRZlVNbGs?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-10 [萝卜快跑28城落地，百度Apollo World定L4仿真标准](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBIX01CdUNMdW8zZG9CWFgzM0RpSWFQQ3FjQjdKazFOQ2R0eXpKRFIwZXdvOHZ3b3VVOEI2WGR5R0tqNWs5MDI4TDJIYUJ4bnJUQUVqTWtUUmFwN00?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Pony.ai</b> (59)</summary>

- 📰 2026-11-11 [2026 Robotaxi 开始收费运营，国内 L4 自动驾驶玩家进展如何？](https://news.google.com/rss/articles/CBMif0FVX3lxTE5TREtocDVDN05vaEJUTm4tbWRwNXp6d0JjOFJiczAzbXp0UVNva09WVHliR3dVUWdBLUc0bG1mZTROLThybkt2cnRLY19kTEd4aHl6UDUtcmtNUWl6MkI1ZFRyM21VWjNpcTRjS3Z6S21lazZsMVlSeGctNGNLU1E?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-11 [Croatian robotaxi company Verne prepares a Berlin launch](https://news.google.com/rss/articles/CBMigwFBVV95cUxON2NLcnBOQkVaQWozTDJDdXoySGFvMkdTdGt0QmFuVlpwWUxPRTdsSThzUGxyMWFnOW9hb3FxRVJ6Ml9Za1ZaU0VMczJsZnB1Y196Y3JfMHJ6QmltakE2WVQtWDUyY0NUQVFLb2xINEpsQUU1V1JGNzdLRnVFMkFfWGxlcw?oc=5) <sub>MLQ.ai</sub>
- 📰 2026-11-11 [Verne robotaxi service prepares for launch in Berlin](https://news.google.com/rss/articles/CBMilAFBVV95cUxQMlBtOGpPNjVkOHNuTENGLUNaR2sxYXlpSG9heWJ3b1lndS05ODZMc3hlRHU4bVdXaVg0WThpLVk0YkNHV2phcVNpb1BUWFZKckU3UUpIODg1SWF0dFVVMFh6aUJVUEszOTdyUW80Z2pXRVctZlJYbjByU3JZNDFzYnc3aDNKcVgtVEl3THJMVlpRZDMy?oc=5) <sub>electrive.com</sub>
- 📰 2026-11-11 [24公里46元对23公里77元，小马智行与网约车实测对比](https://news.google.com/rss/articles/CBMic0FVX3lxTE5lVFRZVnpFSlNmUjV1c29leUJ1YTY5OHROVkItUWdncDJ5V2o5bkZfTkFYTmphelhvallwVjhNQjdtMlhpcG9keTFpR1otaUstV1A5ejRfV0hsWThncmVTY21YYUd2dms1RnhBWTFXSGl5Y2c?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-11 [Robotruck赛道全景：全球及中国的六类条路线样本——DeepWay深向科技](https://news.google.com/rss/articles/CBMiZEFVX3lxTE1qcmhrb1lWRFF6bUxIM2hDYURadEVjOUgwazVpU05HUXlEQkk4SXdzR0xIUW9ndTN2NUlCUW04TGRlYXpSYUZYUHlVTklJSlowaHFqR3hCd3NkQ1dJTUI1eDd2Z1U?oc=5) <sub>衡阳新闻网</sub>

</details>

<details><summary><b>WeRide</b> (72)</summary>

- 📰 2026-11-12 [破解完FSD，还说技不如人，特斯拉破防了](https://news.google.com/rss/articles/CBMipwFBVV95cUxQWklONEp5c1h3SkFQLTZuMnFzdTIxNGhkVWhVeS1mOWFRWDFVQ0I5RDNGUHhOT1RuUnV1QnRmVFZ4aWktYzZFaGdQczNMSU10R3l1NDE2RGlReU4wNGZ4SHhCOE1DV2hMdWt2ZkxDRWVieXZ3dHdJMVlIeG9INHJhWWl3RDdKYkVmVWJEUms1TkNsQkgwTTA1dTYzMkZHc3ZuZENmWXNNVQ?oc=5) <sub>新浪财经</sub>
- 📰 2026-11-12 [13款新车扎堆，年底买车先别急](https://news.google.com/rss/articles/CBMia0FVX3lxTE8xRi1xQmI0M2hsVFQtS2hxVzBtWFBjUHFPMHJWODhYX3RDc3NTdmg3ZUI5NWZZcklaSE1keVMzUnhaTWwwZV9HMVgyM05CNlMxYjB5alFDVWtfbHRyT2hxUjMxOHV4NTJYOFdn?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-12 [【图】升级800V平台/现款售9.78万起 新款零跑Lafa5将于广州车展上市](https://news.google.com/rss/articles/CBMiYkFVX3lxTFBBejhURDZtYnoyOHdFRGQ4MDJmZnYwUmN0YWljc3N5eHhiXzc0TFlkMFZKRFZiVVNITHJVS0RILVhLTmcyT0c2YzV2WUVNNWZLR0J3WHNZMjBDbTBDMm50ZHhR?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-11 [2026 Robotaxi 开始收费运营，国内 L4 自动驾驶玩家进展如何？](https://news.google.com/rss/articles/CBMif0FVX3lxTE5TREtocDVDN05vaEJUTm4tbWRwNXp6d0JjOFJiczAzbXp0UVNva09WVHliR3dVUWdBLUc0bG1mZTROLThybkt2cnRLY19kTEd4aHl6UDUtcmtNUWl6MkI1ZFRyM21VWjNpcTRjS3Z6S21lazZsMVlSeGctNGNLU1E?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-11 [启明周报 \| 启明创投投资企业要闻十条 Vol.35, 2026.11.11](https://news.google.com/rss/articles/CBMingJBVV95cUxPN3VuVEs4SUEzN3drNU8zODgxOFo3UVZQdGZveEtEdHVWc1pMRmJ3UkVtVzc5dGJUUVlsSnJWM1A3S3doZWJkbHhsZTVQRU44WDVqOTB5SUFSd1VyU2R6SlhvOUV4OF9IRUMwRnh4RGFKMUdmTXFkUFVfcC1DbTF3S0Q4dlJPMzk5VDZzcFNjZVNzRHRfWTNNd3BfYTlGUVMtUWtYeXQ4N243cm5wdE95MVBid1dmVjNfbHNyQXlXZzRSMzJCbTVqb1lJdGZiZHhfbDdCSC1hT2NHVE5IcE9sYmMtRThnNU9LMHlTSW0zVkZOdC1ZWHhqSDdmTHkzamNTLTdSRkdiczBWVHlCLXJEX1FkSXpBbjB0UElpX2p3?oc=5) <sub>启明创投</sub>

</details>

<details><summary><b>Horizon Robotics</b> (50)</summary>

- 📰 2026-11-12 [Nvidia's Thor Quadruples Compute, but Memory Bandwidth Lags: The Smart-Driving Chip "Arms Race" Needs a New Yardstick](https://news.google.com/rss/articles/CBMidkFVX3lxTE1WcGhZWE1iNDI2ajBpMVNUQmptOVUwOUdRSGZETlRHVHBwdmFzXzU5TVhmeXZTdmljMXdFRFRRYkZGRHNQMzN5bDlfNllxMElvTXdaUm40NHlwM1RZVVFjWERLdjRsc1NnaGNDZ3MydkVvbWFaV1E?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-12 [大众ID.AURA T6深度评测：12.99万起的中型纯电SUV，家用能闭眼选吗？+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE1zUnNCUVp0Q1ZoZ3VUUXQ2dklTTGVRZjRGQlRoS21OQ0xTa3ZCMlRjMUlfUFUtNkZGTWVLVlRPMHNNaTRpSE44T1owaE5mVmUxdlNaQ2JldUVSWmlWaEdmLXVjR085VVoxdGcwLWJxdFhQUQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-12 [【视频】iCAR V27 全能家用硬派SUV，颜值实力双双在线](https://news.google.com/rss/articles/CBMiW0FVX3lxTE4zZ0t6NjlGdk5kcU44Q2laN2NsTWZ6c1g1RTZFMVBjUXFTQnUwTWlIaDdlZW41SFdyczN1VHRtMnM3SlVySkpYLXk3VmFubjRVUXE5dUNTUEQ2RFU?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-11 [VW China EV sales climb to monthly record in sign of turnaround](https://news.google.com/rss/articles/CBMijAFBVV95cUxOOGpwWUJReGFkWE0zdlZlZGlJSUxxRWJKdUtVTV9nb3UzQmZ3QUpfZTI2NnFRN2pMalY1LUQwYjJRNG5PclhWNFlNTXZodDhOV2Mza2w5blRNR1pLVXdzX1RJZ1dyR05NdTdlRUFuak0xSzQ5QUM5Q3hFUFE1UjF1TG0zdEgxMXlNVWxoaA?oc=5) <sub>Automotive News</sub>
- 📰 2026-11-11 [Exclusive-Volkswagen’s China EV venture has no new models planned for next two years, sources say](https://news.google.com/rss/articles/CBMixAFBVV95cUxOS0E0dkpwcG9LdUtoWFBOTXBEb2JWWGJUdDJicG1pQlUtNk9HTkZkSVlvUmRBTmZnc21CWVFySkNmWEd1MjZZVGRSYklkRGdpVC1ybElQT2dQNEx3MkZFWFo4dm1Ic0l5X1VjMTdBTE9NZVBEYjlCemFvOEQyNUcxX2kwbnAyMGg4dXpmWTZ6YmNveWFuSGZZWGhzdlJrZDVkMmV0bFpzYkNJaThuSGZaOENPcjcwZDUtV0pzZzBoUGNjVVNH?oc=5) <sub>WTVB</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (21)</summary>

- 📰 2026-11-11 [【视频】特斯拉发函，媒体CEO：放马过来#特斯拉#埃安Ray7](https://news.google.com/rss/articles/CBMia0FVX3lxTE5xOHhzcEd1V1RKWmxPZ3BEYUN6NGRhOXB2cHFXSWxFNGEzdjFPbkotY0VMQlpGTGxyV0FCc3p3S1NkU1NjSjI3b01nN2FTcnl3blB4dC00UGlQNlk0Ukp4SEhIYUtSVXNhRlQ4?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-10 [【视频】Model Y L 六座家用｜一副好脚垫能省多少事？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE92blRNM1I5N0tnc3BHSmRid3RwcFIwNnMtYWJwTkcxZ1Z4RDVjTVRzS3hvUm5BMGptOGNSelRBdWM4cW9ZZWtNMHN1Nm9lUkNtdnB1aUtiVkVyREE?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-10 [官方预告已发！smart #2 BRABUS，比你想象的来得更快](https://news.google.com/rss/articles/CBMiXkFVX3lxTE5Nd2ZtYXF4b3pfdGJ6dEdBTVcxcS1zeUIyNzA3bzNTRFI0bmgydlJJYWplR2ZNYXFDQTlsLUpDS1BLdmJ4bThYdU1RNjM5VUR2NnlvNEJMcHBScVBzekE?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-09 [雨天接娃四车开过，赛那四驱油耗6.1L，两驱版差距在哪？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9EbHdKOVNtb0k5TEhKbkxJSVZFOWxZUXZlS3kwNWtLcTBxcTJmc2RBUEVHTzRzdzBOS3N2Z2JmZnpEZzQxbVlXR3pKeC04YzFhWnRRUGRZOVY2Zm8?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-09 [DFF Partners with DP World for Development of Autonomous Logistics Solutions](https://news.google.com/rss/articles/CBMirwFBVV95cUxNQ0Zpa21lNWZ6bjFZdFdnY2NIWmNuLUJIMTdTZGhtZVBDZzZ4NVRjWGthUnhWSmk2emlDVWdFQXdSYnBkR2NUSkVya0dJTEZyUUltdlBmWkdjUmprZUVYcGpTV0w2cXBVOEhLTTJhNDVYVHlXbklnUEtUbHhLWWRMaFJ5WktuUVA2dkxsamM2Vm9aa1lXaG85dkJJOUh4cHhZMkhkRDdGMlBBdzZOamlF?oc=5) <sub>Future Transport-News</sub>

</details>

<details><summary><b>Mobileye</b> (13)</summary>

- 📰 2026-11-11 [Mobileye Announces Participation in Upcoming Fourth Quarter 2026 Investor Conferences](https://news.google.com/rss/articles/CBMiwgFBVV95cUxOR29NaGt3LXBWY1o0YTZEZXBTaGhySjAycERjTVRxcEw1RjhXT21tb2hxbGk1ODkwWFZlbnBkdTE3ems3dW0tbWlUaUpUNUs3T0VJeXlBUF9wUGtLeEtVRGNnQmVsUWQzZEJxeHl4OGdiRjFpbGFkV3JEM3Vwb1NRVDZGc3EyZUpIQXpyV1NBckR2MG9sZGRvZWJRZk9ycDdrYWY4ZmtIS2pSUmpuZFFvX2V4VUVJXzZaS0xrQkNCVV9JQQ?oc=5) <sub>Quantisnow</sub>
- 📰 2026-11-09 [Nvidia Scandal Sparks Auto Industry Watch](https://news.google.com/rss/articles/CBMidEFVX3lxTFBUSkZrRUk0TktpdFF1dEthaHQzMFdVRXQySHRMMXFwT2s2akhzT183RFlib2NuZG9lNkVoUElrOWFmbEx2OUNUY2ZhYlROQWRyZjN1eDFXdk9ObmFYQkdOUzNNM1FCazUwVWJRbWZILThIM1RO?oc=5) <sub>Businesskorea</sub>
- 📰 2026-11-09 [Maxwell AI Cuts Code Costs 67%, Runs 38x Faster [2026]](https://news.google.com/rss/articles/CBMieEFVX3lxTFBlMjEtN1BpMTdFQ1JKOTBKQjBvaFV3V0dISVg4SGtlQS1YczlwRFJsRHFEWTl4eHRiak1wYmVnS1lEMkhGaUpmNks3eUU5ckExSl9DekNyLTNhSHRNcllrSXNSbHFzMFdDUHZPVkljalNlZTV6c0R0UA?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-07 [Mobileye Global (MBLY) Lifts Guidance Following Earnings As Fair Value Debate Returns](https://news.google.com/rss/articles/CBMi0wFBVV95cUxNOF9fMHVEMXdjcUJ1ci1PZ3hqNnV3SHVHanAwSHc4TzJvTnVPSnlxYzRaekFoLUtETWdTeVFVNzNFY2U4SnNxczlUVjF2bEE4WEFPcXdDRjZQWnhKU0J0ekFGS0l2cnlLVmZTN0o4MjFSMUgwOTJ1UkEwQXREdnZXbTM3VmNpNm42YndkTHBGT2prNENPZ1JHTURJRy11a19YRjQyc1B2V0Y4aXBVamRXeFpzamRYWWpWX1c4eXpWYmdiWVIwUVRYck1OUXZjTElGaFM40gHYAUFVX3lxTE5nb2VZYnRkMGY3a1l5UTJTU1ZJUndzc1VjWHpicnNpRm1pdURTMUwzYWJYeVdYRy1kNVh3UjNub19fWm11eTVLSGVUVEJFTlBDcHExWFhBWFdPZDdsY05FRS1kUEtoRi1RVFROcjIzalJmdVA2amlrOG5OSmtlMUJtMlo0S21IUGpaRXE5b1JvV0xCaEo0OGZPaW9UeWQ0bEZ0d0VQU1Y2b2QzQnh2YzVaSTIzVV9pTUJOUy1BM1puZ2N0SUc0SzltUnotUU4ySDlfR2psMm0tSA?oc=5) <sub>Simply Wall St</sub>
- 📰 2026-11-06 [Mois Navon: On Mobileye’s Success, AI Ethics, and the $15.3 Billion Intel Deal](https://news.google.com/rss/articles/CBMivwFBVV95cUxNZWE4YU1udlFHX2tSMHFJWERQME5TMk9FaVBxRUZjbm81MlVjZDU2V25FRS1DVFdWV3lHZ3IzaUJLaHBsZnJHN3pPLUt0QlhzYU5NaXpkZ3ZDZGVEdGJNb2ZjRFV4MUk1bXllek45NVR3NHFITFY5RUZESE1qUWZmbjJsYnE0eVFtWXRYYU1iM2VwTmZoanZPT0doUUxyY2ZpeDAwLXRzTENQRzJKZXJYNDNheVcySGRRQnlDaURHbw?oc=5) <sub>UA.NEWS</sub>

</details>

<details><summary><b>Aurora</b> (26)</summary>

- 📰 2026-11-10 [Kearney, MIT put US driverless truck cost parity at 2028](https://news.google.com/rss/articles/CBMihgFBVV95cUxOaUF2Mlg4M01hbDlhZ1EzMkxsNHpyLXExUk5SMzVSaWFYMU9va2EtWm5jeWk3VGV3RWRzekREalZFOXJsajFabHppYmlCZUw4cEZNNndoSGFwQlc5cTFkcEhFMTl1eEtZMjUzQlc3V3Y0OWxlcG5GeEFCZm5Qc3kxdWZ2ay16Zw?oc=5) <sub>FreightWaves</sub>
- 📰 2026-11-10 [Wing to Invest $125M in U.S. Manufacturing Footprint](https://news.google.com/rss/articles/CBMiuwFBVV95cUxPTnBYcDRkNXRuNUR4RXlPM0hTV2lYRlJHYXdCQ2RldmNiZnpLbFh2ZGhtcTJJNU01LUxIUnB1Q1ZJOWZFWWtyd2ZJQXYzbWdvWWF2QmdrZmNUS2x4SDZHR1VJU1lseTlMSS1BUDFyVk1keDhPMVB3S1pLejU1dktkX2JmWTg1UzFvWHZFcVBUVGdHWGxSbUQzVVVmWEdFUTFEcjl6Q3BqcS10c0xndV82dF94eFQ1VjlfaVBj?oc=5) <sub>SupplyChainBrain</sub>
- 📰 2026-11-10 [3 Great Penny Stocks To Own In November 2026](https://news.google.com/rss/articles/CBMiwAFBVV95cUxNV0xqQzBNSldFR2FoVnJYT1NvcktEZWd2Q2NRblRpdzk0VjhZRndZeHBBaUlRU1FPaWJIcjNGOF9NUFdRYzhndjFJSmJTMUI3UDNFRktOOUhVRFZ3cFJ4ZjFPekVsZTFKUUhydF9DNk8tV1F5U0JINDZEcXdRRnFXYW5CZG5GTWt0cmlYRFRsQ2ZwZkFxMmk0eGU5emR1eU9wNGtOWllKS0x3ckpjVGgxYlRTNW4tei1nU2sxcXREMnTSAcYBQVVfeXFMTUtKV2NJSXpfWlpVLTh0TWgzdExHdGwxOGZmdlFyOXJ4aTZ2Wk5DQzdfc3BMU2UySXQzNlhjdWZlVE5sSTc1Z3NyU1VVOW5NTkkwQVZ5cHlZMjdBRUFYMjVmRDl5NG42LVI3ZlpCTkpaNjZtcnNYNTA2OWpqTG1ReGlMaE4xWXhvNVJ0b0Q2RjlMbTU5RHRXYVdBTlY2cE5tT0p0LTNtX0xnTy0wYlVIMGREaWkwdWpiYVl5dGl3ZXE0MmF2eUJB?oc=5) <sub>Simply Wall St</sub>
- 📰 2026-11-09 [Opinion \| Truckers hate these jobs. Let driverless trucks take them.](https://news.google.com/rss/articles/CBMipgFBVV95cUxQM0k0WWkzYlVsOFdpbFNSZmJfenVKeV94ZkFCOHZRZmZhM1JfUlpaVTUwcnVFNDJkMjJBWlhIb0lhdzJsa3Nodnh3N19tVzlRcXFJZFN0ZU5MZmlnV2hYZmZ4RV9BZmVyRE01ZVhydjg0VlZBUkp0NElEM3BGTEhuNXpNa3F3UC1rRkg1R3czdWZQQWFNa2VoWXkzbkhiOFl5RGxUMUt3?oc=5) <sub>The Washington Post</sub>
- 📰 2026-11-09 [Clark: What fleets should know about autonomous trucking](https://news.google.com/rss/articles/CBMi1wFBVV95cUxQRldXemJMcGs5TnpOalV4d1g2aEdDaTN3aGRZS1pQSHJzbFRBY0FOaTV3VHlCMTJZQ1NDZmo3UFpaRjhtSFNKZk9uYk5VN1VUSDlDamFhY19vWktyd2pRVmtuN3lUV2RLRGZINWpLQ05wQXVIZzdGd2JrRGk2NEl3aHNlNGJMWFY5RzNiR25NRkQ1NmVCR2dPNXhDVDVNQTVTeU4tOGlqT2FERXMzdHNudzVNRmd2S3hiNWliRGd6QVJERjB5NWh3dzZKZ3ZKdjdLTTc5alZTUQ?oc=5) <sub>FleetOwner</sub>

</details>

<details><summary><b>Zoox</b> (38)</summary>

- 📰 2026-11-11 [Tesla Robotaxi Media Control: 3 Claims Unconfirmed [2026]](https://news.google.com/rss/articles/CBMikwFBVV95cUxOVkRrNzdUSTFyS3VlU1NlUG5KVXU3bzBXcVRyYlBXSVdMUFNFU0thNVFLeFg1T3FjRU9kc3d2NTFqSFFfSk5iSEg1WEhNOVd2QXB2OFQySV92UU5QWmJBbmtXTzNsbzBPUGpzRFl1c3VrZ1hGbWc0VHNNUi1sbWdGdXFwbUxHZy1kcUN5aW9hcUI1b2M?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-11 [How Much Is Tesla’s Robotaxi Actually Worth?](https://news.google.com/rss/articles/CBMijwFBVV95cUxNWE9qRm5GRm00cElFVGJId0ZvRUxwNGwtN1hOWHJRcG1LTzhhbVlvNzk0M3h0Q2tBdFJNNkxONGV2UjVqdVMzR3RQUUllYUtpY1BiNkZYdEo5T0FpdVVmZk1hZG56aTRYYkt5ZXBXWlFhVmI5d3BQM1ZnNWlob2Facks3MXEySnFHM0R0Q0tSNA?oc=5) <sub>24/7 Wall St.</sub>
- 📰 2026-11-11 [Alphabet Urged to Buy Uber in $180 Billion Robotaxi Play as Waymo Ties Loosen](https://news.google.com/rss/articles/CBMidkFVX3lxTFBXbkdvdjVTWnVZRVoyQ2xwVVBVaG1RX1d5bC0ycU1MRHgtck1uRVQtSVVkVlJ0LTVHbVdQaF9LUVBiVlpLT2trWHNIQ1RfRTl0eFJjajVJaUVjdFNRLWU1bW1vU0JqQ002THR1Nzd5RGZiczR3RHc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-10 [Revised DC bill would clear path for driverless taxis, but does it have the votes?](https://news.google.com/rss/articles/CBMiygFBVV95cUxPbENFNTM1MmNYd3JCRnlRVmJ4Nk82bmVGTEgtLVVQYlBvU2lWRXRIS25Bejh0LTExSG84SkRYSWgzUDBsWEY0dmwyTDRvQWVSM2c5THRWUXZuMExIRFBSZ3VyTFRsdlNMc2RvQ2VHS2xyNEFHVTgwTFE4S3J5QzZ6WWxGcUNpNFoxaWhNRTEwLWotWENBd0RrVG81YWhXU2hpUW8tV0xVRFNSU2pIZHVWYzJfTmRYVFRzd0xVREdWZFBkN0MwbW96R3lB0gHSAUFVX3lxTE05QlVWTWhsbHE0YVlONFRWakI3OVY3YnlMdENVOVF0SkdBUmFBREI2YXU1Rk5ySUZvQUVnNzR5NnNkVFA3RmhzekVQR29FaW16UDZYLXBHb21YRmg3WnlOOTFVNVBQaDZPeXRXbDNuYlNHZDRROUgzYWRZQVUyRnZweExLS2xGMG5MNlFrbmNKekNJNWdNTF82SkRiWFlKTlhIWUFLSnJqSE5NVXF3dXBMcnRqVEEyODlKdG96LVRWd0pXZVFkQldfbk4yaXFvTmlVZw?oc=5) <sub>NBC4 Washington</sub>
- 📰 2026-11-10 [Business briefs: TGI Fridays plans return to Las Vegas with five new restaurants](https://news.google.com/rss/articles/CBMilwFBVV95cUxPT2lSNldLdFp0QXdiWHg1akt5cFlwOUFGMTNhV2RtRzJwY1J4OEdVYmJxVFhKVXlUaEpWTGNtRTRBUW5MR3VseHFJR0o5R0FaSURVSUg5TC01Rnl5bTJRZWQ5T2VlMkd0SVVyZVI2RGdPOW1Lb2VDdWhObFZBaWNlY21OQVR3Z3BGYl9MbnVMWEFtNXpnN2lv?oc=5) <sub>Las Vegas Sun</sub>

</details>

<details><summary><b>Motional</b> (13)</summary>

- 📰 2026-11-11 [Korean firms shift CES focus to industrial AI](https://news.google.com/rss/articles/CBMiqgFBVV95cUxQQVpGVm5oN2E0dXpVQ2tfaXVaZXlZanNWcllzRTJCc19OS0F3V2Z1eWEteEpub2dQWWJleEtYMTVyVkRGaVpmWmwwQi12V0JhdjlvRENjU3JWMlpLTkJkOHhMYl9JeDh0RU14Mm5fZmx0X1Z4NlJTYmtKNkc2ck4wT3pQTUZxYjFmQ2M5a1ZoTC1WSmZOOGxMOGJFakVoTm4tcTNaekZZdVFWZ9IBqgFBVV95cUxQQVpGVm5oN2E0dXpVQ2tfaXVaZXlZanNWcllzRTJCc19OS0F3V2Z1eWEteEpub2dQWWJleEtYMTVyVkRGaVpmWmwwQi12V0JhdjlvRENjU3JWMlpLTkJkOHhMYl9JeDh0RU14Mm5fZmx0X1Z4NlJTYmtKNkc2ck4wT3pQTUZxYjFmQ2M5a1ZoTC1WSmZOOGxMOGJFakVoTm4tcTNaekZZdVFWZw?oc=5) <sub>The Korea Times</sub>
- 📰 2026-11-10 [Tesla Fort Worth Robotaxi Field Report｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1aT2xVRzVDa1RNSDEwb0FuOTRwU1lPenVGSmhER1ZoRmJJdTZpeGlaNEt6OEN1SWxKYlBUS2N0aXprRnBPQ3NxVjB5VG9maVNGWHVWU2VwbW45UWpJS0xB?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-11-09 [Nvidia Hardware to Run Kakao Mobility’s Own Level 4 Driving AI in Kia Vans](https://news.google.com/rss/articles/CBMiqwFBVV95cUxOdnhiQkNMYk5WWWNtak9OVFdvdjdJYzNQT3htNzc4MjFiemlCRVpSaHJQUHlqd1N3NUVQZ0pESjBHWXZpR3RkdDVqNDhTc3RJd0l1ak96OXRFeEF6T0o4bWdnNHA5dDZjTEhWQjJobWtmY1JXMXItQUdtdUwyeE95WFR2Znk1dGI2eXk4N1hXMmxvVHFxU3J6R1l3Z2hpNEdmSDBTZjl1M05HaGc?oc=5) <sub>Electric Vehicles</sub>
- 📰 2026-11-09 [Jony Ive Shows The Real Process Behind the Ferrari Luce｜Cleo Abram: HUGE Conversations](https://news.google.com/rss/articles/CBMiX0FVX3lxTE42VWFqQXo4YTIwQjRGbk4xZjZ4Rko5MkNmMFZ2OHlEZGZpaURkM2NhLVRNSG02M0NsS3RIaTJ2WHlEVDRKY2U1bFdjZ0NLWjZJblhHVzhuQzdXYzZTeHZz?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-11-08 [Tesla Robotaxi Orlando Field Report｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5ObkNyUS1ncHVCU28ybkRSblpObzVkeGRqaEg3dTRRcWIwTFdCV0tyRnNMeEw3Wk1oRVhZM1g0OW8xSkdxYU5rM2NfLWo0SV9heXRKSnZRd3Nwc3FnRkxZ?oc=5) <sub>finance.biggo.com</sub>

</details>

<details><summary><b>comma.ai</b> (4)</summary>

- 📰 2026-11-06 [Canadian YouTuber Linus Tech Tips Tests Tesla FSD](https://news.google.com/rss/articles/CBMiggFBVV95cUxNZVZaT1Q4X0NlakJzTnFkTGdqTmFPM3pDbFZPUnBYVVNrVzFxMlpZQ3VaTEJFUmJrNVpjMmZ5RVphUDE4WURNT0x4NkhnN01LdTdzSEVnS2NUNkROams2cnNzNkpnalhWcDVuckhETUtxaDZrSHNXTXhKYUlpN2dPTlZn?oc=5) <sub>Drive Tesla Canada</sub>
- 📰 2026-10-29 [We Upgrade Our comma three to a comma four: Is It Worth It?](https://news.google.com/rss/articles/CBMimwFBVV95cUxOVkgtNU9hLXVYM0U2VjNpVldsNFFoQm53SjJGcU1CcnNMWXY5YzFYdVhoYlNZdG5vX21Va2h4b2RLYTNEUTBLdUFhMXd5eTVjLXBSTHE5bFN6elNqa1diTThPQ0Z0Mlo4SldDTzQ4eGxEWl9NTjNKcUNGQmhLeGRSMUxOSElpMkVNOTN4QWhMV0hPRFFJV3cyeVNLSQ?oc=5) <sub>Transport Evolved</sub>
- 📰 2026-10-29 [Aftermarket Self-Driving Devices Face Federal Investigation Following Five Crashes, Three Deaths](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPUG8ycGN4Tl96dk4xZk1yTEJrVkpvVGNsX2JnbWJoeXlzS1ZsVDlEYWk0SnFQQTZXQXpfN21BU20wR1FmR1lsUFpoeHdzU1BUaGdheTZ3LUFkVnpaOHhyWUU0YU1yWERQYmI2TDRnd1VpbTM3Ui1yWFdQVzZIRHVrUEhZUFBKcGpM?oc=5) <sub>AOL.com</sub>
- 📰 2026-10-29 [A $1,000 Device Enables Hands-Free Driving. But Fatal Crashes Have Prompted Scrutiny.](https://news.google.com/rss/articles/CBMixAFBVV95cUxObnRHUXNNS2wxNVFWeHVLdm9qYmZ1bnpaUVN2VWJ1eHZhbFRiWGxoVWxaSjNuNzNKQXZ0RV80dVRnckFGc003eXZJeW5ZWkhUakpsdk9sQ0lnQUZZeVNGekRzYmhvR2RrU1Ric29JeUFmQzNNdEE5NEtZLUgyS2hmQ1hwYWlMdFNDRHNZQVB6dHNqUjIyaXpRMFd2c0YxN0c3Vk9yZF9kR255QmtTUlRiaEtYbDY1dHVZQm9ReHY5WUdMSzJQ?oc=5) <sub>WSJ</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
