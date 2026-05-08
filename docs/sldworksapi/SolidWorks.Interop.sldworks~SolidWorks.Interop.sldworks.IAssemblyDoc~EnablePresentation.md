# EnablePresentation Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EnablePresentation`

Gets or sets whether the assembly is in presentation mode.
Gets or sets whether the assembly is in presentation mode.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EnablePresentation As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim value As System.Boolean
 
instance.EnablePresentation = value
 
value = instance.EnablePresentation
```

```

System.bool EnablePresentation {get; set;}
```

```

property System.bool EnablePresentation {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True enables presentation mode, false disables it

Remarks

Call this property before calling [IComponent2::PresentationTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~PresentationTransform.md) because presentation transforms are effective only in this mode. This property prohibits reconfiguring the FeatureManager design tree when SOLIDWORKS is using the presentation transforms. This property also prohibits selections in the model view.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IComponent2::GetTotalTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetTotalTransform.md)  
[IComponent2::RemovePresentationTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~RemovePresentationTransform.md)  
[IComponent2::Transform2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Transform2.md)
