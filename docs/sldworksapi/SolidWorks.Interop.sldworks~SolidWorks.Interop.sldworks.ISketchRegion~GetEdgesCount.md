# GetEdgesCount Method (ISketchRegion)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion~GetEdgesCount`

Gets the number of edges for this sketch region.
Gets the number of edges for this sketch region.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEdgesCount() As System.Integer
```

```

Dim instance As ISketchRegion
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

Call this method before calling [ISketchRegion::IGetEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion~IGetEdges.md) to get the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchRegion Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion.md)  
[ISketchRegion Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion_members.md)  
[ISketchRegion::GetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion~GetEdges.md)
