# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ClassName
                                 A QGIS plugin
 Aqui é a descrição de um plugin.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-04-11
        copyright            : (C) 2019 by __AUTOR__
        email                : __EMAIL__
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ClassName class from file ClassName.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .module_name import ClassName
    return ClassName(iface)
