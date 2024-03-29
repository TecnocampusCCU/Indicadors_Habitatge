# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Indicadors_Habitatge
                                 A QGIS plugin
 Indicadors_Habitatge
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-11-10
        copyright            : (C) 2020 by CCU
        email                : jlopez@tecnocampus.cat
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
    """Load Indicadors_Habitatge class from file Indicadors_Habitatge.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Indicadors_Habitatge import Indicadors_Habitatge
    return Indicadors_Habitatge(iface)
