def merge_dicts(base: dict, update: dict) -> dict:
    """
    Merge `update` into `base` recursively.
    - Dicts merge recursively.
    - Lists append new items (avoiding duplicates if needed).
    """
    result = base.copy()
    for k, v in update.items():
        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
            result[k] = merge_dicts(result[k], v)
        elif k in result and isinstance(result[k], list) and isinstance(v, list):
            result[k] = result[k] + [x for x in v if x not in result[k]]
        else:
            result[k] = v
    return result
