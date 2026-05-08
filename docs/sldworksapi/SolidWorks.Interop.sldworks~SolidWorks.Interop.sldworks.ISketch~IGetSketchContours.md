# IGetSketchContours Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSketchContours`

Gets the sketch contours in this sketch.
Gets the sketch contours in this sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSketchContours( _
   ByVal Count As System.Integer _
) As SketchContour
```

```

Dim instance As ISketch
Dim Count As System.Integer
Dim value As SketchContour
 
value = instance.IGetSketchContours(Count)
```

```

SketchContour IGetSketchContours( 
   System.int Count
)
```

```

SketchContour^ IGetSketchContours( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of sketch contours

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [sketch contours](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [ISketch::GetSketchContourCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchContourCount.md) before calling this method to get Count.

This method works even if the sketch is suppressed.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[ISketch::GetSketchContours Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchContours.md)
