# **************************************************************************
# *
# * Authors:     J.M. De la Rosa Trevin (delarosatrevin@scilifelab.se)
# *
# * SciLifeLab, Stockholm University
# *
# * This program is free software; you can redistribute it and/or modify
# * it under the terms of the GNU General Public License as published by
# * the Free Software Foundation; either version 2 of the License, or
# * (at your option) any later version.
# *
# * This program is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# * GNU General Public License for more details.
# *
# * You should have received a copy of the GNU General Public License
# * along with this program; if not, write to the Free Software
# * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA
# * 02111-1307  USA
# *
# *  All comments concerning this program package may be sent to the
# *  e-mail address 'scipion@cnb.csic.es'
# *
# **************************************************************************

import os

import pyworkflow.em

from .constants import ETHAN, ETHAN_HOME


_logo = "bamford_logo.gif"
_references =['Kivioja2000']


class Plugin(pyworkflow.em.Plugin):
    _homeVar = ETHAN_HOME
    _pathVars = [ETHAN_HOME]
    _supportedVersions = ['1.2']

    @classmethod
    def _defineVariables(cls):
        cls._defineEmVar(ETHAN_HOME, 'ethan-1.2')

    @classmethod
    def getProgram(cls):
        return os.path.join(os.environ[ETHAN_HOME], ETHAN)


pyworkflow.em.Domain.registerPlugin(__name__)
