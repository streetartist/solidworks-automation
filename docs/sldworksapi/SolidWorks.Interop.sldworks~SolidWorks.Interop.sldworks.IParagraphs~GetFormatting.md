# GetFormatting Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~GetFormatting`

Gets the formatting of the current paragraph.
Gets the formatting of the current paragraph.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFormatting( _
   ByRef Paragraphspacing As System.Double, _
   ByRef LineSpacing As System.Double _
) As System.Boolean
```

```

Dim instance As IParagraphs
Dim Paragraphspacing As System.Double
Dim LineSpacing As System.Double
Dim value As System.Boolean
 
value = instance.GetFormatting(Paragraphspacing, LineSpacing)
```

```

System.bool GetFormatting( 
   out System.double Paragraphspacing,
   out System.double LineSpacing
)
```

```

System.bool GetFormatting( 
   [Out] System.double Paragraphspacing,
   [Out] System.double LineSpacing
) 
```

#### Parameters

*Paragraphspacing*
:   Paragraph spacing

*LineSpacing*
:   Line spacing

#### Return Value

True if successful, false if not

Remarks

Before calling this method, set the current paragraph using [IParagraphs::CurrentParagraph](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~CurrentParagraph.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IParagraphs Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.md)  
[IParagraphs Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs_members.md)  
[IParagraphs::SetFormatting Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~SetFormatting.md)
