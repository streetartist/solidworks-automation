# InsertBomTable2 Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertBomTable2`

Obsolete. Superseded by IModelDocExtension::InsertBomTable3.
Obsolete. Superseded by [IModelDocExtension::InsertBomTable3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertBomTable3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertBomTable2( _
   ByVal TemplateName As System.String, _
   ByVal X As System.Integer, _
   ByVal Y As System.Integer, _
   ByVal BomType As System.Integer, _
   ByVal ConfigurationName As System.String, _
   ByVal Hidden As System.Boolean _
) As BomTableAnnotation
```

```

Dim instance As IModelDocExtension
Dim TemplateName As System.String
Dim X As System.Integer
Dim Y As System.Integer
Dim BomType As System.Integer
Dim ConfigurationName As System.String
Dim Hidden As System.Boolean
Dim value As BomTableAnnotation
 
value = instance.InsertBomTable2(TemplateName, X, Y, BomType, ConfigurationName, Hidden)
```

```

BomTableAnnotation InsertBomTable2( 
   System.string TemplateName,
   System.int X,
   System.int Y,
   System.int BomType,
   System.string ConfigurationName,
   System.bool Hidden
)
```

```

BomTableAnnotation^ InsertBomTable2( 
   System.String^ TemplateName,
   System.int X,
   System.int Y,
   System.int BomType,
   System.String^ ConfigurationName,
   System.bool Hidden
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

*Hidden*
:   True to hide the BOM table, false to show it

#### Return Value

[BOM table annotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.md)

Remarks

The system does not default to the Default configuration when you specify an empty string for Configuration. You must specify the configuration.

BOM table templates are in the <*SOLIDWORKS\_*install\_dir>\lang\<language> folder and have a filename extension of .sldbomtbt. The template and table must be of the same type. For example, you could specify C:\Program Files\SOLIDWORKS\lang\English\bom-standard.sldbomtbt for TemplateName if you wanted to insert an English-version of the standard BOM table template.

If the BOM table is a parts-only or indented-style BOM and ConfigurationName is invalid, then the BOM is not created.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IView::InsertBomTable3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable3.md)
