import sys
sys.path.append('../pfeature2')
from pfeature2.aac_wp import *
from pfeature2.dpc_wp import *
from pfeature2.bin_aa_wp import *
from pfeature2.bin_aa_nt import *
from pfeature2.bin_aa_ct import *
from pfeature2.bin_aa_rt import *
from pfeature2.bin_aa_st import *
from pfeature2.bin_di_ct import *
from pfeature2.bin_di_nt import *





dataset_dir = '../dataset/'
features_dir = '../features/'

def generate_aac_features():

    aac_wp(dataset_dir + 'pos_train', features_dir + 'aac/pos_train')
    aac_wp(dataset_dir + 'neg_train', features_dir + 'aac/neg_train')
    aac_wp(dataset_dir + 'pos_valid', features_dir + 'aac/pos_valid')
    aac_wp(dataset_dir + 'neg_valid', features_dir + 'aac/neg_valid')

def generate_dpc_features():
    dpc_wp(dataset_dir + 'pos_train', features_dir + 'dpc/pos_train', 0)
    dpc_wp(dataset_dir + 'neg_train', features_dir + 'dpc/neg_train', 0)
    dpc_wp(dataset_dir + 'pos_valid', features_dir + 'dpc/pos_valid', 0)
    dpc_wp(dataset_dir + 'neg_valid', features_dir + 'dpc/neg_valid', 0)


def generate_bin_features():
    bin_aa_wp(dataset_dir + 'pos_train', features_dir + 'bp/pos_train')
    bin_aa_wp(dataset_dir + 'neg_train', features_dir + 'bp/neg_train')
    bin_aa_wp(dataset_dir + 'pos_valid', features_dir + 'bp/pos_valid')
    bin_aa_wp(dataset_dir + 'neg_valid', features_dir + 'bp/neg_valid')


#  def generate_nt_features():
#     bin_aa_nt(dataset_dir + 'pos_train', features_dir + 'bp/nt/pos_train_n5', 5)
#     bin_aa_nt(dataset_dir + 'pos_train', features_dir + 'bp/nt/pos_train_n10', 10)
#     bin_aa_nt(dataset_dir + 'pos_train', features_dir + 'bp/nt/pos_train_n15', 15)
#
#     bin_aa_nt(dataset_dir + 'neg_train', features_dir + 'bp/nt/neg_train_n5', 5)
#     bin_aa_nt(dataset_dir + 'neg_train', features_dir + 'bp/nt/neg_train_n10', 10)
#     bin_aa_nt(dataset_dir + 'neg_train', features_dir + 'bp/nt/neg_train_n15', 15)
#
#     bin_aa_nt(dataset_dir + 'pos_valid', features_dir + 'bp/nt/pos_valid_n5', 5)
#     bin_aa_nt(dataset_dir + 'pos_valid', features_dir + 'bp/nt/pos_valid_n10', 10)
#     bin_aa_nt(dataset_dir + 'pos_valid', features_dir + 'bp/nt/pos_valid_n15', 15)
#
#     bin_aa_nt(dataset_dir + 'neg_valid', features_dir + 'bp/nt/neg_valid_n5', 5)
#     bin_aa_nt(dataset_dir + 'neg_valid', features_dir + 'bp/nt/neg_valid_n10', 10)
#     bin_aa_nt(dataset_dir + 'neg_valid', features_dir + 'bp/nt/neg_valid_n15', 15)
#
# def generate_ct_features():
#     bin_aa_ct(dataset_dir + 'pos_train', features_dir + 'bp/ct/pos_train_c5', 5)
#     bin_aa_ct(dataset_dir + 'pos_train', features_dir + 'bp/ct/pos_train_c10', 10)
#     bin_aa_ct(dataset_dir + 'pos_train', features_dir + 'bp/ct/pos_train_c15', 15)
#
#     bin_aa_ct(dataset_dir + 'neg_train', features_dir + 'bp/ct/neg_train_c5', 5)
#     bin_aa_ct(dataset_dir + 'neg_train', features_dir + 'bp/ct/neg_train_c10', 10)
#     bin_aa_ct(dataset_dir + 'neg_train', features_dir + 'bp/ct/neg_train_c15', 15)
#
#     bin_aa_ct(dataset_dir + 'pos_valid', features_dir + 'bp/ct/pos_valid_c5', 5)
#     bin_aa_ct(dataset_dir + 'pos_valid', features_dir + 'bp/ct/pos_valid_c10', 10)
#     bin_aa_ct(dataset_dir + 'pos_valid', features_dir + 'bp/ct/pos_valid_c15', 15)
#
#     bin_aa_ct(dataset_dir + 'neg_valid', features_dir + 'bp/ct/neg_valid_c5', 5)
#     bin_aa_ct(dataset_dir + 'neg_valid', features_dir + 'bp/ct/neg_valid_c10', 10)
#     bin_aa_ct(dataset_dir + 'neg_valid', features_dir + 'bp/ct/neg_valid_c15', 15)

