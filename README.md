# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-10-09 · 1,254 papers tracked · 37 curated.

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
- [End-to-End Driving & Planning](#end-to-end-driving--planning) (8)
- [3DGS / NeRF Reconstruction & Sensor Sim](#3dgs--nerf-reconstruction--sensor-sim) (3)
- [Perception: BEV, Occupancy, 3D Detection, Mapping](#perception-bev-occupancy-3d-detection-mapping) (8)
- [Datasets & Benchmarks](#datasets--benchmarks) (2)
- [Safety, Robustness & Evaluation](#safety-robustness--evaluation) (3)
- [Industry Tracker](#-industry-tracker)

## VLA / VLM for Driving

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Teaching Vision-Language-Action Models What to See and Where to Look](https://arxiv.org/abs/2607.01658)<br><sub>Yuguang Yang, Canyu Chen, Zhewen Tan et al.</sub> | ECCV 2026<br>2026-07<br>📑 1 | [⭐ 32](https://github.com/ShivaTeam/DriveTeach-VLA) | Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving |
| [DeepSight: Long-Horizon World Modeling via Latent States Prediction for End-to-End Autonomous Driving](https://arxiv.org/abs/2605.10564)<br><sub>Lingjun Zhang, Changjie Wu, Linzhe Shi et al.</sub> | ICML 2026<br>2026-05<br>📑 1 | [⭐ 31](https://github.com/hotdogcheesewhite/DeepSight) | End-to-end autonomous driving systems are increasingly integrating Vision-Language Model (VLM) architectures, incorporating text reasoning or visual reasoning to enhance the robustness and accuracy of driving decisions |
| [CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving](https://arxiv.org/abs/2607.04179)<br><sub>Zhaohong Liu, Hao Ye, Xianlin Zhang et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 1](https://github.com/MICLAB-BUPT/CritiqueDriveVLM) | End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving |
| [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)<br><sub>Nan Yang, Zhanwen Liu, Linfeng Zhang et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 4](https://github.com/Zizzzzzzz/MVPruner) | Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings |
| [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)<br><sub>Yuan Gao, Wenting Miao, Mattia Piccinini et al.</sub> | IROS<br>2026-07<br>📑 1 | [⭐ 27](https://github.com/TUM-AVS/Chat2scenic) | Validating autonomous driving systems requires diverse, regulation-compliant test scenarios |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 7 | [⭐ 490](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
| [Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air](https://arxiv.org/abs/2605.31066)<br><sub>Tianle Zeng, Yanci Wen, Xueang Yu et al.</sub> | arXiv<br>2026-05<br>📑 2 | [⭐ 1,112](https://github.com/louiszengCN/CarlaAir) | Recent aerial vision-language-action (VLA) models show promising single-UAV capabilities, such as tracking moving objects and navigating to language-specified landmarks |

## World Models & Generative Simulation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [HERMES++: Toward a Unified Driving World Model for 3D Scene Understanding and Generation](https://arxiv.org/abs/2604.28196)<br><sub>Xin Zhou, Dingkang Liang, Xiwu Chen et al.</sub> | ICCV 2025<br>2026-04<br>📑 4 | [⭐ 72](https://github.com/H-EmbodVis/HERMESV2) | Driving world models serve as a pivotal technology for autonomous driving by simulating environmental dynamics |
| [FrozenDrive: Zero-Shot Text-Guided Driving Scene Generation and Data Augmentation with Parameter-Free Frozen Diffusion Model](https://arxiv.org/abs/2606.20110)<br><sub>Yuhwan Jeong, Hyeonseong Kim, Daehyun We et al.</sub> | ECCV 2026<br>2026-06<br>📑 1 | [⭐ 10](https://github.com/daehyunwe/FrozenDrive) | Synthetic data for autonomous driving is surging, powered by diffusion models that promise scalable scene generation |
| [MESSENGER: Memory-Enhanced Sequential Scene Flow Estimation via Autoregressive Next-Frame Forecasting](https://arxiv.org/abs/2610.10759)<br><sub>Jiuming Liu, Jianing Li, Mengmeng Liu et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 0](https://github.com/liujiuming123/Messenger) | Scene flow can capture low-level 3D motion displacements in dynamic scenarios |
| [ASTAD: Asymmetric Style Transfer for Synthetic-to-Real Adaptation in Autonomous Driving](https://arxiv.org/abs/2606.29286)<br><sub>Dingyi Yao, Xinqi Zhang, Lihui Peng et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 1](https://github.com/Dingyi-Yao/ASTAD) | Synthetic data mitigates the data scarcity problem in autonomous driving perception |
| [Is Your Driving World Model an All-Around Player?](https://arxiv.org/abs/2605.10858)<br><sub>Lingdong Kong, Ao Liang, Tianyi Yan et al.</sub> | arXiv<br>2026-05<br>📑 5 | [⭐ 254](https://github.com/worldbench/WorldLens) | Today's driving world models can generate remarkably realistic dash-cam videos, yet no single model excels universally |
| [Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends](https://arxiv.org/abs/2606.01164)<br><sub>Jiuming Liu, Chaojun Ni, Mengmeng Liu et al.</sub> | arXiv<br>2026-06<br>📑 4 | [⭐ 239](https://github.com/liujiuming123/Awesome-Interactive-World-Model) | With rapid development of large language models and diffusion-based content generation, world modeling has attracted increasing research attention, benefiting various downstream domains such as game engines, embodied AI,… |

## End-to-End Driving & Planning

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](https://arxiv.org/abs/2609.26792)<br><sub>Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.</sub> | CoRL 2026<br>2026-09<br>📑 1 | [⭐ 11](https://github.com/VAIL-UCLA/DreamStream) | Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions |
| [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)<br><sub>Shen Zheng, Anurag Ghosh, Gaurav Parmar et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 30](https://github.com/ShenZheng2000/WarpI2I) | Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs) |
| [G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance](https://arxiv.org/abs/2606.26017)<br><sub>Hang Yu, Ye Jin, Alessandro Canevaro et al.</sub> | IROS 2026<br>2026-06<br>📑 4 | [⭐ 6](https://github.com/HangYuu/G2DP) | In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 15 | [⭐ 345](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
| [Latent-Centroid Steering: Single-Pass Classifier-Free Guidance for Command-Aligned Autonomous Driving](https://arxiv.org/abs/2608.00237)<br><sub>Meibo Hu, Jiamian Wang, Pichao Wang et al.</sub> | IROS 2026<br>2026-08<br>📑 1 | [⭐ 2](https://github.com/codingmlinprocess/LCS) | Vision-language models (VLMs) have recently emerged as a promising paradigm for end-to-end autonomous driving, enabling agents to map multimodal inputs and high-level navigation instructions directly to executable trajec… |
| [DVGT-2: Vision-Geometry-Action Model for Autonomous Driving at Scale](https://arxiv.org/abs/2604.00813)<br><sub>Sicheng Zuo, Zixun Xie, Wenzhao Zheng et al.</sub> | arXiv<br>2026-04<br>📑 11 | [⭐ 365](https://github.com/wzzheng/DVGT) | End-to-end autonomous driving has evolved from the conventional paradigm based on sparse perception into vision-language-action (VLA) models, which focus on learning language descriptions as an auxiliary task to facilita… |
| [STAGE: STyle-controllable Action GEneration for personalized autonomous driving](https://arxiv.org/abs/2607.29517)<br><sub>Zihao Liu, Xing Liu, Yizhai Zhang et al.</sub> | RA-L<br>2026-07 | [⭐ 6](https://github.com/CarlDegio/STAGE) | Driving style refers to the behavioral preferences that drivers maintain during driving, shaped by their diverse experiences, habits, and needs, and is typically reflected in varying levels of aggressiveness |
| [A Survey on End-to-End Autonomous Driving Training from the Perspectives of Data, Strategy, and Platform](https://arxiv.org/abs/2610.00926)<br><sub>Chengkai Xu, Yiming Cui, Jiaqi Liu et al.</sub> | arXiv<br>2026-10<br>📑 4 | [⭐ 104](https://github.com/Jiaaqiliu/Awesome-Training-Ecosystem-for-E2E-AD) | Autonomous driving is a cornerstone technology for the future of intelligent transportation, where end-to-end learning has emerged as a transformative paradigm that directly maps multimodal sensory inputs to driving acti… |

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
| [FreeOcc: Training-Free Embodied Open-Vocabulary Occupancy Prediction](https://arxiv.org/abs/2604.28115)<br><sub>Zeyu Jiang, Changqing Zhou, Xingxing Zuo et al.</sub> | RSS<br>2026-04<br>📑 6 | [⭐ 139](https://github.com/the-masses/FreeOcc) | Existing learning-based occupancy prediction methods rely on large-scale 3D annotations and generalize poorly across environments |
| [Revisiting Token Compression for Accelerating ViT-based Sparse Multi-View 3D Object Detectors](https://arxiv.org/abs/2604.14563)<br><sub>Mingqian Ji, Shanshan Zhang, Jian Yang</sub> | CVPR 2026<br>2026-04<br>📑 1 | [⭐ 9](https://github.com/Mingqj/SEPatch3D) | Vision Transformer (ViT)-based sparse multi-view 3D object detectors have achieved remarkable accuracy but still suffer from high inference latency due to heavy token processing |
| [Horizon3D: Sparse Radar-Camera Fusion for Long-Range 3D Perception in Autonomous Driving](https://arxiv.org/abs/2606.31096)<br><sub>Geonho Bang, Geunju Baek, Dongyoung Lee et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 23](https://github.com/geonhobang/Horizon3D) | Long-range 3D object detection is critical for safe autonomous driving at highway speeds, yet existing radar-camera fusion methods remain limited at extended ranges |
| [Explainability-Aware Frustum Attack: Exposing Structural Vulnerabilities in LiDAR-Based 3D Object Detectors](https://arxiv.org/abs/2606.29963)<br><sub>Chengzeng You, Binbin Xu, Soteris Demetriou</sub> | ECCV<br>2026-06 | [⭐ 2](https://github.com/SecMindLab/Saliency_LiDAR) | The structural vulnerabilities of point cloud-based 3D object detectors remain poorly understood |
| [PointLAM: Local Attentive Mamba for Efficient Point-based 3D Object Detection](https://arxiv.org/abs/2609.21780)<br><sub>Xuanming Shang, Weijia Zhang, Chao Ma</sub> | ECCV 2026<br>2026-09 | [⭐ 4](https://github.com/PointLAM/PointLAM) | 3D object detection from LiDAR point clouds faces a fundamental dilemma: voxel-based methods achieve efficiency at the cost of geometric quantization, while point-based methods preserve fidelity but suffer from prohibiti… |
| [Vernata: Self-Supervised Learning of LiDAR Point Representations](https://arxiv.org/abs/2608.06919)<br><sub>Oliver Lemke, Alexander Liniger, Abel Gawel et al.</sub> | IROS 2026<br>2026-08 | [⭐ 18](https://github.com/rai-opensource/vernata) | LiDAR serves as a primary sensing modality for robots operating in outdoor environments |
| [Towards Compact Autonomous Driving Perception with Balanced Learning and Multi-sensor Fusion](https://arxiv.org/abs/2606.02979)<br><sub>Oskar Natan, Jun Miura</sub> | arXiv<br>2026-06<br>📑 44 | [⭐ 9](https://github.com/oskarnatan/compact-perception) | We present a novel compact deep multi-task learning model to handle various autonomous driving perception tasks in one forward pass |

## Datasets & Benchmarks

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Towards All-Day Perception for Off-Road Driving: A Large-Scale Multispectral Dataset and Comprehensive Benchmark](https://arxiv.org/abs/2604.27499)<br><sub>Shuo Wang, Jilin Mei, Wenfei Guan et al.</sub> | RA-L 2026<br>2026-04 | [⭐ 6](https://github.com/wsnbws/IRON) | Off-road nighttime autonomous driving suffers from unreliable visible-light perception, making infrared modality crucial for accurate freespace detection |
| [123D: Unifying Multi-Modal Autonomous Driving Data at Scale](https://arxiv.org/abs/2605.08084)<br><sub>Daniel Dauner, Valentin Charraut, Bastian Berle et al.</sub> | arXiv<br>2026-05<br>📑 2 | [⭐ 400](https://github.com/kesai-labs/py123d) | The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics |

## Safety, Robustness & Evaluation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [CCFM: Collision-Constrained Flow Matching for Safety-Critical Scenario Generation](https://arxiv.org/abs/2607.04451)<br><sub>Ke Li, Kaidi Liang, Yuxin Ding et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 3](https://github.com/KELISBU/CCFM) | Evaluation of autonomous vehicle (AV) planners in safety-critical closed-loop simulation is essential for real-world deployment |
| [Lipschitz Optimization for Formal Verification of Homographies](https://arxiv.org/abs/2605.23203)<br><sub>Jean-Guillaume Durand, Panagiotis Kouvaros, Maxime Gariel et al.</sub> | CVPR 2026<br>2026-05 | [⭐ 2](https://github.com/jeangud/homography-verification) | The adoption of vision neural networks in regulated industries requires formal robustness guarantees, especially in safety-critical domains such as healthcare, autonomous vehicles, and aerospace |
| [CADET: A Modular Platform for Evaluating Distributed Cooperative Autonomy in Connected Autonomous Vehicles](https://arxiv.org/abs/2606.04072)<br><sub>Pragya Sharma, Brian Wang, Mani Srivastava</sub> | ICRA 2026<br>2026-06<br>📑 1 | [⭐ 0](https://github.com/nesl/cadet) | Deep learning models are increasingly central to autonomous vehicle (AV) pipelines, yet their integration has traditionally followed a monolithic design where perception, planning, and control execute on a single onboard… |

## 🏢 Industry Tracker

Latest 14 days of news, official blog posts and new open-source repos from tracked companies. Full daily feed in [`daily/`](daily/).

<details><summary><b>Waymo</b> (232)</summary>

- 📝 2026-10-08 [Waymo Closes $5 Billion Debt Financing to Accelerate Business Expansion](https://waymo.com/blog/2026/10/waymo-closes-5-billion-debt-financing) <sub>official blog</sub>
- 📝 2026-10-08 [Sober Drivers Still Face Nearly 4x Nighttime Risk: Why Road Safety Demands a Safe System Approach](https://waymo.com/blog/2026/10/sober-driving-benchmarks) <sub>official blog</sub>
- 📰 2026-10-08 [Waymo locks in $5B loan from Blackstone, PIMCO to fuel robotaxi expansion](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNcjlhRElvb3F6ZXgtX0hiYjNkdC1GdDlRQk52azA3NjZsQjdIV2VnM204cldKV0poVzliNWRhSWV6Ym9OR3JISjd3YXM4ZDlNWVkxUUdYTDZrNVY3S2FoUWF1LWlLZUUtcVY4RUwyR3Z2MXRwRzM3MzBfSno2eGpBZWVNcHpLVFg1bk9aNWlqYkNTYlFqRmFuMUxLcHFRZnlkajRwNlNyX3B1QQ?oc=5) <sub>TechCrunch</sub>
- 📰 2026-10-08 [Alphabet's Waymo secures $5 billion term loan to accelerate expansion](https://news.google.com/rss/articles/CBMirgFBVV95cUxOb0hkcWk3SGVuRHo2Rl92bWlManRvOXl3Zzl4T2FxOFNxclV0Vjl0cldtVC1lT3Q3Q1dHTmxaakFDTWdBZy04Tkw5SS1kSUI0MnBRNUtIZDg0SE1VRE5VdkNPYmhEN0JuTEpMcmdqMlFRcDBtSHNzSUVNU1ZVUnlOOFNHS19UZUVvdVZXZWtXWEcwbVF0Z1kySVVScnJXX2hmRXk5d2Q2X3V1Nm5Tb2c?oc=5) <sub>Reuters</sub>
- 📰 2026-10-08 [Waymo begins fully autonomous testing in Detroit, other northern cities](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE81V1RrbGY3Yk5aZVpQd2tnRmhFbTBqaFZWQzV1aG1ia24wYWlDREtzbkdlOEtfbHl0eFFCQmtxNEgyX3EtdVZpYUsxUTVHZ2ZjV3kyT2JNY1NDdG4ydHVpTElzYlF2NUk?oc=5) <sub>Chicago Tribune</sub>

</details>

<details><summary><b>Tesla</b> (354)</summary>

- 📰 2026-10-09 [760+ Unsupervised Tesla in Robotaxi Texas and Florida](https://news.google.com/rss/articles/CBMimwFBVV95cUxNSUlwZkRlck5feVBmSS1yRWprcTFqeEEyMVJUX1dxRHc0bHhaY0VReTFqVHExZThPQXBvMTQxdWFKRnhNZDVQMTY1ZmVTZzlkRkZRNmlRODRIMWxSUU56dmpzNXVPdG94Q1JLY2ROLXBKTm9sODcxYzgzMTVFZjNGaU53OElmdE9iV2l5OHpGaHJhN28yR3NueFRkdw?oc=5) <sub>NextBigFuture.com</sub>
- 📰 2026-10-09 [Key facts: Tesla, Inc. 486,532 Q3 deliveries; $25B+ 2026 capex; $43.5B cash](https://news.google.com/rss/articles/CBMiyAFBVV95cUxOZGpscHJmNjRmUDByVDBPejdfdzJmdjY0aFRxN3FCX2gzd2szbzB2cjN5eVJZU2xQMlMxaXp5MXIyLW1UX1lra0NyOXh0TmRWMFY0WFJGcy04WXJGYmZTcW1MMFRDOW0wRlhJVDZfcEdQTWVjQTFMV09wUUJ6NFBoSzhjdE1zZ1p3T3Bpa2I2Q1lOTnNXRmd2YmRuc2s0S1NKTjVnUm11b3JhUTZFQ0N6QUxUTnltOHEtTlYtRV82Zjk4N3UtcWs1Zw?oc=5) <sub>TradingView</sub>
- 📰 2026-10-09 [《硅谷101》｜特斯拉FSD十三年的冒险、争议与进化 本期《硅谷101》…](https://news.google.com/rss/articles/CBMigAFBVV95cUxPMWF6TU5vdnh0U3hEUGNBMS1lcjhjY3lBNUJkeWJSWVRyVEdfdC1iZWRhOUFQOGI2cXk0Z0NXN3VITU1EcE9MX196WFV5MUFrem9xS3E1RDhLbXY3OURjWTd1VHJEbGVsNkM4TE5yclBRNXRsUGdXZWtIUzdwdHFMZw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-08 [Key facts: Tesla price cut, record registrations; EU FSD delayed; Q3](https://news.google.com/rss/articles/CBMixAFBVV95cUxQQ2tJam9XbDRGaHkzdmplaHRuaGlUdnpNa1B1RmpHMUlTNDBfNlp6cTZUSVVwN3h6UjZLWk8yNjdlUEN0dnZvdTF1b25IS2dTbjBzQ3FJcXRsNHRLeEg3M2RNeU9qeno1OG9TSmJKbjBVdkl4eHFWMkJRcHdwSjJKWlloMVFYdWh5SHpCeU9MaXdmMk55UUswamlDRWh2RXpXVHpzUUtTajJCZ2IzU29kVkNmNHVTSUxZY2VQWlQ2OG9SQjUz?oc=5) <sub>TradingView</sub>
- 📰 2026-10-08 [特斯拉无人驾驶出租车竟被灰色小猫给难住了- Tesla 特斯拉](https://news.google.com/rss/articles/CBMiYEFVX3lxTE83emxtTGRXT2wzZVVpQ2xHa0VvUGdxb1plenZJeTFDNEVEUGI5ek1XRWQ3TnFsR1R0VWdRWFA0VVJ6ZTFnNTNQR2xkZUg3cGtNQVR2Q3dCLUhuRzhuRFI1Zw?oc=5) <sub>cnBeta.COM</sub>

</details>

<details><summary><b>NVIDIA</b> (220)</summary>

- 📰 2026-10-08 [Can You Invest in Wayve in 2026? Details & Alternatives](https://news.google.com/rss/articles/CBMigAFBVV95cUxQdW45U05hcG5zUnk5WDBsVW00dkswdUN3X2twNEFjSVctNGxENDNYNGdrRGFCMWNZbEZBVk00cGVyX09kVFNWSTBBemNHYzJFVHJqN2lQd2lTdzllcUVaUHBpNHVnNXJ6T1k4ZzRPdi1ETVpUTkY0OFg5UUM3Z3Nqbw?oc=5) <sub>The Motley Fool</sub>
- 📰 2026-10-08 [Nvidia and Micron Set to Dominate S&P 500 Earnings as AI Spending Boom Drives 29.5% Profit Surge](https://news.google.com/rss/articles/CBMidkFVX3lxTFBySnUyWHBJOThueVYyY0lTYmI1MHF1UDVmczRQdXFaMlFZNnVZc2lYeUlTVmhqejAyOXBiR01kZkZhWGNuTWpMNG5qeHlHcXlka2pjXzZ5QjA5d1FxakRfRDR6WDlFR09ZU1lXclFrMDhmeXNxMGc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-08 [5 Steps to Create SimReady Assets for Robotics with Frontier AI Models \| NVIDIA Technical Blog](https://news.google.com/rss/articles/CBMiqAFBVV95cUxQb29oVGtZV3BUeFkwcENKZHJ3UmtzaTAtdXFkU3FfWDFScVo5VnlJRkt3QU0xaVBKRVItcjVndjZaOFFKOWJtRWQ2N0k4cHdoYl9QX2xaY0JIaktfSEJyT2RsVXRVSDZ5SmFTaDZRYnBtbF9EaVJCS1ktVU9pQUs1Y0xaSUtGc3dNcFk0UXhEQkh4NV91OXZ1cEJBMTlLR01NVExxaDdFNXc?oc=5) <sub>NVIDIA Developer</sub>
- 📰 2026-10-08 [NVIDIA exec says one company has the edge on self-driving cars](https://news.google.com/rss/articles/CBMipAFBVV95cUxNenFyblFIV2otMlVNSUhlSmhfelB6R3JwMWtVUDF0bW1qeHAyZ2RPWXRkOGxvZUFxbDg1RXNyZHh3X0k1aFRLZ3J4V1oxTXN2bVhmMkxPQ0M3blFCUnp2S2o4TEhLNV9MbklURTVudm9lRjUwT3l3MGpRQmp0T1oyX0tYaTkwQm1ELTlfdWpjazJqb3NRc3F2TmVEcGJ5MjZoYWcwVA?oc=5) <sub>Detroit Free Press</sub>
- 📰 2026-10-08 [Nvidia Analysts See New Growth Drivers Ahead Of Earnings, From Blackwell Ultra To $20B Vera Opportunity](https://news.google.com/rss/articles/CBMi0AFBVV95cUxPV21OZ3R1a2Z0M09TcEV4cFBKbmpZdTlVX1JZTjJYM0l2ajhvUmU3aHJUbnpxcHh4cVNfTTc3bmpRVUZpM290R2tISVQ0Zy1vaGsyTFM3Ul9odXZUN2RIdmZ4U2Y2WXoyTU9SbEZlck9VSDVDNmd3WGg5am5PUWlaMmJBUGRjU1Z2WHhUcDQwQVpFTmN6M2kwRTJOMDBXYmRCLW9kM2JtRHgwWWpNaWpacWs0UkZFOE1JblNWOXlHSmtpSndwb1dBX2xONVBOMzBC?oc=5) <sub>Stocktwits</sub>

</details>

<details><summary><b>Wayve</b> (64)</summary>

- 📰 2026-10-08 [Can You Invest in Wayve in 2026? Details & Alternatives](https://news.google.com/rss/articles/CBMigAFBVV95cUxQdW45U05hcG5zUnk5WDBsVW00dkswdUN3X2twNEFjSVctNGxENDNYNGdrRGFCMWNZbEZBVk00cGVyX09kVFNWSTBBemNHYzJFVHJqN2lQd2lTdzllcUVaUHBpNHVnNXJ6T1k4ZzRPdi1ETVpUTkY0OFg5UUM3Z3Nqbw?oc=5) <sub>The Motley Fool</sub>
- 📰 2026-10-08 [Uber vs. Pony AI: Which Company Has the Edge in the Robotaxi Race?](https://news.google.com/rss/articles/CBMiuwFBVV95cUxOLUlfUFRqSTNGOFpHcW05Vl9hWlJtbWtObmRHTHZJVHZpRFlGM1lTanlyVGtxNTU3MlZzLVJ6ekYwdFFZYTdsaHFDQi1wUmJkdmhlcXh0eDFQeEYzMVU3eE1IUkJpZ2VDb1UxU1BYR1VSalF3M0ZIYXRiOWFTUjFvWm5Yb0ViQXJyNEZxTlVpckMtSnBVZzN6Y3UzT1Q1bXlPNzEzbzBTei1NSXloMHlSZldfYWtzaDZNb2VJ?oc=5) <sub>TradingView</sub>
- 📰 2026-10-08 [Uber to bring Pony AI’s robotaxis to London network alongside Wayve](https://news.google.com/rss/articles/CBMinwFBVV95cUxQc2R0RE56MF9VY19mS3dYTUcyM0QxbmEwRUJZdHlQQXJHYTQtX1RsYl9pR1B3TzlHdW1raUpHdmtFWTlVem9acmpDT0FwWTJFVFJ1R0tObWcwcFRHekN6RDBhQkwzNG9ObTZ0NmRBcm1oaXhUaG9vVDE5Uk1PUy1tYnAyMDBtZUVlSUtYWExMLTY0czhrSjRycXc0UTBVUkk?oc=5) <sub>Zag Daily</sub>
- 📰 2026-10-08 [Uber and China’s Pony.ai plan to launch robotaxis in London](https://news.google.com/rss/articles/CBMimAFBVV95cUxPRWphNWlOMkMwRUJyX1RPVGJOeTRaOHJBQi1YcUZtcXNnZUMtNDVDb3FBV3JkV01zWjZvN1czbUxlaDk0bVFoTV80cUg5UGE3OTRaLTZ3SkhBNjZkbXZPZnZxQ3Z2LWxrcG5IdUNSRVk5MGJUVlpQdGZQUjNfbmFlMFBuMllqcHF4MHBaZ0ZYZ2hSRGtEeDRfNA?oc=5) <sub>TechCrunch</sub>
- 📰 2026-10-08 [Uber, Pony.ai Plan Robotaxi Tests in London Within Weeks](https://news.google.com/rss/articles/CBMiWEFVX3lxTE9vdXN0YS1ueU43bGNlbDhXbFR1RWhlX1hhV2xNXzNITHJpUlNrSUdEY0VTUzFIczIwdTUzWWhTYmt0NFY3bnVIa3FYV0RaRlNWQUdIcHNWYlQ?oc=5) <sub>www.tokenpost.com</sub>

</details>

<details><summary><b>Momenta</b> (137)</summary>

- 📰 2026-10-09 [月入5000，拿下带Momenta智驾的艾尼氪 V](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBLbmUwclRXQi1SN2ZTNFdmMDlXcl91SmVsWjFibFJRQ3VUOHlUVUJSZkxYeUJUSVJ4dExzRWlfZ0FrNDNGQ1hOUnVuWkpPVWFIUW9ZeVVaQ0Rzdw?oc=5) <sub>爱咖号</sub>
- 📰 2026-10-09 [【视频】9.99万元起B级纯电！月入5000，拿下带Momenta智驾的艾尼氪V](https://news.google.com/rss/articles/CBMia0FVX3lxTE9qcXN5NWdnY1R2QUdvYjhJUmNVS1BBT2VGaEU0SGcycGVUbklYTDl6LXdYdDZpeFRLWnM3dTJYR0NfaEg0QzRWbXNlSkttZkcwelJVZDdiYVUyVEFfc1JoYXU5MUtJcjAyeU1v?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-08 [带激光雷达的豪华插混SUV哪款好？凯迪拉克全新XT5 PHEV与领克09、腾势N8等智驾车型横评+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE0zY0lua0JndHY4M3g4VjJWQWhQZjlnR3ZMS0hORjhGa20xS1V6dV9acDgyQlJhellmX0FxLWtfU1ZOX09acUpsQk1fN2tlRG0yVVBqcG1HOTZMRWtYWHc0?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-08 [Can You Invest in Wayve in 2026? Details & Alternatives](https://news.google.com/rss/articles/CBMigAFBVV95cUxQdW45U05hcG5zUnk5WDBsVW00dkswdUN3X2twNEFjSVctNGxENDNYNGdrRGFCMWNZbEZBVk00cGVyX09kVFNWSTBBemNHYzJFVHJqN2lQd2lTdzllcUVaUHBpNHVnNXJ6T1k4ZzRPdi1ETVpUTkY0OFg5UUM3Z3Nqbw?oc=5) <sub>The Motley Fool</sub>
- 📰 2026-10-08 [【视频】激光雷达+Momenta R7！东风日产新N7把车位到车位领航带到12万级](https://news.google.com/rss/articles/CBMiW0FVX3lxTE15bVM5ajRET2plaVZSekpQOVM0LURlX0RCdmczREZuSFFpT2tHc1YzRXQ5Y25scEJSZ2tuUHQ4OUhrZ3Vvc3kxN2RfSTFQemxjZ0wtT29Ga3M4ZFU?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>XPeng</b> (268)</summary>

- 📰 2026-10-09 [XPENG names robotaxi service XPENG YOYO, moves toward public trials](https://news.google.com/rss/articles/CBMioAFBVV95cUxOMmp1TmFmdmxnZHYyOFFRU3JqbnMyXzFpTkFINWpBN2lqdVlrVV9BWkpFM25EMzVDSWoxS3F5TDJrcW9jMmVHelNRVFJMV0VYVXF5bXdRWWlnNTNzWi0ydHlLUnEwOFZ2ZlBVWlRYRXMwT2NwdTc3NF9sVzhheVZPVGRLYkZjR1lVVkUwb2lFSi1kWEtOc1VHcFg1VmhDT2NZ?oc=5) <sub>TechNode</sub>
- 📰 2026-10-09 [XPeng's European Ambitions Take Center Stage in Paris as Robotaxi Unit Opens to Riders](https://news.google.com/rss/articles/CBMi2gFBVV95cUxQRDhRdW9ib2QtQWoyUl83YmxDdzV6dVhoU0ZWRGhCLTMzeWxqcjlGUkVtUlhYb3IyRHpLTUdGWDI5X3kyTllFN0Q0aW1IUHJBbmNGQjZCb1UwNlhMQV9UNTgzSkx0a3h2WkVIS1h6TUlRUnZKTmN3dS1FeTJTUk1Zb3N2dFAzTU83RzJfQ0RkOTRmMk55ek1iMS1FR09JYm9IVWZad2VzNjhjTGstOHo2OFVlX0VzWk56QUZLMkxEQ19QNE9pLWFMeDljZHMwbWxOQ0NuTWluQW5Edw?oc=5) <sub>AD HOC NEWS</sub>
- 📰 2026-10-09 [德系底盘加小鹏智驾 与众09 AI底盘预判悬挂](https://news.google.com/rss/articles/CBMigAFBVV95cUxPWWxQXzQwSXdPdWhYSExFOEp1Zng5UGpNeHVLNS1YTEFJaUplWDlnV3RUUC1XN0Z5Um9Oa3lmYmFWVklkZ3VoT1I4dnBPZ2FMMk5CTXI5dmpacEVZNXFhdjBpRmItWFJBU3JUenRMWDBhWkVnRDh0cGNmSnhUVWJmWA?oc=5) <sub>新浪网</sub>
- 📰 2026-10-09 [多花8万买四驱和智驾，小鹏GX对比奕境X9、理想L8谁更值](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1ZRWx6MFhiS250X0xjNndiV2JYZ3AycUZKZXJyRlZ5X2drUWRRaWNTSGE2ajVISi1IWFRFWFFiVXlNQTB6VmFia3l0UlJhc3NvLTJDaUNqd3lTbzQ?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-09 [【视频】小鹏P7+定价18.68万，不愧是AI 汽车时代的颠覆](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9scVNwWXdzNkhsMnFzVVptVXpBNHZjSmhXakdHZDhYcnRKbEg5ZTcyOVFHcUNMeUZXYnNFb2wwYzgwYzFQSHBlaXNaOURiUmZSUVNMajQ5TTZfX2s?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Li Auto</b> (164)</summary>

- 📰 2026-10-09 [Li Auto to launch 2026 Li i6 on October 28, deliveries to start in early November](https://news.google.com/rss/articles/CBMic0FVX3lxTE1DOHZfa0lZaE5rTDlHYWRMcHpybXJ1clozX3lnT1NicjUzNVJ5U0tDTTZEZmxkOGQ4UHc5RWNJaHdkb240SHEtWk9OM0ptejZMbjhJMnBSYnNSZEFvU1BjdWY5UGxxQmRDZFlacTZNV1dZeTA?oc=5) <sub>CnEVPost</sub>
- 📰 2026-10-09 [Li Auto’s 2026 i6 set for October 28 launch without CATL’s battery](https://news.google.com/rss/articles/CBMiowFBVV95cUxOdXV0Ykd3M2ZLYk5Kd3JrMmhnUEk2X2RDLXZwMExWNi1pVmNEZU50Y3RsZzN0MFZ4dXVOYzFRdGpTbXViUThYLW1RdzE0OVRONGIxSUJpd2xNbWhBSm1QM3EtNFVkSl9GTHZlSW1qYmREMXdJS2FuOHpMazBSNDJudGJwR0NEbHREMjVPbGlyS3dnYkFWMVhhRHNiU1ZaZllCczNr?oc=5) <sub>CarNewsChina.com</sub>
- 📰 2026-10-09 [这侧向AES救大命啊！加鸡腿@杨杰Safety 视频来源:五个打不刘 #理想汽车[超话]##主动安全# ​](https://news.google.com/rss/articles/CBMigAFBVV95cUxQemVzRjVFS3ZnU3Q5X2YxS0g3Z0diQk5JdHZGdFRsZVVlZFRvaXN2Y1JYWEkyZmE0OEd1eTJJMlJNOGRmTUZpazUzeklPSllGd1NIVGt6M1dyeklVZnhucG5PWE11RkFCOUdyc1dQdWxhLXpQMTd6NnYxQ2VuYTdaeg?oc=5) <sub>新浪网</sub>
- 📰 2026-10-09 [问界新M8标配L3架构华为智驾，锂电排产同环比双增印证需求释放](https://news.google.com/rss/articles/CBMijAFBVV95cUxQSWZyUTBra0RobXNmNW44S3pDa3o1MzE2alotM1dOUm9fMHlIdkl4bmdvV2kzejhKYjNXRS1mTXhyTjZTam1uWHJwd3JSREFmQlpUY3dybk9RQkowa3dKMFBuZ0ZrRWtUUDFneGdfeU04YUFtUTdzWkNEaG5NVWphc3Y5V3pHUS1fRHRFaA?oc=5) <sub>搜狐网</sub>
- 📰 2026-10-09 [国投证券国际：理想汽车-W维持“买入”评级 目标价70.20港元](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQeURDcXVrem56dk9VNmVxS0xadWhPbzd6RjdNT21jYjdab3REcnhFZmVPSlVBWEdXVlFuSVJmd2lyV2lNY25mOFlWeXVLX0tta2hDNFBCQWJHNWFBS0lmeFdpdy1RR3JYUUlYTmlXYjVQRUVBdFpPUDJ5dHVoX29rMG95ZEdlNUlHM2dz?oc=5) <sub>新浪财经</sub>

</details>

<details><summary><b>NIO</b> (157)</summary>

- 📰 2026-10-09 [蔚来9月智驾报告出炉 总里程超2.5亿公里 达1月4.3倍](https://news.google.com/rss/articles/CBMiW0FVX3lxTE80RjUwdVJyZ2RRSTFxeXBkYUdLTWxDM2Vfb29rMXpOOHJUanZlbTI0QWN4alEtcW4zTHlCOTk0NUxYVXdNaW5uUVhkc1dzd1k4SHBrc0llT3R6R3M?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-08 [Nio Onvo reaches 200,000 deliveries about 2 years after first handover](https://news.google.com/rss/articles/CBMicEFVX3lxTE1mX1FxdzZsREctTE92SFJGcWhwd2dib0tXSk9pTm84Q1dOT0lienMxYzY4M3pNMEJseThOYk8wUWhEVEZxTE14eXpwV3NhZU5JR1lGU0JaWDlkclpKbmI2c2FER0pvSE92bk5YRklkTWE?oc=5) <sub>CnEVPost</sub>
- 📰 2026-10-08 [从ES6到ES8，体验升级不是一点点](https://news.google.com/rss/articles/CBMigAFBVV95cUxNTlUwbEctMm5NdXNhZkk0OU1Ob1l6eThuY3NTb3hGd0U1UFFjVk5GVkpRSHFHQ2dSVm5pM1lNcjV2UkIxak5aUFY0dGs2bzUyYldyaVNfQklIT0tzTWxXOC0ySGZwX3JOZGU5ZjJMelNkbEpTYy1qNTgzYVNGM1pwNw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-08 [【视频】《帮看车》3年3万公里长测：二代蔚来ES6，让我又爱又嫌？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE4zYkRFbnA5X1JzQnlOWDNiMTkzYzhneW9MaFRmdnRscVlxTjlaNWdGU0NIUW5Dbk81VVFZLUpLVDJ3ZnpCWlNrNi1FMWcyRzlLZ3ljUzNfRTRRV2s?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-08 [【视频】蔚来ES8 2026款五座行政签名版租电版](https://news.google.com/rss/articles/CBMiW0FVX3lxTE8xcm1MT1NYOW9TSkhBZkNEdzRjRmpXN1J2bUk2VnNIQ2dYb1o5RFVXOXJkTGtyNUhDdEQ3bmVQWl9ja3NWVjlDSUF4a211LUx1Vk5lZFpEQTZ2WVk?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Huawei</b> (419)</summary>

- 📰 2026-10-09 [华为乾崑智驾国庆主动避险 5.8 万次，辅助驾驶的真实价值在哪](https://news.google.com/rss/articles/CBMif0FVX3lxTE12X204QlZlN3p0MEUwZ3oxa3NIaXl5bG5IeGY2RDBvUzNnWk5IVEhxTkgtNVNNUFhaanUyRnhGdVpXa2JVOUpDSU1ib1ZUQkdaS0JUbnh0MG5sZ1Nrcl9sc1l3ZEpnN01jSHNCN20yejFGcnFNMHhqYl9tV2FYREk?oc=5) <sub>新浪网</sub>
- 📰 2026-10-09 [华为乾崑智驾国庆假期报告：超90%的人都在用 主动避免碰撞5.8万次](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBKM2J3SUZETEhfMi1WTU8zWGFjTzA3MUgtUzJVbVB4czdoYXpnbzA0UE9hLXRQYjhfQVlGaDFiY051b3ZkVWdQdjZaWjhpd2VDTlhLNWFacjM?oc=5) <sub>驱动之家</sub>
- 📰 2026-10-09 [华为乾崑智驾解答三大场景实战：CAS 5.0可事前防范](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPMFVUQTNoWGluRnlUMmF2WVFDR3A3dExjQ1ZLZm5vVmQyQUNtT0oweEJXM3EzMk9DY2pvOFpUYWs0MFE1UnVKN2xxOTN1R210bk1EUXJUS2ZuemdNZmtKX1NYdkV0Uk9jbTFub2FaLXpJbDFoWjZmMWNfYkc2THIza3lOUEhCc2pO?oc=5) <sub>搜狐网</sub>
- 📰 2026-10-09 [华为乾崑智驾国庆出行报告：辅助驾驶总里程5.53亿公里 主动避免碰撞5.8万次](https://news.google.com/rss/articles/CBMiTEFVX3lxTE9TNXFWN1NYckI0YVFIMlpBOXZjbno2VGNNbTJ0b3JycVVjdEt4ZGFHMGd6VWFaN3pQcWo1RlBKOTI1OHhzeUFFMENNTWI?oc=5) <sub>凤凰网科技</sub>
- 📰 2026-10-09 [华为乾崑公布2026国庆假期用户出行报告 辅助驾驶累计里程达5.53亿公里](https://news.google.com/rss/articles/CBMiW0FVX3lxTE8wMnhtY3diY2Y2VUN1eHdFVEwxVXZWTDgxNmlyMFlRLXFnLW1BMjlRc0wxdkRXNlRod01jWVVMTDdMRVNyZHJrdktfd0tlczNSVFhVd2xSeVI0bFU?oc=5) <sub>网通社</sub>

</details>

<details><summary><b>Baidu Apollo</b> (53)</summary>

- 📰 2026-10-08 [Waymo locks in $5B loan from Blackstone, PIMCO to fuel robotaxi expansion](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNcjlhRElvb3F6ZXgtX0hiYjNkdC1GdDlRQk52azA3NjZsQjdIV2VnM204cldKV0poVzliNWRhSWV6Ym9OR3JISjd3YXM4ZDlNWVkxUUdYTDZrNVY3S2FoUWF1LWlLZUUtcVY4RUwyR3Z2MXRwRzM3MzBfSno2eGpBZWVNcHpLVFg1bk9aNWlqYkNTYlFqRmFuMUxLcHFRZnlkajRwNlNyX3B1QQ?oc=5) <sub>TechCrunch</sub>
- 📰 2026-10-08 [Pony.ai Adds London to Uber Robotaxi Push in Europe](https://news.google.com/rss/articles/CBMijwFBVV95cUxNNjNTOU13UXpsdVYtN2ZEaEJVeDFKaHJyaE1mYWZ4RGFQQjBNckg4OHNRTl9nNmp3TnJtOEhTU0lIY3RNZ3VCSy1ncEt3dkF6d0lxSTMyUHQ1dk83c09yWXRjbHZ2VnV4ZlBXWjE5d05raVdwQnpKREdxVkNFNFMwYlZ1N1pHaU9GZ2MwaC1xZw?oc=5) <sub>Electric Vehicles</sub>
- 📰 2026-10-08 [Uber and Pony.ai to test robotaxi service in Lo...](https://news.google.com/rss/articles/CBMikgFBVV95cUxOaDdlY2Q1cHluVUktVTFfa1pyb1ZhXzhDMnFtZkVrLUl1d2dyQXNSQUFlaGlHSjBlWURGelMtSUdnWlVPMkZ1YjVVT0QxQ3U0elFYc1lsTVN5VWZlcVA3VGxkbG9hTVYwbkVGTWQ3OFAtOUpWcktEVlZJLWlEaGpjS0Z5bEJWeWNVR2IySWJZZ29rZw?oc=5) <sub>Pluang</sub>
- 📰 2026-10-08 [Uber and Pony.ai plan robotaxi tests in London within weeks](https://news.google.com/rss/articles/CBMib0FVX3lxTE9rUTJXVUdwckFQSEFnVFZnN0lXOWlFU2JHYnVUUDVUZy1rZkkzcDJVVG9LZU9GZVllZWtLUnNmWEh5Z18tR0hKVnNTYy1DOWN6SDI1NWczd1E2RUlFZy1mN2JUWDRpWGNHZkxVTHJxVQ?oc=5) <sub>Crypto Briefing</sub>
- 📰 2026-10-07 [Robotaxi market accelerates towards $159bn](https://news.google.com/rss/articles/CBMilAFBVV95cUxQeV9GbVdCVWVLUTRIM092WDFUWml4cEtRei15ek81c3l0c3JwdlJlQlpoWDlNQl9qdkZoOWd5UXpFS0VRUGxVVWhpeEEyOHB4WVBNaWNqQUVkWHRkVGpZUUFaZ3ZkamE3c0xfMmUxSENMR3VhbWY4TW5pR0tGbjVjbGluVVo4b2U5SzdFeU9QS3IySUdR?oc=5) <sub>ITWeb</sub>

</details>

<details><summary><b>Pony.ai</b> (139)</summary>

- 📰 2026-10-09 [Pony.ai's Robotaxi Expansion Reaches Middle East and Europe; Goldman Sachs Maintains Buy Rating, Cuts Target Price to HK$202.4](https://news.google.com/rss/articles/CBMidkFVX3lxTE95VG5sWlNSQzI3MjVFNnBoYXVCTHVjNEpUdERqYWxIRVB1U1lGdFFYZ2FqWWdVT0JBZEtrVGxJODhVQ292U2Y4VlBJN09HUmxpZFlkN3dXUXhreFFWenZfcTljNWxVWXRhbC00VUpXNkctTHBXR2c?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-09 [Uber, China’s Pony.ai to test robotaxis in London](https://news.google.com/rss/articles/CBMigwFBVV95cUxQZmFXTnIxaVZfNFlYQjd0Q3JMOE44MmFQS1dtdTVRNU9rVzJ5cm02Uzc5NUlCUzU2S0t4TzVhYXY4LTE1blUwLU5rX1hDSkxRTjRZeFNIVkxnbG90NXBfSE15NThheGpYWmljN2k0Q0lWT0ZuSEk1bGluWGpiQWFXNEV1QQ?oc=5) <sub>Tech in Asia</sub>
- 📰 2026-10-09 [Pony.ai Teams Up with Uber to Launch Robotaxi Testing in London Within Weeks](https://news.google.com/rss/articles/CBMidkFVX3lxTE00UDJpV3h3OTFaNG9tY3RZYlNwdEI0ZFRNUlh6SHVGckpNWWVfVmRnTEdiVzJGU3cweXE4WmV6dEdBSDBDUTNfeWdhU2FHU1ktbXI0aVBzOTFPNktmMnlYcDJkVl84V0tnRW9SWjY2SXozSkVkWHc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-09 [华尔街知名投资人“木头姐”连续三天增持小马智行超32万股](https://news.google.com/rss/articles/CBMihwFBVV95cUxPRk02OE9VclIyUDl1QjVmZDJFYWpEaUxYR3JUSE1ZSnJGTDh2RGYxMWZ2bXR5V281WTd4RjJYRzV0WEZmb1BSLWZnZjE1NTRyTG9Qdlk1U0JFQUxhbWR5Qjh4eU5QTWRZWUxSTm9zZ3Zub1VJNjlMSzZaa2xIVmdvV3J0cmU2Y0U?oc=5) <sub>新浪财经</sub>
- 📰 2026-10-09 [小马智行与Uber将第七代Robotaxi引入伦敦 数周内启动测试](https://news.google.com/rss/articles/CBMikgVBVV95cUxOOV9yd1hjWExxMC04bFVVMDVUdXljQjNoNHBnNFRqWldQZUhEMEItSFdhNWF0X3JfS0NOQU5MQmVXejBHb05xMjB0SG9ndnlwS09Gb0paNVBDeks0eGhiMzJ4cnZReWk2Y2EwTDNKal9Hc3B6V21GOVpOQ1M3bEJTejZ0RWk5UUJqWEZXSFYzZmhHdE9TemdZT1QyZVRUcDhSa21lWTBIcDl5Rmx6ZnZTUnRiYTN5SE1CMDBzT0U0MFQ1bUMxNnlJbnFSWjh4aDhHMWFXU0ItOFl6ck1LVkg4WWRCMTZwWmdiV0RaYnBPRlVMbEEzVUV2Q3A5SDlNRU1BRnoteWtUTDRxTmJ3X0s1S1loYzZmei14VmNRamFBVUxMbmQ4T1BpSUtxR2x6TXFVenJZYm9IczJkVkdpUWhVN1h4bW9CUGRtZlRZV0RqbUlvYnJrTWlHSUlpZ19aNmNmZ0xBMXVyZjcyUDlrenc5OHN1ZzYxa0x5STFISHZMSkR1RHJudGVyNWo3NFNBYXpUSTdtdF9qRW5CVDBybnJXYVFQMzI5eGQ3UWhUejRtRDBuejd5Qk1LcktTY01wcU9xVWdTS0Y3WFV6MkJfZFZGdDI0ZUVETWVvMy1MYlBvNnRaY2JnR3pVa1J6bFc2U1RkZTNHUXVBczF5SWRucW1SQ3A1NzNleVdDSWt4RnI0azZma2dHMFpsRWQ4endIZUppQU92Z05sZG02TDVTa1F1ZlJYR3Y4Y2VIeUJEUUl3WEo5UWdqTS1aUU5MOHdHS2YxTmI5OGUySURpd0ZDTXE0N2w4elR2R0hMcDFHY1E5MUJfdGpSZVhwaXo2N1pLYVh1TTNicm5wUElFQjZsRk9uUVl3?oc=5) <sub>finance.sina.com.cn</sub>

</details>

<details><summary><b>WeRide</b> (130)</summary>

- 📰 2026-10-09 [The Rising Tailwind of the Great AI-Driven Mobility Era: Accelerating the Future of Smart Transportation](https://news.google.com/rss/articles/CBMiU0FVX3lxTE9ZOTFudkl3UGx1ZWYzenR1cDZNXzdOM1dIRFV0RV9GQjNuQ0FwbFlYM3dfV1lUNTdRaXA5bnFKVUJyYzhKMjg1T3lOV3FvY09MS01F?oc=5) <sub>36 Kr</sub>
- 📰 2026-10-09 [专业做10万级续航不缩水智驾纯电SUV推荐](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9fMV96TUZnV2RSODRiVkhrd3llX1lVQXgyV0RubFRFeHdWMWd2RVdNZXIzMWI2U1REZ0ZkWjE1eXZIMFVOZnkzZmF5Y1E0RzVHdFRxSFMtMlp4QWc?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-09 [美股半导体股全线下跌，英伟达市值一夜蒸发超万亿元，加密货币19万人爆仓](https://news.google.com/rss/articles/CBMiYEFVX3lxTE5NdXRFN3lHV0lROXVQdVZ0cDBQbVVGaC1UT05lNWpicVVQQjdINTZ1N0Uwa1d1bzBiRWFBQTltS3lXUmJDVUlTMHE5QVIyV1ZOTUMzTDV6ak9TUGpyNEpuNA?oc=5) <sub>新黄河</sub>
- 📰 2026-10-09 [10月9日早餐 \| 台积电业绩超预期；美股科技股走弱](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQZXZERWdxeDlnVXk2YzJFNmpObFJ3VFlCOUFKcVFrUlhkN1dnTjFNaEh6UWhOWTdoV0RpUjgwdzR3NDkwaTRsNWVLcW16d3A3UG82bERnWnZHN0o5dW9DbURfQ25NT1VpdTFFb3Z4WVplUGpMU2xOZVdwMTFhQkdrWmZlcVpWVXlKWThZ?oc=5) <sub>搜狐网</sub>
- 📰 2026-10-08 [[Shockwave] Singapore, Global Autonomous Driving Gateway and "Technology Test Bed"](https://news.google.com/rss/articles/CBMiZEFVX3lxTE5wTnQzckEweFYwbDQ1aXRpOU8wOTFpYmxCTmZNLTJRWEhWTWlvQjZMVGZHUWxjWlRHdzhQWkdaeUN0a3VHcTVNNVdUVUFMWjN0Q0VUVWNYMGlqQkhQcWczdUx2bFg?oc=5) <sub>아시아경제</sub>

</details>

<details><summary><b>Horizon Robotics</b> (203)</summary>

- 💻 2026-09-29 [HorizonRobotics/Ego4WAM](https://github.com/HorizonRobotics/Ego4WAM) <sub>GitHub</sub>
- 📰 2026-10-09 [日本车企开始拥抱中国供应链，铃木e-Sky将采用比亚迪电池和地平线智驾芯片_公司新闻_财经](https://news.google.com/rss/articles/CBMiYEFVX3lxTFBvQnRlNE84WTE5TElqSkxVenNqY1RkVjc1dXVILWtwUHdRdERVT0tqcTBGM2l5Q3hlbHN0T0x5NGFQSnphM2VSZG5jMW9ZaDBzdnl6bE1RMnhBRkN0cGoxZw?oc=5) <sub>证券之星</sub>
- 📰 2026-10-09 [【视频】什么路都能倒，HSD2.1版本来咯，V27车主节后回来就能拿到推送！](https://news.google.com/rss/articles/CBMiW0FVX3lxTE4wRUV0bGpYcDg0ckl0Uno2WkVCZXJ1MHRxamZnUjNVWXhZNWoydy04cEgwTTMyRDhMa1JyaGN5eVkxc3hGUWVlMmMwYlBCUW80czBlWVNzOEo4bXc?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-09 [预售价8.08万起！捷达首款绿牌车本月上市](https://news.google.com/rss/articles/CBMia0FVX3lxTE5JTDd2OGgzUFROWG5CbmFTTTFwQnc0V2FkOXZKVENvSGFocHgtSUkzZHZwTHFzVDFmRmpRQmNrMWhJNXJqalBKaEFZdEI3aGFFeExRSmpIVTNiU2lnay1DLTgtYXdJOG90TU5J?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-09 [从城市NOA到记忆泊车，大众ID.AURA T6、与众07、奥迪E7X德系纯电SUV智驾横评](https://news.google.com/rss/articles/CBMickFVX3lxTE53Y1FFLUdTazdsSHBhTE9jNy1mNmE1TUU5eGhtckt5N2ExODZHTk9xS1gxeVR0cVl1TDZqcGdBX0lMbkU4NFpoMGFXZGdCSmtDeEJTZkdYcGJhdW1jeXpCblpYM1R5UG15Y0djanRKSDd1dw?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (29)</summary>

- 📰 2026-10-08 [城市NOA座次重排：第二换人，头部三强只差1.7%](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNd1ZkX3lwNUE5bUEtTGR4a1JiSHBSbXM1aDJxUmc4TEtlVGRJUFZKempPX1dtYVZoVkVRY1pZNWRlZ09GMzBBODRlQ0FMZjQtR0Z4R2g3NC1pUkhfeG92a3hzaGtuWDFlYk1ZaUJSWjZzVFh4R014cTFTZ1p4bW54WldObE9oTmEy?oc=5) <sub>搜狐网</sub>
- 📰 2026-10-08 [元戎8个月从第八杀到第二，城市NOA打响“华元魔”头部肉搏战](https://news.google.com/rss/articles/CBMibEFVX3lxTFAwbUU2LVd1bkVoVUZVcUdrczBEUmNwQzVnaDFXX0hQU3U4eVpScElhMC1ydHVPRVhuUHI5OVNYZXVjOC0xV3VkQUQ4Q2ZyNURuNUdWaTAwMWV1SkFUUUlxZXR5SjI5cFJSdzJrbA?oc=5) <sub>中华网</sub>
- 📰 2026-10-07 [与问界M7同一工厂制造赛豆科技首车AIVA ME7测试车曝光_热点推荐](https://news.google.com/rss/articles/CBMiYEFVX3lxTE9fYVd2TTUyZWxoZC1ZZGNWczlwNXhUclo0OENVVkhhaFpxRTRFQlhNeFZBZXNRQUQ2MnVEOTB1TVAtMEZRTDVTQk5TcWw1QkZSSlRieUpkaXdpMl9xS0wzaA?oc=5) <sub>证券之星</sub>
- 📰 2026-10-07 [800V平台+700续航，三月亮相AIVA算速成车吗？](https://news.google.com/rss/articles/CBMiY0FVX3lxTE5JUnM5TE4xcUtpNjlSOFZJVW41bVpNRmZZZk9UQjhKWkV0SUNIcnBmVERJbEpzZFYwVkxwVXVvRDVnNmtOb2JBOFhKTVd2eVlpb2V2Ty1YQkJZTElKcURlZWFtZw?oc=5) <sub>www.bitauto.com</sub>
- 📰 2026-10-06 [【视频】特斯拉Model Y L 2025款长续航全轮驱动版](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9lN2x2MGx5NWdINEEwbHFXdUc0amd4czh1SllPek4yZG9XdjZPemxpSUp1OXQ0V1hOTjBRUW9yTE9HeWN1X0VPclNKdzVzMmh0d3RlVjF6N3hWVWM?oc=5) <sub>车家号</sub>

</details>

<details><summary><b>Mobileye</b> (20)</summary>

- 📰 2026-10-07 [Uber invests in robotaxi provider Verne](https://news.google.com/rss/articles/CBMigwFBVV95cUxQQkxEa25xSjBNT0ZJMzZINk54a2txS3k0S0pvTU4wZEJ5eVhHY0FNRWlyaVdIcVhYdmlPQl9HVUsyUnlkcW1UVzRVc180dHNCT1hXV3ZUcms3Mzg5aUoyZENTUWU3VHJtRlFuQmp0dWpQRDlmU2xlSDQ1MnlEZW11YmFGWQ?oc=5) <sub>electrive.com</sub>
- 📰 2026-10-07 [MOIA America Launches First Autonomous ID. Buzz Rides](https://news.google.com/rss/articles/CBMixAFBVV95cUxQY2FmM1hNRDEzV0c3c2NSVklIUDBPU1VrbmRmNnRLV3lNRzRITUVHUldKcVNYajNSYXJkdTJmbzRGeWt3V3ZrcXlmanBfR2t5cjRKZlU3b2JHbUg3VUx0ejdIS2ZUT25DRm5KTGtzSm1OaEhhQ2Zsb2Zhb0tHMDlnaWhnOGJHLXBvYk1GYkNYVFJRb2M2R3BmamRnN3RMZlJ2a3JlSGc3VnNmcXBtVDdub0s2VjhXSDhKVjFDR1pIQjYwLUpI?oc=5) <sub>Fuel Cells Works</sub>
- 📰 2026-10-07 [Uber takes a stake in Croatian robotaxi startup Verne](https://news.google.com/rss/articles/CBMikAFBVV95cUxOMkFfTDhoaldrejJpdUNUd1JvRXN1MlZwYVZQRjdPQ19FM2oyWjgxTndscUdGWFVZaG5nSWVKNWQ1dVYtNzFNZ2t0VnFwaS1mOFpneG41RW51M19leE9XSUN5WjhGbjF0ZkUtRVI4RDBiSUxtX2ZCTDBUekNRN3p1ZXZzUFU5aXJ0cjk5bHA3aUU?oc=5) <sub>Dealroom</sub>
- 📰 2026-10-05 [Moia’s autonomous shuttles start first passenger tests](https://news.google.com/rss/articles/CBMilgFBVV95cUxPaXBLWlk2ckZabm9UeXdOV1lCZTRjaDBkVmk4bDNVRWVMZkxKUEVTOVBqZERzWGlySkROdEs0bkE3SURjaG44c1Y4M3lsM0NmSG95X0diNlY4cGJoMUp1UUMxVnFkQ2Y0UTR2UDdtdTFzczBDSHpId3ZmWDltWlY3Ulg1bHBYMzJweHhDOWkzd3lyVWwxSGc?oc=5) <sub>electrive.com</sub>
- 📰 2026-10-03 [We Found Atoms, Rode Wayve and Watched Uber’s Autonomy Clock Speed Up｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1QZjNLZlpHR2ZtcHFaUDF5bEE3ZktHQlNoN0E1amxaVEg0eUdQbElIVlVVZk1JdTlqZG1kbGZYVTBvZDdKRDRKVWlqa2dRNDF3aTN4dEpmdTdxX0dTVnlj?oc=5) <sub>finance.biggo.com</sub>

</details>

<details><summary><b>Aurora</b> (55)</summary>

- 📰 2026-10-08 [Bollywood actor Nana Patekar dies at 75](https://news.google.com/rss/articles/CBMimwFBVV95cUxPVzhsbTRiV1k4RzB1X01kY0IzUFZPS3ZySVFLeGVTZ1pOOXB5VzlpUjZ4a1hMUmtHckJtMGN4THpXUWUtVzVKLUl4eDBtUVlvR1M1WHdJOG1TQkpjTzFXdFQwTV9yUEpOSlFrTnRJclJVVXg2bkpKMEZVV3YxLS0xOVBncEN2LVFpR2w2MGFJSEtqb3Y2R2lwTlNRZw?oc=5) <sub>Reuters</sub>
- 📰 2026-10-08 [Trump awarding former baseball star Clemens the Presidential Medal of Freedom](https://news.google.com/rss/articles/CBMinwFBVV95cUxNdURUbzFPeVNUc2poVm0taDh3eE5sRlRyS0x0eVB5V0lDdE05d1RnS2s0dDhjTW0zUkRqd2toZ1lqMlVLV2VhbUZvSDRsbWt2RlZ6cGdVY2tmQnQwcVdyNGJnZGVZcXV3TFJfZ2hBNnNCWnkyajhtWGlSOWxZRzNFLTJPUWl5VU16Ym01RHM1emprMFhLWW5DcFUzV09YNjA?oc=5) <sub>SRN News</sub>
- 📰 2026-10-08 [US grants Aurora exemption for self-driving trucks safety feature](https://news.google.com/rss/articles/CBMiqgFBVV95cUxONnE4aU1ld3FwRG93N0JmVUhpT1AzcWx0cDkwWXRzbG81VmNGTE9GTHh1ZHVsajZmTDZGUXJockJMLXV5ZFN4emtGZE8yTFU3T2UzU2VkdWVXZGgyX2ZETmdTamhZa1pZbmVjNk9jUU9YRmNTelpfZVBoNDY4Y0xqM3FBSTFMUTgzMWFlaVVVaW5lWHVWN1J6bXRUeEd0eU5HM0o1T1BvcnRTUQ?oc=5) <sub>Reuters</sub>
- 📰 2026-10-08 [US NHC says Isaias has become a hurricane](https://news.google.com/rss/articles/CBMinAFBVV95cUxPcWFsYXRiMjJHNGJ5OGdEbHhfU2tZUlNEaWltRzZHbWlCcjk1OXlfUUlGV3h5Zjl4dlcxVG5KcG5PRDE0bVMwSVZaVHA1anFPSDVVUGJGN0ZnYUZVMzFyRl84SHFzMFFBQ1dicnhjQ3NkM1d0QXIyUWRmNWRHb1FCbENSc0YtdmIzbTRidktIM2JFUzY0UlY5dVFxVDc?oc=5) <sub>Reuters</sub>
- 📰 2026-10-08 [Self-Driving Big Rig Operator Aurora Wins Regulatory Exemption](https://news.google.com/rss/articles/CBMirwFBVV95cUxOYTNRU1hydE9ESWxIQUZLeU9FRDNZRThNaFAwb2JnUFFmTTJiSjRGb0FiSjFFNFhWQnpHUWhfM0pCbUp0WkJWNjJvdnFVR25rbjNiQVlTTTctdmJ1ME5oZzBQcndFdWZobng0cV9fZGxlWm1RVWRXdjJjV19MWWtSRkU2U0JCRUdHXzBXLVg5S3NOckZxODNLUGRLaUp5c1dDcUQzTUlORFFxZEh3T293?oc=5) <sub>Bloomberg Government News</sub>

</details>

<details><summary><b>Zoox</b> (95)</summary>

- 📰 2026-10-09 [Zoox Investors, Directors Clash Over Amazon Deal Class](https://news.google.com/rss/articles/CBMiVkFVX3lxTE80b1JUV1VZVHdxOC1wN184c1VlNXFvMXRXM2FKb1JucVNUZ1dldnR6UVRvVU04bVhlTzN1NGxSazRXQ3BQZnFuQ25icTdTMHpyOUJyS1NR0gFWQVVfeXFMTzRvUlRXVVlUd3E4LXA3XzhzVWU1cW8xdFczYUpvUm5xU1RnV2V2dHpRVG9VTThtWGVPM3U0bFJrNFdDcFBmcW5DbmJxN1MwenI5QnJLU1E?oc=5) <sub>Law360</sub>
- 📰 2026-10-08 [Zoox T-Mobile Arena Drop Off Field Report｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBBZjBWUjA3Njg0dGY4SU91bV9jMlk4NkU0bXJib3lwY0NtSENVclZjVU1jS1NVWlFvNk5yTlQ3Wm5SN2FibElndXVSRTVpRnRFTGZ0NnhfWlltSmJoMlJN?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-08 [Uber vs. Pony AI: Which Company Has the Edge in the Robotaxi Race?](https://news.google.com/rss/articles/CBMiuwFBVV95cUxOLUlfUFRqSTNGOFpHcW05Vl9hWlJtbWtObmRHTHZJVHZpRFlGM1lTanlyVGtxNTU3MlZzLVJ6ekYwdFFZYTdsaHFDQi1wUmJkdmhlcXh0eDFQeEYzMVU3eE1IUkJpZ2VDb1UxU1BYR1VSalF3M0ZIYXRiOWFTUjFvWm5Yb0ViQXJyNEZxTlVpckMtSnBVZzN6Y3UzT1Q1bXlPNzEzbzBTei1NSXloMHlSZldfYWtzaDZNb2VJ?oc=5) <sub>TradingView</sub>
- 📰 2026-10-08 [Zoox Charged $42 and Took a 28-Minute Detour: David Moss on Las Vegas' Most Expensive Robotaxi](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1sc2dnNjNzbnNqTVdic3NBT2N4bHBBcTczUEFhZ05qek1iZFozUXoyN0pzdWVHdEw0UDZRTVlQQlNWN0Q5RHNZbk16MjVfUXZCR2FlR2dpS2V6Ykk?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-08 [What state is setting tough penalties for robotaxis that block first responders?](https://news.google.com/rss/articles/CBMiwAFBVV95cUxObmtEZ21hRXhoV3lDNzEyTzh5S29ySDRUUGdMbFJjblhIM2l1OGRkVnVjU2RaNWNTaEV6Qlg1a3RwWDdNTDZqZzVScXBGTy1LdHBuZkFrc2oyRHZ4WkU4SGJ5WGRUZTAzTnMtdlZtR0ZPM251Smd6LVozcmNGZlFKdnc2LU9URGVVUXNTTzZzMVdVQ09jNmVKd1ZNQnpHbjVaczhaNVdrQTFpdDkyVkZxRDBKZEZYVjBMM0ozVmpoZVc?oc=5) <sub>GovTech</sub>

</details>

<details><summary><b>Motional</b> (49)</summary>

- 📰 2026-10-09 [Pony.ai's Robotaxi Expansion Reaches Middle East and Europe; Goldman Sachs Maintains Buy Rating, Cuts Target Price to HK$202.4](https://news.google.com/rss/articles/CBMidkFVX3lxTE95VG5sWlNSQzI3MjVFNnBoYXVCTHVjNEpUdERqYWxIRVB1U1lGdFFYZ2FqWWdVT0JBZEtrVGxJODhVQ292U2Y4VlBJN09HUmxpZFlkN3dXUXhreFFWenZfcTljNWxVWXRhbC00VUpXNkctTHBXR2c?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-08 [[Shockwave] Singapore, Global Autonomous Driving Gateway and "Technology Test Bed"](https://news.google.com/rss/articles/CBMiZEFVX3lxTE5wTnQzckEweFYwbDQ1aXRpOU8wOTFpYmxCTmZNLTJRWEhWTWlvQjZMVGZHUWxjWlRHdzhQWkdaeUN0a3VHcTVNNVdUVUFMWjN0Q0VUVWNYMGlqQkhQcWczdUx2bFg?oc=5) <sub>아시아경제</sub>
- 📰 2026-10-08 [Zoox Charged $42 and Took a 28-Minute Detour: David Moss on Las Vegas' Most Expensive Robotaxi](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1sc2dnNjNzbnNqTVdic3NBT2N4bHBBcTczUEFhZ05qek1iZFozUXoyN0pzdWVHdEw0UDZRTVlQQlNWN0Q5RHNZbk16MjVfUXZCR2FlR2dpS2V6Ykk?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-08 [Zoox T-Mobile Arena Drop Off Field Report｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBBZjBWUjA3Njg0dGY4SU91bV9jMlk4NkU0bXJib3lwY0NtSENVclZjVU1jS1NVWlFvNk5yTlQ3Wm5SN2FibElndXVSRTVpRnRFTGZ0NnhfWlltSmJoMlJN?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-08 [Six Years Under Euisun Chung: Hyundai Motor Group Solidifies Top 3 Position, Surpasses Volkswagen in Operating Profit](https://news.google.com/rss/articles/CBMidkFVX3lxTE05el8wNkdNWlo4WUJxcFE4ejhyYkhPeDVxdVNHVkEzdVR2TVNtMGF6dzVQZ2NXVzBZYmlQaXU1NEpmQzRYdVgyemZsQmNoZUpCcVdMQ1o3TUh2RTRpUHlwZzFWTGIyUkUtejFaQnoySGs1ci1wYWc?oc=5) <sub>BigGo Finance</sub>

</details>

<details><summary><b>comma.ai</b> (24)</summary>

- 📰 2026-10-07 [Researchers Find that AI Models Struggle With Even The Most Basic Driving Skills](https://news.google.com/rss/articles/CBMiuwFBVV95cUxNb2ZGRGxGZDNjLWU1OVBPNjUtUlJXR0hiVGV3WEJ1eUVnSWExMWVvRmJjX2NtQm9sX0plMTU3YzZwUm5ZTzVoSGttcXZmQ3BqbW40X2doNFMycUk4UWE3anlidy1vWHNYZndVZjZWLUYtbnlHeVBFRjJOaTF4SWxzbmotR0xsNkVIcEhfZ0M3LUs5R2FyV1lVdlRRU3JwakpQcXpBUzlEOEhsWlB3Q19EdXFhQjRvZDU5MHln?oc=5) <sub>Auto Spies</sub>
- 📰 2026-10-07 [OpenAI's GPT-6 Astra is the only AI model to finish a real-world driving test in a Toyota Corolla](https://news.google.com/rss/articles/CBMifEFVX3lxTE9iZmN2ZFp6blVBRnZUTkYtYTJ3b0hSb0xhQjZyQXh5MUN2T3ladUlEb1F1SWJzc3FtamZtazk4LTVUWVpNX0ZjbGZwMnpERk45TVVQWVA1RjBZVUxxTTAzTWpaV1JqUzIwM1I2Wk1tTzc3bDJpaWluc2JVam4?oc=5) <sub>Crypto Briefing</sub>
- 📰 2026-10-06 [AI Agents Tried to Drive a Corolla, Crashing on 8 of 11 Runs](https://news.google.com/rss/articles/CBMiuAFBVV95cUxONWxQTEZham1kc1J4S2lMNUh6OTN1QWhXbl92U21NUWZTZWhNUUdwcFVvUHYtVWJzSjl4TjlCeFhUY2ppMXd3WkkxaHJFRmFlNUN2NGFSSENnV2ZZYWRNZ3JIUjd0dzFlTS0wR3gtbmxXN3VHOUkxWWg2VVFpTVgzWGN2T3RPdEFJV0cyWjRPSVFyNWZTYjFyX0pzYjFEUWQwLUlfbGo1bm8xVUZXQmpyQ3pCNXV5ZE9x?oc=5) <sub>thetruthaboutcars.com</sub>
- 📰 2026-10-05 [Researchers Discover ChatGPT Can Drive a Car. Grok, on the Other Hand…](https://news.google.com/rss/articles/CBMikgFBVV95cUxNNnNwX0g5bHV4STJlMXNOcXRnYnBHWHNoelViM2pJSzFob3dvUVJIdFlDRDV4X09DSVloZmxCTk5NODd3b3RBR2JmWEJQRktXUTYyWDNveS15UEw0NnVfSFluMlJxZHlBb3NhYnRNdDJsZ01MbVNpOXY4OW9nQnBSYnFRQ1U2YVd3a3R2ZTY4VlJNdw?oc=5) <sub>The Drive</sub>
- 📰 2026-09-30 [A $999 Box Promises Hands-Free Driving. Its Own Code Says ‘THIS IS NOT A PRODUCT.’ Now NHTSA Is Investigating Crashes That Killed Three.](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPNFIyamduTmQxb1dKNlh5Z1hCYUhyemoyU2I2bjFUWjZQSDVFSDFWOGxlM1hnQms4Q1lpalg0bXlCTEZTdVJ3eGtNTjlLamY2eW9LX09IejF6SkJxSmZ2QjRkU1pUczlRY2g3cUZIN3hvSUc3a3pUWHVKVk40MlY3Wk5SX3dnOHBl?oc=5) <sub>Yahoo</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
