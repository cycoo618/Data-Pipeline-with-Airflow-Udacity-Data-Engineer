from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'

    @apply_defaults
    def __init__(self,
                 # Define your operators params (with defaults) here
                 # Example:
                 # conn_id = your-connection-name
                 table="",
                 sql_queries="",
                 redshift_conn_id="",
                 append_data="",
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        # Map params here
        # Example:
        # self.conn_id = conn_id
        self.table=table
        self.sql_queries=sql_queries
        self.redshift_conn_id=redshift_conn_id
        self.append_data=append_data

    def execute(self, context):
        self.log.info('LoadDimensionOperator not implemented yet')
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        self.log.info("Loading dimension table from Staging tables")
        if self.append_data == True:
            redshift.run("INSERT INTO {} {}".format(self.table, self.sql_queries))
        else:
            redshift.run("DELETE FROM {}".format(self.table_name))
            redshift.run("INSERT INTO {} {}".format(self.table, self.sql_queries))
            
        
        
