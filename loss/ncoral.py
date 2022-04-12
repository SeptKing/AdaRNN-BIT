import torch
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def CORAL(source, target):
    d = source.size(1)
    ns, nt = source.size(0), target.size(0)

    #source covariance
    tmp_s = torch.ones((1, ns)).to(device) @ source ## @是矩阵乘法运算符
    cs = (source.t() @ source - (tmp_s.t() @ tmp_s) / ns) / (ns - 1)

    #target covariance
    tmp_t = torch.ones((1, nt)).to(device) @ target
    ct = (target.t() @ target - (tmp_t.t() @ tmp_t) / nt) / (nt -1)

    #frobenius norm
    loss = (cs - ct).pow(2).sum()
    loss = loss / (4 * d * d)


