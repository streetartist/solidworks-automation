# GetTorque Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetTorque`

Gets the angle and the axis of the torque applied to this mate.
Gets the angle and the axis of the torque applied to this mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTorque( _
   ByRef Angle As System.Double _
) As MathVector
```

```

Dim instance As IMate2
Dim Angle As System.Double
Dim value As MathVector
 
value = instance.GetTorque(Angle)
```

```

MathVector GetTorque( 
   out System.double Angle
)
```

```

MathVector^ GetTorque( 
   [Out] System.double Angle
) 
```

#### Parameters

*Angle*
:   Angle

#### Return Value

[Axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md)  
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.md)  
[IMate2::SetTorque Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~SetTorque.md)  
[IMate2::GetForce Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetForce.md)  
[IMate2::SetForce Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~SetForce.md)
