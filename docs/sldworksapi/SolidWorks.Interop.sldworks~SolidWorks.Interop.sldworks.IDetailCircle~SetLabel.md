# SetLabel Method (IDetailCircle)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~SetLabel`

Sets the label for this detail circle.
Sets the label for this detail circle.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetLabel( _
   ByVal Label As System.String _
) As System.Boolean
```

```

Dim instance As IDetailCircle
Dim Label As System.String
Dim value As System.Boolean
 
value = instance.SetLabel(Label)
```

```

System.bool SetLabel( 
   System.string Label
)
```

```

System.bool SetLabel( 
   System.String^ Label
) 
```

#### Parameters

*Label*
:   Label for this detail view

#### Return Value

True if label is set, false if not

Remarks

Setting the detail circle label also updates the detail view label.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.md)  
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.md)  
[IDetailCircle::GetLabel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetLabel.md)  
[IDrawingDoc::CreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDetailViewAt3.md)  
[IDrawingDoc::ICreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateDetailViewAt3.md)  
[IDetailCircle::SetLabelPosition Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~SetLabelPosition.md)
