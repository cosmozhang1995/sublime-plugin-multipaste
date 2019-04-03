import sublime
import sublime_plugin
import os
import json

dirname = os.path.split(__file__)[0]
strings_filename = os.path.join(dirname, "strings.json")

class PastebinInsertCommand(sublime_plugin.TextCommand):
    counter = 0
    def run(self, edit, index):
        # insstr = self.view.settings().get("pastebin_string_%d" % index)
        insstr = None
        try:
            with open(strings_filename, "r") as file:
                strings = json.load(file)
                insstr = strings[str(index)]
        except Exception:
            pass
        if insstr:
            for sel in self.view.sel():
                self.view.insert(edit, sel.a, insstr)
        else:
            print("no string to insert", pool)

class PastebinCreateCommand(sublime_plugin.TextCommand):
    counter = 0
    def run(self, edit, index):
        insstr = self.view.substr(self.view.sel()[0])
        # self.view.settings().set("pastebin_string_%d" % index, insstr)
        strings = {}
        try:
            with open(strings_filename, "r") as file:
                strings = json.load(file)
        except Exception:
            pass
        strings[str(index)] = insstr
        with open(strings_filename, "w") as file:
            json.dump(strings, file, indent=2)
