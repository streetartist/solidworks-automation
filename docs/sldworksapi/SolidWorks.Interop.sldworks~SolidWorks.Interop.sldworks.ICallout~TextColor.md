# TextColor Property (ICallout)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~TextColor`

Gets or sets the color of the text in the specified row in this callout.
Gets or sets the color of the text in the specified row in this callout.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TextColor( _
   ByVal RowID As System.Integer _
) As System.Integer
```

```

Dim instance As ICallout
Dim RowID As System.Integer
Dim value As System.Integer
 
instance.TextColor(RowID) = value
 
value = instance.TextColor(RowID)
```

```

System.int TextColor( 
   System.int RowID
) {get; set;}
```

```

property System.int TextColor {
   System.int get(System.int RowID);
   void set (System.int RowID, System.int value);
}
```

#### Parameters

*RowID*
:   Row in callout

#### Property Value

[System color](ms-help://SolidWorks.Interop.swconst/SolidWorks/SO_Colors.htm)

Remarks

You must use a system color; you cannot use any other RGB values. To see system colors, click Tools > Options > Colors in the SOLIDWORKS user interface.

Example

[Create Multi-row Callouts (VBA)](Create_Multi-row_Callouts_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICallout Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.md)  
[ICallout Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout_members.md)  
[ICallout::OpaqueColor Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~OpaqueColor.md)
