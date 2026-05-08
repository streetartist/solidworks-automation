# InsertRevisionTable Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~InsertRevisionTable`

Obsolete. Superseded by ISheet::InsertRevisionTable2.
Obsolete. Superseded by [ISheet::InsertRevisionTable2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~InsertRevisionTable2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertRevisionTable( _
   ByVal UseAnchorPoint As System.Boolean, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal AnchorType As System.Integer, _
   ByVal TableTemplate As System.String _
) As RevisionTableAnnotation
```

```

Dim instance As ISheet
Dim UseAnchorPoint As System.Boolean
Dim X As System.Double
Dim Y As System.Double
Dim AnchorType As System.Integer
Dim TableTemplate As System.String
Dim value As RevisionTableAnnotation
 
value = instance.InsertRevisionTable(UseAnchorPoint, X, Y, AnchorType, TableTemplate)
```

```

RevisionTableAnnotation InsertRevisionTable( 
   System.bool UseAnchorPoint,
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.string TableTemplate
)
```

```

RevisionTableAnnotation^ InsertRevisionTable( 
   System.bool UseAnchorPoint,
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.String^ TableTemplate
) 
```

#### Parameters

*UseAnchorPoint*
:   If true and the appropriate sheet format anchor point exists, then insert table at this point; if false, then use the values specified for the X and Y arguments as the insertion point

*X*
:   X coordinate for the placement of the revision table annotation

*Y*
:   Y coordinate for the placement of this revision table annotation

*AnchorType*
:   Anchor type as defined by [swBOMConfigurationAnchorType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBOMConfigurationAnchorType_e.html)

*TableTemplate*
:   Path and filename of the template that you want to use that corresponds to this type of table (see **Remarks**)

#### Return Value

[Revision table](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation.md) or null if a revision table on the sheet already exists

Remarks

By default, the revision table templates are in the <install\_dir>\lang\<language> folder and have a filename extension of .sldrevtbt. The template and table must be of the same type. For example, you would specify C:\Program Files\SOLIDWORKS\lang\English\standard revision block.sldrevtbt for TableTemplate if you wanted to insert an English-version of the revision block table template.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)  
[ISheet::RevisionTable Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~RevisionTable.md)
