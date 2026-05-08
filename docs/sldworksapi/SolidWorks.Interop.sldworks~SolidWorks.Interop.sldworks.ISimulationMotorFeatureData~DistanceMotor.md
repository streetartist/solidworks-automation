# DistanceMotor Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~DistanceMotor`

Sets the distance and time for which to operate this motor feature.
Sets the distance and time for which to operate this motor feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub DistanceMotor( _
   ByVal Displacement As System.Double, _
   ByVal StartTime As System.Double, _
   ByVal Duration As System.Double _
) 
```

```

Dim instance As ISimulationMotorFeatureData
Dim Displacement As System.Double
Dim StartTime As System.Double
Dim Duration As System.Double
 
instance.DistanceMotor(Displacement, StartTime, Duration)
```

```

void DistanceMotor( 
   System.double Displacement,
   System.double StartTime,
   System.double Duration
)
```

```

void DistanceMotor( 
   System.double Displacement,
   System.double StartTime,
   System.double Duration
) 
```

#### Parameters

*Displacement*
:   Displacement in degrees

*StartTime*
:   Start time in seconds

*Duration*
:   Duration in seconds

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulationMotorFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.md)  
[ISimulationMotorFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData_members.md)  
[ISimulationMotorFeatureData::ConstantSpeedMotor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~ConstantSpeedMotor.md)  
[ISimulationMotorFeatureData::InterpolatedMotor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~InterpolatedMotor.md)  
[ISimulationMotorFeatureData::OscillatingMotor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~OscillatingMotor.md)  
[ISimulationMotorFeatureData::Expression Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~Expression.md)
