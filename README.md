# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-10-03 · 1,231 papers tracked · 36 curated.

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
- [3DGS / NeRF Reconstruction & Sensor Sim](#3dgs--nerf-reconstruction--sensor-sim) (2)
- [Perception: BEV, Occupancy, 3D Detection, Mapping](#perception-bev-occupancy-3d-detection-mapping) (8)
- [Datasets & Benchmarks](#datasets--benchmarks) (3)
- [Safety, Robustness & Evaluation](#safety-robustness--evaluation) (3)
- [Industry Tracker](#-industry-tracker)

## VLA / VLM for Driving

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Teaching Vision-Language-Action Models What to See and Where to Look](https://arxiv.org/abs/2607.01658)<br><sub>Yuguang Yang, Canyu Chen, Zhewen Tan et al.</sub> | ECCV 2026<br>2026-07<br>📑 1 | [⭐ 30](https://github.com/ShivaTeam/DriveTeach-VLA) | Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving |
| [DeepSight: Long-Horizon World Modeling via Latent States Prediction for End-to-End Autonomous Driving](https://arxiv.org/abs/2605.10564)<br><sub>Lingjun Zhang, Changjie Wu, Linzhe Shi et al.</sub> | ICML 2026<br>2026-05<br>📑 1 | [⭐ 31](https://github.com/hotdogcheesewhite/DeepSight) | End-to-end autonomous driving systems are increasingly integrating Vision-Language Model (VLM) architectures, incorporating text reasoning or visual reasoning to enhance the robustness and accuracy of driving decisions |
| [CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving](https://arxiv.org/abs/2607.04179)<br><sub>Zhaohong Liu, Hao Ye, Xianlin Zhang et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 1](https://github.com/MICLAB-BUPT/CritiqueDriveVLM) | End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving |
| [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)<br><sub>Nan Yang, Zhanwen Liu, Linfeng Zhang et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 3](https://github.com/Zizzzzzzz/MVPruner) | Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings |
| [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)<br><sub>Yuan Gao, Wenting Miao, Mattia Piccinini et al.</sub> | IROS<br>2026-07<br>📑 1 | [⭐ 27](https://github.com/TUM-AVS/Chat2scenic) | Validating autonomous driving systems requires diverse, regulation-compliant test scenarios |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 6 | [⭐ 482](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
| [Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air](https://arxiv.org/abs/2605.31066)<br><sub>Tianle Zeng, Yanci Wen, Xueang Yu et al.</sub> | arXiv<br>2026-05<br>📑 2 | [⭐ 1,105](https://github.com/louiszengCN/CarlaAir) | Recent aerial vision-language-action (VLA) models show promising single-UAV capabilities, such as tracking moving objects and navigating to language-specified landmarks |

## World Models & Generative Simulation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [HERMES++: Toward a Unified Driving World Model for 3D Scene Understanding and Generation](https://arxiv.org/abs/2604.28196)<br><sub>Xin Zhou, Dingkang Liang, Xiwu Chen et al.</sub> | ICCV 2025<br>2026-04<br>📑 4 | [⭐ 71](https://github.com/H-EmbodVis/HERMESV2) | Driving world models serve as a pivotal technology for autonomous driving by simulating environmental dynamics |
| [FrozenDrive: Zero-Shot Text-Guided Driving Scene Generation and Data Augmentation with Parameter-Free Frozen Diffusion Model](https://arxiv.org/abs/2606.20110)<br><sub>Yuhwan Jeong, Hyeonseong Kim, Daehyun We et al.</sub> | ECCV 2026<br>2026-06<br>📑 1 | [⭐ 10](https://github.com/daehyunwe/FrozenDrive) | Synthetic data for autonomous driving is surging, powered by diffusion models that promise scalable scene generation |
| [ASTAD: Asymmetric Style Transfer for Synthetic-to-Real Adaptation in Autonomous Driving](https://arxiv.org/abs/2606.29286)<br><sub>Dingyi Yao, Xinqi Zhang, Lihui Peng et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 1](https://github.com/Dingyi-Yao/ASTAD) | Synthetic data mitigates the data scarcity problem in autonomous driving perception |
| [Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends](https://arxiv.org/abs/2606.01164)<br><sub>Jiuming Liu, Chaojun Ni, Mengmeng Liu et al.</sub> | arXiv<br>2026-06<br>📑 4 | [⭐ 237](https://github.com/liujiuming123/Awesome-Interactive-World-Model) | With rapid development of large language models and diffusion-based content generation, world modeling has attracted increasing research attention, benefiting various downstream domains such as game engines, embodied AI,… |
| [Is Your Driving World Model an All-Around Player?](https://arxiv.org/abs/2605.10858)<br><sub>Lingdong Kong, Ao Liang, Tianyi Yan et al.</sub> | arXiv<br>2026-05<br>📑 4 | [⭐ 253](https://github.com/worldbench/WorldLens) | Today's driving world models can generate remarkably realistic dash-cam videos, yet no single model excels universally |

## End-to-End Driving & Planning

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](https://arxiv.org/abs/2609.26792)<br><sub>Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.</sub> | CoRL 2026<br>2026-09<br>📑 1 | [⭐ 10](https://github.com/VAIL-UCLA/DreamStream) | Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions |
| [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)<br><sub>Shen Zheng, Anurag Ghosh, Gaurav Parmar et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 31](https://github.com/ShenZheng2000/WarpI2I) | Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs) |
| [G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance](https://arxiv.org/abs/2606.26017)<br><sub>Hang Yu, Ye Jin, Alessandro Canevaro et al.</sub> | IROS 2026<br>2026-06<br>📑 4 | [⭐ 6](https://github.com/HangYuu/G2DP) | In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors |
| [Fail2Drive: Benchmarking Closed-Loop Driving Generalization](https://arxiv.org/abs/2604.08535)<br><sub>Simon Gerstenecker, Andreas Geiger, Katrin Renz</sub> | arXiv<br>2026-04<br>📑 15 | [⭐ 173](https://github.com/autonomousvision/fail2drive) | Generalization under distribution shift remains a central bottleneck for closed-loop autonomous driving |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 14 | [⭐ 344](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
| [Latent-Centroid Steering: Single-Pass Classifier-Free Guidance for Command-Aligned Autonomous Driving](https://arxiv.org/abs/2608.00237)<br><sub>Meibo Hu, Jiamian Wang, Pichao Wang et al.</sub> | IROS 2026<br>2026-08 | [⭐ 2](https://github.com/codingmlinprocess/LCS) | Vision-language models (VLMs) have recently emerged as a promising paradigm for end-to-end autonomous driving, enabling agents to map multimodal inputs and high-level navigation instructions directly to executable trajec… |
| [STAGE: STyle-controllable Action GEneration for personalized autonomous driving](https://arxiv.org/abs/2607.29517)<br><sub>Zihao Liu, Xing Liu, Yizhai Zhang et al.</sub> | RA-L<br>2026-07<br>📑 1 | [⭐ 6](https://github.com/CarlDegio/STAGE) | Driving style refers to the behavioral preferences that drivers maintain during driving, shaped by their diverse experiences, habits, and needs, and is typically reflected in varying levels of aggressiveness |
| [DVGT-2: Vision-Geometry-Action Model for Autonomous Driving at Scale](https://arxiv.org/abs/2604.00813)<br><sub>Sicheng Zuo, Zixun Xie, Wenzhao Zheng et al.</sub> | arXiv<br>2026-04<br>📑 11 | [⭐ 363](https://github.com/wzzheng/DVGT) | End-to-end autonomous driving has evolved from the conventional paradigm based on sparse perception into vision-language-action (VLA) models, which focus on learning language descriptions as an auxiliary task to facilita… |

## 3DGS / NeRF Reconstruction & Sensor Sim

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DriveWeaver: Point-Conditioned Video Inpainting for Controllable Vehicle Insertion in Autonomous Driving Simulation](https://arxiv.org/abs/2606.31918)<br><sub>Junzhe Jiang, Zipei Ma, Zijie Pan et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 16](https://github.com/LogosRoboticsGroup/DriveWeaver) | A pivotal step in autonomous driving simulation involves inserting foreground vehicles with predefined trajectories into simulated scenes |
| [Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796)<br><sub>Leshu Li, Jie Peng, Yang Zhao</sub> | ICRA<br>2026-06 | [⭐ 12](https://github.com/UMN-ZhaoLab/Pocket-SLAM) | 3D Gaussian Splatting (3DGS) has garnered significant attention in Simultaneous Localization and Mapping (SLAM) due to its advances in capturing fine-grained geometry features and synthesizing novel views |

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

<details><summary><b>Waymo</b> (160)</summary>

- 📝 2026-09-24 [Our Vision for London: How Waymo can Support a Safer, Connected UK Capital](https://waymo.com/blog/2026/09/visionforlondon) <sub>official blog</sub>
- 📝 2026-09-22 [Introducing transit rewards](https://waymo.com/blog/2026/09/transit-rewards) <sub>official blog</sub>
- 📰 2026-10-03 [Blue state councilman mocked after claiming self-driving cars are 'murdering' pets: 'Hide your cats'](https://news.google.com/rss/articles/CBMiugFBVV95cUxNX1E4WEVrR2Z3RFlNR0RxRUVsbVZ3QzdsVEdiM3JNak9SaWswLU1GX1lEamlON0pWd196eDMwRlB1eGx6b1pZU3V4dWRxNV8wbGdTN29BeXJQLXotZmVjRlFKTGFvUmIxSmlRVl9VVkptSlhqbDJXazlTbXpZb29WWk5TQjZpTHRKOC1GSmZrLUNpLTN2MC1yYXRjQUhoem5yM1Uzd0w3eFJLRmhBc3M3WWhUbjZUbENXc0HSAb8BQVVfeXFMT3pPSWY3blF0UXRleDJPMWNhNTBFeWZLN1p0UXAtbGRoaUthNnFUdVZPRGtkWDRsNWhIQktwVEZTSlk2OWtmbjV4Ry0zNzZ2Y2xvTTlwNUlvYTdpcTY3UlBXQ281UDBfRzBEUHBNSGRoMHdZdzlReDdSOU9JbVU4UXh4V0hVTkk0ZGJMeGtrU3A0cFcyckluOWs3ek9fR190d2c5RE9tRkQ1U0R3Zk04TlpfdVBpZTVkUVZ3WXdvUlE?oc=5) <sub>Fox News</sub>
- 📰 2026-10-03 [Minneapolis mayor, city council members clash over driverless robotaxis](https://news.google.com/rss/articles/CBMi4AFBVV95cUxNWmdzTWJOS3FIQWVJT0RPSWtrdUN0LVY3UktlcXRYUkpGc1NyZHZfLU9vNi1XcW80YUxyTV8xVU4yeEhHblpLdjlhX1UwSDFMaUhwN3RFeHVZc0VuNmVFVUUydkpCbDEwQ2ZNOFJoYjNEcXlCOWVkMGx0T1F1ODFBbHliQ1FqMXhtZ19xRmNTN2VrRy1ZOTl1bHlqVzIxOU9rMG9qOE1haE5BdXdLT3hhNDRuMkgweW5mUWNKaGFMbWV5b3U2QjlyYlBPV0ZwcTlmbTVaWHktZmd0aXA5WjlocQ?oc=5) <sub>kare11.com</sub>
- 📰 2026-10-02 [DATA: Robotaxis in Phoenix have the lowest crash rate among major US cities](https://news.google.com/rss/articles/CBMisgFBVV95cUxNTmlhZlhieUFJM2IxMFhGRFMxZFJXWlVndXRULTg1LTltSVd5Y1F6LWJXY1BrODNhbG1qUXk4cUc4XzBVY0Exal8xRkRwU2ZpclotVGNmUmNTQjN2cHdmT2FlelhWb0Jma1dXX2Jhd0cxZXowOEVpcjBqdmNWeHd2RC1GVkNYTGNuUHN2VVQyYUZJdURoM1gxdTdZczFZcUZ5N0lmQnRxU0pOb1l1VUFnZ01B?oc=5) <sub>ABC15 Arizona</sub>

</details>

<details><summary><b>Tesla</b> (247)</summary>

- 📰 2026-10-03 [Musk says pet safety behind Robotaxi nighttime limits](https://news.google.com/rss/articles/CBMinwFBVV95cUxNalVWeGtnNnFINnFiZ05qYzdOOUc1aWwwWmticHVyb0VKUTBCNjhxbk44OTNwS0tEUDExWVgtQnJiNXRGLV9EeVJtdkpRZkJIajE2cEpCcW9oZW1BODRMNDJMNGI4d1JrMW85WE53NXJEbEdvQlR0bnBWTVZ4M2lzbEZOY1RfV1J2LWdaMUFranlxelc3MXdpUGJvRXRTYUk?oc=5) <sub>breakingthenews.net</sub>
- 📰 2026-10-03 [特斯拉三季度交付超48.6万辆，超市场预期；销量已连续两年下滑，股价较去年底高点下跌25%](https://news.google.com/rss/articles/CBMijAFBVV95cUxOT0pjZk9yNjkyWW0xZEdVM2NTQi1MUFJ2VDBOd2ZBbVhSQ18xZjh5S1J6YVBFUmdRc3BqaHh1MDgtRTBLOS02QmhIZl9xZTE0dmp2YXAwOHRNNXJoOW9IcDFlWlRfMkhtcFNRX1h0dUlxZ0FOUm5KVmNiazRyUEtoRHR6SktLMEk3U2xVYQ?oc=5) <sub>搜狐网</sub>
- 📰 2026-10-02 [Tesla Cybercab Fleet Hits 158 in Texas: Your Questions Answered](https://news.google.com/rss/articles/CBMingFBVV95cUxQcU02TkNDVnI2N3hWNHAtTlVBcjNUVWRBSmRScDhUaTdqVjdZRW95Xy0tTk9XWm5vWFBxNW42clY4Tk43MzdoRFhqZkhMbzBqOUxDcFRFYW1kZ1NhRUpsb0tUTkx2NnNnM2RTRmNhcDlSalpmVzJxd0swOUIwV1piTEdJX2VHc2xYWmFJd0ljcmJDemVZMlZzanloWEJXdw?oc=5) <sub>BASENOR</sub>
- 📰 2026-10-02 [Belgian test finds Tesla FSD sped through 20 mph zones, tried illegal cyclist passes](https://news.google.com/rss/articles/CBMioAFBVV95cUxNTVZBYlQtek9jRlQ2c2ROU1JHdlZMTlgxSmZVbVl0a0wyY0s0c1FCcUxEYm5WeE5JeDBfMlRNVDAwQ3Y5U3hUUUhEYUZiSGtVUDNieDB1ZXVCZ0JvVWZWWndtdTVZdG5kS0k2UVh4SC1SbmxuZ1VJbFBzaGlzTVJuaXdtUXZmRWJuTzVPbTdhTzB4SFgxLTNiSWx5YjdlZ2Vt?oc=5) <sub>Yahoo Autos</sub>
- 📰 2026-10-02 [【视频】广州雨夜“狂飙” 特斯拉FSD V14实战一镜到底](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5lWUpDeGhqY3I1VzAtaTZ5T0RDcGo5YTJsOHVhWl9oRVhtSll6bmhvcHJ4VFpvVENlVXNDVUFHM3oxYnQ2TDlTbWNkaFFYVWxkMHRWQlFHMDJSM1U?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>NVIDIA</b> (164)</summary>

- 📰 2026-10-03 [Nvidia patched 114 GPU driver flaws on September 30, and one is rated 9.9](https://news.google.com/rss/articles/CBMikgFBVV95cUxQUEVjZnQ2dkFQcjlZVVJuVE93NGJYQ0tqaDI2TTBBVXg0Zm55c0RzMDFwRWRWT2JtN0xyN0J3dXdvcHpoX1d1TlBRWkJLRU1uOVFzTHAxS2FHV1RuZmZ6cDM4REUtZUx6NF9xU3hYTGljQmlFdU4xazNqYVd3Sy01bnBnX0U4VW1Yanp1RG51TUNDQQ?oc=5) <sub>MIXED Reality News</sub>
- 📰 2026-10-02 [Skild AI launches robot model trained from one video](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNbWlTakU2cG5MT0w2RXNGbUVBVnRqcHRKcC1RcWc4TGZNb0ttUHRVSUNuWS1GU0hLOG9KY1otNUlLU3pKTG1tRnc3RDVLZGdCYWFxZTZ3SGhhc2VOQmFvZXdRWmhqSGZhZjV5V1gySG9rZGl5VFZCb1I1aFltRzJkanRpWXBEVjZ4?oc=5) <sub>IT Brief Australia</sub>
- 📰 2026-10-02 [Best AI Stocks to Buy in 2026: 10 Top Picks & How to Invest](https://news.google.com/rss/articles/CBMilwFBVV95cUxQcTN4SWRQbVZpY1lwSnJjN3YxWmY5LU5Qck5ia2psWWRwcWplZ0RGTFo3ZmJrZDZ1S1RQZFF2NUcwOTh0NXA3NlM0a25ieHhPWHprdTBmbWxzY2FtdHRIMlpSY1pzcTU5ZkhfN0wtcF9UeDg4WnZVYTZPSkRtcDNZaUJ1djdPQ1RVRkVQeVFUTnJrMFJ5VXdj?oc=5) <sub>The Motley Fool</sub>
- 📰 2026-10-02 [How AI could transform Kazakhstan’s industries: Interview with NVIDIA vice president](https://news.google.com/rss/articles/CBMitwFBVV95cUxNamQzdnV1T0xWOEJSXzIzbXZyRWhaSjNKT2Nza0haSFF0cXJtcDJYUHlPNGFfZEFmR2wzYk9LNWVORXpUMC1WVUQzY3hsaW5COTUtZU14QnpxbFBLaFliS29MeGVIdmFfYTVucThrMkxHUXVhUjJyNWdrM3hCYXQ3OVdTYjFBSG1UZHB2SGJjeXBjZHlDOExESWZ2VUZzbUNIQk5xcHZ4dzJkQTVRNzRQWWljWk5rVkXSAbcBQVVfeXFMTlVodHRXdnZDemR4blVKX0FxN3gzcEhlWjV3LUlJaGQ5TTh5U3FocFNfb01iMEltV2VHdkF4dXhMUGc3Q0RLU2txMTM4aGJjRHJDTlh2Ml8yVngwbnVjYzhrQnVxenQ0UEV1bFJZZFcxTkVESEhGamVKeXhBSUhLVEFMVW9kUlpoTW1UbXRyZEtzLThWVGdrWjF0N2d0cUVRbjZHZW55VVZoeS1kU2Rhdk5lNTFGOVpV?oc=5) <sub>Qazinform</sub>
- 📰 2026-10-02 [Einride taps Nvidia to scale autonomous trucking](https://news.google.com/rss/articles/CBMilAFBVV95cUxPOUw5cUhjNTFRVm5oSURkQ1c1dE9GalVHNjlZLVJxeXF6VlBoaF9ET0loYkJSVzJ6VkdGSlh4eXZ5b1QzTmFWX1VYZkZ3Sjl2eXlQSndsMUdCdkYyeEtZNHkwbEtvTlBJRzhPRTNvcUk5Xy1DLXEzTFItZXFEb0NDNTZqNXFibWNFOGQ2cVRHTlk1RjZv?oc=5) <sub>truckingdive.com</sub>

</details>

<details><summary><b>Wayve</b> (56)</summary>

- 📰 2026-10-02 [Mercedes-Benz Strikes Wayve Self-Driving Deal While Slashing Models and Reopening Buyouts](https://news.google.com/rss/articles/CBMi2wFBVV95cUxPamtrUHF1elJPSm1rejltSE5GWUZOZmdJYW41Q1RNcDgzcU12dk5OOW1tYThjWktLZnpVQk5zX1N0SW9reGU1eHR5aUNtOFZUbm9CMGEtZnZURXhoLUtWcGxvbFRNcC10RTVmdi1jTzB2NFMteGtzVjFxcmtGdXhvMFRrWHpabUpyX1RqcDlPVnFKMTlFSVlMNVhFZGdtSmVMMVlqMU1wV2hpTm55ZE9hWFFVcDR2VEpRMmRmT3ViclNOSkRVM2ZRU1dNYUhabEVGdnRsZlBrVGdJUEE?oc=5) <sub>AD HOC NEWS</sub>
- 📰 2026-10-02 [Mercedes-Benz Pairs Wayve Self-Driving Pact With Deep Cuts to German Cost Base](https://news.google.com/rss/articles/CBMi5AFBVV95cUxObzFuSDBHdDZmdTVUbEhyb25Jc3FOcTA5LWFVWFBrNWw1QWgwUmx3RUtGQTBMeHdQRGNQUkhBSlZKMEtvaEQ4R1Q0VVVyX2FUTGVxQUc2MkphUlVyZmdHaEF5em5odUNPR3ZodlEzYnFzYWw4WC1jbmZIUWUtVGlqZzVTbWNzNE5hNHZwMXIyTGpkdzdaQVB6Um0xX29PUVA5T2hLU3JabkF6SHlNOUR2bUtGYUpWbHAtQ1N0dy13eXB1OU10ZmlEanBycGFWeXhieHJfcEthZnZGWG00V2liaWxBV0M?oc=5) <sub>AD HOC NEWS</sub>
- 📰 2026-10-02 [Why I won’t Wayve goodbye to Black Cabs](https://news.google.com/rss/articles/CBMigwFBVV95cUxNNTZYRmM1dm5YT29lWVFsZjBJaFA1eUV5b1JKSng1VFgySTRQVmp3RXJBbUdFRElIRVhKaXZZRUt6dmhINy1yMVpUWThDOW1naklNQ0RIaHFYTzZ1UnBaRDcxMVdsejBaWDAxcEFhSGhRbE04eEs4SDlBRUQwcXNQMzhJNA?oc=5) <sub>Liberal Democrat Voice</sub>
- 📰 2026-10-01 [Tesla postpones Roadster unveiling due to weather](https://news.google.com/rss/articles/CBMikAFBVV95cUxPQjBMeFhnQlpJYVc4NlFGUmZnRkRKQVhrMzUtazNsV1pHQlNtM1lHU0xsWUY3QmgyNll4T3FPUlhwcWJrbmozWlhxZ1dreWJZQnJFTWpseWFTelBPQjBpSktNc2hXdUtidGdGOEJQbzIwYXFmQUNSeWh2dktvNmdjNGZ2TUtZTklnNm1RSmpQakI?oc=5) <sub>electrive.com</sub>
- 📰 2026-10-01 [Stellantis and Wayve to show hands-free Fiat and Maserati](https://news.google.com/rss/articles/CBMimwFBVV95cUxOaDNUY2ZmMDY3VmxlZXJOdnFKcnBIVzFRazZjRmFSemE0eTVCRjNyeEN0VHpsWW1iTnRZWUhRR3RhTnNPU1ZHbzhxZWloTGdUX2NLQzJ2bHBqMjhBWnB0Sy1rT2t5WTRNeDZ2WXNMUE9zcG5Ea3hFaVNITG9RNUtkV1JlXzhJYl9vdjRFSlp0SFZfOUt6MjFzNnYxRQ?oc=5) <sub>Automotive World</sub>

</details>

<details><summary><b>Momenta</b> (136)</summary>

- 📰 2026-10-03 [带激光雷达的豪华插混SUV哪款好？凯迪拉克全新XT5 PHEV与领克08激光版等5款智驾横评+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE5BdUdXMl9uM1Z2VlJNSzJiU2M4OWp2cDRQUEc2c1h5U1YzdjZuNmZMU1RFSFVEclFuOEppbERLRThXZFNzUVlHamxFX25sNDJYWVBlc0gyRFpiQ2MzNHRGMVNlREJMMkk0SWl6OHo2bXdiQQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-03 [充电速度快的豪华插混SUV推荐？5款快充豪华插混SUV横评，全新XT5 PHEV值得优先看+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE5rb05adHA2cFB4NW82M3ZTcm1oNWl3UUZSaHpwYjJNY2RmSVVYOGl2QVVhdmFOdkZKdlBoTXF3WnE5aDRCbUtJeVdBWExyVTA3OWI0ODFIdEJtbjliRW5ucG9YcldNbUJRemRORk1DVHF0dw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-02 [New Buy Rating for Momenta Global Ltd. Class A (6880), the Technology Giant](https://news.google.com/rss/articles/CBMi5wFBVV95cUxQNWlIOVZpNm1UOVF1QXdCcE1xZlExV1FJc1I0UDI4YWxfZWJvOElOOE5YTVN3NkZvVTQzSnFGSlQ2R01RXy1xVXVsdzVuSjVYNXRTTExJR0czZzhkR09XRE1jN0lVR2NiZkpyMGlBMG9qM005MTBrSWE4dUYtMlRtVnkxWkhoQWdpUDJhOGxFdFBHeWFPRjdKMVlMT3p5RV9DOUJWaWJFOWotYVQ0bTJScWRsSlhGc2JzVzN5b0tPUFZ3LUczZ3JDdzVRME53QW91bWJPX0xYYkluMlZ2WFZGNzdyM3pmS00?oc=5) <sub>The Globe and Mail</sub>
- 📰 2026-10-02 [【视频】Momenta R7世界模型上车宝马iX3+7系智驾表现实测](https://news.google.com/rss/articles/CBMiW0FVX3lxTE13Um5SSi1MNnM2TVA2V2hqYkRtVEU1REdpbkVmZDlrRmNVblFrZGVGa1hjSV90bE9xbnhBR1Y2UzduVXVkYjVQMVVSLWNDLWxhYlF4d2N5OHJmblE?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-02 [带激光雷达的豪华插混SUV哪款好？5款智驾横评，全新XT5 PHEV与领克08激光版智能泊车实测对比+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE9qbHJtb3pRRXFNVmFUekRmOHc4U2VmWWZFVkt2YU1oSk5UMzA2ODlibEg2WU9ZWEtBeTZrZlZHUDJRUkxCczhrRWRCbVZ6dFYyVFViOFhsU2E1dVRrS09IYmFGU3RCSUFsLXJ6VzBYYzYzdw?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>XPeng</b> (189)</summary>

- 📰 2026-10-03 [小鹏MONA L03月交付破1.4万 九成用户多花钱选了智驾版本](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5mMEZwUDk0dl9Ob0RoX1o1V2V3WVVBclVYQTQxbnZjVlo0RFBuVDBrelo5WU9MZ2YwS1JqaGlaRFgzQ3R6M1FTVWNDb0YzOTR2V040WVkzSDRCeUE?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-03 [小鹏P7+黑色版值得买吗？黑武士颜值+AI智驾深度解析+FAQ](https://news.google.com/rss/articles/CBMimAFBVV95cUxNLVRud3RCR2NrR3lMSDFWZURPMlhFQ0ZTRFJXb3ZtUGFnRms5eF9HdDZ2OVhxNl92WjYwU1ZsR3NlWjE3QlFaZWxKNzJzSVZBRWlhaUpuUU80di00Ym9DLXRYU0JvQ1EtYi1kNVB2M29JRU4yXy03ZHRKbHlkd2lTRlhhX2o0YmNFaWlTRjN1V3BBa19wbS1NSA?oc=5) <sub>finance.sina.com.cn</sub>
- 📰 2026-10-03 [15万内掀背轿跑，MG 07凭什么让两强紧张？](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBQZElDUkxLRjd2Wk1RQTRjRnQwdUtMR3ZycHNiTTdZMjZSQUJfRGl5YXI2WkJDWW1RUi1UaFBQU0RQNFB6eS12WlhxMWpUZmREV3hjdXZ1RUtPRk0?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-02 [快充差10分钟，小鹏MONA L03和铂智3X长途谁更省心？](https://news.google.com/rss/articles/CBMia0FVX3lxTE1UUDR0S3RBWHZpY3ZvcFVBR1M1T05Wbk9xdjRBUDgxSnMyOUtUT0tabnJvcUcwakZtTms0TDRTSXdtM1FLMk81SzItdjk1NEhaYVZmUVFhSENic3BSWl83THJ3cm9MdjZqWmkw?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-02 [503马力四驱+6座，小鹏GX对比三款增程SUV，谁更适合你](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBZWFBObGVTbE44Z1dlTTJZT0NKYmxkNWVESE81a1FrRWphS1U3NkNWSW9vd0V3R255YXJrNC1SaDBkQUtMNzVIUzhCM3NDdHVUMXNqb1NsU1ZDMWM?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Li Auto</b> (143)</summary>

- 📰 2026-10-03 [新上市的豪华插混SUV哪款值得买？凯迪拉克全新XT5 PHEV与理想L7、腾势N9等热门车型对比+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE1WRWlpU0VZX2NnRzJNUURjR25LR2tTSXdXNm11NnhpdmtyZXBNVHhCQzFNM0hpekNFTng2cnB2T3h5NGYtcnBadlJEUlJRczNiUnd3TVdabTFnS3k3YnF5ZzNtMVIwMWttM0F2aEJ0MGR0dw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-03 [神行者8对比三款热门大六座SUV：30万预算，谁把“全能”做到了极致？](https://news.google.com/rss/articles/CBMickFVX3lxTE5LTFBBeGxDdkh4UFhvLTRyemRGcTlDNXY3SnU4ODVDTndfNmtHMVNmR1BLY1ZRYUoyeUljNmVscFNmLWJTb0hUbTVUaTNBeDZQdDdBTXhkVnRsU0JpaFRodm55ZGtTRGxidW9SQ3d2SEgyQQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-03 [深度横评：FREELANDER神行者8对比理想i9、问界M8，谁在重塑豪华全地形标准？](https://news.google.com/rss/articles/CBMickFVX3lxTE5UdTcxQklCSkFZaG5jNDdCUUJNQktTV2l6S3BQeTF6RV8tNEwxR3c4X2x5Z2lrUEVtNGkxYWx2LWhGWHV4NW56LTZKUDJUcElMSHBjNE5TZ3VUMEtZWS1PSkhHaXNoa096TGtyakpuaEFOUQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-02 [Is Li Auto (LI) Trading At A Discount On Strong Deliveries And Execution Risks?](https://news.google.com/rss/articles/CBMixgFBVV95cUxPZlRTOEFUZnFNamhESHU1aldBYnA5UFAwTS1Ua0RxVlNLUDBETzM3OXAxUDBkcmwtUUx6UU9aSEtQRmFQczNKUnJWdVppckxOeWI5dFg2N05IMGtzMTloQzFLYTlwdmJSejVFNkpFbkkyODZoaGVoUlNjWHRFWndnYVFHSnd1REdndnlocjM4VTdIQU14WlVzRUFEcW9CNFc2UXpZeUJ1aFRMbXowRzlDVWYwcWpJT1E0dThtOUdQc1F0Zm5nR0HSAcsBQVVfeXFMUF84YXVrRXBIYlUxVm9raGJ0X0QyRkQ5WU9MS2NKdHhwd3d4RDhQaFpLX1RLSlRSdGZkbjlxaEI1YXVob2NSS0xJMWF1UkJOSGNDSktNVG5va1p6Z1NxbjF3NFg2SkJEdUdKZGRPdnZ5cDlqYTFPQUpTS1pUeHQxcFRKQTFMY3o0aUtreGlCMUJsSzI5TlJnX1hkYzhMZ1JZdDhidXp4OUw4WE1nNzR1V1JMM2hCenV1bGM2NnNDRWRoQ0xXMGdoSUdrSVE?oc=5) <sub>Simply Wall Street</sub>
- 📰 2026-10-02 [Li Auto Premium Chinese Brand Coming To Malaysia](https://news.google.com/rss/articles/CBMikwFBVV95cUxPa0tOTmZkOHpvckFyUDlnblZUd0Nhc1dlMnRxU0JqVm1EQ21TcVVZM3lVMGJkMFJIbndDNWFfQkFUZXFCbzJOaEVWX1liam1WMVVjcVlqVU8yTHJIYlVxcUhWWHQyckd5UmI1b0RHeHdxd0ZZbXJEYmQ1NmZmTTJMYk1PdlJGLXJwaXdmWm1HdWJhNkU?oc=5) <sub>Newswav</sub>

</details>

<details><summary><b>NIO</b> (145)</summary>

- 📰 2026-10-03 [【视频】15万多开蔚来ET5！75度电池买断不用月租](https://news.google.com/rss/articles/CBMia0FVX3lxTE42cDV5akJzblRBQVBxdnl0Vl91N0E5U08taG1nYWhXcG1Nbk9Vd2cySW5RcjhjOV9peS1ONUpsOWU4c1k4MWRqZ0VWS3kyZUdnUzJSMnhtcFhvS0hmRXBlYkIyRUxkbWNsN2lZ?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-03 [【视频】蔚来EC6 2022款 75kWh 运动版买断版](https://news.google.com/rss/articles/CBMiW0FVX3lxTE44VEdJZUFLbG5Pbm5YQnJ2MUlocjlCc3ZWSDktTlA5REFHMDhDZVFQV29OTjktMjVTTlA2NjNDd1Y3VGJJNjNUSnd3MldQdklJNnhoc1JmOUktRjQ?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-03 [【视频】蔚来ES6 100kWh电池可换电真能规避电池衰减吗？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1qS3ZCR2xJTUd2cmF1Q2pNNVJoZ2xROFV0Ym5uTndVamVfQTAtdlBzTkVxMVNoVmFQbmJMQ2ptMmItSGpvZDlKYXh3SVJUcEYtVi1iY0pPT2Z0Zlk?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-02 [【视频】蔚来EC6的买家根本不是年轻人这台溜背纯电轿跑SUV在讨好谁？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1MQWEwRng4SWk0eGJkWkhIc2lPaldSRDc4cVlyeTRuZEVkc2VuNkRiRFBVUXdSVzVLeUxVRG92WHZ0UnZzbmRJRUxVN1p2YS02THUyb2RLaFR6eUU?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-02 [Rivian Jumps 4% After Delivering 19,248 Vehicles and Reaffirming Full-Year Guidance; Tesla Rises 2%](https://news.google.com/rss/articles/CBMihAJBVV95cUxOZmhwQ2VjeC1aam4zeXhiZzBUSS1lMWEyOW1oaTlIdk5IdXRrMTYxcWhWTjE2N0hTMmhaZlBRWmZ5bTcyUHN4YjhPb3BvamNqdE5IY0dFQkstUUxqUU44UXgzZ2x2OXkzNmxBR1BMWjhQbkxuNzVXWHZaZEl0b1NNOFBiWGNZell1VFoxREVDVUR4cFVkNE5fRmhsT0g1UmlFMElwNjc5Nk1JaHV3X2ozc3FELXEzWndKUWgyQWtwSWo5TGhzYnJGcUJqRTlPVlEwVTUzdUE1aV9SZGtrQTlobVAtSHBxbDNERW5LSXdyTzlQbFFuREE5NGJ3aFdDVVhUeTRVZw?oc=5) <sub>24/7 Wall St.</sub>

</details>

<details><summary><b>Huawei</b> (302)</summary>

- 📰 2026-10-03 [VOYAH Dream 9 First Look](https://news.google.com/rss/articles/CBMia0FVX3lxTE9ZbTljdVhiaFdBY3hKYlNoajVLc0Z5ek9DeDRoWHB5TkxOUWxxc3Bqd0NreUs2VFRHMHp4bTRRTzZ2c1pUMVRFTzhHNlN3aEpmLUZpRW5DV2FlZVdhdFlvVkFjNnJhTG9uRXJV?oc=5) <sub>Alvinology</sub>
- 📰 2026-10-03 [华为乾崑智驾累计辅助驾驶里程突破160亿公里](https://news.google.com/rss/articles/CBMiYEFVX3lxTE42NHg3VEJhNnlWWGhUWWhxMW5rQzdvbGkzcWhJanR5QmREeXJKUGVCaVlTQmdGTklCRFhPMDgwa1UwNVlOUHhWM1N4d2NtQU1jT21CZVFrTHNjMmxMbUFIMA?oc=5) <sub>东方财富</sub>
- 📰 2026-10-03 [【视频】华为乾崑智驾ADS 5 ，打通你的智驾生活圈](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9OLUdIemcxdlpGQlZ5NzRjd3FJRW4yWEJPVkd6R2g1QUlLRVI3N18zY3k3aUZYMG9uRk9sMWpFNzNrX0d3Q3JIdHhaeURacEdvdDA5TEFlaEU4MFk?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-03 [享界V8正式开启预售：32.98万起，2026价目表全解读+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE9hZFpKanVLVVlPY1VwcnZteV94czRsVElUbEh0SWFhQmVwSGJOUl9vOVQ1MFFNaXdraXRlZVUwcWc2WWFJMmhTQ2dOckkzRzFBelVhZ3Z3ekQwdEFONXUtc2hxcHdnRHAzRXY0NFRQWnhYUQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-03 [【视频】新深蓝S07 华为乾崑全系标配15万级“智驾平权”是真的？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5WOHVkQVlYNEZpeTB3ZHhyaTM0RWNQUjNWOEhzWHhJQXl1WUFJWE5fV3A1YW5PYU43Nm44MTN3X1pWbnY5aEw1d29ZRkZrRXY4MEZFenU2VFlzREE?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Baidu Apollo</b> (44)</summary>

- 📰 2026-10-03 [艾媒咨询 \| 2026年中国Robotaxi行业发展趋势及标杆企业研究报告](https://news.google.com/rss/articles/CBMijAFBVV95cUxOcktmcDgwOXJreWVKbDQ2TnBPSzJLU1hSak4wdDdUS04zeGlNSGpiaUd1cjNWNW5ZY3RlUldUbVNDdy1UR3pwLWRWR2lzT25WVnpidWV6Rk9zNW9lWHZieWJQTUhPUHhZUGJGaVZvX3dXZnZkMV9aNWZ1bkFZTEdTUkZmNkFqZDBzemt3Tw?oc=5) <sub>搜狐网</sub>
- 📰 2026-10-02 [Lyft app launches in Europe](https://news.google.com/rss/articles/CBMijgFBVV95cUxPZldVVUxUU3ZlN3pCRkdpZGpxcmZHUGg1LVB3eVVJLTNWYm5aanI0d0piSnpJN1N0QVFhTkh2Y3lTa0RwQnl0aXF6MnJZVTlXYllEelRfWEtqbnlHMVVMQlYwTFJIMll6TnAxd1NBWll3cW5OcWd5RHduMHZ1anJxX3k5R2tpYTkzbHA2aUpn?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-10-02 [Switzerland’s first robotaxi takes to the road](https://news.google.com/rss/articles/CBMigAFBVV95cUxNRS11TkFwM183UC1RUExMRFRId3M5SHhlOGVJRkttSmZxbFBMVFFocEhXSk1TUnR4X3ZGcHlhMlpZWTNHTkt0alphZ1cwSklJOVhRZHA2ejhzVkZHaGpKZEg4VkNTRGU4SVVFV3JJbEdna3gtRjE5MXNtTG1lWW1jZw?oc=5) <sub>lenews.ch</sub>
- 📰 2026-10-02 [德信体育官网顾客消费超20万，因小事发帖吐槽后账号被限，Tiffany中国零售团队通过邮件致歉](https://news.google.com/rss/articles/CBMiW0FVX3lxTE05bWYzQUQ5LWFpdmRBNGU2ZHZkNnpfdndPWDlPQVJQVlBHeG1TNWRHX09ZcDE4cGpLUDFKbWVKTDJ4ejJtLWhEZUk4aXpBNlhralVzUVZnUW01ODg?oc=5) <sub>Pchome电脑之家</sub>
- 📰 2026-10-02 [PG电子赏金女王伊朗最高领袖：西方干涉时代已终结，伊朗已变得独立强大](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1CSnFBY0RUQjkxbnRwS3BrYmp6T1lMak9EeDU1alBuVkVRbl9OWUZFMVVuMzZJOHdNWFVrNnh3cDB3M296RllUZDN4ZFVkazNQSzE0SGFIYWRXdw?oc=5) <sub>Pchome电脑之家</sub>

</details>

<details><summary><b>Pony.ai</b> (104)</summary>

- 📰 2026-10-02 [纳斯达克中国金龙指数收跌1.03%](https://news.google.com/rss/articles/CBMiY0FVX3lxTE1VQklEWDF0MGhLYWFXUlhmQVp1QmRQdlVYRU81ZW5XMUdGU2Z6WF9UWFVkdk5CdlBkZlBNVTdGN00wWnZmU3J2bWltT1pTZ3lEdVVzNVBvZ0tpc2U4Q1BOMkpjaw?oc=5) <sub>东方财富</sub>
- 📰 2026-10-02 [Does Pony AI (PONY) Change Its Growth Story With Europe’s First Driverless Trial?](https://news.google.com/rss/articles/CBMikgFBVV95cUxOaTM2RklpMUE5ZGpJbU54UlRnS3dqb0hJWTRuaVlxai16QXNKdUhsNzloWDItZ2dRRDVLcC1YSXVDcmFlV3NCcy1vWVNWZG8yMlZUOUdmdG41eHdTSFNUUGZiX1FhV3cxdm1nY1BjLU1BM09DZDNHamFJRDdfYlVpN3N3cjVqanlCcUVLc1pqdkVsZw?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-10-02 [全球食品价格9月升至近四年最高](https://news.google.com/rss/articles/CBMibEFVX3lxTFBmZ3JLc3dMZW1rdzdSeHB4TUh2bGhYbDdhalEzdENIT0Zyc3RsOC1YWWJwQ3VjSk5iRkxyREhOeXduSkl5OVluQnhJLWJya0NLb0tub25FOEk5Q0VQdTRZeFlWY3JsUkNBY2I1Vg?oc=5) <sub>早晨报</sub>
- 📰 2026-10-02 [国际油价狂飙超6%，美股光通信、芯片股大涨，SK海力士涨超5%，也门胡塞武装称24小时内遭沙特空袭47次](https://news.google.com/rss/articles/CBMikwJBVV95cUxQVE9QNV9janFud29MU0FtSDlFUVNjTWFPak55b0twLUdhbF9QV25EQnpJS0dFNzU5cUxTOVVGM1JOcE5Xem14VmdNSlVfS1o2dU5hc2JQcnZwdnpDZm5kaVE3UWFBVEg0WWRfNER4YjRtWGxpZ1NCY1BKbk93VWI3STluT1U3R3Z3d0dCSWwzbEt5d2JLT1lDUUpwMzZxNG9qSGEtREV5ME91QXdLYWhJTEF2cjRhR1AyTHhCTzNmWG02SDBRbXg3SktIT2dpeWdJLUJ1ZFlIX0VrSVRTUUNnQWdsX1dDMDdSeDJGa3BEWHR1LVA4ZExRT2h6SjgxMFpLT3dhRXFFWHZMS21TOWUwbzdvTQ?oc=5) <sub>finance.sina.com.cn</sub>
- 📰 2026-10-02 [10月3日热门中概股多数下跌，网易跌2.82%，京东跌2.24%](https://news.google.com/rss/articles/CBMiigFBVV95cUxPM2d4OHNlbWNVM1dmUXdkQVl6UkwyNnRURUNoVFktemtaWXZCcG5BY1hqVDNSOXdsaGpCelpKSVJ4VzJYcDJrLVdKT3I5RllMbURNMEp3M1h5N1pValE5NzU2WVcwbDk1Q2kwa2lWV3FTVzc3LVVvd0RVbFF0Q0U1eko0UlNiR1p6NXc?oc=5) <sub>finance.sina.com.cn</sub>

</details>

<details><summary><b>WeRide</b> (96)</summary>

- 📰 2026-10-03 [Pony AI, WeRide to stay unprofitable through 2028](https://news.google.com/rss/articles/CBMikgFBVV95cUxNbXpzb3E5eTB5dm1HU05YVndNVXNlb0lTMXh1bDRSMkxkZmRDa2xnQkxfajNSNHlOa1dvRG5YSVctdGlJZ01QWWd4b0EtZkdEaFZtb0xPeDc3QmZ3eEUzTGVOLURUSWJfZEY1ejZqeDVIMXJfcFhFdFZrSTNjNmhJYkVadWhPcXBPWEhmeS01MHNBdw?oc=5) <sub>Briefs Finance</sub>
- 📰 2026-10-02 [国庆车展人气爆棚！传祺越7全国圈粉持续热销，购车权益至高 5.6 万](https://news.google.com/rss/articles/CBMif0FVX3lxTE5BbkVsSkE3Q1VoczcyOVdhTmtkQWoyb2k4V0JXMk1SVWhVT1lPbURmSFo5TjRIcW8tLWZKNFVyRDdGWGhiQlFHRVZ0UDVuNnFuZnE3ejZIeWNGbTZ3c0p2ZFNvS0JlcDA1ZXV4c3p1b0FOSUdYVk5EUmtRZ3M1a0E?oc=5) <sub>k.sina.com.cn</sub>
- 📰 2026-10-02 [马斯克将特斯拉AI5芯片内存需求减半至72GB，AI6削减三分之一至144GB](https://news.google.com/rss/articles/CBMiUkFVX3lxTE8zalhDM0stSm00R0pXMVh2SVhJZzVKNG9DSXhKLWZ5WERKanBPVE5Cd3RYMVllVnJxQUlUdEVMbG96akxpemE0LW5MN3Nacld1blE?oc=5) <sub>icloudnews.net</sub>
- 📰 2026-10-02 [AION i60配置参数](https://news.google.com/rss/articles/CBMickFVX3lxTE1BUzB6aGRWTVN4OTVVYWUzZDBOaGFnUDd5YzI1cHdDSkEtVzVCcW92SlRDazlJeUFqbmJqeG1wWUNlTU0tSTRRV1FlWmptczV4TU1ZMHN3VTVvTHZRbHpaeUh5ZU4xUFlHSjd6TzVvbTR5QQ?oc=5) <sub>k.sina.com.cn</sub>
- 📰 2026-10-02 [China Robotaxis Face Losses as Utilization Trails Waymo, BI Says](https://news.google.com/rss/articles/CBMitAFBVV95cUxOMkNnOElING5sMG9sb0QwLTJVaVRTakFUbnVKMnY1bFBkOGRwNWZ3ZkpkR3VEQVJyOGdQTFZhdlo0NzhjQjdFRGkycGdxY0JMckozSlpFSWl1dVd0TWRuV0hKdVhhTFJlMDh5aWlVOEtpcWhudGhKN2dCUFExRURqTEp2Mk1SS0RMLXNGZlh3SXFfSi1uNG1QOVg3WEFKcDVxclhISEJleTJjRFNGUEF0NlprMFA?oc=5) <sub>Bloomberg.com</sub>

</details>

<details><summary><b>Horizon Robotics</b> (142)</summary>

- 💻 2026-09-29 [HorizonRobotics/Ego4WAM](https://github.com/HorizonRobotics/Ego4WAM) <sub>GitHub</sub>
- 💻 2026-09-24 [HorizonRobotics/CogWAM](https://github.com/HorizonRobotics/CogWAM) <sub>GitHub</sub>
- 📰 2026-10-03 [【视频】深蓝S05纯电版全系200kW后驱，10万级罕见配置，值不值？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9vdzJHYVY4U0dlcjFLT0ZaZVVfeUtoWFZGRnFWU0hKVGk4M2ZFTlRPeVlzdEp6eV9nckRNSzFtcm83bk8tVnJHdW5xT1ZnWmJXbjcwdDVRNmxOeEk?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-03 [【视频】100万辆之后深蓝更狠了，全新深蓝S07直接把高端科技塞进15万级](https://news.google.com/rss/articles/CBMia0FVX3lxTFB0SllvbUczV3dqYzZ4ZUozT0c0UGVDTFVNckRjMDRZWUJJVXlwcWd0NWRRWWFNZG54bTExZW8yS0YyRDAxV2lyaHNpVWdlQklrSDRFWU9SeEw2VXF4MjZkamFDOWJ1WTl2aUVB?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-03 [192线激光雷达与城市NOA加持，三款德系纯电SUV辅助驾驶真实力横评](https://news.google.com/rss/articles/CBMickFVX3lxTE0wNmFVRXdHSW1Nemx5WHlCSWowVVF2UkxseVZUSjlVd2hrTEg2SklBbVU5bVpMS3Z1Vl91amN5SlVTczRIUngwVjM1TjBXRlI2TzQ5M2VJQTVaaS1hY1p6ODRLbV85WHFzQk93N2FRYVB5UQ?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (24)</summary>

- 📰 2026-10-03 [你的国庆自驾搭子来咯🥁！无论是堵车、窄路、复杂路口，还是泊车，小元都陪你轻松出发，安全抵达。#元戎启行DeepRoute ##DeepRouteIO##辅助驾驶##物理AI##国庆节##自驾游](https://news.google.com/rss/articles/CBMiY0FVX3lxTE9oQzI1QkRUaU5jRDFaR1QxMzBmVDRZSkVXb0FuWkJfUzN0MEh5NDZSVEhCR2hjUzhUdldrTkhEelNlZ0JPTE9SWEhaOXRHNi1rZ1hBQUNOWElJWF9fV3c5aHh3RQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-02 [华为放手13天，赛力斯憋了3年的大招在巴黎炸响！](https://news.google.com/rss/articles/CBMif0FVX3lxTE1EU2I1a1BiV21VZGdwQWI1a08waTdfc1V6MDR0bXNwNWNDNGZrLUlDM1c0aUNFVmVBRUNsRjBQTWZCNGU1TmdJRG1qSlg0UHNHVmZDMUVuY3d4UmJyTlJoWXF3VzRHWDQyY21qSlBwX0RfMFdoemZwMTN5N3MyLVk?oc=5) <sub>k.sina.com.cn</sub>
- 📰 2026-10-02 [华为第一，元戎第二，Momenta 第三：城市NOA前三强差距只剩1.7%](https://news.google.com/rss/articles/CBMiSEFVX3lxTE9TN05LeXZBZHM5MVZKY0lmbGJXMjE5Qm9QZkJmTjNkOTdnN0xNc0NKZUNfM0hZZWFpYmdqMGRwODFYRDc4b2dJeA?oc=5) <sub>i.ifeng.com</sub>
- 📰 2026-10-02 [元戎启行中国城市NOA装机量增速明显](https://news.google.com/rss/articles/CBMifEFVX3lxTE0tU2VqTFl0VG5fOTUwWFpfb1Z3MWNCX1RUQ0xPeDJkUUQ2eVY3MndsRmpUbU1tNkk1cTlpNDVtY3NVUXBaRWs3aXc4djlMcDQtNFppcndCNHNCekxXR1pqbk5pbmxuY1NYV2lMdE1YTFUxa3NIMFh4cXVuY04?oc=5) <sub>新华网</sub>
- 📰 2026-09-30 [赛力斯代工，豆包上车，这台跨界SUV 在巴黎亮灯了\|赛豆科技\|赛力斯\|元戎启行\|me7\|aiva\|豆包大模型_新浪新闻](https://news.google.com/rss/articles/CBMiY0FVX3lxTE5UYlN4M1d3aFdYN1lZRGpLTTZpVmlBTzV1U3hLZ0s0emlPOTBXRUdJbHBVb1E1bld6ZG5KVVRzT2l0T19EbWNNdUx2RkdrSWtvcHB3b2VhTmF6OWZKWTBtRmFvSQ?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>Mobileye</b> (17)</summary>

- 📰 2026-10-02 [Mobileye Global Sees ADAS Momentum, Eyes Porsche Launch and Robotaxi Expansion](https://news.google.com/rss/articles/CBMi0wFBVV95cUxQYzRBUnBoMFNxTkNkYjFDNl9YbVpSRTVwb1N5SjFjMm56dEFiS0I2amZUQ1JqMHFTTlJHb2N2bkhlUXhOaTRpbHJIWWxhWWVBeUxsdlZ1bUtTdzRsZEUzV2NHWUpaVnN2ZzljWnhZSnlibjNHNjE5M1pyc21xekJGM1A3Z3V0SGZRVTVGSG1hMm9DWVlnSUhBQ3hKNk9yQjBZUU12bXN3MUFWc3k1XzZKXzZIeGh5bEVZaXpta3cwMjVHUGxlaHRINGhKdnhERU12TkRN?oc=5) <sub>MarketBeat</sub>
- 📰 2026-09-30 [3 EV Stocks With Up To 39% Revenue Growth](https://news.google.com/rss/articles/CBMikAFBVV95cUxNbktkTHB2ZmdVWjdmMG5GaWdrR0dyenFac2dnV2d3eWpIVGxmOHJIeVpZU0RBREthd2xEenRPODRhcHhyaDVYV0FGX1l2eVhtTVNDZV9kN2t5UlR0b0Zyc1MtdDluZkZpaElxMlJud0VIZlN0eldEWGZVZ1Z5MlRyV0NRdU04bkRaaVdVV05nejE?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-09-30 [Mobileye Global And 2 AI Driving Stocks To Watch](https://news.google.com/rss/articles/CBMiwwFBVV95cUxQSDFHSFBPOGlJM0RvZ0toN1JTdThRbFNLd3dIUmU0YV91Zl9hQTdWcnVxOXM5TUpHa281bEZkbDhXMDZmdWtHcmlTU0lfZl9SNTA5bC1QMmZQTVpKMkdGTmhiZWI0aDg1VnZ1Z1pFdW9WWHM0SzBaYlJMb2ZMNXN4TEdNampfQXlvekx6UEZRVEd4bU1IS0VWTVFRWkcyWE5IamRockRJQWF1b2lxWnBmVmNrS1RIQV9EYVhJSW05SkZodWvSAcgBQVVfeXFMTmRuV0ZhQ19iRGZhek1SUkVCV0VwWERKcWJkdklUV1NPUm9wSXBTN0hrSVRPUWthSTAzbE5PREh0QmhvUGlCSEtzRVcxRWtleUdtS2psMXhsUWNrSGp1VDRzc1F4NjN0dEZIT3pXWFRhYy1Nc3RSd0VBV0c3ZHlZUGFnU2wzZVQ3N0xtR0oxVzczV2VaR3h2U0ozRmVQTDlBOVRmTEtOdFFVS08tRy1WRllMUWFfLXN6ajFLbWx1T1FhWEtrS1IzeXc?oc=5) <sub>simplywall.st</sub>
- 📰 2026-09-30 [Mobileye Global And 2 Top Autonomous Vehicle Stocks To Watch](https://news.google.com/rss/articles/CBMingFBVV95cUxNSXlrYjJPWG8yQ1B2NF9hTXJ6YnJTdU9pRFFUTEwyMDZ0bjJMNHctSzdqbTFIc3k3T0RFNTVmUUtmRkhxdGQ0bjdHdHZhSkUzUHUzSlVoMTFNRVMzMUUyMlBCTDVLeG1MV1R1NkVXYmp3U2w1ZDRPUWNwMUduWjM4d0NIMFFUWnc3QXM4OXlQS2NDT0RobVRycjJsR0tMZw?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-09-29 [Mobileye at Evercore’s 9th Annual ADAS, AV & AI Forum: growth and autonomy](https://news.google.com/rss/articles/CBMiywFBVV95cUxPU2lGZVVxeEFwczgySTQyOFBlNkhoN2ROMU1aaFBsWWlFVF9nZndrN284OEMxUTJ6WGtLb1l5dWlCd25qSHRwdW8ybTZTcTg2ZnZ0eVM1MWhreko0dVYyNVNpSUtRd3MwUkdfU2MzT210ZUxLYzRPU2RjUnFjSGNyZGNBVTd2WURGNThzRnBGYXU2NFNsMGhyMmdhZFZpdl85WTV1SUtmS0dUYVJCcmljNFlNYTR1UUNBTF9fWFhieE52TGJlZHZ2QXltTQ?oc=5) <sub>Investing.com UK</sub>

</details>

<details><summary><b>Aurora</b> (45)</summary>

- 📰 2026-10-02 [Aurora Sets 2030 Scale Targets as Kodiak Names Its Driverless Launch Lane](https://news.google.com/rss/articles/CBMipwFBVV95cUxOcUxDQ1dvcFluRHh6bnBzYTBhMmR2QXgyamkydGRYYUU1eTNUeGh1bnFObWMwd2Fsejd2YUdVV0lsRXZjMEtSdjEzV1ZWZUpZclZhM0Z3ZXdCUk1UZEhkRWtucXV5Nmx3RTAtV01rWjBRRDlaUmhRSjE5c1VWSXpjeE4tbFpuQlNfU3M5S0R0Z3VDUVRzNE9rUkFCRUlPM3psX3B0UTRISQ?oc=5) <sub>act-news.com</sub>
- 📰 2026-10-02 [Aurora CEO on plans to scale up fleet of self-driving trucks](https://news.google.com/rss/articles/CBMigAFBVV95cUxNQ19oRjhzVGxFNmZiVXpwZUpOempNd0xUWV8zU01KM0U4QU51TDVYQXFWcGZJdGRObmpMaEs3UUc3bHdzaVlGdHdmSU5IV2xibnhHbW9JalRJU0NpTWQ1QUkySlg4MDBTUVpKbFVpc2dlbFRqakFMVmRfQnpkcW9xWQ?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-10-02 [Autonomous truck beacon waiver moves closer to October renewal amid legal challenge](https://news.google.com/rss/articles/CBMihAFBVV95cUxQQ0lmYzY3VUFxWlVueUZaTURHVC1vT3VDc2NfN3M5ZzAtZWpCNXBxUk52X2dNVllLdUg2amlNN0R3X1dyM0NGUTZiS3dLcFBWOU5zTGN6cjFodERTelE3RW1vRGZBS2w0NjFHSVBfMGJqU1JhUHZlN3hBT1hhSUFlNmNPbXM?oc=5) <sub>FreightWaves</sub>
- 📰 2026-10-02 [Driverless trucking in 'first innings,' but fears rise of a blowout game](https://news.google.com/rss/articles/CBMitgFBVV95cUxQZ2hRYjVyckNOVmtiYms3aVFDcTgxbzlYelQ3WmpranB4eHBHRXRpZFBBVGhzMFNWcEtoVnRlWEhwTFJOYW5WNFhrS3NYeEhtN2J0LWVOOFhzX0xKWEJJVXBHTEJ2R3J1em44cHVfdFZ6TTFqbGZBT01zQzB4UzlYRXFUSnBCbWF6MnNfMFNCX0k3cHRqMzdjNjM4cFBoeHhPa0VidVZWQ0UzeDZvd1BzaFR0U1VTdw?oc=5) <sub>overdriveonline.com</sub>
- 📰 2026-10-02 [Self-driving big rigs roll into California as driverless future comes into focus](https://news.google.com/rss/articles/CBMiqAFBVV95cUxNMnlHV2RtMU1WUGJGVTdjZ3N3TzdreHdWTHZEZDBwUk1OaVlDb2Q3SnlqMGZXYkxsWkViUi13RDhLekxtYmNhcFE4N2xVRkxGNVBPYS1LYm1iU0hkUHR6ZHZRUDZqZzJsam0xSnRFTV9TYkdTMnVSdWg4QnRvWUlPQmxNTnFVUVc2Vm9RSkFwN1hMY2xtZlRTMFJZRFV2UWdTVHFVaHNud08?oc=5) <sub>New York Post</sub>

</details>

<details><summary><b>Zoox</b> (81)</summary>

- 📰 2026-10-02 [California signs law imposing fines on robotaxi operators — TechCrunch](https://news.google.com/rss/articles/CBMisAFBVV95cUxOc2hlSEkybklDM2hmdVY3Rm5hVTFFMDhwZW9BY1JyV3BHeW40ZDR4aWhwSW9PZWk1WXc1WU5Qd1V1Q1VGVjZvM2pxd0xEdEluOVlHaUtFR1R2Mk1nLWhGU3cxa3lja2dOTDc4Uk9mQmJseHFZUkJHVFdGcG5IYnFIdG54bmNtVDQ3dmtGakd5anpRb3RSa2lRRnhPWEt5cFZUVzcxSUZlWXZ4V05Tcjc0Nw?oc=5) <sub>UA.NEWS</sub>
- 📰 2026-10-02 [Self-driving big rigs roll into California as driverless future comes into focus](https://news.google.com/rss/articles/CBMiqAFBVV95cUxNMnlHV2RtMU1WUGJGVTdjZ3N3TzdreHdWTHZEZDBwUk1OaVlDb2Q3SnlqMGZXYkxsWkViUi13RDhLekxtYmNhcFE4N2xVRkxGNVBPYS1LYm1iU0hkUHR6ZHZRUDZqZzJsam0xSnRFTV9TYkdTMnVSdWg4QnRvWUlPQmxNTnFVUVc2Vm9RSkFwN1hMY2xtZlRTMFJZRFV2UWdTVHFVaHNud08?oc=5) <sub>New York Post</sub>
- 📰 2026-10-02 [Robotaxi operators will face fines for blocking first responders](https://news.google.com/rss/articles/CBMioAFBVV95cUxQTkxIUGliT0tPdU5KZzJoQm1JUDZXMVA0RGo5OHV5RV9pSm9lYzVyRUp0MV9WaFN4ZzJvdlRpMktmeHdOWDlYNG5xQk51cExkZTNtZFBKTG1yNG9nWG1aMzhCcEF2UEJXcjhIRHMtMXJCZ2lVbnVEaWRoM01BWjFtWmhCa1ZxRE5lX0hhSkJVSG5obVV1d05tamVnOFgtdzgt?oc=5) <sub>TechCrunch</sub>
- 📰 2026-10-02 [Robotaxi interior is not a private space, industry reworks seating and surveillance design](https://news.google.com/rss/articles/CBMixAFBVV95cUxQZkFBaWM4cDA5RGozNzg5NDgwbGswcFBmQzQ2REczN1RBeFM0alZ4VUtSb1lrbFMwdElSSElYdGRjSml0dzR2OXFfazY3djVBc2hLMzMxc0gxV2h5QjRDOHdxY1V4d0RwVnFibUhUbXFSVl9UYVpEUVBjR3RSM2hIWVVGVjhsdzNpbXBSWFFsb2FWRlJlYWVka1ptQzEtcmlJeHdsX0hzclE5SUJERVR3MVVjMFBWc3VLMzlKaFFhYWJ3LWds?oc=5) <sub>디지털투데이</sub>
- 📰 2026-10-02 [‘I Have to Buy My Dad That Lamborghini’: Indian Techie’s Silicon Valley Journey](https://news.google.com/rss/articles/CBMi2wFBVV95cUxNMTNIWTY0YWF5RW1vMXZFUVNYaGdZZUJfcGlNMm9XWG1jMy01QTFGdUZUZlQ3TFhNNFlrWlJITUJqQk5NRUJHOWZrZGNvZXhmZHZBSmtqUF9lM1duQUlIZ21MNkw5TWVEVGNQVzJSQXdrWEIwV200R1JETWtkaTFQaDdtdkhPTVR5WXRKVkp3R21kYnZmU2VvR09Hc2N2NVpxMFFkMElMRWNjVzVtel9KNjJUM2pfdW9UaTJ0X0lGeE8wb3BwYTZub1F6LURRdzNSWkE0ZVp0WTZjWXc?oc=5) <sub>Dainik Jagran MP CG</sub>

</details>

<details><summary><b>Motional</b> (26)</summary>

- 📰 2026-10-02 [Synopsys Unveils Autonomous Semiconductor Design Agents; 50 Collaborations Underway with Samsung, Nvidia](https://news.google.com/rss/articles/CBMidkFVX3lxTE5JSGVJNUZDUHBaZGpNYy1nTEcteGdsaUF0WVBIdUx2Yzd1X01lSkhIbHFqaDhENzZTOE1Zc29Rc0VRU0xfY3pLSDdwbk9sQ01oMWJxamNfOHZhRTdVdXQxRnIxdHpFNUg5UXVRX1haeDVEd2dGZ1E?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-02 [South Korea's Hanchang Plunges Over 90% on First Day of Delisting Sell-Off, Tumbling to 85 Won](https://news.google.com/rss/articles/CBMidkFVX3lxTE1GYTN6S3BEUVlyVi1nMDhvd09hNE5MR0FQeWQwV2hkWGpEYXItR05jRlBJaGNQdk1kaWlqa3o1VWUwVEZtX3FUOTBWNy1ULVZGRmlOTFVSNmJyZk9OdU0zcmFPUFAwRkxVWkd4cFVMaHRFd3RHc0E?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-02 [Google's Robot Strategy: Software First, With Gemini Robotics at the Core](https://news.google.com/rss/articles/CBMidkFVX3lxTFA4U0E1dE9RNFB2Q2Z6N0MtV05Db212M3dOMWtTeXY4eGJmN3BCa1ZFOUZxbHQ3akJwd1NSTi1MZU9TVGxTeUstYjFJMkFLMGFHRHZSX0drdGtTcVk0Y2VGZU10a0dPVlpmdlR3LUUxMkRkVDJYY3c?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-02 [Supermarket rice prices in Japan fall for 7th straight week, 5kg at ¥2,926 below ¥3,000 for 3rd consecutive week](https://news.google.com/rss/articles/CBMidkFVX3lxTE5OWVltSmxJY0hzTDhGNnlyRkpMbWlta2F0M0ZRRHdBd19BRUFCbE5qcWdrYTZ1T0UtMHFIc09KTl9ORVpDSXl1eUxLT1JwN1hDZ0Y3Y0JhVjFTSVN0MTdUVVNzZGxiYl9GYS1QTkl4MWR4cDZ3TXc?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-02 [California Governor Signs Law Penalizing Robotaxis That Block Emergency Responders](https://news.google.com/rss/articles/CBMidkFVX3lxTE8wM3NhbG5Ha3F2ZDBwdVpkU0FETjdvYXFCdUplVWZ4ZG1oMmIwZE8xb04za1dSS3RlOVFXbzZ4cUlkMVp0TE9zdndKazk4QVBCcjdUdERLVnNHZzlEWjVWTV9uc0NRclN6TklraDF0dTdzYjRlM1E?oc=5) <sub>finance.biggo.com</sub>

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
