# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-10-14 · 1,278 papers tracked · 39 curated.

**Selection rule.** A paper is listed only if it (1) is primarily about autonomous driving,
(2) has public code, and (3) shows at least one strong signal: accepted at a top venue
(CVPR / ICCV / ECCV / NeurIPS / ICLR / ICML / CoRL / RSS / TPAMI, or ICRA / IROS / AAAI / RA-L),
≥200 GitHub stars, ≥3 citations / month, or a well-known lab with traction. Papers are then ranked by a
composite score (venue, stars, citation velocity, LLM rubric for novelty / rigor / impact, SOTA claims)
with a per-topic cap. See [`scripts/rank.py`](scripts/rank.py).

📅 [Daily digests](daily/) · 🗓️ [Weekly digests](weekly/) · 📦 [Raw data](data/)

## Contents

- [VLA / VLM for Driving](#vla--vlm-for-driving) (7)
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
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 16 | [⭐ 346](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
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
| [123D: Unifying Multi-Modal Autonomous Driving Data at Scale](https://arxiv.org/abs/2605.08084)<br><sub>Daniel Dauner, Valentin Charraut, Bastian Berle et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 401](https://github.com/kesai-labs/py123d) | The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics |

## Safety, Robustness & Evaluation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [CCFM: Collision-Constrained Flow Matching for Safety-Critical Scenario Generation](https://arxiv.org/abs/2607.04451)<br><sub>Ke Li, Kaidi Liang, Yuxin Ding et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 3](https://github.com/KELISBU/CCFM) | Evaluation of autonomous vehicle (AV) planners in safety-critical closed-loop simulation is essential for real-world deployment |
| [Lipschitz Optimization for Formal Verification of Homographies](https://arxiv.org/abs/2605.23203)<br><sub>Jean-Guillaume Durand, Panagiotis Kouvaros, Maxime Gariel et al.</sub> | CVPR 2026<br>2026-05 | [⭐ 2](https://github.com/jeangud/homography-verification) | The adoption of vision neural networks in regulated industries requires formal robustness guarantees, especially in safety-critical domains such as healthcare, autonomous vehicles, and aerospace |
| [CADET: A Modular Platform for Evaluating Distributed Cooperative Autonomy in Connected Autonomous Vehicles](https://arxiv.org/abs/2606.04072)<br><sub>Pragya Sharma, Brian Wang, Mani Srivastava</sub> | ICRA 2026<br>2026-06<br>📑 1 | [⭐ 0](https://github.com/nesl/cadet) | Deep learning models are increasingly central to autonomous vehicle (AV) pipelines, yet their integration has traditionally followed a monolithic design where perception, planning, and control execute on a single onboard… |

## 🏢 Industry Tracker

Latest 14 days of news, official blog posts and new open-source repos from tracked companies. Full daily feed in [`daily/`](daily/).

<details><summary><b>Waymo</b> (210)</summary>

- 📝 2026-10-08 [Sober Drivers Still Face Nearly 4x Nighttime Risk: Why Road Safety Demands a Safe System Approach](https://waymo.com/blog/2026/10/sober-driving-benchmarks) <sub>official blog</sub>
- 📝 2026-10-08 [Waymo Closes $5 Billion Debt Financing to Accelerate Business Expansion](https://waymo.com/blog/2026/10/waymo-closes-5-billion-debt-financing) <sub>official blog</sub>
- 📰 2026-10-14 [Portland weighs new rules for driverless cars as Waymo plans Rose City fleet](https://news.google.com/rss/articles/CBMipAFBVV95cUxOcmZldWMxQ05CcTNZSUtXZ0ZaVmlPTFdsTGZwMlJEU2ZVVDlxQVdHYlpBWGF1RnNjUURHN0hBOWZjQUcxSUo3WFlURnkyYmNyMzNZaVZxM2ZoNHIwZmp1eDdnWjZUSml5R3NDNF9CN1JjMDFHaXlBME9naHlwdlAzV3l1bXFNbmpQQUx0TEQ1TFpMbk5BVlpldG1CVE9abmp0Z0RXYg?oc=5) <sub>KPTV</sub>
- 📰 2026-10-14 [Tesla Robotaxi Fleet in Austin Soars 8x in a Month [2026]](https://news.google.com/rss/articles/CBMid0FVX3lxTE5rTFJuUnZQa0NUWmJkMVdGQllOMWFvcTh2WkI0NGxKWVZYWnB5Y2VUOUE4N2ptN21Pb0gxVDFzWGZ1M0lvWEtJUHc3aTZNMTNpUkJBejFBMVJIemJrenJ6bFMxQmlkNkt0cFFhNVpselhKc0o5LWJz?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-10-14 [Waymo begins service at Nashville International Airport](https://news.google.com/rss/articles/CBMinwFBVV95cUxQZlVnQUktMFpXZzdYX2E2V0xSVDNZdXd3VkZ3bTBrejNSdUlBdFdPbkFQSk45dnlGSTNoOTFvb1dHTmxLYUlmWll3Z29CbWtuQjZCTE10Uk4xTUk1VHc2LXoyaExJV0F6VTJkaG9OVmpYYkZJb1JFUGRpd2RRT2lnang5M3IzZ1QwMlRhV1lRTnNyVlA0d0hNRUF3MlJmaTQ?oc=5) <sub>Airline Routes & Ground Services</sub>

</details>

<details><summary><b>Tesla</b> (340)</summary>

- 📰 2026-10-14 [My Tesla robotaxi was stuck on fart mode](https://news.google.com/rss/articles/CBMid0FVX3lxTE1wZmFQS3NjQ1BEVWNDVTZ6X2Z4ZmdKV1Q2Mm1JUklHSzFMMDRGWGRNWjI3Tmc0M2s4YjI0QUI5WGhtMk5DaW9jS3hWUGM2M18yeGJWN0Q0MHlfdklhWEtQdm1uQ3g4U0FUWUxScG1SX1N5cmR4ekhV?oc=5) <sub>The San Francisco Standard</sub>
- 📰 2026-10-14 [Tesla Robotaxi Fart Mode Glitch: What Happened [2026]](https://news.google.com/rss/articles/CBMib0FVX3lxTFA0Q0JqQkJtQW44Mm8wREl5NDk4MDNfUUU5d0lfZFpFbXE3bUlxeXU0Z3ljSEpqbnVDd1dHWVI0YzJablotMW9wTmlzQ2xhNlVwbHVFRFJCRnZyQ3pPRXI2N3RKY09ERDl1Y2lTVy1jaw?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-10-14 [Tesla has been forced to rename Full Self-Driving in Europe after it was labeled 'misleading'](https://news.google.com/rss/articles/CBMijgFBVV95cUxQeURUcEJTMWw1aHpQS01Hb3d3RnMxMFJzZjVaZVEtTDBmT01yLXhUbEpERnp5MkR2YWh6TjZGVEYzQnE3eVFnMWNxS1ZKRFNWMm5wbDJoelRSWWFzYWZFTVVybWgzVTloODRrVWVfZHVFaElYa2t0Wndnd3dsWUgzN2hCbWVnb05ZdklOWl93?oc=5) <sub>Supercar Blondie</sub>
- 📰 2026-10-14 [Tesla Robotaxi Fleet in Austin Soars 8x in a Month [2026]](https://news.google.com/rss/articles/CBMid0FVX3lxTE5rTFJuUnZQa0NUWmJkMVdGQllOMWFvcTh2WkI0NGxKWVZYWnB5Y2VUOUE4N2ptN21Pb0gxVDFzWGZ1M0lvWEtJUHc3aTZNMTNpUkJBejFBMVJIemJrenJ6bFMxQmlkNkt0cFFhNVpselhKc0o5LWJz?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-10-14 [Tesla Rival XPeng Says It Can Adapt Driver-Assist Tech for Europe in Just 2 Weeks as Elon Musk's TSLA Faces Fresh Regulatory Pushback Over FSD](https://news.google.com/rss/articles/CBMilwFBVV95cUxOcHU3NmNNRWxwdWlab1djeW9ZYkZZRWotSmNJbE1DSVdXTHkxdEs3MmRCbGhpTlhJeWNIWHJac2lLNUppRDludHpZc3Y4cEFhX0UtVENvNURtX21DR1VZalBCb0p6RWpWZzNtTDJtNV9SOGlkQlpNRHhPdnl1U3oxNUVWUFo5SXNnQk5CdFF5dXlaczF5Qldz?oc=5) <sub>Yahoo Finance</sub>

</details>

<details><summary><b>NVIDIA</b> (212)</summary>

- 📰 2026-10-14 [European Cities Deploy NVIDIA-Powered AI Agents to Run Smarter Urban Operations](https://news.google.com/rss/articles/CBMiekFVX3lxTE5mU01rUUJVYmZVeVFELWp3azNXc2xOTGF2cGg4clFwSlpyTmhLRmdFV0ZhcU5kOE5fWlBEbEx0WDhYOTdtQWp6VnFZT0FPUmNJVjFoX2p2b2pFZEZQUEs1SXQtdlBUaThzeDFjNkJ1bWQtOVgtTzRUU0hR?oc=5) <sub>NVIDIA Blog</sub>
- 📰 2026-10-14 [Nvidia will invest $10B in Europe’s tech ecosystem](https://news.google.com/rss/articles/CBMie0FVX3lxTE42Z2d0UFJPM2pJQjVZTHJyVGRhekc0eVFiTmFVQ3JmVTluNVdGV19LR3FBeTRxS21zaEpXNjBfelF3RTlYZDN4ZmtmQnBrX1l6T0h0SzBkazF5ZGZublFHVXBOdjVjbXBnMmdVbDVXNDZ6MUFxUGV4eGlDNA?oc=5) <sub>GamesBeat</sub>
- 📰 2026-10-13 [World Model Odyssey-3 Drives Cars in India After Just 20 Hours of Simulation](https://news.google.com/rss/articles/CBMiwwFBVV95cUxQWFAtTkdQaWVzV09kMmkzclIxNktyLWlQMUdqQjBpSGZCR21SS1VYZkc3dEdCOVBENmU2aDlzTDlMMFdSTnd1c3ZEZ1pZTDRwTzZxQVJXQ2RqQnEyMzRTb1hEV2hRTURpWlo2Zl93NGdKd203VDhtQm9lNzVCMmdoUzdTNTNzX3plZUlyVldmRnVnWlVxN2EtTDI3bFBGdENTYXhxa0UyM2dkV1paNFJuaXVJYlU5VTY3NlRCVU1pand0M0k?oc=5) <sub>Tech Times</sub>
- 📰 2026-10-13 [HPE Confirms NVIDIA Rubin PCIe GPU in ProLiant DL585a Gen13 Server](https://news.google.com/rss/articles/CBMihgFBVV95cUxNcEhOLXktNWxpTUxuVnNBRTQ0d3VEZzVoTl9nMVhYSVJRSXUtYlpsVWw4NFJmcTg3emVkUWlNcVQxMEVnN3JMaEF5MVVzaTEtQTNVTUM3YTVXNk1YYVdNU2VQTEE2X3UzQnZQTlpMOEloektVWEhpMEt0WE03X19WLThNaDJuQQ?oc=5) <sub>Technetbook</sub>
- 📰 2026-10-13 [From Earth to Orbit, France’s Ecosystem Delivers Agentic Computing at Scale With NVIDIA](https://news.google.com/rss/articles/CBMic0FVX3lxTFBTRGZFbUlVZjJzY1M2ZGVVc3hubnlhYmNTTlJCWk5xdWJBeENiZzN2RGRfZ2U5d21tMjNVV0xKcFFSMm5BWDFydDhjT0o1NFBGQlc5aWlEcG5kMUlNY1pNS2J1UGhJaGlwbmhkaTFnYmtoNEE?oc=5) <sub>NVIDIA Blog</sub>

</details>

<details><summary><b>Wayve</b> (59)</summary>

- 📰 2026-10-13 [A ride in a self driving Fiat](https://news.google.com/rss/articles/CBMiZkFVX3lxTFBLWHl6Y0t5QzNXY185VFVmcnZzMjJJNnR6T1ZfMkVZbFdOcVVoaXBIdzYwS1lKMjQ4UVNTQXpkYlc4S3p5SGpnbG11OC1ZeTlzdmI5TnF4WHZIYlhIRFRfSHpqQVNZUQ?oc=5) <sub>Focus Malaysia</sub>
- 📰 2026-10-12 [Stellantis and Wayve Aim to Cut Self-Driving Costs](https://news.google.com/rss/articles/CBMivwFBVV95cUxNQ2hZZUdLUlVEWkpxMVFySTF6bXRzSU1pNmF0T21GbjBfYVlZekMtYmtNOWNIQ3NLVVFOSWVvQnZpUUhVeFBPTGNjRG16ZkRqTjNPLVhrN3JLRjlyYWFwQmM4anVqT3JjSGswWDFBdG1ZLW04bkJYczk5WGx3X2t5cE5IUjhiVi1LMktrcDhDM0ZONGtXUGRZVFFyRWZXNTdHM1hEbldxNlNTbDB6NFpnM01BeGp5eFlMeGtHWkJxMA?oc=5) <sub>Konsulteer</sub>
- 📰 2026-10-12 [A ride in a self-driving Fiat - Autos](https://news.google.com/rss/articles/CBMiO0FVX3lxTE41TjJieFFsTnBHYl9HMGh4NjcwZFloUFA2VmhlazJEU1E5WEpFUERFU1h1V3pRejFSWG80?oc=5) <sub>Howl.link</sub>
- 📰 2026-10-12 [London Assembly takes hard line on robotaxis in scathing new report](https://news.google.com/rss/articles/CBMipgFBVV95cUxPc2JhYnF5bEpzYnpHRVFiWEdablprSXI1NTR6R1FPVXNOQW9tOGxTMG9SSG5ZandWYlA0Nmgxd3d4aDVQX2w0REIwbGcyTjdvYWFfd1JpNW91RFUyNlZOdVdMa1JwVlZaSlU4NzRvZ3FVamdEbzFfX2lYZFpCODR2cDh2N1M3R3pFMUdXZDg2bk9SWWdreE1mSmZDekhNc2JZOGdlOWZR?oc=5) <sub>Professional Driver Magazine</sub>
- 📰 2026-10-12 [Rise of the Machines: What Angelenos Think About Driverless Cars and AI’s Threat to Hollywood Jobs](https://news.google.com/rss/articles/CBMi0AFBVV95cUxQQ0NkcjJkZzFrdmVfZ3pfU0drRzFzazVibFFqZDNTbHRzRWJweEFhOGhfaGp2Zi1DU291bTJMOUo5Y1NaWExNQ3Etc3V5b1A3VXpMdl9CVkpkeWJGalh0QlRIUjlwcHF2SnUyazMxcUYwRGFYV2h4ODhDb0U0bkFLTzhja1V5ZnM2dGJRLVdrUFpNT3RuMjJaS1U3N3JKdmk3NW9Xc3VLaHl5bXgtS3o5Y0RVeDJNUWNBd01vcVZsbmptTnU0LUJkRGR6ZmFZaU1J?oc=5) <sub>Technology Org</sub>

</details>

<details><summary><b>Momenta</b> (91)</summary>

- 📰 2026-10-14 [[China Shock, K-Industry on the Brink \| Autos] 2. China Hits the Accelerator on "Autonomous Driving"... Even Europe's Luxury Automakers Reach Out](https://news.google.com/rss/articles/CBMiZEFVX3lxTE8yM1VubTBHUjFyM1RQejJiV0ZLMzlaY0JFbEdlYl9UVzZKRDNjXzBQaGxDc1RJTlFqVjBXZTMycWdZLWlVd3JaNldqblRYOEZJMDE2MEJYcmMzRDNBUVBoMGZ6SGg?oc=5) <sub>아시아경제</sub>
- 📰 2026-10-14 [更像是一位时刻陪伴在身旁的“老司机”。#新车划重点# 带你看看这台车在智驾方面都有什么亮点。1、【越级感知硬件】](https://news.google.com/rss/articles/CBMiY0FVX3lxTFBvVmJQQTIwUVFBdW44dGRxSVpwRm1DOExRd2hMalZxSzV6ZmNxOTZzeC0zNTJwS1lmSGVTOURTb1ZYVk82RE5iZFNZZk43UldBTzVqWC1hSGNpMDI4TXUwaHZNaw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-14 [带激光雷达的豪华插混SUV哪款好？全新混动XT5与领克08、腾势N9、理想L8、问界M7横评对比+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFBfNWdEckdDeE9zSHZVVTNjMnhfS2s1T1JpNEREZTRTM2pUTW1xRExEU0NYczRoSHZpY1BiN2tmMUxVNk94VDE5Y1AwQXhjZU5OV2ctc3I1VlVOR0R5cElyYWJoMWVrTE9vcmtTTExnV2NMUQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-13 [丰田铂智3X销量累计15万辆了，还有人说传统车企落后吗？](https://news.google.com/rss/articles/CBMif0FVX3lxTFB6RUQwUzI2emtFel9lZmpRaW5EdHZYMjhQZDJ6ZjhDNG5JdGMzSVlvdkJSN0dlWTZoeHlWb0JpQlRSUVNTb1BDVjBkZ0xDZDl6N0pKN29IUmN4SWhDNUoySGp6am9mNTA1WkpWTTJNUzE2RnJ3dDY1VHREQ1ZGYk0?oc=5) <sub>新浪网</sub>
- 📰 2026-10-13 [ID. ERA 8X用第一梯队智驾，撑起合资反攻底气](https://news.google.com/rss/articles/CBMiW0FVX3lxTE51MFZ6R01Oa2NvVFNHOEczakxUQXpVX1Ewb1U4TWhLSlFWM0FvaE50T0EtWDVOcFoxdDNtWWQzYXFMOUtBUlJYclZ3NkNlb2hHclBEWWFXbFR2Rmc?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>XPeng</b> (289)</summary>

- 📰 2026-10-14 [25万预算新能源SUV横评：小鹏G9L、理想L6、智界R7怎么选](https://news.google.com/rss/articles/CBMickFVX3lxTFAzVktpSW04dW5DaXVWUlhDU244TFBPSkZ4Z0ZvbGRKdXI3VDYyYnFEcEpfNkRiekE2WG1jNENaT2pRNnpXd19UXzQwS2puZ2JleFZtWExQdW13WE44ZjEtS2Q4TVVieVYwOWhpQ1BybUJ1Zw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-14 [智能体验好的大五座盘点，小鹏G9L第二代VLA全系标配值得优先看](https://news.google.com/rss/articles/CBMickFVX3lxTE15a1k4ODBEVjlsR21xelByYlhlU0w4Ykt5dHA3WTVXVThIbms5REhFLVBvd2lVNkI1M3dHa3hfbkJtdzRTTk9rd2FVUk1paW55QkJ5U0tieWY2RHZBOEk1UU1hRjlCbVp1M25ObXQ0bFhhZw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-14 [舱驾一体哪家强？小鹏G9L与智界R7、理想L6智能大五座横评+选购清单](https://news.google.com/rss/articles/CBMickFVX3lxTFA3Zi1VdG5SX1VlSTZkWW41OXRJTXloM1h4LU9wLVlQdXRJWnh4QnhHV0tudU9NZFd4aFl0bDRUX1ZnOTJiSU9MWllRZFBoUXY4Y0VDYm5NM3JFSHBJTTJ5SmFhZEY5N1Z4QXFKekNzSXZqQQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-14 [25万预算新能源SUV横评，小鹏G9L与理想L6、极氪7X怎么选](https://news.google.com/rss/articles/CBMickFVX3lxTE5mOTYycTZ1Z2RHUHM4US1yZ3U5NEFKUVpGYjEwa28zdmtXVTJIQ2t4NlZyenEzWURDOUszOU9zVXBJOHNWTS03Wk5DM2dRcjVUY2puaXFaRXJMamxsZERRTDkyWktTRi10NVBOcW8xMHN1QQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-14 [25万预算能买到什么配置？小鹏G9L与4款热门新能源SUV横评](https://news.google.com/rss/articles/CBMickFVX3lxTE1wZUNKeHJ0ZGxPenhLVWQ0b1RJaWlwX3QtbEt5MWp6OE9neWR0SV9oVnJEcHZBSzYyQXR0azNKQkppMEl0NWNrdEM5T1lhZ1F5TmJ5eHB2T3JRYlU3Wm1Gc2Vnejh4UTJoRXNRNHIwNm9PUQ?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>Li Auto</b> (162)</summary>

- 📰 2026-10-14 [舱驾一体哪家强？小鹏G9L与智界R7、理想L6智能大五座横评+选购清单](https://news.google.com/rss/articles/CBMickFVX3lxTFA3Zi1VdG5SX1VlSTZkWW41OXRJTXloM1h4LU9wLVlQdXRJWnh4QnhHV0tudU9NZFd4aFl0bDRUX1ZnOTJiSU9MWllRZFBoUXY4Y0VDYm5NM3JFSHBJTTJ5SmFhZEY5N1Z4QXFKekNzSXZqQQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-14 [25万预算新能源SUV横评：小鹏G9L、理想L6、智界R7怎么选](https://news.google.com/rss/articles/CBMickFVX3lxTFAzVktpSW04dW5DaXVWUlhDU244TFBPSkZ4Z0ZvbGRKdXI3VDYyYnFEcEpfNkRiekE2WG1jNENaT2pRNnpXd19UXzQwS2puZ2JleFZtWExQdW13WE44ZjEtS2Q4TVVieVYwOWhpQ1BybUJ1Zw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-14 [25万预算新能源SUV横评，小鹏G9L与理想L6、极氪7X怎么选](https://news.google.com/rss/articles/CBMickFVX3lxTE5mOTYycTZ1Z2RHUHM4US1yZ3U5NEFKUVpGYjEwa28zdmtXVTJIQ2t4NlZyenEzWURDOUszOU9zVXBJOHNWTS03Wk5DM2dRcjVUY2puaXFaRXJMamxsZERRTDkyWktTRi10NVBOcW8xMHN1QQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-14 [25万预算新能源SUV怎么选？小鹏G9L与理想L6、问界M6横评清单](https://news.google.com/rss/articles/CBMickFVX3lxTE82VlU1MkdMWkxDQjlEemxOLXVpWkdGRE5MX21xYzByejIwZDdJOUpvWHFkbjlqOFJpUklNdHg5RmVzUGJseHdBVU5ZQTc1Q1ZRbTBQVkU5XzJhdVp3cXZrWG5sbFd2OW4zZUJLNXB6VGVSQQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-13 [新上市的豪华插混SUV哪款值得买？5款近期上市新车横评，全新XT5值得优先看+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE1aaVExSDg1dkxPdW85b2loWHhTbnpjc2Q4SllkOHY3LVNxNm9BWlloLUhkSkJVNEN1UzhtOTBEbzN3eXh5T0RYNWJQbXYxZWYwSU5pTHBGVzVsRlVNQWEzWE0wZTFCWWpvUXEtaC1oU0c4dw?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>NIO</b> (144)</summary>

- 📰 2026-10-14 [全家舒适大五座横评：小鹏G9L、理想L6、问界M7与蔚来ES6对比清单](https://news.google.com/rss/articles/CBMickFVX3lxTFBMZW50VEtUbDRWdWg2REIxYnVHMWFQdy1INTdic3lZVTlPSVdoSEwzZTVXOFlabFNjdTNSRU53QlE4dXoxLXhPSEN2M0xRNlN0YU5OS2gwdVk1cGprWHVzcVNNUlJ4Zm9WenVlY0tTaVZCdw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-14 [麋鹿80km/h+与5.4m转弯半径：小鹏G9L与极氪7X、智界R7、蔚来ES6底盘横评+怎么选](https://news.google.com/rss/articles/CBMickFVX3lxTE5aMnRaeUpCeXJkUGZjZHBQOVdIdS1RVXM5MVJTOHprV1ZMSlIwM2FfaU1lb1VkYkd0TDQxR181alY5T3hTZ2FVR1dOWUtLdVdVZjNhMVA4N19JQTh6Q01FYzF1QjhGYWdhalB4a25nTnh6Zw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-14 [双腔空悬+后轮转向：小鹏G9L与极氪7X、智界R7、蔚来ES6大五座SUV底盘横评+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFBpaFhBV0F4SkprZkt5eVRFbWtFNTJyd0h0VlBOQVROVEd6VWRsa2N1R3luRXJKa2ZnUTFBcFlvcjJpWG5iNUEwLW5JMWRrMHZFVUVuYXZtM3ZucGxzVWVlcWFCT254ZGM3TmZxenRXazhzUQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-14 [麋鹿80km/h+大五座SUV底盘横评：小鹏G9L、极氪7X、智界R7、蔚来ES6怎么选+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE1qdERjNlB0dGROUmpVX2YwT2NQZFYwNG8zNE5lS3ZxUWU3WU1fd2pCMWtfNmNiSnJsbTV6cXcwUXl5MEY3SlNkSWkwYjA3ZG83aXZOZFhPWWF5RWxncU56WHFmRjZLcGkwcTR4TnNObjF3UQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-13 [【视频】2023年上牌蔚来ET5 75度买断](https://news.google.com/rss/articles/CBMia0FVX3lxTE9uUklFRmlzMXpXTG9BY2x0dG9uSWdMeERpUGRYZ0M5ZGs1TW03QVlEZ0tkOEp2cUw5eFZqMmtLQjlJTHEybWNtc0ZxdGt1T3pFN1NSaG9kTTFxcExBWVhJSUpEVlJ6LWROaGZJ?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Huawei</b> (396)</summary>

- 📰 2026-10-14 [Avatr debuts three models at Paris Motor Show, to formally enter European market in 2027](https://news.google.com/rss/articles/CBMi8gFBVV95cUxPTGgzS1BKeW16WFp4NVFtS3p3MlVsSGZ4Q3FpTkVPRHVrMnNyRzQzZFNMakFyb1lXZWU0NDlZWWQ3QUZiemlMbzhyY1cwWEt4SDEzcTNwcVNQR2pxcEY5NzA3dzNXaWthYlF3UklLenNDOHgtVktiV0U1WVJ1a0NJRkk1LXA0cjEtMGJDR21KNC1UbS1fZ1RHMnVPeDNhdkRzZlRtN2ZPYU11N19hV24tQ1QycGl5MTJBdUVnLURWT3VtNVkyVGlicGlmRkRaYVdqeUM0UmY2VVYwRC1BVWNQQVBOWmxMYlFXWG9rUld0b1Iydw?oc=5) <sub>Gasgoo</sub>
- 📰 2026-10-14 [[China Shock, K-Industry on the Brink \| Autos] 2. China Hits the Accelerator on "Autonomous Driving"... Even Europe's Luxury Automakers Reach Out](https://news.google.com/rss/articles/CBMiZEFVX3lxTE8yM1VubTBHUjFyM1RQejJiV0ZLMzlaY0JFbEdlYl9UVzZKRDNjXzBQaGxDc1RJTlFqVjBXZTMycWdZLWlVd3JaNldqblRYOEZJMDE2MEJYcmMzRDNBUVBoMGZ6SGg?oc=5) <sub>아시아경제</sub>
- 📰 2026-10-14 [Avatr T09 Debut: Can It Drive the Brand's Leap?](https://news.google.com/rss/articles/CBMiuAFBVV95cUxQNm1OcWxQYVN5bkh4X0RjNFZka003LWxjQ1lfOC1ERFJ2QlUxdEJHby1YQWFNV1o4NVY2OFp2cV9Zb2l6cjJaNVZiejFQMVdoOVlka3o3NVlZT01KUHZ1V3BRdHVKNXNzSnRSeDFQR25LR2xvRGI5YVlxemNxLUMyeS1vSDRzaTVkYjJPdFZhM1RVNHltTjBibEpFa3F3RUNpX0dkM0c1bENyTHQ2MTMzb1NoeElSWWs0?oc=5) <sub>Gasgoo</sub>
- 📰 2026-10-14 [【视频】探店\| 华境S把路走宽了！大六座+华为乾崑，花15万享受MPV的舒适](https://news.google.com/rss/articles/CBMia0FVX3lxTE44am9KMkVKcWlSczV5bGZwUGRaR0VXMmIwSVpjN29Kc0cyYXp2TmZsZjc0SW9uMDNDUC01Zlg0RmxnRFRfWE1pZ0h1VVpYNXhZZjcwRngteTJwcUtUOUhLT2s3YUhHTV84c0g0?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-14 [【视频】12万多买华为智驾大六座？星海V6顶配提车](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9HMnR1QjV6bHlOaFp1clZYdncwWjh2cEdwMDdkUDVyQXpVNk9zZkdsV1RTZGU5RjdTanVmM3BnM0pPa09lTXAyTWVzUlpBWkJ4MEdSNG1RMVhBTHc?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Baidu Apollo</b> (55)</summary>

- 📰 2026-10-13 [Waymo完成50亿美元首次债务融资，特斯拉Cybercab单日新增注册150辆，小鹏Robotaxi启用小鹏悠游](https://news.google.com/rss/articles/CBMiVEFVX3lxTE9JZFBKMTdRVUxUUHhQT2RzZ1EzTWtGS24zR3BfX20yNk5Uek42LXA1SWc4UEVEU3l5SXZoY0xJRVFlT2tycHgzWEZEZzhuY1gtZjRydQ?oc=5) <sub>虎嗅网</sub>
- 📰 2026-10-13 [【视频】骑了10年摩托第一次在路上被这样打招呼](https://news.google.com/rss/articles/CBMia0FVX3lxTE4tblJESDFLN1hsWHVRZmFHRUZjX0w3VHZzbEZCY1lPMGRRRlFXUmdVS2p1UC1VYXNUQ1VJdFF4UC1Lc0pKcjZhNlB3aHVGNTc1dDlYdUJQejYwc3ZhenhFd0JXMWpxUWpENXVJ?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-13 [Baidu opens free Tung Chung robotaxi trials](https://news.google.com/rss/articles/CBMie0FVX3lxTFBtaVl0RjQtXzRHY2dNNzNHZEEwaW9QQ3pFMTlrc0dIaVBqRUhubVRZdDI5ZXh0NnV2VDFKcU5KQ3BoNGdEUjdCNHBVWi1BN0hjOWhKVFZxT3NHRGhmckVwV1JqUUZQbG1XdG9JeXMzcjQwV2hBc2NMRkp5RQ?oc=5) <sub>Dimsum Daily</sub>
- 📰 2026-10-13 [深化智慧出行合作 韩泰iON携手萝卜快跑拓展十城自动驾驶版图](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBRSFp5M1hZZkM3Z21vS0xJWS1vOHkyM3pYMWJkMWNlSDBBcHc3aGpFT0x4T0RiSloxNDFlZFhIdHRzQjRmWU44UEtZMXlHM242OEdLTkZkR2k3S3c?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-13 [三菱全新跨界跑旅EclipseSportback预备正式上路！纯电驱动](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1vT0VkRnBqRjF3VFVZV05sOEFubFpLdFgyMmdrYjM4UUZDMzByaDNhRE4tSjUyRFBHMVBJYXdzRVd2VG1iUVJpRFRUcFl4V3gwYzlmdjNjOFNlb0k?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Pony.ai</b> (148)</summary>

- 📰 2026-10-14 [Croatia trials full driverless robotaxi service](https://news.google.com/rss/articles/CBMiogFBVV95cUxOYXJtbDc3MEc2T3Vva1NnZmdMMlNQd0w0V0RPdm9lak0xeDJVbjhMQ0Zra0hLZWdaTElBdnpGM1g4VGZQWFNYUmNoX3RUWElIY3VJWnlobk5PdEd4R09tMFlZMGFfckJaSzlhZ1V4clFSclFOZE5NbmZzaGRyU1NhaW0wT1dzSUNzbUY1Z082dkJxSS1LVHVWX1A1M3h2UHJoRVE?oc=5) <sub>The Star</sub>
- 📰 2026-10-13 [美股存储、光通信暴跌，Lumentum跌近10%，中概股多数下跌，小米集团跌超6%，霸王茶姬逆势涨超6%](https://news.google.com/rss/articles/CBMiggFBVV95cUxObjF2Q19XMWt4NFN2ekFXclk0cWlDZkIzM0ZHMk12RDJTVzNud2JjdEtxLXVqS2VtTVd5aDZ5NFY3NEdQOUVFTjBTUEtWUE9JTk9JVEN5YmtKTjZ5SE1pVnd1ZWhnSWxrcjByNUZrRTUzaTN4dlZWNEl6U3JaZjIzMWJR?oc=5) <sub>新浪网</sub>
- 📰 2026-10-13 [小马智行-W盘中跌超10%](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBTaGkwYnZPSXBUVjlHeERzRUs4Z19SYW9iOHdBWFFxeVktVWk2azhDZ2ZHTV9VOFhYSGJFV21lZzRYbm5qV3lWaXpNVmNHTGRoUTlkODRaR0kzd0Ni?oc=5) <sub>www.caiwennews.com</sub>
- 📰 2026-10-13 [粤芯半导体登陆创业板，早期投资方广汽资本收获51家上市公司](https://news.google.com/rss/articles/CBMiWEFVX3lxTE9mLVBUX1FmNVBNYmVQeFRBRFN0ZDV3VWhTVGpmREdEN1lnR2N6d3RYd3FCMUQxYlhBbDZtdlVIT211cU4wT19uX05xalU2dnlIckc5aFBlMm8?oc=5) <sub>36 Kr</sub>
- 📰 2026-10-13 [Waymo完成50亿美元首次债务融资，特斯拉Cybercab单日新增注册150辆，小鹏Robotaxi启用小鹏悠游](https://news.google.com/rss/articles/CBMiVEFVX3lxTE9JZFBKMTdRVUxUUHhQT2RzZ1EzTWtGS24zR3BfX20yNk5Uek42LXA1SWc4UEVEU3l5SXZoY0xJRVFlT2tycHgzWEZEZzhuY1gtZjRydQ?oc=5) <sub>虎嗅网</sub>

</details>

<details><summary><b>WeRide</b> (140)</summary>

- 📰 2026-10-14 [港股10月14日午盘恒科指涨1.61% AI概念股多数调整](https://news.google.com/rss/articles/CBMiYkFVX3lxTE56ZXE2UHE0bGxiazYzQUYyUTB6SWxwVG1HV01ub0xqRzJ1U0dhZURLcjZhMjVSZldjeUJhQlpNM1ByTjR3aWlfU25ZV0ZZOTRyZVdaeWdRWUhBNnozOWNydjV3?oc=5) <sub>观点网</sub>
- 📰 2026-10-14 [医疗健康产业日报(10.13) : 行业动态](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNODRVRlFCaVlxMGxlcEN3Vi0xRVdVVGcyb01Wb1YwbkVwX3lkbEFVZ0xHSTBqMUlvZEJ4QXRtTW1wcEhUTms5SklpWmdJTDBpNTMwcnh5M0ZMRWw4dkpublVCNHlTRHRwcmw3Q1VEclBMTG1UZ1Vfak96VTlxUTNDZmVCaGozQzI5?oc=5) <sub>搜狐</sub>
- 📰 2026-10-14 [10 月 14 日隔夜要闻：美股收跌 苹果智能家居亮相 OpenAI 办公室被植入精密录音设备](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE0wRUpvWWNYRlVCTTdTb3pGVWZQWjU3cjB4U1FERXlRSVVUUWN6VEFfRXNBZ3BuRFFfajlOWTdVb0M5NVIySXJ5X3hEZDRLLWttYnJBdTN5Z2JZbXg4ZmJJa0FBa25nTTA?oc=5) <sub>ZAKER新闻</sub>
- 📰 2026-10-13 [Waymo完成50亿美元首次债务融资，特斯拉Cybercab单日新增注册150辆，小鹏Robotaxi启用小鹏悠游](https://news.google.com/rss/articles/CBMiVEFVX3lxTE9JZFBKMTdRVUxUUHhQT2RzZ1EzTWtGS24zR3BfX20yNk5Uek42LXA1SWc4UEVEU3l5SXZoY0xJRVFlT2tycHgzWEZEZzhuY1gtZjRydQ?oc=5) <sub>虎嗅网</sub>
- 📰 2026-10-13 [Uber Robotaxi Leader to Depart Next Month](https://news.google.com/rss/articles/CBMigAFBVV95cUxPTnRaT29CdC15OTNRUXI3TXhPOVJLTmpjS0c3bVVEeHBkU2szVEFBR2YtTG5keFFoMHBvLVNscG5HaERtUWRkNzZiS08xNHYzMFIwNjFkeEhmN19xTWVzTkpXaEFVUzVJZ2JqYzJaTWxMME4zaElqYldtTm13WC1TQQ?oc=5) <sub>WSJ</sub>

</details>

<details><summary><b>Horizon Robotics</b> (183)</summary>

- 📰 2026-10-14 [China new models September 2026: Hongqi G919, VW ID.AURA T6 and Hyundai Ioniq V arrive](https://news.google.com/rss/articles/CBMiwwFBVV95cUxQT085WTFGX1dRMkpRSFViX2tkNnFNa1BGenJ0RVdiTXFGN0JlNU9LMU9QOXpNcmUtanVxaFUwaEtyb3AtLTVOMGRsdm9KX2YxdTBtLUMydlktVnFnVzJTcENqaHZJanpMbGF6alB0THFibmxaLTdEcDNuSjQ0SGFZM09aMWwyX0l1dklXVEJBWjBEUGplY1Z3bDVtMjRwQ3lPYUtYMTJZZFp6aEpEdmptTUNuWWMyc2dZLWMtQ2d1dUhrWkU?oc=5) <sub>Best Selling Cars Blog</sub>
- 📰 2026-10-13 [【视频】深蓝推出两款PHEV车型，满足海内外用户对动力的多元化需求](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5OM2Rta2dQd1hRaE9UWmQ5aHgzR0x1eTZRdElubzJLVWU2Z3hDVk1wcFZjRUZOTVlVYWFKMnM2ZDFFX1VGaUVWU3kwaFltR0hRbkhWcW5DZ0VSTzg?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-13 [【视频】都是方盒子绿牌车？怎么选#传祺越7#吉利银河战舰700#长城H10](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9lVTdLS3lIVFZQVmxEUFh5U0paNUZVMHVOak1tbkppNXZBMm1RUkE1VDYxSGNMLWpReGJoXzMxemwtTVVPRXJjVC13SkZlcEZ3cGdYcHl3ZDNYLWc?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-13 [地平线整车智能体获工博会2026 CIIF大奖](https://news.google.com/rss/articles/CBMijAFBVV95cUxQME9nazZWSmQ5MGVLdkZZVmFzNmx4TzBCdzFDVFBrY0NzS1ZqNDh6YXl5MmJuSENnVFFvck15QU41V0t4d3ZoV3NyMkxsbExqLXBBUGQtNW5sWFpCei0xcF9WMmlJLTl5U24xQ3F1NEs4ZnpMdWItZTY1MW84aDNoUDlfWGh6UW5TS2NXQw?oc=5) <sub>搜狐</sub>
- 📰 2026-10-13 [合资纯电SUV高速NOA谁更让人安心？三车横评：丰田bZ5、马自达EZ-60与大众ID.AURA T6的智驾答卷](https://news.google.com/rss/articles/CBMiX0FVX3lxTE92TDA2d2h0WWptWXplcWxiWk05SjE3eFB2NFVReWxVd3RMcjZKVlZvaW15Mmx3a0Y1VlhkWG9fb3YyVzdHZEM4cmVxUE5fbUg0bngwM1NadWI4dlU1VFhj?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (28)</summary>

- 📰 2026-10-14 [赛豆科技AIVA第二款SUV或将采用换电方案](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5WSE1zeWlTbjE1UFVyQ2tveGFfS2lhU0FoVFVHR1J2NHhUbUY0U3RUai03SVV6UlREQkM2dENhRk5WaTZGM1lxRjhNakJYY2xFLXZ0Z1JBQWFSLUE?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-13 [TomTom与元戎启行达成合作推进基于AI的自动驾驶技术_车市动态](https://news.google.com/rss/articles/CBMia0FVX3lxTE9XcTVveVNlN2hfeVcxOThFNUd5NjdLY1JJNTcxWFdKU19Ic3p0bkVIcHBNdHFEdnBHVW41cWZwTXpuazJsRDY5cmtGVmdoQ2R3UWVscldLMFpDYzRUaTZuTUtqc3d5Z2pDTjdn?oc=5) <sub>中金在线</sub>
- 📰 2026-10-13 [TomTom partners with DeepRoute.ai on self-driving cars](https://news.google.com/rss/articles/CBMihwFBVV95cUxNczBsNnlscW41ZWlKVHVSZG1mc0FINkMxTk15TDBjZ18yRjF5S01LRFJBaF9sakJkU0xIdHYzWGZNRnJzY0pGOWoxQUE1SlFUVHJiZXJsaXlGZW1LSGtSZEhXdEtmcVZFTko0RGphSWNfYmZKY2ktRHJGc2ViUTVrUkd4clg4STg?oc=5) <sub>IO+</sub>
- 📰 2026-10-12 [TomTom and DeepRoute.ai partner to advance AI-based automated driving](https://news.google.com/rss/articles/CBMijAFBVV95cUxQM25CX2RxVmJzRkc5bmNUMGNTUGxlSU9pOEw5d08xb3ZyWjEyRlNtcVJvVElNenQ3VVhlQ0ZhcXd0bjh5OVNnOG81LWlOUnVRSTZYeGFOaU53V2d0U0F0WjZpcVJHMXR1VkpSSjFjLWdFOFM1NEhOSUYyVUozb0VRc1FKeGRIdjVqYndUbw?oc=5) <sub>Yahoo Finance UK</sub>
- 📰 2026-10-12 [费莫一刘念邱：智驾无图的经验，也能迁移到机器人 \| 物理AI 50人](https://news.google.com/rss/articles/CBMiekFVX3lxTE00amwwNk9KSGJlbUNzcXBtdWFQZEZpNHZxcVF4ZHJoTFg3T2lhUjlZREU5cUx3X2hYckROWEgzalBDYURDVThkZk1LMnZlTmtvQUJlbTZ2RmtVNGJGczNGMEdxNkpURHRXQS1rQUs3UXhWN2F0Nk9HWWFR?oc=5) <sub>雷峰网</sub>

</details>

<details><summary><b>Mobileye</b> (13)</summary>

- 📰 2026-10-13 [Mobileye Announces Timing of its Third Quarter 2026 Results](https://news.google.com/rss/articles/CBMitwFBVV95cUxQc2dBRE5uWEtaSE5fRXRuTEdtTTVwamoxQVBSNlJMVTlxbm9aZFV3Q0RkSTdkcXpBQkt0dnVNRmRULXFPUEpoNlo3NTB5WEd3RldGMWdYWWpLVVFVaW1nRFFUWlhvSWp2ODF3WUtnekNuNzBXeG85VDM5eWY1U0taamZjcGFTbkw3Mjdsbm9pR1g0NGFGMC1LX3BrQWQtemJMbVl4NFhtSzlScGZHTS1EV01zQW1NRGs?oc=5) <sub>Business Wire</sub>
- 📰 2026-10-13 [INIT enters autonomous fleet management market](https://news.google.com/rss/articles/CBMijAFBVV95cUxPRW92TDM0SHlYNWFaMlJhMVlqUUVLN21oak9rSzRBX2hVTVdFNG4wdnBrMElCTmY4OGhXaGtTaWVZZ2JURkdYLTVLRkpmWHg3VmlncUlHMDZla05MdkRzdmxCeHB5RGNoSEhvX2RzMEtVT2pNaTVGMjBIZ2p4VFlJTHMtMVczdWFvSkdsTw?oc=5) <sub>electrive.com</sub>
- 📰 2026-10-07 [Uber invests in robotaxi provider Verne](https://news.google.com/rss/articles/CBMigwFBVV95cUxQQkxEa25xSjBNT0ZJMzZINk54a2txS3k0S0pvTU4wZEJ5eVhHY0FNRWlyaVdIcVhYdmlPQl9HVUsyUnlkcW1UVzRVc180dHNCT1hXV3ZUcms3Mzg5aUoyZENTUWU3VHJtRlFuQmp0dWpQRDlmU2xlSDQ1MnlEZW11YmFGWQ?oc=5) <sub>electrive.com</sub>
- 📰 2026-10-07 [MOIA America Launches First Autonomous ID. Buzz Rides](https://news.google.com/rss/articles/CBMixAFBVV95cUxQY2FmM1hNRDEzV0c3c2NSVklIUDBPU1VrbmRmNnRLV3lNRzRITUVHUldKcVNYajNSYXJkdTJmbzRGeWt3V3ZrcXlmanBfR2t5cjRKZlU3b2JHbUg3VUx0ejdIS2ZUT25DRm5KTGtzSm1OaEhhQ2Zsb2Zhb0tHMDlnaWhnOGJHLXBvYk1GYkNYVFJRb2M2R3BmamRnN3RMZlJ2a3JlSGc3VnNmcXBtVDdub0s2VjhXSDhKVjFDR1pIQjYwLUpI?oc=5) <sub>Fuel Cells Works</sub>
- 📰 2026-10-07 [Uber takes a stake in Croatian robotaxi startup Verne](https://news.google.com/rss/articles/CBMikAFBVV95cUxOMkFfTDhoaldrejJpdUNUd1JvRXN1MlZwYVZQRjdPQ19FM2oyWjgxTndscUdGWFVZaG5nSWVKNWQ1dVYtNzFNZ2t0VnFwaS1mOFpneG41RW51M19leE9XSUN5WjhGbjF0ZkUtRVI4RDBiSUxtX2ZCTDBUekNRN3p1ZXZzUFU5aXJ0cjk5bHA3aUU?oc=5) <sub>Dealroom</sub>

</details>

<details><summary><b>Aurora</b> (67)</summary>

- 📰 2026-10-14 [Driverless Truck Beacons: Tanker Access, Hazmat Limits](https://news.google.com/rss/articles/CBMia0FVX3lxTE1jYUxvVlVFNHdFUTlyYWRZbFNkZmt6NS03ZzQyS2JBUjR0bDdqNG1aR1BnZHhjZWpPWWZCZ25VM2Y3VFI0bmZjMklSMDJzMjRnOG4yRVBrU2swWWUtWHBWT2hFSm9sUTd2LUdr?oc=5) <sub>Tank Transport</sub>
- 📰 2026-10-14 [Autonomous Trucking Advances on Costs, Freight Operations and Federal Rules](https://news.google.com/rss/articles/CBMia0FVX3lxTE13ak1NNlJKWHNVTmFwd0FXbVEydXQ1ZENkc0tyVWVIT0pIOUlOVkJ4WXBYLWNRR3ExSmpHNjVkdFJuQVFLV0g0V0dMcHBpYlR6Y0Y3b0xrT25IV2lNenJ1dGt3dXNhdkIxUHRV?oc=5) <sub>Advanced Clean Tech (ACT) News</sub>
- 📰 2026-10-14 [Charger Logistics inks deal with Kodiak for autonomous hauls](https://news.google.com/rss/articles/CBMiwAFBVV95cUxPSW1EOTFJTkZnWDJveV9DZ0Z2WGNRbHpDUWQweHJOcG9GdERiMmFCQ1Bhb1VEcmFWLUZVZWdwMUR5MjN6MDJyRHVpZjhQZDJQbXRneEJ5TGFlb3lNZW94blQyaXpxa1RGbVlSTE14ZklsdUQ2X3dZUDVUMUVhYXJvby1LRG5YYmhpaVRaOGR1ZW9maWJNdHdmbExpb0NuUU4xc1ptQnBJZzB4Zm1XZkRCdlhSdDViaDdLTmJrU1huNk8?oc=5) <sub>Commercial Carrier Journal</sub>
- 📰 2026-10-13 [FMCSA lets driverless trucks swap warning triangles for cab-mounted beacons](https://news.google.com/rss/articles/CBMiuAFBVV95cUxNQlVRTk1zNHRWQnNXcm1RV2Y2Q1VIR212OXJxaUVVb1oxQWxpUjY1WVhiMHhMZzVrSml2TGdVQVN5a3czLUpmNDZZUEY4cEkxTUFmMktBSUppQUNxNkpRcUYwa1VEdmF3NzROR0J2dmdXdGM4QS0ySjg1dTZONFdqOEtIc2NndGU2cjNtWTVlNDlTX3VoZXkwelRYdU43dlk2WGFpRy13NU0wSXA5LUctZDM5ZTlDRjFr?oc=5) <sub>Trucking Dive</sub>
- 📰 2026-10-13 [Inside an 80,000-pound autonomous Volvo VNL](https://news.google.com/rss/articles/CBMiswFBVV95cUxQX0xMNkdzamFsTjl6TnRtS1pwTzdIQXFTNXAzUU1nZUJpZ3ZlbWkyX24yV0pHYXdNQ2VPaU5sWjdPWFlRWVdNeWhhZHktRkdtU0lITWdDanJCNVhCTUhBeERlTkNDcERudXFhTGNaNGF3TEpKSzRwSVkzdkgyM2tDR1hldUtIb0RRUmo0aTZvMFVKWkl3Tm4wSkFYUVdiZ1BweGtIOXVLMFRuYzhGOXR2WVdBYw?oc=5) <sub>Commercial Carrier Journal</sub>

</details>

<details><summary><b>Zoox</b> (70)</summary>

- 📰 2026-10-14 [What Is Zoox?](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1tcFFURGhVdTg2OC1oeS1sTmJhRmFyRmNJMkFKQjkyYktGUXA5Tl80aFBYMW9veF9tTUV2NUVuSGhYQVBhZXdKS1JWOFM4OU5Jb3Zr?oc=5) <sub>Built In</sub>
- 📰 2026-10-13 [Vietnamese electric ride hailing service launches in L.A. with its own cars and drivers](https://news.google.com/rss/articles/CBMiywFBVV95cUxOLW9NQzYtdGJ1U1BEUnczdkFtSW1iR1h5SW1rdkZKU3BVUU10dk1LNW5PRTVHMkE3d3hjRGhDc1VkenpiWmtpc3VVaUxhQU92YXdBNWRqOUlrVjBrcjVraG1CNENRd2NZOWVaZnFfS2Y1VmtfNzktaV9oT0lVVkxXNjN5QXd2dGNQT1JJNnZYa3VvQmhtb25YV29YVUVrYmVMSnpPbGtFV01oaXQtQTBKVTl2d192YTZOeGJzeWl0X3RoLTlqbVZkOU1zUQ?oc=5) <sub>Los Angeles Times</sub>
- 📰 2026-10-13 [Feds Eye Probe Into Reports of Tesla Robotaxis Zooming Through School Zones](https://news.google.com/rss/articles/CBMie0FVX3lxTE02dzdJR1E1WEd6VnhtX2pwLUItbmpTMlZMVUhOY2p6OTFoYUhNNnBvNXdSSG1lQkRGcWNOcm9nOThqYWJsMWRCYTVQbm5PQWh0MVNKX0xzT0p6bV9RSHhBOXhLUEtWMmttZHV4VE5VSS1WeWhXMDdSQkoxOA?oc=5) <sub>AOL.ca</sub>
- 📰 2026-10-12 [Jeff Bezos Could Take Blue Origin Public. Amazon Investors Just Got a New Space Question](https://news.google.com/rss/articles/CBMimAFBVV95cUxORWRPLTFjQnM0WXR3NUdEMGc5VWU5RWVoZXo2bEZxV1FWaDBCTHZNeFEtbHhYRGlrMHozTS1KYlQ2Mjl6dUYwUWEzMXhEOXFIUDFELXFCMnpEWVhfdW1Qa3VhTGZZaUlhUU1DamlwX2FYWTFORUxWWGVzLV9oV1piTEozZHIyQzZ3Y0ExTnpaTkh5ZE8ybnY3eQ?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-10-12 [Amazon in talks to buy AI startup Decart for $7b](https://news.google.com/rss/articles/CBMieEFVX3lxTE90aVNkRUVPOW5nTHBMWDM1YlhiLXJ2THFISE1VMzZxalM5WEdfbjdpZ3lpWUNicGRiQ1lBYmNKal8teV8ydmJTN001OG91dDlVYkZkNG00STdtalJ1alE5ckNQSHNOOXFHNjEyaXo4ZEZ2RHA0U1ppNA?oc=5) <sub>Tech in Asia</sub>

</details>

<details><summary><b>Motional</b> (48)</summary>

- 📰 2026-10-13 [Hyundai Motor Group chief marks 6 years at helm with physical AI ambitions](https://news.google.com/rss/articles/CBMi0AFBVV95cUxOY2g0R29NX1hSa0ZuUzJveFVZYUQ1YzVVNEItNnRkUjY0TnRHNi1fY1ppaVc2YmotOEt3YXhCeWxLNVN1NGQ2c2hGNVJYclBocEhKcDgzNjMtdjFPeGJ1bWJjTFR0UGgtUzNwdWZqQkQzaHB5U3k3bXpPcDQ2S05KUzktWkJWN21WSjItamJ6eV84clptQzRHV25xYXFyNURmamNLWGkxeFVNUDFCeWs2cTJta25zcE54WGFYcEE5T1YyaVQtMEh5ZTZvUTNUUlUz0gHQAUFVX3lxTE5jaDRHb01fWFJrRm5TMm94VVlhRDVjNVU0Qi02dGRSNjROdEc2LV9jWmlpVzZiai04S3dheEJ5bEs1U3U0ZDZzaEY1UlhyUGhwSEpwODM2My12MU94YnVtYmNMVHRQaC1TM3B1ZmpCRDNocHlTeTdtek9wNDZLTkpTOS1aQlY3bVZKMi1qYnp5XzhyWm1DNEdXbnFhcXI1RGZqY0tYaTF4VU1QMUJ5azZxMm1rbnNwTnhYYVhwQTlPVjJpVC0wSHllNm9RM1RSVTM?oc=5) <sub>The Korea Times</sub>
- 📰 2026-10-11 [Six Years into Euisun Chung's Tenure... Hyundai Motor Group Moves Beyond the 'Global Big Three' Toward Physical AI](https://news.google.com/rss/articles/CBMiZEFVX3lxTE1qSWl5SS12dk8yVXMwandrR090TkZkdzZDaFladGpmOGNZZDNrMGxBQV9zSkV5TXpVeXIzWGhKd0FVYUQ0ZFdsT1pEWGxZNDV1UC14N0FsZmxVd0ZFOUVkamhoMWg?oc=5) <sub>아시아경제</sub>
- 📰 2026-10-10 [Waymo's $5 Billion First-Ever Debt Raise Signals a Robotaxi Land Grab, Not a Science Project](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9BaGt6ckszSmpwTDVsOGUzQ29DXy0yc3BsVFdSTjNtZFZrR3dWYUd5TzcwSTYzUTE3MlVmd3B4UG1iSS1kRHpySXpFVlhRTWd3cjVCOUgwVW5FcWc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-10 [Waymo Goes to Wall Street｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTFA2Z3RvWEJLVEtPTDJWNVcyaGQweFBVUnZFb0RST0wxRWhCdUJudXJQeU9helBuODZrTlBDZlh4NF9zb3dyNjRxQ3BzTGpZLWJvQzNObmFlYjl1R010Z3hB?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-09 [Hyundai delays its in-house autonomous driving solution to 2029](https://news.google.com/rss/articles/CBMilAFBVV95cUxOM1BRRVUzZ21fMHFubEhHNHRGcFVDQTFwdkRMWnljalNhS193bHpKY0dLSUZjN2tXamRlZUZIZ24wdmh5cWE5bnI2MzF4Qm5lVXJlWFZqTXE2TkpFLUZJWExJQWY4RDFuemJJbmZWZ01DMmRoUG9yLUlIZHNnT3RVeHdYR3hMSkk4RlBfcjlHU0R6Mzhn0gGUAUFVX3lxTE4zUFFFVTNnbV8wcW5sSEc0dEZwVUNBMXB2RExaeWNqU2FLX3dsekpjR0tJRmM3a1dqZGVlRkhnbjB2aHlxYTlucjYzMXhCbmVVcmVYVmpNcTZOSkUtRklYTElBZjhEMW56YkluZlZnTUMyZGhQb3ItSUhkc2dPdFV4d1hHeExKSThGUF9yOUdTRHozOGc?oc=5) <sub>Motor Illustrated</sub>

</details>

<details><summary><b>comma.ai</b> (7)</summary>

- 📰 2026-10-07 [Researchers Find that AI Models Struggle With Even The Most Basic Driving Skills](https://news.google.com/rss/articles/CBMiuwFBVV95cUxNb2ZGRGxGZDNjLWU1OVBPNjUtUlJXR0hiVGV3WEJ1eUVnSWExMWVvRmJjX2NtQm9sX0plMTU3YzZwUm5ZTzVoSGttcXZmQ3BqbW40X2doNFMycUk4UWE3anlidy1vWHNYZndVZjZWLUYtbnlHeVBFRjJOaTF4SWxzbmotR0xsNkVIcEhfZ0M3LUs5R2FyV1lVdlRRU3JwakpQcXpBUzlEOEhsWlB3Q19EdXFhQjRvZDU5MHln?oc=5) <sub>Auto Spies</sub>
- 📰 2026-10-07 [OpenAI's GPT-6 Astra is the only AI model to finish a real-world driving test in a Toyota Corolla](https://news.google.com/rss/articles/CBMifEFVX3lxTE9iZmN2ZFp6blVBRnZUTkYtYTJ3b0hSb0xhQjZyQXh5MUN2T3ladUlEb1F1SWJzc3FtamZtazk4LTVUWVpNX0ZjbGZwMnpERk45TVVQWVA1RjBZVUxxTTAzTWpaV1JqUzIwM1I2Wk1tTzc3bDJpaWluc2JVam4?oc=5) <sub>Crypto Briefing</sub>
- 📰 2026-10-06 [AI Agents Tried to Drive a Corolla, Crashing on 8 of 11 Runs](https://news.google.com/rss/articles/CBMiuAFBVV95cUxONWxQTEZham1kc1J4S2lMNUh6OTN1QWhXbl92U21NUWZTZWhNUUdwcFVvUHYtVWJzSjl4TjlCeFhUY2ppMXd3WkkxaHJFRmFlNUN2NGFSSENnV2ZZYWRNZ3JIUjd0dzFlTS0wR3gtbmxXN3VHOUkxWWg2VVFpTVgzWGN2T3RPdEFJV0cyWjRPSVFyNWZTYjFyX0pzYjFEUWQwLUlfbGo1bm8xVUZXQmpyQ3pCNXV5ZE9x?oc=5) <sub>thetruthaboutcars.com</sub>
- 📰 2026-10-05 [Researchers Discover ChatGPT Can Drive a Car. Grok, on the Other Hand…](https://news.google.com/rss/articles/CBMikgFBVV95cUxNNnNwX0g5bHV4STJlMXNOcXRnYnBHWHNoelViM2pJSzFob3dvUVJIdFlDRDV4X09DSVloZmxCTk5NODd3b3RBR2JmWEJQRktXUTYyWDNveS15UEw0NnVfSFluMlJxZHlBb3NhYnRNdDJsZ01MbVNpOXY4OW9nQnBSYnFRQ1U2YVd3a3R2ZTY4VlJNdw?oc=5) <sub>The Drive</sub>
- 📰 2026-09-30 [A $999 Box Promises Hands-Free Driving. Its Own Code Says ‘THIS IS NOT A PRODUCT.’ Now NHTSA Is Investigating Crashes That Killed Three.](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPNFIyamduTmQxb1dKNlh5Z1hCYUhyemoyU2I2bjFUWjZQSDVFSDFWOGxlM1hnQms4Q1lpalg0bXlCTEZTdVJ3eGtNTjlLamY2eW9LX09IejF6SkJxSmZ2QjRkU1pUczlRY2g3cUZIN3hvSUc3a3pUWHVKVk40MlY3Wk5SX3dnOHBl?oc=5) <sub>Yahoo</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
