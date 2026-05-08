# InsertWeldTable Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertWeldTable`

Inserts a weld table into this drawing view.
Inserts a weld table into this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertWeldTable( _
   ByVal UseAnchorPoint As System.Boolean, _
   ByVal IncludeAnnotations As System.Boolean, _
   ByVal CombineSameType As System.Boolean, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal AnchorType As System.Integer, _
   ByVal Configuration As System.String, _
   ByVal TableTemplate As System.String _
) As System.Boolean
```

```

Dim instance As IView
Dim UseAnchorPoint As System.Boolean
Dim IncludeAnnotations As System.Boolean
Dim CombineSameType As System.Boolean
Dim X As System.Double
Dim Y As System.Double
Dim AnchorType As System.Integer
Dim Configuration As System.String
Dim TableTemplate As System.String
Dim value As System.Boolean
 
value = instance.InsertWeldTable(UseAnchorPoint, IncludeAnnotations, CombineSameType, X, Y, AnchorType, Configuration, TableTemplate)
```

```

System.bool InsertWeldTable( 
   System.bool UseAnchorPoint,
   System.bool IncludeAnnotations,
   System.bool CombineSameType,
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.string Configuration,
   System.string TableTemplate
)
```

```

System.bool InsertWeldTable( 
   System.bool UseAnchorPoint,
   System.bool IncludeAnnotations,
   System.bool CombineSameType,
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.String^ Configuration,
   System.String^ TableTemplate
) 
```

#### Parameters

*UseAnchorPoint*
:   If true and the appropriate sheet format anchor point exists, then insert the table at the anchor point; if false, then use the values specified for the X and Y arguments as the insertion point

*IncludeAnnotations*
:   True to include weld symbols not attached to cosmetic weld features, false to not

*CombineSameType*
:   True to group welds having the same weld symbol and weld size, false to not

*X*
:   X coordinate in meters for the placement of the weld table; valid only if UseAnchorPoint = False

*Y*
:   Y coordinate in meters for the placement of the weld table; valid only if UseAnchorPoint = False

*AnchorType*
:   Anchor type as defined by [swBomConfigurationAnchorType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBOMConfigurationAnchorType_e.html)

*Configuration*
:   Name of the part configuration for which to insert the weld table

*TableTemplate*
:   Path and filename of the template that corresponds to this type of table (see Remarks)

#### Return Value

True if successful, false if not

Remarks

The weld table template installed with SOLIDWORKS is <*SOLIDWORKS\_*install\_dir>\lang\<language>\**weldtable-standard.sldwldtbt**.

Example

[Insert Weld Table (VBA)](Insert_Weld_Table_Example_VB.htm)  
[Insert Weld Table (VB.NET)](Insert_Weld_Table_Example_VBNET.htm)  
[Insert Weld Table (C#)](Insert_Weld_Table_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)
