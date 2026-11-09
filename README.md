# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-11-09 · 1,284 papers tracked · 45 curated.

**Selection rule.** A paper is listed only if it (1) is primarily about autonomous driving,
(2) has public code, and (3) shows at least one strong signal: accepted at a top venue
(CVPR / ICCV / ECCV / NeurIPS / ICLR / ICML / CoRL / RSS / TPAMI, or ICRA / IROS / AAAI / RA-L),
≥200 GitHub stars, ≥3 citations / month, or a well-known lab with traction. Papers are then ranked by a
composite score (venue, stars, citation velocity, LLM rubric for novelty / rigor / impact, SOTA claims)
with a per-topic cap. See [`scripts/rank.py`](scripts/rank.py).

📅 [Daily digests](daily/) · 🗓️ [Weekly digests](weekly/) · 📦 [Raw data](data/)

## Contents

- [VLA / VLM for Driving](#vla--vlm-for-driving) (12)
- [World Models & Generative Simulation](#world-models--generative-simulation) (5)
- [End-to-End Driving & Planning](#end-to-end-driving--planning) (11)
- [3DGS / NeRF Reconstruction & Sensor Sim](#3dgs--nerf-reconstruction--sensor-sim) (5)
- [Perception: BEV, Occupancy, 3D Detection, Mapping](#perception-bev-occupancy-3d-detection-mapping) (7)
- [Motion Prediction & Behavior Modeling](#motion-prediction--behavior-modeling) (2)
- [Safety, Robustness & Evaluation](#safety-robustness--evaluation) (3)
- [Industry Tracker](#-industry-tracker)

## VLA / VLM for Driving

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Teaching Vision-Language-Action Models What to See and Where to Look](https://arxiv.org/abs/2607.01658)<br><sub>Yuguang Yang, Canyu Chen, Zhewen Tan et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 37](https://github.com/ShivaTeam/DriveTeach-VLA) | Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving |
| [DeepSight: Long-Horizon World Modeling via Latent States Prediction for End-to-End Autonomous Driving](https://arxiv.org/abs/2605.10564)<br><sub>Lingjun Zhang, Changjie Wu, Linzhe Shi et al.</sub> | ICML 2026<br>2026-05<br>📑 3 | [⭐ 31](https://github.com/hotdogcheesewhite/DeepSight) | End-to-end autonomous driving systems are increasingly integrating Vision-Language Model (VLM) architectures, incorporating text reasoning or visual reasoning to enhance the robustness and accuracy of driving decisions |
| [SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving](https://arxiv.org/abs/2610.20609)<br><sub>Shaoyuan Xie, Zihan Zhang, Jingxuan Wang et al.</sub> | CoRL 2026<br>2026-10 | [⭐ 35](https://github.com/ASGuard-UCI/safedrive-vla) | Vision-Language-Action (VLA) models are gaining attention in autonomous driving, inheriting commonsense priors from large language models (LLMs) and widening the navigation interface from a fixed command set to free-form… |
| [Scene-Adaptive VLA: Efficient Autonomous Driving via Dynamic Layer Routing](https://arxiv.org/abs/2610.24590)<br><sub>Yujia Yang, Quan Yuan, Jiawei Fan et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 4](https://github.com/yang-luvu/Scene-Adaptive-VLA) | Vision-Language-Action (VLA) models offer a promising paradigm for autonomous driving |
| [CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving](https://arxiv.org/abs/2607.04179)<br><sub>Zhaohong Liu, Hao Ye, Xianlin Zhang et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 1](https://github.com/MICLAB-BUPT/CritiqueDriveVLM) | End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving |
| [PixelPilot: Scalable Vision-Language-Action Models for End-to-End Autonomous Driving](https://arxiv.org/abs/2607.04637)<br><sub>Pin Tang, Guoqing Wang, Xiangxuan Ren et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 1](https://github.com/VISION-SJTU/PixelPilot) | Vision-Language-Action Models (VLAs), which leverage the advanced reasoning capabilities of Vision-Language Models (VLMs), show promising generalization in complex autonomous driving scenarios |
| [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)<br><sub>Nan Yang, Zhanwen Liu, Linfeng Zhang et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 11](https://github.com/Zizzzzzzz/MVPruner) | Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings |
| [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)<br><sub>Yuan Gao, Wenting Miao, Mattia Piccinini et al.</sub> | IROS<br>2026-07<br>📑 1 | [⭐ 31](https://github.com/TUM-AVS/Chat2scenic) | Validating autonomous driving systems requires diverse, regulation-compliant test scenarios |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 18 | [⭐ 546](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
| [GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives](https://arxiv.org/abs/2609.39601)<br><sub>Qize Yu, Lianrui Fan, Boyu Chen et al.</sub> | arXiv<br>2026-09<br>📑 3 | [⭐ 381](https://github.com/groundingpi/GroundingPI) | Precise grounding matters |
| [GRAVA: Grounded Reasoning-to-Action Representation and Learning for Autonomous Driving](https://arxiv.org/abs/2609.15169)<br><sub>Xiao Liu, Haoyu Li, Jianghao Leng et al.</sub> | arXiv<br>2026-09 | [⭐ 487](https://github.com/AhernResearch/grava) | Driving vision-language-action (VLA) models increasingly reason before acting, but their intermediate reasoning is often weakly grounded in physical scene evidence and loosely connected to executable behavior |
| [Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air](https://arxiv.org/abs/2605.31066)<br><sub>Tianle Zeng, Yanci Wen, Xueang Yu et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 1,128](https://github.com/louiszengCN/CarlaAir) | Recent aerial vision-language-action (VLA) models show promising single-UAV capabilities, such as tracking moving objects and navigating to language-specified landmarks |

## World Models & Generative Simulation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [FrozenDrive: Zero-Shot Text-Guided Driving Scene Generation and Data Augmentation with Parameter-Free Frozen Diffusion Model](https://arxiv.org/abs/2606.20110)<br><sub>Yuhwan Jeong, Hyeonseong Kim, Daehyun We et al.</sub> | ECCV 2026<br>2026-06<br>📑 1 | [⭐ 10](https://github.com/daehyunwe/FrozenDrive) | Synthetic data for autonomous driving is surging, powered by diffusion models that promise scalable scene generation |
| [MESSENGER: Memory-Enhanced Sequential Scene Flow Estimation via Autoregressive Next-Frame Forecasting](https://arxiv.org/abs/2610.10759)<br><sub>Jiuming Liu, Jianing Li, Mengmeng Liu et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 0](https://github.com/liujiuming123/Messenger) | Scene flow can capture low-level 3D motion displacements in dynamic scenarios |
| [ASTAD: Asymmetric Style Transfer for Synthetic-to-Real Adaptation in Autonomous Driving](https://arxiv.org/abs/2606.29286)<br><sub>Dingyi Yao, Xinqi Zhang, Lihui Peng et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 2](https://github.com/Dingyi-Yao/ASTAD) | Synthetic data mitigates the data scarcity problem in autonomous driving perception |
| [Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends](https://arxiv.org/abs/2606.01164)<br><sub>Jiuming Liu, Chaojun Ni, Mengmeng Liu et al.</sub> | arXiv<br>2026-06<br>📑 9 | [⭐ 249](https://github.com/liujiuming123/Awesome-Interactive-World-Model) | With rapid development of large language models and diffusion-based content generation, world modeling has attracted increasing research attention, benefiting various downstream domains such as game engines, embodied AI,… |
| [Is Your Driving World Model an All-Around Player?](https://arxiv.org/abs/2605.10858)<br><sub>Lingdong Kong, Ao Liang, Tianyi Yan et al.</sub> | arXiv<br>2026-05<br>📑 6 | [⭐ 258](https://github.com/worldbench/WorldLens) | Today's driving world models can generate remarkably realistic dash-cam videos, yet no single model excels universally |

## End-to-End Driving & Planning

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [MOJITO: Modal Joint Learning for Unified End-to-End Autonomous Driving](https://arxiv.org/abs/2607.23511)<br><sub>Zhijing Cheng, Xuancheng Zhang, Donglin Di et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 32](https://github.com/mumucc01/MOJITO) | End-to-end autonomous driving systems commonly follow a cascaded two-stage pipeline where a perception stage compresses multi-modal sensor inputs into a compact context and a downstream planner predicts trajectories cond… |
| [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](https://arxiv.org/abs/2609.26792)<br><sub>Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.</sub> | CoRL 2026<br>2026-09<br>📑 1 | [⭐ 14](https://github.com/VAIL-UCLA/DreamStream) | Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions |
| [DriveMLP: When Training Strategy Outperforms Model Complexity in Autonomous Driving](https://arxiv.org/abs/2610.29676)<br><sub>Alessandro Canevaro, Julian Schmidt, Hang Yu et al.</sub> | CoRL<br>2026-10 | [⭐ 6](https://github.com/alessandro-canevaro/DriveMLP) | Learning motion planning policies that remain reliable under closed-loop execution is a central challenge in Autonomous Driving (AD) |
| [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)<br><sub>Shen Zheng, Anurag Ghosh, Gaurav Parmar et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 32](https://github.com/ShenZheng2000/WarpI2I) | Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs) |
| [G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance](https://arxiv.org/abs/2606.26017)<br><sub>Hang Yu, Ye Jin, Alessandro Canevaro et al.</sub> | IROS 2026<br>2026-06<br>📑 6 | [⭐ 7](https://github.com/HangYuu/G2DP) | In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors |
| [SimWAM: A Simple World Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.07468)<br><sub>Zongchuang Zhao, Xin Zhou, Tianyang Xu et al.</sub> | arXiv<br>2026-08<br>📑 14 | [⭐ 206](https://github.com/H-EmbodVis/SimWAM) | In autonomous driving, World-Action Models (WAMs) have improved end-to-end planning by transferring video dynamics priors to action prediction, but many still couple planning with future-video generation at inference, in… |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 19 | [⭐ 360](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
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
| [Horizon3D: Sparse Radar-Camera Fusion for Long-Range 3D Perception in Autonomous Driving](https://arxiv.org/abs/2606.31096)<br><sub>Geonho Bang, Geunju Baek, Dongyoung Lee et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 25](https://github.com/geonhobang/Horizon3D) | Long-range 3D object detection is critical for safe autonomous driving at highway speeds, yet existing radar-camera fusion methods remain limited at extended ranges |
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

## Safety, Robustness & Evaluation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [CCFM: Collision-Constrained Flow Matching for Safety-Critical Scenario Generation](https://arxiv.org/abs/2607.04451)<br><sub>Ke Li, Kaidi Liang, Yuxin Ding et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 3](https://github.com/KELISBU/CCFM) | Evaluation of autonomous vehicle (AV) planners in safety-critical closed-loop simulation is essential for real-world deployment |
| [Lipschitz Optimization for Formal Verification of Homographies](https://arxiv.org/abs/2605.23203)<br><sub>Jean-Guillaume Durand, Panagiotis Kouvaros, Maxime Gariel et al.</sub> | CVPR 2026<br>2026-05 | [⭐ 2](https://github.com/jeangud/homography-verification) | The adoption of vision neural networks in regulated industries requires formal robustness guarantees, especially in safety-critical domains such as healthcare, autonomous vehicles, and aerospace |
| [CADET: A Modular Platform for Evaluating Distributed Cooperative Autonomy in Connected Autonomous Vehicles](https://arxiv.org/abs/2606.04072)<br><sub>Pragya Sharma, Brian Wang, Mani Srivastava</sub> | ICRA 2026<br>2026-06<br>📑 1 | [⭐ 0](https://github.com/nesl/cadet) | Deep learning models are increasingly central to autonomous vehicle (AV) pipelines, yet their integration has traditionally followed a monolithic design where perception, planning, and control execute on a single onboard… |

## 🏢 Industry Tracker

Latest 14 days of news, official blog posts and new open-source repos from tracked companies. Full daily feed in [`daily/`](daily/).

<details><summary><b>Waymo</b> (134)</summary>

- 📝 2026-11-05 [How the Waymo Driver Manages Severe Winter Weather](https://waymo.com/blog/2026/11/winter-weather-preparedness) <sub>official blog</sub>
- 📝 2026-11-05 [Rethinking What Freedom of Movement Feels Like for Women](https://waymo.com/blog/2026/11/because-women) <sub>official blog</sub>
- 📰 2026-11-07 [Waymo Toyota: 1 Bold Robotaxi Deal With a Winning Partner](https://news.google.com/rss/articles/CBMia0FVX3lxTE41aHY0RTc5TmVSOUNJemdKdVpGZzV1b0h1NTN1QjVEbXJUVktYbDlsOEtmdHN4M2pIWHVWU0xkbEN4TEd4dVRtbV9RODV1Yzd0M0M0SVJFSllKZjZGd2JxYXgzWE1VREJlMjhB?oc=5) <sub>Global Brands Magazine</sub>
- 📰 2026-11-06 [Waymo expands into five metros with $5 billion loan as AI stocks sink](https://news.google.com/rss/articles/CBMinAFBVV95cUxPeTl4cEZsTktiQ1VGLVBzUVBJd3BtQWRWM2xzUFVkeW9QUHl4VzZaRmN5elNCTXFKV3Q5QTR0NDRzSExMMkxTZkdDRG1fY2NMVkREbVZsaUVacW9ELTdQOUJHVy0zODRoUUkwOUtiYkRyaW9BTlFQOUlSX3MwTkRKdVF1THlhTzluZThka01LaUJ6RG0wTlhSbklyTkw?oc=5) <sub>Startup Fortune</sub>
- 📰 2026-11-06 [New patent enables driverless taxis to brake or swerve if a cyclist crashes, months after autonomous vehicle firm Waymo warned avoiding cycle lanes was “too high a bar”](https://news.google.com/rss/articles/CBMid0FVX3lxTE5VVVJVT3o1NVpiUVlqVElRNjczWUdpLVlPUzV0WlppMTdaWjM4clpnWkd6Ri05eFllVENzMko3YlVLVFJ0dF8zRUMzU1RkdGdFOTdXMWVzY2RwOXZPX3JxeWg5ajEyMnBUT1RhWUxEendlYUNhcENN?oc=5) <sub>Road.cc</sub>

</details>

<details><summary><b>Tesla</b> (207)</summary>

- 📰 2026-11-07 [Tesla to End Cybertruck Production After Safety Recalls and Falling Sales](https://news.google.com/rss/articles/CBMiiAFBVV95cUxQMW9zNzhXbVNzZDJ5a213ZjRWX1FUZFA4WFFWaFBVbWp4cWlzakh6dXk1aFhmem94UlFrT0N5bGdZNFJWN2U0MjhnckVOakgycHgyS3hyYTY0c2VDdVFoT295NWV3ODZPWHNXT3JyTDZXS3p4OWV3S002dmNKLWo1RVV1c0NfanUy?oc=5) <sub>Law Commentary</sub>
- 📰 2026-11-07 [Elon Musk Says Tesla Will Wind Down Cybertruck Production in Texas by Mid-2027: 15 outlets compared](https://news.google.com/rss/articles/CBMi4AFBVV95cUxOVjlpZGJTNTlzWWVQcksyTWl2YjVpM3pXSGk4NHRBOUdsSTJSWmlHVW0yRWVBZVB2Z3pnSllkaFM4Y0E0LUpXc3RpR1lid2pBWHlxblB4Y1NTTnlVNDlIN0xJdnpwVGJFSlRQVGltZWw2N2VzM0VfNEVfYnZySXVFX0xhbElDLXd2THk1cC1pYk8ySU5WY3JNVEtGNGJlYm9ZQTRDc0ZvZmtuWjN6LUNkemdJMl9yOHFJOG1YUDViY0ZUQnNLZ05xTjFaQm5FMnNzb2k0X2NDM2FSS0NrTTltWA?oc=5) <sub>NewsCord</sub>
- 📰 2026-11-06 [Tesla’s Musk pulls plug on Cybertruck for robotaxi push after years of poor sales](https://news.google.com/rss/articles/CBMi1gFBVV95cUxNX0VpVjMySk1VdHFEa1BGeWJ0WGliOFpBLXdDYWFlV2doZkRBOFFMQlhQcTg5V3BEWXFaelpsbEdLbk5TWFlQNmFDa3ZicWtkYm9jbndKaFI0YnhBTThxX1REVlJOSlp1UzBSeG5JdHFvXzkwbWxNTFNjcUFsTXlEOXhXcndLeFN3Qi1vTzV1VkVvTF9zcV9zQnZyNXR1RmdHVzhMMGNCOGFNT0wxTV9YUmluVHFHbGUtUGJxTlFhcWxGN09BNEk1V3E4OFVnQzZkNmozQ2VB?oc=5) <sub>South China Morning Post</sub>
- 📰 2026-11-06 [You Can Now Rent A Tesla With FSD On Turo](https://news.google.com/rss/articles/CBMiakFVX3lxTFBWTDUzbHI4bGF6MTdvQjBDdVBjRkpUTWd2LVA5MThQUGFDYTdvMFhoYmVaT3BwU0xRdU01Mm5ReGlYQ09pbjBiZ3UwR1Q4WU1aMlJ0QmFGcnBZUFFrYVRfWTlHOHlXOS12UXc?oc=5) <sub>CarScoops</sub>
- 📰 2026-11-06 [Tesla Skeptic Tries FSD, Then an Intersection Scare Has Him Hitting the Brake](https://news.google.com/rss/articles/CBMimwFBVV95cUxPcnFqX3VCTHBhZFJZYThvc1B6UmtWQlNZM1pPM0xUcFJKX25aR1ctazdJdHFHT01JSGtpdno3cWF1eWlicGExRjFYUVcxa1BFSXdPNEctRUFPMHp3emVpTGs5WXM3V1FyOFYxdDlORzA0MTJoazA2TTl6Y2ZGU0NNSWVDOWgydmEtLXBhanN0bU0tV0NZVmJUQkFycw?oc=5) <sub>Yahoo Autos</sub>

</details>

<details><summary><b>NVIDIA</b> (107)</summary>

- 💻 2026-11-02 [NVIDIA/nvperf-core — Core NVIDIA Nsight Perf SDK APIs and libraries for collecting and analyzing GPU performance data directly from application code.](https://github.com/NVIDIA/nvperf-core) <sub>GitHub</sub>
- 📰 2026-11-07 [Volvo EX90 and ES90 announce prices in Vietnam, starting from 2.6 billion VND.](https://news.google.com/rss/articles/CBMikgFBVV95cUxPQUNJWFJPbHVxekJsdW5yUjBPb3FCVVJ3UWRqYi1vTjZyX0VSaW9oUWkxX2k4SGJHNm1oMDdBTlBYUWlqSGotNEd4MlY4Tm1XNDhvX2g0bllKRVU1RkY4SlNvMGhTbnhmV2gzQ3FXOUx3MmVxc2RUSUp6aGx3VENGQVNzRXFVM3cyamIwV01vN0hpZw?oc=5) <sub>Vietnam.vn</sub>
- 📰 2026-11-07 [China’s top spy agency recruited woman who targeted Nvidia’s Jensen Huang](https://news.google.com/rss/articles/CBMikgFBVV95cUxOT2p3WUZBWlFtYzVoNTJsODd1NVZrM0dSMnQydThRX0dXcXJRMk96QWVzTnowRkF5V3FoMUU1b2ZOVUQwM0U5eUdmX0d5LUNCYm91cFgzQXE3UVJTdDhZWjF6TEV0R0I5eHlDYk1rQ0Z0VXhLSmZmVG1VMDJqeUhYYS0xM0g5Y2FyUmllM013N2ZBdw?oc=5) <sub>The Japan Times</sub>
- 📰 2026-11-06 [8800 GTX Demo: 14.6GB Download, RTX 4070 Needed [2026]](https://news.google.com/rss/articles/CBMijwFBVV95cUxPc2pnZXdYeW41b1JNV0NVSEt3VS04ZXRreEV4cVBYeXMwRGU5R010SnNfc1NlTFdYaXlyNHc0TTVsM1p6WFkyUVlNV2paODhNN1cwRm1rMWxVaHlhdlEyYTBCVkx2aV8xYkxPWUpkWk5vdEY0cUpFbUFiZVhwZ1p5WXdPeFFPeTd1THg4Yjl5aw?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-11-06 [Jensen Huang Says Nvidia's Next-Gen Vera Rubin Chips Will Generate $40 Billion in Revenue per Gigawatt, Up From $25 Billion for Grace Blackwell. What That Means for Nvidia's Growth Runway?](https://news.google.com/rss/articles/CBMimAFBVV95cUxNcUFWdjA2ZXlKcFMtdk5DS0RtTHJ1N1dDSnpjN2VoMFpnZDN5MFU3WjVpUHFQMm9ZZy1nNEJSZ1pYM3g1dEkzWmJxcHZmaC1TY1Nkc2FIcFlOMl9OQWw2a3A1cXVZQ3NMclpadmZFQTdkYWVTS1dibjFSVDVXeGIwZTFtRHZHZHpnZUFXaWItMGJab09MblRnTw?oc=5) <sub>The Motley Fool</sub>

</details>

<details><summary><b>Wayve</b> (29)</summary>

- 📰 2026-11-06 [U.S. Dark Money Tries to Stop Robotaxis as Japan Says Yes to Full Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTFAtLTNZbVB6ci0xRTZJVzUzMGFDekxRbi1SQmFhV3VvYTc5b2JVajctSjNJYy1PZG9QeFBHVWp4d0pwNHBhQzUtZUlMVDdRQy0yUHpBaWNoVFRfbllyTVNn?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-11-06 [PAVE UK adds accessibility, insurance and legal expertise](https://news.google.com/rss/articles/CBMinwFBVV95cUxNT2ptcncxV21xOGFUWWppaUVPVExWMHBHaEFnX25WYjNYSk5JQTNNT1pPVzkyUHFyMVBmWlk0RExGRmhiODBaOGw4RFN5cTV6WExsSVlNT21oVkNWQ216M0s0dUJfWk1jZ3NHR1pNcXA0RHp2c2pNeUlPU2s0SUpYR3hEUHZFNWFmQWRyY0VRc19ZbFh4eE9pbFRsVUF4VE0?oc=5) <sub>The Engineer</sub>
- 📰 2026-11-05 [Uber plans $10bn investment in robotaxi expansion by 2028](https://news.google.com/rss/articles/CBMimAFBVV95cUxNajdmczdJWGZ1b1B1ZlA0NFk5NmFZRVFZMmd5d0J2WnphWkVjYWlJbUVfM2ZhMlZqXzM0RVVLRi1Ba2xoT0hYZVhXX2VGWVZSUEVjQ2lVQWQ5MHM5dThkX2daNHJad0ZGVnpPbjNtT2Rxa1pkUnpzSVV6S0p1YlFYcDg4RUlsbE1uek9sekJGMFA2SlIwc2p4Sw?oc=5) <sub>National Technology News</sub>
- 📰 2026-11-05 [Waymo Roulette on Lyft in Nashville Field Report｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1vbUxkMzIwb2EwZGxIWWRvQWNOMWRKMUZ1cXJJNV9waEJuWVRvWDl4cG9XYWxNZ0d3YkdmNG9JT2p1aTFLRmRJT0RDN1hBR2dGQ0lOZkJlUi13TmhlT2hF?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-11-03 [ARAPL Subsidiary Humro Secures US Department Of War Approval For Autonomous Industrial Vehicles](https://news.google.com/rss/articles/CBMi1AFBVV95cUxOSHJ3VzZHdUlQZEdVVmtzVy1aS2NCNDl2azNKd192Q1MwNWkxVHA5bEo5S1pBdkpMVjItN2NPZUxpNktzOS1tSE5iOExCMDhuYmJoUEhjUkY4Rk9oS01kUDduZGFoM2RIaXVYMTVBeDJVc0U4cVNieEIxNFZGN2s0REtFcGV2TzJmWnI3Z092NG5UN1Vab0xLeDhhNXlzUVQwaXFPamtITjVYSXZxbHFrTFFVbnJ1VmdZd1BjZUtiMHE2cENOSUdJcEhkZmZGVlJ4SjRtYg?oc=5) <sub>Motoring Trends</sub>

</details>

<details><summary><b>Momenta</b> (65)</summary>

- 📰 2026-11-07 [上汽Momenta成立合资公司！瞄准全球L3智驾，「全栈自研」已成过去式](https://news.google.com/rss/articles/CBMif0FVX3lxTFBsNGJKNmQ4dUlYd19XZ1ZyRTd0cndKMHBGeEpnem5zNTBRVTVNTU52ejNzOXI2WTNPZzNQQ29lZWY0cllvNXRlM2hxeWVfTk8xejQ5QnN4QThQc0ZqcFBnclZnZDFpR1JMekhQWHRfNWZMQWJXREkwMFFlMk1wVms?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-06 [注册资本3亿元！上汽联手Momenta设合资公司，车企“绑定”智驾供应商只为技术红利？](https://news.google.com/rss/articles/CBMiYkFVX3lxTE5wN18zR3ZoME02ZnlFUzEtcnlRM2VJdzdoTFpmdXhUY2Y1U0Uyck9pdlJIVDNaQnZtMFpYZkxRWUh3cmVrRWFuNllkb2szS21iX2NEc085UmZ6TUliOXVNRm13?oc=5) <sub>同花顺财经</sub>
- 📰 2026-11-06 [General Motors showcases Cadillac at CIIE, XT5 PHEV becomes top-selling model in China](https://news.google.com/rss/articles/CBMi4AFBVV95cUxNLUNoWGRTN2FkQm5BUU55ci1wMFVIcnoxWUNmaE90UDJWYmRkVE5ucG4xRXNxMFl2Yk1PME12QURteGhKa181OVdDTzBOX2pycXJqX1ZGSEdpMWZzQUFVa0Z3c0hHLTE1VV9OOWdtenlnTE0xaW83X0FBbGdxanhTUHQzU0JkbDg3SzhaMldZVGt6bnZFaWRsOTJ3YXNEbVRtTDBZV1lXRGV4RlZ6dmlqSUF6TEhfdUJYMVlsT3lJclZnZFJOLUpMMEtYUkVmVlV2bGcwMWVJdjhSSFhFN1B2dg?oc=5) <sub>Gasgoo</sub>
- 📰 2026-11-06 [为了L3自动驾驶 上汽真是拼了！联手Momenta成立3亿元合资公司](https://news.google.com/rss/articles/CBMifkFVX3lxTE04c0hocTJSTF93VDFKYzhvbE1ES0pNRlR2Z1RNTGhsRnNIQkZJOHFCb1Z1Wm52bllIWmZSV2gzVFJ1bmEwLXBDT3RTdjAwSEVGZ1pQbVlXQmNUeTBfUHV0OUZTazd6UXVkTHJPZWcyTHNfZHM0S0ZsRXhyNHVnUQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-06 [上汽与Momenta合设3亿合资公司，共研L2、L3高阶智驾](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5FYk9QTnB1MnpFQ05adU9SSUJ4bnA4eXhLdE9KREgyRWZqajhUdnNwNUdDRVpsQldYT3kwQzYzakhnZWlVelJUMTNOc29OdkJPN1ltdHF4ZjR6YzA?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>XPeng</b> (158)</summary>

- 📰 2026-11-07 [23万级大五座SUV长途横评：小鹏G9L、问界M6、理想L6谁更懂家庭？+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5lX2NWX05BQ2twMm1sWXBaaE1KV1BNVEd3dnd1bjdOLV93UGxuSE1ucjJsOTV1Ny1oVTRPMmlVTWI5Wk80WlJhN3U5ZzZGSC1WUjVINGhoQzZad0pUcVgw?oc=5) <sub>新浪网</sub>
- 📰 2026-11-07 [XPeng's Korea Leadership Hire and Robotaxi Green Light Add Weight to October's 50,237-Vehicle Record](https://news.google.com/rss/articles/CBMiggJBVV95cUxPaEZLVXB4OHEyclJ6eW1Scm4wUjNiR0syTTRzV3pWSXRGN2FvYVRBZWNUZGUzMEdLb0UyZHRnMFFiRXNJMnduUnYxQkRZcW5vSmJCcXJYQjlldElWalNiSVV6SU1XTjJMYkRXdDNBRjFueXpSRE5pSlpWTDlIVlVUTFp1cVVHTC1rSjAxN1JkU2t0aExDMXBnZmd6MFZ4clFWZDhzd2cybkVYZE9FUklXXzdCS0dUSWp2VHpOUlZaMnBqcE9DNkMyOWQ5RDBJV0pmbmswOEpBbkFMSzFfUUFxR3dwT1dCN3JhNENvQmE2cWtERmVYZWxTVG5zLTdzbGE1MkE?oc=5) <sub>ad-hoc-news.de</sub>
- 📰 2026-11-07 [As EV adoption slows, battery recyclers beyond China struggle to stay in the game](https://news.google.com/rss/articles/CBMiogFBVV95cUxOcm9OUVplb2xMZ2N2V3BKaGd6aHVnVTAxM0NMX2VfWmFfbDdfcmd6dThWWXJGTzhTa2JmTXlIcTloczdjSDZtYnQ1WkpGSmVZWnpFNS1YLVNQUUd0aGplRnN4WkI0MmNESTF1cXBLU05zeVRBRmJueEJ1TDdYZEUxdjFYSnFkc2VlOXF5QVBoNHVhNmd3V2NwNFN0WDZTa2p4SkE?oc=5) <sub>KrASIA</sub>
- 📰 2026-11-07 [4款30万级大六座横评：奕境X9 27.98万起带四激光，五座换六座该选空间还是智驾？+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9KS2NUYlNscE9KTEVINnlBMVBXVV9KQUN0aU1iT25wMk5IUU1SQU16cjZ3MjlkSlQwSURDV3VNTDQxX3BlYXZOLTJRSDF4cDBHRmphcEgzYzAteTNkTHBn?oc=5) <sub>新浪网</sub>
- 📰 2026-11-07 [30万内四激光大六座怎么挑？奕境X9对比问界M8、理想L9、小鹏GX，4车4场景讲透+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9LSmVjMmRiS2I4THRnREtXNFQtSWM5dlBkLW9YRE8wMWR5Y1NCQWxQbnB0U3JvZGJmV1ZGUzhaMVMyTlhNVjNYY2dzSDB0ak10ajFQVmpaYUVJMFpvRmxZ?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>Li Auto</b> (103)</summary>

- 📰 2026-11-07 [理想汽车推送OTA 9.2.0版本，VLA智驾与智能座舱全面升级](https://news.google.com/rss/articles/CBMiW0FVX3lxTFByTW9OVmxYRUZjRU9COEZneVRXcXoyYlpSbEtkYWkwUVcwcGRvU3dsT0RGdzhMZDZFZFEwNTdJclMyeGg5czAtZmgwb2tSSVptdnREamVsc20yMzg?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-07 [理想OTA 9.2.0开始推送，智驾座舱升级](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBPbEIyUU5YeEJ1RS1tNFJ3SnB6ZkZNc2J0SlhtYUZZSl9NeURWcU5vLURadWdLT0U1bWtTLWVUd2dnUF93MFhBNFJtSFU0V0t5YlVoaEtGeXRsbWc?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-06 [理想ONE落地价现在多少钱？从36万跌到9万起，抄底还是加钱上L8？3个维度说清+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9oenBNVEJLSjU1UHphTHBvNld4U2xNOWxnYVlrQzN6Yjl2SFZ1QlZ1ejdTemFxcWZOUURNTHphZDhRdHJKc0ZIdExzU1JOU0pZd25JLVdWcGNrbTNBTnNB?oc=5) <sub>新浪网</sub>
- 📰 2026-11-06 [一家五口谁更舒适？小鹏G9L对比问界M7、理想L8、理想i6四车横评+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE8yVTdmTlNpTEFPVGVzQjEzbGwxR1FaVmVBUWQ4NHNzNFdRZDl0SGNPX21WOU5kbUJxM1hwQU01R0ZMVzhfMWl1SDlYbUZqMGE5RDNFYXo2eGMzZDJJZ25j?oc=5) <sub>新浪网</sub>
- 📰 2026-11-06 [理想L8、领克900都试了，为什么我最终锁定了神行者8？深度横评给你答案](https://news.google.com/rss/articles/CBMickFVX3lxTFBJelYwYjllQXlhNEE2WS1oZUVWSDNnb1RSRlR3Z3ZBcXZhaV9keWlmWmNOTTVCSXRWMVVTVjVaaHNYUFF6SXNBZDdGR2RnM01jSFV5UVBLamdzTUtjYUFEd2dtMWJMOTlkaGtDUGJDdTk2Zw?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>NIO</b> (61)</summary>

- 📰 2026-11-07 [Nio Firefly wins 2026 Red Dot Award for smart cockpit design](https://news.google.com/rss/articles/CBMifEFVX3lxTE1ENjlTNFo4RlAtZXpwZi1mbGRsVjI2RVpEQWUzdUNpY0RETl9Xbmx2TnFqbVJQVWpZLXNSVmZRNnlLS213cmNsMGhwNHQyVDZ6cnBSWUtRdWZrN0RBVWVBRUwxbmxuTkNwb2h4c0dVbFpMd3c3QlFGM2N0T2E?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-07 [乐道L90挑战智驾通过贵州科目二](https://news.google.com/rss/articles/CBMic0FVX3lxTE5wOUZPOHFad3hQQ0JYUkpyMXRpYmJ0MkMxc2V6REVuNnNZSHU3UVZRYmZqWlk4b2drbEp6dS1raXd1OWZGUnVpcEtfdHFmV1drQTBJOUhfTmRULTlqUzloZVR5SzhhbmIzSzc1WklKRWJIRlk?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-06 [Nio CEO Says Self-Driving Shouldn’t Cost Taxi Drivers Their Jobs](https://news.google.com/rss/articles/CBMingFBVV95cUxNSEMydXhEa05VcG5CUmNXQnhOVnE1NG1OUDlPMmJWM2JPcDZCSWxfWThwd2VTZnF5TUF4MHBIV1NuaDA5TE1RNnhOb3c1dF9ZMTA0OVhYYnJvRkZKejkzOUs4MEgwS21abXdTZ21zd2pWRG5pbWttYUltR05uSVV2a1N2NHJuSk45dGVYTDRrM25yM3E2ektIQXczYXUzUQ?oc=5) <sub>Electric Vehicles</sub>
- 📰 2026-11-06 [BYD Yangwang U9 Xtreme breaches 500 km/h barrier to set new world record for production cars](https://news.google.com/rss/articles/CBMifkFVX3lxTFBBMm5yVFg4WEluOUxBWHJybXQtRFNOR28za0R3WDhIZFdZblFlZFFkSjFLOUtMVXFwLWFsT3pJUUQ0SktNZm1VTTBrTW11a3RJTndpYmE2Z2tJdnN1REhtRlZZVDN4M3lwU093S3owZEVRcXJoWC1hU1VPcjRqdw?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-06 [NIO's William Li Renews Criticism of "Battery-Stacking" Approach: Vehicle Weight Up 20%, Road Damage Rises to 2.07 Times](https://news.google.com/rss/articles/CBMidkFVX3lxTE8zS1h2NHFSLW9kUWYwQWhPQllCZG1mVzRNYVNHMVdrVmhzeG41Q0ZuX3lpdW9yUHl6NUJrQUtQRGRqOHl6REhJdjBZM3B0b1V6WVdfdTcwS2NwekdMYW9lbEdLdnVWVWZSWUFDMkNHdG1FWk5DaUE?oc=5) <sub>BigGo Finance</sub>

</details>

<details><summary><b>Huawei</b> (172)</summary>

- 📰 2026-11-07 [27.98万起的大六座，奕境X9、问界M7、深蓝S09三款华为智驾SUV怎么挑？+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBpWVNSZHI2SzhaU3lJVFZNTGE3ZnpaYzI5eExhVHF2cEhBOXZ5TklwX3JsU0NhWVdTZ3ZCcG1NQnJzTFdwMVM3ZDBlRjh1dkdNTUV4S1pROU1rekFWRWRB?oc=5) <sub>新浪网</sub>
- 📰 2026-11-07 [奥迪A5L双车怎么选？25万起买华为智驾还是德系底盘？3个维度说清+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1RRDF6R1p5OEFSU292MEJxZ2dHOEhDQXlCZ2tjTWRnSDBUYU41OGoyUElsV3phaWdlX1VyOHFmVkVhODlybzdoaTFKVGxZeUQ3eG1Ja29scFJseVdfV2Jj?oc=5) <sub>新浪网</sub>
- 📰 2026-11-07 [岚图梦想家PHEV真实测评：华为智驾+空悬底盘，40万级MPV值得买吗？+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBjVkE5elRQbUkwSEktWDB5SS1fLW9QaFc0X0JocTZBVm5KTU9pWnNpSmIzVDIyQ21kQjRUSU5ZckZwZWhCaVBwSGpQVXdXQ3kzMExRdWZuX2Y3S0xPT25z?oc=5) <sub>新浪网</sub>
- 📰 2026-11-07 [27.98万起就带四激光大六座，奕境X9、问界M7、深蓝S09怎么挑？+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1ZM1JqMFVEZGN6dDQzX3ladVRzbV9OWFA4c1NkWjJJbWtaWE5WdTB1aFVfbUExVDFYUTV3TmRHN2h5VVViTWthUkc2RFo4YnNldTJXX0VTMW1TUVNvLVBB?oc=5) <sub>新浪网</sub>
- 📰 2026-11-07 [3款家庭大六座横评：奕境X9、问界M8、理想L9谁更懂全家出行？+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTFByLVBodmlOVmY5dl81b2FtVFAwdHZieXZKLUtja0JfNnI3WW5RYml2c3ozVDFYSHpPRGliR2R1RGQ4dkU5WDZBOFNPZG5VY1J0Q1ltREZvcm85RmFUZmVJ?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>Baidu Apollo</b> (38)</summary>

- 📰 2026-11-06 [时速 4km 的“安全”代价：二十分钟的路，我坐了一个小时\|萝卜快跑\|自动驾驶\|路怒症_新浪新闻](https://news.google.com/rss/articles/CBMiY0FVX3lxTE1rUUFmT19aQnlfM2hMbndwSTlmNERNM1Q2ajM5aDNOOE1WNnB2NG9vTHVuLVVmNmV5dmNVTkd3RkJBblRnNjJ0c2VhS2ltWG1zUmNiYUJyQmFMaGR5ZmFyZ2hhOA?oc=5) <sub>新浪网</sub>
- 📰 2026-11-06 [Robotaxis Aren't Killing Lyft's Business: CEO Says Company Is Growing in AV Markets, Details Waymo Partnership](https://news.google.com/rss/articles/CBMi9gFBVV95cUxPaGl2SWJTd3RZb3MyZ2QyZFZvaFAtdlJsc2NiVGpLSGRyamZ4WG5RRmU2UDVUcE1yVDRJSDdZdFNwSXlZclVDbXBiSDdGZ0VrQkFmWXptUUl5Ymxha056VW9KS0Y2MWFZb3hOYTVTNk4xcV9BUU5sUlRTZ3BVMHdDQ3o3M1U5U2JGQkxlMnRwSE9NQ2I5dTIzVVJHV2kzekZITUR5UGJSVnA3ZFJkVHBwVTBmd0FkR3hhcHZ0aGIyNTFBTUxCaTZOeUNydlRlc19uVExoejZ0R0UzV3VoY1BWWWFpQ2Mwbl93UVRCdmk3YkpBek14T2c?oc=5) <sub>Benzinga</sub>
- 📰 2026-11-06 [Lyft CEO Calls Robotaxis a 'Gift,' Projects Autonomous Rides Could Hit 10% of Business by 2030](https://news.google.com/rss/articles/CBMidkFVX3lxTE4wVUpHbHhrU09EcWhHUGFEaVRvVzVPN180bjNQNXJLWEpCZ2M3SGVEOWJtZ1dQQ2JQZm5INGpKZjlYY3JmVWZHd19ISnBEbGNGZ3NlajhidlhEQ0ZjQ2xCa2R6Z0EyVGJLMklsUnF6bGtLZVZud3c?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-05 [让AI教AI开车 百度Apollo World最新进展 接单、出发、抵达，这趟萝卜快跑的行程全在虚拟世界里完成。百度披露世界模型 Apollo World最新进展，可以调节车流、设置突发情况，生成相机图像和激光雷达点云，供驾驶系统反复测试。连月球道路都能模拟，这个虚拟训练](https://news.google.com/rss/articles/CBMijAFBVV95cUxPWGtoTUdxdDNKQlU1NkFPUlpVVWpBbmVGMmhDa2l6WHJwNWVLMWtBbVRxMWNJVnZJaFRWVjI5RzJYT3JwVGhUWk9SSDR0MmhFRUVjUG5DUktOMm1sWUVMbXoxdndrUW9qdng3VVZobjFIUlAwV050dTFqd2d5aE1aeU84MjZVZ2ZQXzdLSw?oc=5) <sub>搜狐网</sub>
- 📰 2026-11-05 [Airbus profit lifted by jet order boom](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1VU2RKQVhCTEJCMmU1a05Ld2JZYk5CUDd2THNKWEtfQUg2RE1vMEVKUUJNNnBONXZlaUY1M05zOEd4OUhJUFMxM1N5T3ZrVWhtSlQ4emY1bjYwVS1fZXRjWUxlTEg3cDQ?oc=5) <sub>Reuters</sub>

</details>

<details><summary><b>Pony.ai</b> (83)</summary>

- 📰 2026-11-07 [1.4万辆到70.5万辆：Robotaxi的账本，算得过来吗？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE4zZnZ3aGZHdmJ6WGllUktWdHdWOERQQ3J5SjRwVF91b1RzeklrdWNmZ2ZUUmpNVzRPZzBXY2NjM0FXc09ZSDhSMzdFa0xpSTlmVGRJRkJGOTVmZ28?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-07 [Singapore regulators review autonomous driving standards following Grab vehicle incident](https://news.google.com/rss/articles/CBMic0FVX3lxTE9mOVppZ2psSkFIbm0wVjVXdXgyTV91S0t2bmZ0LTdzU0twSFZjMzdWVEV1N2FwZkZXY2x1aW5zSTFlVU52bEFFaG1KT3JYb0lFMnAwa3F0MThfOWNfOXVIeVBSWlpRMDhzWFRoLWlXN0F2ak0?oc=5) <sub>PravdaReport</sub>
- 📰 2026-11-07 [Grab autonomous vehicle appears to nearly hit schoolgirl at Punggol junction](https://news.google.com/rss/articles/CBMivgFBVV95cUxQY1pPT1IxNmpkQVl6SEU3UXRKZFZDWXFrU3BzdlkwZm9keGk3aVo1ek9kQk1YdGJUTWNXQkxWRG14ZGhUczktaXpDQ3NjUkNtNmNleTJYX213b0pxT21wMGx3bFBRR0Y5M3otV0pvdDZVdW9oc3pNeGpRYkVLcXpESWVQRk92WEsxVFRvQ3Z1Mk15U0F5OUl1VzE3em5qcG1sUDJ6UDlhcFJ4S2pseEZsMlhNeTZra1hOaVRiZGdB?oc=5) <sub>The Online Citizen</sub>
- 📰 2026-11-06 [Grab reviewing incident after autonomous shuttle fails to give way to woman, child at Punggol crossing](https://news.google.com/rss/articles/CBMijgFBVV95cUxNMlpQcWRpb2FVWHZXUkNxRU5mYlhhS0NobFdpU3RVSGlad3NSSlZqTmhNendTU0d2R0hsRjA5WWNkTnhZYTl4bDVFVjNUaktaYWxDVUhMdGZ1M2p5Yy1zN0xDYVVHcGdUc2EtWENYWTJReXlsV2xsYWtqRDNFcmY5cHdnUk91QVpjUkZINWNn?oc=5) <sub>AsiaOne.com</sub>
- 📰 2026-11-06 [11月6日热门中概股多数上涨，阿里巴巴涨2.64%](https://news.google.com/rss/articles/CBMiowJBVV95cUxPSG1LUFB3ZDBUbW82SVRhdC1XRmxuUXR5Vi1Zck5veThFYlZyTklTUExuNHVKUkJES2k3T3VQeDdfUlpocGJtU24zdGVjVGJjaFZ6cXlQMDYzMjdPR3FCQzJEeGMySE1IZ3h5RzRIQjdDTkR0cXZoXzBlZ0tZdnpITndVU2E0MHdLb0pVRWtvWi1TM2hDLUhtWGxUUmVzMlJKakZkQmMxVTNKYWpDZDFHV01INDBXTGxpUG8ydEZYM1JUUEowMjEyMVZmRlhRcFMxQmMtMmwxWTJGUkpSdHBPb2V6SmtZRDMtcXZEY2w1dHprN3Y1QTJHUXZlQ2VqYTY5Zlh4T0NXaHZ2WWJfcEdXVlJOTVliQ01tZkVIc2xKQkdXXzA?oc=5) <sub>新浪财经</sub>

</details>

<details><summary><b>WeRide</b> (73)</summary>

- 📰 2026-11-07 [1.4万辆到70.5万辆：Robotaxi的账本，算得过来吗？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE4zZnZ3aGZHdmJ6WGllUktWdHdWOERQQ3J5SjRwVF91b1RzeklrdWNmZ2ZUUmpNVzRPZzBXY2NjM0FXc09ZSDhSMzdFa0xpSTlmVGRJRkJGOTVmZ28?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-07 [Grab autonomous vehicle appears to nearly hit schoolgirl at Punggol junction](https://news.google.com/rss/articles/CBMivgFBVV95cUxQY1pPT1IxNmpkQVl6SEU3UXRKZFZDWXFrU3BzdlkwZm9keGk3aVo1ek9kQk1YdGJUTWNXQkxWRG14ZGhUczktaXpDQ3NjUkNtNmNleTJYX213b0pxT21wMGx3bFBRR0Y5M3otV0pvdDZVdW9oc3pNeGpRYkVLcXpESWVQRk92WEsxVFRvQ3Z1Mk15U0F5OUl1VzE3em5qcG1sUDJ6UDlhcFJ4S2pseEZsMlhNeTZra1hOaVRiZGdB?oc=5) <sub>The Online Citizen</sub>
- 📰 2026-11-07 [11月12日，4款新车扎堆上市，哪款值得期待？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1hSjhQS3ROeGotd2dOT1RJOXhoWklmd1RYZzg1UU5CUHE0d3dOalFpVTJKbmJoSE5yVGoySWh5eEtNR3lFR1JJZ0ZBSHJFbEVZTlhuRkVILXhqY3M?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-06 [文远知行CEO韩旭谈Robotaxi，安全第一舒适第二](https://news.google.com/rss/articles/CBMigAFBVV95cUxQQUR2b3hvS2ZrbDZMemZ2NHZNeWg3YmRyby1Na3J3c0pIdGI4TWFGZ3ZVbkdIRFUwY09nek9ZYVVYNVlsaGdSZUw2dXFUOTNXQUJXTDZGalhGZnctMVN2Uy1FU1NWdGFlWk1KZ2ZyYV9rT2ZETmp3V0RXTTZfZEs0SQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-06 [Grab Reviews Punggol Autonomous Vehicle Incident Involving Girl at Crossing](https://news.google.com/rss/articles/CBMinwFBVV95cUxOa0NVMU90VU9nUjJ1UGlEdUhyRF9GTEo5U2NiQ1hMMVFaeTZSam4tZ2U4REZzYTd0YjJPRWVlY2w2ZU8tRTNMckZvSWxYTlR6WHN2ZllSTkx5TUNMUDd4bHl5RjNoMjliY0xubWlBc1ZzenM3akZjbDU4bW9rZ1JGcTVhbGVhWW5Hc1VHdHFhQWxGbVRhUzRVVExaM3ByRFk?oc=5) <sub>Goody Feed</sub>

</details>

<details><summary><b>Horizon Robotics</b> (68)</summary>

- 📰 2026-11-07 [深蓝S05新款2027款智驾值不值？13万带激光雷达城区NOA，3个维度说清+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBpcEphTWt0ZXVVOHladmExbjAwTDFWSmlnanVIWVpDVkY0cW5JTU5XNldYNXB3ei1RT040cjZweUw5OG9yMWg2NTg5OWFfQmRqX3E0dzZlbG5odjJ4enRV?oc=5) <sub>新浪网</sub>
- 📰 2026-11-06 [东风奕派M8天元激光版值得买吗？15万级标配激光雷达的六座纯电SUV，3个维度说清+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1BcXAyb1FabFlLbVc5UEZlLVN6NlRpUjNSeW9ydVlydDd6aVZvMUVKRWRXSjh3UklYRnVDOGRyaC1CaXk2My1xUG1naElVOTFaSDJJQ0VhZ3VVcDZQOXJV?oc=5) <sub>新浪网</sub>
- 📰 2026-11-06 [Volkswagen’s Jetta M6 EV quietly launches "taxi" trim in China with 600,000 km warranty at 12,900 USD](https://news.google.com/rss/articles/CBMixgFBVV95cUxPeGg5Vk5DSklFb2ZRaHZDRnA3dDVsMVFTLVJ5NW1mNkFIY0lSa0FfeWFqdUJ2aUR5dVZLWkVXa014eTNGeHlHeFVHZHY5dy03eDF5V0taZUQ1anRYeHhqalZaanJtQWctUGJlQzlPU25WdFN0MUVwTXFHQ04zQVQwUmlHWk50enVoQ3p5Z1hkSlJCLU4zMWlUOW5mMVVHLUQyZUtoNHpXdHJ5YzlmZURhdExQN2hmcDI1dXNMaTBMb0RZb3pWYUE?oc=5) <sub>CarNewsChina.com</sub>
- 📰 2026-11-06 [余凯：活过 2027、赢在 2030，智驾竞争回归商业本质](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1IUkRnei1ET3htYjlaOHh2cjNnN3A0c2Q0X21iemZJRk9vb0d0NkJmWVpNeF9nc0o0VEZVZGZQZTlRcXNiam8zd3VQY216MG44TEQ5NVhxTEc5Wk0?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-06 [奕派M8天元激光版把华为换成地平线，便宜了2万都省哪了？](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBPTWVMVG03ZHZLYkRyNXQwcVJTUTVEMW91V0R5Mk9pVjROUkRlU2xINmktTjBIdzJsTGlrbExPeHZnUDhzTlM3dmhvR2w5c3UxU2tZV093eUZjeW8?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (9)</summary>

- 📰 2026-11-06 [从10万到50万，VLA智驾车怎么挑](https://news.google.com/rss/articles/CBMia0FVX3lxTE95b0pDV0ZCWUdKMG1mVm1NS0lhOWJ5VDJjeWhIVlVTTlhHREp4bzE3QTE1U1FqM0s4Wms3ZFItTmlxSlN3QkhkSGN5UHZoQ05NUnR2Y1doWTRzT2tRSHUxalpZSzc1QzlRbjlv?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-05 [问界销量跌54% 赛力斯“重心转向”AIVA赛豆](https://news.google.com/rss/articles/CBMifkFVX3lxTE90MlN1VHRnQWVmZUZSMUQ1VXlNNGxacXAtY3p0a1hyRHY2b0NkRUxQQU53OGtFU0dEaUQyQ2ZsOWRxeW1HcmE3SF8xOXBERUpZMTB1YnJrakdoQTB3dDhNU1VNaDVqVzl0X1BOZlZ0UmhNX1FhQWVTYTB3X2dSdw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-04 [GPT-6之后，智驾公司只剩一条路？](https://news.google.com/rss/articles/CBMiUEFVX3lxTE9SazhISDVJc01Sbzg2WHg1ZzREaWdVR2lxODNKb3VpcF9QYkhCUWpHLWhxa3RFV1VZdG1HdW9wblVrVlZKdWM0R1lmUDA3c1ZW?oc=5) <sub>盖世汽车</sub>
- 📰 2026-11-03 [11-12月，至少10款重磅SUV排队上市](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9tUmQ5Z1RpMkVRUGF3Z3Y0NmcyUk9NSy1TeVowSUkzY2VmcWdMTlhkY2gtN1RrUXZNWmRWQi0yVEdPU2MxRVRtbDdXY0xod0lzT2NVRmp1VjNFUlE?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-02 [Toyota & Waymo to Begin Scaling Autonomous Japanese Fleet](https://news.google.com/rss/articles/CBMikwFBVV95cUxQczdaa2pqTnhGbVc2SmVxemkzamNNdFVwWWZ3ZnRlbXU1SW1qX1NpemxvWDkyNWhlMWRTNHBvZ3hnYURVcTVlejlBS1BmcHM5YkVMcE1VOXNWYXJpQWRKa2JERF9VMVZMb0o3RkVrMHNUQnhtWEluTzE0RDMxM3VkaXdmSzF4Z1dTUGdNaE12Q05iOWs?oc=5) <sub>Future Transport-News</sub>

</details>

<details><summary><b>Mobileye</b> (22)</summary>

- 📰 2026-11-07 [Mobileye Global (MBLY) Lifts Guidance Following Earnings As Fair Value Debate Returns](https://news.google.com/rss/articles/CBMi0wFBVV95cUxNOF9fMHVEMXdjcUJ1ci1PZ3hqNnV3SHVHanAwSHc4TzJvTnVPSnlxYzRaekFoLUtETWdTeVFVNzNFY2U4SnNxczlUVjF2bEE4WEFPcXdDRjZQWnhKU0J0ekFGS0l2cnlLVmZTN0o4MjFSMUgwOTJ1UkEwQXREdnZXbTM3VmNpNm42YndkTHBGT2prNENPZ1JHTURJRy11a19YRjQyc1B2V0Y4aXBVamRXeFpzamRYWWpWX1c4eXpWYmdiWVIwUVRYck1OUXZjTElGaFM40gHYAUFVX3lxTE5nb2VZYnRkMGY3a1l5UTJTU1ZJUndzc1VjWHpicnNpRm1pdURTMUwzYWJYeVdYRy1kNVh3UjNub19fWm11eTVLSGVUVEJFTlBDcHExWFhBWFdPZDdsY05FRS1kUEtoRi1RVFROcjIzalJmdVA2amlrOG5OSmtlMUJtMlo0S21IUGpaRXE5b1JvV0xCaEo0OGZPaW9UeWQ0bEZ0d0VQU1Y2b2QzQnh2YzVaSTIzVV9pTUJOUy1BM1puZ2N0SUc0SzltUnotUU4ySDlfR2psMm0tSA?oc=5) <sub>Simply Wall St</sub>
- 📰 2026-11-06 [Mois Navon: On Mobileye’s Success, AI Ethics, and the $15.3 Billion Intel Deal](https://news.google.com/rss/articles/CBMivwFBVV95cUxNZWE4YU1udlFHX2tSMHFJWERQME5TMk9FaVBxRUZjbm81MlVjZDU2V25FRS1DVFdWV3lHZ3IzaUJLaHBsZnJHN3pPLUt0QlhzYU5NaXpkZ3ZDZGVEdGJNb2ZjRFV4MUk1bXllek45NVR3NHFITFY5RUZESE1qUWZmbjJsYnE0eVFtWXRYYU1iM2VwTmZoanZPT0doUUxyY2ZpeDAwLXRzTENQRzJKZXJYNDNheVcySGRRQnlDaURHbw?oc=5) <sub>UA.NEWS</sub>
- 📰 2026-11-03 [Elon Musk: Teslas will soon be able to drive themselves coast to coast](https://news.google.com/rss/articles/CBMic0FVX3lxTFA3WXZ0NzdKSEFxdnJJWWdIZ08zMThvN2h1UllLc3p6RlJrTHBfNTFMcmVKYmNMZGdzWG1uY2NqSzNmUXdGVWFsdzM4TXdoaGNRWFNYQWpYcHZ1c0JEdzQ4VnM4YTczYlNWWE9wYnFGRnFLZzQ?oc=5) <sub>Mashable</sub>
- 📰 2026-11-03 [Conferencia de resultados del 3T de 2026 de Mobileye (MBLY): Eleva previsiones a medida que crece la demanda de EyeQ](https://news.google.com/rss/articles/CBMidkFVX3lxTE1WUVVUTTZWaU1NbGpBZ18zS0NEN25uMnZnZVNqY3RjZnAyTG1CQnM2QlNIYk1pV191TlQyWWJoVXNQWjI1MVZZYkFGU0hMYzBzTl9idElzek0wSVNKRjdTdTY1ekZubDVNS1dtNnhyTGZheHlaTFE?oc=5) <sub>TradingKey</sub>
- 📰 2026-10-30 [Mobileye Global (MBLY) Dropped, What Is Behind Its Latest Move?](https://news.google.com/rss/articles/CBMi0gFBVV95cUxPeV9lYmcxQk5FbDhpNTJzVWw1Nm1OYS1SRS1xdU5YbS1ybXV3MTV5YUtwSGFYTGJvWTJOWHpVMVVraUs2R0VwSmFzbzB5bzFQajNGMVlLUW1KLW9qNWV3eTROMTZwVi1vTF9xeXVxTDNjZWpUbi1pNV9zcnRNS1pmcUNDbkpRUFgzZGtjdzZMeDkzVWVDLTl2S19ESHA3eUFYV29IQmRITWtLRVo1TVFjbm5KR2NHTUR6dTRVS2VjWENEVzdyZ3JBUFNMN2RuVnpveXfSAdcBQVVfeXFMUHNYLTFxZVNVNW12WVRKcGtqTXhPS0c4R1ZBMmtMaWpjMWdfRTE0X1d6bm1rZ0lpVUwzV09LWE1vWWx2bGdhU3RLc2QycWQxMHlIbDdreUVOQXFHWHh2UVNvWFJnci02bmhWcTlqNDV6Nk1lejQ3U05iTDFSM1JYU2Rpbm1pS2pnOWJaNFU1Q0U1bmtEaEJYaWN2dzEyS0pYb1NsMkFDRG5oOTEzaWZuMGtVTHFCdUZ1dU56T0ZmdFBfc3BSSUhmVEs5N3diMEJXaGt0VWluNjg?oc=5) <sub>Simply Wall St</sub>

</details>

<details><summary><b>Aurora</b> (33)</summary>

- 📰 2026-11-06 [Aurora Innovation delays driverless truck produ...](https://news.google.com/rss/articles/CBMipAFBVV95cUxQRklSWDhVZ2l3NXVOMmVHXzRyUURUYmVqVTBibE4zOXlLTEZmdS0zal8zRnF2WEhWdGhoZFJ5WVFZLWhSRE9HQmJmVGROandBODJLRWZEZkhuckpJblpjbFBzUmNlV3RRVmRvaFYzQW5vN2V2Z2ZUNmxnUnJadnI5UTgwbW5hMU1jZzJYY1VaYVhvSEtZYWlzb0VpUGhRZk9ScFItYw?oc=5) <sub>Pluang</sub>
- 📰 2026-11-06 [Aurora’s truck production schedule delayed by supply, quality issues](https://news.google.com/rss/articles/CBMirAFBVV95cUxPeDd1TDk3NlhHVFNnd2U2Q0txeUFWTXFoaWdvVEFkQzh3TXZBOXluQkdsMUVfSFY0Qjg3elpaU3NGZXJ1OUpsSE5oeDRndFpiNm9Va3NaWktVVEo3OS1QWTZEZ24zNGFrLXp3MTNnX1ZKRnkyZE11V2gtQVBTUkktWjhUMXBNY2RLc2g1UmY3ZzVUclAyZjdBa2xQMk42SEl4QllNN1Vkb1dyQUJT?oc=5) <sub>Trucking Dive</sub>
- 📰 2026-11-06 [Webull And 2 Other Top Penny Stocks To Watch](https://news.google.com/rss/articles/CBMixgFBVV95cUxQU0dlSkpCQktPUHgwN3RmTHFPUGJBREh1alAydElPU0hrOWpSbzZ5WWk5dlhvTy1NRlNJNVFyV0c0QjUybWxYcWp4YmxNRUFLbzA1MmVYZnR0ZmRFWDVyR19wcFB6UlVfYjN4c2xKWXVxNlQ1OGdiaDRzdGtRVThkWkNIbkxzSWU0Vi01WUFQUVIyZ2t0ZGUtT3VBLXZ3SGxhYTVWc0Jrb3pZR250NlotMmx1ZVZBUUY5RmhhY0I0d3phMUxzMGfSAcYBQVVfeXFMUFNHZUpKQkJLT1B4MDd0ZkxxT1BiQURIdWpQMnRJT1NIazlqUm82eVlpOXZYb08tTUZTSTVRcldHNEI1Mm1sWHFqeGJsTUVBS28wNTJlWGZ0dGZkRVg1ckdfcHBQelJVX2IzeHNsSll1cTZUNThnYmg0c3RrUVU4ZFpDSG5Mc0llNFYtNVlBUFFSMmdrdGRlLU91QS12d0hsYWE1VnNCa296WUdudDZaLTJsdWVWQVFGOUZoYWNCNHd6YTFMczBn?oc=5) <sub>Simply Wall St</sub>
- 📰 2026-11-05 [A former Apple and Uber engineer raised $51 million to rethink the self-driving truck](https://news.google.com/rss/articles/CBMiqAFBVV95cUxQWEhKMmM1YlR6MEZsanJJZVFvZmVNSnpyQ2JLaDVhLXhMZkJ3TWdNTjVpZ3RCMTNOYmdkWEFtZjJpZDdYYmlyUWlaZDJjV2FSdEJVcTVGUjNqODV1Zm14WDFMOThDYkw4Q0NZWFZuUDF2blFGbDVOdmljTllsM25RSHVtbElKWE1PZFNOQm5aWkxCcExsYWlBZ1pFQk1zXzMxU0MzUHpBcGM?oc=5) <sub>Business Insider</sub>
- 📰 2026-11-05 [Ex-Apple engineer raises $51M to build cabless self-driving trucks](https://news.google.com/rss/articles/CBMioAFBVV95cUxQck80dWF6bkZPS2ptX3IyRzIySDhLQi1RNDFoN2JCOF9oWEFvS2xGS0VWNXo4TzVoSEpYSWxBblQ2bTJjTGI2cHlwRVI3RnRoYlV4Ml9VNm1RUkY1MkJaNDl5OXVWQXZhLUp5SW5jZU52bW9rR2laT183dUhRaWExYm9yNWVuWFhnMkNGRHVNNEpIV2taNEY4azg4NUZJM3lC?oc=5) <sub>Dealroom</sub>

</details>

<details><summary><b>Zoox</b> (33)</summary>

- 📰 2026-11-07 [Zoox expands sports partnerships with multi-year Las Vegas Grand Prix deal](https://news.google.com/rss/articles/CBMipgFBVV95cUxQUW9WR2g2NWlXOElyT3pzX3JtN3JrVGk0T1V2ZGhQM1ltQmw0REpBMDliWWlTUHp0aGxqSjZ2ZUUtX0s4cEV1QVR0Yl9oTVNqZ0d4ZVRRSFdHVUZ2Wi11X29NbmFGMmUxTDljVEJJay03dVl5Z1VvWFZSR1ZNQW9JNHBIUHdMRklyS25vQnc4QldMZ3FndzQ1UnZ4OHl0WXlCbEVCZXFn?oc=5) <sub>SportsMint Media</sub>
- 📰 2026-11-06 [Zoox Lands Las Vegas Grand Prix Deal, Plans Race Rides From 2027](https://news.google.com/rss/articles/CBMinwFBVV95cUxPVFQ2U3dHNVBZQVppMmNOMkNTN0ptWnp5MG9ZZHlnWVpTclhDemtERENlZFFyNVdTVms2Tk1HMjhURW5lUkUzTmJLdTdpUENiaUo0eHk2c1d1UEczSWRTMTNZZ0g5anBKOVRjVHk2eUpGVV9xNy1rYV8yOG8zS3hJNzduVDFJYWVjbVhFTThXb2JHUFZwMEpOSjFodXNEUWc?oc=5) <sub>Electric Vehicles</sub>
- 📰 2026-11-06 [Zoox named official autonomous ride hail partner of Las Vegas Grand Prix](https://news.google.com/rss/articles/CBMi2AFBVV95cUxPZDlNbWJISWVyNEREb2V4eXBXYzltMFFjcnBISHZCbk9IbG5WQUpjbnpOWlBCZU5DWEVrWmxmY1JvT0hZcTJxM2pmOTl5N1NDOGVoQ3ZaSldqcHV0anptUEE4LXhnRFlYVkxoMU55TTUwN2pHLXl3MERxQ2o5c1NaQUlhZHBRMGZCSG1UVUE5NUFSVWdTaVNhd1g5NUx6Wkk1TW1DSlZiMnBKWG5WcndNY3UxVEp6aXh1VGV4dUV2eDVZcmNGdHJFbDBianpXUXg1V05raW9ZUTA?oc=5) <sub>Las Vegas Review-Journal</sub>
- 📰 2026-11-06 [Zoox reveals autonomous ride-sharing boxcar with no steering wheel](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1VU3U1S0hCVl9tYkViNW9GUXA5MGFvNk5WbjBmQ2p4TTVWWWhwX0ltbkx6YlZqU3RqMkkyUUh4cXZyRGUxT1N1S296Q0p0TjB3V3JUMThjbG5tY19CQkFfVjU0WnlrVkE?oc=5) <sub>Mashable</sub>
- 📰 2026-11-05 [Amazon’s Zoox Plans Robotaxi Testing Expansion Into Europe and Asia](https://news.google.com/rss/articles/CBMif0FVX3lxTE51ZDBrdXB0elVyTkNPa21PMG9SX1ZyV3d5MEpNb0F6dkowbGFuSTlDWjk2eFBoVklLQ3E2S0FtV1NKVXdVMHA0LWFHaW1UWVZaSzIxcE0zaFN4SDFQSVRaQndfU2l6WGNXZk5iVGpaU1Z1T3B2eWxUYjV3NWE5S00?oc=5) <sub>Drive Tesla Canada</sub>

</details>

<details><summary><b>Motional</b> (11)</summary>

- 📰 2026-11-06 [Uber CEO Dara Khosrowshahi Ramps Up Robotaxi Deals as Freight Revenue Jumps](https://news.google.com/rss/articles/CBMijwFBVV95cUxPaEVFaUVkcmt0OXh0V04yS3pYeW9ZVXg2aUxTV0g3TzhoQUZPTVQ5WmFSUlVFR0ctMkdoc0dlcXpyTXdTdVJoTjBhRmxrVE9pdzUzVkN6WGE5b2RMSVhBblhBU3lHcjZvY3lVVmZPWExpbWRESTZ1c1dTZlVOSEczRzdVX3dIMmV2ZkcwSzZ3QQ?oc=5) <sub>Observer</sub>
- 📰 2026-11-06 [U.S. Dark Money Tries to Stop Robotaxis as Japan Says Yes to Full Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTFAtLTNZbVB6ci0xRTZJVzUzMGFDekxRbi1SQmFhV3VvYTc5b2JVajctSjNJYy1PZG9QeFBHVWp4d0pwNHBhQzUtZUlMVDdRQy0yUHpBaWNoVFRfbllyTVNn?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-11-06 [Uber to have 700 robotaxis by year’s end](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPd2RBVXBVbTU1WXVPckdkVnh2RGh0UDI3R3Y2MjNHZlBSME56WFRYN3htTmNadGpHcngtdjc5OW9zRmZubjFmMlZxWWJNbVllNk42bTZNMURvSWZiV2R0WklUdHA5YW9FWjZRSHVnVG9LbXBDWExDSVl4eEhDQTFZWkdyWk54bG1YQWp3?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-11-05 [Waymo Roulette on Lyft in Nashville Field Report｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1vbUxkMzIwb2EwZGxIWWRvQWNOMWRKMUZ1cXJJNV9waEJuWVRvWDl4cG9XYWxNZ0d3YkdmNG9JT2p1aTFLRmRJT0RDN1hBR2dGQ0lOZkJlUi13TmhlT2hF?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-11-05 [Uber Targets More Than 2,000 Driverless Vehicles on Its Platform by the End of 2027](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBzZFlLN1hTWk0xREpRTWl4dDBLTWxzV2QzTF9xU2pNRFhaNk9VSV8yNGVYamJzVk9kbVp4Y09TWDVIdmduOUpSU1JiRzhXMHc3d2pCMlBtNkw?oc=5) <sub>www.tokenpost.com</sub>

</details>

<details><summary><b>comma.ai</b> (4)</summary>

- 📰 2026-11-06 [Canadian YouTuber Linus Tech Tips Tests Tesla FSD](https://news.google.com/rss/articles/CBMiggFBVV95cUxNZVZaT1Q4X0NlakJzTnFkTGdqTmFPM3pDbFZPUnBYVVNrVzFxMlpZQ3VaTEJFUmJrNVpjMmZ5RVphUDE4WURNT0x4NkhnN01LdTdzSEVnS2NUNkROams2cnNzNkpnalhWcDVuckhETUtxaDZrSHNXTXhKYUlpN2dPTlZn?oc=5) <sub>Drive Tesla Canada</sub>
- 📰 2026-10-29 [We Upgrade Our comma three to a comma four: Is It Worth It?](https://news.google.com/rss/articles/CBMimwFBVV95cUxOVkgtNU9hLXVYM0U2VjNpVldsNFFoQm53SjJGcU1CcnNMWXY5YzFYdVhoYlNZdG5vX21Va2h4b2RLYTNEUTBLdUFhMXd5eTVjLXBSTHE5bFN6elNqa1diTThPQ0Z0Mlo4SldDTzQ4eGxEWl9NTjNKcUNGQmhLeGRSMUxOSElpMkVNOTN4QWhMV0hPRFFJV3cyeVNLSQ?oc=5) <sub>Transport Evolved</sub>
- 📰 2026-10-29 [Aftermarket Self-Driving Devices Face Federal Investigation Following Five Crashes, Three Deaths](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPUG8ycGN4Tl96dk4xZk1yTEJrVkpvVGNsX2JnbWJoeXlzS1ZsVDlEYWk0SnFQQTZXQXpfN21BU20wR1FmR1lsUFpoeHdzU1BUaGdheTZ3LUFkVnpaOHhyWUU0YU1yWERQYmI2TDRnd1VpbTM3Ui1yWFdQVzZIRHVrUEhZUFBKcGpM?oc=5) <sub>AOL.com</sub>
- 📰 2026-10-29 [A $1,000 Device Enables Hands-Free Driving. But Fatal Crashes Have Prompted Scrutiny.](https://news.google.com/rss/articles/CBMixAFBVV95cUxObnRHUXNNS2wxNVFWeHVLdm9qYmZ1bnpaUVN2VWJ1eHZhbFRiWGxoVWxaSjNuNzNKQXZ0RV80dVRnckFGc003eXZJeW5ZWkhUakpsdk9sQ0lnQUZZeVNGekRzYmhvR2RrU1Ric29JeUFmQzNNdEE5NEtZLUgyS2hmQ1hwYWlMdFNDRHNZQVB6dHNqUjIyaXpRMFd2c0YxN0c3Vk9yZF9kR255QmtTUlRiaEtYbDY1dHVZQm9ReHY5WUdMSzJQ?oc=5) <sub>WSJ</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
