# UpperCase Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~UpperCase`

Gets or sets whether text in the table is all upper case.
Gets or sets whether text in the table is all upper case.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UpperCase As System.Integer
```

```

Dim instance As ITableAnnotation
Dim value As System.Integer
 
instance.UpperCase = value
 
value = instance.UpperCase
```

```

System.int UpperCase {get; set;}
```

```

property System.int UpperCase {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

1 if text is all upper case, 0 if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)
