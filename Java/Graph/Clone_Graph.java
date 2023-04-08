// 133. Clone Graph
// Leetcode Medium
// Date: 8 April 2023
// TC: O(N)
// SC: O(N)


// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}


class Solution {
    public Node clone(Node node, HashMap<Node, Node> vis )
    {
        Node newNode = new Node(node.val);
        vis.put(node, newNode);

        for(Node nod : node.neighbors)
        {
            if(vis.containsKey(nod))
                newNode.neighbors.add(vis.get(nod));
            else
                newNode.neighbors.add(clone(nod, vis));
        }
        return newNode;
    }
    public Node cloneGraph(Node node) {
        if (node == null) return null;
        HashMap<Node, Node> vis = new HashMap<Node, Node>();
        return clone(node, vis);

    }
}