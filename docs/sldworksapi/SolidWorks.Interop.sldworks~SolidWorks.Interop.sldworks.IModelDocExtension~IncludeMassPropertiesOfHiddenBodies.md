# IncludeMassPropertiesOfHiddenBodies Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IncludeMassPropertiesOfHiddenBodies`

Gets or sets whether to include the mass properties of hidden components in the assembly.
Gets or sets whether to include the mass properties of hidden components in the assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IncludeMassPropertiesOfHiddenBodies As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim value As System.Boolean
 
instance.IncludeMassPropertiesOfHiddenBodies = value
 
value = instance.IncludeMassPropertiesOfHiddenBodies
```

```

System.bool IncludeMassPropertiesOfHiddenBodies {get; set;}
```

```

property System.bool IncludeMassPropertiesOfHiddenBodies {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to include the mass properties of hidden components in the assembly, false to not

Example

[Get Mass Properties of Visible and Hidden Components (C#)](Get_Mass_Properties_of_Visible_and_Hidden_Components_Example_CSharp.htm)  
[Get Mass Properties of Visible and Hidden Components (VB.NET)](Get_Mass_Properties_of_Visible_and_Hidden_Components_Example_VBNET.htm)  
[Get Mass Properties of Visible and Hidden Components (VBA)](Get_Mass_Properties_of_Visible_and_Hidden_Components_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IAssemblyDoc::HasUnloadedComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~HasUnloadedComponents.md)  
[IAssemblyDoc::HideComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~HideComponent.md)  
[IAssemblyDoc::ISetComponentVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ISetComponentVisibility.md)  
[IAssemblyDoc::SetComponentVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetComponentVisibility.md)  
[IComponent2::HasUnloadedComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~HasUnloadedComponents.md)  
[IComponent2::IsHidden Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsHidden.md)  
[IModelDoc2::HideComponent2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~HideComponent2.md)  
[IModelDocExtension::CreateMassProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateMassProperty.md)