def generate_rt_features():
    bin_aa_rt(dataset_dir + 'pos_train', features_dir + 'bp/rt/pos_train_r5', 5, 5)
    bin_aa_rt(dataset_dir + 'pos_train', features_dir + 'bp/rt/pos_train_r10', 10, 10)
    bin_aa_rt(dataset_dir + 'pos_train', features_dir + 'bp/rt/pos_train_r15', 15, 15)

    bin_aa_rt(dataset_dir + 'neg_train', features_dir + 'bp/rt/neg_train_r5', 5, 5)
    bin_aa_rt(dataset_dir + 'neg_train', features_dir + 'bp/rt/neg_train_r10', 10, 10)
    bin_aa_rt(dataset_dir + 'neg_train', features_dir + 'bp/rt/neg_train_r15', 15, 15)

    bin_aa_rt(dataset_dir + 'pos_valid', features_dir + 'bp/rt/pos_valid_r5', 5, 5)
    bin_aa_rt(dataset_dir + 'pos_valid', features_dir + 'bp/rt/pos_valid_r10', 10, 10)
    bin_aa_rt(dataset_dir + 'pos_valid', features_dir + 'bp/rt/pos_valid_r15', 15, 15)

    bin_aa_rt(dataset_dir + 'neg_valid', features_dir + 'bp/rt/neg_valid_r5', 5, 5)
    bin_aa_rt(dataset_dir + 'neg_valid', features_dir + 'bp/rt/neg_valid_r10', 10, 10)
    bin_aa_rt(dataset_dir + 'neg_valid', features_dir + 'bp/rt/neg_valid_r15', 15, 15)

def generate_split_features(split_factor):
    bin_aa_st(dataset_dir + 'pos_train', features_dir + 'bp/split/pos_train_s5', split_factor)
    bin_aa_st(dataset_dir + 'pos_train', features_dir + 'bp/split/pos_train_s10', split_factor)
    bin_aa_st(dataset_dir + 'pos_train', features_dir + 'bp/split/pos_train_s15', split_factor)

    bin_aa_st(dataset_dir + 'neg_train', features_dir + 'bp/split/neg_train_s5', split_factor)
    bin_aa_st(dataset_dir + 'neg_train', features_dir + 'bp/split/neg_train_s10', split_factor)
    bin_aa_st(dataset_dir + 'neg_train', features_dir + 'bp/split/neg_train_s15', split_factor)

    bin_aa_st(dataset_dir + 'pos_valid', features_dir + 'bp/split/pos_valid_s5', split_factor)
    bin_aa_st(dataset_dir + 'pos_valid', features_dir + 'bp/split/pos_valid_s10', split_factor)
    bin_aa_st(dataset_dir + 'pos_valid', features_dir + 'bp/split/pos_valid_s15', split_factor)
    #
    bin_aa_st(dataset_dir + 'neg_valid', features_dir + 'bp/split/neg_valid_s5', split_factor)
    bin_aa_st(dataset_dir + 'neg_valid', features_dir + 'bp/split/neg_valid_s10', split_factor)
    bin_aa_st(dataset_dir + 'neg_valid', features_dir + 'bp/split/neg_valid_s15', split_factor)

