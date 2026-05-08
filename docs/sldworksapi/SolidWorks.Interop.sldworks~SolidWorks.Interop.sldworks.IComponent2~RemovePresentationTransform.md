# RemovePresentationTransform Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~RemovePresentationTransform`

Removes the presentation transform from this component.
Removes the presentation transform from this component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub RemovePresentationTransform() 
```

```

Dim instance As IComponent2
 
instance.RemovePresentationTransform()
```

```

void RemovePresentationTransform()
```

```

void RemovePresentationTransform(); 
```

Remarks

Set [IAssemblyDoc::EnablePresentation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EnablePresentation.md) to false after a user is finished with presentation transforms and has called IComponent2::RemovePresentationTransform, which removes any transform applied by [IComponent::PresentationTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~PresentationTransform.md).

After calling IComponent2::RemovePresentationTransfrom, the component is next drawn in a position consistent with its underlying geometry ([IComponent2::Transform2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Transform2.md)).

Example

[Use Presentation Transforms to Move Component (VBA)](Use_Presentation_Transforms_to_Move_Component_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IAssemblyDoc::EnablePresentation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EnablePresentation.md)  
[IComponent2::GetTotalTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetTotalTransform.md)  
[IComponent2::PresentationTransform Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~PresentationTransform.md)  
[IComponent2::Transform2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Transform2.md)
