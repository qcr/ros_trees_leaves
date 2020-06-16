from rv_trees.leaves import Leaf

try:
    input = raw_input
except NameError:
    pass


class Print(Leaf):
    def __init__(self, name='Print', *args, **kwargs):
        super(Print, self).__init__(name,
                                    result_fn=self._result_fn,
                                    *args,
                                    **kwargs)

    def _result_fn(self):
        print(self.loaded_data)
        return self.loaded_data


class SelectItem(Leaf):
    # NOTE: this is BLOCKING & should ONLY BE USED for debugging purposes
    _DEFAULT_SELECT_TEXT = "Please select an item"

    def __init__(self, select_text=None, *args, **kwargs):
        super(SelectItem, self).__init__("Select Item",
                                         result_fn=self._result_fn,
                                         save=True,
                                         *args,
                                         **kwargs)
        self.select_text = (SelectItem._DEFAULT_SELECT_TEXT
                            if select_text is None else select_text)

    def _result_fn(self):
        items = self.loaded_data
        if (not isinstance(items, list) or len(items) == 0 or
                not any([isinstance(i, str) for i in items])):
            ValueError(
                "SelectItem leaf expects a list of strings as loaded_data. "
                "It has been provided with: %s" % (items))

        item = None
        while (item is None or item not in items):
            item = input("%s %s: " % (self.select_text, items))

        return item
