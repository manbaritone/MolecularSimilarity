#!/usr/bin/env python3
import model_interface

_required_models = {}


def register_model(name, constructor):
    _required_models[name] = constructor


def create_model(name: str) -> model_interface.IModel:
    if _required_models == {}:
        _discover_models()
    return _required_models[name]()


def _discover_models():
    import model.active_index_model
    import model.descriptors_model
    import model.rdkit_ecfp_model
    import model.rdkit_fcfp_model
    import model.rdkit_tt_model
    import model.rdkit_ap_model
    import model.control_model
    import model.active_inactive_index_model
    import model.linear_regression_model
    import model.decision_tree_model
    import model.nbit_ecfp_model
    import model.nbit_fcfp_model
    import model.nbit_ap_model
    import model.nbit_ecfp_model2
    import model.nbit_fcfp_model2
    import model.nbit_tt_model
    import model.equivalent_class_model
    import model.baseline_model
    import model.ecfp_pair_model
