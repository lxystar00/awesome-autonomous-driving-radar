# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-10-13 · 1,251 papers tracked · 39 curated.

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
| [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)<br><sub>Nan Yang, Zhanwen Liu, Linfeng Zhang et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 8](https://github.com/Zizzzzzzz/MVPruner) | Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings |
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
| [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)<br><sub>Shen Zheng, Anurag Ghosh, Gaurav Parmar et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 31](https://github.com/ShenZheng2000/WarpI2I) | Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs) |
| [G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance](https://arxiv.org/abs/2606.26017)<br><sub>Hang Yu, Ye Jin, Alessandro Canevaro et al.</sub> | IROS 2026<br>2026-06<br>📑 4 | [⭐ 6](https://github.com/HangYuu/G2DP) | In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors |
| [SUV: Future Scene Understanding as Video Generation for End-to-End Driving](https://arxiv.org/abs/2608.03084)<br><sub>Yibo Yuan, Jiacheng Fu, Jiangtong Zhu et al.</sub> | RA-L 2026<br>2026-08 | [⭐ 20](https://github.com/ASH-2046/SUV) | End-to-end driving requires a coherent understanding of future scenes, yet existing methods model these scenes using task-specific heads and output formats, with limited scalability |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 16 | [⭐ 346](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
| [Latent-Centroid Steering: Single-Pass Classifier-Free Guidance for Command-Aligned Autonomous Driving](https://arxiv.org/abs/2608.00237)<br><sub>Meibo Hu, Jiamian Wang, Pichao Wang et al.</sub> | IROS 2026<br>2026-08<br>📑 1 | [⭐ 2](https://github.com/codingmlinprocess/LCS) | Vision-language models (VLMs) have recently emerged as a promising paradigm for end-to-end autonomous driving, enabling agents to map multimodal inputs and high-level navigation instructions directly to executable trajec… |
| [DVGT-2: Vision-Geometry-Action Model for Autonomous Driving at Scale](https://arxiv.org/abs/2604.00813)<br><sub>Sicheng Zuo, Zixun Xie, Wenzhao Zheng et al.</sub> | arXiv<br>2026-04<br>📑 14 | [⭐ 367](https://github.com/wzzheng/DVGT) | End-to-end autonomous driving has evolved from the conventional paradigm based on sparse perception into vision-language-action (VLA) models, which focus on learning language descriptions as an auxiliary task to facilita… |
| [STAGE: STyle-controllable Action GEneration for personalized autonomous driving](https://arxiv.org/abs/2607.29517)<br><sub>Zihao Liu, Xing Liu, Yizhai Zhang et al.</sub> | RA-L<br>2026-07 | [⭐ 6](https://github.com/CarlDegio/STAGE) | Driving style refers to the behavioral preferences that drivers maintain during driving, shaped by their diverse experiences, habits, and needs, and is typically reflected in varying levels of aggressiveness |
| [A Survey on End-to-End Autonomous Driving Training from the Perspectives of Data, Strategy, and Platform](https://arxiv.org/abs/2610.00926)<br><sub>Chengkai Xu, Yiming Cui, Jiaqi Liu et al.</sub> | arXiv<br>2026-10<br>📑 5 | [⭐ 104](https://github.com/Jiaaqiliu/Awesome-Training-Ecosystem-for-E2E-AD) | Autonomous driving is a cornerstone technology for the future of intelligent transportation, where end-to-end learning has emerged as a transformative paradigm that directly maps multimodal sensory inputs to driving acti… |

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

<details><summary><b>Waymo</b> (211)</summary>

- 📝 2026-10-08 [Sober Drivers Still Face Nearly 4x Nighttime Risk: Why Road Safety Demands a Safe System Approach](https://waymo.com/blog/2026/10/sober-driving-benchmarks) <sub>official blog</sub>
- 📝 2026-10-08 [Waymo Closes $5 Billion Debt Financing to Accelerate Business Expansion](https://waymo.com/blog/2026/10/waymo-closes-5-billion-debt-financing) <sub>official blog</sub>
- 📰 2026-10-13 [Elon Musk calls Waymo cars ‘pet destroyers’ as robotaxi rivals clash over safety](https://news.google.com/rss/articles/CBMiuAFBVV95cUxONGU5dmV1R2VERlRIblZGd1VWbDlsVTRTN3dUOEtVRkxqMUxGMWlCQ2JZVGxxNVdKQUM0dDY0RlBuTnZuM0hjWDFQa0FQWmd1MkVnaHZQcXo5dTQ3NjRFQzhoaXcwWUpaY19JOEZiZzdQMlk5WUNJVE9iV1dRUTZwNTFiY05xWGV2cHltMFJ5TjY4TEFrY19aUDhqanFXUGlJUTVnNE1ESWJpMS1IRXEyWnhYczVuX1Nu0gG-AUFVX3lxTE15ZHVUU1NnWVVfQUhhZmx3QXhNZW9ISlc3ckY3ektSV1drcThTYzlrZlU3TFl5N1l0UnlGUXBvTi1DN2JnOUhSVmxINnMwOFZDNlRSTUM1SHp2M1RzUDljTW1ORkFaUllRQ1dwUU1IcnNQb3dXY3M4LTI3YjRPelA1Q3FRTmdEMU9OWWRYc25KV2wxVU53MldBcEFzS2tRczZDVEV6T0hwa2VsajVhZ050NkEtWkEtTVg4a2J4b2c?oc=5) <sub>Fox Business</sub>
- 📰 2026-10-13 [Elon Musk targets Waymo over pet collisions as robotaxi rivalry heats up](https://news.google.com/rss/articles/CBMiW0FVX3lxTE0wZjlMcW00aEhKSXZVX2Q3WlNTY3AyckNwblg2ZVVOV0JLUjRnbE5pMUlxYjI0Qmd3ZTRFY24ycS1IZFpwSGFMdHhobEFQRk1hQmd6V1puazVibVU?oc=5) <sub>Fox Business</sub>
- 📰 2026-10-12 [Driverless Trucks Can Skip Warning Triangles for 5 Years as Critics Object](https://news.google.com/rss/articles/CBMikAFBVV95cUxPZnNoVjlPOWlnYlRqNU1Od1Nzc0U1U0lhb1lBR0o5OFNHRTd6VDV3T1lCbzhtc0hVUWIxdHN1M3NLZlczUWlQMGRrVEhRQUtSUlB0VW1oeDVZMkY4RFlSM0gyNzZtMVNVUEFKczBGWU9xTzRjdFo2ZWNuUzVKaFdjTlFEU19sd3NsUU1OY3ZqX3o?oc=5) <sub>The Eastern Herald</sub>

</details>

<details><summary><b>Tesla</b> (348)</summary>

- 📰 2026-10-13 [Tesla Cybercab and Robotaxi’s real advantage won’t be the ride service](https://news.google.com/rss/articles/CBMia0FVX3lxTE1samE2NkJCakN3aW5aak5kMFR2bTlDVGJTN2pyZDBIRjhYUjMzWVpxT01VYU92RTZRLVB3b0Z2c1lMZFdlRTdDQmxRQmVBeUg0OHRrN3NsaldkTThMTGRkbDlKTmVtZlhkQ05v?oc=5) <sub>Teslarati</sub>
- 📰 2026-10-13 [Elon Musk calls Waymo cars ‘pet destroyers’ as robotaxi rivals clash over safety](https://news.google.com/rss/articles/CBMivgFBVV95cUxNeWR1VFNTZ1lVX0FIYWZsd0F4TWVvSEpXN3JGN3pLUldXa3E4U2M5a2ZVN0xZeTdZdFJ5RlFwb04tQzdiZzlIUlZsSDZzMDhWQzZUUk1DNUh6djNUc1A5Y01tTkZBWlJZUUNXcFFNSHJzUG93V2NzOC0yN2I0T3pQNUNxUU5nRDFPTllkWHNuSldsMVVOdzJXQXBBc0trUXM2Q1RFek9IcGtlbGo1YWdOdDZBLVpBLU1YOGtieG9n0gG-AUFVX3lxTE15ZHVUU1NnWVVfQUhhZmx3QXhNZW9ISlc3ckY3ektSV1drcThTYzlrZlU3TFl5N1l0UnlGUXBvTi1DN2JnOUhSVmxINnMwOFZDNlRSTUM1SHp2M1RzUDljTW1ORkFaUllRQ1dwUU1IcnNQb3dXY3M4LTI3YjRPelA1Q3FRTmdEMU9OWWRYc25KV2wxVU53MldBcEFzS2tRczZDVEV6T0hwa2VsajVhZ050NkEtWkEtTVg4a2J4b2c?oc=5) <sub>Fox Business</sub>
- 📰 2026-10-13 [Tesla scales Cybercabs in Texas and halts the number of Model Y Robotaxis](https://news.google.com/rss/articles/CBMiswFBVV95cUxNNmJxMURqdHgwUV9XcXJJVk5iSHppS0VXSG5BR1FlRkhhVGNkN0l2UzFMRF9ucU50bXQ5SUtiTFZHWGp1VlJSM1M5SHFfVFBHN0JSMzRhZEczSlJ5VVluRVpySmptWkllNlpNUkZCbjlBdnhEZU5UQzhILWprNnRtcXBIdDktRF9Hbm1qZ0R1dC1rbm1zUkxjYWFzVE45a2xST1pGR0hmT2hnajRxNU05NmVUNA?oc=5) <sub>Tesla Oracle</sub>
- 📰 2026-10-13 [Elon Musk targets Waymo over pet collisions as robotaxi rivalry heats up](https://news.google.com/rss/articles/CBMiW0FVX3lxTE0wZjlMcW00aEhKSXZVX2Q3WlNTY3AyckNwblg2ZVVOV0JLUjRnbE5pMUlxYjI0Qmd3ZTRFY24ycS1IZFpwSGFMdHhobEFQRk1hQmd6V1puazVibVU?oc=5) <sub>Fox Business</sub>
- 📰 2026-10-12 [Tesla renames its FSD system in Europe under pressure from regulators](https://news.google.com/rss/articles/CBMivwFBVV95cUxON1lxQzRqZE9UNTRHa29FeTB6N0N4UGJ4RFNYWjdEV1FDOGdpdEVkUnJuSnM1U3hxM1F4OThmZllCa29NYmNiQ2JLd3ZSS2RNbHVzaTIxZzRZcDlON2lXQk1KNVNjVnFBTmtLOHBaWktSV04yTElxREVoT05mbHJZenFQVk0xY0lpTHNDX1RZOVJHRjJQMkh2Zm1uZzZNR2hwNG54Q3pVZ1F5LTY3S1lqdkpXcFJYOHFJS09NdEt5TQ?oc=5) <sub>marketscreener.com</sub>

</details>

<details><summary><b>NVIDIA</b> (215)</summary>

- 📰 2026-10-13 [Korea could be physical AIs Taiwan, Nvidia Korea chief says](https://news.google.com/rss/articles/CBMiV0FVX3lxTE0ydkRmQjRBNVBsQlZuQnhJc3hMNm53aTE3OWRDTWYwb3VGRFY4WDVCa281a3l1bnJJX29IUWdrOUR1dk4wZzQ0d0VQSEJZMDlScUJvV0dDRdIBV0FVX3lxTE0ydkRmQjRBNVBsQlZuQnhJc3hMNm53aTE3OWRDTWYwb3VGRFY4WDVCa281a3l1bnJJX29IUWdrOUR1dk4wZzQ0d0VQSEJZMDlScUJvV0dDRQ?oc=5) <sub>Aju Press</sub>
- 📰 2026-10-13 [From Earth to Orbit, France’s Ecosystem Delivers Agentic Computing at Scale With NVIDIA](https://news.google.com/rss/articles/CBMic0FVX3lxTFBTRGZFbUlVZjJzY1M2ZGVVc3hubnlhYmNTTlJCWk5xdWJBeENiZzN2RGRfZ2U5d21tMjNVV0xKcFFSMm5BWDFydDhjT0o1NFBGQlc5aWlEcG5kMUlNY1pNS2J1UGhJaGlwbmhkaTFnYmtoNEE?oc=5) <sub>NVIDIA Blog</sub>
- 📰 2026-10-13 [World Model Odyssey-3 Drives Cars in India After Just 20 Hours of Simulation](https://news.google.com/rss/articles/CBMiwwFBVV95cUxQWFAtTkdQaWVzV09kMmkzclIxNktyLWlQMUdqQjBpSGZCR21SS1VYZkc3dEdCOVBENmU2aDlzTDlMMFdSTnd1c3ZEZ1pZTDRwTzZxQVJXQ2RqQnEyMzRTb1hEV2hRTURpWlo2Zl93NGdKd203VDhtQm9lNzVCMmdoUzdTNTNzX3plZUlyVldmRnVnWlVxN2EtTDI3bFBGdENTYXhxa0UyM2dkV1paNFJuaXVJYlU5VTY3NlRCVU1pand0M0k?oc=5) <sub>Tech Times</sub>
- 📰 2026-10-13 [HPE Confirms NVIDIA Rubin PCIe GPU in ProLiant DL585a Gen13 Server](https://news.google.com/rss/articles/CBMihgFBVV95cUxNcEhOLXktNWxpTUxuVnNBRTQ0d3VEZzVoTl9nMVhYSVJRSXUtYlpsVWw4NFJmcTg3emVkUWlNcVQxMEVnN3JMaEF5MVVzaTEtQTNVTUM3YTVXNk1YYVdNU2VQTEE2X3UzQnZQTlpMOEloektVWEhpMEt0WE03X19WLThNaDJuQQ?oc=5) <sub>Technetbook</sub>
- 📰 2026-10-12 [Nvidia expands autonomous driving safety tech to robots, targets humanoid commercialisation](https://news.google.com/rss/articles/CBMi0gFBVV95cUxNb2tTdlR0dXVveUZJSG9KOFRKcEhzZW1hRlp5QktOVmVVWHVTclB6dkN1SG83SGNKWWFFY3BfRm5WNTNrRVJXTElHYW9XXzlZMWU4V3ZxMkdEZnRiU21NMmJjVXJHVjc3bS1LNDUzWlV2em5TaXdwMW5ia2RLc0MtRXhkaW1wWjRuLUJ2eUVaUmh4MFl5U1gwVlk0QjBqUnJQNmJqY3ctVWpfWVhMNFpyc0ROcElkODFVWVV3MXdzX244ZjVxcVdDS2VzZmFFX2RqOGc?oc=5) <sub>디지털투데이</sub>

</details>

<details><summary><b>Wayve</b> (66)</summary>

- 📰 2026-10-13 [A ride in a self driving Fiat](https://news.google.com/rss/articles/CBMiZkFVX3lxTFBLWHl6Y0t5QzNXY185VFVmcnZzMjJJNnR6T1ZfMkVZbFdOcVVoaXBIdzYwS1lKMjQ4UVNTQXpkYlc4S3p5SGpnbG11OC1ZeTlzdmI5TnF4WHZIYlhIRFRfSHpqQVNZUQ?oc=5) <sub>Focus Malaysia</sub>
- 📰 2026-10-12 [Stellantis and Wayve Aim to Cut Self-Driving Costs](https://news.google.com/rss/articles/CBMivwFBVV95cUxNQ2hZZUdLUlVEWkpxMVFySTF6bXRzSU1pNmF0T21GbjBfYVlZekMtYmtNOWNIQ3NLVVFOSWVvQnZpUUhVeFBPTGNjRG16ZkRqTjNPLVhrN3JLRjlyYWFwQmM4anVqT3JjSGswWDFBdG1ZLW04bkJYczk5WGx3X2t5cE5IUjhiVi1LMktrcDhDM0ZONGtXUGRZVFFyRWZXNTdHM1hEbldxNlNTbDB6NFpnM01BeGp5eFlMeGtHWkJxMA?oc=5) <sub>Konsulteer</sub>
- 📰 2026-10-12 [Rural self-driving cars 'nonsense', says expert](https://news.google.com/rss/articles/CBMiW0FVX3lxTE90N05PaE9WcVBCNGU5aGF6OUU1N21PVTk4Z2dLa3RjU2h3NnVJckt6TVZjN1YxLXJHSE5pMDF6OXdWdDVyb3ppNkZTazl5ZVY4M01jTXVHODUzeGM?oc=5) <sub>BBC</sub>
- 📰 2026-10-12 [Rise of the Machines: What Angelenos Think About Driverless Cars and AI’s Threat to Hollywood Jobs](https://news.google.com/rss/articles/CBMi0AFBVV95cUxQQ0NkcjJkZzFrdmVfZ3pfU0drRzFzazVibFFqZDNTbHRzRWJweEFhOGhfaGp2Zi1DU291bTJMOUo5Y1NaWExNQ3Etc3V5b1A3VXpMdl9CVkpkeWJGalh0QlRIUjlwcHF2SnUyazMxcUYwRGFYV2h4ODhDb0U0bkFLTzhja1V5ZnM2dGJRLVdrUFpNT3RuMjJaS1U3N3JKdmk3NW9Xc3VLaHl5bXgtS3o5Y0RVeDJNUWNBd01vcVZsbmptTnU0LUJkRGR6ZmFZaU1J?oc=5) <sub>Technology Org</sub>
- 📰 2026-10-12 [London Assembly takes hard line on robotaxis in scathing new report](https://news.google.com/rss/articles/CBMipgFBVV95cUxPc2JhYnF5bEpzYnpHRVFiWEdablprSXI1NTR6R1FPVXNOQW9tOGxTMG9SSG5ZandWYlA0Nmgxd3d4aDVQX2w0REIwbGcyTjdvYWFfd1JpNW91RFUyNlZOdVdMa1JwVlZaSlU4NzRvZ3FVamdEbzFfX2lYZFpCODR2cDh2N1M3R3pFMUdXZDg2bk9SWWdreE1mSmZDekhNc2JZOGdlOWZR?oc=5) <sub>Professional Driver Magazine</sub>

</details>

<details><summary><b>Momenta</b> (95)</summary>

- 📰 2026-10-13 [丰田铂智3X销量累计15万辆了，还有人说传统车企落后吗？](https://news.google.com/rss/articles/CBMif0FVX3lxTFB6RUQwUzI2emtFel9lZmpRaW5EdHZYMjhQZDJ6ZjhDNG5JdGMzSVlvdkJSN0dlWTZoeHlWb0JpQlRSUVNTb1BDVjBkZ0xDZDl6N0pKN29IUmN4SWhDNUoySGp6am9mNTA1WkpWTTJNUzE2RnJ3dDY1VHREQ1ZGYk0?oc=5) <sub>新浪网</sub>
- 📰 2026-10-13 [ID. ERA 8X用第一梯队智驾，撑起合资反攻底气](https://news.google.com/rss/articles/CBMiW0FVX3lxTE51MFZ6R01Oa2NvVFNHOEczakxUQXpVX1Ewb1U4TWhLSlFWM0FvaE50T0EtWDVOcFoxdDNtWWQzYXFMOUtBUlJYclZ3NkNlb2hHclBEWWFXbFR2Rmc?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-12 [权益价20.68万元起 上汽大众ID.ERA 8X正式上市 搭载Momenta R7世界模型智驾方案](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPN0w5MjlRM1U2bVJzQWl3M3dzaTE1aUxOMkRkREhaWkpiWGNxaU5GN0hJcnBhOUdSeld2SXVmVTZNbXh0TzYxTXVCTUFueUo5TUMtVlVLYkxXMHJpSm02Xy1jUEZPZ0ZQbHdrc1p6ZUswWk9YdkxJVWpZbXJEOE4yR252Zk1IYjdq?oc=5) <sub>搜狐</sub>
- 📰 2026-10-12 [HSCI / HK Connect Dec 2026 Index Rebalance Forecast](https://news.google.com/rss/articles/CBMijgFBVV95cUxORGtDMERfR2Q4SUVkSkpKQkJlcDI3dlFmQVM4X0hjdUJNQVZxSUtqbFBVZWFFYjdMOTJUa1V3b1NKTFRGekVMSnpoTFN1OHl2RTFpNVlSakRVUzFUdWZQZ1lWcWphU1VCUnEzMzNhOEJ2d2RXZnA1azNqMHVfQnYxQzFiMDViUW5aOTR1bkVR?oc=5) <sub>Smartkarma</sub>
- 📰 2026-10-12 [全系标配Momenta R7智驾，上汽大众ID. ERA 8X 20.68万元起](https://news.google.com/rss/articles/CBMiW0FVX3lxTFA0U012Y2xabDNCUkpZM0dsWmxEbWY5ZERVaXFLVzU0RU90ei1mQmpnUnIyTlBkVFRROVQtSW5WQlpYQ3lhemYyVjJCQS1wejBOSDFybXBjVDlzSkU?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>XPeng</b> (294)</summary>

- 📰 2026-10-13 [Xpeng unveils YOYO robotaxi to target autonomous driving market](https://news.google.com/rss/articles/CBMirgFBVV95cUxNU2Znd1Y4WWRRdFpEMnJHWDNrdXFheEdXWnRIQllYbGkzUERNalZNSlpVdzFRenE0OXQ3dTFJaUFEUXZSTll6VjlUU1JiOC1Hd0dpX2JqeUJTSDc5VXJROW5nVEstdGZGZ01taVRGVlRxSU40VmZKUC1JVTNRS28zNi1RVmN4SUpEUnozRVR0NV9TdFhUZkhkTnk5Y0owb2lWRmhSN3FPZ3h3VnBLOGc?oc=5) <sub>디지털투데이</sub>
- 📰 2026-10-13 [XPeng confirms luxe new arrival: 2026 XPeng G9L coming to Australia as alternative to Wey V9X and Zeekr 8X](https://news.google.com/rss/articles/CBMixAFBVV95cUxOdDN4NDZ2UkRIQzJIYTR5eUNMbFZvLTRMSWJsaG5PLTJscjVUMnRxOEIzZG5ycnVBT05FQ0EzN2hhTzdRVmVURHRTQ3psQUU3RzZuNmh5Tjh5Zmh4R2NNREo1cmxiVmN3aHcxMFYxb2MyTEJoVTNWMVhZY2o2Ql9tSko2SlZ0d3o2cjVZdlV1SHFQd3RGZ3o1S1I3SzV6TlJJUmZrLUg1eFZkRG5Wc3RoU3hEQVhEbzdfaVlqcVAyeU80TVVO?oc=5) <sub>CarsGuide</sub>
- 📰 2026-10-13 [XPeng confirms luxe new arrival](https://news.google.com/rss/articles/CBMiigFBVV95cUxQVTZGS0M2eEZXXzA2b05CZnp2RE5WejY1UHRXZHRvM25xRGpSNmxjWTR5TDR4NDNITXh6c2FuWVpMOGxJcTJ3NTBaMU5la3k5U0lwQmtyQndxMlpQMUx2anJtbkZJbGJmMk9faUd1NWRvWTJ2anp3eUVVSDJHSDlfOVRGSHU4RWM5U1E?oc=5) <sub>Bega District News</sub>
- 📰 2026-10-13 [小鹏G9L巴黎车展全球上市，法国市场售价74990欧元起，小鹏NGP首次在欧洲开展大规模公开体验](https://news.google.com/rss/articles/CBMifkFVX3lxTE5JVXBleUcxWmREZjFtWXFVQmZPYTNDaE9kVERtMVRBN204VHNOTnl0dkppbzh3N2pjNS1nWGJMWjVMakRpNHU2Q2NWMGRuRjA3WnlEUnN2U0l6TzZEV05tX0NzVS1DOGNVdm51dzk0NG1aWFNENE4ydGFrbWhvdw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-13 [快充差10分钟，小鹏MONA、零跑C10和铂智3X谁更省心？](https://news.google.com/rss/articles/CBMia0FVX3lxTE51Z3VQX1pPZHNzcGF5RGZZSzhndVJZUzIwck4teHoyMVVDRVp5X2ZHZXVySk1XZXg4T3dBOFp3ZjBRSVNraDRNRjRtczFxQkRsTzFNcDBWakQyazVpSXQ0bmpwcHpfS3Mxbm1r?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Li Auto</b> (159)</summary>

- 📰 2026-10-13 [Li Auto i6 EV crossover to reach Europe as Li 6 in Q1 2027 with 8 European languages](https://news.google.com/rss/articles/CBMivgFBVV95cUxNRTFyYzVMenJ4MTVfcVF0aE9Uc3VQZUphUTFtbWVpdEU2OHhqb1c3ajFST1hoV1NnMGZHUi1oamZ6blN2dXhETEw4UDRLcmV1aXU4Nm80dHV2TWoxbEhYRTNpcXNxZ2EzMXVDaHdPVmNjeDh0OTFCQVJ2V3dvT0NCeTJJRkh2VGktT0JkY1FCRTJRNW16MlhSc095ZVA4RVlNM1Q3TWR3SlRXc3BNdnpXU1RnUVRpTlBEbjMzbHZR?oc=5) <sub>CarNewsChina.com</sub>
- 📰 2026-10-13 [Europe’s biggest auto show is now dominated by Chinese cars](https://news.google.com/rss/articles/CBMirwFBVV95cUxOU1g1cXpSWEVWWWJFOTRGamFVRTUzT0RPdWMzemtfS3RrNFozdHYyYm5FdTRxWFZVcDBBUFZ5UkltYS04MEotUDZya3lva2xGVjl2aTRCc1g0T3RQbjVGTnJFdlI3bm9lbFluazdIeFUzRFhPT0xhUjhCSU9OYXNWb0VOeXVhLXdJUnhHVWp3Q3c3bDRVWldTcTI1V3B3ZEk2aWxSRXRDSlhRNUxWQmFR0gG0AUFVX3lxTE05S3U5T1VTZGhUNGlzbmRkSWJSOEJmcTVCdHBLNktwMW9pV2wzV2lrLVB0NGlNSmJOaHA2R19vWlk1eW5oM0Zjby14TndheGFhMzBiQ1I1ZEUtSk1jRFR0V3RFWGMtak4xMUZvb24zSGhwcHdDOVJsOFpnLUJxVzY4clIwZ3MxRFRjTEdyZXNrb2EteDNYb1RaX3N2T0hFSk9nLXJLVXBaQ09WczJhMksya3hoVA?oc=5) <sub>Livemint</sub>
- 📰 2026-10-13 [2026款理想i6不降价，要对老用户负责](https://news.google.com/rss/articles/CBMia0FVX3lxTFAzNVNyOTNLZmlvS1Z3ZmNPaE1nZ2NOQS1HNW16b1N1TTZYdnRRSWgzWXlrd25qVUVkQ1p0dU5QMDNYVXNlNlJDd1RfdkhBT2VCWWNlY3NyX0ItUDlNdUl4S0Y0eGVRbllHeE1B?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-13 [新上市的豪华插混SUV哪款值得买？5款近期上市新车横评，全新XT5值得优先看+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE1aaVExSDg1dkxPdW85b2loWHhTbnpjc2Q4SllkOHY3LVNxNm9BWlloLUhkSkJVNEN1UzhtOTBEbzN3eXh5T0RYNWJQbXYxZWYwSU5pTHBGVzVsRlVNQWEzWE0wZTFCWWpvUXEtaC1oU0c4dw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-12 [放弃理想L9选了它：一台让全家不再做选择题的大六座SUV](https://news.google.com/rss/articles/CBMickFVX3lxTE1WTWxYeVRqZlRFdFc0cm5zUGVFMzVZb2xSQjRKMF9SZ29ja3d6N0xFX0ZDeFRQQnRZRFVYeXBWcFlVVm1Oc2ZNYnEwTl94SjI2bWFnbEczZ3RPc0tUNFBXWDlqeEhlSHc1V0NWcEZGU1FEQQ?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>NIO</b> (144)</summary>

- 📰 2026-10-13 [【视频】23款蔚来ES6租电](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9fT3dOdXZjaFF4Y2FvTE53TkZNR1g1bUVockdMdURRUGhQcmRzUGlzaE9wZ0pNQUxCaXAzWlowLWVwYjFPMXNnR09FZ0NMX1lybVk5bE5EYlE0ejg?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-13 [【视频】2023年上牌蔚来ET5 75度买断](https://news.google.com/rss/articles/CBMia0FVX3lxTE9uUklFRmlzMXpXTG9BY2x0dG9uSWdMeERpUGRYZ0M5ZGs1TW03QVlEZ0tkOEp2cUw5eFZqMmtLQjlJTHEybWNtc0ZxdGt1T3pFN1NSaG9kTTFxcExBWVhJSUpEVlJ6LWROaGZJ?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-12 [跨省自驾2000公里实测：理想L9、问界M8、蔚来ES8和神行者8，谁更适合远方？](https://news.google.com/rss/articles/CBMickFVX3lxTFBZaU8tOWN4NmxPdWNqR3BMbkY3eXM4aVFVbHVEZUl6UVhJbFpWZHZYOWFDYWZ4bWJDR0Q0OHVyN0FBblYyVWNDSFh1aldMOVhQRVRfWkhxeTdTbTV3WGs5a1ZYSDdkTTdFSThzY3R6U1hrUQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-12 [【视频】蔚来2024年et5](https://news.google.com/rss/articles/CBMia0FVX3lxTFBGWklRelYwdHBDVDZWcFFWZGsweXVkemd4ZVRNMGtzTFMtbTBsc3Y0MGgwbzVIV1dsQVJzSXB1OVlOM0swSzJqejVkQzd0OVBqdEZlSFBBY21ZcGZySTFpNE1Fc3VyUW5lR0hz?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-12 [蔚来ES8值不值？38万起3.9秒破百，但换电与智驾要怎么选+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFBZSGpNbGdoSkV5WXo1eENWdmh4Vmt3TUZka18yaFBKYXpBUmEzUnJQLUlMaE8wcS1tZFBsRDRVa285SmgwQnJINzVNbVRWamN3TzVoMWFscmZUMDIwNHBmdWZYQy1FQUtSVURKbEc0eXp1dw?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>Huawei</b> (401)</summary>

- 📰 2026-10-13 [AVATR Showcases Three Models at Paris Motor Show, Targets European Entry in 2027](https://news.google.com/rss/articles/CBMi1gFBVV95cUxOX243MGswandhdUE5Qko0TG1HV3A4NW1mUldlWVl1a0VnSURrODg5VVhxZDdtdHpOVVhTVi1WRXZralBQNGZCZDh0bXREQkh3OG1SaEdwLVIxZk1ZckM2Q2dDeDlTX3JIRENhYWZVS0Rxb0RfMjBQN2FPWTNjcHhXeTV6ZWpVVHQ2ekg2bFFra1dEUWY0MTBQYWFpWWdHMi12X2lJdURKSDNKODY0M0xmN0o3dzdmVWNlSVU4ZFZGQ1BadWN4cW00UUl2cVJNdmtWckFKUENn?oc=5) <sub>Gasgoo</sub>
- 📰 2026-10-13 [Nvidia's China AI-chip share falls as Huawei closes gap, report finds](https://news.google.com/rss/articles/CBMilgFBVV95cUxQakNuckZoYmwxVFJyQWQxWHhvNEtzM1lkcmEyOGZnVG90TW5jaWpLUXBac2ZQemxBblVhR2pHVnp0MFM5Nnk1WkNJak9INGw4Sm1ZcTEzWUlWWEdDUENsWUlDNlpoNFJTYzA1ZVdVbDVOUGVaYmdtbTRyUTNFQk04NTN0Y2I2VVBWM3c2V0FUT0FDcl9oSmc?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-10-13 [China smartphone shipments fall for sixth straight quarter - IDC](https://news.google.com/rss/articles/CBMiowFBVV95cUxQWjdYR2FnbGhuMVBVb0o3QnVweWlMblpJal91STF2Q0NHXzBISXlxTjY5dV9iY3hUNW5NczlvLU5TeFlqc0pTTVpibGZhUXlJUWdzQXFHS2xUX0F0TWEyQVJzNkEyc0txUFctRy12WWx4dUQ4ZnRGYmJaNm9yQ0VWV2ExSGVwRDZnNWpmek4tdzhyQVNtblVKaE85d0pTeEdWaGl3?oc=5) <sub>KSL News</sub>
- 📰 2026-10-13 [Nvidia AI chip share in China falls as Huawei catches up- Reuters](https://news.google.com/rss/articles/CBMilAFBVV95cUxOZUZsb2dHV3NNb1BsZ1NRcWN3ZlNGVVh5YjNsR3QzS1RqSnZDcFViWEF2eTA0eVdEZkdZVVBnQ2d4SjRIcy1PSk5IQmc1WlhWam9TbnlGTW9hVDd2UTgyNXlZa0NfWUQzeG4tbW5tWUp0cU1TTWxCbk13MVVQSS1Ld3FaNFVscV81UnJrc1lleG9MUEZJ?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-10-13 [China struggles to shift tech firms away from Nvidia chips](https://news.google.com/rss/articles/CBMifkFVX3lxTE4yTW02dXlqSmV1dWtmM1RtaFpJMzdZaklEVXVaRkhsWk9RdVJWRGVGZUtQUzVELXlZa1NoSGpvQ1hRcTVKNVJJYkpPZW5WMnREa2JWU09uRjlQTVZ2eDhob19lZnBudks2d0FEX0VFOEhRWm85VUd0YmpXWjUxQQ?oc=5) <sub>Crypto Briefing</sub>

</details>

<details><summary><b>Baidu Apollo</b> (58)</summary>

- 📰 2026-10-13 [Baidu opens free Tung Chung robotaxi trials](https://news.google.com/rss/articles/CBMie0FVX3lxTFBtaVl0RjQtXzRHY2dNNzNHZEEwaW9QQ3pFMTlrc0dIaVBqRUhubVRZdDI5ZXh0NnV2VDFKcU5KQ3BoNGdEUjdCNHBVWi1BN0hjOWhKVFZxT3NHRGhmckVwV1JqUUZQbG1XdG9JeXMzcjQwV2hBc2NMRkp5RQ?oc=5) <sub>Dimsum Daily</sub>
- 📰 2026-10-13 [深化智慧出行合作 韩泰iON携手萝卜快跑拓展十城自动驾驶版图](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBRSFp5M1hZZkM3Z21vS0xJWS1vOHkyM3pYMWJkMWNlSDBBcHc3aGpFT0x4T0RiSloxNDFlZFhIdHRzQjRmWU44UEtZMXlHM242OEdLTkZkR2k3S3c?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-13 [Waymo完成50亿美元首次债务融资，特斯拉Cybercab单日新增注册150辆，小鹏Robotaxi启用小鹏悠游](https://news.google.com/rss/articles/CBMiVEFVX3lxTE9JZFBKMTdRVUxUUHhQT2RzZ1EzTWtGS24zR3BfX20yNk5Uek42LXA1SWc4UEVEU3l5SXZoY0xJRVFlT2tycHgzWEZEZzhuY1gtZjRydQ?oc=5) <sub>虎嗅网</sub>
- 📰 2026-10-13 [【视频】骑了10年摩托第一次在路上被这样打招呼](https://news.google.com/rss/articles/CBMia0FVX3lxTE4tblJESDFLN1hsWHVRZmFHRUZjX0w3VHZzbEZCY1lPMGRRRlFXUmdVS2p1UC1VYXNUQ1VJdFF4UC1Lc0pKcjZhNlB3aHVGNTc1dDlYdUJQejYwc3ZhenhFd0JXMWpxUWpENXVJ?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-13 [三菱全新跨界跑旅EclipseSportback预备正式上路！纯电驱动](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1vT0VkRnBqRjF3VFVZV05sOEFubFpLdFgyMmdrYjM4UUZDMzByaDNhRE4tSjUyRFBHMVBJYXdzRVd2VG1iUVJpRFRUcFl4V3gwYzlmdjNjOFNlb0k?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Pony.ai</b> (136)</summary>

- 📰 2026-10-13 [I think the city where the robotaxi runs safely is a city where 'physical AI' has become commonplac..](https://news.google.com/rss/articles/CBMiU0FVX3lxTFBnSk9fZWZWVzltamlXSDM5UFQwb2N1bFUydV80a1pkbHdKV1I0RXlXWTkzdU9qWXNObWlJenBNRmNfMTZFMzhha2d3VEp2MWJfR1ZN?oc=5) <sub>매일경제</sub>
- 📰 2026-10-13 [小马智行-W盘中跌超10%](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBTaGkwYnZPSXBUVjlHeERzRUs4Z19SYW9iOHdBWFFxeVktVWk2azhDZ2ZHTV9VOFhYSGJFV21lZzRYbm5qV3lWaXpNVmNHTGRoUTlkODRaR0kzd0Ni?oc=5) <sub>www.caiwennews.com</sub>
- 📰 2026-10-13 [Waymo完成50亿美元首次债务融资，特斯拉Cybercab单日新增注册150辆，小鹏Robotaxi启用小鹏悠游](https://news.google.com/rss/articles/CBMiVEFVX3lxTE9JZFBKMTdRVUxUUHhQT2RzZ1EzTWtGS24zR3BfX20yNk5Uek42LXA1SWc4UEVEU3l5SXZoY0xJRVFlT2tycHgzWEZEZzhuY1gtZjRydQ?oc=5) <sub>虎嗅网</sub>
- 📰 2026-10-13 [粤芯半导体登陆创业板，早期投资方广汽资本收获51家上市公司](https://news.google.com/rss/articles/CBMiWEFVX3lxTE9mLVBUX1FmNVBNYmVQeFRBRFN0ZDV3VWhTVGpmREdEN1lnR2N6d3RYd3FCMUQxYlhBbDZtdlVIT211cU4wT19uX05xalU2dnlIckc5aFBlMm8?oc=5) <sub>36 Kr</sub>
- 📰 2026-10-13 [美股存储、光通信暴跌，Lumentum跌近10%，中概股多数下跌，小米集团跌超6%，霸王茶姬逆势涨超6%](https://news.google.com/rss/articles/CBMiggFBVV95cUxObjF2Q19XMWt4NFN2ekFXclk0cWlDZkIzM0ZHMk12RDJTVzNud2JjdEtxLXVqS2VtTVd5aDZ5NFY3NEdQOUVFTjBTUEtWUE9JTk9JVEN5YmtKTjZ5SE1pVnd1ZWhnSWxrcjByNUZrRTUzaTN4dlZWNEl6U3JaZjIzMWJR?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>WeRide</b> (134)</summary>

- 📰 2026-10-13 [Waymo完成50亿美元首次债务融资，特斯拉Cybercab单日新增注册150辆，小鹏Robotaxi启用小鹏悠游](https://news.google.com/rss/articles/CBMiVEFVX3lxTE9JZFBKMTdRVUxUUHhQT2RzZ1EzTWtGS24zR3BfX20yNk5Uek42LXA1SWc4UEVEU3l5SXZoY0xJRVFlT2tycHgzWEZEZzhuY1gtZjRydQ?oc=5) <sub>虎嗅网</sub>
- 📰 2026-10-12 [Fast and furious: Driverless race cars navigate the track in A2RL league](https://news.google.com/rss/articles/CBMiwwFBVV95cUxQd2VRY3F2MjdhdHhWelh5NkIyZXNHbll6UTltdld0OEROR0JIZFFFMjhkRERkd0p2bnhobXF4RDFfSmtad3JoazlZbFBuMFZDbDJYLWFrOUFXZWZTSkUwSXRtODhIWU0wR0tLeFB3SjJCSExQUEJ6a1pOaGlXdjYwbkdBYTJydWEwWVhVMTh1N0FSeXpZOGZhTjZQUWtmSDFvMm5oV2FvTUhDeGNlQ2dwa0hwZnlObmtwR0pOY015TVhQM2c?oc=5) <sub>The Star</sub>
- 📰 2026-10-12 [港股异动 \| 文远知行-W(00800)涨超7% 公司加速推进海外Robotaxi 部署 商业化进程提速](https://news.google.com/rss/articles/CBMiXEFVX3lxTE82dmUwektBMzliRTZIdjktTlZTQXZpbENvclNHMWlEUDgyTlhQRUp5VTZJNEVMdTJzSjJCejI4dmdkUlRXcm5SMjBNYXU1Z3VLSW1Na1ZMOG9USmN5?oc=5) <sub>Moomoo</sub>
- 📰 2026-10-12 [港股午评：恒生指数涨0.17%，恒生科技指数跌0.55%](https://news.google.com/rss/articles/CBMijwFBVV95cUxNMDRUTk1lRTVuaHAzejZnMl9EZ1BIVWFDRm50c2tGdzNwRFpBLTV1Z2wyb3JYNHdJbUl4U1oxRGZqVDE0YlpocUZmLUdyamxUdDZqbjFJV20zYVdoaXhzU3JBWkwzZ0RLa2RmQXVhUEkwREZuYnl0Y1NHTjhyYkJMZ29Hc2RhNVktbklJb0M1OA?oc=5) <sub>21财经</sub>
- 📰 2026-10-12 [智能驾驶板块走强 图达通（02665）涨超23% 城市NOA渗透率突破20% 带动产业链放量-证券之星](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1aU2wwQ20zNWNmbWFLX283SXptcTFuMDRiMWFwNU8yZ2hwZG1jNVRGcTVkb1hrNS1BWjN4YWhmRnlMX2NwOTM4UnJLbF91T3h2VXZSc3BENmk3X3dCekE?oc=5) <sub>证券之星</sub>

</details>

<details><summary><b>Horizon Robotics</b> (196)</summary>

- 💻 2026-09-29 [HorizonRobotics/Ego4WAM](https://github.com/HorizonRobotics/Ego4WAM) <sub>GitHub</sub>
- 📰 2026-10-13 [【视频】深蓝推出两款PHEV车型，满足海内外用户对动力的多元化需求](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5OM2Rta2dQd1hRaE9UWmQ5aHgzR0x1eTZRdElubzJLVWU2Z3hDVk1wcFZjRUZOTVlVYWFKMnM2ZDFFX1VGaUVWU3kwaFltR0hRbkhWcW5DZ0VSTzg?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-13 [【视频】都是方盒子绿牌车？怎么选#传祺越7#吉利银河战舰700#长城H10](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9lVTdLS3lIVFZQVmxEUFh5U0paNUZVMHVOak1tbkppNXZBMm1RUkE1VDYxSGNMLWpReGJoXzMxemwtTVVPRXJjVC13SkZlcEZ3cGdYcHl3ZDNYLWc?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-12 [德系智驾新标杆，大众ID.AURA T6与丰田bZ5、马自达EZ-60的合资纯电SUV高速NOA深度横评](https://news.google.com/rss/articles/CBMickFVX3lxTE9WWG8yWDRpRG4yZDdQMmR3S0FhU1RycWlmTWhEMG9ZbGdFb0V3WXpUSlNqTkhjaXllZVREckNBZngyVG9GeUNiMTA3T0h2MTRJWHZQM1dUM1dSa05oQkZhNkJxUFAyMU9IcFdHY2g2RS11Zw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-12 [China's autonomous-driving veterans pivot to embodied AI as capital shifts from "storytelling" to "demanding results"](https://news.google.com/rss/articles/CBMidkFVX3lxTFB2Y01aZHNqandfdHZSRkF3MGYtTWw0eWVVbk5FdjdNZzBHbGd5Z2lQYm5jelQ0NThHMWRIU2Vfd3hrU0s4WFZBekNXRDJWQ3VneDZhak05MTI0RjRVcUJkXzJMM25aWnpVSVlBZ25WQ2V2MndJdUE?oc=5) <sub>BigGo Finance</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (28)</summary>

- 📰 2026-10-13 [TomTom与元戎启行达成合作推进基于AI的自动驾驶技术_车市动态](https://news.google.com/rss/articles/CBMia0FVX3lxTE9XcTVveVNlN2hfeVcxOThFNUd5NjdLY1JJNTcxWFdKU19Ic3p0bkVIcHBNdHFEdnBHVW41cWZwTXpuazJsRDY5cmtGVmdoQ2R3UWVscldLMFpDYzRUaTZuTUtqc3d5Z2pDTjdn?oc=5) <sub>中金在线</sub>
- 📰 2026-10-12 [TomTom and DeepRoute.ai partner to advance AI-based automated driving](https://news.google.com/rss/articles/CBMijAFBVV95cUxQM25CX2RxVmJzRkc5bmNUMGNTUGxlSU9pOEw5d08xb3ZyWjEyRlNtcVJvVElNenQ3VVhlQ0ZhcXd0bjh5OVNnOG81LWlOUnVRSTZYeGFOaU53V2d0U0F0WjZpcVJHMXR1VkpSSjFjLWdFOFM1NEhOSUYyVUozb0VRc1FKeGRIdjVqYndUbw?oc=5) <sub>Yahoo Finance UK</sub>
- 📰 2026-10-12 [费莫一刘念邱：智驾无图的经验，也能迁移到机器人 \| 物理AI 50人](https://news.google.com/rss/articles/CBMiekFVX3lxTE00amwwNk9KSGJlbUNzcXBtdWFQZEZpNHZxcVF4ZHJoTFg3T2lhUjlZREU5cUx3X2hYckROWEgzalBDYURDVThkZk1LMnZlTmtvQUJlbTZ2RmtVNGJGczNGMEdxNkpURHRXQS1rQUs3UXhWN2F0Nk9HWWFR?oc=5) <sub>雷峰网</sub>
- 📰 2026-10-12 [TomTom Partners with DeepRoute.ai and Will Present an Autonomous Vehicle in Paris](https://news.google.com/rss/articles/CBMi1wFBVV95cUxOZlM0QS1zV1N0QkY5UUdSQm5IY1dSemhpNWVfdkx3LU5VRHNuZUJ1U3BzZWZaRG0tdTZvTUxQaHAzaHM1ZVdGeDRUdDJHX1pzUWJRR1pFNVNoZVhSTTZEWUVONGxEMTRHZWFoNjhHYlEyczU1c2QxMmh2VmR0UXkya0NybmNiWU1ab2taSDBMeXd1YVpZNWZVaHZDajNmc2FoeFkxcjhETFNPRTVqU0xRM2RpRHUwM1hEWm14djRBMGwzWEo1bnV0X1I2Z09EVUw5LVVnaUtQRQ?oc=5) <sub>Idéal Investisseur</sub>
- 📰 2026-10-11 [VC的钱，正追着智驾“老炮儿”跑](https://news.google.com/rss/articles/CBMiTkFVX3lxTE52WjRJaHIxTVAwdVVKQnVpSUkyUGVzc25RclM5REE4TnRuUUcySVdoSGt4aThERXJZSlZMcFZjem94NUhQa1ZPV0NKWWp6QQ?oc=5) <sub>36Kr</sub>

</details>

<details><summary><b>Mobileye</b> (13)</summary>

- 📰 2026-10-07 [Uber invests in robotaxi provider Verne](https://news.google.com/rss/articles/CBMigwFBVV95cUxQQkxEa25xSjBNT0ZJMzZINk54a2txS3k0S0pvTU4wZEJ5eVhHY0FNRWlyaVdIcVhYdmlPQl9HVUsyUnlkcW1UVzRVc180dHNCT1hXV3ZUcms3Mzg5aUoyZENTUWU3VHJtRlFuQmp0dWpQRDlmU2xlSDQ1MnlEZW11YmFGWQ?oc=5) <sub>electrive.com</sub>
- 📰 2026-10-07 [MOIA America Launches First Autonomous ID. Buzz Rides](https://news.google.com/rss/articles/CBMixAFBVV95cUxQY2FmM1hNRDEzV0c3c2NSVklIUDBPU1VrbmRmNnRLV3lNRzRITUVHUldKcVNYajNSYXJkdTJmbzRGeWt3V3ZrcXlmanBfR2t5cjRKZlU3b2JHbUg3VUx0ejdIS2ZUT25DRm5KTGtzSm1OaEhhQ2Zsb2Zhb0tHMDlnaWhnOGJHLXBvYk1GYkNYVFJRb2M2R3BmamRnN3RMZlJ2a3JlSGc3VnNmcXBtVDdub0s2VjhXSDhKVjFDR1pIQjYwLUpI?oc=5) <sub>Fuel Cells Works</sub>
- 📰 2026-10-07 [Uber takes a stake in Croatian robotaxi startup Verne](https://news.google.com/rss/articles/CBMikAFBVV95cUxOMkFfTDhoaldrejJpdUNUd1JvRXN1MlZwYVZQRjdPQ19FM2oyWjgxTndscUdGWFVZaG5nSWVKNWQ1dVYtNzFNZ2t0VnFwaS1mOFpneG41RW51M19leE9XSUN5WjhGbjF0ZkUtRVI4RDBiSUxtX2ZCTDBUekNRN3p1ZXZzUFU5aXJ0cjk5bHA3aUU?oc=5) <sub>Dealroom</sub>
- 📰 2026-10-05 [Moia’s autonomous shuttles start first passenger tests](https://news.google.com/rss/articles/CBMilgFBVV95cUxPaXBLWlk2ckZabm9UeXdOV1lCZTRjaDBkVmk4bDNVRWVMZkxKUEVTOVBqZERzWGlySkROdEs0bkE3SURjaG44c1Y4M3lsM0NmSG95X0diNlY4cGJoMUp1UUMxVnFkQ2Y0UTR2UDdtdTFzczBDSHpId3ZmWDltWlY3Ulg1bHBYMzJweHhDOWkzd3lyVWwxSGc?oc=5) <sub>electrive.com</sub>
- 📰 2026-10-03 [We Found Atoms, Rode Wayve and Watched Uber’s Autonomy Clock Speed Up｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1QZjNLZlpHR2ZtcHFaUDF5bEE3ZktHQlNoN0E1amxaVEg0eUdQbElIVlVVZk1JdTlqZG1kbGZYVTBvZDdKRDRKVWlqa2dRNDF3aTN4dEpmdTdxX0dTVnlj?oc=5) <sub>finance.biggo.com</sub>

</details>

<details><summary><b>Aurora</b> (63)</summary>

- 📰 2026-10-12 [Self-Driving Trucks Win 5-Year US Beacon Exemption [2026]](https://news.google.com/rss/articles/CBMif0FVX3lxTFBBUmFCem5ScXN0T3VNUU1lLVRvTjIzWFRndlh2NkJkY3ROXzkyNTQwR2dnWEI5ekpHeGpGLXZ1a0tIS3EwaVlSZlJrX1RoQnRhWkEyWlZzaTFnYXlGQkJOWUd5emNWbG9Ha2NWTTJQVGQ1VVN3X0htVmY4TGVFWmM?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-10-12 [Driverless Trucks Can Skip Warning Triangles for 5 Years as Critics Object](https://news.google.com/rss/articles/CBMikAFBVV95cUxPZnNoVjlPOWlnYlRqNU1Od1Nzc0U1U0lhb1lBR0o5OFNHRTd6VDV3T1lCbzhtc0hVUWIxdHN1M3NLZlczUWlQMGRrVEhRQUtSUlB0VW1oeDVZMkY4RFlSM0gyNzZtMVNVUEFKczBGWU9xTzRjdFo2ZWNuUzVKaFdjTlFEU19sd3NsUU1OY3ZqX3o?oc=5) <sub>The Eastern Herald</sub>
- 📰 2026-10-12 [Werner backs autonomous trucks, but economic and liability hurdles remain](https://news.google.com/rss/articles/CBMitAFBVV95cUxQWDdjRGZpQkZ4VzdjcFFEVXVLSU5VOWd1eC1RTFJVX3VBZi1zZHgzZFJLMk8tS2hCTjVYbURoSnVxRkRkSzYwcmw2R2thcWRMYlJsTE1XbzZCYVhmMTAwSEVudmdHMUE2bGJRWjR2dnBwM3V0Wk9meEl6WW1SeDRSVnY3UElqanZjOVd0TTZpd3ZrdWtCX19fQk4xV0VNTlNWVlVuUVFnZ1JheGFWR1JlTFhZOUk?oc=5) <sub>Trucking Dive</sub>
- 📰 2026-10-12 [Kodiak, Charger Launch Autonomous Trucking Dallas to Laredo](https://news.google.com/rss/articles/CBMirgFBVV95cUxOMFNUUzF4Y1UzbFd0Yk9XR1ZvREhlQnpuSkp2dzdrdVBJMUpXUDFKaGZvM1ljSkpIT0oxSkx1M0ZZb2Z6aWxhVjFlZE42bmd5Q3M2eFR4VkptSUE2SG9FQkJ0TmViTm9WemhoSGljQXRQZ3FoUVN5dW4yQlRaMmdJQjlmTmRpa0hNX1RuX3FYUmdHcGhUY09xV04wR25valh4QW53LXJKQllyNnQxRlE?oc=5) <sub>Hoodline</sub>
- 📰 2026-10-11 [US grants self-driving truck makers five-year warning-device exemption](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNVmdoOEUzeWJzaUZ2TFo4TGkyTnNxQXFEM1hBX3poNEFTZTlDdXZZQ2x0M2MtMzBqTDlqNzduU2pkR2hMSTczeVAybEVfWEJoNFF1eTEyckV0QlJYQ0FoTzB3QkM4R1h3YWZiTi10QlI3LTM5WGVPVUtmZ19kN01MMjJVVFQwMEpQ?oc=5) <sub>mezha.net</sub>

</details>

<details><summary><b>Zoox</b> (76)</summary>

- 📰 2026-10-12 [Jeff Bezos Could Take Blue Origin Public. Amazon Investors Just Got a New Space Question](https://news.google.com/rss/articles/CBMimAFBVV95cUxORWRPLTFjQnM0WXR3NUdEMGc5VWU5RWVoZXo2bEZxV1FWaDBCTHZNeFEtbHhYRGlrMHozTS1KYlQ2Mjl6dUYwUWEzMXhEOXFIUDFELXFCMnpEWVhfdW1Qa3VhTGZZaUlhUU1DamlwX2FYWTFORUxWWGVzLV9oV1piTEozZHIyQzZ3Y0ExTnpaTkh5ZE8ybnY3eQ?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-10-12 [Amazon in talks to buy AI startup Decart for $7b](https://news.google.com/rss/articles/CBMieEFVX3lxTE90aVNkRUVPOW5nTHBMWDM1YlhiLXJ2THFISE1VMzZxalM5WEdfbjdpZ3lpWUNicGRiQ1lBYmNKal8teV8ydmJTN001OG91dDlVYkZkNG00STdtalJ1alE5ckNQSHNOOXFHNjEyaXo4ZEZ2RHA0U1ppNA?oc=5) <sub>Tech in Asia</sub>
- 📰 2026-10-12 [NHTSA Launches Investigation into Approximately 1,000 Tesla Cybercabs](https://news.google.com/rss/articles/CBMidEFVX3lxTE5xZnV5d3B1VDZCS1BDNUZoQjgybF9WLS02SDNrV1ZBUmpxbGk3M1MzYVBmM1F1NXo0V3VUT1pRRkdxZFl5TmpjTF9uRndRNGVvVlBmNUFkQndNVFlkLUZHWFZzRkxYNGkyYmtMN0puaE1ydmFV?oc=5) <sub>https://www.ababnews.com/</sub>
- 📰 2026-10-11 [Texas Roads Have Become The Testing Ground For Driverless Semi Trucks](https://news.google.com/rss/articles/CBMie0FVX3lxTFAyVTJ2bGJpZmtSaDFMQTF1dGxOQmdmTkpSLXVYLU51NmpYSmFSZUI5TF95cjdvY293TnRrQ2xZdDF4Wk54T2NNZjF4c2IxYmRwMDdyNDNCZDhLcFI1czBSN0VUc2FYOUt0LXR4QnFWdXpWaFJoc1FXOXV4TQ?oc=5) <sub>BGR</sub>
- 📰 2026-10-10 [Workers erupt over DC plan to bring robotaxis to city streets: ‘This is bulls—’](https://news.google.com/rss/articles/CBMirAFBVV95cUxOV0lTd2hnYmFUYkdFYXB0NGhIdU1KUlZVT2hmQXBMeFkzTkhuNHFxN1RDalQ2d3hiMlZFYmJNR0lqUGdEWUtSZU1yeWREM2hLbWNaOExQeTJRMjJwZWVkWWVnTHdrOURNMi0tQlFIdDRnV1RVMXZ4d0N6WW5VTGNNSFpZcVJlRmlZbHlvM1FvaVloRWk3TDY1bDZNX1JQZC1qbmdta3Z4SmlUX2Na?oc=5) <sub>930 WFMD Free Talk</sub>

</details>

<details><summary><b>Motional</b> (52)</summary>

- 📰 2026-10-11 [Six Years into Euisun Chung's Tenure... Hyundai Motor Group Moves Beyond the 'Global Big Three' Toward Physical AI](https://news.google.com/rss/articles/CBMiZEFVX3lxTE1qSWl5SS12dk8yVXMwandrR090TkZkdzZDaFladGpmOGNZZDNrMGxBQV9zSkV5TXpVeXIzWGhKd0FVYUQ0ZFdsT1pEWGxZNDV1UC14N0FsZmxVd0ZFOUVkamhoMWg?oc=5) <sub>아시아경제</sub>
- 📰 2026-10-10 [Waymo's $5 Billion First-Ever Debt Raise Signals a Robotaxi Land Grab, Not a Science Project](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9BaGt6ckszSmpwTDVsOGUzQ29DXy0yc3BsVFdSTjNtZFZrR3dWYUd5TzcwSTYzUTE3MlVmd3B4UG1iSS1kRHpySXpFVlhRTWd3cjVCOUgwVW5FcWc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-10 [Waymo Goes to Wall Street｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTFA2Z3RvWEJLVEtPTDJWNVcyaGQweFBVUnZFb0RST0wxRWhCdUJudXJQeU9helBuODZrTlBDZlh4NF9zb3dyNjRxQ3BzTGpZLWJvQzNObmFlYjl1R010Z3hB?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-09 [Hyundai delays its in-house autonomous driving solution to 2029](https://news.google.com/rss/articles/CBMilAFBVV95cUxOM1BRRVUzZ21fMHFubEhHNHRGcFVDQTFwdkRMWnljalNhS193bHpKY0dLSUZjN2tXamRlZUZIZ24wdmh5cWE5bnI2MzF4Qm5lVXJlWFZqTXE2TkpFLUZJWExJQWY4RDFuemJJbmZWZ01DMmRoUG9yLUlIZHNnT3RVeHdYR3hMSkk4RlBfcjlHU0R6Mzhn0gGUAUFVX3lxTE4zUFFFVTNnbV8wcW5sSEc0dEZwVUNBMXB2RExaeWNqU2FLX3dsekpjR0tJRmM3a1dqZGVlRkhnbjB2aHlxYTlucjYzMXhCbmVVcmVYVmpNcTZOSkUtRklYTElBZjhEMW56YkluZlZnTUMyZGhQb3ItSUhkc2dPdFV4d1hHeExKSThGUF9yOUdTRHozOGc?oc=5) <sub>Motor Illustrated</sub>
- 📰 2026-10-09 [Pony.ai's Robotaxi Expansion Reaches Middle East and Europe; Goldman Sachs Maintains Buy Rating, Cuts Target Price to HK$202.4](https://news.google.com/rss/articles/CBMidkFVX3lxTE95VG5sWlNSQzI3MjVFNnBoYXVCTHVjNEpUdERqYWxIRVB1U1lGdFFYZ2FqWWdVT0JBZEtrVGxJODhVQ292U2Y4VlBJN09HUmxpZFlkN3dXUXhreFFWenZfcTljNWxVWXRhbC00VUpXNkctTHBXR2c?oc=5) <sub>BigGo Finance</sub>

</details>

<details><summary><b>comma.ai</b> (11)</summary>

- 📰 2026-10-07 [Researchers Find that AI Models Struggle With Even The Most Basic Driving Skills](https://news.google.com/rss/articles/CBMiuwFBVV95cUxNb2ZGRGxGZDNjLWU1OVBPNjUtUlJXR0hiVGV3WEJ1eUVnSWExMWVvRmJjX2NtQm9sX0plMTU3YzZwUm5ZTzVoSGttcXZmQ3BqbW40X2doNFMycUk4UWE3anlidy1vWHNYZndVZjZWLUYtbnlHeVBFRjJOaTF4SWxzbmotR0xsNkVIcEhfZ0M3LUs5R2FyV1lVdlRRU3JwakpQcXpBUzlEOEhsWlB3Q19EdXFhQjRvZDU5MHln?oc=5) <sub>Auto Spies</sub>
- 📰 2026-10-07 [OpenAI's GPT-6 Astra is the only AI model to finish a real-world driving test in a Toyota Corolla](https://news.google.com/rss/articles/CBMifEFVX3lxTE9iZmN2ZFp6blVBRnZUTkYtYTJ3b0hSb0xhQjZyQXh5MUN2T3ladUlEb1F1SWJzc3FtamZtazk4LTVUWVpNX0ZjbGZwMnpERk45TVVQWVA1RjBZVUxxTTAzTWpaV1JqUzIwM1I2Wk1tTzc3bDJpaWluc2JVam4?oc=5) <sub>Crypto Briefing</sub>
- 📰 2026-10-06 [AI Agents Tried to Drive a Corolla, Crashing on 8 of 11 Runs](https://news.google.com/rss/articles/CBMiuAFBVV95cUxONWxQTEZham1kc1J4S2lMNUh6OTN1QWhXbl92U21NUWZTZWhNUUdwcFVvUHYtVWJzSjl4TjlCeFhUY2ppMXd3WkkxaHJFRmFlNUN2NGFSSENnV2ZZYWRNZ3JIUjd0dzFlTS0wR3gtbmxXN3VHOUkxWWg2VVFpTVgzWGN2T3RPdEFJV0cyWjRPSVFyNWZTYjFyX0pzYjFEUWQwLUlfbGo1bm8xVUZXQmpyQ3pCNXV5ZE9x?oc=5) <sub>thetruthaboutcars.com</sub>
- 📰 2026-10-05 [Researchers Discover ChatGPT Can Drive a Car. Grok, on the Other Hand…](https://news.google.com/rss/articles/CBMikgFBVV95cUxNNnNwX0g5bHV4STJlMXNOcXRnYnBHWHNoelViM2pJSzFob3dvUVJIdFlDRDV4X09DSVloZmxCTk5NODd3b3RBR2JmWEJQRktXUTYyWDNveS15UEw0NnVfSFluMlJxZHlBb3NhYnRNdDJsZ01MbVNpOXY4OW9nQnBSYnFRQ1U2YVd3a3R2ZTY4VlJNdw?oc=5) <sub>The Drive</sub>
- 📰 2026-09-30 [A $999 Box Promises Hands-Free Driving. Its Own Code Says ‘THIS IS NOT A PRODUCT.’ Now NHTSA Is Investigating Crashes That Killed Three.](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPNFIyamduTmQxb1dKNlh5Z1hCYUhyemoyU2I2bjFUWjZQSDVFSDFWOGxlM1hnQms4Q1lpalg0bXlCTEZTdVJ3eGtNTjlLamY2eW9LX09IejF6SkJxSmZ2QjRkU1pUczlRY2g3cUZIN3hvSUc3a3pUWHVKVk40MlY3Wk5SX3dnOHBl?oc=5) <sub>Yahoo</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
