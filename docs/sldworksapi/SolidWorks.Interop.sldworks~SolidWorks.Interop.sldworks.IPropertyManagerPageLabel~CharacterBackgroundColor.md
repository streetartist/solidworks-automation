# CharacterBackgroundColor Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel~CharacterBackgroundColor`

Gets or sets the background color for the specified range of characters in this PropertyManager label.
Gets or sets the background color for the specified range of characters in this PropertyManager label.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CharacterBackgroundColor( _
   ByVal StartChar As System.Short, _
   ByVal EndChar As System.Short _
) As System.Integer
```

```

Dim instance As IPropertyManagerPageLabel
Dim StartChar As System.Short
Dim EndChar As System.Short
Dim value As System.Integer
 
instance.CharacterBackgroundColor(StartChar, EndChar) = value
 
value = instance.CharacterBackgroundColor(StartChar, EndChar)
```

```

System.int CharacterBackgroundColor( 
   System.short StartChar,
   System.short EndChar
) {get; set;}
```

```

property System.int CharacterBackgroundColor {
   System.int get(System.short StartChar, System.short EndChar);
   void set (System.short StartChar, System.short EndChar, System.int value);
}
```

#### Parameters

*StartChar*
:   0-based index value of start character

*EndChar*
:   0-based index value of end character

#### Property Value

RGB value for the text background color for the specified characters; if not specified, then the background color for this control is used

Remarks

You can use a [group box](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup.md) with just a [label](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel.md) to look like a [message box](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~SetMessage3.md) on a PropertyManager page. Set the [background of the group box](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup~BackgroundColor.md) and the background of the label to the same color and the [label text](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel~CharacterColor.md) to a different color. You can also position the group box anywhere on the PropertyManager page.

NOTE: If you want to set the background color of the message box to be the same as the color typically used by SOLIDWORKS for a message box, use [ISldWorks::GetUserPreferenceIntegerValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceIntegerValue.md) swPropertyManagerColorImportantMessage to get the COLORREF value.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageLabel Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel.md)  
[IPropertyManagerPageLabel Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel_members.md)
