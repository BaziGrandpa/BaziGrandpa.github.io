---
layout: page
title:  "Genetic Algorithm , Ant Colony Optimization and Particle Swarm Optimization"
subtitle: "How randomness is guided in optimization?"
date:   2025-1-1 21:21:21 +0530
categories: ["Stochastic Optimization"]
lang: "en"
---

Stochastic optimization algorithms have revolutionized the way we solve complex optimization problems. Unlike deterministic methods, they embrace randomness—but not blindly. 

Instead, their success lies in **guided randomness**, rather then completely **random search** the whole solution space, we carefully designed rules steer the search for optimal solutions. So it is useful when the solution space is too large and the system is too complex to be solved by deterministic methods.

In this blog, we'll explore the core principles behind some popular algorithms like Genetic Algorithms (GA), Ant Colony Optimization (ACO), and Particle Swarm Optimization (PSO) from the perspective of rules and guided randomness.



## What is Stochastic Optimization?
Stochastic optimization refers to a class of optimization methods that use randomness to search for solutions. The randomness helps:
- **Explore** diverse areas of the solution space.
- **Avoid** getting stuck in local optima.

But the randomness is **not completely random**—it is guided by **rules** tailored to the specific algorithm.



## The Importance of Rules in Stochastic Optimization
At the heart of every stochastic optimization algorithm are **rules**. These rules:
- Provide structure to the randomness.
- Guide the algorithm toward promising areas of the solution space.
- Balance **exploration** (searching new areas) and **exploitation** (refining known good areas).



## Guided Randomness in GA, ACO, and PSO

### 1. Genetic Algorithms (GA)
Inspired by the principles of natural selection, GA mimics the process of evolution, wher the fittest individuals are selected to produce offspring.

<img src="{{ "/assets/img/blog_25_1_1_1.png" | relative_url }}" alt="Alt text describing the image" style="width: 550px; height: auto; display: block; margin: auto;">

#### Key steps of GA
- **Encoding schemes**: Carefully design the **Encoding schemes** of a chromosome, which is the representation of the solution. And different **Encoding schemes** will lead to different mutation implementations. Usually, the chromosome is a **binary string**, all we need to do is to decode the binary string to the solution.
- **Fitness function**: Evaluate the fitness of each chromosome, which is the objective function we want to optimize. The fitness function is the key to the success of GA, it will determine the selection of the chromosomes. And also the fitness function is the **unique part** of the problem we want to solve. 

- **Selection**: this step is to select the chromosomes that will be used when **forming new individuals**, can be carried out in many different ways; the two most common are **roulette-wheel**(probability of selection is proportional to the fitness of the individual) 
selection and **tournament selection**(randomly select a few individuals and select the best one with a certain probability, with the probability, sometimes the **worse** one will be selected).
- **Crossover**: this step is to **combine** the genetic material of two parents to produce offspring. The crossover can be done in many different ways, the most common one is **single-point crossover**.
<img src="{{ "/assets/img/blog_25_1_1_2.png" | relative_url }}" alt="Alt text describing the image" style="width: 550px; height: auto; display: block; margin: auto;">

- **Mutation**: this step is to **introduce small random changes** to the offspring, to maintain diversity in the population. So that the algorithm can **explore** the solution space more efficiently.


#### Rules:
- **Selection**: Favor individuals with higher fitness to act as parents.
- **Crossover**: Combine genetic material from parents to create offspring.
- **Mutation**: Introduce small random changes to maintain diversity.

#### Guided Randomness:
- **Exploitation:**Fitness evaluation guides the selection of parents, Namely the whole population is guided by the individual with the highest fitness.
- **Exploration**:But mutation and crossover introduce randomness.




### 2. Ant Colony Optimization (ACO)
Modeled after the behavior of real-world ants finding the shortest paths to food. Ants will choose the path with the strongest pheromones with high probability, but also explore new paths with low probability.
And the problem being solved is not necessarily the shortest path problem, it can be any optimization problem, just need to disign the logical data strutcture of the problem to be like a graph.
<img src="{{ "/assets/img/blog_25_1_1_3.png" | relative_url }}" alt="Alt text describing the image" style="width: 550px; height: auto; display: block; margin: auto;">

