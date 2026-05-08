# NewSheet4 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~NewSheet4`

Creates a new drawing sheet in this drawing document.
Creates a new drawing sheet in this drawing document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function NewSheet4( _
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
   ByVal ZoneLeftMargin As System.Double, _
   ByVal ZoneRightMargin As System.Double, _
   ByVal ZoneTopMargin As System.Double, _
   ByVal ZoneBottomMargin As System.Double, _
   ByVal ZoneRow As System.Integer, _
   ByVal ZoneCol As System.Integer _
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
Dim ZoneLeftMargin As System.Double
Dim ZoneRightMargin As System.Double
Dim ZoneTopMargin As System.Double
Dim ZoneBottomMargin As System.Double
Dim ZoneRow As System.Integer
Dim ZoneCol As System.Integer
Dim value As System.Boolean
 
value = instance.NewSheet4(Name, PaperSize, TemplateIn, Scale1, Scale2, FirstAngle, TemplateName, Width, Height, PropertyViewName, ZoneLeftMargin, ZoneRightMargin, ZoneTopMargin, ZoneBottomMargin, ZoneRow, ZoneCol)
```

```

System.bool NewSheet4( 
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
   System.double ZoneLeftMargin,
   System.double ZoneRightMargin,
   System.double ZoneTopMargin,
   System.double ZoneBottomMargin,
   System.int ZoneRow,
   System.int ZoneCol
)
```

```

System.bool NewSheet4( 
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
   System.double ZoneLeftMargin,
   System.double ZoneRightMargin,
   System.double ZoneTopMargin,
   System.double ZoneBottomMargin,
   System.int ZoneRow,
   System.int ZoneCol
) 
```

#### Parameters

*Name*
:   Name to be given to the new drawing sheet

*PaperSize*
:   Size of paper as defined in [swDwgPaperSizes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgPaperSizes_e.html); valid only if TemplateIn is swDwgTemplates\_e.swDwgTemplateNone

*TemplateIn*
:   Template as defined in [swDwgTemplates\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgTemplates_e.html)

*Scale1*
:   Scale numerator

*Scale2*
:   Scale denominator

*FirstAngle*
:   True for first angle projection, false for third angle projection

*TemplateName*
:   Name of custom template with full directory path; valid only if TemplateIn is set to swDwgTemplates\_e.swDwgTemplateCustom

*Width*
:   Paper width; valid only if TemplateIn is set to swDwgTemplates\_e.swDwgTemplateNone or PaperSize is set to swDwgPaperSizes\_e.swDwgPapersUserDefined

*Height*
:   Paper height; valid only if TemplateIn is set to swDwgTemplates\_e.swDwgTemplateNone or PaperSize is set to swDwgPaperSizes\_e.swDwgPapersUserDefined

*PropertyViewName*
:   Name of view containing the model from which to get custom property values

*ZoneLeftMargin*
:   Zone area left margin; distance from drawing sheet's left edge

*ZoneRightMargin*
:   Zone area right margin; distance from drawing sheet's right edge

*ZoneTopMargin*
:   Zone area top margin; distance from drawing sheet's top edge

*ZoneBottomMargin*
:   Zone area bottom margin; distance from drawing sheet's bottom edge

*ZoneRow*
:   Number of zone rows in the zone area of this sheet (see **Remarks**)

*ZoneCol*
:   Number of zone columns in the zone area of this sheet (see **Remarks**)

#### Return Value

True if drawing sheet creation was successful, false if not

Remarks

The drawing sheet can be created with zones that annotations in other views can reference. Each zone is referenced by an alphanumeric label that is defined using the Zone Editor. See the SOLIDWORKS Help for more information about drawing sheet zones.

(ZoneRow x ZoneCol) is the total number of zones in the zone area of this drawing sheet. The zone area is specified by ZoneLeftMargin, ZoneRightMargin, ZoneTopMargin, and ZoneBottomMargin.

Example

[Create Drawing Sheet Zones (VBA)](Create_Drawing_Sheet_Zones_Example_VB.htm)  
[Create Drawing Sheet Zones (VB.NET)](Create_Drawing_Sheet_Zones_Example_VBNET.htm)  
[Create Drawing Sheet Zones (C#)](Create_Drawing_Sheet_Zones_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::ActivateSheet Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActivateSheet.md)  
[IDrawingDoc::EditSheet Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditSheet.md)  
[IDrawingDoc::GetCurrentSheet Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetCurrentSheet.md)  
[IDrawingDoc::GetSheetCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetSheetCount.md)  
[IDrawingDoc::GetSheetNames Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetSheetNames.md)  
[IDrawingDoc::ReorderSheets Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ReorderSheets.md)  
[IDrawingDoc::SetupSheet6 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetupSheet6.md)  
[IDrawingDoc::SheetNext Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SheetNext.md)  
[IDrawingDoc::SheetPrevious Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SheetPrevious.md)  
[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[IDrawingDoc::PasteSheet Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~PasteSheet.md)  
[ISheet::GetDrawingZone Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetDrawingZone.md)
