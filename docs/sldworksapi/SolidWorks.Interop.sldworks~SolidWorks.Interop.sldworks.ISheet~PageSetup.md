# PageSetup Property (ISheet)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~PageSetup`

Gets the page setup for this sheet.
Gets the page setup for this sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property PageSetup As System.Object
```

```

Dim instance As ISheet
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

Remarks

Page setup values are overridden on a sheet by sheet basis.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)  
[ISheet::IPageSetup Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~IPageSetup.md)  
[ISheet::GetProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetProperties.md)  
[ISheet::IGetProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~IGetProperties.md)  
[ISheet::SetProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetProperties.md)
