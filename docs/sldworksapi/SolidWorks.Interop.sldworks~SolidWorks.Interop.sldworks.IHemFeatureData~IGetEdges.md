# IGetEdges Method (IHemFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData~IGetEdges`

Gets the edges for this hem.
Gets the edges for this hem.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetEdges( _
   ByVal EdgeCount As System.Integer _
) As System.Object
```

```

Dim instance As IHemFeatureData
Dim EdgeCount As System.Integer
Dim value As System.Object
 
value = instance.IGetEdges(EdgeCount)
```

```

System.object IGetEdges( 
   System.int EdgeCount
)
```

```

System.Object^ IGetEdges( 
   System.int EdgeCount
) 
```

#### Parameters

*EdgeCount*
:   Number of edges

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) of size EdgeCount

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [IHemFeatureData::GetEdgesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData~GetEdgesCount.md) before calling this method.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData.md)  
[IHemFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData_members.md)  
[IHemFeatureData::ISetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData~ISetEdges.md)  
[IHemFeatureData::Edges Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData~Edges.md)
