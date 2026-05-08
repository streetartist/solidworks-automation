# CreateParabola Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateParabola`

Creates a parabola in the active sketch.
Creates a parabola in the active sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateParabola( _
   ByVal XFocus As System.Double, _
   ByVal YFocus As System.Double, _
   ByVal ZFocus As System.Double, _
   ByVal XApex As System.Double, _
   ByVal YApex As System.Double, _
   ByVal ZApex As System.Double, _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal Z1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double, _
   ByVal Z2 As System.Double _
) As SketchSegment
```

```

Dim instance As ISketchManager
Dim XFocus As System.Double
Dim YFocus As System.Double
Dim ZFocus As System.Double
Dim XApex As System.Double
Dim YApex As System.Double
Dim ZApex As System.Double
Dim X1 As System.Double
Dim Y1 As System.Double
Dim Z1 As System.Double
Dim X2 As System.Double
Dim Y2 As System.Double
Dim Z2 As System.Double
Dim value As SketchSegment
 
value = instance.CreateParabola(XFocus, YFocus, ZFocus, XApex, YApex, ZApex, X1, Y1, Z1, X2, Y2, Z2)
```

```

SketchSegment CreateParabola( 
   System.double XFocus,
   System.double YFocus,
   System.double ZFocus,
   System.double XApex,
   System.double YApex,
   System.double ZApex,
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2
)
```

```

SketchSegment^ CreateParabola( 
   System.double XFocus,
   System.double YFocus,
   System.double ZFocus,
   System.double XApex,
   System.double YApex,
   System.double ZApex,
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2
) 
```

#### Parameters

*XFocus*
:   X coordinate for the focus

*YFocus*
:   Y coordinate for the focus

*ZFocus*
:   Z coordinate for the focus

*XApex*
:   X coordinate for the apex

*YApex*
:   Y coordinate for the apex

*ZApex*
:   Z coordinate for the apex

*X1*
:   X coordinate for the start point

*Y1*
:   Y coordinate for the start point

*Z1*
:   Z coordinate for the start point

*X2*
:   X coordinate for the end point

*Y2*
:   Y coordinate for the end point

*Z2*
:   Z coordinate for the end point

#### Return Value

[Sketch segment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md) for the parabola

Example

[Create Parabola (VBA)](Create_Parabola_Example_VB.htm)  
[Create Parabola (VB.NET)](Create_Parabola_Example_VBNET.htm)  
[Create Parabola (C#)](Create_Parabola_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)  
[ISketchManager::CreateConic Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateConic.md)
