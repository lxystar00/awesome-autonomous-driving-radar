# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-10-07 · 1,242 papers tracked · 38 curated.

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
| [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)<br><sub>Nan Yang, Zhanwen Liu, Linfeng Zhang et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 3](https://github.com/Zizzzzzzz/MVPruner) | Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings |
| [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)<br><sub>Yuan Gao, Wenting Miao, Mattia Piccinini et al.</sub> | IROS<br>2026-07<br>📑 1 | [⭐ 27](https://github.com/TUM-AVS/Chat2scenic) | Validating autonomous driving systems requires diverse, regulation-compliant test scenarios |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 7 | [⭐ 490](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
| [Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air](https://arxiv.org/abs/2605.31066)<br><sub>Tianle Zeng, Yanci Wen, Xueang Yu et al.</sub> | arXiv<br>2026-05<br>📑 2 | [⭐ 1,112](https://github.com/louiszengCN/CarlaAir) | Recent aerial vision-language-action (VLA) models show promising single-UAV capabilities, such as tracking moving objects and navigating to language-specified landmarks |

## World Models & Generative Simulation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [HERMES++: Toward a Unified Driving World Model for 3D Scene Understanding and Generation](https://arxiv.org/abs/2604.28196)<br><sub>Xin Zhou, Dingkang Liang, Xiwu Chen et al.</sub> | ICCV 2025<br>2026-04<br>📑 4 | [⭐ 71](https://github.com/H-EmbodVis/HERMESV2) | Driving world models serve as a pivotal technology for autonomous driving by simulating environmental dynamics |
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
| [A Survey on End-to-End Autonomous Driving Training from the Perspectives of Data, Strategy, and Platform](https://arxiv.org/abs/2610.00926)<br><sub>Chengkai Xu, Yiming Cui, Jiaqi Liu et al.</sub> | arXiv<br>2026-10<br>📑 4 | [⭐ 102](https://github.com/Jiaaqiliu/Awesome-Training-Ecosystem-for-E2E-AD) | Autonomous driving is a cornerstone technology for the future of intelligent transportation, where end-to-end learning has emerged as a transformative paradigm that directly maps multimodal sensory inputs to driving acti… |

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
| [123D: Unifying Multi-Modal Autonomous Driving Data at Scale](https://arxiv.org/abs/2605.08084)<br><sub>Daniel Dauner, Valentin Charraut, Bastian Berle et al.</sub> | arXiv<br>2026-05<br>📑 2 | [⭐ 399](https://github.com/kesai-labs/py123d) | The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics |

## Safety, Robustness & Evaluation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [CCFM: Collision-Constrained Flow Matching for Safety-Critical Scenario Generation](https://arxiv.org/abs/2607.04451)<br><sub>Ke Li, Kaidi Liang, Yuxin Ding et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 3](https://github.com/KELISBU/CCFM) | Evaluation of autonomous vehicle (AV) planners in safety-critical closed-loop simulation is essential for real-world deployment |
| [Lipschitz Optimization for Formal Verification of Homographies](https://arxiv.org/abs/2605.23203)<br><sub>Jean-Guillaume Durand, Panagiotis Kouvaros, Maxime Gariel et al.</sub> | CVPR 2026<br>2026-05 | [⭐ 2](https://github.com/jeangud/homography-verification) | The adoption of vision neural networks in regulated industries requires formal robustness guarantees, especially in safety-critical domains such as healthcare, autonomous vehicles, and aerospace |
| [CADET: A Modular Platform for Evaluating Distributed Cooperative Autonomy in Connected Autonomous Vehicles](https://arxiv.org/abs/2606.04072)<br><sub>Pragya Sharma, Brian Wang, Mani Srivastava</sub> | ICRA 2026<br>2026-06<br>📑 1 | [⭐ 0](https://github.com/nesl/cadet) | Deep learning models are increasingly central to autonomous vehicle (AV) pipelines, yet their integration has traditionally followed a monolithic design where perception, planning, and control execute on a single onboard… |

## 🏢 Industry Tracker

Latest 14 days of news, official blog posts and new open-source repos from tracked companies. Full daily feed in [`daily/`](daily/).

<details><summary><b>Waymo</b> (219)</summary>

- 📝 2026-09-24 [Our Vision for London: How Waymo can Support a Safer, Connected UK Capital](https://waymo.com/blog/2026/09/visionforlondon) <sub>official blog</sub>
- 📰 2026-10-07 [Waymo and the acceleration of autonomous vehicles](https://news.google.com/rss/articles/CBMiiAFBVV95cUxQZTEtaGxxZ2t2VzlnOGpPQjZlYXNKTW1pLVBhb2RSZWdLUkpXMjZoQUw0QUxTN2hJLTRxVThNWUY2NzdXeFkyNzdXdTJvT0tkOGgyTVZELVBsUUVTSml5OVdEUVNDRThRM3o2MnZOZkYzcXFWY3BweEt2eXNHMUVmd0piek1sd2Fm?oc=5) <sub>WPLN News</sub>
- 📰 2026-10-07 [Driverless cars hit the streets of downtown Detroit as Waymo begins its fully autonomous phase](https://news.google.com/rss/articles/CBMivAFBVV95cUxQSi1Vd3NlNVhsWjlGdlNFUkpUTU85ZFB0TklyOGxwYVdvTzFSNFhRVlRFSVU3T2x1a21oR0djWUVtOGVvNzJVWVZfeER2TC1WQWFkZ0g0THlOT002ejZ2cHQ3STBZMGY0THZUOGpSTW5ualctQng4bVRWV005QXhXLTZIYzNUWDQ2aktmcFZJSnBRWE5mXzJUTmMzQnlrcXJjS0pkbnI3S2FfZE1xb3JFN051VjZKbUpLSlgwcA?oc=5) <sub>WXYZ 7 News Detroit</sub>
- 📰 2026-10-07 [Waymo Robotaxi — Safety Concerns Rise Amid 210+ LA Collisions](https://news.google.com/rss/articles/CBMie0FVX3lxTE9BUUpkbmRHeHhYdmllc3B2Nklxdkx2cjQ2RUtXX2cwM21JNFhTMXM5YWxNRWVEMWJXZXRrNnNsclQ2VkNFc0lLWTFkSE1CVV8ta0VCY2VCODlhX2loTk8tOFRxLU5CMENFaTdndkpUeDBhMk9FOWZsVWNjdw?oc=5) <sub>The Korea Daily</sub>
- 📰 2026-10-06 [Letter: A happy ending to your Secret Service altercation](https://news.google.com/rss/articles/CBMicEFVX3lxTFBORjRPaHE0RFhxdkpjZzNZXzZjcmZocXZET0dCbHlnNlBPTkZvV2t3TVlpVEhiSFhtV2ZWdzJBM09qZXNublZZbUY0NGJVbjVFcF9UNF9qbjJPY0kxVi1xSV9XYWlzQl9ERTRqQndiSWw?oc=5) <sub>ft.com</sub>

</details>

<details><summary><b>Tesla</b> (319)</summary>

- 📰 2026-10-07 [Tesla is browbeating the EU to approve its ‘Full Self-Driving’ tech. The pressure is working.](https://news.google.com/rss/articles/CBMiyAFBVV95cUxOdjBuOTVpakJxeU9NUm55Z2xWcU42ellEeUI4XzhuaGdNWWViVkFqSGJwVGg5Y3NPNmFlTFVBdVBiWGh3TmdCbjF1UnhGM00tQXFPSS1lOHB2YVk1d3ZGbnEwMkRuWGJFREdOcmFaZ3VOYm4tTHkydlZEOEJrTGNqVDZHSk5IZFkxSGFHREhFcm9ZamZNU2YxbmRfVVpmYUJwYm5Wc2Zhdm9yUnlZYW1UM2xjcXVtWGNsQlZsTjh2eXBjQWRaSm9OQg?oc=5) <sub>Reuters</sub>
- 📰 2026-10-07 [Tesla FSD V14.3.11 and V14.3 Lite Rolling Out: What to Do Now](https://news.google.com/rss/articles/CBMiaEFVX3lxTE1kQ201alBFM1VrTDBnSmRpM1lYRzkxSUNMWVl4ZXdTUm10V2NjclR2N3JrVkh4bnN5MUpJczhkU0dJQ21waUI3eEhTRXBwRlJCMUdIaEZlSlA2QjI0bF81QTRDM2xmVUh4?oc=5) <sub>BASENOR</sub>
- 📰 2026-10-07 [Tesla to showcase its Cybercab robotaxi at Paris auto show](https://news.google.com/rss/articles/CBMipgFBVV95cUxNWThXQzB5OWw0LUpOcWZZN0pVdEZVdlBhZ0Y5ZFlYeDlkT1FOVDJPa0hsUWVadkNLa1d6LWo5ZVlzeko3Q09RRVR0UC1qYmhqc1NvWWtDOUpqaDhibHp5NWdwOWxJdW8xMGVwSkc5TzZGRng1Z2x6X3EzRlVTeTdVcVBzcU5FWFhrOS1mSFc2c3FmNmJyU3MwQWdtTFIwd0ROQUlYQW5R?oc=5) <sub>Automotive News</sub>
- 📰 2026-10-07 [Inside Tesla's pressure campaign to win EU approval for 'Full Self-Driving'](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1aSXZZaERSSjlPclVwTk1TRW5XRHdUaXliZmZYMGt4WmtvcnlQOTRpN3dVQVcyRUN2Zzg4eWJRMHpOeDNxVGZ5ZTUxWW0zQUctWWlmZEV1MjJtOVAzUDE2QXNwSE9STUk?oc=5) <sub>Reuters</sub>
- 📰 2026-10-07 [Tesla ships ‘spooky’ Halloween Mode with creepy and fun features](https://news.google.com/rss/articles/CBMigwFBVV95cUxQSEZWZ180RlR3dGtZZHBIQWpKZnVEdU10ZmR0WkFUWTQ5Q0JrQVRWeTAtTU82TWUxdS1lMThUWF9PdW1hREtIdmFISTI3Z2JUd2ViOUJEaEg3b0tiSC1majBGY0hxdW80Wmk5RGswcGxiUDdLLVZUZFR3Z3pEb19VMTdZMA?oc=5) <sub>Teslarati</sub>

</details>

<details><summary><b>NVIDIA</b> (209)</summary>

- 📰 2026-10-07 [Gears of War: E-Day Out Now With DLSS 4.5](https://news.google.com/rss/articles/CBMiogFBVV95cUxQcG1KbENSNjh5U2lPTEROT1VYdVBsU24yQzBseWt6VTc2bmozSFhpUFZhakFRWElyS0NKSVZmU2JRNWZ4NXRkbkZCaGlFOWFoV3lhdTNkQVdpNURBVFpSTFJTend4c2w5OEE2MXdBcHhTV3Z6SF9IcmFoZ3pteFk3bXN1TTlNVmZ5T1RHMFBhSzZaRC1LaDV1X2N5dEYzbjI0eVE?oc=5) <sub>NVIDIA</sub>
- 📰 2026-10-07 [AI Giants Drive Market Rally: Nvidia (NVDA), Microsoft (MSFT), M](https://news.google.com/rss/articles/CBMipwFBVV95cUxORVItQU1ROGdNZXR0YWZwOHlEZjFJTzVDUVJyWWw0Q0piUUFlOG5USnVCRmFoSUxKY3B5bFFWVjUyQ2E2S0p0T3NKZ3ozRDVOZmxSS1RhYmVHd20tcEJGQVczWHFlcF81VnFvX3NuT1dSSGxpN2c3anFncE9YZ3Z5bUk1MG03TE1TdXhZcU5IU1ZSYy13QVV6SV9mcVQzNkQ5eFJSNm9NZw?oc=5) <sub>GuruFocus</sub>
- 📰 2026-10-07 [Morgan Stanley reinstates this AI chipmaker as its top pick in semiconductors](https://news.google.com/rss/articles/CBMizwFBVV95cUxNX1YxTWRJNWp0bV9faHUzcUQtamZRZTVheGtSTkdYWHZ1OTRTX25BQjZTc1QwVEVhdkc2Tk1meU5jeDI4MmFRLWpqNk85bko2TjVZanNLcGFEUURmRzZsQTk2YlNYeV9ZS1NvVXJQWFdYVENOendiSlpwa1lOaDllTWVwb0ZBazBhcnhOSDFoYTNEWTQtemZzbnFSV3o3ZEpQNHRzMF8wbWNMWEhsUFFNdHRvcHZfX0lCNlZGNnVVLVAyMUxmNmRFWUFVVzkwRVk?oc=5) <sub>StreetInsider</sub>
- 📰 2026-10-07 [Open-Source SCSKiller Tool Precompiles Shaders, Kills PC Stutter [2026]](https://news.google.com/rss/articles/CBMif0FVX3lxTFBYdW92cWNNeFBWRXVnTlRuTHVxd3hiTkpjSWRHLTM4SnhlSWhLOVppSnVJWXpiSml0eE9mWDU2b2F0QzJHdWpmdFEwaE1tTlN3UkM3VXBabXg5WlA1UnUtUzJjSjh1VnQ1ZkxxTUxjY1IwUERsYlFUSHNNODRTbDQ?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-10-06 [Nvidia’s NVentures Joins Reactor’s $74 Million Funding Round](https://news.google.com/rss/articles/CBMiWEFVX3lxTE0yaXVQQ3BGdWtGRlBWbjhzcUYwRV9mQWM0ZWJqdTNzbnpEdUNTc0ttT0M1ZmFIQk5KX3Z6YWZEWUx5SVVRZFphYTZyRW9yWXZfWXdwcVI3MWw?oc=5) <sub>tokenpost.com</sub>

</details>

<details><summary><b>Wayve</b> (64)</summary>

- 📰 2026-10-06 [Watch Wayve CEO Kendall on the Future of Driving](https://news.google.com/rss/articles/CBMingFBVV95cUxQT1ZoV09JRWhBd1lXZW5ORnVVZHJCRTh1T0NseEZTZ3NEQkpMczFGU3pVdW5OZDBjckZQOXp2bW40Ung5Zjk4TDdiNGRlNmFEZ3RJYXBiemRaSS0tNXFnaUU5d3RXdWt6UHlQNWYtM3VlblNza1VIbURWZlppVFlPSWY2aHl2MkxtZTYwYUFDd0RvWEEyS05TTjRnY0FQUQ?oc=5) <sub>Bloomberg.com</sub>
- 📰 2026-10-06 [Stellantis And Wayve Take Hands-Free Driving Tech To Turin](https://news.google.com/rss/articles/CBMijgFBVV95cUxQbG9TWWUxSnZZaUh3SWJsODlXRS1uRWpHMFVpY1VqYUFfYUpDR0pxcjdpZUVOTGdBWkd1UjFZSjBrSm80ZnliOUVsTDlxZ3l2anpVZ21VWlhvMEpjMzdSckJYT0tBNEhqdzJkbUJqVnhfWTRMeGxoYWtrdFlUMHlPdXJKazhTX1NCVDJiRlhn?oc=5) <sub>MoparInsiders</sub>
- 📰 2026-10-06 [Volkswagen reportedly picks Wayve over Nvidia for next generation autonomous driving push](https://news.google.com/rss/articles/CBMi0AFBVV95cUxNMmtmMFpodDVWb09kY2pNZXprRWhCbTNfMUJhcndsTF81bzdibGxMTHhtaUtXS2FybWJaMmM0c3lxcEkwMVliNGZGeGtBSVo5YjEzMEVnLUpiMVBlX09pV2o3M2hucEI4SVdYNG1TQnJaVkhnaXJQSUdERV9zZ0duLW9LVGJ1YU9OVTRIb195SDdWVmVSNUxTNDlPTkNKcDF6NXJFOV9QZnRFS2tRX21pbkhLbXlzVDNDaW4wa1BZaXZzRFp6eFRXbWs4MUxBcDJ2?oc=5) <sub>Business Upturn</sub>
- 📰 2026-10-05 [Driverless taxis deserve a clear run](https://news.google.com/rss/articles/CBMiowFBVV95cUxNd3FabkJBaUdFd19oSGgwS1NpT3oyWDA0LTItOFlKMmdXOVFNS3VBQnpHbW0tYmFZR0xua0VkZ1hVcDBVTllPQnZTNnpPc3FTODJYbUJuYkJiTjM4c1lMV0FmdFprcHlvY01abW9Pb2RGNVBuclhmZzZaSzZndk1taUdTQ0RraUtZOFliNlpuQUpoWmctVGxzOVZSSTltQ3czSTQw?oc=5) <sub>The Times</sub>
- 📰 2026-10-05 [Volkswagen Hands Self-Driving Software Reins to Wayve as Model Offensive and Battery Deals Take Shap](https://news.google.com/rss/articles/CBMi3AFBVV95cUxOSGVyMTg1ZHE1R2ItUDlMNWVGUkJBN2pqTFk3STYxOVZCS1RjUHBRMk9zWFd5LXZUNGF1dUI5MGhfYW4tRmVkWW9PNkhacnk0MENteXc5YXozUndSWUdTOUFwZjBtNlNKM1NULTdfZmFHcmVKMkNUT0tUMGNFZ2FkMENtRTB4c1gtQXVWM3FlTzN2TWpxQkE0UFppeTk5c09UWERBNTcySVdfMWlLRUFPNXpIR3Y3OEc1c0RmdHZBa200YWVOYU1XZ1ZpUzNJZUoyX0ZKZnR5bTFwZWhF?oc=5) <sub>AD HOC NEWS</sub>

</details>

<details><summary><b>Momenta</b> (143)</summary>

- 📰 2026-10-07 [新上市的豪华插混SUV哪款值得买？6款近期智驾横评，全新XT5 PHEV入榜+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1iSGR0T01ZcGljNXI0MmtGcUZkMUtQZTdHczJxaEI2a2kycEZfS3pVcVVNdFZOZnNxQjBiMWI4MEFDQTRmMG1vSjhSZTlMcWhPcU04VWVZNlo4cmo1RzhZ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-07 [新上市的豪华插混SUV哪款值得买？凯迪拉克全新XT5 PHEV与理想L7、腾势N9智驾横评+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE9ua0lwNldMUW1OVTE0OXhCeHZqcDN2a2pFMnY2TUpfYTZBRDlaSVE1NldTZHYyTjdVOTA4LW9WMWV1ckdhVHJkLVBUT0M4LUoyUXBzc0xDalgydUYyQ2RqcmhMVDhHOVJJV0NjQ2VQV3Q1Zw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-06 [【视频】改写合资历史！神龙科技x Momenta！中国智驾反向出海！](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9yVGRXSWF1VGlkQ3FIempTYXBYYk1CTWJ3Ymhuak1EeEhNMlRNem1rNm9VOTNFT3AwQnhpSjgyeG9ZUUc3RFY4SUp0TmNucThudWZTMGl0NEpyVm8?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-06 [带激光雷达的豪华插混SUV哪款好？全新XT5 PHEV与4款智驾车型对比+FAQ\|SUV\|蓝山\|XT5\|R7\|凯迪拉克_新浪新闻](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1KWWpROXU2WG9BVGdvTU5sU01BalgwdEoyOC1MTHVfR2NyQU1ocmVUVWJDYkpkcU1ZbHdqV01HM3o1RllpUjBaTDZzMXNkMlRTX1hJcE1hNllmcHlCV2dV?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-06 [Global Robotaxi Fleet to Exceed 1.5 Million Vehicles in 2036](https://news.google.com/rss/articles/CBMirgFBVV95cUxORER1cUN0YnlmaW5oN2JXZmtIeTFMdWFaSk90LVY0SUdiRk05SFVnV2lld3ZMQmRqMEJGYlN2V0xHN2hadnlqYXhVYlAxNWFHRVBsQVYyVjFwNlZ0aURNakxROVVORE51QVNNT1dnbXU0Q1Q1ZElJcDBNRXFlb3dfTmxoY1pldEJMaUV3dXEtYnVxdmppNUVGMTVLMWdTb01LeEhrSG56N2hlakJVTmc?oc=5) <sub>I-Connect007</sub>

</details>

<details><summary><b>XPeng</b> (243)</summary>

- 📰 2026-10-07 [快充0.2小时对0.3小时，小鹏GX和澎程N90长途谁更省心](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9WQ1NPXzJHeXplV1hVS0w0SWQ2aU5tMkhzdXpKbHZXb1hQMHVVRk9rbjQwMUY4cThxSnRrMVdBam1uUFZKV3NqWkdDYWZaVlBVTS1tVzFIcWpFSmM?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-07 [3颗智驾芯片加6座布局，小鹏GX和奕境X9谁更适合全家？](https://news.google.com/rss/articles/CBMia0FVX3lxTFBSZ1JGbFZpdHdLUGYzUHpudmxEMFNaSllaVzlTUGVMTDR5UlRobklWSEVhNjVEdjJWanZfN1lDdmg3MU9pcGl6akNEX1hUczlOc2R2dzY5ZmtHLVNhZUdFMTJPWDhFQm02emIw?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-07 [20-25万增程车买哪款？小鹏G7凭续航和智驾杀出重围+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFBNMFhwM2FRbDlnbU81M1lVYzctMlNYb1ZudDBEV3FMTzRpemdYdnNDaGNqT2FWd1NZY052TDhFd0NqdmNvd2ZySGkyVm9rNFRlTXM0ZEdaNjlkcEhzZXZkMmFJLTd3NmtaVkxGX1J6azJZUQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-07 [【视频】1704km全球综合续航最长，小鹏G6超级增程上市18.68万元起售](https://news.google.com/rss/articles/CBMia0FVX3lxTE5PdXcyeDdyTk5MYWxPZFBKNk5rRjdxbURZczNVMkdZWWZaR3FmMy1iQjlhQ2Y5SXkwTDc1WURBQU11T05oNUVQUXFjMTNob2FrMWd5VDBhNmdLMlFIeVlLS3ZnVEZQTThaN3Nr?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-07 [【视频】10万级SUV颜值天花板？小鹏MONA L03法拉利前设计师操刀](https://news.google.com/rss/articles/CBMia0FVX3lxTE1fSVAzVHFUWVFlNWxZd0tWVmMtcVU1dVB3X3IyMEg2T1RSUUNNSlNVQmxsRi1EalRTWkl6c1AyXzYtbVBDbDd5cU5oRF95MXg4YWRSWFJKV3M1TUdLRDkxVkFZZU9LYVhzcW1J?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Li Auto</b> (174)</summary>

- 📰 2026-10-07 [Li Auto plans to enter Thailand by the end of 2026 as one more RHD market](https://news.google.com/rss/articles/CBMirwFBVV95cUxOM1BUTFMyZWVvZ285cVVKUXNfR2tEV3AzZXRWbGZ3NnJTZnFPNUJ6aUFaX0xOQ0RZQ2o3U1dBQjdoNWxFRG1xai15RFQtM1NwMElUazhuaXJTWHZWa184Zmp6MEtLRG01TTBjYm9FakRrZW4yNGNMeXpZVUNlY1U2dFU3ay1QSWlsazh0aWZCbEJfc1FVal9yWEZKa2FyblNXa3VZWVJQV0dzUTBvZVUw?oc=5) <sub>CarNewsChina.com</sub>
- 📰 2026-10-07 [限时28.99万起，集齐全地形+华为ADS5+800V？神行者8、领克900、理想L8三车横评](https://news.google.com/rss/articles/CBMickFVX3lxTE1zcUJibndCT1lOeV9GRDhqX3p3eUYzd3k5Y2pxR2xGQUtIZU9NaHZDQUNkRFRrZjdiQ2pFc1p1TmJpeC1yUUFJMzRwVEhSbEZLWC1IUlJmRnVZMjduQWtBNUFoWmNGalBuaTlvZVoxX3owUQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-06 [进入智驾模式都有语音提示吗？实测理想/问界给出3个关键答案+FAQ\|试驾评测\|suv评测\|新能源\|鸿蒙智行\|问界_新浪新闻](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1ZOVd2MVR6ZXYyOERqc0pwbzdwZHItcXZack13YnIwaEs0NEd2TmVPc3ZtbUFmeS1vSFUyOEFIOUFBbkRPZjRadS1pNWtrVWd4NzNRT0xPNzFEWHVhdVRF?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-06 [家用大六座SUV的“全都要”解法：对比理想L8、智己LS8与神行者8谁更懂生活？](https://news.google.com/rss/articles/CBMickFVX3lxTE9LOVVEcXNTZG8tWkRvWmJhcVVseWtxZDg4TktFTjN0MzAxcm53b2Rrb2ZlQ1YtTklJYjgyMnp1d2plS3lQR0pmYnNvRUhmem5SUVR2MmJuenpieG81QTlDamxlbHo3N2V3VEh3Qm42cnotQQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-06 [还在等理想i8？更廉价的理想SUV曝光了，很亲民！](https://news.google.com/rss/articles/CBMiW0FVX3lxTE13V0tJYVF5cXg4NXVrWGhSN1hyM1U0NndUSXk2MlpZcWFDa2huSUxPZFUtRTBGQ1U2MS01YzJVR2JjdFhJaGItMzljU0tMMkFuZEpPQUtBUm4zcEU?oc=5) <sub>车家号</sub>

</details>

<details><summary><b>NIO</b> (169)</summary>

- 📰 2026-10-06 [蔚来ES9值得买吗？4.3秒破百+3分钟换电，49.8万起的行政旗舰SUV深度解析+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1pYVppbnA4STB0T1J3VnVucEc0S0dXMXgwcFpvOExDTjd1bEI4YVdFNHFxRU1WVEozSWU0cmpfNklBZVpWdjdlckxYNHBuRndHNVNvTXBRQTB3dzdTbUNB?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-06 [20万级全能纯电SUV，配备蔚来智能三大件，2026款乐道L60适合家用](https://news.google.com/rss/articles/CBMiW0FVX3lxTE90VW00M3RjMEI3VXlLSHNOSF9FQ3BnZ2F6Z2RENk5qSkpLclo1c2ZYUDhYZWo3bUVYcjNqMVhTbWRhalE1a29UR05SWnFVUHNnZUdtN0hFWVlUNGc?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-06 [40万以上的智驾好的车有哪些？](https://news.google.com/rss/articles/CBMickFVX3lxTE9iM0FTSTNha1RNTDNxenBPZi1XRlJBY2Z4YzdkeWFsdXQ4UWdwRFZuVWItOXQ4Y09zSnBEWVVuclVPcUtZRnY5VFVDRlA1T0h0elVNTkxVeXEzcU1SdFVZV1U1UlZPTmhCYTBaNnJUal9nQQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-06 [蔚来EC7值得买吗？2026款轿跑SUV实测：设计、智驾、换电三大维度拆解+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE1tZER5X25VMHZWTXhVeW5UWWlVTnpvcUUtWk5nU0ZKek9YME9SY2hBQlZhaE5tRzNWMlVfUFN6Mk16azR0aXNZNFVCem5GdDVhd01QdTk3MVZ0czdIOU9TMkl0RFdhNW0xNHVyUFdNWWtqUQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-06 [【视频】买下！24年蔚来et5 外白内紫75kw买断行驶3万公里](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5wN0ZTOGJXT3RuMUFsWTZtMExKdnNxTVhEVlVGTzhPbnNFV2o3ZmRYSGV0R0xPd09nUmw0bHNhaHR3bG1mQVBIVXVsVmFuQ19YWU1BZVVDaEZoMXM?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Huawei</b> (387)</summary>

- 📰 2026-10-07 [Robotaxis intensify charging infrastructure pressure, could drive over 35% of North American EV power demand by 2030](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQc1hpZXEwa2hKWmRWXzNuUlJPSkNTSTEzZjJaOUJXSy1iZjlHbjFDbFdfUXFtR19ZSm5hUGJZdFhjMmVnY1M4bVNwS3RsTlpaa18wdjVKcHBXMFBxQXNPcVpxOUxTT2xYUDY0TUpRSXAzQVZSX2I5YzZONEhCUXQ1ODloaWlHYW1VSkFpRjVFNXVmZC1DZlFib2tBMXVMZHpIZjRaOUJUQmR6MUk?oc=5) <sub>digitimes</sub>
- 📰 2026-10-07 [99%都不知道华为乾崑智驾 ADS 5 有一个超人性化超越大卡车做法！](https://news.google.com/rss/articles/CBMigAFBVV95cUxOMlNseWp4Ykh2UUI0bmxJaVB3ZlBZNFBxRlAxTnk5WVhHcTlndEJONUNLeDJEY3BoczNncVhDU2RIbFNhU0pZSklFQVZBZElIWGk1WDlzWDNVaU1NWkVsd0VsdUMzWGhVTXhtM09OTlBlMWhTbGlla3BQMWVuM3NGaA?oc=5) <sub>新浪网</sub>
- 📰 2026-10-07 [深蓝S07值得买吗？15万级华为智驾SUV真实体验+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE5HWjlYZGNjTVVvdkp1UE9OZmlJUnQ4SmdpUWIwSUotYmxfOWctTjJ0Zm5yS3hkcENXcGFEamI0eklFLUJ3UmVReFlRVWg2UTJMeFktUXhPQnItbnNkODdiQWlmU1IzZk1kdGl6QzlmQmY5QQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-07 [【视频】30万级搭载华为乾崑智驾的MPV 岚图梦想家冠军版上市](https://news.google.com/rss/articles/CBMia0FVX3lxTE9oWXg4V0h2WDBRT1hOeXVLbm9RWm15Nm1jcE5kUjVMTHY1TXpYcE1VYnlZWmZFSU1qUU9rdjZFSmNfel90dkhUSmt3SThwWktGTFpZRHRqZ3dJei1DY05JcHJpMUVVOGV3NHR3?oc=5) <sub>车家号</sub>
- 📰 2026-10-07 [25万级华为智驾方盒子，猛士X700三版本我劝你这么选](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1VSlpxM2lIX2tSbnU0UTVWVTBWdFBIVUR4UmpzRUI3YTRhVzA3Mjg1c3NmTUdqTC11eE1sdE9EQXZ2Qy11SkkzcGJmWGJRZXBtUm52S0VjSk1Va0E?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Baidu Apollo</b> (52)</summary>

- 📰 2026-10-07 [Cathie Wood Bets Big on Flying Taxis With Joby, Archer Trades—Invests in TSLA Robotaxi Rivals WeRide, Pony AI](https://news.google.com/rss/articles/CBMi9wFBVV95cUxNSU1GeW9BdXZpVEd2Ym5vbEotR2ZqM1JYYl94S2tfX2EwRmpCQ3o2X0QxVENzVURaak5Rcjl3WjA3YTJTYll6T1doTi1yQ0txS0c5dHhQS3RaVHAtU1EyYmludG10aUEwZGpheVR6cnF6LUp2aWVTbjlycDQ0bHZKek1sWHFOOFFfa1BWRmw0N0FjQUpteWVhZThvSElGVnJHdkVYU21ZanFsczkwNkMwVlhIbXJlLTJnLXgwUXlKdkpBcHdCcGxWWTFYd2djREI2ZjF0aHdqZWQ2aGJXMUh3STNwRzRNZFRReXgyNncwcnFVSUpWdEFV?oc=5) <sub>Benzinga</sub>
- 📰 2026-10-06 [The technology of the robotaxi ...](https://news.google.com/rss/articles/CBMicEFVX3lxTE9TUFYtYVppbE4wZ3B2YWpoSjUxVEFQV1dXNHFYM1VDaXNUSHZWVEtpazdwRDNzcC1ZRU81SGJ3SExCYkJsOTBVV1BBWnc2V185SkNHWDdtRWEyQmN4MU1qQjFmZVQ3V3pKa2szOVZ2ck0?oc=5) <sub>eeNews Europe</sub>
- 📰 2026-10-06 [Global Robotaxi Fleet to Exceed 1.5 Million Vehicles in 2036](https://news.google.com/rss/articles/CBMirgFBVV95cUxORER1cUN0YnlmaW5oN2JXZmtIeTFMdWFaSk90LVY0SUdiRk05SFVnV2lld3ZMQmRqMEJGYlN2V0xHN2hadnlqYXhVYlAxNWFHRVBsQVYyVjFwNlZ0aURNakxROVVORE51QVNNT1dnbXU0Q1Q1ZElJcDBNRXFlb3dfTmxoY1pldEJMaUV3dXEtYnVxdmppNUVGMTVLMWdTb01LeEhrSG56N2hlakJVTmc?oc=5) <sub>I-Connect007</sub>
- 📰 2026-10-06 [深圳无人驾驶网约车全面实测：谁在跑？怎么叫？一文说清+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE5uZWJzTDJwbjBiLVROdkZSdm8zaUxnaDM1TnJ4c1dUYzNQZTBGellhOWdVOERLWjBuckdjUzVKY2w2eFJCVVZHVEJzNFl5dFZReHhYUWlIdEVKV0VyNWhSalFHVzd5UVgzYjR3QzdoSWIwZw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-05 [Global Robotaxi Fleet Set to Reach 2M Units by 2035](https://news.google.com/rss/articles/CBMiogFBVV95cUxNMXRqMzNocUlfUGtIM2NuTUgyVXBTRVdocUJTalhVR0VGeXY3OGpMdkdOTE5HM0U0U0o4MGFBbEJGSFVxRlFHRFFYaGlKXy14elR3ci16b2hiRnlrZU8tWTg1VFpIWWlEYkNOOGV4N0pNR3dCWHNpNFlOZVMwN1ZLVm9NTkxxT0dmVVM2NnE1S3RlS1N5WFhnYlhhdjdHbUp0QXc?oc=5) <sub>Electronics For You BUSINESS</sub>

</details>

<details><summary><b>Pony.ai</b> (119)</summary>

- 📰 2026-10-07 [Cathie Wood Bets Big on Flying Taxis With Joby, Archer Trades—Invests in TSLA Robotaxi Rivals WeRide, Pony AI](https://news.google.com/rss/articles/CBMi9wFBVV95cUxNSU1GeW9BdXZpVEd2Ym5vbEotR2ZqM1JYYl94S2tfX2EwRmpCQ3o2X0QxVENzVURaak5Rcjl3WjA3YTJTYll6T1doTi1yQ0txS0c5dHhQS3RaVHAtU1EyYmludG10aUEwZGpheVR6cnF6LUp2aWVTbjlycDQ0bHZKek1sWHFOOFFfa1BWRmw0N0FjQUpteWVhZThvSElGVnJHdkVYU21ZanFsczkwNkMwVlhIbXJlLTJnLXgwUXlKdkpBcHdCcGxWWTFYd2djREI2ZjF0aHdqZWQ2aGJXMUh3STNwRzRNZFRReXgyNncwcnFVSUpWdEFV?oc=5) <sub>Benzinga</sub>
- 📰 2026-10-07 [科技消费新趋势 \| 12公里18.5元、4次无保护左转……深夜体验第七代Robotaxi：从留意它怎么开，到悠然坐一程](https://news.google.com/rss/articles/CBMioAFBVV95cUxOSkNEVmNRNEVjS3JReDIwVzVlVUpKdHR3YktFWERzc1V0bnlieV9INmVKQ2RwODMyU0djWVhYUU5jeG93RHFSaDhWYV8tTUo5ZEkyb1dZdmlLSTZ1elVoRUUxVDlhSTcxNDNHdjFXR1lHU25MeU12NGh2amlON005YmNEQ1BWR1E4cGJGa1pMbHhqQ1ZRdmdicHpUMk5fcExW?oc=5) <sub>新浪财经</sub>
- 📰 2026-10-06 [Inside Europe’s new robotaxi service: A ride in Verne’s driverless shuttle](https://news.google.com/rss/articles/CBMihwFBVV95cUxNTFNUWGZDWTJ2eklCM0ZpaXFvMGw1bEdYNDJycW9jWGphWnhHenhjZFVvRC1fLXhzTnhWWnFlaUZsWF9qS3ZpdmhPTUNjQ1JmaGFadHY3YlZFaGhiaFA2S0t4RThKbGR5SWg5c054NDdiWlFHWWNCQTR2dWJKdmxqcy1zYk53M0E?oc=5) <sub>Automotive News</sub>
- 📰 2026-10-06 [Waymo Boosts Private Debt Deal to $5 Billion in Push for Growth](https://news.google.com/rss/articles/CBMiswFBVV95cUxPdE02V0J1WUxHU09MaUNQZHk0cndQWk5mV1VVdG9hY0JLamRrRjQzVEdzYkNhVldEWFN4U0NZc20xV3I1UTlMcnZPMEpLZW1YZTNtWDhVVHpVUUIxaTJGSEJUV3RUZ3BvV3VaUEswbmpnUERsazRIYk1vQ0FuX3JSS2V3NUx0NXNvQi00V2dweDRfOWdWbDBzajQtbExJcEY5c2VfcF9EYWFrbDctSGJKRG03TQ?oc=5) <sub>Bloomberg.com</sub>
- 📰 2026-10-06 [Global Robotaxi Fleet to Exceed 1.5 Million Vehicles in 2036](https://news.google.com/rss/articles/CBMirgFBVV95cUxORER1cUN0YnlmaW5oN2JXZmtIeTFMdWFaSk90LVY0SUdiRk05SFVnV2lld3ZMQmRqMEJGYlN2V0xHN2hadnlqYXhVYlAxNWFHRVBsQVYyVjFwNlZ0aURNakxROVVORE51QVNNT1dnbXU0Q1Q1ZElJcDBNRXFlb3dfTmxoY1pldEJMaUV3dXEtYnVxdmppNUVGMTVLMWdTb01LeEhrSG56N2hlakJVTmc?oc=5) <sub>I-Connect007</sub>

</details>

<details><summary><b>WeRide</b> (110)</summary>

- 📰 2026-10-07 [Cathie Wood Bets Big on Flying Taxis With Joby, Archer Trades—Invests in TSLA Robotaxi Rivals WeRide, Pony AI](https://news.google.com/rss/articles/CBMi9wFBVV95cUxNSU1GeW9BdXZpVEd2Ym5vbEotR2ZqM1JYYl94S2tfX2EwRmpCQ3o2X0QxVENzVURaak5Rcjl3WjA3YTJTYll6T1doTi1yQ0txS0c5dHhQS3RaVHAtU1EyYmludG10aUEwZGpheVR6cnF6LUp2aWVTbjlycDQ0bHZKek1sWHFOOFFfa1BWRmw0N0FjQUpteWVhZThvSElGVnJHdkVYU21ZanFsczkwNkMwVlhIbXJlLTJnLXgwUXlKdkpBcHdCcGxWWTFYd2djREI2ZjF0aHdqZWQ2aGJXMUh3STNwRzRNZFRReXgyNncwcnFVSUpWdEFV?oc=5) <sub>Benzinga</sub>
- 📰 2026-10-07 [激光雷达+702km，埃安Ray7把料堆满只等价格揭锅](https://news.google.com/rss/articles/CBMia0FVX3lxTE9tanJSWHF6enkxN3oyVkNCLUoyQXhMSHp3LTlnZHFEV3NRdDhaVnpnQklBUjlYTk9TYk1VOERnVllad3lwSFZfczIyTkQ0UFNsQ0ZwQURuRFh3ZzJPRXFPQ0NLdm04YlFrNVJ3?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-06 [部分港股人工智能相关个股延续涨势 傅里叶涨近16%](https://news.google.com/rss/articles/CBMiYEFVX3lxTFAwd3dKYVlMU1ZxM21VUEpGZFBFOUpZeGhBR1VCQmJoQ245RDVIQVZrdUZoTGctYmpBbk93ZmdyYXlXZGs3eXBZLUpkTUhLemF6TGZva2wtam9GaVZIMEMxXw?oc=5) <sub>东方财富</sub>
- 📰 2026-10-06 [Robotaxi Fleets Could Scale to 1.5 Million Vehicles Worldwide by 2036](https://news.google.com/rss/articles/CBMirgFBVV95cUxNR0tJMjYzanZsUFFveWM2dFduWW9HdnBPNzNQT0E3YXY4U3l4QnpZUE9LVkF1NUF1X1ZIN0UzLUgyS0hfYjBnSDQyZFZZMFJNSXVINlp0Q1NTZnN4VFFubkhOeTM5WXpwcVZ5ODR2QUhuRFRKQnlrYWMyUHVRdnhpOFdTUFhfVmZ2LThfWEg5VG9UeV9oT05iOGUtbnAtQzlpWWV5OU9tNEluTTdNaEE?oc=5) <sub>IoT Business News</sub>
- 📰 2026-10-06 [Global Robotaxi Fleet to Exceed 1.5 Million Vehicles in 2036](https://news.google.com/rss/articles/CBMirgFBVV95cUxORER1cUN0YnlmaW5oN2JXZmtIeTFMdWFaSk90LVY0SUdiRk05SFVnV2lld3ZMQmRqMEJGYlN2V0xHN2hadnlqYXhVYlAxNWFHRVBsQVYyVjFwNlZ0aURNakxROVVORE51QVNNT1dnbXU0Q1Q1ZElJcDBNRXFlb3dfTmxoY1pldEJMaUV3dXEtYnVxdmppNUVGMTVLMWdTb01LeEhrSG56N2hlakJVTmc?oc=5) <sub>I-Connect007</sub>

</details>

<details><summary><b>Horizon Robotics</b> (185)</summary>

- 💻 2026-09-29 [HorizonRobotics/Ego4WAM](https://github.com/HorizonRobotics/Ego4WAM) <sub>GitHub</sub>
- 💻 2026-09-24 [HorizonRobotics/CogWAM](https://github.com/HorizonRobotics/CogWAM) <sub>GitHub</sub>
- 📰 2026-10-07 [铃木轻型电动车e-Sky将于11月在日本上市，搭载比亚迪电池与地平线智驾芯片](https://news.google.com/rss/articles/CBMiWEFVX3lxTE93X1RxVUlQN0hJZHJBZ0VCSWFfWDVqZ3c4NVlPZG5ELWVWemVhbHBzeXF1RnlQZ2ZpQXFPcGQ3OGlTd2l0NmluejBwWlZJV0dkUGxvUnROWGY?oc=5) <sub>网通社</sub>
- 📰 2026-10-07 [【视频】iCAR V27零百5.5秒，比理想L8还快？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE42QndxYTZia09BZFh0TVVzNWU5VVloUGpZLWZkcnpRRkRtbTNmWTc1V1VuczhrQkNlRFVQczNpVmxfNUZxSTBLTm1IYlRQQVBkV01zb3lzQXFOMFk?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-07 [【视频】做汽车界的iPhone ，iCAR V27专为破局而来](https://news.google.com/rss/articles/CBMia0FVX3lxTE1xNUhiT0xoZmNEY08zQWlZR2Z2NW14N084RWRzYXgycXVDZXpVUWFHQkY4UERWd2M0YXN5eTRtQ1V3SEIyNDFSUFA4LVE1bVB3WDdlaDcxVjRDRU1XR3JpRk5EcFZmVGRtVU9j?oc=5) <sub>车家号</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (26)</summary>

- 📰 2026-10-06 [黑芝麻智能(02533)股票股价_股价行情_讨论_资讯_财报_数据报告](https://news.google.com/rss/articles/CBMiP0FVX3lxTE5PM3NHQmFOaHR3anl3OURLOVQzRm1qemJTYl9kN29GRFZ1Y1c0Y1VrQ25mTHBOQkFMVXE5cmYwNA?oc=5) <sub>雪球</sub>
- 📰 2026-10-06 [【视频】特斯拉Model Y L 2025款长续航全轮驱动版](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9lN2x2MGx5NWdINEEwbHFXdUc0amd4czh1SllPek4yZG9XdjZPemxpSUp1OXQ0V1hOTjBRUW9yTE9HeWN1X0VPclNKdzVzMmh0d3RlVjF6N3hWVWM?oc=5) <sub>车家号</sub>
- 📰 2026-10-03 [赛豆科技首款车型—AIVA ME7正式首发，采用时下流行的轿跑SUV造型比例，并且配备大尺寸的轮圈与多活塞卡钳，车尾还配备镂空扰流板，预计是一台主打年轻运动的产品。结合此前的消息，这款车会融合豆包大模型以及火山引擎生态，并且有报道称其辅助驾驶将采](https://news.google.com/rss/articles/CBMiY0FVX3lxTE4tU1hIOTd3MWtGSUV0RjZPR3pKRTNVTGNzaXpkenphcG5FVk1pNnZZMGdIUy1TVi1SMW9JdV9KMjFPYXlqakw3MmhObmtMZVB2VlVob2RoaFJTcVFsU09OTnFVNA?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-03 [提供豆包大模型将覆盖20万元以上主流市场AIVA ME7全球首秀_热点推荐](https://news.google.com/rss/articles/CBMiYEFVX3lxTE83MUJRVjJpdG92N0xFSUpkdHlsMWdWQlpaWE1CYzQwblNiOFVMVURPRFZ0amZQTXNpdl9odkpOSk9SZVAyWDhadnBXbWozTHNjOXNkRmRRS2dXbV9BQndHMg?oc=5) <sub>证券之星</sub>
- 📰 2026-10-03 [又一AI原生车！AIVA品牌首车ME7全球首秀，量产或假以时日](https://news.google.com/rss/articles/CBMiW0FVX3lxTFA2cVdGVzNJZlBpODJxZXJnVlVaOXFjQ3gzcTRUOHhibHZ3VlAtYWIyWnFHQmRPbUdFd2lsWGtPLXpfRTZoMGhOcF96am1CeklVUnRTS0RFZkpEZ2s?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Mobileye</b> (21)</summary>

- 📰 2026-10-05 [Moia’s autonomous shuttles start first passenger tests](https://news.google.com/rss/articles/CBMilgFBVV95cUxPaXBLWlk2ckZabm9UeXdOV1lCZTRjaDBkVmk4bDNVRWVMZkxKUEVTOVBqZERzWGlySkROdEs0bkE3SURjaG44c1Y4M3lsM0NmSG95X0diNlY4cGJoMUp1UUMxVnFkQ2Y0UTR2UDdtdTFzczBDSHpId3ZmWDltWlY3Ulg1bHBYMzJweHhDOWkzd3lyVWwxSGc?oc=5) <sub>electrive.com</sub>
- 📰 2026-10-03 [We Found Atoms, Rode Wayve and Watched Uber’s Autonomy Clock Speed Up｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1QZjNLZlpHR2ZtcHFaUDF5bEE3ZktHQlNoN0E1amxaVEg0eUdQbElIVlVVZk1JdTlqZG1kbGZYVTBvZDdKRDRKVWlqa2dRNDF3aTN4dEpmdTdxX0dTVnlj?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-03 [What Mobileye Global (MBLY) Could Not Prove Before The 49% Fall](https://news.google.com/rss/articles/CBMi0wFBVV95cUxOTDFoVXlyNjVvYmJycldRVUhaOHNieXV1MGJlRDVWWlVmUXVPMUY5NUlHWV9PcTYyYlMxWGNxRXk2c3R6b293RThGVW9ONFBBaUtqSkJsRl9MNjRvVVAxRW1WdGdrUXRKaDJqS042RDBXODB5YkoteU5USVlhdlBfS3pGcnlpVzZ0al90dm51WndmSGNCSElQWE9JY3hHaVJhMFZTSGpSMDVuWGQ2ZWtDQVlxVUFHeHJRVFJNclNaS2RLR3RsQnZ1c05rQjZseGhSVzVj0gHYAUFVX3lxTE9LbTQwSTVOazZ1ZkxtRXhjdm5qSjluZjlEandjc3JUdWNkRGdwbGpYdmhNM0NIYlRrQjlMdnI4ZWZGM2FHOUV6SHF2TnJJMDlWTktBWEluVnVQZ2FFYU5WMUF4WS0zSXRmbkRDQzEyVmFUNmJzTFZwTzZDVEFIcXZVd3BLZUFHa1daeDdBako4ZFVseEVsSzE4UURFSmQ0Mnl4V01HZHdybXlFNXFIelVJMURQNC1GNVJKSXgzMTkxenhxLVB0dFlxc1FJLTBzMmh2UzJjaVhKMQ?oc=5) <sub>Simply Wall Street</sub>
- 📰 2026-10-03 [Grayson Brulte: Zoox Has an Intersection Problem, and Uber Has 18 Months to Own Its Autonomy Stack](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9Gbmp2RTY3bW1WaFdrMDhqeWVpUHR0WXNEcFA2eWk4Ukdidmx4bXp4ZmdoNFhUWGZoM2pTNVBCVUlJSUl4SVM0UlcwbERnMTNVYmlxTjlxYXBwV0k?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-02 [Mobileye Global Sees ADAS Momentum, Eyes Porsche Launch and Robotaxi Expansion](https://news.google.com/rss/articles/CBMi0wFBVV95cUxQYzRBUnBoMFNxTkNkYjFDNl9YbVpSRTVwb1N5SjFjMm56dEFiS0I2amZUQ1JqMHFTTlJHb2N2bkhlUXhOaTRpbHJIWWxhWWVBeUxsdlZ1bUtTdzRsZEUzV2NHWUpaVnN2ZzljWnhZSnlibjNHNjE5M1pyc21xekJGM1A3Z3V0SGZRVTVGSG1hMm9DWVlnSUhBQ3hKNk9yQjBZUU12bXN3MUFWc3k1XzZKXzZIeGh5bEVZaXpta3cwMjVHUGxlaHRINGhKdnhERU12TkRN?oc=5) <sub>MarketBeat</sub>

</details>

<details><summary><b>Aurora</b> (49)</summary>

- 📰 2026-10-06 [The Autonomous Trucks Are Coming for the Lane, Not Necessarily for Your Business](https://news.google.com/rss/articles/CBMingFBVV95cUxQcnJrUkNaRUxZb3NXeGJ0dTJfSjg1VFZjdWw3MDMtX2ZjOEtaNE9RVGpzUW9WQl85WE9YdGNoRms4ckFDdnNscWFaNjFRUFFOaW9zYVBNUU0tcVJqZzVrb0hWTExBQllaZVJ0Y08wY3U3QUdHaWV1eG1YRkU2RUN3aDJjQXRndUZuemFaNG43UTh6aXFqbjlud01Fckxldw?oc=5) <sub>Yahoo Finance</sub>
- 📰 2026-10-06 [Volvo and Waabi Launch Autonomous Trucking Operations in Texas](https://news.google.com/rss/articles/CBMi0gFBVV95cUxPT3Zub0diNmp3T2NJb3ZuYmVMajhpVXYxOWZVYklZVDc1SEFxZFdSVnVCMlcwaWtZLS1RS3lxUjlEdndwMGtoTVByMXZxWW83Y1RJdmdHNmVIMms2VjEwRHQta1UxNlJYdTVKNDB0b0hYTkJheVdWSGVXbVZwV3JkNEJSZVkzWjFZUll6dXRNVllTMm41TENuQnFJeUdnNDVnV1A2MnV4Q2ltWkNHU3c3TThQZ1BMdWo3dEFHRGRqeW9UVkdqOXRneWFIeTdWV3hRNUE?oc=5) <sub>Commercial Carrier Journal</sub>
- 📰 2026-10-05 [Another autonomous trucking company hits the road between Houston and Dallas](https://news.google.com/rss/articles/CBMilgFBVV95cUxOQ2tLdXlkSUVHNFhBQ0lZV0VRamJDWGdLVDkxeEVsYkh6aXBmSW41ZkQ4VFQ0bVZqbEFWM1NjSVFBOHNBT0s2TGNDX3l5X1M4ODZNRktxcjFfT25DZkhZS1JJQzJUYXZ0V2tNYjRQUm9LWEsxbEpmOUhQSE5HcFFzanpWZkJ3NTM2X1pTWWNsZTM4cU9ldXc?oc=5) <sub>Axios</sub>
- 📰 2026-10-05 [Truck Accident Lawyer Explains Liability as Self-Driving Big Rigs Hit California Highways](https://news.google.com/rss/articles/CBMi2wFBVV95cUxNRzdPUGxqemFTV3hhMmlpSXB3cXNxS29LdkFZcXVTQ1ZXdDRqR1VPTkdsaTc4LTU0djIyb2xPMEoxLURYQ25zQWhxRGp5SmVKTThaUEpkeXlUclQ0Mkk4dG9iaDIzSGQwNWFPRTI1dDVsa2FMTFRkbEJhRms5WGZ5QlQwc2pjbDNrZ0VpX3pVZG1ZRXRJcHh0Zmg4Y2Nra1k0QXpvQXBPVnhtaXpkdDl5dmJ3dHBjaVcxb2p4M1NXaXZxeE5vNEpiTVhOajRkV1RUaUg2bWxlOVJhdmM?oc=5) <sub>24-7 Press Release</sub>
- 📰 2026-10-05 [Volvo, Waabi Launch Autonomous Freight Runs From Dallas To Houston](https://news.google.com/rss/articles/CBMingFBVV95cUxQSVJNREZabFlHQzFRdk5IM0MzUTNTOVkwU0xMWXVkaUdTV2lPN3FTamZELTRvZ3dUX0lHNzZEZk5jN0FpaUJEcFpWeHdaQnB5NjlXdjdMZGlmZHpTUXB2ZXROcmR6U0NZNnhweGhMS2loaVRORlA5ckgyeWVfbjVkVlhMLWkyUXF0OGJwVjN6NXh1X2pxdkJLd3MxYUFWZw?oc=5) <sub>Dallas Express</sub>

</details>

<details><summary><b>Zoox</b> (90)</summary>

- 📰 2026-10-07 [My Verdict on a Robotaxi Airport Ride: Relaxing, but Really Slow](https://news.google.com/rss/articles/CBMirAFBVV95cUxPNFFERWVlTV8wWTFDcGFUMFBlbkxqTnQ4WTRlZnZsdlVqNXVOT0tqRDVWUnhRaXk5VW9mbGRUMFRpODBOTXk0M1RRaXBEbU5EaGhfMjRmS3pBaHJLN21EWTF4dEU2aUs3Wk0tQW5TTC14T1NnMGN4aWFkMUNzd3N5eHYzeDZYR0E1d0tjNjJZM0VqZUFOQXVuWTAxcFBxOFdhZ2p0dHQ5U0tCQ1la?oc=5) <sub>WSJ</sub>
- 📰 2026-10-07 [Waymo Robotaxi — Safety Concerns Rise Amid 210+ LA Collisions](https://news.google.com/rss/articles/CBMie0FVX3lxTE9BUUpkbmRHeHhYdmllc3B2Nklxdkx2cjQ2RUtXX2cwM21JNFhTMXM5YWxNRWVEMWJXZXRrNnNsclQ2VkNFc0lLWTFkSE1CVV8ta0VCY2VCODlhX2loTk8tOFRxLU5CMENFaTdndkpUeDBhMk9FOWZsVWNjdw?oc=5) <sub>The Korea Daily</sub>
- 📰 2026-10-06 [Waymo Boosts Private Debt Deal to $5 Billion in Push for Growth](https://news.google.com/rss/articles/CBMiswFBVV95cUxPdE02V0J1WUxHU09MaUNQZHk0cndQWk5mV1VVdG9hY0JLamRrRjQzVEdzYkNhVldEWFN4U0NZc20xV3I1UTlMcnZPMEpLZW1YZTNtWDhVVHpVUUIxaTJGSEJUV3RUZ3BvV3VaUEswbmpnUERsazRIYk1vQ0FuX3JSS2V3NUx0NXNvQi00V2dweDRfOWdWbDBzajQtbExJcEY5c2VfcF9EYWFrbDctSGJKRG03TQ?oc=5) <sub>Bloomberg.com</sub>
- 📰 2026-10-06 [Atlassian Williams F1 Team Fan Zone presented by Kraken returns to Austin in 2026](https://news.google.com/rss/articles/CBMi6gFBVV95cUxOWHFEcGNSSVB0ckEySzJsR3JiZ1BWRHg5VlFnNWdzMDRlSWtfZ3lLM1ZKTW5YcERoNGs1SDVUNEVXSkY1WkZVZU0yMHNHVmptbFA5Z1RsT2ozQ2JZeU1xWEgzREpTN2ZaUGMyZUFnQmVBUlUyeVFraktSMWRoeWZ5dDlLNU5LQlVQdkZGWXdSYkU0Y2gxNDQ3em5fb3M0QXE3dlRGUVRQQ1d6RGNoUTZ4d3h2d0lOQ0xueVlQekNhZG9TV3I4eXF4Vm1kdWwzVTZRWlJTUXYxYWJJNl8zbXJFVFJJRFFUeERFNmc?oc=5) <sub>williamsf1</sub>
- 📰 2026-10-05 [More robotaxis, more crashes: A dive into data](https://news.google.com/rss/articles/CBMif0FVX3lxTE1fWXcwd0FUb1VCbDNnN2ZfeU5IZWJrd004YjVYMVdVNkh4OGFfQk0xX3J0cjE0WVZrUURTUlU4eFE2bUJTRnBBODZveVFIcWE2WjUzYXJrVDliR0g3cVFpOWJQMjZvMXc1QnBrVW8xMlFvcDJIQXpOM2lwa2NUYUU?oc=5) <sub>PressReader</sub>

</details>

<details><summary><b>Motional</b> (39)</summary>

- 📰 2026-10-06 [Robotaxi race pits camera-only Tesla, sensor-heavy Waymo, and Korea’s Hyundai - CHOSUNBIZ](https://news.google.com/rss/articles/CBMiggFBVV95cUxQcF82S1VlVzBzVUxVXzdYNlJydlJldEtmUnlJYzNEWVE2OU1kYWM1aVZ4TDg1dU1oeEFWc29UWE0zNmtOSGk1OE55QnNhS3pKS0lYMENDZGxZQTRXTUF4NmdvZG54NV8zZ0V0UHBDb1JPRE9mQk5zX3Jvc2RxYzVNVml30gGWAUFVX3lxTE92SGMtS044YXZyaUM3QVMwT2c5ZXZrRUdoSXVJOG9UREJwcHd4NklmbTdVVmNINmJSM2lyM2VEdkhvZTNOT3Q0VXVxcmFxU0szamRLSDgwOFdrUjQxNmMzZjY2VG82WWxuM3cxRnE3Z2o2TXVoZ2pEV2hCbUxnTzZmdUxSV2tmc2FDV0lxMHVzS21na1NMQQ?oc=5) <sub>Chosunbiz</sub>
- 📰 2026-10-06 [Global Robotaxi Fleet to Exceed 1.5 Million Vehicles in 2036](https://news.google.com/rss/articles/CBMirgFBVV95cUxORER1cUN0YnlmaW5oN2JXZmtIeTFMdWFaSk90LVY0SUdiRk05SFVnV2lld3ZMQmRqMEJGYlN2V0xHN2hadnlqYXhVYlAxNWFHRVBsQVYyVjFwNlZ0aURNakxROVVORE51QVNNT1dnbXU0Q1Q1ZElJcDBNRXFlb3dfTmxoY1pldEJMaUV3dXEtYnVxdmppNUVGMTVLMWdTb01LeEhrSG56N2hlakJVTmc?oc=5) <sub>I-Connect007</sub>
- 📰 2026-10-06 [PIMCO Sees Treasuries as 'Screaming Good Value' After Yields Hit 24-Year High](https://news.google.com/rss/articles/CBMidkFVX3lxTE5sdDZFa3JYaFdrSlFWdks4TWVYQ3lhbFJEanlPaEJPX2lUdnlTaE5wVGtUNjVJTV94c3NyUC0xTzhRVy10a1ZZUGNBY1NwalI0bExTTHMwVGZxRlRIeE1nQlNUeUFhWXFMN1AtWFk2dTZDUjBTTHc?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-06 [Ripple to Provide Institutional Prime Brokerage to Brevan Howard, Accelerating Wall Street Expansion](https://news.google.com/rss/articles/CBMidkFVX3lxTFBoZm12LXI0Wmc0UlRKSzlWTW8wU1RvT1RGb1Q3RnRlOExpUmVqa3JJNEpVQ2J4M24xRlJ4WkV3SEk4X011LTdHemdoQXp2R1ZONERuVGN1VFZOR3dtd09yUlo1QzFmcEh5dG1OU25UbjJuT1RMQXc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-06 [Volkswagen reportedly picks Wayve over Nvidia for next generation autonomous driving push](https://news.google.com/rss/articles/CBMi0AFBVV95cUxNMmtmMFpodDVWb09kY2pNZXprRWhCbTNfMUJhcndsTF81bzdibGxMTHhtaUtXS2FybWJaMmM0c3lxcEkwMVliNGZGeGtBSVo5YjEzMEVnLUpiMVBlX09pV2o3M2hucEI4SVdYNG1TQnJaVkhnaXJQSUdERV9zZ0duLW9LVGJ1YU9OVTRIb195SDdWVmVSNUxTNDlPTkNKcDF6NXJFOV9QZnRFS2tRX21pbkhLbXlzVDNDaW4wa1BZaXZzRFp6eFRXbWs4MUxBcDJ2?oc=5) <sub>Business Upturn</sub>

</details>

<details><summary><b>comma.ai</b> (46)</summary>

- 📰 2026-10-06 [AI Agents Tried to Drive a Corolla, Crashing on 8 of 11 Runs](https://news.google.com/rss/articles/CBMiuAFBVV95cUxONWxQTEZham1kc1J4S2lMNUh6OTN1QWhXbl92U21NUWZTZWhNUUdwcFVvUHYtVWJzSjl4TjlCeFhUY2ppMXd3WkkxaHJFRmFlNUN2NGFSSENnV2ZZYWRNZ3JIUjd0dzFlTS0wR3gtbmxXN3VHOUkxWWg2VVFpTVgzWGN2T3RPdEFJV0cyWjRPSVFyNWZTYjFyX0pzYjFEUWQwLUlfbGo1bm8xVUZXQmpyQ3pCNXV5ZE9x?oc=5) <sub>thetruthaboutcars.com</sub>
- 📰 2026-10-05 [Researchers Discover ChatGPT Can Drive a Car. Grok, on the Other Hand…](https://news.google.com/rss/articles/CBMikgFBVV95cUxNNnNwX0g5bHV4STJlMXNOcXRnYnBHWHNoelViM2pJSzFob3dvUVJIdFlDRDV4X09DSVloZmxCTk5NODd3b3RBR2JmWEJQRktXUTYyWDNveS15UEw0NnVfSFluMlJxZHlBb3NhYnRNdDJsZ01MbVNpOXY4OW9nQnBSYnFRQ1U2YVd3a3R2ZTY4VlJNdw?oc=5) <sub>The Drive</sub>
- 📰 2026-09-30 [A $999 Box Promises Hands-Free Driving. Its Own Code Says ‘THIS IS NOT A PRODUCT.’ Now NHTSA Is Investigating Crashes That Killed Three.](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPNFIyamduTmQxb1dKNlh5Z1hCYUhyemoyU2I2bjFUWjZQSDVFSDFWOGxlM1hnQms4Q1lpalg0bXlCTEZTdVJ3eGtNTjlLamY2eW9LX09IejF6SkJxSmZ2QjRkU1pUczlRY2g3cUZIN3hvSUc3a3pUWHVKVk40MlY3Wk5SX3dnOHBl?oc=5) <sub>Yahoo</sub>
- 📰 2026-09-30 [The $999 Driving Gadget That Just Landed In Federal Crosshairs](https://news.google.com/rss/articles/CBMicEFVX3lxTE5kRFFmYXdUcmRRZ2wtNzF4QlRqQ0o1UmVscVhPWFlsVVE3S1dRVWdtLWFsOFJYeUlHY3phaWZYejBnWjFvVmxTcEJNRVBaQUJscU1VODZvRmxrREVYRDUyZlNJdTNsMUN4MmkwYXY1TWs?oc=5) <sub>HotCars</sub>
- 📰 2026-09-30 [Federal Probe Opens Into Aftermarket Self-Driving Hardware After Three Deaths](https://news.google.com/rss/articles/CBMiqgFBVV95cUxObDZzR1Z3QnZLaDR0bTRldUFvc0ZESTBoUHIyZE1PSmJHWFR4MmdrTi0zWkRFT250VG5WbTNuTWd4dzV6R1FIYzV2NzI2NGlfMzkwdHBTZFdIYkxpNG9pWldBQjdxTF9OOTFiZ1M2RlVfaFlkNThCRk41c21ZcXRsalFfOXpqTXRhYVRhaVREaFRRamMzcE41TGNMVTA5azFDWWxCalpHNkdCUQ?oc=5) <sub>Gadget Review</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
