# BackgroundColor Property (IPropertyManagerPageGroup)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup~BackgroundColor`

Gets or sets the background color of this PropertyManager group box.
Gets or sets the background color of this PropertyManager group box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BackgroundColor As System.Integer
```

```

Dim instance As IPropertyManagerPageGroup
Dim value As System.Integer
 
instance.BackgroundColor = value
 
value = instance.BackgroundColor
```

```

System.int BackgroundColor {get; set;}
```

```

property System.int BackgroundColor {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

COLORREF value

Remarks

You can use a group box with just a [label](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel.md) to look like a [message box](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~SetMessage3.md) on a PropertyManager page. Set the background of the group box and the [background of the label](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl~BackgroundColor.md) to the same color and the [label text](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel~CharacterColor.md) to a different color. You can also position the group box anywhere on the PropertyManager page.

NOTE: If you want to set the background color of the message box to be the same as the color typically used by SOLIDWORKS for a message box, use [ISldWorks::GetUserPreferenceIntegerValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceIntegerValue.md) swPropertyManagerColorImportantMessage to get the COLORREF value.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup.md)  
[IPropertyManagerPageGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup_members.md)
