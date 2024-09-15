from database.DB_connect import DBConnect
from model.gene import Genes


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def get_all_chromosomes():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select distinct g.chromosome as chr
                        from genes g
                        where g.chromosome > 0"""
            cursor.execute(query)

            for row in cursor:
                result.append(row["chr"])

            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_all_genes():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select *
                        from genes g"""
            cursor.execute(query)

            for row in cursor:
                result.append(Genes(**row))

            cursor.close()
            cnx.close()
        return result


    @staticmethod
    def get_all_edges():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select g1.Chromosome as cr1, g2.Chromosome as cr2, g1.GeneID as g1, g2.GeneID as g2, i.Expression_Corr as corr
                        from interactions i, genes g1, genes g2
                        where i.GeneID1 <> i.GeneID2 
                        and i.GeneID1 = g1.GeneID
                        and i.GeneID2 = g2.GeneID
                        and g2.Chromosome <> g1.Chromosome
                        and g2.Chromosome > 0
                        and g1.Chromosome > 0
                        group by g1.GeneID, g2.GeneID"""
            cursor.execute(query)

            for row in cursor:
                result.append((row["cr1"], row["cr2"], row["g1"], row["g2"], row["corr"]))

            cursor.close()
            cnx.close()
        return result
