# ISetTextFormat Method (IAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ISetTextFormat`

Sets the text format information for the specified text within this annotation.
Sets the text format information for the specified text within this annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISetTextFormat( _
   ByVal Index As System.Integer, _
   ByVal UseDoc As System.Boolean, _
   ByVal TextFormat As TextFormat _
) As System.Boolean
```

```

Dim instance As IAnnotation
Dim Index As System.Integer
Dim UseDoc As System.Boolean
Dim TextFormat As TextFormat
Dim value As System.Boolean
 
value = instance.ISetTextFormat(Index, UseDoc, TextFormat)
```

```

System.bool ISetTextFormat( 
   System.int Index,
   System.bool UseDoc,
   TextFormat TextFormat
)
```

```

System.bool ISetTextFormat( 
   System.int Index,
   System.bool UseDoc,
   TextFormat^ TextFormat
) 
```

#### Parameters

*Index*
:   Number indicating which text within this annotation to check

*UseDoc*
:   True to use the document default setting for text format, false to not

*TextFormat*
:   Object to use for the [ITextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.md) on the specified piece of text

#### Return Value

True if this method is successful in setting the text format information, false if not

Remarks

The behavior of this method differs depending on the type of annotation.

- [Datum Target](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym.md) and [Datum Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.md) Symbols  
    
  These symbols always use the document default setting for dimension text format to display all of the text objects within the symbol. This method has no effect on the annotation.
- [Geometric Tolerance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md), [Display Dimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md), [Simple Notes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md), [Surface Finish](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.md), and [Weld](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md) Symbols  
    
  These symbols can use the document default setting for display of all text objects within the symbol (dimension text setting for the geometric tolerance symbols and display dimensions, or note text setting for notes) or they can use a local format. The index argument is not used and should be set to 0.
- [Blocks](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md) (and compound notes in documents created in SOLIDWORKS 2015 and earlier)  
    
  These symbols might contain several different pieces of text; each piece can use the document default setting for notes or a local format. The index argument identifies the text. The index value is 0 based. If the index value is invalid, then this method returns false. To get the number of text or TextFormat objects, use [IAnnotation::GetTextFormatCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetTextFormatCount.md).
- Rich Text Format  
    
  If a notes contains embedded rich text information in the string, then using this method to set a specific text format has no effect and returns false. If you use this method to set the note to use the document default text format, then all of the rich text font information is removed from the string.  
    
  To set a specific text format for a note that contains embedded rich text information, perform these two steps. First use this method to set the document default. Then use this method to set the specific text format.

If the useDoc argument is True, then the annotation is set to use the appropriate document default setting and ignores the textFormat argument, which should be set to NULL. To determine whether or not this annotation is using the document default settings for text format, use [IAnnotation::GetUseDocTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetUseDocTextFormat.md). To set the text format information, use [IAnnotation::SetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetTextFormat.md) or [IAnnotation::ISetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ISetTextFormat.md).

To see the effects of changing the text format information for this annotation, use [ModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)  
[IAnnotation::SetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetTextFormat.md)  
[IAnnotation::IGetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetTextFormat.md)  
[IAnnotation::GetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetTextFormat.md)
