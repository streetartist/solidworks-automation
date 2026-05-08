# ISetSetbackVertexDistance Method (IVariableFilletFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ISetSetbackVertexDistance`

Sets the setback distance for the specified vertex and its edges on this variable fillet feature.
Sets the setback distance for the specified vertex and its edges on this variable fillet feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISetSetbackVertexDistance( _
   ByVal Count As System.Integer, _
   ByVal Vtx As Vertex, _
   ByRef EdgeArr As Edge, _
   ByRef DistArr As System.Double _
) As System.Boolean
```

```

Dim instance As IVariableFilletFeatureData2
Dim Count As System.Integer
Dim Vtx As Vertex
Dim EdgeArr As Edge
Dim DistArr As System.Double
Dim value As System.Boolean
 
value = instance.ISetSetbackVertexDistance(Count, Vtx, EdgeArr, DistArr)
```

```

System.bool ISetSetbackVertexDistance( 
   System.int Count,
   Vertex Vtx,
   ref Edge EdgeArr,
   ref System.double DistArr
)
```

```

System.bool ISetSetbackVertexDistance( 
   System.int Count,
   Vertex^ Vtx,
   Edge^% EdgeArr,
   System.double% DistArr
) 
```

#### Parameters

*Count*
:   Number of setback distances

*Vtx*
:   [Vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md) for which to set the setback distance

*EdgeArr*
:   - in-process, unmanaged C++: Pointer to an array of [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) at the specified vertex (see **Remarks**)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*DistArr*
:   - in-process, unmanaged C++: Pointer to an array of setback distances at the specified

    - VBA, VB.NET, C#, and C++/CLI: Not supported

#### Return Value

TRUE if setback distance is set, FALSE if not

Remarks

There is a one-to-one correspondence between the edge array and the distance array.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.md)  
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.md)  
[IVariableFilletFeatureData2::SetSetbackVertexDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetSetbackVertexDistance.md)  
[IVariableFilletFeatureData2::SetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetSetbackVertices.md)  
[IVariableFilletFeatureData2::ISetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ISetSetbackVertices.md)  
[IVariableFilletFeatureData2::GetSetbackDistanceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetSetbackDistanceCount.md)  
[IVariableFilletFeatureData2::GetSetbackVertexDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetSetbackVertexDistance.md)  
[IVariableFilletFeatureData2::GetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetSetbackVertices.md)  
[IVariableFilletFeatureData2::GetSetbackVerticesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetSetbackVerticesCount.md)  
[IVariableFilletFeatureData2::IGetSetbackVertexDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~IGetSetbackVertexDistance.md)  
[IVariableFilletFeatureData2::IGetSetbackVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~IGetSetbackVertices.md)
