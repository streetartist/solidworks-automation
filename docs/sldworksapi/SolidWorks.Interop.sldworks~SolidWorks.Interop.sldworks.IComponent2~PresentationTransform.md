# PresentationTransform Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~PresentationTransform`

Gets or sets the component transform.
Gets or sets the component transform.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PresentationTransform As MathTransform
```

```

Dim instance As IComponent2
Dim value As MathTransform
 
instance.PresentationTransform = value
 
value = instance.PresentationTransform
```

```

MathTransform PresentationTransform {get; set;}
```

```

property MathTransform^ PresentationTransform {
   MathTransform^ get();
   void set (    MathTransform^ value);
}
```

#### Property Value

[Component transform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md)

Remarks

This property affects the graphical display; it does not affect the underlying model geometry.

This property:

- gets or sets the component transform for graphical display.
- ignores all mate and in-context relationships. Only the display of the component on the screen is affected.
- does not apply the transform to component geometry.
- does not display any changes. To display changes, call [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md).

This property's functionality is for graphical purposes only and does not affect solid models. For example, if you want to animate the explode steps for an assembly, then maintaining assembly mate and in-context relationships is not needed or desirable.

You must first enable a presentation transform by setting [IAssemblyDoc::EnablePresentation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EnablePresentation.md) to true. [IComponent2::RemovePresentationTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~RemovePresentationTransform.md) removes any transform applied by IComponent2::PresentationTransform. Set IAssemblyDoc::EnablePresentation to false after calling IComponent2::RemovePresentationTransform. After calling this method, the component is next drawn in a position consistent with its underlying geometry ([IComponent2::Transform2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Transform2.md)).

Example

[Use Presentation Transforms to Move Component (VBA)](Use_Presentation_Transforms_to_Move_Component_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::GetSpecificTransform Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSpecificTransform.md)
