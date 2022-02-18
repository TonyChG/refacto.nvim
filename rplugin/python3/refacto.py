import re
import pynvim
import neovim

brackets = {
    "{": "}",
    "[": "]",
    "(": ")",
    "<": ">",
}


def escape(string):
    for escaped in "\$.*[]^#":
        string = string.replace(escaped, f"\\{escaped}")
    return string


@neovim.plugin
class Main(object):
    def __init__(self, vim):
        self.vim = vim

    @neovim.function("Refacto")
    def refacto(self, _):
        try:
            selection = self.vim.eval('@"')
            selection = escape(selection)
            self.vim.command(
                f"let pattern = input('Replace [{selection}] with : ')"
            )
            pattern = self.vim.eval("pattern")
            pattern = escape(pattern)
            if len(pattern) > 0:
                self.vim.command(f"%s#{selection}#{pattern}#gc|''")
        except pynvim.api.common.NvimError as error:
            self.vim.command(f"echo '{error}'")

    @neovim.function("Selection")
    def selection(self, _):
        self.vim.command(
            "let cursor = nr2char(strgetchar(getline('.')[col('.') - 1:], 0))"
        )
        cursor = self.vim.eval("cursor")

        if re.match(r"[\"'\*]", cursor):
            self.vim.command(f"normal yf{cursor}")
        elif re.match(r"[\]\[\(\)\{\}<>]", cursor):
            self.vim.command(f"normal yf{brackets[cursor]}")
        else:
            self.vim.command(f"normal yiw")

    @neovim.function("SelectionRefacto")
    def selection_refacto(self, _):
        self.selection(_)
        self.refacto(_)
