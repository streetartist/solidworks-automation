# SetTransformAndSolve3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetTransformAndSolve3`

Sets the transform and solves for the mates for this component.
Sets the transform and solves for the mates for this component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetTransformAndSolve3( _
   ByVal XformIn As MathTransform, _
   ByVal ThisConfiguration As System.Boolean _
) As System.Boolean
```

```

Dim instance As IComponent2
Dim XformIn As MathTransform
Dim ThisConfiguration As System.Boolean
Dim value As System.Boolean
 
value = instance.SetTransformAndSolve3(XformIn, ThisConfiguration)
```

```

System.bool SetTransformAndSolve3( 
   MathTransform XformIn,
   System.bool ThisConfiguration
)
```

```

System.bool SetTransformAndSolve3( 
   MathTransform^ XformIn,
   System.bool ThisConfiguration
) 
```

#### Parameters

*XformIn*
:   Pointer to the [IMathTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md) object to use to set and solve

*ThisConfiguration*
:   True to transform this configuration, false to transform all configurations

#### Return Value

True if the transform was set and solved, false if not

Remarks

If making multiple calls to this method, consider using [IDragOperator::Drag](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~Drag.md), which is more efficient because it reuses the solver. However, DragOperator::Drag does not support clash detection or dynamic clearance.

The transform specified must be in relation to the root component. See [IConfiguration::GetRootComponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetRootComponent.md) or [IConfiguration::IGetRootComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetRootComponent2.md).

SOLIDWORKS moves the destination component, or any component above it in the assembly tree, so that the destination component's transform is set to the desired one. Transforming an object using this method can cause SOLIDWORKS to transform other mated or constrained objects.

After you have changed a component's transform, you can call [IAssemblyDoc::UpdateBox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UpdateBox.md) to avoid clipping in shaded display mode.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::GetTotalTransform Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetTotalTransform.md)  
[IComponent2::GetSpecificTransform Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSpecificTransform.md)  
[IComponent2::Transform2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Transform2.md)
