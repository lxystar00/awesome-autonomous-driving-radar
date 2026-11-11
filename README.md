# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-11-11 · 1,284 papers tracked · 45 curated.

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

<details><summary><b>Waymo</b> (141)</summary>

- 📝 2026-11-05 [How the Waymo Driver Manages Severe Winter Weather](https://waymo.com/blog/2026/11/winter-weather-preparedness) <sub>official blog</sub>
- 📝 2026-11-05 [Rethinking What Freedom of Movement Feels Like for Women](https://waymo.com/blog/2026/11/because-women) <sub>official blog</sub>
- 📰 2026-11-11 [Waymo tests self-driving cars in Fairbanks climate](https://news.google.com/rss/articles/CBMimgFBVV95cUxPbm1XdE1WU05kaHdxTEFOd2ZwT3VPMFdRd19GZmpFaWU2QjRMNXQ5aGtXVGJGT3VmbU16WUF1ajJBa19pZVJwckhEbDZvYmdJRzNESTF6ckQ5dGZzcG5CeHFBU1BPOUJTb1F6YVVZLV9Pd08tRWg3VW04ZGYxSDYzalV3TWNhdHNRUkhwNDlhWWpvZXVXRWI0ZjNR0gGuAUFVX3lxTE5MRkk2bWFYSnRoRU85akxBU3g2OXZlb09RT19iYUQ3SGdlOVZRNmY4Mkd2U1l0QllnaF9hZXVrNzNLUGVyeEVMdkhpU2pUTU5JalZNN3lJREVSVlVYUmlGd29menZSdzBxUkFwVkJRLTBRajB6U3AtYmFCdDA1MnVvcUlQRTNIRWRkMHFqMVdkQ1BuanJFaGh1NVY1R3NFU0J3bkpBQVVRMjY0cjhXUQ?oc=5) <sub>KTVF Fairbanks</sub>
- 📰 2026-11-11 [‘That’s The Bet’: Palmer Luckey Backs Elon Musk’s $150 Billion Robotaxi Ambitions as Tesla Tops Waymo in Texas](https://news.google.com/rss/articles/CBMi7gFBVV95cUxOczFuR3J3ZHR0bVRHa09ZdGpmWVJobjlyck1qdUY2T1BzYWZjdUNPQVZjekRzUXd6ek1Yd1VKaG1wZUx4X3djbE5qZjI2TlhXZVAzTW0wTlpfNTIxTG0yYVl2czBRb294VGlTM3VCN1YwdUZYVnpSSmVyalFTUXhoWjJobzlCbE94MVJmdVFLOWNwdHVUTkxkYWlTZ0djMFZuTWpJZzBYYUp3UkpXSjFEbVAyd2Jhc2VMYzRIX1pWamtDODgyQWpPS0tWVjFpR1NROXRsM245MkphNWlJMXA5OFhVcTRIRUpCYUZZRlBB?oc=5) <sub>Benzinga</sub>
- 📰 2026-11-11 [Introducing the Waymo Accessibility Network UK: Co-Designing the Future of Autonomous Mobility](https://news.google.com/rss/articles/CBMiywFBVV95cUxOdDBGUm14V09RazdmM3FjLV8wTFkyMWdwOFNWckxyQWNZNzdDRHhjd2daY3ZYR2sxVVN4NlZLOHJVb3FWQjVWNF9xWHExN2djU2Q2SnQ2MDV3WkcwVlNMcTl2bUNHR2FnR2VrT2lISnpKMmFaU0ozOWdyckZqZmZzVktZbXpmU0ItRDAzUUVDRHpNNmZVTDUyV09XbWV6aldyMjJPQ0c5bWJBS1U5ZmpPbjVVbU05bEdxaXdDWFdZdkVHRE5WakM0R2Rxaw?oc=5) <sub>CleanTechnica</sub>

</details>

<details><summary><b>Tesla</b> (197)</summary>

- 📰 2026-11-11 [Finland approves Tesla's Assisted Driving system](https://news.google.com/rss/articles/CBMiogFBVV95cUxOTlM5bTZEWktQbU9STjk1NE9iMjNpUVJaNUJXcVI1bUV3ZmxPN2p2NjQ0c2ZaQXdITlJkeDNCYkV2MjgwVjlaMjFYTnN6U2VGMHBJNDV3T1VTZ3IwTnVRcGtxdGR5djY3VldGVnVhOEg4YTI0dEUzbWJJVUFNeHZoa1RuZVphZnU3SGk4b3FPeEcxSjR1aGVsMUh5SExpNlZINVE?oc=5) <sub>Reuters</sub>
- 📰 2026-11-11 [‘That’s The Bet’: Palmer Luckey Backs Elon Musk’s $150 Billion Robotaxi Ambitions as Tesla Tops Waymo in Texas](https://news.google.com/rss/articles/CBMi7gFBVV95cUxOczFuR3J3ZHR0bVRHa09ZdGpmWVJobjlyck1qdUY2T1BzYWZjdUNPQVZjekRzUXd6ek1Yd1VKaG1wZUx4X3djbE5qZjI2TlhXZVAzTW0wTlpfNTIxTG0yYVl2czBRb294VGlTM3VCN1YwdUZYVnpSSmVyalFTUXhoWjJobzlCbE94MVJmdVFLOWNwdHVUTkxkYWlTZ0djMFZuTWpJZzBYYUp3UkpXSjFEbVAyd2Jhc2VMYzRIX1pWamtDODgyQWpPS0tWVjFpR1NROXRsM245MkphNWlJMXA5OFhVcTRIRUpCYUZZRlBB?oc=5) <sub>Benzinga</sub>
- 📰 2026-11-11 [Tesla Robotaxi Media Control: 3 Claims Unconfirmed [2026]](https://news.google.com/rss/articles/CBMikwFBVV95cUxOVkRrNzdUSTFyS3VlU1NlUG5KVXU3bzBXcVRyYlBXSVdMUFNFU0thNVFLeFg1T3FjRU9kc3d2NTFqSFFfSk5iSEg1WEhNOVd2QXB2OFQySV92UU5QWmJBbmtXTzNsbzBPUGpzRFl1c3VrZ1hGbWc0VHNNUi1sbWdGdXFwbUxHZy1kcUN5aW9hcUI1b2M?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-11 [Chinese media CEO defies Tesla's legal threat over unauthorized FSD testing: "See you in court"](https://news.google.com/rss/articles/CBMixwFBVV95cUxPTG9yTXI4QTI3cDRxWktObi03eU1TeFdfeDd4VFRFMlZRWExNVk4yRmFIU25nUGVsR1EzVE1Ma1VwVUhEQUZFOGxrR3BUYUd2R3A0VW54WHNOcl9abnJGX3lZMU5WS3pnUzJiV0RzNml2TWFUNEVjUjlyWlNGclhqZGJSalF2TURWLTNMeGo3UFZ6WnpTc2pwdmZiREc1ZU1DQlEyWkZpRnRvRDRVVmFPT2ttRm9oZ2p1Y0NjQXZDWFQydDBQRWp3?oc=5) <sub>CarNewsChina.com</sub>
- 📰 2026-11-11 [Tesla Robotaxis Extend into San Antonio](https://news.google.com/rss/articles/CBMigwFBVV95cUxOR3FjYkc3dUUzT1ZyaVRLT2xJUUNhTFU2dlp3Vjh1LXlkMGlOX3hMZUdCZjhCR3NfY3RGbDRudWZoTy1FeVN5TVZ2bUNGczlicVBVSmprYXE3VWRKX3JUdFZZWFJCQXloRjM0WjRraFZzQkN3aUxsUUt1LVBVRVZrYW1kWQ?oc=5) <sub>CleanTechnica</sub>

</details>

<details><summary><b>NVIDIA</b> (111)</summary>

- 💻 2026-11-02 [NVIDIA/nvperf-core — Core NVIDIA Nsight Perf SDK APIs and libraries for collecting and analyzing GPU performance data directly from application code.](https://github.com/NVIDIA/nvperf-core) <sub>GitHub</sub>
- 📰 2026-11-10 [Kakao Mobility Partners With Nvidia to Develop Autonomous Kia Vehicles](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1VS0gxNGViX2IyQ211cVhMSTRxQ0lUeU9GcHhZSVhUQnRSaU82bGtNM193eUpvTmYwd0xZaDR2eDdVdG04U0hfZ2Q5QV9jM0hnM3J0WHIyb1lxS2tJMlA4WXZzbGVQSWc?oc=5) <sub>THE ELEC, Korea Electronics Industry Media</sub>
- 📰 2026-11-10 [Running AV Reasoning Models Within Onboard Compute and Latency Limits \| NVIDIA Technical Blog](https://news.google.com/rss/articles/CBMipwFBVV95cUxNenBjcEZMVlVoTTJBN3BaWHRtdzF3QjItZU96b1N3Q1NkbFhneFhzektYS1RxLXhPSnFkOHVHTGVjQ2lQX0tuYUtpWU1NRVB6bk1sbm0zaG14d3d4akE0eTRTSi1BejNEbExNNGNZQXJKQ3p0M0l1bDBUb0xBblV5RlM4R1BqLVVzV3NLa2Y4c3pYZFAyVnRXVGF1XzEtWEYybU5XeVhGbw?oc=5) <sub>NVIDIA Developer</sub>
- 📰 2026-11-10 [Autobrains Brings NVIDIA Alpamayo Intelligence to the Road](https://news.google.com/rss/articles/CBMirwFBVV95cUxNb01WR190R0dOalpMSGVxX182S1B3dU9yS1EzeTBEeGtQTlhqMVBpYmZtZlNvLS1qdzcwODZCbTNRbzEyNzF2VjFwVU1hU3dQVGJGa3ptQjJGMHBCQ2xHazEwejNrbEJ1cWRKWEJlNEYxWm13NkdwT1lKWHJfYmRhVGtSWC1PTWp3UTZud3NvZGxpcVljSV94ZndMbkRkSTFxVFoyZ0MtSmNpcHptNTQ0?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-11-10 [NVIDIA Releases Alpamayo 2 Edge Weights for Autonomous Driving](https://news.google.com/rss/articles/CBMijAFBVV95cUxPbDBIYTNEQlVWWUZyZkpzNi02Smp0d1JQVDFVZG42TEk0WUhHbHJmbW9lRFB5TlJYUzFLUGNoX1J3RDZfa3k4bXA2Y0ppRUVKUFBWdUhxZXoyanJjRGRNX2R0LVdmYjlKbGZxSUdYQXU5Zl9UU0dwaUtXVldkOUdmazJsMGVoT182Z0JCRw?oc=5) <sub>Unite.AI</sub>

</details>

<details><summary><b>Wayve</b> (38)</summary>

- 📰 2026-11-10 [What Does CoreWeave (CRWV) Winning A New AI Training Deal Mean?](https://news.google.com/rss/articles/CBMimgFBVV95cUxOcDNZY2dVeVo0ZWNwN2hmZDlEZFJOelNPMy0yRmhWRzV5UjV5Q2tmNEtxN0p4d2pTb29iR0FtZjFueXJvUzB5cVpxaXBnNXpwelZXTXFEdzFvalotZjB2bWc3eThkS3BLZ2xLN3haOV8xRERuY0hYRFQtVjRsc1VvNE9FclhlT1YyVnFhWkFtaThfTkszRlVNa3V3?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-11-10 [CoreWeave Cloud to power Wayve's AI Driver training in deployment of autonomous vehicles](https://news.google.com/rss/articles/CBMixgFBVV95cUxPMUNvcEZsZ3kzNzFsN295US1lLUlUQW5xcExTdFRwMm91ZG91dlVHU0lyeU40b2dweF9aYzBScEd5VHZXRmtBLUxYTTFkbzdheTFUN0Jrb0xiWklZWExlV0ZpRzZ1ZGlUNTlhaVdnM1p3aVdSdlRBUjk1eXBLRmRHemVUdk13WTRnUmU5bG5ReHREQkFPU0NxQmtRMk9qYXJpbk40cm82Mko1Y21oUGoySG1OeXZYZi1Ba2l0WkFQYVV2V2liWXc?oc=5) <sub>ROI-NJ</sub>
- 📰 2026-11-10 [CoreWeave Falls 1% Pre-Market: Strikes Multi-Year AI Cloud Partnership With UK Autonomous Driving Company Wayve Ahead of Q3 Earnings](https://news.google.com/rss/articles/CBMi0wFBVV95cUxOVTlxMlUydHpuRlJWdXdoNHU1Z19ISmg0UTcwaG1tNXh1YnpMOVNmSXdzZXVqS19uSG9oU3hJaXhFSFNpdktxWmdQR0YwTENiT3R6d0RJS2JwSDA0T3pYWG41T1pJWmpFaDViV1F3SDJuNnduc1N3U0h1SVRRNWYzY1RkY3planFLV1dnYmllMy1YN29fUzUtWVdyb0d4Q3VsbDlZNHpIeFNuQm5ldjRlRklPOFhoSDVsSVhQd2VrZkptVURGVVNyNHlrTlVOUWc2NnU0?oc=5) <sub>TradingKey</sub>
- 📰 2026-11-10 [Wayve bets its driver on rented Blackwell muscle](https://news.google.com/rss/articles/CBMisAFBVV95cUxPUDZ6bGVHcndyRzNMVzNqdTdWVHUyT09VTG1FNkVNd05iVWpNTTgtb0p3ZHRLUlFUd2c4U2Y5bzYwX1pKeHh2RnhFRUZ4MTg5TXJPZzhDUUJEU0hyTF8zcWNKX05lOUItQVNpTEhfTk4zS0d1bkN0NnVxNm1SNzlMbmI0UW9QSk1uMUNwRVlSNFZ2S3oyMmw2d2JobUV4bGpPdFFmMnJiLWI3MmxRdjdGYg?oc=5) <sub>StartupHub.ai</sub>
- 📰 2026-11-10 [CoreWeave Lands Wayve AI Training Deal, With Price Undisclosed](https://news.google.com/rss/articles/CBMigwFBVV95cUxOQ2NWNy1paVdrOXVObUwybkVmNk1aVUFIQ1lwVktJSmFJVG51VGJLZUJPekZvX2dOVkkybFo0dUxJZE1pQV9PZGRmU2tVVjV2bkRxTzl4WFhua0FmSkpjd3d3Y21QcTZidmFqcnlRQ2V3QkVJclJlck5pVzZ1U29rQkJvMA?oc=5) <sub>The Eastern Herald</sub>

</details>

<details><summary><b>Momenta</b> (69)</summary>

- 📰 2026-11-10 [3亿元！上汽集团成立新合资公司](https://news.google.com/rss/articles/CBMiiAFBVV95cUxQaVlsRnZrOFJwN2I2clBxdlJXRGZfSlhsT0ZMcjAtZ2J3U3FIc3RhX2hyNDVoaEJNRDNUaWpnTWVQa3R1cl9CV2ktcVV3ZzBjdjh5cGtDRy1MQTduVkVXRmtMQUFzejhGREtIM2I5NlhzT2gtWTR4c1RVV1dILVpJYjl0T3Y5ckZz?oc=5) <sub>搜狐网</sub>
- 📰 2026-11-10 [东风日产NX7定档11月13日开售值得等吗？3个维度说清+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1BUGFObXRVTkROUWxEd0Fsc2phekhhQTlldU5fSzFCei1RaUZFazBzRVN5Sm5oV0EwUDNQdUJPczlmVmJFTVJ5YjdCN1E0UE1CRFpwRzJzUDJjbjFZTzBJ?oc=5) <sub>新浪网</sub>
- 📰 2026-11-10 [奔驰跳过L3直冲L4，引入Momenta智驾](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9WOVUtMEhKamt5NVIxMGkyRFZBOFI5ZUw4MF82Z1VVR2FYOGlNNFVZOUNTdUhCbW93eTIwZTlOWVNRZmlJbnEzcXpzUzRxVjZ6cWp1MEpLbzBXN00?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-10 [电池+智驾外购、配置看齐国产，日产NX7能打动看重合资的用户？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE84TlFBTHJmWFp4S0ktWGFHQzU1S2NOWi1tMGNJcmZGd0lwUmZhZEFqSkt4RVdCQlE5aTRXajhJaFVZaXQyNGgwUmlxT3ZIOVNRaDE1TUpBVE5UOGc?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-10 [Zero Interventions at the Arc de Triomphe, a Love Letter in the WSJ: How 100% US Tariffs Fail to Halt the Global Surge of Chinese Automotive Tech](https://news.google.com/rss/articles/CBMinwJBVV95cUxNQnNxQ2NGS0VCSkc0RXVpSFlnVTh6WUQwa2NEUnpfMXJlNEVqWW5FMW1yazM3UXdMVTRWZllLWERCRWphWkRKOTM0YUUtby1nWVMwYnp6V2ZqUFI3bTlEYkhwYUNjcmVVWDdKSTc0c3hVSGN0VThxWEFxZU1TUHBRYWw0d1pmMzNsUE5xYnhENTRCMzF0ZkU1a2NBejFzbTZXa19UUFVoTnRBci1LTnpURXlPMHd5UFlWakVBQWpsWndNQ3pBcjk1VHJxdHFBWXl5SzhtVmxwTE5XSjZKYkVPZmJpUVNsU0toN0ZYQ1ltSWJsTXFZVjc3MGJoU2c4RHJuS3JDRVVkRlRXTmFqNzRheG9lemZuLVZXVWM5WVEzZw?oc=5) <sub>巴士的報</sub>

</details>

<details><summary><b>XPeng</b> (144)</summary>

- 📰 2026-11-11 [China’s Temu, JD.com revamp business models amid tariff headwinds](https://news.google.com/rss/articles/CBMiiwFBVV95cUxNRl9telcwX3RuSnRkNklYOHpTOWw0SDBPdEo3UVBhZWxpQ1ZnR0IyNFhDWFUwYm91R2o0VG51X2dIZlktX2FWZFgzejc3Qy1rZy1pZnJDbms2SmJadzdKVHp6c3R5Z2hpQjJyS2pVZUozNVhDeDRHaWdPeFNZbXhQUGkxaG1IZzBOQ0Zz?oc=5) <sub>KrASIA</sub>
- 📰 2026-11-11 [EV World 2026 Opens in Dubai: 300+ Participants, Autonomous Taxis, BYD, XPENG and a Big China Partnership](https://news.google.com/rss/articles/CBMizAFBVV95cUxPSm9kUlR0Q1gwbG5EbmpEZUtjZFRiZ3RMS3hmOFkzVnIxYlpldkY4TU84a0QwVGI1YkZrN2k5YmNpdFVxckwxU081WENEeElIejBTS1Nna1BsczZyZ0hiUlN5dUtSN3I5cVNJcjBwelRkSUpnSTZNZUlNSC1OVXZ5S0c1NHc2Mi1FaHZMS1V4dTZ3VTNZY3cxSk1aekhYVTNZdEFmaFlVakdsOEZUdUxzSUVRVGhtdXNrX3c2ZXhnb203dTR4M0tVWXEwcnA?oc=5) <sub>tiresandparts.net</sub>
- 📰 2026-11-11 [XPeng's European ADAS Ambition Meets Its Operational Test](https://news.google.com/rss/articles/CBMiyAFBVV95cUxQYWF1UzVGNktvcmR2YTNvMzhRSTdqcWg2ZFV2SUN5cFBMbDZPdGd0OF83SmhIUVpsZFlOTmE5MHZnWVZSRlJZOFRpcUVpaV8xdnFWU01EOHlhU3d4c2VDM1Q4dlV4Z0VmZ2pibFhjMFBTVWUzOS1JLVJWNjBsZUdaZU1iTklLaEtxVlNNYVRfOWlURnpLTk9kZ0pzUDhiYmYtbE9rcWxuUEJzQVc4WEl6MHk2MHFaT1B2WEpUSHE2eVJYUDFUdW9PZw?oc=5) <sub>ad-hoc-news.de</sub>
- 📰 2026-11-11 [Middle East weekly: Alibaba Cloud signs Dubai AI deal, Tencent Cloud partners with OmniOps, Aramco acquires 49% stake in Humain, and more](https://news.google.com/rss/articles/CBMi5wFBVV95cUxOeDlrdUc3aEltY1JjWUl6VHBjdDBqOWFZbFRldjZlV2Z2UVdEWFd6bVk0WEdmNnN4cUtOaEEwTDhhUl91OEM1dWgydjlYVFc1NEI3c3BabmpGX25LdnM5aFFLQ3YtZks2QzQ4T0RfV3ZlNWZDVHd4Ui1aUmY0Y05RQUJicEVWOGFPUjlzbUlxeFJYN1FwR1RNdWQwaDJWX05saTlIYnU4MG4yU2czaEZic3JQWkRtV0ZiVHF5YUVYeGJaTE5QN3J1SEMxNlNjblU5c3djMXdjRi1UU3NJY3hicXlNdnZacmc?oc=5) <sub>KrASIA</sub>
- 📰 2026-11-11 [小鹏MONA L03智驾差异：Max蒸馏版与Ultra SE完整版怎么选](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9YX05OLTR4T0JGa1UyY2EtN19GRHhNOXM2dlJGRjBMUHJTRjhIYjFRNkY3a29YTVhqeWxpY0QxT0Nibm0wYnBrN3dhUG40NmJDbVcwdXZsR28xY0E?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Li Auto</b> (121)</summary>

- 📰 2026-11-11 [Li Auto enters the Vietnamese automotive market, unveiling its first four electrified models.](https://news.google.com/rss/articles/CBMiogFBVV95cUxPdUs2QXlkb0VOWjBVOEFpcFlSOTJjUUNuWHZ4TmFZYlRuQ0lPZ1Z4SmFYcE0yWko3U3ltVEluWHR5RlV5UzZuZEZoVEVZNG5QRjhiUkpzaGpQY2FkYVFLQ2hka29tVTFtRmZ5MG9Qd0x4cUhSWkxGY2NObE1GYXFxT0RPVnB4c1dCTEhzUVR1d0NsWUN6azdCb0l4SlRLdDVEb2c?oc=5) <sub>Vietnam.vn</sub>
- 📰 2026-11-11 [新增眼镜指挥泊车/驾驶风格切换 理想推送OTA 8.7.0](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5YSEF6YWhTQndzeHoyMVA1RXhrOVBkd0o0bFdkWC1mZ0hYUldFMkZIMGZSRU5YWjdhYkZIOWpQUzh5VFF4OFBMMjZGV3cwS05NdXc1dURITTh0Y1U?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-10 [Cyan is emerging as a signal for autonomous driving, UDC, OLEDWorks and Audi to evaluate light-blue OLED lighting](https://news.google.com/rss/articles/CBMipgFBVV95cUxQd2pUSDY1Q2xnWWxQYjhaakxyR0JBOXpxSG9qRkdTa3lJczZyNE4tMUt0UjVYUTlNbUlxQ2ZrVVUySnpXdzhwRmk0SlFaMFo3bzJYZUotY2hteEZxdVFDdFdLenZwOUlNRWUtQ1NMNjJobFM4N3NWUDB6ZGZwWl9LamxsbXVJb0g0cHROTldhRlZ0aXhrTkozVHVtVjVlb0EwVXBlZE9R?oc=5) <sub>OLED-Info</sub>
- 📰 2026-11-10 [Li Auto's updated i6 orders estimated above 50,000 as Deutsche Bank sees year-end delivery recovery](https://news.google.com/rss/articles/CBMihwFBVV95cUxQbXpuYThJWERLMlRfUE1oaEZUb2FneVVfNUhtMDVkLVBBSnpHbWk4OG11MEdtT1ZrYW8tVF9pY1FSbzhfZ1FreTROMTJ1MTBoU2F3YU44Ymx4QngwZGFYODE0b3lxZFpNWFhVaHBUSm9DSmJfR2FlOXY3VjhXa1NlZE9abDQ4Yk0?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-10 [China’s Li Auto makes Asia-Pacific push announcing entry into Singapore, Hong Kong, Thailand, Vietnam](https://news.google.com/rss/articles/CBMi1gFBVV95cUxQc2tmb2FhYjN2V1BtSUUwanJHcW96Ny1kRDJHYTBLeDdENDRuVl9USXpTNUR2dnpoU1ZkTTE0RmdrT21YR25MbVE5Nm1jRDdtWjdKMVV3azJxQ0ZwYUwwZGsyRFRmYV82VXpnZ3RLbDJnTVgzblE4OU1oS05qWVJVclFWZ1MxSG9SMFpkUUYzM3pQQmFJMldDb253cEY0RnNzUFVFdmdVc01BU3hYMDhyOWpHcV9USHNrN2JTU1d6aFBDUUx0UFI0TFBzQVZ2SWNXX2tLSzZ3?oc=5) <sub>The Business Times</sub>

</details>

<details><summary><b>NIO</b> (80)</summary>

- 📰 2026-11-11 [Nio ES9 reaches 40,000 deliveries, adding latest 10,000 in 49 days](https://news.google.com/rss/articles/CBMiaEFVX3lxTE1LY19PcV9US3lDcFJfQkRwQ3lzQVB4NVdJT3Eyang0cnRJSXFYbVpIZXNGVmhoYjRCSXpaVW96azJXbG9FWk1MUEV2dWdwRHBmeV9YQkNxOU1UUWtBZzlTb0tTVDVnaloz?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-11 [BYD apologizes to owners, blames supplier coding error for Da Tang wheel rim mix-up](https://news.google.com/rss/articles/CBMifEFVX3lxTE42anM0OWlLQ0Uxc0s2UWtnbnJqcE1xalQ4MzZJNVhrMmNiNDV0M3JzemxmRVdoSFRQOEJMei1hY1hBYWxjeG51a1VnRDJBMC0zb0VqQThuSTRQYUlnVlVyTlBqUnNhVWFmUGdvQnJOV2hTVGJQUnFadVNnOGk?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-11 [Lynk & Co unveils 7-seat 900L SUV, expanding flagship plug-in hybrid lineup](https://news.google.com/rss/articles/CBMickFVX3lxTFA0N19KaDNGSVgxdlk5akFyVGx6enUxcndNNHlFb3VHY3RrNF9OOVhndVhwN29GVDhDYVROVDU2OEtEdjlCODB1OHhBNXhaWHdYS1M2dHJSTEZJZ294aTJ5Z0ZUeVg2SnV5V240S3ZjaW5jUQ?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-11 [【视频】蔚来ES6 2023款 75kWh](https://news.google.com/rss/articles/CBMiW0FVX3lxTFAtNVBxT3ZrSzA5WnBKUlMyWk5CdjVUbF9iNUI0eHRicW9rQS1weW9EdFJGRVRieVM4aFJkNUx0R3JDeDNpWnJxWmtoQkNmYjBSZDBIMG5KRFk5SUU?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-10 [The Subscription Trap: Are Luxury Carmakers Charging Owners Twice?](https://news.google.com/rss/articles/CBMisAFBVV95cUxQN1c4d293VWwzWTdscExVVGdoMVBId2ROS21kdlV2Mkt0ZU9nYnRMenB6UEhIeFJqNFJ3NEZVcW4yR3dDd2NQRW1NOHBpLUx6SlNaQlZWeEpxeGhodW5TWE1iMGpXZVZGR0llYkp4TkJlM1NuQ0VzTkI3RHp3aUY2VmlVQy12bTMyVjBqMjMzQjlQdmFVXzJid2lYb3ZkWnkzYUpRaTVPV29VdU82YmpHQQ?oc=5) <sub>LUXUO</sub>

</details>

<details><summary><b>Huawei</b> (192)</summary>

- 📰 2026-11-11 [AITO M8 Cumulative Deliveries Surpass 190,000 Units 19 Months After Launch](https://news.google.com/rss/articles/CBMizgFBVV95cUxQX1F3WlF6M2NMQy05eDVrLXJWQTVZazgxV1JWU0ZfazhiSjMzdXowVjBmdXV5QVJ6QW9XQ0dxYlU0NEY1RHBmeFBjaXo3OTA0TFVQcndtUnktdU1NR0dGWTdqY0RRTmtNSHVoR29QdFBBR19pUDRnbUZ4SmtIR2dHY2lJcml4ckJ4d2NGZVJzejFYWHJlWUQzbF9FOWFkbHQxTFJRNHVDYUdWMzczQ2NpdjdmMllGWmFXNlVneXhYeF9aZnQ2ZkdNVlJ0cGN4Zw?oc=5) <sub>Gasgoo</sub>
- 📰 2026-11-11 [Nio ES9 reaches 40,000 deliveries, adding latest 10,000 in 49 days](https://news.google.com/rss/articles/CBMiaEFVX3lxTE1LY19PcV9US3lDcFJfQkRwQ3lzQVB4NVdJT3Eyang0cnRJSXFYbVpIZXNGVmhoYjRCSXpaVW96azJXbG9FWk1MUEV2dWdwRHBmeV9YQkNxOU1UUWtBZzlTb0tTVDVnaloz?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-11 [China NEV sales rise 13.1% to record 1.94 million in October, CAAM data shows](https://news.google.com/rss/articles/CBMib0FVX3lxTE81Z2hRNWZRTWw2RlhwdjZsRVJ3aGJhVURyb0tuOU4xS2JiOWFyLWswblMzSUFGTFI2V09tUFpYclNCZ0ljTEt2akxYNjdxZkpPeEhTWGdaOERzeXZQYnNDakptMG9ycEllMW5UQnVZUQ?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-11 [Lynk & Co unveils 7-seat 900L SUV, expanding flagship plug-in hybrid lineup](https://news.google.com/rss/articles/CBMickFVX3lxTFA0N19KaDNGSVgxdlk5akFyVGx6enUxcndNNHlFb3VHY3RrNF9OOVhndVhwN29GVDhDYVROVDU2OEtEdjlCODB1OHhBNXhaWHdYS1M2dHJSTEZJZ294aTJ5Z0ZUeVg2SnV5V240S3ZjaW5jUQ?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-11 [售18.98万深蓝G318四驱畅行乾崑版上市搭华为乾崑智驾/鸿蒙座舱_新车上市](https://news.google.com/rss/articles/CBMibEFVX3lxTE9OV0dvZFFYcTZTREpHc1ZTLThQdG00M2hmZXRpYTRZZzR5enUzZHRUZTRzMDlXTUdiRXRpNXljT1p6VnBFM3F5bF9iUi1mR0pteUZ2S1ZKaVhmOFRjZ2JSTEJYV01IWFRDTHVsTw?oc=5) <sub>中金在线</sub>

</details>

<details><summary><b>Baidu Apollo</b> (34)</summary>

- 📰 2026-11-10 [百度Apollo World首秀，萝卜快跑2.4亿公里全无人](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9IOHlYeHpXSnBsX1RQMFA1ZV9BclR2TXI1WXVXS0FvOVVVRlVTNGUxaVQ3YnY4UWtGa05SZmtHYi1seW10NV9adkRLLW9LZ3lBa2p2M3VRZlVNbGs?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-10 [萝卜快跑28城落地，百度Apollo World定L4仿真标准](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBIX01CdUNMdW8zZG9CWFgzM0RpSWFQQ3FjQjdKazFOQ2R0eXpKRFIwZXdvOHZ3b3VVOEI2WGR5R0tqNWs5MDI4TDJIYUJ4bnJUQUVqTWtUUmFwN00?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-10 [Kakao Mobility, Nvidia form Level 4 autonomous driving alliance; Tesla Cybertruck to be phased out](https://news.google.com/rss/articles/CBMi0AFBVV95cUxQSnM4VW1mOHpXVW0yQ0tEN25KT2RWTVJBZ1JUZ0FYNUcyYWZJRlg3YzF3ME45Yno2dXNPT3dVWnozcERjdnBZLXZ2OTAyVE1TcXFtSEFKYVFnXzV2aFFUak12Y0NWSU9LQVlKMzVUblJsbVljbjc0OFBaVXY2d2diQ2NpRGhFaTJfWDFOVEdpemNCVXBpSzYwWnNxQnRRNHVZc09OTWFTTTRZSTQtUGFFRmlTM0JHMGowNF9vZ1lRcEZ4QUFKbzlsaWdwZUs3SS1n?oc=5) <sub>디지털투데이</sub>
- 📰 2026-11-09 [Weekly Recap: Robotaxi expansion and Lyft Go subscription launch](https://news.google.com/rss/articles/CBMiwwFBVV95cUxPcmd6T05CeEN1eDVfUGtrN0U3c0RXOS1sMUNCNXdvblV6WTVpNGFDTXI4NE9QNm1DWEhZZzlSTTQ0QXVKeElRZVNYcDJuLU51MUVQVFVXTXFhenVseEhoMnE2VnVlMW1ZVWFwNDZuQWJnUk5JM3czejVkYUJ6SllXdi1oVWtXUncxeEpzUllwQ0RheG1PNWM3aDVIWlpLdUs4UXB5d2NyNU1VYnRFVHpWd1FEZW10ZFlRUmdaUVNjU0YwTXc?oc=5) <sub>TradingView</sub>
- 📰 2026-11-09 [China robotaxi services spread but still require long walk to pickup points](https://news.google.com/rss/articles/CBMivgFBVV95cUxQOUpMWFNyUU92N1BuckN4QkRtUDV0MkdRdDUtTWowN3VmVWgxdFNTQ3o2cVFiM2o5T1Joc25sS05OR2xGUWYxT3hIc3NGMDMxWEhha0JxNGNOSUlKZWNjTkJVUlF5enhZRnJNWkdMOHppNWo3SVBNa3FyQUNZY2dzV00wbTRQOWRqdG5RR0hJQkdyMFZOZUtWUEtDTmxQNTI1NktyTkVyM1M0X3NzeU5DWTlPNkpjV0N6VndsNGpn?oc=5) <sub>디지털투데이</sub>

</details>

<details><summary><b>Pony.ai</b> (65)</summary>

- 📰 2026-11-11 [2026 Robotaxi 开始收费运营，国内 L4 自动驾驶玩家进展如何？](https://news.google.com/rss/articles/CBMif0FVX3lxTE5TREtocDVDN05vaEJUTm4tbWRwNXp6d0JjOFJiczAzbXp0UVNva09WVHliR3dVUWdBLUc0bG1mZTROLThybkt2cnRLY19kTEd4aHl6UDUtcmtNUWl6MkI1ZFRyM21VWjNpcTRjS3Z6S21lazZsMVlSeGctNGNLU1E?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-10 [11月10日热门中概股多数下跌 阿里拼多多跌超3% 京东跌超2%](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9BTU1kai0tem9QQjlaUFEwMTlHWHA4ZDNZZXZRQVdNZVNhSWFSdEc3cGFOMU1MYjN4Q2doSjJMaEdMbzRNQmJCaEhGWDEzLVJYamhXRF9MVHdjMU41aHJj?oc=5) <sub>Kuai.Media</sub>
- 📰 2026-11-10 [CDG autonomous vehicle stops in yellow box in Punggol, company adjusting software after incident](https://news.google.com/rss/articles/CBMiwAFBVV95cUxNdFZGdWVlOXcyaEx1Z0JYWnoweXFLbGJjY2dfWEVnWS1Xc2Q0ZU4zaWxCbGVqa01WWTRTRVd5OVNpR2dpR3hSR0FCVHdHR0hEbFpwSjNiTTczZmFNSkx6NFJoRGdWa2prRUhQeEZicnpTN2UxUWxXZGUwaTNGdFpEWG9CNzl2bE9KTV9TYkVxY1RERzlPUnJXSjJPWjlfc0ZVdzBpekdjNzR3WmtoVC1BS0NmQWdrWks0enRUOUJWdjE?oc=5) <sub>Stomp Singapore</sub>
- 📰 2026-11-10 [Aurrigo to Trial Autonomous Shuttle at Portsmouth International Port](https://news.google.com/rss/articles/CBMipAFBVV95cUxOYTJhenVEUHh1eG1zQmdMY0ZMSlhEOS1rU3ZWcnJ0RktiMnJtYmhZdzBpdWUweGRWcVpzRjFfUXc5VFNSYWJMQmNIZE1iRXhaVVczZ3dKa0RlalZwWThlN2QwUEpDR0RyRjZuMFY4WkozbFdnRjM3ZnBDT0s5VGJSYTFtWm5zTHRxcnc0a2ROSFM1R0hUZGRHTms5cVBDOWt4UW5nLQ?oc=5) <sub>Future Transport-News</sub>
- 📰 2026-11-10 [Stellantis Plant Buyer Says It Holds European Automaker’s Letter of Intent](https://news.google.com/rss/articles/CBMitAFBVV95cUxOemJYWU5vXzhrNWVNQ1RnZ0t6WHpEZ0pnRHJHNWFxWENTRFl6VEtCYkFWRkhPNzdDcGR5VC1aR2oycTM0VXRnWWJ1NUhNdHAwVnE2VmFCZFRsQWtzaGtvV0JiMmhUeGUzUFJCY2Y1VUdVTjFOQmZWQ0hpejVSTTNuVEtaX1l1VDFCeFYxc2tvMmJNNDVfeWI5RmRpbFExaGExR3lqcEcxdUJvM3laMEtXd21LbFI?oc=5) <sub>Electric Vehicles</sub>

</details>

<details><summary><b>WeRide</b> (74)</summary>

- 📰 2026-11-11 [2026 Robotaxi 开始收费运营，国内 L4 自动驾驶玩家进展如何？](https://news.google.com/rss/articles/CBMif0FVX3lxTE5TREtocDVDN05vaEJUTm4tbWRwNXp6d0JjOFJiczAzbXp0UVNva09WVHliR3dVUWdBLUc0bG1mZTROLThybkt2cnRLY19kTEd4aHl6UDUtcmtNUWl6MkI1ZFRyM21VWjNpcTRjS3Z6S21lazZsMVlSeGctNGNLU1E?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-10 [Top 8 RoboBus Manufacturers in 2026 for Autonomous Public Transport](https://news.google.com/rss/articles/CBMiwwFBVV95cUxNVUMwY2JCS195TUlGVWJUWWhTeGhHVHRPOXJmRmx3eU5HTzJzNVhZUFhKUnZiZVFvMmdUUmhXT21zQ2tNejlQdnktRGJ4YzBrSDFkeE9zd2VQMkI2RUp2NzZhOXRPWEIwWVNWc2trdEFtaEVJcXJaUUtrYjNxajJlTUY0elV4bEJRNlRxM1E2OEJKeU1DMmV2OTBZd3RROWREYkxjMGxXUGI2ck94R2IyNmJJTXB6ZERfNHZCd3lxU3dyM0k?oc=5) <sub>Akron Beacon Journal</sub>
- 📰 2026-11-10 [把文远知行大模型装进车里，埃安Ray7 11 月 12 日上市\|广汽埃安\|文远知行\|宁德时代\|华为\|曾辉\|埃安Ray7](https://news.google.com/rss/articles/CBMiY0FVX3lxTE5WQlZ3WWxncjhfWHlwd0NrWUpFdVdiUHU0UzlfLXo1dU03NlhPeGxyZEl0anBiXzJjNnoxUmtmSTE3ZjNvYmhOaWh6SlJmRVJ6YjZSVlZkU3dTRGFkQUoySjJOTQ?oc=5) <sub>新浪网</sub>
- 📰 2026-11-10 [广汽埃安 Ray 7 11月12日上市，配华为雷达](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1lcGpmMVNpOXRyOVR6V2Jhdm14NTdQRldNcm9JQjVWa1g3MGVZdV8xZ3hROENBZGhNS25HUmZvRlV5M1k1VF9iWGR2dGVScFFmMkdvQmNEczRadms?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-10 [埃安Ray7配华为激光雷达，续航700km](https://news.google.com/rss/articles/CBMia0FVX3lxTE1SejZqLTNXa1hFeml2R1ZZTWFpYWh6by1zYVY4cWdnZnEtdU5KTUlTOTZEZFhOeC1Hd0FJUGlaZFNrMFJvdVB1aVl5SHllT2Y4amRhR09Uai1GenJNMXhIVzZPX3VKU2NGWVFB?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Horizon Robotics</b> (51)</summary>

- 📰 2026-11-10 [Apple's HALO Ignites Physical AI; Manycore Tech Surges 30% in Afternoon Hong Kong Trading](https://news.google.com/rss/articles/CBMidkFVX3lxTE9kRDdUVnMwSm1KSzFmUzlLVDBTVG1zUHNzaTVRLUdtUmJwTnVHWWFGbjFTazMtSnJVQWtoQVFUMm5MQ3V4dnFkNERfUzVxQjhxalZ4QzVjVTl5bVI5NGlLQmJjd0Y2LTlqRC1xdk5OS2VwQXZCclE?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-10 [网传比亚迪天神之眼C将停产？比亚迪紧急辟谣：均为不实信息！](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1kelpMaG5NWkJpLUZWN3BIOHdqRjIxWWtWZXZnTy1mMTBJVU1CSmRlMERRMld4dVkwR1JyV21GTm5VZUhXUmVZeUJwN0cwQXJENUVBcm5pVXEyN0U?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-10 [大众 ID. 系列双冠王，地平线芯片凭什么拿下销量第一？\|德国大众\|地平线\|HSD 智驾基座大模型\|智驾芯片_新浪新闻](https://news.google.com/rss/articles/CBMiY0FVX3lxTE1DYW9QcXNrRU5Mdm1kcWJUaWNHRGlIRTUtU3dSbC0ybnJwUDkxQTY2M09SNjJtSmUzWHhHNkxyZk5sS0VhU2duR09PU00xb3N2NjlMWjJUYzlTSk1yOXlCWmt6QQ?oc=5) <sub>新浪网</sub>
- 📰 2026-11-09 [英伟达智驾芯片份额从45%跌至30.2%，地平线 华为芯片份额紧追](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1Xa2lvYmRDdVM5alNieHA0OFU2WXZMcUlqaTRCMW53c3FfendtYXVWNm5HLW9FZmRYbjR3a1B4MklUemswU3NLeXJmZnUxblBOa2luOTdMa0w5VEU?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-09 [iCAR V27：不到20万，把“精装”硬派SUV开回家](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBsdkFORkxiNXhUYlhrejBKUVZKZFA1YUVzV2haWm04RFE3emhvRzlkam00clJxZjBxVGxsUmp1RGZjc21ncmZLUC11YnBZdGRYNHROMnlsT01TTlU?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (20)</summary>

- 📰 2026-11-11 [【视频】特斯拉发函，媒体CEO：放马过来#特斯拉#埃安Ray7](https://news.google.com/rss/articles/CBMia0FVX3lxTE5xOHhzcEd1V1RKWmxPZ3BEYUN6NGRhOXB2cHFXSWxFNGEzdjFPbkotY0VMQlpGTGxyV0FCc3p3S1NkU1NjSjI3b01nN2FTcnl3blB4dC00UGlQNlk0Ukp4SEhIYUtSVXNhRlQ4?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-10 [【视频】Model Y L 六座家用｜一副好脚垫能省多少事？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE92blRNM1I5N0tnc3BHSmRid3RwcFIwNnMtYWJwTkcxZ1Z4RDVjTVRzS3hvUm5BMGptOGNSelRBdWM4cW9ZZWtNMHN1Nm9lUkNtdnB1aUtiVkVyREE?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-09 [雨天接娃四车开过，赛那四驱油耗6.1L，两驱版差距在哪？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9EbHdKOVNtb0k5TEhKbkxJSVZFOWxZUXZlS3kwNWtLcTBxcTJmc2RBUEVHTzRzdzBOS3N2Z2JmZnpEZzQxbVlXR3pKeC04YzFhWnRRUGRZOVY2Zm8?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-09 [DFF Partners with DP World for Development of Autonomous Logistics Solutions](https://news.google.com/rss/articles/CBMirwFBVV95cUxNQ0Zpa21lNWZ6bjFZdFdnY2NIWmNuLUJIMTdTZGhtZVBDZzZ4NVRjWGthUnhWSmk2emlDVWdFQXdSYnBkR2NUSkVya0dJTEZyUUltdlBmWkdjUmprZUVYcGpTV0w2cXBVOEhLTTJhNDVYVHlXbklnUEtUbHhLWWRMaFJ5WktuUVA2dkxsamM2Vm9aa1lXaG85dkJJOUh4cHhZMkhkRDdGMlBBdzZOamlF?oc=5) <sub>Future Transport-News</sub>
- 📰 2026-11-09 [【视频】全新腾势Z9GT征战沐尘GT549，易三方降维打击，全场唯一素车漂移](https://news.google.com/rss/articles/CBMia0FVX3lxTFB2VXJBcUdVbW1IdFA1OFpLTkRSUTdSZ1hfSlhZVmdLWmdhQ2ZRR3NoUWgxeW5rdlJPeGZFdlQ5Ri02azBRdmpyUzExZzFmVEEzNG01ZU9aMV9xZHF1aHdLQVZxME5xMHozeEsw?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Mobileye</b> (16)</summary>

- 📰 2026-11-09 [Nvidia Scandal Sparks Auto Industry Watch](https://news.google.com/rss/articles/CBMidEFVX3lxTFBUSkZrRUk0TktpdFF1dEthaHQzMFdVRXQySHRMMXFwT2s2akhzT183RFlib2NuZG9lNkVoUElrOWFmbEx2OUNUY2ZhYlROQWRyZjN1eDFXdk9ObmFYQkdOUzNNM1FCazUwVWJRbWZILThIM1RO?oc=5) <sub>Businesskorea</sub>
- 📰 2026-11-09 [Maxwell AI Cuts Code Costs 67%, Runs 38x Faster [2026]](https://news.google.com/rss/articles/CBMieEFVX3lxTFBlMjEtN1BpMTdFQ1JKOTBKQjBvaFV3V0dISVg4SGtlQS1YczlwRFJsRHFEWTl4eHRiak1wYmVnS1lEMkhGaUpmNks3eUU5ckExSl9DekNyLTNhSHRNcllrSXNSbHFzMFdDUHZPVkljalNlZTV6c0R0UA?oc=5) <sub>shattered.io</sub>
- 📰 2026-11-07 [Mobileye Global (MBLY) Lifts Guidance Following Earnings As Fair Value Debate Returns](https://news.google.com/rss/articles/CBMi0wFBVV95cUxNOF9fMHVEMXdjcUJ1ci1PZ3hqNnV3SHVHanAwSHc4TzJvTnVPSnlxYzRaekFoLUtETWdTeVFVNzNFY2U4SnNxczlUVjF2bEE4WEFPcXdDRjZQWnhKU0J0ekFGS0l2cnlLVmZTN0o4MjFSMUgwOTJ1UkEwQXREdnZXbTM3VmNpNm42YndkTHBGT2prNENPZ1JHTURJRy11a19YRjQyc1B2V0Y4aXBVamRXeFpzamRYWWpWX1c4eXpWYmdiWVIwUVRYck1OUXZjTElGaFM40gHYAUFVX3lxTE5nb2VZYnRkMGY3a1l5UTJTU1ZJUndzc1VjWHpicnNpRm1pdURTMUwzYWJYeVdYRy1kNVh3UjNub19fWm11eTVLSGVUVEJFTlBDcHExWFhBWFdPZDdsY05FRS1kUEtoRi1RVFROcjIzalJmdVA2amlrOG5OSmtlMUJtMlo0S21IUGpaRXE5b1JvV0xCaEo0OGZPaW9UeWQ0bEZ0d0VQU1Y2b2QzQnh2YzVaSTIzVV9pTUJOUy1BM1puZ2N0SUc0SzltUnotUU4ySDlfR2psMm0tSA?oc=5) <sub>Simply Wall St</sub>
- 📰 2026-11-06 [Mois Navon: On Mobileye’s Success, AI Ethics, and the $15.3 Billion Intel Deal](https://news.google.com/rss/articles/CBMivwFBVV95cUxNZWE4YU1udlFHX2tSMHFJWERQME5TMk9FaVBxRUZjbm81MlVjZDU2V25FRS1DVFdWV3lHZ3IzaUJLaHBsZnJHN3pPLUt0QlhzYU5NaXpkZ3ZDZGVEdGJNb2ZjRFV4MUk1bXllek45NVR3NHFITFY5RUZESE1qUWZmbjJsYnE0eVFtWXRYYU1iM2VwTmZoanZPT0doUUxyY2ZpeDAwLXRzTENQRzJKZXJYNDNheVcySGRRQnlDaURHbw?oc=5) <sub>UA.NEWS</sub>
- 📰 2026-11-03 [Elon Musk: Teslas will soon be able to drive themselves coast to coast](https://news.google.com/rss/articles/CBMic0FVX3lxTFA3WXZ0NzdKSEFxdnJJWWdIZ08zMThvN2h1UllLc3p6RlJrTHBfNTFMcmVKYmNMZGdzWG1uY2NqSzNmUXdGVWFsdzM4TXdoaGNRWFNYQWpYcHZ1c0JEdzQ4VnM4YTczYlNWWE9wYnFGRnFLZzQ?oc=5) <sub>Mashable</sub>

</details>

<details><summary><b>Aurora</b> (29)</summary>

- 📰 2026-11-10 [Kearney, MIT put US driverless truck cost parity at 2028](https://news.google.com/rss/articles/CBMihgFBVV95cUxOaUF2Mlg4M01hbDlhZ1EzMkxsNHpyLXExUk5SMzVSaWFYMU9va2EtWm5jeWk3VGV3RWRzekREalZFOXJsajFabHppYmlCZUw4cEZNNndoSGFwQlc5cTFkcEhFMTl1eEtZMjUzQlc3V3Y0OWxlcG5GeEFCZm5Qc3kxdWZ2ay16Zw?oc=5) <sub>FreightWaves</sub>
- 📰 2026-11-09 [Opinion \| Truckers hate these jobs. Let driverless trucks take them.](https://news.google.com/rss/articles/CBMipgFBVV95cUxQM0k0WWkzYlVsOFdpbFNSZmJfenVKeV94ZkFCOHZRZmZhM1JfUlpaVTUwcnVFNDJkMjJBWlhIb0lhdzJsa3Nodnh3N19tVzlRcXFJZFN0ZU5MZmlnV2hYZmZ4RV9BZmVyRE01ZVhydjg0VlZBUkp0NElEM3BGTEhuNXpNa3F3UC1rRkg1R3czdWZQQWFNa2VoWXkzbkhiOFl5RGxUMUt3?oc=5) <sub>The Washington Post</sub>
- 📰 2026-11-09 [Clark: What fleets should know about autonomous trucking](https://news.google.com/rss/articles/CBMi1wFBVV95cUxQRldXemJMcGs5TnpOalV4d1g2aEdDaTN3aGRZS1pQSHJzbFRBY0FOaTV3VHlCMTJZQ1NDZmo3UFpaRjhtSFNKZk9uYk5VN1VUSDlDamFhY19vWktyd2pRVmtuN3lUV2RLRGZINWpLQ05wQXVIZzdGd2JrRGk2NEl3aHNlNGJMWFY5RzNiR25NRkQ1NmVCR2dPNXhDVDVNQTVTeU4tOGlqT2FERXMzdHNudzVNRmd2S3hiNWliRGd6QVJERjB5NWh3dzZKZ3ZKdjdLTTc5alZTUQ?oc=5) <sub>FleetOwner</sub>
- 📰 2026-11-09 [Premium Comment Driverless trucking’s carriers start to sign – next test: which signatures bind](https://news.google.com/rss/articles/CBMiogFBVV95cUxPRnZJU2hDWWxLQkZYeTNKUUxtem9acEsxd1ljZlBFV2dCV1l5NHY5bFBVeFlwNXJHTVlqQWpicGk5c3UwSDVxTUF2ZVhxZGRQSzNsQTdNLWJEWC1KWFFpcG43MDNvX2FaMTFycXRzSmJnMW4zSlA2eWV2YWJqU1FWeTZoWk1fTTA1a21YdDdFblpWUHcyNVdIeUpsRXZjLWhuSnc?oc=5) <sub>The Loadstar</sub>
- 📰 2026-11-08 [Nuvation Bio And 2 Penny Stocks To Watch](https://news.google.com/rss/articles/CBMiygFBVV95cUxPQTRqN0NwOFFPV1dBeUtGSXp6RGtfLS1MQ0l2cWlrd0tDdi0xME1ObzR0ZndYbmUzeERRNExDS3k5WmJVcmNkRnhTMUkxWHJQYU5OSWhMczRsdmZZZVVwZlhocmdFYTlTcWN6NExmaFFPMXJzNnN1ZWVaMnFYb0VnRmdhS0Mta1ktQW0yRXRPUmJIVUtYTjg0elduS1RaMFlpamtqRkZ3YkxWRlZmZHdhRFJrQ1NGYkViYWhrQ2lPLVJIMGYtU0dkR0930gHKAUFVX3lxTE9BNGo3Q3A4UU9XV0F5S0ZJenpEa18tLUxDSXZxaWt3S0N2LTEwTU5vNHRmd1huZTN4RFE0TENLeTlaYlVyY2RGeFMxSTFYclBhTk5JaExzNGx2ZlllVXBmWGhyZ0VhOVNxY3o0TGZoUU8xcnM2c3VlZVoycVhvRWdGZ2FLQy1rWS1BbTJFdE9SYkhVS1hOODR6V25LVFowWWlqa2pGRndiTFZGVmZkd2FEUmtDU0ZiRWJhaGtDaU8tUkgwZi1TR2RHT3c?oc=5) <sub>Simply Wall St</sub>

</details>

<details><summary><b>Zoox</b> (38)</summary>

- 📰 2026-11-10 [Revised DC bill would clear path for driverless taxis, but does it have the votes?](https://news.google.com/rss/articles/CBMiygFBVV95cUxPbENFNTM1MmNYd3JCRnlRVmJ4Nk82bmVGTEgtLVVQYlBvU2lWRXRIS25Bejh0LTExSG84SkRYSWgzUDBsWEY0dmwyTDRvQWVSM2c5THRWUXZuMExIRFBSZ3VyTFRsdlNMc2RvQ2VHS2xyNEFHVTgwTFE4S3J5QzZ6WWxGcUNpNFoxaWhNRTEwLWotWENBd0RrVG81YWhXU2hpUW8tV0xVRFNSU2pIZHVWYzJfTmRYVFRzd0xVREdWZFBkN0MwbW96R3lB0gHSAUFVX3lxTE05QlVWTWhsbHE0YVlONFRWakI3OVY3YnlMdENVOVF0SkdBUmFBREI2YXU1Rk5ySUZvQUVnNzR5NnNkVFA3RmhzekVQR29FaW16UDZYLXBHb21YRmg3WnlOOTFVNVBQaDZPeXRXbDNuYlNHZDRROUgzYWRZQVUyRnZweExLS2xGMG5MNlFrbmNKekNJNWdNTF82SkRiWFlKTlhIWUFLSnJqSE5NVXF3dXBMcnRqVEEyODlKdG96LVRWd0pXZVFkQldfbk4yaXFvTmlVZw?oc=5) <sub>NBC4 Washington</sub>
- 📰 2026-11-10 [Business briefs: TGI Fridays plans return to Las Vegas with five new restaurants](https://news.google.com/rss/articles/CBMilwFBVV95cUxPT2lSNldLdFp0QXdiWHg1akt5cFlwOUFGMTNhV2RtRzJwY1J4OEdVYmJxVFhKVXlUaEpWTGNtRTRBUW5MR3VseHFJR0o5R0FaSURVSUg5TC01Rnl5bTJRZWQ5T2VlMkd0SVVyZVI2RGdPOW1Lb2VDdWhObFZBaWNlY21OQVR3Z3BGYl9MbnVMWEFtNXpnN2lv?oc=5) <sub>Las Vegas Sun</sub>
- 📰 2026-11-10 [Get ready for our 2026 Las Vegas Fan Zone presented by Zoox](https://news.google.com/rss/articles/CBMizAFBVV95cUxOX1lqYVlnZjVHNnFmdTFoMVlldVlucS1EZ2tLYlZKWWhMNTREbnE5eWNyZ0tWUlpxNXFWVmN6Yk55cElLSDJpaEtEeUVzN3FoS0VucVQ2eDJETUpxMEZ1T09RZnFtdzR1UW9NUVhsZGY5c25XaklkN2pjQ1VLVmVtMS0tYWlKS0MzZjdfODRCa3FLOTlLZnd5XzBta21uTl9Fd3JiUFlSQVpBcG9uNmd5VHRqZk9Dal9Zam53ajZnQjAxejRvNnlvQW00RkQ?oc=5) <sub>williamsf1</sub>
- 📰 2026-11-09 [Hope Means Nevada Returns to UNLV With Hope in Action 5K Walk](https://news.google.com/rss/articles/CBMimAFBVV95cUxQZGV1R0Y3Skd0ajhWbmMtQW5YOEdpWUtsYjhkeU5BbTBfdWZ1UTVGSHBJcHI5R1E3djhHaGc4UDk5VTY4SlpreWhvVWNmX0FXNndCeUczcjRrTExlYmc0eXNvRGQ3Qm9mYk1ZekRJUlZDMHlhT3kzYkJQTVdCcWNaQjRtRUROUHFNSzBOSXdUUXBnLXgtSXY3WQ?oc=5) <sub>96.3 KKLZ</sub>
- 📰 2026-11-09 [Vegas Fashion Week Returns for Second Year With Runway Shows Across Las Vegas](https://news.google.com/rss/articles/CBMirgFBVV95cUxPb1J1SVdXTUtIMEp4MVdsZXd0ZE9mZU5ObnNKVFFJaVhrV3VvUVdNdW9PSVR1NUIyVlB2M29tUV9WcDNYNTk3VkpwZ0NCQnFGQkptWFkxbkVPeFkwR0hzNjgxZ3gzODlLQVVrQlNBaGpSeDh1UENZYVpQczhUSUZtdUp3TlFCblItLUYyVzVZbGR3YXVkeWVvWW5XMEhDY0thenNvZkI1WDJSVUk3NFE?oc=5) <sub>96.3 KKLZ</sub>

</details>

<details><summary><b>Motional</b> (16)</summary>

- 📰 2026-11-11 [Korean firms shift CES focus to industrial AI](https://news.google.com/rss/articles/CBMiqgFBVV95cUxQQVpGVm5oN2E0dXpVQ2tfaXVaZXlZanNWcllzRTJCc19OS0F3V2Z1eWEteEpub2dQWWJleEtYMTVyVkRGaVpmWmwwQi12V0JhdjlvRENjU3JWMlpLTkJkOHhMYl9JeDh0RU14Mm5fZmx0X1Z4NlJTYmtKNkc2ck4wT3pQTUZxYjFmQ2M5a1ZoTC1WSmZOOGxMOGJFakVoTm4tcTNaekZZdVFWZ9IBqgFBVV95cUxQQVpGVm5oN2E0dXpVQ2tfaXVaZXlZanNWcllzRTJCc19OS0F3V2Z1eWEteEpub2dQWWJleEtYMTVyVkRGaVpmWmwwQi12V0JhdjlvRENjU3JWMlpLTkJkOHhMYl9JeDh0RU14Mm5fZmx0X1Z4NlJTYmtKNkc2ck4wT3pQTUZxYjFmQ2M5a1ZoTC1WSmZOOGxMOGJFakVoTm4tcTNaekZZdVFWZw?oc=5) <sub>The Korea Times</sub>
- 📰 2026-11-09 [Nvidia Hardware to Run Kakao Mobility’s Own Level 4 Driving AI in Kia Vans](https://news.google.com/rss/articles/CBMiqwFBVV95cUxOdnhiQkNMYk5WWWNtak9OVFdvdjdJYzNQT3htNzc4MjFiemlCRVpSaHJQUHlqd1N3NUVQZ0pESjBHWXZpR3RkdDVqNDhTc3RJd0l1ak96OXRFeEF6T0o4bWdnNHA5dDZjTEhWQjJobWtmY1JXMXItQUdtdUwyeE95WFR2Znk1dGI2eXk4N1hXMmxvVHFxU3J6R1l3Z2hpNEdmSDBTZjl1M05HaGc?oc=5) <sub>Electric Vehicles</sub>
- 📰 2026-11-09 [Jony Ive Shows The Real Process Behind the Ferrari Luce｜Cleo Abram: HUGE Conversations](https://news.google.com/rss/articles/CBMiX0FVX3lxTE42VWFqQXo4YTIwQjRGbk4xZjZ4Rko5MkNmMFZ2OHlEZGZpaURkM2NhLVRNSG02M0NsS3RIaTJ2WHlEVDRKY2U1bFdjZ0NLWjZJblhHVzhuQzdXYzZTeHZz?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-11-08 [Tesla Robotaxi Orlando Field Report｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5ObkNyUS1ncHVCU28ybkRSblpObzVkeGRqaEg3dTRRcWIwTFdCV0tyRnNMeEw3Wk1oRVhZM1g0OW8xSkdxYU5rM2NfLWo0SV9heXRKSnZRd3Nwc3FnRkxZ?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-11-08 [Waymo Just Blew Up Uber’s Robotaxi Growth Story｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBXdmg5SVRYNVVVT0d3Y3o1S1drU3RrT0szWGpoSHZMZzFlb09ZVVNJS2xvY3VDUWoyVW5hZXppeHN5OTRwTTFwZW1BZkdqdy1jX2U0ZUotR1dYaHFCaXhr?oc=5) <sub>finance.biggo.com</sub>

</details>

<details><summary><b>comma.ai</b> (4)</summary>

- 📰 2026-11-06 [Canadian YouTuber Linus Tech Tips Tests Tesla FSD](https://news.google.com/rss/articles/CBMiggFBVV95cUxNZVZaT1Q4X0NlakJzTnFkTGdqTmFPM3pDbFZPUnBYVVNrVzFxMlpZQ3VaTEJFUmJrNVpjMmZ5RVphUDE4WURNT0x4NkhnN01LdTdzSEVnS2NUNkROams2cnNzNkpnalhWcDVuckhETUtxaDZrSHNXTXhKYUlpN2dPTlZn?oc=5) <sub>Drive Tesla Canada</sub>
- 📰 2026-10-29 [We Upgrade Our comma three to a comma four: Is It Worth It?](https://news.google.com/rss/articles/CBMimwFBVV95cUxOVkgtNU9hLXVYM0U2VjNpVldsNFFoQm53SjJGcU1CcnNMWXY5YzFYdVhoYlNZdG5vX21Va2h4b2RLYTNEUTBLdUFhMXd5eTVjLXBSTHE5bFN6elNqa1diTThPQ0Z0Mlo4SldDTzQ4eGxEWl9NTjNKcUNGQmhLeGRSMUxOSElpMkVNOTN4QWhMV0hPRFFJV3cyeVNLSQ?oc=5) <sub>Transport Evolved</sub>
- 📰 2026-10-29 [Aftermarket Self-Driving Devices Face Federal Investigation Following Five Crashes, Three Deaths](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPUG8ycGN4Tl96dk4xZk1yTEJrVkpvVGNsX2JnbWJoeXlzS1ZsVDlEYWk0SnFQQTZXQXpfN21BU20wR1FmR1lsUFpoeHdzU1BUaGdheTZ3LUFkVnpaOHhyWUU0YU1yWERQYmI2TDRnd1VpbTM3Ui1yWFdQVzZIRHVrUEhZUFBKcGpM?oc=5) <sub>AOL.com</sub>
- 📰 2026-10-29 [A $1,000 Device Enables Hands-Free Driving. But Fatal Crashes Have Prompted Scrutiny.](https://news.google.com/rss/articles/CBMixAFBVV95cUxObnRHUXNNS2wxNVFWeHVLdm9qYmZ1bnpaUVN2VWJ1eHZhbFRiWGxoVWxaSjNuNzNKQXZ0RV80dVRnckFGc003eXZJeW5ZWkhUakpsdk9sQ0lnQUZZeVNGekRzYmhvR2RrU1Ric29JeUFmQzNNdEE5NEtZLUgyS2hmQ1hwYWlMdFNDRHNZQVB6dHNqUjIyaXpRMFd2c0YxN0c3Vk9yZF9kR255QmtTUlRiaEtYbDY1dHVZQm9ReHY5WUdMSzJQ?oc=5) <sub>WSJ</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
