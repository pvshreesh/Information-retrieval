import os
import time

import numpy as np
import pandas as pd

from data_handling import CleanData
from svd import SVDAlgorithm
from error_funcs import *
from cur import *
from collaborative_filtering import *

def rcf(M):
    start = time.time()
    m = M[200:300, 150:250].T
    cf = Collaborate(m.T)
    m_p = cf.comp()
    print("Collaborative Filtering Time: " +str(time.time() - start))
    print("RMSE Collaborative Filtering: " + str(rmse(m, m_p.T)))
    print("Top K precision Collaborative Filtering: " + str(top_k(40, m, m_p.T)))
    print("Spearman correlation Collaborative Filtering: " + str(spearman_correlation(m, m_p.T)))

def rcfBaseline(M):
    start = time.time()
    m = M[200:250, 150:200]
    cfb = Collaborate(m.T)
    m_p = cfb.comp(baseline=True)
    print("Collaborative Filtering with baseline Time: " +str(time.time() - start))
    print("RMSE Collaborative Filtering with baseline: " + str(rmse(m, m_p.T)))
    print("Top K precision Collaborative Filtering with baseline: " + str(top_k(40, m, m_p.T)))
    print("Spearman correlation Collaborative Filtering with baseline: " + str(spearman_correlation(m, m_p.T)))

def rsvd(M):
    s = SVDAlgorithm()
    svd_start = time.time()
    U, sigma, V = s.svd(M, dimension_reduction=1.0)
    M_p = np.dot(np.dot(U, sigma), V)
    print("SVD Time: " +str(time.time() - svd_start))
    print("RMSE SVD: " + str(rmse(M, M_p)))
    print("Top K precision SVD: " + str(top_k(40, M, M_p)))
    print("Spearman correlation SVD: " + str(spearman_correlation(M, M_p)))

def rsvdReduce(M):
    s = SVDAlgorithm()
    svd_reduce_start = time.time()
    U, sigma, V = s.svd(M, dimension_reduction=0.9)
    M_p = np.dot(np.dot(U, sigma), V)
    print("SVD Reduction Time: " +str(time.time() - svd_reduce_start))
    print("RMSE Reduction SVD: " + str(rmse(M, M_p)))
    print("Top K precision SVD Reduction: " + str(top_k(40, M, M_p)))
    print("Spearman correlation SVD Reduction: " + str(spearman_correlation(M, M_p)))

def rcur(M):
    cur_start = time.time()
    M_p = cur(M, 600, 600, repeat=False)
    print("CUR Time: " +str(time.time() - cur_start))
    print("RMSE CUR: " + str(rmse(M, M_p)))
    print("Top K precision CUR: " + str(top_k(40, M, M_p)))
    print("Spearman correlation CUR: " + str(spearman_correlation(M, M_p)))

def rcurReduce(M):
    cur_reduce_start = time.time()
    M_p = cur(M, 600, 600, dim_red=0.9, repeat=True)
    print("CUR Reduction Time: " +str(time.time() - cur_reduce_start))
    print("RMSE Reduction CUR: " + str(rmse(M, M_p)))
    print("Top K precision CUR Reduction: " + str(top_k(40, M, M_p)))
    print("Spearman correlation CUR Reduction: " + str(spearman_correlation(M, M_p)))


if __name__=="__main__":
    formated_dataset = False
    for files in os.listdir('.'):
        if str(files).endswith('.npy') or str(files).endswith('.csv'):
            print("Formatted dataset already exists.")
            formated_dataset = True
            break

    M = np.load('meta.npy')
    rcf(M)
    rcfBaseline(M)
    rsvd(M)
    rsvdReduce(M)
    rcur(M)
    rcurReduce(M)
