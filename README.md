# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-10-08 · 1,252 papers tracked · 38 curated.

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
| [ASTAD: Asymmetric Style Transfer for Synthetic-to-Real Adaptation in Autonomous Driving](https://arxiv.org/abs/2606.29286)<br><sub>Dingyi Yao, Xinqi Zhang, Lihui Peng et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 1](https://github.com/Dingyi-Yao/ASTAD) | Synthetic data mitigates the data scarcity problem in autonomous driving perception |
| [Is Your Driving World Model an All-Around Player?](https://arxiv.org/abs/2605.10858)<br><sub>Lingdong Kong, Ao Liang, Tianyi Yan et al.</sub> | arXiv<br>2026-05<br>📑 5 | [⭐ 254](https://github.com/worldbench/WorldLens) | Today's driving world models can generate remarkably realistic dash-cam videos, yet no single model excels universally |
| [Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends](https://arxiv.org/abs/2606.01164)<br><sub>Jiuming Liu, Chaojun Ni, Mengmeng Liu et al.</sub> | arXiv<br>2026-06<br>📑 4 | [⭐ 239](https://github.com/liujiuming123/Awesome-Interactive-World-Model) | With rapid development of large language models and diffusion-based content generation, world modeling has attracted increasing research attention, benefiting various downstream domains such as game engines, embodied AI,… |

## End-to-End Driving & Planning

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](https://arxiv.org/abs/2609.26792)<br><sub>Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.</sub> | CoRL 2026<br>2026-09<br>📑 1 | [⭐ 11](https://github.com/VAIL-UCLA/DreamStream) | Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions |
| [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)<br><sub>Shen Zheng, Anurag Ghosh, Gaurav Parmar et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 30](https://github.com/ShenZheng2000/WarpI2I) | Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs) |
| [G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance](https://arxiv.org/abs/2606.26017)<br><sub>Hang Yu, Ye Jin, Alessandro Canevaro et al.</sub> | IROS 2026<br>2026-06<br>📑 4 | [⭐ 6](https://github.com/HangYuu/G2DP) | In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors |
| [Fail2Drive: Benchmarking Closed-Loop Driving Generalization](https://arxiv.org/abs/2604.08535)<br><sub>Simon Gerstenecker, Andreas Geiger, Katrin Renz</sub> | arXiv<br>2026-04<br>📑 17 | [⭐ 173](https://github.com/autonomousvision/fail2drive) | Generalization under distribution shift remains a central bottleneck for closed-loop autonomous driving |
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
| [SearchAD: Large-Scale Rare Image Retrieval Dataset for Autonomous Driving](https://arxiv.org/abs/2604.08008)<br><sub>Felix Embacher, Jonas Uhrig, Marius Cordts et al.</sub> | CVPR 2026<br>2026-04 | [⭐ 9](https://github.com/iis-esslingen/searchad_devkit) | Retrieving rare and safety-critical driving scenarios from large-scale datasets is essential for building robust autonomous driving (AD) systems |
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

<details><summary><b>Waymo</b> (230)</summary>

- 📝 2026-10-07 [Preparing for the Unexpected: A New Framework for AV Incident Management Exercises](https://waymo.com/blog/2026/10/incident-management-exercises) <sub>official blog</sub>
- 📝 2026-09-24 [Our Vision for London: How Waymo can Support a Safer, Connected UK Capital](https://waymo.com/blog/2026/09/visionforlondon) <sub>official blog</sub>
- 📰 2026-10-07 [Driverless cars hit the streets of downtown Detroit as Waymo begins its fully autonomous phase](https://news.google.com/rss/articles/CBMivAFBVV95cUxQSi1Vd3NlNVhsWjlGdlNFUkpUTU85ZFB0TklyOGxwYVdvTzFSNFhRVlRFSVU3T2x1a21oR0djWUVtOGVvNzJVWVZfeER2TC1WQWFkZ0g0THlOT002ejZ2cHQ3STBZMGY0THZUOGpSTW5ualctQng4bVRWV005QXhXLTZIYzNUWDQ2aktmcFZJSnBRWE5mXzJUTmMzQnlrcXJjS0pkbnI3S2FfZE1xb3JFN051VjZKbUpLSlgwcA?oc=5) <sub>WXYZ 7 News Detroit</sub>
- 📰 2026-10-07 [Waymo Robotaxi — Safety Concerns Rise Amid 210+ LA Collisions](https://news.google.com/rss/articles/CBMie0FVX3lxTE9BUUpkbmRHeHhYdmllc3B2Nklxdkx2cjQ2RUtXX2cwM21JNFhTMXM5YWxNRWVEMWJXZXRrNnNsclQ2VkNFc0lLWTFkSE1CVV8ta0VCY2VCODlhX2loTk8tOFRxLU5CMENFaTdndkpUeDBhMk9FOWZsVWNjdw?oc=5) <sub>The Korea Daily</sub>
- 📰 2026-10-07 [Waymo and the acceleration of autonomous vehicles](https://news.google.com/rss/articles/CBMiiAFBVV95cUxQZTEtaGxxZ2t2VzlnOGpPQjZlYXNKTW1pLVBhb2RSZWdLUkpXMjZoQUw0QUxTN2hJLTRxVThNWUY2NzdXeFkyNzdXdTJvT0tkOGgyTVZELVBsUUVTSml5OVdEUVNDRThRM3o2MnZOZkYzcXFWY3BweEt2eXNHMUVmd0piek1sd2Fm?oc=5) <sub>WPLN News</sub>

</details>

<details><summary><b>Tesla</b> (341)</summary>

- 📰 2026-10-08 [Key facts: Tesla price cut, record registrations; EU FSD delayed; Q3](https://news.google.com/rss/articles/CBMixAFBVV95cUxQQ2tJam9XbDRGaHkzdmplaHRuaGlUdnpNa1B1RmpHMUlTNDBfNlp6cTZUSVVwN3h6UjZLWk8yNjdlUEN0dnZvdTF1b25IS2dTbjBzQ3FJcXRsNHRLeEg3M2RNeU9qeno1OG9TSmJKbjBVdkl4eHFWMkJRcHdwSjJKWlloMVFYdWh5SHpCeU9MaXdmMk55UUswamlDRWh2RXpXVHpzUUtTajJCZ2IzU29kVkNmNHVTSUxZY2VQWlQ2OG9SQjUz?oc=5) <sub>TradingView</sub>
- 📰 2026-10-08 [德国联邦交通部力推特斯拉FSD欧盟审批 拟允许超速10%](https://news.google.com/rss/articles/CBMiYkFVX3lxTFB6bmh5YnJPNS0tb2NGMGZhTGROMUZWNXBTX0hjUmRZUkFjMFdTUHljRl9jUWx6QWRwV3VTT19Hdlpvb2YtYXN0ekxEbFVRaEprYzRDZjVXRDVjUHlqaTRVekt3?oc=5) <sub>观点网</sub>
- 📰 2026-10-08 [特斯拉无人驾驶出租车竟被灰色小猫给难住了- Tesla 特斯拉](https://news.google.com/rss/articles/CBMiYEFVX3lxTE83emxtTGRXT2wzZVVpQ2xHa0VvUGdxb1plenZJeTFDNEVEUGI5ek1XRWQ3TnFsR1R0VWdRWFA0VVJ6ZTFnNTNQR2xkZUg3cGtNQVR2Q3dCLUhuRzhuRFI1Zw?oc=5) <sub>cnBeta.COM</sub>
- 📰 2026-10-07 [特斯拉、比亚迪占据进口车市场40%……“维修地狱”与“半套FSD”8日接受国政监查质询](https://news.google.com/rss/articles/CBMigwFBVV95cUxNQXZJajdVT2xrSldfSWVNWmpDVmRqa1FJU3c3UnVuanlZdUhudkVTRGc3bU1rdENRRGZoamRtTktZV2VXREREb3BFMk91QlZ4SWJkTTNQdUtIMEVsTm1nMEJmeG5xdHY3STdGUEdPN2NLOU9JLUNiVkNKWFl3QWU1bE55UQ?oc=5) <sub>스타뉴스</sub>
- 📰 2026-10-07 [Tesla FSD V14.3.11 and V14.3 Lite Rolling Out: What to Do Now](https://news.google.com/rss/articles/CBMiaEFVX3lxTE1kQ201alBFM1VrTDBnSmRpM1lYRzkxSUNMWVl4ZXdTUm10V2NjclR2N3JrVkh4bnN5MUpJczhkU0dJQ21waUI3eEhTRXBwRlJCMUdIaEZlSlA2QjI0bF81QTRDM2xmVUh4?oc=5) <sub>BASENOR</sub>

</details>

<details><summary><b>NVIDIA</b> (218)</summary>

- 📰 2026-10-08 [Nvidia and Micron Set to Dominate S&P 500 Earnings as AI Spending Boom Drives 29.5% Profit Surge](https://news.google.com/rss/articles/CBMidkFVX3lxTFBySnUyWHBJOThueVYyY0lTYmI1MHF1UDVmczRQdXFaMlFZNnVZc2lYeUlTVmhqejAyOXBiR01kZkZhWGNuTWpMNG5qeHlHcXlka2pjXzZ5QjA5d1FxakRfRDR6WDlFR09ZU1lXclFrMDhmeXNxMGc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-08 [Can You Invest in Wayve in 2026? Details & Alternatives](https://news.google.com/rss/articles/CBMigAFBVV95cUxQdW45U05hcG5zUnk5WDBsVW00dkswdUN3X2twNEFjSVctNGxENDNYNGdrRGFCMWNZbEZBVk00cGVyX09kVFNWSTBBemNHYzJFVHJqN2lQd2lTdzllcUVaUHBpNHVnNXJ6T1k4ZzRPdi1ETVpUTkY0OFg5UUM3Z3Nqbw?oc=5) <sub>The Motley Fool</sub>
- 📰 2026-10-07 [Gears of War: E-Day Out Now With DLSS 4.5](https://news.google.com/rss/articles/CBMiogFBVV95cUxQcG1KbENSNjh5U2lPTEROT1VYdVBsU24yQzBseWt6VTc2bmozSFhpUFZhakFRWElyS0NKSVZmU2JRNWZ4NXRkbkZCaGlFOWFoV3lhdTNkQVdpNURBVFpSTFJTend4c2w5OEE2MXdBcHhTV3Z6SF9IcmFoZ3pteFk3bXN1TTlNVmZ5T1RHMFBhSzZaRC1LaDV1X2N5dEYzbjI0eVE?oc=5) <sub>NVIDIA</sub>
- 📰 2026-10-07 [Morgan Stanley reinstates this AI chipmaker as its top pick in semiconductors](https://news.google.com/rss/articles/CBMizwFBVV95cUxNX1YxTWRJNWp0bV9faHUzcUQtamZRZTVheGtSTkdYWHZ1OTRTX25BQjZTc1QwVEVhdkc2Tk1meU5jeDI4MmFRLWpqNk85bko2TjVZanNLcGFEUURmRzZsQTk2YlNYeV9ZS1NvVXJQWFdYVENOendiSlpwa1lOaDllTWVwb0ZBazBhcnhOSDFoYTNEWTQtemZzbnFSV3o3ZEpQNHRzMF8wbWNMWEhsUFFNdHRvcHZfX0lCNlZGNnVVLVAyMUxmNmRFWUFVVzkwRVk?oc=5) <sub>StreetInsider</sub>
- 📰 2026-10-07 [Open-Source SCSKiller Tool Precompiles Shaders, Kills PC Stutter [2026]](https://news.google.com/rss/articles/CBMif0FVX3lxTFBYdW92cWNNeFBWRXVnTlRuTHVxd3hiTkpjSWRHLTM4SnhlSWhLOVppSnVJWXpiSml0eE9mWDU2b2F0QzJHdWpmdFEwaE1tTlN3UkM3VXBabXg5WlA1UnUtUzJjSjh1VnQ1ZkxxTUxjY1IwUERsYlFUSHNNODRTbDQ?oc=5) <sub>https://tech-insider.org/</sub>

</details>

<details><summary><b>Wayve</b> (62)</summary>

- 📰 2026-10-08 [Can You Invest in Wayve in 2026? Details & Alternatives](https://news.google.com/rss/articles/CBMigAFBVV95cUxQdW45U05hcG5zUnk5WDBsVW00dkswdUN3X2twNEFjSVctNGxENDNYNGdrRGFCMWNZbEZBVk00cGVyX09kVFNWSTBBemNHYzJFVHJqN2lQd2lTdzllcUVaUHBpNHVnNXJ6T1k4ZzRPdi1ETVpUTkY0OFg5UUM3Z3Nqbw?oc=5) <sub>The Motley Fool</sub>
- 📰 2026-10-07 [Driverless cars are 'nonsense', says Oxfordshire-based motoring expert](https://news.google.com/rss/articles/CBMilwFBVV95cUxONTBQU0doTFlIVlVtV0pKMmtpeG1DbTFicU51SlFUODJBdDdGSEVjRDdGOV85Q2FkYmlxVWIwN0VvZTVvQ21VS1kyUVMyNEVOdFJ6dFVpbFRNRHdyV01lZXpGLTFkcWdZNi1EQWRjTVl2aUdCTzJmU0pRSDZxQ3drcm40TDk3MkpQcDh1UWpRTTZ0aGdUUTdz?oc=5) <sub>Oxford Mail</sub>
- 📰 2026-10-06 [Volkswagen reportedly picks Wayve over Nvidia for next generation autonomous driving push](https://news.google.com/rss/articles/CBMi0AFBVV95cUxNMmtmMFpodDVWb09kY2pNZXprRWhCbTNfMUJhcndsTF81bzdibGxMTHhtaUtXS2FybWJaMmM0c3lxcEkwMVliNGZGeGtBSVo5YjEzMEVnLUpiMVBlX09pV2o3M2hucEI4SVdYNG1TQnJaVkhnaXJQSUdERV9zZ0duLW9LVGJ1YU9OVTRIb195SDdWVmVSNUxTNDlPTkNKcDF6NXJFOV9QZnRFS2tRX21pbkhLbXlzVDNDaW4wa1BZaXZzRFp6eFRXbWs4MUxBcDJ2?oc=5) <sub>Business Upturn</sub>
- 📰 2026-10-06 [Watch Wayve CEO Kendall on the Future of Driving](https://news.google.com/rss/articles/CBMingFBVV95cUxQT1ZoV09JRWhBd1lXZW5ORnVVZHJCRTh1T0NseEZTZ3NEQkpMczFGU3pVdW5OZDBjckZQOXp2bW40Ung5Zjk4TDdiNGRlNmFEZ3RJYXBiemRaSS0tNXFnaUU5d3RXdWt6UHlQNWYtM3VlblNza1VIbURWZlppVFlPSWY2aHl2MkxtZTYwYUFDd0RvWEEyS05TTjRnY0FQUQ?oc=5) <sub>Bloomberg.com</sub>
- 📰 2026-10-06 [Stellantis And Wayve Take Hands-Free Driving Tech To Turin](https://news.google.com/rss/articles/CBMijgFBVV95cUxQbG9TWWUxSnZZaUh3SWJsODlXRS1uRWpHMFVpY1VqYUFfYUpDR0pxcjdpZUVOTGdBWkd1UjFZSjBrSm80ZnliOUVsTDlxZ3l2anpVZ21VWlhvMEpjMzdSckJYT0tBNEhqdzJkbUJqVnhfWTRMeGxoYWtrdFlUMHlPdXJKazhTX1NCVDJiRlhn?oc=5) <sub>MoparInsiders</sub>

</details>

<details><summary><b>Momenta</b> (147)</summary>

- 📰 2026-10-08 [Can You Invest in Wayve in 2026? Details & Alternatives](https://news.google.com/rss/articles/CBMigAFBVV95cUxQdW45U05hcG5zUnk5WDBsVW00dkswdUN3X2twNEFjSVctNGxENDNYNGdrRGFCMWNZbEZBVk00cGVyX09kVFNWSTBBemNHYzJFVHJqN2lQd2lTdzllcUVaUHBpNHVnNXJ6T1k4ZzRPdi1ETVpUTkY0OFg5UUM3Z3Nqbw?oc=5) <sub>The Motley Fool</sub>
- 📰 2026-10-08 [带激光雷达的豪华插混SUV哪款好？凯迪拉克全新XT5 PHEV与领克09、腾势N8等智驾车型横评+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE0zY0lua0JndHY4M3g4VjJWQWhQZjlnR3ZMS0hORjhGa20xS1V6dV9acDgyQlJhellmX0FxLWtfU1ZOX09acUpsQk1fN2tlRG0yVVBqcG1HOTZMRWtYWHc0?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-07 [新上市的豪华插混SUV哪款值得买？6款近期智驾横评，全新XT5 PHEV入榜+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1iSGR0T01ZcGljNXI0MmtGcUZkMUtQZTdHczJxaEI2a2kycEZfS3pVcVVNdFZOZnNxQjBiMWI4MEFDQTRmMG1vSjhSZTlMcWhPcU04VWVZNlo4cmo1RzhZ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-07 [新上市的豪华插混SUV哪款值得买？凯迪拉克全新XT5 PHEV与理想L7、腾势N9智驾横评+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE9ua0lwNldMUW1OVTE0OXhCeHZqcDN2a2pFMnY2TUpfYTZBRDlaSVE1NldTZHYyTjdVOTA4LW9WMWV1ckdhVHJkLVBUT0M4LUoyUXBzc0xDalgydUYyQ2RqcmhMVDhHOVJJV0NjQ2VQV3Q1Zw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-07 [The global robotaxi fleet to exceed 1.5 million vehicles in 2036](https://news.google.com/rss/articles/CBMikwFBVV95cUxQMUUxQ29BNHhpR3ZHZkRkZjlZYmlHNE1CWTdGNl9ub2lxME56TUwtdERBVEhRMzlPUjIxd1hZajl2MGdLcGNRdGd6ZkdPa29ZSUFieFluOHBFYlI5N0ZqYjJMRGF2WE5rZmQ0QzdlNjctNXV3Q1I1MUZVOF9NTXJUZk1DbFhsT1A5U2FpUkhEbFB4SWc?oc=5) <sub>TyN Magazine</sub>

</details>

<details><summary><b>XPeng</b> (257)</summary>

- 📰 2026-10-08 [XPENG names Robotaxi service 'XPENG YOYO'](https://news.google.com/rss/articles/CBMiogFBVV95cUxPVWo4R0xwZmlKVks3bVNWSnVYOTZVUVI1Yk40Tmo0b2laQzI4TUFjclZ0RERLOEdtaHUxZ2s3UVg0aDV4TmotcTZfWWhaOUpxMENPRE5SNEdJWHJnVVFzbWh6NFJoaXF5c0dRaFBOYlpjMFNKNGdVX2JjbDlFbE40RGxDanQtNU5sWVFFYXBaNHpRcGhDR2kyQnotdDQwXzdYeVE?oc=5) <sub>Gasgoo</sub>
- 📰 2026-10-08 [Xpeng unveils Yoyo name as it advances robotaxi business](https://news.google.com/rss/articles/CBMic0FVX3lxTE1QSnlWWGdaak1PN043Mng2cTdpT0tBd2VBbzFDWldZeUlsVzhNQW1RejR2YTE2UVRnSFFLN2g3RDNKbHRQWmktRS10bkxlMUp2RmpZd2g2TER4aTVHeE9qTXhUOE5XdzVCZ3p6ZEhMOGxpVms?oc=5) <sub>CnEVPost</sub>
- 📰 2026-10-08 [XPeng Names Robotaxi Unit "YOYO," Launches Ride-Hailing Mini Program in Commercialization Push](https://news.google.com/rss/articles/CBMidkFVX3lxTE1YYVJPel9IMHMwVFUyMDdPMDB6YmktNDRZMDdCOVZPOWZYcXVhQnA3U1h0TS11VlZyOW84ckF6cU4zWGFSU3JZalN0TkhiU21KX0tfb25lMUpkUkx3TldRTjFXX2xWTFNKcW5ySTk2cUZfMXFvalE?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-08 [小鹏MONA M03值得买吗？3个维度说清15万级纯电轿车标杆+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE9BZHBLQ0tHd0RqQVpVU0RLanEtMGFWdmI2OHBhVk51V0l6N21xbDZIb1NoM0VwN0tMSHBoRVRpc0FjZ3NZd1RxR0t3cS1GUllidWk3SFU2azBUQ1RQQVozRXpNNUFDU0VyY29JY0hQZkNCdw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-08 [小鹏MONA M03真实测评：续航真能跑620km？智驾靠谱吗？3个维度说清+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5DdWp2Nm9PUTZnVGtxbldtVEtkQ2xGRm5tUFROaXVtdEdfa015QzBIdWp4UEc4OVZQYmQtQXFHU0FKNGhlcndsemlVT21iMjlaRVk1WV9QUkxkVDk4TjhV?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>Li Auto</b> (180)</summary>

- 📰 2026-10-08 [NIO And 2 Other EV Stocks To Own](https://news.google.com/rss/articles/CBMimgFBVV95cUxNZHUtWnBHZm9pWmNKVUJRcllFMzlKeHRoLVhGZGZub3N2bVhYSGRwbDJnTFdnZFNISlZKaF9fR3RCbkFiQVAyWk80SW45Z0NSUVJmQUFTd1lGWXZ2NUctNjh3UkJ0RFhabGthUEFPQ2ItT3NrUDV0YzFHQk9JZGluWF9PNkJUbjhLcU5ndFlXU2tNT2lVaDk5QklR0gGfAUFVX3lxTE9EdldiY0NScWE2dC03MlpXZ0YtbE1yTGJZQXlDZmxtRnh6NndLREFDUW5GN2NiMy1PT2NTV1BIWXYxcWUyZXVOeW1Vb3J1Ml94UTJqakxNLU5BeXExSXc0bHhZa096NE5BZFVnTFpMOGhnRmVWd0xLTTJncHh3WjlMX09Sd0M0Mk5VMGhhMS1fdTA2aGRMX2dJNGhYejdhcw?oc=5) <sub>Simply Wall Street</sub>
- 📰 2026-10-08 [Can You Invest in Wayve in 2026? Details & Alternatives](https://news.google.com/rss/articles/CBMigAFBVV95cUxQdW45U05hcG5zUnk5WDBsVW00dkswdUN3X2twNEFjSVctNGxENDNYNGdrRGFCMWNZbEZBVk00cGVyX09kVFNWSTBBemNHYzJFVHJqN2lQd2lTdzllcUVaUHBpNHVnNXJ6T1k4ZzRPdi1ETVpUTkY0OFg5UUM3Z3Nqbw?oc=5) <sub>The Motley Fool</sub>
- 📰 2026-10-07 [Li Auto plans to enter Thailand by the end of 2026 as one more RHD market](https://news.google.com/rss/articles/CBMirwFBVV95cUxOM1BUTFMyZWVvZ285cVVKUXNfR2tEV3AzZXRWbGZ3NnJTZnFPNUJ6aUFaX0xOQ0RZQ2o3U1dBQjdoNWxFRG1xai15RFQtM1NwMElUazhuaXJTWHZWa184Zmp6MEtLRG01TTBjYm9FakRrZW4yNGNMeXpZVUNlY1U2dFU3ay1QSWlsazh0aWZCbEJfc1FVal9yWEZKa2FyblNXa3VZWVJQV0dzUTBvZVUw?oc=5) <sub>CarNewsChina.com</sub>
- 📰 2026-10-07 [限时28.99万起，集齐全地形+华为ADS5+800V？神行者8、领克900、理想L8三车横评](https://news.google.com/rss/articles/CBMickFVX3lxTE1zcUJibndCT1lOeV9GRDhqX3p3eUYzd3k5Y2pxR2xGQUtIZU9NaHZDQUNkRFRrZjdiQ2pFc1p1TmJpeC1yUUFJMzRwVEhSbEZLWC1IUlJmRnVZMjduQWtBNUFoWmNGalBuaTlvZVoxX3owUQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-07 [50万六座增程SUV，理想L9底盘操控体验](https://news.google.com/rss/articles/CBMia0FVX3lxTE9YR19SclhxdlRnem9lQWJjdlpjb0RaVnpXYlN1Yk5EaFhHZzZHbmM2ZkF6c3RfRTkzcEJCZXR5MkRHSHV2ZXo1RXBZOUJ1Z2NrM21ON0stUDBZcmtpWEhSWW1XakpCdll1VXE0?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>NIO</b> (167)</summary>

- 📰 2026-10-08 [Nio Onvo reaches 200,000 deliveries about 2 years after first handover](https://news.google.com/rss/articles/CBMicEFVX3lxTE1mX1FxdzZsREctTE92SFJGcWhwd2dib0tXSk9pTm84Q1dOT0lienMxYzY4M3pNMEJseThOYk8wUWhEVEZxTE14eXpwV3NhZU5JR1lGU0JaWDlkclpKbmI2c2FER0pvSE92bk5YRklkTWE?oc=5) <sub>CnEVPost</sub>
- 📰 2026-10-08 [【视频】《帮看车》3年3万公里长测：二代蔚来ES6，让我又爱又嫌？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE4zYkRFbnA5X1JzQnlOWDNiMTkzYzhneW9MaFRmdnRscVlxTjlaNWdGU0NIUW5Dbk81VVFZLUpLVDJ3ZnpCWlNrNi1FMWcyRzlLZ3ljUzNfRTRRV2s?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-08 [从ES6到ES8，体验升级不是一点点](https://news.google.com/rss/articles/CBMigAFBVV95cUxNTlUwbEctMm5NdXNhZkk0OU1Ob1l6eThuY3NTb3hGd0U1UFFjVk5GVkpRSHFHQ2dSVm5pM1lNcjV2UkIxak5aUFY0dGs2bzUyYldyaVNfQklIT0tzTWxXOC0ySGZwX3JOZGU5ZjJMelNkbEpTYy1qNTgzYVNGM1pwNw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-08 [【视频】蔚来ET5的上班穿搭7DAY](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1XRzBpU3VEdTRZVlhMYmZ1d2thWUxEQVd2dDExb2E0cW9QMDhyZGJmbXM5WlEyeF9RX2xPMHdFTjZNTC11aGpKOW5yZ3J5TGw0b1NJYjZTZHRHU3c?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-08 [【视频】蔚来ES8 2026款五座行政签名版租电版](https://news.google.com/rss/articles/CBMiW0FVX3lxTE8xcm1MT1NYOW9TSkhBZkNEdzRjRmpXN1J2bUk2VnNIQ2dYb1o5RFVXOXJkTGtyNUhDdEQ3bmVQWl9ja3NWVjlDSUF4a211LUx1Vk5lZFpEQTZ2WVk?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Huawei</b> (409)</summary>

- 📰 2026-10-08 [Huawei’s new US$3,500 trifold phone turns heads – but it’s not for everyone](https://news.google.com/rss/articles/CBMixAFBVV95cUxOOUJvNHB5ZkhTMXVVRTVHR2k2SEJwekh5SUhobG1IQkJpNmRBQXN4S096Z2Q2b19xRERRd2F0d09XQmg5TURjRXlqVEJ3RHhzbG1BeklEal8zblZIVXdyZFF1RmRQQzNSZ3lEdndRY0RzNTNTV3dXUEEyTG5hTFRqUmtUUEk5V3BkeEdRY1F4U2s1MnlPSE5oY1lBSWVnbHkxcmVQWm1OTGc4Xy1QTDdPaDY0dGo3RGpaX3VWbS10a1F1QVVM0gHEAUFVX3lxTE96SFlmOVJfSjZoQ2xMS3VDb2xwTEs3M1pWWUZ3VUc5bE1HY2hmQ2FodzJ5SnJnYVdfRlJhRUNOVjNzMHBhWjlaZzRlSWM5UENrQk5jd0g2NUt0ZmxPdE9tVGVDdXZuUHFtd3YzZXBGNVV0b0l1V2IzclRTa1hnamFucGN5cmYtTWpWdmZrWURHZ2s0WHFuUEs3MUhieUZCb2l6aW1SN3UxcGxFTWZpZHRoSnVvYld1YnpiYWhtWEdGM29PcGs?oc=5) <sub>South China Morning Post</sub>
- 📰 2026-10-08 [Sri Lanka AI Week 2026 Huawei continues to showcase practical AI applications](https://news.google.com/rss/articles/CBMiyAFBVV95cUxOT3J0emh2RjJINU5PYkFsZXMtcmJaSEdMVDBKejRReWoxckZvMi1rOGRESUhBdjc4bVdpa1d2TzJxOVAxay1KNTZOSEh4ek9VM0NPaGZQZnhrR0plRTBLeWdCUWlyTGRnaGRxRllLcVEwSjBPV1VqcFVYUUt6NmZ2X29YR2FJRERUSzJqallFMWJ3aV9iU2k2R2NrNDlKQUZvQkJxUEppbnZ6bURlTTV0TUNaTWs1aUh6WmthQ0QxS3VIbGFnZ3RSag?oc=5) <sub>Daily Mirror - Sri Lanka</sub>
- 📰 2026-10-08 [都搭载华为乾崑智驾与鸿蒙座舱，启境GX7与智界R7你选谁？](https://news.google.com/rss/articles/CBMiWEFVX3lxTFBzNFhBbkU0Mnp1X3h0OFlIYk9qd2l2NzBSMWt4dVlqZDFsb1dzcVdpYms5b0RMUjI4dWxJZEdpSWJ5WEN0a2hiY2FyemtTSUhIX0UtTFJfTjI?oc=5) <sub>爱咖号</sub>
- 📰 2026-10-08 [【视频】8.99万起搭载华为乾崑星海V6可4/6大平层](https://news.google.com/rss/articles/CBMiW0FVX3lxTE45WVVKamRGZldzZXVqendnNWQ5d2w4OWU3ZGYyOUp2ZDc4Zmtua3J5ak9vMmVZa1doX0J4MXBwWm4yVWhncGthWjUwY0gzNVZCUUZmWTJzamI3REk?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-08 [北汽星钽5X到店实拍：方盒子带华为乾崑智驾，钛7慌不慌？](https://news.google.com/rss/articles/CBMiTEFVX3lxTE4yb29KUktxUFQxRTNfelRnRDk3MnBKN3dBbFB2bkZVaXdYVjdjMDNlTG9nRFoyUnRCWlJib3RkSDA1ZHR1eXE2cmxqYlE?oc=5) <sub>搜狐网</sub>

</details>

<details><summary><b>Baidu Apollo</b> (50)</summary>

- 📰 2026-10-07 [Cathie Wood Bets Big on Flying Taxis With Joby, Archer Trades—Invests in TSLA Robotaxi Rivals WeRide, Pony AI](https://news.google.com/rss/articles/CBMi9wFBVV95cUxNSU1GeW9BdXZpVEd2Ym5vbEotR2ZqM1JYYl94S2tfX2EwRmpCQ3o2X0QxVENzVURaak5Rcjl3WjA3YTJTYll6T1doTi1yQ0txS0c5dHhQS3RaVHAtU1EyYmludG10aUEwZGpheVR6cnF6LUp2aWVTbjlycDQ0bHZKek1sWHFOOFFfa1BWRmw0N0FjQUpteWVhZThvSElGVnJHdkVYU21ZanFsczkwNkMwVlhIbXJlLTJnLXgwUXlKdkpBcHdCcGxWWTFYd2djREI2ZjF0aHdqZWQ2aGJXMUh3STNwRzRNZFRReXgyNncwcnFVSUpWdEFV?oc=5) <sub>Benzinga</sub>
- 📰 2026-10-07 [The global robotaxi fleet to exceed 1.5 million vehicles in 2036](https://news.google.com/rss/articles/CBMikwFBVV95cUxQMUUxQ29BNHhpR3ZHZkRkZjlZYmlHNE1CWTdGNl9ub2lxME56TUwtdERBVEhRMzlPUjIxd1hZajl2MGdLcGNRdGd6ZkdPa29ZSUFieFluOHBFYlI5N0ZqYjJMRGF2WE5rZmQ0QzdlNjctNXV3Q1I1MUZVOF9NTXJUZk1DbFhsT1A5U2FpUkhEbFB4SWc?oc=5) <sub>TyN Magazine</sub>
- 📰 2026-10-07 [Robotaxi market accelerates towards $159bn](https://news.google.com/rss/articles/CBMilAFBVV95cUxQeV9GbVdCVWVLUTRIM092WDFUWml4cEtRei15ek81c3l0c3JwdlJlQlpoWDlNQl9qdkZoOWd5UXpFS0VRUGxVVWhpeEEyOHB4WVBNaWNqQUVkWHRkVGpZUUFaZ3ZkamE3c0xfMmUxSENMR3VhbWY4TW5pR0tGbjVjbGluVVo4b2U5SzdFeU9QS3IySUdR?oc=5) <sub>ITWeb</sub>
- 📰 2026-10-07 [Uber launches Baidu’s driverless Apollo Go robotaxis in Dubai](https://news.google.com/rss/articles/CBMipwFBVV95cUxQMzBFUWtLM29UOTZfVTllWFJ3aUw4MFRqM2l2Wkd5aXN6bndfLWFzV3R4TFlzT3FLdXdXNDhPSTB6VTUzcUNWbnZnTTh0c2dDanYyYm85M0kxUEJuWTBEZmQ0X2J2U1RXRzh6SW94YWpvZ1VGUjU2YXRubVB3c2JmVy1TYjBwVm1iT1pNVTJLcTRQejJEekZJWG9iaG1TQ0NZVkRCbE94VQ?oc=5) <sub>scanx.trade</sub>
- 📰 2026-10-07 [李彦宏“豪赌”AI 10年，百度尚未写完的终局_公司新闻_财经](https://news.google.com/rss/articles/CBMiYEFVX3lxTFB6cUtNbllpMzhPaHdIRmZPWWl0emdZYkxESk90ZnJlRGxXcU1fM1Z5clpSTEU2Z3JaaDlMMVBCOEp2VWNJejFUTVRjMUxJdThoNDNDTEtXMUFTSHZfMlE4YQ?oc=5) <sub>证券之星</sub>

</details>

<details><summary><b>Pony.ai</b> (119)</summary>

- 📰 2026-10-08 [《大行》高盛降小马智行(02026.HK)目标价至202.4元 中国及海外Robotaxi车队扩张](https://news.google.com/rss/articles/CBMiXEFVX3lxTE1NUjVWMVhtQVZKTDJDYmhEYTl2NGtzd3pfNnJnMGNEalBFZmlhRE0tYlBhQmhiZHVBZ1BFQ0JTTWl3OHViME01NC1RVE5NWDh2Mlg3bkhheDBsU0la?oc=5) <sub>Moomoo</sub>
- 📰 2026-10-08 [高盛下调小马智行目标价至202.4港元 维持买入评级](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQQTFfMGdfTmFlTy1uNFY5YWlNa0pTMS11a21PbnBoa05GWVNYTGJHTzZ1UkVXZWllV3NDUVZ0SlBsQ2cxM0t2Z1RPejRKQ0djTndPbDMzSXlhcjY1RkZEUjFXYkFxNWROSGV5Tmphenkza0tydFFRMUV5VHpxZi1ZRnl1T1hkOGJKRTZV?oc=5) <sub>搜狐网</sub>
- 📰 2026-10-07 [Cathie Wood Bets Big on Flying Taxis With Joby, Archer Trades—Invests in TSLA Robotaxi Rivals WeRide, Pony AI](https://news.google.com/rss/articles/CBMi9wFBVV95cUxNSU1GeW9BdXZpVEd2Ym5vbEotR2ZqM1JYYl94S2tfX2EwRmpCQ3o2X0QxVENzVURaak5Rcjl3WjA3YTJTYll6T1doTi1yQ0txS0c5dHhQS3RaVHAtU1EyYmludG10aUEwZGpheVR6cnF6LUp2aWVTbjlycDQ0bHZKek1sWHFOOFFfa1BWRmw0N0FjQUpteWVhZThvSElGVnJHdkVYU21ZanFsczkwNkMwVlhIbXJlLTJnLXgwUXlKdkpBcHdCcGxWWTFYd2djREI2ZjF0aHdqZWQ2aGJXMUh3STNwRzRNZFRReXgyNncwcnFVSUpWdEFV?oc=5) <sub>Benzinga</sub>
- 📰 2026-10-07 [科技消费新趋势 \| 12公里18.5元、4次无保护左转……深夜体验第七代Robotaxi：从留意它怎么开，到悠然坐一程](https://news.google.com/rss/articles/CBMioAFBVV95cUxOSkNEVmNRNEVjS3JReDIwVzVlVUpKdHR3YktFWERzc1V0bnlieV9INmVKQ2RwODMyU0djWVhYUU5jeG93RHFSaDhWYV8tTUo5ZEkyb1dZdmlLSTZ1elVoRUUxVDlhSTcxNDNHdjFXR1lHU25MeU12NGh2amlON005YmNEQ1BWR1E4cGJGa1pMbHhqQ1ZRdmdicHpUMk5fcExW?oc=5) <sub>新浪财经</sub>
- 📰 2026-10-07 [Uber invests in robotaxi provider Verne](https://news.google.com/rss/articles/CBMigwFBVV95cUxQQkxEa25xSjBNT0ZJMzZINk54a2txS3k0S0pvTU4wZEJ5eVhHY0FNRWlyaVdIcVhYdmlPQl9HVUsyUnlkcW1UVzRVc180dHNCT1hXV3ZUcms3Mzg5aUoyZENTUWU3VHJtRlFuQmp0dWpQRDlmU2xlSDQ1MnlEZW11YmFGWQ?oc=5) <sub>electrive.com</sub>

</details>

<details><summary><b>WeRide</b> (119)</summary>

- 📰 2026-10-08 [[Shockwave] Singapore, Global Autonomous Driving Gateway and "Technology Test Bed"](https://news.google.com/rss/articles/CBMiZEFVX3lxTE5wTnQzckEweFYwbDQ1aXRpOU8wOTFpYmxCTmZNLTJRWEhWTWlvQjZMVGZHUWxjWlRHdzhQWkdaeUN0a3VHcTVNNVdUVUFMWjN0Q0VUVWNYMGlqQkhQcWczdUx2bFg?oc=5) <sub>아시아경제</sub>
- 📰 2026-10-08 [白犀牛完成1亿美元C轮融资 无人配送头部企业资金差距扩大](https://news.google.com/rss/articles/CBMiX0FVX3lxTE80c2pCdDA3VGJqYjN2b29lWGNfSkV0cXdsUjJ6b3AyVndOYndSVi1leEwxNGRuaEZfdTl0Q2NqYk0tS1F5UkZVMTZiT21FYjZqb3prNEpSS0kzRlNqUnZB?oc=5) <sub>虎嗅网</sub>
- 📰 2026-10-08 [恒生科技指数大调整 成份股将增至50只](https://news.google.com/rss/articles/CBMiigJBVV95cUxOMFNIMHZnbGhyMjU5dWU0Vl9ZQzUyMWpSU2JDeExraXRFSG1uY01BQkZ2UkJuMXpOaFpCMEU4a1B4UGE5bDU2Nzh6WUZQUDQ3RUZoa3VHX1VCNWN1My1XUDlLV3lwVW9DSkwyajBPUXJTWWZhaG83WFRraHEwSmF2MGg0TnlVRExPQVpDSnpvM2RXVlZVcUtPbmtIS3p1MWg4dDAyMG8xSU90YkNHREQ5TkQ1UGExbTc5VUdYQVBjVnREMW54Qi03TFhXNmRzUzZoRUVITWtaZ3pHVWMxS2hpcEtYWFlFX3F4R2FHczFjNDM3Y2FLYklzSlA5WDM3MHgwdV9yd0lzX0MyUQ?oc=5) <sub>新浪财经</sub>
- 📰 2026-10-07 [Cathie Wood Bets Big on Flying Taxis With Joby, Archer Trades—Invests in TSLA Robotaxi Rivals WeRide, Pony AI](https://news.google.com/rss/articles/CBMi9wFBVV95cUxNSU1GeW9BdXZpVEd2Ym5vbEotR2ZqM1JYYl94S2tfX2EwRmpCQ3o2X0QxVENzVURaak5Rcjl3WjA3YTJTYll6T1doTi1yQ0txS0c5dHhQS3RaVHAtU1EyYmludG10aUEwZGpheVR6cnF6LUp2aWVTbjlycDQ0bHZKek1sWHFOOFFfa1BWRmw0N0FjQUpteWVhZThvSElGVnJHdkVYU21ZanFsczkwNkMwVlhIbXJlLTJnLXgwUXlKdkpBcHdCcGxWWTFYd2djREI2ZjF0aHdqZWQ2aGJXMUh3STNwRzRNZFRReXgyNncwcnFVSUpWdEFV?oc=5) <sub>Benzinga</sub>
- 📰 2026-10-07 [激光雷达+702km，埃安Ray7把料堆满只等价格揭锅](https://news.google.com/rss/articles/CBMia0FVX3lxTE9tanJSWHF6enkxN3oyVkNCLUoyQXhMSHp3LTlnZHFEV3NRdDhaVnpnQklBUjlYTk9TYk1VOERnVllad3lwSFZfczIyTkQ0UFNsQ0ZwQURuRFh3ZzJPRXFPQ0NLdm04YlFrNVJ3?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Horizon Robotics</b> (194)</summary>

- 💻 2026-09-29 [HorizonRobotics/Ego4WAM](https://github.com/HorizonRobotics/Ego4WAM) <sub>GitHub</sub>
- 💻 2026-09-24 [HorizonRobotics/CogWAM](https://github.com/HorizonRobotics/CogWAM) <sub>GitHub</sub>
- 📰 2026-10-08 [磷酸铁锂电池和ADAS是什么？铃木e-Sky搭载比亚迪电池与地平线智驾芯片告诉你答案](https://news.google.com/rss/articles/CBMiWEFVX3lxTE5RV1l6NUV0em9YQmpSZW5nT1NBX2daa2dyejliR1F0dlM1U19KYURjWnRVT0ZPenlRVTBsRDJwbVk3TFRfbVliSHEzbVViaHZEbVNrZVktOGI?oc=5) <sub>网通社</sub>
- 📰 2026-10-08 [一汽-大众ID. AURA的第二款车谍照。做了个纯电家轿，尺寸不太大。看图应该和T6一样也有192线激光雷达+地平线智驾。#大众ID. AURA纯电轿车谍照曝光# ​\|一汽-大众id. aura\|纯电家轿\|192线激光雷达\|地平线智驾_新浪新闻](https://news.google.com/rss/articles/CBMiY0FVX3lxTE9OTVNCR0tOblVSWXVxRm1wbHA3Tmg0ZDIxWms5MHpVS0pMb25FMTAxeFhjblNlbjBSckVsa1lDc2g2SWNIczl1dmhiWUQ0Qk9LbzdxSWk4eUxFVEJ4bGlTbHM5aw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-08 [铃木e-Sky定档11月上市，310km续航+地平线智驾芯片亮点全解析](https://news.google.com/rss/articles/CBMiXEFVX3lxTE8yNkNwbzhBZ3FQd2ZRTVlrZGc5YlFuZG9xeENYZVg4NFZGTDNGcVZKdmRwcWhaNlNsTW9SdWxYa2hfZmtSb2tQc0JLa2s2VmtyMFBMSnBEZERxV0VY?oc=5) <sub>网通社</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (30)</summary>

- 📰 2026-10-08 [元戎8个月从第八杀到第二，城市NOA打响“华元魔”头部肉搏战](https://news.google.com/rss/articles/CBMibEFVX3lxTFAwbUU2LVd1bkVoVUZVcUdrczBEUmNwQzVnaDFXX0hQU3U4eVpScElhMC1ydHVPRVhuUHI5OVNYZXVjOC0xV3VkQUQ4Q2ZyNURuNUdWaTAwMWV1SkFUUUlxZXR5SjI5cFJSdzJrbA?oc=5) <sub>中华网</sub>
- 📰 2026-10-08 [城市NOA座次重排：第二换人，头部三强只差1.7%](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNd1ZkX3lwNUE5bUEtTGR4a1JiSHBSbXM1aDJxUmc4TEtlVGRJUFZKempPX1dtYVZoVkVRY1pZNWRlZ09GMzBBODRlQ0FMZjQtR0Z4R2g3NC1pUkhfeG92a3hzaGtuWDFlYk1ZaUJSWjZzVFh4R014cTFTZ1p4bW54WldObE9oTmEy?oc=5) <sub>搜狐网</sub>
- 📰 2026-10-07 [与问界M7同一工厂制造赛豆科技首车AIVA ME7测试车曝光_热点推荐](https://news.google.com/rss/articles/CBMiYEFVX3lxTE9fYVd2TTUyZWxoZC1ZZGNWczlwNXhUclo0OENVVkhhaFpxRTRFQlhNeFZBZXNRQUQ2MnVEOTB1TVAtMEZRTDVTQk5TcWw1QkZSSlRieUpkaXdpMl9xS0wzaA?oc=5) <sub>证券之星</sub>
- 📰 2026-10-07 [800V平台+700续航，三月亮相AIVA算速成车吗？](https://news.google.com/rss/articles/CBMiY0FVX3lxTE5JUnM5TE4xcUtpNjlSOFZJVW41bVpNRmZZZk9UQjhKWkV0SUNIcnBmVERJbEpzZFYwVkxwVXVvRDVnNmtOb2JBOFhKTVd2eVlpb2V2Ty1YQkJZTElKcURlZWFtZw?oc=5) <sub>www.bitauto.com</sub>
- 📰 2026-10-06 [【视频】特斯拉Model Y L 2025款长续航全轮驱动版](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9lN2x2MGx5NWdINEEwbHFXdUc0amd4czh1SllPek4yZG9XdjZPemxpSUp1OXQ0V1hOTjBRUW9yTE9HeWN1X0VPclNKdzVzMmh0d3RlVjF6N3hWVWM?oc=5) <sub>车家号</sub>

</details>

<details><summary><b>Mobileye</b> (24)</summary>

- 📰 2026-10-07 [Uber invests in robotaxi provider Verne](https://news.google.com/rss/articles/CBMigwFBVV95cUxQQkxEa25xSjBNT0ZJMzZINk54a2txS3k0S0pvTU4wZEJ5eVhHY0FNRWlyaVdIcVhYdmlPQl9HVUsyUnlkcW1UVzRVc180dHNCT1hXV3ZUcms3Mzg5aUoyZENTUWU3VHJtRlFuQmp0dWpQRDlmU2xlSDQ1MnlEZW11YmFGWQ?oc=5) <sub>electrive.com</sub>
- 📰 2026-10-07 [MOIA America Launches First Autonomous ID. Buzz Rides](https://news.google.com/rss/articles/CBMixAFBVV95cUxQY2FmM1hNRDEzV0c3c2NSVklIUDBPU1VrbmRmNnRLV3lNRzRITUVHUldKcVNYajNSYXJkdTJmbzRGeWt3V3ZrcXlmanBfR2t5cjRKZlU3b2JHbUg3VUx0ejdIS2ZUT25DRm5KTGtzSm1OaEhhQ2Zsb2Zhb0tHMDlnaWhnOGJHLXBvYk1GYkNYVFJRb2M2R3BmamRnN3RMZlJ2a3JlSGc3VnNmcXBtVDdub0s2VjhXSDhKVjFDR1pIQjYwLUpI?oc=5) <sub>Fuel Cells Works</sub>
- 📰 2026-10-07 [Uber takes a stake in Croatian robotaxi startup Verne](https://news.google.com/rss/articles/CBMikAFBVV95cUxOMkFfTDhoaldrejJpdUNUd1JvRXN1MlZwYVZQRjdPQ19FM2oyWjgxTndscUdGWFVZaG5nSWVKNWQ1dVYtNzFNZ2t0VnFwaS1mOFpneG41RW51M19leE9XSUN5WjhGbjF0ZkUtRVI4RDBiSUxtX2ZCTDBUekNRN3p1ZXZzUFU5aXJ0cjk5bHA3aUU?oc=5) <sub>Dealroom</sub>
- 📰 2026-10-05 [Moia’s autonomous shuttles start first passenger tests](https://news.google.com/rss/articles/CBMilgFBVV95cUxPaXBLWlk2ckZabm9UeXdOV1lCZTRjaDBkVmk4bDNVRWVMZkxKUEVTOVBqZERzWGlySkROdEs0bkE3SURjaG44c1Y4M3lsM0NmSG95X0diNlY4cGJoMUp1UUMxVnFkQ2Y0UTR2UDdtdTFzczBDSHpId3ZmWDltWlY3Ulg1bHBYMzJweHhDOWkzd3lyVWwxSGc?oc=5) <sub>electrive.com</sub>
- 📰 2026-10-03 [We Found Atoms, Rode Wayve and Watched Uber’s Autonomy Clock Speed Up｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1QZjNLZlpHR2ZtcHFaUDF5bEE3ZktHQlNoN0E1amxaVEg0eUdQbElIVlVVZk1JdTlqZG1kbGZYVTBvZDdKRDRKVWlqa2dRNDF3aTN4dEpmdTdxX0dTVnlj?oc=5) <sub>finance.biggo.com</sub>

</details>

<details><summary><b>Aurora</b> (50)</summary>

- 📰 2026-10-08 [US grants Aurora exemption for self-driving trucks safety feature](https://news.google.com/rss/articles/CBMiqgFBVV95cUxONnE4aU1ld3FwRG93N0JmVUhpT1AzcWx0cDkwWXRzbG81VmNGTE9GTHh1ZHVsajZmTDZGUXJockJMLXV5ZFN4emtGZE8yTFU3T2UzU2VkdWVXZGgyX2ZETmdTamhZa1pZbmVjNk9jUU9YRmNTelpfZVBoNDY4Y0xqM3FBSTFMUTgzMWFlaVVVaW5lWHVWN1J6bXRUeEd0eU5HM0o1T1BvcnRTUQ?oc=5) <sub>Reuters</sub>
- 📰 2026-10-08 [Bollywood actor Nana Patekar dies at 75](https://news.google.com/rss/articles/CBMimwFBVV95cUxPVzhsbTRiV1k4RzB1X01kY0IzUFZPS3ZySVFLeGVTZ1pOOXB5VzlpUjZ4a1hMUmtHckJtMGN4THpXUWUtVzVKLUl4eDBtUVlvR1M1WHdJOG1TQkpjTzFXdFQwTV9yUEpOSlFrTnRJclJVVXg2bkpKMEZVV3YxLS0xOVBncEN2LVFpR2w2MGFJSEtqb3Y2R2lwTlNRZw?oc=5) <sub>Reuters</sub>
- 📰 2026-10-08 [US NHC says Isaias has become a hurricane](https://news.google.com/rss/articles/CBMinAFBVV95cUxPcWFsYXRiMjJHNGJ5OGdEbHhfU2tZUlNEaWltRzZHbWlCcjk1OXlfUUlGV3h5Zjl4dlcxVG5KcG5PRDE0bVMwSVZaVHA1anFPSDVVUGJGN0ZnYUZVMzFyRl84SHFzMFFBQ1dicnhjQ3NkM1d0QXIyUWRmNWRHb1FCbENSc0YtdmIzbTRidktIM2JFUzY0UlY5dVFxVDc?oc=5) <sub>Reuters</sub>
- 📰 2026-10-08 [Trump awarding former baseball star Clemens the Presidential Medal of Freedom](https://news.google.com/rss/articles/CBMinwFBVV95cUxNdURUbzFPeVNUc2poVm0taDh3eE5sRlRyS0x0eVB5V0lDdE05d1RnS2s0dDhjTW0zUkRqd2toZ1lqMlVLV2VhbUZvSDRsbWt2RlZ6cGdVY2tmQnQwcVdyNGJnZGVZcXV3TFJfZ2hBNnNCWnkyajhtWGlSOWxZRzNFLTJPUWl5VU16Ym01RHM1emprMFhLWW5DcFUzV09YNjA?oc=5) <sub>SRN News</sub>
- 📰 2026-10-07 [Aurora Innovation wins regulatory fight as federal agency waives safety requirement for five years](https://news.google.com/rss/articles/CBMinwFBVV95cUxPVWx2WWNZRWVOT2xNei1QZGpNTndBQWNRNmM1WnA2R2pxWVRzUy14TTZEY25lSjlTNUdBTW1rbXlUTVRLSmRKTzFrVVRncDNzQkcyVlV1T012TGZSajdGWmxPRWJaYjBtNlpYc0NXVVY0a3pkWnNLa1ppbUN6TlhGR01lS203YkRseWNaY1RLWlM4TGNxTEY0bDZsTW0yWXM?oc=5) <sub>The Business Journals</sub>

</details>

<details><summary><b>Zoox</b> (91)</summary>

- 📰 2026-10-07 [Waymo Robotaxi — Safety Concerns Rise Amid 210+ LA Collisions](https://news.google.com/rss/articles/CBMie0FVX3lxTE9BUUpkbmRHeHhYdmllc3B2Nklxdkx2cjQ2RUtXX2cwM21JNFhTMXM5YWxNRWVEMWJXZXRrNnNsclQ2VkNFc0lLWTFkSE1CVV8ta0VCY2VCODlhX2loTk8tOFRxLU5CMENFaTdndkpUeDBhMk9FOWZsVWNjdw?oc=5) <sub>The Korea Daily</sub>
- 📰 2026-10-07 [My Verdict on a Robotaxi Airport Ride: Relaxing, but Really Slow](https://news.google.com/rss/articles/CBMirAFBVV95cUxPNFFERWVlTV8wWTFDcGFUMFBlbkxqTnQ4WTRlZnZsdlVqNXVOT0tqRDVWUnhRaXk5VW9mbGRUMFRpODBOTXk0M1RRaXBEbU5EaGhfMjRmS3pBaHJLN21EWTF4dEU2aUs3Wk0tQW5TTC14T1NnMGN4aWFkMUNzd3N5eHYzeDZYR0E1d0tjNjJZM0VqZUFOQXVuWTAxcFBxOFdhZ2p0dHQ5U0tCQ1la?oc=5) <sub>WSJ</sub>
- 📰 2026-10-07 [LastFeet Autonomous Delivery Field Report｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTFAzLVJQdDAwY2JXUDdLdjh5OW8zVmNRR0NoUEFaRGpEU2MyeUM5cmNjQW51Ykl0N0ltSVZoaHVNX0VDZlVYZ3cyRFlVVXEwTWVVMFczTVZZY0hBdl9tSm9n?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-07 [Metallica Returns to Sphere for Second Las Vegas Weekend](https://news.google.com/rss/articles/CBMimwFBVV95cUxQd3dJTmxid2lXSHo4M0lGdjUyS21HeHp0ajhWOEJRYUZIT09WYXdnak1Ob0NkTTBCX2pELTJHc0hqVWFpMzIybTFnZVhqNWNHOXU1VW0wY3Y5Mks0MEJObnFBY0h5MHdrbTduLW5DdEVldV9NaVJYVE1wODNOdi1lUE5QRW5vM05Pb1ZWX0lGNXJkb3hpX1AtdmZNaw?oc=5) <sub>Casino.com</sub>
- 📰 2026-10-06 [Waymo Boosts Private Debt Deal to $5 Billion in Push for Growth](https://news.google.com/rss/articles/CBMiswFBVV95cUxPdE02V0J1WUxHU09MaUNQZHk0cndQWk5mV1VVdG9hY0JLamRrRjQzVEdzYkNhVldEWFN4U0NZc20xV3I1UTlMcnZPMEpLZW1YZTNtWDhVVHpVUUIxaTJGSEJUV3RUZ3BvV3VaUEswbmpnUERsazRIYk1vQ0FuX3JSS2V3NUx0NXNvQi00V2dweDRfOWdWbDBzajQtbExJcEY5c2VfcF9EYWFrbDctSGJKRG03TQ?oc=5) <sub>Bloomberg.com</sub>

</details>

<details><summary><b>Motional</b> (45)</summary>

- 📰 2026-10-08 [[Shockwave] Singapore, Global Autonomous Driving Gateway and "Technology Test Bed"](https://news.google.com/rss/articles/CBMiZEFVX3lxTE5wTnQzckEweFYwbDQ1aXRpOU8wOTFpYmxCTmZNLTJRWEhWTWlvQjZMVGZHUWxjWlRHdzhQWkdaeUN0a3VHcTVNNVdUVUFMWjN0Q0VUVWNYMGlqQkhQcWczdUx2bFg?oc=5) <sub>아시아경제</sub>
- 📰 2026-10-07 [Waymo Upsizes Inaugural Private Loan to $5 Billion to Fund Asia Expansion](https://news.google.com/rss/articles/CBMidkFVX3lxTE5haXItRnN0QnQ0RHFkZUNWUG9MYlZFeURpbmtxb3VSTEVOYlVCNGF4emlrWUE4X1ItbDJFa0lFSmlQZVNNVnJQTWxDRkZKSVZzVnJzZzlodVhmTnBXaHB6eXdUNUdYNVdselFVcGc3Q1VEb2ZfS3c?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-07 [The global robotaxi fleet to exceed 1.5 million vehicles in 2036](https://news.google.com/rss/articles/CBMikwFBVV95cUxQMUUxQ29BNHhpR3ZHZkRkZjlZYmlHNE1CWTdGNl9ub2lxME56TUwtdERBVEhRMzlPUjIxd1hZajl2MGdLcGNRdGd6ZkdPa29ZSUFieFluOHBFYlI5N0ZqYjJMRGF2WE5rZmQ0QzdlNjctNXV3Q1I1MUZVOF9NTXJUZk1DbFhsT1A5U2FpUkhEbFB4SWc?oc=5) <sub>TyN Magazine</sub>
- 📰 2026-10-07 [Lee Redden's LastFeet Can Climb Code-Compliant Stairs and Save 25% of Door-Delivery Time](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5NRFIwR2ZoLVNxVmdaR2F3WFV6VWtSNEhnRUM2cDFLcXZ1TXRQU09HNkszRFlQNmZ2eEY2Q183N0J4NnFYbEgyLVhRd2FFVzF3S3c5WXc0QjRUa0U?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-07 [Germany Backs Tesla's Full Self-Driving for EU-Wide Approval, Musk Responds](https://news.google.com/rss/articles/CBMidkFVX3lxTE0wRWQ1Q2hHQU5yc0lvT2M2OGF5dzJkY1JwNERBdDFuQlpmVzhQdFlvWGVWREJZSWN5ZExPLUZBRFNCLXhsUmx3TFNGdHk1ZlAzVWlmQTRId3NYUklET3ZOcndjTk5XQnJGdXkwVDdvdDM0UU85YlE?oc=5) <sub>BigGo Finance</sub>

</details>

<details><summary><b>comma.ai</b> (33)</summary>

- 📰 2026-10-07 [Researchers Find that AI Models Struggle With Even The Most Basic Driving Skills](https://news.google.com/rss/articles/CBMiuwFBVV95cUxNb2ZGRGxGZDNjLWU1OVBPNjUtUlJXR0hiVGV3WEJ1eUVnSWExMWVvRmJjX2NtQm9sX0plMTU3YzZwUm5ZTzVoSGttcXZmQ3BqbW40X2doNFMycUk4UWE3anlidy1vWHNYZndVZjZWLUYtbnlHeVBFRjJOaTF4SWxzbmotR0xsNkVIcEhfZ0M3LUs5R2FyV1lVdlRRU3JwakpQcXpBUzlEOEhsWlB3Q19EdXFhQjRvZDU5MHln?oc=5) <sub>Auto Spies</sub>
- 📰 2026-10-07 [OpenAI's GPT-6 Astra is the only AI model to finish a real-world driving test in a Toyota Corolla](https://news.google.com/rss/articles/CBMifEFVX3lxTE9iZmN2ZFp6blVBRnZUTkYtYTJ3b0hSb0xhQjZyQXh5MUN2T3ladUlEb1F1SWJzc3FtamZtazk4LTVUWVpNX0ZjbGZwMnpERk45TVVQWVA1RjBZVUxxTTAzTWpaV1JqUzIwM1I2Wk1tTzc3bDJpaWluc2JVam4?oc=5) <sub>Crypto Briefing</sub>
- 📰 2026-10-06 [AI Agents Tried to Drive a Corolla, Crashing on 8 of 11 Runs](https://news.google.com/rss/articles/CBMiuAFBVV95cUxONWxQTEZham1kc1J4S2lMNUh6OTN1QWhXbl92U21NUWZTZWhNUUdwcFVvUHYtVWJzSjl4TjlCeFhUY2ppMXd3WkkxaHJFRmFlNUN2NGFSSENnV2ZZYWRNZ3JIUjd0dzFlTS0wR3gtbmxXN3VHOUkxWWg2VVFpTVgzWGN2T3RPdEFJV0cyWjRPSVFyNWZTYjFyX0pzYjFEUWQwLUlfbGo1bm8xVUZXQmpyQ3pCNXV5ZE9x?oc=5) <sub>thetruthaboutcars.com</sub>
- 📰 2026-10-05 [Researchers Discover ChatGPT Can Drive a Car. Grok, on the Other Hand…](https://news.google.com/rss/articles/CBMikgFBVV95cUxNNnNwX0g5bHV4STJlMXNOcXRnYnBHWHNoelViM2pJSzFob3dvUVJIdFlDRDV4X09DSVloZmxCTk5NODd3b3RBR2JmWEJQRktXUTYyWDNveS15UEw0NnVfSFluMlJxZHlBb3NhYnRNdDJsZ01MbVNpOXY4OW9nQnBSYnFRQ1U2YVd3a3R2ZTY4VlJNdw?oc=5) <sub>The Drive</sub>
- 📰 2026-09-30 [A $999 Box Promises Hands-Free Driving. Its Own Code Says ‘THIS IS NOT A PRODUCT.’ Now NHTSA Is Investigating Crashes That Killed Three.](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPNFIyamduTmQxb1dKNlh5Z1hCYUhyemoyU2I2bjFUWjZQSDVFSDFWOGxlM1hnQms4Q1lpalg0bXlCTEZTdVJ3eGtNTjlLamY2eW9LX09IejF6SkJxSmZ2QjRkU1pUczlRY2g3cUZIN3hvSUc3a3pUWHVKVk40MlY3Wk5SX3dnOHBl?oc=5) <sub>Yahoo</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
