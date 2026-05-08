# SetFunctionStepValues Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~SetFunctionStepValues`

Sets the step function, whose magnitude transitions smoothly from one value to another value, for this Force feature.
Sets the step function, whose magnitude transitions smoothly from one value to another value, for this Force feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetFunctionStepValues( _
   ByVal F1InitialValue As System.Double, _
   ByVal T1StartStepTime As System.Double, _
   ByVal F2InitialValue As System.Double, _
   ByVal T2EndStepTime As System.Double _
) As System.Boolean
```

```

Dim instance As ISimulationForceFeatureData
Dim F1InitialValue As System.Double
Dim T1StartStepTime As System.Double
Dim F2InitialValue As System.Double
Dim T2EndStepTime As System.Double
Dim value As System.Boolean
 
value = instance.SetFunctionStepValues(F1InitialValue, T1StartStepTime, F2InitialValue, T2EndStepTime)
```

```

System.bool SetFunctionStepValues( 
   System.double F1InitialValue,
   System.double T1StartStepTime,
   System.double F2InitialValue,
   System.double T2EndStepTime
)
```

```

System.bool SetFunctionStepValues( 
   System.double F1InitialValue,
   System.double T1StartStepTime,
   System.double F2InitialValue,
   System.double T2EndStepTime
) 
```

#### Parameters

*F1InitialValue*
:   Value of the function before the step

*T1StartStepTime*
:   Time at which the step begins

*F2InitialValue*
:   Value of the function after the step

*T2EndStepTime*
:   Time at which the step ends

#### Return Value

True if the operation succeeds, false if it fails

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulationForceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.md)  
[ISimulationForceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData_members.md)  
[ISimulationForceFeatureData::GetFunctionStepValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~GetFunctionStepValues.md)  
[ISimulationForceFeatureData::GetFunctionHarmonicValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~GetFunctionHarmonicValues.md)  
[ISimulationForceFeatureData::SetFunctionHarmonicValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~SetFunctionHarmonicValues.md)  
[ISimulationForceFeatureData::FunctionConstantValue Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~FunctionConstantValue.md)  
[ISimulationForceFeatureData::FunctionExpression Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~FunctionExpression.md)  
[ISimulationForceFeatureData::ForceFunctionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ForceFunctionType.md)
