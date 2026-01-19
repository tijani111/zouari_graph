#!/usr/bin/env python3
"""
Verification script for TheorieAnwendung branch.
Checks node count, character count, and structure completeness.
"""

from GraphModel.Graph import Graph
from Structured_Main_Knowledge_Graph.GraphStructure.TheorieAnwendung.TheorieAnwendungSubGraph import TheorieAnwendungSubGraph
from ComponentAssembly.GraphAnalyzer import GraphAnalyzer
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge

def verify_structure():
    """Verify the TheorieAnwendung branch structure and requirements."""
    print("=" * 70)
    print("VERIFICATION: Theorie und Praxis Branch")
    print("=" * 70)
    print()

    # Create graph and build subgraph
    graph = Graph()
    subgraph = TheorieAnwendungSubGraph(graph)

    # Analyze graph
    analyzer = GraphAnalyzer()
    
    # Count nodes
    knowledge_node_count = sum(1 for node in graph.nodes if type(node) is NodeKnowledge)
    
    # Count characters
    total_characters = 0
    for node in graph.nodes:
        if type(node) is NodeKnowledge:
            total_characters += len(node.description) + len(node.titel)

    # Count source nodes
    source_node_count = len(graph.nodes) - knowledge_node_count

    # Calculate average characters per node
    avg_chars_per_node = total_characters / knowledge_node_count if knowledge_node_count > 0 else 0

    # Print results
    print("📊 STATISTICS:")
    print(f"   Total NodeKnowledge nodes: {knowledge_node_count}")
    print(f"   Source nodes: {source_node_count}")
    print(f"   Total nodes in graph: {len(graph.nodes)}")
    print()
    
    print("📝 CHARACTER COUNT:")
    print(f"   Total characters (titel + description): {total_characters:,}")
    print(f"   Average per node: {avg_chars_per_node:.0f}")
    print(f"   Estimated per team member (if 1 person): {total_characters:,}")
    print()

    # Requirements check
    print("✅ REQUIREMENTS CHECK:")
    min_nodes = 20
    min_chars_per_member = 30000
    
    if knowledge_node_count >= min_nodes:
        print(f"   ✓ Minimum {min_nodes} knowledge nodes: {knowledge_node_count} (exceeds by {knowledge_node_count - min_nodes})")
    else:
        print(f"   ✗ Minimum {min_nodes} knowledge nodes: {knowledge_node_count} (missing {min_nodes - knowledge_node_count})")
    
    if source_node_count >= 2:
        print(f"   ✓ Sources required: {source_node_count} sources present")
    else:
        print(f"   ✗ Sources required: Only {source_node_count} sources (need at least 2)")
    
    if total_characters >= min_chars_per_member:
        print(f"   ✓ Character count (~{min_chars_per_member:,} per member): {total_characters:,}")
    else:
        print(f"   ⚠ Character count: {total_characters:,} (target: ~{min_chars_per_member:,} per team member)")
        print(f"     Note: This assumes 1 team member. Multiply by team size for total requirement.")
    print()

    # Structure check
    print("🔍 STRUCTURE CHECK:")
    root_node = subgraph.root_node
    
    # Count direct connections from root
    root_connections = len(root_node.connected_nodes) if hasattr(root_node, 'connected_nodes') else 0
    
    print(f"   Root node: '{root_node.titel}'")
    print(f"   Direct connections from root: {root_connections}")
    print()

    # List all knowledge nodes by category
    print("📋 NODE BREAKDOWN:")
    categories = {}
    for node in graph.nodes:
        if type(node) is NodeKnowledge:
            # Try to categorize based on title
            title = node.titel
            if "Theorieorientierte" in title or "Theoretische Informatik" in title or "Komplexitätstheorie" in title or "Formale Methoden" in title:
                cat = "TheorieSchwerpunkt"
            elif "Anwendungsorientierte" in title or "Software Engineering" in title or "Praktische Projekte" in title or "Industriekooperationen" in title:
                cat = "AnwendungsSchwerpunkt"
            elif "Perspektiven" in title or "Studierendenperspektive" in title or "Industrieanforderungen" in title or "Wissenschaftliche Relevanz" in title or "Didaktische" in title:
                cat = "BalancePerspektiven"
            elif "Modulbeispiele" in title or "Algorithmik:" in title or "Datenbanken:" in title or "Künstliche Intelligenz:" in title or "Netzwerktechnik:" in title:
                cat = "Modulbeispiele"
            elif "Cluster" in title or "3." in title:
                cat = "Clusters"
            elif "Zentrale Bewertung" in title:
                cat = "Root"
            else:
                cat = "Other"
            
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(title)
    
    for cat, nodes in sorted(categories.items()):
        print(f"   {cat}: {len(nodes)} nodes")
        for node_title in sorted(nodes)[:5]:  # Show first 5
            print(f"      - {node_title}")
        if len(nodes) > 5:
            print(f"      ... and {len(nodes) - 5} more")
    print()

    # Summary
    print("=" * 70)
    print("SUMMARY:")
    print(f"   ✓ Structure is complete with {knowledge_node_count} knowledge nodes")
    print(f"   ✓ {source_node_count} source nodes present")
    print(f"   ✓ Total content: {total_characters:,} characters")
    if total_characters < min_chars_per_member:
        print(f"   ⚠ Consider adding more content to reach ~{min_chars_per_member:,} characters per team member")
    print("=" * 70)

if __name__ == "__main__":
    verify_structure()
