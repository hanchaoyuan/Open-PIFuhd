# author: lingtengqiu
# data: 2021-01-18
# all networks are built from two part:
# one is backbone, the other is head
import torch.nn as nn
from engineer.registry import build_from_cfg
from .registry import BACKBONES, HEADS,DEPTH,PIFU


def build(cfg, registry, default_args=None):
    if isinstance(cfg, list):
        modules = [
            build_from_cfg(cfg_, registry, default_args) for cfg_ in cfg
        ]
        return nn.Sequential(*modules)
    else:
        return build_from_cfg(cfg, registry, default_args)

def build_backbone(cfg):
    return build(cfg, BACKBONES)

def build_depth(cfg):
    return build(cfg, DEPTH)

def build_head(cfg):
    return build(cfg, HEADS)

def build_model(cfg):
    # modules = [build_backbone(cfg.backbone), build_head(cfg.head),build_depth(cfg.depth)]
    # cfg.PIFu.backbone=modules[0]
    # cfg.PIFu.head = modules[1]
    # cfg.PIFu.depth =modules[2]
    return build(cfg.PIFu,PIFU)
    # return build_backbone(cfg.backbone)