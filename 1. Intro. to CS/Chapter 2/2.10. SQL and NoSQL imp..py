#SQL Implementation (SQLite)
import sqlite3

class SQLDatabase:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS nodes
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            label TEXT,
                            data TEXT)''')
        self.conn.commit()

    def create_node(self, label, data):
        self.cursor.execute('INSERT INTO nodes (label, data) VALUES (?, ?)', (label, data))
        self.conn.commit()

    def read_node(self, node_id):
        self.cursor.execute('SELECT * FROM nodes WHERE id=?', (node_id,))
        return self.cursor.fetchone()

    def update_node(self, node_id, label, data):
        self.cursor.execute('UPDATE nodes SET label=?, data=? WHERE id=?', (label, data, node_id))
        self.conn.commit()

    def delete_node(self, node_id):
        self.cursor.execute('DELETE FROM nodes WHERE id=?', (node_id,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()

db = SQLDatabase('data.db')
db.create_node('Person', 'John')
node = db.read_node(1)
print("Read node:", node)
db.update_node(1, 'Person', 'Jane')
updated_node = db.read_node(1)
print("Updated node:", updated_node)
db.delete_node(1)
db.close_connection()


#NoSQL Implementation (Graph Database using NetworkX)
import networkx as nx

class GraphDatabase:
    def __init__(self):
        self.graph = nx.Graph()

    def create_node(self, node_id, label, data):
        self.graph.add_node(node_id, label=label, data=data)

    def read_node(self, node_id):
        return self.graph.nodes[node_id]

    def update_node(self, node_id, label, data):
        self.graph.nodes[node_id]['label'] = label
        self.graph.nodes[node_id]['data'] = data

    def delete_node(self, node_id):
        self.graph.remove_node(node_id)

db = GraphDatabase()
db.create_node(1, 'Person', 'John')
node = db.read_node(1)
print("Read node:", node)
db.update_node(1, 'Person', 'Jane')
updated_node = db.read_node(1)
print("Updated node:", updated_node)
db.delete_node(1)
