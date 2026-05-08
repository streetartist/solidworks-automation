# SetFunctionHarmonicValues Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~SetFunctionHarmonicValues`

Sets the harmonic function values for this Force feature.
Sets the harmonic function values for this Force feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetFunctionHarmonicValues( _
   ByVal Amplitude As System.Double, _
   ByVal Frequency As System.Double, _
   ByVal Average As System.Double, _
   ByVal PhaseShift As System.Double _
) As System.Boolean
```

```

Dim instance As ISimulationForceFeatureData
Dim Amplitude As System.Double
Dim Frequency As System.Double
Dim Average As System.Double
Dim PhaseShift As System.Double
Dim value As System.Boolean
 
value = instance.SetFunctionHarmonicValues(Amplitude, Frequency, Average, PhaseShift)
```

```

System.bool SetFunctionHarmonicValues( 
   System.double Amplitude,
   System.double Frequency,
   System.double Average,
   System.double PhaseShift
)
```

```

System.bool SetFunctionHarmonicValues( 
   System.double Amplitude,
   System.double Frequency,
   System.double Average,
   System.double PhaseShift
) 
```

#### Parameters

*Amplitude*
:   Amplitude of the function measured peak to peak

*Frequency*
:   Frequency of the function

*Average*
:   Average value of the function; the function oscillates about this value

*PhaseShift*
:   Phase shift for the function

#### Return Value

True if the operation succeeds, false if it fails

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulationForceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.md)  
[ISimulationForceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData_members.md)  
[ISimulationForceFeatureData::GetFunctionHarmonicValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~GetFunctionHarmonicValues.md)  
[ISimulationForceFeatureData::GetFunctionStepValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~GetFunctionStepValues.md)  
[ISimulationForceFeatureData::SetFunctionStepValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~SetFunctionStepValues.md)  
[ISimulationForceFeatureData::FunctionConstantValue Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~FunctionConstantValue.md)  
[ISimulationForceFeatureData::FunctionExpression Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~FunctionExpression.md)  
[ISimulationForceFeatureData::ForceFunctionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ForceFunctionType.md)
