# InteractiveAdvancedOpen Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~InteractiveAdvancedOpen`

Gets whether to display an intermediate dialog, which allows the interactive user to set options before opening a document.
Gets whether to display an intermediate dialog, which allows the interactive user to set options before opening a document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property InteractiveAdvancedOpen As System.Boolean
```

```

Dim instance As IDocumentSpecification
Dim value As System.Boolean
 
instance.InteractiveAdvancedOpen = value
 
value = instance.InteractiveAdvancedOpen
```

```

System.bool InteractiveAdvancedOpen {get; set;}
```

```

property System.bool InteractiveAdvancedOpen {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to display an intermediate dialog to the interactive user, false to not (default)

Remarks

This property is not valid for opening **3D**EXPERIENCE files using SOLIDWORKS Connected.

Example

[Open Advanced Dialog On Document Open (VBA)](Open_Advanced_Dialog_On_Open_Example_VB.htm)  
[Open Advanced Dialog On Document Open (VB.NET)](Open_Advanced_Dialog_On_Open_Example_VBNET.htm)  
[Open Advanced Dialog On Document Open (C#)](Open_Advanced_Dialog_On_Open_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.md)  
[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.md)
