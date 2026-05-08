# SetFormatting Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~SetFormatting`

Sets the formatting of the current paragraph.
Sets the formatting of the current paragraph.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetFormatting( _
   ByVal Paragraphspacing As System.Double, _
   ByVal LineSpacing As System.Double _
) As System.Boolean
```

```

Dim instance As IParagraphs
Dim Paragraphspacing As System.Double
Dim LineSpacing As System.Double
Dim value As System.Boolean
 
value = instance.SetFormatting(Paragraphspacing, LineSpacing)
```

```

System.bool SetFormatting( 
   System.double Paragraphspacing,
   System.double LineSpacing
)
```

```

System.bool SetFormatting( 
   System.double Paragraphspacing,
   System.double LineSpacing
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

After calling this method, call [IParagraphs::UpdateParagraph](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~UpdateParagraph.md) to update the model.

Example

See the [IParagraphs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IParagraphs Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.md)  
[IParagraphs Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs_members.md)  
[IParagraphs::GetFormatting Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~GetFormatting.md)
