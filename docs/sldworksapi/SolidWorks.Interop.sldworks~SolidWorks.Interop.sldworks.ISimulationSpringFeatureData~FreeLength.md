# FreeLength Property (ISimulationSpringFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~FreeLength`

Gets or sets the free length (i.e., length to stretch or compress the spring) for the functional expression for this simulation spring feature.
Gets or sets the free length (i.e., length to stretch or compress the spring) for the functional expression for this simulation spring feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FreeLength As System.Double
```

```

Dim instance As ISimulationSpringFeatureData
Dim value As System.Double
 
instance.FreeLength = value
 
value = instance.FreeLength
```

```

System.double FreeLength {get; set;}
```

```

property System.double FreeLength {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Free length

Remarks

The initial distance is the distance between the parts as currently displayed in the graphics area. Call [ISimulationSpringFeatureData::UpdateToModelChanges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~UpdateToModelChanges.md) to have the free length dynamically update to model changes while the PropertyManager page is open.

The spring does not exert any force when its length is equal to its free length.

Example

[Add Spring to Motion Study (C#)](Add_Spring_to_Motion_Study_Example_CSharp.htm)  
[Add Spring to Motion Study (VB.NET)](Add_Spring_to_Motion_Study_Example_VBNET.htm)  
[Add Spring to Motion Study (VBA)](Add_Spring_to_Motion_Study_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulationSpringFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData.md)  
[ISimulationSpringFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData_members.md)  
[ISimulationSpringFeatureData::ExponentOfDamperForceExpression Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~ExponentOfDamperForceExpression.md)  
[ISimulationSpringFeatureData::ExponentOfSpringForceExpression Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~ExponentOfSpringForceExpression.md)  
[ISimulationSpringFeatureData::FreeAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~FreeAngle.md)  
[ISimulationSpringFeatureData::SpringConstant Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~SpringConstant.md)
