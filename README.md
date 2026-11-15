# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-11-15 · 1,270 papers tracked · 47 curated.

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
| [GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives](https://arxiv.org/abs/2609.39601)<br><sub>Qize Yu, Lianrui Fan, Boyu Chen et al.</sub> | arXiv<br>2026-09<br>📑 3 | [⭐ 438](https://github.com/groundingpi/GroundingPI) | Precise grounding matters |
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
| [SimWAM: A Simple World Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.07468)<br><sub>Zongchuang Zhao, Xin Zhou, Tianyang Xu et al.</sub> | arXiv<br>2026-08<br>📑 15 | [⭐ 209](https://github.com/H-EmbodVis/SimWAM) | In autonomous driving, World-Action Models (WAMs) have improved end-to-end planning by transferring video dynamics priors to action prediction, but many still couple planning with future-video generation at inference, in… |
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
| [DRS-VPT: Directly Relocalizing in a Scan with Vision Point Transformers](https://arxiv.org/abs/2609.12557)<br><sub>Lanke Frank Tarimo Fu, Maurice Fallon</sub> | ECCV 2026<br>2026-09 | [⭐ 18](https://github.com/ori-drs/drs-vpt) | We present DRS-VPT, a feed-forward transformer architecture for foundational image-to-scan registration |
| [Horizon3D: Sparse Radar-Camera Fusion for Long-Range 3D Perception in Autonomous Driving](https://arxiv.org/abs/2606.31096)<br><sub>Geonho Bang, Geunju Baek, Dongyoung Lee et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 26](https://github.com/geonhobang/Horizon3D) | Long-range 3D object detection is critical for safe autonomous driving at highway speeds, yet existing radar-camera fusion methods remain limited at extended ranges |
| [Explainability-Aware Frustum Attack: Exposing Structural Vulnerabilities in LiDAR-Based 3D Object Detectors](https://arxiv.org/abs/2606.29963)<br><sub>Chengzeng You, Binbin Xu, Soteris Demetriou</sub> | ECCV<br>2026-06 | [⭐ 2](https://github.com/SecMindLab/Saliency_LiDAR) | The structural vulnerabilities of point cloud-based 3D object detectors remain poorly understood |
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

<details><summary><b>Waymo</b> (156)</summary>

- 📝 2026-11-05 [How the Waymo Driver Manages Severe Winter Weather](https://waymo.com/blog/2026/11/winter-weather-preparedness) <sub>official blog</sub>
- 📝 2026-11-05 [Rethinking What Freedom of Movement Feels Like for Women](https://waymo.com/blog/2026/11/because-women) <sub>official blog</sub>
- 📰 2026-11-14 [Elon Musk Ally Jason Calacanis Bets Another $1M On Uber — Says Waymo Team-Up Could Steal Tesla’s Driverless Crown](https://news.google.com/rss/articles/CBMi3gFBVV95cUxQSTc0N2VLYVlDOHgwVEV4RUpjZjByeG83S25JdHoxZ1ZkaEx0aVZXUXdCeXBqZ0lZRUpaajl3Wm1hUXhQeWdoWXlSRnlreFZpRW40aXpnemEzU2FnTU96NWlEbzNOc3oxNGlyNFR5OG1tellaMG9ac2NNNl9GV25USlNlVnk3b1E4ZnNLQkw3cWc0OWZpdVZxQTdYbzg3cHkycjFSZTJLTDE3Q2F3VXhHNVRLc1ZCbHpkbUJpaXVNcUh1bE5VYmx3dDRZWHNkWTZmcXh2ODlrNnRXeXdrLXc?oc=5) <sub>Stocktwits</sub>
- 📰 2026-11-14 [Waymo Co-CEO Says Company Considers Footage Requests Through Formal Legal Process](https://news.google.com/rss/articles/CBMiW0FVX3lxTE82aG5XOE1aYnY2Wm9xckI0bnVFR3l4Wkt0bHRKczFWa0JIeUlTSkNUeWpfNGZYYV9zZ2x2ODVQaWhoQm1iS1NtZWl6VE5HcTZLUnJ3Q3R0eWlCUzA?oc=5) <sub>www.tokenpost.com</sub>
- 📰 2026-11-14 [Atlanta already has Waymo and May Mobility. Now Atlantans could see a different kind of robotaxi roaming the streets. #atlantanewsfirst #crimewatchatlanta](https://news.google.com/rss/articles/CBMiUkFVX3lxTFBHU2RzM2pSNUhsTTg4RnlnUWFndF9HajVfZnhqMGVFaWdTM2NQcDBPRVBrSUtsbnJ6YnB4OUt3T2wxOGFUYU1xVmEyRk5YZnliV0E?oc=5) <sub>Instagram</sub>

</details>

<details><summary><b>Tesla</b> (220)</summary>

- 📰 2026-11-15 [Tesla FSD Deer Clip: 41 mph Claim Unverified](https://news.google.com/rss/articles/CBMic0FVX3lxTFBYcDFvem50bC0wUllMZGxaNU1HMGlQdGZwcEF2VlEyNTFMMFVMOXk5aTdEVVFwbGVObWdUeW9KdGhvQ1JUZ0tUQno3eEVVTkI3VC1PbXY5NlN3aDAzZ294eTFQUTlBQ203RzZ1aUF6T0plRVE?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-15 [Tesla makes major Cybercab announcement as driverless vehicle goes on sale](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQeWRiUWowYWVmQW9OdUFReWE4cDdfWDlZSUVJNURfUEp3UTJncjFBQVVwOVhxcVB1dmpfSkJNYVhmQ2lUM01YNHUwTzRDX2VNdHdWenNkSjN1RTFpM1ByeG1XeElsdDN6Yl8xSnlsZnlqUUtDY0VyVU90c1Rxb3JZdmM3M0czSVRTUmI5V2pVRlRVQ0VYMi0zckIycFM3eWtEcEhnTXpEa29iUlHSAbABQVVfeXFMUHp6UmxGSl9iLUxTY3hhSmRUYkNZcHkzck16VVprb3pqVE9nUnRrdDJKNWxpYUZybFNrMkt2WFFZejdJdkxBMDJESFR0N01rRTJoVGxVa21uWm1zbFk4aXFaT093SVRVQlFuaWU3aDh3MGkxeERGcmJCbzFkeTc4dnRORmFyU010cjR0Y0I3bW5RU2hweUlmQU1xVFFiZzlfN2Z0SEJubUhxR1BOel85X0U?oc=5) <sub>Fox Business</sub>
- 📰 2026-11-15 [Tesla Cybercab — Driverless Robotaxi Available for Personal Purchase at $29,990](https://news.google.com/rss/articles/CBMic0FVX3lxTE96QXJDblp4di1zdko0SDdYOV80ZENpbHdCTFp1ZFllVTlzMU5tNHU2bkFqOFhMOGtEV0dORnBzbGpsUzNJTjF1WlZidXFjUUJONTB6dzBUQkJuc2ZWOEVpcUwtb2NySEhZM1NlVWRhaG82VkE?oc=5) <sub>The Korea Daily</sub>
- 📰 2026-11-15 [Tesla sells the Cybercab privately, but keeps control of the car](https://news.google.com/rss/articles/CBMieEFVX3lxTE1NY0taZTJ0QklMRmUxRmIxWTU0NU11X0JLYVhjX3RnTWt0bm9YbVFQMnYxc2FaVjRNeVhBNUpfTHpGR0tnRzJacWN2aGd6R0I4MXAzUUQycDZNZzBqVDhnNE1qdnVOWFBDS0phVUI0NmJwRVZ0djdORw?oc=5) <sub>AutoNext.co</sub>
- 📰 2026-11-15 [Tesla Sells Driverless Cybercab to U.S. Individuals](https://news.google.com/rss/articles/CBMiiAFBVV95cUxON3Mtd1hTRzdJRnE3bm1vc1BBQmVKSTZ3NU5nUmd3bnItWTBfMUUzSXBKQmRxZkhXZVNCRmphdFUyZzR3WFlZMnNqc1c0NFMwRUlWUWdpeEtNRDl6R0tKNUYzdWk1OHJQTzZrSDNycDZGLTU3c0lhVzhzcGF6ZDFnWnNyS1dCYnEz?oc=5) <sub>조선일보</sub>

</details>

<details><summary><b>NVIDIA</b> (139)</summary>

- 💻 2026-11-02 [NVIDIA/nvperf-core — Core NVIDIA Nsight Perf SDK APIs and libraries for collecting and analyzing GPU performance data directly from application code.](https://github.com/NVIDIA/nvperf-core) <sub>GitHub</sub>
- 📰 2026-11-14 [Weekend Drive: Nvidia’s auto future after Jensen Huang; Toyota revives Scion](https://news.google.com/rss/articles/CBMiowFBVV95cUxQamlsYmd6QzJkaWNTa0Nqb25jRzBCUWIxczlYTXhoTVR2OC02QXNPNXNLbFo0M2dwbWtoSllDNWZPMkZ5c1dEcHhKaGt2c2pqT3Rxa0V2MWFWWTBBOUFhVWdDZHBkM1hQaGJjUVFxLURGZnozREFMQlo5RWFkZXpqMmxKeVl6RmFwYTdwakQtTmpwa2t1NFMtWFJUS19ta0tGeUc0?oc=5) <sub>Automotive News</sub>
- 📰 2026-11-14 [The Nvidia scandal is heightening America's AI rivalry with China ahead of Trump's visit](https://news.google.com/rss/articles/CBMisAFBVV95cUxNZVM2T1MwenMySnV6SWdfX1hoRDM2VXVBcEpqekZWeXZaWDJ6dlJNODdQYXdEV3ROMFlZUXlkdW45OEgxOHoySTRBUFdsay1kZW81OFJhYmtaSVR5WWZPNmZmRW1ySmptR1RvanJjQU9wOW9ON2FSVmJERElfOWMwQWNBcHdYUWN1aWxCeFJ0bVJWbjh6ZmhBYUpmTDRJb0lsbVU2V2ozQzg5SUFQbFlPOQ?oc=5) <sub>Audacy</sub>
- 📰 2026-11-14 [Trump is taking Elon Musk on his Asia trip, but he plans to avoid talking about Nvidia scandal](https://news.google.com/rss/articles/CBMisgFBVV95cUxPNzBXYlhwWFlvT2ttTkhiVjcza2R3NUlXSHp3MjB6MUdRaWhKNVFSekcxNzk3Y19Fa2o1UWZoWkJYMzVfSkl4RGRMVWpXdE1iTkU3NnZUWHBTTnI2RnJOMUV0UWZTbE9IcjY2WHc3Y0VQYk14aU1aSXBpOUdJaEFyQWNmUzhKQVZqN0k3Q3BtNTFDTE5DZXZWVm1Dc21qMkdDWV9fTE5MSFFFLWZ4eW5mNGp3?oc=5) <sub>Audacy</sub>
- 📰 2026-11-14 [Nvidia Leadership Reshuffle: Why the Automotive Sector Isn’t Panicking – Key Insights & Industry Impact](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1kSEdoX0tub1h1eWVpZVNYdlNFSDNZTFp2Tk0xYW9SNTUtSmlnR05RRk51YXdGQjN1eG5FUzdCZVJWVU9JYXBzVnQ3anpxb0N6cDMw?oc=5) <sub>36Kr</sub>

</details>

<details><summary><b>Wayve</b> (39)</summary>

- 📰 2026-11-13 [The Verdict Is In And The Brits Lead The World In Detesting Self Driving Cars](https://news.google.com/rss/articles/CBMibkFVX3lxTFBJZWtXTkdEQVRoMVVIZUhjbWZkQXJla04zZ2dteGxMQlp6LW9CSGpIbjNJSFhXdVN4VkxIVnZvdGNMeTNoTlNrRUdjeVcyU2RXUmJOZThLOUtNQmpfNmNZeHJRYzJ3LTg0bXJiX1NR?oc=5) <sub>AutoSpies.com</sub>
- 📰 2026-11-13 [UBER - I Think the Market Has Uber Completely Backwards](https://news.google.com/rss/articles/CBMi3wFBVV95cUxOV3ZEb3N6WjFIOTJ0b0llOFFrQ05ONFNtSUM5clg3ZTlpVlZjWnhIeDBwTzloWXZzamI2cXViQlg1Y09TQW9MZDhxakUyY04wNU1XVmVHaFp4eVpYNnhpYzFtS2lIOHpDaHFHbS1FaVdwd1FqQlFzLWd0czBOcjlrUHZEOEJlaHdBVVFXU0FVdG55akdLbVlhOGwyS3NVY2RDd2V2V1EwNE1pbEhNSUhOS1E3ZWVQUG1OSjIxSDU5VlZtbEZlYWpBZE41akh0RkxiZlYzc25WSHhOLWdRODlZ?oc=5) <sub>Simply Wall St</sub>
- 📰 2026-11-13 [Nvidia’s Interim CEO Inherits Robotaxi Bet Jensen Huang Built](https://news.google.com/rss/articles/CBMingFBVV95cUxNMTZobWtOZjZDc1duRG85T2tIVE05NTZ3cXZaQnE0Y1Z1UUJETGJONDJGX19mZ00zUGJkXzVZdmJGRV9VeC1kUjQ0QmxOcHotbFdWNmQ4SkM5WXlOLVhYWDNSTURaX0lVM0RlS1ZTTnJjYVBVWEJJLUZNZGd0NkFVazRxU2dTSmF3aDlnem1iYUlWNkQxQXlDZkRTbUNxUQ?oc=5) <sub>Electric Vehicles</sub>
- 📰 2026-11-12 [Brits lead the world in hating self-driving cars, and there's one big reason why](https://news.google.com/rss/articles/CBMiiwFBVV95cUxObEZNNndscVpKcWVER1JFMUVyTmdvOFNtdG9jMnRscHFjLXFMLUtVdjl4cGtkZkFUMnZmV0duUkpCSkY3a2RJcnB5TFNqRGlzbGJaQTlVWnZrMlhkalZRTWhYSVlLc2NnbjBfblVrNXI1RHMxS0lYa0d3M054NDFMeENYZzRLRFhmcnB3?oc=5) <sub>Auto Express</sub>
- 📰 2026-11-12 [Agile Robots Raises 500 Million Dollars at 8.5 Billion Valuation](https://news.google.com/rss/articles/CBMiZkFVX3lxTFB0Mi1XZFA0Rm5Bek12cXNKNHdNZ0lBNTF2bHE1TzZ2b1ctQzVURXFVVnhlTFdGejNmb0NvTFkxbXBzcENjc29oX1k1VTRib0NzS0pRTkpFajl1UmRBQTJKeVREdWpGZw?oc=5) <sub>SuaraGarut.ID</sub>

</details>

<details><summary><b>Momenta</b> (79)</summary>

- 📰 2026-11-14 [东风日产NX7预售12.99万起 三版本搭载宁德电池与Momenta智驾](https://news.google.com/rss/articles/CBMic0FVX3lxTE5hbzdXLTZqaXVxYWxQNkw1alcwZDJHc3Q3Q3RfLU9Sc09xRUlxcUItR3VEVzI5TDlvbEd2RDVBdXdlY2tYZ09mS3RvZlZmemFwanpReFhQSTVUQ1BGUXRoQ0hMNzdZaXRLSXg0Mnl3aW53Q0E?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-14 [东风日产NX7顶配预售14.99万 搭载Momenta智驾](https://news.google.com/rss/articles/CBMic0FVX3lxTE8wX2x4UmlfaVBwWUt2MUdYMXFaOFRDQlpPcHA3dlFFbnR6NVdQbnp2NTJXQ3FIa000OGtsam9xOW51bTlYd1NKR2dZSVlnWVNIb0tZQWRNNmptYTVSdXBNc056empRUUNEdXAwWnZweGtGZjQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-14 [【视频】MG07重磅智驾Momenta R7即将登场总经理评价：急性子的老司机](https://news.google.com/rss/articles/CBMia0FVX3lxTE14Vjk2dk9zVmM0dzl5c2RlMGgycm5pOEFZVjBLLS05RWt5RW1DcnRmSHkxdjhsQ0l5M2F1VERSZFp2TlhaeHBTam5WQVZuTzdKdGRSWF9KTmxsV0xVcUxmYm45MjVkLTlyMkNV?oc=5) <sub>车家号</sub>
- 📰 2026-11-14 [上汽奥迪E7X将OTA升级Momenta R7智驾](https://news.google.com/rss/articles/CBMiW0FVX3lxTFB4OEkxeTlJNlRMTXBDdVEwU0dsS0g0TF8ydFNyUExrOGpMQW9oSklTVEJYV3JUTDF6M1pWTTVEc0I4NmIyQzVOV1NfbnpIaVZYOWU0T1FIeTVCZFk?oc=5) <sub>车家号</sub>
- 📰 2026-11-13 [15 万内插混带激光雷达，这台日产把“沙发”和“智驾”都配齐了\|Momenta\|东风日产\|宁德时代\|激光雷达_新浪新闻](https://news.google.com/rss/articles/CBMiY0FVX3lxTE5QRXE1NUYycG1XMFN1aWM1bU5UbnlDcEp0SVpXNUtyd0NtbDZXT29md0d1dFk1MWE2OS13Y29MMmdJMWt0N2tqZ05fSjVPd2FNNnVuNzBoREIybWlNbENVczJWMA?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>XPeng</b> (140)</summary>

- 📰 2026-11-15 [25万预算新能源SUV选购清单，小鹏G9L与理想L6、乐道L80、智界R7横评](https://news.google.com/rss/articles/CBMickFVX3lxTE5YNnpSUXhOakNJSFNPR0pXY25zelprRzlIcHRDbkRseGx4a19uMWx5R1J0QzB4S2xxSmRaaWROd2FIVjBLQkxLbVdPYWtWcFowTWQxTGExTFQxMHlhUmdrVU9FVUxRWHJNdFFyQXNMMjM2UQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-14 [最近这波新能源新车怎么挑：小鹏G9L、理想L6与智界R7横评](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9Eb09fWFFtS215VC1ncmNaZWxKRWhYajQzMzdaY1lVdTNSRGZrN0N5TFVMRmdOT1FKckN2bjFUQS00eGNLaVd4TzVhQmNLY1ZDUi1yLUgxTmtJVTI2R19Z?oc=5) <sub>新浪网</sub>
- 📰 2026-11-14 [智能座舱与智驾横评：小鹏G9L、理想L6、问界M7、蔚来ES6值得看](https://news.google.com/rss/articles/CBMickFVX3lxTE1fZ1hyZjVid0dSVGQ3MVJ1VzRieUdGcWxvYVVjOUdZeHZFdFIzZEFMSFhUZkktN01BVWgtckoyV3M4Q1Z6Z0V2SEVjbmhaQlJYM0ZSV3hRV0VvalBmVUUtS2JvbEdrUEw2aTFrdzNENm43QQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-14 [25万级大五座SUV推荐：小鹏G9L入榜，与理想L6、乐道L80、蔚来ES6怎么选](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBucGFRWm16ZmFaeUl6RThDdFY4TXoyTjh2XzB1cW43R0lNa1NWN1ZNU2VLX25tWXpkVzBCX0VnN3pJd0E2Y3JoT2s3eUpGR3ZtQ0E4a3Q5NHM4cm5WMElJ?oc=5) <sub>新浪网</sub>
- 📰 2026-11-14 [小鹏G9L对比理想L6、问界M7、蔚来ES6：智能大五座SUV推荐与座舱智驾横评](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBYc1FWVmFtLWcwNUEwUnFqaDVTOXBIRUp2UGZBelhMRDNzUUFfMU5qT0p4bkJZYncya25jVWFIQ0t3OTRZT3F2MVR0cTVQTUtDLXVNTGJxNUVrazBBMS1B?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>Li Auto</b> (149)</summary>

- 📰 2026-11-15 [小鹏G9L对比智界R7、理想L6、极氪7X：智能大五座SUV横评推荐](https://news.google.com/rss/articles/CBMickFVX3lxTE1nTW1JYlZVdGIwYVVHc1FNQW5JbmEzNTJ0eU9xYl8xenpZODdLdUdZSGFBemZjMUdYSG9PYzlxWmYtdzF3YmV5aGpMVUpSX25ZajFIaDIxSmZEcmN1SVZ0MEk2UDJYZ1hMU080a2ZxT1VVZw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-15 [理想MEGA 2026款值得买吗？50.98万配5C超充+后轮转向，3个维度说清+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9jbVExR0RFOVZBcTJ2MlZ5RjY2dDBFMS1YSW9DLU5jT2ZHZVpUekpZcXBDTDhUQUwzbHQzRFlUdy1oWklfYUFPUWpyeXVaM3ppWTNTb1NxSWY2aTY4Qjdr?oc=5) <sub>新浪网</sub>
- 📰 2026-11-14 [跨省自驾、露营、三代同堂，四款大六座SUV横评，奕境X9用三排平权和增程1500km作答](https://news.google.com/rss/articles/CBMickFVX3lxTFBfMXdBRTNrZ1oycmxtdzdNUU1oYVNiT2hfV2xBXzFKRkhlb3FfNGdDQzB2OEQ3cDc0UGxWNUpsVno1ci1lMkV6bVZLTFotYkVRVXlMa01oM0JxVUtjRWFfUm5zX3I1UUlfV0N3cE9zU1UxZw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-14 [理想MEGA高速续航实测打几折？3个维度说清值不值50.98万+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE5sMmtab2ZLQUhDVmlCR1ZjMkdVeHRaamhBckNDemQ0bWhFdGtaZEpUTWFWNTdYcV84R3NsUlJMSUFMcy1mNEg5bWtldFF6VjlJMU9mY2N1a2JSRnJ3ZzZpc2RhOGdZMzRyZXY1clU0LXI2UQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-14 [Nissan NX7 opens pre-sales at 129,900 CNY as N-series retail slides 14.5%](https://news.google.com/rss/articles/CBMiqAFBVV95cUxOUktiWnRPTWFnY3pXbkxabXU4bDRWOUxvZTN4TUdzdkJqVW5BZnNpaEl3dldXYS1hNTZCMXdGQUNSUHIxWjkxNm5JSllKZnN3a0h5clBhMjdLdFVSdm1sNzQwWWMycE52dS1lNXhzcjZjdVpVVnliUWZTaWRqMlpjSnpYODBSeWp5MDVKbDh2cThLRzlwajZJTTRGU0x1TzVDZ2NHTjZCai0?oc=5) <sub>GlobalChinaEV</sub>

</details>

<details><summary><b>NIO</b> (113)</summary>

- 📰 2026-11-15 [蔚来EC6值得买吗？3个维度说清35.8万起的真实产品力+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5UNWZYQm52emFGX0NNMmE1NVFSSUZlU0FJU01JZTlic3Fma0pYWjZmYkNRTE53SU1mcWIydTlucEd6Unl4dVgxZE9xYjd1TEZWc2xENl90Y1VrTVZnbnNV?oc=5) <sub>新浪网</sub>
- 📰 2026-11-15 [【视频】买下！24年蔚来ec6 外南极星蓝内丹霞红75kw买断](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5kMndaZEZPdVhHRnRsdkpMZ0NWaVl3ZEIxUy1TYWwwcEVwcG1GVzd3cVdLWXIyTVlvbWhvY0x1WFhGZ0lNR0ZEOWFhRlhxckZoeUl0dnVmWkNTRWs?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-15 [二手报价12.98万，蔚来ES6，行驶9.7万公里，0次过户](https://news.google.com/rss/articles/CBMia0FVX3lxTE5qQTVwc1NfQnJMemdfcmVucGpzV05rNm1COXZvSkJZLVRxTnF5enBMZndvN1lMZnh4dERtcDJ3WXhKbUpocmtPMEMtM0NKZEVkSDBxLTd5T09qZzU5VmZ3dW5XM3pxTjVzWDM4?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-15 [小鹏G9L对比理想L6、蔚来ES6：家用新能源大五座SUV盘点](https://news.google.com/rss/articles/CBMiX0FVX3lxTE04Y2pybjNJOFF2WmdSYTYzUDh5QTVhc1lXTUNZcHJvTzJkaGdoQk85Mk5XdFNmaVBZS1NydnFVSkZQdF80eTVLWFE3dmNfSldKbkhfakhVb01KLUtkM01J?oc=5) <sub>新浪网</sub>
- 📰 2026-11-14 [【视频】蔚来ES6 2025款 75kWh](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5UOXczZV9KNnlTcDZ2N1dNS1Y2OXliMDBEbS1SQ05ZZlZDbUEzV2FOUWY0Mks2RXplQ01aSFU1M3lrM1A0ZjlKUnBLZkZpcndBZG5YZkxjZXhYMkU?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Huawei</b> (225)</summary>

- 📰 2026-11-15 [四款华为乾崑智驾SUV横评：20万到50万区间，奕境X9为何把896线四激光雷达做成全系标配](https://news.google.com/rss/articles/CBMiX0FVX3lxTE8zamFYbmhWZWJyQ3dqSkRCdUJLMGJORUZDZmJsa1ZqYU9MUUJ2Y2gta2xQWlFQQ3psYWFSMXo0WmVWY1NKSUpmVE5yVXQ1azJDbXctZkZ2UkJ6dWZvRDdV?oc=5) <sub>新浪网</sub>
- 📰 2026-11-15 [ADS 5能不能全系标配？3款乾崑智驾新款SUV横评给你答案](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9Hekt6ckZGNm44YlJETlNJMlBrNEFBRnZTbm5vVTVlaEt2S3pZLXFBMGlqTlhkTDU4ZW1Fd3dGVzRfZXNJRnBFSGVOdkJzMS1MTHllTHoyQXJRWVNSWUJZ?oc=5) <sub>新浪网</sub>
- 📰 2026-11-15 [四款华为智驾SUV横评：全系标配ADS 5与896线四激光雷达的奕境X9，30万级大六座怎么选](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBzWVFTdWtHWldGaXBSUnh6dm9oQVRiSTNwQ0VienNIdzYzTEY4bUtQNHBpaDJwRmdVOUl0LVNUejJocUYxaUE0QklLUXZta0YtaWJMNEZtcTlSbXdvem5R?oc=5) <sub>新浪网</sub>
- 📰 2026-11-15 [四款华为智驾新款SUV横评：奕境X9领衔，30万级全栈智驾大六座怎么选](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1oa09QTjZNRktpUl80Z01sam05ejl2ODdZOG1xZ1d5VjVWYThPY0JyUWFVaUNxSHkxVVZmSXJtamVDcDNiVDdpbURrTXZvZk9hZHM1WWRCNmFJeVc3YXJz?oc=5) <sub>新浪网</sub>
- 📰 2026-11-15 [三款华为智驾SUV横评：ADS 5四激光、鸿蒙座舱6与30万级家庭旗舰怎么选](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1CVUxpUlVVNnhWbVVhNnF0M1FkakpyNFM4aUs3ZC1tQmVtVTZRWnFLTUczUS1OWmMzS1VIVWRtY19mdVZuVWkwU3d2TVVZYkRlaDdPLU9TYTV0RUJJZnZz?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>Baidu Apollo</b> (37)</summary>

- 📰 2026-11-14 [Baidu heads into Q3 earnings: What to expect?](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNNFR3VVdfal93LWFoWl91SzRaUmRLM05vTzFLaUdGMG1id21zRmE2eHJocmFJMzdPMDhZMnkzWHBBZmtFYTZmekd1UnpRSDdKS29oaV9Sb3lMSVJDakw2VmtuazE1QW03a1FWeWlvTVdWd215WjM4a0pTYkYzbWpzbXRXNWhIZUVfcjBWXzRrTDlXQnNDMGFXeExadzI3SEgwRmh1QzU3WV9wUQ?oc=5) <sub>TradingView</sub>
- 📰 2026-11-14 [Baidu Pledges Apache License for ERNIE 5.5 AI Weights Due This Month; Base Model Bars EU, UK](https://news.google.com/rss/articles/CBMi1wFBVV95cUxQRDYxc0p6aDJZWkkwSW11YlJrQk5yQ0hUN1Mzbi16TlcwSVNrYWp4RHdfTHlsUXVOWXVEbDhwQ3E1ZlR2MHhGeXA4cnBwMWc4aTBPS1QtMTJKd2F2Mk4xMDRsbXhQczBHdHBSMjBLVy1WNEFQeDh5Y0UyZWloMjc2LTFIcTlNdXV5ZTRYbmR5V0YxMEc3Tm9yTnFCdndEQVB4a3FfMmU4MFVVREVjNERsN2ZPR3owY21rLVM0WTI3Q0RmSjk0MUdlVjYzdFlaZkF4M3N5MVpBWQ?oc=5) <sub>Tech Times</sub>
- 📰 2026-11-13 [鹏城迎APEC！无人车穿行深圳，外国嘉宾直呼不可思议](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQZXEzdEFHZkF3VE1IUG1XYnlfYzdOWWw4Tkh1a0lCemZ6Z08wbUNyYlliZ3RsYUc1YnR6SlVhNGNrYXNNQktyLXR0cVFJaVl6dlBvR3g2Nm53RUZ6RF9kX20zU0lDWW5zN01OR3IxczF1OFRNTENiWmhKdGo0dXlPVG5RS3RPUnYycXlV?oc=5) <sub>Sohu</sub>
- 📰 2026-11-13 [Hail a Robotaxi: Where Self-Driving Cars Are Already Normal](https://news.google.com/rss/articles/CBMijwFBVV95cUxNd1FvOVRITjBwRFRUYUQtVjlSWjRqQjRHM2lBXzBCWnBSTF90bzQ5MkEwSG9sa3F0ekR6bF9GM1d5QWQyOUdKQk9XdGoyaUVjQXZjVldFcDJ0amZENkVOOUNSc2tlZlhXS0JESWJmRmFidlBVaXFrYXZkZWZOM0JPQ3Qybk10S1RSc3p5WGM4OA?oc=5) <sub>Yahoo</sub>
- 📰 2026-11-12 [百度李彦宏：今天的具身智能大约相当于2016年前后的无人驾驶](https://news.google.com/rss/articles/CBMidEFVX3lxTFBEal9NZExGTzFna2haSzdhSnVwR2VLZDA5dm81MjFmMXJhWFcwNEJXMTBxc0NzTEVFY2dvWi14d1Z6RUxkREpsNkd4N2JoSjdQMDVnMjgtbkFiRWJYejQyMUFYS3gtcGxtSXA1aUJLUVRjeU13?oc=5) <sub>金融界</sub>

</details>

<details><summary><b>Pony.ai</b> (61)</summary>

- 📰 2026-11-14 [小马智行(PONY.US、02026.HK) 2026 年第三季度业绩电话会｜长桥证券](https://news.google.com/rss/articles/CBMiU0FVX3lxTE9IVDN4YkNZajJEX1hEYXNpeDZNV204M1lzU3F3SmUtN29NbDVSUExzU01KeTZJRXJTcXBJOUVXc0t0WGFvcnpzQm93UVFZY3loWk1F?oc=5) <sub>Longbridge</sub>
- 📰 2026-11-14 [丰田铂智4X无人驾驶出租车，能打过小鹏和特斯拉吗？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE14UXZYeUlOMV9SM2VMZ2tjUFIxU1ZldHlLX0pMOTRKaXBLQ19HLWc3WjlJQUd3UTdKUm9UY1JSUWZxTzdjTkxGa0RBdEF1WGttbUM1RTZTZTY3ZE0?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-14 [金桥菁英交友派对季走进EKA·天物！百余名青年结对共赴一场“城市约会”](https://news.google.com/rss/articles/CBMiVkFVX3lxTE9kNVh0SmlNMlZLdzdxVDZ5NUlDNjdOLVNLUUlELWhrd0kxYmlyYi1JX0U5d3RZNWRzb2hxOGkxMHhEZW1yd0pweVJFOHZiVzFQT2tDc0J3?oc=5) <sub>Sohu</sub>
- 📰 2026-11-13 [小马智行将于11月18日盘前发布财报，一图速览分析师最新预测](https://news.google.com/rss/articles/CBMisgFBVV95cUxPYVcxVjZZbVVYNTdjclg5emVCMmlOb2VDU0t5SXZQblRNXzEwSFpIU0VLbGktTHNRaHZad2ZNdnUzcDJ4cFBsaDJwSkU3VUJ1amFub1BGa2N6SjJwUHhBanltbHVKeHJpSlZwZE1CdVdpb04wWVFGcXFfbG5uUWU1MXJzcWFOeUx6NllWU0dWLWtsOGRzT0J5ZHRGU09xUm5acUFCZml1eGFyX1RaNnVlOXhB?oc=5) <sub>Moomoo</sub>
- 📰 2026-11-13 [Hail a Robotaxi: Where Self-Driving Cars Are Already Normal](https://news.google.com/rss/articles/CBMijwFBVV95cUxNd1FvOVRITjBwRFRUYUQtVjlSWjRqQjRHM2lBXzBCWnBSTF90bzQ5MkEwSG9sa3F0ekR6bF9GM1d5QWQyOUdKQk9XdGoyaUVjQXZjVldFcDJ0amZENkVOOUNSc2tlZlhXS0JESWJmRmFidlBVaXFrYXZkZWZOM0JPQ3Qybk10S1RSc3p5WGM4OA?oc=5) <sub>Yahoo</sub>

</details>

<details><summary><b>WeRide</b> (90)</summary>

- 📰 2026-11-15 [【视频】原生后驱云辇- C 守稳第三代元PLUS A级纯电爽开](https://news.google.com/rss/articles/CBMia0FVX3lxTE1DNWM4c0tZSTV4UnlocVpxWjFSVVRZWEJHUWZtLWMtWG9rM3ZZbWJ1ZUY2Zmp1bzhDMnFsQTZvaHZ6N3A0YkFOdGNkZF90aWxiaWZXVGxvU0lUYm9uNXhoZEdkZG9mU0h1N0tR?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-14 [埃安Ray 7限时11.47万来抢市场了](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBpdTBFT3JqdlNZLW9UQWtOaUdYMi0wbFM3Vmk1d2pjaUFqSW13dnhzYjQxQkcyekhXdTZTSm1hdzF4aWh3Q2Q1U05TSFRjMFdzamsyLWdXb0VHYms?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-13 [DeepSeek Unmanned Entrepreneurship: Innovative AI-Powered Autonomous Business Solutions](https://news.google.com/rss/articles/CBMiU0FVX3lxTE9oNDE4amRNYU1lQTZzTnQ0U0pNZllDUkJYSk42UmI1MjZfc0xYT1dmVGRrM093bUowNFpTeHlyRHBIZkJIWVV5UlhCc1FIZ1EzU1ZB?oc=5) <sub>36氪</sub>
- 📰 2026-11-13 [WeRide's WRD 3.0 Adds Another Volume Model as GAC Aion's Ray7 Launches from 114,700 Yuan with End-to-End Smart Driving](https://news.google.com/rss/articles/CBMidkFVX3lxTFB5ekNRVVlteEJhLTJZaVdkNk5CUEVZR3RKTVJiX0tpdzQ4eE5DY0F1Z05XSDkyc3lqb1ZIUzRFRGZvNGZrbE0xV21zcXpyM3ZBTEZMVDNEY1RWREtQd1BfeFZLR0pERjIwUVhpZG5jaDBjTkZ6MUE?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-13 [埃安Ray7限时11.47万元起 后驱702km续航](https://news.google.com/rss/articles/CBMikAFBVV95cUxOd2VxcjlQQmJWWk5LVERkLTZBdWZGcnNXSk1nLVp5UUFTbkg1MEdkV2M5S3RkUkRHcFZjdVpVdEpteXlrRmg4cU50SDB4MWhuZkpsN1R4b2ZSdzRCbEk5aF9DYmNPdmQxbEhXbGs4WDRZbGx6Q1lhYjNScFdSMDVzdzM2VEY2c2htZnd1U1R3NXE?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>Horizon Robotics</b> (63)</summary>

- 📰 2026-11-15 [深蓝S05新款2027款智驾值得买吗？3个维度说清激光雷达+天枢领航+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9yYWF6X3h4RjY2dDU1RUo3c2pqM0wwaUZRSHZZWVlya21vZlhRTDJYUVlyckxWSTRmRE5uSFFtU0dUeVRuZmprRnZ0M1pIV001alZweWx3YktNNjlpb1Iw?oc=5) <sub>新浪网</sub>
- 📰 2026-11-15 [《极限竞速：地平线6》游戏2026年末-2027年路线图公布，含两款DLC及内容更新](https://news.google.com/rss/articles/CBMiTEFVX3lxTE5JLVFFU3BFVExxYnREcnBDTjVRR0hYeVhpb0RWVFNPUTJJQVV0dEJRb2xVVDl6MXZvSjQ4RlNZNUhtZS1hdUdaOXUwYjY?oc=5) <sub>凤凰网科技</sub>
- 📰 2026-11-14 [Nvidia Leadership Reshuffle: Why the Automotive Sector Isn’t Panicking – Key Insights & Industry Impact](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1kSEdoX0tub1h1eWVpZVNYdlNFSDNZTFp2Tk0xYW9SNTUtSmlnR05RRk51YXdGQjN1eG5FUzdCZVJWVU9JYXBzVnQ3anpxb0N6cDMw?oc=5) <sub>36Kr</sub>
- 📰 2026-11-14 [China’s Arcfox launches two new EVs with 99-second battery swaps](https://news.google.com/rss/articles/CBMingFBVV95cUxNOTVkVU1mYzRpN3pvSU80cF9fQkw1UU0xUnJpZ2JYMlB6QUhOQkJTYzd3OGdTbjhtcVNVbndEN1RyQlotRGFsOGJuMVNQRnBGSkw0ci1LaVdfczFqbkJLMzJyTkU3NXJnNENlNUx3UTA5R194T3Q1U0hhT0VqZXByMHg0QW1iYUotcDZxd1FfYUI5bldVRzBXRHBKejFfdw?oc=5) <sub>Interesting Engineering</sub>
- 📰 2026-11-14 [理想ONE 21款还值得买吗？3个维度说清二手行情与配置真相+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9OSkpfQmtIVVpjcUpuaWZMS2QteUFnaW41VGY3WklON2FDVkh3UTVoamRwVmxfc24zbW9ieWNYSWl2YWFIbmhJY3lEOWJwcmMyY2F1YVpLd2F6U2ptMU9F?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (21)</summary>

- 📰 2026-11-14 [DeepSeek无人创业](https://news.google.com/rss/articles/CBMiTEFVX3lxTE1QUnM4dm1XbE8tWmIwSE1hN1JMTjZKRklrM3FmbkdNbVd2WllWUWpjQVhYV0xwaHhqUHp4T2ZkMGpHMExqWjFNU1lPYXo?oc=5) <sub>凤凰网科技</sub>
- 📰 2026-11-13 [【视频】小米澎程N90和特斯拉Model Y L怎么选，同价位还有哪些推荐？](https://news.google.com/rss/articles/CBMiW0FVX3lxTFB6dElibXRFYWFsZU9vQnhjX3YwZjF2VVd6QjhLdXJIV3pmRGhzTmpuTFRER2xXV1Zjc2ZqNld2RVY1MkxrTENqczVRc2MwNHl1VFljSkt2TjRxZ0U?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-13 [Valued at over 500 billion yuan but barely producing founders: Why DeepSeek has become a "settling pool" for AI talent](https://news.google.com/rss/articles/CBMidkFVX3lxTE5BN29naDgxcE4xa2NUUi1qSlFKTHpBZlVjVVozN2FaWS1kVy1ENkxsV0dxVTlQS0ZJWHkxV3lfY09LN2xldl9XYk1mTFA1SjBUdTJfV05LYWllNFJZZ3RwV1VPSmNQZGk1a085UGFMOXloMHE0d2c?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-11 [【视频】特斯拉发函，媒体CEO：放马过来#特斯拉#埃安Ray7](https://news.google.com/rss/articles/CBMia0FVX3lxTE5xOHhzcEd1V1RKWmxPZ3BEYUN6NGRhOXB2cHFXSWxFNGEzdjFPbkotY0VMQlpGTGxyV0FCc3p3S1NkU1NjSjI3b01nN2FTcnl3blB4dC00UGlQNlk0Ukp4SEhIYUtSVXNhRlQ4?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-11 [【视频】26年特斯拉YL](https://news.google.com/rss/articles/CBMiW0FVX3lxTE15a0hBYUc1enJBUDFBTkRRNlQtdGs4OFU0NjR0WXNFYnhHX09YZGd0WTRkREJVZlVwSTBNaGVUY0ZUSmU5WEFWQlVnZ1o1dUpCNENiYVptdHZYa3M?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Mobileye</b> (12)</summary>

- 📰 2026-11-14 [May Mobility plans 10,000 ID. Buzz robotaxis on €9 million revenue](https://news.google.com/rss/articles/CBMihwFBVV95cUxQdkgzeUVTSS1wc1czVWhUTllrV1ZaVk1VLUUtUTVhTlFVSnJVSGFvcmtvRC1QZHNnWUxHY1B6c3gtUjZqdzFRSm9CSTNuZENtdFlRZGpoaDZGalJQb2xmZ1UtMGJyX1JObkdfaVF6SThudG9kajdDaW1xZVY4dzFraUF6NXd5RVk?oc=5) <sub>AutoNext.co</sub>
- 📰 2026-11-13 [Automobile manufacturing stocks Q3 recap: Benchmarking Tesla](https://news.google.com/rss/articles/CBMivAFBVV95cUxQemM0Qm9BZXFLb2o3YWdJWkFwb1FLcVdMb3NZNDE2bTB2U0hTb29PbnRiQXhFejA3ZklYUEdTR1lZaGpFT2tjOWJPT0luaXF2aXI2ekRhSlhPQnpQNWxQQUpLdTAyeWxvN2dBV2dNcEhiM0VDOWtwNzNtUHlSVVBmMVR3eDZKTWtXSWRvTUd6V1FhVzRqX0MyMDZjQm4xdjAwRmREZEl1X1V3b25CVk9MSUF6Q1draU9nZU1peQ?oc=5) <sub>TradingView</sub>
- 📰 2026-11-13 [Korean Optics Maker Optrontec Triples Profit as US Automakers Replace Chinese Camera Suppliers](https://news.google.com/rss/articles/CBMi3wFBVV95cUxPWHNlSUphR3lWUXJBNm93Mm1QdFZ1MVVSZU9jTlBxc0ZuR3JyU3pYQU9OUmk4VDh1NnhCMnV3dXdSenBkVldzS09Zb0NVeGJSc1V3aXhiU1E1aTNsd1RydXlIT2RDdDk5SWZUOC0zbTNlbUxxZVpMaUdIcm1lRUM4U1k0TVBhUmNtMXlCUDh2Vzd3dXE4aGxCRDZlaU5MZFNHNllfRDM3dXoyRWlTckRFREZfRjBpNjhLaW5YVkd3OWJuQWRLVmE2ZFpOck9zdXZrYnVXZk5pYks2WnFKNURZ?oc=5) <sub>Tech Times</sub>
- 📰 2026-11-12 [JPMorgan Downgrades Self-Driving Technology Supplier as Volkswagen Faces Delays](https://news.google.com/rss/articles/CBMi1gFBVV95cUxNRXhmZ1ZxandRVnNmaEhwZmljMjNVemVoUEIzVFZPQWlGQ0lxeTNES2JuczR4dnZiU3hpUWlydklMWXVLeW5tWVBFSVVlY2hfXzM5dm4yWEZ4UmJYcTdJU2o2MWZhS1VMWkhwb281SndVb1BkN25QTUV3TURlUmxVTzdYTUFDVFVVTkdKRk1wVlpzMmZ0QjZqWUw5ZDU4dnV0bXhzZEtJYll5SkFlZFBxWFU2aGFvYVZLWHQ1d3RfZDdrdVFzQkVUd09lUjlqYjVTWlNSZDhB?oc=5) <sub>TradingView</sub>
- 📰 2026-11-12 [Tesla FSD Gains Ground in Europe: Is EU-Wide Approval Near?](https://news.google.com/rss/articles/CBMisgFBVV95cUxPOHl0V1BnS18xZnYxOTlvTmZ3bXpGckVjMXZxYmh3TmpldVFkMlhRSmRYLWl3eDI5eWVfSm1kcXZSQ3ZmSUYteXdISFVlb2ZRNG5oOUNzR24waG00cEQ2SUNMTXdFbDR3X1c1Rko0UGw2TnY2NDQxc09QSDJsWDRfbTV0OUNJb2JQNUgwZTY0ajhhT3BZUTBmVUotSGtwSE1wQW9QTkZuS0VsMF9PNE1RcDV3?oc=5) <sub>TradingView</sub>

</details>

<details><summary><b>Aurora</b> (30)</summary>

- 📰 2026-11-15 [Archer Aviation And 2 Other Penny Stocks To Watch](https://news.google.com/rss/articles/CBMixAFBVV95cUxPMmkwbVE5akZOMWNlM1ZOMzhiRERnSDM5Y2hxc1dPYzdPN2xNdW11RnZXMXlfb09vQ0FpaUNwQnVlM1BYekRKMlpwU2h2OFRkU296MG4weU0xbENsejRhelMwR1AtclowWDhtZkd3WGdISDBjWWRCTTNUT2tWcXN1S05rR0lFLUlQVEpOSHJwc0VqcDVJZ3YzcWRncGZUTk5OU1UyUVhHVl92OFJ6MGxuWWRtTUthLVBEeldqcDVuM201VHVF0gHKAUFVX3lxTFBVM0k1cUlMdzFYUy04cDBhN1IwU1J4cWkxQzlOY2VyNUJjQWk5VHlrWVlBcVlrRnBkY1JXdjFCUm9Fa1VxLXVKSWpxdnJQV3U3OEtFdVhmSDhaUHMzR016a1FOMkpCQjN3bmZUTGVCTnVuaE9wX1dCbkJtb3FKSzE5TGNpbmMzbDNFQWFaRkpqSVRFdXhHaFNZa2F5OElxZzhBS3VwMXlCMW5DLWV3bmhhck1HdTVhZ1VLLWptcTZtQXhYa0l5aEVPN3c?oc=5) <sub>Simply Wall St</sub>
- 📰 2026-11-14 [Should Truck Production Delays Require Action From Aurora Innovation (AUR) Investors?](https://news.google.com/rss/articles/CBMi0AFBVV95cUxQM0Z3WEJQclFZaGZESEs2VUNRSXRLVnAzUW9Mdy1hSFQ0QTBXdWs2ZVd1SDdFQXBFZWhGM0IxamZKcmN6VGQwaGpORzFNdEZvUE16T1pDN3VGa3pmRmR4VHF6YV9yMFBVYnllUnlOdmxzWUR4bzhab1A2dlVNSFllS0NmQXBJQ3BRcDN3V0wtQy01R1R6ZmQ2SHpkTFFVNTBmZEdTTGlJVmV1YWtHX1F4c0lJWlljVXZkbWlKTlZjMDhLQlgxWGtrN1pJc0RJYVhO0gHWAUFVX3lxTE1VS1NpejQzUVhxSnEwMjZ1NE53QUlwMHZ2dkxRNFhpSlE2RHJpeEZ1ckZFZlZQMmxGbXYyRHNXaXNWLWNrODc5eW1oTURNc3ZSUVZOY0FpaEh0UEZUcjJMZjJJWjFLWDNxX1VEVzE2a2NGTEtwZDZjOHctVE53Q094YlY3c2NybEN4UTV6MEZSTjlvRlhWc2M1VjdlaUxoM2ZqTW5QRkVTVWR0a2hnV1ctejNVaFdiaXNzakV6ZGRIblEzVVp4Y0x6dF9xM0RiV2lCcDFFR1E?oc=5) <sub>Simply Wall St</sub>
- 📰 2026-11-14 [Aurora: 3 Key Takeaways for Long-Term Investors](https://news.google.com/rss/articles/CBMilwFBVV95cUxNMVFqdzVjR2I5Ulp3TldKbTdXUWprU1BmWTAwMXJOTVl2cWQwZGdNTF9qRlIwVFp0OG9Qdk9QcEY3VG81cG9iV3dFTWVRRFltM3I4ODRDQ2pNUUlhc09zS2Q5ZU85RVNoUHBOb0Y5R1FRZXJ0V1I2Sk9kVUpjdlU0bFpCM0N5TUY1NUxONDZMN2pBeWs2ZVBz?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-11-14 [3 Penny Stocks To Watch With Up To 72% Revenue Growth](https://news.google.com/rss/articles/CBMizgFBVV95cUxONWJzcExzODFFZG1rUElNUW9KYllJRkxMT2ZmaVNKNjdyb1RtMzZVUG5SMHFEYXZTUnpvd2JhSmVrckJ6Z3hCd1FUNEI1T20zQmZRQ1dqaUcxS3p3NTlZTm5MV1dWSG5wZUdpdDFKem5XdGVuaEh1MXhycUZKWWhSQm5xWl9GR1BoTlZ3TjRFeWJiSlZ6QVZMTC01S0FpRDhuMV9LRHhORFFoeXhCeUJWWjAzNm45RUxlX1JQSXpqX2ZQQzVkZ3N2QkNiRTNQd9IBzgFBVV95cUxONWJzcExzODFFZG1rUElNUW9KYllJRkxMT2ZmaVNKNjdyb1RtMzZVUG5SMHFEYXZTUnpvd2JhSmVrckJ6Z3hCd1FUNEI1T20zQmZRQ1dqaUcxS3p3NTlZTm5MV1dWSG5wZUdpdDFKem5XdGVuaEh1MXhycUZKWWhSQm5xWl9GR1BoTlZ3TjRFeWJiSlZ6QVZMTC01S0FpRDhuMV9LRHhORFFoeXhCeUJWWjAzNm45RUxlX1JQSXpqX2ZQQzVkZ3N2QkNiRTNQdw?oc=5) <sub>Simply Wall St</sub>
- 📰 2026-11-13 [AUR Investigation Ongoing: BFA Law Reminds Aurora Investors to Contact the Firm about its Securities Fraud Investigation to Recover Losses](https://news.google.com/rss/articles/CBMiqwJBVV95cUxPRGpBZHRRMWt6QVZjTFNRc0xJQTN5N0RUVUp0VTJBS21vel9MTTgzTjBrMjFjV1EtTzBmMjlUR05TZHo3YWE0V3pnelhWWmQ1YjJnZy1CMnphNnpKSWZGaFJhTC03bFBGbWN3VzgzbnVRTHhQNlJoUUdyMEtMbzNVRHFKX3NIekZVbHcyaHpaXzNIQi1ZNnNlWC1ubGJVZDhvN1pIcWFXZnhrT191ODFTR1JORXNQSjFWSW9MV0ZRWEhUWkQ0U1pyVkNIOGljSmgwYlFXTzZhdnF2QlBzdHJqejhHY200aElLbjVSWjhqcjF3S1haSFZXaHFRRzlBU1hTWURaUVdyNVFWNG1rQjl2SG01S05GQmJLQVQzcTZqUWVqczVIaE5YdVc0RQ?oc=5) <sub>mykxlg.com</sub>

</details>

<details><summary><b>Zoox</b> (51)</summary>

- 📰 2026-11-14 [Zoox Launches Robotaxis in Atlanta](https://news.google.com/rss/articles/CBMifEFVX3lxTFBuWnJ1QmFxN2RYUzR0SnVoYzFGdlFCTTNSOEctbFRLTENZOTN3UHlKZGlLak1vTzdiN0ZPS0puY3A5LTF3OXFNMHR2UGtMeXFVbC1Nc3RtXzhNWFJpdzkzU3E1WlIwbWRTdmtxQTJDZzZkdUpMNGhnazloRWY?oc=5) <sub>CleanTechnica</sub>
- 📰 2026-11-14 [Atlanta already has Waymo and May Mobility. Now Atlantans could see a different kind of robotaxi roaming the streets. #atlantanewsfirst #crimewatchatlanta](https://news.google.com/rss/articles/CBMiUkFVX3lxTFBHU2RzM2pSNUhsTTg4RnlnUWFndF9HajVfZnhqMGVFaWdTM2NQcDBPRVBrSUtsbnJ6YnB4OUt3T2wxOGFUYU1xVmEyRk5YZnliV0E?oc=5) <sub>Instagram</sub>
- 📰 2026-11-14 [Zoox Expands Robotaxi Service in Las Vegas](https://news.google.com/rss/articles/CBMihwFBVV95cUxQTFQtODdsVXI1akFuaVRmWWl5V19NMVJ1eERkdjB2ck15cklwOXoyY2ZQa283V3REVUZuTEJkYWN1ZFNZTy1IV3VFZDFtVEpHWU5JWEhUMHRIdVlodkk1VXN4cnNEV0tjbWIwaS1uVTA0aGQ3T3lULW12aTB5MTkxZm1FanFpM2s?oc=5) <sub>CleanTechnica</sub>
- 📰 2026-11-14 [Zoox Robotaxi Launches in Atlanta, Rides Limited for Now](https://news.google.com/rss/articles/CBMipwFBVV95cUxOcVRsSmZzRzlHVU9EenU2aXBLR0pvNDNPTExZOW5yN19iOGZSNUJvbXRtbVNJcy1LVkRFcE1MN2Q3R05tTWczcXVlYWRmUTBVMHRlc1lxbnNDTzJTZW5fc0dtSUpnZGV0LWFIbjlraGJWdU0wUjNoVHcyU0RHR2dXMFhUMXBzSjhxekVITVlHZzVmRkpzN2czOXhSX1k1N052Vy0ycHhXdw?oc=5) <sub>Hoodline</sub>
- 📰 2026-11-13 [Zoox could soon charge for robotaxi rides in Las Vegas](https://news.google.com/rss/articles/CBMi1wFBVV95cUxQR3VIT0Q2S1VFX0JYZlpFSUU5Rm5JTzJDcjVKQ0tPQzZuaTZvRFBvOExqZnRXVWtKR0JmVmhuQ3B2N1B2RzJaZVR4b2JGY3JIc1gzdXluRVktdks0RlE5ZExyaldCeENZTFh0YjNYYjZMTUdYRWE2aWM5djdZMjJfaVR1b3BBS0ticXNSQm9BNnd0dmxtTkhCU3VTNi1IMzhMSUFIWnFJQ2dNbTFRa1dncDZLakxKM01YeTMycHBnem9YMmN5TUs1ZFZiMkJsNllQNkl0YUgyUQ?oc=5) <sub>KSNV</sub>

</details>

<details><summary><b>Motional</b> (16)</summary>

- 📰 2026-11-14 [Samsara's David Gal: Physical AI Starts With the Forklift You Already Own](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1aSWJmMnZVNkpEUFZYeV8tREdvaEp2VVRpZXRZYURLbzNDRkR2Y3N3Uy1YSi1UZzV0Z0U4VWZLalRXZzhQaGVGRmVGekc2TktFWnlScFpJRHJFdjQ?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-13 ["Cars That Keep Going Even When Sensors Fail"... Hyundai Motor Boosts Autonomous Driving Reliability](https://news.google.com/rss/articles/CBMiZEFVX3lxTE9BX3gtSThrelhocW04V2VGTXc5NnB0X1F6VFBlenZLX2Mzc01UY3o1c2E2eE8tQzdqbktEOVIyTzBtdnFOeXF5NlEzS3lIXzNLMEVzQ1V4dTQ1M3ZXY1FQR21pank?oc=5) <sub>아시아경제</sub>
- 📰 2026-11-13 [Hyundai Motor: "Safety Over Speed"... Ensuring Cars Keep Moving Even If Sensors Fail](https://news.google.com/rss/articles/CBMidEFVX3lxTE5Vc1NOV0ZacmFwUjhSNVhhSTc3VFQ4QV9DanB6aGNSWFhONW1CcEpyZ1NaNm9heUk2ZGhLRm9XaE5NcXVJZUtjUmJIeDQ2TUFEczBVem0tbGYtRkp6eVlhTjVHdmtVUno3NmRpZldWalhZbUYz?oc=5) <sub>아시아경제</sub>
- 📰 2026-11-13 [Huang’s Exit Puts Hyundai Motor Group’s Dual-Track Autonomous Driving Strategy to the Test](https://news.google.com/rss/articles/CBMidEFVX3lxTFBZTG1rU1ozSDFnd1diLWNmZVBXcFRjZ0J1UGpqZ1BCck83SFhJOUhBcDE3ZlZKV0tod29JZzh4dVctU0pYR2h5bWxSTVg3ci1XTUFMeVh6WmQ3SkpncVBadDZMX2p4VWlzSG1MQVh5NFZhWGVN?oc=5) <sub>Businesskorea</sub>
- 📰 2026-11-11 [Korean firms shift CES focus to industrial AI](https://news.google.com/rss/articles/CBMiqgFBVV95cUxQQVpGVm5oN2E0dXpVQ2tfaXVaZXlZanNWcllzRTJCc19OS0F3V2Z1eWEteEpub2dQWWJleEtYMTVyVkRGaVpmWmwwQi12V0JhdjlvRENjU3JWMlpLTkJkOHhMYl9JeDh0RU14Mm5fZmx0X1Z4NlJTYmtKNkc2ck4wT3pQTUZxYjFmQ2M5a1ZoTC1WSmZOOGxMOGJFakVoTm4tcTNaekZZdVFWZ9IBqgFBVV95cUxQQVpGVm5oN2E0dXpVQ2tfaXVaZXlZanNWcllzRTJCc19OS0F3V2Z1eWEteEpub2dQWWJleEtYMTVyVkRGaVpmWmwwQi12V0JhdjlvRENjU3JWMlpLTkJkOHhMYl9JeDh0RU14Mm5fZmx0X1Z4NlJTYmtKNkc2ck4wT3pQTUZxYjFmQ2M5a1ZoTC1WSmZOOGxMOGJFakVoTm4tcTNaekZZdVFWZw?oc=5) <sub>The Korea Times</sub>

</details>

<details><summary><b>comma.ai</b> (2)</summary>

- 📰 2026-11-12 [Goodbye, BlueCruise! We Install a comma four in Our F-150 Lightning](https://news.google.com/rss/articles/CBMirwFBVV95cUxPY1o5ekZ4WnpraUxVMHV6OVdyMEtEbjQxQXY5STdJdXlHNlN6eUFZNzFwSnA5cFhHd3pNdTZNNy03dXBOZ1ZoX3RFX2E5V2JNTE9aVlhJaG90bW5YWEdzX2NGXzd3VFZ6NG5JVkFrM3daTmY4UDBTN1I4NWU3eGJqUm9tY1VaRWxoZkp3WDJLNnVLQjN5WG9NMzlxLWI0aVU2TFhLUEZwUE5YUDdUcWFJ?oc=5) <sub>Transport Evolved</sub>
- 📰 2026-11-06 [Canadian YouTuber Linus Tech Tips Tests Tesla FSD](https://news.google.com/rss/articles/CBMiggFBVV95cUxNZVZaT1Q4X0NlakJzTnFkTGdqTmFPM3pDbFZPUnBYVVNrVzFxMlpZQ3VaTEJFUmJrNVpjMmZ5RVphUDE4WURNT0x4NkhnN01LdTdzSEVnS2NUNkROams2cnNzNkpnalhWcDVuckhETUtxaDZrSHNXTXhKYUlpN2dPTlZn?oc=5) <sub>Drive Tesla Canada</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
