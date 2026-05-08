# Style Property (IPropertyManagerPageSelectionbox)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~Style`

Gets or sets style of this selection box.
Gets or sets style of this selection box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Style As System.Integer
```

```

Dim instance As IPropertyManagerPageSelectionbox
Dim value As System.Integer
 
instance.Style = value
 
value = instance.Style
```

```

System.int Style {get; set;}
```

```

property System.int Style {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Style as defined in [swPropMgrPageSelectionboxStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropMgrPageSelectionBoxStyle_e.html)

Remarks

You must set this property before the PropertyManager page is displayed.

For a selection list to automatically have a horizontal scroll bar if the text is wider than the selection box, set this property's style to swPropMgrPageSelectionBoxStyle\_HScroll.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.md)  
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.md)
