# SkipColon Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~SkipColon`

Gets and sets whether to add a colon at the end of the callout label.
Gets and sets whether to add a colon at the end of the callout label.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SkipColon As System.Boolean
```

```

Dim instance As ICallout
Dim value As System.Boolean
 
instance.SkipColon = value
 
value = instance.SkipColon
```

```

System.bool SkipColon {get; set;}
```

```

property System.bool SkipColon {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

False to add a colon, true to not

Remarks

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
[ICallout::Label2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~Label2.md)
