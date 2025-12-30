
# GAN-model-for-Anomaly-Detection

> **Generative AI–enhanced, real-time anomaly detection for Integrated Energy Systems (IES) at the grid edge, using WGAN‑GP + LSTM to forecast system response and flag cyber anomalies via reconstruction‑error + discriminator‑score fusion.** 

[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Generative%20AI-WGAN--GP%20%2B%20LSTM-orange.svg)](#)
[![Data](https://img.shields.io/badge/Data-PSS%C2%AEE%20%2B%20IEEE%20118--bus-lightgrey.svg)](#)
[![Status](https://img.shields.io/badge/status-research--code-brightgreen.svg)](#)

---

## Overview

Modern IES blend renewables (solar, wind), batteries, clean fuels, and thermal demand—boosting efficiency and resilience while enlarging the cyber‑attack surface at the **grid–IES interface**. Labeled attack data is scarce, so this project uses **generative models** trained on **simulation‑based time‑series** to learn “normal” behavior and flag deviations **in real time**. The implementation combines a **Wasserstein GAN with Gradient Penalty (WGAN‑GP)** with **LSTM** temporal modeling; the generator’s **reconstruction error** and the discriminator’s **probability score** are fused to produce an anomaly likelihood over **sliding latent windows**. 

> **Paper**: *Generative AI‑Enhanced Real‑Time Anomaly Detection in Integrated Energy Systems*, IEEE Transactions on Smart Grid (2026).  

> **GitHub repository**: https://github.com/UTD-DOES/GAN-model-for-Anomaly-Detection  

---

## Key Features

- **WGAN‑GP + LSTM architecture** for stable adversarial training and long‑range temporal dependencies in non‑stationary IES signals. 
- **Dual‑metric scoring**: fuse **discriminator probability** with **generator reconstruction error** for robust unsupervised detection per sliding window. 
- **Simulation‑driven data** from **PSS®E** dynamic models of IES connected to the **IEEE 118‑bus** network (faults, outages, trips, and diverse cyberattack patterns). 
- **Ready for real‑time monitoring**: deploy the **pre‑trained discriminator** to score incoming signals; thresholds tune sensitivity vs. false alarms. 

---

## Installation

This repo is primarily **Jupyter Notebook** driven with supporting **Python** utilities. Set up a clean environment:

```bash
# Python >= 3.9 recommended
python -m venv .venv
source .venv/bin/activate   # (Windows) .venv\Scripts\activate

pip install --upgrade pip
pip install jupyter numpy scipy pandas matplotlib torch torchvision torchaudio scikit-learn
```

---

## Data

- Place your simulation‑generated time series (e.g., bus voltages, frequency, power flows) under **`Dataset/`**.  
- The paper’s dataset was produced with **PSS®E** on IES connected to **IEEE 118‑bus**, covering faults/outages/trips and multiple cyberattack patterns (shift, variance manipulation, oscillation enhancement, blending, injection, noise, partial spoofing). 

If you intend to reproduce the paper’s results, generate a comparable dataset via PSS®E (nonlinear, time‑domain simulations) or adapt field data after appropriate normalization and windowing. 

---

## Quick Start (Notebooks)

### 1) Launch Jupyter

```bash
jupyter lab   # or: jupyter notebook
```

### 2) Open training notebook

Open a notebook in **`GAN Model/`** (e.g., `train_wgangp_lstm.ipynb`). Configure:

- **GAN hyperparams**: learning rate (≈1e‑4), batch size (≈40), noise length (≈100), epochs (≈35). 
- **Windowing**: latent sliding window size and variance‑adaptive logic.
- **Paths**: point to datasets in `Dataset/`.

Run all cells to train the **WGAN‑GP + LSTM** model. Monitor generator/discriminator losses and convergence stability (thanks to Wasserstein loss + gradient penalty). 

### 3) Open inference notebook

Use an inference notebook (e.g., `score_stream.ipynb`) to score **incoming signals**:

- Compute **discriminator probability** + **generator reconstruction error** per window.  
- Fuse them into an **anomaly likelihood** and compare to a **threshold**.

> As shown in the paper’s sensitivity study, lowering the detection threshold increases detection of fake samples from **12% (τ=0.7)** to **93% (τ=0.1)**, at the cost of more false alarms. Tune for your operational needs. 

---


## Method Details

1. **Adaptive latent time window**: window length τ(t) scales inversely with short‑term signal variance to capture appropriate context without overfitting. 
2. **Encoder → LSTM Generator**: reconstructs expected signal; **reconstruction error** (ℓ2) quantifies deviation from learned normal patterns. 
3. **WGAN‑GP Discriminator**: outputs a **Wasserstein‑based score**; gradient penalty enforces 1‑Lipschitz continuity for stable training. 
4. **Fusion score & thresholding**: combine both metrics to yield anomaly likelihood; alert when threshold exceeded (tunable to balance sensitivity/false alarms). 

---


## Reproducibility & Hardware

- **Optimizer**: **RMSprop**, selected for non‑stationary objectives and sparse gradients common in coupled thermal‑electrical dynamics. 
- **Hardware**: Efficient on CPU; paper experiments used **Intel® Xeon® E5‑2603 v3 (12 cores)**. GPU is optional. 

---

## Citation

If you use this repository or build upon its method, please cite:

```text
S. Badakhshan, J. Zhang,
"Generative AI‑Enhanced Real‑Time Anomaly Detection in Integrated Energy Systems,"
IEEE Transactions on Smart Grid, 2026.
```

---

## Contributing

Pull requests are welcome! Please:

- Keep notebooks **reproducible** (seeded randomness, explicit data paths).
- Add unit tests for new Python utilities.
- Consider adding `CONTRIBUTING.md`, issue templates, and a security policy to meet GitHub community standards. 

---

## Links

- **GitHub**: https://github.com/UTD-DOES/GAN-model-for-Anomaly-Detection 
- **IEEE Xplore Abstract (if accessible)**: https://ieeexplore.ieee.org/abstract/document/11232457 

---

## FAQ

**Q1. Do I need labeled attack data?**  \
No. The approach is **unsupervised**: trained on normal (or simulation‑generated) behavior; anomalies are flagged by deviation from learned patterns via reconstruction error + discriminator score. 

**Q2. Can I run this on CPU only?**  \
Yes. The paper reports CPU‑only experiments; GPUs can accelerate training but are not mandatory. 

**Q3. How do I choose the detection threshold?**  \
Use validation signals to calibrate; lower thresholds increase sensitivity (and false alarms), higher thresholds reduce both. The paper’s sensitivity analysis provides guidance. 

