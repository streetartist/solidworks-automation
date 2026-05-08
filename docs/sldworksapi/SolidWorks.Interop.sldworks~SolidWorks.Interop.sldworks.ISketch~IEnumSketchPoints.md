# IEnumSketchPoints Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IEnumSketchPoints`

Gets the sketch points enumeration in this sketch.
Gets the sketch points enumeration in this sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IEnumSketchPoints() As EnumSketchPoints
```

```

Dim instance As ISketch
Dim value As EnumSketchPoints
 
value = instance.IEnumSketchPoints()
```

```

EnumSketchPoints IEnumSketchPoints()
```

```

EnumSketchPoints^ IEnumSketchPoints(); 
```

#### Return Value

[Sketch points enumeration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchPoints.md)

Example

[Select All Sketch Segments (C++)](Select_All_Sketch_Segments_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[ISketch::GetSketchPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchPoints2.md)  
[ISketch::GetSketchPointsCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchPointsCount2.md)  
[ISketch::GetUserPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetUserPoints2.md)  
[ISketch::GetUserPointsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetUserPointsCount.md)  
[ISketch::IGetUserPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetUserPoints2.md)
