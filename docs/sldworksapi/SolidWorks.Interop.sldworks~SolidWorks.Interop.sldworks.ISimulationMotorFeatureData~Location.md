# Location Property (ISimulationMotorFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~Location`

Select a face, vertex, or edge on the assembly for the reference origin when setting motion relative to another part.
Select a face, vertex, or edge on the assembly for the reference origin when setting motion relative to another part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Location As System.Object
```

```

Dim instance As ISimulationMotorFeatureData
Dim value As System.Object
 
instance.Location = value
 
value = instance.Location
```

```

System.object Location {get; set;}
```

```

property System.Object^ Location {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

[Face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), [vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md), or [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

Example

[Create Linear Motor Feature (VBA)](Create_Linear_Motor_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulationMotorFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.md)  
[ISimulationMotorFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData_members.md)  
[ISimulationMotorFeatureData::RelativeComponent Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~RelativeComponent.md)  
[ISimulationMotorFeatureData::LoadReferances Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~LoadReferences.md)
