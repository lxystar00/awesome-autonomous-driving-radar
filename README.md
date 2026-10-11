# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-10-11 · 1,248 papers tracked · 38 curated.

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
- [Perception: BEV, Occupancy, 3D Detection, Mapping](#perception-bev-occupancy-3d-detection-mapping) (8)
- [Datasets & Benchmarks](#datasets--benchmarks) (2)
- [Safety, Robustness & Evaluation](#safety-robustness--evaluation) (3)
- [Industry Tracker](#-industry-tracker)

## VLA / VLM for Driving

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Teaching Vision-Language-Action Models What to See and Where to Look](https://arxiv.org/abs/2607.01658)<br><sub>Yuguang Yang, Canyu Chen, Zhewen Tan et al.</sub> | ECCV 2026<br>2026-07<br>📑 1 | [⭐ 33](https://github.com/ShivaTeam/DriveTeach-VLA) | Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving |
| [DeepSight: Long-Horizon World Modeling via Latent States Prediction for End-to-End Autonomous Driving](https://arxiv.org/abs/2605.10564)<br><sub>Lingjun Zhang, Changjie Wu, Linzhe Shi et al.</sub> | ICML 2026<br>2026-05<br>📑 1 | [⭐ 31](https://github.com/hotdogcheesewhite/DeepSight) | End-to-end autonomous driving systems are increasingly integrating Vision-Language Model (VLM) architectures, incorporating text reasoning or visual reasoning to enhance the robustness and accuracy of driving decisions |
| [CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving](https://arxiv.org/abs/2607.04179)<br><sub>Zhaohong Liu, Hao Ye, Xianlin Zhang et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 1](https://github.com/MICLAB-BUPT/CritiqueDriveVLM) | End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving |
| [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)<br><sub>Nan Yang, Zhanwen Liu, Linfeng Zhang et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 8](https://github.com/Zizzzzzzz/MVPruner) | Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings |
| [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)<br><sub>Yuan Gao, Wenting Miao, Mattia Piccinini et al.</sub> | IROS<br>2026-07<br>📑 1 | [⭐ 27](https://github.com/TUM-AVS/Chat2scenic) | Validating autonomous driving systems requires diverse, regulation-compliant test scenarios |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 9 | [⭐ 500](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
| [Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air](https://arxiv.org/abs/2605.31066)<br><sub>Tianle Zeng, Yanci Wen, Xueang Yu et al.</sub> | arXiv<br>2026-05<br>📑 2 | [⭐ 1,114](https://github.com/louiszengCN/CarlaAir) | Recent aerial vision-language-action (VLA) models show promising single-UAV capabilities, such as tracking moving objects and navigating to language-specified landmarks |

## World Models & Generative Simulation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [HERMES++: Toward a Unified Driving World Model for 3D Scene Understanding and Generation](https://arxiv.org/abs/2604.28196)<br><sub>Xin Zhou, Dingkang Liang, Xiwu Chen et al.</sub> | ICCV 2025<br>2026-04<br>📑 4 | [⭐ 72](https://github.com/H-EmbodVis/HERMESV2) | Driving world models serve as a pivotal technology for autonomous driving by simulating environmental dynamics |
| [FrozenDrive: Zero-Shot Text-Guided Driving Scene Generation and Data Augmentation with Parameter-Free Frozen Diffusion Model](https://arxiv.org/abs/2606.20110)<br><sub>Yuhwan Jeong, Hyeonseong Kim, Daehyun We et al.</sub> | ECCV 2026<br>2026-06<br>📑 1 | [⭐ 10](https://github.com/daehyunwe/FrozenDrive) | Synthetic data for autonomous driving is surging, powered by diffusion models that promise scalable scene generation |
| [MESSENGER: Memory-Enhanced Sequential Scene Flow Estimation via Autoregressive Next-Frame Forecasting](https://arxiv.org/abs/2610.10759)<br><sub>Jiuming Liu, Jianing Li, Mengmeng Liu et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 0](https://github.com/liujiuming123/Messenger) | Scene flow can capture low-level 3D motion displacements in dynamic scenarios |
| [ASTAD: Asymmetric Style Transfer for Synthetic-to-Real Adaptation in Autonomous Driving](https://arxiv.org/abs/2606.29286)<br><sub>Dingyi Yao, Xinqi Zhang, Lihui Peng et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 1](https://github.com/Dingyi-Yao/ASTAD) | Synthetic data mitigates the data scarcity problem in autonomous driving perception |
| [Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends](https://arxiv.org/abs/2606.01164)<br><sub>Jiuming Liu, Chaojun Ni, Mengmeng Liu et al.</sub> | arXiv<br>2026-06<br>📑 6 | [⭐ 242](https://github.com/liujiuming123/Awesome-Interactive-World-Model) | With rapid development of large language models and diffusion-based content generation, world modeling has attracted increasing research attention, benefiting various downstream domains such as game engines, embodied AI,… |
| [Is Your Driving World Model an All-Around Player?](https://arxiv.org/abs/2605.10858)<br><sub>Lingdong Kong, Ao Liang, Tianyi Yan et al.</sub> | arXiv<br>2026-05<br>📑 5 | [⭐ 256](https://github.com/worldbench/WorldLens) | Today's driving world models can generate remarkably realistic dash-cam videos, yet no single model excels universally |

## End-to-End Driving & Planning

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](https://arxiv.org/abs/2609.26792)<br><sub>Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.</sub> | CoRL 2026<br>2026-09<br>📑 1 | [⭐ 11](https://github.com/VAIL-UCLA/DreamStream) | Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions |
| [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)<br><sub>Shen Zheng, Anurag Ghosh, Gaurav Parmar et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 31](https://github.com/ShenZheng2000/WarpI2I) | Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs) |
| [G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance](https://arxiv.org/abs/2606.26017)<br><sub>Hang Yu, Ye Jin, Alessandro Canevaro et al.</sub> | IROS 2026<br>2026-06<br>📑 4 | [⭐ 6](https://github.com/HangYuu/G2DP) | In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors |
| [SUV: Future Scene Understanding as Video Generation for End-to-End Driving](https://arxiv.org/abs/2608.03084)<br><sub>Yibo Yuan, Jiacheng Fu, Jiangtong Zhu et al.</sub> | RA-L 2026<br>2026-08 | [⭐ 20](https://github.com/ASH-2046/SUV) | End-to-end driving requires a coherent understanding of future scenes, yet existing methods model these scenes using task-specific heads and output formats, with limited scalability |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 16 | [⭐ 345](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
| [Latent-Centroid Steering: Single-Pass Classifier-Free Guidance for Command-Aligned Autonomous Driving](https://arxiv.org/abs/2608.00237)<br><sub>Meibo Hu, Jiamian Wang, Pichao Wang et al.</sub> | IROS 2026<br>2026-08<br>📑 1 | [⭐ 2](https://github.com/codingmlinprocess/LCS) | Vision-language models (VLMs) have recently emerged as a promising paradigm for end-to-end autonomous driving, enabling agents to map multimodal inputs and high-level navigation instructions directly to executable trajec… |
| [DVGT-2: Vision-Geometry-Action Model for Autonomous Driving at Scale](https://arxiv.org/abs/2604.00813)<br><sub>Sicheng Zuo, Zixun Xie, Wenzhao Zheng et al.</sub> | arXiv<br>2026-04<br>📑 13 | [⭐ 367](https://github.com/wzzheng/DVGT) | End-to-end autonomous driving has evolved from the conventional paradigm based on sparse perception into vision-language-action (VLA) models, which focus on learning language descriptions as an auxiliary task to facilita… |
| [STAGE: STyle-controllable Action GEneration for personalized autonomous driving](https://arxiv.org/abs/2607.29517)<br><sub>Zihao Liu, Xing Liu, Yizhai Zhang et al.</sub> | RA-L<br>2026-07 | [⭐ 6](https://github.com/CarlDegio/STAGE) | Driving style refers to the behavioral preferences that drivers maintain during driving, shaped by their diverse experiences, habits, and needs, and is typically reflected in varying levels of aggressiveness |
| [A Survey on End-to-End Autonomous Driving Training from the Perspectives of Data, Strategy, and Platform](https://arxiv.org/abs/2610.00926)<br><sub>Chengkai Xu, Yiming Cui, Jiaqi Liu et al.</sub> | arXiv<br>2026-10<br>📑 5 | [⭐ 104](https://github.com/Jiaaqiliu/Awesome-Training-Ecosystem-for-E2E-AD) | Autonomous driving is a cornerstone technology for the future of intelligent transportation, where end-to-end learning has emerged as a transformative paradigm that directly maps multimodal sensory inputs to driving acti… |

## 3DGS / NeRF Reconstruction & Sensor Sim

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DriveWeaver: Point-Conditioned Video Inpainting for Controllable Vehicle Insertion in Autonomous Driving Simulation](https://arxiv.org/abs/2606.31918)<br><sub>Junzhe Jiang, Zipei Ma, Zijie Pan et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 16](https://github.com/LogosRoboticsGroup/DriveWeaver) | A pivotal step in autonomous driving simulation involves inserting foreground vehicles with predefined trajectories into simulated scenes |
| [Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796)<br><sub>Leshu Li, Jie Peng, Yang Zhao</sub> | ICRA<br>2026-06 | [⭐ 13](https://github.com/UMN-ZhaoLab/Pocket-SLAM) | 3D Gaussian Splatting (3DGS) has garnered significant attention in Simultaneous Localization and Mapping (SLAM) due to its advances in capturing fine-grained geometry features and synthesizing novel views |
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
| [Vernata: Self-Supervised Learning of LiDAR Point Representations](https://arxiv.org/abs/2608.06919)<br><sub>Oliver Lemke, Alexander Liniger, Abel Gawel et al.</sub> | IROS 2026<br>2026-08 | [⭐ 18](https://github.com/rai-opensource/vernata) | LiDAR serves as a primary sensing modality for robots operating in outdoor environments |
| [Towards Compact Autonomous Driving Perception with Balanced Learning and Multi-sensor Fusion](https://arxiv.org/abs/2606.02979)<br><sub>Oskar Natan, Jun Miura</sub> | arXiv<br>2026-06<br>📑 44 | [⭐ 9](https://github.com/oskarnatan/compact-perception) | We present a novel compact deep multi-task learning model to handle various autonomous driving perception tasks in one forward pass |

## Datasets & Benchmarks

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Towards All-Day Perception for Off-Road Driving: A Large-Scale Multispectral Dataset and Comprehensive Benchmark](https://arxiv.org/abs/2604.27499)<br><sub>Shuo Wang, Jilin Mei, Wenfei Guan et al.</sub> | RA-L 2026<br>2026-04 | [⭐ 6](https://github.com/wsnbws/IRON) | Off-road nighttime autonomous driving suffers from unreliable visible-light perception, making infrared modality crucial for accurate freespace detection |
| [123D: Unifying Multi-Modal Autonomous Driving Data at Scale](https://arxiv.org/abs/2605.08084)<br><sub>Daniel Dauner, Valentin Charraut, Bastian Berle et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 400](https://github.com/kesai-labs/py123d) | The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics |

## Safety, Robustness & Evaluation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [CCFM: Collision-Constrained Flow Matching for Safety-Critical Scenario Generation](https://arxiv.org/abs/2607.04451)<br><sub>Ke Li, Kaidi Liang, Yuxin Ding et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 3](https://github.com/KELISBU/CCFM) | Evaluation of autonomous vehicle (AV) planners in safety-critical closed-loop simulation is essential for real-world deployment |
| [Lipschitz Optimization for Formal Verification of Homographies](https://arxiv.org/abs/2605.23203)<br><sub>Jean-Guillaume Durand, Panagiotis Kouvaros, Maxime Gariel et al.</sub> | CVPR 2026<br>2026-05 | [⭐ 2](https://github.com/jeangud/homography-verification) | The adoption of vision neural networks in regulated industries requires formal robustness guarantees, especially in safety-critical domains such as healthcare, autonomous vehicles, and aerospace |
| [CADET: A Modular Platform for Evaluating Distributed Cooperative Autonomy in Connected Autonomous Vehicles](https://arxiv.org/abs/2606.04072)<br><sub>Pragya Sharma, Brian Wang, Mani Srivastava</sub> | ICRA 2026<br>2026-06<br>📑 1 | [⭐ 0](https://github.com/nesl/cadet) | Deep learning models are increasingly central to autonomous vehicle (AV) pipelines, yet their integration has traditionally followed a monolithic design where perception, planning, and control execute on a single onboard… |

## 🏢 Industry Tracker

Latest 14 days of news, official blog posts and new open-source repos from tracked companies. Full daily feed in [`daily/`](daily/).

<details><summary><b>Waymo</b> (214)</summary>

- 📝 2026-10-08 [Sober Drivers Still Face Nearly 4x Nighttime Risk: Why Road Safety Demands a Safe System Approach](https://waymo.com/blog/2026/10/sober-driving-benchmarks) <sub>official blog</sub>
- 📝 2026-10-08 [Waymo Closes $5 Billion Debt Financing to Accelerate Business Expansion](https://waymo.com/blog/2026/10/waymo-closes-5-billion-debt-financing) <sub>official blog</sub>
- 📰 2026-10-11 [Waymo Secures $5 Billion Loan—Its First—to Fuel Expansion Plans](https://news.google.com/rss/articles/CBMipwFBVV95cUxNY3A5ZURJVV95RmhHWlVrRTVFSUt3czI3M2pCNkhIUVYta3lzZWFLelQ3Mm5ZWXBIN3FPR2hjUXlUZW40SXN0anhoNUM1ZnhTSG5mYi1fbUNvaWNVUHRDUGpweVE0Q3FRZVQtNEF5NlZPUW9OQVhBQjd4TUNYbnd0cHVBZnVSbmZrMHE5VnBvRlotR2owODNKWmc4QjVCNzJBTEJTV3VoZw?oc=5) <sub>Inc.com</sub>
- 📰 2026-10-10 [Workers erupt over DC plan to bring robotaxis to city streets: ‘This is bulls---’](https://news.google.com/rss/articles/CBMioAFBVV95cUxNUUZ4dXZxSXBGNmZTMjdvTFFxb0xuN2hWa29Hbi14M0hPSk9wRUVmdDV1RlRCeU1kMHh5V005MUNHYkttYTk4SDJqTk5tVmZKMnR0bzEtUXh1ZXVBakR2LTdTX05tYXF5VEYyRWFqd3ZkT0o3dnBUQTFKaDhCNV9OMnYwSnktX3BIYW1HaXpHY0I2Uk9Jc1FncVVfOHpoRlMw0gGmAUFVX3lxTE5ETVpTb2dDaUxsUmw0Y1BaQk56SzhoSUNnUm5ERGhVZ0QwZjZOTGdPbGlVSnhncUYzTUhJVzdZNGFONTdwVGFFUzMwQ0lDV1ctT3l6aG1MdUczTkdvVktxeVZSaEhjVFZsT3MySkdKNlJ2aWwtOUF6bHdWNXlmZTZSZDQtYjV5UUJ2M0M4ZFdaT05FR3BxWTdsYmRqNkhHbEZIX3JJX3c?oc=5) <sub>Fox News</sub>
- 📰 2026-10-10 [Waymo's $5 Billion First-Ever Debt Raise Signals a Robotaxi Land Grab, Not a Science Project](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9BaGt6ckszSmpwTDVsOGUzQ29DXy0yc3BsVFdSTjNtZFZrR3dWYUd5TzcwSTYzUTE3MlVmd3B4UG1iSS1kRHpySXpFVlhRTWd3cjVCOUgwVW5FcWc?oc=5) <sub>BigGo Finance</sub>

</details>

<details><summary><b>Tesla</b> (348)</summary>

- 📰 2026-10-11 [Tesla Renames Full Self-Driving Package to Assisted Driving Across Europe](https://news.google.com/rss/articles/CBMinAFBVV95cUxPclJQMHpreE1IZ0l2cF9MRVhGZVlTc3pTMUhlZTZ5Nm9USkxSbzZ5NGhWal9qdHM1YnNkeFVsMkd6WVJ3WDQtU3QyUGlldDNsVnl5T25LQ0I2Q2RyUVQ0Nk81LUwyRGg5b3h0X3VGeGY5ZVY0M0tHamE0YkUtSXVCb1VrdktwLTlXQnZMaE5pbWlYd1NGYThNU1E1UzI?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-10-11 [Tesla Renames Full Self-Driving to Tesla Assisted Driving in Europe After German Regulator Talks](https://news.google.com/rss/articles/CBMiywFBVV95cUxOaXJtOGdwazNpQkFaU3NXOVU5STE0cWc2VUtEVnMyd3FBY0E2aUVJWUNQR2hPYkttOUd2UHJXS2tmbXdzUHBlVzR4akExMXVsbW4yV0xWdTktSmhlaHpZMWZuSnN0aWJqQUIwRGE4dVgzdjcwMllWTTdTQVdRRHFtaDRFdEZvR0I3QnVETF9tRGRDS19EdWRyNjVmRGZDcGRzMDlMZUVQVWtwY05udm0zMTFqNnd6bDNRbUNMd2NOVG1QOTBYSHJxeDc2QQ?oc=5) <sub>gHacks</sub>
- 📰 2026-10-11 [苦等6年，满血版FSD终于来了！这次特斯拉再也没有借口可找了！](https://news.google.com/rss/articles/CBMiXkFVX3lxTE9RQ0dqQ29uTU5wdVR1el9tamZSdERqNWNTVkJVNVpWQ3JRM29mYk9Mdk1MLXFrNEE5dW1ydFBKZ1FRZXRaMHV6WncwdEZYQUg0Z1g4UENIdmFMcjBfLVE?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-10 [特斯拉FSD v14官方首发使用教程！ FSD欧洲更名Tesla Assisted Driving ​](https://news.google.com/rss/articles/CBMigAFBVV95cUxQQ3lWSWVJNEJnVHN1bmpuMHNWNnRpYlkzWllBSUJlQmZlUkNxSzVHd2FFOG4zVFVnc3UxWWJVSElQUVRObHdXR3JZY1dpMWlxUXFPNE1rckhJVVhTd1VoNE9Mc1dDUldSdVVMMzl1ZnpFbUNmaWltTUhKWkZ3VTdIRQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-10 [巴黎车展上演小鹏NGP VS 特斯拉FSD 智驾仅两家报名](https://news.google.com/rss/articles/CBMiiAFBVV95cUxOMTlRRnhPMHhGNkN6WlNfNUYxZS1Xd3VHdEN0eUQzT3RBcWlNTGttcFg2YkJhT091TFd5YzRCUEtZNS1BWVJtcXRHT1JSRGFnSjE0YV9qR21WcV9oVG52UmlFMWFDdFpET1RIM0dLODhIT1drbmZCUDRHYzcyRzlscTVvUExpTjVh?oc=5) <sub>搜狐网</sub>

</details>

<details><summary><b>NVIDIA</b> (216)</summary>

- 📰 2026-10-11 [Valve Details Steam Machine Verified: 47 vs 38 Games [2026]](https://news.google.com/rss/articles/CBMigAFBVV95cUxNVXFKcWpxck9TZWZJNmVSZ3Q1WUdsTFlRTjdTSkd4QWp3WXMxMmNEMUdnUV9keE1XdFN5QXZMWnRRcjN4RlhDQXpRZnlVSDB0RlMxN1NMeVFncFZ1VzZlSHJ2WW12RERjVHRYVlZUa0pxTDY4N0NLdVNUTUg5Rkp5Qg?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-10-10 [Nvidia in talks to invest further in Reflection AI or buy it, FT reports](https://news.google.com/rss/articles/CBMisAFBVV95cUxPaFV2ZkJEanVWQlYzV2c2WVZxQ2V0S24yeEVYNW1TeXlzX082dTRvVUpZWG1HVFNCYTNNVUZZc0NpaWVBdW5feWx4clU0NGtHVDZtR053YXYtWFZnSmRVMGFMQ0ROT0phRzBNd0RVYUVTbk1CTmFucGJPY05ueXdqNVdwQlpJamFaYzZzaUpIdjZjTVhIbTN0ZURBMXYwdmlTRHZWVTVrVklXOWlZXzFxag?oc=5) <sub>93.3 The Drive</sub>
- 📰 2026-10-10 [Nvidia reportedly halts GeForce RTX 5090 production in favor of AI data center and professional GPUs — impending supply drought expected to drive up prices, RTX 5080 24GB rumored as new gaming flagship](https://news.google.com/rss/articles/CBMi5AJBVV95cUxQSjBCd255Y1gyWXBvSnlpVW4xNHVteF9MTG40Yngxdml6SnJ2R2JoNkF4OTdzMGJ1dkRIaVNoVlc0MnItdkNCTV9QX2FscW4zRGw1UkFTV285VW9DZS0tWmNXdmR2dUtCNmh6dWRWcmxSN3lVWDVhZ01qNUxGZ2k1bW03LWZPWndlX3NXcENxczczNUJNSUU4OHNzN3pQbmlkMmpPM2xfVXA1Z1E0b2dsMUZ4UXRGUkJ5aWh5MnVMUjZuNDMyeHBOUFdjNEJ1X3V2Wm1seDlfWHpEbC1idlR3RFhIMzhvTzRhYXFYWF91UEhXTEpfMldZUXNhMmt6Vmtsa0dnQ1B3eS15X0tmVEFXYWo5RFlUZWl6b21LTUtGM3FQbjJ0eFZscy1IOE9LaEdWb3F2Nnd4TWVXcnBKN2J1TTNzbEhaQ0ExVEpYQTRuaEhOLWg1elY2U0pYc3dvdHBac0JLLQ?oc=5) <sub>Tom's Hardware</sub>
- 📰 2026-10-10 [Nvidia RTX 5060 Runs macOS 15 With Metal 3 Acceleration Using Unofficial Driver](https://news.google.com/rss/articles/CBMipwFBVV95cUxOT2F4ekxMU1d2M2VNQk9OY0E0VHVjT1cyeTVlVlcyekhJRktxaFY1Tk12RUJubUZHUkFXelVqMWdmN2Y0U1poSmJSN00wLTlrZWVmSDVuRHFXcVZPYTdRQ0pjNFc4ZlAta3RQc3oxbjZYdzJDU2xzandzaUdvbDVxZjN0OEdOQ1dZeDI1b0NWTzZnSUlES2plbHJJOVJVckxBcy1OalZ1dw?oc=5) <sub>eTeknix</sub>
- 📰 2026-10-10 [Prediction: This Will Be the Next Big AI Gold Rush and This Company Will Be the Winner.](https://news.google.com/rss/articles/CBMi9wFBVV95cUxOdWt1V3Jtc3N6d21tcmhMRG1XVWVYa1I4SnVfUVVNWFFaZkRCS2FsanhWMnczd0tZY0UzcWtzUnEtdExmdnFkUzd1WUptdFQxRUtvWWRpT1NUcUZodmNNS1RaYVB4cXJKQVl3UmRCQk5xNExRZnZjQkpSaFJpUkJvLTZ4QnZrWGJxQnBwMjRmMW9sRDhNLWlMSTdocjI4c3o5a3EwS0VaM0R1TzIyNnl5UG5PelVYc2tUWXk0M0dCR04xTm01clJqSWxpc2VRWjZuRTdKbDNWYVhpZ0RESnBCWVNfR0hZZW9qa2NlSFVzMERIOHdtSTRr?oc=5) <sub>The Globe and Mail</sub>

</details>

<details><summary><b>Wayve</b> (64)</summary>

- 📰 2026-10-09 [Stellantis CEO says Wayve partnership will cut self-driving costs and timelines](https://news.google.com/rss/articles/CBMidkFVX3lxTFBmYUUzb1R1UkJYYmFlaGhZVVYzVkVqb01sWUJNWnZqVW05RGN6MVN0czVlNU1sUTBzTDRpam82UkN2THllajV2QnBFd05ON3Eyc3JTMDZmMTFDMlNXX2tsVXVyekVRUDJlOWFyYlpRNmJ5Q2Y4b1E?oc=5) <sub>Quartz</sub>
- 📰 2026-10-09 [Wayve’s Alex Kendall: AI driving will be required ‘like a seatbelt’](https://news.google.com/rss/articles/CBMilgFBVV95cUxPT1oxeTlZZkhJRk56T3VELVZRVzVZVXE4R3RnZG1MeEZRWlI0aXBVN3MxLVlyLWhNV1Z5bDNIRFBJN01ubG1kTEllcm54QXZ6Q2p4MG1wN0c3WnZoR3ZZYzlUN2lHX1dxNk56TFVMZHFMc0NmVDE4a3pMX2x3RS1ZbHVpdjQ0MGRlXzByWTRkMEVCX0lFdWc?oc=5) <sub>The Next Web</sub>
- 📰 2026-10-09 [Stellantis Taps Wayve to Cut Self-Driving Costs and Speed Up Development](https://news.google.com/rss/articles/CBMidkFVX3lxTE1scXo5UUFGQVkyV3pDcFlmSXhVejI2R1prVklCRmEwckNXZlJLVWI5SzlUdjhpcXg2WGJ3b3U5Y3A0N2pHMTlRdERVMEo2bmR6RWRROXV6Y3FQdi13alp0a3Qwckg3MzEySkt4RGNRbFBTN2JtQlE?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-09 [Stellantis CEO says Wayve tie-up can cut self-driving costs, development time](https://news.google.com/rss/articles/CBMi2gFBVV95cUxNYldMeElseFhadXkybkktR0swTklvbVVTZVpZazBhcUYyZGR3dHhUMUE2ZVVsOC1pbFRjcVJGajk5Tlo3bFhqeGRVX0ZSSmV3aHVWR1FyQmFYQTJfR1MxVFB6UUozLTNoRHNiMVUwcEpFTk51TEk0MUxuRlM2X0ZJRm8wemM1MVo2cFFQcGRlVVlkcUZmNnVDREUtTmdORnJVLXZ5SXRYT2VWLXNEdlFaSDQ1NXE4Y2syTm0waWpPUUpmWVBxTi1xMjRvTWZhTlRoeUNDb1h1OUtPdw?oc=5) <sub>Reuters</sub>
- 📰 2026-10-09 [Stellantis partners with Wayve to cut autonomous driving costs](https://news.google.com/rss/articles/CBMiuwFBVV95cUxNM0NRODlJdV9sMUY5dHdGSExQNlpCVnRNTGlObUdVX1ZkMGI5S1pIRzFCaFRIN1l4UmNkV09qS0tMZUVNNGVfclhMMzVCQ25IX1Z4eHJENVVkaFU0Z3hETTdrakhzSWszTHNPUm1NSUhmd012NHFrT2ZxWGlZYmRDc0UweFNIakNfaHZPNExKMFJ6ZExzZ2VjeUpDN0FDdHZyMjVKMFhlV1dWeU51WHc4V1Vfb1MwRkIyUDRN?oc=5) <sub>Investing.com</sub>

</details>

<details><summary><b>Momenta</b> (113)</summary>

- 📰 2026-10-11 [新上市的豪华插混SUV哪款值得买？全新XT5 PHEV、理想L7、领克900与腾势N9智能驾驶横评+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFBES0QtTkY2R3U5eVJsbWZCTkpHSmFaRDQ5WVExRXZCbmhTakRpSFBVYjdweWZpZG5ReHQ2WHFmaHA5V1U4S1EzLVdSMVg0SWtfdlkwLUI2eUFuRkEtV1hpWVdhR0dKRzBPQllTNFVaeWJudw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-10 [2026年MOMENTA：智驾从L2走向L4，R7开启物理AI序章](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1JWGJxSWVhdFlsclVpMHJDWF93VjBCckZKRVp2eXJwYTNwNUVzQmN6NGdabGhrQTdsd2JfalRiQlJMT3ZOU1RzWVplNHpQX29nOXJR?oc=5) <sub>电子工程专辑</sub>
- 📰 2026-10-10 [标配800V/Momenta R7 上汽大众ID.ERA 8X将于10月12日上市_热点推荐](https://news.google.com/rss/articles/CBMiYEFVX3lxTE5ISms4VjNkczZUSkc0QTRzcHZoZnRDM3k0bXhWV1NMeEljX29RRDVtUzhIN3YycndNUHVpb3VfWDdMYy1tMzhfQ05pRE5fRVA2c3ZpSVBKQjQwelpWTmxoUg?oc=5) <sub>证券之星</sub>
- 📰 2026-10-10 [带激光雷达的豪华插混SUV哪款好？全新XT5 PHEV与4款智驾横评，Momenta R7算法怎么选+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE85LW5Qa1c5dW1idkt3czBZd1RqYWItSlMzbVZpbFJBb3R1ZnQ0c01TcmVlMGx2d2ZVSTN6Y01WXzRQXzJDbjYtb2tMSlYwXzFEeVl0S3BXMHJBdlo1YmoxZlNxc2VobmRfMTNWTXFNeW5mdw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-10 [全系标配800V+Momenta R7 上汽大众ID.ERA 8X即将上市 值得等吗？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1nVkJ5QmkzU2RwRVE4cVF1UVYtTXg5cVl6bUhqNnlxemN4RzFzNDlwV3dWUzFmWUUzQ3c1YldmLUp0ZExUenVfdWhtUHA5TzlCQVFJaS0zUjFQczg?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>XPeng</b> (276)</summary>

- 📰 2026-10-10 [XPENG Launches "YOYO" Robotaxi](https://news.google.com/rss/articles/CBMidEFVX3lxTE5MbTd6d2VTRko4czktWXgyTE5LbjRmSUhKNHFteVV2U3lqU1RrSVVFUERKQzRZU29RdS1NTzlyV1pmWi12c1dtMl9XeFZqTHRIZnNtUnAtZEg5cWF2OEcyMkY3UTJiNUtHRE9ZYWFyWkVsV01v?oc=5) <sub>CleanTechnica</sub>
- 📰 2026-10-10 [小鹏GX真实测评：26.98万起的“智驾卷王”，这3个维度决定谁该买+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFBsV2cxZkdxSjI5NWNhOUszTnB2bUtTWFFobVZSNml4NW1DLWotZE9PcHBtX3dxUGR0WXR0LWF5eHlOU2g4Z3Byc3YwTm1LRTF6Q2FZd2J0SjlSd3l5ZTh3VlR5QlhFdzhuam1Mb2xqWlVGQQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-10 [XPeng Pitches Its Self-Driving Stack to Western Rivals as Robotaxis Eye 2027 Overseas Debut](https://news.google.com/rss/articles/CBMi2wFBVV95cUxNNmRrNS14U1F2SGtSd0h4ZkNfc2o0Zng1Y2dyZURlSEdWQ0VzQVJwUFRWMHFWU1BmWVR0ZHBjYmZTWE5COFJ3U3NWNW5kYmZ1WUltZEFDQTE3U0RITEFXV3BmR1NCN0tLeDlZOUtaYmRUVWVNc1hPUTBkMWk3d2ppVGJycmdGRjVVcHV1dUFZelFCU2FtcU1IX3ZINnJFdnl0ajBKM1RRWlFJT1E4NVZUT0dBamZ2Z3JMM21SZzJzUHlaa1FoWEFWU1RRNlZVLWdaNEhpbVp5ODJTODg?oc=5) <sub>AD HOC NEWS</sub>
- 📰 2026-10-10 [巴黎街头窄巷多，敢让智驾实车跑路的，只有这两家\|小鹏\|特斯拉\|巴黎车展\|ngp_新浪新闻](https://news.google.com/rss/articles/CBMiY0FVX3lxTFA1MlU5dEN1ZW9ZUnNkN0w5Z3RVbDJXTVZQTVFDNS1kM3IwUWVDM2VUUXdacUowS0w0eVBuakZuTS1tRklWbkV3cGRQWkZTZmdZc0xiVWtRRzllOWNxaGVoclMxZw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-10 [小鹏GX性能评测：26万级旗舰SUV，续航/底盘/智驾真实表现如何？+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1MVVJrYTdPTjVPcVlFTjRhNE9KM0h6M3lWZGxlUjdVOFZJMktjUXNyQk02Tl9HRzgzekx0OHFoZmdxWGtRdjBXNDV4V1BqRUNfMlRTVElkMTBBbnJxblYw?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>Li Auto</b> (165)</summary>

- 📰 2026-10-11 [30万级新能源SUV横评：试过领克900、智己LS8、理想L8，最终我还是锁单了神行者8](https://news.google.com/rss/articles/CBMickFVX3lxTE5KSmpfbEdQbHNmWnNfR3pneWd2NWRmVmN3M19VZWhsRHlDYUZZWk9UcFlkUkc4eDVtZXhFbWxPRnhlTVd0MmtVSjAtaXY0SEdUV0k4VExrcEk5RF9wLXM3NW1oM0VXc3FlWW1HM19VeTc5UQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-11 [新上市的豪华插混SUV哪款值得买？全新XT5 PHEV、理想L7、领克900与腾势N9智能驾驶横评+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFBES0QtTkY2R3U5eVJsbWZCTkpHSmFaRDQ5WVExRXZCbmhTakRpSFBVYjdweWZpZG5ReHQ2WHFmaHA5V1U4S1EzLVdSMVg0SWtfdlkwLUI2eUFuRkEtV1hpWVdhR0dKRzBPQllTNFVaeWJudw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-11 [新上市的豪华插混SUV哪款值得买？智驾横评，全新XT5 PHEV对比理想L7/奥迪Q5L+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE1uUlJWakpERERpR3FHM2JDZm9CUG9IWlpOMWhxQm9EQTFXLWR0THhNdVFlSHo5OHFORGZEeWo2Q3RZUTlhc3ZtazBxM1dGOHRUY2NXcXF1ZGFTU3VsS1FnTWdPWVBiZDlJeGpMdVdiVFhyQQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-10 [长途自驾横评：神行者8、理想L9与问界M8，谁才是真正的全场景豪华SUV？](https://news.google.com/rss/articles/CBMickFVX3lxTE5CY0dBNXlfdEV2RVo3Mm8wZ2x3RXlla1dESFNNaVc3VHBVN1dZRjkzakViRmpIQVB2X3lSSUZoQVR5M0M0NTl2d0tmRVJ6Mm5uV3ltdWlMVmhkTFlxaTYyYUxpdVNmcTBLMGw1NWF6WXNWUQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-10 [三款旗舰SUV正面交锋：理想i9、问界M8与神行者8，谁才是全场景最优解？](https://news.google.com/rss/articles/CBMickFVX3lxTE05OFBKc3dmeFc2dmZvcnhCUEszU3l0TjFpM2RacVpqT0Q4VnFUZjI2RUZsWTZRSkx5R2tMcWV3ekVfU2ZsaWdPX1BHSVZyc1p4OVFjMjhqaWwzem1CS2wyZ19YY2tHMlAwYUxRWDNzSzJ0dw?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>NIO</b> (153)</summary>

- 📰 2026-10-11 [蔚来抱上吉利大腿,小米锁单8万台,华为智驾破190万!新势力图鉴](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1zQXZBRVdWNGFjaHMtZ1F0ZEtCbzF0UjFCdW95SC1RY2RzLU1kZGN0VThmLV80R3dqMUxSNWhpZmMyME1QSzU4VExaXzJ2blpQNEZIRXFDRHpsUEU?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-10 [【视频】蔚来EC6 2024款75kWh租电版](https://news.google.com/rss/articles/CBMia0FVX3lxTE9QbUVhVXoya2kzSS1xS2dyZk53YVBOWDAwdFFtOW5XS0ZCNVNhVTdreU9IM1daek9uaFNoUnNxMndtR09vWHVMOTZmTmt2a2t4bnEyZlNCa0JhVnp4OUdkTXBwOWJSSTVLT2lJ?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-10 [310km纯电+12分钟超充+全地形，神行者8对比理想L9/问界M8/蔚来ES8，谁才是长途之王？](https://news.google.com/rss/articles/CBMickFVX3lxTFBrZEhVNEtDWmhOak5JOFhwSXhVOW15Ync5bVlDY2tVTU9PTWhjVWo3aEFFckZ2YWZJOFVrNnZfT0ZGX1pVYU43WllqRDFBZ1R2SkU3MG5JcDNCNV9DcUwyTWJ2LXBYYUhySmNueWZ5MDVMZw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-10 [蔚来EC6值不值40万？刷完试驾视频，我总结了3个关键点+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1QY0ZRUWw3MEs0WU1YWEZqd2RjZDN3YkpIRDVneU8xZ1I4U2hGRHZHMmdneEVUZjM5dEJsR1pGZWdNSVpQWmw3ZDhMQ0o0aEdDMmhrZlpONTRXT2RpYVc0?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-10 [长途出行如何选？问界M8、蔚来ES8与神行者8的硬核较量](https://news.google.com/rss/articles/CBMickFVX3lxTE8xLU9LLUF5TnFidUJTaFZRQzgwWWg5YmNXY1hyT0tRc2FfVFVVLXF4eVpLdGFSZzdhNjhnYnh5N3RSU09Mb3BNNXprMGZtSC1tTlRYeFZvZVR2aFZGZmdDWG1uNnQ0LXZaRnhxYWN2c0Rkdw?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>Huawei</b> (397)</summary>

- 📰 2026-10-11 [Wide-Screen Phone 2026: Oppo, Honor Chase Huawei's 180K Hit](https://news.google.com/rss/articles/CBMiX0FVX3lxTE85UnhhMUl1Y3hYeWZqc21SWmVBQUtTYkt3MkR4TGpOM1dZWUtkdFJUTFVfWEg0QW9WLTEwRnpZYXg3NW9lLWhEenNqdVJzQ0JnRllqbWRFNDJCaUFIRGpz?oc=5) <sub>Memeburn</sub>
- 📰 2026-10-11 [Palmal Group and Omera Renewable Energy sign MoU for 4.07 MWh Huawei battery energy storage system](https://news.google.com/rss/articles/CBMiyAFBVV95cUxPU3lUZGhXaElQaHJ4aWlhQXppcmp1LTFFQ1RkekE0RFhOWjc1YkRod2s2TDVPV0NXSUJRaEE3UF85b0RoSmU3TFIydDFSRmlyYXRUaFA3S2tzWmNCSlB3djhRcWNHeGJVSXcwTDVnRXRMLTY3OVd2alZjam1HTlNSbkl6VjR2bFBIUlVwRVlWalhYM0JkdHd1MmlUMkZfMzFQRWd3V1lGVGFZMmJjcHFLcHl1cmV3OHZvZFNaM2VidU5rMkg2c3VNVg?oc=5) <sub>Textile Today</sub>
- 📰 2026-10-11 [开着路虎神行者8在苏州东方之门下体验华为乾崑ADS](https://news.google.com/rss/articles/CBMigAFBVV95cUxOTngwTGs3WXcxWUdEWjBMakhJUlZLdV9rMlphTW16OTNzS2RnVGJjRVV6NjBDeEM5aDFJWDJrMXpEbUNKb3dvWW5ZczZXUmY1VXpDLU5ZUVdCVzlYeFpXMk5pNVBBNWFTdFlua2tZNXI3X012OTZ1cTVKRlFfQnA2OA?oc=5) <sub>新浪网</sub>
- 📰 2026-10-11 [增程版大六座SUV奕境X9重磅上市](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9jRnFqRTk5dmNGaldjbDI3UldsRjVVek85RUFldFk1WHE5a0xrV0JXNXo5U0xscEc0S0hHbF9kUUVZYTJIa2J3bXhkX3RRNmo4NkhFdWpwY2ppcjg?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-11 [13万真能买华为智驾+5米车身？极狐阿尔法T7深度拆解，3个维度说清值不值+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE5ESGkydWgyd3JwUXpqZG85OThlOUItM0E4eGp0eFNhTmFuemM4Vkp3ZmhXN0FqYk5wbTdfNXF0TEthM3Q3U2Jnem03RG5sa0FKZkloMVhGTmZ2NzY4Z3RYUWlndG5wb1Z4OG9NbGVrUnkyUQ?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>Baidu Apollo</b> (54)</summary>

- 📰 2026-10-10 [BIDU's GPU Cloud Revenue Soars 283% In Q2 — CEO Says AI Business Is Now 'Firmly Established As The Core'](https://news.google.com/rss/articles/CBMi1AFBVV95cUxNMS1oZ21ORWQyd2FnbEczVHoxNmRtYTR1bF8yZ3Q0UTBheGVvSkRubGFIb3RDOXBKMWJ6cE5fZloyVkhaMFlFbWlfbUdJbDNFRkpTQ2NHbXBybTVGQ2szZjk3blBVTFpzM3pjZ1dNSU9WZG5xR0FyYzd2OXJSWjJFU3RFYnloTGtqdTdaY1g4eURubG9jTlBvZHFvcXp0R1FYOTlyVGJVcTVzN3BNN1RocXItc2pWYVZhb18tZUlSTndjNllCZlo2Rl8yaFlIVUJ1V29XXw?oc=5) <sub>Stocktwits</sub>
- 📰 2026-10-10 [Waymo Goes to Wall Street｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTFA2Z3RvWEJLVEtPTDJWNVcyaGQweFBVUnZFb0RST0wxRWhCdUJudXJQeU9helBuODZrTlBDZlh4NF9zb3dyNjRxQ3BzTGpZLWJvQzNObmFlYjl1R010Z3hB?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-09 [从“卖产品”到“深度参与”：中国企业进入中东的方式正在改变- 21世纪经济报道](https://news.google.com/rss/articles/CBMid0FVX3lxTE1uanZ4SGtKLTJjY3I5LWJIdEcwV3htNGRhSTJ6MkJiQi0xNExYTzZTM3h0V01NeU41c2REU28ybF93X0J6Qmp1Ykl4cVY1b0VjMVJfaXRlWktuTlJIckQzTmtqWUJXOUdPOVhvd0Z1NFhYT082YXhN?oc=5) <sub>ZAKER新闻</sub>
- 📰 2026-10-09 [Xpeng's Yoyo robotaxi service goes live - ArenaEV](https://news.google.com/rss/articles/CBMifkFVX3lxTE05ZmdRVFl0SUJadTdFS2FETjRQS0R6czlWVElYTms3OG56THFhQjluQVoxUUpraEJTX1JkNW9jSERLNS1PNVFDQnVTUGtYSjgwVW54WEJUTW5NZHhYU1EzYXhTd3dnT0xuQVlyRkxtbnhzM1o0cktfZGQzNnFBUdIBfkFVX3lxTE05ZmdRVFl0SUJadTdFS2FETjRQS0R6czlWVElYTms3OG56THFhQjluQVoxUUpraEJTX1JkNW9jSERLNS1PNVFDQnVTUGtYSjgwVW54WEJUTW5NZHhYU1EzYXhTd3dnT0xuQVlyRkxtbnhzM1o0cktfZGQzNnFBUQ?oc=5) <sub>EV Arena</sub>
- 📰 2026-10-09 [百度萝卜快跑：东涌自动车测试项目10·20起展开公众试乘](https://news.google.com/rss/articles/CBMiVEFVX3lxTFA2QkNSRVhNeG9lbWl1WU9uRjJ4SmVDRnhxUS1wRV9Yc2tES01SODJXeXFGd2R3b2dJQ2UyRWlfU1I5d0ZySmliNEFRaEFIRlZBd0UyMg?oc=5) <sub>https://www.hkong.cn/</sub>

</details>

<details><summary><b>Pony.ai</b> (129)</summary>

- 📰 2026-10-11 [Uber Expands Driverless Taxi Testing With Pony.ai in London](https://news.google.com/rss/articles/CBMiZEFVX3lxTE95X1oxNURSM0JJaUVXTFNVV21qRkJHUGh2M0xnb3hzVUY1YUYycERjSktIRU94NjNrNjlTNkJIVW1LNVJ6NVRYY2d6X05xajlkd3VfeXJUZk5Db05neWozOFdOZV8?oc=5) <sub>SuaraGarut.ID</sub>
- 📰 2026-10-10 [This AI Autonomous Driving Firm Joins MSCI China Index —What’s On The Cards?](https://news.google.com/rss/articles/CBMixAFBVV95cUxNRTlBel85R2d6RU1SWWU0bXBhenFMMzVKS0F3OUdKcWYtN216bUNnX3cyMWZ4REZBQTlGWHIyQmg1Tzlocnd5US1sb2o4S1YzU25VeWJ4NGc0clNjV21MdzZKd1l1RGVvVkdXQzVRNy1FMUxNX1ZBYmpoSVVTSmkyZzJSNkxxLUZJM3lLR1g0ZXFhNXlTSS1VdXNuZ0kyeHVfdmNlOUh1S1VyRkNIRGYyZTF3TVkxY1dJdEY4aG1OUWd2c2dp?oc=5) <sub>Stocktwits</sub>
- 📰 2026-10-10 [European Driverless Taxis](https://news.google.com/rss/articles/CBMibEFVX3lxTFBrVW56akx6SEd3Q1FhVmdxNnlpcy1BekpPRktQd2NINm5HM18xRWZFd3JHVHlSUkNKZVAteTdRVGJSV1hzVkh3a01yMW9BTHVmUzBxbEgzX1c5VVRXRmNTal9PRC01WlN3QWplNw?oc=5) <sub>Trend Hunter</sub>
- 📰 2026-10-10 [Uber and Pony.ai Plan London Robotaxi Tests; Launch Date Unset](https://news.google.com/rss/articles/CBMioAFBVV95cUxObWRfZjBTY3Mwb09nR1pyd1lFUi1pYXBsMzU2enh0aUtxTmU1R090REY0V3BxdWxIRmpjTHc4U2UwblBqTHhaUWlOdXRzNTZxNUQ2OHRTZHZZQzczRzdYTU9xaFVlX3lULWlCeTNobXVnXzdjc3BUaEpmOE9NYzBtaDAxbHpBQ2VWSGxFbWpLYVk5MXc4LUJjUHZwTWY5WFFY?oc=5) <sub>Quasa.io</sub>
- 📰 2026-10-10 [近期车圈新闻｜OPmobility/宝马/优必选/佛瑞亚海拉/丰田/小鹏汽车/小马智行/福田汽车/立讯精密/本田/纳芯微](https://news.google.com/rss/articles/CBMickFVX3lxTE9VM0pNQTlnMHhUeUcyeG5hOXlHV3lvX2xXMnFleXh1b2Vkd0t5MjBfcVhTZUZpSF91VkUzVkxGNkNmbzVkcFVxRGpiQU5DZEU4MWFWS01SdzgtN1BoRVFSV0dBNjZrcHM5R3ZRLTZVRTVPQQ?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>WeRide</b> (134)</summary>

- 📰 2026-10-11 [PCB股001389、603228业绩大增！南向资金爆买两只互联网龙头-证券之星](https://news.google.com/rss/articles/CBMiXkFVX3lxTE9UQ0dmVHJSN3hOWUZGaTVZTWc4dkRPN1hwbTcxSVlyLVZnemRMMFA4eWVLbGNWYzdUNFF4c1RFbm53SVR1ODN2UlZmMDhxblhNb0ZxUkFHZzNvdG9abVE?oc=5) <sub>证券之星</sub>
- 📰 2026-10-10 [蹊跷的“全国第二”：汽车网站城市NOA装机量排名，元戎启行上半年数据相差近五成 \| 大鱼财经](https://news.google.com/rss/articles/CBMiYEFVX3lxTFB1MGppeVNQb0FOSWFNWm4xWHZaeGlTR2JhWERsZkJNTG0xSzJaYldkb3QtbVNudWRPRmx0RVBoMVNwZzdjZ2FNRmZZQmJkQlBGWmpYdlIxTW9OOVliMWNPMA?oc=5) <sub>新黄河</sub>
- 📰 2026-10-10 [配华为电驱和宁德时代电池埃安Ray7将于10月17日开启预售_热点推荐](https://news.google.com/rss/articles/CBMiYEFVX3lxTE1BRDBCQ0ZOckRPVDNIRUx2eTFvMHUzN1hQYmg0WkgxeUtrUlI4VXNtX1lYMUVsYzlPUFBOUU1nWkFYMko1MnhuU3dMUm9DTGJRclpqOXJIdEZyd2w0c0dmZw?oc=5) <sub>证券之星</sub>
- 📰 2026-10-10 [AION i60油电混合值得买吗？增程版1738km续航实测，3个维度说清+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE5aNzBJM3N2cUdOUVpnODdQZk9Wc0FqV1ZtbGhJTVpicnhIcjctWW05M0RCZGJWa3JTUm9DYm5GTmtObEZrTURjQXdrUjh1eUgzYm1oSkp4MmY2N2VoLTBhXzd3eHBCXzBoOEhzYy1reEUxQQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-10 [AION i60值得买吗？双动力+700km续航，3个维度说清十万级SUV怎么选+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFBGaW1Fb3RkUzdLd3gtLXdqaTV4T0NxTFB4ZU9UR1VFNUYwT2I5X0t6LWYyRmkwQmpGb0RVemtNa0VCTERZcUppd2FBXzhTeEkyeXRsWVVyT3ZQXzlfeUt1Um84MWl6TEN2SldkWGFCVUg4dw?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>Horizon Robotics</b> (205)</summary>

- 💻 2026-09-29 [HorizonRobotics/Ego4WAM](https://github.com/HorizonRobotics/Ego4WAM) <sub>GitHub</sub>
- 📰 2026-10-10 [【视频】老车主有话说：iCAR V27新增300km长续航](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBhenZmNkgwQXp3ZE43dEZ0MDBTRDB1NFJNNmE4a1oyVU1lbVdIZ1FSWGtQdW41OUlvM2ljS05WMWJmUlNWSVRVcV9SVUdxa0Y4aDRTSVl5dEwwVWs?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-10 [13万带娃露营，深蓝S05 vs 零跑C10后备厢够用吗？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1LMzFRNnhSSUJPVjFWTFBIWTB1SzhGMTNicktJdTBqUEdMcmJYd3owN1NHaUdwTkg1U0hWZzBueTZvdVg4dURwWG0wd2tFdHNXdV81THc4dDhlV1k?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-10 [China's August ADAS Chip Installation Rankings: Nvidia Holds Top Spot, Horizon Robotics Narrows Gap to 10 Percentage Points](https://news.google.com/rss/articles/CBMidkFVX3lxTFBDQWZpV2dPcklnSVlXd3haTmpJaWJESTdYTzRySndUU0Z2aDRlWXpVWTFKOEhsSEdyOGUyNzJEUE94em5hZWFyVUVhbGQ2VkZuaHl6TWJZVWlKNnVyTk9rYThIZGR0X1Z0aG83VzdhZFV2bVVOclE?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-10 [The "duopoly" pattern in smart driving chips continues to strengthen: NVIDIA (NVDA.US) ranks first, while Horizon Robotics (09660) holds a steady second place as the market share gap narrows.](https://news.google.com/rss/articles/CBMirgFBVV95cUxNRmkwVkpHYVdIQmJTdWhrVUlwX2xydzV1TEEyaHFTQVZwSW1DMUFQRHJJRXpJSUdKdVdHOHZnX2lJdUhPdHhTeHE3WU5VZ3ZqZ0M0NjMyejZmc2Y3VThiUkd4cFZLNExoWHhSVjBRMG1KYzhfSDBtckZ4d1JseDh0b3RPNzVkNWo5eERsQW81UXVyeGpORVk5eWhqcTZraS1ZaVhmYzVmVjlpdDd0Ymc?oc=5) <sub>富途牛牛</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (30)</summary>

- 📰 2026-10-10 [观察｜28岁的姚顺雨坐在马化腾旁边，深圳的AI下半场要怎么走？](https://news.google.com/rss/articles/CBMif0FVX3lxTE80cFpSSElQR2dpM19kVS1DV29KSGw4eFFJMm1hX2dFU0doZDFxRzB4eVpPN3lGRVhBalVEMGxoSUlLX3JkbHVjdjJhTDdxUXdlMnRneGxGQ3NpMi1GSDlnZUN5bldsTjFINGZhMkZudm5kR2pZaEs0WGNUSk1oRWc?oc=5) <sub>新浪网</sub>
- 📰 2026-10-10 [赛豆AIVA ME7首款量产车能买吗？20万级AI汽车3个维度看清+FAQ](https://news.google.com/rss/articles/CBMif0FVX3lxTE9YT3gycC04RVo0SGljaUxQemtKSVZrZTdvRUNRV0gtVi1jbUNQTWhXdzZqenhTaGJUVVBac1VoSFhDcmowT29GTDhXUDNNWnN3MjRfRjNhVXYwVl9BZy10QTVaTWRTaFgycVl0X19ZaUIwa0lhZ2FMNUpuM013RkE?oc=5) <sub>新浪网</sub>
- 📰 2026-10-09 [赛豆AIVA ME7深度解析：20万级原创AI轿跑SUV，真香还是噱头？+FAQ](https://news.google.com/rss/articles/CBMif0FVX3lxTFBzaVFpNWNnbjNlQU1iTU13aTcwc2pBZERxVlV3RkpESjJRN1g4YmotNmNISW11eGtVXy1aSHBmeF9hQWxMeGdNRXBrd1lEMVpkRjJUWUxIbmxnSjgtZHpzT3h2VmxhZlNDd25oTm9sNDVVZm5NaDJyYkQ0RGVxR1U?oc=5) <sub>新浪网</sub>
- 📰 2026-10-08 [城市NOA座次重排：第二换人，头部三强只差1.7%](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNd1ZkX3lwNUE5bUEtTGR4a1JiSHBSbXM1aDJxUmc4TEtlVGRJUFZKempPX1dtYVZoVkVRY1pZNWRlZ09GMzBBODRlQ0FMZjQtR0Z4R2g3NC1pUkhfeG92a3hzaGtuWDFlYk1ZaUJSWjZzVFh4R014cTFTZ1p4bW54WldObE9oTmEy?oc=5) <sub>搜狐网</sub>
- 📰 2026-10-08 [豆包加持，赛力斯AIVA新车呼之欲出，20万元级市场要变天？](https://news.google.com/rss/articles/CBMiTkFVX3lxTE5IM1pkZ2RWaG1YLWRIMFRIcXY3aHgtUklFbG9NaUJCd1ZkXzNvUjRHel9wOTRJOXBzM09GRGQweFQ1WnBoZXE3ZkJjTmtWQQ?oc=5) <sub>36Kr</sub>

</details>

<details><summary><b>Mobileye</b> (19)</summary>

- 📰 2026-10-07 [Uber invests in robotaxi provider Verne](https://news.google.com/rss/articles/CBMigwFBVV95cUxQQkxEa25xSjBNT0ZJMzZINk54a2txS3k0S0pvTU4wZEJ5eVhHY0FNRWlyaVdIcVhYdmlPQl9HVUsyUnlkcW1UVzRVc180dHNCT1hXV3ZUcms3Mzg5aUoyZENTUWU3VHJtRlFuQmp0dWpQRDlmU2xlSDQ1MnlEZW11YmFGWQ?oc=5) <sub>electrive.com</sub>
- 📰 2026-10-07 [MOIA America Launches First Autonomous ID. Buzz Rides](https://news.google.com/rss/articles/CBMixAFBVV95cUxQY2FmM1hNRDEzV0c3c2NSVklIUDBPU1VrbmRmNnRLV3lNRzRITUVHUldKcVNYajNSYXJkdTJmbzRGeWt3V3ZrcXlmanBfR2t5cjRKZlU3b2JHbUg3VUx0ejdIS2ZUT25DRm5KTGtzSm1OaEhhQ2Zsb2Zhb0tHMDlnaWhnOGJHLXBvYk1GYkNYVFJRb2M2R3BmamRnN3RMZlJ2a3JlSGc3VnNmcXBtVDdub0s2VjhXSDhKVjFDR1pIQjYwLUpI?oc=5) <sub>Fuel Cells Works</sub>
- 📰 2026-10-07 [Uber takes a stake in Croatian robotaxi startup Verne](https://news.google.com/rss/articles/CBMikAFBVV95cUxOMkFfTDhoaldrejJpdUNUd1JvRXN1MlZwYVZQRjdPQ19FM2oyWjgxTndscUdGWFVZaG5nSWVKNWQ1dVYtNzFNZ2t0VnFwaS1mOFpneG41RW51M19leE9XSUN5WjhGbjF0ZkUtRVI4RDBiSUxtX2ZCTDBUekNRN3p1ZXZzUFU5aXJ0cjk5bHA3aUU?oc=5) <sub>Dealroom</sub>
- 📰 2026-10-05 [Moia’s autonomous shuttles start first passenger tests](https://news.google.com/rss/articles/CBMilgFBVV95cUxPaXBLWlk2ckZabm9UeXdOV1lCZTRjaDBkVmk4bDNVRWVMZkxKUEVTOVBqZERzWGlySkROdEs0bkE3SURjaG44c1Y4M3lsM0NmSG95X0diNlY4cGJoMUp1UUMxVnFkQ2Y0UTR2UDdtdTFzczBDSHpId3ZmWDltWlY3Ulg1bHBYMzJweHhDOWkzd3lyVWwxSGc?oc=5) <sub>electrive.com</sub>
- 📰 2026-10-03 [We Found Atoms, Rode Wayve and Watched Uber’s Autonomy Clock Speed Up｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1QZjNLZlpHR2ZtcHFaUDF5bEE3ZktHQlNoN0E1amxaVEg0eUdQbElIVlVVZk1JdTlqZG1kbGZYVTBvZDdKRDRKVWlqa2dRNDF3aTN4dEpmdTdxX0dTVnlj?oc=5) <sub>finance.biggo.com</sub>

</details>

<details><summary><b>Aurora</b> (61)</summary>

- 📰 2026-10-10 [Autonomous Trucking Hits Regulatory Green Lights but Economic and Safety Questions Linger](https://news.google.com/rss/articles/CBMiugFBVV95cUxOTWpyRnRTWmc4N3ZLMnNCM3lrVXhTQS0yOU1ZZm1na19UR1dpTFZvVXV0YmVhUFFyOHFMZW5sRWFPclppVHM2ZVB0ZWgzdXNDTDUxRF8tOUFpX2xfelRBM1RtUkVnWUZJUjhKVjJCMEdScE9xejVOX3B2Wk9pZENZY2VNTHVPQnpMYXZiM2hETC1hTlF6VlJ0YVFYSzlWSGZFSGdtakNQLWpEMi0wbW1oa0o5U3VvNDctekE?oc=5) <sub>news.lavx.hu</sub>
- 📰 2026-10-10 [U.S. Approves Beacons Instead of Triangles for Certain Level 4 Autonomous Trucks](https://news.google.com/rss/articles/CBMiWEFVX3lxTE90RHUzcGstTU8zd1ZlUjdmdmQxbzZwR0U1Q3VTRXdRdmdqemgxQ2M5d1ZyWFFvNHJVQWVlazd5bU9XWF9INjVQbzhITzZkV25qVGlZUkZjY1Y?oc=5) <sub>CubaHeadlines</sub>
- 📰 2026-10-10 [The U.S. allows the use of beacons instead of triangles on certain level 4 autonomous trucks](https://news.google.com/rss/articles/CBMiwgFBVV95cUxNbGFELVhEYy1keWYxUEZ4S25pSGd1a291QTVvZGJPZXEtWlpqZnFlTWlRc0ROY2VyNVAyOXYwX3RVNl84REc2VWQzd0FzMldISWFUcnZpcGhnMm5tcllQWHNSTHdoNG9WNnVTLW5kVEJBLU5lWDItbThnMUNabXdHYm1jUHZWNkdkcE1yUmRncHhrTWlSOUw3dFhWbkNXdjR0Q1U0dUV5SE95eklYWlk0azgyMUd6UkEyRjZNTGxpZkxKUQ?oc=5) <sub>CiberCuba</sub>
- 📰 2026-10-09 [FMCSA exemption gives driverless trucks a green light](https://news.google.com/rss/articles/CBMigwFBVV95cUxQVGJYNjYtb3c3V1dKcVdDWmlmdUwzQXRiYkJ6ckk3VjVjUlUzdkFWQXE1bWw1dHotLWNQUlFLYU16VmNPRGFZTUc3SF93eWZ5bjdlaHhYU19TbHQ1YVZMWWI5eTBfT1ItdVVHelJwVW9BLVExVDVENU9ORjl1R1d3Vk8tVQ?oc=5) <sub>Land Line Media</sub>
- 📰 2026-10-09 [Kodiak AI, Charger Logistics launch autonomous Laredo lane](https://news.google.com/rss/articles/CBMihwFBVV95cUxQb0RtaXVVc1NDVWtMRElXaFl5dVhpSVV1d2tkZUFkMlVQdC1tOXN0WTUzUkZ4WmRIVFJsbEYzV0MxOFJSbEphYXItcUJITW1ZTkNHTld3SEV3UC1jZjNrNkg0SlZ6WFFOU2wtR0I2d3NHM0RPM2tYaHJVeWJOWldzaWFERnRTcGs?oc=5) <sub>FreightWaves</sub>

</details>

<details><summary><b>Zoox</b> (85)</summary>

- 📰 2026-10-10 [Waymo's $5 Billion First-Ever Debt Raise Signals a Robotaxi Land Grab, Not a Science Project](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9BaGt6ckszSmpwTDVsOGUzQ29DXy0yc3BsVFdSTjNtZFZrR3dWYUd5TzcwSTYzUTE3MlVmd3B4UG1iSS1kRHpySXpFVlhRTWd3cjVCOUgwVW5FcWc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-10 [Workers erupt over DC plan to bring robotaxis to city streets: ‘This is bulls—’](https://news.google.com/rss/articles/CBMirAFBVV95cUxOV0lTd2hnYmFUYkdFYXB0NGhIdU1KUlZVT2hmQXBMeFkzTkhuNHFxN1RDalQ2d3hiMlZFYmJNR0lqUGdEWUtSZU1yeWREM2hLbWNaOExQeTJRMjJwZWVkWWVnTHdrOURNMi0tQlFIdDRnV1RVMXZ4d0N6WW5VTGNNSFpZcVJlRmlZbHlvM1FvaVloRWk3TDY1bDZNX1JQZC1qbmdta3Z4SmlUX2Na?oc=5) <sub>930 WFMD Free Talk</sub>
- 📰 2026-10-10 [CES 2027 Super Preview: Geely and XPeng Confirm Attendance, Mobility Has Become a Core Topic](https://news.google.com/rss/articles/CBMiU0FVX3lxTFA4Njl4M3R2ZFZfWDJGbkk0TjFPTVJWZzVKME1HdklEX3AzLVhSUEczU0o0RzNfSVB6SjRYcFBwYmVucF9LbHJuX1ZJMnVMWmVCWlJz?oc=5) <sub>36氪</sub>
- 📰 2026-10-10 [Waymo Goes to Wall Street｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTFA2Z3RvWEJLVEtPTDJWNVcyaGQweFBVUnZFb0RST0wxRWhCdUJudXJQeU9helBuODZrTlBDZlh4NF9zb3dyNjRxQ3BzTGpZLWJvQzNObmFlYjl1R010Z3hB?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-09 [Zoox Grounds Atlanta Test Fleet After Toxic Gas Exposures Make Workers Ill](https://news.google.com/rss/articles/CBMingFBVV95cUxORGlqTUp2RzZERlpBZTVSYVlRNjRPTTVrNmhBV25SN1FIekJROUFhV0V6WFJneHlDZ24zSnNYTXRjdWdGaWhPcEZqd0pRazc3WEtXV1RGVlFucWxhalpENTFrTEdCbDI4UDlPWE8xWUpkVmJyVnk3d0F1ZEpaNHdtOHJITEtEeFY1RVFodDYxcWE5SVZVQzAxVG1PSUlXUQ?oc=5) <sub>Vocal</sub>

</details>

<details><summary><b>Motional</b> (53)</summary>

- 📰 2026-10-11 [Six Years into Euisun Chung's Tenure... Hyundai Motor Group Moves Beyond the 'Global Big Three' Toward Physical AI](https://news.google.com/rss/articles/CBMiZEFVX3lxTE1qSWl5SS12dk8yVXMwandrR090TkZkdzZDaFladGpmOGNZZDNrMGxBQV9zSkV5TXpVeXIzWGhKd0FVYUQ0ZFdsT1pEWGxZNDV1UC14N0FsZmxVd0ZFOUVkamhoMWg?oc=5) <sub>아시아경제</sub>
- 📰 2026-10-10 [Waymo Goes to Wall Street｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTFA2Z3RvWEJLVEtPTDJWNVcyaGQweFBVUnZFb0RST0wxRWhCdUJudXJQeU9helBuODZrTlBDZlh4NF9zb3dyNjRxQ3BzTGpZLWJvQzNObmFlYjl1R010Z3hB?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-10 [Waymo's $5 Billion First-Ever Debt Raise Signals a Robotaxi Land Grab, Not a Science Project](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9BaGt6ckszSmpwTDVsOGUzQ29DXy0yc3BsVFdSTjNtZFZrR3dWYUd5TzcwSTYzUTE3MlVmd3B4UG1iSS1kRHpySXpFVlhRTWd3cjVCOUgwVW5FcWc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-09 [Hyundai delays its in-house autonomous driving solution to 2029](https://news.google.com/rss/articles/CBMilAFBVV95cUxOM1BRRVUzZ21fMHFubEhHNHRGcFVDQTFwdkRMWnljalNhS193bHpKY0dLSUZjN2tXamRlZUZIZ24wdmh5cWE5bnI2MzF4Qm5lVXJlWFZqTXE2TkpFLUZJWExJQWY4RDFuemJJbmZWZ01DMmRoUG9yLUlIZHNnT3RVeHdYR3hMSkk4RlBfcjlHU0R6Mzhn0gGUAUFVX3lxTE4zUFFFVTNnbV8wcW5sSEc0dEZwVUNBMXB2RExaeWNqU2FLX3dsekpjR0tJRmM3a1dqZGVlRkhnbjB2aHlxYTlucjYzMXhCbmVVcmVYVmpNcTZOSkUtRklYTElBZjhEMW56YkluZlZnTUMyZGhQb3ItSUhkc2dPdFV4d1hHeExKSThGUF9yOUdTRHozOGc?oc=5) <sub>Motor Illustrated</sub>
- 📰 2026-10-09 [Pony.ai's Robotaxi Expansion Reaches Middle East and Europe; Goldman Sachs Maintains Buy Rating, Cuts Target Price to HK$202.4](https://news.google.com/rss/articles/CBMidkFVX3lxTE95VG5sWlNSQzI3MjVFNnBoYXVCTHVjNEpUdERqYWxIRVB1U1lGdFFYZ2FqWWdVT0JBZEtrVGxJODhVQ292U2Y4VlBJN09HUmxpZFlkN3dXUXhreFFWenZfcTljNWxVWXRhbC00VUpXNkctTHBXR2c?oc=5) <sub>BigGo Finance</sub>

</details>

<details><summary><b>comma.ai</b> (13)</summary>

- 📰 2026-10-07 [Researchers Find that AI Models Struggle With Even The Most Basic Driving Skills](https://news.google.com/rss/articles/CBMiuwFBVV95cUxNb2ZGRGxGZDNjLWU1OVBPNjUtUlJXR0hiVGV3WEJ1eUVnSWExMWVvRmJjX2NtQm9sX0plMTU3YzZwUm5ZTzVoSGttcXZmQ3BqbW40X2doNFMycUk4UWE3anlidy1vWHNYZndVZjZWLUYtbnlHeVBFRjJOaTF4SWxzbmotR0xsNkVIcEhfZ0M3LUs5R2FyV1lVdlRRU3JwakpQcXpBUzlEOEhsWlB3Q19EdXFhQjRvZDU5MHln?oc=5) <sub>Auto Spies</sub>
- 📰 2026-10-07 [OpenAI's GPT-6 Astra is the only AI model to finish a real-world driving test in a Toyota Corolla](https://news.google.com/rss/articles/CBMifEFVX3lxTE9iZmN2ZFp6blVBRnZUTkYtYTJ3b0hSb0xhQjZyQXh5MUN2T3ladUlEb1F1SWJzc3FtamZtazk4LTVUWVpNX0ZjbGZwMnpERk45TVVQWVA1RjBZVUxxTTAzTWpaV1JqUzIwM1I2Wk1tTzc3bDJpaWluc2JVam4?oc=5) <sub>Crypto Briefing</sub>
- 📰 2026-10-06 [AI Agents Tried to Drive a Corolla, Crashing on 8 of 11 Runs](https://news.google.com/rss/articles/CBMiuAFBVV95cUxONWxQTEZham1kc1J4S2lMNUh6OTN1QWhXbl92U21NUWZTZWhNUUdwcFVvUHYtVWJzSjl4TjlCeFhUY2ppMXd3WkkxaHJFRmFlNUN2NGFSSENnV2ZZYWRNZ3JIUjd0dzFlTS0wR3gtbmxXN3VHOUkxWWg2VVFpTVgzWGN2T3RPdEFJV0cyWjRPSVFyNWZTYjFyX0pzYjFEUWQwLUlfbGo1bm8xVUZXQmpyQ3pCNXV5ZE9x?oc=5) <sub>thetruthaboutcars.com</sub>
- 📰 2026-10-05 [Researchers Discover ChatGPT Can Drive a Car. Grok, on the Other Hand…](https://news.google.com/rss/articles/CBMikgFBVV95cUxNNnNwX0g5bHV4STJlMXNOcXRnYnBHWHNoelViM2pJSzFob3dvUVJIdFlDRDV4X09DSVloZmxCTk5NODd3b3RBR2JmWEJQRktXUTYyWDNveS15UEw0NnVfSFluMlJxZHlBb3NhYnRNdDJsZ01MbVNpOXY4OW9nQnBSYnFRQ1U2YVd3a3R2ZTY4VlJNdw?oc=5) <sub>The Drive</sub>
- 📰 2026-09-30 [A $999 Box Promises Hands-Free Driving. Its Own Code Says ‘THIS IS NOT A PRODUCT.’ Now NHTSA Is Investigating Crashes That Killed Three.](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPNFIyamduTmQxb1dKNlh5Z1hCYUhyemoyU2I2bjFUWjZQSDVFSDFWOGxlM1hnQms4Q1lpalg0bXlCTEZTdVJ3eGtNTjlLamY2eW9LX09IejF6SkJxSmZ2QjRkU1pUczlRY2g3cUZIN3hvSUc3a3pUWHVKVk40MlY3Wk5SX3dnOHBl?oc=5) <sub>Yahoo</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
