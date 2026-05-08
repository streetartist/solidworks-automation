# GetSetbackDistanceCount Method (ISimpleFilletFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetSetbackDistanceCount`

Gets the number of setback distances for the specified vertex on this simple fillet feature.
Gets the number of setback distances for the specified vertex on this simple fillet feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSetbackDistanceCount( _
   ByVal Vtx As Vertex _
) As System.Integer
```

```

Dim instance As ISimpleFilletFeatureData2
Dim Vtx As Vertex
Dim value As System.Integer
 
value = instance.GetSetbackDistanceCount(Vtx)
```

```

System.int GetSetbackDistanceCount( 
   Vertex Vtx
)
```

```

System.int GetSetbackDistanceCount( 
   Vertex^ Vtx
) 
```

#### Parameters

*Vtx*
:   [Vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md)

#### Return Value

Number of setback distances and number of edges

Remarks

Because there is a one-to-one correspondence between the edges and distances, the Count argument also represents the number of edges at the specified vertex.

Call this method before calling [ISimpleFilletFeatureData2::IGetSetbackVertexDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetSetbackVertexDistance.md) to get the number setback distances and number of edges for the vertex.

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
