# awesome-papers

## useful website

* Arxiv-CS-RAG: [https://huggingface.co/spaces/bishmoy/Arxiv-CS-RAG](https://huggingface.co/spaces/bishmoy/Arxiv-CS-RAG)
* Papes.cool:
  * [https://papers.cool/arxiv/cs.LG](https://papers.cool/arxiv/cs.LG): Machine Learning
  * [https://papers.cool/arxiv/cs.DC](https://papers.cool/arxiv/cs.DC): Distributed, Parallel, and Cluster Computing
  * [https://papers.cool/arxiv/cs.OS](https://papers.cool/arxiv/cs.OS): Operating Systems
  * [https://papers.cool/arxiv/cs.CL](https://papers.cool/arxiv/cs.CL): Computation and Language
* Find Related Papers
  * Connect Papers: [https://www.connectedpapers.com/](https://www.connectedpapers.com)
  * Sematic Scholar: [https://www.semanticscholar.org/](https://www.semanticscholar.org)

## awesome papers
<!-- -------------------------------------------------------------------------- Template (DE NOT DELETE) -----------------------------------------------------------------------------
[Template] * (conf/trans/arxiv) Paper title [link](http_source_link) [NOTE: key words / author / affiliation]
[Examples] * (NIPS'17) Attention Is All You Need [link](https://arxiv.org/abs/1706.03762) [Attention | Google]
[Examples] * (Arxiv'24) Optimal Block-Level Draft Verification for Accelerating Speculative Decoding [link](https://arxiv.org/abs/2403.10444) [Speculative Decoding | Google]
------------------------------------------------------------------------------- Template (DE NOT DELETE) ----------------------------------------------------------------------------- -->

---
## TODO list
* SC'24
* ICML'24
* SOSP'23
* PPoPP'24
* SIGCOMM'24

---
## [arxiv papers]
* NanoFlow: Towards Optimal Large Language Model Serving Throughput [2408.12757](https://arxiv.org/abs/2408.12757) [github](https://github.com/efeslab/Nanoflow)
* Efficient LLM Scheduling by Learning to Rank [2408.15792](http://www.arxiv.org/abs/2408.15792) [Hao-ai-lab]
* DSP: Dynamic Sequence Parallelism for Multi-Dimensional Transformers [2403.10266](https://arxiv.org/abs/2403.10266)
* [ICML'24] Quest: Query-Aware Sparsity for Efficient Long-Context LLM Inference [2406.10774](https://arxiv.org/abs/2406.10774) [github](https://github.com/mit-han-lab/Quest)
* [COLM'24] Keep the Cost Down: A Review on Methods to Optimize LLM's KV-Cache Consumption [paper](https://openreview.net/forum?id=8tKjqqMM5z#discussion)
* Slice-Level Scheduling for High Throughput and Load Balanced LLM Serving [2406.13511](https://arxiv.org/abs/2406.13511)
* LoongServe: Efficiently Serving Long-context Large Language Models with Elastic Sequence Parallelism [2404.09526](https://arxiv.org/abs/2404.09526)


---
## [HPCA 2024](https://ieeexplore.ieee.org/document/10476401)
* Smart-Infinity: Fast **Large Language Model Training** using Near-Storage Processing on a Real System
* ASADI: Accelerating **Sparse Attention** Using Diagonal-based In-Situ Computing
* Tessel: Boosting **Distributed Execution** of Large DNN Models via **Flexible Schedule Search**
* Enabling Large Dynamic **Neural Network Training** with Learning-based **Memory Management**
* LibPreemptible: Enabling Fast, Adaptive, and Hardware-Assisted User-Space Scheduling
* TinyTS: Memory-Efficient **TinyML Model Compiler** Framework on Microcontrollers
* GPU Scale-Model Simulation


---
## [SOSP 2024](https://sigops.org/s/conferences/sosp/2024/accepted.html)
### ML Inference
* LoongServe: Efficiently Serving **Long-Context Large Language Models** with Elastic Sequence Parallelism
* PowerInfer: Fast **Large Language Model Serving** with a **Consumer-grade GPU**
* Apparate: Rethinking **Early Exits** to Tame Latency-Throughput Tensions in **ML Serving**
* Improving **DNN Inference Throughput** Using Practical, Per-Input Compute Adaptation
### ML Training
* Enabling Parallelism **Hot Switching** for Efficient **Training of Large Language Models**
* Reducing Energy Bloat in **Large Model Training**
* ReCycle: Pipeline Adaptation for the Resilient Distributed **Training of Large DNNs**
### Other
* Tenplex: Dynamic Parallelism for Deep Learning using Parallelizable Tensor Collections
* Scaling Deep Learning Computation over the Inter-Core Connected Intelligence Processor with T10
* Uncovering Nested Data Parallelism and Data Reuse in DNN Computation with FractalTensor


---
## [ATC 2024](https://www.usenix.org/conference/atc24/technical-sessions)
### ML Inference
* Power-aware Deep Learning Model Serving with μ-Serve
* Cost-Efficient Large Language Model Serving for Multi-turn Conversations with CachedAttention
* PUZZLE: Efficiently Aligning Large Language Models through Light-Weight Context Switch
* Quant-LLM: Accelerating the Serving of Large Language Models via FP6-Centric Algorithm-System Co-Design on Modern GPUs
## ML Training
* Accelerating the Training of Large Language Models using Efficient Activation Rematerialization and Optimal Hybrid Parallelism
* Metis: Fast Automatic Distributed Training on Heterogeneous GPUs
* FwdLLM: Efficient Federated Finetuning of Large Language Models with Perturbed Inferences


---
## [EuroSys 2024](https://dl.acm.org/doi/proceedings/10.1145/3627703)
* Aceso: Efficient Parallel DNN Training through Iterative Bottleneck Alleviation
* Model Selection for Latency-Critical Inference Serving
* Optimus: Warming Serverless ML Inference via Inter-Function Model Transformation
* CDMPP: A Device-Model Agnostic Framework for Latency Prediction of Tensor Programs
* Orion: Interference-aware, Fine-grained GPU Sharing for ML Applications
* HAP: SPMD DNN Training on Heterogeneous GPU Clusters with Automated Program Synthesis
* Blox: A Modular Toolkit for Deep Learning Schedulers
* DynaPipe: Optimizing Multi-task Training through Dynamic Pipelines
* GMorph: Accelerating Multi-DNN Inference via Model Fusion
* ScheMoE: An Extensible Mixture-of-Experts Distributed Training System with Tasks Scheduling
* ZKML: An Optimizing System for ML Inference in Zero-Knowledge Proofs


---
## [ASPLOS 2024](https://dl.acm.org/doi/proceedings/10.1145/3620666)
* 8-bit Transformer Inference and Fine-tuning for Edge Accelerators
* AdaPipe: Optimizing Pipeline Parallelism with Adaptive Recomputation and Partitioning
* Centauri: Enabling Efficient Scheduling for Communication-Computation Overlap in Large Model Training via Communication Partitioning
* Characterizing Power Management Opportunities for LLMs in the Cloud
* FaaSMem: Improving Memory Efficiency of Serverless Computing with Memory Pool Architecture
* Fractal: Joint Multi-Level Sparse Pattern Tuning of Accuracy and Performance for DNN Pruning
* FUYAO: DPU-enabled Direct Data Transfer for Serverless Computing
* NeuPIMs: NPU-PIM Heterogeneous Acceleration for Batched LLM Inferencing
* PrimePar: Efficient Spatial-temporal Tensor Partitioning for Large Transformer Model Training
* SpecInfer: Accelerating Large Language Model Serving with Tree-based Speculative Inference and Verification
* SpecPIM: Accelerating Speculative Inference on PIM-Enabled System via Architecture-Dataflow Co-Exploration


---
## [OSDI 2024](https://www.usenix.org/conference/osdi24)

### LLM Serving 
* Taming Throughput-Latency Tradeoff in LLM Inference with Sarathi-Serve [link](https://arxiv.org/abs/2403.02310) []
* DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving [link](https://arxiv.org/pdf/2401.09670.pdf) [PKU]
* Fairness in Serving Large Language Models [link](https://arxiv.org/abs/2401.00588)[Ion Stoica]
* ServerlessLLM: Locality-Enhanced Serverless Inference for Large Language Models [link]([https://arxiv.org/abs/2401.00588](https://arxiv.org/abs/2401.14351))[Serveless]
* InfiniGen: Efficient Generative Inference of Large Language Models with Dynamic KV Cache Management
* Llumnix: Dynamic Scheduling for Large Language Model Serving
### ML Scheduling
* Parrot: Efficient Serving of LLM-based Applications with Semantic Variable
* USHER: Holistic Interference Avoidance for Resource Optimized ML Inference
* Fairness in Serving Large Language Models
* MonoNN: Enabling a New Monolithic Optimization Space for Neural Network Inference Tasks on Modern GPU-Centric Architectures
* MAST: Global Scheduling of ML Training across Geo-Distributed Datacenters at Hyperscale


---
## [NSDI 2024](https://)

* to be updated
* (NSDI'24) MegaScale: Scaling Large Language Model Training to More Than 10,000 GPUs [link](https://arxiv.org/abs/2402.15627) [Training|Bytedance]
* (NSDI'24) DISTMM: Accelerating Distributed Multimodal Model Training [link](https://www.amazon.science/publications/distmm-accelerating-distributed-multimodal-model-training) [multi-model|Amazon]
* (NSDI'24) Approximate Caching for Efficiently Serving Text-to-Image Diffusion Models [link](https://arxiv.org/abs/2312.04429#:~:text=In%20this%20paper%2C%20we%20introduce,image%20generation%20for%20similar%20prompts.) []
* (NSDI'24) Swing: Short-cutting Rings for Higher Bandwidth Allreduce [link](https://arxiv.org/abs/2401.09356) [Allreduce]
* (NSDI'24) Vulcan: Automatic Query Planning for Live ML Analytics [link](https://yiwenzhang92.github.io/assets/docs/vulcan-nsdi24.pdf) [Planning]
* (NSDI'24) CASSINI: Network-Aware Job Scheduling in Machine Learning Clusters [link](https://arxiv.org/abs/2308.00852) [Communication]
* (NSDI'24) Towards Domain-Specific Network Transport for Distributed DNN Training [link](https://arxiv.org/abs/2008.08445) [Training | DNN]


---
## [MLSys 2024](https://mlsys.org/virtual/2024/papers.html?filter=titles)

* [Accepted Papers](https://mlsys.org/Conferences/2024/AcceptedPapers)

#### LLM - serving
* (MLSys'24) HeteGen: Efficient Heterogeneous Parallel Inference for Large Language Models on Resource-Constrained Devices [paper](https://arxiv.org/abs/2403.01164) [**Inference** | **Parallelism** | NUS]
* (MLSys'24) FlashDecoding++: Faster Large Language Model Inference with Asynchronization, Flat GEMM Optimization, and Heuristics [paper](https://arxiv.org/abs/2311.01282) [**Inference** | Tsinghua | SJTU]
* (MLSys'24) VIDUR: A LARGE-SCALE SIMULATION FRAMEWORK FOR LLM INFERENCE [-]() [**Inference** | **Simulation Framework** | Microsoft]
* (MLSys'24) UniDM: A Unified Framework for Data Manipulation with Large Language Models [paper](https://arxiv.org/abs/2402.03009) [**Inference** | **Memory** | **Long Context** | Alibaba]
* (MLSys'24) SiDA: Sparsity-Inspired Data-Aware Serving for Efficient and Scalable Large Mixture-of-Experts Models [paper](https://arxiv.org/abs/2310.18859) [**Serving** | **MoE**]
* (MLSys'24) Keyformer: KV Cache reduction through key tokens selection for Efficient Generative Inference [paper](https://arxiv.org/abs/2403.09054) [**Inference** | **KV Cache**]
* (MLSys'24) Q-Hitter: A Better Token Oracle for Efficient LLM Inference via Sparse-Quantized KV Cache [paper](https://arxiv.org/abs/2306.14048) [**Inference** | **KV Cache**]
* (MLSys'24) Prompt Cache: Modular Attention Reuse for Low-Latency Inference [paper](https://arxiv.org/abs/2311.04934) [**Inference** | **KV Cache** | Yale]
* (MLSys'24) SLoRA: Scalable Serving of Thousands of LoRA Adapters [paper](https://arxiv.org/abs/2311.03285) [code](https://github.com/S-LoRA/S-LoRA) [**Serving** | **LoRA** | Stanford | Berkerley]
* (MLSys'24) Punica: Multi-Tenant LoRA Serving [paper](https://arxiv.org/abs/2310.18547) [code](https://github.com/punica-ai/punica) [**Serving** | **LoRA** | Tianqi Chen]

#### LLM - training and quantization
* (MLSys'24) AWQ: Activation-aware Weight Quantization for On-Device LLM Compression and Acceleration [paper](https://arxiv.org/abs/2306.00978) [code](https://github.com/mit-han-lab/llm-awq) [**Quantization** | MIT]
* (MLSys'24) Efficient Post-training Quantization with FP8 Formats [paper](https://arxiv.org/abs/2309.14592) [**Quantization** | Intel]
* (MLSys'24) Does Compressing Activations Help Model Parallel Training? [paper](https://arxiv.org/abs/2301.02654) [**Quantization**]
* (MLSys'24) Atom: Low-Bit Quantization for Efficient and Accurate LLM Serving [paper](https://arxiv.org/abs/2310.19102) [code](https://github.com/efeslab/Atom) [**Quantization** | **Serving** | SJTU | CMU]
* (MLSys'24) QMoE: Sub-1-Bit Compression of Trillion Parameter Models [paper](https://arxiv.org/abs/2310.16795) [code](https://github.com/IST-DASLab/qmoe) [**Quantization** | **MoE** | Google]
* (MLSys'24) Lancet: Accelerating Mixture-of-Experts Training by Overlapping Weight Gradient Computation and All-to-All Communication [-]() [**Training** | **MoE** | HKU]
* (MLSys'24) DiffusionPipe: Training Large Diffusion Models with Efficient Pipelines [-]() [**Training** | **Diffusion** | HKU]

#### ML Serving
* (MLSys'24) FLASH: Fast Model Adaptation in ML-Centric Cloud Platforms [paper](https://haoran-qiu.com/publication/mlsys-2024/) [code](https://gitlab.engr.illinois.edu/DEPEND/flash) [MLsys | UIUC]
* (MLSys'24) ACROBAT: Optimizing Auto-batching of Dynamic Deep Learning at Compile Time [paper](https://arxiv.org/abs/2305.10611) [**Compiling** | **Batching** | CMU]
* (MLSys'24) On Latency Predictors for Neural Architecture Search [paper](https://arxiv.org/abs/2403.02446) [Google]
* (MLSys'24) vMCU: Coordinated Memory Management and Kernel Optimization for DNN Inference on MCUs [paper](https://arxiv.org/abs/2001.03288) [**DNN Inference** | PKU]















