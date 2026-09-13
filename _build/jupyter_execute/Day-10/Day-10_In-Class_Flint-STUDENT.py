#!/usr/bin/env python
# coding: utf-8

# # Day 10 In-class Assignment: Get the Lead Out: Understanding The Water Crisis in Flint, MI

# ### <p style="text-align: right;"> &#9989; Put your name here.</p>
# 
# #### <p style="text-align: right;"> &#9989; Put your group member names here.</p>

# <div align="center"><img src="https://assets1.cbsnewsstatic.com/hub/i/r/2017/09/21/d348dfb2-b44c-49de-95c5-893fdf143ce6/thumbnail/620x349/d43e72275d7f4c4966124cfd9e66e22a/0921-eve-flinthearing-reynolds.jpg" width=800px></div>
# 

# ## Learning Goals:
# 
# By the end of this assignment you should be able to:
# * Use Pandas to filter data to select particular subsets of interest
# * Articulate, based on your own perception, what you thinks makes a data visualization "good" versus "bad"
# * Use data to support a claim or make an argument

# ## Assignment instructions
# 
# Work with your group to complete this assignment. Instructions for submitting this assignment are at the end of the notebook. The assignment is due at the end of class.

# Today we want you to think about what the data is telling you, but still use coding to help you; and, use some of the visualization ideas you explored above. We'll be looking at the publicly released [Flint Water Quality dataset](http://flintwaterstudy.org/2015/12/complete-dataset-lead-results-in-tap-water-for-271-flint-samples/). The water testing method involves collecting three different bottles worth of water.

# In[ ]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np
import pandas as pd

