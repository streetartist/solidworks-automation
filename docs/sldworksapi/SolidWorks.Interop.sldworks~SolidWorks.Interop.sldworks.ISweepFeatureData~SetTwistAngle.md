# SetTwistAngle Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~SetTwistAngle`

Sets the angle at which to twist this sweep feature.
Sets the angle at which to twist this sweep feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetTwistAngle( _
   ByVal Angle As System.Double _
) 
```

```

Dim instance As ISweepFeatureData
Dim Angle As System.Double
 
instance.SetTwistAngle(Angle)
```

```

void SetTwistAngle( 
   System.double Angle
)
```

```

void SetTwistAngle( 
   System.double Angle
) 
```

#### Parameters

*Angle*
:   Angle of twist in radians

Remarks

This method is valid only if [ISweepFeatureData::TwistControlType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~TwistControlType.md) is set to [swTwistControlType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTwistControlType_e.html).swTwistControlConstantTwistAlongPath.

In the Sweep PropertyManager, you can specify revolutions, degrees, or radians. To specify Angle, you must convert revolutions and degrees to radians:

> 1 revolution = 360 degrees = 2\*pi = 6.28319 radians

This method sets the angle of twist in radians in Direction 1 of a bidirectional sweep.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.md)  
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.md)  
[ISweepFeatureData::GetTwistAngle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetTwistAngle.md)  
[ISweepFeatureData::D1ReverseTwistDir Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~D1ReverseTwistDir.md)  
[ISweepFeatureData::SetD2TwistAngle Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~SetD2TwistAngle.md)
