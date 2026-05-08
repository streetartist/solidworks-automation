# Value Property (ICallout)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~Value`

Gets or sets the value in for the specified row in this callout.
Gets or sets the value in for the specified row in this callout.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Value( _
   ByVal RowID As System.Integer _
) As System.String
```

```

Dim instance As ICallout
Dim RowID As System.Integer
Dim value As System.String
 
instance.Value(RowID) = value
 
value = instance.Value(RowID)
```

```

System.string Value( 
   System.int RowID
) {get; set;}
```

```

property System.String^ Value {
   System.String^ get(System.int RowID);
   void set (System.int RowID, System.String^ value);
}
```

#### Parameters

*RowID*
:   Row in callout

#### Property Value

Value

Example

[Create Multi-row Callouts (VBA)](Create_Multi-row_Callouts_Example_VB.htm)  
[Create a Callout Independent of a Selection (C#)](Create_a_Callout_Independent_of_a_Selection_Example_CSharp.htm)  
[Create a Callout Independent of a Selection (VB.NET)](Create_a_Callout_Independent_of_a_Selection_Example_VBNET.htm)  
[Create a Callout Independent of a Selection (VBA)](Create_a_Callout_Independent_of_a_Selection_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICallout Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.md)  
[ICallout Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout_members.md)  
[ICallout::ValueInactive Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~ValueInactive.md)  
[ICallout::TextColor Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~TextColor.md)
