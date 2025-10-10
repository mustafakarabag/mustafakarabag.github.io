---
layout: archive
title: ""
permalink: /projects-publications/
---



**Tags:** #[bargaining](tags/bargaining.md)  #[communication](tags/communication.md)  #[computational hardness](tags/computational-hardness.md)  #[deception](tags/deception.md)  #[estimation theory](tags/estimation-theory.md)  #[formal methods](tags/formal-methods.md)  #[games](tags/games.md)  #[information concealment](tags/information-concealment.md)  #[information theory](tags/information-theory.md)  #[large language models](tags/large-language-models.md)  #[learning](tags/learning.md)  #[limited information](tags/limited-information.md)  #[multiagent systems](tags/multiagent-systems.md)  #[multiarmed bandits](tags/multiarmed-bandits.md)  #[optimization](tags/optimization.md)  #[perception](tags/perception.md)  #[privacy](tags/privacy.md)  #[security](tags/security.md)  #[sequential decision-making](tags/sequential-decision-making.md)
<hr style='border: 1px solid black; margin: 20px 0;'>

# Preprints

### Sequential Resource Trading Using Comparison-Based Gradient Estimation

Surya Murthy, **Mustafa O. Karabag**, Ufuk Topcu  
*Preprint, 2025*  

[Paper](https://arxiv.org/pdf/2408.11186)

<details markdown="1">
<summary markdown="span">**Show abstract**</summary>

Autonomous agents interact with other autonomous agents and humans of unknown preferences to share resources in their environment. We explore sequential trading for resource allocation in a setting where two greedily rational agents sequentially trade resources from a finite set of categories. Each agent has a utility function that depends on the amount of resources it possesses in each category. The offering agent makes trade offers to improve its utility without knowing the responding agent's utility function, and the responding agent only accepts offers that improve its utility. To facilitate cooperation between an autonomous agent and another autonomous agent or a human, we present an algorithm for the offering agent to estimate the responding agent's gradient (preferences) and make offers based on previous acceptance or rejection responses. The algorithm's goal is to reach a Pareto-optimal resource allocation state while ensuring that the utilities of both agents improve after every accepted trade. The algorithm estimates the responding agent's gradient by leveraging the rejected offers and the greedy rationality assumption, to prune the space of potential gradients. We show that, after the algorithm makes a finite number of rejected offers, the algorithm either finds a mutually beneficial trade or certifies that the current state is epsilon-weakly Pareto optimal. We compare the proposed algorithm against various baselines in continuous and discrete trading scenarios and show that it improves the societal benefit with fewer offers. Additionally, we validate these findings in a user study with human participants, where the algorithm achieves high performance in scenarios with high resource conflict due to aligned agent goals.

</details>



#[large language models](tags/large-language-models/) #[limited information](tags/limited-information/) #[multiagent systems](tags/multiagent-systems/) #[optimization](tags/optimization/)

<hr style='border: 1px solid black; margin: 20px 0;'>


### Do LLMs Strategically Reveal, Conceal, and Infer Information? A Theoretical and Empirical Analysis in The Chameleon Game

**Mustafa O. Karabag**, Ufuk Topcu  
*Preprint, 2025*  

[Paper](https://arxiv.org/pdf/2501.19398)

<details markdown="1">
<summary markdown="span">**Show abstract**</summary>

Large language model-based (LLM-based) agents have become common in settings that include non-cooperative parties. In such settings, agents' decision-making needs to conceal information from their adversaries, reveal information to their cooperators, and infer information to identify the other agents' characteristics. To investigate whether LLMs have these information control and decision-making capabilities, we make LLM agents play the language-based hidden-identity game, The Chameleon. In the game, a group of non-chameleon agents who do not know each other aim to identify the chameleon agent without revealing a secret. The game requires the aforementioned information control capabilities both as a chameleon and a non-chameleon. The empirical results show that while non-chameleon LLM agents identify the chameleon, they fail to conceal the secret from the chameleon, and their winning probability is far from the levels of even trivial strategies. To formally explain this behavior, we give a theoretical analysis for a spectrum of strategies, from concealing to revealing, and provide bounds on the non-chameleons' winning probability.  Based on the empirical results and theoretical analysis of different strategies, we deduce that LLM-based non-chameleon agents reveal excessive information to agents of unknown identities. Our results point to a weakness of contemporary LLMs, including GPT-4, GPT-4o, Gemini 1.5, and Claude 3.5 Sonnet, in strategic interactions.

</details>



#[games](tags/games/) #[information concealment](tags/information-concealment/) #[large language models](tags/large-language-models/) #[multiagent systems](tags/multiagent-systems/)

<hr style='border: 1px solid black; margin: 20px 0;'>


### Deceptive Sequential Decision-Making via Regularized Policy Optimization

Yerin Kim, Alexander Benvenuti, Bo Chen, **Mustafa O. Karabag**, Abhishek Kulkarni, Nathaniel D. Bastian, Ufuk Topcu, Matthew Hale  
*Preprint, 2025*  

[Paper](https://arxiv.org/abs/2501.18803)

<details markdown="1">
<summary markdown="span">**Show abstract**</summary>

Autonomous systems are increasingly expected to operate in the presence of adversaries, though an adversary may infer sensitive information simply by observing a system, without even needing to interact with it. Therefore, in this work we present a deceptive decision-making framework that not only conceals sensitive information, but in fact actively misleads adversaries about it. We model autonomous systems as Markov decision processes, and we consider adversaries that attempt to infer their reward functions using inverse reinforcement learning. To counter such efforts, we present two regularization strategies for policy synthesis problems that actively deceive an adversary about a system’s underlying rewards. The first form of deception is “diversionary”, and it leads an adversary to draw any false conclusion about what the system’s reward function is. The second form of deception is “targeted”, and it leads an adversary to draw a specific false conclusion about what the system’s reward function is. We then show how each form of deception can be implemented in policy optimization problems, and we analytically bound the loss in total accumulated reward that is induced by deception. Next, we evaluate these developments in a multi-agent sequential decision-making problem with one real agent and multiple decoys. We show that diversionary deception can cause the adversary to believe that the most important agent is the least important, while attaining a total accumulated reward that is 98.83\% of its optimal, non-deceptive value. Similarly, we show that targeted deception can make any decoy appear to be the most important agent, while still attaining a total accumulated reward that is 99.25\% of its optimal, non-deceptive value.

</details>



#[deception](tags/deception/) #[information concealment](tags/information-concealment/) #[sequential decision-making](tags/sequential-decision-making/)

<hr style='border: 1px solid black; margin: 20px 0;'>


### Approximate Feedback Nash Equilibria with Sparse Inter-Agent Dependencies

Xinjie Liu, Jingqi Li, Filippos Fotiadis, **Mustafa O. Karabag**, Jesse Milzman, David Fridovich-Keil, Ufuk Topcu  
*Preprint, 2025*  

[Paper](https://arxiv.org/pdf/2410.16441)

<details markdown="1">
<summary markdown="span">**Show abstract**</summary>

Feedback Nash equilibrium strategies in multi-agent dynamic games require availability of all players’ state information to compute control actions. However, in real-world scenarios, sensing and communication limitations between agents make full state feedback expensive or impractical, and such strategies can become fragile when state information from other agents is inaccurate. To this end, we propose a regularized dynamic programming approach for finding sparse feedback policies that selectively depend on the states of a subset of agents in dynamic games. The proposed approach solves convex adaptive group Lasso problems to compute sparse policies approximating Nash equilibrium solutions. We prove the regularized solutions’ asymptotic convergence to a neighborhood of Nash equilibrium policies in linear-quadratic (LQ) games. Further, we extend the proposed approach to general non-LQ games via an iterative algorithm. Simulation results in multi-robot interaction scenarios show that the proposed approach effectively computes feedback policies with varying sparsity levels. When agents have noisy observations of other agents’ states, simulation results indicate that the proposed regularized policies consistently achieve lower costs than standard Nash equilibrium policies by up to 77\% for all interacting agents whose costs are coupled with other agents’ states.

</details>



#[communication](tags/communication/) #[games](tags/games/) #[limited information](tags/limited-information/) #[multiagent systems](tags/multiagent-systems/)

<hr style='border: 1px solid black; margin: 20px 0;'>


### DiBS-MTL: Transformation-Invariant Multitask Learning with Direction Oracles

Surya Murthy, Kushagra Gupta, **Mustafa O. Karabag**, David Fridovich-Keil, Ufuk Topcu  
*Preprint, 2025*  

[Paper](https://www.arxiv.org/pdf/2509.23948)

<details markdown="1">
<summary markdown="span">**Show abstract**</summary>

Multitask learning (MTL) algorithms typically rely on schemes that combine different task losses or their gradients through weighted averaging. These methods aim to find Pareto stationary points by using heuristics that require access to task loss values, gradients, or both. In doing so, a central challenge arises because task losses can be arbitrarily, nonaffinely scaled relative to one another, causing certain tasks to dominate training and degrade overall performance. A recent advance in cooperative bargaining theory, the Direction-based Bargaining Solution (DiBS), yields Pareto stationary solutions immune to task domination because of its invariance to monotonic nonaffine task loss transformations. However, the convergence behavior of DiBS in nonconvex MTL settings is currently not understood. To this end, we prove that under standard assumptions, a subsequence of DiBS iterates converges to a Pareto stationary point when task losses are possibly nonconvex, and propose DiBS-MTL, a computationally efficient adaptation of DiBS to the MTL setting. Finally, we validate DiBS-MTL empirically on standard MTL benchmarks, showing that it achieves competitive performance with state-of-the-art methods while maintaining robustness to nonaffine monotonic transformations that significantly degrade the performance of existing approaches, including prior bargaining-inspired MTL methods.

</details>



#[bargaining](tags/bargaining/) #[learning](tags/learning/) #[limited information](tags/limited-information/) #[optimization](tags/optimization/)

<hr style='border: 1px solid black; margin: 20px 0;'>


### Designing Inferable Signaling Schemes for Bayesian Persuasion

Caleb Probine, **Mustafa O. Karabag**, Ufuk Topcu  
*Preprint, 2025*  

[Paper](https://arxiv.org/pdf/2510.01434)

<details markdown="1">
<summary markdown="span">**Show abstract**</summary>

In Bayesian persuasion, an informed sender, who observes a state, commits to a randomized signaling scheme that guides a self-interested receiver’s actions. Classical models assume the receiver knows the commitment. We, instead, study the setting where the receiver infers the scheme from repeated interactions. We bound the sender’s performance loss relative to the known-commitment case by a term that grows with the signal space size and shrinks as the receiver’s optimal actions become more distinct. We then lower bound the samples required for the sender to approximately achieve their known-commitment performance in the inference setting. We show that the sender requires more samples in persuasion compared to the leader in a Stackelberg game, which includes commitment but lacks signaling. Motivated by these bounds, we propose two methods for designing inferable signaling schemes, one being stochastic gradient descent (SGD) on the sender’s inference-setting utility, and the other being optimization with a boundedly-rational receiver model. SGD performs best in low- interaction regimes, but modeling the receiver as boundedly- rational and tuning the rationality constant still provides a flexible method for designing inferable schemes. Finally, we apply SGD to a safety alert example and show it to find schemes that have fewer signals and make citizens’ optimal actions more distinct compared to the known-commitment case.

</details>



#[games](tags/games/) #[learning](tags/learning/) #[multiagent systems](tags/multiagent-systems/)

<hr style='border: 1px solid black; margin: 20px 0;'>


### Deceptive Planning Exploiting Inattention Blindness

**Mustafa O. Karabag**, Jesse Milzman, Ufuk Topcu  
*Preprint, 2025*  

[Paper](https://www.arxiv.org/pdf/2510.02714)

<details markdown="1">
<summary markdown="span">**Show abstract**</summary>

We study decision-making with rational inattention in settings where agents have perception constraints. In such settings, inaccurate prior beliefs or models of others may lead to inattention blindness, where an agent is unaware of its incorrect beliefs. We model this phenomenon in two-player zero-sum stochastic games, where Player 1 has perception constraints and Player 2 deceptively deviates from its security policy presumed by Player 1 to gain an advantage. We formulate the perception constraints as an online sensor selection problem, develop a value-weighted objective function for sensor selection capturing rational inattention, and propose the greedy algorithm for selection under this monotone objective function. When Player 2 does not deviate from the presumed policy, this objective function provides an upper bound on the expected value loss compared to the security value where Player 1 has perfect information of the state. We then propose a myopic decision-making algorithm for Player 2 to exploit Player 1's beliefs by deviating from the presumed policy and, thereby, improve upon the security value. Numerical examples illustrate how Player 1 persistently chooses sensors that are consistent with its priors, allowing Player 2 to systematically exploit its inattention.

</details>



#[deception](tags/deception/) #[games](tags/games/) #[perception](tags/perception/) #[security](tags/security/) #[sequential decision-making](tags/sequential-decision-making/)

<hr style='border: 1px solid black; margin: 20px 0;'>


### Deceptive Exploration in Multi-armed Bandits

I. Arda Vurankaya, **Mustafa O. Karabag**, Wesley A. Suttle, Jesse Milzman, David Fridovich-Keil, Ufuk Topcu  
*Preprint, 2025*  

<details markdown="1">
<summary markdown="span">**Show abstract**</summary>

We consider a multi-armed bandit setting in which each arm has a public and a private reward distribution. An observer expects an agent to follow Thompson Sampling according to the public rewards, however, the deceptive agent aims to quickly identify the best private arm without being noticed. The observer can observe the public rewards and the pulled arms, but not the private rewards. The agent, on the other hand, observes both the public and private rewards. We formalize detectability as a stepwise Kullback-Leibler (KL) divergence constraint between the actual pull probabilities used by the agent and the anticipated pull probabilities by the observer. We model successful pulling of public suboptimal arms as a Bernoulli process where the success probability decreases with each successful pull, and show these pulls can happen at most at a $\Theta(\sqrt{T}) $ rate under the KL constraint. We then formulate a maximin problem based on public and private means, whose solution characterizes the optimal error exponent for best private arm identification. We finally propose an algorithm inspired by top-two algorithms. This algorithm naturally adapts its exploration according to the hardness of pulling arms based on the public suboptimality gaps. We provide numerical examples illustrating the $\Theta(\sqrt{T}) $ rate and the behavior of the proposed algorithm.

</details>



#[deception](tags/deception/) #[learning](tags/learning/) #[multiarmed bandits](tags/multiarmed-bandits/) #[security](tags/security/)

<hr style='border: 1px solid black; margin: 20px 0;'>


### When Should a Leader Act Suboptimally? The Role of Inferability in Repeated Stackelberg Games

**Mustafa O. Karabag**, Sophia Smith, Negar Mehr, David Fridovich-Keil, Ufuk Topcu  
*Preprint, 2024*  

[Paper](https://arxiv.org/abs/2310.00468)

<details markdown="1">
<summary markdown="span">**Show abstract**</summary>

When interacting with other decision-making agents in non-adversarial scenarios, it is critical for an autonomous agent to have inferable behavior: The agent's actions must convey their intention and strategy. We model the inferability problem using Stackelberg games with observations where a leader and a follower repeatedly interact. During the interactions, the leader uses a fixed mixed strategy. The follower does not know the leader's strategy and dynamically reacts to the statistically inferred strategy based on the leader's previous actions. In the inference setting, the leader may have a lower performance compared to the setting where the follower has full information on the leader's strategy. We refer to the performance gap between these settings as the inferability gap. For a variety of game settings, we show that the inferability gap is upper-bounded by a function of the number of interactions and the stochasticity level of the leader's strategy, encouraging the use of inferable strategies with lower stochasticity levels. We also analyze bimatrix Stackelberg games and identify a set of games where the leader's near-optimal strategy may suffer from a large inferability gap.

</details>



#[games](tags/games/) #[learning](tags/learning/) #[multiagent systems](tags/multiagent-systems/)

<hr style='border: 1px solid black; margin: 20px 0;'>


# Journal Publications

### Designing Policies for Transition-Independent Multiagent Systems that are Robust to Communication Loss

**Mustafa O. Karabag**, Cyrus Neary, Ufuk Topcu  
*Journal of Autonomous Agents and Multi-Agent Systems (JAAMAS), 2025*  

[Paper](https://doi.org/10.1007/s10458-025-09721-9)

<details markdown="1">
<summary markdown="span">**Show abstract**</summary>

In a cooperative multiagent system, a collection of agents executes a joint policy in order to achieve some common objective. The successful deployment of such systems hinges on the availability of reliable inter-agent communication. However, many sources of potential disruption to communication exist in practice, such as radio interference, hardware failure, and adversarial attacks. In this work, we develop joint policies for cooperative multiagent systems that are robust to potential losses in communication. More specifically, we develop joint policies for cooperative Markov games with independent transitions and joint reach-avoid objectives. First, we propose an algorithm for the decentralized execution of joint policies during periods of communication loss. This algorithm is designed to work under arbitrary communication partitions between the agents. Next, we use the total correlation of the state-action process induced by a joint policy as a measure of the intrinsic dependencies between the agents. We then use this measure to lower-bound the performance of a joint policy under randomly intermittent or adversarial communication loss scenarios. We show the existence of a multiagent decision-making environment in which this bound is tight—the highest performance under intermittent communication loss, for any policy execution mechanism, is of the same order as the bound. We then present an algorithm that maximizes a proxy to this lower bound in order to synthesize minimum-dependency joint policies that remain performant under communication loss. Through two-agent and three-agent numerical experiments, we show that the proposed minimum-dependency policies require minimal coordination between the agents while incurring little to no loss in performance; the total correlation value of the synthesized policy is significantly lower than the total correlation value of the baseline policy which does not take potential communication losses into account. As a result, the performance of the minimum-dependency policies remains consistently high regardless of whether or not communication is available. By contrast, the performance of the baseline policy decreases drastically when communication is lost.

</details>



#[communication](tags/communication/) #[information theory](tags/information-theory/) #[limited information](tags/limited-information/) #[multiagent systems](tags/multiagent-systems/)

<hr style='border: 1px solid black; margin: 20px 0;'>


### Identity concealment games: How I learned to stop revealing and love the coincidences

**Mustafa O. Karabag**, Melkior Ornik, Ufuk Topcu  
*Automatica, 2024*  

[Paper](https://linkinghub.elsevier.com/retrieve/pii/S0005109823006519)

<details markdown="1">
<summary markdown="span">**Show abstract**</summary>

In an adversarial environment, a hostile player performing a task may behave like a non-hostile one in order not to reveal its identity to an opponent. To model such a scenario, we define identity concealment games: zero-sum stochastic reachability games with a zero-sum objective of identity concealment. To measure the identity concealment of the player, we introduce the notion of an average player. The average player’s policy represents the expected behavior of a non-hostile player. We show that there exists an equilibrium policy pair for every identity concealment game and give the optimality equations to synthesize an equilibrium policy pair. If the player’s opponent follows a non-equilibrium policy, the player can hide its identity better. For this reason, we study how the hostile player may learn the opponent’s policy. Since learning via exploration policies would quickly reveal the hostile player’s identity to the opponent, we consider the problem of learning a near-optimal policy for the hostile player using the game runs collected under the average player’s policy. Consequently, we propose an algorithm that provably learns a near-optimal policy and give an upper bound on the number of sample runs to be collected.

</details>



#[deception](tags/deception/) #[games](tags/games/) #[information theory](tags/information-theory/) #[learning](tags/learning/) #[security](tags/security/)

<hr style='border: 1px solid black; margin: 20px 0;'>


### Exploiting Partial Observability for Optimal Deception

**Mustafa O. Karabag**, Melkior Ornik, Ufuk Topcu  
*IEEE Transactions on Automatic Control (TAC), 2023*  

[Paper](https://doi.org/10.1109/TAC.2022.3209959)

<details markdown="1">
<summary markdown="span">**Show abstract**</summary>

Deception is a useful tool in situations where an agent operates in the presence of its adversaries. We consider a setting where a supervisor provides a reference policy to an agent, expects the agent to operate in an environment by following the reference policy, and partially observes the agent's behavior. The agent instead follows a different deceptive policy to achieve a different task. We model the environment with a Markov decision process and study the synthesis of optimal deceptive policies under partial observability. We formalize the notion of deception as a hypothesis testing problem and show that the synthesis of optimal deceptive policies is nondeterministic polynomial-time hard (NP-hard). As an approximation, we consider the class of mixture policies, which provides a convex optimization formulation of the deception problem. We give an algorithm that converges to the optimal mixture policy. We also consider a special class of Markov decision processes where the transition and observation functions are deterministic. For this case, we give a randomized algorithm for path planning that generates a path for the agent in polynomial time and achieves the optimal value for the considered objective function.

</details>



#[computational hardness](tags/computational-hardness/) #[deception](tags/deception/) #[information theory](tags/information-theory/) #[security](tags/security/) #[sequential decision-making](tags/sequential-decision-making/)

<hr style='border: 1px solid black; margin: 20px 0;'>


### Deception in Supervisory Control

**Mustafa O. Karabag**, Melkior Ornik, Ufuk Topcu  
*IEEE Transactions on Automatic Control (TAC), 2022*  

[Paper](https://ieeexplore.ieee.org/document/9351619)

<details markdown="1">
<summary markdown="span">**Show abstract**</summary>

The use of deceptive strategies is important for an agent that attempts not to reveal his intentions in an adversarial environment. We consider a setting, in which a supervisor provides a reference policy and expects an agent to follow the reference policy and perform a task. The agent may instead follow a different deceptive policy to achieve a different task. We model the environment and the behavior of the agent with a Markov decision process, represent the tasks of the agent and the supervisor with reachability specifications, and study the synthesis of optimal deceptive policies for such agents. We also study the synthesis of optimal reference policies that prevent deceptive strategies of the agent and achieve the supervisor's task with high probability. We show that the synthesis of optimal deceptive policies has a convex optimization problem formulation, while the synthesis of optimal reference policies requires solving a nonconvex optimization problem. We also show that the synthesis of optimal reference policies is NP-hard.

</details>



#[computational hardness](tags/computational-hardness/) #[deception](tags/deception/) #[information theory](tags/information-theory/) #[security](tags/security/) #[sequential decision-making](tags/sequential-decision-making/)

<hr style='border: 1px solid black; margin: 20px 0;'>


### Entropy Maximization for Markov Decision Processes Under Temporal Logic Constraints

Yagiz Savas, Melkior Ornik, Murat Cubuktepe, **Mustafa O. Karabag**, Ufuk Topcu  
*IEEE Transactions on Automatic Control (TAC), 2020*  

[Paper](https://doi.org/10.1109/TAC.2019.2922583)

<details markdown="1">
<summary markdown="span">**Show abstract**</summary>

We study the problem of synthesizing a policy that maximizes the entropy of a Markov decision process (MDP) subject to a temporal logic constraint. Such a policy minimizes the predictability of the paths it generates, or dually, maximizes the exploration of different paths in an MDP while ensuring the satisfaction of a temporal logic specification. We first show that the maximum entropy of an MDP can be finite, infinite, or unbounded. We provide necessary and sufficient conditions under which the maximum entropy of an MDP is finite, infinite, or unbounded. We then present an algorithm which is based on a convex optimization problem to synthesize a policy that maximizes the entropy of an MDP. We also show that maximizing the entropy of an MDP is equivalent to maximizing the entropy of the paths that reach a certain set of states in the MDP. Finally, we extend the algorithm to an MDP subject to a temporal logic specification. In numerical examples, we demonstrate the proposed method on different motion planning scenarios and illustrate the relation between the restrictions imposed on the paths by a specification, the maximum entropy, and the predictability of paths.

</details>



#[information concealment](tags/information-concealment/) #[information theory](tags/information-theory/) #[security](tags/security/) #[sequential decision-making](tags/sequential-decision-making/)

<hr style='border: 1px solid black; margin: 20px 0;'>


# Conference Publications

### Policies with Sparse Inter-Agent Dependencies in Dynamic Games: A Dynamic Programming Approach

Xinjie Liu, Jingqi Li, Filippos Fotiadis, **Mustafa O. Karabag**, Jesse Milzman, David Fridovich-Keil, Ufuk Topcu  
*International Conference on Autonomous Agents and Multiagent Systems (AAMAS), 2025*  

[Paper](https://dl.acm.org/doi/10.5555/3709347.3743961)

<details markdown="1">
<summary markdown="span">**Show abstract**</summary>

Common feedback strategies in multi-agent dynamic games require all players' state information to compute control strategies. However, in real-world scenarios, sensing and communication limitations between agents make full state feedback expensive or impractical, and such strategies can become fragile when state information from other agents is inaccurate. To this end, we propose a regularized dynamic programming approach for finding sparse feedback policies that selectively depend on the states of a subset of agents in dynamic games. The proposed approach solves convex adaptive group Lasso problems to compute sparse policies approximating Nash equilibrium solutions. We prove the regularized solutions' asymptotic convergence to a neighborhood of Nash equilibrium policies in linear-quadratic (LQ) games. We extend the proposed approach to general non-LQ games via an iterative algorithm. Empirical results in multi-robot interaction scenarios show that the proposed approach effectively computes feedback policies with varying sparsity levels. When agents have noisy observations of other agents' states, simulation results indicate that the proposed regularized policies consistently achieve lower costs than standard Nash equilibrium policies by up to 77\% for all interacting agents whose costs are coupled with other agents' states.

</details>



#[communication](tags/communication/) #[games](tags/games/) #[limited information](tags/limited-information/) #[multiagent systems](tags/multiagent-systems/)

<hr style='border: 1px solid black; margin: 20px 0;'>


### Value of Information-based Deceptive Path Planning Under Adversarial Interventions

Wesley A. Suttle, Jesse Milzman, **Mustafa O. Karabag**, Brian M. Sadler, Ufuk Topcu  
*IEEE Conference on Decision and Control (CDC), 2025*  

[Paper](https://arxiv.org/abs/2503.24284)

<details markdown="1">
<summary markdown="span">**Show abstract**</summary>

Existing methods for deceptive path planning (DPP) address the problem of designing paths that conceal their true goal from a passive, external observer. Such methods do not apply to problems where the observer has the ability to perform adversarial interventions to impede the path planning agent. In this paper, we propose a novel Markov decision process (MDP)-based model for the DPP problem under adversarial interventions and develop powerful new value of information (VoI) objectives to guide the design of DPP policies.
Using the VoI objectives we propose, path planning agents deceive the adversarial observer into choosing suboptimal interventions by selecting trajectories that are of low informational value to the observer. Leveraging connections to the linear programming theory for MDPs, we derive computationally efficient solution methods for synthesizing policies for performing DPP under adversarial interventions. In our experiments, we illustrate the effectiveness of the proposed solution method in achieving deceptiveness under adversarial interventions and demonstrate the superior performance of our approach to both existing DPP methods and conservative path planning approaches on illustrative gridworld problems.

</details>



#[deception](tags/deception/) #[security](tags/security/) #[sequential decision-making](tags/sequential-decision-making/)

<hr style='border: 1px solid black; margin: 20px 0;'>


### Cooperative Bargaining Games Without Utilities: Mediated Solutions from Direction Oracles

Kushagra Gupta, Surya Murthy, **Mustafa O. Karabag**, Ufuk Topcu, David Fridovich-Keil  
*Conference on Neural Information Processing Systems (NeurIPS), 2025*  

[Paper](https://arxiv.org/abs/2505.14817)

<details markdown="1">
<summary markdown="span">**Show abstract**</summary>

Cooperative bargaining games are widely used to model resource allocation and
conflict resolution. Traditional solutions assume the mediator can access agents’
utility function values and gradients. However, there is an increasing number of
settings, such as human-AI interactions, where utility values may be inaccessible
or incomparable due to unknown, nonaffine transformations. To model such
settings, we consider that the mediator has access only to agents’ most preferred
directions—normalized utility gradients in the decision space. To this end, we
propose a cooperative bargaining algorithm where a mediator has access to only
the direction oracle of each agent. We prove that unlike popular approaches
such as the Nash and Kalai-Smorodinsky bargaining solutions, our approach is
invariant to monotonic nonaffine transformations, and that under strong convexity
and smoothness assumptions, this approach enjoys global asymptotic convergence
to Pareto stationary solutions. Moreover, we show that the bargaining solutions
found by our algorithm also satisfy the axioms of symmetry and (under slightly
stronger conditions) independence of irrelevant alternatives, which are popular
in the literature. Finally, we conduct experiments in two domains, multi-agent
formation assignment and mediated stock portfolio allocation, which validate these
theoretical results.

</details>



#[bargaining](tags/bargaining/) #[limited information](tags/limited-information/) #[optimization](tags/optimization/)

<hr style='border: 1px solid black; margin: 20px 0;'>


### Encouraging Inferable Behavior for Autonomy: Repeated Bimatrix Stackelberg Games with Observations

**Mustafa O. Karabag**, Sophia Smith, David Fridovich-Keil, Ufuk Topcu  
*American Control Conference (ACC), 2024*  

[Paper](https://ieeexplore.ieee.org/document/10644936)

<details markdown="1">
<summary markdown="span">**Show abstract**</summary>

When interacting with other non-competitive decision-making agents, it is critical for an autonomous agent to have inferable behavior: Their actions must convey their intention and strategy. For example, an autonomous car's strategy must be inferable by the pedestrians interacting with the car. We model the inferability problem using a repeated bimatrix Stackelberg game with observations where a leader and a follower repeatedly interact. During the interactions, the leader uses a fixed, potentially mixed strategy. The follower, on the other hand, does not know the leader's strategy and dynamically reacts based on observations that are the leader's previous actions. In the setting with observations, the leader may suffer from an inferability loss, i.e., the performance compared to the setting where the follower has perfect information of the leader's strategy. We show that the inferability loss is upper-bounded by a function of the number of interactions and the stochasticity level of the leader's strategy, encouraging the use of inferable strategies with lower stochasticity levels. As a converse result, we also provide a game where the required number of interactions is lower bounded by a function of the desired inferability loss.

</details>



#[games](tags/games/) #[learning](tags/learning/) #[multiagent systems](tags/multiagent-systems/)

<hr style='border: 1px solid black; margin: 20px 0;'>


### Defining and Measuring Deception in Sequential Decision Systems: Application to Network Defense

Yerin Kim, Alexander Benvenuti, Bo Chen, **Mustafa O. Karabag**, Abhishek Kulkarni, Nathaniel B. Bastian, Ufuk Topcu, Matthew Hale  
*IEEE Military Communications Conference (MILCOM), 2024*  

[Paper](https://ieeexplore.ieee.org/document/10773660)

<details markdown="1">
<summary markdown="span">**Show abstract**</summary>

Concealing true targets plays a crucial role in preventing adversaries from launching effective attacks. Deception techniques enhance security by misleading and delaying adversaries. This paper presents a framework for defining and measuring deception in sequential decision systems modeled as Markov decision processes with task constraints. We introduce three types of deception: diversionary, targeted, and equivocal, which are implemented by synthesizing deceptive policies using constrained optimization. Adversaries are modeled with inverse reinforcement learning to infer system goals. Numerical results demonstrate the effectiveness of our deception techniques in misleading adversaries and enhancing system security.

</details>



#[deception](tags/deception/) #[information concealment](tags/information-concealment/) #[security](tags/security/) #[sequential decision-making](tags/sequential-decision-making/)

<hr style='border: 1px solid black; margin: 20px 0;'>


### Deceptive Planning for Resource Allocation

Shenghui Chen, Yagiz Savas, **Mustafa O. Karabag**, Brian M. Sadler, Ufuk Topcu  
*American Control Conference (ACC), 2024*  

[Paper](https://ieeexplore.ieee.org/document/10644373)

<details markdown="1">
<summary markdown="span">**Show abstract**</summary>

We consider a team of autonomous agents that navigate in an adversarial environment and aim to achieve a task by allocating their resources over a set of target locations. An adversary in the environment observes the autonomous team's behavior to infer their objective and responds against the team. In this setting, we propose strategies for controlling the density of the autonomous team so that they can deceive the adversary regarding their objective while achieving the desired final resource allocation. We first develop a prediction algorithm based on the principle of maximum entropy to express the team's behavior expected by the adversary. Then, by measuring the deceptiveness via Kullback-Leibler divergence, we devise convex optimization-based planning algorithms that deceive the adversary by either exaggerating the behavior towards a decoy allocation strategy or creating ambiguity regarding the final allocation strategy. A user study with $320$ participants demonstrates that the proposed algorithms are effective for deception and reveal the inherent biases of participants towards proximate goals.

</details>



#[deception](tags/deception/) #[security](tags/security/) #[sequential decision-making](tags/sequential-decision-making/)

<hr style='border: 1px solid black; margin: 20px 0;'>


### A Decentralized Shotgun Approach for Team Deception

Caleb Probine, **Mustafa O. Karabag**, Ufuk Topcu  
*International Conference on Decision and Game Theory for Security (GameSec), 2024*  

[Paper](https://link.springer.com/chapter/10.1007/978-3-031-74835-6_9)

<details markdown="1">
<summary markdown="span">**Show abstract**</summary>

Deception is helpful for agents masking their intentions from an observer. We consider a team of agents deceiving their supervisor. The supervisor defines nominal behavior for the agents via reference policies, but the agents share an alternate task that they can only achieve by deviating from these references. As such, the agents use deceptive policies to complete the task while ensuring that their behaviors remain plausible to the supervisor. We propose a setting with centralized deceptive policy synthesis and decentralized execution. We model each agent with a Markov decision process and constrain the agents' deceptive policies so that, with high probability, at least one agent achieves the task. We then provide an algorithm to synthesize deceptive policies that ensure the deviations of all agents are small by minimizing the worst Kullback-Leibler divergence between any agent's deceptive and reference policies. Thanks to decentralization, this algorithm scales linearly with the number of agents and also facilitates the efficient synthesis of reference policies. We then explore a more general version of the deceptive policy synthesis problem. In particular, we consider a supervisor who selects a subset of agents to eliminate based on the agents' behaviors. We give algorithms to synthesize deceptive policies so that, after the supervisor eliminates some agents, the remaining agents complete the task with high probability. We demonstrate the developed methods in a package delivery example.

</details>



#[deception](tags/deception/) #[multiagent systems](tags/multiagent-systems/) #[security](tags/security/) #[sequential decision-making](tags/sequential-decision-making/)

<hr style='border: 1px solid black; margin: 20px 0;'>


### Simulator-Driven Deceptive Control via Path Integral Approach

Apurva Patil, **Mustafa O. Karabag**, Takashi Tanaka, Ufuk Topcu  
*IEEE Conference on Decision and Control (CDC), 2023*  

[Paper](https://ieeexplore.ieee.org/document/10383936)

<details markdown="1">
<summary markdown="span">**Show abstract**</summary>

We consider a setting where a supervisor delegates an agent to perform a certain control task, while the agent is incentivized to deviate from the given policy to achieve its own goal. In this work, we synthesize the optimal deceptive policies for an agent who attempts to hide its deviations from the supervisor's policy. We study the deception problem in the continuous-state discrete-time stochastic dynamics setting and, using motivations from hypothesis testing theory, formulate a Kullback-Leibler control problem for the synthesis of deceptive policies. This problem can be solved using backward dynamic programming in principle, which suffers from the curse of dimensionality. However, under the assumption of deterministic state dynamics, we show that the optimal deceptive actions can be generated using path integral control. This allows the agent to numerically compute the deceptive actions via Monte Carlo simulations. Since Monte Carlo simulations can be efficiently parallelized, our approach allows the agent to generate deceptive control actions online. We show that the proposed simulation-driven control approach asymptotically converges to the optimal control distribution.

</details>



#[deception](tags/deception/) #[information theory](tags/information-theory/) #[security](tags/security/) #[sequential decision-making](tags/sequential-decision-making/)

<hr style='border: 1px solid black; margin: 20px 0;'>


### Scenario-Game ADMM: A Parallelized Scenario-Based Solver for Stochastic Noncooperative Games

Jingqi Li, Chih-Yuan Chiu, Lasse Peters, Fernando Palafox, **Mustafa O. Karabag**, Javier Alonso-Mora, Somayeh Sojoudi, Claire Tomlin, David Fridovich-Keil  
*IEEE Conference on Decision and Control (CDC), 2023*  

[Paper](https://ieeexplore.ieee.org/document/10383423)

<details markdown="1">
<summary markdown="span">**Show abstract**</summary>

Decision-making in multi-player games can be extremely challenging, particularly under uncertainty. In this work, we propose a new sample-based approximation to a class of stochastic, general-sum, pure Nash games, where each player has an expected-value objective and a set of chance constraints. This new approximation scheme inherits the accuracy of objective approximation from the established sample average approximation (SAA) method and enjoys a feasibility guarantee derived from the scenario optimization literature. We characterize the sample complexity of this new game-theoretic approximation scheme, and observe that high accuracy usually requires a large number of samples, which results in a large number of sampled constraints. To accommodate this, we decompose the approximated game into a set of smaller games with few constraints for each sampled scenario, and propose a decentralized, consensus-based ADMM algorithm to efficiently compute a generalized Nash equilibrium (GNE) of the approximated game. We prove the convergence of our algorithm to a GNE and empirically demonstrate superior performance relative to a recent baseline algorithm based on ADMM and interior point method.

</details>



#[multiagent systems](tags/multiagent-systems/) #[optimization](tags/optimization/)

<hr style='border: 1px solid black; margin: 20px 0;'>


### On the Sample Complexity of Vanilla Model-Based Offline Reinforcement Learning with Dependent Samples

**Mustafa O. Karabag**, Ufuk Topcu  
*AAAI Conference on Artificial Intelligence (AAAI), 2023*  

[Paper](https://dl.acm.org/doi/10.1609/aaai.v37i7.25989)

<details markdown="1">
<summary markdown="span">**Show abstract**</summary>

Offline reinforcement learning (offline RL) considers problems where learning is performed using only previously collected samples and is helpful for the settings in which collecting new data is costly or risky. In model-based offline RL, the learner performs estimation (or optimization) using a model constructed according to the empirical transition frequencies. We analyze the sample complexity of vanilla model-based offline RL with dependent samples in the infinite-horizon discounted-reward setting. In our setting, the samples obey the dynamics of the Markov decision process and, consequently, may have interdependencies. Under no assumption of independent samples, we provide a high-probability, polynomial sample complexity bound for vanilla model-based off-policy evaluation that requires partial or uniform coverage. We extend this result to the off-policy optimization under uniform coverage. As a comparison to the model-based approach, we analyze the sample complexity of off-policy evaluation with vanilla importance sampling in the infinite-horizon setting. Finally, we provide an estimator that outperforms the sample-mean estimator for almost deterministic dynamics that are prevalent in reinforcement learning.

</details>



#[learning](tags/learning/) #[limited information](tags/limited-information/) #[sequential decision-making](tags/sequential-decision-making/)

<hr style='border: 1px solid black; margin: 20px 0;'>


### Differential Privacy in Cooperative Multiagent Planning

Bo Chen, Calvin Hawkins, **Mustafa O. Karabag**, Cyrus Neary, Matthew Hale, Ufuk Topcu  
*Uncertainty in Artificial Intelligence (UAI), 2023*  

[Paper](https://proceedings.mlr.press/v216/chen23e.html)

<details markdown="1">
<summary markdown="span">**Show abstract**</summary>

Privacy-aware multiagent systems must protect agents' sensitive data while simultaneously ensuring that agents accomplish their shared objectives. Towards this goal, we propose a framework to privatize inter-agent communications in cooperative multiagent decision-making problems. We study sequential decision-making problems formulated as cooperative Markov games with reach-avoid objectives. We apply a differential privacy mechanism to privatize agents' communicated symbolic state trajectories, and then we analyze tradeoffs between the strength of privacy and the team's performance. For a given level of privacy, this tradeoff is shown to depend critically upon the total correlation among agents' state-action processes. We synthesize policies that are robust to privacy by reducing the value of the total correlation. Numerical experiments demonstrate that the team's performance under these policies decreases by only 3 percent when comparing private versus non-private implementations of communication. By contrast, the team's performance decreases by roughly 86 percent when using baseline policies that ignore total correlation and only optimize team performance.

</details>



#[multiagent systems](tags/multiagent-systems/) #[privacy](tags/privacy/) #[sequential decision-making](tags/sequential-decision-making/)

<hr style='border: 1px solid black; margin: 20px 0;'>


### Planning Not to Talk: Multiagent Systems that are Robust to Communication Loss

**Mustafa O. Karabag**, Cyrus Neary, Ufuk Topcu  
*International Conference on Autonomous Agents and Multiagent Systems (AAMAS), 2022*  

[Paper](https://dl.acm.org/doi/10.5555/3535850.3535930)

<details markdown="1">
<summary markdown="span">**Show abstract**</summary>

In a cooperative multiagent system, a collection of agents executes a joint policy in order to achieve some common objective. The successful deployment of such systems hinges on the availability of reliable inter-agent communication. However, many sources of potential disruption to communication exist in practice, such as radio interference, hardware failure, and adversarial attacks. In this work, we develop joint policies for cooperative multiagent systems that are robust to potential losses in communication. More specifically, we develop joint policies for cooperative Markov games with reach-avoid objectives. First, we propose an algorithm for the decentralized execution of joint policies during periods of communication loss. Next, we use the total correlation of the state-action process induced by a joint policy as a measure of the intrinsic dependencies between the agents. We then use this measure to lower-bound the performance of a joint policy when communication is lost. Finally, we present an algorithm that maximizes a proxy to this lower bound in order to synthesize minimum-dependency joint policies that are robust to communication loss. Numerical experiments show that the proposed minimum-dependency policies require minimal coordination between the agents while incurring little to no loss in performance; the total correlation value of the synthesized policy is one fifth of the total correlation value of the baseline policy which does not take potential communication losses into account. As a result, the performance of the minimum-dependency policies remains consistently high regardless of whether or not communication is available. By contrast, the performance of the baseline policy decreases by twenty percent when communication is lost.

</details>



#[communication](tags/communication/) #[limited information](tags/limited-information/) #[multiagent systems](tags/multiagent-systems/) #[sequential decision-making](tags/sequential-decision-making/)

<hr style='border: 1px solid black; margin: 20px 0;'>


### Alternating Direction Method of Multipliers for Decomposable Saddle-Point Problems

**Mustafa O. Karabag**, David Fridovich-Keil, Ufuk Topcu  
*Annual Allerton Conference on Communication, Control, and Computing (Allerton), 2022*  

[Paper](https://ieeexplore.ieee.org/abstract/document/9929349)

<details markdown="1">
<summary markdown="span">**Show abstract**</summary>

Saddle-point problems appear in various settings including machine learning, zero-sum stochastic games, and regression problems. We consider decomposable saddle-point problems and study an extension of the alternating direction method of multipliers to such saddle-point problems. Instead of solving the original saddle-point problem directly, this algorithm solves smaller saddle-point problems by exploiting the decomposable structure. We show the convergence of this algorithm for convex-concave saddle-point problems under a mild assumption. We also provide a sufficient condition for which the assumption holds. We demonstrate the convergence properties of the saddle-point alternating direction method of multipliers with numerical examples on a power allocation problem in communication channels and a network routing problem with adversarial costs.

</details>



#[optimization](tags/optimization/)

<hr style='border: 1px solid black; margin: 20px 0;'>


### Smooth Convex Optimization Using Sub-Zeroth-Order Oracles

**Mustafa O. Karabag**, Cyrus Neary, Ufuk Topcu  
*AAAI Conference on Artificial Intelligence (AAAI), 2021*  

[Paper](https://ojs.aaai.org/index.php/AAAI/article/view/16499/16306)

<details markdown="1">
<summary markdown="span">**Show abstract**</summary>

We consider the problem of minimizing a smooth, Lipschitz, convex function over a compact, convex set using sub-zeroth-order oracles: an oracle that outputs the sign of the directional derivative for a given point and a given direction, an oracle that compares the function values for a given pair of points, and an oracle that outputs a noisy function value for a given point. We show that the sample complexity of optimization using these oracles is polynomial in the relevant parameters. The optimization algorithm that we provide for the comparator oracle is the first algorithm with a known rate of convergence that is polynomial in the number of dimensions. We also give an algorithm for the noisy-value oracle that incurs a regret of O{\textasciitilde}(n3.75T0.75) (ignoring the other factors and logarithmic dependencies) where n is the number of dimensions and T is the number of queries.

</details>



#[learning](tags/learning/) #[limited information](tags/limited-information/) #[optimization](tags/optimization/)

<hr style='border: 1px solid black; margin: 20px 0;'>


### Optimal Deceptive and Reference Policies for Supervisory Control

**Mustafa O. Karabag**, Melkior Ornik, Ufuk Topcu  
*IEEE Conference on Decision and Control (CDC), 2019*  

[Paper](https://ieeexplore.ieee.org/document/9029607)

<details markdown="1">
<summary markdown="span">**Show abstract**</summary>

The use of deceptive strategies is important for an agent that attempts not to reveal his intentions in an adversarial environment. We consider a setting in which a supervisor provides a reference policy and expects an agent to follow the reference policy and perform a task. The agent may instead follow a different, deceptive policy to achieve a different task. We model the environment and the behavior of the agent with a Markov decision process, represent the tasks of the agent and the supervisor with linear temporal logic formulae, and study the synthesis of optimal deceptive policies for such agents. We also study the synthesis of optimal reference policies that prevents deceptive strategies of the agent and achieves the supervisor's task with high probability. We show that the synthesis of deceptive policies has a convex optimization problem formulation, while the synthesis of reference policies requires solving a nonconvex optimization problem.

</details>



#[deception](tags/deception/) #[information theory](tags/information-theory/) #[security](tags/security/) #[sequential decision-making](tags/sequential-decision-making/)

<hr style='border: 1px solid black; margin: 20px 0;'>


### Least Inferable Policies for Markov Decision Processes

**Mustafa O. Karabag**, Melkior Ornik, Ufuk Topcu  
*American Control Conference (ACC), 2019*  

[Paper](https://doi.org/10.23919/ACC.2019.8815129)

<details markdown="1">
<summary markdown="span">**Show abstract**</summary>

In a variety of applications, an agent's success depends on the knowledge that an adversarial observer has or can gather about the agent's decisions. It is therefore desirable for the agent to achieve a task while reducing the ability of an observer to infer the agent's policy. We consider the task of the agent as a reachability problem in a Markov decision process and study the synthesis of policies that minimize the observer's ability to infer the transition probabilities of the agent between the states of the Markov decision process. We introduce a metric that is based on the Fisher information as a proxy for the information leaked to the observer and using this metric formulate a problem that minimizes expected total information subject to the reachability constraint. We proceed to solve the problem using convex optimization methods. To verify the proposed method, we analyze the relationship between the expected total information and the estimation error of the observer, and show that, for a particular class of Markov decision processes, these two values are inversely proportional.

</details>



#[estimation theory](tags/estimation-theory/) #[information concealment](tags/information-concealment/) #[security](tags/security/) #[sequential decision-making](tags/sequential-decision-making/)

<hr style='border: 1px solid black; margin: 20px 0;'>


# Other Publications

### Formal Methods for Autonomous Systems

Tichakorn Wongpiromsarn, Mahsa Ghasemi, Murat Cubuktepe, Georgios Bakirtzis, Steven Carr, **Mustafa O. Karabag**, Cyrus Neary, Parham Gohari, Ufuk Topcu  
*Foundations and Trends in Systems and Control, 2023*  

[Paper](10.1561/2600000029)

<details markdown="1">
<summary markdown="span">**Show abstract**</summary>

Formal methods refer to rigorous, mathematical approaches to system development and have played a key role in establishing the correctness of safety-critical systems. The main building blocks of formal methods are models and specifications, which are analogous to behaviors and requirements in system design and give us the means to verify and synthesize system behaviors with formal guarantees. 
This monograph provides a survey of the current state of the art on applications of formal methods in the autonomous systems domain. We consider correct-by-construction synthesis under various formulations, including closed systems, reactive, and probabilistic settings. Beyond synthesizing systems in known environments, we address the concept of uncertainty and bound the behavior of systems that employ learning using formal methods. Further, we examine the synthesis of systems with monitoring, a mitigation technique for ensuring that once a system deviates from expected behavior, it knows a way of returning to normalcy. We also show how to overcome some limitations of formal methods themselves with learning. We conclude with future directions for formal methods in reinforcement learning, uncertainty, privacy, explainability of formal methods, and regulation and certification.

</details>



#[formal methods](tags/formal-methods/) #[sequential decision-making](tags/sequential-decision-making/)

<hr style='border: 1px solid black; margin: 20px 0;'>

