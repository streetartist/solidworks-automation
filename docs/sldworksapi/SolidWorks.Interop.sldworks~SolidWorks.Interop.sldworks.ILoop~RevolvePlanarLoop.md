# RevolvePlanarLoop Method (ILoop)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop~RevolvePlanarLoop`

Obsolete. Superseded by ILoop2::RevolvePlanarLoop.
Obsolete. Superseded by [ILoop2::RevolvePlanarLoop](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~RevolvePlanarLoop.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RevolvePlanarLoop( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal Axisx As System.Double, _
   ByVal Axisy As System.Double, _
   ByVal Axisz As System.Double, _
   ByVal RevAngle As System.Double _
) As System.Object
```

```

Dim instance As ILoop
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim Axisx As System.Double
Dim Axisy As System.Double
Dim Axisz As System.Double
Dim RevAngle As System.Double
Dim value As System.Object
 
value = instance.RevolvePlanarLoop(X, Y, Z, Axisx, Axisy, Axisz, RevAngle)
```

```

System.object RevolvePlanarLoop( 
   System.double X,
   System.double Y,
   System.double Z,
   System.double Axisx,
   System.double Axisy,
   System.double Axisz,
   System.double RevAngle
)
```

```

System.Object^ RevolvePlanarLoop( 
   System.double X,
   System.double Y,
   System.double Z,
   System.double Axisx,
   System.double Axisy,
   System.double Axisz,
   System.double RevAngle
) 
```

#### Parameters

*X*

*Y*

*Z*

*Axisx*

*Axisy*

*Axisz*

*RevAngle*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILoop Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop.md)  
[ILoop Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop_members.md)
