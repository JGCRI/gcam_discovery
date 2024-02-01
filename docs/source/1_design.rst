.. _design:

************************
Experimental Design
************************

Designing a scenario discovery experiment with GCAM is centered around the construction of a large scenario ensemble of model runs. This is typically the most difficult and laborious step of the process, but spending the time to develop a rich and impactful ensemble of realizations will provide the greatest return on the quality of the final research product, and will increase opportunities for leveraging the ensemble in additional projects and new collaborations. There is no set threshold of unique model simulations to reach in order to constitute a “large ensemble” but the output must sufficiently explore an uncertainty space relevant to the research questions. Organizing thoughts and ideas about relevant uncertainties can be facilitated by the use of existing frameworks for modeling uncertainty. One such technique is the “XLRM” framework commonly deployed in RDM circles, articulating and delineating the relevant eXogenous uncertainties, strategy Levers, modeled Relationships, and performance Measures (metrics) [Rand 2003]. Developing the intellectual basis for an ensemble using this framework can be done by answering the following questions:

Which uncertain exogenous parameters should be varied within the scenario configurations?
------------------------------------------------------------------------------------------

This list will constitute the parametric uncertainty space covered by the ensemble. Generally, this will be informed by a review of the relevant literature, conversations with stakeholders, and specific research goals to be achieved. Some possibilities for what to include could be a combination of: 

- Parameters commonly shown to be important drivers of your relevant outcomes (e.g., water availability on crop production)
- Under-explored and deeply uncertain parameters
- Parameters for which there is ambiguity in how their uncertainty will propagate
- Parameters of which the model’s representation is particularly strong or detailed
- Parameters which are highly connected to many different systems (e.g., population).

Determining the Number of Variable Parameters
______________________________________________

In addition to literature review and expert elicitation, the makeup of a scenario ensemble will also be bound by practicality. Because each new sensitivity will multiply the ensemble size, there will be a realistic limit based on total computation time and storage capacity for the resulting databases. Similarly, it must also be determined how many discrete values a parameter can take on. For example, ten sensitivities with two unique values each will result in the same number of model runs as four sensitivities with five unique values each. Another consideration regarding practicality is estimating the amount of time before data obsolescence. In a constantly evolving field focused on modeling future states of the world, the relevance of forecasts wanes over time, so a balance must be struck between coverage and speed.

What are the plausible ranges for each sensitivity?
____________________________________________________

This can be determined through literature review, where extreme bounds can be chosen to cover the widest possible range, or simply the most common. Additionally, some parameters may be bounded by their zero-sum complementarity with competing options, or physics of natural processes. 

