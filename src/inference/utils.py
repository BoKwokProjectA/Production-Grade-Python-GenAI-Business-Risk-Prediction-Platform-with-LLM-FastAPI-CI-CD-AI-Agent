"""
Utility functions for model handling
"""


def strip_orig_mod_prefix(state_dict):
    new_state_dict = {}
    for key, value in state_dict.items():
        new_key = key.replace("net._orig_mod.", "net.")
        new_state_dict[new_key] = value
    return new_state_dict
