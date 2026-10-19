# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-10-19 · 1,289 papers tracked · 40 curated.

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
| [Teaching Vision-Language-Action Models What to See and Where to Look](https://arxiv.org/abs/2607.01658)<br><sub>Yuguang Yang, Canyu Chen, Zhewen Tan et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 34](https://github.com/ShivaTeam/DriveTeach-VLA) | Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving |
| [DeepSight: Long-Horizon World Modeling via Latent States Prediction for End-to-End Autonomous Driving](https://arxiv.org/abs/2605.10564)<br><sub>Lingjun Zhang, Changjie Wu, Linzhe Shi et al.</sub> | ICML 2026<br>2026-05<br>📑 2 | [⭐ 31](https://github.com/hotdogcheesewhite/DeepSight) | End-to-end autonomous driving systems are increasingly integrating Vision-Language Model (VLM) architectures, incorporating text reasoning or visual reasoning to enhance the robustness and accuracy of driving decisions |
| [SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving](https://arxiv.org/abs/2610.20609)<br><sub>Shaoyuan Xie, Zihan Zhang, Jingxuan Wang et al.</sub> | CoRL 2026<br>2026-10 | [⭐ 21](https://github.com/ASGuard-UCI/safedrive-vla) | Vision-Language-Action (VLA) models are gaining attention in autonomous driving, inheriting commonsense priors from large language models (LLMs) and widening the navigation interface from a fixed command set to free-form… |
| [CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving](https://arxiv.org/abs/2607.04179)<br><sub>Zhaohong Liu, Hao Ye, Xianlin Zhang et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 1](https://github.com/MICLAB-BUPT/CritiqueDriveVLM) | End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving |
| [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)<br><sub>Nan Yang, Zhanwen Liu, Linfeng Zhang et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 10](https://github.com/Zizzzzzzz/MVPruner) | Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings |
| [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)<br><sub>Yuan Gao, Wenting Miao, Mattia Piccinini et al.</sub> | IROS<br>2026-07<br>📑 1 | [⭐ 28](https://github.com/TUM-AVS/Chat2scenic) | Validating autonomous driving systems requires diverse, regulation-compliant test scenarios |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 10 | [⭐ 517](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
| [Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air](https://arxiv.org/abs/2605.31066)<br><sub>Tianle Zeng, Yanci Wen, Xueang Yu et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 1,116](https://github.com/louiszengCN/CarlaAir) | Recent aerial vision-language-action (VLA) models show promising single-UAV capabilities, such as tracking moving objects and navigating to language-specified landmarks |
| [GRAVA: Grounded Reasoning-to-Action Representation and Learning for Autonomous Driving](https://arxiv.org/abs/2609.15169)<br><sub>Xiao Liu, Haoyu Li, Jianghao Leng et al.</sub> | arXiv<br>2026-09 | [⭐ 262](https://github.com/AhernResearch/grava) | Driving vision-language-action (VLA) models increasingly reason before acting, but their intermediate reasoning is often weakly grounded in physical scene evidence and loosely connected to executable behavior |

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
| [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](https://arxiv.org/abs/2609.26792)<br><sub>Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.</sub> | CoRL 2026<br>2026-09<br>📑 1 | [⭐ 13](https://github.com/VAIL-UCLA/DreamStream) | Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions |
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
| [123D: Unifying Multi-Modal Autonomous Driving Data at Scale](https://arxiv.org/abs/2605.08084)<br><sub>Daniel Dauner, Valentin Charraut, Bastian Berle et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 403](https://github.com/kesai-labs/py123d) | The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics |

## Safety, Robustness & Evaluation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [CCFM: Collision-Constrained Flow Matching for Safety-Critical Scenario Generation](https://arxiv.org/abs/2607.04451)<br><sub>Ke Li, Kaidi Liang, Yuxin Ding et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 3](https://github.com/KELISBU/CCFM) | Evaluation of autonomous vehicle (AV) planners in safety-critical closed-loop simulation is essential for real-world deployment |
| [Lipschitz Optimization for Formal Verification of Homographies](https://arxiv.org/abs/2605.23203)<br><sub>Jean-Guillaume Durand, Panagiotis Kouvaros, Maxime Gariel et al.</sub> | CVPR 2026<br>2026-05 | [⭐ 2](https://github.com/jeangud/homography-verification) | The adoption of vision neural networks in regulated industries requires formal robustness guarantees, especially in safety-critical domains such as healthcare, autonomous vehicles, and aerospace |
| [CADET: A Modular Platform for Evaluating Distributed Cooperative Autonomy in Connected Autonomous Vehicles](https://arxiv.org/abs/2606.04072)<br><sub>Pragya Sharma, Brian Wang, Mani Srivastava</sub> | ICRA 2026<br>2026-06<br>📑 1 | [⭐ 0](https://github.com/nesl/cadet) | Deep learning models are increasingly central to autonomous vehicle (AV) pipelines, yet their integration has traditionally followed a monolithic design where perception, planning, and control execute on a single onboard… |

## 🏢 Industry Tracker

Latest 14 days of news, official blog posts and new open-source repos from tracked companies. Full daily feed in [`daily/`](daily/).

<details><summary><b>Waymo</b> (224)</summary>

- 📝 2026-10-16 [Hello Toronto! Waymo is En Route](https://waymo.com/blog/2026/10/waymo-in-toronto) <sub>official blog</sub>
- 📝 2026-10-08 [Sober Drivers Still Face Nearly 4x Nighttime Risk: Why Road Safety Demands a Safe System Approach](https://waymo.com/blog/2026/10/sober-driving-benchmarks) <sub>official blog</sub>
- 📰 2026-10-18 [Waymo is launching a campaign to teach people about self-driving cars](https://news.google.com/rss/articles/CBMiZkFVX3lxTE5mOFpQODM1VUVob2tIM1JpVnpMN1F2a2NaSDVkaUI3YngxT0dGRkxCOXo4NkdsTUJCRFNtZDBnaHJsbU00dmpkYnEyY0ZhZU1XVW9GQlFUeTNFU3o2ZXJpWkZ4b3h3Zw?oc=5) <sub>Mashable</sub>
- 📰 2026-10-18 [Waymo Announces First Canadian Robotaxi Service With Toronto Launch Planned for 2028](https://news.google.com/rss/articles/CBMixgFBVV95cUxQd0trRjdjaHFfT01XZ0RQTHRiWTJuUU8xZV9TTUVaUzh0U0NpV2cyUXJsdGxIUmJmLU1PY2dsRlZyRm9HZVlCWW14eE5BNDdwblVlR2tub1lXdld4QnVOZXAzNEZROVhQTEpEU3JLcVVlcE9odzlycnFzLURmREVuMlY4NWZuX3BOYlRuc1hXd1Q3VTlaNzFTbl94dTdIelowcFNxSG5KR2VacExGRHo1WUJ2U2ptb25KS1FfcHNKNHVRamNHUUE?oc=5) <sub>Rus Tourism News</sub>
- 📰 2026-10-18 [D.C. Mayoral Nominee Says District Should Not Rush Waymo Legislation](https://news.google.com/rss/articles/CBMiogFBVV95cUxOWHI4M1I1NnNzMFdqSHhibEpXT3p6VGd4b1NkRWp3bDFwall6dUhZbzFJLVhCZm84UV9scEhJbURvbGlodHNJTVpCS19BQV9UOHJ0bFdoc3BwdkNLWUZpMDBlTC05b19WZ01DR2JUd1VQU2ZaMVhaZ05GOW5kU3hSZ2VaRXExRWpXZDNWRlBSc2VzX25QdlZNNnd6YnF1czh0M0E?oc=5) <sub>The MoCo Show -</sub>

</details>

<details><summary><b>Tesla</b> (350)</summary>

- 📰 2026-10-19 [Tesla FSD Showroom Trials: 5 Details That Matter](https://news.google.com/rss/articles/CBMiigFBVV95cUxQQ0lIVGs4c0xHQWpqS1dYQ1h6NEJORldvZjY2ZmxLYUtEWC1KVXlxSjZBVkZMRHBDT01pekpJblB0cFdfVVg2U0ZqdE1SbmFmWWpXUkc2Z3M5TzZ2a2Y0MkRQN0tsdkdVSE9kRlI5UWh4MmhSSkE2QzdzOWRYYmJmZ3NiMjMxZ3NBZWc?oc=5) <sub>BASENOR - Tesla Accessories</sub>
- 📰 2026-10-19 [Tesla FSD and Autopilot: Features, HW3 vs AI4, and Subscriptions](https://news.google.com/rss/articles/CBMidEFVX3lxTE1Fa1Jpa0YzLUtUSXhXbkdzMTFVdlVmVWdWaU5VVXljMlNDcDBUQWFxc09pNFZpOXdDMU16ekRycjRFcUpkakpTWWZnY2RzcGQ5eUJlZ0FBc1RGaml6VnpuSTZwN3J5YWpESzgySThXbmZIWkQ0?oc=5) <sub>Drive Tesla Canada</sub>
- 📰 2026-10-18 [美国一男子打开特斯拉FSD后睡觉 撞上执勤警车致2名巡警重伤](https://news.google.com/rss/articles/CBMiWEFVX3lxTE1pZ25ndUI0a1dSbXJ6RzFkcko5aWlUNGlWZ1hDcHU2UTNSSF9HRDBGdjZTNDU5dHVxUDhxcmVGS1lSbC0xZ3BIaGVacG5XdkZGcWR4RzAwR1Q?oc=5) <sub>驱动之家</sub>
- 📰 2026-10-18 [【网通社快报】新款特斯拉Roadster将搭载受限版FSD](https://news.google.com/rss/articles/CBMiTEFVX3lxTE92cDYzNkVFaFhwdWVGblZRNlFSM3RIRmJQSEg1SlQ1SkhOUV8wRy1YZ0FxcHVxUkxDRWJsLWxvd1pReU8wczF3N3ZpNkI?oc=5) <sub>凤凰网汽车</sub>
- 📰 2026-10-18 [49ers' Kyle Shanahan plans to coach preseason opener, learned not to fully trust Tesla Autopilot](https://news.google.com/rss/articles/CBMilAFBVV95cUxQZUg3V2l6SUUxaXlTRDlINnd5c29VTEctOTIxZDJqeFduWV93X1A3MU43VzRUUElWX2dTWktNX2J2eV82cUo1Q01BVHNSVmZfNG9SYm00Z1MwWnk0WTJoQ1VMRE02a0EzZFdFREJvRUhUUmZRUUQ4U3lmLVhrVXFtV3FrNlpCQXhjRU5sbjBxV0hlTnBI?oc=5) <sub>49ers Webzone</sub>

</details>

<details><summary><b>NVIDIA</b> (233)</summary>

- 📰 2026-10-19 [Volvo Cars and Mercedes-Benz build next automated driving systems on NVIDIA technology](https://news.google.com/rss/articles/CBMi0wFBVV95cUxPLWVBZ3RmWDR5RHROcV8tNXJWT0xsX2luUVZCX1RkUDVkUEJuSHNlbXg2cWhDNjIyZF9yVk5zU0g1a1lXX3UydHZVQWprdGhGazc3TGRod3FSbUEwVTFnWEZ5ME1NVkZqVkV3X3VvX1ZmVlNheEFYbzVPeXk4anhBVUx1MWowY0FBRkJmY2JQMDhfVHh4N2lsZXF1WlRjOUFaNi1XRFNJVGtFckR5QW1nNWMwNzNTMUdSUlMtVU5qblBhOUoyVHFHeTVBalJ5TVk2clpj?oc=5) <sub>EV Infrastructure News</sub>
- 📰 2026-10-19 [Nvidia Shield Running Slow? Here's How To Speed It Up](https://news.google.com/rss/articles/CBMia0FVX3lxTFBaQjZnT0t6cmt1YlR6R3JGRlZRbWdlOEpKVzNKWmp6b1J2X010YUFYRENiSEMtajN4SEx5NTVlbDhDWHBrQmVLRUFZX24taUdHNnprQjh0V2huOFBmZGRER3BSeU55bkoyWm9r?oc=5) <sub>BGR</sub>
- 📰 2026-10-18 [Mercedes-Benz, NVIDIA Expand Automated Driving Partnership with AI-Powered Driving Systems](https://news.google.com/rss/articles/CBMi6gFBVV95cUxPZHFoTHVOTmNqVDhjZ1l0N1FTN1RTVHZoZXQwMFQyY0VlNVowb2liWm9ySXkzUEhwNDA5Wlh4X0R6dzlJQTc5cHJuTXhKTzJwNVdCVkVSYlpMSnBoLWRETzM1TlBtNjl6cU5YMHVBdEdSWUt3Qlo4MUlXTjNjVGpQT1dXd21NWEhkT1RubXgwdk1tVHJuUFRIdUxkWk5HN0pMYm8weTlLVUw5WTNsZGF1QWg3THhLYmdNZFhaeGpPTl9kRXlTbzd1RWlJLXNWdFdyMl9HLTNxOUI3Vm9KVmVBT0xmN1c1YXVBcVE?oc=5) <sub>The Fast Mode</sub>
- 📰 2026-10-18 [Mercedes Expands Nvidia Partnership on Autonomous Driving, Building Next-Gen OS With Level 4 and Robo-Limousines in Sight](https://news.google.com/rss/articles/CBMidkFVX3lxTFBTWFNJNUpkMUhuY05Ra1JGTEM4NEd1YXZDc3ZPRlN2eHQ4ZmJVRmpILS16dVpDYzg1ZTlmYXhuOURmeXpDdkhFV1dNeElLSWRwa1Z1M0VmWGVHaWlIM0drS3pHWFRna09QNzZ3TGFfYWtXamZMc0E?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-18 [Volvo Taps NVIDIA for Cars That Could Let Drivers Take Their Eyes Off the Road](https://news.google.com/rss/articles/CBMirAFBVV95cUxNb0NTenN0aEZuX19LRDV0RklTZU5TT0JuaTBDbEN6SVotVDFfVWl3WjJEanp4aUNqUlZEenpheEJuNzVDQTB4eUVRRjhsbWJJNWdUMkNURDZYQVVIcUFHTXR6a2JIaXowcHJ4SDI1VkQ2SDZ5MmNUMWY4a1lyUTBuMmZFeWV5SVlDa2l6V3pHd3lFcUhLWUVrNmlHcjVZTjN5dDFsbUJhbkNCNmhu?oc=5) <sub>Autoblog</sub>

</details>

<details><summary><b>Wayve</b> (65)</summary>

- 📰 2026-10-18 [ADCU stages protest against Uber driverless rollout outside Wayve headquarters](https://news.google.com/rss/articles/CBMisgFBVV95cUxNTXFiRkJLVmQ5REhuMjRLT0tlcGEyekR4TzlpaFJyS2pnSVlramJMOGdBZWRUMFFnRHk3STc0eWduUWlyVzJMb2FMeDVOUWVpLUI4dURnWTFwN2h0S0xJSi1Da1kybFpQREpPMDMtQmxubW9vQkU5SzlvenZmUEp6UG5NSzg4cm1XcDZyaXU3MnYwT3ZiaHFmMWRWcmxrMU9iODRvWnd2LTlUWms3a3l0MG53?oc=5) <sub>TaxiPoint Taxi News</sub>
- 📰 2026-10-18 [Drivers’ Union Protests Uber-Wayve Supervised Autonomous Rides in London](https://news.google.com/rss/articles/CBMimAFBVV95cUxOVEdrd3NDSnM0M3AtNVR3TE83b2ZRV015cXktdUs3NXdja3Y2ODI1N2xEYnd4U1lZQkZHLXp2THZZU1N0ZHZuckVOZWhwR0dfVXA0Z0JwekFBZU1ucGl3eUJwdy1WdHl6a0dHRFl2eGQwdVlKSFROUFNlQTRPQ2dzTzZ3SGR4MzRzZnFPNE5JM3A3dXdtR0libA?oc=5) <sub>DM News</sub>
- 📰 2026-10-18 [The Gap Between Autonomous Hype and Reality is Growing](https://news.google.com/rss/articles/CBMiO0FVX3lxTE9xdjBpQUdKZUowYjhpVlZwU20tUjNhN3hpQnFldWpfOV9tdUdaVkRObnR6VlY1eFlFdFU4?oc=5) <sub>Howl.link</sub>
- 📰 2026-10-17 [Protesters call for London robotaxi trials to stop](https://news.google.com/rss/articles/CBMiXkFVX3lxTE9LMjQ2Z1pqdXk3aWV2a3g0OUs1UTI4N1dwRS1Dd08xZ1QzejZrRWNkRkxvckFYdjZtWVhFZmRMR3BIUzJTRWxPSTZnaUsxanpqV2o1aExUbnJKNE9IWXc?oc=5) <sub>BBC</sub>
- 📰 2026-10-17 [Uber driver 'feels like an old car' joining protest against robotaxis](https://news.google.com/rss/articles/CBMihwFBVV95cUxNS1FhTkVpR2liY0FfUDh4eURDNlo3VkM0RVotb25rLU54MEpJamhxQUV1UTFiUDJvaWRmS2NyOUNWTld6Q2hRRTNvYVEwckp3ajAzR25tUVktQVlPa0l4ZHk3OGJVRnNYSTBoY2M5dC1pYk14QjljelZoaEUyaGRoakdmRGFxQzTSAYcBQVVfeXFMTUtRYU5FaUdpYmNBX1A4eHlEQzZaN1ZDNEVaLW9uay1OeDBKSWpocUFFdVExYlAyb2lkZktjcjlDVk5XekNoUUUzb2FRMHJKd2owM0dubVFZLUFZT2tJeGR5NzhiVUZzWEkwaGNjOXQtaWJNeEI5Y3pWaGhFMmhkaGpHZkRhcUM0?oc=5) <sub>My London</sub>

</details>

<details><summary><b>Momenta</b> (86)</summary>

- 📰 2026-10-19 [北京现代艾尼氪V拼了，能否撬动新能源车市场？](https://news.google.com/rss/articles/CBMijAFBVV95cUxNSEFPNHN0QW45Wl9JamgzcFNtMS00T1Z5anJsUEYwbU9ocF9HX19kSVJHQVhQWjEwY3oyR3g2djV0blFCckZpR2VXcUktRXllYnFTYXVXU1p5YXlyNUZmMWZyNjhka0pHbkFuU1JucFlWVV9fcEhEVS1VNE1wR2RVbGpqM1AwQWVIYzZMTw?oc=5) <sub>搜狐</sub>
- 📰 2026-10-18 [智驾好的车推荐哪几款？2026实测榜单+分人群选购指南+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE96Z3RxWEQ4YXpPMTY0NUlhbkprcmhYaWlqLXMzZzFvenBkSlo5RTdHMllqdzczRy03V2JLOGJFODBtM2tWUGdYZWdsT0NOS3hpbXBUNzFibjlXc2pvR0NpajE4WU9DdDZCUjB3OFJmc3JfZw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-18 [奔驰迈巴赫S450值得买吗？3个维度说清智能、设计、动力+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFA0MUl1ZkpVclprS29HbnRSWXA1THQ2a1AxenFGdThPMTU3NWdxeFpRaHVScU9SVFNreHJwREx2T3R4WEE5T0dhWk5WRGdGY0pNTmFubEpQUl9tT0RDYnB5dDAyNEI4TFFRV2lBWGtNYjlsQQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-18 [丰田铂智3X纯电车值得买吗？13个月销冠背后的3个真相+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE4zUXRvWkZhR1pNLUtvbk5aYWhTR1BHYlZFWExpOWRybF9hWXdYV19CSVpqU0htLW1iWHNucjRjeEdkNnEyUG1FRDNoY05tRUZJRkhFbmo4OURPZVZPWGpLSVloZ3l4Q2NEM05xUmRwQ3hvUQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-18 [日产NX8测评视频怎么选？实测650km续航+智驾零接管，15万级SUV真香还是翻车？+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE1fVkhHUkprbE5yaTI0Uzg1Q1JXYnJsUGE1YzMtTmo2RmRRZlZDN1NzUzBGTHlXLU1aa2ltS01ZSVRxSi0zcXVadGZndWFHWlE5aDFCdjdkc0VJRHZPR1JWa3RWTjVPX0NkcFhVX2pfR2JLZw?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>XPeng</b> (313)</summary>

- 📰 2026-10-19 [XPeng promises a new in-car app experience powered by Google Play - ArenaEV](https://news.google.com/rss/articles/CBMioAFBVV95cUxNV1hlYldPTXI0ckg2WXExVWQwU3RaUFRwOTB2T3JwN0RCYm1fakZDVVNGX3BaVjFhdG84Z0dLRU4yeV8xS0NtNW55Y0RNckFHVTI4OGRDSHNhOFBWbnFad0N2dXBLRnVqMkZxMjFGVE14TTA5U1BXZk82RGgxMUpzdzUtdFBQSV9WNFFtU2hNa21Rdm9FdmdsRVhwbTV1M01M0gGgAUFVX3lxTE1XWGViV09NcjRySDZZcTFVZDBTdFpQVHA5MHZPcnA3REJibV9qRkNVU0ZfcFpWMWF0bzhnR0tFTjJ5XzFLQ201bnljRE1yQUdVMjg4ZENIc2E4UFZucVp3Q3Z1cEtGdWoyRnEyMUZUTXhNMDlTUFdmTzZEaDExSnN3NS10UFBJX1Y0UW1TaE1rbVF2b0V2Z2xFWHBtNXUzTUw?oc=5) <sub>ArenaEV</sub>
- 📰 2026-10-19 [Chinese EVs achieve five-star ANCAP ratings](https://news.google.com/rss/articles/CBMijwFBVV95cUxQVnFVcXducDVmaGd0aGxkUEZ2ckRsb2oyM0E2c1Jhd0RMMndzdkNFLXY3QXQ1dTRka1VwVjJmeVlFT2lUdVlYUndSc18tZU9YeERMb1dzb0hUbEhhNE9JelNvVGdWMEJ6Y0hUcEYyUzNSQ01fdXFFYjBzTWxSQXBnVXNMMXdNdEJKWldsRUxoSQ?oc=5) <sub>Paint & Panel</sub>
- 📰 2026-10-19 [25万级大五座SUV盘点，小鹏G9L凭什么以“黄金大五座”入局？+FA](https://news.google.com/rss/articles/CBMiX0FVX3lxTE01ZFVXSmJ6cnlXZklDUXZVbHA3cW5abkFwd3pRbXY4LV9hY3ZrVXJNVTU4MU8wVC1pdGl4RTU1RnNhSjd1b0JkRDNMbUtpRG5qSjQ1V25MMGt1Qm1lakNz?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-19 [双腔空悬+后轮转向：小鹏G9L与4款大五座SUV操控横评+避坑指南\|操控不错\|小鹏G9\|纯电\|空气悬架\|SUV_新浪新闻](https://news.google.com/rss/articles/CBMiX0FVX3lxTE42czY4TTdNWFdzWXJtakVfcFVpZTY5ZUduclJkOEdQRG1xYUl0MzFxdVV0MUFfaUVpMHpnOEJpVTNrYTYzd2JyOGVaUk9uWWhVWXNVWVM4MVh2S1YyZW1B?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-19 [小鹏G9L对比极氪7X、理想L6、智界R7，补能速度谁更快](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBvM3pFNEotUXFfRm44a3I1N2lXWEFBSTFRb3RZQmE5SnZQU1AzSHI1RHV6SXZLaXlsdTdRN180TW9ySkoyeWdTVkl0MkViWWxoQmF2ai1jSmt5X28zRlVV?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>Li Auto</b> (153)</summary>

- 📰 2026-10-19 [理想L6目前价位多少？24.98万起值得买吗？3个维度说清+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE4xOHRCeEFhQ2plZm5XWjZyR2lDcHNXNUJqNkFwWmhSU2tGYk0yTXY2bllMS2tHYTRvTXZoekItaG4xZ1FHVmNKUmZEdUx6WkhzdVpXMkY5X21scU5xWXo3NENwb2oteTQ2bXlPSmNMTTg1Zw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-19 [理想智驾迎来技术大牛：原华为ADS核心成员杨旭光被曝入职](https://news.google.com/rss/articles/CBMiWEFVX3lxTE9LYnB4cF9KU2JpendYLW12SDNETzE4RkNoTUxJQ0paSDJjd2tlYXNRYUFDTTMwNE1zeWMwYnFmR2NXTFBubGlodURJdXgtamlVREN6eFNUNWw?oc=5) <sub>驱动之家</sub>
- 📰 2026-10-19 [新上市的豪华插混SUV哪款值得买？凯迪拉克全新XT5 PHEV与热门车型横评+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFBoQTZaV2RvZEhnYzRSdTZFTzZzTF9TcGNMM0xOVUdtQ3JNZEstdlg2aUdmbEh0NERmMEJ6RUR3ODVxSFFRUDV3SElsQjZtUHFva1dGTVJETDQ1RmpPOFMyeGRacDc4TVFOOFdneEJ0cm5UZw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-18 [Is Li Auto (LI) Undervalued As Its Chip Unit Secures RMB1.625b In New Funding?](https://news.google.com/rss/articles/CBMixAFBVV95cUxNNDc5ZEhFb244aXBQVW96bEpUazBBNC14UG14MGJNenl2RTVoYmlBZVNkVWJ2ZVcwcmJwbzUyeXFpZzVXZlFDVkxMeEJncDlENUx3TWZjY1JqM0FZZW1qZ1ZYZGNEMTlmeDBGME8wV05kN1phUUlHUUxBUF9rOUdtaDFyVGlEZ0Y5aHRJaW03ZFhkekhwU19zS0JmOWlKNS1GQkNtVzlmeWZhRHhIMXVoWEdwUjhTMDBiVEhlRzRLVWxnT3Rf0gHKAUFVX3lxTE1VLTZyV0VkTVQ2cktlV21KLXVyMzk2MWpNUWZZVGZNcHlrLUk2bS1kdU1EVDlpQ1pZeHh4UlNBYlZZWFhPd2xtUjZRdVF4YWFkc2JxcVJWbE9IelZGWElybE10d2pwOC1GWlhWSVlOd3JiQWJVRTNST0hxMFplbVhHWmtlbkk3aXFXWG1JN0lGUlFfbVo2NG0za3oyLXBuZl8zUDNXWkxWM2tTUUtKc2lha19WUWVaWUt3SDROQ0d2YWp4QlIzaWt3U0E?oc=5) <sub>Simply Wall Street</sub>
- 📰 2026-10-18 [World Insights: LatAm journalists explore drivers of China's NEV industry](https://news.google.com/rss/articles/CBMifEFVX3lxTE1LWUtfWktDaFZQcXM3RmRfZ2FwYV9zWmN6SG45MzFlZ1R4cUt0WE9MWmlRSVdhZy1jXzhGT1lLVV9DSDR6c3NWQ1EtRk5GbW5zcEVNTnV4d3BoUXBpa3JzRkZJMzl4TWNRSnRxaDFvcUQtaE45WkJrY283Qzk?oc=5) <sub>Xinhua</sub>

</details>

<details><summary><b>NIO</b> (153)</summary>

- 📰 2026-10-18 [蔚来ES6 2026款33.8万起，5年换电老车主说真话：值不值？+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE1adzhQX3pmbGRjNnVZWVBoS3dCeHd1U2R3RU9iaXdHNFd3SlFTdlkwRjBQcUdpTU5nSlR5RC1BaXlaMFNnaXVzdWlRMnltXzVvdjVCUm1DNkFncFFIeElNZTVGS0NtQ3N2SUVPRlZXaU12UQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-18 [Even if those new Chinese EV automakers dare to sell their technology, who on earth would dare to buy it?](https://news.google.com/rss/articles/CBMiU0FVX3lxTFBNOWhGbmhlR0MwS3dEbkFTUzN1azJGMUFMbW1vc3JPclRoLVlPck1pSkpUbEJOTE1pdDhGd1VUQjd5NVl1VFNpaFoyUlQtSUpNWU1j?oc=5) <sub>36Kr</sub>
- 📰 2026-10-18 [Taisei (TSE:1801) Wins MLIT Autonomous Logistics Trial, Is The Valuation Too Cheap?](https://news.google.com/rss/articles/CBMizwFBVV95cUxNSkZKYl9wTnV6elNhUktud0hzb0Vrb0wzZVV4bXpkdnZCa0cwcWJXUnNtNmVwMkpzMUxKdzBkZThZanBJN1dfVWxRcVAzTXA2aUl6Umg0V0ZjQnczam1HazRkd09iMGxDak1rVTJlQll5QVgxQnBKMGd5NFRuRl8wOXY5RzBidUxfOE80bGhxNHZwc1VMb0Y5WGpwLTBwLXBMQ202ZHRSUlpwSzkzdURDakpVTWMzRUtRdGUyam0xa1NjWlk2SnZhUFVuQlgtc1nSAdQBQVVfeXFMUDRuYThBRTVpM0h4a1NIZHVZSDhfTGVzSl9pTVp0Y2g5RXUtckNFeE5QYXZQYmQ3YUE1LWFOdnNMRi1waV8wTWVKNDlGXzNHbldMak1WRi1JNW5MYTRjalhqZTc0dmpQR2FrLXlKR2pRb2pqU285QmJveWZhaDFBNWhaQTU4UUVqWmp6aHRxTWRadUtvTnh0Z0xDbVMzQ1VINmFnd1VZcGRlYXB4MkZMeDZaV2QwZkdCN3liOW1MQzFsRFZkbmlUQVNWMVFBa0FPMV9qOVg?oc=5) <sub>Simply Wall Street</sub>
- 📰 2026-10-18 [蔚来ES9和问界M9 Ultimate怎么选？6大维度对比+FAQ](https://news.google.com/rss/articles/CBMiakFVX3lxTE1vb0QyUTZWaGpWamwxNG5Kc2xKeF9MaTBLQ3RObmRhbTJtOVhZTl9PQmJIdWlBMXpSRzBPVTg4U2pzRmNnOXFaV0ptU1FWY0pUN3FsV3RfMjR1ai01UW9UaC02LWZFazdINkE?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-18 [30-40万新能源怎么选不踩坑？按这3个维度买就对了+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE5rQXRKTENCa216VFA5NWJUdFFmaHJQUnNmZzRLM1dGYW9iYzBPUTV1MDNMYVdGVGRIM0tmM0N4LUZmYmdLQmNCV2pMdVhGam9pS0ZUcl9FRHFGS25Gb0JBQ3U4QmF3UnN4UWtTZzJ4VzNBQQ?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>Huawei</b> (352)</summary>

- 📰 2026-10-19 [Spyware Infection Just by Displaying Ads: New Attack Method "AdFection" Reported](https://news.google.com/rss/articles/CBMiWEFVX3lxTE8xTFExRTFyUk9wNHZCYVNrUTk3QmtzQUN5R2JNUjU5VV9Pc1NpRzR3aWtWS0RSTTRIOXByQjhPUlE4eDRLb3JTeW10bWtjd0JsM3Z1OGVGOWU?oc=5) <sub>ASCII.jp</sub>
- 📰 2026-10-19 [奥迪A6L e-tron搭载华为乾崑智驾，续航快充兼备](https://news.google.com/rss/articles/CBMigAFBVV95cUxQT1B6dWdTSG9JM1FZMW1WNDFCRXBZMXhYX0I0N04tRUF6VlB1S1pFcnMycExjYXVKXzUtaVBpUmxDUGMzaFU2ZUhDN2ptam9Remh2WFAwTnFLbGJGNEtDS2hXRUxMOTE3SzZPLTBwQ2VneWxfelMzQlVyekV2cy0tOQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-19 [【视频】2027款纵横G700动态体验华为乾崑智驾有多强](https://news.google.com/rss/articles/CBMiW0FVX3lxTE0zU3cySW9Ba2RQMXc2OXAwVnpHLV9wbFRLbU5jTFl3U1ZDVWZvZXduWnJLemFJMExtMk9yZVFBUi1qRGEyRXNrOThLWjFIUFd3WlQ4S3RwbkFQLTg?oc=5) <sub>车家号</sub>
- 📰 2026-10-19 [奥迪A6L降到28万还等新款吗？新旧两代怎么选，3个维度说清+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE12MGtqV2Z2LXhiLWNndmJ4dElYZFlQbWJoSkUzYWgxbFR6UUo2WXpJYk55RXVJQWRjd2Y2ZjdZZUVYdFFrVnJrZGRKLUtCS29wOExuZ1FDc3JTY1JyS2xBci1ER05PVnNhYTA5R2FoenBCdw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-19 [【视频】华境首批专营店开业：华境S全系标配ADS5，真六座SUV 到店实拍](https://news.google.com/rss/articles/CBMia0FVX3lxTE5sVDBNdmhQODdDMmpRUzl6VzB1ckc3SlpHdmFiYXp6UmdidUtiMHJvd1lCWEFJQ3lOWEZlLTFvVkJLMUVzUm1EYmgzMFdFSmlXeWtwc3NwNXIwUVR1SWRyb1FMWkd0OEtUWVl3?oc=5) <sub>车家号</sub>

</details>

<details><summary><b>Baidu Apollo</b> (53)</summary>

- 📰 2026-10-18 [Seoul taxi overcharge complaints by foreigners top 6,000, few acted on](https://news.google.com/rss/articles/CBMiugFBVV95cUxQcEZXRHVkMXg5Sy1yNXNsZXNEWXo5X0hDemZkMERmYzM0ZkIzQ2I4bndEZWFRbjRGV3B1Z1BzNFRtT1NvbGJrSG9CTEltRGF3V3ZGcWhLakI0My1KVGNLcHU0YnRGNlpmbHVhcWg1ZWtxOXl2LUR0ZmFGUlgxWkdWM2gzcXdTYS1hT182R0ZSZ2hFOUlIVVU3b2FlVGx2WG5wZTJFZTlQaEdRN28tc0p3MXZQRDdPM0Juemc?oc=5) <sub>Korea JoongAng Daily</sub>
- 📰 2026-10-18 [钰见雄安Vlog \|在雄安体验没有司机没有方向盘的车 你的出行，自动驾驶来接管](https://news.google.com/rss/articles/CBMif0FVX3lxTE4zMXFWSUZQSVB4TGhtXzRweXdJbmpKY1JnR1dVVG1YLUt6bUhXTXViMmhEcGNuMmpSbHdFdVFRbkNnclV4QnJ6Qk9GbmdmX19NeHVfZG0yTzBpMHYtekY2NjZNSlFNYVV3aENaVWFqUEV5bHNOT2dDcFRDVWdSdHM?oc=5) <sub>新浪网</sub>
- 📰 2026-10-18 [The Gap Between Autonomous Hype and Reality is Growing](https://news.google.com/rss/articles/CBMiO0FVX3lxTE9xdjBpQUdKZUowYjhpVlZwU20tUjNhN3hpQnFldWpfOV9tdUdaVkRObnR6VlY1eFlFdFU4?oc=5) <sub>Howl.link</sub>
- 📰 2026-10-17 [Croatia Robotaxi Goes Driverless: Pony.ai Hardware, 22km [2026]](https://news.google.com/rss/articles/CBMigAFBVV95cUxPbXpWaW1YYXplbkJnTzFEYV9LVmpRT2lvY0dxMmNkakw4OWNJQzVNVFpQbW55SUFhT0lvUGNsaV8zY1VUdUhmem52LUtRZl85TXBDaFVDc0U1UGc3Rno1SnQ0Z3hwcDJlNEpWQ0hZV3lRT1lDTDAxbGpjUlhNWV93Yg?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-10-17 [科技早报 \| iPhone Duo首批现货最高涨7143元；长鑫科技预计前三季度净利超1300亿](https://news.google.com/rss/articles/CBMiWEFVX3lxTE84Q1BrQ3hBT3k2VmlQdmZtMDBXN0xvcUpkT252WElIRmNNVlQ3YktOYzlrTWdkT044ZWNkUXEzMnNkbGVfNnJWakp3WUFHYmFJdklyaHc1YkY?oc=5) <sub>Jiemian.com</sub>

</details>

<details><summary><b>Pony.ai</b> (145)</summary>

- 📰 2026-10-18 [New robo-taxi is sleek and slim compared to other 'monstrosities'](https://news.google.com/rss/articles/CBMicEFVX3lxTE1tMS0wZllmRm9ZMm5KYThvSV9PclNCd0xUS2J2cnUyODZUMFJDaHRmRkpWM2treG1XQkF4Q0lRT2k0M0JLYS1XM0w1cHh6a0NJMWFzUDlzeE9Bc1RTZWZUMl91emlrZHZaUE1CMVM3eGE?oc=5) <sub>Mashable</sub>
- 📰 2026-10-18 [Look, no hands: Euronews rode driverless in Europe's first robotaxi in Zagreb](https://news.google.com/rss/articles/CBMirwFBVV95cUxNZFdXZUg1TUZvWENYTnFUbGpKNzF4cExPWDJLMVdUUktQblN6ODBpY0F0QW5CajlPNDFxRWJJQkVjVFpiTTY1SEVVV1JET2h5NE9kYllobk5zQkZGM1pFSkdBNUc1bGdlSUlUYUh4ZnRybWFiWDhka0RzVFdJZlo5TVVWdW1wZjZ0VFdkUzE4czkwQ0EtcVpUX3UycWdKaWJGNXlBUC1hR1ZINjFjSWNr?oc=5) <sub>Euronews.com</sub>
- 📰 2026-10-18 [Uber Expands Driverless Taxi Push Across Europe After Zagreb Launch](https://news.google.com/rss/articles/CBMingFBVV95cUxQRDRqYmh4NlFZS2d1N3ByUS1oZExINXM5TGVYRnFXbVgzR1hCSk56VlZLbHdzaVoxcktqTUdTRHkzWkpGVnhYMHR0YVh5c09DSkZuRi1WYUNqamNqV1JSTzhLSWNBb3VvQ3pZSTRpaFptNFpxZFAzTV9SS282ZDE4MUZnb3p2UnpxMkt2eEtCZDA3WkpLLXlwZ24xc0kwQQ?oc=5) <sub>IndexBox</sub>
- 📰 2026-10-17 [正片发布！广东10年育出自动驾驶第一梯队](https://news.google.com/rss/articles/CBMib0FVX3lxTE8ybmgxd2pZM3JsWHVqejV0MHk1cjhjd2E5NWROUUNkaDd1X2h6dTM0WGRpa3hjUFZKemFnQVR2Nl9SZ29adUNDV1RBT2NlNXhRZ25vMWNqbG0tNFM2T3pQcV9lR3lWZWFHZ0k0cHFYYw?oc=5) <sub>新浪财经</sub>
- 📰 2026-10-17 [Croatia Robotaxi Goes Driverless: Pony.ai Hardware, 22km [2026]](https://news.google.com/rss/articles/CBMigAFBVV95cUxPbXpWaW1YYXplbkJnTzFEYV9LVmpRT2lvY0dxMmNkakw4OWNJQzVNVFpQbW55SUFhT0lvUGNsaV8zY1VUdUhmem52LUtRZl85TXBDaFVDc0U1UGc3Rno1SnQ0Z3hwcDJlNEpWQ0hZV3lRT1lDTDAxbGpjUlhNWV93Yg?oc=5) <sub>https://tech-insider.org/</sub>

</details>

<details><summary><b>WeRide</b> (156)</summary>

- 📰 2026-10-18 [埃安Ray7预售：12.88万起！45.58度电池能跑530公里！](https://news.google.com/rss/articles/CBMiW0FVX3lxTE54Vm1GMHhPdnVpZl9pMG51eVhhcjhFOU1qdXhPWFVWOWtkVHNiWWRfUHdMTTZiejUta0Nfd0ZGZExINTE2MXd3R3lHV3pSc0lUOUZjMEc1U1pCYXM?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-18 [埃安Ray7预售12.88万起，搭载L4同源智驾电耗9.7度](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9pS0U3czRMbUV1WjRhR1BTbHJEeDNMd1ltVG9ZVjJjaEZwSTJDck1IX0hUYS15MDM1Z2RCVGJUbmt2RC1Vc1gzRDNOVldtUndEUzlVVTJTYkRkQVk?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-18 [【视频】马自达CX-4行驶2.8万公里](https://news.google.com/rss/articles/CBMia0FVX3lxTE1lRkZyWmVZU2FtNmszSE5zelpWLWtPdmVRbmtDYnBnSDVieWNSaXA0YUdQeXIyMV9lNWVheDBsZUM4QzNKelM0V3draHhpZmZOazBkUVl4aWJwYlRjVEp6d2hXbF81SXZENDZZ?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-18 [广汽埃安Ray系列首款车型开启预售，2小时订单6817辆](https://news.google.com/rss/articles/CBMiZEFVX3lxTE9FQnlrVUt4eGd4U3BZQWJSRnpiN3dxbUJWT0NISDZXeTZyWGVwSk8tMzdXZG1hdjUwY3l5aklwUzhWQXgtNzdJZ3JtOGtxWlEwYlYzcVlxMmEtaFcyX2xaMjc4elA?oc=5) <sub>新京报</sub>
- 📰 2026-10-18 [预售12.88万起 AION Ray7开启预售 192线激光雷达/纯电续航702km](https://news.google.com/rss/articles/CBMiYEFVX3lxTE94Wmp0dUJpVTUzTVpxdlVjVzVmTThYbnp1OGl0VE9ZNWFrR2hSTFp3cFFsNGM4dWNkdE8ydDcwck1UZ29SRUo1TFBkTkpXS2RjaFFFY09VMHlsUjJhWW5rNA?oc=5) <sub>太平洋汽车</sub>

</details>

<details><summary><b>Horizon Robotics</b> (150)</summary>

- 📰 2026-10-18 [【视频】29万起配空悬+华为智驾！岚图泰山X8选购指南](https://news.google.com/rss/articles/CBMiakFVX3lxTE1OWi1iMzNETER3V21yX3hsUjJxaFhWSVZxb1JrbW93Z3JXa1lMbWJlLVR5OE1CMzRsZGlIbTVLTGdBSVVFU2w4blUzMlFaeWZOX296S1F1QXhya2gzclNKOWZSdGFtQUVMR0E?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-18 [搭载激光雷达的新能源SUV推荐：高阶智驾家用SUV怎么选](https://news.google.com/rss/articles/CBMia0FVX3lxTE1EM2pmNDNUQmpQd0xOdUw4RzRJSEdaNkk2V3NKaGF4UG1IYkt2dnQwVjJSMnp2U1BNeVo1S21HeWhGODhhMmFjemt2TEdwNUhYbXBRU2hlbkRnUnlib1JuTlZJQUFLdmhSVkRr?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-18 [【视频】越野也有智驾！老掌沟实测泰山X8纯电版ADS5 障碍物避让](https://news.google.com/rss/articles/CBMiW0FVX3lxTE8xUHFkNENFQ3JjWXZkY3NRYlczWmhwOTVCQzF6a0JSZmNXREUxelctTFk1eElicjJTY2VEUGNkNnp4eGdJcTRwczhYMnU4eE9oVDdaNzAxVTVydEk?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-18 [蔚来ES9和问界M9 Ultimate怎么选？6大维度对比+FAQ](https://news.google.com/rss/articles/CBMiakFVX3lxTE1vb0QyUTZWaGpWamwxNG5Kc2xKeF9MaTBLQ3RObmRhbTJtOVhZTl9PQmJIdWlBMXpSRzBPVTg4U2pzRmNnOXFaV0ptU1FWY0pUN3FsV3RfMjR1ai01UW9UaC02LWZFazdINkE?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-18 [10-30万预算哪款SUV有小蓝灯智驾辅助？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE96RTI1d29WWDFFbXcwd1JPQXBtVjhKeG9OVHlzZ2drNG52VHNLTV9UV3RjX1Q4VlJiRnNwVFJ0RFF0M0FObE1vZ2tkcWEzQU1odVRjd0RUS3YyYzg?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (29)</summary>

- 📰 2026-10-18 [金年体育平台官方：从“安装障碍”到“用户激增”，安装成功率提升至99%](https://news.google.com/rss/articles/CBMiV0FVX3lxTFBTSWxuOGdya2hsQ1FwSURIUWhUUV9RWjRoem5sQkJCMEwzM25nay1JU0xmM3NpcS1adUl2bG51RU13WmRWOEY1cEUwMnZLX0xxcnRiZlk0OA?oc=5) <sub>TGBUS</sub>
- 📰 2026-10-18 [工信部412批新车，赛豆ME7和方程豹钛9应该是关注度最高的了……赛豆M...](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1zUzU1RXBKR3pOMDJWSV9JajBMWThiSWsxNVVjZW1NblZHZVQwRUxqWHJjTnlBeFktWXVzdGdWSm92RXdHTW15T0RJZjk2YW1yNExsYXhqY3NSTlU?oc=5) <sub>车家号</sub>
- 📰 2026-10-17 [赛豆 ME7 落地凤凰工厂，新造车模式能否站稳 20 万级市场](https://news.google.com/rss/articles/CBMiiAFBVV95cUxOc3RJOWhnazVrNEpGSU82eERzY0VONHlMNmt4ZmRBX084MnprNzBQLTlWbUdlazJpdkVmclNQeS10LWl1VWhjeDR4UmNLNmx3STcyaXZwMlpTQVc1bDU3Rm5SRnNCbU5HVTdRNlU2WjV1emNPSUg1MzhCdlRMTUFZNWdxcXl4UDZi?oc=5) <sub>搜狐</sub>
- 📰 2026-10-17 [AI Cloud 100 China 2026榜单在沪发布物理AI企业成上榜主力\|具身智能\|上海市\|自动驾驶\|月之暗面\|阶跃星辰](https://news.google.com/rss/articles/CBMiwwFBVV95cUxQUDZQZFpKdThfMEhrWFBpNlJneDFNTEZfQjJLbFZUT005NjFva0tmSUd3cnZXVEZGNzlxUEg2aHVuN3pPQUV5SngtMlNIMWVMa1lNcTh6bmdWQnlnT0s5NzlFekFMS3UwSG56V3BmM2pQazVRbHpKUVlaYnZROVdoREU0ODRPU2FKaFRIZ19rMFZ6NU1qeXdEakVrWldzNFA3U3lPRTVVeGR4R1B6dGJmNzJFcWVlX0M3QUNqZks3OGJHdFU?oc=5) <sub>finance.sina.com.cn</sub>
- 📰 2026-10-17 [赛力斯凤凰工厂制造 赛豆ME7申报：用上字节跳动豆包座舱](https://news.google.com/rss/articles/CBMiWEFVX3lxTE9ORjJMWl9TQjE4ejZYQ0V6SWEtY0dsOEF4dnBKYTJVakdxdEFaWlFlVHU4dUxCeUVjdkdEWkpBZGJMOG0yQlBJOVdOVWxqd1Z4Rmg3NlZCVzk?oc=5) <sub>驱动之家</sub>

</details>

<details><summary><b>Mobileye</b> (15)</summary>

- 📰 2026-10-18 [Polestar 4 is an electric car that combines everything into one](https://news.google.com/rss/articles/CBMiUEFVX3lxTFB6eFU2TG1qczVlQ0dzbHAwOWF2MVZXNkFFYTJDemJVT2EzUFE0M1k5dnJDR2thNWNIM3c4cnR2c29HOUlTdGNlX2k1U1kzbk81?oc=5) <sub>Mashable</sub>
- 📰 2026-10-17 [Why Mobileye Global Fell Even As Sales Rose](https://news.google.com/rss/articles/CBMivAFBVV95cUxOblE2a0FORVFwdlBzb2t3bTJ4Z0w2YUpPVURicGRfMDlpdUNpWmowRzMwcDJPVEp6NXJZOXg3UXJEcTN2VVdHSkxXTGY4TmxVZmpZTk9QSmVOYVRzUDdJamo1bXF3aFdreUZGb19CWjVyQ2NqRHB2SWs4OEw2N2t0c21pZG9XMENUMEtMTVh4blRuMERqaUJHekQ3S0I5SFhxRU9LdXdyckEzamRmWDFqRnNROUowaUZweGl4aNIBwgFBVV95cUxPYjV5SndkRFlUM1EtOUtUWGVMOHNTNFYyYnZVU0Rfamg5SjJIbWtfcjJWY0ZoVHRVN3ljQlVkekNfY3I1NDlkbDBYNkx0UUhaU2N5OWk2cmpmZ3NYejZjQkI5T0Myenp6ZUN5Z3VoWVR4eDNGei1paGdvcUt5b3VPNEZleDZCZW55c3Zzb0FSYTU3S0M1MzZhdXEtNllTM1VSTWw1a0pWYm55aHBJUDU2OXZOd1A1Ql9INkNhVkgtR0cwdw?oc=5) <sub>Simply Wall Street</sub>
- 📰 2026-10-16 [Citi starts Mobileye at Buy, calls it a global leader in vehicle vision](https://news.google.com/rss/articles/CBMiygFBVV95cUxNVmg5SEZPdDZ4NWZyMThTZGVKc014ZTVwQ1VnQWQ1SzZ1MjhKQ2wwcTJPZUc1T253Y28zc1FHMXB4LXZNNnptQlJzUkEwLTJRN2xHOHd1WGl0TlNFYzZldlNkM2daRHJvUTNsSW80MDJBY1NDVi14cHF2ZDkyZDliZzNObWpxemN3YWE1M3VhZ3RPTW43LUZKaTBKSGpaaHRuOEtRV3h2TC0yd1pkZGtBZzYweHNBbVFLWjRscUxOY1FWN3BUTnZWajFn?oc=5) <sub>StreetInsider</sub>
- 📰 2026-10-15 [Innoviz Technologies Targets $8B Security, Defense Lidar Market at Conference](https://news.google.com/rss/articles/CBMi0gFBVV95cUxOWkhGNi1UZUFBdHJfUlgtdEFPZEliMXQ5azhkVHh2aGotMEhodUhDc0d6WmZjSmttZHhmSEdQY2ZDN0hzMDR0RVRQTW9QRzlqLUxWX1ZaejBDVVh2NzhZNkl5b1c0eUpTSzdNZWx3aElrZmo4T2JSdjVpdzZQdEVONVRCcUlDMmJLbHd5QXBzUnhkSjdRUWd2WHFZRlV0M0JkdG5nQUg0RWlwUzl2eXJUeUR2dWRGenVZVmtDVkFPT1lXcFFMY0JPVk1VRXVaZFhhNkE?oc=5) <sub>TradingView</sub>
- 📰 2026-10-15 [Zacks Industry Outlook Highlights Mobileye Global and Hesai Group](https://news.google.com/rss/articles/CBMivgFBVV95cUxNUndoTm0tSWlkQ1pyR3hUZ0VBd0U4N3R2U2RGV1pqbEQyd3hMYWhLdy1DMFllalpBZElrSFlWRThWUWxoQjF1ZXMtQ1FnYTFpdXQ5Y3VPUi03UldhUnVRdHI3R0Utd0lsSkQzOFlFSXBTeGFMdGwtSGRFaEw2UFc2VENzVDYwdV9vajNxcjZZRnZGSldqU1RvX21yenVwQnk0WkFEYm9qc0NCWEt0UU9QVGFOamhGZUlxNkwxZU53?oc=5) <sub>TradingView</sub>

</details>

<details><summary><b>Aurora</b> (66)</summary>

- 📰 2026-10-18 [Aurora Innovation (AUR) Wins A 5 Year US Waiver, Is It 60% Undervalued?](https://news.google.com/rss/articles/CBMi1gFBVV95cUxNZUY3dFlETjNKYmxFRWVKLURRTjlfVDVLVWliNjJrcXpjWXFxTklncXpNYWwyM0xfYjBaNFpBOHlaX0I4eFNJMF9WZWNCR2R0RWxfOTBhTGFfREtLd1JVOTJaLUVLTFJoY3hNTzExZFdaR3RDTnk0NGJBOGs2T1NyZ29yV2otempKQ2RzalppRHJ5TnhfV2JTdzBDTVM1T3AteTBmSHZldHRGMlRlc2ZfaEc0T0VOcnpOQnBwcExLUEUyRmVib1M5MFJVRkpWamkzU3l6Ui1n0gHWAUFVX3lxTE1lRjd0WUROM0pibEVFZUotRFFOOV9UNUtVaWI2MmtxemNZcXFOSWdxek1hbDIzTF9iMFo0WkE4eVpfQjh4U0kwX1ZlY0JHZHRFbF85MGFMYV9ES0t3UlU5MlotRUtMUmhjeE1PMTFkV1pHdENOeTQ0YkE4azZPU3Jnb3JXai16akpDZHNqWmlEcnlOeF9XYlN3MENNUzVPcC15MGZIdmV0dEYyVGVzZl9oRzRPRU5yek5CcHBwTEtQRTJGZWJvUzkwUlVGSlZqaTNTeXpSLWc?oc=5) <sub>Simply Wall Street</sub>
- 📰 2026-10-18 [Driverless 18-wheelers are hitting US roads. Are they ready for every emergency?](https://news.google.com/rss/articles/CBMi2wFBVV95cUxOeDhYbFlPYVdOaUhZZzBSWU93QUxWMmFPMzZpYUlxNzg1X3BIZWxsSFBEeUFoVkdaUlZDc0g3NUZXQ0VyMDlReWMwem1HbXhfU2FtbDFUT3MyLXRvSWZXWUp1X1ZnQXhpaXpvUWMyblhWeEdlYzl3Q0VBZkljR3d6LXFzSTBISEJiNTF3VlRRUTF0N0k0eTJVZVVLZ1dfUl9uaGdiUFdWVDJtcDZYY0hXalFZek9EMHd6MkxMM1Jpbmd4c1kxRnBYMVBKei0xUzlOSi1rQzhBaDltVTDSAdsBQVVfeXFMTng4WGxZT2FXTmlIWWcwUllPd0FMVjJhTzM2aWFJcTc4NV9wSGVsbEhQRHlBaFZHWlJWQ3NINzVGV0NFcjA5UXljMHptR214X1NhbWwxVE9zMi10b0lmV1lKdV9WZ0F4aWl6b1FjMm5YVnhHZWM5d0NFQWZJY0d3ei1xc0kwSEhCYjUxd1ZUUVExdDdJNHkyVWVVS2dXX1JfbmhnYlBXVlQybXA2WGNIV2pRWXpPRDB3ejJMTDNSaW5neHNZMUZwWDFQSnotMVM5Tkota0M4QWg5bVUw?oc=5) <sub>The Financial Express</sub>
- 📰 2026-10-17 [The Most Polite Trucker in America Is a Driverless 18-Wheeler](https://news.google.com/rss/articles/CBMifkFVX3lxTE93OW9admIyUlN5bFZhR01TY2d3S1J1a19qSDdpOEJONWtORnNBVm9rWGMyaEtXV05KRXBJTjZPWUNXOVFSSFA3R0tPTWhXQUdEaEhaVWFfMDFYMHNLT1M0dzFTclE3ZlVKdkhSZXp5dk1feXdUdXl2WnZNM0xQZw?oc=5) <sub>WSJ</sub>
- 📰 2026-10-16 [Who Is Legally Responsible When a Driverless Truck Causes Damage on the Road?](https://news.google.com/rss/articles/CBMinwFBVV95cUxPYXFFTnpDaTRjcDVTZ2VwYUVFUWV2dG1VOHZBMy1SZXdOaDhvRVp0UEpaMTFwRWg0VW56eUU2WG56Y01GNWhmcTM2T1hEZU9LV1Y0OS1PNmNPLVgtZFU2OXk2OHlBcXJtMHhzRzJSejBBcllJLWR2SmNxRDRIcGoyQkRpN2tkOWMtNkh0UWJYelBGMm51UEZsS1g4dmtrelk?oc=5) <sub>Freedom For All Americans</sub>
- 📰 2026-10-15 [Waabi, Warrior Logistics begin customer operations in Texas](https://news.google.com/rss/articles/CBMiaEFVX3lxTE9xc3hGT3NBWFFNeEJTbGJzdzN0U3l5VzNkWlJTcDdSY2hNaFRmZ0VJQ0FfdzUxRi05NW9EMlhIbXEyYlplWmVHeVh5ZHNFSmNWMkRvMzBYYzVIYWFPRTIydXpWcF9lZWtj?oc=5) <sub>Transport Topics</sub>

</details>

<details><summary><b>Zoox</b> (61)</summary>

- 📰 2026-10-18 [The Gap Between Autonomous Hype and Reality is Growing](https://news.google.com/rss/articles/CBMiO0FVX3lxTE9xdjBpQUdKZUowYjhpVlZwU20tUjNhN3hpQnFldWpfOV9tdUdaVkRObnR6VlY1eFlFdFU4?oc=5) <sub>Howl.link</sub>
- 📰 2026-10-18 [Tesla Expands Cybercab Fleet as Safety and Profit Risks Persist](https://news.google.com/rss/articles/CBMib0FVX3lxTE4zVEJoT3FUalAtcE1iSWxpY3hNQ2FTWnBTeENKblNHZ1dVZ2ZnUVZTLURwcDZoMzI5ZzFHTmJzRFh6ZlhSV1RvVU1jdnVPcFZXUWVOVi01Y3ZIVkh2NTZpWWZYampjd0hJT0VkLXpyOA?oc=5) <sub>SuaraGarut.ID</sub>
- 📰 2026-10-17 [Oakland can’t find footing in Bay Area comeback as R&D sales dip](https://news.google.com/rss/articles/CBMipAFBVV95cUxNY0JMQm5LdWk1S09rSVFWS0JSLVZac1RtWDJialB5VXV4MnZmeEdNS2FMMDF2ZlpOcGxhR2d0cmoxM2RFWmg5cDdPTHFkLTRBNUVPbGJNMTVNcnY2YXdKTUYyZDRtOXZvWWxLc2o0Q1RyeXl0VG4tU3JkTHVibGdQZll5bVRvNDlKQVpkNllaaHZINlVEd1luODhvakRqalhrNlNITw?oc=5) <sub>The Real Deal</sub>
- 📰 2026-10-16 [Tesla Roadster — The Last Best Driver’s Car](https://news.google.com/rss/articles/CBMilwFBVV95cUxONzhwRjV4NlZ2czJyTVNwa0VzNnowd2lyZjF3d1h5YVRFTnhLckxlUWR5WU5DWEl2eUg4VnpyV0l0emdqNmtLanBvNWNpbzJtZmxON3N1UmRtckUteFdfa2g1amxhWnpSblZheXlSRTB5ak1RVHJpRUFfU0wyMndkYzh1WEo2SlRJN25feTJSckdmbjg1eG5N?oc=5) <sub>eletric-vehicles.com</sub>
- 📰 2026-10-16 [As Robotaxis Spread, Carmakers Must Choose Between Owning the Customer and Selling the Car](https://news.google.com/rss/articles/CBMilwFBVV95cUxNc2Y4S25PZUdJMVcwWkZKYWV2cG1tR0ltRUI1NmZyVG1xbVEyX2dIN1dWMzg0aG1zamtQMUpLbjlzQnhkMkxCRTNwTVVxNjFDckJKOFRhSDJYbHItS1pXa2FyRzFlWnMxbG9tTV9mMkVWekQyQ1JjVUZyS2hJaF9aNE00U0NCWDRRb3RGWUJLc1otM1VSZ3A0?oc=5) <sub>The Motley Fool</sub>

</details>

<details><summary><b>Motional</b> (31)</summary>

- 📰 2026-10-18 [Hyundai Motor, Kia to Deploy Humanoids in Factories from 2032, Unveil 'Autonomous Operating Factory' Roadmap](https://news.google.com/rss/articles/CBMidkFVX3lxTE5BSkloNVFid1JrenR2b2g4a1N2OXI4SVNYQmRvMW5wc2lHS0Y5TVUzVlRJTjd0Wlo4UUFmWDA0U3hQTmFxOG9uSF9oOC1TMGs0cV9temVoeXhzUkx0Vzg3ZU5qNDJXRnJTb2l4VXg4U195Q2U3R0E?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-18 [Hyundai Motor moves to sidestep self-driving fallout in India](https://news.google.com/rss/articles/CBMiugFBVV95cUxNaXZ0YW55OGwzWnN4XzN4Y3YxeVpDQTJKOExNM1dmWkRSbUpjaUhhUUd5T084cnIxY3VSNzB6TzNSMjRreHJfN3l0VEt4b2VSM1lpanRUY3dDTmRNRWxBeVdwdlBCZGFMcWVHQkl5Yk9ReDgxbk14RTVmN0JNbU5RTWwyaVJ2ZTBRcU1Bc1BBai00eXNHMExxb0VkNEozUGl0dlZtT1BpWTN5M2dmbkZtZlI4ZEQxc3hibnfSAb8BQVVfeXFMTjY1OFZ6b3Z2S2lxd296ZHE0VTFpaHYzeU01bmZkSGJlSi1kbDRjWVJZLTl5VXhMVWRNVUxjeEg0aFdUWDg4Ukhhc2NYNkZ4dUlPQUFHeGtlRnB6QkotMDZYcXN3clRwZWduT1RndFg5WGZYWXlHQkZpUEZhb3NXNjlPYUZxRVVFcXlNTW1wWVYxUHhyWWFKbmJ3c1RsUk8xbnZmb2FIYW1EejBzWGdpNU5XT1R1dThfbDFaell0czg?oc=5) <sub>The Korea Times</sub>
- 📰 2026-10-18 [Hyundai Motor, Kia Unveil 'Autonomous Operating Factory' Roadmap with Humanoid Deployment by 2032](https://news.google.com/rss/articles/CBMidkFVX3lxTE5BSkloNVFid1JrenR2b2g4a1N2OXI4SVNYQmRvMW5wc2lHS0Y5TVUzVlRJTjd0Wlo4UUFmWDA0U3hQTmFxOG9uSF9oOC1TMGs0cV9temVoeXhzUkx0Vzg3ZU5qNDJXRnJTb2l4VXg4U195Q2U3R0E?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-17 [Grayson Brulte: Waymo Will Launch Driver-Out UK Service by Q1 2027 as London Permit Becomes 'the Keys'](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9VUjFlTTg4T2NGVlQ5dlIteGN1RVVNOWV1UTVCTEhGU3poT1FHOFN6VjB3VU5QX012ZEpaZ2RNNV9RNkRuV2hmQkxTY2EyN2FjanZhRVpPczBLWTg?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-14 [Hyundai’s two robotaxi plans take different routes](https://news.google.com/rss/articles/CBMikAFBVV95cUxQNWdFN1RBOWctNVVIZmRxemEzVEhrQ2MzVkN6YkJWME81bW41bFFqQVVDLTl4SEQ3OTYwalRQaFo0Q0xwaVR4M3FYOUZpMUV3OEJSTDktdHY4enVEdDgzY0xuV3lSa3hCTTAwdE93bkhoS2M5aHdxcmVkbEJIM1QteTlVbjhfTk9UUVBraW9GX2TSAZABQVVfeXFMUDVnRTdUQTlnLTVVSGZkcXphM1RIa0NjM1ZDemJCVjBPNW1uNWxRakFVQy05eEhENzk2MGpUUGhaNENMcGlUeDNxWDlGaTFFdzhCUkw5LXR2OHp1RHQ4M2NMbld5Umt4Qk0wMHRPd25IaEtjOWh3cXJlZGxCSDNULXk5VW44X05PVFFQa2lvRl9k?oc=5) <sub>ABC27</sub>

</details>

<details><summary><b>comma.ai</b> (4)</summary>

- 📰 2026-10-07 [Researchers Find that AI Models Struggle With Even The Most Basic Driving Skills](https://news.google.com/rss/articles/CBMiuwFBVV95cUxNb2ZGRGxGZDNjLWU1OVBPNjUtUlJXR0hiVGV3WEJ1eUVnSWExMWVvRmJjX2NtQm9sX0plMTU3YzZwUm5ZTzVoSGttcXZmQ3BqbW40X2doNFMycUk4UWE3anlidy1vWHNYZndVZjZWLUYtbnlHeVBFRjJOaTF4SWxzbmotR0xsNkVIcEhfZ0M3LUs5R2FyV1lVdlRRU3JwakpQcXpBUzlEOEhsWlB3Q19EdXFhQjRvZDU5MHln?oc=5) <sub>Auto Spies</sub>
- 📰 2026-10-07 [OpenAI's GPT-6 Astra is the only AI model to finish a real-world driving test in a Toyota Corolla](https://news.google.com/rss/articles/CBMifEFVX3lxTE9iZmN2ZFp6blVBRnZUTkYtYTJ3b0hSb0xhQjZyQXh5MUN2T3ladUlEb1F1SWJzc3FtamZtazk4LTVUWVpNX0ZjbGZwMnpERk45TVVQWVA1RjBZVUxxTTAzTWpaV1JqUzIwM1I2Wk1tTzc3bDJpaWluc2JVam4?oc=5) <sub>Crypto Briefing</sub>
- 📰 2026-10-06 [AI Agents Tried to Drive a Corolla, Crashing on 8 of 11 Runs](https://news.google.com/rss/articles/CBMiuAFBVV95cUxONWxQTEZham1kc1J4S2lMNUh6OTN1QWhXbl92U21NUWZTZWhNUUdwcFVvUHYtVWJzSjl4TjlCeFhUY2ppMXd3WkkxaHJFRmFlNUN2NGFSSENnV2ZZYWRNZ3JIUjd0dzFlTS0wR3gtbmxXN3VHOUkxWWg2VVFpTVgzWGN2T3RPdEFJV0cyWjRPSVFyNWZTYjFyX0pzYjFEUWQwLUlfbGo1bm8xVUZXQmpyQ3pCNXV5ZE9x?oc=5) <sub>thetruthaboutcars.com</sub>
- 📰 2026-10-05 [Researchers Discover ChatGPT Can Drive a Car. Grok, on the Other Hand…](https://news.google.com/rss/articles/CBMikgFBVV95cUxNNnNwX0g5bHV4STJlMXNOcXRnYnBHWHNoelViM2pJSzFob3dvUVJIdFlDRDV4X09DSVloZmxCTk5NODd3b3RBR2JmWEJQRktXUTYyWDNveS15UEw0NnVfSFluMlJxZHlBb3NhYnRNdDJsZ01MbVNpOXY4OW9nQnBSYnFRQ1U2YVd3a3R2ZTY4VlJNdw?oc=5) <sub>The Drive</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
