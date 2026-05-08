# InsertBomTable6 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable6`

Inserts a bill of materials (BOM) table for this drawing view using SOLIDWORKS table functionality.
Inserts a bill of materials (BOM) table for this drawing view using SOLIDWORKS table functionality.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertBomTable6( _
   ByVal UseAnchorPoint As System.Boolean, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal AnchorType As System.Integer, _
   ByVal BomType As System.Integer, _
   ByVal Configuration As System.String, _
   ByVal TableTemplate As System.String, _
   ByVal Hidden As System.Boolean, _
   ByVal IndentedNumberingType As System.Integer, _
   ByVal DetailedCutList As System.Boolean, _
   ByVal DissolvePartLevelRows As System.Boolean, _
   ByVal DisplayAsOneItem As System.Boolean _
) As System.Object
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
Dim IndentedNumberingType As System.Integer
Dim DetailedCutList As System.Boolean
Dim DissolvePartLevelRows As System.Boolean
Dim DisplayAsOneItem As System.Boolean
Dim value As System.Object
 
value = instance.InsertBomTable6(UseAnchorPoint, X, Y, AnchorType, BomType, Configuration, TableTemplate, Hidden, IndentedNumberingType, DetailedCutList, DissolvePartLevelRows, DisplayAsOneItem)
```

```

System.object InsertBomTable6( 
   System.bool UseAnchorPoint,
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.int BomType,
   System.string Configuration,
   System.string TableTemplate,
   System.bool Hidden,
   System.int IndentedNumberingType,
   System.bool DetailedCutList,
   System.bool DissolvePartLevelRows,
   System.bool DisplayAsOneItem
)
```

```

System.Object^ InsertBomTable6( 
   System.bool UseAnchorPoint,
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.int BomType,
   System.String^ Configuration,
   System.String^ TableTemplate,
   System.bool Hidden,
   System.int IndentedNumberingType,
   System.bool DetailedCutList,
   System.bool DissolvePartLevelRows,
   System.bool DisplayAsOneItem
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

*IndentedNumberingType*
:   Type of numbering as defined by [swNumberingType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swNumberingType_e.html); valid only for BomType = swBomType\_e.swBomType\_Indented

*DetailedCutList*
:   True to show the detailed cut list, false to not

*DissolvePartLevelRows*
:   True to dissolve part level rows, false to not; valid only when DetailedCutList is true

*DisplayAsOneItem*
:   True to group into one item number, false to display separately

#### Return Value

[BOM table annotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.md)

Remarks

If BomType is swBomType\_TopLevelOnly, then do not specify Configuration. Instead, use [IBomFeature::GetConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~GetConfigurations.md) and [IBomFeature::SetConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~SetConfigurations.md) to work with configurations in BOM tables.

If the drawing was created using a configuration other than the Default configuration, then the configuration active at the time the drawing was created is the configuration used in the BOM table when an empty string is specified for the Configuration parameter.

BOM table templates are in the install\_dir\lang\<language> folder and have a filename extension of .sldbomtbt. The template and table must be of the same type. For example, you could specify C:\Program Files\SOLIDWORKS\lang\English\bom-standard.sldbomtbt for TableTemplate if you wanted to insert an English-version of the standard BOM table template.

If the BOM table is a parts-only or indented-style BOM and the Configuration specified is invalid, then the BOM is not created.

If the **Restrict top-level only BOMs to one configuration** option on the **Document Properties > Tables > Bill of Materials** dialog or [IModelDocExtension::GetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceToggle.md)([swUserPreferenceToggle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceToggle_e.html).swOneConfigOnlyTopLevelBom) returns true, then only the active or default configuration of the drawing view is inserted in the BOM.

NOTE: Use [IView::InsertBomTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable.md) to insert a BOM using Microsoft Excel.

Example

[Dissolve Subassembly in a BOM Table (VBA)](Dissolve_Subassembly_in_a_BOM_Table_Example_VB.htm)  
[Dissolve Subassembly in a BOM Table (VB.NET)](Dissolve_Subassembly_in_a_BOM_Table_Example_VBNET.htm)  
[Dissolve Subassembly in a BOM Table (C#)](Dissolve_Subassembly_in_a_BOM_Table_Example_CSharp.htm)  
[Insert and Show BOM Table and BOM Balloon (VBA)](Insert_and_Show_BOM_Table_and_BOM_Balloon_Example_VB.htm)  
[Insert and Show BOM Table and BOM Balloon (VB.NET)](Insert_and_Show_BOM_Table_and_BOM_Balloon_Example_VBNET.htm)  
[Insert and Show BOM Table and BOM Balloon (C#)](Insert_and_Show_BOM_Table_and_BOM_Balloon_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IModelDocExtension::InsertBomTable4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertBomTable4.md)  
[IBomFeature::DissolvePartLevelRows Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~DissolvePartLevelRows.md)  
[IBomFeature::NumberingTypeOnIndentedBOM Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~NumberingTypeOnIndentedBOM.md)  
[IView::GetKeepLinkedToBOM Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetKeepLinkedToBOM.md)  
[IView::GetKeepLinkedToBOMName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetKeepLinkedToBOMName.md)  
[IView::SetKeepLinkedToBOM Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetKeepLinkedToBOM.md)
