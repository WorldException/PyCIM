# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class GeographicalRegion(IdentifiedObject):
    """A geographical region of a power system network model.
    """

    def __init__(self, Regions=None, *args, **kw_args):
        """Initializes a new 'GeographicalRegion' instance.

        @param Regions: The association is used in the naming hierarchy.
        """
        self._Regions = []
        self.Regions = [] if Regions is None else Regions

        super(GeographicalRegion, self).__init__(*args, **kw_args)

    def getRegions(self):
        """The association is used in the naming hierarchy.
        """
        return self._Regions

    def setRegions(self, value):
        for x in self._Regions:
            x._Region = None
        for y in value:
            y._Region = self
        self._Regions = value

    Regions = property(getRegions, setRegions)

    def addRegions(self, *Regions):
        for obj in Regions:
            obj._Region = self
            self._Regions.append(obj)

    def removeRegions(self, *Regions):
        for obj in Regions:
            obj._Region = None
            self._Regions.remove(obj)
