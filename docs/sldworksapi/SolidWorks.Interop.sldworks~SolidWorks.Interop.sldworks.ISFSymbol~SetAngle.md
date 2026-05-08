# SetAngle Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~SetAngle`

Sets the angle for this surface finish symbol.
Sets the angle for this surface finish symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetAngle( _
   ByVal Angle As System.Double _
) As System.Boolean
```

```

Dim instance As ISFSymbol
Dim Angle As System.Double
Dim value As System.Boolean
 
value = instance.SetAngle(Angle)
```

```

System.bool SetAngle( 
   System.double Angle
)
```

```

System.bool SetAngle( 
   System.double Angle
) 
```

#### Parameters

*Angle*
:   Angle in radians

#### Return Value

True if the angle is set, false if it is not

Remarks

This method automatically sets the orientation to swSFOrientation\_UserDefined. See [ISFSymbol::Orientation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~Orientation.md) for details.

Use [ISFSymbol::GetAngle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetAngle.md) to get the angle of the symbol.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.md)  
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.md)
