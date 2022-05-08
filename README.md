# Temporal Link Prediction using Tensor Factorization

## Overview
Due to the simple fact that no single country can produce everything that is required by its economy, countries trade with each other. These trades are broadly categorized either as merchandise trade or service trade and the standard currency for all such international trade is the US dollar. It is often of strategic interest to forecast a country’s trade behaviors given their trade history to either consolidate and reevaluate one’s foreign policy if the said country is friendly or to devise appropriate economic checks and safeguards if the country is hostile. In this project, we aim to model international trade patterns as a graph and study the temporal dynamics of this graph to predict future behavior of any particular country. For simplicity, we focus just on the petroleum trade network. We use tensor factorization and exponential smoothing to obtain predictions for global petroleum trade and obtain a log RMSE of up to 3.827. These results are contained in the notebook `tensor-factorization-experiment.ipynb`.

## Data
The data for country-country trade is obtained from the [United Nations Comtrade Portal](https://comtrade.un.org/data/) which provides data on the international trade of several commodities including petroleum, metals, and foods. This data is available using their open access Application Programming Interface (API) which supports filtering by Time Period, Source Country or the Reporter, Target Country or the Partner, Trade flow which is either Import, Export or Reexport, and the Harmonized System Code aka the HS Code. Of particular interest is the HS Code which essentially is a universal way of categorizing traded products. Since this study is only concerned with the trade of Petroleum, we set the HS Code value to 27 (which signifies the category of "Mineral fuels, mineral oils and products of their distillation; bituminous substances; mineral waxes" of which Petroleum is also a part of.

We thus downloaded the trade dataset for the period of 2012 to 2021 and used data from 2012-2018 to train the model and 2019, 2020, and 2021 to test the model. Special care was given to not exceed the recommended rate limit imposed by the Comtrade portal and scrape the data ethically.

## References
https://www.sci-hub.st/10.1007/978-3-642-28320-8_9
https://www.osti.gov/servlets/purl/1141980
