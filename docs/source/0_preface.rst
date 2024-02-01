.. _preface:

************************
Preface
************************

Models are often treated as predictive tools. If the structure of the model adequately represents the structure of the real system, and the parameters are known with sufficient precision, then the model outputs will closely mirror reality and decision makers can plan accordingly. In practice, for all but the simplest systems, this is not the case. Models of complicated systems are generally simplifications, and parameter values may be highly uncertain. For such systems, even small differences in parameter values can result in fundamentally different model behavior. As such, any single prediction will be of limited use in decision making, and a different approach is needed.

Exploratory modeling seeks to understand system behavior across a range of conditions, rather than to use models to make a single “best guess” about the future. It falls within the scope of robust decision making (RDM), a framework tailored to systems operating with significant deep uncertainty. Scenario discovery is one manifestation of exploratory modeling, using machine learning techniques on large datasets to uncover the drivers of relevant outcomes and describe the robustness of observed dynamics across wide uncertainty spaces.

Decision makers and stakeholders can benefit from the improved uncertainty characterization and more complete understanding of potential interactions and tradeoffs afforded by a scenario discovery analysis. Examples of scenario discovery outcomes include:

- Identification of critical drivers and shared conditions influencing relevant metrics
- Clustered scenario typologies connecting drivers to intuitive, accessible narratives
- Quantification of relative feature importance among drivers
- Classification of extreme outcomes
- Robustness of scenario pathways
- Sources of risk or volatility, to recommend future work or targets for strategic planning

Integrated, multisector, multiregional models such as GCAM are well-suited for scenario discovery analyses, as they model highly complex, deeply uncertain systems through the coupling of interconnected energy, water, land, climate, and socioeconomic sectors. For such large models which rely on many thousands of calibrated parameters, future forecasts, and abstractions of real world systems, characterizing the various sources of uncertainty is important for adding robustness and validity to modeling exercises. Scenario discovery is a method for applying a many-dimensional sensitivity analysis to model inputs to reduce the inherent modeling biases associated with “best guess” parameter values. In this document, we will focus our explanation of scenario discovery on application to the GCAM model. However, the approach and interpretation is generalizable to other modeling frameworks.