# Loading the data
# flint_data = pd.read_json("""[{"SampleID":1,"Zip Code":48504,"Ward":6,"PbBottle1_ppb":0.344,"PbBottle2_ppb":0.226,"PbBottle3_ppb":0.145},{"SampleID":2,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":8.133,"PbBottle2_ppb":10.77,"PbBottle3_ppb":2.761},{"SampleID":4,"Zip Code":48504,"Ward":1,"PbBottle1_ppb":1.111,"PbBottle2_ppb":0.11,"PbBottle3_ppb":0.123},{"SampleID":5,"Zip Code":48507,"Ward":8,"PbBottle1_ppb":8.007,"PbBottle2_ppb":7.446,"PbBottle3_ppb":3.384},{"SampleID":6,"Zip Code":48505,"Ward":3,"PbBottle1_ppb":1.951,"PbBottle2_ppb":0.048,"PbBottle3_ppb":0.035},{"SampleID":7,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":7.2,"PbBottle2_ppb":1.4,"PbBottle3_ppb":0.2},{"SampleID":8,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":40.63,"PbBottle2_ppb":9.726,"PbBottle3_ppb":6.132},{"SampleID":9,"Zip Code":48503,"Ward":5,"PbBottle1_ppb":1.1,"PbBottle2_ppb":2.5,"PbBottle3_ppb":0.1},{"SampleID":12,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":10.6,"PbBottle2_ppb":1.038,"PbBottle3_ppb":1.294},{"SampleID":13,"Zip Code":48505,"Ward":3,"PbBottle1_ppb":6.2,"PbBottle2_ppb":4.2,"PbBottle3_ppb":2.3},{"SampleID":15,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":4.358,"PbBottle2_ppb":0.822,"PbBottle3_ppb":0.147},{"SampleID":16,"Zip Code":48505,"Ward":5,"PbBottle1_ppb":24.37,"PbBottle2_ppb":8.796,"PbBottle3_ppb":4.347},{"SampleID":17,"Zip Code":48505,"Ward":2,"PbBottle1_ppb":6.609,"PbBottle2_ppb":5.752,"PbBottle3_ppb":1.433},{"SampleID":18,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":4.062,"PbBottle2_ppb":1.099,"PbBottle3_ppb":1.085},{"SampleID":19,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":2.484,"PbBottle2_ppb":0.72,"PbBottle3_ppb":0.565},{"SampleID":20,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":0.438,"PbBottle2_ppb":1.046,"PbBottle3_ppb":0.511},{"SampleID":21,"Zip Code":48503,"Ward":5,"PbBottle1_ppb":1.29,"PbBottle2_ppb":0.243,"PbBottle3_ppb":0.225},{"SampleID":22,"Zip Code":48504,"Ward":6,"PbBottle1_ppb":0.548,"PbBottle2_ppb":0.622,"PbBottle3_ppb":0.361},{"SampleID":23,"Zip Code":48504,"Ward":2,"PbBottle1_ppb":3.131,"PbBottle2_ppb":0.674,"PbBottle3_ppb":0.683},{"SampleID":24,"Zip Code":48504,"Ward":6,"PbBottle1_ppb":120,"PbBottle2_ppb":239.7,"PbBottle3_ppb":29.71},{"SampleID":25,"Zip Code":48505,"Ward":1,"PbBottle1_ppb":2.911,"PbBottle2_ppb":0.406,"PbBottle3_ppb":0.237},{"SampleID":26,"Zip Code":48505,"Ward":5,"PbBottle1_ppb":16.52,"PbBottle2_ppb":10.26,"PbBottle3_ppb":2.762},{"SampleID":27,"Zip Code":48505,"Ward":1,"PbBottle1_ppb":1.984,"PbBottle2_ppb":1.13,"PbBottle3_ppb":0.712},{"SampleID":28,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":5.367,"PbBottle2_ppb":2.474,"PbBottle3_ppb":1.616},{"SampleID":29,"Zip Code":48504,"Ward":2,"PbBottle1_ppb":5.5,"PbBottle2_ppb":8.4,"PbBottle3_ppb":2.4},{"SampleID":30,"Zip Code":48506,"Ward":4,"PbBottle1_ppb":0.639,"PbBottle2_ppb":0.223,"PbBottle3_ppb":0.194},{"SampleID":31,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":6.087,"PbBottle2_ppb":28.87,"PbBottle3_ppb":2.13,"Notes":"*house sampled twice"},{"SampleID":31,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":10.32,"PbBottle2_ppb":13.47,"PbBottle3_ppb":18.19,"Notes":"*house sampled twice"},{"SampleID":33,"Zip Code":48503,"Ward":6,"PbBottle1_ppb":66.88,"PbBottle2_ppb":2.662,"PbBottle3_ppb":2.082},{"SampleID":34,"Zip Code":48505,"Ward":1,"PbBottle1_ppb":20.41,"PbBottle2_ppb":3.543,"PbBottle3_ppb":2.344},{"SampleID":35,"Zip Code":48504,"Ward":6,"PbBottle1_ppb":109.6,"PbBottle2_ppb":80.47,"PbBottle3_ppb":94.52},{"SampleID":36,"Zip Code":48503,"Ward":8,"PbBottle1_ppb":5.06,"PbBottle2_ppb":3.406,"PbBottle3_ppb":4.088},{"SampleID":37,"Zip Code":48504,"Ward":2,"PbBottle1_ppb":2.774,"PbBottle2_ppb":0.21,"PbBottle3_ppb":0.264},{"SampleID":38,"Zip Code":48505,"Ward":3,"PbBottle1_ppb":4.453,"PbBottle2_ppb":3.679,"PbBottle3_ppb":3.523},{"SampleID":39,"Zip Code":48505,"Ward":1,"PbBottle1_ppb":0.4,"PbBottle2_ppb":0.3,"PbBottle3_ppb":0.7},{"SampleID":40,"Zip Code":48529,"Ward":9,"PbBottle1_ppb":0.974,"PbBottle2_ppb":0.142,"PbBottle3_ppb":0.118},{"SampleID":41,"Zip Code":48505,"Ward":5,"PbBottle1_ppb":3.228,"PbBottle2_ppb":2.534,"PbBottle3_ppb":2.222},{"SampleID":42,"Zip Code":48505,"Ward":2,"PbBottle1_ppb":12.55,"PbBottle2_ppb":4.132,"PbBottle3_ppb":0.12},{"SampleID":43,"Zip Code":48505,"Ward":3,"PbBottle1_ppb":0.501,"PbBottle2_ppb":0.156,"PbBottle3_ppb":15.14},{"SampleID":44,"Zip Code":48504,"Ward":2,"PbBottle1_ppb":2.448,"PbBottle2_ppb":0.373,"PbBottle3_ppb":0.288},{"SampleID":45,"Zip Code":48505,"Ward":3,"PbBottle1_ppb":5.508,"PbBottle2_ppb":5.157,"PbBottle3_ppb":2.621},{"SampleID":46,"Zip Code":48504,"Ward":6,"PbBottle1_ppb":1.293,"PbBottle2_ppb":0.441,"PbBottle3_ppb":0.281},{"SampleID":47,"Zip Code":48505,"Ward":1,"PbBottle1_ppb":4.699,"PbBottle2_ppb":1.395,"PbBottle3_ppb":0.329},{"SampleID":48,"Zip Code":48504,"Ward":6,"PbBottle1_ppb":6.093,"PbBottle2_ppb":2.682,"PbBottle3_ppb":1.458},{"SampleID":49,"Zip Code":48504,"Ward":2,"PbBottle1_ppb":0.8,"PbBottle2_ppb":0.8,"PbBottle3_ppb":0.5},{"SampleID":50,"Zip Code":48503,"Ward":5,"PbBottle1_ppb":1.626,"PbBottle2_ppb":1.332,"PbBottle3_ppb":0.327},{"SampleID":51,"Zip Code":48507,"Ward":8,"PbBottle1_ppb":2.576,"PbBottle2_ppb":2.852,"PbBottle3_ppb":1.48},{"SampleID":52,"Zip Code":48504,"Ward":1,"PbBottle1_ppb":2.362,"PbBottle2_ppb":0.467,"PbBottle3_ppb":0.339},{"SampleID":53,"Zip Code":48503,"Ward":5,"PbBottle1_ppb":1.585,"PbBottle2_ppb":0.494,"PbBottle3_ppb":1.232},{"SampleID":54,"Zip Code":48506,"Ward":4,"PbBottle1_ppb":3.058,"PbBottle2_ppb":1.808,"PbBottle3_ppb":1.169},{"SampleID":55,"Zip Code":48506,"Ward":4,"PbBottle1_ppb":2.423,"PbBottle2_ppb":0.393,"PbBottle3_ppb":0.373},{"SampleID":56,"Zip Code":48503,"Ward":8,"PbBottle1_ppb":30.91,"PbBottle2_ppb":42.58,"PbBottle3_ppb":44.6},{"SampleID":57,"Zip Code":48503,"Ward":8,"PbBottle1_ppb":4.47,"PbBottle2_ppb":3.649,"PbBottle3_ppb":1},{"SampleID":58,"Zip Code":48505,"Ward":1,"PbBottle1_ppb":2.172,"PbBottle2_ppb":1.76,"PbBottle3_ppb":1.44},{"SampleID":59,"Zip Code":48505,"Ward":3,"PbBottle1_ppb":1.8,"PbBottle2_ppb":0.5,"PbBottle3_ppb":0.2},{"SampleID":63,"Zip Code":48503,"Ward":5,"PbBottle1_ppb":0.965,"PbBottle2_ppb":0.166,"PbBottle3_ppb":0.319},{"SampleID":65,"Zip Code":48505,"Ward":1,"PbBottle1_ppb":7.636,"PbBottle2_ppb":5.206,"PbBottle3_ppb":9.239},{"SampleID":66,"Zip Code":48506,"Ward":3,"PbBottle1_ppb":3.158,"PbBottle2_ppb":1.948,"PbBottle3_ppb":2.802},{"SampleID":67,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":105.3,"PbBottle2_ppb":12.84,"PbBottle3_ppb":4.534},{"SampleID":68,"Zip Code":48506,"Ward":3,"PbBottle1_ppb":4.476,"PbBottle2_ppb":0.355,"PbBottle3_ppb":0.334},{"SampleID":69,"Zip Code":48504,"Ward":1,"PbBottle1_ppb":2.828,"PbBottle2_ppb":6.694,"PbBottle3_ppb":20.99},{"SampleID":71,"Zip Code":48503,"Ward":5,"PbBottle1_ppb":2.481,"PbBottle2_ppb":3.86,"PbBottle3_ppb":24.64},{"SampleID":72,"Zip Code":48507,"Ward":5,"PbBottle1_ppb":11.52,"PbBottle2_ppb":0.288,"PbBottle3_ppb":0.215},{"SampleID":73,"Zip Code":48507,"Ward":8,"PbBottle1_ppb":3.784,"PbBottle2_ppb":0.292,"PbBottle3_ppb":0.258},{"SampleID":74,"Zip Code":48503,"Ward":5,"PbBottle1_ppb":1.344,"PbBottle2_ppb":0.729,"PbBottle3_ppb":1.226},{"SampleID":75,"Zip Code":48504,"Ward":6,"PbBottle1_ppb":11.93,"PbBottle2_ppb":9.645,"PbBottle3_ppb":3.514},{"SampleID":76,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":10.96,"PbBottle2_ppb":7.744,"PbBottle3_ppb":4.16},{"SampleID":77,"Zip Code":48504,"Ward":6,"PbBottle1_ppb":3.341,"PbBottle2_ppb":0.555,"PbBottle3_ppb":0.917},{"SampleID":78,"Zip Code":48503,"Ward":5,"PbBottle1_ppb":1.229,"PbBottle2_ppb":1.192,"PbBottle3_ppb":0.218},{"SampleID":79,"Zip Code":48503,"Ward":6,"PbBottle1_ppb":6.3,"PbBottle2_ppb":1.1,"PbBottle3_ppb":0.3,"Notes":"*house sampled twice"},{"SampleID":79,"Zip Code":48503,"Ward":6,"PbBottle1_ppb":5.153,"PbBottle2_ppb":0.385,"PbBottle3_ppb":0.322,"Notes":"*house sampled twice"},{"SampleID":80,"Zip Code":48504,"Ward":6,"PbBottle1_ppb":6.054,"PbBottle2_ppb":0.927,"PbBottle3_ppb":0.676},{"SampleID":82,"Zip Code":48504,"Ward":2,"PbBottle1_ppb":31.14,"PbBottle2_ppb":4.73,"PbBottle3_ppb":3.188},{"SampleID":83,"Zip Code":48504,"Ward":6,"PbBottle1_ppb":102.7,"PbBottle2_ppb":9.894,"PbBottle3_ppb":3.133},{"SampleID":84,"Zip Code":48504,"Ward":2,"PbBottle1_ppb":1.38,"PbBottle2_ppb":3.734,"PbBottle3_ppb":0.524},{"SampleID":85,"Zip Code":48505,"Ward":3,"PbBottle1_ppb":1.132,"PbBottle2_ppb":2.17,"PbBottle3_ppb":0.465},{"SampleID":87,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":3.232,"PbBottle2_ppb":2.989,"PbBottle3_ppb":1.927},{"SampleID":88,"Zip Code":48532,"Ward":8,"PbBottle1_ppb":0.507,"PbBottle2_ppb":2.315,"PbBottle3_ppb":0.231},{"SampleID":90,"Zip Code":48506,"Ward":4,"PbBottle1_ppb":8.561,"PbBottle2_ppb":5.141,"PbBottle3_ppb":4.724},{"SampleID":91,"Zip Code":48505,"Ward":3,"PbBottle1_ppb":9.997,"PbBottle2_ppb":0.983,"PbBottle3_ppb":0.611},{"SampleID":92,"Zip Code":48504,"Ward":1,"PbBottle1_ppb":4.152,"PbBottle2_ppb":0.758,"PbBottle3_ppb":0.433},{"SampleID":93,"Zip Code":48504,"Ward":2,"PbBottle1_ppb":75.82,"PbBottle2_ppb":11.65,"PbBottle3_ppb":3.942},{"SampleID":95,"Zip Code":48506,"Ward":4,"PbBottle1_ppb":138.8,"PbBottle2_ppb":2.745,"PbBottle3_ppb":0.797},{"SampleID":96,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":0.8,"PbBottle2_ppb":0.2,"PbBottle3_ppb":0.2},{"SampleID":97,"Zip Code":48504,"Ward":2,"PbBottle1_ppb":7.244,"PbBottle2_ppb":1051,"PbBottle3_ppb":1.328},{"SampleID":98,"Zip Code":48506,"Ward":3,"PbBottle1_ppb":1.621,"PbBottle2_ppb":0.3,"PbBottle3_ppb":0.238},{"SampleID":99,"Zip Code":48505,"Ward":1,"PbBottle1_ppb":1.032,"PbBottle2_ppb":0.363,"PbBottle3_ppb":0.216},{"SampleID":100,"Zip Code":48504,"Ward":2,"PbBottle1_ppb":0.866,"PbBottle2_ppb":0.292,"PbBottle3_ppb":0.269},{"SampleID":101,"Zip Code":48504,"Ward":2,"PbBottle1_ppb":2.525,"PbBottle2_ppb":0.59,"PbBottle3_ppb":0.438},{"SampleID":102,"Zip Code":48505,"Ward":5,"PbBottle1_ppb":9.408,"PbBottle2_ppb":4.444,"PbBottle3_ppb":3.935},{"SampleID":103,"Zip Code":48505,"Ward":0,"PbBottle1_ppb":0.739,"PbBottle2_ppb":4.883,"PbBottle3_ppb":0.953},{"SampleID":104,"Zip Code":48505,"Ward":1,"PbBottle1_ppb":0.9,"PbBottle2_ppb":0.2,"PbBottle3_ppb":0.1},{"SampleID":105,"Zip Code":48504,"Ward":2,"PbBottle1_ppb":1.403,"PbBottle2_ppb":0.142,"PbBottle3_ppb":0.121},{"SampleID":106,"Zip Code":48503,"Ward":8,"PbBottle1_ppb":5.655,"PbBottle2_ppb":5.882,"PbBottle3_ppb":10.66},{"SampleID":107,"Zip Code":48505,"Ward":2,"PbBottle1_ppb":31.06,"PbBottle2_ppb":8.578,"PbBottle3_ppb":3.176},{"SampleID":108,"Zip Code":48506,"Ward":4,"PbBottle1_ppb":1.469,"PbBottle2_ppb":0.291,"PbBottle3_ppb":0.25},{"SampleID":109,"Zip Code":48505,"Ward":1,"PbBottle1_ppb":23.85,"PbBottle2_ppb":2.301,"PbBottle3_ppb":1.62},{"SampleID":110,"Zip Code":48505,"Ward":2,"PbBottle1_ppb":9.766,"PbBottle2_ppb":11.13,"PbBottle3_ppb":7.144},{"SampleID":111,"Zip Code":48505,"Ward":1,"PbBottle1_ppb":4.69,"PbBottle2_ppb":0.953,"PbBottle3_ppb":0.929},{"SampleID":112,"Zip Code":48505,"Ward":3,"PbBottle1_ppb":4.066,"PbBottle2_ppb":5.894,"PbBottle3_ppb":4.76},{"SampleID":113,"Zip Code":48505,"Ward":1,"PbBottle1_ppb":0.846,"PbBottle2_ppb":0.455,"PbBottle3_ppb":0.366},{"SampleID":114,"Zip Code":48505,"Ward":1,"PbBottle1_ppb":2.054,"PbBottle2_ppb":3.978,"PbBottle3_ppb":0.355},{"SampleID":115,"Zip Code":48506,"Ward":7,"PbBottle1_ppb":3.744,"PbBottle2_ppb":5.592,"PbBottle3_ppb":2.476},{"SampleID":116,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":12.9,"PbBottle2_ppb":2.202,"PbBottle3_ppb":1.667},{"SampleID":117,"Zip Code":48505,"Ward":1,"PbBottle1_ppb":0.543,"PbBottle2_ppb":0.183,"PbBottle3_ppb":0.162},{"SampleID":118,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":6.877,"PbBottle2_ppb":2.984,"PbBottle3_ppb":2.201},{"SampleID":119,"Zip Code":48505,"Ward":1,"PbBottle1_ppb":0.552,"PbBottle2_ppb":0.19,"PbBottle3_ppb":0.205},{"SampleID":121,"Zip Code":48506,"Ward":3,"PbBottle1_ppb":59,"PbBottle2_ppb":2.9,"PbBottle3_ppb":0.5},{"SampleID":122,"Zip Code":48506,"Ward":4,"PbBottle1_ppb":0.349,"PbBottle2_ppb":0.13,"PbBottle3_ppb":0.131},{"SampleID":123,"Zip Code":48506,"Ward":4,"PbBottle1_ppb":4.764,"PbBottle2_ppb":1.388,"PbBottle3_ppb":1.06},{"SampleID":124,"Zip Code":48506,"Ward":4,"PbBottle1_ppb":0.832,"PbBottle2_ppb":0.284,"PbBottle3_ppb":0.214},{"SampleID":125,"Zip Code":48506,"Ward":4,"PbBottle1_ppb":1.224,"PbBottle2_ppb":0.568,"PbBottle3_ppb":0.465},{"SampleID":126,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":15.9,"PbBottle2_ppb":3.7,"PbBottle3_ppb":2.2},{"SampleID":127,"Zip Code":48506,"Ward":4,"PbBottle1_ppb":5.667,"PbBottle2_ppb":1.405,"PbBottle3_ppb":0.896},{"SampleID":128,"Zip Code":48506,"Ward":4,"PbBottle1_ppb":3.564,"PbBottle2_ppb":2.767,"PbBottle3_ppb":2.127},{"SampleID":129,"Zip Code":48506,"Ward":4,"PbBottle1_ppb":0.475,"PbBottle2_ppb":0.2,"PbBottle3_ppb":0.268},{"SampleID":130,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":5.3,"PbBottle2_ppb":0.5,"PbBottle3_ppb":0.2},{"SampleID":131,"Zip Code":48506,"Ward":4,"PbBottle1_ppb":1.166,"PbBottle2_ppb":0.736,"PbBottle3_ppb":0.269},{"SampleID":132,"Zip Code":48506,"Ward":4,"PbBottle1_ppb":0.684,"PbBottle2_ppb":0.306,"PbBottle3_ppb":0.094},{"SampleID":133,"Zip Code":48503,"Ward":8,"PbBottle1_ppb":6.347,"PbBottle2_ppb":1.724,"PbBottle3_ppb":0.678},{"SampleID":134,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":10.56,"PbBottle2_ppb":5.672,"PbBottle3_ppb":4.813},{"SampleID":135,"Zip Code":48502,"Ward":5,"PbBottle1_ppb":2.273,"PbBottle2_ppb":2.808,"PbBottle3_ppb":3.048},{"SampleID":136,"Zip Code":48505,"Ward":1,"PbBottle1_ppb":1.571,"PbBottle2_ppb":1.265,"PbBottle3_ppb":0.316},{"SampleID":137,"Zip Code":48503,"Ward":8,"PbBottle1_ppb":5.402,"PbBottle2_ppb":4.196,"PbBottle3_ppb":1.945},{"SampleID":138,"Zip Code":48504,"Ward":6,"PbBottle1_ppb":43.19,"PbBottle2_ppb":7.688,"PbBottle3_ppb":4.39},{"SampleID":139,"Zip Code":48503,"Ward":8,"PbBottle1_ppb":1.492,"PbBottle2_ppb":1.409,"PbBottle3_ppb":0.378},{"SampleID":140,"Zip Code":48503,"Ward":5,"PbBottle1_ppb":66.24,"PbBottle2_ppb":17.75,"PbBottle3_ppb":8.815},{"SampleID":141,"Zip Code":48505,"Ward":1,"PbBottle1_ppb":1.799,"PbBottle2_ppb":0.032,"PbBottle3_ppb":0.031},{"SampleID":142,"Zip Code":48503,"Ward":8,"PbBottle1_ppb":1.861,"PbBottle2_ppb":1.355,"PbBottle3_ppb":0.64},{"SampleID":143,"Zip Code":48503,"Ward":8,"PbBottle1_ppb":2.672,"PbBottle2_ppb":2.001,"PbBottle3_ppb":1.094},{"SampleID":144,"Zip Code":48505,"Ward":1,"PbBottle1_ppb":3.741,"PbBottle2_ppb":1.211,"PbBottle3_ppb":0.258},{"SampleID":145,"Zip Code":48506,"Ward":4,"PbBottle1_ppb":1.934,"PbBottle2_ppb":0.374,"PbBottle3_ppb":0.424},{"SampleID":146,"Zip Code":48506,"Ward":4,"PbBottle1_ppb":27.05,"PbBottle2_ppb":0.902,"PbBottle3_ppb":0.61},{"SampleID":147,"Zip Code":48506,"Ward":4,"PbBottle1_ppb":1.174,"PbBottle2_ppb":0.291,"PbBottle3_ppb":4.055},{"SampleID":148,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":2.325,"PbBottle2_ppb":1.099,"PbBottle3_ppb":0.466},{"SampleID":149,"Zip Code":48506,"Ward":4,"PbBottle1_ppb":1.966,"PbBottle2_ppb":0.253,"PbBottle3_ppb":0.201},{"SampleID":150,"Zip Code":48506,"Ward":4,"PbBottle1_ppb":1.959,"PbBottle2_ppb":0.438,"PbBottle3_ppb":0.448},{"SampleID":151,"Zip Code":48506,"Ward":4,"PbBottle1_ppb":0.823,"PbBottle2_ppb":1.881,"PbBottle3_ppb":0.412},{"SampleID":152,"Zip Code":48506,"Ward":4,"PbBottle1_ppb":11.2,"PbBottle2_ppb":7.553,"PbBottle3_ppb":12.21},{"SampleID":153,"Zip Code":48504,"Ward":2,"PbBottle1_ppb":5.668,"PbBottle2_ppb":3.341,"PbBottle3_ppb":3.268},{"SampleID":154,"Zip Code":48506,"Ward":4,"PbBottle1_ppb":6.261,"PbBottle2_ppb":1.316,"PbBottle3_ppb":0.5},{"SampleID":155,"Zip Code":48506,"Ward":4,"PbBottle1_ppb":4.797,"PbBottle2_ppb":1.594,"PbBottle3_ppb":1.264},{"SampleID":156,"Zip Code":48506,"Ward":4,"PbBottle1_ppb":0.64,"PbBottle2_ppb":0.905,"PbBottle3_ppb":0.151},{"SampleID":158,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":8.713,"PbBottle2_ppb":2.799,"PbBottle3_ppb":50.97},{"SampleID":159,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":2.544,"PbBottle2_ppb":1.099,"PbBottle3_ppb":0.498},{"SampleID":161,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":0.41,"PbBottle2_ppb":0.096,"PbBottle3_ppb":0.116},{"SampleID":162,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":32.85,"PbBottle2_ppb":35.76,"PbBottle3_ppb":9.103},{"SampleID":163,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":12.87,"PbBottle2_ppb":14.87,"PbBottle3_ppb":6.326},{"SampleID":164,"Zip Code":48503,"Ward":8,"PbBottle1_ppb":38.02,"PbBottle2_ppb":38.7,"PbBottle3_ppb":38.94},{"SampleID":165,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":2.435,"PbBottle2_ppb":8.183,"PbBottle3_ppb":1.296},{"SampleID":166,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":2.997,"PbBottle2_ppb":1.867,"PbBottle3_ppb":1.512},{"SampleID":167,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":11,"PbBottle2_ppb":10.53,"PbBottle3_ppb":8.688},{"SampleID":168,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":6.219,"PbBottle2_ppb":12.33,"PbBottle3_ppb":4.202},{"SampleID":169,"Zip Code":48503,"Ward":8,"PbBottle1_ppb":8.8,"PbBottle2_ppb":3.1,"PbBottle3_ppb":4.5},{"SampleID":170,"Zip Code":48504,"Ward":6,"PbBottle1_ppb":8.071,"PbBottle2_ppb":0.947,"PbBottle3_ppb":0.839},{"SampleID":171,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":3.262,"PbBottle2_ppb":0.453,"PbBottle3_ppb":0.252},{"SampleID":172,"Zip Code":48503,"Ward":8,"PbBottle1_ppb":2.267,"PbBottle2_ppb":0.541,"PbBottle3_ppb":0.391},{"SampleID":173,"Zip Code":48505,"Ward":3,"PbBottle1_ppb":0.922,"PbBottle2_ppb":0.878,"PbBottle3_ppb":0.491},{"SampleID":174,"Zip Code":48504,"Ward":6,"PbBottle1_ppb":27.02,"PbBottle2_ppb":31.25,"PbBottle3_ppb":11.37},{"SampleID":176,"Zip Code":48503,"Ward":8,"PbBottle1_ppb":0.906,"PbBottle2_ppb":0.961,"PbBottle3_ppb":1.052},{"SampleID":177,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":2.85,"PbBottle2_ppb":6.862,"PbBottle3_ppb":0.951},{"SampleID":178,"Zip Code":48504,"Ward":2,"PbBottle1_ppb":1.852,"PbBottle2_ppb":0.472,"PbBottle3_ppb":0.422},{"SampleID":179,"Zip Code":48506,"Ward":4,"PbBottle1_ppb":5.35,"PbBottle2_ppb":1.328,"PbBottle3_ppb":0.595},{"SampleID":180,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":25.21,"PbBottle2_ppb":4.337,"PbBottle3_ppb":1.019},{"SampleID":182,"Zip Code":48504,"Ward":6,"PbBottle1_ppb":15.55,"PbBottle2_ppb":3.962,"PbBottle3_ppb":1.861},{"SampleID":183,"Zip Code":48506,"Ward":4,"PbBottle1_ppb":0.793,"PbBottle2_ppb":0.533,"PbBottle3_ppb":0.391},{"SampleID":184,"Zip Code":48506,"Ward":4,"PbBottle1_ppb":5.068,"PbBottle2_ppb":0.683,"PbBottle3_ppb":0.489},{"SampleID":185,"Zip Code":48507,"Ward":8,"PbBottle1_ppb":26.64,"PbBottle2_ppb":8.878,"PbBottle3_ppb":6.619},{"SampleID":186,"Zip Code":48506,"Ward":4,"PbBottle1_ppb":1.867,"PbBottle2_ppb":0.165,"PbBottle3_ppb":0.175},{"SampleID":189,"Zip Code":48506,"Ward":4,"PbBottle1_ppb":19.16,"PbBottle2_ppb":12.54,"PbBottle3_ppb":7.719},{"SampleID":191,"Zip Code":48503,"Ward":5,"PbBottle1_ppb":28.7,"PbBottle2_ppb":12.7,"PbBottle3_ppb":8.6},{"SampleID":192,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":20.22,"PbBottle2_ppb":8.908,"PbBottle3_ppb":6.677},{"SampleID":193,"Zip Code":48507,"Ward":8,"PbBottle1_ppb":2.9,"PbBottle2_ppb":0.6,"PbBottle3_ppb":0.7},{"SampleID":194,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":18.86,"PbBottle2_ppb":5.051,"PbBottle3_ppb":2.548},{"SampleID":195,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":2.816,"PbBottle2_ppb":0.324,"PbBottle3_ppb":0.362},{"SampleID":196,"Zip Code":48506,"Ward":3,"PbBottle1_ppb":118.4,"PbBottle2_ppb":40.78,"PbBottle3_ppb":39.99},{"SampleID":197,"Zip Code":48506,"Ward":3,"PbBottle1_ppb":27.45,"PbBottle2_ppb":0.939,"PbBottle3_ppb":0.533},{"SampleID":198,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":1.2,"PbBottle2_ppb":0.1,"PbBottle3_ppb":0.1},{"SampleID":200,"Zip Code":48506,"Ward":4,"PbBottle1_ppb":4.681,"PbBottle2_ppb":0.755,"PbBottle3_ppb":0.456},{"SampleID":201,"Zip Code":48506,"Ward":3,"PbBottle1_ppb":11.57,"PbBottle2_ppb":6.08,"PbBottle3_ppb":1.782},{"SampleID":202,"Zip Code":48532,"Ward":8,"PbBottle1_ppb":6.557,"PbBottle2_ppb":0.289,"PbBottle3_ppb":0.371},{"SampleID":203,"Zip Code":48505,"Ward":3,"PbBottle1_ppb":3.4,"PbBottle2_ppb":9.6,"PbBottle3_ppb":1.7},{"SampleID":204,"Zip Code":48504,"Ward":6,"PbBottle1_ppb":0.7,"PbBottle2_ppb":0.2,"PbBottle3_ppb":0.2},{"SampleID":205,"Zip Code":48507,"Ward":8,"PbBottle1_ppb":158,"PbBottle2_ppb":90.83,"PbBottle3_ppb":91.69},{"SampleID":206,"Zip Code":48506,"Ward":4,"PbBottle1_ppb":0.977,"PbBottle2_ppb":0.47,"PbBottle3_ppb":0.381},{"SampleID":207,"Zip Code":48503,"Ward":8,"PbBottle1_ppb":8.471,"PbBottle2_ppb":4.692,"PbBottle3_ppb":1.48},{"SampleID":208,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":11.47,"PbBottle2_ppb":23.15,"PbBottle3_ppb":7.129},{"SampleID":209,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":5.228,"PbBottle2_ppb":2.477,"PbBottle3_ppb":1.014},{"SampleID":210,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":0.956,"PbBottle2_ppb":0.196,"PbBottle3_ppb":0.157},{"SampleID":211,"Zip Code":48504,"Ward":6,"PbBottle1_ppb":1.671,"PbBottle2_ppb":0.405,"PbBottle3_ppb":4.721},{"SampleID":212,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":1.152,"PbBottle2_ppb":0.708,"PbBottle3_ppb":0.282},{"SampleID":213,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":0.5,"PbBottle2_ppb":0.1,"PbBottle3_ppb":0.1},{"SampleID":214,"Zip Code":48503,"Ward":5,"PbBottle1_ppb":10.74,"PbBottle2_ppb":2.331,"PbBottle3_ppb":1.628},{"SampleID":215,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":3.9,"PbBottle2_ppb":0.4,"PbBottle3_ppb":0.2},{"SampleID":216,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":2.149,"PbBottle2_ppb":0.368,"PbBottle3_ppb":0.333},{"SampleID":217,"Zip Code":48506,"Ward":4,"PbBottle1_ppb":1.1,"PbBottle2_ppb":0.4,"PbBottle3_ppb":0.2},{"SampleID":218,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":7.087,"PbBottle2_ppb":9.467,"PbBottle3_ppb":1.28},{"SampleID":219,"Zip Code":48505,"Ward":1,"PbBottle1_ppb":1.329,"PbBottle2_ppb":0.609,"PbBottle3_ppb":0.527},{"SampleID":220,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":6.2,"PbBottle2_ppb":0.7,"PbBottle3_ppb":0.6},{"SampleID":221,"Zip Code":48505,"Ward":3,"PbBottle1_ppb":0.8,"PbBottle2_ppb":0.26,"PbBottle3_ppb":0.255},{"SampleID":222,"Zip Code":48503,"Ward":8,"PbBottle1_ppb":9.3,"PbBottle2_ppb":9.7,"PbBottle3_ppb":5},{"SampleID":223,"Zip Code":48504,"Ward":2,"PbBottle1_ppb":2.1,"PbBottle2_ppb":1.2,"PbBottle3_ppb":0.5},{"SampleID":224,"Zip Code":48505,"Ward":1,"PbBottle1_ppb":4.563,"PbBottle2_ppb":3.106,"PbBottle3_ppb":2.997},{"SampleID":225,"Zip Code":48504,"Ward":2,"PbBottle1_ppb":4.808,"PbBottle2_ppb":6.196,"PbBottle3_ppb":1.523},{"SampleID":226,"Zip Code":48504,"Ward":2,"PbBottle1_ppb":0.753,"PbBottle2_ppb":2.526,"PbBottle3_ppb":0.549},{"SampleID":227,"Zip Code":48505,"Ward":1,"PbBottle1_ppb":1.862,"PbBottle2_ppb":1.213,"PbBottle3_ppb":0.898},{"SampleID":228,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":1.183,"PbBottle2_ppb":0.366,"PbBottle3_ppb":0.201},{"SampleID":229,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":8.2,"PbBottle2_ppb":3.2,"PbBottle3_ppb":2.6},{"SampleID":230,"Zip Code":48504,"Ward":6,"PbBottle1_ppb":3.679,"PbBottle2_ppb":0.498,"PbBottle3_ppb":0.288},{"SampleID":231,"Zip Code":48505,"Ward":1,"PbBottle1_ppb":2.37,"PbBottle2_ppb":7.333,"PbBottle3_ppb":3.797},{"SampleID":234,"Zip Code":48504,"Ward":2,"PbBottle1_ppb":0.828,"PbBottle2_ppb":1.318,"PbBottle3_ppb":0.233},{"SampleID":235,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":0.719,"PbBottle2_ppb":0.254,"PbBottle3_ppb":0.058},{"SampleID":236,"Zip Code":48504,"Ward":1,"PbBottle1_ppb":2.822,"PbBottle2_ppb":1.221,"PbBottle3_ppb":0.258},{"SampleID":237,"Zip Code":48504,"Ward":8,"PbBottle1_ppb":2.867,"PbBottle2_ppb":0.723,"PbBottle3_ppb":0.744},{"SampleID":238,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":2.332,"PbBottle2_ppb":3.588,"PbBottle3_ppb":1.221},{"SampleID":240,"Zip Code":48503,"Ward":8,"PbBottle1_ppb":4.401,"PbBottle2_ppb":2.111,"PbBottle3_ppb":1.572},{"SampleID":241,"Zip Code":48504,"Ward":6,"PbBottle1_ppb":2.708,"PbBottle2_ppb":2.238,"PbBottle3_ppb":0.809},{"SampleID":242,"Zip Code":48504,"Ward":6,"PbBottle1_ppb":34.13,"PbBottle2_ppb":6.002,"PbBottle3_ppb":1.71},{"SampleID":243,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":5.218,"PbBottle2_ppb":2.614,"PbBottle3_ppb":0.831},{"SampleID":244,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":15.73,"PbBottle2_ppb":13.95,"PbBottle3_ppb":3.584},{"SampleID":245,"Zip Code":48504,"Ward":6,"PbBottle1_ppb":3.045,"PbBottle2_ppb":2.744,"PbBottle3_ppb":0.299},{"SampleID":246,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":1.1,"PbBottle2_ppb":0.5,"PbBottle3_ppb":0.3},{"SampleID":247,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":1.386,"PbBottle2_ppb":0.288,"PbBottle3_ppb":0.432},{"SampleID":248,"Zip Code":48504,"Ward":6,"PbBottle1_ppb":0.915,"PbBottle2_ppb":0.354,"PbBottle3_ppb":0.306},{"SampleID":249,"Zip Code":48504,"Ward":6,"PbBottle1_ppb":2.145,"PbBottle2_ppb":0.345,"PbBottle3_ppb":3.738},{"SampleID":250,"Zip Code":48507,"Ward":8,"PbBottle1_ppb":4.056,"PbBottle2_ppb":0.547,"PbBottle3_ppb":0.378},{"SampleID":251,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":1.668,"PbBottle2_ppb":1.508,"PbBottle3_ppb":2.72},{"SampleID":252,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":7.575,"PbBottle2_ppb":1.362,"PbBottle3_ppb":1.094},{"SampleID":253,"Zip Code":48507,"Ward":8,"PbBottle1_ppb":5.59,"PbBottle2_ppb":4.306,"PbBottle3_ppb":2.019},{"SampleID":254,"Zip Code":48503,"Ward":5,"PbBottle1_ppb":0.708,"PbBottle2_ppb":0.326,"PbBottle3_ppb":0.303},{"SampleID":255,"Zip Code":48504,"Ward":6,"PbBottle1_ppb":1.701,"PbBottle2_ppb":4.397,"PbBottle3_ppb":1.287},{"SampleID":256,"Zip Code":48504,"Ward":6,"PbBottle1_ppb":1.467,"PbBottle2_ppb":0.149,"PbBottle3_ppb":0.137},{"SampleID":258,"Zip Code":48504,"Ward":2,"PbBottle1_ppb":2.582,"PbBottle2_ppb":259.8,"PbBottle3_ppb":61.96},{"SampleID":259,"Zip Code":48505,"Ward":2,"PbBottle1_ppb":22.08,"PbBottle2_ppb":15.86,"PbBottle3_ppb":9.262},{"SampleID":260,"Zip Code":48507,"Ward":8,"PbBottle1_ppb":16.51,"PbBottle2_ppb":2.024,"PbBottle3_ppb":7.068},{"SampleID":262,"Zip Code":48507,"Ward":8,"PbBottle1_ppb":56.26,"PbBottle2_ppb":4.692,"PbBottle3_ppb":1.243},{"SampleID":263,"Zip Code":48504,"Ward":6,"PbBottle1_ppb":2.433,"PbBottle2_ppb":1.334,"PbBottle3_ppb":1.376},{"SampleID":264,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":0.5,"PbBottle2_ppb":0.2,"PbBottle3_ppb":0.5},{"SampleID":265,"Zip Code":48504,"Ward":6,"PbBottle1_ppb":29.13,"PbBottle2_ppb":11.57,"PbBottle3_ppb":6.388},{"SampleID":266,"Zip Code":48505,"Ward":1,"PbBottle1_ppb":12.3,"PbBottle2_ppb":0.5,"PbBottle3_ppb":0.4},{"SampleID":267,"Zip Code":48504,"Ward":6,"PbBottle1_ppb":3.445,"PbBottle2_ppb":0.29,"PbBottle3_ppb":0.167},{"SampleID":268,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":16.49,"PbBottle2_ppb":12.83,"PbBottle3_ppb":9.018},{"SampleID":269,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":3.365,"PbBottle2_ppb":2.45,"PbBottle3_ppb":1.675},{"SampleID":270,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":1.154,"PbBottle2_ppb":0.176,"PbBottle3_ppb":0.12},{"SampleID":271,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":13.53,"PbBottle2_ppb":21.91,"PbBottle3_ppb":4.675},{"SampleID":272,"Zip Code":48504,"Ward":6,"PbBottle1_ppb":2.229,"PbBottle2_ppb":1.573,"PbBottle3_ppb":0.84},{"SampleID":273,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":28.91,"PbBottle2_ppb":5.471,"PbBottle3_ppb":3.056},{"SampleID":274,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":6.601,"PbBottle2_ppb":1.929,"PbBottle3_ppb":0.417},{"SampleID":275,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":0.948,"PbBottle2_ppb":0.27,"PbBottle3_ppb":0.207},{"SampleID":276,"Zip Code":48505,"Ward":3,"PbBottle1_ppb":3.484,"PbBottle2_ppb":0.434,"PbBottle3_ppb":0.306},{"SampleID":278,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":1.888,"PbBottle2_ppb":0.359,"PbBottle3_ppb":0.322},{"SampleID":279,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":13.95,"PbBottle2_ppb":12.2,"PbBottle3_ppb":8.251},{"SampleID":280,"Zip Code":48504,"Ward":6,"PbBottle1_ppb":6.27,"PbBottle2_ppb":4.036,"PbBottle3_ppb":1.182},{"SampleID":281,"Zip Code":48506,"Ward":7,"PbBottle1_ppb":19.12,"PbBottle2_ppb":22.02,"PbBottle3_ppb":7.968},{"SampleID":282,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":1.633,"PbBottle2_ppb":0.465,"PbBottle3_ppb":0.238},{"SampleID":283,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":1.114,"PbBottle2_ppb":0.605,"PbBottle3_ppb":0.255},{"SampleID":284,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":3.9,"PbBottle2_ppb":0.558,"PbBottle3_ppb":0.504},{"SampleID":285,"Zip Code":48504,"Ward":1,"PbBottle1_ppb":3.521,"PbBottle2_ppb":0.45,"PbBottle3_ppb":0.321},{"SampleID":286,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":3.832,"PbBottle2_ppb":0.794,"PbBottle3_ppb":0.339},{"SampleID":287,"Zip Code":48505,"Ward":3,"PbBottle1_ppb":3.243,"PbBottle2_ppb":0.738,"PbBottle3_ppb":0.27},{"SampleID":289,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":0.99,"PbBottle2_ppb":0.25,"PbBottle3_ppb":0.263},{"SampleID":290,"Zip Code":48507,"Ward":9,"PbBottle1_ppb":1.203,"PbBottle2_ppb":19.26,"PbBottle3_ppb":1.626},{"SampleID":291,"Zip Code":48506,"Ward":3,"PbBottle1_ppb":2.261,"PbBottle2_ppb":0.102,"PbBottle3_ppb":0.407},{"SampleID":292,"Zip Code":48503,"Ward":4,"PbBottle1_ppb":16.99,"PbBottle2_ppb":6.32,"PbBottle3_ppb":3.585},{"SampleID":293,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":3.322,"PbBottle2_ppb":2.559,"PbBottle3_ppb":1.512},{"SampleID":294,"Zip Code":48506,"Ward":4,"PbBottle1_ppb":14.33,"PbBottle2_ppb":1.284,"PbBottle3_ppb":0.323},{"SampleID":295,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":18.11,"PbBottle2_ppb":20.21,"PbBottle3_ppb":4.263},{"SampleID":296,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":12.81,"PbBottle2_ppb":7.874,"PbBottle3_ppb":1.78},{"SampleID":298,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":1.083,"PbBottle2_ppb":0.322,"PbBottle3_ppb":0.26},{"SampleID":299,"Zip Code":48503,"Ward":7,"PbBottle1_ppb":29.59,"PbBottle2_ppb":3.258,"PbBottle3_ppb":1.843},{"SampleID":300,"Zip Code":48505,"Ward":1,"PbBottle1_ppb":4.287,"PbBottle2_ppb":4.345,"PbBottle3_ppb":4.905}]""")
flint_data = pd.read_csv('flint_water_data.csv')


