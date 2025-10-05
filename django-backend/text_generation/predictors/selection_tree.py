SELECTION_TREE = {
    "read_book": {
        "read_another": {
            "add_own_text": {
                "add_own_text": {}
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
        "knowledge": [{"path": "./text_generation/predictors/data/moby_dick.txt"}]
    },
    "read_another": {
        "knowledge": [{"path": "./text_generation/predictors/data/alice.txt"}]
    },
    "add_own_text": {
        "knowledge": []
    },
    "1gram": {
        "capabilities": {"previous": {"enabled": True, "depth": 1, "mode": "deterministic"}}
    },
    "2gram": {
        "capabilities": {"previous": {"enabled": True, "depth": 2, "mode": "deterministic"}}
    },
    "3gram": {
        "capabilities": {"previous": {"enabled": True, "depth": 3, "mode": "deterministic"}}
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

    node = SELECTION_TREE
    for f in selected_features:
        unlocked.update(node.keys())
        node = node.get(f, {})

    unlocked.update(node.keys())

    unlocked -= set(selected_features)

    return sorted(unlocked)
