package program

type Dep struct {
	Prereq int
	Job    int
}

func TopologicalSort(jobs []int, deps []Dep) []int {
	// Write your code here.
	jobGraph := createJobGraph(jobs, deps)
	return orderedJobPairs(jobGraph)
}

func createJobGraph(jobs []int, deps []Dep) *JobGraph {
	graph := NewJobGraph(jobs)
	for _, dep := range deps {
		graph.AddPreq(dep.Job, dep.Prereq)
	}
	return graph
}

func orderedJobPairs(graph *JobGraph) []int {
	orderedJobs := []int{}
	nodes := graph.Nodes
	for len(nodes) != 0 {
		node := nodes[len(nodes)-1]
		nodes = nodes[:len(nodes)-1]
		containsCycle := dfs(node, &orderedJobs)
		if containsCycle {
			return []int{}
		}
	}
	return orderedJobs
}

func dfs(node *JobNode, orderedJobs *[]int) bool {
	if node.Visited {
		return false
	} else if node.Visiting {
		return true
	}
	node.Visiting = true 	
	for _, preqNode := range node.Prereqs {
		containsCycle := dfs(preqNode, orderedJobs) 
		if containsCycle {
			return true
		}
	}
	node.Visited = true
	node.Visiting = false
	*orderedJobs = append(*orderedJobs, node.Job)
	return false
}


type JobGraph struct {
	Nodes []*JobNode
	Graph map[int]*JobNode
}

func NewJobGraph(jobs []int) *JobGraph {
	g := &JobGraph{
		Graph: map[int]*JobNode{},
	}
	for _, job := range jobs {
		g.AddNode(job)
	}
	return g	
}

func (g *JobGraph) AddNode (job int) {
	g.Graph[job] = &JobNode{Job: job}
	g.Nodes = append(g.Nodes, g.Graph[job])
}

func (g *JobGraph) AddPreq(job, prereq int) {
	jobNode := g.GetNode(job)
	prereqNode := g.GetNode(prereq)
	jobNode.Prereqs = append(jobNode.Prereqs, prereqNode)
}

func (g *JobGraph) GetNode (job int) *JobNode {
	if _, found := g.Graph[job]; !found {
		g.AddNode(job)
	}
	return g.Graph[job]
}

type JobNode struct {
	Job int 
	Prereqs []*JobNode
	Visiting bool 
	Visited bool
}

