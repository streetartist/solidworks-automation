# DirectionReference Property (ISimulationMotorFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~DirectionReference`

Gets or sets the direction in which the motor moves.
Gets or sets the direction in which the motor moves.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DirectionReference As System.Object
```

```

Dim instance As ISimulationMotorFeatureData
Dim value As System.Object
 
instance.DirectionReference = value
 
value = instance.DirectionReference
```

```

System.object DirectionReference {get; set;}
```

```

property System.Object^ DirectionReference {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Circular edge; a planar, cylindrical, or conical face; an axis; or a plane indicating the direction to move the motor

Example

[Create Linear Motor Feature (VBA)](Create_Linear_Motor_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulationMotorFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.md)  
[ISimulationMotorFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData_members.md)  
[ISimulationMotorFeatureData::ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~ReverseDirection.md)
