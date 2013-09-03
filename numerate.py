import sublime_plugin


class numerate(sublime_plugin.TextCommand):
    def run(self, edit):
        for i, region in enumerate(self.view.sel()):
            self.view.insert(edit, region.begin(), str(i + 1))
