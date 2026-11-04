## Summary (mean±sd over trials)

| model | condition | recall | exact | precision | false-act | unparse |
|---|---|---|---|---|---|---|
| claude-opus-5.5 | preload | 0.997±0.005 | 0.679±0.005 | 0.701±0.001 | 0.000±0.000 | 0.000±0.000 |
| claude-sonnet-5.5 | disclosure | 0.975±0.005 | 0.571±0.014 | 0.599±0.011 | 0.000±0.000 | 0.000±0.000 |
| claude-sonnet-5.5 | preload-anchor | 0.994±0.005 | 0.639±0.000 | 0.649±0.001 | 0.000±0.000 | 0.000±0.000 |
| claude-sonnet-5.5 | preload | 0.985±0.005 | 0.633±0.005 | 0.658±0.003 | 0.000±0.000 | 0.000±0.000 |
| gemini-3.5-flash | disclosure | 0.988±0.005 | 0.522±0.011 | 0.606±0.011 | 0.000±0.000 | 0.000±0.000 |
| gemini-3.5-flash | preload-anchor | 1.000±0.000 | 0.617±0.011 | 0.687±0.009 | 0.000±0.000 | 0.000±0.000 |
| gemini-3.5-flash | preload | 0.978±0.005 | 0.664±0.011 | 0.722±0.008 | 0.000±0.000 | 0.000±0.000 |
| glm-5.3-flash | disclosure | 0.969±0.005 | 0.546±0.032 | 0.594±0.010 | 0.000±0.000 | 0.000±0.000 |
| glm-5.3-flash | preload-anchor | 0.994±0.005 | 0.654±0.005 | 0.671±0.019 | 0.000±0.000 | 0.000±0.000 |
| glm-5.3-flash | preload | 0.991±0.009 | 0.657±0.016 | 0.667±0.023 | 0.000±0.000 | 0.000±0.000 |
| gpt-5.2 | disclosure | 0.935±0.009 | 0.546±0.024 | 0.584±0.019 | 0.000±0.000 | 0.000±0.000 |
| gpt-5.2 | preload-anchor | 0.948±0.014 | 0.716±0.014 | 0.729±0.006 | 0.000±0.000 | 0.000±0.000 |
| gpt-5.2 | preload | 0.951±0.005 | 0.688±0.033 | 0.711±0.037 | 0.167±0.083 | 0.017±0.008 |
| gpt-6-astra | disclosure | 0.991±0.000 | 0.472±0.000 | 0.498±0.000 | 0.000±0.000 | 0.000±0.000 |
| gpt-6-astra | preload-anchor | 1.000±0.000 | 0.648±0.000 | 0.659±0.000 | 0.083±0.000 | 0.000±0.000 |
| gpt-6-astra | preload | 1.000±0.000 | 0.620±0.000 | 0.643±0.000 | 0.000±0.000 | 0.000±0.000 |
| mimo-v2.6-pro | disclosure | 0.994±0.005 | 0.481±0.019 | 0.545±0.012 | 0.000±0.000 | 0.000±0.000 |
| mimo-v2.6-pro | preload-anchor | 1.000±0.000 | 0.494±0.011 | 0.577±0.009 | 0.000±0.000 | 0.000±0.000 |
| mimo-v2.6-pro | preload | 1.000±0.000 | 0.543±0.023 | 0.617±0.009 | 0.000±0.000 | 0.000±0.000 |
| nemotron-3.5-lightning-nvfp4 | disclosure | 0.793±0.005 | 0.682±0.019 | 0.681±0.037 | 0.000±0.000 | 0.000±0.000 |
| nemotron-3.5-lightning-nvfp4 | preload-anchor | 0.855±0.019 | 0.738±0.027 | 0.749±0.062 | 0.000±0.000 | 0.000±0.000 |
| nemotron-3.5-lightning-nvfp4 | preload | 0.747±0.033 | 0.660±0.019 | 0.692±0.034 | 0.444±0.048 | 0.114±0.013 |
| nemotron-3.5-super-vl-nvfp4 | disclosure | 0.932±0.019 | 0.645±0.005 | 0.648±0.012 | 0.000±0.000 | 0.000±0.000 |
| nemotron-3.5-super-vl-nvfp4 | preload-anchor | 0.960±0.019 | 0.793±0.005 | 0.734±0.013 | 0.000±0.000 | 0.000±0.000 |
| nemotron-3.5-super-vl-nvfp4 | preload | 0.981±0.009 | 0.830±0.019 | 0.824±0.014 | 0.028±0.048 | 0.003±0.005 |
| nemotron-3.5-super-vl | disclosure | 0.929±0.014 | 0.673±0.005 | 0.662±0.009 | 0.000±0.000 | 0.000±0.000 |
| nemotron-3.5-super-vl | preload-anchor | 0.917±0.040 | 0.753±0.019 | 0.770±0.022 | 0.000±0.000 | 0.014±0.013 |
| nemotron-3.5-super-vl | preload | 0.938±0.019 | 0.753±0.014 | 0.753±0.018 | 0.000±0.000 | 0.036±0.010 |
| sonnet | disclosure | 0.935±0.000 | 0.583±0.000 | 0.620±0.000 | 0.000±0.000 | 0.000±0.000 |
| sonnet | preload-anchor | 0.972±0.000 | 0.620±0.000 | 0.652±0.000 | 0.000±0.000 | 0.000±0.000 |
| sonnet | preload | 0.981±0.000 | 0.630±0.000 | 0.684±0.000 | 0.000±0.000 | 0.000±0.000 |

