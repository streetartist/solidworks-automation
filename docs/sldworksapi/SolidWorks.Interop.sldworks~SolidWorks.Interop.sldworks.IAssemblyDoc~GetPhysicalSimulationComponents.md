# GetPhysicalSimulationComponents Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetPhysicalSimulationComponents`

Obsolete. Not superseded.
Obsolete. Not superseded.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetPhysicalSimulationComponents( _
   ByVal InDuration As System.Double, _
   ByRef OutCount As System.Integer, _
   ByRef OutComponents As System.Object, _
   ByRef OutTransforms As System.Object, _
   ByRef OutStepStartTimes As System.Object, _
   ByRef OutStepDurations As System.Object, _
   ByRef OutTotalPhysSimDuration As System.Double _
) 
```

```

Dim instance As IAssemblyDoc
Dim InDuration As System.Double
Dim OutCount As System.Integer
Dim OutComponents As System.Object
Dim OutTransforms As System.Object
Dim OutStepStartTimes As System.Object
Dim OutStepDurations As System.Object
Dim OutTotalPhysSimDuration As System.Double
 
instance.GetPhysicalSimulationComponents(InDuration, OutCount, OutComponents, OutTransforms, OutStepStartTimes, OutStepDurations, OutTotalPhysSimDuration)
```

```

void GetPhysicalSimulationComponents( 
   System.double InDuration,
   out System.int OutCount,
   out System.object OutComponents,
   out System.object OutTransforms,
   out System.object OutStepStartTimes,
   out System.object OutStepDurations,
   out System.double OutTotalPhysSimDuration
)
```

```

void GetPhysicalSimulationComponents( 
   System.double InDuration,
   [Out] System.int OutCount,
   [Out] System.Object^ OutComponents,
   [Out] System.Object^ OutTransforms,
   [Out] System.Object^ OutStepStartTimes,
   [Out] System.Object^ OutStepDurations,
   [Out] System.double OutTotalPhysSimDuration
) 
```

#### Parameters

*InDuration*
:   Total elapsed time for Physical Simulation

*OutCount*
:   Size for all returned arrays

*OutComponents*
:   Array of the [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) objects

*OutTransforms*
:   Array of the [IMathTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md) objects

*OutStepStartTimes*
:   Array of doubles of size outCount; when each step in the Physical Simulation should happen

*OutStepDurations*
:   Array of doubles of size outCount; how long each step in the Physical Simulation should take

*OutTotalPhysSimDuration*
:   Total elapsed time Physical Simulation should have taken

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[ISimulation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation.md)  
[ISimulationGravityFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationGravityFeatureData.md)  
[ISimulationLinearSpringFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationLinearSpringFeatureData.md)  
[ISimulationMotorFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.md)
