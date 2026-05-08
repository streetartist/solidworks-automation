# ConstantSpeedMotor Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~ConstantSpeedMotor`

Sets the constant speed for this motor feature.
Sets the constant speed for this motor feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ConstantSpeedMotor( _
   ByVal Speed As System.Double _
) 
```

```

Dim instance As ISimulationMotorFeatureData
Dim Speed As System.Double
 
instance.ConstantSpeedMotor(Speed)
```

```

void ConstantSpeedMotor( 
   System.double Speed
)
```

```

void ConstantSpeedMotor( 
   System.double Speed
) 
```

#### Parameters

*Speed*
:   Constant speed in RPMs

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulationMotorFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.md)  
[ISimulationMotorFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData_members.md)  
[ISimulationMotorFeatureData::DistanceMotor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~DistanceMotor.md)  
[ISimulationMotorFeatureData::InterpolatedMotor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~InterpolatedMotor.md)  
[ISimulationMotorFeatureData::OscillatingMotor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~OscillatingMotor.md)  
[ISimulationMotorFeatureData::Expression Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~Expression.md)
