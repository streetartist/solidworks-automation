# SetForce Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~SetForce`

Sets the magnitude and direction of the force to apply to this mate.
Sets the magnitude and direction of the force to apply to this mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetForce( _
   ByVal Magnitude As System.Double, _
   ByVal Direction As MathVector _
) As System.Boolean
```

```

Dim instance As IMate2
Dim Magnitude As System.Double
Dim Direction As MathVector
Dim value As System.Boolean
 
value = instance.SetForce(Magnitude, Direction)
```

```

System.bool SetForce( 
   System.double Magnitude,
   MathVector Direction
)
```

```

System.bool SetForce( 
   System.double Magnitude,
   MathVector^ Direction
) 
```

#### Parameters

*Magnitude*
:   Magnitude

*Direction*
:   [Direction](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md)

#### Return Value

True if the operation succeeds, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md)  
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.md)  
[IMate2::GetForce Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetForce.md)  
[IMate2::GetTorque Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetTorque.md)  
[IMate2::SetTorque Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~SetTorque.md)
