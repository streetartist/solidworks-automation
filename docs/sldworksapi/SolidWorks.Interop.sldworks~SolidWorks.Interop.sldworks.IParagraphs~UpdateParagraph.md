# UpdateParagraph Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~UpdateParagraph`

Updates the model with the changes made to the current paragraph.
Updates the model with the changes made to the current paragraph.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function UpdateParagraph() As System.Boolean
```

```

Dim instance As IParagraphs
Dim value As System.Boolean
 
value = instance.UpdateParagraph()
```

```

System.bool UpdateParagraph()
```

```

System.bool UpdateParagraph(); 
```

#### Return Value

True if the model is updated with the paragraph changes, false if not

Remarks

You must call this method to update the model after calling:

- [IParagraphs::SetBulletsAndNumbering](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~SetBulletsAndNumbering.md)
- [IParagraphs::SetFormatting](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~SetFormatting.md)
- [IParagraphs::SetIndentation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~SetIndentation.md)
- [IParagraphs::SetTextSegmentFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~SetTextSegmentFormat.md)

Example

See the [IParagraphs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IParagraphs Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.md)  
[IParagraphs Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs_members.md)
