# GetForce Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetForce`

Gets the magnitude and direction of the force applied to this mate.
Gets the magnitude and direction of the force applied to this mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetForce( _
   ByRef Magnitude As System.Double _
) As MathVector
```

```

Dim instance As IMate2
Dim Magnitude As System.Double
Dim value As MathVector
 
value = instance.GetForce(Magnitude)
```

```

MathVector GetForce( 
   out System.double Magnitude
)
```

```

MathVector^ GetForce( 
   [Out] System.double Magnitude
) 
```

#### Parameters

*Magnitude*
:   Magnitude

#### Return Value

[Direction](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md)  
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.md)  
[IMate2::SetForce Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~SetForce.md)  
[IMate2::GetTorque Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetTorque.md)  
[IMate2::SetTorque Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~SetTorque.md)
