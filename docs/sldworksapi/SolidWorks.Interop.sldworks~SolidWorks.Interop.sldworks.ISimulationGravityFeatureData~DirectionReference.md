# DirectionReference Property (ISimulationGravityFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationGravityFeatureData~DirectionReference`

Gets or sets the direction of in which gravity moves.
Gets or sets the direction of in which gravity moves.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DirectionReference As System.Object
```

```

Dim instance As ISimulationGravityFeatureData
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

Linear edge, planar face, axis, or plane indicating the direction of gravity

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulationGravityFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationGravityFeatureData.md)  
[ISimulationGravityFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationGravityFeatureData_members.md)  
[ISimulationGravityFeatureData::ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationGravityFeatureData~ReverseDirection.md)
