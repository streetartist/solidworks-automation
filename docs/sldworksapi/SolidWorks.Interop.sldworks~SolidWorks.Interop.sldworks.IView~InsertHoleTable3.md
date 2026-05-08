# InsertHoleTable3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertHoleTable3`

Inserts a hole table in this drawing view.
Inserts a hole table in this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertHoleTable3( _
   ByVal UseAnchorPoint As System.Boolean, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal AnchorType As System.Integer, _
   ByVal StartValue As System.String, _
   ByVal Template As System.String, _
   ByVal TagOrder As System.Integer, _
   ByVal TagType As System.Integer, _
   ByVal ManualTags As System.Object _
) As System.Object
```

```

Dim instance As IView
Dim UseAnchorPoint As System.Boolean
Dim X As System.Double
Dim Y As System.Double
Dim AnchorType As System.Integer
Dim StartValue As System.String
Dim Template As System.String
Dim TagOrder As System.Integer
Dim TagType As System.Integer
Dim ManualTags As System.Object
Dim value As System.Object
 
value = instance.InsertHoleTable3(UseAnchorPoint, X, Y, AnchorType, StartValue, Template, TagOrder, TagType, ManualTags)
```

```

System.object InsertHoleTable3( 
   System.bool UseAnchorPoint,
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.string StartValue,
   System.string Template,
   System.int TagOrder,
   System.int TagType,
   System.object ManualTags
)
```

```

System.Object^ InsertHoleTable3( 
   System.bool UseAnchorPoint,
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.String^ StartValue,
   System.String^ Template,
   System.int TagOrder,
   System.int TagType,
   System.Object^ ManualTags
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
:   Starting value for the specified TagType

*Template*
:   Path and filename of the hole table template that corresponds to the hole table you want to create (see Remarks)

*TagOrder*
:   Tag numbering as defined in [swHoleTableTagOrder\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHoleTableTagOrder_e.html)

*TagType*
:   Tag type as defined in [swHoleTableTagStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHoleTableTagStyle_e.html)

*ManualTags*
:   Array of custom tags; valid only if TagType is swHoleTableTagStyle\_e.swHoleTable\_ManualTags

#### Return Value

[Hole table annotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTableAnnotation.md)

Remarks

This method inserts a hole table with the following information for selected holes:

- Datum tag
- X-location of hole center
- Y-location of hole center
- Size of the hole

This method displays datum tags next to holes that have been pre-selected in the view. The location of the datum tags is relative to a datum origin that is also pre-selected in the view.

Before calling this method, call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select the datum origin, hole edges, and faces (for multiple holes) as follows:

|  |  |
| --- | --- |
| **Selection** | **Mark** |
| Datum origin vertex | 1 |
| Hole edges and faces | 2 |
| Datum origin x axis direction reference | 4 |
| Datum origin y axis direction reference | 8 |

Specify Template using a hole table template (**\*.sldholtbt**):

- in install\_dir\lang\*language*.
- that matches the table you want to create. For example, to insert a hole table with letter tags, specify Template using *install\_dir*\lang\English\standard hole table--letters.sldholtbt.

Example

[Insert Hole Table (VBA)](Insert_Hole_Table_Example_VB.htm)  
[Insert Hole Table (VB.NET)](Insert_Hole_Table_Example_VBNET.htm)  
[Insert Hole Table (C#)](Insert_Hole_Table_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)
