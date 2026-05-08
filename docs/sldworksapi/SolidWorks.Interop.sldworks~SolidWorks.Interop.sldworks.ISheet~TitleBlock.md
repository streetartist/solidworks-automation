# TitleBlock Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~TitleBlock`

Gets the title block in this sheet.
Gets the title block in this sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property TitleBlock As TitleBlock
```

```

Dim instance As ISheet
Dim value As TitleBlock
 
value = instance.TitleBlock
```

```

TitleBlock TitleBlock {get;}
```

```

property TitleBlock^ TitleBlock {
   TitleBlock^ get();
}
```

#### Property Value

[Title block](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock.md) in this sheet

Remarks

Only one title block can exist in a sheet. This property gets that title block, if it exists.

Example

[Get Notes from New or Existing Title Block (VBA)](Get_Notes_from_New_or_Existing_Title_Block_Example_VB.htm)  
[Get Notes from New or Existing Title Block (VB.NET)](Get_Notes_from_New_or_Existing_Title_Block_Example_VBNET.htm)  
[Get Notes from New or Existing Title Block (C#)](Get_Notes_from_New_or_Existing_Title_Block_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)  
[ISheet::TitleBlock Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~TitleBlock.md)
