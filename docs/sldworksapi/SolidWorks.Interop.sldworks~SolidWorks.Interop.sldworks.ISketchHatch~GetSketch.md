# GetSketch Method (ISketchHatch)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~GetSketch`

Gets the sketch }}-->}}-->for the current sketch hatch.
Gets the sketch for the current sketch hatch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSketch() As Sketch
```

```

Dim instance As ISketchHatch
Dim value As Sketch
 
value = instance.GetSketch()
```

```

Sketch GetSketch()
```

```

Sketch^ GetSketch(); 
```

#### Return Value

[Sketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)

Remarks

You can use the [ISketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md) interface for extracting information about geometry in the sketch.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.md)  
[ISketchHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch_members.md)
