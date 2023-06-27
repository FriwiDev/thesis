# Controller REST API

This document contains the required REST API functionality from controllers.
It uses a subset of the REST API provided by Ryu.
The resulting subset will be modelled using openapi to make us able to
provide code for other controllers in the future.

[Online API specification from Ryu](https://ryu.readthedocs.io/en/latest/app/ofctl_rest.html) | [GitHub source code](https://github.com/faucetsdn/ryu/blob/master/ryu/app/ofctl_rest.py)

### Required information retrieval requests

- [Get all switches](https://ryu.readthedocs.io/en/latest/app/ofctl_rest.html#get-all-switches)
- [Get switch description](https://ryu.readthedocs.io/en/latest/app/ofctl_rest.html#get-the-desc-stats)

- [Get all flows](https://ryu.readthedocs.io/en/latest/app/ofctl_rest.html#get-all-flows-stats)
- [Get all flows filtered](https://ryu.readthedocs.io/en/latest/app/ofctl_rest.html#get-flows-stats-filtered-by-fields)

- [Get all tables and their features](https://ryu.readthedocs.io/en/latest/app/ofctl_rest.html#get-table-features)

- [Get port descriptions](https://ryu.readthedocs.io/en/latest/app/ofctl_rest.html#get-ports-description)

- [Get queue stats](https://ryu.readthedocs.io/en/latest/app/ofctl_rest.html#get-queues-stats)

### Required modification requests

- [Add a flow entry](https://ryu.readthedocs.io/en/latest/app/ofctl_rest.html#add-a-flow-entry)
- [Delete all matching flows](https://ryu.readthedocs.io/en/latest/app/ofctl_rest.html#delete-all-matching-flow-entries)
- [Delete flow strict](https://ryu.readthedocs.io/en/latest/app/ofctl_rest.html#delete-flow-entry-strictly)
- [Delete all flows](https://ryu.readthedocs.io/en/latest/app/ofctl_rest.html#delete-all-flow-entries)

### Used data structures

We use the match and action data structures. You can find them [here](https://ryu.readthedocs.io/en/latest/app/ofctl_rest.html#reference-description-of-match-and-actions).