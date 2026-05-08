# InsertPunchTable Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertPunchTable`

Inserts a punch table in the flat pattern drawing view of a sheet metal part.
Inserts a punch table in the flat pattern drawing view of a sheet metal part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertPunchTable( _
   ByVal UseAnchorPoint As System.Boolean, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal AnchorType As System.Integer, _
   ByVal StartValue As System.String, _
   ByVal TableTemplate As System.String _
) As PunchTableAnnotation
```

```

Dim instance As IView
Dim UseAnchorPoint As System.Boolean
Dim X As System.Double
Dim Y As System.Double
Dim AnchorType As System.Integer
Dim StartValue As System.String
Dim TableTemplate As System.String
Dim value As PunchTableAnnotation
 
value = instance.InsertPunchTable(UseAnchorPoint, X, Y, AnchorType, StartValue, TableTemplate)
```

```

PunchTableAnnotation InsertPunchTable( 
   System.bool UseAnchorPoint,
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.string StartValue,
   System.string TableTemplate
)
```

```

PunchTableAnnotation^ InsertPunchTable( 
   System.bool UseAnchorPoint,
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.String^ StartValue,
   System.String^ TableTemplate
) 
```

#### Parameters

*UseAnchorPoint*
:   If true, and the sheet format anchor point exists, then insert table at the anchor point; if false, then insert the table at the location specified by the X and Y parameters

*X*
:   X coordinate for the anchor of this punch table

*Y*
:   Y coordinate for the anchor of this punch table

*AnchorType*
:   Anchor type as defined by [swBomConfigurationAnchorType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBOMConfigurationAnchorType_e.html)

*StartValue*
:   Starting value for datum tags; a letter from A to Z, if TableTemplate uses letter tags; a positive integer, if TableTemplate uses number tags (see **Remarks**)

*TableTemplate*
:   Path and filename of the table template that corresponds to the type of table you want to use (see Remarks)

#### Return Value

[IPunchTableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTableAnnotation.md)

Remarks

Punch tables contain information about the punches that are created by forming tools in sheet metal parts. This method inserts a punch table with the following information for pre-selected punches:

| Column | Description |
| --- | --- |
| TAG | Datum tag added to each punch in the flat pattern view |
| PUNCH ID | Property of the forming tool or library feature |
| X Location | Distance from the x-axis to the point of insertion of the forming tool in the flat pattern view |
| Y Location | Distance from the y-axis to the point of insertion of the forming tool in the flat pattern view |
| ANGLE | Angle between the x-axis and the forming tool |
| QUANTITY | Number of times that the punch occurs in the flat pattern view |

The locations of the datum tags are relative to a datum origin that is pre-selected in the view.

Before calling this method, call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select the datum origin, punch edges, and punch faces (for multiple punches) as follows:

| **Selection** | **Mark** |
| --- | --- |
| Datum origin vertex | 1 |
| Punch edges and faces | 2 |
| Datum origin x-axis direction reference | 4 |
| Datum origin y-axis direction reference | 8 |

Specify TableTemplate using a punch table template (**\*.sldpuntbt**) in install\_dir\lang\*language*.

Specify a StartValue that matches the table you want to create. For example, to insert a punch table with letter tags, specify a StartValue with a letter from A to Z.

Example

[Insert Punch Table (VBA)](Insert_Punch_Table_Example_VB.htm)  
[Insert Punch Table (VB.NET)](Insert_Punch_Table_Example_VBNET.htm)  
[Insert Punch Table (C#)](Insert_Punch_Table_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IPunchTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable.md)  
[IFeatureManager::CreateFormTool Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFormTool.md)  
[ILibraryFormToolFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData.md)