## Per-domain recall (worst first)

| model | condition | domain | recall |
|---|---|---|---|
| claude-opus-5.5 | preload | amsc-skills | 62/63 (0.98) |
| claude-opus-5.5 | preload | academy | 9/9 (1.00) |
| claude-opus-5.5 | preload | basedata-skills | 45/45 (1.00) |
| claude-opus-5.5 | preload | baseeval-skills | 72/72 (1.00) |
| claude-opus-5.5 | preload | basesafe-skills | 54/54 (1.00) |
| claude-opus-5.5 | preload | hpc-skills | 45/45 (1.00) |
| claude-opus-5.5 | preload | literature-search | 9/9 (1.00) |
| claude-opus-5.5 | preload | multi-agent-systems | 9/9 (1.00) |
| claude-opus-5.5 | preload | plasma-sim-skills | 18/18 (1.00) |
| claude-sonnet-5.5 | disclosure | amsc-skills | 58/63 (0.92) |
| claude-sonnet-5.5 | disclosure | hpc-skills | 42/45 (0.93) |
| claude-sonnet-5.5 | disclosure | academy | 9/9 (1.00) |
| claude-sonnet-5.5 | disclosure | basedata-skills | 45/45 (1.00) |
| claude-sonnet-5.5 | disclosure | baseeval-skills | 72/72 (1.00) |
| claude-sonnet-5.5 | disclosure | basesafe-skills | 54/54 (1.00) |
| claude-sonnet-5.5 | disclosure | literature-search | 9/9 (1.00) |
| claude-sonnet-5.5 | disclosure | multi-agent-systems | 9/9 (1.00) |
| claude-sonnet-5.5 | disclosure | plasma-sim-skills | 18/18 (1.00) |
| claude-sonnet-5.5 | preload-anchor | amsc-skills | 61/63 (0.97) |
| claude-sonnet-5.5 | preload-anchor | academy | 9/9 (1.00) |
| claude-sonnet-5.5 | preload-anchor | basedata-skills | 45/45 (1.00) |
| claude-sonnet-5.5 | preload-anchor | baseeval-skills | 72/72 (1.00) |
| claude-sonnet-5.5 | preload-anchor | basesafe-skills | 54/54 (1.00) |
| claude-sonnet-5.5 | preload-anchor | hpc-skills | 45/45 (1.00) |
| claude-sonnet-5.5 | preload-anchor | literature-search | 9/9 (1.00) |
| claude-sonnet-5.5 | preload-anchor | multi-agent-systems | 9/9 (1.00) |
| claude-sonnet-5.5 | preload-anchor | plasma-sim-skills | 18/18 (1.00) |
| claude-sonnet-5.5 | preload | amsc-skills | 59/63 (0.94) |
| claude-sonnet-5.5 | preload | hpc-skills | 44/45 (0.98) |
| claude-sonnet-5.5 | preload | academy | 9/9 (1.00) |
| claude-sonnet-5.5 | preload | basedata-skills | 45/45 (1.00) |
| claude-sonnet-5.5 | preload | baseeval-skills | 72/72 (1.00) |
| claude-sonnet-5.5 | preload | basesafe-skills | 54/54 (1.00) |
| claude-sonnet-5.5 | preload | literature-search | 9/9 (1.00) |
| claude-sonnet-5.5 | preload | multi-agent-systems | 9/9 (1.00) |
| claude-sonnet-5.5 | preload | plasma-sim-skills | 18/18 (1.00) |
| gemini-3.5-flash | disclosure | basesafe-skills | 52/54 (0.96) |
| gemini-3.5-flash | disclosure | baseeval-skills | 70/72 (0.97) |
| gemini-3.5-flash | disclosure | academy | 9/9 (1.00) |
| gemini-3.5-flash | disclosure | amsc-skills | 63/63 (1.00) |
| gemini-3.5-flash | disclosure | basedata-skills | 45/45 (1.00) |
| gemini-3.5-flash | disclosure | hpc-skills | 45/45 (1.00) |
| gemini-3.5-flash | disclosure | literature-search | 9/9 (1.00) |
| gemini-3.5-flash | disclosure | multi-agent-systems | 9/9 (1.00) |
| gemini-3.5-flash | disclosure | plasma-sim-skills | 18/18 (1.00) |
| gemini-3.5-flash | preload-anchor | academy | 9/9 (1.00) |
| gemini-3.5-flash | preload-anchor | amsc-skills | 63/63 (1.00) |
| gemini-3.5-flash | preload-anchor | basedata-skills | 45/45 (1.00) |
| gemini-3.5-flash | preload-anchor | baseeval-skills | 72/72 (1.00) |
| gemini-3.5-flash | preload-anchor | basesafe-skills | 54/54 (1.00) |
| gemini-3.5-flash | preload-anchor | hpc-skills | 45/45 (1.00) |
| gemini-3.5-flash | preload-anchor | literature-search | 9/9 (1.00) |
| gemini-3.5-flash | preload-anchor | multi-agent-systems | 9/9 (1.00) |
| gemini-3.5-flash | preload-anchor | plasma-sim-skills | 18/18 (1.00) |
| gemini-3.5-flash | preload | basesafe-skills | 47/54 (0.87) |
| gemini-3.5-flash | preload | academy | 9/9 (1.00) |
| gemini-3.5-flash | preload | amsc-skills | 63/63 (1.00) |
| gemini-3.5-flash | preload | basedata-skills | 45/45 (1.00) |
| gemini-3.5-flash | preload | baseeval-skills | 72/72 (1.00) |
| gemini-3.5-flash | preload | hpc-skills | 45/45 (1.00) |
| gemini-3.5-flash | preload | literature-search | 9/9 (1.00) |
| gemini-3.5-flash | preload | multi-agent-systems | 9/9 (1.00) |
| gemini-3.5-flash | preload | plasma-sim-skills | 18/18 (1.00) |
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
| gpt-5.2 | disclosure | academy | 5/9 (0.56) |
| gpt-5.2 | disclosure | plasma-sim-skills | 16/18 (0.89) |
| gpt-5.2 | disclosure | hpc-skills | 41/45 (0.91) |
| gpt-5.2 | disclosure | basedata-skills | 42/45 (0.93) |
| gpt-5.2 | disclosure | amsc-skills | 59/63 (0.94) |
| gpt-5.2 | disclosure | baseeval-skills | 68/72 (0.94) |
| gpt-5.2 | disclosure | basesafe-skills | 54/54 (1.00) |
| gpt-5.2 | disclosure | literature-search | 9/9 (1.00) |
| gpt-5.2 | disclosure | multi-agent-systems | 9/9 (1.00) |
| gpt-5.2 | preload-anchor | baseeval-skills | 63/72 (0.88) |
| gpt-5.2 | preload-anchor | hpc-skills | 41/45 (0.91) |
| gpt-5.2 | preload-anchor | amsc-skills | 60/63 (0.95) |
| gpt-5.2 | preload-anchor | basedata-skills | 44/45 (0.98) |
| gpt-5.2 | preload-anchor | academy | 9/9 (1.00) |
| gpt-5.2 | preload-anchor | basesafe-skills | 54/54 (1.00) |
| gpt-5.2 | preload-anchor | literature-search | 9/9 (1.00) |
| gpt-5.2 | preload-anchor | multi-agent-systems | 9/9 (1.00) |
| gpt-5.2 | preload-anchor | plasma-sim-skills | 18/18 (1.00) |
| gpt-5.2 | preload | baseeval-skills | 64/72 (0.89) |
| gpt-5.2 | preload | amsc-skills | 57/63 (0.90) |
| gpt-5.2 | preload | basedata-skills | 44/45 (0.98) |
| gpt-5.2 | preload | hpc-skills | 44/45 (0.98) |
| gpt-5.2 | preload | academy | 9/9 (1.00) |
| gpt-5.2 | preload | basesafe-skills | 54/54 (1.00) |
| gpt-5.2 | preload | literature-search | 9/9 (1.00) |
| gpt-5.2 | preload | multi-agent-systems | 9/9 (1.00) |
| gpt-5.2 | preload | plasma-sim-skills | 18/18 (1.00) |
| gpt-6-astra | disclosure | basesafe-skills | 17/18 (0.94) |
| gpt-6-astra | disclosure | academy | 3/3 (1.00) |
| gpt-6-astra | disclosure | amsc-skills | 21/21 (1.00) |
| gpt-6-astra | disclosure | basedata-skills | 15/15 (1.00) |
| gpt-6-astra | disclosure | baseeval-skills | 24/24 (1.00) |
| gpt-6-astra | disclosure | hpc-skills | 15/15 (1.00) |
| gpt-6-astra | disclosure | literature-search | 3/3 (1.00) |
| gpt-6-astra | disclosure | multi-agent-systems | 3/3 (1.00) |
| gpt-6-astra | disclosure | plasma-sim-skills | 6/6 (1.00) |
| gpt-6-astra | preload-anchor | academy | 3/3 (1.00) |
| gpt-6-astra | preload-anchor | amsc-skills | 21/21 (1.00) |
| gpt-6-astra | preload-anchor | basedata-skills | 15/15 (1.00) |
| gpt-6-astra | preload-anchor | baseeval-skills | 24/24 (1.00) |
| gpt-6-astra | preload-anchor | basesafe-skills | 18/18 (1.00) |
| gpt-6-astra | preload-anchor | hpc-skills | 15/15 (1.00) |
| gpt-6-astra | preload-anchor | literature-search | 3/3 (1.00) |
| gpt-6-astra | preload-anchor | multi-agent-systems | 3/3 (1.00) |
| gpt-6-astra | preload-anchor | plasma-sim-skills | 6/6 (1.00) |
| gpt-6-astra | preload | academy | 3/3 (1.00) |
| gpt-6-astra | preload | amsc-skills | 21/21 (1.00) |
| gpt-6-astra | preload | basedata-skills | 15/15 (1.00) |
| gpt-6-astra | preload | baseeval-skills | 24/24 (1.00) |
| gpt-6-astra | preload | basesafe-skills | 18/18 (1.00) |
| gpt-6-astra | preload | hpc-skills | 15/15 (1.00) |
| gpt-6-astra | preload | literature-search | 3/3 (1.00) |
| gpt-6-astra | preload | multi-agent-systems | 3/3 (1.00) |
| gpt-6-astra | preload | plasma-sim-skills | 6/6 (1.00) |
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
| nemotron-3.5-super-vl | disclosure | amsc-skills | 53/63 (0.84) |
| nemotron-3.5-super-vl | disclosure | hpc-skills | 39/45 (0.87) |
| nemotron-3.5-super-vl | disclosure | academy | 8/9 (0.89) |
| nemotron-3.5-super-vl | disclosure | basesafe-skills | 51/54 (0.94) |
| nemotron-3.5-super-vl | disclosure | baseeval-skills | 69/72 (0.96) |
| nemotron-3.5-super-vl | disclosure | basedata-skills | 45/45 (1.00) |
| nemotron-3.5-super-vl | disclosure | literature-search | 9/9 (1.00) |
| nemotron-3.5-super-vl | disclosure | multi-agent-systems | 9/9 (1.00) |
| nemotron-3.5-super-vl | disclosure | plasma-sim-skills | 18/18 (1.00) |
| nemotron-3.5-super-vl | preload-anchor | amsc-skills | 55/63 (0.87) |
| nemotron-3.5-super-vl | preload-anchor | academy | 8/9 (0.89) |
| nemotron-3.5-super-vl | preload-anchor | literature-search | 8/9 (0.89) |
| nemotron-3.5-super-vl | preload-anchor | baseeval-skills | 65/72 (0.90) |
| nemotron-3.5-super-vl | preload-anchor | basesafe-skills | 49/54 (0.91) |
| nemotron-3.5-super-vl | preload-anchor | plasma-sim-skills | 17/18 (0.94) |
| nemotron-3.5-super-vl | preload-anchor | basedata-skills | 43/45 (0.96) |
| nemotron-3.5-super-vl | preload-anchor | hpc-skills | 43/45 (0.96) |
| nemotron-3.5-super-vl | preload-anchor | multi-agent-systems | 9/9 (1.00) |
| nemotron-3.5-super-vl | preload | multi-agent-systems | 6/9 (0.67) |
| nemotron-3.5-super-vl | preload | baseeval-skills | 64/72 (0.89) |
| nemotron-3.5-super-vl | preload | basedata-skills | 41/45 (0.91) |
| nemotron-3.5-super-vl | preload | amsc-skills | 60/63 (0.95) |
| nemotron-3.5-super-vl | preload | hpc-skills | 44/45 (0.98) |
| nemotron-3.5-super-vl | preload | basesafe-skills | 53/54 (0.98) |
| nemotron-3.5-super-vl | preload | academy | 9/9 (1.00) |
| nemotron-3.5-super-vl | preload | literature-search | 9/9 (1.00) |
| nemotron-3.5-super-vl | preload | plasma-sim-skills | 18/18 (1.00) |
| sonnet | disclosure | hpc-skills | 13/15 (0.87) |
| sonnet | disclosure | amsc-skills | 19/21 (0.90) |
| sonnet | disclosure | baseeval-skills | 22/24 (0.92) |
| sonnet | disclosure | basesafe-skills | 17/18 (0.94) |
| sonnet | disclosure | academy | 3/3 (1.00) |
| sonnet | disclosure | basedata-skills | 15/15 (1.00) |
| sonnet | disclosure | literature-search | 3/3 (1.00) |
| sonnet | disclosure | multi-agent-systems | 3/3 (1.00) |
| sonnet | disclosure | plasma-sim-skills | 6/6 (1.00) |
| sonnet | preload-anchor | hpc-skills | 14/15 (0.93) |
| sonnet | preload-anchor | basesafe-skills | 17/18 (0.94) |
| sonnet | preload-anchor | amsc-skills | 20/21 (0.95) |
| sonnet | preload-anchor | academy | 3/3 (1.00) |
| sonnet | preload-anchor | basedata-skills | 15/15 (1.00) |
| sonnet | preload-anchor | baseeval-skills | 24/24 (1.00) |
| sonnet | preload-anchor | literature-search | 3/3 (1.00) |
| sonnet | preload-anchor | multi-agent-systems | 3/3 (1.00) |
| sonnet | preload-anchor | plasma-sim-skills | 6/6 (1.00) |
| sonnet | preload | hpc-skills | 14/15 (0.93) |
| sonnet | preload | amsc-skills | 20/21 (0.95) |
| sonnet | preload | academy | 3/3 (1.00) |
| sonnet | preload | basedata-skills | 15/15 (1.00) |
| sonnet | preload | baseeval-skills | 24/24 (1.00) |
| sonnet | preload | basesafe-skills | 18/18 (1.00) |
| sonnet | preload | literature-search | 3/3 (1.00) |
| sonnet | preload | multi-agent-systems | 3/3 (1.00) |
| sonnet | preload | plasma-sim-skills | 6/6 (1.00) |

## Top confusions (all models/conditions pooled)

| required | selected instead | count |
|---|---|---|
| pbs | slurm | 45 |
| i2-api | amsc-mag | 34 |
| globus-compute | perlmutter | 30 |
| ai-fingerprint | fingerprinting | 25 |
| configuration-planner | configuration-creator | 24 |
| data-exploration | configuration-creator | 19 |
| iri-api | amsc-python-client | 19 |
| amsc-python-client | iri-api | 17 |
| globus-compute | iri-api | 12 |
| amsc-python-client | perlmutter | 12 |
| amsc-python-client | pbs | 11 |
| skill-creator | <nothing> | 11 |
| uncertainty-quantification | <nothing> | 11 |
| globus-compute | amsc-python-client | 10 |
| iri-api | perlmutter | 9 |
