# ReactionLocation Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ReactionLocation`

Gets or sets the location at which to apply the force for an action/reaction force.
Gets or sets the location at which to apply the force for an action/reaction force.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReactionLocation As System.Object
```

```

Dim instance As ISimulationForceFeatureData
Dim value As System.Object
 
instance.ReactionLocation = value
 
value = instance.ReactionLocation
```

```

System.object ReactionLocation {get; set;}
```

```

property System.Object^ ReactionLocation {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Vertex, circle/sphere/torus center, or edge midpoint

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulationForceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.md)  
[ISimulationForceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData_members.md)  
[ISimulationForceFeatureData::ActionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ActionType.md)  
[ISimulationForceFeatureData::ActionDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ActionDirection.md)  
[ISimulationForceFeatureData::ActionLocation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ActionLocation.md)
