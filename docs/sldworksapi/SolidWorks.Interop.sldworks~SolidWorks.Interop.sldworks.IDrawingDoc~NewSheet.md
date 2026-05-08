# NewSheet Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~NewSheet`

Obsolete. Superseded by IDrawingDoc::NewSheet3.
Obsolete. Superseded by [IDrawingDoc::NewSheet3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~NewSheet3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub NewSheet( _
   ByVal Name As System.String, _
   ByVal PaperSize As System.Short, _
   ByVal TemplateIn As System.Short, _
   ByVal Scale1 As System.Double, _
   ByVal Scale2 As System.Double _
) 
```

```

Dim instance As IDrawingDoc
Dim Name As System.String
Dim PaperSize As System.Short
Dim TemplateIn As System.Short
Dim Scale1 As System.Double
Dim Scale2 As System.Double
 
instance.NewSheet(Name, PaperSize, TemplateIn, Scale1, Scale2)
```

```

void NewSheet( 
   System.string Name,
   System.short PaperSize,
   System.short TemplateIn,
   System.double Scale1,
   System.double Scale2
)
```

```

void NewSheet( 
   System.String^ Name,
   System.short PaperSize,
   System.short TemplateIn,
   System.double Scale1,
   System.double Scale2
) 
```

#### Parameters

*Name*

*PaperSize*

*TemplateIn*

*Scale1*

*Scale2*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)
