# 🚗 Awesome Autonomous Driving Radar

> A **curated, auto-maintained** list of ~100 high-quality, open-source autonomous-driving
> papers from the last 6 months, plus a daily industry tracker.
> Updated 2026-10-30 · 1,309 papers tracked · 44 curated.

**Selection rule.** A paper is listed only if it (1) is primarily about autonomous driving,
(2) has public code, and (3) shows at least one strong signal: accepted at a top venue
(CVPR / ICCV / ECCV / NeurIPS / ICLR / ICML / CoRL / RSS / TPAMI, or ICRA / IROS / AAAI / RA-L),
≥200 GitHub stars, ≥3 citations / month, or a well-known lab with traction. Papers are then ranked by a
composite score (venue, stars, citation velocity, LLM rubric for novelty / rigor / impact, SOTA claims)
with a per-topic cap. See [`scripts/rank.py`](scripts/rank.py).

📅 [Daily digests](daily/) · 🗓️ [Weekly digests](weekly/) · 📦 [Raw data](data/)

## Contents

- [VLA / VLM for Driving](#vla--vlm-for-driving) (11)
- [World Models & Generative Simulation](#world-models--generative-simulation) (5)
- [End-to-End Driving & Planning](#end-to-end-driving--planning) (10)
- [3DGS / NeRF Reconstruction & Sensor Sim](#3dgs--nerf-reconstruction--sensor-sim) (5)
- [Perception: BEV, Occupancy, 3D Detection, Mapping](#perception-bev-occupancy-3d-detection-mapping) (8)
- [Motion Prediction & Behavior Modeling](#motion-prediction--behavior-modeling) (1)
- [Datasets & Benchmarks](#datasets--benchmarks) (1)
- [Safety, Robustness & Evaluation](#safety-robustness--evaluation) (3)
- [Industry Tracker](#-industry-tracker)

## VLA / VLM for Driving

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Teaching Vision-Language-Action Models What to See and Where to Look](https://arxiv.org/abs/2607.01658)<br><sub>Yuguang Yang, Canyu Chen, Zhewen Tan et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 35](https://github.com/ShivaTeam/DriveTeach-VLA) | Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving |
| [DeepSight: Long-Horizon World Modeling via Latent States Prediction for End-to-End Autonomous Driving](https://arxiv.org/abs/2605.10564)<br><sub>Lingjun Zhang, Changjie Wu, Linzhe Shi et al.</sub> | ICML 2026<br>2026-05<br>📑 2 | [⭐ 31](https://github.com/hotdogcheesewhite/DeepSight) | End-to-end autonomous driving systems are increasingly integrating Vision-Language Model (VLM) architectures, incorporating text reasoning or visual reasoning to enhance the robustness and accuracy of driving decisions |
| [SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving](https://arxiv.org/abs/2610.20609)<br><sub>Shaoyuan Xie, Zihan Zhang, Jingxuan Wang et al.</sub> | CoRL 2026<br>2026-10 | [⭐ 30](https://github.com/ASGuard-UCI/safedrive-vla) | Vision-Language-Action (VLA) models are gaining attention in autonomous driving, inheriting commonsense priors from large language models (LLMs) and widening the navigation interface from a fixed command set to free-form… |
| [Scene-Adaptive VLA: Efficient Autonomous Driving via Dynamic Layer Routing](https://arxiv.org/abs/2610.24590)<br><sub>Yujia Yang, Quan Yuan, Jiawei Fan et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 2](https://github.com/yang-luvu/Scene-Adaptive-VLA) | Vision-Language-Action (VLA) models offer a promising paradigm for autonomous driving |
| [CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving](https://arxiv.org/abs/2607.04179)<br><sub>Zhaohong Liu, Hao Ye, Xianlin Zhang et al.</sub> | ECCV 2026<br>2026-07<br>📑 2 | [⭐ 1](https://github.com/MICLAB-BUPT/CritiqueDriveVLM) | End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving |
| [MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving](https://arxiv.org/abs/2606.27660)<br><sub>Nan Yang, Zhanwen Liu, Linfeng Zhang et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 11](https://github.com/Zizzzzzzz/MVPruner) | Vision-Language Models (VLMs) improve generalization and interpretability in autonomous driving but suffer from efficiency issues due to long visual token sequences, particularly in standard multi-view settings |
| [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)<br><sub>Yuan Gao, Wenting Miao, Mattia Piccinini et al.</sub> | IROS<br>2026-07<br>📑 1 | [⭐ 29](https://github.com/TUM-AVS/Chat2scenic) | Validating autonomous driving systems requires diverse, regulation-compliant test scenarios |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111)<br><sub>Xin Zhou, Zongchuang Zhao, Zhibo Yang et al.</sub> | arXiv<br>2026-09<br>📑 12 | [⭐ 536](https://github.com/QwenLM/Qwen-Drive-1.0) | We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving |
| [GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives](https://arxiv.org/abs/2609.39601)<br><sub>Qize Yu, Lianrui Fan, Boyu Chen et al.</sub> | arXiv<br>2026-09<br>📑 2 | [⭐ 232](https://github.com/groundingpi/GroundingPI) | Precise grounding matters |
| [GRAVA: Grounded Reasoning-to-Action Representation and Learning for Autonomous Driving](https://arxiv.org/abs/2609.15169)<br><sub>Xiao Liu, Haoyu Li, Jianghao Leng et al.</sub> | arXiv<br>2026-09 | [⭐ 414](https://github.com/AhernResearch/grava) | Driving vision-language-action (VLA) models increasingly reason before acting, but their intermediate reasoning is often weakly grounded in physical scene evidence and loosely connected to executable behavior |
| [Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air](https://arxiv.org/abs/2605.31066)<br><sub>Tianle Zeng, Yanci Wen, Xueang Yu et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 1,123](https://github.com/louiszengCN/CarlaAir) | Recent aerial vision-language-action (VLA) models show promising single-UAV capabilities, such as tracking moving objects and navigating to language-specified landmarks |

## World Models & Generative Simulation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [FrozenDrive: Zero-Shot Text-Guided Driving Scene Generation and Data Augmentation with Parameter-Free Frozen Diffusion Model](https://arxiv.org/abs/2606.20110)<br><sub>Yuhwan Jeong, Hyeonseong Kim, Daehyun We et al.</sub> | ECCV 2026<br>2026-06<br>📑 1 | [⭐ 10](https://github.com/daehyunwe/FrozenDrive) | Synthetic data for autonomous driving is surging, powered by diffusion models that promise scalable scene generation |
| [MESSENGER: Memory-Enhanced Sequential Scene Flow Estimation via Autoregressive Next-Frame Forecasting](https://arxiv.org/abs/2610.10759)<br><sub>Jiuming Liu, Jianing Li, Mengmeng Liu et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 0](https://github.com/liujiuming123/Messenger) | Scene flow can capture low-level 3D motion displacements in dynamic scenarios |
| [ASTAD: Asymmetric Style Transfer for Synthetic-to-Real Adaptation in Autonomous Driving](https://arxiv.org/abs/2606.29286)<br><sub>Dingyi Yao, Xinqi Zhang, Lihui Peng et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 2](https://github.com/Dingyi-Yao/ASTAD) | Synthetic data mitigates the data scarcity problem in autonomous driving perception |
| [Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends](https://arxiv.org/abs/2606.01164)<br><sub>Jiuming Liu, Chaojun Ni, Mengmeng Liu et al.</sub> | arXiv<br>2026-06<br>📑 9 | [⭐ 247](https://github.com/liujiuming123/Awesome-Interactive-World-Model) | With rapid development of large language models and diffusion-based content generation, world modeling has attracted increasing research attention, benefiting various downstream domains such as game engines, embodied AI,… |
| [Is Your Driving World Model an All-Around Player?](https://arxiv.org/abs/2605.10858)<br><sub>Lingdong Kong, Ao Liang, Tianyi Yan et al.</sub> | arXiv<br>2026-05<br>📑 6 | [⭐ 257](https://github.com/worldbench/WorldLens) | Today's driving world models can generate remarkably realistic dash-cam videos, yet no single model excels universally |

## End-to-End Driving & Planning

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](https://arxiv.org/abs/2609.26792)<br><sub>Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.</sub> | CoRL 2026<br>2026-09<br>📑 1 | [⭐ 14](https://github.com/VAIL-UCLA/DreamStream) | Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions |
| [DriveMLP: When Training Strategy Outperforms Model Complexity in Autonomous Driving](https://arxiv.org/abs/2610.29676)<br><sub>Alessandro Canevaro, Julian Schmidt, Hang Yu et al.</sub> | CoRL<br>2026-10 | [⭐ 5](https://github.com/alessandro-canevaro/DriveMLP) | Learning motion planning policies that remain reliable under closed-loop execution is a central challenge in Autonomous Driving (AD) |
| [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)<br><sub>Shen Zheng, Anurag Ghosh, Gaurav Parmar et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 32](https://github.com/ShenZheng2000/WarpI2I) | Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs) |
| [G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance](https://arxiv.org/abs/2606.26017)<br><sub>Hang Yu, Ye Jin, Alessandro Canevaro et al.</sub> | IROS 2026<br>2026-06<br>📑 6 | [⭐ 7](https://github.com/HangYuu/G2DP) | In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors |
| [SimWAM: A Simple World Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.07468)<br><sub>Zongchuang Zhao, Xin Zhou, Tianyang Xu et al.</sub> | arXiv<br>2026-08<br>📑 10 | [⭐ 202](https://github.com/H-EmbodVis/SimWAM) | In autonomous driving, World-Action Models (WAMs) have improved end-to-end planning by transferring video dynamics priors to action prediction, but many still couple planning with future-video generation at inference, in… |
| [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)<br><sub>Aarti Basant, Amlan Kar, Despoina Paschalidou et al.</sub> | arXiv<br>2026-06<br>📑 17 | [⭐ 354](https://github.com/nv-tlabs/omni-dreams) | As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck |
| [Latent-Centroid Steering: Single-Pass Classifier-Free Guidance for Command-Aligned Autonomous Driving](https://arxiv.org/abs/2608.00237)<br><sub>Meibo Hu, Jiamian Wang, Pichao Wang et al.</sub> | IROS 2026<br>2026-08 | [⭐ 2](https://github.com/codingmlinprocess/LCS) | Vision-language models (VLMs) have recently emerged as a promising paradigm for end-to-end autonomous driving, enabling agents to map multimodal inputs and high-level navigation instructions directly to executable trajec… |
| [HEAT: Heterogeneous End-to-End Autonomous Driving via Trajectory-Guided World Models](https://arxiv.org/abs/2605.19631)<br><sub>Hoonhee Cho, Giwon Lee, Jae-Young Kang et al.</sub> | RA-L 2026<br>2026-05<br>📑 2 | [⭐ 0](https://github.com/heat2026/heat2026.github.io) | End-to-end autonomous driving has emerged as a compelling alternative to traditional modular pipelines by directly mapping raw sensor data to driving actions |
| [STAGE: STyle-controllable Action GEneration for personalized autonomous driving](https://arxiv.org/abs/2607.29517)<br><sub>Zihao Liu, Xing Liu, Yizhai Zhang et al.</sub> | RA-L<br>2026-07<br>📑 1 | [⭐ 6](https://github.com/CarlDegio/STAGE) | Driving style refers to the behavioral preferences that drivers maintain during driving, shaped by their diverse experiences, habits, and needs, and is typically reflected in varying levels of aggressiveness |
| [A Survey on End-to-End Autonomous Driving Training from the Perspectives of Data, Strategy, and Platform](https://arxiv.org/abs/2610.00926)<br><sub>Chengkai Xu, Yiming Cui, Jiaqi Liu et al.</sub> | arXiv<br>2026-10<br>📑 5 | [⭐ 109](https://github.com/Jiaaqiliu/Awesome-Training-Ecosystem-for-E2E-AD) | Autonomous driving is a cornerstone technology for the future of intelligent transportation, where end-to-end learning has emerged as a transformative paradigm that directly maps multimodal sensory inputs to driving acti… |

## 3DGS / NeRF Reconstruction & Sensor Sim

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [DriveWeaver: Point-Conditioned Video Inpainting for Controllable Vehicle Insertion in Autonomous Driving Simulation](https://arxiv.org/abs/2606.31918)<br><sub>Junzhe Jiang, Zipei Ma, Zijie Pan et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 17](https://github.com/LogosIntelligenceLab/DriveWeaver) | A pivotal step in autonomous driving simulation involves inserting foreground vehicles with predefined trajectories into simulated scenes |
| [MCSplat: Multi-View Photometric and Geometric Consistent Feed-Forward Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2610.25345)<br><sub>Yifei Wang, Wei Tian, Wenhua Bao et al.</sub> | NeurIPS 2026<br>2026-10 | [⭐ 11](https://github.com/yfwang0824/MCSplat) | Driving-scene reconstruction via feed-forward Gaussian splatting from sparse multi-view images remains challenging due to two factors |
| [Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796)<br><sub>Leshu Li, Jie Peng, Yang Zhao</sub> | ICRA<br>2026-06 | [⭐ 15](https://github.com/UMN-ZhaoLab/Pocket-SLAM) | 3D Gaussian Splatting (3DGS) has garnered significant attention in Simultaneous Localization and Mapping (SLAM) due to its advances in capturing fine-grained geometry features and synthesizing novel views |
| [NIDAR: NIR-Guided Intrinsic Decomposition for Scalable Scene-Agnostic LiDAR Intensity Reconstruction](https://arxiv.org/abs/2609.36878)<br><sub>Junjie Zhang, Jie Yin, Kefei Qian et al.</sub> | IROS 2026<br>2026-09 | [⭐ 24](https://github.com/Zjj587/NIDAR) | LiDAR return intensity provides complementary surface-response cues for robotic perception and state estimation, yet many simulation pipelines omit it or reproduce it using reconstruction methods that require real intens… |
| [MM-TRELLIS: Point-Cloud Guided Multi-Modal 3D Vehicle Generation in Autonomous Driving](https://arxiv.org/abs/2606.24301)<br><sub>Hongli Xiao, Youjian Zhang, Yucai Bai et al.</sub> | ICRA 2026<br>2026-06 | [⭐ 10](https://github.com/HongliXiao/MM-TRELLIS) | Recovering realistic 3D vehicle models from autonomous driving scenes is crucial for synthesizing training data and building simulation environment |

## Perception: BEV, Occupancy, 3D Detection, Mapping

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Deformable Gaussian Occupancy: Decoupling Rigid and Nonrigid Motion with Factorized Distillation](https://arxiv.org/abs/2605.28587)<br><sub>Yang Gao, Wuyang Li, Po-Chien Luan et al.</sub> | CVPR 2026<br>2026-05<br>📑 2 | [⭐ 22](https://github.com/vita-epfl/DeGO) | Understanding dynamic 3D environments is essential for safe autonomous driving, particularly when reasoning about human-centric, nonrigid agents |
| [Horizon3D: Sparse Radar-Camera Fusion for Long-Range 3D Perception in Autonomous Driving](https://arxiv.org/abs/2606.31096)<br><sub>Geonho Bang, Geunju Baek, Dongyoung Lee et al.</sub> | ECCV 2026<br>2026-06 | [⭐ 25](https://github.com/geonhobang/Horizon3D) | Long-range 3D object detection is critical for safe autonomous driving at highway speeds, yet existing radar-camera fusion methods remain limited at extended ranges |
| [Explainability-Aware Frustum Attack: Exposing Structural Vulnerabilities in LiDAR-Based 3D Object Detectors](https://arxiv.org/abs/2606.29963)<br><sub>Chengzeng You, Binbin Xu, Soteris Demetriou</sub> | ECCV<br>2026-06 | [⭐ 2](https://github.com/SecMindLab/Saliency_LiDAR) | The structural vulnerabilities of point cloud-based 3D object detectors remain poorly understood |
| [PointLAM: Local Attentive Mamba for Efficient Point-based 3D Object Detection](https://arxiv.org/abs/2609.21780)<br><sub>Xuanming Shang, Weijia Zhang, Chao Ma</sub> | ECCV 2026<br>2026-09 | [⭐ 5](https://github.com/PointLAM/PointLAM) | 3D object detection from LiDAR point clouds faces a fundamental dilemma: voxel-based methods achieve efficiency at the cost of geometric quantization, while point-based methods preserve fidelity but suffer from prohibiti… |
| [UniD-Shift: Towards Unified Semantic Segmentation via Interpretable Share-Private Multimodal Decomposition](https://arxiv.org/abs/2605.07356)<br><sub>Shuai Zhang, Zhecheng Shi, Zhuxiao Li et al.</sub> | CVPR 2026<br>2026-05 | [⭐ 5](https://github.com/shuaizhang69/UniD-Shift) | Semantic segmentation of large-scale 3D point clouds is crucial for applications such as autonomous driving and urban digital twins |
| [PriorMaskMap: Robust Online Vectorized Map Construction with Biased Priors](https://arxiv.org/abs/2610.39283)<br><sub>Haoming Xu, Wei Li, Yu Hu</sub> | ECCV 2026<br>2026-10 | [⭐ 0](https://github.com/healenrens/PriorMaskMap) | Online vectorized map construction provides autonomous vehicles with essential, real-time semantic and geometric scene understanding |
| [Vernata: Self-Supervised Learning of LiDAR Point Representations](https://arxiv.org/abs/2608.06919)<br><sub>Oliver Lemke, Alexander Liniger, Abel Gawel et al.</sub> | IROS 2026<br>2026-08 | [⭐ 22](https://github.com/rai-opensource/vernata) | LiDAR serves as a primary sensing modality for robots operating in outdoor environments |
| [Towards Compact Autonomous Driving Perception with Balanced Learning and Multi-sensor Fusion](https://arxiv.org/abs/2606.02979)<br><sub>Oskar Natan, Jun Miura</sub> | arXiv<br>2026-06<br>📑 45 | [⭐ 9](https://github.com/oskarnatan/compact-perception) | We present a novel compact deep multi-task learning model to handle various autonomous driving perception tasks in one forward pass |

## Motion Prediction & Behavior Modeling

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [Flow-ERD: Agent-type Aware Flow Matching With Entropy-Regularized Distillation for Diverse Traffic Simulation](https://arxiv.org/abs/2607.06957)<br><sub>Seulbin Hwang, Kiyoung Om, Dae Jung Kim et al.</sub> | RA-L<br>2026-07 | [⭐ 0](https://github.com/seulbinHwang/flow-erd-project-page) | Realistic and diverse traffic simulation is essential to autonomous driving development |

## Datasets & Benchmarks

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [123D: Unifying Multi-Modal Autonomous Driving Data at Scale](https://arxiv.org/abs/2605.08084)<br><sub>Daniel Dauner, Valentin Charraut, Bastian Berle et al.</sub> | arXiv<br>2026-05<br>📑 3 | [⭐ 405](https://github.com/kesai-labs/py123d) | The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics |

## Safety, Robustness & Evaluation

| Paper | Venue / Date | Code | TL;DR |
|---|---|---|---|
| [CCFM: Collision-Constrained Flow Matching for Safety-Critical Scenario Generation](https://arxiv.org/abs/2607.04451)<br><sub>Ke Li, Kaidi Liang, Yuxin Ding et al.</sub> | ECCV 2026<br>2026-07 | [⭐ 3](https://github.com/KELISBU/CCFM) | Evaluation of autonomous vehicle (AV) planners in safety-critical closed-loop simulation is essential for real-world deployment |
| [Lipschitz Optimization for Formal Verification of Homographies](https://arxiv.org/abs/2605.23203)<br><sub>Jean-Guillaume Durand, Panagiotis Kouvaros, Maxime Gariel et al.</sub> | CVPR 2026<br>2026-05 | [⭐ 2](https://github.com/jeangud/homography-verification) | The adoption of vision neural networks in regulated industries requires formal robustness guarantees, especially in safety-critical domains such as healthcare, autonomous vehicles, and aerospace |
| [CADET: A Modular Platform for Evaluating Distributed Cooperative Autonomy in Connected Autonomous Vehicles](https://arxiv.org/abs/2606.04072)<br><sub>Pragya Sharma, Brian Wang, Mani Srivastava</sub> | ICRA 2026<br>2026-06<br>📑 1 | [⭐ 0](https://github.com/nesl/cadet) | Deep learning models are increasingly central to autonomous vehicle (AV) pipelines, yet their integration has traditionally followed a monolithic design where perception, planning, and control execute on a single onboard… |

## 🏢 Industry Tracker

Latest 14 days of news, official blog posts and new open-source repos from tracked companies. Full daily feed in [`daily/`](daily/).

<details><summary><b>Waymo</b> (263)</summary>

- 📝 2026-10-30 [Toyota and Waymo Advance Autonomous Driving Collaboration for Safer Streets and Freedom of Movement for All](https://waymo.com/blog/2026/10/toyota-bz4x-partnership) <sub>official blog</sub>
- 📝 2026-10-16 [Hello Toronto! Waymo is En Route](https://waymo.com/blog/2026/10/waymo-in-toronto) <sub>official blog</sub>
- 📰 2026-10-30 [Toyota, Waymo to begin autonomous taxi trial service in Japan in 2027](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBsb1pNSi03MEhtRHdzV25vWnZtbkpkbnAtdk8wM3Y0TkZSbGc2ZURFSUR1RlJ5Q2cyeldsR2xTR0VIM2NLUW41d3BqS0xzQWxRd0c2VUtMOHQ2Zw?oc=5) <sub>Japan Wire by Kyodo News</sub>
- 📰 2026-10-30 [Waymo taps Toyota to supply robotaxis for Japan and the U.K.](https://news.google.com/rss/articles/CBMiqwFBVV95cUxOelFPTElwcTFoUXFiU0JRQnBuZFpGVU42UEJMazZCbUlRUW5KTWtHX3dqQ2dGWjIzblZxc3pGNTJGbm5TUi1sNGp0X2dKSzUteC1yQUR3MkFmcVF3dzdUd0gtQ2cycUdQVFRsM2ZHMFRyamN3d3FPS3BDTkFfczJGMTlONFY5T2tlb3hLbU9BTkFaUjc3aUdtbmd4bWVZTFJ6eU10NDVEX3gzc00?oc=5) <sub>TechCrunch</sub>
- 📰 2026-10-30 [Toyota, Waymo to test autonomous bZ4Xs in Japan in 2027, eye overseas expansion](https://news.google.com/rss/articles/CBMi0AFBVV95cUxNM2VSd2JZbTF3VUx1c0VGV1kxb19YbXBHRmoxUzRDYWwyOXRockRVbXZQa1pMR25HM09IbndSS0g1b2FWbWpubmx4b19GZEdOZUZSYW9EMW02NFBfNnNaLWlzX01VbU4zLTNERmpRUVA2ZlZtNHc3VTlJU3pUbkd4QURIX185Q3Q1YkYtRkdFb2FZMFhSZ0dfSHJ4cUpoM2YyVERnOFJEM0RiN3RVcEZuMUNTN3pSOGNDNXJEeXhYVzdwZlZZVlptRFI3WGhLYmZZ?oc=5) <sub>StreetInsider</sub>

</details>

<details><summary><b>Tesla</b> (392)</summary>

- 📰 2026-10-30 [Tesla Launches FSD Supervised Referral Program: Free Month for Every Signup](https://news.google.com/rss/articles/CBMirgFBVV95cUxPYnJhUEdGSU95T0JXa0J4dWZwaWJtX2d2Uzh1NjZrOHRXcE9kNmNBSW5VaC1BWkd1bzc4N3pUUWhQUkhWNVBLNGlIM1hzTTRvVllJNjJ2d3UxYTZGVThMQ2Z5SzJPYzROMzdlS0dyRzRKMTZBakRoS3JzQnpoTWwxREdRQnN6RnV4TzNjcUhfYzQ4RTV6YUZIdEVLRTczXzFYRlVQVU1vNndhTHp6WWc?oc=5) <sub>BASENOR - Tesla Accessories</sub>
- 📰 2026-10-30 [Tesla's robotaxi cash flow could bankroll SpaceX's AI ambitions: Ark Invest](https://news.google.com/rss/articles/CBMiqAFBVV95cUxNcDFsX0k4eDNmLTVSNFNWQ2gxZXVWb3lKbDBEV0xyRF9KcTBxMXpsUlFsYVNBRFoyU2JfOXMzdkYwUFpDMEpKclZQanBOMGlTN1Q5RTBTWkFaaWVrMkdVWVlOQUJsYm5EejYtbVBZUTFPSWF5OGZjM1FhbXZkVVlSc0hFTGFwZzNHWjNoYTVLVUpDeDRBc0M4cXJTMUNpMlhET2JEd0R6SEM?oc=5) <sub>CNBC</sub>
- 📰 2026-10-30 [Tesla Robotaxi: 40 Min for 2 Blocks in Houston [2026]](https://news.google.com/rss/articles/CBMigAFBVV95cUxNaU02eGFPcnZyV3ZmRmI0anZkMkI2YldHblUwWURlSGdMdTFVUmJNZUJlT0tEeEtKMmtmOFUxR0JNbm1Jdm96djdMUDBZRkxQWVhpbFU3OU1VZmpfckdKTFNOeWpodlItSTVnOEJScnpCLVVBQ0w5VVFEZFBObGZSQw?oc=5) <sub>https://tech-insider.org/</sub>
- 📰 2026-10-30 [Tesla made napping in a Robotaxi easier with its latest update](https://news.google.com/rss/articles/CBMic0FVX3lxTE84MDhiWGhZZlpNWVkxMXlkZjdlTkF6RHVkZzhzamhFdGNZNnZQdGhCdGM3MlBJXzFyNk0wcHJoZzNuV2FmNGhKT2tBWXQ5N1dhREJ1VTNDcWJOdWFoaUdGUGRueTFabkdta0ZHZjJfbFh2d1U?oc=5) <sub>Teslarati</sub>
- 📰 2026-10-30 [Tesla Swaps $250 Car Referral Credit for $99 FSD Reward in the US](https://news.google.com/rss/articles/CBMioAFBVV95cUxQb3hZRm1INy1KZVlrcl9jQk1XaF8taHFwM1V6Q2pOVjR0WnA0WDdMQXhKanlsTmlEN05faEVoM01nY0JDb1c2WW8zdDNmRE51dnBVdl9MVTlfdkhweDRhS05YNlBySEVraHR4SWJkVlA4SDA4XzVWYjEyd3lCRnVkcmpiR0k4RUt0RjNrYXY5UUdsOUZud2MwVUtaLXZxUWFU?oc=5) <sub>Electric Vehicles</sub>

</details>

<details><summary><b>NVIDIA</b> (255)</summary>

- 💻 2026-10-20 [NVIDIA/flare-local-inference](https://github.com/NVIDIA/flare-local-inference) <sub>GitHub</sub>
- 📰 2026-10-30 [NVIDIA Invests $1 Billion, Becomes Naver's Third-Largest Shareholder](https://news.google.com/rss/articles/CBMiiAFBVV95cUxQaWdTVVp6ajU1aEVqUXNRQmV2cU1LTThXVTB5TGd3S3dOTnBxVlNCWjdyZjlQQ0w1dkxMZGpBRHAwaU9vaC1WaUhYTk1XOVNXV2poV1JpTEZCRGZqeXgyNUpQUUtKdlVFcE8wZUVHaEZ3cXphNUJZTXliaVlvakVKNzQ2UUNKblRL?oc=5) <sub>조선일보</sub>
- 📰 2026-10-30 ['Nvidia chief seen as target of China spy plot'](https://news.google.com/rss/articles/CBMiuwFBVV95cUxOVHlIaG9SZEExcEVPckQxWHRBUTE2YmRZQnA2cFVhOC02ZFdEc2pIQUhOaF9GdmhsMWgtNGhtRUpEMjdKZElxQy0zZ24wdXkzOGRVOHRmTm5Wc3diSHBQT3hscUdRelZFWjhyMW11akU5dUtoLXdOMUJPODlUUlJQZHR4YjVITFZoYXBBSEZtakNHQ1BOSUZiVy03TTlXSXNJQW9TemY5bmhjUVUxUk5ZTDJydmxiclRhaUpj0gHAAUFVX3lxTE9xeXJwZmhza2lpSDl5SXFsNHcwU3hHUTBCTWtDTkxaQjVfX1VtY1Brd01zamlpdnkxRnRUdjBmTC1IUDZsbHlMRjJFTVZ0V3dxX2tnanU5RmdtcTduR3VWZ3BsODJJTFhIejJ1V0FIaXVscEpFTUdDZm40dEl5TDlpRjFiRWdwVEVHTjhJanNmbzlzTVJzZVY4cnEwdDhfUWZvQzlaLUQxeTBtd1k4NV9QN1NiMDhRTGJFVE10VnlKdQ?oc=5) <sub>The Times of India</sub>
- 📰 2026-10-30 [Honeywell launches Forge Plant Cognition with Dangote, built with NVIDIA AI and Dell capabilities](https://news.google.com/rss/articles/CBMi3AFBVV95cUxQUHFXOHVkbFcxdXZSeGFKejM0M2Q2WC1TT25jOUp4WFZ2Xzl4VUxTNHo3OHNWUzd4a2xCV0g2R1hLUUo2TzJ1YUhfOW50TlcwVklGRHR1VWo4a0NaQWFrejRhLWJDZ2liaHRGTjgxUUZaTm1mV2NWWnpPNnYwRGszUllIM1NBTGlNekIzYi14OFhCSzdjOERzbVlIUXNRajdIUTQ2bWpGR0hlTHczM19hZTNnYk9fd2xRSzQ5SG9yX3h3VGNCS3NCdkhuRlI3QXhxSFYwRC1DcXIwMk9F0gHcAUFVX3lxTFBQcVc4dWRsVzF1dlJ4YUp6MzQzZDZYLVNPbmM5SnhYVnZfOXhVTFM0ejc4c1ZTN3hrbEJXSDZHWEtRSjZPMnVhSF85bnROVzBWSUZEdHVVajhrQ1pBYWt6NGEtYkNnaWJodEZOODFRRlpObWZXY1Zaek82djBEazNSWUgzU0FMaU16QjNiLXg4WEJLN2M4RHNtWUhRc1FqN0hRNDZtakZHSGVMdzMzX2FlM2diT193bFFLNDlIb3JfeHdUY0JLc0J2SG5GUjdBeHFIVjBELUNxcjAyT0U?oc=5) <sub>DQ</sub>
- 📰 2026-10-30 [A spy too close to Nvidia. Trump knew about it and did nothing](https://news.google.com/rss/articles/CBMiwAFBVV95cUxQX1JZbzJ0aGVBdDZxblkzUlQ4VmdZSFBXend5YUdxUXpJUktrc2wxZFhQVUNkQ1NEWnFHNkFDY19kYXE5ZTEyUjRTQVNEa0h0NmhJRVhZeEhzazZ3LWxzckowcGZmMUNwUnRFSVlWbm41UGFfVzEwTnVNTlZRaXY4RGxQbHhEWUU3b2U5RXRpMVF0X1h1NVkyQ2M1aGFWem15M05vUWVFd2xKT0paQ2Y4SWJ0MFZTUWk1bkNFT2JnekY?oc=5) <sub>Il Foglio</sub>

</details>

<details><summary><b>Wayve</b> (64)</summary>

- 📰 2026-10-30 [Nvidia's web of AI bets: smart strategy or bubble risk?](https://news.google.com/rss/articles/CBMivwFBVV95cUxNVkZCd3RXTzVrU0RxVml6c1ZyYTMyVU03a09YRVdrNXhvUkU0M1REYzlBYkZfLUlKcUxVZ2VKQVFCenJVSEdTNEJZNVJKN0xpb21fVjAxUWhOb2lHWk55dE1Gb24zZWpWLW9zbE5VckZ5YXktY1BCblR6cFJITVJDT3B6NV9FcVljaXY4QnpKQ3FrWjNzQV9MSC1IWi03S0phYXd6UDlnWlVFOTh1ZFhMTS1jM0RINTVGcEZ0UG45MNIBvwFBVV95cUxNVkZCd3RXTzVrU0RxVml6c1ZyYTMyVU03a09YRVdrNXhvUkU0M1REYzlBYkZfLUlKcUxVZ2VKQVFCenJVSEdTNEJZNVJKN0xpb21fVjAxUWhOb2lHWk55dE1Gb24zZWpWLW9zbE5VckZ5YXktY1BCblR6cFJITVJDT3B6NV9FcVljaXY4QnpKQ3FrWjNzQV9MSC1IWi03S0phYXd6UDlnWlVFOTh1ZFhMTS1jM0RINTVGcEZ0UG45MA?oc=5) <sub>The Hindu</sub>
- 📰 2026-10-29 [AI-powered 2++ vehicles to run on Japanese roads from fiscal 2027](https://news.google.com/rss/articles/CBMiVkFVX3lxTE9EZW4xV21QVU9kRzJHTFczaUNiVGdxaWxXTG5heW5aUDVDYUtxaEtDY1FZV1YybjRrMU05eE5jUFBLYk5ZQ2Z0V0htQzdhc20tUHVoQnFB?oc=5) <sub>朝日新聞</sub>
- 📰 2026-10-29 [Top 10 Best AI Startups In Europe 2026](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1RRXVxTmhjbTU4M2VfczBRMXFSODNPQm5qbUpBWGlMQncxZWNESlRzZHNVNVZBY2J6cXRuQ0lmX1lJV2xrR0pPOFZoeTlhdm9WLURzaXpMT0t5a0tEbmx0OXdJajJOelk?oc=5) <sub>Nubia Magazine!</sub>
- 📰 2026-10-28 [Top 10: AI Leaders in Europe](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1uRm1MZEtJM0RpZzFfTnNoNHJaYkdXRVFhekdtLUUyamQybC1oT3djc2RZMTYtOUpEWkNBNGVQNFdyZFFhNGQ5MkVBZWFZaFdldVc1WkZhR2Z4SGpUOFd4SjEtby1aaEk?oc=5) <sub>AI Magazine</sub>
- 📰 2026-10-28 [Nissan makes next Rogue its first software-defined vehicle as it chases Tesla, Chinese rivals](https://news.google.com/rss/articles/CBMigwFBVV95cUxOSW5oWFBKRzR3Rk0yU2hOZ19PeFJrbWRESDVoWWliMzYwdG12ZWYzeHJLSkw0b1ctckRWckVEZnktRFNNYWMwWHhHR3duNDl0ZUhrUEZJSVpwamI2Y19ZMkUzRTdGVmxDYzVSZEV5cTY4TWhsZ0lYeHNSamRvS3loWHlmWQ?oc=5) <sub>Automotive News</sub>

</details>

<details><summary><b>Momenta</b> (114)</summary>

- 📰 2026-10-30 [China's XHEART ships 200,000 X7 Ultra large-model autonomous-driving chips in two years as 700 TOPS part enters mass production](https://news.google.com/rss/articles/CBMidkFVX3lxTE9UTEpnczNrTUxQdUlTRnloUVMzbXRjS2UzaUczSXp1bkxYWjFGa0Z0WEtXUHFkZ0g0S0xnTGIwT09obTYtanNYNDhtSXRidG93UndZZ293aXdWb3lQRHZpb1h5Ty10TFFiUGRLdlZJdnNfUm80aEE?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-30 [XHEART与Momenta，重算智驾的算力账](https://news.google.com/rss/articles/CBMiakFVX3lxTE1aWGpMSnFfSC02OXlObWJqVy1lQjhmc2VYQUN1NDNfWmt0ZGFIcDJ2eEowRFVKaGJlUUlEQV9CWFo3UVNCTW5UdHhObU85QjNxZGZ1RXhaeEtFcU9lUVNmSEhSOXNuXzRoN2c?oc=5) <sub>风闻</sub>
- 📰 2026-10-30 [算力3000TOPS，XHEART智驾芯片是行业第一？](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBwOTF3T3dzVFJKcXFBZ0EzYkFscmN4RnIwSEw5ZUJtVTdrWHllUjJuMFo0TWxrODNXOXRtT21yakxoRVZpaUZ6X053WC1NSVkwa05qbmg2MDdLTzQ?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-29 [智己 LS8 NEO 纯电，更大，更强，更领先！](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBSLThBU0k1OWVYbm01QXduaWJ1aGJHdzFxTkNzLTNjMUpVdm8yaFFXai1PNW91ZGJzcXJURTVrYV9MaE1IYklWMW10azBoc251QTJhMHlrakdIWU0?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-29 [700 TOPS of computing power! XHEART unveils large-model autonomous driving chip; industry partners including Taiwan Semiconductor attend](https://news.google.com/rss/articles/CBMirgFBVV95cUxPenFvcUdObnJBTFE0Y0tJUkMzY1haQmJUVFZJUFpjQzdDSzAtX2t2ZG9GaHlaenF1Tk5SMGUwczhtNklXMjZURnJyQVZDektmLVd2LXQwdHBUR01fRm5aR2tGWHdQOTV4dy10ZzFpZzdjWG41VHd5TjNXTHVmQzZXN0s4aThCVFBWalRBSXA0TGowRGN1QkxDTUZDdUI1YWl2bms5d2RmeUU0VDVkYVE?oc=5) <sub>Moomoo</sub>

</details>

<details><summary><b>XPeng</b> (253)</summary>

- 📰 2026-10-30 [【视频】13万级配图灵AI智驾？小鹏MONA L03卷出新高度](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9ST3d5TmpMREcxdnc1MVdkZFN3T1Z0Z2F2MHJVanRmY3FiOGJ2UndnSzVjSGk1ekt3OHo3eWpJQklBZUpXUG1Ldk43UG15Y2pJSWR5ZS1xekROeEE?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-30 [小鹏MONA L05正式上市，搭载图灵AI智驾/增程综合1310km](https://news.google.com/rss/articles/CBMia0FVX3lxTE5pQ3VTME1UeUNDRGMzcW5qZmFrQW9UMnBmSlJEOURBMTN4VzMtNXdHRF9UYUdPNnBSRGZJV1Z5cllFMi1Nd2Z0WlN3NDlxNHlja01JTGc3SDhOMGtDYXhobEFLTDBPZjhVQllB?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-30 [【视频】13.98万起上市！小鹏MONA L05，带图灵智驾的大五座SUV](https://news.google.com/rss/articles/CBMiW0FVX3lxTE4tQmozZ2UxdVN1RExvNWpNbXZabHc1YzkteGpCcFJsV3ZzS1VkMDF0MFFJZGJKQnMwaG9TQUNya3pBMVMySmtPb1B2cjBSR3NrX2dfUWlQd1lLTTg?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-30 [小鹏MONA L05上市14.98万起，智驾与Robotaxi同源](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9WOXhtMER0Qzcxc2xXNG90SVhhb1d2MDk5T29PQU5SOWVRSE5IUGZlcDZQSVgwcW5xd2pja015c1RFVjc5dXNpU1J2S3pEb21DTl8zczEyX0podzQ?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-30 [小鹏MONA L05保姆级导购丨限时13.98万起贵不贵？6款配置怎么选？](https://news.google.com/rss/articles/CBMiW0FVX3lxTFB3a0UydVY3TWh5Tm0ta204d2lUcHAtbnIyOXN6aTY1X3kyZXhfRkZUY2MzNG1oc2xvRENmWXBBREh4ZHpVRVlPQWFhWjZXU0VTTFBSdldRSURjaGc?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Li Auto</b> (154)</summary>

- 📰 2026-10-30 [Li Auto's i6 production reaches 200,000 as November capacity targets 20,000](https://news.google.com/rss/articles/CBMibkFVX3lxTE4yMUtJSjYwVEdNd0N0M2pmZkdyUWJ5bVh1ODgxb0hEM0F0Sk02bTNLZV9oMFlNd1pxdWx3S3I5aUptRjYwb05hZ29Ma1hVcTdydkpCZTlEbWN1OFZaNFUxTnRSTFAzZTZpRXVOZ0Zn?oc=5) <sub>CnEVPost</sub>
- 📰 2026-10-30 [How Does the Li Auto i6 Turn Flagship Technology into Standard Equipment?](https://news.google.com/rss/articles/CBMizAFBVV95cUxOMlNhMW90STl1YVJReUkxdFEwYklGR2JpSGxiYTNIT3Nzb1ZYa1hqa3IydVlCYklCZG5YTkM5YW9zZzlXOWNWcHRpTHE0MXVqVUF3Wl9iZ2NFOS1sM1FjOHZEUjBSR1I5N21uSThaaWV1eXhRSGdfQjRBV0swaVVjczRqMHdCWFRnRHpEME43ZVJZUjdYODF1WjJrNXl6MWE2THdZN2RFMnR3YmEzZEN1TGpRSXFIaEJtT0o3REtoS3dzNXFRWUxyXzBsTzk?oc=5) <sub>Gasgoo</sub>
- 📰 2026-10-30 [从空间到智驾，横评奕境X9、理想L9、问界M8、领克900，谁定义了第二代家庭旗舰？](https://news.google.com/rss/articles/CBMickFVX3lxTE9ZSjdVYXQ4SHBsTGlQc1NYenlSaXk0QWRRWWxKTjh0TlItc0w2QW1JQWRNV2Y3TUVIQUltRndrTUtlV3dlYm5ZRGN0WDZEd0d4WVNsV1BnVWw2WEJ5aXpPRWZtRjl5ajNlMWZILU1VTjhWQQ?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-30 [3款20多万增程SUV智能座舱与智驾横评：小米澎程、理想L7、比亚迪唐DM-i怎么挑？+FAQ](https://news.google.com/rss/articles/CBMickFVX3lxTE44dDJhYm5fWGo2NUxSV3NzYzJaMi1ZNXdHbkRoQTVzWHFEQ2lOdXU2S0dIWlpqSk96QThzaWFPSXFQQmI2bklCRTNGd3ZKbTZmUThIbFJMZlNsV2hqdzRqYWRfcEhobnZKUVl4M0JvX3Zqdw?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-29 [Li Auto's 2026 i6 Launches: Self-Developed Battery and Chip Standard Across All Trims, Starting at 249,800 Yuan](https://news.google.com/rss/articles/CBMidkFVX3lxTE4zVm54UEt3V0g4WkFWVlRaRWl3a1lZYmRhSHN0bjhCNlJOVlhITnlFNkdEQXl0X0oweENXbjJMU21uNzJfY0lqMmM3UW1oRzBZQ0ZCUXhjSlhUZm5qNjJMenVSN05zRThtNGhkcWlLOGJJc0ZMSkE?oc=5) <sub>BigGo Finance</sub>

</details>

<details><summary><b>NIO</b> (142)</summary>

- 📰 2026-10-30 [【视频】新到店26年蔚来Es9](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBNZEEwT1dhX1lGWkN4bi0zR1dSNEhmaTNzRzFQUXZKWnFaMVVtTlg5V3RoYk9GQzFJMExqUjE3NjdpWjZDdDU4a2pVN3ExYVF2SHVjZmdDLUxuX28?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-29 [Nio Smart Factory: What Makes its EV Plant Different?](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQaWRpNFEtbGhmLVd5aG9Femh6RnFXZGticFpNY2ctTjdIb1BPRHdweEhFYWY5MElZWFFVa1F4ZUtGVnItRTFSQXM0Qjd1WXVQd0RaV1VtaE5YOGxpZE1pNTdXbHFwdmd5MFk5OG90ZjBUcmJNTTdScDd1endwX0hPSmpqSkVPTWRNekpJY1VNdmxmMC1ud0xCS0ZpWlFQNmV4NXRzX2V6YmtRNm_SAasBQVVfeXFMUGlkaTRRLWxoZi1XeWhvRXpoekZxV2RrYnBaTWNnLU43SG9QT0R3cHhIRWFmOTBJWVhRVWtReGVLRlZyLUUxUkFzNEI3dVl1UHdEWldVbWhOWDhsaWRNaTU3V2xxcHZneTBZOThvdGYwVHJiTU03UnA3dXp3cF9IT0pqakpFT01kTXpKSWNVTXZsZjAtbndMQktGaVpRUDZleDV0c19lemJrUTZv?oc=5) <sub>Artificial Intelligence News & Cryptocurrency News: Latest Trends \| Analytics Insight</sub>
- 📰 2026-10-29 [再测蔚来ES8，世界模型NWM迭代升级智能驾驶](https://news.google.com/rss/articles/CBMikAFBVV95cUxPS1R0aktfU2IwU19rMXN2REc1WGJDVnVwTXRDZ3VWTHhtVkUwSE5PbUNaQzhOZUs1TGRrZngzZW4yWjRzVTNHSnp6OHBMa09JQmJzREJMb0JzSjJsR3VBWlB6LUc1Z3pFbVlPOUxxV2hQUFRoRkhrTmNzTkxySVlhY1RFbVdES1phaW9QQXBQekc?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-29 [蔚来ES8值得买吗？40万级六座SUV实测：高速续航353km+3.97秒破百+FAQ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1yZ29jTDc3QnFNMTVvTkQ0ZzhVbmlKYVRqZmh3cXptTktTejdyU09rZkxwUEdwY3ZKajFoUnZ0X3hpNkJobm0wTkZOMnl1NzFzZVh1d09TUlFuNDQ5dnBj?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-29 [蔚来-SW(09866)股票股价_股价行情_讨论_资讯_财报_数据报告](https://news.google.com/rss/articles/CBMiP0FVX3lxTFBtZlJUaTc2M0diM3A5RHdVcGc0MXoyQlYzTzlPSEl3V3JkSVRlRGQ1MGd0QVBHSkdvSXEzWmh5Zw?oc=5) <sub>雪球</sub>

</details>

<details><summary><b>Huawei</b> (340)</summary>

- 📰 2026-10-30 [Watch: HUAWEI nova 16s Pro Review - Stellar true color selfies, 200MP cameras](https://news.google.com/rss/articles/CBMiekFVX3lxTE44TWp0SWRUZTY4SGx4azBoVldtWFFNcWVqWFdsOUxqZGE3Qm9NazhkSTMwd3FmTjRMRzVfS0tpOG84WXRmVEllNThUcXVKNDAyYWJrS3VJNUxfOXhaelRyaWpEVW1rdGdYQnpKM3BoOEwyYVRyN2UyRVdB?oc=5) <sub>GIZGUIDE</sub>
- 📰 2026-10-30 [HUAWEI nova 16s Series pre-order in PH: Worth PHP 14,997 freebies, starts at PHP 29,999](https://news.google.com/rss/articles/CBMiigFBVV95cUxOR1djZF9kbndhTjdlLURDZzNxOE5aSFhNMHltMjF2Zlo0dlJqNTRRQWFscTRmWDNLeS1oTC1GaFhBM3VvZUIxMkRkaTlxbkJEY3ZGWlVIenVZUDhDOV9kTmR3aVdSR2JpV01fZTlGUk8tRFpKV2kzcUtBWU9Iam00UUVDOVk5NmFYNFE?oc=5) <sub>GIZGUIDE</sub>
- 📰 2026-10-30 [鸿蒙智行问界新M8选配公开：华为乾崑智驾ADS 5、全系L3级架构，预售38.98万元起](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPUlc0Y05tcGhkZ3dnZTZ4bXBMWEh4OGlEWW5LeUVzai1XRVB0VE1ya1BDLTV5ZzBscG13WHJTUjhRaFNoS3VYUzA4TXpITU40a2RQdEVUMlVlN29idUt5b3FDc3VxR29nb2pyMERsdl9yOGoxZFZQMTJPZmZaeng0SER4Unc4cU0t?oc=5) <sub>搜狐网</sub>
- 📰 2026-10-30 [闪电快讯 ｜ 阿维塔07L Max纯电版上市：搭载华为乾崑896线激光雷达](https://news.google.com/rss/articles/CBMieEFVX3lxTFA1Q0Mtd3hYT2FwRTJYamFwVVhPN3ZXMzNveGg4YWVmdExaeDloLXFVSXVOREQ1a3pWV1dkd19MS2VEX1dTc2pOUmNNSkpXb1E5NEIzRWtOdnBkQml2OGRkNWRRZ1NFY2ZyUllveVpYREpidUMyUW5wSA?oc=5) <sub>新浪财经</sub>
- 📰 2026-10-30 [搭载华为乾崑896线激光雷达，阿维塔07L Max纯电版上市22.99万元起](https://news.google.com/rss/articles/CBMiiAFBVV95cUxQUlFIWUM0NDM1dnotckg0SERnQ2pwX0lRUkxCTXlqWm96LWVrRWtiSHhUYkxGQ2EyYnh3b0IwejBVSWoxeDRrZnRuc3BHYS1pSTFTSDVLMzFwWEE5dl9VbDZGb0RPUmgxSDVqX1djTEh3aW9qdVpaNU9kdFdGZ0g1NzFKQXpJdllR?oc=5) <sub>搜狐网</sub>

</details>

<details><summary><b>Baidu Apollo</b> (61)</summary>

- 📰 2026-10-29 [萝卜快跑负责人黎宇昕是95后真年轻 提拔真快](https://news.google.com/rss/articles/CBMijAFBVV95cUxPMnJRRnBTeU9TUVRkaHFaS2lvZmxDZkVxYTJ6SVQwN0dIMnEyRVRhXzhxU21TZEFRMlAxT0Y4RU5XbVhpTEpIeDB4YUNlOUpsemdhcDFTVXNsRGlNMjcyWmtMeExRUEsyWjRDRHQ0TTRkalQ5ZXdjUmlZcmtvSzY4LVpZa0N0ZUJXeGtaOQ?oc=5) <sub>搜狐网</sub>
- 📰 2026-10-29 [Baidu Develops World Model Tailored for Autonomous Driving](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1KZW9yQ1FwYWdsbTlYMFYzZFVfeEVuVHI0RDNXSmYwVlZQY1dFbjZYcnh3WVU2VDFmMUdvcGZ4WVNPVW85RktteEF6OHFVdWtlUDlr?oc=5) <sub>36Kr</sub>
- 📰 2026-10-29 [Key facts: Tesla (TSLA) 1.7M FSD Users; Barclays Upgrade; 450x PE](https://news.google.com/rss/articles/CBMivwFBVV95cUxPWFZJaWRRamJxZXQ4amY2LWo3Um5HREFMemhuLTVybWg3ZEM3SzVyY1hsVHV0bmx2cG1UQ3F4ak8zMUNGYzlDYWtnQUk3elFMdlJ1TVFJd045c1Nvb0NNX1dobUU2NmluM3d3VkpIY1NCZXFkNHV0MjhDVEpHZEREXzdJLWFYYzBzanhHVWExMF9nN0ZWMTZsU1AtTldMWk9ETUs1WTF2SlR6MWtlX0JweHQ2ZzVTTHVwUnI0cDNycw?oc=5) <sub>TradingView</sub>
- 📰 2026-10-29 [Hesai Leads Global Robotaxi Lidar Market with 62% Share as Robotaxi Industry Moves Toward Scale, Yole Group Reports](https://news.google.com/rss/articles/CBMi8gFBVV95cUxQaE40Ym5SMXFZYWhRM3FYYzUxbzI0Yk5tTExfWVpsMW1mTkdRLTNpdVJPQkR6NzJub2hFaFZ2TWJlc2VWdEVlZC1ZWThOb0U0aV9pblFOSmZNQ2t6bVNjRnoxeVZnMVRVTnpZNkgtTXZyM09nMmNUb25VVlBpR1ZGeEtIWGlSUWhJMFBCUC01dDh3R3JLOGxDNEpacEMwRWZoNmEySU03emlOTENXbDhMS0ctSFVRaXJRZ0RPOHFKdlVucTM4THc4YnhCR09LV1FpSnBEcVRneEI3d1hwdlFieGIzaV8yaTY4LWMwTzNIc0Rrdw?oc=5) <sub>Thailand Business News</sub>
- 📰 2026-10-28 [Robotaxi标杆停摆4个月后低调重启：萝卜快跑在武汉郊区恢复接单](https://news.google.com/rss/articles/CBMiXkFVX3lxTE45ZGMyRjVJcWhJajIwVnR0NXA3VjN6NTlUc3IyaWdiRFVkLXVtYTBrdjRFZUIwcDNDa3RlWnlNdmRsRlc4YTRDMi1tUS1ONnl4Z2RhckRVZlNCWGVOMnc?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Pony.ai</b> (151)</summary>

- 📰 2026-10-29 [广汽领程与小马智行联合研发，T9 ROBOTRUCK在广州从化正式下线](https://news.google.com/rss/articles/CBMijAFBVV95cUxONGNtU2xFWHRjT1BrbGN6U2tYbWNtRHVNc1lCdmdDZGhyUTQyTlhwa0V5cERZbGpNYnRCdjdRWkVsQkI4bWZEYlItVmdGb2xYMGlRYXNuOXlBUmQ1YW1heU44b2dvdURFWnRJbFd6d3QtWUlLNWZGZmxYRWduTFkyajVHNW9vTTBlNElkdQ?oc=5) <sub>搜狐网</sub>
- 📰 2026-10-29 [北京小马慧行科技公司增资至2.2亿美元](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNZFhuS0dyU2hDcHdyVmREeVpCMFNHY3FEbzFDM2hGS3c2V2UxUGlGakFPTWhPZEE0MmxjZHJVcWIyQVl0QVowV3kySmwwMDNrTy0tOW5sSF9nYUNBQlAtd21mXzBVMENZaXpTVnE1NDJ5TUdsRjRUMkx0YnBoTS1xdVI4VDNuRjA3?oc=5) <sub>搜狐网</sub>
- 📰 2026-10-29 [Kodiak AI and DTL to Deploy Driverless Trucks Across Sun Belt](https://news.google.com/rss/articles/CBMimwFBVV95cUxNazhJV0M4LWM1V3pmWnYxV3F4bE1UQkVIbmJYTDdHTjd3c0RwMHdabWJPZ2pHY2RZaThId3ZidVdIcUc0RG1vSEFsQTN6M0J1S1pIQllkc0JpNGdEQXNkRVYxS2YyaFNfVml5TUtoZ1pfb1N3SFBFNkRlU2hwcWN3T055bWtSNlFzSG13eFVfY1ItYnNZNllGckhIaw?oc=5) <sub>Future Transport-News</sub>
- 📰 2026-10-29 [inDrive, Pony.ai and NVIDIA explore robotaxi launch in Kazakhstan’s Astana](https://news.google.com/rss/articles/CBMiX0FVX3lxTE4wUnBhd0JOQ2Jza2ZVN3p0bFNoR2Zpa1dGWTdoWXNGakRxS3pnQzBmQ1EyR1M5QTBGWVlxS3NvSEs1bnF1VHpnTGROTDE1MXh0SEE3V2FEQ1E3QVBlRXFv?oc=5) <sub>Trend News Agency</sub>
- 📰 2026-10-29 [Croatian Self-Driving Cars Take to British Roads: Verne, Uber and Pony.ai](https://news.google.com/rss/articles/CBMipAFBVV95cUxQdUR4S0E1RUNDWS1nSlFwVjVSTTJSdU4wVGk1eTNsaERjSE9qaFc3ekJLb05pZHR1VVVsbGg2YjlxTXFlVUhScEdpcDFsUmRCeGVSOXBod09CT1dfQjNUaHFxUmxOUXJqUWRyQVdWZ0RwaExQajNVSVVYaGxHUlhHaUlsVjdhbEdhSmFFd2VvVUJWTnEzYzJUN3NndXV6R3BhR01mNA?oc=5) <sub>The Region</sub>

</details>

<details><summary><b>WeRide</b> (127)</summary>

- 📰 2026-10-29 [文远知行001号员工带队，景烁科技融资数千万美元](https://news.google.com/rss/articles/CBMid0FVX3lxTE9lTnNlN1Z5ZVpwQS1JZ0hfXzZ3Z3JtZkJDWF9pVkdQZnNWeEZiekUtTkFja2RpVjc5R1JQdGNGd3pkR3BUTFNpZ0tmejh6aU1TTFc0V2FvQzM5LWxHOEFhOTdVVnlFbW8xZm1sNzlsOG0yZ0lSVmI0?oc=5) <sub>新浪财经</sub>
- 📰 2026-10-29 [文远知行-W(00800.HK)：景烁、台州文远及投资者订立增资协议](https://news.google.com/rss/articles/CBMijAFBVV95cUxPclo2Y1JURlMzTFVxRUVfb3pEem1jUURha0RpbHlMb1BFRTFRcFgxa1U1ZTYwUEllbDFxMzBIX012NHBCU3QyYW81R1c1SjU1XzVJd2JtN1JfelNsNmtxTXdvbVJHQlFSdEhDNjZwS2JnX2l2TmJvcW40OXhhX0U0Tk15T1BsSmZrUHZ6dw?oc=5) <sub>搜狐网</sub>
- 📰 2026-10-29 [文远知行 - 投资者将以合计对价人民币7,000万元认购景硕注册资本人民币400万元](https://news.google.com/rss/articles/CBMivAFBVV95cUxQeUxYUzI5UE9MMzVyMUpqTTlkU0h1QnQ5RE90MjBLVjNsb3RSbWVlTl9CNlg5TDVFTFRndWZ5Zm5kNnpPbDIwdzJEWlhYNlE0QWhTVjhWT293bEEtY0Q3OXdnLWJaZS1jWTFXODhoRHg4b0JaNi1oWU5UZ2gtanZIUUVUMXFLdTgwUlNvU2N0aTh2TjdUcTBRUGdjaGJlMklVc3g0RHJsY2JxS0RwMDVaemhoQjZ3Q2RSMVREcw?oc=5) <sub>Moomoo</sub>
- 📰 2026-10-29 [文远知行(00800.HK)全资附属引资7,000万人民币 持股摊薄至67%](https://news.google.com/rss/articles/CBMiXEFVX3lxTE84cmFSdzRqaEhXWXFMZ05xelBReWp2QjY4VldjMzBXMHhRYkYyZThHYk80ZlBIbFlTY1NjaGVNSFRES0RnN3JqRzFldTU3MHpkT2hGZ0gxd0Qwa0dm?oc=5) <sub>Moomoo</sub>
- 📰 2026-10-29 [文远知行-W(00800)：景烁、台州文远及投资者订立增资协议\|港E声](https://news.google.com/rss/articles/CBMiS0FVX3lxTE9zZkNEaEpxcEJtX1NOMWJrS1E2OENZNm8tdEZlT0pULVFYQmlOLWZlY1kwR3E0cE9sTVV3eDhndEt2dDZGd196T2t4RQ?oc=5) <sub>时代在线</sub>

</details>

<details><summary><b>Horizon Robotics</b> (164)</summary>

- 📰 2026-10-30 [German President experiences Horizon Robotics' intelligent driving technology](https://news.google.com/rss/articles/CBMi1AFBVV95cUxNNGhwZEtUV0hPRGRuUHdRTDBtOVR2MVJXMVpaMW0yQzBCUDh2QmRLNE1nNm8tb1pwNFJfdUVxc1AtMHVaMzhGQTFnVllyc0lybE1hcnpRV1MwUHZranVJRkRwQUVSal84RmU3TnBZckJoSjNaYUlWR1RKYWRRY1AzYzFTWFQ2UDZnMU0yd2FZZ2Z4UVBVUEsyVVVndXlkZVhEVEJGdjNkWXVWQjVxQTZqdUtzUEJPVjNIQjIyQnVPZ29PV3lRNzRXVEZLUm5LN2lhY0xNTw?oc=5) <sub>Gasgoo</sub>
- 📰 2026-10-30 [【视频】全场景倒车比ADS还牛？地平线HSD2.1夜间辅助驾驶表现如何？](https://news.google.com/rss/articles/CBMia0FVX3lxTE9CTzNvNG9HMExYaXllWnpQQzFzcDlIanFzRi1VSkpHSGhKbGZ0TkhNMEZxN1NaU2RaVlR6aGN2MGFiSXdaSml2dGZKUGF4ZEwwZXZuNm05SE9OM3VfTW8wRW03ZzQybUtVR2Yw?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-30 [从实验室演示（Demo）到规模化量产！天瞳威视助力精益智驾走向大众](https://news.google.com/rss/articles/CBMidkFVX3lxTE5oa0Q0MWQ3QzgtbGtTOGZVU1NGYVJ6NENoMnEwVDl2Y2JjXy1DbmdkZlBCTW1KSmRCLVZYUEttZXpoNzJySmUwc213Vk5BM2owZngxNlVZY2IyWTFRaWVibVptZGdpOWZrNU15MFYyTG9tT2NOTUE?oc=5) <sub>新浪财经</sub>
- 📰 2026-10-30 [2027，地平线和Momenta系在芯片上撞车](https://news.google.com/rss/articles/CBMi2wFBVV95cUxQajJGUzFRclZQZXdRV2dhVG9naTZoM3dzNk5aQ2ZJOUlHN1lIYnlIeUtJcjVCTFp4MHpsVldrbXMybmZfM2tOVGpTbWw3cnNYdHlTb2VrcmljR0gyWHNRMGktemwxV3VhcTNKelpwNjc3OHptYk1KNDR6dEJfZHFVM2xWMUw2MEs1NTNGb2VRaUp2WTVpc3h0cVJRY2UtZVhSU3p1Q2MwU3lxcEJoN3ppdnpvaXNPNExpa2dremlkNy1OS19ZQUhxSVVaOFVsckNDZ3VoTnJSZHBydHM?oc=5) <sub>手机新浪网</sub>
- 📰 2026-10-30 [算力3000TOPS，XHEART智驾芯片是行业第一？](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBwOTF3T3dzVFJKcXFBZ0EzYkFscmN4RnIwSEw5ZUJtVTdrWHllUjJuMFo0TWxrODNXOXRtT21yakxoRVZpaUZ6X053WC1NSVkwa05qbmg2MDdLTzQ?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>DeepRoute.ai</b> (29)</summary>

- 📰 2026-10-29 [2022‑2026H1 国内乘用车 NOA 第三方智驾算法厂商全景梳理](https://news.google.com/rss/articles/CBMiU0FVX3lxTFBkSDRpNG03a29aNElYOFZSSjE5OE5iMTRISFd6ME1DWnE4OG95S0FlRFYyNm5oNTRlNktRcVc3VXo4TFpPZ3V0QWxqRjJwMElGWlA4?oc=5) <sub>电子工程专辑</sub>
- 📰 2026-10-29 [他在不被看见的技术高地，砸碎了一堵西方60年的技术高墙！](https://news.google.com/rss/articles/CBMiZEFVX3lxTE93ZmRqYi1TVC1qMXJpSEdYXzhCVEF4TGhqT1BVZngwVW9UeEQySDYyZ05uaDViX2ZxN1lmdkVLM05sXy1LdmxjVGstaWwxUnd6akhRZnpYUUVzRGNfODJ0cWxfUnc?oc=5) <sub>中国新闻周刊</sub>
- 📰 2026-10-29 [摩门塔发布700TOPS大模型芯片，“算法公司”继续拓展硬件边界](https://news.google.com/rss/articles/CBMinwFBVV95cUxOcEF5bTVVbWlfcXcwRlplZUhvaTJZMmNKV1ZiSzh0dkVJT3JTZkZyS2R6b0oxNTQ2LUEtNVVLZ0J4dy1WeGFhbnM0djhFMEtuai1WRFVuYnp2djhjRXotTm5BQ21pNC1XLW5DUV9lbko4d1pSVHZUOENoZHoweFV6WjNjRUFIeU9ZVU9uOWtvaFdlSllTR1AwSjM1T0RoajA?oc=5) <sub>汽车公社</sub>
- 📰 2026-10-29 [赛力斯AIVA ME7纯电轿跑SUV搭载豆包大模型，对标小米YU7](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9EeEYtUUFTdlF5aEpOXzBZaFZMRnlUMUU1Z3dPVHoyVFFGaUNnZlNMYklmc2hxRXRLcUpPUDVXMmtzY3czTV9mVDNqT1ByTlZyUU8xOC13Rk5sNFk?oc=5) <sub>汽车之家</sub>
- 📰 2026-10-24 [4款7系SUV扎堆上市，问界M7车长5080mm](https://news.google.com/rss/articles/CBMiW0FVX3lxTE14Njc1UEhVa2JDUjZldVh5cm9SaHl2bTB4dE5fQnVEbEpuUE1UTzJQS0dXOU50UjVYYm9IeGwyVFIzQ085QktXaFBvaExySzQ5VFROUnoyY2hCT0U?oc=5) <sub>汽车之家</sub>

</details>

<details><summary><b>Mobileye</b> (34)</summary>

- 📰 2026-10-30 [Mobileye Global (MBLY) Dropped, What Is Behind Its Latest Move?](https://news.google.com/rss/articles/CBMi0gFBVV95cUxPeV9lYmcxQk5FbDhpNTJzVWw1Nm1OYS1SRS1xdU5YbS1ybXV3MTV5YUtwSGFYTGJvWTJOWHpVMVVraUs2R0VwSmFzbzB5bzFQajNGMVlLUW1KLW9qNWV3eTROMTZwVi1vTF9xeXVxTDNjZWpUbi1pNV9zcnRNS1pmcUNDbkpRUFgzZGtjdzZMeDkzVWVDLTl2S19ESHA3eUFYV29IQmRITWtLRVo1TVFjbm5KR2NHTUR6dTRVS2VjWENEVzdyZ3JBUFNMN2RuVnpveXfSAdcBQVVfeXFMUHNYLTFxZVNVNW12WVRKcGtqTXhPS0c4R1ZBMmtMaWpjMWdfRTE0X1d6bm1rZ0lpVUwzV09LWE1vWWx2bGdhU3RLc2QycWQxMHlIbDdreUVOQXFHWHh2UVNvWFJnci02bmhWcTlqNDV6Nk1lejQ3U05iTDFSM1JYU2Rpbm1pS2pnOWJaNFU1Q0U1bmtEaEJYaWN2dzEyS0pYb1NsMkFDRG5oOTEzaWZuMGtVTHFCdUZ1dU56T0ZmdFBfc3BSSUhmVEs5N3diMEJXaGt0VWluNjg?oc=5) <sub>Simply Wall St</sub>
- 📰 2026-10-29 [Mobileye slides even as it tweaks full-year guidance on SuperVision strength](https://news.google.com/rss/articles/CBMi1gFBVV95cUxNaEtXanY5ZnlTNjZLRmkxWjgyeHdVZDNBWUxQTzZWWm1fM0Z0bjdFNE1CU0ZDdzF1Z0NwV1QyN1FQcmdvR05SSl9EVEw1ZzJBVWdfcGt2SzE3eEZ4dFZWVHZ4NXRlY1RuVlhLY180ZDRXNUtCVXdQRjYtSllDMjVvamM1U0ticFFzeXgwMm4xTWN6RDJONlNZN2xDUklQOFU3ZnBULVBMNW4xSU1UYTNNcE5QMUhVNDUzMmxuZU5PbWozbDkzOGZuNGg3X0tKc21MUTZxcmZR?oc=5) <sub>TradingView</sub>
- 📰 2026-10-29 [Mobileye Releases Third Quarter 2026 Results, Updates Guidance, and Provides Business Overview](https://news.google.com/rss/articles/CBMi4wFBVV95cUxOcTJ2RkYtWl90d1VOWTBqU2pLbmNjbHkwWTZ1UjE5QW9PZ2xpaGVkYWZObTRDQ1dRWHFYRGM3UDBjWGVNLTJMVUtTMWlyOG1heHhnX1BuX0EtQ2pWLXJBeVhaRElhVk1pSXgzendFMHU2X3RqUmpWbE4zYktYbjF4ZlF6RW5NTFZaRGczbkEwS1pidjBFTmh4bVAxeDdJMFM2RHdnV0prSVZyc0RMd29JaWs2eXlsMHNGaThFaUozZXIxaU5TSW9mTGVYVUZ5Wm9zMXNTeTM4cG5KSFJNTVlHaDJUaw?oc=5) <sub>Business Wire</sub>
- 📰 2026-10-29 [Mobileye Q3 Revenue Falls 2% to $492 Million; Adjusted EPS Is $0.11](https://news.google.com/rss/articles/CBMibEFVX3lxTE4yczhEc1RNUzhiSVU4THdjamZndlcxazNRSDlSRjYxRldOVFhwSjZzOTVjRG12MFZ0YWVNMk1oWmdQLUNUU0RsWmhIMjV2LXZXRk83RnlEOTh1S09nMjBNTWtPQnppaFJEM0Ricg?oc=5) <sub>TradingView</sub>
- 📰 2026-10-29 [Mobileye set for record low as earnings fail to revive growth](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE04Tk0xTTJvVnVhM3NmcFM4Vmt3ejhMMmlSa0RQdUZoZkVrTkhDeUd4OXpWRzV2R3pmVDdqWmN3aFpiZDF6Zk0yNXBQMDdTNEFiWXlUZ1AzQmM1SmF5b05abFlWa00zZ0E?oc=5) <sub>CTech</sub>

</details>

<details><summary><b>Aurora</b> (48)</summary>

- 📰 2026-10-30 [Aurora’s Driverless Trucks on Pace for 2027 Expansion Target](https://news.google.com/rss/articles/CBMiqwFBVV95cUxNNU9JbHBiY2l5OGQ5a0ZESkJhYWxyZFlHSW9UWDJhd216VDBpYlJxcldnejIwT3daNl9rU3NtNHVxVEw4WV9MMENlNG84OWoteDNDNDc3elozY2JqdmlRQW9Ua1ZxWkRPUEtTNnFsNUhKam5UOTNJZ2ttQTdEVlo1WDRHTDFOblVmY3FXNXlvdkp4U3RUZWtDSEZ2MjlXMUJQT3M3UDhIRGo5clk?oc=5) <sub>Supply Chain Brain</sub>
- 📰 2026-10-29 [Aurora’s Autonomous Trucks on Track for 2027 After Missing Goals](https://news.google.com/rss/articles/CBMitgFBVV95cUxNdEE4b1hOZGhoT1E2aDRLOWlZZ21XQ2J1WDA0Qkc4bDlkVWVYX2dNMUFLWS1GLXQ2em9GRlJacno0Q3I4NTh2QnlRSlp6eFRUN01uaUF6TnBTLXVtazVfcUNiSGlFQXB0NWR1N215ZXBETWdIZ1pBaDlYaFpuVnB3dHZoVmdaRnpZVmMyc3ZkdXVkc1JhZE9TV3FFRXdnNHM0QzdKQ2plUzNzVWtrZElnd3U2azZRdw?oc=5) <sub>Bloomberg.com</sub>
- 📰 2026-10-29 [Aurora ramping up its driverless truck production](https://news.google.com/rss/articles/CBMifkFVX3lxTE5qNThMcnRlX0tydkllclFneU16QjRZLVVodlFZZ28ydWRFSlBTUmVaX29COGtIMktjUzN0azNaQUx2ZTRYeVh1NGIwWlJUb1V3cDVvWTBCdTY1d25tQWNzdXdaUVp3QXByRW5DTng3cDZ0ZVRXeXhkREZDLTVTZw?oc=5) <sub>Land Line Media</sub>
- 📰 2026-10-29 [Aurora Innovation delays 200-truck goal to February amid supply chain issues](https://news.google.com/rss/articles/CBMipwFBVV95cUxPZnJMZGV1enFlTEdOSkl5Ri02QjdwS003NjZ3UFpNR1JlMm5YYWdLNzdKZTA2SG14NFRqNmJXV1Zlc3dZLUJVeXJmV0ZETThPWHptQ3NscHNzNDNJbHRaVUt0eWtEYXhQQUJ2VnFMWEFKUFpGTlE2eDJGN3R1eDVBbkxrUTR0R25hZkU4LUdISmN0Y0ZwME40ckVTQ0d2R2g2c3FMNEVuNA?oc=5) <sub>The Business Journals</sub>
- 📰 2026-10-29 [Aurora targets 1,000 driverless trucks by end of 2027, 30,000 by 2030](https://news.google.com/rss/articles/CBMitgFBVV95cUxPcFNWYU83Z2d6MWZpTkNod2M5RFJUVTRUdWttSnNTbnpXdXQ4NUd2S1p0TlBwUl9ubTZrZWlTWjdvNzFKNnhUSEx4US1ta1N4VF9RbVJLNGZOZ3FBQ3ZqMVE1UGZDM0R4dVNSU0lySFRwVWdfbGZkVnJudEFWYnB6d3k3d2lQVmQyTDVTbmhBamRJT1YzaHNra3JJNWVhclBPMjhNSzltLWE3LXhQTkU3RmtaekJMUQ?oc=5) <sub>Truck News</sub>

</details>

<details><summary><b>Zoox</b> (61)</summary>

- 📰 2026-10-29 [Waymo's New Ojai Robotaxi Wins on Cabin Space, Loses on Smooth Driving in Las Vegas Test](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBQbzdiZWVJcF9IYnVFdVFEbUFOeWtnQWtueUY4MFdtcWxPb1pkN1RqYXlib05PNklzRVZKNF9Sdl9EeGd4b3lpMl82ejdvbjhCeGUtMXhlRWpGUFk?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-29 [Amazon Q3 Sales Rise 12% as Operating Income Reaches $28.1 Billion](https://news.google.com/rss/articles/CBMixAFBVV95cUxOZVNPZGtQU0ZNS09nV2Q1ME1wMmM3QW9Yc25pSVI1dkRjeFoyVC1VYlRKeUwwQ29oQm5BU3QtMFp6Si1FMTFpeU44aGo3dC1ob2VQbUN5Mkh2Y24yZnV2c0RaaVFpVnFSa2tUZzNYMGFXRXY1QVk3eGFlMmpkYzBVdUVkUDhJajlOeTYyak95UEtMZ3N3UEhaRG1pTFVpQ1lBdDFBOGFKeVNKM09Wb1gzcDhZczYzNmtiLXNQSUhFZTFZMnNJ?oc=5) <sub>TradingView</sub>
- 📰 2026-10-29 [Amazon Q3 earnings, revenue miss; AWS net sales soar](https://news.google.com/rss/articles/CBMiggFBVV95cUxPMnBTa3VJdDJnOV9VZURoVHptYW1NREFfMW9sRDhNQ2pJWXEyLUxxRnpwM2FnaksweUd5VHNFZzdHVGYxVE9mQnMweUN3eDlrSDg3QzNfdmliTTNYczh1VHdmT3NScDVmY0t6cnhhWTNXZUgzSVN6dTI0akkxcmQyek93?oc=5) <sub>Chain Store Age</sub>
- 📰 2026-10-28 [Nevada caught between AI job growth and job losses](https://news.google.com/rss/articles/CBMiggFBVV95cUxQTVF1SXJGdUFXOTE0REU0QU95Zm44ckxxMzRZSXVPakNTQkFFcjVKMHUtcWdSODFzeTRST2U3SHZWRWxSUjJGUUVRdUoxLUVNWHRKUFlxUktKOUhGdGo2SjM5VVJPUk5LbXNjcW5QbGcwM3diaDV0c05OV3BQS1hwSjJB?oc=5) <sub>Reuters</sub>
- 📰 2026-10-28 [As Waymo expands overseas, it remains a niche cash-burning business](https://news.google.com/rss/articles/CBMipgFBVV95cUxNcnFOal9qb29IdlNMWEd0c3I0ZDM3aXBxLTQyYW41ZFlMTnpQLTNadzdQX0p0RnBOLUR5MUFxQUFjRzlPU1pBQW5RZjVwWG52MjNVZFFDUTBwVTlVcU1yYjRxdUtwbVNqM0pWMXBZOG90ekJNSmJ6ckpJam9sZ1dzRUE5SUo4OUsyYlRBSG1BQ0xoRDlhcTFLNUt0a3pFT0lZeHllOERR0gGrAUFVX3lxTFBnV2JPdjVVQkhmSVJVN3ZyRjNjZk95NHZCandZR0FMQTlCbkhHRy1HLXRZMVAxTGNYMU40QUNBSHYxOXZHRzlIRE42VWI5eG1TMlJlOWpEM3pOb3g0UDJUMGVYWVR6cGZUUHV2cUUtQmszSG1yM1JINnc1c2w5NEhwWFp1VC1ITWczUzJPa3U1MVZHNVJad3VYX1Q2MGs1UGE5QjBFcXR2Vl9IZw?oc=5) <sub>CNBC</sub>

</details>

<details><summary><b>Motional</b> (15)</summary>

- 📰 2026-10-29 [Hesai Leads Global Robotaxi Lidar Market with 62% Share as Robotaxi Industry Moves Toward Scale, Yole Group Reports](https://news.google.com/rss/articles/CBMi8gFBVV95cUxQaE40Ym5SMXFZYWhRM3FYYzUxbzI0Yk5tTExfWVpsMW1mTkdRLTNpdVJPQkR6NzJub2hFaFZ2TWJlc2VWdEVlZC1ZWThOb0U0aV9pblFOSmZNQ2t6bVNjRnoxeVZnMVRVTnpZNkgtTXZyM09nMmNUb25VVlBpR1ZGeEtIWGlSUWhJMFBCUC01dDh3R3JLOGxDNEpacEMwRWZoNmEySU03emlOTENXbDhMS0ctSFVRaXJRZ0RPOHFKdlVucTM4THc4YnhCR09LV1FpSnBEcVRneEI3d1hwdlFieGIzaV8yaTY4LWMwTzNIc0Rrdw?oc=5) <sub>Thailand Business News</sub>
- 📰 2026-10-28 [Hyundai Motor Rises to No. 29 in Interbrand’s Best Global Brands 2026 Ranking](https://news.google.com/rss/articles/CBMirgFBVV95cUxOYW13NmJqeUZhQ1A1UnJOYjB6NUdRZU9uOHdFRVR6Um42WFlSZmdOOXV2WnJqVUdJVUw0eXVPSTMxdWlNRnMySXJ6N2dhd0pIYXBpWXU2cDdZRlZNWGhhWWVLcDdnV05kMVd4cGtiYUkzNnRPTVN2UW82cmdSdHNfZy1KMlktRlZWMF9TdWNLSDlZeWJZcWtscG5ZVWg2T2ZMY09NNFNDOGlPUkw3SVE?oc=5) <sub>Indian Television Dot Com</sub>
- 📰 2026-10-28 [Hyundai Motor Rises To No. 29 In Interbrand Global Brand Ranking](https://news.google.com/rss/articles/CBMiqwFBVV95cUxPWlRYZlVKTzNZWmdfWXpGUmxJd2ZKQ1pnX1otaXB4XzgycnY0NmZkUXFsSGFZQlRKbFJWRkFwWmIzWEF6X0IzRjh3Z09YYkxGRm1nbURLQU05R3pnN3ZLcHVfMHRRNm85T3hXeUR5Mklha19vZ2QxUmdiNE4xTUxaaV9Nd3hLQk9Nc1ZTY1lxbmR2Z3RxSXQ5RlRnb2RLTmowMkVaZzRIZUdGZDDSAasBQVVfeXFMT1pUWGZVSk8zWVpnX1l6RlJsSXdmSkNaZ19aLWlweF84MnJ2NDZmZFFxbEhhWUJUSmxSVkZBcFpiM1hBel9CM0Y4d2dPWGJMRkZtZ21ES0FNOUd6Zzd2S3B1XzB0UTZvOU94V3lEeTJJYWtfb2dkMVJnYjROMU1MWmlfTXd4S0JPTXNWU2NZcW5kdmd0cUl0OUZUZ29kS05qMDJFWmc0SGVHRmQw?oc=5) <sub>Autocar Professional</sub>
- 📰 2026-10-28 [Waymo Beats Uber by $10 at Nashville Airport, but Loses on the Highway, Field Report Finds](https://news.google.com/rss/articles/CBMiW0FVX3lxTFAzS3V3bDhOWnRqTmhzRzVNQWx1MlBhV0psZ2lwZEU0TEdoazhtMXZ0Tm9jbUlId2p0TV9EX3FiUmtmZXNPaGdkS3dGY2ZlNEc5cks3WGNUSGxFVnM?oc=5) <sub>BigGo Finance</sub>
- 📰 2026-10-28 [Waymo Nashville Airport Field Report｜Road to Autonomy](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5DTDlkRWVqN1hmbndLVTU0RGZOLXhLWjRabFVIc01jb3R0eGRUNDBOZ0pzdzJLbGRSelpydjF5TXVMc0UwNnB3OTZCN05iV0stdzBGWTJ1R0s2WjdyZEE0?oc=5) <sub>finance.biggo.com</sub>

</details>

<details><summary><b>comma.ai</b> (9)</summary>

- 📝 2026-10-23 [openpilot 0.11.2](https://blog.comma.ai/0112release/) <sub>official blog</sub>
- 📰 2026-10-29 [A $1,000 Device Enables Hands-Free Driving. But Fatal Crashes Have Prompted Scrutiny.](https://news.google.com/rss/articles/CBMixAFBVV95cUxObnRHUXNNS2wxNVFWeHVLdm9qYmZ1bnpaUVN2VWJ1eHZhbFRiWGxoVWxaSjNuNzNKQXZ0RV80dVRnckFGc003eXZJeW5ZWkhUakpsdk9sQ0lnQUZZeVNGekRzYmhvR2RrU1Ric29JeUFmQzNNdEE5NEtZLUgyS2hmQ1hwYWlMdFNDRHNZQVB6dHNqUjIyaXpRMFd2c0YxN0c3Vk9yZF9kR255QmtTUlRiaEtYbDY1dHVZQm9ReHY5WUdMSzJQ?oc=5) <sub>WSJ</sub>
- 📰 2026-10-29 [We Upgrade Our comma three to a comma four: Is It Worth It?](https://news.google.com/rss/articles/CBMimwFBVV95cUxOVkgtNU9hLXVYM0U2VjNpVldsNFFoQm53SjJGcU1CcnNMWXY5YzFYdVhoYlNZdG5vX21Va2h4b2RLYTNEUTBLdUFhMXd5eTVjLXBSTHE5bFN6elNqa1diTThPQ0Z0Mlo4SldDTzQ4eGxEWl9NTjNKcUNGQmhLeGRSMUxOSElpMkVNOTN4QWhMV0hPRFFJV3cyeVNLSQ?oc=5) <sub>Transport Evolved</sub>
- 📰 2026-10-29 [Aftermarket Self-Driving Devices Face Federal Investigation Following Five Crashes, Three Deaths](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPUG8ycGN4Tl96dk4xZk1yTEJrVkpvVGNsX2JnbWJoeXlzS1ZsVDlEYWk0SnFQQTZXQXpfN21BU20wR1FmR1lsUFpoeHdzU1BUaGdheTZ3LUFkVnpaOHhyWUU0YU1yWERQYmI2TDRnd1VpbTM3Ui1yWFdQVzZIRHVrUEhZUFBKcGpM?oc=5) <sub>AOL.com</sub>
- 📰 2026-10-21 [Is the race to build self-driving AI turning into a cyberwar?](https://news.google.com/rss/articles/CBMikAFBVV95cUxPd1ljS1V3ZmI4RGdJZkRQdVpkNmRqcm5tVUtpRllXYWMyQ2ZnaFFKRzgzY0VaUDNTR3VwYV9lRHI2RnRUcV9za0p3bTNsMGJmSHNZUlR0MDFsYm1FLTVtUEl1UEJhSi1hXzMtc05tendPaDltRzlMczQwRkx0dTZJaGVjTk1DOXp1cVpSS2Zqc0w?oc=5) <sub>Yahoo Tech</sub>

</details>

---

<sub>Generated by [`scripts/run.py`](scripts/run.py). Scores and summaries are automated and may contain mistakes; PRs to [`config.yaml`](config.yaml) `curation.include/exclude` are welcome.</sub>
