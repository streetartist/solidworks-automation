# IInsertBomTable Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IInsertBomTable`

Inserts a Bill of Materials (BOM) table for this drawing view using Microsoft Excel.
Inserts a Bill of Materials (BOM) table for this drawing view using Microsoft Excel.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IInsertBomTable( _
   ByVal Template As System.String, _
   ByVal Xloc As System.Double, _
   ByVal Yloc As System.Double, _
   ByRef Errors As System.Integer _
) As BomTable
```

```

Dim instance As IView
Dim Template As System.String
Dim Xloc As System.Double
Dim Yloc As System.Double
Dim Errors As System.Integer
Dim value As BomTable
 
value = instance.IInsertBomTable(Template, Xloc, Yloc, Errors)
```

```

BomTable IInsertBomTable( 
   System.string Template,
   System.double Xloc,
   System.double Yloc,
   out System.int Errors
)
```

```

BomTable^ IInsertBomTable( 
   System.String^ Template,
   System.double Xloc,
   System.double Yloc,
   [Out] System.int Errors
) 
```

#### Parameters

*Template*
:   File name of the template to use to create this BOM

*Xloc*
:   X coordinate of the location of the BOM

*Yloc*
:   Y coordinate of the location of the BOM

*Errors*
:   Status of the BOM creation operation as defined in [swBOMConfigurationCreationErrors\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBOMConfigurationCreationErrors_e.html)

#### Return Value

[BOM table](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable.md)

Remarks

This method creates a default BOM table at the specified location, using the given template. There are some user preferences that control the default appearance of the table; set them before calling this method to create a BOM that looks like you want it to look. See:

- [ISldWorks::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.md) values swBOMConfigurationLocked, swBOMConfigurationUseDocumentFont, swBOMConfigurationUseSummaryInfo, swBOMConfigurationAlignBottom, swBOMContentsDisplayAtTop, swBOMControlIdFromAssembly, swBOMControlMissingRows, and swBOMControlSplitTable
- [ISldWorks::SetUserPreferenceIntegerValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceIntegerValue.md) values swBOMConfigurationAnchorType, swBOMConfigurationWhatToShow, swBOMControlMissingRowDisplay, and swBOMControlSplitDirection
- [ISldWorks::SetUserPreferenceDoubleValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceDoubleValue.md) value swBOMControlSplitHeight

The Template argument is the full path name of the BOM template to use in creating this BOM. If you specify only a file name with no directory, SOLIDWORKS looks for it in *install\_dir*\lang\local language. If the file name is blank, the template uses the **bomtemp.xls** file in that directory.

The Xloc and Yloc arguments are the (X,Y) drawing location where the BOM is anchored. To get the drawing origin from the drawing view origin, use [IView::GetXform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetXform.md) or [IView::IGetXform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetXform.md). To get the drawing view extents on the drawing, use [IView::GetOutline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetOutline.md) or [IView::IGetOutline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetOutline.md).

If the BOM creation fails, the Dispatch pointer that is returned is null. If you want more information about why the operation failed, use the Errors argument. You can pass in null as the Errors argument if you are not interested in the specific information.

**NOTE:** Use [IView::InsertBomTable2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable2.md) to insert a BOM using SOLIDWORKS table functionality.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::InsertBomTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable.md)  
[IView::SetKeepLinkedToBOM Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetKeepLinkedToBOM.md)  
[IView::GetKeepLinkedToBOM Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetKeepLinkedToBOM.md)  
[IView::GetKeepLinkedToBOMName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetKeepLinkedToBOMName.md)
