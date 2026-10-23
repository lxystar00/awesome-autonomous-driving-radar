# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-10-23 · 1,305 papers tracked · 43 curated.

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
- [End-to-End Driving & Planning](#end-to-end-driving--planning) (10)
- [3DGS / NeRF Reconstruction & Sensor Sim](#3dgs--nerf-reconstruction--sensor-sim) (4)
- [Perception: BEV, Occupancy, 3D Detection, Mapping](#perception-bev-occupancy-3d-detection-mapping) (8)
- [Datasets & Benchmarks](#datasets--benchmarks) (2)
- [Safety, Robustness & Evaluation](#safety-robustness--evaluation) (3)
- [Industry Tracker](#-industry-tracker)

## VLA / VLM for Driving

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Teaching Vision-Language-Action Models What to See and Where to Look](https://arxiv.org/abs/2607.01658)<br><sub>Yuguang Yang, Canyu Chen, Zhewen Tan et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 34](https://github.com/ShivaTeam/DriveTeach-VLA) | Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving |
| [DeepSight: Long-Horizon World Modeling via Latent States Prediction for End-to-End Autonomous Driving](https://arxiv.org/abs/2605.10564)<br><sub>Lingjun Zhang, Changjie Wu, Linzhe Shi et al.</sub> | ICML 2026<br>2026-05<br>📑 2 | [⭐ 31](https://github.com/hotdogcheesewhite/DeepSight) | End-to-end autonomous driving systems are increasingly integrating Vision-Language Model (VLM) architectures, incorporating text reasoning or visual reasoning to enhance the robustness and accuracy of driving decisions |
| [SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving](https://arxiv.org/abs/2610.20609)<br><sub>Shaoyuan Xie, Zihan Zhang, Jingxuan Wang et al.</sub> | CoRL 2026<br>2026-10 | [⭐ 27](https://github.com/ASGuard-UCI/safedrive-vla) | Vision-Language-Action (VLA) models are gaining attention in autonomous driving, inheriting commonsense priors from large language models (LLMs) and widening the navigation interface from a fixed command set to free-form… |
| [Scene-Adaptive VLA: Efficient Autonomous Driving via Dynamic Layer Routing](https://arxiv.org/abs/2610.24590)<br><sub>Yujia Yang, Quan Yuan, Jiawei Fan et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 2](https://github.com/yang-luvu/Scene-Adaptive-VLA) | Vision-Language-Action (VLA) models offer a promising paradigm for autonomous driving |
| [CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving](https://arxiv.org/abs/2607.04179)<br><sub>Zhaohong Liu, Hao Ye, Xianlin Zhang et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 1](https://github.com/MICLAB-BUPT/CritiqueDriveVLM) | End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving |
| [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)<br><sub>Nan Yang, Zhanwen Liu, Linfeng Zhang et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 11](https://github.com/Zizzzzzzz/MVPruner) | Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings |
| [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)<br><sub>Yuan Gao, Wenting Miao, Mattia Piccinini et al.</sub> | IROS<br>2026-07<br>📑 1 | [⭐ 29](https://github.com/TUM-AVS/Chat2scenic) | Validating autonomous driving systems requires diverse, regulation-compliant test scenarios |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 11 | [⭐ 522](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
| [Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air](https://arxiv.org/abs/2605.31066)<br><sub>Tianle Zeng, Yanci Wen, Xueang Yu et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 1,119](https://github.com/louiszengCN/CarlaAir) | Recent aerial vision-language-action (VLA) models show promising single-UAV capabilities, such as tracking moving objects and navigating to language-specified landmarks |
| [GRAVA: Grounded Reasoning-to-Action Representation and Learning for Autonomous Driving](https://arxiv.org/abs/2609.15169)<br><sub>Xiao Liu, Haoyu Li, Jianghao Leng et al.</sub> | arXiv<br>2026-09 | [⭐ 297](https://github.com/AhernResearch/grava) | Driving vision-language-action (VLA) models increasingly reason before acting, but their intermediate reasoning is often weakly grounded in physical scene evidence and loosely connected to executable behavior |

## World Models & Generative Simulation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [HERMES++: Toward a Unified Driving World Model for 3D Scene Understanding and Generation](https://arxiv.org/abs/2604.28196)<br><sub>Xin Zhou, Dingkang Liang, Xiwu Chen et al.</sub> | ICCV 2025<br>2026-04<br>📑 4 | [⭐ 72](https://github.com/H-EmbodVis/HERMESV2) | Driving world models serve as a pivotal technology for autonomous driving by simulating environmental dynamics |
| [FrozenDrive: Zero-Shot Text-Guided Driving Scene Generation and Data Augmentation with Parameter-Free Frozen Diffusion Model](https://arxiv.org/abs/2606.20110)<br><sub>Yuhwan Jeong, Hyeonseong Kim, Daehyun We et al.</sub> | ECCV 2026<br>2026-06<br>📑 1 | [⭐ 10](https://github.com/daehyunwe/FrozenDrive) | Synthetic data for autonomous driving is surging, powered by diffusion models that promise scalable scene generation |
| [MESSENGER: Memory-Enhanced Sequential Scene Flow Estimation via Autoregressive Next-Frame Forecasting](https://arxiv.org/abs/2610.10759)<br><sub>Jiuming Liu, Jianing Li, Mengmeng Liu et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 0](https://github.com/liujiuming123/Messenger) | Scene flow can capture low-level 3D motion displacements in dynamic scenarios |
| [ASTAD: Asymmetric Style Transfer for Synthetic-to-Real Adaptation in Autonomous Driving](https://arxiv.org/abs/2606.29286)<br><sub>Dingyi Yao, Xinqi Zhang, Lihui Peng et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 2](https://github.com/Dingyi-Yao/ASTAD) | Synthetic data mitigates the data scarcity problem in autonomous driving perception |
| [Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends](https://arxiv.org/abs/2606.01164)<br><sub>Jiuming Liu, Chaojun Ni, Mengmeng Liu et al.</sub> | arXiv<br>2026-06<br>📑 8 | [⭐ 245](https://github.com/liujiuming123/Awesome-Interactive-World-Model) | With rapid development of large language models and diffusion-based content generation, world modeling has attracted increasing research attention, benefiting various downstream domains such as game engines, embodied AI,… |
| [Is Your Driving World Model an All-Around Player?](https://arxiv.org/abs/2605.10858)<br><sub>Lingdong Kong, Ao Liang, Tianyi Yan et al.</sub> | arXiv<br>2026-05<br>📑 6 | [⭐ 256](https://github.com/worldbench/WorldLens) | Today's driving world models can generate remarkably realistic dash-cam videos, yet no single model excels universally |

## End-to-End Driving & Planning

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](https://arxiv.org/abs/2609.26792)<br><sub>Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.</sub> | CoRL 2026<br>2026-09<br>📑 1 | [⭐ 13](https://github.com/VAIL-UCLA/DreamStream) | Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions |
| [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)<br><sub>Shen Zheng, Anurag Ghosh, Gaurav Parmar et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 32](https://github.com/ShenZheng2000/WarpI2I) | Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs) |
| [DriveMLP: When Training Strategy Outperforms Model Complexity in Autonomous Driving](https://arxiv.org/abs/2610.29676)<br><sub>Alessandro Canevaro, Julian Schmidt, Hang Yu et al.</sub> | CoRL<br>2026-10 | [⭐ 0](https://github.com/alessandro-canevaro/DriveMLP) | Learning motion planning policies that remain reliable under closed-loop execution is a central challenge in Autonomous Driving (AD) |
| [G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance](https://arxiv.org/abs/2606.26017)<br><sub>Hang Yu, Ye Jin, Alessandro Canevaro et al.</sub> | IROS 2026<br>2026-06<br>📑 5 | [⭐ 6](https://github.com/HangYuu/G2DP) | In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 17 | [⭐ 349](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
| [SimWAM: A Simple World Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.07468)<br><sub>Zongchuang Zhao, Xin Zhou, Tianyang Xu et al.</sub> | arXiv<br>2026-08<br>📑 9 | [⭐ 198](https://github.com/H-EmbodVis/SimWAM) | In autonomous driving, World-Action Models (WAMs) have improved end-to-end planning by transferring video dynamics priors to action prediction, but many still couple planning with future-video generation at inference, in… |
| [Latent-Centroid Steering: Single-Pass Classifier-Free Guidance for Command-Aligned Autonomous Driving](https://arxiv.org/abs/2608.00237)<br><sub>Meibo Hu, Jiamian Wang, Pichao Wang et al.</sub> | IROS 2026<br>2026-08 | [⭐ 2](https://github.com/codingmlinprocess/LCS) | Vision-language models (VLMs) have recently emerged as a promising paradigm for end-to-end autonomous driving, enabling agents to map multimodal inputs and high-level navigation instructions directly to executable trajec… |
| [DVGT-2: Vision-Geometry-Action Model for Autonomous Driving at Scale](https://arxiv.org/abs/2604.00813)<br><sub>Sicheng Zuo, Zixun Xie, Wenzhao Zheng et al.</sub> | arXiv<br>2026-04<br>📑 15 | [⭐ 369](https://github.com/wzzheng/DVGT) | End-to-end autonomous driving has evolved from the conventional paradigm based on sparse perception into vision-language-action (VLA) models, which focus on learning language descriptions as an auxiliary task to facilita… |
| [STAGE: STyle-controllable Action GEneration for personalized autonomous driving](https://arxiv.org/abs/2607.29517)<br><sub>Zihao Liu, Xing Liu, Yizhai Zhang et al.</sub> | RA-L<br>2026-07<br>📑 1 | [⭐ 6](https://github.com/CarlDegio/STAGE) | Driving style refers to the behavioral preferences that drivers maintain during driving, shaped by their diverse experiences, habits, and needs, and is typically reflected in varying levels of aggressiveness |
| [A Survey on End-to-End Autonomous Driving Training from the Perspectives of Data, Strategy, and Platform](https://arxiv.org/abs/2610.00926)<br><sub>Chengkai Xu, Yiming Cui, Jiaqi Liu et al.</sub> | arXiv<br>2026-10<br>📑 5 | [⭐ 109](https://github.com/Jiaaqiliu/Awesome-Training-Ecosystem-for-E2E-AD) | Autonomous driving is a cornerstone technology for the future of intelligent transportation, where end-to-end learning has emerged as a transformative paradigm that directly maps multimodal sensory inputs to driving acti… |

## 3DGS / NeRF Reconstruction & Sensor Sim

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DriveWeaver: Point-Conditioned Video Inpainting for Controllable Vehicle Insertion in Autonomous Driving Simulation](https://arxiv.org/abs/2606.31918)<br><sub>Junzhe Jiang, Zipei Ma, Zijie Pan et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 16](https://github.com/LogosRoboticsGroup/DriveWeaver) | A pivotal step in autonomous driving simulation involves inserting foreground vehicles with predefined trajectories into simulated scenes |
| [Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796)<br><sub>Leshu Li, Jie Peng, Yang Zhao</sub> | ICRA<br>2026-06 | [⭐ 14](https://github.com/UMN-ZhaoLab/Pocket-SLAM) | 3D Gaussian Splatting (3DGS) has garnered significant attention in Simultaneous Localization and Mapping (SLAM) due to its advances in capturing fine-grained geometry features and synthesizing novel views |
| [NIDAR: NIR-Guided Intrinsic Decomposition for Scalable Scene-Agnostic LiDAR Intensity Reconstruction](https://arxiv.org/abs/2609.36878)<br><sub>Junjie Zhang, Jie Yin, Kefei Qian et al.</sub> | IROS 2026<br>2026-09 | [⭐ 19](https://github.com/Zjj587/NIDAR) | LiDAR return intensity provides complementary surface-response cues for robotic perception and state estimation, yet many simulation pipelines omit it or reproduce it using reconstruction methods that require real intens… |
| [MM-TRELLIS: Point-Cloud Guided Multi-Modal 3D Vehicle Generation in Autonomous Driving](https://arxiv.org/abs/2606.24301)<br><sub>Hongli Xiao, Youjian Zhang, Yucai Bai et al.</sub> | ICRA 2026<br>2026-06 | [⭐ 9](https://github.com/HongliXiao/MM-TRELLIS) | Recovering realistic 3D vehicle models from autonomous driving scenes is crucial for synthesizing training data and building simulation environment |

## Perception: BEV, Occupancy, 3D Detection, Mapping

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Deformable Gaussian Occupancy: Decoupling Rigid and Nonrigid Motion with Factorized Distillation](https://arxiv.org/abs/2605.28587)<br><sub>Yang Gao, Wuyang Li, Po-Chien Luan et al.</sub> | CVPR 2026<br>2026-05<br>📑 2 | [⭐ 22](https://github.com/vita-epfl/DeGO) | Understanding dynamic 3D environments is essential for safe autonomous driving, particularly when reasoning about human-centric, nonrigid agents |
| [FreeOcc: Training-Free Embodied Open-Vocabulary Occupancy Prediction](https://arxiv.org/abs/2604.28115)<br><sub>Zeyu Jiang, Changqing Zhou, Xingxing Zuo et al.</sub> | RSS<br>2026-04<br>📑 7 | [⭐ 143](https://github.com/the-masses/FreeOcc) | Existing learning-based occupancy prediction methods rely on large-scale 3D annotations and generalize poorly across environments |
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
| [123D: Unifying Multi-Modal Autonomous Driving Data at Scale](https://arxiv.org/abs/2605.08084)<br><sub>Daniel Dauner, Valentin Charraut, Bastian Berle et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 404](https://github.com/kesai-labs/py123d) | The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics |

## Safety, Robustness & Evaluation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [CCFM: Collision-Constrained Flow Matching for Safety-Critical Scenario Generation](https://arxiv.org/abs/2607.04451)<br><sub>Ke Li, Kaidi Liang, Yuxin Ding et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 3](https://github.com/KELISBU/CCFM) | Evaluation of autonomous vehicle (AV) planners in safety-critical closed-loop simulation is essential for real-world deployment |
| [Lipschitz Optimization for Formal Verification of Homographies](https://arxiv.org/abs/2605.23203)<br><sub>Jean-Guillaume Durand, Panagiotis Kouvaros, Maxime Gariel et al.</sub> | CVPR 2026<br>2026-05 | [⭐ 2](https://github.com/jeangud/homography-verification) | The adoption of vision neural networks in regulated industries requires formal robustness guarantees, especially in safety-critical domains such as healthcare, autonomous vehicles, and aerospace |
| [CADET: A Modular Platform for Evaluating Distributed Cooperative Autonomy in Connected Autonomous Vehicles](https://arxiv.org/abs/2606.04072)<br><sub>Pragya Sharma, Brian Wang, Mani Srivastava</sub> | ICRA 2026<br>2026-06<br>📑 1 | [⭐ 0](https://github.com/nesl/cadet) | Deep learning models are increasingly central to autonomous vehicle (AV) pipelines, yet their integration has traditionally followed a monolithic design where perception, planning, and control execute on a single onboard… |

## 🏢 Industry Tracker

Latest 14 days of news, official blog posts and new open-source repos from tracked companies. Full daily feed in [`daily/`](daily/).

<details><summary><b>Waymo</b> (223)</summary>

- 📝 2026-10-16 [Hello Toronto! Waymo is En Route](https://waymo.com/blog/2026/10/waymo-in-toronto) <sub>official blog</sub>
- 📰 2026-10-23 [Automakers Align on 2028 Autonomous Driving Commercialization](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNcVd3V1JhaGFMR3NySU14c3dTNkZrcWZpSktMNWxYOHhGc21DaFpydDIyaXYzZlJJSjlYTXVrSnctTnNuY1VnbHF2c3EySHMzNzNRYmJHZTRpVlFGb2xhSUplQXd1WVdiVFZacHVNQ3lBYUxTREk1c1VxRVd2ZEtDelY2UTBuSGdI?oc=5) <sub>조선일보</sub>
- 📰 2026-10-23 [Waymo founder predicts ‘landslide’ robotaxi adoption in Singapore, driven by high car costs](https://news.google.com/rss/articles/CBMi0gFBVV95cUxOelVrcFlIWEdRSTFKMzVmNWF1UUFCUnpJY0JmcmlxRFhWYkp2UzBpN09WQ0x0SDhXWVQ1a2tUNV9nTVNQZWY2OGs0OHhQeHFNLTMwS2hLYXhaOGR3VTVHM2l1c1RSSy1QMi1nTG43ejlDOTF1cmZjVHo4MHNQWHRoRlctNmo2dkxWZklSNUU2cEN4ZzhPNU54XzJoaS1LNmtXdHFkQ0k3RVZWdEZsT1VzclVxblBUcDJ1TWJLWHROZGdHT3lRanEzcEZkOHAyZlZrRHc?oc=5) <sub>The Business Times</sub>
- 📰 2026-10-22 [Waymo launches autonomous ride service at Las Vegas airport](https://news.google.com/rss/articles/CBMiogFBVV95cUxOUGhJTWkyQlR1cEh3dEVnWmNJbUtXTkhiblZRNHo3ZVowc0JCQUhUZHZ0R3l3T2UzUHJsVlBubHhhV0NZOFhkaGd1Wk1yRUFRSkp3VWxoZ0RIblBlS3pFdTA2ZWJDLWJwRWNqbDl6ZnBob2J0cmszZThmWVQzcUREZVExWEtvTFJmczBVZDFHQ0h1SjBkVV94Y2xBb293VVRXZ1E?oc=5) <sub>FOX5 Vegas</sub>
- 📰 2026-10-22 [Tesla Robotaxi Video Dodges Waymo, Avride [2026]](https://news.google.com/rss/articles/CBMicEFVX3lxTE1pcVZYT1hNODVQa0NXTWVnMGp1R3l2czRFTkpYWnZndmFqQkgzTEh4VFRwTm9nbVpmQ29PcjhNa2RUeVdvVlQybEhibk56ejZlR3ZBSzJfTHc2cmJqV0RlRENYR2RTRFZYQnQ2WjVHWHk?oc=5) <sub>shattered.io</sub>

</details>

<details><summary><b>Tesla</b> (355)</summary>

- 📰 2026-10-23 [Tesla buyers are buying for Full Self-Driving and not for the car, data shows](https://news.google.com/rss/articles/CBMikAFBVV95cUxQelZwbXE4QWtpNVMyVnpQajNpdXZmSVcwbl9sT2sxaWZfMHZGdjlGRWJTSmdOM09qODF0VHhvbERUUVRER2JacXJvOUZPRmM2aElkRS1RNkNIRVZlVTg3bUdqa0owa1UySmlDb2VJZG9DNm9yN21IN2NmSGpGeG5GbTNEM0Z5ako3TEJxaG5FSWI?oc=5) <sub>Teslarati</sub>
- 📰 2026-10-23 [Tesla Robotaxi Austin Expansion: 5 Details That Matter](https://news.google.com/rss/articles/CBMikgFBVV95cUxPZ21WS0dmZzEwOWc5bDk3MWRIeGZhci1MWkcyWjRHQTNNOUhDMmRqNm5aZnhzYWRDZV9mcUhIdUdJcUtvY0llNFYzWGtNTlh3emRINjBIb2Vfb3UzZEdPcDhURmtfVVNHbmYxVmlzZkFsdFNrQ0JVSnNOVlRyamYzeW81Y3pBdWpyV3I3VjlSYklBQQ?oc=5) <sub>BASENOR</sub>
- 📰 2026-10-23 [Tesla Builds Own FSD Maps, Starting With v15 [2026]](https://news.google.com/rss/articles/CBMicEFVX3lxTFB1RG5lRTFHb0luT0l6VFRfU0tlQ1NsQ1pVVDBVQTYwNGEyeDJyaldudmtvSFFLZFdCVDVoMVdUSVozcWRMdTVuVTQyMEd3a1I4elZnUTNWT21ldF9JYVc2ZDA4eDlPMnItS2plSEFQYi0?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-10-23 [Tesla lists Jacksonville robotaxi service as ‘coming soon’; no launch date announced](https://news.google.com/rss/articles/CBMi7gFBVV95cUxPenJSYTZ5aV9GVmhKT2k4el8zdWdsMnJvYklINGVZMmRNMk92UXNNTGVkWi1BMEpPRldMaWJhc01sWGFTdlBuaERoS2NxdEFKTHBacXJ1YXF3VlgzV3duN0Y4elRLS3RZc1h5eEUzVXh5bFJuNTN0MDE2QW8wYU1kMFd2RFE5UUZ3eE9TUlgtdG9wUDJTQ3NNXy1rSkNIZFk1b0pEZmZPMDVucVhXeTRja0FGVkJnUE1CMmw0MU9hekpRSVkwVnk5d0VMZmMxal9LOGthb3p2dWZwdmxxNzlJVFUxSS0tWmk1TGY0alVB?oc=5) <sub>Action News Jax</sub>
- 📰 2026-10-23 [California reporter's Tesla robotaxi got stuck in 'fart mode,' and no one could shut it off](https://news.google.com/rss/articles/CBMifkFVX3lxTE9aTnRJMEJ4ZHBsem1BSUk4QWRINktfQ3lrYTlEVVc2M3Bfc3JPUWNRdzNCWDJmQVpOWjRZNkdUcjRZclFQNmtuQmJ1NTRqSGd2Vk5wbS05NkwtWExEZDhCN2hKNGdWMHk2QU1BUklQdXozZVVqMV90d0kzZENHUQ?oc=5) <sub>The Cool Down</sub>

</details>

<details><summary><b>NVIDIA</b> (247)</summary>

- 💻 2026-10-20 [NVIDIA/flare-local-inference](https://github.com/NVIDIA/flare-local-inference) <sub>GitHub</sub>
- 📰 2026-10-23 [Einride to trial Nvidia Alpamayo in autonomous trucks](https://news.google.com/rss/articles/CBMilgFBVV95cUxPQjJyeHBLMXA3dVBFTTN3WHlRMVg3NVJkX1RNaDhBcFdOcHpZYk8zemlJV0hiQzlza2hKenNzaDIyckx5VjZ6VGk1OGtzUmJjY2NqNUtkNHBtaFhFRlg3cGE2aHowSVdnY3JlM1g1WlhpRnRiSlBzSEdTU0xzY3FUcjBkRVpGMnZjMU5rNHN0Rmh0Q0g1TUE?oc=5) <sub>Automotive World</sub>
- 📰 2026-10-23 [NVIDIA Details Kazakhstan GPU Deployments and Robotaxi Plans](https://news.google.com/rss/articles/CBMiigFBVV95cUxQNXNQT0lLRTVQdzM5OUx1RXQ0RU9ZTzc1SVo4aDVVdEFEcVl1WUVqakJmVTBNTFkxVGpIM3NDc1BhM2Jsc1YzZkIzU3gyMDZ5RnREbUFMV1VSUDRqMDQtS05fRUdMdjJMbl9NRnlyTEVjMXFBQjN3YXRHZ19kcnVqV1plM2hyWDNPU1E?oc=5) <sub>Unite.AI</sub>
- 📰 2026-10-22 [NVIDIA Cosmos Opens New Tools to Train, Evaluate and Deploy World Models](https://news.google.com/rss/articles/CBMigwFBVV95cUxOMWg0TFo2MFdIOWsyZnVmOTM0RVZfZXdETG14QXpVNnNlLXQzOFBtV2FzMUtSSWZidlgtVzRBdnlwbXRmMC1KcE11RFd2TEUyRTA1RUVkczAwcmJBNUV1dVhRS0I2TldvN2Zib1ZNTFJDU2VuNmtlUlQyc1hLeXpNNnhyRQ?oc=5) <sub>NVIDIA Blog</sub>
- 📰 2026-10-22 [TIER IV and Technical University of Munich Bring NVIDIA Hyperion to Level 4 Autonomous Driving in Germany](https://news.google.com/rss/articles/CBMioAFBVV95cUxPaVpqenh6Z3VmU3dEMGxOTlFibU43a1BhNFl3eUhkdzNfS294OXBwQTVnUTJTT3AwaVhFdndxQkpUSkpKS3hJU185Z2ZRck1yTkRqSmFQTkpqczlMSGY0T21CYnctVjMzTFExM0YxNnZpcjhsZVlfYmdGWGRZdnNZNmZUNmFmSFo1MDZiSlV6QkttWTMwTnFqU3FTSktVazFj?oc=5) <sub>Yahoo Finance</sub>

</details>

<details><summary><b>Wayve</b> (68)</summary>

- 📰 2026-10-23 [Automakers Align on 2028 Autonomous Driving Commercialization](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNcVd3V1JhaGFMR3NySU14c3dTNkZrcWZpSktMNWxYOHhGc21DaFpydDIyaXYzZlJJSjlYTXVrSnctTnNuY1VnbHF2c3EySHMzNzNRYmJHZTRpVlFGb2xhSUplQXd1WVdiVFZacHVNQ3lBYUxTREk1c1VxRVd2ZEtDelY2UTBuSGdI?oc=5) <sub>조선일보</sub>
- 📰 2026-10-23 [Uber rival inDrive eyes 2027 robotaxi tests in Central Asia with Pony.ai and Nvidia](https://news.google.com/rss/articles/CBMiugFBVV95cUxOaWhUal96SUMzM0RCbURnU0FPWnNfYzF2Qmtjc09PbjcwUmgzTmFyR1lyOHdtbUNFV0tuX3hMTzhIamtJTGk2cVBFeGI5dXJYOW04NERCU005LVp3NkdUMlVwSjVGYzJJcGZDTElfRVhfYjJYNnpPdmNVNjhlRUtHQ1hwbjZKc1NDNXc3cUdGbWtmNVJrRW1oR2d3SGtmemZfV0s0dmhVT2tqQWtQWHoySEN1SFpiYk5yUnc?oc=5) <sub>TechCrunch</sub>
- 📰 2026-10-22 [Nvidia embraces European automakers](https://news.google.com/rss/articles/CBMifkFVX3lxTFBXc2t3NnFTNEJYRTRQMk1wQWh5NnpmSnozdGc3YTlYV0tMZ01VMjNsY0lYQ2lKWjhpVDRPeXNRSUJMY24wX1hKQms3VGhlTTRVd0pQQXpJTXQ4WDlYNXI1NExYLWZJcmxJNUFzLThVdnF6S0d2TE53MVBEZFZ6dw?oc=5) <sub>electrive.com</sub>
- 📰 2026-10-22 [Fancy car touchscreens? We prefer buttons, say drivers](https://news.google.com/rss/articles/CBMiqAFBVV95cUxNNGc2Z0M4T1lrYjV4WXpJNlhMSXFWT3JXTG9NQnRkQnVLMUZZVXlXQmR0eWxPZmI1cnJDbDB1MEVuTlEwWTVfOFVfR0hoOFVTX29qcmwtdF83ZGdSNXg4WjBaODN2NTFwVDY4ZDcwWU45WTl5YjJ1WEtxc1FKQmloU0U4bUdxT1ctdGRKZWRDX0ZZVUdod21wNFg3cFdVMk1kMmlTeDZLbzU?oc=5) <sub>The Times</sub>
- 📰 2026-10-22 [Zoox Las Vegas Airport Field Report｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBuM3U0cTFKZHF4ZjhlSVhzY1k4dlVoMDhWVy1PaWUtcUJKWF9jeEtEczdXbm0zbjhTUXBiVFBpdWplUm1NNHBTbndsdzM5TTZYM1ZJSjVJNXBQM09iRkJJ?oc=5) <sub>finance.biggo.com</sub>

</details>

<details><summary><b>Momenta</b> (98)</summary>

- 📰 2026-10-22 [Momenta联合JAECOO完成巴黎凯旋门环岛无接管智驾测试](https://news.google.com/rss/articles/CBMiZkFVX3lxTFBNcGU1YzJqb05SUkdqeWFqeHB6SjN1c29tOUNYaE5JQUZUd2tOdlNkOXUxNy1rbGZTdVZNTkROcFBmQlZZQWlJTVZoaUFJMXEwS2JfSEFzeUkxM1NKcHdhV2lya2JJQQ?oc=5) <sub>东方财富</sub>
- 📰 2026-10-22 [China Proposes Exterior Lights to Indicate Vehicles Using Self-Driving](https://news.google.com/rss/articles/CBMiwwFBVV95cUxNM1J0Sm9PT25ZdmxpNGlhVHBPSm5qTTBLdktUZDZ2SDJ0NTRNTXQyelJsdGpyRDNQRENtUThBSTZTdmdVRXBpV3hWLUJfUnVIUFBLbmxjZkhCYnRmM1NkTkJPVE95TzlNSU9sMGdKVjZpMGRNSzgwNzljTjFTR3NLTTN6cW1SNDh3ZEpNbDZwb2E3QTdSaDZvb1AwWjM3bFAyV0l2d2xsYVhuZzNZbVk2X1BDd3Z3RUpqVTRILUU3cmVJNFk?oc=5) <sub>Caixin Global</sub>
- 📰 2026-10-22 [Can L3 autonomy arrive by 2028? Six Chinese auto executives debate "skipping L3"](https://news.google.com/rss/articles/CBMidkFVX3lxTFBIYnJ3LU5mWEFlRXFQa280NEt5NzdoMkFCdjQyOE1SSElncjdRWkp2WU9SekpicTdFbjZrM0NBZTZpdkpGdE90anRkWGxCQTVibjBZSTBnamFsSUdENnUwQmNtUlZYY0FrbzRLUW5pRDZXdFBhdEE?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-22 [NASA Awards Task Order Contract to Momentus for Mission Formulation Phase of Fly Foundational Robots Resupply Mission](https://news.google.com/rss/articles/CBMihwFBVV95cUxOTlJMWFFMX2x2dWM1OFV3SWM1cmdrT09OVVp2eWJ5T0ZxdFNTQWNZRGJJd1BCT2Nidi1fOWozUzBLQUV3ajNSQkNEOFUwT2pBdGdsWFVhMDV4T2h0Q3JGU0stN25vdTcwM3k1cUJyM3Q5NmVmbk9GVFQxbVNPTE5pNDJWZW84LU0?oc=5) <sub>Yahoo Finance Singapore</sub>
- 📰 2026-10-22 [Momenta联合奇瑞巴黎车展完成凯旋门环岛城市NOA首挑战](https://news.google.com/rss/articles/CBMic0FVX3lxTFBoamJ4QWJhVmpyV012akl1dl9lZDhyejc2MWt6SVAzM25xQkpJSVZOVkl1WENHa012OEVhRjQ0TTZtZGY5eGxMT2dqanBncmJRbjdDN1VTVnk3Vk1RTUNxazRSY0g2YTV6aUtMbGRHME1zYmM?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>XPeng</b> (279)</summary>

- 📰 2026-10-23 [第二代VLA全系标配 小鹏G9L与四款大五座SUV智能横评](https://news.google.com/rss/articles/CBMickFVX3lxTE93T3hXVFhLcGxNNlRuQjRGVGNETk9ETURnd3QyOUVBQ203VTRweVF0UGJ5aXFtODJ1Y2FqT3hER2N5Qk9Td1lTeFdOQXpCekRQUkZjb1J6dVRfS3cteWZoX2xKeWhjbFM2VzBWZFAzZFdiQQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-23 [长途不焦虑的大五座SUV盘点，小鹏G9L超级增程与4款热门车横评](https://news.google.com/rss/articles/CBMickFVX3lxTFBOMkp1Mjc1YjA3dzBZdlpoM3hURG5qS1ZnTkFZc3RnT09XdGJ1TzdVdjNEcHhyNG5pdVUwWHZhRGlIOGZRb096LWREYVYtaE9mSnh0YzRybThGekNEbHBhbUJGejJlem9CNzNfUmNuX3dpdw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-23 [周末带娃露营，小鹏MONA L03和铂智3X的后排空间差异有多大？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5Bcm40ckx3RExwM21XVmxzRF9uNGpXZHc1TS1KSFpTS20tQXpCOExEdzgzMHQ5VnpYWnJKS3pKMER4bGVyQ0JWeHI2SmZxMW1zT0dFUXNBTHV5Tlk?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-23 [小鹏MONA L05智驾实测一镜到底 NGP漫游体验#MONAL05首发评测# ​](https://news.google.com/rss/articles/CBMigAFBVV95cUxOdkNRUmhCRkdOczc2RVljUlZSOEN3Sk9KTHdEclZ3SGhqSy1rblpCM0dxRkFBaWo5ZWZIMTFwYlZJOElVUU9Jbk14di1TclFuYU1abkNVcU52N0h6djJzSWpVQnVzOHU5WW95LTBvZnk0bDYxMVNadFAtekNHSXNnZA?oc=5) <sub>新浪网</sub>
- 📰 2026-10-22 [25万预算新能源SUV横评，小鹏G9L与4款热门车配置密度对比+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFB1b1RoVGktT3M2Tk5iNl83anV1MXpwMFV5VHhkQl9CNFdub01GWXduWWtCMjNZeFJKendfMy0zeVFweEZQZnYxVFJrc0NyNmlmUXZ5enFCQVQ5N3VIVklQdl9Fb1V6RUxjRTRFM2JuaEpuUQ?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>Li Auto</b> (161)</summary>

- 📰 2026-10-23 [Automakers bet on intensive in-house R&D to break through; Li Auto and Xiaomi Group both rose more than 4%.](https://news.google.com/rss/articles/CBMimAFBVV95cUxQcmNMN1A2Y2llcnRBMk4zWEVMQnREYmJ3ZzU5djdUZmF5LUlxVFI0T3dvWGFMcjZyTGRNaW5IM2dhLW45MHh3SVVtd2dTNkF6OE9zZjlQQ3lSYm9CV1BJbGJyM2x1MWF0VHczY2ljVWxaUWtEQVhaVGxkSmVnLWJEd1g0VHdRSE9pa3N0SDFLTHh4Rkt1RDVEbg?oc=5) <sub>Moomoo</sub>
- 📰 2026-10-23 [试过理想L8与智己LS8才懂：30万级新能源SUV的终极答案，为什么是神行者8](https://news.google.com/rss/articles/CBMickFVX3lxTE9RTEpXXy1ob3o2dE93c0t1VUZZYUZmZlF1VzFDeVBGck1ieGRWUFdaNjcwQXlOaElZdEw4WnpUMkhlak5fc00yMm5mSHRMYnk2QjFoLUd0TXphV01GVlpCWGdNSEFYeHEtdHozcm8wRHN4Zw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-23 [【视频】理想汽车理想L7 2023款 Pro 5.1万公里](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBMYzVFaE9ya1FRdTZaZWhOTTJDaXQ0bjVrbDVSUjJTcmdCaW5SOGhTVDhGVloycW51RHVqdDVLN3o3UUNNYWJlbVJ3S0VpX2RGakVHdUlFeGhDWTQ?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-22 [长途自驾新能源SUV怎么选？开理想L9、问界M8和神行者8各跑3000公里后，聊聊真实差距](https://news.google.com/rss/articles/CBMickFVX3lxTE1WOHdNWlJfYVRlQ0Y4bzg0N3I5aW5GR2Fybkt6MHE0Zk4ya1lGQ0U3LTU1NlVWaEZpSmJmUlVQQTh3MHBfOWMzc1JYVEpZQUtRREVza3ZaZGNXNjhwUkY2SlBSdzQ2WXdJbHNfRld2Z2lRZw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-22 [China drafts ban on blue driver-assist lamps below L3, new models from 2028](https://news.google.com/rss/articles/CBMirgFBVV95cUxNVWFFUG1ickk2ZzNEQk5uRWZKWVVhRHBNOG05Qzh4M0FYYmdTSllvYzNyLV93alRTRERuTGVBU2lUVGM1dUVWZzBXajVJeHZHYTNIbmpEYTBUbXZYdjNWWjFBejd2bkZrN2psM2lsTnMwcE9BY2RicmQzMERocTZFbkpDeUFVMW9uM1FvYVRWRXFYNU1oMmg4cThVdVhQMlB4MkdyVjNpNnBGb2xTdHc?oc=5) <sub>GlobalChinaEV</sub>

</details>

<details><summary><b>NIO</b> (159)</summary>

- 📰 2026-10-22 [$NIO Inc (NIO.US)$](https://news.google.com/rss/articles/CBMiqwFBVV95cUxONFhhcDRVa2thWHhqbm43OXczT3hKUjVDU29wb2hjWE00LW9vWEJTbGVnRkdHaHE3aDNzUHZSVDFJbmhTekFqX0VUYVRWUDYxWnREbEFia3ZrN092NWdzMEZVNFlxMTJkX1FWT3ZORlVsbF9ZdmYxd3FGdWI1Yld2NnNyeWNsUUtxc3lCN2x1S1V3Z3lUekx5a2FFZ0NGOFpmbGtSYW00S1BMWnM?oc=5) <sub>Moomoo</sub>
- 📰 2026-10-22 [李斌称智驾核心是减少事故，蔚来91.4亿公里避免907万次事故](https://news.google.com/rss/articles/CBMic0FVX3lxTE8tdU03UU9BWUhJYjlBV0VDSkM2ZHNqdkNTMk05MmpOVzE4dF9UWjRLU1VzTEUwbnJTeDR5X3Y3VHhPMEYzeXBneWIyUlI4a1U4MG51OWNyVTl2dEpwYVdUUjZOMDYxSjVrWHJqeC1kMVJxNFk?oc=5) <sub>新浪网</sub>
- 📰 2026-10-22 [李斌谈自动驾驶下半场 蔚来智驾避免907万次潜在事故](https://news.google.com/rss/articles/CBMigAFBVV95cUxPang2SDFJTVN4RVdXM2puVDQ5SUFjQThURUJjb0FFRXBtUDI4TE1KTGRZSzQzYnFLQVVYVkRlbm01dUFsNU04MlM0QTBORUZka2tkT2xmckFhVDBpQk5HM2RvelR1MFQwVUIydmVzaGVQaExNSndyN3M3d09JblVmSw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-22 [Can L3 autonomy arrive by 2028? Six Chinese auto executives debate "skipping L3"](https://news.google.com/rss/articles/CBMidkFVX3lxTFBIYnJ3LU5mWEFlRXFQa280NEt5NzdoMkFCdjQyOE1SSElncjdRWkp2WU9SekpicTdFbjZrM0NBZTZpdkpGdE90anRkWGxCQTVibjBZSTBnamFsSUdENnUwQmNtUlZYY0FrbzRLUW5pRDZXdFBhdEE?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-22 [蔚来李斌：智驾避免907万次潜在事故，安全里程达人驾8倍](https://news.google.com/rss/articles/CBMigAFBVV95cUxOQksxNDlaYmxHZFp2b2lUWktScEFVUTlxZ3JjaXJ0bFhBT0Z4RXJOaFJKSXNhTm5VZmhPcFlLTHctTF9RLWZKRDdLMG5YUDllM3VnUEtLcEwySHg4SXFGNlk0ZFF4d3puejJqUm4xQndRY19QVm5zeVZMWlhvMUtDdw?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>Huawei</b> (357)</summary>

- 📰 2026-10-23 [US blocks two devices with Chinese-made surveillance chips](https://news.google.com/rss/articles/CBMiygFBVV95cUxOdFJzTkxuSjlKbXkwU0NKOFlDMWJOSlhsM01fUm9Sa3h5bVg1UGxFMDEwUE5mMTl2Y0RoeDI4YkNoZWJyU1RpcnhBZjlwekI2eW5DbXpQWVdja1NBZTZaendsQnFBNWk5YjVoWURkUzRYQWUwUHhuYVdKbjZzZ0lEalhRVEVDdG1hbjkwQnF5MDNpZHdFeXhyeHV5OFVScWVTOTF4X3ByZDBmaVFmZ3R4eldRdm1oNE9vRzM4UHpiTE5NNEsyREpMVG9B?oc=5) <sub>ET Telecom</sub>
- 📰 2026-10-23 [Huawei announces Pura 90 Plus with curved frames and triangular camera module](https://news.google.com/rss/articles/CBMitwFBVV95cUxQcV82RHg3YkpLZkJvLVI0NE11ZFl6d0NSdGJtRmFEbzhpUXo3SjJUbDB6TF95bVZpYVlWZ2JxNGlDa0VaQ3VhY3oxNGxUbjRvTk5DTUFQTm1jYnU1elR5T0FlM1dkSWJVR0ZIaTh0dzBQbnZ5S3d0REpwdko1cnpaamxTZDgyaWdMU3pkSVpNNm1SeXdWcTR4WVlTYjU0ZEI4dTB2S01LMmZHejN6ZDdoZGNTa1VPdlk?oc=5) <sub>Gizmochina</sub>
- 📰 2026-10-23 [HUAWEI nova 16s Series Price in the Philippines](https://news.google.com/rss/articles/CBMifkFVX3lxTFBnOHptTGpTd3RPcnA0SXpNSTRvOFpyMjFYSllKZ3NsQWdCbloxek9iR0ttbS1SNDFyVWl2SWJIakVBYk1FS1hYSVVPV2lzTHFrVktpVmhlQXNJdnltUG9pdjNIMXBHejdLd2p3YzZCZW41cDg4ZVg2bHBYaWlLQQ?oc=5) <sub>ManilaShaker</sub>
- 📰 2026-10-23 [Confirmed: HUAWEI nova 16s Series is coming to the Philippines, with prices starting at PHP 29,999](https://news.google.com/rss/articles/CBMikAFBVV95cUxPRVctMGw5SUdLUm1LdzdPRk9YSnVTYkFXMm1KLXA5S2J5cGFDOVVQVXBNbFlzTHlVd3BGSWw3R3VuRXo4MmtHeWZHYXJzT3RWMGNXWE9DOTF0REM5WGJUT1Vlc0YtdVM0MGl6UTVrMjJYUlZ3ZERsb2ZXM3hqYl9OaHV1YWQ0RDJTTC1NdTE3VnU?oc=5) <sub>GIZGUIDE</sub>
- 📰 2026-10-23 [智驾水平揭底 华为乾崑ADS5.0与比亚迪天神之眼B领先](https://news.google.com/rss/articles/CBMigAFBVV95cUxPWmFuRXVTNklXRGpMMTVhc3c3MmZpTzJCM3NobEdtLVFOc2hoMmFKa1ZMUXo1d3NadVMwaUd0SDVyYVM2X2M4RlBEQW9VaWJvTzFuVUtLcnU0b3Boak5hWE9ITnptWnQ0X2ZkdElreGxVSElfZUJyRmNrWWcxZDBESg?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>Baidu Apollo</b> (47)</summary>

- 📰 2026-10-22 [Hankook Tire Expands Baidu Robotaxi Tire Supply from 4 Cities to 10](https://news.google.com/rss/articles/CBMidkFVX3lxTE5WY2pvTkFhWjFJby1lTDRBd2tLeHV4c2RJR0FqeExIRUlYajNRbV9SVzlNZkNrVkgxVlhYdHhDZlQzaE1JREhuYjJKdXctdVRfVWxVbW9lSURnejgxdm9Mb1A3emRVdk9nNHJJZWVKbnliNjU4OVE?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-22 [Hankook Tire expands Baidu robotaxi tire supply across 10 Chinese cities - CHOSUNBIZ](https://news.google.com/rss/articles/CBMiggFBVV95cUxPcWE0VmY0bURKT2NMQndsVnJFZVBpVFBnLUxSMVZ5a2pOR1pVblQwNGlibzlDMU9LQzZzZ3o2ZVcxZHhyLVd0b3RTalhNd0hlRnFzdTBEYXFCcFY1MFk1bEZwVkhucEJxcEcyX3pTdEZ4TmZ0TGpyN1V6UG9BY0hWaGtn0gGWAUFVX3lxTE1tMXNtTW1mUkhMS2N0OG5PbHZvM2lNd3VTOXlTdFpvbHRCbkxFYXZtVm5lMWJxNS16UmRncXd4bUNac1dZaldGbkZUNUtPaVlXRGI2cWNJUlgtMlc2eDdfVmVoN09QVGozTGU3eERJOGd6TzB0aHJ1Y09OZmlGWDJtNm9HamYyU083dEZhb3V6QkZxdXVqZw?oc=5) <sub>Chosunbiz</sub>
- 📰 2026-10-22 [Hankook Tire expands iON supply to Baidu robotaxis in China from 4 to 10 cities](https://news.google.com/rss/articles/CBMiU0FVX3lxTE5fbUZlTzE2cThST2g3RGQ0TzE4RlFTMlRyWFlFTkV2YkRLMHZjUkMtRGV6RWF2NlU5Y1ROeE4wZ1NIbUJqY3kwNllJUzRnRnJUMmw0?oc=5) <sub>매일경제</sub>
- 📰 2026-10-22 [Hankook Tire expands supply for Baidu robotaxis in China, extending coverage to 10 cities](https://news.google.com/rss/articles/CBMiWEFVX3lxTE5oSW9MZURCUEI5ck4xWUFsMDZsY3J6c2dJWTVZcFpGamNWUXpFNUZBamdsdlVyZ0hSalZBS24zQ0hMOE5XR3oxZUx6T3hGX1A4OG9HZ1M0VVM?oc=5) <sub>파이낸셜뉴스</sub>
- 📰 2026-10-22 [Hankook Tire Expands iON Supply to Baidu Robotaxi Fleet in China](https://news.google.com/rss/articles/CBMiogFBVV95cUxQVklEUTl5UnNLZGMwaEVFT0wyWXRrYjhPMUgxLWlmNU41cGk2TnRtSUtsQS1SM0JaUVJ1Tk9YYXFsTE1MUmpLbllfOG85U2lRRndZM21WRmhPeWc4TjJFX3Fad1BfNW9RNUQ5dlNhRmg2NTJKT2F3RzZfSFFYaDA3YUVJR3VVM0RBNmM5V1I5VDJMWndSdjFCS01QTmVnQ2xGRXc?oc=5) <sub>Seoul Economic Daily</sub>

</details>

<details><summary><b>Pony.ai</b> (144)</summary>

- 📰 2026-10-23 [Uber rival inDrive eyes 2027 robotaxi tests in Central Asia with Pony.ai and Nvidia](https://news.google.com/rss/articles/CBMiugFBVV95cUxOaWhUal96SUMzM0RCbURnU0FPWnNfYzF2Qmtjc09PbjcwUmgzTmFyR1lyOHdtbUNFV0tuX3hMTzhIamtJTGk2cVBFeGI5dXJYOW04NERCU005LVp3NkdUMlVwSjVGYzJJcGZDTElfRVhfYjJYNnpPdmNVNjhlRUtHQ1hwbjZKc1NDNXc3cUdGbWtmNVJrRW1oR2d3SGtmemZfV0s0dmhVT2tqQWtQWHoySEN1SFpiYk5yUnc?oc=5) <sub>TechCrunch</sub>
- 📰 2026-10-23 [Pony.ai partners with inDrive, Nvidia to launch robotaxis in Kazakhstan](https://news.google.com/rss/articles/CBMixAFBVV95cUxPd3RfYXZ3VmFIMHVsLWhBUEkxa3NYek5NS3VCQzBUdXlfd1dDeU85TGdBcnI4N1duVEltOGZzemsyUmNUb1N0LU9XeXVHQ05WcVg4dVNzVmVGZXpxa1d4WklnNm82MUtwQ1BGQnlJVzhjd2JQeDExUDRCNVhIUWVnT0NlZnh4OHJHWlBnNEk0Y1Blbm5sUndmSEM5eFVOZmloR1VrYW1EQjZrZFQtR2pGczlYZFpRcVhWT3BaY2t3NWtDS0k1?oc=5) <sub>Investing.com</sub>
- 📰 2026-10-23 [Pony.ai, Nvidia, inDrive partner to assess L4 autonomous ride-hailing launch in Kazakhstan](https://news.google.com/rss/articles/CBMi7wFBVV95cUxNX0F5bElEWGp4dHoybmJBWk40YUhteTdvaHlRTS1jLUhtOUFCekhQZk9fU1JYV2VuVkRhTGhoWjZCdjZ0eW91eF9vU0pybTUyN3ctWWtqVGJmQVBXM3E2OEJtQ3ozVXFLV2lSd2RFb0lJX1ZWeVBaem1idDFZdGJJZ0IxQ2RUT1A1a0FtM1ZTTEo3QUZvSE9WRlctRmJqZ1dZek95SmpFYUt5S1J0aXFLNV9XTy1TMUd0bGtfWDJQVUE0b1k1WXFUS2dpRVNxdV9CT2Z2ajVQY25uaUZYRlR2cEx1TnB0czllQ2IwN1M2aw?oc=5) <sub>TradingView</sub>
- 📰 2026-10-23 [NVIDIA Details Kazakhstan GPU Deployments and Robotaxi Plans](https://news.google.com/rss/articles/CBMiigFBVV95cUxQNXNQT0lLRTVQdzM5OUx1RXQ0RU9ZTzc1SVo4aDVVdEFEcVl1WUVqakJmVTBNTFkxVGpIM3NDc1BhM2Jsc1YzZkIzU3gyMDZ5RnREbUFMV1VSUDRqMDQtS05fRUdMdjJMbl9NRnlyTEVjMXFBQjN3YXRHZ19kcnVqV1plM2hyWDNPU1E?oc=5) <sub>Unite.AI</sub>
- 📰 2026-10-23 [inDrive to test Pony.ai robotaxis in Kazakhstan by 2027 with Nvidia AI tech support](https://news.google.com/rss/articles/CBMirAFBVV95cUxNby0zMkhEekRrMHNXMVFGUGNuZ3RtMWtXeGQyaTdKbGY2cklnRXBCcWx5ZS01RXpyUHJLbnBsQU4wMUxtY0pQVnBEcnFtc3RCWDA4cDVsbFJQQ0tRbE1MX3FIWFc2X0s1dXlFSXFzTXlzc2E2cl9oejR4TXpnRG5JZDFKYUlqRmowLXBxVGZIR0dLbk0zenYyTDZGYXNLTFhySFh6SW0wSVdjeUlO?oc=5) <sub>Pluang</sub>

</details>

<details><summary><b>WeRide</b> (150)</summary>

- 📰 2026-10-22 [文远知行-W盘中跌超5%](https://news.google.com/rss/articles/CBMiXEFVX3lxTE1wODFUX0hOa3gtbmxPMERLczdFb2VvbXVNRllIYkM0c0hNU0YwTmZzMm02bjJQUTBwTm5GcFFkQ2hQb0FWbDc1NFBqYVFvM19wSG0tMmx1U3dTdS1S?oc=5) <sub>www.caiwennews.com</sub>
- 📰 2026-10-22 [文远知行等在珠海成立投资合伙企业 出资额1600万元](https://news.google.com/rss/articles/CBMiYkFVX3lxTE1NUFNrbzZ4MzJOSmhlVU9EZFJId2k3dFA3Z2xOb0d0VXNXOHpObnFRMU9ZQnFna0hJLTIzNGdGc3N0XzdHNHRERmZjaE9wTDBZS2tpaHl1Z2E1bllKYXlCTWl3?oc=5) <sub>观点网</sub>
- 📰 2026-10-22 [芯联集成前三季度营收同比增43.09%， 毛利率创历史新高](https://news.google.com/rss/articles/CBMiUEFVX3lxTFBQMVc3a1F6Zm1XSGc2dlZSSHNKOVoycHJPX0c4M2xXY29XNEVqdjFfWjJkTzRfNnBHem90V1ZaeW9BeUtXRXdIWEpLUDhEZy10?oc=5) <sub>盖世汽车</sub>
- 📰 2026-10-22 [特斯拉Optimus规划年产100万台，周产2万需一年](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9jRkhUWFlFejZuN1NKenQ1SnpKa3NfclVkY25jcktBRTN1U0gtdjlRSTd5eHM4MTdnTk1acFducDVxSWNFWjNua3F0eXh1ZUVFaFVIYzUwTjdzd2c?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-22 [WeRide targets Madrid Robotaxi service launch by end-2026](https://news.google.com/rss/articles/CBMiugFBVV95cUxPczB0TFAwa0hqTEN0M3F0M0g0Sk0tbFZMMGQ5ejB2b2pBSXNPN09lTVNHcXJoZUFtY19DWjlzV2tnSV8wbFpOSk1QM1pYcDFFTEdlbGdIM0tpaHFYMmthSmpKUngxa0ZJaDJIakRRd182Q2lqX0FXU3pZR0IyMk5ROS1yeXk0ZFdkN3llWjA0TV9KV3pVRWlXVWhCbUZjRklHS1ZaU3J5a2lrU3B6XzNQUWFKdnFxcjJhYUE?oc=5) <sub>Gasgoo</sub>

</details>

<details><summary><b>Horizon Robotics</b> (147)</summary>

- 📰 2026-10-23 [又一款“成都造”新能源车入局，捷达M6顶配将城市NOA带入10万元内](https://news.google.com/rss/articles/CBMiZkFVX3lxTE9YZUhBaWYzVGtldnZXVndHbzJadUI2dE41YW1oMzZuWVMyTlIxMkU4RTZVSHhkUjlCeFN5bWhQdFozUFRHMm9wbEVweWgwODF0YmdDNFJzZV9EM2NiR2JWN2luMnN2Zw?oc=5) <sub>每日经济新闻</sub>
- 📰 2026-10-22 [Autonomous Driving on the Horizon: Divergent Paths of BYD, Huawei, and XPeng](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1rSVc4NGFJdGtBOUpsdnhfRjVWU2hTekFiQVZvdFJ1SUtaWGIzWjNhOWtxdHNlNzQ0dlVsQ1lPaFkySlJoMno1Y09UV0JqbHJ5WGZV?oc=5) <sub>36Kr</sub>
- 📰 2026-10-22 [世界智能网联汽车大会，大佬齐了。最有意思的是德系三强一把手都来了。大众说在中国搞研发，2027 年 L3 就绪，找了小鹏和地平线合作；奔驰宝马也都找了Momenta 做智驾。以前是中国车企学德国，现在反过来了。L3 时间线也乱：大众说2027，比亚迪说2028，何小鹏](https://news.google.com/rss/articles/CBMiY0FVX3lxTE5ZNmJYWmlhaG1FazhfUmM5YWRETlVUYTM2NVczcW5UMEMwd0xUVnpGQnd5OWZRVnJqeVRtN05udTlTeEphV1ZNZzRfMm5nVE5jSDRWQW1lWXNla0V2bTQ5TWhxSQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-22 [比亚迪华为同台谈智驾！何小鹏再次开炮L3，六位车圈大佬激辩](https://news.google.com/rss/articles/CBMickFVX3lxTE1MTEVjdXM0aEc1SC1XR0MwLTFhTU5fZ2F1OFdzSjctUGtxYVN6RWRodWxQWlFtRmFMWjBXZ1dSY0NqZ2xESUJoMXpFdVdMUHYxY3NleVRpZ1UwcG1lRGU2Q3Y4V1Uza2I3V2NtMmtaS3NCQQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-22 [VW pools driver assistance development in Europe into new unit](https://news.google.com/rss/articles/CBMioAFBVV95cUxOYlRrdld3LWpvbktqOWtJWUk5UzNrcWNzdlZ2MUE5Yi01ZVY3YUZTcVJPMnpyMjVmQzhXbVBMODBTTUVSWE1lMUxiaVpJbXI1U3VhRkptalRuMkFqR2pTa2Q2aDVmcUdNb1ZFVmx0NFpXLUM5QXA2WWtjamo3RkpRTWREcDBvcHdvRkNHSmRBNjk4YlRmMmhPRXNaWTV3V3Zr?oc=5) <sub>Yahoo Finance</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (32)</summary>

- 📰 2026-10-23 [超5200只个股下跌！A股跌破3600点](https://news.google.com/rss/articles/CBMickFVX3lxTFBFOElzMjBpNzhSb21lWDN2c1BwaHhZeHowVW1MQS1qQ3NNeTJ2S0N2aXBzV0dNSjdKQUNWcGtSODBMbV9Ha3NGdkh1LUh0WTNzeW85X1ZweGUtaG84XzFVR2pyT3hPdzJONVRSV1JveWVYUQ?oc=5) <sub>finance.sina.com.cn</sub>
- 📰 2026-10-22 [赛力斯首款量产车，不选华为路线，这台溜背SUV 有点不一样\|赛力斯\|AIVA\|ME7\|华为\|宁德时代\|元戎启行_新浪新闻](https://news.google.com/rss/articles/CBMiY0FVX3lxTE5Jb0pMdllfRElOZEdGNHplUXgyUlpILTIxczJmeElDUXJpdUtZS1o1cHlHZ1lCeUlQT0FPdDZ3bUxNbU5XQ0RHZkpQVU9PeWdhdFRhd3RSZkE1WHVGMWxKQlBDTQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-22 [空间短板彻底补齐！近5米车长配3050轴距，赛力斯新车亮相](https://news.google.com/rss/articles/CBMia0FVX3lxTFA0NnZNRk84WlNyWFJfVEYxSmpMVHhsT0lzanVBQjd4bGpIOU9GVWtLM0tZU3hGa1hrcXgtbzNVX01VclREZ3hpTWFhZDhXaURiaDJLMFFCNjYwS2lmd0c2LTYxLWU2TXo5M3NB?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-21 [新芯航途完成战略轮融资，雷诺集团首次投资、奇瑞汽车追加投资，历史累计融资约50亿元。](https://news.google.com/rss/articles/CBMiVEFVX3lxTE4wNTZCVVA5R1ZTTmNTWFZIZXVkbVlza09lSDFETkpqTWdaNzdDVk9EeDJJTmdHVTJXUmlQbWFrc2UxVUVUbGhyY2JEek9SeFpDaFdJTQ?oc=5) <sub>虎嗅</sub>
- 📰 2026-10-20 [2026 国内 L4 自动驾驶企业盘点：魔视智能、小马智行、百度 Apollo](https://news.google.com/rss/articles/CBMijgFBVV95cUxNV3VKQ2pmYmJ4RWhCQzN0RV9Rbkk1SDF4dFpjNngxR2VJS05HbFJBUXBWMGZwSTlNWllUY2dtc05ueWJuVElaWGUtVlAyWW5KNVJPU09WUmhHdUYyOXlIWjViekMwZTAwWXZBRGtydVpmUEpKQmZkSThlejVwRUo4SDVyRGh6UUxnTXNCUHl3?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>Mobileye</b> (19)</summary>

- 📰 2026-10-22 [Mobileye Achieves First TÜV SÜD Inspection Certificate for ADAS Development](https://news.google.com/rss/articles/CBMiygFBVV95cUxOTHZRQjV1cnA1T01OSC0yZ1Z5TmtOVy0zRHhtNGcwTmw2NGhoeVJsR1BhbVpEbnFLeGtYMkxubGFpVUxIelFVZlNBcVlMUlFwT0NMdE5TM3JVTnhpcW9HekxZUVdOOXFYY3otb3ZTd1FRU0hISlIxb3g0eURSME11dlFxUUtTdFlGNlZkS0RIekZSeGQ1WW1rRjdNbVI3VUZ5RUs1RXpid3B1WV90MS1LQzc1aXBpZ0VzRXB3V2J0eGJ5dFUtQnhWNVlB?oc=5) <sub>Business Wire</sub>
- 📰 2026-10-21 [Intel Banks $150M Paper Gain As Joby And Mobileye Rally In Q2](https://news.google.com/rss/articles/CBMiywFBVV95cUxOZVNKbmU1VlRTYVdUcExFLTRvdXhPLWJ5MkJyUFVMT3RMMlFvWjI5ejFPVjBfVFlET0p3RG04enRyd09pMHdpLWFZME94OXFoNHdFdFBJbXNMekRhR3pfcGstVmRWMTBEcHViMDdBaWxSLVRPNHhNUlZLYkRlcE1xM1BoS1NIWmpQUk9zQy1oUm5Fd1BOUWkyQkpGQnF5YUltUDAwS0tEYnJ0c2hkNVg5ZWFGalpxTTU4V3JyU3ZVc3MtazFJeXdkVnhHNA?oc=5) <sub>Stocktwits</sub>
- 📰 2026-10-21 [Mobileye cut to Underperform at RBC Capital on ADAS displacement risk](https://news.google.com/rss/articles/CBMiuwFBVV95cUxQbGV2OURKazdBc0c3ZlkwTDg1aDBENU5uN0ozYXRaQTBzWnNyX2hEWjI5Tm9FSDkybXBsVHFnNjJHaW9OaGg0NUsxY3Qzd2dKRUx4eUhBSW5EU242VVEwV3lKU3k3ZkpGUFpYTzdVNnhXQjVzU29YTVdCYndDOElCQkNVd2l6RzdkQ1ZyMHhsc19TQVJVS29kSmtoaGFfZkhxWkZMWEczLTlvSk1Ga2pwUWdBLTgxd1BnUmE0?oc=5) <sub>TipRanks</sub>
- 📰 2026-10-20 [BlackBerry Climbs 6% as QNX Royalty Backlog Tops $1.2B; Aptiv Edges Higher, Mobileye Global Holds Steady](https://news.google.com/rss/articles/CBMi3AFBVV95cUxPWk9iSUpIeHRDOXd4T1NSYnlfYkJVNEJaLUlONWpKSFBPdFhsVHhGMjN2VDRBeS01ZDViX3E5ZWQ3QUU5UGtZUDFfZXpkenJfZHREZXhOZGMxRVM2MHloMGFheVZkNTQ1b05xRHFWeG84cXFIc2x2NjJYcDZaRkEteExDTk5iTnBxRGczYWtGaWZ0U0pIQmVpNVEwajJwS3ZzZ2ZYQV9UbUJ0OWwyVlNDWlFqZGtsUTR0cHpnd1hqWk1yU3VwMllCYTIyLU1XcnNBOFJEbE5IU0NNQnNo?oc=5) <sub>24/7 Wall St.</sub>
- 📰 2026-10-19 [DoublesAI unveils CEM AI model to cut computing costs by up to 67 percent](https://news.google.com/rss/articles/CBMiuwFBVV95cUxOUWExeFBKN2RaRFduZUY3UGdHZXNjdGxEWklyRnByX1oxcWhidEdUbjlnbTlQQ2tRMlZkT2NCazZkTC1wZTJtVEtTMWhhOUl0cGVOSmstdllLa3N2UVFsd0lQM00yVmg1THVKVVF1TlA1ZXkzY3FIZGVZR1lsOHNucnhCcEdEcTB1cS1LbDZ0aGxuQjJodzd3VE9md3MxZzQ2aG5nbGpybnRKN0FQR1ZXRG92TDVoR3dGU2VB?oc=5) <sub>디지털투데이</sub>

</details>

<details><summary><b>Aurora</b> (52)</summary>

- 📰 2026-10-22 [How does a driverless truck get refueled or stop at a weigh station?](https://news.google.com/rss/articles/CBMivAFBVV95cUxNU2tla05zSVRfNTd6cEM1Z0M1MjZxdHo0X1BaMkpBekpTSUpRamxacVJiVzBhSGtrSUZOSXV5RkZfdHBoUkFOR05hSkFrREk5dXFKN0hWQ18tZVNWRTJpS2xMY0JBcEdGWW81czJPeENibVFmTUJFUGtUNVRmdmc3eldQT0tSS20wX1prcXpDc1RTMEhlRDV0V2djd09YWVJobkV2VWlPQmktaUY3SWw4bDVaTVVUd3drOVRBVg?oc=5) <sub>Truck News</sub>
- 📰 2026-10-21 [Federal Motor Carrier Safety Administration (FMCSA) Grants a Crucial Regulatory Exemption for Autonomous Trucks](https://news.google.com/rss/articles/CBMigAJBVV95cUxNQjItT3d6TUxmeUxoU3pjMzBFeVlWbDNxczZSRER0U1c0NFdwOTlMX2kyck1PWnpjbDkxOVdtX0tYY3RUbHd0Ymt5TGJrX1BUczFhVFVHYkxCb0xtQ2hZSFRVVjM4Z2VCZmV4NGt1SHhZNm9XSGhybGc4NWFxc3BvTTlPZVVtX1FZTmV2bkJ6WDI3NU1MdElqcThnazBaMl9PeDVOR243THctYXNPRF9SUnFTUnVhQmo0RnJ6T2N5LVZtSVAwQWpLSHFqMFN2RzNzYnA5T3NGUVNJVDB1RzBwRTl6b3lmRWNJb0loVzdjQUNFdmVHV0hmYnl2YWFXOTQ2?oc=5) <sub>Sidley Austin</sub>
- 📰 2026-10-21 [Aurora (AUR) Is Scaling Driverless Trucks. Can Revenue Catch Up With the Spending?](https://news.google.com/rss/articles/CBMiowFBVV95cUxNRVlhdGZlNW9kbG91b2IwcWliTjExLVBmVXRsbnV0Rlp5RXNrN0FfaTc5SVpiNzRxZkdZZVhFZnExa3hPVE5TZnhlSnF1VDJGQ3BrT3FDWUpUS1E3LXBOTGlSYXlHVGFJV2FPemcyb0pDNHlEdmRmQ0Q5NnpNaVNzZXFTUE5RS20wb2ZtMGVUeFY5clRRZUJHWHJmdmpfeWUzMnI0?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-10-21 [DOT Grants NAM-Backed Waiver for Autonomous Trucks](https://news.google.com/rss/articles/CBMidkFVX3lxTFBFeWxvajNoRkNDckxWcS1Yc0l4dGpWZXRhaURHLTBfUTVVcjBSdEZldlNUT1M3eERUSE9iUXBJd0I1Q2N0T3ZUQTFhaThPZVZRalV2aTl6bzN6dFUySnpFcWcxb0JZVGQtRWRJSkkzX0JMN0U4MXc?oc=5) <sub>National Association of Manufacturers - NAM</sub>
- 📰 2026-10-21 [These Texas companies made Time’s list of the best inventions of 2026](https://news.google.com/rss/articles/CBMif0FVX3lxTE9weFZ5ZUc5T2lkMFVBTGlORUZBVzJEWWVwSU00WmJwRWtJcGxsYS1ZZ2diMHA2UlRCanY5LUlRYnpSXzhsQkxpYk1mZGl2emhwU0UyZHNHUlkxa0hrZFZhMVpyYUFoeC1paS1zdkZxSmlkRnZFX0xOaUtRMXl6WjQ?oc=5) <sub>AOL.com</sub>

</details>

<details><summary><b>Zoox</b> (63)</summary>

- 📰 2026-10-23 [150 Amazon Robotaxis Could Soon Be Moving Into A Santa Monica Parking Garage](https://news.google.com/rss/articles/CBMirwFBVV95cUxOUEdVWHdvbnRvcGdsbUdsN0Jncmd2QzJRMF9kbVFWNDdnOURCaTA2MDdscGctWVREbzBxdzY2d0VQWUJPbUs1UzRRUzkzSEtqV1hucGNiM3BRS0J2M0I1NVNPeE5SU0JCZ2tVcGdSWDZjS3BXR2dVbjM0U1pGZDlQSm1oMEYtSXZILXZRcC1DSEF3SHhMZ0g2a3RYRUV0WlFkdm5xT0xwa2c0ck1RWXRB?oc=5) <sub>Patch</sub>
- 📰 2026-10-23 [Automakers Align on 2028 Autonomous Driving Commercialization](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNcVd3V1JhaGFMR3NySU14c3dTNkZrcWZpSktMNWxYOHhGc21DaFpydDIyaXYzZlJJSjlYTXVrSnctTnNuY1VnbHF2c3EySHMzNzNRYmJHZTRpVlFGb2xhSUplQXd1WVdiVFZacHVNQ3lBYUxTREk1c1VxRVd2ZEtDelY2UTBuSGdI?oc=5) <sub>조선일보</sub>
- 📰 2026-10-22 [Tesla Delays Unsupervised FSD to Q2 2027, Robotaxi-Only](https://news.google.com/rss/articles/CBMiggFBVV95cUxQbDI3WUtQRU9wLUpiZWFieW5nSzdaSnFmY3FsSE11ekRZVDM5MUdMRE5Oa01nZ0VCYjMtUTZoYkpjNkR5aVVEUWFWMUpPMV9IRDNJYnh4UFpuR0lRUkRvb2JtZDR2d05sRUt1UkljMnVyQlgyRFl3R1p4TEtvYnNXLUhn?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-10-22 [Zoox Las Vegas Airport Field Report｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBuM3U0cTFKZHF4ZjhlSVhzY1k4dlVoMDhWVy1PaWUtcUJKWF9jeEtEczdXbm0zbjhTUXBiVFBpdWplUm1NNHBTbndsdzM5TTZYM1ZJSjVJNXBQM09iRkJJ?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-22 [Santa Monica Eyes Zoox Library Parking Deal as Waymo Dispute Continues](https://news.google.com/rss/articles/CBMi-AFBVV95cUxPcGs0dE1tY1NIWUNsRVpwbzA3ZjNxT1kxREp6MG50TEpTcW1OSUJLMVBMRl9mNzdXc2h2MmFxb0JCeXNpanlINzQ1MFJ4cF9pOHM1NVlodFlKYXpxQ1FoNUdPRGlUdXoxejAwb2Z6UDlRTk9CVVhJYUdpbWJ1aGtTWnVPUjMwR2RGODdWZk9Hck1oVnNNdVdjeE15LXpodFk4NEpoRlNCSkh5TzZWWlM3ZTlobi1fMTNMTXBEazRMdHlpeUxtNnliLUNwRngzNEhDWkNVWjZfeUxQRUlHcm1XYkxoM0lYVFR0d0VSX3JkM1FWclFmLW55YQ?oc=5) <sub>Westside Current</sub>

</details>

<details><summary><b>Motional</b> (16)</summary>

- 📰 2026-10-22 [Zoox Las Vegas Airport Field Report｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBuM3U0cTFKZHF4ZjhlSVhzY1k4dlVoMDhWVy1PaWUtcUJKWF9jeEtEczdXbm0zbjhTUXBiVFBpdWplUm1NNHBTbndsdzM5TTZYM1ZJSjVJNXBQM09iRkJJ?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-21 [EU Regulators Open Probe Into Booking.com Over Fake Listings and Phishing Scams](https://news.google.com/rss/articles/CBMidkFVX3lxTE1Rd2lBWTFiT2s0UG55ZzNOS2NlQ1JOQkVPX3hwSEhRQ2tTa0ZpS19telVJUmRSclZnZXlBSEF3eURRcnNTUDFIaVZ3VG1rcUFXc1cwOVRiU2hIMnFDY0pGTVVVcTZ6U1Fhc2JVSU9xdkI0eTRiX1E?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-21 [Taiwan Blocks Grab's $600 Million Foodpanda Deal, Citing Uber Ties](https://news.google.com/rss/articles/CBMidkFVX3lxTE9sZHZrRlE3bFZXdlJoUEg5azRoMTJiUnVyLVNKWmNaYVgyeDdGZVJ1bEFTN196cEhuaTFJVFVhVW5fdG5aanN6d0s3MmJmVFQ5Nms3OTBCek1IS09nSkFfLUdTV0pDMkR0TlZTNlltWUQtM1k1V1E?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-21 [XPENG Next Generation Pilot (NGP) Field Report｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE4xUFBoMW5mRlRQenVJWmVBMHhyMU5HV3VGQXBzQVhYMXVPXzhKeEhRY2Q0d1pKZ2hTcm81X0pSMF8yUGRwYzE3QlVVRko4YUlNNUhncUNzbTZhSkVveTBF?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-20 [China's CATL posts 14.54% rise in Q3 net profit to 21.246 billion yuan](https://news.google.com/rss/articles/CBMidkFVX3lxTE1VaFpob2tDMTR0dDMtMmNOcks2V1M4V0pKWmltNTY3VmRZNE43UHZxaHRRQW9hOVVjWWFzVkxWdmlpaDRoWUVuN0xISzNUVnZsMVVYU05CMWx1ZDctS1EtdzhDbVVqS0laSGJDbkFtRExycnJRV1E?oc=5) <sub>BigGo Finance</sub>

</details>

<details><summary><b>comma.ai</b> (5)</summary>

- 📰 2026-10-21 [Is the race to build self-driving AI turning into a cyberwar?](https://news.google.com/rss/articles/CBMikAFBVV95cUxPd1ljS1V3ZmI4RGdJZkRQdVpkNmRqcm5tVUtpRllXYWMyQ2ZnaFFKRzgzY0VaUDNTR3VwYV9lRHI2RnRUcV9za0p3bTNsMGJmSHNZUlR0MDFsYm1FLTVtUEl1UEJhSi1hXzMtc05tendPaDltRzlMczQwRkx0dTZJaGVjTk1DOXp1cVpSS2Zqc0w?oc=5) <sub>Yahoo Tech</sub>
- 📰 2026-10-21 [SquachWatch Turns ESP32 CYD Into Standalone Privacy Scanner](https://news.google.com/rss/articles/CBMikgFBVV95cUxQT3EzRFl0MWRwUm1tYklBYngwR0lDVGswYUJ5TUdQNjdPdkJLajV0bklVU2FCWFdMUlJjMng5NEc2ejQyUV9MeHB4RjF2UlRxQ1pUdFpSTWlETVU4WmFxTVpLTmJ3Z0NPX3ZnWEc2M09VcDZRNmtlUDlBZU5hQmFrUlNWOHBCRGtZQWs1Z3Z4TlVBQQ?oc=5) <sub>news.lavx.hu</sub>
- 📰 2026-10-21 [IQ.Lvbs claims hack attempt traced to rival Comma.ai IP address](https://news.google.com/rss/articles/CBMilwFBVV95cUxNVXdkQWthMXBaOUd3aGV2Nl9Kb28ydFVOcElQcTUwRnEyWVF4NTVzOWd4d2hDSlFFbjc3Y2hranNuOUtSS2dha2NKYzRvUkxzSlJxSGhQZTI0MEVySU9UOVpjUlVSUEpPTl9LcWhhNWJzLXdQaEhNMnRCZUVGd0dDTEZFYzdhcTdsQWNkczU1X0UtWTdJbXdN?oc=5) <sub>news.lavx.hu</sub>
- 📰 2026-10-20 [Auto tech startup claims it traced hack attempt back to rival's IP address](https://news.google.com/rss/articles/CBMizAFBVV95cUxOVHlZN1E1cDJqNEFHSFg3U1hCbnZRdFhtdk11blVLd2d2dUNIVkYxUG1xd0NIWjdNZGNVMHJvalh4SEM2cTJhclMzWHRyR0thRWJDMHFNUWcwNHAza21ybFYxV1Zyd2ZoaHRORmRtdGxBbWlSWk1UUnllQVp2dGFCVlFjcE0yOG1OaW9hdGhRb0lpS25LeUZFc2pKem5QaGVnZ0pLNExzeDdUOGNERVM2andndkh4LW5JWDdaSGhqQmZxOFMtb283aDFIWkE?oc=5) <sub>The Register</sub>
- 📰 2026-10-20 [2400 miles with Comma AI, Android Auto, YouTube Music, and other various tech](https://news.google.com/rss/articles/CBMisAFBVV95cUxNeUNQVTFnMUoxMUpGT080WUdQMHlSVTBDdWxFM3lGRndwbmtZZnZGMVFZRWpDb3JoZllSVk1ZaUFCUHM0TmZTeng1bXlvQUJ4S25rSW9uZFljSExya0FPblRsMTEtZkUwWVhyM1ZqNkx1V01jbFBqdURfMlU5TmJHWnVqQV9aWUhrdUhCa25PN0tRalctSmpWYUkzOGVJUUxxUmFIeXIyczRlVGhqUVFIcQ?oc=5) <sub>Pocketables</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
