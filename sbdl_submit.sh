spark-submit --master yarn --deploy-mode cluster \
--py-files sdbl_lib.zip \
--files conf/sbdl.conf,con/spark.conf,log4j.properties \
sbdl_main.py qa 2025-04-02
