# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-10-05 · 1,233 papers tracked · 38 curated.

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

<details><summary><b>Waymo</b> (180)</summary>

- 📝 2026-09-24 [Our Vision for London: How Waymo can Support a Safer, Connected UK Capital](https://waymo.com/blog/2026/09/visionforlondon) <sub>official blog</sub>
- 📝 2026-09-22 [Introducing transit rewards](https://waymo.com/blog/2026/09/transit-rewards) <sub>official blog</sub>
- 📰 2026-10-05 [Black Baptist Pastors Take on Waymo: ‘God Created Us to Be Interdependent’](https://news.google.com/rss/articles/CBMiUEFVX3lxTE9SNEdXSWVfeXEwUlZBYzJmQjJDaVpuTFlzYTRRTVZVNTZPYzVnYWpwVDRmbzdZWlh3RElyeTNxUURTLTZ5OThnenNYZGIyMU5f?oc=5) <sub>EURweb</sub>
- 📰 2026-10-05 [Elon Musk admits that Tesla Robotaxis have a 'cat problem'; and one which Google’s Waymo does not ‘agree’](https://news.google.com/rss/articles/CBMilgJBVV95cUxPOFFUZWdBVm1CZFNRRmJYek10Q0xLNlV1TlByX1ljYmpUZWs0T0RMS19NQUppdDR5Mm44T0lSX1E3dlVvakdnNTAyTEI2NmVhVFM2S0ZVdE56c3VldzV2Ni1nYnl2ZmxFcUxfMXdLZ0tCeUlFZVdHSWprT0JUc0RObjNSZExUYWx6WUU1WjlMSHpVdkNGcFJhYjQ1Zzcza3p1NWQ5ckdDTjdfUGEyTTNxRDVWQWRKa1ZLaUxKYzAyS1hCMFJWSjhIcVd2MkItMGstZFJDZU9maUVPaUFZb3JtMFM0R2QwSTVJZ01aQVFIdi1YelJMNFRLTXJKY3FiU2hLTUx5WmhXT2dEY2Q3SG80cU1IM1ZSd9IBmwJBVV95cUxQTFc3UmtLMUlQSHp4M1NoYU1nY3BYdXZ1Zl9qSTBWaFFjMTZoOHlGZk5PdWhldkRPRW80Z2VVcmNxbm5Wd3BnZjQtNlhmZVpWQkNFX2JrTGlTdjJRNnhOaG9zVU5jZzhBR0xKQXotaS1seHN4UnkzU1d1cFJXZWd4blI2N2ZXT1dUYWdJVVZwVVBfSnByQjB2ZVM1dUtOOTJOZTVNVXBmWmlPRzNybkRUWVZ5Z295QmFZVktkMWRqSWt1bmc4LTdJZzNTSWgycDRuZ1IyUl9NYmZPN3BHY0tPZFlXZEZkTHZkVXAtdlRxVEtFNk9VU3BoSENtZWNqUkpkeUVya3VkSUVMZ0pqeTF0QzBQeU5jZ2xTV0lN?oc=5) <sub>The Times of India</sub>
- 📰 2026-10-05 [‘Our way’: Tesla faces fresh fight in Aus](https://news.google.com/rss/articles/CBMi1gFBVV95cUxQMFA1eXlIMklmSFppWldIOHFpMUYtamhiNWVKQ3F5eXNQR1ZzRzVyYWU3SnBOb0lXUnNKczYwWElLenl0Yzh3MTRWNmRPY3dVQnlSYVluSzl5WC0tcWpkMXUyOVYwSTdod2U2cTNmWE5rakJOTnRTcHktOElaNlNQMFIyZ0hEWUNwMHFJbGR4U3Zrb2NGV2xWTmE5SnprSENoQnc1Q3BlQXVSTUVJNmpIbmlNVkRqNjV0cS1FVmw5UUt1cEJGc2QyTFgzdF9uWmNIV0tZODVR?oc=5) <sub>The Australian</sub>

</details>

<details><summary><b>Tesla</b> (281)</summary>

- 📰 2026-10-05 [Gary Black Says He Accepts Higher Gas Prices, Increased FSD Awareness Are Driving Tesla Sales, but There](https://news.google.com/rss/articles/CBMi9wFBVV95cUxQc1EyQzJ0UjFoX290czRGeDlRbGtmblBhc09ndGFtY0hwT3BxQ1lWTzJENnBkNXJFMmNTWXJaNmx1YlpPbnhqLWtmTjhIelNEZEYwX3BnMFdQWGJnZmNXQk43bEVGbGxBNkxaQ084TGFJZnFBUlk5WElWaFJ5U0ZYVl9QSXdudWdOcnBsYzZ2c1hYUmVlOVNseVEtd2hqbmJfcTlOcU5CZk9aTzNLM2lwMGJGbzZLcVdvZklPa29zbk9Uc2MzQklxZ0NHaG5qOWJOVjNvdXh2dVlRRHJWb1JZT2xSRHlFa0Vqc0RsOTFtSHozdzVTVElj?oc=5) <sub>Benzinga</sub>
- 📰 2026-10-05 [Tesla wins over Netflix’s Selling Sunset star, who’s now ditching his Bentley](https://news.google.com/rss/articles/CBMicEFVX3lxTE1tRmpBVjI3UWxXNVZhdTJJTC1zbW9ySTZodGZYdVhxQzV3Z0dteHo4a3ViODhCWTNqeFNjMDhwR2pnaHA5OUotUkpOYkJwUGJHVTgyWFpWcTNjbXdHM0pyZHdKR2NaNldlbG5RSWRqenA?oc=5) <sub>teslarati.com</sub>
- 📰 2026-10-05 [Elon Musk admits that Tesla Robotaxis have a 'cat problem'; and one which Google’s Waymo does not ‘agree’](https://news.google.com/rss/articles/CBMilgJBVV95cUxPOFFUZWdBVm1CZFNRRmJYek10Q0xLNlV1TlByX1ljYmpUZWs0T0RMS19NQUppdDR5Mm44T0lSX1E3dlVvakdnNTAyTEI2NmVhVFM2S0ZVdE56c3VldzV2Ni1nYnl2ZmxFcUxfMXdLZ0tCeUlFZVdHSWprT0JUc0RObjNSZExUYWx6WUU1WjlMSHpVdkNGcFJhYjQ1Zzcza3p1NWQ5ckdDTjdfUGEyTTNxRDVWQWRKa1ZLaUxKYzAyS1hCMFJWSjhIcVd2MkItMGstZFJDZU9maUVPaUFZb3JtMFM0R2QwSTVJZ01aQVFIdi1YelJMNFRLTXJKY3FiU2hLTUx5WmhXT2dEY2Q3SG80cU1IM1ZSd9IBmwJBVV95cUxQTFc3UmtLMUlQSHp4M1NoYU1nY3BYdXZ1Zl9qSTBWaFFjMTZoOHlGZk5PdWhldkRPRW80Z2VVcmNxbm5Wd3BnZjQtNlhmZVpWQkNFX2JrTGlTdjJRNnhOaG9zVU5jZzhBR0xKQXotaS1seHN4UnkzU1d1cFJXZWd4blI2N2ZXT1dUYWdJVVZwVVBfSnByQjB2ZVM1dUtOOTJOZTVNVXBmWmlPRzNybkRUWVZ5Z295QmFZVktkMWRqSWt1bmc4LTdJZzNTSWgycDRuZ1IyUl9NYmZPN3BHY0tPZFlXZEZkTHZkVXAtdlRxVEtFNk9VU3BoSENtZWNqUkpkeUVya3VkSUVMZ0pqeTF0QzBQeU5jZ2xTV0lN?oc=5) <sub>The Times of India</sub>
- 📰 2026-10-05 [疯了？带FSD的特斯拉现在只要十多万就能拿下！#特斯拉# #model3# #fsd# #马斯克# ​](https://news.google.com/rss/articles/CBMigAFBVV95cUxQZlJKNFNOeHZUY1pTa09pMG5VeUJLenkyZFVOaVVlaGxLbTliLTl5NmY2bGxRM2xyLVpoUUM3ZGJpWGdTdUxiMDAzQ1FaU1hFVndrcm50Wkhwa3NsNHhmbTlpa00wNE80dk5laENiZzFMei01bDFiTTdLM1F4RGQzag?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-04 [Tesla's Cybercab Hits an NHTSA Probe Just Hours Into Its Austin Launch](https://news.google.com/rss/articles/CBMingFBVV95cUxOMkZDMGJqYmpUZjZLQTA1eUoydE42VlF0NUttVlJSZkxFb1RDZm8xT2lJUkw4czVaVUpQWFBJcVNnUE5oYUlOR2V1V01oaDJtcTAxdVB3S0xVbFVQZkJqUlZqRjkwNVh6eEFxZWcyeFBfSXZQU3pIU2ZtMnZ6cTRJRnhwbUNwTWtiQlhYWTZuekdzOGc5Q0FkRmhpRjN6UQ?oc=5) <sub>Startup Fortune</sub>

</details>

<details><summary><b>NVIDIA</b> (193)</summary>

- 📰 2026-10-05 [Greenko founders-backed AM Intelligence orders 20,000 Nvidia GPUs in $4 billion deal](https://news.google.com/rss/articles/CBMi1wFBVV95cUxQc0hqUXh1Sm85VE92UzIyV0NvV0ZCM2V5TDdZdzY1NWdQZ20zYkVvR2FYR0ZTOE04a015YXhwRzZSOGRjQlZKUjRoVjViU0c1U3pFRmdxLXBhZUpwb1VydnQ0eVJaSmJxVW5NM25sa1V3NlpKMm92Y1U2SXdnUHgzVTYwR0hZMTUyNkp4eFJTY1MyckN4RlpVMnUta1pYcUQ1cHdCdWZ6Qm0xZWdQRzBScmNjbjh5YXFmOXVycFlnbXNHRXNNNUlhZEVDVUkxdHFUZXlQTzliOA?oc=5) <sub>TradingView</sub>
- 📰 2026-10-05 [AI Memory Crunch Drives Price Hikes Even for Aging Consumer Electronics](https://news.google.com/rss/articles/CBMidkFVX3lxTE12ZVFjLWpSSkM0RC1Xa1d6MmpEeE43dlB6ODJ4Q3pQNDBvQUtoMXJmQWZmbDdNWVZqUHZqZlc3Zi1YRmozME5IYnFjSjVUdkUyM3F5dVFUb2YwcUhpRjBNR2ZITzZLT0dwZjBfOHVjbm9ZZW80MFE?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-05 [ASUS Ascent GX 10 vs NVIDIA DGX Spark: Same GB 10 Platform, Very Different Prices](https://news.google.com/rss/articles/CBMic0FVX3lxTFAtSlJxUks2cnFWY2FJd193TGoySkRhNmRhSDQyTEgyeVpLOUE4eVdhYkR5ZEJScElISDRlTkhyR3VxamRzampaTFZLV3FyOEZ4Z1ktQ2t0MHo3X3hmbi1LeDFhVFdTUUE2U0JpTEtNVlp5aTQ?oc=5) <sub>Techgenyz</sub>
- 📰 2026-10-05 [Why Did NVDA, HPE, CRWD Stocks Rise To 52-Week Highs Last Week?](https://news.google.com/rss/articles/CBMivgFBVV95cUxOWXpyYlE0eEpnNlp1Q1NuS2Z1azFRZ2k3WEZIODRyU3dfdW9Uc19zUGFsTUs0UmFCM04xTklnYnA3YUlDS0pHNVRtUWZELTBDZzBLSWotX3ZveUZ5ZnktbUJ4Sy1JU0psTXhhUmVnUVJoUG9FMlZEV3l2TGpBNEF1REo2bm9WSVU5T2UxeXhwUzVVSHR3aW9UZHpZZ0lkUXNrZl9UbTNSbFctSmE5cEV3OHdpSXNuZmpQd2Fzd3NB?oc=5) <sub>TradingView</sub>
- 📰 2026-10-05 [Volkswagen Picks Britain's Wayve Over Nvidia as Labor Chief Disputes Blume's Account of Contract Cut](https://news.google.com/rss/articles/CBMi1wFBVV95cUxOcThBbDl5ZldUaWFqLXgyWnMzSE52Njc3dmtrdlU0ZWtEbVpNR1Z3X0RLSGVtVThiaV9WSGEzYXYzVFVqZzNJUE0tYzh3S2tEUTBFRE9qUEl3TTJ0bmVRQjFzLWdXTnluemlLYVJyVjEtZExZazJyWHFiNFd5TmNrRExXdGVkekNKd3gxMUQtT2FaNUkwa2RJR2dDWU5sVjAwemNCcjZLbm1NWDc1SkhMYkVUZFZfTFFTTC1PcDNVbjNrc2RvYWwyQU5CUnlpaTcwTVRSQlR6WQ?oc=5) <sub>AD HOC NEWS</sub>

</details>

<details><summary><b>Wayve</b> (66)</summary>

- 📰 2026-10-05 [Driverless taxis deserve a clear run](https://news.google.com/rss/articles/CBMiowFBVV95cUxNd3FabkJBaUdFd19oSGgwS1NpT3oyWDA0LTItOFlKMmdXOVFNS3VBQnpHbW0tYmFZR0xua0VkZ1hVcDBVTllPQnZTNnpPc3FTODJYbUJuYkJiTjM4c1lMV0FmdFprcHlvY01abW9Pb2RGNVBuclhmZzZaSzZndk1taUdTQ0RraUtZOFliNlpuQUpoWmctVGxzOVZSSTltQ3czSTQw?oc=5) <sub>The Times</sub>
- 📰 2026-10-05 [Volkswagen Picks Britain's Wayve Over Nvidia as Labor Chief Disputes Blume's Account of Contract Cut](https://news.google.com/rss/articles/CBMi1wFBVV95cUxOcThBbDl5ZldUaWFqLXgyWnMzSE52Njc3dmtrdlU0ZWtEbVpNR1Z3X0RLSGVtVThiaV9WSGEzYXYzVFVqZzNJUE0tYzh3S2tEUTBFRE9qUEl3TTJ0bmVRQjFzLWdXTnluemlLYVJyVjEtZExZazJyWHFiNFd5TmNrRExXdGVkekNKd3gxMUQtT2FaNUkwa2RJR2dDWU5sVjAwemNCcjZLbm1NWDc1SkhMYkVUZFZfTFFTTC1PcDNVbjNrc2RvYWwyQU5CUnlpaTcwTVRSQlR6WQ?oc=5) <sub>AD HOC NEWS</sub>
- 📰 2026-10-04 [Autonomous & Self-Driving Vehicle News: Arbe Robotics, Faraday Future, TIER IV, RideFlux, KGM, Hyundai Mobis, Stellantis, Wayve & California \| auto connected car news](https://news.google.com/rss/articles/CBMi_wFBVV95cUxPVVFJRjdNVmIzTl9RVkgwZEM3U3NDdlZRTmd6TG1vX3pzTmJ2aXJDTTFKQllRSUlGelNFeTVMR3ZpUjhRcERqVUNaSlBUZGhWS1RwNlFwS1VMVzFDNEc4UTA3a3pXZnFGUHFwWkNnSnZiWmg3YmdPTVJRN1oxOGxJc2dnRU5Sc25zcVZhbUhNYjkycEJNamsxeUVaN3o4UG5nM2FzWGQwdEZIZ05wSTFxX0hSS1U0bTNlVkpjNXFCS3pJSVlmNG1Pd0g4SlVGZFV4UGNXMHVMZHhYckdkaTdCd0N1X0NhZy1XWUVfX0Q5aEtmcVdBLWFDZDlVSEMwRWs?oc=5) <sub>AUTO Connected Car News</sub>
- 📰 2026-10-04 [Silicon Valley’s uberX Rider Zero: Aaron Levie](https://news.google.com/rss/articles/CBMiiAFBVV95cUxON24wcEtKZzF4VXJmWmdpTWg0WUpJTVhZNkhaaUtrcEpnSEtRVGxMVktwdlMtVks5UGlRYlVBWDR2OE95c2tPazZaallyNzRxRkk0WklibVJKVk8wUWpWX3E1NDJPeUtxdFRWTk1kb2FndkZDYnpZWk5pZ2x6dzJ6eG43YXk4cm1F?oc=5) <sub>Uber</sub>
- 📰 2026-10-04 [Taxi union demands payoffs over driverless cars due to job loss fears](https://news.google.com/rss/articles/CBMilAFBVV95cUxObVJMZHg3TjRtY183VHpmLW9SaFlScnhudVZpNDlCbV9LcVF0OWJzak1nOVpUY1VqaWxCWW8yMWNhYkY2OVhPZGRKSC1iLTZwNm1SOVV5ZmZfcklYb0RrUmZWUjhORk5xSVh3S3pNZ0N2YzhzRkhHQ0hLWlpoMEgwS20zdUx3Yi11Ymc1aDNUcUFOM3pN?oc=5) <sub>The Times</sub>

</details>

<details><summary><b>Momenta</b> (141)</summary>

- 📰 2026-10-04 [Momenta完成约5亿美元Pre-IPO融资，已秘密启动IPO招股](https://news.google.com/rss/articles/CBMiXkFVX3lxTFBUUklfT3JjSURoZmd3b1pLOVpCOXZFMlF6ZlFVUEFqVjhCelMxSTVHYmlCMnV1UmxKR3NzWDg2RDlUTURiUXlFVVJCTklyejFVZ1lfbUI2NzdjcW5sWXc?oc=5) <sub>车家号</sub>
- 📰 2026-10-04 [【视频】盘点最像路虎揽胜的5款车型](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBIVk42X1hqbk54dG9ZSlpLcXJqZUhmWDIxWFk3N1AtSVlYSzZVYmFXVWRaWmRyVkNWbm8ybGxMdEtmQUwxbzloM1VYUnNWUzhmT1dBbWo2WUk5UzA?oc=5) <sub>车家号</sub>
- 📰 2026-10-04 [带激光雷达的豪华插混SUV哪款好？全新XT5 PHEV与三款PHEV智驾横评+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE5qQ3RuTmtxSm15d2tjWVhJQkhwODRaejI3UTRpVFV0ekxCWENaaUpqUVBCR2E1WG5IYUFFdmVvbnMxdEIzS0t3LTZNa0RqUGg1SEtnNTRBMFN5VXQ2RkdUWm02NFFjYmZTY2hFYlJVZ2NIdw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-04 [新上市的豪华插混SUV哪款值得买？5款近期上市新车横评，全路况智驾成全新XT5胜负手+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFBVZDVPZ3VaSWdtamxEQ29vQllfdHp0SDlVNGZQN0hLVXN0ZG44cWZyMllxOW1tUy1sWS1IQ2NTTXVWRzNGSC1EYmNTS1NuYlFObVF3N00teGxDSmFLZTcxNEZzT181cWhKb3hhWnhwYXlOZw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-03 [带激光雷达的豪华插混SUV哪款好？全新XT5 PHEV、领克08激光版、腾势N9与理想L8横评+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE96aHE4dWMtOF8yRlYyOUQ5dEk3TlNoSVAtZlh1cmxQVkxUMktLY25nLU1PSnU0LUE0N0tjZ3FfOWd4a183dS15MlI1THd1QU1mVnNYZEdQZEh2WUpHUzd3VVl6OFhRU1UyVWhoNFpGSlVuZw?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>XPeng</b> (212)</summary>

- 📰 2026-10-05 [Robotaxis acquiring a business case](https://news.google.com/rss/articles/CBMilAFBVV95cUxQdW9ncFVPWGlEZ0l1czRFWHRLWHBrbWFSTGFuQUJOZUotdDJlYWJoLVdvUWd3amxlcjRkb2M3V2kwOWZLMVBfbTlIb1pDN0NvYnJJOXNkUWhJb0dtR05WbW9oeEhaZ2kzOFZpWXByVXJ2cEZ1TUxaTld6WXNyWEgtakNnZ0JBMmZLb3NiSkRmV3hjZTlH?oc=5) <sub>electronicsweekly.com</sub>
- 📰 2026-10-05 [What Did The Market Misjudge About XPeng (XPEV)?](https://news.google.com/rss/articles/CBMirwFBVV95cUxQRGQ0aXBLS2p3cENUSFNqWnNGUVM4ZGhJeWx4RU0zYnNIYWxTOWJGVmhFV1U1bXNnam1ZVWpHT1o2WTNKZkl4NVVxay1lVm5QWU1PMVhEMGxwSFpuVldRS1ZIVmtsUkxqdGYzMGkyV29OYy05V3ZBTEk4bll6ak1hWTJZakhVSjhIWHI0QzFxbzBSMVVmbkpwR3l0QXBSSS04TVlEdEJrTXUyZ1RnR0ZV0gG0AUFVX3lxTFBaeEhOR1g3VEdaVDlqRVN3YnVmQUl2RDRuV3dBcklvVVluU0M0S1E3V0I1WTJqejNGMVh0SklVM1NKcmdPa0REdDAyVWFSOGZsZkF6UGlJSjRVSXNTVy0zSWxjWUxRQ2N5Z3J6UllGNXdqb29nb1RiVlE2Y0hiaHdjbjBBbnduaFNiV3N1SFQybVk2YTJJQ2xGT0RNTnl0Q2pTZGFaMDFCeEpDTGtQZllBZ3FIQQ?oc=5) <sub>Simply Wall Street</sub>
- 📰 2026-10-05 [小鹏G9L 23.18万起，值得买吗？5大核心卖点深度解析+FAQ](https://news.google.com/rss/articles/CBMif0FVX3lxTE11Qy1fbmZCaVA0b21pcDA1QzFiZ1k0MUs5NTB4SGNGSGNGQUF5WjJxTGZ3WlBYVXlPa3M1TGcydFBOSGctWEduWFRBaWFvZ0lyeE1Dc0NXc0NOckh0WjhmVnc2REhkOVE3dUlwZ09hZzMwXzdjb2RYWFg4dTQyRHM?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-05 [月销14000辆，小鹏MONA L03正在抓住被遗忘的BBA年轻用户](https://news.google.com/rss/articles/CBMia0FVX3lxTFBhTHNWRlNOUFVJdU1QbmF0UmZyaGEtcmVudEk5S1dZRGh0SmtCcEw4VDVIVlBQaVRkZ19QN1V3cF8xRTBHUWM0VXBTbV92d3NJUDVyZXY1cVk2TnhEWjZrSWVZdmxSSjJTUDdB?oc=5) <sub>车家号</sub>
- 📰 2026-10-05 [【视频】自驾途中的一次刹车，揭开了一位84岁老人隐藏28年的“第二人生”](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBhT29jYXdSY09BcTdfQndsTnI3dkU5NFE1bXEyN3k3d2V0XzJGZXdLUE5nRExWTXdhcnJvUi1EdWRKb180Z2U0b1hvWllhejU5VHNsekI0UHhHbHc?oc=5) <sub>车家号</sub>

</details>

<details><summary><b>Li Auto</b> (166)</summary>

- 📰 2026-10-05 [【视频】理想汽车理想L7 2023款 Pro](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5QMGZkckdvdnFwcnAtMGprX2JGVHk0WDl6b2pjQUxCYmJLUWxNT0hucjNPU1VGMmRnNlE3OVAzZ1Q4MjNHSFlFQ1JmYkJTTjNwZGVJRlVuSUJkWUE?oc=5) <sub>车家号</sub>
- 📰 2026-10-05 [四车横评领克900、理想L8、智己LS8与神行者8：谁才是30万级家庭全场景真旗舰？](https://news.google.com/rss/articles/CBMickFVX3lxTFBsd0JxLTlfd2wzSWRSQlFQd29OUGhGZlNtc3YtczBjZVlrNVhDRktlc0VKa2h4aG4yNkJPV0JCa3VreUZiZVVZSk1yMzFJSVUwbGo5TmZuRWRITXd4aURwTFFLWTFOWXk5a2R2cXU5RktBdw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-05 [碰撞前10米辅助驾驶“消失”，接管窗口再引争议](https://news.google.com/rss/articles/CBMieEFVX3lxTE9QWGw0Q3NENmJ2aXJxU2ZNUFM1ZHhNbFc3UHpMekFJVTFvTUVJdUZKbldibkkybXBxWERFcWlYRjdENHlHWFp3THFPMHBSRXR6Ym4zbEUwVl9EWDNFRDJPOHpLaXVvb1VmVUg3SE1ndXpyWHk3bWY2OQ?oc=5) <sub>新浪财经</sub>
- 📰 2026-10-05 [6座SUV的终极选择题，神行者8和理想L9谁更懂中国家庭？](https://news.google.com/rss/articles/CBMickFVX3lxTE50NDFFMUpyOEVncXFmeF9GWVI4YWtCZTJyc0FqMmpES1pMNG00Z3RiTGtDMWlLdk92b0FIU0pNQkNCYkFRaHFwQlowTkduT2hBTjN4Nm9WUHhkS2gtQTJEZFAxLW5PQzNPMmVnMGxpSnpNUQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-04 [Is Delivery Update Altering The Investment Case For Li Auto (LI)?](https://news.google.com/rss/articles/CBMiygFBVV95cUxQa0xCXzExZWxrWTFxUnpwbnJJNi1zQlRvV2VxRE9pOWp2ZGFRNHd6Rld4bGFjLTlQaHNMSm1FbmpScmVtVkU1MjBiYUVpa2VJWGVlcHg1cFFPSlpnOE9Gb1BLbFpYWElSVFRMT19LeVNfVktrS2NLbjlHYlU2amZFRnZLVEpMU3RyR2J4M2QwZHRHNFh2aGlWOXh6Ny04LXdwdy1mNGNSaHRKTDFyeTR0X1dpZnR6NUQxLVFBTTFtTmdvMzRmb1lxXzVB0gHKAUFVX3lxTFBrTEJfMTFlbGtZMXFSenBuckk2LXNCVG9XZXFET2k5anZkYVE0d3pGV3hsYWMtOVBoc0xKbUVualJyZW1WRTUyMGJhRWlrZUlYZWVweDVwUU9KWmc4T0ZvUEtsWlhYSVJUVExPX0t5U19WS2tLY0tuOUdiVTZqZkVGdktUSkxTdHJHYngzZDBkdEc0WHZoaVY5eHo3LTgtd3B3LWY0Y1JodEpMMXJ5NHRfV2lmdHo1RDEtUUFNMW1OZ28zNGZvWXFfNUE?oc=5) <sub>Simply Wall Street</sub>

</details>

<details><summary><b>NIO</b> (155)</summary>

- 📰 2026-10-05 [【视频】新到24年蔚来EC6 75度租电极品一手3万公里](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5JRlBXNUNpTUhEc0JLVl8xZzI2UFp6OHVXUHdZOHhBTXV6MnNyNjJ6ZVZJMVVMdXVWeDF2NkV2ZHQyN2Q2TWw5eFZpYktIcjljMEVmRGI2Sk5PYnc?oc=5) <sub>车家号</sub>
- 📰 2026-10-04 [Consumer Tech (Sep 28-Oct 2): Anthropic Preparing for IPO, Trump Weighs AI Stakes & More](https://news.google.com/rss/articles/CBMi2AFBVV95cUxOYXRIMGo5WmZ6bEZCYm5JVEZNQkk0dUhGSFFrbUhzUWVQMU5jeVlGdXo4LWtaQ3dYUmJCaWxuVHFkMVo4QUFGYzJ2R3lUSmFoRE8wMFRuaHdlNkh4TjhMcDhuaXV3M3lVMmM4ZXNUaWxYaU1NWk9kYVdsSXJIaWpQc01sZmJJZHhVRlRsY0pKWFczYjlOaVFtRG9kZkQ2U1VmT0RfaTkxajlqVUxCUE9wU2NwMk9zcGxGbnRzQnR5LU90dDRyZFJ4Q2l6UkVXQmJwM3M0X0tUNUY?oc=5) <sub>TradingView</sub>
- 📰 2026-10-04 [【视频】23款二代蔚来ES8](https://news.google.com/rss/articles/CBMiW0FVX3lxTE84SjhQOFI2ODVpV251dTljMWhkbEdSaDBDd25sM0Y1eElSV0N5em9DekRLcm5YdXJrOUlKaXc5Q0dxSjV3NXpyUzdNOHhmbndFM3FGSVBVVHBTcDA?oc=5) <sub>车家号</sub>
- 📰 2026-10-04 [近期上市的中型豪华SUV推荐？5款新车横评，凯迪拉克全新XT5 PHEV对比宝马X3、蔚来ES6等+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTFAtRWkzbk1Ra01UZFRGeDNRVG42Q3d6UmI3SGNuWkJfTVdyYzVPMDhHbVFNRE9YMU5sdWR2MEEyVnZPakJIMk1MZUxmdDFTUXYtNmhJbDl5NXdlOHl4TjA4?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-04 [【视频】蔚来ES6 24款75kWh，24年10月上牌，目前安全行驶了2.5万公里](https://news.google.com/rss/articles/CBMia0FVX3lxTE5yMkdWU3JLRDFuNmlmazRNZHJWOEtfcUNtSzFwSWxvM1c2UzBSSFhkYXJRNWtfWV9mUktHdzk2LXZXWGxwbVRHSDZwWmVmdXR6QnVScVhWalNJb0hGeVhTeHdHekM0MTNZaTR3?oc=5) <sub>车家号</sub>

</details>

<details><summary><b>Huawei</b> (344)</summary>

- 📰 2026-10-05 [Huawei, Qualcomm strike multi-year patent agreement across 5G, AI](https://news.google.com/rss/articles/CBMiuAFBVV95cUxPWi1LV3ZjcVpUUlNmR2RRZ1MzQld5dDRYSmxTV3FrVFQ5S3dPWkxBZEVOV1N5VXFPX3lEdnFoU3JWNl9Pbk1hWFVWb3h1NzR5bEtqTDdxZHRnaG1NXzdjLTRvLWZ5NEMwSXFHNGwwVkR3NnU0YnlUQ0RyOUJfRFdHOW43X3Y2bWtsZkcyLVkwbUhhMHVBbzRkWlNlaVpIczVLWFBvVjAtVnRxUjFWX09mNnktOHN4RHgy?oc=5) <sub>South China Morning Post</sub>
- 📰 2026-10-05 [Huawei and Qualcomm Announce Broad Patent License Agreement](https://news.google.com/rss/articles/CBMi2gFBVV95cUxQdWlYdXdzM3hISHliTjBqckVfU2Z0SEpjMkgtRUJucU9TZHAtd0dCemJJdjlXOEZKb2QyTlBqWjc5dXN4OUVKNHpqdHZqa3ZzWjdib0pIcmlJRV9IX1ZKUGdhNkoyYnl0Y1JiYU05TGQtV3JyNmsxTnVvcURyRmU0Y1NmbG1WY0tuWnBZVFJFWTdNTERWb0syczFHUHlrVkhxOVFsVUxlVlcxMUhHWWF5bDZMdEVyWnMzb2Mxd3V3V0ladTdDejItMWh6dTd6M2R6TndSMUR5V08zQQ?oc=5) <sub>Bluefield Daily Telegraph</sub>
- 📰 2026-10-05 [Huawei agrees to a multi-year patent licensing deal with Qualcomm](https://news.google.com/rss/articles/CBMi0AFBVV95cUxOX3REVUhLMjVZbDYzaC1VTmNIejU2aGFVOUNOdXlzTno0VWtNRmIzN29IUklzWUp6YUNBb096a2lIX3l3TEFJQTlab3ZwNXhnSlVyajRHcDlqU0RoM01NS3psb25jYVVNWFQxQkZKOW12ZVpxSHRpdjJ1ODBXYV9MS1dtUjBWcXlZeV9LS3NJSWV5ZWdueDFBNlNobVVkblRRWGhwUkZibzRvd2VEM2J3bHIwVHRtQW5DeGFkZVN0cW9NS255WkVGU1RmOGI2VjZo0gHWAUFVX3lxTE1FTGlIaUFQTVV3dGNyMGFoWUhCM25CUTY2UmFjNkZkYi1CeTNKYXY3RWswNDhlUzBuR2xfNVNKcTE3LVAyVVFmSWhUaWhNRElkTVlHMHV2NXlMRkdiY2syMVpVZjhaelI3QW1NdGE1YXdrcTNxNkg5a2t2UzRUTXFVLUZCMllVQkFwMmVyTmxsMWwtbTVZWUxhYWNQMnY0ZF9TcVBIT0hhNHNoRWFXZjFsQ0ZTQnpiWXBfUTNYM3cyYmxFYjlrSUx5dXJfM2lUVEJqR0VCWWc?oc=5) <sub>The Economic Times</sub>
- 📰 2026-10-05 [Huawei continues to showcase practical AI applications at Sri Lanka AI Week 2026](https://news.google.com/rss/articles/CBMiwgFBVV95cUxNRF9NS202S044YmVneWZRMFZmWC1LZ3ZfLTBvSmpFeEJ5MWY1RU1nU04xMWxrX3Zha1VXbGc3d0U0R1FyS21ud1JZWHJBa2VUMHIxbklJWXRSMF9LY3p5MmpEbkFXTEE3UkxVM1RiMWJhWGk1OWJUWkxvVFpHLXRqSklBUHhXNkNWeGhhMm5rdHd5RFZwSVozb01OeFJEYWRRRlh4NDl2M2xJbG4wcmRSX2xTVWV4U0pJc0Q0ZGlvTFRmQQ?oc=5) <sub>Daily FT</sub>
- 📰 2026-10-05 [【视频】2026款华境S 全系华为乾崑大型SUV不到20万？](https://news.google.com/rss/articles/CBMiXkFVX3lxTE05aE9ZM2FUbFBTSEIxUDQtQ1FDekY3dHRVWFY3RzY5amFldDVJMVN3U2FCTnJSVXh2dFJTZVJTbFJFWHNPSmh0Zi1tc0RwdWJoTnJyQ1gzZHdvWm03RWc?oc=5) <sub>车家号</sub>

</details>

<details><summary><b>Baidu Apollo</b> (48)</summary>

- 📰 2026-10-05 [Robotaxis acquiring a business case](https://news.google.com/rss/articles/CBMilAFBVV95cUxQdW9ncFVPWGlEZ0l1czRFWHRLWHBrbWFSTGFuQUJOZUotdDJlYWJoLVdvUWd3amxlcjRkb2M3V2kwOWZLMVBfbTlIb1pDN0NvYnJJOXNkUWhJb0dtR05WbW9oeEhaZ2kzOFZpWXByVXJ2cEZ1TUxaTld6WXNyWEgtakNnZ0JBMmZLb3NiSkRmV3hjZTlH?oc=5) <sub>electronicsweekly.com</sub>
- 📰 2026-10-05 [#深圳无人驾驶网约车关门打不开#深圳宝安乘坐萝卜快跑无人驾驶初体验在百度地图导航的界面里点打车，看了下萝卜快跑比其他运营商都便宜，干脆就体验了一下。1️⃣首先，上车点不能任选，叫车后会弹出一个你定位附近的地点（通常是主干道路边）让你步行前往上](https://news.google.com/rss/articles/CBMiY0FVX3lxTE9IdGVCVVVGeUY1UTR5bEpHdWZHTTBlcGx2VzJESFlrTVRPN3pJSVdjU3ZLNDdYaFZKaWpNb2dBM3ZPUFRRNUN4NTdzWDRTQ3N5eldIQnE0dVZPYk9PRHRqY3Nydw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-04 [多花5万换224mm车长和36马力，格瑞维亚和艾力绅谁更值](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9KVjVEeXZwTFdsMHVZSThyNHZqengwRVV6OFFVZ1k2WE9DUl8tclBiTnhIa2U0OTZkZWgzUkIxeHEyUUhfdC1Mci1CYUw4S0xlZktxM0NRMkhzRFE?oc=5) <sub>车家号</sub>
- 📰 2026-10-03 [ASTS Retail Sentiment Nears 1-Year Low As SpaceX Turns Up The Heat In Global Mobile Race](https://news.google.com/rss/articles/CBMi0gFBVV95cUxNUFlfalRZc0RObmR5SHpnbFg4VmNCMC1HcVdkQUJJZk1JMkVvZXBFdG5nQkZ2b1MwSHN5eVVod09GVnZqWnl4TlZhcUJZc3BMVzdZdmNpT3h6UWtoVFpkSDdWZ0JZdUFtcUVqaDJ6RDlURExmVnZNRUFKdDVIYWFOaTNJXzJCWHhWQzJwOVo0emZsTFd5VlRIN2c1NS1QNEZ0LXpDa0FOREdDZ3BGd0MwTkxLRkRPSm1PajZOQ2FtVXRrUkZ6cERyb2FhZzBSZTZrMUE?oc=5) <sub>Stocktwits</sub>
- 📰 2026-10-03 [特斯拉大涨市值1.49万亿美元，别拿Cybercab当“萝卜快跑”](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1hSUFDdWNpc3RBaENGQXFMZFRBRFdnOFM4TC1NUjlhZmxpYjk4aDA2RWRfT3NyUlFQdjNiT19jMVRTdkFaSnB1M2t1ZUhVc2otQVhRaFVHZUQ0eUE?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Pony.ai</b> (110)</summary>

- 📰 2026-10-05 [Robotaxis acquiring a business case](https://news.google.com/rss/articles/CBMilAFBVV95cUxQdW9ncFVPWGlEZ0l1czRFWHRLWHBrbWFSTGFuQUJOZUotdDJlYWJoLVdvUWd3amxlcjRkb2M3V2kwOWZLMVBfbTlIb1pDN0NvYnJJOXNkUWhJb0dtR05WbW9oeEhaZ2kzOFZpWXByVXJ2cEZ1TUxaTld6WXNyWEgtakNnZ0JBMmZLb3NiSkRmV3hjZTlH?oc=5) <sub>electronicsweekly.com</sub>
- 📰 2026-10-05 [Weekly UAE & Qatar Financial News Roundup \| CSC Financial Launches Operations at DIFC, Qatar Issues $3 Billion Sovereign Bonds](https://news.google.com/rss/articles/CBMiU0FVX3lxTFBVT19uSVRRc01aZ3JiNjlqb1pHTXk5S1NKTzhBOFJuZEVab0hGcVN0Zk5rR3RZMjhudk1VdmxSa2otRWhkZ3RNa1lFRHdBRUpqZjJR?oc=5) <sub>36Kr</sub>
- 📰 2026-10-05 [Pony.ai Unveils L4 Truck as It Courts European Tests](https://news.google.com/rss/articles/CBMihwFBVV95cUxPWnpIQkRyZHVlcS10VS16c2tfRXNteW1rck5JMl9DT2ZaUGh6UWhwRVkwQ0ZyWjVTRkFYWlFjc3o4Xzlhb2JCM2J0a1EzQnVCdVJEcS1sSnJJUUVYSmtINFl0OHB2c3JuTndJZGhtNHdPa1l3TGFsM1JwcktaV1RZc2k5SGdkNHM?oc=5) <sub>streamlinefeed.co.ke</sub>
- 📰 2026-10-05 [深圳乘客被无人驾驶车车门夹手指小马智行称属意外｜即时新闻｜中港台｜on.cc东网](https://news.google.com/rss/articles/CBMijwFBVV95cUxNRUlEYlBCVHU5UjdZZWJNbmlJZi16Y2owR0VOc1VYLVJwUk5kb0Q0T3dPclV3NW1EUVRCX2JZSTc4RE9oWE10eEhqMzVXX3FRNjZPcG04OGxud3dhOG1CZVRtMzVrZDYwT2VuSnAzby1ORGxISWFPUmUyYUU0N3U1czRIUVVicUtVbm1uaFNoVQ?oc=5) <sub>on.cc東網</sub>
- 📰 2026-10-04 [We Found Atoms, Rode Wayve and Watched Uber’s Autonomy Clock Speed Up｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1QZjNLZlpHR2ZtcHFaUDF5bEE3ZktHQlNoN0E1amxaVEg0eUdQbElIVlVVZk1JdTlqZG1kbGZYVTBvZDdKRDRKVWlqa2dRNDF3aTN4dEpmdTdxX0dTVnlj?oc=5) <sub>finance.biggo.com</sub>

</details>

<details><summary><b>WeRide</b> (106)</summary>

- 📰 2026-10-05 [Robotaxis acquiring a business case](https://news.google.com/rss/articles/CBMilAFBVV95cUxQdW9ncFVPWGlEZ0l1czRFWHRLWHBrbWFSTGFuQUJOZUotdDJlYWJoLVdvUWd3amxlcjRkb2M3V2kwOWZLMVBfbTlIb1pDN0NvYnJJOXNkUWhJb0dtR05WbW9oeEhaZ2kzOFZpWXByVXJ2cEZ1TUxaTld6WXNyWEgtakNnZ0JBMmZLb3NiSkRmV3hjZTlH?oc=5) <sub>electronicsweekly.com</sub>
- 📰 2026-10-05 [Weekly UAE & Qatar Financial News Roundup \| CSC Financial Launches Operations at DIFC, Qatar Issues $3 Billion Sovereign Bonds](https://news.google.com/rss/articles/CBMiU0FVX3lxTFBVT19uSVRRc01aZ3JiNjlqb1pHTXk5S1NKTzhBOFJuZEVab0hGcVN0Zk5rR3RZMjhudk1VdmxSa2otRWhkZ3RNa1lFRHdBRUpqZjJR?oc=5) <sub>36Kr</sub>
- 📰 2026-10-04 [Learn Why The Bull Case For WeRide (WRD) Could Change Following Slovakia Self Driving Alliance](https://news.google.com/rss/articles/CBMiywFBVV95cUxPWkVscFNKRlpIaC16UGlfWWNvVWlPdTB1MkdrMVMyM2VuRmIyRmRUcmM3ZUh1RGJiUlhfSTVzMDdQMl9SQ2hnVHkxRVpOUV9UTDQ5aTRXWVV3NlR3b01HcndiZUdCTzR0OEtpRDQyaXhVYUFEZjdfRXQzSU5HNU9reGNCdDVuSVNDMFZEOWpfRXQxVFlqbng2cmZlZVpJT1pyLU1ucm5fRDRrUGFpdTkycHo0bVRhRTBLVlpEU2llaVNZUFZRekhYR3hlONIBywFBVV95cUxPWkVscFNKRlpIaC16UGlfWWNvVWlPdTB1MkdrMVMyM2VuRmIyRmRUcmM3ZUh1RGJiUlhfSTVzMDdQMl9SQ2hnVHkxRVpOUV9UTDQ5aTRXWVV3NlR3b01HcndiZUdCTzR0OEtpRDQyaXhVYUFEZjdfRXQzSU5HNU9reGNCdDVuSVNDMFZEOWpfRXQxVFlqbng2cmZlZVpJT1pyLU1ucm5fRDRrUGFpdTkycHo0bVRhRTBLVlpEU2llaVNZUFZRekhYR3hlOA?oc=5) <sub>Simply Wall Street</sub>
- 📰 2026-10-04 [一周要闻·阿联酋&卡塔尔｜中信建投证券落户迪拜国际金融中心；卡塔尔发行30亿美元主权债券](https://news.google.com/rss/articles/CBMiU0FVX3lxTFBhSnhLSlZnelBIU21ZM3cxRzByVW8xRnRaVmY1SXptYW5FcHFpN2hJUk1BZHZ4SWpPdEpuc0R1eUdVdk9wNjVHN1ZCclRsWTloZ3Vz?oc=5) <sub>36Kr</sub>
- 📰 2026-10-03 [文远知行(WRD)讨论区- 股票评论- 股吧交流社区](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBMSGxrODJvZkF3TURFX0ZGS2lrdGxEZ3lkWGk3NXVneE9yLTJGWUFuSEhqa0Y0M0NLSXZ6RTlVcTlWOWstd21OVjRCUVExTGYtUHpKUjBsazE1RGdNVHhF?oc=5) <sub>Moomoo</sub>

</details>

<details><summary><b>Horizon Robotics</b> (157)</summary>

- 💻 2026-09-29 [HorizonRobotics/Ego4WAM](https://github.com/HorizonRobotics/Ego4WAM) <sub>GitHub</sub>
- 💻 2026-09-24 [HorizonRobotics/CogWAM](https://github.com/HorizonRobotics/CogWAM) <sub>GitHub</sub>
- 📰 2026-10-05 [零跑C10六秒破百，深蓝S05七秒内，四车同价动力差异在哪？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9YZldJQThCTDFtTEZBQkpTV1JQb3p4dGE1ODlaRXNNSzcxb05OVTlhNkFoZE9udTdqbFVZbmZMRVlTeWRXV3oydmh2NTZPQjZvYWVxMTJMaGk5eTQ?oc=5) <sub>车家号</sub>
- 📰 2026-10-05 [轿跑成为主流了？9月上市的5款轿车盘点](https://news.google.com/rss/articles/CBMia0FVX3lxTFBzc0NNQkRXdkQyYmxjTzVNcnllbDVwNU43aldMVEppSXZ4R3N2d3Z2QjByMTNNZktCcmxmemlZZ1RaNzJoWDN1aHNrLVR6NVd1MFBzeGc0ZmdFS3V3a1kwV1ZRMFJHblU5bFRN?oc=5) <sub>车家号</sub>
- 📰 2026-10-04 [【视频】蔚来ES9中岛地平线，新车现车没有需要等，咱们现车在售](https://news.google.com/rss/articles/CBMiW0FVX3lxTE81TlpWOEZnVHNFNU1DalNWa0hzVEtFeERmRl82S3BBQzNUWkRFUFU2ODBnTXVlUXg4RlJMV2RFRUZoSmNWY2dxQ183R05FOWU0eE9vcFpnVmw3WWM?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (27)</summary>

- 📰 2026-10-03 [赛豆科技首款车型—AIVA ME7正式首发，采用时下流行的轿跑SUV造型比例，并且配备大尺寸的轮圈与多活塞卡钳，车尾还配备镂空扰流板，预计是一台主打年轻运动的产品。结合此前的消息，这款车会融合豆包大模型以及火山引擎生态，并且有报道称其辅助驾驶将采](https://news.google.com/rss/articles/CBMiY0FVX3lxTE4tU1hIOTd3MWtGSUV0RjZPR3pKRTNVTGNzaXpkenphcG5FVk1pNnZZMGdIUy1TVi1SMW9JdV9KMjFPYXlqakw3MmhObmtMZVB2VlVob2RoaFJTcVFsU09OTnFVNA?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-03 [提供豆包大模型将覆盖20万元以上主流市场AIVA ME7全球首秀_热点推荐](https://news.google.com/rss/articles/CBMiYEFVX3lxTE83MUJRVjJpdG92N0xFSUpkdHlsMWdWQlpaWE1CYzQwblNiOFVMVURPRFZ0amZQTXNpdl9odkpOSk9SZVAyWDhadnBXbWozTHNjOXNkRmRRS2dXbV9BQndHMg?oc=5) <sub>证券之星</sub>
- 📰 2026-10-03 [又一AI原生车！AIVA品牌首车ME7全球首秀，量产或假以时日](https://news.google.com/rss/articles/CBMiW0FVX3lxTFA2cVdGVzNJZlBpODJxZXJnVlVaOXFjQ3gzcTRUOHhibHZ3VlAtYWIyWnFHQmRPbUdFd2lsWGtPLXpfRTZoMGhOcF96am1CeklVUnRTS0RFZkpEZ2s?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-03 [你的国庆自驾搭子来咯🥁！无论是堵车、窄路、复杂路口，还是泊车，小元都陪你轻松出发，安全抵达。#元戎启行DeepRoute ##DeepRouteIO##辅助驾驶##物理AI##国庆节##自驾游](https://news.google.com/rss/articles/CBMiY0FVX3lxTE9oQzI1QkRUaU5jRDFaR1QxMzBmVDRZSkVXb0FuWkJfUzN0MEh5NDZSVEhCR2hjUzhUdldrTkhEelNlZ0JPTE9SWEhaOXRHNi1rZ1hBQUNOWElJWF9fV3c5aHh3RQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-03 [AIVA ME7巴黎首秀，赛力斯这次想讲一个不一样的“AI故事”](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5wS2JvX2l0SXI2ODdxd1g3T09YeUNtRGlJRG9KTkhXU1VEOUtmZkcyNWdCamhKd2pLR1JEekxDV1ZTeWwxa3FmOHo3RDFMNkFTb1RJNzN6SnctMjA?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Mobileye</b> (20)</summary>

- 📰 2026-10-03 [We Found Atoms, Rode Wayve and Watched Uber’s Autonomy Clock Speed Up｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1QZjNLZlpHR2ZtcHFaUDF5bEE3ZktHQlNoN0E1amxaVEg0eUdQbElIVlVVZk1JdTlqZG1kbGZYVTBvZDdKRDRKVWlqa2dRNDF3aTN4dEpmdTdxX0dTVnlj?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-03 [What Mobileye Global (MBLY) Could Not Prove Before The 49% Fall](https://news.google.com/rss/articles/CBMi0wFBVV95cUxOTDFoVXlyNjVvYmJycldRVUhaOHNieXV1MGJlRDVWWlVmUXVPMUY5NUlHWV9PcTYyYlMxWGNxRXk2c3R6b293RThGVW9ONFBBaUtqSkJsRl9MNjRvVVAxRW1WdGdrUXRKaDJqS042RDBXODB5YkoteU5USVlhdlBfS3pGcnlpVzZ0al90dm51WndmSGNCSElQWE9JY3hHaVJhMFZTSGpSMDVuWGQ2ZWtDQVlxVUFHeHJRVFJNclNaS2RLR3RsQnZ1c05rQjZseGhSVzVj0gHYAUFVX3lxTE9LbTQwSTVOazZ1ZkxtRXhjdm5qSjluZjlEandjc3JUdWNkRGdwbGpYdmhNM0NIYlRrQjlMdnI4ZWZGM2FHOUV6SHF2TnJJMDlWTktBWEluVnVQZ2FFYU5WMUF4WS0zSXRmbkRDQzEyVmFUNmJzTFZwTzZDVEFIcXZVd3BLZUFHa1daeDdBako4ZFVseEVsSzE4UURFSmQ0Mnl4V01HZHdybXlFNXFIelVJMURQNC1GNVJKSXgzMTkxenhxLVB0dFlxc1FJLTBzMmh2UzJjaVhKMQ?oc=5) <sub>Simply Wall Street</sub>
- 📰 2026-10-03 [Grayson Brulte: Zoox Has an Intersection Problem, and Uber Has 18 Months to Own Its Autonomy Stack](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9Gbmp2RTY3bW1WaFdrMDhqeWVpUHR0WXNEcFA2eWk4Ukdidmx4bXp4ZmdoNFhUWGZoM2pTNVBCVUlJSUl4SVM0UlcwbERnMTNVYmlxTjlxYXBwV0k?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-02 [Mobileye Global Sees ADAS Momentum, Eyes Porsche Launch and Robotaxi Expansion](https://news.google.com/rss/articles/CBMi0wFBVV95cUxQYzRBUnBoMFNxTkNkYjFDNl9YbVpSRTVwb1N5SjFjMm56dEFiS0I2amZUQ1JqMHFTTlJHb2N2bkhlUXhOaTRpbHJIWWxhWWVBeUxsdlZ1bUtTdzRsZEUzV2NHWUpaVnN2ZzljWnhZSnlibjNHNjE5M1pyc21xekJGM1A3Z3V0SGZRVTVGSG1hMm9DWVlnSUhBQ3hKNk9yQjBZUU12bXN3MUFWc3k1XzZKXzZIeGh5bEVZaXpta3cwMjVHUGxlaHRINGhKdnhERU12TkRN?oc=5) <sub>MarketBeat</sub>
- 📰 2026-09-30 [3 EV Stocks With Up To 39% Revenue Growth](https://news.google.com/rss/articles/CBMikAFBVV95cUxNbktkTHB2ZmdVWjdmMG5GaWdrR0dyenFac2dnV2d3eWpIVGxmOHJIeVpZU0RBREthd2xEenRPODRhcHhyaDVYV0FGX1l2eVhtTVNDZV9kN2t5UlR0b0Zyc1MtdDluZkZpaElxMlJud0VIZlN0eldEWGZVZ1Z5MlRyV0NRdU04bkRaaVdVV05nejE?oc=5) <sub>Yahoo Finance</sub>

</details>

<details><summary><b>Aurora</b> (47)</summary>

- 📰 2026-10-04 [California Signs Law Requiring Robotaxi Companies to Respond to Breakdowns](https://news.google.com/rss/articles/CBMiaEFVX3lxTE5VS2twNXRVbmFiOG5WVTdLT3hzRDlndWc4NzVXR2dRRWJsUTlDVWJNTV9iV0xnX0ZLZ2ZVRkhRcXlMel9fRVhmWDdWTjJYZ1dvWGJPOHRVR3NXcDB4QkZNTVFGQWJ4VTJx?oc=5) <sub>Межа. Новини України.</sub>
- 📰 2026-10-02 [Aurora Sets 2030 Scale Targets as Kodiak Names Its Driverless Launch Lane](https://news.google.com/rss/articles/CBMipwFBVV95cUxOcUxDQ1dvcFluRHh6bnBzYTBhMmR2QXgyamkydGRYYUU1eTNUeGh1bnFObWMwd2Fsejd2YUdVV0lsRXZjMEtSdjEzV1ZWZUpZclZhM0Z3ZXdCUk1UZEhkRWtucXV5Nmx3RTAtV01rWjBRRDlaUmhRSjE5c1VWSXpjeE4tbFpuQlNfU3M5S0R0Z3VDUVRzNE9rUkFCRUlPM3psX3B0UTRISQ?oc=5) <sub>act-news.com</sub>
- 📰 2026-10-02 [Above the Fold: Supply Chain Logistics News (October 2, 2026)](https://news.google.com/rss/articles/CBMinwFBVV95cUxON25lb0VXdFQxb3RVb2EtWmJKYUloTW5yN3ZJMXZ4eWM2dmZHZG43ZktyNzJnWmptLVpMa0lmcG1BRmRMUGU1d1FYV1NKSUVqWkdfemcySTdGUl9kc05BS0J0YkMxVUpnMDNXYXhWY3ZTQUFQUEpxT2hMdGg5WEFGS1JQdDU4YnhqcWJjN3NkQVZMeHZrVTZhYW50ODl5MzA?oc=5) <sub>Talking Logistics with Adrian Gonzalez</sub>
- 📰 2026-10-02 [Kodiak AI adds its first retail customer for driverless freight service](https://news.google.com/rss/articles/CBMizwFBVV95cUxPOFdCYU4tdUVRZURuc2tfQ05rR0g4bVZFdTJxN3FLRm94bENUaWRqWUtBU3YwM3djSldXd3V5YjdiNTdwRXNOTUpoem4wdHQ4aVNlWHRtb3FQekk4blQ3OU5NaWZhSTQ3VVhwVlp6eFk5Vlp1X1Z1a1J4VmxZc1dnNld4TVFZTUtQTldpQ1pneGRWcHdRMU9CSkNSdlRIV0g1WHBLV3NKandOS1dlSnFiYVFqWFNsWXBrcjItcFhBY1NRUndfekxfUXJtcklRRmM?oc=5) <sub>TradingView</sub>
- 📰 2026-10-02 [Kodiak AI Autonomous Truck Hauls Fresno-L.A. Produce Run](https://news.google.com/rss/articles/CBMipgFBVV95cUxQZnBqQzJnc1RDRkF4QUtCT1hfM0dLdGNnSngtUG5UVDlNUnZ1TWtzNGNhdndLQzNxNnZfZG1LT0w2WmF0U19xZzVsOG05WTdJLTlFTDFhUEtfYTRVclpKcTZCczUwN25iTllqSDQ0dFU0bXM2a0lwcHRQTE04MFFDck1iOWNqQWVrRUJJeFJROVlsQ1dXYjAwRGZLdGtlMVRZaHFfTWxR?oc=5) <sub>Hoodline</sub>

</details>

<details><summary><b>Zoox</b> (85)</summary>

- 📰 2026-10-04 [California law sets fines for robotaxis that impede 911 response](https://news.google.com/rss/articles/CBMijgFBVV95cUxPblpMZUNYcmctTEJOOUVKT21YdEFDZ2FnNDdqX1FHOVpFY283ODV1ZlNaLTBqRkMybDhfNjJ3UVlFVlpSa1pkYlpQdkNIdUQxSGdUZGo4ZG00SVZnRF9kMGRmUmVJLWpNRXpaTm9WR3BCZTBjYndOQ2g3QVpsaHRfenVyVUhhSVlFOEZqSEF3?oc=5) <sub>Mashable</sub>
- 📰 2026-10-04 [Here's How Zoox's Robotaxi Safety Testing Will Work](https://news.google.com/rss/articles/CBMifEFVX3lxTFB0OXRqRHVQaDRiQ1FGU3NrUE5UVmRIQXFrSDV2X05KTEowTlZGQnl3QmptaThGQkg1NmdhUFZjUndSbmxRQThCQzRTLUtCWjlSRW15WmM2YzRYZTZxWTd5OFpxNWZ4dVJTajVrX1QwSk02ZU1NU2tXQzJhZV8?oc=5) <sub>InsideEVs</sub>
- 📰 2026-10-04 [The Minneapolis City Council Auto Know Better](https://news.google.com/rss/articles/CBMimwJBVV95cUxQWGFvNDdxWlh2RjVRR21FZm5Xb2Z6VUpKM25idG5qeGw5Zkwxc2JMMUhTR1VLdERrM2c1eGFMMVZaUDRQLUt6N05fOXM2QU1DcGFCVnFGMVlSc0ZzUjZUZEZORTcwSE5zZ1NIQld5S2phMUswNGwzWXlLaHN2dXU0ekJfQ3ptVDNpZ0pFLXlnWERqdTE3REJFWXlvMThIbWxuY0czcDFpcUNzd1p3eGdYd21oek9YY3FTNmk2TVQtMlRYNGVEUUpDbEhHb0VXcHlrUTFBS01veFdIOHlQZ0pNUkloejNOM2o1T2hrbXdMb09qeWUzSW5pYUM3cVRFZ05RWFhKaWRDa2UwSjRRZ3B4S2tMekcwT1NMSFdj?oc=5) <sub>National Review</sub>
- 📰 2026-10-04 [California Signs Law Requiring Robotaxi Companies to Respond to Breakdowns](https://news.google.com/rss/articles/CBMiaEFVX3lxTE5VS2twNXRVbmFiOG5WVTdLT3hzRDlndWc4NzVXR2dRRWJsUTlDVWJNTV9iV0xnX0ZLZ2ZVRkhRcXlMel9fRVhmWDdWTjJYZ1dvWGJPOHRVR3NXcDB4QkZNTVFGQWJ4VTJx?oc=5) <sub>Межа. Новини України.</sub>
- 📰 2026-10-03 [We Found Atoms, Rode Wayve and Watched Uber’s Autonomy Clock Speed Up｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1QZjNLZlpHR2ZtcHFaUDF5bEE3ZktHQlNoN0E1amxaVEg0eUdQbElIVlVVZk1JdTlqZG1kbGZYVTBvZDdKRDRKVWlqa2dRNDF3aTN4dEpmdTdxX0dTVnlj?oc=5) <sub>finance.biggo.com</sub>

</details>

<details><summary><b>Motional</b> (31)</summary>

- 📰 2026-10-04 [Uber Says It Has A 'Superpower' To Boost EV Charging Growth](https://news.google.com/rss/articles/CBMieEFVX3lxTE55ZnVFb2oyTzlTRlBCN1hmclR2NXNoOTBlVUZsMGdQVHo1RDBMX1BBdlh2ejBVZEtDZlhCdEpUNDN4eG4tZ3A0Z3RJZ0NvV2NUTFFTLWN0ZTVzWHBVa1dLVVN1aU9OV01MTXNGVjFyYWVvNHA2WDhzaQ?oc=5) <sub>InsideEVs</sub>
- 📰 2026-10-04 [Tesla Extends Austin Robotaxi Hours to 11 P.M. as Musk Tackles Nighttime Pet Detection](https://news.google.com/rss/articles/CBMidkFVX3lxTE40aTRzX3JId0lTcklpc0xaVUljQzJRc0NEeHVJMUM5bFcyQk5UTGgzU29BOW9jVTFyejFhVGQydGdXU28tY01wN3FUeHdXN2gzZm1GSEptMGdsN1EwU001TVV4R0pSTUJ1OVgtSVdJTHRkZlVvTVE?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-04 [Hyundai’s New Santa Fe Will Go Electric And Keep The Gas Tank](https://news.google.com/rss/articles/CBMigAFBVV95cUxNSDNOMnY2NUhDeC1FT01Hc0IxMDVGT1BiZkNhSnlybThvN2k5MkpfR3NaSG94ZmN3ZE1YSHlkNjcycU9FVktZRnZmdXBoMFJwcU16R1lPOEZlQUhLTFNWV3gxekQ2eFlaOTBWUmpjRy0xTURiOUU0bTZPLXA5TDNWUQ?oc=5) <sub>InsideEVs</sub>
- 📰 2026-10-03 [Philippines and Singapore Wrap Up Talks to Modernize 1977 Tax Treaty](https://news.google.com/rss/articles/CBMidkFVX3lxTE5xaDlQWXYwZ3NCQURZZDRRYUVCbnpLMVhUalJaMEVYRnFjb2JTWTFVZm1wWlhXTkVyRXFJY2Z2ZUVEbjlGcVpyQWc1ckFma3ZaajhjLVJLSEVwRVpNMGhIRXprOVl3eUJsR0hKLVprWkFBWEViN3c?oc=5) <sub>finance.biggo.com</sub>
- 📰 2026-10-02 [Synopsys Unveils Autonomous Semiconductor Design Agents; 50 Collaborations Underway with Samsung, Nvidia](https://news.google.com/rss/articles/CBMidkFVX3lxTE5JSGVJNUZDUHBaZGpNYy1nTEcteGdsaUF0WVBIdUx2Yzd1X01lSkhIbHFqaDhENzZTOE1Zc29Rc0VRU0xfY3pLSDdwbk9sQ01oMWJxamNfOHZhRTdVdXQxRnIxdHpFNUg5UXVRX1haeDVEd2dGZ1E?oc=5) <sub>finance.biggo.com</sub>

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
