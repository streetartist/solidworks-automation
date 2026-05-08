# GetContourEdgeCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetContourEdgeCount`

Gets the number of edges for this sketch contour.
Gets the number of edges for this sketch contour.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetContourEdgeCount() As System.Integer
```

```

Dim instance As ISketch
Dim value As System.Integer
 
value = instance.GetContourEdgeCount()
```

```

System.int GetContourEdgeCount()
```

```

System.int GetContourEdgeCount(); 
```

#### Return Value

Number of edges

Remarks

If the sketch contour is not closed or contains interior non-construction elements, this method returns 0.

Call this method before calling [ISketch::IGetContourEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetContourEdges.md) to get the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[ISketch::GetContourEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetContourEdges.md)
