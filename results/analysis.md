## Summary (mean±sd over trials)

| model | condition | recall | exact | precision | false-act | unparse |
|---|---|---|---|---|---|---|
| glm-5.3-flash | disclosure | 0.969±0.005 | 0.546±0.032 | 0.594±0.010 | 0.000±0.000 | 0.000±0.000 |
| glm-5.3-flash | preload-anchor | 0.994±0.005 | 0.654±0.005 | 0.671±0.019 | 0.000±0.000 | 0.000±0.000 |
| glm-5.3-flash | preload | 0.991±0.009 | 0.657±0.016 | 0.667±0.023 | 0.000±0.000 | 0.000±0.000 |
| mimo-v2.6-pro | disclosure | 0.994±0.005 | 0.481±0.019 | 0.545±0.012 | 0.000±0.000 | 0.000±0.000 |
| mimo-v2.6-pro | preload-anchor | 1.000±0.000 | 0.494±0.011 | 0.577±0.009 | 0.000±0.000 | 0.000±0.000 |
| mimo-v2.6-pro | preload | 1.000±0.000 | 0.543±0.023 | 0.617±0.009 | 0.000±0.000 | 0.000±0.000 |
| nemotron-3.5-lightning-nvfp4 | disclosure | 0.793±0.005 | 0.682±0.019 | 0.681±0.037 | 0.000±0.000 | 0.000±0.000 |
| nemotron-3.5-lightning-nvfp4 | preload-anchor | 0.855±0.019 | 0.738±0.027 | 0.749±0.062 | 0.000±0.000 | 0.000±0.000 |
| nemotron-3.5-lightning-nvfp4 | preload | 0.747±0.033 | 0.660±0.019 | 0.692±0.034 | 0.444±0.048 | 0.114±0.013 |
| nemotron-3.5-super-vl-nvfp4 | disclosure | 0.932±0.019 | 0.645±0.005 | 0.648±0.012 | 0.000±0.000 | 0.000±0.000 |
| nemotron-3.5-super-vl-nvfp4 | preload-anchor | 0.960±0.019 | 0.793±0.005 | 0.734±0.013 | 0.000±0.000 | 0.000±0.000 |
| nemotron-3.5-super-vl-nvfp4 | preload | 0.981±0.009 | 0.830±0.019 | 0.824±0.014 | 0.028±0.048 | 0.003±0.005 |

## Per-domain recall (worst first)

