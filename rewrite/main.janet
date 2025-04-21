(print "Lift build tool")

# get source files
# get header files

# build a depgraph

(defn build-depgraph
  "Builds a dependency graph from a list of source files and header files"
  [sources headers]
  (print "Building depgraph...")
  (map print sources)
  (map print headers)
)

(build-depgraph @["magic.c"] @["magic.h"])