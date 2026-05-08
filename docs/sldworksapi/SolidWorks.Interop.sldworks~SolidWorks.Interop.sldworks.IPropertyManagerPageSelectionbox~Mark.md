# Mark Property (IPropertyManagerPageSelectionbox)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~Mark`

Gets or sets the mark used on selected items in this selection box.
Gets or sets the mark used on selected items in this selection box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Mark As System.Integer
```

```

Dim instance As IPropertyManagerPageSelectionbox
Dim value As System.Integer
 
instance.Mark = value
 
value = instance.Mark
```

```

System.int Mark {get; set;}
```

```

property System.int Mark {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Number to use as a mark; this number is used by methods or properties that require ordered entity selection

Remarks

You can only use this method to set properties on the PropertyManager page before it is displayed or while it is closed. See [IPropertyManagerPage2::Show2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Show2.md) and [IPropertyManagerPage2::Close](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Close.md).

It is easiest to use the Mark property as a read-only property. If this property is not set before the PropertyManager is shown, then the Mark value is automatically set. Once the PropertyManager page is displayed, then the application can query the Mark for its value.

If the application must rely on specific mark values for specific selection boxes, then the set the Mark value before the PropertyManager page is shown. In this case, ensure that each selection box contains a different value. Otherwise, the user's selection is displayed in the selection boxes that have the same Mark value.

Mark values (whether set by the SOLIDWORKS application or by your application) must be powers of two (for example, 1, 2, 4, 8).

Example

[Select Multiple Objects for Selection Boxes (C#)](Select_Multiple_Objects_for_Selection_Boxes_Example_CSharp.htm)  
[Select Multiple Objects for Selection Boxes (VB.NET)](Select_Multiple_Objects_for_Selection_Boxes_Example_VBNET.htm)  
[Select Multiple Objects for Selection Boxes (VBA)](Select_Multiple_Objects_for_Selection_Boxes_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.md)  
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.md)
