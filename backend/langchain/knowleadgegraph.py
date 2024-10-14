from dotenv import load_dotenv

from langchain_community.graphs import Neo4jGraph
from langchain_groq import ChatGroq
from langchain_core.documents import Document
from langchain_experimental.graph_transformers import LLMGraphTransformer

load_dotenv()

graph = Neo4jGraph()

llm = ChatGroq(model_name ="Gemma2-9b-It")

text = """
Abstract —Authentication is a significant issue in system 
control in computer based communication. Human face 
recognition is an important branch of biometric verification 
and has been widely used in many applications, such as video 
monitor system, human-computer interaction, and door 
control system and network security. This paper describes a 
method for Student’s Attendance System which will integrate 
with the face recognition technology using Personal 
Component Analysis (PCA) algorithm. The system will record 
the attendance of the students in class room environment 
automatically and it will provide the facilities to the faculty to 
access the information of the students easily by maintaining a 
log for clock-in and clock-out time. 
 
Index Terms —Face recognition system, automatic 
attendance, authentication, bio-metric, PCA. 
 
I. INTRODUCTION  
Face recognition is as old as computer vision, both 
because of the practical importance of the topic and 
theoretical interest from cognitive scientists. Despite the fact 
that other methods of identification (such as fingerprints, or 
iris scans) can be more accurate, face recognition has always 
remains a major focus of research because of its non-
invasive nature and because it is people's primary method of 
person identification. Face recognition technology is 
gradually evolving to a universal biometric solution since it 
requires virtually zero effort from the user end while 
compared with other biometric options. Biometric face 
recognition is basically used in three main domains: time 
attendance systems and employee management; visitor 
management systems; and last but not the least authorization 
systems and access control systems. 
Traditionally, student’s a ttendances are taken manually by 
using attendance sheet given by the faculty members in class, 
which is a time consuming event. Moreover, it is very 
difficult to verify one by one student in a large classroom 
environment with distributed branches whether the 
authenticated students are actually responding or not. 
The present authors demonstrate in this paper how face 
recognition can be used for an effective attendance system 
to automatically record the presence of an enrolled 
individual within the respective venue. Proposed system 
also maintains a log file to keep records of the entry of every 
individual with respect to a universal system time.
"""

documents = [Document(page_content=text)]

llm_transformer = LLMGraphTransformer(llm=llm)

graph_documents = llm_transformer.convert_to_graph_documents(documents)

print(f"Nodes:{graph_documents[0].nodes}")
print(f"Relationships:{graph_documents[0].relationships}")

graph.add_graph_documents(graph_documents)
