# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-10-24 · 1,297 papers tracked · 42 curated.

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
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 12 | [⭐ 522](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
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
| [STAGE: STyle-controllable Action GEneration for personalized autonomous driving](https://arxiv.org/abs/2607.29517)<br><sub>Zihao Liu, Xing Liu, Yizhai Zhang et al.</sub> | RA-L<br>2026-07<br>📑 1 | [⭐ 6](https://github.com/CarlDegio/STAGE) | Driving style refers to the behavioral preferences that drivers maintain during driving, shaped by their diverse experiences, habits, and needs, and is typically reflected in varying levels of aggressiveness |
| [A Survey on End-to-End Autonomous Driving Training from the Perspectives of Data, Strategy, and Platform](https://arxiv.org/abs/2610.00926)<br><sub>Chengkai Xu, Yiming Cui, Jiaqi Liu et al.</sub> | arXiv<br>2026-10<br>📑 5 | [⭐ 109](https://github.com/Jiaaqiliu/Awesome-Training-Ecosystem-for-E2E-AD) | Autonomous driving is a cornerstone technology for the future of intelligent transportation, where end-to-end learning has emerged as a transformative paradigm that directly maps multimodal sensory inputs to driving acti… |

## 3DGS / NeRF Reconstruction & Sensor Sim

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DriveWeaver: Point-Conditioned Video Inpainting for Controllable Vehicle Insertion in Autonomous Driving Simulation](https://arxiv.org/abs/2606.31918)<br><sub>Junzhe Jiang, Zipei Ma, Zijie Pan et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 16](https://github.com/LogosRoboticsGroup/DriveWeaver) | A pivotal step in autonomous driving simulation involves inserting foreground vehicles with predefined trajectories into simulated scenes |
| [Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796)<br><sub>Leshu Li, Jie Peng, Yang Zhao</sub> | ICRA<br>2026-06 | [⭐ 14](https://github.com/UMN-ZhaoLab/Pocket-SLAM) | 3D Gaussian Splatting (3DGS) has garnered significant attention in Simultaneous Localization and Mapping (SLAM) due to its advances in capturing fine-grained geometry features and synthesizing novel views |
| [NIDAR: NIR-Guided Intrinsic Decomposition for Scalable Scene-Agnostic LiDAR Intensity Reconstruction](https://arxiv.org/abs/2609.36878)<br><sub>Junjie Zhang, Jie Yin, Kefei Qian et al.</sub> | IROS 2026<br>2026-09 | [⭐ 22](https://github.com/Zjj587/NIDAR) | LiDAR return intensity provides complementary surface-response cues for robotic perception and state estimation, yet many simulation pipelines omit it or reproduce it using reconstruction methods that require real intens… |
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

<details><summary><b>Waymo</b> (225)</summary>

- 📝 2026-10-16 [Hello Toronto! Waymo is En Route](https://waymo.com/blog/2026/10/waymo-in-toronto) <sub>official blog</sub>
- 📰 2026-10-24 [Tesla Robotaxi vs. Google Waymo: Who Has the Advantage in Autonomous Taxi Commercialization?](https://news.google.com/rss/articles/CBMi4gFBVV95cUxOWGpHYk1JM1BiTWNTS3lGU1VkX0F4a0RwUENxaHhqYklZUkNHY05IUnFPY2FfOFVGcDF5N0NiT0pfTGFxc0hLZ3lLd0JKdDF1c0xXb05CanRMUGpfWWdsb0tiWmVDODU4WDdENlgzdk1fMHVRdzdTMzdfalA0cmxkRlFTeExTVVd2MFlna09UUzR0N3RiRjBYcmwyQkNPOGRNVzlPV0lmdEd5X3BtR0trejlVc21DNm9pTl9vR1RnSC1jU1J4N1g3SmVaM0NmRFZEOXBvSW5KVVJzSVNaYWNiS09n?oc=5) <sub>TradingKey</sub>
- 📰 2026-10-23 [Waymo founder predicts ‘landslide’ robotaxi adoption in Singapore, driven by high car costs](https://news.google.com/rss/articles/CBMi0gFBVV95cUxOelVrcFlIWEdRSTFKMzVmNWF1UUFCUnpJY0JmcmlxRFhWYkp2UzBpN09WQ0x0SDhXWVQ1a2tUNV9nTVNQZWY2OGs0OHhQeHFNLTMwS2hLYXhaOGR3VTVHM2l1c1RSSy1QMi1nTG43ejlDOTF1cmZjVHo4MHNQWHRoRlctNmo2dkxWZklSNUU2cEN4ZzhPNU54XzJoaS1LNmtXdHFkQ0k3RVZWdEZsT1VzclVxblBUcDJ1TWJLWHROZGdHT3lRanEzcEZkOHAyZlZrRHc?oc=5) <sub>The Business Times</sub>
- 📰 2026-10-23 [Automakers Align on 2028 Autonomous Driving Commercialization](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNcVd3V1JhaGFMR3NySU14c3dTNkZrcWZpSktMNWxYOHhGc21DaFpydDIyaXYzZlJJSjlYTXVrSnctTnNuY1VnbHF2c3EySHMzNzNRYmJHZTRpVlFGb2xhSUplQXd1WVdiVFZacHVNQ3lBYUxTREk1c1VxRVd2ZEtDelY2UTBuSGdI?oc=5) <sub>조선일보</sub>
- 📰 2026-10-23 [Union concerns keep Illinois self-driving car plan in "park"](https://news.google.com/rss/articles/CBMieEFVX3lxTE0zZExRVkJtcWlkajAydjNsOGNXOEU4ekNBYnF6ckhxZHFXTWZMTzNENmZWRHdjakdkRzllalhVSVdaRFk1dWd2dXBybkpaSS1aNEsxUzFzbTFmMUc0RWpuS2hUM1AwbGVKaHlnUnJMZUxJdERjd3lDRg?oc=5) <sub>Audacy</sub>

</details>

<details><summary><b>Tesla</b> (354)</summary>

- 📰 2026-10-24 [Elon Musk Says Tesla Cars' Value Lies in FSD Service: 'People Are Buying FSD With a Car Attached, Not the Other Way Around'](https://news.google.com/rss/articles/CBMijwFBVV95cUxPT2pPQjVyNzBvbFk4OEFMTFdLaHRfU09PMzBtQnNHN0ZwOGdRTG1NdTRob05vQU1pSzhhelVLUmZKU2l6T2E2VWVLWkpuaWxoakRIVmJUeGo4TmNMRDh0TWFNSHNJNGNZZ0VIendReHZFRllZN3V3bktRVEs5YVdwVDJob0tLMkRCOXZlYldrcw?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-10-24 [Musk: FSD Is the Product, 1.74M Subscribers [2026]](https://news.google.com/rss/articles/CBMigwFBVV95cUxQd2NOUzVKMVlKY0d2Y2d0eXVMcTBqSWNCejVpOXFRRV9XM0FyLTJock1fOHNCR2tWcEg4cHY2eFlIZTlJUHFIWVU4TmhhRlhXcEZCRUw4VGkxVVBxbTZKMVBpcHR1ZGE5N0xZZUM5cm5qQ09uQmJJUGRsUjlXdHdZaFdOYw?oc=5) <sub>tech-insider.org</sub>
- 📰 2026-10-24 [Tesla's Robotaxi: The Math Behind a 2027 Profitability Bet](https://news.google.com/rss/articles/CBMiugFBVV95cUxPUEhwMnpILXIyRTJHOW5qZXhYT3RIU1NVdUZ0YzEwaVJWMEFmdGpXVVpsdUY4UEVSUHl1TUhMaUdIVWJrVTFFMy04ODRUUzR0b1dFZFhXdWxVdWhXam85NlY5X1VkblVCNXJILWJ6MC1xQ09Ld29aTVhueXZLNFdHZ1FKMFBiX0RUR2tCUDgzelhYemFwYzBuQnZVdTJsUnQ2WXZTSTRDWEpPbjN3QVZzMTZpZi1uVUdGMHc?oc=5) <sub>Gasgoo</sub>
- 📰 2026-10-24 [Vallejo: Man Killed By Tesla In 'Full Self-Driving' Mode Is Identified](https://news.google.com/rss/articles/CBMilwFBVV95cUxPZ0tuY0tIUVJYMW9pTldxa05sYS1ic09zTlZ1NXl4bVpPUTZXeDJHYzdFaDl0RVI5cEhSQkR6TWVYZl9pUWRQSzU3VUJWd0VEN0FTaHFFcWMzUkw3UURSaDFDSEZFbWRiQ2VOblZ1UVBmS1ZxUTg0UlpzTUpEdnlkWkR0Xy1NRmRIOFMwLUZDLWFMMzl1RHp3?oc=5) <sub>SFGATE</sub>
- 📰 2026-10-24 [Tesla Robotaxi vs. Google Waymo: Who Has the Advantage in Autonomous Taxi Commercialization?](https://news.google.com/rss/articles/CBMi4gFBVV95cUxOWGpHYk1JM1BiTWNTS3lGU1VkX0F4a0RwUENxaHhqYklZUkNHY05IUnFPY2FfOFVGcDF5N0NiT0pfTGFxc0hLZ3lLd0JKdDF1c0xXb05CanRMUGpfWWdsb0tiWmVDODU4WDdENlgzdk1fMHVRdzdTMzdfalA0cmxkRlFTeExTVVd2MFlna09UUzR0N3RiRjBYcmwyQkNPOGRNVzlPV0lmdEd5X3BtR0trejlVc21DNm9pTl9vR1RnSC1jU1J4N1g3SmVaM0NmRFZEOXBvSW5KVVJzSVNaYWNiS09n?oc=5) <sub>TradingKey</sub>

</details>

<details><summary><b>NVIDIA</b> (246)</summary>

- 💻 2026-10-20 [NVIDIA/flare-local-inference](https://github.com/NVIDIA/flare-local-inference) <sub>GitHub</sub>
- 📰 2026-10-23 [Einride to trial Nvidia Alpamayo in autonomous trucks](https://news.google.com/rss/articles/CBMilgFBVV95cUxPQjJyeHBLMXA3dVBFTTN3WHlRMVg3NVJkX1RNaDhBcFdOcHpZYk8zemlJV0hiQzlza2hKenNzaDIyckx5VjZ6VGk1OGtzUmJjY2NqNUtkNHBtaFhFRlg3cGE2aHowSVdnY3JlM1g1WlhpRnRiSlBzSEdTU0xzY3FUcjBkRVpGMnZjMU5rNHN0Rmh0Q0g1TUE?oc=5) <sub>Automotive World</sub>
- 📰 2026-10-23 [NVIDIA Details Kazakhstan GPU Deployments and Robotaxi Plans](https://news.google.com/rss/articles/CBMiigFBVV95cUxQNXNQT0lLRTVQdzM5OUx1RXQ0RU9ZTzc1SVo4aDVVdEFEcVl1WUVqakJmVTBNTFkxVGpIM3NDc1BhM2Jsc1YzZkIzU3gyMDZ5RnREbUFMV1VSUDRqMDQtS05fRUdMdjJMbl9NRnlyTEVjMXFBQjN3YXRHZ19kcnVqV1plM2hyWDNPU1E?oc=5) <sub>Unite.AI</sub>
- 📰 2026-10-23 [Einride to Test NVIDIA Reasoning AI in Autonomous Trucks](https://news.google.com/rss/articles/CBMikAFBVV95cUxNUWZVWGM5Q3FTa3lHTE1XYVlGMFd4WE5oZzUwbTZMMWlEOGxKcURuWjdNdlN3LV9IaXdZOHBkaS1VZkdoWkJ2LTBUWjZBRDlvNi1vckhSSk1hM3dzcUluMXNqUWQtUk5OdzJVMkxJb2NkSVZfR2h1YmpIQzlwcnlreTFTcE5VOHBtN05pX1RBLXA?oc=5) <sub>Advanced Clean Tech (ACT) News</sub>
- 📰 2026-10-23 [Wayve, Stellantis and Nvidia team up with France on self-driving cars](https://news.google.com/rss/articles/CBMie0FVX3lxTFBKR2VWYV9kTV80VVRWR0I0RkhjaDNMUFJxRHJHdVRjbDNBTkNCVzRRLTYtamNmM1J4eVBhR29tR1JERUttVllTWXRDamRlbm1MTG40ZEJnUWlUQ2Q1cnhGcER1UzIxMnJ4NXFpd2FsWC0tV1ZCSVJsRGQ2VQ?oc=5) <sub>The Next Web</sub>

</details>

<details><summary><b>Wayve</b> (68)</summary>

- 📰 2026-10-24 [China's Baidu tests robotaxi on London streets, World News](https://news.google.com/rss/articles/CBMifEFVX3lxTE8tWW5taWpYWllPUkx0WVE1S2s3Y1B4UDEzTHliWWpDaWZfOFp5RklzejNuSEJBNXJSZ0h6UlV0R1E1QTJNVlZaTjQ3NFY0em9NalZOeHdaZzFrYjlFWG1CUnBESExUVV82d21fb1Z2UkhOTmw0SHVVeUVhYW8?oc=5) <sub>AsiaOne.com</sub>
- 📰 2026-10-23 [Uber rival inDrive eyes 2027 robotaxi tests in Central Asia with Pony.ai and Nvidia](https://news.google.com/rss/articles/CBMiugFBVV95cUxOaWhUal96SUMzM0RCbURnU0FPWnNfYzF2Qmtjc09PbjcwUmgzTmFyR1lyOHdtbUNFV0tuX3hMTzhIamtJTGk2cVBFeGI5dXJYOW04NERCU005LVp3NkdUMlVwSjVGYzJJcGZDTElfRVhfYjJYNnpPdmNVNjhlRUtHQ1hwbjZKc1NDNXc3cUdGbWtmNVJrRW1oR2d3SGtmemZfV0s0dmhVT2tqQWtQWHoySEN1SFpiYk5yUnc?oc=5) <sub>TechCrunch</sub>
- 📰 2026-10-23 [Automakers Align on 2028 Autonomous Driving Commercialization](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNcVd3V1JhaGFMR3NySU14c3dTNkZrcWZpSktMNWxYOHhGc21DaFpydDIyaXYzZlJJSjlYTXVrSnctTnNuY1VnbHF2c3EySHMzNzNRYmJHZTRpVlFGb2xhSUplQXd1WVdiVFZacHVNQ3lBYUxTREk1c1VxRVd2ZEtDelY2UTBuSGdI?oc=5) <sub>조선일보</sub>
- 📰 2026-10-23 [Wayve, Stellantis and Nvidia team up with France on self-driving cars](https://news.google.com/rss/articles/CBMie0FVX3lxTFBKR2VWYV9kTV80VVRWR0I0RkhjaDNMUFJxRHJHdVRjbDNBTkNCVzRRLTYtamNmM1J4eVBhR29tR1JERUttVllTWXRDamRlbm1MTG40ZEJnUWlUQ2Q1cnhGcER1UzIxMnJ4NXFpd2FsWC0tV1ZCSVJsRGQ2VQ?oc=5) <sub>The Next Web</sub>
- 📰 2026-10-23 [Wayve, Stellantis, and NVIDIA Join French Government on AV Deployment](https://news.google.com/rss/articles/CBMikwFBVV95cUxNMFVrMXlJQUFxVmczUlhQVHpDejllUERJZ0lIWk5SdXQwajIxZ21kOWFnQ3Q0ckp3SGFBSEdEcnJuTUlHZkZmN2xqZUZSak5VTVRHbERnb3o4NDRiUHB6VWVkdW5WNjg3WlQ4aURSYzRSNkxkNmNxWkNaQnJ2VlA0TTJmOGFuVjBRVHR1SkJBWkFFd3M?oc=5) <sub>Unite.AI</sub>

</details>

<details><summary><b>Momenta</b> (105)</summary>

- 📰 2026-10-24 [家越07订单火爆 99.7%选装Momenta](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1mQWJmYUttaXl6cnYtY0R1b29Qd1JwZjk3UFhKQzNKYjZSNXJNTXZKdHcwWFd6WEZtUTBrYlE2d2RYLVdhREZiRFNkNVNsaGpJall4aHA1c2dQT00?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-24 [【视频】豆包上车+综合续航1480km+Momenta智驾！15万以内家用SUV这么卷？](https://news.google.com/rss/articles/CBMia0FVX3lxTE1hNk9JMU1vdlNSQ2o2OHVMR081YTl0ZFNaekt2cVo1TFlLVVRfUGdzWXFJZU5PdDFxb2I0RUl2dlFodWdyOS1KQ1VjT1hMMDJLcmYzc2t4ZjNGVGR0amQteGNVY0NDVU0wNHUw?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-24 [700TOPS算力配Momenta R7智驾 东风风神L8+上市12.99万起](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9DWUxpb0hwMmlzUVdla3l1d3BCM3pieWUyQ1VOVW9uVFp6dmJiTE1DWHl2NFh0cUh5UDlVV1BjTXYwTVFRQlF2dVZHd0hDUkllMjdKbVNGOG1UaTZDdnIw?oc=5) <sub>新车资讯</sub>
- 📰 2026-10-24 [13.99万起，配Momenta R7世界模型，但有几个人真的看懂了风神L8+](https://news.google.com/rss/articles/CBMiW0FVX3lxTFB4MFJHSV9WdDdWMHlTV001bXVXZm1kRXVuelFXcG94WmN0LThQNlhMZ1NhcnVzQk94d29nbTdPYlgtWlhSeVJDcDl6NE5SSzdUZmxyZXNBZDN5LXM?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-23 [Pony.ai partners with inDrive, Nvidia to launch robotaxis in Kazakhstan](https://news.google.com/rss/articles/CBMihwFBVV95cUxORmdqOVRYMWJDeVowMHU5VDFXYXJ3WS1sYTN1dC1wcFNlRkZYLWpsNENkZ1lzNnlWZmNRakhpMzcyWjZNaDlIVmxfcm1GeklNcEY0V2ZmYU1BMlJ0Y0RrSDZUNHQ4blRUeW1lYnVwOGlnNVhFeW1pN2NjVEh5eklEc1JlZFh4SEE?oc=5) <sub>Yahoo Finance Singapore</sub>

</details>

<details><summary><b>XPeng</b> (261)</summary>

- 📰 2026-10-24 [Interior of the new BYD Seal 07 reveals a grownup design - ArenaEV](https://news.google.com/rss/articles/CBMimgFBVV95cUxPbVBubGVwR0k1aHc5OUN2bzA5Mng1eFZWODUzUFpfWjJMTlhKR3ZLZ0IyZGJLQl9BZ0xTSUQwQlFra0I1Vmx5X3lnQ0oxZ29fX3g5dks4X250T3pjMHE5UjZja1FZOHJSdWhGejZxdVhBaHVENllSUmpuNzIzOEl3X2s1Q0pKQ05qeWpPa2VROC1yZUt0ZEdyc2dR0gGWAUFVX3lxTE90WHJKUEEyNXp2SURiSXk5b25hQlphV1FySzU2U0V0RmVPdjVpeVlmTkVmMHBpem84bG4xLXVJZ0NFc0ZoS09TRnY2OTNGcEZncFN3b2x6Q2tXQ0tCaWdyQWFrbjNOVmR3RE04Uk1rYllDeFhZbmF4NkVZbUNnbXF2UDQ4aWxpbUpJQlZVcjlMS3ItX1pQQQ?oc=5) <sub>ArenaEV</sub>
- 📰 2026-10-24 [智驾与座舱谁更聪明？小鹏G9L、智界R7、理想L6智能大五座SUV对比+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE1oMU9saGhsN2lLOFBPQm42bWN3UTRIUnFHUnVycTdHVUpPVDVpdTdrN2dVaTNaZjV5dzNwczBnNGgzQXozV19TQndIenNfVnVFNm55UHVvRXo1NTN3S3Q5R0hfNUZwd21KcjRJWGpNUVRvUQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-23 [小鹏MONA L05智驾实测一镜到底 NGP漫游体验#MONAL05首发评测# ​](https://news.google.com/rss/articles/CBMigAFBVV95cUxOdkNRUmhCRkdOczc2RVljUlZSOEN3Sk9KTHdEclZ3SGhqSy1rblpCM0dxRkFBaWo5ZWZIMTFwYlZJOElVUU9Jbk14di1TclFuYU1abkNVcU52N0h6djJzSWpVQnVzOHU5WW95LTBvZnk0bDYxMVNadFAtekNHSXNnZA?oc=5) <sub>新浪网</sub>
- 📰 2026-10-23 [长途不焦虑的大五座SUV盘点，小鹏G9L超级增程与4款热门车横评](https://news.google.com/rss/articles/CBMickFVX3lxTFBOMkp1Mjc1YjA3dzBZdlpoM3hURG5qS1ZnTkFZc3RnT09XdGJ1TzdVdjNEcHhyNG5pdVUwWHZhRGlIOGZRb096LWREYVYtaE9mSnh0YzRybThGekNEbHBhbUJGejJlem9CNzNfUmNuX3dpdw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-23 [周末带娃露营，小鹏MONA L03和铂智3X的后排空间差异有多大？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5Bcm40ckx3RExwM21XVmxzRF9uNGpXZHc1TS1KSFpTS20tQXpCOExEdzgzMHQ5VnpYWnJKS3pKMER4bGVyQ0JWeHI2SmZxMW1zT0dFUXNBTHV5Tlk?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Li Auto</b> (159)</summary>

- 📰 2026-10-24 [Roewe Prices Lidar-Equipped AI Driving at 120,000 Yuan in the Jiayue 07](https://news.google.com/rss/articles/CBMif0FVX3lxTE9FeC1SWWxnZUNoQUlJWndrU0RCbEV5LUlKMVJ1ckZKZURwUGp1dGtfREdJSEpWUENndVY3dHJCOHFzeC1nckJranF4NGxMSFMyTFF3RWVrbVJPZndIUUg5WTl2MG9MTENHVUs0UF9wd0dYU21NZ2NLMnBVVTJhaDQ?oc=5) <sub>Trending on Weibo</sub>
- 📰 2026-10-24 [综合1602km与9分钟快充：小鹏G9L与理想L6、问界M7长途SUV横评+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFBzTkMtd2VPalkxVTN1cDBoNjdUYVlJSTduZ3dJLUtlNWtCaGZGWDhEQ3NJMzJMdVVuaU1RLVNTbGxpQmw2TVlEbmNNQW00UHJwUmZNcVFOODFvRmdDdHJRQ2t5RHdwN0c5MDlMVFFrZlB1dw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-24 [9月豪华SUV市场神仙打架：理想i9、问界M8与FREELANDER神行者8深度横评，谁才是真正的全场景王者？](https://news.google.com/rss/articles/CBMickFVX3lxTFBkLVQzX3RxX1BJSXE3MloyamJuWUFnc2RJdWVxZ3VGYUgzb2c2SHVJMW93ZF9BTWIzZ3loX1ZlWVBKYUlqTWxLbXYxVWJEM1Yzc2JMRFpCR19LT2QwUXk2QTJSSHFUd1g1WjJlVjRZYWRlZw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-23 [试过理想L8与智己LS8才懂：30万级新能源SUV的终极答案，为什么是神行者8](https://news.google.com/rss/articles/CBMickFVX3lxTE9RTEpXXy1ob3o2dE93c0t1VUZZYUZmZlF1VzFDeVBGck1ieGRWUFdaNjcwQXlOaElZdEw4WnpUMkhlak5fc00yMm5mSHRMYnk2QjFoLUd0TXphV01GVlpCWGdNSEFYeHEtdHozcm8wRHN4Zw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-23 [Automakers bet on intensive in-house R&D to break through; Li Auto and Xiaomi Group both rose more than 4%.](https://news.google.com/rss/articles/CBMimAFBVV95cUxQcmNMN1A2Y2llcnRBMk4zWEVMQnREYmJ3ZzU5djdUZmF5LUlxVFI0T3dvWGFMcjZyTGRNaW5IM2dhLW45MHh3SVVtd2dTNkF6OE9zZjlQQ3lSYm9CV1BJbGJyM2x1MWF0VHczY2ljVWxaUWtEQVhaVGxkSmVnLWJEd1g0VHdRSE9pa3N0SDFLTHh4Rkt1RDVEbg?oc=5) <sub>Moomoo</sub>

</details>

<details><summary><b>NIO</b> (155)</summary>

- 📰 2026-10-24 [智驾怎么比 ，享界G9与蔚来ES9解析](https://news.google.com/rss/articles/CBMif0FVX3lxTE93c0lKRDRQU2RLdS1Eemk1d0x5QTZFcUI1c253b0hxdlZscTE5Q0JIUm5OX2d0dVhxc05wZUlPNmFqT0haajk4dElBMGJtOFFTYW13cjktMDdDNTNQT0JwZTF3Skh5SDliRWc4dGQ0anhjeVRuWldLRGMwdHFOVzg?oc=5) <sub>新浪网</sub>
- 📰 2026-10-23 [Nio ES8 Reaches 160,000 Deliveries 13 Months After Launch](https://news.google.com/rss/articles/CBMilAFBVV95cUxOTHNLRjVFZExmRjlkR3VNRWZ5NzQ2QnhjdnVhQ2VBMnJIMVRxUjQtWG5MYTZseGxqWlNObk9BRVhLaEtYU1ZZV25zeFN3eXBXOC14cW44RkVmM1Y4Nk1VOE1WZ0ZPa3N3RER6WnBLWHdfNHdfa0dYdTllaEpsbnVKSW9ObHpIbDNfWkJDTTNRd3llN2Zh?oc=5) <sub>Electric Vehicles</sub>
- 📰 2026-10-23 [Nio's Firefly Lands in Bangkok as Battery Upgrade and Self-Driving Economics Face Investor Scrutiny](https://news.google.com/rss/articles/CBMigAJBVV95cUxQWVlBLUl6ZjAwNUtKMTlTQVdCYnJRaDdOUGw0NTh6SWJ5UEZ6a1dlRTRlLTBjS19KRmQ4MFhtNGMtZ2dFVkdWU08yNl9TazNyVzlramJsOC1zdWVDR0tvWW11THV1VlBLY3lRWG9oMm1HanZ5c1pzYXdmRkxIbHF1Mkd6Z21td2ZGYS1uQVZENDBJUHdBd3FQQ3ZOQ2RaNFJIOEhMdmE1QTZnSUJFWWFsQVVmRHVOcGJ4OVEtX0M3UU1vNWhxRHlhVGJyZ3RSUjdNb0xvdkd4bzNfejF4OUI0dnJKdWNSRTRTS2hRa2VJLXhGRUJxdmZTbnhkeEpCeThQ?oc=5) <sub>AD HOC NEWS</sub>
- 📰 2026-10-23 [Nio’s Firefly Launches Bigger Battery in China, Lifting Range to 348 Miles](https://news.google.com/rss/articles/CBMitAFBVV95cUxPcjQtdlBmODRiZVlBZV9Tb3lEZ0M5T0Y1Y1RNVE9mdVZ2aUluM1pLQW9DckNXYWloT0h5alFjUlVUMlhubDA1QWJzTmxveUcwUnlTYjB4ZUl4YTNzNHA4ZlRkX25nM0dNdjJGaXRBb2Q4cWRGcDJoQWlMNUFlSTBQdFBJVFdsUWI4d1Z6bC1oYzRDRmtNdm5jQXFzQi0xNTUwR0xhZy1CdDd6Tld1WWNBUDJHOHg?oc=5) <sub>Electric Vehicles</sub>
- 📰 2026-10-23 [Rivian Acquires Startup Led by Former Tesla Autopilot Simulation Head](https://news.google.com/rss/articles/CBMiqgFBVV95cUxOVXdqM0dlVkV3SkNDam1tcUxoVkhjT1Jya2ZhV2ZIMEg2c3pNVkpBU0I4U0swdndCQUpfcVpRZ0h4YVo2c1cxT0tmRkJ0UVJpaTR2RU5UZEo0bzQ3QU14SjFLU2xpZUhNNkVON3Z3SUJCRmtvVDFkUFd0N2tzS2ZBbW11ZnNGUXRBZnFNYkRDY25zZzZMd3I2S2dsVmJ1bWIwQXNCaU0wellPdw?oc=5) <sub>Electric Vehicles</sub>

</details>

<details><summary><b>Huawei</b> (356)</summary>

- 📰 2026-10-24 [Huawei-Backed Aito M9 Bursts Into Flames After Fatal Crash, Raising Safety Concerns](https://news.google.com/rss/articles/CBMixAFBVV95cUxQdGFWU2g3bWh4VTEwQmFWZUxPNmgtUTN1T0hZR25DRldIWmtWbFBudnlzMjNCdEd2Z0EwdG5hWDFEdEZKeHhHdXpjLUMzdC16MDhjc1dIaHRqU2VkaHk2N1hBN0VfTVFCeUpHeENZdzBsMHlVM1FDVXF1QzJBc1JNZkdxNjhWY1gzUmFnbm92dE9iSDN1SUJicWZyNExWR2tkVmlBblNjUHpkanZhX1Z1b3NTU1VJMTdlNTI3S0w3dVZDSF9U?oc=5) <sub>Vision Times</sub>
- 📰 2026-10-24 [405 KZN homes get a head start on fibre, with a catch](https://news.google.com/rss/articles/CBMigwFBVV95cUxQUlNrel9sUjhKa0YtVkE2bGRnNnowV2tTaGRrRTI5QnpqVnN6NlY1T2VQa1VJOGtHNE11UlVmMW1KOUx6UF9PMUhCYXZLcVRGYU9tNU54U3M2eEJEb2JRRmEwVEZoSmp1ejFtd0R0eGhWVmk2UWNPbVkxaGhHd1VLaDFETQ?oc=5) <sub>Townpress Newspaper</sub>
- 📰 2026-10-24 [第二届华为乾崑智驾公开赛10月31日开赛](https://news.google.com/rss/articles/CBMigAFBVV95cUxPcUhoWkxLYlpqNE03ZkU1ZmFDNUdwR2Y2N2d1LU8xTUxNanRtSGloME5LdnJnN085NXpNU0c1SkFOUjFCSjhCR09xUkh0MldONklRZU5nV1JXZ1N2ZUlJelFvYkk5SlEyM0ZVNF9TRGI1X29aYUd1ckM2U1FrYXhzbA?oc=5) <sub>新浪网</sub>
- 📰 2026-10-24 [第二届华为乾崑智驾公开赛官宣10月31日正式开赛，26日开启报名](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPcHprbFNOMHBKU1hpRDlETHFpOGxTdnplNDVTV191bGxRMVNtNGJVQ055T3pxTVRGeklvYi1NLVV5R0JNU3V6WlBRdTNMbDR2bnlGSklESktUYk1lekZvdTZJYTFfQmt2Uk5EMGhoM0pGMmF5eWc3M3QwLUlqbldRSklqUlItTGg2?oc=5) <sub>搜狐网</sub>
- 📰 2026-10-24 [【视频】第一届超15万人参与！第二届华为乾崑智驾公开赛要来了](https://news.google.com/rss/articles/CBMia0FVX3lxTFBwMmNpNHpxRi1JVmRxMjROS19aMnRpRHdvbVlLbldlbFcwSVZOQ1ZOUmluVER3Yk1QMHN2QmliRzhGSmNlRzRzT0x5bHJ4dm5BdHEtZU0xVlg1bEZMbTNxSHVaODFlYVlpblpJ?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Baidu Apollo</b> (48)</summary>

- 📰 2026-10-23 [China's Baidu tests robotaxi on London streets](https://news.google.com/rss/articles/CBMimwFBVV95cUxOcUl6bGxJdkU1a3dZU1JRbmY1WWNfZ0RfV0V4LXhOTi1ZLUxpVFV1cjNFS1lHRTVsTkhmUTRpVHpKOHd4dXp1a25TazhJTXUwdFdWNWotNE9qRExzZmVmVnVnbnRmbGJJRV9SbU93UVhSdGxYUnpkX0pXYy11UVc3VGdrSW1XQjdqQTVVZHl0MFJGMVZtdlJzQVU5RQ?oc=5) <sub>Reuters</sub>
- 📰 2026-10-23 [China's Baidu showcases robotaxi test vehicle in London](https://news.google.com/rss/articles/CBMirAFBVV95cUxPUDVibU56QktsNWRhVU1rQ1pKSUJpNGZNZUc2T2RRd0Rqb040RjIzR2Y3NjlFTFktU2dIRnBGb2pDdUFNbTgyVkdxRnc1Q0pPenVnQUstSmZwUU1BUzYzbFlOTUYtVHVJY3FWd1NnaXBmU1NCdmdVVGZqWlBmcFU5VFlQSi1ROE5Gb0NKLWc1bFNYNWhvWjNSeDQzS0NSOTZWUHEwcWo4eFNUOFZT?oc=5) <sub>marketscreener.com</sub>
- 📰 2026-10-23 [L'azienda cinese Baidu testa i robotaxi per le strade di Londra](https://news.google.com/rss/articles/CBMieEFVX3lxTE9WbTJaT194WVQtajJsdk5OLXRMb1VOb1JCaDY0eG5VdVl1OEdIczdXTEFVOGxjXzdiZW5LSjhSR0JobzJBZUFXSm16NVB6V0RhUDZQcENUVXM2T29UcnZsbjFhS3JWWDVoSU1rNjB4dnBRWThJbEk3dw?oc=5) <sub>TradingView</sub>
- 📰 2026-10-23 [Baidu Robotaxis in London: Driverless Rides Target 2027](https://news.google.com/rss/articles/CBMilwFBVV95cUxPYkhxcm5kcWJLWkZjclVGOS11dUlvMXdaM2dGNGhkZ2JYVkVJX0xKQW5KY0ZteEFhM1lhZ1U4eGNxaWhBN3RiRkxjWTdyMVJpNFBxQ3F1TFk3U3l1WFNsMVVrLUFGYXI5dXk1VDJxQllvUWpzcmpuM09FMEV0d1V5V0p0Y1FOSE1Dc3l0Wm1rTUZvakxJWkFJ0gGkAUFVX3lxTE9xcm9URHQ0RWlvdVZQTkR3NHc1U2FDd0cwU1hTd0xCQWRJZEZEQ1czZEVZT2U5NFdVNHg1OFJCZVBWN0xvVGRhWjVTQTAtVVB3VDFpQjA5cmV5ODNVbDBqQVBlbTFDbzZ0R3d1aDBMY0xhcE9NdWNiRmp0c2gtMDBFb0wyNHEwR0xZaXMwN0o1cU85ZGs3QjN1ZzdpQW9RU3BJdmt5?oc=5) <sub>Analytics Insight</sub>
- 📰 2026-10-22 [Hankook Tire expands supply to Baidu's robotaxi service across 10 Chinese cities](https://news.google.com/rss/articles/CBMiV0FVX3lxTE1CVG5iTGtQRGJWY1Z6R3RFUjlGS3dhXzNmbWpDWHNtTjFUNnlMb1dEaXhtZkNVZlY2T3B0cnUzSGptQVJaUm9aM1FyQTVlY1MtR1RTX3hZbw?oc=5) <sub>헤럴드경제</sub>

</details>

<details><summary><b>Pony.ai</b> (147)</summary>

- 📰 2026-10-23 [InDrive targets 2027 robotaxi tests in Kazakhstan with Pony.ai and Nvidia](https://news.google.com/rss/articles/CBMimAFBVV95cUxPTVprNXIwWFdjRlE0QlpqcFhmUC1aX1AtRU45TTlXYW0yWWgyTHdjbFROVE5WN2pXWGh1U2FqWkdjNndtMnR6WUYwUzR4Qkt6MVZsVkZ1LTg3RG9VSkN4Y0VLREN0NHVQRVBDbjhzXzA5OFRCRFFVcUpoUHZkSlNWaHJfX0d6SDNCdkdaSVhhcmR0d3NJREVKeA?oc=5) <sub>Traders Union</sub>
- 📰 2026-10-23 [Pony.ai, Nvidia, inDrive partner to assess L4 autonomous ride-hailing launch in Kazakhstan](https://news.google.com/rss/articles/CBMi7wFBVV95cUxNX0F5bElEWGp4dHoybmJBWk40YUhteTdvaHlRTS1jLUhtOUFCekhQZk9fU1JYV2VuVkRhTGhoWjZCdjZ0eW91eF9vU0pybTUyN3ctWWtqVGJmQVBXM3E2OEJtQ3ozVXFLV2lSd2RFb0lJX1ZWeVBaem1idDFZdGJJZ0IxQ2RUT1A1a0FtM1ZTTEo3QUZvSE9WRlctRmJqZ1dZek95SmpFYUt5S1J0aXFLNV9XTy1TMUd0bGtfWDJQVUE0b1k1WXFUS2dpRVNxdV9CT2Z2ajVQY25uaUZYRlR2cEx1TnB0czllQ2IwN1M2aw?oc=5) <sub>TradingView</sub>
- 📰 2026-10-23 [Pony.ai partners with inDrive, Nvidia to launch robotaxis in Kazakhstan](https://news.google.com/rss/articles/CBMixAFBVV95cUxPd3RfYXZ3VmFIMHVsLWhBUEkxa3NYek5NS3VCQzBUdXlfd1dDeU85TGdBcnI4N1duVEltOGZzemsyUmNUb1N0LU9XeXVHQ05WcVg4dVNzVmVGZXpxa1d4WklnNm82MUtwQ1BGQnlJVzhjd2JQeDExUDRCNVhIUWVnT0NlZnh4OHJHWlBnNEk0Y1Blbm5sUndmSEM5eFVOZmloR1VrYW1EQjZrZFQtR2pGczlYZFpRcVhWT3BaY2t3NWtDS0k1?oc=5) <sub>Investing.com</sub>
- 📰 2026-10-23 [Uber rival inDrive eyes 2027 robotaxi tests in Central Asia with Pony.ai and Nvidia](https://news.google.com/rss/articles/CBMiugFBVV95cUxOaWhUal96SUMzM0RCbURnU0FPWnNfYzF2Qmtjc09PbjcwUmgzTmFyR1lyOHdtbUNFV0tuX3hMTzhIamtJTGk2cVBFeGI5dXJYOW04NERCU005LVp3NkdUMlVwSjVGYzJJcGZDTElfRVhfYjJYNnpPdmNVNjhlRUtHQ1hwbjZKc1NDNXc3cUdGbWtmNVJrRW1oR2d3SGtmemZfV0s0dmhVT2tqQWtQWHoySEN1SFpiYk5yUnc?oc=5) <sub>TechCrunch</sub>
- 📰 2026-10-23 [NVIDIA Details Kazakhstan GPU Deployments and Robotaxi Plans](https://news.google.com/rss/articles/CBMiigFBVV95cUxQNXNQT0lLRTVQdzM5OUx1RXQ0RU9ZTzc1SVo4aDVVdEFEcVl1WUVqakJmVTBNTFkxVGpIM3NDc1BhM2Jsc1YzZkIzU3gyMDZ5RnREbUFMV1VSUDRqMDQtS05fRUdMdjJMbl9NRnlyTEVjMXFBQjN3YXRHZ19kcnVqV1plM2hyWDNPU1E?oc=5) <sub>Unite.AI</sub>

</details>

<details><summary><b>WeRide</b> (148)</summary>

- 📰 2026-10-24 [【视频】官方套件变身，4小时让家用车秒变运动潮车](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBzRXJEeHBLZUVqSnFyZ2NWNHZ2QUpQNk5zOE9jZEFubGZuS01sTlBwRFJaajZ6REN3bm1CeGhDb2tuS0wzTXZJRVBkYVFyQ085dDl4OExETmg4MGs?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-24 [【视频】不用大刀阔斧，一套原厂运动套件，也能让埃安N60颜值升级](https://news.google.com/rss/articles/CBMiW0FVX3lxTE53SkhIN0EydUROUDlybTNzNUdlUld0ZWx1ZGhwY0I4T3hmZWVvR0ZFSmwyaEVEcFpIUV9yZTIzZXJka3BpYkU1eWZOb00xazdHRzFDU3gxZk5yX3M?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-24 [广汽埃安Ray7预售12.88万元起，首发华为DriveONE EMB全电线控制动](https://news.google.com/rss/articles/CBMiVEFVX3lxTE53MGZOWXFjdmh2dGc1eWoyeVNKTGk2aGFpWXBLa0pVMGJIbEg3Vm5PMVRyZXgxQUNIOWlnWUNzaGVnQU8wckpTbEZ0RGNVYm9Jal82SQ?oc=5) <sub>虎嗅</sub>
- 📰 2026-10-23 [From Physical AI to Scaled Deployment: WeRide Named Among WICV 2026's Top 10 Automotive AI Application Cases](https://news.google.com/rss/articles/CBMijgFBVV95cUxNRUk5M3Nib0xIZWwyMmFDOTN4ZmFwOTVCS1lvaGp6Wk50dmoxRTg1RTd2YnBuaTJ6UTdLZkp4VGI0b0NFTXdUbGtIOE5VWEJvRGdFLTBvVVN6bzVISHpYTVJXbGhnU3NDVjR0TER5ZlJxS1RBU1V3bzdjMnZjQzAxWnBjWEZiRWxNaEVIMGN3?oc=5) <sub>Yahoo Finance Singapore</sub>
- 📰 2026-10-23 [文远知行亮相2026世界智能网联汽车大会，物理AI飞轮入选“汽车人工智能应用十大案例”](https://news.google.com/rss/articles/CBMigAFBVV95cUxNaTBOeE9uaGgyczBRZVFITnF2Mk1BbkswcnhTczBEMGFjQmQ2NG13MjlLXzlleWJZQ2J0Mnp2Qm1MZEJVTEVSa28zN2JVV2RrelJETmxPSDNZUVJkbUdhMzJYVks5aFFncHQwR0o0RE5mdERLUFVuVmpGQlR2LXlwRg?oc=5) <sub>新浪财经</sub>

</details>

<details><summary><b>Horizon Robotics</b> (145)</summary>

- 📰 2026-10-24 [10万级城区NOA激战正酣，智驾供应商却盯上了另一张船票](https://news.google.com/rss/articles/CBMiU0FVX3lxTE94T0xKVFV5XzZlS1Q2RFUtWTFCWTZTTXdVOG8ydGlCa3ZEc1hDUERjbEh0Vy1oVFUxZENaTVc5WWVZbDZXb1NDZkpfc05kWElMMmlV?oc=5) <sub>电子工程专辑</sub>
- 📰 2026-10-23 [又一款“成都造”新能源车入局，捷达M6顶配将城市NOA带入10万元内](https://news.google.com/rss/articles/CBMiZkFVX3lxTE9YZUhBaWYzVGtldnZXVndHbzJadUI2dE41YW1oMzZuWVMyTlIxMkU4RTZVSHhkUjlCeFN5bWhQdFozUFRHMm9wbEVweWgwODF0YmdDNFJzZV9EM2NiR2JWN2luMnN2Zw?oc=5) <sub>每日经济新闻</sub>
- 📰 2026-10-23 [Jetta M6 Notches 10,000 Locked Orders in 19 Hours as FAW-Volkswagen Enters China's All-Electric Family Sedan Market From 79,800 Yuan](https://news.google.com/rss/articles/CBMidkFVX3lxTE9nZzhONTVKWVBzTTQ2TzV1dkU0Q1VrdUl5V1JJWUZBTjlfaDN2SVBkRkRMQjhDR2Z6bEVWYlFxdXJScXNHQkFYSzVVbHNEcjNZemN4YWFQYzE5TmJZenN2b3o1LWs0Ry0yVWxvM0hrVmNIVGNZQWc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-23 [Price reduction at market launch: Jetta M6 enters the Chinese market](https://news.google.com/rss/articles/CBMiqAFBVV95cUxQTHk4ZnRTV1FRN1JhTl9xMmc1ZExUaVRvZHJNSlFUOWdaZUhWWmw0M194eEtwdjZlVkVTaDdieE03czZZbDVOQzNIZzlMUUt5NEdaczJvaFMzOTctamFDSldEYUVpWUJ4Z2NDYUtUcjFUZE1vMThFczlDS3h3WVBBSGhsUW8wS2pFZ1AzWnV0aHZfNS1YSzFMZ0xmckZkVGNhNG0wTV9MelE?oc=5) <sub>electrive.com</sub>
- 📰 2026-10-23 [Jetta M6 starts at 79,800 CNY, but city NOA is reserved for the 99,800 trim](https://news.google.com/rss/articles/CBMiqwFBVV95cUxNSVpLZXNQUlcxT2wzNmotZHhjNFEyU0dQS0RzY3pUcjJLSnU3QnpwMGRRRXpyWVE4aHVzbU5WQ3phdXI5QjFVTUJtUXBubjJRWmVhUkttREI1b2pWVzlMTHJldlduQ2ZDYVpEZkx1SUZNSnFJSVRhYWJ0U2dxN0I0SXkwbFpSdUo4bWlIX29ZOUVyRnNWRTl0VEVJSFkzWGl0MG1XSUh5SHI5S2c?oc=5) <sub>GlobalChinaEV</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (36)</summary>

- 📰 2026-10-23 [超5200只个股下跌！A股跌破3600点](https://news.google.com/rss/articles/CBMickFVX3lxTFBFOElzMjBpNzhSb21lWDN2c1BwaHhZeHowVW1MQS1qQ3NNeTJ2S0N2aXBzV0dNSjdKQUNWcGtSODBMbV9Ha3NGdkh1LUh0WTNzeW85X1ZweGUtaG84XzFVR2pyT3hPdzJONVRSV1JveWVYUQ?oc=5) <sub>finance.sina.com.cn</sub>
- 📰 2026-10-23 [US: Waymo Launches Services to Harry Reid International Airport](https://news.google.com/rss/articles/CBMinAFBVV95cUxOV2M2dkZzWEw4TXdrbU1kMzlPelNRbk5FQU5YbTY1MUNoRUdITmY0a1dzSUZjWE9JdXotNkI5Mkg5RzZQMlZORlM0OUppSVNlc0llbVFMa1NJNHpzLWhEbkl5RC1wSnZsUFNoVDJyUlgxa19OTWVGRFBvMHBIbDlYZllzV3NQMjMwMklTSWp6NWZqaDVuZndFUnpjckg?oc=5) <sub>Future Transport-News</sub>
- 📰 2026-10-23 [元戎启行周光：Astra 引发行业焦虑，基座模型将驱动下一轮技术跃迁](https://news.google.com/rss/articles/CBMiXkFVX3lxTE9kM0hySVNYZ3JHNjdKaTVGTjdkY2ZWTFcyc0I2Wngwd0cyRkM4M1NSXzkxeFN5LVBTVzB2MHJKYThfdEVyUlAzYmRPRHVrRm9qMXo4SXFzVlNUdlpHU3c?oc=5) <sub>DoNews</sub>
- 📰 2026-10-23 [元戎启行CEO 「基座模型有望推动MPCI指标从百公里级向千公里级提升，并进一步探索万公里级能力」 在2026世界智能网联汽车大会上表示](https://news.google.com/rss/articles/CBMiiAFBVV95cUxQd1BIRU9KT0dDeG5VU2Z2TUhyVnlVWXUwZHM3TlNnTlc1YWFjcjl5N2xGSWlTN2lJdDd5VS15QVZxVENqaVgwSVdDb21kSWRxSGVLbUpIMnhXYWY3U0hJZHRwSDllSHJWOS1ldTVTRW5nQVN4Tm90dmo2V3NMeExtQ2Q1ODZvUVcy?oc=5) <sub>搜狐</sub>
- 📰 2026-10-23 [元戎启行CEO周光在2026世界智能网联汽车大会发言](https://news.google.com/rss/articles/CBMiW0FVX3lxTFB5ZjJfdjJNR3dla2MwVktBZTlkTkJaQWVnT3praURrdDNFTHR1MjZScGR3R0Zab211eVRYeVVhMFAxQ2dSM3pfU011a2EtRXRXSG5fWXltTVA1VXM?oc=5) <sub>网通社</sub>

</details>

<details><summary><b>Mobileye</b> (21)</summary>

- 📰 2026-10-23 [Mobileye Sinks 5% While BlackBerry Rises 3%: Is Wall Street Choosing Car Software Over Chips?](https://news.google.com/rss/articles/CBMizgFBVV95cUxQbm9SLTUwcmItY2g1d05SYU04Nld6NDB5ekhDcVB1a3pyYlZqVWRNN19VNEZYalhiX08xTUo5bnF6Nk41OHpNNWdBUFI0YkRIX3N3ZWxCMWVOUFB5Si1SQVJpa2JFSTBjMVhEWkFLNmFXMm9waC1Xc3QyVXREb1g4UEJFRFhWaVhwb0w3dGxpUGhTdG5pVk9FeW0zVmJQTmxCZjVPclEyS3J1Tm96T3lvSmN6MFl1eHo3aHV5cVc3NlF2TmVxZzE2c0tNOWE5dw?oc=5) <sub>24/7 Wall St.</sub>
- 📰 2026-10-22 [Mobileye Achieves First TÜV SÜD Inspection Certificate for ADAS Development](https://news.google.com/rss/articles/CBMiygFBVV95cUxOTHZRQjV1cnA1T01OSC0yZ1Z5TmtOVy0zRHhtNGcwTmw2NGhoeVJsR1BhbVpEbnFLeGtYMkxubGFpVUxIelFVZlNBcVlMUlFwT0NMdE5TM3JVTnhpcW9HekxZUVdOOXFYY3otb3ZTd1FRU0hISlIxb3g0eURSME11dlFxUUtTdFlGNlZkS0RIekZSeGQ1WW1rRjdNbVI3VUZ5RUs1RXpid3B1WV90MS1LQzc1aXBpZ0VzRXB3V2J0eGJ5dFUtQnhWNVlB?oc=5) <sub>Business Wire</sub>
- 📰 2026-10-22 [Mobileye secures first TÜV SÜD certificate for ADAS work](https://news.google.com/rss/articles/CBMimgFBVV95cUxQM2E4elBaalF6Um9lajNMQTEyUmpaYW0zbTVMV1BNR0hlUTlIMkpyUWNoaXlHM3JWblBwSUhiNGRJTTgxVDFYOWROWW43TW1qZlZQeDhXaFY4TmJ6VE9vRi11SGcwQjg4WHpPM2g0Q0YxUGFBdmhMcTFtbEFWaTZqdmh0dkloM2RYMS1GdVVlblpSX0hTbVdMRG1R?oc=5) <sub>Automotive World</sub>
- 📰 2026-10-21 [Intel Banks $150M Paper Gain As Joby And Mobileye Rally In Q2](https://news.google.com/rss/articles/CBMiywFBVV95cUxOZVNKbmU1VlRTYVdUcExFLTRvdXhPLWJ5MkJyUFVMT3RMMlFvWjI5ejFPVjBfVFlET0p3RG04enRyd09pMHdpLWFZME94OXFoNHdFdFBJbXNMekRhR3pfcGstVmRWMTBEcHViMDdBaWxSLVRPNHhNUlZLYkRlcE1xM1BoS1NIWmpQUk9zQy1oUm5Fd1BOUWkyQkpGQnF5YUltUDAwS0tEYnJ0c2hkNVg5ZWFGalpxTTU4V3JyU3ZVc3MtazFJeXdkVnhHNA?oc=5) <sub>Stocktwits</sub>
- 📰 2026-10-21 [Mobileye cut to Underperform at RBC Capital on ADAS displacement risk](https://news.google.com/rss/articles/CBMiuwFBVV95cUxQbGV2OURKazdBc0c3ZlkwTDg1aDBENU5uN0ozYXRaQTBzWnNyX2hEWjI5Tm9FSDkybXBsVHFnNjJHaW9OaGg0NUsxY3Qzd2dKRUx4eUhBSW5EU242VVEwV3lKU3k3ZkpGUFpYTzdVNnhXQjVzU29YTVdCYndDOElCQkNVd2l6RzdkQ1ZyMHhsc19TQVJVS29kSmtoaGFfZkhxWkZMWEczLTlvSk1Ga2pwUWdBLTgxd1BnUmE0?oc=5) <sub>TipRanks</sub>

</details>

<details><summary><b>Aurora</b> (51)</summary>

- 📰 2026-10-23 [Driverless Trucks Log 1,200 Miles, Observer Returns [2026]](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQcG1PcHdpRkFhcENGLUpkbTl2LTNWdGRKdFVfbmJBYV9TMFhHMDJzTlZDTDh3aFh6bnYzS1d3YlJmS01DRVc1NGpLNTBseVZqS05LSDBBX2tsNlhsN3Jid3dGNTRxeFAyNVVJQzBxYmkyaExDSXlfaXZWbE0tQi1ZYXdMOWVxUFFqT2dz?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-10-23 [Self-Driving Trucks on I-45: 240-Mile Route [2026]](https://news.google.com/rss/articles/CBMihwFBVV95cUxPaDFqOGxqUlRHZEFfNVJCMGdJUndhZm1EbldJaWJxamRFbkt0TE94blF3U2ZTMUJFbkxSZWtFNHBqUEhab2daeHZwSFVsVFZFeWNtV0M0elEySk1sMTdTbk9VNzI1dFk3OEgyLWg2dFBIenVwNGFkSzMzaklnYXhfa19TUjdsM2M?oc=5) <sub>shattered.io</sub>
- 📰 2026-10-22 [How does a driverless truck get refueled or stop at a weigh station?](https://news.google.com/rss/articles/CBMivAFBVV95cUxNU2tla05zSVRfNTd6cEM1Z0M1MjZxdHo0X1BaMkpBekpTSUpRamxacVJiVzBhSGtrSUZOSXV5RkZfdHBoUkFOR05hSkFrREk5dXFKN0hWQ18tZVNWRTJpS2xMY0JBcEdGWW81czJPeENibVFmTUJFUGtUNVRmdmc3eldQT0tSS20wX1prcXpDc1RTMEhlRDV0V2djd09YWVJobkV2VWlPQmktaUY3SWw4bDVaTVVUd3drOVRBVg?oc=5) <sub>Truck News</sub>
- 📰 2026-10-22 [This week’s biggest Winners & Losers](https://news.google.com/rss/articles/CBMipgFBVV95cUxNWVV5RzlSQ0llUVBvYkpFZmQ2SjRGVFZRUlpSLWFUbFI3LW56dk1wb2V1aFJqQ3NFd3hKaXpjSnQwbXlHSzFVUW42NXJVZjFNNmhBbmc5NlhtaUl1TFdKYmpNN1FhYVhYVWhEVjIwUnpWQVNWWUl2UjFQb2MyQnFnMzZWY2ZFa0VOS2dlb2xKUURKNk84X29qQkFOZ3NjOUNub2RtMF9R?oc=5) <sub>City & State Pennsylvania</sub>
- 📰 2026-10-22 [Trevor Mogg](https://news.google.com/rss/articles/CBMiT0FVX3lxTE1zUEphb2swbEtnZUQ3NllKTlptT0ZGMXdOU2ZXWTJKQzNJektUOWdZRXBTWk9hRVJCY2kwNEUtNlFKQXduMmVIRFc4OHJBcG8?oc=5) <sub>www.bgr.com</sub>

</details>

<details><summary><b>Zoox</b> (62)</summary>

- 📰 2026-10-23 [Automakers Align on 2028 Autonomous Driving Commercialization](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNcVd3V1JhaGFMR3NySU14c3dTNkZrcWZpSktMNWxYOHhGc21DaFpydDIyaXYzZlJJSjlYTXVrSnctTnNuY1VnbHF2c3EySHMzNzNRYmJHZTRpVlFGb2xhSUplQXd1WVdiVFZacHVNQ3lBYUxTREk1c1VxRVd2ZEtDelY2UTBuSGdI?oc=5) <sub>조선일보</sub>
- 📰 2026-10-23 [150 Amazon Robotaxis Could Soon Be Moving Into A Santa Monica Parking Garage](https://news.google.com/rss/articles/CBMirwFBVV95cUxOUEdVWHdvbnRvcGdsbUdsN0Jncmd2QzJRMF9kbVFWNDdnOURCaTA2MDdscGctWVREbzBxdzY2d0VQWUJPbUs1UzRRUzkzSEtqV1hucGNiM3BRS0J2M0I1NVNPeE5SU0JCZ2tVcGdSWDZjS3BXR2dVbjM0U1pGZDlQSm1oMEYtSXZILXZRcC1DSEF3SHhMZ0g2a3RYRUV0WlFkdm5xT0xwa2c0ck1RWXRB?oc=5) <sub>Patch</sub>
- 📰 2026-10-23 [NHTSA proposes cyan lights for autonomous vehicles — The Verge](https://news.google.com/rss/articles/CBMipAFBVV95cUxOMFMydURkSTRRVS1xRXBkNzRKX2Q0Z3ZaeU95dzBoVkFpZllIXzZtNnlZSkxKNHdYV0pNZ0Z5WEN0S3A4bjNuVXZmLVY2TXphLVZmd25ZMjAtUUlqakxCUk5Ja3NrRldVb3A3NHZnSWxfcnRQWFlTUHBJNzdqcHJpM0NGbU15bDhvWGZTaFpKbzl2ckY2QkViZkJka29YZkV6R2dObQ?oc=5) <sub>UA.NEWS</sub>
- 📰 2026-10-23 [Green-Blue Lights on the Road Could Soon Mean a Driverless Car](https://news.google.com/rss/articles/CBMiswFBVV95cUxPdFJ3d0duQ29HV0NPRkRYUGpOcUYwX1pTbl9UUVhIMFJIbjNzRDRrTzhOMG9vbkJDMHBnTERLcjlpQ0ZTQmJnR05XZkJfekNWVlNnTmw0WnFzcHZsQWQ4V1d6M1F5Z1FiZkNuWHJnZkc0RzFBemdJZzNUSnJCVThYdWFGcTk3a1djR0hGWnpVUmVuc2t4d3c4OUVldjFnNFU1bHV6amFndjlzTGota3Y5NWZGYw?oc=5) <sub>Bloomberg.com</sub>
- 📰 2026-10-23 [New Report Explores Waymo's Impact on LA Uber, Lyft Drivers](https://news.google.com/rss/articles/CBMiqAFBVV95cUxQSDJXRUQ1cVdMMlNWUEl6VkI2UkRvRk1GU09NUVlyd2lydWZQMGp1Sk5NRTJKMThNaTlaX2RsN0hJMlVwQ2tZOGdEcjJZdWRFU2dUbnZiWmxQTVAzekJWNWRZcEgteXBhUm8zZ2Qzb3AxS3VZN3RTNWpaa1ZUSS1tZmZEcXpIb2hhX0N5aHFIWUI3WFZ5R2g5M2Rzb29yaUhCeWpHUmp6Vy0?oc=5) <sub>KFI AM 640</sub>

</details>

<details><summary><b>Motional</b> (14)</summary>

- 📰 2026-10-22 [Zoox Las Vegas Airport Field Report｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBuM3U0cTFKZHF4ZjhlSVhzY1k4dlVoMDhWVy1PaWUtcUJKWF9jeEtEczdXbm0zbjhTUXBiVFBpdWplUm1NNHBTbndsdzM5TTZYM1ZJSjVJNXBQM09iRkJJ?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-21 [XPENG Next Generation Pilot (NGP) Field Report｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE4xUFBoMW5mRlRQenVJWmVBMHhyMU5HV3VGQXBzQVhYMXVPXzhKeEhRY2Q0d1pKZ2hTcm81X0pSMF8yUGRwYzE3QlVVRko4YUlNNUhncUNzbTZhSkVveTBF?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-21 [EU Regulators Open Probe Into Booking.com Over Fake Listings and Phishing Scams](https://news.google.com/rss/articles/CBMidkFVX3lxTE1Rd2lBWTFiT2s0UG55ZzNOS2NlQ1JOQkVPX3hwSEhRQ2tTa0ZpS19telVJUmRSclZnZXlBSEF3eURRcnNTUDFIaVZ3VG1rcUFXc1cwOVRiU2hIMnFDY0pGTVVVcTZ6U1Fhc2JVSU9xdkI0eTRiX1E?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-21 [Taiwan Blocks Grab's $600 Million Foodpanda Deal, Citing Uber Ties](https://news.google.com/rss/articles/CBMidkFVX3lxTE9sZHZrRlE3bFZXdlJoUEg5azRoMTJiUnVyLVNKWmNaYVgyeDdGZVJ1bEFTN196cEhuaTFJVFVhVW5fdG5aanN6d0s3MmJmVFQ5Nms3OTBCek1IS09nSkFfLUdTV0pDMkR0TlZTNlltWUQtM1k1V1E?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-20 [China's CATL posts 14.54% rise in Q3 net profit to 21.246 billion yuan](https://news.google.com/rss/articles/CBMidkFVX3lxTE1VaFpob2tDMTR0dDMtMmNOcks2V1M4V0pKWmltNTY3VmRZNE43UHZxaHRRQW9hOVVjWWFzVkxWdmlpaDRoWUVuN0xISzNUVnZsMVVYU05CMWx1ZDctS1EtdzhDbVVqS0laSGJDbkFtRExycnJRV1E?oc=5) <sub>BigGo Finance</sub>

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
