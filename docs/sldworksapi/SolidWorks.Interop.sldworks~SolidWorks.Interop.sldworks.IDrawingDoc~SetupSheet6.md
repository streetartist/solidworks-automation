# SetupSheet6 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetupSheet6`

Sets up the specified drawing sheet.
Sets up the specified drawing sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetupSheet6( _
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
   ByVal RemoveModifiedNotes As System.Boolean, _
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
Dim RemoveModifiedNotes As System.Boolean
Dim ZoneLeftMargin As System.Double
Dim ZoneRightMargin As System.Double
Dim ZoneTopMargin As System.Double
Dim ZoneBottomMargin As System.Double
Dim ZoneRow As System.Integer
Dim ZoneCol As System.Integer
Dim value As System.Boolean
 
value = instance.SetupSheet6(Name, PaperSize, TemplateIn, Scale1, Scale2, FirstAngle, TemplateName, Width, Height, PropertyViewName, RemoveModifiedNotes, ZoneLeftMargin, ZoneRightMargin, ZoneTopMargin, ZoneBottomMargin, ZoneRow, ZoneCol)
```

```

System.bool SetupSheet6( 
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
   System.bool RemoveModifiedNotes,
   System.double ZoneLeftMargin,
   System.double ZoneRightMargin,
   System.double ZoneTopMargin,
   System.double ZoneBottomMargin,
   System.int ZoneRow,
   System.int ZoneCol
)
```

```

System.bool SetupSheet6( 
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
   System.bool RemoveModifiedNotes,
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
:   Name of the sheet to set up

*PaperSize*
:   Size of paper as defined in [swDwgPaperSizes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgPaperSizes_e.html); valid only if TemplateIn is set to swDwgTemplates\_e.swDwgTemplateNone

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

*RemoveModifiedNotes*
:   True to delete modified notes, false to not

*ZoneLeftMargin*
:   Zone area left margin; distance from drawing sheet's left edge

*ZoneRightMargin*
:   Zone area right margin; distance from drawing sheet's right edge

*ZoneTopMargin*
:   Zone area top margin; distance from drawing sheet's top edge

*ZoneBottomMargin*
:   Zone area bottom margin; distance from drawing sheet's bottom edge

*ZoneRow*
:   Number of zone rows in the zone area of this sheet (see **Remarks**)

*ZoneCol*
:   Number of zone columns in the zone area of this sheet (see **Remarks**)

#### Return Value

True if drawing sheet setup is successful, false if not

Remarks

After calling this method, call [IModelDoc2::ForceRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceRebuild3.md) to update any changes to first angle/third angle projections in the drawing views.

If you specify a different filename for TemplateName than what is currently being used by SOLIDWORKS, then SOLIDWORKS updates the sheet format.

The drawing sheet can be set up with zones that annotations in other views can reference. Each zone is referenced by an alphanumeric label that is defined using the Zone Editor. See the SOLIDWORKS Help for more information about drawing sheet zones.

Multiplying ZoneRow by ZoneCol equals the total number of zones in the zone area of this drawing sheet. The zone area is specified by ZoneLeftMargin, ZoneRightMargin, ZoneTopMargin, and ZoneBottomMargin.

To modify the setups of multiple drawing sheets with just one call to IDrawingDoc::SetupSheet6, call [IDrawingDoc::SetSelectedSheets](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetSheetsSelected.md) before calling IDrawingDoc::SetupSheet6.

Example

[Create Drawing Sheet Zones (VBA)](Create_Drawing_Sheet_Zones_Example_VB.htm)  
[Create Drawing Sheet Zones (VB.NET)](Create_Drawing_Sheet_Zones_Example_VBNET.htm)  
[Create Drawing Sheet Zones (C#)](Create_Drawing_Sheet_Zones_Example_CSharp.htm)  
[Modify Multiple Drawing Sheets Setups (C#)](Modify_Multiple_Drawing_Sheets_Setups_Example_CSharp.htm)  
[Modify Multiple Drawing Sheets Setups (VB.NET)](Modify_Multiple_Drawing_Sheets_Setups_Example_VBNET.htm)  
[Modify Multiple Drawing Sheets Setups (VBA)](Modify_Multiple_Drawing_Sheets_Setups_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::ActivateSheet Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActivateSheet.md)  
[IDrawingDoc::EditSheet Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditSheet.md)  
[IDrawingDoc::GetEditSheet Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetEditSheet.md)  
[IDrawingDoc::GetSheetCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetSheetCount.md)  
[IDrawingDoc::GetSheetNames Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetSheetNames.md)  
[IDrawingDoc::NewSheet4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~NewSheet4.md)  
[IDrawingDoc::PasteSheet Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~PasteSheet.md)  
[IDrawingDoc::SheetNext Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SheetNext.md)  
[IDrawingDoc::SheetPrevious Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SheetPrevious.md)  
[IDrawingDoc::ReorderSheets Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ReorderSheets.md)  
[ISheet::GetDrawingZone Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetDrawingZone.md)  
[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)
