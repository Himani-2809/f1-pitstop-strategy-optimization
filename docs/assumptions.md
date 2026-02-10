# Modeling Assumptions

This project aims to develop machine-learning models to predict two primary outcomes:
1. The lap on which a driver performs their **first pit stop**
2. The **tyre compound** selected during that pit stop

To reduce dimensionality, control strategic variability, and maintain interpretability,
the following assumptions were adopted.

## Core Assumptions

- **Only the first pit stop is modeled** for each driver, even in races involving multiple stops.
  This simplifies strategy representation and enables consistent comparison across drivers.

- **Wet and mixed-condition races are excluded**, as changing track conditions introduce
  highly non-linear effects that are outside the scope of the current modeling framework.

- A **driver-specific baseline pace** is approximated using the *final qualifying lap time*,
  referred to as the **base lap time**. This serves as a proxy for intrinsic car–driver performance.

- **Tyre degradation** is modeled using simple quadratic or non-linear approximations for each
  compound (Soft, Medium, Hard), representing fractional lap-time increases as a function of tyre age.

- **Aerodynamic effects** such as DRS, slipstreaming, and dirty air are deliberately ignored.
  This isolates the influence of tyre-related and timing-based variables on pit-stop decisions.

## Rationale

These simplifications allow the analysis to focus on **fundamental, interpretable indicators**
that influence pit-stop strategy, while providing a structured foundation for progressively
incorporating higher-fidelity physical and strategic effects in future work.

