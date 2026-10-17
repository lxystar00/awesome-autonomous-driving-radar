# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-10-17 · 1,282 papers tracked · 40 curated.

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
| [SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving](https://arxiv.org/abs/2610.20609)<br><sub>Shaoyuan Xie, Zihan Zhang, Jingxuan Wang et al.</sub> | CoRL 2026<br>2026-10 | [⭐ 19](https://github.com/ASGuard-UCI/safedrive-vla) | Vision-Language-Action (VLA) models are gaining attention in autonomous driving, inheriting commonsense priors from large language models (LLMs) and widening the navigation interface from a fixed command set to free-form… |
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

<details><summary><b>Waymo</b> (217)</summary>

- 📝 2026-10-16 [Hello Toronto! Waymo is En Route](https://waymo.com/blog/2026/10/waymo-in-toronto) <sub>official blog</sub>
- 📝 2026-10-08 [Sober Drivers Still Face Nearly 4x Nighttime Risk: Why Road Safety Demands a Safe System Approach](https://waymo.com/blog/2026/10/sober-driving-benchmarks) <sub>official blog</sub>
- 📰 2026-10-17 [Waymo launching self-driving taxi testing in Toronto](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBFX1Rld2d4d2xSVXBFZ091cjNGSHF6aHRwZWR2RndaNkVPZHpOR2FJYkY5WlBkYVVsVThvUW83N0hMZHV0dk9DcG4wN0pCYS0yMURFN2lseHhhQQ?oc=5) <sub>CBC</sub>
- 📰 2026-10-16 [Waymo Opens To Everyone In San Antonio, San Diego, & Tampa](https://news.google.com/rss/articles/CBMilwFBVV95cUxPeWpMZ1VuWjFTazZmU1BZVjJlWDNuQUxpWFJ6bjlNckpEdS1HNjFnXzFyUWNaOHVQSk5wN1UtNF9sNnVRM29jQ2NfVVRHc3NCaUhuSHZwRVhSU0I1LW51VjUwU0RHOHBsM0dlT1M0NnRQS3VMSDYyb0dwRlhEVkR3cWk2d1JjakppU1h0TFlRVFFUNXlISWhB?oc=5) <sub>CleanTechnica</sub>
- 📰 2026-10-16 [Janeese Lewis George Says D.C. Should Hold Off on Legalizing Self-Driving Cars](https://news.google.com/rss/articles/CBMic0FVX3lxTE9hcTI5YnQtaGJiaG1OUi1LSmZXUjFXX3BkRzRJUXBRaEs2R2lPblotbkpDa3pRZkZaNTRXMnduTVNmT3JqSmdlMDBQSk4tYmVMYXhDNTlqeExsRGNLSGR4VS1QNUs3VlBtQVVkUXNVLUFWUzA?oc=5) <sub>NOTUS</sub>

</details>

<details><summary><b>Tesla</b> (352)</summary>

- 📰 2026-10-17 [Tesla FSD Crash Liability: Who Is Responsible? [2026]](https://news.google.com/rss/articles/CBMiekFVX3lxTE05Ync1OGZGMU9raFdhTzMxV0dGdFQyeGRFMEpPdkV6VDdKVVZHSzJFOHd2UjlZN1c4UDB3c2RHZGR5ekFicERHZnpuUHAyR0hPS0hwdEVXeC03dGU0VHF3aXVJTEw3R1d0UVdqWW1xNGlLbzlMZ0FvNVZn?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-10-17 [CHP: Tesla driver says he fell asleep in Full Self-Driving before hitting CHP cruiser](https://news.google.com/rss/articles/CBMisgFBVV95cUxQN0ROQXpRRXpNRTlUczdiMW1tN1NVUGNjeEZqWGgya3lKN2hOa2ZveVJtNWlJUy1CMlRaazRmTTFoMVRuUDViQy1BLXdWREJWS1BwWTVXRk95RU1JVzhIaU9td2JVZTZNanREMVZBTTZTTjNvdjJqaDFjd05NNGNuTmM0YTc3dy1kS0FXTUs0NVJXSTZ0NXd4d0psTl9aZ1Bwc0ZhemdQdld2TzNpM252SWV3?oc=5) <sub>KMPH Fox 26</sub>
- 📰 2026-10-17 [Tesla Roadster Hypercar is a vison of the automotive future. Here's how](https://news.google.com/rss/articles/CBMi2wFBVV95cUxObXVOcjdKc3dfWnRoNy1vb3AxY2w4R0NwSFc4UVZ0V0dlcDVzQWdPRzlYNDhaX0FVWFZ2MXQ2YVlQV3FOblc4ZGdJOVAwRW44WE5IeVVJQ1NraFlMQjQxX0FvcXBSUFJiUUlPa1dBeWJlSHl0Y2MtWlROUjBUY0ZNZGZ6QjRRckhmQXpuWTB3MmphNHJQcUo0NmdaSDZYLU93N2QwVnNSRW5VNGxzOUVmT1VqNzk1TENGdXJIcDExN3FpNjh6RkxwcWpRazJmcFJvUnpiUUZtVHEzNGs?oc=5) <sub>The Detroit News</sub>
- 📰 2026-10-17 [Sleeping Tesla Driver on FSD Injures 2 CHP Officers [2026]](https://news.google.com/rss/articles/CBMidEFVX3lxTFBsZ0x0dkxUd1dCa09feXQ5bzNnTlR6THVBZkRiOGlzYV9wdzYtUlE5VG5zd3QwWER1VlRUVVloTnAyTEtYNEFucXROMktRY0kzLUx4S2k3Vi1IUmxfbE54bjVMVmJsenk3OFc2TXJsZ2lOOXpv?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-10-17 [US: Tesla in full self-driving mode crashes into CHP vehicle, injuring two officers](https://news.google.com/rss/articles/CBMitgFBVV95cUxOTjBaNUwwbklKaDJqTnNpX0JjektCNGw3ZGs3eTBtZHNERTJQVnRVQ0NlZGpKQkxydkVxR09wVHBvNkZHV19tSFdOX3VaVnVpS0ZFdDVHN0hxUlctNFZzamg4OUplcTh5QXE2bmVCNzBIal9zQXNLdkdpUGdWTmtFOWxmSFZ1WnVNT2haN1ZobzI5Ylk1elZvdWN2RXVDWl9IVEM0eDhsb0lIOFVsZ1ZhMWI0bEs5QQ?oc=5) <sub>Connected to India</sub>

</details>

<details><summary><b>NVIDIA</b> (221)</summary>

- 📰 2026-10-17 [NVIDIA's Jensen Huang: AI Market Volatility Will Subside as AI Drives Transformation](https://news.google.com/rss/articles/CBMiuAFBVV95cUxPcXh5eDBOVkdpNWN6N3BnUjBaTE5SR0l4czZ1bE5aTHNqY2g1c2cwbmdYVnJ5a2ZfdENaWjVMUXgyckRnVFRxRi1OYXpFbzZGRmxRNjVVT2VicTM2cGdDRmZydzR1d1pVNGxJUUZxNzZrSFY1bndZX1FObUJ6VGx4dWdDN252dy1aa2Q4UEgxV0xfZUZaRXJmeW5aOWRCem9sU3lGTWRVbjlzRGQ3cjJXc0FYTktpVW5r?oc=5) <sub>KuCoin</sub>
- 📰 2026-10-16 [Volvo expands Nvidia partnership: new automated driving stack before 2030](https://news.google.com/rss/articles/CBMiqAFBVV95cUxOOV9KWUlwRU1pbk9aaDJ1andGZUVaNmo5Y3pGd28wV2FNenM1NUlwRFhDRnhSRDgwYi01aFROTEVHX2FKREY1czk4WnRGaU9zZ2tpN0xMeTVpTzdVVkQwX3d5YnY2WmFFeFgwUm1tTDZhSFNuSHktSXBqeTJJejJYb0FqWlJRR2FWb1JZeDNzV3pneGJoS1BaUVU1bUlZbVVPRUhXVi0yNlE?oc=5) <sub>Softonic</sub>
- 📰 2026-10-16 [Volvo teams up with Nvidia to develop next-generation assisted driving system](https://news.google.com/rss/articles/CBMiwAFBVV95cUxNZjEzNjd1M2xuYXNYODR0Y2xrOGJFNWdHN0NQY2tvd1BvVzBaS2FYcEo4VkpyaVl3b0x0SWZ1bV9TLUJiek9yMkJwQjZZMWRNQzNHTldselJQclZiR0d4cmtKOGUwcWRZZlhpY3AtT1psZ0JrVWwyWEZJREtBamUycU82M2xXNFlJZk95LVBLbU13cVVqcmhQb2dOWi1ZbUhJcmVVMW5VX3Vqb1RLOUZUMmJRbG5OVVRtWDdFTlVaLU4?oc=5) <sub>디지털투데이</sub>
- 📰 2026-10-16 [Volvo expands Nvidia partnership for hands-free automated driving](https://news.google.com/rss/articles/CBMifkFVX3lxTE05VnpCLTJEX0dVSktnVXRURGNXLXhFdXRfSXFFaVNreXJaaWxHMlV4TzBHTG5oZ25TVGlLMEU3Mk9TV1VpczRlUHBrSE9fR1BKOE9WLXVxOWdibnN6YzBNVGw0bFJsUlpwd29UbFVsMEE0aTMxOXVnVl9OdGhNUQ?oc=5) <sub>Cryptopolitan</sub>
- 📰 2026-10-16 [Mercedes-Benz and NVIDIA Expand Strategic Partnership to Advance Safe Highly Automated Driving in the Next Decade](https://news.google.com/rss/articles/CBMi4gFBVV95cUxQTXA1UW9vQzZaTV9SWVNMN1hYdUVlTENDeUZCTG9VR3loWWVJS1E0bjZJcFJndFNyZDZYaTh2bF9OU24yeF93d1FwbUNCWnZZbmZXUTNTcklPN25DTGtIeFN2NEdZaElkUTUtV3dHWWtKaU90VmtGWDNCYkNRcGtva21IRFRmcUFDUkhyWXcyLTFUNDZ1aGhDaHotZ1hkYmw3Z0MwM3NZVkdqR3pyZWhEVXF6ZVNoYkZtWXNwS09OQjZLLU9aaUtENVNDT3Y0NXFlcWY0TkxZNWpsY3M5QnBZNVFB?oc=5) <sub>NVIDIA Newsroom</sub>

</details>

<details><summary><b>Wayve</b> (66)</summary>

- 📰 2026-10-16 [‘We should all be worried’: calls grow to limit London rollout of robotaxis](https://news.google.com/rss/articles/CBMiqwFBVV95cUxON184ekxIVGM5blloZ0xnMDRkSk1EejBQZktheVB0ZFJDYXpDRnd2MjM2YjlTWE5ZelR5YlhRUTUwc192dGxhSmd4VEowMzc3aWdIMXlUVTJUdjRzeVQxcG54SGl2VWtKZ2ZfUjFfcVAtRkZBSEh5Zm9QdUh4c0VfRG16RU15N1dDeUVCQ3NMdWNzYVVPUlYtemxJMWtqWVBya1RTSE5TVW02NXc?oc=5) <sub>The Guardian</sub>
- 📰 2026-10-16 [Mercedes-Benz and NVIDIA expand partnership to develop next-generation autonomous driving](https://news.google.com/rss/articles/CBMilwFBVV95cUxNQjVOaEJNSERlTFpZWHAxaW1HR2Y2NUk5VjhUUEh6UVlod25yUGw2dWlLMnpBMWoxMlE0cGVUckl6OXZoSTl3Zm5wV0dEWU9IMk55SmRLZlFUU1Q5Qlo0T1o2Q1VJTTVmdG9iRXJkY1FDR0hiMGZvMzl3YlQyVGR4TUlSTlRRczg2MFZqS1dPRXBlS2RFdDhn?oc=5) <sub>Drive Tesla Canada</sub>
- 📰 2026-10-16 [ADAS and self-driving levels explained, and where the US and UK stand](https://news.google.com/rss/articles/CBMilAFBVV95cUxQR1pLSC1zNlREQm1CNGtFRWtpUTAydEFqUTBXLWxiNDBpYzNJajlEOEgxak1FeGw3c0RmZTdjRUF6d1pzaEhxV25hbkd0cFdEUHJrYmZXRVo5dWFVeFFVenRwZ0o4M1FONFkzM1B2WmgycnllQ1M5QmtkaEtDWWpvT0hkYzhrd0NvT25zYzdHYWFZaER1?oc=5) <sub>Pasquale Pillitteri</sub>
- 📰 2026-10-16 [Drivers union advocates for lifetime basic income for private hire drivers in face of robotaxi rollout](https://news.google.com/rss/articles/CBMiyAFBVV95cUxNYU8tSWNISFRCcW9PY1F0eXhPRFFlLVZQS0xzVGNpZ3VZblJkN1NpbllxWHZKUUhXYTdueHp5OVZVY2tJRGVueV9xZ2kwdkhmMEd2bXFhVWNIZVp1RFExSjQxXzFuTHduTExRcU9xNkpBcjItSmdNY2I1RlI2bHJmQUN1bWd5dGcza1BUR051OExfMXNFRVhrTlBvLVNCeC1QRGhTcTNvNnZMOTBPdTFRTWZWZzN0Z3lEUER3cUt5R2ZKRjZOVDlIQg?oc=5) <sub>Highways News</sub>
- 📰 2026-10-16 [London robotaxis face political and driver backlash as Uber and Wayve expand UK rollout](https://news.google.com/rss/articles/CBMivgFBVV95cUxQMS04RW9NUDlrdWtObzhfc2pIZUs1b1ZkUWVfNnl5N3pXUkZIZHh4bEJMNllSM2VDTEtkdlBraWZHdjlHRUxZbTBUZHViZ3luS09fZk5KODZoSkN0UEFyaWVxc1ZPNkxWNjZDVnNpVDdPMHAzNkZ5SEJfLWU5cFlvbjVLc3FrVXcyU0VONGJwYUUwRjRHN1R2akpYWXNqa19jYlZmZ0dWcVBYRElSVy01NnhfZG82Yi1ZOFFkUVJR?oc=5) <sub>https://streamlinefeed.co.ke/</sub>

</details>

<details><summary><b>Momenta</b> (87)</summary>

- 📰 2026-10-16 [东风风神L8+将于10月23日上市，搭载Momenta R7世界模型](https://news.google.com/rss/articles/CBMib0FVX3lxTFBpX0VGWjJwOVdaMHM5TkZreEVzLWdYWlhwYlU0OWVONXZXMVRQclc5SnNJUUZiX2FqaE4zV2V0Tk1oUmEyMkdiU2pJNzhNUkNrUUswUHdManpiY1RwR0pjZkhlU2R4akNOTWJZU0NqYw?oc=5) <sub>中华网</sub>
- 📰 2026-10-16 [CXMT Backed XHEART Secures Cumulative 5 Billion Yuan Financing – 36Kr Exclusive](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1CY2lTejdyVE1zREhUcXpMWmhfVGktTmxjQk1NX19mMWl3dlpnTlQxeldTeXFnUjBqa1BiTFVENHdkU2x1RkktMmxsX2RUX2dmSENZ?oc=5) <sub>36Kr</sub>
- 📰 2026-10-16 [Gasgoo Daily: Geely Partners with Google; JAECOO and Momenta Test L2++ Driving Tech in Paris; Li Auto's Chip Unit Secures Funding](https://news.google.com/rss/articles/CBMikwJBVV95cUxQUWROZVdTOWpFT2xkUm0wT2N6d2pOUXlaSGpENzRJRTdoajh2TUVaT2t1NlZBNVFDRGd0dUJBZE5UeGw4SUZzWnc3XzgtbXdWNkFwSTZjUkkyME9mdGFRMHdGZlVEMm9WU0xwMjJmUEdlclc4cURTUHVvZC1FYTdTQW00NUJUc3RNM2o1TGtfYXdsVkxVX1FqUGh3OUJEYjhWUktpSlVpRFhvNHVVNHRYeDVRSFprQm0tRjdSRVlQYUlZOVhLN19HOGN3NVJVcXhIazFFMGlDM0Jmb0NheTI1X2g1SG80Wm42N0dXdVNvc3dmT2QwdW1CdzNnTVFmQjdzdWpIUU9SamJfSjN6b2hyZlQwOA?oc=5) <sub>Gasgoo</sub>
- 📰 2026-10-16 [‘Most important strategic partner’: Mercedes’ Nvidia self-driving deal](https://news.google.com/rss/articles/CBMidkFVX3lxTFBKN1Bta0tlckhUSElCQXhKblhKb3pDSzM3c3cxdFZqRFZMZXI3UmxabXRWbDVrWWt3VXlQMmlnMDJ1NU5GMldnUE5pTFBjaEx3TExabUtoQVdIejdiZ0haZXZSSjRIaHhIdm5vVG9LaFhOWUFySFE?oc=5) <sub>The Next Web</sub>
- 📰 2026-10-16 [ADAS and self-driving levels explained, and where the US and UK stand](https://news.google.com/rss/articles/CBMilAFBVV95cUxQR1pLSC1zNlREQm1CNGtFRWtpUTAydEFqUTBXLWxiNDBpYzNJajlEOEgxak1FeGw3c0RmZTdjRUF6d1pzaEhxV25hbkd0cFdEUHJrYmZXRVo5dWFVeFFVenRwZ0o4M1FONFkzM1B2WmgycnllQ1M5QmtkaEtDWWpvT0hkYzhrd0NvT25zYzdHYWFZaER1?oc=5) <sub>Pasquale Pillitteri</sub>

</details>

<details><summary><b>XPeng</b> (302)</summary>

- 📰 2026-10-17 [小鹏扛鼎之作！GX无伪装实车曝光，配22寸轮毂+悬浮logo](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5FdHR4eVVaaFVwaTZUNE1JZERobkY3dS1hZ1ZwUC1SSUsxNUNhd3hkQllFRlEtbmxwbVVmejNzbm1pd0QtbkRsT3lSdURieUNDLWloYjJCV0RIT2s?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-17 [智能大五座SUV横评：小鹏G9L第二代VLA全系标配与智界R7、理想L6怎么选](https://news.google.com/rss/articles/CBMickFVX3lxTFBnTGVkUjlkalgwdFZnc0xMMVhzNm5RVS0ycUU2MXQtVFZLc3J2Z2lPanpKX25MWUlxUTZsNHFVVjhCX2ZpQnJEVTZ6MW44UXVaZ1BrTEJRSGJXc0k5R2Z5RmdOUVNoQ2FuLTd3N2lzcndlZw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-17 [25万预算新能源SUV横评，小鹏G9L与极氪7X、理想L6、智界R7怎么选？](https://news.google.com/rss/articles/CBMickFVX3lxTE0tZmZac3dzbWhBVVFubG5hc0ptMG5EUDFsRTZldWZzOUthTzgtQTdGMjNMSmkzTWZUdi03TXI4TV95YmxQVndiM0x1M1otMDF5Vlh6VjFDS2xKOXpJcXZ2WXBpWmtSdnpnQnFwa3dHRktEZw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-17 [充电最快的大五座SUV横评：小鹏G9L、极氪7X、智界R7、理想L6谁领跑？](https://news.google.com/rss/articles/CBMickFVX3lxTE1aMjNnc2poM08wc3d5UVBhTUFHZGY3VDlXR3NXMjFEc2c5cG4tcVU1THJJRVlQcmdrc2h2bEZudnMwV2dnWmg1dUNFLTl4Sm5oaThoeDFuR1hzUm50d1pIenV4R0xINUlRNlR4clYxLUg3QQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-17 [小鹏MONA L05预售价16.98万元起，满足中欧澳五星安全标准](https://news.google.com/rss/articles/CBMic0FVX3lxTFBhMkJ2cVc5Yy1EajJqVGF5dzVmdUFfbmxidHlBOFdLbVJjbERib3dsSXJ6R2xfZ0RFUVRoeFp0NFEyYzc3NWh3N04wX2ZlLUlaVG9xTzBHcnNhakNlSWp6S2pVaGtpaTU3MmVTS0RtVTdNUG8?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>Li Auto</b> (155)</summary>

- 📰 2026-10-17 [全域全能还是城市专精？神行者8、领克900、理想L8三车横评，30万级新能源SUV选购指南](https://news.google.com/rss/articles/CBMickFVX3lxTE0tMGhGWDhDcV93U25JMTZaU0Z2N1hsYm9xNGlRbFVDV19vMGd4Q2hObW1manJuYUhSYi03VEZNYV9xMDZUU2xmOGNSUUdSTEVXdWx4bFZzZDcxb3o3Umx6eV9jQU82X21BXzhPRERCZ1ZUQQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-16 [Li Auto's chip unit MHX raises $243M in early VC round](https://news.google.com/rss/articles/CBMikAFBVV95cUxNYUdUb3RjZFhDd09acUFRZzE0M3EwR1BEcXowMnZUcTZiSzNBdEF5NGJCME44Sjk5ZXo1TGo1ZjlWMXk5OVVpWHlLNm9qSEJTdjViUGU4QUg1MExqVTduZ2FEeUE5eUw4c0l3UUNwVEZpakltNklrZ2VFZl9UQUlHemVtM1Q5dGw4TFFab2ptVmU?oc=5) <sub>Dealroom</sub>
- 📰 2026-10-16 [Li Auto chip unit signs first funding deal at up to $2.5 billion post-money valuation](https://news.google.com/rss/articles/CBMif0FVX3lxTE0xM2ZoV0ZfLWgwZS0tbmVoeGVvZ1pvM0ZtY2NKazliY3VtY0pKTVViY2ljZjkycndNSGJRM0lIVHdIYVg1Y25TbG1nWTlXYnpreUxXVFpoRWFZdFJNRUdrTUZMTFJPQzEtN3ZVYWRZRUxsb0c1NDU0RU95bkxOMjg?oc=5) <sub>CnEVPost</sub>
- 📰 2026-10-16 [Gasgoo Daily: Geely Partners with Google; JAECOO and Momenta Test L2++ Driving Tech in Paris; Li Auto's Chip Unit Secures Funding](https://news.google.com/rss/articles/CBMikwJBVV95cUxQUWROZVdTOWpFT2xkUm0wT2N6d2pOUXlaSGpENzRJRTdoajh2TUVaT2t1NlZBNVFDRGd0dUJBZE5UeGw4SUZzWnc3XzgtbXdWNkFwSTZjUkkyME9mdGFRMHdGZlVEMm9WU0xwMjJmUEdlclc4cURTUHVvZC1FYTdTQW00NUJUc3RNM2o1TGtfYXdsVkxVX1FqUGh3OUJEYjhWUktpSlVpRFhvNHVVNHRYeDVRSFprQm0tRjdSRVlQYUlZOVhLN19HOGN3NVJVcXhIazFFMGlDM0Jmb0NheTI1X2g1SG80Wm42N0dXdVNvc3dmT2QwdW1CdzNnTVFmQjdzdWpIUU9SamJfSjN6b2hyZlQwOA?oc=5) <sub>Gasgoo</sub>
- 📰 2026-10-16 [Li Auto looks to commercialize in-house chips beyond its vehicles (LAAOF:OTCMKTS)](https://news.google.com/rss/articles/CBMikwFBVV95cUxNTVNqZlp5eEVWOXQ4R3d1dW84QmZDRlh4QnRCSVpqOWIxbk1vS2ZSN3BFSThRcGVNWHA1LTl2ZXdDTEdGVEtCSFJnU3ZISU9pOGdFb1R4djVUZDdsNzhHRHY1WUItOEpWNzd3NkMxRDNLNXYyVmFwNFhITDNBX2pEa19RY1YzUk05Y3pWdGs1QUxLczQ?oc=5) <sub>Seeking Alpha</sub>

</details>

<details><summary><b>NIO</b> (147)</summary>

- 📰 2026-10-17 [小鹏G9L对比极氪7X、智界R7、蔚来ES6，底盘操控谁更扎实+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5nRjBPV2NzU05FWTd5Q0tRbW5QNUFvMl9ScGtHSXBJRVJNMnZlU1k3UVctSTJfNU1TUTYyRXZkclpsWHlEcEtwR1N6bEpyWXo2OWlRSm1VZV9renRUazZR?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-17 [大五座SUV操控横评：小鹏G9L、极氪7X、智界R7、蔚来ES6底盘谁更扎实+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE9fWFBYanVzYWJiWl9pSkZHSXlUWExLYVp5dDhkcHJnczFxWTVmUmd3ZU1oQVdhdjhwSXNFOUZRcFg2aFpTaUQ3VTF4aE1xaUZLenN2dnBfREdUZHZWQnhTdUJIRFpldUhrdU1kb3NRVDg0dw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-16 [智能体验好的大五座候选清单，小鹏G9L第二代VLA全系标配入榜](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBDSlZ2TzIwUlpUSGRzU0xnalg3SGhnRnFfSUxCbU41ZFRRczJVeE42eWFjbEtmZjRwLXEtQllpRkc3MVNaM1ZQYVh0RjhGX2M5Znc1ZnRwOWZfYUhucjR3?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-16 [底盘操控好的大五座SUV横评：小鹏G9L、极氪7X、智界R7、蔚来ES6谁更扎实+选购清单](https://news.google.com/rss/articles/CBMiX0FVX3lxTE4xNW0xR1VRNlBmQXlZZjduVXVqdTJjVGxUXzhCRGRhVGxQc2Nmb1A1ZGpCMm1makpEbExrbUlJR3o4QTc1MmJlYlo2Ni1QanJ5Y1BRdE84dVNUeElYSmZn?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-16 [Tesla's Roadster can fly, and Nio's William Li admits: 'This we really don't have'](https://news.google.com/rss/articles/CBMihAFBVV95cUxQb3QyQUtDdW1pbEQ1VlY2MUZHd1BOMmhkQVp3QVlCVHBVRmx1cVlXR1lTdWZKQzZIUllZX3NlVXdvQWUwLWRleUVKSnlpRS00SlFVLV96QWVaQ3JLVndYaXRrNTVhaGdrNFM5bHAzSDVDVHprUUJmeUdYU3FHTnU5aWlzMHE?oc=5) <sub>CnEVPost</sub>

</details>

<details><summary><b>Huawei</b> (352)</summary>

- 📰 2026-10-17 [【视频】华为乾崑智驾ADS5 加持！纵横 G700享前所未享](https://news.google.com/rss/articles/CBMiXkFVX3lxTE5zWXAyaXFxV2pLa0FwZmF0ajA5dlE0MkJoSEFSSDBoWmhyV2pIa0lYREFsR1lKZnlwQm5UdTNsTzlwVHotY1o4bVJhZ0pXdnZtLXpnUnJIenpJd2cxQkE?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-17 [【视频】10万买华为智驾六座SUV？星海V6真香还是噱头？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1kUnFwQzJ6bDlxemM2SHRPWnpVTWlWdmViQmUwNzYzUEt3eERIN3VmMTNpM3l5NFlUVmZ6Y0xKTWVjSVQxbFdaYWJzb1NPUWY5Q25uSjdFcktpNnM?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-17 [95%用户选中高配，奕境X9读懂了家庭旗舰的真正需求](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBDR004U2JIS29RbXc1ZFdzYzFBRHItTXQtalFLSXU0R21KQlVISUd3RG9DZlFCUmt0dzB4aFpvV1lGdS04ZUFHOHltLWNOOC11aENDNWZ0cURlRW8?oc=5) <sub>车家号</sub>
- 📰 2026-10-17 [【视频】乾崑智驾+双AI加持，极狐阿尔法T7是你的菜吗？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE85dllmeFNDRXJtVUU0SFdLRVlQY2xRRktFVm0zZlExVkZiX0tHR28zbW41T2RLN3lLcnBPRXNQTFphNGlQLWI4UE9PZ05NQktaSnA5Yi1yYk1EdzQ?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-17 [【视频】24小时大定突破9157台降2万/奕境X9反而更值了？](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBBV3ZsVE9hdXQtWTkyYUJuTXhOVG94QkZIOUFTU0JTUVptMGZTSjBYRUplR29rQlBZcW5rWUFnc0M2a3piQkNCNGpHYWNEc2pZV28zbV9sdFBIb0E?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Baidu Apollo</b> (47)</summary>

- 📰 2026-10-17 [科技早报 \| iPhone Duo首批现货最高涨7143元；长鑫科技预计前三季度净利超1300亿](https://news.google.com/rss/articles/CBMiWEFVX3lxTE84Q1BrQ3hBT3k2VmlQdmZtMDBXN0xvcUpkT252WElIRmNNVlQ3YktOYzlrTWdkT044ZWNkUXEzMnNkbGVfNnJWakp3WUFHYmFJdklyaHc1YkY?oc=5) <sub>Jiemian.com</sub>
- 📰 2026-10-16 [Baidu opens Tung Chung robotaxi public trials](https://news.google.com/rss/articles/CBMifkFVX3lxTE51Y2F6QXRJd0JPaVBydjNhVXBhQ0o1UnNHWjd6RTZDbl9VS1RraTE0dkhlRjEwRHlCR2kybFpOLS11LVBnbkRIaHdXYjdGZzhGWVk1TkVJQUJQOGhyNnNIUGtBaXYzZHFwU0tHem90dmZuWVhkZkp4azN5ZWZUZw?oc=5) <sub>Dimsum Daily</sub>
- 📰 2026-10-16 [百度萝卜快跑10月21日起香港东涌开放公众试乘](https://news.google.com/rss/articles/CBMifkFVX3lxTE14UFZZZ3VfSzJqUmpNVUhuWEVmRDAtcWdfOTJGdFBIUVNwNGk3TXJsay1sSTRnV056bWdoZ2VxRVJPTnhQbHF0ZEtkYVFGWTEwSlU3OFRrcTd1QU9ha2J4a1dmZEMwZjYySXBNdTRET0hGOF9PMXNQeFRLZDVBdw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-16 [萝卜快跑将于10月21日至11月3日在香港东涌开展自动驾驶公众试乘](https://news.google.com/rss/articles/CBMiXkFVX3lxTE5EUm5iRG5sM242N1N4QlowLUlrYTRQcTlaYk5TSFd3N0tZMndtWjVkMWpEYkZkeGhWMF8wNW5mMXN0eDhHNmFweXhqUEJ4blNQVVVtajFNV19OaExDanc?oc=5) <sub>车家号</sub>
- 📰 2026-10-16 [HK又有新玩法！百度萝卜快跑下周开放免费试乘 限量1000个名额](https://news.google.com/rss/articles/CBMiwAFBVV95cUxQc3NhR0ZmbzBybndGZlZoMm1ETHRJWENXOFhUbmVES1AzY3M4R0ZkMDBHR1JYUGF1U082SU1WMnBvaWd0aktzMmpnSV83UzJ0cWNHd2tsUXdFSWJJeUIxOHlTalZlYlJlamlvVnZ4by00Ry1PeEkyenQ1bkRFU3owbDNWWmd0SF8tVlZIR0gyLWlRQWI4NTA2QlppaWNSbFBHWFhaWGtCNHBWdG50dTE1cFZxa19NRi01LVctTjg0RXQ?oc=5) <sub>加拿大省钱快报</sub>

</details>

<details><summary><b>Pony.ai</b> (143)</summary>

- 📰 2026-10-16 [Uber Announces Manchester Autonomous Vehicle Testing With Verne and Pony.ai](https://news.google.com/rss/articles/CBMingFBVV95cUxOY1dZZzRQbUhwV1NyVEdWY2lKUzFKemthX1NETl85NDFQVGJyWEFqZ0xxNThEbDlnMC02RWZLc25BNWgyY09nZGdGdmx2LTVoTDdqR3dsS295YTZvTEM5SGdqaEJZN0YwRDIwaUFFNzJESVlrLXp2U3ZGOHo2N0ExTG1mUnVmaEM4Mjd0bjk1QmlrbDlkbXdMYWprNDQ5UQ?oc=5) <sub>DM News</sub>
- 📰 2026-10-16 [小马智行（PONY.US）10月16日收盘报4.93美元/股，跌4.64%](https://news.google.com/rss/articles/CBMijAFBVV95cUxPRVhCTUhoZ2RaV2lBX216cFkwY3d2QzEwdldFeGk4YUY3dHpoSHZOc010bC12RnpKbENIUUdtc1ZnRVQ5X3BzdC1KS1lLRFU3YjhJTFhtRVVhejFmWDl0LU92eERGak05amdpTHV5UGpwaWpiaTdjQVBEaWVOUUljVkhwN0wyZWpmVTNuXw?oc=5) <sub>搜狐</sub>
- 📰 2026-10-16 [小马智行收跌4.64%，成交额1616.15万美元](https://news.google.com/rss/articles/CBMiggFBVV95cUxQLXJlb1Nrby1RN0RSVGotNEVRbG5VMVkzc2Z4WHFjT0lsVS1pVWh4YnNYdEVVZVZNdWVORm52REp0QkdjekRYZVVMdVNmWDhTZmQzT2R0cVlPU3F3MjFseVRhUjZRNGROWG9tVG5MX3g4THNYaTk3YVktbnlRUm9McWRB?oc=5) <sub>新浪网</sub>
- 📰 2026-10-16 [10月17日热门中概股多数下跌，台积电跌超2%\|纳斯达克中国金龙指数\|日月光半导体\|阿里巴巴股票\|WSP控股\|满帮公司](https://news.google.com/rss/articles/CBMiqgFBVV95cUxQeWd5MzdSWWtXMElkTlZKaUotbUxvOTNiNTl4bXpnXzg0ODhnWUFTcFVYUW12WS1iTFJIQnB6VjVYY25ndERNOEREb2lIN3hmNVF0MjhJbzdFUXNocV9WSTdYVUJKRnh1Q3lNZ2xoUjJIbjdRU3lkSGFucTlPN0JZdDBkZU1Sa2JyR0JPWXlRYmRUVVdhN1otX1M2d2VVYlAxc2F6aUhod2RqUQ?oc=5) <sub>finance.sina.com.cn</sub>
- 📰 2026-10-16 [10月16日港股软件服务行业沽空数据盘点，腾讯控股、网易、智谱沽空金额位居行业前三-证券之星](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1xZ3RwUEVIdVl4bnhPZlhjZklkMG5tNUFSMmM2RW1fQW9VeXlFZGpRZVFTYWF0aWRCS2J6a0h3alFRWlRWdUc5a2lYYjNqaEpmaFBHZ05kR2EyZEVQdlE?oc=5) <sub>证券之星</sub>

</details>

<details><summary><b>WeRide</b> (146)</summary>

- 📰 2026-10-17 [【视频】10万级标配激光雷达，埃安N60把城市NOA打下来了？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE8wYWE2WjNCNmJzakV2TVVGSVdqdHNlME1MbllxclZrcVQtSHNPRGNlbllydnFMcTdyVzdJQTQ0MWRVUWllckhSOVg2Q2xVWFZWLXN3NWhzbkZScUU?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-17 [【视频】副驾零重力+按摩，埃安N60把舒适卷到10万级](https://news.google.com/rss/articles/CBMiW0FVX3lxTE41eHVOT3lqTmZpVnk4Zi0wb09ua2ZmTUt3VW1FZVNRVEtqV1NSVmU1N0FNM09peldPbDE3WHFTbVlGejRyUHI3N1B4dHhkRmNOeGJfdWQ5ZXR2WW8?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-16 [三部门调查尊界刹车踏板断裂，港股通汽车ETF易方达涨1.44%](https://news.google.com/rss/articles/CBMijAFBVV95cUxNdWZnbG9mRWZ1YjRNdTZFMnA5ZTh2Zy1JcHVEd2VWNlRvNWIybWtHR05ic1FDSlpOaG1LQ1pBdUV0aGllMTBlbFFBakRuMEJPOGU3a1pZQi1VNl8yQmVsU1puVDhUWFN0eU5OWF9wdlZLcTdIQnJnOFdvVG5kcWNJVC0yelpRZC1lRV9OYQ?oc=5) <sub>搜狐</sub>
- 📰 2026-10-16 [ADAS and self-driving levels explained, and where the US and UK stand](https://news.google.com/rss/articles/CBMilAFBVV95cUxQR1pLSC1zNlREQm1CNGtFRWtpUTAydEFqUTBXLWxiNDBpYzNJajlEOEgxak1FeGw3c0RmZTdjRUF6d1pzaEhxV25hbkd0cFdEUHJrYmZXRVo5dWFVeFFVenRwZ0o4M1FONFkzM1B2WmgycnllQ1M5QmtkaEtDWWpvT0hkYzhrd0NvT25zYzdHYWFZaER1?oc=5) <sub>Pasquale Pillitteri</sub>
- 📰 2026-10-16 [首搭华为全电线控制动续航最高700公里！埃安Ray7定档10月17日预售_热点推荐](https://news.google.com/rss/articles/CBMiYEFVX3lxTE1FSlVQMzZ1VjZ4cV9kZkNtNFhmQ2tXZUQ4c1NBLWFlVDYxTkxZaWszbGs4MHFYRjdLT2YzR2MxZm5IVTl1RHlSQUlHbXZtdnItVUlGc1JMUXRaYW5PTHhUYQ?oc=5) <sub>证券之星</sub>

</details>

<details><summary><b>Horizon Robotics</b> (157)</summary>

- 📰 2026-10-17 [合资纯电SUV高速智驾横评：ID.AURA T6、bZ5与EZ-60，谁才是长途出行的安心之选？](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5ad1I1c0tIV3ppLUh6UU5fOG55cjhxMkhyTWh6ak13VHFqNjlabG5tVVpvWnItX2lBLVRmdll2eWtINi1ra3E2YmQwWlBNM2g0ZGJBZHZBUHZoTEI0NTRZ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-16 [换的是算力，还是消费者的知情权？铂智3X芯片争议](https://news.google.com/rss/articles/CBMiW0FVX3lxTFA2bER3eTBpUzlhbVhtcDcwaGxLZ0NQcy1qNGt3N1dmQk4xWWxmS2Q4MWlEMXJKVVY3LUxoMVBpRUdqcjlHZmo3emwxcS1tV29wZDZYd0Vpb0liSzQ?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-16 [NOA杀到8万级市场，谁在「闷声赚钱」？](https://news.google.com/rss/articles/CBMijAFBVV95cUxOMVVPTlF4enJTaFhuVHo0TFZSREw3RDM5aDNIdG5WZ3kwMHJKeHotRFNFVXlBejYyMTM2dVZlQTNxczdsYm1WLXFYRWRqWmEzQW5EeXFEY05iWGFPTjhZRWJXc1czUlRIbzlXOFl4ODhOTTZSWTVwTHVoWEVKMkJhRUFMMlpxSHcxVTU4Vg?oc=5) <sub>搜狐</sub>
- 📰 2026-10-16 [大众与众07加装激光雷达，10万级卷智驾](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1aM3diNDNqc2lyQ2o5VkJ6dDFhVXRFQnQtcVBOV0VEUm1VYnlUNWt5ZUR5WkZvSDlTTS1qZk5IbWFpNHJtRDU4TE0wcldCb0RNeUlXbk9mTXNPd2c?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-16 [比亚迪智驾保有量超395万辆：数据规模是不是护城河？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9iWDhjdmxtRGYyaWVpdllKeE9rT1lySURnLU1PS1hrcklvX3UteHY4SXZVWWd5NFVBSno1TndSUVNTYTBoZnE4ejJiQ0NSN1FKbXRNN2QxSkwtZzg?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (32)</summary>

- 📰 2026-10-17 [赛力斯凤凰工厂制造 赛豆ME7申报：用上字节跳动豆包座舱](https://news.google.com/rss/articles/CBMiWEFVX3lxTE9ORjJMWl9TQjE4ejZYQ0V6SWEtY0dsOEF4dnBKYTJVakdxdEFaWlFlVHU4dUxCeUVjdkdEWkpBZGJMOG0yQlBJOVdOVWxqd1Z4Rmg3NlZCVzk?oc=5) <sub>驱动之家</sub>
- 📰 2026-10-17 [赛豆 ME7 落地凤凰工厂，新造车模式能否站稳 20 万级市场](https://news.google.com/rss/articles/CBMiiAFBVV95cUxOc3RJOWhnazVrNEpGSU82eERzY0VONHlMNmt4ZmRBX084MnprNzBQLTlWbUdlazJpdkVmclNQeS10LWl1VWhjeDR4UmNLNmx3STcyaXZwMlpTQVc1bDU3Rm5SRnNCbU5HVTdRNlU2WjV1emNPSUg1MzhCdlRMTUFZNWdxcXl4UDZi?oc=5) <sub>搜狐</sub>
- 📰 2026-10-16 [【视频】#卡泰驰二手车特斯拉YL](https://news.google.com/rss/articles/CBMiW0FVX3lxTE85eTFWS0xEY25USjY4aXFQRkhjZmZPVHhVeXQ5eHluRkphVFVORXJJaExYSkxrV3Nlc3lWZE9PUXRGdXRRMk5BZlZ4cTNMUFpuWklkNzdCNHRiRWM?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-16 [Volvo Extends Partnership with NVIDIA for New Automated Driving Technology](https://news.google.com/rss/articles/CBMirAFBVV95cUxOWExPaUZZQnhhR2U2eW5lMWdsVmtvb1VUT2o3Sll3anJoblVXcnRIM2Ywajdha3FlM0lBcl9ENUVRX09xQ3g5cVE1ckViOFdpeXFLanEzUzRyd1l2UDhKWnhTeDNlWjFPRnY4SkNJU1R3a2JQd3RCaTZrLXk0U0w5ZTRneXFFZ2lUd0l4WWtxRXpZNmRSYUpsRndlUk0wVDB4b09jOVhuZEwtTzk5?oc=5) <sub>Future Transport-News</sub>
- 📰 2026-10-15 [London Assembly Transport Committee Calls for Cap on Autonomous Vehicles](https://news.google.com/rss/articles/CBMiqgFBVV95cUxPMk5heTNKQnFWZnBNb1U4RVRzeTNZU0U4cWxlTG5WT1FoMG5scGhVazBoYU1lWW9wc0RUakJiNFhYcFJ0ZVprUDY4UXNyM1RZS3NsdkFyZTJtWHM1YzRrejZXMC13bkpVVy1seUZYa3h0YV9kM1FuMDVndlpNV0dmb282NWU0YUkwTEJwdU5FeWdtVElYYWhZZVFQTWZxWFF3ZHVneGl0RVBSQQ?oc=5) <sub>Future Transport-News</sub>

</details>

<details><summary><b>Mobileye</b> (16)</summary>

- 📰 2026-10-16 [Citi starts Mobileye at Buy, calls it a global leader in vehicle vision](https://news.google.com/rss/articles/CBMiygFBVV95cUxNVmg5SEZPdDZ4NWZyMThTZGVKc014ZTVwQ1VnQWQ1SzZ1MjhKQ2wwcTJPZUc1T253Y28zc1FHMXB4LXZNNnptQlJzUkEwLTJRN2xHOHd1WGl0TlNFYzZldlNkM2daRHJvUTNsSW80MDJBY1NDVi14cHF2ZDkyZDliZzNObWpxemN3YWE1M3VhZ3RPTW43LUZKaTBKSGpaaHRuOEtRV3h2TC0yd1pkZGtBZzYweHNBbVFLWjRscUxOY1FWN3BUTnZWajFn?oc=5) <sub>StreetInsider</sub>
- 📰 2026-10-15 [Innoviz Technologies Targets $8B Security, Defense Lidar Market at Conference](https://news.google.com/rss/articles/CBMi0gFBVV95cUxOWkhGNi1UZUFBdHJfUlgtdEFPZEliMXQ5azhkVHh2aGotMEhodUhDc0d6WmZjSmttZHhmSEdQY2ZDN0hzMDR0RVRQTW9QRzlqLUxWX1ZaejBDVVh2NzhZNkl5b1c0eUpTSzdNZWx3aElrZmo4T2JSdjVpdzZQdEVONVRCcUlDMmJLbHd5QXBzUnhkSjdRUWd2WHFZRlV0M0JkdG5nQUg0RWlwUzl2eXJUeUR2dWRGenVZVmtDVkFPT1lXcFFMY0JPVk1VRXVaZFhhNkE?oc=5) <sub>TradingView</sub>
- 📰 2026-10-15 [Zacks Industry Outlook Highlights Mobileye Global and Hesai Group](https://news.google.com/rss/articles/CBMivgFBVV95cUxNUndoTm0tSWlkQ1pyR3hUZ0VBd0U4N3R2U2RGV1pqbEQyd3hMYWhLdy1DMFllalpBZElrSFlWRThWUWxoQjF1ZXMtQ1FnYTFpdXQ5Y3VPUi03UldhUnVRdHI3R0Utd0lsSkQzOFlFSXBTeGFMdGwtSGRFaEw2UFc2VENzVDYwdV9vajNxcjZZRnZGSldqU1RvX21yenVwQnk0WkFEYm9qc0NCWEt0UU9QVGFOamhGZUlxNkwxZU53?oc=5) <sub>TradingView</sub>
- 📰 2026-10-15 [Becker Transactions Announces Availability of MagTrac’s Autonomous Vehicle Patents Focused on All-Weather Driving](https://news.google.com/rss/articles/CBMi-gFBVV95cUxOYjB0LUhhdmxDaFFxWm9HSk1LMjZvRVg5WGdNS011dzhWVnNPNDJCZ0twUUlHel9vbW1hR3ZKLUkxQzh5TjhHdjVhdXFodXQ1U0ZCT2t4QVU2bEhld2VLNTRDdVlpXzN0WnE4TmplWlp0MWJnczlaVXVoX09fREttNkJhaFlIbDZTMF9Pb1RfaG1jbUlzR29wcXhqNTNhY3dGUEFjTEJkSFJzaGlNZ0NjTkE0a0xyRExpellkSmxNV3BLV1lIYjMwcV9kc3pRSFp0M1BkRVVMUDVIWjBlZkFYZDJ2Q2xBY3pYajY1LVhpNjgyaUlRUUlaRk13?oc=5) <sub>Kitsap Sun</sub>
- 📰 2026-10-15 [An Israeli AI startup says it cracked a 38 year old graph theory bound for $2,000](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQS1RBR3FmbVZXTmFmdVF4cnBON094cVlGWHJBaTBSTlRIVlhEX25wREdVOWE5ckxxTEtTSTR0VTd0bXpVUHBCQzdQZzNCbTMzWk9XRXRQcjFqdnFVcEJWS0JJRWdDTDNwM3liS1NuR21pYmN5Y05ocklJc0p0NU9feGNXcC1nNTRCb1RPb0syQzhkbHRsN05sMWF4TDVMYzYweVo2UmY5YTkxUXc?oc=5) <sub>Startup Fortune</sub>

</details>

<details><summary><b>Aurora</b> (66)</summary>

- 📰 2026-10-17 [The Most Polite Trucker in America Is a Driverless 18-Wheeler](https://news.google.com/rss/articles/CBMifkFVX3lxTE93OW9admIyUlN5bFZhR01TY2d3S1J1a19qSDdpOEJONWtORnNBVm9rWGMyaEtXV05KRXBJTjZPWUNXOVFSSFA3R0tPTWhXQUdEaEhaVWFfMDFYMHNLT1M0dzFTclE3ZlVKdkhSZXp5dk1feXdUdXl2WnZNM0xQZw?oc=5) <sub>WSJ</sub>
- 📰 2026-10-16 [Who Is Legally Responsible When a Driverless Truck Causes Damage on the Road?](https://news.google.com/rss/articles/CBMinwFBVV95cUxPYXFFTnpDaTRjcDVTZ2VwYUVFUWV2dG1VOHZBMy1SZXdOaDhvRVp0UEpaMTFwRWg0VW56eUU2WG56Y01GNWhmcTM2T1hEZU9LV1Y0OS1PNmNPLVgtZFU2OXk2OHlBcXJtMHhzRzJSejBBcllJLWR2SmNxRDRIcGoyQkRpN2tkOWMtNkh0UWJYelBGMm51UEZsS1g4dmtrelk?oc=5) <sub>Freedom For All Americans</sub>
- 📰 2026-10-15 [Autonomous trucking needs smarter trailers, Charger Logistics says](https://news.google.com/rss/articles/CBMitAFBVV95cUxPVnpIU0d0VHQwTmJHRVc2eHJRWGNHaGdOMWtLYmJuQ0VKb2ctdl9hWm1ISGMyQ0xiMllEekxSeFNxNld1MjQ0Uk0yRXA2SjNJUFp2WS1EVUtabGhEU0dWQVJCMUNIUi1uR01fc3g4dmFDRmpQa3Z6ZlcxSkl0aUJZdGRCRVZZWnNlUUFwRjg1WTlOeE5ZUmY3V3o0dVVBVlQxTVpGcm1hSHU0S2hybkRqUElHa2I?oc=5) <sub>Truck News</sub>
- 📰 2026-10-15 [See which Pittsburgh companies made Time Magazine's best inventions list](https://news.google.com/rss/articles/CBMilgFBVV95cUxOa2pITl95ZmYtRzMyRXdISGlMRjkwVDc3U1pZZVZ1aTV1bmFBck9nWGNDTmR0VG1tY2F3RkNhb0N0MEdkN0xkU3NqMFVuZExNcjN6MFdQRWpMdG1sVHRTZGs3ajhzeEhwMmFGeW1wcGpTVkc5b3V5VWJJTzl0NFpJZUZuTkd3TjEwcGJhM2w5Z0hoVjJmeVE?oc=5) <sub>The Business Journals</sub>
- 📰 2026-10-15 [FMCSA approves warning beacons for autonomous trucks](https://news.google.com/rss/articles/CBMicEFVX3lxTFBjNy0ycnEyZnNRazZuNXBIUE9QRk9iMElTY3c2Tk9aOTZVRzd5ZHBSMEl3X2NPOFZrcVpHNDJrVXA4cXdHdXM3eXlIQ0hzajlTbFJ5aUZZd3N0VjVMZm8zUFVBZFMtUE00REEwZEpsc04?oc=5) <sub>Transport Topics</sub>

</details>

<details><summary><b>Zoox</b> (62)</summary>

- 📰 2026-10-16 [Zoox Leases Two More Hayward Warehouses for Robotaxis](https://news.google.com/rss/articles/CBMiogFBVV95cUxNS3hoQXBUa01acFRaQjRYMWNxOENEYllhV3EtcnFBNjBLUmFtLW9qRlU4WE9GVEhXblJlNmhoY3hkNFRKclZ1X3lHUXFpUV9Cc2lnbHFsQ2YzX2RSQXJ1d0xra3pnRy1YbEp2eW5ON0xqYXB4aWJEaUIzZDVGU1BTUm5ERmNrZVdTUTlJZ0ZOckJfZUJhTVdGRjQ5YkRhNTFYOFE?oc=5) <sub>Hoodline</sub>
- 📰 2026-10-16 [Zoox doubles down in Hayward with 350K sf industrial lease amid robotaxi battle for market share](https://news.google.com/rss/articles/CBMirAFBVV95cUxOczJCSGJUd2Q2TG0tM2MtY2JUblZodnc5WVV4NGxCWnhuSFpaYVRwcjdfN09CTXlFS0llRy1CVmVkZnBiRUxqVGluY1YwVGhWb2pocWdncS12ZnV3NHR5OGNkQkhqWl9qUGY5OGF5eHFxSjByWUJNQW9rNlRjenNhdHYyN29LMWpRNXZTRlE0TDc3VVJFXzBwRFRyc3lwWDUydkx4X2ltRGdMS2lt?oc=5) <sub>The Real Deal</sub>
- 📰 2026-10-16 [As Robotaxis Spread, Carmakers Must Choose Between Owning the Customer and Selling the Car](https://news.google.com/rss/articles/CBMilwFBVV95cUxNc2Y4S25PZUdJMVcwWkZKYWV2cG1tR0ltRUI1NmZyVG1xbVEyX2dIN1dWMzg0aG1zamtQMUpLbjlzQnhkMkxCRTNwTVVxNjFDckJKOFRhSDJYbHItS1pXa2FyRzFlWnMxbG9tTV9mMkVWekQyQ1JjVUZyS2hJaF9aNE00U0NCWDRRb3RGWUJLc1otM1VSZ3A0?oc=5) <sub>The Motley Fool</sub>
- 📰 2026-10-16 [Tesla Roadster — The Last Best Driver’s Car](https://news.google.com/rss/articles/CBMilwFBVV95cUxONzhwRjV4NlZ2czJyTVNwa0VzNnowd2lyZjF3d1h5YVRFTnhLckxlUWR5WU5DWEl2eUg4VnpyV0l0emdqNmtLanBvNWNpbzJtZmxON3N1UmRtckUteFdfa2g1amxhWnpSblZheXlSRTB5ak1RVHJpRUFfU0wyMndkYzh1WEo2SlRJN25feTJSckdmbjg1eG5N?oc=5) <sub>eletric-vehicles.com</sub>
- 📰 2026-10-15 [Tesla Robotaxi Tally Hits 739, Trails Waymo’s 1,185 [2026]](https://news.google.com/rss/articles/CBMid0FVX3lxTE5DeGxZSWQyTzdKUHBkUnFqV2Z2ODFsc2JwSHNxZ1psUGE5WHNNbmpWTzhYUlVSWkozRFM2aUZPTDl4SkpUdW1Ubm5LeWxULXRXY1cwdVRlTjRjWHdnRWhEQ3kzTVRvOXYwcmpFLXBnUlVmYlNMNnJR?oc=5) <sub>https://tech-insider.org/</sub>

</details>

<details><summary><b>Motional</b> (31)</summary>

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
