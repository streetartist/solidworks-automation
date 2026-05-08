# GetEdgesCount Method (IHemFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData~GetEdgesCount`

Gets the number of edges for this hem.
Gets the number of edges for this hem.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEdgesCount() As System.Integer
```

```

Dim instance As IHemFeatureData
Dim value As System.Integer
 
value = instance.GetEdgesCount()
```

```

System.int GetEdgesCount()
```

```

System.int GetEdgesCount(); 
```

#### Return Value

Number of edges

Remarks

Call this method before calling [IHemFeatureData::IGetEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData~IGetEdges.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData.md)  
[IHemFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData_members.md)  
[IHemFeatureData::ISetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData~ISetEdges.md)  
[IHemFeatureData::Edges Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData~Edges.md)
