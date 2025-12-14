from .utils import merge_dicts

SELECTION_TREE = {
    "read_book": {
        "read_another": {
            "add_own_text": {
                "select_corpus": {}
            }
        },
        "1gram": {
            "2gram": {
                "3gram": {}
            },
            "weighted_random": {}
        },
        "tokenization": {
            "nltk": {}
        }
    }
}


FEATURE_CONFIG_MAP = {
    "read_book": {
        "knowledge": [{"id": "moby_dick"}]
    },
    "read_another": {
        "knowledge": [{"id": "alice"}]
    },
    "add_own_text": {
        "knowledge": []
    },
    "1gram": {
        "capabilities": {"previous": {"enabled": True, "depth": 1}}
    },
    "2gram": {
        "capabilities": {"previous": {"enabled": True, "depth": 2}}
    },
    "3gram": {
        "capabilities": {"previous": {"enabled": True, "depth": 3}}
    },
    "weighted_random": {
        "capabilities": {"previous": {"mode": "weighted"}}
    },
    "tokenization": {
        "capabilities": {"tokenizer": {"type": "nltk"}}
    },
    "nltk": {
        "capabilities": {"tokenizer": {"type": "nltk"}}
    }
}

def get_unlocked_features(selected_features):
    if not selected_features:
        return list(SELECTION_TREE.keys())

    unlocked = set()

    def traverse(node, selected_path):
        """Recursively unlock children only along selected paths."""
        for feature, children in node.items():
            if feature in selected_path:
                traverse(children, selected_path)
            else:
                unlocked.add(feature)

    traverse(SELECTION_TREE, set(selected_features))

    unlocked -= set(selected_features)
    return sorted(unlocked)

def get_tree_with_status(selected_features):
    def traverse(node, path):
        result = {}
        for feature, children in node.items():
            full_path = path + [feature]
            if feature in selected_features:
                status = "selected"
            elif all(f in selected_features for f in path):
                status = "available"
            else:
                status = "locked"
            result[feature] = {
                "status": status,
                "children": traverse(children, full_path)
            }
        return result
    return traverse(SELECTION_TREE, [])

def rebuild_config_from_selected(selected_features = []):
    config = {}
    for feat in selected_features:
        feat_config = FEATURE_CONFIG_MAP.get(feat, {})
        config = merge_dicts(config, feat_config)
    config["selected_features"] = selected_features
    return config