# PrintDirect Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~PrintDirect`

Prints the current document to the default printer.
Prints the current document to the default printer.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub PrintDirect() 
```

```

Dim instance As IModelDoc2
 
instance.PrintDirect()
```

```

void PrintDirect()
```

```

void PrintDirect(); 
```

Remarks

|  |  |
| --- | --- |
| **For this type of document...** | **Then this is printed...** |
| Drawing | All sheets |
| Part or assembly | Active view |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDocExtension::PrintOut Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PrintOut.md)  
[IModelDocExtension::IPrintOut2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IPrintOut2.md)  
[IModelDoc2::PrintPreview Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~PrintPreview.md)  
[IModelDoc2::Printer Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Printer.md)  
[IModelDoc2::PageSetup Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~PageSetup.md)  
[IModelDoc2::IPageSetup Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IPageSetup.md)
