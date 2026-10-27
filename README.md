# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-10-27 · 1,306 papers tracked · 44 curated.

**Selection rule.** A paper is listed only if it (1) is primarily about autonomous driving,
(2) has public code, and (3) shows at least one strong signal: accepted at a top venue
(CVPR / ICCV / ECCV / NeurIPS / ICLR / ICML / CoRL / RSS / TPAMI, or ICRA / IROS / AAAI / RA-L),
≥200 GitHub stars, ≥3 citations / month, or a well-known lab with traction. Papers are then ranked by a
composite score (venue, stars, citation velocity, LLM rubric for novelty / rigor / impact, SOTA claims)
with a per-topic cap. See [`scripts/rank.py`](scripts/rank.py).

📅 [Daily digests](daily/) · 🗓️ [Weekly digests](weekly/) · 📦 [Raw data](data/)

## Contents

- [VLA / VLM for Driving](#vla--vlm-for-driving) (10)
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
| [Teaching Vision-Language-Action Models What to See and Where to Look](https://arxiv.org/abs/2607.01658)<br><sub>Yuguang Yang, Canyu Chen, Zhewen Tan et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 34](https://github.com/ShivaTeam/DriveTeach-VLA) | Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving |
| [DeepSight: Long-Horizon World Modeling via Latent States Prediction for End-to-End Autonomous Driving](https://arxiv.org/abs/2605.10564)<br><sub>Lingjun Zhang, Changjie Wu, Linzhe Shi et al.</sub> | ICML 2026<br>2026-05<br>📑 2 | [⭐ 31](https://github.com/hotdogcheesewhite/DeepSight) | End-to-end autonomous driving systems are increasingly integrating Vision-Language Model (VLM) architectures, incorporating text reasoning or visual reasoning to enhance the robustness and accuracy of driving decisions |
| [SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving](https://arxiv.org/abs/2610.20609)<br><sub>Shaoyuan Xie, Zihan Zhang, Jingxuan Wang et al.</sub> | CoRL 2026<br>2026-10 | [⭐ 29](https://github.com/ASGuard-UCI/safedrive-vla) | Vision-Language-Action (VLA) models are gaining attention in autonomous driving, inheriting commonsense priors from large language models (LLMs) and widening the navigation interface from a fixed command set to free-form… |
| [Scene-Adaptive VLA: Efficient Autonomous Driving via Dynamic Layer Routing](https://arxiv.org/abs/2610.24590)<br><sub>Yujia Yang, Quan Yuan, Jiawei Fan et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 2](https://github.com/yang-luvu/Scene-Adaptive-VLA) | Vision-Language-Action (VLA) models offer a promising paradigm for autonomous driving |
| [CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving](https://arxiv.org/abs/2607.04179)<br><sub>Zhaohong Liu, Hao Ye, Xianlin Zhang et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 1](https://github.com/MICLAB-BUPT/CritiqueDriveVLM) | End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving |
| [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)<br><sub>Nan Yang, Zhanwen Liu, Linfeng Zhang et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 11](https://github.com/Zizzzzzzz/MVPruner) | Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings |
| [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)<br><sub>Yuan Gao, Wenting Miao, Mattia Piccinini et al.</sub> | IROS<br>2026-07<br>📑 1 | [⭐ 29](https://github.com/TUM-AVS/Chat2scenic) | Validating autonomous driving systems requires diverse, regulation-compliant test scenarios |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 12 | [⭐ 522](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
| [GRAVA: Grounded Reasoning-to-Action Representation and Learning for Autonomous Driving](https://arxiv.org/abs/2609.15169)<br><sub>Xiao Liu, Haoyu Li, Jianghao Leng et al.</sub> | arXiv<br>2026-09 | [⭐ 355](https://github.com/AhernResearch/grava) | Driving vision-language-action (VLA) models increasingly reason before acting, but their intermediate reasoning is often weakly grounded in physical scene evidence and loosely connected to executable behavior |
| [Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air](https://arxiv.org/abs/2605.31066)<br><sub>Tianle Zeng, Yanci Wen, Xueang Yu et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 1,123](https://github.com/louiszengCN/CarlaAir) | Recent aerial vision-language-action (VLA) models show promising single-UAV capabilities, such as tracking moving objects and navigating to language-specified landmarks |

## World Models & Generative Simulation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [HERMES++: Toward a Unified Driving World Model for 3D Scene Understanding and Generation](https://arxiv.org/abs/2604.28196)<br><sub>Xin Zhou, Dingkang Liang, Xiwu Chen et al.</sub> | ICCV 2025<br>2026-04<br>📑 5 | [⭐ 72](https://github.com/H-EmbodVis/HERMESV2) | Driving world models serve as a pivotal technology for autonomous driving by simulating environmental dynamics |
| [FrozenDrive: Zero-Shot Text-Guided Driving Scene Generation and Data Augmentation with Parameter-Free Frozen Diffusion Model](https://arxiv.org/abs/2606.20110)<br><sub>Yuhwan Jeong, Hyeonseong Kim, Daehyun We et al.</sub> | ECCV 2026<br>2026-06<br>📑 1 | [⭐ 10](https://github.com/daehyunwe/FrozenDrive) | Synthetic data for autonomous driving is surging, powered by diffusion models that promise scalable scene generation |
| [MESSENGER: Memory-Enhanced Sequential Scene Flow Estimation via Autoregressive Next-Frame Forecasting](https://arxiv.org/abs/2610.10759)<br><sub>Jiuming Liu, Jianing Li, Mengmeng Liu et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 0](https://github.com/liujiuming123/Messenger) | Scene flow can capture low-level 3D motion displacements in dynamic scenarios |
| [ASTAD: Asymmetric Style Transfer for Synthetic-to-Real Adaptation in Autonomous Driving](https://arxiv.org/abs/2606.29286)<br><sub>Dingyi Yao, Xinqi Zhang, Lihui Peng et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 2](https://github.com/Dingyi-Yao/ASTAD) | Synthetic data mitigates the data scarcity problem in autonomous driving perception |
| [Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends](https://arxiv.org/abs/2606.01164)<br><sub>Jiuming Liu, Chaojun Ni, Mengmeng Liu et al.</sub> | arXiv<br>2026-06<br>📑 8 | [⭐ 245](https://github.com/liujiuming123/Awesome-Interactive-World-Model) | With rapid development of large language models and diffusion-based content generation, world modeling has attracted increasing research attention, benefiting various downstream domains such as game engines, embodied AI,… |
| [Is Your Driving World Model an All-Around Player?](https://arxiv.org/abs/2605.10858)<br><sub>Lingdong Kong, Ao Liang, Tianyi Yan et al.</sub> | arXiv<br>2026-05<br>📑 6 | [⭐ 257](https://github.com/worldbench/WorldLens) | Today's driving world models can generate remarkably realistic dash-cam videos, yet no single model excels universally |

## End-to-End Driving & Planning

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](https://arxiv.org/abs/2609.26792)<br><sub>Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.</sub> | CoRL 2026<br>2026-09<br>📑 1 | [⭐ 13](https://github.com/VAIL-UCLA/DreamStream) | Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions |
| [DriveMLP: When Training Strategy Outperforms Model Complexity in Autonomous Driving](https://arxiv.org/abs/2610.29676)<br><sub>Alessandro Canevaro, Julian Schmidt, Hang Yu et al.</sub> | CoRL<br>2026-10 | [⭐ 3](https://github.com/alessandro-canevaro/DriveMLP) | Learning motion planning policies that remain reliable under closed-loop execution is a central challenge in Autonomous Driving (AD) |
| [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)<br><sub>Shen Zheng, Anurag Ghosh, Gaurav Parmar et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 32](https://github.com/ShenZheng2000/WarpI2I) | Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs) |
| [G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance](https://arxiv.org/abs/2606.26017)<br><sub>Hang Yu, Ye Jin, Alessandro Canevaro et al.</sub> | IROS 2026<br>2026-06<br>📑 5 | [⭐ 6](https://github.com/HangYuu/G2DP) | In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 17 | [⭐ 349](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
| [SimWAM: A Simple World Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.07468)<br><sub>Zongchuang Zhao, Xin Zhou, Tianyang Xu et al.</sub> | arXiv<br>2026-08<br>📑 9 | [⭐ 198](https://github.com/H-EmbodVis/SimWAM) | In autonomous driving, World-Action Models (WAMs) have improved end-to-end planning by transferring video dynamics priors to action prediction, but many still couple planning with future-video generation at inference, in… |
| [Latent-Centroid Steering: Single-Pass Classifier-Free Guidance for Command-Aligned Autonomous Driving](https://arxiv.org/abs/2608.00237)<br><sub>Meibo Hu, Jiamian Wang, Pichao Wang et al.</sub> | IROS 2026<br>2026-08 | [⭐ 2](https://github.com/codingmlinprocess/LCS) | Vision-language models (VLMs) have recently emerged as a promising paradigm for end-to-end autonomous driving, enabling agents to map multimodal inputs and high-level navigation instructions directly to executable trajec… |
| [STAGE: STyle-controllable Action GEneration for personalized autonomous driving](https://arxiv.org/abs/2607.29517)<br><sub>Zihao Liu, Xing Liu, Yizhai Zhang et al.</sub> | RA-L<br>2026-07<br>📑 1 | [⭐ 6](https://github.com/CarlDegio/STAGE) | Driving style refers to the behavioral preferences that drivers maintain during driving, shaped by their diverse experiences, habits, and needs, and is typically reflected in varying levels of aggressiveness |
| [A Survey on End-to-End Autonomous Driving Training from the Perspectives of Data, Strategy, and Platform](https://arxiv.org/abs/2610.00926)<br><sub>Chengkai Xu, Yiming Cui, Jiaqi Liu et al.</sub> | arXiv<br>2026-10<br>📑 5 | [⭐ 109](https://github.com/Jiaaqiliu/Awesome-Training-Ecosystem-for-E2E-AD) | Autonomous driving is a cornerstone technology for the future of intelligent transportation, where end-to-end learning has emerged as a transformative paradigm that directly maps multimodal sensory inputs to driving acti… |

## 3DGS / NeRF Reconstruction & Sensor Sim

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DriveWeaver: Point-Conditioned Video Inpainting for Controllable Vehicle Insertion in Autonomous Driving Simulation](https://arxiv.org/abs/2606.31918)<br><sub>Junzhe Jiang, Zipei Ma, Zijie Pan et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 16](https://github.com/LogosIntelligenceLab/DriveWeaver) | A pivotal step in autonomous driving simulation involves inserting foreground vehicles with predefined trajectories into simulated scenes |
| [MCSplat: Multi-View Photometric and Geometric Consistent Feed-Forward Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2610.25345)<br><sub>Yifei Wang, Wei Tian, Wenhua Bao et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 10](https://github.com/yfwang0824/MCSplat) | Driving-scene reconstruction via feed-forward Gaussian splatting from sparse multi-view images remains challenging due to two factors |
| [Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796)<br><sub>Leshu Li, Jie Peng, Yang Zhao</sub> | ICRA<br>2026-06 | [⭐ 14](https://github.com/UMN-ZhaoLab/Pocket-SLAM) | 3D Gaussian Splatting (3DGS) has garnered significant attention in Simultaneous Localization and Mapping (SLAM) due to its advances in capturing fine-grained geometry features and synthesizing novel views |
| [NIDAR: NIR-Guided Intrinsic Decomposition for Scalable Scene-Agnostic LiDAR Intensity Reconstruction](https://arxiv.org/abs/2609.36878)<br><sub>Junjie Zhang, Jie Yin, Kefei Qian et al.</sub> | IROS 2026<br>2026-09 | [⭐ 22](https://github.com/Zjj587/NIDAR) | LiDAR return intensity provides complementary surface-response cues for robotic perception and state estimation, yet many simulation pipelines omit it or reproduce it using reconstruction methods that require real intens… |
| [MM-TRELLIS: Point-Cloud Guided Multi-Modal 3D Vehicle Generation in Autonomous Driving](https://arxiv.org/abs/2606.24301)<br><sub>Hongli Xiao, Youjian Zhang, Yucai Bai et al.</sub> | ICRA 2026<br>2026-06 | [⭐ 9](https://github.com/HongliXiao/MM-TRELLIS) | Recovering realistic 3D vehicle models from autonomous driving scenes is crucial for synthesizing training data and building simulation environment |

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

<details><summary><b>Waymo</b> (249)</summary>

- 📝 2026-10-16 [Hello Toronto! Waymo is En Route](https://waymo.com/blog/2026/10/waymo-in-toronto) <sub>official blog</sub>
- 📰 2026-10-27 [Early Uber Investor Jason Calacanis Says Waymo’s China Car ‘Optics’ Could Push It To Buy Lucid Or Rivian](https://news.google.com/rss/articles/CBMi5wFBVV95cUxObU5nX0lOQ1ZaWXZaS1VVa1FOV195a2tOOE5lU2haeXh0Zmc3ZWF5LWxpWFJ1cDNtQkRwZU8wdGdIS3RPcHR1ZDZtbGp1eVJld1lJMThHdGpxUWo2N1ZHTmpnSDdpSUFFN0FGZzMyNnFCWEl5MmhHX2pJemk3RWRSRjBKMDJVUkM3bXlTcndJazVnVlRxOWtOZlZLZmVwSWJnMWhoRk1zVGllTk5MaHplbm5jMkVlNXBCSDBhZm91YTExTnRXR09ralpCNXRxUTRleGFzSGlGZXhLS3VpSVpwOXhkb29XZVU?oc=5) <sub>Stocktwits</sub>
- 📰 2026-10-27 [High car costs give Singapore a robotaxi edge: Waymo founder](https://news.google.com/rss/articles/CBMirwFBVV95cUxOUzhpNkZpLXhlS2U3aTk5ODBUMk5rT0RXbUJZZmc4alpsU3ZNclJfOHlPVk9sbkZfbnlGdDk5QlktdkZMS0dKZnllRUVnYzJyalB2SVo4VlBMSC03a01pekY4c2pHTUxobUFndmVfYk5JajVGVTdoQVBwMWtoYlRhMHdmT25oQVNQRUhMSVdPQ1NHWUVvUy1mczdMOThlNlhtMDdoRWUyREtzUXNGMEZZ?oc=5) <sub>Tech in Asia</sub>
- 📰 2026-10-27 [Bedrock Robotics Raises $600 Million As Demand for Autonomous Heavy Equipment Surges](https://news.google.com/rss/articles/CBMijwFBVV95cUxPZUhWV2t2azVWX3lQV3pneWN0ejRRQzJYXzhiQ3Y3NTNyZnNiVlpZQUxkUnh5YkVRQXY2MUVFX2JDMnFZNlhZMVl6OS1qYkRBeC1mLV9wNzNlaFplcTJXVmNNZVB5REMwd1lxU0VhdXQzTTliLTlCN3Bab3VxeXEwY05EMlVGSmJ1YXhfNXFrUdIBjwFBVV95cUxPZUhWV2t2azVWX3lQV3pneWN0ejRRQzJYXzhiQ3Y3NTNyZnNiVlpZQUxkUnh5YkVRQXY2MUVFX2JDMnFZNlhZMVl6OS1qYkRBeC1mLV9wNzNlaFplcTJXVmNNZVB5REMwd1lxU0VhdXQzTTliLTlCN3Bab3VxeXEwY05EMlVGSmJ1YXhfNXFrUQ?oc=5) <sub>Ventureburn</sub>
- 📰 2026-10-26 [Tesla Cybercab Adds 2 Features: Rear Cam, Quiet Mode [2026]](https://news.google.com/rss/articles/CBMihAFBVV95cUxQRzhJaGVfZ3FpUE1oaFlnOEItREJMZ1ZJeXhUMU1jbHFjWkRsWkZCLTdTTXM3SXNIUm1LdGxUanZWY3BpcGZMTUlLeFhrZlVQWWw3ck9vZC1tMm9Vdk1SUVp5eVlQcGpmVWlVN000OGFncmVZTmU3aWktRmVMWVZ3WVRuRXM?oc=5) <sub>https://tech-insider.org/</sub>

</details>

<details><summary><b>Tesla</b> (369)</summary>

- 📰 2026-10-27 [Tesla FSD Hits 16.7B Miles — 50 Million Per Day and Climbing](https://news.google.com/rss/articles/CBMimAFBVV95cUxPLW05ajFOcm9HOWVkU2xpOGpOMFk1VmlTc2NxdS1yNGwzNHBiWl9IeV9HNGRCZHg1QlpzMjZWZEJYMEFKRllkWGpEMEtHZ0p0a3Y0M3lzZWczZlJOSUptMFJob3d1UVlYOWo3TEh2a0dYOVRtSUtwTGJxSXBETzhQa3JuRXNrd0c1QWJPVmxzdzhxak9JdHRteQ?oc=5) <sub>BASENOR - Tesla Accessories</sub>
- 📰 2026-10-27 [Tesla FSD Subscriptions: 1.74M vs $1B Run Rate [2026]](https://news.google.com/rss/articles/CBMikwFBVV95cUxQUmg5VUZsOG95RTBEbmFIam1OeldQTXVoUWJUWi05VFhwZzF1RU9yTE5uQllHRDBPS0FEMjVmSzluOHNyQW92YTNEdkZ5LVpnWXpDQTExQXd4eUM2MVVfVVllTDQtZ0dOZlNUOVgzQlIyMkRXaWo5dlYzOTNxUW9LVmdkckRONXA5bUR0SlBWZkxDS1k?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-10-27 [Tesla FSD Safety Data: 6M Miles Per Collision — What It Means](https://news.google.com/rss/articles/CBMimAFBVV95cUxOQ0x4WEFLX1NYNXk0UzJwQzlpeXpGelQ2djkwQ3ByWUpZb3lVMmplRVJIZkZrZ2JwbmZmckp6X3RoX3YwcHpza2ZhS0FWd1BLamxDRWlObHd0X24wSnBXbWxUcktsMjEzdkF3T2FreC0zWmxuT2Y5RmJ1TktTQWlBMEpjR3I0a1RXV1AwLW8xN1A2ODFuSHdiaw?oc=5) <sub>BASENOR - Tesla Accessories</sub>
- 📰 2026-10-27 [Tesla Turo FSD Rentals Launch Oct. 28 [2026]](https://news.google.com/rss/articles/CBMie0FVX3lxTE84cDBOREtiU0xud1hBNVFJVEdybHlMdTZuZHJMMnQzR2tLeF9xTVFDUExWU0IzdlBxQ3dNY1MzamczcjRuOW9iN1l0aW1EMDB4dEJzOE1NMlp3NUlZTXhVSkpfN2ktcGZBTHJjUEZhVlBDVDJKa0U2VDhzQQ?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-10-27 [Tesla has a Cybercab problem nobody saw coming](https://news.google.com/rss/articles/CBMifkFVX3lxTE1lendZcGdwdlRyN21JTjBNT0Z4ajZHaHR5ZGNZR2RZakYwMUtyOXdxLXBua19VQTZfeEc3TUFYeGMzVDlNMmU4Wl9wMkpEcEVWYXg2LXJBdGJoQnhnbV9WQW41eThPblRfQnk5MG0xY3pnY09mRmdObnI5Q1JQdw?oc=5) <sub>Teslarati</sub>

</details>

<details><summary><b>NVIDIA</b> (262)</summary>

- 💻 2026-10-20 [NVIDIA/flare-local-inference](https://github.com/NVIDIA/flare-local-inference) <sub>GitHub</sub>
- 📰 2026-10-27 [51World wins Nvidia’s nod. Now it just needs to translate that to sales](https://news.google.com/rss/articles/CBMingFBVV95cUxOSV9nbDF6SkVSRENoU05ybXBUeTJrbUpoVmVLamI5N0FidWlfVmJyb0xSUXZmeXY3Q0VRTVlhdjhwanJ2VGNDc2xQVkRRMGZjOEtLSjU3RjB0ZF90VFF1QzluODNfek40WktzVlVMeEtKdWV6QmJXbC0zRkJJQUhhU3NzMVlQb2NxYVlYZDQ2amw1Mm44Q2RtS19wWVExUQ?oc=5) <sub>Bamboo Works</sub>
- 📰 2026-10-26 [Autonomous & Self-Driving Vehicle News: Tesla, Mobileye, Aeva, Ouster, Pony.ai, NVIDIA, Stellantis, Bolt, Wayve, Volkswagen, Einride, Valeo, Aptiv & TIER IV \| auto connected car news](https://news.google.com/rss/articles/CBMijgJBVV95cUxNLXpSRDZNWTdpaUNvcWdGUWJBRUxfMGlXTXYtNFEyV0NxU0hfTmhxUlQwb2JGN3Y0VW9QS25NeVRPNkxsVV93ZkZGdGp5bW9iU3VERTFwaW5MckVKc0xmTEJVR1NFTFJORXR5SVZ2VlNDY0VFRjhabEo4dkp4WU1xTFpYci1kcWNsNndSNHg2cExQUVlCRVEtb1plX0dLa2diaDV6eU9hX1dnT1pOTmVkZXBNQ1pnUHlZQ1BVX1FEWWJfcS1fejBXbUdWZE5qZDRDUGtmTnFUZVhYTkItWlN5emwyMnRGNWFITHVDTEZwQk9hdXpJT3d3N2UybExoRjRtLTVZUFE4ZFBZQVZJLXc?oc=5) <sub>AUTO Connected Car News</sub>
- 📰 2026-10-26 [Jensen Huang calls AI as a five-layer cake: Nvidia GTC Berlin](https://news.google.com/rss/articles/CBMirAFBVV95cUxPYXNNWS1vQ1Z1czhXRk0ycS1tOWM1WHhWMFhXZnVaNmpvU2tlcXN4N29DTjB0WFAyNkhwekVrOWgyOUU0Q21jOUFLenJhZnJ4NzFvZS1XRC1UcGFyelFHa1RWeVA1cEw2ZVpkRHdjZk5BcmlieHhpTTktM1NPUFFhdHZpTXVGZm40aEl2ZHA0UW5pNlN2dWkzcWpIVnF2S2pBR1dNX0tqaU5lang20gGsAUFVX3lxTE9hc01ZLW9DVnVzOFdGTTJxLW05YzVYeFYwWFdmdVo2am9Ta2Vxc3g3b0NOMHRYUDI2SHB6RWs5aDI5RTRDbWM5QUt6cmFmcng3MW9lLVdELVRwYXJ6UUdrVFZ5UDVwTDZlWmREd2NmTkFyaWJ4eGlNOS0zU09QUWF0dmlNdUZmbjRoSXZkcDRRbmk2U3Z1aTNxakhWcXZLakFHV01fS2ppTmVqeDY?oc=5) <sub>DQ</sub>
- 📰 2026-10-26 [inDrive and Pony.ai Announce Kazakhstan Robotaxi Collaboration Using NVIDIA Hyperion](https://news.google.com/rss/articles/CBMiugFBVV95cUxNZ3RvSm9KeXB2MDFwX1pEWExvS3VlZDNGNTdLSWkwV1R1VE9uclRtVU5vTEtBcDh2dlI0UHZFaE1jTzV4aHpRcmpicUNDaUlxZjBFQWI3cDg0NXZYLUJUQkQtNDBBN1cyaWVpSGhSM2pkYWM2M2M3VGNYelBhUmgzMFdXb1p2MlhYQW9fVnhXMWEtWHVqMEw5Sm9BTXNNdnBxYV9LVTAyR1UtZ00zOE40YXBLSE42RTRsc1E?oc=5) <sub>World Business Outlook</sub>

</details>

<details><summary><b>Wayve</b> (66)</summary>

- 📰 2026-10-26 [Autonomous & Self-Driving Vehicle News: Tesla, Mobileye, Aeva, Ouster, Pony.ai, NVIDIA, Stellantis, Bolt, Wayve, Volkswagen, Einride, Valeo, Aptiv & TIER IV \| auto connected car news](https://news.google.com/rss/articles/CBMijgJBVV95cUxNLXpSRDZNWTdpaUNvcWdGUWJBRUxfMGlXTXYtNFEyV0NxU0hfTmhxUlQwb2JGN3Y0VW9QS25NeVRPNkxsVV93ZkZGdGp5bW9iU3VERTFwaW5MckVKc0xmTEJVR1NFTFJORXR5SVZ2VlNDY0VFRjhabEo4dkp4WU1xTFpYci1kcWNsNndSNHg2cExQUVlCRVEtb1plX0dLa2diaDV6eU9hX1dnT1pOTmVkZXBNQ1pnUHlZQ1BVX1FEWWJfcS1fejBXbUdWZE5qZDRDUGtmTnFUZVhYTkItWlN5emwyMnRGNWFITHVDTEZwQk9hdXpJT3d3N2UybExoRjRtLTVZUFE4ZFBZQVZJLXc?oc=5) <sub>AUTO Connected Car News</sub>
- 📰 2026-10-26 [Stellantis moves forward with autonomous mobility initiatives in France](https://news.google.com/rss/articles/CBMirgFBVV95cUxOUDBCRGRFNDJTMVM1eEZoWU0tSm5tbm9ZblI1RnlSSW1kNU9ZOTBkOV9qSG9nZDlLN0MxUEtkRmNVTy1kZEVITTlMb3BLS1l2VnVEOTBKNW41MDNXeVlsU215VWFCUkVzVmdZQk9kT3MzMFJPZXFGems5Vy15Qk5vaDNjcTN6cnhxQWNoOEZleF9JRUwwSlF2OUpTZ1lNY0t1dndEVHBjcUFwRmI5dWc?oc=5) <sub>electrive.com</sub>
- 📰 2026-10-26 [Wayve, NVIDIA and Stellantis Join Forces to Advance Autonomous Driving in France](https://news.google.com/rss/articles/CBMiuwFBVV95cUxQZi1zNFE1VmJRREREX2NoaEY3ZUNwWjJRV0llVXI1SDhUanVISUtlS2xkRG9YSnFRVGVJdEVEMjdBUUNOQ3ZOazQ3MzRvRFVESllhSlNHUkhZempoTk9vaUZkTk9tcTN5Nl9wR0gyeHE2YXNqWk03OHJkNnBvdFpaR3QyWDV6X25US2JTczFjZnI2YV9XWG5TVEpmWlc1eDZGcHY2UVRsckNzMTNBaGl2UDNyLVZ5OWI1RjdV?oc=5) <sub>Electric Cars Report</sub>
- 📰 2026-10-26 [Artificial Intelligence (AI) in Self-Driving Cars Analyzes Market Trends, Segment Details, and Business Strategies](https://news.google.com/rss/articles/CBMi5wFBVV95cUxQWlhEWWpObzFXTGlGUkhkdEJVc2otRWFLX3pSdU5rSHJmRFN0dWQ2NTd3djNvNEM4bjFzUDZqMFpuMXBBc1ZORkNaNU1QZm9sdE41b01XVXlaTE1TRk5PMnBWNjlUdlFreVNBLVJDZVN6VTdSOXdxdXZPOXRmX25iRVlOZ0xrSG5iLTRpZGoxTlpodTVGQ2RtLTdHSjVkeTFXNHZEOXRpek9qb0MtVzVnNDdoYUhVTnBaaElndl93MEZvdzhxclBNSlF5VUl4eGJhdXBsU0ZRVnlFMkd4VGF3eE9kaDdxdm8?oc=5) <sub>EIN News</sub>
- 📰 2026-10-26 [Autonomous vehicle: the state wants to move from testing to services](https://news.google.com/rss/articles/CBMid0FVX3lxTFBxN1AtYjRQZHZzdTdRaUVVRUltTnJ5REI5OGlld3NPUk53cU90T2wxQUYyMHgzMmcxSHRRWU1EUkFsUXZUaFhZQjd2NTAxekRjdkk2MTBpMUF1UUp4NzJFVlZBLU5IUXpCcjJXV1pSLUFXVkdrOTEw?oc=5) <sub>Flottes Automobiles</sub>

</details>

<details><summary><b>Momenta</b> (110)</summary>

- 📰 2026-10-26 [央视全程直播智驾上珠峰，风神L8+重新定义15 万级智驾天花板](https://news.google.com/rss/articles/CBMiaEFVX3lxTE9kR2h0cHFzZEl2emdNUjNNM291UFpzT25uNF9zcGpvQTVYS3dfdUZmaXh0ZzMwY19ndzdQcXY2bDVHUUNWRG9IQ3JYWW5xZ1pkS2tyU043eXFHa2taSFFlYmlhZ2hTTVFz?oc=5) <sub>盖世汽车</sub>
- 📰 2026-10-26 [【视频】抢先实拍东风日产NX7，宁德电池Momenta智驾，插混大沙发依然最强](https://news.google.com/rss/articles/CBMia0FVX3lxTE5jM3hGYzZlMElvMDYyeENRSldqUWhMXzFSVHAyWWw4ZEtUR3RfNFNmdS1zbldfbTRhZ2Vqc1Rqek5INVE2V1VuM0c0Y3YwV0pFZnYzNHZJNzdRbEhSdDRTZUtOM09DajRvMmZZ?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-26 [China Boosts Self-Driving Push With VW, Xpeng Technology Trials](https://news.google.com/rss/articles/CBMiswFBVV95cUxQRGlGVmN3eHItalpkV3BGVl9KMWh1YWFPZlJZS0F5YnBZM1QyR2lpbFNSMmp2c3JZYzlmZlBNeTRhVDNMWHNWSlU0dFlpMFFZSkxvTV9jTXJlLXVFaGFydnBwZUhRblY4YVJwcFpYdnJxTWhYM2Uyb2NrRnByc0hsb3VEWjh4NmRfWDFMUWw0MlQ2a3ZpUDc2S2pYb1JJVkFFQzNUUWFzMWl3Q3dNR0s4YTlsZw?oc=5) <sub>Bloomberg.com</sub>
- 📰 2026-10-26 [Algorithm Companies Launch "Chip-Making" Survival Battle: Strategic Competition & Industry Transformation](https://news.google.com/rss/articles/CBMiU0FVX3lxTE10R3Q1VHRPU1c4aGdmeVBNVUg1cTBvbm45UjNydkNtYnNSVjJTUWFBc1REVDN5U2tLaXZrZUE1N0xHM2c3cVdIOXFzbDd2dE9zYjNF?oc=5) <sub>eu.36kr.com</sub>
- 📰 2026-10-26 [带激光雷达的豪华插混SUV哪款好？5款智驾SUV横评对比，看全新XT5 PHEV凭Momenta R7入榜+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE1PTUZ0SDVUVTNSSWN2RnRtaThMa0lLaVVsZGt3YlAwZkVFT0loaGhnVlZxX25wMEhSWXhLTDlHVGk3RXBSaU5scnBjcW4zYXlOQ29uLUJ5dGx5OWlqUlpSR01GelpKVnplYXA3ZFVSWWdNQQ?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>XPeng</b> (252)</summary>

- 📰 2026-10-27 [China grants permits to VW joint venture and Xpeng as driverless car race builds](https://news.google.com/rss/articles/CBMi0AFBVV95cUxQTGIxdFpJZWRndWx6MXpVd3lVT3ZHdDdYMXBqbW9zUGIyczE1LUFXR3d1Z2ZnSXhtdHJCeDF6SkpDX1M0dTBkakh2dnRDOEUtek9HcnFnQ0c3Yzl6TGsxOWJCV3pPc1I0MWtyeGhETFZLMnI0UzlmVmRJYm84TnlVd25LTHV5VFdVYWpnSjFZbGl0QmxIUWNhbzQ3Yl84SXdEV2pSU2tJcHplLXhialpDLUlrMWZCaHJZdmZ6VlYzbDdydTJZbFhreWZDNXROZ2810gHQAUFVX3lxTFBReGtIRXZiZUhHc3FVejF6T0hqUGdqeEFMVjdNekNETmUyWjdDZGkzZW52bUIwbDl1aXA0MThVbkpESDQ2b3BfOWF3THpoZzlxN2h4V3FwVmdnVTlCMDduRmhxcE1ycW01VlNpZkxrY3dtUXp5dUkxSHlLWXEwYk1oR2JMZHMybThKaTAwUGxHZEpqeHNmYjlZekI4d3ZwMjNUQ19oWE5wOHg4cTR5SnhWcjRKNGIxellFZkRNNGh3TGstcDV0R3gyUzRBSzlmNDc?oc=5) <sub>South China Morning Post</sub>
- 📰 2026-10-27 [XPeng Robotaxi Approved for Public Demonstration Operations; Intelligent Driving Moves Toward Large-Scale Deployment](https://news.google.com/rss/articles/CBMiyAFBVV95cUxQS2szNEI4ZFdCSnR4NkZnM0pRRUs1UUtSdWJkSTJjQnhBMXhpQlFCSFZEdU5rN1BoUjZMM1Z1cW9jWGl4eUtaeFZyYlhVV3owSnhrVmwtWXJuelp5blN6QU5jSnBCNjlVRDUwWDB5bXBYRGJnWTd0Y0hBajVfTHlaSWMzOUFHdTB2OGVrRFo4Nl8wZUhnNWFZUUVkV1FYVFc0dmxHeFJuRUdqaUpWMmdweEFHeFd4cDI1cTFqejZOWUlLejRJN3U2bQ?oc=5) <sub>Moomoo</sub>
- 📰 2026-10-27 [China's XPeng Wins Citywide L4 Robotaxi Permit in Guangzhou, Entering Commercial Validation Phase](https://news.google.com/rss/articles/CBMidkFVX3lxTE1TM0JIYk5tMG10NElQYTF3WFB3YlRabWFlS2NrN3RxSkJnUmhJaWdCSTNTbGJWY05KczBMVnhmeHRaVlIzNE9Md3ZOWlljamJWSDRlRW05Wm5LeWp2cklqcFhXTEdOd3ZxNkRTUFU2eEplSVU1M0E?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-27 [XPeng Wins L4 Robotaxi Demonstration License in Guangzhou](https://news.google.com/rss/articles/CBMirwFBVV95cUxPSGtWWmJYcWFjTVM3UXlKdnI3RldXVFNfMkVpbGF6d01ZNFAxb1JaTWtGNWhUMTVRYkRIS1daZlRpenhPQUhmamZGV3d2eUhzMk9XbzBKSy1ocTFqTHpxYWJGajJtWlhLMmw2YmdlZnRRd1RJNjFXSE5sNXA2bmpfZFR1N1JhNGlackVkb3llakRIR2doWndJSXNxak5YNzI2N1hNaDR4NElRazdmeDJn?oc=5) <sub>marketscreener.com</sub>
- 📰 2026-10-27 [China has successively granted permits for autonomous driving operations to EV maker XPeng and Volks..](https://news.google.com/rss/articles/CBMiT0FVX3lxTE5xbERHUURWVUZOeV9sUzFXbXRwdDNndERiVGphQk9ka2hneWd2MDItWmZ1Q09aRTNENjV1LWZaVG5CMkl5ZzhmMU5jOTVZMXM?oc=5) <sub>매일경제</sub>

</details>

<details><summary><b>Li Auto</b> (153)</summary>

- 📰 2026-10-27 [Why This Global Auto Parts Giant Is Venturing Beyond Core Business into the Robotics Sector](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1FV1p6VGVFS1NpeHFMWGktZEY3U0N6QTZtalUwQzl2MlZOSlE3SEhISzRRbWhXR1dySzRVNHh3MUFTekphWUd3ZTA0cGpIYmptTXNj?oc=5) <sub>eu.36kr.com</sub>
- 📰 2026-10-27 [25万预算新能源SUV横评：小鹏G9L与理想L6、问界M6、乐道L80同台较量](https://news.google.com/rss/articles/CBMickFVX3lxTE9ST2xSMXJ0NzJhcldLdmF0ZWRUbWIya2dqdEd3eTlHbVp4Rkk2RmZVRmZlNFo2dVVYS2NISnVfSlM0dnNiYWw0Z3ktLU4tWFUtaWhLM091dWdYOE9kdVlybUdIYlpRTzNrMHFwbzRTRUI0QQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-26 [25万预算新能源SUV怎么选？小鹏G9L对比理想L6、问界M6横评+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE1fNWxhQ3J2dzYyTkxCaVRTWk9mZGMyTm5FZ0RaeVhvemFtRzFtSVYwZFRic3VqMjZtaHR3b1V0S200QlNFS1hSLUxMRmkxX19VVHBlT1RtVDA1SFdLWUxxS0pCN0JLUjg0U2FtTVVXSVR2QQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-26 [车企电池自研真相：理想26.5亿入股，比亚迪全链掌控](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9WWjBLa0NpUUVickFnOHdKTEFqZHJPNFBMVFlnV1YyaU1odngxNVJ0cmNlQTBLbDFSQk5taEdFcnh6WTJqQm96ME5mcUlQYWE4NjBrWUMtZVRwZVE?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-26 [豪华大六座与全地形的交集：神行者8、理想L8、领克900横评](https://news.google.com/rss/articles/CBMickFVX3lxTFBHTnZNeno1ay04MWZNZGpzU2hKblpnWTVxZEhBOVJLQWpTUFRYU2ZobmwxU0NRRXYzSlBWYWtLV25MSXpOVjQ0Z1o5Q3NhWmVpVEhaRHRiVjFiOTRhS3hqRmNzWTRtRlYzc3NnYng0MGlndw?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>NIO</b> (157)</summary>

- 📰 2026-10-27 [Volkswagen begins Level 3 autonomous driving road tests in east China](https://news.google.com/rss/articles/CBMiWEFVX3lxTE15ZDdlV2V3MFBxSWxCd251LWRMUmp6RVRrZW9DNFpSUndWcW5Yb0Y3NWFlRGlZQlQtMF9mclVtbGR4SVlRUDliY0xRaEd4UXBmc0RockFOTXk?oc=5) <sub>chinadailyhk</sub>
- 📰 2026-10-27 [【视频】蔚来ES6 2020款 600KM 运动版](https://news.google.com/rss/articles/CBMia0FVX3lxTE0tNzZYN3Y0cXQ2bU81SWRidHdRV19zT1UzRVl4VUotMXZCbGZqWDZXN2pFT3VrS1l3UnFxTHhDUlNFTnRLTWNsZXk0cndfREhxWGxabDFCRzJZRjhDeHowUmJHNVJ5OGxMV2FB?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-26 [变道时别克130码超车 蔚来ET9智驾抢方向盘出车祸](https://news.google.com/rss/articles/CBMigAFBVV95cUxPVkRXeFJuMkhBbXkybVFGMjBGN2xVWXlQVDB5TmZVUVdtQnlveERySEJIUmgwTmJQX3MwT0FIMjVZMjYtTTNvYzdPNEQzbkh0aExyMDlyeW1pV1ZTcFVzSXhCU1hiX1NfTGNoWDZkOTRmTmNLYlFzV3ZJNEY3WWRhTg?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-26 [4款热门新能源豪华SUV横评：经常长途自驾，凭什么神行者8成了川藏线上的移动观景台？](https://news.google.com/rss/articles/CBMickFVX3lxTE5BOHJISGY1VEpiMzYwYmY0YzFOVWk0MTVTUWNIbVB6NVpnczFFZWpNNUdDajhvTFM4bjdpZFZzQlZ3dDNwTy1PeTNZUmFTd2ZZTzA0X1JUd1l5TEtwSzBVbkV6dmdxbDgtUmtkUi11SUJNdw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-26 [Volkswagen Begins Level 3 Testing on Chinese Roads Ahead of 2027 Goal](https://news.google.com/rss/articles/CBMitAFBVV95cUxQYV9NVDJVTjBnNURsSUxvUTRKT29HUUU0ZzdONDk3UnpLUVpZdTdDaW5yaERGaTBOVWhOQjhHNjNNRm14WDllbEFQSzNKWXRVSFlZdHcwS3ppN19VZ3pXQms3VGJqTEx4cTl4b19OTkxMYVNSMUlJYy1tWS1mRnlVUl9DWGgwUU5CaDhUVzlVZ2hQVUo0YVNPQ2FHZnpvZlJUQVhOMXVMc2psM2NSWDN6eE5HLUw?oc=5) <sub>Electric Vehicles</sub>

</details>

<details><summary><b>Huawei</b> (343)</summary>

- 📰 2026-10-27 [HUAWEI WATCH D3 Debuts at ISH-ECS 2026, Bringing Advanced Blood Pressure Monitoring into Everyday Life](https://news.google.com/rss/articles/CBMiekFVX3lxTE1iVHB0ZFBLT2FhenRBcldVWXo2UV9XQ1pJWUF0M1lxRnhjczBYY0lUUnlJaFBFaWs0ME1Ody1uWGxzS3lMOHBqNDI3aUp2MWFZbkJvN3BqeHVwemVLNVUzenBJU3FSZlpkVTJYMDVwdGFmc1E3NlRqcG5n?oc=5) <sub>AOL.com</sub>
- 📰 2026-10-27 [NISCO reports over RMB 100 million in annual savings from AI rollout with Huawei](https://news.google.com/rss/articles/CBMiogFBVV95cUxQVXJoRTRnT2ItQzA2M3hORlpLRVppV1FsMjZWc004X3Jma2ZlREptR2YtQ0V5d1RQeFh1YTMydVA0N3FtU184NGFkcEh0dVAxWmVyX3FNVDdQdklrUnhNVkx2cHpFWS1RYkhtQTFPLVpOdHlwcWVvNzVlT0x0d29JWVdLWDlRaDRyQmJEeW1ZRE5KNXVtbGNjNzVUc0hJLWgtLVE?oc=5) <sub>KrASIA</sub>
- 📰 2026-10-27 [智界V9上市，38.98万元起售，全系标配华为乾崑智驾](https://news.google.com/rss/articles/CBMif0FVX3lxTE91Sk1hcVR2SEVia1BlRTBwWUU2dzc5OTBvenl1djlCVENNaGhvYXJpWEdVZWl2QUFiYi1PbnV3Nnl3V3dES3lCUk5VbUwwNEZBZ0habVVMWUNJYlNfaGp1VFJkMVJHb21wNW1tZGhIV2NLdDNoczF1d0Y1VjgzTlE?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-27 [【视频】第二届华为乾崑智驾公开赛，首日报名人数突破10W！女侠申请出战](https://news.google.com/rss/articles/CBMia0FVX3lxTE5PTThqbDYzT3Q1MkcwbXBGTkp3TXo3aEtsR3ZNUURoVUVOckluMEdIRXVwekJwQTlfNW1lZVROZERfQ3F0eWNsVXJyNmlkbjdubUZzOVliYklaYkQ0bm04QlozNUY0QTBES2ZF?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-27 [28.99万起全系满配三把锁+华为乾崑ADS5，这台30万级新能源SUV上市即爆单的底气何在](https://news.google.com/rss/articles/CBMickFVX3lxTE9RM2pITW0zZTFkcktfbDF4X2lSeXlvYktIYjE2R2E1SGlDcnB1Qm5sUHFoN0J4V0xFZ0lEMnFNeWgxcFo3QjhyYTctZjRUbGNJeWFJTFp2U1RxRXh4TU5UVTNQUC1DUmlTVHFoTHRTbWNLZw?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>Baidu Apollo</b> (56)</summary>

- 📰 2026-10-27 [China grants permits to VW joint venture, Xpeng as driverless car race builds](https://news.google.com/rss/articles/CBMi0AFBVV95cUxQUXhrSEV2YmVIR3NxVXoxek9IalBnanhBTFY3TXpDRE5lMlo3Q2RpM2Vudm1CMGw5dWlwNDE4VW5KREg0Nm9wXzlhd0x6aGc5cTdoeFdxcFZnZ1U5QjA3bkZocXBNcnFtNVZTaWZMa2N3bVF6eXVJMUh5S1lxMGJNaEdiTGRzMm04SmkwMFBsR2RKanhzZmI5WXpCOHd2cDIzVENfaFhOcDh4OHE0eUp4VnI0SjRiMXpZRWZETTRod0xrLXA1dEd4MlM0QUs5ZjQ30gHQAUFVX3lxTFBReGtIRXZiZUhHc3FVejF6T0hqUGdqeEFMVjdNekNETmUyWjdDZGkzZW52bUIwbDl1aXA0MThVbkpESDQ2b3BfOWF3THpoZzlxN2h4V3FwVmdnVTlCMDduRmhxcE1ycW01VlNpZkxrY3dtUXp5dUkxSHlLWXEwYk1oR2JMZHMybThKaTAwUGxHZEpqeHNmYjlZekI4d3ZwMjNUQ19oWE5wOHg4cTR5SnhWcjRKNGIxellFZkRNNGh3TGstcDV0R3gyUzRBSzlmNDc?oc=5) <sub>South China Morning Post</sub>
- 📰 2026-10-26 [Robotaxi赛道又来狠角！小鹏悠游拿下L4级自动驾驶示范运营资质](https://news.google.com/rss/articles/CBMif0FVX3lxTE80R1FKeUFrOXpDaV9HaXlDeVI3a2JtN0FsSGZJQmZJS3VIMkxYVU12R1d2SVNqbTlTQzFvWVFmbEZ5U2xndVFPWlNudXBYSVV6eGxjSjl1WkthUzJpMjhYbUtWYU5FRFpubzdrZk13cjZpMHM2eGN1VG1EbklnWUE?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-26 [Audi CEO speaks at Trump rally as $4 billion US factory announced](https://news.google.com/rss/articles/CBMiZkFVX3lxTFB6STRYOGc0aTZXUV8tWG1CN1Y2LUxKTnVPckg5QlJ4WTcwTmNDQlczQnpjcWlFRjM1MVRrTnBtUWlzTENvVnF4cVZibDg2Wm9WSF9yWktweFN2WEZrSzBISGpfR2I3Zw?oc=5) <sub>Reuters</sub>
- 📰 2026-10-26 [Level 4 robotaxi approval for Xpeng in Guangzhou; VW starts Level 3](https://news.google.com/rss/articles/CBMigwFBVV95cUxOelFDNkU4MERLRXZIS1NjU0p3blZLaGQtUlBHUXJsejhScUlZUkFHUWgtUFlBbnNKeldMX2xMaE91TXZKeUh1OVk1SGVFVy1XdEh3dWpoY3N1djN0Ym1LRjhKb2FWZHl0NjVGb24wLXQwX2RLQ0N0RlZ4T0hJcTVUcUlDdw?oc=5) <sub>The Next Web</sub>
- 📰 2026-10-26 [Learn Why The Bull Case For Lyft (LYFT) Could Change Following Alcove Launch](https://news.google.com/rss/articles/CBMiyAFBVV95cUxPQ1lmVXhkVTRQdUp3VUVYMXphSlNCby1SQWhKWHVULXNnbWx6SmQtV2pLalNlM3NJWlU1ZUNxQXZMSzJNa0RaeENnV1hRaEx6UURqSEljOUQxTVcwZ1ZKaU1Ud0V3NGdQaVYxUGd3UVBJNFdiZHg1bzVIZTg5RWFRMm90WGRweHZ6R2RwM1JDZG1CdUxJSVJ5TDBmcmRkMURqOHBQRFFVem41aFo4Tmp1SFBBemlmQU8xNXVjcmZla1BLbjdteHowTtIBzgFBVV95cUxOeVExU0I4bDBkWHdvdEpDRy1vcVFHdm5jLUhMZWVmZVpYTFk4RURPMTdVSDYtRnRLT1JBb3dPUzJkckV1RG8wT2lidV9vaFYtY0h4bFQ5cWg5NGRBZlFxM1dXdGdRWktPRF9UdkEtYU0tSm5TWlQ1aUZQaVNZUlJydUhzWll0TDRSWXdOakpMUmdDSERJOXA5ZTVOYUxzMUFyNWwzQ1hMQkROUXBQN1hiN1RGTGIwSGNOdmE1amhWXzVmNURQNXViZ1hUUzFkUQ?oc=5) <sub>Simply Wall Street</sub>

</details>

<details><summary><b>Pony.ai</b> (153)</summary>

- 📰 2026-10-27 [小马智行在武汉成立新科技公司，注册资本500万](https://news.google.com/rss/articles/CBMiWEFVX3lxTE1kQ2hCS2huaVk4NE52R2w0WE5OWVZZelpZeXlKekt4SWRkQ1RwaGlzalpVb0lMZFZCYWYxazZ4NnQtczZZczBtRjJtY2RkM09zSXFqN254RUo?oc=5) <sub>36Kr</sub>
- 📰 2026-10-27 [中概股多数上涨，纳斯达克中国金龙指数涨0.63%](https://news.google.com/rss/articles/CBMigwFBVV95cUxPNE43RlBManEzNmx2NmNmV2tMY1l2aXBBNG4wbG1QYzYzZE5sa3ZvXzNuR2M3TzdpUVBqU3RGQ3JiSUxNSXVTX3NLai1yT3h3TDJyRUJqcTRJOG1FT1lNbzdmOTlfQk1mbDZVUWY3VGtvUDBWSUpoV08yZTBtbDVXZWo5TQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-26 [Pony.ai Kazakhstan: Astana Robotaxi MOU, 5 Takeaways [2026]](https://news.google.com/rss/articles/CBMigwFBVV95cUxQMXlZcDlNZVJScEtuVjY3c2xzeGRYRnBKelJnRUlOWXp2Z3R5OW0tdXluMEVpaC1qNGg0c3p5WlptLXhocU8xUS1HdXJ5VjFld2xPUEdZMmhURjdPbFQweGRmdkF4Q09tUVVSOE5hZGx3Q1pnQk1TQ3NrdFF2NUd4RGJ1OA?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-10-26 [inDrive and Pony.ai Announce Kazakhstan Robotaxi Collaboration Using NVIDIA Hyperion](https://news.google.com/rss/articles/CBMiugFBVV95cUxNZ3RvSm9KeXB2MDFwX1pEWExvS3VlZDNGNTdLSWkwV1R1VE9uclRtVU5vTEtBcDh2dlI0UHZFaE1jTzV4aHpRcmpicUNDaUlxZjBFQWI3cDg0NXZYLUJUQkQtNDBBN1cyaWVpSGhSM2pkYWM2M2M3VGNYelBhUmgzMFdXb1p2MlhYQW9fVnhXMWEtWHVqMEw5Sm9BTXNNdnBxYV9LVTAyR1UtZ00zOE40YXBLSE42RTRsc1E?oc=5) <sub>World Business Outlook</sub>
- 📰 2026-10-26 [广州全域L4 示范运营，小鹏Robotaxi 从测试走向商业验证](https://news.google.com/rss/articles/CBMiY0FVX3lxTE5kVWJjc3ZrZ2ZjMFI4X3dUZUZlUHhGU3VFSzVNVHp0dGExZHJxQlgteVQta0JKdHhjR0dmUm5QdXptMUkwc3ZRV2FuWllQdG5RZ3BkdXJPQXE0ZWlGRXVQd2VxWQ?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>WeRide</b> (149)</summary>

- 📰 2026-10-27 [China grants permits to VW joint venture and Xpeng as driverless car race builds](https://news.google.com/rss/articles/CBMi0AFBVV95cUxQTGIxdFpJZWRndWx6MXpVd3lVT3ZHdDdYMXBqbW9zUGIyczE1LUFXR3d1Z2ZnSXhtdHJCeDF6SkpDX1M0dTBkakh2dnRDOEUtek9HcnFnQ0c3Yzl6TGsxOWJCV3pPc1I0MWtyeGhETFZLMnI0UzlmVmRJYm84TnlVd25LTHV5VFdVYWpnSjFZbGl0QmxIUWNhbzQ3Yl84SXdEV2pSU2tJcHplLXhialpDLUlrMWZCaHJZdmZ6VlYzbDdydTJZbFhreWZDNXROZ2810gHQAUFVX3lxTFBReGtIRXZiZUhHc3FVejF6T0hqUGdqeEFMVjdNekNETmUyWjdDZGkzZW52bUIwbDl1aXA0MThVbkpESDQ2b3BfOWF3THpoZzlxN2h4V3FwVmdnVTlCMDduRmhxcE1ycW01VlNpZkxrY3dtUXp5dUkxSHlLWXEwYk1oR2JMZHMybThKaTAwUGxHZEpqeHNmYjlZekI4d3ZwMjNUQ19oWE5wOHg4cTR5SnhWcjRKNGIxellFZkRNNGh3TGstcDV0R3gyUzRBSzlmNDc?oc=5) <sub>South China Morning Post</sub>
- 📰 2026-10-27 [China has successively granted permits for autonomous driving operations to EV maker XPeng and Volks..](https://news.google.com/rss/articles/CBMiT0FVX3lxTE5xbERHUURWVUZOeV9sUzFXbXRwdDNndERiVGphQk9ka2hneWd2MDItWmZ1Q09aRTNENjV1LWZaVG5CMkl5ZzhmMU5jOTVZMXM?oc=5) <sub>매일경제</sub>
- 📰 2026-10-27 [Chery boss questions future of car ownership amid rise of robotaxis](https://news.google.com/rss/articles/CBMiqAFBVV95cUxNRzlPeG5kd29XbUdaWXRDc2Jhb010bEJxakwydHNFbmZRSDQwTVYyQ21KVEFSaHFULXY1dzRSMHFvSm15VC1KS0hCYmxjNTctYlFWaDU2VTQ5ajViVXlGVkZoeGdoV0hkbWlkSEctbVg4LUtFY2lGUkljTGhEYlk5bFAtVzFhTTkybFJhdm1YekEzUmRpakVxd3c2LVU3WU5sVDk4aTRiQV8?oc=5) <sub>CarExpert</sub>
- 📰 2026-10-26 [广州全域L4 示范运营，小鹏Robotaxi 从测试走向商业验证](https://news.google.com/rss/articles/CBMiY0FVX3lxTE5kVWJjc3ZrZ2ZjMFI4X3dUZUZlUHhGU3VFSzVNVHp0dGExZHJxQlgteVQta0JKdHhjR0dmUm5QdXptMUkwc3ZRV2FuWllQdG5RZ3BkdXJPQXE0ZWlGRXVQd2VxWQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-26 [国产医疗神经接口龙头企业亮相北京CMEF 品驰医疗携前沿脑机创新成果迎接全球宾客](https://news.google.com/rss/articles/CBMiUkFVX3lxTE5ZejZQckFJaTBvSHNsMXJxaE9QRVlEUjhnbUpCUDVuRDBIT0NsS1hsU2hLZko5VE42QnAzbDkwdWpRT05kVDJqZFNnOUlIOXlnT0E?oc=5) <sub>www.icloudnews.net</sub>

</details>

<details><summary><b>Horizon Robotics</b> (160)</summary>

- 📰 2026-10-27 [Volkswagen Starts Testing Level 3 Autonomous In China](https://news.google.com/rss/articles/CBMinwFBVV95cUxOV0pfV2FtaTlaTUlxdHc5aFlVMnVyOHVHcGFqNHVKQTNWVDgxYnRmZzZzWFRWblRZZ2JNN2VNR0RRNkZ0UWg1LS1Cdk04cXhXTG5xZDExaS1ENWtKM0pDZ0VqbU9JWDZlWk4tN3d4TVJmTm8xalYxWlllbEdJNUYzTHoyQU9mT1VPTDdMY3JiM2FMaU9sMTR3NGxmcUlGbkk?oc=5) <sub>BusinessToday Malaysia</sub>
- 📰 2026-10-27 [Volkswagen Secures L3 Autonomous Road Test Permit in Hefei](https://news.google.com/rss/articles/CBMiigFBVV95cUxOSDN3dHN0Tm5nR3pQTm1zdmdoR1hDaEJXY1FHVlQzWjV6OTFMM1hRaHh5Skx1RGFwQ1ZteU1WaUZXa09oY3J5cnpoREZQUWJfUkFrNmlWT1dsSHhyUFEzSWxQZm15RjVYbUlUT2E0ZE1jM3NJVTFITXJYRlJOQXRWSFIzNC1rcnZGREE?oc=5) <sub>Retail News Asia</sub>
- 📰 2026-10-27 [Volkswagen begins Level 3 autonomous driving road tests in China, targets commercialisation in 2027](https://news.google.com/rss/articles/CBMi3AFBVV95cUxPX01NaWh3VHFNY3NzLXp3MmpWNHdKXzF1VnR0ZDhnbFdpcS1uYXN0RmpiUXFTLWo1TEdldE5ER1ZYN1o2QzJnTjUtTWVTU081c0JxUmxHM0FXSmVWYV9VeWliMTlZMDZjY2hzNGdEa1Y5cENGTm5lTE1LaVU0bjJMajJEOEw0Y24tcktBYnNtRzhrZ3g4ZnlUUTZTQnBDVWRPOExybjM1dEhFd2lPUXo3TGZTQS1LeFlrZGg4eDBub2wyclVndmVWOUNycVJGZ3pLVVB0VTNyRjRfa0Nq?oc=5) <sub>디지털투데이</sub>
- 📰 2026-10-27 [CHINA-VOLKSWAGEN-AUTONOMOUS DRIVING-TEST (CN)](https://news.google.com/rss/articles/CBMikwFBVV95cUxOQ2ZBT1E5RjRKc2ZhdmY2cExTdDFBS1dHTkJnZm9FdUhzRWlIOUJCcUJEbUZwUmtScEp2b2gwSDhpR0hKRmtZNmxhQ3REZkgxam1BX2tzX2M4OHEzdDhva0ExMUxncjRnWVFsY2pZeTNrWWE5S3FIdmEteDhTbzA1MXJXRU1qeVUteHBCVVAybkY5WE0?oc=5) <sub>Big News Network.com</sub>
- 📰 2026-10-27 [冲顶600亿，李书福押对了印奇_车市动态](https://news.google.com/rss/articles/CBMia0FVX3lxTE9SWmc1NmhvRnNiUDdoTUhwRjB2ZV9yWGRmREZib1p1ejFhd1lzdURSd2lOZ2NBWl8zcVpxVTdNN0FXakVzcjNGdThpa01QVUtfZWxDQXF3cWlhd051bVk0NGlPWXN0SFpNa2NJ?oc=5) <sub>中金在线</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (33)</summary>

- 📰 2026-10-24 [4款7系SUV扎堆上市，问界M7车长5080mm](https://news.google.com/rss/articles/CBMiW0FVX3lxTE14Njc1UEhVa2JDUjZldVh5cm9SaHl2bTB4dE5fQnVEbEpuUE1UTzJQS0dXOU50UjVYYm9IeGwyVFIzQ085QktXaFBvaExySzQ5VFROUnoyY2hCT0U?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-24 [从2026 WICV演讲看：文远、元戎、智驾新程把智驾的下一轮押在哪？](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1UMzkyZlFUZFdhS3l3M1dPYVAxemFzYjRHSFlnWjJUbEVzaDgzRF96VUJiUFhPWTlNdG95czM4NXg1Y0ZlY1JiY2VyV1YxcFZxblpv?oc=5) <sub>电子工程专辑</sub>
- 📰 2026-10-24 [欧拉5城市NOA值得买吗？11.58万带激光雷达，3个维度说清+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE9tdVFPMXpMMGg5UlpDNGt2RzJIMVJ5Slk4dG5SVGJxM0dqaENiNHhVWi1TSWFYTXFuc3VvMXdJMFdHOEY4cUNOcF9peENCbmxFVlVxcDRIMUlUdVdpaTYyWGpaZGY2Q2F1UGxTM1lVU0Zkdw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-23 [元戎启行周光：基座模型成自动驾驶新引擎，推动MPCI向千公里级跃迁](https://news.google.com/rss/articles/CBMiXkFVX3lxTE9wRGVmQ3liVG9hUjNic1QyekVrS3VKVUNZbFJ5WHc2dlR3UHQzdGhCRFVROHVnTl9NLVdENGZIM2hUT1doV01USEtvSHJsaV9iclpoWEd4M1hfVDZFMFE?oc=5) <sub>SmartHey</sub>
- 📰 2026-10-23 [US: Waymo Launches Services to Harry Reid International Airport](https://news.google.com/rss/articles/CBMinAFBVV95cUxOV2M2dkZzWEw4TXdrbU1kMzlPelNRbk5FQU5YbTY1MUNoRUdITmY0a1dzSUZjWE9JdXotNkI5Mkg5RzZQMlZORlM0OUppSVNlc0llbVFMa1NJNHpzLWhEbkl5RC1wSnZsUFNoVDJyUlgxa19OTWVGRFBvMHBIbDlYZllzV3NQMjMwMklTSWp6NWZqaDVuZndFUnpjckg?oc=5) <sub>Future Transport-News</sub>

</details>

<details><summary><b>Mobileye</b> (29)</summary>

- 📰 2026-10-26 [Autonomous & Self-Driving Vehicle News: Tesla, Mobileye, Aeva, Ouster, Pony.ai, NVIDIA, Stellantis, Bolt, Wayve, Volkswagen, Einride, Valeo, Aptiv & TIER IV \| auto connected car news](https://news.google.com/rss/articles/CBMijgJBVV95cUxNLXpSRDZNWTdpaUNvcWdGUWJBRUxfMGlXTXYtNFEyV0NxU0hfTmhxUlQwb2JGN3Y0VW9QS25NeVRPNkxsVV93ZkZGdGp5bW9iU3VERTFwaW5MckVKc0xmTEJVR1NFTFJORXR5SVZ2VlNDY0VFRjhabEo4dkp4WU1xTFpYci1kcWNsNndSNHg2cExQUVlCRVEtb1plX0dLa2diaDV6eU9hX1dnT1pOTmVkZXBNQ1pnUHlZQ1BVX1FEWWJfcS1fejBXbUdWZE5qZDRDUGtmTnFUZVhYTkItWlN5emwyMnRGNWFITHVDTEZwQk9hdXpJT3d3N2UybExoRjRtLTVZUFE4ZFBZQVZJLXc?oc=5) <sub>AUTO Connected Car News</sub>
- 📰 2026-10-26 [Connected Car News: OmniAir, Arbe, MapQuest, State Farm, MIT, Google, Apple, NXP, Mobileye, TÜV SÜD, Audi, Spotify, Mercedes-Benz, Hyundai Mobis & Samsung \| auto connected car news](https://news.google.com/rss/articles/CBMijAJBVV95cUxQU0RRRTJIRGVJZllKWlNWTVREYl9lSzItOGJNU2VwOGo2cWdDT1lXQVpVNWd0ZnN3RnIzVU5pWUluNF9BTUNWUEhQTTZ3bmVCOUtuaGNkdDJEY2dsMGxTVU9iOHROazVSc29TWktSZUZ6V2tJRzViQzRob3RpTWJpQXVfSUJtMXBMVVFWTjk1b3RRWnpaWnJwWWc4N1J6bjl5dlBmX2xHYXVvZ2p0MXJzalJYTG81ZnhkUXp4SzhLQkZRNEV3c1Y0dm9lQ1FldVRqS0NQdTdMMmxkZFVCTXBoUVJMSHNwRk8tMWs5cHFxaksxeGFCdlVaTnZxdk5ucWM3eWhpYkkxNHZ2bGEz?oc=5) <sub>AUTO Connected Car News</sub>
- 📰 2026-10-26 [If Intel doesn’t mess up this time, Classiq could do for it what Android did for Google](https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBrSWJKLVdrcV9FQkhIMHNUck51VjdoSV9vZUJYdzZRaElWczJwSU4yOXlxRzJLRjg3RmEzQWFrRlplQ0xLd1M0R3BuaWpSSHFLdVBYZ1I5NEgxYUhjUGg4aWVJQVZIVWM?oc=5) <sub>www.calcalistech.com</sub>
- 📰 2026-10-26 [Intel to Acquire Israeli Quantum Computing Startup Classiq in $2.3 Billion Deal](https://news.google.com/rss/articles/CBMinAJBVV95cUxQM2JLOHhqZFdHZTZjcFpFVjhEanJoR3hsaGlZcG81aDdFekpVMTlqVkpmRGFEWFBwOTlkZE1XN1dRVHdhMnFza1ppdWlKRldSVTlTRHdaVXZRc2N6ai1HeVNaQ3k1Y3NwWjJkaG5WbHpyOHBUMGpCNDdvaklZM3U3NkNGOWNNTDF6a1o4REg1VEhKNHR5U0x3Yy13bUVCNWF4Ml9oOVRKdmptdzkxRWdWdmhrUl9MaGpfWXZHby1HYzY5c3h3ajVKLXhCVmFrWlFEaTJFVE0zVi1rUDJsdUlIcTFEdE1WejVxX0hMd1ZlMUhfLTZhcTIyREp6MlczUUFqVXE5Q19BX2VSSjdYRElBU2tkWkNieFlZZTE0ag?oc=5) <sub>Haaretz</sub>
- 📰 2026-10-26 [Where Mobileye Global Goes After A 51% Drop](https://news.google.com/rss/articles/CBMiuwFBVV95cUxON1Y4bVE5WURxSnA1RGJCM2p6V01laEViRFhYc3V3aEF2Y1BXZzFaT1dCbVdZVXdBR2RiT281MmJFRkstcEhKZlFSWHhnX2ZTbGVZRjJZOVVDTGctWGh0amdjN09mTVRuZnRoTVFfMzhYOTBBWHpuQ21FNjRsM01meFpzb1dFQUY1RnBnV29GVHFoNmdmTVZLeG10TDNqN3dYdzE1YzZzV19HRHZmb0VZMUY1OHBJVWctelpR?oc=5) <sub>Simply Wall Street</sub>

</details>

<details><summary><b>Aurora</b> (48)</summary>

- 📰 2026-10-26 [Charger Logistics plans to buy 500 autonomous trucks using Aurora’s tech](https://news.google.com/rss/articles/CBMiswFBVV95cUxPTWhOSkVpUjdLRXhNN2F3R1B0WnZXcGVvQW1HdmQ0djAtelhnck5TbzVnSGptUWtZRXQ4U0pxdFdrQ0k4LWNTZW5yTm1RSS1WUEdpZUd3dWJCdzJlUjVzMnVrQ2gxR3VVbl81bXgzWWluWml4bzJPTmhYTDZ6Tjc1T0FkQUNMYlRxTEdkM3JRR2tKaXVmWmtsOXBnNzgwZjJoek9TR0d1ZTFGQ3JVSHI1b1FhQQ?oc=5) <sub>Trucking Dive</sub>
- 📰 2026-10-26 [Charger Logistics Plans to Buy Up to 500 Aurora Driverless Trucks](https://news.google.com/rss/articles/CBMihgFBVV95cUxNRmF4cmJObzZ2NzZSbzVGb3Nvb0lOZXhhT21lVS1fOEM3WUMydWdiSDZVWkVFb3Q5eGJXX1BEbVFzMG5qZi1XVlp6NU1TTHRpamVUSWpBa1VRb3QzbnVlbmZqcDBOSzlVN0RuQ3JIajYtRVRhMUtJblVjUzlwRGEySGlES3NDUQ?oc=5) <sub>Advanced Clean Tech (ACT) News</sub>
- 📰 2026-10-26 [Aurora to sell upwards of 500 driverless trucks to major trucking firm](https://news.google.com/rss/articles/CBMimwFBVV95cUxQODVpVElvVTNvWXl2Qm16VEd2RHJOSHJ5SE1UdTVIOXFsalkzQi0tUVBFVWFUT2tXUzlUcU9MVF9nU19rSUMwSUFtcDRkTXFkX3VyaFlfaGpqNnpIdWtzT2syVVpCbGY1WkU1RGdQeGo0QnVoNTE1RXVuaWpUcnZpMHU5N2l4dHpIOHNqTmhEMk1STWdqX0lpUXJzbw?oc=5) <sub>The Business Journals</sub>
- 📰 2026-10-26 [Charger Logistics and Aurora to Begin Scaling Autonomous Fleet to 500 Trucks](https://news.google.com/rss/articles/CBMi1AFBVV95cUxNUnhMUFlGYkttWWNzRHI2RXd2UXZiNDhnYXQwNkRFRFo4YXlCWVFEWU05eTNZUms3MzZIekZvaUhOaTZoYXRHeDZrVGQ2S3U1cjh6S0wtbWdYMXhsbXRVTmxrcW1kY3JoTUxIeWRzaXA0QktlYWJhSC1hYXZCNHRWNUZXT1A4YnBlVkhOMWprV1p4NHVfU25La3FJMW9ublhfcDRPRnBOSFFUS1JaTWVPbEF1eEpLbEh5Sm5SWTRCLVpoTkFaWHNWWEpGSnV0SGhZMW1MYg?oc=5) <sub>Morningstar</sub>
- 📰 2026-10-26 [Aurora targets 30K driverless trucks, $5B revenue in 2030](https://news.google.com/rss/articles/CBMingFBVV95cUxQMGowWW1ZY1dOc1l5RGxoSzN4blg0VlpXeUpWNG5pOGhudmhmSjZaR0pUc3NwYzd3ckQyZUV2bjJqa2JuazItNjgwMTduOG9kU2NIVXg0WGtoYXJxVE8yUkhFQzZVY1JlU3hldVJReWRmVXllMGNIYnFRTzNLRkg1VHE4dDFIdlZJQmRubWN6UkVRemROOGI5OVBQZ2d0dw?oc=5) <sub>Trucking Dive</sub>

</details>

<details><summary><b>Zoox</b> (68)</summary>

- 📰 2026-10-26 [Austin Robotaxi Jam Shows Waymo, Zoox and Tesla Cybercabs Don't Know What to Do](https://news.google.com/rss/articles/CBMirAFBVV95cUxOTnFtVXVPcmJsbTdQS1NGUzRTbHJEVk03cWxocG5QREFnWjhBelp0ZHRWV2N1dTRvWXFYUWpBZ01KNFRRU3kySjFid2FDS2Nla2lQVE5KX09YT1QzNmV4TGh3Tk40WEZlS2NIc3BoaGU5akVGdmotWEo0d0dOQjFTN1FrZTZmVnlTLV8zdmhQWlJ3YTN5bi1yTUpLWnhmTUNweEo3MWFnZWNNMTRm?oc=5) <sub>Hoodline</sub>
- 📰 2026-10-26 [Zoox, Waymo and Cybercab meet in Austin. Cue the Spider-Man meme.](https://news.google.com/rss/articles/CBMikAFBVV95cUxPVTZGYTcyUEpFTTdUak1pZ0EzM2FSWkRRam1YdlVFMXlEY3VBQzR6dW54cWl6QXRldU1KcmVWQnpkdkFtdUlibG1Fci03bjdodFBQLUNmTVh5bExPTDdDZHVUb1FpQjRMa21wV2tNZTBaZTJEVFFheXpIVkRyR3paRm9oN3RRMVN3SFRJLTZHb0s?oc=5) <sub>Austin American-Statesman</sub>
- 📰 2026-10-26 [Tesla’s self-driving Robotaxi service expands into greater Houston, with a rocket-shaped service map](https://news.google.com/rss/articles/CBMi6AFBVV95cUxQczdjaU40WElhTnV6LUthbmNnRHJ4bUh4ZmtWNDJTYW5GZ2ZxSy15Wm9QZ2x3Qi1pbjV5Q2Vtb0hZay1pb0Vrd0s3WERPQldOcmc3Z3NsNV9mQlRIaWpCSXROU01SNnV4c1hRaGVYZDhlLU8tRE83M3RydTR1X2ZFeGdleTVocWtyNmZBajZCTVZXVnJldFVYdDNadUIweUFoNWdWbmFZYnZ2Ukx0OXNrSnc3RlZ1X2V5UldHM1M2bHliUXlNWGJIeUs4MWRFazkxRExfNUZFVFVkSnJvUWxRUldzZ1BYaWt50gHoAUFVX3lxTFBzN2NpTjRYSWFOdXotS2FuY2dEcnhtSHhma1Y0MlNhbkZnZnFLLXlab1BnbHdCLWluNXlDZW1vSFlrLWlvRWt3SzdYRE9CV05yZzdnc2w1X2ZCVEhpakJJdE5TTVI2dXhzWFFoZVhkOGUtTy1ETzczdHJ1NHVfZkV4Z2V5NWhxa3I2ZkFqNkJNVldWcmV0VVh0M1p1QjB5QWg1Z1ZuYVlidnZSTHQ5c2tKdzdGVnVfZXlSV0czUzZseWJReU1YYkh5SzgxZEVrOTFETF81RkVUVWRKcm9RbFFSV3NnUFhpa3k?oc=5) <sub>Houston Public Media</sub>
- 📰 2026-10-26 [Can electronic sounds help autonomous cars be safer?](https://news.google.com/rss/articles/CBMikgFBVV95cUxQOFNLaHp1SDlyekdsV1BETVlGbG80cE5aVEdhTGFncnI1amZBdFRfVjFmbUwyUk1YNi11RlJoaTFaajk1WnBZSmFITGxiSV9qdHRxNld1TDVmME5hOEhMdGtzNEo1X3JzU3dObjRueWZNX0dLSTIxQ1JWakZyUVB3bmpqbG1iY1RGZ1hpQVJ2UjJmUQ?oc=5) <sub>WVTF</sub>
- 📰 2026-10-26 [Texas streets become a battleground as Cybercab, Zoox and Waymo fight for space in Austin](https://news.google.com/rss/articles/CBMif0FVX3lxTE1UVUZFbnFpaG44ZGZxcm44WGpWay1xYjJPQnd2cVlhUGw5NnZ6U0dsY18wQi02QUYtdGNia1BIbFB1VnAyandXWnJXUDBTSWFQZk5VZHUycFFzXzdkMjhDV3g3T1ZucVJ4cUpQaXVtMHJZMjluWVU3VG45UTBSbGc?oc=5) <sub>https://latination.com/</sub>

</details>

<details><summary><b>Motional</b> (12)</summary>

- 📰 2026-10-23 [Waymo Is Accelerating Robotaxi Deployments. Who's Trying to Stop It?｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE83QXNrSG5UMnZyN2ltY3BENUtsUVBVVk4zbnpNTVNCTENELTBYZjVpY0NqMnFRUFYzVmdMSWdzVWswU1NZWHBRSkd1N3E1WnZxbUVaZ2tneWlmQWU0dTVZ?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-22 [Zoox Las Vegas Airport Field Report｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBuM3U0cTFKZHF4ZjhlSVhzY1k4dlVoMDhWVy1PaWUtcUJKWF9jeEtEczdXbm0zbjhTUXBiVFBpdWplUm1NNHBTbndsdzM5TTZYM1ZJSjVJNXBQM09iRkJJ?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-21 [XPENG Next Generation Pilot (NGP) Field Report｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE4xUFBoMW5mRlRQenVJWmVBMHhyMU5HV3VGQXBzQVhYMXVPXzhKeEhRY2Q0d1pKZ2hTcm81X0pSMF8yUGRwYzE3QlVVRko4YUlNNUhncUNzbTZhSkVveTBF?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-21 [EU Regulators Open Probe Into Booking.com Over Fake Listings and Phishing Scams](https://news.google.com/rss/articles/CBMidkFVX3lxTE1Rd2lBWTFiT2s0UG55ZzNOS2NlQ1JOQkVPX3hwSEhRQ2tTa0ZpS19telVJUmRSclZnZXlBSEF3eURRcnNTUDFIaVZ3VG1rcUFXc1cwOVRiU2hIMnFDY0pGTVVVcTZ6U1Fhc2JVSU9xdkI0eTRiX1E?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-21 [Taiwan Blocks Grab's $600 Million Foodpanda Deal, Citing Uber Ties](https://news.google.com/rss/articles/CBMidkFVX3lxTE9sZHZrRlE3bFZXdlJoUEg5azRoMTJiUnVyLVNKWmNaYVgyeDdGZVJ1bEFTN196cEhuaTFJVFVhVW5fdG5aanN6d0s3MmJmVFQ5Nms3OTBCek1IS09nSkFfLUdTV0pDMkR0TlZTNlltWUQtM1k1V1E?oc=5) <sub>BigGo Finance</sub>

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
