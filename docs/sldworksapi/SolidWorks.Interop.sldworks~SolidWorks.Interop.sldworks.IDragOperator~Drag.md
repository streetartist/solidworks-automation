# Drag Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~Drag`

Sets the transform matrix for this drag operation.
Sets the transform matrix for this drag operation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Drag( _
   ByVal PXform As System.Object _
) As System.Boolean
```

```

Dim instance As IDragOperator
Dim PXform As System.Object
Dim value As System.Boolean
 
value = instance.Drag(PXform)
```

```

System.bool Drag( 
   System.object PXform
)
```

```

System.bool Drag( 
   System.Object^ PXform
) 
```

#### Parameters

*PXform*
:   Math transform that specifies the desired motion for this step

#### Return Value

True if the move was successful, false if not (see **Remarks**)

Remarks

This method is more precise than the [IDragOperator::DragAsUI](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~DragAsUI.md) method. IDragOperator::DragAsUI is more like an interactive drag operation performed in the SOLIDWORKS 2001Plus software and it may give better graphics performance than IDragOperator::Drag.

You will see an improvement in performance when this method is used in the default state. If [collision detection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~CollisionDetectionEnabled.md) or [clearance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~DynamicClearanceEnabled.md) is enabled, then the original mode is used. This method is more efficient than making multiple calls to [IComponent2::SetTransformAndSolve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetTransformAndSolve2.md) because this method reuses the solver.

Use [IDragOperator::UseAbsoluteTransforms](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~UseAbsoluteTransform.md) to set the transforms type to absolute or relative.

If the desired orientation set by this method was not honored and remedial action occurred, then the [IDragOperation::DragCorrected](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~DragCorrected.md) property is set.

This method returns false if the drag cannot be performed. This typically occurs because of a collision.

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
[IDragOperator::CollisionDetectionEnabled Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~CollisionDetectionEnabled.md)  
[IDragOperator::DragAsUI Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~DragAsUI.md)  
[IDragOperator::DynamicClearanceEnabled Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~DynamicClearanceEnabled.md)  
[IDragOperator::IDrag Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~IDrag.md)  
[IDragOperator::UseAbsoluteTransform Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~UseAbsoluteTransform.md)
