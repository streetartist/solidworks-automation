# GetText Method (IParagraphs)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~GetText`

Gets the text of the current paragraph.
Gets the text of the current paragraph.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetText( _
   ByVal ShowWordWrap As System.Boolean _
) As System.String
```

```

Dim instance As IParagraphs
Dim ShowWordWrap As System.Boolean
Dim value As System.String
 
value = instance.GetText(ShowWordWrap)
```

```

System.string GetText( 
   System.bool ShowWordWrap
)
```

```

System.String^ GetText( 
   System.bool ShowWordWrap
) 
```

#### Parameters

*ShowWordWrap*
:   True to show word wrap, false to not

#### Return Value

Text of the current paragraph

Remarks

Before calling this method, set the current paragraph using [IParagraphs::CurrentParagraph](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~CurrentParagraph.md).

Example

See the [IParagraphs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IParagraphs Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.md)  
[IParagraphs Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs_members.md)
