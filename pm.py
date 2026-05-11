#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('---- 位相余裕と安定性の確認 -----')

import numpy as np
import control as ctrl


def cal_pm2(a, b, k):
    L = ctrl.tf([k], [1, (a + b), a * b, 0])
    gm, pm, Wcg, Wcp = ctrl.margin(L)
    print('--------------------------------------------------------------')
    print(f'位相余裕[deg]={pm:.3f}  ゲイン交差周波数={Wcp:.3f}  a={a:.3f}  b={b:.3f}  k={k:.3f}')
    try:
        Gm_db = 20 * np.log10(gm) if (np.isfinite(gm) and gm > 0) else np.inf
    except Exception:
        Gm_db = 20 * np.log10(np.abs(gm))
    print(f'ゲイン余裕[dB]={Gm_db:.3f}  位相交差周波数={Wcg:.3f}')
    FB = ctrl.feedback(L, ctrl.tf([1], [1]))
    poles = ctrl.poles(FB)
    def _fmt_pole(p):
        try:
            re = p.real
            im = p.imag
        except Exception:
            # fallback for real numbers
            return f'{p:.3f}'
        if np.isclose(im, 0):
            return f'{re:.3f}'
        return f'{re:.3f}{im:+.3f}j'

    formatted_poles = [_fmt_pole(p) for p in poles]
    print('閉ループ極 =', formatted_poles)
    return {'L': L, 'gm': gm, 'pm': pm, 'Wcg': Wcg, 'Wcp': Wcp, 'poles': poles}


def cal_pm3(a, b, c, k):
    La = ctrl.tf([1], [1, a])
    Lb = ctrl.tf([1], [1, b])
    Lc = ctrl.tf([1], [1, c])
    L = k * La * Lb * Lc
    gm, pm, Wcg, Wcp = ctrl.margin(L)
    print('--------------------------------------------------------------')
    print(f'位相余裕[deg]={pm:.3f}  ゲイン交差周波数={Wcp:.3f}  a={a:.3f}  b={b:.3f}  c={c:.3f}  k={k:.3f}')
    try:
        Gm_db = 20 * np.log10(gm) if (np.isfinite(gm) and gm > 0) else np.inf
    except Exception:
        Gm_db = 20 * np.log10(np.abs(gm))
    print(f'ゲイン余裕[dB]={Gm_db:.3f}  位相交差周波数={Wcg:.3f}')
    FB = ctrl.feedback(L, ctrl.tf([1], [1]))
    poles = ctrl.poles(FB)
    def _fmt_pole2(p):
        try:
            re = p.real
            im = p.imag
        except Exception:
            return f'{p:.3f}'
        if np.isclose(im, 0):
            return f'{re:.3f}'
        return f'{re:.3f}{im:+.3f}j'

    formatted_poles = [_fmt_pole2(p) for p in poles]
    print('閉ループ極 =', formatted_poles)
    return {'L': L, 'gm': gm, 'pm': pm, 'Wcg': Wcg, 'Wcp': Wcp, 'poles': poles}


def main():
    #　パラメータがa,b,kの場合
    examples = [
        (2, 3, 5 * np.sqrt(2)),
        (4, 6, 40 * np.sqrt(2)),
        (2, 5, 14 * np.sqrt(3)),
        (3, 3, 12 * np.sqrt(3)),
        (2 * np.sqrt(3), 2 * np.sqrt(3), 32),
        (4, 15, 114),
        (5, 9, 84),
        (np.sqrt(3), 3, np.sqrt(6) * 6),
        (1, np.sqrt(3), 2 * np.sqrt(2)),
    ]
    for a, b, k in examples:
        cal_pm2(a, b, k)

    #　パラメータがa,b,c,kの場合
    a = 1
    b = np.sqrt(3)
    c = np.sqrt(3)
    k = 4 * np.sqrt(2)
    cal_pm3(a, b, c, k)

if __name__ == '__main__':
    main()