#### Key steps of ACO
- **Initialization**: We usually initialize model the system as a graph, and will initialize the pheromones on the edges of the graph.

- **Probabilistic Path Selection**: in **step2**, ants will choose a edge base on the probability.
$\tau _{ij}$  denote the pheromone on the edge $i$ to $j$, $\eta _{ij}$ denote the heuristic information, which is the inverse of the distance between the two nodes. $\alpha$ and $\beta$ are the parameters to control the importance of the pheromone and the heuristic information. So the probability of choosing the edge $i$ to $j$ is $ \frac{\text{pheromones} \cdot \text{heuristic information}}{\sum \text{pheromones} \cdot \text{heuristic information}}$

- **Pheromone Update**: in **step3**, after an ant has finished the tour, we will update the pheromones on the edges it has traversed and store the pheromone into $\Delta \tau ^k$ 
. After all ants finish their journey, the pheromone update like $\tau _{ij} = (1-\rho) \cdot \tau _{ij} + \Delta \tau _{ij}$, where $\rho$ is the evaporation rate, and $\Delta \tau _{ij}$ is the pheromone the ant has left on the edge $i$ to $j$ by summing all the $\Delta \tau ^k$ of all the ants that has traversed the edge $i$ to $j$.

#### **Rules**:
- **Pheromone Update**: Ants leave pheromones on paths they traverse.
- **Probabilistic Path Selection**: Ants prefer paths with stronger pheromones but still explore new paths.
- **Evaporation**: Pheromone strength decreases over time to avoid over-concentration.

#### **Guided Randomness**:
- **Exploitation**: Ants follow paths with stronger pheromones.
- **Exploitation**: But they also explore new paths with low probability.



### 3. Particle Swarm Optimization (PSO)
Inspired by the social behavior of bird flocks or fish schools. Each particle(individual) adjusts its position based on its personal best, the global best, and a random factor to search the solution space.

<img src="{{ "/assets/img/blog_25_1_1_4.png" | relative_url }}" alt="Alt text describing the image" style="width: 550px; height: auto; display: block; margin: auto;">



#### Key steps of PSO

- **Initialization**: Initialize the position and velocity of each particle. Randomly distribute the particles in the solution space.

- **Update Velocity**: In each iteration, update the position and velocity of each particle based on the formula *4.1*, Two key concepts would be **personal best** and **swarm best**, **personal best** is the best position the particle has ever reached, and **swarm best** is the best position the **whole swarm** has ever reached. And the updated velocity is the combination of the **personal best**, **swarm best**, and a random factor.


#### **Rules**:
Each particle adjusts its position based on:
  - Its personal best position.
  - The swarm best position found by the swarm.
  - A random factor to maintain exploration.

#### **Guided Randomness**:
- **Exploitation**: Particles adjust their positions based on the best solutions found.
- **Exploration**: But they also explore new areas with random factors.



## Key takeaways
The power of stochastic optimization lies in its **rules** and **guided randomness**. Algorithms like GA, ACO, and PSO use randomness to explore, but they are driven by well-crafted rules that ensure efficiency and effectiveness. 
- **Genetic Algorithms (GA)**: Mimics the process of evolution by modeling the solution as a chromosome. And introduce randomness by mutation and crossover, guided by the fitness function to choose the best individuals and form new individuals.

- **Ant Colony Optimization (ACO)** : Modeled after the behavior of real-world ants finding the shortest paths to food, and introduce randomness by probabilistic path selection, guided by the pheromones on the edges of the graph.

- **Particle Swarm Optimization (PSO)**: Inspired by the social behavior of bird flocks or fish schools, and introduce randomness by updating the velocity of each particle, guided by the personal best, swarm best, and a random factor.


## References
- *Wahde, M. Biologically Inspired Optimization Methods: An Introduction. Chalmers University of Technology, Sweden, 2008.*