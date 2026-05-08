# GetEdgesCount Method (ISketchContour)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour~GetEdgesCount`

Gets the number of edges in this sketch contour.
Gets the number of edges in this sketch contour.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEdgesCount() As System.Integer
```

```

Dim instance As ISketchContour
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

Call this method before calling [ISketchContour::IGetEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour~IGetEdges.md) to get the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchContour Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour.md)  
[ISketchContour Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour_members.md)  
[ISketchContour::GetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour~GetEdges.md)
