
import dask.dataframe as dd
from backend.ingection.parser import parse_log_line
from backend.ingection.loader import load_logs

def build_pipeline(file_path):
    bag=load_logs(file_path)
    parsed = (
        bag.map(parse_log_line)
        .filter(lambda x: x is not None)  
    )
    meta_data = {
        "timestamp": "datetime64[ns]", 
        "level" : "string", 
        "service" : "string", 
        "message" : "string",
    }
    df = parsed.to_dataframe(meta=meta_data)
    return df