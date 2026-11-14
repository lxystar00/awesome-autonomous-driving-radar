# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-11-14 · 1,279 papers tracked · 47 curated.

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

<details><summary><b>Waymo</b> (141)</summary>

- 📝 2026-11-05 [How the Waymo Driver Manages Severe Winter Weather](https://waymo.com/blog/2026/11/winter-weather-preparedness) <sub>official blog</sub>
- 📝 2026-11-05 [Rethinking What Freedom of Movement Feels Like for Women](https://waymo.com/blog/2026/11/because-women) <sub>official blog</sub>
- 📰 2026-11-14 [Elon Musk Ally Jason Calacanis Bets Another $1M On Uber — Says Waymo Team-Up Could Steal Tesla’s Driverless Crown](https://news.google.com/rss/articles/CBMi3gFBVV95cUxQSTc0N2VLYVlDOHgwVEV4RUpjZjByeG83S25JdHoxZ1ZkaEx0aVZXUXdCeXBqZ0lZRUpaajl3Wm1hUXhQeWdoWXlSRnlreFZpRW40aXpnemEzU2FnTU96NWlEbzNOc3oxNGlyNFR5OG1tellaMG9ac2NNNl9GV25USlNlVnk3b1E4ZnNLQkw3cWc0OWZpdVZxQTdYbzg3cHkycjFSZTJLTDE3Q2F3VXhHNVRLc1ZCbHpkbUJpaXVNcUh1bE5VYmx3dDRZWHNkWTZmcXh2ODlrNnRXeXdrLXc?oc=5) <sub>Stocktwits</sub>
- 📰 2026-11-14 [Waymo Co-CEO Says Company Considers Footage Requests Through Formal Legal Process](https://news.google.com/rss/articles/CBMiW0FVX3lxTE82aG5XOE1aYnY2Wm9xckI0bnVFR3l4Wkt0bHRKczFWa0JIeUlTSkNUeWpfNGZYYV9zZ2x2ODVQaWhoQm1iS1NtZWl6VE5HcTZLUnJ3Q3R0eWlCUzA?oc=5) <sub>www.tokenpost.com</sub>
- 📰 2026-11-13 [Most reported Waymo school bus violations came after a software fix, triggering a new probe](https://news.google.com/rss/articles/CBMiigFBVV95cUxPbEJ2blFBN0RUT1dBNzdvemJfOFNraHZYZldtUDRlc1BZeVA0R0JEVm5UYWRSVGFGRTNUSGYwQnVUR3gwZlRFNWpvSEktVGpjRFVTcU5iWlJlR0Q5N1Q2QUw3dmFPQnhKSzdtX3JwX2x6NW9obXRyaUxiSXZoYXpWQVp1TGpLV09ZVUE?oc=5) <sub>The Cool Down</sub>

</details>

<details><summary><b>Tesla</b> (193)</summary>

- 📰 2026-11-14 [Tesla Cybercab orders open at $29,990 + $299/mo, only in Robotaxi zones](https://news.google.com/rss/articles/CBMilwFBVV95cUxQVFA3STVYaFRsY056bXBKdkJmS1Q1LVFWZl80RUluY0syZWZHTlFWOUV3dl85V1k5R2FRSFdfcXdSc09ZMkNjOWZCNjl5eEdhMHo4T3hHeVF1anZCMlBzTDNaenExQXFuN1hIcEpyWnM0RzBpV1c5OUhxUHJZOVFoY3NqQjVlQ05qT0YyM1lTRWVFTTAxYl9v?oc=5) <sub>Electrek</sub>
- 📰 2026-11-14 [Tesla Cybercab Orders Open: $299/Month Autonomy Plan and Delivery City Pick](https://news.google.com/rss/articles/CBMirAFBVV95cUxOYkNLcDRoT3k5UHB5NTE4Y1k1cTFlYXE2aFIzZ05XMzYzaUpPVG1Od1U2SmRoWGVOanpIeUN4eXUwZlI2MzFkdWpMM05vRUtvRUluTXBXc3MzY1JseThWSVQwY0F2UVV1WVAyMkR2dmJnWndSb3JzY19iVUlQSVZwczJ3VmRITDRpYU9vckNvWXRkOF81Vk9RaHdxaVVRa0w2d1JIYjlNOUFGLU5C?oc=5) <sub>BASENOR - Tesla Accessories</sub>
- 📰 2026-11-14 [Tesla Says It’s Starting to Sell Cybercabs for Personal Use](https://news.google.com/rss/articles/CBMirwFBVV95cUxQVW9TQXZVWjF2c2FxVllYb2MwdjhVZ1ExOTNTRGpJTThYNWt6QVM4VWE0MWRwQ0VxU2ctdnB3UGtjTlY2d1NzT3JCQWZUUXlrbXhldG9PVzhyVERZNmJuVjhLbnp6MlpxRVJwbFpWTE15aW5NUmcxY3lpXzY1azdSSHFqODVDSEt5R0hyNTR5aTJXcDFvQW9ZbGJlNEd1VDZGN1hRMGdTcHlyOEdSY0tr?oc=5) <sub>Bloomberg.com</sub>
- 📰 2026-11-14 [Tesla Opens Cybercab Purchases to Select Private Buyers](https://news.google.com/rss/articles/CBMingFBVV95cUxOV3JrNnF2Rl83ei1YRlZxbzV3VGlxaENVUHZKYVU1b2FCRFRYRGUyWllsbDM2N0dVRjd1LUFxcFpaWm9XcmFnS2lzdWhlX2ZZbDIyVkZIbHJqclVJSXNPT1NsYmZFaXlMdnRUek9jaUNTX3ZabGc4Zk5GZkpVeXdyaWFmM3ZvcGwwVmtfdlFmeTVtZVZOQ3IwUHdydGFwUQ?oc=5) <sub>The Defiant</sub>
- 📰 2026-11-14 [Tesla invites select customers to buy a Cybercab for $29,990](https://news.google.com/rss/articles/CBMijwFBVV95cUxQRlJld3V6dV9jeEg2YlJvRGFRcGpDZC1ZeWFWQXM3N0htRFItWExlTjdJdHlVWkJqMGpTMmNlWWpSVWNaTWJ6VWRMeHFkRUwwRjhhTmhNNmVVdEZOYUZkVUZZTUpuOVFxSFNGWk1mNzczNFA1NzZOclhSY1IwSkNaWjg3ZXVRckZUeklVOTRHRQ?oc=5) <sub>Startup Fortune</sub>

</details>

<details><summary><b>NVIDIA</b> (123)</summary>

- 💻 2026-11-02 [NVIDIA/nvperf-core — Core NVIDIA Nsight Perf SDK APIs and libraries for collecting and analyzing GPU performance data directly from application code.](https://github.com/NVIDIA/nvperf-core) <sub>GitHub</sub>
- 📰 2026-11-13 [Trading Day: Weathering the Nvidia storm](https://news.google.com/rss/articles/CBMihgFBVV95cUxOdlRiUzVpMWdlaWkwR1N1MU80UTc0Sll4UTZGcnFOXzVhbG1WUG5qZi10dXZJOVdsUWZJVWNKQVFLUGVZSi11TnZhTTJpY05aRl9ROWVXQWVfZDBvQ0pGNURBeUxvLTNicWt1QzFEN2tQTGFUcWE5dXg3eDYwdHNHWklzRzJlQQ?oc=5) <sub>93.3 The Drive</sub>
- 📰 2026-11-13 [Fallout from the Nvidia scandal may dampen the exuberance around the AI boom](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQeEZnNG9Ec3V4bVhSRHpZcVpsMmZyVzhQZE1SODNpYXgtd1BGcklSSEtTMDFwd1pBX0ttU21oaFJYRDJTaGQ2UkFCZldNdm5fcXRjQXhMNXlJRmZMVHlUY2ZLVTZyZUV6bFJGVUc4Rlc5QnRuWFNsVVk3VUJFTk56dVg3dWU5dEc0Y01LcHRRSE9aa0dvZldxd2VWbThNUURmLUptT3dPRkM5MlU?oc=5) <sub>Audacy</sub>
- 📰 2026-11-13 [Evening Wrap: ASX 200 slides as NVIDIA woes, bond yield spike and falling commodities drive broad sell-off](https://news.google.com/rss/articles/CBMiqwFBVV95cUxPc1pzOXV5Vmc0dmdOU3ZQV3ZfSzNUd18tY1hfaTdlSjZqOGgyci05LW9VTzh5QklGNktzay1BNnIzYmZxeHZUcWNJTXhDNUtvZ2lmY2lqZUJtM1NMYWxwRlpYTlZmRG0tNXp6WHAtTnlObm9lVlFFRlhDNTRBaVphWHFpaElkaVVoWDBZd3dPaGtodDc2eF9rSXFNOHVQLTBNV0RrNkVXM0FEYkU?oc=5) <sub>Market Index</sub>
- 📰 2026-11-13 [Trader ‘made $196m’ shorting Nvidia before Jensen Huang scandal](https://news.google.com/rss/articles/CBMiygFBVV95cUxPYVZ1N0w4YUt4TlkwME5YUGlmMWNvU3c3Ty1QY0hxUVA5VU5UeXBGYzVaQUNJWnpha05nRTVwZGQ2d3JpR1BDdUFoczdRcU03Rk82VS1IWkxVN2R0Z1VoN1ItenVBemdTV2dHTjZ4eXd6Vmt5bU1meF9VTXJZYzNQNlZoeUZBcHNmQ255Z2x4OVdaZ0RMX0stZTYtNTg3ZVNlRW93SWpkSzBYSjdQdUdsZUVzTlBuYk1Ja3VMVi1ZU1ZqbUVld2hWM0Jn?oc=5) <sub>The Times</sub>

</details>

<details><summary><b>Wayve</b> (38)</summary>

- 📰 2026-11-13 [The Verdict Is In And The Brits Lead The World In Detesting Self Driving Cars](https://news.google.com/rss/articles/CBMibkFVX3lxTFBJZWtXTkdEQVRoMVVIZUhjbWZkQXJla04zZ2dteGxMQlp6LW9CSGpIbjNJSFhXdVN4VkxIVnZvdGNMeTNoTlNrRUdjeVcyU2RXUmJOZThLOUtNQmpfNmNZeHJRYzJ3LTg0bXJiX1NR?oc=5) <sub>AutoSpies.com</sub>
- 📰 2026-11-13 [UBER - I Think the Market Has Uber Completely Backwards](https://news.google.com/rss/articles/CBMi3wFBVV95cUxOV3ZEb3N6WjFIOTJ0b0llOFFrQ05ONFNtSUM5clg3ZTlpVlZjWnhIeDBwTzloWXZzamI2cXViQlg1Y09TQW9MZDhxakUyY04wNU1XVmVHaFp4eVpYNnhpYzFtS2lIOHpDaHFHbS1FaVdwd1FqQlFzLWd0czBOcjlrUHZEOEJlaHdBVVFXU0FVdG55akdLbVlhOGwyS3NVY2RDd2V2V1EwNE1pbEhNSUhOS1E3ZWVQUG1OSjIxSDU5VlZtbEZlYWpBZE41akh0RkxiZlYzc25WSHhOLWdRODlZ?oc=5) <sub>Simply Wall St</sub>
- 📰 2026-11-12 [Brits lead the world in hating self-driving cars, and there's one big reason why](https://news.google.com/rss/articles/CBMiiwFBVV95cUxObEZNNndscVpKcWVER1JFMUVyTmdvOFNtdG9jMnRscHFjLXFMLUtVdjl4cGtkZkFUMnZmV0duUkpCSkY3a2RJcnB5TFNqRGlzbGJaQTlVWnZrMlhkalZRTWhYSVlLc2NnbjBfblVrNXI1RHMxS0lYa0d3M054NDFMeENYZzRLRFhmcnB3?oc=5) <sub>Auto Express</sub>
- 📰 2026-11-12 [Agile Robots Raises 500 Million Dollars at 8.5 Billion Valuation](https://news.google.com/rss/articles/CBMiZkFVX3lxTFB0Mi1XZFA0Rm5Bek12cXNKNHdNZ0lBNTF2bHE1TzZ2b1ctQzVURXFVVnhlTFdGejNmb0NvTFkxbXBzcENjc29oX1k1VTRib0NzS0pRTkpFajl1UmRBQTJKeVREdWpGZw?oc=5) <sub>SuaraGarut.ID</sub>
- 📰 2026-11-12 [AI Startup Wayve is Charting a New Road](https://news.google.com/rss/articles/CBMidEFVX3lxTE0ya29aQXBDRTd1VWFUMHlSdVNwWmRyQW0zZkExNHdvMVNHUHBkcmVaNm5fNWMwU1VQbDU3YXNkQ3lOYzVVb3VZcmpYVjRUWTNBZ2hTeHFTX0pmUC1sZHUyVURLMmZ2dFJQMXh6U2ZnMTNNdFN1?oc=5) <sub>J.P. Morgan</sub>

</details>

<details><summary><b>Momenta</b> (74)</summary>

- 📰 2026-11-14 [东风日产NX7预售12.99万起 三版本搭载宁德电池与Momenta智驾](https://news.google.com/rss/articles/CBMic0FVX3lxTE5hbzdXLTZqaXVxYWxQNkw1alcwZDJHc3Q3Q3RfLU9Sc09xRUlxcUItR3VEVzI5TDlvbEd2RDVBdXdlY2tYZ09mS3RvZlZmemFwanpReFhQSTVUQ1BGUXRoQ0hMNzdZaXRLSXg0Mnl3aW53Q0E?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-13 [【视频】ID.ERA 9X 2026款 Max四驱版](https://news.google.com/rss/articles/CBMia0FVX3lxTE1JUE9PRmdMQjQ2NUxzeFVtUEJWUzg2MU54UGFwZ1YxbHF3bWtVQWRfLTl1aEphLXFzRzZrWE5CMmxuRHJ0dVRMSGxsSlNXenYxaVc3VVB6TExMbk1HRDJKejVWQVh0WlYtSGhR?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-13 [把智驾和电驱做成透明模型，这次发布会看得比参数表更直观\|Momenta\|东风日产\|AI 云擎电驱\|NX7_新浪新闻](https://news.google.com/rss/articles/CBMiY0FVX3lxTE1CVlppZ1NIX1dXNGZNZFR4bG1ldjRmTEEyUlR4RnlvTm5BV1BYTjlOc3h1MmlXcmhhMmFwUFk0VWNveHpvWjk0QVlBVU1QdENOdGdDclRxMm5nYTBzZV8zb0ZtVQ?oc=5) <sub>新浪网</sub>
- 📰 2026-11-13 [20 万内插混首选？看 GTR 同框，NX7 把舒适和智驾揉进车里\|Momenta\|东风日产\|战神 GTR_新浪新闻](https://news.google.com/rss/articles/CBMiY0FVX3lxTE50Q04yYkVURHZXdTlZRUoxV3BQX244WVpwT3NEd3Mtejg2cFpwdjF5V25qaUdiU3FDNVBpX29IMmNVU1lOdVI2YTlNTEd0bllnWFphLTVYWmMtMmFRTGQxYVBRMA?oc=5) <sub>新浪网</sub>
- 📰 2026-11-13 [凯迪拉克XT5插混版智驾值得买吗？3个维度说清+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE14Q3pIU1pNWVlObVhxS1lDUVMtclh3S3BNRFNfTGNZRjltWjhFSHROUkR4bzhFWTdaT1JjRWVTaUp2UDVoSlZHYW43ajhnU01rMjF0djlLcUZISVpoNGlNNUQ5UHZnYklCM2N4d0NpcWRGdw?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>XPeng</b> (136)</summary>

- 📰 2026-11-14 [智能座舱与智驾横评：小鹏G9L、理想L6、问界M7、蔚来ES6值得看](https://news.google.com/rss/articles/CBMickFVX3lxTE1fZ1hyZjVid0dSVGQ3MVJ1VzRieUdGcWxvYVVjOUdZeHZFdFIzZEFMSFhUZkktN01BVWgtckoyV3M4Q1Z6Z0V2SEVjbmhaQlJYM0ZSV3hRV0VvalBmVUUtS2JvbEdrUEw2aTFrdzNENm43QQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-14 [小鹏G9L对比理想L6、问界M7、蔚来ES6：智能大五座SUV推荐与座舱智驾横评](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBYc1FWVmFtLWcwNUEwUnFqaDVTOXBIRUp2UGZBelhMRDNzUUFfMU5qT0p4bkJZYncya25jVWFIQ0t3OTRZT3F2MVR0cTVQTUtDLXVNTGJxNUVrazBBMS1B?oc=5) <sub>新浪网</sub>
- 📰 2026-11-14 [大五座新能源SUV怎么选：小鹏G9L与理想L6、乐道L80、问界M6同框对比](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9fVkRqOWJDVThoOGxDTXZiaDhDN1VYZnQzYzlNRXBqbjR5QW9DTXhMemEzWDdGQk9ZMzJKT25rS29TUTgzZzJIUlRKOEdicERoTWptaTVsX3o2dncwelNN?oc=5) <sub>新浪网</sub>
- 📰 2026-11-14 [25万级大五座SUV推荐：小鹏G9L入榜，与理想L6、乐道L80、蔚来ES6怎么选](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBucGFRWm16ZmFaeUl6RThDdFY4TXoyTjh2XzB1cW43R0lNa1NWN1ZNU2VLX25tWXpkVzBCX0VnN3pJd0E2Y3JoT2s3eUpGR3ZtQ0E4a3Q5NHM4cm5WMElJ?oc=5) <sub>新浪网</sub>
- 📰 2026-11-14 [最近这波新能源新车怎么挑：小鹏G9L、理想L6与智界R7横评](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9Eb09fWFFtS215VC1ncmNaZWxKRWhYajQzMzdaY1lVdTNSRGZrN0N5TFVMRmdOT1FKckN2bjFUQS00eGNLaVd4TzVhQmNLY1ZDUi1yLUgxTmtJVTI2R19Z?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>Li Auto</b> (140)</summary>

- 📰 2026-11-14 [跨省自驾、露营、三代同堂，四款大六座SUV横评，奕境X9用三排平权和增程1500km作答](https://news.google.com/rss/articles/CBMickFVX3lxTFBfMXdBRTNrZ1oycmxtdzdNUU1oYVNiT2hfV2xBXzFKRkhlb3FfNGdDQzB2OEQ3cDc0UGxWNUpsVno1ci1lMkV6bVZLTFotYkVRVXlMa01oM0JxVUtjRWFfUm5zX3I1UUlfV0N3cE9zU1UxZw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-14 [理想MEGA高速续航实测打几折？3个维度说清值不值50.98万+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE5sMmtab2ZLQUhDVmlCR1ZjMkdVeHRaamhBckNDemQ0bWhFdGtaZEpUTWFWNTdYcV84R3NsUlJMSUFMcy1mNEg5bWtldFF6VjlJMU9mY2N1a2JSRnJ3ZzZpc2RhOGdZMzRyZXY1clU0LXI2UQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-13 [27.98万起标配ADS 5四激光大六座，奕境X9与问界M8、小鹏GX、理想L9四车实测谁更合家用？+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE1waFpTbE4xQ3J5bml2UTdsZjdtazA0SlRzQnF6MXhRUTViZW1QZ1pZU3N1bVdlcm80LURrX282S0FIcmhpbFAzaWZiTVNleFBza3ZQcm9heE10N2hxQzBTblIyeUlnSWhaYkhPbDRhU3F4UQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-13 [Changan seeks to sell 10% stake in Avatr at implied valuation of $4.7 billion](https://news.google.com/rss/articles/CBMidEFVX3lxTE1uanlOMHRrZkNjeXNqSE9OcmJ4d3RUeTFCREpqU3NXa2RRWDJoV2RtUVhWOUFySFY2VkplRzYzeDRqSzNGcFlvZ1NHV2hUelh3dTVqNTF2cXdlWEtqUzZBdkQ4T2MtWlB0VW1BTjBkWlV5MVBR?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-13 [Li Auto's 6-seat electric flagship i9 tops 10,000 deliveries less than 2 months after launch](https://news.google.com/rss/articles/CBMic0FVX3lxTFBUX1l4YmRoaWFFendhTU5UdFV3ODZ3czFBS2ZPT1B5RG12aXZSb2tJMEhPc3RXeXNicjJRb0o1RV82Q0xkUHkzT1daa1hCcW5WWmhidnVwMEdMVkpoRjJ1VWp5bUNtelZ1alR3akhKN1VqYkk?oc=5) <sub>CnEVPost</sub>

</details>

<details><summary><b>NIO</b> (104)</summary>

- 📰 2026-11-14 [【视频】蔚来ES6 2025款 75kWh](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5UOXczZV9KNnlTcDZ2N1dNS1Y2OXliMDBEbS1SQ05ZZlZDbUEzV2FOUWY0Mks2RXplQ01aSFU1M3lrM1A0ZjlKUnBLZkZpcndBZG5YZkxjZXhYMkU?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-14 [蔚来第三代ES6前脸谍照曝光：车长超5米明年4月亮相](https://news.google.com/rss/articles/CBMia0FVX3lxTE5fMkZtSEpGYW0zS2kwTmUyOVBDWWpCUmZaTVk2WEE4c2VGdmxqT2dxZDNLT2RsRG83Y09TVzNXY0Fvb3A0YmtiVjdJbkI2UE0yVHFtYjVmMnJTMkFUaXlNUVQ0TVNZUGFCRFVv?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-13 [Changan seeks to sell 10% stake in Avatr at implied valuation of $4.7 billion](https://news.google.com/rss/articles/CBMidEFVX3lxTE1uanlOMHRrZkNjeXNqSE9OcmJ4d3RUeTFCREpqU3NXa2RRWDJoV2RtUVhWOUFySFY2VkplRzYzeDRqSzNGcFlvZ1NHV2hUelh3dTVqNTF2cXdlWEtqUzZBdkQ4T2MtWlB0VW1BTjBkWlV5MVBR?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-13 [BYD opens pre-sales for third-gen Tang, expanding 5-seat electric SUV lineup](https://news.google.com/rss/articles/CBMic0FVX3lxTE5paGlsXzBRclozQXoyTkVEbkNOWVJDblYxQTBBdlZkc0xfRFFrZTY0aUs3cW0zLXJ6aVR1ZlRTX0tSMko5dWhiT0wydkk2S3hNSFRKZk5hT3NvaVpVVnFUR3FxTDNqeXJuc2RMTDUwZl9SVWM?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-13 [GAC-Huawei brand Aistaland adds EREV variant to GT7 amid slow sales ramp-up](https://news.google.com/rss/articles/CBMickFVX3lxTE5DQVZVVGRGZzN2eE9tNFlPSE9EaW1sMHJuS3JkekdJSXJhZm5VbDRaVWdBb0NUanQ3eTNwV1R0ak1aZjNldk5SeDNGb2JRVDhtNThza19FSFpJR2dqN1lHUVRYNC1fbWtIY05MZWtUYnBSdw?oc=5) <sub>CnEVPost</sub>

</details>

<details><summary><b>Huawei</b> (215)</summary>

- 📰 2026-11-14 [Nvidia Leadership Reshuffle: Why the Automotive Sector Isn’t Panicking – Key Insights & Industry Impact](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1kSEdoX0tub1h1eWVpZVNYdlNFSDNZTFp2Tk0xYW9SNTUtSmlnR05RRk51YXdGQjN1eG5FUzdCZVJWVU9JYXBzVnQ3anpxb0N6cDMw?oc=5) <sub>36Kr</sub>
- 📰 2026-11-14 [三款乾崑智驾SUV横评：20万到35万，家庭出行如何一步到位](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBEcllrNHU2WTRxelp2OUxJUm94bkd6OTVuTy1aQm1FUG5SNDRyVjRUUER5YV82aUVfNTg5cl8weVlCT1NXeV9VcENtS2lfdHl4bWlvbVBBUVoxMDZlYWdn?oc=5) <sub>新浪网</sub>
- 📰 2026-11-14 [【视频】续航超500km+华为乾崑智驾ADS SE，星海V6把家庭需求研究透了！](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9PZlRMekhGWDIyYWZqbzJnZHZUY3hYbEpoajEzSnBHNnExT2ExcEJkQTFTeWhHdHhkZWdzalhDR3lJUHNNbWxaZ2NRZ25feWNoUjBiRGcyX2hFZFk?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-14 [四款大六座智能增程横评：华为乾崑ADS 5、四激光雷达与鸿蒙座舱6，谁全系标配？](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBsbHlZQUo1M3ltOGpKSkNuYVRZQzVVM1dpQjRQdGhEMnhOTlFMS0dzNXBlLUdWcDJEUHJRT010emo1T2oyaWNYUEQxNEdKNUVXMWZmM2tTQW9WZ3IxNjBZ?oc=5) <sub>新浪网</sub>
- 📰 2026-11-14 [新款岚图知音限时19.79万开卖！搭载鸿蒙座舱5.2，上车华为乾崑智驾ADS 5](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNS2VhRHBXM29XMEFJV2FoTHlDd1dzOEh6U0ljcm9NdEFHaXdJa005RWUtZy1ibkRCVnVDWXN2b2YyUHFULW9MSWs0LUktS2RRYlJiU1lWUEs3WXpqWGY5MVJuNldOTVBwbTFnZC0zdnl5ay1IeXRSN0J0SlNpSE1HeHJnbW1zRmF1?oc=5) <sub>Sohu</sub>

</details>

<details><summary><b>Baidu Apollo</b> (35)</summary>

- 📰 2026-11-13 [Hail a Robotaxi: Where Self-Driving Cars Are Already Normal](https://news.google.com/rss/articles/CBMijwFBVV95cUxNd1FvOVRITjBwRFRUYUQtVjlSWjRqQjRHM2lBXzBCWnBSTF90bzQ5MkEwSG9sa3F0ekR6bF9GM1d5QWQyOUdKQk9XdGoyaUVjQXZjVldFcDJ0amZENkVOOUNSc2tlZlhXS0JESWJmRmFidlBVaXFrYXZkZWZOM0JPQ3Qybk10S1RSc3p5WGM4OA?oc=5) <sub>Yahoo</sub>
- 📰 2026-11-13 [鹏城迎APEC！无人车穿行深圳，外国嘉宾直呼不可思议](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQZXEzdEFHZkF3VE1IUG1XYnlfYzdOWWw4Tkh1a0lCemZ6Z08wbUNyYlliZ3RsYUc1YnR6SlVhNGNrYXNNQktyLXR0cVFJaVl6dlBvR3g2Nm53RUZ6RF9kX20zU0lDWW5zN01OR3IxczF1OFRNTENiWmhKdGo0dXlPVG5RS3RPUnYycXlV?oc=5) <sub>Sohu</sub>
- 📰 2026-11-12 [百度李彦宏：今天的具身智能大约相当于2016年前后的无人驾驶](https://news.google.com/rss/articles/CBMidEFVX3lxTFBEal9NZExGTzFna2haSzdhSnVwR2VLZDA5dm81MjFmMXJhWFcwNEJXMTBxc0NzTEVFY2dvWi14d1Z6RUxkREpsNkd4N2JoSjdQMDVnMjgtbkFiRWJYejQyMUFYS3gtcGxtSXA1aUJLUVRjeU13?oc=5) <sub>金融界</sub>
- 📰 2026-11-12 [萝卜快跑联手神州租车在海南推出无人车租赁，关于无人自驾游你想知道的都在这里（Q&A）](https://news.google.com/rss/articles/CBMiXEFVX3lxTE1FcHRhbWk2cVdabFAyWHcteWFMQk9DSkR6aUZfMmdIWUlmU2tsNWZ1bUsxZGQ0UDY4Vndha0JITWlGajRyc2kxWnJ2MzVrdm5BZmN6c3JNS1Vpd0hM?oc=5) <sub>网通社</sub>
- 📰 2026-11-12 [百度世界 2026：萝卜快跑把无人驾驶做成了全球出行新服务](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9lSDh4ZUdHSTdGQjNEZFpZTDFJVGVuamRNdndvQWExOVJnUXQyZ3owSTIzTU5sakF2Mk5PbGpNWlEtN3BpVEFKdVlKVnljcTJBU1FqeVEtMzFhdkk?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Pony.ai</b> (58)</summary>

- 📰 2026-11-14 [小马智行(PONY.US、02026.HK) 2026 年第三季度业绩电话会｜长桥证券](https://news.google.com/rss/articles/CBMiU0FVX3lxTE9IVDN4YkNZajJEX1hEYXNpeDZNV204M1lzU3F3SmUtN29NbDVSUExzU01KeTZJRXJTcXBJOUVXc0t0WGFvcnpzQm93UVFZY3loWk1F?oc=5) <sub>Longbridge</sub>
- 📰 2026-11-13 [小马智行将于11月18日盘前发布财报，一图速览分析师最新预测](https://news.google.com/rss/articles/CBMisgFBVV95cUxPYVcxVjZZbVVYNTdjclg5emVCMmlOb2VDU0t5SXZQblRNXzEwSFpIU0VLbGktTHNRaHZad2ZNdnUzcDJ4cFBsaDJwSkU3VUJ1amFub1BGa2N6SjJwUHhBanltbHVKeHJpSlZwZE1CdVdpb04wWVFGcXFfbG5uUWU1MXJzcWFOeUx6NllWU0dWLWtsOGRzT0J5ZHRGU09xUm5acUFCZml1eGFyX1RaNnVlOXhB?oc=5) <sub>Moomoo</sub>
- 📰 2026-11-13 [Blue‑Green Signals: The Autonomy Revolution Shaping Transportation](https://news.google.com/rss/articles/CBMikAFBVV95cUxQaDhyZW5kYjJZT1JVTF9rM3ZXeFpUUnlTdHVOVE80cTlOV2thczVobTNoa014SlJlUTJLTlNYczlPZ0R6SC10SkVYRThZRWdrYUVoU0JXR1NScEJQNWZGOVhDMVNxVWlqS1hIQkxTYzZVLS1MWTB2dlUyWUpMRXFSVjJ4N1ZRQUhtN241cFZoeGY?oc=5) <sub>Vocal</sub>
- 📰 2026-11-13 [Hail a Robotaxi: Where Self-Driving Cars Are Already Normal](https://news.google.com/rss/articles/CBMijwFBVV95cUxNd1FvOVRITjBwRFRUYUQtVjlSWjRqQjRHM2lBXzBCWnBSTF90bzQ5MkEwSG9sa3F0ekR6bF9GM1d5QWQyOUdKQk9XdGoyaUVjQXZjVldFcDJ0amZENkVOOUNSc2tlZlhXS0JESWJmRmFidlBVaXFrYXZkZWZOM0JPQ3Qybk10S1RSc3p5WGM4OA?oc=5) <sub>Yahoo</sub>
- 📰 2026-11-13 [小马智行港股跌4.23%创新低募67亿港元基石浮亏76%_证券要闻](https://news.google.com/rss/articles/CBMibkFVX3lxTFB4Y2p4TXlPVHhBdmU0WGdmTkF3TE9YUjZCQklDY2RXdlNYZFdBRXNYT3pnWEFiRWtwY2gxbzlJenJ4bnRfSDVaSGp1TWllcGNhU3ZHaWZBb0tDT0o2TzVRWG9iMzU0THdOY3NPbzNR?oc=5) <sub>中金在线</sub>

</details>

<details><summary><b>WeRide</b> (84)</summary>

- 📰 2026-11-13 [埃安Ray7限时11.47万元起 后驱702km续航](https://news.google.com/rss/articles/CBMikAFBVV95cUxOd2VxcjlQQmJWWk5LVERkLTZBdWZGcnNXSk1nLVp5UUFTbkg1MEdkV2M5S3RkUkRHcFZjdVpVdEpteXlrRmg4cU50SDB4MWhuZkpsN1R4b2ZSdzRCbEk5aF9DYmNPdmQxbEhXbGs4WDRZbGx6Q1lhYjNScFdSMDVzdzM2VEY2c2htZnd1U1R3NXE?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-13 [都说13万只能买代步车 莫干山试完埃安Ray7这话得改](https://news.google.com/rss/articles/CBMickFVX3lxTE51aUc0dkdjb1lmY3VLYnBEaU1LQnU1ZndrMW9rdkw5Q2xRbW1CdXpjY2MzSTExNW5TSkN4QVdncWt4T3FfMGw0RWZuRmh5MThMLU5lV2lVVmJyOFhFczY5M1NVcDdzWDlOOVNpUkJpZVAwQQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-13 [CLTC纯电续航702km！AION Ray7上市：限时11.47万元起](https://news.google.com/rss/articles/CBMijAFBVV95cUxPNHVPcUlvMTh4aGlPSFFlNVloOUQ0NGNRaWZ1LUttMDNaRnBxMGswVFRRWUdqUHFBZ3plWnBCWHRZR3ptN1pyVElKWkZHQS1Sa2xzVnpiZlNab0t6WC1MYU5nakJMRC1JdXVieEhvaUFUTVVRWUR2akUzZTh2d292SF9pbDJZSlU1bm9DTA?oc=5) <sub>Sohu</sub>
- 📰 2026-11-13 [我们的APEC局②｜从广州到新加坡：一辆无人巴士的出海故事](https://news.google.com/rss/articles/CBMiigFBVV95cUxOSlZqbG1OZEdNQy1PYVVHend5THZKWDQxVUxZaFRWRGM1c2pxa254c2tJR1d0QlZDd2lqTnhDak5Dcm1rb20ySWw4VFd0SzRUVTlqYkU5MkRDaUp0WHRjNURVWG5uTVItcDdyZnAwR29pZ2dhcTRtWkNpcVg5cmtuSV9kT2NaQ2xNb0E?oc=5) <sub>广州日报新花城</sub>
- 📰 2026-11-13 [文远知行赋能AION i60实测两度刷新纪录，好评率超90%凭什么？](https://news.google.com/rss/articles/CBMiiAFBVV95cUxQc2t2YV9kUmx0SXI0SXZaSWRQem1mbml4YkpvUVZyTkFXZTU3LU0zUGpzZ25JV09UcXVldGk5YXFoVHZ4YmJpMTltYmxlaTNVQ0tHX0lTQXJYeGVvZ3p6YUdiNFJubTY4TGxsMVYyOWRIVmJpbF9EVEJ0TG1RTk9aQkw0X1Y1cS0y?oc=5) <sub>Sohu</sub>

</details>

<details><summary><b>Horizon Robotics</b> (52)</summary>

- 📰 2026-11-14 [Nvidia Leadership Reshuffle: Why the Automotive Sector Isn’t Panicking – Key Insights & Industry Impact](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1kSEdoX0tub1h1eWVpZVNYdlNFSDNZTFp2Tk0xYW9SNTUtSmlnR05RRk51YXdGQjN1eG5FUzdCZVJWVU9JYXBzVnQ3anpxb0N6cDMw?oc=5) <sub>36Kr</sub>
- 📰 2026-11-13 [ID.ERA 5X Starts at 99,900 Yuan, SAIC Volkswagen Finds New Competitive Position](https://news.google.com/rss/articles/CBMi4wFBVV95cUxNVjYtTHhSQzJYLWNBVjdSUy1uZF9SNENvLUlUY2txRGcxU0RmMlh6Qm91T0xZQVE5WjBXOUVIaUJ4WUxPdkJXbDlsRU54ZHd3anVuQzdnTnZzWnVCWjZxX3NNaWN5dXRDQzI2SGFnRTdBSEtjOHlnN0lnZGJfaTNtU2RHMUFIX0toRVl3bUFPbG0wcDBjUFR2VTlJSUFvZy14S19NUk5yeWplSnNlUTZNV01IUGZfMlZ0MGswaTVHZnVUdThJXzJSbFFFWDFoYlV6SHAtU0RNMmhlY0RiLUJjNzVFdw?oc=5) <sub>Gasgoo</sub>
- 📰 2026-11-13 [【视频】地平线 V2.1，路况再乱也从容](https://news.google.com/rss/articles/CBMia0FVX3lxTE00eVBMN0hDbXkwalg3TGk4dFRRdGJCUjVqeWYwZUwwSE9DNzNseTEyRU91RDFiNG8wMUdWTEZvMDliaXJTWHVxeVg4aEU5UnNEcTF1aWFqbHg4VTNqaTU1cEc3UUFCR3kxSUJr?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-13 [【视频】酷睿程HS8+地平线HSD，ID. AURA L5同级独一档](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5OZ05KS0Z2UFAxN0FvNnltQVNOaE4wYUlWdWU3LW5KWi1KaldVNFpGd2dlbHA1WUtoWmx2QUlHeXBuS0RkSGJiQVFDRDZhYUVCaThOdmkySk9mSVE?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-13 [VW launches the ID. ERA 5X in China with pricing](https://news.google.com/rss/articles/CBMijgFBVV95cUxPSFZqbjVlZkNxSnF0Z21yeUtodWs2QV95YVlQUW9McWo1YVVyTVVKb2RtNnVQQXI1a2M3dmp3c2tCTlFMYVdGRXc1SnIzVFM2aDBuMEtIUXlzZmQ1WEV1MGZpMjBVeXhERHhrWVhDY3kteFFxcUUxMmh5WDdRcUhqMDdiTEFneFpaZG53M3BR?oc=5) <sub>electrive.com</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (21)</summary>

- 📰 2026-11-14 [DeepSeek无人创业](https://news.google.com/rss/articles/CBMiTEFVX3lxTE1QUnM4dm1XbE8tWmIwSE1hN1JMTjZKRklrM3FmbkdNbVd2WllWUWpjQVhYV0xwaHhqUHp4T2ZkMGpHMExqWjFNU1lPYXo?oc=5) <sub>凤凰网科技</sub>
- 📰 2026-11-13 [【视频】小米澎程N90和特斯拉Model Y L怎么选，同价位还有哪些推荐？](https://news.google.com/rss/articles/CBMiW0FVX3lxTFB6dElibXRFYWFsZU9vQnhjX3YwZjF2VVd6QjhLdXJIV3pmRGhzTmpuTFRER2xXV1Zjc2ZqNld2RVY1MkxrTENqczVRc2MwNHl1VFljSkt2TjRxZ0U?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-13 [Valued at over 500 billion yuan but barely producing founders: Why DeepSeek has become a "settling pool" for AI talent](https://news.google.com/rss/articles/CBMidkFVX3lxTE5BN29naDgxcE4xa2NUUi1qSlFKTHpBZlVjVVozN2FaWS1kVy1ENkxsV0dxVTlQS0ZJWHkxV3lfY09LN2xldl9XYk1mTFA1SjBUdTJfV05LYWllNFJZZ3RwV1VPSmNQZGk1a085UGFMOXloMHE0d2c?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-11 [【视频】特斯拉发函，媒体CEO：放马过来#特斯拉#埃安Ray7](https://news.google.com/rss/articles/CBMia0FVX3lxTE5xOHhzcEd1V1RKWmxPZ3BEYUN6NGRhOXB2cHFXSWxFNGEzdjFPbkotY0VMQlpGTGxyV0FCc3p3S1NkU1NjSjI3b01nN2FTcnl3blB4dC00UGlQNlk0Ukp4SEhIYUtSVXNhRlQ4?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-11 [【视频】26年特斯拉YL](https://news.google.com/rss/articles/CBMiW0FVX3lxTE15a0hBYUc1enJBUDFBTkRRNlQtdGs4OFU0NjR0WXNFYnhHX09YZGd0WTRkREJVZlVwSTBNaGVUY0ZUSmU5WEFWQlVnZ1o1dUpCNENiYVptdHZYa3M?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Mobileye</b> (11)</summary>

- 📰 2026-11-13 [Korean Optics Maker Optrontec Triples Profit as US Automakers Replace Chinese Camera Suppliers](https://news.google.com/rss/articles/CBMi3wFBVV95cUxPWHNlSUphR3lWUXJBNm93Mm1QdFZ1MVVSZU9jTlBxc0ZuR3JyU3pYQU9OUmk4VDh1NnhCMnV3dXdSenBkVldzS09Zb0NVeGJSc1V3aXhiU1E1aTNsd1RydXlIT2RDdDk5SWZUOC0zbTNlbUxxZVpMaUdIcm1lRUM4U1k0TVBhUmNtMXlCUDh2Vzd3dXE4aGxCRDZlaU5MZFNHNllfRDM3dXoyRWlTckRFREZfRjBpNjhLaW5YVkd3OWJuQWRLVmE2ZFpOck9zdXZrYnVXZk5pYks2WnFKNURZ?oc=5) <sub>Tech Times</sub>
- 📰 2026-11-13 [Automobile manufacturing stocks Q3 recap: Benchmarking Tesla](https://news.google.com/rss/articles/CBMivAFBVV95cUxQemM0Qm9BZXFLb2o3YWdJWkFwb1FLcVdMb3NZNDE2bTB2U0hTb29PbnRiQXhFejA3ZklYUEdTR1lZaGpFT2tjOWJPT0luaXF2aXI2ekRhSlhPQnpQNWxQQUpLdTAyeWxvN2dBV2dNcEhiM0VDOWtwNzNtUHlSVVBmMVR3eDZKTWtXSWRvTUd6V1FhVzRqX0MyMDZjQm4xdjAwRmREZEl1X1V3b25CVk9MSUF6Q1draU9nZU1peQ?oc=5) <sub>TradingView</sub>
- 📰 2026-11-12 [JPMorgan Downgrades Self-Driving Technology Supplier as Volkswagen Faces Delays](https://news.google.com/rss/articles/CBMi1gFBVV95cUxNRXhmZ1ZxandRVnNmaEhwZmljMjNVemVoUEIzVFZPQWlGQ0lxeTNES2JuczR4dnZiU3hpUWlydklMWXVLeW5tWVBFSVVlY2hfXzM5dm4yWEZ4UmJYcTdJU2o2MWZhS1VMWkhwb281SndVb1BkN25QTUV3TURlUmxVTzdYTUFDVFVVTkdKRk1wVlpzMmZ0QjZqWUw5ZDU4dnV0bXhzZEtJYll5SkFlZFBxWFU2aGFvYVZLWHQ1d3RfZDdrdVFzQkVUd09lUjlqYjVTWlNSZDhB?oc=5) <sub>TradingView</sub>
- 📰 2026-11-12 [Tesla FSD Gains Ground in Europe: Is EU-Wide Approval Near?](https://news.google.com/rss/articles/CBMisgFBVV95cUxPOHl0V1BnS18xZnYxOTlvTmZ3bXpGckVjMXZxYmh3TmpldVFkMlhRSmRYLWl3eDI5eWVfSm1kcXZSQ3ZmSUYteXdISFVlb2ZRNG5oOUNzR24waG00cEQ2SUNMTXdFbDR3X1c1Rko0UGw2TnY2NDQxc09QSDJsWDRfbTV0OUNJb2JQNUgwZTY0ajhhT3BZUTBmVUotSGtwSE1wQW9QTkZuS0VsMF9PNE1RcDV3?oc=5) <sub>TradingView</sub>
- 📰 2026-11-11 [Mobileye Announces Participation in Upcoming Fourth Quarter 2026 Investor Conferences](https://news.google.com/rss/articles/CBMiwgFBVV95cUxOR29NaGt3LXBWY1o0YTZEZXBTaGhySjAycERjTVRxcEw1RjhXT21tb2hxbGk1ODkwWFZlbnBkdTE3ems3dW0tbWlUaUpUNUs3T0VJeXlBUF9wUGtLeEtVRGNnQmVsUWQzZEJxeHl4OGdiRjFpbGFkV3JEM3Vwb1NRVDZGc3EyZUpIQXpyV1NBckR2MG9sZGRvZWJRZk9ycDdrYWY4ZmtIS2pSUmpuZFFvX2V4VUVJXzZaS0xrQkNCVV9JQQ?oc=5) <sub>Quantisnow</sub>

</details>

<details><summary><b>Aurora</b> (26)</summary>

- 📰 2026-11-14 [Should Truck Production Delays Require Action From Aurora Innovation (AUR) Investors?](https://news.google.com/rss/articles/CBMi0AFBVV95cUxQM0Z3WEJQclFZaGZESEs2VUNRSXRLVnAzUW9Mdy1hSFQ0QTBXdWs2ZVd1SDdFQXBFZWhGM0IxamZKcmN6VGQwaGpORzFNdEZvUE16T1pDN3VGa3pmRmR4VHF6YV9yMFBVYnllUnlOdmxzWUR4bzhab1A2dlVNSFllS0NmQXBJQ3BRcDN3V0wtQy01R1R6ZmQ2SHpkTFFVNTBmZEdTTGlJVmV1YWtHX1F4c0lJWlljVXZkbWlKTlZjMDhLQlgxWGtrN1pJc0RJYVhO0gHWAUFVX3lxTE1VS1NpejQzUVhxSnEwMjZ1NE53QUlwMHZ2dkxRNFhpSlE2RHJpeEZ1ckZFZlZQMmxGbXYyRHNXaXNWLWNrODc5eW1oTURNc3ZSUVZOY0FpaEh0UEZUcjJMZjJJWjFLWDNxX1VEVzE2a2NGTEtwZDZjOHctVE53Q094YlY3c2NybEN4UTV6MEZSTjlvRlhWc2M1VjdlaUxoM2ZqTW5QRkVTVWR0a2hnV1ctejNVaFdiaXNzakV6ZGRIblEzVVp4Y0x6dF9xM0RiV2lCcDFFR1E?oc=5) <sub>Simply Wall St</sub>
- 📰 2026-11-13 [Archer Aviation And 2 Top Penny Stocks To Watch](https://news.google.com/rss/articles/CBMiwgFBVV95cUxNckZLN21fSnBMejAtZFNiTk9sbzlWM1drb2R0Qi1YcHdFbGZGSnlaLURxQUFqcUlIWkM4MGtMOE5tWXVob0FYczBvUks4aTJrc0lrMmlzLUNpV2FMT0p2eWI2alVBSEF5bnlqUGVaSklMYWFiTGVtaE15c0Z3Rm1yQ0ROWlZmeWhsSENHY2FjSnkwRTlKQ2JEY2RpVUJXd29fWFhUOEVicVpweFBiUlI2MG5rM083TTZQUlExbFpnSDdlZw?oc=5) <sub>Simply Wall St</sub>
- 📰 2026-11-13 [AUR Investigation Ongoing: BFA Law Reminds Aurora Investors to Contact the Firm about its Securities Fraud Investigation to Recover Losses](https://news.google.com/rss/articles/CBMiqwJBVV95cUxPRGpBZHRRMWt6QVZjTFNRc0xJQTN5N0RUVUp0VTJBS21vel9MTTgzTjBrMjFjV1EtTzBmMjlUR05TZHo3YWE0V3pnelhWWmQ1YjJnZy1CMnphNnpKSWZGaFJhTC03bFBGbWN3VzgzbnVRTHhQNlJoUUdyMEtMbzNVRHFKX3NIekZVbHcyaHpaXzNIQi1ZNnNlWC1ubGJVZDhvN1pIcWFXZnhrT191ODFTR1JORXNQSjFWSW9MV0ZRWEhUWkQ0U1pyVkNIOGljSmgwYlFXTzZhdnF2QlBzdHJqejhHY200aElLbjVSWjhqcjF3S1haSFZXaHFRRzlBU1hTWURaUVdyNVFWNG1rQjl2SG01S05GQmJLQVQzcTZqUWVqczVIaE5YdVc0RQ?oc=5) <sub>mykxlg.com</sub>
- 📰 2026-11-13 [Nvidia's Asian Supply Chain Prepares for Life after Huang](https://news.google.com/rss/articles/CBMi1gFBVV95cUxNWHpRZHV1RjdadVZscDZTNmk0bXRYMENJdDJEOFp4UWdUQnpacWZtbS1kUVpsdXZXb0FmV1F0eG0zMy1Oaks3MDdiUnhOR2FmMlc5blNuWGdldzZDMUJOUmwtOElheHNPaTJoWEdEajR0QUYzc3JLc1FnbEJqM293VXczTzJSYlZuZks1RUdqcjQyUlJwR3c5WHdLdmIyUHpDTm1TUVJqSmJLU3hLR2l1TExINlU1YWdZa3hSMzUtM09iX1kzNFpBTkVlTGlzWFluVE04d3lB?oc=5) <sub>SupplyChainBrain</sub>
- 📰 2026-11-12 [Autonomous Trucks Could Be Cheaper Than Human Drivers in U.S. by 2028](https://news.google.com/rss/articles/CBMi5AFBVV95cUxNZ09XbjNWYmswcURfNFRaN2poUF90MXRtN0lRSmlZclptYk5vQUptQ19Denh4ZlhyblRFNk9Vb3Vra085cmdnSWZyZE5KSVFMa3JhczgtdFZFTVVjVVphSWo0OGNiN3E2Q3VzN1lYaFM0TXhfVVA4R3RhaER1TmtBRkVuZWItQ2VPVDlWd3dfOFdPUC1VZ2V5dVJ2bl9qNTFwTjc4V2YtUGJQdGQ0Y3ZMZWc0Y0otdUlRa1BSOHlJUVNYWm93NWk4bTNRRG1aVmxpRDlmZTF6dDV3Qk1DM3JacFA2NFA?oc=5) <sub>SupplyChainBrain</sub>

</details>

<details><summary><b>Zoox</b> (46)</summary>

- 📰 2026-11-13 [Zoox expands Las Vegas service, rolls out next-gen robotaxi](https://news.google.com/rss/articles/CBMikwFBVV95cUxNeC1CcmxNUFdoeFU5TVBkNE9Za2U0d09pR0hQR0dDNnFjLU5feGhCa2FQN05tdTZ0NUFBVXhjS0p3bnlnWjdfZVB4aFdlVkw3MktUQU9NNWhJN3RUcXZzaUlaWndVWDFaT2phelkzZ0Qya1VpejgyUTk2TU5uTWJoYm8tVDNEWG9QRFRSTVN2RlRzaHc?oc=5) <sub>KSNV</sub>
- 📰 2026-11-13 [Zoox brings robotaxis to Atlanta, with public rides still to come](https://news.google.com/rss/articles/CBMipAFBVV95cUxOeXZodGdoaUJKMjhHMVBzT3pMLUkyMXp5djJzdnAxZ1dsTFVJTzVadmxYUFRLUEJ4ODVPQXJJLUlfajJOTVk5NnFwRkZ4eFlUcjVfY3NQYlN1YktxZTFvTFNPcjdxWWJGLV8xVWVMV1pFQnZKQlUwVmY1MVgxMS12OEZZVXIzVDVhWWp5ZnppOGwzS2NldWNoN0NkbWpaUW1pSmJkaA?oc=5) <sub>CBS News</sub>
- 📰 2026-11-13 [Zoox launches pod-shaped robotaxi fleet in Atlanta](https://news.google.com/rss/articles/CBMipgFBVV95cUxObkh0empNZjVlbnZISGtCMldKM3FOWkpsbUR2WFY2WG9wN0pvcUNYbEZuVWhsSmJiVkRidjFXYk9mNkN0LUtVeXdkN0NJNWJnTlFIWktWN0gwQzVkcnVMaG5yUkVlV2ZQSFpyS3pTTElsSGcyQnprUVpGMU90ckRUMDU2SHRTd3lJaG9wTDNaN3UwbHR4bF8tcGFfNzZRUmx2MUxOMnNR?oc=5) <sub>The Business Journals</sub>
- 📰 2026-11-13 [Zoox could soon charge for robotaxi rides in Las Vegas](https://news.google.com/rss/articles/CBMi1wFBVV95cUxQR3VIT0Q2S1VFX0JYZlpFSUU5Rm5JTzJDcjVKQ0tPQzZuaTZvRFBvOExqZnRXVWtKR0JmVmhuQ3B2N1B2RzJaZVR4b2JGY3JIc1gzdXluRVktdks0RlE5ZExyaldCeENZTFh0YjNYYjZMTUdYRWE2aWM5djdZMjJfaVR1b3BBS0ticXNSQm9BNnd0dmxtTkhCU3VTNi1IMzhMSUFIWnFJQ2dNbTFRa1dncDZLakxKM01YeTMycHBnem9YMmN5TUs1ZFZiMkJsNllQNkl0YUgyUQ?oc=5) <sub>KSNV</sub>
- 📰 2026-11-13 [Zoox Brings Purpose-Built Robotaxi to Atlanta for Limited Testing](https://news.google.com/rss/articles/CBMikAFBVV95cUxNaWl1UnZQRWpPR3RmcWdQMjIxSF9ncWh5MkhPT1pFanYydGk3UnhyTHl1dThwcU9RTjRDb0lVQ0tQdFo2aXFCci1iaHZzbzRkZHdCdzVvV1B5Y25FYTMzSEE0WGZuVVBoc29lS2g1WXpqUFZzemY2LTFpT2NXLWFMMDh1TkRrX2pXbUdHWVhCSm8?oc=5) <sub>Unite.AI</sub>

</details>

<details><summary><b>Motional</b> (15)</summary>

- 📰 2026-11-13 ["Cars That Keep Going Even When Sensors Fail"... Hyundai Motor Boosts Autonomous Driving Reliability](https://news.google.com/rss/articles/CBMiZEFVX3lxTE9BX3gtSThrelhocW04V2VGTXc5NnB0X1F6VFBlenZLX2Mzc01UY3o1c2E2eE8tQzdqbktEOVIyTzBtdnFOeXF5NlEzS3lIXzNLMEVzQ1V4dTQ1M3ZXY1FQR21pank?oc=5) <sub>아시아경제</sub>
- 📰 2026-11-13 [Hyundai Motor: "Safety Over Speed"... Ensuring Cars Keep Moving Even If Sensors Fail](https://news.google.com/rss/articles/CBMidEFVX3lxTE5Vc1NOV0ZacmFwUjhSNVhhSTc3VFQ4QV9DanB6aGNSWFhONW1CcEpyZ1NaNm9heUk2ZGhLRm9XaE5NcXVJZUtjUmJIeDQ2TUFEczBVem0tbGYtRkp6eVlhTjVHdmtVUno3NmRpZldWalhZbUYz?oc=5) <sub>아시아경제</sub>
- 📰 2026-11-13 [Huang’s Exit Puts Hyundai Motor Group’s Dual-Track Autonomous Driving Strategy to the Test](https://news.google.com/rss/articles/CBMidEFVX3lxTFBZTG1rU1ozSDFnd1diLWNmZVBXcFRjZ0J1UGpqZ1BCck83SFhJOUhBcDE3ZlZKV0tod29JZzh4dVctU0pYR2h5bWxSTVg3ci1XTUFMeVh6WmQ3SkpncVBadDZMX2p4VWlzSG1MQVh5NFZhWGVN?oc=5) <sub>Businesskorea</sub>
- 📰 2026-11-11 [Korean firms shift CES focus to industrial AI](https://news.google.com/rss/articles/CBMiqgFBVV95cUxQQVpGVm5oN2E0dXpVQ2tfaXVaZXlZanNWcllzRTJCc19OS0F3V2Z1eWEteEpub2dQWWJleEtYMTVyVkRGaVpmWmwwQi12V0JhdjlvRENjU3JWMlpLTkJkOHhMYl9JeDh0RU14Mm5fZmx0X1Z4NlJTYmtKNkc2ck4wT3pQTUZxYjFmQ2M5a1ZoTC1WSmZOOGxMOGJFakVoTm4tcTNaekZZdVFWZ9IBqgFBVV95cUxQQVpGVm5oN2E0dXpVQ2tfaXVaZXlZanNWcllzRTJCc19OS0F3V2Z1eWEteEpub2dQWWJleEtYMTVyVkRGaVpmWmwwQi12V0JhdjlvRENjU3JWMlpLTkJkOHhMYl9JeDh0RU14Mm5fZmx0X1Z4NlJTYmtKNkc2ck4wT3pQTUZxYjFmQ2M5a1ZoTC1WSmZOOGxMOGJFakVoTm4tcTNaekZZdVFWZw?oc=5) <sub>The Korea Times</sub>
- 📰 2026-11-10 [Tesla Fort Worth Robotaxi Field Report｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1aT2xVRzVDa1RNSDEwb0FuOTRwU1lPenVGSmhER1ZoRmJJdTZpeGlaNEt6OEN1SWxKYlBUS2N0aXprRnBPQ3NxVjB5VG9maVNGWHVWU2VwbW45UWpJS0xB?oc=5) <sub>finance.biggo.com</sub>

</details>

<details><summary><b>comma.ai</b> (2)</summary>

- 📰 2026-11-12 [Goodbye, BlueCruise! We Install a comma four in Our F-150 Lightning](https://news.google.com/rss/articles/CBMirwFBVV95cUxPY1o5ekZ4WnpraUxVMHV6OVdyMEtEbjQxQXY5STdJdXlHNlN6eUFZNzFwSnA5cFhHd3pNdTZNNy03dXBOZ1ZoX3RFX2E5V2JNTE9aVlhJaG90bW5YWEdzX2NGXzd3VFZ6NG5JVkFrM3daTmY4UDBTN1I4NWU3eGJqUm9tY1VaRWxoZkp3WDJLNnVLQjN5WG9NMzlxLWI0aVU2TFhLUEZwUE5YUDdUcWFJ?oc=5) <sub>Transport Evolved</sub>
- 📰 2026-11-06 [Canadian YouTuber Linus Tech Tips Tests Tesla FSD](https://news.google.com/rss/articles/CBMiggFBVV95cUxNZVZaT1Q4X0NlakJzTnFkTGdqTmFPM3pDbFZPUnBYVVNrVzFxMlpZQ3VaTEJFUmJrNVpjMmZ5RVphUDE4WURNT0x4NkhnN01LdTdzSEVnS2NUNkROams2cnNzNkpnalhWcDVuckhETUtxaDZrSHNXTXhKYUlpN2dPTlZn?oc=5) <sub>Drive Tesla Canada</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