# #### Key for data fields in this data set:
# 
# - *SampleID*: Unique study code for each sample
# - *Zip Code*: location where samples were collected
# - *Ward*: location where samples were collected
# - *PbBottle1_ppb*: Concentration of lead in parts per billion (ppb) in sample acquired at initial turn on of water
# - *PbBottle2_ppb*: Concentration of lead in parts per billion (ppb) in sample acquired after 45 seconds of flushing water
# - *PbBottle3_ppb*: Concentration of lead in parts per billion (ppb) in sample acquired after 120 seconds of flushing water
# 
# 
# #### EPA Limits
# 
# 
# The U.S. Environmental Protection Agency (EPA) guidelines about lead contaminants state:
# 
# > Lead and copper are regulated by a treatment technique that requires systems to control the corrosiveness of their water. **If more than 10% of tap water samples exceed the action level,** water systems must take additional steps. For copper, the action level is 1.3 mg/L (1300 ppb), and **for lead is 0.015 mg/L (15 ppb).** 
# >
# > Source: (http://www.epa.gov/your-drinking-water/table-regulated-drinking-water-contaminants#seven). 
# 
# 
# 

# ## 1. Analysis Using Descriptive Statistics
# ### 1.1
# Use `describe()` function to determine the mean, standard deviation, min, median, and max of the first set of samples (`PbBottle1_ppb`). 