| model | condition | domain | recall |
|---|---|---|---|
| glm-5.3-flash | disclosure | hpc-skills | 42/45 (0.93) |
| glm-5.3-flash | disclosure | amsc-skills | 59/63 (0.94) |
| glm-5.3-flash | disclosure | basesafe-skills | 51/54 (0.94) |
| glm-5.3-flash | disclosure | academy | 9/9 (1.00) |
| glm-5.3-flash | disclosure | basedata-skills | 45/45 (1.00) |
| glm-5.3-flash | disclosure | baseeval-skills | 72/72 (1.00) |
| glm-5.3-flash | disclosure | literature-search | 9/9 (1.00) |
| glm-5.3-flash | disclosure | multi-agent-systems | 9/9 (1.00) |
| glm-5.3-flash | disclosure | plasma-sim-skills | 18/18 (1.00) |
| glm-5.3-flash | preload-anchor | basesafe-skills | 52/54 (0.96) |
| glm-5.3-flash | preload-anchor | academy | 9/9 (1.00) |
| glm-5.3-flash | preload-anchor | amsc-skills | 63/63 (1.00) |
| glm-5.3-flash | preload-anchor | basedata-skills | 45/45 (1.00) |
| glm-5.3-flash | preload-anchor | baseeval-skills | 72/72 (1.00) |
| glm-5.3-flash | preload-anchor | hpc-skills | 45/45 (1.00) |
| glm-5.3-flash | preload-anchor | literature-search | 9/9 (1.00) |
| glm-5.3-flash | preload-anchor | multi-agent-systems | 9/9 (1.00) |
| glm-5.3-flash | preload-anchor | plasma-sim-skills | 18/18 (1.00) |
| glm-5.3-flash | preload | hpc-skills | 43/45 (0.96) |
| glm-5.3-flash | preload | basesafe-skills | 53/54 (0.98) |
| glm-5.3-flash | preload | academy | 9/9 (1.00) |
| glm-5.3-flash | preload | amsc-skills | 63/63 (1.00) |
| glm-5.3-flash | preload | basedata-skills | 45/45 (1.00) |
| glm-5.3-flash | preload | baseeval-skills | 72/72 (1.00) |
| glm-5.3-flash | preload | literature-search | 9/9 (1.00) |
| glm-5.3-flash | preload | multi-agent-systems | 9/9 (1.00) |
| glm-5.3-flash | preload | plasma-sim-skills | 18/18 (1.00) |
| mimo-v2.6-pro | disclosure | basesafe-skills | 52/54 (0.96) |
| mimo-v2.6-pro | disclosure | academy | 9/9 (1.00) |
| mimo-v2.6-pro | disclosure | amsc-skills | 63/63 (1.00) |
| mimo-v2.6-pro | disclosure | basedata-skills | 45/45 (1.00) |
| mimo-v2.6-pro | disclosure | baseeval-skills | 72/72 (1.00) |
| mimo-v2.6-pro | disclosure | hpc-skills | 45/45 (1.00) |
| mimo-v2.6-pro | disclosure | literature-search | 9/9 (1.00) |
| mimo-v2.6-pro | disclosure | multi-agent-systems | 9/9 (1.00) |
| mimo-v2.6-pro | disclosure | plasma-sim-skills | 18/18 (1.00) |
| mimo-v2.6-pro | preload-anchor | academy | 9/9 (1.00) |
| mimo-v2.6-pro | preload-anchor | amsc-skills | 63/63 (1.00) |
| mimo-v2.6-pro | preload-anchor | basedata-skills | 45/45 (1.00) |
| mimo-v2.6-pro | preload-anchor | baseeval-skills | 72/72 (1.00) |
| mimo-v2.6-pro | preload-anchor | basesafe-skills | 54/54 (1.00) |
| mimo-v2.6-pro | preload-anchor | hpc-skills | 45/45 (1.00) |
| mimo-v2.6-pro | preload-anchor | literature-search | 9/9 (1.00) |
| mimo-v2.6-pro | preload-anchor | multi-agent-systems | 9/9 (1.00) |
| mimo-v2.6-pro | preload-anchor | plasma-sim-skills | 18/18 (1.00) |
| mimo-v2.6-pro | preload | academy | 9/9 (1.00) |
| mimo-v2.6-pro | preload | amsc-skills | 63/63 (1.00) |
| mimo-v2.6-pro | preload | basedata-skills | 45/45 (1.00) |
| mimo-v2.6-pro | preload | baseeval-skills | 72/72 (1.00) |
| mimo-v2.6-pro | preload | basesafe-skills | 54/54 (1.00) |
| mimo-v2.6-pro | preload | hpc-skills | 45/45 (1.00) |
| mimo-v2.6-pro | preload | literature-search | 9/9 (1.00) |
| mimo-v2.6-pro | preload | multi-agent-systems | 9/9 (1.00) |
| mimo-v2.6-pro | preload | plasma-sim-skills | 18/18 (1.00) |
| nemotron-3.5-lightning-nvfp4 | disclosure | academy | 3/9 (0.33) |
| nemotron-3.5-lightning-nvfp4 | disclosure | plasma-sim-skills | 11/18 (0.61) |
| nemotron-3.5-lightning-nvfp4 | disclosure | amsc-skills | 42/63 (0.67) |
| nemotron-3.5-lightning-nvfp4 | disclosure | basesafe-skills | 40/54 (0.74) |
| nemotron-3.5-lightning-nvfp4 | disclosure | hpc-skills | 38/45 (0.84) |
| nemotron-3.5-lightning-nvfp4 | disclosure | basedata-skills | 40/45 (0.89) |
| nemotron-3.5-lightning-nvfp4 | disclosure | baseeval-skills | 65/72 (0.90) |
| nemotron-3.5-lightning-nvfp4 | disclosure | literature-search | 9/9 (1.00) |
| nemotron-3.5-lightning-nvfp4 | disclosure | multi-agent-systems | 9/9 (1.00) |
| nemotron-3.5-lightning-nvfp4 | preload-anchor | amsc-skills | 46/63 (0.73) |
| nemotron-3.5-lightning-nvfp4 | preload-anchor | hpc-skills | 37/45 (0.82) |
| nemotron-3.5-lightning-nvfp4 | preload-anchor | basesafe-skills | 45/54 (0.83) |
| nemotron-3.5-lightning-nvfp4 | preload-anchor | baseeval-skills | 61/72 (0.85) |
| nemotron-3.5-lightning-nvfp4 | preload-anchor | basedata-skills | 43/45 (0.96) |
| nemotron-3.5-lightning-nvfp4 | preload-anchor | academy | 9/9 (1.00) |
| nemotron-3.5-lightning-nvfp4 | preload-anchor | literature-search | 9/9 (1.00) |
| nemotron-3.5-lightning-nvfp4 | preload-anchor | multi-agent-systems | 9/9 (1.00) |
| nemotron-3.5-lightning-nvfp4 | preload-anchor | plasma-sim-skills | 18/18 (1.00) |
| nemotron-3.5-lightning-nvfp4 | preload | baseeval-skills | 41/72 (0.57) |
| nemotron-3.5-lightning-nvfp4 | preload | amsc-skills | 42/63 (0.67) |
| nemotron-3.5-lightning-nvfp4 | preload | hpc-skills | 34/45 (0.76) |
| nemotron-3.5-lightning-nvfp4 | preload | multi-agent-systems | 7/9 (0.78) |
| nemotron-3.5-lightning-nvfp4 | preload | basesafe-skills | 43/54 (0.80) |
| nemotron-3.5-lightning-nvfp4 | preload | basedata-skills | 40/45 (0.89) |
| nemotron-3.5-lightning-nvfp4 | preload | plasma-sim-skills | 17/18 (0.94) |
| nemotron-3.5-lightning-nvfp4 | preload | academy | 9/9 (1.00) |
| nemotron-3.5-lightning-nvfp4 | preload | literature-search | 9/9 (1.00) |
| nemotron-3.5-super-vl-nvfp4 | disclosure | amsc-skills | 52/63 (0.83) |
| nemotron-3.5-super-vl-nvfp4 | disclosure | academy | 8/9 (0.89) |
| nemotron-3.5-super-vl-nvfp4 | disclosure | basesafe-skills | 48/54 (0.89) |
| nemotron-3.5-super-vl-nvfp4 | disclosure | hpc-skills | 41/45 (0.91) |
| nemotron-3.5-super-vl-nvfp4 | disclosure | basedata-skills | 45/45 (1.00) |
| nemotron-3.5-super-vl-nvfp4 | disclosure | baseeval-skills | 72/72 (1.00) |
| nemotron-3.5-super-vl-nvfp4 | disclosure | literature-search | 9/9 (1.00) |
| nemotron-3.5-super-vl-nvfp4 | disclosure | multi-agent-systems | 9/9 (1.00) |
| nemotron-3.5-super-vl-nvfp4 | disclosure | plasma-sim-skills | 18/18 (1.00) |
| nemotron-3.5-super-vl-nvfp4 | preload-anchor | amsc-skills | 58/63 (0.92) |
| nemotron-3.5-super-vl-nvfp4 | preload-anchor | baseeval-skills | 67/72 (0.93) |
| nemotron-3.5-super-vl-nvfp4 | preload-anchor | hpc-skills | 43/45 (0.96) |
| nemotron-3.5-super-vl-nvfp4 | preload-anchor | basesafe-skills | 53/54 (0.98) |
| nemotron-3.5-super-vl-nvfp4 | preload-anchor | academy | 9/9 (1.00) |
| nemotron-3.5-super-vl-nvfp4 | preload-anchor | basedata-skills | 45/45 (1.00) |
| nemotron-3.5-super-vl-nvfp4 | preload-anchor | literature-search | 9/9 (1.00) |
| nemotron-3.5-super-vl-nvfp4 | preload-anchor | multi-agent-systems | 9/9 (1.00) |
| nemotron-3.5-super-vl-nvfp4 | preload-anchor | plasma-sim-skills | 18/18 (1.00) |
| nemotron-3.5-super-vl-nvfp4 | preload | baseeval-skills | 67/72 (0.93) |
| nemotron-3.5-super-vl-nvfp4 | preload | amsc-skills | 62/63 (0.98) |
| nemotron-3.5-super-vl-nvfp4 | preload | academy | 9/9 (1.00) |
| nemotron-3.5-super-vl-nvfp4 | preload | basedata-skills | 45/45 (1.00) |
| nemotron-3.5-super-vl-nvfp4 | preload | basesafe-skills | 54/54 (1.00) |
| nemotron-3.5-super-vl-nvfp4 | preload | hpc-skills | 45/45 (1.00) |
| nemotron-3.5-super-vl-nvfp4 | preload | literature-search | 9/9 (1.00) |
| nemotron-3.5-super-vl-nvfp4 | preload | multi-agent-systems | 9/9 (1.00) |
| nemotron-3.5-super-vl-nvfp4 | preload | plasma-sim-skills | 18/18 (1.00) |

## Top confusions (all models/conditions pooled)

| required | selected instead | count |
|---|---|---|
| i2-api | amsc-mag | 27 |
| pbs | slurm | 24 |
| ai-fingerprint | fingerprinting | 19 |
| globus-compute | perlmutter | 15 |
| iri-api | amsc-python-client | 10 |
| amsc-python-client | perlmutter | 10 |
| uncertainty-quantification | <nothing> | 10 |
| configuration-planner | configuration-creator | 9 |
| amsc-python-client | aurora | 7 |
| configuration-tester | <nothing> | 7 |
| configuration-creator | configuration-planner | 7 |
| amsc-python-client | iri-api | 6 |
| iri-api | perlmutter | 6 |
| battleprint | agentic-vulnerabilities-scan | 4 |
| slurm | pbs | 4 |
