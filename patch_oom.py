"""Usage: python patch_oom.py <your_script.py>  -> writes <your_script>_fixed.py (OOM fix for the Phase-2 preflight / training)."""
import re, sys
src_path = sys.argv[1]
s = open(src_path).read()

def rep(old, new, label):
    global s
    if s.count(old) != 1:
        raise SystemExit(f'PATCH FAILED at "{label}": found {s.count(old)} matches (expected 1). Send this message.')
    s = s.replace(old, new)

rep("import os, sys, subprocess, shutil, glob\n",
    "import os, sys, subprocess, shutil, glob, gc\nos.environ.setdefault('PYTORCH_CUDA_ALLOC_CONF', 'expandable_segments:True')\n", 'env+gc')
rep("P2_W, P2_DEPTH, P2_HEADS, P2_ZC, P2_BS = (64, 2, 4, 4, 32) if SMOKE else (384, 10, 6, 4, 128)",
    "P2_W, P2_DEPTH, P2_HEADS, P2_ZC, P2_BS = (64, 2, 4, 4, 32) if SMOKE else (384, 10, 6, 4, 128)\n"
    "    P2_BS_VAE = 32 if SMOKE else int(os.environ.get('FP_VAE_BS', 24))          # the VAE works at full image resolution -> small batch", 'batch sizes')
rep("s.cin = nn.Sequential(nn.Conv2d(cc, w, 3, padding=1), nn.SiLU(), nn.Conv2d(w, w, 4 * patch, stride=4 * patch))",
    "s.cin = nn.Sequential(nn.Conv2d(cc, 64, 3, padding=1), nn.SiLU(), nn.Conv2d(64, w, 4 * patch, stride=4 * patch))", 'cheap cond branch')
s, n = re.subn(r"(for i in range\(0, len\(perm\) - )P2_BS( \+ 1, )P2_BS(\):\s*\n\s*x, L, _, _ = p2_batch\(perm\[i:i \+ )P2_BS(\])",
               r"\1P2_BS_VAE\2P2_BS_VAE\3P2_BS_VAE\4", s)
if n != 1: raise SystemExit(f'PATCH FAILED at "vae train loop": {n} matches')
rep("bs = P2_BS; idx = idx_train[:bs]; x, L, ty, mk = p2_batch(idx); res = {}",
    "bs = P2_BS; idx = idx_train[:bs]; x, L, ty, mk = p2_batch(idx); res = {}; xv = x[:P2_BS_VAE]", 'preflight batch')
rep("dit = LayoutDiT(P2_ZC, P2_CC, P2_IMG // 4, P2_W, P2_DEPTH, P2_HEADS).to(DEVICE); o2 = torch.optim.AdamW(dit.parameters(), 2e-4)",
    "dit = o2 = None; _lazy = lambda: (lambda d: (d, torch.optim.AdamW(d.parameters(), 2e-4)))(LayoutDiT(P2_ZC, P2_CC, P2_IMG // 4, P2_W, P2_DEPTH, P2_HEADS).to(DEVICE))", 'lazy dit')
rep("rec, mu, lv = vae(x)\n", "rec, mu, lv = vae(xv)\n", 'vae input')
rep("loss = (rec.float() - x).abs().mean(); o1.zero_grad()", "loss = (rec.float() - xv).abs().mean(); o1.zero_grad()", 'vae loss')
rep("z1 = torch.randn(bs, P2_ZC, P2_IMG // 4, P2_IMG // 4, device=DEVICE);",
    "(dit is None and (gc.collect(), torch.cuda.empty_cache())); dit, o2 = (dit, o2) if dit is not None else _lazy(); z1 = torch.randn(bs, P2_ZC, P2_IMG // 4, P2_IMG // 4, device=DEVICE);", 'dit created after vae test')
rep("nb = len(idx_train) // bs; est = (nb * res['vae'] * P2_VAE_EP + nb * res['dit'] * P2_DIT_EP) / 3600",
    "nb = len(idx_train) // bs; nbv = len(idx_train) // P2_BS_VAE; est = (nbv * res['vae'] * P2_VAE_EP + nb * res['dit'] * P2_DIT_EP) / 3600", 'estimate')
rep("del vae, dit, o1, o2", "del vae, dit, o1, o2; gc.collect(); torch.cuda.empty_cache()", 'cleanup')
rep("layout_dit_{P2_IMG}.pt'))): preflight()", "layout_dit_{P2_IMG}.pt'))): gc.collect(); torch.cuda.empty_cache(); preflight()", 'pre-call cleanup')

out = src_path.replace('.py', '') + '_fixed.py'
open(out, 'w').write(s); print('OK ->', out)
