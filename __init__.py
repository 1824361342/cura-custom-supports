# Copyright (c) 2018 Lokster <http://lokspace.eu>
# Based on the SupportBlocker plugin, and licensed under LGPLv3 or higher.

from . import CustomSupports

from UM.i18n import i18nCatalog
i18n_catalog = i18nCatalog("cura")

def getMetaData():
    return {
        "tool": {
            "name": i18n_catalog.i18nc("@label", "Custom Support"),
            "description": i18n_catalog.i18nc("@info:tooltip", "Add custom supports"),
            "icon": "tool_icon.svg",
            "weight": 4
        }
    }

def register(app):
    return { "tool": CustomSupports.CustomSupports() }
