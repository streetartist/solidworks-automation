# UseLightWeightDefault Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~UseLightWeightDefault`

Gets or sets whether to use the system default lightweight setting.
Gets or sets whether to use the system default lightweight setting.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseLightWeightDefault As System.Boolean
```

```

Dim instance As IDocumentSpecification
Dim value As System.Boolean
 
instance.UseLightWeightDefault = value
 
value = instance.UseLightWeightDefault
```

```

System.bool UseLightWeightDefault {get; set;}
```

```

property System.bool UseLightWeightDefault {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use the system default lightweight setting, false to use [IDocumentSpecification::Lightweight value](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~LightWeight.md)

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
