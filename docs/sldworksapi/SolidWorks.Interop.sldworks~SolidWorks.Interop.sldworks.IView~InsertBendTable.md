# InsertBendTable Method (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBendTable`

Inserts a bend table for this drawing view.
Inserts a bend table for this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertBendTable( _
   ByVal UseAnchorPoint As System.Boolean, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal AnchorType As System.Integer, _
   ByVal StartValue As System.String, _
   ByVal TableTemplate As System.String _
) As BendTableAnnotation
```

```

Dim instance As IView
Dim UseAnchorPoint As System.Boolean
Dim X As System.Double
Dim Y As System.Double
Dim AnchorType As System.Integer
Dim StartValue As System.String
Dim TableTemplate As System.String
Dim value As BendTableAnnotation
 
value = instance.InsertBendTable(UseAnchorPoint, X, Y, AnchorType, StartValue, TableTemplate)
```

```

BendTableAnnotation InsertBendTable( 
   System.bool UseAnchorPoint,
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.string StartValue,
   System.string TableTemplate
)
```

```

BendTableAnnotation^ InsertBendTable( 
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
:   True to insert the bend table at the sheet format anchor point, false to insert it at the point specified by the X and Y parameters of this method

*X*
:   X-coordinate for placement of the bend table; valid only when UseAnchorPoint is false

*Y*
:   Y-coordinate for placement of the bend table; valid only when UseAnchorPoint is false

*AnchorType*
:   Anchor type as defined in [swBomConfigurationAnchorType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBomConfigurationAnchorType_e.html)

*StartValue*
:   Starting datum tag; a value from A to Z for letter tags; a positive integer for number tags

*TableTemplate*
:   Full pathname of the template (e.g., *install\_dir*\**lang\***language**\*****bendtable-standard.sldbndtbt**)

#### Return Value

[IBendTableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTableAnnotation.md)

Example

[Insert Bend Table (VBA)](Insert_Bend_Table_Example_VB.htm)  
[Insert Bend Table (VB.NET)](Insert_Bend_Table_Example_VBNET.htm)  
[Insert Bend Table (C#)](Insert_Bend_Table_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IBendTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable.md)  
[IPartDoc::InsertBendTable Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~InsertBendTable.md)
