# PerimeterCircle Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~PerimeterCircle`

Draws a 3-point perimeter arc.
Draws a 3-point perimeter arc.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function PerimeterCircle( _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double, _
   ByVal X3 As System.Double, _
   ByVal Y3 As System.Double _
) As System.Object
```

```

Dim instance As ISketchManager
Dim X1 As System.Double
Dim Y1 As System.Double
Dim X2 As System.Double
Dim Y2 As System.Double
Dim X3 As System.Double
Dim Y3 As System.Double
Dim value As System.Object
 
value = instance.PerimeterCircle(X1, Y1, X2, Y2, X3, Y3)
```

```

System.object PerimeterCircle( 
   System.double X1,
   System.double Y1,
   System.double X2,
   System.double Y2,
   System.double X3,
   System.double Y3
)
```

```

System.Object^ PerimeterCircle( 
   System.double X1,
   System.double Y1,
   System.double X2,
   System.double Y2,
   System.double X3,
   System.double Y3
) 
```

#### Parameters

*X1*
:   coordinate for first point

*Y1*
:   y coordinate for first point

*X2*
:   x coordinate for second point

*Y2*
:   y coordinate for second point

*X3*
:   x coordinate for third point

*Y3*
:   y coordinate for third point

#### Return Value

[3-point perimeter arc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)
