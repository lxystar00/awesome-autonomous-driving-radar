# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-09-29 · 1,249 papers tracked · 44 curated.

**Selection rule.** A paper is listed only if it (1) is primarily about autonomous driving,
(2) has public code, and (3) shows at least one strong signal: accepted at a top venue
(CVPR / ICCV / ECCV / NeurIPS / ICLR / ICML / CoRL / RSS / TPAMI, or ICRA / IROS / AAAI / RA-L),
≥200 GitHub stars, ≥3 citations / month, or a well-known lab with traction. Papers are then ranked by a
composite score (venue, stars, citation velocity, LLM rubric for novelty / rigor / impact, SOTA claims)
with a per-topic cap. See [`scripts/rank.py`](scripts/rank.py).

📅 [Daily digests](daily/) · 🗓️ [Weekly digests](weekly/) · 📦 [Raw data](data/)

## Contents

- [VLA / VLM for Driving](#vla--vlm-for-driving) (10)
- [World Models & Generative Simulation](#world-models--generative-simulation) (5)
- [End-to-End Driving & Planning](#end-to-end-driving--planning) (11)
- [3DGS / NeRF Reconstruction & Sensor Sim](#3dgs--nerf-reconstruction--sensor-sim) (2)
- [Perception: BEV, Occupancy, 3D Detection, Mapping](#perception-bev-occupancy-3d-detection-mapping) (10)
- [Datasets & Benchmarks](#datasets--benchmarks) (3)
- [Safety, Robustness & Evaluation](#safety-robustness--evaluation) (3)
- [Industry Tracker](#-industry-tracker)

## VLA / VLM for Driving

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DeepSight: Long-Horizon World Modeling via Latent States Prediction for End-to-End Autonomous Driving](https://arxiv.org/abs/2605.10564)<br><sub>Lingjun Zhang, Changjie Wu, Linzhe Shi et al.</sub> | ICML 2026<br>2026-05<br>📑 1 | [⭐ 31](https://github.com/hotdogcheesewhite/DeepSight) | End-to-end autonomous driving systems are increasingly integrating Vision-Language Model (VLM) architectures, incorporating text reasoning or visual reasoning to enhance the robustness and accuracy of driving decisions |
| [Teaching Vision-Language-Action Models What to See and Where to Look](https://arxiv.org/abs/2607.01658)<br><sub>Yuguang Yang, Canyu Chen, Zhewen Tan et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 30](https://github.com/ShivaTeam/DriveTeach-VLA) | Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving |
| [CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving](https://arxiv.org/abs/2607.04179)<br><sub>Zhaohong Liu, Hao Ye, Xianlin Zhang et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 1](https://github.com/MICLAB-BUPT/CritiqueDriveVLM) | End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving |
| [TopoHR: Hierarchical Centerline Representation for Cyclic Topology Reasoning in Driving Scenes with Point-to-Instance Relations](https://arxiv.org/abs/2604.24119)<br><sub>Yifeng Bai, Zhirong Chen, Bo Song et al.</sub> | CVPR 2026<br>2026-04<br>📑 1 | [⭐ 3](https://github.com/Yifeng-Bai/TopoHR) | Topology reasoning is crucial for autonomous driving |
| [EgoDyn-Bench: Evaluating Ego-Motion Understanding in Vision-Centric Foundation Models for Autonomous Driving](https://arxiv.org/abs/2604.22851)<br><sub>Finn Rasmus Schäfer, Yuan Gao, Dingrui Wang et al.</sub> | ECCV 2026<br>2026-04<br>📑 1 | [⭐ 5](https://github.com/TUM-AVS/EgoDyn-Bench) | While Vision-Language Models (VLMs) have advanced high-level reasoning in autonomous driving, their ability to ground this reasoning in the underlying physics of ego-motion remains poorly understood |
| [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)<br><sub>Nan Yang, Zhanwen Liu, Linfeng Zhang et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 3](https://github.com/Zizzzzzzz/MVPruner) | Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings |
| [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)<br><sub>Yuan Gao, Wenting Miao, Mattia Piccinini et al.</sub> | IROS<br>2026-07<br>📑 1 | [⭐ 26](https://github.com/TUM-AVS/Chat2scenic) | Validating autonomous driving systems requires diverse, regulation-compliant test scenarios |
| [UniDriveVLA: Unifying Understanding, Perception, and Action Planning for Autonomous Driving](https://arxiv.org/abs/2604.02190)<br><sub>Yongkang Li, Lijun Zhou, Sixu Yan et al.</sub> | arXiv<br>2026-04<br>📑 14 | [⭐ 246](https://github.com/xiaomi-research/unidrivevla) | Vision-Language-Action (VLA) models have recently emerged in autonomous driving, with the promise of leveraging rich world knowledge to improve the cognitive capabilities of driving systems |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 3 | [⭐ 477](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
| [Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air](https://arxiv.org/abs/2605.31066)<br><sub>Tianle Zeng, Yanci Wen, Xueang Yu et al.</sub> | arXiv<br>2026-05<br>📑 2 | [⭐ 1,103](https://github.com/louiszengCN/CarlaAir) | Recent aerial vision-language-action (VLA) models show promising single-UAV capabilities, such as tracking moving objects and navigating to language-specified landmarks |

## World Models & Generative Simulation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [HERMES++: Toward a Unified Driving World Model for 3D Scene Understanding and Generation](https://arxiv.org/abs/2604.28196)<br><sub>Xin Zhou, Dingkang Liang, Xiwu Chen et al.</sub> | ICCV 2025<br>2026-04<br>📑 4 | [⭐ 71](https://github.com/H-EmbodVis/HERMESV2) | Driving world models serve as a pivotal technology for autonomous driving by simulating environmental dynamics |
| [FrozenDrive: Zero-Shot Text-Guided Driving Scene Generation and Data Augmentation with Parameter-Free Frozen Diffusion Model](https://arxiv.org/abs/2606.20110)<br><sub>Yuhwan Jeong, Hyeonseong Kim, Daehyun We et al.</sub> | ECCV 2026<br>2026-06<br>📑 1 | [⭐ 10](https://github.com/daehyunwe/FrozenDrive) | Synthetic data for autonomous driving is surging, powered by diffusion models that promise scalable scene generation |
| [ASTAD: Asymmetric Style Transfer for Synthetic-to-Real Adaptation in Autonomous Driving](https://arxiv.org/abs/2606.29286)<br><sub>Dingyi Yao, Xinqi Zhang, Lihui Peng et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 1](https://github.com/Dingyi-Yao/ASTAD) | Synthetic data mitigates the data scarcity problem in autonomous driving perception |
| [Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends](https://arxiv.org/abs/2606.01164)<br><sub>Jiuming Liu, Chaojun Ni, Mengmeng Liu et al.</sub> | arXiv<br>2026-06<br>📑 4 | [⭐ 237](https://github.com/liujiuming123/Awesome-Interactive-World-Model) | With rapid development of large language models and diffusion-based content generation, world modeling has attracted increasing research attention, benefiting various downstream domains such as game engines, embodied AI,… |
| [Is Your Driving World Model an All-Around Player?](https://arxiv.org/abs/2605.10858)<br><sub>Lingdong Kong, Ao Liang, Tianyi Yan et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 253](https://github.com/worldbench/WorldLens) | Today's driving world models can generate remarkably realistic dash-cam videos, yet no single model excels universally |

## End-to-End Driving & Planning

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [ExploreVLA: Dense World Modeling and Exploration for End-to-End Autonomous Driving](https://arxiv.org/abs/2604.02714)<br><sub>Zihao Sheng, Xin Ye, Jingru Luo et al.</sub> | ECCV 2026<br>2026-04<br>📑 7 | [⭐ 30](https://github.com/zihaosheng/ExploreVLA) | End-to-end autonomous driving models based on Vision-Language-Action (VLA) architectures have shown promising results by learning driving policies through behavior cloning on expert demonstrations |
| [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](https://arxiv.org/abs/2609.26792)<br><sub>Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.</sub> | CoRL 2026<br>2026-09<br>📑 1 | [⭐ 10](https://github.com/VAIL-UCLA/DreamStream) | Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions |
| [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)<br><sub>Shen Zheng, Anurag Ghosh, Gaurav Parmar et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 31](https://github.com/ShenZheng2000/WarpI2I) | Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs) |
| [G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance](https://arxiv.org/abs/2606.26017)<br><sub>Hang Yu, Ye Jin, Alessandro Canevaro et al.</sub> | IROS 2026<br>2026-06<br>📑 4 | [⭐ 6](https://github.com/HangYuu/G2DP) | In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors |
| [Fail2Drive: Benchmarking Closed-Loop Driving Generalization](https://arxiv.org/abs/2604.08535)<br><sub>Simon Gerstenecker, Andreas Geiger, Katrin Renz</sub> | arXiv<br>2026-04<br>📑 13 | [⭐ 172](https://github.com/autonomousvision/fail2drive) | Generalization under distribution shift remains a central bottleneck for closed-loop autonomous driving |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 12 | [⭐ 343](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
| [Latent-Centroid Steering: Single-Pass Classifier-Free Guidance for Command-Aligned Autonomous Driving](https://arxiv.org/abs/2608.00237)<br><sub>Meibo Hu, Jiamian Wang, Pichao Wang et al.</sub> | IROS 2026<br>2026-08 | [⭐ 2](https://github.com/codingmlinprocess/LCS) | Vision-language models (VLMs) have recently emerged as a promising paradigm for end-to-end autonomous driving, enabling agents to map multimodal inputs and high-level navigation instructions directly to executable trajec… |
| [STAGE: STyle-controllable Action GEneration for personalized autonomous driving](https://arxiv.org/abs/2607.29517)<br><sub>Zihao Liu, Xing Liu, Yizhai Zhang et al.</sub> | RA-L<br>2026-07<br>📑 1 | [⭐ 6](https://github.com/CarlDegio/STAGE) | Driving style refers to the behavioral preferences that drivers maintain during driving, shaped by their diverse experiences, habits, and needs, and is typically reflected in varying levels of aggressiveness |
| [SparseDriveV2: Scoring is All You Need for End-to-End Autonomous Driving](https://arxiv.org/abs/2603.29163)<br><sub>Wenchao Sun, Xuewu Lin, Keyu Chen et al.</sub> | arXiv<br>2026-03<br>📑 16 | [⭐ 255](https://github.com/swc-17/SparseDriveV2) | End-to-end multi-modal planning has been widely adopted to model the uncertainty of driving behavior, typically by scoring candidate trajectories and selecting the optimal one |
| [DVGT-2: Vision-Geometry-Action Model for Autonomous Driving at Scale](https://arxiv.org/abs/2604.00813)<br><sub>Sicheng Zuo, Zixun Xie, Wenzhao Zheng et al.</sub> | arXiv<br>2026-04<br>📑 10 | [⭐ 362](https://github.com/wzzheng/DVGT) | End-to-end autonomous driving has evolved from the conventional paradigm based on sparse perception into vision-language-action (VLA) models, which focus on learning language descriptions as an auxiliary task to facilita… |
| [Bench2Drive-VL: Benchmarks for Closed-Loop Autonomous Driving with Vision-Language Models](https://arxiv.org/abs/2604.01259)<br><sub>Xiaosong Jia, Yuqian Shao, Zhenjie Yang et al.</sub> | arXiv<br>2026-04<br>📑 4 | [⭐ 225](https://github.com/Thinklab-SJTU/Bench2Drive-VL) | With the rise of vision-language models (VLM), their application for autonomous driving (VLM4AD) has gained significant attention |

## 3DGS / NeRF Reconstruction & Sensor Sim

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DriveWeaver: Point-Conditioned Video Inpainting for Controllable Vehicle Insertion in Autonomous Driving Simulation](https://arxiv.org/abs/2606.31918)<br><sub>Junzhe Jiang, Zipei Ma, Zijie Pan et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 16](https://github.com/LogosRoboticsGroup/DriveWeaver) | A pivotal step in autonomous driving simulation involves inserting foreground vehicles with predefined trajectories into simulated scenes |
| [Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796)<br><sub>Leshu Li, Jie Peng, Yang Zhao</sub> | ICRA<br>2026-06 | [⭐ 11](https://github.com/UMN-ZhaoLab/Pocket-SLAM) | 3D Gaussian Splatting (3DGS) has garnered significant attention in Simultaneous Localization and Mapping (SLAM) due to its advances in capturing fine-grained geometry features and synthesizing novel views |

## Perception: BEV, Occupancy, 3D Detection, Mapping

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Deformable Gaussian Occupancy: Decoupling Rigid and Nonrigid Motion with Factorized Distillation](https://arxiv.org/abs/2605.28587)<br><sub>Yang Gao, Wuyang Li, Po-Chien Luan et al.</sub> | CVPR 2026<br>2026-05<br>📑 2 | [⭐ 22](https://github.com/vita-epfl/DeGO) | Understanding dynamic 3D environments is essential for safe autonomous driving, particularly when reasoning about human-centric, nonrigid agents |
| [ProOOD: Prototype-Guided Out-of-Distribution 3D Occupancy Prediction](https://arxiv.org/abs/2604.01081)<br><sub>Yuheng Zhang, Mengfei Duan, Kunyu Peng et al.</sub> | CVPR 2026<br>2026-04 | [⭐ 21](https://github.com/7uHeng/ProOOD) | 3D semantic occupancy prediction is central to autonomous driving, yet current methods are vulnerable to long-tailed class bias and out-of-distribution (OOD) inputs, often overconfidently assigning anomalies to rare clas… |
| [Revisiting Token Compression for Accelerating ViT-based Sparse Multi-View 3D Object Detectors](https://arxiv.org/abs/2604.14563)<br><sub>Mingqian Ji, Shanshan Zhang, Jian Yang</sub> | CVPR 2026<br>2026-04<br>📑 1 | [⭐ 9](https://github.com/Mingqj/SEPatch3D) | Vision Transformer (ViT)-based sparse multi-view 3D object detectors have achieved remarkable accuracy but still suffer from high inference latency due to heavy token processing |
| [FreeOcc: Training-Free Embodied Open-Vocabulary Occupancy Prediction](https://arxiv.org/abs/2604.28115)<br><sub>Zeyu Jiang, Changqing Zhou, Xingxing Zuo et al.</sub> | RSS<br>2026-04<br>📑 4 | [⭐ 138](https://github.com/the-masses/FreeOcc) | Existing learning-based occupancy prediction methods rely on large-scale 3D annotations and generalize poorly across environments |
| [Horizon3D: Sparse Radar-Camera Fusion for Long-Range 3D Perception in Autonomous Driving](https://arxiv.org/abs/2606.31096)<br><sub>Geonho Bang, Geunju Baek, Dongyoung Lee et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 23](https://github.com/geonhobang/Horizon3D) | Long-range 3D object detection is critical for safe autonomous driving at highway speeds, yet existing radar-camera fusion methods remain limited at extended ranges |
| [Explainability-Aware Frustum Attack: Exposing Structural Vulnerabilities in LiDAR-Based 3D Object Detectors](https://arxiv.org/abs/2606.29963)<br><sub>Chengzeng You, Binbin Xu, Soteris Demetriou</sub> | ECCV<br>2026-06 | [⭐ 1](https://github.com/SecMindLab/Saliency_LiDAR) | The structural vulnerabilities of point cloud-based 3D object detectors remain poorly understood |
| [PointLAM: Local Attentive Mamba for Efficient Point-based 3D Object Detection](https://arxiv.org/abs/2609.21780)<br><sub>Xuanming Shang, Weijia Zhang, Chao Ma</sub> | ECCV 2026<br>2026-09 | [⭐ 3](https://github.com/PointLAM/PointLAM) | 3D object detection from LiDAR point clouds faces a fundamental dilemma: voxel-based methods achieve efficiency at the cost of geometric quantization, while point-based methods preserve fidelity but suffer from prohibiti… |
| [Native-Domain Cross-Attention for Camera-LiDAR Extrinsic Calibration Under Large Initial Perturbations](https://arxiv.org/abs/2603.29414)<br><sub>Ni Ou, Zhuo Chen, Xinru Zhang et al.</sub> | RA-L 2026<br>2026-03 | [⭐ 12](https://github.com/gitouni/ProjFusion) | Accurate camera-LiDAR fusion relies on precise extrinsic calibration, which fundamentally depends on establishing reliable cross-modal correspondences under potentially large misalignments |
| [Vernata: Self-Supervised Learning of LiDAR Point Representations](https://arxiv.org/abs/2608.06919)<br><sub>Oliver Lemke, Alexander Liniger, Abel Gawel et al.</sub> | IROS 2026<br>2026-08 | [⭐ 17](https://github.com/rai-opensource/vernata) | LiDAR serves as a primary sensing modality for robots operating in outdoor environments |
| [Towards Compact Autonomous Driving Perception with Balanced Learning and Multi-sensor Fusion](https://arxiv.org/abs/2606.02979)<br><sub>Oskar Natan, Jun Miura</sub> | arXiv<br>2026-06<br>📑 44 | [⭐ 9](https://github.com/oskarnatan/compact-perception) | We present a novel compact deep multi-task learning model to handle various autonomous driving perception tasks in one forward pass |

## Datasets & Benchmarks

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [SearchAD: Large-Scale Rare Image Retrieval Dataset for Autonomous Driving](https://arxiv.org/abs/2604.08008)<br><sub>Felix Embacher, Jonas Uhrig, Marius Cordts et al.</sub> | CVPR 2026<br>2026-04 | [⭐ 9](https://github.com/iis-esslingen/searchad_devkit) | Retrieving rare and safety-critical driving scenarios from large-scale datasets is essential for building robust autonomous driving (AD) systems |
| [Towards All-Day Perception for Off-Road Driving: A Large-Scale Multispectral Dataset and Comprehensive Benchmark](https://arxiv.org/abs/2604.27499)<br><sub>Shuo Wang, Jilin Mei, Wenfei Guan et al.</sub> | RA-L 2026<br>2026-04 | [⭐ 6](https://github.com/wsnbws/IRON) | Off-road nighttime autonomous driving suffers from unreliable visible-light perception, making infrared modality crucial for accurate freespace detection |
| [123D: Unifying Multi-Modal Autonomous Driving Data at Scale](https://arxiv.org/abs/2605.08084)<br><sub>Daniel Dauner, Valentin Charraut, Bastian Berle et al.</sub> | arXiv<br>2026-05<br>📑 2 | [⭐ 396](https://github.com/kesai-labs/py123d) | The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics |

## Safety, Robustness & Evaluation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [CCFM: Collision-Constrained Flow Matching for Safety-Critical Scenario Generation](https://arxiv.org/abs/2607.04451)<br><sub>Ke Li, Kaidi Liang, Yuxin Ding et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 3](https://github.com/KELISBU/CCFM) | Evaluation of autonomous vehicle (AV) planners in safety-critical closed-loop simulation is essential for real-world deployment |
| [Lipschitz Optimization for Formal Verification of Homographies](https://arxiv.org/abs/2605.23203)<br><sub>Jean-Guillaume Durand, Panagiotis Kouvaros, Maxime Gariel et al.</sub> | CVPR 2026<br>2026-05 | [⭐ 2](https://github.com/jeangud/homography-verification) | The adoption of vision neural networks in regulated industries requires formal robustness guarantees, especially in safety-critical domains such as healthcare, autonomous vehicles, and aerospace |
| [CADET: A Modular Platform for Evaluating Distributed Cooperative Autonomy in Connected Autonomous Vehicles](https://arxiv.org/abs/2606.04072)<br><sub>Pragya Sharma, Brian Wang, Mani Srivastava</sub> | ICRA 2026<br>2026-06<br>📑 1 | [⭐ 0](https://github.com/nesl/cadet) | Deep learning models are increasingly central to autonomous vehicle (AV) pipelines, yet their integration has traditionally followed a monolithic design where perception, planning, and control execute on a single onboard… |

## 🏢 Industry Tracker

Latest 14 days of news, official blog posts and new open-source repos from tracked companies. Full daily feed in [`daily/`](daily/).

<details><summary><b>Waymo</b> (102)</summary>

- 📝 2026-09-24 [Our Vision for London: How Waymo can Support a Safer, Connected UK Capital](https://waymo.com/blog/2026/09/visionforlondon) <sub>official blog</sub>
- 📝 2026-09-22 [Introducing transit rewards](https://waymo.com/blog/2026/09/transit-rewards) <sub>official blog</sub>
- 📰 2026-09-28 [Waymo, Uber, Lyft Hit Gas On Robotaxi Real Estate Expansion](https://news.google.com/rss/articles/CBMizgFBVV95cUxPR3QwUkxkbUVIMDRlaEZ3cU04bTZsY0NpdE5TYXJpSWtQQ0N5X3ZUa0E2dkdtSzgwNjVsVlI1NGJ2bEdkckJxUU1nTy1QOHlLMzNBbGhNUVZVQjFEbklRYnhyMjM0Y2loTFhRbjU4OWZHdGkyVjJ2RzJGRVhVbk5wSmRjTW40LU5jMHliZTZ1NVctUlNodnVudjRLeThxdTdhaERBak1WdVZCajVhSllDVWhYQmNMWVYxT2xWZFFoeEx3c1JLckduMy0tOF9LZw?oc=5) <sub>Bisnow</sub>
- 📰 2026-09-28 [Chinese Cars Are Already Invading Texas, And You Can Thank Waymo For It](https://news.google.com/rss/articles/CBMiWEFVX3lxTE53WXRFZkQzdHZXVi1Nd0p1OGQwa3BnMUdYWHJfUVVEQWtxLW5sQnM1cnFjeTBWNWI3NkpoWTVZQlpVdGYwX3h4eTFFbFY0dEdfT0lzakFuQ1M?oc=5) <sub>CarBuzz</sub>
- 📰 2026-09-28 [Waymo Robotaxis Arrive in Munich as Testing With Jaguar I-PACEs Begins](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNbmpjeVY4SDJGRlQ5WkRlazFueHZtMFpWYjQ3aWFQTHBmQmVCbjJMZzVuUV80RUlaYWtnS2YtdmV5Q2pWOHNIeC16UUdqRk90TEtSMFFzNVNVZkRyMFo3TEw2TTdTSEdId0FSdXdKbWhrVExZU0FaMTR3LTJZVmhNSmRjZC02NW5BM3FuRTlDazl2SWtDaVR6ZXRRWXlnejFxeGViSG9uOHNjZw?oc=5) <sub>eletric-vehicles.com</sub>

</details>

<details><summary><b>Tesla</b> (152)</summary>

- 📰 2026-09-29 [中国智能辅助驾驶达到全球新高度 小鹏NGP和特斯拉FSD首次同台竞技，小鹏在小路窄路和复杂场景更胜一筹](https://news.google.com/rss/articles/CBMidEFVX3lxTFBwNTBtUXdBVHBqRmxCeXM4aUk3MmwzOTZESHZycm0ycUlNU0ZjUVotcVdpaG1IaTZSV0RzMzd4bk9pZ1hKZXhxbWN1R3hWb3FnZG9fRWpseGgwUW4xQ0dBR0QtSmpXdzFYR2Z4RjZudEdoSldk?oc=5) <sub>金融界</sub>
- 📰 2026-09-28 [Tesla FSD and the Free Trial Offer: 5 Details That Matter](https://news.google.com/rss/articles/CBMilgFBVV95cUxPQUVyTTZPRjYyUkZTeEZyLVh5Tmg0eXNSSFpsYUV5elB3eEcteG42SEpaeVhGOHA0NXU4d1dlaV9rSXg1OEladl9XVGhva0NNRTFsYWtHSjYtNVdOSjBfdk13YzktdHB6SGY3d0ZDWWFuSW8tVzZfUTAzeWRyOTR0TkhsUWk5clVNM3pXVVhLYkRBOXY5dkE?oc=5) <sub>BASENOR</sub>
- 📰 2026-09-28 [XPENG VLA 2.0 vs. Tesla FSD in Amsterdam — Part 1: XPENG L03](https://news.google.com/rss/articles/CBMimgFBVV95cUxQQnk0MEdBMmE1dFRENzBOcEU2SFlsRDRjVTdIT0JxWUxRdTktNVhBWUZneGxNcTE4bzlWZER5VjdSbFNvZmE5RVFRQm55OEJ0Nk1BNnIwemRTNkZ4Z1czQ3lJRGlOdnZPMEhWSHJQX0VSY3pza1NsTWJQSlJENWxVOWxwb05oaGZocVJZZ3pqdGZERF95ZkFOdzlR?oc=5) <sub>CleanTechnica</sub>
- 📰 2026-09-28 [Tesla: Current and upcoming models, prices, specs, and more](https://news.google.com/rss/articles/CBMiSEFVX3lxTE9IaWtMS3AxdnhqLXNOTXJmaGRJdmdnMVUwV0lsMmJJbGZ1TlFNX0pMV0VfTkZpMXFwOFZnT2E2UWhrM0dhVFlEUg?oc=5) <sub>Electrek</sub>
- 📰 2026-09-28 [Tesla Lawsuit Claims Autopilot Accelerated So Violently the Tires Burst](https://news.google.com/rss/articles/CBMiowFBVV95cUxOdGpIV1M3RDlhV3dmQkFnM192OTF5aW5GMUw2X1ZKNDFkZmtPSXNGUzYzSnNNZW5lMVpKUmFEQWRwTFpmbjViUEFwV0pYZi0xeXVNSmJabUQ5NkZHbmZ2U0gtaThuY2ZiUEZzem5iZkRvaDYxcmFoMXZPLVJNSzZfN0xPck5VOTJ2X1V2R2UtaDU5TG5ZZ05lVmZ0ZVN1cTRPZUQ0?oc=5) <sub>Autoblog</sub>

</details>

<details><summary><b>NVIDIA</b> (105)</summary>

- 💻 2026-09-18 [NVIDIA/swe-serve — SWE-Serve: an agentic benchmark of 53 production inference-engineering tasks derived from merged SGLang pull requests, run with Harbor.](https://github.com/NVIDIA/swe-serve) <sub>GitHub</sub>
- 💻 2026-09-16 [NVlabs/Skill2Env — Democratizing Collective Intelligence](https://github.com/NVlabs/Skill2Env) <sub>GitHub</sub>
- 📰 2026-09-28 [China May Let Alibaba Buy Nvidia’s RTX Chips, Information Says](https://news.google.com/rss/articles/CBMitAFBVV95cUxNSmpMYk0xRTBfdm5NMXRfNVNfMlE0cnppenNvTHNITzhVNXZ0R2NIX0Z3bmlWSmV1RHBpYURmWmdMT1ZLY2hUWG5WcDRsaFVSWktoRWFNQkdtRzg5UHpLeGstQXFGdkprdGhEbk05RUE5MEM4UTVlb281N3lOb2Y2WndNNHhzNUEtU3JlMUd5Z2FQRFRiM29JMU1fa25QRzBnekJJU3FYZGZlby1faklDS1pURG8?oc=5) <sub>Bloomberg</sub>
- 📰 2026-09-28 [Powerhouse PC, ideal for QHD or 4K gaming, gets price slashed by $239 on Newegg right now in this unmissable deal](https://news.google.com/rss/articles/CBMi2AFBVV95cUxNcUNmWlpkdDFtcEJpcW16TWlYMnViMi05aDc4dWJ2a0xhdHJTSzFnQTJJRjJRUEYzWUxMM0FhcWxGeEF5bkIzYU9WZTM4MGVJTi1zUjJObUxZWWlic0J5d3JnTGRTdmJXa19Sb0NpT3czUWd6TGJnVHEzRmxUSGNLeDRWTkgyVG8yNzF5aXk3MEd5T3RxMnF1MGdJSFlKWnVDVWhYa0hoMVRLODV2bk5uWW1nOG9rTG1ZdkRRY3I1N0tYWmRCcEdKZTVqNDlHMVI3LUpBd0k2eTQ?oc=5) <sub>pcguide.com</sub>
- 📰 2026-09-28 [NVIDIA Cosmos 3 on AWS: Omnimodal World Models for Physical AI](https://news.google.com/rss/articles/CBMipgFBVV95cUxNRWh4bjdGQS1pMGVZWHVERHd6dmtSVFpaNWlkUU9FY0lOUlZxd1NYVUlsZUN4dDZXZHhQWUNUMUJNN1dmb2Z5aGJDbjhiQ0RQYVpLQnF4cl9SZi0xQmVGQUNORjIxVDRTd3V1Yi13ZXNkUTRRRmtJY0piUHBuaVFfS0N5dTNLV2NUdk1uT1ZfUzhLTWZfS0wzMTE3ZGJIeG9DaFBtS1dR?oc=5) <sub>Amazon Web Services (AWS)</sub>

</details>

<details><summary><b>Wayve</b> (48)</summary>

- 📰 2026-09-28 [Weekly Recap: Rogue e-Power U.S. launch and Wayve Series D backing](https://news.google.com/rss/articles/CBMixAFBVV95cUxOVlZpTlo1a01ucWczNXRhSWUybHFWSG93TVdfNS10U3RtSU1nbkE2UlhJNlV4WkVUQTBjRG51NlB1WFRScF9fZ0dsNDcwanlneGUyZ1pvS0lDeTlmcXBzcWd4bmVYVF80cmx3bGcwaVdFN1VLM1plT3prNnN4NGNPd2I4Mmx1d2paWjYtVHNBOWMtUUxRQVlWdmVleGV6eVNSRnhvRVFYSWpuLU9GcUZfRGVTalhsZEdGNFZISFphcnBXMnFU?oc=5) <sub>TradingView</sub>
- 📰 2026-09-28 [Nissan to trial autonomous car in Cambridge](https://news.google.com/rss/articles/CBMinAFBVV95cUxPd2xuUWJvMXFZM3ZBbE0yOXlvOWdaRkgtNzlRVXplUDE2S1JCaERaY3FtWF9pVkowcmJ5MmE2TWhMcGhqZW84RGF0RXVOTWpZRXNqbDZFMk1rdnZBeE9ack93dm52UEhCa3FCWml0aDJBX1FqQ1VoMmk1aHZVNWxuQ3pRcGpHaDRfRW5CckRGWDgwbVpxSmlSdzljSXU?oc=5) <sub>Motor Trade News</sub>
- 📰 2026-09-28 [Nissan Motor Remains On Thin Financial Ice As Midsize Rogue Hybrid Debuts (OTCMKTS:NSANY)](https://news.google.com/rss/articles/CBMitAFBVV95cUxNQ1dWdmhFVUlldnNCT3FOSUJCbU9ZcTd6Y2tXVUR6UVhEck5UaERoejd3LWFlbDctbEtGVTNUVFVtb2YxZmI2Unl5QzVTSjQtVThTbWJkMlRaN0V6TkJkQ1kxWlU1dTVFbzJkeEF6RzdjUTFNMGpvNGU4dG5LaTRmc0ZxbE91Y3c4ZWR5b0xIOFN6VU1IekR6d05PeGtaSk5uU3pVUXBobktHc0FBY01JUkg1TC0?oc=5) <sub>Seeking Alpha</sub>
- 📰 2026-09-28 [Nissan leads £3m autonomous transport project in Cambridge](https://news.google.com/rss/articles/CBMingFBVV95cUxPYndubmh5QUx0Zzk1UnhSb0NyeHg1cEczc2g1Wk1UQXgzQk9JSUlMN2dSSXRibGtXdjVWRVZVZXhxdzI1a0k1cWFxdkUzazVjak8tbGQzTF9PWW8yQ09yU0xjT1pWUmdLTjlRSjNucjY5c1Y2OXMxRmFvZFVTMzBxQnVfTGU1cGEyNG5fWi1Qdy1BNlNEX1o0bE1WNDA4QQ?oc=5) <sub>theengineer.co.uk</sub>
- 📰 2026-09-28 [Momenta and Stellantis' China JV with Dongfeng to co-develop intelligent driving technology](https://news.google.com/rss/articles/CBMihgFBVV95cUxNeC0tUXRtQm5pbU9ISEc0ZXhNbmktUmRjNkY1eldSeWxtSEJPV25kdWRYOG1QZ1Axckh0SVdHbnhJVXVZSnNvUGZNY3BnZ2xfVWstcTE4dDgxSkZScGZsMmJqbS1LdnNWYzlNbnlzeUk1UDQzWW9hR3U4Z2dlSVhBd05qVmVXUQ?oc=5) <sub>AOL.ca</sub>

</details>

<details><summary><b>Momenta</b> (100)</summary>

- 📰 2026-09-28 [Momenta Brings Driver-Assist Tech To Jeep And Peugeot](https://news.google.com/rss/articles/CBMiigFBVV95cUxOdTZqa2tVZWRpZGtOd05rT0pXRXRUQnFuTi1uUnlYVHVRMW5KTnFTbFJkU0pib3hYS0tORTBLdEh4cHBQWUk4dFQxQW1nN2x0bG53WldzS0JrdG1BczFaeHItTktzYW4tOVBKb1g5blk2WnB1Qlo3U2JuS0dfQnE4RG5HTHQ3cFlpZ3c?oc=5) <sub>Finimize</sub>
- 📰 2026-09-28 [Momenta and Stellantis' China JV with Dongfeng to co-develop intelligent driving technology](https://news.google.com/rss/articles/CBMivAFBVV95cUxQMzByVUtHMHlIWGhiUzl5Vzd0YXhiWnZ6R25pMzVUTjlLSW1SaDFnRy1fSnAwd1BlUWwzb0dBa3ljWnZLRWlKNmdIYXpXUTM3QUg3MjByLVZSd042VkZZT2F1LXVaM2xaZzN1X01WWWE1LS1wVG9hNlY4TjE1MmtKb1YzR1NoTTBhRHNwSzMzYW9LSDhTMlFjQ3g2NWtNYWdfSmFpX3c5bHlBSkxPUnFnbDBpb1ppS2ZQNHM3NQ?oc=5) <sub>Reuters</sub>
- 📰 2026-09-28 [Momenta 智驾方案上车标致、Jeep 全新车型 将落地中国及欧洲等市场](https://news.google.com/rss/articles/CBMiXEFVX3lxTE9xRnQ5dGJUSk9fRTRGQVFsZ0M4SmFqOHZpLXNZYklDc1lEeU93T2ZIbXNrSGpTTzhGTWhlMHdZRVJyZUduczdLdlBldzM4U19oTWR5cC1Xa01vbThH?oc=5) <sub>Moomoo</sub>
- 📰 2026-09-28 [Momenta, Stellantis' China JV with Dongfeng to co-develop intelligent driving technology](https://news.google.com/rss/articles/CBMiuAFBVV95cUxPWGVYNnVlOHpSVlB0czRybUZkcUJvZFBRMzRHNzd0cW1TV2p1TmM5MC1XZkl1RFEwLTlVcG9RbWdDN1A5UkFmTllUMEdLNmNOVEZrN3VEQWt3M0xMdWNHeURTZ0g5a3dDVDVTbVBhVWRXV1F2X2pHMlVxUmlKRWF6YW96ZmtabVhQZU9iRmVMTUcxeElVeXVWWGpkMzA5OWpQb3BkTnowVUVfT0Q0NkVlX1c4VG1hOGpu?oc=5) <sub>NST Online</sub>
- 📰 2026-09-28 [Stellantis JV, Momenta to develop driver-assist systems for Jeep, Peugeot](https://news.google.com/rss/articles/CBMilwFBVV95cUxNOEg3UTltZExodWZFMUNKVXczckxwdHJkUVVaZTB0RkN5dkkxUEV6WWtKalQ5Rjk1dk15VDdFc3ZuNUt0bmg4bXdWbTcxQmFGeFJxNVBXUGdlZWRfUUNYR3dwem9neGNmZUZGdnhvbjRoWElBVk84RXNjSjdjRnpFNkNja2FCRkFyeHlTWkxYODM1a3JtS3o4?oc=5) <sub>Automotive News</sub>

</details>

<details><summary><b>XPeng</b> (133)</summary>

- 📰 2026-09-28 [XPENG VLA 2.0 vs. Tesla FSD in Amsterdam — Part 1: XPENG L03](https://news.google.com/rss/articles/CBMimgFBVV95cUxQQnk0MEdBMmE1dFRENzBOcEU2SFlsRDRjVTdIT0JxWUxRdTktNVhBWUZneGxNcTE4bzlWZER5VjdSbFNvZmE5RVFRQm55OEJ0Nk1BNnIwemRTNkZ4Z1czQ3lJRGlOdnZPMEhWSHJQX0VSY3pza1NsTWJQSlJENWxVOWxwb05oaGZocVJZZ3pqdGZERF95ZkFOdzlR?oc=5) <sub>CleanTechnica</sub>
- 📰 2026-09-28 [VW confirms ID. Tiguan is coming, shows it in testing - ArenaEV](https://news.google.com/rss/articles/CBMikwFBVV95cUxOQ1JfZDNmSDJjbFBFbmF4ZVoxNldwaC05RUE0a0hGUUVFWHBrdzZSU0QxTTZEbUcyUk5lUUJMZDVZVHctLWJkMUU2aXp5Z2tnWU9Fb3pHZ2xTZXo4aDF2SXJFMjVPbEExRllFX2ZoMUIzM0U0ZVJBeGlSdVVTMVlzeDBjb3prMFdwNUtNSHhJZzJVSDDSAY8BQVVfeXFMTm1NWS0wYmY0N2FWMmM2bjR4VHlJSEZMUzZXdmNYN2ZaTklGSWVCRWNWUGdKdGNoWjB4aEkyMGxnV0g0TnNWTFl0eG1kTG92c2VmdWQ4SmIwR21HMS1aVy01cnBBQVc4QTJfWkNJdzhkN1dxdjcyQUtXNWNLTEFYMTQzZ3F0aS1JSnowQzFVSkE?oc=5) <sub>ArenaEV</sub>
- 📰 2026-09-28 [Nio Advances 3% as Geely Takes 30% Stake in Battery Swapping Unit; XPeng and Tesla Pull Back](https://news.google.com/rss/articles/CBMizgFBVV95cUxQQml3UlVqdnBQVWhvYk9fV1ZJeG9Jbk15VVViTm5kWEZGeHh1X3FqZzZuSGViTGdyZFJRYzk0RnphRmttS2c2RUktTVVfLWpaUmViMFlqWjZFd1dZelFna0liTGFoMll2ZjU1ejNwdVA2Z1h0aDc4M3JIZWhud2MxeHp0emlub1MwNHp6Y3pLTmR5d2hKNm1iU1FBNmpUSUtYQlpoYnVZYUpsd3Q3MzNmelFNd2s0LVE3Z3RVcjVWeWlqQlBNSkZMc3ZUVmNpQQ?oc=5) <sub>24/7 Wall St.</sub>
- 📰 2026-09-28 [Nio to Run Separate Swap Network for Geely’s Cao Cao Fleet and Robotaxis](https://news.google.com/rss/articles/CBMiqAFBVV95cUxOMmo2MlRKNUhSR0ZzaGJwRlNsN2hqNURaTUpfbWg3YV82V28tYXlrem1LZHFEYkFTZVNDTTR1VzA5RmxoX21VTTUxRjQzYXVyTE5Fem5Ua3Ziby1oVEk1RWJzaUtuTE85bDRmWUFQclVPOUtsYmZLX242WUgyc2l0UGREN3JzY0VYdFZNUnktSDFqVDBBUzZGV2c1eVRJRUlYNHJrNXM3eHk?oc=5) <sub>eletric-vehicles.com</sub>
- 📰 2026-09-28 [Xpeng Consolidates 4 Product Lines into 2 to Cut R&D Costs](https://news.google.com/rss/articles/CBMijgFBVV95cUxPeFR0NXZRd2VNaXowNUUwU1lqTEM1YUpUbVl6N3dVaFRoQmRGWWtSd0RUaW5KOVVtWTVuTUs1NXBLQzJQSENYY21kUlB0b3hYM3U5UmxwTElOWVRzNU9nN1ByeEpFekJvVElGNTlWZXg5dVBTR3I3Rm9na1h2dk0tRGtwVE1JUzlxSWp2UnhR?oc=5) <sub>Retail News Asia</sub>

</details>

<details><summary><b>Li Auto</b> (104)</summary>

- 📰 2026-09-28 [Nio Sells 30% Stake in Nio Power to Geely for US$2.4 Billion](https://news.google.com/rss/articles/CBMikAFBVV95cUxNMzNjY0pacHVwYi01dktrRzhydWRQVlF2Y0RIblBWdGV1eWU0UGdKaTdJU1ByWFhnUXozR2s2RlltejNuUWJTOTN3ZVNVZmZfbURaaEQ0R2Q4WWhGM1dJUFRoWUFPTldxWFhyYkw3Mlh3dVhfNzBrSEJRelloY0RHWm1BZEJlMGl4a3dlYkl0Ulg?oc=5) <sub>indexbox.io</sub>
- 📰 2026-09-28 [30万级家庭SUV终极横评：理想L8、领克900与神行者8，谁才是真正的“全场景担当”？](https://news.google.com/rss/articles/CBMickFVX3lxTE50dzNnWnAxRTZ6T0FqT0NWaEh3VUpENE9fakJkSUtTZU5tTXdTamRweWZFTkNETVR2RXpOX1FTWlI4Q0psWWQzLW1Hb2dDZlFfNlRFcEdnNEN4RGxBRmRra2tDUW1vRXI4dGRwUFF4RU9vZw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-28 [理想L9 Livis正式发布，售价55.98万](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBvbmZLcUJfYTd5V0Z2QWpxNE9jUDVHVmJiVU1OWkwwQXplYkF5NjFHOTZObTFKYmM0Mk41RFdFWDlsODBUbmlGUnY0UDlGallTcUNNNlY1UGtDWDg?oc=5) <sub>chejiahao.autohome.com.cn</sub>
- 📰 2026-09-28 [带激光雷达的豪华插混SUV哪款好？凯迪拉克全新XT5 PHEV与领克08激光版、腾势N9智驾横评+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFBHeTVURzE0UUJ5WEx3dWJyYldnR3dzaVczOW51TGt1VU5mYTVMamF1TmtXUzF3bnRGZXVRRGcwQzRaRHJZNnRQSFlPb3V6TnMtM1gySGdnNlhsd0ZHNVNPY0FueXFHOFZhdk51LW9GSWMzZw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-28 [30万级家庭SUV全能之争：理想L8、问界M7、神行者8谁更无界？](https://news.google.com/rss/articles/CBMickFVX3lxTE13bnR1Y0RmNGE4NDNqbW16dWxqaWgwWkNqaGVkRGRRcHdqdS14am9pd3FTeEpodExXY1JEZHJrZkx4dHZFeG51YU9QdXNFeXpTbTBmQkd3VDF5SHNQR1poV3pFdU1pWERLTjZQYm8ybkpnQQ?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>NIO</b> (103)</summary>

- 📰 2026-09-28 [长途自驾豪华SUV横评：理想L9、问界M8、蔚来ES8和神行者8，谁才是全场景旗舰？](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5DcGpMTWMtdnVrREVqSVRlTkRjeXFVU2pRdEtESjNibjYyNVhZWFkzbVFmQ0djZ1p4SXFYTUR6VlFZRTV5c2xrTXNfeDhFSTNXR3UyM2R5LUF4NFpIOS1v?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-28 [Nio Advances 3% as Geely Takes 30% Stake in Battery Swapping Unit; XPeng and Tesla Pull Back](https://news.google.com/rss/articles/CBMizgFBVV95cUxQQml3UlVqdnBQVWhvYk9fV1ZJeG9Jbk15VVViTm5kWEZGeHh1X3FqZzZuSGViTGdyZFJRYzk0RnphRmttS2c2RUktTVVfLWpaUmViMFlqWjZFd1dZelFna0liTGFoMll2ZjU1ejNwdVA2Z1h0aDc4M3JIZWhud2MxeHp0emlub1MwNHp6Y3pLTmR5d2hKNm1iU1FBNmpUSUtYQlpoYnVZYUpsd3Q3MzNmelFNd2s0LVE3Z3RVcjVWeWlqQlBNSkZMc3ZUVmNpQQ?oc=5) <sub>24/7 Wall St.</sub>
- 📰 2026-09-28 [Gasgoo Daily: NIO, Geely Partner on Charging & Swapping; Momenta, DSAT to co-develop ADAS; RoboSense, NVIDIA Deepen Physical AI Collaboration](https://news.google.com/rss/articles/CBMioAJBVV95cUxNMHhBOXZvVjBMSXBFTHpCS3pTOHNMRnFIa19lT1BTazVadE9pWmZrRlhzY1lQczBFVzQ5b0NUZzhHY09oSFZjR1pHYzQ4YTlndTlBOFVKYmp0SHcybjZ3cFhtRVRZSkNGYzRiM1NncFVOR21IOHVlU3pzRVJuQ1R4UWZaQUdQZkQxZElIVTlJX2swbzQ4TG15RGZEVG9BSXpUT09yZ2tNN1c3NkVaVXcybTNqWXdvdTIxQk5kNlowbUFoX29GZjNKMUR2R3IzRnF2NVpZendXZ2F2RnM4cHAtUDE2aElLczBRaDhlOXJyNVlhMDBCaFNWYWc3QTN2N1RRTll4U1BmWnpyWkR1bV9aRXJWcXRPR3NYaEhoM3oxX0Q?oc=5) <sub>Gasgoo</sub>
- 📰 2026-09-28 [NIO & Geely Joint Venture: Strategic Automotive Partnership for Next-Generation New Energy Vehicles](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1IM0tQdnRQUEhxMGtZZDZ2eWVWRnYzZjlLeV8wQ1RVemlIXzh1dVFOdUJRLThvaUJoVnI1ZXBqVjBQRmtsWHlMS0ZndVpoQ19FZ244?oc=5) <sub>36Kr</sub>
- 📰 2026-09-28 [蔚来插混前驱新款？别被误导！ES6/乐道L60安全智驾三电对比+FAQ](https://news.google.com/rss/articles/CBMifkFVX3lxTE5wMzdmRG5iUDdmM1JSbl95Sklfc0Z4M1RDTnAwSU1tMHgyNG1YWTQ4T0M3YXBPOXFnSS11SHhJc1gwdDZmS3RGdV9MZFc1aXZCQXdXV2ZMZkhPajR1dGZ6SEpTUWZzcHB4RnoyNmY0c0FfSVMtcXM3R3JCVnljUQ?oc=5) <sub>新浪财经</sub>

</details>

<details><summary><b>Huawei</b> (177)</summary>

- 📰 2026-09-29 [36Kr Exclusive: Ex-Huawei Noah's Ark Lab Generative Large Model Team Head Launches Home Embodied Intelligence Startup, Secures Over 1 Billion Yuan Financing In One Year](https://news.google.com/rss/articles/CBMiU0FVX3lxTE9hWHM0ckhIXzdnLWFrLU5TQkxNUDJJZ05BdE5xeWRoWV91Nkc1NHl6aDFHZmZmSzNqSWxrdGVPa2taUmtMOHBmZ1kydUNvU1ZVY0lR?oc=5) <sub>36Kr</sub>
- 📰 2026-09-29 [希望与车企达成双赢合作！靳玉志：华为智驾今年研发投入190亿元](https://news.google.com/rss/articles/CBMiWEFVX3lxTE1ZaWNKZ3JoRmlBN1B6WVl2eF90c1FNNnZQaXNhTmJ5dFhGRkJmMldMbS1ZYkk4TXUyVkNhRmJKMlVfNm5HLVh3TXZHUHI0akFtZFJPbDctV1g?oc=5) <sub>驱动之家</sub>
- 📰 2026-09-29 [闪电快讯 \| 鸿蒙智行智界RX以25.98万元起售价上市，享界V8开启预售](https://news.google.com/rss/articles/CBMiWEFVX3lxTE11YW9MZDFUNkxRY18zN2ZsUXVpb2VQR2RXcE9GbEpPTHN1dEhpZkFlbEJsdGdPNmc0aXltV3FZNnB4cFVRU3RIdnY2Ui1kLTYzcUJFakVQNXo?oc=5) <sub>Jiemian.com</sub>
- 📰 2026-09-29 [纵横G700焕新上市：华为智驾上车，价格诚意几何？](https://news.google.com/rss/articles/CBMijAFBVV95cUxOS05NNm1wY29RVkpqU2d3ZHJnWllmZ0k2MlpOMGJuZ2IzOUw0WmEzYWN2T29sRHUxWUJ4eXRLNXJaYWlKWU1CdDFLRmd2ZEYwN1lUaEJ6UzY4cEIzU0RYLUtucW5JcTJPQWkxMGFxb0JvaUF0U0IzUlhBQk16S1Rpbk81REt5UUJNYVNOZw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-29 [10万出头6座+L2全配，星海V6和阿尔法T5怎么选更香？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9RV0ZHVmtESjV6aHAtLWt0bmtKMUwwSXRJdGFYY1BJamoyNm1QSzkyWVZoS25jSXBKSHVnX0VaOU5udHBRUkN0b0F4RXlZdUN2OU1uSnpLZGFJUnc?oc=5) <sub>chejiahao.autohome.com.cn</sub>

</details>

<details><summary><b>Baidu Apollo</b> (38)</summary>

- 📰 2026-09-28 [Letter from Mideast: Chinese robotaxis help drive Dubai's smart mobility future](https://news.google.com/rss/articles/CBMifEFVX3lxTE5TX1h0MWVnUXVYOFREbGlRbm1faEw0LU1KQnlNZEE0OWs1QmZMZGs4VGluNmZlc1Bma2hRSlZ4RG82TWdkTzIzZXhQM0psajBRcTZXa3RWRzJoVWR4UWFVN1FtZXpMUDgzMFFkdEZydXk3QXNuTUZzb081RHI?oc=5) <sub>Xinhua</sub>
- 📰 2026-09-28 [Top 10 Best AI Companies In China 2026](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE93SnRFcUJ0WkdhS3o3eTRSN2ZPdmM5Yi0tLXZlWk4ycjF2OVMzc25DQ0hUcDZ6UF82bms0V2hvS0VNemh0a29lZzBvZzJGV2xPdUVMemxwRC1Wd0lvdzJreXU1NVhEVXM?oc=5) <sub>Nubia Magazine!</sub>
- 📰 2026-09-28 [逐一摸需求，5个项目落地！顺德把高校科研送进车间](https://news.google.com/rss/articles/CBMiUkFVX3lxTFA4TGJGRXhIRzNTNzB5T1RKa2tYcFR5VkNXWWI3ZjRqcGJOcXN5UEpIVFRleEhHY2o4cVJ0YnlsQjFBLVQxT1Zyd2FXM3l3V3poc3c?oc=5) <sub>南方网</sub>
- 📰 2026-09-27 [百度的萝卜快跑进军韩国，全球乘坐量超2000万人次](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9uanVCVFFmb25lTy1mMWs4T09kZFdSOWlFbUpxSm52c2U0VGxKNWxjNjh1cHJFY2Foc1IxUW9VU0VPSHhkYW9vaWttSndRMnVjZXVLeWVsSFVaNDA?oc=5) <sub>chejiahao.autohome.com.cn</sub>
- 📰 2026-09-26 [特斯拉Cybercab进入商业化运营，Robotaxi竞争转向运营效率与成本控制](https://news.google.com/rss/articles/CBMiVEFVX3lxTE5iYm1EU2d3RHV1dzE1ZmVWYnVlR01GR0dPZUdidERtdjAtLXlWZnFTUk94VTVMT0ZkMHV6bHl4bHJ3UHNNS0lRME55dUI4NENMZjVpaw?oc=5) <sub>虎嗅网</sub>

</details>

<details><summary><b>Pony.ai</b> (75)</summary>

- 📰 2026-09-28 [Letter from Mideast: Chinese robotaxis help drive Dubai's smart mobility future](https://news.google.com/rss/articles/CBMifEFVX3lxTE5TX1h0MWVnUXVYOFREbGlRbm1faEw0LU1KQnlNZEE0OWs1QmZMZGs4VGluNmZlc1Bma2hRSlZ4RG82TWdkTzIzZXhQM0psajBRcTZXa3RWRzJoVWR4UWFVN1FtZXpMUDgzMFFkdEZydXk3QXNuTUZzb081RHI?oc=5) <sub>Xinhua</sub>
- 📰 2026-09-28 [Zacks Investment Ideas feature highlights: Alibaba, Baidu, Kingsoft Cloud, Tencent, Hesai, Pony AI and WeRide](https://news.google.com/rss/articles/CBMiqAFBVV95cUxNaUJvc2NjRUdkd0tOQm9scVh0VXZsQm4zYVhkbEgtNndJcnlCc085S0dXbTQyNWFaSkhsUy13V3VBTkxnaXpyQU1SLVZSRHRuZm1WRWJVb0VPQXNxajdERnlmRWlUYVYwblg0N05qbXd5N2hGcjRpSjlWa1d4bkNldVlIRDhBU1BLRXlNQXFZYTN4U085bHFBOGMwTDVTTU1kRDEzc0lGdzU?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-09-28 [Tesla, WeRide and Pony.ai are already testing at Dubai’s new lab](https://news.google.com/rss/articles/CBMipgFBVV95cUxNb3BhYVRiMWRSQkxYN0hBM2xEMzBoaGhTeEZBVUZsekFlbEs3aDVPelZBeW9KaDlsS0wzS0l1Z2dOMlNtVGhhaTRDR2NCTVFpVWNISE41aFNzZ3RpSHFDQ0dOVXlMaTJwa3M4M0haMnRsdFlBMVBraEUzNW93Qlp6dlRlUnNEN21hUzd4NWdna3dtV0dIQjBkNjRHazdKR28tRUZXZzJR?oc=5) <sub>Absolute Geeks</sub>
- 📰 2026-09-28 [A mandatory tax-cover sale, not a discretionary trade: Pony AI (PONY) officer reports 15,524 ADS for sale.](https://news.google.com/rss/articles/CBMikgFBVV95cUxPWGswQk9sTnNNUFhudl9sdHdCY3JCaHBJZkt2VVVhR3FrSnJDZ2stYVp6ckExMGlNM3FoV2V4OTA3ejRUNjRuaXZKbzcxcTQwXzlOemx0Z01qaTFOS2lqdE9uM0JON3dOVjh5TmNDN2xfR19xMVFVc3V1VlhyQUZxSDh5cnBSVF9XZWNkREFjd2hfdw?oc=5) <sub>Stock Titan</sub>
- 📰 2026-09-28 [Pony AI Soars as Robotruck Breakthrough Ignites Rally](https://news.google.com/rss/articles/CBMilwFBVV95cUxNYlFRNnRNb2JjX1RMdXFmMjR0NVFHYVN2ejA2TXhzSVVVNHd0aUZXYWpuMV9FSUJWbWc0eFBESmVlWDR0cnJiYklWWDlTQWxjeXhCeDN4c3lEYWZqR2pHeHNPZVpfazhCaFJ6WUI5VkRrVDA1WE5naThaLV9fcmhFSjdtZU9oYXRLbGxvVDNmNUNHd3VYUHVJ?oc=5) <sub>TipRanks</sub>

</details>

<details><summary><b>WeRide</b> (71)</summary>

- 📰 2026-09-28 [Weekly Recap: H1 revenue +73% and fully driverless robotaxi service in UAE](https://news.google.com/rss/articles/CBMizgFBVV95cUxOY3pxX3lfWDN1Ri0xUTNKaHJ4ZFFPUUhaVGJNdG5hbWxrd1didHk4TXBMekc2OXVDQ01vdnZsN01sX1BqY05iNzdZVkcycDFOR01aY0ZZM216b0JCYVc2a0tEQmNjR0w2YlktdVNzQ3FCVnhZNkVjOHNHTGhUMlIwVnEycG1DbXRRVVBTeXhzbHVISXB5RHpwQ3g1SFdhX3o0cHVDdEFzbEx0ODFnZ2E1Wmlnd2hUUWpQWFlhSXpQc1lCdDZLcEZCaFlvOEtOQQ?oc=5) <sub>TradingView</sub>
- 📰 2026-09-28 [Tesla, WeRide and Pony.ai are already testing at Dubai’s new lab](https://news.google.com/rss/articles/CBMipgFBVV95cUxNb3BhYVRiMWRSQkxYN0hBM2xEMzBoaGhTeEZBVUZsekFlbEs3aDVPelZBeW9KaDlsS0wzS0l1Z2dOMlNtVGhhaTRDR2NCTVFpVWNISE41aFNzZ3RpSHFDQ0dOVXlMaTJwa3M4M0haMnRsdFlBMVBraEUzNW93Qlp6dlRlUnNEN21hUzd4NWdna3dtV0dIQjBkNjRHazdKR28tRUZXZzJR?oc=5) <sub>Absolute Geeks</sub>
- 📰 2026-09-28 [Letter from Mideast: Chinese robotaxis help drive Dubai's smart mobility future](https://news.google.com/rss/articles/CBMifEFVX3lxTE5TX1h0MWVnUXVYOFREbGlRbm1faEw0LU1KQnlNZEE0OWs1QmZMZGs4VGluNmZlc1Bma2hRSlZ4RG82TWdkTzIzZXhQM0psajBRcTZXa3RWRzJoVWR4UWFVN1FtZXpMUDgzMFFkdEZydXk3QXNuTUZzb081RHI?oc=5) <sub>Xinhua</sub>
- 📰 2026-09-28 [全新“方盒子”车型传祺越7上市](https://news.google.com/rss/articles/CBMigAFBVV95cUxNVlVjcWhEamtWYk1KZnRLTWFCZGY3TkVOMFg2OEpROGdIU2NWU1YxNk5CdlVVdENRanFkMU8yMzFyRWhHb012V0M4dWFGTm0wUjRDb0t4QXV5MW9TREFQNVc0UzltZzRPalNIWnB4TFpHVzdDZXVUWWZteDRjT1B1Mg?oc=5) <sub>经济参考报</sub>
- 📰 2026-09-28 [10万内就有激光雷达！这几款电车你确定不看看？](https://news.google.com/rss/articles/CBMiXkFVX3lxTFBrSkdjUHN0UVJ1bGFkUmdNNEZ5Uy05emMteVlJWmNETWxvX1JtSjUxU0xrY0U1bXZpSGExWHExNkhLeHlpck54VXZHRG42QjBaajAySHZGWENUVjV2OFE?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Horizon Robotics</b> (88)</summary>

- 💻 2026-09-24 [HorizonRobotics/CogWAM](https://github.com/HorizonRobotics/CogWAM) <sub>GitHub</sub>
- 📰 2026-09-29 [A safety camera using BlackBerry software was selected; production is projected at several million units.](https://news.google.com/rss/articles/CBMitAFBVV95cUxQODl1MUJydG04c0RYSXR5RExHMFluSVJtb3hjZXUxbjVOVWtUdDFTTHBmY1lZblFJR08wUVRoOHhqS0lwalVualpNRTZ2NFFXRG9JMFdrOUdQLV9EZHhuQVdJSDgwY05hYVRsejlueWF2bXdHOEV3S29MQmo2TVFOTlZtUGxxWXVPOGJYWmdBV1pnZTBjMExLMndrS0xROTc5QmJUaks4U2ZQTEtaUXk1MVpINms?oc=5) <sub>Stock Titan</sub>
- 📰 2026-09-29 [QNX and neueHCT Join Forces to Accelerate Global Intelligent Driving Deployment, Anchored by Major German Automaker Program Win](https://news.google.com/rss/articles/CBMi5AFBVV95cUxPcW5NS2FqTm9yNVV6ZDY5QURNaTBjcmVhQnMyRW84Y2o3Q1FBY2VhbndIbWppTVFicGhRd3lfLXZjNWNuOWtWX0RNbWczSV9LRmNiaktqS3FjZWtnQzF3UjhERWMtYXR2aEZxYVhmUFV3ejQwLUVXZ3E4LW1SM3dNWkNPTTJMSnhqSnN1b255enFldFJGX1EzdHRwMFp1NHkzeWlDajlienNCLVNaRDZLVWNzSG5sSWd0anMtczlzMUZWMjAzd3g5Q1NZWFNNS0w1ZWE3X2NaMlhvbmxwTjJJaHREYWs?oc=5) <sub>ACCESS Newswire</sub>
- 📰 2026-09-29 [地平线机器人中期营收破20亿，亏损扩大，市占率领先但增长空间有限](https://news.google.com/rss/articles/CBMiUkFVX3lxTE11aXEtSkFkbVVfYXppVHh3Q2NxOWtpN0Z3cHQ2U29ncmJ3aUxtdWs2c0h0NDkwUlJLaEkwaXgyNXFhX05OaFhZbWFFWFZKRjZSZ3c?oc=5) <sub>虎嗅网</sub>
- 📰 2026-09-29 [【视频】深蓝S05新款实测：FSD加持，操控下限能提多高？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE82RDMzb25acjI0VjVBUnE5RlhKeThVVmVQRTdhY0NMb3hBLUhGSzFKbDluVzgzRTg4RlBIaXp3SktVS0YyN3lXSDVGZG5oRklCQkF0X1pzdWFyczg?oc=5) <sub>chejiahao.autohome.com.cn</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (18)</summary>

- 📰 2026-09-28 [单飞后，半价“问界”来了！赛力斯官宣，新车9月28日发布！](https://news.google.com/rss/articles/CBMifkFVX3lxTE1pdjI1Q2h5Qjl4ckhIR0piVWdNYXdkc281bEM0VXBMUWYxM1VxUUg4ZXBMWDlZempiUkNFd0lsOG5wUkJTcWI5MkNTbUNoWnZzc2xwbW1ZSmlFWE9YclRMNjVNX0VHbVNaemkxZ1Z3bjg0QlFUelZUNTJZY2p4dw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-09-28 [Momenta与神龙科技签署全球战略合作协议](https://news.google.com/rss/articles/CBMiT0FVX3lxTE9XREQ4ZEJaWjc5UmJMQVVTYVctMS1wWUNBVUk1Mk9TWUFiZWtIM3l0ZEpxY2c2dW1LRm5CVkpNLTlqdDBzeXlNZ2ZfdjA5V28?oc=5) <sub>citnews.com.cn</sub>
- 📰 2026-09-28 [aiyouxi真人中国官网全新版本上线，打造极致数字娱乐体验- 体坛网_体坛+](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1BcWIzNW5ETDl4Q1c5Q2V1QkRVaDVUR2xPSEpxYmFyTnlqUDQ0ODkzQ3poUU1pWjJFTXA0N3VqNUZELUgwdldKSTg3REplcEItS193VTlXSUhMMGhHMmc?oc=5) <sub>体坛</sub>
- 📰 2026-09-28 [云鼎4008登录网站AI推理平台发布，本地化部署赋能体育产业智能化升级](https://news.google.com/rss/articles/CBMiSkFVX3lxTE1xaXFmUXlZOVA1Q2NmdnQxMlBOQ0RGNGdreDNSbEFhbllZVHRZODQ2MTNPekxNWi1lTjRJSU1LQ0VYSGxzczdPSU5B?oc=5) <sub>体坛</sub>
- 📰 2026-09-27 [k云体育中国官方全新升级：多模态AI生态正式发布，开启智能交互新纪元](https://news.google.com/rss/articles/CBMiU0FVX3lxTE5xUnRUdEVGdnhpQmtELV8zTzg2V19pTXJoUVVfQURQektBaHZnUDk2VGdXV1VQbTByX3Z3WW5sbXY4cGhUaXplN3Y1dmh6MVg4NFZr?oc=5) <sub>体坛加</sub>

</details>

<details><summary><b>Mobileye</b> (12)</summary>

- 📰 2026-09-28 [Germany: RMV, Deutsche Bahn and HOLON launch KIRA+ for Level 4 autonomous public transport in Rhine-Main region](https://news.google.com/rss/articles/CBMipAFBVV95cUxQVE41MUVYal9PVDQyMHc3TlpHNXhna1ItOGFrZVp0NjJyaVZzVzU5bkxFSmFrd0dNTl9BM1E4RzJybzY2Ml91SVMwdmJlV3lXdllyLUJBTTZWMEpMN0ZCU1U0QlhpUF9WcDFwV0w2ZmRXcTNDSmxxZ2stMW0xUzdRZXdYVkl6Zy15bFdKNEdXc1d3b1FmMTljQ1pYRVFWYzBnUS1Ucw?oc=5) <sub>Sustainable Bus</sub>
- 📰 2026-09-28 [Aurora CFO says 30,000 driverless trucks by 2030 isn’t as far-fetched as it sounds](https://news.google.com/rss/articles/CBMitgFBVV95cUxOOHZmNEZELWs1TXRlV1hHQ2tzMVp1X0FGaWtSQXVMSDF5ZXJ3MnJ1MTVIckFPanA1bS1iMHFnTUxRdlNaVEVReV9XLXdjY0NxQ3p5ZVY5cV9HcF9tYUZ3bnFNbHZNMWFWZGxKSlZSYWdwRG0wM3FQMDhFU1hTZTgzZnNmd01xQUZhRTl0c3RqNVZQU3pjYlZNRUxFNWVYYU1iTGhqZnB6M0lIZE1YM2EtQWt3SEZ1dw?oc=5) <sub>TechCrunch</sub>
- 📰 2026-09-28 [Can NIO's Geely Alliance Drive Battery-Swapping Adoption?](https://news.google.com/rss/articles/CBMisgFBVV95cUxQLW5zM3paYXpzenJuMTBXbENBWUZ2NHBFQmNYZDFSX1NJUjlFQWNjeXBwdGl3WFhiNEloUGR3UmtyZHJFYU5OeFprS3RMT1kxMkVyWG5qeVJHbzNZMUFPeVpfYmp6Uk8yRUQwOHk5dkdUMkNJNjZNMk5BT3M0ME5DOE1zd3NNMXV3Y1NyTmRIQUtZSzRQYUhqTm9teU45bEU4WGIwVldTWk5hUjJHdXp1Z1dB?oc=5) <sub>TradingView</sub>
- 📰 2026-09-28 [Handing Over the Wheel: Tesla FSD's Thirteen-Year Journey of Risk, Controversy, and Evolution｜硅谷101](https://news.google.com/rss/articles/CBMiX0FVX3lxTE10T2lRa3hkY3QzLUZueFlxRFQzeThoM1Utai1SS3k2WFMtalM4bWYybXpyQ1hiSWJMZW9DbXB0c2pVRE5ZenJ6NmRtY3dNazVKc080NFRJMzdQcUp6eDVJ?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-09-28 [Kerry Liu Xiangke: Tesla's AI5 Chip Lead Concealed Progress for a Year—Musk Personally Sent Blueprints to TSMC Before the Truth Came Out](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5lekRXS2d6V1J3ZE1kQURJNm4tTG9XRmRxQ1ZhQi1JVzFwVTBoekU4c0VVb0k0bllJeHZJbDhfTzYxRUVjbFVUOFBvdFRzTUh1dFJDOE5KSDRYdXM?oc=5) <sub>finance.biggo.com</sub>

</details>

<details><summary><b>Aurora</b> (32)</summary>

- 📰 2026-09-28 [Aurora CFO says 30,000 driverless trucks by 2030 isn’t as far-fetched as it sounds](https://news.google.com/rss/articles/CBMitgFBVV95cUxOOHZmNEZELWs1TXRlV1hHQ2tzMVp1X0FGaWtSQXVMSDF5ZXJ3MnJ1MTVIckFPanA1bS1iMHFnTUxRdlNaVEVReV9XLXdjY0NxQ3p5ZVY5cV9HcF9tYUZ3bnFNbHZNMWFWZGxKSlZSYWdwRG0wM3FQMDhFU1hTZTgzZnNmd01xQUZhRTl0c3RqNVZQU3pjYlZNRUxFNWVYYU1iTGhqZnB6M0lIZE1YM2EtQWt3SEZ1dw?oc=5) <sub>TechCrunch</sub>
- 📰 2026-09-28 [Aurora targets 30,000 trucks by 2030 via asset-light option](https://news.google.com/rss/articles/CBMiYkFVX3lxTE1ybm9lejV3R3JwZDA0eDVVVjNwcTZqemRTQ2xQQXJrcXp2d01zZS1UWTRLbk4xRkNfVHV6UTNxbFhHVnFLMFFLZkJvQlR3cS1tbG9ranVmdGIxOUQtNDlxYzJR?oc=5) <sub>Transport Topics</sub>
- 📰 2026-09-28 [Aurora plans 30,000 self-driving trucks on roads by 2030, targeting $5B revenue despite current small scale.](https://news.google.com/rss/articles/CBMioAFBVV95cUxNck5hOENGbDFCc3BLLUNBS3VqRmZBb3ZkZUhKT000NlVBYzRxTEdLNGEwOFM1dFdSbk5wdXB4ODF6Y2FpR213U3ItY1BjSWlmbkIwcTdFa1JpRnJNM3hjX191Y2phSjYtaUNIOWZIbGd5ZXlhVzJ5amEyUDFrWHkxRWUxVW1tTUpxTEZtWGNkOTBHQTYwRnlrcUxVYk15bXZ5?oc=5) <sub>Pluang</sub>
- 📰 2026-09-27 [Aurora Innovation’s Road to Profitability Runs Through Fleet Expansion](https://news.google.com/rss/articles/CBMiuwFBVV95cUxOMGZqV0c1ZXlBY2VoanlHVEdycEFQQVBqYktmV01tMGM5c3lPT2Ntb0Q5TndWTlk1dUtOSzEteHhJWWI4RFY2YnBwbEduQ3RqUXVrdTFoUTZzd2xQZXViQmxLWnFicjhmUTJIRTBsamxnUVZtZDdzOVhycm0tM3NCX2xYMmE1M1ZCWlJoZXVpd095cHc2M21uVmM2empyVUcwMkdvejNMNXRFbDVvNnRRNkRoZkJzZGdGaEp30gG7AUFVX3lxTE4wZmpXRzVleUFjZWhqeUdUR3JwQVBBUGpiS2ZXTW0wYzlzeU9PY21vRDlOd1ZOWTV1S05LMS14eElZYjhEVjZicHBsR25DdGpRdWt1MWhRNnN3bFBldWJCbEtacWJyOGZRMkhFMGxqbGdRVm1kN3M5WHJybS0zc0JfbFgyYTUzVkJaUmhldWl3T3lwdzYzbW5WYzZ6anJVRzAyR296M0w1dEVsNW82dFE2RGhmQnNkZ0ZoSnc?oc=5) <sub>Insider Monkey</sub>
- 📰 2026-09-27 [Autonomous & Self-Driving Vehicles News: Waymo, ComEd, TIER IV, Einride, Hyundai, AEye, Witherite, Aurora, NHTSA, Volvo & Arbe Robotics \| auto connected car news](https://news.google.com/rss/articles/CBMi9gFBVV95cUxPXzN2cFVQendmTl9ma0N5YzVwbkJRZ0ZneTdESG1VeTduazdQVzN6MXJwWmt2UlZYZDh2WkVZLU10TFphRnhVRGNidU5yU1p4dFhLTlR3Ukk3S1VSQkVqd0pkYXhNZ2RyZHp3SXpJNW14NVhORWl2WE9CVm9QSDN6aXJjS1Brdjd3ZEw3ODczM1ItVVlidXJ2TmFPbW1OZ08xZnozd2hKbWNZdmpTS1lLZVB0ZjdlSzlQa3VKVGFsQ2ZUeXVaWVZWNW5SaDh4NzVrZVZROVFmMkVwVUVqbXp0ZTlBOEpnYVdWMEdNYUFZdWQzS2k5SkE?oc=5) <sub>AUTO Connected Car News</sub>

</details>

<details><summary><b>Zoox</b> (57)</summary>

- 📰 2026-09-28 [Aurora CFO says 30,000 driverless trucks by 2030 isn’t as far-fetched as it sounds](https://news.google.com/rss/articles/CBMitgFBVV95cUxOOHZmNEZELWs1TXRlV1hHQ2tzMVp1X0FGaWtSQXVMSDF5ZXJ3MnJ1MTVIckFPanA1bS1iMHFnTUxRdlNaVEVReV9XLXdjY0NxQ3p5ZVY5cV9HcF9tYUZ3bnFNbHZNMWFWZGxKSlZSYWdwRG0wM3FQMDhFU1hTZTgzZnNmd01xQUZhRTl0c3RqNVZQU3pjYlZNRUxFNWVYYU1iTGhqZnB6M0lIZE1YM2EtQWt3SEZ1dw?oc=5) <sub>TechCrunch</sub>
- 📰 2026-09-28 [Waymo, Uber, Lyft Hit Gas On Robotaxi Real Estate Expansion](https://news.google.com/rss/articles/CBMizgFBVV95cUxPR3QwUkxkbUVIMDRlaEZ3cU04bTZsY0NpdE5TYXJpSWtQQ0N5X3ZUa0E2dkdtSzgwNjVsVlI1NGJ2bEdkckJxUU1nTy1QOHlLMzNBbGhNUVZVQjFEbklRYnhyMjM0Y2loTFhRbjU4OWZHdGkyVjJ2RzJGRVhVbk5wSmRjTW40LU5jMHliZTZ1NVctUlNodnVudjRLeThxdTdhaERBak1WdVZCajVhSllDVWhYQmNMWVYxT2xWZFFoeEx3c1JLckduMy0tOF9LZw?oc=5) <sub>Bisnow</sub>
- 📰 2026-09-28 [Commercial Vehicle Group Q2FY26 Results: Revenue up 13.5% to $195.2 million](https://news.google.com/rss/articles/CBMixAFBVV95cUxNT3lLeG1jSER6aGo3cGxoaHNteHBqajJLQ19MZ2xIODlXRlFaRURqb2oydHpORTFYQUlTYndBTkgwaUNIclhlMDhQeEJzYmdXb1dGNlR6d0N0bEJMNmFMdzNGT3BnUzJsNTVEd0w3Qi1CTVE4dkxDc1RCRjJHS3FoWDl6VUJydHo1U3duQXFqUmszUWJVczZWMDRSNHBhTVlBVGFleUJUS2lLRHFIbEJuN01MYm02d0djUHNBMU9KWGM3cUtX?oc=5) <sub>scanx.trade</sub>
- 📰 2026-09-28 [Tesla Heads to Trial in California. Should Investors Be Worried?](https://news.google.com/rss/articles/CBMikAFBVV95cUxOM05JdEhaajd4cWYtM3RRVnVDNTVMV0NnVTJweUMtY0taeC1WT25QNm8wRF9vZEZRQUJKTFc0bDFBNHd1S1R0T0psUVFhblBJN25aa2UweWNEN0tNSERYLVpuYlpBWWNycm5yZndKRHFFamg3OXVWNHk1VE5VZU5mcVQyaG5lckdQQ051dS1zQW8?oc=5) <sub>Yahoo Finance UK</sub>
- 📰 2026-09-28 [Tesla delays Roadster 2 event again due to bad weather](https://news.google.com/rss/articles/CBMikwFBVV95cUxOZ2dSOEVCMWJ4aFUxS3FsZ1Q1dVFjZlNiUjRHVWhKR2JXMFVxakdTWmVrcHlJYTBpZHNoRkQ0RTNOel92eFYtTWVyMUlibFpzdGhzNlBwR0QxYm9Ob2NLdTRFZm05bnlQdmZUQzhxVmNqbkRxRW95djFyd2RJaFdaN3dBYkRRQjRwSnVHTEFoUWh4NEE?oc=5) <sub>TechCrunch</sub>

</details>

<details><summary><b>Motional</b> (8)</summary>

- 📰 2026-09-29 [Hyundai Motor touts physical AI vision, courts global tech talent in U.S. - CHOSUNBIZ](https://news.google.com/rss/articles/CBMiggFBVV95cUxQNWZDY3F6Mk9mMGRIT2lWdnlVZmhib3FBbktkRG56al9PdTZwWUVTUTZ1ZnNvT1ZLTzA5N3NFa3dFZGRSWUNGTTFJX09pVVZRTFM2NVU4WHM3YjMyYjBaM1Z5Z0NmZjV2M0NXdzdIWHZvTzNLclg0OVM1MGNXcGpSb1ln0gGWAUFVX3lxTE9BYlRHQ3hoMEZlNE1CYV9VdXhUYk5jRHQ2N1gwZUdnUnA3elhNRm9ZRUdVSjAwZkVKLWt5WTRobkxMdUVNNXVISjhkU2ZjQ3AyU0RfUG5ZRHQ2OXZSYXh3cGJHaVhxT1p2djU4cnU4NFg5TXBKaUxTWThYNmN1X3NjLTFBSTB3WGlRM2pPVFNfSGNFaHRyUQ?oc=5) <sub>Chosunbiz</sub>
- 📰 2026-09-29 [Hyundai Motor Group Completes Tech Talent Forum for Global Top-Tier Technical Talent](https://news.google.com/rss/articles/CBMigwFBVV95cUxNYWttY2laenc2bk0tT21JVVViMk9SN1RZSWNuMkdrSWUzSlB3ZVM5UjZtVDlBUlM0VFZMd0JHdVA1LVhqUXBXcU1vczF3eTVibDg5X0F3eHBpaV9mRHBRZjlnRzh5ZkowMTRpZ2pDZmhHZW1jUzJSZndDV3BUbFBFdXRQZw?oc=5) <sub>starnewskorea.com</sub>
- 📰 2026-09-28 [Hyundai Motor Group Hosts 'HMG Tech Talent Forum'...Bringing Together Technology Talent and Key Leaders](https://news.google.com/rss/articles/CBMic0FVX3lxTE1vc2FpeFVIbjF2MWwwTFI0ZDFhYjAxU1d1bF9uWk5iSkdTc2xPTjVxOWxldVhEVkN5WGx3ZXljN2FOTVJGdVN3VjVWdDFCTVlfRTlyR2ZQeUc5cmFBYUozZ0trQURnanBQdUVvbHZrQldHd28?oc=5) <sub>아시아경제</sub>
- 📰 2026-09-26 [The Robotaxi Reality Check You Won't Get From an Investor Deck｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1oVm5UbjMzU3RzeTlQUTNNQkkzdUUxMWFzalpCZlJIMGdKQWx5ZVo4eU1mQW9MWWxEdlFZSjlpUHRXMDRQd19uRkRVcWRCNmxEd2JraF9nVC1zd0ZDRDBj?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-09-26 [Walter Piecyk and Grayson Brulte: The Robotaxi Bottleneck Is Depots, Not Software](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBlREZaMnNLXzJxMGdBNUQ0S0Y1VGxGb0NqVWJtZVpfOGl2SW9pZnNhRFpacjVLUUdFOG10S0ozWHFVazVveWkxQUt3dnNNeFlyU1BiVlNTNjlreWs?oc=5) <sub>finance.biggo.com</sub>

</details>

<details><summary><b>comma.ai</b> (39)</summary>

- 📝 2026-09-16 [Bugs that broke driving: Machine Learning edition](https://blog.comma.ai/ml-bugs/) <sub>official blog</sub>
- 💻 2026-09-15 [commaai/comma_hack_7 — some chestnut examples](https://github.com/commaai/comma_hack_7) <sub>GitHub</sub>
- 📰 2026-09-28 [NHTSA Investigates Comma.ai Driver-Assistance System After 5 Crashes and 3 Deaths](https://news.google.com/rss/articles/CBMihAFBVV95cUxNX0xVMkNFUnVtYXBHZUhMYl84bklrSGxGLXZ2b290WjNVVU1rSXJ1VWF4Z3hpY0NaY1VWekUyTl9Dd1VDUFc2dzhtT2tyR1BLTmI3UE9rUy1PendUM0FmTF91U1pUekRjZ2FjTGMyTWZfNGluMVBWazZBNFRWLXlRQ3czV1M?oc=5) <sub>AOL.com</sub>
- 📰 2026-09-27 [Autonomous & Self-Driving Vehicles News: Waymo, ComEd, TIER IV, Einride, Hyundai, AEye, Witherite, Aurora, NHTSA, Volvo & Arbe Robotics \| auto connected car news](https://news.google.com/rss/articles/CBMi9gFBVV95cUxPXzN2cFVQendmTl9ma0N5YzVwbkJRZ0ZneTdESG1VeTduazdQVzN6MXJwWmt2UlZYZDh2WkVZLU10TFphRnhVRGNidU5yU1p4dFhLTlR3Ukk3S1VSQkVqd0pkYXhNZ2RyZHp3SXpJNW14NVhORWl2WE9CVm9QSDN6aXJjS1Brdjd3ZEw3ODczM1ItVVlidXJ2TmFPbW1OZ08xZnozd2hKbWNZdmpTS1lLZVB0ZjdlSzlQa3VKVGFsQ2ZUeXVaWVZWNW5SaDh4NzVrZVZROVFmMkVwVUVqbXp0ZTlBOEpnYVdWMEdNYUFZdWQzS2k5SkE?oc=5) <sub>AUTO Connected Car News</sub>
- 📰 2026-09-26 [Only 15 Minutes, Riau Researchers Offer a Way to Get Water to Put Out Peat](https://news.google.com/rss/articles/CBMiQkFVX3lxTFA2aTZXWGtxRHBaczVwMFBwRENsMHpBQ292MVBzMEpHbF8wTXpjekdqeElmVnM1a2VVWEN0YUZPZGM4dw?oc=5) <sub>VOI.ID</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
