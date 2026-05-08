# RemoveEdges Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~RemoveEdges`

Removes edges from this edge flange.
Removes edges from this edge flange.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveEdges( _
   ByVal EdgeArray As System.Object _
) As System.Integer
```

```

Dim instance As IEdgeFlangeFeatureData
Dim EdgeArray As System.Object
Dim value As System.Integer
 
value = instance.RemoveEdges(EdgeArray)
```

```

System.int RemoveEdges( 
   System.object EdgeArray
)
```

```

System.int RemoveEdges( 
   System.Object^ EdgeArray
) 
```

#### Parameters

*EdgeArray*
:   Array of [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)s to remove

#### Return Value

Error code as defined by [swEdgeFlangeError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEdgeFlangeError_e.html)

Example

[Remove Edge from Edge Flange Feature (C#)](Remove_Edge_from_Edge_Flange_Feature_Example_CSharp.htm)  
[Remove Edge from Edge Flange Feature (VB.NET)](Remove_Edge_from_Edge_Flange_Feature_Example_VBNET.htm)  
[Remove Edge from Edge Flange Feature (VBA)](Remove_Edge_from_Edge_Flange_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.md)  
[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.md)  
[IEdgeFlangeFeatureData::Edges Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~Edges.md)  
[IEdgeFlangeFeatureData::AddEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~AddEdges.md)  
[IEdgeFlangeFeatureData::IGetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~IGetEdges.md)  
[IEdgeFlangeFeatureData::ISetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~ISetEdges.md)
