# SetBulletsAndNumbering Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~SetBulletsAndNumbering`

Sets the list properties of the current paragraph.
Sets the list properties of the current paragraph.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetBulletsAndNumbering( _
   ByVal ParagraphType As System.Integer, _
   ByVal NumberingType As System.Integer, _
   ByVal StartAt As System.Integer, _
   ByVal Type As System.Integer, _
   ByVal Format As System.Integer _
) As System.Boolean
```

```

Dim instance As IParagraphs
Dim ParagraphType As System.Integer
Dim NumberingType As System.Integer
Dim StartAt As System.Integer
Dim Type As System.Integer
Dim Format As System.Integer
Dim value As System.Boolean
 
value = instance.SetBulletsAndNumbering(ParagraphType, NumberingType, StartAt, Type, Format)
```

```

System.bool SetBulletsAndNumbering( 
   System.int ParagraphType,
   System.int NumberingType,
   System.int StartAt,
   System.int Type,
   System.int Format
)
```

```

System.bool SetBulletsAndNumbering( 
   System.int ParagraphType,
   System.int NumberingType,
   System.int StartAt,
   System.int Type,
   System.int Format
) 
```

#### Parameters

*ParagraphType*
:   List type as defined in [swParagraphType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swParagraphType_e.html)

*NumberingType*
:   Numbering direction as defined in [swNumberedListStartType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swNumberedListStartType_e.html); valid only if ParagraphType is swParagraphType\_e.swParagraphNumbered

*StartAt*
:   Letter or number starting this numbered list, depending on Type; valid only if ParagraphType is swParagraphType\_e.swParagraphNumbered

*Type*
:   Numbered list type as defined in [swNumberedListType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swNumberedListType_e.html); valid only if ParagraphType is swParagraphType\_e.swParagraphNumbered

*Format*
:   Numbered list format as defined in [swNumberingFormat\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swNumberingFormat_e.html); valid only if ParagraphType is swParagraphType\_e.swParagraphNumbered

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
[IParagraphs::GetBulletsAndNumbering Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~GetBulletsAndNumbering.md)
