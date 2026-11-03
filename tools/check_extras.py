#!/usr/bin/env python3
"""Validate redesign extras. Usage: python3 tools/check_extras.py [sri|kana|mla|all]
Checks structure, lengths, icon names, and that sheet key words really occur in the verse (Devanagari and IAST)."""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build as B

SER = {"sri": B.VERSES, "kana": B.KVERSES, "mla": B.MVERSES}
def strip(t): return re.sub(r"<[^>]+>", " ", t)
def nd(t):  # normalise devanagari: drop tags, spaces, danda, avagraha spelling kept
    return re.sub(r"[\s।॥|,;.\-]", "", strip(t))
def ni(t):
    t = strip(t).lower().replace("’", "'").replace("ṃ", "ṁ")
    return re.sub(r"[\s\-,;.'’]", "", t)

def check(series):
    errs = []; n_ok = 0
    for v in SER[series]:
        if not v.get("sheet"): continue
        tag = f"{series} {v['n']}"
        def e(m): errs.append(f"{tag}: {m}")
        kp, ic, fn, sh = v.get("keypoints"), v.get("icons"), v.get("formnotes"), v["sheet"]
        if not kp or len(kp) not in (3, 4): e("keypoints must be 3 or 4"); continue
        N = len(kp)
        if not ic or len(ic) != N: e("icons length must equal keypoints")
        else:
            for x in ic:
                if x not in B.ICONS: e(f"unknown icon {x}")
        if len(set(ic or [])) != len(ic or []): e("icons repeat")
        if not fn or len(fn) != N: e("formnotes length must equal keypoints")
        for a, b in kp:
            if len(a) > 13: e(f"keypoint name too long ({a})")
            if ":" not in b: e(f"keypoint gloss needs 'Word: description' ({a})")
            else:
                g, dsc = b.split(":", 1)
                if len(g) > 14: e(f"gloss word too long ({g})")
                if len(dsc) > 95: e(f"keypoint description >95 chars ({a})")
        for body, ask in (fn or []):
            if not 90 <= len(body) <= 330: e(f"formnote body length {len(body)} (want 90-330)")
            if not ask.endswith("?") or len(ask) > 130: e("formnote ask must be a question <=130 chars")
        if not v.get("tagline") or len(v["tagline"]) > 130: e("tagline missing or >130")
        if not v.get("forms_title"): e("forms_title missing")
        for k in ("essence", "short", "salut", "words", "take", "salut_title", "centre_title", "centre"):
            if not sh.get(k): e(f"sheet.{k} missing")
        if len(sh.get("salut", [])) != N: e("sheet.salut length must equal keypoints")
        for t in sh.get("salut", []):
            if len(t) > 85: e(f"salut line >85 chars: {t[:30]}")
        if len(sh.get("essence", "")) > 200: e("essence >200")
        if len(sh.get("short", "")) > 250: e("short >250")
        if not 3 <= len(sh.get("take", [])) <= 4: e("take must have 3-4 lines")
        for t in sh.get("take", []):
            if len(t) > 52: e(f"take line >52 chars: {t}")
        if not 3 <= len(sh.get("words", [])) <= 4: e("sheet.words must have 3-4 entries")
        vd, vi = nd(v["deva"]), ni(v["iast"])
        for dv, ia, gl in sh.get("words", []):
            if nd(dv)[:max(2, len(nd(dv))-2)] not in vd: e(f"sheet word not in verse (Devanagari): {dv}")
            if ni(ia)[:max(3, len(ni(ia))-2)] not in vi: e(f"sheet word not in verse (IAST): {ia}")
            if len(gl) > 34: e(f"word gloss >34 chars: {gl}")
        if len(sh.get("centre", "").split()) != 2: e("sheet.centre must be exactly two words")
        for lab_, t in (("salut_title", 24), ("centre_title", 26)):
            if len(sh.get(lab_, "")) > t: e(f"{lab_} >{t} chars")
        if len(v.get("sketchalt", "")) < 60: e("sketchalt missing or too short")
        blob = " ".join([v.get("tagline", ""), sh.get("essence", ""), sh.get("short", "")] + [b for _, b in kp] + [x for x, _ in fn or []] + [y for _, y in fn or []] + sh.get("salut", []) + sh.get("take", []) + [v.get("sketchalt", "")])
        if "—" in blob or "&lt;" in blob or "<" in blob: e("em dash or markup in text")
        if re.search(r"[ऀ-ॿ]", blob.replace(" ", "")) and False: pass
        n_ok += 1
    return errs, n_ok

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    tot = []
    for s in (SER if which == "all" else [which]):
        errs, n = check(s); print(f"{s}: {n} verses with extras checked, {len(errs)} problems"); tot += errs
    for x in tot: print("  -", x)
    sys.exit(1 if tot else 0)
