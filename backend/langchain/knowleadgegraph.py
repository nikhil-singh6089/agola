import os
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
 
Manuscript received March 8, 2012; revised May 14, 2012 . 
The authors are with the Computer Science and Engineer ing Department , 
National Institute of Technology, Agartala , India (e-mail: 
nirmalya.kar@gmail.com, mkdb06@gmail.com, ashim.nita@gmail.com, 
dwijen.rudrapal@gmail.com ). A. Background and Related Work 
The first attempts to use face recognition began in the 
1960’s with a semi -automated system. Marks were made on 
photographs to locate the major features; it used features 
such as eyes, ears, noses, and mouths. Then distances and 
ratios were computed from these marks to a common 
reference point and compared to reference data. In the early 
1970’s Goldstein, Harmon and Lesk [2] created a system of 
21 subjective markers such as hair colour and lip thickness. 
This proved even harder to automate due to the subjective 
nature of many of the measurements still made completely 
by hand.  
Fisher and Elschlagerb [3] approaches to measure 
different pieces of the face and mapped them all onto a 
global template, which was found that these features do not 
contain enough unique data to represent an adult face. 
Another approach is the Connectionist approach [4], 
which seeks to classify the human face using a combination 
of both range of gestures and a set of identifying markers. 
This is usually implemented using 2-dimensional pattern 
recognition and neural net principles. Most of the time this 
approach requires a huge number of training faces to 
achieve decent accuracy; for that reason it has yet to be 
implemented on a large scale. 
The first fully automated system [5] to be developed 
utilized very general pattern recognition. It compared faces 
to a generic face model of expected features and created a 
series of patters for an image relative to this model. This 
approach is mainly statistical and relies on histograms and 
the gray scale value.
"""

documents = [Document(page_content=text)]

llm_transformer = LLMGraphTransformer(llm=llm)

graph_documents = llm_transformer.convert_to_graph_documents(documents)

print(f"Nodes:{graph_documents[0].nodes}")
print(f"Relationships:{graph_documents[0].relationships}")

graph.add_graph_documents(graph_documents)
