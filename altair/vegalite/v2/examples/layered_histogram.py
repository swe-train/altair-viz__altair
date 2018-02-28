"""
Layered Histogram
=================
This example shows how to make a layered histogram in Altair.
"""

import pandas as pd
import altair as alt
import numpy as np
np.random.seed(42)

# Generating Data
df = pd.DataFrame({'Trial A':np.random.normal(0, 0.8, 1000),
                   'Trial B':np.random.normal(-2, 1, 1000),
                   'Trial C':np.random.normal(3, 2, 1000)})

# Tidying Data
df = pd.melt(df, id_vars=df.index.name, 
             value_vars=df.columns,
             var_name = 'Experiment',
             value_name='Measurement')

chart = alt.Chart(df).mark_bar(opacity=0.3).encode(
    x=alt.X('Measurement',bin = alt.BinParams(maxbins=100)),
    y=alt.Y('count(*):Q', stack=None), 
    color=alt.Color('Experiment', 
                    scale=alt.Scale(range=['#0000ff', 
                                           '#008000', 
                                           '#ff0000'])
                   )
).configure_bar(binSpacing=0)