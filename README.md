# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-10-28 · 1,309 papers tracked · 45 curated.

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
- [End-to-End Driving & Planning](#end-to-end-driving--planning) (9)
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
| [SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving](https://arxiv.org/abs/2610.20609)<br><sub>Shaoyuan Xie, Zihan Zhang, Jingxuan Wang et al.</sub> | CoRL 2026<br>2026-10 | [⭐ 29](https://github.com/ASGuard-UCI/safedrive-vla) | Vision-Language-Action (VLA) models are gaining attention in autonomous driving, inheriting commonsense priors from large language models (LLMs) and widening the navigation interface from a fixed command set to free-form… |
| [Scene-Adaptive VLA: Efficient Autonomous Driving via Dynamic Layer Routing](https://arxiv.org/abs/2610.24590)<br><sub>Yujia Yang, Quan Yuan, Jiawei Fan et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 2](https://github.com/yang-luvu/Scene-Adaptive-VLA) | Vision-Language-Action (VLA) models offer a promising paradigm for autonomous driving |
| [CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving](https://arxiv.org/abs/2607.04179)<br><sub>Zhaohong Liu, Hao Ye, Xianlin Zhang et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 1](https://github.com/MICLAB-BUPT/CritiqueDriveVLM) | End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving |
| [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)<br><sub>Nan Yang, Zhanwen Liu, Linfeng Zhang et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 11](https://github.com/Zizzzzzzz/MVPruner) | Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings |
| [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)<br><sub>Yuan Gao, Wenting Miao, Mattia Piccinini et al.</sub> | IROS<br>2026-07<br>📑 1 | [⭐ 29](https://github.com/TUM-AVS/Chat2scenic) | Validating autonomous driving systems requires diverse, regulation-compliant test scenarios |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 12 | [⭐ 531](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
| [GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives](https://arxiv.org/abs/2609.39601)<br><sub>Qize Yu, Lianrui Fan, Boyu Chen et al.</sub> | arXiv<br>2026-09<br>📑 2 | [⭐ 214](https://github.com/groundingpi/GroundingPI) | Precise grounding matters |
| [GRAVA: Grounded Reasoning-to-Action Representation and Learning for Autonomous Driving](https://arxiv.org/abs/2609.15169)<br><sub>Xiao Liu, Haoyu Li, Jianghao Leng et al.</sub> | arXiv<br>2026-09 | [⭐ 414](https://github.com/AhernResearch/grava) | Driving vision-language-action (VLA) models increasingly reason before acting, but their intermediate reasoning is often weakly grounded in physical scene evidence and loosely connected to executable behavior |
| [Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air](https://arxiv.org/abs/2605.31066)<br><sub>Tianle Zeng, Yanci Wen, Xueang Yu et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 1,123](https://github.com/louiszengCN/CarlaAir) | Recent aerial vision-language-action (VLA) models show promising single-UAV capabilities, such as tracking moving objects and navigating to language-specified landmarks |

## World Models & Generative Simulation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [HERMES++: Toward a Unified Driving World Model for 3D Scene Understanding and Generation](https://arxiv.org/abs/2604.28196)<br><sub>Xin Zhou, Dingkang Liang, Xiwu Chen et al.</sub> | ICCV 2025<br>2026-04<br>📑 5 | [⭐ 72](https://github.com/H-EmbodVis/HERMESV2) | Driving world models serve as a pivotal technology for autonomous driving by simulating environmental dynamics |
| [FrozenDrive: Zero-Shot Text-Guided Driving Scene Generation and Data Augmentation with Parameter-Free Frozen Diffusion Model](https://arxiv.org/abs/2606.20110)<br><sub>Yuhwan Jeong, Hyeonseong Kim, Daehyun We et al.</sub> | ECCV 2026<br>2026-06<br>📑 1 | [⭐ 10](https://github.com/daehyunwe/FrozenDrive) | Synthetic data for autonomous driving is surging, powered by diffusion models that promise scalable scene generation |
| [MESSENGER: Memory-Enhanced Sequential Scene Flow Estimation via Autoregressive Next-Frame Forecasting](https://arxiv.org/abs/2610.10759)<br><sub>Jiuming Liu, Jianing Li, Mengmeng Liu et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 0](https://github.com/liujiuming123/Messenger) | Scene flow can capture low-level 3D motion displacements in dynamic scenarios |
| [ASTAD: Asymmetric Style Transfer for Synthetic-to-Real Adaptation in Autonomous Driving](https://arxiv.org/abs/2606.29286)<br><sub>Dingyi Yao, Xinqi Zhang, Lihui Peng et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 2](https://github.com/Dingyi-Yao/ASTAD) | Synthetic data mitigates the data scarcity problem in autonomous driving perception |
| [Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends](https://arxiv.org/abs/2606.01164)<br><sub>Jiuming Liu, Chaojun Ni, Mengmeng Liu et al.</sub> | arXiv<br>2026-06<br>📑 8 | [⭐ 247](https://github.com/liujiuming123/Awesome-Interactive-World-Model) | With rapid development of large language models and diffusion-based content generation, world modeling has attracted increasing research attention, benefiting various downstream domains such as game engines, embodied AI,… |
| [Is Your Driving World Model an All-Around Player?](https://arxiv.org/abs/2605.10858)<br><sub>Lingdong Kong, Ao Liang, Tianyi Yan et al.</sub> | arXiv<br>2026-05<br>📑 6 | [⭐ 257](https://github.com/worldbench/WorldLens) | Today's driving world models can generate remarkably realistic dash-cam videos, yet no single model excels universally |

## End-to-End Driving & Planning

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](https://arxiv.org/abs/2609.26792)<br><sub>Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.</sub> | CoRL 2026<br>2026-09<br>📑 1 | [⭐ 14](https://github.com/VAIL-UCLA/DreamStream) | Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions |
| [DriveMLP: When Training Strategy Outperforms Model Complexity in Autonomous Driving](https://arxiv.org/abs/2610.29676)<br><sub>Alessandro Canevaro, Julian Schmidt, Hang Yu et al.</sub> | CoRL<br>2026-10 | [⭐ 5](https://github.com/alessandro-canevaro/DriveMLP) | Learning motion planning policies that remain reliable under closed-loop execution is a central challenge in Autonomous Driving (AD) |
| [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)<br><sub>Shen Zheng, Anurag Ghosh, Gaurav Parmar et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 32](https://github.com/ShenZheng2000/WarpI2I) | Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs) |
| [G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance](https://arxiv.org/abs/2606.26017)<br><sub>Hang Yu, Ye Jin, Alessandro Canevaro et al.</sub> | IROS 2026<br>2026-06<br>📑 5 | [⭐ 7](https://github.com/HangYuu/G2DP) | In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 17 | [⭐ 349](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
| [SimWAM: A Simple World Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.07468)<br><sub>Zongchuang Zhao, Xin Zhou, Tianyang Xu et al.</sub> | arXiv<br>2026-08<br>📑 9 | [⭐ 198](https://github.com/H-EmbodVis/SimWAM) | In autonomous driving, World-Action Models (WAMs) have improved end-to-end planning by transferring video dynamics priors to action prediction, but many still couple planning with future-video generation at inference, in… |
| [Latent-Centroid Steering: Single-Pass Classifier-Free Guidance for Command-Aligned Autonomous Driving](https://arxiv.org/abs/2608.00237)<br><sub>Meibo Hu, Jiamian Wang, Pichao Wang et al.</sub> | IROS 2026<br>2026-08 | [⭐ 2](https://github.com/codingmlinprocess/LCS) | Vision-language models (VLMs) have recently emerged as a promising paradigm for end-to-end autonomous driving, enabling agents to map multimodal inputs and high-level navigation instructions directly to executable trajec… |
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
| [FreeOcc: Training-Free Embodied Open-Vocabulary Occupancy Prediction](https://arxiv.org/abs/2604.28115)<br><sub>Zeyu Jiang, Changqing Zhou, Xingxing Zuo et al.</sub> | RSS<br>2026-04<br>📑 7 | [⭐ 143](https://github.com/the-masses/FreeOcc) | Existing learning-based occupancy prediction methods rely on large-scale 3D annotations and generalize poorly across environments |
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
| [123D: Unifying Multi-Modal Autonomous Driving Data at Scale](https://arxiv.org/abs/2605.08084)<br><sub>Daniel Dauner, Valentin Charraut, Bastian Berle et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 403](https://github.com/kesai-labs/py123d) | The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics |

## Safety, Robustness & Evaluation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [CCFM: Collision-Constrained Flow Matching for Safety-Critical Scenario Generation](https://arxiv.org/abs/2607.04451)<br><sub>Ke Li, Kaidi Liang, Yuxin Ding et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 3](https://github.com/KELISBU/CCFM) | Evaluation of autonomous vehicle (AV) planners in safety-critical closed-loop simulation is essential for real-world deployment |
| [Lipschitz Optimization for Formal Verification of Homographies](https://arxiv.org/abs/2605.23203)<br><sub>Jean-Guillaume Durand, Panagiotis Kouvaros, Maxime Gariel et al.</sub> | CVPR 2026<br>2026-05 | [⭐ 2](https://github.com/jeangud/homography-verification) | The adoption of vision neural networks in regulated industries requires formal robustness guarantees, especially in safety-critical domains such as healthcare, autonomous vehicles, and aerospace |
| [CADET: A Modular Platform for Evaluating Distributed Cooperative Autonomy in Connected Autonomous Vehicles](https://arxiv.org/abs/2606.04072)<br><sub>Pragya Sharma, Brian Wang, Mani Srivastava</sub> | ICRA 2026<br>2026-06<br>📑 1 | [⭐ 0](https://github.com/nesl/cadet) | Deep learning models are increasingly central to autonomous vehicle (AV) pipelines, yet their integration has traditionally followed a monolithic design where perception, planning, and control execute on a single onboard… |

## 🏢 Industry Tracker

Latest 14 days of news, official blog posts and new open-source repos from tracked companies. Full daily feed in [`daily/`](daily/).

<details><summary><b>Waymo</b> (264)</summary>

- 📝 2026-10-16 [Hello Toronto! Waymo is En Route](https://waymo.com/blog/2026/10/waymo-in-toronto) <sub>official blog</sub>
- 📰 2026-10-28 [Viral video shows stopped Waymo near Universal as service expands in Orlando](https://news.google.com/rss/articles/CBMixwFBVV95cUxOOS01NktQWTgtcnhzSzhyMzAxcE9FWUptbFJtTS1OZWMtRi0zNGFKRk1HbFdBSXBiQ3NqNnUybHdwYlZVb1hLczhGc2RSb29mMXdMUERXdDFjeXEwUnRhZWtmeGJYMC15d1FIaUs4TE5FdDlVYUdOZkt2UGpHWklRQjNBc0pZZmdYcW9DUjR1SHZvUFB0NWJHeW5hT19tYm9UTHp2bExicndYM0pfVTRsejRhVWRQaWZIUUVIUU5XVVotQW1odXhF?oc=5) <sub>WKMG</sub>
- 📰 2026-10-28 [Stalled in D.C., Waymo turns to Virginia](https://news.google.com/rss/articles/CBMijgFBVV95cUxOVURiVEtaYUdaUXM4UUVVdVJMVzdIY3FEUEtmWGRoZXg4dUZXaTNtdmFYVlU3NzlKNHI4cV9kanJ3VzRfYjd0ajJJUTdYQkFLZkFDLUJJc20tUFlCZWhtQWxZNHJqRVNydHVLdFFILVA5Y1RjZHJaajVwRmcwMXN4UmtsRFctWDlVY05RdzdR?oc=5) <sub>The Washington Post</sub>
- 📰 2026-10-28 [Waymo vs Tesla Robotaxi [2026]: 7x Gap, Waymo Wins](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPR0d1dUh6eEJFLWJSYzJMY0UyZkhOdGhjaGJLdWFVYWRsYWdZOGpaYmZDZUJLMXhtdVNoTF9SWDVfSUptRVZIMDBPWFdTU0twOV9oNDdObHdpTHBfN3Y0MDdKWTEwekd1ZHVuWG1NeDQzNDBhei1Vd3VQRm9MLWNEZDVvbFdLaFNt?oc=5) <sub>tech-insider.org</sub>
- 📰 2026-10-28 [Tesla Robotaxi vs Waymo: 438K Miles vs 7x Gap [2026]](https://news.google.com/rss/articles/CBMie0FVX3lxTFBxSkpiU0tqbUI1d0RnV2tmT2w2by1KS0YwaEpndTdhcGItQXpaZm5vXzJQZ2NScFVyOG0ySXJqQ005VWxjaXhsdjE5bldsb201VThfTEltbUtVTDNNdlFzVGdERS0xX3BGcUoyTnYwaDV3VXJROC0tMmwyYw?oc=5) <sub>shattered.io</sub>

</details>

<details><summary><b>Tesla</b> (375)</summary>

- 📰 2026-10-28 [Turo Now Lets You Rent A Tesla With Full Self-Driving](https://news.google.com/rss/articles/CBMidEFVX3lxTE1XdFU4TERHeWU5TU8yRG1naVFxQVBQRll3aEs1Vi1iY3VYNGZkN29PTVJsRjlfSS1ZanZQVXBsTUxJT3kwRXJqTHRjUWdKOTZrRHNxSXQxQVlDWU1pUVplYTV5MnlQVjAxcjRqRFd0Z2Z3b2c2?oc=5) <sub>Motor1.com</sub>
- 📰 2026-10-28 [Waymo vs Tesla Robotaxi [2026]: 7x Gap, Waymo Wins](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPR0d1dUh6eEJFLWJSYzJMY0UyZkhOdGhjaGJLdWFVYWRsYWdZOGpaYmZDZUJLMXhtdVNoTF9SWDVfSUptRVZIMDBPWFdTU0twOV9oNDdObHdpTHBfN3Y0MDdKWTEwekd1ZHVuWG1NeDQzNDBhei1Vd3VQRm9MLWNEZDVvbFdLaFNt?oc=5) <sub>tech-insider.org</sub>
- 📰 2026-10-28 [Elon Musk Says Tesla Robotaxi Expansion to Miami, Tampa Beaches Is ‘Coming Soon’ After Ron DeSantis’ Call](https://news.google.com/rss/articles/CBMi_AFBVV95cUxNeTdvWHJEdl83eGx5UXU0cWtXc2FLeTFGZDFJS2NRZENVNkMzSkNpYkp1Z2o3czd4a0VlX0RKalhuQ0N5WXVUcHVqdE96U3RrTjFIMmZDSEFrU1pGTHNyRExEdmRJUEp3Y0NjX24zY3VUekFIMmRuVUtRTHB0QTRzSGlzLTVJS2dsbmJ0NFZ0ckZqM2xBT2o4VmdfQldVbHNHR0ZPcnNtR0lZWGR0UkxIc0dTMU5QWVNRT0FNRVlXWm9DNlN6OG1IRVJpNlh1Xzc3V3RqTFBlRmJLWktVaFJ2TEdiSTJzQ1Z0MkpSS2lZQVNXSjI3ejJacUota3Q?oc=5) <sub>Benzinga</sub>
- 📰 2026-10-28 [Tesla Robotaxi vs Waymo: 438K Miles vs 7x Gap [2026]](https://news.google.com/rss/articles/CBMie0FVX3lxTFBxSkpiU0tqbUI1d0RnV2tmT2w2by1KS0YwaEpndTdhcGItQXpaZm5vXzJQZ2NScFVyOG0ySXJqQ005VWxjaXhsdjE5bldsb201VThfTEltbUtVTDNNdlFzVGdERS0xX3BGcUoyTnYwaDV3VXJROC0tMmwyYw?oc=5) <sub>shattered.io</sub>
- 📰 2026-10-28 [Cybercab Battery: 4 Sealed Modules, LFP Room [2026]](https://news.google.com/rss/articles/CBMihgFBVV95cUxPNEZ5RGhWbWhyUnhfdlVma3BTVHZFalRSZ0JsSmJxVXdRMy1FNnVmNkd3eGlVeHp0ZXI2bU01WlJyQ2M2MnlyMndPX2gyaVdDN3Y0am91ZE8xUFZYRm1kVjNmSmc3elNZS0F6bFRoNlBnZE43Q25ucXdvay1DN1VJeHJJbVFmdw?oc=5) <sub>https://tech-insider.org/</sub>

</details>

<details><summary><b>NVIDIA</b> (258)</summary>

- 💻 2026-10-20 [NVIDIA/flare-local-inference](https://github.com/NVIDIA/flare-local-inference) <sub>GitHub</sub>
- 📰 2026-10-28 [Google Cloud and NVIDIA unveil Vera Rubin AI systems and new sovereign cloud tools](https://news.google.com/rss/articles/CBMiwAFBVV95cUxPUkxHUjZ2YVpiSUFiQktPemJQdG1SOTBFNEpEWUtZM1JMcXdmQmkzNXJJbjZnM0RBNmQ3TnVlZms3SE5KWDlsenlnZFpSTEZnN1djRnRLLUFqbjAzeEZwTjdPcjlTNk9rRzR4Uy12RjdkdlV1RUV5amJ3SllqUm1fc1pOcmFhUnc1TVJBa1cyUXAzR2lnUExIbmVGdlNzX1duUFczTVQwYWVNalI5RlR2dVhkMGJVSS1wbnJSbVV4Rk8?oc=5) <sub>EdTech Innovation Hub</sub>
- 📰 2026-10-28 [Palit Says GALAX Is Going Nowhere and Continues To Operate As Usual, Though Recent GPU Shortages Drive Uncertaintity For Smaller Brands](https://news.google.com/rss/articles/CBMikwFBVV95cUxNSkNVNXE3MzJpM3c0MDIySGg5LXZRdnlqS25Gb1FmN2xPYVlYdGFDRGsycGtyNXFrcHRTMVdGT1FkdFdHNHBIWDB5QUFyallPZlVSZHZwMG9wcnJ4aEpteTY2N1ZSMk9kS1Npd245aVQwSTY1dVdLclZVV2lZZkRnc0NhLTliRGlJZ2RXdXlQYzJhSFXSAZMBQVVfeXFMTUpDVTVxNzMyaTN3NDAyMkhoOS12UXZ5aktuRm9RZjdsT2FZWHRhQ0RrMnBrcjVxa3B0UzFXRk9RZHRXRzRwSFgweUFBcmpZT2ZVUmR2cDBvcHJyeGhKbXk2NjdWUjJPZEtTaXduOWlUMEk2NXVXS3JWVVdpWWZEZ3NDYS05YkRpSWdkV3V5UGMyYUhV?oc=5) <sub>Wccftech</sub>
- 📰 2026-10-27 [51World wins Nvidia’s nod. Now it just needs to translate that to sales](https://news.google.com/rss/articles/CBMingFBVV95cUxOSV9nbDF6SkVSRENoU05ybXBUeTJrbUpoVmVLamI5N0FidWlfVmJyb0xSUXZmeXY3Q0VRTVlhdjhwanJ2VGNDc2xQVkRRMGZjOEtLSjU3RjB0ZF90VFF1QzluODNfek40WktzVlVMeEtKdWV6QmJXbC0zRkJJQUhhU3NzMVlQb2NxYVlYZDQ2amw1Mm44Q2RtS19wWVExUQ?oc=5) <sub>Bamboo Works</sub>
- 📰 2026-10-27 [Wayve, Stellantis, NVIDIA Collaborate on Autonomous Vehicles in France](https://news.google.com/rss/articles/CBMi9AFBVV95cUxOX3MxQjhfdGRNclQ0QnNRenVlZ183TTZjRkt1ODdJNS1zUWJySUZxaVlBN1RwYmduZV9IUFNoeVJtRVc5UVNqeHgyM1FyVXA4RzNjV1dQTkE2QmNucVl3ZTRiUDRua01pV2VTNVN1X1hPbXdNeTFYTllIamVfUVRjOEpINWVUTk1JTkdVQjNBV2RPN19aZjdKMVMzTjd6aTR3Z0hZbXN0bzhzeGFGdGhoUGR4RzhldVBYNzBFV1BwYkN3RUdLc1pSbjRTQlZkU1Z0Z1pWRWJGYzZMZGRRTGUxTDZyczlmeWdrekZ6bnBrSEdJemZf?oc=5) <sub>Fuel Cells Works</sub>

</details>

<details><summary><b>Wayve</b> (63)</summary>

- 📰 2026-10-27 [Wayve, Stellantis, NVIDIA Collaborate on Autonomous Vehicles in France](https://news.google.com/rss/articles/CBMi9AFBVV95cUxOX3MxQjhfdGRNclQ0QnNRenVlZ183TTZjRkt1ODdJNS1zUWJySUZxaVlBN1RwYmduZV9IUFNoeVJtRVc5UVNqeHgyM1FyVXA4RzNjV1dQTkE2QmNucVl3ZTRiUDRua01pV2VTNVN1X1hPbXdNeTFYTllIamVfUVRjOEpINWVUTk1JTkdVQjNBV2RPN19aZjdKMVMzTjd6aTR3Z0hZbXN0bzhzeGFGdGhoUGR4RzhldVBYNzBFV1BwYkN3RUdLc1pSbjRTQlZkU1Z0Z1pWRWJGYzZMZGRRTGUxTDZyczlmeWdrekZ6bnBrSEdJemZf?oc=5) <sub>Fuel Cells Works</sub>
- 📰 2026-10-27 [German taxi operator MTZ to deploy up to 500 autonomous taxis under Tensor deal](https://news.google.com/rss/articles/CBMihwFBVV95cUxPZEQ4ajZ1cmxOUlNlVE1VYkh3U2UwRDVWbGhKVk9LdnVOLThzYXBhQzRhUWp3LWdqOFBvUFRoZUtPX1FmdVVQT3FxVkJJZS0yTTdrQ0p0Q3FUdTVicEpPWHpmUHNZXzQ2OGxKQV9kcFVscFkzYllkZ3FaQXlMQmUwcEN3WUk1M2c?oc=5) <sub>Yahoo Finance UK</sub>
- 📰 2026-10-26 [Artificial Intelligence (AI) in Self-Driving Cars Analyzes Market Trends, Segment Details, and Business Strategies](https://news.google.com/rss/articles/CBMi5wFBVV95cUxQWlhEWWpObzFXTGlGUkhkdEJVc2otRWFLX3pSdU5rSHJmRFN0dWQ2NTd3djNvNEM4bjFzUDZqMFpuMXBBc1ZORkNaNU1QZm9sdE41b01XVXlaTE1TRk5PMnBWNjlUdlFreVNBLVJDZVN6VTdSOXdxdXZPOXRmX25iRVlOZ0xrSG5iLTRpZGoxTlpodTVGQ2RtLTdHSjVkeTFXNHZEOXRpek9qb0MtVzVnNDdoYUhVTnBaaElndl93MEZvdzhxclBNSlF5VUl4eGJhdXBsU0ZRVnlFMkd4VGF3eE9kaDdxdm8?oc=5) <sub>EIN News</sub>
- 📰 2026-10-26 [Wayve, NVIDIA and Stellantis Join Forces to Advance Autonomous Driving in France](https://news.google.com/rss/articles/CBMiuwFBVV95cUxQZi1zNFE1VmJRREREX2NoaEY3ZUNwWjJRV0llVXI1SDhUanVISUtlS2xkRG9YSnFRVGVJdEVEMjdBUUNOQ3ZOazQ3MzRvRFVESllhSlNHUkhZempoTk9vaUZkTk9tcTN5Nl9wR0gyeHE2YXNqWk03OHJkNnBvdFpaR3QyWDV6X25US2JTczFjZnI2YV9XWG5TVEpmWlc1eDZGcHY2UVRsckNzMTNBaGl2UDNyLVZ5OWI1RjdV?oc=5) <sub>Electric Cars Report</sub>
- 📰 2026-10-26 [Autonomous vehicle: the state wants to move from testing to services](https://news.google.com/rss/articles/CBMid0FVX3lxTFBxN1AtYjRQZHZzdTdRaUVVRUltTnJ5REI5OGlld3NPUk53cU90T2wxQUYyMHgzMmcxSHRRWU1EUkFsUXZUaFhZQjd2NTAxekRjdkk2MTBpMUF1UUp4NzJFVlZBLU5IUXpCcjJXV1pSLUFXVkdrOTEw?oc=5) <sub>Flottes Automobiles</sub>

</details>

<details><summary><b>Momenta</b> (113)</summary>

- 📰 2026-10-28 [新世代宝马i3即将上市，更新Momenta R7双脑协同](https://news.google.com/rss/articles/CBMiW0FVX3lxTFA3ckFjamZVbkVSN2VqcU04akxNYmhMRUtEQW1FYS1yZVNPMEQxUzhjdWRiQ2NPcTFUTDVWcmQxLXpJN05MckxMNlNqOVdiQjJ4TnZSXzN0U05DVFk?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-28 [700TOPS算力满血上车！东风风神L8+把高阶辅助驾驶打到15万级](https://news.google.com/rss/articles/CBMijAFBVV95cUxNQ2t1Wi1JNjZQclZWbWpISEZvcEVncVBIcTFYUGhSWWhOd3RORFFDN1BBMWV3WmU5a2JISmk5SkRNMFZkVDhOb1FxU0JkWk1OZmt0V2dvYTlHRWIzdmxLTmJ0MUFOMjU4b3lnc3NtY0NUWThLQVFtNnk1eGNGOVdkTVdkN0Z4WkViUWdISA?oc=5) <sub>搜狐网</sub>
- 📰 2026-10-27 [【视频】大型SUV销量惨淡？增程+智驾让ID.ERA 9X翻盘](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1KaWNVY1BseFlNNHB1VWhHNDJ3ZGZuajM1aDdZVVh2amhLSHNMMUVmMjBmMGE3eU4wMVBPUkNud2ZHb3ZCeFhFN0p1UFBLV3ZZei1vbFhuanB1STg?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-27 [带激光雷达的豪华插混SUV哪款好？全新XT5 PHEV与腾势N9、领克08激光版智驾横评+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFBUUnctbUptOFdFWlhnZkplTWg1STNrMkFndFdIejRCUjNUeFJ0WC1UaE5HeUd6VTdEelQ3d2FJVTFGUGc1cjRwc2xiaG0tSm9MemZXT3BZYl83eHRmNHNlM1JwTFBqa0E1VFl1NW1hbTAzZw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-27 [【视频】Momenta AI Car 雨夜实测，告别死板口令，语音就能操控整车](https://news.google.com/rss/articles/CBMiW0FVX3lxTE04WVh1bXBDTUpHOWRwSkh1TlpsYm5BWGRtd2RsVmFRT0FMUFBEenhCV05mSzVlMWtmbURvZ3NaNHlBUFU3VWxqTDNpcFluLU8xM1ppZjFUbUwwaE0?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>XPeng</b> (241)</summary>

- 📰 2026-10-28 [智舱与智驾谁更全能？小鹏G9L、智界R7、理想L6、蔚来ES6大五座智能体验盘点](https://news.google.com/rss/articles/CBMickFVX3lxTE4zMnRjandNcDUzS19CcVhMUVNUT0pNbTRaMHJ2TFUtQ1JuRDJnZ2lwWWpPMm80bE1JSHJ1Z3FfMHJ2OXRycXZidFFfUjI4NFF4WXRUMVBIeFlwM1d1TUFEcFFwSTJrdzZqU3NHS01tMGtfdw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-28 [舱驾一体不是口号，小鹏G9L与智界R7、理想L6、极氪7X智能大五座SUV横评](https://news.google.com/rss/articles/CBMickFVX3lxTE9Jakw5NUI1X2RzSmlBWGVDSk01MDFuMFk5UjVlU0lGZXZqdi11ZTNyYl9HTldWX1FkbDFIQjR5aEVpT2xJT0N1V3EzVjhwVE16RlRxbjRBcm0yaUkwMDUzZU9UTjNyblNDdDBKaFlPTGtvQQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-28 [【图】小鹏MONA L05将于10月29日上市 预售16.98万起 增程+纯电中型SUV](https://news.google.com/rss/articles/CBMiYkFVX3lxTE5xQWh1bHlnQVE0RFJVV2pOU2ZwZERRUmtDcG9TN3Y4dmpMMjVGZWtUVWhhYThwM3c5amVYM1NpNmdFWGlyRXZ5TEJPRVZmOGIzeWZWUjdGSWxsUlRQSjA3UXln?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-27 [【视频】VLA智驾丝滑博弈，小鹏MONA L05纯电续航真能打？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE95YS1HU0tTYTlYQ3hobG94Nm04dU1RYXN5a18yWE96VXU4ZF9pNy1IUnNmUURyaVpTcng1bWJMZEdvV3VDblZ1QUVSR0g2c0RCVkxGRnRoNWMyLW8?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-27 [25万预算新能源SUV横评：小鹏G9L与理想L6、问界M6、乐道L80同台较量](https://news.google.com/rss/articles/CBMickFVX3lxTE9ST2xSMXJ0NzJhcldLdmF0ZWRUbWIya2dqdEd3eTlHbVp4Rkk2RmZVRmZlNFo2dVVYS2NISnVfSlM0dnNiYWw0Z3ktLU4tWFUtaWhLM091dWdYOE9kdVlybUdIYlpRTzNrMHFwbzRTRUI0QQ?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>Li Auto</b> (147)</summary>

- 📰 2026-10-28 [智舱与智驾谁更全能？小鹏G9L、智界R7、理想L6、蔚来ES6大五座智能体验盘点](https://news.google.com/rss/articles/CBMickFVX3lxTE4zMnRjandNcDUzS19CcVhMUVNUT0pNbTRaMHJ2TFUtQ1JuRDJnZ2lwWWpPMm80bE1JSHJ1Z3FfMHJ2OXRycXZidFFfUjI4NFF4WXRUMVBIeFlwM1d1TUFEcFFwSTJrdzZqU3NHS01tMGtfdw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-28 [【视频】理想汽车理想L7 2024款 Pro](https://news.google.com/rss/articles/CBMia0FVX3lxTE9jeFBOMlU0QWRYdWtPWC1YRkc5TDFfbmFnR0NsWmNINF9lZXlhdXNjN0x5NmZBY1J4bVVPR2dpendmV29CbHlCczFXNlpIalYzSDhEaG5tbzZoeTdOdE8ydllVNERaZUhxVHBz?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-27 [25万预算新能源SUV横评：小鹏G9L与理想L6、问界M6、乐道L80同台较量](https://news.google.com/rss/articles/CBMickFVX3lxTE9ST2xSMXJ0NzJhcldLdmF0ZWRUbWIya2dqdEd3eTlHbVp4Rkk2RmZVRmZlNFo2dVVYS2NISnVfSlM0dnNiYWw0Z3ktLU4tWFUtaWhLM091dWdYOE9kdVlybUdIYlpRTzNrMHFwbzRTRUI0QQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-27 [Why This Global Auto Parts Giant Is Venturing Beyond Core Business into the Robotics Sector](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1FV1p6VGVFS1NpeHFMWGktZEY3U0N6QTZtalUwQzl2MlZOSlE3SEhISzRRbWhXR1dySzRVNHh3MUFTekphWUd3ZTA0cGpIYmptTXNj?oc=5) <sub>eu.36kr.com</sub>
- 📰 2026-10-27 [BYD God’s Eye Avoids Collisions in Night-Time Emergencies](https://news.google.com/rss/articles/CBMiqgFBVV95cUxOS0dhRmdLYlhkTUk5azA4SlFOUVVEMndMZm0yRkFtS1FLem11ZjdtWGc4ZkRLdjRkTU9oVDlFZnN5eTRXUjU5Y1ZfblJlUWdsSFpBYlVzbE9nSk1xMmxZR0dMUE5GRzVHSnlyWGktdGpDU2JIT2dLLVVMZ1gtRlRqeXEtQmc1ZWkyQTFvS1ZRLTFCN29WTFRkd0x5ckFoNUtiN1dPMVVlMUJDZw?oc=5) <sub>Electric Vehicles</sub>

</details>

<details><summary><b>NIO</b> (149)</summary>

- 📰 2026-10-28 [智舱与智驾谁更全能？小鹏G9L、智界R7、理想L6、蔚来ES6大五座智能体验盘点](https://news.google.com/rss/articles/CBMickFVX3lxTE4zMnRjandNcDUzS19CcVhMUVNUT0pNbTRaMHJ2TFUtQ1JuRDJnZ2lwWWpPMm80bE1JSHJ1Z3FfMHJ2OXRycXZidFFfUjI4NFF4WXRUMVBIeFlwM1d1TUFEcFFwSTJrdzZqU3NHS01tMGtfdw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-28 [【视频】贵1.18万就为紫色？蔚来EC6灵韵特别版值不值](https://news.google.com/rss/articles/CBMiW0FVX3lxTFA2M2xFVldvelEyb0xJdExyZWdWQVlkaFRkMFQxcDZNSWNKaHNPUmU3TmFxR0REYmVKc2Zlb1VYNFN5bm5GNXA3Wjk4MVZ2R2pqSG9QdzNuU2cxYzg?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-27 [【视频】蔚来ES6 2020款 600KM 运动版](https://news.google.com/rss/articles/CBMia0FVX3lxTE0tNzZYN3Y0cXQ2bU81SWRidHdRV19zT1UzRVl4VUotMXZCbGZqWDZXN2pFT3VrS1l3UnFxTHhDUlNFTnRLTWNsZXk0cndfREhxWGxabDFCRzJZRjhDeHowUmJHNVJ5OGxMV2FB?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-27 [Volkswagen begins Level 3 autonomous driving road tests in east China](https://news.google.com/rss/articles/CBMiWEFVX3lxTE15ZDdlV2V3MFBxSWxCd251LWRMUmp6RVRrZW9DNFpSUndWcW5Yb0Y3NWFlRGlZQlQtMF9mclVtbGR4SVlRUDliY0xRaEd4UXBmc0RockFOTXk?oc=5) <sub>chinadailyhk</sub>
- 📰 2026-10-27 [Nio ET5 Takes On Changsha’s Night Traffic in Four-City Smart Driving Test](https://news.google.com/rss/articles/CBMivwFBVV95cUxQb0RraDB6NkZRYW1GRU5IaWpoajVZVmc1TUIxM0FlNHVqYjNzSGdvRzdXdkdnMm52ckhvNDNqNUdwbEtvcXZYX2cwaGRoZzlHMlN4Z1p5SHZSbHdyaE5nLXJVbnZ5YURES0Rhb0x5cFF4NlpGdEZXSUlrSEtucTVsZ18tX2R5c2xmdVpXNjBrNEFCbWVoSDIzWnY5WWQ2VFliYjduSndybjFuXzh4Vl9kM1g4N3pDeHlKNEdVZUJ6OA?oc=5) <sub>Electric Vehicles</sub>

</details>

<details><summary><b>Huawei</b> (338)</summary>

- 📰 2026-10-28 [Exercise-Responsive Blood Pressure Monitoring](https://news.google.com/rss/articles/CBMihwFBVV95cUxPT1JSYUtXSm9xSjRIV01WQnJKWkNIbjU4eGo0OTUzajhIMTQtVURyajZTNlVzSjQtUlJtcUlCZ3l5YTN2Q1o5U2VDeHlBa0NDRjBVVlJkNU5GV09MVlRWalI3NUZnUExiTlFIZjczcmR3SmhOei1qQWxZcTRLWno2V0tDSkwxdkk?oc=5) <sub>Trend Hunter</sub>
- 📰 2026-10-28 [HUAWEI Watch GT 7 Pro Review: Built for the Wild, Ready for the Slopes](https://news.google.com/rss/articles/CBMiqwFBVV95cUxPTUNBV0tzSGJpN01IOHlvai00RXpFZ2lZTXg5NnItZ0p2Mnc5SE1wMVlndldkRVBfU3o2YlVKQW0xNWtlcU0tQmJ2aEpTRjV6NFNzUjRLR1pXUEpIei1PUFVkMkxENzdKb0dPUHlUd1pnSXBEQWdFU056Y1BtcHZxakpTZkZia3dwUTZhT1diZGtiaXJRS05MN3hSTmZ2eEpiR3EtWGdsNXhVMTQ?oc=5) <sub>Gizmochina</sub>
- 📰 2026-10-28 [新款真的更好吗如果2024款知音只要13.39万呢_热点推荐](https://news.google.com/rss/articles/CBMiYEFVX3lxTE1zanpUUzlYZXZ2dDRPNENkTnFLWl9lbS1CVGVQOXRtZWZxME9kWkU4QXZpWnZ2Y3FvM1lDckppcHlZVzBfcHBiSmtXeUhVdlZ1aVI2Q0JfOV9hNTJfLXB1WA?oc=5) <sub>证券之星</sub>
- 📰 2026-10-28 [40万豪华MPV横评新视角：四款车型舒适、智能与安全配置全解析](https://news.google.com/rss/articles/CBMickFVX3lxTFBsWmY3dzBPckNPX1F4QzQ4bDRVdGdkeE1neWdRMkNKdm51eUktZHktSDZrWVFLTlhxRHJySEhxcFN4QUV1ekJTLUxUbGdGMnlvdGM1bFhWdlQ5NkZxQXdQUFk3M19TRy1yWjhvSjhGTFc3UQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-28 [2026年30万内城市辅助驾驶SUV怎么选](https://news.google.com/rss/articles/CBMia0FVX3lxTE5XdUhXTl9lSk9zNGpLVTF3VXJzeDAwV2c5TDFUZUdpQV9IZ2ZvYWdvcGNGUC10NlJrNHNXckhLSVJZUnJqQTU0NkNhNzE3U3AxV2pYbnZGakdhS1k0aDFkNm1rSFFJc1dCcFdv?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Baidu Apollo</b> (56)</summary>

- 📰 2026-10-28 [Baidu reportedly developing world model as autonomous-driving ambitions expand](https://news.google.com/rss/articles/CBMisAFBVV95cUxNX3d2TEVkQU1HN2ZRSFZJMkJaeEpCV0lLMXJvMDNCdWZXd0FzaVd2dlUxOFFDeHZ5bEQyNlpiUUtQTVN5elpUOWd5Q1NBTFh5UjFSYzdzcWFacWdVdDZMMWY5ODJkOE1XY3p3M3BjcU9BODNWajd1eVJaeFlhZG9rNVd0Y0ZaSzNhVXBlbGd1bjRKQXpVb20teHRpRGVTbm85VkZTZjFnU1huVktMQTVXbA?oc=5) <sub>TechNode</sub>
- 📰 2026-10-28 [百度计划近日披露世界模型研发进展 萝卜快跑已覆盖全球28座城市](https://news.google.com/rss/articles/CBMiTkFVX3lxTE5qV3RzLWVJQkxjMFhaZ0FHY0ppUXJEcTBOYURjOEhmSnp2cjNqYk1uSnRMb3lqWV9RTXhpU0xpT3ppRGxNV1pSSlZNQnJwUQ?oc=5) <sub>观点网</sub>
- 📰 2026-10-27 [China grants permits to VW joint venture, Xpeng as driverless car race builds](https://news.google.com/rss/articles/CBMi0AFBVV95cUxQUXhrSEV2YmVIR3NxVXoxek9IalBnanhBTFY3TXpDRE5lMlo3Q2RpM2Vudm1CMGw5dWlwNDE4VW5KREg0Nm9wXzlhd0x6aGc5cTdoeFdxcFZnZ1U5QjA3bkZocXBNcnFtNVZTaWZMa2N3bVF6eXVJMUh5S1lxMGJNaEdiTGRzMm04SmkwMFBsR2RKanhzZmI5WXpCOHd2cDIzVENfaFhOcDh4OHE0eUp4VnI0SjRiMXpZRWZETTRod0xrLXA1dEd4MlM0QUs5ZjQ30gHQAUFVX3lxTFBReGtIRXZiZUhHc3FVejF6T0hqUGdqeEFMVjdNekNETmUyWjdDZGkzZW52bUIwbDl1aXA0MThVbkpESDQ2b3BfOWF3THpoZzlxN2h4V3FwVmdnVTlCMDduRmhxcE1ycW01VlNpZkxrY3dtUXp5dUkxSHlLWXEwYk1oR2JMZHMybThKaTAwUGxHZEpqeHNmYjlZekI4d3ZwMjNUQ19oWE5wOHg4cTR5SnhWcjRKNGIxellFZkRNNGh3TGstcDV0R3gyUzRBSzlmNDc?oc=5) <sub>South China Morning Post</sub>
- 📰 2026-10-27 [Baidu and Lyft target 2027 for driverless London service](https://news.google.com/rss/articles/CBMimgFBVV95cUxOZmZiZkFzbnlPNUIzRXA0djJpdnBWdEIzTGxoWS1FeUZYOU84dlppYUdsSVhTUWU3NEIzZFBkTnA1LVlxSlhsMUpBcU9VT3RJbllJN2wwSG12WWI4bUpQQ29QYjNuTzRPU2s2WkxjakEyb3l2T1RJOV9JSjdOSE54MkZjcTYta21KNm1Yb245VjZydzZ1dHpvZDdR?oc=5) <sub>Automotive World</sub>
- 📰 2026-10-27 [Baidu: An Asymmetric Risk-Reward Opportunity With Multiple Re-Rating Catalysts (BIDU)](https://news.google.com/rss/articles/CBMiugFBVV95cUxNTUxZTXFfRml6ZEVwQWxvamZJOC1sZHA2eGdyYVVNb3RVNjJIWmNXcmNDRjdKckp0endrbldza2J6QWpfNTdCYjR3em9ENkNOWUNCSnFqT0ZkbHFMX0NFLXRnaHY3WVF4eWNpV3RMOUp3dkt5SlZFcUhOLS1OeFBjLThIRkpQM3ZqR3Z1YjVSX1RhWGNPdFBQWktkLXUybmtWMlNOaktFWUlHZGtUcFp3c2V0OUJ6aXczZGc?oc=5) <sub>Seeking Alpha</sub>

</details>

<details><summary><b>Pony.ai</b> (145)</summary>

- 📰 2026-10-28 [Chinese Tech Firms Confident in Challenging NVIDIA, Tesla](https://news.google.com/rss/articles/CBMijgFBVV95cUxQUmdRcGZwbDBHSl9fc1QtQVdtWGNYcFpzSm1IWERfZHhKMGhoSlVrVWJDOV9lNVRlUm4zdHJwWmZfblFRT1BxSlBIT1FpcndiZ1oxQmptRVFySkpqT0ZvcVFaVzBfcDVmcG5OeDFmTXgtV2p3UEZzNzFIeGl1YWxqNldwZmViTTNTSVhveVZn?oc=5) <sub>조선일보</sub>
- 📰 2026-10-28 [Chinese Tech Firms Surge on Domestic Markets, Narrowing Semiconductor Gap](https://news.google.com/rss/articles/CBMijgFBVV95cUxOWXhnUG43eTBrWTd0Q1BhdTRockRmX0QzeGhxSjlBeWRxRE9FQjlBRlFwNldGQ2FGYXBLRmRQOFRlSDJycVZaUGVFWG5tYWp1OVFiNU5zZ2lGY3RxQ1F0RW1MMVdPRW10bk9US25UbndhS2RwcGUwVEhNMVVDQS11QnFQT3cwNTc3ZVhEcDNB?oc=5) <sub>조선일보</sub>
- 📰 2026-10-27 [小马智行在武汉成立新科技公司，注册资本500万](https://news.google.com/rss/articles/CBMiWEFVX3lxTE1kQ2hCS2huaVk4NE52R2w0WE5OWVZZelpZeXlKekt4SWRkQ1RwaGlzalpVb0lMZFZCYWYxazZ4NnQtczZZczBtRjJtY2RkM09zSXFqN254RUo?oc=5) <sub>36Kr</sub>
- 📰 2026-10-27 [中概股多数上涨，纳斯达克中国金龙指数涨0.63%](https://news.google.com/rss/articles/CBMigwFBVV95cUxPNE43RlBManEzNmx2NmNmV2tMY1l2aXBBNG4wbG1QYzYzZE5sa3ZvXzNuR2M3TzdpUVBqU3RGQ3JiSUxNSXVTX3NLai1yT3h3TDJyRUJqcTRJOG1FT1lNbzdmOTlfQk1mbDZVUWY3VGtvUDBWSUpoV08yZTBtbDVXZWo5TQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-27 [Pony.ai Partners with inDrive and NVIDIA for Robotaxi Pilot in Kazakhstan](https://news.google.com/rss/articles/CBMizwFBVV95cUxQOXMxRW5aUzR0cEdTQ2dBSFZ3NWNSQUE2SFhlbTBObjZTZ0E4dXVaTXE4NFcydVJqSU9tbmNvUVlWMS01aWVwbzh3aFgtaVZLdVhFazVhV0p3eHE5NGozRFpzc2hTS0stYko0WlN4Rnc4akJwQVNBeTRKcXJiWVBjSjkzZk16UXVrQTNkWi02WWNObG1oSWh3Yk5IZFZEQnE1OF9oMGlYbDg3dXduQ2dGV3dsMy12TlhPSXRrRFZLa0tqRUVBM3ZzbE00UWRsdFk?oc=5) <sub>Gasgoo</sub>

</details>

<details><summary><b>WeRide</b> (139)</summary>

- 📰 2026-10-28 [WeRide Unveils Global Insurance Partnership Program to Scale Autonomous Vehicles Worldwide](https://news.google.com/rss/articles/CBMi1wFBVV95cUxOTU1hZ21vOXRFS1cwVDR0SHFnTDdTOHZKYjUtUm9OcF94c2xmQndfUTRmb0ZOUWZ5WktzTlZrZ1hNMlc0NWx0Mm80ZUJieDNyOXFHRGdxb3ZKVEJkZEtBSnVpTFJCMjh0NVZJLTlLTnFZc292QW1FWENpTkNSWjFRZVd1T2RicXdybDhGSS1QZV9Wd0Q4QzZqZFFEdlJHR3czNjZQUG5Ickk3cTdzZFRVR18yckxpRnl0dDdfVF9SMXJzbGFZYjNsclFDME9KT21PZlp6V0FnNA?oc=5) <sub>Detroit Free Press</sub>
- 📰 2026-10-28 [WeRide launches global insurance program with A...](https://news.google.com/rss/articles/CBMirgFBVV95cUxQWldwcEM4NHBHMWhhNVZiUkcxaElVbkh4RFBjOHVvaklIUzdlbUFXblZOdnkzLUNRWTd3ODhSVDRLVUVLVUMxT1FpeWMwb0hJMzQwOE9TeDh5Ry0zTDdXSFc3ZGhuVS1iNm14WkRYbS0tMlFfc2ZmYkZXZ1BGak1jYmd6NlZCSUExUjZ6bkhHX185SjYzNkc5V1hoYWtEYnhYcnhzd3R1TW0xdTJPR2c?oc=5) <sub>Pluang</sub>
- 📰 2026-10-28 [文远知行-W（00800）涨超7% 启动自动驾驶全球保险合作计划-证券之星](https://news.google.com/rss/articles/CBMiXkFVX3lxTFA4dHdCdzBqSmlKaDJIaExHMERnRVRGMWY3Q3llQl92WElRWGhOMHMzd0FkYUxycFJfUnI5WVFtc053eU9Welp5UWI0R1JVdzAyZDVpalYyVkdLX1EycVE?oc=5) <sub>证券之星</sub>
- 📰 2026-10-27 [Chery boss questions future of car ownership amid rise of robotaxis](https://news.google.com/rss/articles/CBMiqAFBVV95cUxNRzlPeG5kd29XbUdaWXRDc2Jhb010bEJxakwydHNFbmZRSDQwTVYyQ21KVEFSaHFULXY1dzRSMHFvSm15VC1KS0hCYmxjNTctYlFWaDU2VTQ5ajViVXlGVkZoeGdoV0hkbWlkSEctbVg4LUtFY2lGUkljTGhEYlk5bFAtVzFhTTkybFJhdm1YekEzUmRpakVxd3c2LVU3WU5sVDk4aTRiQV8?oc=5) <sub>CarExpert</sub>
- 📰 2026-10-27 [China has successively granted permits for autonomous driving operations to EV maker XPeng and Volks..](https://news.google.com/rss/articles/CBMiT0FVX3lxTE5xbERHUURWVUZOeV9sUzFXbXRwdDNndERiVGphQk9ka2hneWd2MDItWmZ1Q09aRTNENjV1LWZaVG5CMkl5ZzhmMU5jOTVZMXM?oc=5) <sub>매일경제</sub>

</details>

<details><summary><b>Horizon Robotics</b> (159)</summary>

- 📰 2026-10-28 [德国总统访问大众合肥基地，亲身试驾在华自主研发电动汽车 10月27日，德国总统施泰因迈尔访华首站走进大众合肥研发中心，试驾在华本土研发的智驾电动车ID.AURA T6，并在下车后体验手机遥控泊车。该车型搭载大众与小鹏联合开发的CEA架构，以及大众与地平](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNWDhOemd5T3BhT3dnQ1RpMDdJMmN4LVFiRk5SU1ZSb25LSVoxazhpd1p5U285RlF5eVlFcHdvTURBLXAyaGpTUlQ3WEk2WUU2VVNpR2FMdzZ3cmVmVmI0SlcxeHo3OXZ3cjhpZEk5MHE3d3p3Sy1EVTd2OFNNQ3NIMkFZbEI0WHph?oc=5) <sub>搜狐网</sub>
- 📰 2026-10-28 [韩国KOSPI指数涨幅扩大至6%](https://news.google.com/rss/articles/CBMifkFVX3lxTE92dGFMSmQ0V05pOEtpVXFWNWtqOGJMakJjb2FuNExOZ2VuaW9yajl1Y1QxQ0ttRk4yRmpIeEhDdXdFQXA1bU9jUkJRUXhZVGY2ZDZYU3lVRlMyWTVKOTMtS3BOcTB3WFQ3SG9sVVFTZzBuNWtlWVZnMmJSY1ROQQ?oc=5) <sub>东方财富</sub>
- 📰 2026-10-27 [Volkswagen Secures L3 Autonomous Road Test Permit in Hefei](https://news.google.com/rss/articles/CBMiigFBVV95cUxOSDN3dHN0Tm5nR3pQTm1zdmdoR1hDaEJXY1FHVlQzWjV6OTFMM1hRaHh5Skx1RGFwQ1ZteU1WaUZXa09oY3J5cnpoREZQUWJfUkFrNmlWT1dsSHhyUFEzSWxQZm15RjVYbUlUT2E0ZE1jM3NJVTFITXJYRlJOQXRWSFIzNC1rcnZGREE?oc=5) <sub>Retail News Asia</sub>
- 📰 2026-10-27 [25万预算能买到什么？小鹏G9L与3款热门大五座SUV配置横评](https://news.google.com/rss/articles/CBMickFVX3lxTFA0NzBHQV9UMkttTjJoaUIzMmZkak9zLW1NaFFCWDF2QThwWUxkRFR0Nk1TWUFldFVkekI2aTBfNnFhVnZ1SHR2S3BiaDVqZ05RbjlSMkhLS3NibGdNQWdhNGhnRmM0WC1JQ015QU8zREI5UQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-27 [CHINA-VOLKSWAGEN-AUTONOMOUS DRIVING-TEST (CN)](https://news.google.com/rss/articles/CBMikwFBVV95cUxOQ2ZBT1E5RjRKc2ZhdmY2cExTdDFBS1dHTkJnZm9FdUhzRWlIOUJCcUJEbUZwUmtScEp2b2gwSDhpR0hKRmtZNmxhQ3REZkgxam1BX2tzX2M4OHEzdDhva0ExMUxncjRnWVFsY2pZeTNrWWE5S3FIdmEteDhTbzA1MXJXRU1qeVUteHBCVVAybkY5WE0?oc=5) <sub>Big News Network.com</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (31)</summary>

- 📰 2026-10-24 [4款7系SUV扎堆上市，问界M7车长5080mm](https://news.google.com/rss/articles/CBMiW0FVX3lxTE14Njc1UEhVa2JDUjZldVh5cm9SaHl2bTB4dE5fQnVEbEpuUE1UTzJQS0dXOU50UjVYYm9IeGwyVFIzQ085QktXaFBvaExySzQ5VFROUnoyY2hCT0U?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-24 [从2026 WICV演讲看：文远、元戎、智驾新程把智驾的下一轮押在哪？](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1UMzkyZlFUZFdhS3l3M1dPYVAxemFzYjRHSFlnWjJUbEVzaDgzRF96VUJiUFhPWTlNdG95czM4NXg1Y0ZlY1JiY2VyV1YxcFZxblpv?oc=5) <sub>电子工程专辑</sub>
- 📰 2026-10-24 [欧拉5城市NOA值得买吗？11.58万带激光雷达，3个维度说清+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE9tdVFPMXpMMGg5UlpDNGt2RzJIMVJ5Slk4dG5SVGJxM0dqaENiNHhVWi1TSWFYTXFuc3VvMXdJMFdHOEY4cUNOcF9peENCbmxFVlVxcDRIMUlUdVdpaTYyWGpaZGY2Q2F1UGxTM1lVU0Zkdw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-23 [元戎启行周光：基座模型成自动驾驶新引擎，推动MPCI向千公里级跃迁](https://news.google.com/rss/articles/CBMiXkFVX3lxTE9wRGVmQ3liVG9hUjNic1QyekVrS3VKVUNZbFJ5WHc2dlR3UHQzdGhCRFVROHVnTl9NLVdENGZIM2hUT1doV01USEtvSHJsaV9iclpoWEd4M1hfVDZFMFE?oc=5) <sub>SmartHey</sub>
- 📰 2026-10-23 [US: Waymo Launches Services to Harry Reid International Airport](https://news.google.com/rss/articles/CBMinAFBVV95cUxOV2M2dkZzWEw4TXdrbU1kMzlPelNRbk5FQU5YbTY1MUNoRUdITmY0a1dzSUZjWE9JdXotNkI5Mkg5RzZQMlZORlM0OUppSVNlc0llbVFMa1NJNHpzLWhEbkl5RC1wSnZsUFNoVDJyUlgxa19OTWVGRFBvMHBIbDlYZllzV3NQMjMwMklTSWp6NWZqaDVuZndFUnpjckg?oc=5) <sub>Future Transport-News</sub>

</details>

<details><summary><b>Mobileye</b> (31)</summary>

- 📰 2026-10-28 [Intel Unveiled Major Acquisition Deal Worth 15.3 Billion Yuan](https://news.google.com/rss/articles/CBMiU0FVX3lxTE90WEEwZWZVeVUxbkZadThjRlhFQU5ZUXh4N1hidkg4a0lzT2NJNEdpalJvUTlxUFZuY1FKMXI4OUprV2JCVk9tcXdUVi1PR05QRS13?oc=5) <sub>36Kr</sub>
- 📰 2026-10-27 [Mobileye Receives TÜV SÜD's First AEB Development and Testing Certificate](https://news.google.com/rss/articles/CBMiywFBVV95cUxPdmgzR2dSY0RSeGRWaHdmRE9XWFNBVi1sQlhNZGFJZUpubFpjZk9qNWtweDRWS3RCZjRlUEZxU1AyR1VDZk5iamdRUE91WWdwd2lVcDdBdG5URXNMOUo0eDF5MWVzb2FVbzVDRjBTY1pHOFBRWDE1aHd2WG1JSDBGcnd2YW9lQmFfVE5PN0FXX3Z3X2RuZEljd2k0MlhRUXc3OUpRVkZxQjc2alJMYmdLYU9IWGFtSlB4cU4zMDl1QTNDeElpTS1UaEV2RQ?oc=5) <sub>Gasgoo</sub>
- 📰 2026-10-27 [Intel To Acquire Israeli Quantum Computing Startup Classiq For $2.3 Billion](https://news.google.com/rss/articles/CBMiqgFBVV95cUxPY0N2azgyaUxFbnp2Y2JDd3piZ3hCeXdZdkZDOUVsdUluY0ExeDZvTjVKemU3MnNnNTRVb2NLek5QV1haczhOZGJMeUp2LWZMV1pKckI5M1ZZSDU0VDQ1VlNONmdCOEYwc2x3QnozaVcyZVNRVUJ4UWh0OEhGaHpXel9GQ2l5NDEyZ1E2VmpWbnhURVk4V0tVcUdsTnprVEFhdk16OFlIZldwQQ?oc=5) <sub>VINnews</sub>
- 📰 2026-10-26 [Autonomous & Self-Driving Vehicle News: Tesla, Mobileye, Aeva, Ouster, Pony.ai, NVIDIA, Stellantis, Bolt, Wayve, Volkswagen, Einride, Valeo, Aptiv & TIER IV \| auto connected car news](https://news.google.com/rss/articles/CBMijgJBVV95cUxNLXpSRDZNWTdpaUNvcWdGUWJBRUxfMGlXTXYtNFEyV0NxU0hfTmhxUlQwb2JGN3Y0VW9QS25NeVRPNkxsVV93ZkZGdGp5bW9iU3VERTFwaW5MckVKc0xmTEJVR1NFTFJORXR5SVZ2VlNDY0VFRjhabEo4dkp4WU1xTFpYci1kcWNsNndSNHg2cExQUVlCRVEtb1plX0dLa2diaDV6eU9hX1dnT1pOTmVkZXBNQ1pnUHlZQ1BVX1FEWWJfcS1fejBXbUdWZE5qZDRDUGtmTnFUZVhYTkItWlN5emwyMnRGNWFITHVDTEZwQk9hdXpJT3d3N2UybExoRjRtLTVZUFE4ZFBZQVZJLXc?oc=5) <sub>AUTO Connected Car News</sub>
- 📰 2026-10-26 [Where Mobileye Global Goes After A 51% Drop](https://news.google.com/rss/articles/CBMiuwFBVV95cUxON1Y4bVE5WURxSnA1RGJCM2p6V01laEViRFhYc3V3aEF2Y1BXZzFaT1dCbVdZVXdBR2RiT281MmJFRkstcEhKZlFSWHhnX2ZTbGVZRjJZOVVDTGctWGh0amdjN09mTVRuZnRoTVFfMzhYOTBBWHpuQ21FNjRsM01meFpzb1dFQUY1RnBnV29GVHFoNmdmTVZLeG10TDNqN3dYdzE1YzZzV19HRHZmb0VZMUY1OHBJVWctelpR?oc=5) <sub>Simply Wall Street</sub>

</details>

<details><summary><b>Aurora</b> (47)</summary>

- 📰 2026-10-27 [Charger Logistics plans 500-strong Aurora driverless fleet](https://news.google.com/rss/articles/CBMinAFBVV95cUxOazJVaVFXTlNlc19UX3NxcFhNVHBWSHFxWTluTWk2STlxeTJtUmZrMHBlVzQ1QmhERll5NS02N1FucGgtVDJRZ3BILXhhVTdqa0RYRGs4MUdkZnNhUHBVd0tQSVF0N1k1TU5MdE1XWEtJbzZ2dmZkSi1rWTIzSXItT2RONGtvMmY4MF9WWnlUSGcwSjRXeVg5bWlzZnE?oc=5) <sub>Automotive World</sub>
- 📰 2026-10-26 [Aurora to sell upwards of 500 driverless trucks to major trucking firm](https://news.google.com/rss/articles/CBMimwFBVV95cUxQODVpVElvVTNvWXl2Qm16VEd2RHJOSHJ5SE1UdTVIOXFsalkzQi0tUVBFVWFUT2tXUzlUcU9MVF9nU19rSUMwSUFtcDRkTXFkX3VyaFlfaGpqNnpIdWtzT2syVVpCbGY1WkU1RGdQeGo0QnVoNTE1RXVuaWpUcnZpMHU5N2l4dHpIOHNqTmhEMk1STWdqX0lpUXJzbw?oc=5) <sub>The Business Journals</sub>
- 📰 2026-10-26 [Aurora targets 30K driverless trucks, $5B revenue in 2030](https://news.google.com/rss/articles/CBMingFBVV95cUxQMGowWW1ZY1dOc1l5RGxoSzN4blg0VlpXeUpWNG5pOGhudmhmSjZaR0pUc3NwYzd3ckQyZUV2bjJqa2JuazItNjgwMTduOG9kU2NIVXg0WGtoYXJxVE8yUkhFQzZVY1JlU3hldVJReWRmVXllMGNIYnFRTzNLRkg1VHE4dDFIdlZJQmRubWN6UkVRemROOGI5OVBQZ2d0dw?oc=5) <sub>Trucking Dive</sub>
- 📰 2026-10-26 [Charger Logistics and Aurora to Begin Scaling Autonomous Fleet to 500 Trucks](https://news.google.com/rss/articles/CBMi1AFBVV95cUxNUnhMUFlGYkttWWNzRHI2RXd2UXZiNDhnYXQwNkRFRFo4YXlCWVFEWU05eTNZUms3MzZIekZvaUhOaTZoYXRHeDZrVGQ2S3U1cjh6S0wtbWdYMXhsbXRVTmxrcW1kY3JoTUxIeWRzaXA0QktlYWJhSC1hYXZCNHRWNUZXT1A4YnBlVkhOMWprV1p4NHVfU25La3FJMW9ublhfcDRPRnBOSFFUS1JaTWVPbEF1eEpLbEh5Sm5SWTRCLVpoTkFaWHNWWEpGSnV0SGhZMW1MYg?oc=5) <sub>Morningstar</sub>
- 📰 2026-10-26 [Charger Logistics plans to buy up to 500 autonomous trucks](https://news.google.com/rss/articles/CBMixgFBVV95cUxPZE0tcXlXT2c5OXU5VjJzU0VOMFZwVWJfdXRhLV9zV2hkU1VGckFUTngtdV85WnVsNWVBQ2tXcjh1OE1KTE9LNlVZNHlMUFF2S2owMHdRQ25lMW1VRElmTzdPUzA2NndBOXZ0MHdMOTJpQkcyVHIxWjhjRVhJeTVIZ0FPTEI2SlRQNlVjNlhvMnV0TTEwNEQ2cDBCUWtPdTcwc0lVVkpxZTBEZ1ZzejJ6dU53RGxiNHlMZVpDWHNIYU5SVThwcHc?oc=5) <sub>DC Velocity</sub>

</details>

<details><summary><b>Zoox</b> (66)</summary>

- 📰 2026-10-28 [Where Are the Cybercabs? Zoox Eyes 150 Cars [2026]](https://news.google.com/rss/articles/CBMikwFBVV95cUxNMUZXQnhZd0ZhcHl4Qi1tbjFKSGxQSlgxY0tPT2pMbmlKZ1pYbVNaQ01WV2hicndLbGZoV0xTRk1iM1IzSHE0U19EZ3BYS3UyZFNYVHN6WmZDeVZPVnU1M085R3I5ZnFkZ2E2SmtPZHo2bnJEOWZHRl94TXpIZGxPbVBfelJQUHoyU1hSZ3BjTDlIcWs?oc=5) <sub>shattered.io</sub>
- 📰 2026-10-27 [‘Where Are The Cybercabs?’ Tesla Investor Ross Gerber Takes Aim at Elon Musk as Amazon’s Zoox Eyes Expansion With Santa Monica Deal for 150 Robotaxis](https://news.google.com/rss/articles/CBMiaEFVX3lxTFAtSmZYX1h4LXhNdkpuMjk4MlVBY2ZGRmRjSmhBa2ZITGU3ckNONDBndjRpNU5McVFjaWdfVzJjRWFydmcteGFJRVBTTXh4Mzh2MFhkNXhlTl9xdGttSEhJWXVBdXJFZ0tw?oc=5) <sub>TradingView</sub>
- 📰 2026-10-27 [Robotaxi Market Projected to Hit US$ 198.6 Billion by 2033 as Waymo, Tesla, and Uber Scale Operations](https://news.google.com/rss/articles/CBMinAFBVV95cUxNYnI5NUJ3cDlDOFlEcTVJM1hJUTlQVEtZLVpVRVV5WUREMDdtT3BmVnQydGZ3RnNMRUFGN3h0eTR4bjdON0F4NkNJUi16T1Q4WGZYVFJNZG4yR1VoZnk5b0Q4QVBwVS1sMHBWTE9hMFNDSHd0cUhzQ21sZ3p4WllONWZERFdTazVRVTRYTEFKak1YQ3Zvc3ByRXQyMHU?oc=5) <sub>openPR.com</sub>
- 📰 2026-10-26 [Tesla’s self-driving Robotaxi service expands into greater Houston, with a rocket-shaped service map](https://news.google.com/rss/articles/CBMi6AFBVV95cUxQczdjaU40WElhTnV6LUthbmNnRHJ4bUh4ZmtWNDJTYW5GZ2ZxSy15Wm9QZ2x3Qi1pbjV5Q2Vtb0hZay1pb0Vrd0s3WERPQldOcmc3Z3NsNV9mQlRIaWpCSXROU01SNnV4c1hRaGVYZDhlLU8tRE83M3RydTR1X2ZFeGdleTVocWtyNmZBajZCTVZXVnJldFVYdDNadUIweUFoNWdWbmFZYnZ2Ukx0OXNrSnc3RlZ1X2V5UldHM1M2bHliUXlNWGJIeUs4MWRFazkxRExfNUZFVFVkSnJvUWxRUldzZ1BYaWt50gHoAUFVX3lxTFBzN2NpTjRYSWFOdXotS2FuY2dEcnhtSHhma1Y0MlNhbkZnZnFLLXlab1BnbHdCLWluNXlDZW1vSFlrLWlvRWt3SzdYRE9CV05yZzdnc2w1X2ZCVEhpakJJdE5TTVI2dXhzWFFoZVhkOGUtTy1ETzczdHJ1NHVfZkV4Z2V5NWhxa3I2ZkFqNkJNVldWcmV0VVh0M1p1QjB5QWg1Z1ZuYVlidnZSTHQ5c2tKdzdGVnVfZXlSV0czUzZseWJReU1YYkh5SzgxZEVrOTFETF81RkVUVWRKcm9RbFFSV3NnUFhpa3k?oc=5) <sub>Houston Public Media</sub>
- 📰 2026-10-26 [Texas streets become a battleground as Cybercab, Zoox and Waymo fight for space in Austin](https://news.google.com/rss/articles/CBMif0FVX3lxTE1UVUZFbnFpaG44ZGZxcm44WGpWay1xYjJPQnd2cVlhUGw5NnZ6U0dsY18wQi02QUYtdGNia1BIbFB1VnAyandXWnJXUDBTSWFQZk5VZHUycFFzXzdkMjhDV3g3T1ZucVJ4cUpQaXVtMHJZMjluWVU3VG45UTBSbGc?oc=5) <sub>https://latination.com/</sub>

</details>

<details><summary><b>Motional</b> (13)</summary>

- 📰 2026-10-28 [Hyundai Motor Rises to No. 29 in Interbrand’s Best Global Brands 2026 Ranking](https://news.google.com/rss/articles/CBMirgFBVV95cUxOYW13NmJqeUZhQ1A1UnJOYjB6NUdRZU9uOHdFRVR6Um42WFlSZmdOOXV2WnJqVUdJVUw0eXVPSTMxdWlNRnMySXJ6N2dhd0pIYXBpWXU2cDdZRlZNWGhhWWVLcDdnV05kMVd4cGtiYUkzNnRPTVN2UW82cmdSdHNfZy1KMlktRlZWMF9TdWNLSDlZeWJZcWtscG5ZVWg2T2ZMY09NNFNDOGlPUkw3SVE?oc=5) <sub>Indian Television Dot Com</sub>
- 📰 2026-10-28 [Hyundai Motor Rises To No. 29 In Interbrand Global Brand Ranking](https://news.google.com/rss/articles/CBMiqwFBVV95cUxPWlRYZlVKTzNZWmdfWXpGUmxJd2ZKQ1pnX1otaXB4XzgycnY0NmZkUXFsSGFZQlRKbFJWRkFwWmIzWEF6X0IzRjh3Z09YYkxGRm1nbURLQU05R3pnN3ZLcHVfMHRRNm85T3hXeUR5Mklha19vZ2QxUmdiNE4xTUxaaV9Nd3hLQk9Nc1ZTY1lxbmR2Z3RxSXQ5RlRnb2RLTmowMkVaZzRIZUdGZDDSAasBQVVfeXFMT1pUWGZVSk8zWVpnX1l6RlJsSXdmSkNaZ19aLWlweF84MnJ2NDZmZFFxbEhhWUJUSmxSVkZBcFpiM1hBel9CM0Y4d2dPWGJMRkZtZ21ES0FNOUd6Zzd2S3B1XzB0UTZvOU94V3lEeTJJYWtfb2dkMVJnYjROMU1MWmlfTXd4S0JPTXNWU2NZcW5kdmd0cUl0OUZUZ29kS05qMDJFWmc0SGVHRmQw?oc=5) <sub>Autocar Professional</sub>
- 📰 2026-10-23 [Waymo Is Accelerating Robotaxi Deployments. Who's Trying to Stop It?｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE83QXNrSG5UMnZyN2ltY3BENUtsUVBVVk4zbnpNTVNCTENELTBYZjVpY0NqMnFRUFYzVmdMSWdzVWswU1NZWHBRSkd1N3E1WnZxbUVaZ2tneWlmQWU0dTVZ?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-22 [Zoox Las Vegas Airport Field Report｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBuM3U0cTFKZHF4ZjhlSVhzY1k4dlVoMDhWVy1PaWUtcUJKWF9jeEtEczdXbm0zbjhTUXBiVFBpdWplUm1NNHBTbndsdzM5TTZYM1ZJSjVJNXBQM09iRkJJ?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-21 [XPENG Next Generation Pilot (NGP) Field Report｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE4xUFBoMW5mRlRQenVJWmVBMHhyMU5HV3VGQXBzQVhYMXVPXzhKeEhRY2Q0d1pKZ2hTcm81X0pSMF8yUGRwYzE3QlVVRko4YUlNNUhncUNzbTZhSkVveTBF?oc=5) <sub>finance.biggo.com</sub>

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
