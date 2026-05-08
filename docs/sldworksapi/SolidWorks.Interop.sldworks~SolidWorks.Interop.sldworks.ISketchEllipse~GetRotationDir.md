# GetRotationDir Method (ISketchEllipse)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse~GetRotationDir`

Gets the rotation direction for this sketch ellipse segment.
Gets the rotation direction for this sketch ellipse segment.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetRotationDir() As System.Integer
```

```

Dim instance As ISketchEllipse
Dim value As System.Integer
 
value = instance.GetRotationDir()
```

```

System.int GetRotationDir()
```

```

System.int GetRotationDir(); 
```

#### Return Value

Rotation direction (counterclockwise = 1, clockwise = -1)

Remarks

This method determines the direction (counterclockwise or clockwise) that the sketch entity proceeds around the ellipse, beginning at its start point and ending at its ending point if the sketch entity is not a complete ellipse.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchEllipse Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse.md)  
[ISketchEllipse Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse_members.md)
