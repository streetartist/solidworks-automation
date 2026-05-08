# CollisionDetectionEnabled Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~CollisionDetectionEnabled`

Gets or sets the collision detection setting.
Gets or sets the collision detection setting.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CollisionDetectionEnabled As System.Boolean
```

```

Dim instance As IDragOperator
Dim value As System.Boolean
 
instance.CollisionDetectionEnabled = value
 
value = instance.CollisionDetectionEnabled
```

```

System.bool CollisionDetectionEnabled {get; set;}
```

```

property System.bool CollisionDetectionEnabled {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if collision detection is enabled, false if it is disabled

Example

[Rotate Assembly Component on Axis Using IDragOperator::Drag (VBA)](Rotate_Assembly_Component_on_Axis_Example_VB.htm)  
[Rotate Assembly Component on Axis Using IDragOperator::Drag (VB.NET)](Rotate_Assembly_Component_on_Axis_Example_VBNET.htm)  
[Rotate Assembly Component on Axis Using IDragOperator::Drag (C#)](Rotate_Assembly_Component_on_Axis_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.md)  
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.md)  
[IDragOperator::CollisionDetection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~CollisionDetection.md)  
[IDragOperator:Drag Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~Drag.md)  
[IDragOperator:DragAsUI Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~DragAsUI.md)  
[IDragOperator:DynamicClearanceEnabled Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~DynamicClearanceEnabled.md)  
[IDragOperator::ICollisionDetection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~ICollisionDetection.md)
