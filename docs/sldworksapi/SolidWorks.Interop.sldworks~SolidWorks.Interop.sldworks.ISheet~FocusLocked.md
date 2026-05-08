# FocusLocked Property (ISheet)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~FocusLocked`

Gets or sets whether focus is locked on this sheet.
Gets or sets whether focus is locked on this sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FocusLocked As System.Boolean
```

```

Dim instance As ISheet
Dim value As System.Boolean
 
instance.FocusLocked = value
 
value = instance.FocusLocked
```

```

System.bool FocusLocked {get; set;}
```

```

property System.bool FocusLocked {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if focus locked on sheet, false if not

Example

[Insert Spline in Drawing (C++)](Insert_Spline_in_Drawing_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)  
[IView::FocusLocked Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~FocusLocked.md)
