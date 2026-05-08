# SpringConstant Property (ISimulationSpringFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~SpringConstant`

Gets or sets the strength of this simulation spring feature.
Gets or sets the strength of this simulation spring feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SpringConstant As System.Double
```

```

Dim instance As ISimulationSpringFeatureData
Dim value As System.Double
 
instance.SpringConstant = value
 
value = instance.SpringConstant
```

```

System.double SpringConstant {get; set;}
```

```

property System.double SpringConstant {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Strength

Remarks

Springs apply a force to a component. A spring with a higher spring constant moves a component faster than a spring with a lower spring constant. A component with a smaller mass moves faster than a component with a larger mass when acted upon by an equal strength spring.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulationSpringFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData.md)  
[ISimulationSpringFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData_members.md)  
[ISimulationSpringFeatureData::ExponentOfDamperForceExpression Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~ExponentOfDamperForceExpression.md)  
[ISimulationSpringFeatureData::ExponentOfSpringForceExpression Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~ExponentOfSpringForceExpression.md)  
[ISimulationSpringFeatureData::FreeAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~FreeAngle.md)  
[ISimulationSpringFeatureData::FreeLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~FreeLength.md)
