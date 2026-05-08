# InsertHoleTable Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertHoleTable`

Obsolete. Superseded by IView::InsertHoleTable2.
Obsolete. Superseded by [IView::InsertHoleTable2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertHoleTable2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertHoleTable( _
   ByVal UseAnchorPoint As System.Boolean, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal AnchorType As System.Integer, _
   ByVal TableTemplate As System.String _
) As HoleTableAnnotation
```

```

Dim instance As IView
Dim UseAnchorPoint As System.Boolean
Dim X As System.Double
Dim Y As System.Double
Dim AnchorType As System.Integer
Dim TableTemplate As System.String
Dim value As HoleTableAnnotation
 
value = instance.InsertHoleTable(UseAnchorPoint, X, Y, AnchorType, TableTemplate)
```

```

HoleTableAnnotation InsertHoleTable( 
   System.bool UseAnchorPoint,
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.string TableTemplate
)
```

```

HoleTableAnnotation^ InsertHoleTable( 
   System.bool UseAnchorPoint,
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.String^ TableTemplate
) 
```

#### Parameters

*UseAnchorPoint*
:   If True and the appropriate sheet format anchor point exists, then insert table at this point; if false, then use the values specified for the X and Y arguments as the insertion point

*X*
:   X coordinate for the placement of this hole table

*Y*
:   Y coordinate for the placement of this hole table

*AnchorType*
:   Anchor type as defined by [swBomConfigurationAnchorType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBOMConfigurationAnchorType_e.html)

*TableTemplate*
:   Path and filename of the template that you want to use that corresponds to this type of table (see Remarks)

#### Return Value

[Hole table annotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTableAnnotation.md)

Remarks

This method requires ordered preselection of various entities:

- datum = 1
- hole = 2
- x axis = 4
- y axis = 8

See [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) for details.

By default, the hole table templates are in the <install\_dir>\lang\<language> folder and have a filename extension of .sldholtbt. The template and table must be of the same type. For example, you could specify C:\Program Files\SOLIDWORKS\lang\English\standard hole table--letters.sldholetbt for TableTemplate if you wanted to insert an English-version of the standard hole letters table template.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)
