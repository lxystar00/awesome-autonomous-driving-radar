# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-10-04 · 1,228 papers tracked · 37 curated.

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
- [End-to-End Driving & Planning](#end-to-end-driving--planning) (8)
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
| [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)<br><sub>Shen Zheng, Anurag Ghosh, Gaurav Parmar et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 31](https://github.com/ShenZheng2000/WarpI2I) | Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs) |
| [G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance](https://arxiv.org/abs/2606.26017)<br><sub>Hang Yu, Ye Jin, Alessandro Canevaro et al.</sub> | IROS 2026<br>2026-06<br>📑 4 | [⭐ 6](https://github.com/HangYuu/G2DP) | In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors |
| [Fail2Drive: Benchmarking Closed-Loop Driving Generalization](https://arxiv.org/abs/2604.08535)<br><sub>Simon Gerstenecker, Andreas Geiger, Katrin Renz</sub> | arXiv<br>2026-04<br>📑 15 | [⭐ 173](https://github.com/autonomousvision/fail2drive) | Generalization under distribution shift remains a central bottleneck for closed-loop autonomous driving |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 15 | [⭐ 344](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
| [Latent-Centroid Steering: Single-Pass Classifier-Free Guidance for Command-Aligned Autonomous Driving](https://arxiv.org/abs/2608.00237)<br><sub>Meibo Hu, Jiamian Wang, Pichao Wang et al.</sub> | IROS 2026<br>2026-08 | [⭐ 2](https://github.com/codingmlinprocess/LCS) | Vision-language models (VLMs) have recently emerged as a promising paradigm for end-to-end autonomous driving, enabling agents to map multimodal inputs and high-level navigation instructions directly to executable trajec… |
| [STAGE: STyle-controllable Action GEneration for personalized autonomous driving](https://arxiv.org/abs/2607.29517)<br><sub>Zihao Liu, Xing Liu, Yizhai Zhang et al.</sub> | RA-L<br>2026-07<br>📑 1 | [⭐ 6](https://github.com/CarlDegio/STAGE) | Driving style refers to the behavioral preferences that drivers maintain during driving, shaped by their diverse experiences, habits, and needs, and is typically reflected in varying levels of aggressiveness |
| [DVGT-2: Vision-Geometry-Action Model for Autonomous Driving at Scale](https://arxiv.org/abs/2604.00813)<br><sub>Sicheng Zuo, Zixun Xie, Wenzhao Zheng et al.</sub> | arXiv<br>2026-04<br>📑 11 | [⭐ 366](https://github.com/wzzheng/DVGT) | End-to-end autonomous driving has evolved from the conventional paradigm based on sparse perception into vision-language-action (VLA) models, which focus on learning language descriptions as an auxiliary task to facilita… |

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

<details><summary><b>Waymo</b> (168)</summary>

- 📝 2026-09-24 [Our Vision for London: How Waymo can Support a Safer, Connected UK Capital](https://waymo.com/blog/2026/09/visionforlondon) <sub>official blog</sub>
- 📝 2026-09-22 [Introducing transit rewards](https://waymo.com/blog/2026/09/transit-rewards) <sub>official blog</sub>
- 📰 2026-10-04 [California law sets fines for robotaxis that impede 911 response](https://news.google.com/rss/articles/CBMijgFBVV95cUxPblpMZUNYcmctTEJOOUVKT21YdEFDZ2FnNDdqX1FHOVpFY283ODV1ZlNaLTBqRkMybDhfNjJ3UVlFVlpSa1pkYlpQdkNIdUQxSGdUZGo4ZG00SVZnRF9kMGRmUmVJLWpNRXpaTm9WR3BCZTBjYndOQ2g3QVpsaHRfenVyVUhhSVlFOEZqSEF3?oc=5) <sub>Mashable</sub>
- 📰 2026-10-04 [Tesla's Cybercab stumbles out of the gate in Austin: 45 vehicles at launch underscore Robotaxi expansion anxiety](https://news.google.com/rss/articles/CBMidkFVX3lxTFBjaTBpc3IzeGtISjF3ckRHaTFHTlJJaTYyenVTTWQtVzBWNDdmOVBPYjVUYWFaa2NtQjlYZlppb3hWd1hfc1ZwSEplYTdhMm5Icld0Mk1vWWVHQXE0ODdEbjJVOGRrRDlBNFJXdF9WRDItbDY0NVE?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-03 [Blue state councilman mocked after claiming self-driving cars are 'murdering' pets: 'Hide your cats'](https://news.google.com/rss/articles/CBMiugFBVV95cUxNX1E4WEVrR2Z3RFlNR0RxRUVsbVZ3QzdsVEdiM3JNak9SaWswLU1GX1lEamlON0pWd196eDMwRlB1eGx6b1pZU3V4dWRxNV8wbGdTN29BeXJQLXotZmVjRlFKTGFvUmIxSmlRVl9VVkptSlhqbDJXazlTbXpZb29WWk5TQjZpTHRKOC1GSmZrLUNpLTN2MC1yYXRjQUhoem5yM1Uzd0w3eFJLRmhBc3M3WWhUbjZUbENXc0HSAb8BQVVfeXFMT3pPSWY3blF0UXRleDJPMWNhNTBFeWZLN1p0UXAtbGRoaUthNnFUdVZPRGtkWDRsNWhIQktwVEZTSlk2OWtmbjV4Ry0zNzZ2Y2xvTTlwNUlvYTdpcTY3UlBXQ281UDBfRzBEUHBNSGRoMHdZdzlReDdSOU9JbVU4UXh4V0hVTkk0ZGJMeGtrU3A0cFcyckluOWs3ek9fR190d2c5RE9tRkQ1U0R3Zk04TlpfdVBpZTVkUVZ3WXdvUlE?oc=5) <sub>Fox News</sub>

</details>

<details><summary><b>Tesla</b> (268)</summary>

- 📰 2026-10-04 [Tesla FSD Feels Like Magic: What Musk Actually Means](https://news.google.com/rss/articles/CBMijwFBVV95cUxQcEMwVkJITzV5NU95aFAwaEZycGhKSTNwNnZoRjMwZFFFa1l3aV80bENONXlPRlZ2bnk4djhDcDF5SmdNZWZHYzY3VjZKMDMxd0hwMkoyQnlnSFZGYVJfNG9mMWNiNEJta2ZfNHZpa0Y0Rmg5SWwySmZQM21tSFpJa1lvWGhCSmFZRS1mN1NXRQ?oc=5) <sub>BASENOR</sub>
- 📰 2026-10-04 [Footage shows Tesla detecting a hazard well before its driver as its Full Self-Driving mode shows off its impressive capabilities](https://news.google.com/rss/articles/CBMifkFVX3lxTE5MQUdzbWxoRmxsWUhJWlg3Um9qazZ4UXItbkc0dFhGX0MzX2FaeVBWLUIwQl9KVlJPVUpfbDM0TFhkbjc2cTVSY3FReHUxMHZnUDBheDlyRVJGX1NUZVBMdEJ6ekhoTUtOa0luYXZ2VTdOU2dBVmh2WnpZME40QQ?oc=5) <sub>supercarblondie.com</sub>
- 📰 2026-10-04 [Tesla's Cybercab Hits an NHTSA Probe Just Hours Into Its Austin Launch](https://news.google.com/rss/articles/CBMingFBVV95cUxOMkZDMGJqYmpUZjZLQTA1eUoydE42VlF0NUttVlJSZkxFb1RDZm8xT2lJUkw4czVaVUpQWFBJcVNnUE5oYUlOR2V1V01oaDJtcTAxdVB3S0xVbFVQZkJqUlZqRjkwNVh6eEFxZWcyeFBfSXZQU3pIU2ZtMnZ6cTRJRnhwbUNwTWtiQlhYWTZuekdzOGc5Q0FkRmhpRjN6UQ?oc=5) <sub>Startup Fortune</sub>
- 📰 2026-10-04 [Tesla's Cybercab stumbles out of the gate in Austin: 45 vehicles at launch underscore Robotaxi expansion anxiety](https://news.google.com/rss/articles/CBMidkFVX3lxTFBjaTBpc3IzeGtISjF3ckRHaTFHTlJJaTYyenVTTWQtVzBWNDdmOVBPYjVUYWFaa2NtQjlYZlppb3hWd1hfc1ZwSEplYTdhMm5Icld0Mk1vWWVHQXE0ODdEbjJVOGRrRDlBNFJXdF9WRDItbDY0NVE?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-04 [Tesla FSD's Automatic Collision Evasion: What Ashok Says It Can Do](https://news.google.com/rss/articles/CBMioAFBVV95cUxOT19pX2lBV3dncE9BTUpKbDdBbFJ0THBwcUtMM2dzZEVlM0RIa0JjcHZzMlF1NUdoSlZMNEF1VnlQT1k1bHQyanhIRnlXUzVxUk56WG1UYXRSS0o3TW1iajJ5OHg0dE0ya3lCNUMxZC1jNHl2bnFPbGNGWWFmRXk5Tktqelo2bWNVUDlDb1VOc19VX1ZkSjhOQmYzUkg3aVVV?oc=5) <sub>BASENOR</sub>

</details>

<details><summary><b>NVIDIA</b> (173)</summary>

- 📰 2026-10-03 [Nvidia patched 114 GPU driver flaws on September 30, and one is rated 9.9](https://news.google.com/rss/articles/CBMikgFBVV95cUxQUEVjZnQ2dkFQcjlZVVJuVE93NGJYQ0tqaDI2TTBBVXg0Zm55c0RzMDFwRWRWT2JtN0xyN0J3dXdvcHpoX1d1TlBRWkJLRU1uOVFzTHAxS2FHV1RuZmZ6cDM4REUtZUx6NF9xU3hYTGljQmlFdU4xazNqYVd3Sy01bnBnX0U4VW1Yanp1RG51TUNDQQ?oc=5) <sub>MIXED Reality News</sub>
- 📰 2026-10-03 [Nvidia-branded trailers stolen in California, thieves discover 20 tons of sand instead AI hardware](https://news.google.com/rss/articles/CBMi-gFBVV95cUxQc3M1R0diTEpPMW9JOTljNmYxQmRuMGVCbVd6c0pWVHhmZWZKSGY3aVBrNnY2Sm9YV0dzdEROSnVGTVBhaHZPclEtZVR6UUlRWTRXNWpSQU5WdTFCc3A3TTRaVDNXdlExNmpJVVVMNk5jZFNoQWFNWnUzLXF4ampnLVhFSHR2emkzMWJZZkVObFJVd0dFdXJBeVNCYzlYYjEwMUhqaEYzOEdGbWk4ODFzTEdMcjZFQThKY1drR0tDLU5HLS1iRUg0N21RRXY1SnEtNFNMZGU5WElrLVA5dmdrMjBqcjhDd1dlczdxdmw0UGphR3pwUjNrTXZR0gH_AUFVX3lxTE8yTXVmMjFaT3ZxVGNBeVJJVVg3NVZoR252V2NXei1KSGtGVzlhVkxpam5TN3hSaDBHRWw4UGVTR1VpTmJKRlZXNWM0ZmxPeEtJUEJ6bmVJWGJzLUp3NzNVV2ZJRUNZVWtXc1prLWprX2ItR3VMWjEwcXJiczRaQk14Wkx6czJFdm5hOGxnREpnMjJ2Vm03RUJqYWhVdUV0REJoWm1wc1ZRUWFMREREZGM5ekVyNUpTa19mOHpoNi10bDlSWVhSaDlPTG5oNnE1d2JCeGNOUG4xUXZ1TjV5TG5UU0stU1A4MC1jQ0VMSGxjRHdFQUdsTGVlUzlDMnpISQ?oc=5) <sub>Business Today</sub>
- 📰 2026-10-03 [Samsung Reportedly Hikes Chip Prices Amid TSMC Capacity Crunch: Nvidia, Apple, Tesla Fuel Demand](https://news.google.com/rss/articles/CBMizwFBVV95cUxPRXlpYVphMzNFdnZ0b3loTTJncFplVGhfd2xST09WcTRjTEJvU2FSbU5hZjlReFJ5LTd4XzZ1Qks3MUUxNTI5MUI3eDRBR1Z4SGtpaEpEMjVkUW1zOTd5QTJORjhaTE1Ta1FyMU1XYjdNZVZmWjhHV1ktbVFoRDhacGp6TTE0bGJYQk1BdENkLVd5LWdMdHVDYU5hNjEzcjdXYkNnODhSblV4N1d6a2xlOEwxM3E3cExIUzdJRjhhdDhfZk5rX0E5Rk9vWGdfbk0?oc=5) <sub>Stocktwits</sub>
- 📰 2026-10-03 [Nvidia follows Google and Apple to quietly hike Shield TV Pro price by a massive $100](https://news.google.com/rss/articles/CBMiswFBVV95cUxQdWVFaEpzWE5WZ2tRV1FZUVJIRGNQOHdEcjluNUcxTUhPdDNZMlg5ZEhGZ0o1dGp2YXBqTTBBb05vNlQzSUZ0SkdfQ0RDYUZPb3VsMHJIUDFEODNXbE1URktUQzVRb3NKZkZ4dTJxT0MyTHVXNGlRejZyTXExY2puS1p3WGkwWG9wdUVScE1jbVpjeHZCVnU2elJLRTJqb09Mekg5X1NlWm1QUW5IT0stU2g0WQ?oc=5) <sub>Neowin</sub>
- 📰 2026-10-02 [Nvidia Adds $4,999 DGX Spark With 64GB of Memory as RAM Prices Surge](https://news.google.com/rss/articles/CBMidkFVX3lxTE9CTlV5SU1oSG9YbVlCc214UGUyUjJOc0tGd19QeEhyWVNjZlR3bmpDSk5pdnRiZlprV0gzWTRrTFZPVzEwb2Z2NkNuVThMU29nUWp0S2ViNXc5d2p6NHZqVC1iS2ZpbnppTEFKcWlfUVU0Y0hDSFE?oc=5) <sub>finance.biggo.com</sub>

</details>

<details><summary><b>Wayve</b> (60)</summary>

- 📰 2026-10-03 [We Found Atoms, Rode Wayve and Watched Uber’s Autonomy Clock Speed Up｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1QZjNLZlpHR2ZtcHFaUDF5bEE3ZktHQlNoN0E1amxaVEg0eUdQbElIVlVVZk1JdTlqZG1kbGZYVTBvZDdKRDRKVWlqa2dRNDF3aTN4dEpmdTdxX0dTVnlj?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-03 [Grayson Brulte: Zoox Has an Intersection Problem, and Uber Has 18 Months to Own Its Autonomy Stack](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9Gbmp2RTY3bW1WaFdrMDhqeWVpUHR0WXNEcFA2eWk4Ukdidmx4bXp4ZmdoNFhUWGZoM2pTNVBCVUlJSUl4SVM0UlcwbERnMTNVYmlxTjlxYXBwV0k?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-03 [50 Key Figures Named Europe's Most Influential AI Leaders](https://news.google.com/rss/articles/CBMimAFBVV95cUxPSl9zM2JPUjhNUTBLQ0lOd1BSMnZacllUS0hHa2VSdHYweFIweWQzeFozN1FkLTJ6bkNPR3AxWnpNMzZvekdEd0p6SHVNZ3NPMEVhaGl4QnFYejltWkdpd2ZEU3VYZjFmV3lLb1VlNjdMVGVSZUZ4UGZnQjFzTFh2YVVrQWpFZklfNHpMMHRCaFhxdk1xNXlvOQ?oc=5) <sub>n24.com.tr</sub>
- 📰 2026-10-02 [Why I won’t Wayve goodbye to Black Cabs](https://news.google.com/rss/articles/CBMigwFBVV95cUxNNTZYRmM1dm5YT29lWVFsZjBJaFA1eUV5b1JKSng1VFgySTRQVmp3RXJBbUdFRElIRVhKaXZZRUt6dmhINy1yMVpUWThDOW1naklNQ0RIaHFYTzZ1UnBaRDcxMVdsejBaWDAxcEFhSGhRbE04eEs4SDlBRUQwcXNQMzhJNA?oc=5) <sub>Liberal Democrat Voice</sub>
- 📰 2026-10-02 [Mercedes-Benz Pairs Wayve Self-Driving Pact With Deep Cuts to German Cost Base](https://news.google.com/rss/articles/CBMi5AFBVV95cUxObzFuSDBHdDZmdTVUbEhyb25Jc3FOcTA5LWFVWFBrNWw1QWgwUmx3RUtGQTBMeHdQRGNQUkhBSlZKMEtvaEQ4R1Q0VVVyX2FUTGVxQUc2MkphUlVyZmdHaEF5em5odUNPR3ZodlEzYnFzYWw4WC1jbmZIUWUtVGlqZzVTbWNzNE5hNHZwMXIyTGpkdzdaQVB6Um0xX29PUVA5T2hLU3JabkF6SHlNOUR2bUtGYUpWbHAtQ1N0dy13eXB1OU10ZmlEanBycGFWeXhieHJfcEthZnZGWG00V2liaWxBV0M?oc=5) <sub>AD HOC NEWS</sub>

</details>

<details><summary><b>Momenta</b> (137)</summary>

- 📰 2026-10-03 [带激光雷达的豪华插混SUV哪款好？凯迪拉克全新XT5 PHEV与领克08激光版等5款智驾横评+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE5BdUdXMl9uM1Z2VlJNSzJiU2M4OWp2cDRQUEc2c1h5U1YzdjZuNmZMU1RFSFVEclFuOEppbERLRThXZFNzUVlHamxFX25sNDJYWVBlc0gyRFpiQ2MzNHRGMVNlREJMMkk0SWl6OHo2bXdiQQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-03 [充电速度快的豪华插混SUV推荐？5款快充豪华插混SUV横评，全新XT5 PHEV值得优先看+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE5rb05adHA2cFB4NW82M3ZTcm1oNWl3UUZSaHpwYjJNY2RmSVVYOGl2QVVhdmFOdkZKdlBoTXF3WnE5aDRCbUtJeVdBWExyVTA3OWI0ODFIdEJtbjliRW5ucG9YcldNbUJRemRORk1DVHF0dw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-03 [带激光雷达的豪华插混SUV哪款好？全新XT5 PHEV、领克08激光版、腾势N9与理想L8横评+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE96aHE4dWMtOF8yRlYyOUQ5dEk3TlNoSVAtZlh1cmxQVkxUMktLY25nLU1PSnU0LUE0N0tjZ3FfOWd4a183dS15MlI1THd1QU1mVnNYZEdQZEh2WUpHUzd3VVl6OFhRU1UyVWhoNFpGSlVuZw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-03 [【视频】现代艾尼氪V：个性化外观+800V+Momenta智驾](https://news.google.com/rss/articles/CBMia0FVX3lxTE1jYUdZa0c0Qi1XTlRJcExaanN3WlQyNDIwZk1qc09fV1VKSHRzSWdodld3MW9UaW5zbzgxMkZFcDllMUxrUVRIV25pV2EweWx2ZGhuQjQ3RUVWcUNtZDFFNnhOYXN3SUhUSmJj?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-03 [MG 07上市10.59万起！纯电轿跑配800V+智驾，15万级值得买吗？+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE0yQ0I0OUdJRFhoVllGSWI2cnhGVXNIT1U4dzY3TmdxNjV4MlQ3RjAtYlBUb0F1b2lhaGptUkJkV012X0xBZTZCMmhST1lKaF9uNDdHdnRJLWxFTmlSNWZNcVM4bVRCa0ZjRXVCNUJFSGZZUQ?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>XPeng</b> (197)</summary>

- 📰 2026-10-04 [小鹏MONA M03和MG 07通勤一周不充电，谁更省心？](https://news.google.com/rss/articles/CBMia0FVX3lxTE9KU2FFdzgzN1hSeW9BMWJ4b1I3bG04S19ScDlrVzVkem5IaW95OVBFZlVrVk5ZTVVHc0lXYWZ5bjlmU2lHVnZRamVzZXI5a01aa29wM0RkblNtRGRWMlFRNmxGZFhFRVRNNHpZ?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-03 [小鹏MONA L03月交付破1.4万 九成用户多花钱选了智驾版本](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5mMEZwUDk0dl9Ob0RoX1o1V2V3WVVBclVYQTQxbnZjVlo0RFBuVDBrelo5WU9MZ2YwS1JqaGlaRFgzQ3R6M1FTVWNDb0YzOTR2V040WVkzSDRCeUE?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-03 [15万内掀背轿跑，MG 07凭什么让两强紧张？](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBQZElDUkxLRjd2Wk1RQTRjRnQwdUtMR3ZycHNiTTdZMjZSQUJfRGl5YXI2WkJDWW1RUi1UaFBQU0RQNFB6eS12WlhxMWpUZmREV3hjdXZ1RUtPRk0?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-03 [小鹏P7+黑色版值得买吗？黑武士颜值+AI智驾深度解析+FAQ](https://news.google.com/rss/articles/CBMimAFBVV95cUxNLVRud3RCR2NrR3lMSDFWZURPMlhFQ0ZTRFJXb3ZtUGFnRms5eF9HdDZ2OVhxNl92WjYwU1ZsR3NlWjE3QlFaZWxKNzJzSVZBRWlhaUpuUU80di00Ym9DLXRYU0JvQ1EtYi1kNVB2M29JRU4yXy03ZHRKbHlkd2lTRlhhX2o0YmNFaWlTRjN1V3BBa19wbS1NSA?oc=5) <sub>finance.sina.com.cn</sub>
- 📰 2026-10-03 [3 Robotaxi Stocks Retail Investors Are Screening After Tesla Cybercab Headlines](https://news.google.com/rss/articles/CBMi1gFBVV95cUxNN3ZfS2R2amU4alluc1JkdXFJMUVkRTc4S1ZsMXZ6YTVxWFV4Y1JUbnZBUWJwYmV0Qm5RcXNadUNMdWJkell3YlJHdzk0bXlMVll0VmN0NWQ1dFlLRV9MSzdnSXZaYzY1WnAtN2dBTzRmaEZHU1ZyZGpzMzlDRWZxRmdxVVdXdjV2S3loQjFQZmNQNFIwRWYxSTV5S3V0QVJrekwtVHJNTks5ZnV2d1NFN2ZHRTFIYllwV0E5WWltc204MkZ2SXdscncwdjZFLUJfd0hoMkp30gHWAUFVX3lxTE03dl9LZHZqZThqWW5zUmR1cUkxRWRFNzhLVmwxdnphNXFYVXhjUlRudkFRYnBiZXRCblFxc1p1Q0x1YmR6WXdiUkd3OTRteUxWWXRWY3Q1ZDV0WUtFX0xLN2dJdlpjNjVacC03Z0FPNGZoRkdTVnJkanMzOUNFZnFGZ3FVV1d2NXZLeWhCMVBmY1A0UjBFZjFJNXlLdXRBUmt6TC1Uck1OSzlmdXZ3U0U3ZkdFMUhiWXBXQTlZaW1zbTgyRnZJd2xydzB2NkUtQl93SGgySnc?oc=5) <sub>Simply Wall Street</sub>

</details>

<details><summary><b>Li Auto</b> (158)</summary>

- 📰 2026-10-04 [Is Delivery Update Altering The Investment Case For Li Auto (LI)?](https://news.google.com/rss/articles/CBMiygFBVV95cUxQa0xCXzExZWxrWTFxUnpwbnJJNi1zQlRvV2VxRE9pOWp2ZGFRNHd6Rld4bGFjLTlQaHNMSm1FbmpScmVtVkU1MjBiYUVpa2VJWGVlcHg1cFFPSlpnOE9Gb1BLbFpYWElSVFRMT19LeVNfVktrS2NLbjlHYlU2amZFRnZLVEpMU3RyR2J4M2QwZHRHNFh2aGlWOXh6Ny04LXdwdy1mNGNSaHRKTDFyeTR0X1dpZnR6NUQxLVFBTTFtTmdvMzRmb1lxXzVB0gHKAUFVX3lxTFBrTEJfMTFlbGtZMXFSenBuckk2LXNCVG9XZXFET2k5anZkYVE0d3pGV3hsYWMtOVBoc0xKbUVualJyZW1WRTUyMGJhRWlrZUlYZWVweDVwUU9KWmc4T0ZvUEtsWlhYSVJUVExPX0t5U19WS2tLY0tuOUdiVTZqZkVGdktUSkxTdHJHYngzZDBkdEc0WHZoaVY5eHo3LTgtd3B3LWY0Y1JodEpMMXJ5NHRfV2lmdHo1RDEtUUFNMW1OZ28zNGZvWXFfNUE?oc=5) <sub>Simply Wall Street</sub>
- 📰 2026-10-04 [别再只盯着"移动的家"了，从城市到山野的全场景才叫真旗舰｜神行者8 vs 理想L9 深度横评](https://news.google.com/rss/articles/CBMickFVX3lxTE9tSHpzRGNoUmZUTGRSTHZjallzRmFtenFtLU8yNk1LLUFaaGY1RHBoYnZOS2N4WVRJdjNfV2J3RjVMS2pYVEozTkJHaDBuR2g3bXQyNC1oLUczU1o0aDQtY2Z1V2ZySk5uYWl0cDBBZzhBQQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-03 [神行者8对比三款热门大六座SUV：30万预算，谁把“全能”做到了极致？](https://news.google.com/rss/articles/CBMickFVX3lxTE5LTFBBeGxDdkh4UFhvLTRyemRGcTlDNXY3SnU4ODVDTndfNmtHMVNmR1BLY1ZRYUoyeUljNmVscFNmLWJTb0hUbTVUaTNBeDZQdDdBTXhkVnRsU0JpaFRodm55ZGtTRGxidW9SQ3d2SEgyQQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-03 [深度横评：FREELANDER神行者8对比理想i9、问界M8，谁在重塑豪华全地形标准？](https://news.google.com/rss/articles/CBMickFVX3lxTE5UdTcxQklCSkFZaG5jNDdCUUJNQktTV2l6S3BQeTF6RV8tNEwxR3c4X2x5Z2lrUEVtNGkxYWx2LWhGWHV4NW56LTZKUDJUcElMSHBjNE5TZ3VUMEtZWS1PSkhHaXNoa096TGtyakpuaEFOUQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-03 [新上市的豪华插混SUV哪款值得买？凯迪拉克全新XT5 PHEV与理想L7、腾势N9等热门车型对比+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE1WRWlpU0VZX2NnRzJNUURjR25LR2tTSXdXNm11NnhpdmtyZXBNVHhCQzFNM0hpekNFTng2cnB2T3h5NGYtcnBadlJEUlJRczNiUnd3TVdabTFnS3k3YnF5ZzNtMVIwMWttM0F2aEJ0MGR0dw?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>NIO</b> (149)</summary>

- 📰 2026-10-03 [【视频】蔚来EC6 2022款 75kWh 运动版买断版](https://news.google.com/rss/articles/CBMiW0FVX3lxTE44VEdJZUFLbG5Pbm5YQnJ2MUlocjlCc3ZWSDktTlA5REFHMDhDZVFQV29OTjktMjVTTlA2NjNDd1Y3VGJJNjNUSnd3MldQdklJNnhoc1JmOUktRjQ?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-03 [【视频】15万多开蔚来ET5！75度电池买断不用月租](https://news.google.com/rss/articles/CBMia0FVX3lxTE42cDV5akJzblRBQVBxdnl0Vl91N0E5U08taG1nYWhXcG1Nbk9Vd2cySW5RcjhjOV9peS1ONUpsOWU4c1k4MWRqZ0VWS3kyZUdnUzJSMnhtcFhvS0hmRXBlYkIyRUxkbWNsN2lZ?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-03 [【视频】蔚来ES6 100kWh电池可换电真能规避电池衰减吗？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1qS3ZCR2xJTUd2cmF1Q2pNNVJoZ2xROFV0Ym5uTndVamVfQTAtdlBzTkVxMVNoVmFQbmJMQ2ptMmItSGpvZDlKYXh3SVJUcEYtVi1iY0pPT2Z0Zlk?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-03 [蔚来世界大模型2.0什么水平？蔚来ES6智驾实测](https://news.google.com/rss/articles/CBMigAFBVV95cUxPWkxuTWdYUlhlaFkyVXowc1kxTjN0UzNycEVCc3o5dHNEc0ctQWJ2SHpGUVBsNXllN0tsZmlpTXI2RnFlSFdoSVduQi00SF81cEJqbHBEMS11b3RGNzdVZ092cDB4c3NXSmF1bVpLaGdDTHJ4czZyMTktbzYxQ3pFTg?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-03 [蔚来ES8大五座版值得买吗？38.28万起，换电+900V，3个维度说清+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE5UUVl5Z0NCTXNQclY0UnpwRGwwX2pFTjViZjgwZF80eVU0em1Ndi1VMVZadHAwTXg4Y0dCLU1sZFJ1TlB0Zk1KYktXb2tEZU1Odk1qRlBUUVE0UXB0U2V3Rm5KRlh4Qm4yQkFxVjdpU1BQdw?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>Huawei</b> (327)</summary>

- 📰 2026-10-04 [Huawei Mate 90 2026: Kirin 9030, 6,600mAh and a $194 Hike](https://news.google.com/rss/articles/CBMiYkFVX3lxTE91WmsxbE5Pa2Y4R2pMNW9KTlRfbW13QmVHR3o5WENxZDZ2OU52M3ZQUHVLMFVORDZwblVEV29ReEdvZnB4X2thSEFHT1FnX3RkTTJCa1RkTVJTMXN1SVZYOXFn?oc=5) <sub>Memeburn</sub>
- 📰 2026-10-04 [【视频】华为乾崑智驾ADS Pro主动介入避险，关键时刻真能扛住！](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBRcjlrbFRIZFFKcjNGNENIZThlTDIwRUhlTlZ2V2pUdVZ4VEVsZGMweDJQNWNyazhYYzhnRVUyRm1GTi1GM0pRMUxGZGFoaGlJZlBSTUFHaDFMR2s?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-04 [2026款问界M5值得买吗？鸿蒙智行三大升级深度拆解+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE05VG96REstRlpiSldhZVFZcGpaYzhIOXJwYVQ1U2xOWTVaTUswNk1nVHFxcW5SMjBCajFEdjdyZTBMQ1lTSkVEVGZlaV9Memt5aFZNZVFsRTlJdjhQLXNF?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-04 [主动安全是盾，被动安全是命：奕境X9和问界新M8，谁在兜底？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5Pc2VYTXFxbGcwM2M3bjZ0eHRieFdISm9ZLXJ0Mjh5WjhvMUd3UllERjQybWZqUEJ6SlZ4ZXdTY0Nqenl0cFdCYlNqR25ZLTFzS2d6VURpa3Z3dmc?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-04 [2026款岚图梦想家PHEV值得买吗？32.99万起+华为智驾+350km纯电，3个维度说清+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5lRlU3LXkydGhEYXhuSHZLN0RDYkV1VnQxU3otOUxtdWtET21jX3dGc21vdWJZSmdvVzZZcUs4TEFrYWQ3eUpVSGQ3NmJnZkd0S21qZGZJdVdkamt1TE9N?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>Baidu Apollo</b> (46)</summary>

- 📰 2026-10-03 [艾媒咨询 \| 2026年中国Robotaxi行业发展趋势及标杆企业研究报告](https://news.google.com/rss/articles/CBMijAFBVV95cUxOcktmcDgwOXJreWVKbDQ2TnBPSzJLU1hSak4wdDdUS04zeGlNSGpiaUd1cjNWNW5ZY3RlUldUbVNDdy1UR3pwLWRWR2lzT25WVnpidWV6Rk9zNW9lWHZieWJQTUhPUHhZUGJGaVZvX3dXZnZkMV9aNWZ1bkFZTEdTUkZmNkFqZDBzemt3Tw?oc=5) <sub>搜狐网</sub>
- 📰 2026-10-03 [ASTS Retail Sentiment Nears 1-Year Low As SpaceX Turns Up The Heat In Global Mobile Race](https://news.google.com/rss/articles/CBMi0gFBVV95cUxNUFlfalRZc0RObmR5SHpnbFg4VmNCMC1HcVdkQUJJZk1JMkVvZXBFdG5nQkZ2b1MwSHN5eVVod09GVnZqWnl4TlZhcUJZc3BMVzdZdmNpT3h6UWtoVFpkSDdWZ0JZdUFtcUVqaDJ6RDlURExmVnZNRUFKdDVIYWFOaTNJXzJCWHhWQzJwOVo0emZsTFd5VlRIN2c1NS1QNEZ0LXpDa0FOREdDZ3BGd0MwTkxLRkRPSm1PajZOQ2FtVXRrUkZ6cERyb2FhZzBSZTZrMUE?oc=5) <sub>Stocktwits</sub>
- 📰 2026-10-03 [特斯拉大涨市值1.49万亿美元，别拿Cybercab当“萝卜快跑”](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1hSUFDdWNpc3RBaENGQXFMZFRBRFdnOFM4TC1NUjlhZmxpYjk4aDA2RWRfT3NyUlFQdjNiT19jMVRTdkFaSnB1M2t1ZUhVc2otQVhRaFVHZUQ0eUE?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-02 [Lyft app launches in Europe](https://news.google.com/rss/articles/CBMijgFBVV95cUxPZldVVUxUU3ZlN3pCRkdpZGpxcmZHUGg1LVB3eVVJLTNWYm5aanI0d0piSnpJN1N0QVFhTkh2Y3lTa0RwQnl0aXF6MnJZVTlXYllEelRfWEtqbnlHMVVMQlYwTFJIMll6TnAxd1NBWll3cW5OcWd5RHduMHZ1anJxX3k5R2tpYTkzbHA2aUpn?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-10-02 [德信体育官网顾客消费超20万，因小事发帖吐槽后账号被限，Tiffany中国零售团队通过邮件致歉](https://news.google.com/rss/articles/CBMiW0FVX3lxTE05bWYzQUQ5LWFpdmRBNGU2ZHZkNnpfdndPWDlPQVJQVlBHeG1TNWRHX09ZcDE4cGpLUDFKbWVKTDJ4ejJtLWhEZUk4aXpBNlhralVzUVZnUW01ODg?oc=5) <sub>Pchome电脑之家</sub>

</details>

<details><summary><b>Pony.ai</b> (105)</summary>

- 📰 2026-10-03 [3 Robotaxi Stocks Retail Investors Are Screening After Tesla Cybercab Headlines](https://news.google.com/rss/articles/CBMi0AFBVV95cUxNWklYSmZGdHROVHBDU28tYTZJb2NnY2EzdkFDSnRLalNhVW5EVDNLVHVSVXlwdWhnZmVmTi1ZSE5TdGJvQ0J5dEVzeUV1X1Q5aWJuRnBCWE1mNFJ3c0ZURWx4Z2Z0aGN0Vy01Um84U2dKNkMwUnowTDkxUmJVaFNpTjM2RXVWUFlORk5RcGZtQjdjcy1xTnpBOTRJNDFsVmNWR2c3MG9GMUVYYTk3QTRNdEJCWVhGMjBTLU1FREcxZnBidll6aEJVQWxmUUtXNXVv0gHWAUFVX3lxTE03dl9LZHZqZThqWW5zUmR1cUkxRWRFNzhLVmwxdnphNXFYVXhjUlRudkFRYnBiZXRCblFxc1p1Q0x1YmR6WXdiUkd3OTRteUxWWXRWY3Q1ZDV0WUtFX0xLN2dJdlpjNjVacC03Z0FPNGZoRkdTVnJkanMzOUNFZnFGZ3FVV1d2NXZLeWhCMVBmY1A0UjBFZjFJNXlLdXRBUmt6TC1Uck1OSzlmdXZ3U0U3ZkdFMUhiWXBXQTlZaW1zbTgyRnZJd2xydzB2NkUtQl93SGgySnc?oc=5) <sub>Simply Wall Street</sub>
- 📰 2026-10-03 [特斯拉大涨市值1.49万亿美元，别拿Cybercab当“萝卜快跑”](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1hSUFDdWNpc3RBaENGQXFMZFRBRFdnOFM4TC1NUjlhZmxpYjk4aDA2RWRfT3NyUlFQdjNiT19jMVRTdkFaSnB1M2t1ZUhVc2otQVhRaFVHZUQ0eUE?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-02 [全球食品价格9月升至近四年最高](https://news.google.com/rss/articles/CBMibEFVX3lxTFBmZ3JLc3dMZW1rdzdSeHB4TUh2bGhYbDdhalEzdENIT0Zyc3RsOC1YWWJwQ3VjSk5iRkxyREhOeXduSkl5OVluQnhJLWJya0NLb0tub25FOEk5Q0VQdTRZeFlWY3JsUkNBY2I1Vg?oc=5) <sub>早晨报</sub>
- 📰 2026-10-02 [10月3日热门中概股多数下跌，网易跌2.82%，京东跌2.24%](https://news.google.com/rss/articles/CBMiigFBVV95cUxPM2d4OHNlbWNVM1dmUXdkQVl6UkwyNnRURUNoVFktemtaWXZCcG5BY1hqVDNSOXdsaGpCelpKSVJ4VzJYcDJrLVdKT3I5RllMbURNMEp3M1h5N1pValE5NzU2WVcwbDk1Q2kwa2lWV3FTVzc3LVVvd0RVbFF0Q0U1eko0UlNiR1p6NXc?oc=5) <sub>finance.sina.com.cn</sub>
- 📰 2026-10-02 [Does Pony AI (PONY) Change Its Growth Story With Europe’s First Driverless Trial?](https://news.google.com/rss/articles/CBMikgFBVV95cUxOaTM2RklpMUE5ZGpJbU54UlRnS3dqb0hJWTRuaVlxai16QXNKdUhsNzloWDItZ2dRRDVLcC1YSXVDcmFlV3NCcy1vWVNWZG8yMlZUOUdmdG41eHdTSFNUUGZiX1FhV3cxdm1nY1BjLU1BM09DZDNHamFJRDdfYlVpN3N3cjVqanlCcUVLc1pqdkVsZw?oc=5) <sub>Yahoo Finance</sub>

</details>

<details><summary><b>WeRide</b> (100)</summary>

- 📰 2026-10-03 [Pony AI, WeRide to stay unprofitable through 2028](https://news.google.com/rss/articles/CBMikgFBVV95cUxNbXpzb3E5eTB5dm1HU05YVndNVXNlb0lTMXh1bDRSMkxkZmRDa2xnQkxfajNSNHlOa1dvRG5YSVctdGlJZ01QWWd4b0EtZkdEaFZtb0xPeDc3QmZ3eEUzTGVOLURUSWJfZEY1ejZqeDVIMXJfcFhFdFZrSTNjNmhJYkVadWhPcXBPWEhmeS01MHNBdw?oc=5) <sub>Briefs Finance</sub>
- 📰 2026-10-03 [WeRide (WRD) After The ELEVATE Slovakia Deal And The Valuation Debate](https://news.google.com/rss/articles/CBMiywFBVV95cUxQei1oZTBYbEZlNzQzZUJ5eExhVkZVNFUzY1hMcElGOG1sbkY1SEIxbUpsb25scU81dVB5cG1iUnpldmZRWjRZMWtLbTBjcVhNbG5CNmpaQzdBRXk2M3c5NDNDNXNNOGFqeG92SENyXzZoNm8zWDBRYzVQRXFGdlRNc085a2d5S1VvQ21wd2E3bk9ENXZITTBKRzJMZGptQS1YazdUVHBFeW9VNlpVakQwdmxFbUtSRTRIZzZ3RExEMWcxVTlQOHVnblRyZ9IBywFBVV95cUxQei1oZTBYbEZlNzQzZUJ5eExhVkZVNFUzY1hMcElGOG1sbkY1SEIxbUpsb25scU81dVB5cG1iUnpldmZRWjRZMWtLbTBjcVhNbG5CNmpaQzdBRXk2M3c5NDNDNXNNOGFqeG92SENyXzZoNm8zWDBRYzVQRXFGdlRNc085a2d5S1VvQ21wd2E3bk9ENXZITTBKRzJMZGptQS1YazdUVHBFeW9VNlpVakQwdmxFbUtSRTRIZzZ3RExEMWcxVTlQOHVnblRyZw?oc=5) <sub>Simply Wall Street</sub>
- 📰 2026-10-03 [We Found Atoms, Rode Wayve and Watched Uber’s Autonomy Clock Speed Up｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1QZjNLZlpHR2ZtcHFaUDF5bEE3ZktHQlNoN0E1amxaVEg0eUdQbElIVlVVZk1JdTlqZG1kbGZYVTBvZDdKRDRKVWlqa2dRNDF3aTN4dEpmdTdxX0dTVnlj?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-03 [Black vans map Madrid streets for Spain's first robotaxi rollout](https://news.google.com/rss/articles/CBMinwFBVV95cUxPaHJxeUctTWRvVUV5S21yZE9QSmhXZl9lZXlQalk3eFQxa0UtSzN2YnJ1cG9jbEZac3lMNE5Dc3Z5Slp2TlpDWmZkU1lKRTE4SURHR3l6R3NIdmIzNnJLMmNTR1k3OHZSUGd2djk1ZjJMb3JvWW5WMTVsd1BqbGFDYnFwNy1ydi1xT3ZTZ2VNVzQ4UUFCZnFxZHpyMk1qMGc?oc=5) <sub>RUSSPAIN.com</sub>
- 📰 2026-10-03 [Isabel Rodríguez faces political storm after housing decree defeat](https://news.google.com/rss/articles/CBMiogFBVV95cUxNRndiX2otNlRHQkIxRmJOUHA4bXBROEVSemlkSFUybHM0bW1tUjNmRklmR1JxLUs2b09UMUJ2N3dGNU8yZjdDaklvcnkzeFlsZDZlazZSd3lBdURHSDRoZkhGMUZpaEE0SDJ2czh2RmlxaG1KMHViYUdqREVFVWJ3dmRVWUFpdGRyWElrekhVR2xWNGpLWDlxSTBLVGp6QVJwLUE?oc=5) <sub>RUSSPAIN.com</sub>

</details>

<details><summary><b>Horizon Robotics</b> (153)</summary>

- 💻 2026-09-29 [HorizonRobotics/Ego4WAM](https://github.com/HorizonRobotics/Ego4WAM) <sub>GitHub</sub>
- 💻 2026-09-24 [HorizonRobotics/CogWAM](https://github.com/HorizonRobotics/CogWAM) <sub>GitHub</sub>
- 📰 2026-10-04 [【视频】蔚来ES9中岛地平线，新车现车没有需要等，咱们现车在售](https://news.google.com/rss/articles/CBMiW0FVX3lxTE81TlpWOEZnVHNFNU1DalNWa0hzVEtFeERmRl82S3BBQzNUWkRFUFU2ODBnTXVlUXg4RlJMV2RFRUZoSmNWY2dxQ183R05FOWU0eE9vcFpnVmw3WWM?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-04 [【视频】纯电300km，家用、越野全兼顾，iCAR V27长续航版值得买吗？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1PLUthcGNHS212VXU5eVlUOUV3M1dTR0w4dm54TFNBRWxyVnNOc2pMSm5sNnNKUEhQTUpYX2h6d3N4WVNwY3RpejNQVGlPMl9BVlVHemE2UnFQUlk?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-04 [周末带娃露营，深蓝S05和零跑C10、铂智3X后备厢差距在哪](https://news.google.com/rss/articles/CBMia0FVX3lxTE9UNmhRVGpvSEFLa1NRQW9qdGFkNnhvX3FfWmRxcFZYWmJicWgtRFdGd3N2Ri1ZcVliV3BPR29rNGlkeFpXZDQ1YTVtaU5pYmhPNF93dXRtSS05aERMaTMyUDVVQ0NpTzJoQnM4?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (27)</summary>

- 📰 2026-10-03 [你的国庆自驾搭子来咯🥁！无论是堵车、窄路、复杂路口，还是泊车，小元都陪你轻松出发，安全抵达。#元戎启行DeepRoute ##DeepRouteIO##辅助驾驶##物理AI##国庆节##自驾游](https://news.google.com/rss/articles/CBMiY0FVX3lxTE9oQzI1QkRUaU5jRDFaR1QxMzBmVDRZSkVXb0FuWkJfUzN0MEh5NDZSVEhCR2hjUzhUdldrTkhEelNlZ0JPTE9SWEhaOXRHNi1rZ1hBQUNOWElJWF9fV3c5aHh3RQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-03 [赛豆科技首款车型—AIVA ME7正式首发，采用时下流行的轿跑SUV造型比例，并且配备大尺寸的轮圈与多活塞卡钳，车尾还配备镂空扰流板，预计是一台主打年轻运动的产品。结合此前的消息，这款车会融合豆包大模型以及火山引擎生态，并且有报道称其辅助驾驶将采](https://news.google.com/rss/articles/CBMiY0FVX3lxTE4tU1hIOTd3MWtGSUV0RjZPR3pKRTNVTGNzaXpkenphcG5FVk1pNnZZMGdIUy1TVi1SMW9JdV9KMjFPYXlqakw3MmhObmtMZVB2VlVob2RoaFJTcVFsU09OTnFVNA?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-03 [提供豆包大模型将覆盖20万元以上主流市场AIVA ME7全球首秀_热点推荐](https://news.google.com/rss/articles/CBMiYEFVX3lxTE83MUJRVjJpdG92N0xFSUpkdHlsMWdWQlpaWE1CYzQwblNiOFVMVURPRFZ0amZQTXNpdl9odkpOSk9SZVAyWDhadnBXbWozTHNjOXNkRmRRS2dXbV9BQndHMg?oc=5) <sub>证券之星</sub>
- 📰 2026-10-03 [城市NOA市场上演“三国杀”：元戎反超Momenta，追到华为身后](https://news.google.com/rss/articles/CBMidkFVX3lxTE5reDJCYnVQOHFaeXRCN2RENTUweDF2cVRrbkZPN0RUV3d2YnF1ZDdmT0NuUnloR3EyRGlDU2x4ZTkyZVdNdzJ1N1RRUVV2T0RLd2R4SEFnMFVaLVNHTjE0R1pUV25JQmhvR1NINHZrNDBTdFFCcWc?oc=5) <sub>news.sina.com.cn</sub>
- 📰 2026-10-03 [AIVA ME7巴黎首秀，赛力斯这次想讲一个不一样的“AI故事”](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5wS2JvX2l0SXI2ODdxd1g3T09YeUNtRGlJRG9KTkhXU1VEOUtmZkcyNWdCamhKd2pLR1JEekxDV1ZTeWwxa3FmOHo3RDFMNkFTb1RJNzN6SnctMjA?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Mobileye</b> (20)</summary>

- 📰 2026-10-03 [What Mobileye Global (MBLY) Could Not Prove Before The 49% Fall](https://news.google.com/rss/articles/CBMi0wFBVV95cUxOTDFoVXlyNjVvYmJycldRVUhaOHNieXV1MGJlRDVWWlVmUXVPMUY5NUlHWV9PcTYyYlMxWGNxRXk2c3R6b293RThGVW9ONFBBaUtqSkJsRl9MNjRvVVAxRW1WdGdrUXRKaDJqS042RDBXODB5YkoteU5USVlhdlBfS3pGcnlpVzZ0al90dm51WndmSGNCSElQWE9JY3hHaVJhMFZTSGpSMDVuWGQ2ZWtDQVlxVUFHeHJRVFJNclNaS2RLR3RsQnZ1c05rQjZseGhSVzVj0gHYAUFVX3lxTE9LbTQwSTVOazZ1ZkxtRXhjdm5qSjluZjlEandjc3JUdWNkRGdwbGpYdmhNM0NIYlRrQjlMdnI4ZWZGM2FHOUV6SHF2TnJJMDlWTktBWEluVnVQZ2FFYU5WMUF4WS0zSXRmbkRDQzEyVmFUNmJzTFZwTzZDVEFIcXZVd3BLZUFHa1daeDdBako4ZFVseEVsSzE4UURFSmQ0Mnl4V01HZHdybXlFNXFIelVJMURQNC1GNVJKSXgzMTkxenhxLVB0dFlxc1FJLTBzMmh2UzJjaVhKMQ?oc=5) <sub>Simply Wall Street</sub>
- 📰 2026-10-03 [We Found Atoms, Rode Wayve and Watched Uber’s Autonomy Clock Speed Up｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1QZjNLZlpHR2ZtcHFaUDF5bEE3ZktHQlNoN0E1amxaVEg0eUdQbElIVlVVZk1JdTlqZG1kbGZYVTBvZDdKRDRKVWlqa2dRNDF3aTN4dEpmdTdxX0dTVnlj?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-03 [Grayson Brulte: Zoox Has an Intersection Problem, and Uber Has 18 Months to Own Its Autonomy Stack](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9Gbmp2RTY3bW1WaFdrMDhqeWVpUHR0WXNEcFA2eWk4Ukdidmx4bXp4ZmdoNFhUWGZoM2pTNVBCVUlJSUl4SVM0UlcwbERnMTNVYmlxTjlxYXBwV0k?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-02 [Mobileye Global Sees ADAS Momentum, Eyes Porsche Launch and Robotaxi Expansion](https://news.google.com/rss/articles/CBMi0wFBVV95cUxQYzRBUnBoMFNxTkNkYjFDNl9YbVpSRTVwb1N5SjFjMm56dEFiS0I2amZUQ1JqMHFTTlJHb2N2bkhlUXhOaTRpbHJIWWxhWWVBeUxsdlZ1bUtTdzRsZEUzV2NHWUpaVnN2ZzljWnhZSnlibjNHNjE5M1pyc21xekJGM1A3Z3V0SGZRVTVGSG1hMm9DWVlnSUhBQ3hKNk9yQjBZUU12bXN3MUFWc3k1XzZKXzZIeGh5bEVZaXpta3cwMjVHUGxlaHRINGhKdnhERU12TkRN?oc=5) <sub>MarketBeat</sub>
- 📰 2026-09-30 [3 EV Stocks With Up To 39% Revenue Growth](https://news.google.com/rss/articles/CBMikAFBVV95cUxNbktkTHB2ZmdVWjdmMG5GaWdrR0dyenFac2dnV2d3eWpIVGxmOHJIeVpZU0RBREthd2xEenRPODRhcHhyaDVYV0FGX1l2eVhtTVNDZV9kN2t5UlR0b0Zyc1MtdDluZkZpaElxMlJud0VIZlN0eldEWGZVZ1Z5MlRyV0NRdU04bkRaaVdVV05nejE?oc=5) <sub>Yahoo Finance</sub>

</details>

<details><summary><b>Aurora</b> (47)</summary>

- 📰 2026-10-02 [Aurora Sets 2030 Scale Targets as Kodiak Names Its Driverless Launch Lane](https://news.google.com/rss/articles/CBMipwFBVV95cUxOcUxDQ1dvcFluRHh6bnBzYTBhMmR2QXgyamkydGRYYUU1eTNUeGh1bnFObWMwd2Fsejd2YUdVV0lsRXZjMEtSdjEzV1ZWZUpZclZhM0Z3ZXdCUk1UZEhkRWtucXV5Nmx3RTAtV01rWjBRRDlaUmhRSjE5c1VWSXpjeE4tbFpuQlNfU3M5S0R0Z3VDUVRzNE9rUkFCRUlPM3psX3B0UTRISQ?oc=5) <sub>act-news.com</sub>
- 📰 2026-10-02 [Kodiak AI adds its first retail customer for driverless freight service](https://news.google.com/rss/articles/CBMizwFBVV95cUxPOFdCYU4tdUVRZURuc2tfQ05rR0g4bVZFdTJxN3FLRm94bENUaWRqWUtBU3YwM3djSldXd3V5YjdiNTdwRXNOTUpoem4wdHQ4aVNlWHRtb3FQekk4blQ3OU5NaWZhSTQ3VVhwVlp6eFk5Vlp1X1Z1a1J4VmxZc1dnNld4TVFZTUtQTldpQ1pneGRWcHdRMU9CSkNSdlRIV0g1WHBLV3NKandOS1dlSnFiYVFqWFNsWXBrcjItcFhBY1NRUndfekxfUXJtcklRRmM?oc=5) <sub>TradingView</sub>
- 📰 2026-10-02 [Autonomous truck beacon waiver moves closer to October renewal amid legal challenge](https://news.google.com/rss/articles/CBMihAFBVV95cUxQQ0lmYzY3VUFxWlVueUZaTURHVC1vT3VDc2NfN3M5ZzAtZWpCNXBxUk52X2dNVllLdUg2amlNN0R3X1dyM0NGUTZiS3dLcFBWOU5zTGN6cjFodERTelE3RW1vRGZBS2w0NjFHSVBfMGJqU1JhUHZlN3hBT1hhSUFlNmNPbXM?oc=5) <sub>FreightWaves</sub>
- 📰 2026-10-02 [Self-driving big rigs roll into California as driverless future comes into focus](https://news.google.com/rss/articles/CBMiqAFBVV95cUxNMnlHV2RtMU1WUGJGVTdjZ3N3TzdreHdWTHZEZDBwUk1OaVlDb2Q3SnlqMGZXYkxsWkViUi13RDhLekxtYmNhcFE4N2xVRkxGNVBPYS1LYm1iU0hkUHR6ZHZRUDZqZzJsam0xSnRFTV9TYkdTMnVSdWg4QnRvWUlPQmxNTnFVUVc2Vm9RSkFwN1hMY2xtZlRTMFJZRFV2UWdTVHFVaHNud08?oc=5) <sub>New York Post</sub>
- 📰 2026-10-02 [Aurora CEO on plans to scale up fleet of self-driving trucks](https://news.google.com/rss/articles/CBMigAFBVV95cUxNQ19oRjhzVGxFNmZiVXpwZUpOempNd0xUWV8zU01KM0U4QU51TDVYQXFWcGZJdGRObmpMaEs3UUc3bHdzaVlGdHdmSU5IV2xibnhHbW9JalRJU0NpTWQ1QUkySlg4MDBTUVpKbFVpc2dlbFRqakFMVmRfQnpkcW9xWQ?oc=5) <sub>Yahoo Finance</sub>

</details>

<details><summary><b>Zoox</b> (84)</summary>

- 📰 2026-10-04 [California law sets fines for robotaxis that impede 911 response](https://news.google.com/rss/articles/CBMijgFBVV95cUxPblpMZUNYcmctTEJOOUVKT21YdEFDZ2FnNDdqX1FHOVpFY283ODV1ZlNaLTBqRkMybDhfNjJ3UVlFVlpSa1pkYlpQdkNIdUQxSGdUZGo4ZG00SVZnRF9kMGRmUmVJLWpNRXpaTm9WR3BCZTBjYndOQ2g3QVpsaHRfenVyVUhhSVlFOEZqSEF3?oc=5) <sub>Mashable</sub>
- 📰 2026-10-03 [Grayson Brulte: Zoox Has an Intersection Problem, and Uber Has 18 Months to Own Its Autonomy Stack](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9Gbmp2RTY3bW1WaFdrMDhqeWVpUHR0WXNEcFA2eWk4Ukdidmx4bXp4ZmdoNFhUWGZoM2pTNVBCVUlJSUl4SVM0UlcwbERnMTNVYmlxTjlxYXBwV0k?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-03 [We Found Atoms, Rode Wayve and Watched Uber’s Autonomy Clock Speed Up｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1QZjNLZlpHR2ZtcHFaUDF5bEE3ZktHQlNoN0E1amxaVEg0eUdQbElIVlVVZk1JdTlqZG1kbGZYVTBvZDdKRDRKVWlqa2dRNDF3aTN4dEpmdTdxX0dTVnlj?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-02 [Robotaxis Are Watching You: Privacy Crisis in Self-Driving Cars](https://news.google.com/rss/articles/CBMimwFBVV95cUxPT2FiM015WHE2UTFZV2YybXlMekRHWG5sX3gzbVJkREh6aUFfNENxbndOT0Rjb3g1RmFOZUtBX0hlTGljSnl3VmFJa0JET0VtTGlyd2FmNGRISDBpSnVaSHRnMm0yQVMxZmR3X0RVeE9jbVlIbktxenpkM0NxYzVjOUVzWFN1c25CVXZOQWxmOUJWYzNXZDBpckRCZw?oc=5) <sub>The Tech Buzz</sub>
- 📰 2026-10-02 [California passes new law to tackle robotaxi disruptions](https://news.google.com/rss/articles/CBMiswFBVV95cUxQTXdWbGZKbTJsZFBVMlRlSlc1MmdVOUYwRUVBQVVzWmx6Y0dhTFhTZnNSZVNaZk45aG9KRUdIWjNRSEVZUmVFU1c4Um9xbFZMVjIza3RsS3drV0xEb1JHZzF3OG5yUDQ0RnQtMWw2eEtjMkItY3ZmOXFZaHUzOEdDSl9FUTlIUEw3c204OGU1Sjg5X2JJWW1ZekpaOG5pRWlaZWR2Q0tVOVIyQnZvcnV0dFpsRQ?oc=5) <sub>NewsBytes</sub>

</details>

<details><summary><b>Motional</b> (28)</summary>

- 📰 2026-10-03 [Philippines and Singapore Wrap Up Talks to Modernize 1977 Tax Treaty](https://news.google.com/rss/articles/CBMidkFVX3lxTE5xaDlQWXYwZ3NCQURZZDRRYUVCbnpLMVhUalJaMEVYRnFjb2JTWTFVZm1wWlhXTkVyRXFJY2Z2ZUVEbjlGcVpyQWc1ckFma3ZaajhjLVJLSEVwRVpNMGhIRXprOVl3eUJsR0hKLVprWkFBWEViN3c?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-02 [Synopsys Unveils Autonomous Semiconductor Design Agents; 50 Collaborations Underway with Samsung, Nvidia](https://news.google.com/rss/articles/CBMidkFVX3lxTE5JSGVJNUZDUHBaZGpNYy1nTEcteGdsaUF0WVBIdUx2Yzd1X01lSkhIbHFqaDhENzZTOE1Zc29Rc0VRU0xfY3pLSDdwbk9sQ01oMWJxamNfOHZhRTdVdXQxRnIxdHpFNUg5UXVRX1haeDVEd2dGZ1E?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-02 [South Korea's Hanchang Plunges Over 90% on First Day of Delisting Sell-Off, Tumbling to 85 Won](https://news.google.com/rss/articles/CBMidkFVX3lxTE1GYTN6S3BEUVlyVi1nMDhvd09hNE5MR0FQeWQwV2hkWGpEYXItR05jRlBJaGNQdk1kaWlqa3o1VWUwVEZtX3FUOTBWNy1ULVZGRmlOTFVSNmJyZk9OdU0zcmFPUFAwRkxVWkd4cFVMaHRFd3RHc0E?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-02 [South Korea's Hanchang Plunges 93% on First Day of Delisting Trading, Tumbling to 85 Won](https://news.google.com/rss/articles/CBMidkFVX3lxTE1GYTN6S3BEUVlyVi1nMDhvd09hNE5MR0FQeWQwV2hkWGpEYXItR05jRlBJaGNQdk1kaWlqa3o1VWUwVEZtX3FUOTBWNy1ULVZGRmlOTFVSNmJyZk9OdU0zcmFPUFAwRkxVWkd4cFVMaHRFd3RHc0E?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-02 [Supermarket rice prices in Japan fall for 7th straight week, 5kg at ¥2,926 below ¥3,000 for 3rd consecutive week](https://news.google.com/rss/articles/CBMidkFVX3lxTE5OWVltSmxJY0hzTDhGNnlyRkpMbWlta2F0M0ZRRHdBd19BRUFCbE5qcWdrYTZ1T0UtMHFIc09KTl9ORVpDSXl1eUxLT1JwN1hDZ0Y3Y0JhVjFTSVN0MTdUVVNzZGxiYl9GYS1QTkl4MWR4cDZ3TXc?oc=5) <sub>finance.biggo.com</sub>

</details>

<details><summary><b>comma.ai</b> (44)</summary>

- 📰 2026-09-30 [A $999 Box Promises Hands-Free Driving. Its Own Code Says ‘THIS IS NOT A PRODUCT.’ Now NHTSA Is Investigating Crashes That Killed Three.](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPNFIyamduTmQxb1dKNlh5Z1hCYUhyemoyU2I2bjFUWjZQSDVFSDFWOGxlM1hnQms4Q1lpalg0bXlCTEZTdVJ3eGtNTjlLamY2eW9LX09IejF6SkJxSmZ2QjRkU1pUczlRY2g3cUZIN3hvSUc3a3pUWHVKVk40MlY3Wk5SX3dnOHBl?oc=5) <sub>Yahoo</sub>
- 📰 2026-09-30 [The $999 Driving Gadget That Just Landed In Federal Crosshairs](https://news.google.com/rss/articles/CBMicEFVX3lxTE5kRFFmYXdUcmRRZ2wtNzF4QlRqQ0o1UmVscVhPWFlsVVE3S1dRVWdtLWFsOFJYeUlHY3phaWZYejBnWjFvVmxTcEJNRVBaQUJscU1VODZvRmxrREVYRDUyZlNJdTNsMUN4MmkwYXY1TWs?oc=5) <sub>HotCars</sub>
- 📰 2026-09-30 [Federal Probe Opens Into Aftermarket Self-Driving Hardware After Three Deaths](https://news.google.com/rss/articles/CBMiqgFBVV95cUxObDZzR1Z3QnZLaDR0bTRldUFvc0ZESTBoUHIyZE1PSmJHWFR4MmdrTi0zWkRFT250VG5WbTNuTWd4dzV6R1FIYzV2NzI2NGlfMzkwdHBTZFdIYkxpNG9pWldBQjdxTF9OOTFiZ1M2RlVfaFlkNThCRk41c21ZcXRsalFfOXpqTXRhYVRhaVREaFRRamMzcE41TGNMVTA5azFDWWxCalpHNkdCUQ?oc=5) <sub>Gadget Review</sub>
- 📰 2026-09-29 [US auto regulator closes airbag defect petition in about 807,000 Honda Odyssey cars](https://news.google.com/rss/articles/CBMigAFBVV95cUxPbllOY01DRVNHZUd5dXR2MXJDc0N1bXdVS2V2V3BzX0NqdmxORnl1cm9PU25FSU9YX2xyajJVNEVwdXFjZFM4eHQzX1ZmeHVTR3lyTVpnNlRna0dXMThiR1A5TGdseEtJTDUyQzVqN25nMUV3MVdYWVExMHlQZTFPWQ?oc=5) <sub>AOL.com</sub>
- 📰 2026-09-29 [NHTSA investigating deaths/injuries linked to comma.ai driving system](https://news.google.com/rss/articles/CBMitwFBVV95cUxQMUxNaU15eUlyamdpeUtadXJFQnlOMTJYOHJmdHRJYnpJMWdJb3hJRlRISlNGZVA3dkhSNnNVOG53N3dMQUtOVmFCNUpqRWhaXzA1TG5HM2I0aEV2bG42VkdoRXRyYUI3SkpnM3ZCS2JLUkMtemRJNEVONkh3cExkakF1LVNEVjNZMjFpVndjaExSaHhiME45NGZEbWFCUi1YQ2M4Q2pLOGFISWQyeGhVV1Z3QW0yM28?oc=5) <sub>repairerdrivennews.com</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
