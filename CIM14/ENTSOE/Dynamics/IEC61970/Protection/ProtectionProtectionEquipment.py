# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from CIM14.ENTSOE.Dynamics.IEC61970.Core.CoreEquipment import CoreEquipment

class ProtectionProtectionEquipment(CoreEquipment):

    def __init__(self, ConductingEquipments=None, *args, **kw_args):
        """Initialises a new 'ProtectionProtectionEquipment' instance.

        @param ConductingEquipments: 
        """
        self._ConductingEquipments = []
        self.ConductingEquipments = [] if ConductingEquipments is None else ConductingEquipments

        super(ProtectionProtectionEquipment, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ConductingEquipments"]
    _many_refs = ["ConductingEquipments"]

    def getConductingEquipments(self):
        """
        """
        return self._ConductingEquipments

    def setConductingEquipments(self, value):
        for p in self._ConductingEquipments:
            filtered = [q for q in p.ProtectionEquipments if q != self]
            self._ConductingEquipments._ProtectionEquipments = filtered
        for r in value:
            if self not in r._ProtectionEquipments:
                r._ProtectionEquipments.append(self)
        self._ConductingEquipments = value

    ConductingEquipments = property(getConductingEquipments, setConductingEquipments)

    def addConductingEquipments(self, *ConductingEquipments):
        for obj in ConductingEquipments:
            if self not in obj._ProtectionEquipments:
                obj._ProtectionEquipments.append(self)
            self._ConductingEquipments.append(obj)

    def removeConductingEquipments(self, *ConductingEquipments):
        for obj in ConductingEquipments:
            if self in obj._ProtectionEquipments:
                obj._ProtectionEquipments.remove(self)
            self._ConductingEquipments.remove(obj)

