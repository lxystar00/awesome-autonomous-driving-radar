# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-10-06 · 1,239 papers tracked · 38 curated.

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
- [End-to-End Driving & Planning](#end-to-end-driving--planning) (9)
- [3DGS / NeRF Reconstruction & Sensor Sim](#3dgs--nerf-reconstruction--sensor-sim) (3)
- [Perception: BEV, Occupancy, 3D Detection, Mapping](#perception-bev-occupancy-3d-detection-mapping) (8)
- [Datasets & Benchmarks](#datasets--benchmarks) (3)
- [Safety, Robustness & Evaluation](#safety-robustness--evaluation) (3)
- [Industry Tracker](#-industry-tracker)

## VLA / VLM for Driving

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Teaching Vision-Language-Action Models What to See and Where to Look](https://arxiv.org/abs/2607.01658)<br><sub>Yuguang Yang, Canyu Chen, Zhewen Tan et al.</sub> | ECCV 2026<br>2026-07<br>📑 1 | [⭐ 31](https://github.com/ShivaTeam/DriveTeach-VLA) | Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving |
| [DeepSight: Long-Horizon World Modeling via Latent States Prediction for End-to-End Autonomous Driving](https://arxiv.org/abs/2605.10564)<br><sub>Lingjun Zhang, Changjie Wu, Linzhe Shi et al.</sub> | ICML 2026<br>2026-05<br>📑 1 | [⭐ 31](https://github.com/hotdogcheesewhite/DeepSight) | End-to-end autonomous driving systems are increasingly integrating Vision-Language Model (VLM) architectures, incorporating text reasoning or visual reasoning to enhance the robustness and accuracy of driving decisions |
| [CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving](https://arxiv.org/abs/2607.04179)<br><sub>Zhaohong Liu, Hao Ye, Xianlin Zhang et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 1](https://github.com/MICLAB-BUPT/CritiqueDriveVLM) | End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving |
| [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)<br><sub>Nan Yang, Zhanwen Liu, Linfeng Zhang et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 3](https://github.com/Zizzzzzzz/MVPruner) | Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings |
| [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)<br><sub>Yuan Gao, Wenting Miao, Mattia Piccinini et al.</sub> | IROS<br>2026-07<br>📑 1 | [⭐ 27](https://github.com/TUM-AVS/Chat2scenic) | Validating autonomous driving systems requires diverse, regulation-compliant test scenarios |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 7 | [⭐ 489](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
| [Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air](https://arxiv.org/abs/2605.31066)<br><sub>Tianle Zeng, Yanci Wen, Xueang Yu et al.</sub> | arXiv<br>2026-05<br>📑 2 | [⭐ 1,109](https://github.com/louiszengCN/CarlaAir) | Recent aerial vision-language-action (VLA) models show promising single-UAV capabilities, such as tracking moving objects and navigating to language-specified landmarks |

## World Models & Generative Simulation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [HERMES++: Toward a Unified Driving World Model for 3D Scene Understanding and Generation](https://arxiv.org/abs/2604.28196)<br><sub>Xin Zhou, Dingkang Liang, Xiwu Chen et al.</sub> | ICCV 2025<br>2026-04<br>📑 4 | [⭐ 71](https://github.com/H-EmbodVis/HERMESV2) | Driving world models serve as a pivotal technology for autonomous driving by simulating environmental dynamics |
| [FrozenDrive: Zero-Shot Text-Guided Driving Scene Generation and Data Augmentation with Parameter-Free Frozen Diffusion Model](https://arxiv.org/abs/2606.20110)<br><sub>Yuhwan Jeong, Hyeonseong Kim, Daehyun We et al.</sub> | ECCV 2026<br>2026-06<br>📑 1 | [⭐ 10](https://github.com/daehyunwe/FrozenDrive) | Synthetic data for autonomous driving is surging, powered by diffusion models that promise scalable scene generation |
| [ASTAD: Asymmetric Style Transfer for Synthetic-to-Real Adaptation in Autonomous Driving](https://arxiv.org/abs/2606.29286)<br><sub>Dingyi Yao, Xinqi Zhang, Lihui Peng et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 1](https://github.com/Dingyi-Yao/ASTAD) | Synthetic data mitigates the data scarcity problem in autonomous driving perception |
| [Is Your Driving World Model an All-Around Player?](https://arxiv.org/abs/2605.10858)<br><sub>Lingdong Kong, Ao Liang, Tianyi Yan et al.</sub> | arXiv<br>2026-05<br>📑 5 | [⭐ 253](https://github.com/worldbench/WorldLens) | Today's driving world models can generate remarkably realistic dash-cam videos, yet no single model excels universally |
| [Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends](https://arxiv.org/abs/2606.01164)<br><sub>Jiuming Liu, Chaojun Ni, Mengmeng Liu et al.</sub> | arXiv<br>2026-06<br>📑 4 | [⭐ 239](https://github.com/liujiuming123/Awesome-Interactive-World-Model) | With rapid development of large language models and diffusion-based content generation, world modeling has attracted increasing research attention, benefiting various downstream domains such as game engines, embodied AI,… |

## End-to-End Driving & Planning

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](https://arxiv.org/abs/2609.26792)<br><sub>Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.</sub> | CoRL 2026<br>2026-09<br>📑 1 | [⭐ 11](https://github.com/VAIL-UCLA/DreamStream) | Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions |
| [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)<br><sub>Shen Zheng, Anurag Ghosh, Gaurav Parmar et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 30](https://github.com/ShenZheng2000/WarpI2I) | Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs) |
| [G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance](https://arxiv.org/abs/2606.26017)<br><sub>Hang Yu, Ye Jin, Alessandro Canevaro et al.</sub> | IROS 2026<br>2026-06<br>📑 4 | [⭐ 6](https://github.com/HangYuu/G2DP) | In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors |
| [Fail2Drive: Benchmarking Closed-Loop Driving Generalization](https://arxiv.org/abs/2604.08535)<br><sub>Simon Gerstenecker, Andreas Geiger, Katrin Renz</sub> | arXiv<br>2026-04<br>📑 15 | [⭐ 173](https://github.com/autonomousvision/fail2drive) | Generalization under distribution shift remains a central bottleneck for closed-loop autonomous driving |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 15 | [⭐ 345](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
| [Latent-Centroid Steering: Single-Pass Classifier-Free Guidance for Command-Aligned Autonomous Driving](https://arxiv.org/abs/2608.00237)<br><sub>Meibo Hu, Jiamian Wang, Pichao Wang et al.</sub> | IROS 2026<br>2026-08 | [⭐ 2](https://github.com/codingmlinprocess/LCS) | Vision-language models (VLMs) have recently emerged as a promising paradigm for end-to-end autonomous driving, enabling agents to map multimodal inputs and high-level navigation instructions directly to executable trajec… |
| [STAGE: STyle-controllable Action GEneration for personalized autonomous driving](https://arxiv.org/abs/2607.29517)<br><sub>Zihao Liu, Xing Liu, Yizhai Zhang et al.</sub> | RA-L<br>2026-07<br>📑 1 | [⭐ 6](https://github.com/CarlDegio/STAGE) | Driving style refers to the behavioral preferences that drivers maintain during driving, shaped by their diverse experiences, habits, and needs, and is typically reflected in varying levels of aggressiveness |
| [DVGT-2: Vision-Geometry-Action Model for Autonomous Driving at Scale](https://arxiv.org/abs/2604.00813)<br><sub>Sicheng Zuo, Zixun Xie, Wenzhao Zheng et al.</sub> | arXiv<br>2026-04<br>📑 11 | [⭐ 366](https://github.com/wzzheng/DVGT) | End-to-end autonomous driving has evolved from the conventional paradigm based on sparse perception into vision-language-action (VLA) models, which focus on learning language descriptions as an auxiliary task to facilita… |
| [A Survey on End-to-End Autonomous Driving Training from the Perspectives of Data, Strategy, and Platform](https://arxiv.org/abs/2610.00926)<br><sub>Chengkai Xu, Yiming Cui, Jiaqi Liu et al.</sub> | arXiv<br>2026-10<br>📑 4 | [⭐ 102](https://github.com/Jiaaqiliu/Awesome-Training-Ecosystem-for-E2E-AD) | Autonomous driving is a cornerstone technology for the future of intelligent transportation, where end-to-end learning has emerged as a transformative paradigm that directly maps multimodal sensory inputs to driving acti… |

## 3DGS / NeRF Reconstruction & Sensor Sim

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DriveWeaver: Point-Conditioned Video Inpainting for Controllable Vehicle Insertion in Autonomous Driving Simulation](https://arxiv.org/abs/2606.31918)<br><sub>Junzhe Jiang, Zipei Ma, Zijie Pan et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 16](https://github.com/LogosRoboticsGroup/DriveWeaver) | A pivotal step in autonomous driving simulation involves inserting foreground vehicles with predefined trajectories into simulated scenes |
| [Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796)<br><sub>Leshu Li, Jie Peng, Yang Zhao</sub> | ICRA<br>2026-06 | [⭐ 12](https://github.com/UMN-ZhaoLab/Pocket-SLAM) | 3D Gaussian Splatting (3DGS) has garnered significant attention in Simultaneous Localization and Mapping (SLAM) due to its advances in capturing fine-grained geometry features and synthesizing novel views |
| [MM-TRELLIS: Point-Cloud Guided Multi-Modal 3D Vehicle Generation in Autonomous Driving](https://arxiv.org/abs/2606.24301)<br><sub>Hongli Xiao, Youjian Zhang, Yucai Bai et al.</sub> | ICRA 2026<br>2026-06 | [⭐ 8](https://github.com/HongliXiao/MM-TRELLIS) | Recovering realistic 3D vehicle models from autonomous driving scenes is crucial for synthesizing training data and building simulation environment |

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

<details><summary><b>Waymo</b> (202)</summary>

- 📝 2026-09-24 [Our Vision for London: How Waymo can Support a Safer, Connected UK Capital](https://waymo.com/blog/2026/09/visionforlondon) <sub>official blog</sub>
- 📝 2026-09-22 [Introducing transit rewards](https://waymo.com/blog/2026/09/transit-rewards) <sub>official blog</sub>
- 📰 2026-10-06 [Waymo recalls 672 driverless vehicles after Phoenix taxi hits utility pole, prompting software and map up](https://news.google.com/rss/articles/CBMiuAJBVV95cUxQUHRlVGJyMF9LbmMtTk1FZFFWYjVXTHRPOV9nYUVxc2pxaDhYOW5QZVowRG5EWDFqUzVqbE1QM3dKQ0lvUnZTZnY2aVQwcFFNWkNEOE5XamtvX09hOFJFUTdISWdvTF90UjhnaG9RT2V4MnZFamI4NG54YWE0dU5rZjVuU0lOcGZYTERIV1FfNFpiZzd4bG9felItaG01VXR5WHo4V3JMMGF5eENVZkxsck4xcEFnWkFnOTdYa0Y0X21Ud2RUQ0lQRTRtaUhEMFp6eGlDMDVnNjBEMTNzZk1PQUdOUF9vRnBGek9LbVhpS25DenktWjk5d2Z2TUw0S25MMmw0bTlHdXZuTVRuaWdlZVdRLUlvSmhoUFVPaDd6ZkQ1b3d6NkFqUFphWXhYSThjS2daT2QwVGXSAb4CQVVfeXFMT096Y1llU3dHU0dUcjNIcGhWUzd1RUJwZm00dWdJa2ViTFZvb2NUVjJ4TmN1YVljajdMNWg5X3dCQlJMNm1ncVdfUGhxbVh5NFh3NHdSTDNGWGdtYnhYQS15QmpyQklHbTR2d0d5VkVNX3RwX2NxMzlwVmJFWFNpZExLQzM2R3h4VHJlNFFycXM0MzM3R3dkdl9Bd3p5SVE3dnFLRXN0NHpWVF9NR19EaDhyVjZQVERWdUtCTjRIbXk1OFFpTVBCelRmcWV6VGc3dGljcXFMTVVLbGpmNWIycnFvUFRiVUVjcm9FemhxbUZtaUQtOEtNTkFiTHpZaHNQalY1R24yemc2SzI2Ui1LRVhPWmtSLXhVMHJZaUdxaHhtdWQwd3JlN2o0N0VncmFEdW8zMVE5aml2U1ZGdXBn?oc=5) <sub>The Times of India</sub>
- 📰 2026-10-06 [Tesla’s Got ‘Waymo’ Problems With Autonomous Driving](https://news.google.com/rss/articles/CBMijAFBVV95cUxQSWRRUXhvM0pxblUyelhvMHd0MjFsTjlvS1hQMklTaDdma3pQMDhCdHpsejItRDB2SXBJSTVTcUNCZVZTMG43b25NdkFIX0x0QmViQkl1TkxiaHRNV0ZSRHBYXzNqZ1NCRzBfbmhkajVYMmhfaWppcHVvTEdDVXJQLWN3V1k5bTBLcHZUYw?oc=5) <sub>Tarmac Life</sub>
- 📰 2026-10-06 [D.C. union leader: Waymo threatens thousands of driving jobs](https://news.google.com/rss/articles/CBMiXkFVX3lxTFAtTm1tcVcwRjdWT3R2ZzZ1VlBubFVvUzRiYXNGd3pXSWVwWXhXcGZaNHRmOVFmaFdHM0NMQ29vUEpFeno0NjdWNzFMWGQ3aWl2a1I5bFhVSXJ4RU1pX3fSAWNBVV95cUxPT0hUS1l2akJCNHNSaUVlVUxJRmlUQlFaTV9KUVRIMFZxMGFCc2NzaFZZd3ZDeE5wNVN6d2FCY3I4MHI3eWpDY2lSMWpOYW5yN1ZRQkhRRWxCTU9NTG9oaDROS1E?oc=5) <sub>FOX 5 DC</sub>

</details>

<details><summary><b>Tesla</b> (295)</summary>

- 📰 2026-10-06 [Tesla reveals early Robotaxi charging strategy, showing scrappy DNA](https://news.google.com/rss/articles/CBMigwFBVV95cUxPTW5oV2dxLVhaWTRrUk1rOXZGZzltdldOeUs4QmJTSG9DM0ZJS1JhNW1MeXJwX1J2R1VwZk9MUmI0c19tb2N1bUpqRVRtU3BKMmhoR3FCMmVST2l2QjFfbkdvMXJZZV93dzljRHUxUDdZLS1Xam9pX0d3ZGhvTTZHMzJPRQ?oc=5) <sub>Teslarati</sub>
- 📰 2026-10-06 [Elon Musk Says Gray Kittens Are Grounding Tesla Robotaxis At Night](https://news.google.com/rss/articles/CBMihAFBVV95cUxQT0U2dHVhOTUxMmVGM2RsWWc5V2QtMGdfS1I5SkVVcDNDaTRiX0FEUXBaSlc2NzZsUVdpemZKanowZWptSVdmakZiRHFZUEVvWUM3M2VNemQ5Tms2V0w4Rm5paWtNRkx6SWh2UFhOM3VjZEpLbkZCdXN3SXhFdXMxcEhiTFc?oc=5) <sub>Motor1.com</sub>
- 📰 2026-10-06 [Tesla robotaxi extends operating hours by 1 hour in Austin; further expansion remains task](https://news.google.com/rss/articles/CBMi0AFBVV95cUxQMWpab185MnNJa2oxU1lBa24zZEFsZzdXMGFNNGtJYURDNjQzaTJVeDZYNWZ0X1ZCU1VHMmdCOU1pOXljY1pGMG5pQXAxaXlrYndLVVJsNnlFTTdqVXRhYl9Tb19zNVN0NF9sbk1oRmg5LWpzZzk5TWtpem55cnB3MFd3bGFRMnNhcWJlQ1BOSHZnLTFBNlRKOWI4bWM4ejRmVlM3VlJUR2dOS2lLbGE3MFQtRklBU0xQYjBQNElhWGhKZzlDVzY5WVNDeVE4VFkt?oc=5) <sub>디지털투데이</sub>
- 📰 2026-10-06 [Tesla lets drivers flee a Supercharger plugged in, but not in Europe](https://news.google.com/rss/articles/CBMikwFBVV95cUxNemRYVWRXaU1ReGlhc2VtTVBXRDBXYU5wTEVtWWFpMzFPMF9jVVUwSmlVYmNtZlZNeFhrOVh6YmVXa2ZaQi1md2pid1BoTkdoNjUwajFMTnJIS25QZkVoR2dDTzlVVERGN0sxT1kxN2YyTFl4RGsyaGRCcWZnV3hSSXhfZEttNFBBeDh4a0hTc0JON2s?oc=5) <sub>autonext.co</sub>
- 📰 2026-10-06 [Calls grow to scrap Tesla's $99-a-month FSD subscription and make it standard](https://news.google.com/rss/articles/CBMivgFBVV95cUxPeHVMZlF2a1lTZGFQbFlGM3JHOVZCTnEzZlF2N2Jkbm9wc1hpclhiNWFKTXRyMnJnaVFkV0J6UEhiUENFQzRNc2xKR1B5eDJfcG5pcGVIN0hBQVd6LWF3UENHRTNlTl9XaVlZZHk3cTEwVHpkM1B5R2dGRFJoclJEd1JKMlJHSEdCeDhJa3ltckhtdUZHLVBsQ1NzdGw3ajJpVGV6VzFVTVZ6Wnpra19ab1kzNVdIWjl2UENYeTV3?oc=5) <sub>디지털투데이</sub>

</details>

<details><summary><b>NVIDIA</b> (199)</summary>

- 📰 2026-10-06 [Hyundai, NVIDIA and LG Advance AI-Defined Vehicle Platform](https://news.google.com/rss/articles/CBMilwFBVV95cUxOMDdrUmZabmFENTZpaEJBZWxYNGxBMEk2OGxCWVFUNEVOb1hWd1ZoeWpHUkIyaE9BelFLajNFa2FZYlNfSkZ2TjY0TFctLVhaR2VKb3p6Q3FlcHEzdVZUTjlkbThoSnRRWXBLTjFLWnp4MEhxdUVvNmJZSU1VbUQ1eW5veTZXb25kTGFSUjRJZTFUS3A1WUdN?oc=5) <sub>konsulteer.com</sub>
- 📰 2026-10-06 [Nvidia's 114-CVE driver bulletin went live reading 'Default Summary' for two days](https://news.google.com/rss/articles/CBMiigFBVV95cUxPd28xWExRaEpmN0EtWmoxYzh0Z3dqc1VQZ1lGYkRLbVprX3RkZEU3cHdFaTJadncwSk81U0EyQWs1UDA0YzNYdG83MUdSR2NzbnZkanNVTTNPdHpMTWFncFNuZFlNWXRGc3hlOXc4ZGdsWXRKangzenFMbXFRNldCcHF3aTI3aWRDZ1E?oc=5) <sub>mixed-news.com</sub>
- 📰 2026-10-06 [Hyundai, Nvidia and LG Form Self-Driving Alliance to Take On Tesla](https://news.google.com/rss/articles/CBMiowFBVV95cUxPbDl0WjBOdTFSUjVHN2tIMG1lYkJsNUFtcVlLdVBubGhTYy1MWjlOdGtsVGRvOUlFWlg3c216cWY5MldxNDhJdnE4blYyV1kyRWI3NVdnaklQNUtKMG8tRk9SbjFjb0NGMVhFNGpwME00UDZ0S3l6bFpvSHJ0TW42V3VSNmNUZ1JVR3pJQjl1dllfMG5KN3ppV1FQUzBvNzhOWm5v?oc=5) <sub>Seoul Economic Daily</sub>
- 📰 2026-10-06 [Nvidia GTX 10 Series Gets Windows XP Support Thanks to New Modded Drivers](https://news.google.com/rss/articles/CBMinwFBVV95cUxNNml1SS1SOXl3OWVqMzhvb2xjX0lXdzdjYktJTVJ4R19GMnJaa2k0QTlzSTBuLUZHX0xkUUVuQUhPWmNfN0ktYmNJY1Q4TjM4V0tlbWdia25tSW9MVk0wcWpuci1rbXMyUkp5dGozaWIxX00xbFRDelRhT2Jqb20wU2VuWWtJZm12dzJXMm0zcEk2bW5lNVpOSWZSbm8tajQ?oc=5) <sub>eTeknix</sub>
- 📰 2026-10-06 [Nvidia’s NVentures Joins Reactor’s $74 Million Funding Round](https://news.google.com/rss/articles/CBMiWEFVX3lxTE0yaXVQQ3BGdWtGRlBWbjhzcUYwRV9mQWM0ZWJqdTNzbnpEdUNTc0ttT0M1ZmFIQk5KX3Z6YWZEWUx5SVVRZFphYTZyRW9yWXZfWXdwcVI3MWw?oc=5) <sub>tokenpost.com</sub>

</details>

<details><summary><b>Wayve</b> (69)</summary>

- 📰 2026-10-05 [Driverless taxis deserve a clear run](https://news.google.com/rss/articles/CBMiowFBVV95cUxNd3FabkJBaUdFd19oSGgwS1NpT3oyWDA0LTItOFlKMmdXOVFNS3VBQnpHbW0tYmFZR0xua0VkZ1hVcDBVTllPQnZTNnpPc3FTODJYbUJuYkJiTjM4c1lMV0FmdFprcHlvY01abW9Pb2RGNVBuclhmZzZaSzZndk1taUdTQ0RraUtZOFliNlpuQUpoWmctVGxzOVZSSTltQ3czSTQw?oc=5) <sub>The Times</sub>
- 📰 2026-10-05 [Volkswagen Picks Britain's Wayve Over Nvidia as Labor Chief Disputes Blume's Account of Contract Cut](https://news.google.com/rss/articles/CBMi1wFBVV95cUxOcThBbDl5ZldUaWFqLXgyWnMzSE52Njc3dmtrdlU0ZWtEbVpNR1Z3X0RLSGVtVThiaV9WSGEzYXYzVFVqZzNJUE0tYzh3S2tEUTBFRE9qUEl3TTJ0bmVRQjFzLWdXTnluemlLYVJyVjEtZExZazJyWHFiNFd5TmNrRExXdGVkekNKd3gxMUQtT2FaNUkwa2RJR2dDWU5sVjAwemNCcjZLbm1NWDc1SkhMYkVUZFZfTFFTTC1PcDNVbjNrc2RvYWwyQU5CUnlpaTcwTVRSQlR6WQ?oc=5) <sub>AD HOC NEWS</sub>
- 📰 2026-10-05 [Volkswagen Selects Wayve for Self Driving Tech Over Nvidia](https://news.google.com/rss/articles/CBMi3AFBVV95cUxNekxNRzIxNGszOUZJSjdfQnRWWWRLVGpDRnIwYUl6U0lLMUxoVFREcW1qSFVTeF9ZNDREUHExX2Y3a25WSkx1LUhxZS10UmxhamhTR0pvUHh4NUx2RHB3b2hESFBBOG5jVElBZERJdGN2RVIwUkdKN254MzJvaWEzdHhMb0NqeWNsZzR4d0pGMDFWTl9SV0hIYm5iblc1cFQ2bjNJRE5aYl9Xb0dlLVNvNjhyZU9lZXhOQUp0b3M1bWdLaTFqMkpYOGxNeGRjaDRQOUREeDBfMV9jZlJl?oc=5) <sub>Fuel Cells Works</sub>
- 📰 2026-10-05 [Volkswagen reportedly selects Wayve for future autonomous driving technology](https://news.google.com/rss/articles/CBMi2wFBVV95cUxOVmFBd1JuSWF6bElKMTRjN29fbHFMdVhTQkZRbHlyTkZoLUVuRVhaU25iUms3UDNnNGRfWWJ6UmtsLWtFdXpJbmZTS3J5T1RtQ2g3Sl9hT29ZWXctdlVrXzhDVUtJT2RuT0c0MVZKMTliMFlBdmVIOUI4OGFtaEN2elNzQUJLMXhvTi1LRTlhaDliaEZyX3BibjlQUEt2VHJWQ2RSbk8zYklXb0s4dWcxbllTOFJtTGNnTXVDbXRwNERDc1JjbUtkYmZ1azNEb1JPcDRZbTFMMEl2RE0?oc=5) <sub>Global Sources</sub>
- 📰 2026-10-05 [Volkswagen Hands Self-Driving Software Reins to Wayve as Model Offensive and Battery Deals Take Shap](https://news.google.com/rss/articles/CBMi3AFBVV95cUxOSGVyMTg1ZHE1R2ItUDlMNWVGUkJBN2pqTFk3STYxOVZCS1RjUHBRMk9zWFd5LXZUNGF1dUI5MGhfYW4tRmVkWW9PNkhacnk0MENteXc5YXozUndSWUdTOUFwZjBtNlNKM1NULTdfZmFHcmVKMkNUT0tUMGNFZ2FkMENtRTB4c1gtQXVWM3FlTzN2TWpxQkE0UFppeTk5c09UWERBNTcySVdfMWlLRUFPNXpIR3Y3OEc1c0RmdHZBa200YWVOYU1XZ1ZpUzNJZUoyX0ZKZnR5bTFwZWhF?oc=5) <sub>AD HOC NEWS</sub>

</details>

<details><summary><b>Momenta</b> (142)</summary>

- 📰 2026-10-06 [【视频】改写合资历史！神龙科技x Momenta！中国智驾反向出海！](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9yVGRXSWF1VGlkQ3FIempTYXBYYk1CTWJ3Ymhuak1EeEhNMlRNem1rNm9VOTNFT3AwQnhpSjgyeG9ZUUc3RFY4SUp0TmNucThudWZTMGl0NEpyVm8?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-06 [带激光雷达的豪华插混SUV哪款好？全新XT5 PHEV与4款智驾车型对比+FAQ\|SUV\|蓝山\|XT5\|R7\|凯迪拉克_新浪新闻](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1KWWpROXU2WG9BVGdvTU5sU01BalgwdEoyOC1MTHVfR2NyQU1ocmVUVWJDYkpkcU1ZbHdqV01HM3o1RllpUjBaTDZzMXNkMlRTX1hJcE1hNllmcHlCV2dV?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-05 [带激光雷达的豪华插混SUV哪款好？5款智驾横评，凯迪拉克全新XT5 PHEV综合盘点+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE00bWpzanVYY3hhQ1RIV3FFaVZ0X1c3VHM5V3YzanVmS0RIQjZmNVN3MW9sVG1ncDN0dlVKcFJ5dFZCQ1RDMlUxTzVMVlp3cWNLZFZDLUJRTklCMTdWV3l0S2Q0QUFjeXB6OE1mUlhxcVp1QQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-05 [新上市的中型插混SUV买哪款？凯迪拉克全新XT5 PHEV与比亚迪唐、领克08等热门车型对比+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE9xMGFNd3hrdlBOb25WLU9hM0h5NlpMM0RfTHNabENUdnpETnlsZlBEVFNaZEtGdnhPNXVwRDcwQXMtdGNWNUNtLVBUWlloY0V3YnlvTlFsRzE0Z21aeXVqQzczd1ZDODUteDZhRXhoTm16UQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-04 [带激光雷达的豪华插混SUV哪款好？全新XT5 PHEV与三款PHEV智驾横评+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE5qQ3RuTmtxSm15d2tjWVhJQkhwODRaejI3UTRpVFV0ekxCWENaaUpqUVBCR2E1WG5IYUFFdmVvbnMxdEIzS0t3LTZNa0RqUGg1SEtnNTRBMFN5VXQ2RkdUWm02NFFjYmZTY2hFYlJVZ2NIdw?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>XPeng</b> (232)</summary>

- 📰 2026-10-06 [周末带娃逛商场，小鹏MONA L03和ID.AURA T6的智驾差距在哪？](https://news.google.com/rss/articles/CBMia0FVX3lxTFAxTmlpTlktYWRqZmsyal9MTkNMQlFpUFZ4bThzdVA4RDhGMmhkYV9LcWkyXzJObzdsanhVcmJwcmpJalRRRmVLVW9tWkd6QU55QTVLSUNjd2p4dDMwSS03MWY3ajlKRG1qRlRJ?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-06 [18-25万价位区间的纯电中大型车三年保值率](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBPck1zb2otd1hhVkFTS3l4OEdVckZmTXpaTTZMVGVQeHFIUFVrNFBPUXQ0NDZCVEdybVUtbEdGT0U2WFpPbVgzdGgwRXpQMzYxNGk3dXMzRGpjT0U?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-06 [2026年了，20W以内的中型纯电SUV怎么选才不后悔](https://news.google.com/rss/articles/CBMiXkFVX3lxTE5PVExZaU9mMTc0UFVWbzNXRGY0X0lGZVpQUkNuNk1WZ1Q3RldKa0dCalYzaGJzWXNhOWhOcmE5cjBLSnZEaHFUT3FHdTE0eWpOV3c0d2lqdGZNQWpqQ0E?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-05 [小鹏G9L 23.18万起，值得买吗？5大核心卖点深度解析+FAQ](https://news.google.com/rss/articles/CBMif0FVX3lxTE11Qy1fbmZCaVA0b21pcDA1QzFiZ1k0MUs5NTB4SGNGSGNGQUF5WjJxTGZ3WlBYVXlPa3M1TGcydFBOSGctWEduWFRBaWFvZ0lyeE1Dc0NXc0NOckh0WjhmVnc2REhkOVE3dUlwZ09hZzMwXzdjb2RYWFg4dTQyRHM?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-05 [Robotaxis acquiring a business case](https://news.google.com/rss/articles/CBMilAFBVV95cUxQdW9ncFVPWGlEZ0l1czRFWHRLWHBrbWFSTGFuQUJOZUotdDJlYWJoLVdvUWd3amxlcjRkb2M3V2kwOWZLMVBfbTlIb1pDN0NvYnJJOXNkUWhJb0dtR05WbW9oeEhaZ2kzOFZpWXByVXJ2cEZ1TUxaTld6WXNyWEgtakNnZ0JBMmZLb3NiSkRmV3hjZTlH?oc=5) <sub>electronicsweekly.com</sub>

</details>

<details><summary><b>Li Auto</b> (169)</summary>

- 📰 2026-10-06 [家用大六座SUV的“全都要”解法：对比理想L8、智己LS8与神行者8谁更懂生活？](https://news.google.com/rss/articles/CBMickFVX3lxTE9LOVVEcXNTZG8tWkRvWmJhcVVseWtxZDg4TktFTjN0MzAxcm53b2Rrb2ZlQ1YtTklJYjgyMnp1d2plS3lQR0pmYnNvRUhmem5SUVR2MmJuenpieG81QTlDamxlbHo3N2V3VEh3Qm42cnotQQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-06 [进入智驾模式都有语音提示吗？实测理想/问界给出3个关键答案+FAQ\|试驾评测\|suv评测\|新能源\|鸿蒙智行\|问界_新浪新闻](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1ZOVd2MVR6ZXYyOERqc0pwbzdwZHItcXZack13YnIwaEs0NEd2TmVPc3ZtbUFmeS1vSFUyOEFIOUFBbkRPZjRadS1pNWtrVWd4NzNRT0xPNzFEWHVhdVRF?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-05 [四车横评领克900、理想L8、智己LS8与神行者8：谁才是30万级家庭全场景真旗舰？](https://news.google.com/rss/articles/CBMickFVX3lxTFBsd0JxLTlfd2wzSWRSQlFQd29OUGhGZlNtc3YtczBjZVlrNVhDRktlc0VKa2h4aG4yNkJPV0JCa3VreUZiZVVZSk1yMzFJSVUwbGo5TmZuRWRITXd4aURwTFFLWTFOWXk5a2R2cXU5RktBdw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-05 [【视频】理想汽车理想L7 2023款 Pro](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5QMGZkckdvdnFwcnAtMGprX2JGVHk0WDl6b2pjQUxCYmJLUWxNT0hucjNPU1VGMmRnNlE3OVAzZ1Q4MjNHSFlFQ1JmYkJTTjNwZGVJRlVuSUJkWUE?oc=5) <sub>车家号</sub>
- 📰 2026-10-05 [碰撞前10米辅助驾驶“消失”，接管窗口再引争议](https://news.google.com/rss/articles/CBMieEFVX3lxTE9QWGw0Q3NENmJ2aXJxU2ZNUFM1ZHhNbFc3UHpMekFJVTFvTUVJdUZKbldibkkybXBxWERFcWlYRjdENHlHWFp3THFPMHBSRXR6Ym4zbEUwVl9EWDNFRDJPOHpLaXVvb1VmVUg3SE1ndXpyWHk3bWY2OQ?oc=5) <sub>新浪财经</sub>

</details>

<details><summary><b>NIO</b> (163)</summary>

- 📰 2026-10-06 [蔚来ES9值得买吗？4.3秒破百+3分钟换电，49.8万起的行政旗舰SUV深度解析+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1pYVppbnA4STB0T1J3VnVucEc0S0dXMXgwcFpvOExDTjd1bEI4YVdFNHFxRU1WVEozSWU0cmpfNklBZVpWdjdlckxYNHBuRndHNVNvTXBRQTB3dzdTbUNB?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-06 [20万级全能纯电SUV，配备蔚来智能三大件，2026款乐道L60适合家用](https://news.google.com/rss/articles/CBMiW0FVX3lxTE90VW00M3RjMEI3VXlLSHNOSF9FQ3BnZ2F6Z2RENk5qSkpLclo1c2ZYUDhYZWo3bUVYcjNqMVhTbWRhalE1a29UR05SWnFVUHNnZUdtN0hFWVlUNGc?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-05 [【视频】新到24年蔚来EC6 75度租电极品一手3万公里](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5JRlBXNUNpTUhEc0JLVl8xZzI2UFp6OHVXUHdZOHhBTXV6MnNyNjJ6ZVZJMVVMdXVWeDF2NkV2ZHQyN2Q2TWw5eFZpYktIcjljMEVmRGI2Sk5PYnc?oc=5) <sub>车家号</sub>
- 📰 2026-10-05 [【视频】蔚来智驾2.0实测：环岛掉头全搞定？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9CdW9aLVVOZ01TR01FT3NFQ0JERVowSmFrLVkzbDQ2R3hlQklpUHBaclFmSkJQQUgxNWtSWG9tOU9Yak1pYnhCM19jVmxJWTdWZGl0c3hjZVJ1cHM?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-05 [2026高端智驾SUV终极之选：问界M9/理想L9/蔚来ES8谁更强？+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE8wUHNveXpRUUVMelVYSjFtc0JzeWJFYXhLTU1TZEpBbkF1eG84Slo5ZkNLMHU3aUFuS1FyUzNfa0F3bTd5QUMwQ2M1czVnXzRzU0xHb2wtWFB3T0FkS05fRUJJOXlxSzVqT29CTG1TWURQZw?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>Huawei</b> (374)</summary>

- 📰 2026-10-06 [Qualcomm to pay Huawei for first time in 5G, AI patent breakthrough](https://news.google.com/rss/articles/CBMiuAFBVV95cUxPUHpkeEFQNElSckZOaHJ2SVgzR090LTJ2MnZoNWUwSGhLM2d1RzdGY2xZSzdvdTVINFVsQlZQelVjYnZ6bzNIMkxCZ0dPU2NjWWpISEhhZC14cnJIZ3VQQnhCWERESnItS0MtUzJhVTZkTDZjY1Qwc1FHWnoybXFkM05waU1TMDlXSlBaZlJ3Ykp6dE5icGV3bF8xSFFDRDR4d0N1aE9ZVkpJZWVCWTFabGtyUVlkREFS?oc=5) <sub>Nikkei Asia</sub>
- 📰 2026-10-06 [HUAWEI Watch GT 7 Series, Watch D3 now up for pre-order in PH](https://news.google.com/rss/articles/CBMic0FVX3lxTE16WnZSNGl0Y2dpbXl0UFNhdU9ub0ZzaHFHUnNzWXZxWXB1YloyaW5mbTJGdXNYNnNQa01EemhoTEhPSHlvOFhjWjdFT1pUR3BCaUtDcjZWdENhVXB4d29fei1rUXpweGhfM1lDdDVzZ0xWelE?oc=5) <sub>speed.ph</sub>
- 📰 2026-10-06 [都是华为乾崑智驾，20-50万有的，十万的星海V6能不能跟上？](https://news.google.com/rss/articles/CBMiggFBVV95cUxPRHMzelktbG5WN0lhV0tPT0NCUl9jYUNlR3ZOeE90WXFJRXIzakVrRHliLXNNU0ZqT2ZqcEVTX2xxTTlOTjU5dnBXUDRyS0JxM1JZeTM0M3dTQXBrTFpCMU1Ha3hlWGwtRTFpaTVrMy1sQzlQRDR0RHJUc0lqSGhPakxR?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-06 [岚图知音1300公里零接管，华为乾崑智驾实测](https://news.google.com/rss/articles/CBMif0FVX3lxTE96ZXRHRnFtN1VSOFlfVUpYRUVXVXJnWTZDeUg5dE1RVF9PcmdnTG1HVkFGeFh4eWN0X3ItR1JTVlllOUw3TEtsUEZFRVp0Mlhaay0wMDlidm13QlJlQ3YxYXp4a2hndGhXTVNzakFWU3dWQmJxZmJNN3JxZVpYMTg?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-06 [极狐阿尔法T7：15万级智驾续航双优SUV](https://news.google.com/rss/articles/CBMiW0FVX3lxTE15TkJfNnZTNFoxTUFkVUVnZ18tc0NzOHhYYzNlRGM1V0lONUF2Qk52dHBwcXY0b3A3Rl8yVXcya2ZLN3JXQnFOaW5RaWZ0SjEtdFp3dEI2a1hGX28?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Baidu Apollo</b> (50)</summary>

- 📰 2026-10-06 [The technology of the robotaxi ...](https://news.google.com/rss/articles/CBMicEFVX3lxTE9TUFYtYVppbE4wZ3B2YWpoSjUxVEFQV1dXNHFYM1VDaXNUSHZWVEtpazdwRDNzcC1ZRU81SGJ3SExCYkJsOTBVV1BBWnc2V185SkNHWDdtRWEyQmN4MU1qQjFmZVQ3V3pKa2szOVZ2ck0?oc=5) <sub>eeNews Europe</sub>
- 📰 2026-10-05 [Robotaxis acquiring a business case](https://news.google.com/rss/articles/CBMilAFBVV95cUxQdW9ncFVPWGlEZ0l1czRFWHRLWHBrbWFSTGFuQUJOZUotdDJlYWJoLVdvUWd3amxlcjRkb2M3V2kwOWZLMVBfbTlIb1pDN0NvYnJJOXNkUWhJb0dtR05WbW9oeEhaZ2kzOFZpWXByVXJ2cEZ1TUxaTld6WXNyWEgtakNnZ0JBMmZLb3NiSkRmV3hjZTlH?oc=5) <sub>electronicsweekly.com</sub>
- 📰 2026-10-05 [#深圳无人驾驶网约车关门打不开#深圳宝安乘坐萝卜快跑无人驾驶初体验在百度地图导航的界面里点打车，看了下萝卜快跑比其他运营商都便宜，干脆就体验了一下。1️⃣首先，上车点不能任选，叫车后会弹出一个你定位附近的地点（通常是主干道路边）让你步行前往上](https://news.google.com/rss/articles/CBMiY0FVX3lxTE9IdGVCVVVGeUY1UTR5bEpHdWZHTTBlcGx2VzJESFlrTVRPN3pJSVdjU3ZLNDdYaFZKaWpNb2dBM3ZPUFRRNUN4NTdzWDRTQ3N5eldIQnE0dVZPYk9PRHRqY3Nydw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-05 [Big tech races to dominate robotaxi as China leads and Korea tests - CHOSUNBIZ](https://news.google.com/rss/articles/CBMiggFBVV95cUxNcm9zSU95S2RkSXJqNWh1Y0dudHBvUElDME4zNUxGT1licVlRUWYyUG1TeEFDZTZsdUhLb1BLSXllRENoRnRRaFYwQ0ZRLWVDREU2UllkdUFqY21ST2tFcHNhR3lDRDdiUXlZcEJrUEdYQU5wV3Zncy1nOHo1Rmp1dUxn0gGWAUFVX3lxTFA5ejcwcnozNzZ4WkFmby1sbGJWNWJGRUNoQnRCYW1FakxYXzRZLXJtc1NxSWZWaXZTZUxGLWJ6aHdsSEl3R04xdGJSZEhxbjh4dlZBdWFEZWN1SVR5MUlWWWtmQTYycldsYlVRSXNTcjN0eThJMGJjZWNJb0pCNndWUE5Oa0hDVXBlOWl1OVFtcjE0LW5vdw?oc=5) <sub>Chosunbiz</sub>
- 📰 2026-10-05 [Robotaxis acquire a business case](https://news.google.com/rss/articles/CBMilAFBVV95cUxQdW9ncFVPWGlEZ0l1czRFWHRLWHBrbWFSTGFuQUJOZUotdDJlYWJoLVdvUWd3amxlcjRkb2M3V2kwOWZLMVBfbTlIb1pDN0NvYnJJOXNkUWhJb0dtR05WbW9oeEhaZ2kzOFZpWXByVXJ2cEZ1TUxaTld6WXNyWEgtakNnZ0JBMmZLb3NiSkRmV3hjZTlH?oc=5) <sub>Electronics Weekly</sub>

</details>

<details><summary><b>Pony.ai</b> (116)</summary>

- 📰 2026-10-06 [Inside Europe’s new robotaxi service: A ride in Verne’s driverless shuttle](https://news.google.com/rss/articles/CBMihwFBVV95cUxNTFNUWGZDWTJ2eklCM0ZpaXFvMGw1bEdYNDJycW9jWGphWnhHenhjZFVvRC1fLXhzTnhWWnFlaUZsWF9qS3ZpdmhPTUNjQ1JmaGFadHY3YlZFaGhiaFA2S0t4RThKbGR5SWg5c054NDdiWlFHWWNCQTR2dWJKdmxqcy1zYk53M0E?oc=5) <sub>Automotive News</sub>
- 📰 2026-10-05 [Pony.ai Unveils L4 Truck as It Courts European Tests](https://news.google.com/rss/articles/CBMihwFBVV95cUxPWnpIQkRyZHVlcS10VS16c2tfRXNteW1rck5JMl9DT2ZaUGh6UWhwRVkwQ0ZyWjVTRkFYWlFjc3o4Xzlhb2JCM2J0a1EzQnVCdVJEcS1sSnJJUUVYSmtINFl0OHB2c3JuTndJZGhtNHdPa1l3TGFsM1JwcktaV1RZc2k5SGdkNHM?oc=5) <sub>streamlinefeed.co.ke</sub>
- 📰 2026-10-05 [深圳乘客被无人驾驶车车门夹手指小马智行称属意外｜即时新闻｜中港台｜on.cc东网](https://news.google.com/rss/articles/CBMijwFBVV95cUxNRUlEYlBCVHU5UjdZZWJNbmlJZi16Y2owR0VOc1VYLVJwUk5kb0Q0T3dPclV3NW1EUVRCX2JZSTc4RE9oWE10eEhqMzVXX3FRNjZPcG04OGxud3dhOG1CZVRtMzVrZDYwT2VuSnAzby1ORGxISWFPUmUyYUU0N3U1czRIUVVicUtVbm1uaFNoVQ?oc=5) <sub>on.cc東網</sub>
- 📰 2026-10-05 [Weekly UAE & Qatar Financial News Roundup \| CSC Financial Launches Operations at DIFC, Qatar Issues $3 Billion Sovereign Bonds](https://news.google.com/rss/articles/CBMiU0FVX3lxTFBVT19uSVRRc01aZ3JiNjlqb1pHTXk5S1NKTzhBOFJuZEVab0hGcVN0Zk5rR3RZMjhudk1VdmxSa2otRWhkZ3RNa1lFRHdBRUpqZjJR?oc=5) <sub>36Kr</sub>
- 📰 2026-10-05 [Robotaxis acquiring a business case](https://news.google.com/rss/articles/CBMilAFBVV95cUxQdW9ncFVPWGlEZ0l1czRFWHRLWHBrbWFSTGFuQUJOZUotdDJlYWJoLVdvUWd3amxlcjRkb2M3V2kwOWZLMVBfbTlIb1pDN0NvYnJJOXNkUWhJb0dtR05WbW9oeEhaZ2kzOFZpWXByVXJ2cEZ1TUxaTld6WXNyWEgtakNnZ0JBMmZLb3NiSkRmV3hjZTlH?oc=5) <sub>electronicsweekly.com</sub>

</details>

<details><summary><b>WeRide</b> (108)</summary>

- 📰 2026-10-06 [部分港股人工智能相关个股延续涨势 傅里叶涨近16%](https://news.google.com/rss/articles/CBMiYEFVX3lxTFAwd3dKYVlMU1ZxM21VUEpGZFBFOUpZeGhBR1VCQmJoQ245RDVIQVZrdUZoTGctYmpBbk93ZmdyYXlXZGs3eXBZLUpkTUhLemF6TGZva2wtam9GaVZIMEMxXw?oc=5) <sub>东方财富</sub>
- 📰 2026-10-05 [Weekly UAE & Qatar Financial News Roundup \| CSC Financial Launches Operations at DIFC, Qatar Issues $3 Billion Sovereign Bonds](https://news.google.com/rss/articles/CBMiU0FVX3lxTFBVT19uSVRRc01aZ3JiNjlqb1pHTXk5S1NKTzhBOFJuZEVab0hGcVN0Zk5rR3RZMjhudk1VdmxSa2otRWhkZ3RNa1lFRHdBRUpqZjJR?oc=5) <sub>36Kr</sub>
- 📰 2026-10-05 [Robotaxis acquiring a business case](https://news.google.com/rss/articles/CBMilAFBVV95cUxQdW9ncFVPWGlEZ0l1czRFWHRLWHBrbWFSTGFuQUJOZUotdDJlYWJoLVdvUWd3amxlcjRkb2M3V2kwOWZLMVBfbTlIb1pDN0NvYnJJOXNkUWhJb0dtR05WbW9oeEhaZ2kzOFZpWXByVXJ2cEZ1TUxaTld6WXNyWEgtakNnZ0JBMmZLb3NiSkRmV3hjZTlH?oc=5) <sub>electronicsweekly.com</sub>
- 📰 2026-10-05 [Robotaxis acquire a business case](https://news.google.com/rss/articles/CBMilAFBVV95cUxQdW9ncFVPWGlEZ0l1czRFWHRLWHBrbWFSTGFuQUJOZUotdDJlYWJoLVdvUWd3amxlcjRkb2M3V2kwOWZLMVBfbTlIb1pDN0NvYnJJOXNkUWhJb0dtR05WbW9oeEhaZ2kzOFZpWXByVXJ2cEZ1TUxaTld6WXNyWEgtakNnZ0JBMmZLb3NiSkRmV3hjZTlH?oc=5) <sub>Electronics Weekly</sub>
- 📰 2026-10-05 [Global Robotaxi Fleet Set to Reach 2M Units by 2035](https://news.google.com/rss/articles/CBMiogFBVV95cUxNMXRqMzNocUlfUGtIM2NuTUgyVXBTRVdocUJTalhVR0VGeXY3OGpMdkdOTE5HM0U0U0o4MGFBbEJGSFVxRlFHRFFYaGlKXy14elR3ci16b2hiRnlrZU8tWTg1VFpIWWlEYkNOOGV4N0pNR3dCWHNpNFlOZVMwN1ZLVm9NTkxxT0dmVVM2NnE1S3RlS1N5WFhnYlhhdjdHbUp0QXc?oc=5) <sub>Electronics For You BUSINESS</sub>

</details>

<details><summary><b>Horizon Robotics</b> (172)</summary>

- 💻 2026-09-29 [HorizonRobotics/Ego4WAM](https://github.com/HorizonRobotics/Ego4WAM) <sub>GitHub</sub>
- 💻 2026-09-24 [HorizonRobotics/CogWAM](https://github.com/HorizonRobotics/CogWAM) <sub>GitHub</sub>
- 📰 2026-10-06 [Hong Kong’s Hermitage Capital stays devoted to top-tier tech stocks](https://news.google.com/rss/articles/CBMiugFBVV95cUxOS083OXVOSFc2QnBOY0hCeG1DSVB4OFhXLWhRSWd1VHlXQ3B0WDZ5eG9DcldFUGNLSmRKYl9DSUlCZm80bVRXM29ScU8xWnNDRndLVDBJcGwtZ1R6QUZQQ2U1WWtSTWZRc21vc2dPZENEYWs5X1J1M1FKWjl4Qmp6cTZjQ011cHA3YjUzRFFOaTc4dzdSR0NfNno5NlVCU3hTdnF4Y2lqVWQ2eXQwb1FCM1kxcWstbENWWlHSAboBQVVfeXFMTktPNzl1TkhXNkJwTmNIQnhtQ0lQeDhYVy1oUUlndVR5V0NwdFg2eXhvQ3JXRVBjS0pkSmJfQ0lJQmZvNG1UVzNvUnFPMVpzQ0Z3S1QwSXBsLWdUekFGUENlNVlrUk1mUXNtb3NnT2RDRGFrOV9SdTNRSlo5eEJqenE2Y0NNdXBwN2I1M0RRTmk3OHc3UkdDXzZ6OTZVQlN4U3ZxeGNpalVkNnl0MG9RQjNZMXFrLWxDVlpR?oc=5) <sub>South China Morning Post</sub>
- 📰 2026-10-06 [越野周末选iCAR V27，城市通勤用小米N70，差别在哪？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1NYUtfLXpOcUZHZ1k5RmtWaXc1eTBhcFpldk13LTViSncwZXVpc1F4ZHd4U0lBdVlBZU1aUnlLR1JlVFZhdFZ4UERnRURjbnpVNzhwTmRzY2lRems?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-06 [【视频】趣驾南川178，天枢领航上车，全新深蓝S05就是假期带娃好搭子](https://news.google.com/rss/articles/CBMiW0FVX3lxTFB5NDJKZ2NWdEN3SkFBcVRWeVdDU3dVZTdQaG1FQ2ZmQ2xYRU9OVjdUcDlYaURndm90NnVQTGJVSl9OUzhoaFR4SXk5Vlk2eGNLcWh6SndXMkJBQ2s?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (25)</summary>

- 📰 2026-10-03 [赛豆科技首款车型—AIVA ME7正式首发，采用时下流行的轿跑SUV造型比例，并且配备大尺寸的轮圈与多活塞卡钳，车尾还配备镂空扰流板，预计是一台主打年轻运动的产品。结合此前的消息，这款车会融合豆包大模型以及火山引擎生态，并且有报道称其辅助驾驶将采](https://news.google.com/rss/articles/CBMiY0FVX3lxTE4tU1hIOTd3MWtGSUV0RjZPR3pKRTNVTGNzaXpkenphcG5FVk1pNnZZMGdIUy1TVi1SMW9JdV9KMjFPYXlqakw3MmhObmtMZVB2VlVob2RoaFJTcVFsU09OTnFVNA?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-03 [提供豆包大模型将覆盖20万元以上主流市场AIVA ME7全球首秀_热点推荐](https://news.google.com/rss/articles/CBMiYEFVX3lxTE83MUJRVjJpdG92N0xFSUpkdHlsMWdWQlpaWE1CYzQwblNiOFVMVURPRFZ0amZQTXNpdl9odkpOSk9SZVAyWDhadnBXbWozTHNjOXNkRmRRS2dXbV9BQndHMg?oc=5) <sub>证券之星</sub>
- 📰 2026-10-03 [又一AI原生车！AIVA品牌首车ME7全球首秀，量产或假以时日](https://news.google.com/rss/articles/CBMiW0FVX3lxTFA2cVdGVzNJZlBpODJxZXJnVlVaOXFjQ3gzcTRUOHhibHZ3VlAtYWIyWnFHQmRPbUdFd2lsWGtPLXpfRTZoMGhOcF96am1CeklVUnRTS0RFZkpEZ2s?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-03 [你的国庆自驾搭子来咯🥁！无论是堵车、窄路、复杂路口，还是泊车，小元都陪你轻松出发，安全抵达。#元戎启行DeepRoute ##DeepRouteIO##辅助驾驶##物理AI##国庆节##自驾游](https://news.google.com/rss/articles/CBMiY0FVX3lxTE9oQzI1QkRUaU5jRDFaR1QxMzBmVDRZSkVXb0FuWkJfUzN0MEh5NDZSVEhCR2hjUzhUdldrTkhEelNlZ0JPTE9SWEhaOXRHNi1rZ1hBQUNOWElJWF9fV3c5aHh3RQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-03 [AIVA ME7巴黎首秀，赛力斯这次想讲一个不一样的“AI故事”](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5wS2JvX2l0SXI2ODdxd1g3T09YeUNtRGlJRG9KTkhXU1VEOUtmZkcyNWdCamhKd2pLR1JEekxDV1ZTeWwxa3FmOHo3RDFMNkFTb1RJNzN6SnctMjA?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Mobileye</b> (21)</summary>

- 📰 2026-10-05 [Moia’s autonomous shuttles start first passenger tests](https://news.google.com/rss/articles/CBMilgFBVV95cUxPaXBLWlk2ckZabm9UeXdOV1lCZTRjaDBkVmk4bDNVRWVMZkxKUEVTOVBqZERzWGlySkROdEs0bkE3SURjaG44c1Y4M3lsM0NmSG95X0diNlY4cGJoMUp1UUMxVnFkQ2Y0UTR2UDdtdTFzczBDSHpId3ZmWDltWlY3Ulg1bHBYMzJweHhDOWkzd3lyVWwxSGc?oc=5) <sub>electrive.com</sub>
- 📰 2026-10-03 [We Found Atoms, Rode Wayve and Watched Uber’s Autonomy Clock Speed Up｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1QZjNLZlpHR2ZtcHFaUDF5bEE3ZktHQlNoN0E1amxaVEg0eUdQbElIVlVVZk1JdTlqZG1kbGZYVTBvZDdKRDRKVWlqa2dRNDF3aTN4dEpmdTdxX0dTVnlj?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-03 [What Mobileye Global (MBLY) Could Not Prove Before The 49% Fall](https://news.google.com/rss/articles/CBMi0wFBVV95cUxOTDFoVXlyNjVvYmJycldRVUhaOHNieXV1MGJlRDVWWlVmUXVPMUY5NUlHWV9PcTYyYlMxWGNxRXk2c3R6b293RThGVW9ONFBBaUtqSkJsRl9MNjRvVVAxRW1WdGdrUXRKaDJqS042RDBXODB5YkoteU5USVlhdlBfS3pGcnlpVzZ0al90dm51WndmSGNCSElQWE9JY3hHaVJhMFZTSGpSMDVuWGQ2ZWtDQVlxVUFHeHJRVFJNclNaS2RLR3RsQnZ1c05rQjZseGhSVzVj0gHYAUFVX3lxTE9LbTQwSTVOazZ1ZkxtRXhjdm5qSjluZjlEandjc3JUdWNkRGdwbGpYdmhNM0NIYlRrQjlMdnI4ZWZGM2FHOUV6SHF2TnJJMDlWTktBWEluVnVQZ2FFYU5WMUF4WS0zSXRmbkRDQzEyVmFUNmJzTFZwTzZDVEFIcXZVd3BLZUFHa1daeDdBako4ZFVseEVsSzE4UURFSmQ0Mnl4V01HZHdybXlFNXFIelVJMURQNC1GNVJKSXgzMTkxenhxLVB0dFlxc1FJLTBzMmh2UzJjaVhKMQ?oc=5) <sub>Simply Wall Street</sub>
- 📰 2026-10-03 [Grayson Brulte: Zoox Has an Intersection Problem, and Uber Has 18 Months to Own Its Autonomy Stack](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9Gbmp2RTY3bW1WaFdrMDhqeWVpUHR0WXNEcFA2eWk4Ukdidmx4bXp4ZmdoNFhUWGZoM2pTNVBCVUlJSUl4SVM0UlcwbERnMTNVYmlxTjlxYXBwV0k?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-02 [Mobileye Global Sees ADAS Momentum, Eyes Porsche Launch and Robotaxi Expansion](https://news.google.com/rss/articles/CBMi0wFBVV95cUxQYzRBUnBoMFNxTkNkYjFDNl9YbVpSRTVwb1N5SjFjMm56dEFiS0I2amZUQ1JqMHFTTlJHb2N2bkhlUXhOaTRpbHJIWWxhWWVBeUxsdlZ1bUtTdzRsZEUzV2NHWUpaVnN2ZzljWnhZSnlibjNHNjE5M1pyc21xekJGM1A3Z3V0SGZRVTVGSG1hMm9DWVlnSUhBQ3hKNk9yQjBZUU12bXN3MUFWc3k1XzZKXzZIeGh5bEVZaXpta3cwMjVHUGxlaHRINGhKdnhERU12TkRN?oc=5) <sub>MarketBeat</sub>

</details>

<details><summary><b>Aurora</b> (53)</summary>

- 📰 2026-10-05 [Ready for Driverless Trucks? I Took a Ride in Kodiak’s Autonomous Semi](https://news.google.com/rss/articles/CBMiiAFBVV95cUxONWtkOXlmSG5HRnlSYU5IZ25QYnMzb2JfRDloYkZuWTJmY2EzX0NrUy11dF8ybng5a2VVSFdxZHJnOFNxbHdQQWdKVkUtckMweHpVUkw2cTBxZkhkSEFyLUI0cWl0a0FxOTV4WFFsX1VyQVBRcVp4TWtZYmY3bkp0SXVFNmI2UlRN?oc=5) <sub>CNET</sub>
- 📰 2026-10-05 [Another autonomous trucking company hits the road between Houston and Dallas](https://news.google.com/rss/articles/CBMilgFBVV95cUxOQ2tLdXlkSUVHNFhBQ0lZV0VRamJDWGdLVDkxeEVsYkh6aXBmSW41ZkQ4VFQ0bVZqbEFWM1NjSVFBOHNBT0s2TGNDX3l5X1M4ODZNRktxcjFfT25DZkhZS1JJQzJUYXZ0V2tNYjRQUm9LWEsxbEpmOUhQSE5HcFFzanpWZkJ3NTM2X1pTWWNsZTM4cU9ldXc?oc=5) <sub>Axios</sub>
- 📰 2026-10-05 [Truck Accident Lawyer Explains Liability as Self-Driving Big Rigs Hit California Highways](https://news.google.com/rss/articles/CBMi2wFBVV95cUxNRzdPUGxqemFTV3hhMmlpSXB3cXNxS29LdkFZcXVTQ1ZXdDRqR1VPTkdsaTc4LTU0djIyb2xPMEoxLURYQ25zQWhxRGp5SmVKTThaUEpkeXlUclQ0Mkk4dG9iaDIzSGQwNWFPRTI1dDVsa2FMTFRkbEJhRms5WGZ5QlQwc2pjbDNrZ0VpX3pVZG1ZRXRJcHh0Zmg4Y2Nra1k0QXpvQXBPVnhtaXpkdDl5dmJ3dHBjaVcxb2p4M1NXaXZxeE5vNEpiTVhOajRkV1RUaUg2bWxlOVJhdmM?oc=5) <sub>24-7 Press Release</sub>
- 📰 2026-10-05 [Volvo, Waabi Launch Autonomous Freight Runs From Dallas To Houston](https://news.google.com/rss/articles/CBMingFBVV95cUxQSVJNREZabFlHQzFRdk5IM0MzUTNTOVkwU0xMWXVkaUdTV2lPN3FTamZELTRvZ3dUX0lHNzZEZk5jN0FpaUJEcFpWeHdaQnB5NjlXdjdMZGlmZHpTUXB2ZXROcmR6U0NZNnhweGhMS2loaVRORlA5ckgyeWVfbjVkVlhMLWkyUXF0OGJwVjN6NXh1X2pxdkJLd3MxYUFWZw?oc=5) <sub>Dallas Express</sub>
- 📰 2026-10-05 [Volvo and Waabi Trucks Start Hauling Freight on Dallas-Houston Corridor](https://news.google.com/rss/articles/CBMiowFBVV95cUxNbUNPS0Y5TEg4RVFBZ0d2eWJ3eDMtRWdyUm9yU09uaXV4a1Qxd0JlUG5zVW14RVlkWXFncXFNMW9UZVA1NWZwMGZGWUhrM2t4TkRSRVpFY0RtZFpnUFJabzJfdThablNJTjZGYnN4bnVjZkdkbllyR285R29IdTEzNk94dFdHS3pqTVBYdVNBSS1LVHEzU3ZmS3I0cU85YUVROUpj?oc=5) <sub>Hoodline</sub>

</details>

<details><summary><b>Zoox</b> (89)</summary>

- 📰 2026-10-05 [Americans are warming up to the idea of autonomous vehicles, survey finds](https://news.google.com/rss/articles/CBMimgFBVV95cUxOYno5eTJlb1ZKb2ZuaUFTRUJlbjNCN2NDMzFwcFlmQ3BrVTZ1b2NWV3ZBM2hNb282MVNNYkdac2w4cTV3YkFkQ0pXUUR0c0FENDhnOEUzZjBJZVB5RWxfdnZlcXJXY0RGY2wzTms2MWVEbVQxUXNfTEhRekg3VFQ0ZjJHbGVMeTl0THJ0V25YREVESUVERjRXdUpB?oc=5) <sub>marketplace.org</sub>
- 📰 2026-10-05 [As robotaxi accidents increase in L.A., the data reveal the safer driver](https://news.google.com/rss/articles/CBMipgFBVV95cUxPYktYa2piUzVWSjdlZnc5ODAtd0NvOVh1WlZsQzJIdmstV0paQXp0U1FiLXI1LTJvWEYxaWlmNGcyNWRuc3BrV0xfWVg1RUU1d1U2SHRRVTcwYVowY19CSHg3a25fcG5hUFE4cEd2Qm5wMm0xRjgyeFV5ZTVFUW5tMDNXcmlXMFFaQmFOMDlhOXdDMldnUFowZVowZjRHaXViYkZWTWpR?oc=5) <sub>Los Angeles Times</sub>
- 📰 2026-10-05 [More robotaxis, more crashes: A dive into data](https://news.google.com/rss/articles/CBMif0FVX3lxTE1fWXcwd0FUb1VCbDNnN2ZfeU5IZWJrd004YjVYMVdVNkh4OGFfQk0xX3J0cjE0WVZrUURTUlU4eFE2bUJTRnBBODZveVFIcWE2WjUzYXJrVDliR0g3cVFpOWJQMjZvMXc1QnBrVW8xMlFvcDJIQXpOM2lwa2NUYUU?oc=5) <sub>PressReader</sub>
- 📰 2026-10-05 [Robotaxis reshape mobility as big tech races globally and Korea emerges testbed - CHOSUNBIZ](https://news.google.com/rss/articles/CBMilgFBVV95cUxQOXo3MHJ6Mzc2eFpBZm8tbGxiVjViRkVDaEJ0QmFtRWpMWF80WS1ybXNTcUlmVml2U2VMRi1iemh3bEhJd0dOMXRiUmRIcW44eHZWQXVhRGVjdUlUeTFJVllrZkE2MnJXbGJVUUlzU3IzdHk4STBiY2VjSW9KQjZ3VlBOTmtIQ1VwZTlpdTlRbXIxNC1ub3fSAZYBQVVfeXFMUDl6NzByejM3NnhaQWZvLWxsYlY1YkZFQ2hCdEJhbUVqTFhfNFktcm1zU3FJZlZpdlNlTEYtYnpod2xISXdHTjF0YlJkSHFuOHh2VkF1YURlY3VJVHkxSVZZa2ZBNjJyV2xiVVFJc1NyM3R5OEkwYmNlY0lvSkI2d1ZQTk5rSENVcGU5aXU5UW1yMTQtbm93?oc=5) <sub>Chosunbiz</sub>
- 📰 2026-10-04 [Here's How Zoox's Robotaxi Safety Testing Will Work](https://news.google.com/rss/articles/CBMifEFVX3lxTFB0OXRqRHVQaDRiQ1FGU3NrUE5UVmRIQXFrSDV2X05KTEowTlZGQnl3QmptaThGQkg1NmdhUFZjUndSbmxRQThCQzRTLUtCWjlSRW15WmM2YzRYZTZxWTd5OFpxNWZ4dVJTajVrX1QwSk02ZU1NU2tXQzJhZV8?oc=5) <sub>InsideEVs</sub>

</details>

<details><summary><b>Motional</b> (34)</summary>

- 📰 2026-10-05 [Nvidia Shield TV Pro Price Jumps 50% to $299.99 Amid Component Shortage](https://news.google.com/rss/articles/CBMidkFVX3lxTE1TVG56dXRydHllMGxNMzhOZU9QVTRjOGZwZWEzakwwQW1QZFE0b0ExX3VUYzBNVmZTVzlrQmpyT2M3cUtjb3BwbmhGczVmMk5jT2k3SUN6dEp3R1FsTEFVN095TlJBZC1QbFdiNHNBckdTQ25lRFE?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-05 [Big tech races to dominate robotaxi as China leads and Korea tests - CHOSUNBIZ](https://news.google.com/rss/articles/CBMiggFBVV95cUxNcm9zSU95S2RkSXJqNWh1Y0dudHBvUElDME4zNUxGT1licVlRUWYyUG1TeEFDZTZsdUhLb1BLSXllRENoRnRRaFYwQ0ZRLWVDREU2UllkdUFqY21ST2tFcHNhR3lDRDdiUXlZcEJrUEdYQU5wV3Zncy1nOHo1Rmp1dUxn0gGWAUFVX3lxTFA5ejcwcnozNzZ4WkFmby1sbGJWNWJGRUNoQnRCYW1FakxYXzRZLXJtc1NxSWZWaXZTZUxGLWJ6aHdsSEl3R04xdGJSZEhxbjh4dlZBdWFEZWN1SVR5MUlWWWtmQTYycldsYlVRSXNTcjN0eThJMGJjZWNJb0pCNndWUE5Oa0hDVXBlOWl1OVFtcjE0LW5vdw?oc=5) <sub>Chosunbiz</sub>
- 📰 2026-10-05 [Wikimedia Says Rogue OpenAI Agents May Have Caused Data Service Outage](https://news.google.com/rss/articles/CBMidkFVX3lxTE40TzM0aUt6V0hkU0w0eHlERGlnX1lkZ0pBWnlHc0pjNlB4Slc4R2FsMUFjMXM0c0dZZHJaVHJScUNqdEFtVHg0STdpOUhpR0dWblpyc2ljSzd1RlBZNWVDanNydHprbXZLaUJsaTA5bnVNVWRpbUE?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-05 [Ethereum Staking Withdrawal Queue Hits 780,000 ETH Amid MetaMask Validator Exodus](https://news.google.com/rss/articles/CBMidkFVX3lxTE95cklqd3ZTbnJmdHJVRENLeGVSa0hPZExHd3BsTjBVNDdjUnduZEtHSHhxQV9sVjMzdnhLejFWVi01elEwV3VGUjRHMUV1Q1FMYzBNWlNETEU0OExwc2lKb2tSMUxpWDFLVzUyTW94NGVkZ25Qamc?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-04 [Hyundai’s New Santa Fe Will Go Electric And Keep The Gas Tank](https://news.google.com/rss/articles/CBMigAFBVV95cUxNSDNOMnY2NUhDeC1FT01Hc0IxMDVGT1BiZkNhSnlybThvN2k5MkpfR3NaSG94ZmN3ZE1YSHlkNjcycU9FVktZRnZmdXBoMFJwcU16R1lPOEZlQUhLTFNWV3gxekQ2eFlaOTBWUmpjRy0xTURiOUU0bTZPLXA5TDNWUQ?oc=5) <sub>InsideEVs</sub>

</details>

<details><summary><b>comma.ai</b> (45)</summary>

- 📰 2026-10-05 [Researchers Discover ChatGPT Can Drive a Car. Grok, on the Other Hand…](https://news.google.com/rss/articles/CBMikgFBVV95cUxNNnNwX0g5bHV4STJlMXNOcXRnYnBHWHNoelViM2pJSzFob3dvUVJIdFlDRDV4X09DSVloZmxCTk5NODd3b3RBR2JmWEJQRktXUTYyWDNveS15UEw0NnVfSFluMlJxZHlBb3NhYnRNdDJsZ01MbVNpOXY4OW9nQnBSYnFRQ1U2YVd3a3R2ZTY4VlJNdw?oc=5) <sub>The Drive</sub>
- 📰 2026-09-30 [A $999 Box Promises Hands-Free Driving. Its Own Code Says ‘THIS IS NOT A PRODUCT.’ Now NHTSA Is Investigating Crashes That Killed Three.](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPNFIyamduTmQxb1dKNlh5Z1hCYUhyemoyU2I2bjFUWjZQSDVFSDFWOGxlM1hnQms4Q1lpalg0bXlCTEZTdVJ3eGtNTjlLamY2eW9LX09IejF6SkJxSmZ2QjRkU1pUczlRY2g3cUZIN3hvSUc3a3pUWHVKVk40MlY3Wk5SX3dnOHBl?oc=5) <sub>Yahoo</sub>
- 📰 2026-09-30 [The $999 Driving Gadget That Just Landed In Federal Crosshairs](https://news.google.com/rss/articles/CBMicEFVX3lxTE5kRFFmYXdUcmRRZ2wtNzF4QlRqQ0o1UmVscVhPWFlsVVE3S1dRVWdtLWFsOFJYeUlHY3phaWZYejBnWjFvVmxTcEJNRVBaQUJscU1VODZvRmxrREVYRDUyZlNJdTNsMUN4MmkwYXY1TWs?oc=5) <sub>HotCars</sub>
- 📰 2026-09-30 [Federal Probe Opens Into Aftermarket Self-Driving Hardware After Three Deaths](https://news.google.com/rss/articles/CBMiqgFBVV95cUxObDZzR1Z3QnZLaDR0bTRldUFvc0ZESTBoUHIyZE1PSmJHWFR4MmdrTi0zWkRFT250VG5WbTNuTWd4dzV6R1FIYzV2NzI2NGlfMzkwdHBTZFdIYkxpNG9pWldBQjdxTF9OOTFiZ1M2RlVfaFlkNThCRk41c21ZcXRsalFfOXpqTXRhYVRhaVREaFRRamMzcE41TGNMVTA5azFDWWxCalpHNkdCUQ?oc=5) <sub>Gadget Review</sub>
- 📰 2026-09-29 [US auto regulator closes airbag defect petition in about 807,000 Honda Odyssey cars](https://news.google.com/rss/articles/CBMigAFBVV95cUxPbllOY01DRVNHZUd5dXR2MXJDc0N1bXdVS2V2V3BzX0NqdmxORnl1cm9PU25FSU9YX2xyajJVNEVwdXFjZFM4eHQzX1ZmeHVTR3lyTVpnNlRna0dXMThiR1A5TGdseEtJTDUyQzVqN25nMUV3MVdYWVExMHlQZTFPWQ?oc=5) <sub>AOL.com</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
