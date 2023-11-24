# Author: M. MAD
import math
import statistics as st

import prettytable as pt


QUARTILES = [0.25, 0.5, 0.75]
# The incremental loop method won't work for 0.3, 0.8 and 0.9 deciles
DECILES = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]


class DataType: pass

class Discrete(DataType): pass

class Continuous(DataType): pass


data = [100, 121, 130, 129, 150, 116, 120, 117, 154, 125, 110, 119, 130,
        115, 125, 125, 90, 109, 100, 120, 92, 112, 115, 118]

data_type = Continuous()
# data_type = Discrete()

number_of_classes = 8

precise_intervals = False
# precise_intervals = True

calculate_q = True
# calculate_q = False

calculate_d = True
# calculate_d = False


def def_class_ranges(minv, K, L):
    r = []
    for i in range(K):
        h = minv + L
        r.append((minv, h))
        minv = h
    return r


def continuous_x_i_lst(minv, K, L):
    minv += L/2
    r = []
    for i in range(K):
        r.append(minv)
        minv += L
    return r


def count_in_class(data, low, high, is_last=False):
    count = 0
    for e in data:
        if e >= low and (e < high if not is_last else e <= high):
            count += 1
    return count


def fr_lister(data, x_i_or_ranges, dt):
    data_len = len(data)
    x_i_or_ranges_len = len(x_i_or_ranges)
    r_postfix = f"/{data_len}"
    f_i_lst, F_i_lst, r_i_lst, R_i_lst = [], [0], [], []
    for i, u in enumerate(x_i_or_ranges):
        is_last = i == x_i_or_ranges_len-1
        if isinstance(dt, Discrete):
            count = data.count(u)
        elif isinstance(dt, Continuous):
            count = count_in_class(data, u[0], u[1], is_last)
        f_i_lst.append(count)
        r_i_lst.append(str(count) + r_postfix)
        F_i_lst.append(F_i_lst[-1] + count)
        R_i_lst.append(str(F_i_lst[-1]) + r_postfix)
        if is_last:
            F_i_lst.pop(0)  # delete the initial 0 to make it's length equal to other lists
    return f_i_lst, F_i_lst, r_i_lst, R_i_lst


def quantile_calc(data, p, class_ranges, f_i_lst, F_i_lst):
    np = len(data)*p
    for i, F in enumerate(F_i_lst):
        if F > np:
            q_class_no = i
            break
    f = f_i_lst[q_class_no]
    prev_F = F_i_lst[q_class_no-1]
    prev_L = class_ranges[q_class_no-1][0]
    w = class_ranges[q_class_no][1] - class_ranges[q_class_no][0]
    np_F = np-prev_F
    np_F_in_w = np_F * w
    np_F_in_w_on_f = np_F_in_w / f
    q = prev_L + np_F_in_w_on_f
    print(f"Q_{p} (The {q_class_no+1}th class; \
({class_ranges[q_class_no][0]}, {class_ranges[q_class_no][1]})) = \
L + ((np-F)w)/f = \
{prev_L} + (({len(data)}*{p}-{prev_F}){w})/{f} = \
{prev_L} + (({np}-{prev_F}){w})/{f} = \
{prev_L} + (({np_F}){w})/{f} = \
{prev_L} + {np_F_in_w}/{f} = \
{prev_L} + {np_F_in_w_on_f} = {q}")


def fdt(x_i_lst, f_i_lst, F_i_lst, r_i_lst, R_i_lst, f_i_times_x_i_lst,
        x_i_sq_lst, f_i_times_x_i_sq_lst, class_ranges=None):
    t = pt.PrettyTable()
    # t.field_names = ["Class Range", "x_i", "f_i", "F_i", "r_i", "R_i", "f_i*x_i", "(x_i)^2", "f_i*(x_i)^2"]
    if class_ranges is not None:
        t.add_column("Class Range", class_ranges)
    t.add_column("x_i", x_i_lst)
    t.add_column("f_i", f_i_lst)
    t.add_column("F_i", F_i_lst)
    t.add_column("r_i", r_i_lst)
    t.add_column("R_i", R_i_lst)
    t.add_column("f_i*x_i", f_i_times_x_i_lst)
    t.add_column("(x_i)^2", x_i_sq_lst)
    t.add_column("f_i*(x_i)^2", f_i_times_x_i_sq_lst)
    t.add_autoindex("i")
    return t


def main(data=data, dt=data_type, K: int = number_of_classes, pi: bool = precise_intervals,
         calc_q : bool = calculate_q, calc_d : bool = calculate_d):
    data = sorted(data)
    data_len = len(data)
    minv = min(data)
    maxv = max(data)
    R = maxv - minv  # Range
    L = R/K if pi else round(R/K)  # Class interval
    print(f"""Sorted data: {data}
n = {data_len}
min = {minv}
max = {maxv}
R = max - min = {maxv} - {minv} = {R}
L = R / K = {R} / {K} = {L}

Frequency Distribution Table:""")
    if isinstance(dt, Discrete):
        class_ranges = None
        x_i_lst = sorted(list(set(data)))
        K = len(x_i_lst)
    elif isinstance(dt, Continuous):
        class_ranges = def_class_ranges(minv, K, L)
        x_i_lst = continuous_x_i_lst(minv, K, L)
    else:
        raise ValueError("parameter 'dt' have to be of type 'Discrete' or 'Continuous'")
    f_i_lst, F_i_lst, r_i_lst, R_i_lst = fr_lister(data, x_i_lst if isinstance(dt, Discrete) else class_ranges, dt)
    f_i_times_x_i_lst = [f_i_lst[i] * x_i_lst[i] for i in range(K)]
    x_i_sq_lst = [x_i**2 for x_i in x_i_lst]
    f_i_times_x_i_sq_lst = [f_i_lst[i] * x_i_sq_lst[i] for i in range(K)]
    # print(f_i_times_x_i_lst)
    t = fdt(x_i_lst, f_i_lst, F_i_lst, r_i_lst, R_i_lst, f_i_times_x_i_lst,
            x_i_sq_lst, f_i_times_x_i_sq_lst, class_ranges)
    t.set_style(pt.DOUBLE_BORDER)
    print(t)
    x_bar = sum(f_i_times_x_i_lst)/data_len
    S_sq = (sum(f_i_times_x_i_sq_lst)/data_len) - x_bar**2
    S = math.sqrt(S_sq)
    Cv = S/x_bar
    M = x_i_lst[f_i_lst.index(max(f_i_lst))]
    print(f"""
x_bar (Mean) = Σ(f_i*x_i)/n = {sum(f_i_times_x_i_lst)}/{data_len} = {x_bar}
S^2 (Variance) = ((1/n)*Σ(f_i*x_i^2)) - x_bar^2 = {sum(f_i_times_x_i_lst)}/{data_len} - {x_bar**2} = {sum(f_i_times_x_i_lst)/data_len} - {x_bar**2} = {S_sq}
S (Standard Deviation) = √(S^2) = √{S_sq} = {S}
Cv (Coefficient of Variation) = S/x_bar = {S}/{x_bar} = {Cv}
M (Mode) = {M}
""")
    if isinstance(dt, Continuous):
        if calc_q:
            print("### Calculating Qs (Quartiles):")
            for p in QUARTILES:
                quantile_calc(data, p, class_ranges, f_i_lst, F_i_lst)
                print("--------------------")
        if calc_d:
            print("### Calculating Ds (Deciles):")
            for p in DECILES:
                quantile_calc(data, p, class_ranges, f_i_lst, F_i_lst)
                print("--------------------")


if __name__ == "__main__":
    main()