# In[ ]:


#Write your code here


# ### 1.2
# From this, can you determine if the water supply in Flint met the EPA standard?

# *Write your answer here*

# ### 1.3
# What is the median of this sample? How does it compare to the mean? Do you expect this sample to be close to a normal (Gaussian) distribution?

# *Write your answer here*

# ## 2. Analysis Using Visualizations
# ### 2.1
# Make a histogram visualization of the distribution of the first set of samples (`PbBottle1_ppb`). Use the `axvline()` function to add a line showing where the EPA limit is. (You will probably need to google what this function does.) Also, make sure that your plot has x and y-axes labels and a title.

# In[ ]:


#Write your code here


# ### 2.2
# Does the distribution of samples look like a normal (Gausian) distribution? Is that what you predicted based on your analysis of the descriptive statistics (Part 1.3)?

# *Write your answer here*

# ### 2.3
# Looking at this, there’s a big pile up of samples that are near or below the EPA limit, and it makes it hard to get a sense of what the full distribution looks like. Use the `yscale()` to make the y-scale logarithmic. 

# In[ ]:


#Write your code here


# ### 2.4
# As discussed in the pre-class, logarithmic scales allow us to get a better handle on distributions with a *large dynamic range*. Use your log plot to count the number of samples that lie above the EPA limit. 
# 
# What fraction of the total samples appear to fall above the EPA limit?

