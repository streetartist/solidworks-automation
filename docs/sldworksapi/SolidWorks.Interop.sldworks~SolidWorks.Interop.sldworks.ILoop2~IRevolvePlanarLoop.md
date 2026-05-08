# IRevolvePlanarLoop Method (ILoop2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IRevolvePlanarLoop`

Creates a body by revolving a planar loop around an axis.
Creates a body by revolving a planar loop around an axis.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IRevolvePlanarLoop( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal Axisx As System.Double, _
   ByVal Axisy As System.Double, _
   ByVal Axisz As System.Double, _
   ByVal RevAngle As System.Double, _
   ByRef StopFacesOut As Face2 _
) As Body2
```

```

Dim instance As ILoop2
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim Axisx As System.Double
Dim Axisy As System.Double
Dim Axisz As System.Double
Dim RevAngle As System.Double
Dim StopFacesOut As Face2
Dim value As Body2
 
value = instance.IRevolvePlanarLoop(X, Y, Z, Axisx, Axisy, Axisz, RevAngle, StopFacesOut)
```

```

Body2 IRevolvePlanarLoop( 
   System.double X,
   System.double Y,
   System.double Z,
   System.double Axisx,
   System.double Axisy,
   System.double Axisz,
   System.double RevAngle,
   out Face2 StopFacesOut
)
```

```

Body2^ IRevolvePlanarLoop( 
   System.double X,
   System.double Y,
   System.double Z,
   System.double Axisx,
   System.double Axisy,
   System.double Axisz,
   System.double RevAngle,
   [Out] Face2^ StopFacesOut
) 
```

#### Parameters

*X*
:   x coordinate of the axis point

*Y*
:   y coordinate of the axis point

*Z*
:   z coordinate of the axis point

*Axisx*
:   Direction along x

*Axisy*
:   Direction along y

*Axisz*
:   Direction along z

*RevAngle*
:   Angle of revolution in radians

*StopFacesOut*
:   Array of two stop [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

#### Return Value

New [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILoop2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.md)  
[ILoop2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2_members.md)  
[ILoop2::RevolvePlanarLoop Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~RevolvePlanarLoop.md)
