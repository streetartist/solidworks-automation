# SetupSheet5 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetupSheet5`

Obsolete. Superseded by IDrawingDoc::SetupSheet6.
Obsolete. Superseded by [IDrawingDoc::SetupSheet6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetupSheet6.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetupSheet5( _
   ByVal Name As System.String, _
   ByVal PaperSize As System.Integer, _
   ByVal TemplateIn As System.Integer, _
   ByVal Scale1 As System.Double, _
   ByVal Scale2 As System.Double, _
   ByVal FirstAngle As System.Boolean, _
   ByVal TemplateName As System.String, _
   ByVal Width As System.Double, _
   ByVal Height As System.Double, _
   ByVal PropertyViewName As System.String, _
   ByVal RemoveModifiedNotes As System.Boolean _
) As System.Boolean
```

```

Dim instance As IDrawingDoc
Dim Name As System.String
Dim PaperSize As System.Integer
Dim TemplateIn As System.Integer
Dim Scale1 As System.Double
Dim Scale2 As System.Double
Dim FirstAngle As System.Boolean
Dim TemplateName As System.String
Dim Width As System.Double
Dim Height As System.Double
Dim PropertyViewName As System.String
Dim RemoveModifiedNotes As System.Boolean
Dim value As System.Boolean
 
value = instance.SetupSheet5(Name, PaperSize, TemplateIn, Scale1, Scale2, FirstAngle, TemplateName, Width, Height, PropertyViewName, RemoveModifiedNotes)
```

```

System.bool SetupSheet5( 
   System.string Name,
   System.int PaperSize,
   System.int TemplateIn,
   System.double Scale1,
   System.double Scale2,
   System.bool FirstAngle,
   System.string TemplateName,
   System.double Width,
   System.double Height,
   System.string PropertyViewName,
   System.bool RemoveModifiedNotes
)
```

```

System.bool SetupSheet5( 
   System.String^ Name,
   System.int PaperSize,
   System.int TemplateIn,
   System.double Scale1,
   System.double Scale2,
   System.bool FirstAngle,
   System.String^ TemplateName,
   System.double Width,
   System.double Height,
   System.String^ PropertyViewName,
   System.bool RemoveModifiedNotes
) 
```

#### Parameters

*Name*
:   Name for the sheet

*PaperSize*
:   Size of paper if using swDwgTemplateNone as defined in [swDwgPaperSizes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgPaperSizes_e.html)

*TemplateIn*
:   Template as defined in [swDwgTemplates\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgTemplates_e.html)

*Scale1*
:   Scale numerator

*Scale2*
:   Scale denominator

*FirstAngle*
:   True for first angle projection, false otherwise

*TemplateName*
:   Name of custom template with full directory path if using swDwgTemplateCustom

*Width*
:   Paper width; valid only if TemplateIn is set to swDwgTemplates\_e.swDwgTemplateNone or PaperSize is set to swDwgPaperSizes\_e.swDwgPapersUserDefined

*Height*
:   Paper height if TemplateIn is set to swDwgTemplateNone or swDwgPapersUserDefined

*PropertyViewName*
:   Name of view containing the model from which to get custom property values

*RemoveModifiedNotes*
:   True to delete modified notes, false to not

Remarks

Call [IModelDoc2::ForceRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceRebuild3.md) after calling IDrawingDoc::SetupSheet5 to update any changes to first angle/third angle projections in the drawing views.

If you specify a different filename for TemplateName than what is currently being used by SOLIDWORKS, then SOLIDWORKS updates the sheet format.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::ActivateSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActivateSheet.md)  
[IDrawingDoc::EditSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditSheet.md)  
[IDrawingDoc::GetEditSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetEditSheet.md)  
[IDrawingDoc::GetSheetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetSheetCount.md)  
[IDrawingDoc::GetSheetNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetSheetNames.md)  
[IDrawingDoc::IGetCurrentSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetCurrentSheet.md)  
[IDrawingDoc::IGetSheetNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetSheetNames.md)  
[IDrawingDoc::IReorderSheets Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IReorderSheets.md)  
[IDrawingDoc::NewSheet3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~NewSheet3.md)  
[IDrawingDoc::SheetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SheetNext.md)  
[IDrawingDoc::SheetPrevious Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SheetPrevious.md)  
[IDrawingDoc::ReorderSheets](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ReorderSheets.md)  
[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)
