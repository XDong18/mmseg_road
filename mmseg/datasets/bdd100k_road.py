import os.path as osp

from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class Bdd100k_road_Dataset(CustomDataset):
    """Pascal VOC dataset.

    Args:
        split (str): Split txt file for Pascal VOC.
    """

    CLASSES = ('background', 'alternative', 'direct')

    PALETTE = [[0, 130, 0], [255, 0, 0], [0, 0, 255]]

    def __init__(self, split, **kwargs):
        super(Bdd100k_road_Dataset, self).__init__(
            img_suffix='.jpg', seg_map_suffix='.png', split=split, **kwargs)
        assert osp.exists(self.img_dir)
