# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-10-18 · 1,280 papers tracked · 40 curated.

**Selection rule.** A paper is listed only if it (1) is primarily about autonomous driving,
(2) has public code, and (3) shows at least one strong signal: accepted at a top venue
(CVPR / ICCV / ECCV / NeurIPS / ICLR / ICML / CoRL / RSS / TPAMI, or ICRA / IROS / AAAI / RA-L),
≥200 GitHub stars, ≥3 citations / month, or a well-known lab with traction. Papers are then ranked by a
composite score (venue, stars, citation velocity, LLM rubric for novelty / rigor / impact, SOTA claims)
with a per-topic cap. See [`scripts/rank.py`](scripts/rank.py).

📅 [Daily digests](daily/) · 🗓️ [Weekly digests](weekly/) · 📦 [Raw data](data/)

## Contents

- [VLA / VLM for Driving](#vla--vlm-for-driving) (9)
- [World Models & Generative Simulation](#world-models--generative-simulation) (6)
- [End-to-End Driving & Planning](#end-to-end-driving--planning) (9)
- [3DGS / NeRF Reconstruction & Sensor Sim](#3dgs--nerf-reconstruction--sensor-sim) (3)
- [Perception: BEV, Occupancy, 3D Detection, Mapping](#perception-bev-occupancy-3d-detection-mapping) (8)
- [Datasets & Benchmarks](#datasets--benchmarks) (2)
- [Safety, Robustness & Evaluation](#safety-robustness--evaluation) (3)
- [Industry Tracker](#-industry-tracker)

## VLA / VLM for Driving

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Teaching Vision-Language-Action Models What to See and Where to Look](https://arxiv.org/abs/2607.01658)<br><sub>Yuguang Yang, Canyu Chen, Zhewen Tan et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 33](https://github.com/ShivaTeam/DriveTeach-VLA) | Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving |
| [DeepSight: Long-Horizon World Modeling via Latent States Prediction for End-to-End Autonomous Driving](https://arxiv.org/abs/2605.10564)<br><sub>Lingjun Zhang, Changjie Wu, Linzhe Shi et al.</sub> | ICML 2026<br>2026-05<br>📑 2 | [⭐ 31](https://github.com/hotdogcheesewhite/DeepSight) | End-to-end autonomous driving systems are increasingly integrating Vision-Language Model (VLM) architectures, incorporating text reasoning or visual reasoning to enhance the robustness and accuracy of driving decisions |
| [SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving](https://arxiv.org/abs/2610.20609)<br><sub>Shaoyuan Xie, Zihan Zhang, Jingxuan Wang et al.</sub> | CoRL 2026<br>2026-10 | [⭐ 21](https://github.com/ASGuard-UCI/safedrive-vla) | Vision-Language-Action (VLA) models are gaining attention in autonomous driving, inheriting commonsense priors from large language models (LLMs) and widening the navigation interface from a fixed command set to free-form… |
| [CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving](https://arxiv.org/abs/2607.04179)<br><sub>Zhaohong Liu, Hao Ye, Xianlin Zhang et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 1](https://github.com/MICLAB-BUPT/CritiqueDriveVLM) | End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving |
| [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)<br><sub>Nan Yang, Zhanwen Liu, Linfeng Zhang et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 10](https://github.com/Zizzzzzzz/MVPruner) | Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings |
| [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)<br><sub>Yuan Gao, Wenting Miao, Mattia Piccinini et al.</sub> | IROS<br>2026-07<br>📑 1 | [⭐ 27](https://github.com/TUM-AVS/Chat2scenic) | Validating autonomous driving systems requires diverse, regulation-compliant test scenarios |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 10 | [⭐ 514](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
| [Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air](https://arxiv.org/abs/2605.31066)<br><sub>Tianle Zeng, Yanci Wen, Xueang Yu et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 1,115](https://github.com/louiszengCN/CarlaAir) | Recent aerial vision-language-action (VLA) models show promising single-UAV capabilities, such as tracking moving objects and navigating to language-specified landmarks |
| [GRAVA: Grounded Reasoning-to-Action Representation and Learning for Autonomous Driving](https://arxiv.org/abs/2609.15169)<br><sub>Xiao Liu, Haoyu Li, Jianghao Leng et al.</sub> | arXiv<br>2026-09 | [⭐ 202](https://github.com/AhernResearch/grava) | Driving vision-language-action (VLA) models increasingly reason before acting, but their intermediate reasoning is often weakly grounded in physical scene evidence and loosely connected to executable behavior |

## World Models & Generative Simulation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [HERMES++: Toward a Unified Driving World Model for 3D Scene Understanding and Generation](https://arxiv.org/abs/2604.28196)<br><sub>Xin Zhou, Dingkang Liang, Xiwu Chen et al.</sub> | ICCV 2025<br>2026-04<br>📑 4 | [⭐ 72](https://github.com/H-EmbodVis/HERMESV2) | Driving world models serve as a pivotal technology for autonomous driving by simulating environmental dynamics |
| [FrozenDrive: Zero-Shot Text-Guided Driving Scene Generation and Data Augmentation with Parameter-Free Frozen Diffusion Model](https://arxiv.org/abs/2606.20110)<br><sub>Yuhwan Jeong, Hyeonseong Kim, Daehyun We et al.</sub> | ECCV 2026<br>2026-06<br>📑 1 | [⭐ 10](https://github.com/daehyunwe/FrozenDrive) | Synthetic data for autonomous driving is surging, powered by diffusion models that promise scalable scene generation |
| [MESSENGER: Memory-Enhanced Sequential Scene Flow Estimation via Autoregressive Next-Frame Forecasting](https://arxiv.org/abs/2610.10759)<br><sub>Jiuming Liu, Jianing Li, Mengmeng Liu et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 0](https://github.com/liujiuming123/Messenger) | Scene flow can capture low-level 3D motion displacements in dynamic scenarios |
| [ASTAD: Asymmetric Style Transfer for Synthetic-to-Real Adaptation in Autonomous Driving](https://arxiv.org/abs/2606.29286)<br><sub>Dingyi Yao, Xinqi Zhang, Lihui Peng et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 1](https://github.com/Dingyi-Yao/ASTAD) | Synthetic data mitigates the data scarcity problem in autonomous driving perception |
| [Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends](https://arxiv.org/abs/2606.01164)<br><sub>Jiuming Liu, Chaojun Ni, Mengmeng Liu et al.</sub> | arXiv<br>2026-06<br>📑 7 | [⭐ 244](https://github.com/liujiuming123/Awesome-Interactive-World-Model) | With rapid development of large language models and diffusion-based content generation, world modeling has attracted increasing research attention, benefiting various downstream domains such as game engines, embodied AI,… |
| [Is Your Driving World Model an All-Around Player?](https://arxiv.org/abs/2605.10858)<br><sub>Lingdong Kong, Ao Liang, Tianyi Yan et al.</sub> | arXiv<br>2026-05<br>📑 6 | [⭐ 256](https://github.com/worldbench/WorldLens) | Today's driving world models can generate remarkably realistic dash-cam videos, yet no single model excels universally |

## End-to-End Driving & Planning

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](https://arxiv.org/abs/2609.26792)<br><sub>Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.</sub> | CoRL 2026<br>2026-09<br>📑 1 | [⭐ 12](https://github.com/VAIL-UCLA/DreamStream) | Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions |
| [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)<br><sub>Shen Zheng, Anurag Ghosh, Gaurav Parmar et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 32](https://github.com/ShenZheng2000/WarpI2I) | Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs) |
| [G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance](https://arxiv.org/abs/2606.26017)<br><sub>Hang Yu, Ye Jin, Alessandro Canevaro et al.</sub> | IROS 2026<br>2026-06<br>📑 5 | [⭐ 6](https://github.com/HangYuu/G2DP) | In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors |
| [SimWAM: A Simple World Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.07468)<br><sub>Zongchuang Zhao, Xin Zhou, Tianyang Xu et al.</sub> | arXiv<br>2026-08<br>📑 9 | [⭐ 197](https://github.com/H-EmbodVis/SimWAM) | In autonomous driving, World-Action Models (WAMs) have improved end-to-end planning by transferring video dynamics priors to action prediction, but many still couple planning with future-video generation at inference, in… |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 16 | [⭐ 347](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
| [Latent-Centroid Steering: Single-Pass Classifier-Free Guidance for Command-Aligned Autonomous Driving](https://arxiv.org/abs/2608.00237)<br><sub>Meibo Hu, Jiamian Wang, Pichao Wang et al.</sub> | IROS 2026<br>2026-08 | [⭐ 2](https://github.com/codingmlinprocess/LCS) | Vision-language models (VLMs) have recently emerged as a promising paradigm for end-to-end autonomous driving, enabling agents to map multimodal inputs and high-level navigation instructions directly to executable trajec… |
| [DVGT-2: Vision-Geometry-Action Model for Autonomous Driving at Scale](https://arxiv.org/abs/2604.00813)<br><sub>Sicheng Zuo, Zixun Xie, Wenzhao Zheng et al.</sub> | arXiv<br>2026-04<br>📑 15 | [⭐ 367](https://github.com/wzzheng/DVGT) | End-to-end autonomous driving has evolved from the conventional paradigm based on sparse perception into vision-language-action (VLA) models, which focus on learning language descriptions as an auxiliary task to facilita… |
| [STAGE: STyle-controllable Action GEneration for personalized autonomous driving](https://arxiv.org/abs/2607.29517)<br><sub>Zihao Liu, Xing Liu, Yizhai Zhang et al.</sub> | RA-L<br>2026-07<br>📑 1 | [⭐ 6](https://github.com/CarlDegio/STAGE) | Driving style refers to the behavioral preferences that drivers maintain during driving, shaped by their diverse experiences, habits, and needs, and is typically reflected in varying levels of aggressiveness |
| [A Survey on End-to-End Autonomous Driving Training from the Perspectives of Data, Strategy, and Platform](https://arxiv.org/abs/2610.00926)<br><sub>Chengkai Xu, Yiming Cui, Jiaqi Liu et al.</sub> | arXiv<br>2026-10<br>📑 5 | [⭐ 107](https://github.com/Jiaaqiliu/Awesome-Training-Ecosystem-for-E2E-AD) | Autonomous driving is a cornerstone technology for the future of intelligent transportation, where end-to-end learning has emerged as a transformative paradigm that directly maps multimodal sensory inputs to driving acti… |

## 3DGS / NeRF Reconstruction & Sensor Sim

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DriveWeaver: Point-Conditioned Video Inpainting for Controllable Vehicle Insertion in Autonomous Driving Simulation](https://arxiv.org/abs/2606.31918)<br><sub>Junzhe Jiang, Zipei Ma, Zijie Pan et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 16](https://github.com/LogosRoboticsGroup/DriveWeaver) | A pivotal step in autonomous driving simulation involves inserting foreground vehicles with predefined trajectories into simulated scenes |
| [Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796)<br><sub>Leshu Li, Jie Peng, Yang Zhao</sub> | ICRA<br>2026-06 | [⭐ 14](https://github.com/UMN-ZhaoLab/Pocket-SLAM) | 3D Gaussian Splatting (3DGS) has garnered significant attention in Simultaneous Localization and Mapping (SLAM) due to its advances in capturing fine-grained geometry features and synthesizing novel views |
| [MM-TRELLIS: Point-Cloud Guided Multi-Modal 3D Vehicle Generation in Autonomous Driving](https://arxiv.org/abs/2606.24301)<br><sub>Hongli Xiao, Youjian Zhang, Yucai Bai et al.</sub> | ICRA 2026<br>2026-06 | [⭐ 9](https://github.com/HongliXiao/MM-TRELLIS) | Recovering realistic 3D vehicle models from autonomous driving scenes is crucial for synthesizing training data and building simulation environment |

## Perception: BEV, Occupancy, 3D Detection, Mapping

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Deformable Gaussian Occupancy: Decoupling Rigid and Nonrigid Motion with Factorized Distillation](https://arxiv.org/abs/2605.28587)<br><sub>Yang Gao, Wuyang Li, Po-Chien Luan et al.</sub> | CVPR 2026<br>2026-05<br>📑 2 | [⭐ 22](https://github.com/vita-epfl/DeGO) | Understanding dynamic 3D environments is essential for safe autonomous driving, particularly when reasoning about human-centric, nonrigid agents |
| [FreeOcc: Training-Free Embodied Open-Vocabulary Occupancy Prediction](https://arxiv.org/abs/2604.28115)<br><sub>Zeyu Jiang, Changqing Zhou, Xingxing Zuo et al.</sub> | RSS<br>2026-04<br>📑 6 | [⭐ 142](https://github.com/the-masses/FreeOcc) | Existing learning-based occupancy prediction methods rely on large-scale 3D annotations and generalize poorly across environments |
| [Horizon3D: Sparse Radar-Camera Fusion for Long-Range 3D Perception in Autonomous Driving](https://arxiv.org/abs/2606.31096)<br><sub>Geonho Bang, Geunju Baek, Dongyoung Lee et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 24](https://github.com/geonhobang/Horizon3D) | Long-range 3D object detection is critical for safe autonomous driving at highway speeds, yet existing radar-camera fusion methods remain limited at extended ranges |
| [Explainability-Aware Frustum Attack: Exposing Structural Vulnerabilities in LiDAR-Based 3D Object Detectors](https://arxiv.org/abs/2606.29963)<br><sub>Chengzeng You, Binbin Xu, Soteris Demetriou</sub> | ECCV<br>2026-06 | [⭐ 2](https://github.com/SecMindLab/Saliency_LiDAR) | The structural vulnerabilities of point cloud-based 3D object detectors remain poorly understood |
| [PointLAM: Local Attentive Mamba for Efficient Point-based 3D Object Detection](https://arxiv.org/abs/2609.21780)<br><sub>Xuanming Shang, Weijia Zhang, Chao Ma</sub> | ECCV 2026<br>2026-09 | [⭐ 5](https://github.com/PointLAM/PointLAM) | 3D object detection from LiDAR point clouds faces a fundamental dilemma: voxel-based methods achieve efficiency at the cost of geometric quantization, while point-based methods preserve fidelity but suffer from prohibiti… |
| [UniD-Shift: Towards Unified Semantic Segmentation via Interpretable Share-Private Multimodal Decomposition](https://arxiv.org/abs/2605.07356)<br><sub>Shuai Zhang, Zhecheng Shi, Zhuxiao Li et al.</sub> | CVPR 2026<br>2026-05 | [⭐ 5](https://github.com/shuaizhang69/UniD-Shift) | Semantic segmentation of large-scale 3D point clouds is crucial for applications such as autonomous driving and urban digital twins |
| [Vernata: Self-Supervised Learning of LiDAR Point Representations](https://arxiv.org/abs/2608.06919)<br><sub>Oliver Lemke, Alexander Liniger, Abel Gawel et al.</sub> | IROS 2026<br>2026-08 | [⭐ 22](https://github.com/rai-opensource/vernata) | LiDAR serves as a primary sensing modality for robots operating in outdoor environments |
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

<details><summary><b>Waymo</b> (214)</summary>

- 📝 2026-10-16 [Hello Toronto! Waymo is En Route](https://waymo.com/blog/2026/10/waymo-in-toronto) <sub>official blog</sub>
- 📝 2026-10-08 [Sober Drivers Still Face Nearly 4x Nighttime Risk: Why Road Safety Demands a Safe System Approach](https://waymo.com/blog/2026/10/sober-driving-benchmarks) <sub>official blog</sub>
- 📰 2026-10-17 [Waymo launching self-driving taxi testing in Toronto](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBFX1Rld2d4d2xSVXBFZ091cjNGSHF6aHRwZWR2RndaNkVPZHpOR2FJYkY5WlBkYVVsVThvUW83N0hMZHV0dk9DcG4wN0pCYS0yMURFN2lseHhhQQ?oc=5) <sub>CBC</sub>
- 📰 2026-10-17 [Man Gets In Waymo. Then The Self-Driving Car Gets Pulled Over: 'Who Even Gets The Ticket?'](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE51b3g3bVJ3b2x5X3ZZdWNjRGJRX1A2WWd3d1VwazZ2dEFiWFRYSmU1bkVmQy04V3JPaFUtSHZxbWpFWUdBanRZdW1lNU9NSkVKQWZDWXVDQ25mX3ktYUZXQ2RFX2VoV0U?oc=5) <sub>Motor1.com</sub>
- 📰 2026-10-17 [Tesla Just Won in Court: Self-Driving Buyers Can’t Sue as a Class](https://news.google.com/rss/articles/CBMiqwFBVV95cUxNUkpaYWZsQzhlMkI2R3Y3b2VVZjlrWk45d0djenY5TkNmRzhpNG05RjhMZmY4aTFHSkFaTl9QMk9aYm9WRmdtRV9UdFRGczJ6T011Qm4zekhSUFREYXM0Z3UwMnhfYmdRT052RWJ0MWJOUkx6dW9NZnNUUFdfdWlsSTdvSF9PaDlkdmhiSDlGVEt2LXRhOU1aRlNlWkkwdHdQcnlRcXJxcEJyZjQ?oc=5) <sub>24/7 Wall St.</sub>

</details>

<details><summary><b>Tesla</b> (352)</summary>

- 📰 2026-10-18 [Man who's used Full Self-Driving on his 2025 Tesla Model 3 Highland has taken 50 people from his village for a ride and they've all had one common experience](https://news.google.com/rss/articles/CBMilwFBVV95cUxNUXdReEROOC10NlZrNUU0MHZ0X05YUEllMm90d2lIOGtKT3JpMGJnUlBEaGp4TjcydldPUzRMTGtmSFRpdEh3cFNick8yWDJiMGZyOGtZdFJ4bUtNUUdWQ3hxSFRHd0lhT3VGVFpSbmVQdjFjYjhBczE3Rnc3OGJLNmNHeFpERVN3VjNOUWtTdHJfTllfUVpj?oc=5) <sub>supercarblondie.com</sub>
- 📰 2026-10-18 [49ers' Kyle Shanahan plans to coach preseason opener, learned not to fully trust Tesla Autopilot](https://news.google.com/rss/articles/CBMilAFBVV95cUxQZUg3V2l6SUUxaXlTRDlINnd5c29VTEctOTIxZDJqeFduWV93X1A3MU43VzRUUElWX2dTWktNX2J2eV82cUo1Q01BVHNSVmZfNG9SYm00Z1MwWnk0WTJoQ1VMRE02a0EzZFdFREJvRUhUUmZRUUQ4U3lmLVhrVXFtV3FrNlpCQXhjRU5sbjBxV0hlTnBI?oc=5) <sub>49ers Webzone</sub>
- 📰 2026-10-18 [【网通社快报】新款特斯拉Roadster将搭载受限版FSD](https://news.google.com/rss/articles/CBMiTEFVX3lxTE92cDYzNkVFaFhwdWVGblZRNlFSM3RIRmJQSEg1SlQ1SkhOUV8wRy1YZ0FxcHVxUkxDRWJsLWxvd1pReU8wczF3N3ZpNkI?oc=5) <sub>凤凰网汽车</sub>
- 📰 2026-10-18 [美国一男子打开特斯拉FSD后睡觉 撞上执勤警车致2名巡警重伤](https://news.google.com/rss/articles/CBMiWEFVX3lxTE1pZ25ndUI0a1dSbXJ6RzFkcko5aWlUNGlWZ1hDcHU2UTNSSF9HRDBGdjZTNDU5dHVxUDhxcmVGS1lSbC0xZ3BIaGVacG5XdkZGcWR4RzAwR1Q?oc=5) <sub>驱动之家</sub>
- 📰 2026-10-18 [特斯拉延长奥斯汀Robotaxi运营时间至午夜，FSD v15将支持全天候运营](https://news.google.com/rss/articles/CBMickFVX3lxTE1ldG9rTHNWeHVHQWFhMEFJRHd0eXNQekJQRWQyTVZKOWhBeGJ6ay1QOWJOZmtXV2Fzb2s5TC12UDhhZEZWVWF0SHlWMU1UZS1pYjBMeFU3WVNOa1RyZXpMUnlzSjlQdzItbS02Rll5YzZXQQ?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>NVIDIA</b> (224)</summary>

- 📰 2026-10-17 [NVIDIA's Jensen Huang: AI Market Volatility Will Subside as AI Drives Transformation](https://news.google.com/rss/articles/CBMiuAFBVV95cUxPcXh5eDBOVkdpNWN6N3BnUjBaTE5SR0l4czZ1bE5aTHNqY2g1c2cwbmdYVnJ5a2ZfdENaWjVMUXgyckRnVFRxRi1OYXpFbzZGRmxRNjVVT2VicTM2cGdDRmZydzR1d1pVNGxJUUZxNzZrSFY1bndZX1FObUJ6VGx4dWdDN252dy1aa2Q4UEgxV0xfZUZaRXJmeW5aOWRCem9sU3lGTWRVbjlzRGQ3cjJXc0FYTktpVW5r?oc=5) <sub>KuCoin</sub>
- 📰 2026-10-17 [Nvidia, Mercedes-Benz Expand AI Autonomous Driving Partnership](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1BRTQ2SDZDVE9hRTN1Xzd1N3QyTFRLYzByTktVZXl4dm92bjNWb0V0SXBXLTB5RENYOEhaWnVCVVhGTmV1LXIzQldyanhZV0lYdDlYd05LTmFTczZDZVlsX1ZLNHoxWk0?oc=5) <sub>THE ELEC, Korea Electronics Industry Media</sub>
- 📰 2026-10-17 [Volvo bets on Nvidia for eyes-off driving, minus the lidar](https://news.google.com/rss/articles/CBMiggFBVV95cUxPMzQ3d1hwQWVUc2hqRl9xTU5mcUNpUEIzWDV4ZldpT2o2VEZ0NVF3dHhfOVRQRFpXRk9wbzhLRllBSkRrZFROZU1ya2hVMkIzQ1c3VDBIdGpOWDE4OEhIcUZHOGhnNDFaTVZQSEN2R3ZOU29tODBGQlZpLW1CTWhKOVFn?oc=5) <sub>AutoNext.co</sub>
- 📰 2026-10-17 [The FPS Review Weekender: NVIDIA’s RTX Spark Laptops Are Here, and Reviewers Like the GPU More Than the Price, Plus 10 More Hardware Reviews](https://news.google.com/rss/articles/CBMiiAJBVV95cUxOV1lQNFVHWkg1bnFqdEJubXRtMHUwTUd0S3l5aFlVV3ZCcnB4eGZjb05IaEp5QVdxMVFmNTlhQi1pMklZVVJkUzBwdEVLMmZ4c2VaaG9CcFJ0S1NuS1RIbXBDakk3Uy1YMDQzdWtHS3duY2s4aFdIZ3FFSDB2U0FwMkhpYkh5VERzSjZ4dnVwRzBvOUVvZjMxVjRMMTFmb0tBUGlqXzE4LUwtTlFCb3Z5R3dRbmpLLXR1VFRJNUpkMFEySEZjLV9aMEVwNlRieGNwWUljTi03cHB5eW5UZE52Q2c2ekV2LWczdnU3VlFINElpN2hGSFphZ0ZXaHR3aC03UG1JUFExdjE?oc=5) <sub>The FPS Review</sub>
- 📰 2026-10-17 [Mercedes bets its self-driving future on NVIDIA, and Level 4 is the target](https://news.google.com/rss/articles/CBMivAFBVV95cUxQSWtRZkRwYUYta2VnVGhockF4WnQyQlQwNFI4ajJDVzFibFI5T2Y2SmRFdkNnSFV6bjFwQTlSbXJuRElCdEdReVVYLTNBdDlsUEQzc3RRWGhkR1RldE1ZS2xKV0w4TjBTNmcxUU1zQmZvTzRJLVFyUUctbDByRXFlNnBBTFlFVHhXUVo3c21pNkpaUjFkenBnYUhwQXRsejdWUGFqb0VibmZaYWhOLUwwU0gxRmxTX0hxdGJaVg?oc=5) <sub>Absolute Geeks</sub>

</details>

<details><summary><b>Wayve</b> (64)</summary>

- 📰 2026-10-17 [Protesters call for London robotaxi trials to stop](https://news.google.com/rss/articles/CBMiXkFVX3lxTE9LMjQ2Z1pqdXk3aWV2a3g0OUs1UTI4N1dwRS1Dd08xZ1QzejZrRWNkRkxvckFYdjZtWVhFZmRMR3BIUzJTRWxPSTZnaUsxanpqV2o1aExUbnJKNE9IWXc?oc=5) <sub>BBC</sub>
- 📰 2026-10-16 [‘We should all be worried’: calls grow to limit London rollout of robotaxis](https://news.google.com/rss/articles/CBMiqwFBVV95cUxON184ekxIVGM5blloZ0xnMDRkSk1EejBQZktheVB0ZFJDYXpDRnd2MjM2YjlTWE5ZelR5YlhRUTUwc192dGxhSmd4VEowMzc3aWdIMXlUVTJUdjRzeVQxcG54SGl2VWtKZ2ZfUjFfcVAtRkZBSEh5Zm9QdUh4c0VfRG16RU15N1dDeUVCQ3NMdWNzYVVPUlYtemxJMWtqWVBya1RTSE5TVW02NXc?oc=5) <sub>The Guardian</sub>
- 📰 2026-10-16 [Drivers union advocates for lifetime basic income for private hire drivers in face of robotaxi rollout](https://news.google.com/rss/articles/CBMiyAFBVV95cUxNYU8tSWNISFRCcW9PY1F0eXhPRFFlLVZQS0xzVGNpZ3VZblJkN1NpbllxWHZKUUhXYTdueHp5OVZVY2tJRGVueV9xZ2kwdkhmMEd2bXFhVWNIZVp1RFExSjQxXzFuTHduTExRcU9xNkpBcjItSmdNY2I1RlI2bHJmQUN1bWd5dGcza1BUR051OExfMXNFRVhrTlBvLVNCeC1QRGhTcTNvNnZMOTBPdTFRTWZWZzN0Z3lEUER3cUt5R2ZKRjZOVDlIQg?oc=5) <sub>Highways News</sub>
- 📰 2026-10-16 [Mercedes-Benz and NVIDIA expand partnership to develop next-generation autonomous driving](https://news.google.com/rss/articles/CBMilwFBVV95cUxNQjVOaEJNSERlTFpZWHAxaW1HR2Y2NUk5VjhUUEh6UVlod25yUGw2dWlLMnpBMWoxMlE0cGVUckl6OXZoSTl3Zm5wV0dEWU9IMk55SmRLZlFUU1Q5Qlo0T1o2Q1VJTTVmdG9iRXJkY1FDR0hiMGZvMzl3YlQyVGR4TUlSTlRRczg2MFZqS1dPRXBlS2RFdDhn?oc=5) <sub>Drive Tesla Canada</sub>
- 📰 2026-10-16 [London robotaxis face political and driver backlash as Uber and Wayve expand UK rollout](https://news.google.com/rss/articles/CBMivgFBVV95cUxQMS04RW9NUDlrdWtObzhfc2pIZUs1b1ZkUWVfNnl5N3pXUkZIZHh4bEJMNllSM2VDTEtkdlBraWZHdjlHRUxZbTBUZHViZ3luS09fZk5KODZoSkN0UEFyaWVxc1ZPNkxWNjZDVnNpVDdPMHAzNkZ5SEJfLWU5cFlvbjVLc3FrVXcyU0VONGJwYUUwRjRHN1R2akpYWXNqa19jYlZmZ0dWcVBYRElSVy01NnhfZG82Yi1ZOFFkUVJR?oc=5) <sub>https://streamlinefeed.co.ke/</sub>

</details>

<details><summary><b>Momenta</b> (84)</summary>

- 📰 2026-10-18 [智驾好的车推荐哪几款？2026实测榜单+分人群选购指南+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE96Z3RxWEQ4YXpPMTY0NUlhbkprcmhYaWlqLXMzZzFvenBkSlo5RTdHMllqdzczRy03V2JLOGJFODBtM2tWUGdYZWdsT0NOS3hpbXBUNzFibjlXc2pvR0NpajE4WU9DdDZCUjB3OFJmc3JfZw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-17 [Autonomous Driving Faces Arc de Triomphe Test](https://news.google.com/rss/articles/CBMikgFBVV95cUxNeTV4VWZraWg3bG1PRFN0VU5zc19sZkRla01ZeTl2TzMwVm14MlhaMV9VM3pwOHpvd2gwa01OSGgtbDVQNWlKUnI1TXZaeG8yV2x6RmI0SmtMUTJmQllwTmZpOVRYRzNWcE1VSEZreElkem03OTJ4VWNaN1RyMTA3WWROSU9lS2VlWXNXaTFEcllZQQ?oc=5) <sub>Briefs Finance</sub>
- 📰 2026-10-17 [XHEART Completes Strategic Funding Round with CXMT, Renault, and Chery as Investors](https://news.google.com/rss/articles/CBMidkFVX3lxTFBuY3ZLbVhWemprZU45MXpMaXdJWlJ2a3ZiMXdGekg5WDY2a2ZabWdtTkYtd0dCR3Awam5PU01oek5mZTlyLXdUWWxGMERlTVFqMVJWMlY5TTQtSHdidlFXRG1NeERCMzhmZWZabFFiMENiVU02WUE?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-17 [东风风神L8+将于10月23日上市，搭载Momenta R7世界模型\|插电混动\|智驾\|东风l8\|新车\|小桌板](https://news.google.com/rss/articles/CBMirARBVV95cUxQMWtVWVEzLWlYVTdadlhJdTVBNWZWUS1ULUtmYlFtQlF4WHI5SjRRMjhndGJyQ25mMjFaeDh2U1EyUktWd2RTcWUwb01RYk94NHkzREFfNFpzTGZoTXlSSm5TY2xwdHloaE44Mm5qSkhQczdCUk5MY0pjV29jUWFtcnlURE1od0d2R2JoenZCMlJraU8ta3ZDbGpxOEpndXZaZDFaTmF2bmI0YmtKaF91YjlWMjdlMFhtR24zdld1MVZndnNVYlAyUFVXeDJDSGtfajAyVlhBWl85dXViLW5hR1lzeWxxLXhQN1RxZnk5anhyOVZsTEI4N0UxcDBVNnNyR3VaU0ZBbkY4eUZLa2h4YXRwOEp5dkE1MWNza2hkcmtKbF9tUE5idGo3RTJHM0ZYRzFZcDFkX1VBbE9tbXVJcE1TZS1SblZiaWNqRVY3VXoxTUZpWjU3NzNvYy1YNndvRHNHS0VDN3NzeHZ5LWxoTmxWRU92YTFiU0VSUHJEVjFzMF9LX3g5RnFBRlRHc3A0MlpjOFVmaTJJY2QwVjd4b3prQ3RMUHhWSTlPc0R4TU1GNkstWmp2Y29KbHlVMWRLblRIYzRLbjlYN3pfWjczZVJZZEhvdDZiUURUU1NRaVBxOS1HSEMxa0ZVaG04MmpEdTc3Q0Z5cnN6UGpqVmNneHVMZDlfbzJZSURERGdlcjlyeG0yTTY2VHp5UWcyNGg0NWNNZkJYOVJRMGww?oc=5) <sub>finance.sina.com.cn</sub>
- 📰 2026-10-17 [【联合征服巴黎“最难魔鬼环岛”：奇瑞 JAECOO 联合 Momenta 完成首个无接管凯旋门智驾挑战】测试车全程经过复杂路况，成功完成无接管挑战，展现出优秀的智驾表现。后续该车型将在测试后正式与欧洲用户见面。#奇瑞智驾挑战# ​\|Momenta\|奇瑞JAECOO\|凯旋门\|智](https://news.google.com/rss/articles/CBMiY0FVX3lxTE9pU2t0QlJ2N251cDVpVGgzRFl4bnQ3dy01X0I4c0haa0w2aGY4ZjNJaWNUam4tMzQxZm1mYVRLTTkzaUQyVE1UaG53S0UtMFZ0U093RXVNNEd5c3hoTm9KZ2F0WQ?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>XPeng</b> (308)</summary>

- 📰 2026-10-18 [23万级增配不增价：小鹏G9L、理想L6、智界R7、极氪7X新上市大五座横评](https://news.google.com/rss/articles/CBMickFVX3lxTE5oWkgtSkFaRnQ3MlBMMV9JeTM4a3ZsUk9sWXNlazlzUVdjY29HeVFGQS1XMWFPaFVsU0FXQzN1NWdxaFYtZGZuelh2WENxQnRmd3g2Wko4MDdRRG42TmM0UVZwVVktU0Y0ZDBfYkxDT0RVUQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-17 [25万预算新能源SUV横评，小鹏G9L与极氪7X、理想L6、智界R7怎么选？](https://news.google.com/rss/articles/CBMickFVX3lxTE0tZmZac3dzbWhBVVFubG5hc0ptMG5EUDFsRTZldWZzOUthTzgtQTdGMjNMSmkzTWZUdi03TXI4TV95YmxQVndiM0x1M1otMDF5Vlh6VjFDS2xKOXpJcXZ2WXBpWmtSdnpnQnFwa3dHRktEZw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-17 [充电最快的大五座SUV横评：小鹏G9L、极氪7X、智界R7、理想L6谁领跑？](https://news.google.com/rss/articles/CBMickFVX3lxTE1aMjNnc2poM08wc3d5UVBhTUFHZGY3VDlXR3NXMjFEc2c5cG4tcVU1THJJRVlQcmdrc2h2bEZudnMwV2dnWmg1dUNFLTl4Sm5oaThoeDFuR1hzUm50d1pIenV4R0xINUlRNlR4clYxLUg3QQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-17 [小鹏扛鼎之作！GX无伪装实车曝光，配22寸轮毂+悬浮logo](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5FdHR4eVVaaFVwaTZUNE1JZERobkY3dS1hZ1ZwUC1SSUsxNUNhd3hkQllFRlEtbmxwbVVmejNzbm1pd0QtbkRsT3lSdURieUNDLWloYjJCV0RIT2s?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-17 [智能大五座SUV横评：小鹏G9L第二代VLA全系标配与智界R7、理想L6怎么选](https://news.google.com/rss/articles/CBMickFVX3lxTFBnTGVkUjlkalgwdFZnc0xMMVhzNm5RVS0ycUU2MXQtVFZLc3J2Z2lPanpKX25MWUlxUTZsNHFVVjhCX2ZpQnJEVTZ6MW44UXVaZ1BrTEJRSGJXc0k5R2Z5RmdOUVNoQ2FuLTd3N2lzcndlZw?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>Li Auto</b> (144)</summary>

- 📰 2026-10-17 [全域全能还是城市专精？神行者8、领克900、理想L8三车横评，30万级新能源SUV选购指南](https://news.google.com/rss/articles/CBMickFVX3lxTE0tMGhGWDhDcV93U25JMTZaU0Z2N1hsYm9xNGlRbFVDV19vMGd4Q2hObW1manJuYUhSYi03VEZNYV9xMDZUU2xmOGNSUUdSTEVXdWx4bFZzZDcxb3o3Umx6eV9jQU82X21BXzhPRERCZ1ZUQQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-17 [领克900、理想L8、智己LS8与神行者8同场对比：30万级新能源SUV的“全能选手”终于来了](https://news.google.com/rss/articles/CBMickFVX3lxTE5IbXcwd2NTU21yTDJDZUh1Z1A2QWdyZVUwODBjMEY3dnZCcVBqRVJ2VVBNWUlNVkdOV0Q4ZG9qUDA5U3owTDZHYzZQLWxZX2RuZzhIeGdpUDM2T3JmVDI1a3MtOWVKc2JpaVZtelloa3Vwdw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-17 [一家五口出行SUV横评：小鹏G9L、理想L6、问界M7，谁的二排更懂家人？](https://news.google.com/rss/articles/CBMickFVX3lxTFBEYjUweklpSV9qV0xWODM3R3lPLWs3VDg4OWJTQWFaUmlXS3lCVVJaQi16aDd3dHFHNzBJbzJNRUZTQzFMdm5ydnVjYk1BaEs5WUNFenJ3MkJMN0ljQndfUnp2UjUxRDlNc2tNbzV2QzdVZw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-17 [理想高管评价特斯拉：FSD稳坐智驾第一梯队，Roadster却“面目全非”？+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE04NUk5cVVNczRZbmVUS01iNzlpMWp4LXN6aWEzRUxRV2pIaWVpcld0OVoxVXlKVnZoNUZFckNLUTNYM0loXzJuZFZYQTlqdFF4RjJNUW4zc0JlVzRRUm5HTzJfZ2VHSzFyRko3cHBhRFJ3Zw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-16 [Gasgoo Daily: Geely Partners with Google; JAECOO and Momenta Test L2++ Driving Tech in Paris; Li Auto's Chip Unit Secures Funding](https://news.google.com/rss/articles/CBMikwJBVV95cUxQUWROZVdTOWpFT2xkUm0wT2N6d2pOUXlaSGpENzRJRTdoajh2TUVaT2t1NlZBNVFDRGd0dUJBZE5UeGw4SUZzWnc3XzgtbXdWNkFwSTZjUkkyME9mdGFRMHdGZlVEMm9WU0xwMjJmUEdlclc4cURTUHVvZC1FYTdTQW00NUJUc3RNM2o1TGtfYXdsVkxVX1FqUGh3OUJEYjhWUktpSlVpRFhvNHVVNHRYeDVRSFprQm0tRjdSRVlQYUlZOVhLN19HOGN3NVJVcXhIazFFMGlDM0Jmb0NheTI1X2g1SG80Wm42N0dXdVNvc3dmT2QwdW1CdzNnTVFmQjdzdWpIUU9SamJfSjN6b2hyZlQwOA?oc=5) <sub>Gasgoo</sub>

</details>

<details><summary><b>NIO</b> (145)</summary>

- 📰 2026-10-18 [Even if those new Chinese EV automakers dare to sell their technology, who on earth would dare to buy it?](https://news.google.com/rss/articles/CBMiU0FVX3lxTFBNOWhGbmhlR0MwS3dEbkFTUzN1azJGMUFMbW1vc3JPclRoLVlPck1pSkpUbEJOTE1pdDhGd1VUQjd5NVl1VFNpaFoyUlQtSUpNWU1j?oc=5) <sub>36Kr</sub>
- 📰 2026-10-18 [蔚来ES6 2026款33.8万起，5年换电老车主说真话：值不值？+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE1adzhQX3pmbGRjNnVZWVBoS3dCeHd1U2R3RU9iaXdHNFd3SlFTdlkwRjBQcUdpTU5nSlR5RC1BaXlaMFNnaXVzdWlRMnltXzVvdjVCUm1DNkFncFFIeElNZTVGS0NtQ3N2SUVPRlZXaU12UQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-17 [小鹏G9L对比极氪7X、智界R7、蔚来ES6，底盘操控谁更扎实+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5nRjBPV2NzU05FWTd5Q0tRbW5QNUFvMl9ScGtHSXBJRVJNMnZlU1k3UVctSTJfNU1TUTYyRXZkclpsWHlEcEtwR1N6bEpyWXo2OWlRSm1VZV9renRUazZR?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-17 [大五座SUV操控横评：小鹏G9L、极氪7X、智界R7、蔚来ES6底盘谁更扎实+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE9fWFBYanVzYWJiWl9pSkZHSXlUWExLYVp5dDhkcHJnczFxWTVmUmd3ZU1oQVdhdjhwSXNFOUZRcFg2aFpTaUQ3VTF4aE1xaUZLenN2dnBfREdUZHZWQnhTdUJIRFpldUhrdU1kb3NRVDg0dw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-17 [XHEART Completes Strategic Funding Round with CXMT, Renault, and Chery as Investors](https://news.google.com/rss/articles/CBMidkFVX3lxTFBuY3ZLbVhWemprZU45MXpMaXdJWlJ2a3ZiMXdGekg5WDY2a2ZabWdtTkYtd0dCR3Awam5PU01oek5mZTlyLXdUWWxGMERlTVFqMVJWMlY5TTQtSHdidlFXRG1NeERCMzhmZWZabFFiMENiVU02WUE?oc=5) <sub>BigGo Finance</sub>

</details>

<details><summary><b>Huawei</b> (352)</summary>

- 📰 2026-10-18 [Ex-Huawei Automotive BU Global Foundational Model Team Head Launches Startup: Hangzhou Embodied AI Brain Firm Secures Nearly ¥100M Financing \| Hard Krypton Exclusive Premiere](https://news.google.com/rss/articles/CBMiU0FVX3lxTE00UmNTRDJYNFJ4NG9Ca1RCTTAzMkZvTW9pLXFtSk9icXh0R2lnTF9ERHJwb2tnNUkyZThOMFlsR3F4TGwwVkJlVm9wZXItT2tBMVNJ?oc=5) <sub>36Kr</sub>
- 📰 2026-10-18 [This wide-screen Huawei Pura X View lookalike runs Android out of the box](https://news.google.com/rss/articles/CBMiogFBVV95cUxPU3QtSWlkaXpqRnpnV0w4SDJJbDNsbFVoMVBqRVluUmFaRmczWFV2WWliU1UzcWh4TnlreGk1WDdtOWJRZ3Q1Q0o2NDZ1UWV5X1UzTHZpMThtaFlDUWJEM2xjNVNKSHoxV211dGlmMlRKa3k2R2lFYk11Sm9IYkJTRThmY25uQ0Joc21sZEFMdVFjdk9GYkUwbG9zU0NETkhOblE?oc=5) <sub>Gizmochina</sub>
- 📰 2026-10-18 [【视频】29万起配空悬+华为智驾！岚图泰山X8选购指南](https://news.google.com/rss/articles/CBMiakFVX3lxTE1OWi1iMzNETER3V21yX3hsUjJxaFhWSVZxb1JrbW93Z3JXa1lMbWJlLVR5OE1CMzRsZGlIbTVLTGdBSVVFU2w4blUzMlFaeWZOX296S1F1QXhya2gzclNKOWZSdGFtQUVMR0E?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-17 [奕境X9纯电版申报图曝光，双动力矩阵落子，11月见真章](https://news.google.com/rss/articles/CBMia0FVX3lxTE9EUnRXZUxwTV9lY0lUZmNaVWNjd2lTNHJ6NnhZR21GUVNOR2JoR1dDamxEeE1RZkpjNlJ0bmphbkR4OG9zdDZsa0pWalAxWmpLZVdlYlhJbFlYRk9kZW52bHZ0b1RWMTJOcTVZ?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-17 [【视频】10万买华为智驾六座SUV？星海V6真香还是噱头？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1kUnFwQzJ6bDlxemM2SHRPWnpVTWlWdmViQmUwNzYzUEt3eERIN3VmMTNpM3l5NFlUVmZ6Y0xKTWVjSVQxbFdaYWJzb1NPUWY5Q25uSjdFcktpNnM?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Baidu Apollo</b> (53)</summary>

- 📰 2026-10-18 [Seoul taxi overcharge complaints by foreigners top 6,000, few acted on](https://news.google.com/rss/articles/CBMiugFBVV95cUxQcEZXRHVkMXg5Sy1yNXNsZXNEWXo5X0hDemZkMERmYzM0ZkIzQ2I4bndEZWFRbjRGV3B1Z1BzNFRtT1NvbGJrSG9CTEltRGF3V3ZGcWhLakI0My1KVGNLcHU0YnRGNlpmbHVhcWg1ZWtxOXl2LUR0ZmFGUlgxWkdWM2gzcXdTYS1hT182R0ZSZ2hFOUlIVVU3b2FlVGx2WG5wZTJFZTlQaEdRN28tc0p3MXZQRDdPM0Juemc?oc=5) <sub>Korea JoongAng Daily</sub>
- 📰 2026-10-18 [钰见雄安Vlog \|在雄安体验没有司机没有方向盘的车 你的出行，自动驾驶来接管](https://news.google.com/rss/articles/CBMif0FVX3lxTE4zMXFWSUZQSVB4TGhtXzRweXdJbmpKY1JnR1dVVG1YLUt6bUhXTXViMmhEcGNuMmpSbHdFdVFRbkNnclV4QnJ6Qk9GbmdmX19NeHVfZG0yTzBpMHYtekY2NjZNSlFNYVV3aENaVWFqUEV5bHNOT2dDcFRDVWdSdHM?oc=5) <sub>新浪网</sub>
- 📰 2026-10-17 [科技早报 \| iPhone Duo首批现货最高涨7143元；长鑫科技预计前三季度净利超1300亿](https://news.google.com/rss/articles/CBMiWEFVX3lxTE84Q1BrQ3hBT3k2VmlQdmZtMDBXN0xvcUpkT252WElIRmNNVlQ3YktOYzlrTWdkT044ZWNkUXEzMnNkbGVfNnJWakp3WUFHYmFJdklyaHc1YkY?oc=5) <sub>Jiemian.com</sub>
- 📰 2026-10-17 [Croatia Robotaxi Goes Driverless: Pony.ai Hardware, 22km [2026]](https://news.google.com/rss/articles/CBMigAFBVV95cUxPbXpWaW1YYXplbkJnTzFEYV9LVmpRT2lvY0dxMmNkakw4OWNJQzVNVFpQbW55SUFhT0lvUGNsaV8zY1VUdUhmem52LUtRZl85TXBDaFVDc0U1UGc3Rno1SnQ0Z3hwcDJlNEpWQ0hZV3lRT1lDTDAxbGpjUlhNWV93Yg?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-10-16 [Baidu opens Tung Chung robotaxi public trials](https://news.google.com/rss/articles/CBMifkFVX3lxTE51Y2F6QXRJd0JPaVBydjNhVXBhQ0o1UnNHWjd6RTZDbl9VS1RraTE0dkhlRjEwRHlCR2kybFpOLS11LVBnbkRIaHdXYjdGZzhGWVk1TkVJQUJQOGhyNnNIUGtBaXYzZHFwU0tHem90dmZuWVhkZkp4azN5ZWZUZw?oc=5) <sub>Dimsum Daily</sub>

</details>

<details><summary><b>Pony.ai</b> (145)</summary>

- 📰 2026-10-17 [Croatia Robotaxi Goes Driverless: Pony.ai Hardware, 22km [2026]](https://news.google.com/rss/articles/CBMigAFBVV95cUxPbXpWaW1YYXplbkJnTzFEYV9LVmpRT2lvY0dxMmNkakw4OWNJQzVNVFpQbW55SUFhT0lvUGNsaV8zY1VUdUhmem52LUtRZl85TXBDaFVDc0U1UGc3Rno1SnQ0Z3hwcDJlNEpWQ0hZV3lRT1lDTDAxbGpjUlhNWV93Yg?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-10-17 [Dongguan Binhaiwan Bay Area, Pony.ai deepen intelligent connected vehicle cooperation](https://news.google.com/rss/articles/CBMiZkFVX3lxTE5MSkNiZTNwNDd4VEVMdkRNYldUZGt1dkFycWRMdFhqZzh3UG01ZURyRjk4SDFyQ1JOVHAxclJCVFl6U2hrdHRVN1V6bm9Mc0c1VmtvQ09pRjlwWk9iN21fa2t1YzBJQQ?oc=5) <sub>Guangdong News</sub>
- 📰 2026-10-17 [Croatia trials full driverless robotaxi service powered by Chinese firm](https://news.google.com/rss/articles/CBMiqgFBVV95cUxOREV5OUU1cU1PdmVPX0FqNDk4NkpZa1B6MTB0eWxMdDhhWlVRUDNUTHZwaDVNMnZIU0NZT3d5YUtqV21Kb19BQVN5MFZ5YjJwbERkQ2FsY0VacnBVb0pSblJkbXFaRUM1UjB5SVRBSmtfRlduVFFqYXBQZlBMOXRkZTVKRnIySVlvc2JEeGVuWUF0aDdKQ3IzWU94NGs1c1NYeEh1cmlxb2dVQQ?oc=5) <sub>CGTN</sub>
- 📰 2026-10-17 [正片发布！广东10年育出自动驾驶第一梯队](https://news.google.com/rss/articles/CBMib0FVX3lxTE8ybmgxd2pZM3JsWHVqejV0MHk1cjhjd2E5NWROUUNkaDd1X2h6dTM0WGRpa3hjUFZKemFnQVR2Nl9SZ29adUNDV1RBT2NlNXhRZ25vMWNqbG0tNFM2T3pQcV9lR3lWZWFHZ0k0cHFYYw?oc=5) <sub>新浪财经</sub>
- 📰 2026-10-16 [三部门调查尊界刹车踏板断裂，港股通汽车ETF易方达涨1.44%](https://news.google.com/rss/articles/CBMijAFBVV95cUxNdWZnbG9mRWZ1YjRNdTZFMnA5ZTh2Zy1JcHVEd2VWNlRvNWIybWtHR05ic1FDSlpOaG1LQ1pBdUV0aGllMTBlbFFBakRuMEJPOGU3a1pZQi1VNl8yQmVsU1puVDhUWFN0eU5OWF9wdlZLcTdIQnJnOFdvVG5kcWNJVC0yelpRZC1lRV9OYQ?oc=5) <sub>搜狐</sub>

</details>

<details><summary><b>WeRide</b> (155)</summary>

- 📰 2026-10-18 [预售12.88万起 AION Ray7开启预售 192线激光雷达/纯电续航702km](https://news.google.com/rss/articles/CBMiYEFVX3lxTE94Wmp0dUJpVTUzTVpxdlVjVzVmTThYbnp1OGl0VE9ZNWFrR2hSTFp3cFFsNGM4dWNkdE8ydDcwck1UZ29SRUo1TFBkTkpXS2RjaFFFY09VMHlsUjJhWW5rNA?oc=5) <sub>太平洋汽车</sub>
- 📰 2026-10-18 [广汽埃安Ray系列首款车型开启预售，2小时订单6817辆](https://news.google.com/rss/articles/CBMiZEFVX3lxTE9FQnlrVUt4eGd4U3BZQWJSRnpiN3dxbUJWT0NISDZXeTZyWGVwSk8tMzdXZG1hdjUwY3l5aklwUzhWQXgtNzdJZ3JtOGtxWlEwYlYzcVlxMmEtaFcyX2xaMjc4elA?oc=5) <sub>新京报</sub>
- 📰 2026-10-18 [埃安Ray7预售12.88万起，搭载L4同源智驾电耗9.7度](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9pS0U3czRMbUV1WjRhR1BTbHJEeDNMd1ltVG9ZVjJjaEZwSTJDck1IX0hUYS15MDM1Z2RCVGJUbmt2RC1Vc1gzRDNOVldtUndEUzlVVTJTYkRkQVk?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-18 [【视频】马自达CX-4行驶2.8万公里](https://news.google.com/rss/articles/CBMia0FVX3lxTE1lRkZyWmVZU2FtNmszSE5zelpWLWtPdmVRbmtDYnBnSDVieWNSaXA0YUdQeXIyMV9lNWVheDBsZUM4QzNKelM0V3draHhpZmZOazBkUVl4aWJwYlRjVEp6d2hXbF81SXZENDZZ?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-18 [埃安Ray7预售：12.88万起！45.58度电池能跑530公里！](https://news.google.com/rss/articles/CBMiW0FVX3lxTE54Vm1GMHhPdnVpZl9pMG51eVhhcjhFOU1qdXhPWFVWOWtkVHNiWWRfUHdMTTZiejUta0Nfd0ZGZExINTE2MXd3R3lHV3pSc0lUOUZjMEc1U1pCYXM?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Horizon Robotics</b> (155)</summary>

- 📰 2026-10-18 [搭载激光雷达的新能源SUV推荐：高阶智驾家用SUV怎么选](https://news.google.com/rss/articles/CBMia0FVX3lxTE1EM2pmNDNUQmpQd0xOdUw4RzRJSEdaNkk2V3NKaGF4UG1IYkt2dnQwVjJSMnp2U1BNeVo1S21HeWhGODhhMmFjemt2TEdwNUhYbXBRU2hlbkRnUnlib1JuTlZJQUFLdmhSVkRr?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-18 [【视频】29万起配空悬+华为智驾！岚图泰山X8选购指南](https://news.google.com/rss/articles/CBMiakFVX3lxTE1OWi1iMzNETER3V21yX3hsUjJxaFhWSVZxb1JrbW93Z3JXa1lMbWJlLVR5OE1CMzRsZGlIbTVLTGdBSVVFU2w4blUzMlFaeWZOX296S1F1QXhya2gzclNKOWZSdGFtQUVMR0E?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-18 [【视频】越野也有智驾！老掌沟实测泰山X8纯电版ADS5 障碍物避让](https://news.google.com/rss/articles/CBMiW0FVX3lxTE8xUHFkNENFQ3JjWXZkY3NRYlczWmhwOTVCQzF6a0JSZmNXREUxelctTFk1eElicjJTY2VEUGNkNnp4eGdJcTRwczhYMnU4eE9oVDdaNzAxVTVydEk?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-17 [合资纯电SUV高速智驾横评：ID.AURA T6、bZ5与EZ-60，谁才是长途出行的安心之选？](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5ad1I1c0tIV3ppLUh6UU5fOG55cjhxMkhyTWh6ak13VHFqNjlabG5tVVpvWnItX2lBLVRmdll2eWtINi1ra3E2YmQwWlBNM2g0ZGJBZHZBUHZoTEI0NTRZ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-17 [VW updates ID. UNYX 06 and 07 in China with LiDAR, lower entry prices](https://news.google.com/rss/articles/CBMicEFVX3lxTFBVdWh5MnBWamM3MF9PdVFsN1RDNTN5WkpSZ0VscjhQZmdYY3ZkYl9BcWlVUXlNc2FHVE0xcW9TdS1VQl82RmlOajZVWk10c1N2QnFDUkVIdDVCRXBhOElwZGprNWVKY3FNdFhtTXRFZGg?oc=5) <sub>CnEVPost</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (27)</summary>

- 📰 2026-10-17 [赛豆 ME7 落地凤凰工厂，新造车模式能否站稳 20 万级市场](https://news.google.com/rss/articles/CBMiiAFBVV95cUxOc3RJOWhnazVrNEpGSU82eERzY0VONHlMNmt4ZmRBX084MnprNzBQLTlWbUdlazJpdkVmclNQeS10LWl1VWhjeDR4UmNLNmx3STcyaXZwMlpTQVc1bDU3Rm5SRnNCbU5HVTdRNlU2WjV1emNPSUg1MzhCdlRMTUFZNWdxcXl4UDZi?oc=5) <sub>搜狐</sub>
- 📰 2026-10-17 [赛力斯凤凰工厂制造 赛豆ME7申报：用上字节跳动豆包座舱](https://news.google.com/rss/articles/CBMiWEFVX3lxTE9ORjJMWl9TQjE4ejZYQ0V6SWEtY0dsOEF4dnBKYTJVakdxdEFaWlFlVHU4dUxCeUVjdkdEWkpBZGJMOG0yQlBJOVdOVWxqd1Z4Rmg3NlZCVzk?oc=5) <sub>驱动之家</sub>
- 📰 2026-10-17 [AI Cloud 100 China 2026榜单在沪发布物理AI企业成上榜主力\|具身智能\|上海市\|自动驾驶\|月之暗面\|阶跃星辰](https://news.google.com/rss/articles/CBMiwwFBVV95cUxQUDZQZFpKdThfMEhrWFBpNlJneDFNTEZfQjJLbFZUT005NjFva0tmSUd3cnZXVEZGNzlxUEg2aHVuN3pPQUV5SngtMlNIMWVMa1lNcTh6bmdWQnlnT0s5NzlFekFMS3UwSG56V3BmM2pQazVRbHpKUVlaYnZROVdoREU0ODRPU2FKaFRIZ19rMFZ6NU1qeXdEakVrWldzNFA3U3lPRTVVeGR4R1B6dGJmNzJFcWVlX0M3QUNqZks3OGJHdFU?oc=5) <sub>finance.sina.com.cn</sub>
- 📰 2026-10-16 [【视频】#卡泰驰二手车特斯拉YL](https://news.google.com/rss/articles/CBMiW0FVX3lxTE85eTFWS0xEY25USjY4aXFQRkhjZmZPVHhVeXQ5eHluRkphVFVORXJJaExYSkxrV3Nlc3lWZE9PUXRGdXRRMk5BZlZ4cTNMUFpuWklkNzdCNHRiRWM?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-16 [Volvo Extends Partnership with NVIDIA for New Automated Driving Technology](https://news.google.com/rss/articles/CBMirAFBVV95cUxOWExPaUZZQnhhR2U2eW5lMWdsVmtvb1VUT2o3Sll3anJoblVXcnRIM2Ywajdha3FlM0lBcl9ENUVRX09xQ3g5cVE1ckViOFdpeXFLanEzUzRyd1l2UDhKWnhTeDNlWjFPRnY4SkNJU1R3a2JQd3RCaTZrLXk0U0w5ZTRneXFFZ2lUd0l4WWtxRXpZNmRSYUpsRndlUk0wVDB4b09jOVhuZEwtTzk5?oc=5) <sub>Future Transport-News</sub>

</details>

<details><summary><b>Mobileye</b> (14)</summary>

- 📰 2026-10-17 [Why Mobileye Global Fell Even As Sales Rose](https://news.google.com/rss/articles/CBMivAFBVV95cUxOblE2a0FORVFwdlBzb2t3bTJ4Z0w2YUpPVURicGRfMDlpdUNpWmowRzMwcDJPVEp6NXJZOXg3UXJEcTN2VVdHSkxXTGY4TmxVZmpZTk9QSmVOYVRzUDdJamo1bXF3aFdreUZGb19CWjVyQ2NqRHB2SWs4OEw2N2t0c21pZG9XMENUMEtMTVh4blRuMERqaUJHekQ3S0I5SFhxRU9LdXdyckEzamRmWDFqRnNROUowaUZweGl4aNIBwgFBVV95cUxPYjV5SndkRFlUM1EtOUtUWGVMOHNTNFYyYnZVU0Rfamg5SjJIbWtfcjJWY0ZoVHRVN3ljQlVkekNfY3I1NDlkbDBYNkx0UUhaU2N5OWk2cmpmZ3NYejZjQkI5T0Myenp6ZUN5Z3VoWVR4eDNGei1paGdvcUt5b3VPNEZleDZCZW55c3Zzb0FSYTU3S0M1MzZhdXEtNllTM1VSTWw1a0pWYm55aHBJUDU2OXZOd1A1Ql9INkNhVkgtR0cwdw?oc=5) <sub>Simply Wall Street</sub>
- 📰 2026-10-16 [Citi starts Mobileye at Buy, calls it a global leader in vehicle vision](https://news.google.com/rss/articles/CBMiygFBVV95cUxNVmg5SEZPdDZ4NWZyMThTZGVKc014ZTVwQ1VnQWQ1SzZ1MjhKQ2wwcTJPZUc1T253Y28zc1FHMXB4LXZNNnptQlJzUkEwLTJRN2xHOHd1WGl0TlNFYzZldlNkM2daRHJvUTNsSW80MDJBY1NDVi14cHF2ZDkyZDliZzNObWpxemN3YWE1M3VhZ3RPTW43LUZKaTBKSGpaaHRuOEtRV3h2TC0yd1pkZGtBZzYweHNBbVFLWjRscUxOY1FWN3BUTnZWajFn?oc=5) <sub>StreetInsider</sub>
- 📰 2026-10-15 [Innoviz Technologies Targets $8B Security, Defense Lidar Market at Conference](https://news.google.com/rss/articles/CBMi0gFBVV95cUxOWkhGNi1UZUFBdHJfUlgtdEFPZEliMXQ5azhkVHh2aGotMEhodUhDc0d6WmZjSmttZHhmSEdQY2ZDN0hzMDR0RVRQTW9QRzlqLUxWX1ZaejBDVVh2NzhZNkl5b1c0eUpTSzdNZWx3aElrZmo4T2JSdjVpdzZQdEVONVRCcUlDMmJLbHd5QXBzUnhkSjdRUWd2WHFZRlV0M0JkdG5nQUg0RWlwUzl2eXJUeUR2dWRGenVZVmtDVkFPT1lXcFFMY0JPVk1VRXVaZFhhNkE?oc=5) <sub>TradingView</sub>
- 📰 2026-10-15 [Zacks Industry Outlook Highlights Mobileye Global and Hesai Group](https://news.google.com/rss/articles/CBMivgFBVV95cUxNUndoTm0tSWlkQ1pyR3hUZ0VBd0U4N3R2U2RGV1pqbEQyd3hMYWhLdy1DMFllalpBZElrSFlWRThWUWxoQjF1ZXMtQ1FnYTFpdXQ5Y3VPUi03UldhUnVRdHI3R0Utd0lsSkQzOFlFSXBTeGFMdGwtSGRFaEw2UFc2VENzVDYwdV9vajNxcjZZRnZGSldqU1RvX21yenVwQnk0WkFEYm9qc0NCWEt0UU9QVGFOamhGZUlxNkwxZU53?oc=5) <sub>TradingView</sub>
- 📰 2026-10-15 [Becker Transactions Announces Availability of MagTrac’s Autonomous Vehicle Patents Focused on All-Weather Driving](https://news.google.com/rss/articles/CBMi-gFBVV95cUxOYjB0LUhhdmxDaFFxWm9HSk1LMjZvRVg5WGdNS011dzhWVnNPNDJCZ0twUUlHel9vbW1hR3ZKLUkxQzh5TjhHdjVhdXFodXQ1U0ZCT2t4QVU2bEhld2VLNTRDdVlpXzN0WnE4TmplWlp0MWJnczlaVXVoX09fREttNkJhaFlIbDZTMF9Pb1RfaG1jbUlzR29wcXhqNTNhY3dGUEFjTEJkSFJzaGlNZ0NjTkE0a0xyRExpellkSmxNV3BLV1lIYjMwcV9kc3pRSFp0M1BkRVVMUDVIWjBlZkFYZDJ2Q2xBY3pYajY1LVhpNjgyaUlRUUlaRk13?oc=5) <sub>Kitsap Sun</sub>

</details>

<details><summary><b>Aurora</b> (67)</summary>

- 📰 2026-10-18 [Aurora Innovation (AUR) Wins A 5 Year US Waiver, Is It 60% Undervalued?](https://news.google.com/rss/articles/CBMi1gFBVV95cUxNZUY3dFlETjNKYmxFRWVKLURRTjlfVDVLVWliNjJrcXpjWXFxTklncXpNYWwyM0xfYjBaNFpBOHlaX0I4eFNJMF9WZWNCR2R0RWxfOTBhTGFfREtLd1JVOTJaLUVLTFJoY3hNTzExZFdaR3RDTnk0NGJBOGs2T1NyZ29yV2otempKQ2RzalppRHJ5TnhfV2JTdzBDTVM1T3AteTBmSHZldHRGMlRlc2ZfaEc0T0VOcnpOQnBwcExLUEUyRmVib1M5MFJVRkpWamkzU3l6Ui1n0gHWAUFVX3lxTE1lRjd0WUROM0pibEVFZUotRFFOOV9UNUtVaWI2MmtxemNZcXFOSWdxek1hbDIzTF9iMFo0WkE4eVpfQjh4U0kwX1ZlY0JHZHRFbF85MGFMYV9ES0t3UlU5MlotRUtMUmhjeE1PMTFkV1pHdENOeTQ0YkE4azZPU3Jnb3JXai16akpDZHNqWmlEcnlOeF9XYlN3MENNUzVPcC15MGZIdmV0dEYyVGVzZl9oRzRPRU5yek5CcHBwTEtQRTJGZWJvUzkwUlVGSlZqaTNTeXpSLWc?oc=5) <sub>Simply Wall Street</sub>
- 📰 2026-10-17 [The Most Polite Trucker in America Is a Driverless 18-Wheeler](https://news.google.com/rss/articles/CBMifkFVX3lxTE93OW9admIyUlN5bFZhR01TY2d3S1J1a19qSDdpOEJONWtORnNBVm9rWGMyaEtXV05KRXBJTjZPWUNXOVFSSFA3R0tPTWhXQUdEaEhaVWFfMDFYMHNLT1M0dzFTclE3ZlVKdkhSZXp5dk1feXdUdXl2WnZNM0xQZw?oc=5) <sub>WSJ</sub>
- 📰 2026-10-16 [Who Is Legally Responsible When a Driverless Truck Causes Damage on the Road?](https://news.google.com/rss/articles/CBMinwFBVV95cUxPYXFFTnpDaTRjcDVTZ2VwYUVFUWV2dG1VOHZBMy1SZXdOaDhvRVp0UEpaMTFwRWg0VW56eUU2WG56Y01GNWhmcTM2T1hEZU9LV1Y0OS1PNmNPLVgtZFU2OXk2OHlBcXJtMHhzRzJSejBBcllJLWR2SmNxRDRIcGoyQkRpN2tkOWMtNkh0UWJYelBGMm51UEZsS1g4dmtrelk?oc=5) <sub>Freedom For All Americans</sub>
- 📰 2026-10-15 [Waabi, Warrior Logistics begin customer operations in Texas](https://news.google.com/rss/articles/CBMiaEFVX3lxTE9xc3hGT3NBWFFNeEJTbGJzdzN0U3l5VzNkWlJTcDdSY2hNaFRmZ0VJQ0FfdzUxRi05NW9EMlhIbXEyYlplWmVHeVh5ZHNFSmNWMkRvMzBYYzVIYWFPRTIydXpWcF9lZWtj?oc=5) <sub>Transport Topics</sub>
- 📰 2026-10-15 [DOT awards $200M for truck parking projects](https://news.google.com/rss/articles/CBMinwFBVV95cUxNM2Ytcmh3YnhIdnZ6Z1VtZHE2V05EQW1SNS1rckJ3NDVSQjZORjN4Um1lMHRpWjl6LXlWVllCVDc3a0dxclBrcTJ4R1M0RmE3TWsyTDNOWEEtYWRuaXNoLWRZY0xQWHJzbFh2c0JjQjdvRW5VQUdqZW42SGwwTmNvRzgzUGhBRkxDVnhRc1ZrM2Y0ejlLYWlMUEhtYjlsZEE?oc=5) <sub>Commercial Carrier Journal</sub>

</details>

<details><summary><b>Zoox</b> (63)</summary>

- 📰 2026-10-17 [Oakland can’t find footing in Bay Area comeback as R&D sales dip](https://news.google.com/rss/articles/CBMipAFBVV95cUxNY0JMQm5LdWk1S09rSVFWS0JSLVZac1RtWDJialB5VXV4MnZmeEdNS2FMMDF2ZlpOcGxhR2d0cmoxM2RFWmg5cDdPTHFkLTRBNUVPbGJNMTVNcnY2YXdKTUYyZDRtOXZvWWxLc2o0Q1RyeXl0VG4tU3JkTHVibGdQZll5bVRvNDlKQVpkNllaaHZINlVEd1luODhvakRqalhrNlNITw?oc=5) <sub>The Real Deal</sub>
- 📰 2026-10-16 [Tesla Roadster — The Last Best Driver’s Car](https://news.google.com/rss/articles/CBMilwFBVV95cUxONzhwRjV4NlZ2czJyTVNwa0VzNnowd2lyZjF3d1h5YVRFTnhLckxlUWR5WU5DWEl2eUg4VnpyV0l0emdqNmtLanBvNWNpbzJtZmxON3N1UmRtckUteFdfa2g1amxhWnpSblZheXlSRTB5ak1RVHJpRUFfU0wyMndkYzh1WEo2SlRJN25feTJSckdmbjg1eG5N?oc=5) <sub>eletric-vehicles.com</sub>
- 📰 2026-10-16 [As Robotaxis Spread, Carmakers Must Choose Between Owning the Customer and Selling the Car](https://news.google.com/rss/articles/CBMilwFBVV95cUxNc2Y4S25PZUdJMVcwWkZKYWV2cG1tR0ltRUI1NmZyVG1xbVEyX2dIN1dWMzg0aG1zamtQMUpLbjlzQnhkMkxCRTNwTVVxNjFDckJKOFRhSDJYbHItS1pXa2FyRzFlWnMxbG9tTV9mMkVWekQyQ1JjVUZyS2hJaF9aNE00U0NCWDRRb3RGWUJLc1otM1VSZ3A0?oc=5) <sub>The Motley Fool</sub>
- 📰 2026-10-16 [Zoox Leases Two More Hayward Warehouses for Robotaxis](https://news.google.com/rss/articles/CBMiogFBVV95cUxNS3hoQXBUa01acFRaQjRYMWNxOENEYllhV3EtcnFBNjBLUmFtLW9qRlU4WE9GVEhXblJlNmhoY3hkNFRKclZ1X3lHUXFpUV9Cc2lnbHFsQ2YzX2RSQXJ1d0xra3pnRy1YbEp2eW5ON0xqYXB4aWJEaUIzZDVGU1BTUm5ERmNrZVdTUTlJZ0ZOckJfZUJhTVdGRjQ5YkRhNTFYOFE?oc=5) <sub>Hoodline</sub>
- 📰 2026-10-16 [Zoox doubles down in Hayward with 350K sf industrial lease amid robotaxi battle for market share](https://news.google.com/rss/articles/CBMirAFBVV95cUxOczJCSGJUd2Q2TG0tM2MtY2JUblZodnc5WVV4NGxCWnhuSFpaYVRwcjdfN09CTXlFS0llRy1CVmVkZnBiRUxqVGluY1YwVGhWb2pocWdncS12ZnV3NHR5OGNkQkhqWl9qUGY5OGF5eHFxSjByWUJNQW9rNlRjenNhdHYyN29LMWpRNXZTRlE0TDc3VVJFXzBwRFRyc3lwWDUydkx4X2ltRGdMS2lt?oc=5) <sub>The Real Deal</sub>

</details>

<details><summary><b>Motional</b> (32)</summary>

- 📰 2026-10-18 [Hyundai Motor, Kia to Deploy Humanoids in Factories from 2032, Unveil 'Autonomous Operating Factory' Roadmap](https://news.google.com/rss/articles/CBMidkFVX3lxTE5BSkloNVFid1JrenR2b2g4a1N2OXI4SVNYQmRvMW5wc2lHS0Y5TVUzVlRJTjd0Wlo4UUFmWDA0U3hQTmFxOG9uSF9oOC1TMGs0cV9temVoeXhzUkx0Vzg3ZU5qNDJXRnJTb2l4VXg4U195Q2U3R0E?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-17 [Grayson Brulte: Waymo Will Launch Driver-Out UK Service by Q1 2027 as London Permit Becomes 'the Keys'](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9VUjFlTTg4T2NGVlQ5dlIteGN1RVVNOWV1UTVCTEhGU3poT1FHOFN6VjB3VU5QX012ZEpaZ2RNNV9RNkRuV2hmQkxTY2EyN2FjanZhRVpPczBLWTg?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-14 [Hyundai’s two robotaxi plans take different routes](https://news.google.com/rss/articles/CBMikAFBVV95cUxQNWdFN1RBOWctNVVIZmRxemEzVEhrQ2MzVkN6YkJWME81bW41bFFqQVVDLTl4SEQ3OTYwalRQaFo0Q0xwaVR4M3FYOUZpMUV3OEJSTDktdHY4enVEdDgzY0xuV3lSa3hCTTAwdE93bkhoS2M5aHdxcmVkbEJIM1QteTlVbjhfTk9UUVBraW9GX2TSAZABQVVfeXFMUDVnRTdUQTlnLTVVSGZkcXphM1RIa0NjM1ZDemJCVjBPNW1uNWxRakFVQy05eEhENzk2MGpUUGhaNENMcGlUeDNxWDlGaTFFdzhCUkw5LXR2OHp1RHQ4M2NMbld5Umt4Qk0wMHRPd25IaEtjOWh3cXJlZGxCSDNULXk5VW44X05PVFFQa2lvRl9k?oc=5) <sub>ABC27</sub>
- 📰 2026-10-13 [Hyundai Motor Group chief marks 6 years at helm with physical AI ambitions](https://news.google.com/rss/articles/CBMi0AFBVV95cUxOY2g0R29NX1hSa0ZuUzJveFVZYUQ1YzVVNEItNnRkUjY0TnRHNi1fY1ppaVc2YmotOEt3YXhCeWxLNVN1NGQ2c2hGNVJYclBocEhKcDgzNjMtdjFPeGJ1bWJjTFR0UGgtUzNwdWZqQkQzaHB5U3k3bXpPcDQ2S05KUzktWkJWN21WSjItamJ6eV84clptQzRHV25xYXFyNURmamNLWGkxeFVNUDFCeWs2cTJta25zcE54WGFYcEE5T1YyaVQtMEh5ZTZvUTNUUlUz0gHQAUFVX3lxTE5jaDRHb01fWFJrRm5TMm94VVlhRDVjNVU0Qi02dGRSNjROdEc2LV9jWmlpVzZiai04S3dheEJ5bEs1U3U0ZDZzaEY1UlhyUGhwSEpwODM2My12MU94YnVtYmNMVHRQaC1TM3B1ZmpCRDNocHlTeTdtek9wNDZLTkpTOS1aQlY3bVZKMi1qYnp5XzhyWm1DNEdXbnFhcXI1RGZqY0tYaTF4VU1QMUJ5azZxMm1rbnNwTnhYYVhwQTlPVjJpVC0wSHllNm9RM1RSVTM?oc=5) <sub>The Korea Times</sub>
- 📰 2026-10-11 [Six Years into Euisun Chung's Tenure... Hyundai Motor Group Moves Beyond the 'Global Big Three' Toward Physical AI](https://news.google.com/rss/articles/CBMiZEFVX3lxTE1qSWl5SS12dk8yVXMwandrR090TkZkdzZDaFladGpmOGNZZDNrMGxBQV9zSkV5TXpVeXIzWGhKd0FVYUQ0ZFdsT1pEWGxZNDV1UC14N0FsZmxVd0ZFOUVkamhoMWg?oc=5) <sub>아시아경제</sub>

</details>

<details><summary><b>comma.ai</b> (4)</summary>

- 📰 2026-10-07 [Researchers Find that AI Models Struggle With Even The Most Basic Driving Skills](https://news.google.com/rss/articles/CBMiuwFBVV95cUxNb2ZGRGxGZDNjLWU1OVBPNjUtUlJXR0hiVGV3WEJ1eUVnSWExMWVvRmJjX2NtQm9sX0plMTU3YzZwUm5ZTzVoSGttcXZmQ3BqbW40X2doNFMycUk4UWE3anlidy1vWHNYZndVZjZWLUYtbnlHeVBFRjJOaTF4SWxzbmotR0xsNkVIcEhfZ0M3LUs5R2FyV1lVdlRRU3JwakpQcXpBUzlEOEhsWlB3Q19EdXFhQjRvZDU5MHln?oc=5) <sub>Auto Spies</sub>
- 📰 2026-10-07 [OpenAI's GPT-6 Astra is the only AI model to finish a real-world driving test in a Toyota Corolla](https://news.google.com/rss/articles/CBMifEFVX3lxTE9iZmN2ZFp6blVBRnZUTkYtYTJ3b0hSb0xhQjZyQXh5MUN2T3ladUlEb1F1SWJzc3FtamZtazk4LTVUWVpNX0ZjbGZwMnpERk45TVVQWVA1RjBZVUxxTTAzTWpaV1JqUzIwM1I2Wk1tTzc3bDJpaWluc2JVam4?oc=5) <sub>Crypto Briefing</sub>
- 📰 2026-10-06 [AI Agents Tried to Drive a Corolla, Crashing on 8 of 11 Runs](https://news.google.com/rss/articles/CBMiuAFBVV95cUxONWxQTEZham1kc1J4S2lMNUh6OTN1QWhXbl92U21NUWZTZWhNUUdwcFVvUHYtVWJzSjl4TjlCeFhUY2ppMXd3WkkxaHJFRmFlNUN2NGFSSENnV2ZZYWRNZ3JIUjd0dzFlTS0wR3gtbmxXN3VHOUkxWWg2VVFpTVgzWGN2T3RPdEFJV0cyWjRPSVFyNWZTYjFyX0pzYjFEUWQwLUlfbGo1bm8xVUZXQmpyQ3pCNXV5ZE9x?oc=5) <sub>thetruthaboutcars.com</sub>
- 📰 2026-10-05 [Researchers Discover ChatGPT Can Drive a Car. Grok, on the Other Hand…](https://news.google.com/rss/articles/CBMikgFBVV95cUxNNnNwX0g5bHV4STJlMXNOcXRnYnBHWHNoelViM2pJSzFob3dvUVJIdFlDRDV4X09DSVloZmxCTk5NODd3b3RBR2JmWEJQRktXUTYyWDNveS15UEw0NnVfSFluMlJxZHlBb3NhYnRNdDJsZ01MbVNpOXY4OW9nQnBSYnFRQ1U2YVd3a3R2ZTY4VlJNdw?oc=5) <sub>The Drive</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
