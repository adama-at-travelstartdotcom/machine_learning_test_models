

import model_x


class linear_regression_model(model_x.linear_regression_model):

    def __init__(self, dataset=..., step=0.1, epoch=100, batch_size=0):
        super().__init__(dataset, step, epoch, batch_size)

    def execute(self):

        model_x.linear_regression_model.matplotlib_dataset(self)

        model_x.linear_regression_model.batched_dataset(self)

        model_x.linear_regression_model.root_mean_error(self)

        model_x.linear_regression_model.model(self)





