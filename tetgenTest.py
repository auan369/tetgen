import pyvista as pv
import tetgen
import numpy as np
pv.set_plot_theme('document')
#import numpy
#from stl import mesh



mesh = pv.read('ball10.stl')

#mesh = pv.read('Assignment_1.stl')

# Write the mesh to a TetGen input file
#mesh.save('button_cap.poly')

#sphere = pv.Sphere()
tet = tetgen.TetGen(mesh)
vertices,elems = tet.tetrahedralize(order=1, mindihedral=20, minratio=1.5)
grid = tet.grid

grid.plot(show_edges=True)


mask = np.logical_or(grid.points[:, 0] < 0, grid.points[:, 0] > 0.5)
half = grid.extract_points(mask)
plotter = pv.Plotter()

#plotter.add_mesh(half, color="w", show_edges=True)
plotter.add_mesh(grid, color="r", style="wireframe", opacity=0.2)
#plotter.camera_position = cpos
plotter.show()

def get_edges_from_tetrahedra(vertices, elems):
    edges = set()
    
    for tetrahedron in elems:
        # Tetrahedron vertices
        v0, v1, v2, v3 = sorted(tetrahedron)  # Sort vertices in ascending order
        
        # Define edges of the tetrahedron as pairs of vertices
        tetrahedron_edges = [
            (v0, v1), (v0, v2), (v0, v3),
            (v1, v2), (v1, v3), (v2, v3)
        ]
        
        # Add the edges to the set (removing duplicates)
        edges.update(tetrahedron_edges)
    
    # Convert the set of edges back to a list
    edge_list = list(edges)
    edge_list.sort()
    edge_list = [val for pair in edge_list for val in pair]
    
    return edge_list

verts = []
tetIds = []
tetEdgeIds = []
tetSurfaceTriIds = []

tetEdgeIds = get_edges_from_tetrahedra(vertices, elems)




for i, vertex in enumerate(vertices):
    verts.extend(vertex)
print("Number of points: ",len(vertices))
print("Number of tetrahedra: ",len(elems))

for i, elem in enumerate(elems):
    tetIds.extend(elem)  # Assuming each tetrahedron has 4 vertices
    
'''
The faces array is organized as::
    [n0, p0_0, p0_1, ..., p0_n, n1, p1_0, p1_1, ..., p1_n, ...]
    where ``n0`` is the number of points in face 0, and ``pX_Y`` is the
    Y'th point in face X.
remove every third element and the first element; these are the number of vertices in each face
'''
faces_array = np.array(tet.mesh.faces)
indices_to_keep = np.arange(len(faces_array)) % 4 != 0
tetSurfaceTriIds = faces_array[indices_to_keep]






# print(vertices)
# print(elems)
# print(tetEdgeIds[:10])
# print(tetSurfaceTriIds[:10])
# print(elems[0])
# print(elems[1])
# print(elems[2])
# print(elems[3])

# for i, vertex in enumerate(vertices):
#     verts_array.extend(vertex)

#print(verts_array)



import json
verts = [float(v) for v in verts]
tetIds = [int(t) for t in tetIds]
tetEdgeIds = [int(te) for te in tetEdgeIds]
tetSurfaceTriIds = [int(ts) for ts in tetSurfaceTriIds]
# Assuming you have already populated verts, tetIds, tetEdges, and tetSurfaceTriIds lists

# Define a dictionary to hold the data
data = {
    "name": "test2",
    "verts": verts,
    "tetIds": tetIds,
    "tetEdgeIds": tetEdgeIds,
    "tetSurfaceTriIds": tetSurfaceTriIds
}

# Specify the output JSON file path
output_file_path = "output_data_ball10.json"

# Write the data to the JSON file
with open(output_file_path, "w") as outfile:
    json.dump(data, outfile, separators=(",", ":"))

print(f"Data has been saved to {output_file_path}")





vertices_out = []
for i, vertex in enumerate(vertices):
    temp = [float(v) for v in vertex]
    vertices_out.append(temp)


data2 = {
    "vertices": vertices_out,
}

#! getting the vertices for mujoco c++ code
with open('output.txt', 'w') as file:
    for i, vertex in enumerate(vertices):
        print(f"std::vector<double> pos{i} =  {{{vertex[0]},{vertex[1]},{vertex[2]}}};", file=file)

    print("std::vector<double> dummy = {0.0,0.0,0.0};", file=file)

    print("std::vector<std::vector<double>> arrayOfPos ={", end ="", file=file)
    for i, vertex in enumerate(vertices):
        if i == len(vertices)-1:
            print(f"pos{i}", end ="", file=file)
        else:
            print(f"pos{i}", end =",", file=file)
    print("};", file=file)

    print("std::vector<std::vector<double>> arrayOfOldPos ={", end ="", file=file)
    for i, vertex in enumerate(vertices):
        if i == len(vertices)-1:
            print(f"pos{i}", end ="", file=file)
        else:
            print(f"pos{i}", end =",", file=file)
    print("};", file=file)

    print("std::vector<std::vector<double>> arrayOfVel ={", end ="", file=file)
    for i, vertex in enumerate(vertices):
        if i == len(vertices)-1:
            print(f"dummy", end ="", file=file)
        else:
            print(f"dummy", end =",", file=file)
    print("};", file=file)

    print("std::vector<std::vector<double>> arrayOfPosChangeLinear ={", end ="", file=file)
    for i, vertex in enumerate(vertices):
        if i == len(vertices)-1:
            print(f"pos{i}", end ="", file=file)
        else:
            print(f"pos{i}", end =",", file=file)
    print("};", file=file)

    print("std::vector<std::vector<double>> arrayOfPosChangeVol ={", end ="", file=file)
    for i, vertex in enumerate(vertices):
        if i == len(vertices)-1:
            print(f"pos{i}", end ="", file=file)
        else:
            print(f"pos{i}", end =",", file=file)
    print("};", file=file)

    print("std::vector<double> arrayOfInvMass;", file=file)
    print("std::vector<std::vector<double>> arrayOfTet = {", file=file)
    for i, elem in enumerate(elems):
        if i == len(elems)-1:
            print(f"{{{elem[0]},{elem[1]},{elem[2]},{elem[3]}}}", end ="};\n", file=file)
        else:
            print(f"{{{elem[0]},{elem[1]},{elem[2]},{elem[3]}}}", end =",\n", file=file)
    print("std::vector<double> volRest;", file=file)
    print("std::vector<double> volCurrent;", file=file)
    print("std::vector<std::vector<double>> arrayOfEdges={", file=file)
    for i in range(len(tetEdgeIds)//2):
        if i == len(tetEdgeIds)//2-1:
            print(f"{{{tetEdgeIds[2*i]},{tetEdgeIds[2*i+1]}}}", end ="};\n", file=file)
        else:
            print(f"{{{tetEdgeIds[2*i]},{tetEdgeIds[2*i+1]}}}", end =",\n", file=file)
#! end of prints

# Specify the output JSON file path
output_file_path = "output_vertices_ball10.json"

# Write the data to the JSON file
with open(output_file_path, "w") as outfile:
    json.dump(data2, outfile, separators=(",", ":"))

print(f"Data has been saved to {output_file_path}")