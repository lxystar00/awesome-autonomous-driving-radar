# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-10-01 · 1,240 papers tracked · 37 curated.

**Selection rule.** A paper is listed only if it (1) is primarily about autonomous driving,
(2) has public code, and (3) shows at least one strong signal: accepted at a top venue
(CVPR / ICCV / ECCV / NeurIPS / ICLR / ICML / CoRL / RSS / TPAMI, or ICRA / IROS / AAAI / RA-L),
≥200 GitHub stars, ≥3 citations / month, or a well-known lab with traction. Papers are then ranked by a
composite score (venue, stars, citation velocity, LLM rubric for novelty / rigor / impact, SOTA claims)
with a per-topic cap. See [`scripts/rank.py`](scripts/rank.py).

📅 [Daily digests](daily/) · 🗓️ [Weekly digests](weekly/) · 📦 [Raw data](data/)

## Contents

- [VLA / VLM for Driving](#vla--vlm-for-driving) (8)
- [World Models & Generative Simulation](#world-models--generative-simulation) (5)
- [End-to-End Driving & Planning](#end-to-end-driving--planning) (8)
- [3DGS / NeRF Reconstruction & Sensor Sim](#3dgs--nerf-reconstruction--sensor-sim) (2)
- [Perception: BEV, Occupancy, 3D Detection, Mapping](#perception-bev-occupancy-3d-detection-mapping) (8)
- [Datasets & Benchmarks](#datasets--benchmarks) (3)
- [Safety, Robustness & Evaluation](#safety-robustness--evaluation) (3)
- [Industry Tracker](#-industry-tracker)

## VLA / VLM for Driving

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Teaching Vision-Language-Action Models What to See and Where to Look](https://arxiv.org/abs/2607.01658)<br><sub>Yuguang Yang, Canyu Chen, Zhewen Tan et al.</sub> | ECCV 2026<br>2026-07<br>📑 1 | [⭐ 30](https://github.com/ShivaTeam/DriveTeach-VLA) | Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving |
| [DeepSight: Long-Horizon World Modeling via Latent States Prediction for End-to-End Autonomous Driving](https://arxiv.org/abs/2605.10564)<br><sub>Lingjun Zhang, Changjie Wu, Linzhe Shi et al.</sub> | ICML 2026<br>2026-05<br>📑 1 | [⭐ 31](https://github.com/hotdogcheesewhite/DeepSight) | End-to-end autonomous driving systems are increasingly integrating Vision-Language Model (VLM) architectures, incorporating text reasoning or visual reasoning to enhance the robustness and accuracy of driving decisions |
| [CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving](https://arxiv.org/abs/2607.04179)<br><sub>Zhaohong Liu, Hao Ye, Xianlin Zhang et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 1](https://github.com/MICLAB-BUPT/CritiqueDriveVLM) | End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving |
| [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)<br><sub>Nan Yang, Zhanwen Liu, Linfeng Zhang et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 3](https://github.com/Zizzzzzzz/MVPruner) | Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings |
| [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)<br><sub>Yuan Gao, Wenting Miao, Mattia Piccinini et al.</sub> | IROS<br>2026-07<br>📑 1 | [⭐ 27](https://github.com/TUM-AVS/Chat2scenic) | Validating autonomous driving systems requires diverse, regulation-compliant test scenarios |
| [UniDriveVLA: Unifying Understanding, Perception, and Action Planning for Autonomous Driving](https://arxiv.org/abs/2604.02190)<br><sub>Yongkang Li, Lijun Zhou, Sixu Yan et al.</sub> | arXiv<br>2026-04<br>📑 15 | [⭐ 247](https://github.com/xiaomi-research/unidrivevla) | Vision-Language-Action (VLA) models have recently emerged in autonomous driving, with the promise of leveraging rich world knowledge to improve the cognitive capabilities of driving systems |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 6 | [⭐ 482](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
| [Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air](https://arxiv.org/abs/2605.31066)<br><sub>Tianle Zeng, Yanci Wen, Xueang Yu et al.</sub> | arXiv<br>2026-05<br>📑 2 | [⭐ 1,105](https://github.com/louiszengCN/CarlaAir) | Recent aerial vision-language-action (VLA) models show promising single-UAV capabilities, such as tracking moving objects and navigating to language-specified landmarks |

## World Models & Generative Simulation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [HERMES++: Toward a Unified Driving World Model for 3D Scene Understanding and Generation](https://arxiv.org/abs/2604.28196)<br><sub>Xin Zhou, Dingkang Liang, Xiwu Chen et al.</sub> | ICCV 2025<br>2026-04<br>📑 4 | [⭐ 71](https://github.com/H-EmbodVis/HERMESV2) | Driving world models serve as a pivotal technology for autonomous driving by simulating environmental dynamics |
| [FrozenDrive: Zero-Shot Text-Guided Driving Scene Generation and Data Augmentation with Parameter-Free Frozen Diffusion Model](https://arxiv.org/abs/2606.20110)<br><sub>Yuhwan Jeong, Hyeonseong Kim, Daehyun We et al.</sub> | ECCV 2026<br>2026-06<br>📑 1 | [⭐ 10](https://github.com/daehyunwe/FrozenDrive) | Synthetic data for autonomous driving is surging, powered by diffusion models that promise scalable scene generation |
| [ASTAD: Asymmetric Style Transfer for Synthetic-to-Real Adaptation in Autonomous Driving](https://arxiv.org/abs/2606.29286)<br><sub>Dingyi Yao, Xinqi Zhang, Lihui Peng et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 1](https://github.com/Dingyi-Yao/ASTAD) | Synthetic data mitigates the data scarcity problem in autonomous driving perception |
| [Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends](https://arxiv.org/abs/2606.01164)<br><sub>Jiuming Liu, Chaojun Ni, Mengmeng Liu et al.</sub> | arXiv<br>2026-06<br>📑 4 | [⭐ 237](https://github.com/liujiuming123/Awesome-Interactive-World-Model) | With rapid development of large language models and diffusion-based content generation, world modeling has attracted increasing research attention, benefiting various downstream domains such as game engines, embodied AI,… |
| [Is Your Driving World Model an All-Around Player?](https://arxiv.org/abs/2605.10858)<br><sub>Lingdong Kong, Ao Liang, Tianyi Yan et al.</sub> | arXiv<br>2026-05<br>📑 4 | [⭐ 253](https://github.com/worldbench/WorldLens) | Today's driving world models can generate remarkably realistic dash-cam videos, yet no single model excels universally |

## End-to-End Driving & Planning

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](https://arxiv.org/abs/2609.26792)<br><sub>Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.</sub> | CoRL 2026<br>2026-09<br>📑 1 | [⭐ 10](https://github.com/VAIL-UCLA/DreamStream) | Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions |
| [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)<br><sub>Shen Zheng, Anurag Ghosh, Gaurav Parmar et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 31](https://github.com/ShenZheng2000/WarpI2I) | Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs) |
| [G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance](https://arxiv.org/abs/2606.26017)<br><sub>Hang Yu, Ye Jin, Alessandro Canevaro et al.</sub> | IROS 2026<br>2026-06<br>📑 4 | [⭐ 6](https://github.com/HangYuu/G2DP) | In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors |
| [Fail2Drive: Benchmarking Closed-Loop Driving Generalization](https://arxiv.org/abs/2604.08535)<br><sub>Simon Gerstenecker, Andreas Geiger, Katrin Renz</sub> | arXiv<br>2026-04<br>📑 15 | [⭐ 173](https://github.com/autonomousvision/fail2drive) | Generalization under distribution shift remains a central bottleneck for closed-loop autonomous driving |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 14 | [⭐ 344](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
| [Latent-Centroid Steering: Single-Pass Classifier-Free Guidance for Command-Aligned Autonomous Driving](https://arxiv.org/abs/2608.00237)<br><sub>Meibo Hu, Jiamian Wang, Pichao Wang et al.</sub> | IROS 2026<br>2026-08 | [⭐ 2](https://github.com/codingmlinprocess/LCS) | Vision-language models (VLMs) have recently emerged as a promising paradigm for end-to-end autonomous driving, enabling agents to map multimodal inputs and high-level navigation instructions directly to executable trajec… |
| [STAGE: STyle-controllable Action GEneration for personalized autonomous driving](https://arxiv.org/abs/2607.29517)<br><sub>Zihao Liu, Xing Liu, Yizhai Zhang et al.</sub> | RA-L<br>2026-07<br>📑 1 | [⭐ 6](https://github.com/CarlDegio/STAGE) | Driving style refers to the behavioral preferences that drivers maintain during driving, shaped by their diverse experiences, habits, and needs, and is typically reflected in varying levels of aggressiveness |
| [DVGT-2: Vision-Geometry-Action Model for Autonomous Driving at Scale](https://arxiv.org/abs/2604.00813)<br><sub>Sicheng Zuo, Zixun Xie, Wenzhao Zheng et al.</sub> | arXiv<br>2026-04<br>📑 11 | [⭐ 363](https://github.com/wzzheng/DVGT) | End-to-end autonomous driving has evolved from the conventional paradigm based on sparse perception into vision-language-action (VLA) models, which focus on learning language descriptions as an auxiliary task to facilita… |

## 3DGS / NeRF Reconstruction & Sensor Sim

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DriveWeaver: Point-Conditioned Video Inpainting for Controllable Vehicle Insertion in Autonomous Driving Simulation](https://arxiv.org/abs/2606.31918)<br><sub>Junzhe Jiang, Zipei Ma, Zijie Pan et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 16](https://github.com/LogosRoboticsGroup/DriveWeaver) | A pivotal step in autonomous driving simulation involves inserting foreground vehicles with predefined trajectories into simulated scenes |
| [Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796)<br><sub>Leshu Li, Jie Peng, Yang Zhao</sub> | ICRA<br>2026-06 | [⭐ 12](https://github.com/UMN-ZhaoLab/Pocket-SLAM) | 3D Gaussian Splatting (3DGS) has garnered significant attention in Simultaneous Localization and Mapping (SLAM) due to its advances in capturing fine-grained geometry features and synthesizing novel views |

## Perception: BEV, Occupancy, 3D Detection, Mapping

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Deformable Gaussian Occupancy: Decoupling Rigid and Nonrigid Motion with Factorized Distillation](https://arxiv.org/abs/2605.28587)<br><sub>Yang Gao, Wuyang Li, Po-Chien Luan et al.</sub> | CVPR 2026<br>2026-05<br>📑 2 | [⭐ 22](https://github.com/vita-epfl/DeGO) | Understanding dynamic 3D environments is essential for safe autonomous driving, particularly when reasoning about human-centric, nonrigid agents |
| [FreeOcc: Training-Free Embodied Open-Vocabulary Occupancy Prediction](https://arxiv.org/abs/2604.28115)<br><sub>Zeyu Jiang, Changqing Zhou, Xingxing Zuo et al.</sub> | RSS<br>2026-04<br>📑 5 | [⭐ 138](https://github.com/the-masses/FreeOcc) | Existing learning-based occupancy prediction methods rely on large-scale 3D annotations and generalize poorly across environments |
| [Revisiting Token Compression for Accelerating ViT-based Sparse Multi-View 3D Object Detectors](https://arxiv.org/abs/2604.14563)<br><sub>Mingqian Ji, Shanshan Zhang, Jian Yang</sub> | CVPR 2026<br>2026-04<br>📑 1 | [⭐ 9](https://github.com/Mingqj/SEPatch3D) | Vision Transformer (ViT)-based sparse multi-view 3D object detectors have achieved remarkable accuracy but still suffer from high inference latency due to heavy token processing |
| [Horizon3D: Sparse Radar-Camera Fusion for Long-Range 3D Perception in Autonomous Driving](https://arxiv.org/abs/2606.31096)<br><sub>Geonho Bang, Geunju Baek, Dongyoung Lee et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 23](https://github.com/geonhobang/Horizon3D) | Long-range 3D object detection is critical for safe autonomous driving at highway speeds, yet existing radar-camera fusion methods remain limited at extended ranges |
| [Explainability-Aware Frustum Attack: Exposing Structural Vulnerabilities in LiDAR-Based 3D Object Detectors](https://arxiv.org/abs/2606.29963)<br><sub>Chengzeng You, Binbin Xu, Soteris Demetriou</sub> | ECCV<br>2026-06 | [⭐ 2](https://github.com/SecMindLab/Saliency_LiDAR) | The structural vulnerabilities of point cloud-based 3D object detectors remain poorly understood |
| [PointLAM: Local Attentive Mamba for Efficient Point-based 3D Object Detection](https://arxiv.org/abs/2609.21780)<br><sub>Xuanming Shang, Weijia Zhang, Chao Ma</sub> | ECCV 2026<br>2026-09 | [⭐ 4](https://github.com/PointLAM/PointLAM) | 3D object detection from LiDAR point clouds faces a fundamental dilemma: voxel-based methods achieve efficiency at the cost of geometric quantization, while point-based methods preserve fidelity but suffer from prohibiti… |
| [Vernata: Self-Supervised Learning of LiDAR Point Representations](https://arxiv.org/abs/2608.06919)<br><sub>Oliver Lemke, Alexander Liniger, Abel Gawel et al.</sub> | IROS 2026<br>2026-08 | [⭐ 18](https://github.com/rai-opensource/vernata) | LiDAR serves as a primary sensing modality for robots operating in outdoor environments |
| [Towards Compact Autonomous Driving Perception with Balanced Learning and Multi-sensor Fusion](https://arxiv.org/abs/2606.02979)<br><sub>Oskar Natan, Jun Miura</sub> | arXiv<br>2026-06<br>📑 44 | [⭐ 9](https://github.com/oskarnatan/compact-perception) | We present a novel compact deep multi-task learning model to handle various autonomous driving perception tasks in one forward pass |

## Datasets & Benchmarks

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [SearchAD: Large-Scale Rare Image Retrieval Dataset for Autonomous Driving](https://arxiv.org/abs/2604.08008)<br><sub>Felix Embacher, Jonas Uhrig, Marius Cordts et al.</sub> | CVPR 2026<br>2026-04 | [⭐ 9](https://github.com/iis-esslingen/searchad_devkit) | Retrieving rare and safety-critical driving scenarios from large-scale datasets is essential for building robust autonomous driving (AD) systems |
| [Towards All-Day Perception for Off-Road Driving: A Large-Scale Multispectral Dataset and Comprehensive Benchmark](https://arxiv.org/abs/2604.27499)<br><sub>Shuo Wang, Jilin Mei, Wenfei Guan et al.</sub> | RA-L 2026<br>2026-04 | [⭐ 6](https://github.com/wsnbws/IRON) | Off-road nighttime autonomous driving suffers from unreliable visible-light perception, making infrared modality crucial for accurate freespace detection |
| [123D: Unifying Multi-Modal Autonomous Driving Data at Scale](https://arxiv.org/abs/2605.08084)<br><sub>Daniel Dauner, Valentin Charraut, Bastian Berle et al.</sub> | arXiv<br>2026-05<br>📑 2 | [⭐ 399](https://github.com/kesai-labs/py123d) | The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics |

## Safety, Robustness & Evaluation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [CCFM: Collision-Constrained Flow Matching for Safety-Critical Scenario Generation](https://arxiv.org/abs/2607.04451)<br><sub>Ke Li, Kaidi Liang, Yuxin Ding et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 3](https://github.com/KELISBU/CCFM) | Evaluation of autonomous vehicle (AV) planners in safety-critical closed-loop simulation is essential for real-world deployment |
| [Lipschitz Optimization for Formal Verification of Homographies](https://arxiv.org/abs/2605.23203)<br><sub>Jean-Guillaume Durand, Panagiotis Kouvaros, Maxime Gariel et al.</sub> | CVPR 2026<br>2026-05 | [⭐ 2](https://github.com/jeangud/homography-verification) | The adoption of vision neural networks in regulated industries requires formal robustness guarantees, especially in safety-critical domains such as healthcare, autonomous vehicles, and aerospace |
| [CADET: A Modular Platform for Evaluating Distributed Cooperative Autonomy in Connected Autonomous Vehicles](https://arxiv.org/abs/2606.04072)<br><sub>Pragya Sharma, Brian Wang, Mani Srivastava</sub> | ICRA 2026<br>2026-06<br>📑 1 | [⭐ 0](https://github.com/nesl/cadet) | Deep learning models are increasingly central to autonomous vehicle (AV) pipelines, yet their integration has traditionally followed a monolithic design where perception, planning, and control execute on a single onboard… |

## 🏢 Industry Tracker

Latest 14 days of news, official blog posts and new open-source repos from tracked companies. Full daily feed in [`daily/`](daily/).

<details><summary><b>Waymo</b> (131)</summary>

- 📝 2026-09-24 [Our Vision for London: How Waymo can Support a Safer, Connected UK Capital](https://waymo.com/blog/2026/09/visionforlondon) <sub>official blog</sub>
- 📝 2026-09-22 [Introducing transit rewards](https://waymo.com/blog/2026/09/transit-rewards) <sub>official blog</sub>
- 📰 2026-09-30 [Minneapolis council advances proposal to mandate human drivers in robotaxis](https://news.google.com/rss/articles/CBMiuAFBVV95cUxOVklnZnJWWmxNa1kyLWIyUXMwb1lIVks4YnRVUjZsYzlwQndqTjM2eFdQLUQ1X2g4M1oxZWVGNzJFNnNrOUVoNGVGbEI0ZmVsLUdWMlFac052djN6UHRqeGkxQ3hqVk9NUWFweExpUnJGaHlkNTMzWnkxX1owemZLRk1HOG40VWhLUWtqdDNfMlhvQkZYQ2hZMG1MMHV3elFBNUYxbThQRlVvYm00NHpCTV9udHo4aW5F?oc=5) <sub>Minnesota Reformer</sub>
- 📰 2026-09-30 [The unexpected challenges facing Waymo on South Florida roads](https://news.google.com/rss/articles/CBMirwFBVV95cUxOX0lGdzBvbS1MdnRqWTFQMjJrbWd6RThabHNtZzk0aFJkTzdBSTh0eHB0M1ExVmh0V01qWDl3aUx1YW1ySEhjYjlyM2ROemZVekZXaXIzR21nS0lVcWcxdm5zNkE4cDlsSGpERENHMVhuUFdQZ0VfbllhdGt5NTdGRE91SjRhWnNLRE5FWUF4U1JZYUFNMGpGWVRXWU5HaDQ1cDVxaFNuVDhsQlBpaWVv0gG3AUFVX3lxTE1sWlh2N09YUklSNUhOa2RPNVZNTVc2b18taEZ2UXpnSnFzWVFnXzBHbnNhUkZTWXMtU2ZpLUIxZDlvdlFoMUJXdVdUTUJZVktBYU14X0RKc05OTzIzOEpBenMyLV93di05dFdCNklUSVJmWWJjM2JiOFVIUUJLekNQS0RmcTNZLWJ5QkJ1bVVFSW05bVd1amM2ZkQyb29WZ3RnMVg0QV9sNWdBVDVRbDVSQW1iQ1ZEbw?oc=5) <sub>NBC 6 South Florida</sub>
- 📰 2026-09-30 [Waymo robotaxis may be available to buy one day](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9oSzg4V2o1VnNOWHBSSDljLXdkaWZKTW5DM2VXdGtxdHRKYU84dDhTVzg4TTltMjdHVzNQUkdkNHRMNkRfWnlicFdkMDhQOWluQ3o3MHNMRmo4aThUYVhr?oc=5) <sub>Mashable</sub>

</details>

<details><summary><b>Tesla</b> (199)</summary>

- 📰 2026-09-30 [VLA 2.0 vs. FSD in Amsterdam — Part 3: Comparing XPENG & Tesla](https://news.google.com/rss/articles/CBMimgFBVV95cUxNRnZjMEdLeXBkWldneUxETFcxVXRscWhMSHF6WExyNTVDbC1sZEV6d19YcHRSTkFLdWZITU9HOFdFOVl1bk5Za01TeGFOdV9jUUw4MTkwd1JVSW1qUGhWci1qYUg3Uk9PSGNPcFRXN0NWSXVfd29EajhlbnI5RDZkcjhhQkFXVGtSSDVPOTdDZ3A2dU5CYURfWEFR?oc=5) <sub>CleanTechnica</sub>
- 📰 2026-09-30 [Tesla Robotaxi fleets are the new crypto treasury for zombie companies](https://news.google.com/rss/articles/CBMilwFBVV95cUxPeFowNmhCbjY0d0prVHVhM0U0RExXUDE3V0Q3UFZDcVp4VktBV3pqNTl3c0dramhoMDdSUktrTmVVRWpNTGg4LXNuVW5NZmN4bTRiZlNGVlhIbUhmN3RzNkp1M0FQQktGTm9uX2p2dl9May1ZTFRydnVlOHhXM3o5NTBsV01iZ1ExNTNONGl0dERqWkxDVzNR?oc=5) <sub>Electrek</sub>
- 📰 2026-09-30 [KIDZ AI Inc. Submits Initial Tesla Robotaxi Fleet Procurement Inquiry, Unveils Autonomous Fleet Operations Strategy](https://news.google.com/rss/articles/CBMi5AFBVV95cUxQTkhlNUc1blNjT0hFN1d1a0xEX2JWd1VYcHYybXJxMkd3ODBqMDhOcE04YUFsNzFjV29Va1BZSFl6S2Mxb2ZESVEyYWlzbGFTU2syTVBqNDRXZTFMald3R1VnOXB4eUlCeGZLR2pJdTBMNEM3M3NNWV92bl9xNTY4d2s4MjViQlJFY0V4YkF0UDhfTWtfRENzYzBEMGMwUkY1c2RnMU0wQ2gzNFVjdDNHQnpyaUZyZXhXdGV3WmhENUVuTTFySVFDaXljb1VySVJ1YmJSbmtKdlNwelNfc0ZHclJyX1Y?oc=5) <sub>Quiver Quantitative</sub>
- 📰 2026-09-30 [Tesla Locks In $30 Billion Credit Line To Fund Soaring AI Spending](https://news.google.com/rss/articles/CBMiowFBVV95cUxPRXVucTR1TS1QRm5iTXhLQ2hSUVNJd2J1ekhJeGtia3o5R2VZME85X0tiSkV4UE1fTnY5Y3hOejYzQm02eUR6eWM1TEt4N3FFRjFBYmhhWlI4OE5lb3FKa3RPQWpBNHJVM1kyeFI4cmVGdFdaNEZlRVBvYU9sNlBtOU1DeU00VHFGMXdubGszVFpwWUFjb1R2TE11UmZINFdnZ2Nr?oc=5) <sub>Investor's Business Daily</sub>
- 📰 2026-09-30 [Tesla Expands Cybercab Fleet to Strengthen Robotaxi Operations](https://news.google.com/rss/articles/CBMikgFBVV95cUxObGEwc2VvZnYySDBKVW90VG9RbUpYcFd2Z0J4MnRFWWpGdFdaaFR0ejROc0ZraTV5MHNkQ005RWxoRmk1Z3g3dUUxRDg0TjdfdGVJU0VJNkd1UXYycTdHQm0tX0ptbTBJYm9zMi1LUTlSTVVURHRTNU95c2RPMnBhdlZxa3NwQW5aYktQMkY2eGJlZw?oc=5) <sub>Yahoo Finance UK</sub>

</details>

<details><summary><b>NVIDIA</b> (129)</summary>

- 💻 2026-09-18 [NVIDIA/swe-serve — SWE-Serve: an agentic benchmark of 53 production inference-engineering tasks derived from merged SGLang pull requests, run with Harbor.](https://github.com/NVIDIA/swe-serve) <sub>GitHub</sub>
- 📰 2026-09-30 [Delta and NVIDIA collaborate on autonomous driving systems](https://news.google.com/rss/articles/CBMikAFBVV95cUxNMEtkX3hQSXVIekdielBtR3Y2NTBJT0VaNHhDYmJ4RTFWTzRPQ0pteXltZ1JlT1phd0duWmhWT19LOHZNTTNxUTdlSFhlTUVPTzh1TVFmQWsxS0VOc2lfSUxrdkxkVVpHTlFQeE0yd1JLVHBTbEh3YXNEUHJoR2Uwd1hGYnd4SFdabXZHNW16X2M?oc=5) <sub>Engineering.com</sub>
- 📰 2026-09-30 [Delta Electronics to advance autonomous driving with NVIDIA Hyperion](https://news.google.com/rss/articles/CBMimgFBVV95cUxNWThDXzdCcEFWakE4d2hFZ2dMVmxKOHR5dVRSbm1YRDk1eTBGVjFmMlllbW1FbURCUGdHWjlXT2o2d25CN2J4NEJLem8xVE5RNDVrYVdvVXltVUZWbURIWTg0NkFDaFZpa1NUSHJmdWlGY09hZkV4SG1EQ2xhempzWXJzMWhkR0F3QkFBXzFTaE00a1FCbXh0V1dR?oc=5) <sub>Engineer Live</sub>
- 📰 2026-09-30 [AMD's $8.2 billion World Labs deal is a direct answer to NVIDIA's Hugging Face buy](https://news.google.com/rss/articles/CBMi0AFBVV95cUxPa1NRV0lSdWVYUkZNN2gzemFMNVdnRFo0YXQ1TU9wZUtBNEM0NE9oWHpnMC1aZGVpTjdvZ21yUVZzdE9VQW5RaUZKWjMwQndrQWZxVWN0SF9ld2dzbWJudEU4YlBNNWFlbE8wNU94VWQ5U3dmdVB5Q1pEX2poY2l6MElHUVNWRkZqR2xocTFPUW9ucWZ6S2gxQTZaelN0amNlRzI2bWk3R1Rta1FSc0pyQzhFcDRPYThlRDhjUWV3bU9ZUG4wSTNuQXl0YnBYMmQx?oc=5) <sub>TweakTown</sub>
- 📰 2026-09-30 [Nvidia, AMD chiefs join Tsinghua advisory board amid China's AI drive](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5OZmp5N2RVQi1vbWtSNzNCZDZaY0lGdENPN0RjejZtemE3d0FTaEhERkVmb29ZZ0hDV0xZT0dQbVFQMXlmSEFjZEkwTGFiOGpEbTRaZzdNcXEtd9IBWkFVX3lxTE5OZmp5N2RVQi1vbWtSNzNCZDZaY0lGdENPN0RjejZtemE3d0FTaEhERkVmb29ZZ0hDV0xZT0dQbVFQMXlmSEFjZEkwTGFiOGpEbTRaZzdNcXEtdw?oc=5) <sub>mlex.com</sub>

</details>

<details><summary><b>Wayve</b> (55)</summary>

- 📰 2026-09-30 [Uber Heads Into Earnings With Fresh AV Win – Wayve’s London Approval Puts Robotaxi Ambitions In Focus](https://news.google.com/rss/articles/CBMitwFBVV95cUxQRVZJYm1EckE4SzRlX0sxR1RhUlhiOGQ4aTZyRHZ4V1R6OGY2czBoZTZ2ZHl4aW9lUkNQNENXMDZkOGc2QXZoZUpRRGxSaG54a2ZYNlhDekg2SG53cXZ2TVBpVUZWNTFaZXg0a09QMnZiMThWVTBlSkNUbjUycGp1R1JtUmtZcGhuRFRHWVdsbHRvdGhWVTYyQVIzZldnUHN4WUozNDNleEh6RjNMUXRQR3BTTlN4NW8?oc=5) <sub>Stocktwits</sub>
- 📰 2026-09-30 [Portugal, Slovakia and Norway Join Initiative on Autonomous Vehicle Testbeds](https://news.google.com/rss/articles/CBMirgFBVV95cUxQWmtzV0pPLXRnZWF6RDQzaV94VmlDTEVjMi1BOEtBZDZVRDZoeDVzT1dROGRVN3hQcjJneFBKLVZSa2Z3aU1kc1BLQjZhT3B2Z21weUpzaUF6UDJQNms1XzJkUWJwY0d0MklJMTUxUmZ3T2xMRTVyS052eDBObWx2UFRBenJqVGROVF8yODktZDR5Q1dqLXhDX0YwendmV24yOXlfX0hvdjdDR1hJX1E?oc=5) <sub>Future Transport-News</sub>
- 📰 2026-09-30 [Marie Claire UK Brought Some of London's Most Inspiring Women Together to Talk About the Future—Then We Talked About Everything Else](https://news.google.com/rss/articles/CBMihAFBVV95cUxNMEhlQmZkQTIwR2tUaXJReXNKTlpEaVp4bjh4ZWlVYnpvazdPWHNva1V0Z2IyeVV0X1kyRk5LdzNTQ2pWNlVITVlURDNVSV94UW9DYUxISU5fU1VUT0hiM3dJd0RQM0F5dUllRWZnc1NMbnNPTXlha09mVmRhMXM1SG1ROWk?oc=5) <sub>Marie Claire UK</sub>
- 📰 2026-09-30 [Mercedes-Benz Ties Autonomous Driving Deal to Sweeping German Cost Overhaul](https://news.google.com/rss/articles/CBMi1AFBVV95cUxPVTU0SkhqekFmQ1dCcWgxcnk4YWdXTWF5cURITHd3WEZOOXh6b093TFhYUGEybmxudllrelNpSXBya2JBQ3l5UUtNS2RObjY2T29ETHM0TWNvUFQ4allkTHBkS0huX1JnbktKY0xQR0dfVkNCZU1JbkxzNFM0T1BWWUZ1ZmxlaWdYQlpuT3RuZXFrZmlIOFNvb1QyVlJrcEVHUVFHQWlDUkctZDluOWx5N2ZKeDZyZ0lLSExlbjFkVXRkYVE5RGNGbEJjNWlPcU9LQ25iNA?oc=5) <sub>AD HOC NEWS</sub>
- 📰 2026-09-29 [Nissan to Launch Autonomous Driving Project in Cambridge](https://news.google.com/rss/articles/CBMilAFBVV95cUxPc1lnTUNoYWFOOTdqVWpob25tY0pkRmluZHhnNGVTVEstN0t6cXJ4SXBHV0NTcERjdFNCcDVKWlVaT1NLaEsweU00dlhsMl8xNW9aQzVSX25xWDlKVXRQWGNoZmx1blVWRmdnM0VRTEVnUTlyNHJxS182TUpxblpraG8zdnc2Vl9iZUVqSHZqOHJCMXBS?oc=5) <sub>Future Transport-News</sub>

</details>

<details><summary><b>Momenta</b> (121)</summary>

- 📰 2026-09-30 [上汽大众ID.ERA 8X预售，1.5T增程/Momenta智驾，价格25万级别](https://news.google.com/rss/articles/CBMiW0FVX3lxTE11emZVVzlRNFZQbm5hVW1oRC1PclVXb2EtNXYyalJBMG5tczVENTJjQkdPX1JkWlJueGNSWUtzeTBJdDZMM1l0OW5ybnhCV1R6NThVV3VmYUtjWW8?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-30 [Mercedes-backed Momenta targets Dubai and Europe for robotaxi expansion](https://news.google.com/rss/articles/CBMiugFBVV95cUxOd3FjRE9WRlF3Mm8xRElBMkNyanI1MDJhVFVjcXBOMmRpeFluZVdOWkJ3dGVscDNkSUd4aW9lT0JlbV84am5IZU9xNWNYcEQ1bnpWbW5PeG42WWpaRUx0dXd1WDhRQmpQZ1lzakJ4VTlJcUdzQjVoTzNLZ3FaWGN2akZjaUVWVm05OFh2U3ZWOFFvbUpYc3FDM0RhN0JINGUtb2lXR1ZCTEFVQUhwY05QZ3RmX1l0TVJvRGc?oc=5) <sub>Reuters</sub>
- 📰 2026-09-30 [Mercedes-Backed Momenta Targets Europe for Robotaxi Growth](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNajdPSW93b0pqR2lPcnlaMllLWC1wNkVFQ1Q2d3V0OTVVbFdRTlhjd1VWcnRyLWVLUmJtRVEtcmxCMjFRa2dzNm9fZzctRG1tTmRheU1KRm1BdXEzam16Tl9EaXdaY2MxeEdmSkxLYVlDTnJyaGxsQVZKcllDdFk5NnQtTWl3MFlzazk4ZlZJNG1aUkM4VGRVVmxNdnk3OEw0NzdiN2NjSmd4Zw?oc=5) <sub>konsulteer.com</sub>
- 📰 2026-09-30 [Mercedes-backed Momenta plans massive Dubai robotaxi expansion in 2027](https://news.google.com/rss/articles/CBMisAFBVV95cUxPcU1MdDItX2FuU3VUN2FDcnlxQnpqSnB6RTMxdkV3amxUeXN6MElVdDNjVW82ZlIydlR4cU1FNWFYdkhFSHVrQjhidmI4bXVKVktlQktVeEFWZUdNQ0NtaXZzbE11NjRGX01vbngzNERJbTk2TVk4aE5YQk5BSkJZOTI5d3VuNmJoVG9ZNHN3NllNSXpzdEJuUXJGRTlyNzh6bWZSTEJ6dFJVY3Z5bnJ3Yg?oc=5) <sub>Arabian Business</sub>
- 📰 2026-09-30 [BMW新世代智驾有多强？Momenta R7世界模型加持，实测环岛鬼探头+90%续航达成率+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFBxeWlyS0I2V3JfbEJMakJTSXZkWFM0WnRHaHMzUUlPdUlHc3gzN0c3MzJUZldWX2h0MDMyS0t3RlVNbnZpOEg4VTh5RkV2US0yRGxIUW0wQkYwd0lKU0lvUUkwZ2ViTmJ2OEVwXzBDRmRfZw?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>XPeng</b> (171)</summary>

- 📰 2026-09-30 [华为智驾对决小鹏GX，奕境X9这30万值不值](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9XeXNtVlZkMzJzUFlCVXVOdW1zVkdLTF9XZUwybEJJZXJvX1RKX0ZpOW1hLWM0U2YxZ1dWRk9MNkdFcVZqbEJ3dTB4Z2RfTjg1MFRKZkxYYU1ocW8?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-30 [XPeng (XPEV) Puts Humanoid Robots And G9L SUV At The Center Of Global Plans](https://news.google.com/rss/articles/CBMimwFBVV95cUxPTVFNQ1l4ODVKQldEWmRJVUdJS1lxcXBsOWl5TS1DazRhVTBOR2c0WUw4S3c3UUZQbWQ4UU1YYXYxSXhFTWtBejhQX2xvQU82Nm9kNlVKZjRxbWwtMFctT0ktb2lhMkRFYUc4UjlqaVphRkdNWUJyTExUblVyS2hyU2tNSGdzc0p0bTJEcFZhRkx6YnpqeHNDWHloWQ?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-09-30 [Gasgoo Daily:BYD’s Xi’an Battery Project Enters Full-Scale Production; XPENG and Banma Develop an Automotive-Grade AI Cockpit; PATEO Signs Global Supply Agreement with Jeep](https://news.google.com/rss/articles/CBMizgJBVV95cUxPUTBQV2s2NFdRaUNDTUhDVzVBLWFlU1g1aE5xbFVuNTlGVDFyVmJiNjJrRUh3bDYwMjgxZEtlSmx4YmY4UkU3S3RNOHpvOE5jd3VidnNjbHhjTmVHajFfdFVmLWM5ZUl3NE9DR0J4RHBsUVhKZ2Q1cjRmVWdPZVhUbXFWT280cVNRdnNseWhTMDFhM0FNZDlmS1k1bmExUGJxTExEMEx0M0dRU3hhY1NkSGQyS1Nod04zZGl3bDl5d2NYbUVUSzQtemtTeWktMS1oVFg2d29wV3JNcV9aRlYtRW5KaldpSWV4QWxFQllzVzYxZGhobk9OMnE4SUdicS1PMW83WTNaOTR6RmlhSEx0Rm82ekRUVEoycTVvajZ1Y1M2RU5jUHYwRnEzVy1qSzRnN3VrVk96cjNvaDBvQzQ5YzNvQzA5ZVBrem1OSjJR?oc=5) <sub>Gasgoo</sub>
- 📰 2026-09-30 [小鹏G6同价位买燃油插混还是纯电？3个维度说清+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE9SMFpqR3FKUDRNYUdGUnF1ZHhKWmthUjVIUGotdkRla0Etekx6VjlUbnU0cVhYTVFKMlhobmN0YzBrU00teTlNVmRqYkpGTFNsSHZxajBvSDVTX3A2WFEtZndCMW5aRmhWVnpwalM2eXdmUQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-30 [2026智驾好的车有哪些？华为小鹏理想三分天下，这5款闭眼选不后悔+FAQ](https://news.google.com/rss/articles/CBMifkFVX3lxTE1neXN1UWJIV1d0WmlET2JQcm9vbnllVnUwRzQxUk5OZ3VKUjNiMEdpUWZUQkNQVHRuVWM1cFdETHJHYVc3RlFmVTRqUHV0Z241TU9vbnZFUzI4TWxPNlNlcVVqSXU4OUlqTTlaWm4yNmNnMEQ3YkRtaWlvbUlYUQ?oc=5) <sub>finance.sina.com.cn</sub>

</details>

<details><summary><b>Li Auto</b> (122)</summary>

- 📰 2026-09-30 [问界M9 2026款智驾：6颗激光雷达+L3预埋，50万级智能天花板？+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE1scmZ2M3hSOWYwb2dhWGR0MEtpcTMzMFQtU0sxMnAyUWZFdXZKa19WZFlZZFVmSTJaR1dyVkZqYzhGMFhuNUhiMlMxb3RKWHViVXVVcE9maG0zUjE0SnByMGtxeTA3Uk13UVdUVWRqNVBfQQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-30 [BMW, Li Auto, Lucid, Bolt](https://news.google.com/rss/articles/CBMipgFBVV95cUxOUUREQXZCSWFSeTFWSTRzMjl5TFZrRzdySHA4ZXUya3RrRDNfTHN4bWdWOWZwVVB5NnhUYXJrNW1fYk1zVklvZTNyWEk3ckdtSU1zUjJHUVIwSUpZX0o5T3dDb3Qwd18wRFpXQ0pBaVJvZE1UMER5UTI4aHJidVU5MXZEX3d2NzdBZ1NVOURJdlpXU0prTXczYnlmZXB3LUhwYmxSQWV3?oc=5) <sub>IAA Mobility</sub>
- 📰 2026-09-30 [Li Auto Chinese Luxury Auto Brand Planning To Launch In Malaysia](https://news.google.com/rss/articles/CBMiqAFBVV95cUxQT2QwWmY2MHJSVndjNlFVREliLVZ4bjN0ZWtQR085QzBhYzlBNXJHZG4yWTZVZGRwek9CQmdFeThSWTZyYmxVY2hFMVVqN1JZTWRuZDJyZWlvVFlVZnBaa2pFS1U5QkFWYm1Cbk9semlubFRHU0ZHVHFROTI4ZXNBSEN1dVUzeE9qRFFhQ0hTTlBfMXhreXY0S1dwV1E1WGhWU1BsUldremE?oc=5) <sub>Newswav</sub>
- 📰 2026-09-30 [40万级六座SUV路线之争：神行者8的全场景野心 vs 理想L9的家庭哲学](https://news.google.com/rss/articles/CBMickFVX3lxTE9Ha1pIbTJUbU5uQ3gyOUZFN2FPU3FrdFdMYlJZLXd3dnkyTDNnM1hYb0toeUc0eDBhRGJETThORnJoT0stQU1Mb2liREVUWU04c2tCTmh4U19ZeVJ3R3o3d091X1p4Nmw5cnhBazNXcExGdw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-30 [理想L9 Ultra限时选装包发布 马赫具身智能套装2万元](https://news.google.com/rss/articles/CBMiXkFVX3lxTE9OTXNIY1dlbGVlYi1LSy1Wd2xyMmpqNktmR1dhd0otRmdMdkVqb0czVncwUkV3blNhYnlYUlhpeEFKcmc4Sm0tMUljSmFyNEFKS0RQdmh1dTJJSFc3eWc?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>NIO</b> (129)</summary>

- 📰 2026-10-01 [周末带娃去郊野，智界RX和蔚来ES8谁更合适？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5PUzBHQmZ6R002Ry00S09SbTlhSVk1TEsxWm91cXNGdGk4ejZOdjdiX1BrbkUtUlYwZ0ZWblBUSHBqOGU0NnBJeFZxMkhGX0ZndnM4MmxyZWpUQ0U?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-30 [HSL to Serially Produce Indigenous JAYA AUV, Boosting India’s Underwater and Maritime Capabilities](https://news.google.com/rss/articles/CBMi0AFBVV95cUxNWnVyR0E3THFCUThmOE9FWjRpN2d6YTN1TnVEenJxMzdIX2RDYnFZS2FZd3Nub0swQUJYNjlTZEJmb2Q2amVySjJ0b0ZxM1c2NHZjMnVnYWFhMThPTVB3ckJDbHdpQmY0dXVLRzB3UkpKZ2hLejZHS2EzRlVtVTBCLU5CRnhvQjNwSWR6dlE4SFBneWZnNlJhenBYeUduM1NCTC1IbkRNcWRMTTNYSGZ1bm00UWJfLWx2dHlHbmp1a1A4R2tfalZtRWVTUnhyNFd4?oc=5) <sub>Indianmasterminds</sub>
- 📰 2026-09-30 [Hindustan Shipyard to Serially Produce Indigenous JAYA AUV After ToT](https://news.google.com/rss/articles/CBMipgFBVV95cUxQSDA2MUFmTThCNnE0SXYzckJzZjNNSlRvNmlFbUN5RFVkZ08zWEFPOEViRDhmZWRKYmpQeVEtODk4WGxqZFV5Rzl5QURDVGw1eUVfUEZCNUhaSTlVVG0wY1B5TUN4eWZ1aFpkWnF2eUZDem1KRHNDMHh6aUlQRXFQSFhfMGRKT2w4b3YxdVd2TlpqSEdJLU5qUkk2S2Q0dWZIS0cyQ3BB?oc=5) <sub>PSU Connect</sub>
- 📰 2026-09-30 [李斌回应蔚来完整视频全解读：换电开放、智驾兜底、长期亏损？3个维度说清+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFAzaWlJcFlSZW1HWEFJLVVIelNCbGJNdkJOZW1qWFMyYTVvZUtGN1Rmd3BEaW4taDQyNzZfNXRrMkVvaG5UbWVWWDR6TGtNSmplTFRRd2FSSVhnRmNkOGVKMTJEYURWUUFPdUNkOVpzbFZPUQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-30 [蔚来NOP+精准识别施工改道，智驾走对向车道](https://news.google.com/rss/articles/CBMigAFBVV95cUxNalVUczQtYWVxY3hfQ3ZOWTBiRGdhWTBXSFl4M0dYZHZWWXRTVENPRnVpZmRWS25MN1N1RXRHYjFNWTJsNU95c2dqOG5zalp4QzVrV0Fod2FHX0V3Z0dFem5nTHJIQnRUYUo0OFBfREpWREVXWDgyTl9vQmlZUm83dw?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>Huawei</b> (246)</summary>

- 📰 2026-10-01 [华境S大六座SUV 9月交付7416台：连续5个月增长，标配华为乾崑智驾ADS 5 Pro](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNTFlOOWpUaUlPV0dna01PU2I5dXJhYjlUQ1BzYno1NWtmR1pVSTFiLUJnWXAzaXN5REFIdW05Rzd1Uk44ZUlkZFRKVm1ranRVVWYxb3Y4QnVMUGpJMVRpa3ROUTlhLVphR0lDa0JQTFkxZWZMQ0pCYzJUNFc1M2hHd2xUaUNkd1hG?oc=5) <sub>搜狐网</sub>
- 📰 2026-10-01 [华为乾崑联合小红书推出全网首部智驾路书，5条路线大家可以参考](https://news.google.com/rss/articles/CBMijAFBVV95cUxOaUN4U0dIWk90anBEeU9vaG0ySmpuaTduWE1zQzhENFFQektOT0RsN05JOUsyU2lsRC1Tck9oOWZIMGFvTTlMVmdXLWxPMlRBNmwtcjE5a3dDU3RLOW5NX1ByX2EyTFp6T3dzd1VPZ2F3RmIwTUMyc05PRHM0ajRtR2NybVF2NUZ2aTdwbg?oc=5) <sub>搜狐网</sub>
- 📰 2026-09-30 [【视频】800V平台+华为乾崑ADS 5赋能24.98万起猛士X700开启预售](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBjR1pjWVZHamw4SU5tSWxwdTdYbjhGZ3VuVXZTZEVFcE5JUUFlUmVxZHN1dWpxdUdGSTR5a1dLNXVfNmx2c0hKSTgtbU1IdjRtejFpUFl0STVKNnM?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-30 [30.49万起，华为乾崑+三把锁，2027款纵横G700上市](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5CM3hVR2xQYnJobWVhaWo0N1RZa3JkWkU3M0tDRVJqOU56MmpSa2V3OVVkSVk4VWp6dEctMTVIc3FHSXJxQUpfSTFqb0k3dExFV3liTWhtY3pHTWs?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-30 [新款智界R7焕新上市，华为乾崑智驾加持，23.98万起](https://news.google.com/rss/articles/CBMiW0FVX3lxTE8tdU5ra0R6ZEZ1aWFncld4ZldsejNPcDBFcGNvaVUtYXNLM0NySXBLREo1VHJUTU9PUFZZanlQam92cFZ3TU0tTktkWW80SDNBZFV1bzItOTFEVWc?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Baidu Apollo</b> (41)</summary>

- 📰 2026-09-30 [The robotaxi reality check](https://news.google.com/rss/articles/CBMiekFVX3lxTE9IYjVzLVNLczdEdEloREY1akdEYXRFUDVCempsMmNSck51QjJwcnlPVHU1R0hkYUF3QlhuZzJzbmRCdVlCYnNSTVJlMC1iNmkwU0dOMEdrNEJFLUpXTTdPNEF6cFF1dVpIS21WMGplS0RYNUxoRVVoVnl3?oc=5) <sub>Interesting Engineering</sub>
- 📰 2026-09-30 [Lyft Launches App Access in Europe for North American Riders](https://news.google.com/rss/articles/CBMilwFBVV95cUxOWk9icXFBNE95R05zUnFDeklsbURiMERVOW9ES2IyZE9MeVpxeWxBUkFsVmd0YnY1dGtTQk4tenBfYUVIdng3cklJZGxOMTJnekJldUllNDlHbFhUd19vUmdkS3Q0ak1pdGhjZFFtTmc4WEl5ajl3TjJoLWhadmZORDc1ZEt2Nm81UFNnTEljdkstb2dwRHJr?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-09-30 [Could this driverless car cut Australia’s road toll?](https://news.google.com/rss/articles/CBMi-AFBVV95cUxQSVc2NVVObE5qbmxRUTRqX1ZVX2dtTTBZMUEydnZuSF92U19KXzJ4blhKTVoxaW1rR0lyTUJEQ0Y0SHNORjVRZ2Fsbm9ZcnM5blNpZndWalUtWXYzaTMxSE50cktuY2tQUEc0T3FmeDFFTXVkNl9XQmZsdG95RmhQRHpKYS0waVVBVS1ZcHNpTXE1eWluVV8zYloxYWVRSUJFTXdYMkdZanpLeE5jdHp2cG1vNGw3MW1tZWcwS1NsWkxGWk1ZUkJjMjhhb3E1VEswLV80dUlEXzNOUmk4SjdiTHBabTl5cUNITE5reWVheDM5dnNjQWNWdg?oc=5) <sub>The Courier Mail</sub>
- 📰 2026-09-30 [d88尊龙就ag高考查分系统崩溃，家长翻墙进教育局讨说法被拘](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE43aWI0Um01dWYxdVAzT3Y5T0JhX3ZYaUxPLUN4eGNjTmVrTXpUQkJLV2V5QjViU3VVOTgxek15dEhHV2YySUFnMEh6Q0o4VVNhMGljN1hDZnZHc0FURHF3R0JDdDhFc1E?oc=5) <sub>Pchome电脑之家</sub>
- 📰 2026-09-30 [91y捕鱼大厅·“老字号新顶流”网络主题宣传活动今日上线 22家北京老字号集结焕新](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1XeTVDLWw4Wi1tbU1lN2otVXVHNG90TnRoWTdsR0E5czF5Q3A4M09NdkZzNlEzYjBfeGxTSHRuYlJLOTlMZmpKbmk4cE5KYVQ3QzZNbjhJUTd5QkNqdU1j?oc=5) <sub>Pchome电脑之家</sub>

</details>

<details><summary><b>Pony.ai</b> (88)</summary>

- 📰 2026-10-01 [小马智行：董事兼高管Jun Peng拟出售300万份ADS，市值约1962万美元](https://news.google.com/rss/articles/CBMiZkFVX3lxTFBkVk1SNnlSS0ZGSTh2QnVLOW9waHBKQ0twTklMZXBEU3g2YUJtZUtaQklHZWF5TXpRaF9va051MHVOUU9SYnFqRlBJMFRJcVk0LXdxVWlENEdIMXpSYVRIa0JWeHpPQQ?oc=5) <sub>东方财富</sub>
- 📰 2026-10-01 [Bernstein：中国自动驾驶的三重优势--规模、成本与采用率如何重塑全球格局](https://news.google.com/rss/articles/CBMif0FVX3lxTFB1SDVSLXhqNm1zekpaN3hEWHIycmc2N2p6ZWY3Y3B2MHhzaERNQi1oMjdYOXpTMTd1T1NIbVNkRF9UeXEtZDdhSUlEQlVjR05KQzI4ZG9zOEZSOUpOSGU0anc2eElVMEt5dXhhR2xEMHBTS1JVRXFKUHNYV0syOXc?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-30 [美股AI硬件股普涨，BE上涨超11%，SpaceX涨2.59%；贝恩报告：数据中心投资需6万亿美元AI年收入支撑，缺口高达4.2万亿；CPU交货周期延长至25-30周——《投资早参》](https://news.google.com/rss/articles/CBMiZkFVX3lxTE4xckFKNkY4ZjJTMTFvZ093UXlUYV9aaFBXN096Ml8tbzB5Y3N4STFMNnN4RkhUNnBTZGdiVFVpRVZqXzVyMmppWEtKLWVLR2tOVnVocVdOajJpcXpOTlJNbXB3MjRaZw?oc=5) <sub>mrjjxw.com</sub>
- 📰 2026-09-30 [Pony.ai and Verne begin fully driverless robotaxi passenger trials in Zagreb](https://news.google.com/rss/articles/CBMizgFBVV95cUxPZGprUUV6a2tVbnB0UDl0b2Rzbk9oWFRBeG1xWk96ZnlUQXpmU0tRYXJrSm01MWRYb21MX3Btd1RsNjNfaEdYTmFRVl9UejllbFc3LVlRSGRDMFNuUHdSRjV2Q2Y5MjFsZVVwd3oyS293QXJoNXRXdTZVMUwtbmQxVUxXblNvdVZXYVkwZU5FVWR1TDctZEpQZ2cxOU5sZEs1d1B4emxIVEhsWjlLRnpyd0R3SE5WTWRXVjFIQW5wMERpdzMySGZOVUw2MmtuUQ?oc=5) <sub>Robotics & Automation News</sub>
- 📰 2026-09-30 ["SoundHound AI Jumps 5% on India Product Launch; BigBear.ai Rises 3%, Pony AI Stays Flat](https://news.google.com/rss/articles/CBMixgFBVV95cUxNWEFmZ2htZU55ZXVNMWVXUldPeXZQdFVzbDgwVGlNWVlOMmwweUVfU3dzbHBoMmxaNGdCcXI0U194NHR5RjZ2NXo4NU0yRFctR2Q3by1yVmtRejZMVF9pSTlXek50aTlHNEhwVkhQdTNNX2NhRUVzWWVZdmRsV2tYaHJ5RWFlUHRyTWdxcm51U3BIcHJ4bWR6V0U3SDdKVWUzQjFFNEZ0eEk1XzFEUVdlTGNzSDdwVS1OUG0tZmNGNHZ0VmVUZFE?oc=5) <sub>24/7 Wall St.</sub>

</details>

<details><summary><b>WeRide</b> (77)</summary>

- 📰 2026-09-30 [Uber targets Madrid for its first driverless taxi rollout](https://news.google.com/rss/articles/CBMilgFBVV95cUxNVXZMcXk2RWpycm1YX21ydXdrU2JDakxZZnAwaEFkdnl6c3N4Q2dJVlEtNFFKTUU4ZFRZV3BTWEh5LU5jaE9iUHU0Z0U5Nk9pQWFuWlNqTmhEYjVaR25KY2kwYkxSQXVlZTc3RXhJTGNjd1Iya29EbUFtbjhQUjEzWkhCOWRONEVxT0VqdlQzdVZQUXRSZ1E?oc=5) <sub>RUSSPAIN.com</sub>
- 📰 2026-09-30 [L4级同源算法+华为电驱！埃安i60 ​](https://news.google.com/rss/articles/CBMiggFBVV95cUxQb2t1NWNVYks5RlgtWm1nTDVyOXdjVzRzNjNBaGdVdDdOT2RIa0pmSjFwalNWbmFOalFWdTZFRjdUaUhwb1pMU1drVE4tU2lUZzcwYXU0M2I5MFY5eWt2WDlfcExadW4teS1IS1Itdk94VHlXQldoM0hwLTM5UG9qQnZn?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-30 [9月30日港股软件服务行业沽空数据盘点，腾讯控股、网易、MINIMAX-W沽空金额位居行业前三-证券之星](https://news.google.com/rss/articles/CBMiXkFVX3lxTE55N2xwMmFZNnBlRXN6elV4SEtGc3NtczRzWm9Lb3lCV2VUMlVSTXM3eHpJZzFoMU0xaWs1Z0p1Y0ZXVWtWTHo3WHhMSUt2MDFvTGVaOFBQSFJGVjBVSmc?oc=5) <sub>证券之星</sub>
- 📰 2026-09-30 [芯片、光通信，集体大涨！原油期货，跌破90美元](https://news.google.com/rss/articles/CBMiXEFVX3lxTE9IeE9EbG1LNEJWX3k2SUFkQkpRb0tIRDdqOGRCbUNFZlFBZ3JMQXBGcV9TNUl6bVNFZDltZG1PdlQ1bXI2UWFZei1WdEVOTHo1NFdVdlZGR1J0TDA2?oc=5) <sub>证券时报网</sub>
- 📰 2026-09-30 [广汽集团(02238)股票股价_股价行情_讨论_资讯_财报_数据报告](https://news.google.com/rss/articles/CBMiP0FVX3lxTE5YYkNDNWhyYnpZRVBFNl9vd2dLUC1BbXZhMlRDREF5UEFXRmRhaURfTFgyMGZqUnc3NUJlY3lhcw?oc=5) <sub>雪球</sub>

</details>

<details><summary><b>Horizon Robotics</b> (109)</summary>

- 💻 2026-09-29 [HorizonRobotics/Ego4WAM](https://github.com/HorizonRobotics/Ego4WAM) <sub>GitHub</sub>
- 💻 2026-09-24 [HorizonRobotics/CogWAM](https://github.com/HorizonRobotics/CogWAM) <sub>GitHub</sub>
- 📰 2026-09-30 [【视频】15万级激光性价比之王！到店体验全新深蓝S05](https://news.google.com/rss/articles/CBMia0FVX3lxTE1fb1hKclJtbmtBS3ZIOTIyenY5Q0VfN09tcmxiYmg0RWdxcC1YQW43TUJfUUFORnJrYm5heTFsLUI3Q1ZhZk90UVBqQ2YwVG1hY3BfZFVYVjhCdVdWTUdWVnMxamVCVm9nTUFN?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-30 [Horizon Robotics CEO Yu Kai: Win EVs and You Win Robotics, With Mind-Off Driving by 2035](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBBQW90cWE1WXkxTXFDS3p0dFJ2eWdrMkh3bzdKaE5UQ3ctLWExR1B1ZmJudmhNamtDUnF6NkgwSmRxbmt4MDlYQ2hKeC1YTkwtQnh2Mi1Vc0hRUDA?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-09-30 [QNX, neueHCT smart camera selected by German automaker for China](https://news.google.com/rss/articles/CBMifkFVX3lxTFBEU2RJSDU5MkVuTGFlSmk5U0xrMzgtVXdnVE02MmZjWnlMMW52bTctdGx5ZmYzdWoyeHRhMmljRGN4ZVJOcGZpc01ST2E1VUx5NFhFbVBacVlFMzcwQUlna0c0aTBNTkJGYTBodDZhVnZPazBzMGlyazVudlpvdw?oc=5) <sub>Just Auto</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (21)</summary>

- 📰 2026-09-30 [赛力斯代工，豆包上车，这台跨界SUV 在巴黎亮灯了\|赛豆科技\|赛力斯\|元戎启行\|me7\|aiva\|豆包大模型_新浪新闻](https://news.google.com/rss/articles/CBMiY0FVX3lxTE5UYlN4M1d3aFdYN1lZRGpLTTZpVmlBTzV1U3hLZ0s0emlPOTBXRUdJbHBVb1E1bld6ZG5KVVRzT2l0T19EbWNNdUx2RkdrSWtvcHB3b2VhTmF6OWZKWTBtRmFvSQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-29 [奔驰长轴距GLE上市：国产大五座豪华SUV值不值](https://news.google.com/rss/articles/CBMiXkFVX3lxTE9nLUUzRnVPRUNnUVNHTUtrYThkY29wOW05NXREWDZQY3NtT2EwMEtCclFxbFZ5S1ZGZTQ4RnEzTUw5X2dRaWMwbmR3eXBiVVdjcW1qbU9vV3BMM2VyalE?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-29 [AIVA ME7巴黎完成全球首秀，纯电版快充15分钟即可补能至80%](https://news.google.com/rss/articles/CBMiW0FVX3lxTE03REhqQXhsSEhKZ1VIdDFkWXM5d3pPZjMwSGw2OWJFUkdhbXk4YWNTODhDT2JGQXU3bkpMNF9TakpjLWJVNWE4aXRpZXZGcHZxTzNwYTVMOXJSTlU?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-28 [Momenta与神龙科技签署全球战略合作协议](https://news.google.com/rss/articles/CBMiT0FVX3lxTE9XREQ4ZEJaWjc5UmJMQVVTYVctMS1wWUNBVUk1Mk9TWUFiZWtIM3l0ZEpxY2c2dW1LRm5CVkpNLTlqdDBzeXlNZ2ZfdjA5V28?oc=5) <sub>citnews.com.cn</sub>
- 📰 2026-09-28 [云鼎4008登录网站AI推理平台发布，本地化部署赋能体育产业智能化升级](https://news.google.com/rss/articles/CBMiSkFVX3lxTE1xaXFmUXlZOVA1Q2NmdnQxMlBOQ0RGNGdreDNSbEFhbllZVHRZODQ2MTNPekxNWi1lTjRJSU1LQ0VYSGxzczdPSU5B?oc=5) <sub>体坛</sub>

</details>

<details><summary><b>Mobileye</b> (15)</summary>

- 📰 2026-09-30 [Mobileye Global And 2 AI Driving Stocks To Watch](https://news.google.com/rss/articles/CBMiwwFBVV95cUxQSDFHSFBPOGlJM0RvZ0toN1JTdThRbFNLd3dIUmU0YV91Zl9hQTdWcnVxOXM5TUpHa281bEZkbDhXMDZmdWtHcmlTU0lfZl9SNTA5bC1QMmZQTVpKMkdGTmhiZWI0aDg1VnZ1Z1pFdW9WWHM0SzBaYlJMb2ZMNXN4TEdNampfQXlvekx6UEZRVEd4bU1IS0VWTVFRWkcyWE5IamRockRJQWF1b2lxWnBmVmNrS1RIQV9EYVhJSW05SkZodWvSAcgBQVVfeXFMTmRuV0ZhQ19iRGZhek1SUkVCV0VwWERKcWJkdklUV1NPUm9wSXBTN0hrSVRPUWthSTAzbE5PREh0QmhvUGlCSEtzRVcxRWtleUdtS2psMXhsUWNrSGp1VDRzc1F4NjN0dEZIT3pXWFRhYy1Nc3RSd0VBV0c3ZHlZUGFnU2wzZVQ3N0xtR0oxVzczV2VaR3h2U0ozRmVQTDlBOVRmTEtOdFFVS08tRy1WRllMUWFfLXN6ajFLbWx1T1FhWEtrS1IzeXc?oc=5) <sub>simplywall.st</sub>
- 📰 2026-09-29 [Mobileye at Evercore’s 9th Annual ADAS, AV & AI Forum: growth and autonomy](https://news.google.com/rss/articles/CBMiywFBVV95cUxPU2lGZVVxeEFwczgySTQyOFBlNkhoN2ROMU1aaFBsWWlFVF9nZndrN284OEMxUTJ6WGtLb1l5dWlCd25qSHRwdW8ybTZTcTg2ZnZ0eVM1MWhreko0dVYyNVNpSUtRd3MwUkdfU2MzT210ZUxLYzRPU2RjUnFjSGNyZGNBVTd2WURGNThzRnBGYXU2NFNsMGhyMmdhZFZpdl85WTV1SUtmS0dUYVJCcmljNFlNYTR1UUNBTF9fWFhieE52TGJlZHZ2QXltTQ?oc=5) <sub>Investing.com UK</sub>
- 📰 2026-09-29 [Nio Slides 4% as Geely Takes 30% Stake in Nio Power Unit; XPeng Drops 4%, Tesla Slips](https://news.google.com/rss/articles/CBMiwgFBVV95cUxPSDRxdzA0bnhuMHdpT29qUXZ0WnVxcloxMmNOX0V0bHRkY3JOcjk5TFZqSGhJUXBZUmo1MFVsdXV5eHBsWklVekhadzYzR2hZclFfaFF4WV9MQk96aDYzd19hWU90VnJzczEwb3dQcE5rc2YtakE1SjJIc0JieFYxaFNSa1JDWFhlVndYLWJQWlRQWDV4REh5OElvSDFNQnBBenBXYTE4SFc5NmFlNGg3ZlFYU0U1SDVpSWNWZ21yN2Eydw?oc=5) <sub>24/7 Wall St.</sub>
- 📰 2026-09-28 [Can NIO's Geely Alliance Drive Battery-Swapping Adoption?](https://news.google.com/rss/articles/CBMisgFBVV95cUxQLW5zM3paYXpzenJuMTBXbENBWUZ2NHBFQmNYZDFSX1NJUjlFQWNjeXBwdGl3WFhiNEloUGR3UmtyZHJFYU5OeFprS3RMT1kxMkVyWG5qeVJHbzNZMUFPeVpfYmp6Uk8yRUQwOHk5dkdUMkNJNjZNMk5BT3M0ME5DOE1zd3NNMXV3Y1NyTmRIQUtZSzRQYUhqTm9teU45bEU4WGIwVldTWk5hUjJHdXp1Z1dB?oc=5) <sub>TradingView</sub>
- 📰 2026-09-28 [Germany: RMV, Deutsche Bahn and HOLON launch KIRA+ for Level 4 autonomous public transport in Rhine-Main region](https://news.google.com/rss/articles/CBMipAFBVV95cUxQVE41MUVYal9PVDQyMHc3TlpHNXhna1ItOGFrZVp0NjJyaVZzVzU5bkxFSmFrd0dNTl9BM1E4RzJybzY2Ml91SVMwdmJlV3lXdllyLUJBTTZWMEpMN0ZCU1U0QlhpUF9WcDFwV0w2ZmRXcTNDSmxxZ2stMW0xUzdRZXdYVkl6Zy15bFdKNEdXc1d3b1FmMTljQ1pYRVFWYzBnUS1Ucw?oc=5) <sub>Sustainable Bus</sub>

</details>

<details><summary><b>Aurora</b> (38)</summary>

- 📰 2026-09-30 [How Aurora plans to reach 30,000 autonomous trucks by 2030](https://news.google.com/rss/articles/CBMikAFBVV95cUxOelgtT3NIQ0NYOXJPWXNFT21USXJNeFEweElLaHNpYnU2VEdmVU9fMTQ1a0t2OXZZRE1vTUFlNDltTHVnckljTVZDdGdfbEhlOHhBcjZ3UVI5NHRGZ3hiczN4YWljUFRfdTQtdTlIRnhCR3hNcThndzFMVnN3MFFDTmVWcTJTTDEtazNGc1FpS0w?oc=5) <sub>Transportation and Logistics International</sub>
- 📰 2026-09-30 [Did Driverless Truck Expansion Just Shift Aurora's (AUR) Investment Narrative?](https://news.google.com/rss/articles/CBMi0AFBVV95cUxNNlIyeW5hb01mWW5LaTNZQ2F1NUlJMUJqNkU1V1RraVRoSFVwWFNSd1lRdzNMOEVJRS14dXdqQmlubW10MEJrVmZJOTNxNXhLZ3NVWVFYaHhhQzBSd2dDRW1tNjNwUGNOb29NY3hocVF0R3dRYkFuMmxJUHk0N1FFSzF5cUY1ak9USnVFcU4xUjlNOENUYVFWOXpjcWx5VDJDY0VZVll0cGFnR0pOUnpTdHVUYUEzWkZIazR2LVZfNXlNSGVLZXRrYnhzZzNSM2hv0gHWAUFVX3lxTE03R0tsUmluLXZkZUtDekFGVXlkTEdRZ3J4RTg3S0ZkelJDTG5fWVhqajJ1YWtCXzRTOTQxVHhVWEVuZlU1WVExeE5EaldVQTVOQzVQZkRFY0RKLURqbVhrX3FXdF8waTRZY2R2LUhjeU91NEp3ZUFUZEx5UDdLOUQ2TnVfYjU3OEEwME1ZMFg2Szg5a1hhMUIyZzdJMkFvVnVGOHlPTDAwTUdtdzJqQm56R1hQX2tHLVg5Z1VkcUxKck1XU1hGNDQzck5MZEM5NEVVZWYtVFE?oc=5) <sub>simplywall.st</sub>
- 📰 2026-09-30 [Aurora Innovation: The Future of Autonomous Trucking](https://news.google.com/rss/articles/CBMijgFBVV95cUxOYnBpZWZmQkVwb3Q4aU9HVlhrYnMxTGI2Y3g1U190MEFRTlhGU1FrSXJoaEswQi1JNkVWbGQtYlN3YWkzQnd2YkFGNFhWVktIQ3RrOU9MR2ZFWHJjbUZ2ZDgzR1JQWGVxLUxYLWFzSFU1dU1HZks3SFEweGdhMjFhZVgxeTEydC1WMGZyaExn?oc=5) <sub>Intellectia AI</sub>
- 📰 2026-09-29 [Aurora Innovation Targets $5B Revenue as Driverless Truck Fleet Scales](https://news.google.com/rss/articles/CBMiogFBVV95cUxPN25IeTJfcUpqSTQ2RzFHWE0yd09HUUhoZ3FXTlBweWJhSlF6QjN5Y19rR1dWbmZCdVpKRE5aellXQjU1VndhMjNyN3pvbGl2aXJiRUo1cTdPUTViUTI1Tjd2Q0tvZFFvOVdUNzhQUEJMeGUyMG1lb1VRQWRUdVlXQXNNRHFnUm1BMmo1MEd4QXBRYWs3R21CbFhxY0dDM0FDLUE?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-09-29 [Aurora at Evercore forum: driverless trucking moves toward scale By Investing.com](https://news.google.com/rss/articles/CBMiwgFBVV95cUxOMDB0Q0lrcmY2Z0ItWUtPWUpXUldCMnZJOWI0bW9ZMUJ6STNKejZFYUVlSVgzMUs0OGo0cEpvdnIyVlNXekh4RVVVRHF3aVIzOEUxWGM2X0E1ZW1jb28zQVV0X1YwdkwwSW4tVm9Ca1RxbUFtOFJJRG1MSXFWLU9mWkZweVlqNDJaTkNrdVN3cHNmdTBkZlJSanBSd2tHcHI4SVVKRnhRWnBOQjFMN3RTc0FCb1JycDlGc1paVzVmaE9kZw?oc=5) <sub>Investing.com UK</sub>

</details>

<details><summary><b>Zoox</b> (68)</summary>

- 📰 2026-09-30 [Minneapolis council advances proposal to mandate human drivers in robotaxis](https://news.google.com/rss/articles/CBMiuAFBVV95cUxOVklnZnJWWmxNa1kyLWIyUXMwb1lIVks4YnRVUjZsYzlwQndqTjM2eFdQLUQ1X2g4M1oxZWVGNzJFNnNrOUVoNGVGbEI0ZmVsLUdWMlFac052djN6UHRqeGkxQ3hqVk9NUWFweExpUnJGaHlkNTMzWnkxX1owemZLRk1HOG40VWhLUWtqdDNfMlhvQkZYQ2hZMG1MMHV3elFBNUYxbThQRlVvYm00NHpCTV9udHo4aW5F?oc=5) <sub>Minnesota Reformer</sub>
- 📰 2026-09-30 [Amazon’s Zoox robotaxis to test winter driving conditions in Denver](https://news.google.com/rss/articles/CBMirAFBVV95cUxPcVVCcmpzbWJhaWlzcjZhSVVidXU4bzN6cE1oRHZGVlFXeHl4ZzYtUGlmWDJuWjFHLXZVSFFjRmdWYURjREROX3Yxcnd6ZkZ6UkV1Rml5UGZGLXdsRU11WmpqekFERlFQYXZTS2lpaFJFZGE5dHc1ZzVEaEFyQXR1ajRZSVE0ejhDdWVidWV3bTRFdkhvVlRwSGkwWnJtR1ZQMTZKTFdxR0V1SGFj?oc=5) <sub>Denver Gazette</sub>
- 📰 2026-09-30 [Zoox robotaxis to test winter driving conditions in Denver](https://news.google.com/rss/articles/CBMi1gFBVV95cUxQZExPUkhfbURsb3VVazdzd0Izc2MzRTgyVURIRDFlMElQY1hHcm1PUGQwUVozM09GY2U1aDNEa0lRdE1MV1VGUkkxVlVIclZ2RDAxZ1FmWUl5QjBzczFhcWVYbXlGX3FpVHRrMnZVVW1MNEFKVlhZMUJVTDd5cDhRTUpJeE5WVU5HbGVDQ3QzR29OTUhSeEhGQWZQMXdfNmQ0aTl3WWZzMEN0amRLMWIyM3gzR09VQUZuRWNjVXQzZTdleEZEdWJldW8wSXVCSnpER1BST3Rn?oc=5) <sub>9News</sub>
- 📰 2026-09-30 [Westminster ends free EV charging at city-owned stations](https://news.google.com/rss/articles/CBMiogFBVV95cUxQS0tGcmRBNjhVMFZlaTdfc00tenQ5aDFSRm96Wk1hbFNsNm5DczZReDM3VElVSzl3V0REeFRHaU5kTHA2VWR1VTlrUVRySW1iZl9OUnBpeFR3T0hNSS12VHhmaGVXajMtNFlMMDRiM3ZRVGZ6ajRpMEN6M3hROU10LU9HN20yZlpLcWhBZnJKNEZiS0VIQTVVWTFYSnpNX3d2NkE?oc=5) <sub>Denver Gazette</sub>
- 📰 2026-09-30 [Zoox – a new fleet of self-driving cars – testing in Denver](https://news.google.com/rss/articles/CBMizAFBVV95cUxNcDM2MW1nQlgzNGtJUHF6c1BxRktGTG5FS0c5cWhTRjEwYk40d3IwdEIxTU9ySWhsMF84ZzdfWVU2RkZrdFZhTnpTblhlejdPbWhNbTlrUDJhSjBhR0VGQTVOMy0zb2NyZnN4WGtZTVIxNW5jRkhCY1A1eFQzS2M3a3ktLTNpbnh2SDZMX2c3NEpPeUN4VUdCUjMxRFo4ZndYRVBfdTA0VEw1dGEtNGtuZWl5alpDODAzWm9aLU1jV2NSZ1hkUFp5by1faG4?oc=5) <sub>9News</sub>

</details>

<details><summary><b>Motional</b> (11)</summary>

- 📰 2026-09-29 [Hyundai Motor Group wraps up HMG Tech Talent Forum in Silicon Valley](https://news.google.com/rss/articles/CBMiV0FVX3lxTE04TjRpT3lvQW1oUWc3Y0NuWXJtMjdPVFIyS05XZThIX19XNG53RVktaENMYlQzX0NoMW1mdG44RUpWZjZwcHBJdklHZHV6cHU3WVllckFiQQ?oc=5) <sub>헤럴드경제</sub>
- 📰 2026-09-29 ["Sharing a Vision for AI, Robotics and Autonomous Driving"...Hyundai Motor Group Holds Tech Forum in Silicon Valley](https://news.google.com/rss/articles/CBMiU0FVX3lxTFAtOTlDdkFCRHYtZHQ2ZFJRN1VtY2VaSEdBbHhTS3FsUndkdGZyTXpfZU1PTnNGMHdyZUVFNkVTelRmMU9Jdl9lLVJwSldUVDYyN2pz?oc=5) <sub>매일경제</sub>
- 📰 2026-09-29 [Hyundai Motor touts physical AI vision, courts global tech talent in U.S. - CHOSUNBIZ](https://news.google.com/rss/articles/CBMiggFBVV95cUxQNWZDY3F6Mk9mMGRIT2lWdnlVZmhib3FBbktkRG56al9PdTZwWUVTUTZ1ZnNvT1ZLTzA5N3NFa3dFZGRSWUNGTTFJX09pVVZRTFM2NVU4WHM3YjMyYjBaM1Z5Z0NmZjV2M0NXdzdIWHZvTzNLclg0OVM1MGNXcGpSb1ln0gGWAUFVX3lxTE9BYlRHQ3hoMEZlNE1CYV9VdXhUYk5jRHQ2N1gwZUdnUnA3elhNRm9ZRUdVSjAwZkVKLWt5WTRobkxMdUVNNXVISjhkU2ZjQ3AyU0RfUG5ZRHQ2OXZSYXh3cGJHaVhxT1p2djU4cnU4NFg5TXBKaUxTWThYNmN1X3NjLTFBSTB3WGlRM2pPVFNfSGNFaHRyUQ?oc=5) <sub>Chosunbiz</sub>
- 📰 2026-09-29 [Hyundai Motor Group Completes Tech Talent Forum for Global Top-Tier Technical Talent](https://news.google.com/rss/articles/CBMigwFBVV95cUxNYWttY2laenc2bk0tT21JVVViMk9SN1RZSWNuMkdrSWUzSlB3ZVM5UjZtVDlBUlM0VFZMd0JHdVA1LVhqUXBXcU1vczF3eTVibDg5X0F3eHBpaV9mRHBRZjlnRzh5ZkowMTRpZ2pDZmhHZW1jUzJSZndDV3BUbFBFdXRQZw?oc=5) <sub>starnewskorea.com</sub>
- 📰 2026-09-29 [Hyundai Motor touts physical AI vision at HMG Tech Talent Forum in US - CHOSUNBIZ](https://news.google.com/rss/articles/CBMiggFBVV95cUxQNWZDY3F6Mk9mMGRIT2lWdnlVZmhib3FBbktkRG56al9PdTZwWUVTUTZ1ZnNvT1ZLTzA5N3NFa3dFZGRSWUNGTTFJX09pVVZRTFM2NVU4WHM3YjMyYjBaM1Z5Z0NmZjV2M0NXdzdIWHZvTzNLclg0OVM1MGNXcGpSb1ln0gGWAUFVX3lxTE9BYlRHQ3hoMEZlNE1CYV9VdXhUYk5jRHQ2N1gwZUdnUnA3elhNRm9ZRUdVSjAwZkVKLWt5WTRobkxMdUVNNXVISjhkU2ZjQ3AyU0RfUG5ZRHQ2OXZSYXh3cGJHaVhxT1p2djU4cnU4NFg5TXBKaUxTWThYNmN1X3NjLTFBSTB3WGlRM2pPVFNfSGNFaHRyUQ?oc=5) <sub>Chosunbiz</sub>

</details>

<details><summary><b>comma.ai</b> (44)</summary>

- 📰 2026-09-30 [The $999 Driving Gadget That Just Landed In Federal Crosshairs](https://news.google.com/rss/articles/CBMicEFVX3lxTE5kRFFmYXdUcmRRZ2wtNzF4QlRqQ0o1UmVscVhPWFlsVVE3S1dRVWdtLWFsOFJYeUlHY3phaWZYejBnWjFvVmxTcEJNRVBaQUJscU1VODZvRmxrREVYRDUyZlNJdTNsMUN4MmkwYXY1TWs?oc=5) <sub>HotCars</sub>
- 📰 2026-09-30 [Federal Probe Opens Into Aftermarket Self-Driving Hardware After Three Deaths](https://news.google.com/rss/articles/CBMiqgFBVV95cUxObDZzR1Z3QnZLaDR0bTRldUFvc0ZESTBoUHIyZE1PSmJHWFR4MmdrTi0zWkRFT250VG5WbTNuTWd4dzV6R1FIYzV2NzI2NGlfMzkwdHBTZFdIYkxpNG9pWldBQjdxTF9OOTFiZ1M2RlVfaFlkNThCRk41c21ZcXRsalFfOXpqTXRhYVRhaVREaFRRamMzcE41TGNMVTA5azFDWWxCalpHNkdCUQ?oc=5) <sub>Gadget Review</sub>
- 📰 2026-09-30 [A $999 Box Promises Hands-Free Driving. Its Own Code Says ‘THIS IS NOT A PRODUCT.’ Now NHTSA Is Investigating Crashes That Killed Three.](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPNFIyamduTmQxb1dKNlh5Z1hCYUhyemoyU2I2bjFUWjZQSDVFSDFWOGxlM1hnQms4Q1lpalg0bXlCTEZTdVJ3eGtNTjlLamY2eW9LX09IejF6SkJxSmZ2QjRkU1pUczlRY2g3cUZIN3hvSUc3a3pUWHVKVk40MlY3Wk5SX3dnOHBl?oc=5) <sub>Yahoo</sub>
- 📰 2026-09-29 [US auto regulator closes airbag defect petition in about 807,000 Honda Odyssey cars](https://news.google.com/rss/articles/CBMigAFBVV95cUxPbllOY01DRVNHZUd5dXR2MXJDc0N1bXdVS2V2V3BzX0NqdmxORnl1cm9PU25FSU9YX2xyajJVNEVwdXFjZFM4eHQzX1ZmeHVTR3lyTVpnNlRna0dXMThiR1A5TGdseEtJTDUyQzVqN25nMUV3MVdYWVExMHlQZTFPWQ?oc=5) <sub>AOL.com</sub>
- 📰 2026-09-29 [NHTSA investigating deaths/injuries linked to comma.ai driving system](https://news.google.com/rss/articles/CBMitwFBVV95cUxQMUxNaU15eUlyamdpeUtadXJFQnlOMTJYOHJmdHRJYnpJMWdJb3hJRlRISlNGZVA3dkhSNnNVOG53N3dMQUtOVmFCNUpqRWhaXzA1TG5HM2I0aEV2bG42VkdoRXRyYUI3SkpnM3ZCS2JLUkMtemRJNEVONkh3cExkakF1LVNEVjNZMjFpVndjaExSaHhiME45NGZEbWFCUi1YQ2M4Q2pLOGFISWQyeGhVV1Z3QW0yM28?oc=5) <sub>repairerdrivennews.com</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
