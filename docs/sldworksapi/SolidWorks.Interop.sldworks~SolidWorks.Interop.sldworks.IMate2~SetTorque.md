# SetTorque Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~SetTorque`

Sets the angle and the axis of the torque to apply to this mate.
Sets the angle and the axis of the torque to apply to this mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetTorque( _
   ByVal Angle As System.Double, _
   ByVal Axis As MathVector _
) As System.Boolean
```

```

Dim instance As IMate2
Dim Angle As System.Double
Dim Axis As MathVector
Dim value As System.Boolean
 
value = instance.SetTorque(Angle, Axis)
```

```

System.bool SetTorque( 
   System.double Angle,
   MathVector Axis
)
```

```

System.bool SetTorque( 
   System.double Angle,
   MathVector^ Axis
) 
```

#### Parameters

*Angle*
:   Angle

*Axis*
:   [Axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md)

#### Return Value

True if the operation succeeds, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md)  
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.md)  
[IMate2::GetTorque Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetTorque.md)  
[IMate2::GetForce Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetForce.md)  
[IMate2::SetForce Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~SetForce.md)
