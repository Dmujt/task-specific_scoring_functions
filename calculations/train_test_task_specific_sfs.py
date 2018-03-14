#!/usr/bin/env python

#-------------------------------------------------------------------------------
def get_ba_data(tr_df, task):
    """
    This function is used to replace task-specific dependent labels
    such as ligand poses RMSD values for docking with binding affinity
    data. In the data frame tr_df, valid binding affinity values for the
    docking task are associated with ligand poses whose RMSD = 0,
    which are essentially the native conformations ('label' == 0). The rows
    with BA data of positive values are the actual active ligands for
    the screening task ('label' > 0).
    """
    if task == 'dock':
      tr_df = tr_df[tr_df['label']==0].copy()
    elif task == 'screen':
        tr_df = tr_df[tr_df['label'] > 0].copy()
    tr_df['label'] = tr_df['ba'].copy()
    return tr_df
