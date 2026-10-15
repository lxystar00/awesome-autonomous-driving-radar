# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-10-15 · 1,282 papers tracked · 40 curated.

**Selection rule.** A paper is listed only if it (1) is primarily about autonomous driving,
(2) has public code, and (3) shows at least one strong signal: accepted at a top venue
(CVPR / ICCV / ECCV / NeurIPS / ICLR / ICML / CoRL / RSS / TPAMI, or ICRA / IROS / AAAI / RA-L),
≥200 GitHub stars, ≥3 citations / month, or a well-known lab with traction. Papers are then ranked by a
composite score (venue, stars, citation velocity, LLM rubric for novelty / rigor / impact, SOTA claims)
with a per-topic cap. See [`scripts/rank.py`](scripts/rank.py).

📅 [Daily digests](daily/) · 🗓️ [Weekly digests](weekly/) · 📦 [Raw data](data/)

## Contents

- [VLA / VLM for Driving](#vla--vlm-for-driving) (8)
- [World Models & Generative Simulation](#world-models--generative-simulation) (6)
- [End-to-End Driving & Planning](#end-to-end-driving--planning) (9)
- [3DGS / NeRF Reconstruction & Sensor Sim](#3dgs--nerf-reconstruction--sensor-sim) (3)
- [Perception: BEV, Occupancy, 3D Detection, Mapping](#perception-bev-occupancy-3d-detection-mapping) (9)
- [Datasets & Benchmarks](#datasets--benchmarks) (2)
- [Safety, Robustness & Evaluation](#safety-robustness--evaluation) (3)
- [Industry Tracker](#-industry-tracker)

## VLA / VLM for Driving

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Teaching Vision-Language-Action Models What to See and Where to Look](https://arxiv.org/abs/2607.01658)<br><sub>Yuguang Yang, Canyu Chen, Zhewen Tan et al.</sub> | ECCV 2026<br>2026-07<br>📑 1 | [⭐ 33](https://github.com/ShivaTeam/DriveTeach-VLA) | Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving |
| [DeepSight: Long-Horizon World Modeling via Latent States Prediction for End-to-End Autonomous Driving](https://arxiv.org/abs/2605.10564)<br><sub>Lingjun Zhang, Changjie Wu, Linzhe Shi et al.</sub> | ICML 2026<br>2026-05<br>📑 1 | [⭐ 31](https://github.com/hotdogcheesewhite/DeepSight) | End-to-end autonomous driving systems are increasingly integrating Vision-Language Model (VLM) architectures, incorporating text reasoning or visual reasoning to enhance the robustness and accuracy of driving decisions |
| [SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving](https://arxiv.org/abs/2610.20609)<br><sub>Shaoyuan Xie, Zihan Zhang, Jingxuan Wang et al.</sub> | CoRL 2026<br>2026-10 | [⭐ 19](https://github.com/ASGuard-UCI/safedrive-vla) | Vision-Language-Action (VLA) models are gaining attention in autonomous driving, inheriting commonsense priors from large language models (LLMs) and widening the navigation interface from a fixed command set to free-form… |
| [CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving](https://arxiv.org/abs/2607.04179)<br><sub>Zhaohong Liu, Hao Ye, Xianlin Zhang et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 1](https://github.com/MICLAB-BUPT/CritiqueDriveVLM) | End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving |
| [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)<br><sub>Nan Yang, Zhanwen Liu, Linfeng Zhang et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 9](https://github.com/Zizzzzzzz/MVPruner) | Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings |
| [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)<br><sub>Yuan Gao, Wenting Miao, Mattia Piccinini et al.</sub> | IROS<br>2026-07<br>📑 1 | [⭐ 27](https://github.com/TUM-AVS/Chat2scenic) | Validating autonomous driving systems requires diverse, regulation-compliant test scenarios |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 9 | [⭐ 504](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
| [Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air](https://arxiv.org/abs/2605.31066)<br><sub>Tianle Zeng, Yanci Wen, Xueang Yu et al.</sub> | arXiv<br>2026-05<br>📑 2 | [⭐ 1,115](https://github.com/louiszengCN/CarlaAir) | Recent aerial vision-language-action (VLA) models show promising single-UAV capabilities, such as tracking moving objects and navigating to language-specified landmarks |

## World Models & Generative Simulation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [HERMES++: Toward a Unified Driving World Model for 3D Scene Understanding and Generation](https://arxiv.org/abs/2604.28196)<br><sub>Xin Zhou, Dingkang Liang, Xiwu Chen et al.</sub> | ICCV 2025<br>2026-04<br>📑 4 | [⭐ 72](https://github.com/H-EmbodVis/HERMESV2) | Driving world models serve as a pivotal technology for autonomous driving by simulating environmental dynamics |
| [FrozenDrive: Zero-Shot Text-Guided Driving Scene Generation and Data Augmentation with Parameter-Free Frozen Diffusion Model](https://arxiv.org/abs/2606.20110)<br><sub>Yuhwan Jeong, Hyeonseong Kim, Daehyun We et al.</sub> | ECCV 2026<br>2026-06<br>📑 1 | [⭐ 10](https://github.com/daehyunwe/FrozenDrive) | Synthetic data for autonomous driving is surging, powered by diffusion models that promise scalable scene generation |
| [MESSENGER: Memory-Enhanced Sequential Scene Flow Estimation via Autoregressive Next-Frame Forecasting](https://arxiv.org/abs/2610.10759)<br><sub>Jiuming Liu, Jianing Li, Mengmeng Liu et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 0](https://github.com/liujiuming123/Messenger) | Scene flow can capture low-level 3D motion displacements in dynamic scenarios |
| [ASTAD: Asymmetric Style Transfer for Synthetic-to-Real Adaptation in Autonomous Driving](https://arxiv.org/abs/2606.29286)<br><sub>Dingyi Yao, Xinqi Zhang, Lihui Peng et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 1](https://github.com/Dingyi-Yao/ASTAD) | Synthetic data mitigates the data scarcity problem in autonomous driving perception |
| [Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends](https://arxiv.org/abs/2606.01164)<br><sub>Jiuming Liu, Chaojun Ni, Mengmeng Liu et al.</sub> | arXiv<br>2026-06<br>📑 7 | [⭐ 243](https://github.com/liujiuming123/Awesome-Interactive-World-Model) | With rapid development of large language models and diffusion-based content generation, world modeling has attracted increasing research attention, benefiting various downstream domains such as game engines, embodied AI,… |
| [Is Your Driving World Model an All-Around Player?](https://arxiv.org/abs/2605.10858)<br><sub>Lingdong Kong, Ao Liang, Tianyi Yan et al.</sub> | arXiv<br>2026-05<br>📑 5 | [⭐ 256](https://github.com/worldbench/WorldLens) | Today's driving world models can generate remarkably realistic dash-cam videos, yet no single model excels universally |

## End-to-End Driving & Planning

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](https://arxiv.org/abs/2609.26792)<br><sub>Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.</sub> | CoRL 2026<br>2026-09<br>📑 1 | [⭐ 12](https://github.com/VAIL-UCLA/DreamStream) | Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions |
| [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)<br><sub>Shen Zheng, Anurag Ghosh, Gaurav Parmar et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 32](https://github.com/ShenZheng2000/WarpI2I) | Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs) |
| [G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance](https://arxiv.org/abs/2606.26017)<br><sub>Hang Yu, Ye Jin, Alessandro Canevaro et al.</sub> | IROS 2026<br>2026-06<br>📑 4 | [⭐ 6](https://github.com/HangYuu/G2DP) | In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors |
| [SUV: Future Scene Understanding as Video Generation for End-to-End Driving](https://arxiv.org/abs/2608.03084)<br><sub>Yibo Yuan, Jiacheng Fu, Jiangtong Zhu et al.</sub> | RA-L 2026<br>2026-08 | [⭐ 20](https://github.com/ASH-2046/SUV) | End-to-end driving requires a coherent understanding of future scenes, yet existing methods model these scenes using task-specific heads and output formats, with limited scalability |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 16 | [⭐ 347](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
| [Latent-Centroid Steering: Single-Pass Classifier-Free Guidance for Command-Aligned Autonomous Driving](https://arxiv.org/abs/2608.00237)<br><sub>Meibo Hu, Jiamian Wang, Pichao Wang et al.</sub> | IROS 2026<br>2026-08<br>📑 1 | [⭐ 2](https://github.com/codingmlinprocess/LCS) | Vision-language models (VLMs) have recently emerged as a promising paradigm for end-to-end autonomous driving, enabling agents to map multimodal inputs and high-level navigation instructions directly to executable trajec… |
| [DVGT-2: Vision-Geometry-Action Model for Autonomous Driving at Scale](https://arxiv.org/abs/2604.00813)<br><sub>Sicheng Zuo, Zixun Xie, Wenzhao Zheng et al.</sub> | arXiv<br>2026-04<br>📑 14 | [⭐ 367](https://github.com/wzzheng/DVGT) | End-to-end autonomous driving has evolved from the conventional paradigm based on sparse perception into vision-language-action (VLA) models, which focus on learning language descriptions as an auxiliary task to facilita… |
| [STAGE: STyle-controllable Action GEneration for personalized autonomous driving](https://arxiv.org/abs/2607.29517)<br><sub>Zihao Liu, Xing Liu, Yizhai Zhang et al.</sub> | RA-L<br>2026-07 | [⭐ 6](https://github.com/CarlDegio/STAGE) | Driving style refers to the behavioral preferences that drivers maintain during driving, shaped by their diverse experiences, habits, and needs, and is typically reflected in varying levels of aggressiveness |
| [A Survey on End-to-End Autonomous Driving Training from the Perspectives of Data, Strategy, and Platform](https://arxiv.org/abs/2610.00926)<br><sub>Chengkai Xu, Yiming Cui, Jiaqi Liu et al.</sub> | arXiv<br>2026-10<br>📑 5 | [⭐ 106](https://github.com/Jiaaqiliu/Awesome-Training-Ecosystem-for-E2E-AD) | Autonomous driving is a cornerstone technology for the future of intelligent transportation, where end-to-end learning has emerged as a transformative paradigm that directly maps multimodal sensory inputs to driving acti… |

## 3DGS / NeRF Reconstruction & Sensor Sim

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DriveWeaver: Point-Conditioned Video Inpainting for Controllable Vehicle Insertion in Autonomous Driving Simulation](https://arxiv.org/abs/2606.31918)<br><sub>Junzhe Jiang, Zipei Ma, Zijie Pan et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 16](https://github.com/LogosRoboticsGroup/DriveWeaver) | A pivotal step in autonomous driving simulation involves inserting foreground vehicles with predefined trajectories into simulated scenes |
| [Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796)<br><sub>Leshu Li, Jie Peng, Yang Zhao</sub> | ICRA<br>2026-06 | [⭐ 14](https://github.com/UMN-ZhaoLab/Pocket-SLAM) | 3D Gaussian Splatting (3DGS) has garnered significant attention in Simultaneous Localization and Mapping (SLAM) due to its advances in capturing fine-grained geometry features and synthesizing novel views |
| [MM-TRELLIS: Point-Cloud Guided Multi-Modal 3D Vehicle Generation in Autonomous Driving](https://arxiv.org/abs/2606.24301)<br><sub>Hongli Xiao, Youjian Zhang, Yucai Bai et al.</sub> | ICRA 2026<br>2026-06 | [⭐ 8](https://github.com/HongliXiao/MM-TRELLIS) | Recovering realistic 3D vehicle models from autonomous driving scenes is crucial for synthesizing training data and building simulation environment |

## Perception: BEV, Occupancy, 3D Detection, Mapping

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Deformable Gaussian Occupancy: Decoupling Rigid and Nonrigid Motion with Factorized Distillation](https://arxiv.org/abs/2605.28587)<br><sub>Yang Gao, Wuyang Li, Po-Chien Luan et al.</sub> | CVPR 2026<br>2026-05<br>📑 2 | [⭐ 22](https://github.com/vita-epfl/DeGO) | Understanding dynamic 3D environments is essential for safe autonomous driving, particularly when reasoning about human-centric, nonrigid agents |
| [FreeOcc: Training-Free Embodied Open-Vocabulary Occupancy Prediction](https://arxiv.org/abs/2604.28115)<br><sub>Zeyu Jiang, Changqing Zhou, Xingxing Zuo et al.</sub> | RSS<br>2026-04<br>📑 6 | [⭐ 140](https://github.com/the-masses/FreeOcc) | Existing learning-based occupancy prediction methods rely on large-scale 3D annotations and generalize poorly across environments |
| [Revisiting Token Compression for Accelerating ViT-based Sparse Multi-View 3D Object Detectors](https://arxiv.org/abs/2604.14563)<br><sub>Mingqian Ji, Shanshan Zhang, Jian Yang</sub> | CVPR 2026<br>2026-04<br>📑 1 | [⭐ 9](https://github.com/Mingqj/SEPatch3D) | Vision Transformer (ViT)-based sparse multi-view 3D object detectors have achieved remarkable accuracy but still suffer from high inference latency due to heavy token processing |
| [Horizon3D: Sparse Radar-Camera Fusion for Long-Range 3D Perception in Autonomous Driving](https://arxiv.org/abs/2606.31096)<br><sub>Geonho Bang, Geunju Baek, Dongyoung Lee et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 23](https://github.com/geonhobang/Horizon3D) | Long-range 3D object detection is critical for safe autonomous driving at highway speeds, yet existing radar-camera fusion methods remain limited at extended ranges |
| [Explainability-Aware Frustum Attack: Exposing Structural Vulnerabilities in LiDAR-Based 3D Object Detectors](https://arxiv.org/abs/2606.29963)<br><sub>Chengzeng You, Binbin Xu, Soteris Demetriou</sub> | ECCV<br>2026-06 | [⭐ 2](https://github.com/SecMindLab/Saliency_LiDAR) | The structural vulnerabilities of point cloud-based 3D object detectors remain poorly understood |
| [PointLAM: Local Attentive Mamba for Efficient Point-based 3D Object Detection](https://arxiv.org/abs/2609.21780)<br><sub>Xuanming Shang, Weijia Zhang, Chao Ma</sub> | ECCV 2026<br>2026-09 | [⭐ 5](https://github.com/PointLAM/PointLAM) | 3D object detection from LiDAR point clouds faces a fundamental dilemma: voxel-based methods achieve efficiency at the cost of geometric quantization, while point-based methods preserve fidelity but suffer from prohibiti… |
| [UniD-Shift: Towards Unified Semantic Segmentation via Interpretable Share-Private Multimodal Decomposition](https://arxiv.org/abs/2605.07356)<br><sub>Shuai Zhang, Zhecheng Shi, Zhuxiao Li et al.</sub> | CVPR 2026<br>2026-05 | [⭐ 5](https://github.com/shuaizhang69/UniD-Shift) | Semantic segmentation of large-scale 3D point clouds is crucial for applications such as autonomous driving and urban digital twins |
| [Vernata: Self-Supervised Learning of LiDAR Point Representations](https://arxiv.org/abs/2608.06919)<br><sub>Oliver Lemke, Alexander Liniger, Abel Gawel et al.</sub> | IROS 2026<br>2026-08 | [⭐ 20](https://github.com/rai-opensource/vernata) | LiDAR serves as a primary sensing modality for robots operating in outdoor environments |
| [Towards Compact Autonomous Driving Perception with Balanced Learning and Multi-sensor Fusion](https://arxiv.org/abs/2606.02979)<br><sub>Oskar Natan, Jun Miura</sub> | arXiv<br>2026-06<br>📑 45 | [⭐ 9](https://github.com/oskarnatan/compact-perception) | We present a novel compact deep multi-task learning model to handle various autonomous driving perception tasks in one forward pass |

## Datasets & Benchmarks

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Towards All-Day Perception for Off-Road Driving: A Large-Scale Multispectral Dataset and Comprehensive Benchmark](https://arxiv.org/abs/2604.27499)<br><sub>Shuo Wang, Jilin Mei, Wenfei Guan et al.</sub> | RA-L 2026<br>2026-04 | [⭐ 6](https://github.com/wsnbws/IRON) | Off-road nighttime autonomous driving suffers from unreliable visible-light perception, making infrared modality crucial for accurate freespace detection |
| [123D: Unifying Multi-Modal Autonomous Driving Data at Scale](https://arxiv.org/abs/2605.08084)<br><sub>Daniel Dauner, Valentin Charraut, Bastian Berle et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 402](https://github.com/kesai-labs/py123d) | The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics |

## Safety, Robustness & Evaluation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [CCFM: Collision-Constrained Flow Matching for Safety-Critical Scenario Generation](https://arxiv.org/abs/2607.04451)<br><sub>Ke Li, Kaidi Liang, Yuxin Ding et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 3](https://github.com/KELISBU/CCFM) | Evaluation of autonomous vehicle (AV) planners in safety-critical closed-loop simulation is essential for real-world deployment |
| [Lipschitz Optimization for Formal Verification of Homographies](https://arxiv.org/abs/2605.23203)<br><sub>Jean-Guillaume Durand, Panagiotis Kouvaros, Maxime Gariel et al.</sub> | CVPR 2026<br>2026-05 | [⭐ 2](https://github.com/jeangud/homography-verification) | The adoption of vision neural networks in regulated industries requires formal robustness guarantees, especially in safety-critical domains such as healthcare, autonomous vehicles, and aerospace |
| [CADET: A Modular Platform for Evaluating Distributed Cooperative Autonomy in Connected Autonomous Vehicles](https://arxiv.org/abs/2606.04072)<br><sub>Pragya Sharma, Brian Wang, Mani Srivastava</sub> | ICRA 2026<br>2026-06<br>📑 1 | [⭐ 0](https://github.com/nesl/cadet) | Deep learning models are increasingly central to autonomous vehicle (AV) pipelines, yet their integration has traditionally followed a monolithic design where perception, planning, and control execute on a single onboard… |

## 🏢 Industry Tracker

Latest 14 days of news, official blog posts and new open-source repos from tracked companies. Full daily feed in [`daily/`](daily/).

<details><summary><b>Waymo</b> (208)</summary>

- 📝 2026-10-08 [Sober Drivers Still Face Nearly 4x Nighttime Risk: Why Road Safety Demands a Safe System Approach](https://waymo.com/blog/2026/10/sober-driving-benchmarks) <sub>official blog</sub>
- 📝 2026-10-08 [Waymo Closes $5 Billion Debt Financing to Accelerate Business Expansion](https://waymo.com/blog/2026/10/waymo-closes-5-billion-debt-financing) <sub>official blog</sub>
- 📰 2026-10-15 [Tesla Robotaxi Tally Hits 739, Trails Waymo’s 1,185 [2026]](https://news.google.com/rss/articles/CBMid0FVX3lxTE5DeGxZSWQyTzdKUHBkUnFqV2Z2ODFsc2JwSHNxZ1psUGE5WHNNbmpWTzhYUlVSWkozRFM2aUZPTDl4SkpUdW1Ubm5LeWxULXRXY1cwdVRlTjRjWHdnRWhEQ3kzTVRvOXYwcmpFLXBnUlVmYlNMNnJR?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-10-15 [Waymo expands to 20 cities as NHTSA opens new school bus safety probe](https://news.google.com/rss/articles/CBMingFBVV95cUxPTGJublNHeG9KZDVRbFZIdzNad2w4ZTQzY01XcEJ2ZnJkRzM5NkdQZm9TZHNyTEZ6anhyemJPdU9kbnpKQUFLYWlWMVlxekRVUjZTaEpuOXpneGN3dFhvUHRRdTdEZkVJUGNMOXRDaWp2Y0k0SXNWQkFacEtwU0h6SXIzTzVtUktMdjZCRkVITFlVWmJMQ0lEZVRKWGhCdw?oc=5) <sub>Startup Fortune</sub>
- 📰 2026-10-14 [Tesla Robotaxi Fleet in Austin Soars 8x in a Month [2026]](https://news.google.com/rss/articles/CBMid0FVX3lxTE5rTFJuUnZQa0NUWmJkMVdGQllOMWFvcTh2WkI0NGxKWVZYWnB5Y2VUOUE4N2ptN21Pb0gxVDFzWGZ1M0lvWEtJUHc3aTZNMTNpUkJBejFBMVJIemJrenJ6bFMxQmlkNkt0cFFhNVpselhKc0o5LWJz?oc=5) <sub>https://tech-insider.org/</sub>

</details>

<details><summary><b>Tesla</b> (341)</summary>

- 📰 2026-10-15 [Tesla Robotaxi Tally Hits 739, Trails Waymo’s 1,185 [2026]](https://news.google.com/rss/articles/CBMid0FVX3lxTE5DeGxZSWQyTzdKUHBkUnFqV2Z2ODFsc2JwSHNxZ1psUGE5WHNNbmpWTzhYUlVSWkozRFM2aUZPTDl4SkpUdW1Ubm5LeWxULXRXY1cwdVRlTjRjWHdnRWhEQ3kzTVRvOXYwcmpFLXBnUlVmYlNMNnJR?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-10-15 [Musk Teases 'Banger' Tesla AI Demo, Hints at Recursive Self-Improvement](https://news.google.com/rss/articles/CBMipgFBVV95cUxOZFFXMExRVE5GdXppeE5aMjJiMDF1QV9aeUthMTUyNU9uTW9qQ3VHdTVEdnYzWEpLejZZdEt4OWthMU80ZWpQc20yVVlXb01DUHhJRFkxRGpUeVhaMm1aWGh1cUN1MDNHVUVueVZqN096eGFCNEd0cjZkRHpQNHdxR2NRNVFXdkc3MXQzOXFZai14X2syZlJwSTU2SmlSTWh4cGlyRml3?oc=5) <sub>BASENOR - Tesla Accessories</sub>
- 📰 2026-10-15 [Tesla Cybercab Hits 300+ in Austin: Inside the Hardware [2026]](https://news.google.com/rss/articles/CBMic0FVX3lxTFBSalF5NS11ckNDZDVpQ1hpTDlERTR4dWhRUVVJckZOb1dtTnRVMWtRQ0hSbU8xZDNvR2J0WV96TmFpX0p1QXFlSXBEMG12LVNDbkNHelBDTThPNFRRajQxYWZMWDlUZUNfQU1UeWpPV0VFRjQ?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-10-15 [特斯拉向HW3英特尔芯片版老款Model S/X推送FSD v14 Lite](https://news.google.com/rss/articles/CBMifkFVX3lxTE9zUkRJbWdfOG9wS084c0tQLU1XVTRMb3o0MXp1OEszcjl4b2RhQmQ3T2JxcGRQY0phX2lZUEtXbVp1WE5Wa0xtd1pyRXRCbGNHMjV4TFMxNkV2Wjg1djV5V1ZCbUNFc1RRai1xblJLeDFqS0tQdW1SOGxRWVYzUQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-14 [Tesla Robotaxi Fleet in Austin Soars 8x in a Month [2026]](https://news.google.com/rss/articles/CBMid0FVX3lxTE5rTFJuUnZQa0NUWmJkMVdGQllOMWFvcTh2WkI0NGxKWVZYWnB5Y2VUOUE4N2ptN21Pb0gxVDFzWGZ1M0lvWEtJUHc3aTZNMTNpUkJBejFBMVJIemJrenJ6bFMxQmlkNkt0cFFhNVpselhKc0o5LWJz?oc=5) <sub>https://tech-insider.org/</sub>

</details>

<details><summary><b>NVIDIA</b> (211)</summary>

- 📰 2026-10-15 [Nvidia, Broadcom and Micron Could Drive 40% of S&P 500 Earnings Growth](https://news.google.com/rss/articles/CBMiqAFBVV95cUxOcWFQeV9JN21ueG84MEFJZzc3aFM1RlRfdm4zUUJqS0Q3RVZQTm9wWUVTSTc2SUdpeVduZnd6NVFLSU1YZVdpVjVDeXBtb1QxUzg1WTVHdGJuM2dINlE3dlg2VFdCbkdvTEV5R2x1YURyZnJoWXBJSklLZzZvMzVWNGk5T2x2UVVuTVU1SFBHbDBLU3EtbzZQbGdyeUdEVjZYcGhkZEg4a1Y?oc=5) <sub>CryptoRank</sub>
- 📰 2026-10-15 [Embedl and Space Cargo Unlimited Bring AI Autonomy to the Space Edge](https://news.google.com/rss/articles/CBMirwFBVV95cUxPd2hNX28zMGtuN3JSODhKQVdDYXg0bi1LZ3VRdWpWdnZ6VTlzRW83MVA0V3BvckNWNUFLSnIzTUxNMUZ4S3NzeXdaeGxTMV9YeGdkeEZPb2FzRGFDMUVRQk95RXN0eHNpQ0JxZXRIdkdFdERGM1VVNzJFTFpxaEo2S2RSUkM5WjNLWUh1Z2pRMWZWUE9jVElkeHhCTzh4QXJmWU9FNGk0aU1vTUdoYjc4?oc=5) <sub>EIN News</sub>
- 📰 2026-10-14 [European Cities Deploy NVIDIA-Powered AI Agents to Run Smarter Urban Operations](https://news.google.com/rss/articles/CBMiekFVX3lxTE5mU01rUUJVYmZVeVFELWp3azNXc2xOTGF2cGg4clFwSlpyTmhLRmdFV0ZhcU5kOE5fWlBEbEx0WDhYOTdtQWp6VnFZT0FPUmNJVjFoX2p2b2pFZEZQUEs1SXQtdlBUaThzeDFjNkJ1bWQtOVgtTzRUU0hR?oc=5) <sub>NVIDIA Blog</sub>
- 📰 2026-10-14 [Nvidia will invest $10B in Europe’s tech ecosystem](https://news.google.com/rss/articles/CBMie0FVX3lxTE42Z2d0UFJPM2pJQjVZTHJyVGRhekc0eVFiTmFVQ3JmVTluNVdGV19LR3FBeTRxS21zaEpXNjBfelF3RTlYZDN4ZmtmQnBrX1l6T0h0SzBkazF5ZGZublFHVXBOdjVjbXBnMmdVbDVXNDZ6MUFxUGV4eGlDNA?oc=5) <sub>GamesBeat</sub>
- 📰 2026-10-14 [NVIDIA and Semiconductor Leaders Advance AI Across Chip Design and Manufacturing for AI-Defined Fabs](https://news.google.com/rss/articles/CBMi0AFBVV95cUxQY0JQSW1rVk16Vk96aEt1QzRJeHNUNXZfclVRVlBFdmhhQ09HS2N3YUlfRnRTejgtdGkwc040QWdHbXkyVXFJcW1uaTdZdV9EMUo0ZDN6cnFiOWxneTlidVpIYmljSHJkTVJaNmhUTDRwb2czQXNtN00taFQ5MkhBZVlITUN6QTBYcUVrdV8tQXFtcDJ2d2EwRjVONU1VdGRCNUhRRnBUbUp1UFRfMmNqaWFJMVdRVXRLa2UzTF9yVmhnM0VadXk3TzRSTjJMZGJn?oc=5) <sub>NVIDIA Newsroom</sub>

</details>

<details><summary><b>Wayve</b> (62)</summary>

- 📰 2026-10-14 [UK tech companies raise $25.7bn this year](https://news.google.com/rss/articles/CBMilwFBVV95cUxQWU1zbVpRTTZiWmlDVkpqVm8xZmVDdVZ1Yld4WjlWcENtMWl1U0VfVnNKck91bTRQSl9ITW10WmY4MzdTNkZ6NjQtMXBYN0djWXlhbDNDaHhkcWdCZEw0LUlBSDBLZ3ZheVVqOUJZR05WQzJVemk1TW1NMlMxR1NLTlRLTGpUQ2ZWQVdtWlk4akVIYW15NGhz?oc=5) <sub>Electronics Weekly</sub>
- 📰 2026-10-14 [Uber and Pony AI take robotaxis to Manchester](https://news.google.com/rss/articles/CBMigwFBVV95cUxPQTNhV29nNHNKYXhNTnV6QUNEaVVsdm5HSHctTHZsaU00aW9qWkl1Q0xvdlFQNHpYZ2o1SDc2MF9mUUFRYTh4aGloaGdlZWV5bGtoZ2hETDFrMVNyeHdtXzFSSkNMZTlEVkZiTmJIcjNVLVY4VVF1anBKLXQ3dDVUeDhtTQ?oc=5) <sub>Zag Daily</sub>
- 📰 2026-10-14 [UK Government backs World Congress for Intelligent Transport Systems](https://news.google.com/rss/articles/CBMiogFBVV95cUxPbllTN1lLWmlFT2VqWDhBaGxTRjhqQlFMQjVvZ29kMm1tRGpzMlRjVHhmU3ZpTHNwQVZYWWlYOTNudUlTS0g5N0lzdnd3M2lBZlBvSVlwaXlFclFhcXB0dXJzdGdjS3ZtY1o2QjNER2ZaS0V4b19ocEd5MUNtN2diZGR5VDE3bk5DbGRfOS1aU3lJWEdCVHUyaWFjWFc3UWNoTkE?oc=5) <sub>Zag Daily</sub>
- 📰 2026-10-13 [A ride in a self driving Fiat](https://news.google.com/rss/articles/CBMiZkFVX3lxTFBLWHl6Y0t5QzNXY185VFVmcnZzMjJJNnR6T1ZfMkVZbFdOcVVoaXBIdzYwS1lKMjQ4UVNTQXpkYlc4S3p5SGpnbG11OC1ZeTlzdmI5TnF4WHZIYlhIRFRfSHpqQVNZUQ?oc=5) <sub>Focus Malaysia</sub>
- 📰 2026-10-13 [Croatia trials full driverless robotaxi service](https://news.google.com/rss/articles/CBMikgFBVV95cUxPc1IxMUxJSEd3VTFBQ01hcUloWnNoSVFIcE9IU2NpcXloRDFQRWZPeHFVYXRBV3h5ZmZEWHNqallFaloxcVl1eWE5RWQ2RngtVVJYOFg5ZERneENwMkRvWGdUaXI0Yjh1Q3pZemFBU2VkOXQ4TDFkakU1eVdBUUhKYWhQRlhWWktYS1BfZ1hDdTJPdw?oc=5) <sub>Yahoo Finance UK</sub>

</details>

<details><summary><b>Momenta</b> (82)</summary>

- 📰 2026-10-15 [豪华SUV怎么选？XT5 PHEV 25.99万起全系标配智驾，兼顾动力油耗+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE5mZTNRVnJXQXlJWVp0Q2N4a05KNkp3aUl3OXB5eUNrSnUxLXdzNWFZbFBFSldULWtKUXc2dTU5Z3VPYVpncmk4cTV0Q294a2lwNDE2dGFRM2dqR3hwVTNPTno3TUhSMDlqV0toN180TE00dw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-15 [15万级哪款SUV配Momenta辅助驾驶，自动泊车辅助靠谱度怎么验](https://news.google.com/rss/articles/CBMia0FVX3lxTE04V3E1Vkc4OE04MHVPUUlQNXYxcEpONEV1cGVVSzduYjJfNmRxVmNDM2xVNWVvZ3QyaDRSWkY1YU9DVkZxQk9TM3JPVGRtMjl3UHpLMEdWZFFxV1I2RkszZ0VIRmFIX2dWLUUw?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-14 [[China Shock, K-Industry on the Brink \| Autos] 2. China Hits the Accelerator on "Autonomous Driving"... Even Europe's Luxury Automakers Reach Out](https://news.google.com/rss/articles/CBMiZEFVX3lxTE8yM1VubTBHUjFyM1RQejJiV0ZLMzlaY0JFbEdlYl9UVzZKRDNjXzBQaGxDc1RJTlFqVjBXZTMycWdZLWlVd3JaNldqblRYOEZJMDE2MEJYcmMzRDNBUVBoMGZ6SGg?oc=5) <sub>아시아경제</sub>
- 📰 2026-10-14 [更像是一位时刻陪伴在身旁的“老司机”。#新车划重点# 带你看看这台车在智驾方面都有什么亮点。1、【越级感知硬件】](https://news.google.com/rss/articles/CBMiY0FVX3lxTFBvVmJQQTIwUVFBdW44dGRxSVpwRm1DOExRd2hMalZxSzV6ZmNxOTZzeC0zNTJwS1lmSGVTOURTb1ZYVk82RE5iZFNZZk43UldBTzVqWC1hSGNpMDI4TXUwaHZNaw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-14 [带激光雷达的豪华插混SUV哪款好？全新混动XT5与领克08、腾势N9、理想L8、问界M7横评对比+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFBfNWdEckdDeE9zSHZVVTNjMnhfS2s1T1JpNEREZTRTM2pUTW1xRExEU0NYczRoSHZpY1BiN2tmMUxVNk94VDE5Y1AwQXhjZU5OV2ctc3I1VlVOR0R5cElyYWJoMWVrTE9vcmtTTExnV2NMUQ?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>XPeng</b> (294)</summary>

- 📰 2026-10-15 [15万预算四车对比，小鹏MONA L03和零跑C10谁更值？](https://news.google.com/rss/articles/CBMia0FVX3lxTE9xRVYzUkZBSHB3YXVqR0tZWjdtV28tODBaR1hKeXRjWmQ0LVloLWtTMlNGcHJQWkxGZzMxcGkta0hiRFJ5cUFzRERYQU9YaFBURWZRZDB2a1ZhYWhiaVdUY3diaXN4RFhFTkY4?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-15 [【视频】有路就好开！MONA L03&M03 智驾体验直接越级](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBkZFpVdWd2alNodkQ5bDlmdWN4UWZ6a0xDQmFlejZHUFkwU1VqWjgtQ1F3TzJ0bEk1MncxSTFULVdpY1FQdEJwM1BhcmY1d2JEZ21vNXAzZW5nSFk?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-14 [舱驾一体哪家强？小鹏G9L与智界R7、理想L6智能大五座横评+选购清单](https://news.google.com/rss/articles/CBMickFVX3lxTFA3Zi1VdG5SX1VlSTZkWW41OXRJTXloM1h4LU9wLVlQdXRJWnh4QnhHV0tudU9NZFd4aFl0bDRUX1ZnOTJiSU9MWllRZFBoUXY4Y0VDYm5NM3JFSHBJTTJ5SmFhZEY5N1Z4QXFKekNzSXZqQQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-14 [25万预算新能源SUV横评：小鹏G9L、理想L6、智界R7怎么选](https://news.google.com/rss/articles/CBMickFVX3lxTFAzVktpSW04dW5DaXVWUlhDU244TFBPSkZ4Z0ZvbGRKdXI3VDYyYnFEcEpfNkRiekE2WG1jNENaT2pRNnpXd19UXzQwS2puZ2JleFZtWExQdW13WE44ZjEtS2Q4TVVieVYwOWhpQ1BybUJ1Zw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-14 [25万预算新能源SUV怎么选：小鹏G9L对比四款热门大五座+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE9GaUxCdDY5YktXV1ZpWV9oTmdIYnNObHNHMXRyMTZ1Q1BIRUt1V0lRZ2llX09Tdy0tTlhUZk5CRHB2Zkp3ZHJ6allMWGw3bjZXcnNJTVdQVnplbUZ2UzlnTHZQTGo3WnQ5dENVNnp5dHVrUQ?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>Li Auto</b> (154)</summary>

- 📰 2026-10-14 [25万预算新能源SUV怎么选？小鹏G9L与理想L6、问界M6横评清单](https://news.google.com/rss/articles/CBMickFVX3lxTE82VlU1MkdMWkxDQjlEemxOLXVpWkdGRE5MX21xYzByejIwZDdJOUpvWHFkbjlqOFJpUklNdHg5RmVzUGJseHdBVU5ZQTc1Q1ZRbTBQVkU5XzJhdVp3cXZrWG5sbFd2OW4zZUJLNXB6VGVSQQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-14 [舱驾一体哪家强？小鹏G9L与智界R7、理想L6智能大五座横评+选购清单](https://news.google.com/rss/articles/CBMickFVX3lxTFA3Zi1VdG5SX1VlSTZkWW41OXRJTXloM1h4LU9wLVlQdXRJWnh4QnhHV0tudU9NZFd4aFl0bDRUX1ZnOTJiSU9MWllRZFBoUXY4Y0VDYm5NM3JFSHBJTTJ5SmFhZEY5N1Z4QXFKekNzSXZqQQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-14 [25万预算新能源SUV横评，小鹏G9L与理想L6、极氪7X怎么选](https://news.google.com/rss/articles/CBMickFVX3lxTE5mOTYycTZ1Z2RHUHM4US1yZ3U5NEFKUVpGYjEwa28zdmtXVTJIQ2t4NlZyenEzWURDOUszOU9zVXBJOHNWTS03Wk5DM2dRcjVUY2puaXFaRXJMamxsZERRTDkyWktTRi10NVBOcW8xMHN1QQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-14 [25万预算新能源SUV横评：小鹏G9L、理想L6、智界R7怎么选](https://news.google.com/rss/articles/CBMickFVX3lxTFAzVktpSW04dW5DaXVWUlhDU244TFBPSkZ4Z0ZvbGRKdXI3VDYyYnFEcEpfNkRiekE2WG1jNENaT2pRNnpXd19UXzQwS2puZ2JleFZtWExQdW13WE44ZjEtS2Q4TVVieVYwOWhpQ1BybUJ1Zw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-14 [2 Auto Equipment Providers to Buy as Technology Reshapes Industry](https://news.google.com/rss/articles/CBMivgFBVV95cUxQZXI3bk9ZOXcyZVR5VWFJV0d3S3NUaE1oUGE4UU1KaENLQWdELTdtc21ubTg3REhQWHlTWFJMVmZQNEltU2E1Q09ndE9ubjVKZlJ5WXM5N2FqV0VKMzUxckJIZWhFSHpZc2k0TW9ORDhveVNWT3lDNWJfd29oTTZ0UkR3YjVDOWE3dExGT2lLUzRxV1UyS2JzVWcwa29wVk01eDQzdjAtRnVPSlRzX3daaXBXd1l0N29uRURPZDFB?oc=5) <sub>TradingView</sub>

</details>

<details><summary><b>NIO</b> (141)</summary>

- 📰 2026-10-14 [麋鹿80km/h+大五座SUV底盘横评：小鹏G9L、极氪7X、智界R7、蔚来ES6怎么选+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE1qdERjNlB0dGROUmpVX2YwT2NQZFYwNG8zNE5lS3ZxUWU3WU1fd2pCMWtfNmNiSnJsbTV6cXcwUXl5MEY3SlNkSWkwYjA3ZG83aXZOZFhPWWF5RWxncU56WHFmRjZLcGkwcTR4TnNObjF3UQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-14 [双腔空悬+后轮转向：小鹏G9L与极氪7X、智界R7、蔚来ES6大五座SUV底盘横评+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFBpaFhBV0F4SkprZkt5eVRFbWtFNTJyd0h0VlBOQVROVEd6VWRsa2N1R3luRXJKa2ZnUTFBcFlvcjJpWG5iNUEwLW5JMWRrMHZFVUVuYXZtM3ZucGxzVWVlcWFCT254ZGM3TmZxenRXazhzUQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-14 [麋鹿80km/h+与5.4m转弯半径：小鹏G9L与极氪7X、智界R7、蔚来ES6底盘横评+怎么选](https://news.google.com/rss/articles/CBMickFVX3lxTE5aMnRaeUpCeXJkUGZjZHBQOVdIdS1RVXM5MVJTOHprV1ZMSlIwM2FfaU1lb1VkYkd0TDQxR181alY5T3hTZ2FVR1dOWUtLdVdVZjNhMVA4N19JQTh6Q01FYzF1QjhGYWdhalB4a25nTnh6Zw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-14 [全家舒适大五座横评：小鹏G9L、理想L6、问界M7与蔚来ES6对比清单](https://news.google.com/rss/articles/CBMickFVX3lxTFBMZW50VEtUbDRWdWg2REIxYnVHMWFQdy1INTdic3lZVTlPSVdoSEwzZTVXOFlabFNjdTNSRU53QlE4dXoxLXhPSEN2M0xRNlN0YU5OS2gwdVk1cGprWHVzcVNNUlJ4Zm9WenVlY0tTaVZCdw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-14 [Share by Nio bloggers](https://news.google.com/rss/articles/CBMigAFBVV95cUxPbG1KR09MU000dThMeGZEeThZTHhQcDdJU2FDOEZKaVI2YTNNV2hMNnNVNUdVOF94ek9YSFhxZC1PcDdHbWxpcHRxR0VLZFBQam9kb19hVjNvcExoUmd1QWRFakowd04zV01RSDdaRFdpVXBtYW00SHdyY3lYbXdDaQ?oc=5) <sub>Moomoo</sub>

</details>

<details><summary><b>Huawei</b> (374)</summary>

- 📰 2026-10-15 [Avatr launches 2026 Avatr 06 with Huawei ADS 5, trims lineup to 2 variants](https://news.google.com/rss/articles/CBMibkFVX3lxTE9fOENjb2R0dF9sVHBJZFB3ZXdTSExmYmZjUDJwSXJMaTYwVlAyV2JCVC1WNGJFenhnVEdJLTJmTlJJRXJrdXA0MEd1ZjJnSkRhTzh5Z1pKOXVwNFpVcUJTTkNQQVlsMXFhRlhjQXNB?oc=5) <sub>CnEVPost</sub>
- 📰 2026-10-15 [AITO M6 cumulative deliveries surpass 60,000 units](https://news.google.com/rss/articles/CBMirgFBVV95cUxQam5oZEZnQnBzNkk5V1NmSlQteXFHMS1ZN3M4R3BEZ0pyRUVZNmhib3Q0RnJPUV9HZEQyOVpWNDBfZHJkVHc2NmpnRWhiNmgzUDRmT0FXTzMyZnJGU014anZEVl96U1J2dllGeFM3dERlbkZkTm16UVhIV2Y5UDcxZkpjVE9MWDlXaXZDWlkzTl9ESXZYYU5LZnpXWDJaVU9Ob203U2s2ZFgyWXBZbXc?oc=5) <sub>Gasgoo</sub>
- 📰 2026-10-15 [【视频】华为乾崑智驾+阿里千问这台13.28万元起的中大型SUV太超值！](https://news.google.com/rss/articles/CBMia0FVX3lxTFBLSjBtQXRMWHVtV1kzSFZ0QVhMZGJRSHJXLVIxaGRKaGZVYWxXSnVFZno5ZEF0NlhiQWFkeXR2bldRLXNZdGZNbGtmWVNjOEdIOUpROVVpcGNPaHFzdEV2cUpZNjRtaTVpYmFr?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-15 [【视频】12.59万起！家用舒适拉满！全新旅行者7正式上市](https://news.google.com/rss/articles/CBMiW0FVX3lxTE0zc3JwOF9xcUxza1RwY1JJSFVwWHJFNHF4ZDV2d2FmNnhUYjBWS2ZkYWlFMWZVa3JybmtvamVQQjhJSU13Z3BXNlVGdlc2aWVBMEVVRnM2UWx1UlE?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-15 [【视频】华为乾崑ADS5安排上了？全能方盒子捷途旅行者7 12.59万起！](https://news.google.com/rss/articles/CBMiW0FVX3lxTFB4UDRaZ1hpZVo5bzBqSnVicUIwZmxNRXFEQWl1RmdnNll0bl91b0thTGhqT0pvZGZEUHUxYlliRmd1Z3ZhWWxHTTVmV2hSVmxfRFlrU3RDTkc0Z3M?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Baidu Apollo</b> (48)</summary>

- 📰 2026-10-13 [Waymo完成50亿美元首次债务融资，特斯拉Cybercab单日新增注册150辆，小鹏Robotaxi启用小鹏悠游](https://news.google.com/rss/articles/CBMiVEFVX3lxTE9JZFBKMTdRVUxUUHhQT2RzZ1EzTWtGS24zR3BfX20yNk5Uek42LXA1SWc4UEVEU3l5SXZoY0xJRVFlT2tycHgzWEZEZzhuY1gtZjRydQ?oc=5) <sub>虎嗅网</sub>
- 📰 2026-10-13 [小马智行杀入伦敦牵手Uber，中国Robotaxi出海怎么打？](https://news.google.com/rss/articles/CBMijwFBVV95cUxPQjd5cFFBdWZZNTN4Tkd2cmtrQVIxenFtTVJtT1ZzdTk3bldFWnNhRFlHVzJFSTYydnlKenpvQWdUY3hZeGZrcDZudl9tVEVTbnVZaExrb2g3LVpZZjlFd3RKeHg2bTN5a2UwWFk1clVRSjduSFpyTDdfMHB0SUhKVTRmOE9GalppMnJ3UXRoVQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-13 [【视频】骑了10年摩托第一次在路上被这样打招呼](https://news.google.com/rss/articles/CBMia0FVX3lxTE4tblJESDFLN1hsWHVRZmFHRUZjX0w3VHZzbEZCY1lPMGRRRlFXUmdVS2p1UC1VYXNUQ1VJdFF4UC1Lc0pKcjZhNlB3aHVGNTc1dDlYdUJQejYwc3ZhenhFd0JXMWpxUWpENXVJ?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-13 [Baidu opens free Tung Chung robotaxi trials](https://news.google.com/rss/articles/CBMie0FVX3lxTFBtaVl0RjQtXzRHY2dNNzNHZEEwaW9QQ3pFMTlrc0dIaVBqRUhubVRZdDI5ZXh0NnV2VDFKcU5KQ3BoNGdEUjdCNHBVWi1BN0hjOWhKVFZxT3NHRGhmckVwV1JqUUZQbG1XdG9JeXMzcjQwV2hBc2NMRkp5RQ?oc=5) <sub>Dimsum Daily</sub>
- 📰 2026-10-13 [深化智慧出行合作 韩泰iON携手萝卜快跑拓展十城自动驾驶版图](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBRSFp5M1hZZkM3Z21vS0xJWS1vOHkyM3pYMWJkMWNlSDBBcHc3aGpFT0x4T0RiSloxNDFlZFhIdHRzQjRmWU44UEtZMXlHM242OEdLTkZkR2k3S3c?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Pony.ai</b> (149)</summary>

- 📰 2026-10-15 [出海日报｜大睿生物向罗氏授权创新药，博力威与越南VinFast签署合作协议](https://news.google.com/rss/articles/CBMiWEFVX3lxTE9IWDgxZGFidXJqNW9idG50THBEVzNaV1p3ZTdtSXNOdmxOWC0yTEFzRF9VRTNEb080YlhRQjFMaUIwTDdpMXA0Q29oVHNHa0JBZUMzNXg1Mmc?oc=5) <sub>Jiemian.com</sub>
- 📰 2026-10-14 [Croatia trials full driverless robotaxi service](https://news.google.com/rss/articles/CBMiogFBVV95cUxOYXJtbDc3MEc2T3Vva1NnZmdMMlNQd0w0V0RPdm9lak0xeDJVbjhMQ0Zra0hLZWdaTElBdnpGM1g4VGZQWFNYUmNoX3RUWElIY3VJWnlobk5PdEd4R09tMFlZMGFfckJaSzlhZ1V4clFSclFOZE5NbmZzaGRyU1NhaW0wT1dzSUNzbUY1Z082dkJxSS1LVHVWX1A1M3h2UHJoRVE?oc=5) <sub>The Star</sub>
- 📰 2026-10-14 [Uber and Pony AI take robotaxis to Manchester](https://news.google.com/rss/articles/CBMigwFBVV95cUxPQTNhV29nNHNKYXhNTnV6QUNEaVVsdm5HSHctTHZsaU00aW9qWkl1Q0xvdlFQNHpYZ2o1SDc2MF9mUUFRYTh4aGloaGdlZWV5bGtoZ2hETDFrMVNyeHdtXzFSSkNMZTlEVkZiTmJIcjNVLVY4VVF1anBKLXQ3dDVUeDhtTQ?oc=5) <sub>Zag Daily</sub>
- 📰 2026-10-14 [Pony.ai Lands Second UK City in Under a Week as Seventh-Gen Robotaxi Debuts in Manchester](https://news.google.com/rss/articles/CBMidkFVX3lxTE9OSy14RFNzemcybENwXzhMRUdWSklReHA5bFQ0WXQ3NGFNemZFZ1ZpUVR5WGFpVnIwNE40MktLblJiSFdEY1VaVHBYdUg5Nzl2dHhERmJqYkdXOVB0eUFoOFowNml0TWdFc2tIenQ4ZkotSTBOSmc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-14 [Gasgoo Daily:Chery Selects Bosch ADAS Technology for Six New Models in Europe; Pony.ai Expands Robotaxi Operations to Manchester; XPENG Opens Intelligent Vehicle Solutions Business to Global Partners](https://news.google.com/rss/articles/CBMi8wJBVV95cUxOQmpKdlhBR0o4cndXS0pVSHd4NUFTSFNMYkRGU2RxY05uUFNpRFpTUE5yRTVmQW5WaXlUcDRBU0ZRRm1NWEFOYnpqLU94Mm9DNC1ZQjZsNU1zbmJKRXFOVklrcVRJZnBxOEZZWGlEbkZ5TkhlQnZxR1VQZHhseExobkNFRGtuYzB4NXBvRUhyMmRDZFVzeW1PQlA5Ujg4UEdPd3NpcW9WVFpOX21HakVDb2VZYnR6RTgwLWR6N1JndDAyN2tUTzJCeE5hQ3hxQTdTZWVIcmtGVHVSbnZfWGlxcUhHLVNBT2VFY3ZGUXBJV0ZhV3VJdGU3ZElaWmd4WkxKcEEzUUdWcDZqT01uQVZsQUhPR09yQ1JnSnkxUTI1MC1BVU9haW9sZWhpTTdXLWZJMVkxTGZ2a1FoS2ZrYkt3eVFLSVFaS0NkU2lpVkVQOGNTVFJHSG1BWkw0ckJpOC1rOFRndmdOSmtDbGM5ZENreDZOaw?oc=5) <sub>Gasgoo</sub>

</details>

<details><summary><b>WeRide</b> (141)</summary>

- 📰 2026-10-15 [文远知行-W盘中跌超6%](https://news.google.com/rss/articles/CBMiXEFVX3lxTE1HVC1BV01sNURBTTY2RVd2SVI3WU5mMzVXbHlwaW9hNlBTU00wSkhvdWE0VjBZbmJ5M2lwc3NldmstVlpTcUVZdXZZVWdCdUNDUEF6cWdWNW13aUlj?oc=5) <sub>www.caiwennews.com</sub>
- 📰 2026-10-14 [医疗健康产业日报(10.13) : 行业动态](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNODRVRlFCaVlxMGxlcEN3Vi0xRVdVVGcyb01Wb1YwbkVwX3lkbEFVZ0xHSTBqMUlvZEJ4QXRtTW1wcEhUTms5SklpWmdJTDBpNTMwcnh5M0ZMRWw4dkpublVCNHlTRHRwcmw3Q1VEclBMTG1UZ1Vfak96VTlxUTNDZmVCaGozQzI5?oc=5) <sub>搜狐</sub>
- 📰 2026-10-14 [港股10月14日午盘恒科指涨1.61% AI概念股多数调整](https://news.google.com/rss/articles/CBMiYkFVX3lxTE56ZXE2UHE0bGxiazYzQUYyUTB6SWxwVG1HV01ub0xqRzJ1U0dhZURLcjZhMjVSZldjeUJhQlpNM1ByTjR3aWlfU25ZV0ZZOTRyZVdaeWdRWUhBNnozOWNydjV3?oc=5) <sub>观点网</sub>
- 📰 2026-10-14 [10 月 14 日隔夜要闻：美股收跌 苹果智能家居亮相 OpenAI 办公室被植入精密录音设备](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE0wRUpvWWNYRlVCTTdTb3pGVWZQWjU3cjB4U1FERXlRSVVUUWN6VEFfRXNBZ3BuRFFfajlOWTdVb0M5NVIySXJ5X3hEZDRLLWttYnJBdTN5Z2JZbXg4ZmJJa0FBa25nTTA?oc=5) <sub>ZAKER新闻</sub>
- 📰 2026-10-14 [10月14日港股软件服务行业沽空数据盘点，腾讯控股、网易、智谱沽空金额位居行业前三-证券之星](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1TUU0zTzdJdlZkaGo2eU1KNVJlOENZMkpnVDRvdDJHWGpSOUJ3WXdxbmtrWVBVek1TS21VVlRGenR5andlV2Fsbm5ZY3o4SzBQMzFaYnkzNGZRUk5MSEE?oc=5) <sub>证券之星</sub>

</details>

<details><summary><b>Horizon Robotics</b> (173)</summary>

- 📰 2026-10-15 [捷途旅行者7上市，限时12.59万元起！](https://news.google.com/rss/articles/CBMia0FVX3lxTE9Bck5mWVZWcjhOd2hBRy1UT3N6ZWdNNFhWSGdfNGFhQUlyaWwxVGVmcGJlWm1VUjVoanlOVTBuT2ZGMHVWaHF3b2Y3ek9ZQTRlMmgzVHVqU1BzejNOYjE1M24teC1MUHdLa1Bz?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-14 [China new models September 2026: Hongqi G919, VW ID.AURA T6 and Hyundai Ioniq V arrive](https://news.google.com/rss/articles/CBMiwwFBVV95cUxQT085WTFGX1dRMkpRSFViX2tkNnFNa1BGenJ0RVdiTXFGN0JlNU9LMU9QOXpNcmUtanVxaFUwaEtyb3AtLTVOMGRsdm9KX2YxdTBtLUMydlktVnFnVzJTcENqaHZJanpMbGF6alB0THFibmxaLTdEcDNuSjQ0SGFZM09aMWwyX0l1dklXVEJBWjBEUGplY1Z3bDVtMjRwQ3lPYUtYMTJZZFp6aEpEdmptTUNuWWMyc2dZLWMtQ2d1dUhrWkU?oc=5) <sub>Best Selling Cars Blog</sub>
- 📰 2026-10-14 [12.59万起，捷途旅行者7把华为乾崑、宁德大电池和XWD塞进方盒子](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5ITXVoaHVoTVFybVlmYy1iaW9NTzNmc0h0VmkwTTdKcGtZMnl0Zk9ydTBxb0I0bVZjQnVSUzZmelFlMWd5UC1xejZGRnRPUWJMUUVRNzdWR09jSkU?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-14 [地平线HSD V2.1将首发全场景倒车，循迹倒车120米已是行业上限](https://news.google.com/rss/articles/CBMiXkFVX3lxTE5OZVp0dktpdlN2dVVKZzFkY0F3NXMzUTYxaHJXV0lZNXlkZWdQOUdzc2FfcUVJYkFsZDRUaE5FTThpSGcwREwweFJmMW1PeDRRSFJjdEdOLWZGTTVYcUE?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-14 [【视频】星途ET5：猎鹰700智驾+ 长续航增程，新奢中型家用SUV](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5SLXVBVWRWNXBCcEdWakhsT3BEWHBrb3BEa1JUSEl0Zkh4aFN6VzRZbGVyNTAxMWJJX0ZnVTlxWU8tNnU1UC1CVHo5NUg1elpYY2F2T3RDVTR2Mk0?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (31)</summary>

- 📰 2026-10-15 [数据驱动的具身智能：迈向规模化之路｜QCon 上海](https://news.google.com/rss/articles/CBMiXkFVX3lxTE5qSDE3dmxBTFE3LTdLZ0lyV05Sc0VsQm02bEp1bWJBZ1pXRFVwUG5uWTAwdG05WWNnT3d2N0JzS1NBa3QtWmJCb3JOeUU1czZ0bmZwQU96Vi1FZk9hNEE?oc=5) <sub>InfoQ-CN</sub>
- 📰 2026-10-14 [赛豆科技AIVA第二款SUV或将采用换电方案](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5WSE1zeWlTbjE1UFVyQ2tveGFfS2lhU0FoVFVHR1J2NHhUbUY0U3RUai03SVV6UlREQkM2dENhRk5WaTZGM1lxRjhNakJYY2xFLXZ0Z1JBQWFSLUE?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-14 [TomTom & DeepRoute.ai Sign MoU for Automated Driving Solutions](https://news.google.com/rss/articles/CBMimgFBVV95cUxPN2FUMHRsQU5FRHkzd1NTbmJxTWNkcmhVSmJIQVNibXJBMXlPSmtxc3ZLY2kzb2JtUmxOdllRcWs1WXZCQUp2LTJVMTRScWVPTmRpek1xLWVXYTEwZDN5ZnVXOEZmMm4tbC1ULWRXMng5SnVwTjQwajI4X0x6TW54dVlvY1gtSE9kc29Ca0xrS0FLNEliQlFHcGpR?oc=5) <sub>Future Transport-News</sub>
- 📰 2026-10-14 [How TomTom and DeepRoute.AI Are Advancing AI-Based Driving](https://news.google.com/rss/articles/CBMikgFBVV95cUxPTlNCVERPY0U4ajVoMEVtUF9UenVjcEZZMG1xM0J4QWdvVWtqUFBWQlI0X3RPeExKYmhxOFhwa3dObHRudHBfSEsxNXNJMWhkSlhxUmN6bHhtQUI4NDBTeFplZFlZV0dnLWVYbnR3V3dsM19Hc2VSN21EaG9GbnJIT2c2T3ZrZ1FwZzhveVNjN0hTZw?oc=5) <sub>AI Magazine</sub>
- 📰 2026-10-14 [赛豆汽车,6月9日正式发布！](https://news.google.com/rss/articles/CBMiW0FVX3lxTFA5YVptZWJLMVZHVjJYZmN0MFVBd3NRSFpuRUk4TDNEa0Vnc3pGZnQ3Q0sxY2ZvenBmUzVFM0NGTTBHWXZCRVpqbE4xZjBxU0hfNlVEa2ZzMS1LczA?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Mobileye</b> (12)</summary>

- 📰 2026-10-14 [2 Auto Equipment Providers to Buy as Technology Reshapes Industry](https://news.google.com/rss/articles/CBMivgFBVV95cUxQZXI3bk9ZOXcyZVR5VWFJV0d3S3NUaE1oUGE4UU1KaENLQWdELTdtc21ubTg3REhQWHlTWFJMVmZQNEltU2E1Q09ndE9ubjVKZlJ5WXM5N2FqV0VKMzUxckJIZWhFSHpZc2k0TW9ORDhveVNWT3lDNWJfd29oTTZ0UkR3YjVDOWE3dExGT2lLUzRxV1UyS2JzVWcwa29wVk01eDQzdjAtRnVPSlRzX3daaXBXd1l0N29uRURPZDFB?oc=5) <sub>TradingView</sub>
- 📰 2026-10-14 [Shashua: Israel must invest in AI infrastructure to compete](https://news.google.com/rss/articles/CBMipwFBVV95cUxNOHFQMmpVTDlEQXZESFFEWUpzS1NsNWJhUHJFU3hBejFYeGxXR2ZyR1V2RVVZZ0NsOVZvUjliTGRldzYyaHBpS2RqYVhnTndkNXhqQnAtZFFWN3hJUlYxN05weXpWbEtyWHRraXJ4Q3ZUbDBMNU9CU1FuM2ozalgzSzRvUTU5MDMtWkhNcUxSeWI0OWdfU2VmaENoNXRlVUliZWVzZXF3MA?oc=5) <sub>Globes - Israel Business News</sub>
- 📰 2026-10-13 [INIT enters autonomous fleet management market](https://news.google.com/rss/articles/CBMijAFBVV95cUxPRW92TDM0SHlYNWFaMlJhMVlqUUVLN21oak9rSzRBX2hVTVdFNG4wdnBrMElCTmY4OGhXaGtTaWVZZ2JURkdYLTVLRkpmWHg3VmlncUlHMDZla05MdkRzdmxCeHB5RGNoSEhvX2RzMEtVT2pNaTVGMjBIZ2p4VFlJTHMtMVczdWFvSkdsTw?oc=5) <sub>electrive.com</sub>
- 📰 2026-10-13 [Mobileye Announces Timing of its Third Quarter 2026 Results](https://news.google.com/rss/articles/CBMitwFBVV95cUxQc2dBRE5uWEtaSE5fRXRuTEdtTTVwamoxQVBSNlJMVTlxbm9aZFV3Q0RkSTdkcXpBQkt0dnVNRmRULXFPUEpoNlo3NTB5WEd3RldGMWdYWWpLVVFVaW1nRFFUWlhvSWp2ODF3WUtnekNuNzBXeG85VDM5eWY1U0taamZjcGFTbkw3Mjdsbm9pR1g0NGFGMC1LX3BrQWQtemJMbVl4NFhtSzlScGZHTS1EV01zQW1NRGs?oc=5) <sub>Business Wire</sub>
- 📰 2026-10-07 [Uber invests in robotaxi provider Verne](https://news.google.com/rss/articles/CBMigwFBVV95cUxQQkxEa25xSjBNT0ZJMzZINk54a2txS3k0S0pvTU4wZEJ5eVhHY0FNRWlyaVdIcVhYdmlPQl9HVUsyUnlkcW1UVzRVc180dHNCT1hXV3ZUcms3Mzg5aUoyZENTUWU3VHJtRlFuQmp0dWpQRDlmU2xlSDQ1MnlEZW11YmFGWQ?oc=5) <sub>electrive.com</sub>

</details>

<details><summary><b>Aurora</b> (66)</summary>

- 📰 2026-10-14 [Autonomous Trucking Advances on Costs, Freight Operations and Federal Rules](https://news.google.com/rss/articles/CBMia0FVX3lxTE13ak1NNlJKWHNVTmFwd0FXbVEydXQ1ZENkc0tyVWVIT0pIOUlOVkJ4WXBYLWNRR3ExSmpHNjVkdFJuQVFLV0g0V0dMcHBpYlR6Y0Y3b0xrT25IV2lNenJ1dGt3dXNhdkIxUHRV?oc=5) <sub>Advanced Clean Tech (ACT) News</sub>
- 📰 2026-10-14 [Driverless Truck Beacons: Tanker Access, Hazmat Limits](https://news.google.com/rss/articles/CBMia0FVX3lxTE1jYUxvVlVFNHdFUTlyYWRZbFNkZmt6NS03ZzQyS2JBUjR0bDdqNG1aR1BnZHhjZWpPWWZCZ25VM2Y3VFI0bmZjMklSMDJzMjRnOG4yRVBrU2swWWUtWHBWT2hFSm9sUTd2LUdr?oc=5) <sub>Tank Transport</sub>
- 📰 2026-10-14 [Charger Logistics inks deal with Kodiak for autonomous hauls](https://news.google.com/rss/articles/CBMiwAFBVV95cUxPSW1EOTFJTkZnWDJveV9DZ0Z2WGNRbHpDUWQweHJOcG9GdERiMmFCQ1Bhb1VEcmFWLUZVZWdwMUR5MjN6MDJyRHVpZjhQZDJQbXRneEJ5TGFlb3lNZW94blQyaXpxa1RGbVlSTE14ZklsdUQ2X3dZUDVUMUVhYXJvby1LRG5YYmhpaVRaOGR1ZW9maWJNdHdmbExpb0NuUU4xc1ptQnBJZzB4Zm1XZkRCdlhSdDViaDdLTmJrU1huNk8?oc=5) <sub>Commercial Carrier Journal</sub>
- 📰 2026-10-14 [Expect to see more driverless trucks in 2027](https://news.google.com/rss/articles/CBMid0FVX3lxTE5IVTM4Wm1uQ05KVDZxNVYtSm81RFk3Q2lOZVljM19wbkt1UDdjNFY1VVVRalViREI5VVg1QjRDX2k0anN5eWFXOFhuYmxfMi1VNWJBU3ByLVY1dnQyaWN6a0FSTG1hREdVa29rcHc3Um93NWtrOWNB?oc=5) <sub>Land Line Media</sub>
- 📰 2026-10-14 [Volvo Says Driverless Trucks Are Coming to Texas in 2027](https://news.google.com/rss/articles/CBMiiAFBVV95cUxQUE9XN0ZpRHZXRkRRLUtfTzFfSy1tUHRwSF9NVWtkYjJOajVuUThZcFFzd2N5NjNkeHM5YUF4TWhlUzJ6Yk5PeEdKR28wVlZOWnplUVhQQWs3T0VNbjhBbjRSdlFrNkFTVy1pdGFSdDBiX0NPQzVIeHVFUkdHS1JYb2pkdFRNcTVC?oc=5) <sub>Autoweek</sub>

</details>

<details><summary><b>Zoox</b> (70)</summary>

- 📰 2026-10-15 [Tesla Robotaxi Tally Hits 739, Trails Waymo’s 1,185 [2026]](https://news.google.com/rss/articles/CBMid0FVX3lxTE5DeGxZSWQyTzdKUHBkUnFqV2Z2ODFsc2JwSHNxZ1psUGE5WHNNbmpWTzhYUlVSWkozRFM2aUZPTDl4SkpUdW1Ubm5LeWxULXRXY1cwdVRlTjRjWHdnRWhEQ3kzTVRvOXYwcmpFLXBnUlVmYlNMNnJR?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-10-15 [Tesla Cybercab Hits 300+ in Austin: Inside the Hardware [2026]](https://news.google.com/rss/articles/CBMic0FVX3lxTFBSalF5NS11ckNDZDVpQ1hpTDlERTR4dWhRUVVJckZOb1dtTnRVMWtRQ0hSbU8xZDNvR2J0WV96TmFpX0p1QXFlSXBEMG12LVNDbkNHelBDTThPNFRRajQxYWZMWDlUZUNfQU1UeWpPV0VFRjQ?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-10-14 [What Is Zoox?](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1tcFFURGhVdTg2OC1oeS1sTmJhRmFyRmNJMkFKQjkyYktGUXA5Tl80aFBYMW9veF9tTUV2NUVuSGhYQVBhZXdKS1JWOFM4OU5Jb3Zr?oc=5) <sub>Built In</sub>
- 📰 2026-10-14 [Geely Monjaro EM-i on Track with Yann Ehrlacher](https://news.google.com/rss/articles/CBMioAFBVV95cUxQX0VuZGI5aG5WbnNIWm5kck5Ea3RvZDFUTnJRMld4S2R5S3N2X1VPUzlBNDdRRHBMVW5DZWI3NFJ1V2dHb183N3hwcVlYSEd0MTVXTk9WV1h2LVQyMThXN1FPTVVpUW9pcXg2T0xMNDRLckJDUEMtYkJQMkNHaWN4WUZxUlE4N3FFVDA3VVVuLXlGUk4xWWoyY2xUSlJ6aU0w?oc=5) <sub>eletric-vehicles.com</sub>
- 📰 2026-10-14 [BYD Han — Westward Road Trip Along the Yellow River](https://news.google.com/rss/articles/CBMioAFBVV95cUxQTWd2N0NUWFJzNHU1aFozb1lUZWdSTUt4R3Z0YWgtbU51UkdZREp4ODI1NFJuZFR6YjhFTHNwZmlIMFg2eW9PdHhFNl81QlJocE1HWkh4ZUFxYXQxSW1ZNlI1b0h6RGU0cVh3OXZBNVVWbTV3M3QweXlURTFaRUl4NnBCUXVHb1dGOERJeU1pU0xHQ3ktaklOOFRiWkVpd25F?oc=5) <sub>Electric Vehicles</sub>

</details>

<details><summary><b>Motional</b> (49)</summary>

- 📰 2026-10-14 [Hyundai’s two robotaxi plans take different routes](https://news.google.com/rss/articles/CBMikAFBVV95cUxQNWdFN1RBOWctNVVIZmRxemEzVEhrQ2MzVkN6YkJWME81bW41bFFqQVVDLTl4SEQ3OTYwalRQaFo0Q0xwaVR4M3FYOUZpMUV3OEJSTDktdHY4enVEdDgzY0xuV3lSa3hCTTAwdE93bkhoS2M5aHdxcmVkbEJIM1QteTlVbjhfTk9UUVBraW9GX2TSAZABQVVfeXFMUDVnRTdUQTlnLTVVSGZkcXphM1RIa0NjM1ZDemJCVjBPNW1uNWxRakFVQy05eEhENzk2MGpUUGhaNENMcGlUeDNxWDlGaTFFdzhCUkw5LXR2OHp1RHQ4M2NMbld5Umt4Qk0wMHRPd25IaEtjOWh3cXJlZGxCSDNULXk5VW44X05PVFFQa2lvRl9k?oc=5) <sub>ABC27</sub>
- 📰 2026-10-13 [Hyundai Motor Group chief marks 6 years at helm with physical AI ambitions](https://news.google.com/rss/articles/CBMi0AFBVV95cUxOY2g0R29NX1hSa0ZuUzJveFVZYUQ1YzVVNEItNnRkUjY0TnRHNi1fY1ppaVc2YmotOEt3YXhCeWxLNVN1NGQ2c2hGNVJYclBocEhKcDgzNjMtdjFPeGJ1bWJjTFR0UGgtUzNwdWZqQkQzaHB5U3k3bXpPcDQ2S05KUzktWkJWN21WSjItamJ6eV84clptQzRHV25xYXFyNURmamNLWGkxeFVNUDFCeWs2cTJta25zcE54WGFYcEE5T1YyaVQtMEh5ZTZvUTNUUlUz0gHQAUFVX3lxTE5jaDRHb01fWFJrRm5TMm94VVlhRDVjNVU0Qi02dGRSNjROdEc2LV9jWmlpVzZiai04S3dheEJ5bEs1U3U0ZDZzaEY1UlhyUGhwSEpwODM2My12MU94YnVtYmNMVHRQaC1TM3B1ZmpCRDNocHlTeTdtek9wNDZLTkpTOS1aQlY3bVZKMi1qYnp5XzhyWm1DNEdXbnFhcXI1RGZqY0tYaTF4VU1QMUJ5azZxMm1rbnNwTnhYYVhwQTlPVjJpVC0wSHllNm9RM1RSVTM?oc=5) <sub>The Korea Times</sub>
- 📰 2026-10-11 [Six Years into Euisun Chung's Tenure... Hyundai Motor Group Moves Beyond the 'Global Big Three' Toward Physical AI](https://news.google.com/rss/articles/CBMiZEFVX3lxTE1qSWl5SS12dk8yVXMwandrR090TkZkdzZDaFladGpmOGNZZDNrMGxBQV9zSkV5TXpVeXIzWGhKd0FVYUQ0ZFdsT1pEWGxZNDV1UC14N0FsZmxVd0ZFOUVkamhoMWg?oc=5) <sub>아시아경제</sub>
- 📰 2026-10-10 [Waymo's $5 Billion First-Ever Debt Raise Signals a Robotaxi Land Grab, Not a Science Project](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9BaGt6ckszSmpwTDVsOGUzQ29DXy0yc3BsVFdSTjNtZFZrR3dWYUd5TzcwSTYzUTE3MlVmd3B4UG1iSS1kRHpySXpFVlhRTWd3cjVCOUgwVW5FcWc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-10 [Waymo Goes to Wall Street｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTFA2Z3RvWEJLVEtPTDJWNVcyaGQweFBVUnZFb0RST0wxRWhCdUJudXJQeU9helBuODZrTlBDZlh4NF9zb3dyNjRxQ3BzTGpZLWJvQzNObmFlYjl1R010Z3hB?oc=5) <sub>finance.biggo.com</sub>

</details>

<details><summary><b>comma.ai</b> (4)</summary>

- 📰 2026-10-07 [Researchers Find that AI Models Struggle With Even The Most Basic Driving Skills](https://news.google.com/rss/articles/CBMiuwFBVV95cUxNb2ZGRGxGZDNjLWU1OVBPNjUtUlJXR0hiVGV3WEJ1eUVnSWExMWVvRmJjX2NtQm9sX0plMTU3YzZwUm5ZTzVoSGttcXZmQ3BqbW40X2doNFMycUk4UWE3anlidy1vWHNYZndVZjZWLUYtbnlHeVBFRjJOaTF4SWxzbmotR0xsNkVIcEhfZ0M3LUs5R2FyV1lVdlRRU3JwakpQcXpBUzlEOEhsWlB3Q19EdXFhQjRvZDU5MHln?oc=5) <sub>Auto Spies</sub>
- 📰 2026-10-07 [OpenAI's GPT-6 Astra is the only AI model to finish a real-world driving test in a Toyota Corolla](https://news.google.com/rss/articles/CBMifEFVX3lxTE9iZmN2ZFp6blVBRnZUTkYtYTJ3b0hSb0xhQjZyQXh5MUN2T3ladUlEb1F1SWJzc3FtamZtazk4LTVUWVpNX0ZjbGZwMnpERk45TVVQWVA1RjBZVUxxTTAzTWpaV1JqUzIwM1I2Wk1tTzc3bDJpaWluc2JVam4?oc=5) <sub>Crypto Briefing</sub>
- 📰 2026-10-06 [AI Agents Tried to Drive a Corolla, Crashing on 8 of 11 Runs](https://news.google.com/rss/articles/CBMiuAFBVV95cUxONWxQTEZham1kc1J4S2lMNUh6OTN1QWhXbl92U21NUWZTZWhNUUdwcFVvUHYtVWJzSjl4TjlCeFhUY2ppMXd3WkkxaHJFRmFlNUN2NGFSSENnV2ZZYWRNZ3JIUjd0dzFlTS0wR3gtbmxXN3VHOUkxWWg2VVFpTVgzWGN2T3RPdEFJV0cyWjRPSVFyNWZTYjFyX0pzYjFEUWQwLUlfbGo1bm8xVUZXQmpyQ3pCNXV5ZE9x?oc=5) <sub>thetruthaboutcars.com</sub>
- 📰 2026-10-05 [Researchers Discover ChatGPT Can Drive a Car. Grok, on the Other Hand…](https://news.google.com/rss/articles/CBMikgFBVV95cUxNNnNwX0g5bHV4STJlMXNOcXRnYnBHWHNoelViM2pJSzFob3dvUVJIdFlDRDV4X09DSVloZmxCTk5NODd3b3RBR2JmWEJQRktXUTYyWDNveS15UEw0NnVfSFluMlJxZHlBb3NhYnRNdDJsZ01MbVNpOXY4OW9nQnBSYnFRQ1U2YVd3a3R2ZTY4VlJNdw?oc=5) <sub>The Drive</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
