# Callout Property (IPropertyManagerPageSelectionbox)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~Callout`

Gets or sets a multi-row, editable callout for this selection box.
Gets or sets a multi-row, editable callout for this selection box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Callout As Callout
```

```

Dim instance As IPropertyManagerPageSelectionbox
Dim value As Callout
 
instance.Callout = value
 
value = instance.Callout
```

```

Callout Callout {get; set;}
```

```

property Callout^ Callout {
   Callout^ get();
   void set (    Callout^ value);
}
```

#### Property Value

[Callout](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.md) for this selection box

Remarks

This property returns NULL if callouts are not enabled for this selection box. Use [IPropertyManagerPageSelectionbox::SetCalloutLabel](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~SetCalloutLabel.md) to enable the default callouts.

To create callouts for selection boxes:

1. Use [ISelectionManager::CreateCallout2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~CreateCallout2.md) to create the basic callout information.
2. Use the [ICallout](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.md) interface to modify the look and of the callout.
3. Use ISelectionBox::Callout to set the callout information for the selection box.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.md)  
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.md)
