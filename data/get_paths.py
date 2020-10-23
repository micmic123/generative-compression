import pandas as pd
import os
import glob


for dir in ['train', 'test', 'val']:
   paths = glob.glob(os.path.expanduser(f'~/datasets/leftImg8bit/{dir}/*/**.png'))
  #  paths = glob.glob(os.path.expanduser(f'~/datasets/leftImg8bit_small/{dir}/*/**.png'))
   pd.DataFrame(paths, columns=['path']).to_hdf(f'./{dir}.h5', key='df')

# for dir in ['val']:
#     paths = glob.glob(os.path.expanduser(f'~/datasets/toy/{dir}/*/**.png'))
#     pd.DataFrame(paths, columns=['path']).to_hdf(f'./{dir}.h5', key='df')
