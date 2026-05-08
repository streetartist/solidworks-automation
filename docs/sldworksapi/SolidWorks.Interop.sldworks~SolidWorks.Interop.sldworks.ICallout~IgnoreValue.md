# IgnoreValue Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~IgnoreValue`

Gets or sets whether to ignore the callout value in the given row.
Gets or sets whether to ignore the callout value in the given row.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IgnoreValue( _
   ByVal RowID As System.Integer _
) As System.Boolean
```

```

Dim instance As ICallout
Dim RowID As System.Integer
Dim value As System.Boolean
 
instance.IgnoreValue(RowID) = value
 
value = instance.IgnoreValue(RowID)
```

```

System.bool IgnoreValue( 
   System.int RowID
) {get; set;}
```

```

property System.bool IgnoreValue {
   System.bool get(System.int RowID);
   void set (System.int RowID, System.bool value);
}
```

#### Parameters

*RowID*
:   Index of callout row

#### Property Value

True to ignore callout value, false to not

Remarks

Use this API to remove the white space that remains in the callout when [ICallout::Value](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~Value.md) is set to an empty string.

This property applies only to a callout that is independent of a selection or created with [IModelDocExtension::CreateCallout](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateCallout.md).

Example

[Create a Callout Independent of a Selection (VBA)](Create_a_Callout_Independent_of_a_Selection_Example_VB.htm)  
[Create a Callout Independent of a Selection (VB.NET)](Create_a_Callout_Independent_of_a_Selection_Example_VBNET.htm)  
[Create a Callout Independent of a Selection (C#)](Create_a_Callout_Independent_of_a_Selection_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICallout Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.md)  
[ICallout Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout_members.md)
