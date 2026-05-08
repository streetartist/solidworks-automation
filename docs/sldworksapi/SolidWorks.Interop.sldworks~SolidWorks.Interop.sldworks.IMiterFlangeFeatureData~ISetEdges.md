# ISetEdges Method (IMiterFlangeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~ISetEdges`

Sets the edges for this miter flange feature.
Sets the edges for this miter flange feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetEdges( _
   ByVal EdgeCount As System.Integer, _
   ByRef EdgeArray As System.Object _
) 
```

```

Dim instance As IMiterFlangeFeatureData
Dim EdgeCount As System.Integer
Dim EdgeArray As System.Object
 
instance.ISetEdges(EdgeCount, EdgeArray)
```

```

void ISetEdges( 
   System.int EdgeCount,
   ref System.object EdgeArray
)
```

```

void ISetEdges( 
   System.int EdgeCount,
   System.Object^% EdgeArray
) 
```

#### Parameters

*EdgeCount*
:   Number of edges

*EdgeArray*
:   - in-process, unmanaged C++: Pointer to an array of [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) used to define the miter flange feature

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMiterFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData.md)  
[IMiterFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData_members.md)  
[IMiterFlangeFeatureData::IGetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~IGetEdges.md)  
[IMiterFlangeFeatureData::IGetEdgesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~IGetEdgesCount.md)  
[IMiterFlangeFeatureData::Edges Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~Edges.md)
