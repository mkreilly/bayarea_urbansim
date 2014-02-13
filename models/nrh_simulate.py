import pandas as pd, numpy as np, statsmodels.api as sm
from synthicity.urbanchoice import *
from synthicity.utils import misc
import time, copy, os, sys

def nrh_simulate(dset,year=None,show=True):

  assert "hedonicmodel" == "hedonicmodel" # should match!
  returnobj = {}
  t1 = time.time()
  
  # TEMPLATE configure table
  buildings = dset.building_filter(residential=0)
  # ENDTEMPLATE

  # TEMPLATE merge 
  t_m = time.time()
  buildings = pd.merge(buildings,dset.fetch('nodes'),**{u'right_index': True, u'left_on': u'_node_id'})
  print "Finished with merge in %f" % (time.time()-t_m)
  # ENDTEMPLATE
  
  print "Finished specifying in %f seconds" % (time.time()-t1)
  t1 = time.time()

  simrents = []
  
  # TEMPLATE creating segments
  segments = buildings.groupby([u'general_type'])
  # ENDTEMPLATE
    
  for name, segment in segments:
    outname = "nrh" if name is None else "nrh_"+name
    
    # TEMPLATE computing vars
    est_data = pd.DataFrame(index=segment.index)
    est_data["accessibility"] = (segment.nets_all_regional1_30.apply(np.log1p)).astype('float')
    est_data["reliability"] = (segment.nets_all_regional2_30.apply(np.log1p)).astype('float')
    est_data["ln_stories"] = (segment.stories.apply(np.log1p)).astype('float')
    est_data = sm.add_constant(est_data,prepend=False)
    est_data = est_data.fillna(0)
    # ENDTEMPLATE

      
    print "Generating rents on %d buildings" % (est_data.shape[0])
    vec = dset.load_coeff(outname)
    vec = np.reshape(vec,(vec.size,1))
    rents = est_data.dot(vec).astype('f4')
    rents = rents.apply(np.exp)
    simrents.append(rents[rents.columns[0]])
    returnobj[name] = misc.pandassummarytojson(rents.describe())
    rents.describe().to_csv(os.path.join(misc.output_dir(),"nrh_simulate.csv"))
      
  simrents = pd.concat(simrents)
  dset.buildings["nonresidential_rent"] = simrents.reindex(dset.buildings.index)
  dset.store_attr("nonresidential_rent",year,simrents)

  print "Finished executing in %f seconds" % (time.time()-t1)
  return returnobj