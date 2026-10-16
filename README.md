# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-10-16 · 1,289 papers tracked · 40 curated.

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
| [Teaching Vision-Language-Action Models What to See and Where to Look](https://arxiv.org/abs/2607.01658)<br><sub>Yuguang Yang, Canyu Chen, Zhewen Tan et al.</sub> | ECCV 2026<br>2026-07<br>📑 1 | [⭐ 33](https://github.com/ShivaTeam/DriveTeach-VLA) | Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving |
| [DeepSight: Long-Horizon World Modeling via Latent States Prediction for End-to-End Autonomous Driving](https://arxiv.org/abs/2605.10564)<br><sub>Lingjun Zhang, Changjie Wu, Linzhe Shi et al.</sub> | ICML 2026<br>2026-05<br>📑 1 | [⭐ 31](https://github.com/hotdogcheesewhite/DeepSight) | End-to-end autonomous driving systems are increasingly integrating Vision-Language Model (VLM) architectures, incorporating text reasoning or visual reasoning to enhance the robustness and accuracy of driving decisions |
| [SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving](https://arxiv.org/abs/2610.20609)<br><sub>Shaoyuan Xie, Zihan Zhang, Jingxuan Wang et al.</sub> | CoRL 2026<br>2026-10 | [⭐ 19](https://github.com/ASGuard-UCI/safedrive-vla) | Vision-Language-Action (VLA) models are gaining attention in autonomous driving, inheriting commonsense priors from large language models (LLMs) and widening the navigation interface from a fixed command set to free-form… |
| [CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving](https://arxiv.org/abs/2607.04179)<br><sub>Zhaohong Liu, Hao Ye, Xianlin Zhang et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 1](https://github.com/MICLAB-BUPT/CritiqueDriveVLM) | End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving |
| [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)<br><sub>Nan Yang, Zhanwen Liu, Linfeng Zhang et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 9](https://github.com/Zizzzzzzz/MVPruner) | Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings |
| [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)<br><sub>Yuan Gao, Wenting Miao, Mattia Piccinini et al.</sub> | IROS<br>2026-07<br>📑 1 | [⭐ 27](https://github.com/TUM-AVS/Chat2scenic) | Validating autonomous driving systems requires diverse, regulation-compliant test scenarios |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 9 | [⭐ 514](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
| [Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air](https://arxiv.org/abs/2605.31066)<br><sub>Tianle Zeng, Yanci Wen, Xueang Yu et al.</sub> | arXiv<br>2026-05<br>📑 2 | [⭐ 1,115](https://github.com/louiszengCN/CarlaAir) | Recent aerial vision-language-action (VLA) models show promising single-UAV capabilities, such as tracking moving objects and navigating to language-specified landmarks |
| [GRAVA: Grounded Reasoning-to-Action Representation and Learning for Autonomous Driving](https://arxiv.org/abs/2609.15169)<br><sub>Xiao Liu, Haoyu Li, Jianghao Leng et al.</sub> | arXiv<br>2026-09 | [⭐ 202](https://github.com/AhernResearch/grava) | Driving vision-language-action (VLA) models increasingly reason before acting, but their intermediate reasoning is often weakly grounded in physical scene evidence and loosely connected to executable behavior |

## World Models & Generative Simulation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [HERMES++: Toward a Unified Driving World Model for 3D Scene Understanding and Generation](https://arxiv.org/abs/2604.28196)<br><sub>Xin Zhou, Dingkang Liang, Xiwu Chen et al.</sub> | ICCV 2025<br>2026-04<br>📑 4 | [⭐ 72](https://github.com/H-EmbodVis/HERMESV2) | Driving world models serve as a pivotal technology for autonomous driving by simulating environmental dynamics |
| [FrozenDrive: Zero-Shot Text-Guided Driving Scene Generation and Data Augmentation with Parameter-Free Frozen Diffusion Model](https://arxiv.org/abs/2606.20110)<br><sub>Yuhwan Jeong, Hyeonseong Kim, Daehyun We et al.</sub> | ECCV 2026<br>2026-06<br>📑 1 | [⭐ 10](https://github.com/daehyunwe/FrozenDrive) | Synthetic data for autonomous driving is surging, powered by diffusion models that promise scalable scene generation |
| [MESSENGER: Memory-Enhanced Sequential Scene Flow Estimation via Autoregressive Next-Frame Forecasting](https://arxiv.org/abs/2610.10759)<br><sub>Jiuming Liu, Jianing Li, Mengmeng Liu et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 0](https://github.com/liujiuming123/Messenger) | Scene flow can capture low-level 3D motion displacements in dynamic scenarios |
| [ASTAD: Asymmetric Style Transfer for Synthetic-to-Real Adaptation in Autonomous Driving](https://arxiv.org/abs/2606.29286)<br><sub>Dingyi Yao, Xinqi Zhang, Lihui Peng et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 1](https://github.com/Dingyi-Yao/ASTAD) | Synthetic data mitigates the data scarcity problem in autonomous driving perception |
| [Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends](https://arxiv.org/abs/2606.01164)<br><sub>Jiuming Liu, Chaojun Ni, Mengmeng Liu et al.</sub> | arXiv<br>2026-06<br>📑 7 | [⭐ 244](https://github.com/liujiuming123/Awesome-Interactive-World-Model) | With rapid development of large language models and diffusion-based content generation, world modeling has attracted increasing research attention, benefiting various downstream domains such as game engines, embodied AI,… |
| [Is Your Driving World Model an All-Around Player?](https://arxiv.org/abs/2605.10858)<br><sub>Lingdong Kong, Ao Liang, Tianyi Yan et al.</sub> | arXiv<br>2026-05<br>📑 5 | [⭐ 256](https://github.com/worldbench/WorldLens) | Today's driving world models can generate remarkably realistic dash-cam videos, yet no single model excels universally |

## End-to-End Driving & Planning

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](https://arxiv.org/abs/2609.26792)<br><sub>Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.</sub> | CoRL 2026<br>2026-09<br>📑 1 | [⭐ 12](https://github.com/VAIL-UCLA/DreamStream) | Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions |
| [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)<br><sub>Shen Zheng, Anurag Ghosh, Gaurav Parmar et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 32](https://github.com/ShenZheng2000/WarpI2I) | Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs) |
| [G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance](https://arxiv.org/abs/2606.26017)<br><sub>Hang Yu, Ye Jin, Alessandro Canevaro et al.</sub> | IROS 2026<br>2026-06<br>📑 4 | [⭐ 6](https://github.com/HangYuu/G2DP) | In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors |
| [SUV: Future Scene Understanding as Video Generation for End-to-End Driving](https://arxiv.org/abs/2608.03084)<br><sub>Yibo Yuan, Jiacheng Fu, Jiangtong Zhu et al.</sub> | RA-L 2026<br>2026-08 | [⭐ 21](https://github.com/ASH-2046/SUV) | End-to-end driving requires a coherent understanding of future scenes, yet existing methods model these scenes using task-specific heads and output formats, with limited scalability |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 16 | [⭐ 347](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
| [Latent-Centroid Steering: Single-Pass Classifier-Free Guidance for Command-Aligned Autonomous Driving](https://arxiv.org/abs/2608.00237)<br><sub>Meibo Hu, Jiamian Wang, Pichao Wang et al.</sub> | IROS 2026<br>2026-08<br>📑 1 | [⭐ 2](https://github.com/codingmlinprocess/LCS) | Vision-language models (VLMs) have recently emerged as a promising paradigm for end-to-end autonomous driving, enabling agents to map multimodal inputs and high-level navigation instructions directly to executable trajec… |
| [DVGT-2: Vision-Geometry-Action Model for Autonomous Driving at Scale](https://arxiv.org/abs/2604.00813)<br><sub>Sicheng Zuo, Zixun Xie, Wenzhao Zheng et al.</sub> | arXiv<br>2026-04<br>📑 14 | [⭐ 367](https://github.com/wzzheng/DVGT) | End-to-end autonomous driving has evolved from the conventional paradigm based on sparse perception into vision-language-action (VLA) models, which focus on learning language descriptions as an auxiliary task to facilita… |
| [STAGE: STyle-controllable Action GEneration for personalized autonomous driving](https://arxiv.org/abs/2607.29517)<br><sub>Zihao Liu, Xing Liu, Yizhai Zhang et al.</sub> | RA-L<br>2026-07 | [⭐ 6](https://github.com/CarlDegio/STAGE) | Driving style refers to the behavioral preferences that drivers maintain during driving, shaped by their diverse experiences, habits, and needs, and is typically reflected in varying levels of aggressiveness |
| [A Survey on End-to-End Autonomous Driving Training from the Perspectives of Data, Strategy, and Platform](https://arxiv.org/abs/2610.00926)<br><sub>Chengkai Xu, Yiming Cui, Jiaqi Liu et al.</sub> | arXiv<br>2026-10<br>📑 5 | [⭐ 106](https://github.com/Jiaaqiliu/Awesome-Training-Ecosystem-for-E2E-AD) | Autonomous driving is a cornerstone technology for the future of intelligent transportation, where end-to-end learning has emerged as a transformative paradigm that directly maps multimodal sensory inputs to driving acti… |

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
| [FreeOcc: Training-Free Embodied Open-Vocabulary Occupancy Prediction](https://arxiv.org/abs/2604.28115)<br><sub>Zeyu Jiang, Changqing Zhou, Xingxing Zuo et al.</sub> | RSS<br>2026-04<br>📑 6 | [⭐ 140](https://github.com/the-masses/FreeOcc) | Existing learning-based occupancy prediction methods rely on large-scale 3D annotations and generalize poorly across environments |
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
| [123D: Unifying Multi-Modal Autonomous Driving Data at Scale](https://arxiv.org/abs/2605.08084)<br><sub>Daniel Dauner, Valentin Charraut, Bastian Berle et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 402](https://github.com/kesai-labs/py123d) | The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics |

## Safety, Robustness & Evaluation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [CCFM: Collision-Constrained Flow Matching for Safety-Critical Scenario Generation](https://arxiv.org/abs/2607.04451)<br><sub>Ke Li, Kaidi Liang, Yuxin Ding et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 3](https://github.com/KELISBU/CCFM) | Evaluation of autonomous vehicle (AV) planners in safety-critical closed-loop simulation is essential for real-world deployment |
| [Lipschitz Optimization for Formal Verification of Homographies](https://arxiv.org/abs/2605.23203)<br><sub>Jean-Guillaume Durand, Panagiotis Kouvaros, Maxime Gariel et al.</sub> | CVPR 2026<br>2026-05 | [⭐ 2](https://github.com/jeangud/homography-verification) | The adoption of vision neural networks in regulated industries requires formal robustness guarantees, especially in safety-critical domains such as healthcare, autonomous vehicles, and aerospace |
| [CADET: A Modular Platform for Evaluating Distributed Cooperative Autonomy in Connected Autonomous Vehicles](https://arxiv.org/abs/2606.04072)<br><sub>Pragya Sharma, Brian Wang, Mani Srivastava</sub> | ICRA 2026<br>2026-06<br>📑 1 | [⭐ 0](https://github.com/nesl/cadet) | Deep learning models are increasingly central to autonomous vehicle (AV) pipelines, yet their integration has traditionally followed a monolithic design where perception, planning, and control execute on a single onboard… |

## 🏢 Industry Tracker

Latest 14 days of news, official blog posts and new open-source repos from tracked companies. Full daily feed in [`daily/`](daily/).

<details><summary><b>Waymo</b> (208)</summary>

- 📝 2026-10-08 [Sober Drivers Still Face Nearly 4x Nighttime Risk: Why Road Safety Demands a Safe System Approach](https://waymo.com/blog/2026/10/sober-driving-benchmarks) <sub>official blog</sub>
- 📝 2026-10-08 [Waymo Closes $5 Billion Debt Financing to Accelerate Business Expansion](https://waymo.com/blog/2026/10/waymo-closes-5-billion-debt-financing) <sub>official blog</sub>
- 📰 2026-10-16 [Waymo Opens To Everyone In San Antonio, San Diego, & Tampa](https://news.google.com/rss/articles/CBMilwFBVV95cUxPeWpMZ1VuWjFTazZmU1BZVjJlWDNuQUxpWFJ6bjlNckpEdS1HNjFnXzFyUWNaOHVQSk5wN1UtNF9sNnVRM29jQ2NfVVRHc3NCaUhuSHZwRVhSU0I1LW51VjUwU0RHOHBsM0dlT1M0NnRQS3VMSDYyb0dwRlhEVkR3cWk2d1JjakppU1h0TFlRVFFUNXlISWhB?oc=5) <sub>CleanTechnica</sub>
- 📰 2026-10-16 ['My Waymo Is Being Driven By Someone Real': Woman Gets In Waymo. Then It Runs A Red Light](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE5iS0lrejVVdUt4cFgtSTJDRzJVQ29Uak5uSUsyaFk5RDZtRGREbnJmVHJCQ01kbnhXbkxRdTN3MTNCMXhBdHNSbER2WGR0SXl5bHRZMUwyOXlFREo2YVhtTHVxS3k3c1k?oc=5) <sub>Motor1.com</sub>
- 📰 2026-10-16 [Janeese Lewis George Says D.C. Should Hold Off on Legalizing Self-Driving Cars](https://news.google.com/rss/articles/CBMic0FVX3lxTE9hcTI5YnQtaGJiaG1OUi1LSmZXUjFXX3BkRzRJUXBRaEs2R2lPblotbkpDa3pRZkZaNTRXMnduTVNmT3JqSmdlMDBQSk4tYmVMYXhDNTlqeExsRGNLSGR4VS1QNUs3VlBtQVVkUXNVLUFWUzA?oc=5) <sub>NOTUS</sub>

</details>

<details><summary><b>Tesla</b> (347)</summary>

- 📰 2026-10-16 [Watch: Tesla Robotaxi Pushes Through Austin Bollards](https://news.google.com/rss/articles/CBMie0FVX3lxTE9VUXVkOERrU3BUTV9KTHRYYU1zc1lIeUZyaEM0M0hMbmJINU9DTVg0c1FlMy15OWxGU3Fwc2hGS2g1RmZkR0dtZ1g1TmhIRU5PRXQ5N0RSM05scEs0QXo3WmM5U3Y0aTZUclJHX2NfLVVPSmFpNEl6eC15aw?oc=5) <sub>Motor1.com</sub>
- 📰 2026-10-16 [My Family & Friends Go Electric](https://news.google.com/rss/articles/CBMidkFVX3lxTFBhODZzU2hlV0N4RkZWb2RqNXVpOGVDekFJanVjeFlMQ3RkNVJ1Q3pIa29LbGhnS2RFaG85SV9xMnhPSGtyRmdPUnUtMkhSeEhmVGVZMUdYRG1OX2hQX2RLYXEzN2ViN3VKUUMzMG1TaTZnYVNpMmc?oc=5) <sub>CleanTechnica</sub>
- 📰 2026-10-16 [Watch the live stream of the Tesla Roadster unveiling event and get live updates (pics and info)](https://news.google.com/rss/articles/CBMitwFBVV95cUxNUWdWTHQ4QndkdGFwejcxVk9jY1FWWTk1QkJoN2VrSWJTR2diMkpIYi15WW9FcWJwcGtub2dqajMza0FPSThHRzB5WDNRbGs2MHBSY3FVRVhkZlVKcmNacFZXUUtndDNCQjdTWjFENTZvdm9pV09LcF8xQTVFVzNMdVE5SFM5b3Bva3RjYVBWQjFNRUpyYmRtT2oyRUE4ZHRMUFFLWVNON2kwcHppMGNTM2F6Y2pkWkk?oc=5) <sub>Tesla Oracle</sub>
- 📰 2026-10-16 [Tesla Roadster Event Recap: It Flies, Flips, and Hits 0-60 in 0.81s](https://news.google.com/rss/articles/CBMipAFBVV95cUxNLVFRYVR1LXJHeWhnVjhvMUI2aXl2OUJGVDdQUUtBcmJyWVFESFBqNkdrcURkMU1UXzJyX2RpcUpOVnplMy1Qb2gtOUFoVElGZ2FZcHdUTmNXcENfSEIyX3ZzSEt3ZGRHMWYxNWZWbGFfenFlX0NVbG5Ma3ZzYTVCZXoyUzB0Q1dxTnZGRWhnNFZhSktGQlFvcUx6VFBSbVpFRTE2Zg?oc=5) <sub>Not a Tesla App</sub>
- 📰 2026-10-16 [Tesla’s Robotaxi Just Put Starlink Inside Its Roof](https://news.google.com/rss/articles/CBMie0FVX3lxTFAweFNaTF9zYW5oTVhmWDU2cUx2SHdOU1BOYWhNRzhtQ1RDQWU5ZG9VbnNXSXRjYzJJWC0yYUtaTmRpZ2xQdFB0SWM1TWxMZ0IycnNpRnJSWXhTaXJ4TXg3UEN3RktiNXphWllQSzFQSkRkUHhOMlNVOW9yNA?oc=5) <sub>Motor1.com</sub>

</details>

<details><summary><b>NVIDIA</b> (222)</summary>

- 📰 2026-10-16 [Volvo teams up with Nvidia to develop next-generation assisted driving system](https://news.google.com/rss/articles/CBMiwAFBVV95cUxNZjEzNjd1M2xuYXNYODR0Y2xrOGJFNWdHN0NQY2tvd1BvVzBaS2FYcEo4VkpyaVl3b0x0SWZ1bV9TLUJiek9yMkJwQjZZMWRNQzNHTldselJQclZiR0d4cmtKOGUwcWRZZlhpY3AtT1psZ0JrVWwyWEZJREtBamUycU82M2xXNFlJZk95LVBLbU13cVVqcmhQb2dOWi1ZbUhJcmVVMW5VX3Vqb1RLOUZUMmJRbG5OVVRtWDdFTlVaLU4?oc=5) <sub>디지털투데이</sub>
- 📰 2026-10-16 [Volvo expands Nvidia partnership for hands-free automated driving](https://news.google.com/rss/articles/CBMifkFVX3lxTE05VnpCLTJEX0dVSktnVXRURGNXLXhFdXRfSXFFaVNreXJaaWxHMlV4TzBHTG5oZ25TVGlLMEU3Mk9TV1VpczRlUHBrSE9fR1BKOE9WLXVxOWdibnN6YzBNVGw0bFJsUlpwd29UbFVsMEE0aTMxOXVnVl9OdGhNUQ?oc=5) <sub>Cryptopolitan</sub>
- 📰 2026-10-16 [Volvo expands Nvidia partnership: new automated driving stack before 2030](https://news.google.com/rss/articles/CBMiqAFBVV95cUxOOV9KWUlwRU1pbk9aaDJ1andGZUVaNmo5Y3pGd28wV2FNenM1NUlwRFhDRnhSRDgwYi01aFROTEVHX2FKREY1czk4WnRGaU9zZ2tpN0xMeTVpTzdVVkQwX3d5YnY2WmFFeFgwUm1tTDZhSFNuSHktSXBqeTJJejJYb0FqWlJRR2FWb1JZeDNzV3pneGJoS1BaUVU1bUlZbVVPRUhXVi0yNlE?oc=5) <sub>Softonic</sub>
- 📰 2026-10-15 [Nvidia, Broadcom and Micron Could Drive 40% of S&P 500 Earnings Growth](https://news.google.com/rss/articles/CBMiqAFBVV95cUxOcWFQeV9JN21ueG84MEFJZzc3aFM1RlRfdm4zUUJqS0Q3RVZQTm9wWUVTSTc2SUdpeVduZnd6NVFLSU1YZVdpVjVDeXBtb1QxUzg1WTVHdGJuM2dINlE3dlg2VFdCbkdvTEV5R2x1YURyZnJoWXBJSklLZzZvMzVWNGk5T2x2UVVuTVU1SFBHbDBLU3EtbzZQbGdyeUdEVjZYcGhkZEg4a1Y?oc=5) <sub>CryptoRank</sub>
- 📰 2026-10-15 [Embedl and Space Cargo Unlimited Bring AI Autonomy to the Space Edge](https://news.google.com/rss/articles/CBMirwFBVV95cUxPd2hNX28zMGtuN3JSODhKQVdDYXg0bi1LZ3VRdWpWdnZ6VTlzRW83MVA0V3BvckNWNUFLSnIzTUxNMUZ4S3NzeXdaeGxTMV9YeGdkeEZPb2FzRGFDMUVRQk95RXN0eHNpQ0JxZXRIdkdFdERGM1VVNzJFTFpxaEo2S2RSUkM5WjNLWUh1Z2pRMWZWUE9jVElkeHhCTzh4QXJmWU9FNGk0aU1vTUdoYjc4?oc=5) <sub>EIN News</sub>

</details>

<details><summary><b>Wayve</b> (64)</summary>

- 📰 2026-10-15 [Uber begins autonomous vehicle testing in Manchester with Pony AI](https://news.google.com/rss/articles/CBMihgFBVV95cUxQUmxvR1VHSWp4ZF9GU0UzdFdfakNvaTBwazRmUUl0bHJhWk9teDJoOG8xUENuRGhWODhmTldaN3BjWnVXRHQ2Nm0tNXBwTUlidWlfMGJseDhRUG5PVGVlZDhJcTlUZnFlMmNEdWV1dHhYVkdIT0RLOGdlWnVkVHVZdjVjV2xSZw?oc=5) <sub>Highways News</sub>
- 📰 2026-10-15 [Lyft starts a business travel brand, escalating its Uber rivalry](https://news.google.com/rss/articles/CBMiigFBVV95cUxNRVA0UC0wR0Rwc29qYjg3ckxnUE5DTklycXFabktVd3BYQVF5SHB6NFA0UXotd2ZZa3RzNEJuWXZZUnE0OG94LWVLRkhXanVhTVZQQV9ia001OGpxbWdZQ28xd1JUenBYaWRuWGJ2THR5Q2YzeTFRWkFMZE9vZGRZM2R0NmZyZGIxeUE?oc=5) <sub>Yahoo Finance UK</sub>
- 📰 2026-10-15 [“Let’s build AI unicorns first” ... How Britain and Singapore are pursuing a place among the AI top three](https://news.google.com/rss/articles/CBMiU0FVX3lxTE12MjAxQjA0WFo1RmNqQUtlRzhORlYxS01BWWVsV0s2UzBMQk5YWXZPZ1gwQ1FaV0daMklWbGdteGVOczdhSmEwU0lmLVJXSl9fTjVB?oc=5) <sub>매일경제</sub>
- 📰 2026-10-14 [UK Government backs World Congress for Intelligent Transport Systems](https://news.google.com/rss/articles/CBMiogFBVV95cUxPbllTN1lLWmlFT2VqWDhBaGxTRjhqQlFMQjVvZ29kMm1tRGpzMlRjVHhmU3ZpTHNwQVZYWWlYOTNudUlTS0g5N0lzdnd3M2lBZlBvSVlwaXlFclFhcXB0dXJzdGdjS3ZtY1o2QjNER2ZaS0V4b19ocEd5MUNtN2diZGR5VDE3bk5DbGRfOS1aU3lJWEdCVHUyaWFjWFc3UWNoTkE?oc=5) <sub>Zag Daily</sub>
- 📰 2026-10-14 [UK tech companies raise $25.7bn this year](https://news.google.com/rss/articles/CBMilwFBVV95cUxQWU1zbVpRTTZiWmlDVkpqVm8xZmVDdVZ1Yld4WjlWcENtMWl1U0VfVnNKck91bTRQSl9ITW10WmY4MzdTNkZ6NjQtMXBYN0djWXlhbDNDaHhkcWdCZEw0LUlBSDBLZ3ZheVVqOUJZR05WQzJVemk1TW1NMlMxR1NLTlRLTGpUQ2ZWQVdtWlk4akVIYW15NGhz?oc=5) <sub>Electronics Weekly</sub>

</details>

<details><summary><b>Momenta</b> (86)</summary>

- 📰 2026-10-16 [东风风神L8+将于10月23日上市，搭载Momenta R7世界模型](https://news.google.com/rss/articles/CBMib0FVX3lxTFBpX0VGWjJwOVdaMHM5TkZreEVzLWdYWlhwYlU0OWVONXZXMVRQclc5SnNJUUZiX2FqaE4zV2V0Tk1oUmEyMkdiU2pJNzhNUkNrUUswUHdManpiY1RwR0pjZkhlU2R4akNOTWJZU0NqYw?oc=5) <sub>中华网</sub>
- 📰 2026-10-15 [豪华SUV怎么选？XT5 PHEV 25.99万起全系标配智驾，兼顾动力油耗+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE5mZTNRVnJXQXlJWVp0Q2N4a05KNkp3aUl3OXB5eUNrSnUxLXdzNWFZbFBFSldULWtKUXc2dTU5Z3VPYVpncmk4cTV0Q294a2lwNDE2dGFRM2dqR3hwVTNPTno3TUhSMDlqV0toN180TE00dw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-15 [15万级哪款SUV配Momenta辅助驾驶，自动泊车辅助靠谱度怎么验](https://news.google.com/rss/articles/CBMia0FVX3lxTE04V3E1Vkc4OE04MHVPUUlQNXYxcEpONEV1cGVVSzduYjJfNmRxVmNDM2xVNWVvZ3QyaDRSWkY1YU9DVkZxQk9TM3JPVGRtMjl3UHpLMEdWZFFxV1I2RkszZ0VIRmFIX2dWLUUw?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-15 [Jeep production returns to China for global export, except to the U.S.](https://news.google.com/rss/articles/CBMiqwFBVV95cUxORnlUS2FBLWp5OThuWjRLM0g1MkNPWnY2enRZTk84Rnk3cjJ3dEFtSk5jeEUxZHhfaEFpbjNKeG1IdFBMU2UtSWphR0dEcFppZ21uQmdVSV9nUnF4ZnZMV1lHTDdDaW1SUDFUeWE3MWNueXI4VjZGTEV1X3hIcFZfOENmM1NoTGZkQUNNTFZRem5MSm1CRDFGUk1QMEFBWXYxRjd6SEJUSEotYU0?oc=5) <sub>Automotive News</sub>
- 📰 2026-10-15 [东风日产新N7智驾联合Momenta防晕车](https://news.google.com/rss/articles/CBMic0FVX3lxTFB5WGtwMnpoT2h2NTdJZUFhNDJjMDktM1N5R1J4QUhrMU9xXzQ4QUZISFFhLXZYVWhHeEZRcjl6djRVY2FKa1ZuR0I0QTdDMFlBTmJMNjBOX0wwQmw3TF9JUDdhZVdqbjB3LUtGV0t6TXhMZEE?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>XPeng</b> (299)</summary>

- 📰 2026-10-16 [小鹏MONA L05预售：16.98万起！纯电/增程双动力，大五座SUV](https://news.google.com/rss/articles/CBMiW0FVX3lxTE54S3dQX1E4Z213b1NOblZKV3Zpc3FwVFFRSlRLSG5CeXA1VXRFRFluTC1sR1dFcVEwc3Raa3ljcGdzdGhGcEg5WFdyMmMtZFdyOVZBRjRoNHAxVUE?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-16 [全家舒适大五座SUV横评：小鹏G9L、理想L6、问界M7怎么选+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE9hUm81Ml8wcDdFcG1JZjZ6TGdjZHR6SVlFSjQ5MVNpenJYT3VmUWRkTjB4end3X2tNSWNXTUxKYTduai1veGRDVENpTFBpX0ptNXFJeFpnZlRfNUFyWkt2NlVvVXJhMGFxY0hZeFhXMVdqdw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-16 [23.18万起的新王炸：小鹏G9L、理想L6、极氪7X新上市大五座横评](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9XcnR1aUlXSHFKOExXVHpwdUhkYmZZcGV3dVNpb0pndDhSbmNQVUh1c1RZRU5zRExmcnRhYjZmNVZTcEd0SmM4WlJuRXBXdnpnblNBNUV6ZUVpZ3JxQXF3?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-16 [MiniVlog \| 姗姗来迟的小鹏之夜记录](https://news.google.com/rss/articles/CBMic0FVX3lxTFB2N0RkS2lhT3FEUXJ3M0Z6bWhOZ1VSWlk2QU5kcDRfSUFQaDM5ekI5Qmc5RFFqdHdib2RVaGRydDBpNkU0bXQ0MGRHb3B3TXJZQU52WVA3blpuLTkzS2JCTlBzRzVpTnFCMlpoWE05ZlNLd2M?oc=5) <sub>新浪网</sub>
- 📰 2026-10-16 [最近上市的新能源SUV盘点，小鹏G9L凭23万级大满配入榜+横评](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5pQ1RrR3Y0S1RMeDhPbzRxZjktcjgyeGh5d05ieTMxSDdfb05pRl9ZRm9IcEg0SGprcG1rcldpWDF5WWVZdHMtNlByQkhTTmJ1alpXNTVlRV9rT2pwUi1Z?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>Li Auto</b> (151)</summary>

- 📰 2026-10-15 [Chinese car companies building networks in Europe](https://news.google.com/rss/articles/CBMitwFBVV95cUxOZ1ZDZzNfVHZBQkNFMHVwdDFQMDFheVNnclhmby1CQjZKTnNSUWlNOWJkbGRCbUtYbjBkZUw2a0VGdUdDZ3JZOURkU3ZrN1VvMHV0TGFqQzN5aWtIM296a2tSc1c1V3JCQklqVkhDSGpzZk9DbWVtUmE2MmJ4Q1MzdkFYNDNmbFdsWjF6N3F5ZkRfMjk3RTN5RTY4NTFhNm03d19ISzBUTVpSSDRfV3hod0MtWWpMQWs?oc=5) <sub>CGTN</sub>
- 📰 2026-10-15 [Zacks Industry Outlook Highlights Mobileye Global and Hesai Group](https://news.google.com/rss/articles/CBMivgFBVV95cUxNUndoTm0tSWlkQ1pyR3hUZ0VBd0U4N3R2U2RGV1pqbEQyd3hMYWhLdy1DMFllalpBZElrSFlWRThWUWxoQjF1ZXMtQ1FnYTFpdXQ5Y3VPUi03UldhUnVRdHI3R0Utd0lsSkQzOFlFSXBTeGFMdGwtSGRFaEw2UFc2VENzVDYwdV9vajNxcjZZRnZGSldqU1RvX21yenVwQnk0WkFEYm9qc0NCWEt0UU9QVGFOamhGZUlxNkwxZU53?oc=5) <sub>TradingView</sub>
- 📰 2026-10-15 [Semi-Autonomous Vehicle Market Report Offers Analysis of Market Development and Future Growth Opportunities](https://news.google.com/rss/articles/CBMikwFBVV95cUxOLUZLaDRTQVVGNS1MaVAyRVpJQjZfb3ZoamZKR3hKZGhSdFdFX1hTSjZXU1NJMlZub2hEVG5YVG9VZVo0R3N2Y0k5VFB1VURBcHVwTHdyTm9GcDZzZzJ2ZC16VVB6ZU9wWkQtY0JaYnNoTS03eWxTLTJkQnFqQ0NwSFVSRk5yZmUwb1NYTjVlTUNqX0k?oc=5) <sub>openPR.com</sub>
- 📰 2026-10-15 [1 In 3 Car Brands At Paris Motor Show Was Chinese!](https://news.google.com/rss/articles/CBMie0FVX3lxTE14ZkdGLW9vaEFtenJ2bE1vSU9xNHBvRzl5bnBTMjZLQ01EZUF5MkNJdXlBRDJSeXVKQmtWX3ItREhIcUZJMjRJQTAxdFcwTXJEVmRaQ3FRZmRmOURYNlc2b1hMYWE0MHl6WFFjOTgyNEpEVDhkZkhMRTBYZw?oc=5) <sub>Cartoq</sub>
- 📰 2026-10-15 [理想汽车马赫M100智驾芯片亮相央视经济半小时](https://news.google.com/rss/articles/CBMic0FVX3lxTE1vbkp1eVlVSEt6aHliVERJU2Z5ei01aXNtVjVqaTNWTUtBazhvalUtLXd3LTB1ZFRndkVVbzB3WUJtRF9DNzhsX1plalpValNybVlWUmVwaUR6VXN0Q0dFSXM1NjF4NGlYdi1xWGJIQ0lKSHc?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>NIO</b> (142)</summary>

- 📰 2026-10-16 [智能体验好的大五座候选清单，小鹏G9L第二代VLA全系标配入榜](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBDSlZ2TzIwUlpUSGRzU0xnalg3SGhnRnFfSUxCbU41ZFRRczJVeE42eWFjbEtmZjRwLXEtQllpRkc3MVNaM1ZQYVh0RjhGX2M5Znc1ZnRwOWZfYUhucjR3?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-16 [底盘操控好的大五座SUV横评：小鹏G9L、极氪7X、智界R7、蔚来ES6谁更扎实+选购清单](https://news.google.com/rss/articles/CBMiX0FVX3lxTE4xNW0xR1VRNlBmQXlZZjduVXVqdTJjVGxUXzhCRGRhVGxQc2Nmb1A1ZGpCMm1makpEbExrbUlJR3o4QTc1MmJlYlo2Ni1QanJ5Y1BRdE84dVNUeElYSmZn?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-15 [Rivian Moves to Block RAVAN Trademark for Autonomy Tech](https://news.google.com/rss/articles/CBMilwFBVV95cUxOczFLTER4Rkh1WkNzVFBTakg3MzhYV3FycW0wUFUwVjk1TkRjSzV1cVF3ejNXVEZXdU9QVFBZZ0puLU0tUmtBcXBEMGE0QmhWYW1kRnpYcndvUGFjNE1pLVFRbzhsVjVwZzdmdjYwdjlENkZ3RDgxWG5nSk9QWjVLMkkzOTlnaUpvSmhmWXBDa18zV3VIb25V?oc=5) <sub>Electric Vehicles</sub>
- 📰 2026-10-15 [30-40万价位段：智能轿车热门配置与车型解读](https://news.google.com/rss/articles/CBMickFVX3lxTFBGaDFod0UwNEdMOGhNWXpPNWV5TF9jVUJtajJIY0lOMnM3am1sVkhEeVlmWEVlTEhPWUFEZk9tWnpOTlBHWEp5enlxdnJqc0hSQlU1TnI0emwxYjVDZFRMajNXLXUyRktic3ZjV054TWN6dw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-15 [长途自驾拒绝续航焦虑 神行者8、蔚来ES8、理想L9三款豪华SUV谁才是真正的“全场景之王”](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5TTk5oM1ZjWDRSeWpNR2tiTElfYXl6OEthZHFhWS10TXlUbUFHcWUzM0hNOEQzUU53Nk9zbXl4dTEyUVFkRlE1VDNZc0xISGVHdWJuTmVuRzduUVVoNU4w?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>Huawei</b> (359)</summary>

- 📰 2026-10-16 [HUAWEI nova 16s Series Specs Revealed Ahead of PH Launch](https://news.google.com/rss/articles/CBMiigFBVV95cUxPaGM5aU5icW5Oem5MLURPTjdZekN4TVdwVXZQRGoyMWN1MjUzX2xJM1hkOUl4Q1VmR0FSNlFWbDVSV3BfZk55WHlEeEdXXzlEODhZdlRIdkRuUlRRNmRPMkwxWVY0VlF2akZiczA4VFpKTDItUGJnTUJTZm9veDJFQmRIbUJuUTZwN3c?oc=5) <sub>ManilaShaker</sub>
- 📰 2026-10-16 [12.59万起 华为乾崑智驾与XWD四驱加持](https://news.google.com/rss/articles/CBMic0FVX3lxTE5ESi1HSzdCZ0hQemtlWGlobko0QS01VEUxT0R5bFpUeU9iX1owdXZsMXdGSlNiRWEtV0p2ZHlIRzEtTm4ydVhERTRHT0ZLSHV4TE9HN2ZNLThwckw5Vi1ueFoyXzE0U3ZHeVFQcVRUQ2stc00?oc=5) <sub>新浪网</sub>
- 📰 2026-10-16 [20万级就给足乾崑大六座，华境和华为的关系是什么？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9jamJ2eGlFMGhOQVVpcWZscENqalcxMzgwbXpEejliTGpSSkpyNmRYWFZ0c3NTdFhZTDFOVHNKZ3VrdlpBaV9FR3hTcEhlbXhMMjVVaDEtcmk4Nnc?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-16 [奕境X9六座SUV上市，华为全家桶30万级真香警告](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5vR3FTNXZHQ01vaWtTd2NQdVg3SThORUdMM2o2dDEzc1FSUmxrTzlEU2J4MlpNVGxzZ2thdFk0cmRqVWpNNVc4R1BCNE9uMm9MNFJsazRva3otWUE?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-16 [【视频】全新旅行者7：冠军世家出手，重新定义7系方盒子标杆](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5kODJDNFkwRmpSa3JVTVE2UnZQLThpZVRpSkN0ekNxXzI1elVtZkpla2tsazZYczlWX0E2RkhfSmtMOW5vOFd4c3liUU54SGxHWkhzbkdMU3JuZHc?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Baidu Apollo</b> (47)</summary>

- 📰 2026-10-15 [Over 1,000 Hongkongers to ride Baidu’s robotaxis in city-first public trial](https://news.google.com/rss/articles/CBMi0wFBVV95cUxNWnNjLWZZMENDWVZ1bjVDaXJVT0hnNGxNMTAzbEN6cDBEa3lJYWd4SkNqbzF3WWMtczJDR0s1WWJpTmp2Q2dfTGhJXzNMeDVMSmZIT3o2QkUxTU51ckt3VnJPaktOc1lNTWlSZUtCWTEzUWc5UkJrWEpLVk9oZFN0c0RSNEh5U2RKUTdVMktadVJ1dlg5QkRDMmtXa0haVkZDSGhmaXlVVktyaUhJczZ3amhrb282eFhpbjBLWjFteWltY0ZDSkp4UmZDMlY4T182bU5B0gHTAUFVX3lxTE1ac2MtZlkwQ0NZVnVuNUNpclVPSGc0bE0xMDNsQ3pwMERreUlhZ3hKQ2pvMXdZYy1zMkNHSzVZYmlOanZDZ19MaElfM0x4NUxKZkhPejZCRTFNTnVyS3dWck9qS05zWU1NaVJlS0JZMTNRZzlSQmtYSktWT2hkU3RzRFI0SHlTZEpRN1UyS1p1UnV2WDlCREMya1drSFpWRkNIaGZpeVVWS3JpSElzNndqaGtvbzZ4WGluMEtaMW15aW1jRkNKSnhSZkMyVjhPXzZtTkE?oc=5) <sub>South China Morning Post</sub>
- 📰 2026-10-15 [Baidu's Apollo Go to offer free robotaxi rides in HK from Oct. 21](https://news.google.com/rss/articles/CBMif0FVX3lxTE9DNDB2Z2dfVWhUdUtkemZYUy1OeTBnN25GY2tNa21iZXhOR2k2X2dkdXdMVDBqMEdNY3VtYkp5OUdFUWZrbk03NF91d1Rab3JSaVc0d2EzSnpoOVM0QzBfcjJqbi1Gam41Ni1tQVB5S092WEZtVlFxVGRNay1sdmc?oc=5) <sub>dotdotnews</sub>
- 📰 2026-10-15 [Charles Wright: London, not Whitehall, should be in charge of 'robotaxi' rollout](https://news.google.com/rss/articles/CBMipgFBVV95cUxOZjVpLXVLNGF5MXlzN3JSV2JXc2pBSzNFRkJSSDBGU2NKX0RWcnBISGJIYVZqVnhtMFhFSzFpYnhCYlB0VE1UcklxQUZheVZuTk1SclRQSWFZTlduX05JakF3Z0toQmlaR3J4UGZqeHRDTVRacGxIZlppazVaeFVwdExwcm5oMEc2U1ZqOEJ1Q2F1R3BHZmxBckVpN2tLTHdjNXdVT0FR0gGrAUFVX3lxTE1KVS1ZRnBwUExVRUY4cGtrcTVaUldiNjE3RHVCV2pFVjQ2UnRHbEVnQnVlQ2NUcFl2QmFMdkdMQ3Z2OFVCXy1UdzQwMEJNelBHSXRtVXh2SVpXQ3Nnam5FSk9uT1dWQnFGNzctNmt4czhOYnNETzUtdEkwNDU4NDRIS3hyOXZ5T2h6RkpUc21icmdkVV91Z2U3V21ja01vZ09jOEJNNVh2NDNCQQ?oc=5) <sub>OnLondon</sub>
- 📰 2026-10-13 [Waymo完成50亿美元首次债务融资，特斯拉Cybercab单日新增注册150辆，小鹏Robotaxi启用小鹏悠游](https://news.google.com/rss/articles/CBMiVEFVX3lxTE9JZFBKMTdRVUxUUHhQT2RzZ1EzTWtGS24zR3BfX20yNk5Uek42LXA1SWc4UEVEU3l5SXZoY0xJRVFlT2tycHgzWEZEZzhuY1gtZjRydQ?oc=5) <sub>虎嗅网</sub>
- 📰 2026-10-13 [小马智行杀入伦敦牵手Uber，中国Robotaxi出海怎么打？](https://news.google.com/rss/articles/CBMijwFBVV95cUxPQjd5cFFBdWZZNTN4Tkd2cmtrQVIxenFtTVJtT1ZzdTk3bldFWnNhRFlHVzJFSTYydnlKenpvQWdUY3hZeGZrcDZudl9tVEVTbnVZaExrb2g3LVpZZjlFd3RKeHg2bTN5a2UwWFk1clVRSjduSFpyTDdfMHB0SUhKVTRmOE9GalppMnJ3UXRoVQ?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>Pony.ai</b> (137)</summary>

- 📰 2026-10-15 [出海日报｜大睿生物向罗氏授权创新药，博力威与越南VinFast签署合作协议](https://news.google.com/rss/articles/CBMiWEFVX3lxTE9IWDgxZGFidXJqNW9idG50THBEVzNaV1p3ZTdtSXNOdmxOWC0yTEFzRF9VRTNEb080YlhRQjFMaUIwTDdpMXA0Q29oVHNHa0JBZUMzNXg1Mmc?oc=5) <sub>Jiemian.com</sub>
- 📰 2026-10-15 [Pony.ai launches Gen-7 Robotaxi testing in Manchester, expanding UK presence to two cities](https://news.google.com/rss/articles/CBMi5AFBVV95cUxNMlo2V0dtLVpVYVZPWEItNVN3VUdrOTFCZEg3R1dpbWVxWS1xcVpCcXEwN3BmYlk4dmlxUVZDUEhrWF9fLW1RbE95ZVJCS0Y3a0NqejRDTmxkYm5Jd2R1Q01IR0tSZDFQYkFucFc4Q2p6YTlNRU9LM09nR09UR1ZJQ1Y5T3VXb0laX0RiZ2hURE1BNXRlMmRhZF9TU0lkMUZOTHI5N0YxOUJkQXRPRVlJUExjWVhPaThSdU9tRXlXT2ljbXJhX0RsWVlVNVdWZWRyeXZHR2tKczRBVFdaaGlLTE9LS2o?oc=5) <sub>Gasgoo</sub>
- 📰 2026-10-15 [Uber begins autonomous vehicle testing in Manchester with Pony AI](https://news.google.com/rss/articles/CBMihgFBVV95cUxQUmxvR1VHSWp4ZF9GU0UzdFdfakNvaTBwazRmUUl0bHJhWk9teDJoOG8xUENuRGhWODhmTldaN3BjWnVXRHQ2Nm0tNXBwTUlidWlfMGJseDhRUG5PVGVlZDhJcTlUZnFlMmNEdWV1dHhYVkdIT0RLOGdlWnVkVHVZdjVjV2xSZw?oc=5) <sub>Highways News</sub>
- 📰 2026-10-15 [思想耀岭南 \| 第17集嘉宾大揭秘：他从南沙出发，让中国无人驾驶驶向世界](https://news.google.com/rss/articles/CBMid0FVX3lxTE92ZVNFNVBBSkVRSHE2LThUWFpKLUt5cDJPQW1iSG5Sc2ZyWlVadlVKRXRjQ2tVX0pVVURtSk9KZWRtZEcwLXFOdnVGekthdHNhU1pzVERWVzlvbVc3MEFyeENQWGdDa25Kbk5FWFZ3dUJYcnN1bHhB?oc=5) <sub>珠海网</sub>
- 📰 2026-10-15 [10月15日港股软件服务行业沽空数据盘点，腾讯控股、智谱、网易沽空金额位居行业前三-证券之星](https://news.google.com/rss/articles/CBMiXkFVX3lxTE9EWnBDcDkwSFFXMS1YaXQtVzdXYUIzS2NydXAzVzdmYTVKUHFwS1FXT2RFMTNwbGNROThpY1k4OHFsZ1o5SGpUU3VCcXdIRTdVemtOSFpXN0NGRGM3NEE?oc=5) <sub>证券之星</sub>

</details>

<details><summary><b>WeRide</b> (147)</summary>

- 📰 2026-10-16 [三部门调查尊界刹车踏板断裂，港股通汽车ETF易方达涨1.44%](https://news.google.com/rss/articles/CBMijAFBVV95cUxNdWZnbG9mRWZ1YjRNdTZFMnA5ZTh2Zy1JcHVEd2VWNlRvNWIybWtHR05ic1FDSlpOaG1LQ1pBdUV0aGllMTBlbFFBakRuMEJPOGU3a1pZQi1VNl8yQmVsU1puVDhUWFN0eU5OWF9wdlZLcTdIQnJnOFdvVG5kcWNJVC0yelpRZC1lRV9OYQ?oc=5) <sub>搜狐</sub>
- 📰 2026-10-15 [文远知行-W盘中跌超6%](https://news.google.com/rss/articles/CBMiXEFVX3lxTE1HVC1BV01sNURBTTY2RVd2SVI3WU5mMzVXbHlwaW9hNlBTU00wSkhvdWE0VjBZbmJ5M2lwc3NldmstVlpTcUVZdXZZVWdCdUNDUEF6cWdWNW13aUlj?oc=5) <sub>www.caiwennews.com</sub>
- 📰 2026-10-15 [US No Longer Embraces Innovation: China Does](https://news.google.com/rss/articles/CBMib0FVX3lxTE1ubnd1UUpkSzRmQjRqMy00UEkxX3dZV0M2SjljTWFfblFIRjNJNERUTVd3T2FQaHNZdXY0dUVSNDBkTHFqYkxRWFlpWW9wdWtYRDlDazQwQ0d5MGlhUXFZVUthMFg4MENNMEJpYnpnQQ?oc=5) <sub>www.policyarena.org</sub>
- 📰 2026-10-15 [张雄双品牌焕新首考没及格：埃安N60销量承压，昊铂S600破局乏力](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5GNjd2a0NoNFpOcnVGUTd6VVE0RUtLdnJVSTFqNkNpSXdtbDlaQUphSGFnbVJwaS1tOGd3Mm5xejdhb05JMEMzNE92a1VhTGJJYUxvR28wZ09TQ3c?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-15 [美股科技股大跳水，光通信、半导体股暴跌，戴尔科技跌超11%，Lumentum、甲骨文跌约9%，英伟达跌3%，中概股下挫](https://news.google.com/rss/articles/CBMigwFBVV95cUxNRGN2UXNaQUk0WWowcnFRVk54ZHF3bzd6RHVRc3lKaFRjNG5NWm05TzE0VmJ5ZEtubjI5Q2k2bXllWTBVdU5xSnAwZ2p4OERUVVlya1lZQk0yRV9fLW90U1Q2MnhfVVpyblljYzJUbUpJYmU1YjJuZUxlLVRBUEE1SWVYSQ?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>Horizon Robotics</b> (168)</summary>

- 📰 2026-10-16 [换的是算力，还是消费者的知情权？铂智3X芯片争议](https://news.google.com/rss/articles/CBMiW0FVX3lxTFA2bER3eTBpUzlhbVhtcDcwaGxLZ0NQcy1qNGt3N1dmQk4xWWxmS2Q4MWlEMXJKVVY3LUxoMVBpRUdqcjlHZmo3emwxcS1tV29wZDZYd0Vpb0liSzQ?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-16 [NOA杀到8万级市场，谁在「闷声赚钱」？](https://news.google.com/rss/articles/CBMijAFBVV95cUxOMVVPTlF4enJTaFhuVHo0TFZSREw3RDM5aDNIdG5WZ3kwMHJKeHotRFNFVXlBejYyMTM2dVZlQTNxczdsYm1WLXFYRWRqWmEzQW5EeXFEY05iWGFPTjhZRWJXc1czUlRIbzlXOFl4ODhOTTZSWTVwTHVoWEVKMkJhRUFMMlpxSHcxVTU4Vg?oc=5) <sub>搜狐</sub>
- 📰 2026-10-15 [捷途旅行者7上市，限时12.59万元起！](https://news.google.com/rss/articles/CBMia0FVX3lxTE9Bck5mWVZWcjhOd2hBRy1UT3N6ZWdNNFhWSGdfNGFhQUlyaWwxVGVmcGJlWm1VUjVoanlOVTBuT2ZGMHVWaHF3b2Y3ek9ZQTRlMmgzVHVqU1BzejNOYjE1M24teC1MUHdLa1Bz?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-15 [德系纯电SUV智驾横评：ID.4 CROZZ、奥迪E7X与大众ID.AURA T6谁更懂中国路？](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBEa2JaeVlXa3NrRmc3QVhDdWk0UVJEaVM5VmE1VUdINHI4TkhBZ0EteUlLd21pY1FJOEdnaElXOFp2VHcwcVhESWhORkFfMmdPSmlCN2dNWGNka2lrSWdZ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-15 [德系纯电智驾横评：从ID.4到EZ-60，ID.AURA T6如何凭“听劝”跃居第一梯队](https://news.google.com/rss/articles/CBMickFVX3lxTE94UnpqNmt1aWE2OTJicFhCQ0pvZzNweWNnMGFyczZsMFdTYl92cUdMbW1QR002VTRGd1VIUVR5UFhPOG8xaTlVdWM3OElnaGJFQnlnbks0Z1ZpWjRWZzl2WHRMMGZlTnpBYXJIZFNQSk5HUQ?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (33)</summary>

- 📰 2026-10-16 [【视频】#卡泰驰二手车特斯拉YL](https://news.google.com/rss/articles/CBMiW0FVX3lxTE85eTFWS0xEY25USjY4aXFQRkhjZmZPVHhVeXQ5eHluRkphVFVORXJJaExYSkxrV3Nlc3lWZE9PUXRGdXRRMk5BZlZ4cTNMUFpuWklkNzdCNHRiRWM?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-15 [数据驱动的具身智能：迈向规模化之路｜QCon 上海](https://news.google.com/rss/articles/CBMiXkFVX3lxTE5qSDE3dmxBTFE3LTdLZ0lyV05Sc0VsQm02bEp1bWJBZ1pXRFVwUG5uWTAwdG05WWNnT3d2N0JzS1NBa3QtWmJCb3JOeUU1czZ0bmZwQU96Vi1FZk9hNEE?oc=5) <sub>InfoQ-CN</sub>
- 📰 2026-10-15 [London Assembly Transport Committee Calls for Cap on Autonomous Vehicles](https://news.google.com/rss/articles/CBMiqgFBVV95cUxPMk5heTNKQnFWZnBNb1U4RVRzeTNZU0U4cWxlTG5WT1FoMG5scGhVazBoYU1lWW9wc0RUakJiNFhYcFJ0ZVprUDY4UXNyM1RZS3NsdkFyZTJtWHM1YzRrejZXMC13bkpVVy1seUZYa3h0YV9kM1FuMDVndlpNV0dmb282NWU0YUkwTEJwdU5FeWdtVElYYWhZZVFQTWZxWFF3ZHVneGl0RVBSQQ?oc=5) <sub>Future Transport-News</sub>
- 📰 2026-10-14 [赛豆科技AIVA第二款SUV或将采用换电方案](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5WSE1zeWlTbjE1UFVyQ2tveGFfS2lhU0FoVFVHR1J2NHhUbUY0U3RUai03SVV6UlREQkM2dENhRk5WaTZGM1lxRjhNakJYY2xFLXZ0Z1JBQWFSLUE?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-14 [How TomTom and DeepRoute.AI Are Advancing AI-Based Driving](https://news.google.com/rss/articles/CBMikgFBVV95cUxPTlNCVERPY0U4ajVoMEVtUF9UenVjcEZZMG1xM0J4QWdvVWtqUFBWQlI0X3RPeExKYmhxOFhwa3dObHRudHBfSEsxNXNJMWhkSlhxUmN6bHhtQUI4NDBTeFplZFlZV0dnLWVYbnR3V3dsM19Hc2VSN21EaG9GbnJIT2c2T3ZrZ1FwZzhveVNjN0hTZw?oc=5) <sub>AI Magazine</sub>

</details>

<details><summary><b>Mobileye</b> (16)</summary>

- 📰 2026-10-15 [Zacks Industry Outlook Highlights Mobileye Global and Hesai Group](https://news.google.com/rss/articles/CBMivgFBVV95cUxNUndoTm0tSWlkQ1pyR3hUZ0VBd0U4N3R2U2RGV1pqbEQyd3hMYWhLdy1DMFllalpBZElrSFlWRThWUWxoQjF1ZXMtQ1FnYTFpdXQ5Y3VPUi03UldhUnVRdHI3R0Utd0lsSkQzOFlFSXBTeGFMdGwtSGRFaEw2UFc2VENzVDYwdV9vajNxcjZZRnZGSldqU1RvX21yenVwQnk0WkFEYm9qc0NCWEt0UU9QVGFOamhGZUlxNkwxZU53?oc=5) <sub>TradingView</sub>
- 📰 2026-10-15 [Becker Transactions Announces Availability of MagTrac’s Autonomous Vehicle Patents Focused on All-Weather Driving](https://news.google.com/rss/articles/CBMi-gFBVV95cUxOYjB0LUhhdmxDaFFxWm9HSk1LMjZvRVg5WGdNS011dzhWVnNPNDJCZ0twUUlHel9vbW1hR3ZKLUkxQzh5TjhHdjVhdXFodXQ1U0ZCT2t4QVU2bEhld2VLNTRDdVlpXzN0WnE4TmplWlp0MWJnczlaVXVoX09fREttNkJhaFlIbDZTMF9Pb1RfaG1jbUlzR29wcXhqNTNhY3dGUEFjTEJkSFJzaGlNZ0NjTkE0a0xyRExpellkSmxNV3BLV1lIYjMwcV9kc3pRSFp0M1BkRVVMUDVIWjBlZkFYZDJ2Q2xBY3pYajY1LVhpNjgyaUlRUUlaRk13?oc=5) <sub>Kitsap Sun</sub>
- 📰 2026-10-15 [An Israeli AI startup says it cracked a 38 year old graph theory bound for $2,000](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQS1RBR3FmbVZXTmFmdVF4cnBON094cVlGWHJBaTBSTlRIVlhEX25wREdVOWE5ckxxTEtTSTR0VTd0bXpVUHBCQzdQZzNCbTMzWk9XRXRQcjFqdnFVcEJWS0JJRWdDTDNwM3liS1NuR21pYmN5Y05ocklJc0p0NU9feGNXcC1nNTRCb1RPb0syQzhkbHRsN05sMWF4TDVMYzYweVo2UmY5YTkxUXc?oc=5) <sub>Startup Fortune</sub>
- 📰 2026-10-15 [Innoviz Technologies Targets $8B Security, Defense Lidar Market at Conference](https://news.google.com/rss/articles/CBMi0gFBVV95cUxOWkhGNi1UZUFBdHJfUlgtdEFPZEliMXQ5azhkVHh2aGotMEhodUhDc0d6WmZjSmttZHhmSEdQY2ZDN0hzMDR0RVRQTW9QRzlqLUxWX1ZaejBDVVh2NzhZNkl5b1c0eUpTSzdNZWx3aElrZmo4T2JSdjVpdzZQdEVONVRCcUlDMmJLbHd5QXBzUnhkSjdRUWd2WHFZRlV0M0JkdG5nQUg0RWlwUzl2eXJUeUR2dWRGenVZVmtDVkFPT1lXcFFMY0JPVk1VRXVaZFhhNkE?oc=5) <sub>TradingView</sub>
- 📰 2026-10-14 [Shashua: Israel must invest in AI infrastructure to compete](https://news.google.com/rss/articles/CBMipwFBVV95cUxNOHFQMmpVTDlEQXZESFFEWUpzS1NsNWJhUHJFU3hBejFYeGxXR2ZyR1V2RVVZZ0NsOVZvUjliTGRldzYyaHBpS2RqYVhnTndkNXhqQnAtZFFWN3hJUlYxN05weXpWbEtyWHRraXJ4Q3ZUbDBMNU9CU1FuM2ozalgzSzRvUTU5MDMtWkhNcUxSeWI0OWdfU2VmaENoNXRlVUliZWVzZXF3MA?oc=5) <sub>Globes - Israel Business News</sub>

</details>

<details><summary><b>Aurora</b> (69)</summary>

- 📰 2026-10-15 [FMCSA approves warning beacons for autonomous trucks](https://news.google.com/rss/articles/CBMicEFVX3lxTFBjNy0ycnEyZnNRazZuNXBIUE9QRk9iMElTY3c2Tk9aOTZVRzd5ZHBSMEl3X2NPOFZrcVpHNDJrVXA4cXdHdXM3eXlIQ0hzajlTbFJ5aUZZd3N0VjVMZm8zUFVBZFMtUE00REEwZEpsc04?oc=5) <sub>Transport Topics</sub>
- 📰 2026-10-15 [Aurora Driver 2: The Best Inventions of 2026](https://news.google.com/rss/articles/CBMic0FVX3lxTE9vRVNxSXhsNC1TcDlZcWp1SWh3cGJnXzFiVC1zOGF2TmJOMjlESkxfZVRWMGtGTHlDM1FISHMxTFk2UXhNQXVkR3BaazVBMVpUMkUwN0IyVUl2Zjc2MWpfMWxlRjJtTlF1UzRKMUZPdHJRbHM?oc=5) <sub>Time Magazine</sub>
- 📰 2026-10-15 [See which Pittsburgh companies made Time Magazine's best inventions list](https://news.google.com/rss/articles/CBMilgFBVV95cUxOa2pITl95ZmYtRzMyRXdISGlMRjkwVDc3U1pZZVZ1aTV1bmFBck9nWGNDTmR0VG1tY2F3RkNhb0N0MEdkN0xkU3NqMFVuZExNcjN6MFdQRWpMdG1sVHRTZGs3ajhzeEhwMmFGeW1wcGpTVkc5b3V5VWJJTzl0NFpJZUZuTkd3TjEwcGJhM2w5Z0hoVjJmeVE?oc=5) <sub>The Business Journals</sub>
- 📰 2026-10-15 [Autonomous trucking needs smarter trailers, Charger Logistics says](https://news.google.com/rss/articles/CBMitAFBVV95cUxPVnpIU0d0VHQwTmJHRVc2eHJRWGNHaGdOMWtLYmJuQ0VKb2ctdl9hWm1ISGMyQ0xiMllEekxSeFNxNld1MjQ0Uk0yRXA2SjNJUFp2WS1EVUtabGhEU0dWQVJCMUNIUi1uR01fc3g4dmFDRmpQa3Z6ZlcxSkl0aUJZdGRCRVZZWnNlUUFwRjg1WTlOeE5ZUmY3V3o0dVVBVlQxTVpGcm1hSHU0S2hybkRqUElHa2I?oc=5) <sub>Truck News</sub>
- 📰 2026-10-14 [Autonomous Trucking Advances on Costs, Freight Operations and Federal Rules](https://news.google.com/rss/articles/CBMia0FVX3lxTE13ak1NNlJKWHNVTmFwd0FXbVEydXQ1ZENkc0tyVWVIT0pIOUlOVkJ4WXBYLWNRR3ExSmpHNjVkdFJuQVFLV0g0V0dMcHBpYlR6Y0Y3b0xrT25IV2lNenJ1dGt3dXNhdkIxUHRV?oc=5) <sub>Advanced Clean Tech (ACT) News</sub>

</details>

<details><summary><b>Zoox</b> (68)</summary>

- 📰 2026-10-16 [Zoox Leases Two More Hayward Warehouses for Robotaxis](https://news.google.com/rss/articles/CBMiogFBVV95cUxNS3hoQXBUa01acFRaQjRYMWNxOENEYllhV3EtcnFBNjBLUmFtLW9qRlU4WE9GVEhXblJlNmhoY3hkNFRKclZ1X3lHUXFpUV9Cc2lnbHFsQ2YzX2RSQXJ1d0xra3pnRy1YbEp2eW5ON0xqYXB4aWJEaUIzZDVGU1BTUm5ERmNrZVdTUTlJZ0ZOckJfZUJhTVdGRjQ5YkRhNTFYOFE?oc=5) <sub>Hoodline</sub>
- 📰 2026-10-15 [Tesla Robotaxi Tally Hits 739, Trails Waymo’s 1,185 [2026]](https://news.google.com/rss/articles/CBMid0FVX3lxTE5DeGxZSWQyTzdKUHBkUnFqV2Z2ODFsc2JwSHNxZ1psUGE5WHNNbmpWTzhYUlVSWkozRFM2aUZPTDl4SkpUdW1Ubm5LeWxULXRXY1cwdVRlTjRjWHdnRWhEQ3kzTVRvOXYwcmpFLXBnUlVmYlNMNnJR?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-10-15 [Tesla Cybercab Hits 300+ in Austin: Inside the Hardware [2026]](https://news.google.com/rss/articles/CBMic0FVX3lxTFBSalF5NS11ckNDZDVpQ1hpTDlERTR4dWhRUVVJckZOb1dtTnRVMWtRQ0hSbU8xZDNvR2J0WV96TmFpX0p1QXFlSXBEMG12LVNDbkNHelBDTThPNFRRajQxYWZMWDlUZUNfQU1UeWpPV0VFRjQ?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-10-15 [Exclusive: Amazon’s Zoox more than doubles its robotaxi footprint in Bay Area city](https://news.google.com/rss/articles/CBMiowFBVV95cUxNeVV6MkRja212cExtNm5jQ0JVMXFRMkZDcmpKcU5uRHFOeGVpUldCWDY3YXFRQ0dzZmktdmNVbnBpVDJ5ZVVlbnBKQU1hUmVqUVRvMWxnMTJqeS1GR0gybWJWdGFPU3lmNWRpbm1hcEsyeXBIbU8zWWtCdTBFMmQxREIyRG9VTDhIZzE3LTM3OHlfNFRBOXpqX1k5WGEzT3pEbUFF?oc=5) <sub>San Francisco Chronicle</sub>
- 📰 2026-10-15 [Minneapolis City Council fails to override mayor’s robotaxi veto](https://news.google.com/rss/articles/CBMiogFBVV95cUxQX0poTjJkOXNzcm42akc5bjJVOFBPRk44OHA4M0g0NEpZR0prSmgwZUl5T2VLcGlsMjgxd0RscGdPWVpCUWhTTEJYWVMtaWpadk9ZMDVYQ1dOSlkwZVRTc1daYXBxQmUtMVEtbTJScjkxUmk5aGd0ZjRlM1lXdFNxYTFOWThfeFExUUUwQWllbVFTb083YzNhLWVWVDJkMy1LZVE?oc=5) <sub>5 EYEWITNESS NEWS</sub>

</details>

<details><summary><b>Motional</b> (41)</summary>

- 📰 2026-10-14 [Hyundai’s two robotaxi plans take different routes](https://news.google.com/rss/articles/CBMikAFBVV95cUxQNWdFN1RBOWctNVVIZmRxemEzVEhrQ2MzVkN6YkJWME81bW41bFFqQVVDLTl4SEQ3OTYwalRQaFo0Q0xwaVR4M3FYOUZpMUV3OEJSTDktdHY4enVEdDgzY0xuV3lSa3hCTTAwdE93bkhoS2M5aHdxcmVkbEJIM1QteTlVbjhfTk9UUVBraW9GX2TSAZABQVVfeXFMUDVnRTdUQTlnLTVVSGZkcXphM1RIa0NjM1ZDemJCVjBPNW1uNWxRakFVQy05eEhENzk2MGpUUGhaNENMcGlUeDNxWDlGaTFFdzhCUkw5LXR2OHp1RHQ4M2NMbld5Umt4Qk0wMHRPd25IaEtjOWh3cXJlZGxCSDNULXk5VW44X05PVFFQa2lvRl9k?oc=5) <sub>ABC27</sub>
- 📰 2026-10-13 [Hyundai Motor Group chief marks 6 years at helm with physical AI ambitions](https://news.google.com/rss/articles/CBMi0AFBVV95cUxOY2g0R29NX1hSa0ZuUzJveFVZYUQ1YzVVNEItNnRkUjY0TnRHNi1fY1ppaVc2YmotOEt3YXhCeWxLNVN1NGQ2c2hGNVJYclBocEhKcDgzNjMtdjFPeGJ1bWJjTFR0UGgtUzNwdWZqQkQzaHB5U3k3bXpPcDQ2S05KUzktWkJWN21WSjItamJ6eV84clptQzRHV25xYXFyNURmamNLWGkxeFVNUDFCeWs2cTJta25zcE54WGFYcEE5T1YyaVQtMEh5ZTZvUTNUUlUz0gHQAUFVX3lxTE5jaDRHb01fWFJrRm5TMm94VVlhRDVjNVU0Qi02dGRSNjROdEc2LV9jWmlpVzZiai04S3dheEJ5bEs1U3U0ZDZzaEY1UlhyUGhwSEpwODM2My12MU94YnVtYmNMVHRQaC1TM3B1ZmpCRDNocHlTeTdtek9wNDZLTkpTOS1aQlY3bVZKMi1qYnp5XzhyWm1DNEdXbnFhcXI1RGZqY0tYaTF4VU1QMUJ5azZxMm1rbnNwTnhYYVhwQTlPVjJpVC0wSHllNm9RM1RSVTM?oc=5) <sub>The Korea Times</sub>
- 📰 2026-10-11 [Six Years into Euisun Chung's Tenure... Hyundai Motor Group Moves Beyond the 'Global Big Three' Toward Physical AI](https://news.google.com/rss/articles/CBMiZEFVX3lxTE1qSWl5SS12dk8yVXMwandrR090TkZkdzZDaFladGpmOGNZZDNrMGxBQV9zSkV5TXpVeXIzWGhKd0FVYUQ0ZFdsT1pEWGxZNDV1UC14N0FsZmxVd0ZFOUVkamhoMWg?oc=5) <sub>아시아경제</sub>
- 📰 2026-10-10 [Waymo's $5 Billion First-Ever Debt Raise Signals a Robotaxi Land Grab, Not a Science Project](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9BaGt6ckszSmpwTDVsOGUzQ29DXy0yc3BsVFdSTjNtZFZrR3dWYUd5TzcwSTYzUTE3MlVmd3B4UG1iSS1kRHpySXpFVlhRTWd3cjVCOUgwVW5FcWc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-10 [Waymo Goes to Wall Street｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTFA2Z3RvWEJLVEtPTDJWNVcyaGQweFBVUnZFb0RST0wxRWhCdUJudXJQeU9helBuODZrTlBDZlh4NF9zb3dyNjRxQ3BzTGpZLWJvQzNObmFlYjl1R010Z3hB?oc=5) <sub>finance.biggo.com</sub>

</details>

<details><summary><b>comma.ai</b> (4)</summary>

- 📰 2026-10-07 [Researchers Find that AI Models Struggle With Even The Most Basic Driving Skills](https://news.google.com/rss/articles/CBMiuwFBVV95cUxNb2ZGRGxGZDNjLWU1OVBPNjUtUlJXR0hiVGV3WEJ1eUVnSWExMWVvRmJjX2NtQm9sX0plMTU3YzZwUm5ZTzVoSGttcXZmQ3BqbW40X2doNFMycUk4UWE3anlidy1vWHNYZndVZjZWLUYtbnlHeVBFRjJOaTF4SWxzbmotR0xsNkVIcEhfZ0M3LUs5R2FyV1lVdlRRU3JwakpQcXpBUzlEOEhsWlB3Q19EdXFhQjRvZDU5MHln?oc=5) <sub>Auto Spies</sub>
- 📰 2026-10-07 [OpenAI's GPT-6 Astra is the only AI model to finish a real-world driving test in a Toyota Corolla](https://news.google.com/rss/articles/CBMifEFVX3lxTE9iZmN2ZFp6blVBRnZUTkYtYTJ3b0hSb0xhQjZyQXh5MUN2T3ladUlEb1F1SWJzc3FtamZtazk4LTVUWVpNX0ZjbGZwMnpERk45TVVQWVA1RjBZVUxxTTAzTWpaV1JqUzIwM1I2Wk1tTzc3bDJpaWluc2JVam4?oc=5) <sub>Crypto Briefing</sub>
- 📰 2026-10-06 [AI Agents Tried to Drive a Corolla, Crashing on 8 of 11 Runs](https://news.google.com/rss/articles/CBMiuAFBVV95cUxONWxQTEZham1kc1J4S2lMNUh6OTN1QWhXbl92U21NUWZTZWhNUUdwcFVvUHYtVWJzSjl4TjlCeFhUY2ppMXd3WkkxaHJFRmFlNUN2NGFSSENnV2ZZYWRNZ3JIUjd0dzFlTS0wR3gtbmxXN3VHOUkxWWg2VVFpTVgzWGN2T3RPdEFJV0cyWjRPSVFyNWZTYjFyX0pzYjFEUWQwLUlfbGo1bm8xVUZXQmpyQ3pCNXV5ZE9x?oc=5) <sub>thetruthaboutcars.com</sub>
- 📰 2026-10-05 [Researchers Discover ChatGPT Can Drive a Car. Grok, on the Other Hand…](https://news.google.com/rss/articles/CBMikgFBVV95cUxNNnNwX0g5bHV4STJlMXNOcXRnYnBHWHNoelViM2pJSzFob3dvUVJIdFlDRDV4X09DSVloZmxCTk5NODd3b3RBR2JmWEJQRktXUTYyWDNveS15UEw0NnVfSFluMlJxZHlBb3NhYnRNdDJsZ01MbVNpOXY4OW9nQnBSYnFRQ1U2YVd3a3R2ZTY4VlJNdw?oc=5) <sub>The Drive</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
