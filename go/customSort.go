type byPriority []priority 
  
// have a sort interface 
func (s byPriority) Len() int {
  return len(s)
}
  
func (s byPriority) Swap(i, j int) {
    s[i], s[j] = s[j], s[i]
}
func (s byPriority) Less(i, j int) bool {
    return s[i].weight < s[j].weight
}


type priority struct {
  char rune
  // values should correspond to values in the ordered string 
  weight int
}

func customSortString(S string, T string) string {
  
  ordered := make(map[rune]int) // ordered, name of the rune + the "weight"
  for i, v := range S {
    ordered[v] = i
  }
  
  
  customSort := make(byPriority,0)
  for _, v := range T { 
    if val, ok := ordered[v]; ok {
      customSort = append(customSort, priority{char: v, weight: val})
    } else {
      customSort = append(customSort, priority{char: v, weight: 10000})
    }
  }
  
  sort.Sort(byPriority(customSort))
    
  var sorted string = "";
  
  // get all the values in sorted order 
  for _, v := range customSort {
    sorted += string(v.char)
  }
  
  return sorted 
  
}
