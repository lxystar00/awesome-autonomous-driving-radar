# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-10-12 · 1,254 papers tracked · 38 curated.

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
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 16 | [⭐ 346](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
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
| [123D: Unifying Multi-Modal Autonomous Driving Data at Scale](https://arxiv.org/abs/2605.08084)<br><sub>Daniel Dauner, Valentin Charraut, Bastian Berle et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 401](https://github.com/kesai-labs/py123d) | The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics |

## Safety, Robustness & Evaluation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [CCFM: Collision-Constrained Flow Matching for Safety-Critical Scenario Generation](https://arxiv.org/abs/2607.04451)<br><sub>Ke Li, Kaidi Liang, Yuxin Ding et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 3](https://github.com/KELISBU/CCFM) | Evaluation of autonomous vehicle (AV) planners in safety-critical closed-loop simulation is essential for real-world deployment |
| [Lipschitz Optimization for Formal Verification of Homographies](https://arxiv.org/abs/2605.23203)<br><sub>Jean-Guillaume Durand, Panagiotis Kouvaros, Maxime Gariel et al.</sub> | CVPR 2026<br>2026-05 | [⭐ 2](https://github.com/jeangud/homography-verification) | The adoption of vision neural networks in regulated industries requires formal robustness guarantees, especially in safety-critical domains such as healthcare, autonomous vehicles, and aerospace |
| [CADET: A Modular Platform for Evaluating Distributed Cooperative Autonomy in Connected Autonomous Vehicles](https://arxiv.org/abs/2606.04072)<br><sub>Pragya Sharma, Brian Wang, Mani Srivastava</sub> | ICRA 2026<br>2026-06<br>📑 1 | [⭐ 0](https://github.com/nesl/cadet) | Deep learning models are increasingly central to autonomous vehicle (AV) pipelines, yet their integration has traditionally followed a monolithic design where perception, planning, and control execute on a single onboard… |

## 🏢 Industry Tracker

Latest 14 days of news, official blog posts and new open-source repos from tracked companies. Full daily feed in [`daily/`](daily/).

<details><summary><b>Waymo</b> (215)</summary>

- 📝 2026-10-08 [Sober Drivers Still Face Nearly 4x Nighttime Risk: Why Road Safety Demands a Safe System Approach](https://waymo.com/blog/2026/10/sober-driving-benchmarks) <sub>official blog</sub>
- 📝 2026-10-08 [Waymo Closes $5 Billion Debt Financing to Accelerate Business Expansion](https://waymo.com/blog/2026/10/waymo-closes-5-billion-debt-financing) <sub>official blog</sub>
- 📰 2026-10-12 [Driverless Trucks Can Skip Warning Triangles for 5 Years as Critics Object](https://news.google.com/rss/articles/CBMikAFBVV95cUxPZnNoVjlPOWlnYlRqNU1Od1Nzc0U1U0lhb1lBR0o5OFNHRTd6VDV3T1lCbzhtc0hVUWIxdHN1M3NLZlczUWlQMGRrVEhRQUtSUlB0VW1oeDVZMkY4RFlSM0gyNzZtMVNVUEFKczBGWU9xTzRjdFo2ZWNuUzVKaFdjTlFEU19sd3NsUU1OY3ZqX3o?oc=5) <sub>The Eastern Herald</sub>
- 📰 2026-10-12 [Tokyo police to set up section for autonomous driving accidents](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPRHhTbDRMZ29lbnU5R0xWejU4ME5mX29FTFBLMl9qal9XdjN0WkRwMnJuek1UNmViMkhmZ1J6X3F4SnFmS2p4WnZZSkRKOXJNbHhlQ2IyLTFaWU54YmhCczFWZDhUdGc2enV3ZHVGRWl0ZjJ1dG5qOHg4cmFWN051UEwwRXdhcmh2Sjkw?oc=5) <sub>The Japan Times</sub>
- 📰 2026-10-11 [Waymo Secures $5 Billion Loan—Its First—to Fuel Expansion Plans](https://news.google.com/rss/articles/CBMipwFBVV95cUxNY3A5ZURJVV95RmhHWlVrRTVFSUt3czI3M2pCNkhIUVYta3lzZWFLelQ3Mm5ZWXBIN3FPR2hjUXlUZW40SXN0anhoNUM1ZnhTSG5mYi1fbUNvaWNVUHRDUGpweVE0Q3FRZVQtNEF5NlZPUW9OQVhBQjd4TUNYbnd0cHVBZnVSbmZrMHE5VnBvRlotR2owODNKWmc4QjVCNzJBTEJTV3VoZw?oc=5) <sub>Inc.com</sub>

</details>

<details><summary><b>Tesla</b> (351)</summary>

- 📰 2026-10-12 [Tesla renames its FSD system in Europe under pressure from regulators](https://news.google.com/rss/articles/CBMivwFBVV95cUxON1lxQzRqZE9UNTRHa29FeTB6N0N4UGJ4RFNYWjdEV1FDOGdpdEVkUnJuSnM1U3hxM1F4OThmZllCa29NYmNiQ2JLd3ZSS2RNbHVzaTIxZzRZcDlON2lXQk1KNVNjVnFBTmtLOHBaWktSV04yTElxREVoT05mbHJZenFQVk0xY0lpTHNDX1RZOVJHRjJQMkh2Zm1uZzZNR2hwNG54Q3pVZ1F5LTY3S1lqdkpXcFJYOHFJS09NdEt5TQ?oc=5) <sub>marketscreener.com</sub>
- 📰 2026-10-12 [Key facts: Tesla, Inc.: 10 chips/yr at Giga Texas; Cybertruck lagging](https://news.google.com/rss/articles/CBMixAFBVV95cUxPY1JCZ2c0akItQVd2V2o5ZUU4RzdMNmlXWlBpQWtmZ2x5T25SRUxqVEhFV2haNjlqUjgwby1LWEc5Q21BcDRNN3ZHSXhRZkV3ZF9LTnJSejZSdDVNUUdqd3l4Z1VUdlZpcnRzWnFRQndXNE9fRHVYUkwyemNGcFpaZFlnQ3lRWGJXZWRRMTdvN3BnSW5kaVZ0eWdXVlBGc2RudnhpSlVMYVVrYVN5YkdhRi03dXd1UXdfd0FPY29TUDhKallR?oc=5) <sub>TradingView</sub>
- 📰 2026-10-11 [This Week in TSLA: FSD's Europe Rebrand, Elon Musk Receives Medal From Trump and More](https://news.google.com/rss/articles/CBMi0AFBVV95cUxQUE96bWR3SklXamxheW9MckwxbEw4bU1yQUpIR3pLZlUwMS01ZnB1ckp2MW5NS0ptNGdPYk1FVmU3SUdGVUkweHduMjZNaVZHSFFtMjk0cXhUWjNYTjVlaE5zMDBhQjVxTm1KZ0l1SVU3TE9sWjdmX21jQUExekZXYV9zZ0xCdkc2T3dxRnJxb0JkcnVyOWhRQ091Zk1kcG1md3phVklMczM5TV9zNWVZRGdmLVdMRnJHYXFFTGJLSnpuemRyb09qam9HM0pnTFBK?oc=5) <sub>Benzinga</sub>
- 📰 2026-10-11 [Tesla Renames Full Self-Driving to Tesla Assisted Driving in Europe After German Regulator Talks](https://news.google.com/rss/articles/CBMiywFBVV95cUxOaXJtOGdwazNpQkFaU3NXOVU5STE0cWc2VUtEVnMyd3FBY0E2aUVJWUNQR2hPYkttOUd2UHJXS2tmbXdzUHBlVzR4akExMXVsbW4yV0xWdTktSmhlaHpZMWZuSnN0aWJqQUIwRGE4dVgzdjcwMllWTTdTQVdRRHFtaDRFdEZvR0I3QnVETF9tRGRDS19EdWRyNjVmRGZDcGRzMDlMZUVQVWtwY05udm0zMTFqNnd6bDNRbUNMd2NOVG1QOTBYSHJxeDc2QQ?oc=5) <sub>gHacks</sub>
- 📰 2026-10-11 [Tesla Drops ‘Full Self-Driving’ Name in Europe as Germany Backs Faster EU Approval for ‘Tesla Assisted Driving’](https://news.google.com/rss/articles/CBMimAFBVV95cUxQVFlUUm9WTXl1SEJteVFnOUlQUWFXam5RM1pKVjNMaEh2YWFabHV6a3NOOXdHWVVVY1o5am42QVNzelRjTUdwTkNULXRsdnV5SExNNEo5UXQ0V0JoR19rWHJQQ05GVTZQb3hTTUlxNTVRRFNhWHJQWThhZllLVm1xWS1iUURsLVIxU0xMU2R6czJFUVo1Qm9PSQ?oc=5) <sub>Yahoo Finance</sub>

</details>

<details><summary><b>NVIDIA</b> (222)</summary>

- 📰 2026-10-12 [Nvidia expands autonomous driving safety tech to robots, targets humanoid commercialisation](https://news.google.com/rss/articles/CBMi0gFBVV95cUxNb2tTdlR0dXVveUZJSG9KOFRKcEhzZW1hRlp5QktOVmVVWHVTclB6dkN1SG83SGNKWWFFY3BfRm5WNTNrRVJXTElHYW9XXzlZMWU4V3ZxMkdEZnRiU21NMmJjVXJHVjc3bS1LNDUzWlV2em5TaXdwMW5ia2RLc0MtRXhkaW1wWjRuLUJ2eUVaUmh4MFl5U1gwVlk0QjBqUnJQNmJqY3ctVWpfWVhMNFpyc0ROcElkODFVWVV3MXdzX244ZjVxcVdDS2VzZmFFX2RqOGc?oc=5) <sub>디지털투데이</sub>
- 📰 2026-10-12 [Nvidia's Vera CPU Packs a 1K-Entry Reorder Buffer in Its Custom Olympus Core](https://news.google.com/rss/articles/CBMidkFVX3lxTE13V3Q2b2xfenRENGRmZnQ0R2w1LUppUUp2ZkRnbEp6TWVKMlhEXzR3ZC1ocFJteXJuN0VSaVdNdXBsb0trNXRCYkx2WDV5WVNlQVhvV1hGQTk2V0k5M2Fuenp3dE8yTnQ2bGRqcl81X0pwVG1DdGc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-12 [Zeekr prices 9X plug-in hybrid SUV from €119,500 to challenge BMW, Mercedes](https://news.google.com/rss/articles/CBMikgFBVV95cUxPMEtCenBjRlh5VWxjVWJHRjRRMFN3QmM0d2o4MzdRcERQUU04ZGxLa0gxNE1tQUotaW85TllMblZOUUUzajhHUGY5N0JsLXhEZXBZZWVDbGJaN0dkcTdzMU9LZ1dBb19PSnJoYVE1RVhWajd5SjY4Q0dmOG9qbE81bmtROFJJN2JJNGtYQ0VnWEVjdw?oc=5) <sub>Automotive News</sub>
- 📰 2026-10-12 [Investor Concerns Over Market Outlook Amid High Expectations](https://news.google.com/rss/articles/CBMimgFBVV95cUxPZE0zWVhqLVhtamRERDhTZWl4RDdCYzlVbE9OdGNfNUc4X29jdm1ZSml6TWRvTC1tM3JmaGNEZHotSkxTbzc5V0I0a29ET003QVZqNGRCZ3ktVnVYZ1F5LTJKb042cC1ZR003XzA5ZUNfUWJJczdhX0ppUV8xY3VUNnVEWFNmT3QxSnkzSlpGRDRtOUQ5aDh0MnNR?oc=5) <sub>Intellectia AI</sub>
- 📰 2026-10-12 [Supermicro Powers DigiPowerX Full-Stack AI with NVIDIA Blackwell](https://news.google.com/rss/articles/CBMiZEFVX3lxTFBBRDhmdFo2TVNrWU1vWHllVUljZzBpV0swMDN1ZHVOV0hjSVQ4Zjdac1JGbUxjeU04enpwODhEeENYZ2tNU19UeEtHa3BCWjE2V05KVm9aTEhwNjIzd1c2ZTZ5YzU?oc=5) <sub>Supermicro</sub>

</details>

<details><summary><b>Wayve</b> (65)</summary>

- 📰 2026-10-11 [London’s plans for driverless cars ‘lack crucial safety features’](https://news.google.com/rss/articles/CBMiogFBVV95cUxNZU1WU2N5Y0JaM3R0QTVtQmxJNUlkSlA1SC1pNUNmT3RyMmZobEhvOGFfWXFlVFg2enI1Y3ZqWjF2eFN6b0k1MURvXzRjWHFiRlA0THFmdXBIc19Hc0s4Z3JkbkNOdzdXeTJRZXNTaHUxbDl0NHpDOVR6cVdRcGh6azdSMS1SSzZVbUhLMWhFWnczOE9XYW4tTlZUYlpYOElqRHc?oc=5) <sub>The Times</sub>
- 📰 2026-10-11 [Waymo Goes to Wall Street｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTFA2Z3RvWEJLVEtPTDJWNVcyaGQweFBVUnZFb0RST0wxRWhCdUJudXJQeU9helBuODZrTlBDZlh4NF9zb3dyNjRxQ3BzTGpZLWJvQzNObmFlYjl1R010Z3hB?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-11 [Autonomous & Self-Driving Vehicle News: Stellantis, Wayve, XPENG, TIER IV, Avride, Sodexo Campus, Helm.ai, Pilot & Tesla \| auto connected car news](https://news.google.com/rss/articles/CBMi5AFBVV95cUxQVkY2cHM2TUVLYjlkMXJZc3ZjRUN0M2RFVU5mNkF1Q2Fab0RycnM5aG11d0pQNDdaV2p2S1d5REc0clNheFJRWGFOUjNSZEJqczVZWUFJZldfNlJDNDhnM0preGRxSDk5blVTM01GLXEtTEV3TWlHSGtsRk5JWTNfd3JTak1ON1BFTDJqX3NKV2dMOGxORHZ1dGE1TVR0djlzVmNXR1V1SUQ0QTc3bHFwSTBCWndNZlNoV1ljQlZicEhoY0xGRTQtb2pMZHdPbFktTHdxdHR1MlRMUmxUTDlKbkhyVzM?oc=5) <sub>AUTO Connected Car News</sub>
- 📰 2026-10-11 [Uber Expands Driverless Taxi Testing With Pony.ai in London](https://news.google.com/rss/articles/CBMiZEFVX3lxTE95X1oxNURSM0JJaUVXTFNVV21qRkJHUGh2M0xnb3hzVUY1YUYycERjSktIRU94NjNrNjlTNkJIVW1LNVJ6NVRYY2d6X05xajlkd3VfeXJUZk5Db05neWozOFdOZV8?oc=5) <sub>SuaraGarut.ID</sub>
- 📰 2026-10-10 [Tesla's Full Self-Driving Is Now Called Assisted Driving In Europe](https://news.google.com/rss/articles/CBMie0FVX3lxTE52RExBODZnVENockNsZ3hSeFFhbC1KQ1ZYN3pSeTRSTmM5d1R5QjFWZWJIYTB5eDFaVmc4YjRubWYxVk1FNTdhbHFDTjB5dGFzalR4RDZULUo5MjUtaGM5UVVNX2ZWOEVUUUNvcVV3MmtHakV2QzU4ZGpvVQ?oc=5) <sub>AOL.ca</sub>

</details>

<details><summary><b>Momenta</b> (104)</summary>

- 📰 2026-10-12 [权益价20.68万元起 上汽大众ID.ERA 8X正式上市 搭载Momenta R7世界模型智驾方案](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPN0w5MjlRM1U2bVJzQWl3M3dzaTE1aUxOMkRkREhaWkpiWGNxaU5GN0hJcnBhOUdSeld2SXVmVTZNbXh0TzYxTXVCTUFueUo5TUMtVlVLYkxXMHJpSm02Xy1jUEZPZ0ZQbHdrc1p6ZUswWk9YdkxJVWpZbXJEOE4yR252Zk1IYjdq?oc=5) <sub>搜狐</sub>
- 📰 2026-10-11 [英伟达ThorU+Momenta R7绝对是最顶智驾 深度体验东风风神L8+](https://news.google.com/rss/articles/CBMickFVX3lxTE1EUHVhb3hPOHFaU3NhSVRhTi1qSC13Nmdwc0NRaUZzdkpNRF9nNjJvU2NKZDVPd2I5MlcxY2habnFwZUp3LTVVbkkzZWtLNk9GTVpEOVhiNldvU2tOUUYtbktpcUh0MDdZQ2Nwb1NfUzctUQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-11 [【视频】东风风神L8+顶配天元智驾+Momenta世界模型，七大场景泊车超省心](https://news.google.com/rss/articles/CBMiW0FVX3lxTE54MGpNNVJBX3lPUmZXRG0yVlVTWXBPWHRnUzdOWFR3YU0zSHZvc2NwdERZU1d0VXdYRkhQWlFDdS0yRVhBWHVZNFBKaElLTjRXSlRsTTJ0RDZEUkE?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-11 [新上市的豪华插混SUV哪款值得买？全新XT5 PHEV、理想L7、领克900与腾势N9智能驾驶横评+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFBES0QtTkY2R3U5eVJsbWZCTkpHSmFaRDQ5WVExRXZCbmhTakRpSFBVYjdweWZpZG5ReHQ2WHFmaHA5V1U4S1EzLVdSMVg0SWtfdlkwLUI2eUFuRkEtV1hpWVdhR0dKRzBPQllTNFVaeWJudw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-10 [Waymo Goes to Wall Street](https://news.google.com/rss/articles/CBMiXEFVX3lxTE9CNlVOd2gzcW5YMmZYM2xhTzdNdnZ6RUVjTFE5SnVFLUpGOThrLS1XMHV6LVBNRHhydnpScGozZjVCbW9IR195VDktLUxydFlQUGhNOXRBcXN1ZGc5?oc=5) <sub>YouTube</sub>

</details>

<details><summary><b>XPeng</b> (286)</summary>

- 📰 2026-10-12 [Relaunched XPeng G6 takes on Tesla Model Y, but which is the better EV?](https://news.google.com/rss/articles/CBMilAFBVV95cUxPRXVDN0JQWlNDME5wVV9XMmNxOGlsWDlGZEpTc192S29oc1JJZHMwYWwwTzJub1F6Mk5YcjFxZWVpenJXajh3QWQ1SnpzcmV1b0J2amljYnF5Qkhhd1Z1bzRJaVBkMVRmSVlpOVo5LWxEQV9HLWRMNTFQQWNPSFNFblBfdmFfeTcwM01YZEZoSmpzT3pm?oc=5) <sub>Drive</sub>
- 📰 2026-10-12 [Honor Win 2 series with active cooling fan to be unveiled next week - GSMArena.com news](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQcDlrQUNNVm8xSFZuMlNXc19ISzg0cTdvWmhaMGFQbHo2QTZyRjkzeV9Gd3NDNS16YnhWaEFPYmRGclczM3hlZ3ViYm9xU0twaGpsNlpoNzVFTlRtODFPNUZIWlFDbmF0UVQ5VHBVMkdNOHBKTTFxeEp6NDJBVWY1NUlOQ1FzZWlialZLWmZubk1QT2hpMmRCMWhRaW1tYnVBOU9XbVpOM29hMnfSAacBQVVfeXFMT3h5MUFHWHVwZkhMMHdNMFVQRi1JSjkydjE4bTV5VDBEREFDR3RURjdvUWlieEVGc2V4TkJLTXMxV1pGc3hCN1M4a2tkUVhYdDNPdFk2WHJhdl9uMzE0MVk5UUpWUDNpVkhlYno5Yk1rZ25EZU56OGJrcjI4TzF4WGJJQ3NFQ2pKMms2MUh0ZHZqOFQ3bGdnVGxPZVVzYjZjb0tldlBhd0k?oc=5) <sub>GSMArena.com</sub>
- 📰 2026-10-12 [都是明星车手实测，大众8X和小鹏G9L有何不同？](https://news.google.com/rss/articles/CBMiWEFVX3lxTE9qM2N1VnJIZThXQkFuOTd0dHkxeFVEdG5WczczTFpnTWk2TTVLeXBkTS11OXF6QmFrWkhuTHZuZlpPNjcwa2NTeVp0cnJyb2ltVWZ3UW5rd1A?oc=5) <sub>爱咖号</sub>
- 📰 2026-10-12 [2027 XPeng L03: price, specs and release date in Australia](https://news.google.com/rss/articles/CBMiqgFBVV95cUxQcV9pczlWamlGbnI3bmpLMWIyQ0pfaVBYWE95ODBzSjY2RGNLVkwxMmNJTVpTNkNQTW5WZWZxWlNEYjgxeTF6Nlp2elg2WEp0SmxLMXI4Tk1JT1Q5ZHB4Nk01S05MWURRa1g5SU5Ia1BpQXVMMHQtM1F5ZXZqUm5Tbks1ck4zVXFIRkhQOFpZZ042SUpnRkpGNjF0dnVMd2p4Q3A0aUdSTWZTQQ?oc=5) <sub>RACV</sub>
- 📰 2026-10-12 [小鹏GX 2026款智能到底有多强？3000TOPS算力+26.98万起，值不值得买？+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFBFOTdxUmpkR1FBdkZMQlZNSENfeFlUeWJZQnRRY2RHTFgyNlBxai1vVVJPNE9oUWhQalZucWxUcTZCWXJQNEQyMkU3cE0tODRWbVpoTmtUdHZXZi1mRGdxTGw0bzJmR2VDOFdGMkJKZjlVZw?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>Li Auto</b> (157)</summary>

- 📰 2026-10-12 [放弃理想L9选了它：一台让全家不再做选择题的大六座SUV](https://news.google.com/rss/articles/CBMickFVX3lxTE1WTWxYeVRqZlRFdFc0cm5zUGVFMzVZb2xSQjRKMF9SZ29ja3d6N0xFX0ZDeFRQQnRZRFVYeXBWcFlVVm1Oc2ZNYnEwTl94SjI2bWFnbEczZ3RPc0tUNFBXWDlqeEhlSHc1V0NWcEZGU1FEQQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-12 [VC funds are now chasing the seasoned veterans in the intelligent driving industry.](https://news.google.com/rss/articles/CBMiU0FVX3lxTE9oeklWenlHaGpNSm9TM24wdUk4RTl1Vzd1UGRUZVBJVjc1VS1TRkFLa3NxdElTTlpJNzNWaTR5NmlIM1FRb3dHVnpGRzBaV1RXTTVv?oc=5) <sub>36 Kr</sub>
- 📰 2026-10-12 [跨省自驾2000公里实测：理想L9、问界M8、蔚来ES8和神行者8，谁更适合远方？](https://news.google.com/rss/articles/CBMickFVX3lxTFBZaU8tOWN4NmxPdWNqR3BMbkY3eXM4aVFVbHVEZUl6UVhJbFpWZHZYOWFDYWZ4bWJDR0Q0OHVyN0FBblYyVWNDSFh1aldMOVhQRVRfWkhxeTdTbTV3WGs5a1ZYSDdkTTdFSThzY3R6U1hrUQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-12 [China's autonomous-driving veterans pivot to embodied AI as capital shifts from "storytelling" to "demanding results"](https://news.google.com/rss/articles/CBMidkFVX3lxTFB2Y01aZHNqandfdHZSRkF3MGYtTWw0eWVVbk5FdjdNZzBHbGd5Z2lQYm5jelQ0NThHMWRIU2Vfd3hrU0s4WFZBekNXRDJWQ3VneDZhak05MTI0RjRVcUJkXzJMM25aWnpVSVlBZ25WQ2V2MndJdUE?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-12 [长途自驾的终极形态？对比理想L9、问界M8和蔚来ES8后，FREELANDER神行者8给出了另一种答案](https://news.google.com/rss/articles/CBMickFVX3lxTFB5YUxyUXhhMVhZcEdPRGhONTRkQUtOMHNCR1VIMjdYc1QzMFJlZVRnTDFIbllfUkpSdURtTVNYcDJSaHVkWkxBWmY2OWJoVEhVcS1vUlZxRUMyOElRRlRnUUJPXzI1LXVlWWlUTWZPbDB3dw?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>NIO</b> (147)</summary>

- 📰 2026-10-12 [跨省自驾2000公里实测：理想L9、问界M8、蔚来ES8和神行者8，谁更适合远方？](https://news.google.com/rss/articles/CBMickFVX3lxTFBZaU8tOWN4NmxPdWNqR3BMbkY3eXM4aVFVbHVEZUl6UVhJbFpWZHZYOWFDYWZ4bWJDR0Q0OHVyN0FBblYyVWNDSFh1aldMOVhQRVRfWkhxeTdTbTV3WGs5a1ZYSDdkTTdFSThzY3R6U1hrUQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-12 [【视频】蔚来2024年et5](https://news.google.com/rss/articles/CBMia0FVX3lxTFBGWklRelYwdHBDVDZWcFFWZGsweXVkemd4ZVRNMGtzTFMtbTBsc3Y0MGgwbzVIV1dsQVJzSXB1OVlOM0swSzJqejVkQzd0OVBqdEZlSFBBY21ZcGZySTFpNE1Fc3VyUW5lR0hz?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-11 [开电驱豪华SUV跑长途到底靠不靠谱？深度横评神行者8、理想L9、蔚来ES8，谁才是真正的全场景伙伴](https://news.google.com/rss/articles/CBMickFVX3lxTE5HcWxia3ByM0RiRmJZenV1aVZ1X0U3ZXNMcXkycDJuUW80clpIUTNxRHdteFRDNHJBcnBRbUZMYTBmWTBDTnY4c3hzeVpOcmVEWi1NVGtaU3d2U0RXZVZ5MVE5ZEVJVTEzLWhaTWNGc2FFZw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-11 [25-30万家用买啥车？三款纯电SUV横评，按需求闭眼选+FAQ](https://news.google.com/rss/articles/CBMif0FVX3lxTE9kVmMyTXRTRWRtUzBST253OE81ZGNQOUFkVDRnMC1uWWotOGFGOTBrVzc5eU80RUhnYXdDXzJpYXNkRjFVbTNCcHcwa1pTejdGRk1xWnFhYy1BejVjVmNjVnZjMHZtMnV2LW1WSV85eHMtT0FQWGdEcXRlTjN4SHM?oc=5) <sub>新浪网</sub>
- 📰 2026-10-11 [【视频】第一视角分享蔚来ET9地平线版5天使用感受](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBmVWVNOUFGbjVqYTkzMWQtLVpJYTdyUHk4RVZiRkVIOFBXS1prb1A3S3RhRi1JenR3T21EaFpTby1rc3RlWl9QOEtmYU9tQlRXcjBubHUwdWd6TlE?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Huawei</b> (406)</summary>

- 📰 2026-10-12 [Avatr T09 six-seat SUV confirmed for Australia](https://news.google.com/rss/articles/CBMiogFBVV95cUxOQl9BeUJnU0JpblQ0QXdDZFhhUnF5X2xreTZ0UEtrSHVScXhSQVZqZ3pPQXctR1hLX2tXSkUzUVVncDVJVHpzaEJJbm9yMG9SSUx2TjhhelFaSjQ0QktpSDFnQWVVWlhLOFN0ME1zcjdKVzdua0gxX2FmQmdxMFkxMndyRC1PMWtPaTA5WTZwcEQ1Wm1ONjRhbDV1a3pyb3BaNXc?oc=5) <sub>Carsales</sub>
- 📰 2026-10-12 [China's autonomous-driving veterans pivot to embodied AI as capital shifts from "storytelling" to "demanding results"](https://news.google.com/rss/articles/CBMidkFVX3lxTFB2Y01aZHNqandfdHZSRkF3MGYtTWw0eWVVbk5FdjdNZzBHbGd5Z2lQYm5jelQ0NThHMWRIU2Vfd3hrU0s4WFZBekNXRDJWQ3VneDZhak05MTI0RjRVcUJkXzJMM25aWnpVSVlBZ25WQ2V2MndJdUE?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-12 [增程SUV智能大横评：小米澎程、启境GX7、理想L6谁更值得买+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5JRUtWQUVKRmhmWGl4Sm1TTjBhT3IyNFZ2c3RreUhwbEVFUzY3UmN6bGhVNGpfRTlWY05sbnhnTGRYUzNpMlgzY09aa2o0eVpOYk0ydGVxcElQMFJYTFk0?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-12 [【视频】华境S大六座SUV绕不开的选择！华为鸿蒙座舱华为乾崑ADS 5](https://news.google.com/rss/articles/CBMiXkFVX3lxTFAzUGR0OFliYWp3UHpBQ19oX284c2U1NE1hd0J1SnNTTVR3N3FzeFdUMjRwU0V1SGVJUDNRdndGQ0pISXJXeEpOX0Nkc01PQzdTTUstZ3c0S3JTXzU2Q3c?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-12 [Changan-CATL’s Avatr unveils flagship T09 concept at 2026 Paris Motor Show](https://news.google.com/rss/articles/CBMirwFBVV95cUxOREptc3VvX1JJcmFUN2FOd20yQ3lWODlNM2tUQU5nSHFldTkwdUtZVWVYTkxBbWtab0FaSW85MjlHdjRaaEVwV3RCZGM1a0NEU3N0ZTRHamlWSzJuYnBJeFNRV09aUXg3RlFRQ2hOdmUyVkdBdWd3LTNhblNUQnE3cFYtaVZrT1pLakViaVNCZGR4a25LWG1IYnZETE9ZRmM5NlVYNnJfUVFVcE8tek9J?oc=5) <sub>CarNewsChina.com</sub>

</details>

<details><summary><b>Baidu Apollo</b> (54)</summary>

- 📰 2026-10-10 [BIDU's GPU Cloud Revenue Soars 283% In Q2 — CEO Says AI Business Is Now 'Firmly Established As The Core'](https://news.google.com/rss/articles/CBMi1AFBVV95cUxNMS1oZ21ORWQyd2FnbEczVHoxNmRtYTR1bF8yZ3Q0UTBheGVvSkRubGFIb3RDOXBKMWJ6cE5fZloyVkhaMFlFbWlfbUdJbDNFRkpTQ2NHbXBybTVGQ2szZjk3blBVTFpzM3pjZ1dNSU9WZG5xR0FyYzd2OXJSWjJFU3RFYnloTGtqdTdaY1g4eURubG9jTlBvZHFvcXp0R1FYOTlyVGJVcTVzN3BNN1RocXItc2pWYVZhb18tZUlSTndjNllCZlo2Rl8yaFlIVUJ1V29XXw?oc=5) <sub>Stocktwits</sub>
- 📰 2026-10-10 [约1亿美元融资落地，安全短板仍是哈啰Robotaxi绕不开的考题｜大鱼财经](https://news.google.com/rss/articles/CBMijwFBVV95cUxOYXdGVDVHc213QllpS0dxWXg3MGJDbnJnQXVTRWtRak5QcmZ1Ty1HR1VyVlJpY3R0aGstLTNFQUE4cWN5RDlxMl9EYUZJWjkwd0lQczV4WnlKUE1PNE9EWHB4N3VaQXFPdWUzall3bDJGMkg0Zi1TWEdJV0ZYUUVKZWNqVW1LOEdiRURWUFpQTQ?oc=5) <sub>搜狐网</sub>
- 📰 2026-10-10 [Waymo Goes to Wall Street｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTFA2Z3RvWEJLVEtPTDJWNVcyaGQweFBVUnZFb0RST0wxRWhCdUJudXJQeU9helBuODZrTlBDZlh4NF9zb3dyNjRxQ3BzTGpZLWJvQzNObmFlYjl1R010Z3hB?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-09 [百度萝卜快跑：东涌自动车测试项目10·20起展开公众试乘](https://news.google.com/rss/articles/CBMiVEFVX3lxTFA2QkNSRVhNeG9lbWl1WU9uRjJ4SmVDRnhxUS1wRV9Yc2tES01SODJXeXFGd2R3b2dJQ2UyRWlfU1I5d0ZySmliNEFRaEFIRlZBd0UyMg?oc=5) <sub>https://www.hkong.cn/</sub>
- 📰 2026-10-09 [从“卖产品”到“深度参与”：中国企业进入中东的方式正在改变- 21世纪经济报道](https://news.google.com/rss/articles/CBMid0FVX3lxTE1uanZ4SGtKLTJjY3I5LWJIdEcwV3htNGRhSTJ6MkJiQi0xNExYTzZTM3h0V01NeU41c2REU28ybF93X0J6Qmp1Ykl4cVY1b0VjMVJfaXRlWktuTlJIckQzTmtqWUJXOUdPOVhvd0Z1NFhYT082YXhN?oc=5) <sub>ZAKER新闻</sub>

</details>

<details><summary><b>Pony.ai</b> (134)</summary>

- 📰 2026-10-12 [港股人工智能概念股走强海致科技集团涨超8%_7x24快讯_新浪财经](https://news.google.com/rss/articles/CBMiS0FVX3lxTFBkWlk4OXlweUJKdmkyWE96OW0zYTk2ZnFlZDY3ZmZneFJoMFkycGxxZEx1VGVkYnZuTUlYRk9ZRGVPellVTkF5ZlJXRQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-12 [A股盘前速览：美股上个交易日三大指数集体收涨，光通信、中国资产爆发；证监会召开座谈会；立讯精密、工业富联回应遭美国337调查](https://news.google.com/rss/articles/CBMijwFBVV95cUxNaDMxSGhETml1andxWTEzNHR6cjBqNnM5SGlFdlBiN19qU0lKNjBNbWRxTklJa25FNmIzVjFZYVpDSFk5UndyZ0NhT3BIdDYxN0tkdnBhR3JjdWJ4VkJlWGIxemJRNWtCM3Z4S20wcVNVUUZoNjdPaU14SjcwZWJCVlBaZnRBc0xPRUtCNk9Hdw?oc=5) <sub>21财经</sub>
- 📰 2026-10-12 [小马智行旗下第七代Robotaxi引入英国伦敦 早盘股价涨逾7%](https://news.google.com/rss/articles/CBMiiAFBVV95cUxOeG5xVEZISTVFZkFKRkJwWm5JeF9VZ003NVFqYnBjMXl2SXZqNVJVYkxQVHVDdkVVb0FnV1JiNXRLd2Q3a3hwQ21QUWE2QjU3WXJNeUNTTnFfZVYzeEN2YXk2VVFyVnJjbmRmRGJlZkRYN004YXJUNEdnbm01elR3T3AtRnhFTlRv?oc=5) <sub>搜狐</sub>
- 📰 2026-10-12 [港股午评\|恒生指数早盘涨0.17% 东方海外国际领涨蓝筹_港闻资讯_港股_证券之星](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1uMG5fQzhKenBHOThFajRnNExkalhVOF9hNXpqa3hzM2o3R3VFQ1R2amRDd2VBQWh4WUNXU0h2Ukh2RVhpS1A4b2Z3U2psNDNBbmJTa3FwcDRaT2VLSmc?oc=5) <sub>证券之星</sub>
- 📰 2026-10-12 [小马智行-W早盘涨逾7% 正在推进将旗下第七代Robotaxi引入英国伦敦](https://news.google.com/rss/articles/CBMilgFBVV95cUxONWNQdTNYRmlDVTh5SkZYUlpmeFpHSEtOd0E1Z2ZTUW1URXl4LTVleVEtSHZ4MmZIRmExMTJPS2NHRlVBMDdYenRjY3dkeU5ONGpHUTJLUUF1TS13QmRxZkozWkxBUkhjc1dqbU4xeF9scWxucTFuWW5tOE5FV05WdjBFcXhhbzJtXzY0QktIelZ4Sk91OWc?oc=5) <sub>新浪财经</sub>

</details>

<details><summary><b>WeRide</b> (132)</summary>

- 📰 2026-10-12 [Fast and furious: Driverless race cars navigate the track in A2RL league](https://news.google.com/rss/articles/CBMiwwFBVV95cUxQd2VRY3F2MjdhdHhWelh5NkIyZXNHbll6UTltdld0OEROR0JIZFFFMjhkRERkd0p2bnhobXF4RDFfSmtad3JoazlZbFBuMFZDbDJYLWFrOUFXZWZTSkUwSXRtODhIWU0wR0tLeFB3SjJCSExQUEJ6a1pOaGlXdjYwbkdBYTJydWEwWVhVMTh1N0FSeXpZOGZhTjZQUWtmSDFvMm5oV2FvTUhDeGNlQ2dwa0hwZnlObmtwR0pOY015TVhQM2c?oc=5) <sub>The Star</sub>
- 📰 2026-10-12 [港股异动 \| 文远知行-W(00800)涨超7% 公司加速推进海外Robotaxi 部署 商业化进程提速](https://news.google.com/rss/articles/CBMiXEFVX3lxTE82dmUwektBMzliRTZIdjktTlZTQXZpbENvclNHMWlEUDgyTlhQRUp5VTZJNEVMdTJzSjJCejI4dmdkUlRXcm5SMjBNYXU1Z3VLSW1Na1ZMOG9USmN5?oc=5) <sub>Moomoo</sub>
- 📰 2026-10-12 [港股午评：恒生指数涨0.17%，恒生科技指数跌0.55%](https://news.google.com/rss/articles/CBMijwFBVV95cUxNMDRUTk1lRTVuaHAzejZnMl9EZ1BIVWFDRm50c2tGdzNwRFpBLTV1Z2wyb3JYNHdJbUl4U1oxRGZqVDE0YlpocUZmLUdyamxUdDZqbjFJV20zYVdoaXhzU3JBWkwzZ0RLa2RmQXVhUEkwREZuYnl0Y1NHTjhyYkJMZ29Hc2RhNVktbklJb0M1OA?oc=5) <sub>21财经</sub>
- 📰 2026-10-12 [智能驾驶板块走强 图达通（02665）涨超23% 城市NOA渗透率突破20% 带动产业链放量-证券之星](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1aU2wwQ20zNWNmbWFLX283SXptcTFuMDRiMWFwNU8yZ2hwZG1jNVRGcTVkb1hrNS1BWjN4YWhmRnlMX2NwOTM4UnJLbF91T3h2VXZSc3BENmk3X3dCekE?oc=5) <sub>证券之星</sub>
- 📰 2026-10-12 [AION Ray7将10月17日开启预售 中大型纯电轿车 竞争小米SU7](https://news.google.com/rss/articles/CBMijgFBVV95cUxOcVJUV2NUdXY4TFc5S0NhYWQzOUhkVEx5ek9jNzRPSXpkaS1rVWNVSldiMXZmY1lUUDU2M2N0UWVVNkI0dlFSMmdXSHB2TGVfR3JRcTRNVWIyMHVCNHBiV0RINjlkelRzN3k2M2psT29QTEN5T0hPcXRzVWxLOG41YmFjQ0g1Z2RLUWRJX21R?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>Horizon Robotics</b> (204)</summary>

- 💻 2026-09-29 [HorizonRobotics/Ego4WAM](https://github.com/HorizonRobotics/Ego4WAM) <sub>GitHub</sub>
- 📰 2026-10-12 [德系智驾新标杆，大众ID.AURA T6与丰田bZ5、马自达EZ-60的合资纯电SUV高速NOA深度横评](https://news.google.com/rss/articles/CBMickFVX3lxTE9WWG8yWDRpRG4yZDdQMmR3S0FhU1RycWlmTWhEMG9ZbGdFb0V3WXpUSlNqTkhjaXllZVREckNBZngyVG9GeUNiMTA3T0h2MTRJWHZQM1dUM1dSa05oQkZhNkJxUFAyMU9IcFdHY2g2RS11Zw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-12 [China's autonomous-driving veterans pivot to embodied AI as capital shifts from "storytelling" to "demanding results"](https://news.google.com/rss/articles/CBMidkFVX3lxTFB2Y01aZHNqandfdHZSRkF3MGYtTWw0eWVVbk5FdjdNZzBHbGd5Z2lQYm5jelQ0NThHMWRIU2Vfd3hrU0s4WFZBekNXRDJWQ3VneDZhak05MTI0RjRVcUJkXzJMM25aWnpVSVlBZ25WQ2V2MndJdUE?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-11 [3 Asian Penny Stocks With Market Caps Under US$9B](https://news.google.com/rss/articles/CBMizAFBVV95cUxPazhfSFlzSkFnSVozeWZuLXd4MUVjalZUYTdnUUZtOFNySW1oV0xkLXJXUzduem9jcmdDc1ZaUWdnUmFGRTU2VFppYTBHYmllS2xlMDBsM3hBVjB4UDQ0a2ZNZWRXQW5qbVdhSUxueFF5bm5DV09wZGtBTnNuUXRiSDdKYkRiVHloSGg4WVdpY3NxRzh0WVdIekVMcWwzS2VfYTFkSHpRODd1NFpIMVhSRk9TRjBzbGpRaHJiZ0dvZGdJb1B1MUpyNXNnY0_SAdIBQVVfeXFMTXhpRW1TTWEtcjFXU2M0MTZTQ3FaN2lZSUV0NWVFSERDb05vT2xMSlFQVUN1NzFzZlBMbTJ2NGRvbnBXbzg1R3VBZUFIdWh5bjBOV2tGUkZIQmMtWmdjVXBpSldlMFZRYndTMnRCSzhQVjI3X09TR0lKT05XTi1rT1RjSjRVVmV2RG1jc3JTTS1DNEFkeW5mMndMek9xcDhiNXpVM3lJV3JHQVlFSTVQRWduZlZISThILW1UMmNUNmlnSk9ZbDloWEhaQWE2NEp3dEpn?oc=5) <sub>Simply Wall Street</sub>
- 📰 2026-10-11 [英伟达、地平线领跑智驾芯片市场 双方份额差距年内缩小约25个百分点](https://news.google.com/rss/articles/CBMib0FVX3lxTE5PVE5FRDlWVm9fQ0RtRGFNY2htRTBva1BVRVZFOFFZTkVNdUJNdDB4Smlrd2ZXV25nUmVxMjVnSWFkTDA3aDVkSGVFTl9QZzRBQ20xckhIQzhVeGR5c1g5czFDTVJUeTktNFg4SWpPNA?oc=5) <sub>zqrb.cn</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (29)</summary>

- 📰 2026-10-12 [TomTom and DeepRoute.ai partner to advance AI-based automated driving](https://news.google.com/rss/articles/CBMijAFBVV95cUxQM25CX2RxVmJzRkc5bmNUMGNTUGxlSU9pOEw5d08xb3ZyWjEyRlNtcVJvVElNenQ3VVhlQ0ZhcXd0bjh5OVNnOG81LWlOUnVRSTZYeGFOaU53V2d0U0F0WjZpcVJHMXR1VkpSSjFjLWdFOFM1NEhOSUYyVUozb0VRc1FKeGRIdjVqYndUbw?oc=5) <sub>Yahoo Finance UK</sub>
- 📰 2026-10-12 [费莫一刘念邱：智驾无图的经验，也能迁移到机器人 \| 物理AI 50人](https://news.google.com/rss/articles/CBMiekFVX3lxTE00amwwNk9KSGJlbUNzcXBtdWFQZEZpNHZxcVF4ZHJoTFg3T2lhUjlZREU5cUx3X2hYckROWEgzalBDYURDVThkZk1LMnZlTmtvQUJlbTZ2RmtVNGJGczNGMEdxNkpURHRXQS1rQUs3UXhWN2F0Nk9HWWFR?oc=5) <sub>雷峰网</sub>
- 📰 2026-10-10 [赛豆AIVA ME7首款量产车能买吗？20万级AI汽车3个维度看清+FAQ](https://news.google.com/rss/articles/CBMif0FVX3lxTE9YT3gycC04RVo0SGljaUxQemtKSVZrZTdvRUNRV0gtVi1jbUNQTWhXdzZqenhTaGJUVVBac1VoSFhDcmowT29GTDhXUDNNWnN3MjRfRjNhVXYwVl9BZy10QTVaTWRTaFgycVl0X19ZaUIwa0lhZ2FMNUpuM013RkE?oc=5) <sub>新浪网</sub>
- 📰 2026-10-10 [观察｜28岁的姚顺雨坐在马化腾旁边，深圳的AI下半场要怎么走？](https://news.google.com/rss/articles/CBMif0FVX3lxTE80cFpSSElQR2dpM19kVS1DV29KSGw4eFFJMm1hX2dFU0doZDFxRzB4eVpPN3lGRVhBalVEMGxoSUlLX3JkbHVjdjJhTDdxUXdlMnRneGxGQ3NpMi1GSDlnZUN5bldsTjFINGZhMkZudm5kR2pZaEs0WGNUSk1oRWc?oc=5) <sub>新浪网</sub>
- 📰 2026-10-09 [赛豆AIVA ME7深度解析：20万级原创AI轿跑SUV，真香还是噱头？+FAQ](https://news.google.com/rss/articles/CBMif0FVX3lxTFBzaVFpNWNnbjNlQU1iTU13aTcwc2pBZERxVlV3RkpESjJRN1g4YmotNmNISW11eGtVXy1aSHBmeF9hQWxMeGdNRXBrd1lEMVpkRjJUWUxIbmxnSjgtZHpzT3h2VmxhZlNDd25oTm9sNDVVZm5NaDJyYkQ0RGVxR1U?oc=5) <sub>新浪网</sub>

</details>

<details><summary><b>Mobileye</b> (18)</summary>

- 📰 2026-10-07 [Uber invests in robotaxi provider Verne](https://news.google.com/rss/articles/CBMigwFBVV95cUxQQkxEa25xSjBNT0ZJMzZINk54a2txS3k0S0pvTU4wZEJ5eVhHY0FNRWlyaVdIcVhYdmlPQl9HVUsyUnlkcW1UVzRVc180dHNCT1hXV3ZUcms3Mzg5aUoyZENTUWU3VHJtRlFuQmp0dWpQRDlmU2xlSDQ1MnlEZW11YmFGWQ?oc=5) <sub>electrive.com</sub>
- 📰 2026-10-07 [MOIA America Launches First Autonomous ID. Buzz Rides](https://news.google.com/rss/articles/CBMixAFBVV95cUxQY2FmM1hNRDEzV0c3c2NSVklIUDBPU1VrbmRmNnRLV3lNRzRITUVHUldKcVNYajNSYXJkdTJmbzRGeWt3V3ZrcXlmanBfR2t5cjRKZlU3b2JHbUg3VUx0ejdIS2ZUT25DRm5KTGtzSm1OaEhhQ2Zsb2Zhb0tHMDlnaWhnOGJHLXBvYk1GYkNYVFJRb2M2R3BmamRnN3RMZlJ2a3JlSGc3VnNmcXBtVDdub0s2VjhXSDhKVjFDR1pIQjYwLUpI?oc=5) <sub>Fuel Cells Works</sub>
- 📰 2026-10-07 [Uber takes a stake in Croatian robotaxi startup Verne](https://news.google.com/rss/articles/CBMikAFBVV95cUxOMkFfTDhoaldrejJpdUNUd1JvRXN1MlZwYVZQRjdPQ19FM2oyWjgxTndscUdGWFVZaG5nSWVKNWQ1dVYtNzFNZ2t0VnFwaS1mOFpneG41RW51M19leE9XSUN5WjhGbjF0ZkUtRVI4RDBiSUxtX2ZCTDBUekNRN3p1ZXZzUFU5aXJ0cjk5bHA3aUU?oc=5) <sub>Dealroom</sub>
- 📰 2026-10-05 [Moia’s autonomous shuttles start first passenger tests](https://news.google.com/rss/articles/CBMilgFBVV95cUxPaXBLWlk2ckZabm9UeXdOV1lCZTRjaDBkVmk4bDNVRWVMZkxKUEVTOVBqZERzWGlySkROdEs0bkE3SURjaG44c1Y4M3lsM0NmSG95X0diNlY4cGJoMUp1UUMxVnFkQ2Y0UTR2UDdtdTFzczBDSHpId3ZmWDltWlY3Ulg1bHBYMzJweHhDOWkzd3lyVWwxSGc?oc=5) <sub>electrive.com</sub>
- 📰 2026-10-03 [We Found Atoms, Rode Wayve and Watched Uber’s Autonomy Clock Speed Up｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1QZjNLZlpHR2ZtcHFaUDF5bEE3ZktHQlNoN0E1amxaVEg0eUdQbElIVlVVZk1JdTlqZG1kbGZYVTBvZDdKRDRKVWlqa2dRNDF3aTN4dEpmdTdxX0dTVnlj?oc=5) <sub>finance.biggo.com</sub>

</details>

<details><summary><b>Aurora</b> (64)</summary>

- 📰 2026-10-12 [Self-Driving Trucks Win 5-Year US Beacon Exemption [2026]](https://news.google.com/rss/articles/CBMif0FVX3lxTFBBUmFCem5ScXN0T3VNUU1lLVRvTjIzWFRndlh2NkJkY3ROXzkyNTQwR2dnWEI5ekpHeGpGLXZ1a0tIS3EwaVlSZlJrX1RoQnRhWkEyWlZzaTFnYXlGQkJOWUd5emNWbG9Ha2NWTTJQVGQ1VVN3X0htVmY4TGVFWmM?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-10-12 [Driverless Trucks Can Skip Warning Triangles for 5 Years as Critics Object](https://news.google.com/rss/articles/CBMikAFBVV95cUxPZnNoVjlPOWlnYlRqNU1Od1Nzc0U1U0lhb1lBR0o5OFNHRTd6VDV3T1lCbzhtc0hVUWIxdHN1M3NLZlczUWlQMGRrVEhRQUtSUlB0VW1oeDVZMkY4RFlSM0gyNzZtMVNVUEFKczBGWU9xTzRjdFo2ZWNuUzVKaFdjTlFEU19sd3NsUU1OY3ZqX3o?oc=5) <sub>The Eastern Herald</sub>
- 📰 2026-10-11 [US grants self-driving truck makers five-year warning-device exemption](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNVmdoOEUzeWJzaUZ2TFo4TGkyTnNxQXFEM1hBX3poNEFTZTlDdXZZQ2x0M2MtMzBqTDlqNzduU2pkR2hMSTczeVAybEVfWEJoNFF1eTEyckV0QlJYQ0FoTzB3QkM4R1h3YWZiTi10QlI3LTM5WGVPVUtmZ19kN01MMjJVVFQwMEpQ?oc=5) <sub>mezha.net</sub>
- 📰 2026-10-11 [Iran steps up attacks as oil traffic through Strait of Hormuz falls](https://news.google.com/rss/articles/CBMifEFVX3lxTE5Ea1VPcUlLRHVzei1hblRoT0g1WTcybFJZNEhMci1aWkI4UGdTdm9TdmsyQjN0UFJVeC16WW5peFBSRDlGeC0xckw1RkJHSzUydVFrRDBTNWxfM0RVeHExazJFTDlBdllQQ3JrcFhOUEtJYUZvcTI4d3ZCcXA?oc=5) <sub>mezha.net</sub>
- 📰 2026-10-11 [Texas Roads Have Become The Testing Ground For Driverless Semi Trucks](https://news.google.com/rss/articles/CBMie0FVX3lxTFAyVTJ2bGJpZmtSaDFMQTF1dGxOQmdmTkpSLXVYLU51NmpYSmFSZUI5TF95cjdvY293TnRrQ2xZdDF4Wk54T2NNZjF4c2IxYmRwMDdyNDNCZDhLcFI1czBSN0VUc2FYOUt0LXR4QnFWdXpWaFJoc1FXOXV4TQ?oc=5) <sub>BGR</sub>

</details>

<details><summary><b>Zoox</b> (79)</summary>

- 📰 2026-10-11 [Texas Roads Have Become The Testing Ground For Driverless Semi Trucks](https://news.google.com/rss/articles/CBMie0FVX3lxTFAyVTJ2bGJpZmtSaDFMQTF1dGxOQmdmTkpSLXVYLU51NmpYSmFSZUI5TF95cjdvY293TnRrQ2xZdDF4Wk54T2NNZjF4c2IxYmRwMDdyNDNCZDhLcFI1czBSN0VUc2FYOUt0LXR4QnFWdXpWaFJoc1FXOXV4TQ?oc=5) <sub>BGR</sub>
- 📰 2026-10-10 [Workers erupt over DC plan to bring robotaxis to city streets: ‘This is bulls—’](https://news.google.com/rss/articles/CBMirAFBVV95cUxOV0lTd2hnYmFUYkdFYXB0NGhIdU1KUlZVT2hmQXBMeFkzTkhuNHFxN1RDalQ2d3hiMlZFYmJNR0lqUGdEWUtSZU1yeWREM2hLbWNaOExQeTJRMjJwZWVkWWVnTHdrOURNMi0tQlFIdDRnV1RVMXZ4d0N6WW5VTGNNSFpZcVJlRmlZbHlvM1FvaVloRWk3TDY1bDZNX1JQZC1qbmdta3Z4SmlUX2Na?oc=5) <sub>930 WFMD Free Talk</sub>
- 📰 2026-10-10 [Waymo's $5 Billion First-Ever Debt Raise Signals a Robotaxi Land Grab, Not a Science Project](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9BaGt6ckszSmpwTDVsOGUzQ29DXy0yc3BsVFdSTjNtZFZrR3dWYUd5TzcwSTYzUTE3MlVmd3B4UG1iSS1kRHpySXpFVlhRTWd3cjVCOUgwVW5FcWc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-10 [Waymo Goes to Wall Street｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTFA2Z3RvWEJLVEtPTDJWNVcyaGQweFBVUnZFb0RST0wxRWhCdUJudXJQeU9helBuODZrTlBDZlh4NF9zb3dyNjRxQ3BzTGpZLWJvQzNObmFlYjl1R010Z3hB?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-10 [Waymo Goes to Wall Street](https://news.google.com/rss/articles/CBMiXEFVX3lxTE9CNlVOd2gzcW5YMmZYM2xhTzdNdnZ6RUVjTFE5SnVFLUpGOThrLS1XMHV6LVBNRHhydnpScGozZjVCbW9IR195VDktLUxydFlQUGhNOXRBcXN1ZGc5?oc=5) <sub>YouTube</sub>

</details>

<details><summary><b>Motional</b> (53)</summary>

- 📰 2026-10-11 [Six Years into Euisun Chung's Tenure... Hyundai Motor Group Moves Beyond the 'Global Big Three' Toward Physical AI](https://news.google.com/rss/articles/CBMiZEFVX3lxTE1qSWl5SS12dk8yVXMwandrR090TkZkdzZDaFladGpmOGNZZDNrMGxBQV9zSkV5TXpVeXIzWGhKd0FVYUQ0ZFdsT1pEWGxZNDV1UC14N0FsZmxVd0ZFOUVkamhoMWg?oc=5) <sub>아시아경제</sub>
- 📰 2026-10-10 [Waymo's $5 Billion First-Ever Debt Raise Signals a Robotaxi Land Grab, Not a Science Project](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9BaGt6ckszSmpwTDVsOGUzQ29DXy0yc3BsVFdSTjNtZFZrR3dWYUd5TzcwSTYzUTE3MlVmd3B4UG1iSS1kRHpySXpFVlhRTWd3cjVCOUgwVW5FcWc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-10 [Waymo Goes to Wall Street｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTFA2Z3RvWEJLVEtPTDJWNVcyaGQweFBVUnZFb0RST0wxRWhCdUJudXJQeU9helBuODZrTlBDZlh4NF9zb3dyNjRxQ3BzTGpZLWJvQzNObmFlYjl1R010Z3hB?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-09 [Hyundai delays its in-house autonomous driving solution to 2029](https://news.google.com/rss/articles/CBMilAFBVV95cUxOM1BRRVUzZ21fMHFubEhHNHRGcFVDQTFwdkRMWnljalNhS193bHpKY0dLSUZjN2tXamRlZUZIZ24wdmh5cWE5bnI2MzF4Qm5lVXJlWFZqTXE2TkpFLUZJWExJQWY4RDFuemJJbmZWZ01DMmRoUG9yLUlIZHNnT3RVeHdYR3hMSkk4RlBfcjlHU0R6Mzhn0gGUAUFVX3lxTE4zUFFFVTNnbV8wcW5sSEc0dEZwVUNBMXB2RExaeWNqU2FLX3dsekpjR0tJRmM3a1dqZGVlRkhnbjB2aHlxYTlucjYzMXhCbmVVcmVYVmpNcTZOSkUtRklYTElBZjhEMW56YkluZlZnTUMyZGhQb3ItSUhkc2dPdFV4d1hHeExKSThGUF9yOUdTRHozOGc?oc=5) <sub>Motor Illustrated</sub>
- 📰 2026-10-09 [Pony.ai's Robotaxi Expansion Reaches Middle East and Europe; Goldman Sachs Maintains Buy Rating, Cuts Target Price to HK$202.4](https://news.google.com/rss/articles/CBMidkFVX3lxTE95VG5sWlNSQzI3MjVFNnBoYXVCTHVjNEpUdERqYWxIRVB1U1lGdFFYZ2FqWWdVT0JBZEtrVGxJODhVQ292U2Y4VlBJN09HUmxpZFlkN3dXUXhreFFWenZfcTljNWxVWXRhbC00VUpXNkctTHBXR2c?oc=5) <sub>BigGo Finance</sub>

</details>

<details><summary><b>comma.ai</b> (12)</summary>

- 📰 2026-10-07 [Researchers Find that AI Models Struggle With Even The Most Basic Driving Skills](https://news.google.com/rss/articles/CBMiuwFBVV95cUxNb2ZGRGxGZDNjLWU1OVBPNjUtUlJXR0hiVGV3WEJ1eUVnSWExMWVvRmJjX2NtQm9sX0plMTU3YzZwUm5ZTzVoSGttcXZmQ3BqbW40X2doNFMycUk4UWE3anlidy1vWHNYZndVZjZWLUYtbnlHeVBFRjJOaTF4SWxzbmotR0xsNkVIcEhfZ0M3LUs5R2FyV1lVdlRRU3JwakpQcXpBUzlEOEhsWlB3Q19EdXFhQjRvZDU5MHln?oc=5) <sub>Auto Spies</sub>
- 📰 2026-10-07 [OpenAI's GPT-6 Astra is the only AI model to finish a real-world driving test in a Toyota Corolla](https://news.google.com/rss/articles/CBMifEFVX3lxTE9iZmN2ZFp6blVBRnZUTkYtYTJ3b0hSb0xhQjZyQXh5MUN2T3ladUlEb1F1SWJzc3FtamZtazk4LTVUWVpNX0ZjbGZwMnpERk45TVVQWVA1RjBZVUxxTTAzTWpaV1JqUzIwM1I2Wk1tTzc3bDJpaWluc2JVam4?oc=5) <sub>Crypto Briefing</sub>
- 📰 2026-10-06 [AI Agents Tried to Drive a Corolla, Crashing on 8 of 11 Runs](https://news.google.com/rss/articles/CBMiuAFBVV95cUxONWxQTEZham1kc1J4S2lMNUh6OTN1QWhXbl92U21NUWZTZWhNUUdwcFVvUHYtVWJzSjl4TjlCeFhUY2ppMXd3WkkxaHJFRmFlNUN2NGFSSENnV2ZZYWRNZ3JIUjd0dzFlTS0wR3gtbmxXN3VHOUkxWWg2VVFpTVgzWGN2T3RPdEFJV0cyWjRPSVFyNWZTYjFyX0pzYjFEUWQwLUlfbGo1bm8xVUZXQmpyQ3pCNXV5ZE9x?oc=5) <sub>thetruthaboutcars.com</sub>
- 📰 2026-10-05 [Researchers Discover ChatGPT Can Drive a Car. Grok, on the Other Hand…](https://news.google.com/rss/articles/CBMikgFBVV95cUxNNnNwX0g5bHV4STJlMXNOcXRnYnBHWHNoelViM2pJSzFob3dvUVJIdFlDRDV4X09DSVloZmxCTk5NODd3b3RBR2JmWEJQRktXUTYyWDNveS15UEw0NnVfSFluMlJxZHlBb3NhYnRNdDJsZ01MbVNpOXY4OW9nQnBSYnFRQ1U2YVd3a3R2ZTY4VlJNdw?oc=5) <sub>The Drive</sub>
- 📰 2026-09-30 [A $999 Box Promises Hands-Free Driving. Its Own Code Says ‘THIS IS NOT A PRODUCT.’ Now NHTSA Is Investigating Crashes That Killed Three.](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPNFIyamduTmQxb1dKNlh5Z1hCYUhyemoyU2I2bjFUWjZQSDVFSDFWOGxlM1hnQms4Q1lpalg0bXlCTEZTdVJ3eGtNTjlLamY2eW9LX09IejF6SkJxSmZ2QjRkU1pUczlRY2g3cUZIN3hvSUc3a3pUWHVKVk40MlY3Wk5SX3dnOHBl?oc=5) <sub>Yahoo</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
