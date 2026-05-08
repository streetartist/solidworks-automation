# UseDocumentDefaults Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~UseDocumentDefaults`

Gets or sets whether to use the document default settings for the component's line fonts.
Gets or sets whether to use the document default settings for the component's line fonts.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseDocumentDefaults As System.Boolean
```

```

Dim instance As IDrawingComponent
Dim value As System.Boolean
 
instance.UseDocumentDefaults = value
 
value = instance.UseDocumentDefaults
```

```

System.bool UseDocumentDefaults {get; set;}
```

```

property System.bool UseDocumentDefaults {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use the document default settings for the component's line fonts, false to use the selected settings

Example

[Get Components in Drawing View (C#)](Get_Components_in_Drawing_View_Example_CSharp.htm)  
[Get Components in Drawing View (VB.NET)](Get_Components_in_Drawing_View_Example_VBNET.htm)  
[Get Components in Drawing View (VBA)](Get_Components_in_Drawing_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent.md)  
[IDrawingComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent_members.md)  
[IDrawingComponent::GetLineStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~GetLineStyle.md)  
[IDrawingComponent::GetLineThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~GetLineThickness.md)  
[IDrawingComponent::SetLineStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~SetLineStyle.md)  
[IDrawingComponent::SetLineThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~SetLineThickness.md)