# *Write your answer here*

# ### 2.5
# Based on this analysis, does it appear that the Flint samples met the EPA standards?

# *Write your answer here*

# ## STOP
# Based on your analysis so far, answer the following question: ***Would you feel comfortable drinking a glass of water in Flint at the height of the water crises?***

# *Write your answer here*

# ## 3. Analysis Using Masks
# 
# In the previous part, you used descriptive statistics and a visualization to try to estimate the number of samples that fell above the EPA limit. Now we’re going to actually count the number that actually don’t meet the EPA regulation. 
# 
# ### 3.1
# 
# Create a mask and a new dataframe that only contain samples where `PbBottle1_pb` was greater than the EPA limit.

# In[ ]:


#Write your code here


# ### 3.2
# Answer the following questions: 
# 1. How many samples were above the EPA limit? 
# 2. What fraction of the total samples does this comprise? 

# *Write your answer here*

# ### 3.3
# Based on this analysis, do these samples meet the EPA standards?

# *Write your answer here*

# ## 4. Extending Analysis to the Other Samples
# 
# Repeat the analysis you did parts 1, 2, and 3 for both the `PbBottle2_ppb` and  `PbBottle3_ppb` samples. Recall that these are samples drawn 45 seconds after the taps are turned on (`PbBottle2_ppb`) and two minutes after the taps are turned on (`PbBottle3_ppb`). 
# To complete this section, you should:
# 1. Fill in the table below with descriptive statistics and fraction of samples above the EPA limit.
# 2. Have a three panel plot showing the distribution of samples. The y-axes for each of them should be logarithmic and each plot should have x and y-axes labels and a title.
# 
# 
# | Sample | Mean | Std. Dev | Min | Median | Max | Fraction > EPA |
# | :----- | :----- | :------ | :----- | :----- | :----- | :----- |
# | PbBottle1_ppb | ??| ?? | ??  | ?? | ?? | ?? |
# | PbBottle2_ppb | ??| ?? | ??  | ?? | ?? | ?? |
# | PbBottle3_ppb | ??| ?? | ??  | ?? | ?? | ?? |

