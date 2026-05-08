# DynamicClearanceEnabled Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~DynamicClearanceEnabled`

Gets or sets the dynamic clearance setting.
Gets or sets the dynamic clearance setting.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DynamicClearanceEnabled As System.Boolean
```

```

Dim instance As IDragOperator
Dim value As System.Boolean
 
instance.DynamicClearanceEnabled = value
 
value = instance.DynamicClearanceEnabled
```

```

System.bool DynamicClearanceEnabled {get; set;}
```

```

property System.bool DynamicClearanceEnabled {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True enables the dynamic clearance option, false disables it

Example

[Rotate Assembly Component on Axis Using IDragOperator::Drag (VBA)](Rotate_Assembly_Component_on_Axis_Example_VB.htm)  
[Rotate Assembly Component on Axis Using IDragOperator::Drag (VB.NET)](Rotate_Assembly_Component_on_Axis_Example_VBNET.htm)  
[Rotate Assembly Component on Axis Using IDragOperator::Drag (C#)](Rotate_Assembly_Component_on_Axis_Example_CSharp.htm)  
[Rotate Assembly Component on Axis Using IDragOperator::DragAsUI (VBA)](Rotate_Assembly_Component_on_Axis_Example2_VB.htm)  
[Rotate Assembly Component on Axis Using IDragOperator::DragAsUI (VB.NET)](Rotate_Assembly_Component_on_Axis_Example2_VBNET.htm)  
[Rotate Assembly Component on Axis Using IDragOperator::DragAsUI (C#)](Rotate_Assembly_Component_on_Axis_Example2_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.md)  
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.md)  
[IDragOperator::AddDynamicClearance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~AddDynamicClearance.md)  
[IDragOperator::CollisionDetection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~CollisionDetection.md)  
[IDragOperator::Drag Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~Drag.md)  
[IDragOperator::DragAsUI Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~DragAsUI.md)  
[IDragOperator::IDrag Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~IDrag.md)  
[IDragOperator::IAddDynamicClearance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~IAddDynamicClearance.md)
