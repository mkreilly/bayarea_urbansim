import os, sys
import simplejson
from synthicity.utils import misc

sys.path.insert(0,".")
import dataset
dset = dataset.BayAreaDataset(os.path.join(misc.data_dir(),'bayarea.h5'))

print "Running rsh_simulate"
import rsh_simulate
retval = rsh_simulate.rsh_simulate(dset)
if retval: open(os.path.join(misc.output_dir(),"rsh_simulate.json"),"w").write(simplejson.dumps(retval,sort_keys=True,indent=4))
print "Running hlcms_simulate"
import hlcms_simulate
retval = hlcms_simulate.hlcms_simulate(dset)
if retval: open(os.path.join(misc.output_dir(),"hlcms_simulate.json"),"w").write(simplejson.dumps(retval,sort_keys=True,indent=4))
 