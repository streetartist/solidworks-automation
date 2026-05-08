# SetupSheet2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetupSheet2`

Obsolete. Superseded by IDrawingDoc::SetupSheet4.
Obsolete. Superseded by [IDrawingDoc::SetupSheet4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetupSheet4.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetupSheet2( _
   ByVal Name As System.String, _
   ByVal PaperSize As System.Short, _
   ByVal TemplateIn As System.Short, _
   ByVal Scale1 As System.Double, _
   ByVal Scale2 As System.Double, _
   ByVal SkPointsFlag As System.Integer _
) 
```

```

Dim instance As IDrawingDoc
Dim Name As System.String
Dim PaperSize As System.Short
Dim TemplateIn As System.Short
Dim Scale1 As System.Double
Dim Scale2 As System.Double
Dim SkPointsFlag As System.Integer
 
instance.SetupSheet2(Name, PaperSize, TemplateIn, Scale1, Scale2, SkPointsFlag)
```

```

void SetupSheet2( 
   System.string Name,
   System.short PaperSize,
   System.short TemplateIn,
   System.double Scale1,
   System.double Scale2,
   System.int SkPointsFlag
)
```

```

void SetupSheet2( 
   System.String^ Name,
   System.short PaperSize,
   System.short TemplateIn,
   System.double Scale1,
   System.double Scale2,
   System.int SkPointsFlag
) 
```

#### Parameters

*Name*

*PaperSize*

*TemplateIn*

*Scale1*

*Scale2*

*SkPointsFlag*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)
