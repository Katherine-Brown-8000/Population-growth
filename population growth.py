import numpy as np

n_years = 300  # The number of years passing with these parameters
lifespan = 79
start_reproductive_age = 25
end_reproductive_age = 35
initial_population = 7e9
reproductive_rate = 1.25
mortality_rate = 0.05


def simulated_population_growth(
        n_years,
        lifespan,
        start_reproductive_age,
        end_reproductive_age,
        initial_population,
        reproductive_rate,
        mortality_rate,
):
    population = [initial_population] + [0] * (n_years - 1)
    age_distribution = [0] * lifespan
    age_distribution[0] = initial_population

    for year in range(1, n_years):
        new_offspring = 0

        for age in range(start_reproductive_age, end_reproductive_age):
            new_offspring += age_distribution[age] * reproductive_rate

        for age in range(lifespan - 1, 0, -1):
            age_distribution[age] = age_distribution[age - 1]

        age_distribution = [age * (1 - mortality_rate) for age in age_distribution]

        age_distribution[0] = new_offspring

        population[year] = sum(age_distribution)

    return population, age_distribution

population, age_distribution = simulated_population_growth(
    n_years,
    lifespan,
    start_reproductive_age,
    end_reproductive_age,
    initial_population,
    reproductive_rate,
    mortality_rate,
)

scientific_notation = [np.format_float_scientific(pop, precision=2) for pop in population]

print(f"Final population at year {n_years}: {population[-1]}")
print(f"Scientific notation {scientific_notation[-1]}")
