# ICreateBrepBody3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBrepBody3`

Creates a temporary body from BREP (boundary representation) data.
Creates a temporary body from BREP (boundary representation) data.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateBrepBody3( _
   ByVal Type As System.Integer, _
   ByVal NTopologies As System.Integer, _
   ByRef Topologies As System.Integer, _
   ByRef EdgeTolArray As System.Double, _
   ByRef VertexTolArray As System.Double, _
   ByRef PointArray As System.Double, _
   ByRef CurveArra1 As Curve, _
   ByRef CurveSurfaceArray1 As Surface, _
   ByRef CurveArray2 As Curve, _
   ByRef CurveSurfaceArray2 As Surface, _
   ByRef SurfaceArray As Surface, _
   ByVal NRelations As System.Integer, _
   ByRef Parents As System.Integer, _
   ByRef Children As System.Integer, _
   ByRef Senses As System.Integer, _
   ByVal Option As System.Integer _
) As Body2
```

```

Dim instance As IModeler
Dim Type As System.Integer
Dim NTopologies As System.Integer
Dim Topologies As System.Integer
Dim EdgeTolArray As System.Double
Dim VertexTolArray As System.Double
Dim PointArray As System.Double
Dim CurveArra1 As Curve
Dim CurveSurfaceArray1 As Surface
Dim CurveArray2 As Curve
Dim CurveSurfaceArray2 As Surface
Dim SurfaceArray As Surface
Dim NRelations As System.Integer
Dim Parents As System.Integer
Dim Children As System.Integer
Dim Senses As System.Integer
Dim Option As System.Integer
Dim value As Body2
 
value = instance.ICreateBrepBody3(Type, NTopologies, Topologies, EdgeTolArray, VertexTolArray, PointArray, CurveArra1, CurveSurfaceArray1, CurveArray2, CurveSurfaceArray2, SurfaceArray, NRelations, Parents, Children, Senses, Option)
```

```

Body2 ICreateBrepBody3( 
   System.int Type,
   System.int NTopologies,
   ref System.int Topologies,
   ref System.double EdgeTolArray,
   ref System.double VertexTolArray,
   ref System.double PointArray,
   ref Curve CurveArra1,
   ref Surface CurveSurfaceArray1,
   ref Curve CurveArray2,
   ref Surface CurveSurfaceArray2,
   ref Surface SurfaceArray,
   System.int NRelations,
   ref System.int Parents,
   ref System.int Children,
   ref System.int Senses,
   System.int Option
)
```

```