def generate_nt_features():
    bin_di_nt(dataset_dir + 'pos_train', features_dir + 'bp/nt/pos_train_n5', 5, 1)
    bin_di_nt(dataset_dir + 'pos_train', features_dir + 'bp/nt/pos_train_n10', 10, 1)
    bin_di_nt(dataset_dir + 'pos_train', features_dir + 'bp/nt/pos_train_n15', 15, 1)

    bin_di_nt(dataset_dir + 'neg_train', features_dir + 'bp/nt/neg_train_n5', 5, 1)
    bin_di_nt(dataset_dir + 'neg_train', features_dir + 'bp/nt/neg_train_n10', 10, 1)
    bin_di_nt(dataset_dir + 'neg_train', features_dir + 'bp/nt/neg_train_n15', 15, 1)

    bin_di_nt(dataset_dir + 'pos_valid', features_dir + 'bp/nt/pos_valid_n5', 5, 1)
    bin_di_nt(dataset_dir + 'pos_valid', features_dir + 'bp/nt/pos_valid_n10', 10, 1)
    bin_di_nt(dataset_dir + 'pos_valid', features_dir + 'bp/nt/pos_valid_n15', 15, 1)

    bin_di_nt(dataset_dir + 'neg_valid', features_dir + 'bp/nt/neg_valid_n5', 5, 1)
    bin_di_nt(dataset_dir + 'neg_valid', features_dir + 'bp/nt/neg_valid_n10', 10, 1)
    bin_di_nt(dataset_dir + 'neg_valid', features_dir + 'bp/nt/neg_valid_n15', 15, 1)

def generate_ct_features():
    bin_di_ct(dataset_dir + 'pos_train', features_dir + 'bp/ct/pos_train_c5', 5, 1)
    bin_di_ct(dataset_dir + 'pos_train', features_dir + 'bp/ct/pos_train_c10', 10, 1)
    bin_di_ct(dataset_dir + 'pos_train', features_dir + 'bp/ct/pos_train_c15', 15, 1)

    bin_di_ct(dataset_dir + 'neg_train', features_dir + 'bp/ct/neg_train_c5', 5, 1)
    bin_di_ct(dataset_dir + 'neg_train', features_dir + 'bp/ct/neg_train_c10', 10, 1)
    bin_di_ct(dataset_dir + 'neg_train', features_dir + 'bp/ct/neg_train_c15', 15, 1)

    bin_di_ct(dataset_dir + 'pos_valid', features_dir + 'bp/ct/pos_valid_c5', 5, 1)
    bin_di_ct(dataset_dir + 'pos_valid', features_dir + 'bp/ct/pos_valid_c10', 10, 1)
    bin_di_ct(dataset_dir + 'pos_valid', features_dir + 'bp/ct/pos_valid_c15', 15, 1)

    bin_di_ct(dataset_dir + 'neg_valid', features_dir + 'bp/ct/neg_valid_c5', 5, 1)
    bin_di_ct(dataset_dir + 'neg_valid', features_dir + 'bp/ct/neg_valid_c10', 10, 1)
    bin_di_ct(dataset_dir + 'neg_valid', features_dir + 'bp/ct/neg_valid_c15', 15, 1)

# generate_aac_features()
# generate_dpc_features()
# generate_bin_features()

generate_nt_features()
generate_ct_features()
# generate_rt_features()
# generate_split_features(5)
# bin_aa_ct(dataset_dir + 'neg_train', features_dir + 'bp/ct/neg_train_c5', 5)
