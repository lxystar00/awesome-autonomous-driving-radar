# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-11-04 · 1,285 papers tracked · 44 curated.

**Selection rule.** A paper is listed only if it (1) is primarily about autonomous driving,
(2) has public code, and (3) shows at least one strong signal: accepted at a top venue
(CVPR / ICCV / ECCV / NeurIPS / ICLR / ICML / CoRL / RSS / TPAMI, or ICRA / IROS / AAAI / RA-L),
≥200 GitHub stars, ≥3 citations / month, or a well-known lab with traction. Papers are then ranked by a
composite score (venue, stars, citation velocity, LLM rubric for novelty / rigor / impact, SOTA claims)
with a per-topic cap. See [`scripts/rank.py`](scripts/rank.py).

📅 [Daily digests](daily/) · 🗓️ [Weekly digests](weekly/) · 📦 [Raw data](data/)

## Contents

- [VLA / VLM for Driving](#vla--vlm-for-driving) (11)
- [World Models & Generative Simulation](#world-models--generative-simulation) (5)
- [End-to-End Driving & Planning](#end-to-end-driving--planning) (10)
- [3DGS / NeRF Reconstruction & Sensor Sim](#3dgs--nerf-reconstruction--sensor-sim) (5)
- [Perception: BEV, Occupancy, 3D Detection, Mapping](#perception-bev-occupancy-3d-detection-mapping) (8)
- [Motion Prediction & Behavior Modeling](#motion-prediction--behavior-modeling) (1)
- [Datasets & Benchmarks](#datasets--benchmarks) (1)
- [Safety, Robustness & Evaluation](#safety-robustness--evaluation) (3)
- [Industry Tracker](#-industry-tracker)

## VLA / VLM for Driving

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Teaching Vision-Language-Action Models What to See and Where to Look](https://arxiv.org/abs/2607.01658)<br><sub>Yuguang Yang, Canyu Chen, Zhewen Tan et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 36](https://github.com/ShivaTeam/DriveTeach-VLA) | Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving |
| [DeepSight: Long-Horizon World Modeling via Latent States Prediction for End-to-End Autonomous Driving](https://arxiv.org/abs/2605.10564)<br><sub>Lingjun Zhang, Changjie Wu, Linzhe Shi et al.</sub> | ICML 2026<br>2026-05<br>📑 3 | [⭐ 31](https://github.com/hotdogcheesewhite/DeepSight) | End-to-end autonomous driving systems are increasingly integrating Vision-Language Model (VLM) architectures, incorporating text reasoning or visual reasoning to enhance the robustness and accuracy of driving decisions |
| [SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving](https://arxiv.org/abs/2610.20609)<br><sub>Shaoyuan Xie, Zihan Zhang, Jingxuan Wang et al.</sub> | CoRL 2026<br>2026-10 | [⭐ 32](https://github.com/ASGuard-UCI/safedrive-vla) | Vision-Language-Action (VLA) models are gaining attention in autonomous driving, inheriting commonsense priors from large language models (LLMs) and widening the navigation interface from a fixed command set to free-form… |
| [Scene-Adaptive VLA: Efficient Autonomous Driving via Dynamic Layer Routing](https://arxiv.org/abs/2610.24590)<br><sub>Yujia Yang, Quan Yuan, Jiawei Fan et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 4](https://github.com/yang-luvu/Scene-Adaptive-VLA) | Vision-Language-Action (VLA) models offer a promising paradigm for autonomous driving |
| [CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving](https://arxiv.org/abs/2607.04179)<br><sub>Zhaohong Liu, Hao Ye, Xianlin Zhang et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 1](https://github.com/MICLAB-BUPT/CritiqueDriveVLM) | End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving |
| [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)<br><sub>Nan Yang, Zhanwen Liu, Linfeng Zhang et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 11](https://github.com/Zizzzzzzz/MVPruner) | Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings |
| [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)<br><sub>Yuan Gao, Wenting Miao, Mattia Piccinini et al.</sub> | IROS<br>2026-07<br>📑 1 | [⭐ 29](https://github.com/TUM-AVS/Chat2scenic) | Validating autonomous driving systems requires diverse, regulation-compliant test scenarios |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 13 | [⭐ 539](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
| [GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives](https://arxiv.org/abs/2609.39601)<br><sub>Qize Yu, Lianrui Fan, Boyu Chen et al.</sub> | arXiv<br>2026-09<br>📑 2 | [⭐ 291](https://github.com/groundingpi/GroundingPI) | Precise grounding matters |
| [GRAVA: Grounded Reasoning-to-Action Representation and Learning for Autonomous Driving](https://arxiv.org/abs/2609.15169)<br><sub>Xiao Liu, Haoyu Li, Jianghao Leng et al.</sub> | arXiv<br>2026-09 | [⭐ 491](https://github.com/AhernResearch/grava) | Driving vision-language-action (VLA) models increasingly reason before acting, but their intermediate reasoning is often weakly grounded in physical scene evidence and loosely connected to executable behavior |
| [Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air](https://arxiv.org/abs/2605.31066)<br><sub>Tianle Zeng, Yanci Wen, Xueang Yu et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 1,125](https://github.com/louiszengCN/CarlaAir) | Recent aerial vision-language-action (VLA) models show promising single-UAV capabilities, such as tracking moving objects and navigating to language-specified landmarks |

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
| [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](https://arxiv.org/abs/2609.26792)<br><sub>Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.</sub> | CoRL 2026<br>2026-09<br>📑 1 | [⭐ 14](https://github.com/VAIL-UCLA/DreamStream) | Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions |
| [DriveMLP: When Training Strategy Outperforms Model Complexity in Autonomous Driving](https://arxiv.org/abs/2610.29676)<br><sub>Alessandro Canevaro, Julian Schmidt, Hang Yu et al.</sub> | CoRL<br>2026-10 | [⭐ 6](https://github.com/alessandro-canevaro/DriveMLP) | Learning motion planning policies that remain reliable under closed-loop execution is a central challenge in Autonomous Driving (AD) |
| [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)<br><sub>Shen Zheng, Anurag Ghosh, Gaurav Parmar et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 32](https://github.com/ShenZheng2000/WarpI2I) | Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs) |
| [G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance](https://arxiv.org/abs/2606.26017)<br><sub>Hang Yu, Ye Jin, Alessandro Canevaro et al.</sub> | IROS 2026<br>2026-06<br>📑 6 | [⭐ 7](https://github.com/HangYuu/G2DP) | In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors |
| [SimWAM: A Simple World Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.07468)<br><sub>Zongchuang Zhao, Xin Zhou, Tianyang Xu et al.</sub> | arXiv<br>2026-08<br>📑 11 | [⭐ 205](https://github.com/H-EmbodVis/SimWAM) | In autonomous driving, World-Action Models (WAMs) have improved end-to-end planning by transferring video dynamics priors to action prediction, but many still couple planning with future-video generation at inference, in… |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 18 | [⭐ 357](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
| [Latent-Centroid Steering: Single-Pass Classifier-Free Guidance for Command-Aligned Autonomous Driving](https://arxiv.org/abs/2608.00237)<br><sub>Meibo Hu, Jiamian Wang, Pichao Wang et al.</sub> | IROS 2026<br>2026-08 | [⭐ 2](https://github.com/codingmlinprocess/LCS) | Vision-language models (VLMs) have recently emerged as a promising paradigm for end-to-end autonomous driving, enabling agents to map multimodal inputs and high-level navigation instructions directly to executable trajec… |
| [HEAT: Heterogeneous End-to-End Autonomous Driving via Trajectory-Guided World Models](https://arxiv.org/abs/2605.19631)<br><sub>Hoonhee Cho, Giwon Lee, Jae-Young Kang et al.</sub> | RA-L 2026<br>2026-05<br>📑 2 | [⭐ 0](https://github.com/heat2026/heat2026.github.io) | End-to-end autonomous driving has emerged as a compelling alternative to traditional modular pipelines by directly mapping raw sensor data to driving actions |
| [STAGE: STyle-controllable Action GEneration for personalized autonomous driving](https://arxiv.org/abs/2607.29517)<br><sub>Zihao Liu, Xing Liu, Yizhai Zhang et al.</sub> | RA-L<br>2026-07<br>📑 1 | [⭐ 5](https://github.com/CarlDegio/STAGE) | Driving style refers to the behavioral preferences that drivers maintain during driving, shaped by their diverse experiences, habits, and needs, and is typically reflected in varying levels of aggressiveness |
| [A Survey on End-to-End Autonomous Driving Training from the Perspectives of Data, Strategy, and Platform](https://arxiv.org/abs/2610.00926)<br><sub>Chengkai Xu, Yiming Cui, Jiaqi Liu et al.</sub> | arXiv<br>2026-10<br>📑 5 | [⭐ 109](https://github.com/Jiaaqiliu/Awesome-Training-Ecosystem-for-E2E-AD) | Autonomous driving is a cornerstone technology for the future of intelligent transportation, where end-to-end learning has emerged as a transformative paradigm that directly maps multimodal sensory inputs to driving acti… |

## 3DGS / NeRF Reconstruction & Sensor Sim

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DriveWeaver: Point-Conditioned Video Inpainting for Controllable Vehicle Insertion in Autonomous Driving Simulation](https://arxiv.org/abs/2606.31918)<br><sub>Junzhe Jiang, Zipei Ma, Zijie Pan et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 17](https://github.com/LogosIntelligenceLab/DriveWeaver) | A pivotal step in autonomous driving simulation involves inserting foreground vehicles with predefined trajectories into simulated scenes |
| [MCSplat: Multi-View Photometric and Geometric Consistent Feed-Forward Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2610.25345)<br><sub>Yifei Wang, Wei Tian, Wenhua Bao et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 11](https://github.com/yfwang0824/MCSplat) | Driving-scene reconstruction via feed-forward Gaussian splatting from sparse multi-view images remains challenging due to two factors |
| [Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796)<br><sub>Leshu Li, Jie Peng, Yang Zhao</sub> | ICRA<br>2026-06 | [⭐ 15](https://github.com/UMN-ZhaoLab/Pocket-SLAM) | 3D Gaussian Splatting (3DGS) has garnered significant attention in Simultaneous Localization and Mapping (SLAM) due to its advances in capturing fine-grained geometry features and synthesizing novel views |
| [NIDAR: NIR-Guided Intrinsic Decomposition for Scalable Scene-Agnostic LiDAR Intensity Reconstruction](https://arxiv.org/abs/2609.36878)<br><sub>Junjie Zhang, Jie Yin, Kefei Qian et al.</sub> | IROS 2026<br>2026-09 | [⭐ 24](https://github.com/Zjj587/NIDAR) | LiDAR return intensity provides complementary surface-response cues for robotic perception and state estimation, yet many simulation pipelines omit it or reproduce it using reconstruction methods that require real intens… |
| [MM-TRELLIS: Point-Cloud Guided Multi-Modal 3D Vehicle Generation in Autonomous Driving](https://arxiv.org/abs/2606.24301)<br><sub>Hongli Xiao, Youjian Zhang, Yucai Bai et al.</sub> | ICRA 2026<br>2026-06 | [⭐ 10](https://github.com/HongliXiao/MM-TRELLIS) | Recovering realistic 3D vehicle models from autonomous driving scenes is crucial for synthesizing training data and building simulation environment |

## Perception: BEV, Occupancy, 3D Detection, Mapping

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Deformable Gaussian Occupancy: Decoupling Rigid and Nonrigid Motion with Factorized Distillation](https://arxiv.org/abs/2605.28587)<br><sub>Yang Gao, Wuyang Li, Po-Chien Luan et al.</sub> | CVPR 2026<br>2026-05<br>📑 2 | [⭐ 22](https://github.com/vita-epfl/DeGO) | Understanding dynamic 3D environments is essential for safe autonomous driving, particularly when reasoning about human-centric, nonrigid agents |
| [Horizon3D: Sparse Radar-Camera Fusion for Long-Range 3D Perception in Autonomous Driving](https://arxiv.org/abs/2606.31096)<br><sub>Geonho Bang, Geunju Baek, Dongyoung Lee et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 25](https://github.com/geonhobang/Horizon3D) | Long-range 3D object detection is critical for safe autonomous driving at highway speeds, yet existing radar-camera fusion methods remain limited at extended ranges |
| [Explainability-Aware Frustum Attack: Exposing Structural Vulnerabilities in LiDAR-Based 3D Object Detectors](https://arxiv.org/abs/2606.29963)<br><sub>Chengzeng You, Binbin Xu, Soteris Demetriou</sub> | ECCV<br>2026-06 | [⭐ 2](https://github.com/SecMindLab/Saliency_LiDAR) | The structural vulnerabilities of point cloud-based 3D object detectors remain poorly understood |
| [PointLAM: Local Attentive Mamba for Efficient Point-based 3D Object Detection](https://arxiv.org/abs/2609.21780)<br><sub>Xuanming Shang, Weijia Zhang, Chao Ma</sub> | ECCV 2026<br>2026-09 | [⭐ 5](https://github.com/PointLAM/PointLAM) | 3D object detection from LiDAR point clouds faces a fundamental dilemma: voxel-based methods achieve efficiency at the cost of geometric quantization, while point-based methods preserve fidelity but suffer from prohibiti… |
| [UniD-Shift: Towards Unified Semantic Segmentation via Interpretable Share-Private Multimodal Decomposition](https://arxiv.org/abs/2605.07356)<br><sub>Shuai Zhang, Zhecheng Shi, Zhuxiao Li et al.</sub> | CVPR 2026<br>2026-05 | [⭐ 5](https://github.com/shuaizhang69/UniD-Shift) | Semantic segmentation of large-scale 3D point clouds is crucial for applications such as autonomous driving and urban digital twins |
| [PriorMaskMap: Robust Online Vectorized Map Construction with Biased Priors](https://arxiv.org/abs/2610.39283)<br><sub>Haoming Xu, Wei Li, Yu Hu</sub> | ECCV 2026<br>2026-10 | [⭐ 1](https://github.com/healenrens/PriorMaskMap) | Online vectorized map construction provides autonomous vehicles with essential, real-time semantic and geometric scene understanding |
| [Vernata: Self-Supervised Learning of LiDAR Point Representations](https://arxiv.org/abs/2608.06919)<br><sub>Oliver Lemke, Alexander Liniger, Abel Gawel et al.</sub> | IROS 2026<br>2026-08 | [⭐ 22](https://github.com/rai-opensource/vernata) | LiDAR serves as a primary sensing modality for robots operating in outdoor environments |
| [Towards Compact Autonomous Driving Perception with Balanced Learning and Multi-sensor Fusion](https://arxiv.org/abs/2606.02979)<br><sub>Oskar Natan, Jun Miura</sub> | arXiv<br>2026-06<br>📑 46 | [⭐ 9](https://github.com/oskarnatan/compact-perception) | We present a novel compact deep multi-task learning model to handle various autonomous driving perception tasks in one forward pass |

## Motion Prediction & Behavior Modeling

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Flow-ERD: Agent-type Aware Flow Matching With Entropy-Regularized Distillation for Diverse Traffic Simulation](https://arxiv.org/abs/2607.06957)<br><sub>Seulbin Hwang, Kiyoung Om, Dae Jung Kim et al.</sub> | RA-L<br>2026-07 | [⭐ 0](https://github.com/seulbinHwang/flow-erd-project-page) | Realistic and diverse traffic simulation is essential to autonomous driving development |

## Datasets & Benchmarks

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [123D: Unifying Multi-Modal Autonomous Driving Data at Scale](https://arxiv.org/abs/2605.08084)<br><sub>Daniel Dauner, Valentin Charraut, Bastian Berle et al.</sub> | arXiv<br>2026-05<br>📑 4 | [⭐ 405](https://github.com/kesai-labs/py123d) | The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics |

## Safety, Robustness & Evaluation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [CCFM: Collision-Constrained Flow Matching for Safety-Critical Scenario Generation](https://arxiv.org/abs/2607.04451)<br><sub>Ke Li, Kaidi Liang, Yuxin Ding et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 3](https://github.com/KELISBU/CCFM) | Evaluation of autonomous vehicle (AV) planners in safety-critical closed-loop simulation is essential for real-world deployment |
| [Lipschitz Optimization for Formal Verification of Homographies](https://arxiv.org/abs/2605.23203)<br><sub>Jean-Guillaume Durand, Panagiotis Kouvaros, Maxime Gariel et al.</sub> | CVPR 2026<br>2026-05 | [⭐ 2](https://github.com/jeangud/homography-verification) | The adoption of vision neural networks in regulated industries requires formal robustness guarantees, especially in safety-critical domains such as healthcare, autonomous vehicles, and aerospace |
| [CADET: A Modular Platform for Evaluating Distributed Cooperative Autonomy in Connected Autonomous Vehicles](https://arxiv.org/abs/2606.04072)<br><sub>Pragya Sharma, Brian Wang, Mani Srivastava</sub> | ICRA 2026<br>2026-06<br>📑 1 | [⭐ 0](https://github.com/nesl/cadet) | Deep learning models are increasingly central to autonomous vehicle (AV) pipelines, yet their integration has traditionally followed a monolithic design where perception, planning, and control execute on a single onboard… |

## 🏢 Industry Tracker

Latest 14 days of news, official blog posts and new open-source repos from tracked companies. Full daily feed in [`daily/`](daily/).

<details><summary><b>Waymo</b> (188)</summary>

- 📝 2026-10-30 [Toyota and Waymo Advance Autonomous Driving Collaboration for Safer Streets and Freedom of Movement for All](https://waymo.com/blog/2026/10/toyota-bz4x-partnership) <sub>official blog</sub>
- 📰 2026-11-04 [Waymo: No ‘imminent plans’ to grow its San Antonio service area](https://news.google.com/rss/articles/CBMijwFBVV95cUxPQW9GRlBEUjJzMVh6aVlwcWVneklfQ08tbm8xQkw4QkxIYXg5WDZ6Vk9ZZmFBbm1QZ05fUVlsNU1TUDlKV2QteS1zWmNGdG5CVmtmNFZrWjFFXzY1Q09pQW92M21XQTFFVDhzcW5ZVjVLb0dnV0xmWTVlOUpfYmYzekhGX2dZaWVKM3Vpd0xPdw?oc=5) <sub>San Antonio Express-News</sub>
- 📰 2026-11-04 ["Not Ready To Be Uploaded Yet": Woman's Waymo Ride Takes a Frightening Turn in San Francisco, Leaving Her Questioning Self-Driving Cars](https://news.google.com/rss/articles/CBMinAFBVV95cUxOU2dRRHB3Smctb1MtblY5d1JfNnlWYVlUZy1NN1VxNzlyVmQ2TDJoQmZ3Q0tubGxyWlJqbjN0TUw2QkZHSG16dUxRb3p6bjJSN1JsLWVXWmZZOFZNUk0wUy1hLWN3YkZCT2Q0STVEWS05TW9EeTFURlhGb0RBTlFjQm5BeXlkVkFCcWJnREdhUGx3X1NSRlNFcWtJejg?oc=5) <sub>Yahoo Autos</sub>
- 📰 2026-11-04 [Toyota joins the autonomous party with plans to build fully self-driving cars starting in 2027](https://news.google.com/rss/articles/CBMijAFBVV95cUxOcjRoaDBvUmZ1TkFfNDFxWU1MX2FTdER3M3c4RTNUOUhxTy1yb09aQXRtUVdyRTFGOF91cEY2QlRtZ2dzSjBFOVBlZFJyNFFmSDFnNGF4SFBJZGxxM2NaNzBHTkxDTGxBOURVWHpMaUZVZ2VLampma1VfODVJTUtwVU4yYzBBMEZYRTlkSg?oc=5) <sub>WhichCar</sub>
- 📰 2026-11-04 [Early Uber Investor: Tesla and Uber Will “Split 80%” of the Robotaxi Market](https://news.google.com/rss/articles/CBMingFBVV95cUxNRTg4dzAxcDVPMmw5VWRWZFBMZFB3eGtJR3RKcll3dklRdlJnOEM0VFctZGxNZGRCTWJ1MkdkSXNzbnFmWmJ5bUJhUlh4Rk1BYmZjOUs5T3N4Sl9hSlNOaE1oME5YQVo2NWtWMXJoMS1YUUc1ZWhiZ0ZUUm9FbmZPTXJyM1dkSXQtNVlUb2NFM2E5eW9GWmJ6dDFmZWo1dw?oc=5) <sub>TIKR.com</sub>

</details>

<details><summary><b>Tesla</b> (313)</summary>

- 📰 2026-11-04 [EXCLUSIVE: Tesla misled South Korean customers about automated-driving tech, consumer group alleges](https://news.google.com/rss/articles/CBMi3gFBVV95cUxPaHFtVW90SEVfXzZpTkdUYVU0WENhU1BnZ3I4QW1sUUJjcGxqVHlpZzA4ODAyRF9LUmdRbnpCSjRPdUd2YjVTaktzZnJHeWx4WWxNMDhnaWVoS3c3djAyeEpMUWlaVVZwVE5BYUxnemhmbXlSRzBWdU41c0lRMGQwclZIbTVITE1iQWVhbzNsdjFySF9raFl0aDNHV0JLRjBqMU8xNmxBVmUxNUVpck1XcUlITmNqUFRMUWhHOEJmUzc1cTVMbUxjbVM2c2J0TGRHVG5PV1JNc2ZRSU5OV3c?oc=5) <sub>Reuters</sub>
- 📰 2026-11-04 [Tesla FSD Reacts to a Surprise Swerve — Caught on Video](https://news.google.com/rss/articles/CBMikgFBVV95cUxNX3UwWVFQQWxOOUlFNFFjUHY2d3F0aG84N09rQlhsLWRScEIyeTkzdHJHajl2NmVCZDlxNHV6OVIzUDFzQnY3a2ZOdmk4elpXRkR3Y2tUXzJUMXJnVjJ4S1EwelJlXzdSZ2pqaGdoOUZIT09TR2hhZjdtYXRQU2hDbVRGWkdNajhvQnNsUVVUeUdEQQ?oc=5) <sub>BASENOR - Tesla Accessories</sub>
- 📰 2026-11-04 [Tesla misled South Korean buyers over Full Self-Driving, consumer group alleges](https://news.google.com/rss/articles/CBMisgFBVV95cUxOcnBFYXlTMy1GMjRLa0JPYXJrUFRrdjFYaUphZG4zQWtDU3RjQ2x0eHVqbXBpZFFvSDJBV290Y2MtbkVPRy1GQTVmaFBGaDlsMEk4Uk5rS0pMYm1JbC1kWERaSlROUHhIMnlic0tseW5GTDBNUENMNnJ0TUJuZkVDUFFrZnNRM2hmUG1STFViUi0zVUh2cFJaZ1JwRDhYM0ZFV0paT1ZYZ1ZHUi1ISWhNRXhB?oc=5) <sub>investingLive</sub>
- 📰 2026-11-04 [Tesla’s cheapest Model 3 tested with FSD Supervised on Australian roads](https://news.google.com/rss/articles/CBMipgFBVV95cUxPRVd3Zk5lenJHM1dkY04ySG9SLTROM3l2RGNJb28wbk5iYXI4SkRyVGwtaTV0dXgtN2VEMy1QYlFVRkFMczZWd2plQkNCVFExOHViY1diOTF3ckI1V29MbGQ4ZVNULWttQ0E0R2dmZHB2ZXFzM2NUYWZyYjBhNWhmZ0h5ZjROT05pdUpMM09ETzRBVVBiU2U5TnFHc1hSekdNMzZjM3ZB?oc=5) <sub>The Driven</sub>
- 📰 2026-11-04 [Nico Rosberg knows a thing or two about driving. He's an F1 WORLD CHAMPION. And Tesla FSD just won him over. After a week driving around San Francisco in a Cybertruck with FSD Supervised, he called it LIFE-CHANGING. He got time back between me](https://news.google.com/rss/articles/CBMibEFVX3lxTE9sVFdZdWQxdk5WNFh2ZzcwUTFzczNjTW9mWldxaEJTLXhsUXJmSGZOMDlFMGJHakhQbzVxOTdFc1NvZk9ic2Z4eml5dHRhTGdOcElGOWZiMWhlcllaODF4RGUxSVlJYURERS1SZw?oc=5) <sub>X</sub>

</details>

<details><summary><b>NVIDIA</b> (178)</summary>

- 💻 2026-11-02 [NVIDIA/nvperf-core — Core NVIDIA Nsight Perf SDK APIs and libraries for collecting and analyzing GPU performance data directly from application code.](https://github.com/NVIDIA/nvperf-core) <sub>GitHub</sub>
- 📰 2026-11-04 [Volvo, Nvidia Expand Self-Driving Alliance Toward 'Eyes-Off' Driving With Next-Gen AI Chips](https://news.google.com/rss/articles/CBMidkFVX3lxTE1JSVB6QTZfOHhoU0U5RWNOcjEyaFVCSmdtVFJYcmZMYk5lb1QyeGM0X2EwSHkySExteTFoSjlOYmg1NVM5a0VRcU44bTlybFl4LXVlY3RhTU1jZlR6S2stSzdCYzNRckFXY3lpUGdOX2tlejkzUGc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-04 [Volvo Cars and NVIDIA Expand Autonomous Driving Partnership, Plan Phased Rollout of “Mind-Off” Technology](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1kT3VXRG1pR2U1Z194dWthbGFDMzhBTmdZaXIwWmNpeThZQ21sS0pCRkNVNjdoclAyc3U1dE16MEJCWEdIRW8zcjJXMEhXQTFQV2s0?oc=5) <sub>매일경제</sub>
- 📰 2026-11-03 [PATEO Advances In-Vehicle AI with NVIDIA Nemotron and ByteDance Doubao on its AI Box built on NVIDIA DRIVE AGX Thor](https://news.google.com/rss/articles/CBMitAJBVV95cUxONGZlRHNVWno1YW42MXM5SExyM3VxdUhONS1MbDFfOHQwbFlLejlsaVNzeDVOaThXTFA5LVV6QlhoNkx5MlBDNGNaVVE0LTYwMW0tTHhmSTc2dlA4T2Q1aURrZ2V4UTdsVjBVYndlbHp5b3pMVjVJY2F2dEF0djl1RHUtdE1kSExRQVRWYkkyVVIxbXF2RlhTUGdVOTgxY1Nyc0gxVmR3UXVDdU9NREVpa0xFUk9aa3d1ZGhzLTc3eUpiNlJOMTdvYXQyenBmaG5YWGswR2RQcjVmZ3NrQ3pVd04xcnM4NlJLa20tTGpvc0RnN1YycFcxSVdoMzJyUmYwWTZwd2twRzg0QzJ5YmR0Z2w4aC1kejMwcjNaYjF3b0JZX2pib09PSmsxN1pYMTRvc1pnMw?oc=5) <sub>The Conway Daily Sun</sub>
- 📰 2026-11-03 [Pateo AI Box runs Nvidia and ByteDance models in the car](https://news.google.com/rss/articles/CBMimgFBVV95cUxQekRuSUo2dU5hUEpTMjN4cG9uTzJTZ1kzSnBUN1J4MDE2WjlXeklYdV9jZUg4N3RhZkJMenB6WkdqUGt4cU56MDVxeEdkSXlCWmZ3X0s3ZW1NMjBJbkozZlFEZUlWLVBySEhWWXpMd1NTNmFPS3k3SElDcmdxMkJDOHdkUU1wbXFTVW9JRUpXMTNlY01tNzZ1MTln?oc=5) <sub>Automotive World</sub>

</details>

<details><summary><b>Wayve</b> (49)</summary>

- 📰 2026-11-03 [ARAPL Subsidiary Humro Secures US Department Of War Approval For Autonomous Industrial Vehicles](https://news.google.com/rss/articles/CBMi1AFBVV95cUxOSHJ3VzZHdUlQZEdVVmtzVy1aS2NCNDl2azNKd192Q1MwNWkxVHA5bEo5S1pBdkpMVjItN2NPZUxpNktzOS1tSE5iOExCMDhuYmJoUEhjUkY4Rk9oS01kUDduZGFoM2RIaXVYMTVBeDJVc0U4cVNieEIxNFZGN2s0REtFcGV2TzJmWnI3Z092NG5UN1Vab0xLeDhhNXlzUVQwaXFPamtITjVYSXZxbHFrTFFVbnJ1VmdZd1BjZUtiMHE2cENOSUdJcEhkZmZGVlJ4SjRtYg?oc=5) <sub>Motoring Trends</sub>
- 📰 2026-11-03 [Half would ride robotaxi with no controls, Startline Motor Finance finds](https://news.google.com/rss/articles/CBMiwgFBVV95cUxNN1NjdlFYZV9kbmlwZFhPM1BjcVdmbmFCQUtWYWtibU4xSHF2N1pyeVprWVF5N0k0ODJyMXNSZi1nZlp3WWNWeVZiWHU3MVRXUnJkSUtOWnczNXVIcXVOQWdTSEkzYXVrSVN4UF9mc09oc2o4UzVDM0lIVlphWEx3ZVg2RVhHSF9NSHlFVjN1LU0wSEJHSGVhTFhIOXN6clNocFRSUC1DU2hhbnFQVWY0VDhud3FzSGxVTFNlV0dDQ2Y3QQ?oc=5) <sub>Motor Trade News</sub>
- 📰 2026-11-02 [BMW to expand partially automated driving to cities from 2027](https://news.google.com/rss/articles/CBMitAFBVV95cUxNazR3SVVYd2hBNDVOSTJ2Q2FmX3hyOVRnaTV2MXk3UkluSDZ1V0JYU3d5cVBxejVfV0xIdWVoNm9IME51TkFHbW1uWklfZjFJY2QyMG9rMFVmUElfUWg1VVRraGFEajI4ZjZ5cmtVQXg2SVlNbWxzS1cwaDk2c1pTWjhVazBDVkRxdmJFRVcxdGViNzJjaDZkSWRiREh3Z09SU3REU194Uy1jSFNKSTR0eUdGdlE?oc=5) <sub>Motor Trade News</sub>
- 📰 2026-11-02 [UK Urged To Address Jobs And Resilience As London Robotaxi Trials Expand](https://news.google.com/rss/articles/CBMimAFBVV95cUxPb0hzWFlKREtLd1BMeDNnZUo0b0ZGckpqMDUydUlSSG9VTzM4QUhsaVFMeDAwcmhpWlZzeVU5ZlEtTkJDaXhrWDI0WkFwRW1rN2VCM3FOLWtoWjloV09Zcm81TnpQX3Jxek43TmxtQWl4WWN6bkdxQ3NPQkQ4QWF2aUxOaG9WSGIxdGRDTEVTUGdqNm9mZ3VJZA?oc=5) <sub>Dataconomy</sub>
- 📰 2026-11-02 [Britain's driverless dream hits a roundabout of awkward questions](https://news.google.com/rss/articles/CBMivgFBVV95cUxNMWhvU0llampvVWtuR0ZESjlkX1hKNWM1ZEppX3g3dXRFY1hGU2hZaEJOQzFDTmJyVjRxM2dkenAzdjJIVjFWMmhydUJFcnJVMHd1VmNmT09tZnhSRXIwZ2dqOWNsVzFHNkpGMGxhaW03QnI4R2VNWWNxSDZBNmJ3VTNmakZGUW85R2tiUVoxcHpqaEVMZEFQUXRaTEZOejJkckgwS2hTQl9wR3hHemgzaFBpdkh3dUxyQkFicFBR?oc=5) <sub>The Register</sub>

</details>

<details><summary><b>Momenta</b> (96)</summary>

- 📰 2026-11-04 [Stellantis与东风深化合作，标致Jeep将搭载Momenta智驾](https://news.google.com/rss/articles/CBMia0FVX3lxTFAyMjdTOEd5c0JCXzBmWGtZREdaMFlzX29sZ0l1SkpPLTJ5MXh5a3dmQ1lrUllvbjZJekVBaU9LWVVtM1Ntdnlqa3ZTY2hrcjgyUEVTaUZCb2ZUalJNQ3NmdjZLeGtiWDF4MWpB?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-04 [25万级大五座SUV选购指南：大众8X为何成为不挑路的德系旗舰之选](https://news.google.com/rss/articles/CBMiW0FVX3lxTFB2RjZVeHRlMEtDckZjVkxrWGZyQm1kOG1ST0ZHN2IwNjAzMzBWYXotaEg3YWw2VUo2SW9FcUFiLXF1U2VPWXdUSUtKTnJ0M2FfeWRXQkVuVm9yOU0?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-03 [China’s Baidu launches AI model simulating road environment for robotaxis](https://news.google.com/rss/articles/CBMipgFBVV95cUxNNlkxYmZsdkRrNldoVUw2eGpGLVhlNWdXQV9GTlFJQW1MakV6TzU0dmFReU1VS0JZTDhpT2gwYzVQTlJ5OUVfamh6WGpuMHBEVEc5M0xhdlo3UzZ4UWlMTUhrREg4MlpiUFZJNVM0NFBxZjVPQ3lKWmlBVVVzOXRqMDlNN2oydHlpV3pPQzkxTTRsLW51YVFxTFJjV3pCYjFUMzZhRnR3?oc=5) <sub>WTVB</sub>
- 📰 2026-11-03 [智驾中国·长沙篇 奔驰Momenta R6行吗？](https://news.google.com/rss/articles/CBMijAFBVV95cUxPVng2ZGFWLVBLcjNIbWRUTmVPU0trazdzTHE4Y1FNeWJFdU84bkZfVkJMVFd1bDR5THJ2NGRBekc1d3pEUUhkbXdBb0UtZWtVcktMYXRBc2twenVsWWpJcTBkal9EQlFaUFVTQU9tS3Z6cVZUWG9DV1p5b21xRzQzNzM1TjNYRmN6UmJmZA?oc=5) <sub>搜狐网</sub>
- 📰 2026-11-03 [【视频】宁德电池+Momenta智驾，东风日产NX7真舍得下本？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1zUFlXdHdUbkZnbENtazlNbzhBT25sZnptSXFZTlp1Vk9ydGNEMEVURHIyZWxkc2ZJSUxYdXp3QmZTS3BHYm9Da3ZCb3NjVjNNcEZxYy0yaU50Z3c?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>XPeng</b> (196)</summary>

- 📰 2026-11-04 [XPENG Sales Soar!](https://news.google.com/rss/articles/CBMiZEFVX3lxTFB5Vk9Ib0w1WEVneTNYSExvZWZncVRtanQ3WGhiNllhVG5BYnk5TU1PUzVhWmVDZk9RUmVBSHZGdmZ0a2U3S0VtMkRYdjVjelk3LUhPeC1fdlRfaUZ4OUJ3VG8tbEo?oc=5) <sub>CleanTechnica</sub>
- 📰 2026-11-04 [XPeng's August Deliveries Rose 4% — But the Guidance That Followed Is What Investors Can't Swallow](https://news.google.com/rss/articles/CBMi-wFBVV95cUxQTFM5OF83NDg5UHFQMmtPNHBTR3poaGNpZlMtTWM0eWtqSUxIMlhGWG52V3duS2d6R3RxNnVHRjhrYWljR3o4S0E4YXhtUFQ1VlNCS1o2SnpQbEN6cUJyeGZSUzk5RDV3NTZrR1ppbnRUVVVSSy14bFNreG9JZ29Dd3Z3MURLN1dIQ2dvT0JkXy1MaGZNZWdKTHEySFQ5clFWTjV2SkZrdkh6TWtXS2tCQnRCVmV2T2dHM0hkQl9yLXl6RlhvWk5DMjdFVnVOelc3bEEwT0c2dDZaQzk0YzFnUUs4VFVUUEg1TEpvWlRZN1ZianUzT0pLUkUySQ?oc=5) <sub>ad-hoc-news.de</sub>
- 📰 2026-11-04 [智能大五座SUV怎么选？小鹏G9L、智界R7、理想L6、问界M7智能体验对比清单](https://news.google.com/rss/articles/CBMickFVX3lxTFBaa2ZHTVZRTDRxN01iUXd6bGNMTWpNeVZ4aUloNE9qeVFDcHdMazF1dGViZHlCRVFOQl9HLTVSSndxWHdCb1EzVVluV2pCenFVbEoyMXBVaGl1MndZbno3ZGIwS3Y1bGc1UW1oMk05OHJjUQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-04 [最近上市新能源SUV选购清单：小鹏G9L、理想L6、问界M7、智界R7怎么选](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1sTEpVcFlYOHJwa1c2WVluaGhvc2FBWUJ1YkFNdHdFM2ZEalcxbDc2ZXJaX3ZrTmlhRjJqaTZNaTJzTGRMdGhOcmJiTVJiZXEzVVRJcXdqdE9ueUU4aFdr?oc=5) <sub>新浪网</sub>
- 📰 2026-11-04 [25万预算新能源SUV选购清单：小鹏G9L、理想L6、智界R7与乐道L90横评](https://news.google.com/rss/articles/CBMickFVX3lxTFBYN0J2NVBIbTE3RnRyWWwtUkZuNWpjcFUxbnRMYTg3bExfWDFPUGp6NHotLWIyWndYeE5oMUoyQXVSZjQxT3F4VnpyOGViWTVNQ1A2OTB6WVRXZTFiVnM0VEtWVGRmR0pYY0ltb2t4Tk05UQ?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>Li Auto</b> (130)</summary>

- 📰 2026-11-04 [New-generation Li Auto L6 October retail sales surpass 10,000](https://news.google.com/rss/articles/CBMivAFBVV95cUxQT09DWnlhdVZjb3JNRW8tbGpkQ0pvX21jaXVGQ0RCQURoVTc2OHJIRFpjX0tRZUpudzlDX2dkcG1kRk1oNk1SajlYM3pVbkJaN1ZkN21aQm8wUUFXdWQ3QlVMRlc5dWhZcTNQRWw2SE1fR0NqRF9mem8zYlNHdFI0UkpBUkM3X1FGaVotMkxHcFhPWWp1UW52OVk1dmplWXk0ZWZyXzVQaEJSLVVsVFV3WHFJYjRKZ1RtRGVtNQ?oc=5) <sub>Gasgoo</sub>
- 📰 2026-11-04 [理想MEGA24款二手跌破34万值得抄底吗？3个维度说清+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE1iVUJPSUVtdm9relR5WEZDMHV5U2h3VENEZHhrZWdpUHkyX0NhT3lPMFpWUjRMUlBjX2RnZ1l4NEVsU2d4NnJtMDdTRExrclZacDBDMFMyd3VNTF80WmdGcy1lNk9pZ0t0TzJ1NGVBMHhfdw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-04 [2026大六座SUV四车横评：奕境X9与领克900、理想L9、东风奕派M8，谁更懂家庭旗舰](https://news.google.com/rss/articles/CBMickFVX3lxTE9YQldNWnd1d2dzeUtqVERkNFdGZGo3NEdRQjRZdzBNY1NHRDZyT3pKR2NMbml4b1RKLWJYZWxCMFU3ZVhmOF9QaVZtaW1xNW4tZUtxUmJnVlZMX0ZERXl5S2Qyekh5dS1KRkF5MEJ3SEcwdw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-04 [启境GX7/理想L6/问界M6全维度对比：配置/空间/智驾一次说透](https://news.google.com/rss/articles/CBMigAFBVV95cUxQNk5aR0Y3NVdGaTFGaS1QT2ZWdF9xZ2lEcTZTRldCS1YwclloR1plNmwybEtjeEdGTUl0dlpOeW9KWVZsdmxxNGRJM0JMaVJGNkZleENJc1BZbE8wTXdrOTFuTXlzWmI0R3QtNkt3TkR5OVNLMDhIVHVENV90XzNYQQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-11-04 [四款大六座家用SUV横评：空间、续航、智驾逐项对比后，奕境X9成了全家都点头的答案](https://news.google.com/rss/articles/CBMickFVX3lxTE9zeXcwLVAwQUNkcUZ0LXlwNG1aemQ5Y0p4UjhHT2pkeDU3Y19aX01RbEdITnJOV19LYUQ4Q016R2ZvX1FWM1hxOEd4aksxYndTaEF3Znp2MVFUVWVFbEx6TXdMM3FxZVVOZ21aUkVHWTNVUQ?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>NIO</b> (99)</summary>

- 📰 2026-11-04 [Chery's iCar V25 boxy extended-range SUV set for November 19 launch](https://news.google.com/rss/articles/CBMibkFVX3lxTFBySlVkbDZZVl9lbmZMTktqSHAtc0ZBTVBDSmZHXzV0djNhd083XzlwRmJoT3llYlhsSFFDYWl0WUtnZGI2OGhxLUdmdW1JU2x5aExKRkFBYktIODlvSlhwR3hraVhuOEMtc0lCOXJ3?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-04 [【视频】24年蔚来ES6，选配3万多，原漆带车衣，现在只要14万！](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5jYmpHS05YdWYtQm5lanRRRjJmcnNKVm0tOENFdzFZUnlkQ1E1clRkNUVJY2tvWDN2cHUzNERMdjhYaUtXaUZJaXEwN3VkWThJM2hsSk1IemJfS2c?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-04 [25万预算新能源SUV选购清单：小鹏G9L、理想L6、蔚来ES6怎么选](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5laVkyNFYzNGxMeDFVZktiMjZHSi1ENFJnNjJLTWRfdjNkNzMxY1pEWjBLTTdRVjRtQVZRVDl0dkpXOU44eEhCVVFtdkRISV85R01DYUU3dE5fZmFLdXMw?oc=5) <sub>新浪网</sub>
- 📰 2026-11-04 [小鹏G9L与智界R7、理想L6、极氪7X横评，智能体验好的大五座SUV选购清单](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5xVy11SkZBQXJOUzdlRno3dXFmbGdyNzVYZXhlLUtOZDNhY3A0RUdGVTJLQjVlSjByVDB4ODk4cFFoMlhWdHpwbHdOdHhiaUJGOW9tREdPWDJUYm9xNVhV?oc=5) <sub>新浪网</sub>
- 📰 2026-11-04 [大五座装载能力盘点：小鹏G9L、理想L6、极氪7X、蔚来ES6横评](https://news.google.com/rss/articles/CBMiX0FVX3lxTE56bGkwY3pycTkzMEpLQnB6VE1DVDZaUFBoaTJHeTRpMHFzNmVYSEVRUUZOeEpzQ1NuMXR5d2xYZzFYaWw4N3hHNVotcUZ2QnVXSXpydnJGcWJsV2Q0OHpR?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>Huawei</b> (249)</summary>

- 📰 2026-11-04 [These Trucks Haul 90 Tons of Coal on Battery Power—and Drive Themselves](https://news.google.com/rss/articles/CBMirwFBVV95cUxNYnNBT3NFWU00OExpM1Z1b3FON1pSSmh6cUM5dlBsV1RTS1pvaEJHUjV2dnNVVGJnbm14SDJfcWxnMURBRUY3U2ZwN1g1d2Izc2JnTHl1cF96UWNsZlhpTU5ySk5IRHVLcnFMZzQ4dTJ1Sm1TQUVDVG14YjZLSzlHLTRlUUQ2emVCcGh1d0R0QnFvLXl5bXhsb0VTTVFiRVEzOU1XWHpOY3FNTy1zVmNz?oc=5) <sub>WSJ</sub>
- 📰 2026-11-04 [Chery's iCar V25 boxy extended-range SUV set for November 19 launch](https://news.google.com/rss/articles/CBMibkFVX3lxTFBySlVkbDZZVl9lbmZMTktqSHAtc0ZBTVBDSmZHXzV0djNhd083XzlwRmJoT3llYlhsSFFDYWl0WUtnZGI2OGhxLUdmdW1JU2x5aExKRkFBYktIODlvSlhwR3hraVhuOEMtc0lCOXJ3?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-04 [15.98 万元起，东风奕派 M8 天元激光版上市，用自研智驾替换华为乾崑](https://news.google.com/rss/articles/CBMiQ0FVX3lxTE8xaWRPTHdtc0NtcGNzcnV0OEJ2QTZ0TWlOQnVfVl95VlVXTnl4bFFTSVRyMlc5RlBzR1BwdlNuSDhTWTg?oc=5) <sub>爱范儿</sub>
- 📰 2026-11-04 [乾崑智驾里程累计破170亿公里，月活占比95.2%_车市动态](https://news.google.com/rss/articles/CBMia0FVX3lxTE9mUXROb0FfN0k5ZE0wQ3hNMDFJcWcyVzF3a0pYekVYaU9xU21ZMzA5VEx6ZEJzRnYzR1ZCMS1JSnBpQ2lNN0R4UGJmTHpPQlJRVHRia0huTUV2Q1RiTXR5TTBKdXhPMi1fX1FZ?oc=5) <sub>中金在线</sub>
- 📰 2026-11-04 [四款乾崑智驾SUV横评：奕境X9全系标配ADS 5与四激光雷达，30万级大六座怎么选](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1KVjlPS0Y5QTk5UFNZR19ZRmJ0VGZ2Q1NON24zRFQ4dlJaSjgyb0tfNm5UNWQwbDh4dUxuci02d3E0cWpGaEl0Q3p4WFlKbS1WdV9hQlZBbjNEbXRLc2Uw?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>Baidu Apollo</b> (54)</summary>

- 📰 2026-11-04 [Baidu Unveils "Apollo World" AI for Autonomous Driving Training, Cutting Development Costs with 100,000 km of Simulated Driving per Day](https://news.google.com/rss/articles/CBMidkFVX3lxTE9xZGlhaGM4NG5TdmR4MGxDNzFKa0F2S25qOXpfX3oza2FFRDBYUlZiRnZVM0FrR0RITGZoMk9EUE9vdDkyQ0hoTmdXRFI1MXRCdjhvbmpHUWVJLVgzbk5GYTFpLTZpNFhGaXhxb3FuaDJMekowSmc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-04 [百度首次披露Apollo World世界模型，萝卜快跑端到端已投入运营](https://news.google.com/rss/articles/CBMiU0FVX3lxTE5YUVcxcWdjREZiVHRLWWV6ZEFyVlN4bGpKaXpLUS10TXhTTi16S0xPQnUzb0JOM3piQkNqZHJDZnlhVE5LeVB2VWk0RWxSUzFzaXFr?oc=5) <sub>华尔街见闻</sub>
- 📰 2026-11-04 [【视频】萝卜快跑开挂了！云端1天跑完地上3年测试里程](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBMY0tMaFFNdVRmWTA3N3RNUXlzSC1aX2Z1ajd6akhQc3AwdkJSdU9sRERUX3J3VGtXNWlGQnZ5aE5RQ0dUNl9GQXBuWGR2d3UzcU44QXNtU04xQ1k?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-04 [百度披露Apollo World世界模型，每天可生成10万公里模拟驾驶](https://news.google.com/rss/articles/CBMijgFBVV95cUxQMXlHZEhvdlJpdS1WQkQ1OE1lNmVCQ2JsRHdENXpMUHYxUGkxTHR2S0Z6MWhMQUloTmI3RGV5SXY5WjZuWTUwOUFRdGp4bElEd2JSNnV6U2UtTW9nZllsaWJUTWY3WmJ2eFFXUzhvblg2Q1BhaDQ3QnVWZGE5ZWt1LVdLUTU2TC1sM2hZbWZ3?oc=5) <sub>动点科技</sub>
- 📰 2026-11-04 [百度披露Apollo World世界模型 无人车虚拟世界路测1天抵现实3年](https://news.google.com/rss/articles/CBMiUkFVX3lxTFBOVXRSQ3Q0ZlhpQy1hNXhnanRQb2xlTW9zMTI5QU9DcGY5dnhPTTJtNllLY0p4YkxrQUZEN1VzVGxFSkVUajVTR1llYmVSU2NxVXc?oc=5) <sub>香港01</sub>

</details>

<details><summary><b>Pony.ai</b> (128)</summary>

- 📰 2026-11-04 [Baidu Unveils "Apollo World" AI for Autonomous Driving Training, Cutting Development Costs with 100,000 km of Simulated Driving per Day](https://news.google.com/rss/articles/CBMidkFVX3lxTE9xZGlhaGM4NG5TdmR4MGxDNzFKa0F2S25qOXpfX3oza2FFRDBYUlZiRnZVM0FrR0RITGZoMk9EUE9vdDkyQ0hoTmdXRFI1MXRCdjhvbmpHUWVJLVgzbk5GYTFpLTZpNFhGaXhxb3FuaDJMekowSmc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-11-03 [北京小马易行科技公司增资至5.2亿美元](https://news.google.com/rss/articles/CBMiZkFVX3lxTE1PXzlGcGJ6Y0ZXdHFhcjdyckFNcDB2aGJYSnRyZHVfaXlCb2oybWo0S1huQ2lscWxIT0N4U2FjYW02eVd4ZGw5SHZRdGxEd2ZKYXZYTHEyT0dmbXZNN2QxTTItSUVoZw?oc=5) <sub>每日经济新闻</sub>
- 📰 2026-11-03 [纳斯达克中国金龙指数涨超0.5%](https://news.google.com/rss/articles/CBMiY0FVX3lxTE5JM2V5MkFkbzFjWDlfVldTZTZTMjBLNU9pakMwTjV5UHAxY2E2aUdtRDF3ZERBZWFpeC1UejdNNEI3YlhxZ3pXUXpSYjZIZEVtOHprdS1TQjNNM2kxZFBOV3V3QQ?oc=5) <sub>东方财富</sub>
- 📰 2026-11-02 [Manchester Robotaxi Test: 0 Riders, 0 Applications [2026]](https://news.google.com/rss/articles/CBMijwFBVV95cUxNc3pUSHVPUU5rTENVZS0yV0RoLU9JNW9aRnhDc0dwTld3X2JoUzB5M3l5NG9oQVJHRzFJb1U3QldFbUQ2dkh0NlB1MDR5RkgtYnBVYlpHeng3YTB6RF9sY3RySVBRSlBwY1M3VjlhRWtUUjJmXzBWWWRRbHJPQ0szdVZzMU9Gc3dOTlZZUWFTaw?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-11-02 [Self-Driving Taxis Manchester: 3 Firms Test, 0 Riders](https://news.google.com/rss/articles/CBMikAFBVV95cUxQbHRobXBMMjhUWWd0VWsxNEtQdk1aV1JyRUJadVJBRmJwV2ZPMUkybkZ6UXpESENoMkViM0YzUkJXZzhFUjJsdFQteHZqTEN0ODBETGJHQmZPQTV5akpaVl9pbllSTTc5UTcxN0p5REZOMXdkbm93T1huLUcxcEs0MUNEaG80Z3Y3QXloZ003QzA?oc=5) <sub>shattered.io</sub>

</details>

<details><summary><b>WeRide</b> (104)</summary>

- 📰 2026-11-03 [Will the first robotaxis operate in Spain in 2027?](https://news.google.com/rss/articles/CBMilgFBVV95cUxPeEdBTFo5eEJfZEdJOTdkY0xRaTYtUl96d3lyVWliTklOSmlKY3dZVEdrVUFqLTlTM2RZMDBqdFJRTTFjQUVwdnJFOU5DOVZBZ0NpbXFhNUoyNWJxd296S0doWXp2alVscmU3eWhycHNHUmFWbU9JQW9uYWFUVG1hR2VvbTJMS1d4aURQOHBlVVpMbF9QX3c?oc=5) <sub>Spain Travel News</sub>
- 📰 2026-11-03 [Mutua Madrileña insures the first fleet of 20 autonomous cars from Uber and WeRide in Spain](https://news.google.com/rss/articles/CBMixwFBVV95cUxOVGUzbWtwUW9la2VtSl9qbWF3QkwtNG1LN1IycVl4Ukhfd1JfWFBmNUwwWldYZEpSQ0gtekI2aFJxSUpBcEp5eW9pMU5aVko2emJyajJWTzdGMHpaRjdpSWlmMFItMG5HRHZSNlBleGRpdld4VlNTSFh6Wm42Qm9UNURiWTdHYnFpSTI0cUlGeU9kOTlLZkhJeEtzNTBaZEdTSlJaYkFfbmdfdmpFNUg4SG4zR3lVc1cyaHpZT0E0T2NjMmRLaFhn0gHMAUFVX3lxTE56ZDAwMFIyN0tVUm1xOV9HS1lpU0pHa1Y4THA3aVBlaFhUWkc5VEd2UjZId3Jud3RXbzBrR2VxVFJzLU40RXlneG05R1JiQTZFSC1vVE0ySlIzV1hQOFBXd3NXTVYxSkxMUmpsaGowaHc5cFg5M3RiZTNDc1IwbWlzVEhBd0xoQ2lkbE1odkVkVW5pM0NaRS1tSmJFcTFuT05PZEQ0eXRNSS1CMnZ4Z21fbWVRQ3FyRVBwWFUzUm1BUmdyWFJIdUpoN0tpTg?oc=5) <sub>Demócrata</sub>
- 📰 2026-11-03 [港股异动丨文远知行飙升超20%，被传分拆Robovan进行独立融资](https://news.google.com/rss/articles/CBMiakFVX3lxTE1EVnU1Uk9Wd1ZsMjRScnV0akNLUkRLWVNSaXh0Mldyd1N1OUY5dnlFSF9DSzhrV3l0MVFiWTJQMl9LVmZNc2ZIYVJ2Rmw3STdvS0VzVHJMeV9uT3o2UGdJTUpsSDhSQVpMc2c?oc=5) <sub>TradingView</sub>
- 📰 2026-11-03 [12.88万的埃安Ray7，把华为的电机和EMB一起端上来了](https://news.google.com/rss/articles/CBMiWEFVX3lxTE5DcWoxc1pjMmFfMWVFdmlNdXZOc3dSeklLZmdXNVRNRmltdXBybU1FRWxDUXBQMHhqU1FGTlNHUFBuYmdvSF8wVHBuYkFvajB5bjBGdUV6WHU?oc=5) <sub>爱咖号</sub>
- 📰 2026-11-03 [15万级纯电轿车海选：Ray7、银河TT和启源A06怎么选](https://news.google.com/rss/articles/CBMia0FVX3lxTE5NblZfWjJRdko2VDdsR2E2V1VnRk9GNEtHcmRiVDUxZ0VEdl93b0pNeHZTQmZXcTQwMDA3YTVRdTVYMmdqWVAzU2M1YVgzSkR6MFdKbmVsOThLYUl6ajBRZE5MMmVDMHFwTTNr?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Horizon Robotics</b> (121)</summary>

- 📰 2026-11-04 [Volkswagen and Stellantis advance self-driving car plans in China and France](https://news.google.com/rss/articles/CBMirgFBVV95cUxQUTZzTkZlT2Y2ZU5IZzdjYkxHVHp4WE5XdDRUVTkxcWJqVlZfa180M1Z6ZjNSNFlTSElxZTg1UHlYbnZKZ3ZmMWMxdTg5dTdXY2JFYTZENWpuMWV6UXNRbjlIdVJLVW9oTmdMTExsTGRQNzVINzFYbm9rVFJlMDNiTWQ3cUlzcG1YVExLUnYtbWVITWxHRG4zb0ktVVdMOS01OGhlbjhjZV9ha2VENkE?oc=5) <sub>The Driven</sub>
- 📰 2026-11-04 [Chery iCaur V25 EREV set for November 19 launch with pre-sales from 19,650 USD](https://news.google.com/rss/articles/CBMitAFBVV95cUxQbFpiU0gtWUpwSkdVRmpQQ0U5bGYtaEdROXY2QnpzRHY3LUNfQkhibkQxcU4xT1QtdnRtMlJRSlRBTURWNGNwdHlwcU1xcWZ1YTBNRHB5ei1JQU5hUnhxX3BrRjBVQmdEOUtRckF6R2N6WlJpcGdfOFkzOE9fZ0tGNDlfcmI0RkVta2FVaWx0dElOY2t0LWZWRGgxeGpzb09oY0dOcHJVcEhVMTNwZEYyTVExdkU?oc=5) <sub>CarNewsChina.com</sub>
- 📰 2026-11-04 [Chery's iCar V25 boxy extended-range SUV set for November 19 launch](https://news.google.com/rss/articles/CBMibkFVX3lxTFBySlVkbDZZVl9lbmZMTktqSHAtc0ZBTVBDSmZHXzV0djNhd083XzlwRmJoT3llYlhsSFFDYWl0WUtnZGI2OGhxLUdmdW1JU2x5aExKRkFBYktIODlvSlhwR3hraVhuOEMtc0lCOXJ3?oc=5) <sub>CnEVPost</sub>
- 📰 2026-11-04 [无底线的PPT算力狂飙！地平线余凯质疑智驾芯片算力虚标](https://news.google.com/rss/articles/CBMiWEFVX3lxTE5fUE9GNnlwSWkzelZTNzBndGFyXzh5WmN4RV9IcGxVRkQzdUhlbUpiRlpnVlRhbW4xNl8wS2JuLXlhUjNMc2pyaE1uR29sZ2dnSmc0LU5uQXY?oc=5) <sub>驱动之家</sub>
- 📰 2026-11-03 [GlobalData: Physical AI Buzz Surges on X Amid Robotics and Autonomous Mobility Boom](https://news.google.com/rss/articles/CBMijgFBVV95cUxOV01Pb2VVZ1ZfLVVqaEQ2VmJKUGlRclRGMGdTMHVzT3ozcmJONWhBV3Z0MXBVdDhub2xLemh6NlB3eXNBeXAwbnBkX2trdngtSElZcjdnSHhqeWlmaElPVlJRLUxPMUhVOUtPMFZDVTdGSW51SGhRYlZwbHZzclo2d1hETzRyWnR4OXh1cW5R?oc=5) <sub>Wazzup.PH</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (19)</summary>

- 📰 2026-11-04 [GPT-6之后，智驾公司只剩一条路？](https://news.google.com/rss/articles/CBMiUEFVX3lxTE9SazhISDVJc01Sbzg2WHg1ZzREaWdVR2lxODNKb3VpcF9QYkhCUWpHLWhxa3RFV1VZdG1HdW9wblVrVlZKdWM0R1lmUDA3c1ZW?oc=5) <sub>盖世汽车</sub>
- 📰 2026-11-03 [11-12月，至少10款重磅SUV排队上市](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9tUmQ5Z1RpMkVRUGF3Z3Y0NmcyUk9NSy1TeVowSUkzY2VmcWdMTlhkY2gtN1RrUXZNWmRWQi0yVEdPU2MxRVRtbDdXY0xod0lzT2NVRmp1VjNFUlE?oc=5) <sub>汽车之家</sub>
- 📰 2026-11-02 [Toyota & Waymo to Begin Scaling Autonomous Japanese Fleet](https://news.google.com/rss/articles/CBMikwFBVV95cUxQczdaa2pqTnhGbVc2SmVxemkzamNNdFVwWWZ3ZnRlbXU1SW1qX1NpemxvWDkyNWhlMWRTNHBvZ3hnYURVcTVlejlBS1BmcHM5YkVMcE1VOXNWYXJpQWRKa2JERF9VMVZMb0o3RkVrMHNUQnhtWEluTzE0RDMxM3VkaXdmSzF4Z1dTUGdNaE12Q05iOWs?oc=5) <sub>Future Transport-News</sub>
- 📰 2026-10-29 [2022‑2026H1 国内乘用车 NOA 第三方智驾算法厂商全景梳理](https://news.google.com/rss/articles/CBMiU0FVX3lxTFBkSDRpNG03a29aNElYOFZSSjE5OE5iMTRISFd6ME1DWnE4OG95S0FlRFYyNm5oNTRlNktRcVc3VXo4TFpPZ3V0QWxqRjJwMElGWlA4?oc=5) <sub>电子工程专辑</sub>
- 📰 2026-10-29 [他在不被看见的技术高地，砸碎了一堵西方60年的技术高墙！](https://news.google.com/rss/articles/CBMiZEFVX3lxTE93ZmRqYi1TVC1qMXJpSEdYXzhCVEF4TGhqT1BVZngwVW9UeEQySDYyZ05uaDViX2ZxN1lmdkVLM05sXy1LdmxjVGstaWwxUnd6akhRZnpYUUVzRGNfODJ0cWxfUnc?oc=5) <sub>中国新闻周刊</sub>

</details>

<details><summary><b>Mobileye</b> (28)</summary>

- 📰 2026-11-03 [Conferencia de resultados del 3T de 2026 de Mobileye (MBLY): Eleva previsiones a medida que crece la demanda de EyeQ](https://news.google.com/rss/articles/CBMidkFVX3lxTE1WUVVUTTZWaU1NbGpBZ18zS0NEN25uMnZnZVNqY3RjZnAyTG1CQnM2QlNIYk1pV191TlQyWWJoVXNQWjI1MVZZYkFGU0hMYzBzTl9idElzek0wSVNKRjdTdTY1ekZubDVNS1dtNnhyTGZheHlaTFE?oc=5) <sub>TradingKey</sub>
- 📰 2026-11-03 [Elon Musk: Teslas will soon be able to drive themselves coast to coast](https://news.google.com/rss/articles/CBMic0FVX3lxTFA3WXZ0NzdKSEFxdnJJWWdIZ08zMThvN2h1UllLc3p6RlJrTHBfNTFMcmVKYmNMZGdzWG1uY2NqSzNmUXdGVWFsdzM4TXdoaGNRWFNYQWpYcHZ1c0JEdzQ4VnM4YTczYlNWWE9wYnFGRnFLZzQ?oc=5) <sub>Mashable</sub>
- 📰 2026-10-30 [Mobileye Global (MBLY) Dropped, What Is Behind Its Latest Move?](https://news.google.com/rss/articles/CBMi0gFBVV95cUxPeV9lYmcxQk5FbDhpNTJzVWw1Nm1OYS1SRS1xdU5YbS1ybXV3MTV5YUtwSGFYTGJvWTJOWHpVMVVraUs2R0VwSmFzbzB5bzFQajNGMVlLUW1KLW9qNWV3eTROMTZwVi1vTF9xeXVxTDNjZWpUbi1pNV9zcnRNS1pmcUNDbkpRUFgzZGtjdzZMeDkzVWVDLTl2S19ESHA3eUFYV29IQmRITWtLRVo1TVFjbm5KR2NHTUR6dTRVS2VjWENEVzdyZ3JBUFNMN2RuVnpveXfSAdcBQVVfeXFMUHNYLTFxZVNVNW12WVRKcGtqTXhPS0c4R1ZBMmtMaWpjMWdfRTE0X1d6bm1rZ0lpVUwzV09LWE1vWWx2bGdhU3RLc2QycWQxMHlIbDdreUVOQXFHWHh2UVNvWFJnci02bmhWcTlqNDV6Nk1lejQ3U05iTDFSM1JYU2Rpbm1pS2pnOWJaNFU1Q0U1bmtEaEJYaWN2dzEyS0pYb1NsMkFDRG5oOTEzaWZuMGtVTHFCdUZ1dU56T0ZmdFBfc3BSSUhmVEs5N3diMEJXaGt0VWluNjg?oc=5) <sub>Simply Wall St</sub>
- 📰 2026-10-29 [Mobileye slides even as it tweaks full-year guidance on SuperVision strength](https://news.google.com/rss/articles/CBMi1gFBVV95cUxNaEtXanY5ZnlTNjZLRmkxWjgyeHdVZDNBWUxQTzZWWm1fM0Z0bjdFNE1CU0ZDdzF1Z0NwV1QyN1FQcmdvR05SSl9EVEw1ZzJBVWdfcGt2SzE3eEZ4dFZWVHZ4NXRlY1RuVlhLY180ZDRXNUtCVXdQRjYtSllDMjVvamM1U0ticFFzeXgwMm4xTWN6RDJONlNZN2xDUklQOFU3ZnBULVBMNW4xSU1UYTNNcE5QMUhVNDUzMmxuZU5PbWozbDkzOGZuNGg3X0tKc21MUTZxcmZR?oc=5) <sub>TradingView</sub>
- 📰 2026-10-29 [Mobileye Q3 Revenue Falls 2% to $492 Million; Adjusted EPS Is $0.11](https://news.google.com/rss/articles/CBMibEFVX3lxTE4yczhEc1RNUzhiSVU4THdjamZndlcxazNRSDlSRjYxRldOVFhwSjZzOTVjRG12MFZ0YWVNMk1oWmdQLUNUU0RsWmhIMjV2LXZXRk83RnlEOTh1S09nMjBNTWtPQnppaFJEM0Ricg?oc=5) <sub>TradingView</sub>

</details>

<details><summary><b>Aurora</b> (40)</summary>

- 📰 2026-11-04 [AUR Investigation Notice: Kessler Topaz Meltzer & Check, LLP Encourages Aurora Innovation, Inc. (AUR) Investors to Contact the Firm](https://news.google.com/rss/articles/CBMi-AFBVV95cUxOaFF2RWVPZmNNV1EyV1pFLWVhbHF5Z2pfLXdTWENFc0l6WDFBb0VibmZaYkJnR2xtWF9tQldud1N6Uk96QlBaV1F6NVRQczVfRHZheXZ3ZDYwM2U5Sl9jMElmTHI4Rm8yMVhkSXY4elBlUmx0Vmt6b2xidjhYWWRsYlRmUWxRYnkzVHFhckl2MkNfalQyb3RpSVg2eU1NaDdsb3FzNzNtX19acUJSV3puMThZVlplY1lrT2tRSURlRmlhU0Zydmpod0M5VU9IZHJQMC1iSWJnQmwtdTRYLVBRd2ZUanFUTjUxZ1dpMHpEVDFBWk9yTWY1LQ?oc=5) <sub>NewMediaWire</sub>
- 📰 2026-11-03 [Aurora Innovation, Inc. (AUR) Securities Investigation Notice - Levi & Korsinsky](https://news.google.com/rss/articles/CBMi0wFBVV95cUxQZ2hoVzI4QXdBOU1sUVpoNS1ULWcwNDc2MTBaanliTk1PMTE2ckJjeEVIWWU1VGRKRmVlaUxOSklkRE9aVThMT18xQklMUjluVzJ5TTdET0tXQkhNc0VUV2hQSVE0bDd0bmFFeGExMkJ6RHQxQ25Ud1F5MXByOERkUUx4WldaTkZUQ3p4YlotdlVmRnh6VVd1Vm8wT1REYWdYNnp5N3hpQ181OVhwXzFXcHNmU3pFblpjLTBpMWo2cTI1S0NQQkd5WEhNOXFCOURaNkFV?oc=5) <sub>FinancialContent</sub>
- 📰 2026-11-02 ['Driverless' trucking depends on lidar from 'Chinese Military Company' Hesai](https://news.google.com/rss/articles/CBMivwFBVV95cUxQdlNIZXdtNUFpVnNwWHhnWW5DYjU4ZU1GUG8xZmVaZEtwR0NaRXB4SXpEZWJLcTNRSnZNXzVpNmV4b29OODVkZ0VWZFhaQXhnUmhUSDhCV2FUTmpLY2RORkM3MG00NGlqMGNJaEV5cldRbXpaazZzQlJzVzhUc0FKUzRISUg4em9OdEJmWFdVTnZmMW1pOV9MNWdIbHVNQnRERjRUd1pXMlc0WTVMSmFqaENGUUV2RDNOWk1TNy16OA?oc=5) <sub>Overdrive Magazine</sub>
- 📰 2026-11-02 [Weekly Recap: Revenue outlook cut and driverless trucks log 500,000 miles](https://news.google.com/rss/articles/CBMizwFBVV95cUxOejFMMUxxX00zalNzS0E0d19MUTd2aGVhcXpkWkVjaHpWQTQzcVNkRklWUzdjTVpzTUhBY1dXUWRueW1UY3d5S3NWYTJhUGRLeGRTMWhlRmhDUmF3Q0J2dlRDSzNVd2VUMG4zak9uX3cyNUJtNHZHc0xodlJ5Znp0cnFPZTVsOUdmczg5VmlIR2RfSGo0SGtTUGhYQ09rcFEybWFETUp3LWhrSGxqM2NtLUYtV2Yta295RW81Mmk4c3Q4NVdZOVdVdE1VeG5jVWs?oc=5) <sub>TradingView</sub>
- 📰 2026-10-30 [Aurora’s Driverless Trucks on Pace for 2027 Expansion Target](https://news.google.com/rss/articles/CBMiqwFBVV95cUxNNU9JbHBiY2l5OGQ5a0ZESkJhYWxyZFlHSW9UWDJhd216VDBpYlJxcldnejIwT3daNl9rU3NtNHVxVEw4WV9MMENlNG84OWoteDNDNDc3elozY2JqdmlRQW9Ua1ZxWkRPUEtTNnFsNUhKam5UOTNJZ2ttQTdEVlo1WDRHTDFOblVmY3FXNXlvdkp4U3RUZWtDSEZ2MjlXMUJQT3M3UDhIRGo5clk?oc=5) <sub>Supply Chain Brain</sub>

</details>

<details><summary><b>Zoox</b> (49)</summary>

- 📰 2026-11-03 [Tesla's Robotaxi service goes live in Austin. Price? $4.20 per ride.](https://news.google.com/rss/articles/CBMicEFVX3lxTE11X2o1TUdROGotR2FsVTVBaXk5Q2JKWG1DS3Nwa2FLeXYwUlhUSExVZW9uRmVRcllwSW53cFRuRXdqbjlfWnRlQmx4OTN1OUFBa3hnXzFTNUpWT0s4YUVNRm1nTE12Wi1seWdwSVNYTjU?oc=5) <sub>Mashable</sub>
- 📰 2026-11-03 [Tesla Robotaxi Dallas-Fort Worth Field Report｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1DS0hlU1BjN2dyaGNQX1ZBeG9zY3hBeHdXVW1pOTFIS2ZnN1ZiUUhRTUM2T0ZxNWJOTG5wanZWUGdHaUU0SmNOeExNMHotRmxsQjdDVlFweUItRVd0bU93?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-11-03 [A 78-year-old was arrested for blocking an Uber Eats robot in Philly. Now a lawmaker wants to tax every robot delivery](https://news.google.com/rss/articles/CBMimgFBVV95cUxONGFhWk4zUHN3NnlydFJ6dWphTnczYk1QZV9KNWtjYngxc0Z5SG5VTTZlcVJLVHVJQXhEbVI5MjYzQW5LTW1YVl9wbThRUE04M3NRWVZFTTZHSVpSQ05Ic3hqQkpIRmdicG9udkgwRGphYWxSQWJFcXJCR1NwSDdjVlRrcV80d3FUUlN0VEhaTTNjM1BJNVBLc2dn?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-11-03 [So What’s Going On With the Cybercab?](https://news.google.com/rss/articles/CBMigwFBVV95cUxNNUJMd19lM3pPQmtHcndOMmlUUThWWGhsbFA2R1d2WjA5QVhPaV9vY1VPT0dleERRbmRRYzBtakJVX2RwRmpJcmFuS1JCY0dsWFhVQUIzcHFHc0hZLWdiWEhUWWRUXy1NSlZkTk1HV1oxNlcxZVAtZ2tIOUJIb0xhbmJNVQ?oc=5) <sub>Changing Lanes \| Andrew Miller</sub>
- 📰 2026-11-03 [CVG Q3 2026 slides: margin gains drive return to profitability By Investing.com](https://news.google.com/rss/articles/CBMivwFBVV95cUxORTI5ZXktaURkb2w0OTU1cjFuSk1rOGJMNzhTS2M1bXpCakJpSUhnWTBHaEZRQ2pxakx1QmpZWVQxX2prQVBEN3BaN3ZoMkdaV2N5WXFqUnJ2Y2tWbTEtdkxvZTVKbXUybmpMS1gxR0hXNVh5VldDc3N6VmNEb3dmd19nNXF1eWFYZkV1Y0pRdkNZSGNNUjNGYTdkQzNjQ2JUQTluaUs2eFd4bGItYlFKQ01yZENXbzR3TDhvX1V1bw?oc=5) <sub>Investing.com Canada</sub>

</details>

<details><summary><b>Motional</b> (10)</summary>

- 📰 2026-10-29 [Hesai Leads Global Robotaxi Lidar Market with 62% Share as Robotaxi Industry Moves Toward Scale, Yole Group Reports](https://news.google.com/rss/articles/CBMi8gFBVV95cUxQaE40Ym5SMXFZYWhRM3FYYzUxbzI0Yk5tTExfWVpsMW1mTkdRLTNpdVJPQkR6NzJub2hFaFZ2TWJlc2VWdEVlZC1ZWThOb0U0aV9pblFOSmZNQ2t6bVNjRnoxeVZnMVRVTnpZNkgtTXZyM09nMmNUb25VVlBpR1ZGeEtIWGlSUWhJMFBCUC01dDh3R3JLOGxDNEpacEMwRWZoNmEySU03emlOTENXbDhMS0ctSFVRaXJRZ0RPOHFKdlVucTM4THc4YnhCR09LV1FpSnBEcVRneEI3d1hwdlFieGIzaV8yaTY4LWMwTzNIc0Rrdw?oc=5) <sub>Thailand Business News</sub>
- 📰 2026-10-28 [Hyundai Motor Rises to No. 29 in Interbrand’s Best Global Brands 2026 Ranking](https://news.google.com/rss/articles/CBMirgFBVV95cUxOYW13NmJqeUZhQ1A1UnJOYjB6NUdRZU9uOHdFRVR6Um42WFlSZmdOOXV2WnJqVUdJVUw0eXVPSTMxdWlNRnMySXJ6N2dhd0pIYXBpWXU2cDdZRlZNWGhhWWVLcDdnV05kMVd4cGtiYUkzNnRPTVN2UW82cmdSdHNfZy1KMlktRlZWMF9TdWNLSDlZeWJZcWtscG5ZVWg2T2ZMY09NNFNDOGlPUkw3SVE?oc=5) <sub>Indian Television Dot Com</sub>
- 📰 2026-10-28 [Hyundai Motor Rises To No. 29 In Interbrand Global Brand Ranking](https://news.google.com/rss/articles/CBMiqwFBVV95cUxPWlRYZlVKTzNZWmdfWXpGUmxJd2ZKQ1pnX1otaXB4XzgycnY0NmZkUXFsSGFZQlRKbFJWRkFwWmIzWEF6X0IzRjh3Z09YYkxGRm1nbURLQU05R3pnN3ZLcHVfMHRRNm85T3hXeUR5Mklha19vZ2QxUmdiNE4xTUxaaV9Nd3hLQk9Nc1ZTY1lxbmR2Z3RxSXQ5RlRnb2RLTmowMkVaZzRIZUdGZDDSAasBQVVfeXFMT1pUWGZVSk8zWVpnX1l6RlJsSXdmSkNaZ19aLWlweF84MnJ2NDZmZFFxbEhhWUJUSmxSVkZBcFpiM1hBel9CM0Y4d2dPWGJMRkZtZ21ES0FNOUd6Zzd2S3B1XzB0UTZvOU94V3lEeTJJYWtfb2dkMVJnYjROMU1MWmlfTXd4S0JPTXNWU2NZcW5kdmd0cUl0OUZUZ29kS05qMDJFWmc0SGVHRmQw?oc=5) <sub>Autocar Professional</sub>
- 📰 2026-10-28 [Waymo Nashville Airport Field Report｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5DTDlkRWVqN1hmbndLVTU0RGZOLXhLWjRabFVIc01jb3R0eGRUNDBOZ0pzdzJLbGRSelpydjF5TXVMc0UwNnB3OTZCN05iV0stdzBGWTJ1R0s2WjdyZEE0?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-28 [Waymo Beats Uber by $10 at Nashville Airport, but Loses on the Highway, Field Report Finds](https://news.google.com/rss/articles/CBMiW0FVX3lxTFAzS3V3bDhOWnRqTmhzRzVNQWx1MlBhV0psZ2lwZEU0TEdoazhtMXZ0Tm9jbUlId2p0TV9EX3FiUmtmZXNPaGdkS3dGY2ZlNEc5cks3WGNUSGxFVnM?oc=5) <sub>BigGo Finance</sub>

</details>

<details><summary><b>comma.ai</b> (7)</summary>

- 📝 2026-10-23 [openpilot 0.11.2](https://blog.comma.ai/0112release/) <sub>official blog</sub>
- 📰 2026-10-29 [We Upgrade Our comma three to a comma four: Is It Worth It?](https://news.google.com/rss/articles/CBMimwFBVV95cUxOVkgtNU9hLXVYM0U2VjNpVldsNFFoQm53SjJGcU1CcnNMWXY5YzFYdVhoYlNZdG5vX21Va2h4b2RLYTNEUTBLdUFhMXd5eTVjLXBSTHE5bFN6elNqa1diTThPQ0Z0Mlo4SldDTzQ4eGxEWl9NTjNKcUNGQmhLeGRSMUxOSElpMkVNOTN4QWhMV0hPRFFJV3cyeVNLSQ?oc=5) <sub>Transport Evolved</sub>
- 📰 2026-10-29 [Aftermarket Self-Driving Devices Face Federal Investigation Following Five Crashes, Three Deaths](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPUG8ycGN4Tl96dk4xZk1yTEJrVkpvVGNsX2JnbWJoeXlzS1ZsVDlEYWk0SnFQQTZXQXpfN21BU20wR1FmR1lsUFpoeHdzU1BUaGdheTZ3LUFkVnpaOHhyWUU0YU1yWERQYmI2TDRnd1VpbTM3Ui1yWFdQVzZIRHVrUEhZUFBKcGpM?oc=5) <sub>AOL.com</sub>
- 📰 2026-10-29 [A $1,000 Device Enables Hands-Free Driving. But Fatal Crashes Have Prompted Scrutiny.](https://news.google.com/rss/articles/CBMixAFBVV95cUxObnRHUXNNS2wxNVFWeHVLdm9qYmZ1bnpaUVN2VWJ1eHZhbFRiWGxoVWxaSjNuNzNKQXZ0RV80dVRnckFGc003eXZJeW5ZWkhUakpsdk9sQ0lnQUZZeVNGekRzYmhvR2RrU1Ric29JeUFmQzNNdEE5NEtZLUgyS2hmQ1hwYWlMdFNDRHNZQVB6dHNqUjIyaXpRMFd2c0YxN0c3Vk9yZF9kR255QmtTUlRiaEtYbDY1dHVZQm9ReHY5WUdMSzJQ?oc=5) <sub>WSJ</sub>
- 📰 2026-10-21 [Is the race to build self-driving AI turning into a cyberwar?](https://news.google.com/rss/articles/CBMikAFBVV95cUxPd1ljS1V3ZmI4RGdJZkRQdVpkNmRqcm5tVUtpRllXYWMyQ2ZnaFFKRzgzY0VaUDNTR3VwYV9lRHI2RnRUcV9za0p3bTNsMGJmSHNZUlR0MDFsYm1FLTVtUEl1UEJhSi1hXzMtc05tendPaDltRzlMczQwRkx0dTZJaGVjTk1DOXp1cVpSS2Zqc0w?oc=5) <sub>Yahoo Tech</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
