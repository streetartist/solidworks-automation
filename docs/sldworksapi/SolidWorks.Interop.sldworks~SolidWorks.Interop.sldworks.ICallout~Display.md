# Display Method (ICallout)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~Display`

Shows or hides the independent (i.e., not attached to a selection) callout.
Shows or hides the independent (i.e., not attached to a selection) callout.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Display( _
   ByVal Display As System.Boolean _
) As System.Boolean
```

```

Dim instance As ICallout
Dim Display As System.Boolean
Dim value As System.Boolean
 
value = instance.Display(Display)
```

```

System.bool Display( 
   System.bool Display
)
```

```

System.bool Display( 
   System.bool Display
) 
```

#### Parameters

*Display*
:   True to show the callout, false to hide it

#### Return Value

True if the operation is successful, false if not

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
