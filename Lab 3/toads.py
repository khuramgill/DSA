import random

class Toad:
    def __init__(self, is_trustworthy):
        self.is_truthful = bool(int(is_trustworthy))
        
    def is_trustworthy(self):
        return self.is_truthful

    def tell_about(self, other):
        other_is_trustworthy = other.is_trustworthy()
        
        if self.is_trustworthy():
            return other_is_trustworthy
        else:
            random_probability = random.random()
            return random_probability < 0.5

def generate_population(n):
    if n % 2 != 0:
        return None
    
    toads = []
    limit = n // 2
    
    count_truthful = 0
    while count_truthful <= limit :
        
        for i in range(n):
            is_trustworthy = random.randint(0, 1)
            toad = Toad(is_trustworthy)
            toads.append(toad)
        
        for toad in toads:
            if toad.is_trustworthy():
                count_truthful += 1
        
        if count_truthful > limit:
            break
        
        toads.clear()
        count_truthful = 0
    
    return toads

def Truthful_toads_A(population):
    truthful_indices = []
    for i in population:
        for j in population:
            first_toad = i.tell_about(j)
            if first_toad == j.is_trustworthy():
                truthful_indices.append(population.index(i))
                break
    
    del_indices = []
    for k in truthful_indices:
        if population[k].is_trustworthy():
            continue
        elif not population[k].is_trustworthy():
            del_indices.append(k)
                
    for m in del_indices:
        truthful_indices.pop(truthful_indices.index(m))
        
    return truthful_indices

population = generate_population(30)

def Truthful_toads_B(population):
    limit = len(population) // 2
    truthful_indices = []
    
    count = 0
    while count <= limit:
        first = population[count]
        second = population[count + 1]
        
        if first.tell_about(second) and first.is_trustworthy():
            truthful_indices.append(population.index(first))
                        
        count += 1

    if len(truthful_indices) < limit // 2:
        return None
    
    return truthful_indices
        
   
if __name__ == '__main__':
    
    print(f"TrustFull A: {Truthful_toads_A(population)}")
    print(f"TrustFull B: {Truthful_toads_B(population)}")
    
    # print(Truthful_toads_A(population))
    # print(Truthful_toads_B(population))
