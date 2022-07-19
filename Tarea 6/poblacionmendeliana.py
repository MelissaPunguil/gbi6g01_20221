def build_population(N, p):
    """La construccón de la población va de la siguiente manera:
    donde N representa el número de individuos, en este caso los pares de alelos y p significa número de ocurrencia o probalidad de de la
    población"""
    population = []
    for i in range(N):
        allele1 = "A"   
        if scipy.random.rand() > p:
            allele1 = "a"
        allele2 = "A"
        if scipy.random.rand() > p:
            allele2 = "a"
        population.append((allele1, allele2))
    return population

def compute_frequencies(population):
    """ El conteo de genotipos para posteriormente concoer cuantas generaciones se formaron"""
    AA = population.count(("A", "A"))
    Aa = population.count(("A", "a"))
    aA = population.count(("a", "A"))
    aa = population.count(("a", "a"))
    return({"AA": AA, "aa": aa, "Aa": Aa, "aA": aA})

def reproduce_population(population):
    """ La creación de la nueva genereación a traves de la población, es decir, de aquellos individuos de N. Aquí la descendencia recibe un
    cromosoma de cada uno de los padres """
    new_generation = []
    N = len(population)
    for i in range(N):
        # random integer between 0 and N-1
        dad = scipy.random.randint(N)
        mom = scipy.random.randint(N)
        # which chromosome comes from mom
        chr_mom = scipy.random.randint(2)
        offspring = (population[mom][chr_mom], population[dad][1 - chr_mom])
        #if offspring == ("a", "a"): 
          #next()
        new_generation.append(offspring)
    return new_generation