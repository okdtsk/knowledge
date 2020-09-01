#!/usr/bin/env python3

from dataclasses import dataclass
import os
from typing import *


@dataclass
class SidebarItem:
    name: Text
    path: Text

    def format_as_line(self):
        return f"- [{self.name}]({self.path})\n"


def main(docs_dir: Text):
    subdir_names = [
        f.name
        for f in os.scandir(docs_dir)
        if f.is_dir() and not f.name.startswith(".")
    ]
    sidebar_items: List[SidebarItem] = [SidebarItem("Home", "/")] + [
        SidebarItem(d, f"/{d}/") for d in sorted(subdir_names)
    ]
    with open(docs_dir + "/_sidebar.md", "w") as fp:
        fp.writelines([i.format_as_line() for i in sidebar_items])


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("docs_dir", help="Docsify document dir")
    args = parser.parse_args()
    main(args.docs_dir)
