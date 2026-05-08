# ActionLocation Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ActionLocation`

Gets or sets the location at which to apply the force for an action-only force.
Gets or sets the location at which to apply the force for an action-only force.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ActionLocation As System.Object
```

```

Dim instance As ISimulationForceFeatureData
Dim value As System.Object
 
instance.ActionLocation = value
 
value = instance.ActionLocation
```

```

System.object ActionLocation {get; set;}
```

```

property System.Object^ ActionLocation {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Vertex, circular edge, or linear edge to define the points at which the moment is applied

Example

[Create Force Feature (VBA)](Create_Force_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulationForceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.md)  
[ISimulationForceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData_members.md)  
[ISimulationForceFeatureData::ActionDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ActionDirection.md)  
[ISimulationForceFeatureData::ActionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ActionType.md)  
[ISimulationForceFeatureData::ReactionLocation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ReactionLocation.md)