Body2^ ICreateBrepBody3( 
   System.int Type,
   System.int NTopologies,
   System.int% Topologies,
   System.double% EdgeTolArray,
   System.double% VertexTolArray,
   System.double% PointArray,
   Curve^% CurveArra1,
   Surface^% CurveSurfaceArray1,
   Curve^% CurveArray2,
   Surface^% CurveSurfaceArray2,
   Surface^% SurfaceArray,
   System.int NRelations,
   System.int% Parents,
   System.int% Children,
   System.int% Senses,
   System.int Option
) 
```

#### Parameters

*Type*
:   Type of body to create as defined in [swTopology\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTopology_e.html)

*NTopologies*
:   Number of topological entities in the topologies argument

*Topologies*
:   Array of topologies (see [swTopoEntity\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTopoEntity_e.html)), one for each topological entity

*EdgeTolArray*
:   Array of tolerances for edges

*VertexTolArray*
:   Array of tolerances for vertices

*PointArray*
:   Array of coordinates of vertices (geometry for vertices)

*CurveArra1*
:   Array of [curves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md) (geometry for edges; 3D curve) and coedges (geometry for coedges; 2D curve)

*CurveSurfaceArray1*
:   Array of [surfaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md) that lie on CurveArra1 2D curve

*CurveArray2*
:   Array of [curves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md) (geometry for edges; 3D curve) and array of coedges (geometry for coedges; 2D curve)

*CurveSurfaceArray2*
:   Array of [surfaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md) that on lie on CurveArray2 2D curve

*SurfaceArray*
:   Array of [surfaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md) (geometry for faces)

*NRelations*
:   Number of 1-to-1 relationships between topological entities

*Parents*
:   Array of parents, one in each relationship

*Children*
:   Array of children, one in each relationship

*Senses*
:   Array of senses in which child is used by parent in the relationship

*Option*
:   - 0 = Default

    1 = Repair and simplify body

    2 = Simplify body

#### Return Value

[Body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Remarks

The CurveArray1 and CurveArray2 must be paired with CurveSurfaceArray1 and CurveSurfaceArray2, respectively. Order is not important. The 2D curve has to be created in the direction of the loop.

If non-negative values are packed into the EdgeToleranceArray and VertexToleranceArray arrays, then tolerances are applied to the corresponding edges or vertices. These arrays should be the same size as CurveArray1 and PointArray, respectively. Otherwise, a default value of 1.0e-8 (modeler precision) is used.

NOTE: [IModeler::SetInitKnitGapWidth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~SetInitKnitGapWidth.md) does not affect this method.

Useful methods for creating geometry for the topological entities are:

- [IBody2::CreatePlanarSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreatePlanarSurface.md) or [IBody2::ICreatePlanarSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreatePlanarSurface.md)
- [IBody2::AddProfileArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddProfileArc.md) or [IBody2::IAddProfileArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileArc.md)
- [IBody2::AddProfileLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddProfileLine.md) or [IBody2::IAddProfileLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileLine.md)
- [IBody2::CreateRevolutionSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateRevolutionSurface.md) or [IBody2::ICreateRevolutionSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateRevolutionSurface.md)

For example, to create a cone, find topological relationships and form relevant arrays. A complete solid cone consists of 8 topological entities:

- 1 shell
- 2 faces
- 3 loops
- 1 edge
- 1 vertex

There are 8 relations:

- the shell is the parent of 2 faces - 2
- the planar end face has 1 loop - 1
- the conical face has 2 loops - 2
- two loops are each the parent of 1 edge - 2
- one loop is the parent of 1 vertex 1

The topologies array:

|  |  |
| --- | --- |
| **Index** | **Value** |
| 0 | swTopoShell |
| 1 | swTopoFace |
| 2 | swTopoFace |
| 3 | swTopoLoop |
| 4 | swTopoEdge |
| 5 | swTopoLoop |
| 6 | swTopoLoop |
| 7 | swTopoVertex |

The set of arrays:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| index | parents | children | senses | relation |
| 0 | 0 | 1 | 0 | shell to face |
| 1 | 0 | 2 | 0 | shell to face |
| 2 | 1 | 3 | 0 | face to loop |
| 3 | 3 | 4 | -1 | loop to edge |
| 4 | 2 | 5 | 0 | face to loop |
| 5 | 2 | 6 | 0 | face to loop |
| 6 | 5 | 4 | 1 | loop to edge |
| 7 | 6 | 7 | 0 | loop to vertex |

Values in the parents and children arrays correspond to the indices of the topology array.

Each face or edge created by [IModeler::CreateBrepBody3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBrepBody3.md) or IModeler::ICreateBrepBody3 has an associated integer ID that is the same as the index to the input topologies. Use [IFace2::GetFaceId](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetFaceId.md) or [IEdge::GetId](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetID.md) to get the associated integer ID.

Every shell should be a closed shell. Sheet bodies should have additional back faces to form a closed shell. When creating a sheet body, these extra back faces are retained in the result and should be removed using [IModeler::DeleteFacesFromSheetBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~DeleteFacesFromSheetBody.md) or [IModeler::IDeleteFacesFromSheetBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IDeleteFacesFromSheetBody.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::CreateBodiesFromSheets2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodiesFromSheets2.md)  
[IModeler::CreateBodyFromBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromBox.md)  
[IModeler::CreateBodyFromCone Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromCone.md)  
[IModeler::CreateBodyFromCyl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromCyl.md)  
[IModeler::CreateBodyFromFaces2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromFaces2.md)  
[IModeler::CreateBrepBody3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBrepBody3.md)  
[IModeler::CreateExtrudedBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateExtrudedBody.md)  
[IModeler::CreateSweptBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSweptBody.md)  
[IModeler::CreateWireBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateWireBody.md)  
[IModeler::ICreateBodiesFromSheets2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodiesFromSheets2.md)  
[IModeler::ICreateBodyFromBox2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromBox2.md)  
[IModeler::ICreateBodyFromCone2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCone2.md)  
[IModeler::ICreateBodyFromCyl2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCyl2.md)  
[IModeler::ICreateBodyFromFaces3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromFaces3.md)  
[IModeler::ICreateWireBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateWireBody.md)
