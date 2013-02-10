import genetic
#import custom_two_param_score
#import custom_one_param_score
import custom_data_score

#rf = genetic.getrankfunction(custom_two_param_score.buildhiddenset(), custom_two_param_score.scorefunction)
#print genetic.evolve(2, 500, rf, mutationrate = 0.2, breedingrate = 0.1, pexp = 0.7, pnew = 0.1).display()

#rf = genetic.getrankfunction(custom_one_param_score.buildhiddenset(), custom_one_param_score.scorefunction)
#print genetic.evolve(1, 500, rf, mutationrate = 0.2, breedingrate = 0.1, pexp = 0.7, pnew = 0.1).display()

rf = genetic.getrankfunction(custom_data_score.buildhiddenset(), custom_data_score.scorefunction)
print genetic.evolve(1, 500, rf, mutationrate = 0.2, breedingrate = 0.1, pexp = 0.7, pnew = 0.1).display()
