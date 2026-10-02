# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-10-02 · 1,239 papers tracked · 36 curated.

**Selection rule.** A paper is listed only if it (1) is primarily about autonomous driving,
(2) has public code, and (3) shows at least one strong signal: accepted at a top venue
(CVPR / ICCV / ECCV / NeurIPS / ICLR / ICML / CoRL / RSS / TPAMI, or ICRA / IROS / AAAI / RA-L),
≥200 GitHub stars, ≥3 citations / month, or a well-known lab with traction. Papers are then ranked by a
composite score (venue, stars, citation velocity, LLM rubric for novelty / rigor / impact, SOTA claims)
with a per-topic cap. See [`scripts/rank.py`](scripts/rank.py).

📅 [Daily digests](daily/) · 🗓️ [Weekly digests](weekly/) · 📦 [Raw data](data/)

## Contents

- [VLA / VLM for Driving](#vla--vlm-for-driving) (7)
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
| [FreeOcc: Training-Free Embodied Open-Vocabulary Occupancy Prediction](https://arxiv.org/abs/2604.28115)<br><sub>Zeyu Jiang, Changqing Zhou, Xingxing Zuo et al.</sub> | RSS<br>2026-04<br>📑 5 | [⭐ 139](https://github.com/the-masses/FreeOcc) | Existing learning-based occupancy prediction methods rely on large-scale 3D annotations and generalize poorly across environments |
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

<details><summary><b>Waymo</b> (147)</summary>

- 📝 2026-09-24 [Our Vision for London: How Waymo can Support a Safer, Connected UK Capital](https://waymo.com/blog/2026/09/visionforlondon) <sub>official blog</sub>
- 📝 2026-09-22 [Introducing transit rewards](https://waymo.com/blog/2026/09/transit-rewards) <sub>official blog</sub>
- 📰 2026-10-02 [How self-driving cars became reality – and what comes next](https://news.google.com/rss/articles/CBMimwFBVV95cUxPeVFPSVJTMTktczZuUEdueV9OZlRLWkJHbm9ORENRM0RoRFlEZkZ4bFhtOHpRbnkxa29SY2RkXzFlVVJFSHpROFBpNHpyODVrSmJ1M1NuNDFXV3hYU2VlSkk0Y0d2NXhSWDd3cnpQbTc1a3phZTE0aE42bEJLZ2RTOEUxY3JwLUFPMkNIcU15d0lnMmJfWnVTYmktWQ?oc=5) <sub>Technology Org</sub>
- 📰 2026-10-02 [Robotaxi operators will face fines for blocking first responders](https://news.google.com/rss/articles/CBMioAFBVV95cUxQTkxIUGliT0tPdU5KZzJoQm1JUDZXMVA0RGo5OHV5RV9pSm9lYzVyRUp0MV9WaFN4ZzJvdlRpMktmeHdOWDlYNG5xQk51cExkZTNtZFBKTG1yNG9nWG1aMzhCcEF2UEJXcjhIRHMtMXJCZ2lVbnVEaWRoM01BWjFtWmhCa1ZxRE5lX0hhSkJVSG5obVV1d05tamVnOFgtdzgt?oc=5) <sub>TechCrunch</sub>
- 📰 2026-10-02 [DATA: Robotaxis in Phoenix have the lowest crash rate among major US cities](https://news.google.com/rss/articles/CBMisgFBVV95cUxNTmlhZlhieUFJM2IxMFhGRFMxZFJXWlVndXRULTg1LTltSVd5Y1F6LWJXY1BrODNhbG1qUXk4cUc4XzBVY0Exal8xRkRwU2ZpclotVGNmUmNTQjN2cHdmT2FlelhWb0Jma1dXX2Jhd0cxZXowOEVpcjBqdmNWeHd2RC1GVkNYTGNuUHN2VVQyYUZJdURoM1gxdTdZczFZcUZ5N0lmQnRxU0pOb1l1VUFnZ01B?oc=5) <sub>ABC15 Arizona</sub>

</details>

<details><summary><b>Tesla</b> (226)</summary>

- 📰 2026-10-02 [Belgian test finds Tesla FSD sped through 20 mph zones, tried illegal cyclist passes](https://news.google.com/rss/articles/CBMioAFBVV95cUxNTVZBYlQtek9jRlQ2c2ROU1JHdlZMTlgxSmZVbVl0a0wyY0s0c1FCcUxEYm5WeE5JeDBfMlRNVDAwQ3Y5U3hUUUhEYUZiSGtVUDNieDB1ZXVCZ0JvVWZWWndtdTVZdG5kS0k2UVh4SC1SbmxuZ1VJbFBzaGlzTVJuaXdtUXZmRWJuTzVPbTdhTzB4SFgxLTNiSWx5YjdlZ2Vt?oc=5) <sub>Yahoo Autos</sub>
- 📰 2026-10-02 [Tesla Cybercab Fleet Hits 158 in Texas: Your Questions Answered](https://news.google.com/rss/articles/CBMingFBVV95cUxQcU02TkNDVnI2N3hWNHAtTlVBcjNUVWRBSmRScDhUaTdqVjdZRW95Xy0tTk9XWm5vWFBxNW42clY4Tk43MzdoRFhqZkhMbzBqOUxDcFRFYW1kZ1NhRUpsb0tUTkx2NnNnM2RTRmNhcDlSalpmVzJxd0swOUIwV1piTEdJX2VHc2xYWmFJd0ljcmJDemVZMlZzanloWEJXdw?oc=5) <sub>BASENOR</sub>
- 📰 2026-10-02 [Robotaxi operators will face fines for blocking first responders](https://news.google.com/rss/articles/CBMioAFBVV95cUxQTkxIUGliT0tPdU5KZzJoQm1JUDZXMVA0RGo5OHV5RV9pSm9lYzVyRUp0MV9WaFN4ZzJvdlRpMktmeHdOWDlYNG5xQk51cExkZTNtZFBKTG1yNG9nWG1aMzhCcEF2UEJXcjhIRHMtMXJCZ2lVbnVEaWRoM01BWjFtWmhCa1ZxRE5lX0hhSkJVSG5obVV1d05tamVnOFgtdzgt?oc=5) <sub>TechCrunch</sub>
- 📰 2026-10-02 [特斯拉FSD不靠谱，森林湖差点被罚700](https://news.google.com/rss/articles/CBMigAFBVV95cUxOa1c3dkpXQjdrby1qTWdaTFlNWFNEN0VfbkdoRmhGNWNrYjdhVGp3VHBhaVA1bzBHQVhGa3h2a2puWkNpOXZ2akRvelpUSFk1SjAxTmpLV1hjekhLRldzdnQ0YWRoZ1NqODJNN091ellaWTVBb2lkZXhfbTVLT0Qzcw?oc=5) <sub>k.sina.com.cn</sub>
- 📰 2026-10-02 [特斯拉FSD遇减速带bug，拒绝倒车14秒](https://news.google.com/rss/articles/CBMigAFBVV95cUxQc25VLUluY3E3V21Id1ptWDZFdnByTC1kLWV3b0o3NjZkbEFCZUdCZVZNV0xmaWtua05rOGdJc0dsSk5zOFQ0bUdJZFIxeGFXeWdBYTBWanhVbXBlbWphSXUyeTRtMXhvalRGMGRTMm5XZExyalJxTVcwYkRoaXNmNA?oc=5) <sub>k.sina.com.cn</sub>

</details>

<details><summary><b>NVIDIA</b> (149)</summary>

- 💻 2026-09-18 [NVIDIA/swe-serve — SWE-Serve: an agentic benchmark of 53 production inference-engineering tasks derived from merged SGLang pull requests, run with Harbor.](https://github.com/NVIDIA/swe-serve) <sub>GitHub</sub>
- 📰 2026-10-02 [How AI could transform Kazakhstan’s industries: Interview with NVIDIA vice president](https://news.google.com/rss/articles/CBMitwFBVV95cUxNamQzdnV1T0xWOEJSXzIzbXZyRWhaSjNKT2Nza0haSFF0cXJtcDJYUHlPNGFfZEFmR2wzYk9LNWVORXpUMC1WVUQzY3hsaW5COTUtZU14QnpxbFBLaFliS29MeGVIdmFfYTVucThrMkxHUXVhUjJyNWdrM3hCYXQ3OVdTYjFBSG1UZHB2SGJjeXBjZHlDOExESWZ2VUZzbUNIQk5xcHZ4dzJkQTVRNzRQWWljWk5rVkXSAbcBQVVfeXFMTlVodHRXdnZDemR4blVKX0FxN3gzcEhlWjV3LUlJaGQ5TTh5U3FocFNfb01iMEltV2VHdkF4dXhMUGc3Q0RLU2txMTM4aGJjRHJDTlh2Ml8yVngwbnVjYzhrQnVxenQ0UEV1bFJZZFcxTkVESEhGamVKeXhBSUhLVEFMVW9kUlpoTW1UbXRyZEtzLThWVGdrWjF0N2d0cUVRbjZHZW55VVZoeS1kU2Rhdk5lNTFGOVpV?oc=5) <sub>Qazinform</sub>
- 📰 2026-10-02 [Skild AI launches robot model trained from one video](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNbWlTakU2cG5MT0w2RXNGbUVBVnRqcHRKcC1RcWc4TGZNb0ttUHRVSUNuWS1GU0hLOG9KY1otNUlLU3pKTG1tRnc3RDVLZGdCYWFxZTZ3SGhhc2VOQmFvZXdRWmhqSGZhZjV5V1gySG9rZGl5VFZCb1I1aFltRzJkanRpWXBEVjZ4?oc=5) <sub>IT Brief Australia</sub>
- 📰 2026-10-02 [Best AI Stocks to Buy in 2026: 10 Top Picks & How to Invest](https://news.google.com/rss/articles/CBMilwFBVV95cUxQcTN4SWRQbVZpY1lwSnJjN3YxWmY5LU5Qck5ia2psWWRwcWplZ0RGTFo3ZmJrZDZ1S1RQZFF2NUcwOTh0NXA3NlM0a25ieHhPWHprdTBmbWxzY2FtdHRIMlpSY1pzcTU5ZkhfN0wtcF9UeDg4WnZVYTZPSkRtcDNZaUJ1djdPQ1RVRkVQeVFUTnJrMFJ5VXdj?oc=5) <sub>The Motley Fool</sub>
- 📰 2026-10-01 [Thieves stole Nvidia-branded truck filled with sand—but it’s part of $150 million AI theft problem](https://news.google.com/rss/articles/CBMioAFBVV95cUxNMEZPXzdjZUtEbzI1VDdoS3VQWE1KSTQyS1NPUTN4YnBYRk95MzhOZkNvRWd5NE00UHhRTkVfclF2T0hYR1hvNy1ZNU9BcDZ1WUNyY1JSNGlDUkZkdmMyNlJLTThLMEZnS1dxaUlHQ29adFhJTG1xZGQ5VTJIaVIwbzNOY2t2WGZCRDRlSUxKQWd6S0dNLUxEMFB2aldpeFQ1?oc=5) <sub>Fortune</sub>

</details>

<details><summary><b>Wayve</b> (56)</summary>

- 📰 2026-10-01 [Stellantis and Wayve to Demonstrate AI-Powered, Hands-Free Driving at Wave by Vento 2026](https://news.google.com/rss/articles/CBMi2gFBVV95cUxPeDhNTXoyWVJSNVF2MUR2V19laG10Yy1mUFZ1OTFhQ2k5RGdDSUMydF9PblgyOFlGSGgyeDBFZlcwOTllYmVnTm9wMnhycXVtbnJDekJTMC1CTXNobjREazRwZmlXeDZqbW52SXVhenNjRFhsWEkwNUVTV3lsVnJiOS1JRVNGZUR0ejh6WE11OFdhX3lUdHM2b3RfaXNCdC1ndkFmR0thOFd1eGtJTjFMdWMwMGM3cXQxdUtvMmt0SldmV2hRTlpiWUJsalItSEdaMkNZY3FtdzdkQQ?oc=5) <sub>Media Stellantis</sub>
- 📰 2026-10-01 [Stellantis and Wayve to show hands-free Fiat and Maserati](https://news.google.com/rss/articles/CBMimwFBVV95cUxOaDNUY2ZmMDY3VmxlZXJOdnFKcnBIVzFRazZjRmFSemE0eTVCRjNyeEN0VHpsWW1iTnRZWUhRR3RhTnNPU1ZHbzhxZWloTGdUX2NLQzJ2bHBqMjhBWnB0Sy1rT2t5WTRNeDZ2WXNMUE9zcG5Ea3hFaVNITG9RNUtkV1JlXzhJYl9vdjRFSlp0SFZfOUt6MjFzNnYxRQ?oc=5) <sub>Automotive World</sub>
- 📰 2026-10-01 [Tesla postpones Roadster unveiling due to weather](https://news.google.com/rss/articles/CBMikAFBVV95cUxPQjBMeFhnQlpJYVc4NlFGUmZnRkRKQVhrMzUtazNsV1pHQlNtM1lHU0xsWUY3QmgyNll4T3FPUlhwcWJrbmozWlhxZ1dreWJZQnJFTWpseWFTelBPQjBpSktNc2hXdUtidGdGOEJQbzIwYXFmQUNSeWh2dktvNmdjNGZ2TUtZTklnNm1RSmpQakI?oc=5) <sub>electrive.com</sub>
- 📰 2026-09-30 [Portugal, Slovakia and Norway Join Initiative on Autonomous Vehicle Testbeds](https://news.google.com/rss/articles/CBMirgFBVV95cUxQWmtzV0pPLXRnZWF6RDQzaV94VmlDTEVjMi1BOEtBZDZVRDZoeDVzT1dROGRVN3hQcjJneFBKLVZSa2Z3aU1kc1BLQjZhT3B2Z21weUpzaUF6UDJQNms1XzJkUWJwY0d0MklJMTUxUmZ3T2xMRTVyS052eDBObWx2UFRBenJqVGROVF8yODktZDR5Q1dqLXhDX0YwendmV24yOXlfX0hvdjdDR1hJX1E?oc=5) <sub>Future Transport-News</sub>
- 📰 2026-09-30 [Mercedes-Benz Ties Autonomous Driving Deal to Sweeping German Cost Overhaul](https://news.google.com/rss/articles/CBMi1AFBVV95cUxPVTU0SkhqekFmQ1dCcWgxcnk4YWdXTWF5cURITHd3WEZOOXh6b093TFhYUGEybmxudllrelNpSXBya2JBQ3l5UUtNS2RObjY2T29ETHM0TWNvUFQ4allkTHBkS0huX1JnbktKY0xQR0dfVkNCZU1JbkxzNFM0T1BWWUZ1ZmxlaWdYQlpuT3RuZXFrZmlIOFNvb1QyVlJrcEVHUVFHQWlDUkctZDluOWx5N2ZKeDZyZ0lLSExlbjFkVXRkYVE5RGNGbEJjNWlPcU9LQ25iNA?oc=5) <sub>AD HOC NEWS</sub>

</details>

<details><summary><b>Momenta</b> (126)</summary>

- 📰 2026-10-01 [Momenta Global Maps Out A Bigger Robotaxi Fleet](https://news.google.com/rss/articles/CBMiggFBVV95cUxOR0QwRENtY1B6eW1WcHJ3NnVxT1N4Vk91d1oyMHJTYzN3U1FlOHNqb093anluaFRjMVdDWUxpOXVjSUpjMTJJM0ctYkFvT3A5eVVhNFFQdl9KVlYzdl9sMy1aa1JaMTV5N1o1ZjVpSkg4dDBFTmpCU2ZoZGQxOW1xSmF3?oc=5) <sub>finimize.com</sub>
- 📰 2026-10-01 [别克至境L7值得买吗？20万级纯电越级王，3个维度深度解析+FAQ](https://news.google.com/rss/articles/CBMiakFVX3lxTE5FV3FwQ2VYaWVRRWQtUV9fS0J6ckhGVDlfSm5ObmdSR2hiSnZINUFkUmY2VGJHUnktdkh6SldZdC1iY3pZMlRBZU0zM1BzSllYd1VZM2hJV1dGbmRlWnloby05clF4dUluX0E?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-01 [带激光雷达的豪华插混SUV哪款好？全新XT5 PHEV领衔5款智驾车型横评+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFBCZWlwdnZNT2dzeWdPVUl5X1FWMzYtLUdRMjFoazBZNVk5Z1hkYm5LeVRaUXI5NG4yMG00MFE3UkRwazQ4Qk5xa0lqM2IyOHdpZkx2dUVZNnh0OHpNcFZSeGg2VXRkYWlNMGhTYXQ5ZG8xQQ?oc=5) <sub>k.sina.com.cn</sub>
- 📰 2026-09-30 [宁德时代电池+Momenta智驾，艾尼氪V限时9.99万起会火吗？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9nX0JvVFE1a3M1M0Z3R3d5V2E4VXRBYVBGLWVUcUU3OFJ4X0hwT3JCV3R0ZGczNVdiRl9NQXA5d1FIazdsdF9QUnNVQnhTdER4VXRoZ2RGcjQ4OXc?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-30 [神龙科技牵手Momenta：法系Jeep智驾逆袭？3个维度看懂这盘棋+FAQ](https://news.google.com/rss/articles/CBMifkFVX3lxTFBTZUJLOVZtRXNFU19KcXEzYU5zY214eTZvbWpuQ3kwVzdTSlk0UV9aVlpvTEVOU3l3SkxSZEw4cmJzbl92NVFxbFVPSlBtYUdGRVM1eHp6RVlEanpiNE51M2p1ejlOekM5OXdudFdtZmN6NWZscmdOYW5hM3VQQQ?oc=5) <sub>finance.sina.com.cn</sub>

</details>

<details><summary><b>XPeng</b> (180)</summary>

- 📰 2026-10-02 [快充差10分钟，小鹏MONA L03和铂智3X长途谁更省心？](https://news.google.com/rss/articles/CBMia0FVX3lxTE1UUDR0S3RBWHZpY3ZvcFVBR1M1T05Wbk9xdjRBUDgxSnMyOUtUT0tabnJvcUcwakZtTms0TDRTSXdtM1FLMk81SzItdjk1NEhaYVZmUVFhSENic3BSWl83THJ3cm9MdjZqWmkw?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-02 [503马力四驱+6座，小鹏GX对比三款增程SUV，谁更适合你](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBZWFBObGVTbE44Z1dlTTJZT0NKYmxkNWVESE81a1FrRWphS1U3NkNWSW9vd0V3R255YXJrNC1SaDBkQUtMNzVIUzhCM3NDdHVUMXNqb1NsU1ZDMWM?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-01 [XPeng and Tesla Alone in Paris Auto Show’s Self-Driving Rides](https://news.google.com/rss/articles/CBMinAFBVV95cUxPbnNTODJaZFYxeEF4c2ZCZElWLWpaczdaYnRFZzE4X0ZxcE1qa0VxbjlSdUljMUd0ZVpGaW1kZGlCWjJpR3NsS0J5dFBkNTNqTHdMX093bDBSNnhFSG5vajZ4cFp6N2NXYjVYN3pRYm9PejU2V19PbUg2cmt0ekhwRmNSX0lsNExVYVRSZkJHUW9TdmRSdENzWGkwd2c?oc=5) <sub>eletric-vehicles.com</sub>
- 📰 2026-10-01 [XPENG To Launch Its Next-Gen AI Flagship G9L SUV & Showcase Its Physical AI Lineup At The 2026 Paris Motor Show](https://news.google.com/rss/articles/CBMi4AFBVV95cUxQNzZCZkR4a3BXck5BamRJMHRJRUNNRU1Fdk5QU3VhaEdJN3FhQjlVU1U5T1dpbWVkT2VvVkJNZmlFTFF5V3h4dGEyTURyMVV1ODdlVjNsNWpTR0EyenM0RFljd1ktTnRtbE00SDROTzJyd3VDeGlfcUVGYTBIOWRBX3ZQcHFJellVZ0loWmVyRFZmOEZ2eDN4MVZvdU9PUU4wbi1vb0JMX2dqVVJEV2RBcEt0aU9uRzJrZWxPZ0swYlppcFV6NWVrN3gzb3p0WmFpY3NzZktsRHAtMHBmeUcycg?oc=5) <sub>CleanTechnica</sub>
- 📰 2026-10-01 [XPENG Paris Motor Show Lineup: G9L, NGP Rides](https://news.google.com/rss/articles/CBMiZEFVX3lxTE1KQU1IVXNJWnhLWVpJSWxYNHBoTWhmYTJhTnZUR1NXTWZrX0o2X3RXRTA4blhTbmhLUjdQSjA2Z3d5NzdjLUlvbHBSMUVFdTdZWmtBUVlRM3pKdWNjSXg3eW1xbEs?oc=5) <sub>The EV Report</sub>

</details>

<details><summary><b>Li Auto</b> (131)</summary>

- 📰 2026-10-01 [Li Auto delivers fall 6.3% Y/Y to 31,817 in Sept 2026; cumulative deliveries reach 1.83M](https://news.google.com/rss/articles/CBMi4wFBVV95cUxQU01tOFFqNjFPVGpZS0xDN1NMNHlxam1ocnMybFRTYmJtaFR4eURLM3FSM0E4WUU2aE1mYWVsVEg1ZVVfeUg4djBjNTBYakdmajYzYzM0SHZQY1lxSVpRU05DX0U2dlltQW5tVVhTQmE3VDlXVllQUTVUWVEwLXVfdGVKWUxobGVvYWFEOUY5dzdwQXNBbkFFQS0wZFgyNU9TMHMzLXhIbURUdHVhLTRZUXplWXR0M0JxTGVyOEp0YnM4bTI0THE0RUtvUFFkMkJEaC1lUkdNeVVjdTdJb2p6ZzlKUQ?oc=5) <sub>TradingView</sub>
- 📰 2026-10-01 [Li Auto delivers 31,800 vehicles in September, cumulative total tops 1.83 million](https://news.google.com/rss/articles/CBMidkFVX3lxTE9ZQXNFRlg3Mk5DQlRMbHRMMlRNWnFnR2x1UUxkdUNLb2RGZVBELTVGTFFMVktFU1QxaVBySkwtVWszbzdSdmVKZjNQeEl3b2ZPdF85T2FEdXlGS3dGRzFsMmFaNEpvenJla2l3WlZTbG9mUGxJc2c?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-01 [Li Auto September deliveries fall 6.29% to 31,817](https://news.google.com/rss/articles/CBMibkFVX3lxTE9zX2lpLS15ZHVKQ3NHREZoV1NIU1B6Z1RySzBKaE50VmtHTl80cENSN3lVR2tIaGQxMXl2OEVfeUk3QVFyYV93YnNfWXotQzB0Z3ZtbFBfMVhQLUx5N0dRM3FuRURMVFVlVlVhWUNn?oc=5) <sub>CnEVPost</sub>
- 📰 2026-10-01 [The new Li L6 accounts for over 10,000 of Li Auto (LI)'s September deliveries.](https://news.google.com/rss/articles/CBMiqAFBVV95cUxQbE02YlFXMkVNd3k5T29TdGh3UExqNlFHWmVZMXRmVzlHTU16VEpFcU9vMjJHQ0w5M3RHOVFBdmJBcEJ2MFAyeEtxeHYxNjBLTjdQTngxYVZEYUpOU0sxR2xrVTBGbm8zWEJkUWlOeG85ekdlM0NQR25odk01NmQ5di1aYUp1a0E5NTRzY182V1pDbVhmbzkxZF9jUUJZbDZsVWk4VkxCTFA?oc=5) <sub>Stock Titan</sub>
- 📰 2026-10-01 [Li Auto Inc. September 2026 Delivery Update](https://news.google.com/rss/articles/CBMitwFBVV95cUxPX2N6NWNBTTMwbEpacGtqQk1LZXE3dEEyRUIwV1FVRUtKMEZzSG5QWkZheVV6ekU4Ym80N2hQYno1Si1nMzN0dGFERkdRdC05ZmsyTkJyc2dVcnp4TWJrZUgyOGZDRm83bXVzWDZld0ViN096ZXR2YmltMVJBUXlocUxnSmhYQW1sTm9qR09ZeFJFWV83eERHTlZhT2RSOUp5X3VqWWlYYUtTelAtdUJuVFB1dzdaWHPSAbwBQVVfeXFMTW1OdXdNS1lDWXptQ183OTl0NjdldlZrMGtPdFlDRGhWMnp4UHBUdHZUUDRWMW9yNDB3eC04YU9mOVdFTGNramJGNEt3SWZ2SEVHVUJFc0E4VGtyem90Y0ZuYS1iZGhtdUc4emItSmlVT09DNEdwMk9qSDdPYmxTclZza2JXZ3Q5cVVBVXRNNGQtSlpTR3JwWGc2Y3duNWo1NllIYVFabEFYNGdvZlBfUEFGdXNhZHdselE2V0c?oc=5) <sub>The Manila Times</sub>

</details>

<details><summary><b>NIO</b> (138)</summary>

- 📰 2026-10-02 [【视频】蔚来EC6的买家根本不是年轻人这台溜背纯电轿跑SUV在讨好谁？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1MQWEwRng4SWk0eGJkWkhIc2lPaldSRDc4cVlyeTRuZEVkc2VuNkRiRFBVUXdSVzVLeUxVRG92WHZ0UnZzbmRJRUxVN1p2YS02THUyb2RLaFR6eUU?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-01 [周末带娃去郊野，智界RX和蔚来ES8谁更合适？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5PUzBHQmZ6R002Ry00S09SbTlhSVk1TEsxWm91cXNGdGk4ejZOdjdiX1BrbkUtUlYwZ0ZWblBUSHBqOGU0NnBJeFZxMkhGX0ZndnM4MmxyZWpUQ0U?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-01 [2026北京车展，问界M9和蔚来ES9怎么选？](https://news.google.com/rss/articles/CBMibEFVX3lxTE5XdzFncnVJdUpoZm1ULTRYWmdXTzdjUHZGakRicDJWeDVsUkU0S2JWZnE3a1o4UC0zY25RTHducTFXanRLVlhEdURaUGpORE04dFMyQWQ1STV2Z0dnU28yOXJpODFObV9IMU5wOA?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-01 [有无辅助驾驶体验差多少？我们搞了场60万的实测！](https://news.google.com/rss/articles/CBMigAFBVV95cUxQeTJxM1puVjkwS1hsWGtQZmJ2NHdFLUlwbHlpTG4xTFVLM0Q3RXhPQXhQVm8tdVU2Rzh1SDlHakhiOUNrUlh4V0VDRkxPQW9jdTNvU2hlV0E3V1dqcVd1V0lVb0h2TVpIUkU0N1dBaHdlVEZnQXFJXzhmRDdIUlNFWQ?oc=5) <sub>k.sina.com.cn</sub>
- 📰 2026-10-01 [蔚来吉利合作后，小米车主点赞小鹏MONA颜值智驾](https://news.google.com/rss/articles/CBMic0FVX3lxTE5OUDJJazFwTklxUXgtZmlfc2Vub0Z0ek0xb1U3enliVmFIZTNUcUdtVHJRSFM2WG8zRTVHVGlodWc2Wkk1d1M2SmJlaFM2Y3J5RnJGVjRCbVowQzBfOURfRUJUNk9vemxHRGtiYmIwRHdiejQ?oc=5) <sub>k.sina.com.cn</sub>

</details>

<details><summary><b>Huawei</b> (277)</summary>

- 📰 2026-10-02 [Huawei MatePad Air Z Brings HarmonyOS 7 to a Cheaper 12-Inch Tablet, but Swaps OLED for LCD](https://news.google.com/rss/articles/CBMigwFBVV95cUxOUHJzS0ZneVBOdmN0OUcxMVFxU0xOc0lmMXdCUU52SllDOHdEYjBNMGdqRlAxNlRhcHFfQllTaGFyRldBVUJHSlV5eGhUY1FOa0EzaWh6d1lNdjczTlFrczJfTG82SGNDRTd2TmNaZmdZSURBTFF4enlTZG03ckpReTNHMA?oc=5) <sub>Memeburn</sub>
- 📰 2026-10-02 [享界V8的华为乾崑智驾有什么亮点](https://news.google.com/rss/articles/CBMickFVX3lxTE5wZGxkclo0X1EyZnNwS1J2bE5nME5mb1RWZ0lidGdsZkxXTGNnWTJUUWRheUNzeDVWZ3dXazVWbDA3WGRxTnJ1SGY5b2o4ZDFvZDBCS01SOUpvOTE4V1pEeGhhWV9SRkJKeGNSQklSa0pjdw?oc=5) <sub>k.sina.com.cn</sub>
- 📰 2026-10-02 [【视频】全新奥迪A6L 搭载华为乾崑智驾技术，辅助驾驶上车](https://news.google.com/rss/articles/CBMia0FVX3lxTFByOURYTGNSb29IOUJhRFJMck5wakxwYTlBVDZPUVZJZzlYTC1kOTdPdkJudi1kdjFfaW84QUFTcUtJX2FaeXFUdE1aVUlrMnBkYS05R3dTZDNHRjljdGdsQVptbWhxR0dBbHZn?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-02 [30万级大六座价值标尺松动：奕境X9以含华量重定满配门槛](https://news.google.com/rss/articles/CBMia0FVX3lxTFBDT3lBZUFRM1JiU2p1dFloX2p6dXJVdDZoR215eE1zR2FhTHZCUUZBZDFEanl4Q1EtLU5sc1NNRVh0Mkwya3RoSk1hNmF3SzVWS0RPaDAtOXBPOUNVWHVmcXdrNkN0MWFKSWFJ?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-02 [15万预算买新能源SUV选哪款？极狐阿尔法 T7重构智能出行](https://news.google.com/rss/articles/CBMif0FVX3lxTFBWZDVrQUxGWHJ1OU5qNnMtVDRlWlotbWM5UnhmM2cza1NyMnBCSmc4NC15THJfS0p1bTczNkdmOUtmUTBYVnR1MlRna3JLTElKM08zcTd1bTNUcllpVzdPZnlJbkNEX1gzQVFsTmNiNTUxc3N1dmhlTXdmbGhwMjg?oc=5) <sub>k.sina.com.cn</sub>

</details>

<details><summary><b>Baidu Apollo</b> (39)</summary>

- 📰 2026-10-01 [Driverless Taxis Arrive at Chek Lap Kok: Chinese AI Takes the World’s Toughest Driving Test](https://news.google.com/rss/articles/CBMi2AFBVV95cUxQUXhkSmRNTlBSTVQ5ekMxNU40M2N4bmMwMm51aWwzNmxYakFnZjVOWXYteGVmTndYMGtSWEVkejRFaWs5eTZadFY1dGhXdGtHVjhoZEFZN0hCM09neTRIbWZWMFEzS1dFc0oxRTUwZW9hcl8xNndpUWZyUmUtM281Mk8zTWhFZFFNNzduNndZcVJNTDlrOTdyODhsSEs3d1h0S0lYQjBtZTAwSXkzZXJVbnpOWmFMR0NQNVVoT2F6c0czcjF3YURhMUp0Qmx0QTZxNnBCaWxRNDE?oc=5) <sub>巴士的報</sub>
- 📰 2026-10-01 [9.9元起！yabo888app平台官网网址正式上线，凭闪电级响应成为体育迷的终极乐园-体坛网_体坛+](https://news.google.com/rss/articles/CBMiSkFVX3lxTFBJZGxVREpLYllULTNULUZfNE42LXp3ZzZQbmVlOXVpOTF1Vk83VC1nRlpLeXo2UC05QmNHMlRFQ2NmZktnRnI4VVh3?oc=5) <sub>体坛</sub>
- 📰 2026-10-01 [摘掉"S"标记背后：百度用一次"不融资"的转换，重写了自己的资本身份](https://news.google.com/rss/articles/CBMiU0FVX3lxTE05SUFhN3hLQlBybXRrMU1ZZkUxWWZhZVRWWWM2ODhkejR2eDFSTE5XMGpQcDhSN1dscE0xVEo3VDVMd2t0SzB3WnRZcWpua2ROTFFz?oc=5) <sub>搜狐网</sub>
- 📰 2026-09-30 [Could this driverless car cut Australia’s road toll?](https://news.google.com/rss/articles/CBMi-AFBVV95cUxQSVc2NVVObE5qbmxRUTRqX1ZVX2dtTTBZMUEydnZuSF92U19KXzJ4blhKTVoxaW1rR0lyTUJEQ0Y0SHNORjVRZ2Fsbm9ZcnM5blNpZndWalUtWXYzaTMxSE50cktuY2tQUEc0T3FmeDFFTXVkNl9XQmZsdG95RmhQRHpKYS0waVVBVS1ZcHNpTXE1eWluVV8zYloxYWVRSUJFTXdYMkdZanpLeE5jdHp2cG1vNGw3MW1tZWcwS1NsWkxGWk1ZUkJjMjhhb3E1VEswLV80dUlEXzNOUmk4SjdiTHBabTl5cUNITE5reWVheDM5dnNjQWNWdg?oc=5) <sub>The Courier Mail</sub>
- 📰 2026-09-30 [91y捕鱼大厅·“老字号新顶流”网络主题宣传活动今日上线 22家北京老字号集结焕新](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1XeTVDLWw4Wi1tbU1lN2otVXVHNG90TnRoWTdsR0E5czF5Q3A4M09NdkZzNlEzYjBfeGxTSHRuYlJLOTlMZmpKbmk4cE5KYVQ3QzZNbjhJUTd5QkNqdU1j?oc=5) <sub>Pchome电脑之家</sub>

</details>

<details><summary><b>Pony.ai</b> (99)</summary>

- 📰 2026-10-02 [纳斯达克中国金龙指数收跌1.03%](https://news.google.com/rss/articles/CBMiY0FVX3lxTE1VQklEWDF0MGhLYWFXUlhmQVp1QmRQdlVYRU81ZW5XMUdGU2Z6WF9UWFVkdk5CdlBkZlBNVTdGN00wWnZmU3J2bWltT1pTZ3lEdVVzNVBvZ0tpc2U4Q1BOMkpjaw?oc=5) <sub>东方财富</sub>
- 📰 2026-10-01 [Bernstein：中国自动驾驶的三重优势--规模、成本与采用率如何重塑全球格局](https://news.google.com/rss/articles/CBMif0FVX3lxTFB1SDVSLXhqNm1zekpaN3hEWHIycmc2N2p6ZWY3Y3B2MHhzaERNQi1oMjdYOXpTMTd1T1NIbVNkRF9UeXEtZDdhSUlEQlVjR05KQzI4ZG9zOEZSOUpOSGU0anc2eElVMEt5dXhhR2xEMHBTS1JVRXFKUHNYV0syOXc?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-01 [小马智行：董事兼高管Jun Peng拟出售300万份ADS，市值约1962万美元](https://news.google.com/rss/articles/CBMiZkFVX3lxTFBkVk1SNnlSS0ZGSTh2QnVLOW9waHBKQ0twTklMZXBEU3g2YUJtZUtaQklHZWF5TXpRaF9va051MHVOUU9SYnFqRlBJMFRJcVk0LXdxVWlENEdIMXpSYVRIa0JWeHpPQQ?oc=5) <sub>东方财富</sub>
- 📰 2026-10-01 [Driverless Taxis Arrive at Chek Lap Kok: Chinese AI Takes the World’s Toughest Driving Test](https://news.google.com/rss/articles/CBMi2AFBVV95cUxQUXhkSmRNTlBSTVQ5ekMxNU40M2N4bmMwMm51aWwzNmxYakFnZjVOWXYteGVmTndYMGtSWEVkejRFaWs5eTZadFY1dGhXdGtHVjhoZEFZN0hCM09neTRIbWZWMFEzS1dFc0oxRTUwZW9hcl8xNndpUWZyUmUtM281Mk8zTWhFZFFNNzduNndZcVJNTDlrOTdyODhsSEs3d1h0S0lYQjBtZTAwSXkzZXJVbnpOWmFMR0NQNVVoT2F6c0czcjF3YURhMUp0Qmx0QTZxNnBCaWxRNDE?oc=5) <sub>巴士的報</sub>
- 📰 2026-10-01 [Pony AI (PONY) In Focus On Index Changes As Valuation Debate Heats Up](https://news.google.com/rss/articles/CBMikwFBVV95cUxNXzRuT3R6S0ZOMnZfNXg5X0hzckVzeTVGM3BQYy13QzVrajlSMkpYaDYyYkJzUWpCUzNwSndWLWl1VFVaNURrRVh6SnZvdUl6SGtBcGl1OWZEU0FoT1dYeXFQX2xZRVlvSW5WSXpIdWUxcHBFdk93SHRtdmJlRUZlcUJBMXY3enF5N183dkRxQkhScTA?oc=5) <sub>Yahoo Finance</sub>

</details>

<details><summary><b>WeRide</b> (88)</summary>

- 📰 2026-10-02 [国庆车展人气爆棚！传祺越7全国圈粉持续热销，购车权益至高 5.6 万](https://news.google.com/rss/articles/CBMif0FVX3lxTE5BbkVsSkE3Q1VoczcyOVdhTmtkQWoyb2k4V0JXMk1SVWhVT1lPbURmSFo5TjRIcW8tLWZKNFVyRDdGWGhiQlFHRVZ0UDVuNnFuZnE3ejZIeWNGbTZ3c0p2ZFNvS0JlcDA1ZXV4c3p1b0FOSUdYVk5EUmtRZ3M1a0E?oc=5) <sub>k.sina.com.cn</sub>
- 📰 2026-10-02 [马斯克将特斯拉AI5芯片内存需求减半至72GB，AI6削减三分之一至144GB](https://news.google.com/rss/articles/CBMiUkFVX3lxTE8zalhDM0stSm00R0pXMVh2SVhJZzVKNG9DSXhKLWZ5WERKanBPVE5Cd3RYMVllVnJxQUlUdEVMbG96akxpemE0LW5MN3Nacld1blE?oc=5) <sub>icloudnews.net</sub>
- 📰 2026-10-02 [AION i60配置参数](https://news.google.com/rss/articles/CBMickFVX3lxTE1BUzB6aGRWTVN4OTVVYWUzZDBOaGFnUDd5YzI1cHdDSkEtVzVCcW92SlRDazlJeUFqbmJqeG1wWUNlTU0tSTRRV1FlWmptczV4TU1ZMHN3VTVvTHZRbHpaeUh5ZU4xUFlHSjd6TzVvbTR5QQ?oc=5) <sub>k.sina.com.cn</sub>
- 📰 2026-10-01 [Driverless Taxis Arrive at Chek Lap Kok: Chinese AI Takes the World’s Toughest Driving Test](https://news.google.com/rss/articles/CBMi2AFBVV95cUxQUXhkSmRNTlBSTVQ5ekMxNU40M2N4bmMwMm51aWwzNmxYakFnZjVOWXYteGVmTndYMGtSWEVkejRFaWs5eTZadFY1dGhXdGtHVjhoZEFZN0hCM09neTRIbWZWMFEzS1dFc0oxRTUwZW9hcl8xNndpUWZyUmUtM281Mk8zTWhFZFFNNzduNndZcVJNTDlrOTdyODhsSEs3d1h0S0lYQjBtZTAwSXkzZXJVbnpOWmFMR0NQNVVoT2F6c0czcjF3YURhMUp0Qmx0QTZxNnBCaWxRNDE?oc=5) <sub>巴士的報</sub>
- 📰 2026-10-01 [WeRide (WRD) Could Be 62% Undervalued Following Its Slovakia Partnership](https://news.google.com/rss/articles/CBMinAFBVV95cUxPWExvN3llMjJHa2RpTy1tUkpCVjViU05Pa2FYa1hIcm1iUU5VM3ZsVTdISVFMOTlMcVp4S0g5bVlWUC02VkdicnZOcHdnSS0tNzVkYnhhT3lLNHdVUzEzMWkzaWpnYmtLSmRKMFV5c2s0R3QzZlVHZ2N3dkpoTW9RQ1VweXJYdWVfaVNxZmpqa1BYZU5sSV92U1V0OUU?oc=5) <sub>Yahoo Finance</sub>

</details>

<details><summary><b>Horizon Robotics</b> (121)</summary>

- 💻 2026-09-29 [HorizonRobotics/Ego4WAM](https://github.com/HorizonRobotics/Ego4WAM) <sub>GitHub</sub>
- 💻 2026-09-24 [HorizonRobotics/CogWAM](https://github.com/HorizonRobotics/CogWAM) <sub>GitHub</sub>
- 📰 2026-10-02 [QNX & neueHCT win German carmaker camera programme](https://news.google.com/rss/articles/CBMigAFBVV95cUxQY29hVUJmRUlNVHEteEtPLUpzanprWVVoMWVaWGREUlp6YmhJdGZ6N2hCUDFyVE1UcWs2T3h5c0FSd2kyeGtxWVZXeC1JMDVlTzhWNzhTYk95T0oydGE5cGR6X2EwU0tndnQ4OXVnenNBdUdkYm15b2F0blBZdHhaRA?oc=5) <sub>IT Brief Asia</sub>
- 📰 2026-10-02 [【视频】新增51.2kWh宁德时代电池，iCAR V27 长续航版上市](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBsd1lRaE5qOEhrRng4QUNWMVY5dy1sWGNzLUkzbUtjM3hpMVdWQVRLdEN2UVNNMGVGZ0RZN1N5M0tjTEgxS2JLVW5FeTEwQnNZd3JWS0JHb1RJZUk?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-01 [Horizon Robotics Releases HSD V2.1 With End-to-End Reversing, iCAR V27 First in Line for OTA](https://news.google.com/rss/articles/CBMihwFBVV95cUxPSHZxeExuQzI1WGNoZHM2SnY2SzdfeVBmRE5fMk5sYnprM2c5cmhsRXljQ0lsUWdCZlZJa3hYTFNIQWNGbEsxQUVvQWJ6bVdXS25QRlJENTctSnZ3R205UE9odVBacUo0VkNkYWdKNkxUelhSSW9YcEdMVm93S2I3NEcydWVnWU0?oc=5) <sub>Pandaily</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (23)</summary>

- 📰 2026-10-02 [华为第一，元戎第二，Momenta 第三：城市NOA前三强差距只剩1.7%](https://news.google.com/rss/articles/CBMiSEFVX3lxTE9TN05LeXZBZHM5MVZKY0lmbGJXMjE5Qm9QZkJmTjNkOTdnN0xNc0NKZUNfM0hZZWFpYmdqMGRwODFYRDc4b2dJeA?oc=5) <sub>i.ifeng.com</sub>
- 📰 2026-10-02 [华为放手13天，赛力斯憋了3年的大招在巴黎炸响！](https://news.google.com/rss/articles/CBMif0FVX3lxTE1EU2I1a1BiV21VZGdwQWI1a08waTdfc1V6MDR0bXNwNWNDNGZrLUlDM1c0aUNFVmVBRUNsRjBQTWZCNGU1TmdJRG1qSlg0UHNHVmZDMUVuY3d4UmJyTlJoWXF3VzRHWDQyY21qSlBwX0RfMFdoemZwMTN5N3MyLVk?oc=5) <sub>k.sina.com.cn</sub>
- 📰 2026-09-30 [赛力斯代工，豆包上车，这台跨界SUV 在巴黎亮灯了\|赛豆科技\|赛力斯\|元戎启行\|me7\|aiva\|豆包大模型_新浪新闻](https://news.google.com/rss/articles/CBMiY0FVX3lxTE5UYlN4M1d3aFdYN1lZRGpLTTZpVmlBTzV1U3hLZ0s0emlPOTBXRUdJbHBVb1E1bld6ZG5KVVRzT2l0T19EbWNNdUx2RkdrSWtvcHB3b2VhTmF6OWZKWTBtRmFvSQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-29 [奔驰长轴距GLE上市：国产大五座豪华SUV值不值](https://news.google.com/rss/articles/CBMiXkFVX3lxTE9nLUUzRnVPRUNnUVNHTUtrYThkY29wOW05NXREWDZQY3NtT2EwMEtCclFxbFZ5S1ZGZTQ4RnEzTUw5X2dRaWMwbmR3eXBiVVdjcW1qbU9vV3BMM2VyalE?oc=5) <sub>汽车之家</sub>
- 📰 2026-09-29 [AIVA ME7巴黎完成全球首秀，纯电版快充15分钟即可补能至80%](https://news.google.com/rss/articles/CBMiW0FVX3lxTE03REhqQXhsSEhKZ1VIdDFkWXM5d3pPZjMwSGw2OWJFUkdhbXk4YWNTODhDT2JGQXU3bkpMNF9TakpjLWJVNWE4aXRpZXZGcHZxTzNwYTVMOXJSTlU?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Mobileye</b> (17)</summary>

- 📰 2026-10-02 [Mobileye Global Sees ADAS Momentum, Eyes Porsche Launch and Robotaxi Expansion](https://news.google.com/rss/articles/CBMi0wFBVV95cUxQYzRBUnBoMFNxTkNkYjFDNl9YbVpSRTVwb1N5SjFjMm56dEFiS0I2amZUQ1JqMHFTTlJHb2N2bkhlUXhOaTRpbHJIWWxhWWVBeUxsdlZ1bUtTdzRsZEUzV2NHWUpaVnN2ZzljWnhZSnlibjNHNjE5M1pyc21xekJGM1A3Z3V0SGZRVTVGSG1hMm9DWVlnSUhBQ3hKNk9yQjBZUU12bXN3MUFWc3k1XzZKXzZIeGh5bEVZaXpta3cwMjVHUGxlaHRINGhKdnhERU12TkRN?oc=5) <sub>MarketBeat</sub>
- 📰 2026-09-30 [Mobileye Global And 2 AI Driving Stocks To Watch](https://news.google.com/rss/articles/CBMiwwFBVV95cUxQSDFHSFBPOGlJM0RvZ0toN1JTdThRbFNLd3dIUmU0YV91Zl9hQTdWcnVxOXM5TUpHa281bEZkbDhXMDZmdWtHcmlTU0lfZl9SNTA5bC1QMmZQTVpKMkdGTmhiZWI0aDg1VnZ1Z1pFdW9WWHM0SzBaYlJMb2ZMNXN4TEdNampfQXlvekx6UEZRVEd4bU1IS0VWTVFRWkcyWE5IamRockRJQWF1b2lxWnBmVmNrS1RIQV9EYVhJSW05SkZodWvSAcgBQVVfeXFMTmRuV0ZhQ19iRGZhek1SUkVCV0VwWERKcWJkdklUV1NPUm9wSXBTN0hrSVRPUWthSTAzbE5PREh0QmhvUGlCSEtzRVcxRWtleUdtS2psMXhsUWNrSGp1VDRzc1F4NjN0dEZIT3pXWFRhYy1Nc3RSd0VBV0c3ZHlZUGFnU2wzZVQ3N0xtR0oxVzczV2VaR3h2U0ozRmVQTDlBOVRmTEtOdFFVS08tRy1WRllMUWFfLXN6ajFLbWx1T1FhWEtrS1IzeXc?oc=5) <sub>simplywall.st</sub>
- 📰 2026-09-30 [Mobileye Global And 2 Top Autonomous Vehicle Stocks To Watch](https://news.google.com/rss/articles/CBMingFBVV95cUxNSXlrYjJPWG8yQ1B2NF9hTXJ6YnJTdU9pRFFUTEwyMDZ0bjJMNHctSzdqbTFIc3k3T0RFNTVmUUtmRkhxdGQ0bjdHdHZhSkUzUHUzSlVoMTFNRVMzMUUyMlBCTDVLeG1MV1R1NkVXYmp3U2w1ZDRPUWNwMUduWjM4d0NIMFFUWnc3QXM4OXlQS2NDT0RobVRycjJsR0tMZw?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-09-30 [3 EV Stocks With Up To 39% Revenue Growth](https://news.google.com/rss/articles/CBMikAFBVV95cUxNbktkTHB2ZmdVWjdmMG5GaWdrR0dyenFac2dnV2d3eWpIVGxmOHJIeVpZU0RBREthd2xEenRPODRhcHhyaDVYV0FGX1l2eVhtTVNDZV9kN2t5UlR0b0Zyc1MtdDluZkZpaElxMlJud0VIZlN0eldEWGZVZ1Z5MlRyV0NRdU04bkRaaVdVV05nejE?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-09-29 [Mobileye at Evercore’s 9th Annual ADAS, AV & AI Forum: growth and autonomy](https://news.google.com/rss/articles/CBMiywFBVV95cUxPU2lGZVVxeEFwczgySTQyOFBlNkhoN2ROMU1aaFBsWWlFVF9nZndrN284OEMxUTJ6WGtLb1l5dWlCd25qSHRwdW8ybTZTcTg2ZnZ0eVM1MWhreko0dVYyNVNpSUtRd3MwUkdfU2MzT210ZUxLYzRPU2RjUnFjSGNyZGNBVTd2WURGNThzRnBGYXU2NFNsMGhyMmdhZFZpdl85WTV1SUtmS0dUYVJCcmljNFlNYTR1UUNBTF9fWFhieE52TGJlZHZ2QXltTQ?oc=5) <sub>Investing.com UK</sub>

</details>

<details><summary><b>Aurora</b> (40)</summary>

- 📰 2026-10-01 [Benjamin Y. Fong \| Has the Autonomous Trucking Revolution Arrived?](https://news.google.com/rss/articles/CBMijAFBVV95cUxPWTB5bDZtSlA4cm9UTFJadHZWc25OZEp0MzlHajE3Y29BLWlhMVl0WFdKZE1CQVNGMWdBdmljVmFSU1kxSUY0RU1SY0wxOFlQQjdQRV84REQ3NkxzZExTMnJRZlFrc1FzQmtiSFh1ampWUXdjemJWdHVmaVVRazZ3YWhhNmZkLWdsX01vUg?oc=5) <sub>Phenomenal World</sub>
- 📰 2026-10-01 [Cash retainer becomes a 3,419-share grant for director Brittany Bagley at Aurora Innovation (AUR).](https://news.google.com/rss/articles/CBMitAFBVV95cUxQU2hPbWJOMDVzZnJlX1Y3d3JDeDlKN3dVa0VUenFWdVR0V2VyT3NWTFVPdWZFbjRJV2VGVzZ5Z2pWRXc2NVF1MURRWjlkVGVQaDhXR2NhTkc5b1h3eUFmLTJIOFpDVlJfMG9IRFh3NDdDV04xSmE1U05pYVI0S2NqZ1R5UFJZclV3NHBzQkFYOXFuN1dOU25IOFRsWjY4UW9nSDBjejBPTHZXUTIwQkxJWGRKLWE?oc=5) <sub>Stock Titan</sub>
- 📰 2026-09-30 [How Aurora plans to reach 30,000 autonomous trucks by 2030](https://news.google.com/rss/articles/CBMikAFBVV95cUxOelgtT3NIQ0NYOXJPWXNFT21USXJNeFEweElLaHNpYnU2VEdmVU9fMTQ1a0t2OXZZRE1vTUFlNDltTHVnckljTVZDdGdfbEhlOHhBcjZ3UVI5NHRGZ3hiczN4YWljUFRfdTQtdTlIRnhCR3hNcThndzFMVnN3MFFDTmVWcTJTTDEtazNGc1FpS0w?oc=5) <sub>Transportation and Logistics International</sub>
- 📰 2026-09-30 [Did Driverless Truck Expansion Just Shift Aurora's (AUR) Investment Narrative?](https://news.google.com/rss/articles/CBMi0AFBVV95cUxNNlIyeW5hb01mWW5LaTNZQ2F1NUlJMUJqNkU1V1RraVRoSFVwWFNSd1lRdzNMOEVJRS14dXdqQmlubW10MEJrVmZJOTNxNXhLZ3NVWVFYaHhhQzBSd2dDRW1tNjNwUGNOb29NY3hocVF0R3dRYkFuMmxJUHk0N1FFSzF5cUY1ak9USnVFcU4xUjlNOENUYVFWOXpjcWx5VDJDY0VZVll0cGFnR0pOUnpTdHVUYUEzWkZIazR2LVZfNXlNSGVLZXRrYnhzZzNSM2hv0gHWAUFVX3lxTE03R0tsUmluLXZkZUtDekFGVXlkTEdRZ3J4RTg3S0ZkelJDTG5fWVhqajJ1YWtCXzRTOTQxVHhVWEVuZlU1WVExeE5EaldVQTVOQzVQZkRFY0RKLURqbVhrX3FXdF8waTRZY2R2LUhjeU91NEp3ZUFUZEx5UDdLOUQ2TnVfYjU3OEEwME1ZMFg2Szg5a1hhMUIyZzdJMkFvVnVGOHlPTDAwTUdtdzJqQm56R1hQX2tHLVg5Z1VkcUxKck1XU1hGNDQzck5MZEM5NEVVZWYtVFE?oc=5) <sub>simplywall.st</sub>
- 📰 2026-09-30 [Aurora Innovation: The Future of Autonomous Trucking](https://news.google.com/rss/articles/CBMijgFBVV95cUxOYnBpZWZmQkVwb3Q4aU9HVlhrYnMxTGI2Y3g1U190MEFRTlhGU1FrSXJoaEswQi1JNkVWbGQtYlN3YWkzQnd2YkFGNFhWVktIQ3RrOU9MR2ZFWHJjbUZ2ZDgzR1JQWGVxLUxYLWFzSFU1dU1HZks3SFEweGdhMjFhZVgxeTEydC1WMGZyaExn?oc=5) <sub>Intellectia AI</sub>

</details>

<details><summary><b>Zoox</b> (76)</summary>

- 📰 2026-10-02 [Self-driving big rigs roll into California as driverless future comes into focus](https://news.google.com/rss/articles/CBMiqAFBVV95cUxNMnlHV2RtMU1WUGJGVTdjZ3N3TzdreHdWTHZEZDBwUk1OaVlDb2Q3SnlqMGZXYkxsWkViUi13RDhLekxtYmNhcFE4N2xVRkxGNVBPYS1LYm1iU0hkUHR6ZHZRUDZqZzJsam0xSnRFTV9TYkdTMnVSdWg4QnRvWUlPQmxNTnFVUVc2Vm9RSkFwN1hMY2xtZlRTMFJZRFV2UWdTVHFVaHNud08?oc=5) <sub>New York Post</sub>
- 📰 2026-10-02 [Robotaxi operators will face fines for blocking first responders](https://news.google.com/rss/articles/CBMioAFBVV95cUxQTkxIUGliT0tPdU5KZzJoQm1JUDZXMVA0RGo5OHV5RV9pSm9lYzVyRUp0MV9WaFN4ZzJvdlRpMktmeHdOWDlYNG5xQk51cExkZTNtZFBKTG1yNG9nWG1aMzhCcEF2UEJXcjhIRHMtMXJCZ2lVbnVEaWRoM01BWjFtWmhCa1ZxRE5lX0hhSkJVSG5obVV1d05tamVnOFgtdzgt?oc=5) <sub>TechCrunch</sub>
- 📰 2026-10-02 [California signs law imposing fines on robotaxi operators — TechCrunch](https://news.google.com/rss/articles/CBMisAFBVV95cUxOc2hlSEkybklDM2hmdVY3Rm5hVTFFMDhwZW9BY1JyV3BHeW40ZDR4aWhwSW9PZWk1WXc1WU5Qd1V1Q1VGVjZvM2pxd0xEdEluOVlHaUtFR1R2Mk1nLWhGU3cxa3lja2dOTDc4Uk9mQmJseHFZUkJHVFdGcG5IYnFIdG54bmNtVDQ3dmtGakd5anpRb3RSa2lRRnhPWEt5cFZUVzcxSUZlWXZ4V05Tcjc0Nw?oc=5) <sub>UA.NEWS</sub>
- 📰 2026-10-02 [Robotaxi interior is not a private space, industry reworks seating and surveillance design](https://news.google.com/rss/articles/CBMixAFBVV95cUxQZkFBaWM4cDA5RGozNzg5NDgwbGswcFBmQzQ2REczN1RBeFM0alZ4VUtSb1lrbFMwdElSSElYdGRjSml0dzR2OXFfazY3djVBc2hLMzMxc0gxV2h5QjRDOHdxY1V4d0RwVnFibUhUbXFSVl9UYVpEUVBjR3RSM2hIWVVGVjhsdzNpbXBSWFFsb2FWRlJlYWVka1ptQzEtcmlJeHdsX0hzclE5SUJERVR3MVVjMFBWc3VLMzlKaFFhYWJ3LWds?oc=5) <sub>디지털투데이</sub>
- 📰 2026-10-02 [‘I Have to Buy My Dad That Lamborghini’: Indian Techie’s Silicon Valley Journey](https://news.google.com/rss/articles/CBMi2wFBVV95cUxNMTNIWTY0YWF5RW1vMXZFUVNYaGdZZUJfcGlNMm9XWG1jMy01QTFGdUZUZlQ3TFhNNFlrWlJITUJqQk5NRUJHOWZrZGNvZXhmZHZBSmtqUF9lM1duQUlIZ21MNkw5TWVEVGNQVzJSQXdrWEIwV200R1JETWtkaTFQaDdtdkhPTVR5WXRKVkp3R21kYnZmU2VvR09Hc2N2NVpxMFFkMElMRWNjVzVtel9KNjJUM2pfdW9UaTJ0X0lGeE8wb3BwYTZub1F6LURRdzNSWkE0ZVp0WTZjWXc?oc=5) <sub>Dainik Jagran MP CG</sub>

</details>

<details><summary><b>Motional</b> (21)</summary>

- 📰 2026-10-02 [Synopsys Unveils Autonomous Semiconductor Design Agents; 50 Collaborations Underway with Samsung, Nvidia](https://news.google.com/rss/articles/CBMidkFVX3lxTE5JSGVJNUZDUHBaZGpNYy1nTEcteGdsaUF0WVBIdUx2Yzd1X01lSkhIbHFqaDhENzZTOE1Zc29Rc0VRU0xfY3pLSDdwbk9sQ01oMWJxamNfOHZhRTdVdXQxRnIxdHpFNUg5UXVRX1haeDVEd2dGZ1E?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-02 [Google's Robot Strategy: Software First, With Gemini Robotics at the Core](https://news.google.com/rss/articles/CBMidkFVX3lxTFA4U0E1dE9RNFB2Q2Z6N0MtV05Db212M3dOMWtTeXY4eGJmN3BCa1ZFOUZxbHQ3akJwd1NSTi1MZU9TVGxTeUstYjFJMkFLMGFHRHZSX0drdGtTcVk0Y2VGZU10a0dPVlpmdlR3LUUxMkRkVDJYY3c?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-02 [South Korea's Hanchang Plunges Over 90% on First Day of Delisting Sell-Off, Tumbling to 85 Won](https://news.google.com/rss/articles/CBMidkFVX3lxTE1GYTN6S3BEUVlyVi1nMDhvd09hNE5MR0FQeWQwV2hkWGpEYXItR05jRlBJaGNQdk1kaWlqa3o1VWUwVEZtX3FUOTBWNy1ULVZGRmlOTFVSNmJyZk9OdU0zcmFPUFAwRkxVWkd4cFVMaHRFd3RHc0E?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-01 [Motional's Robotaxi Now Drives Smoother Than Waymo or Zoox, Field Test Finds](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5yeFZJMGJOcWFfRXRfR2ZnZTJiUjB4TTV3eGI3NlRxcUlYdXFYVWliUGNtalU4LWFiSHN5OGZGV0ltWm9fN01LcFpmRjI2V1FtVVk1dzNhMklsQ3c?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-01 [Motional Autonomy Roulette on Uber in Las Vegas Field Report｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBfTlhnZ0dNZkE2b2dJZnpyTmUzaGdwVjhUbVd6NHk3UHllc1JPWVkzbjVjTnJsMkVnWEx3czJhWjVEeDZJSkpJRVNkb0FzUnFYSHBHcWt6a1dJRkhFSUJR?oc=5) <sub>finance.biggo.com</sub>

</details>

<details><summary><b>comma.ai</b> (44)</summary>

- 📰 2026-09-30 [A $999 Box Promises Hands-Free Driving. Its Own Code Says ‘THIS IS NOT A PRODUCT.’ Now NHTSA Is Investigating Crashes That Killed Three.](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPNFIyamduTmQxb1dKNlh5Z1hCYUhyemoyU2I2bjFUWjZQSDVFSDFWOGxlM1hnQms4Q1lpalg0bXlCTEZTdVJ3eGtNTjlLamY2eW9LX09IejF6SkJxSmZ2QjRkU1pUczlRY2g3cUZIN3hvSUc3a3pUWHVKVk40MlY3Wk5SX3dnOHBl?oc=5) <sub>Yahoo</sub>
- 📰 2026-09-30 [The $999 Driving Gadget That Just Landed In Federal Crosshairs](https://news.google.com/rss/articles/CBMicEFVX3lxTE5kRFFmYXdUcmRRZ2wtNzF4QlRqQ0o1UmVscVhPWFlsVVE3S1dRVWdtLWFsOFJYeUlHY3phaWZYejBnWjFvVmxTcEJNRVBaQUJscU1VODZvRmxrREVYRDUyZlNJdTNsMUN4MmkwYXY1TWs?oc=5) <sub>HotCars</sub>
- 📰 2026-09-30 [Federal Probe Opens Into Aftermarket Self-Driving Hardware After Three Deaths](https://news.google.com/rss/articles/CBMiqgFBVV95cUxObDZzR1Z3QnZLaDR0bTRldUFvc0ZESTBoUHIyZE1PSmJHWFR4MmdrTi0zWkRFT250VG5WbTNuTWd4dzV6R1FIYzV2NzI2NGlfMzkwdHBTZFdIYkxpNG9pWldBQjdxTF9OOTFiZ1M2RlVfaFlkNThCRk41c21ZcXRsalFfOXpqTXRhYVRhaVREaFRRamMzcE41TGNMVTA5azFDWWxCalpHNkdCUQ?oc=5) <sub>Gadget Review</sub>
- 📰 2026-09-29 [US auto regulator closes airbag defect petition in about 807,000 Honda Odyssey cars](https://news.google.com/rss/articles/CBMigAFBVV95cUxPbllOY01DRVNHZUd5dXR2MXJDc0N1bXdVS2V2V3BzX0NqdmxORnl1cm9PU25FSU9YX2xyajJVNEVwdXFjZFM4eHQzX1ZmeHVTR3lyTVpnNlRna0dXMThiR1A5TGdseEtJTDUyQzVqN25nMUV3MVdYWVExMHlQZTFPWQ?oc=5) <sub>AOL.com</sub>
- 📰 2026-09-29 [NHTSA investigating deaths/injuries linked to comma.ai driving system](https://news.google.com/rss/articles/CBMitwFBVV95cUxQMUxNaU15eUlyamdpeUtadXJFQnlOMTJYOHJmdHRJYnpJMWdJb3hJRlRISlNGZVA3dkhSNnNVOG53N3dMQUtOVmFCNUpqRWhaXzA1TG5HM2I0aEV2bG42VkdoRXRyYUI3SkpnM3ZCS2JLUkMtemRJNEVONkh3cExkakF1LVNEVjNZMjFpVndjaExSaHhiME45NGZEbWFCUi1YQ2M4Q2pLOGFISWQyeGhVV1Z3QW0yM28?oc=5) <sub>repairerdrivennews.com</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
