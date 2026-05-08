# Text Property (IPropertyManagerPageNumberbox)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox~Text`

Gets the text that appears in the number box.
Gets the text that appears in the number box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Text As System.String
```

```

Dim instance As IPropertyManagerPageNumberbox
Dim value As System.String
 
value = instance.Text
```

```

System.string Text {get;}
```

```

property System.String^ Text {
   System.String^ get();
}
```

#### Property Value

Text in number box

Remarks

If a user changes the value in an number box by typing in a new value, the [IPropertyManagerPage2Handler5::OnTextboxChanged](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler5~OnTextboxChanged.md) is called with the current text string and the ID of the number box. You can then use IPropertyManagerPageNumberbox::Text to show the text elsewhere, such as in a callout.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageNumberbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox.md)  
[IPropertyManagerPageNumberbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox_members.md)
