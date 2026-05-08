# Transform2 Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Transform2`

Gets or sets the component transform.
Gets or sets the component transform.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Transform2 As MathTransform
```

```

Dim instance As IComponent2
Dim value As MathTransform
 
instance.Transform2 = value
 
value = instance.Transform2
```

```

MathTransform Transform2 {get; set;}
```

```

property MathTransform^ Transform2 {
   MathTransform^ get();
   void set (    MathTransform^ value);
}
```

#### Property Value

[Component transform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md)

Remarks

This property affects the underlying model geometry and the display of the component.

You must specify the transform in relation to the root component. This also applies when there is an in-context edit in progress. The transform is still with respect to the root component of the active assembly document, not with respect to the root component of the edit target. See [IConfiguration::GetRootComponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetRootComponent.md) and [IConfiguration::IGetRootComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetRootComponent2.md).

The destination component, or any component above it in the assembly tree, is moved so that the destination component's transform is set to the desired one.

You can call [IModelDoc2::Rebuild](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Rebuild.md) with the swUpdateMates argument to rebuild the model after transforming a component. This is much faster than rebuilding all of the geometry for the model using the now obsolete IAssemblyDoc::EditRebuild.

This property lets you violate existing mate relationships. If you place a component at an invalid location based on the mate definitions, then IModelDoc2::Rebuild recalculates existing mate relationships and moves your components to the closest valid location.

After you change a component's transform, you can call [IAssemblyDoc::UpdateBox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UpdateBox.md) to avoid clipping in shaded display mode.

Example

[Align Assembly Component to Assembly Origin and Planes (VBA)](Align_Assembly_Component_to_Assembly_Origin_and_Planes_Example_VB.htm)  
[Combine Assembly Components into Part (VBA)](Combine_Assembly_Components_into_Part_Example_VB.htm)  
[Get Transforms of Assembly Components (VBA)](Get_Transforms_of_Assembly_Components_Example_VB.htm)  
[Transform Point from Component Space to Assembly Space (C#)](Transform_Point_from_Component_Space_to_Assembly_Space_Example_CSharp.htm)  
[Transform Point from Component Space to Assembly Space (VB.NET)](Transform_Point_from_Component_Space_to_Assembly_Space_Example_VBNET.htm)  
[Transform Point from Component Space to Assembly Space (VBA)](Transform_Point_from_Component_Space_to_Assembly_Space_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::GetTotalTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetTotalTransform.md)  
[IComponent2::PresentationTransform Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~PresentationTransform.md)  
[IComponent2::RemovePresentationTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~RemovePresentationTransform.md)  
[IComponent2::SetTransformAndSolve2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetTransformAndSolve2.md)  
[IComponent2::GetSpecificTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSpecificTransform.md)
