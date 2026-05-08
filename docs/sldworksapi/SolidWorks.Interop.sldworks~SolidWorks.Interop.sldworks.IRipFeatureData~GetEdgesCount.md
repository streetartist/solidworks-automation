# GetEdgesCount Method (IRipFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData~GetEdgesCount`

Gets the number of edges for this rip feature.
Gets the number of edges for this rip feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEdgesCount() As System.Integer
```

```

Dim instance As IRipFeatureData
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

Call this method before calling [IRipFeatureData::IGetEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData~IGetEdges.md) to get the size of the array for that method.

Example

See the [IRipFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRipFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData.md)  
[IRipFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData_members.md)  
[IRipFeatureData::ISetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData~ISetEdges.md)  
[IRipFeatureData::Edges Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData~Edges.md)
