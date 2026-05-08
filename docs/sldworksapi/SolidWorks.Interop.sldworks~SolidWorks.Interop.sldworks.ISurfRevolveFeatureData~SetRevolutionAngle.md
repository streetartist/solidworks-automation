# SetRevolutionAngle Method (ISurfRevolveFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfRevolveFeatureData~SetRevolutionAngle`

Sets the angle for this surface revolve feature in Direction 1 or Direction 2.
Sets the angle for this surface revolve feature in Direction 1 or Direction 2.

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

Dim instance As ISurfRevolveFeatureData
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
:   True sets the angle in Direction 1, false sets the angle in Direction 2

*Angle*
:   Angle of the revolution

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfRevolveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfRevolveFeatureData.md)  
[ISurfRevolveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfRevolveFeatureData_members.md)  
[ISurfRevolveFeatureData::GetRevolutionAngle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfRevolveFeatureData~GetRevolutionAngle.md)
