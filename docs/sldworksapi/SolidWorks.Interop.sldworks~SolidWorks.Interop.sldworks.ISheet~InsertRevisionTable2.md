# InsertRevisionTable2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~InsertRevisionTable2`

Inserts a revision table in this drawing sheet.
Inserts a revision table in this drawing sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertRevisionTable2( _
   ByVal UseAnchorPoint As System.Boolean, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal AnchorType As System.Integer, _
   ByVal TableTemplate As System.String, _
   ByVal Shape As System.Integer, _
   ByVal AutoUpdateZoomCells As System.Boolean _
) As RevisionTableAnnotation
```

```

Dim instance As ISheet
Dim UseAnchorPoint As System.Boolean
Dim X As System.Double
Dim Y As System.Double
Dim AnchorType As System.Integer
Dim TableTemplate As System.String
Dim Shape As System.Integer
Dim AutoUpdateZoomCells As System.Boolean
Dim value As RevisionTableAnnotation
 
value = instance.InsertRevisionTable2(UseAnchorPoint, X, Y, AnchorType, TableTemplate, Shape, AutoUpdateZoomCells)
```

```

RevisionTableAnnotation InsertRevisionTable2( 
   System.bool UseAnchorPoint,
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.string TableTemplate,
   System.int Shape,
   System.bool AutoUpdateZoomCells
)
```

```

RevisionTableAnnotation^ InsertRevisionTable2( 
   System.bool UseAnchorPoint,
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.String^ TableTemplate,
   System.int Shape,
   System.bool AutoUpdateZoomCells
) 
```

#### Parameters

*UseAnchorPoint*
:   True to insert the revision table at the existing revision table anchor point, false to anchor the table at the point specified by X and Y

*X*
:   X coordinate for the placement of the revision table annotation

*Y*
:   Y coordinate for the placement of this revision table annotation

*AnchorType*
:   Anchor type as defined by [swBOMConfigurationAnchorType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBOMConfigurationAnchorType_e.html)

*TableTemplate*
:   Path and filename of the template that corresponds to this type of table (see **Remarks**)

*Shape*
:   Revision symbol shape as defined in [swRevisionTableSymbolShape\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRevisionTableSymbolShape_e.html)

*AutoUpdateZoomCells*
:   True to automatically update zone cells, false to not

#### Return Value

[Revision table](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation.md) or null if a revision table already exists

Remarks

By default, the revision table templates are in install\_dir\lang\language and have a filename extension of .sldrevtbt. The template and table must be of the same type. For example, you must specify TableTemplate with *install\_dir*\lang\English\standard revision block.sldrevtbt if you want to insert the English version of a revision block table.

Example

[Create Drawing Sheet Zones (VBA)](Create_Drawing_Sheet_Zones_Example_VB.htm)  
[Create Drawing Sheet Zones (VB.NET)](Create_Drawing_Sheet_Zones_Example_VBNET.htm)  
[Create Drawing Sheet Zones (C#)](Create_Drawing_Sheet_Zones_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)  
[ISheet::RevisionTable Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~RevisionTable.md)
