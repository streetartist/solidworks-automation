# InsertGeneralTableAnnotation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertGeneralTableAnnotation`

Inserts the a general table annotation in this model document.
Inserts the a general table annotation in this model document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertGeneralTableAnnotation( _
   ByVal UseAnchorPoint As System.Boolean, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal AnchorType As System.Integer, _
   ByVal TableTemplate As System.String, _
   ByVal Rows As System.Integer, _
   ByVal Columns As System.Integer _
) As TableAnnotation
```

```

Dim instance As IModelDocExtension
Dim UseAnchorPoint As System.Boolean
Dim X As System.Double
Dim Y As System.Double
Dim AnchorType As System.Integer
Dim TableTemplate As System.String
Dim Rows As System.Integer
Dim Columns As System.Integer
Dim value As TableAnnotation
 
value = instance.InsertGeneralTableAnnotation(UseAnchorPoint, X, Y, AnchorType, TableTemplate, Rows, Columns)
```

```

TableAnnotation InsertGeneralTableAnnotation( 
   System.bool UseAnchorPoint,
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.string TableTemplate,
   System.int Rows,
   System.int Columns
)
```

```

TableAnnotation^ InsertGeneralTableAnnotation( 
   System.bool UseAnchorPoint,
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.String^ TableTemplate,
   System.int Rows,
   System.int Columns
) 
```

#### Parameters

*UseAnchorPoint*
:   True to anchor the table by AnchorType and ignore any coordinates specified by X and Y, false to use the coordinates specified by X and Y

*X*
:   X coordinate of this table annotation

*Y*
:   Y coordinate of this table annotation

*AnchorType*
:   Type of anchor as defined in [swBOMConfigurationAnchorType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBOMConfigurationAnchorType_e.html); valid only if UseAnchorPoint is true and TableTemplate is empty (see **Remarks**)

*TableTemplate*
:   Path and file name of the general table template to use (see Remarks)

*Rows*
:   Number of rows in the table annotation; valid only if TableTemplate is empty (see **Remarks**)

*Columns*
:   Number of columns in the table annotation; valid only if TableTemplate is empty (see **Remarks**)

#### Return Value

[ITableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)

Remarks

|  |  |
| --- | --- |
| **If TableTemplate is...** | **Then..** |
| A valid path and file name | AnchorType, Rows, and Columns are ignored, and a general table based on TableTemplate is inserted |
| Empty | General table based only on all of the specified parameters, except TableTemplate, is inserted |

Example

[Insert General Table in Part (VBA)](Insert_General_Table_in_Part_Example_VB.htm)  
[Insert General Table in Part (VB.NET)](Insert_General_Table_in_Part_Example_VBNET.htm)  
[Insert General Table in Part (C#)](Insert_General_Table_in_Part_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IDrawingDoc::InsertTableAnnotation2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertTableAnnotation2.md)  
[IModelDocExtension::InsertBomTable3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertBomTable3.md)  
[IModelDocExtension::InsertTitleBlockTable Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertTitleBlockTable.md)  
[IModelDocExtension::GetGeneralTableAnnotation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetGeneralTableAnnotation.md)
