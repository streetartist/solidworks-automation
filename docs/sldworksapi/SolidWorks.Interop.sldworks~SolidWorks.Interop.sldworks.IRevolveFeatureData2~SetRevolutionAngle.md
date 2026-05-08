# SetRevolutionAngle Method (IRevolveFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~SetRevolutionAngle`

Sets the angle of the revolve feature in Direction 1 or Direction 2.
Sets the angle of the revolve feature in Direction 1 or Direction 2.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetRevolutionAngle( _
   ByVal Forward As System.Boolean, _
   ByVal Angle As System.Double _
) 
```

```

Dim instance As IRevolveFeatureData2
Dim Forward As System.Boolean
Dim Angle As System.Double
 
instance.SetRevolutionAngle(Forward, Angle)
```

```

void SetRevolutionAngle( 
   System.bool Forward,
   System.double Angle
)
```

```

void SetRevolutionAngle( 
   System.bool Forward,
   System.double Angle
) 
```

#### Parameters

*Forward*
:   True sets the angle in Direction 1, false sets the angle in Direction 2

*Angle*
:   Angle of revolution

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRevolveFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.md)  
[IRevolveFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2_members.md)  
[IRevolveFeatureData2::GetRevolutionAngle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~GetRevolutionAngle.md)  
[IRevolveFeatureData2::ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~ReverseDirection.md)
