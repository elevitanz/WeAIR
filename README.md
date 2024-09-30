# WeAIR
If you use this code please cite the related article: 

The repository contains the code used in the paper: "WeAIR: Wearable Swarm Sensors for Air Quality
Monitoring to Foster Citizens’ Awareness of Climate Change". Please cite the paper when using the code.

Below a detailed description of the repository:

In the 'data' folder you will find all the CSV files obtained from the monitoring campaign using our mobile sensor. In particular, there are both the daily CSV files and the total one. In the folder, there is also a table reporting the minimum and maximum values measured by the sensor for each indicator.

In the 'sensor' folder there are images that reference the architecture and specifications of the sensor, as well as a graphical abstract of the entire project.

In the 'heatmap' folder, you'll find maps of Siena depicting the total route taken during the 20 days of monitoring. Specifically, there's a heatmap for each indicator to visualize the spatial evolution of the indicators.

In the 'plot' folder, you'll find temporal plots depicting the total dataset taken during the 20 days of monitoring. Specifically, there's a figure for each indicator to visualize the temporal evolution of the indicators.

In the 'occurrences' folder, there are two histograms related to the analysis of specific monitoring hours over the 20-day period.

In the 'fixed_versus_mobile_plots' folder, there are comparisons between some mobile monitoring conducted on February 18 near the fixed station at Viale Bracci and the data from the fixed station itself. Specifically, there are plots related to CO and NO2.

In the 'predictions' folder, there are some predictions plots made by the neural network regarding the locations. Specifically, in one case, the input consists of the average of all data collected for each indicator on January 25, while in another case, the input comprises all monitoring data without the locations.

In the 'video' folder, there are trajectories of indicators as heatmaps evolving over time with hourly frequency.

In the 'python' folder there are all the codes related to preprocessing and dataset synchronization, as well as all the scripts related to plots, heatmaps and videos.

In the 'Models.zip' folder, there are all the daily predictive models in the keras.h5 format.
