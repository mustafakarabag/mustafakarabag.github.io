---
layout: archive
title: ""
permalink: /projects-publications/
---

# Planning in Adversarial Domains ([Relevant publications](#adversarialpublications))
 
# Planning in Information-Scarce Domains ([Relevant publications](#informationscarcepublications))

# Conveying Information via Behavior ([Relevant publications](#conveyinformationpublications))

<a name="adversarialpublications"></a>


<a name="deceptionpublications"></a>



### Deception in Supervisory Control

**Mustafa O. Karabag**, Melkior Ornik, and Ufuk Topcu<br><span style="font-size:12pt">IEEE Transactions on Automatic Control (TAC)</span><br>

[Paper](https://ieeexplore.ieee.org/iel7/9/4601496/09351619.pdf)

<img 
src="/images/TACDec1.png" 
width=400 
style="float: right; margin-left: 10px; margin-right: 10px;">

**Abstract:** The use of deceptive strategies is important for an agent that attempts not to reveal his intentions in an adversarial environment. We consider a setting, in which a supervisor provides a reference policy and expects an agent to follow the reference policy and perform a task. The agent may instead follow a different deceptive policy to achieve a different task. We model the environment and the behavior of the agent with a Markov decision process, represent the tasks of the agent and the supervisor with reachability specifications, and study the synthesis of optimal deceptive policies for such agents. We also study the synthesis of optimal reference policies that prevent deceptive strategies of the agent and achieve the supervisor's task with high probability. We show that the synthesis of optimal deceptive policies has a convex optimization problem formulation, while the synthesis of optimal reference policies requires solving a nonconvex optimization problem. We also show that the synthesis of optimal reference policies is NP-hard.

---

### Exploiting Partial Observability for Optimal Deception

**Mustafa O. Karabag**, Melkior Ornik, and Ufuk Topcu<br><span style="font-size:12pt">  IEEE Transactions on Automatic Control</span><br>

[Paper](https://ieeexplore.ieee.org/iel7/9/4601496/09904305.pdf)

<img 
src="/images/TACDec2.png" 
width=400 
style="float: right; margin-left: 10px; margin-right: 10px;">

**Abstract:** 
Deception is a useful tool in situations where an agent operates in the presence of its adversaries. We consider a setting where a supervisor provides a reference policy to an agent, expects the agent to operate in an environment by following the reference policy, and partially observes the agent's behavior. The agent instead follows a different deceptive policy to achieve a different task. We model the environment with a Markov decision process and study the synthesis of optimal deceptive policies under partial observability. We formalize the notion of deception as a hypothesis testing problem and show that the synthesis of optimal deceptive policies is nondeterministic polynomial-time hard (NP-hard). As an approximation, we consider the class of mixture policies, which provides a convex optimization formulation of the deception problem. We give an algorithm that converges to the optimal mixture policy. We also consider a special class of Markov decision processes where the transition and observation functions are deterministic. For this case, we give a randomized algorithm for path planning that generates a path for the agent in polynomial time and achieves the optimal value for the considered objective function.

---

### Identity Concealment Games: How I Learned to Stop Revealing and Love the Coincidences

**Mustafa O. Karabag**, Melkior Ornik, and Ufuk Topcu<br><span style="font-size:12pt">Under review at Automatica</span><br>

[Paper](https://arxiv.org/pdf/2105.05377)

<img 
src="/images/Automatica2023.png" 
width=400 
style="float: right; margin-left: 10px; margin-right: 10px;">

**Abstract:** 
In an adversarial environment, a hostile player performing a task may behave like a non-hostile one in order not to reveal its identity to an opponent. To model such a scenario, we define identity concealment games: zero-sum stochastic reachability games with a zero-sum objective of identity concealment. To measure the identity concealment of the player, we introduce the notion of an average player. The average player's policy represents the expected behavior of a non-hostile player. We show that there exists an equilibrium policy pair for every identity concealment game and give the optimality equations to synthesize an equilibrium policy pair. If the player's opponent follows a non-equilibrium policy, the player can hide its identity better. For this reason, we study how the hostile player may learn the opponent's policy. Since learning via exploration policies would quickly reveal the hostile player's identity to the opponent, we consider the problem of learning a near-optimal policy for the hostile player using the game runs collected under the average player's policy. Consequently, we propose an algorithm that provably learns a near-optimal policy and give an upper bound on the number of sample runs to be collected.

---

### Deceptive Planning for Resource Allocation

Yagiz Savas, **Mustafa O. Karabag**, Brian Sadler, and Ufuk Topcu<br><span style="font-size:12pt">  Preprint</span><br> 

[Paper](https://arxiv.org/pdf/2206.01306.pdf), [Code](https://github.com/mustafakarabag/resource-deception)

<img 
src="/images/resourcealloc-.png" 
width=400 
style="float: right; margin-left: 10px; margin-right: 10px;">

**Abstract:** 
We consider a team of autonomous agents that navigate in an adversarial environment and aim to achieve a task by allocating their resources over a set of target locations. The adversaries in the environment observe the autonomous team's behavior to infer their objective and counter-allocate their own resources to the target locations. In this setting, we develop strategies for controlling the density of the autonomous team so that they can deceive the adversaries regarding their objective while achieving the desired final resource allocation. We first develop a prediction algorithm, based on the principle of maximum entropy, to express the team's behavior expected by the adversaries. Then, by measuring the deceptiveness via Kullback-Leibler divergence, we develop convex optimization-based planning algorithms that deceives adversaries by either exaggerating the behavior towards a decoy allocation strategy or creating ambiguity regarding the final allocation strategy. Finally, we illustrate the performance of the proposed algorithms through numerical simulations.



---


### Simulator-Driven Deceptive Control via Path Integral Approach

Apurva Patil<sup>*</sup>, **Mustafa O. Karabag**<sup>*</sup>, Takashi Tanaka, Ufuk Topcu<br><span style="font-size:12pt">IEEE Conference on Decision and Control (CDC) 2023</span><br> <span style="font-size:10pt;"> <sup>*</sup> indicates equal contribution. </span>

[Paper](https://arxiv.org/pdf/2308.14092)

<img 
src="/images/CDC2023Deception.png" 
width=400 
style="float: right; margin-left: 10px; margin-right: 10px;">

**Abstract:** 
We consider a setting where a supervisor delegates an agent to perform a certain control task, while the agent is incentivized to deviate from the given policy to achieve its own goal. In this work, we synthesize the optimal deceptive policies for an agent who attempts to hide its deviations from the supervisor's policy. We study the deception problem in the continuous-state discrete-time stochastic dynamics setting and, using motivations from hypothesis testing theory, formulate a Kullback-Leibler control problem for the synthesis of deceptive policies. This problem can be solved using backward dynamic programming in principle, which suffers from the curse of dimensionality. However, under the assumption of deterministic state dynamics, we show that the optimal deceptive actions can be generated using path integral control. This allows the agent to numerically compute the deceptive actions via Monte Carlo simulations. Since Monte Carlo simulations can be efficiently parallelized, our approach allows the agent to generate deceptive control actions online. We show that the proposed simulation-driven control approach asymptotically converges to the optimal control distribution.

---

### Optimal Deceptive and Reference Policies for Supervisory Control

**Mustafa O. Karabag**, Melkior Ornik, and Ufuk Topcu<br><span style="font-size:12pt">IEEE Conference on Decision and Control (CDC) 2019</span><br>

[Paper](https://ieeexplore.ieee.org/iel7/8977134/9028853/09029607.pdf)

<img 
src="/images/CDC2019.png" 
width=400 
style="float: right; margin-left: 10px; margin-right: 10px;">

**Abstract:** The use of deceptive strategies is important for an agent that attempts not to reveal his intentions in an adversarial environment. We consider a setting in which a supervisor provides a reference policy and expects an agent to follow the reference policy and perform a task. The agent may instead follow a different, deceptive policy to achieve a different task. We model the environment and the behavior of the agent with a Markov decision process, represent the tasks of the agent and the supervisor with linear temporal logic formulae, and study the synthesis of optimal deceptive policies for such agents. We also study the synthesis of optimal reference policies that prevents deceptive strategies of the agent and achieves the supervisor's task with high probability. We show that the synthesis of deceptive policies has a convex optimization problem formulation, while the synthesis of reference policies requires solving a nonconvex optimization problem.

---

### Differential Privacy in Cooperative Multiagent Planning
<a name="privacypublications"></a>

Bo Chen, Calvin Hawkins, **Mustafa O. Karabag**, Cyrus Neary, Matthew Hale and Ufuk Topcu<br><span style="font-size:12pt">Uncertainty in Artificial Intelligence (UAI) 2023</span><br> 

[Paper](https://proceedings.mlr.press/v216/chen23e/chen23e.pdf), [Code](https://github.com/cyrusneary/differential_privacy_in_mas)

<img 
src="/images/UAI2023.png" 
width=400 
style="float: right; margin-left: 10px; margin-right: 10px;">

**Abstract:** 
Privacy-aware multiagent systems must protect agents' sensitive data while simultaneously ensuring that agents accomplish their shared objectives. Towards this goal, we propose a framework to privatize inter-agent communications in cooperative multiagent decision-making problems. We study sequential decision-making problems formulated as cooperative Markov games with reach-avoid objectives. We apply a differential privacy mechanism to privatize agents' communicated symbolic state trajectories, and then we analyze tradeoffs between the strength of privacy and the team's performance. For a given level of privacy, this tradeoff is shown to depend critically upon the total correlation among agents' state-action processes. We synthesize policies that are robust to privacy by reducing the value of the total correlation. Numerical experiments demonstrate that the team's performance under these policies decreases by only 3 percent when comparing private versus non-private implementations of communication. By contrast, the team's performance decreases by roughly 86 percent when using baseline policies that ignore total correlation and only optimize team performance.

---
### Least Inferable Policies for Markov Decision Processes
<a name="inferabilitypublications"></a>

**Mustafa O. Karabag**, Melkior Ornik, and Ufuk Topcu<br><span style="font-size:12pt">American Control Conference 2019</span><br>

[Paper](https://ieeexplore.ieee.org/iel7/8789884/8814292/08815129.pdf)


<img 
src="/images/ACC2018.png" 
width=400 
style="float: right; margin-left: 10px; margin-right: 10px;">

**Abstract:** In a variety of applications, an agent's success depends on the knowledge that an adversarial observer has or can gather about the agent's decisions. It is therefore desirable for the agent to achieve a task while reducing the ability of an observer to infer the agent's policy. We consider the task of the agent as a reachability problem in a Markov decision process and study the synthesis of policies that minimize the observer's ability to infer the transition probabilities of the agent between the states of the Markov decision process. We introduce a metric that is based on the Fisher information as a proxy for the information leaked to the observer and using this metric formulate a problem that minimizes expected total information subject to the reachability constraint. We proceed to solve the problem using convex optimization methods. To verify the proposed method, we analyze the relationship between the expected total information and the estimation error of the observer, and show that, for a particular class of Markov decision processes, these two values are inversely proportional.

---


### Entropy Maximization for Markov Decision Processes Under Temporal Logic Constraints
<a name="randomnesspublications"></a>

Yagiz Savas, Melkior Ornik, Murat Cubuktepe, **Mustafa O. Karabag**, Ufuk Topcu<br><span style="font-size:12pt">IEEE Transactions on Automatic Control (TAC)</span><br>

[Paper](https://ieeexplore.ieee.org/iel7/9/4601496/08735817.pdf)

<img 
src="/images/TAC2019.png" 
width=400 
style="float: right; margin-left: 10px; margin-right: 10px;">

**Abstract:** We study the problem of synthesizing a policy that maximizes the entropy of a Markov decision process (MDP) subject to a temporal logic constraint. Such a policy minimizes the predictability of the paths it generates, or dually, maximizes the exploration of different paths in an MDP while ensuring the satisfaction of a temporal logic specification. We first show that the maximum entropy of an MDP can be finite, infinite, or unbounded. We provide necessary and sufficient conditions under which the maximum entropy of an MDP is finite, infinite, or unbounded. We then present an algorithm which is based on a convex optimization problem to synthesize a policy that maximizes the entropy of an MDP. We also show that maximizing the entropy of an MDP is equivalent to maximizing the entropy of the paths that reach a certain set of states in the MDP. Finally, we extend the algorithm to an MDP subject to a temporal logic specification. In numerical examples, we demonstrate the proposed method on different motion planning scenarios and illustrate the relation between the restrictions imposed on the paths by a specification, the maximum entropy, and the predictability of paths.



---
<a name="informationscarcepublications"></a>

### Planning Not to Talk: Multiagent Systems that are Robust to Communication Loss
<a name="communicationpublications"></a>

**Mustafa O. Karabag**<sup>*</sup>, Cyrus Neary<sup>*</sup>, and Ufuk Topcu<br><span style="font-size:12pt"> International Conference on Autonomous Agents and Multiagent Systems (AAMAS) 2022</span><br> <span style="font-size:10pt;"> <sup>*</sup> indicates equal contribution. </span>

[Paper](https://ifaamas.org/Proceedings/aamas2022/pdfs/p705.pdf), [Code](https://github.com/cyrusneary/multi-agent-comms)

<img 
src="/images/AAMAS.png" 
width=400 
style="float: right; margin-left: 10px; margin-right: 10px;">

**Abstract:** 
In a cooperative multiagent system, a collection of agents executes a joint policy in order to achieve some common objective. The successful deployment of such systems hinges on the availability of reliable inter-agent communication. However, many sources of potential disruption to communication exist in practice, such as radio interference, hardware failure, and adversarial attacks. In this work, we develop joint policies for cooperative multiagent systems that are robust to potential losses in communication. More specifically, we develop joint policies for cooperative Markov games with reach-avoid objectives. First, we propose an algorithm for the decentralized execution of joint policies during periods of communication loss. Next, we use the total correlation of the state-action process induced by a joint policy as a measure of the intrinsic dependencies between the agents. We then use this measure to lower-bound the performance of a joint policy when communication is lost. Finally, we present an algorithm that maximizes a proxy to this lower bound in order to synthesize minimum-dependency joint policies that are robust to communication loss. Numerical experiments show that the proposed minimum-dependency policies require minimal coordination between the agents while incurring little to no loss in performance; the total correlation value of the synthesized policy is one fifth of the total correlation value of the baseline policy which does not take potential communication losses into account. As a result, the performance of the minimum-dependency policies remains consistently high regardless of whether or not communication is available. By contrast, the performance of the baseline policy decreases by twenty percent when communication is lost.

---

### Smooth Convex Optimization Using Sub-Zeroth-Order Oracles
<a name="optimizationpublications"></a>

**Mustafa O. Karabag**, Cyrus Neary, and Ufuk Topcu<br><span style="font-size:12pt"> AAAI Conference on Artificial Intelligence 2021</span><br> 

[Paper](https://ojs.aaai.org/index.php/AAAI/article/download/16499/16306)

<img 
src="/images/AAAI2021-.png" 
width=400 
style="float: right; margin-left: 10px; margin-right: 10px;">

**Abstract:** 
We consider the problem of minimizing a smooth, Lipschitz, convex function over a compact, convex set using sub-zeroth-order oracles: an oracle that outputs the sign of the directional derivative for a given point and a given direction, an oracle that compares the function values for a given pair of points, and an oracle that outputs a noisy function value for a given point. We show that the sample complexity of optimization using these oracles is polynomial in the relevant parameters. The optimization algorithm that we provide for the comparator oracle is the first algorithm with a known rate of convergence that is polynomial in the number of dimensions. We also give an algorithm for the noisy-value oracle that incurs sublinear regret in the number of queries and polynomial regret in the number of dimensions.


---

### Scenario-Game ADMM: A Parallelized Scenario-Based Solver for Stochastic Noncooperative Games
<a name="uncertainitypublications"></a>

Jingqi Li, Chih-Yuan Chiu, Lasse Peters, Fernando Palafox, **Mustafa O. Karabag**, Javier Alonso-Mora, Somayeh Sojoudi, Claire Tomlin, and David Fridovich-Keil<br><span style="font-size:12pt">IEEE Conference on Decision and Control (CDC) 2023</span><br> 

[Paper](https://arxiv.org/pdf/2304.01945)

<img 
src="/images/CDC2023Scenario-.png" 
width=400 
style="float: right; margin-left: 10px; margin-right: 10px;">

**Abstract:** 
Decision making in multi-agent games can be extremely challenging, particularly under uncertainty. In this work, we propose a new sample-based approximation to a class of stochastic, general-sum, pure Nash games, where each player has an expected-value objective and a set of chance constraints. This new approximation scheme inherits the accuracy of objective approximation from the established sample average approximation (SAA) method and enjoys a feasibility guarantee derived from the scenario optimization literature. We characterize the sample complexity of this new game-theoretic approximation scheme, and observe that high accuracy usually requires a large number of samples, which results in a large number of sampled constraints. To accommodate this, we decompose the approximated game into a set of smaller games with few constraints for each sampled scenario, and propose a decentralized, consensus ADMM algorithm to efficiently compute a generalized Nash equilibrium of the approximated game. We prove the convergence of our algorithm and empirically demonstrate superior performance relative to a recent baseline.


---

### On the Sample Complexity of Vanilla Model-Based Offline Reinforcement Learning with Dependent Samples
<a name="offlinedatapublications"></a>

Mustafa O. Karabag and Ufuk Topcu<br><span style="font-size:12pt">AAAI Conference on Artificial Intelligence 2023</span><br> 

[Paper](https://ojs.aaai.org/index.php/AAAI/article/view/25989/25761)

<img 
src="/images/AAAI2023.png" 
width=300 
style="float: right; margin-left: 10px; margin-right: 10px;">

**Abstract:** 
Offline reinforcement learning (offline RL) considers problems where learning is performed using only previously collected samples and is helpful for the settings in which collecting new data is costly or risky. In model-based offline RL, the learner performs estimation (or optimization) using a model constructed according to the empirical transition frequencies. We analyze the sample complexity of vanilla model-based offline RL with dependent samples in the infinite-horizon discounted-reward setting. In our setting, the samples obey the dynamics of the Markov decision process and, consequently, may have interdependencies. Under no assumption of independent samples, we provide a high-probability, polynomial sample complexity bound for vanilla model-based off-policy evaluation that requires partial or uniform coverage. We extend this result to the off-policy optimization under uniform coverage. As a comparison to the model-based approach, we analyze the sample complexity of off-policy evaluation with vanilla importance sampling in the infinite-horizon setting. Finally, we provide an estimator that outperforms the sample-mean estimator for almost deterministic dynamics that are prevalent in reinforcement learning.

---
<a name="conveyinformationpublications"></a>



### Encouraging Inferable Behavior for Autonomy: Repeated Bimatrix Stackelberg Games with Observations

<a name="offlinedatapublications"></a>

Mustafa O. Karabag, Sophia Smith, David Fridovich-Keil, and Ufuk Topcu<br><span style="font-size:12pt">Under review</span><br> 

[Paper](https://arxiv.org/pdf/2310.00468.pdf)

**Abstract:** 
When interacting with other non-competitive decision-making agents, it is critical for an autonomous agent to have inferable behavior: Their actions must convey their intention and strategy. For example, an autonomous car's strategy must be inferable by the pedestrians interacting with the car. We model the inferability problem using a repeated bimatrix Stackelberg game with observations where a leader and a follower repeatedly interact. During the interactions, the leader uses a fixed, potentially mixed strategy. The follower, on the other hand, does not know the leader's strategy and dynamically reacts based on observations that are the leader's previous actions. In the setting with observations, the leader may suffer from an inferability loss, i.e., the performance compared to the setting where the follower has perfect information of the leader's strategy. We show that the inferability loss is upper-bounded by a function of the number of interactions and the stochasticity level of the leader's strategy, encouraging the use of inferable strategies with lower stochasticity levels. As a converse result, we also provide a game where the required number of interactions is lower bounded by a function of the desired inferability loss.





