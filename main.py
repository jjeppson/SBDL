import sys
from lib import Utils
from lib.logger import Log4j

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("usage: sbdl{local, qa, prod} {load_date}: Arguments are missing")
        sys.exit(-1)
    
    job_run_env = sys.argv[1].upper()
    load_date = sys.argv[2]

    spark = Utils.get_spark_session(job_run_env)
    logger = Log4j(spark)

    logger.info("Finished creating Spark Session")

    orders_list = [("01","02",350,1),
                ("01","04",580,1),
                ("01","07",320,2),
                ("02","03",450,1),
                ("02","06",220,1),
                ("03","01",195,1),
                ("04","09",270,3),
                ("04","08",410,2),
                ("05","02",350,1)]

    order_df = spark.createDataFrame(orders_list).toDF("order_id","prod_id","unit_price","qty")
    order_df.show()

