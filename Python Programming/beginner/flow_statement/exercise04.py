population_a = 80000
percent_growth_population_a = 0.03
population_b = 200000
percent_growth_population_b = 0.015
count_years = 0

# Calculating growthing of population A and B
while population_a < population_b:
    population_a = population_a + (population_a * percent_growth_population_a)
    population_b = population_b + (population_b * percent_growth_population_b)
    count_years += 1

print("Population A: %f " % population_a)
print("Population B: %f " % population_b)
print("Years: %d" % count_years)
