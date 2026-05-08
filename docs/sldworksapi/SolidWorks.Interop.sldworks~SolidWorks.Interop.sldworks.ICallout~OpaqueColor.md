# OpaqueColor Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~OpaqueColor`

Gets or sets the opaque (background) color for the labels for this callout.
Gets or sets the opaque (background) color for the labels for this callout.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property OpaqueColor As System.Integer
```

```

Dim instance As ICallout
Dim value As System.Integer
 
instance.OpaqueColor = value
 
value = instance.OpaqueColor
```

```

System.int OpaqueColor {get; set;}
```

```

property System.int OpaqueColor {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

[System color](ms-help://SolidWorks.Interop.swconst/SolidWorks/SO_Colors.htm)

Remarks

You must use a system color; you cannot use any other RGB values. To see system colors, click **Tools >** **Options >** **Colors** in the SOLIDWORKS user interface.

Example

[Create Multi-row Callouts (VBA)](Create_Multi-row_Callouts_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICallout Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.md)  
[ICallout Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout_members.md)  
[ICallout::TextColor Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~TextColor.md)
