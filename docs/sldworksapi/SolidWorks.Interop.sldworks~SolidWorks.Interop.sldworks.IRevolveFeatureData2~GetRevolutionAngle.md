# GetRevolutionAngle Method (IRevolveFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~GetRevolutionAngle`

Gets the angle of the revolve feature in Direction 1 or Direction 2.
Gets the angle of the revolve feature in Direction 1 or Direction 2.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetRevolutionAngle( _
   ByVal Forward As System.Boolean _
) As System.Double
```

```

Dim instance As IRevolveFeatureData2
Dim Forward As System.Boolean
Dim value As System.Double
 
value = instance.GetRevolutionAngle(Forward)
```

```

System.double GetRevolutionAngle( 
   System.bool Forward
)
```

```

System.double GetRevolutionAngle( 
   System.bool Forward
) 
```

#### Parameters

*Forward*
:   True gets the angle in Direction 1, false gets the angle in Direction 2

#### Return Value

Angle of revolution

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRevolveFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.md)  
[IRevolveFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2_members.md)  
[IRevolveFeatureData2::SetRevolutionAngle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~SetRevolutionAngle.md)  
[IRevolveFeatureData2::ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~ReverseDirection.md)
