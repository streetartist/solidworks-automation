# IGetSetbackVertexDistance Method (ISimpleFilletFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetSetbackVertexDistance`

Gets the setback distance for the specified vertex on this simple fillet feature.
Gets the setback distance for the specified vertex on this simple fillet feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSetbackVertexDistance( _
   ByVal Count As System.Integer, _
   ByVal Vtx As Vertex, _
   ByRef EdgeArr As Edge _
) As System.Double
```

```

Dim instance As ISimpleFilletFeatureData2
Dim Count As System.Integer
Dim Vtx As Vertex
Dim EdgeArr As Edge
Dim value As System.Double
 
value = instance.IGetSetbackVertexDistance(Count, Vtx, EdgeArr)
```

```

System.double IGetSetbackVertexDistance( 
   System.int Count,
   Vertex Vtx,
   out Edge EdgeArr
)
```

```

System.double IGetSetbackVertexDistance( 
   System.int Count,
   Vertex^ Vtx,
   [Out] Edge^ EdgeArr
) 
```

#### Parameters

*Count*
:   Number of edges and setback distances for this vertex

*Vtx*
:   [Vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md) for which to get setback distance

*EdgeArr*
:   - in-process, unmanaged C++: Pointer to an array of [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) at the specified vertex (see **Remarks**)

    VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

#### Return Value

- in-process, unmanaged C++: Pointer to an array of setback distances at the specified vertex

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

There is a one-to-one correspondence between the edge array and the setback distance array.

Before calling this method, call [ISimpleFilletFeatureData2::GetSetbackDistanceCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetSetbackDistanceCount.md) to get the number of edges and setback distances at the specified vertex.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md)  
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.md)  
[ISimpleFilletFeatureData2::GetSetbackVertexDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetSetbackVertexDistance.md)  
[ISimpleFilletFeatureData2::GetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetSetbackVertices.md)  
[ISimpleFilletFeatureData2::GetSetbackVerticesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetSetbackVerticesCount.md)  
[ISimpleFilletFeatureData2::IGetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetSetbackVertices.md)  
[ISimpleFilletFeatureData2::ISetSetbackVertexDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetSetbackVertexDistance.md)  
[ISimpleFilletFeatureData2::ISetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetSetbackVertices.md)  
[ISimpleFilletFeatureData2::SetSetbackVertexDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetSetbackVertexDistance.md)  
[ISimpleFilletFeatureData2::SetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetSetbackVertices.md)
