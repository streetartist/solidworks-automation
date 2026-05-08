# TextBox Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~TextBox`

Gets or sets whether the callout text is enclosed within a box.
Gets or sets whether the callout text is enclosed within a box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TextBox As System.Boolean
```

```

Dim instance As ICallout
Dim value As System.Boolean
 
instance.TextBox = value
 
value = instance.TextBox
```

```

System.bool TextBox {get; set;}
```

```

property System.bool TextBox {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True encloses the callout text in a box, false does not

Remarks

You can only set this property before the callout is shown or while the callout is hidden.

Example

[Create a Callout Independent of a Selection (C#)](Create_a_Callout_Independent_of_a_Selection_Example_CSharp.htm)  
[Create a Callout Independent of a Selection (VB.NET)](Create_a_Callout_Independent_of_a_Selection_Example_VBNET.htm)  
[Create a Callout Independent of a Selection (VBA)](Create_a_Callout_Independent_of_a_Selection_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICallout Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.md)  
[ICallout Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout_members.md)
