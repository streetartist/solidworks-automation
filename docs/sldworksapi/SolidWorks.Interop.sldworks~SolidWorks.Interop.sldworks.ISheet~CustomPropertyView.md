# CustomPropertyView Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~CustomPropertyView`

Gets or sets the drawing view to use to set the custom information for this drawing sheet.
Gets or sets the drawing view to use to set the custom information for this drawing sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CustomPropertyView As System.String
```

```

Dim instance As ISheet
Dim value As System.String
 
instance.CustomPropertyView = value
 
value = instance.CustomPropertyView
```

```

System.string CustomPropertyView {get; set;}
```

```

property System.String^ CustomPropertyView {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Name of the drawing view from which to get the custom information

Remarks

You can also use [IDrawingDoc::SetupSheet4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetupSheet4.md) to set the name of the drawing view to use to set the custom information for this drawing sheet.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)
