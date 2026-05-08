# IGetTextFormat Method (IAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetTextFormat`

Gets the text format for the specified text in this annotation.
Gets the text format for the specified text in this annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetTextFormat( _
   ByVal Index As System.Integer _
) As TextFormat
```

```

Dim instance As IAnnotation
Dim Index As System.Integer
Dim value As TextFormat
 
value = instance.IGetTextFormat(Index)
```

```

TextFormat IGetTextFormat( 
   System.int Index
)
```

```

TextFormat^ IGetTextFormat( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Number indicating which text within this annotation to check

#### Return Value

Pointer to [ITextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.md) of the specified piece of text

Remarks

The behavior of this method differs depending on the type of annotation.

- [Datum Target](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.md) and [Datum Feature Symbols](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym.md)  
    
  These symbols always use the document default setting for dimension text format to  
  display text within the symbol. The index argument is not used and should be set  
  to 0.
- [Geometric Tolerance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md), [Display Dimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md), [Simple Notes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md), [Surface Finish](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.md), and [Weld Symbols](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md)  
    
  These symbols can either use the document default setting to display text within  
  the symbol (dimension text setting for the geometric tolerance symbols and display  
  dimensions, or note text setting for notes) or they can use a local format. The index  
  argument is not used and should be set to 0.
- [Blocks](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md) (and compound notes in documents created in SOLIDWORKS 2015 and earlier)  
    
  These symbols might contain several different pieces of text; each piece can use  
  the document default setting for notes or a local format. The index argument identifies  
  the text. The index value is 0-based. If the index value is invalid, then this method  
  returns a NULL pointer. To get the number of text or [ITextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.md) objects, use [IAnnotation::GetTextFormatCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetTextFormatCount.md).
- Rich Text Format  
    
  If a note contains embedded rich text information in the string, this method returns  
  a text format that does not necessarily reflect what is displayed on the screen for  
  that note. Use [INote::HasMultipleFonts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~HasMultipleFonts.md) to determine if the note contains embedded  
  rich text information.

ITextFormat is returned if it is for a local setting or for the document  
default setting. To determine whether or not this annotation is using the document  
default settings for text format, use [IAnnotation::GetUseDocTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetUseDocTextFormat.md). To set the  
text format information, use [IAnnotation::SetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetTextFormat.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)  
[IAnnotation::GetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetTextFormat.md)  
[ITextFormat Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.md)  
[IAnnotation::GetTextFormatCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetTextFormatCount.md)  
[IAnnotation::ISetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ISetTextFormat.md)  
[IAnnotation::GetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetTextFormat.md)
