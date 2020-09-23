import pathlib
current_file = pathlib.Path(__file__).parent.absolute()
import os
path_to_env = os.path.join(current_file,'..')
import sys
sys.path.insert(1,path_to_env)
from env import ABM
ABC_path = os.path.join(current_file,'..','..','..','FFD/FFD')
sys.path.insert(1,ABC_path)
import tools


settings = {
	"MPI_flag": True,
    "replica_n": 2,
	"output_path": "outputs",
	"model":ABM
}
free_params = {
	## the controller's params
	# "MG_L_t": [2,10],
	# "MG_M_t": [5,15],
	## un checked
	"maturity_t": [0.6,1],
	"a_Diff": [1,5],
	"a_m_OC": [0.5,1],
	"a_m_ALP": [0.5,1],
	"c_weight":[0.0001,0.001],
	"CD_H_t": [0.67,1],
	# "B_Mo": [0.00005,0.00017],
	# "a_Mo": [10,30],
	"a_c_Mo": [5,20],
	# "b_BMP": [0.001,0.005],
	# "b_TGF": [0.01,0.05],
	# "B_Pr": [0.021,0.083],
	"MG_H_t": [20,40],
	"pH_t": [8.5,9.5],
	# "a_TGF_nTGF":[0.067,0.2],
	"a_BMP_nBMP":[0.033,0.1]
}
# free_params = {
# 	"CD_H_t": [0.67,1],
# 	"B_Pr": [0.021,0.083],
# 	"c_weight":[0.0000006,0.000006],
# 	"b_TGF": [0.01,0.05],
# 	"a_m_OC": [0.5,1],
# 	"a_m_ALP": [0.5,1]
# }
if __name__ == "__main__":
	sa_obj = tools.SA(free_params,settings)
	sa_obj.sample()
	sa_obj.run()
	sa_obj.postprocessing()

