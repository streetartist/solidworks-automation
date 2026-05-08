# Velocity Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~Velocity`

Gets or sets the speed of the motor if no other force acts on it.
Gets or sets the speed of the motor if no other force acts on it.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Velocity As System.Double
```

```

Dim instance As ISimulationMotorFeatureData
Dim value As System.Double
 
instance.Velocity = value
 
value = instance.Velocity
```

```

System.double Velocity {get; set;}
```

```

property System.double Velocity {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Speed of the motor

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulationMotorFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.md)  
[ISimulationMotorFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData_members.md)
