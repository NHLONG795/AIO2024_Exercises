import torch


class Softmax:
    def calc(self, data):
        result = torch.Tensor([])

        # HACK: Stabilize the data by subtracting the max value
        max_data = torch.max(data)
        exp_data = torch.exp(data - max_data)
        sum_exp_data = torch.sum(exp_data)

        for x_i in exp_data:
            magnitude_of_xi = x_i / sum_exp_data
            result = torch.cat((result, torch.Tensor([magnitude_of_xi])))

        return result
