# InsertTableAnnotation2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertTableAnnotation2`

Inserts a table annotation in this drawing.
Inserts a table annotation in this drawing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertTableAnnotation2( _
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

Dim instance As IDrawingDoc
Dim UseAnchorPoint As System.Boolean
Dim X As System.Double
Dim Y As System.Double
Dim AnchorType As System.Integer
Dim TableTemplate As System.String
Dim Rows As System.Integer
Dim Columns As System.Integer
Dim value As TableAnnotation
 
value = instance.InsertTableAnnotation2(UseAnchorPoint, X, Y, AnchorType, TableTemplate, Rows, Columns)
```

```

TableAnnotation InsertTableAnnotation2( 
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

TableAnnotation^ InsertTableAnnotation2( 
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
:   True to anchor the table to the general table anchor point and ignore any coordinates specified for X and Y, or false to use the coordinates specified for X and Y

*X*
:   X coordinate to insert this table annotation

*Y*
:   Y coordinate to insert this table annotation

*AnchorType*
:   Type of anchor as defined in [swBOMConfigurationAnchorType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBOMConfigurationAnchorType_e.html) (see **Remarks**)

*TableTemplate*
:   Path and filename of the general table template to use  (see Remarks)

*Rows*
:   Number of rows in the table annotation

*Columns*
:   Number of columns in the table annotation

#### Return Value

Pointer to the [ITableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md) object

Remarks

|  |  |
| --- | --- |
| **If TableTemplate is...** | **Then..** |
| A valid path and filename | AnchorType and Columns are ignored, and the information from the table template is used instead |
| Empty | General table is inserted based only on the other input arguments |

Example

[Insert General Table (VBA)](Insert_General_Table_Example_VB.htm)  
[Get General Table Feature (C#)](Get_General_Table_Feature_Example_CSharp.htm)  
[Get General Table Feature (VB.NET)](Get_General_Table_Feature_Example_VBNET.htm)  
[Get General Table Feature (VBA)](Get_General_Table_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IModelDocExtension::InsertGeneralTableAnnotation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertGeneralTableAnnotation.md)
