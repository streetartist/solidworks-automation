# AddEdges Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~AddEdges`

Adds edges to this edge flange.
Adds edges to this edge flange.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddEdges( _
   ByVal EdgeArray As System.Object, _
   ByVal SketchArray As System.Object _
) As System.Integer
```

```

Dim instance As IEdgeFlangeFeatureData
Dim EdgeArray As System.Object
Dim SketchArray As System.Object
Dim value As System.Integer
 
value = instance.AddEdges(EdgeArray, SketchArray)
```

```

System.int AddEdges( 
   System.object EdgeArray,
   System.object SketchArray
)
```

```

System.int AddEdges( 
   System.Object^ EdgeArray,
   System.Object^ SketchArray
) 
```

#### Parameters

*EdgeArray*
:   Array of [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)s associated with SketchArray

*SketchArray*
:   Array of [sketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)es associated with EdgeArray

#### Return Value

Error code as defined by [swEdgeFlangeError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEdgeFlangeError_e.html)

Remarks

Before calling this method, call [IModelDoc2::InsertSketchForEdgeFlange](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSketchForEdgeFlange.md) to associate the sketches with the edges.

Example

See the [IEdgeFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.md)  
[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.md)  
[IEdgeFlangeFeatureData::Edges Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~Edges.md)  
[IEdgeFlangeFeatureData::RemoveEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~RemoveEdges.md)  
[IEdgeFlangeFeatureData::IGetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~IGetEdges.md)  
[IEdgeFlangeFeatureData::ISetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~ISetEdges.md)
