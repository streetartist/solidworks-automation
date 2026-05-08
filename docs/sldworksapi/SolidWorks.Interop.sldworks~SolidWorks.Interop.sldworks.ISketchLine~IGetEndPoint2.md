# IGetEndPoint2 Method (ISketchLine)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine~IGetEndPoint2`

Gets the sketch point for the end point of the line.
Gets the sketch point for the end point of the line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetEndPoint2() As SketchPoint
```

```

Dim instance As ISketchLine
Dim value As SketchPoint
 
value = instance.IGetEndPoint2()
```

```

SketchPoint IGetEndPoint2()
```

```

SketchPoint^ IGetEndPoint2(); 
```

#### Return Value

End [sketch point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md) or NULL if the operation fails

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.md)  
[ISketchLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine_members.md)  
[ISketchLine::GetEndPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine~GetEndPoint2.md)
