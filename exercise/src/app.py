from dosya_islemleri import read_csv, write_json, write_text
from processing import stats, build_report
from dekorator import required_column

@required_column({"name", "age", "city"})
def validate_rows(rows):
    return rows

def main():
    read_doc = "/home/ahsen/Masaüstü/betikOdevi/betik_diller/exercise/data/people.csv"
    write_doc = "/home/ahsen/Masaüstü/betikOdevi/betik_diller/exercise/data/stats.json"
    write_txt = "/home/ahsen/Masaüstü/betikOdevi/betik_diller/exercise/data/stats_txt.txt"

    rows = read_csv(read_doc)
    rows = validate_rows(rows)  # Kolon kontrolü burada yapılır
    st = stats(rows)

    write_json(write_doc, st)
    write_text(write_txt, build_report(st))
    

if __name__ == "__main__":
    main()