# In[ ]:


#Write your code here


# ## 5. Conclusions
# 
# Based on your new analysis, answer the following question: ***Would you feel comfortable drinking a glass of water in Flint at the height of the water crises?*** 
# 
# **Use statistical values and/or data visualizations to back up your choice.**

# *Write your answer here*

# ## 6. (Time Permitting) Looking for Other Sources of Analysis
# 
# For your project, it will be good to draw upon other resources to compare your results/conclusions to. 
# 
# Go through the [following article from the New York Times](https://www.nytimes.com/2018/07/22/opinion/flint-lead-poisoning-water.html) and compare it's conclusions to your own from Part 5. Given the information in this article, ***Would you feel comfortable drinking a glass of water in Flint at the height of the water crises?*** 
# 
# 
# **NOTE:** If you are an MSU student, you have access to a free New York Times account. [Click this link](https://asmsu.msu.edu/home/services/717-2/) and follow the steps to get access through MSU. 

# *Write your answer here*

# ---
# ## Assignment wrapup
# 
# Please fill out the form that appears when you run the code below. **You must completely fill this out in order to receive credit for the assignment!** 

# In[ ]:


from IPython.display import HTML
HTML(
"""
<iframe 
	src="https://cmse.msu.edu/cmse201-ic-survey" 
	width="800px" 
	height="600px" 
	frameborder="0" 
	marginheight="0" 
	marginwidth="0">
	Loading...
</iframe>
"""
)


# ---
# 
# ## Congratulations, you're done!
# 
# Submit this assignment by uploading your notebook to the course Desire2Learn web page.  Go to the "In-Class Assignments" folder, find the appropriate submission link, and upload everything there. Make sure your name is on it!

# &#169; Copyright 2021,  Michigan State University Board of Trustees
