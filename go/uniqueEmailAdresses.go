func numUniqueEmails(emails []string) int {
  // what if it does not have an @ ... skip ... continue 
  uniqueEmails := make(map[string]bool) // map to make sure emails are unique 
  for _, email := range emails {
    splitEmail := strings.Split(email, "@")
    currentEmail := ""
    if len(splitEmail) == 2 {
      localEmail := splitEmail[0]
      domainEmail := splitEmail[1]
      for _, char := range localEmail {
        if string(char) == "+" {
          break
        } else if string(char) == "." {
          currentEmail += ""
        } else {
          currentEmail += string(char)
        }
      }
      currentEmail += "@"
      currentEmail += domainEmail
      if _, ok := uniqueEmails[currentEmail]; !ok {
        uniqueEmails[currentEmail] = true 
      }
    } 
  }
  return len(uniqueEmails)
}
