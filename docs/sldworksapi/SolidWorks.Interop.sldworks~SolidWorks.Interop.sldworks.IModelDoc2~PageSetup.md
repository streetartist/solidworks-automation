# PageSetup Property (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~PageSetup`

Gets the page setup for this document.
Gets the page setup for this document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property PageSetup As System.Object
```

```

Dim instance As IModelDoc2
Dim value As System.Object
 
value = instance.PageSetup
```

```

System.object PageSetup {get;}
```

```

property System.Object^ PageSetup {
   System.Object^ get();
}
```

#### Property Value

[Page setup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.md)

Example

[Print Drawing and Save As PDF (VBA)](Print_Drawing_and_Save_as_PDF_Example_VB.htm)  
[Print Drawing (C#)](Print_Drawing_as_High_Quality_Example_CSharp.htm)  
[Print Drawing (VB.NET)](Print_Drawing_as_High_Quality_Example_VBNET.htm)  
[Print Drawing (VBA)](Print_Drawing_as_High_Quality_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::IPageSetup Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IPageSetup.md)  
[IModelDocExtension::AppPageSetup Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AppPageSetup.md)  
[IModelDocExtension::UsePageSetup Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UsePageSetup.md)
