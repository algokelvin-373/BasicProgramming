package javaapplication59;

import org.jgrapht.alg.DijkstraShortestPath;
import org.jgrapht.alg.KruskalMinimumSpanningTree;
import org.jgrapht.alg.PrimMinimumSpanningTree;
import org.jgrapht.graph.DefaultDirectedWeightedGraph;
import org.jgrapht.graph.DefaultEdge;
import org.jgrapht.graph.DefaultWeightedEdge;
import org.jgrapht.graph.SimpleGraph;
import org.jgrapht.graph.SimpleWeightedGraph;

public class JavaApplication59 {

public static void main(String[] args) {
int vCount = 6;
// SimpleGraph<String, DefaultEdge> graph = new SimpleGraph<>(DefaultEdge.class);
SimpleWeightedGraph<String, DefaultWeightedEdge> graph2 = new SimpleWeightedGraph<>(DefaultWeightedEdge.class);

String vertex[] = new String[vCount];
for (int i = 0; i < vertex.length; i++) {
vertex[i] = "y" + i;
graph2.addVertex(vertex[i]); 
//graph.addVertex(vertex[i]);
}
// graph.addEdge(vertex[0], vertex[1]);
// graph.addEdge(vertex[0], vertex[4]);
// graph.addEdge(vertex[1], vertex[2]);
// graph.addEdge(vertex[1], vertex[3]);
// graph.addEdge(vertex[1], vertex[4]);
// graph.addEdge(vertex[3], vertex[4]);
// graph.addEdge(vertex[2], vertex[5]);

graph2.addEdge(vertex[0], vertex[1]);
graph2.setEdgeWeight(graph2.getEdge(vertex[0], vertex[1]), 9.0);
graph2.addEdge(vertex[0], vertex[4]);
graph2.setEdgeWeight(graph2.getEdge(vertex[0], vertex[4]), 5.0);
graph2.addEdge(vertex[1], vertex[2]);
graph2.setEdgeWeight(graph2.getEdge(vertex[1], vertex[2]), 10.0);
graph2.addEdge(vertex[1], vertex[3]);
graph2.setEdgeWeight(graph2.getEdge(vertex[1], vertex[3]), 3.0);
graph2.addEdge(vertex[1], vertex[4]);
graph2.setEdgeWeight(graph2.getEdge(vertex[1], vertex[4]), 1.0);
graph2.addEdge(vertex[3], vertex[4]);
graph2.setEdgeWeight(graph2.getEdge(vertex[3], vertex[4]), 7.0);
graph2.addEdge(vertex[2], vertex[5]);
graph2.setEdgeWeight(graph2.getEdge(vertex[2], vertex[5]), 4.0);

/*pengunaan method dijkstra, kruskal, prim liat di javadoc packagenya ya..*/
}

}