# GetSketchContourCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchContourCount`

Gets the number of sketch contours in this sketch.
Gets the number of sketch contours in this sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSketchContourCount() As System.Integer
```

```

Dim instance As ISketch
Dim value As System.Integer
 
value = instance.GetSketchContourCount()
```

```

System.int GetSketchContourCount()
```

```

System.int GetSketchContourCount(); 
```

#### Return Value

Number of sketch contours

Remarks

Call this method before calling [ISketch::IGetSketchContours](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSketchContours.md) to get the size of the array for that method.

This method works even if the sketch is suppressed.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[ISketch::GetSketchContours Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchContours.md)
