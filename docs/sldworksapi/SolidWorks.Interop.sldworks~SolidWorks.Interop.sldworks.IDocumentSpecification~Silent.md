# Silent Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~Silent`

Gets or sets whether to open the model document silently.
Gets or sets whether to open the model document silently.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Silent As System.Boolean
```

```

Dim instance As IDocumentSpecification
Dim value As System.Boolean
 
instance.Silent = value
 
value = instance.Silent
```

```

System.bool Silent {get; set;}
```

```

property System.bool Silent {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to open the model document silently, false to not

Remarks

The software uses the last-displayed configuration if it discovers missing configurations or component references. No warnings or errors display if this property is set to true.

Example

[Get Whether Components Are Loaded (C#)](Get_Whether_Components_Are_Loaded_Example_CSharp.htm)  
[Get Whether Components Are Loaded (VB.NET)](Get_Whether_Components_Are_Loaded_Example_VBNET.htm)  
[Get Whether Components Are Loaded (VBA)](Get_Whether_Components_Are_Loaded_Example_VB.htm)  
[Open Assembly Document (C#)](Open_Assembly_Document_Example_CSharp.htm)  
[Open Assembly Document (VB.NET)](Open_Assembly_Document_Example_VBNET.htm)  
[Open Assembly Document (VBA)](Open_Assembly_Document_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.md)  
[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.md)  
[IDocumentSpecification::AutoRepair Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~AutoRepair.md)  
[IDocumentSpecification::CriticalDataRepair Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~CriticalDataRepair.md)
