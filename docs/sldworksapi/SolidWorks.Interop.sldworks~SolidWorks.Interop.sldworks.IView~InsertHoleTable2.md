# InsertHoleTable2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertHoleTable2`

Obsolete. Superseded by IView::InsertHoleTable3.
Obsolete. Superseded by [IView::InsertHoleTable3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertHoleTable3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertHoleTable2( _
   ByVal UseAnchorPoint As System.Boolean, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal AnchorType As System.Integer, _
   ByVal StartValue As System.String, _
   ByVal TableTemplate As System.String _
) As HoleTableAnnotation
```

```

Dim instance As IView
Dim UseAnchorPoint As System.Boolean
Dim X As System.Double
Dim Y As System.Double
Dim AnchorType As System.Integer
Dim StartValue As System.String
Dim TableTemplate As System.String
Dim value As HoleTableAnnotation
 
value = instance.InsertHoleTable2(UseAnchorPoint, X, Y, AnchorType, StartValue, TableTemplate)
```

```

HoleTableAnnotation InsertHoleTable2( 
   System.bool UseAnchorPoint,
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.string StartValue,
   System.string TableTemplate
)
```

```

HoleTableAnnotation^ InsertHoleTable2( 
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
:   X coordinate in meters for the anchor of this hole table

*Y*
:   Y coordinate in meters for the anchor of this hole table

*AnchorType*
:   Anchor type as defined by [swBomConfigurationAnchorType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBOMConfigurationAnchorType_e.html)

*StartValue*
:   Starting value for datum tags; a letter from A to Z, if TableTemplate uses letter tags; a positive integer, if TableTemplate uses number tags (see **Remarks**)

*TableTemplate*
:   Path and filename of the table template that corresponds to the table you want to use (see Remarks)

#### Return Value

[Hole table annotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTableAnnotation.md)

Remarks

This method inserts a table with the following information for selected holes:

- Datum tag
- X-location of hole center
- Y-location of hole center
- Size

This method displays datum tags next to holes that have been pre-selected in the view. The location of the datum tags is relative to a datum origin that is also pre-selected in the view.

Before calling this method, call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select the datum origin, hole edges, and faces (for multiple holes) as follows:

|  |  |
| --- | --- |
| **Selection** | **Mark** |
| Datum origin vertex | 1 |
| Hole edges and faces | 2 |
| Datum origin x axis direction reference | 4 |
| Datum origin y axis direction reference | 8 |

Specify TableTemplate using a hole table template (**\*.sldholtbt**) in install\_dir\lang\*language*.

Specify a TableTemplate and StartValue that matches the table you want to create. For example, to insert a hole table with letter tags, specify TableTemplate using *install\_dir*\lang\English\standard hole table--letters.sldholtbt and specify StartValue using a letter from A to Z.

Example

[Get Labels of Datum Origin (C#)](Get_Labels_of_Datum_Origin_Example_CSharp.htm)  
[Get Labels of Datum Origin (VB.NET)](Get_Labels_of_Datum_Origin_Example_VBNET.htm)  
[Get Labels of Datum Origin (VBA)](Get_Labels_of_Datum_Origin_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)
