# InsertWeldmentTable Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertWeldmentTable`

Inserts a weldment cut-list table into this drawing view.
Inserts a weldment cut-list table into this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertWeldmentTable( _
   ByVal UseAnchorPoint As System.Boolean, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal AnchorType As System.Integer, _
   ByVal Configuration As System.String, _
   ByVal TableTemplate As System.String _
) As WeldmentCutListAnnotation
```

```

Dim instance As IView
Dim UseAnchorPoint As System.Boolean
Dim X As System.Double
Dim Y As System.Double
Dim AnchorType As System.Integer
Dim Configuration As System.String
Dim TableTemplate As System.String
Dim value As WeldmentCutListAnnotation
 
value = instance.InsertWeldmentTable(UseAnchorPoint, X, Y, AnchorType, Configuration, TableTemplate)
```

```

WeldmentCutListAnnotation InsertWeldmentTable( 
   System.bool UseAnchorPoint,
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.string Configuration,
   System.string TableTemplate
)
```

```

WeldmentCutListAnnotation^ InsertWeldmentTable( 
   System.bool UseAnchorPoint,
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.String^ Configuration,
   System.String^ TableTemplate
) 
```

#### Parameters

*UseAnchorPoint*
:   If true and the appropriate sheet format anchor point exists, then insert table at this point; if false, then use the values specified for the X and Y arguments as the insertion point

*X*
:   X coordinate for the placement of the weldment cut-list table; valid only if UserAnchorPoint = False

*Y*
:   Y coordinate for the placement of the weldment cut-list table; valid only if UseAnchorPoint = False

*AnchorType*
:   Anchor type as defined by [swBomConfigurationAnchorType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBOMConfigurationAnchorType_e.html)

*Configuration*
:   Name of the "As Welded" configuration for the weldment cut-list table

*TableTemplate*
:   Path and filename of the template that corresponds to this type of table (see Remarks)

#### Return Value

[Weldment cut-list annotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation.md)

Remarks

The weldment cut-list table template installed with SOLIDWORKS is <*SOLIDWORKS\_*install\_dir>\lang\<language>\**cut list.sldwldtbt**.

Example

[Insert Weldment Cut List Table (VBA)](Insert_Weldment_Cut_List_Table_Example_VB.htm)  
[Insert Weldment Cut List Table (VB.NET)](Insert_Weldment_Cut_List_Table_Example_VBNET.htm)  
[Insert Weldment Cut List Table (C#)](Insert_Weldment_Cut_List_Table_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetKeepLinkedToBOM Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetKeepLinkedToBOM.md)  
[IView::GetKeepLinkedToBOMName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetKeepLinkedToBOMName.md)  
[IView::SetKeepLinkedToBOM Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetKeepLinkedToBOM.md)
