# OscillatingMotor Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~OscillatingMotor`

Sets the displacement and frequency for oscillating motion for this motor feature.
Sets the displacement and frequency for oscillating motion for this motor feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub OscillatingMotor( _
   ByVal Displacement As System.Double, _
   ByVal Frequency As System.Double _
) 
```

```

Dim instance As ISimulationMotorFeatureData
Dim Displacement As System.Double
Dim Frequency As System.Double
 
instance.OscillatingMotor(Displacement, Frequency)
```

```

void OscillatingMotor( 
   System.double Displacement,
   System.double Frequency
)
```

```

void OscillatingMotor( 
   System.double Displacement,
   System.double Frequency
) 
```

#### Parameters

*Displacement*
:   Displacement in degrees

*Frequency*
:   Frequency in Hz

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulationMotorFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.md)  
[ISimulationMotorFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData_members.md)  
[ISimulationMotorFeatureData::ConstantSpeedMotor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~ConstantSpeedMotor.md)  
[ISimulationMotorFeatureData::DistanceMotor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~DistanceMotor.md)  
[ISimulationMotorFeatureData::InterpolatedMotor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~InterpolatedMotor.md)  
[ISimulationMotorFeatureData::Expression Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~Expression.md)
