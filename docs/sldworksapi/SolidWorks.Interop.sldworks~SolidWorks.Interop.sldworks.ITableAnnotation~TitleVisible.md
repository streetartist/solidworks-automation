# TitleVisible Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~TitleVisible`

Gets or sets whether the title of the table is visible.
Gets or sets whether the title of the table is visible.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TitleVisible As System.Boolean
```

```

Dim instance As ITableAnnotation
Dim value As System.Boolean
 
instance.TitleVisible = value
 
value = instance.TitleVisible
```

```

System.bool TitleVisible {get; set;}
```

```

property System.bool TitleVisible {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if title of the table is visible, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)  
[ITableAnnotation::Title Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Title.md)
