# GetTotalTransform Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetTotalTransform`

Combines the original transform of this component with the presentation transform of this component.
Combines the original transform of this component with the presentation transform of this component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTotalTransform( _
   ByVal IncludePresentationXform As System.Boolean _
) As MathTransform
```

```

Dim instance As IComponent2
Dim IncludePresentationXform As System.Boolean
Dim value As MathTransform
 
value = instance.GetTotalTransform(IncludePresentationXform)
```

```

MathTransform GetTotalTransform( 
   System.bool IncludePresentationXform
)
```

```

MathTransform^ GetTotalTransform( 
   System.bool IncludePresentationXform
) 
```

#### Parameters

*IncludePresentationXform*
:   True to combine the transforms, false to not

#### Return Value

Pointer to the [IMathTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md) object

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IAssemblyDoc::EnablePresentation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EnablePresentation.md)  
[IComponent2::PresentationTransform Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~PresentationTransform.md)  
[IComponent2::RemovePresentationTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~RemovePresentationTransform.md)  
[IComponent2::SetTransformAndSolve2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetTransformAndSolve2.md)  
[IComponent2::Transform2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Transform2.md)  
[IComponent2::GetSpecificTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSpecificTransform.md)
