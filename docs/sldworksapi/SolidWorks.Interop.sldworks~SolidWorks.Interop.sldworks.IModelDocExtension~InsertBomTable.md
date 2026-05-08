# InsertBomTable Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertBomTable`

Obsolete. Superseded by IModelDocExtension::InsertBomTable2.
Obsolete. Superseded by [IModelDocExtension::InsertBomTable2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertBomTable2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertBomTable( _
   ByVal TemplateName As System.String, _
   ByVal X As System.Integer, _
   ByVal Y As System.Integer, _
   ByVal BomType As System.Integer, _
   ByVal ConfigurationName As System.String _
) As BomTableAnnotation
```

```

Dim instance As IModelDocExtension
Dim TemplateName As System.String
Dim X As System.Integer
Dim Y As System.Integer
Dim BomType As System.Integer
Dim ConfigurationName As System.String
Dim value As BomTableAnnotation
 
value = instance.InsertBomTable(TemplateName, X, Y, BomType, ConfigurationName)
```

```

BomTableAnnotation InsertBomTable( 
   System.string TemplateName,
   System.int X,
   System.int Y,
   System.int BomType,
   System.string ConfigurationName
)
```

```

BomTableAnnotation^ InsertBomTable( 
   System.String^ TemplateName,
   System.int X,
   System.int Y,
   System.int BomType,
   System.String^ ConfigurationName
) 
```

#### Parameters

*TemplateName*
:   Path and name of BOM table template (see **Remarks**)

*X*
:   X coordinate for the placement of the BOM table

*Y*
:   Y coordinate for the placement of the BOM table

*BomType*
:   Type of BOM table as defined by [swBomType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBomType_e.html)

*ConfigurationName*
:   Name of the configuration for this BOM table (see Remarks)

#### Return Value

[BOM table annotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.md)

Remarks

The system will not default to the default configuration when you specify an empty string for Configuration. You must specify the configuration.

By default, the BOM table templates are in the <install\_dir>\lang\<language> folder and have a filename extension of .sldbomtbt. The template and table must be of the same type. For example, you could specify C:\Program Files\SOLIDWORKS\lang\English\bom-standard.sldbomtbt for TemplateName if you wanted to insert an English-version of the standard BOM table template.

If the BOM table is a parts-only or indented-style BOM and ConfigurationName is invalid, then the BOM is not created.

Example

[Insert BOM Table and Stacked Balloon (VB.NET)](Insert_BOM_Table_and_Stacked_Balloon_Example_VBNET.htm)  
[Insert BOM Table and Stacked Balloon (VBA)](Insert_BOM_Table_and_Stacked_Balloon_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IView::InsertBomTable2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable2.md)
