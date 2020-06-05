# **************************************************************************
# *
# * Authors:     J.M. De la Rosa Trevin (delarosatrevin@scilifelab.se)
# *
# * SciLifeLab, Stockholm University
# *
# * This program is free software; you can redistribute it and/or modify
# * it under the terms of the GNU General Public License as published by
# * the Free Software Foundation; either version 3 of the License, or
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

import pyworkflow as pw
from pwem.wizards import EmWizard
from pwem.viewers import CoordinatesObjectView
from pyworkflow.utils import makePath, cleanPath, readProperties

from bamfordlab.protocols import ProtEthanPicker


#===============================================================================
# PICKER
#===============================================================================

# Not ready yet
# class BamfordDogPickerWizard(EmWizard):
#     _targets = []
#     # wizard is not ready
#     #_targets = [(ProtEthanPicker, ['radius'])]
#
#     def show(self, form):
#         autopickProt = form.protocol
#         micSet = autopickProt.getInputMicrographs()
#         if not micSet:
#             print 'must specify input micrographs'
#             return
#         project = autopickProt.getProject()
#         micfn = micSet.getFileName()
#         coordsDir = project.getTmpPath(micSet.getName())
#         cleanPath(coordsDir)
#         makePath(coordsDir)
#         # Get current values of the properties
# #         micfn = os.path.join(coordsDir, 'micrographs.xmd')
# #         writeSetOfMicrographs(micSet, micfn)
#         dogpickerProps = os.path.join(coordsDir, 'picker.conf')
#         f = open(dogpickerProps, "w")
#
#         args = {
#           "dogpicker" : os.path.join(os.environ['DOGPICKER_HOME'], "ApDogPicker.py"),
#           "convert" : pw.join('apps', 'pw_convert.py'),
#           'coordsDir': coordsDir,
#           'micsSqlite': micSet.getFileName(),
#           "diameter": autopickProt.diameter,
#           "threshold": autopickProt.threshold,
#           "apix": micSet.getSamplingRate()
#           }
#
#
#         f.write("""
#         parameters = diameter,threshold
#         diameter.value = %(diameter)s
#         diameter.label = Diameter
#         diameter.help = some help
#         threshold.value =  %(threshold)s
#         threshold.label = Threshold
#         threshold.help = some help
#         autopickCommand = %(dogpicker)s  --thresh=%%(threshold) --diam=%%(diameter) --apix=%(apix)s  --image=%%(micrograph) --outfile=%(coordsDir)s/%%(micrographName).txt
#         convertCommand = %(convert)s --coordinates --from dogpicker --to xmipp --input  %(micsSqlite)s --output %(coordsDir)s
#         """ % args)
#         f.close()
#         process = CoordinatesObjectView(project, micfn, coordsDir, autopickProt,
#                                         mode=CoordinatesObjectView.MODE_AUTOMATIC,
#                                         pickerProps=dogpickerProps).show()
#         process.wait()
#         myprops = readProperties(dogpickerProps)
#         form.setVar('diameter', myprops['diameter.value'])
#         form.setVar('threshold', myprops['threshold.value'])
