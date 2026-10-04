# Problem Statement (working draft v1)

**Working title:** Controllable Latent-Space Metaheuristic Optimization for Boundary-Aware Early-Stage Floor Plan Layout

Basis: Pham et al. 2025 (GA+VAE+Pix2Pix), Pham et al. 2026 (GA+Plan-VAE+DiT), and our own ResPlan GA-vs-PSO notebook (`final_comparitively_study.ipynb`).

---

## 1. Background (3 lines)

Hybrid pipelines search the latent space of a layout VAE with a metaheuristic, then render the best layout with a generative model. The premise is that the latent space is a *navigable, constraint-friendly manifold*, so search there beats search in raw coordinates.

## 2. Evidence that the premise is not yet established

| # | Observation | Source |
|---|---|---|
| E1 | Our Plan-VAE v3 reconstructs almost equally well from `encoded_mu`, `zero_z` and `random_z` (centroid error 0.335 / 0.340 / 0.342). The decoder barely uses z. | Notebook Step 12H |
| E2 | Mean centroid reconstruction error is 0.32 (normalized), about one third of the canvas. | Notebook Step 12H |
| E3 | GA and PSO improve the initial population by only 3.9% and 5.8%. PSO beats GA by 2.05% (60/60 cases). | Notebook Steps 17A-17C |
| E4 | About 80% of the fitness is the centroid-distance adjacency term. `L_ratio` is always 0 (inactive). | Notebook Steps 17C-17D |
| E5 | Both optimizers reach their best at about 970-990 of 1000 evaluations, so they have not converged. | Notebook Step 17C |
| E6 | Published fitness uses centroid distance and square proxies; the authors state this misrepresents adjacency and overlap. Reported gains are measured with the same fitness that is optimized. | Paper 2, Sec 6.4 |
| E7 | Latent GA gain degrades for 20-26 rooms (-6.2%). | Paper 2, Table 7 |

E1-E2 must be re-verified (different seeds, KL setting, held-out set) before they are claimed in a paper.

## 3. Problem statement

Existing latent-space layout optimizers assume, but never verify, that (a) the latent space is **controllable** (changing z meaningfully and smoothly changes the layout), and (b) the optimized objective is a **faithful proxy** of architectural quality. When the decoder under-uses z and the fitness is a centroid-distance proxy, metaheuristics have little leverage, and reported gains (about 2% between optimizers, about 4-6% from initialization) are small, non-independently measured, and not shown to transfer to real layout quality.

**We address:** how to build a latent space and a polygon-aware, multi-objective fitness such that metaheuristic search yields *measurable, independently validated* improvements in boundary-constrained residential layouts, and how the choice of optimizer matters once that holds.

## 4. Formalization

- Layout: `L = {(t_i, c_i, s_i)}_{i=1..N}` (type, centroid, equivalent side), optionally with polygons `P_i` and a fixed boundary `B`.
- Decoder `D_theta: z in R^d -> L`. Controllability measure: `C(D) = E_z,delta [ d_layout(D(z), D(z+delta)) / ||delta|| ]`, plus a collapse check `d(D(z), D(0))` against `d(D(mu(x)), x)`.
- Objectives (vector, not scalar): `F(L) = [ f_adj(P, A), f_area(P, target), f_overlap(P), f_boundary(P, B), f_daylight(P, windows) ]` computed on polygons.
- Search: `z* = argmin_z F(D(z))` (Pareto set if multi-objective) under budget `E` evaluations.
- Independent evaluation: `Q(L)` = metrics not used in `F` (for example walkable path length via door graph, polygon IoU with real plans, expert rating).

## 5. Research questions and hypotheses

- **RQ1 (controllability).** Does a controllable latent space (anti-collapse training, free bits / KL schedule, graph or boundary conditioning) increase optimization gain over our current Plan-VAE v3?
  H1: gain from initialization rises from about 4-6% to at least 15% at equal budget.
- **RQ2 (fitness fidelity).** Does a polygon-aware fitness (boundary contact adjacency, true overlap) change which solutions and which optimizers win compared with the centroid proxy?
  H2: rankings of optimizers differ in at least one complexity band, and polygon-fitness solutions score better on independent `Q`.
- **RQ3 (optimizer choice).** With RQ1-RQ2 fixed, how do GA, PSO, DE, CMA-ES and NSGA-II compare (final quality, convergence, Pareto coverage) at 1k and 10k evaluations?
  H3: gaps between optimizers are larger and stable once the latent is controllable; NSGA-II gives a better trade-off front than weighted-sum GA/PSO.
- **RQ4 (transfer).** Do fitness gains transfer to independent geometric metrics `Q` (polygon IoU, door-graph walkable path)? Rendering with DiT/Pix2Pix is out of scope (compute) and listed as future work.

## 6. Success criteria (decide before running)

1. `C(D)` for the new Plan-VAE significantly above v3; `zero_z` and `random_z` reconstruction error clearly worse than `encoded_mu`.
2. Improvement over initialization at least 15% (95% CI excludes the v3 value), on 60+ held-out cases, case as the independent unit.
3. Gains on at least one independent metric `Q` that is not in `F`.
4. Results reproducible with hashed benchmark and seeds (reuse the existing protocol).

## 7. Experiment plan (minimal)

1. Re-verify E1-E5 (latent sensitivity audit, 3 seeds).
2. Train Plan-VAE variants: baseline v3, free-bits/beta sweep, boundary-and-graph-conditioned.
3. Implement polygon fitness using ResPlan polygons, doors, windows; activate `L_ratio`.
4. Run optimizer benchmark (existing 60-case x 30-seed protocol, extended optimizers and budgets).
5. Independent evaluation `Q` + small expert study (5-10 architects).
6. Out of scope: training DiT/Pix2Pix renderers (needs more than Kaggle GPU).

## 7b. Compute budget (Kaggle GPU only)

- VAE variants: small Transformer, one session (under 12 h) per variant; reuse saved ResPlan tensors.
- Optimizers: CPU, about 0.25 s per 1000-evaluation run; 10k-budget benchmark is feasible.
- Keep checkpoints and results in Kaggle datasets, since sessions are ephemeral.

## 8. Risks

- Posterior collapse may be intrinsic to the data and token representation (fallback: direct latent-free parametrization compared as baseline).
- ResPlan has no explicit physical scale per plan beyond area fields; confirm unit handling.
- Independent metric `Q` must be genuinely independent of `F`.
- Novelty must be checked against recent work (HouseDiffusion, GSDiff, HouseLLM, MaskPLAN) before submission.

## 9. Planned contributions

1. Controllability audit and fix for latent-space layout optimization.
2. Polygon-aware, multi-objective fitness with independent validation.
3. Rigorous multi-optimizer benchmark with a frozen, hashed protocol.
4. Evidence on whether latent-space fitness gains transfer to final layouts.

## 10. PhD umbrella link

This is Chapter 1 (representation + optimizer + evaluation core). Later chapters extend objectives (daylight, energy), human-in-the-loop interaction, and other building types.
