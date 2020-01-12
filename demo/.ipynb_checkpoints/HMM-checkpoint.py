# -*- coding: utf-8 -*-
# * `_STATE = ['H','C']` 天氣種類
# * `_PI = {'H':.8, 'C'L.2}` initial state 機率
# * `_A = {'H':{'H':.7, 'C':.3}, 'C':{'H':.4, 'C':.6}}` initial state 機率
# * `_B={'H':{1:.2,2:.4,3:.4}, 'C':{1:.5,2:.4,3:.1} }` 是 Output Matrix
# * `p_aij(i, j) , p_bik(i, k) , p_pi(i)` 是 Model 和演算法的interface
# * `seq_probability(obs_init)` 是計算 sequence probability 的演算法

# # Brute force

# +
from functools import reduce 
import timeit
_STATE=['H','C'] # states
_PI={'H':.8, 'C':.2} # initial state
_A={ 'H':{'H':.7, 'C':.3 }, 'C':{'H':.4,'C':.6} } # transition matrix
_B={'H':{1:.2,2:.4,3:.4}, 'C':{1:.5,2:.4,3:.1} } # output matrix 

def p_aij(i, j):
    return _A[i][j]

def p_bik(i, k):
    return _B[i][k]

def p_pi(i):
    return _PI[i]

def seq_probability(obs_init):
    seq_val=[]; 
    def rec(obs, val_pre, qseq_pre):
        '''
        obs : 想要計算的observation probability
        val_pre : 初始化的機率計算值，用1表示神麼都沒乘
        qseq_pre : 該observation的前面幾個state，例如冷天，熱天，[C, H]
        '''
        if len(obs) >0:
            for q in _STATE:
                if len(qseq_pre) == 0 :
                    # val_pre : 上一個state所累積的total probability
                    # p_pi(q) : hidden state (q)
                    # p_bik : hidden state 對應到output的observation的probability
                    val = val_pre * p_pi(q) * p_bik(q, obs[0])
                else:
                    q_pre = qseq_pre[-1]
                    val = val_pre * p_aij(q_pre,q) * p_bik(q, obs[0])
                qseq = qseq_pre + [q]
                rec(obs[1:], val, qseq)
        else:
            seq_val.append((qseq_pre, val_pre))
    rec(obs_init, 1, [])
    
    for (seq,val) in seq_val:
        print( 'seq : %s , value : %s'%(seq, val))
    print('max_seq : %s  max_val : %s'%( reduce(lambda x1,x2: x2 if x2[1] > x1[1] else x1, seq_val)))


# -

# * 輸入冰淇淋的紀錄 (3,1,3), 程式會把每種可能的天氣序列都列出來，並求得最有可能者

# +
# import hmm
# hmm.seq_probability([3,1,3])

seq_probability([3,1,3])


# -

# # Viterbi

def brute_force_algo(obs_init, print_seq=False):
    start = timeit.default_timer()
    seq_val=[]; 
    def rec(obs, val_pre, qseq_pre):
        if len(obs) >0:
            for q in _STATE:
                if len(qseq_pre) == 0 :
                    val = val_pre * p_pi(q) * p_bik(q, obs[0])
                else:
                    q_pre = qseq_pre[-1]
                    val = val_pre * p_aij(q_pre,q) * p_bik(q, obs[0])
                qseq = qseq_pre + [q]
                rec(obs[1:], val, qseq)
        else:
            seq_val.append((qseq_pre, val_pre))
    rec(obs_init, 1, [])
    if print_seq:
        for (seq,val) in seq_val:
            print( 'seq : %s , value : %s'%(seq, val))
    print( 'result of brute_force_algo:')
    stop = timeit.default_timer()
    print( 'max_seq : %s  max_val : %s'%( 
          reduce(lambda x1,x2: x2 if x2[1] > x1[1] else x1, seq_val)))
    print( 'runtime : %s'%(stop - start ))


def viterbi_algo(obs_init, print_seq=False):
    start = timeit.default_timer()
    state_snapshot=[]
    def rec(obs, val_pre, qseq_pre):
        if len(obs) > 0:
            val = {}
            qseq = {}
            for q in _STATE:
                if len(val_pre) == 0:
                    val.update({ q:p_pi(q) * p_bik(q, obs[0]) })
                    qseq.update({q:[]})
                    state_snapshot.append(([q],val[q]))
                else:
                    val_temp = [( qseq_pre[q_pre]+[q_pre], 
                                val_pre[q_pre] * p_aij(q_pre,q) * p_bik(q, obs[0] )) 
                                for q_pre in _STATE ] 
                    max_q_seq = reduce(lambda x1,x2: x2 if x2[1] > x1[1] else x1, val_temp)
                    state_snapshot.append((max_q_seq[0]+[q],max_q_seq[1]))
                    val.update({ q:max_q_seq[1]  })
                    qseq.update({ q:max_q_seq[0] })
            return rec(obs[1:],val,qseq)
        else:
            val_temp =[( qseq_pre[q]+[q] , val_pre[q] ) for q in _STATE ] 
            max_q_seq = reduce(lambda x1,x2: x2 if x2[1] > x1[1] else x1, val_temp)
            return max_q_seq    
    seq,val = rec(obs_init, {},[])
    if print_seq:
        for (seq,val) in state_snapshot:
            print( 'seq : %s , value : %s'%(seq, val))
    print('result of viterbi_algo:')
    print('max_seq : %s , max_value : %s'%(seq, val))
    stop = timeit.default_timer()
    print( 'runtime : %s'%(stop - start ))


brute_force_algo([3,1,1],True)
viterbi_algo([3,1,1],True)

brute_force_algo([3,1,1,2]*4,False)
viterbi_algo([3,1,1,2]*4,False)


