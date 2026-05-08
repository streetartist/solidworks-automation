# MotorType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~MotorType`

Gets the type of motor for this motor feature.
Gets the type of motor for this motor feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property MotorType As System.Integer
```

```

Dim instance As ISimulationMotorFeatureData
Dim value As System.Integer
 
value = instance.MotorType
```

```

System.int MotorType {get;}
```

```

property System.int MotorType {
   System.int get();
}
```

#### Property Value

Type of motor as defined in [swSimulationMotorType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSimulationMotorType_e.html)

Example

[Create Linear Motor Feature (VBA)](Create_Linear_Motor_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulationMotorFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.md)  
[ISimulationMotorFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData_members.md)
