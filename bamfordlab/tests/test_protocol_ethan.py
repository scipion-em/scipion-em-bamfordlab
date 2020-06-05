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

from pyworkflow.tests import BaseTest, DataSet, setupTestProject
from pwem import Domain
from pwem.protocols import ProtImportMicrographs

from bamfordlab.protocols import ProtEthanPicker

XmippProtPreprocessMicrographs = Domain.importFromPlugin('xmipp3.protocols',
                                                  'XmippProtPreprocessMicrographs')


class TestProtEthanPicking(BaseTest):
    @classmethod
    def setUpClass(cls):
        setupTestProject(cls)
        cls.ds = DataSet.getDataSet('xmipp_tutorial')

    def test_workflow(self):
        # First, import a set of micrographs
        print("Importing BPV mics...")
        protImport = self.newProtocol(ProtImportMicrographs,
                                      filesPath=self.ds.getFile('micrographs'),
                                      filesPattern='BPV*mrc',
                                      samplingRate=1.237, voltage=300)
        self.launchProtocol(protImport)
        self.assertIsNotNone(protImport.outputMicrographs,
                             "There was a problem with the import")

        print("Downsampling...")
        protDownsampling = self.newProtocol(XmippProtPreprocessMicrographs,
                                            doDownsample=True, downFactor=5,
                                            doCrop=False, runMode=1,
                                            numberOfThreads=1)
        protDownsampling.inputMicrographs.set(protImport.outputMicrographs)
        self.launchProtocol(protDownsampling)
        self.assertIsNotNone(protDownsampling.outputMicrographs,
                             "There was a problem with the downsampling")

        # Estimate CTF on the downsampled micrographs
        print("Picking with ETHAN...")
        protEthan = self.newProtocol(ProtEthanPicker, radius=50)
        protEthan.inputMicrographs.set(protDownsampling.outputMicrographs)
        self.launchProtocol(protEthan)
        self.assertIsNotNone(protEthan.outputCoordinates,
                             "There was a problem picking with ETHAN")
