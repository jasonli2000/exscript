# Copyright (C) 2007-2009 Samuel Abels.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2, as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
import copy
from Template import Template
from Scope    import Scope

class Program(Scope):
    def __init__(self, lexer, parser, variables, **kwargs):
        Scope.__init__(self, 'Program', lexer, parser, None, **kwargs)
        self.variables      = variables
        self.init_variables = variables
        self.add(Template(lexer, parser, self))

    def init(self, *args, **kwargs):
        for key in kwargs:
            if key.find('.') >= 0 or key.startswith('_'):
                continue
            if type(kwargs[key]) == type([]):
                self.init_variables[key] = kwargs[key]
            else:
                self.init_variables[key] = [kwargs[key]]

    def execute(self, *args, **kwargs):
        self.variables = copy.copy(self.init_variables)
        if kwargs.has_key('variables'):
            self.variables.update(kwargs.get('variables'))
        self.value()
        return self.variables