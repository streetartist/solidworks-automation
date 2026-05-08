# ActionType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ActionType`

Gets or sets the type of action for this Force feature.
Gets or sets the type of action for this Force feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ActionType As System.Integer
```

```

Dim instance As ISimulationForceFeatureData
Dim value As System.Integer
 
instance.ActionType = value
 
value = instance.ActionType
```

```

System.int ActionType {get; set;}
```

```

property System.int ActionType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of action as defined in [swSimulationForceActionType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSimulationForceActionType_e.html)

Example

[Create Force Feature (VBA)](Create_Force_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulationForceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.md)  
[ISimulationForceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData_members.md)  
[ISimulationForceFeatureData::ActionDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ActionDirection.md)  
[ISimulationForceFeatureData::ActionLocation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ActionLocation.md)  
[ISimulationForceFeatureData::ReactionLocation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ReactionLocation.md)
