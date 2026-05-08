# SheetFormatVisible Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SheetFormatVisible`

Gets or sets whether the sheet format is currently visible in this drawing sheet.
Gets or sets whether the sheet format is currently visible in this drawing sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SheetFormatVisible As System.Boolean
```

```

Dim instance As ISheet
Dim value As System.Boolean
 
instance.SheetFormatVisible = value
 
value = instance.SheetFormatVisible
```

```

System.bool SheetFormatVisible {get; set;}
```

```

property System.bool SheetFormatVisible {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the sheet format is visible, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)  
[ISheet::GetSheetFormatName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetSheetFormatName.md)  
[ISheet::SetSheetFormatName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetSheetFormatName.md)
