# ValueInactive Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~ValueInactive`

Gets or sets whether the user can edit the value in the specified row in this callout.
Gets or sets whether the user can edit the value in the specified row in this callout.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ValueInactive( _
   ByVal RowID As System.Integer _
) As System.Boolean
```

```

Dim instance As ICallout
Dim RowID As System.Integer
Dim value As System.Boolean
 
instance.ValueInactive(RowID) = value
 
value = instance.ValueInactive(RowID)
```

```

System.bool ValueInactive( 
   System.int RowID
) {get; set;}
```

```

property System.bool ValueInactive {
   System.bool get(System.int RowID);
   void set (System.int RowID, System.bool value);
}
```

#### Parameters

*RowID*
:   Row in callout

#### Property Value

True if the value in this row cannot be modified, false if it can

Example

[Create Multi-row Callouts (VBA)](Create_Multi-row_Callouts_Example_VB.htm)  
[Create a Callout Independent of a Selection (VBA)](Create_a_Callout_Independent_of_a_Selection_Example_VB.htm)  
[Create a Callout Independent of a Selection (VB.NET)](Create_a_Callout_Independent_of_a_Selection_Example_VBNET.htm)  
[Create a Callout Independent of a Selection (C#)](Create_a_Callout_Independent_of_a_Selection_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICallout Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.md)  
[ICallout Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout_members.md)  
[ICallout::Value Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~Value.md)
