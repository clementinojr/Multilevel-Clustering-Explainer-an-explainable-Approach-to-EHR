# Multilevel Clustering Explainer: An ExplainableApproach to Electronic Health Records


**Attention**: MCE **not** a commercial method. It is designed for educational and demonstration purposes **only**.

### 1. Brief introduction ###
The repository is organized as follows:
  * [Experiments Results:](https://github.com/clementinojr/Multilevel-Clustering-Explainer-an-explainable-Approach-to-EHR/tree/main/Experiments-Result) contains the base files used to implement and obtain the results. The files contain the figures of the results obtained for both local and global level.
  * [Recovery:](https://github.com/clementinojr/Multilevel-Clustering-Explainer-an-explainable-Approach-to-EHR/tree/main/Recovery) contain the code and notebook used in the pre-processing of the visualization to retrieve the information described in phase 3 of the proposed method.
   * [plot_functions:](https://github.com/clementinojr/Multilevel-Clustering-Explainer-an-explainable-Approach-to-EHR/tree/main/plot_functions) contains the functions used to generate the visual graphics.
  * [complete_script_.py:](https://github.com/clementinojr/Multilevel-Clustering-Explainer-an-explainable-Approach-to-EHR/blob/main/complete_script_%20.py) contains the script used to generate all the results both globally and locally.

### 2. Minimum requirements ###

* Python 3.
* PostgreSQL.

### 3. Required Library ###
  * json
  * re
  * pandas 
  * numpy 
  * sklearn.metrics *
  * time import gmtime, strftime
  * datetime import datetime
  * lime
  * others


### 4. Multilevel Clustering Explainer (MCE)  workflow. Adequacy of data in(Phase~1), construction of explanatory information (with different levels of detail, Local or Global) in(Phase 2), and presentation of information in(Phase 3 ###

 ![Main](./fig-general-method.png)




```
### Acknowledgement ###
The authors would like to thank Brazilian Coordination of Superior Level Staff Improvement (CAPES), grant PROEX-11357281/M;  the Sao Paulo Research Foundation (FAPESP), grants  2016/17078-0, 2018/06228-7, 2019/04660-1, 2018/06074-0; and the National Council for Scientific and Technological Development (CNPq).



### References ####

[1] .  Xie,  X.  A.  Chen,  and  G. Gao,  “Outlining  the  designspace   of   explainable   intelligent   systems   for   medicaldiagnosis,”  inJoint  Proceedings  of  the  ACM  IUI  2019,Los Angeles, USA, March 20, 2019. [Online]. Available:http://ceur-ws.org/Vol-2327/IUI19WS-ExSS2019-18.pdf[2].

[2] R.    Barredo    Arrietaet    al.,    “Explainable    artificialintelligence  (xai):  Concepts,  taxonomies,  opportunitiesand   challenges   toward   responsible   ai,”InformationFusion,  vol.  58,  pp.  82–115,  2020.  [Online].  Available:https://doi.org/10.1016/j.inffus.2019.12.012.

[3] R.  Guidottiet  al.,  “A  survey  of  methods  for  explainingblack   box   models,”ACM   Comput.   Surv.,   vol.   51,no.  5,  pp.  93:1–93:42,  Aug.  2018.  [Online].  Available:http://doi.acm.org/10.1145/3236009.

[4] M.  Ribera  and`A.  Lapedriza,  “Can  we  do  better  expla-nations?  a  proposal  of  user-centered  explainable  ai.”  inIUI Workshops, 2019.

[5] M. T. Ribeiro, S. Singh, and C. Guestrin, “”why should Itrust you?”: Explaining the predictions of any classifier,”inProceedings of the 22nd ACM SIGKDD InternationalConference  on  Knowledge  Discovery  and  Data  Mining,San Francisco, CA, USA, August 13-17, 2016, 2016, pp.1135–1144.

[6] S.  M.  Lundberg  and  S.-I.  Lee,  “A  unified  approach  tointerpreting  model  predictions,”  inProceedings  of  the31st  International  Conference  on  Neural  InformationProcessing Systems, ser. NIPS’17.   Red Hook, NY, USA:Curran Associates Inc., 2017, p. 4768–4777.

[7] F.  Cavaliereet  al.,  “Parkinson’s  disease  diagnosis:  To-wards grammar-based explainable artificial intelligence,”in2020 IEEE Symposium on Computers and Communi-cations (ISCC), 2020, pp. 1–6.

[8] D.  Haimovichet  al.,  “Development  and  validationof  the  quick  covid-19  severity  index:  a  prognostic  toolfor early clinical decompensation,”Annals of emergencymedicine, vol. 76, no. 4, pp. 442–453, 2020.


[9] A.  Morichetta,  P.  Casas,  and  M.  Mellia,  “Explain-it:Towards  explainable  ai  for  unsupervised  network  trafficanalysis,”   inProceedings   of   the   3rd   ACM   CoNEXTWorkshop on Big DAta, Machine Learning and ArtificialIntelligence   for   Data   Communication   Networks,   ser.Big-DAMA  ’19.New  York,  NY,  USA:  Associationfor  Computing  Machinery,  2019,  p.  22–28.  [Online].Available: https://doi.org/10.1145/3359992.3366639.

[10] J.  M.  Clementinoet  al.,  “Bag-of-attributes  representa-tion: A vector space model for electronic health recordsanalysis in omop,” in2020 IEEE 33rd International Sym-posium  on  Computer-Based  Medical  Systems  (CBMS),2020, pp. 197–202.




### Contact ###

This work is part of my program master's degree. You can contact me writing to [juniorclementino@usp.br](https://clementinojr.github.io/).
