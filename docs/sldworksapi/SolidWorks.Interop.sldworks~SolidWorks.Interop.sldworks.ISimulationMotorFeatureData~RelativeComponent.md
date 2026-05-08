# RelativeComponent Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~RelativeComponent`

Gets or sets a part in the assembly to which to reference motion when setting motion relative to another part in this motor feature.
Gets or sets a part in the assembly to which to reference motion when setting motion relative to another part in this motor feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property RelativeComponent As Component2
```

```

Dim instance As ISimulationMotorFeatureData
Dim value As Component2
 
instance.RelativeComponent = value
 
value = instance.RelativeComponent
```

```

Component2 RelativeComponent {get; set;}
```

```

property Component2^ RelativeComponent {
   Component2^ get();
   void set (    Component2^ value);
}
```

#### Property Value

Relative [component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)

Example

[Create Linear Motor Feature (VBA)](Create_Linear_Motor_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulationMotorFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.md)  
[ISimulationMotorFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData_members.md)  
[ISimulationMotorFeatureData::Location Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~Location.md)  
[ISimulationMotorFeatureData::LoadReferences Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~LoadReferences.md)
