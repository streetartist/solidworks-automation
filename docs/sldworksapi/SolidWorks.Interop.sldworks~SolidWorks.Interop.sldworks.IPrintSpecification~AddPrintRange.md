# AddPrintRange Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~AddPrintRange`

Adds a range of pages to print.
Adds a range of pages to print.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub AddPrintRange( _
   ByVal FirstPage As System.Integer, _
   ByVal LastPage As System.Integer _
) 
```

```

Dim instance As IPrintSpecification
Dim FirstPage As System.Integer
Dim LastPage As System.Integer
 
instance.AddPrintRange(FirstPage, LastPage)
```

```

void AddPrintRange( 
   System.int FirstPage,
   System.int LastPage
)
```

```

void AddPrintRange( 
   System.int FirstPage,
   System.int LastPage
) 
```

#### Parameters

*FirstPage*
:   First page of print range

*LastPage*
:   Last page of print range

Remarks

Call this method multiple times to specify multiple ranges of pages to print.

Example

See the [IPrintSpecification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPrintSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification.md)  
[IPrintSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification_members.md)  
[IPrintSpecification::ResetPrintRange Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~ResetPrintRange.md)  
[IPrintSpecification::PrintRange Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~PrintRange.md)
