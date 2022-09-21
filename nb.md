# [Why Do Naive Bayes Classifiers Perform So Well?](https://highdemandskills.com/naive-bayes-perform/#ref2)

* Even the feature are dependent.
  * relativities score(prob)
  * positive correlated --> over confident --> relativities score(prob)
  * negtive correlated --> less contributiion for `P(C|F)`

* assume independence
  * easier to implement / parallelize --> can compute large of data amounts

* when to use
  * high cardinality (url, user, ...)
  * eager learning (realtime learning) by maintain freq tables.


releted paper

[1] C. D. Manning, P. Raghavan, H. Schutze, An introduction to information retrieval, Cambridge University Press, April 2009.

[2] H. Zhang, The optimality of naive Bayes, American Association for Artificial Intelligence, 2004.

[3] S. S. Y. Ng, Y. Xing and K. L. Tsui, A naive Bayes model for robust remaining useful life prediction of lithium-ion battery, Applied Energy, 118, p. 115, 2014.

Post navigation
