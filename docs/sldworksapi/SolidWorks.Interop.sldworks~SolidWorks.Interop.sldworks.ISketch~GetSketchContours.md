# GetSketchContours Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchContours`

Gets the sketch contours in this sketch.
Gets the sketch contours in this sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSketchContours() As System.Object
```

```

Dim instance As ISketch
Dim value As System.Object
 
value = instance.GetSketchContours()
```

```

System.object GetSketchContours()
```

```

System.Object^ GetSketchContours(); 
```

#### Return Value

Array of [sketch contours](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour.md)

Remarks

This method works even if the sketch is suppressed.

Example

[Get Sketch Contours (VBA)](Get_Sketch_Contours_Example_VB.htm)  
[Get Corresponding Objects in Assembly Component (C#)](Get_Corresponding_Objects_in_Assembly_Component_Example_CSharp.htm)  
[Get Corresponding Objects in Assembly Component (VB.NET)](Get_Corresponding_Objects_in_Assembly_Component_Example_VBNET.htm)  
[Get Corresponding Objects in Assembly Component (VBA)](Get_Corresponding_Objects_in_Assembly_Component_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[ISketch::GetSketchContourCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchContourCount.md)  
[ISketch::IGetSketchContours Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSketchContours.md)
