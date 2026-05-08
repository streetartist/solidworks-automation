# Text Property (IStatusBarPane)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStatusBarPane~Text`

Gets or sets the text for this pane.
Gets or sets the text for this pane.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Text As System.String
```

```

Dim instance As IStatusBarPane
Dim value As System.String
 
instance.Text = value
 
value = instance.Text
```

```

System.string Text {get; set;}
```

```

property System.String^ Text {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Status bar pane text

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStatusBarPane Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStatusBarPane.md)  
[IStatusBarPane Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStatusBarPane_members.md)
