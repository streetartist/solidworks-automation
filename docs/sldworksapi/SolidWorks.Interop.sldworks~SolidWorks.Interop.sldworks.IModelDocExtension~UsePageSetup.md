# UsePageSetup Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UsePageSetup`

Gets or sets whether this document uses its own page setup values, SOLIDWORKS application page setup values, or setup values on individual drawing sheets.
Gets or sets whether this document uses its own page setup values, SOLIDWORKS application page setup values, or setup values on individual drawing sheets.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UsePageSetup As System.Integer
```

```

Dim instance As IModelDocExtension
Dim value As System.Integer
 
instance.UsePageSetup = value
 
value = instance.UsePageSetup
```

```

System.int UsePageSetup {get; set;}
```

```

property System.int UsePageSetup {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Page setup to use as defined in [swPageSetupInUse\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPageSetupInUse_e.html)

Remarks

|  |  |
| --- | --- |
| **To retrieve this page setup...** | **Use...** |
| Application | [IModelDocExtension::AppPageSetup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AppPageSetup.md) |
| Document | [IModelDoc2::PageSetup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~PageSetup.md) or [IModelDoc2::IPageSetup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IPageSetup.md) |
| Sheet | [ISheet::PageSetup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~PageSetup.md) or [ISheet::IPageSetup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~IPageSetup.md) |

Example

[Print Drawing (C#)](Print_Drawing_as_High_Quality_Example_CSharp.htm)  
[Print Drawing (VB.NET)](Print_Drawing_as_High_Quality_Example_VBNET.htm)  
[Print Drawing (VBA)](Print_Drawing_as_High_Quality_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IPageSetup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.md)
