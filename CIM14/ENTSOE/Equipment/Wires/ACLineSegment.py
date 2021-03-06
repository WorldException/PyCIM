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

from CIM14.ENTSOE.Equipment.Wires.Conductor import Conductor

class ACLineSegment(Conductor):
    """A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.-  [R4.5] and [R4.7] are satisfied by navigation to ConnectivityNode and Substation -  Each ACLineSegment is required to have an association to a BaseVoltage.  The association to Line is not required. -  Using the “MemberOf_EquipmentContainer” association, an ACLineSegment can only be contained by a Line, but the association to Line is not required. -  Attributes b0ch, g0ch, gch, r0, and x0 are for short circuit only and are not required.   
    """

    def __init__(self, g0ch=0.0, r=0.0, x0=0.0, bch=0.0, x=0.0, b0ch=0.0, gch=0.0, r0=0.0, *args, **kw_args):
        """Initialises a new 'ACLineSegment' instance.

        @param g0ch: Zero sequence shunt (charging) conductance, uniformly distributed, of the entire line section. 
        @param r: Positive sequence series resistance of the entire line section. 
        @param x0: Zero sequence series reactance of the entire line section. 
        @param bch: Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.  This value represents the full charging over the full length of the line. 
        @param x: Positive sequence series reactance of the entire line section. 
        @param b0ch: Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section. 
        @param gch: Positive sequence shunt (charging) conductance, uniformly distributed, of the entire line section. 
        @param r0: Zero sequence series resistance of the entire line section. 
        """
        #: Zero sequence shunt (charging) conductance, uniformly distributed, of the entire line section.
        self.g0ch = g0ch

        #: Positive sequence series resistance of the entire line section.
        self.r = r

        #: Zero sequence series reactance of the entire line section.
        self.x0 = x0

        #: Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.  This value represents the full charging over the full length of the line.
        self.bch = bch

        #: Positive sequence series reactance of the entire line section.
        self.x = x

        #: Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.
        self.b0ch = b0ch

        #: Positive sequence shunt (charging) conductance, uniformly distributed, of the entire line section.
        self.gch = gch

        #: Zero sequence series resistance of the entire line section.
        self.r0 = r0

        super(ACLineSegment, self).__init__(*args, **kw_args)

    _attrs = ["g0ch", "r", "x0", "bch", "x", "b0ch", "gch", "r0"]
    _attr_types = {"g0ch": float, "r": float, "x0": float, "bch": float, "x": float, "b0ch": float, "gch": float, "r0": float}
    _defaults = {"g0ch": 0.0, "r": 0.0, "x0": 0.0, "bch": 0.0, "x": 0.0, "b0ch": 0.0, "gch": 0.0, "r0": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

