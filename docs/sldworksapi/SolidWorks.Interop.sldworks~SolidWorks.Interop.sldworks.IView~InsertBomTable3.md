# InsertBomTable3 Method (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable3`

Obsolete. Superseded by IView::InsertBomTable4.
Obsolete. Superseded by [IView::InsertBomTable4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable4.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertBomTable3( _
   ByVal UseAnchorPoint As System.Boolean, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal AnchorType As System.Integer, _
   ByVal BomType As System.Integer, _
   ByVal Configuration As System.String, _
   ByVal TableTemplate As System.String, _
   ByVal Hidden As System.Boolean _
) As BomTableAnnotation
```

```

Dim instance As IView
Dim UseAnchorPoint As System.Boolean
Dim X As System.Double
Dim Y As System.Double
Dim AnchorType As System.Integer
Dim BomType As System.Integer
Dim Configuration As System.String
Dim TableTemplate As System.String
Dim Hidden As System.Boolean
Dim value As BomTableAnnotation
 
value = instance.InsertBomTable3(UseAnchorPoint, X, Y, AnchorType, BomType, Configuration, TableTemplate, Hidden)
```

```

BomTableAnnotation InsertBomTable3( 
   System.bool UseAnchorPoint,
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.int BomType,
   System.string Configuration,
   System.string TableTemplate,
   System.bool Hidden
)
```

```

BomTableAnnotation^ InsertBomTable3( 
   System.bool UseAnchorPoint,
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.int BomType,
   System.String^ Configuration,
   System.String^ TableTemplate,
   System.bool Hidden
) 
```

#### Parameters

*UseAnchorPoint*
:   If true and the appropriate sheet format anchor point exists, then insert table at this point; if false, then use the values specified for the X and Y arguments as the insertion point

*X*
:   X coordinate for the placement of the BOM table

*Y*
:   Y coordinate for the placement of the BOM table

*AnchorType*
:   Anchor type as defined by [swBomConfigurationAnchorType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBOMConfigurationAnchorType_e.html)

*BomType*
:   Type of BOM table as defined by [swBomType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBomType_e.html)

*Configuration*
:   Name of the configuration for this BOM table (see Remarks)

*TableTemplate*
:   Path and filename of the template that you want to use that corresponds to this type of table (see Remarks)

*Hidden*
:   True to hide the BOM table, false to show it

#### Return Value

[BOM table annotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.md)

Remarks

If BomType is swBomType\_TopLevelOnly, then do not specify Configuration. Instead, use [IBomFeature::GetConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~GetConfigurations.md) or [IBomFeature::IGetConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~IGetConfigurations.md) and [IBomFeature::SetConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~SetConfigurations.md) or [IBomFeature::ISetConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~ISetConfigurations.md) to work with configurations in BOM tables.

If the drawing was created using a configuration other than the Default configuration, then the configuration active at the time the drawing was created is the configuration used in the BOM table when an empty string is specified for the Configuration parameter.

BOM table templates are in the install\_dir\lang\<language> folder and have a filename extension of .sldbomtbt. The template and table must be of the same type. For example, you could specify C:\Program Files\SOLIDWORKS\lang\English\bom-standard.sldbomtbt for TableTemplate if you wanted to insert an English-version of the standard BOM table template.

If the BOM table is a parts-only or indented-style BOM and the Configuration specified is invalid, then the BOM is not created.

NOTE: Use [IView::InsertBomTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable.md) or [IView::IInsertBomTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IInsertBomTable.md) to insert a BOM using Microsoft Excel.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetKeepLinkedToBOM Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetKeepLinkedToBOM.md)  
[IView::GetKeepLinkedToBOMName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetKeepLinkedToBOMName.md)  
[IView::SetKeepLinkedToBOM Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetKeepLinkedToBOM.md)  
[IModelDocExtension::InsertBomTable2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertBomTable2.md)
