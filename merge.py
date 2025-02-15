import yaml
from collections import OrderedDict

PERSONAL_RULE = [
    "DOMAIN-KEYWORD,807.91p51.com,DIRECT",
    "DOMAIN-KEYWORD,killcovid2021,DIRECT"
]


def ordered_yaml_load(stream, Loader=yaml.SafeLoader,
                      object_pairs_hook=OrderedDict):
    class OrderedLoader(Loader):
        pass

    def _construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))

    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        _construct_mapping)
    return yaml.load(stream, OrderedLoader)


def ordered_yaml_dump(data, stream=None, Dumper=yaml.SafeDumper,
                      object_pairs_hook=OrderedDict, **kwds):
    class OrderedDumper(Dumper):
        pass

    def _dict_representer(dumper, data):
        return dumper.represent_mapping(
            yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
            data.items())

    OrderedDumper.add_representer(object_pairs_hook, _dict_representer)
    return yaml.dump(data, stream, OrderedDumper, **kwds)


def edit_rule(rules):
    last_rule = rules.pop()
    # rules += PERSONAL_RULE
    rules = [last_rule]
    return rules


if __name__ == "__main__":
    file = open("base.yaml", "r", encoding="utf-8")
    config = ordered_yaml_load(file)
    bk_file = open("new.yaml", "r", encoding="utf-8")
    bk_config = ordered_yaml_load(bk_file)

    config["proxies"] = bk_config["proxies"]
    config["proxy-groups"] = bk_config["proxy-groups"]
    config["rules"] = edit_rule(bk_config["rules"])

    with open("config.yaml", "w", encoding="utf-8") as f:
        f.write(ordered_yaml_dump(config, allow_unicode=True, encoding=None))
