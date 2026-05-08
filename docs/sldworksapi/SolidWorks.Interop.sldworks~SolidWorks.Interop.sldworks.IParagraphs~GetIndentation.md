# GetIndentation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~GetIndentation`

Gets the indentation of the current paragraph.
Gets the indentation of the current paragraph.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetIndentation( _
   ByRef FirstlineIndent As System.Double, _
   ByRef Indent As System.Double, _
   ByRef IndentIncrement As System.Double _
) As System.Boolean
```

```

Dim instance As IParagraphs
Dim FirstlineIndent As System.Double
Dim Indent As System.Double
Dim IndentIncrement As System.Double
Dim value As System.Boolean
 
value = instance.GetIndentation(FirstlineIndent, Indent, IndentIncrement)
```

```

System.bool GetIndentation( 
   out System.double FirstlineIndent,
   out System.double Indent,
   out System.double IndentIncrement
)
```

```

System.bool GetIndentation( 
   [Out] System.double FirstlineIndent,
   [Out] System.double Indent,
   [Out] System.double IndentIncrement
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

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IParagraphs Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.md)  
[IParagraphs Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs_members.md)  
[IParagraphs::SetIndentation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~SetIndentation.md)
