# ApplyTransforms Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionGroup~ApplyTransforms`

Applies the specified transforms to the components in this collision detection group.
Applies the specified transforms to the components in this collision detection group.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ApplyTransforms( _
   ByVal ComponentTransforms As System.Object _
) As System.Integer
```

```

Dim instance As ICollisionDetectionGroup
Dim ComponentTransforms As System.Object
Dim value As System.Integer
 
value = instance.ApplyTransforms(ComponentTransforms)
```

```

System.int ApplyTransforms( 
   System.object ComponentTransforms
)
```

```

System.int ApplyTransforms( 
   System.Object^ ComponentTransforms
) 
```

#### Parameters

*ComponentTransforms*
:   Array of [IMathTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md)

#### Return Value

Result code as defined in [swCollisionGroupApplyTransformErrors\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCollisionGroupApplyTransformErrors_e.html)

Example

See the [ICollisionDetectionManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICollisionDetectionGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionGroup.md)  
[ICollisionDetectionGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionGroup_members.md)
