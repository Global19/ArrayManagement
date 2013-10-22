import posixpath
from os.path import join, relpath
import pandas as pd

from arraymanagement import default_loader
from arraymanagement.nodes.hdfnodes import PandasCacheableTable
from arraymanagement.nodes import NodeContext

def get_sample2(context, factor=4):
    def _get_data():
        new_rpath = context.rpath(context.join_path('sample.csv'))
        
        
        data = pd.read_csv(fname, **self.config.get('csv_options'))
        data['values'] = data['values'] * 2
        return data
        
        
overrides = {'sample2' : }
old_keys = default_loader.keys

old_get_node = default_loader.get_node

class MyCSVNode(PandasCacheableTable):
    is_group = False
    def _get_data(self):

def get_node(key, context, overrides={}):
    if key == 'sample2':
        fname = "sample.csv"
        new_rpath = context.rpath(context.joinpath('sample.csv'))
        urlpath = context.joinurl(key)
        newcontext = context.clone(relpath=new_rpath, urlpath=urlpath)
        return MyCSVNode(newcontext)
    else:
        return old_get_node(key, context)

def keys(context, overrides={}):
    ks = old_keys(context)
    ks.append('sample2')
    return ks