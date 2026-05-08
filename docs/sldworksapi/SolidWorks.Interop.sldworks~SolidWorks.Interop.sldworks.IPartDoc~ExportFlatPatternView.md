# ExportFlatPatternView Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ExportFlatPatternView`

Obsolete. Superseded by IPartDoc::ExportToDWG2.}}-->
Obsolete. Superseded by [IPartDoc::ExportToDWG2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ExportToDWG2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ExportFlatPatternView( _
   ByVal FilePath As System.String, _
   ByVal Options As System.Integer _
) As System.Boolean
```

```

Dim instance As IPartDoc
Dim FilePath As System.String
Dim Options As System.Integer
Dim value As System.Boolean
 
value = instance.ExportFlatPatternView(FilePath, Options)
```

```

System.bool ExportFlatPatternView( 
   System.string FilePath,
   System.int Options
)
```

```

System.bool ExportFlatPatternView( 
   System.String^ FilePath,
   System.int Options
) 
```

#### Parameters

*FilePath*
:   Path and filename to which to save the sheet metal part in its flattened state to a DXF/DWG file

*Options*
:   Option as described in [swExportFlatPatternViewOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swExportFlatPatternViewOptions_e.html)

#### Return Value

True if the sheet metal part is enabled to be saved in its flattened state to a DXF/DWG file at the specified path and filename, false if not

Remarks

Call this method before calling [IModelDocExtension::SaveAs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveAs.md).

Example

Option Explicit

Dim swApp As SldWorks.SldWorks

Dim swModel As SldWorks.ModelDoc2

Dim swModelDocExt As SldWorks.ModelDocExtension

Dim boolstatus As Boolean

Dim longstatus As Long, longwarnings As Long

Sub main()

Set swApp = Application.SldWorks

Set swModel = swApp.ActiveDoc

Set swModelDocExt = swModel.Extension

boolstatus = swModel.ExportFlatPatternView("F:\Test\Flat pattern - sheet\_metal\_cover.DXF", swExportFlatPatternOption\_None)

swModelDocExt.SaveAs "F:\Test\Flat pattern - sheet\_metal\_cover.DXF", 0, 0, Nothing, longstatus, longwarnings

End Sub

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IPartDoc::ExportToDWG2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ExportToDWG2.md)  
[IPartDoc::IExportToDWG2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IExportToDWG2.md)
