from moead_framework.aggregation import Tchebycheff
from moead_framework.algorithm.combinatorial import Moead
from moead_framework.problem.combinatorial import Rmnk
from moead_framework.tool.result import save_population


###############################
#   Initialize the problem    #
###############################
# Others instances are available here : https://github.com/moead-framework/data/tree/master/problem/RMNK/Instances
instance_file = "moead_framework/test/data/instances/rmnk_0_2_100_1_0.dat"
rmnk = Rmnk(instance_file=instance_file)


#####################################
#      Initialize the algorithm     #
#####################################
number_of_weight = 10
number_of_weight_neighborhood = 2
number_of_crossover_points = 4
number_of_evaluations = 1000
# Others weights files are available here : https://github.com/moead-framework/data/tree/master/weights
weight_file = "moead_framework/test/data/weights/SOBOL-" + str(rmnk.number_of_objective) + "objs-" + str(number_of_weight) + "wei.ws"



###############################
#    Execute the algorithm    #
###############################
moead = Moead(problem=rmnk,
              max_evaluation=number_of_evaluations,
              number_of_weight_neighborhood=number_of_weight_neighborhood,
              number_of_crossover_points=number_of_crossover_points,
              weight_file=weight_file,
              aggregation_function=Tchebycheff,
              )

population = moead.run()


###############################
#       Save the result       #
###############################
save_file = "moead-rmnk" + str(rmnk.number_of_objective) \
            + "-N" + str(number_of_weight) \
            + "-T" + str(number_of_weight_neighborhood) \
            + "-CP" + str(number_of_crossover_points) \
            + "-iter" + str(number_of_evaluations) \
            + ".txt"

save_population(save_file, population)

