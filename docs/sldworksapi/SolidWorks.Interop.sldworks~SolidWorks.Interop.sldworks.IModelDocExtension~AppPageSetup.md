# AppPageSetup Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AppPageSetup`

Gets the SOLIDWORKS application page setup interface for this document.
Gets the SOLIDWORKS application page setup interface for this document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property AppPageSetup As PageSetup
```

```

Dim instance As IModelDocExtension
Dim value As PageSetup
 
value = instance.AppPageSetup
```

```

PageSetup AppPageSetup {get;}
```

```

property PageSetup^ AppPageSetup {
   PageSetup^ get();
}
```

#### Property Value

[Page setup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.md) object for SOLIDWORKS

Remarks

The page setup object used when printing depends on a document setting, which indicates whether to use the application page setup, the page setup for this document.

|  |  |
| --- | --- |
| **To...** | **Use...** |
| Get or set a document setting | [IModelDocExtension::UsePageSetup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UsePageSetup.md) |
| Get the document page setup | [IModelDoc2::PageSetup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~PageSetup.md) or [IModelDoc2::IPageSetup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IPageSetup.md) |
| Get the sheet page setup | [ISheet::PageSetup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~PageSetup.md) or [ISheet::IPageSetup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~IPageSetup.md) |

Although the object that this property returns indicates that it contains application-level values, some of the values that it contains depend on the type of document. Therefore, this API is on a document interface, and you should retrieve a different one for each different document that you print.

This property is read only.

Example

[Get Whether Draft Edges Scaled in Printed Drawing (C#)](Get_Whether_Draft_Edges_Scaled_in_Printed_Drawing_Example_CSharp.htm)  
[Get Whether Draft Edges Scaled in Printed Drawing (VB.NET)](Get_Whether_Draft_Edges_Scaled_in_Printed_Drawing_Example_VBNET.htm)  
[Get Whether Draft Edges Scaled in Printed Drawing (VBA)](Get_Whether_Draft_Edges_Scaled_in_Printed_Drawing_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
