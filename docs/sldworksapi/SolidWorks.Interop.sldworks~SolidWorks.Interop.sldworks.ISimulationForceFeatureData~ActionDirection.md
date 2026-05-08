# ActionDirection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ActionDirection`

Gets or sets the direction of the force.
Gets or sets the direction of the force.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ActionDirection As System.Object
```

```

Dim instance As ISimulationForceFeatureData
Dim value As System.Object
 
instance.ActionDirection = value
 
value = instance.ActionDirection
```

```

System.object ActionDirection {get; set;}
```

```

property System.Object^ ActionDirection {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Along an axis defined by an edge or a plane

Along the line-of-sight between two points

Remarks

The way you define the directions of your forces depends on which forces you are creating. If you are creating an action-only force, the force direction remains fixed with respect to some part in your model, either a moving part or the ground part. In this case, you can define the force direction using one vector defined by an edge or a plane.

If you are creating an action/reaction force, then the direction along which you want the force applied is defined by the line between two points in your model and is constantly changing throughout the simulation. In this case, you can define the force direction as the line between the two points.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulationForceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.md)  
[ISimulationForceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData_members.md)  
[ISimulationForceFeatureData::ActionLocation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ActionLocation.md)  
[ISimulationForceFeatureData::ActionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ActionType.md)  
[ISimulationForceFeatureData::ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ReverseDirection.md)  
[ISimulationForceFeatureData::ReactionLocation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ReactionLocation.md)
