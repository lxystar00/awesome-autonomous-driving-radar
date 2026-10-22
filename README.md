# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-10-22 · 1,302 papers tracked · 43 curated.

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
| [Scene-Adaptive VLA: Efficient Autonomous Driving via Dynamic Layer Routing](https://arxiv.org/abs/2610.24590)<br><sub>Yujia Yang, Quan Yuan, Jiawei Fan et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 0](https://github.com/yang-luvu/Scene-Adaptive-VLA) | Vision-Language-Action (VLA) models offer a promising paradigm for autonomous driving |
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
| [Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends](https://arxiv.org/abs/2606.01164)<br><sub>Jiuming Liu, Chaojun Ni, Mengmeng Liu et al.</sub> | arXiv<br>2026-06<br>📑 7 | [⭐ 245](https://github.com/liujiuming123/Awesome-Interactive-World-Model) | With rapid development of large language models and diffusion-based content generation, world modeling has attracted increasing research attention, benefiting various downstream domains such as game engines, embodied AI,… |
| [Is Your Driving World Model an All-Around Player?](https://arxiv.org/abs/2605.10858)<br><sub>Lingdong Kong, Ao Liang, Tianyi Yan et al.</sub> | arXiv<br>2026-05<br>📑 6 | [⭐ 256](https://github.com/worldbench/WorldLens) | Today's driving world models can generate remarkably realistic dash-cam videos, yet no single model excels universally |

## End-to-End Driving & Planning

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](https://arxiv.org/abs/2609.26792)<br><sub>Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.</sub> | CoRL 2026<br>2026-09<br>📑 1 | [⭐ 13](https://github.com/VAIL-UCLA/DreamStream) | Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions |
| [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)<br><sub>Shen Zheng, Anurag Ghosh, Gaurav Parmar et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 32](https://github.com/ShenZheng2000/WarpI2I) | Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs) |
| [DriveMLP: When Training Strategy Outperforms Model Complexity in Autonomous Driving](https://arxiv.org/abs/2610.29676)<br><sub>Alessandro Canevaro, Julian Schmidt, Hang Yu et al.</sub> | CoRL<br>2026-10 | [⭐ 0](https://github.com/alessandro-canevaro/DriveMLP) | Learning motion planning policies that remain reliable under closed-loop execution is a central challenge in Autonomous Driving (AD) |
| [G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance](https://arxiv.org/abs/2606.26017)<br><sub>Hang Yu, Ye Jin, Alessandro Canevaro et al.</sub> | IROS 2026<br>2026-06<br>📑 5 | [⭐ 6](https://github.com/HangYuu/G2DP) | In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 17 | [⭐ 348](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
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
| [123D: Unifying Multi-Modal Autonomous Driving Data at Scale](https://arxiv.org/abs/2605.08084)<br><sub>Daniel Dauner, Valentin Charraut, Bastian Berle et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 404](https://github.com/kesai-labs/py123d) | The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics |

## Safety, Robustness & Evaluation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [CCFM: Collision-Constrained Flow Matching for Safety-Critical Scenario Generation](https://arxiv.org/abs/2607.04451)<br><sub>Ke Li, Kaidi Liang, Yuxin Ding et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 3](https://github.com/KELISBU/CCFM) | Evaluation of autonomous vehicle (AV) planners in safety-critical closed-loop simulation is essential for real-world deployment |
| [Lipschitz Optimization for Formal Verification of Homographies](https://arxiv.org/abs/2605.23203)<br><sub>Jean-Guillaume Durand, Panagiotis Kouvaros, Maxime Gariel et al.</sub> | CVPR 2026<br>2026-05 | [⭐ 2](https://github.com/jeangud/homography-verification) | The adoption of vision neural networks in regulated industries requires formal robustness guarantees, especially in safety-critical domains such as healthcare, autonomous vehicles, and aerospace |
| [CADET: A Modular Platform for Evaluating Distributed Cooperative Autonomy in Connected Autonomous Vehicles](https://arxiv.org/abs/2606.04072)<br><sub>Pragya Sharma, Brian Wang, Mani Srivastava</sub> | ICRA 2026<br>2026-06<br>📑 1 | [⭐ 0](https://github.com/nesl/cadet) | Deep learning models are increasingly central to autonomous vehicle (AV) pipelines, yet their integration has traditionally followed a monolithic design where perception, planning, and control execute on a single onboard… |

## 🏢 Industry Tracker

Latest 14 days of news, official blog posts and new open-source repos from tracked companies. Full daily feed in [`daily/`](daily/).

<details><summary><b>Waymo</b> (228)</summary>

- 📝 2026-10-16 [Hello Toronto! Waymo is En Route](https://waymo.com/blog/2026/10/waymo-in-toronto) <sub>official blog</sub>
- 📝 2026-10-08 [Sober Drivers Still Face Nearly 4x Nighttime Risk: Why Road Safety Demands a Safe System Approach](https://waymo.com/blog/2026/10/sober-driving-benchmarks) <sub>official blog</sub>
- 📰 2026-10-22 [Waymo launches autonomous ride service at Las Vegas airport](https://news.google.com/rss/articles/CBMiogFBVV95cUxOUGhJTWkyQlR1cEh3dEVnWmNJbUtXTkhiblZRNHo3ZVowc0JCQUhUZHZ0R3l3T2UzUHJsVlBubHhhV0NZOFhkaGd1Wk1yRUFRSkp3VWxoZ0RIblBlS3pFdTA2ZWJDLWJwRWNqbDl6ZnBob2J0cmszZThmWVQzcUREZVExWEtvTFJmczBVZDFHQ0h1SjBkVV94Y2xBb293VVRXZ1E?oc=5) <sub>FOX5 Vegas</sub>
- 📰 2026-10-22 [Tesla Robotaxi Dodges Waymo, Avride After 3.1M Miles [2026]](https://news.google.com/rss/articles/CBMif0FVX3lxTE51TkNXXy1MdXMwdDd6R3VNV3p5dmF2eTRCVF9mSG5kRnludmlNVnR1Nnc5S2Q3ejZGQkN2Z0JjaVYycDcyWUxBQTBsaWE4VVhpWk9rX1VjS0E1d1M0V29aODMzbTFxZTQ2V0dZaTdzcnNvSlJtUnFKYTI4bGtWeFk?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-10-22 [Tesla Robotaxi Video Dodges Waymo, Avride [2026]](https://news.google.com/rss/articles/CBMicEFVX3lxTE1pcVZYT1hNODVQa0NXTWVnMGp1R3l2czRFTkpYWnZndmFqQkgzTEh4VFRwTm9nbVpmQ29PcjhNa2RUeVdvVlQybEhibk56ejZlR3ZBSzJfTHc2cmJqV0RlRENYR2RTRFZYQnQ2WjVHWHk?oc=5) <sub>shattered.io</sub>

</details>

<details><summary><b>Tesla</b> (355)</summary>

- 📰 2026-10-22 [Tesla aims to sell Cybercab robotaxis by end of year despite federal probe](https://news.google.com/rss/articles/CBMizwFBVV95cUxQUzlnbTF6RWxvZ0Nnb2hjaW9IdnBKemRlb3JhR28xOHBEWEtWY0hHVWladXlOYUVfUnpQS2FVUXpnMUlBTHEyRlo1LWtQUEdfQWp1TXliazBoWVNfUTEtUXhwX1VuTlI2NWF4bDNON2ZuQldudllLdlVCcGRPYjdCeGZJWkp4QUsxQ3lwSEE5VzRUUHNpMTNNQThYMVl6TU8zdks1MTZzY05BWVZocExLNE1uNTRLS0Z2QWZFcUxLY0xVd2h4dHppNm5Ha0wyV3c?oc=5) <sub>Reuters</sub>
- 📰 2026-10-22 [Tesla FSD Attachment Rates: 6 Details That Matter](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPdU9rVGFBSjNoVzM4a0JYaUtYdjZWMjIxQ1pNYi1zTDB2dnE3UDZMbjJKdmN4eTEwOXJnVXVuOV93M05wVmFoenBnb2NLTnVsd0wydUwtZXVDMXZBbGRDa0FreWtmS0hETkhBc0kwZFlHWHhCS3ZHRS1jUUpBcGtXcHRBYVN5WFdvQ0Uw?oc=5) <sub>BASENOR</sub>
- 📰 2026-10-22 [Elon Musk says Tesla vehicle demand exceeding production ahead of Dallas Cybercab launch](https://news.google.com/rss/articles/CBMiwgFBVV95cUxQbC1fQUlpLTBJc1l6SXppY3ZZLXVpclhSMmpMTktnUjE2djA0UlVoRXlFT1ptMHhWQlFHSS13b3lzOWZmVThHbXhndmVzRGpyRWlob0lJRGpyOXFHOE5TeDF0d2VuOW5XcGNNeE43SDVaWlNXV1pMRlNEdVl3VzVpMTBCb0FadkdieGJsaFRJSGNxdUN3dDBLUHpSQkg5NXh6MVVyU1pxTXloM1VVZ2x5RGM2Yk1DRmZpN3lJQ19VYXdXZ9IBxwFBVV95cUxQcmtObEV1cWVsclhVNzItRW5WQmtrai1uXzRBTTJ1U2pPdmFmYVYxTHdwY0JuSTZVM2xOcG55RFU1RHN6eDBQckhneldEREtWemJqYTFOWW53OWpLNXFOd1IzWjhxSklTaGFCNHVRUkxHXzU0TXV0QkpTMkxQYUFtWTNieGR4emd6LTFQS3RaT3pCb2pFc1ZycVFHMFNLZW5Vd2xTSjR0WHdGakFRSGQwMDdwYVhtUi1MSjQ2WHZtTzJyckdjX2VZ?oc=5) <sub>Fox Business</sub>
- 📰 2026-10-22 [Tesla says it will start selling Cybercabs by end of year](https://news.google.com/rss/articles/CBMilwFBVV95cUxNbjcxZVFDS3doM0tEZlVOZ2ZvNC1DbTEtdXhtcnRMdXFMUDU2ZFR5X1hKaUpMVG9UbUdSTHdiTkkzb1dFYWN2eG5DYlIxSFdmQ01sOVN6Zi1iOTl5TGNuLWxDeGg3Wk5XeFdtaTFHajYtUnJfVDFVdWtkM0RmX2hfM29ES0ZfNWFNN3BfY3FTcG5pNVl4SGNJ?oc=5) <sub>TechCrunch</sub>
- 📰 2026-10-22 [Tesla Delays Unsupervised FSD to Q2 2027, Robotaxi-Only](https://news.google.com/rss/articles/CBMiggFBVV95cUxQbDI3WUtQRU9wLUpiZWFieW5nSzdaSnFmY3FsSE11ekRZVDM5MUdMRE5Oa01nZ0VCYjMtUTZoYkpjNkR5aVVEUWFWMUpPMV9IRDNJYnh4UFpuR0lRUkRvb2JtZDR2d05sRUt1UkljMnVyQlgyRFl3R1p4TEtvYnNXLUhn?oc=5) <sub>https://tech-insider.org/</sub>

</details>

<details><summary><b>NVIDIA</b> (243)</summary>

- 💻 2026-10-20 [NVIDIA/flare-local-inference](https://github.com/NVIDIA/flare-local-inference) <sub>GitHub</sub>
- 📰 2026-10-22 [NVIDIA Cosmos Opens New Tools to Train, Evaluate and Deploy World Models](https://news.google.com/rss/articles/CBMigwFBVV95cUxOMWg0TFo2MFdIOWsyZnVmOTM0RVZfZXdETG14QXpVNnNlLXQzOFBtV2FzMUtSSWZidlgtVzRBdnlwbXRmMC1KcE11RFd2TEUyRTA1RUVkczAwcmJBNUV1dVhRS0I2TldvN2Zib1ZNTFJDU2VuNmtlUlQyc1hLeXpNNnhyRQ?oc=5) <sub>NVIDIA Blog</sub>
- 📰 2026-10-22 [TIER IV and Technical University of Munich Bring NVIDIA Hyperion to Level 4 Autonomous Driving in Germany](https://news.google.com/rss/articles/CBMioAFBVV95cUxPaVpqenh6Z3VmU3dEMGxOTlFibU43a1BhNFl3eUhkdzNfS294OXBwQTVnUTJTT3AwaVhFdndxQkpUSkpKS3hJU185Z2ZRck1yTkRqSmFQTkpqczlMSGY0T21CYnctVjMzTFExM0YxNnZpcjhsZVlfYmdGWGRZdnNZNmZUNmFmSFo1MDZiSlV6QkttWTMwTnFqU3FTSktVazFj?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-10-22 [Mercedes-Benz and NVIDIA Deepen Strategic Partnership, Jointly Develop Next-Generation Driver-Assistance System](https://news.google.com/rss/articles/CBMikAJBVV95cUxOaWhIdEplcGRPQk9RcTlyY0o0LUlrYXpnanNGZTFqVGJTNlRLM2dxRk1EMmk3SG02VmllN2x5dm8tSFRCcUMyaDktNHhjNDZpX3JXeDFCQ2xsMUlxTWZ4OElmUlNNU0QtV283SDloVFI3aEZQSVoyZ0h2ck1qVzk5V1kzSVBJWTBIZ3JBWVIwWW9WR0ZCUF9MQzZZakFpM21wR2FDTTdfOEdhU09aQV9NbnZKd2dlUUl5QnNYa1M2UTdQX0xNZ3JtbVJsZjk0ZHRBa3NGQ3prbUViS2dVUmVUdmRVVXh5LWlFQUQxVkxxM1NsVE03cFNDcWpRWTlQUHhDWm9NM1ppZ3hzQnJhS2JKZA?oc=5) <sub>Gasgoo</sub>
- 📰 2026-10-22 [NVIDIA GTC Berlin 2026 – Containers, Safety and Sovereignty](https://news.google.com/rss/articles/CBMib0FVX3lxTFBaYkJJM2owQ2pVWDdxeDM2TVVUeWFSTVJxWXpPaGE5U3RGVFd3XzhZR2s1a2tMcWVMcEUwM3UyUmVUWHhfMzNmWkY2QndBRjVwSFVxZGFvYXliSlhXUlB5endxQ1pJQUlFNndvYUVSTQ?oc=5) <sub>Counterpoint Research</sub>

</details>

<details><summary><b>Wayve</b> (69)</summary>

- 📰 2026-10-21 [AppyWay wins V2X Award at Self-Driving Industry Awards 2026](https://news.google.com/rss/articles/CBMitgFBVV95cUxPeEk1eWlfT2Nibm5VYktUZllHNlR2aFdJdXFGS25vYVctNnpQbDhFbElqX0phM21DRHBOSVlDZUxtMHo5b1dvSzVwSzBCUGh6a3VmUnRLOWRhcmNVS0RscjNMb2N6dVdGSVFJQk5RZEdCemlJbXVMbDB6MGpEZHM2d2xBY0ZZcmc1UlFYRjEzUTVVdmZsczdiSElLV05nU1Y4U2ZlMFUzSHNRY1pwX3RSd3k5TFkzdw?oc=5) <sub>Traffic Technology Today</sub>
- 📰 2026-10-21 [ENTER-UBER-AND-AI-FIRM-WAYVE-1-DPT.jpg](https://news.google.com/rss/articles/CBMifkFVX3lxTE5GS25RVGppYWtfNFNLVVVKaVNqbjljQUx1dFdHOFZGVXZGYzhuUzJwM2NvTkJvUG91R1poTmxpRUpQaTBWQ2p0YXZmbFgzaWJFRUhSeXZ1QWNFV21QOHRjakQ2STVfQUU2dnVYYlJqakZ3TVVNZzk4M3M2WWkyQQ?oc=5) <sub>Herald-Review.com</sub>
- 📰 2026-10-21 [AppyWay wins V2X category at the Self-Driving Industry Awards 2026](https://news.google.com/rss/articles/CBMimAFBVV95cUxNdUduUl9yNndid2xLNlJWclVueV8zUzFJSTRKejlSdExRb3czZ2ZmWTFwSC1lU3ZDa2hmVGJpWU0tQS00OVljY2RCUUhkc2RZOUVaQ1NhZ3I2YnI3d2J0ZW9mVjNKZ2s1NC1MTGpzZkpPZnNqbEhidF9kZXFvNHF6ZmwyRVl1YW9mbFJyYjF0YzEzU0NiSEpYRA?oc=5) <sub>Highways News</sub>
- 📰 2026-10-21 [New way of optimising self-driving taxi operations developed](https://news.google.com/rss/articles/CBMimAFBVV95cUxPdXgwUlNoalZ1d2FXMURJcFl6Y1BJdEVpSUpEazA2MmEzVHFSZXlsNmNOajVVd3JPd0YyTkRFdHF6YUl6UDNPaTFQZmk1ZHVhWGVwZjJOOXcyTU1EeGhISXFwdzU1YWJnMEFmYl9RMUN6ZFo2TEltN3AwbG8yeEFPZUlCOHNXLUw4bTEyTm93LUF4Q0xjUVRxYg?oc=5) <sub>Fleet News</sub>
- 📰 2026-10-21 [Nvidia Buys into Europe’s AI, Accounts for 10-15% of Startup Investments in 2026](https://news.google.com/rss/articles/CBMiwwFBVV95cUxQMzZNbE5FeGMzUUV0Y2FVOHU4M3dpVndkOWktVlpaUXJtX2ZGNHVBNXZ0Y3dOU0xzOVkzX3UwRHd5b2ZqZl9ySkxmUmhHdmwxbUd1RUtPNWRWNjlicGM5RUZfbkhvcTBtNF93anB6c3U0dmVUVGxoU01fRkRadVI5UC1yelBXcTJRSWpBbmd3aUpiVkdpSDR4Y0ZrOF9abXBOeHRMaTdZcFIwVTB6NEEzQlk4QnFjc3RlejVCZkY0ZWJTems?oc=5) <sub>www.trendingtopics.eu</sub>

</details>

<details><summary><b>Momenta</b> (93)</summary>

- 📰 2026-10-22 [Momenta联合JAECOO完成巴黎凯旋门环岛无接管智驾测试](https://news.google.com/rss/articles/CBMiZkFVX3lxTFBNcGU1YzJqb05SUkdqeWFqeHB6SjN1c29tOUNYaE5JQUZUd2tOdlNkOXUxNy1rbGZTdVZNTkROcFBmQlZZQWlJTVZoaUFJMXEwS2JfSEFzeUkxM1NKcHdhV2lya2JJQQ?oc=5) <sub>东方财富</sub>
- 📰 2026-10-21 [Momenta曹旭东：世界模型加速“智驾摩尔定律”，2028年迎来L4规模化落地拐点](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1ZTEpzYjZWMGlUckQ0TWJnM0tEXzFmQWJuc0hCSVV2Z01RRUJiUkNSYzRzeFMyRDhzdS1qaDN1RVFxNUliY2lsVDF4d3JTcGVhQTJrNXl3RU8wMU0?oc=5) <sub>网通社</sub>
- 📰 2026-10-21 [【图】2028年或为L4规模化落地重要拐点 Momenta累计量产交付超130万台](https://news.google.com/rss/articles/CBMiYkFVX3lxTE9nZnlIaFhNTzZrcXItaWxIOENDUkMwUGdTc3Bia3ZGano3dzAzbnY5b3oyRnY0cWMycHcwY1ZpQmw5UkJGYnVpOG9rdElTZXNHa2gzQ3p4NTlyZWRHSWFGaUh3?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-21 [体验搭载Momenta R7的宝马iX3 人机共驾踩刹车不退出](https://news.google.com/rss/articles/CBMic0FVX3lxTE1MZnBPNmkwc1Q1Vy1xcUZhZFNzZVRqSzlQLU4wVFhGMlJTM1VrT0FzclNmRnV3SjgwSC1tMHVCdjktNGw4c05wdVVZWmZyckpEWkFHV3luSmJpN0NXN2JRU2R1SUxDckY5V2p1Z1IzY25EWnM?oc=5) <sub>新浪网</sub>
- 📰 2026-10-21 [铂智3X配置参数值得买吗？3个维度拆解10万级纯电SUV+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE83RDJaU0pCWFozSjdGVHp6MWRYeXR1RzgwdTlOZHRyUm1PUzN2UlhvaGxsdWtfSkxSWm1BOUFDSkF1bUJzdkJ3VHd6ODd6YmtDSjF5b1FNeUFsMFR6bTNGaURURlNrVUFSMjNiOXJSU2l2QQ?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>XPeng</b> (291)</summary>

- 📰 2026-10-22 [Autonomous Driving on the Horizon: Divergent Paths of BYD, Huawei, and XPeng](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1rSVc4NGFJdGtBOUpsdnhfRjVWU2hTekFiQVZvdFJ1SUtaWGIzWjNhOWtxdHNlNzQ0dlVsQ1lPaFkySlJoMno1Y09UV0JqbHJ5WGZV?oc=5) <sub>36Kr</sub>
- 📰 2026-10-22 [XPeng "Flies" into Europe: New Energy Vehicle Brand Expands Global Footprint](https://news.google.com/rss/articles/CBMiU0FVX3lxTFB0cmhtd01HUHV2WktQQUJoTEtpU2xfWWVoMlo5LVdwUGVQMjFleDMzVF9kMERvNkx5QVNWM1RMRzBDa2NmcDBkRnhLc3BYVzI4bHYw?oc=5) <sub>36Kr</sub>
- 📰 2026-10-22 [25万预算新能源SUV横评，小鹏G9L与4款热门车配置密度对比+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFB1b1RoVGktT3M2Tk5iNl83anV1MXpwMFV5VHhkQl9CNFdub01GWXduWWtCMjNZeFJKendfMy0zeVFweEZQZnYxVFJrc0NyNmlmUXZ5enFCQVQ5N3VIVklQdl9Fb1V6RUxjRTRFM2JuaEpuUQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-22 [小鹏Mona L03 VLA 2.0智驾 嘉宾蒙眼全程睡着](https://news.google.com/rss/articles/CBMigAFBVV95cUxQX3VnMHQzWGwzdl96UzZ2Q01VS000N2JnSHpTcTUyb3I3My0yVVpKX0Fvam9ybmVvd2hIMmZUYjMxemk5SDJhcFdNb1k2UU5ULWt2NTZ4V19kbzJ4aVN0S3U3elRvNHBTWU9wY05BMmNWYm84THpqb0htUW5fT2lyZg?oc=5) <sub>新浪网</sub>
- 📰 2026-10-21 [30万级纯电轿车，智驾好用的买哪款？](https://news.google.com/rss/articles/CBMiW0FVX3lxTFB5ZEdjX3dKSWVYcUc0VEFRdzNhV2tJMXQxZFh1MzRtaDVMUWtUYWNpOUwxWS0zazhVMkRvV1dxaWxocVFjblJtSUJfSVUyd1BkVUpNT3hOZC1sZjQ?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Li Auto</b> (157)</summary>

- 📰 2026-10-22 [长途自驾新能源SUV怎么选？开理想L9、问界M8和神行者8各跑3000公里后，聊聊真实差距](https://news.google.com/rss/articles/CBMickFVX3lxTE1WOHdNWlJfYVRlQ0Y4bzg0N3I5aW5GR2Fybkt6MHE0Zk4ya1lGQ0U3LTU1NlVWaEZpSmJmUlVQQTh3MHBfOWMzc1JYVEpZQUtRREVza3ZaZGNXNjhwUkY2SlBSdzQ2WXdJbHNfRld2Z2lRZw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-21 [The Little Blue Light Steps Out of the "Confinement Room"](https://news.google.com/rss/articles/CBMiU0FVX3lxTE14OF8wQ0xkMmlwT3NTMmhqUUgtcUItUTdZRE01V1hoTHVzRFZRR0VnUmNWZ0o4RG9pNGNySVJHZzh2RXVkdGtzRncyMzR1Sl9IQ0pz?oc=5) <sub>36Kr</sub>
- 📰 2026-10-21 [Inside the Li Auto Lianshan Battery Production Line](https://news.google.com/rss/articles/CBMipwFBVV95cUxNYWV4OXJndU94bkhTdXJoWUkyYTdiX210VWt4bnZWckFpUE4xWEI5OXZtaDNRZlQ5WXFZWGFyNUpiTXhmS19YM3FGWDZCOV90OUF3ZUlpTHRUdmh1SVdjWjk0R09QTGlfc0ZoVXNqMTFoVjNaS1F1bWRSS19YWmJxaEdnOW1zUnlCcm9oU3pfWC1iZFBYVXFBYV9SRFNyQnpodExCVG00bw?oc=5) <sub>eletric-vehicles.com</sub>
- 📰 2026-10-21 [XPeng's Delivery Edge Over Nio Isn't Moving the Needle — Can the G9L Change That?](https://news.google.com/rss/articles/CBMi5AFBVV95cUxObmo5b3JSYWUyMExaZzR1TVp4WkxrcWwwNlN5T3ZLdjZFZ01zNzNhSERZcjloaG5iS2l0bU5LYzNJY2NfU3hYbi1wSy1pSjVKZU4wUEE2TFdXay10N0gxMnZYbkY1TkdKS1ZhbXI5OUhWZzUzQk9yYXBhOWVCV0gxaGt6Zkdyaklndkg4V1ZSWndWS09oODg2Z0hodk96SzFOeXBMcWtOZkVqQ0lNcmFUeDZqeDZkaE5zOGtpY1Iwc3FVYXZlU09HRkE2UFJkWlhUMDFTNmFrVHB4bWY3eTFEUVJGc1c?oc=5) <sub>AD HOC NEWS</sub>
- 📰 2026-10-21 [XPeng Mona L05 — 500 km of Assisted Driving with Zero Takeovers](https://news.google.com/rss/articles/CBMiswFBVV95cUxPUUJLUkR3SUZJbV9HX3VCY1RfQWR2TTk2TTI4ekRQTTU4U2Z1ZDJsZWxHeHRLU3I5Z3RKMmRRSTk5U04tc29kQnNJd1JIVnl6WTRoNzVwajYtYVdBLXRqdFJhcE1KTEk5djI3ZHlMNFZhUkFnZW1SbG0xZllRV3JWZ1JreVo3SmN1dVpLclpsekU5UElIZ19aS0VTTHpPMkFxakVrUS02eS1KbXZCOG9fakxYTQ?oc=5) <sub>Electric Vehicles</sub>

</details>

<details><summary><b>NIO</b> (165)</summary>

- 📰 2026-10-22 [$NIO Inc (NIO.US)$](https://news.google.com/rss/articles/CBMiqwFBVV95cUxONFhhcDRVa2thWHhqbm43OXczT3hKUjVDU29wb2hjWE00LW9vWEJTbGVnRkdHaHE3aDNzUHZSVDFJbmhTekFqX0VUYVRWUDYxWnREbEFia3ZrN092NWdzMEZVNFlxMTJkX1FWT3ZORlVsbF9ZdmYxd3FGdWI1Yld2NnNyeWNsUUtxc3lCN2x1S1V3Z3lUekx5a2FFZ0NGOFpmbGtSYW00S1BMWnM?oc=5) <sub>Moomoo</sub>
- 📰 2026-10-22 [李斌谈自动驾驶下半场 蔚来智驾避免907万次潜在事故](https://news.google.com/rss/articles/CBMigAFBVV95cUxPang2SDFJTVN4RVdXM2puVDQ5SUFjQThURUJjb0FFRXBtUDI4TE1KTGRZSzQzYnFLQVVYVkRlbm01dUFsNU04MlM0QTBORUZka2tkT2xmckFhVDBpQk5HM2RvelR1MFQwVUIydmVzaGVQaExNSndyN3M3d09JblVmSw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-22 [李斌称智驾核心是减少事故，蔚来91.4亿公里避免907万次事故](https://news.google.com/rss/articles/CBMic0FVX3lxTE8tdU03UU9BWUhJYjlBV0VDSkM2ZHNqdkNTMk05MmpOVzE4dF9UWjRLU1VzTEUwbnJTeDR5X3Y3VHhPMEYzeXBneWIyUlI4a1U4MG51OWNyVTl2dEpwYVdUUjZOMDYxSjVrWHJqeC1kMVJxNFk?oc=5) <sub>新浪网</sub>
- 📰 2026-10-21 [【视频】标配激光雷达却月销仅300台？蔚来EC6为何卖不动](https://news.google.com/rss/articles/CBMia0FVX3lxTE53UFVpSzNiQnk2T3Y0aTBrOEJ4bVlSRnpOa3I4eWJTamdlaFpkV3MzaFdNNzkwNXdkSnd4QW9SWGJCNTBORWFJamFrazA4MDhLZ0RnNjB4NUJoSWVZZDhseXdTWERoSUV1WHJF?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-21 [【视频】家用纯电运动SUV，探店蔚来EC6 租电26.18万起，精致小家庭首选](https://news.google.com/rss/articles/CBMia0FVX3lxTE9SZ0IwRjZ1UVBwWlZnVHRvMVlZZzBEV3pLUW1ORmJsLVlFNHBFbUxYakVpSzY3V1Joc240R09FcHhkV0lMdkJVZ0NUc3FiZUtidFNMeEljX3g5ODdpNFJGVlowaEgzb1pIMnBv?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Huawei</b> (353)</summary>

- 📰 2026-10-22 [Autonomous Driving on the Horizon: Divergent Paths of BYD, Huawei, and XPeng](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1rSVc4NGFJdGtBOUpsdnhfRjVWU2hTekFiQVZvdFJ1SUtaWGIzWjNhOWtxdHNlNzQ0dlVsQ1lPaFkySlJoMno1Y09UV0JqbHJ5WGZV?oc=5) <sub>36Kr</sub>
- 📰 2026-10-22 [CATL expands battery-swapping footprint with Huawei](https://news.google.com/rss/articles/CBMikgFBVV95cUxNeUp3em5QaHRaYVIzWUoyYnFWTXlNX0p4U1BZT3R6MVBoTW80NHVrVTFOc3lIdVdCN2syYzAtS1hRaGl3R3c1ZHJudXNvdll0enF6QldHTHBYZVpSVlk2ZW1McXE2NzlDS0t6Q2dlQ01EMGRzcEFJOHFVb043SnNxVkVuZVFhOGlSNThVSGVjWVFidw?oc=5) <sub>CarNewsChina.com</sub>
- 📰 2026-10-22 [Huawei Sets 10 Gbps Microwave Backhaul Target to Support Mobile AI](https://news.google.com/rss/articles/CBMilAFBVV95cUxPXzc4YV9kdjBzREpFY3h1Qm43MnN3ZjVqYVlONlFVRU1hM3FzQTVLc055MHl3cVpnblNhT2xRMHpfQndJX2M1aEV0VEYtc1dtc2pRMEpFQkpzTlBsMEd1T1ZmVXRxWFdsMFlRZXFfSG1EWmY2aGJDQ3RxMkdDaXhRbnpOM054WE5lelVja1FRbkFINjhx?oc=5) <sub>Retail News Asia</sub>
- 📰 2026-10-22 [Is NIO No Longer Alone? Huawei & CATL Launch Battery Swapping Services – Diversified Energy Replenishment Is the Trend](https://news.google.com/rss/articles/CBMiU0FVX3lxTE9yN1hYVXUyYkdmYkE4b01yUl9YY0JtVjVJZEJYNF9CWHc1WV9aYS1yYlpTWEhrWUNLajFLOFNPNjV1NFVtcURnWENxdEFQTjRCc0ZJ?oc=5) <sub>36Kr</sub>
- 📰 2026-10-22 [Huawei Watch 6 Series pre-orders open on Oct 24 in Singapore](https://news.google.com/rss/articles/CBMirwFBVV95cUxPeHpYdW5oQ21INHpObkxOMm00R3J6R3Z1TnMxYlBLZE5PM1RuUExDc01mRDA4OWthX2o3ZUFpMjA0RlJhbFRtc2dxaGdRVVRBS1dCbXhFdlJCLWo3NDVYaWtKcS0zV2dqLUFJTVdiMDFiTzFQVU9xRlh3YWVobU9HZDVSWFI4X0JzalZhaG1sZ2R3SWZ4YXZLT3lUWDZELUpoNWlSM3p2UHpCWkNpcjhj?oc=5) <sub>Can Buy or Not</sub>

</details>

<details><summary><b>Baidu Apollo</b> (47)</summary>

- 📰 2026-10-22 [Hankook Tire Expands Baidu Robotaxi Tire Supply from 4 Cities to 10](https://news.google.com/rss/articles/CBMidkFVX3lxTE5WY2pvTkFhWjFJby1lTDRBd2tLeHV4c2RJR0FqeExIRUlYajNRbV9SVzlNZkNrVkgxVlhYdHhDZlQzaE1JREhuYjJKdXctdVRfVWxVbW9lSURnejgxdm9Mb1A3emRVdk9nNHJJZWVKbnliNjU4OVE?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-22 [Hankook Tire Expands iON Supply to Baidu Robotaxi Fleet in China](https://news.google.com/rss/articles/CBMiogFBVV95cUxQVklEUTl5UnNLZGMwaEVFT0wyWXRrYjhPMUgxLWlmNU41cGk2TnRtSUtsQS1SM0JaUVJ1Tk9YYXFsTE1MUmpLbllfOG85U2lRRndZM21WRmhPeWc4TjJFX3Fad1BfNW9RNUQ5dlNhRmg2NTJKT2F3RzZfSFFYaDA3YUVJR3VVM0RBNmM5V1I5VDJMWndSdjFCS01QTmVnQ2xGRXc?oc=5) <sub>Seoul Economic Daily</sub>
- 📰 2026-10-22 [Hankook Tire expands Baidu robotaxi tire supply across 10 Chinese cities - CHOSUNBIZ](https://news.google.com/rss/articles/CBMiggFBVV95cUxPcWE0VmY0bURKT2NMQndsVnJFZVBpVFBnLUxSMVZ5a2pOR1pVblQwNGlibzlDMU9LQzZzZ3o2ZVcxZHhyLVd0b3RTalhNd0hlRnFzdTBEYXFCcFY1MFk1bEZwVkhucEJxcEcyX3pTdEZ4TmZ0TGpyN1V6UG9BY0hWaGtn0gGWAUFVX3lxTE1tMXNtTW1mUkhMS2N0OG5PbHZvM2lNd3VTOXlTdFpvbHRCbkxFYXZtVm5lMWJxNS16UmRncXd4bUNac1dZaldGbkZUNUtPaVlXRGI2cWNJUlgtMlc2eDdfVmVoN09QVGozTGU3eERJOGd6TzB0aHJ1Y09OZmlGWDJtNm9HamYyU083dEZhb3V6QkZxdXVqZw?oc=5) <sub>Chosunbiz</sub>
- 📰 2026-10-22 [Hankook Tire expands iON supply to Baidu robotaxis in China from 4 to 10 cities](https://news.google.com/rss/articles/CBMiU0FVX3lxTE5fbUZlTzE2cThST2g3RGQ0TzE4RlFTMlRyWFlFTkV2YkRLMHZjUkMtRGV6RWF2NlU5Y1ROeE4wZ1NIbUJqY3kwNllJUzRnRnJUMmw0?oc=5) <sub>매일경제</sub>
- 📰 2026-10-22 [Hankook Tire expands supply for Baidu robotaxis in China, extending coverage to 10 cities](https://news.google.com/rss/articles/CBMiWEFVX3lxTE5oSW9MZURCUEI5ck4xWUFsMDZsY3J6c2dJWTVZcFpGamNWUXpFNUZBamdsdlVyZ0hSalZBS24zQ0hMOE5XR3oxZUx6T3hGX1A4OG9HZ1M0VVM?oc=5) <sub>파이낸셜뉴스</sub>

</details>

<details><summary><b>Pony.ai</b> (143)</summary>

- 📰 2026-10-21 [Robotaxi周订单突破25万笔，无人车替代网约车进入商业验证期](https://news.google.com/rss/articles/CBMiVEFVX3lxTE82YUlXRTRURjh1SElJNG9PdWtLd1dMSjdCSGQ2Y1Nnd2M2UmxEYXpzbU1rOFdPVTBDZEZGZnVCTFlaRWl3UFVrMmZJemVrX09FOWdXUQ?oc=5) <sub>虎嗅</sub>
- 📰 2026-10-20 [小马智行－Ｗ(02026.HK)11月18日举行董事会会议考虑及批准三季度业绩_股市直播_市场](https://news.google.com/rss/articles/CBMibEFVX3lxTFBUUk9rUTU2dWJiZHY5azNxSEhoN2hPWm9uaHNuLUgzSHZSQWZxR1JRbjgtRUN2a3FFTU5zV2dzVnl5UGxsVTVFTGFEWmJNeU5hS05nQUN3Z1V3ZzBOVWdZMmZKcmd2azdsZmtPMw?oc=5) <sub>中金在线</sub>
- 📰 2026-10-20 [5年招引16个百亿级项目，广州南沙产业聚链积厚成势](https://news.google.com/rss/articles/CBMijwFBVV95cUxOckZMcHo0c2p6SmlUeVAtSWRFajJGNmFrVUNNMVhkb2daenJoNjVyeDVwTndieWpkVlRManhka1JUaVl4eTBXU09jZ0JNdXRJdW9QTWh3WkFkZlB3S1ZfbDYxd0Vqa3llX2htUVRDV0FQTjE1cVNDX3RFY1BlMmVINTl5VWJuSG84Q1REeml2Zw?oc=5) <sub>21财经</sub>
- 📰 2026-10-20 [Pony AI Inc. Announces Third Quarter 2026 Earnings Conference Call and Financial Results Date](https://news.google.com/rss/articles/CBMixAFBVV95cUxOdTREV19naVQxeG5XQjlxY3ZvTFZ1QXNPQ0RzYU8wVmgyZTJTQ2lfdV9JQ0xrUVJfaHpNYXE1Z051b253TGI5N2lDZVFWanZueVZWM0FzNmZvV0w3SDc1Q2VpUFBvcFJldUw4bW5DT1RlN3otRW9WaTJuN2ptaHMtemUtYlRwMHkxVWR5ZUpPTXFxWVVHSUtrdnlPelNqaFI5b2EtRjV6bk1tZ0N2TFlRWl9BVHRRdEpVajh6Y09ZVktncktn?oc=5) <sub>Quiver Quantitative</sub>
- 📰 2026-10-20 [2026 国内 L4 自动驾驶企业盘点：魔视智能、小马智行、百度 Apollo](https://news.google.com/rss/articles/CBMicEFVX3lxTFBobEJvX3gwU1lhMTdBdDY2RUNJellLbHA3WGJleHRtdFg1Q2FaR3pJSkZ1SDZQNG9qaHFPelFtUFdXa0VTMms5T3pwZDFzUFNqMDRLbU5ZQjFrT1pxTkd5dC1tMVNaalM4UlU5VEZfMng?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>WeRide</b> (162)</summary>

- 📰 2026-10-22 [文远知行等在珠海成立投资合伙企业 出资额1600万元](https://news.google.com/rss/articles/CBMiYkFVX3lxTE1NUFNrbzZ4MzJOSmhlVU9EZFJId2k3dFA3Z2xOb0d0VXNXOHpObnFRMU9ZQnFna0hJLTIzNGdGc3N0XzdHNHRERmZjaE9wTDBZS2tpaHl1Z2E1bllKYXlCTWl3?oc=5) <sub>观点网</sub>
- 📰 2026-10-22 [文远知行-W盘中跌超5%](https://news.google.com/rss/articles/CBMiXEFVX3lxTE1wODFUX0hOa3gtbmxPMERLczdFb2VvbXVNRllIYkM0c0hNU0YwTmZzMm02bjJQUTBwTm5GcFFkQ2hQb0FWbDc1NFBqYVFvM19wSG0tMmx1U3dTdS1S?oc=5) <sub>www.caiwennews.com</sub>
- 📰 2026-10-22 [芯联集成前三季度营收同比增43.09%， 毛利率创历史新高](https://news.google.com/rss/articles/CBMiUEFVX3lxTFBQMVc3a1F6Zm1XSGc2dlZSSHNKOVoycHJPX0c4M2xXY29XNEVqdjFfWjJkTzRfNnBHem90V1ZaeW9BeUtXRXdIWEpLUDhEZy10?oc=5) <sub>盖世汽车</sub>
- 📰 2026-10-22 [特斯拉Optimus规划年产100万台，周产2万需一年](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9jRkhUWFlFejZuN1NKenQ1SnpKa3NfclVkY25jcktBRTN1U0gtdjlRSTd5eHM4MTdnTk1acFducDVxSWNFWjNua3F0eXh1ZUVFaFVIYzUwTjdzd2c?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-21 [Sunway plans trials of autonomous buses, driverless logistics and electric aircraft in Malaysia](https://news.google.com/rss/articles/CBMimwFBVV95cUxQRGM2ZWt0ZXFhcGo2UEVYeEZLank5WktEMzJvcGx1dVVYZUJvcU10aFV1Q25DM1JmZHVQSXJYVFdxZ2hSdF91SWZGOVRTaTZKeGxRYkM0SnR3SktMSXNsT0trX2pTRGI5Qi1KU2o2RE42ZmJHMzJmbmRxUjFiX1IxNEVFM2FrdC1RdVJxQXo2bFBDaGFZMXNiNzRkQQ?oc=5) <sub>TNGlobal</sub>

</details>

<details><summary><b>Horizon Robotics</b> (150)</summary>

- 📰 2026-10-22 [Autonomous Driving on the Horizon: Divergent Paths of BYD, Huawei, and XPeng](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1rSVc4NGFJdGtBOUpsdnhfRjVWU2hTekFiQVZvdFJ1SUtaWGIzWjNhOWtxdHNlNzQ0dlVsQ1lPaFkySlJoMno1Y09UV0JqbHJ5WGZV?oc=5) <sub>36Kr</sub>
- 📰 2026-10-22 [比亚迪华为同台谈智驾！何小鹏再次开炮L3，六位车圈大佬激辩](https://news.google.com/rss/articles/CBMickFVX3lxTE1MTEVjdXM0aEc1SC1XR0MwLTFhTU5fZ2F1OFdzSjctUGtxYVN6RWRodWxQWlFtRmFMWjBXZ1dSY0NqZ2xESUJoMXpFdVdMUHYxY3NleVRpZ1UwcG1lRGU2Q3Y4V1Uza2I3V2NtMmtaS3NCQQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-22 [世界智能网联汽车大会，大佬齐了。最有意思的是德系三强一把手都来了。大众说在中国搞研发，2027 年 L3 就绪，找了小鹏和地平线合作；奔驰宝马也都找了Momenta 做智驾。以前是中国车企学德国，现在反过来了。L3 时间线也乱：大众说2027，比亚迪说2028，何小鹏](https://news.google.com/rss/articles/CBMiY0FVX3lxTE5ZNmJYWmlhaG1FazhfUmM5YWRETlVUYTM2NVczcW5UMEMwd0xUVnpGQnd5OWZRVnJqeVRtN05udTlTeEphV1ZNZzRfMm5nVE5jSDRWQW1lWXNla0V2bTQ5TWhxSQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-21 [博世拿下千万套订单，地平线芯片出海，Mobileye怎么办？](https://news.google.com/rss/articles/CBMiiAFBVV95cUxQRUg1V0lmQ0RnVTFvb1RjaFV2M2lDQUhBdk1LTkpiRE5rX1Npd3JnWEFDSFhkSFVldEVqWWNmWnNSOEg3VVJoX2Zqa1BsM3pXbmlLVTRMbzI4ZFpKcks1eUx2NVY1bFE5Ml9TcThfMExfT0hoNlJBd1E4OU0zdjdFNXF5Q1U2WUJE?oc=5) <sub>搜狐</sub>
- 📰 2026-10-21 [捷达M6将于10月22日上市 预售8.08万起 续航最高555km](https://news.google.com/rss/articles/CBMia0FVX3lxTE9GNi1yMHNEVmtQaFNkc3lFMFVFTTNkN0pTZVRnYmo5RmVOTzRLZF9CU0JWUWN3cUJkN19zWi1jQU9WcE4xUmV2cHhoNGdTaXE2dnBWNnZ1dklSb3UteGxUc3NoNEZGYmM4dlVF?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (33)</summary>

- 📰 2026-10-22 [赛力斯首款量产车，不选华为路线，这台溜背SUV 有点不一样\|赛力斯\|AIVA\|ME7\|华为\|宁德时代\|元戎启行_新浪新闻](https://news.google.com/rss/articles/CBMiY0FVX3lxTE5Jb0pMdllfRElOZEdGNHplUXgyUlpILTIxczJmeElDUXJpdUtZS1o1cHlHZ1lCeUlQT0FPdDZ3bUxNbU5XQ0RHZkpQVU9PeWdhdFRhd3RSZkE1WHVGMWxKQlBDTQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-21 [新芯航途完成战略轮融资，雷诺集团首次投资、奇瑞汽车追加投资，历史累计融资约50亿元。](https://news.google.com/rss/articles/CBMiVEFVX3lxTE4wNTZCVVA5R1ZTTmNTWFZIZXVkbVlza09lSDFETkpqTWdaNzdDVk9EeDJJTmdHVTJXUmlQbWFrc2UxVUVUbGhyY2JEek9SeFpDaFdJTQ?oc=5) <sub>虎嗅</sub>
- 📰 2026-10-20 [对标小米YU7，赛力斯全新品牌新车曝光，这车“含华量”高吗？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1FOUdwR2hiMVk2d2tKOUUzMFk2VkVKbm91cUpVRHFac1hmanBZOVlBSnB4NThBV1JVRUpZSTRGYXZRNmFyS3FJS18xcHlvVXl0MDE4WWxvOFBfdGs?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-20 [2026 国内 L4 自动驾驶企业盘点：魔视智能、小马智行、百度 Apollo](https://news.google.com/rss/articles/CBMijgFBVV95cUxNV3VKQ2pmYmJ4RWhCQzN0RV9Rbkk1SDF4dFpjNngxR2VJS05HbFJBUXBWMGZwSTlNWllUY2dtc05ueWJuVElaWGUtVlAyWW5KNVJPU09WUmhHdUYyOXlIWjViekMwZTAwWXZBRGtydVpmUEpKQmZkSThlejVwRUo4SDVyRGh6UUxnTXNCUHl3?oc=5) <sub>新浪网</sub>
- 📰 2026-10-20 [【视频】900元预算Model YL脚垫怎么选？固特异这款环保又耐用](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9OWmRtS0ZsSVE1cUtSNmtjYi1lckQ3NkFadHJqMUVzdkllSWY1SndYUVdiMzBnLXp0ZG5EcHRQaDZ5LVppUFBYcVMzc0NvOFEtX2N4X0dPYVVKRFE?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Mobileye</b> (18)</summary>

- 📰 2026-10-21 [Intel Banks $150M Paper Gain As Joby And Mobileye Rally In Q2](https://news.google.com/rss/articles/CBMiywFBVV95cUxOZVNKbmU1VlRTYVdUcExFLTRvdXhPLWJ5MkJyUFVMT3RMMlFvWjI5ejFPVjBfVFlET0p3RG04enRyd09pMHdpLWFZME94OXFoNHdFdFBJbXNMekRhR3pfcGstVmRWMTBEcHViMDdBaWxSLVRPNHhNUlZLYkRlcE1xM1BoS1NIWmpQUk9zQy1oUm5Fd1BOUWkyQkpGQnF5YUltUDAwS0tEYnJ0c2hkNVg5ZWFGalpxTTU4V3JyU3ZVc3MtazFJeXdkVnhHNA?oc=5) <sub>Stocktwits</sub>
- 📰 2026-10-21 [Mobileye cut to Underperform at RBC Capital on ADAS displacement risk](https://news.google.com/rss/articles/CBMiuwFBVV95cUxQbGV2OURKazdBc0c3ZlkwTDg1aDBENU5uN0ozYXRaQTBzWnNyX2hEWjI5Tm9FSDkybXBsVHFnNjJHaW9OaGg0NUsxY3Qzd2dKRUx4eUhBSW5EU242VVEwV3lKU3k3ZkpGUFpYTzdVNnhXQjVzU29YTVdCYndDOElCQkNVd2l6RzdkQ1ZyMHhsc19TQVJVS29kSmtoaGFfZkhxWkZMWEczLTlvSk1Ga2pwUWdBLTgxd1BnUmE0?oc=5) <sub>TipRanks</sub>
- 📰 2026-10-20 [BlackBerry Climbs 6% as QNX Royalty Backlog Tops $1.2B; Aptiv Edges Higher, Mobileye Global Holds Steady](https://news.google.com/rss/articles/CBMi3AFBVV95cUxPWk9iSUpIeHRDOXd4T1NSYnlfYkJVNEJaLUlONWpKSFBPdFhsVHhGMjN2VDRBeS01ZDViX3E5ZWQ3QUU5UGtZUDFfZXpkenJfZHREZXhOZGMxRVM2MHloMGFheVZkNTQ1b05xRHFWeG84cXFIc2x2NjJYcDZaRkEteExDTk5iTnBxRGczYWtGaWZ0U0pIQmVpNVEwajJwS3ZzZ2ZYQV9UbUJ0OWwyVlNDWlFqZGtsUTR0cHpnd1hqWk1yU3VwMllCYTIyLU1XcnNBOFJEbE5IU0NNQnNo?oc=5) <sub>24/7 Wall St.</sub>
- 📰 2026-10-19 [DoublesAI unveils CEM AI model to cut computing costs by up to 67 percent](https://news.google.com/rss/articles/CBMiuwFBVV95cUxOUWExeFBKN2RaRFduZUY3UGdHZXNjdGxEWklyRnByX1oxcWhidEdUbjlnbTlQQ2tRMlZkT2NCazZkTC1wZTJtVEtTMWhhOUl0cGVOSmstdllLa3N2UVFsd0lQM00yVmg1THVKVVF1TlA1ZXkzY3FIZGVZR1lsOHNucnhCcEdEcTB1cS1LbDZ0aGxuQjJodzd3VE9md3MxZzQ2aG5nbGpybnRKN0FQR1ZXRG92TDVoR3dGU2VB?oc=5) <sub>디지털투데이</sub>
- 📰 2026-10-19 [Beep Begins Testing Autonomous Vans with Passengers in Orlando](https://news.google.com/rss/articles/CBMinAFBVV95cUxQYjhIdjZwdXJCellJZVUteWZIQkgxZEJoN0tldFEyV1pxTVNyRlh4dzJsV2NKOHd4UzNxa2YxLTJQQk1qelA3cm9rVWU0VXJCZ2R1Q3JNbW13dWc3ejVoZk1wX3NEN1VodFZTS3ljVVBHX2JXTmRvdTJDTkpwTXA5MVphMEliRnhxX01yQTg1d1ZkN2JiM2xfdmhrSTI?oc=5) <sub>Future Transport-News</sub>

</details>

<details><summary><b>Aurora</b> (62)</summary>

- 📰 2026-10-22 [How does a driverless truck get refueled or stop at a weigh station?](https://news.google.com/rss/articles/CBMivAFBVV95cUxNU2tla05zSVRfNTd6cEM1Z0M1MjZxdHo0X1BaMkpBekpTSUpRamxacVJiVzBhSGtrSUZOSXV5RkZfdHBoUkFOR05hSkFrREk5dXFKN0hWQ18tZVNWRTJpS2xMY0JBcEdGWW81czJPeENibVFmTUJFUGtUNVRmdmc3eldQT0tSS20wX1prcXpDc1RTMEhlRDV0V2djd09YWVJobkV2VWlPQmktaUY3SWw4bDVaTVVUd3drOVRBVg?oc=5) <sub>Truck News</sub>
- 📰 2026-10-21 [Aurora (AUR) Is Scaling Driverless Trucks. Can Revenue Catch Up With the Spending?](https://news.google.com/rss/articles/CBMiowFBVV95cUxNRVlhdGZlNW9kbG91b2IwcWliTjExLVBmVXRsbnV0Rlp5RXNrN0FfaTc5SVpiNzRxZkdZZVhFZnExa3hPVE5TZnhlSnF1VDJGQ3BrT3FDWUpUS1E3LXBOTGlSYXlHVGFJV2FPemcyb0pDNHlEdmRmQ0Q5NnpNaVNzZXFTUE5RS20wb2ZtMGVUeFY5clRRZUJHWHJmdmpfeWUzMnI0?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-10-21 [DOT Grants NAM-Backed Waiver for Autonomous Trucks](https://news.google.com/rss/articles/CBMidkFVX3lxTFBFeWxvajNoRkNDckxWcS1Yc0l4dGpWZXRhaURHLTBfUTVVcjBSdEZldlNUT1M3eERUSE9iUXBJd0I1Q2N0T3ZUQTFhaThPZVZRalV2aTl6bzN6dFUySnpFcWcxb0JZVGQtRWRJSkkzX0JMN0U4MXc?oc=5) <sub>National Association of Manufacturers - NAM</sub>
- 📰 2026-10-21 [Federal Motor Carrier Safety Administration (FMCSA) Grants a Crucial Regulatory Exemption for Autonomous Trucks](https://news.google.com/rss/articles/CBMigAJBVV95cUxNQjItT3d6TUxmeUxoU3pjMzBFeVlWbDNxczZSRER0U1c0NFdwOTlMX2kyck1PWnpjbDkxOVdtX0tYY3RUbHd0Ymt5TGJrX1BUczFhVFVHYkxCb0xtQ2hZSFRVVjM4Z2VCZmV4NGt1SHhZNm9XSGhybGc4NWFxc3BvTTlPZVVtX1FZTmV2bkJ6WDI3NU1MdElqcThnazBaMl9PeDVOR243THctYXNPRF9SUnFTUnVhQmo0RnJ6T2N5LVZtSVAwQWpLSHFqMFN2RzNzYnA5T3NGUVNJVDB1RzBwRTl6b3lmRWNJb0loVzdjQUNFdmVHV0hmYnl2YWFXOTQ2?oc=5) <sub>Sidley Austin</sub>
- 📰 2026-10-20 [Trucks at ATA's 2026 MC&E in Charlotte, North Carolina [Photos]](https://news.google.com/rss/articles/CBMipgFBVV95cUxPZENwSTBGNU9tanAtcTRjaWtSSFlRQUVyMnZTVEtDVnVmR2E1SFEzVy1JblNObU8zZGVfUXhMMzcyUDhmVEhNVENnVVgtMXZvOUdicXJBZjQ1RmVjc3c0bng5bkNsWDdZSGxxUUI0NTIxWmN5UExQMVJkcVc3SEhWbnlXUU5MU1owWVNMdWNuZUU3VzlkN1huT3J2bGRsWVlzQ2JjcHR3?oc=5) <sub>Heavy Duty Trucking</sub>

</details>

<details><summary><b>Zoox</b> (62)</summary>

- 📰 2026-10-22 [Tesla Delays Unsupervised FSD to Q2 2027, Robotaxi-Only](https://news.google.com/rss/articles/CBMiggFBVV95cUxQbDI3WUtQRU9wLUpiZWFieW5nSzdaSnFmY3FsSE11ekRZVDM5MUdMRE5Oa01nZ0VCYjMtUTZoYkpjNkR5aVVEUWFWMUpPMV9IRDNJYnh4UFpuR0lRUkRvb2JtZDR2d05sRUt1UkljMnVyQlgyRFl3R1p4TEtvYnNXLUhn?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-10-21 [Yomiuri: Japan's Carbon Fiber Manufacturers Expand to Robotaxis, Space](https://news.google.com/rss/articles/CBMixwFBVV95cUxQNzg3LUNDWl9vekhpc29xRzFXSFVmbHZ5anp4RnhOVUNma0hVZE5hNUtzczNRR25CSVRUWGlVdEFLMkVZcDg0R3lqbXBEWDdTSGFVUlZDdGhwSEtsSkRvZURYWDFfOUxRSGdYMDhGQVlaQTBZcDFxa2pXcU8zN002RUNJOE80LTFIR01TNzZfU3dWelRPSFphVDFVa3ljbDh1SjdBRnRUX2lNbUtzQ3MtenZUVFY1TUtjZEtnd0RDNkd5SHVsU1dZ?oc=5) <sub>MarketWatch</sub>
- 📰 2026-10-21 [Amazon (AMZN) Trades at 24 Times Forward Earnings. Can Its Cash Engines Fund the Robotaxi Bet?](https://news.google.com/rss/articles/CBMilwFBVV95cUxOdHNyTEhCeThPa0lFMXQxQlhZaHBCbjdnX2ZtT3BRQkd2OFYxNGpiZzhHYVZHWXNuVjYwYXc1NjlXUEc2a0NMbTVuNDVwS3NpRXRrMjM0R1d4TWp3Zk9CMFlHb0gxRXZtTEJpQmVSdVc3ejZFMXJjTjc0QnowWGVaSXE0ZFBJWVY5bXlieVN5SDE2YmpfMEVN?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-10-21 [A Roadmap for Regulating Robotaxies](https://news.google.com/rss/articles/CBMijwFBVV95cUxPeEV3ZVpfY3V4WGV1UWVEM1JOd0pyZGhITHZFWjhpYVJJOFBNRTZvd3lDdmpqMEY1SnNqN2ZzdmllejdpOEJScnYtWUloUWNGMUE5Y00tSldsTEUtNVBleGFmQVYyTW1QRXNXeVM1OVJEMmZxR0FnVFp4cDB5cUZHS2NzWTJqdXV6Rkd3dE11cw?oc=5) <sub>The Regulatory Review</sub>
- 📰 2026-10-20 [SAHARA Las Vegas Now Accepts Crypto at Its Casino Cage](https://news.google.com/rss/articles/CBMimAFBVV95cUxNZGtJYjl6eEtVdjVxXzUzaEs4Z3B0UjlTNF82YmtJZFhPTC13V0UwQTBadHhvdDhabWpiMzVDakNGRkRxMHNVeEFMTmYycmVISWZhaDB6bFh0eGlCTzR1YlgxV2xIMjJKRUw2YktlQmpoNmwtNTlpa1k1dGlTQkEwRjVnWlg1MjV1cE9mRmpzUXp0cU0yQXp1eg?oc=5) <sub>Casino.com</sub>

</details>

<details><summary><b>Motional</b> (20)</summary>

- 📰 2026-10-21 [EU Regulators Open Probe Into Booking.com Over Fake Listings and Phishing Scams](https://news.google.com/rss/articles/CBMidkFVX3lxTE1Rd2lBWTFiT2s0UG55ZzNOS2NlQ1JOQkVPX3hwSEhRQ2tTa0ZpS19telVJUmRSclZnZXlBSEF3eURRcnNTUDFIaVZ3VG1rcUFXc1cwOVRiU2hIMnFDY0pGTVVVcTZ6U1Fhc2JVSU9xdkI0eTRiX1E?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-21 [Taiwan Blocks Grab's $600 Million Foodpanda Deal, Citing Uber Ties](https://news.google.com/rss/articles/CBMidkFVX3lxTE9sZHZrRlE3bFZXdlJoUEg5azRoMTJiUnVyLVNKWmNaYVgyeDdGZVJ1bEFTN196cEhuaTFJVFVhVW5fdG5aanN6d0s3MmJmVFQ5Nms3OTBCek1IS09nSkFfLUdTV0pDMkR0TlZTNlltWUQtM1k1V1E?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-20 [China's CATL posts 14.54% rise in Q3 net profit to 21.246 billion yuan](https://news.google.com/rss/articles/CBMidkFVX3lxTE1VaFpob2tDMTR0dDMtMmNOcks2V1M4V0pKWmltNTY3VmRZNE43UHZxaHRRQW9hOVVjWWFzVkxWdmlpaDRoWUVuN0xISzNUVnZsMVVYU05CMWx1ZDctS1EtdzhDbVVqS0laSGJDbkFtRExycnJRV1E?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-18 [Hyundai Motor moves to sidestep self-driving fallout in India](https://news.google.com/rss/articles/CBMiugFBVV95cUxNaXZ0YW55OGwzWnN4XzN4Y3YxeVpDQTJKOExNM1dmWkRSbUpjaUhhUUd5T084cnIxY3VSNzB6TzNSMjRreHJfN3l0VEt4b2VSM1lpanRUY3dDTmRNRWxBeVdwdlBCZGFMcWVHQkl5Yk9ReDgxbk14RTVmN0JNbU5RTWwyaVJ2ZTBRcU1Bc1BBai00eXNHMExxb0VkNEozUGl0dlZtT1BpWTN5M2dmbkZtZlI4ZEQxc3hibnfSAb8BQVVfeXFMTjY1OFZ6b3Z2S2lxd296ZHE0VTFpaHYzeU01bmZkSGJlSi1kbDRjWVJZLTl5VXhMVWRNVUxjeEg0aFdUWDg4Ukhhc2NYNkZ4dUlPQUFHeGtlRnB6QkotMDZYcXN3clRwZWduT1RndFg5WGZYWXlHQkZpUEZhb3NXNjlPYUZxRVVFcXlNTW1wWVYxUHhyWWFKbmJ3c1RsUk8xbnZmb2FIYW1EejBzWGdpNU5XT1R1dThfbDFaell0czg?oc=5) <sub>The Korea Times</sub>
- 📰 2026-10-18 [Hyundai Motor, Kia to Deploy Humanoids in Factories from 2032, Unveil 'Autonomous Operating Factory' Roadmap](https://news.google.com/rss/articles/CBMidkFVX3lxTE5BSkloNVFid1JrenR2b2g4a1N2OXI4SVNYQmRvMW5wc2lHS0Y5TVUzVlRJTjd0Wlo4UUFmWDA0U3hQTmFxOG9uSF9oOC1TMGs0cV9temVoeXhzUkx0Vzg3ZU5qNDJXRnJTb2l4VXg4U195Q2U3R0E?oc=5) <sub>BigGo Finance</sub>

</details>

<details><summary><b>comma.ai</b> (5)</summary>

- 📰 2026-10-21 [Is the race to build self-driving AI turning into a cyberwar?](https://news.google.com/rss/articles/CBMikAFBVV95cUxPd1ljS1V3ZmI4RGdJZkRQdVpkNmRqcm5tVUtpRllXYWMyQ2ZnaFFKRzgzY0VaUDNTR3VwYV9lRHI2RnRUcV9za0p3bTNsMGJmSHNZUlR0MDFsYm1FLTVtUEl1UEJhSi1hXzMtc05tendPaDltRzlMczQwRkx0dTZJaGVjTk1DOXp1cVpSS2Zqc0w?oc=5) <sub>Yahoo Tech</sub>
- 📰 2026-10-21 [IQ.Lvbs claims hack attempt traced to rival Comma.ai IP address](https://news.google.com/rss/articles/CBMilwFBVV95cUxNVXdkQWthMXBaOUd3aGV2Nl9Kb28ydFVOcElQcTUwRnEyWVF4NTVzOWd4d2hDSlFFbjc3Y2hranNuOUtSS2dha2NKYzRvUkxzSlJxSGhQZTI0MEVySU9UOVpjUlVSUEpPTl9LcWhhNWJzLXdQaEhNMnRCZUVGd0dDTEZFYzdhcTdsQWNkczU1X0UtWTdJbXdN?oc=5) <sub>news.lavx.hu</sub>
- 📰 2026-10-21 [SquachWatch Turns ESP32 CYD Into Standalone Privacy Scanner](https://news.google.com/rss/articles/CBMikgFBVV95cUxQT3EzRFl0MWRwUm1tYklBYngwR0lDVGswYUJ5TUdQNjdPdkJLajV0bklVU2FCWFdMUlJjMng5NEc2ejQyUV9MeHB4RjF2UlRxQ1pUdFpSTWlETVU4WmFxTVpLTmJ3Z0NPX3ZnWEc2M09VcDZRNmtlUDlBZU5hQmFrUlNWOHBCRGtZQWs1Z3Z4TlVBQQ?oc=5) <sub>news.lavx.hu</sub>
- 📰 2026-10-20 [Auto tech startup claims it traced hack attempt back to rival's IP address](https://news.google.com/rss/articles/CBMizAFBVV95cUxOVHlZN1E1cDJqNEFHSFg3U1hCbnZRdFhtdk11blVLd2d2dUNIVkYxUG1xd0NIWjdNZGNVMHJvalh4SEM2cTJhclMzWHRyR0thRWJDMHFNUWcwNHAza21ybFYxV1Zyd2ZoaHRORmRtdGxBbWlSWk1UUnllQVp2dGFCVlFjcE0yOG1OaW9hdGhRb0lpS25LeUZFc2pKem5QaGVnZ0pLNExzeDdUOGNERVM2andndkh4LW5JWDdaSGhqQmZxOFMtb283aDFIWkE?oc=5) <sub>The Register</sub>
- 📰 2026-10-20 [2400 miles with Comma AI, Android Auto, YouTube Music, and other various tech](https://news.google.com/rss/articles/CBMisAFBVV95cUxNeUNQVTFnMUoxMUpGT080WUdQMHlSVTBDdWxFM3lGRndwbmtZZnZGMVFZRWpDb3JoZllSVk1ZaUFCUHM0TmZTeng1bXlvQUJ4S25rSW9uZFljSExya0FPblRsMTEtZkUwWVhyM1ZqNkx1V01jbFBqdURfMlU5TmJHWnVqQV9aWUhrdUhCa25PN0tRalctSmpWYUkzOGVJUUxxUmFIeXIyczRlVGhqUVFIcQ?oc=5) <sub>Pocketables</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
