# Our work (v10, Swiss Dwellings) vs base paper (Pham et al., Cluster Computing 2026, 29:687)

Lower is better for F, overlap, realism, FID, KID. Higher is better for connections met.

## Phase 1: optimization (F_fixed = Paper-2 fitness + true overlap penalty)

| Step | F_fixed | Overlap | Connections met | Realism |
|---|---|---|---|---|
| Base paper as published (Plan-VAE, Paper-2 fitness, GA 50x20) | 42.19 | 0.804 | 0.959 | 7.99 |
| + corrected fitness (true overlap, touching connections) | 3.80 | 0.022 | 0.688 | 2.78 |
| + graph-conditioned Plan-VAE | 3.08 | 0.022 | 0.787 | 2.85 |
| + tuned CMA-ES, 1,000 evaluations | 2.50 | 0.014 | 0.807 | 3.00 |
| tuned CMA-ES, 3,000 evaluations | 1.69 | 0.006 | 0.912 | 3.04 |
| reference: tuned CMA-ES, bounded raw space, 3,000 evaluations | 0.71 | 0.001 | 0.959 | 3.94 |
| reference: human-designed plans | 5.57 | 0.089 | 0.641 | 2.47 |

## Phase 2: rendering quality (128 px, FID/KID against 4,600 real held-out plans)

| Images | FID | KID |
|---|---|---|
| Real against real (lower bound, n=4600) | 5.98 | 0.0004 |
| Human layouts -> our DiT renderer (n=4600) | 32.59 | 0.0326 |
| Optimized layouts -> our DiT (n=600), best: GVAE + DE | 93.68 | 0.1025 |
| Optimized layouts -> our DiT (n=600), range over methods | 93.68 - 105.27 | 0.1025 - 0.1171 |
| Base-paper replica (Plan-VAE + GA, Paper-2 fitness) -> DiT | 180.39 | 0.2255 |
| Human layouts -> Pix2Pix (Paper 1 renderer) | 212.92 | 0.2712 |
| Optimized layouts -> Pix2Pix, range over methods | 218.02 - 228.04 | 0.2596 - 0.2768 |
| Paper-1-style pipeline (GA + VAE + Pix2Pix) | 309.26 | 0.3927 |

## Verdict

| Point | Base paper | Ours | Better? |
|---|---|---|---|
| Overlap of optimized layouts | 0.804 (our replica) | 0.006 - 0.022 | Yes |
| F_fixed | 42.19 (our replica) | 0.71 - 1.69 | Yes |
| Beats human-designed plans | claims 24.43% on its own delta-F | F_fixed 1.69 vs 5.57, with overlap checked | Yes |
| Statistical rigor | one GA comparison | 40 sites x 15 seeds, tuned optimizers, Wilcoxon + Holm | Yes |
| DiT against GAN | claimed | DiT FID ~94-103 vs Pix2Pix ~213-228 | Confirmed |
| "Latent space beats raw space" | claimed | true only at low budget (<= ~1,000-3,000 evals); at 10,000 raw is equal or better | Not confirmed |
| FID | 1.4873 | 32.59 (human layouts), ~94-103 (optimized) | No (not directly comparable: dataset, image size, test set differ) |

Caveats: the paper's own numbers were not reproduced on its data. All "base paper" rows are our replica on Swiss Dwellings. The DiT was trained for only 40 epochs at 128 px (the `full` preset is 80 epochs).
