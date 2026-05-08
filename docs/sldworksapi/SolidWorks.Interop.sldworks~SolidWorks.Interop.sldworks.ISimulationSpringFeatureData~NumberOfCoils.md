# NumberOfCoils Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~NumberOfCoils`

Gets or sets the number of coils in this simulation spring feature.
Gets or sets the number of coils in this simulation spring feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property NumberOfCoils As System.Integer
```

```

Dim instance As ISimulationSpringFeatureData
Dim value As System.Integer
 
instance.NumberOfCoils = value
 
value = instance.NumberOfCoils
```

```

System.int NumberOfCoils {get; set;}
```

```

property System.int NumberOfCoils {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Number of coils

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
[ISimulationSpringFeatureData::CoilDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~CoilDiameter.md)  
[ISimulationSpringFeatureData::WireDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~WireDiameter.md)
