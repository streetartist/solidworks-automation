# SetSetbackVertexDistance Method (ISimpleFilletFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetSetbackVertexDistance`

Sets the setback distances on fillet edges from the specified fillet corner vertex on this simple fillet feature.
Sets the setback distances on fillet edges from the specified fillet corner vertex on this simple fillet feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetSetbackVertexDistance( _
   ByVal Vtx As System.Object, _
   ByVal EdgeVar As System.Object, _
   ByVal DistVar As System.Object _
) As System.Boolean
```

```

Dim instance As ISimpleFilletFeatureData2
Dim Vtx As System.Object
Dim EdgeVar As System.Object
Dim DistVar As System.Object
Dim value As System.Boolean
 
value = instance.SetSetbackVertexDistance(Vtx, EdgeVar, DistVar)
```

```

System.bool SetSetbackVertexDistance( 
   System.object Vtx,
   System.object EdgeVar,
   System.object DistVar
)
```

```

System.bool SetSetbackVertexDistance( 
   System.Object^ Vtx,
   System.Object^ EdgeVar,
   System.Object^ DistVar
) 
```

#### Parameters

*Vtx*
:   [Vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md) for which to set setback distance

*EdgeVar*
:   Array of [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) for this vertex

*DistVar*
:   Array of distances

#### Return Value

True if the setback distances are set, false if not

Remarks

There is a one-to-one correspondence between the members of the EdgeVar and DistVar arrays.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md)  
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.md)  
[ISimpleFilletFeatureData2::GetSetbackDistanceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetSetbackDistanceCount.md)  
[ISimpleFilletFeatureData2::GetSetbackVertexDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetSetbackVertexDistance.md)  
[ISimpleFilletFeatureData2::GetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetSetbackVertices.md)  
[ISimpleFilletFeatureData2::GetSetbackVerticesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetSetbackVerticesCount.md)  
[ISimpleFilletFeatureData2::IGetSetbackVertexDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetSetbackVertexDistance.md)  
[ISimpleFilletFeatureData2::IGetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetSetbackVertices.md)  
[ISimpleFilletFeatureData2::SetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetSetbackVertices.md)
