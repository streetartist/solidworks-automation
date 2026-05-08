# SetIndentation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~SetIndentation`

Sets the indentation of the current paragraph.
Sets the indentation of the current paragraph.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetIndentation( _
   ByVal FirstlineIndent As System.Double, _
   ByVal Indent As System.Double, _
   ByVal IndentIncrement As System.Double _
) As System.Boolean
```

```

Dim instance As IParagraphs
Dim FirstlineIndent As System.Double
Dim Indent As System.Double
Dim IndentIncrement As System.Double
Dim value As System.Boolean
 
value = instance.SetIndentation(FirstlineIndent, Indent, IndentIncrement)
```

```

System.bool SetIndentation( 
   System.double FirstlineIndent,
   System.double Indent,
   System.double IndentIncrement
)
```

```

System.bool SetIndentation( 
   System.double FirstlineIndent,
   System.double Indent,
   System.double IndentIncrement
) 
```

#### Parameters

*FirstlineIndent*
:   Indentation of first line

*Indent*
:   Indentation of lines other than the first line

*IndentIncrement*
:   Amount by which to increment the current indents

#### Return Value

True if successful, false if not

Remarks

Before calling this method, set the current paragraph using [IParagraphs::CurrentParagraph](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~CurrentParagraph.md).

After calling this method, call [IParagraphs::UpdateParagraph](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~UpdateParagraph.md) to update the model.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IParagraphs Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.md)  
[IParagraphs Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs_members.md)  
[IParagraphs::GetIndentation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~GetIndentation.md)
