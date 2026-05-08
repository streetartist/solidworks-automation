# SetBomTable Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~SetBomTable`

Maps a BOM Table Area in the theme with a BOM table in the model and sets the columns in the BOM table to export to the BOM Table Area in a SOLIDWORKS MBD 3D PDF.
Maps a BOM Table Area in the [theme](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~ThemeName.md) with a BOM table in the model and sets the columns in the BOM table to export to the BOM Table Area in a SOLIDWORKS MBD 3D PDF.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetBomTable( _
   ByVal Index As System.Integer, _
   ByVal BomTableName As System.String, _
   ByVal Columns As System.Object _
) As System.Integer
```

```

Dim instance As IMBD3DPdfData
Dim Index As System.Integer
Dim BomTableName As System.String
Dim Columns As System.Object
Dim value As System.Integer
 
value = instance.SetBomTable(Index, BomTableName, Columns)
```

```

System.int SetBomTable( 
   System.int Index,
   System.string BomTableName,
   System.object Columns
)
```

```

System.int SetBomTable( 
   System.int Index,
   System.String^ BomTableName,
   System.Object^ Columns
) 
```

#### Parameters

*Index*
:   0-based index of the BOM Table Area in the theme (see **Remarks**)

*BomTableName*
:   Name of the BOM table to map to the BOM Table Area specified by Index (see **Remarks**)

*Columns*
:   Array of strings of the names of the columns to export from the BOM table specified in BomTableName (see **Remarks**)

#### Return Value

0 = success; BOM table mapped

1 = failure; specified BomTableName not found in model

Remarks

| To get... | Call... |
| --- | --- |
| Index | [IMBD3PdfData::GetBomAreaCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~GetBomAreaCount.md) to find out the number of BOM Table Areas in the theme |
| BOMTableName | [IBomFeature::Name](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~Name.md) |
| Columns | - [ITableAnnotation::ColumnCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~ColumnCount.md) to get the number of columns in the BOM table - [ITableAnnotation::GetColumnTitle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnTitle.md) for each column you want to export after getting the [table annotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md) for the [BOM table annotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.md) |

Example

[Export BOM's Second Column to BOM Table Area (C#)](Export_BOM's_Second_Column_to_BOM_Table_Area_Example_CSharp.htm)  
[Export BOM's Second Column to BOM Table Area (VB.NET)](Export_BOM's_Second_Column_to_BOM_Table_Area_Example_VBNET.htm)  
[Export BOM's Second Column to BOM Table Area (VBA)](Export_BOM's_Second_Column_to_BOM_Table_Area_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMBD3DPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.md)  
[IMBD3DPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData_members.md)  
[IMBD3DPdfData::ExcludeFromAnnotationView Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~ExcludeFromAnnotationView.md)
