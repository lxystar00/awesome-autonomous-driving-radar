# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-10-10 · 1,248 papers tracked · 38 curated.

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
| [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)<br><sub>Nan Yang, Zhanwen Liu, Linfeng Zhang et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 4](https://github.com/Zizzzzzzz/MVPruner) | Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings |
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
| [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)<br><sub>Shen Zheng, Anurag Ghosh, Gaurav Parmar et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 30](https://github.com/ShenZheng2000/WarpI2I) | Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs) |
| [G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance](https://arxiv.org/abs/2606.26017)<br><sub>Hang Yu, Ye Jin, Alessandro Canevaro et al.</sub> | IROS 2026<br>2026-06<br>📑 4 | [⭐ 6](https://github.com/HangYuu/G2DP) | In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors |
| [SUV: Future Scene Understanding as Video Generation for End-to-End Driving](https://arxiv.org/abs/2608.03084)<br><sub>Yibo Yuan, Jiacheng Fu, Jiangtong Zhu et al.</sub> | RA-L 2026<br>2026-08 | [⭐ 20](https://github.com/ASH-2046/SUV) | End-to-end driving requires a coherent understanding of future scenes, yet existing methods model these scenes using task-specific heads and output formats, with limited scalability |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 16 | [⭐ 345](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
| [Latent-Centroid Steering: Single-Pass Classifier-Free Guidance for Command-Aligned Autonomous Driving](https://arxiv.org/abs/2608.00237)<br><sub>Meibo Hu, Jiamian Wang, Pichao Wang et al.</sub> | IROS 2026<br>2026-08<br>📑 1 | [⭐ 2](https://github.com/codingmlinprocess/LCS) | Vision-language models (VLMs) have recently emerged as a promising paradigm for end-to-end autonomous driving, enabling agents to map multimodal inputs and high-level navigation instructions directly to executable trajec… |
| [DVGT-2: Vision-Geometry-Action Model for Autonomous Driving at Scale](https://arxiv.org/abs/2604.00813)<br><sub>Sicheng Zuo, Zixun Xie, Wenzhao Zheng et al.</sub> | arXiv<br>2026-04<br>📑 13 | [⭐ 367](https://github.com/wzzheng/DVGT) | End-to-end autonomous driving has evolved from the conventional paradigm based on sparse perception into vision-language-action (VLA) models, which focus on learning language descriptions as an auxiliary task to facilita… |
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
| [PointLAM: Local Attentive Mamba for Efficient Point-based 3D Object Detection](https://arxiv.org/abs/2609.21780)<br><sub>Xuanming Shang, Weijia Zhang, Chao Ma</sub> | ECCV 2026<br>2026-09 | [⭐ 5](https://github.com/PointLAM/PointLAM) | 3D object detection from LiDAR point clouds faces a fundamental dilemma: voxel-based methods achieve efficiency at the cost of geometric quantization, while point-based methods preserve fidelity but suffer from prohibiti… |
| [Vernata: Self-Supervised Learning of LiDAR Point Representations](https://arxiv.org/abs/2608.06919)<br><sub>Oliver Lemke, Alexander Liniger, Abel Gawel et al.</sub> | IROS 2026<br>2026-08 | [⭐ 18](https://github.com/rai-opensource/vernata) | LiDAR serves as a primary sensing modality for robots operating in outdoor environments |
| [Towards Compact Autonomous Driving Perception with Balanced Learning and Multi-sensor Fusion](https://arxiv.org/abs/2606.02979)<br><sub>Oskar Natan, Jun Miura</sub> | arXiv<br>2026-06<br>📑 44 | [⭐ 9](https://github.com/oskarnatan/compact-perception) | We present a novel compact deep multi-task learning model to handle various autonomous driving perception tasks in one forward pass |

## Datasets & Benchmarks

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Towards All-Day Perception for Off-Road Driving: A Large-Scale Multispectral Dataset and Comprehensive Benchmark](https://arxiv.org/abs/2604.27499)<br><sub>Shuo Wang, Jilin Mei, Wenfei Guan et al.</sub> | RA-L 2026<br>2026-04 | [⭐ 6](https://github.com/wsnbws/IRON) | Off-road nighttime autonomous driving suffers from unreliable visible-light perception, making infrared modality crucial for accurate freespace detection |
| [123D: Unifying Multi-Modal Autonomous Driving Data at Scale](https://arxiv.org/abs/2605.08084)<br><sub>Daniel Dauner, Valentin Charraut, Bastian Berle et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 400](https://github.com/kesai-labs/py123d) | The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics |

## Safety, Robustness & Evaluation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [CCFM: Collision-Constrained Flow Matching for Safety-Critical Scenario Generation](https://arxiv.org/abs/2607.04451)<br><sub>Ke Li, Kaidi Liang, Yuxin Ding et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 3](https://github.com/KELISBU/CCFM) | Evaluation of autonomous vehicle (AV) planners in safety-critical closed-loop simulation is essential for real-world deployment |
| [Lipschitz Optimization for Formal Verification of Homographies](https://arxiv.org/abs/2605.23203)<br><sub>Jean-Guillaume Durand, Panagiotis Kouvaros, Maxime Gariel et al.</sub> | CVPR 2026<br>2026-05 | [⭐ 2](https://github.com/jeangud/homography-verification) | The adoption of vision neural networks in regulated industries requires formal robustness guarantees, especially in safety-critical domains such as healthcare, autonomous vehicles, and aerospace |
| [CADET: A Modular Platform for Evaluating Distributed Cooperative Autonomy in Connected Autonomous Vehicles](https://arxiv.org/abs/2606.04072)<br><sub>Pragya Sharma, Brian Wang, Mani Srivastava</sub> | ICRA 2026<br>2026-06<br>📑 1 | [⭐ 0](https://github.com/nesl/cadet) | Deep learning models are increasingly central to autonomous vehicle (AV) pipelines, yet their integration has traditionally followed a monolithic design where perception, planning, and control execute on a single onboard… |

## 🏢 Industry Tracker

Latest 14 days of news, official blog posts and new open-source repos from tracked companies. Full daily feed in [`daily/`](daily/).

<details><summary><b>Waymo</b> (225)</summary>

- 📝 2026-10-08 [Sober Drivers Still Face Nearly 4x Nighttime Risk: Why Road Safety Demands a Safe System Approach](https://waymo.com/blog/2026/10/sober-driving-benchmarks) <sub>official blog</sub>
- 📝 2026-10-08 [Waymo Closes $5 Billion Debt Financing to Accelerate Business Expansion](https://waymo.com/blog/2026/10/waymo-closes-5-billion-debt-financing) <sub>official blog</sub>
- 📰 2026-10-09 [What experts say about LA’s autonomous cars and their safety record](https://news.google.com/rss/articles/CBMif0FVX3lxTFBWT00tTlEtbXo0cTVjakl0cnNIbi12cGExYTlmaEtKc0VYaGR4MXJTOUFFdVVYRUZaRG9zZzJTQThaci1iRnZsUkFSSVJhNEd1Z3Z3ZGhYYnVjeGFEaTQwdWRRY1g4ZUM1akRkcGZIOXlmWmE0LW8yb1VfaVNoQ1k?oc=5) <sub>LAist</sub>
- 📰 2026-10-09 [St. Paul City Council president seeks rules for Waymo driverless cars](https://news.google.com/rss/articles/CBMidEFVX3lxTE5tRFBKWXBuenFwbU91N1Z6WnVpb2tBNUZ3TDNFYlIwOGlyNXItVVBoa2ZUUExWOXpZekJHMWdoQXc3THJVcWtqM1FZTDM0eFBiSlNjanVLZ0d6SUVnR1Mzd2xEUFBJSEl0anNqSWhaWlpyYTBi?oc=5) <sub>Pioneer Press</sub>
- 📰 2026-10-09 [While Flock Cameras Spy From Above, Robotaxis Are Watching You From Within](https://news.google.com/rss/articles/CBMic0FVX3lxTE1YbUQtU2NhX1YyWlBMQzZndVh0MW5ES0NiNGJmeGdSZFZMQlZocG9jaEZYdFJmRXBXMU1PcU11dFZGQmhselo4ckVVWXZtMmM0V2hFUFlral96Y1pBdXN4dVAzaW9GenlVMnRhVTZKQktrTE0?oc=5) <sub>CarBuzz</sub>

</details>

<details><summary><b>Tesla</b> (350)</summary>

- 📰 2026-10-10 [Tesla renames FSD as Assisted Driving in Europe after German criticism](https://news.google.com/rss/articles/CBMiggFBVV95cUxNY2NOM0dXMWF0UzB4dGo4WjIyc3VaS2dOdWlqQjBKWFczV25acGx6VHFPTU5WczY1cTQwOG9QUmVEVmpDMVY4bVpfQnpXcXNqNEc1SXV4WDlzdlZfTVNxdU02X3NJeWJoZnpMVmF2NDB2M2dmZ2RENlVzNVpGNG9ZUnl3?oc=5) <sub>mezha.net</sub>
- 📰 2026-10-10 [Backseat Driving: PW Talks with Edward Niedermeyer](https://news.google.com/rss/articles/CBMizgFBVV95cUxOa240NEVpYWl2Q011cEYtQ2l0Uk9NM2h4bi1xaTk3X3N2RXExelNnZ2tnUUNXSkNnRS00SEExSzJjR2Q1YzdsN0N3NUxSNHJXNGl2Z21YcEUtbU5tWG1hOGJwLUVzMzNHZVpwNmNpNnpmNkNTZFBoV3lMNVR3WDR4Y3hGNVJMQWtMMmdOaU85bHJSeHFEWWFrang2bmJ6anBsbjdISEEtbTRGNXI5OGhhWXRvM2NqYlIwcXc1RjlTd3I5bHkyNW96UDdueE9IZw?oc=5) <sub>Publishers Weekly</sub>
- 📰 2026-10-10 [Tesla Renames FSD in Europe to Tesla Assisted Driving Seeking EU Approval: What Does It Mean for TSLA?](https://news.google.com/rss/articles/CBMiuwFBVV95cUxOZlNaRDdDRGVvT3c1YjRWLWItYXM0T3NmWnF2MjdpaU1CcVdLcmVoSXJxRkkyT3AxbFFyUWhRRHdoY1pZblI2bHVobC1Pb2JDME5EVlRFTDBaTUdfWTVzZDRQXy0xWU5CS2tQVXpFa3dldmtNb2sybG0wZnkzUmtaeTZ4RnJkRlVITWE4WW92U2F0cDd4YnFiMFZRS2JEdEtteXBKckdnRzU5cHFzZmJqQUFrWmtWSW0ySjJF?oc=5) <sub>TradingKey</sub>
- 📰 2026-10-10 [特斯拉FSD v14官方首发使用教程！ FSD欧洲更名Tesla Assisted Driving ​](https://news.google.com/rss/articles/CBMigAFBVV95cUxQQ3lWSWVJNEJnVHN1bmpuMHNWNnRpYlkzWllBSUJlQmZlUkNxSzVHd2FFOG4zVFVnc3UxWWJVSElQUVRObHdXR3JZY1dpMWlxUXFPNE1rckhJVVhTd1VoNE9Mc1dDUldSdVVMMzl1ZnpFbUNmaWltTUhKWkZ3VTdIRQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-10 [巴黎车展上演小鹏NGP VS 特斯拉FSD 智驾仅两家报名](https://news.google.com/rss/articles/CBMiiAFBVV95cUxOMTlRRnhPMHhGNkN6WlNfNUYxZS1Xd3VHdEN0eUQzT3RBcWlNTGttcFg2YkJhT091TFd5YzRCUEtZNS1BWVJtcXRHT1JSRGFnSjE0YV9qR21WcV9oVG52UmlFMWFDdFpET1RIM0dLODhIT1drbmZCUDRHYzcyRzlscTVvUExpTjVh?oc=5) <sub>搜狐网</sub>

</details>

<details><summary><b>NVIDIA</b> (219)</summary>

- 📰 2026-10-09 [Astra AI Agent Connects NVIDIA Omniverse Libraries For Simulations](https://news.google.com/rss/articles/CBMidkFVX3lxTE91N1Jpb3huRVJudUNsUUJDbS00OExXZnVDbU1Bd3lDMEYzNDduTGdPNDR0ZTF3NHZDYzItUVRzRkRDdzQwNGdzWElkckd3Q2lQcnJtUE9OTU14eWdiTlZ0UVhYWUNOY3d6RUo2UXJTNnFUZnNvamc?oc=5) <sub>Quantum Zeitgeist</sub>
- 📰 2026-10-09 [AI Chips Update - NVIDIA's $1B Boost for US Scientific Innovation](https://news.google.com/rss/articles/CBMiywFBVV95cUxOWko3RFp3TVJaOUUwNU1hZ0d0bTFFU1FCV3UtU2s1SGczclRkSUVENC1LdmZFT1AtODdfWm5xdTBEWW5UM21vQThkZkRzMU5FWFBCT1N2RFF6dC00ZEhzUjY1NXVtOXlzeVY1a0ozOVZoUFBuYWJQWG9POWh0WTFvRndDR0ZpV3FCVk9YVURiZFNQSDBpYnBsZG1iWk1zd2lEVUJic0pWMm1LanY2bG9QTlVlME9TS1ZDV1RTc3pfekFHT0xZREx2SUhlNNIB0AFBVV95cUxOdzc0WkdPMHRGVENHSjRUY2h4amxHd1V6SVIxZVJIZjd0TC1JdW5ydEZkVHZGdl9zVzNEeERhU3doOWlpVXJwRWdNLXNEc1FVbnBHcW5GaVFpN0dKZkMxbkx6V2drZlpTaVhFbzVLUjlUQkludVJ5UjZOcnpRdnlTbm9sQXpyVGt6U2Z0dU1nUDB5b01oTDQxbVFuWVV3SmdHbDJFRjFNSm4tOTNSZ1pzM2RaaEtfSHM2SnF1UW5MbmVEb0FmdGlka3hiTTRRb2xi?oc=5) <sub>Simply Wall Street</sub>
- 📰 2026-10-09 [Grab & Others Ink AI-Related Deal: Is This a Growth Catalyst?](https://news.google.com/rss/articles/CBMiswFBVV95cUxPekdOVWFvSHNaQ2JCMWJiYzVEQmVSd29XbWhiZjBlbFlxWFhCLVR1SnpPWk8yeWNZalFOVzEySHpGQ2g5SDNYTWZKTmVNNFRrOUFFUDROT1pMbTJNMFRYUmxzU0RhSU9xZ2pRQUtYN0N6UGJGN2FuUWFwdVllUUNQZ1hQSVdxRk5fUXl1UVZJdWF1aFoyMlNTVHczVkg4LU9QOUpPZkQ4ZnBURzFRcEptdl9QTQ?oc=5) <sub>TradingView</sub>
- 📰 2026-10-09 [Hyundai delays its in-house autonomous driving solution to 2029](https://news.google.com/rss/articles/CBMijwFBVV95cUxPOHF2UzRoVXFwaE0xeTQwazkzNi11dDhVa28yZS03ZjEybkhsXy1MMFVHdkc2YnJSVjU1R2I1dzVvZXdRRG05M192WGRzNlV5ZFJVYVVValhMbXVORExsNDZFRk0weWhES3lWTFJMcW9BMF9lUFJ5dERIWXFfQ1daTllHcXdBZUxXdHJoVkJPONIBlAFBVV95cUxOM1BRRVUzZ21fMHFubEhHNHRGcFVDQTFwdkRMWnljalNhS193bHpKY0dLSUZjN2tXamRlZUZIZ24wdmh5cWE5bnI2MzF4Qm5lVXJlWFZqTXE2TkpFLUZJWExJQWY4RDFuemJJbmZWZ01DMmRoUG9yLUlIZHNnT3RVeHdYR3hMSkk4RlBfcjlHU0R6Mzhn?oc=5) <sub>Motor Illustrated</sub>
- 📰 2026-10-09 [Nvidia's Performance in the AI Revolution](https://news.google.com/rss/articles/CBMif0FVX3lxTFBPNklJN1RfNTg2N09PZXQ0WVNSYVZ6Zk01MGtQSVpEa241Qmh0LTgtX3BmSGVLbjhBZ194TmhvejdhOHR0UF81MER4ck9tZ05jTHBSSHY4YUpTc05LRklTODk0enJrMHUxbjJvR0ZtMEl2TFBOQ29XeWxPTmxXZEU?oc=5) <sub>Intellectia AI</sub>

</details>

<details><summary><b>Wayve</b> (67)</summary>

- 📰 2026-10-09 [Stellantis CEO says Wayve tie-up can cut self-driving costs, development time](https://news.google.com/rss/articles/CBMi2gFBVV95cUxNYldMeElseFhadXkybkktR0swTklvbVVTZVpZazBhcUYyZGR3dHhUMUE2ZVVsOC1pbFRjcVJGajk5Tlo3bFhqeGRVX0ZSSmV3aHVWR1FyQmFYQTJfR1MxVFB6UUozLTNoRHNiMVUwcEpFTk51TEk0MUxuRlM2X0ZJRm8wemM1MVo2cFFQcGRlVVlkcUZmNnVDREUtTmdORnJVLXZ5SXRYT2VWLXNEdlFaSDQ1NXE4Y2syTm0waWpPUUpmWVBxTi1xMjRvTWZhTlRoeUNDb1h1OUtPdw?oc=5) <sub>Reuters</sub>
- 📰 2026-10-09 [Stellantis CEO says Wayve partnership will cut self-driving costs and timelines](https://news.google.com/rss/articles/CBMidkFVX3lxTFBmYUUzb1R1UkJYYmFlaGhZVVYzVkVqb01sWUJNWnZqVW05RGN6MVN0czVlNU1sUTBzTDRpam82UkN2THllajV2QnBFd05ON3Eyc3JTMDZmMTFDMlNXX2tsVXVyekVRUDJlOWFyYlpRNmJ5Q2Y4b1E?oc=5) <sub>Quartz</sub>
- 📰 2026-10-09 [Stellantis partners with Wayve to cut autonomous driving costs](https://news.google.com/rss/articles/CBMiuwFBVV95cUxNM0NRODlJdV9sMUY5dHdGSExQNlpCVnRNTGlObUdVX1ZkMGI5S1pIRzFCaFRIN1l4UmNkV09qS0tMZUVNNGVfclhMMzVCQ25IX1Z4eHJENVVkaFU0Z3hETTdrakhzSWszTHNPUm1NSUhmd012NHFrT2ZxWGlZYmRDc0UweFNIakNfaHZPNExKMFJ6ZExzZ2VjeUpDN0FDdHZyMjVKMFhlV1dWeU51WHc4V1Vfb1MwRkIyUDRN?oc=5) <sub>Investing.com</sub>
- 📰 2026-10-09 [Wayve’s Alex Kendall: AI driving will be required ‘like a seatbelt’](https://news.google.com/rss/articles/CBMilgFBVV95cUxPT1oxeTlZZkhJRk56T3VELVZRVzVZVXE4R3RnZG1MeEZRWlI0aXBVN3MxLVlyLWhNV1Z5bDNIRFBJN01ubG1kTEllcm54QXZ6Q2p4MG1wN0c3WnZoR3ZZYzlUN2lHX1dxNk56TFVMZHFMc0NmVDE4a3pMX2x3RS1ZbHVpdjQ0MGRlXzByWTRkMEVCX0lFdWc?oc=5) <sub>The Next Web</sub>
- 📰 2026-10-09 [Stellantis Taps Wayve to Cut Self-Driving Costs and Speed Up Development](https://news.google.com/rss/articles/CBMidkFVX3lxTE1scXo5UUFGQVkyV3pDcFlmSXhVejI2R1prVklCRmEwckNXZlJLVWI5SzlUdjhpcXg2WGJ3b3U5Y3A0N2pHMTlRdERVMEo2bmR6RWRROXV6Y3FQdi13alp0a3Qwckg3MzEySkt4RGNRbFBTN2JtQlE?oc=5) <sub>finance.biggo.com</sub>

</details>

<details><summary><b>Momenta</b> (126)</summary>

- 📰 2026-10-10 [2026年MOMENTA：智驾从L2走向L4，R7开启物理AI序章](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1JWGJxSWVhdFlsclVpMHJDWF93VjBCckZKRVp2eXJwYTNwNUVzQmN6NGdabGhrQTdsd2JfalRiQlJMT3ZOU1RzWVplNHpQX29nOXJR?oc=5) <sub>电子工程专辑</sub>
- 📰 2026-10-10 [标配800V/Momenta R7 上汽大众ID.ERA 8X将于10月12日上市_热点推荐](https://news.google.com/rss/articles/CBMiYEFVX3lxTE5ISms4VjNkczZUSkc0QTRzcHZoZnRDM3k0bXhWV1NMeEljX29RRDVtUzhIN3YycndNUHVpb3VfWDdMYy1tMzhfQ05pRE5fRVA2c3ZpSVBKQjQwelpWTmxoUg?oc=5) <sub>证券之星</sub>
- 📰 2026-10-09 [月入5000，拿下带Momenta智驾的艾尼氪 V](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBLbmUwclRXQi1SN2ZTNFdmMDlXcl91SmVsWjFibFJRQ3VUOHlUVUJSZkxYeUJUSVJ4dExzRWlfZ0FrNDNGQ1hOUnVuWkpPVWFIUW9ZeVVaQ0Rzdw?oc=5) <sub>爱咖号</sub>
- 📰 2026-10-09 [【视频】9.99万元起B级纯电！月入5000，拿下带Momenta智驾的艾尼氪V](https://news.google.com/rss/articles/CBMia0FVX3lxTE9qcXN5NWdnY1R2QUdvYjhJUmNVS1BBT2VGaEU0SGcycGVUbklYTDl6LXdYdDZpeFRLWnM3dTJYR0NfaEg0QzRWbXNlSkttZkcwelJVZDdiYVUyVEFfc1JoYXU5MUtJcjAyeU1v?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-09 [【视频】智己LS8 上海实测Momenta智驾能应付多少复杂路况？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1MaXMzSVgyN1lwdmdVZmV3bnNZY25kNk5xR01XOXdZSmExSTg4UVNZU205OVppLW0tNmxCQ2lYSnNBYXdmME5EVWNnWGJ2U05ZQlpZS1RHNGVwenc?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>XPeng</b> (273)</summary>

- 📰 2026-10-10 [XPENG Launches "YOYO" Robotaxi](https://news.google.com/rss/articles/CBMidEFVX3lxTE5MbTd6d2VTRko4czktWXgyTE5LbjRmSUhKNHFteVV2U3lqU1RrSVVFUERKQzRZU29RdS1NTzlyV1pmWi12c1dtMl9XeFZqTHRIZnNtUnAtZEg5cWF2OEcyMkY3UTJiNUtHRE9ZYWFyWkVsV01v?oc=5) <sub>CleanTechnica</sub>
- 📰 2026-10-10 [XPeng Pitches Its Self-Driving Stack to Western Rivals as Robotaxis Eye 2027 Overseas Debut](https://news.google.com/rss/articles/CBMi2wFBVV95cUxNNmRrNS14U1F2SGtSd0h4ZkNfc2o0Zng1Y2dyZURlSEdWQ0VzQVJwUFRWMHFWU1BmWVR0ZHBjYmZTWE5COFJ3U3NWNW5kYmZ1WUltZEFDQTE3U0RITEFXV3BmR1NCN0tLeDlZOUtaYmRUVWVNc1hPUTBkMWk3d2ppVGJycmdGRjVVcHV1dUFZelFCU2FtcU1IX3ZINnJFdnl0ajBKM1RRWlFJT1E4NVZUT0dBamZ2Z3JMM21SZzJzUHlaa1FoWEFWU1RRNlZVLWdaNEhpbVp5ODJTODg?oc=5) <sub>AD HOC NEWS</sub>
- 📰 2026-10-10 [小鹏GX真实测评：26.98万起的“智驾卷王”，这3个维度决定谁该买+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTFBsV2cxZkdxSjI5NWNhOUszTnB2bUtTWFFobVZSNml4NW1DLWotZE9PcHBtX3dxUGR0WXR0LWF5eHlOU2g4Z3Byc3YwTm1LRTF6Q2FZd2J0SjlSd3l5ZTh3VlR5QlhFdzhuam1Mb2xqWlVGQQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-10 [巴黎车展上演小鹏NGP VS 特斯拉FSD 智驾仅两家报名](https://news.google.com/rss/articles/CBMiiAFBVV95cUxOMTlRRnhPMHhGNkN6WlNfNUYxZS1Xd3VHdEN0eUQzT3RBcWlNTGttcFg2YkJhT091TFd5YzRCUEtZNS1BWVJtcXRHT1JSRGFnSjE0YV9qR21WcV9oVG52UmlFMWFDdFpET1RIM0dLODhIT1drbmZCUDRHYzcyRzlscTVvUExpTjVh?oc=5) <sub>搜狐网</sub>
- 📰 2026-10-10 [小鹏GX性能评测：26万级旗舰SUV，续航/底盘/智驾真实表现如何？+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1MVVJrYTdPTjVPcVlFTjRhNE9KM0h6M3lWZGxlUjdVOFZJMktjUXNyQk02Tl9HRzgzekx0OHFoZmdxWGtRdjBXNDV4V1BqRUNfMlRTVElkMTBBbnJxblYw?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>Li Auto</b> (162)</summary>

- 📰 2026-10-10 [长途自驾豪华SUV横评：理想L9、问界M8、腾势N9与神行者8，谁才是真正的“全地形头等舱”？](https://news.google.com/rss/articles/CBMickFVX3lxTFA4MzZiNmV4VlY5Mm9Ub0VrTUZIckNfRmVibm5pZFA1U2dqeE1ubDVjZTExS3pZdHpwZmtFM2xpWS1hS0FYVjVzbnE0dDg3UnB4WGhsN21YdGoxWG1ramNvMlFoWkZ4Rkw5MVR5M1Y1Q3YzQQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-10 [长途自驾横评：神行者8、理想L9与问界M8，谁才是真正的全场景豪华SUV？](https://news.google.com/rss/articles/CBMickFVX3lxTE5CY0dBNXlfdEV2RVo3Mm8wZ2x3RXlla1dESFNNaVc3VHBVN1dZRjkzakViRmpIQVB2X3lSSUZoQVR5M0M0NTl2d0tmRVJ6Mm5uV3ltdWlMVmhkTFlxaTYyYUxpdVNmcTBLMGw1NWF6WXNWUQ?oc=5) <sub>新浪网</sub>
- 📰 2026-10-10 [三款旗舰SUV正面交锋：理想i9、问界M8与神行者8，谁才是全场景最优解？](https://news.google.com/rss/articles/CBMickFVX3lxTE05OFBKc3dmeFc2dmZvcnhCUEszU3l0TjFpM2RacVpqT0Q4VnFUZjI2RUZsWTZRSkx5R2tMcWV3ekVfU2ZsaWdPX1BHSVZyc1p4OVFjMjhqaWwzem1CS2wyZ19YY2tHMlAwYUxRWDNzSzJ0dw?oc=5) <sub>新浪网</sub>
- 📰 2026-10-10 [2026款理想i6将于10月28日上市，迎来六大升级，11月初开启交付](https://news.google.com/rss/articles/CBMia0FVX3lxTE53Q0xNdEdDWUhZaTVWM0U1cTZlenlSNlRSQXBWTDVzbHlaRjd0SlJJcnpQbEtEdjI1a0xFZ3A0QzlIb25pUmoxb2xFbU1QdTlPX1E3Y1l4Sk16RUotS1hNUmZmeUF6bl9HSVhn?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-09 [国投证券国际：理想汽车-W维持“买入”评级 目标价70.20港元](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQeURDcXVrem56dk9VNmVxS0xadWhPbzd6RjdNT21jYjdab3REcnhFZmVPSlVBWEdXVlFuSVJmd2lyV2lNY25mOFlWeXVLX0tta2hDNFBCQWJHNWFBS0lmeFdpdy1RR3JYUUlYTmlXYjVQRUVBdFpPUDJ5dHVoX29rMG95ZEdlNUlHM2dz?oc=5) <sub>新浪财经</sub>

</details>

<details><summary><b>NIO</b> (160)</summary>

- 📰 2026-10-10 [【视频】蔚来EC6 2024款75kWh租电版](https://news.google.com/rss/articles/CBMia0FVX3lxTE9QbUVhVXoya2kzSS1xS2dyZk53YVBOWDAwdFFtOW5XS0ZCNVNhVTdreU9IM1daek9uaFNoUnNxMndtR09vWHVMOTZmTmt2a2t4bnEyZlNCa0JhVnp4OUdkTXBwOWJSSTVLT2lJ?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-09 [蔚来9月智驾报告出炉 总里程超2.5亿公里 达1月4.3倍](https://news.google.com/rss/articles/CBMiW0FVX3lxTE80RjUwdVJyZ2RRSTFxeXBkYUdLTWxDM2Vfb29rMXpOOHJUanZlbTI0QWN4alEtcW4zTHlCOTk0NUxYVXdNaW5uUVhkc1dzd1k4SHBrc0llT3R6R3M?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-09 [Nio Jumps 5% as Chinese EV Names Rally, XPeng Climbs 4%; Rivian Slips](https://news.google.com/rss/articles/CBMirgFBVV95cUxPNENqcXh3Nnk0cFQyWUJBSDFQeFJXeUVKZDE5bi1VVjI5U1hNbFk3Q3FoUEFRbjViVC15TGZVQ1BPOEhPVWREZ0ZSMHoycDhKOUJ3NDloMFZpNDQ5X3lwcFRac01OTTBoTW4xd2hFdWhqOVcwb0RDTThkU2pSWTBpMDJDdU1ya0lKdnlpT2JOSk5QWGdZQVVDSUp6UTh5cWdmQmgxWUZSOHozTjExX3c?oc=5) <sub>24/7 Wall St.</sub>
- 📰 2026-10-09 [AVGO Gains 3% Overnight: Chipmaker Ups Debt Buyback By $500M After Strong Interest](https://news.google.com/rss/articles/CBMi3AFBVV95cUxOQjVFdmwtdnc0bFpOS0V3WVhpZFdmcHY3S2wtSkRZanRXcE50X2VjS0xOaV8wVkhfNXpxUGxhSU9fQ0U0Tmp6bnZqOVFrTWRhZW9UU0s3cndPU1c1YUtFQ1IydVFGdTEtYUxtUWNVSWhrZE80aHl3YmxEWDZZN2lYejJBTk5Xc0xMOTNURXlpWVdUUDVDNmlrYlFZWUo2UHN3cXF6ajVLTWtydE90eTNIOVkyWjJTcHN5VlBaU2V4bHNQNFNwV3NVLVhrelRyNnVQV3d0eFEtWGJGb2F6?oc=5) <sub>Stocktwits</sub>
- 📰 2026-10-09 [蔚来ES8试驾视频：40万级销冠的“大车开小车感”是真的吗？3个维度拆解+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE40SnVMR09OYVdFVHVBNnZGai1aV3lCTUd6M3JWcTRMbUFOZTQxcWsxY050RUpsN2lBZFg0c3EzeHhNcDBRWWpnMUllcV9uTnFmcEJQc19mTUdyYmd1dk1B?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>Huawei</b> (399)</summary>

- 📰 2026-10-10 [VOYAH DREAM 9 Debuts In China With Rotating Seats, Huawei Technology And Electric Power](https://news.google.com/rss/articles/CBMirwFBVV95cUxNdDV6ZzFYcFBfVXVEclpXcmlVTnpPWWRkMXplaC0yN3dtcDFLMWpzOE1FX2s1d0NNOGVVVzFjV0FjUllmMXZEXzJrUk5mNXFLXy1LYnQ5VWEwdlhJb2RUMGdLTTNIeTV4eUNaVzhhYW9XeWNnMFhWQTF0dGFmVW9UOUZ6TlVoMG1rTk1TUFZGUDJfbnk0MjU2OG5aRzFhQkFJR3V5RnhTVkhUZFpFS29V?oc=5) <sub>AutoApp</sub>
- 📰 2026-10-10 [Huawei-JAC Luxury Vehicle Hit by Safety Concerns After Brake Brackets Fail](https://news.google.com/rss/articles/CBMiugFBVV95cUxQM2tnbVBJN0R4V1ZGOFYxUHZQaDNLQ3JRM290ZFdsOXJ5ZW9BTUJ3WEp5blBldHZEWXNRdC1uX3p5YUVYb0pjd0paYTVvckl0cHEyVDNBSHJlYi1maUlSdVcyY0t0U1RYTjRud0gyTkgzU1NBR1BJUVZCYXVSWkk0WkNzV2dYLUZmSVkwUjZNY0daU09rY2UyclE4NFZpVUJCaTNwS1FINk1IXzlnQ0ZucmtpcUdWRHFzT2c?oc=5) <sub>Vision Times</sub>
- 📰 2026-10-10 [Huawei might be ready to give compact phones another chance](https://news.google.com/rss/articles/CBMilAFBVV95cUxOc0hXZGRkNzItQTRldzY1SW9iQ0RyN0FFWE51am5yRWFPY0JHNVdPUVZLaUhndV9vZ1MxUG5NYzdiMjNpSnljVGlYNFlkY2JmR2tzMmJBU19IZVE4dm5WaGZmdGstRU9oZHJIZEoxVEdxR3dkMV9Ld1NpNktDVzhwX0lVOThJOFppNjdaVXVXX3g2QjZx?oc=5) <sub>Gizmochina</sub>
- 📰 2026-10-10 [【视频】10万级华为乾崑智驾6座SUV 到店体验星海V6](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1KME1heUdmSzhMVTY3cW9ZMUEtbDUxQ2xiV3VBT1ZkTjVuYlhZckU4VWFiVVpqNEZodHlHS3RFWjhoOVE3dHYtSzJIdXZLUVFsUGdXQ0dBNF9yZkE?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-10 [华为乾崑智驾国庆出行报告也来了 累计辅助驾驶总里程5.53亿公里，辅助驾驶里程占比60.80% ​](https://news.google.com/rss/articles/CBMiY0FVX3lxTE1NbkJVYVNNNGxzRmhaUDc4SGt4TjdVM0x0dFlEcTNpSzltaTFQZUhtTERGLUxMZmZiNGVnUmdmQjdYNEVlT2RrOXVMcVNfSGl5MU1jOS1xejV5amZLRF9XS1lhRQ?oc=5) <sub>手机新浪网</sub>

</details>

<details><summary><b>Baidu Apollo</b> (54)</summary>

- 📰 2026-10-09 [Xpeng's Yoyo robotaxi service goes live - ArenaEV](https://news.google.com/rss/articles/CBMifkFVX3lxTE05ZmdRVFl0SUJadTdFS2FETjRQS0R6czlWVElYTms3OG56THFhQjluQVoxUUpraEJTX1JkNW9jSERLNS1PNVFDQnVTUGtYSjgwVW54WEJUTW5NZHhYU1EzYXhTd3dnT0xuQVlyRkxtbnhzM1o0cktfZGQzNnFBUdIBfkFVX3lxTE05ZmdRVFl0SUJadTdFS2FETjRQS0R6czlWVElYTms3OG56THFhQjluQVoxUUpraEJTX1JkNW9jSERLNS1PNVFDQnVTUGtYSjgwVW54WEJUTW5NZHhYU1EzYXhTd3dnT0xuQVlyRkxtbnhzM1o0cktfZGQzNnFBUQ?oc=5) <sub>EV Arena</sub>
- 📰 2026-10-09 [从“卖产品”到“深度参与”：中国企业进入中东的方式正在改变- 21世纪经济报道](https://news.google.com/rss/articles/CBMid0FVX3lxTE1uanZ4SGtKLTJjY3I5LWJIdEcwV3htNGRhSTJ6MkJiQi0xNExYTzZTM3h0V01NeU41c2REU28ybF93X0J6Qmp1Ykl4cVY1b0VjMVJfaXRlWktuTlJIckQzTmtqWUJXOUdPOVhvd0Z1NFhYT082YXhN?oc=5) <sub>ZAKER新闻</sub>
- 📰 2026-10-08 [Uber and Pony.ai to test robotaxi service in Lo...](https://news.google.com/rss/articles/CBMikgFBVV95cUxOaDdlY2Q1cHluVUktVTFfa1pyb1ZhXzhDMnFtZkVrLUl1d2dyQXNSQUFlaGlHSjBlWURGelMtSUdnWlVPMkZ1YjVVT0QxQ3U0elFYc1lsTVN5VWZlcVA3VGxkbG9hTVYwbkVGTWQ3OFAtOUpWcktEVlZJLWlEaGpjS0Z5bEJWeWNVR2IySWJZZ29rZw?oc=5) <sub>Pluang</sub>
- 📰 2026-10-08 [Uber and Pony.ai plan robotaxi tests in London within weeks](https://news.google.com/rss/articles/CBMib0FVX3lxTE9rUTJXVUdwckFQSEFnVFZnN0lXOWlFU2JHYnVUUDVUZy1rZkkzcDJVVG9LZU9GZVllZWtLUnNmWEh5Z18tR0hKVnNTYy1DOWN6SDI1NWczd1E2RUlFZy1mN2JUWDRpWGNHZkxVTHJxVQ?oc=5) <sub>Crypto Briefing</sub>
- 📰 2026-10-08 [Waymo locks in $5B loan from Blackstone, PIMCO to fuel robotaxi expansion](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNcjlhRElvb3F6ZXgtX0hiYjNkdC1GdDlRQk52azA3NjZsQjdIV2VnM204cldKV0poVzliNWRhSWV6Ym9OR3JISjd3YXM4ZDlNWVkxUUdYTDZrNVY3S2FoUWF1LWlLZUUtcVY4RUwyR3Z2MXRwRzM3MzBfSno2eGpBZWVNcHpLVFg1bk9aNWlqYkNTYlFqRmFuMUxLcHFRZnlkajRwNlNyX3B1QQ?oc=5) <sub>TechCrunch</sub>

</details>

<details><summary><b>Pony.ai</b> (132)</summary>

- 📰 2026-10-09 [Pony.ai Teams Up with Uber to Launch Robotaxi Testing in London Within Weeks](https://news.google.com/rss/articles/CBMidkFVX3lxTE00UDJpV3h3OTFaNG9tY3RZYlNwdEI0ZFRNUlh6SHVGckpNWWVfVmRnTEdiVzJGU3cweXE4WmV6dEdBSDBDUTNfeWdhU2FHU1ktbXI0aVBzOTFPNktmMnlYcDJkVl84V0tnRW9SWjY2SXozSkVkWHc?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-09 [小马智行Robotaxi将于伦敦启动道路测试，计划在欧洲五城部署超2000辆](https://news.google.com/rss/articles/CBMiiAFBVV95cUxOazlYUUo1b0tYZGpfNTFubUVMOHNxN2tJYjJLUjN0c0kzczJDRFdkYTEwOEVjR1E1Q09qRDZhMXE2S3NES1BlNHFST1Rjb1prMm84THlXMzV1allwUmlIRWd3eEFFeERJZUs4Ukh4R0h5SmFweG80c3g1ZlhvTDNfSGQxTjF1N2Nv?oc=5) <sub>搜狐网</sub>
- 📰 2026-10-09 [Pony.ai's Robotaxi Expansion Reaches Middle East and Europe; Goldman Sachs Maintains Buy Rating, Cuts Target Price to HK$202.4](https://news.google.com/rss/articles/CBMidkFVX3lxTE95VG5sWlNSQzI3MjVFNnBoYXVCTHVjNEpUdERqYWxIRVB1U1lGdFFYZ2FqWWdVT0JBZEtrVGxJODhVQ292U2Y4VlBJN09HUmxpZFlkN3dXUXhreFFWenZfcTljNWxVWXRhbC00VUpXNkctTHBXR2c?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-09 [高盛：小马智行-W持续扩张Robotaxi车队 维持“买入”评级](https://news.google.com/rss/articles/CBMi4gFBVV95cUxQMUc2R1JKLU1meFp5R1A0Y0FKcVA4ZU1SVjkxZi1idWh6SVEwMWlTdy1EVlZPbHRhLVZiNll1bmFibmRlck92alJCQjNETXJlRjZLNFBaNTVqWndBUW90WmNNcXVxWWVTbnUwT3RUOGstVjNTQ2NVZjFTMElkdWEySENaWmNOXzFZaldKWi0xYmtYNVBSSjRqU2tJMmY3aVlBYjVobWttdWNLbG56RV9UdDNBTkZSSVQwRkJTaVZmUUhqUjJmREFtUjN5VThQUXlydkJQYkIxMm9GUkptMlM3em1n?oc=5) <sub>新浪财经</sub>
- 📰 2026-10-09 [小马智行与Uber将第七代Robotaxi引入伦敦 数周内启动测试](https://news.google.com/rss/articles/CBMikgVBVV95cUxOOV9yd1hjWExxMC04bFVVMDVUdXljQjNoNHBnNFRqWldQZUhEMEItSFdhNWF0X3JfS0NOQU5MQmVXejBHb05xMjB0SG9ndnlwS09Gb0paNVBDeks0eGhiMzJ4cnZReWk2Y2EwTDNKal9Hc3B6V21GOVpOQ1M3bEJTejZ0RWk5UUJqWEZXSFYzZmhHdE9TemdZT1QyZVRUcDhSa21lWTBIcDl5Rmx6ZnZTUnRiYTN5SE1CMDBzT0U0MFQ1bUMxNnlJbnFSWjh4aDhHMWFXU0ItOFl6ck1LVkg4WWRCMTZwWmdiV0RaYnBPRlVMbEEzVUV2Q3A5SDlNRU1BRnoteWtUTDRxTmJ3X0s1S1loYzZmei14VmNRamFBVUxMbmQ4T1BpSUtxR2x6TXFVenJZYm9IczJkVkdpUWhVN1h4bW9CUGRtZlRZV0RqbUlvYnJrTWlHSUlpZ19aNmNmZ0xBMXVyZjcyUDlrenc5OHN1ZzYxa0x5STFISHZMSkR1RHJudGVyNWo3NFNBYXpUSTdtdF9qRW5CVDBybnJXYVFQMzI5eGQ3UWhUejRtRDBuejd5Qk1LcktTY01wcU9xVWdTS0Y3WFV6MkJfZFZGdDI0ZUVETWVvMy1MYlBvNnRaY2JnR3pVa1J6bFc2U1RkZTNHUXVBczF5SWRucW1SQ3A1NzNleVdDSWt4RnI0azZma2dHMFpsRWQ4endIZUppQU92Z05sZG02TDVTa1F1ZlJYR3Y4Y2VIeUJEUUl3WEo5UWdqTS1aUU5MOHdHS2YxTmI5OGUySURpd0ZDTXE0N2w4elR2R0hMcDFHY1E5MUJfdGpSZVhwaXo2N1pLYVh1TTNicm5wUElFQjZsRk9uUVl3?oc=5) <sub>finance.sina.com.cn</sub>

</details>

<details><summary><b>WeRide</b> (130)</summary>

- 📰 2026-10-10 [蹊跷的“全国第二”：汽车网站城市NOA装机量排名，元戎启行上半年数据相差近五成 \| 大鱼财经](https://news.google.com/rss/articles/CBMiYEFVX3lxTFB1MGppeVNQb0FOSWFNWm4xWHZaeGlTR2JhWERsZkJNTG0xSzJaYldkb3QtbVNudWRPRmx0RVBoMVNwZzdjZ2FNRmZZQmJkQlBGWmpYdlIxTW9OOVliMWNPMA?oc=5) <sub>新黄河</sub>
- 📰 2026-10-09 [10月9日早餐 \| 台积电业绩超预期；美股科技股走弱](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQZXZERWdxeDlnVXk2YzJFNmpObFJ3VFlCOUFKcVFrUlhkN1dnTjFNaEh6UWhOWTdoV0RpUjgwdzR3NDkwaTRsNWVLcW16d3A3UG82bERnWnZHN0o5dW9DbURfQ25NT1VpdTFFb3Z4WVplUGpMU2xOZVdwMTFhQkdrWmZlcVpWVXlKWThZ?oc=5) <sub>搜狐网</sub>
- 📰 2026-10-09 [美股半导体股全线下跌，英伟达市值一夜蒸发超万亿元，加密货币19万人爆仓](https://news.google.com/rss/articles/CBMiYEFVX3lxTE5NdXRFN3lHV0lROXVQdVZ0cDBQbVVGaC1UT05lNWpicVVQQjdINTZ1N0Uwa1d1bzBiRWFBQTltS3lXUmJDVUlTMHE5QVIyV1ZOTUMzTDV6ak9TUGpyNEpuNA?oc=5) <sub>新黄河</sub>
- 📰 2026-10-09 [专业做10万级续航不缩水智驾纯电SUV推荐](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9fMV96TUZnV2RSODRiVkhrd3llX1lVQXgyV0RubFRFeHdWMWd2RVdNZXIzMWI2U1REZ0ZkWjE1eXZIMFVOZnkzZmF5Y1E0RzVHdFRxSFMtMlp4QWc?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-09 [The Rising Tailwind of the Great AI-Driven Mobility Era: Accelerating the Future of Smart Transportation](https://news.google.com/rss/articles/CBMiU0FVX3lxTE9ZOTFudkl3UGx1ZWYzenR1cDZNXzdOM1dIRFV0RV9GQjNuQ0FwbFlYM3dfV1lUNTdRaXA5bnFKVUJyYzhKMjg1T3lOV3FvY09MS01F?oc=5) <sub>36 Kr</sub>

</details>

<details><summary><b>Horizon Robotics</b> (206)</summary>

- 💻 2026-09-29 [HorizonRobotics/Ego4WAM](https://github.com/HorizonRobotics/Ego4WAM) <sub>GitHub</sub>
- 📰 2026-10-10 [【视频】老车主有话说：iCAR V27新增300km长续航](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBhenZmNkgwQXp3ZE43dEZ0MDBTRDB1NFJNNmE4a1oyVU1lbVdIZ1FSWGtQdW41OUlvM2ljS05WMWJmUlNWSVRVcV9SVUdxa0Y4aDRTSVl5dEwwVWs?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-10 [13万带娃露营，深蓝S05 vs 零跑C10后备厢够用吗？](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1LMzFRNnhSSUJPVjFWTFBIWTB1SzhGMTNicktJdTBqUEdMcmJYd3owN1NHaUdwTkg1U0hWZzBueTZvdVg4dURwWG0wd2tFdHNXdV81THc4dDhlV1k?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-09 [通勤50公里，深蓝S05快充15分钟，零跑C10要多等多久？](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBKcHVqNXUwSlFNVnhGOG9vTUtZNmRVN0JTc3pjS3JJOTlhSzVsMHU4U19CSGJ6X3U4YnB5MHRuMmZMRGluV2tkRkMtTnBlMnNnLVZlNFVIeDRKVlU?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-09 [【视频】什么路都能倒，HSD2.1版本来咯，V27车主节后回来就能拿到推送！](https://news.google.com/rss/articles/CBMiW0FVX3lxTE4wRUV0bGpYcDg0ckl0Uno2WkVCZXJ1MHRxamZnUjNVWXhZNWoydy04cEgwTTMyRDhMa1JyaGN5eVkxc3hGUWVlMmMwYlBCUW80czBlWVNzOEo4bXc?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (29)</summary>

- 📰 2026-10-09 [赛豆AIVA ME7深度解析：20万级原创AI轿跑SUV，真香还是噱头？+FAQ](https://news.google.com/rss/articles/CBMif0FVX3lxTFBzaVFpNWNnbjNlQU1iTU13aTcwc2pBZERxVlV3RkpESjJRN1g4YmotNmNISW11eGtVXy1aSHBmeF9hQWxMeGdNRXBrd1lEMVpkRjJUWUxIbmxnSjgtZHpzT3h2VmxhZlNDd25oTm9sNDVVZm5NaDJyYkQ0RGVxR1U?oc=5) <sub>新浪网</sub>
- 📰 2026-10-08 [城市NOA座次重排：第二换人，头部三强只差1.7%](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNd1ZkX3lwNUE5bUEtTGR4a1JiSHBSbXM1aDJxUmc4TEtlVGRJUFZKempPX1dtYVZoVkVRY1pZNWRlZ09GMzBBODRlQ0FMZjQtR0Z4R2g3NC1pUkhfeG92a3hzaGtuWDFlYk1ZaUJSWjZzVFh4R014cTFTZ1p4bW54WldObE9oTmEy?oc=5) <sub>搜狐网</sub>
- 📰 2026-10-08 [元戎8个月从第八杀到第二，城市NOA打响“华元魔”头部肉搏战](https://news.google.com/rss/articles/CBMibEFVX3lxTFAwbUU2LVd1bkVoVUZVcUdrczBEUmNwQzVnaDFXX0hQU3U4eVpScElhMC1ydHVPRVhuUHI5OVNYZXVjOC0xV3VkQUQ4Q2ZyNURuNUdWaTAwMWV1SkFUUUlxZXR5SjI5cFJSdzJrbA?oc=5) <sub>中华网</sub>
- 📰 2026-10-08 [豆包加持，赛力斯AIVA新车呼之欲出，20万元级市场要变天？](https://news.google.com/rss/articles/CBMiTkFVX3lxTE5IM1pkZ2RWaG1YLWRIMFRIcXY3aHgtUklFbG9NaUJCd1ZkXzNvUjRHel9wOTRJOXBzM09GRGQweFQ1WnBoZXE3ZkJjTmtWQQ?oc=5) <sub>36Kr</sub>
- 📰 2026-10-07 [与问界M7同一工厂制造赛豆科技首车AIVA ME7测试车曝光_热点推荐](https://news.google.com/rss/articles/CBMiYEFVX3lxTE9fYVd2TTUyZWxoZC1ZZGNWczlwNXhUclo0OENVVkhhaFpxRTRFQlhNeFZBZXNRQUQ2MnVEOTB1TVAtMEZRTDVTQk5TcWw1QkZSSlRieUpkaXdpMl9xS0wzaA?oc=5) <sub>证券之星</sub>

</details>

<details><summary><b>Mobileye</b> (19)</summary>

- 📰 2026-10-07 [Uber invests in robotaxi provider Verne](https://news.google.com/rss/articles/CBMigwFBVV95cUxQQkxEa25xSjBNT0ZJMzZINk54a2txS3k0S0pvTU4wZEJ5eVhHY0FNRWlyaVdIcVhYdmlPQl9HVUsyUnlkcW1UVzRVc180dHNCT1hXV3ZUcms3Mzg5aUoyZENTUWU3VHJtRlFuQmp0dWpQRDlmU2xlSDQ1MnlEZW11YmFGWQ?oc=5) <sub>electrive.com</sub>
- 📰 2026-10-07 [MOIA America Launches First Autonomous ID. Buzz Rides](https://news.google.com/rss/articles/CBMixAFBVV95cUxQY2FmM1hNRDEzV0c3c2NSVklIUDBPU1VrbmRmNnRLV3lNRzRITUVHUldKcVNYajNSYXJkdTJmbzRGeWt3V3ZrcXlmanBfR2t5cjRKZlU3b2JHbUg3VUx0ejdIS2ZUT25DRm5KTGtzSm1OaEhhQ2Zsb2Zhb0tHMDlnaWhnOGJHLXBvYk1GYkNYVFJRb2M2R3BmamRnN3RMZlJ2a3JlSGc3VnNmcXBtVDdub0s2VjhXSDhKVjFDR1pIQjYwLUpI?oc=5) <sub>Fuel Cells Works</sub>
- 📰 2026-10-07 [Uber takes a stake in Croatian robotaxi startup Verne](https://news.google.com/rss/articles/CBMikAFBVV95cUxOMkFfTDhoaldrejJpdUNUd1JvRXN1MlZwYVZQRjdPQ19FM2oyWjgxTndscUdGWFVZaG5nSWVKNWQ1dVYtNzFNZ2t0VnFwaS1mOFpneG41RW51M19leE9XSUN5WjhGbjF0ZkUtRVI4RDBiSUxtX2ZCTDBUekNRN3p1ZXZzUFU5aXJ0cjk5bHA3aUU?oc=5) <sub>Dealroom</sub>
- 📰 2026-10-05 [Moia’s autonomous shuttles start first passenger tests](https://news.google.com/rss/articles/CBMilgFBVV95cUxPaXBLWlk2ckZabm9UeXdOV1lCZTRjaDBkVmk4bDNVRWVMZkxKUEVTOVBqZERzWGlySkROdEs0bkE3SURjaG44c1Y4M3lsM0NmSG95X0diNlY4cGJoMUp1UUMxVnFkQ2Y0UTR2UDdtdTFzczBDSHpId3ZmWDltWlY3Ulg1bHBYMzJweHhDOWkzd3lyVWwxSGc?oc=5) <sub>electrive.com</sub>
- 📰 2026-10-03 [We Found Atoms, Rode Wayve and Watched Uber’s Autonomy Clock Speed Up｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1QZjNLZlpHR2ZtcHFaUDF5bEE3ZktHQlNoN0E1amxaVEg0eUdQbElIVlVVZk1JdTlqZG1kbGZYVTBvZDdKRDRKVWlqa2dRNDF3aTN4dEpmdTdxX0dTVnlj?oc=5) <sub>finance.biggo.com</sub>

</details>

<details><summary><b>Aurora</b> (56)</summary>

- 📰 2026-10-10 [Autonomous Trucking Hits Regulatory Green Lights but Economic and Safety Questions Linger](https://news.google.com/rss/articles/CBMiugFBVV95cUxOTWpyRnRTWmc4N3ZLMnNCM3lrVXhTQS0yOU1ZZm1na19UR1dpTFZvVXV0YmVhUFFyOHFMZW5sRWFPclppVHM2ZVB0ZWgzdXNDTDUxRF8tOUFpX2xfelRBM1RtUkVnWUZJUjhKVjJCMEdScE9xejVOX3B2Wk9pZENZY2VNTHVPQnpMYXZiM2hETC1hTlF6VlJ0YVFYSzlWSGZFSGdtakNQLWpEMi0wbW1oa0o5U3VvNDctekE?oc=5) <sub>news.lavx.hu</sub>
- 📰 2026-10-09 [FMCSA exemption gives driverless trucks a green light](https://news.google.com/rss/articles/CBMigwFBVV95cUxQVGJYNjYtb3c3V1dKcVdDWmlmdUwzQXRiYkJ6ckk3VjVjUlUzdkFWQXE1bWw1dHotLWNQUlFLYU16VmNPRGFZTUc3SF93eWZ5bjdlaHhYU19TbHQ1YVZMWWI5eTBfT1ItdVVHelJwVW9BLVExVDVENU9ORjl1R1d3Vk8tVQ?oc=5) <sub>Land Line Media</sub>
- 📰 2026-10-08 [Bollywood actor Nana Patekar dies at 75](https://news.google.com/rss/articles/CBMimwFBVV95cUxPVzhsbTRiV1k4RzB1X01kY0IzUFZPS3ZySVFLeGVTZ1pOOXB5VzlpUjZ4a1hMUmtHckJtMGN4THpXUWUtVzVKLUl4eDBtUVlvR1M1WHdJOG1TQkpjTzFXdFQwTV9yUEpOSlFrTnRJclJVVXg2bkpKMEZVV3YxLS0xOVBncEN2LVFpR2w2MGFJSEtqb3Y2R2lwTlNRZw?oc=5) <sub>Reuters</sub>
- 📰 2026-10-08 [FMCSA to allow self-driving trucks to use cab-mounted warning beacons in place of triangles](https://news.google.com/rss/articles/CBMiuAFBVV95cUxQMDdzVXVpMXFZNHJKTE5ReWZRN3UwZWNYb3RYRmlYTHNLWFJwaW9GTnhvOVRSV0ZTRDJyRnZwdHdPOEF6dUxCbi1VbW5yMnJPR3pvXzRkemtpZU9Nd0RZN3o0TzY1Yi01dzJKcERzdkNnNTZ0ZzdpWkNXbVhWaG1EdUtJeWxSREtCTWdDb1c1Q0U3OEJhNXVsYjlkU3VjYVRnQXBsc3Nub0Jya2wwc0ZJdEFXQkVhWDVW?oc=5) <sub>CDLLife</sub>
- 📰 2026-10-08 [Trump awarding former baseball star Clemens the Presidential Medal of Freedom](https://news.google.com/rss/articles/CBMinwFBVV95cUxNdURUbzFPeVNUc2poVm0taDh3eE5sRlRyS0x0eVB5V0lDdE05d1RnS2s0dDhjTW0zUkRqd2toZ1lqMlVLV2VhbUZvSDRsbWt2RlZ6cGdVY2tmQnQwcVdyNGJnZGVZcXV3TFJfZ2hBNnNCWnkyajhtWGlSOWxZRzNFLTJPUWl5VU16Ym01RHM1emprMFhLWW5DcFUzV09YNjA?oc=5) <sub>SRN News</sub>

</details>

<details><summary><b>Zoox</b> (89)</summary>

- 📰 2026-10-09 [Zoox Investors, Directors Clash Over Amazon Deal Class](https://news.google.com/rss/articles/CBMiVkFVX3lxTE80b1JUV1VZVHdxOC1wN184c1VlNXFvMXRXM2FKb1JucVNUZ1dldnR6UVRvVU04bVhlTzN1NGxSazRXQ3BQZnFuQ25icTdTMHpyOUJyS1NR0gFWQVVfeXFMTzRvUlRXVVlUd3E4LXA3XzhzVWU1cW8xdFczYUpvUm5xU1RnV2V2dHpRVG9VTThtWGVPM3U0bFJrNFdDcFBmcW5DbmJxN1MwenI5QnJLU1E?oc=5) <sub>Law360</sub>
- 📰 2026-10-09 [The autonomous vehicle industry says it will create jobs. Here's how.](https://news.google.com/rss/articles/CBMimgFBVV95cUxNMnJkLVVUdVFkb3VyUHhFRzBsaE1RNUdaMkNUVzV1QmpBamFzZ3RsVk1mNlJ2SkVMVlJINUVuSW43VVljVmpwVWRZR0FrdjU1SVdXR2lFMmw1Wm9PYkd5dG9PQXlNZWVXUmpXM3VQWXdhXy1qVDMySVJYSlFsOERHUWpjM1AxYjBfenl6aVR6V0g0QXdIN05xSFlB?oc=5) <sub>Austin American-Statesman</sub>
- 📰 2026-10-09 [Zoox Grounds Atlanta Test Fleet After Toxic Gas Exposures Make Workers Ill](https://news.google.com/rss/articles/CBMingFBVV95cUxORGlqTUp2RzZERlpBZTVSYVlRNjRPTTVrNmhBV25SN1FIekJROUFhV0V6WFJneHlDZ24zSnNYTXRjdWdGaWhPcEZqd0pRazc3WEtXV1RGVlFucWxhalpENTFrTEdCbDI4UDlPWE8xWUpkVmJyVnk3d0F1ZEpaNHdtOHJITEtEeFY1RVFodDYxcWE5SVZVQzAxVG1PSUlXUQ?oc=5) <sub>Vocal</sub>
- 📰 2026-10-08 [Tesla Gets Extension to Respond to NHTSA's Cybercab Probe](https://news.google.com/rss/articles/CBMimwFBVV95cUxQUzBGZm04V3RJSU9vU290Yi05U0l6djlYaFg4Q1VwbFRpcmZrMFhxOWd6TTVsazdZRHlXRnM5MTJIYmtfcURyNVQ2Q2kwLUg4SUtBSnVreFUzeld0SlNBamJNM3JxTGNQbXpZcWpVR0M1NXFMeUI4WWI2YmJvLTZfYmRTSm1POWY0cUtUbC1YdlVNWVdmY3BqX3V3MA?oc=5) <sub>Not a Tesla App</sub>
- 📰 2026-10-08 [What state is setting tough penalties for robotaxis that block first responders?](https://news.google.com/rss/articles/CBMiwAFBVV95cUxObmtEZ21hRXhoV3lDNzEyTzh5S29ySDRUUGdMbFJjblhIM2l1OGRkVnVjU2RaNWNTaEV6Qlg1a3RwWDdNTDZqZzVScXBGTy1LdHBuZkFrc2oyRHZ4WkU4SGJ5WGRUZTAzTnMtdlZtR0ZPM251Smd6LVozcmNGZlFKdnc2LU9URGVVUXNTTzZzMVdVQ09jNmVKd1ZNQnpHbjVaczhaNVdrQTFpdDkyVkZxRDBKZEZYVjBMM0ozVmpoZVc?oc=5) <sub>GovTech</sub>

</details>

<details><summary><b>Motional</b> (52)</summary>

- 📰 2026-10-09 [Pony.ai's Robotaxi Expansion Reaches Middle East and Europe; Goldman Sachs Maintains Buy Rating, Cuts Target Price to HK$202.4](https://news.google.com/rss/articles/CBMidkFVX3lxTE95VG5sWlNSQzI3MjVFNnBoYXVCTHVjNEpUdERqYWxIRVB1U1lGdFFYZ2FqWWdVT0JBZEtrVGxJODhVQ292U2Y4VlBJN09HUmxpZFlkN3dXUXhreFFWenZfcTljNWxVWXRhbC00VUpXNkctTHBXR2c?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-09 [Hyundai delays its in-house autonomous driving solution to 2029](https://news.google.com/rss/articles/CBMilAFBVV95cUxOM1BRRVUzZ21fMHFubEhHNHRGcFVDQTFwdkRMWnljalNhS193bHpKY0dLSUZjN2tXamRlZUZIZ24wdmh5cWE5bnI2MzF4Qm5lVXJlWFZqTXE2TkpFLUZJWExJQWY4RDFuemJJbmZWZ01DMmRoUG9yLUlIZHNnT3RVeHdYR3hMSkk4RlBfcjlHU0R6Mzhn0gGUAUFVX3lxTE4zUFFFVTNnbV8wcW5sSEc0dEZwVUNBMXB2RExaeWNqU2FLX3dsekpjR0tJRmM3a1dqZGVlRkhnbjB2aHlxYTlucjYzMXhCbmVVcmVYVmpNcTZOSkUtRklYTElBZjhEMW56YkluZlZnTUMyZGhQb3ItSUhkc2dPdFV4d1hHeExKSThGUF9yOUdTRHozOGc?oc=5) <sub>Motor Illustrated</sub>
- 📰 2026-10-08 [Zoox Charged $42 and Took a 28-Minute Detour: David Moss on Las Vegas' Most Expensive Robotaxi](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1sc2dnNjNzbnNqTVdic3NBT2N4bHBBcTczUEFhZ05qek1iZFozUXoyN0pzdWVHdEw0UDZRTVlQQlNWN0Q5RHNZbk16MjVfUXZCR2FlR2dpS2V6Ykk?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-08 [[Shockwave] Singapore, Global Autonomous Driving Gateway and "Technology Test Bed"](https://news.google.com/rss/articles/CBMiZEFVX3lxTE5wTnQzckEweFYwbDQ1aXRpOU8wOTFpYmxCTmZNLTJRWEhWTWlvQjZMVGZHUWxjWlRHdzhQWkdaeUN0a3VHcTVNNVdUVUFMWjN0Q0VUVWNYMGlqQkhQcWczdUx2bFg?oc=5) <sub>아시아경제</sub>
- 📰 2026-10-08 [Six Years Under Euisun Chung: Hyundai Motor Group Solidifies Top 3 Position, Surpasses Volkswagen in Operating Profit](https://news.google.com/rss/articles/CBMidkFVX3lxTE05el8wNkdNWlo4WUJxcFE4ejhyYkhPeDVxdVNHVkEzdVR2TVNtMGF6dzVQZ2NXVzBZYmlQaXU1NEpmQzRYdVgyemZsQmNoZUpCcVdMQ1o3TUh2RTRpUHlwZzFWTGIyUkUtejFaQnoySGs1ci1wYWc?oc=5) <sub>BigGo Finance</sub>

</details>

<details><summary><b>comma.ai</b> (15)</summary>

- 📰 2026-10-07 [Researchers Find that AI Models Struggle With Even The Most Basic Driving Skills](https://news.google.com/rss/articles/CBMiuwFBVV95cUxNb2ZGRGxGZDNjLWU1OVBPNjUtUlJXR0hiVGV3WEJ1eUVnSWExMWVvRmJjX2NtQm9sX0plMTU3YzZwUm5ZTzVoSGttcXZmQ3BqbW40X2doNFMycUk4UWE3anlidy1vWHNYZndVZjZWLUYtbnlHeVBFRjJOaTF4SWxzbmotR0xsNkVIcEhfZ0M3LUs5R2FyV1lVdlRRU3JwakpQcXpBUzlEOEhsWlB3Q19EdXFhQjRvZDU5MHln?oc=5) <sub>Auto Spies</sub>
- 📰 2026-10-07 [OpenAI's GPT-6 Astra is the only AI model to finish a real-world driving test in a Toyota Corolla](https://news.google.com/rss/articles/CBMifEFVX3lxTE9iZmN2ZFp6blVBRnZUTkYtYTJ3b0hSb0xhQjZyQXh5MUN2T3ladUlEb1F1SWJzc3FtamZtazk4LTVUWVpNX0ZjbGZwMnpERk45TVVQWVA1RjBZVUxxTTAzTWpaV1JqUzIwM1I2Wk1tTzc3bDJpaWluc2JVam4?oc=5) <sub>Crypto Briefing</sub>
- 📰 2026-10-06 [AI Agents Tried to Drive a Corolla, Crashing on 8 of 11 Runs](https://news.google.com/rss/articles/CBMiuAFBVV95cUxONWxQTEZham1kc1J4S2lMNUh6OTN1QWhXbl92U21NUWZTZWhNUUdwcFVvUHYtVWJzSjl4TjlCeFhUY2ppMXd3WkkxaHJFRmFlNUN2NGFSSENnV2ZZYWRNZ3JIUjd0dzFlTS0wR3gtbmxXN3VHOUkxWWg2VVFpTVgzWGN2T3RPdEFJV0cyWjRPSVFyNWZTYjFyX0pzYjFEUWQwLUlfbGo1bm8xVUZXQmpyQ3pCNXV5ZE9x?oc=5) <sub>thetruthaboutcars.com</sub>
- 📰 2026-10-05 [Researchers Discover ChatGPT Can Drive a Car. Grok, on the Other Hand…](https://news.google.com/rss/articles/CBMikgFBVV95cUxNNnNwX0g5bHV4STJlMXNOcXRnYnBHWHNoelViM2pJSzFob3dvUVJIdFlDRDV4X09DSVloZmxCTk5NODd3b3RBR2JmWEJQRktXUTYyWDNveS15UEw0NnVfSFluMlJxZHlBb3NhYnRNdDJsZ01MbVNpOXY4OW9nQnBSYnFRQ1U2YVd3a3R2ZTY4VlJNdw?oc=5) <sub>The Drive</sub>
- 📰 2026-09-30 [A $999 Box Promises Hands-Free Driving. Its Own Code Says ‘THIS IS NOT A PRODUCT.’ Now NHTSA Is Investigating Crashes That Killed Three.](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPNFIyamduTmQxb1dKNlh5Z1hCYUhyemoyU2I2bjFUWjZQSDVFSDFWOGxlM1hnQms4Q1lpalg0bXlCTEZTdVJ3eGtNTjlLamY2eW9LX09IejF6SkJxSmZ2QjRkU1pUczlRY2g3cUZIN3hvSUc3a3pUWHVKVk40MlY3Wk5SX3dnOHBl?oc=5) <sub>Yahoo</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
